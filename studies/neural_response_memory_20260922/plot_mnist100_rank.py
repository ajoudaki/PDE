"""Plot the frozen MNIST100 primary RMS against the correction rank bound."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FuncFormatter
import numpy as np


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    summary = json.loads(args.summary.read_text())
    if (summary["protocol"], summary["training_count"], summary["width"], summary["digits"]) != (
            "mnist100", 100, 4096, [3, 8]):
        raise ValueError("input does not match the frozen MNIST100 experiment")
    primary = summary["primary_level"]
    if primary != .001:
        raise ValueError("expected the completed primary training-MSE .001 endpoint")
    rows = sorted((row for row in summary["comparisons"] if row["level"] == primary),
                  key=lambda row: row["order"])
    if [row["order"] for row in rows] != [1, 2, 3]:
        raise ValueError("expected exactly three primary order comparisons")
    if not all(row["numerical_gate_passed"] for row in rows):
        raise ValueError("all primary numerical gates must pass")
    ranks = np.array([summary["training_count"] * row["order"] for row in rows])
    values = np.array([row["rms_difference"] for row in rows])
    margins = np.array([row["observed_refinement_margin"] for row in rows])
    if not np.isfinite(values).all() or not np.isfinite(margins).all() or np.any(values <= margins):
        raise ValueError("invalid values or sensitivity bars for a logarithmic axis")
    args.output.mkdir(parents=True, exist_ok=True)
    targets = [args.output / ("rms_vs_rank." + extension) for extension in ("png", "pdf")]
    provenance_path = args.output / "rank_figure_provenance.json"
    if any(path.exists() for path in [*targets, provenance_path]):
        raise FileExistsError("supplementary figure outputs already exist")

    plt.rcParams.update({"font.size": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "pdf.fonttype": 42})
    fig, ax = plt.subplots(figsize=(7.1, 4.8))
    fig.subplots_adjust(left=.15, right=.96, bottom=.24, top=.80)
    fig.suptitle("100 training images · n=4096 · digits 3/8", y=.97, fontsize=13)
    ax.set_title("Each model at its own training-MSE 0.001 crossing", fontsize=10, pad=14)
    ax.plot(ranks, values, color="#777777", linewidth=1, linestyle="--", zorder=1)
    for rank, value, margin, row, color in zip(
            ranks, values, margins, rows, ("#0072B2", "#D55E00", "#009E73")):
        ax.errorbar(rank, value, yerr=margin, fmt="o", markersize=7,
                    color=color, ecolor=color, capsize=5, linewidth=1.6, zorder=3)
        ax.annotate(f"P{row['order']}\n{value:.6f}", (rank, value),
                    xytext=(0, 13), textcoords="offset points",
                    ha="center", va="bottom", fontsize=10, color=color)
    ax.set(xlabel="Correction rank bound (100 × P)",
           ylabel="Validation RMS difference from dense",
           yscale="log", xlim=(75, 325), xticks=[100, 200, 300],
           ylim=(float(min(values-margins)*.78), float(max(values+margins)*1.60)))
    ax.yaxis.set_major_locator(FixedLocator([.001, .002, .003, .005]))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value:g}"))
    ax.yaxis.set_minor_locator(FixedLocator([]))
    ax.grid(axis="y", which="major", color="#dddddd", linewidth=.7)
    fig.text(.5, .08, "Bars: observed refinement sensitivity (dense + closure changes).",
             ha="center", fontsize=9)
    fig.text(.5, .035, "Not confidence intervals or rigorous error bounds. Vertical axis is logarithmic.",
             ha="center", fontsize=9)
    for target in targets:
        fig.savefig(target, dpi=200, bbox_inches="tight")
    plt.close(fig)
    provenance = dict(
        source=str(Path(__file__).resolve()), source_sha256=sha256(__file__),
        input=str(args.summary.resolve()), input_sha256=sha256(args.summary),
        output_sha256={path.name: sha256(path) for path in targets},
        primary_training_mse=primary, rank_bounds=ranks.tolist(),
        validation_rms=values.tolist(), observed_refinement_sensitivity=margins.tolist(),
        matplotlib=matplotlib.__version__, command=sys.argv)
    provenance_path.write_text(json.dumps(provenance, indent=2) + "\n")
    print(json.dumps(provenance, indent=2))


if __name__ == "__main__":
    main()
