"""Render separate-method RMS curves from saved discovery metrics, without retraining."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import FixedLocator, FuncFormatter, NullLocator


ORDERS = (1, 3, 5, 6, 7, 8, 9)
COLUMNS = (8, 45, 149, 241, 369, 544, 775)
CASES = {
    "quadrant_pairs": "Paired-label cluster",
    "two_outliers_alternating": "Alternating cluster + two outliers",
}
METHODS = {
    "ours": ("Ours", "#1261a0", "o"),
    "gaussian": ("Gaussian", "#c96519", "s"),
    "orthogonal": ("Orthogonal", "#7944a0", "^"),
}
CASE_TITLES = {
    "quadrant_pairs": "Paired discovery",
    "two_outliers_alternating": "Outlier discovery",
    "pairs_confirm1": "Paired fresh 1",
    "pairs_confirm2": "Paired fresh 2",
    "outliers_confirm1": "Outlier fresh 1",
    "outliers_confirm2": "Outlier fresh 2",
    "negative_confirm1": "Negative control — fresh 1",
    "negative_confirm2": "Negative control — fresh 2",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def draw(rows, out, horizontal, cases, columns_scale, y_limits=(.02, 2), pdf_bundle=None):
    by_p = horizontal == "order"
    single = len(cases) == 1
    fig, panels = plt.subplots(1, len(cases), figsize=(9.2, 6.3) if single else (12.8, 5.8),
                              sharey=True, squeeze=False)
    axes = panels[0]
    for ax, (case, title) in zip(axes, cases.items()):
        for method, (label, color, marker) in METHODS.items():
            selected = sorted((r for r in rows if r["case"] == case and r["method"] == method),
                              key=lambda r: r["order"])
            xs = [r[horizontal] for r in selected]
            # Both traces show independently validated numerical levels of the
            # same experiment. They are not seed confidence intervals.
            ax.plot(xs, [r["l2"] for r in selected], color=color, lw=1.25,
                    linestyle="--", alpha=.65, marker=marker, markersize=6.5,
                    markerfacecolor="white", markeredgewidth=1.0, zorder=2)
            ax.plot(xs, [r["refined_l2"] for r in selected], color=color, lw=2.1,
                    marker=marker, markersize=4.5, zorder=3)
        if not single:
            ax.set_title(title, fontsize=13, pad=13)
        ax.set_yscale("log")
        ax.set_ylim(*y_limits)
        ax.yaxis.set_major_locator(FixedLocator([v for v in [.005, .01, .02, .05, .1, .2, .5, 1, 2]
                                                if y_limits[0] <= v <= y_limits[1]]))
        ax.yaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value:g}"))
        ax.yaxis.set_minor_locator(NullLocator())
        if by_p:
            ax.set_xlim(.7, 9.3)
            ax.set_xticks(ORDERS)
            ax.set_xlabel("Dictionary order p", labelpad=8)
        else:
            ax.set_xscale(columns_scale)
            ax.set_xlim((6, 1000) if columns_scale == "log" else (0, 800))
            ax.xaxis.set_major_locator(FixedLocator(COLUMNS if columns_scale == "log" else range(0, 801, 100)))
            ax.xaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{int(value)}"))
            ax.xaxis.set_minor_locator(NullLocator())
            ax.set_xlabel(f"Number of dictionary vectors K₁ + K₂ ({columns_scale} scale)", labelpad=8)
        ax.grid(axis="y", color="#dddddd", linewidth=.7)
        ax.grid(axis="x", color="#eeeeee", linewidth=.6)
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(labelsize=10)
    axes[0].set_ylabel("RMS error against the full network (log scale)", labelpad=9)
    for ax in axes[1:]:
        ax.tick_params(axis="y", labelleft=True)
    method_handles = [Line2D([0], [0], color=color, marker=marker, lw=2, label=label)
                      for label, color, marker in METHODS.values()]
    fig.legend(handles=method_handles, loc="upper center", bbox_to_anchor=(.5, .925),
               ncol=3, frameon=False, fontsize=11, handlelength=2.5, columnspacing=2.5)
    heading = CASE_TITLES[next(iter(cases))] if single else (
        "Dictionary approximation on the two original configurations")
    fig.suptitle(heading, y=.985, fontsize=16)
    fig.text(.5, .075,
             "Solid / filled: selected finer tolerance   ·   Dashed / open: selected coarser tolerance\n"
             "Width 2,048 · 8,192 circle points · own training-MSE 0.001 crossings" if single else
             "Solid / filled: selected finer tolerance   ·   Dashed / open: selected coarser tolerance\n"
             "The two numerical levels nearly overlap. Width 2,048 · 8,192 circle points · own training-MSE 0.001 crossings",
             ha="center", va="center", fontsize=9, color="#444444", linespacing=1.6)
    tested_orders = sorted({r["order"] for r in rows if r["case"] in cases})
    tested_columns = [dict(zip(ORDERS, COLUMNS))[p] for p in tested_orders]
    fig.text(.5, .018,
             f"Tested p: {', '.join(map(str, tested_orders))}   →   columns: {', '.join(map(str, tested_columns))}.  Lines connect tested points.",
             ha="center", fontsize=9, color="#444444")
    fig.subplots_adjust(left=.115 if single else .082, right=.978, bottom=.23,
                        top=.84 if single else .78, wspace=.2)
    stem = "rms_vs_p" if by_p else "rms_vs_dictionary_columns"
    outputs = []
    for extension in ("png", "pdf", "svg"):
        path = out / (stem + "." + extension)
        fig.savefig(path, dpi=180, facecolor="white")
        outputs.append(path)
    if pdf_bundle is not None:
        pdf_bundle.savefig(fig, facecolor="white")
    plt.close(fig)
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--analysis", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--case", choices=tuple(CASES), help="Render only one original configuration")
    parser.add_argument("--axis", choices=("order", "dictionary_columns", "both"), default="both")
    parser.add_argument("--columns-scale", choices=("linear", "log"), default="log")
    args = parser.parse_args()
    rows = json.loads((args.analysis / "metrics.json").read_text())
    summary = json.loads((args.analysis / "summary.json").read_text())
    expected = {(case, method, p) for case in CASES for method in METHODS for p in ORDERS}
    actual = [(r["case"], r["method"], r["order"]) for r in rows]
    if len(actual) != len(expected) or set(actual) != expected:
        raise ValueError("Unexpected, duplicate, or missing discovery comparison rows")
    if summary["width"] != 2048 or set(summary["cases"]) != set(CASES):
        raise ValueError("Unexpected discovery width or case inventory")
    if not all(r["valid"] and
               r["dictionary_columns"] == dict(zip(ORDERS, COLUMNS))[r["order"]] for r in rows):
        raise ValueError("Invalid comparison or unexpected width/dictionary dimensions")
    cases = CASES if args.case is None else {args.case: CASES[args.case]}
    rows = [r for r in rows if r["case"] in cases]
    args.out.mkdir(parents=True, exist_ok=False)
    plotted = args.out / "plotted_rms.csv"
    fields = ("case", "method", "order", "dictionary_columns", "l2", "refined_l2", "valid")
    with plotted.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows({key: row[key] for key in fields} for row in rows)
    outputs = [plotted]
    for axis in (("order", "dictionary_columns") if args.axis == "both" else (args.axis,)):
        outputs.extend(draw(rows, args.out, axis, cases, args.columns_scale))
    provenance = {
        "command": [sys.executable, "-B", *sys.argv], "cwd": str(Path.cwd()),
        "source_sha256": digest(Path(__file__)),
        "input_hashes": {str((args.analysis / name).resolve()): digest(args.analysis / name)
                         for name in ("metrics.json", "summary.json")},
        "output_hashes": {path.name: digest(path) for path in outputs},
        "python": sys.version, "matplotlib": matplotlib.__version__,
        "cases": list(cases), "axis": args.axis,
        "dictionary_column_scale": args.columns_scale, "y_scale": "log",
        "scope": "Plot saved RMS values only; no new numerical metric, baseline selection, rate fit or training.",
        "numerical_levels": "Both selected levels per cell; solid=finer, dashed=coarser. Not a seed uncertainty band.",
    }
    (args.out / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print(str(args.out.resolve()))


if __name__ == "__main__":
    main()
