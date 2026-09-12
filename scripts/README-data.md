# Skrip Data — Buku *Pengantar Deep Learning untuk Meteorologi*

Data nyata untuk studi kasus (Bab 6, 8, 9) bisa diambil langsung lewat skrip di
folder ini. Semua output disimpan di `manuscripts/ch-0N-*/data/raw/` (di-`.gitignore`),
kecuali dinyatakan lain.

## Peta skrip

| Skrip | Fungsi | Sumber | Butuh akun? |
|---|---|---|---|
| `download_era5.py` | ERA5 (t2m, tp, u10, v10, msl) per stasiun per tahun → `.nc`, opsional CSV harian | Copernicus CDS | ✅ CDS (gratis, `~/.cdsapirc`) |
| `download_ghcn.py` | Stasiun harian observasi (PRCP/TMAX/TMIN/TAVG) → CSV | NOAA GHCN-Daily | ❌ |
| `download_chirps.py` | Deret hujan harian CHIRPS (0,05°) untuk titik pilihan | CHC UCSB | ❌ |
| `download_indices.py` | Indeks ENSO (ONI, MEI.v2) & MJO (RMM) → CSV | CPC NOAA, NOAA PSL, BoM | ❌ |
| `make_tide_harmonic.py` | Rekonstruksi 1 tahun pasang surut dari 30 hari IOC via `utide` | Observasi IOC (derivasi) | ❌ |
| `generate_figures_all.py` | Regenerasi seluruh gambar buku dari data sintetik | – | – |

## 1. ERA5 — `download_era5.py`

```bash
pip install cdsapi xarray netCDF4      # sekali
python scripts/download_era5.py --dry                       # lihat daftar request
python scripts/download_era5.py --stations cilacap --years 2024-2025
python scripts/download_era5.py --stations kupang --years 2016-2016 --process
```

- Default 6-jam-an (cukup untuk fitur harian; request tahunan kecil ~200 KB, terbukti
  lolos quota CDS). `--hourly` untuk jam-an penuh.
- `--process` menulis `era5_<stasiun>_<thn>_daily.csv` dengan `tp`→mm (sum per hari;
  nilai tp 6-jam CDS = akumulasi 6 jam terakhir, bukan kumulatif harian),
  `t2m`→°C (mean), `u10/v10/msl` (mean) — siap dipakai sebagai fitur regional
  notebook Bab 9 (ingat: lag minimal 1 hari terhadap target).
- ⚠️ ERA5 single-levels untuk grid **laut dekat pantai** (mis. Teluk Cilacap)
  cenderung **lebih kering** dari stasiun darat (`tp` underestimated). Untuk
  hujan akurat/lahan, gunakan **ERA5-Land**, CHIRPS/GSMaP, atau stasiun
  (GHCN-Daily) sebagai sumber utama (lihat Bab 6 & 9). Variabel suhu/angin/tekanan
  ERA5 tetap kuat dipakai sebagai fitur regional.
- Konfigurasi stasiun di `BOOK_STATIONS` pada file itu (cilacap, jakarta, kupang,
  merauke; tambahkan sesuai kebutuhan).

## 2. Stasiun harian — `download_ghcn.py`

```bash
python scripts/download_ghcn.py --list           # stasiun Indonesia yang dipakai
python scripts/download_ghcn.py                  # unduh+parse semua stasiun
python scripts/download_ghcn.py --station ID000096805 --fetch
```

Keluaran: `ghcn_<nama>_daily.csv` (`prcp_mm`, `tmax_c`, `tmin_c`, `tavg_c`).
GHCN-Daily adalah sumber **observasi** stasiun terbuka untuk curah hujan saat data
stasiun nasional berizin tidak tersedia.

## 2b. CHIRPS titik — `download_chirps.py`

```bash
python scripts/download_chirps.py --lat -6.2 --lon 106.9 --name jakarta \
    --start 2024-01-01 --end 2024-12-31
```

Ekstrasi deret hujan harian CHIRPS (`chirps_<nama>_daily.csv`, mm/hari). Pixel yang
bertaruh laut memakai nilai terdekat valid (radius ±0,6°). Caching raw `.tif.gz`
di `<outdir>/chirps_raw/`. Butuh `pip install tifffile`.

## 3. Indeks iklim — `download_indices.py`

```bash
python scripts/download_indices.py
```

Menulis `indeks_oni.csv`, `indeks_mei_v2.csv`, `indeks_rmm.csv` (fitur ENSO/MJO
Tabel 9.1). Semua publik, tanpa akun. `--no-fetch` untuk parse file mentah lokal.

## 4. Pasang surut 1 tahun — `make_tide_harmonic.py`

Karena endpoint IOC hanya menyediakan ±30 hari terakhir:

```bash
python scripts/download_ioc.py --source ioc --code cili --days 30 \
    --output manuscripts/ch-08*/data/raw/cili_30d.csv       # (skrip di ch-08)
python scripts/make_tide_harmonic.py \
    --input manuscripts/ch-08*/data/raw/cili_30d.csv \
    --output manuscripts/ch-08*/data/raw/cili_1y_hourly_real.csv \
    --days 366 --lat -7.75
```

Hasil adalah **derivasi harmonik dari observasi nyata** (bukan observasi langsung);
jangan dilaporkan sebagai data stasiun. Fallback numpy tersedia bila `utide` tidak ada.

## Aturan & atribusi

- Lisensi data mengikuti masing-masing penyedia (CDS, NOAA, BoM); buku CC BY-SA.
- Jangan commit: `~/.cdsapirc`, `manuscripts/*/data/raw/`, `manuscripts/*/data/era5/`.
- Untuk distribusi, unggah snapshot data ke Zenodo (`bookDOI`) supaya pembaca tidak
  perlu akun pribadi.