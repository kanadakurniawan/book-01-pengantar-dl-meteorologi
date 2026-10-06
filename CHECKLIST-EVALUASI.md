# Checklist Evaluasi Internal — Buku *Pengantar Deep Learning untuk Meteorologi*

> Wajib lolos **seluruh bab** sebelum publikasi: DOI Zenodo, ISBN, GitHub publik, dan blog.
> Rujukan: `outline.md` → "Alur Kerja Penulisan & Evaluasi Internal".
> Skala: ✅ lolos · ⚠️ perlu perbaikan · ❌ gagal. Tulis catatan di kolom lembar kerja.

> **Pemicu "cek kualitas" (wajib):** bila diminta "cek kualitas" (atau variasi senada),
> kerjakan **dua hal sekaligus** dan laporkan keduanya dalam satu laporan:
>
> 1. Jalankan cek otomatis terpadu — `python scripts/cek-kualitas.py` untuk seluruh buku,
>    atau `python scripts/cek-kualitas.py --file <path>` untuk satu berkas. Perintah ini
>    menjalankan `cek-bahasa-asing.py`, `cek-terminologie.py`, dan `cek-dash-prosa.py`
>    sekaligus; laporkan "bersih" hanya bila exit 0 (ketiganya lolos).
> 2. Telusuri checklist A–E di bawah (isi & keilmuan, struktur, sitasi, kode, build).
>
> Cek otomatis saja tidak cukup, dan checklist saja tidak cukup: "cek kualitas" berarti
> keduanya.

## A. Isi & Keilmuan

### A1. Bahasa — Ejaan & Kaidah (EYD)

- [ ] **Cek kualitas terpadu (otomatis, entry point):** jalankan
      `python scripts/cek-kualitas.py` (seluruh buku) atau
      `python scripts/cek-kualitas.py --file <path>` (satu berkas); perintah ini
      membungkus `cek-bahasa-asing.py`, `cek-terminologie.py`, dan `cek-dash-prosa.py`
      dalam satu jalur. Laporkan "bersih" hanya bila exit 0 (ketiganya lolos); ini bagian
      tetap dari pemicu "cek kualitas" (lihat catatan di awal berkas).
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
- [ ] **Ringkas bernas:** setiap kalimat padat isi, tanpa kata atau frasa yang tidak
      menambah makna — pembuka basa-basi ("perlu diketahui bahwa", "pada dasarnya",
      "sebenarnya"), penegasan berlebihan ("sangat", "benar-benar"), pengulangan gagasan,
      dan sinonim bertumpuk. Rapatkan kalimat tanpa mengorbankan ketepatan teknis dan
      kejelasan alur.
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
| 5 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Belum (D uji Colab; E build & DOI) |
| 6 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Belum (D: uji notebook+data; E: build & DOI) |
| 7 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | Belum (D: uji Colab; E: build & DOI) |
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
- **D (kode & reproduksibilitas):** ⚠️ Kode 1.3 (mini-challenge *persistence* dan
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
  0.0948; `loss="mae"` → MAE 0.0745 / RMSE 0.0921. Sel perbandingan MAE dan MSE (sebelumnya
  belum tereksekusi) kini ikut tereksekusi. Warning Keras `input_shape=` di `Dense` muncul
  (tidak berbahaya; opsional diganti `Input(shape=...)`). Validasi silang di Colab
  disarankan sebelum rilis karena log/GPU Colab dapat sedikit berbeda. Cadangan notebook
  sebelum uji: `C:\Users\Hi\AppData\Local\Temp\kilo\ch-02-01_backup.ipynb`.
- **E (build & output):** ⚠️ Belum diuji `node build/generate.mjs`; `bookDOI` placeholder.

### Catatan Evaluasi Bab 5 (28 Sep 2026 — setelah perbaikan)

- **A (isi & keilmuan):** ✅ Ketiga cek otomatis bersih (bahasa-asing, terminologie,
  dash-prosa; exit 0). Perbaikan terpasang: miring istilah asing disamakan dengan seluruh
  buku (`*baseline*`, `*persistence*`, `*walk-forward*`, `*learning curve*`, `*dropout*`,
  `*threshold*`, `*leakage*`, `*overfit*`/`*underfit*`, `*k-fold*`, `*cross-validation*`,
  `*trade-off*`, `*range*`, `*run*`, `*seed*`, dst. di prosa, judul, dan caption); di §5.5
  "variant" → "varian" dan "mantenir" → "pertahankan"; "latihan benarnya" → "latihan
  sebenarnya". Angka contoh terverifikasi benar (MAE 1.33, RMSE ≈1.41, R² 0.97, Willmott d
  ≈0.99, KGE klimatologi = 1−√2 ≈ −0.41, Tabel 5.4 akurasi/POD/FAR/CSI cocok); disclaimer
  materi pengenalan ada; klaim disitasi.
