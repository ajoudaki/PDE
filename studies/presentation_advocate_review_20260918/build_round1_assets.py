"""Build the evidence figures used by the first presentation round.

This script only redraws retained arrays and reported metrics.  It does not
train models, select new checkpoints, or compute a new scientific result.
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/presentation_advocate_review_20260918/round1"
OUT.mkdir(parents=True, exist_ok=True)

BG = "#F6F3EC"
INK = "#15212A"
MUTED = "#66737B"
BLUE = "#2878D0"
GOLD = "#E0A928"
CORAL = "#E76F51"
TEAL = "#168F8A"

mpl.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 16,
        "axes.facecolor": BG,
        "figure.facecolor": BG,
        "savefig.facecolor": BG,
        "axes.edgecolor": INK,
        "axes.labelcolor": INK,
        "text.color": INK,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
    }
)


def save(fig, name):
    fig.savefig(OUT / name, dpi=220, bbox_inches="tight", pad_inches=0.05)
    plt.close(fig)


def circle_panel():
    path = ROOT / (
        "data/generated/closure_circle_spectral_mechanism/"
        "network_comparison_multi_001/analysis_final/curves.npz"
    )
    z = np.load(path)
    theta = 2 * np.pi * np.arange(720) / 720
    curves = {
        "network": z["quad_d30_n4096__common_T100_mean"],
        "p=1": z["quad_d30_N1_main__T100"],
        "p=3": z["quad_d30_N3_main__T100"],
        "p=5": z["quad_d30_N5_main__T100"],
    }
    base, scale = 2.25, 0.56
    fig = plt.figure(figsize=(8.4, 8.0))
    ax = fig.add_subplot(111, projection="polar")
    ax.set_theta_zero_location("E")
    ax.set_theta_direction(1)
    ax.set_ylim(0.95, 3.25)
    ax.set_xticks(np.deg2rad([0, 45, 90, 135, 180, 225, 270, 315]))
    ax.set_xticklabels([])
    ax.set_yticks([1.25, 2.25, 3.25])
    ax.set_yticklabels([])
    ax.grid(color="#CBD1D2", linewidth=0.8, alpha=0.75)
    ax.spines["polar"].set_visible(False)
    ax.plot(theta, np.full_like(theta, base), color="#9BA5AA", lw=1.2, ls=(0, (2, 4)))
    ax.plot(theta, base + scale * curves["p=1"], color=BLUE, lw=2.6, label="p = 1", zorder=3)
    ax.plot(theta, base + scale * curves["p=3"], color=GOLD, lw=2.6, label="p = 3", zorder=4)
    ax.plot(theta, base + scale * curves["p=5"], color=CORAL, lw=2.8, label="p = 5", zorder=5)
    ax.plot(theta, base + scale * curves["network"], color=INK, lw=3.4, label="network", zorder=6)
    train_deg = np.array([0, 30, 60, 90])
    labels = np.array([-1, 1, -1, 1])
    ax.scatter(
        np.deg2rad(train_deg),
        base + scale * labels,
        s=90,
        facecolor=BG,
        edgecolor=INK,
        linewidth=2.1,
        zorder=10,
    )
    ax.legend(
        loc="lower center",
        bbox_to_anchor=(0.5, -0.10),
        ncol=4,
        frameon=False,
        fontsize=15,
        handlelength=2.0,
    )
    save(fig, "circle_quad30_clean.png")


def order_heatmap():
    cases = ["3 pts · 20°", "3 pts · 40°", "3 pts · 60°", "4 pts · 15°", "4 pts · 30°", "4 pts · 45°"]
    values = np.array(
        [
            [23.68, 10.95, 7.18],
            [33.29, 3.97, 4.69],
            [13.67, 4.81, 7.26],
            [46.46, 32.12, 21.79],
            [7.46, 3.89, 2.08],
            [9.04, 3.02, 3.14],
        ]
    )
    fig, ax = plt.subplots(figsize=(9.6, 6.1))
    cmap = mpl.colors.LinearSegmentedColormap.from_list("error", ["#DDF2EC", "#F4D8B4", "#E88A72"])
    im = ax.imshow(values, cmap=cmap, vmin=0, vmax=48, aspect="auto")
    ax.set_xticks(range(3), ["p = 1", "p = 3", "p = 5"], fontsize=18, color=INK)
    ax.set_yticks(range(6), cases, fontsize=17, color=INK)
    ax.tick_params(length=0, pad=12)
    for i in range(values.shape[0]):
        for j in range(values.shape[1]):
            color = "white" if values[i, j] > 25 else INK
            ax.text(j, i, f"{values[i,j]:.1f}%", ha="center", va="center", color=color, fontsize=18, weight="semibold")
    # The only geometry with passing closure controls at both transitions.
    rect = mpl.patches.Rectangle((-0.49, 3.51), 2.98, 0.98, fill=False, edgecolor=TEAL, linewidth=4)
    ax.add_patch(rect)
    for s in ax.spines.values():
        s.set_visible(False)
    cbar = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.10)
    cbar.set_label("relative RMS to network", fontsize=14, color=MUTED)
    cbar.ax.tick_params(labelsize=12, length=0)
    save(fig, "circle_order_heatmap.png")


def mnist_scatter():
    path = ROOT / "data/generated/first_order_dimension_mnist/matched_loss4096_001/sample_predictions.npz"
    z = np.load(path)
    x = z["network_mean"]
    y = z["closure_matched"].mean(axis=0)
    labels = z["labels"]
    rms = float(np.sqrt(np.mean((y - x) ** 2)))
    fig, ax = plt.subplots(figsize=(8.2, 7.3))
    lim = (-1.28, 1.22)
    ax.plot(lim, lim, color=INK, lw=1.5, ls=(0, (4, 4)), alpha=0.75)
    ax.scatter(x[labels < 0], y[labels < 0], s=18, color=BLUE, alpha=0.38, edgecolors="none", label="5")
    ax.scatter(x[labels > 0], y[labels > 0], s=18, color=CORAL, alpha=0.38, edgecolors="none", label="3")
    ax.set_xlim(lim)
    ax.set_ylim(lim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("network prediction", fontsize=17)
    ax.set_ylabel("p = 1 prediction", fontsize=17)
    ax.grid(color="#CBD1D2", alpha=0.45, linewidth=0.8)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=13)
    ax.text(
        0.04,
        0.94,
        f"1,000 images  ·  RMS = {rms:.3f}",
        transform=ax.transAxes,
        fontsize=17,
        color=INK,
        ha="left",
        va="top",
        bbox=dict(boxstyle="round,pad=.35", facecolor=BG, edgecolor="none", alpha=0.9),
    )
    ax.legend(loc="lower right", frameon=False, ncol=2, fontsize=14, title="digit", title_fontsize=12)
    save(fig, "mnist_matched_scatter_clean.png")


def compute_tradeoff():
    labels = ["time", "peak memory"]
    network = np.ones(2)
    closure = np.array([0.2523, 0.198037])  # conservative same-GPU time ratio, measured allocation ratio
    fig, ax = plt.subplots(figsize=(9.3, 5.0))
    y = np.arange(2)
    h = 0.26
    ax.barh(y + h / 1.7, network, height=h, color="#CBD1D2", label="PCA network")
    ax.barh(y - h / 1.7, closure, height=h, color=TEAL, label="PCA p = 1")
    ax.set_yticks(y, labels, fontsize=19, color=INK)
    ax.set_xlim(0, 1.08)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0], ["0", "25", "50", "75", "100%"], fontsize=13)
    ax.invert_yaxis()
    ax.grid(axis="x", color="#CBD1D2", alpha=0.65, linewidth=0.8)
    ax.spines[:].set_visible(False)
    ax.tick_params(axis="y", length=0, pad=12)
    ax.text(closure[0] + 0.03, y[0] - h / 1.7, "3.75–3.96× faster", va="center", fontsize=17, color=TEAL, weight="bold")
    ax.text(closure[1] + 0.03, y[1] - h / 1.7, "80.2% less", va="center", fontsize=17, color=TEAL, weight="bold")
    ax.text(1.0, y[0] + h / 1.7, "100%", ha="right", va="center", fontsize=13, color=MUTED)
    ax.text(1.0, y[1] + h / 1.7, "100%", ha="right", va="center", fontsize=13, color=MUTED)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.26), ncol=2, frameon=False, fontsize=14)
    save(fig, "pca_compute_tradeoff.png")


if __name__ == "__main__":
    circle_panel()
    order_heatmap()
    mnist_scatter()
    compute_tradeoff()
