#!/usr/bin/env python3
"""Unduh ERA5 / ERA5-Land untuk stasiun buku ini via Copernicus Climate Data Store.

Pola: SATU request cdsapi per stasiun per TAHUN (semua bulan+hari dalam satu
request; terbukti lolos kuota besar CDS tanpa 403 — mengadaptasi
`era5_annual.py` dari riset F_TIDE). Variabel disesuaikan dengan fitur Bab 9
(Tabel 9.1): t2m, tp (total precipitation), u10, v10, msl.

Prasyarat (sekali):
  1. Akun gratis https://cds.climate.copernicus.eu
  2. CDS API key di ~/.cdsapirc  (url + key, jangan di-commit)
  3. pip install cdsapi xarray netCDF4

Pakai:
  python scripts/download_era5.py --dry                 # daftar request saja
  python scripts/download_era5.py                       # semua stasiun, semua tahun
  python scripts/download_era5.py --stations cilacap,jakarta --years 2020-2024
  python scripts/download_era5.py --stations kupang --years 2016-2016 --process
    # --process: ubah .nc -> CSV harian (tp->mm, t2m/u10/v10 -> rerata) di data/raw

Cakupan area: titik stasiun +-0.25 deg (box kecil). Resolusi default 6-jam-an
(tp masih akumulasi 0-6j; agregasi harian = sum). Gunakan --hourly bila perlu
jam-an penuh (request lebih berat).

Atribusi: Hersbach et al. (2023), ERA5 hourly data on single levels,
Copernicus CDS, doi:10.24381/cds.adbb2d47.
"""
from __future__ import annotations

import argparse
import io
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

# Stasiun buku: nama -> (lat, lon, rentang tahun default). Cilacap = pasut Bab 8;
# Jakarta/Kupang/Merauke = calon stasiun hujan Bab 9 (barat vs timur).
BOOK_STATIONS = {
    "cilacap": {"lat": -7.75, "lon": 109.02, "start": 2020, "end": 2026},
    "jakarta": {"lat": -6.183, "lon": 106.833, "start": 2010, "end": 2026},
    "kupang": {"lat": -10.167, "lon": 123.667, "start": 2010, "end": 2026},
    "merauke": {"lat": -8.467, "lon": 140.383, "start": 2010, "end": 2026},
}

# Fitur regional Bab 9 (Tabel 9.1): t2m, tp, u10, v10 (+ msl untuk konteks).
VARIABLES = [
    "2m_temperature",          # t2m, K
    "total_precipitation",     # tp, m (akumulasi per step waktu)
    "10m_u_component_of_wind", # u10, m/s
    "10m_v_component_of_wind", # v10, m/s
    "mean_sea_level_pressure", # msl, Pa
]
DATASET = "reanalysis-era5-single-levels"

# ERA5-Land (0.1 deg, lebih baik utk lahan): tidak punya msl -> pakai t2m/tp/u10/v10.
LAND_VARIABLES = [
    "2m_temperature",
    "total_precipitation",
    "10m_u_component_of_wind",
    "10m_v_component_of_wind",
]
LAND_DATASET = "reanalysis-era5-land"

MIN_VALID_BYTES = 20_000  # file titik kecil selalu > 20 KB utk ERA5


def output_dir(station: str) -> Path:
    d = ROOT / "manuscripts" / "ch-09-studi-kasus-curah-hujan-terbuka" / "data" / "era5" / station
    return d


def hours_list(hourly: bool):
    if hourly:
        return [f"{h:02d}:00" for h in range(24)]
    return ["00:00", "06:00", "12:00", "18:00"]


def has_year(station: str, year: int, land: bool = False) -> bool:
    prefix = "era5land" if land else "era5"
    fp = output_dir(station) / f"{prefix}_{station}_{year}.nc"
    return fp.exists() and fp.stat().st_size > MIN_VALID_BYTES


def plan_jobs(stations, years) -> list[tuple[str, dict, int]]:
    jobs = []
    for name in stations:
        cfg = BOOK_STATIONS.get(name)
        if cfg is None:
            print(f"  [skip] stasiun tak dikenal: {name}", file=sys.stderr)
            continue
        ys = years if years else list(range(cfg["start"], cfg["end"] + 1))
        for y in ys:
            jobs.append((name, cfg, y))
    return jobs