- **B (struktur & konsistensi):** ✅ Volume isi ±3.125 kata (target 3.000–4.500). Prasyarat
  Bab 2/3/4 benar (terverifikasi: §2.7 *leakage*, §4.6 *callback*, §4.7 *learning curve*).
  Tujuan Pembelajaran 4 butir selaras dengan 9 latihan. Penomoran persamaan (5.1), kode
  (5.1–5.3), tabel (5.1–5.5), gambar (5.1) utuh. Belum ada penutup "Koneksi ke Bab
  Berikutnya" (opsional, sama seperti Bab 2).
- **C (sitasi):** ✅ [1]–[8] urut incremental; semua ada di `refs.bib` dan daftar pustaka.
  Perbaikan terpasang: sitasi Willmott 2012 [7] dikoreksi menjadi vol. 32, no. 13, pp.
  2088–2094 dengan DOI 10.1002/joc.2419 (sebelumnya vol. 32, no. 6, pp. 573–580) — disamakan
  di `master.md` [7], `refs.bib`, daftar pustaka no. 16, dan `REGISTER.md`. DOI Gupta
  (10.1016/j.jhydrol.2009.08.003) dan buku Jolliffe (10.1002/9781119960003) terverifikasi
  valid. Dilengkapi: ISBN 978-0-262-03561-3 untuk [3] Deep Learning, tanggal akses untuk [4]
  arXiv. Catatan: arXiv:1207.0580 bukan versi JMLR 2014 [5] (itu paper workshop 2012), jadi
  tidak dicantumkan; [5] JMLR open access tanpa DOI dibiarkan.
- **D (kode & reproduksibilitas):** ⚠️ Notebook `ch-05-04_metrik_walkforward.ipynb` (17 sel)
  lengkap: seed 42, versi TensorFlow dicetak, data sintetik mandiri (tanpa unduhan), fungsi
  MAE/RMSE/R²/KGE/Willmott/POD/FAR/CSI, walk-forward + early stopping + perbandingan
  learning curve dengan/tanpa regularisasi. Uji eksekusi dari awal–akhir TIDAK dapat
  dilakukan di mesin ini (TensorFlow diblokir kebijakan mesin: DLL load failed, Application
  Control policy); wajib diuji di Colab sebelum rilis.
- **E (build & output):** ⚠️ `node build/generate.mjs` belum dijalankan (butuh Pandoc+LaTeX
  di mesin rilis); `bookDOI` masih placeholder `10.5281/zenodo.0000000`.

### Catatan Evaluasi Bab 6 (30 Sep 2026 — setelah perbaikan)

- **A (isi & keilmuan):** ✅ Ketiga cek otomatis bersih (bahasa-asing, terminologie,
  dash-prosa; exit 0). Perbaikan: salah ketik "trasformasi" → "transformasi" (§6.5).
  Notebook `ch-06-05_persiapan_data.ipynb` dibersihkan dari nama fungsi/token tidak baku
  (`_buscar_raiz` → `_cari_direktori_buku`, `cargar_nyata` → `muat_data_nyata`,
  `ETIQUETA` → `ETIKET_SUMBER`, "repoti" → "repositori"), dan guard kolom verifikasi
  dirapikan menjadi `elif c.startswith("chirps")` (kolom yang tidak ada di data tidak
  diproses).
- **B (struktur & konsistensi):** ✅ Volume isi ±4.394 kata (target 3.000–4.500);
  Tujuan Pembelajaran 4 butir selaras dengan latihan; prasyarat Bab 1/2/5; Kode 6.1–6.8,
  Tabel 6.1–6.2, Persamaan 6.1–6.3, dan Gambar 6.1 terdaftar di `REGISTER.md`. Diagram
  Alur 6.1 dihapus dan alurnya dijadikan Tabel 6.1 (pipeline 7 tahap); daftar sumber data
  dijadikan daftar berbutir (bukan tabel), sehingga tabel perbandingan format berkas
  bergeser menjadi Tabel 6.2.
- **C (sitasi):** ✅ Perbaikan: dua entri yang hilang ditambahkan ke `refs.bib`, yaitu
  [6] Okamoto et al. (GSMaP, IGARSS 2005) dan [8] WMO (WMO-No. 8, 2021). Penomoran `[n]`
  disusun ulang agar incremental sesuai kemunculan pertama (sebelumnya [11] mendahului [6]).
  URL WMO-No. 8 diperbaiki (spasi di tengah URL dihapus); inisial Jolliffe dikoreksi
  ("S." → "I. T."). Daftar pustaka agregat (`back-matter/01-daftar-pustaka.md`, kini 48
  entri) dan daftar dataset (`back-matter/03-daftar-dataset-sumber.md`, ditambah GSMaP +
  keterangan ERA5-Land) diselaraskan. Verifikasi DOI via `doi.org` tetap disarankan di
  mesin rilis.
