"""Check state coverage and geometric relationships, not just file freshness."""

import ast
import contextlib
import importlib.util
import io
from itertools import product
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
with patch.object(sys, "path", [str(SCRIPTS), *sys.path]):
    spec = importlib.util.spec_from_file_location("browser_generator", SCRIPTS / "gen-browser-positions.py")
    generator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(generator)


def arithmetic(expression, height, trim=0):
    expression = expression.replace("[HEIGHT]", str(height)).replace("[BOTTOM_TRIM]", str(trim))
    tree = ast.parse(expression, mode="eval")

    def value(node):
        if isinstance(node, ast.Constant) and type(node.value) is int:
            return node.value
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.UAdd):
            return value(node.operand)
        if isinstance(node, ast.BinOp) and isinstance(node.op, (ast.Add, ast.Sub)):
            return value(node.left) + (1 if isinstance(node.op, ast.Add) else -1) * value(node.right)
        raise AssertionError(f"Unsupported geometry expression: {expression}")

    return value(tree.body)


def selected(positions, active, wave):
    for pos in positions:
        checks = re.findall(r"var_equal '(@\$dd_\w+)' (\d+)", pos.get("condition", ""))
        state = {"@$dd_wave_size": wave, **{f"@$dd_show_{rack}_rack": int(rack in active)
                                           for rack in ("fx", "mixer", "video")}}
        if all(state[name] == int(expected) for name, expected in checks):
            return pos
    raise AssertionError("Missing geometry state")


