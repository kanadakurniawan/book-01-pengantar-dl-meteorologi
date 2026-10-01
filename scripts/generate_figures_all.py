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
from matplotlib.colors import LogNorm
from mpl_toolkits.mplot3d import proj3d
import matplotlib.patheffects as pe

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


# ---------------------------------------------------------------- fig-2-2
def fig_2_2():
    """Arsitektur MLP contoh: 1 masukan -> 8 ReLU -> 8 ReLU -> 1 keluaran."""
    fig, ax = plt.subplots(figsize=(11.5, 5.8))
    ax.axis("off")
    ax.set_xlim(0, 12.6)
    ax.set_ylim(-3.75, 3.35)

    xs = {"input": 1.6, "h1": 4.5, "h2": 7.5, "output": 10.6}
    n_h = 8
    r = 0.30
    ys_h1 = np.linspace(2.35, -2.35, n_h)
    ys_h2 = np.linspace(2.35, -2.35, n_h)

    def node(x, y, rr=r, fc="#dbe9f6", ec="#1f4e79", lw=2):
        circ = plt.Circle((x, y), rr, fc=fc, ec=ec, lw=lw)
        ax.add_patch(circ)

    def edge(x1, y1, x2, y2, alpha=0.4, color="#555", lw=1.6):
        ax.plot([x1, x2], [y1, y2], color=color, lw=lw, alpha=alpha,
                zorder=0)

    # lapisan masukan: satu neuron x (suhu kemarin)
    node(xs["input"], 0)
    ax.text(xs["input"] - 0.55, 0, r"$x$", ha="right", va="center",
            fontsize=20, color="#1f4e79")

    # lapisan tersembunyi 1 & 2: 8 neuron ReLU
    for y in ys_h1:
        node(xs["h1"], y)
    for y in ys_h2:
        node(xs["h2"], y)
    ax.text(xs["h1"], 2.9, r"$h_1$", ha="center", va="center", fontsize=18,
            color="#1f4e79")
    ax.text(xs["h2"], 2.9, r"$h_2$", ha="center", va="center", fontsize=18,
            color="#1f4e79")

    # lapisan keluaran: satu neuron a = y-hat (suhu besok)
    node(xs["output"], 0, fc="#f5ead6", ec="#c0552b", lw=2.2)
    ax.text(xs["output"] + 0.55, 0, r"$\hat{y}$", ha="left", va="center",
            fontsize=20, color="#c0552b")

    # sambungan penuh (dense)
    for y2 in ys_h1:
        edge(xs["input"], 0, xs["h1"], y2, alpha=0.65)
    for y1 in ys_h1:
        for y2 in ys_h2:
            edge(xs["h1"], y1, xs["h2"], y2, alpha=0.35, lw=1.5)
    for y1 in ys_h2:
        edge(xs["h2"], y1, xs["output"], 0, alpha=0.65)

    # label lapisan: dua baris di BAWAH tiap kolom (bebas dari node)
    labels = [
        (xs["input"], "Lapisan masukan", "suhu kemarin"),
        (xs["h1"], "Lapisan tersembunyi 1", "8 neuron · ReLU"),
        (xs["h2"], "Lapisan tersembunyi 2", "8 neuron · ReLU"),
        (xs["output"], "Lapisan keluaran", "suhu besok · tanpa aktivasi"),
    ]
    for x, nama, sub in labels:
        ax.text(x, -2.95, nama, ha="center", va="center", fontsize=13,
                color="#1f4e79")
        ax.text(x, -3.35, sub, ha="center", va="center", fontsize=11,
                color="#333")

    save(fig, MANS / "ch-02-regresi-neural-network/figures/fig-2-2-mlp-arsitektur.png")


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
    # Tabel 3.3: model selalu memprediksi "tidak hujan deras", rekaman Cilacap
    # 1960-2024 (5904 hari): TP=0, FP=0, FN=166, TN=5738.
    # LogNorm(vmin=1): sel 0 dirender paling terang; colorbar log supaya
    # intensitas warna bisa dibaca.
    cm = np.array([[5738, 0], [166, 0]])
    labels = [["TN", "FP"], ["FN", "TP"]]
    fig, ax = plt.subplots(figsize=(6.8, 4.6))
    im = ax.imshow(cm, cmap="Blues", norm=LogNorm(vmin=1))
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Prediksi:\nTidak Hujan Deras", "Prediksi:\nHujan Deras"])
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["Aktual:\nTidak Hujan Deras", "Aktual:\nHujan Deras"])
    for i in range(2):
        for j in range(2):
            ax.text(j, i, f"{cm[i, j]}\n({labels[i][j]})", ha="center", va="center",
                    fontsize=13, color="white" if cm[i, j] > 400 else "black")
    ax.set_xlabel("Prediksi")
    ax.set_ylabel("Aktual")
    cbar = fig.colorbar(im, ax=ax, shrink=0.85)
    cbar.set_label("jumlah hari")
    save(fig, MANS / "ch-03-klasifikasi-neural-network/figures/fig-3-2-confusion-matrix.png")


