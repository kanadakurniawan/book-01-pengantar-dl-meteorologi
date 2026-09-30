# Ketentuan Penulisan Buku — *Pengantar Deep Learning untuk Meteorologi*

> Dokumen konsolidasi tunggal untuk semua ketentuan penulisan buku yang telah disepakati.
> Dokumen ini merangkum dan menyatukan ketentuan dari `outline.md`, `CHECKLIST-EVALUASI.md`,
> `REGISTER.md`, `AGENTS.md`, `back-matter/00-lampiran.md`, `PANDUAN-PPT.md`, dan skrip cek di
> `scripts/`. Jika ada perbedaan, yang berlaku adalah isi dokumen sumber yang dirujuk.
> Dokumen ini menjadi acuan cepat pertama saat menulis atau menyunting bab.

## 1. Prinsip dasar

1. Buku ini adalah materi **pengenalan**, bukan klaim riset baru. Semua narasi memakai nada
   formal-hangat dan menghindari hiperbola (*overhype*).
2. **Satu bab ≈ satu artikel blog ≈ satu notebook Colab.** Tiap bab relatif singkat
   (artikel panjang).
3. **Satu buku = satu DOI Zenodo.** Rilis publik pertama adalah v2.0 (lengkap 10 bab);
   versi berikutnya menandai revisi, bukan penambahan bab.
4. **Setiap bab berdiri sendiri** dengan sidebar "Prasyarat: Bab …", tetapi seluruh buku
   memakai satu narasi, satu notasi, satu glosarium, dan satu terminologi.
5. **`manuscripts/ch-NN-*/master.md` adalah satu-satunya sumber kebenaran isi bab (SSOT).**
   Slide dan blog diturunkan dari naskah, bukan dikarang ulang.
6. **Volume target 3.000–4.500 kata isi per bab.** Rincian target per bab ada di
   `outline.md`. Tidak boleh ada bab yang terlalu kurus atau terlalu gemuk.
7. **Setiap hasil model DL dibandingkan dengan *baseline*** (persistence, klimatologi,
   linear, ARIMA, harmonik) dan dilaporkan apa adanya.

## 2. Bahasa dan ejaan

1. Seluruh naskah mengikuti **EYD** dan kaidah PUEBI. Kata tidak baku ditulis ke bentuk
   bakunya, contoh: resiko → risiko, nasehat → nasihat, ijin → izin, jaman → zaman,
   apotik → apotek.
2. Imbuhan, partikel (-lah, -kah, -pun), dan kata depan (di-, ke-, dari) ditulis sesuai kaidah.
3. Tanda baca dipakai sesuai kaidah. Tidak ada "…" di tengah kalimat dan tidak ada tanda
   baca ganda yang keliru.
4. Huruf kapital sesuai EYD. Akronim ditulis kepanjangannya pada pemunculan pertama,
   misalnya *artificial intelligence* → AI, lalu dipakai bentuk singkatnya.
5. **Angka dan satuan:** desimal dengan koma, ribuan dengan titik, satuan SI seragam
   (m/s, °C, mm/hari, m).
6. **Register "pengantar"** yang sudah ada di manuskrip wajib dipertahankan. Jangan
   mengubah konvensi ejaan pengarang secara diam-diam; bila ada masalah bahasa pada naskah,
   laporkan sebagai catatan.
7. Naskah bebas dari kontaminasi bahasa asing (kata berakar Belanda/Italia). Ini dicek
   otomatis oleh `scripts/cek-bahasa-asing.py`.

## 3. Istilah asing dan huruf miring (PUEBI pasal 18)

1. Kata, frasa, atau istilah bahasa asing yang **belum diserap** ke bahasa Indonesia
   ditulis miring (Markdown `*...*`). Berlaku di badan teks dan daftar.
2. **Wajib miring** (belum diserap KBBI), contoh: *baseline*, *persistence*,
   *climatology*, *overfit*, *underfit*, *trade-off*, *end-to-end*, *time series*,
   *neural network*, *deep learning*, *machine learning*, *feature*, *loss function*,
   *hyperparameter*, *epoch*, *batch size*, *learning rate*, *gradient descent*,
   *backpropagation*, *callbacks*, *early stopping*, *dropout*, *seed*, *nowcasting*,
   *downscaling*, *generative*, *pipeline*, *leakage*, *walk-forward*, *skill score*.
