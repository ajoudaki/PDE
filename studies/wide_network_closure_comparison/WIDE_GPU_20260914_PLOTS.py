"""Scientific figures from the completed, frozen wide-network comparison."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np


def main(base):
    networks, closures = {}, {}
    for category, target in [("network", networks), ("closure", closures)]:
        for path in sorted((base/category).glob("*/record.json")):
            record = json.loads(path.read_text())
            if record["status"] == "complete":
                with np.load(path.with_name("observations.npz")) as z:
                    target[path.parent.name] = (record, {key: z[key] for key in z.files})
    widths = sorted({r["width"] for r, a in networks.values() if r["kind"] == "primary"})
    large = widths[-1]
    colors = {1: "#d58c00", 3: "#009e73", 5: "#cc5078", "refined": "#825ac3"}
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "axes.grid": True, "grid.alpha": .17, "savefig.dpi": 180})
    output = base/"figures"
    output.mkdir(exist_ok=True)
    metadata = {"source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "matplotlib": matplotlib.__version__, "numpy": np.__version__,
                "command": sys.argv,
                "observation_sha256": {str(path): hashlib.sha256(path.read_bytes()).hexdigest()
                    for family in ["network", "closure"]
                    for path in sorted((base/family).glob("*/observations.npz"))},
                "figures": []}

    def sample(case, width):
        rows = [a for r, a in networks.values() if r["kind"] == "primary"
                and r["case"] == case and r["width"] == width]
        if len(rows) != 3:
            raise ValueError("Expected all three declared seeds before plotting")
        return {key: np.stack([a[key] for a in rows]) for key in rows[0]}

    def trace(ax, case, key, layer=None):
        for width in widths:
            a = sample(case, width)
            times = a["times"][0]
            values = a[key] if layer is None else a[key][:, :, layer]
            mean = values.mean(axis=0)
            if width == large:
                ax.fill_between(times, values.min(axis=0), values.max(axis=0),
                                color="#214b80", alpha=.14, linewidth=0)
                ax.plot(times, mean, color="#214b80", lw=2.4,
                        label=f"Network {width:,}: mean + seed range")
            else:
                ax.plot(times, mean, color="#8797ab", lw=1.5, ls="--",
                        label=f"Network {width:,}: mean")
        for order in [1, 3, 5, "refined"]:
            name = f"{case}_N3_refined" if order == "refined" else f"{case}_N{order}"
            if name not in closures:
                continue
            _, a = closures[name]
            values = a[key] if layer is None else a[key][:, layer]
            ax.plot(a["times"], values, color=colors[order], lw=1.6,
                    ls=":" if order == "refined" else "-",
                    label="Closure N=3, refined quadrature" if order == "refined" else f"Closure N={order}")

    def timeaxis(ax):
        ax.set_xscale("symlog", linthresh=.5)
        ax.set_xlim(0, 40)
        ax.set_xticks([0, .5, 1, 5, 10, 40])
        ax.xaxis.set_major_formatter(ScalarFormatter())
        ax.set_xlabel("Physical training time t")

    def save(fig, name):
        for extension in ["png", "pdf"]:
            path = output/(name+"."+extension)
            fig.savefig(path, bbox_inches="tight")
            metadata["figures"].append({"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        plt.close(fig)

    fig, axes = plt.subplots(2, 3, figsize=(14, 7.4))
    for row, (case, title) in enumerate([("axis", "Two-axis working data"), ("arcs", "Resolved arc working data")]):
        for col, (key, layer, label) in enumerate([
            ("loss", None, "Weighted squared loss"),
            ("raw_rms", 0, "Hidden layer 1: activation RMS"),
            ("raw_rms", 1, "Hidden layer 2: activation RMS")]):
            trace(axes[row, col], case, key, layer)
            timeaxis(axes[row, col])
            axes[row, col].set_title(title+"\n"+label)
            if col == 0:
                axes[row, col].set_yscale("log")
                axes[row, col].set_ylim((1e-16, 2) if case == "axis" else (1e-4, 2))
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(.5, -.015))
    fig.suptitle("Actual dense neural networks versus observable closures, 0 ≤ t ≤ 40", fontsize=15, y=1.01)
    fig.tight_layout(rect=[0, .105, 1, 1])
    save(fig, "loss_and_hidden_rms")

    fig, axes = plt.subplots(2, 3, figsize=(14, 7.4))
    for row, (case, title) in enumerate([("axis", "Two-axis working data"), ("arcs", "Resolved arc working data")]):
        for layer in [0, 1]:
            trace(axes[row, layer], case, "motion_rms", layer)
            axes[row, layer].set_title(title+f"\nLayer {layer+1}: RMS movement from initialization")
            timeaxis(axes[row, layer])
        network = sample(case, large)
        mean = network["predictions"].mean(axis=0)
        for order in [1, 3, 5, "refined"]:
            name = f"{case}_N3_refined" if order == "refined" else f"{case}_N{order}"
            if name in closures:
                _, a = closures[name]
                error = np.sqrt(np.mean((mean-a["predictions"])**2, axis=1))
                axes[row, 2].plot(a["times"], error, color=colors[order], lw=1.7,
                                  ls=":" if order == "refined" else "-")
        spread = np.sqrt(np.mean((network["predictions"]-mean)**2, axis=2)).max(axis=0)
        axes[row, 2].fill_between(network["times"][0], 0, spread, color="#214b80", alpha=.14)
        axes[row, 2].set_title(title+"\nPrediction RMS error across 128 circle inputs")
        axes[row, 2].set_ylabel(f"Closure error against {large:,} network mean")
        timeaxis(axes[row, 2])
    fig.legend(handles, labels, loc="lower center", ncol=3, frameon=False, bbox_to_anchor=(.5, -.015))
    fig.suptitle("Hidden movement and predictions away from the training points", fontsize=15, y=1.01)
    fig.tight_layout(rect=[0, .105, 1, 1])
    save(fig, "hidden_movement_and_prediction_error")

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
    degrees = np.arange(128)*360/128
    for ax, case, title in zip(axes, ["axis", "arcs"], ["Two-axis working data", "Resolved arc working data"]):
        a = sample(case, large)["predictions"][:, -1]
        ax.fill_between(degrees, a.min(axis=0), a.max(axis=0), color="#214b80", alpha=.2)
        ax.plot(degrees, a.mean(axis=0), lw=2.3, color="#214b80", label=f"Network {large:,}, mean + seed range")
        for order in [1, 3, 5, "refined"]:
            name = f"{case}_N3_refined" if order == "refined" else f"{case}_N{order}"
            if name in closures:
                _, z = closures[name]
                ax.plot(degrees, z["predictions"][-1], color=colors[order], lw=1.5,
                        ls=":" if order == "refined" else "-",
                        label="Closure N=3, refined" if order == "refined" else f"Closure N={order}")
        ax.set_title(title+", t=40")
        ax.set_xlabel("Angle of normalized input u on the unit circle (degrees)")
        ax.set_ylabel("Prediction f(t, u)")
        ax.set_xticks([0, 90, 180, 270, 360])
    fig.legend(*axes[0].get_legend_handles_labels(), loc="lower center", ncol=3,
               frameon=False, bbox_to_anchor=(.5, -.06))
    fig.tight_layout(rect=[0, .13, 1, 1])
    save(fig, "final_circle_predictions")
    (output/"manifest.json").write_text(json.dumps(metadata, indent=2)+"\n")
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    main(parser.parse_args().output)