# ---------------------------------------------------------------- fig-3-3
def fig_3_3():
    # Kontras ROC dan precision-recall untuk kelas langka (proporsi 2,8%,
    # sesuai Tabel 3.3): ROC terlihat cukup baik, PR menyingkap precision
    # yang rendah.
    rng = np.random.default_rng(7)
    fpr = np.linspace(0.0, 1.0, 200)
    tpr = fpr ** 0.43
    tpr = tpr + rng.normal(0, 0.004, fpr.size)
    tpr = np.clip(tpr, 0.0, 1.0)
    tpr[0] = 0.0
    auc = np.sum((tpr[1:] + tpr[:-1]) / 2 * np.diff(fpr))
    prev = 0.028  # proporsi hujan deras (Tabel 3.3)
    prec = (tpr * prev) / (tpr * prev + fpr * (1 - prev) + 1e-12)
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.2))
    ax = axes[0]
    ax.plot(fpr, tpr, color="#1f4e79", lw=2.4, label=f"model (AUC ≈ {auc:.2f})")
    ax.plot([0, 1], [0, 1], ls="--", color="#999", lw=1.2, label="baseline acak")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate (recall)")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1.05)
    ax.legend(loc="lower right")
    ax.grid(alpha=0.25)
    ax = axes[1]
    ax.plot(tpr, prec, color="#1f4e79", lw=2.4, label="model")
    ax.plot([0, 1], [prev, prev], ls="--", color="#999", lw=1.2,
            label="baseline acak (2,8%)")
    ax.set_xlabel("Recall")
    ax.set_ylabel("Precision")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1.05)
    ax.legend(loc="upper right")
    ax.grid(alpha=0.25)
    save(fig, MANS / "ch-03-klasifikasi-neural-network/figures/fig-3-3-roc-pr.png")


# ---------------------------------------------------------------- fig-4-1 (gradien)
def fig_4_1_gradien():
    """Kurva loss 1-D: kemiringan (gradien) di satu titik dan satu langkah turun."""
    w = np.linspace(-0.2, 6.2, 400)
    L = 0.6 * (w - 3.0) ** 2 + 0.5
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    ax.plot(w, L, color="#1f4e79", lw=2.6)

    w0 = 4.8
    L0 = 0.6 * (w0 - 3.0) ** 2 + 0.5
    grad0 = 1.2 * (w0 - 3.0)             # dL/dw pada w0 (positif)

    # garis singgung (gradien) di titik w0
    wtan = np.array([w0 - 1.1, w0 + 1.1])
    Ltan = L0 + grad0 * (wtan - w0)
    ax.plot(wtan, Ltan, color="#c0552b", lw=1.6, ls="--")
    ax.scatter([w0], [L0], s=55, color="#c0552b", zorder=6)
    ax.text(w0 + 0.25, L0 + 0.05, "gradien", ha="left", va="bottom",
            fontsize=11.5, color="#c0552b",
            bbox=dict(fc="white", ec="none", alpha=0.7, pad=1.2))

    # satu langkah: w1 = w0 - eta * gradien (menuju minimum)
    eta = 0.6
    w1 = w0 - eta * grad0
    L1 = 0.6 * (w1 - 3.0) ** 2 + 0.5
    ax.annotate("", xy=(w1, L1), xytext=(w0, L0),
                arrowprops=dict(arrowstyle="-|>", color="#2e7d32", lw=3.0,
                                mutation_scale=28, shrinkA=6, shrinkB=6),
                zorder=5)
    ax.scatter([w1], [L1], s=55, color="#2e7d32", zorder=6)
    ax.text((w0 + w1) / 2 - 0.05, (L0 + L1) / 2 + 0.42, "langkah",
            ha="center", va="bottom", fontsize=11.5, color="#2e7d32",
            bbox=dict(fc="white", ec="none", alpha=0.7, pad=1.2))

    ax.axvline(3.0, color="#999", ls=":", lw=1.3)
    ax.text(3.0, 0.12, "minimum", ha="center", va="bottom", fontsize=11.5,
            color="#666")

    ax.set_xlim(-0.2, 6.2)
    ax.set_ylim(0, 6.2)
    ax.set_xlabel("bobot w")
    ax.set_ylabel("loss L(w)")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(alpha=0.2)
    save(fig, MANS / "ch-04-backpropagation-optimasi/figures/fig-4-1-gradien.png")


