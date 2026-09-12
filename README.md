# Pengantar Deep Learning untuk Meteorologi

> **"Deep learning untuk meteorologi, dari praktisi untuk praktisi di Indonesia."**

Buku pengenalan open-source berbahasa Indonesia yang ditulis oleh **Kanada Kurniawan** —
Meteorology Officer di BMKG (Stasiun Meteorologi Kelas III Maritim Dwikora, Pontianak) dengan
latar riset pengembangan model neural network untuk prediksi cuaca, pasang surut, dan
hidrologi.

Ini adalah materi **pengenalan**, bukan hasil riset baru. Gagasannya sederhana: banyak
praktisi dan mahasiswa kebumian ingin belajar deep learning, tetapi materi yang beredar
terlalu berorientasi ilmu komputer dan jauh dari konteks data Indonesia. Buku ini hadir
untuk mengisi celah itu — dengan contoh data lokal dan bahasa yang bisa dipahami.

## Konsep

Setiap **bab adalah satu artikel blog** yang:

1. Ditulis sebagai **Markdown (master)** di `manuscripts/` — satu-satunya sumber kebenaran isi.
2. Di-sinkronkan ke blog sehingga versi "live" selalu aktual:
   ```
   node build/sync-to-blog.mjs
   ```

**Satu buku = satu DOI Zenodo.** PDF/DOCX utuh buku dirilis di `releases/` per versi.
Karena seluruh 10 bab sudah selesai, rilis publik pertama langsung lengkap (v2.0);
versi berikutnya (v2.1, v3.0) menandai revisi, bukan penambahan bab. Tiap bab relatif
singkat (artikel panjang), sehingga tidak dipublikasikan per-bab di Zenodo; sitasi
stabil melalui DOI buku, sedangkan traffic per topik diperoleh dari artikel blog.

> Rencana detil isi buku (isi per bab, notebook, latihan, SEO, blog mapping, pacing rilis)
> ada di **`outline.md`** — sumber kebenaran perencanaan, dipakai saat menulis tiap bab.

Pendekatan "buku yang hidup" ini memungkinkan materi terus diperbarui tanpa memutus tautan
sitasi — versi baru naik di Zenodo, concept DOI tetap sama.

## Struktur Repositori

```
01-pengantar-dl-meteorologi/
├── outline.md               # OUTLINE: rencana & detil isi 10 bab (sumber perencanaan)
├── front-matter/
│   ├── 00-halaman-judul.md   # Halaman judul (judul, edisi, penulis, DOI)
│   ├── 01-hak-cipta-lisensi.md # Hak cipta & lisensi (imprint)
│   ├── 02-daftar-isi.md      # Daftar isi buku
│   ├── 03-daftar-gambar-tabel.md # Daftar gambar & tabel
│   ├── 04-prakata.md         # Prakata
│   ├── 05-cara-memakai-buku.md  # Peta baca & konvensi (tidak dirilis sebagai bab)
│   └── 06-glosarium-notasi.md # Glosarium, notasi, dan singkatan
├── manuscripts/
│   └── ch-01-pengantar-deep-learning-meteorologi/
│       ├── master.md        # MASTER: sumber kebenaran isi bab
│       ├── refs.bib         # referensi (dipakai saat PDF build via citeproc)
│       └── figures/         # gambar bab (PNG untuk PDF, webp untuk blog)
├── back-matter/
│   ├── 00-lampiran.md       # Lampiran A & B (reproduksibilitas, konvensi)
│   ├── 01-daftar-pustaka.md # Daftar pustaka agregat (IEEE + DOI)
│   ├── 02-indeks.md         # Indeks tematik
│   ├── 03-daftar-dataset-sumber.md # Dataset & sumber data + lisensi
│   ├── 04-daftar-notebook-doi.md   # Daftar notebook & DOI
│   ├── 05-tentang-penulis.md
│   └── 06-kolofon.md
├── notebooks/               # notebook Colab (nama berawalan bab: ch-01-*.ipynb)
├── releases/
│   └── v2.0.0/              # snapshot tiap rilis (PDF+DOCX) → untuk Zenodo
└── build/
    ├── generate.mjs         # master.md → buku utuh (PDF + DOCX) per versi
    └── sync-to-blog.mjs     # sinkronkan master+figures+notebooks → blog (site/src/content/book)
```

## Frontmatter `master.md`

| Field | Kegunaan |
|---|---|
| `title` | Judul bab (blog + PDF) |
| `description` | Ringkasan di blog & metadata PDF |
| `pubDate` | Tanggal rilis (format ISO `YYYY-MM-DD`) |
| `categories`, `tags` | Kategori/SEO blog |
| `version` | Versi bab (semver) |
| `bookDOI` | DOI buku Zenodo (satu untuk seluruh buku; diisi saat rilis) |
| `status` | `draft` (belum live) atau `published` |
| `chapter` | Nomor bab |

## Alur Kerja Penulisan & Penerbitan

**Menulis (Fase 1):** tulis seluruh Bab 1–10 dulu (`master.md` + `refs.bib` + `figures/`
+ `notebooks/`), dengan target volume 3.000–4.500 kata/bab. **Commit lokal setelah tiap
bab** sebagai backup; repo publik baru dibuka saat siap rilis.

**Evaluasi internal (Fase 2):** sebelum publikasi, seluruh buku harus lolos checklist —
isi & keilmuan (sitasi per klaim, anti-overhype), struktur (template seragam, prasyarat),
sitasi ([n] ≡ References ≡ refs.bib, DOI valid), reproduksibilitas (notebook jalan), dan
build (generate.mjs tanpa error). Rincian lengkap: `outline.md` → "Alur Kerja Penulisan
& Evaluasi Internal".

**Penerbitan (Fase 3):** setelah lolos → daftarkan **DOI Zenodo** untuk buku utuh, buat
**ISBN**, buka **GitHub publik** (release v2.0.0), lalu **posting blog 2 artikel/bulan**
berbasis bab.

Tanpa lolos Fase 2, tidak ada publikasi (Zenodo/ISBN/GitHub publik/blog).

## Alur Kerja Rilis (saat milestone tercapai)

1. Generate bundel buku:
   ```
   node build/generate.mjs --version=v2.0.0
   ```
2. Unggah `releases/v2.0.0/` ke Zenodo → dapat **satu DOI buku**, salin ke field
   `bookDOI` di semua bab.
3. Buat ISBN, buka repo publik, buat GitHub release.
4. Posting blog per bab (2 artikel/bulan) via `node build/sync-to-blog.mjs`.

## Prasyarat

- **Pandoc** (wajib untuk output PDF/DOCX): https://pandoc.org
- **LaTeX** (hanya untuk output PDF; DOCX tidak butuh): mis. TinyTeX.

Tanpa keduanya, script tetap bisa sinkronkan master ke blog (tanpa hasil PDF/DOCX).

## Terhubung dengan Brand

- Blog & versi live bab: **kanadakurniawan.com**
- Situs web (deploy): repo `kanadakurniawan/site`

## Lisensi

Dokumen buku © Kanada Kurniawan. Silakan disebarluaskan, dikutip, dan dimanfaatkan untuk
belajar — upayakan tetap memberi kredit melalui **DOI buku Zenodo**.