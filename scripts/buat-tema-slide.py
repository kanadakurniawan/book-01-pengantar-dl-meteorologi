#!/usr/bin/env python3
"""Bangun aset tema slide dari sumber tunggal slides/theme/tokens.json.

Menghasilkan:
  slides/theme/reference-doc.pptx  - template desain untuk pandoc --reference-doc
                                     (ukuran 16:9, warna & font brand)
  slides/theme/theme.css           - tema reveal.js untuk ekspor HTML

Aturan proyek: warna dan font HANYA berubah lewat tokens.json. Jangan menyunting
berkas hasil secara manual karena akan tertimpa saat skrip ini dijalankan ulang.

Pemakaian:
  python scripts/buat-tema-slide.py
  python scripts/buat-tema-slide.py --check   # hanya periksa, tidak menulis

Exit code 0 = sukses; 1 = gagal.
"""
import argparse
import io
import json
import os
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
THEME_DIR = ROOT / "slides" / "theme"
TOKENS_PATH = THEME_DIR / "tokens.json"
PPTX_PATH = THEME_DIR / "reference-doc.pptx"
CSS_PATH = THEME_DIR / "theme.css"
FIXED_DATE = (1980, 1, 1, 0, 0, 0)

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass


def load_tokens() -> dict:
    raw = TOKENS_PATH.read_text(encoding="utf-8")
    data = json.loads(raw)
    for key in ("colors", "fonts", "slide"):
        if key not in data:
            raise ValueError(f"tokens.json tidak punya bagian '{key}'")
    return data


def hex_plain(value: str) -> str:
    """'#006CAC' -> '006CAC'."""
    return value.strip().lstrip("#").upper()


# --------------------------------------------------------------------------
# Patch theme XML di dalam pptx
# --------------------------------------------------------------------------

def _replace_block(xml: str, tag: str, inner: str) -> tuple[str, bool]:
    pattern = re.compile(rf"<a:{tag}>.*?</a:{tag}>", re.S)
    if not pattern.search(xml):
        return xml, False
    return pattern.sub(f"<a:{tag}>{inner}</a:{tag}>", xml, count=1), True


def patch_theme_xml(xml: str, colors: dict, fonts: dict) -> tuple[str, list[str]]:
    """Ganti skema warna dan font di theme1.xml. Kembalikan (xml, daftar catatan)."""
    notes: list[str] = []
    mapping = {
        "dk1": colors["foreground"],
        "lt1": colors["background"],
        "dk2": colors["foreground"],
        "lt2": colors["muted"],
        "accent1": colors["primary"],
        "accent2": colors["secondary"],
        "accent3": colors["accent"],
        "accent4": colors["mutedForeground"],
        "accent5": colors["border"],
        "accent6": colors["primary"],
        "hlink": colors["accent"],
        "folHlink": colors["secondary"],
    }
    for tag, value in mapping.items():
        xml, ok = _replace_block(xml, tag, f'<a:srgbClr val="{hex_plain(value)}"/>')
        if not ok:
            notes.append(f"  tema: elemen warna '{tag}' tidak ditemukan (dilewati)")

    for tag, name in (("majorFont", fonts["heading"]), ("minorFont", fonts["body"])):
        inner = (
            f'<a:latin typeface="{name}"/><a:ea typeface=""/><a:cs typeface=""/>'
        )
        xml, ok = _replace_block(xml, tag, inner)
        if not ok:
            notes.append(f"  tema: elemen font '{tag}' tidak ditemukan (dilewati)")
    return xml, notes


def build_reference_doc(tokens: dict) -> list[str]:
    """Buat reference-doc.pptx dari template bawaan python-pptx lalu beri warna brand."""
    from pptx import Presentation
    from pptx.util import Inches

    notes: list[str] = []
    slide = tokens["slide"]
    prs = Presentation()
    prs.slide_width = Inches(float(slide["widthIn"]))
    prs.slide_height = Inches(float(slide["heightIn"]))

    buf = io.BytesIO()
    prs.save(buf)
    buf.seek(0)

    with zipfile.ZipFile(buf) as zin:
        items = [(info, zin.read(info.filename)) for info in zin.infolist()]

    out_items = []
    patched = False
    for info, data in items:
        if info.filename == "ppt/theme/theme1.xml":
            text = data.decode("utf-8")
            text, patch_notes = patch_theme_xml(text, tokens["colors"], tokens["fonts"])
            notes.extend(patch_notes)
            data = text.encode("utf-8")
            patched = True
        out_items.append((info, data))
    if not patched:
        notes.append("  tema: ppt/theme/theme1.xml tidak ditemukan (warna tidak diterapkan)")

    tmp = PPTX_PATH.with_name(PPTX_PATH.name + ".tmp")
    try:
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
            for info, data in out_items:
                info.date_time = FIXED_DATE
                zout.writestr(info, data)
        os.replace(tmp, PPTX_PATH)
    finally:
        if tmp.exists():
            tmp.unlink()
    return notes


