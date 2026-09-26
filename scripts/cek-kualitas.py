#!/usr/bin/env python3
"""Cek kualitas terpadu: bahasa-asing + terminologie + dash-prosa.

Menjalankan tiga cek kualitas sekaligus dan merangkum hasilnya:

  1. cek-bahasa-asing.py   - kata berakar Belanda/Italia yang bocor ke register
  2. cek-terminologie.py   - satu konsep = satu istilah (terminologi kanonik)
  3. cek-dash-prosa.py     - tanda hubung berspasi (" - ") sebagai pemisah
                             klausa dalam prosa

Pemakaian:
  python scripts/cek-kualitas.py                 # seluruh buku (default)
  python scripts/cek-kualitas.py --file <path>   # satu berkas
  python scripts/cek-kualitas.py --verbose       # tampilkan output penuh
  python scripts/cek-kualitas.py --no-color      # tanpa warna ANSI

Exit code 0 = SEMUA cek bersih; 1 = ada temuan di salah satu cek.
"""
import argparse
import os
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent

# (nama singkat, nama berkas, deskripsi)
CHECKS = [
    ("bahasa-asing", "cek-bahasa-asing.py",
     "kata berakar Belanda/Italia dalam register"),
    ("terminologie", "cek-terminologie.py",
     "konsistensi terminologi kanonik (satu konsep = satu istilah)"),
    ("dash-prosa", "cek-dash-prosa.py",
     "tanda hubung berspasi pemisah klausa dalam prosa"),
]

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
BOLD = "\033[1m"
RESET = "\033[0m"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--file", default=None, help="cek satu berkas saja")
    ap.add_argument("--verbose", action="store_true",
                    help="tampilkan output penuh tiap cek")
    ap.add_argument("--no-color", action="store_true", help="matikan warna ANSI")
    args = ap.parse_args()

    use_color = (not args.no_color) and os.environ.get("NO_COLOR") is None
    if use_color and not sys.stdout.isatty():
        use_color = False

    def paint(text: str, color: str) -> str:
        return f"{color}{text}{RESET}" if use_color else text

    results = []
    for name, script, desc in CHECKS:
        cmd = [sys.executable, str(SCRIPTS / script)]
        if args.file:
            cmd += ["--file", args.file]
        try:
            proc = subprocess.run(
                cmd, capture_output=True, text=True,
                encoding="utf-8", errors="replace", cwd=ROOT,
            )
        except OSError as e:
            print(paint(f"[{name}] GAGAL menjalankan: {e}", RED))
            results.append((name, desc, -1, ""))
            continue

        output = (proc.stdout or "") + (proc.stderr or "")
        ok = proc.returncode == 0
        results.append((name, desc, proc.returncode, output.strip()))

        status = paint("BERSIH" if ok else "TEMUAN", GREEN if ok else RED)
        print(f"[{name}] {status} (exit {proc.returncode})")
        if ok and args.verbose and output:
            print(output)
        if not ok:
            # tampilkan baris temuan (bukan boilerplate summary)
            lines = [ln for ln in output.splitlines()
                     if ln and not ln.startswith(("hit(s) found", "TEMUAN"))]
            print("\n".join(lines))

    print()
    failed = [name for name, _, rc, _ in results if rc != 0]
    if failed:
        print(paint(f"KUALITAS: GAGAL - {len(failed)}/{len(CHECKS)} cek tidak bersih "
                    f"({', '.join(failed)}). Exit 1.", RED))
        return 1

    print(paint(f"KUALITAS: SEMUA {len(CHECKS)} CEK BERSIH. Exit 0.", GREEN))
    return 0


if __name__ == "__main__":
    sys.exit(main())