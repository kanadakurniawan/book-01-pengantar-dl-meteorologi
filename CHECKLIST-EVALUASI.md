# Checklist Evaluasi Internal — Buku *Pengantar Deep Learning untuk Meteorologi*

> Wajib lolos **seluruh bab** sebelum publikasi: DOI Zenodo, ISBN, GitHub publik, dan blog.
> Rujukan: `outline.md` → "Alur Kerja Penulisan & Evaluasi Internal".
> Skala: ✅ lolos · ⚠️ perlu perbaikan · ❌ gagal. Tulis catatan di kolom lembar kerja.

## A. Isi & Keilmuan

### A1. Bahasa — Ejaan & Kaidah (EYD)

- [ ] **Baku & EYD:** seluruh naskah mengikuti *Ejaan Bahasa Indonesia yang Disempurnakan*
      (EYD) dan kaidah PUEBI §18; kata tidak baku ditulis ke bentuk bakunya (mis. "resiko" →
      *risiko*, "nasehat" → *nasihat*, "ijin" → *izin*, "jaman" → *zaman*, "apotik" →
      *apotek*); tidak mengadopsi standar ejaan bahasa lain sebagai baku.
- [ ] **Imbuhan & kata depan:** imbuhan, partikel (-lah, -kah, -pun), dan kata depan
      (di-, ke-, dari) ditulis benar sesuai kaidah EYD.
- [ ] **Tanda baca:** titik, koma, titik dua, titik koma, tanda kutip, dan tanda kurung
      dipakai sesuai kaidah; tidak ada "…" di tengah kalimat atau tanda baca ganda yang keliru.
- [ ] **Huruf kapital & akronim:** huruf kapital sesuai EYD; akronim/singkatan seragam dan
      ditulis kepanjangannya pada pemunculan pertama (mis. *artificial intelligence* → AI).
- [ ] **Angka & satuan:** angka dan satuan konsisten dengan kebiasaan ilmiah Bahasa
      Indonesia (desimal dengan koma, ribuan dengan titik); satuan SI (m/s, °C, mm/hari)
      ditulis seragam.
- [ ] **Tulisan miring (bahasa asing):** kata/frasa bahasa asing yang **belum diserap**
      dicetak *miring* (PUEBI §18; detail di `outline.md` §7); nama merek, nama diri, dan
      akronim (TensorFlow, Colab, DOI, ERA5, dst.) **tidak** dimiringkan; pemunculan pertama
      memakai pola "padanan Indonesia (*istilah asing*)", lalu konsisten di seluruh buku.
- [ ] **Kebahasaan & idiom:** kolokasi wajar Bahasa Indonesia tanpa kalka harfiah
      (mis. "menurunkan hambatan" → "mengatasi hambatan"); frasa kunci konsisten di seluruh
      bab (mis. "yang dapat dijalankan", "mengatasi kedua hambatan").
- [ ] **Ketepatan & konsistensi istilah:** istilah Indonesia + Inggris benar dan seragam di
      seluruh buku; satu istilah satu padanan (glosarium satu sumber); tidak ada istilah
      ganda yang membingungkan pembaca.
- [ ] **Terminologi kanonik (otomatis):** jalankan `python scripts/cek-terminologie.py`;
      exit 0 = satu konsep satu istilah (kanonik: `galat`, `stasiun`, `prediksi`,
      `*baseline*`, `pelatihan`); laporkan hanya "bersih" bila exit 0; `error`/`kesalahan`/
      `station`/`prakiraan`/`patokan`/`forecast`/`training` di prosa = salah.
- [ ] **Elemen non-naratif ikut dicek:** judul/subjudul bab, *caption* gambar & tabel,
      sidebar, komentar kode berbahasa Indonesia, dan glosarium lolos cek yang sama
      (baku, miring, jelas).
- [ ] **Bersih dari kontaminasi:** naskah bebas dari kata korup atau token asing yang bukan
      Bahasa Indonesia maupun Inggris (sisa bahasa lain yang tidak berterima dalam register
      buku); setiap istilah asing yang dipakai adalah istilah domain yang sah dan dicetak
      *miring*. (Catatan: banlist `AGENTS.md` §2 ditujukan untuk chat, bukan untuk manuskrip.)
- [ ] **Tanpa dash sebagai pemisah klausa di prosa (otomatis):** `" - "` tidak dipakai
      sebagai pengganti koma, titik dua, atau titik di kalimat naratif, termasuk
      aposisi ganda ("X - keterangan - Y"); jalankan `python scripts/cek-dash-prosa.py`;
      exit 0 = bersih. Konteks yang dibolehkan (tidak ditandai): label bernomor
      ("Bab x -", "Kode x.y -", "Gambar x.y -", "Tabel x.y -"), frontmatter YAML, judul,
      item daftar (bullet/bernomor), tabel, blok kode/matematika, rentang/operasi angka, URL,
      dan daftar pustaka.

