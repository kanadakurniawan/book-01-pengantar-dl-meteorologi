#!/usr/bin/env python3
"""Unduh & ekstrasi deret harian CHIRPS (grid 0.05°) untuk titik pilihan (Bab 9).

CHIRPS v2.0 daily:
  https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/tifs/p05/<YYYY>/chirps-v2.0.YYYY.MM.DD.tif.gz
Grid global p05 meliputi 60N..40S (2000x7200 px; 0.05 deg). Nilai -9999 = pixel
laut/hilang (CHIRPS satelit-gauge); titik dekat pantai bisa ter-laut -> skrip
memakai pixel VALID TERDEKAT dalam radius s (default 5 px) agar robust.

Pakai:
  python scripts/download_chirps.py --lat -6.2 --lon 106.9 --start 2024-01-01 --end 2024-03-01 \
      --outdir manuscripts/ch-09*/data/raw
  # cached raw .tif.gz di <outdir>/chirps_raw/; keluaran chirps_<nama>_daily.csv

Dependensi: pip install tifffile
Kutip: Funk et al. (2015), doi:10.1038/sdata.2015.66.
"""
from __future__ import annotations

import argparse
import gzip
import io
import ssl
import sys
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://data.chc.ucsb.edu/products/CHIRPS-2.0/global_daily/tifs/p05"
USER_AGENT = "Buku-DL-Meteorologi/1.0 (research)"
NODATA = -9999.0


def fetch(url: str, timeout: int = 120) -> bytes:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
        return r.read()


def load_day(raw_dir: Path, d: date) -> np.ndarray:
    import tifffile

    fname = f"chirps-v2.0.{d.year}.{d.month:02d}.{d.day:02d}.tif.gz"
    raw = raw_dir / fname
    if not raw.exists():
        url = f"{BASE}/{d.year}/{fname}"
        print(f"  [fetch] {d} <- {url}")
        raw.write_bytes(fetch(url))
    arr = tifffile.imread(io.BytesIO(gzip.decompress(raw.read_bytes())))
    return np.asarray(arr, dtype=np.float32)


_GEO = {"x0": None, "y0": None, "dx": 0.05, "dy": 0.05}


def _read_geo(raw_dir: Path, d: date):
    """Baca geotransform CHIRPS dai tag TIFF (ModelTiepoint/ModelPixelScale).

    Grid p05 global_daily berbervariasi (60N..40S atau 50N..50S); tidak
    berandom: baca dari file.
    """
    import tifffile

    if _GEO["x0"] is not None:
        return
    fname = f"chirps-v2.0.{d.year}.{d.month:02d}.{d.day:02d}.tif.gz"
    raw = raw_dir / fname
    if not raw.exists():
        raw.write_bytes(fetch(f"{BASE}/{d.year}/{fname}"))
    with tifffile.TiffFile(io.BytesIO(gzip.decompress(raw.read_bytes()))) as t:
        page = t.pages[0]
        tie = page.tags[33922].value   # pixel(0,0) -> (x0, y0, z0)
        scale = page.tags[33550].value  # dx, dy, dz
    _GEO["x0"], _GEO["y0"] = float(tie[3]), float(tie[4])
    _GEO["dx"], _GEO["dy"] = float(scale[0]), float(scale[1])


def nearest_valid(arr: np.ndarray, lat: float, lon: float, r: int = 12):
    """Pixcil CHIRPS terdekat yang VALID (nilai >= 0; -9999 = laut/hilang)."""
    row = int(np.rint((_GEO["y0"] - lat) / _GEO["dy"]))
    col = int(np.rint((lon - _GEO["x0"]) / _GEO["dx"]))
    h, w = arr.shape
    for rad in range(r + 1):
        for dr in range(-rad, rad + 1):
            for dc in range(-rad, rad + 1):
                rr, cc = row + dr, col + dc
                if 0 <= rr < h and 0 <= cc < w and arr[rr, cc] >= 0:
                    return float(arr[rr, cc])
    return float("nan")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--lat", type=float, required=True)
    ap.add_argument("--lon", type=float, required=True)
    ap.add_argument("--name", default=None, help="nama titik (default lat-lon)")
    ap.add_argument("--start", required=True, help="YYYY-MM-DD")
    ap.add_argument("--end", required=True, help="YYYY-MM-DD")
    ap.add_argument("--radius", type=int, default=12, help="radius pixel utk terdek valid (default 12 ~ 0.6 deg)")
    ap.add_argument("--outdir", type=Path,
                    default=ROOT / "manuscripts" / "ch-09-studi-kasus-curah-hujan-terbuka" / "data" / "raw")
    args = ap.parse_args()

    name = args.name or f"lat{args.lat:.2f}_lon{args.lon:.2f}".replace("-", "m").replace(".", "p")
    raw_dir = args.outdir / "chirps_raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    start = datetime.strptime(args.start, "%Y-%m-%d").date()
    end = datetime.strptime(args.end, "%Y-%m-%d").date()
    days = [(start + timedelta(days=k)) for k in range((end - start).days + 1)]

    rows = []
    _read_geo(raw_dir, days[0])  # ambil geotransform dari file pertama
    for d in days:
        arr = load_day(raw_dir, d)
        rows.append((pd.Timestamp(d), nearest_valid(arr, args.lat, args.lon, args.radius)))
    df = pd.DataFrame(rows, columns=["tanggal", "chirps_mm"])
    out = args.outdir / f"chirps_{name}_daily.csv"
    df.to_csv(out, index=False)
    n_valid = int(df.chirps_mm.notna().sum())
    print(f"[ok] {len(df)} hari, {n_valid} valid -> {out}")
    print("kolom: tanggal, chirps_mm (mm/hari; NaN bila semua pixcel sekitarnya laut/hilang)")
    return 0


if __name__ == "__main__":
    sys.exit(main())