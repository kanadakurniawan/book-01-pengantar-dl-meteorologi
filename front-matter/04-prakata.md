---
title: "Prakata"
book: "Pengantar Deep Learning untuk Meteorologi"
---

# Prakata (Edisi 2.0)

Buku ini lahir dari sebuah pertanyaan sederhana yang sering saya dengar dari
teman-teman di BMKG dan dari mahasiswa kebumian: *"Saya ingin belajar deep
learning, tapi dari mana mulainya?"*

Jawaban yang jujur adalah: bahan belajarnya banyak, tetapi hampir semuanya
ditulis dalam bahasa Inggris dan dengan contoh dari belahan dunia lain. Mahasiswa
kebumian di Indonesia yang ingin belajar *deep learning* biasanya harus
menerjemahkan dua hal sekaligus: bahasa dan konteks. Buku ini ditulis dalam
bahasa Indonesia dan dengan contoh yang dekat dengan dunia meteorologi Indonesia,
sehingga mengatasi kedua hambatan itu sekaligus.

Saya menulis buku ini dengan keyakinan bahwa **deep learning bukan monopoli
ilmuwan komputer**: belajar deep learning bukan hanya memahami arsitektur *neural
network*, tetapi juga memakai metode itu untuk menghadapi persoalan nyata. Alat
terbaik untuk praktisi meteorologi adalah yang dijelaskan dengan data meteorologi.
Karena itu, di setiap bab Anda
akan menemukan:

1. **Konsep** — dijelaskan dari nol, dengan analogi dunia nyata.
2. **Kode** — notebook yang dapat dijalankan langsung di Google Colab.
3. **Data Indonesia** — pasang surut, curah hujan, data terbuka (ERA5/CHIRPS).
4. **Evaluasi yang jujur** — model selalu dibandingkan dengan *baseline*;
   tidak ada klaim berlebihan.

## Mengapa buku ini ada

Tiga alasan utama:

1. **Celah konten**: materi *deep learning* berbahasa Indonesia dengan konteks
   meteorologi masih jarang.
2. **Kebutuhan praktisi**: banyak tugas harian (prediksi tinggi pasang, prediksi
   hujan, verifikasi peringatan dini) bisa dibantu model *neural network*, tetapi
   praktisi butuh panduan yang relevan dengan pekerjaannya.
3. **Prinsip keterbukaan**: buku ini gratis, *living* (bisa diperbarui), dan
   setiap hasil dilaporkan apa adanya.

## Struktur buku

Buku ini terdiri atas empat bagian:

- **Bagian I — Fondasi (Bab 1–5):** posisi *deep learning*, regresi, klasifikasi,
  optimasi/backpropagation, serta evaluasi dan regularisasi untuk data iklim.
- **Bagian II — Data dan Model Sekuensial (Bab 6–7):** pengelolaan data
  meteorologi dan model untuk deret waktu (RNN, LSTM, GRU).
- **Bagian III — Studi Kasus (Bab 8–9):** dua proyek *end-to-end* — prediksi
  pasang surut (Cilacap) dan curah hujan harian dengan data terbuka.
- **Bagian IV — Operasional dan Arah Riset (Bab 10):** dari riset ke praktik,
  interpretasi model, keterbatasan, etika, dan peta riset lanjutan.

Setiap bab berdiri sendiri dan dilengkapi *sidebar* "Prasyarat", satu notebook
Colab, latihan, serta daftar referensi dalam format IEEE. Bagian "Cara Memakai
Buku" memetakan urutan baca yang disarankan.

## Siapa yang sebaiknya membaca

- **Mahasiswa S1 kebumian** (meteorologi, oseanografi, geofisika) yang ingin
  mulai belajar *deep learning* dari nol.
- **Praktisi meteorologi dan lembaga riset** yang ingin menilai kapan *deep learning*
  layak dipakai dan bagaimana membangun model sederhana.
- **Siapa pun** dengan latar belakang non-informatika yang ingin memahami cara
  kerja jaringan saraf melalui contoh data nyata.

## Keterbatasan yang jujur

Buku ini adalah **pengantar**, bukan pengganti buku teks seperti *Deep
Learning* (Goodfellow et al., 2016) atau kursus yang lebih dalam. Buku ini bukan
hasil riset baru, melainkan jembatan menuju literatur primer. Angka dan hasil
yang ditampilkan harus dipahami sebagai ilustrasi alur, bukan sebagai klaim
performa untuk semua kondisi. Bab 10 membahas keterbatasan ini lebih lanjut.

## Ucapan terima kasih

Buku ini tidak akan ada tanpa:

- Teman-teman di BMKG yang selalu bertanya "bagaimana caranya?" dan memotivasi
  penjelasan yang sederhana.
- Mahasiswa kebumian yang bersedia menjadi pembaca awal dan memberi masukan.
- Komunitas open-source TensorFlow, Pandas, NumPy, dan xarray yang membuat alat
  ini tersedia gratis.
- Penyedia data terbuka yang dipakai studi kasus — CHC UCSB (CHIRPS), NOAA,
  Copernicus/ERA5, UNESCO/IOC, UHSLC, dan PSMSL.
- Para penelaah anonim yang memberi umpan balik pada versi draf buku ini.

## Cara menggunakan buku ini

Baca Bab 1–5 berurutan untuk fondasi, lalu Bab 6–10 sesuai kebutuhan. Selalu
jalankan notebook saat membaca — jangan hanya membaca. Panduan lengkap ada di
bagian "Cara Memakai Buku".

Selamat belajar. Semoga buku ini bermanfaat untuk pekerjaan dan riset Anda.

**Kanada Kurniawan**

Pontianak, September 2026