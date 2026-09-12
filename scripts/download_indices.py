#!/usr/bin/env python3
"""Unduh & rapikan indeks iklim yang dipakai Bab 6 & 9 (fitur ENSO/MJO).

Sumber (semua publik, tanpa akun):
  - ONI     : CPC NOAA, https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt
              (indeks ENSO 3-bulan: kolom ANOM siap pakai)
  - MEI.v2  : NOAA PSL, https://psl.noaa.gov/enso/mei/data/meiv2.data
  - RMM MJO : BoM, http://www.bom.gov.au/climate/mjo/graphics/rmm.74toRealtime.txt
              (RMM1/RMM2/phase/amplitude harian, 1974-realtime)

Pemakaian:
  python scripts/download_indices.py                        # unduh + parse semua
  python scripts/download_indices.py --outdir manuscripts/ch-09*/data/raw
  python scripts/download_indices.py --no-fetch             # hanya parse file lokal

Atribusi: Wolter & Timlin (1993/2011); Wheeler & Hendon (2004).
"""
from __future__ import annotations

import argparse
import io
import os
import sys
import urllib.request
import ssl
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = ROOT / "manuscripts" / "ch-09-studi-kasus-curah-hujan-terbuka" / "data" / "raw"
USER_AGENT = "Buku-DL-Meteorologi/1.0 (research)"

URLS = {
    "oni": "https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt",
    "mei_v2": "https://psl.noaa.gov/enso/mei/data/meiv2.data",
    "rmm": "http://www.bom.gov.au/climate/mjo/graphics/rmm.74toRealtime.txt",
}


def fetch(url: str, timeout: int = 90) -> bytes:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        return r.read()


def parse_oni(text: str) -> pd.DataFrame:
    rows = []
    for ln in text.splitlines():
        parts = ln.split()
        if len(parts) == 4 and parts[0] in ("DJF", "JFM", "FMA", "MAM", "AMJ",
                                            "MJJ", "JJA", "JAS", "ASO", "SON",
                                            "OND", "NDJ"):
            seas, yr, total, anom = parts
            yr = int(yr)
            month = {"DJF": 1, "JFM": 2, "FMA": 3, "MAM": 4, "AMJ": 5, "MJJ": 6,
                     "JJA": 7, "JAS": 8, "ASO": 9, "SON": 10, "OND": 11, "NDJ": 12}[seas]
            doi = {"DJF": 0, "JFM": 1, "FMA": 2, "MAM": 3, "AMJ": 4, "MJJ": 5,
                   "JJA": 6, "JAS": 7, "ASO": 8, "SON": 9, "OND": 10, "NDJ": 11}[seas]
            tanggal = pd.Timestamp(year=yr, month=month, day=1) + pd.DateOffset(months=doi)
            rows.append((seas, yr, float(total), float(anom), tanggal))
    df = pd.DataFrame(rows, columns=["seas", "yr", "total", "anom", "tanggal"])
    return df[["tanggal", "seas", "anom", "total"]].sort_values("tanggal")


def parse_mei(text: str) -> pd.DataFrame:
    rows = []
    for ln in text.splitlines():
        parts = ln.split()
        if len(parts) == 13 and parts[0].isdigit() and len(parts[0]) == 4:
            yr = int(parts[0])
            vals = [float(v) for v in parts[1:13]]
            for m, v in enumerate(vals, start=1):
                rows.append((pd.Timestamp(year=yr, month=m, day=1), v))
    df = pd.DataFrame(rows, columns=["tanggal", "mei_v2"])
    return df.sort_values("tanggal")


def parse_rmm(text: str) -> pd.DataFrame:
    rows = []
    for ln in text.splitlines():
        parts = ln.split()
        if len(parts) < 7:
            continue
        try:
            yr, mo, dy = int(parts[0]), int(parts[1]), int(parts[2])
            rmm1, rmm2 = float(parts[3]), float(parts[4])
            phase, amp = int(float(parts[5])), float(parts[6])
        except ValueError:
            continue
        if rmm1 > 9e6 or rmm2 > 9e6:  # missing (1.E36 / 999)
            continue
        rows.append((pd.Timestamp(year=yr, month=mo, day=dy), rmm1, rmm2, phase, amp))
    df = pd.DataFrame(rows, columns=["tanggal", "rmm1", "rmm2", "phase", "amp"])
    return df.sort_values("tanggal")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--outdir", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--no-fetch", action="store_true", help="pakai file mentah lokal")
    args = ap.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)

    raw = {
        "oni": args.outdir / "oni.ascii.txt",
        "mei_v2": args.outdir / "meiv2.data",
        "rmm": args.outdir / "rmm.74toRealtime.txt",
    }

    if not args.no_fetch:
        for key, url in URLS.items():
            print(f"[fetch] {key} <- {url}")
            raw[key].write_bytes(fetch(url))

    parsers = {"oni": parse_oni, "mei_v2": parse_mei, "rmm": parse_rmm}
    for key, fn in parsers.items():
        fp = raw[key]
        if not fp.exists():
            print(f"[skip] {key}: file mentah belum ada (jalankan tanpa --no-fetch)")
            continue
        df = fn(fp.read_text(encoding="utf-8", errors="replace"))
        out = args.outdir / f"indeks_{key}.csv"
        df.to_csv(out, index=False)
        n = len(df)
        yr = (df.tanggal.dt.year.min(), df.tanggal.dt.year.max()) if n else (None, None)
        print(f"[ok] {key}: {n} baris {yr} -> {out.name}")

    print("Selesai. File ~/.cdsapirc tidak diperlukan; semua sumber publik.")
    return 0


if __name__ == "__main__":
    sys.exit(main())