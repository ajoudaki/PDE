"""Plot saved comparison arrays; never reruns a model or training solver."""
import argparse
import json
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("run", type=Path)
    args = parser.parse_args()
    run = args.run
    dense = np.load(run / "dense/final.npz")
    parent = np.load(run / "parent_P1/final.npz")
    degrees = np.rad2deg(dense["theta"])
    fig, (ax, error_ax) = plt.subplots(2, 1, figsize=(10, 7.3), sharex=True,
                                      gridspec_kw={"height_ratios": [2, 1]})
    ax.plot(degrees, dense["circle"], color="#202733", lw=2.3, label="Dense network")
    ax.plot(degrees, parent["circle"], color="#5374b8", lw=1.8, ls="--",
            label="Population closure, P=1")
    error_ax.plot(degrees, parent["circle"]-dense["circle"], color="#5374b8", lw=1.8,
                  label="Population − dense")
    palette = ["#c85432", "#30916b", "#9952ae", "#b68b21"]
    folders = [f for f in sorted(run.glob("scalar_K*"))
               if "refined" not in f.name and "_J" not in f.name
               and (f / "final.npz").exists()]
    for folder, color in zip(folders, palette):
        record = json.loads((folder / "result.json").read_text())
        if "fit_time" not in record:
            continue
        values = np.load(folder / "final.npz")["circle"]
        label = f"Scalar Fourier, K={record['K']}, J={record['J']}"
        ax.plot(degrees, values, color=color, lw=1.8, label=label)
        error_ax.plot(degrees, values-dense["circle"], color=color, lw=1.8,
                      label=f"Scalar K={record['K']} − dense")
    ax.scatter([10, 125], [1, -1], marker="o", s=56, facecolors="white",
               edgecolors="#202733", linewidths=1.7, zorder=6, label="Training data")
    ax.set_title("Whole-circle predictions after fitting two training inputs", loc="left", pad=15)
    ax.set_ylabel("Network output")
    error_ax.set_ylabel("Difference from dense")
    error_ax.set_xlabel("Input angle (degrees)")
    ax.legend(loc="upper right", fontsize=9, framealpha=.93)
    error_ax.axhline(0, color="#888888", lw=.8)
    error_ax.set_xticks(np.arange(0, 361, 45))
    error_ax.set_xlim(0, 360)
    for panel in (ax, error_ax):
        panel.spines[["top", "right"]].set_visible(False)
        panel.grid(alpha=.16)
    fig.text(.09, .012,
             "Three tanh layers · width 16 · internal training RMS 0.0316; scalar Fourier predictor training RMS 0.169",
             fontsize=9, color="#505864")
    fig.tight_layout(rect=(0, .03, 1, 1))
    fig.savefig(run / "circle_comparison.png", dpi=180)
    fig.savefig(run / "circle_comparison.pdf")


if __name__ == "__main__":
    main()
