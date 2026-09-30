# Slide Presentasi Bab

Folder ini menampung sumber slide per bab. Aturan lengkap ada di
[PANDUAN-PPT.md](../PANDUAN-PPT.md). Ringkasnya:

- **Sumber:** satu berkas `slides.md` per bab di `slides/ch-NN/`.
- **Tema:** semua warna, font, dan ukuran berasal dari satu berkas
  `theme/tokens.json`. Jangan menyunting berkas tema hasil build.
- **Aset bersama:** gambar diambil dari `manuscripts/ch-NN-*/figures/`, tidak
  disalin ulang. Kode dan sitasi mengikuti notebook dan `refs.bib` bab.

## Struktur

```
slides/
  theme/
    tokens.json          # sumber tunggal desain (warna, font, ukuran)
    reference-doc.pptx   # hasil generate, template PPTX untuk pandoc
    theme.css            # hasil generate, tema HTML (reveal.js)
  _template/slides.md    # kerangka deck, salin ke ch-NN/
  ch-01/slides.md        # deck Bab 1
  ch-02/slides.md        # deck Bab 2
  ...
  build/                 # hasil render (pptx, html), tidak di-commit
```

## Perintah

```
npm run slide:tema     # bangkitkan tema dari tokens.json
npm run slide:build    # render semua deck (pptx + html) lalu jalankan cek
npm run slide:cek      # pengaman konsistensi saja
npm run slide          # sama dengan slide:build
```

Mulai deck baru:

1. Salin folder `_template` menjadi `ch-01` (atau sesuai bab).
2. Ubah `title` di frontmatter dan isi slide.
3. Rujuk gambar dengan `figures/...` (mengarah ke `figures/` bab terkait).
4. Jalankan `npm run slide:build`.

Hasil render ada di `slides/build/`. Berkas `.pptx` bisa dibuka dan diedit
langsung di PowerPoint; berkas `.html` untuk tayang di peramban.
