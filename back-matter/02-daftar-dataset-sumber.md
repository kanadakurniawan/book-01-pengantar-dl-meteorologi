---
title: "Daftar Dataset dan Sumber"
book: "Pengantar Deep Learning untuk Meteorologi"
---

# Daftar Dataset dan Sumber

> Bagian ini mendokumentasikan sumber data yang dipakai di seluruh buku,
> termasuk lisensi dan cara akses. Konsisten dengan "Kriteria Sitasi" pada
> `outline.md`: setiap data diidentifikasi, lisensi dicantumkan, dan cara akses
> dijelaskan. Hash/snapshot untuk dataset studi kasus akan dirilis di Zenodo
> bersama data buku.

## Data Meteorologi & Klimatologi

| Dataset | Penyedia | Cakupan | Lisensi & akses | Dipakai di |
|---|---|---|---|---|
| Data online cuaca/iklim | BMKG (`dataonline.bmkg.go.id`) | Stasiun Indonesia (suhu, hujan, dsb.) | Gratis untuk riset/pendidikan; **redistribution dibatasi** — baca syarat BMKG | Bab 6, 9 |
| ERA5 global reanalysis | Copernicus C3S (`cds.climate.copernicus.eu`) | Global, 1940–sekarang, harian/jam-an | Lisensi non-komersial; atribusi "Copernicus Climate Change Service (C3S)". Akses via API `cdsapi`. | Bab 6, 9 |
| CHIRPS (precipitation) | UC Santa Barbara / USGS | Global, ≥1981, harian | Gratis dengan atribusi; lihat `doi:10.1038/sdata.2015.66` | Bab 6 |
| Indeks MJO (RMM) | BOM/Australia & Berri | Global, ≥1974 | Publik, gratis dengan atribusi Wheeler & Hendon (2004) | Bab 6, 9 |
| Indeks ENSO/MEI | NOAA | Global, ≥ 1950-an | Publik, gratis | Bab 6, 9 |

## Data Oseanografi (Pasang Surut & Muka Laut)

| Dataset | Penyedia | Cakupan | Lisensi & akses | Dipakai di |
|---|---|---|---|---|
| Sea Level Station Monitoring Facility | UNESCO/IOC (`ioc-sealevelmonitoring.org`) | Real-time/near-real-time, termasuk 24 station Indonesia | Gratis riset/pendidikan; atribusi "UNESCO/IOC". Endpoint: `bgraph.php?code=<KODE>&period=<HARI>` | Bab 8 |
| PSMSL (MSL bulanan) | Permanent Service for Mean Sea Level (`psmsl.org`) | Global, puluhan tahun | Gratis dengan sitasi Holgate et al. (2013); format RLR/Metric | Bab 2*, 8 |
| UHSLC Research Quality | Univ. of Hawaii Sea Level Center (`uhslc.soest.hawaii.edu`) | Hourly/daily research quality | Gratis riset/pendidikan; atribusi UHSLC/NOAA | Bab 8 |
| Peta pasut & data pasang BIG | Badan Informasi Geospasial (`tides.big.go.id`) | Indonesia | Publik; atribusi BIG | Bab 2*, 8 |

\* Bab 2 memakai data pasang surut contoh; keterangan sumber di bab tersebut
mengacu pada BIG (`tides.big.go.id`).

## Data Studi Kasus Buku (sample & skrip)

| Item | Path | Keterangan |
|---|---|---|
| Sample Cilacap hourly (1 th) | `manuscripts/ch-08-…/data/sample/cili_1y_hourly.csv` | Sintetik deterministik (seed=42) untuk notebook out-of-the-box; bukan observasi nyata |
| Skrip unduh IOC/UHSLC/PSMSL | `manuscripts/ch-08-…/scripts/download_ioc.py` | Unduh data nyata untuk eksperimen serius |
| Skrip generator sample | `manuscripts/ch-08-…/scripts/generate_sample.py` | Re-generasi CSV deterministik |

> **Konvensi letak file:** dataset sample dan skrip per-bab disimpan di
> `manuscripts/ch-<NN>-*/data/` dan `manuscripts/ch-<NN>-*/scripts/`. Notebook
> Colab (`*.ipynb`) disimpan di folder `notebooks/` di root repo buku
> dengan prefix `ch-<NN>-`, bukan per-bab di dalam `manuscripts/`.

> **Rilis Zenodo:** saat buku dirilis, snapshot dataset studi kasus (pasang
> surut IOC/UHSLC, data BMKG, fitur ERA5) akan diunggah ke Zenodo dengan
> **DOI data sendiri** dan dirujuk dari `bookDOI` pada `master.md` tiap bab.

## Prinsip penggunaan pada buku

1. **Preferensi sumber primer** — data resmi (BMKG, Copernicus, UNESCO/IOC,
   UHSLC, PSMSL, BIG) diutamakan; bukan salinan tak jelas.
2. **Atribusi wajib** — cantumkan sumber, lisensi, dan versi di setiap
   gambar/tabel yang memakai data (lihat keterangan gambar di tiap bab).
3. **Data contoh sintetik** — dipakai agar notebook dapat dijalankan tanpa
   internet; hasil sintetik **tidak** diklaim sebagai hasil nyata.
4. **Lisensi data berbeda dengan lisensi buku** — buku CC BY-SA 4.0;
   lisensi data adalah milik masing-masing penyedia.