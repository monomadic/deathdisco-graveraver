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
    r"(?:set|var_(?:equal|not_equal))\s+'@\$skin_mode'\s+(-?\d+)"
)
ALLOWED_SKIN_MODES = {0, 1, 2}


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


def main() -> int:
    source = source_variables()
    registry = registry_variables()
    missing = sorted(source - registry)
    stale = sorted(registry - source)
    modes = used_skin_modes()
    unsupported_modes = sorted(modes - ALLOWED_SKIN_MODES)

    findings: list[str] = []
    if missing:
        findings.append("Unregistered skin variables:")
        findings.extend(f"  {name}" for name in missing)
    if stale:
        findings.append("Registered variables no longer referenced by XML:")
        findings.extend(f"  {name}" for name in stale)
    if unsupported_modes:
        findings.append(
            "Unsupported @$skin_mode values (supported: 0=Pro, 1=Performance, 2=Stack):"
        )
        findings.extend(f"  {mode}" for mode in unsupported_modes)

    if findings:
        print("State audit failed:")
        print("\n".join(findings))
        return 1

    mode_list = ", ".join(str(mode) for mode in sorted(modes))
    print(
        f"State audit passed: {len(source)} registered variables; "
        f"@$skin_mode values: {mode_list}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
