#!/usr/bin/env python3
"""
Regenerasi semua gambar buku TANPA judul/teks penjelasan di dalam gambar.
- Judul & penjelasan dipindah ke caption di master.md.
- Label sumbu, legenda, dan label garis pendek yang intrinsik tetap dipertahankan.
Gunakan: python scripts/generate_figures_all.py
"""
from __future__ import annotations
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
MANS = ROOT / "manuscripts"

np.random.seed(42)
DPI = 160


def save(fig, path: Path, close=True, **kw):
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=DPI, bbox_inches="tight", **kw)
    try:
        fig.savefig(path.with_suffix(".webp"), dpi=DPI, format="webp",
                    bbox_inches="tight")
    except Exception:
        pass
    if close:
        plt.close(fig)


# ---------------------------------------------------------------- fig-2-1
def fig_2_1():
    fig, ax = plt.subplots(figsize=(10, 4.5))
    ax.axis("off")
    ax.set_xlim(0, 12)
    ax.set_ylim(-2.3, 2.3)

    cx, cy, r = 5.0, 0.0, 0.95

    # masukan x1..x4 dengan bobot w1..w4
    inputs = [(1.0, 1.45, r"$x_1$", r"$w_1$"),
              (1.0, 0.5, r"$x_2$", r"$w_2$"),
              (1.0, -0.5, r"$x_3$", r"$w_3$"),
              (1.0, -1.45, r"$x_4$", r"$w_4$")]
    for ix, iy, lx, lw_ in inputs:
        ax.text(ix - 0.2, iy, lx, ha="right", va="center", fontsize=15,
                color="#1f4e79")
        start = (ix + 0.12, iy)
        dx, dy = cx - start[0], cy - start[1]
        norm = (dx * dx + dy * dy) ** 0.5
        end = (cx - r * dx / norm, cy - r * dy / norm)
        ax.annotate("", xy=end, xytext=start,
                    arrowprops=dict(arrowstyle="-|>", color="#555", lw=1.5))
        # label bobot: tegak lurus garis, di tengah
        ex, ey = end[0] - start[0], end[1] - start[1]
        elen = (ex * ex + ey * ey) ** 0.5
        nx, ny = -ey / elen, ex / elen
        mid = ((start[0] + end[0]) / 2 + 0.35 * nx,
               (start[1] + end[1]) / 2 + 0.35 * ny)
        ax.text(mid[0], mid[1], lw_, ha="center", va="center",
                fontsize=13, color="#c0552b")

    # badan neuron (penjumlahan)
    circ = plt.Circle((cx, cy), r, fc="#dbe9f6", ec="#1f4e79", lw=2)
    ax.add_patch(circ)
    ax.text(cx, cy, r"$\sum$", ha="center", va="center", fontsize=22,
            color="#1f4e79")
    ax.text(cx + 0.9, cy + r + 0.52,
            r"$z = w_1 x_1 + w_2 x_2 + w_3 x_3 + w_4 x_4 + b$",
            ha="center", fontsize=12.5, color="#1f4e79")

    # bias b dari bawah masuk ke neuron (Σ)
    bx, by = cx, cy - r - 0.75
    ax.annotate("", xy=(cx, cy - r + 0.06), xytext=(bx, by),
                arrowprops=dict(arrowstyle="-|>", color="#c0552b", lw=1.8))
    ax.text(bx + 0.05, by - 0.32, r"$b$", ha="center", va="center",
            fontsize=18, color="#c0552b", fontweight="bold")

    # fungsi aktivasi f
    bx0, by0, bw, bh = 6.9, -0.55, 1.1, 1.1
    box = plt.Rectangle((bx0, by0), bw, bh, fc="#f5ead6", ec="#c0552b", lw=2)
    ax.add_patch(box)
    ax.text(bx0 + bw / 2, by0 + bh / 2, r"$f$", ha="center", va="center",
            fontsize=20, color="#c0552b")
    ax.annotate("", xy=(bx0, 0), xytext=(cx + r, 0),
                arrowprops=dict(arrowstyle="-|>", color="#555", lw=1.5))

    # keluaran a = f(z)
    ax.annotate("", xy=(10.9, 0), xytext=(bx0 + bw, 0),
                arrowprops=dict(arrowstyle="-|>", color="#1f4e79", lw=2))
    ax.text(11.0, 0.32, r"$a = f(z)$", ha="left", va="center", fontsize=14,
            color="#1f4e79")

    save(fig, MANS / "ch-02-regresi-neural-network/figures/fig-2-1-neuron.png")