### A2. Kalimat & Ragam Akademik

- [ ] **Kejelasan kalimat:** tidak ada kalimat yang sulit dipahami; pembaca target
      (mahasiswa kebumian, praktisi) dapat membaca dan menjelaskan ulang setiap kalimat.
- [ ] **Struktur kalimat benar:** setiap kalimat utuh dan tidak rancu — subjek–predikat
      jelas; tidak ada kalimat terpotong, menggantung, atau bermakna ganda.
- [ ] **Panjang kalimat wajar:** tidak ada kalimat bergulir panjang dengan banyak anak
      kalimat; kalimat panjang dipecah menjadi dua atau lebih.
- [ ] **Benar secara bahasa akademik:** tidak ada kalimat yang salah menurut ragam tulis
      ilmiah; tidak bertele-tele, tidak mengklaim lebih dari yang didukung data, dan tidak
      berlebihan (*overhype*).
- [ ] **Kohesi & koherensi:** kalimat dalam paragraf bertautan logis; rujukan kata ganti
      ("ini", "tersebut", "-nya") jelas acuannya.
- [ ] **Paragraf padu:** satu gagasan utama per paragraf; urutan logis; tidak ada paragraf
      fragmen atau paragraf yang terlalu panjang.

### A3. Keilmuan & Kejujuran Ilmiah

- [ ] Semua klaim teknis disitasi; tidak ada pernyataan substantif tanpa sumber.
- [ ] Anti-overhype: semua hasil DL dibandingkan *baseline*; disclaimer "materi pengenalan" ada.
- [ ] Framing jujur di kasus: ML untuk prakiraan cepat/gap, bukan klaim riset baru.
- [ ] Angka/fakta bisa dilacak ke sumber (bukan hafalan/tebakan).

## B. Struktur & Konsistensi

- [ ] Template seragam tiap bab: Pembukaan masalah → Tujuan → Isi/konsep → Kode/notebook →
      Ringkasan kunci → Latihan → Referensi (keywords SEO cukup di metadata YAML bab).
- [ ] **Tujuan Pembelajaran** (3–5 butir aksi) ada di awal bab dan konsisten dengan latihan
      (constructive alignment).
- [ ] Sidebar "Prasyarat: Bab …" benar untuk tiap bab.
- [ ] Notasi & glosarium satu sumber (tidak ada istilah ganda).
- [ ] Kata isi sesuai target volume (3.000–4.500/bab); tidak ada bab terlalu kurus/gendut.
- [ ] Math diketik konsisten; code block sesuai style.

## C. Sitasi

- [ ] `[n]` di teks ≡ daftar References ≡ `refs.bib` (urut incremental pertama-muncul).
- [ ] Kesesuaian isi sitasi: setiap `[n]` benar-benar mendukung klaim pada kalimatnya (cek silang isi sumber ke klaim; bukan hanya konsistensi nomor).
- [ ] DOI valid (uji via `doi.org/<doi>`); ISBN/arXiv tercantum bila tidak ada DOI.
- [ ] URL punya tanggal akses.
- [ ] Tidak ada self-citation berlebihan.

## D. Kode & Reproduksibilitas

- [ ] Semua notebook dapat dijalankan dari awal–akhir (Colab) tanpa error.
- [ ] Seed tetap, versi TensorFlow tercatat.
- [ ] Data kasus tersedia / telah diunggah (dengan lisensi).

## E. Build & Output

- [ ] `node build/generate.mjs` menghasilkan PDF+DOCX tanpa error (butuh Pandoc+LaTeX
      pada mesin rilis).
- [ ] Total halaman realistis (±220 penarget); front/back matter siap.
- [ ] `bookDOI` terisi di semua `master.md` setelah DOI dibuat.

---

## Ringkasan Status per Bab

| Bab | A | B | C | D | E | Siap publikasi? |
|-----|---|---|---|---|---|-----------------|
| 1 | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | Belum (uji build & DOI) |
| 2 | ✅ | ✅ | ✅ | ✅ | ⚠️ | Belum (build & DOI) |
| 3 |   |   |   |   |   |                 |
| 4 |   |   |   |   |   |                 |
| 5 |   |   |   |   |   |                 |
| 6 |   |   |   |   |   |                 |
| 7 |   |   |   |   |   |                 |
| 8 |   |   |   |   |   |                 |
| 9 |   |   |   |   |   |                 |
| 10 |   |   |   |   |   |                 |

> Rule: seluruh bab harus "✅" di semua bagian sebelum lanjut ke Fase 3 (penerbitan).

### Catatan Evaluasi Bab 1 (20 Sep 2026)

- **A (isi & keilmuan):** ✅ Setelah perbaikan: konsistensi *miring* (*deep learning*,
  *outlier*, *k-fold*, *nowcasting*, *downscaling*, *diffusion*) disamakan; kalimat
  bergulir & *comma splice* di 1.0/1.9 dipecah; kurung bersarang di 1.0 dihilangkan;
  klaim "tiga baris terakhir Tabel 1.1" diperbaiki menjadi "tiga aplikasi berikutnya" +
  verifikasi & post-processing.