def download_one(client, name, cfg, year, hourly, land=False):
    st_dir = output_dir(name)
    st_dir.mkdir(parents=True, exist_ok=True)
    prefix = "era5land" if land else "era5"
    out_fp = st_dir / f"{prefix}_{name}_{year}.nc"
    lat, lon = cfg["lat"], cfg["lon"]
    area = [lat + 0.25, lon - 0.25, lat - 0.25, lon + 0.25]  # N, W, S, E
    client.retrieve(
        LAND_DATASET if land else DATASET,
        {
            "product_type": "reanalysis",
            "variable": LAND_VARIABLES if land else VARIABLES,
            "year": str(year),
            "month": [f"{m:02d}" for m in range(1, 13)],
            "day": [f"{d:02d}" for d in range(1, 32)],
            "time": hours_list(hourly),
            "area": area,
            "format": "netcdf",
        },
        str(out_fp),
    )
    print(f"  [ok] {name} {year} -> {out_fp.name}", flush=True)


def _nc_bytes_to_ds(raw: bytes):
    """Baca netCDF dari bytes (in-memory) -> xarray.Dataset.

    netCDF4 mendukung memory I/O (parameter memory=), aman di Windows tanpa
    file sementara. Normalisasi: koordinat waktu disatukan menjadi `time`.
    """
    import netCDF4

    import xarray as xr

    nc = netCDF4.Dataset("mem.nc", memory=raw)
    time_var = None
    for cand in ("valid_time", "time"):
        if cand in nc.variables:
            time_var = cand
            break
    times = None
    if time_var:
        tvals = nc.variables[time_var][:]
        units = nc.variables[time_var].units
        import cftime
        times = pd.to_datetime(cftime.num2date(tvals, units,
                                               only_use_cftime_datetimes=False,
                                               only_use_python_datetimes=True))
    data = {}
    n_time = None if times is None else len(times)
    skip = {"number", "expver", "latitude", "longitude"}
    for vn in nc.variables:
        if vn in skip or vn == time_var:
            continue
        arr = np.asarray(nc.variables[vn][:])
        # area request menghasilkan grid kecil (time,lat,lon) -> rata-rata lat/lon;
        # NaN dari masker lautan dilangkavana (nanmean)
        arr = np.nanmean(arr, axis=tuple(range(1, arr.ndim))) if arr.ndim > 1 else arr
        if arr.ndim != 1 or (n_time is not None and arr.shape[0] != n_time):
            continue
        data[vn] = ("time", arr)
    nc.close()
    ds = xr.Dataset(data)
    if times is not None:
        ds = ds.assign_coords(time=times)
    return ds


def _open_era5(src: Path):
    """Buka file ERA5 (bisa berupa .nc langsung ATAU .zip berisi netCDF dari CDS).

    CDS (format=netcdf) mengembalikan ZIP berisi file terpisah utk variabel
    *instant* (t2m/u10/v10/msl/...) dan *accum* (tp).
    """
    import zipfile

    import xarray as xr

    blob = src.read_bytes()
    if blob[:2] != b"PK":  # netCDF biasa
        ds = xr.open_dataset(src, engine="netcdf4")
        if "valid_time" in ds.variables:
            ds = ds.rename({"valid_time": "time"})
        return ds

    with zipfile.ZipFile(io.BytesIO(blob)) as zf:
        ds_inst = ds_acc = None
        for member in zf.namelist():
            if not member.endswith(".nc"):
                continue
            ds = _nc_bytes_to_ds(zf.read(member))
            if "accum" in member:
                ds_acc = ds
            elif "instant" in member:
                ds_inst = ds
            elif ds_inst is None:
                ds_inst = ds  # struktur generic: satu data_0.nc (mis. ERA5-Land)
        if ds_inst is None:
            raise RuntimeError("Zip ERA5 tidak memuat file data (instant/accum).")
        # gabung variabel accumulated (tp) jika dari file terpisah
        if ds_acc is not None and "tp" in ds_acc.variables:
            ds_inst["tp"] = ds_acc["tp"]
            ds_inst["tp"].attrs = {"long_name": "total precipitation", "units": "m"}
        return ds_inst
    raise FileNotFoundError(src)


