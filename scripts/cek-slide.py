#!/usr/bin/env python3
"""Pengaman konsistensi deck slide (single source of truth).

Memeriksa setiap slides/ch-*/slides.md terhadap aturan PANDUAN-PPT.md:

  HARD (menggagalkan, exit 1)
    - tanda pisah em dash / en dash (dilarang oleh voice-guidelines)
    - gambar yang dirujuk tidak ada di figures/ bab pasangannya
    - jumlah kata per slide melebihi batas (tokens.json)
    - bagian wajib tidak ada (Tujuan Pembelajaran, Ringkasan, Latihan, Referensi)
    - temuan dari cek-bahasa-asing.py dan cek-dash-prosa.py

  LUNAK (peringatan, tetap exit 0)
    - gambar tanpa keterangan "Sumber:" di baris yang sama/dekat
    - daftar Tujuan Pembelajaran tidak 3-5 butir
    - ada penanda placeholder (TODO, FIXME, lorem)

Pemakaian:
  python scripts/cek-slide.py                  # semua deck
  python scripts/cek-slide.py --file <path>    # satu deck
  python scripts/cek-slide.py --verbose

Exit code 0 = lolos (mungkin dengan peringatan); 1 = ada temuan keras.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLIDES_DIR = ROOT / "slides"
SCRIPTS = ROOT / "scripts"
TOKENS_PATH = SLIDES_DIR / "theme" / "tokens.json"

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
except Exception:
    pass

IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
HEADER_RE = re.compile(r"^(#{1,2})\s+(.*)$")
PLACEHOLDER_RE = re.compile(r"TODO|FIXME|lorem ipsum", re.IGNORECASE)
DASH_BAD = ("\u2014", "\u2013")  # em dash, en dash


def load_tokens() -> dict:
    if not TOKENS_PATH.exists():
        return {"slide": {"maxWordsPerSlide": 70}, "requiredSections": []}
    return json.loads(TOKENS_PATH.read_text(encoding="utf-8"))


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2]
    return text


def strip_fences(text: str) -> str:
    """Buang blok kode; kode bersifat verbatim dan tidak ikut diperiksa."""
    out, in_fence = [], False
    for raw in text.splitlines():
        s = raw.strip()
        if s.startswith("```") or s.startswith("~~~"):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(raw)
    return "\n".join(out)


def chapter_figures(slide_path: Path) -> Path | None:
    """slides/ch-01 -> manuscripts/ch-01-*/figures (bila ada)."""
    prefix = slide_path.parent.name
    for ch in sorted((ROOT / "manuscripts").glob(f"{prefix}-*")):
        figs = ch / "figures"
        if figs.is_dir():
            return figs
    return None


def split_slides(text: str) -> list[tuple[str, list[str]]]:
    """Pecah isi jadi (judul slide, baris isi). Konten sebelum header = slide judul."""
    slides: list[tuple[str, list[str]]] = []
    current_title = "(slide judul)"
    current: list[str] = []
    seen_header = False
    for raw in text.splitlines():
        m = HEADER_RE.match(raw)
        if m:
            if seen_header or current:
                slides.append((current_title, current))
            current_title = m.group(2).strip()
            current = []
            seen_header = True
        else:
            current.append(raw)
    slides.append((current_title, current))
    return slides


def body_word_count(lines: list[str]) -> int:
    in_fence = False
    in_notes = False
    words = 0
    for raw in lines:
        s = raw.strip()
        if s.startswith("```") or s.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if s.startswith("::: notes"):
            in_notes = True
            continue
        if in_notes:
            if s.startswith(":::"):
                in_notes = False
            continue
        if s.startswith(":::") or s.startswith("<!--"):
            continue
        if s.startswith("!["):
            continue
        words += len(re.findall(r"\S+", s))
    return words


def resolve_image(src: str, slide_path: Path, figs: Path | None) -> bool:
    src = src.strip().split()[0].strip("<>")
    if src.startswith(("http://", "https://")):
        return True
    candidates = [slide_path.parent / src]
    if figs is not None:
        candidates.append(figs / src)
        candidates.append(figs / Path(src).name)
    candidates.append(ROOT / src)
    return any(c.exists() for c in candidates)


def run_legacy(script: str, target: Path) -> tuple[int, str]:
    cmd = [sys.executable, str(SCRIPTS / script), "--file", str(target)]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True,
                              encoding="utf-8", errors="replace", cwd=ROOT)
    except OSError as exc:
        return 1, f"gagal menjalankan {script}: {exc}"
    return proc.returncode, ((proc.stdout or "") + (proc.stderr or "")).strip()


def check_deck(path: Path, tokens: dict, verbose: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    max_words = int(tokens.get("slide", {}).get("maxWordsPerSlide", 70))
    required = list(tokens.get("requiredSections", []))

    text = path.read_text(encoding="utf-8")
    body = strip_frontmatter(text)
    scan_body = strip_fences(body)
    rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path

    for ch in DASH_BAD:
        if ch in scan_body:
            name = "em dash" if ch == "\u2014" else "en dash"
            errors.append(f"{rel}: mengandung {name} (dilarang, ganti koma/titik dua)")

    figs = chapter_figures(path)
    for m in IMAGE_RE.finditer(scan_body):
        if not resolve_image(m.group(1), path, figs):
            errors.append(f"{rel}: gambar tidak ditemukan -> {m.group(1)}")

    for title, lines in split_slides(scan_body):
        count = body_word_count(lines)
        if count > max_words:
            errors.append(
                f"{rel}: slide '{title}' terlalu padat ({count} kata > {max_words})")

    for section in required:
        if section.lower() not in scan_body.lower():
            errors.append(f"{rel}: bagian wajib hilang -> '{section}'")

    # Tujuan Pembelajaran harus 3-5 butir
    if "Tujuan Pembelajaran" in scan_body:
        block = scan_body.split("Tujuan Pembelajaran", 1)[1]
        bullets = 0
        for raw in block.splitlines()[1:]:
            s = raw.strip()
            if not s:
                if bullets:
                    break
                continue
            if s.startswith("##") or s.startswith("#"):
                break
            if re.match(r"^([-*]|\d+\.)\s", s):
                bullets += 1
        if bullets and not 3 <= bullets <= 5:
            warnings.append(f"{rel}: Tujuan Pembelajaran {bullets} butir (disarankan 3-5)")

    # Gambar sebaiknya punya keterangan sumber di baris yang sama
    for raw in scan_body.splitlines():
        if raw.strip().startswith("!["):
            if "sumber:" not in raw.lower():
                warnings.append(f"{rel}: gambar tanpa keterangan 'Sumber:' -> {raw.strip()[:60]}")

    if PLACEHOLDER_RE.search(scan_body):
        warnings.append(f"{rel}: ada penanda placeholder (TODO/FIXME/lorem)")

    for script in ("cek-bahasa-asing.py", "cek-dash-prosa.py"):
        rc, out = run_legacy(script, path)
        if rc != 0:
            errors.append(f"{rel}: {script} melaporkan temuan\n{out}")

    if verbose and not errors and not warnings:
        print(f"  [bersih] {rel}")
    return errors, warnings


def main() -> int:
    tokens = load_tokens()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--file", default=None, help="cek satu deck slides.md")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    if args.file:
        decks = [Path(args.file).resolve()]
    else:
        decks = sorted(SLIDES_DIR.glob("ch-*/slides.md"))

    if not decks:
        print("Tidak ada deck (slides/ch-*/slides.md). Buat dari slides/_template/slides.md.")
        return 0

    all_errors: list[str] = []
    all_warnings: list[str] = []
    for deck in decks:
        if not deck.is_file():
            all_errors.append(f"{deck}: berkas tidak ditemukan")
            continue
        errors, warnings = check_deck(deck, tokens, args.verbose)
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        state = "TEMUAN" if errors else ("peringatan" if warnings else "bersih")
        shown = deck.relative_to(ROOT) if deck.is_relative_to(ROOT) else deck
        print(f"[{state}] {shown}")

    print()
    for w in all_warnings:
        print(f"  peringatan: {w}")
    if all_errors:
        for e in all_errors:
            print(f"  ERROR: {e}")
        print(f"\nSLIDE: GAGAL - {len(all_errors)} temuan keras pada {len(decks)} deck. Exit 1.")
        return 1
    print(f"SLIDE: LOLOS - {len(decks)} deck "
          f"({len(all_warnings)} peringatan). Exit 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
