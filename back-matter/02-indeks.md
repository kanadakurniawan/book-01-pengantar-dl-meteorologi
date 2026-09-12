---
title: "Indeks"
book: "Pengantar Deep Learning untuk Meteorologi"
---

# Indeks

> Indeks ini disusun **tematis per bagian**, bukan per halaman — karena nomor
> halaman buku dapat berubah antar-edisi. Saat PDF di-render, indeks bernomor
> halaman dapat dihasilkan otomatis oleh LaTeX (mis. `\makeindex`) dari
> kata-kunci berikut.

## A

- Adam (optimizer) — Bab 2, 4
- Analisis harmonik — Bab 8
- ARIMA — Bab 5, 7, 9
- *Artificial intelligence* (AI, kecerdasan buatan) — Bab 1

## B

- *Backpropagation* — Bab 4
- *Baseline* (tolok ukur): *persistence*, klimatologi, ARIMA — Bab 5, 7, 8, 9
- Bias-variance — Bab 5
- Banjir rob — Bab 8
- *Batch size* — Bab 4

## C

- CNN (*convolutional neural network*) — Bab 10 (arah riset)
- Callback: *early stopping*, ModelCheckpoint, ReduceLROnPlateau — Bab 4, 5
- *Class imbalance* — Bab 3, 5, 9
- Colab (Google Colab) — Bab 1, 5
- *Confusion matrix* — Bab 3, 5
- Cross-entropy (binary/categorical) — Bab 3
- CSI/FAR/POD (*Critical Success Index*, *False Alarm Ratio*, *Probability of
  Detection*) — Bab 3, 5, 9

## D

- Data terbuka: GHCN-Daily, CHIRPS, ERA5, pasang surut — Bab 6, 8, 9
- *Deep learning*: definisi, sejarah, kapan layak — Bab 1
- *Downscaling* — Bab 10
- *Drift* (monitoring) — Bab 10
- Dropout — Bab 5
- Dropout sebagai aproksimasi Bayesian — Bab 10

## E

- *Early stopping* — Bab 4, 5
- ENSO/MJO sebagai fitur — Bab 6, 9
- *Epoch* — Bab 4, 5
- ERA5 — Bab 6, 9
- Etika dan keterbatasan *deep learning* — Bab 10
- Evaluasi model: MAE/RMSE/R²/Willmott/KGE; CSI/FAR/POD — Bab 5

## F

- Fitur (lag, musiman, ENSO/MJO) — Bab 6
- Formzahl (tipe pasang) — Bab 8
- Fungsi aktivasi: ReLU, sigmoid, tanh — Bab 2, 4

## G

- Gap data & imputasi — Bab 6, 8, 10
- *Gradient descent* — Bab 4
- GRU — Bab 7
- Glosarium istilah — lihat "Glosarium dan Notasi"

## H

- Harmonik vs *machine learning* — Bab 8
- Horizon prediksi (multi-step) — Bab 7, 8

## I

- Imputasi data hilang — Bab 6, 8, 10
- *Interpretability*: SHAP, permutation importance — Bab 9, 10

## K

- Keras — Bab 1, 2
- KGE (Kling–Gupta Efficiency) — Bab 5
- Klasifikasi: biner, multi-kelas — Bab 3, 9

## L

- LSTM — Bab 7, 8, 9
- *Learning rate*, scheduler — Bab 4
- *Leakage* — Bab 5, 8
- Lisensi data — Bab 6, 8; lihat juga "Daftar Dataset dan Sumber"
- *Loss function* (MSE, MAE, cross-entropy) — Bab 2–4

## M

- MAE vs MSE — Bab 2
- *Machine learning* (ML): definisi, vs DL — Bab 1
- MLP (*multilayer perceptron*) — Bab 2, 8
- Metrik operasional WMO — Bab 5, 9
- MJO (RMM) — Bab 6
- Multi-step forecasting (recursive/direct/seq2seq) — Bab 7

## N

- Neural network — Bab 1, 2
- Normalisasi (z-score, fit pada *train*) — Bab 6
- Notebook Colab — Bab 1; lihat "Daftar Notebook dan DOI"
- *Nowcasting* — Bab 10

## O

- Overfitting / underfitting — Bab 5
- Optimasi: SGD, Adam — Bab 4
- Operasionalisasi model — Bab 10
- *Outlier* / pencilan — Bab 6

## P

- Pasang surut: tipe, analisis harmonik, prediksi — Bab 8
- Perceptron — Bab 2
- *Persistence* (*baseline*) — Bab 7, 8
- Precision/recall/F1 — Bab 3
- Peta aplikasi DL dalam meteorologi — Bab 1

## Q

- Quantile / selang ketidakpastian — Bab 10

## R

- ReLU — Bab 2, 4
- Regresi — Bab 2, 8, 9
- Regularisasi (L2, dropout) — Bab 5
- RNN — Bab 7
- Reproduksibilitas: *seed*, versi TF — Bab 5, 6; Lampiran A

## S

- SGDM/Adam — Bab 4
- SHAP — Bab 9, 10
- Sigmoid / softmax — Bab 3
- *Skill score* (SS) — Bab 7, 8
- Split data berbasis waktu, *walk-forward* — Bab 5, 8
- Stabilitas model & *drift* — Bab 10

## T

- TensorFlow — Bab 1, 2
- *Threshold* (trade-off) — Bab 3, 9
- Time series (deret waktu): *window*, *baseline*, LSTM — Bab 7
- Transformasi target (log1p) — Bab 6

## V

- Vanishing gradient — Bab 4
- Verifikasi operasional (CSI/FAR/POD, tabel kategori) — Bab 5, 9

## W

- Walk-forward validation — Bab 5, 8, 9
- WMO: pedoman verifikasi — Bab 5, 9
- *Window* (jendela input) — Bab 7, 8
- Willmott (indeks kesesuaian) — Bab 5

---

> **Catatan:** untuk indeks bernomor halaman final, jalankan build LaTeX dengan
> `\makeindex` saat `node build/generate.mjs`; kata-kunci di atas adalah seed
> untuk dikurasi lebih lanjut.