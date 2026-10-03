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
