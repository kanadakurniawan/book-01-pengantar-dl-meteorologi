---
title: "Daftar Notebook dan DOI"
book: "Pengantar Deep Learning untuk Meteorologi"
---

# Daftar Notebook dan DOI

> Setiap bab memiliki satu notebook pendamping yang dapat dijalankan di Google
> Colab maupun lokal (Python 3.10+; TensorFlow 2.x, NumPy, Pandas,
> Matplotlib). Nama file diawali nomor bab untuk memudahkan urutan baca.

## Daftar Notebook

| Notebook | Bab | Topik | Catatan |
|---|---|---|---|
| `notebooks/ch-01-00_fondasi_tensorflow.ipynb` | 1 | Fondasi TensorFlow, tensor, setup Colab | Starter; wajib untuk pemula |
| `notebooks/ch-02-01_regresi_pasang_surut.ipynb` | 2 | Regresi; MLP; *baseline persistence* | Mini-kasus pasang surut |
| `notebooks/ch-03-02_klasifikasi_hujan.ipynb` | 3 | Klasifikasi biner/multi-kelas; *imbalance* | Data hujan/level bahaya |
| `notebooks/ch-04-03_optimasi_callbacks.ipynb` | 4 | Backprop manual (GradientTape); LR/batch; callbacks | — |
| `notebooks/ch-05-04_metrik_walkforward.ipynb` | 5 | Metrik MAE/RMSE, CSI/FAR/POD; walk-forward | *Pipeline* dipakai ulang di Bab 8–9 |
| `notebooks/ch-06-05_persiapan_data.ipynb` | 6 | Data terbuka (GHCND/CHIRPS) & ERA5; format; QC; fitur; split | Persiapan data lengkap |
| `notebooks/ch-07-06_lstm_gru.ipynb` | 7 | LSTM/GRU; *windowing*; multi-step | Menyambung Bab 8 |
| `notebooks/ch-08-07_studi_kasus_pasang_surut.ipynb` | 8 | Studi kasus pasang surut (Cilacap) *end-to-end* | Termasuk regenerasi Gambar 8.2/8.3 |
| `notebooks/ch-09-08_studi_kasus_curah_hujan_terbuka.ipynb` | 9 | Studi kasus hujan (data terbuka); klasifikasi + verifikasi | — |
| `notebooks/ch-10-09_operasional_arah_riset.ipynb` | 10 | *Drift*; *quantile*; SHAP; ensembel | — |

## Cara menjalankan

1. **Google Colab** (direkomendasikan): buka notebook via URL GitHub repo publik,
   atau unggah ke Colab. Gratis, tanpa instalasi.
2. **Lokal**: pastikan `pip install tensorflow numpy pandas matplotlib`
   (lihat Lampiran A dan *requirements* tiap notebook; Bab 8 butuh `requests`
   untuk skrip unduh, `xarray`/`netCDF4` opsional untuk Bab 6).

## Reproduksibilitas

- **Seed tetap** (`np.random.seed(42)`, `tf.random.set_seed(42)`) dipakai di
  seluruh notebook agar hasil dapat diulang.
- **Versi TensorFlow** tercatat di metadata notebook (atau di Bab 1/5 saat
  instalasi). Snapshot lingkungan (mulai dari rilis) dirilis di Zenodo.
- **Data**: contoh di repo + skrip unduh; snapshot data studi kasus di Zenodo
  (lihat "Daftar Dataset dan Sumber").

## DOI Terkait

| Entitas | DOI | Status |
|---|---|---|
| Buku utuh (PDF+DOCX) | `10.5281/zenodo.0000000` | **Placeholder** — didaftarkan saat rilis v2.0 |
| Dataset studi kasus (snapshot) | `10.5281/zenodo.0000000` | **Placeholder** — didaftarkan bersama data |
| Versi per-bab | — (tidak ada DOI per bab; sitasi stabil via DOI buku) | — |

> Prinsip: **1 buku = 1 DOI Zenodo** (konsep versi). Saat DOI dibuat,
> placeholder diganti dan disalin ke field `bookDOI` di semua `master.md`.

## Verifikasi cepat notebook

Untuk memastikan notebook tetap dijalankan (Fase 2 — Checklist Evaluasi D):

```bash
# per bab (contoh Bab 8)
python -m pytest --nbmake notebooks/ch-08-07_studi_kasus_pasang_surut.ipynb
```

Atau gunakan `nbconvert --execute` untuk eksekusi headless:

```bash
jupyter nbconvert --to notebook --execute notebooks/ch-08-*.ipynb
```