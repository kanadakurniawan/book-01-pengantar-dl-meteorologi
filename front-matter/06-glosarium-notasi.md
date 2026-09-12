---
title: "Glosarium dan Notasi"
book: "Pengantar Deep Learning untuk Meteorologi"
---

# Glosarium dan Notasi

> Glosarium ini memuat istilah-istilah yang dipakai di seluruh buku. Pada
> pemunculan pertama di tiap bab, istilah ditulis dengan pola
> "padanan Indonesia (*istilah Inggris*)." Setelahnya, buku konsisten memakai
> salah satu bentuk saja. Konvensi penulisan mengikuti aturan di
> `outline.md` (PUEBI §18: istilah asing yang belum diserap dicetak miring).

## Glosarium Istilah

| Istilah | Definisi (ringkas) | Bab terkait |
|---|---|---|
| *Artificial intelligence* (AI) | Kecerdasan buatan: bidang studi membuat mesin meniru kemampuan kognitif manusia | 1 |
| *Machine learning* (ML) | Pembelajaran mesin: cabang AI yang belajar pola dari data tanpa diprogram eksplisit per aturan | 1 |
| *Deep learning* (DL) | Pembelajaran mendalam: cabang ML yang memakai jaringan saraf berlapis | 1 |
| *Neural network* | Jaringan saraf: model matematis berlapis yang terinspirasi neuron biologis | 1–10 |
| Neuron / perceptron | Unit komputasi dasar jaringan: `z = Σ wᵢxᵢ + b`, lalu aktivasi | 2 |
| Fungsi aktivasi (*activation function*) | Fungsi non-linear yang memberi kapasitas model (mis. ReLU, sigmoid, tanh) | 2, 4 |
| Bobot (*weight*), bias | Parameter model yang dipelajari saat pelatihan | 2, 4 |
| Tolok ukur (*baseline*) | Model sederhana sebagai pembanding minimal (persistence, mean, ARIMA) | 5, 7, 8, 9 |
| *Persistence* | *Baseline* yang memprediksi nilai sekarang untuk waktu depan (`ŷ(t+h) = y(t)`) | 7, 8 |
| Regresi | Memprediksi nilai kontinu | 2, 5, 7–9 |
| Klasifikasi | Memprediksi label/kategori | 3, 5, 9 |
| *Loss function* | Fungsi kerugian yang diminimalkan saat pelatihan (MSE, MAE, cross-entropy) | 2–4 |
| *Gradient descent* | Algoritma optimasi dengan turunan dari *loss* | 4 |
| *Backpropagation* | Cara menghitung gradien dengan aturan rantai | 4 |
| *Learning rate* | Langkah ukuran pembaruan bobot | 4 |
| *Epoch*, *batch size* | Satu putaran penuh dataset; jumlah sampel per pembaruan | 4, 5 |
| *Overfitting* / *underfitting* | Model terlalu menghafal data / terlalu sederhana | 5 |
| *Regularisasi* (L2, *dropout*) | Teknik mencegah *overfitting* | 5 |
| *Early stopping* | Menghentikan pelatihan saat validasi berhenti membaik | 5 |
| *Walk-forward* / *blocked* | Validasi silang deret waktu dengan urutan waktu dijaga | 5, 8, 9 |
| *Leakage* | Kebocoran informasi masa depan ke data latih | 5, 8 |
| *Reanalysis* | Data cuaca historis gabungan model + observasi (mis. ERA5) | 6, 9 |
| Nilai hilang / *gap* | Data yang tidak terekam; ditangani dengan imputasi/pemotongan | 6, 8 |
| *Outlier* / pencilan | Nilai ekstrem yang menyimpang dari pola; potensi kesalahan pengukuran | 6 |
| Imputasi | Mengisi nilai hilang dengan estimasi | 6, 8, 10 |
| Normalisasi | Menskala fitur (mis. z-score) agar pelatihan stabil | 6 |
| Fitur lag / *window* | Konstruksi masukan deret waktu dari masa lalu | 7, 8 |
| RNN / LSTM / GRU | Jaringan sekuensial; LSTM/GRU punya *gate* ingatan | 7 |
| Multi-step forecast | Prediksi beberapa langkah ke depan (recursive/direct/seq2seq) | 7 |
| Analisis harmonik | Pemodelan pasang surut dengan konstituen astronomis (M2, S2, K1, O1) | 8 |
| Formzahl (F) | Rasio komponen untuk menentukan tipe pasang | 8 |
| *Tide gauge* / pasang surut | Alat/deret tinggi muka air | 8 |
| MAE / RMSE | Metrik error regresi: *mean absolute error*; *root mean square error* | 2, 5, 8, 9 |
| R², Willmott, KGE | Metrik kesesuaian regresi | 5 |
| CSI / FAR / POD / TS | Metrik verifikasi kejadian ekstrem (kategori) | 3, 5, 9 |
| *Confusion matrix* | Tabel tabulasi prediksi vs aktual untuk klasifikasi | 3, 5 |
| *Class imbalance* | Ketidakseimbangan jumlah sampel antar-kelas | 3, 5, 9 |
| *Threshold* | Ambang keputusan (mis. hujan jika probabilitas > 0,5) | 3, 9 |
| *Drift* | Perubahan distribusi data seiring waktu (atmosfer non-stasioner) | 10 |
| *Quantile* / *interval* prediksi | Rentang ketidakpastian prediksi | 10 |
| SHAP | Metode interpretasi model (kontribusi fitur) | 10 |
| *Downscaling* | Dari skala reanalysis/global ke skala lokal | 10 |
| *Nowcasting* | Prakiraan sangat jangka pendek (kini–6 jam) | 10 |
| *Generative* | Model yang menghasilkan data baru (imputasi, skenario) | 10 |
| *Seed* | Nilai acak tetap untuk reproduksibilitas | 5, 6, 8 |

