#!/usr/bin/env python3
"""Unduh & parse data stasiun harian observasi dari NOAA GHCN-Daily untuk Bab 9.

GHCN-Daily adalah dataset global stasiun terbuka (termasuk 17+ stasiun Indonesia) dari
NOAA NCEI: https://www.ncei.noaa.gov/pub/data/ghcn/daily/
GHCND menjadi sumber observasi stasiun terbuka pengganti data nasional yang berizin.

Pemakaian:
  python scripts/download_ghcn.py                          # daftar stasiun buku
  python scripts/download_ghcn.py --fetch                  # unduh ulang .dly
  python scripts/download_ghcn.py --station ID000096805 --outdir manuscripts/ch-09*/
      data/raw
  python scripts/download_ghcn.py --parse-only             # pakai .dly yang sudah ada

Format nilai GHCN (.dly): PRCP = 0.1 mm, TMAX/TMIN/TAVG = 0.1 C; -9999 = hilang.
Kutip: Menne et al. (2012), J. Atmos. Oceanic Technol. 29, 897-910, doi:10.1175/JTECH-D-11-00103.1.
"""
from __future__ import annotations

import argparse
import io
import os
import sys
import urllib.request
import ssl
from pathlib import Path
from datetime import datetime, timedelta

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = ROOT / "manuscripts" / "ch-09-studi-kasus-curah-hujan-terbuka" / "data" / "raw"
BASE = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/all/"
USER_AGENT = "Buku-DL-Meteorologi/1.0 (research)"

# Stasiun buku: GHCN ID, nama, posisi (barat vs timur untuk Bab 9)
GHCN_STATIONS = {
    "ID000096745": ("jakarta", -6.183, 106.833),
    "ID000096805": ("cilacap", -7.733, 109.017),
    "ID000097372": ("kupang", -10.167, 123.667),
    "ID000097980": ("merauke", -8.467, 140.383),
}


def fetch(url: str, timeout: int = 120) -> bytes:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        return r.read()


def parse_dly(text: bytes) -> pd.DataFrame:
    """Parse file .dly (fixed-width) -> DataFrame harian (prcp, tmax, tmin, tavg).

    Skema .dly: ID(11) YR(4) MONTH(2) ELEMENT(4) lalu 31 blok; tiap blok VALUE(5) MFLAG(1)
    QFLAG(1) SFLAG(1). PRCP/TMAX/TMIN dalam 0.1 mm / 0.1 C; -9999 = missing.
    """
    rows = []
    for line in text.decode("utf-8", "replace").splitlines():
        if len(line) < 21:
            continue
        sid = line[0:11]
        year = int(line[11:15])
        month = int(line[15:17])
        elem = line[17:21]
        for day in range(1, 32):
            off = 21 + (day - 1) * 8
            if off + 5 > len(line):
                break
            try:
                val = int(line[off:off + 5])
            except ValueError:
                continue
            if val == -9999:
                continue
            rows.append((sid, datetime(year, month, day), elem, val))
    df = pd.DataFrame(rows, columns=["id", "tanggal", "elem", "val"])
    if df.empty:
        return pd.DataFrame(columns=["tanggal", "prcp_mm", "tmax_c", "tmin_c", "tavg_c"])

    units = {"PRCP": 0.1, "TMAX": 0.1, "TMIN": 0.1, "TAVG": 0.1}
    names = {"PRCP": "prcp_mm", "TMAX": "tmax_c", "TMIN": "tmin_c", "TAVG": "tavg_c"}
    df = df[df.elem.isin(units)]
    df["val"] = df.apply(lambda r: r.val * 0.1 if r.elem in ("PRCP", "TMAX", "TMIN", "TAVG") else r.val, axis=1)
    df["col"] = df["elem"].map(names)
    out = df.pivot_table(index="tanggal", columns="col", values="val", aggfunc="mean").reset_index()
    for col in ["prcp_mm", "tmax_c", "tmin_c", "tavg_c"]:
        if col not in out.columns:
            out[col] = pd.NA
    return out[["tanggal", "prcp_mm", "tmax_c", "tmin_c", "tavg_c"]].sort_values("tanggal")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--station", default=None, help="GHCN ID (mis. ID000096805); default semua")
    ap.add_argument("--outdir", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--fetch", action="store_true", help="unduh ulang .dly meski sudah ada")
    ap.add_argument("--parse-only", action="store_true", help="hanya parse .dly yang ada")
    ap.add_argument("--list", action="store_true", help="daftar stasiun buku")
    args = ap.parse_args()

    if args.list:
        for sid, (name, lat, lon) in GHCN_STATIONS.items():
            print(f"{sid}  {name:<10} ({lat}, {lon})")
        return 0

    ids = [args.station] if args.station else list(GHCN_STATIONS.keys())
    args.outdir.mkdir(parents=True, exist_ok=True)

    for sid in ids:
        name, lat, lon = GHCN_STATIONS.get(sid, (sid, float("nan"), float("nan")))
        dly = args.outdir / f"ghcn_{name}.dly"
        if args.parse_only and not dly.exists():
            print(f"[skip] {sid} {name}: file .dly belum ada; jalankan --fetch")
            continue
        if args.fetch or not dly.exists():
            url = BASE + sid + ".dly"
            print(f"[fetch] {sid} {name} <- {url}")
            dly.write_bytes(fetch(url))
        body = dly.read_bytes()
        df = parse_dly(body)
        out = args.outdir / f"ghcn_{name}_daily.csv"
        df.to_csv(out, index=False)
        n = len(df)
        yrs = (df.tanggal.dt.year.min(), df.tanggal.dt.year.max()) if n else (None, None)
        print(f"[ok] {sid} {name}: {n} baris  {yrs}  -> {out.name}")

    print("Selesai. Untuk BAB 9: gunakan ghcn_*_daily.csv sebagai stasiun/pelengkap observasi.")
    return 0


if __name__ == "__main__":
    sys.exit(main())