class GeometryTests(unittest.TestCase):
    def test_waveform_ladder_boundaries_and_coverage(self):
        nodes = ET.fromstring(generator.generate_waveforms()).findall("define/panel")
        self.assertEqual(len(nodes), 14)
        for wave in range(14):
            self.assertEqual(int(selected(nodes, set(), wave).get("waveformheight")), 121 + 20 * wave)
        self.assertEqual(nodes[0].get("waveformheight"), "381")
        self.assertEqual(nodes[-1].get("waveformheight"), "121")

    def test_every_rack_combination_preserves_browser_bottom(self):
        surfaces = list(ET.fromstring(generator.generate())) + list(ET.fromstring(generator.generate_stack()))
        for surface in surfaces:
            positions = surface.findall("browser/pos")
            wave_only = surface.get("class") == "BROWSER_SURFACE_PRO"
            self.assertEqual(len(positions), 14 if wave_only else (8 if "STACK" in surface.get("class") else 112))
            for wave, flags in product(range(14), product((False, True), repeat=3)):
                active = {rack for rack, enabled in zip(("fx", "mixer", "video"), flags) if enabled}
                # Independent reference dimensions catch wrong ordering as well
                # as mismatched offsets and heights in any generated surface.
                consumed = sum({"fx": 82, "mixer": 88, "video": 142}[rack] for rack in active)
                if wave_only:
                    consumed = 0
                baseline = selected(positions, set(), wave)
                actual = selected(positions, active, wave)
                with self.subTest(surface=surface.get("class"), wave=wave, racks=active):
                    y0 = arithmetic(baseline.get("y"), 1075, 568)
                    h0 = arithmetic(baseline.get("height"), 1075, 568)
                    y = arithmetic(actual.get("y"), 1075, 568)
                    h = arithmetic(actual.get("height"), 1075, 568)
                    self.assertEqual(y - y0, consumed)
                    self.assertEqual(h0 - h, consumed)
                    self.assertEqual(y + h, y0 + h0)

    def test_rack_fit_guard_matches_surface_geometry(self):
        """The toggle guard says yes exactly when the generated browser keeps its minimum."""
        geometry = generator.rack_fit_script.__globals__
        minimum = geometry["BROWSER_MIN_HEIGHT"]
        surface = next(s for s in ET.fromstring(generator.generate()) if s.get("class") == "BROWSER_PERFORMANCE_SURFACE")
        positions = surface.findall("browser/pos")
        for height, trim, available in ((1075, 568, geometry["PRO_MIXER_BROWSER"]),
                                        (1080 - 60 - 2 - 2 - 2 - 1 - 50, 344, geometry["PRO_EXTENDED_BROWSER"])):
            for flags in product((False, True), repeat=3):
                active = {rack for rack, on in zip(("fx", "mixer", "video"), flags) if on}
                for rack in active:
                    limit = geometry["rack_fit_limit"](available, True, tuple(active))
                    for wave in range(14):
                        browser = arithmetic(selected(positions, active, wave).get("height"), height, trim)
                        fits = limit is None or wave < limit
                        with self.subTest(height=height, racks=active, wave=wave):
                            self.assertEqual(fits, browser >= minimum, f"browser={browser}")
        self.assertEqual(geometry["rack_fit_limit"](geometry["PERFORMANCE_4DECK_BROWSER"], False, ("fx", "mixer")), None)
        self.assertEqual(geometry["rack_fit_limit"](geometry["PERFORMANCE_4DECK_BROWSER"], False, ("fx", "video")), 0)
        self.assertEqual(arithmetic("1080-43-2-333-2-2-333-2-50", 0), geometry["PERFORMANCE_4DECK_BROWSER"])

    def test_rack_toggle_scripts_reload_and_negate(self):
        toggles = ET.fromstring(generator.generate_rack_toggles())
        buttons = toggles.findall(".//button")
        self.assertEqual(len(buttons), 6)
        live = [b for b in buttons if b.get("action") != "nothing"]
        self.assertEqual([b.get("query") for b in live],
                         ["var '@$dd_show_mixer_rack'", "var '@$dd_show_video_rack'", "var '@$dd_show_fx_rack'"])
        for button in live:
            action = button.get("action")
            self.assertNotIn("&&", action)
            self.assertNotIn("toggle", action)
            for branch in re.split(r" : | \? ", action):
                if "set '" in branch:
                    self.assertTrue(branch.strip().endswith("load_skin"), branch)
        for rack in ("fx", "mixer", "video"):
            yes = generator.rack_fit_script(rack, single=True, yes="GO", no="STOP")
            self.assertNotIn("true", yes)
            # every leaf is an action or `nothing`, never a bare query feeding a later `?`
            for branch in re.split(r" \? | : ", yes):
                self.assertTrue(branch.startswith(("var_", "GO", "STOP")), branch)
            self.assertTrue(yes.endswith(" : GO"))
        action = live[2].get("action")  # fx
        self.assertIn("var_smaller '@$dd_wave_size' 10 ? set '@$dd_show_fx_rack' 1 & set '@$dd_show_mixer_rack' 0 & set '@$dd_show_video_rack' 0 & load_skin : nothing", action)

    def test_vu_meter_ladders(self):
        root = ET.fromstring(generator.generate_vu_meters())
        specs = generator.VU_METERS
        self.assertEqual([d.get("class") for d in root], list(specs))
        for define in root:
            spec = specs[define.get("class")]
            visuals = define.findall("visual")
            self.assertEqual(len(visuals), 2)
            for visual in visuals:
                leds = visual.findall("led")
                self.assertEqual(len(leds), spec["leds"])
                self.assertEqual(int(visual.get("height")), (spec["leds"] - 1) * 6 + 4)
                colors = [led.find("on").get("color") for led in reversed(leds)]  # bottom first
                if "1" in visual.get("visibility"):
                    self.assertEqual(colors[:spec["red"]], ["red_vu"] * spec["red"])
                    self.assertEqual(colors[spec["red"]:spec["red"] + spec["orange"]], ["orange_vu"] * spec["orange"])
                    self.assertTrue(all(c == "green_vu" for c in colors[spec["red"] + spec["orange"]:]))
                else:
                    self.assertEqual(colors[:spec["needle"]], ["needle"] * spec["needle"])
                    self.assertTrue(all(c == "deckcolor" for c in colors[spec["needle"]:]))
            self.assertEqual(define.find("slider/pos").get("height"), visuals[0].get("height"))

    def test_check_is_read_only_and_catches_each_output(self):
        with tempfile.TemporaryDirectory() as directory:
            outputs = {Path(directory) / p.name: text for p, text in generator.generated_files().items()}
            with patch.object(generator, "generated_files", return_value=outputs), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(generator.main([]), 0)
                self.assertEqual(generator.main(["--check"]), 0)
                for path, original in outputs.items():
                    path.write_text("stale")
                    self.assertEqual(generator.main(["--check"]), 1)
                    self.assertEqual(path.read_text(), "stale")
                    path.unlink()
                    self.assertEqual(generator.main(["--check"]), 1)
                    self.assertFalse(path.exists())
                    path.write_text(original)


if __name__ == "__main__":
    unittest.main()