3. **Tidak miring** (nama diri, merek, akronim, kata yang sudah diserap): TensorFlow,
   PyTorch, Keras, NumPy, Pandas, scikit-learn, xarray, Google Colab, Python, GitHub,
   Zenodo, DOI, ISBN, arXiv, GPU, CPU, TPU, ERA5, ERA5-Land, WMO, IEEE, BMKG, Internet.
4. **Pemunculan pertama** istilah yang punya padanan Indonesia memakai pola
   "padanan Indonesia (*istilah Inggris*)" (misal "tolok ukur (*baseline*)"). Setelah itu
   konsisten memakai salah satu bentuk saja, jangan mencampur dalam satu paragraf.
5. **Di blok kode, label plot, dan identifier program** istilah tidak dimiringkan; kode
   adalah teks verbatim.
6. **Satu istilah satu padanan.** Glosarium (`front-matter/06-glosarium-notasi.md`)
   adalah satu sumber; istilah sama dipakai di buku, blog, slide, dan YouTube.

## 4. Terminologi kanonik (satu konsep = satu istilah)

Kampanye terminologi menyepakati bentuk kanonik berikut. Pelanggaran dicek otomatis oleh
`scripts/cek-terminologie.py` (exit 0 = bersih).

| Kata yang dipakai | Ganti dengan |
|---|---|
| `error`, `errors`, `kesalahan` | galat |
| `station`, `stations` | stasiun |
| `prakiraan` | prediksi |
| `forecast` (di prosa) | prediksi |
| `patokan` | *baseline* |
| `training` (di prosa) | pelatihan |

Pengecualian yang dibolehkan: frasa tetap seperti "mean absolute error",
"sea level station monitoring", "multi-step forecast", "retraining"; judul referensi;
nama diri; istilah dalam tanda miring; blok kode; URL; dan baris daftar pustaka.

## 5. Gaya prosa dan kalimat

1. **Tanpa tanda hubung berspasi `" - "` sebagai pemisah klausa** di kalimat naratif,
   termasuk pola `"- justru _"`, `"- padahal _"`, dan aposisi ganda `"X - keterangan - Y"`.
   Ganti dengan koma, titik dua, titik, atau pecah menjadi kalimat baru. Dicek otomatis
   oleh `scripts/cek-dash-prosa.py`.
2. Konteks yang tetap dibolehkan memakai `" - "`: label penomoran (`"Bab 8 - "`,
   `"Kode 8.1 - "`, `"Gambar 8.1 - "`, `"Tabel 8.1 - "`), frontmatter YAML, item daftar
   (bullet/bernomor), tabel markdown, blok kode dan math, rentang/operasi angka, dan URL.
3. Kalimat utuh, subjek–predikat jelas, tidak rancu, tidak menggantung, tidak bermakna ganda.
4. Kalimat panjang dipecah. Hindari kalimat bergulir dengan banyak anak kalimat.
5. Satu paragraf satu gagasan utama; paragraf bertautan logis; kata ganti ("ini",
   "tersebut", "-nya") jelas acuannya.
6. Tidak bertele-tele dan tidak mengklaim lebih dari yang didukung data.
7. **Setiap aset (gambar, tabel, persamaan, kode) wajib dirujuk dan dibahas di teks.**
   Tabel tidak boleh tampil tanpa pembahasan minimal pada bagian terkait.
8. **Kata kunci SEO cukup di metadata YAML** bab, tidak di badan teks (keputusan penulis).

## 6. Struktur bab (template seragam)

Urutan baku tiap bab:

1. **Tujuan Pembelajaran** — 3 sampai 5 butir aksi, di awal bab.
2. **Pembukaan masalah** — konteks dan motivasi.
3. **Isi/konsep** — penjelasan dengan intuisi dan kode.
4. **Kode/notebook** — blok kode pendek dan rujukan notebook Colab.
5. **Ringkasan kunci** — 3 sampai 5 butir.
6. **Latihan** — dirancang untuk menguji Tujuan Pembelajaran (*constructive alignment*).
7. **Referensi** — IEEE bernomor, lengkap dengan DOI.

Ketentuan tambahan:

- Sidebar "Prasyarat: Bab …" benar untuk tiap bab.
- Penutup "Koneksi ke Bab Berikutnya": wajib di Bab 1, opsional di bab lain.
- Target volume isi 3.000–4.500 kata per bab (tabel detail di `outline.md`).

## 7. Penomoran aset

1. Format: `Gambar bab.nomor`, `Tabel bab.nomor`, `Persamaan (bab.nomor)`,
   `Kode bab.nomor`.
