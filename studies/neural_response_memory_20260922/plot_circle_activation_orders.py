#!/usr/bin/env python3
"""Plot frozen circle RMS comparisons; no training or analysis reselection."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import shlex
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import NullFormatter


ACTIVATIONS = (("tanh", "tanh", "#2563eb", "o"),
               ("gelu", "GELU", "#d97706", "s"),
               ("sigmoid", "sigmoid", "#8b5cf6", "^"))
TASKS = (("two_outliers_alternating", "Two outliers"),
         ("quadrant_alternating", "Quadrant"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def collect(tanh_path, activation_path):
    sources = {"tanh": tanh_path, "gelu": activation_path, "sigmoid": activation_path}
    metrics = {path: json.loads(path.read_text()) for path in set(sources.values())}
    rows = []
    for milestone in (.1, .001):
        for task, _ in TASKS:
            for activation, *_ in ACTIVATIONS:
                path = sources[activation]
                data = metrics[path]
                require(data["width"] == 4096, "Unexpected width")
                case = task if activation == "tanh" else f"{activation}__{task}"
                for p in (1, 2, 3):
                    found = [r for r in data["comparisons"]
                             if (r["case"], r["P"], r["milestone"]) == (case, p, milestone)]
                    missing = activation == "sigmoid" and task == "quadrant_alternating" and milestone == .001
                    require(len(found) == (0 if missing else 1), f"Unexpected row count: {case}, {p}, {milestone}")
                    row = dict(task=task, activation=activation, P=p, training_mse=milestone,
                               rms_8192="", available=bool(found), numerical_pass="",
                               reason="No shared MSE 0.001 crossing: dense and P1 did not reach it."
                               if missing else "", metrics_file=str(path), dense_run="", closure_run="")
                    if found:
                        source = found[0]
                        value = source["rms_8192"]
                        require(math.isfinite(value) and value > 0, "Invalid RMS")
                        require(source["numerical_pass"] and not source["failed_gates"], "Numerical gate failure")
                        require(source["dense_run"] == data["selected"][case]["dense"]["finest"]
                                and source["closure_run"] == data["selected"][case][f"P{p}"]["finest"],
                                "Comparison is not the frozen selected pair")
                        row.update(rms_8192=value, numerical_pass=True,
                                   dense_run=source["dense_run"], closure_run=source["closure_run"])
                    rows.append(row)
    return rows


def render(rows, milestone, output):
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "pdf.fonttype": 42, "axes.labelcolor": "#253247",
                         "text.color": "#253247", "axes.spines.top": False,
                         "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(11.8, 5.6), sharey=True)
    fig.subplots_adjust(left=.085, right=.975, top=.71, bottom=.21, wspace=.15)
    fig.text(.085, .93, "Circle RMS error vs closure order", fontsize=20, weight="bold")
    stage = "Intermediate comparison" if milestone == .1 else "Fitted comparison"
    fig.text(.085, .875, f"{stage} · each model at its own training MSE = {milestone:g} crossing",
             fontsize=11, color="#526071")
    handles = [Line2D([], [], color=color, marker=marker, linewidth=2.4, markersize=7, label=label)
               for _, label, color, marker in ACTIVATIONS]
    fig.legend(handles=handles, loc="upper left", bbox_to_anchor=(.076, .843), ncol=3,
               frameon=False, columnspacing=2.4)
    for ax, (task, title) in zip(axes, TASKS):
        for activation, _, color, marker in ACTIVATIONS:
            points = [r for r in rows if r["training_mse"] == milestone
                      and r["task"] == task and r["activation"] == activation and r["available"]]
            if points:
                ax.plot([r["P"] for r in points], [r["rms_8192"] for r in points],
                        color=color, marker=marker, markersize=7, linewidth=2.4)
        ax.set(yscale="log", ylim=(.01, 10), xlim=(.86, 3.14), xticks=(1, 2, 3),
               xlabel="Closure order P", title=f"{title} · alternating labels")
        ax.set_yticks((.01, .1, 1, 10), labels=("0.01", "0.1", "1", "10"))
        ax.yaxis.set_minor_formatter(NullFormatter())
        ax.grid(axis="y", which="major", color="#d9e0e8", linewidth=.8)
        ax.grid(axis="y", which="minor", color="#edf0f5", linewidth=.5)
        ax.set_axisbelow(True)
        if milestone == .001 and task == "quadrant_alternating":
            ax.text(.96, .95, "Sigmoid unavailable\nat MSE 0.001", transform=ax.transAxes,
                    ha="right", va="top", fontsize=9, color="#8b5cf6",
                    bbox=dict(facecolor="white", edgecolor="none", alpha=.9, pad=3))
    axes[0].set_ylabel("Circle RMS error vs dense (log scale)")
    fig.text(.085, .102, "3 hidden layers · width 4096 · 8192 circle points · lower is better", fontsize=10)
    fig.text(.085, .059, "Each closure is compared with its activation’s dense reference; one shared initialization.",
             fontsize=9, color="#526071")
    name = "rms_vs_P_common_mse_0p1" if milestone == .1 else "rms_vs_P_fitted_mse_0p001"
    for extension in ("png", "pdf"):
        fig.savefig(output / f"{name}.{extension}", dpi=180, facecolor="white")
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tanh-metrics", type=Path, required=True)
    parser.add_argument("--activation-metrics", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    inputs = [args.tanh_metrics.resolve(), args.activation_metrics.resolve()]
    rows = collect(*inputs)
    args.out.mkdir(parents=True, exist_ok=False)
    with (args.out / "rms_values.csv").open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    for milestone in (.1, .001):
        render(rows, milestone, args.out)
    manifest = dict(
        scope="Presentation only; frozen RMS, selection and numerical gates preserved. No new experiments.",
        metric="RMS difference from same-activation dense predictor on 8192 circle points at matched own-loss crossings",
        width=4096, hidden_layers=3, shared_seed=20260920,
        common_milestone=.1, fitted_milestone=.001,
        available_rows=sum(r["available"] for r in rows), unavailable_rows=sum(not r["available"] for r in rows),
        missing="Sigmoid quadrant: dense and P1 did not reach MSE .001 within the recorded budget.",
        inputs_sha256={str(path): sha(path) for path in inputs},
        source_sha256={str(Path(__file__).resolve()): sha(Path(__file__))},
        command=shlex.join([sys.executable, *sys.argv]), cwd=str(Path.cwd()),
        environment=dict(python=platform.python_version(), matplotlib=matplotlib.__version__,
                         **{key: os.environ.get(key) for key in
                            ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "MPLCONFIGDIR")}),
        output_sha256={path.name: sha(path) for path in sorted(args.out.iterdir())},
        exit_status=0)
    (args.out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(dict(output=str(args.out.resolve()), available_rows=manifest["available_rows"],
                          unavailable_rows=manifest["unavailable_rows"])))


if __name__ == "__main__":
    main()
