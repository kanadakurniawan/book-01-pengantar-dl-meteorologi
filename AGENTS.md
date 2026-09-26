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
   `stessa`, `richiede`, `ecc` (ronda 4: Italiaans).
   Bila token itu muncul di teks chat → ganti dengan Bahasa Indonesia standar
   atau tulis ulang kalimat (langkah 2-3).
6. **Pindai otomatis respons chat**: simpan draft respons ke berkas temp lalu
   jalankan `python scripts/cek-bahasa-asing.py --file <draft.md>`; exit 0 wajib
   SEBELUM dikirim. Ini mencakup langkah 1 dan 5 dengan cara yang mekanis.
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

## 4. Pelaporan

- Jika dalam pengeditan teks manuskrip saya mengusulkan kata asing baru yang bukan
  Bahasa Indonesia/Inggris, catat secara eksplisit dalam respons agar author (user)
  bisa menilainya.
- Jika saya melihat masalah bahasa pada teks manuskrip, laporkan sebagai catatan
  (observasi internal) — jangan diam-diam mengubah konvensi ejaan, itu keputusan pengarang.