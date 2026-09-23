#!/usr/bin/env python3
"""Check for Dutch-origin contamination in the Indonesian manuscripts.

This book is written in an Indonesian "pengantar" register whose words are
tanpa, dengan, hanya, untuk, satu, tidak, etc. During long edits, Dutch
function words (zonder, met, niet, alleen, voor, uit, een, de, het, ...)
creeped into the text. This script scans all manuscripts for those signal
words and reports file:line:word so the author can replace them.

Usage:
    python scripts/cek-bahasa-asing.py
    python scripts/cek-bahasa-asing.py --file manuscripts/ch-02-regresi-neural-network/master.md

Exit code: 0 = clean, 1 = hits found.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Dutch-origin function words that do NOT belong to the register.
# Words that DO belong (dan, tidak, di, satu, hanya, untuk, dengan, tanpa)
# are intentionally NOT in this list.
# Note: "in" and "op" are omitted to avoid false positives inside terms
# like "input" or "ops"; strip code fences/inline code before matching.
BANNED = {
    "zonder", "met", "en", "niet", "alleen", "voor", "uit", "van",
    "een", "het", "de", "wordt", "zijn", "heeft", "hebt",
    "maar", "als", "wat", "hoe", "waarom", "daarom", "ook",
    "welke", "waar", "dat", "dit", "geen", "omdat", "zodat",
    "meer", "eerder", "later", "door", "over", "tussen",
    "twee", "drie", "hier", "daar", "wijkt", "geldt", "heet", "noemt",
    "kunnen", "zien", "betekenen", "voorspelling", "levert",
    "invoer", "uitvoer", "verborgen", "laag", "lagen",
    "nodig", "vroeg", "naar", "goed", "fout", "zelfde", "gewoon",
    "eigenlijk", "komt", "gaat", "zou", "moet", "kan", "wel", "ook",
}

# Keep hyphenated compounds as single tokens so that legitimate domain terms
# like "over-forecast" or "under-forecast" are not split into "over" + "forecast".
TOKEN_RE = re.compile(r"[a-zà-ž]+(?:-[a-zà-ž]+)*")
CODE_FENCE = re.compile(r"^```")
INLINE_CODE = re.compile(r"`[^`]*`")


def scan_text(text: str) -> list[tuple[int, str]]:
    hits = []
    in_fence = False
    for lineno, raw in enumerate(text.splitlines(), start=1):
        if CODE_FENCE.match(raw.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = INLINE_CODE.sub("", raw)
        for word in TOKEN_RE.findall(line.lower()):
            if word in BANNED:
                hits.append((lineno, word))
    return hits


def scan_file(path: Path) -> list[tuple[int, str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []
    return scan_text(text)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--file", help="scan one file instead of the whole book")
    args = ap.parse_args()

    if args.file:
        paths = [Path(args.file)]
    else:
        paths = sorted((ROOT / "manuscripts").glob("*/master.md"))
        paths += sorted((ROOT / "front-matter").glob("*"))
        paths += sorted((ROOT / "back-matter").glob("*"))

    total = 0
    for p in paths:
        if not p.is_file():
            continue
        for lineno, word in scan_file(p):
            print(f"{p.relative_to(ROOT)}:{lineno}: {word}")
            total += 1

    if total:
        print(
            f"\n{total} hit(s) found. Replace with register words "
            "(tanpa/dengan/hanya/untuk/satu/tidak, etc.).",
            file=sys.stderr,
        )
        return 1
    print("Clean: no Dutch-origin signal words found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())