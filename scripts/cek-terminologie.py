#!/usr/bin/env python3
"""Check terminologie-consistentie: één concept = één term in heel het boek.

Canonieke termen (na de terminologie-campagne):
    error/errors, kesalahan  -> galat           (Engels alleen in *cursieve* expansies
                                                  en referentie-titels)
    station/stations         -> stasiun          (behalve in eigennamen en titels)
    prakiraan                -> prediksi
    forecast (proza)         -> prediksi         (behalve *cursieve* termen,
                                                  bestandsnamen en titels)
    patokan                  -> *baseline*
    training (proza)         -> pelatihan        (behalve *training set* en titels)

De check negeert opzettelijk: code-fences, inline code, *...*-spannen (Engelse
termen), markdown-link-bestandsnamen, URL's, bibliografie-regels en vaste
keep-frases (referentie-titels, eigennamen zoals "Sea Level Station Monitoring
Facility"). "retraining" is een vaste Engelse term en wordt niet gevlagd.

Usage:
    python scripts/cek-terminologie.py
    python scripts/cek-terminologie.py --file manuscripts/ch-02-regresi-neural-network/master.md

Exit code: 0 = schoon, 1 = hits gevonden.
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# verouderd woord (ci) -> canonieke term
DEPRECATED = {
    "error": "galat",
    "errors": "galat",
    "kesalahan": "galat",
    "station": "stasiun",
    "stations": "stasiun",
    "prakiraan": "prediksi",
    "forecast": "prediksi",
    "patokan": "*baseline*",
    "training": "pelatihan",
}
WORD_RE = re.compile(r"\b(?:%s)\b" % "|".join(DEPRECATED), re.I)

# vaste frases/eigennamen die legitiem de verouderde vorm bevatten
KEEP_PHRASES = [
    "mean absolute error",
    "mean squared error",
    "root mean square error",
    "back-propagating errors",
    "large-batch training",
    "sea level station monitoring",
    "multi-step forecast",
    "retraining",
]

# bibliografie-regel: geciteerde titel + venster-detail
REFS_RE = re.compile(
    r"et al\.|available:|doi:|arxiv|\bproc\.\b|neurips|iclr|vol\.|\bpp\.\b",
    re.I,
)

CODE_FENCE = re.compile(r"^\s*(```|~~~)")


def backtick_spans(line: str) -> list[tuple[int, int]]:
    """Paren van inline-code `...`."""
    spans = []
    idxs = [i for i, c in enumerate(line) if c == "`"]
    for k in range(0, len(idxs) - 1, 2):
        spans.append((idxs[k], idxs[k + 1] + 1))
    return spans


def link_spans(line: str) -> list[tuple[int, int]]:
    """Doelen van ](...) en URL's."""
    spans = []
    for m in re.finditer(r"\]\((.*?)\)", line):
        spans.append((m.start(), m.end()))
    for m in re.finditer(r"https?://\S+", line):
        spans.append((m.start(), m.end()))
    return spans


def italic_spans(masked: str) -> list[tuple[int, int]]:
    """Samenvoegingen op basis van *-toggle (benadering)."""
    spans = []
    on = None
    for i, ch in enumerate(masked):
        if ch == "*":
            if on is None:
                on = i
            else:
                if i - on > 1:
                    spans.append((on, i + 1))
                on = None
    return spans


def in_spans(pos: int, mlen: int, spans) -> bool:
    for s, e in spans:
        if s <= pos and pos + mlen <= e:
            return True
    return False


def scan_text(text: str) -> list[tuple[int, str]]:
    hits = []
    in_fence = False
    for lineno, raw in enumerate(text.splitlines(), start=1):
        if CODE_FENCE.match(raw.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        # bibliografie-regels: heel de regel overslaan
        if REFS_RE.search(raw) or ('"' in raw and re.search(r"\b(19|20)\d\d\b", raw)):
            continue
        prot = backtick_spans(raw) + link_spans(raw)
        masked = list(raw)
        for s, e in prot:
            for k in range(s, e):
                masked[k] = " "
        for s, e in italic_spans("".join(masked)):
            prot.append((s, e))
        keep_spans = []
        low = raw.lower()
        for kp in KEEP_PHRASES:
            start = 0
            while True:
                i = low.find(kp, start)
                if i < 0:
                    break
                keep_spans.append((i, i + len(kp)))
                start = i + 1
        for m in WORD_RE.finditer(raw):
            if in_spans(m.start(), m.end() - m.start(), prot):
                continue
            if in_spans(m.start(), m.end() - m.start(), keep_spans):
                continue
            hits.append((lineno, m.group(0), DEPRECATED[m.group(0).lower()]))
    return hits


def scan_file(path: Path) -> list[tuple[int, str, str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []
    return scan_text(text)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--file", help="scan één bestand in plaats van het hele boek")
    args = ap.parse_args()

    if args.file:
        paths = [Path(args.file)]
    else:
        paths = sorted((ROOT / "manuscripts").glob("*/master.md"))
        paths += sorted((ROOT / "front-matter").glob("*.md"))
        paths += sorted((ROOT / "back-matter").glob("*.md"))
        paths.append(ROOT / "REGISTER.md")

    total = 0
    for p in paths:
        if not p.is_file():
            continue
        for lineno, word, canon in scan_file(p):
            print(f"{p.relative_to(ROOT)}:{lineno}: {word}  -> gebruik '{canon}'")
            total += 1

    if total:
        print(
            f"\n{total} hit(s) gevonden. Eén concept = één term: vervang met de "
            f"canonieke vorm (zie docstring).",
            file=sys.stderr,
        )
        return 1
    print("Schoon: canonieke terminologie consistent in heel het boek.")
    return 0


if __name__ == "__main__":
    sys.exit(main())