# ---------------------------------------------------------------- fig-3-1
def fig_3_1():
    z = np.linspace(-9, 9, 400)
    s = 1 / (1 + np.exp(-z))
    fig, ax = plt.subplots(figsize=(7, 4.2))
    ax.plot(z, s, color="#1f4e79", lw=2.5)
    ax.axhline(0.5, color="#c0552b", ls="--", lw=1.4)
    ax.annotate("threshold 0,5", xy=(6.2, 0.52), fontsize=10, color="#c0552b")
    ax.set_xlabel("z (bobot × masukan)")
    ax.set_ylabel("σ(z)")
    ax.set_ylim(-0.05, 1.05)
    ax.grid(alpha=0.25)
    save(fig, MANS / "ch-03-klasifikasi-neural-network/figures/fig-3-1-sigmoid.png")


# ---------------------------------------------------------------- fig-3-2
def fig_3_2():
    cm = np.array([[970, 20], [8, 2]])
    fig, ax = plt.subplots(figsize=(6, 4.6))
    im = ax.imshow(cm, cmap="Blues")
    ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
    ax.set_xticklabels(["Prediksi: tidak", "Prediksi: hujan"])
    ax.set_yticklabels(["Aktual: tidak", "Aktual: hujan"])
    for i in range(2):
        for j in range(2):
            ax.text(j, i, f"{cm[i, j]}", ha="center", va="center",
                    fontsize=16, color="white" if cm[i, j] > 400 else "black")
    ax.set_xlabel("Prediksi")
    ax.set_ylabel("Aktual")
    save(fig, MANS / "ch-03-klasifikasi-neural-network/figures/fig-3-2-confusion-matrix.png")


# ---------------------------------------------------------------- fig-4-1 / 5-1
def _learning_curve():
    ep = np.arange(0, 101)
    train = 0.92 * np.exp(-ep / 22) + 0.06
    val = 0.80 * np.exp(-ep / 26) + 0.10
    val[ep > 58] = val[58] + (ep[ep > 58] - 58) * 0.0042
    rng = np.random.default_rng(3)
    train = train + rng.normal(0, 0.008, ep.size)
    val = val + rng.normal(0, 0.012, ep.size)
    return ep, train, val


def fig_4_1():
    ep, train, val = _learning_curve()
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    ax.plot(ep, train, label="Train", color="#1f4e79", lw=2)
    ax.plot(ep, val, label="Validasi", color="#c0552b", lw=2)
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")
    ax.set_ylim(0, 1.0)
    ax.legend()
    ax.grid(alpha=0.25)
    save(fig, MANS / "ch-04-backpropagation-optimasi/figures/fig-4-1-learning-curve.png")


def fig_5_1():
    ep, train, val = _learning_curve()
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    ax.plot(ep, train, label="Train", color="#1f4e79", lw=2)
    ax.plot(ep, val, label="Validasi", color="#c0552b", lw=2)
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")
    ax.set_ylim(0, 1.0)
    ax.legend()
    ax.grid(alpha=0.25)
    save(fig, MANS / "ch-05-overfitting-regularisasi-evaluasi/figures/fig-5-1-learning-curve.png")


