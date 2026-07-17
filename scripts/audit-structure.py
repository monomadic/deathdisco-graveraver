#!/usr/bin/env python3
"""
Audit VirtualDJ skin XML structure beyond basic class casing.

Checks:
  - every defined class is referenced somewhere
  - every defined class is reachable from skin/module roots
  - every XML file under src/ is reachable from src/skin.xml XIncludes
  - XInclude targets exist and export at least one node for /* pointers
  - duplicate class definitions are limited to known conditional variants
  - new always-hidden UI blocks are flagged
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
import re
import sys


SRC_DIR = Path("src")
ROOT_SKIN = SRC_DIR / "skin.xml"


def is_parked(path: Path) -> bool:
    """Files/dirs whose name starts with '_' are deliberately parked out of the
    build (e.g. src/layouts/pro/_positions/). They are not expected to be
    reachable from skin.xml, so the audit ignores them entirely."""

    return any(part.startswith("_") for part in path.parts)

COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
XML_DECL_RE = re.compile(r"<\?xml[^>]*\?>", re.S)
DOCTYPE_RE = re.compile(r"<!DOCTYPE[^>]*>", re.S)
DEFINE_BLOCK_RE = re.compile(
    r'<define\b(?P<attrs>[^<>]*?\bclass="(?P<class>[^"]+)"[^<>]*?)>'
    r"(?P<body>.*?)"
    r"</define>",
    re.S,
)
TAG_RE = re.compile(r"<(?P<tag>[A-Za-z_][\w:.-]*)(?P<attrs>[^<>]*?)>")
ATTR_RE = re.compile(r'\b(?P<name>[A-Za-z_:][\w:.-]*)="(?P<value>[^"]*)"')
CLASS_ATTR_RE = re.compile(r'\bclass="([^"]+)"')
EXPORT_ROOT_RE = re.compile(
    r"<(?P<root>defs|module|globals)\b[^>]*>(?P<body>.*)</(?P=root)>",
    re.S,
)
ELEMENT_RE = re.compile(r"<(?!/)(?!\?)(?!!)[A-Za-z_][\w:.-]*\b")


# These are deliberate conditional variants. Any other duplicate definition is
# suspicious because class resolution then depends on include/order behavior.
ALLOWED_DUPLICATE_DEFINITIONS = {
    "button_main": "color-scheme variant",
    "custom_button": "color-scheme variant",
}


# Always-hidden blocks are rejected unless a deliberate exception is documented
# here with a short explanation.
ALLOWED_ALWAYS_HIDDEN_COUNTS = {}


@dataclass(frozen=True)
class Location:
    path: Path
    line: int

    def __str__(self) -> str:
        return f"{self.path}:{self.line}"


@dataclass(frozen=True)
class Definition:
    name: str
    location: Location


@dataclass(frozen=True)
class Reference:
    name: str
    location: Location


def strip_comments(text: str) -> str:
    """Remove comments while preserving line numbers."""

    return COMMENT_RE.sub(lambda match: "\n" * match.group(0).count("\n"), text)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def attrs_map(attrs: str) -> dict[str, str]:
    return {match.group("name"): match.group("value") for match in ATTR_RE.finditer(attrs)}


def parse_class_graph(paths: list[Path]):
    definitions: dict[str, list[Definition]] = defaultdict(list)
    references: list[Reference] = []
    root_references: list[Reference] = []
    definition_references: dict[str, list[list[str]]] = defaultdict(list)
    hidden_blocks: dict[str, list[Location]] = defaultdict(list)

    for path in paths:
        text = strip_comments(path.read_text(encoding="utf-8"))
        define_ranges: list[tuple[int, int]] = []

        for define_match in DEFINE_BLOCK_RE.finditer(text):
            class_name = define_match.group("class")
            class_key = class_name.lower()
            location = Location(path, line_number(text, define_match.start()))
            definitions[class_key].append(Definition(class_name, location))
            define_ranges.append((define_match.start(), define_match.end()))

            body_references: list[str] = []
            for tag_match in TAG_RE.finditer(define_match.group("body")):
                if tag_match.group("tag") == "define":
                    continue
                class_match = CLASS_ATTR_RE.search(tag_match.group("attrs"))
                if class_match:
                    body_references.append(class_match.group(1).lower())
            definition_references[class_key].append(body_references)

        for tag_match in TAG_RE.finditer(text):
            tag = tag_match.group("tag")
            attrs = tag_match.group("attrs")
            attr_values = attrs_map(attrs)
            location = Location(path, line_number(text, tag_match.start()))

            if attr_values.get("visibility") == "false":
                hidden_blocks[str(path)].append(location)

            class_name = attr_values.get("class")
            if not class_name or tag == "define":
                continue

            class_key = class_name.lower()
            reference = Reference(class_key, location)
            references.append(reference)

            in_define = any(start <= tag_match.start() < end for start, end in define_ranges)
            if not in_define:
                root_references.append(reference)

    return definitions, references, root_references, definition_references, hidden_blocks


def reachable_classes(
    definitions: dict[str, list[Definition]],
    root_references: list[Reference],
    definition_references: dict[str, list[list[str]]],
) -> set[str]:
    reachable: set[str] = set()
    queue = deque(reference.name for reference in root_references if reference.name in definitions)

    while queue:
        class_name = queue.popleft()
        if class_name in reachable:
            continue

        reachable.add(class_name)
        for body_references in definition_references.get(class_name, []):
            for referenced_class in body_references:
                if referenced_class in definitions and referenced_class not in reachable:
                    queue.append(referenced_class)

    return reachable


def include_targets(path: Path) -> list[tuple[Path, Location, str]]:
    text = strip_comments(path.read_text(encoding="utf-8"))
    targets: list[tuple[Path, Location, str]] = []

    for tag_match in TAG_RE.finditer(text):
        if tag_match.group("tag") != "xi:include":
            continue

        attr_values = attrs_map(tag_match.group("attrs"))
        href = attr_values.get("href")
        if not href:
            continue

        target = path.parent / href
        location = Location(path, line_number(text, tag_match.start()))
        targets.append((target, location, attr_values.get("xpointer", "")))

    return targets


def included_files(root: Path) -> tuple[set[Path], list[tuple[Path, Location]], list[str]]:
    seen: set[Path] = set()
    missing: list[tuple[Path, Location]] = []
    empty_exports: list[str] = []
    queue = deque([root])

    while queue:
        path = queue.popleft()
        if path in seen:
            continue
        seen.add(path)

        if not path.exists():
            continue

        for target, location, xpointer in include_targets(path):
            if not target.exists():
                missing.append((target, location))
                continue

            if xpointer.endswith("/*)"):
                target_text = strip_comments(target.read_text(encoding="utf-8"))
                target_text = XML_DECL_RE.sub("", target_text)
                target_text = DOCTYPE_RE.sub("", target_text)
                root_match = EXPORT_ROOT_RE.search(target_text)
                if root_match and not ELEMENT_RE.search(root_match.group("body")):
                    empty_exports.append(f"{location}: include target exports no nodes: {target}")

            queue.append(target)

    return seen, missing, empty_exports


def format_definitions(definitions: list[Definition]) -> list[str]:
    return [f"{definition.location}: {definition.name}" for definition in definitions]


def audit() -> list[str]:
    findings: list[str] = []
    xml_paths = sorted(path for path in SRC_DIR.rglob("*.xml") if not is_parked(path))

    definitions, references, root_references, definition_references, hidden_blocks = parse_class_graph(xml_paths)

    reference_names = {reference.name for reference in references}
    direct_unused = {
        class_name: class_definitions
        for class_name, class_definitions in sorted(definitions.items())
        if class_name not in reference_names
    }
    if direct_unused:
        findings.append("Defined classes with no references:")
        for class_definitions in direct_unused.values():
            findings.extend(f"  {line}" for line in format_definitions(class_definitions))

    reachable = reachable_classes(definitions, root_references, definition_references)
    unreachable = {
        class_name: class_definitions
        for class_name, class_definitions in sorted(definitions.items())
        if class_name not in reachable
    }
    if unreachable:
        findings.append("Defined classes unreachable from skin/module roots:")
        for class_definitions in unreachable.values():
            findings.extend(f"  {line}" for line in format_definitions(class_definitions))

    duplicate_definitions = {
        class_name: class_definitions
        for class_name, class_definitions in sorted(definitions.items())
        if len(class_definitions) > 1 and class_name not in ALLOWED_DUPLICATE_DEFINITIONS
    }
    if duplicate_definitions:
        findings.append("Duplicate class definitions:")
        for class_definitions in duplicate_definitions.values():
            findings.extend(f"  {line}" for line in format_definitions(class_definitions))

    seen_files, missing_includes, empty_exports = included_files(ROOT_SKIN)
    unlinked_files = sorted(set(xml_paths) - seen_files)
    if unlinked_files:
        findings.append("XML files not reachable from src/skin.xml XIncludes:")
        findings.extend(f"  {path}" for path in unlinked_files)

    if missing_includes:
        findings.append("Missing XInclude targets:")
        findings.extend(f"  {location}: missing include target: {target}" for target, location in missing_includes)

    if empty_exports:
        findings.append("Empty XInclude export targets:")
        findings.extend(f"  {line}" for line in empty_exports)

    unexpected_hidden: list[Location] = []
    for path, locations in sorted(hidden_blocks.items()):
        allowed_count = ALLOWED_ALWAYS_HIDDEN_COUNTS.get(path, 0)
        if len(locations) > allowed_count:
            unexpected_hidden.extend(locations[allowed_count:])
    if unexpected_hidden:
        findings.append('Unexpected always-hidden blocks, visibility="false":')
        findings.extend(f"  {location}" for location in unexpected_hidden)

    allowed_duplicates = sum(
        len(class_definitions)
        for class_name, class_definitions in definitions.items()
        if len(class_definitions) > 1 and class_name in ALLOWED_DUPLICATE_DEFINITIONS
    )
    known_hidden = sum(
        min(len(hidden_blocks.get(path, [])), allowed_count)
        for path, allowed_count in ALLOWED_ALWAYS_HIDDEN_COUNTS.items()
    )

    if not findings:
        print(
            "Structural audit passed: "
            f"{sum(len(values) for values in definitions.values())} definitions "
            f"({len(definitions)} unique), {len(references)} references, "
            f"{len(xml_paths)} XML files"
        )
        print(
            "Reachability passed: "
            "0 unused definitions, 0 unreachable definitions, 0 unlinked XML files"
        )
        if allowed_duplicates:
            allowed_names = ", ".join(sorted(ALLOWED_DUPLICATE_DEFINITIONS))
            print(f"Allowed duplicate definitions: {allowed_names}")
        if known_hidden:
            print(f"Known always-hidden blocks: {known_hidden}")

    return findings


def main() -> int:
    if not ROOT_SKIN.exists():
        print(f"Structural audit failed: missing root skin: {ROOT_SKIN}", file=sys.stderr)
        return 1

    findings = audit()
    if findings:
        print("Structural audit failed:")
        for finding in findings:
            print(f"  {finding}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