# ---------------------------------------------------------------- fig-4-2 (loss landscape)
def _loss_surface(x, y):
    """Permukaan loss sintetis: dua lembah dengan satu col (saddle) di antaranya."""
    return (
        -4.5 * np.exp(-(((x - 2.4) ** 2 + (y - 2.4) ** 2) / 1.1))
        - 2.5 * np.exp(-(((x + 2.0) ** 2 + (y + 2.0) ** 2) / 1.0))
        + 1.2 * np.exp(-(((x + 0.7) ** 2 + (y + 0.7) ** 2) / 1.2))
        + 3.0 * np.exp(-(((x - 0.64) ** 2 + (y + 2.04) ** 2) / 1.0))
        + 3.0 * np.exp(-(((x + 2.04) ** 2 + (y - 0.64) ** 2) / 1.0))
    )


def _grad_xy(p):
    h = 1e-4
    gx = (_loss_surface(p[0] + h, p[1]) - _loss_surface(p[0] - h, p[1])) / (2 * h)
    gy = (_loss_surface(p[0], p[1] + h) - _loss_surface(p[0], p[1] - h)) / (2 * h)
    return np.array([gx, gy])


def _proyeksi_ke_axes(ax, x, y, z):
    """Proyeksikan titik 3-D ke koordinat axes (fraksi 0-1) untuk label 2-D."""
    x2, y2, _ = proj3d.proj_transform(x, y, z, ax.get_proj())
    tampilan = ax.transData.transform((x2, y2))
    return ax.transAxes.inverted().transform(tampilan)


