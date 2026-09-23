---
title: "Daftar Gambar dan Daftar Tabel"
book: "Pengantar Deep Learning untuk Meteorologi"
---

# Daftar Gambar dan Daftar Tabel

> Daftar ini merekam seluruh aset visual (gambar) dan tabulasi (tabel) yang
> dipakai di seluruh bab. Penomoran mengikuti konvensi **bab.jenis-urutan**
> (mis. "Gambar 2.1", "Tabel 3.2") dan **reset di tiap bab**, sesuai register
> aset di `REGISTER.md`. Pada edisi cetak/PDF, daftar bernomor halaman dapat
> dihasilkan otomatis oleh LaTeX (`\listoffigures`, `\listoftables`).

## Daftar Gambar

| Nomor | Keterangan | Bab |
|---|---|---|
| Gambar 1.1 | Keterkaitan AI, *machine learning*, dan *deep learning* | 1 |
| Gambar 2.1 | Struktur neuron buatan (x → z → aktivasi a) | 2 |
| Gambar 2.2 | Arsitektur MLP contoh (1 → 8 ReLU → 8 ReLU → 1) | 2 |
| Gambar 3.1 | Kurva sigmoid memetakan z ke (0, 1) | 3 |
| Gambar 3.2 | *Confusion matrix* contoh data tidak seimbang | 3 |
| Gambar 4.1 | Contoh *learning curve* (*train* turun, *val* naik → *overfit*) | 4 |
| Gambar 5.1 | *Learning curve overfit* | 5 |
| Gambar 6.1 | Distribusi curah hujan harian (ekor panjang) | 6 |
| Gambar 7.1 | Ilustrasi RNN *unrolled* (state h) | 7 |
| Gambar 8.1 | Spektrum frekuensi pasang surut (M2/K1) | 8 |
| Gambar 8.2 | Prediksi vs aktual 7 hari (data sample Cilacap) | 8 |
| Gambar 8.3 | Residu per amplitudo dan fase pasang M2 | 8 |
| Gambar 9.1 | Precision–recall untuk hujan lebat | 9 |
| Gambar 9.2 | Verifikasi per kategori intensitas | 9 |
| Gambar 10.1 | Grafik kendali MAE (deteksi *drift*) | 10 |

## Daftar Tabel

| Nomor | Keterangan | Bab |
|---|---|---|
| Tabel 1.1 | Peta aplikasi *deep learning* dalam meteorologi | 1 |
| Tabel 1.2 | Contoh data cuaca mini → shape tensor | 1 |
| Tabel 1.3 | Glosarium mini bab 1 | 1 |
| Tabel 2.1 | Contoh target regresi meteorologi (satuan & sifat data) | 2 |
| Tabel 2.2 | Contoh deret raw pasang surut (nilai ilustratif) | 2 |
| Tabel 2.3 | Contoh *windowing* (dua langkah) pasang surut | 2 |
| Tabel 2.4 | Perbandingan MAE vs MSE | 2 |
| Tabel 3.1 | Perbedaan regresi vs klasifikasi | 3 |
| Tabel 3.2 | Perbandingan sigmoid vs softmax | 3 |
| Tabel 3.3 | Contoh data tidak seimbang | 3 |
| Tabel 3.4 | Struktur *confusion matrix* biner | 3 |
| Tabel 4.1 | Perbandingan fungsi aktivasi dari sisi gradien | 4 |
| Tabel 4.2 | SGD vs Adam | 4 |
| Tabel 5.1 | Underfit / fit / overfit | 5 |
| Tabel 5.2 | Panduan memilih metrik regresi | 5 |
| Tabel 5.3 | Kuartet verifikasi WMO (POD/FAR/CSI/TS) | 5 |
| Tabel 5.4 | Dua model, cerita metrik berbeda | 5 |
| Tabel 5.5 | Skema *walk-forward* (5 *fold*) | 5 |
| Tabel 6.1 | Sumber data utama (GHCND/CHIRPS, ERA5, CMIP6, PSMSL, satelit) | 6 |
| Tabel 6.2 | Perbandingan format berkas (CSV/NetCDF/GRIB) | 6 |
| Tabel 7.1 | Contoh *windowing* (w = 3, h = 1) | 7 |
| Tabel 7.2 | Pilihan panjang *window* | 7 |
| Tabel 7.3 | *Baseline* deret waktu | 7 |
| Tabel 7.4 | LSTM vs GRU | 7 |
| Tabel 7.5 | Strategi multi-langkah | 7 |
| Tabel 8.1 | Tipe pasang surut Indonesia | 8 |
| Tabel 8.2 | Harmonik vs *machine learning* | 8 |
| Tabel 8.3 | Stasiun Indonesia di sumber terbuka (IOC/UHSLC/PSMSL) | 8 |
| Tabel 8.4 | Ringkasan dataset Cilacap yang dibangun (sintetik deterministik) | 8 |
| Tabel 8.5 | Pilihan *window* (jam-an) | 8 |
| Tabel 8.6 | Contoh hasil MAE per *horizon* | 8 |
| Tabel 8.7 | *Skill score* relatif vs *persistence* | 8 |
| Tabel 9.1 | Fitur yang dibangun untuk stasiun | 9 |
| Tabel 9.2 | Kategori intensitas hujan | 9 |
| Tabel 9.3 | Verifikasi *threshold* (POD/FAR/CSI) | 9 |
| Tabel 9.4 | Rancangan eksperimen | 9 |
| Tabel 9.5 | Verifikasi per kategori | 9 |
| Tabel 10.1 | Prosedur *retraining* bertahap | 10 |
| Tabel 10.2 | Alur keputusan *retraining* | 10 |
| Tabel 10.3 | Etika penggunaan *deep learning* | 10 |

> Nomor tabel Bab 10 pada daftar ini menyesuaikan urutan sekuensial yang
> konsisten; periksa silang dengan `REGISTER.md` saat *review* final.