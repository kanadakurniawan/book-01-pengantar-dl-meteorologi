# AGENTS.md — Aturan Proyek: *Pengantar Deep Learning untuk Meteorologi*

> Dokumen ini berlaku sebagai konfigurasi proyek untuk SEMUA sesi/agen yang berjalan di
> workspace `books/01-pengantar-dl-meteorologi/`. Aturan di bawah adalah tambahan atas
> aturan global `~/.config/kilo/AGENTS.md` (Aturan Bahasa). Jika bertentangan, aturan
> global menang; dokumen ini menangani masalah spesifik yang muncul di proyek ini.

## 1. Aturan Bahasa Komunikasi (wajib, berlaku untuk CHAT + Proses Berpikir)

**Chat/respons kepada user:**
1. Hanya **Bahasa Indonesia standar** atau **Bahasa Inggris**.
2. **JANGAN mencampur bahasa lain ke dalam teks sendiri — tidak satu kata pun** (kecuali
   bahasa Inggris). Istilah teknis (TensorFlow, *baseline*, *deep learning*, Colab, ERA5,
   `master.md`, dst.) tetap ditulis verbatim sesuai aturan global — itu bukan pelanggaran.
3. **Kata-kata dari register buku "pengantar" tidak boleh dipakai dalam prosa chat.**
   Sebagian kata manuskrip berbau bahasa asing dan membuat teks chat tidak terbaca.
   Jika istilah buku benar-benar diperlukan, kutip dengan penanda: `dalam bahasa buku: "…"`.
4. **Proses berpikir (thinking):** hanya Bahasa Indonesia atau Bahasa Inggris.

**Pengeditan berkas (isi buku):**
- `manuscripts/*/master.md` dan berkas buku lain HARUS tetap dalam register "pengantar"
  yang sudah ada (itu suara khas buku dan konvensi ejaan pengarang). Banlist di bawah
  berlaku untuk CHAT, bukan untuk teks manuskrip.
- Meta-pembicaraan sendiri di README/CHECKLIST boleh memakai Bahasa Indonesia standar
  (bukan register manuskrip), tetapi tetap hindari kata berbau bahasa asing.

## 2. Banlist (tanda kontaminasi — JANGAN dipakai di chat)

| Kata berbau asing (dilarang di chat) | Gantilah dengan |
|---|---|
| rincian | detail (atau "perincian" hanya sebagai kutipan buku) |
| verdiwa | kesimpulan / menilai |
| persis | tepat / exactly |
| selaraskan | samakan / sinkronkan |
| perbanding | perbandingan / comparison |
| selengkapt | lengkap / complete |
| teleportasi, uitgave, diketing, maksed | hapus, lalu tulis ulang dalam Bahasa Indonesia atau Inggris |

Jika masalah kambuh, tambahkan token baru ke dalam daftar ini.

## 3. Uji Mandiri (wajib sebelum setiap respons chat dikirim)

1. Pindai teks saya sendiri untuk token dari banlist + kata non-Indonesia/non-Inggris lain.
2. Jika menemukan kata mencurigakan → ganti dengan Bahasa Indonesia standar atau Inggris,
   atau tulis ulang kalimatnya.
3. Kalau kalimat tanpa kata itu sudah tidak mengalir → tulis ulang seluruh kalimat;
   JANGAN biarkan kata asing itu berdiri.
4. Jika saya tergoda menyalin istilah buku → beri penanda `dalam bahasa buku: "…"`.
5. **Pindai khusus kata fungsi berakar bahasa Belanda** (sumber kontaminasi di
   proyek ini): `zonder`, `met`, `en`, `niet`, `alleen`, `voor`, `uit`, `een`,
   `de`, `het`, `van`, `wordt`, `zijn`, `heeft`, `maar`, `als`, `omdat`, `veel`,
   `goed`, `ook`, `opnieuw`, `terug`, `blijft`, `gegenereerd`, `gebruikt`,
   `gemaakt`, `wel`, `toch`, `geen`, `nog`, `weer`, `geëvalueerd`, `deze`,
   `geabsorbeerd`, `moeten`, `rechtop`, `schuin`, `ter`, `één`, `regels`,
   `bestanden`, `gewijzigd`, `canonieke`, `bevestigt`, `zodra`, `totaal`,
   `kruis`, `altijd`, `elke`, `keer`, `volledige`, `enige`, `worden`, `staan`,
   `ovvero`, `già`, `tutto`, `altre`, `finali`, `tutti`, `rimasto`,
   `toccato`, `misti`, `vuole`, `coerenza`, `ortografia`, `grafia`,
   `manoscritto`, `proceda`, `assorbiti`, `indonesiani`, `attuale`,
   `stessa`, `richiede`, `ecc` (ronda 4: bahasa Italia).
   Ronda 5 (kontaminasi chat setelah sitasi dari register buku): `zorg`,
   `zitten`, `laten`, `struikelen`, `nergens`, `legger`, `precies`,
   `overslaan`, `vloeiend`, `stapelen`, `geankerd`, `leest`, `betekent`,
   `groter`, `groot`, `ankert`, `wisselt`, `uitleg`, `verandert`, `denkt`,
   `voorstel`, `herschrijven`, `gereed`, `hoeft`, `erna`, `leg`, `zit`,
   `aanloop`, `ervoor`, `blijft`, `identiek`, `ontbrekende`, `bruggen`,
   `noot`, `toepassen`, `grootte`, `stap`, `langzaam`, `springt`, `beetje`,
   `groeit`, `haalt`, `weg`, `barrière`, `heel`, `klein`, `hoeveel`,
   `vóór`, `héél`, `te`, `aan`.
   Ronda 6 (tokens Belanda baru dari draft chat): `lijst`,
   `uitgebreid`, `gecheckt`, `hieronder`, `binnen`, `kort`, `doorlaten`,
   `telkens`, `achter`, `vanaf`, `tot`, `zelf`, `liep`, `verder`, `stel`,
   `stelt`, `vind`, `vindt`, `weet`, `zeg`, `zei`, `leek`.
   Bila token itu muncul di teks chat → ganti dengan Bahasa Indonesia standar
   atau tulis ulang kalimat (langkah 2-3).