def fig_4_2_landscape():
    """Permukaan loss 3-D: minimum global, minimum lokal, saddle point, bidang bobot."""
    x = np.linspace(-5.5, 5.5, 150)
    y = np.linspace(-5.5, 5.5, 150)
    X, Y = np.meshgrid(x, y)
    Z = _loss_surface(X, Y)

    # dua minimum (turunkan dari dekat pusat lembah)
    gmin = np.array([2.2, 2.2])
    lmin = np.array([-1.9, -1.9])
    for _ in range(200):
        gmin -= 0.05 * _grad_xy(gmin)
        lmin -= 0.05 * _grad_xy(lmin)
    # saddle: titik tertinggi pada jalur lurus antara kedua minimum
    ts = np.linspace(0.0, 1.0, 600)
    px = lmin[0] + ts * (gmin[0] - lmin[0])
    py = lmin[1] + ts * (gmin[1] - lmin[1])
    vals = _loss_surface(px, py)
    sad = np.array([px[np.argmax(vals)], py[np.argmax(vals)]])

    fig = plt.figure(figsize=(9.0, 5.8))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, cmap="jet", rstride=2, cstride=2,
                    linewidth=0.12, edgecolor="#333333", alpha=0.96)
    # bidang bobot (referensi z = 0), seperti "bayangan" permukaan
    ax.plot_wireframe(X, Y, np.zeros_like(X), color="#5fb98a", lw=0.35,
                      rstride=12, cstride=12, alpha=0.5)

    zg = _loss_surface(*gmin)
    zl = _loss_surface(*lmin)
    zs = _loss_surface(*sad)

    ax.set_xlabel("bobot $w_1$", labelpad=10)
    ax.set_ylabel("bobot $w_2$", labelpad=10)
    ax.set_zlabel("loss", labelpad=8)
    # garis kisi bidang muncul dari tick; angka tetap ditampilkan
    for sumbu in (ax.xaxis, ax.yaxis, ax.zaxis):
        sumbu.pane.set_facecolor((1.0, 1.0, 1.0, 1.0))
        sumbu.pane.set_edgecolor("#c8c8c8")
        sumbu._axinfo["grid"].update(color="#d9d9d9", linewidth=0.7,
                                     linestyle="-")
    ax.grid(True)
    ax.view_init(elev=26, azim=-58)

    # label di margin (2-D) dengan garis penunjuk ke titik 3-D
    fig.canvas.draw()
    anotasi = [
        (gmin[0], gmin[1], zg, "minimum global", "#1b5e20", "●", 0.86, 1.03),
        (lmin[0], lmin[1], zl, "minimum lokal", "#8a3b1c", "●", 0.14, 1.03),
        (sad[0], sad[1], zs, "saddle point", "#2c3e50", "◆", 0.50, 1.08),
    ]
    for x0, y0, z0, teks, warna, bentuk, tx, ty in anotasi:
        titik = _proyeksi_ke_axes(ax, x0, y0, z0)
        ax.text2D(titik[0], titik[1], bentuk, transform=ax.transAxes,
                  color=warna, fontsize=14, ha="center", va="center",
                  zorder=30,
                  path_effects=[pe.withStroke(linewidth=2.4,
                                              foreground="white")])
        ax.annotate(teks, xy=titik, xycoords=ax.transAxes,
                    xytext=(tx, ty), textcoords=ax.transAxes,
                    color=warna, fontsize=10.5, ha="center", va="center",
                    bbox=dict(fc="white", ec="none", alpha=0.7, pad=1.2),
                    arrowprops=dict(arrowstyle="-", color=warna, lw=1.2,
                                    connectionstyle="arc3,rad=0.12"))
    save(fig, MANS / "ch-04-backpropagation-optimasi/figures/fig-4-2-landscape.png")


# ---------------------------------------------------------------- fig-4-3 / 5-1
def _learning_curve():
    ep = np.arange(0, 101)
    train = 0.92 * np.exp(-ep / 22) + 0.06
    val = 0.80 * np.exp(-ep / 26) + 0.10
    val[ep > 58] = val[58] + (ep[ep > 58] - 58) * 0.0042
    rng = np.random.default_rng(3)
    train = train + rng.normal(0, 0.008, ep.size)
    val = val + rng.normal(0, 0.012, ep.size)
    return ep, train, val


def fig_4_3():
    ep, train, val = _learning_curve()
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    ax.plot(ep, train, label="Train", color="#1f4e79", lw=2)
    ax.plot(ep, val, label="Validasi", color="#c0552b", lw=2)
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Loss")
    ax.set_ylim(0, 1.0)
    ax.legend()
    ax.grid(alpha=0.25)
    save(fig, MANS / "ch-04-backpropagation-optimasi/figures/fig-4-3-learning-curve.png")


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
    """Distribusi curah hujan harian dari observasi GHCN-Daily Cilacap.

    Sumber: NOAA GHCN-Daily, stasiun Cilacap (1960-2024).
    """
    csv = (MANS / "ch-09-studi-kasus-curah-hujan-terbuka" / "data" / "raw"
           / "ghcn_cilacap_daily.csv")
    if not csv.exists():
        raise FileNotFoundError(f"Data GHCN-Daily tidak ditemukan: {csv}")
    import pandas as pd
    df = pd.read_csv(csv, parse_dates=["tanggal"])
    data = df["prcp_mm"].dropna().to_numpy()
    data = data[data >= 0]
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
    fig_2_1(); fig_2_2(); fig_3_1(); fig_3_2(); fig_3_3()
    fig_4_1_gradien(); fig_4_2_landscape(); fig_4_3(); fig_5_1(); fig_6_1(); fig_7_1()
    fig_8_1(); fig_9_1(); fig_9_2(); fig_10_1()
    print("Semua gambar diregenerasi tanpa judul.")


if __name__ == "__main__":
    main()