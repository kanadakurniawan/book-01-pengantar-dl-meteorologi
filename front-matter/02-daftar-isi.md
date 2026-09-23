---
title: "Daftar Isi"
book: "Pengantar Deep Learning untuk Meteorologi"
---

# Daftar Isi

## Front Matter

- Halaman Judul
- Hak Cipta dan Lisensi
- Daftar Isi
- Daftar Gambar dan Daftar Tabel
- Prakata
- Cara Memakai Buku Ini
- Glosarium dan Notasi

## Bagian I — Fondasi (Bab 1–5)

- **Bab 1. Pengantar: Deep Learning untuk Meteorologi**
  - Posisi AI, *machine learning*, dan *deep learning*
  - Peta aplikasi meteorologi yang dibahas buku ini
  - Kapan *deep learning* layak dipakai (vs *baseline* statistik)
  - Menyiapkan Google Colab + TensorFlow, dan tensor pertama
- **Bab 2. Regresi: Perceptron dan Jaringan Saraf untuk Prediksi Besaran**
  - Anatomi neuron: bobot, bias, fungsi aktivasi
  - Dari regresi linear ke MLP; kapan non-linearitas diperlukan
  - Mini-kasus pasang surut: *windowing*, *baseline persistence*, MAE vs MSE
  - Split data deret waktu yang mencegah *leakage*
- **Bab 3. Klasifikasi: Mengenali Kategori Fenomena Cuaca**
  - Sigmoid/softmax dan cross-entropy
  - *Class imbalance* dan mengapa akurasi menipu
  - Precision/recall/F1, *confusion matrix*, pengenalan CSI/FAR
  - Trade-off *threshold* ala praktisi peramalan
- **Bab 4. Backpropagation, Optimasi dan Pelatihan**
  - Intuisi *gradient descent* dan *backpropagation* (aturan rantai)
  - Fungsi aktivasi ditinjau dari gradien; *vanishing gradient*
  - *Learning rate*, *batch size*, *epoch*; SGD vs Adam
  - Callback: *early stopping*, ModelCheckpoint, ReduceLROnPlateau
- **Bab 5. Overfitting, Regularisasi dan Evaluasi untuk Data Iklim**
  - Bias-variance, underfit/overfit, *learning curve*
  - L2, *dropout*, *early stopping*
  - Metrik domain: MAE/RMSE/R²/Willmott/KGE dan CSI/FAR/POD/TS
  - Cross-validation deret waktu: *walk-forward*/*blocked* anti-*leakage*

## Bagian II — Data dan Model Sekuensial (Bab 6–7)

- **Bab 6. Data Meteorologi: Sumber, Kualitas dan Persiapan**
  - Sumber data: stasiun & grid terbuka, ERA5, CMIP6, pasang surut, satelit; lisensi
  - Format CSV/NetCDF/GRIB; nilai hilang, *outlier*, imputasi dasar
  - Eksplorasi: dekomposisi musiman, distribusi, korelasi silang
  - Feature engineering: lag, musiman, ENSO/MJO
  - Normalisasi (fit hanya pada *train*) dan split berbasis waktu
- **Bab 7. Deret Waktu dan Model Sekuensial: RNN, LSTM, GRU**
  - *Windowing* dan *horizon*: prediksi satu dan multi-langkah
  - *Baseline* dulu: *persistence*, mean, AR — DL harus mengalahkannya
  - Intuisi RNN → LSTM → GRU (gate ingatan/lupa) dan keterbatasannya
  - Arsitektur praktis univariate/multivariate; strategi multi-step

## Bagian III — Studi Kasus (Bab 8–9)

- **Bab 8. Studi Kasus: Prediksi Pasang Surut di Perairan Indonesia (Contoh Cilacap)**
  - Konteks banjir rob pesisir dan tipe pasang surut Indonesia
  - Memilih stasiun: Cilacap (GLOSS #291) dan sumber data terbuka
  - Alur kerja (*pipeline*): *baseline* vs MLP vs LSTM/GRU, *walk-forward* 4 blok
  - Evaluasi MAE/RMSE vs toleransi tinggi pasang; prediksi 1–7 hari
  - Framing jujur: analisis harmonik untuk penjelasan, ML untuk prediksi cepat
- **Bab 9. Studi Kasus: Prediksi Curah Hujan dengan Data Terbuka**
  - Regresi jumlah hujan + klasifikasi kategori intensitas
  - Verifikasi operasional CSI/FAR/POD dengan *trade-off threshold*
  - *Walk-forward* vs *baseline* (*persistence*, klimatologi, ARIMA)
  - Interpretasi awal (permutation importance/SHAP) dan verifikasi per kategori

## Bagian IV — Operasional dan Arah Riset (Bab 10)

- **Bab 10. Dari Riset ke Praktik: Operasional, Interpretasi, dan Arah ke Depan**
  - Monitoring *drift* dan strategi retraining/kalibrasi
  - Ketidakpastian prediksi: *quantile*/*interval*, ensembel multi-*seed*
  - Interpretasi SHAP dan tautannya ke pengetahuan atmosfer
  - Keterbatasan dan etika; peta arah riset (CNN, *nowcasting*, *downscaling*, *generative*)

## Back Matter

- Lampiran A — Reproduksibilitas dan Lingkungan Komputasi
- Lampiran B — Konvensi Penulisan dan Penomoran Aset
- Daftar Pustaka
- Indeks
- Daftar Dataset dan Sumber
- Daftar Notebook dan DOI
- Tentang Penulis
- Kolofon

---

> **Catatan:** nomor halaman final (untuk edisi cetak/PDF) dihasilkan otomatis
> oleh mesin pengolah dokumen (Pandoc/LaTeX) saat *build*; daftar di atas
> merupakan sumber kebenaran struktur buku.