"""Render every configuration in the completed scaling campaign from saved RMS.

This is presentation only: three individual methods and both selected numerical
levels, with no new metric calculation, baseline selection, or training.
"""
import argparse
import csv
import json
from pathlib import Path
import sys

import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
import scaling_plot_rms as plot


GROUPS = {
    "scaling_discovery_analysis01": (("quadrant_pairs", "two_outliers_alternating"), plot.ORDERS),
    "scaling_confirm1_analysis02": (("pairs_confirm1", "outliers_confirm1", "negative_confirm1"), (1, 5, 9)),
    "scaling_confirm2_analysis03": (("pairs_confirm2", "outliers_confirm2", "negative_confirm2"), (1, 5, 9)),
}
DISPLAY_ORDER = ("quadrant_pairs", "pairs_confirm1", "pairs_confirm2",
                 "two_outliers_alternating", "outliers_confirm1", "outliers_confirm2",
                 "negative_confirm1", "negative_confirm2")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    rows, input_hashes = [], {}
    dimensions = dict(zip(plot.ORDERS, plot.COLUMNS))
    for root, (cases, orders) in GROUPS.items():
        directory = args.data_root / root
        for name in ("metrics.json", "summary.json"):
            path = directory / name
            input_hashes[str(path.resolve())] = plot.digest(path)
        summary = json.loads((directory / "summary.json").read_text())
        group_rows = json.loads((directory / "metrics.json").read_text())
        expected = {(case, method, p) for case in cases for method in plot.METHODS for p in orders}
        actual = [(r["case"], r["method"], r["order"]) for r in group_rows]
        if (summary["width"] != 2048 or set(summary["cases"]) != set(cases) or
                len(actual) != len(expected) or set(actual) != expected):
            raise ValueError(f"Unexpected case/order/method inventory in {root}")
        if not all(r["valid"] and r["dictionary_columns"] == dimensions[r["order"]] for r in group_rows):
            raise ValueError(f"Invalid comparison or dimension in {root}")
        rows.extend(dict(r, source_analysis=root) for r in group_rows)
    if len(rows) != 96:
        raise ValueError("Expected all 96 final comparison rows")
    args.out.mkdir(parents=True, exist_ok=False)
    exported = args.out / "plotted_rms.csv"
    fields = ("source_analysis", "case", "method", "order", "dictionary_columns", "l2", "refined_l2", "valid")
    with exported.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows({key: r[key] for key in fields} for r in rows)
    bundle = args.out / "all_configurations.pdf"
    outputs = [exported, bundle]
    limits = {}
    with PdfPages(bundle) as pdf:
        for case in DISPLAY_ORDER:
            target = args.out / case
            target.mkdir()
            bounds = (.005, .05) if case.startswith("negative_") else (.02, 2)
            selected = [r for r in rows if r["case"] == case]
            if not all(bounds[0] < r[key] < bounds[1] for r in selected for key in ("l2", "refined_l2")):
                raise ValueError(f"Plot would clip data for {case}")
            outputs.extend(plot.draw(selected, target, "dictionary_columns",
                                     {case: plot.CASE_TITLES[case]}, "linear", bounds, pdf))
            limits[case] = {"x": [0, 800], "y": list(bounds)}
    provenance = {
        "command": [sys.executable, "-B", *sys.argv], "cwd": str(Path.cwd()),
        "source_hashes": {str(p.resolve()): plot.digest(p) for p in (Path(__file__), Path(plot.__file__))},
        "input_hashes": input_hashes,
        "output_hashes": {str(p.relative_to(args.out)): plot.digest(p) for p in outputs},
        "python": sys.version, "matplotlib": matplotlib.__version__,
        "cases": list(DISPLAY_ORDER), "dictionary_column_scale": "linear", "y_scale": "log",
        "axis_limits": limits, "negative_control_range": "Tighter y range to display their smaller RMS errors; all values remain visible.",
        "scope": "Rendering 96 saved comparisons only. No new experiment, arithmetic metric, fitted rate, or control selection.",
        "numerical_levels": "Solid/filled=finer; dashed/open=coarser. Numerical tolerances, not seed uncertainty.",
    }
    (args.out / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print(str(args.out.resolve()))


if __name__ == "__main__":
    main()
