---
title: "Lampiran"
book: "Pengantar Deep Learning untuk Meteorologi"
---

# Lampiran

## Lampiran A — Reproduksibilitas dan Lingkungan Komputasi

Buku ini dirancang agar seluruh kode dapat dijalankan ulang (reproducible).
Konvensi yang dipakai di seluruh notebook:

- **`seed` tetap:** `np.random.seed(42)` dan `tf.random.set_seed(42)` di awal
  setiap notebook agar hasil dapat diulang.
- **Versi library:** versi TensorFlow/Keras yang digunakan tercatat di notebook
  (biasanya di sel pertama) dan di metadata *release* Zenodo.
- **Python:** 3.10+; paket inti: `tensorflow`, `numpy`, `pandas`,
  `matplotlib`. Paket tambahan per bab:
  - Bab 6: `xarray`, `netCDF4` (opsional, untuk data NetCDF) dan `cfgrib`
    (opsional, untuk GRIB).
  - Bab 8: `requests` untuk skrip unduh IOC/UHSLC/PSMSL.
  - Bab 9: `scikit-learn` (opsional, permutasi penting), `shap` (opsional).
- **Data:** data contoh sintetik di-*commit* di repositori; data riil diunduh
  melalui skrip yang disediakan (lihat "Daftar Dataset dan Sumber"). Snapshot
  dataset studi kasus akan diunggah ke Zenodo saat rilis.

## Lampiran B — Konvensi Penulisan dan Penomoran Aset

| Konvensi | Aturan |
|---|---|
| Penomoran aset | `Gambar bab.nomor`, `Tabel bab.nomor`, `Persamaan (bab.nomor)`, `Kode bab.nomor` — deret nomor tiap jenis reset di tiap bab |
| Rujukan aset | setiap aset harus dirujuk di teks; nomor tidak boleh ganda atau loncat |
| Notasi | terpusat di "Glosarium dan Notasi"; istilah Indonesia + Inggris konsisten |
| Sitasi | IEEE bernomor `[n]` sesuai kemunculan pertama; daftar per bab di `refs.bib`; daftar agregat di "Daftar Pustaka" |
| Istilah asing | dicetak miring bila belum diserap KBBI (PUEBI §18) |
| Lesapnya nama merek | TensorFlow, Keras, Google Colab, NumPy, dst. tidak dimiringkan |

> Register lengkap penomoran aset dan sitasi per bab ada di `REGISTER.md`
> (berkas pendamping pengembangan, tidak dirilis sebagai bab).