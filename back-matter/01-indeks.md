---
title: "Indeks"
book: "Pengantar Deep Learning untuk Meteorologi"
---

# Indeks

> Indeks ini disusun **tematis per bagian**, bukan per halaman — karena halaman
> bagian buku dapat berubah antar-edisi. Saat PDF di-render, indeks bernomor
> halaman dapat dihasilkan otomatis oleh LaTeX (mis. `\makeindex`) dari
> kata-kunci berikut.

## A

- Adam (optimizer) — Bab 2, 4
- Analisis harmonik — Bab 8
- *Artificial intelligence* (AI, kecerdasan buatan) — Bab 1

## B

- *Backpropagation* — Bab 4
- *Baseline* (tolok ukur): persistence, klimatologi, ARIMA — Bab 5, 7, 8, 9
- Bias-variance — Bab 5
- BMKG, data dan layanan — Bab 1, 6, 9
- Banjir rob — Bab 8

## C

- CNN (*convolutional neural network*) — Bab 10 (arah riset)
- Confusion matrix — Bab 3, 5
- Cross-entropy (binary/categorical) — Bab 3
- CSI/FAR/POD (*Critical Success Index*, *False Alarm Ratio*, *Probability of
  Detection*) — Bab 3, 5, 9
- Colab (Google Colab) — Bab 1

## D

- Data BMKG, ERA5, CHIRPS, pasang surut — Bab 6, 8, 9
- Deep learning: definisi, sejarah, kapan layak — Bab 1
- *Downscaling* — Bab 10
- Dropout — Bab 5
- *Drift* (monitoring) — Bab 10

## E

- *Epoch*, *batch size* — Bab 4
- ERA5 — Bab 6, 9
- *Early stopping* — Bab 5
- ENSO/MJO sebagai fitur — Bab 6, 9
- Evaluasi model: MAE/RMSE/R²/Willmott/KGE; CSI/FAR/POD — Bab 5

## F

- Formzahl — Bab 8
- Fungsi aktivasi: ReLU, sigmoid, tanh — Bab 2, 4
- Fitur (lag, musiman, ENSO/MJO) — Bab 6

## G

- *Gradient descent* — Bab 4
- Gap data & imputasi — Bab 6, 8, 10
- GRU — Bab 7
- Glosarium istilah — lihat "Glosarium dan Notasi"

## H

- Harmonik vs machine learning — Bab 8
- Horizon prediksi (multi-step) — Bab 7, 8

## I

- Imputasi data hilang — Bab 6, 8, 10
- *Interpretability*: SHAP, permutation importance — Bab 9, 10

## K

- Klasifikasi: biner, multi-kelas — Bab 3, 9
- *Class imbalance* — Bab 3, 5
- KGE (Kling–Gupta Efficiency) — Bab 5

## L

- LSTM — Bab 7, 8, 9
- *Learning rate*, scheduler — Bab 4
- *Leakage* — Bab 5
- Lisensi data — Bab 6, 8, lihat juga "Daftar Dataset & Sumber"

## M

- MAE vs MSE — Bab 2
- *Machine learning* (ML): definisi, vs DL — Bab 1
- MLP (*multilayer perceptron*) — Bab 2, 8
- Multi-step forecasting (recursive/direct/seq2seq) — Bab 7
- Metrik operasional WMO — Bab 5, 9

## N

- Neural network — Bab 1, 2
- Normalisasi (z-score, fit pada train) — Bab 6
- Notebook Colab — Bab 1; lihat "Daftar Notebook & DOI"
- *Nowcasting* — Bab 10

## O

- Overfitting / underfitting — Bab 5
- Optimasi: SGD, Adam — Bab 4
- Operasionalisasi model — Bab 10

## P

- Pasang surut: tipe, analisis harmonik, prediksi — Bab 8
- Perceptron — Bab 2
- Persistence (baseline) — Bab 7, 8
- Precision/recall/F1 — Bab 3
- Peta aplikasi DL dalam meteorologi — Bab 1

## Q

- Quantile / selang ketidakpastian — Bab 10

## R

- ReLU — Bab 2, 4
- Regresi — Bab 2, 8, 9
- Regularisasi (L2, dropout) — Bab 5
- RNN — Bab 7
- Reproduksibilitas: seed, versi TF — Bab 5, 6

## S

- Sigmoid / softmax — Bab 3
- Split data berbasis waktu, *walk-forward* — Bab 5, 8
- Skill score (SS) — Bab 7, 8
- SHAP — Bab 9, 10
- Stabilitas model & *drift* — Bab 10

## T

- TensorFlow/Keras — Bab 1, 2
- Threshold (trade-off) — Bab 3, 9
- Time series (deret waktu): window, baseline, LSTM — Bab 7
- Transformasi target (log1p) — Bab 6

## V

- Verifikasi operasional (CSI/FAR/POD, tabel kategori) — Bab 5, 9
- Vanishing gradient — Bab 4

## W

- Walk-forward validation — Bab 5, 8, 9
- WMO: pedoman verifikasi — Bab 5, 9
- Window (jendela input) — Bab 7, 8

---

> **Catatan:** untuk indeks bernomor halaman final, jalankan build LaTeX dengan
> `\makeindex` pada saat `node build/generate.mjs`; kata-kunci di atas adalah
> seed untuk dikurasi lebih lanjut.