2. Deret nomor tiap jenis **reset di tiap bab**.
3. **Setiap aset wajib dirujuk di teks** pada bagian terkait; nomor tidak boleh ganda dan
   tidak boleh loncat.
4. `REGISTER.md` adalah register terpusat penomoran aset dan sitasi. **Setiap penambahan
   aset atau sitasi baru di `master.md` wajib segera diperbarui di `REGISTER.md`.**
5. Nomor aset dan sitasi mengikuti `master.md` (sumber kebenaran); jangan menomori ulang
   hanya di register.

## 8. Notasi dan glosarium

- Notasi matematis dan istilah terpusat di `front-matter/06-glosarium-notasi.md`.
- Istilah Indonesia + Inggris ditulis seragam di seluruh buku; satu istilah satu padanan.
- Istilah baru ditulis "padanan Indonesia (*istilah Inggris*)" pada pemunculan pertama dan
  dikumpulkan di glosarium.

## 9. Sitasi

1. **Gaya IEEE** bernomor `[1]`, `[2]`, dst., muncul berurutan sesuai kemunculan pertama
   di teks.
2. `[n]` di teks ≡ daftar References ≡ `refs.bib` per bab (identik urutan dan isinya, agar
   output PDF via citeproc sama dengan versi Markdown/blog).
3. **DOI wajib dicantumkan bila tersedia** dan diuji lewat `doi.org/<doi>`. Bila tanpa DOI,
   cantumkan ISBN atau arXiv. URL hanya bila tidak ada DOI dan wajib diberi tanggal akses.
4. Setiap `[n]` harus benar-benar mendukung klaim pada kalimatnya (cek silang isi sumber,
   bukan sekadar konsistensi nomor).
5. Sitasi per klaim, bukan per paragraf kabur. Parafrase, bukan salin-tempel; kutipan
   langsung pendek diberi tanda kutip.
6. Hierarki sumber: jurnal/prosiding peer-reviewed dan buku teks klasik (tertinggi),
   buku teks DL/ML, dokumentasi resmi library, dataset (wajib lisensi dan cara akses),
   preprint (tandai "preprint"), blog/Wikipedia (hanya konteks).
7. Jumlah referensi per bab: 6–12 (Bab 1–5), 8–15 (Bab 6–7), 10–20 (Bab 8–10).
8. Self-citation (DOI buku sendiri melalui `bookDOI`) diperbolehkan secukupnya, tidak
   berlebihan.
9. Pilihan sumber: utamakan yang berusia ≤ 5–10 tahun untuk topik yang cepat berubah;
   preferensikan literatur domain meteo/ocean/hidro bila ada.

## 10. Kode dan reproduksibilitas

1. **Seed tetap** di awal setiap notebook: `np.random.seed(42)` dan `tf.random.set_seed(42)`.
2. **Versi TensorFlow** dicetak di notebook (biasanya sel pertama) dan tercatat di metadata
   rilis Zenodo.
3. Notebook diletakkan di folder `notebooks/` dengan prefix `ch-<NN>-`, satu per bab.
4. Data contoh sintetik di-commit di repositori agar notebook berjalan tanpa internet;
   data riil diunduh melalui skrip yang disediakan (lihat `scripts/README-data.md`).
   Snapshot dataset studi kasus diunggah ke Zenodo saat rilis.
5. Semua notebook harus dapat dieksekusi dari awal sampai akhir tanpa galat.
6. Eksekusi GPU bersifat non-deterministik; perbedaan kecil pada angka desimal terakhir
   antar-run adalah wajar (Lampiran A).

## 11. Front matter dan back matter

- Struktur mengikuti `outline.md`: front (00-halaman-judul sampai 06-glosarium-notasi),
  back (00-lampiran sampai 06-kolofon).
- `front-matter/05-cara-memakai-buku.md` bukan bagian dari bab dan **tidak dirilis ke
  Zenodo sebagai bab ber-DOI**.
- `back-matter/01-daftar-pustaka.md` adalah daftar agregat (IEEE + DOI) yang selaras
  dengan `refs.bib` tiap bab.
- `back-matter/00-lampiran.md`: Lampiran A (reproduksibilitas dan lingkungan komputasi)
  dan Lampiran B (konvensi penulisan dan penomoran aset).

## 12. Metadata YAML `master.md`