# ---------------------------------------------------------------- fig-6-1
def fig_6_1():
    rng = np.random.default_rng(11)
    n_dry = 2700
    rain = rng.gamma(shape=1.35, scale=18, size=800)
    data = np.concatenate([np.zeros(n_dry), rain])
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    ax.hist(data, bins=70, range=(0, 400), color="#4a90e2", alpha=0.85)
    ax.set_xlabel("Curah hujan harian (mm)")
    ax.set_ylabel("Frekuensi (jumlah hari)")
    ax.grid(axis="y", alpha=0.25)
    save(fig, MANS / "ch-06-data-meteorologi/figures/fig-6-1-distribusi-hujan.png")


# ---------------------------------------------------------------- fig-7-1
def fig_7_1():
    fig, ax = plt.subplots(figsize=(10, 3.4))
    ax.axis("off")
    xs = np.arange(5)
    for i, x in enumerate(xs):
        s = 0.75
        box = plt.Rectangle((x - s / 2, -s / 2), s, s, fc="#dbe9f6",
                            ec="#1f4e79", lw=2)
        ax.add_patch(box)
        ax.text(x, 0, f"t={i+1}", ha="center", va="center", fontsize=11)
        # input x_t
        ax.annotate("", xy=(x, -0.95), xytext=(x, -0.75),
                    arrowprops=dict(arrowstyle="->", color="#555"))
        ax.text(x, -1.25, f"x({i+1})", ha="center", fontsize=11, color="#555")
    # arrows betwen cells and h state
    for i in range(4):
        ax.annotate("", xy=(xs[i + 1] - 0.75, 0), xytext=(xs[i] + 0.75, 0),
                    arrowprops=dict(arrowstyle="->", color="#c0552b", lw=1.8))
        ax.text(xs[i] + 0.5, 0.22, "h", fontsize=11, color="#c0552b")
    ax.set_xlim(-1.2, 4.6)
    ax.set_ylim(-1.7, 1.4)
    save(fig, MANS / "ch-07-time-series-lstm-gru/figures/fig-7-1-rnn-unrolled.png")


# ---------------------------------------------------------------- fig-8-1
def fig_8_1():
    csv = (MANS / "ch-08-studi-kasus-pasang-surut-kapuas/data/sample/"
           "cili_1y_hourly.csv")
    t = None
    if csv.exists():
        import pandas as pd
        df = pd.read_csv(csv, parse_dates=["time"])
        s = df["tinggi"].interpolate(limit=6).dropna().values
        wave = s[: min(len(s), 365 * 24)]
    else:
        # fallback sintetik
        jam = np.arange(365 * 24)
        wave = (0.5 * np.sin(2 * np.pi * jam / 12.42)
                + 0.3 * np.sin(2 * np.pi * jam / 24.84 + 0.6)
                + np.random.default_rng(1).normal(0, 0.04, jam.size))
    n = len(wave)
    fft = np.abs(np.fft.rfft(wave - wave.mean())) ** 2
    freqs = np.fft.rfftfreq(n, d=1.0)  # per jam
    periode = np.where(freqs > 0, 1.0 / freqs, np.inf)
    mask = (periode >= 8) & (periode <= 60)
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.plot(periode[mask], fft[mask], color="#1f4e79", lw=1.6)
    for pk, lab in [(12.42, "12,42 jam"), (24.84, "24,84 jam")]:
        ax.axvline(pk, color="#c0552b", ls="--", lw=1.2)
        ax.text(pk, ax.get_ylim()[1] * 0.92 if False else None, "", fontsize=0)
    ax.set_xscale("log")
    ax.set_xlabel("Periode (jam)")
    ax.set_ylabel("Daya (amplitudo²)")
    ax.set_xlim(8, 60)
    # redraw label after setting limits
    ymax = max(fft[mask]) * 0.95
    ax.annotate("12,42 jam", xy=(12.42, ymax * 0.85), ha="center",
                fontsize=10, color="#c0552b")
    ax.annotate("24,84 jam", xy=(24.84, ymax * 0.55), ha="center",
                fontsize=10, color="#c0552b")
    ax.grid(alpha=0.25)
    save(fig, MANS / "ch-08-studi-kasus-pasang-surut-kapuas/figures/fig-8-1-spektrum-pasang.png")


