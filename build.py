"""
==============================================================
 GitHub Profile README Builder
==============================================================

Usage:

    python build.py

This script generates README.md from:

    README.template.md

and the markdown files inside:

    content/

==============================================================
"""

from pathlib import Path
import re

ROOT = Path(__file__).parent

TEMPLATE = ROOT / "README.template.md"
OUTPUT = ROOT / "README.md"
CONTENT = ROOT / "content"


def load_sections():

    sections = {}

    for file in sorted(CONTENT.glob("*.md")):

        text = file.read_text(encoding="utf-8")

        match = re.match(r"\d+\-(.+)\.md", file.name)

        if not match:
            continue

        key = match.group(1)

        sections[key] = text

    return sections


def build():

    template = TEMPLATE.read_text(encoding="utf-8")

    sections = load_sections()

    for key, content in sections.items():

        marker = f"<!-- inject:{key} -->"

        template = template.replace(marker, content)

    OUTPUT.write_text(template, encoding="utf-8")

    print()

    print("=======================================")
    print(" README successfully generated.")
    print("=======================================")
    print()
    print("Output:", OUTPUT)
    print()


if __name__ == "__main__":
    build() 