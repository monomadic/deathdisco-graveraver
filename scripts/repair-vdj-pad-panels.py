#!/usr/bin/env python3
"""
Reset this skin's VirtualDJ pad panel state without touching other settings.

VirtualDJ keeps skin panel selections in one comma-separated <skinPanels> value.
After pad/layout refactors, removed panel names can linger there and win over
the current XML defaults. This helper removes only the pad panel selectors that
belong to this skin: current pad selectors, plus known legacy variants that the
repo no longer defines.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SKIN_XML = REPO_ROOT / "src/skin.xml"
DEFAULT_SETTINGS = (
    Path.home() / "Library/Application Support/VirtualDJ/settings.xml"
)

PANELNAME_EXPANSIONS = (
    "deck1",
    "deck2",
    "deck3",
    "deck4",
    "[PANELNAME]",
)

# These existed in older pad/layout iterations and can survive in settings.xml.
# They are intentionally narrow so similarly named panels from other skins are
# left alone.
LEGACY_PAD_PANEL_TEMPLATES = (
    "@pads_[PANELNAME]",
    "@pads2_[PANELNAME]",
    "@pads3_[PANELNAME]",
    "@padsbtns2_[PANELNAME]",
    "@pads_16_btns_[PANELNAME]",
    "@hotcuesx16_[PANELNAME]",
)


def strip_xml_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def panel_id(token: str) -> str:
    return token.strip().lstrip("!")


def expand_panelname(name: str) -> set[str]:
    names = {name}
    if "[PANELNAME]" in name:
        names.update(name.replace("[PANELNAME]", value) for value in PANELNAME_EXPANSIONS)
    return names


def current_pad_panels(skin_xml: Path) -> set[str]:
    try:
        xml = subprocess.check_output(
            ["xmllint", "--xinclude", "--loaddtd", "--noent", str(skin_xml)],
            text=True,
            cwd=REPO_ROOT,
        )
    except (FileNotFoundError, subprocess.CalledProcessError) as exc:
        raise SystemExit(f"Could not expand {skin_xml}: {exc}") from exc

    xml = strip_xml_comments(xml)
    current: set[str] = set()

    for match in re.finditer(r"<panel\b(?P<attrs>[^>]*)>", xml):
        attrs = match.group("attrs")
        name_match = re.search(r'\bname="([^"]+)"', attrs)
        group_match = re.search(r'\bgroup="([^"]+)"', attrs)
        name = name_match.group(1) if name_match else ""
        group = group_match.group(1) if group_match else ""

        is_pad_panel = (
            "pad" in name.lower()
            or "hotcuesx" in name.lower()
            or group.startswith("pads16")
            or group.startswith("pad_area")
        )
        if name and is_pad_panel:
            current.update(expand_panelname(name))

    return current


def legacy_pad_panels() -> set[str]:
    panels: set[str] = set()
    for template in LEGACY_PAD_PANEL_TEMPLATES:
        panels.update(expand_panelname(template))
    return panels


def read_skin_panels(settings_text: str) -> tuple[re.Match[str], list[str]]:
    match = re.search(r"(?s)<skinPanels>(.*?)</skinPanels>", settings_text)
    if not match:
        raise SystemExit("No <skinPanels> entry found in settings.xml")

    tokens = [token.strip() for token in match.group(1).split(",") if token.strip()]
    return match, tokens


def repair_tokens(tokens: list[str], removable_panels: set[str]) -> tuple[list[str], list[str]]:
    kept: list[str] = []
    removed: list[str] = []

    for token in tokens:
        if panel_id(token) in removable_panels:
            removed.append(token)
        else:
            kept.append(token)

    return kept, removed


def write_settings(settings: Path, original: str, match: re.Match[str], tokens: list[str]) -> Path:
    backup = settings.with_suffix(
        settings.suffix + f".pad-panels-{datetime.now():%Y%m%d-%H%M%S}.bak"
    )
    shutil.copy2(settings, backup)

    replacement = f"<skinPanels>{', '.join(tokens)}</skinPanels>"
    repaired = original[: match.start()] + replacement + original[match.end() :]
    settings.write_text(repaired, encoding="utf-8")

    return backup


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--settings",
        type=Path,
        default=DEFAULT_SETTINGS,
        help=f"VirtualDJ settings.xml path (default: {DEFAULT_SETTINGS})",
    )
    parser.add_argument(
        "--skin-xml",
        type=Path,
        default=DEFAULT_SKIN_XML,
        help=f"Skin XML entrypoint (default: {DEFAULT_SKIN_XML})",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="write the repaired settings.xml after creating a timestamped backup",
    )
    args = parser.parse_args(argv)

    if not args.settings.exists():
        raise SystemExit(f"Settings file not found: {args.settings}")

    current = current_pad_panels(args.skin_xml)
    legacy = legacy_pad_panels()
    removable = current | legacy

    original = args.settings.read_text(encoding="utf-8")
    match, tokens = read_skin_panels(original)
    kept, removed = repair_tokens(tokens, removable)

    stale_removed = sorted({panel_id(token) for token in removed if panel_id(token) in legacy})
    current_reset = sorted({panel_id(token) for token in removed if panel_id(token) in current})

    print(f"Current pad panel names found in skin XML: {len(current)}")
    print(f"Known legacy pad panel names checked: {len(legacy)}")
    print(f"Pad panel selectors to remove from settings: {len(removed)}")

    if stale_removed:
        print("\nLegacy/stale selectors found:")
        for name in stale_removed:
            print(f"  {name}")

    if current_reset:
        print("\nCurrent pad selectors that will reset to XML defaults:")
        for name in current_reset:
            print(f"  {name}")

    if not removed:
        print("\nNo pad panel selectors needed repair.")
        return 0

    if not args.apply:
        print("\nDry run only. Re-run with --apply to update settings.xml.")
        return 0

    backup = write_settings(args.settings, original, match, kept)
    print(f"\nUpdated {args.settings}")
    print(f"Backup written to {backup}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
