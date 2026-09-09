#!/usr/bin/env python3
"""Build the compact evidence figure from sealed processed CSV/JSON outputs."""

from __future__ import annotations

import json
import os
from pathlib import Path
import tempfile

os.environ.setdefault(
    "MPLCONFIGDIR",
    str(Path(tempfile.gettempdir()) / "activation-linearity-matplotlib"),
)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent
PROCESSED = ROOT / "results" / "processed"
if not PROCESSED.is_dir():
    PROCESSED = ROOT / "evidence" / "processed"
FIGURES = ROOT / "figures"


def pct(value: float) -> float:
    return 100.0 * value


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    summary = json.loads((PROCESSED / "summary.json").read_text())
    curves = pd.read_csv(PROCESSED / "figure_time_curves.csv")
    bounds = summary["bootstrap"]["bounds"]

    plt.rcParams.update(
        {
            "font.size": 9,
            "axes.titlesize": 10.5,
            "axes.labelsize": 9.5,
            "legend.fontsize": 8,
            "figure.dpi": 160,
            "savefig.dpi": 220,
            "axes.spines.top": False,
            "axes.spines.right": False,
        }
    )
    fig, axes = plt.subplots(
        1,
        3,
        figsize=(12.4, 3.85),
        gridspec_kw={"width_ratios": [1.0, 1.08, 1.45]},
    )

    # A. Activation dose response.
    ax = axes[0]
    cases = ["C1", "C2", "C4"]
    labels = [r"$c=1$", r"$c=2$", r"$c=4$"]
    dense_sep = [
        pct(
            summary["activation_evidence"][case]["metrics"]["gram"][
                "dense_Cc_vs_C0_separation"
            ]["normalized"]
        )
        for case in cases
    ]
    matched = [
        pct(
            summary["activation_evidence"][case]["metrics"]["gram"][
                "matched_pde_error"
            ]["normalized"]
        )
        for case in cases
    ]
    x = np.arange(len(cases))
    width = 0.36
    bars_a = ax.bar(
        x - width / 2,
        dense_sep,
        width,
        color="#c44e52",
        label="Dense vs identity",
    )
    bars_b = ax.bar(
        x + width / 2,
        matched,
        width,
        color="#4c72b0",
        label="Matched PDE error",
    )
    ax.axhline(5, color="#555555", lw=1.0, ls="--", label="5% tolerance")
    ax.set_xticks(x, labels)
    ax.set_ylabel("Normalized global Gram distance (%)")
    ax.set_title("A. Activation dose response")
    ax.set_ylim(0, 51)
    ax.legend(loc="upper left", frameon=False)
    for bars in (bars_a, bars_b):
        for bar in bars:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 1.0,
                f"{bar.get_height():.1f}",
                ha="center",
                va="bottom",
                fontsize=8,
            )

    # B. Confirmatory hierarchy at c=2.
    ax = axes[1]
    point = [
        pct(bounds["dense_separation_C2_C0_gram"]["observed"]),
        pct(bounds["dense_separation_C2_L2_gram"]["observed"]),
        pct(bounds["matched_C2_gram"]["observed"]),
    ]
    lower = [
        pct(bounds["dense_separation_C2_C0_gram"]["lcb"]),
        pct(bounds["dense_separation_C2_L2_gram"]["lcb"]),
        0.0,
    ]
    upper = [
        pct(bounds["dense_separation_C2_C0_gram"]["ucb"]),
        pct(bounds["dense_separation_C2_L2_gram"]["ucb"]),
        pct(bounds["matched_C2_gram"]["ucb"]),
    ]
    yerr = np.vstack(
        [
            np.maximum(0.0, np.asarray(point) - np.asarray(lower)),
            np.maximum(0.0, np.asarray(upper) - np.asarray(point)),
        ]
    )
    labels_b = ["Identity\nnull", "Gain-matched\nlinear null", "Matched\nnonlinear PDE"]
    colors = ["#c44e52", "#dd8452", "#4c72b0"]
    bars = ax.bar(
        np.arange(3),
        point,
        color=colors,
        yerr=yerr,
        capsize=3,
        error_kw={"lw": 1.0},
    )
    ax.axhline(5, color="#555555", lw=1.0, ls="--")
    ax.set_xticks(np.arange(3), labels_b)
    ax.set_title(r"B. What survives at $c=2$")
    ax.set_ylim(0, 42)
    ax.set_ylabel("Normalized global Gram distance (%)")
    for bar, value in zip(bars, point):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 1.0,
            f"{value:.2f}",
            ha="center",
            va="bottom",
            fontsize=8,
        )
    ax.text(
        0.98,
        0.96,
        "One-sided 95% bounds",
        transform=ax.transAxes,
        ha="right",
        va="top",
        fontsize=7.5,
        color="#555555",
    )

    # C. Representative global trajectory at the output depth.
    ax = axes[2]
    palette = {"C0": "#c44e52", "C2": "#4c72b0", "L2": "#dd8452"}
    case_labels = {
        "C0": "identity",
        "C2": r"$\tanh(2z)/2$",
        "L2": r"$0.5101z$",
    }
    for case in ["C0", "C2", "L2"]:
        for source in ["PDE", "dense"]:
            subset = curves[
                (curves["case_id"] == case) & (curves["source"] == source)
            ]
            style = "-" if source == "PDE" else "--"
            width_line = 2.0 if source == "PDE" else 1.35
            alpha = 1.0 if source == "PDE" else 0.85
            ax.plot(
                subset["time"],
                subset["max_depth_gram_increment_fro"],
                ls=style,
                lw=width_line,
                alpha=alpha,
                color=palette[case],
                label=f"{case_labels[case]} — {source}",
            )
    ax.set_xlim(0, 3.0)
    ax.set_xlabel("Training time")
    ax.set_ylabel(r"$\|\Delta G(s=1,t)\|_F$")
    ax.set_title("C. Dense curves and fixed PDE")
    ax.legend(loc="lower right", frameon=False, ncol=1)

    fig.suptitle(
        "Activation-linearity falsification: identity is wrong; gain matching is much harder",
        fontsize=12,
        y=1.02,
    )
    fig.tight_layout()
    out = FIGURES / "activation_linearity_smoking_gun.png"
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
