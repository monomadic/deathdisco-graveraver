#!/usr/bin/env python3
"""
Expands macro-marked defines in a built skin XML file in-place.

Defines carrying macro="true" are build-time templates, not VirtualDJ
runtime classes: every element referencing one (lowercase class name) is
given the define's children with [PLACEHOLDER] tokens substituted, and the
defines themselves are removed, so VirtualDJ only ever sees plain expanded
XML. This keeps the source parameterized without depending on VirtualDJ's
own define/placeholder engine.

Expansion rules:
  - Placeholder values come from same-named attributes on the referencing
    element (consumed), falling back to defaults declared as name=value in
    the define's placeholders list.
  - Remaining attributes (name, condition, visibility, ...) stay on the
    referencing element.
  - An attribute-free <group> wrapper is flattened away entirely.
  - Expansion is repeated so macro bodies may reference other macros.
"""

import sys
import re
import xml.etree.ElementTree as ET
from copy import deepcopy
from os import getpid
from pathlib import Path


PLACEHOLDER_RE = re.compile(r"\[([A-Z][A-Z0-9_]*)\]")


def collect_macros(element, macros):
    for child in list(element):
        if child.tag == "define" and child.get("macro") == "true":
            spec = {}
            for item in filter(None, child.get("placeholders", "").split(",")):
                name, eq, default = item.partition("=")
                spec[name.lstrip("*")] = default if eq else None
            # Validate template-owned tokens before inserting caller values.
            # Values such as [HEIGHT] passed by an enclosing runtime define are
            # deliberately preserved, even if that token is not a macro input.
            declared = {name.upper() for name in spec}
            used = {token for node in child.iter() for value in node.attrib.values()
                    for token in PLACEHOLDER_RE.findall(value)}
            unknown = used - declared
            if unknown:
                raise SystemExit(
                    f"macro {child.get('class')}: undeclared placeholders "
                    + ", ".join(sorted(unknown)))
            macros[child.get("class").lower()] = (spec, list(child))
            element.remove(child)
        else:
            collect_macros(child, macros)


def substitute(element, values):
    replacements = {name.upper(): value for name, value in values.items()}
    for key, value in element.attrib.items():
        # One pass prevents caller-owned tokens from being substituted again
        # when their names happen to overlap another macro parameter.
        value = PLACEHOLDER_RE.sub(
            lambda match: replacements.get(match[1], match[0]), value)
        element.set(key, value)
    for child in element:
        substitute(child, values)


def expand(element, macros):
    changed = False
    new_children = []
    for child in list(element):
        changed |= expand(child, macros)
        cls = child.get("class", "")
        if cls in macros:
            spec, body = macros[cls]
            values = {}
            for name, default in spec.items():
                value = child.attrib.pop(name, default)
                if value is None:
                    raise SystemExit(
                        f"macro {cls}: missing required placeholder {name!r}")
                values[name] = value
            expansion = [deepcopy(node) for node in body]
            for node in expansion:
                substitute(node, values)
            del child.attrib["class"]
            changed = True
            if child.tag == "group" and not child.attrib:
                new_children.extend(expansion)
                continue
            child.extend(expansion)
        new_children.append(child)
    element[:] = new_children
    return changed


def main(path: Path):
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    tree = ET.parse(path, parser=parser)
    root = tree.getroot()

    macros = {}
    collect_macros(root, macros)
    rounds = 0
    while expand(root, macros):
        rounds += 1
        if rounds > 10:
            raise SystemExit("macro expansion did not converge")

    leftover_defines = [d.get("class") for d in root.iter("define")
                        if d.get("macro") == "true"]
    leftover_refs = sorted({e.get("class") for e in root.iter()
                            if e.get("class", "").lower() in macros})
    if leftover_defines or leftover_refs:
        raise SystemExit("macro expansion left residue: "
                         f"defines={leftover_defines} references={leftover_refs}")

    output = ET.tostring(root, encoding="unicode", xml_declaration=True)
    tmp_path = path.with_name(f".{path.name}.{getpid()}.tmp")
    try:
        tmp_path.write_text(output, encoding="utf-8")
        tmp_path.replace(path)
    finally:
        tmp_path.unlink(missing_ok=True)
    print(f"Expanded {len(macros)} macro defines in {path.name} "
          f"({rounds} expansion rounds)")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
