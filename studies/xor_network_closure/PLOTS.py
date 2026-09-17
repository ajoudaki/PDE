#!/usr/bin/env python3
"""Static scientific figures from the frozen shifted-XOR analysis and raw outputs."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import shlex
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from ANALYSIS import load_manifest, matrix_rms, sha256, write_json


COLORS = {1: "#c45b32", 3: "#4177b6", 5: "#2b9361"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output
    analysis_path = output / "analysis.json"
    result = json.loads(analysis_path.read_text())
    _, manifest = load_manifest(output)
    inputs = np.load(output / "inputs.npz", allow_pickle=False)
    figure_dir = output / "figures"
    figure_dir.mkdir(exist_ok=False)
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
                         "axes.grid": True, "grid.alpha": .18, "savefig.dpi": 170})
    files, notes = [], []

    def save(fig, name):
        path = figure_dir / name
        fig.savefig(path, bbox_inches="tight")
        plt.close(fig)
        files.append(path)

    def raw(key):
        folder = Path(result["runs"][key]["folder"])
        return np.load(folder / "gram.npy", mmap_mode="r", allow_pickle=False), np.load(folder / "observations.npz", allow_pickle=False)

    def closure_key(order, q=2048, p=1024, step=.01):
        matches = ["closure/"+config["name"] for config in manifest["closure_runs"]
                   if config["order"] == order and config["initialization_nodes"] == q
                   and config["population_nodes"] == p and abs(float(config["step"])-step) < 1e-12]
        return matches[0] if len(matches) == 1 and matches[0] in result["runs"] and result["runs"][matches[0]].get("curves") else None

    curves = [(closure_key(order), f"N={order}, Q=2048 P=1024", COLORS[order], "-") for order in (1, 3, 5)]
    finest = closure_key(5, 4096, 2048)
    curves.append((finest, "N=5, Q=4096 P=2048", "#5b2c85", "--"))
    curves = [entry for entry in curves if entry[0]]
    times = np.asarray(result["times"])
    width = result["width_means"].get("8192")
    if width:
        fig = plt.figure(figsize=(13, 12))
        grid = fig.add_gridspec(3, 2, height_ratios=[1.2, 1, 1], hspace=.38)
        ax = fig.add_subplot(grid[0, :])
        ax.fill_between(times, width["loss_seed_min"], width["loss_seed_max"], color="black", alpha=.10,
                        label="8192 seed range")
        ax.plot(times, width["loss"], color="black", lw=2, label="Actual 8192, three-seed mean")
        if "2048" in result["width_means"]:
            ax.plot(times, result["width_means"]["2048"]["loss"], color=".55", lw=1.2, label="Actual 2048 mean")
        ax.plot(times, width["frozen_readout_mean_loss"], color="black", ls="--", label="Frozen hidden layers, trained readout")
        for key, label, color, style in curves:
            ax.plot(times, result["runs"][key]["curves"]["loss"], color=color, ls=style, label=label)
        ax.axhline(.01, color=".6", ls=":", lw=1)
        ax.set(yscale="log", ylabel="Unhalved training MSE", xlabel="Physical time", title="Loss and hidden-Gram agreement through T=100")
        ax.legend(ncol=3, fontsize=9)
        for layer in (1, 2):
            for column, panel in enumerate(("training", "circle")):
                ax = fig.add_subplot(grid[layer, column])
                baseline = width["frozen_gram_baseline"]["panels"][panel]["G"][f"layer{layer}"]["curve"]
                ax.plot(times, baseline, color="black", ls="--", label="Frozen actual mean Gram")
                for key, label, color, style in curves:
                    comparison = result["comparisons"].get(f"{key}:width8192")
                    if comparison:
                        values = comparison["comparison"]["panels"][panel]["G"][f"layer{layer}"]["curve"]
                        ax.plot(times, values, color=color, ls=style, label=label)
                ax.axhline(.05, color=".6", ls=":", lw=1)
                ax.set(xlabel="Physical time", ylabel="Matrix RMS error", title=f"Layer {layer}: {panel} panel vs actual 8192 mean")
                if layer == 1 and column == 0:
                    ax.legend(fontsize=8)
        status = result["verdict"]["interpretation"]
        fig.text(.5, .005, f"{status}. Curves retain all adverse outcomes; detailed controls are in analysis.json.", ha="center", fontsize=9)
        save(fig, "loss_and_gram_errors.png")

        reference_grams = sum(np.asarray(raw(key)[0]) for key in width["members"])/3
        reference_prediction = np.mean([raw(key)[1]["predictions"] for key in width["members"]], axis=0)
        if finest:
            closure_grams = raw(finest)[0]
            requested_times = [0, 10, 40, 100]
            indices = [int(np.flatnonzero(times == t)[0]) for t in requested_times]
            for layer in (0, 1):
                differences = closure_grams[indices, layer, 16:, 16:] - reference_grams[indices, layer, 16:, 16:]
                limit = max(float(np.max(np.abs(differences))), 1e-10)
                fig, axes = plt.subplots(3, 4, figsize=(15, 10), constrained_layout=True)
                for column, (index, time) in enumerate(zip(indices, requested_times)):
                    for row in (0, 1, 2):
                        if row == 0:
                            values = reference_grams[index, layer, 16:, 16:]
                        elif row == 1:
                            values = closure_grams[index, layer, 16:, 16:]
                        else:
                            values = differences[column]
                        image = axes[row, column].imshow(values, origin="lower", cmap="RdBu_r",
                            vmin=-limit if row == 2 else -1, vmax=limit if row == 2 else 1,
                            extent=[0, 360, 0, 360], interpolation="nearest")
                        axes[row, column].grid(False)
                        axes[row, column].set_xticks([0, 180, 360])
                        axes[row, column].set_yticks([0, 180, 360])
                        if row == 0:
                            axes[row, column].set_title(f"t={time}")
                        if row == 2:
                            axes[row, column].set_xlabel(f"Angle (degrees)\nRMS={matrix_rms(values):.4f}")
                        if column == 0:
                            axes[row, column].set_ylabel(["Actual 8192 mean", "N=5, Q=4096 P=2048", "Closure minus actual"][row]+"\nAngle (degrees)")
                        if column == 3:
                            fig.colorbar(image, ax=axes[row, :], shrink=.85, pad=.02)
                fig.suptitle(f"Layer {layer+1} hidden Gram on the passive circle", fontsize=15)
                save(fig, f"layer{layer+1}_gram_evolution.png")
        else:
            notes.append("Finest N5 missing; matrix evolution figures unavailable.")
    else:
        notes.append("Incomplete width8192 mean; overview and actual-reference figures unavailable.")

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))
    labels = inputs["labels"]
    angles = np.linspace(0, 2*np.pi, 361)
    axes[0].plot(np.cos(angles), np.sin(angles), color=".8", lw=1)
    for target, color in ((1, "#aa4934"), (-1, "#3765a1")):
        points = inputs["inputs"][labels == target]
        axes[0].scatter(points[:, 0], points[:, 1], color=color, s=45, label=f"label {target:+d}", zorder=3)
    axes[0].set(xlim=(-1.15, 1.15), ylim=(-1.15, 1.15), aspect="equal", xlabel="u₁", ylabel="u₂",
                title="Frozen 16-point training geometry")
    axes[0].legend()
    circle = inputs["panel"][16:]
    degrees = np.mod(np.degrees(np.arctan2(circle[:, 1], circle[:, 0])), 360)
    order = np.argsort(degrees)
    if width:
        axes[1].plot(degrees[order], reference_prediction[-1, 16:][order], color="black", lw=2, label="Actual 8192 mean")
    for key, label, color, style in curves:
        predictions = raw(key)[1]["predictions"][-1, 16:]
        axes[1].plot(degrees[order], predictions[order], color=color, ls=style, label=label)
    training_angles = np.mod(np.degrees(np.arctan2(inputs["inputs"][:, 1], inputs["inputs"][:, 0])), 360)
    axes[1].scatter(training_angles, labels, color=np.where(labels > 0, "#aa4934", "#3765a1"), s=35, zorder=3, label="Training targets")
    axes[1].axhline(0, color=".6", lw=.7)
    axes[1].set(xlim=(0, 360), xlabel="Input angle (degrees)", ylabel="Prediction", title="Predictions at T=100")
    axes[1].legend(fontsize=8)
    fig.tight_layout()
    save(fig, "geometry_and_final_predictions.png")
    record = {"command": shlex.join(getattr(sys, "orig_argv", [sys.executable, *sys.argv])),
              "argv": getattr(sys, "orig_argv", [sys.executable, *sys.argv]), "analysis_sha256": sha256(analysis_path),
              "plot_source_sha256": sha256(__file__), "analysis_source_sha256": sha256(Path(__file__).with_name("ANALYSIS.py")),
              "inputs_sha256": sha256(output / "inputs.npz"), "outputs": {str(path.relative_to(output)): sha256(path) for path in files},
              "notes": notes, "display_convention": "Main N1/N3/N5 curves share Q2048/P1024 and h=.01; finer N5 Q4096/P2048 is separate. Matrix evolution uses finer N5 h=.01."}
    write_json(output / "plots_manifest.json", record)
    print(json.dumps({"figures": [str(path) for path in files], "notes": notes}))


if __name__ == "__main__":
    main()