# ---------------------------------------------------------------- fig-9-1
def fig_9_1():
    rng = np.random.default_rng(5)
    recall = np.linspace(0.02, 0.97, 60)
    # precision menurun seiring recall naik (hujan lebat langka)
    precision = 0.95 - 0.55 * recall - 0.15 * recall ** 3
    precision = precision + rng.normal(0, 0.012, recall.size)
    precision = np.clip(precision, 0.05, 0.98)
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    ax.plot(recall, precision, color="#1f4e79", lw=2.4)
    ax.plot([0, 1], [0.46, 0.46], ls="--", color="#999", lw=1.2,
            label="baseline acak")
    ax.set_xlabel("Recall (= POD)")
    ax.set_ylabel("Precision (= 1 − FAR)")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1.05)
    ax.legend()
    ax.grid(alpha=0.25)
    save(fig, MANS / "ch-09-studi-kasus-curah-hujan-terbuka/figures/fig-9-1-precision-recall.png")


# ---------------------------------------------------------------- fig-9-2
def fig_9_2():
    ktg = ["Ringan\n(<20)", "Sedang\n(20–50)", "Lebat\n(>50)"]
    pod = [0.90, 0.45, 0.20]
    far = [0.15, 0.40, 0.55]
    csi = [0.78, 0.32, 0.15]
    x = np.arange(3)
    w = 0.26
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    ax.bar(x - w, pod, w, label="POD", color="#1f4e79")
    ax.bar(x, far, w, label="FAR", color="#c0552b")
    ax.bar(x + w, csi, w, label="CSI", color="#4a90e2")
    ax.set_xticks(x); ax.set_xticklabels(ktg)
    ax.set_ylabel("Nilai")
    ax.set_ylim(0, 1.05)
    ax.legend()
    ax.grid(axis="y", alpha=0.25)
    save(fig, MANS / "ch-09-studi-kasus-curah-hujan-terbuka/figures/fig-9-2-verifikasi-kategori.png")


# ---------------------------------------------------------------- fig-10-1
def fig_10_1():
    rng = np.random.default_rng(8)
    minggu = np.arange(1, 53)
    base = 0.11 + rng.normal(0, 0.008, 52)
    base[43:] += np.linspace(0, 0.03, 9)  # drift lambat mulai minggu 44
    mean = base.mean()
    std = base.std()
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.plot(minggu, base, color="#1f4e79", lw=1.6, marker="o", ms=3.5)
    ax.axhline(mean, color="#333", ls="--", lw=1.2, label="rata-rata (0,11)")
    ax.axhline(mean + 2 * std, color="#c0552b", ls="--", lw=1.2,
               label="batas +2σ")
    # tandai titik keluar batas (setelah drift)
    out = minggu[base > mean + 2 * std]
    ax.scatter(out, base[base > mean + 2 * std], s=46, facecolors="none",
               edgecolors="#c0552b", lw=1.8, zorder=5)
    ax.set_xlabel("Minggu")
    ax.set_ylabel("MAE (m)")
    ax.legend(loc="upper left")
    ax.grid(alpha=0.25)
    save(fig, MANS / "ch-10-operasional-arah-riset/figures/fig-10-1-control-chart.png")


def main():
    fig_2_1(); fig_3_1(); fig_3_2()
    fig_4_1(); fig_5_1(); fig_6_1(); fig_7_1()
    fig_8_1(); fig_9_1(); fig_9_2(); fig_10_1()
    print("Semua gambar diregenerasi tanpa judul.")


if __name__ == "__main__":
    main()