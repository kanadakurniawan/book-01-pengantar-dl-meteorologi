#!/usr/bin/env python3
"""Cek pemakaian tanda hubung berspasi (" - ") sebagai pemisah klausa dalam prosa.

Ketentuan (keputusan gaya buku):
  - " - " TIDAK boleh dipakai sebagai pengganti koma/titik dua/titik di dalam
    kalimat naratif, termasuk pola "- justru _", "- padahal _", dan appositive
    ganda ("X - keterangan - Y"). Ganti dengan tanda baca baku.
  - KONTEKS YANG TETAP DIPERBOLEHKAN (tidak di-flag):
      - label penomoran   : "# Bab 8 - _", "**Kode 8.1 - _**", "**Gambar 8.1 - _**", "**Tabel 8.1 - _**", "![Gambar ... - _](...)";
      - frontmatter YAML (blok "---" pertama);
      - item daftar       : bullet ("- ", "* ") dan bernomor ("1. ", "**1.** ", dst.);
      - tabel markdown    : baris dimulai "|";
      - blok kode dan math (fence ```/~~~; $$...$$);
      - rentang/operasi   : angka atau simbol math di kedua sisi ("10 - 19", "x - 1");
      - URL.

Pemakaian:
  python scripts/cek-dash-prosa.py                 # semua manuscripts/*/master.md + sel markdown notebook
  python scripts/cek-dash-prosa.py --file <path>   # satu file
Exit code 0 = bersih; 1 = ada temuan.
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DASH = re.compile(r" - ")
SKIP_PREFIX = (
    "#", "```", "~~~", "|", "- ", "* ", "$$", "![" ,
)
LABEL_START = ("**Kode", "**Gambar", "**Tabel", "**Diagram", "**Alur")
ITEM_NUMBERED = re.compile(r"^\s*(?:\d+\.\s|\*\*\d+[.)]?\*\*\s|\([a-z0-9]+\)\s)")


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2]
    return text


def strip_fences(text: str) -> str:
    out, in_fence = [], False
    for raw in text.splitlines():
        s = raw.strip()
        if s.startswith("```") or s.startswith("~~~"):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(raw)
    return "\n".join(out)


def strip_inline(line: str) -> str:
    line = re.sub(r"`[^`]*`", " ", line)          # inline code
    line = re.sub(r"https?://\S+", " ", line)      # URL
    line = re.sub(r"\$\$?.+?\$\$?", " ", line)     # math inline ($..$)
    return line


def relevant(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    if any(s.startswith(p) for p in SKIP_PREFIX):
        return False
    if any(s.startswith(p) for p in LABEL_START):
        return False
    if ITEM_NUMBERED.match(s):
        return False
    return True


def find_flags(line: str) -> list[int]:
    """Kembalikan posisi awal setiap ' - ' yang kandidat pelanggaran."""
    stripped = strip_inline(line)
    flags = []
    for m in DASH.finditer(stripped):
        before = stripped[m.start() - 1] if m.start() > 0 else " "
        after = stripped[m.end()] if m.end() < len(stripped) else " "
        # rentang/operasi numerik maupun simbol: digit di salah satu sisi
        if before in "0123456789" or after in "0123456789":
            continue
        # simbol math pada ruas kanan (mis. "x - μ")
        if after in "μσ∞π∈≤≥→∖":
            continue
        flags.append(m.start())
    return flags


def scan_text(path: pathlib.Path, lines: list[str]) -> list[tuple[int, str]]:
    hits = []
    for i, raw in enumerate(lines, start=1):
        if not relevant(strip_inline(raw)):
            continue
        if not relevant(raw):
            continue
        flags = find_flags(raw)
        for pos in flags:
            ctx = raw[max(0, pos - 50): pos + 80].strip()
            hits.append((i, f"...{ctx}..."))
    return hits


def scan_markdown(path: pathlib.Path) -> list[tuple[int, str]]:
    text = path.read_text(encoding="utf-8")
    text = strip_frontmatter(text)
    text = strip_fences(text)
    return scan_text(path, text.splitlines())


def scan_notebook(path: pathlib.Path) -> list[tuple[int, str]]:
    nb = json.loads(path.read_text(encoding="utf-8"))
    hits = []
    for idx, cell in enumerate(nb["cells"]):
        if cell["cell_type"] != "markdown":
            continue
        src = "".join(cell["source"]).strip()
        if not src:
            continue
        for line_no, raw in enumerate(src.splitlines(), start=1):
            if not relevant(raw):
                continue
            for pos in find_flags(raw):
                ctx = raw[max(0, pos - 50): pos + 80].strip()
                hits.append((idx, f"[markdown] {line_no}: ...{ctx}..."))
    return hits


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default=None)
    args = ap.parse_args()

    if args.file:
        paths = [pathlib.Path(args.file)]
    else:
        paths = sorted((ROOT / "manuscripts").glob("*/master.md"))
        nb_paths = sorted((ROOT / "notebooks").glob("*.ipynb"))
        paths += nb_paths

    total = 0
    for p in paths:
        if p.suffix == ".ipynb":
            hits = scan_notebook(p)
        else:
            hits = scan_markdown(p)
        tag = f"  [{len(hits)}]"
        print(f"{p.relative_to(ROOT) if p.is_relative_to(ROOT) else p}{tag}")
        for line_no, ctx in hits:
            total += 1
            print(f"    L{line_no}: {ctx}")
    if total:
        print(f"TEMUAN: {total} dash klausa di {len(paths)} file --- tidak bersih (exit 1)")
        return 1
    print(f"Bersih: tidak ada dash pemisah klausa di {len(paths)} file (exit 0)")
    return 0


if __name__ == "__main__":
    sys.exit(main())