# --------------------------------------------------------------------------
# CSS untuk reveal.js
# --------------------------------------------------------------------------

def build_css(tokens: dict) -> None:
    c = tokens["colors"]
    f = tokens["fonts"]
    slide = tokens["slide"]
    body = f["cssFallback"]
    mono = f["monoFallback"]
    css = f"""/* AUTO-GENERATED dari slides/theme/tokens.json. Jangan sunting manual.
   Jalankan ulang: npm run slide:tema */
:root {{
  --brand-primary: {c['primary']};
  --brand-secondary: {c['secondary']};
  --brand-accent: {c['accent']};
  --brand-bg: {c['background']};
  --brand-fg: {c['foreground']};
  --brand-muted: {c['muted']};
  --brand-muted-fg: {c['mutedForeground']};
  --brand-border: {c['border']};
  --font-body: {body};
  --font-mono: {mono};
  --slide-min-font: {slide['minFontPt']}pt;
}}

.reveal {{
  font-family: var(--font-body);
  color: var(--brand-fg);
  background: var(--brand-bg);
  font-size: 26px;
}}
.reveal .slides {{ text-align: left; }}
.reveal h1, .reveal h2, .reveal h3, .reveal h4 {{
  font-family: var(--font-body);
  color: var(--brand-primary);
  text-transform: none;
  font-weight: 700;
  letter-spacing: 0;
  line-height: 1.15;
}}
.reveal h1 {{ font-size: 2.0em; }}
.reveal h2 {{ font-size: 1.45em; }}
.reveal h3 {{ font-size: 1.1em; color: var(--brand-secondary); }}
.reveal a {{ color: var(--brand-accent); }}
.reveal strong {{ color: var(--brand-primary); }}
.reveal code, .reveal pre {{
  font-family: var(--font-mono);
  background: var(--brand-muted);
  color: var(--brand-fg);
  border-radius: 6px;
}}
.reveal pre code {{ padding: 1rem; }}
.reveal section img {{
  border: none;
  background: transparent;
  box-shadow: none;
  max-height: 58vh;
  max-width: 100%;
}}
.reveal table {{ font-size: 0.7em; border-collapse: collapse; }}
.reveal table th {{
  background: var(--brand-primary);
  color: var(--brand-bg);
  padding: 6px 10px;
}}
.reveal table td {{ border-bottom: 1px solid var(--brand-border); padding: 6px 10px; }}
.reveal .progress {{ color: var(--brand-secondary); }}
.reveal .slide-number {{
  color: var(--brand-muted-fg);
  font-family: var(--font-mono);
  font-size: 0.6em;
}}
.reveal .footer {{
  position: absolute;
  bottom: 12px;
  left: 24px;
  font-size: 0.45em;
  color: var(--brand-muted-fg);
}}
"""
    tmp = CSS_PATH.with_name(CSS_PATH.name + ".tmp")
    try:
        tmp.write_text(css, encoding="utf-8")
        os.replace(tmp, CSS_PATH)
    finally:
        if tmp.exists():
            tmp.unlink()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="hanya validasi tokens.json, tidak menulis berkas")
    args = ap.parse_args()

    if not TOKENS_PATH.exists():
        print(f"GAGAL: {TOKENS_PATH} tidak ditemukan", file=sys.stderr)
        return 1

    tokens = load_tokens()
    print(f"Token dibaca: {TOKENS_PATH.relative_to(ROOT)}")
    print(f"  warna utama : {tokens['colors']['primary']}")
    print(f"  font judul  : {tokens['fonts']['heading']}")
    print(f"  ukuran      : {tokens['slide']['aspect']}")

    if args.check:
        print("Periksa token: OK (tidak menulis berkas)")
        return 0

    THEME_DIR.mkdir(parents=True, exist_ok=True)
    try:
        notes = build_reference_doc(tokens)
    except Exception as exc:  # noqa: BLE001
        print(f"GAGAL membuat reference-doc.pptx: {exc}", file=sys.stderr)
        return 1
    build_css(tokens)

    print(f"  OK  {PPTX_PATH.relative_to(ROOT)}")
    print(f"  OK  {CSS_PATH.relative_to(ROOT)}")
    for note in notes:
        print(note)
    print("Selesai. Tema slide siap dipakai.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