| Field | Kegunaan |
|---|---|
| `title` | Judul bab (blog + PDF) |
| `description` | Ringkasan di blog dan metadata PDF |
| `pubDate` | Tanggal rilis, format ISO `YYYY-MM-DD` |
| `categories`, `tags` | Kategori dan SEO blog |
| `version` | Versi bab (semver) |
| `bookDOI` | DOI buku Zenodo (satu untuk seluruh buku) |
| `status` | `draft` atau `published` |
| `chapter` | Nomor bab |

## 13. Cek kualitas otomatis (wajib sebelum melaporkan "selesai")

1. **Cek kualitas terpadu** untuk manuskrip: `python scripts/cek-kualitas.py`
   (atau `npm run cek`) pada seluruh buku, atau `python scripts/cek-kualitas.py
   --file <path>` untuk satu berkas. Terdiri dari tiga cek:
   - `cek-bahasa-asing.py` — kontaminasi kata berakar Belanda/Italia;
   - `cek-terminologie.py` — terminologi kanonik (bagian 4);
   - `cek-dash-prosa.py` — tanda hubung berspasi (bagian 5).
   Laporkan "bersih" hanya bila exit code 0.
2. **Cek bahasa respons chat** (aturan `AGENTS.md` pasal 3): setiap draft respons chat
   disimpan ke berkas sementara lalu diperiksa dengan
   `python scripts/cek-bahasa-asing.py --chat --file <draft.md>`; exit 0 wajib sebelum
   dikirim.
3. **Cek slide:** `npm run slide:build` dan `npm run slide:cek` (detail di `PANDUAN-PPT.md`).
4. Sebelum publikasi, seluruh buku harus lolos `CHECKLIST-EVALUASI.md` Fase 2 (bagian A–E).

## 14. Slide presentasi (ringkasan)

- Satu deck per bab di `slides/ch-NN/slides.md`; aturan penuh di `PANDUAN-PPT.md`.
- Slide memakai SSOT tingkat aset: narasi dari `master.md`, gambar dari `figures/`,
  kode dari notebook, sitasi dari `refs.bib`, istilah dari glosarium.
- Warna, font, dan ukuran hanya diubah lewat `slides/theme/tokens.json`, lalu
  `npm run slide:tema`. Jangan menyunting `reference-doc.pptx` atau `theme.css` manual.
- Slide dilarang memakai em-dash/en-dash; maksimal 70 kata per slide; gambar wajib
  keterangan, sumber/lisensi, dan alt text; sitasi IEEE sama dengan naskah.
- `scripts/cek-slide.py` memeriksa otomatis dan dijalankan di dalam `npm run slide:build`.

## 15. Aturan kerja penyuntingan (dari `AGENTS.md`)

- Manuskrip (`manuscripts/*/master.md` dan berkas buku lain) **wajib tetap dalam register
  "pengantar"** yang sudah ada. Banlist bahasa chat tidak berlaku untuk teks manuskrip.
- Bila mengusulkan kata asing baru yang bukan Bahasa Indonesia/Inggris, catat secara
  eksplisit dalam respons agar pengarang bisa menilai.
- Bila melihat masalah bahasa pada manuskrip, laporkan sebagai catatan, jangan mengubah
  konvensi ejaan pengarang secara diam-diam.
- Setelah menyunting manuskrip, jalankan cek kualitas terpadu (bagian 13) sebelum
  melaporkan "selesai".
- Aturan bahasa komunikasi (banlist kata, uji mandiri, *hard language gate*) berlaku untuk
  respons chat dan diatur lengkap di `AGENTS.md` pasal 1–3a.

## Sumber dokumen

| Dokumen | Peran |
|---|---|
| `outline.md` | Rencana isi, target volume, aturan konsistensi global, kriteria sitasi, alur kerja |
| `CHECKLIST-EVALUASI.md` | Checklist evaluasi internal (bahasa, struktur, sitasi, kode, build) |
| `REGISTER.md` | Register penomoran aset dan sitasi per bab |
| `AGENTS.md` | Aturan bahasa komunikasi, uji mandiri, dan aturan kerja penyuntingan |
| `back-matter/00-lampiran.md` | Lampiran A (reproduksibilitas) dan B (konvensi penulisan) |
| `front-matter/05-cara-memakai-buku.md` | Konvensi yang disampaikan ke pembaca |
| `PANDUAN-PPT.md` | Aturan lengkap slide presentasi |
| `scripts/*.py` | Penegakan otomatis ketentuan bahasa, terminologi, dan gaya |