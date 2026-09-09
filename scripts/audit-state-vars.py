#!/usr/bin/env python3
"""Check that concrete skin variables are registered and skin modes are valid."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
REGISTRY = ROOT / "docs" / "STATE.md"

COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
VARIABLE_RE = re.compile(r"@\$?[A-Za-z0-9_]+")
REGISTRY_ROW_RE = re.compile(r"^\|\s*`(@\$?[A-Za-z0-9_]+)`\s*\|", re.MULTILINE)
SKIN_MODE_RE = re.compile(
    r"(?:set|var_(?:equal|not_equal))\s+'@\$dd_skin_mode'\s+(-?\d+)"
)
ALLOWED_SKIN_MODES = {0, 1, 2}
ATTR_RE = re.compile(r'\b([a-z_0-9]+)="([^"]*)"')
WRITER_RE = re.compile(r"\b(?:set|toggle|cycle)\s+'(@\$?[A-Za-z0-9_]+)'")


def source_variables() -> set[str]:
    variables: set[str] = set()
    for path in sorted(SRC.rglob("*.xml")):
        text = COMMENT_RE.sub("", path.read_text())
        for match in VARIABLE_RE.finditer(text):
            # Dynamic panel names such as @pads16_[PANELNAME] are not variables.
            if match.end() < len(text) and text[match.end()] == "[":
                continue
            variables.add(match.group())
    return variables


def registry_variables() -> set[str]:
    return set(REGISTRY_ROW_RE.findall(REGISTRY.read_text()))


def used_skin_modes() -> set[int]:
    modes: set[int] = set()
    for path in sorted(SRC.rglob("*.xml")):
        text = COMMENT_RE.sub("", path.read_text())
        modes.update(int(value) for value in SKIN_MODE_RE.findall(text))
    return modes


def condition_variables() -> set[str]:
    """Variables read by any condition="" attribute (evaluated only at load)."""
    variables: set[str] = set()
    for path in sorted(SRC.rglob("*.xml")):
        text = COMMENT_RE.sub("", path.read_text())
        for name, value in ATTR_RE.findall(text):
            if name == "condition":
                variables.update(VARIABLE_RE.findall(value))
    return variables


def writers_without_reload(structural: set[str]) -> list[str]:
    """Writers of a condition-read variable whose action chain never reloads."""
    findings: list[str] = []
    for path in sorted(SRC.rglob("*.xml")):
        text = COMMENT_RE.sub("", path.read_text())
        for line_no, line in enumerate(text.splitlines(), 1):
            for name, value in ATTR_RE.findall(line):
                if name == "condition" or "load_skin" in value:
                    continue
                written = {v for v in WRITER_RE.findall(value) if v in structural}
                for variable in sorted(written):
                    findings.append(
                        f"  {path.relative_to(ROOT)}:{line_no} writes {variable} "
                        f"in {name}=\"\" without load_skin"
                    )
    return findings


def main() -> int:
    source = source_variables()
    registry = registry_variables()
    missing = sorted(source - registry)
    stale = sorted(registry - source)
    modes = used_skin_modes()
    unsupported_modes = sorted(modes - ALLOWED_SKIN_MODES)

    findings: list[str] = []
    unreloaded = writers_without_reload(condition_variables())
    if unreloaded:
        findings.append(
            "Writers of condition-read variables that do not reload the skin:"
        )
        findings.extend(unreloaded)
    if missing:
        findings.append("Unregistered skin variables:")
        findings.extend(f"  {name}" for name in missing)
    if stale:
        findings.append("Registered variables no longer referenced by XML:")
        findings.extend(f"  {name}" for name in stale)
    if unsupported_modes:
        findings.append(
            "Unsupported @$dd_skin_mode values (supported: 0=Pro, 1=Performance, 2=Stack):"
        )
        findings.extend(f"  {mode}" for mode in unsupported_modes)

    if findings:
        print("State audit failed:")
        print("\n".join(findings))
        return 1

    mode_list = ", ".join(str(mode) for mode in sorted(modes))
    print(
        f"State audit passed: {len(source)} registered variables; "
        f"@$dd_skin_mode values: {mode_list}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