6. **Pindai otomatis respons chat**: simpan draft respons ke berkas temp lalu
   jalankan `python scripts/cek-bahasa-asing.py --chat --file <draft.md>`;
   exit 0 wajib SEBELUM dikirim. Flag `--chat` ikut melacak banlist §2
   (rincian, persis, perbanding, dst.) yang sah dipakai di dalam register buku
   tetapi terlarang di prosa chat. Cara ini satu-satunya jaminan yang andal:
   pemindaian manual saja terbukti tidak cukup. Ini mencakup langkah 1 dan 5
   secara mekanis.
7. **Saat penyuntingan manuskrip**: jalankan cek kualitas terpadu
   `python scripts/cek-kualitas.py` (atau `npm run cek`) pada berkas yang
   disunting (atau seluruh buku) SEBELUM melaporkan "selesai"; laporkan hanya
   "bersih" bila exit code 0. Cek terpadu ini menjalankan `cek-bahasa-asing.py`,
   `cek-terminologie.py`, dan `cek-dash-prosa.py` sekaligus. Untuk berkas
   tunggal di luar root, gunakan `--file <path>`.
8. Jaga kalimat chat tetap pendek; bila ragu soal satu kata, tulis ulang kalimat
   daripada menebak register.
9. **Semua berkas proyek** (AGENTS.md, CHECKLIST, dokumentasi) ditulis dalam Bahasa
   Indonesia atau Bahasa Inggris. Jangan memakai bahasa Belanda sebagai bahasa
   pengantar, karena bahasa berkas menular ke bahasa respons chat.

## 3a. Hard language gate for chat responses (incident 2026-09-28)

An incident on 2026-09-28: a chat response was sent entirely in Dutch
(`Kwaliteitscheck voor bab 5 is voltooid. Ik heb ... uitgevoerd ...`).
The automated check flags that exact draft (17 hits), so the failure was
procedural, not technical. Root causes found:

1. The mandatory pre-send check (rule 6 in section 3) was skipped.
2. The context is saturated with Dutch tokens: the banlist itself, Dutch words
   in this file's prose (cleaned in this revision), and the "pengantar"
   register that sounds close to Dutch. While trying to write Indonesian, the
   response drifted into Dutch instead.
3. The thinking process also ran in Dutch (violating section 1 rule 4) and
   leaked into the final text.

Prevention rules (hard requirements):

1. EVERY chat response draft must be saved to a temp file and checked with
   `python scripts/cek-bahasa-asing.py --chat --file <draft.md>` before
   sending. Exit 0 is required. Never skip this step, even for short replies.
2. If the check fails, or if there is any doubt about the language of a
   sentence, rewrite the WHOLE sentence in plain English (safe fallback).
   Do NOT repair a sentence word by word in a language you are unsure of:
   that is exactly how the Dutch draft of 2026-09-28 was produced.
3. Deleting only the flagged word is not enough: Dutch word order and grammar
   stay behind. Rewrite the sentence.
4. Keep the thinking process in English or Indonesian. If it drifts into
   Dutch, restart the thinking in English before composing the response.

## 4. Pelaporan

- Jika dalam pengeditan teks manuskrip saya mengusulkan kata asing baru yang bukan
  Bahasa Indonesia/Inggris, catat secara eksplisit dalam respons agar author (user)
  bisa menilainya.
- Jika saya melihat masalah bahasa pada teks manuskrip, laporkan sebagai catatan
  (observasi internal) — jangan diam-diam mengubah konvensi ejaan, itu keputusan pengarang.

## 5. Slide Presentasi (PPT) per Bab

- Setiap bab punya satu deck di `slides/ch-NN/slides.md`. Aturan lengkap ada di
  `PANDUAN-PPT.md`; kerangka awal dari `slides/_template/slides.md`.
- Warna, font, dan ukuran hanya diubah lewat `slides/theme/tokens.json`, lalu
  jalankan `npm run slide:tema`. Jangan menyunting `reference-doc.pptx` atau
  `theme.css` secara manual karena akan tertimpa.
- Gambar diambil dari `manuscripts/ch-NN-*/figures/` lewat rujukan `figures/...`,
  dan istilah serta sitasi mengikuti naskah.
- Sebelum melaporkan deck selesai, jalankan `npm run slide:build` dan pastikan
  exit code 0 (`cek-slide.py` dijalankan otomatis di dalamnya).