def process_to_daily(station: str, year: int, land: bool = False) -> Path:
    """Ubah file ERA5 tahunan -> CSV harian (dirata-ratakan/akumulasi) untuk Bab 9.

    - tp   : meter -> mm (x1000); jumlah per hari (nilai step = akumulasi 6/1 jam)
    - t2m  : K -> degC, rerata harian
    - u10/v10 (dan msl bila ada): rerata harian
    Output: data/era5/<station>/{era5land|era5}_<station>_<year>_daily.csv
    """
    import numpy as np
    import xarray as xr

    st_dir = output_dir(station)
    prefix = "era5land" if land else "era5"
    src = st_dir / f"{prefix}_{station}_{year}.nc"
    if not src.exists():
        raise FileNotFoundError(src)

    ds = _open_era5(src)
    # normalisasi nama variabel CDS -> ringkas
    rename = {
        "2m_temperature": "t2m",
        "total_precipitation": "tp",
        "10m_u_component_of_wind": "u10",
        "10m_v_component_of_wind": "v10",
        "mean_sea_level_pressure": "msl",
    }
    ds = ds.rename({k: v for k, v in rename.items() if k in ds.variables})
    ds = ds[[v for v in ["t2m", "tp", "u10", "v10", "msl"] if v in ds.variables]]

    daily = {}
    if "t2m" in ds:
        daily["t2m_c"] = ds["t2m"].resample(time="1D").mean(dim="time").values - 273.15
    for var in ("u10", "v10", "msl"):
        if var in ds:
            daily[var] = ds[var].resample(time="1D").mean(dim="time").values
    if "tp" in ds:
        # Nilai tp pada step = akumulasi selama step tsb (6 jam utk default,
        # 1 jam utk --hourly); total harian = jumlah langsung.
        # Catatan: ERA5 single-levels untuk grid laut dekat pantai (mis. Teluk
        # Cilacap) cenderung LEBIH KERING dari stasiun darat; untuk hujan akurat
        # gunakan ERA5-Land (--land), CHIRPS/GSMaP, atau stasiun (Bab 6 & 9).
        daily["tp_mm"] = ds["tp"].resample(time="1D").sum(dim="time").values * 1000.0

    idx = pd.to_datetime(ds["time"].values).floor("D").unique()
    df = pd.DataFrame(daily, index=idx)
    df.index.name = "tanggal"
    out = st_dir / f"{prefix}_{station}_{year}_daily.csv"
    df.round(4).to_csv(out)
    ds.close()
    print(f"  [process] {station} {year} -> {out.name} ({len(df)} hari)", flush=True)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stations", default=None, help="koma; default semua")
    ap.add_argument("--years", default=None, help="rentang, mis. 2020-2024")
    ap.add_argument("--hourly", action="store_true", help="resolusi 1 jam (default 6 jam)")
    ap.add_argument("--land", action="store_true",
                    help="pakai ERA5-Land (0.1 deg; hujan darat lebih baik; tanpa msl)")
    ap.add_argument("--process", action="store_true", help="konversi .nc -> CSV harian")
    ap.add_argument("--dry", action="store_true", help="hanya daftar request")
    args = ap.parse_args()

    stations = [s.strip() for s in args.stations.split(",")] if args.stations \
        else list(BOOK_STATIONS.keys())
    years = None
    if args.years:
        y0, y1 = [int(x) for x in args.years.split("-")]
        years = list(range(y0, y1 + 1))

    jobs = plan_jobs(stations, years)
    print(f"Total request ERA5: {len(jobs)}")
    if not jobs:
        return 1

    if args.dry:
        for name, cfg, y in jobs:
            print(f"  {name} {y}  [{cfg['lat']:.4f}, {cfg['lon']:.4f}]")
        return 0

    import cdsapi
    client = cdsapi.Client()
    for name, cfg, y in jobs:
        if has_year(name, y, land=args.land):
            print(f"  [skip] {name} {y} sudah ada")
        else:
            try:
                print(f"[download] {name} {y}")
                download_one(client, name, cfg, y, args.hourly, land=args.land)
            except Exception as e:
                print(f"  [ERR] {name} {y}: {str(e)[:300]}", file=sys.stderr)
        if args.process:
            try:
                process_to_daily(name, y, land=args.land)
            except Exception as e:
                print(f"  [process ERR] {name} {y}: {str(e)[:300]}", file=sys.stderr)
    print("Selesai. Output: manuscripts/ch-09*/data/era5/<station>/")
    return 0


if __name__ == "__main__":
    sys.exit(main())