# Data Nyata & Turunan — Bab 8

> **PENTING — lisensi:** Berkas di folder ini bersumber dari data **nyata** yang
> lisensinya **berbeda dengan lisensi buku** (CC BY-SA 4.0). Khususnya data yang
> diturunkan dari **UNESCO/IOC Sea Level Station Monitoring Facility** berlisensi
> **CC BY-NC 4.0 (non-komersial)** — **tidak** untuk penggunaan komersial, dan
> turunannya tetap non-komersial. Sesuaikan penggunaan/distribusi Anda dengan
> lisensi penyedia masing-masing (lihat `back-matter/03-daftar-dataset-sumber.md`).

## Daftar Berkas

| Berkas | Sumber | Lisensi | Catatan |
|---|---|---|---|
| `cili_30d.csv` | IOC Sea Level Station Monitoring Facility (stasiun `cili`, Cilacap) | **CC BY-NC 4.0 (non-komersial)** | Observasi nyata ~30 hari (sampling 1–3 menit; deskripsi kolom di header) |
| `cili_1y_hourly_real.csv` | Turunan dari `cili_30d.csv` (skrip `make_tide_harmonic.py`) | **CC BY-NC 4.0 (non-komersial)** — turunan data IOC | Deret harmonik 1 tahun; **bukan** pengukuran langsung |
| `cilacap_psmsl_rlr_monthly.rlrdata` | PSMSL (stasiun Cilacap, format RLR) | Gratis; sitasi Holgate et al. (2013) | MSL bulanan jangka panjang |

## Catatan penggunaan

- Data nyata dipakai notebook tanpa internet; hasilnya tetap harus dilaporkan
  dengan framing jujur (contoh pendek, bukan validasi panjang) — lihat
  "Catatan kejujuran" pada `master.md` Bab 8.
- Jangan mengubah atau menghapus keterangan lisensi ini saat menyalin turunan.
- Data IOC (dan turunannya) **tidak boleh dipakai untuk produk/jasa komersial**;
  untuk penggunaan di luar ketentuan CC BY-NC, hubungi penyedia data
  (*data originator*) yang bersangkutan.

## Regenerasi

- IOC real-time:
  ```
  python scripts/download_ioc.py --source ioc --code cili --days 30 \
      --output data/raw/cili_30d.csv
  ```
- Deret harmonik 1 tahun: jalankan `scripts/make_tide_harmonic.py`
  (lihat `scripts/README.md`).