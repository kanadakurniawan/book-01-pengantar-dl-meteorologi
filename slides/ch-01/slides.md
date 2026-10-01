---
title: "Bab 1: Pengantar Deep Learning untuk Meteorologi"
subtitle: "Pengantar Deep Learning untuk Meteorologi"
author: "Kanada Kurniawan"
---

# Bagian I: Fondasi

## Bab 1: Pengantar Deep Learning untuk Meteorologi

- *Deep learning* untuk meteorologi, dari praktisi untuk praktisi di Indonesia.
- Materi pengenalan, bukan klaim riset baru.

::: notes
Sapa pembaca, sebutkan bahwa bab ini adalah titik awal dan tidak butuh prasyarat.
:::

## Prasyarat

- Tidak ada prasyarat. Ini titik awal buku.
- Perkakas: Google Colab dan TensorFlow/Keras.

## Tujuan Pembelajaran

- Membedakan AI, *machine learning*, dan *deep learning*.
- Memetakan aplikasi DL meteorologi ke bab yang relevan.
- Menilai kapan DL layak dibanding *baseline* statistik.
- Menyiapkan Colab dan membuat tensor pertama.

## Peta Isi

1. AI, ML, dan DL.
2. Mengapa DL relevan sekarang.
3. Peta aplikasi dan batas buku.
4. Kapan DL layak dipakai.
5. Alur kerja proyek dan lingkungan.
6. Tensor pertama dan *baseline*.

## AI, ML, dan DL

- AI: bidang luas untuk meniru kemampuan kognitif manusia [2].
- ML: komputer belajar pola dari data tanpa aturan eksplisit [3].
- DL: ML dengan jaringan saraf berlapis [4].

![Keterkaitan AI, ML, dan DL](figures/fig-1-1-hierarki-ai-by-chatgpt.png "Gambar 1.1. Keterkaitan AI, ML, dan DL (Sumber: naskah Bab 1)")

## Mengapa DL Relevan Sekarang

- Data besar: ERA5 dan arsip klimatologi menyediakan volume besar [7].
- Komputasi murah: GPU dan Google Colab gratis.
- *Tooling* matang: TensorFlow/Keras dan PyTorch mudah dipelajari [6].

## Sejarah Singkat

- 1958: *perceptron* satu lapis oleh Rosenblatt [5].
- 1986: *backpropagation* dipopulerkan untuk jaringan bertingkat [8].
- 2012: AlexNet memenangkan ImageNet dengan CNN [9].
- 2019: ulasan Reichstein menegaskan peran DL di sistem kebumian [7].

## Peta Aplikasi DL Meteorologi

Fokus buku: dua aplikasi inti, sisanya arah riset.

| Aplikasi | Dibahas di buku ini |
|---|---|
| Prediksi deret waktu | Bab 2, 7-9 |
| Klasifikasi kejadian | Bab 3, 5, 9 |
| Imputasi data hilang | Bab 6, 8, 10 |
| *Nowcasting*, *downscaling*, generatif | Bab 10 (arah riset) |

## Apa yang Tidak Dibahas

- Bahasa pemrograman selain Python.
- CNN, Transformer, dan model generatif hanya di Bab 10.
- Model skala *big data*; fokus Colab gratis.
- ML klasik dibahas singkat sebagai *baseline*.

## Kapan DL Layak

- Mulai dari *baseline*: regresi linear, ARIMA, dan *persistence*.
- DL layak hanya bila mengalahkan *baseline* dengan data cukup.
- Ingat pembanding non-linear: Random Forest dan XGBoost.
- Utamakan model yang dapat dijelaskan di konteks operasional.
- Pertimbangkan biaya, pemantauan, dan pelatihan ulang.

## Karakteristik Data Meteorologi Indonesia

- Variabilitas tinggi dengan rezim ganda: monsun, MJO [10], dan ENSO.
- Ekor kanan hujan berat: banyak hari nol, sedikit hari ekstrem [11].
- Data hilang, *outlier*, dan inhomogenitas jaringan pengamatan.
- Pasang surut kuat tetapi nonstasioner karena cuaca dan debit sungai.
- Data kejadian ekstrem yang tersedia sangat terbatas.

## Alur Kerja Proyek ML

1. Definisikan masalah: regresi atau klasifikasi, dan target keberhasilan.
2. Kumpulkan data beserta lisensi dan resolusinya (Bab 6).
3. Siapkan data: bersihkan, buat fitur, bagi train/val/test.
4. Bangun model mulai dari *baseline* sederhana.
5. Evaluasi dengan metrik yang sesuai tujuan.
6. Putuskan, lalu pantau dan latih ulang secara berkala.

## Menyiapkan Lingkungan

- Google Colab gratis, tanpa instalasi, dan menyediakan GPU [6].
- Ideal untuk mahasiswa dan praktisi tanpa server sendiri.
- Catat versi TensorFlow dan gunakan *seed* tetap.

```python
import tensorflow as tf
print(tf.__version__)
print("GPU tersedia:", tf.config.list_physical_devices("GPU"))
```

## Tensor Pertama

- Tensor adalah kotak angka dengan beberapa sumbu.
- Skalar 0D, vektor 1D, matriks 2D, tensor 3D.
- Bentuk (*shape*) menentukan bentuk masukan model di Bab 2 dan Bab 7.

```python
import tensorflow as tf
suhu_hari = tf.constant([26.5, 26.8, 27.2])
print(suhu_hari.shape)   # (3,)
```

## Hasil: Persistence dan Klimatologis

- *Persistence*: prediksi besok sama dengan pengamatan hari ini.
- Klimatologis: rata-rata historis untuk hari dan bulan yang sama [12].
- Pada data periodik sintetis, klimatologis mengalahkan *persistence*.
- DL layak hanya bila mengalahkan keduanya secara konsisten.

## Ringkasan

- DL adalah cabang ML berbasis jaringan saraf berlapis.
- Fokus buku: deret waktu dan klasifikasi untuk data Indonesia.
- DL layak jika mengalahkan *baseline* sederhana.
- Lingkungan kerja: Google Colab dan TensorFlow/Keras.
- Matematika yang dibutuhkan terbatas pada dasar aljabar, kalkulus, dan statistika.

## Latihan

1. Prediksi suhu minimum besok: regresi.
2. Hujan deras di atas 50 mm: klasifikasi biner.
3. Level siaga rob: klasifikasi multi-kelas.
4. Jumlah hari hujan sebulan: regresi, mulai dari klimatologis.

## Referensi

- [1] Goodfellow, Bengio, Courville. *Deep Learning*. MIT Press, 2016.
- [4] LeCun, Bengio, Hinton. "Deep learning." *Nature*, 2015. doi: 10.1038/nature14539.
- [5] Rosenblatt. "The perceptron." *Psychological Review*, 1958.
- [6] Abadi et al. "TensorFlow." arXiv:1603.04467, 2016.
- [7] Reichstein et al. "DL for Earth system science." *Nature*, 2019.
- [12] Jolliffe, Stephenson. *Forecast Verification*. Wiley, 2011.

## Penutup

- Unduh buku gratis beserta notebook di kanadakurniawan.com.
- Notebook bab ini: `ch-01-00_fondasi_tensorflow.ipynb`.
