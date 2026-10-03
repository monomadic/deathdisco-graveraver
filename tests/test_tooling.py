"""Small regression fixtures; never read or write live VirtualDJ settings."""

import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parent.parent


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


state = load_script("audit-state-vars")
macros = load_script("expand-skin-macros")
VARIABLE = "@$dd_skin_mode"


class ReloadAuditTests(unittest.TestCase):
    def test_rejects_unreloaded_branches_and_misleading_text(self):
        for action in [
            "loaded ? set '@$dd_skin_mode' 1 : load_skin",
            "loaded ? load_skin : toggle '@$dd_skin_mode'",
            "load_skin & set '@$dd_skin_mode' 1",
            "deck 1 set '@$dd_skin_mode' 1",
            "set '@$dd_skin_mode' 1 & get_text 'load_skin'",
            "set '@$dd_skin_mode' 1 & load_skin_extra",
            "set '@$dd_skin_mode' 1 & loaded ? load_skin : nothing",
        ]:
            with self.subTest(action=action):
                self.assertEqual(state.unreloaded_writes(action, {VARIABLE}), {VARIABLE})

    def test_accepts_explicit_reload_in_each_branch(self):
        for action in [
            "set '@$dd_skin_mode' 1 & load_skin",
            "toggle '@$dd_skin_mode' && load_skin",
            "loaded ? set '@$dd_skin_mode' 1 & load_skin : nothing",
            "loaded ? toggle '@$dd_skin_mode' & load_skin : cycle '@$dd_skin_mode' 3 & load_skin",
            "loaded ? play ? set '@$dd_skin_mode' 1 & load_skin : nothing : nothing",
            "get_text \"set '@$dd_skin_mode' 1 ? :\"",
        ]:
            with self.subTest(action=action):
                self.assertEqual(state.unreloaded_writes(action, {VARIABLE}), set())

    def test_xml_formatting_comments_and_line_numbers(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "skin.xml").write_text('''<skin>
<!-- A multiline comment
     must not shift diagnostic line numbers. -->
<group condition="var_equal '@$dd_skin_mode' 0"/>
<button action='
set "@$dd_skin_mode" 1
'/>
</skin>''')
            with patch.object(state, "ROOT", root), patch.object(state, "SRC", root):
                self.assertEqual(state.condition_variables(), {VARIABLE})
                findings = state.writers_without_reload({VARIABLE})
                self.assertEqual(len(findings), 1)
                self.assertIn("skin.xml:5", findings[0])


class MacroTests(unittest.TestCase):
    def expand(self, xml):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "skin.xml"
            path.write_text(xml)
            with contextlib.redirect_stdout(io.StringIO()):
                macros.main(path)
            return ET.parse(path).getroot()

    def test_typo_rejected_without_rewriting_input(self):
        xml = '''<skin><define class="M" macro="true" placeholders="height">
<visual height="[HIEGHT]"/></define><group class="m" height="20"/></skin>'''
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "skin.xml"
            path.write_text(xml)
            with self.assertRaisesRegex(SystemExit, "undeclared placeholders HIEGHT"):
                macros.main(path)
            self.assertEqual(path.read_text(), xml)

    def test_nested_macros_preserve_runtime_tokens_and_wrapper(self):
        root = self.expand('''<skin>
<define class="INNER" macro="true" placeholders="height,width=10">
<visual height="[HEIGHT]" width="[WIDTH]"/></define>
<define class="OUTER" macro="true" placeholders="size">
<group class="inner" height="[SIZE]"/></define>
<define class="RUNTIME" placeholders="height">
<group class="outer" size="[HEIGHT]" visibility="loaded"/></define>
</skin>''')
        self.assertEqual(len(root.findall("define")), 1)
        wrapper = root.find("define/group")
        self.assertEqual(wrapper.attrib, {"visibility": "loaded"})
        self.assertEqual(wrapper.find("visual").attrib, {"height": "[HEIGHT]", "width": "10"})

    def test_caller_tokens_are_not_substituted_twice(self):
        root = self.expand('''<skin>
<define class="M" macro="true" placeholders="height,width">
<visual height="[HEIGHT]" width="[WIDTH]"/></define>
<define class="RUNTIME" placeholders="width">
<group class="m" height="[WIDTH]" width="10"/></define></skin>''')
        self.assertEqual(root.find("define/visual").attrib,
                         {"height": "[WIDTH]", "width": "10"})

    def test_required_input_still_enforced(self):
        with self.assertRaisesRegex(SystemExit, "missing required placeholder"):
            self.expand('''<skin><define class="M" macro="true" placeholders="height">
<visual height="[HEIGHT]"/></define><group class="m"/></skin>''')


if __name__ == "__main__":
    unittest.main()
