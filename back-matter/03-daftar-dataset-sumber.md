---
title: "Daftar Dataset dan Sumber"
book: "Pengantar Deep Learning untuk Meteorologi"
---

# Daftar Dataset dan Sumber

> Bagian ini mendokumentasikan sumber data yang dipakai di seluruh buku,
> termasuk lisensi dan cara akses. Konsisten dengan "Kriteria Sitasi" pada
> `outline.md`: setiap data diidentifikasi, lisensi dicantumkan, dan cara akses
> dijelaskan. Snapshot data untuk studi kasus dirilis di Zenodo bersama DOI
> buku (`bookDOI`).

## Data Meteorologi & Klimatologi

| Dataset | Penyedia | Cakupan | Lisensi & akses | Dipakai di |
|---|---|---|---|---|
| GHCN-Daily (stasiun global) | NOAA NCEI (`ncei.noaa.gov/pub/data/ghcn/daily`) | Global, termasuk 17+ stasiun Indonesia | Domain publik AS; atribusi Menne et al. (2012) | Bab 6 |
| ERA5 global reanalysis | Copernicus C3S (`cds.climate.copernicus.eu`) | Global, 1940–sekarang, harian/jam-an | Lisensi terbuka (setara CC-BY 4.0); atribusi wajib "Copernicus Climate Change Service (C3S)". Akses via API `cdsapi`. | Bab 6, 9 |
| CHIRPS (precipitation) | UC Santa Barbara / USGS (`chc.ucsb.edu`) | Global, ≥1981, harian | Domain publik (hak cipta dilepaskan); atribusi dianjurkan (kutip Funk et al. 2015); DOI: 10.1038/sdata.2015.66 | Bab 6, 9 |
| Indeks MJO (RMM) | Bureau of Meteorology (BoM), Australia & NOAA | Global, ≥1974 | Publik, gratis dengan atribusi Wheeler & Hendon (2004) | Bab 6, 9 |
| Indeks ENSO: MEI & Nino3.4 | NOAA (`psl.noaa.gov`) | Global, ≥1950-an | Publik, gratis; atribusi Wolter & Timlin (1993) dan NOAA PSL | Bab 6, 9 |

## Data Oseanografi (Pasang Surut & Muka Laut)

| Dataset | Penyedia | Cakupan | Lisensi & akses | Dipakai di |
|---|---|---|---|---|
| Sea Level Station Monitoring Facility | UNESCO/IOC (`ioc-sealevelmonitoring.org`) | Real-time/near-real-time, termasuk 24 stasiun Indonesia | Gratis riset/pendidikan; **CC BY-NC 4.0 (non-komersial)** — tidak untuk penggunaan komersial, dan data turunan tetap non-komersial; atribusi "UNESCO/IOC". Endpoint: `bgraph.php?code=<KODE>&period=<HARI>` | Bab 8 |
| PSMSL (MSL bulanan) | Permanent Service for Mean Sea Level (`psmsl.org`) | Global, puluhan tahun | Gratis dengan sitasi Holgate et al. (2013); format RLR/Metric | Bab 2*, 8 |
| UHSLC Research Quality | Univ. of Hawaii Sea Level Center (`uhslc.soest.hawaii.edu`) | Hourly/daily research quality | Gratis riset/pendidikan; atribusi UHSLC/NOAA | Bab 8 |
| Peta pasut & data pasang BIG | Badan Informasi Geospasial (`tides.big.go.id`) | Indonesia | Publik; atribusi BIG | Bab 2*, 6, 8 |

\* Bab 2 memakai data pasang surut contoh; keterangan sumber di bab tersebut
mengacu pada BIG (`tides.big.go.id`).

## Data Studi Kasus Buku (sampel & skrip)

| Item | Path | Keterangan |
|---|---|---|
| Sampel Cilacap hourly (1 th) | `manuscripts/ch-08-…/data/sample/cili_1y_hourly.csv` | Sintetik deterministik (seed=42) untuk notebook out-of-the-box; **bukan** observasi nyata |
| Skrip unduh IOC/UHSLC/PSMSL | `manuscripts/ch-08-…/scripts/download_ioc.py` | Unduh data nyata untuk eksperimen serius |
| Skrip generator sampel | `manuscripts/ch-08-…/scripts/generate_sample.py` | Re-generasi CSV deterministik |
| Skrip gambar studi kasus | `manuscripts/ch-08-…/scripts/generate_figures.py` | Regenerasi Gambar 8.2 & 8.3 dari sampel |

> **Konvensi letak file:** dataset sampel dan skrip per-bab disimpan di
> `manuscripts/ch-<NN>-*/data/` dan `manuscripts/ch-<NN>-*/scripts/`. Notebook
> Colab (`*.ipynb`) disimpan di folder `notebooks/` di root repo buku
> (prefix `ch-<NN>-`), bukan per-bab di dalam `manuscripts/`.

> **Rilis Zenodo:** saat buku dirilis, snapshot dataset studi kasus (pasang
> surut IOC/UHSLC/PSMSL, deret hujan CHIRPS/ERA5, fitur ERA5, indeks iklim)
> diunggah ke Zenodo dan dirujuk
> melalui `bookDOI` pada `master.md` tiap bab serta "Daftar Notebook dan DOI".
> Berkas snapshot yang diturunkan dari data **IOC (CC BY-NC 4.0)** tetap
> **non-komersial** dan dilisensikan terpisah dari buku (bukan bagian dari
> lisensi CC BY-SA buku).

## Prinsip penggunaan pada buku

1. **Preferensi sumber primer** — data resmi terbuka (NOAA, Copernicus,
   UNESCO/IOC, UHSLC, PSMSL, CHC UCSB) diutamakan; bukan salinan tak jelas.
   Seluruh studi kasus memakai data **terbuka** sehingga dapat direproduksi.
2. **Atribusi wajib** — cantumkan sumber, lisensi, dan versi di setiap
   gambar/tabel yang memakai data (lihat keterangan gambar di tiap bab).
3. **Data contoh sintetik** — dipakai agar notebook dapat dijalankan tanpa
   internet; hasil sintetik **tidak** diklaim sebagai hasil nyata.
4. **Lisensi data berbeda dengan lisensi buku** — buku CC BY-SA 4.0; lisensi
   data adalah milik masing-masing penyedia.
5. **Waspada data non-komersial** — lisensi buku mengizinkan penggunaan
   komersial, tetapi sebagian data (mis. IOC Sea Level Station Monitoring
   Facility, CC BY-NC 4.0) **tidak**. Saat mendistribusikan atau memublikasikan
   turunan yang memuat data non-komersial, kewajiban lisensi data tetap
   mengikuti penyedia; cantumkan peringatan non-komersial secara eksplisit di
   setiap produk turunan.