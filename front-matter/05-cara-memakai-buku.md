---
title: "Cara Memakai Buku Ini"
book: "Pengantar Deep Learning untuk Meteorologi"
---

# Cara Memakai Buku Ini

Bagian depan buku (*front matter*) ini bukan bagian dari bab, sehingga **tidak
dirilis ke Zenodo sebagai bab ber-DOI**. Dokumen ini menjadi satu sumber untuk
panduan penggunaan versi buku (halaman depan) dan halaman panduan di blog.

## Struktur dan urutan baca

- **Baca berurutan** untuk pengalaman mengalir: Bab 1–5 fondasi, Bab 6–7 data dan
  model sekuensial, Bab 8–9 studi kasus, Bab 10 operasional.
- **Atau baca per bab**: setiap bab berdiri sendiri dengan *sidebar* "Prasyarat:
  Bab …" yang memetakan urutan minimal yang perlu dikuasai sebelumnya.

| Rute baca | Bab | Tujuan |
|---|---|---|
| Jalur fondasi | 1 → 2 → 3 → 4 → 5 | Menguasai dasar regresi, klasifikasi, optimasi, dan evaluasi |
| Jalur data & deret waktu | 6 → 7 | Menguasai pengelolaan data meteo dan model LSTM/GRU |
| Jalur studi kasus | 8 → 9 | Praktik *end-to-end* dengan data Indonesia |
| Jalur operasional | 10 | Interpretasi, etika, dan arah riset |

## Konvensi yang dipakai di seluruh buku

- **Penomoran aset:** `Gambar bab.nomor`, `Tabel bab.nomor`,
  `Persamaan (bab.nomor)`, `Kode bab.nomor` — deret nomor masing-masing jenis
  reset di tiap bab.
- **Notasi matematis:** notasi terpusat di bagian "Glosarium dan Notasi";
  istilah Indonesia + Inggris ditulis seragam di seluruh buku.
- **Istilah baru** ditulis dalam bahasa Indonesia dengan istilah Inggris dalam
  tanda kurung pada pemunculan pertama (mis. "fungsi aktivasi (*activation
  function*)") dan dikumpulkan di glosarium.
- **Kode:** blok kode ditulis verbatim; nama identifier tidak diubah menjadi
  miring.

## Praktikkan dengan notebook

Setiap bab disertai notebook Colab yang dapat dieksekusi serta data yang
dirilis di Zenodo (DOI tercantum di metadata bab dan di bagian "Daftar Notebook
dan DOI"). Cara menjalankan:

1. Buka Google Colab (gratis, tanpa instalasi) dan impor notebook GitHub, atau
2. Jalankan secara lokal: `pip install tensorflow numpy pandas matplotlib`
   (persyaratan per-bab tercantum di notebook dan Lampiran A).

## Reproduksibilitas

- **Seed tetap** (`np.random.seed(42)`, `tf.random.set_seed(42)`) dipakai agar
  hasil dapat diulang.
- **Versi TensorFlow** tercatat di notebook dan Lampiran A.
- Data contoh sintetik dipakai agar notebook dapat berjalan tanpa internet;
  hasilnya **bukan** klaim data nyata.