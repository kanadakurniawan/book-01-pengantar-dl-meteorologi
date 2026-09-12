#!/usr/bin/env python3
"""Rekonstruksi deret pasang surut 1 tahun dari observasi IOC 30 hari (Bab 8).

Masalah: endpoint IOC hanya menyediakan ~30 hari terakhir. Karena pasang surut
sangat periodik, kita bisa *pasang konstituen harmonik* pada data 30 hari nyata
(utide.solve) lalu *prediksi* 1 tahun ke depan dengan utide.predic. Hasilnya
deret jam-jaman "real-derived" (bukan murni sintetik) untuk walk-forward.

Pakai:
  python scripts/make_tide_harmonic.py \
      --input manuscripts/ch-08*/data/raw/cili_30d.csv \
      --output manuscripts/ch-08*/data/raw/cili_1y_hourly_real.csv \
      --years 1 --lat -7.75

Jika `utide` tidak terpasang, fallback numpy least-squares untuk konstituen
M2 S2 K1 O1 N2. Catatan: ini DERIVASI dari observasi nyata, bukan observasi;
hasil tidak boleh dilaporkan seolah-olah data stasiun.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd


def fit_predict_utide(ser: pd.Series, n_days: float, lat: float) -> pd.Series:
    import warnings

    import utide

    warnings.filterwarnings("ignore", category=RuntimeWarning)  # noise periodogram utide
    t = ser.index.to_numpy().astype("datetime64[s]").astype("float64") / 86400.0  # days
    h = ser.to_numpy().astype(float)
    coef = utide.solve(t, h, lat=lat, conf_int="linear", verbose=False)
    t_pred = np.arange(t[0], t[-1] + n_days, 1.0 / 24.0)  # hourly, dari awal window
    out = utide.reconstruct(t_pred, coef)
    p = np.asarray(out["h"]).squeeze()
    idx = pd.to_datetime(t_pred * 86400.0, unit="s")
    return pd.Series(p, index=idx).rename("tinggi")


FALLBACK_SPEEDS = {  # derajat/jam untuk fit numpy (Bates/UTide standar)
    "M2": 28.984104, "S2": 30.0, "K1": 15.041069, "O1": 13.943035, "N2": 28.439730,
}


def fit_predict_numpy(ser: pd.Series, n_days: float, lat: float) -> pd.Series:
    t = ser.index.to_numpy().astype("datetime64[s]").astype("float64") / 86400.0  # days
    h = ser.to_numpy().astype(float)
    speed = np.array([FALLBACK_SPEEDS[k] for k in FALLBACK_SPEEDS])
    ang = 2 * np.pi * speed[None, :] * (t[:, None] * 24.0) / 360.0  # t dalam JAM di sini
    A = np.column_stack([np.cos(ang), np.sin(ang)])
    coef, *_ = np.linalg.lstsq(A, h, rcond=None)
    t_pred = np.arange(t[0], t[-1] + n_days, 1.0 / 24.0)
    angp = 2 * np.pi * speed[None, :] * (t_pred[:, None] * 24.0) / 360.0
    p = np.column_stack([np.cos(angp), np.sin(angp)]) @ coef
    idx = pd.to_datetime(t_pred * 86400.0, unit="s")
    return pd.Series(p, index=idx).rename("tinggi")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", type=Path, required=True, help="CSV IOC (kolom time, tinggi)")
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--days", type=float, default=366.0,
                    help="panjang deret rekonstruksi (hari); default 366")
    ap.add_argument("--lat", type=float, default=-7.75, help="lintang stasiun")
    ap.add_argument("--no-utide", action="store_true", help="paksa fallback numpy")
    args = ap.parse_args()

    df = pd.read_csv(args.input, parse_dates=["time"]).sort_values("time")
    ser = df.set_index("time")["tinggi"].astype(float).dropna()
    ser = ser[~ser.index.duplicated(keep="first")]

    try:
        if args.no_utide:
            print("[info] pakai numpy fallback (M2/S2/K1/O1/N2)")
            out = fit_predict_numpy(ser, args.days, args.lat)
        else:
            print("[info] pakai utide (solve+predic)")
            out = fit_predict_utide(ser, args.days, args.lat)
    except Exception as e:
        print(f"[warn] utide gagal ({e}), pakai numpy fallback", file=sys.stderr)
        out = fit_predict_numpy(ser, args.days, args.lat)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    out_df = out.round(4).to_frame().reset_index().rename(columns={"index": "time"})
    out_df.to_csv(args.output, index=False)
    print(f"[ok] {len(out_df)} baris -> {args.output}")
    print("Catatan: hasil ini DERIVASI harmonik dari 30 hari observasi IOC+, bukan observasi langsung.")


if __name__ == "__main__":
    sys.exit(main())