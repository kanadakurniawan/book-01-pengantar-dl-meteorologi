#!/usr/bin/env python3
"""Render semua deck slide ke slides/build/.

Untuk setiap slides/ch-*/slides.md menghasilkan:
  - <nama>.pptx  : PowerPoint asli lewat pandoc --reference-doc (tema brand)
  - <nama>.html  : slide HTML (reveal.js) lewat pandoc, tema theme.css

prasyarat: pandoc terpasang (untuk pptx & html) dan python-pptx (untuk tema).
Bila aset tema belum ada, skrip ini otomatis menjalankannya lebih dulu.

Pemakaian:
  python scripts/build-slide.py
  python scripts/build-slide.py --deck ch-01
  python scripts/build-slide.py --no-check      # lewati cek-slide.py
Exit code 0 = semua deck berhasil dirender; 1 = ada yang gagal.
"""
import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLIDES_DIR = ROOT / "slides"
THEME_DIR = SLIDES_DIR / "theme"
BUILD_DIR = SLIDES_DIR / "build"
REFERENCE_DOC = THEME_DIR / "reference-doc.pptx"
THEME_CSS = THEME_DIR / "theme.css"
TOKENS = THEME_DIR / "tokens.json"
SCRIPTS = ROOT / "scripts"

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
except Exception:
    pass


def have(name: str) -> bool:
    return shutil.which(name) is not None


def chapter_resource_paths(deck: Path) -> str:
    paths = [str(deck.parent)]
    prefix = deck.parent.name
    for ch in sorted((ROOT / "manuscripts").glob(f"{prefix}-*")):
        paths.append(str(ch))
        figs = ch / "figures"
        if figs.is_dir():
            paths.append(str(figs))
    return os.pathsep.join(paths)


def ensure_theme() -> bool:
    reason = None
    if not (REFERENCE_DOC.exists() and THEME_CSS.exists()):
        reason = "Aset tema belum ada"
    else:
        try:
            newest_theme = min(REFERENCE_DOC.stat().st_mtime, THEME_CSS.stat().st_mtime)
            if TOKENS.exists() and TOKENS.stat().st_mtime > newest_theme:
                reason = "tokens.json lebih baru dari aset tema"
        except OSError:
            reason = "Aset tema tidak dapat dibaca"
    if reason is None:
        return True
    print(f"{reason}, membangkitkan ulang dari tokens.json ...")
    proc = subprocess.run([sys.executable, str(SCRIPTS / "buat-tema-slide.py")], cwd=ROOT)
    return proc.returncode == 0


def render(deck: Path) -> list[str]:
    ok: list[str] = []
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    stem = deck.parent.name
    res = f"--resource-path={chapter_resource_paths(deck)}"
    base = [
        "pandoc", str(deck), "--slide-level=2", res,
    ]
    out = BUILD_DIR / f"{stem}.pptx"
    cmd = base + [f"--reference-doc={REFERENCE_DOC}", "-o", str(out)]
    try:
        subprocess.run(cmd, check=True, cwd=ROOT,
                       stdout=sys.stdout, stderr=sys.stderr)
        ok.append(f"  OK  {out.relative_to(ROOT)}")
    except subprocess.CalledProcessError as exc:
        ok.append(f"  GAGAL pptx {stem}: exit {exc.returncode}")

    out = BUILD_DIR / f"{stem}.html"
    cmd = base + [
        "-t", "revealjs", "-s", "--embed-resources",
        f"--css={THEME_CSS}", "--math-method=mathjax", "-o", str(out),
    ]
    try:
        subprocess.run(cmd, check=True, cwd=ROOT,
                       stdout=sys.stdout, stderr=sys.stderr)
        ok.append(f"  OK  {out.relative_to(ROOT)}")
    except subprocess.CalledProcessError as exc:
        ok.append(f"  GAGAL html {stem}: exit {exc.returncode}")
    return ok


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--deck", default=None,
                    help="hanya render satu deck, mis. ch-01")
    ap.add_argument("--no-check", action="store_true",
                    help="lewati cek-slide.py setelah render")
    args = ap.parse_args()

    if not have("pandoc"):
        print("GAGAL: pandoc tidak terpasang (lihat https://pandoc.org).", file=sys.stderr)
        return 1

    if not ensure_theme():
        print("GAGAL: aset tema tidak dapat dibangkitkan.", file=sys.stderr)
        return 1

    if args.deck:
        decks = [SLIDES_DIR / args.deck / "slides.md"]
    else:
        decks = sorted(SLIDES_DIR.glob("ch-*/slides.md"))

    if not decks:
        print("Tidak ada deck (slides/ch-*/slides.md).")
        print("Mulai dari template: salin slides/_template/ menjadi slides/ch-01/.")
        return 0

    failures = 0
    for deck in decks:
        if not deck.is_file():
            print(f"GAGAL: {deck} tidak ditemukan")
            failures += 1
            continue
        print(f"Render {deck.relative_to(ROOT)}")
        for line in render(deck):
            print(line)
            if "GAGAL" in line:
                failures += 1

    if not args.no_check:
        print("\nJalankan pengaman (cek-slide.py):")
        rc = subprocess.run([sys.executable, str(SCRIPTS / "cek-slide.py")], cwd=ROOT).returncode
        if rc != 0:
            failures += 1

    print(f"\nSelesai. Deck diproses: {len(decks)}; kegagalan: {failures}.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
