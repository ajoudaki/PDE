"""Compact scientific figure from audited saved metrics; no new experiments."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--analysis", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    summary = json.loads((args.analysis / "summary.json").read_text())
    rows = json.loads((args.analysis / "metrics.json").read_text())
    colors = {"ours": "#1261a0", "gaussian": "#ce6c1b", "orthogonal": "#7d4196"}
    fig, axes = plt.subplots(len(summary["cases"]), 3,
                             figsize=(14, 3.9 * len(summary["cases"])), squeeze=False)
    for i, case in enumerate(summary["cases"]):
        for method, color in colors.items():
            values = sorted((r for r in rows if r["case"] == case and r["method"] == method), key=lambda r: r["order"])
            for j, field in enumerate(("l2", "max_abs")):
                for prefix, style in (("", "-"), ("refined_", "--")):
                    axes[i, j].plot([r["dictionary_columns"] for r in values],
                                    [r[prefix + field] if r["valid"] else float("nan") for r in values],
                                    style, color=color, marker="o", markersize=3,
                                    label=method if not prefix else None)
        ratios = [r for r in summary["random_over_ours"] if r["case"] == case]
        for prefix, style, label in (("", "-", "selected coarser"), ("refined_", "--", "selected finer")):
            axes[i, 2].plot([r["dictionary_columns"] for r in ratios],
                            [r[prefix + "better_random_over_ours_l2"] if r["valid"] else float("nan") for r in ratios],
                            style, color="#1261a0", marker="o", markersize=3, label=label)
        axes[i, 2].axhline(1, color="gray", linewidth=.8)
        for j, label in enumerate(("Circle RMS error", "Sampled maximum error", "Better random / ours RMS")):
            axes[i, j].set_xscale("log")
            if j < 2:
                axes[i, j].set_yscale("log")
            axes[i, j].set_xlabel("Dictionary columns K1 + K2")
            axes[i, j].set_ylabel(label)
            axes[i, j].set_title(case.replace("_", " "))
            axes[i, j].grid(alpha=.2)
            axes[i, j].legend(fontsize=8)
    fig.suptitle(f"Finite dictionary scaling, n={summary['width']} | solid/dashed: both selected numerical levels\n"
                 "Own training-MSE crossings; 8192 circle angles; no fitted asymptotic rate", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, .93))
    fig.savefig(args.out / "scaling_summary.png", dpi=160)
    plt.close(fig)
    digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
    (args.out / "provenance.json").write_text(json.dumps({
        "command": [sys.executable, "-B", *sys.argv], "source_sha256": digest(Path(__file__)),
        "input_hashes": {str(args.analysis / n): digest(args.analysis / n) for n in ("metrics.json", "summary.json")},
        "figure_sha256": digest(args.out / "scaling_summary.png"),
        "scope": "Rendering already-computed metrics only; no new numerical comparison or trajectory."
    }, indent=2) + "\n")


if __name__ == "__main__":
    main()
