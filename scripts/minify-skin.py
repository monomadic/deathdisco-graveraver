#!/usr/bin/env python3
"""
Minifies a built skin XML file in-place.

Strips XML comments and whitespace-only text nodes. Attribute values and
text content are left untouched — VirtualDJ uses attributes for everything
meaningful, so this is safe.
"""

import sys
import xml.etree.ElementTree as ET
from os import getpid
from pathlib import Path


def strip_comments(element):
    """Remove all comment nodes recursively (ET represents them as tag=callable)."""
    for child in list(element):
        if callable(child.tag):
            element.remove(child)
        else:
            strip_comments(child)


def collapse_whitespace(element):
    """Drop whitespace-only text and tail content."""
    if element.text and not element.text.strip():
        element.text = None
    if element.tail and not element.tail.strip():
        element.tail = None
    for child in element:
        collapse_whitespace(child)


def minify(path: Path):
    before = path.stat().st_size

    # Parse preserving comments so we can drop them
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    tree = ET.parse(path, parser=parser)
    root = tree.getroot()

    strip_comments(root)
    collapse_whitespace(root)

    ET.indent(root, space="")  # compact, no indentation

    output = ET.tostring(root, encoding="unicode", xml_declaration=True)
    tmp_path = path.with_name(f".{path.name}.{getpid()}.tmp")
    try:
        tmp_path.write_text(output, encoding="utf-8")
        tmp_path.replace(path)
    finally:
        tmp_path.unlink(missing_ok=True)

    after = path.stat().st_size
    pct = 100 * (1 - after / before)
    print(f"Minified {path.name}: {before:,} → {after:,} bytes ({pct:.0f}% smaller)")


if __name__ == "__main__":
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("build/skin.xml")
    minify(path)