- **B (struktur & konsistensi):** ✅ Volume kata isi 4.493 (target 3.000–4.500).
  Heading 1.13 kini "Koneksi ke Bab Berikutnya" (kata kunci SEO pindah ke metadata YAML,
  sesuai keputusan penulis); istilah "prakiraan"/"klimatologis" diseragamkan.
- **C (sitasi):** ⚠️ Year Jolliffe disamakan ke 2011 (teks, refs.bib x3, daftar pustaka);
  URL arXiv [6] diberi tanggal akses. DOI belum diverifikasi ulang via `doi.org`
  satu-per-satu di mesin rilis.
- **D (kode & reproduksibilitas):** ⚠️ Kode 1.3 (mini-challenge *persistence* vs
  klimatologis) ditambahkan ke `notebooks/ch-01-00_fondasi_tensorflow.ipynb` (13 sel);
  perlu uji eksekusi dari awal–akhir di Colab.
- **E (build & output):** ⚠️ `node build/generate.mjs` belum dijalankan (butuh
  Pandoc+LaTeX di mesin rilis); `bookDOI` masih placeholder `10.5281/zenodo.0000000`.

### Catatan Evaluasi Bab 2 (21 Sep 2026 — setelah perbaikan)

- **A (isi & keilmuan):** ✅ Perbaikan terpasang: "Contrast dengan MSE" → "Berbeda dengan MSE";
  latihan 10: "run sekema uji" → "jalankan skema uji" (plus "sekema"→"skema",
  "menyaji"→"menyajikan", "diskutikan"→"diskusikan"); "mengoscila" → "berosilasi";
  "baik … baik … baik" → "baik … maupun … maupun"; "~36.500 baris" → "sekitar 36 ribu baris";
  "Di Bab 2 ini" → "dalam bab ini"; "(Bab 2.5)" → "(Bagian 2.5)"; tag YAML "reLU" → "ReLU";
  klaim kesamaan OLS diubah acuannya dari "Kode 2.2–2.3" ke kasus dasar Bagian 2.3 (Kode
  2.2–2.3 adalah MLP ber-ReLU, bukan neuron linear); `print(model.summary())` →
  `model.summary()`. Gaya pisah " - " dibiarkan (register konversasional buku; 12× Bab 1,
  41× Bab 2) — keputusan gaya; rapatkan pada penyuntingan akhir bila diinginkan.
- **B (struktur & konsistensi):** ✅ Volume isi ±3.800 kata (target 3.500–4.000);
  Tujuan Pembelajaran 4 butir selaras dengan latihan; prasyarat Bab 1 benar; penomoran
  persamaan/gambar/tabel/kode utuh. Belum ada penutup "Koneksi ke Bab Berikutnya"
  seperti 1.13 di Bab 1 (opsional).
- **C (sitasi):** ✅ DOI [2] diberi keterangan terbit-ulang: entri *NeurIPS* 2012 + "reissued
  in *Communications of the ACM* 60(6):84–90, 2017, doi: 10.1145/3065386" — disamakan di
  master.md Bab 2, `refs.bib` Bab 2, `back-matter/01-daftar-pustaka.md`, serta Bab 1
  (master.md + refs.bib) agar satu sumber konsisten. [3] daftar References Bab 2 kini
  memuat "(diakses: September 2026)", sama dengan `refs.bib`. Entri Krizhevsky
  diselaraskan hingga nomor volume (vol. 25) di semua berkas. `[n]` teks 1–3 ≡ daftar ≡ bib.
- **D (kode & reproduksibilitas):** ✅ Uji eksekusi ulang dari awal–akhir selesai
  (21 Sep 2026, mesin lokal): `jupyter nbconvert --execute` — 8/8 sel berhasil tanpa error,
  seed 42, TensorFlow 2.21.0 (CPU; GPU `[]` di Windows). Hasil akhir: baseline
  *persistence* MAE 0.3256 m; MLP MAE test 0.0782 m; `loss="mse"` → MAE 0.0782 / RMSE
  0.0948; `loss="mae"` → MAE 0.0745 / RMSE 0.0921. Sel perbandingan MAE vs MSE (sebelumnya
  belum tereksekusi) kini ikut tereksekusi. Warning Keras `input_shape=` di `Dense` muncul
  (tidak berbahaya; opsional diganti `Input(shape=...)`). Validasi silang di Colab
  disarankan sebelum rilis karena log/GPU Colab dapat sedikit berbeda. Cadangan notebook
  sebelum uji: `C:\Users\Hi\AppData\Local\Temp\kilo\ch-02-01_backup.ipynb`.
- **E (build & output):** ⚠️ Belum diuji `node build/generate.mjs`; `bookDOI` placeholder.