- **D (kode & reproduksibilitas):** ⚠️ Notebook `ch-06-05_persiapan_data.ipynb` (17 sel):
  seed 42 ada; tidak memakai TensorFlow (tidak relevan untuk bab data). Notebook memakai
  data nyata di `manuscripts/ch-09-.../data` (ERA5-Land jakarta + indeks RMM/ONI) lewat
  `scripts/download_era5.py` dan `scripts/download_indices.py`; tanpa data itu muncul
  `FileNotFoundError` (memang disengaja). Uji eksekusi awal–akhir menunggu unduhan data di
  Colab.
- **E (build & output):** ⚠️ `node build/generate.mjs` belum dijalankan (butuh Pandoc+LaTeX
  di mesin rilis); `bookDOI` masih placeholder `10.5281/zenodo.0000000`.

### Catatan Evaluasi Bab 7 (5 Okt 2026 — setelah perbaikan)

- **A (isi & keilmuan):** ✅ Ketiga cek otomatis bersih (bahasa-asing, terminologie,
  dash-prosa; exit 0). Perbaikan terpasang: "*Standard*" → "Praktik standar" (§7.2);
  istilah asing tak miring dirapikan (`*zero-inflated*`, `*gusty*`) dan "*autocorrelated*"
  diselaraskan menjadi "*autokorelasi*" (istilah kanonik yang sudah dipakai bab ini);
  kalimat rusak "bekerja di deret panjang yang deret cuaca punya" → "bekerja pada deret
  panjang seperti deret cuaca" dan "untuk penulis memori kandidat" → "untuk menuliskan
  memori kandidat" (§7.5); "state tersembunyi" menyesuaikan pola buku "lapisan tersembunyi
  (*hidden layer*)" menjadi "keadaan tersembunyi (*hidden state*)" (dan "keadaan berulang",
  "keadaan antar *batch*"); desimal diseragamkan ke koma ("0,30"; "0-0,2"); klaim sejarah
  RNN diberi sitasi [1]. Angka contoh (input shape, `N-w-h+1 = 4`, periode pasang surut
  semi-diurnal 12,42 jam/diurnal 24 jam/*tidal day* 24,84 jam) benar; disclaimer materi
  pengenalan ada; framing *baseline*-dulu jujur. Koreksi akurasi §7.1: klaim "Bab 2-5
  memperlakukan data sebagai deretan contoh yang saling bebas" diganti karena keliru —
  Bab 2 §2.5/§2.7 sudah memakai *windowing* dan split menurut waktu, dan Bab 5 §5.5
  menyatakan data deret waktu tidak independen serta memakai *walk-forward*; rumusan baru
  membedakan arsitektur MLP berukuran tetap dari model sekuensial berkeadaan. Keterangan
  dalam tanda kurung "(kondisi hari ini umumnya mirip dengan kemarin)" di §7.1 dihapus
  karena definisi *autokorelasi* sudah ada di Bab 5 §5.5 (dan disebut di Bab 6 §6.6);
  penulisan "autokorelasi" diseragamkan **tanpa miring** di Bab 7 (judul §7.1, §7.3,
  tabel, Ringkasan), karena istilah ini sudah diserap. Perbaikan penyajian §7.2:
  keterangan Tabel 7.1 yang terputus ("windowing deret ke contoh-*window*") dibetulkan,
  dan penjelasan jumlah contoh `N - w - h + 1` ditulis ulang agar lebih mudah dipahami
  (mengapa `w + h` hari disita dan mengapa muncul `+ 1`). Istilah non-kanonik di §7.2
  dibetulkan: "prakiraan" → "prediksi" dan "horison" → "horizon" (temuan `cek-terminologie`),
  dan pengantar deret yang ganda dirapikan menjadi satu kalimat.
- **B (struktur & konsistensi):** ✅ Volume total 4.243 kata (prosa murni ±3.520 kata;
  memenuhi rentang checklist 3.000–4.500). Tujuan Pembelajaran 4 butir selaras dengan 9
  latihan; prasyarat Bab 2/5/6 benar; §7.11 "Menghubungkan ke Bab 8-9" berfungsi sebagai
  penutup koneksi. Penomoran aset utuh: Gambar 7.1, Tabel 7.1–7.5, Persamaan 7.1–7.6, Kode
  7.1–7.7; `REGISTER.md` diperbaiki (Kode 7.6 & 7.7 dirujuk di §7.9, bukan §7.7).
  Notebook §6 dirapikan urutannya (6 → 6a → 6b). Ditambahkan subjudul
  "### Bentuk Tensor Masukan" agar bagian Persamaan 7.1 (bentuk tensor masukan 3D) berdiri
  sendiri sebagai subbagian penting, ditambah penjelasan contoh bentuk `(32, 7, 3)` dan
  perbedaan masukan 2D (MLP) versus 3D (model sekuensial).
- **C (sitasi):** ✅ `[1]`–`[7]` urut incremental pertama-muncul; `[n]` teks ≡ daftar
  References ≡ `refs.bib`. Perbaikan: ISBN 978-0-262-03561-3 dan URL resminya
  ("diakses: September 2026") ditambahkan ke [1] Goodfellow;
  tanggal akses ("diakses: September 2026") ditambahkan ke URL [2], [6], [7] dan ke
  preprint [5]; [5] Cho diselaraskan dengan daftar pustaka agregat (EMNLP 2014, pp.
  1724–1734; preprint arXiv:1406.1078) di `master.md`, `refs.bib`, dan `REGISTER.md`. DOI
  Elman (10.1207/s15516709cog1402_1) dan LSTM (10.1162/neco.1997.9.8.1735) diverifikasi
  valid via `doi.org`/Crossref. Tidak ada self-citation berlebihan.
- **D (kode & reproduksibilitas):** ⚠️ Notebook `ch-07-06_lstm_gru.ipynb` (18 sel) lengkap:
  seed 42, versi TensorFlow dicetak, data sintetik pasang surut mandiri (tanpa unduhan),
  fungsi `buat_window`, *baseline* persistence/klimatologi, LSTM vs GRU, multivariate,
  plot aktual-prediksi, demo *direct* vs *recursive* h=24, *stacked* LSTM. Uji eksekusi
  awal–akhir belum dapat dilakukan di mesin ini (kebijakan mesin memblokir TensorFlow;
  lihat catatan Bab 5) — wajib diuji di Colab sebelum rilis. Catatan: `input_shape=` pada
  layer Keras memicu *warning* deprecation (tidak berbahaya).
- **E (build & output):** ⚠️ `node build/generate.mjs` belum dijalankan (butuh Pandoc+LaTeX
  di mesin rilis); `bookDOI` masih placeholder `10.5281/zenodo.0000000`.

### Catatan Lintas-Bab — Terminologi *window*/*horizon* (5 Okt 2026)

- **Temuan pemunculan pertama:** "*window*/*windowing*" pertama di **Bab 2** (Tujuan
  Pembelajaran baris 24; konsep di §2.5 baris 204–206; kata benda "*window*" baris 220).
  "*horizon*" pertama di **Bab 5 §5.5** (keterangan Tabel 5.5 baris 295 dan Kode 5.3 baris
  319) tanpa penjelasan, lalu baru dijelaskan di **Bab 7 §7.2** (baris 54 dan subbagian
  baris 123).
- **Perbaikan:** Bab 2 §2.5 melabeli istilah pada pemunculan pertama sebagai "**jendela
  masukan** (*window*)"; Bab 5 §5.5 melabeli "**jendela latih** (*training window*)" untuk
  konteks *walk-forward* dan menambahkan definisi singkat "*horizon*" (`h` = jumlah langkah
  ke depan) pada pemunculan pertamanya, karena istilah ini dipakai lebih dulu di Bab 5
  sebelum dijelaskan di Bab 7; Bab 7 §7.2 memakai "**jendela masukan** (*window*)" agar
  seragam. Ini menyelesaikan ambiguitas dua makna "window" (jendela masukan vs jendela
  latih) yang ditemukan saat penelusuran.
- **Verifikasi:** `cek-kualitas.py --file` untuk Bab 2, Bab 5, dan Bab 7 semuanya `exit 0`
  (bahasa-asing, terminologie, dash-prosa bersih).

### Observasi gaya (keputusan pengarang, tidak diubah)

- Dash " - " sebagai pemisah klausa di butir daftar (§7.3, butir AR(p)) diizinkan oleh
  `cek-dash-prosa.py`; dibiarkan mengikuti gaya konversasional buku. Rapatkan bila
  diinginkan pada penyuntingan akhir.
- "**Stateful LSTM**" dan "*stateful* RNN" (§7.9) mencampur bentuk bold dan miring; istilah
  teknisnya konsisten, hanya penekanannya berbeda. Diserahkan ke keputusan pengarang.
- Penulisan "autokorelasi" kini tanpa miring di Bab 7, sedangkan Bab 5 memakai cetak tebal
  saat mendefinisikan dan Bab 6 §6.6 memakai miring (`*autokorelasi*`). Perlu keputusan
  apakah seluruh buku akan menyeragamkannya (usul: tanpa miring karena sudah diserap).