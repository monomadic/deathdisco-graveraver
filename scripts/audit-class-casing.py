#!/usr/bin/env python3
"""
Audit VirtualDJ skin class naming conventions.

Conventions:
  - <define class="..."> names are uppercase.
  - Class implementations/references are lowercase.
  - Every referenced class has a case-insensitive definition.
"""

import re
import sys
from pathlib import Path

COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
TAG_RE = re.compile(r"<(?P<tag>[A-Za-z_][\w:.-]*)(?P<attrs>[^<>]*?)>")
CLASS_ATTR_RE = re.compile(r'\bclass="([^"]+)"')


def uncommented_segments(text: str):
    last = 0
    for match in COMMENT_RE.finditer(text):
        yield text[last:match.start()]
        last = match.end()
    yield text[last:]


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def audit_file(path: Path):
    text = path.read_text(encoding="utf-8")
    findings = []
    definitions = []
    references = []

    base_offset = 0
    for segment in uncommented_segments(text):
        segment_start = text.find(segment, base_offset)
        base_offset = segment_start + len(segment)

        for tag_match in TAG_RE.finditer(segment):
            tag = tag_match.group("tag")
            attrs = tag_match.group("attrs")
            class_match = CLASS_ATTR_RE.search(attrs)
            if not class_match:
                continue

            class_name = class_match.group(1)
            absolute_offset = segment_start + tag_match.start()
            location = f"{path}:{line_number(text, absolute_offset)}"

            if tag == "define":
                definitions.append((class_name, location))
                if class_name != class_name.upper():
                    findings.append(f"{location}: define class should be uppercase: {class_name}")
            else:
                references.append((class_name, location))
                if class_name != class_name.lower():
                    findings.append(f"{location}: class reference should be lowercase: {class_name}")

    return findings, definitions, references


def main() -> int:
    all_findings = []
    definitions = []
    references = []

    for path in sorted(Path("src").rglob("*.xml")):
        findings, file_definitions, file_references = audit_file(path)
        all_findings.extend(findings)
        definitions.extend(file_definitions)
        references.extend(file_references)

    defined_names = {class_name.lower() for class_name, _ in definitions}
    for class_name, location in references:
        if class_name.lower() not in defined_names:
            all_findings.append(f"{location}: class reference has no definition: {class_name}")

    if all_findings:
        print("Class audit failed:")
        for finding in all_findings:
            print(f"  {finding}")
        return 1

    print(f"Class audit passed: {len(definitions)} definitions, {len(references)} references")
    return 0


if __name__ == "__main__":
    sys.exit(main())