## Notasi Matematis

Konvensi notasi di seluruh buku:

| Simbol | Makna |
|---|---|
| `xᵢ` | Fitur / input ke-i |
| `wᵢ` | Bobot (*weight*) ke-i |
| `b` | Bias |
| `z` | Masukan sebelum aktivasi: `z = Σwᵢxᵢ + b` |
| `a` / `ŷ` | Output (aktivasi / prediksi) |
| `f(·)`, `σ(·)` | Fungsi aktivasi; khususnya sigmoid: `σ(z) = 1/(1+e⁻ᶻ)` |
| `ReLU(x)` | `max(0, x)` |
| `y(t)` | Nilai aktual deret waktu pada waktu t |
| `ŷ(t+h)` | Prediksi pada *horizon* h ke depan |
| `w` (*window*), `h` (*horizon*) | Panjang jendela input; jarak prediksi |
| `X`, `y` | Matriks fitur; vektor target |
| `θ`, `η` | Parameter model; *learning rate* |
| `L`, `J` | *Loss function* (fungsi kerugian) |
| MAE | `(1/n) Σ \|yᵢ − ŷᵢ\|` |
| RMSE | `√((1/n) Σ (yᵢ − ŷᵢ)²)` |
| POD / FAR / CSI | Peluang deteksi; *false alarm ratio*; *critical success index* |
| SS | *Skill score* relatif terhadap *baseline*: `1 − MAE_model/MAE_baseline` |
| F (Formzahl) | `(K1 + O1) / (M2 + S2)` untuk tipe pasang |

## Singkatan yang Sering Dipakai

| Singkatan | Kepanjangan |
|---|---|
| AI | *Artificial Intelligence* (kecerdasan buatan) |
| ML | *Machine Learning* (pembelajaran mesin) |
| DL | *Deep Learning* (pembelajaran mendalam) |
| RNN / LSTM / GRU | *Recurrent Neural Network* / *Long Short-Term Memory* / *Gated Recurrent Unit* |
| MLP | *Multilayer Perceptron* |
| CNN | *Convolutional Neural Network* |
| MAE / MSE / RMSE | *Mean Absolute Error* / *Mean Squared Error* / *Root Mean Square Error* |
| R² | Koefisien determinasi |
| KGE | *Kling–Gupta Efficiency* |
| POD / FAR / CSI / TS | *Probability of Detection* / *False Alarm Ratio* / *Critical Success Index* / *Threat Score* |
| SS | *Skill Score* |
| GHCND | *Global Historical Climatology Network - Daily* (NOAA) |
| CHIRPS | *Climate Hazards Group InfraRed Precipitation with Station data* |
| BIG | Badan Informasi Geospasial |
| WMO | *World Meteorological Organization* |
| ERA5 | Reanalysis global generasi kelima ECMWF |
| CHIRPS | *Climate Hazards Group InfraRed Precipitation with Station data* |
| ENSO / MEI | *El Niño–Southern Oscillation* / *Multivariate ENSO Index* |
| MJO / RMM | *Madden–Julian Oscillation* / *Real-time Multivariate MJO index* |
| PSMSL / IOC / UHSLC | *Permanent Service for Mean Sea Level* / *Intergovernmental Oceanographic Commission* / *University of Hawaii Sea Level Center* |
| SHAP | *SHapley Additive exPlanations* |

> Persamaan bernomor mengikuti format `Persamaan (bab.nomor)`, mis.
> `Persamaan (2.1)`. Aset lain: `Gambar bab.nomor`, `Tabel bab.nomor`,
> `Kode bab.nomor`.