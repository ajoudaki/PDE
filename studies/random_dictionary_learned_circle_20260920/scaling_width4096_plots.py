"""Plot the requested width-4096 discovery rerun from its final saved analysis.

RMS values are copied from metrics.json. Training MSE and physical time are
copied from the exact primary/refined trajectory directories selected by
validation.json, including any selected extra-resolution attempts. No model
evaluation, loss calculation, training, or numerical metric is performed.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter
import numpy as np


HERE = Path(__file__).resolve().parent
DATA_ROOT = HERE.parents[1] / "data" / "generated" / HERE.name
WIDTH = 4096
ORDERS = (1, 3, 5, 7)
DIMENSIONS = {1: (5, 3), 3: (35, 10), 5: (128, 21), 7: (333, 36)}
CASES = {"quadrant_pairs": "Paired labels",
         "two_outliers_alternating": "Alternating labels + outliers"}
METHODS = {"ours": ("Ours", "#1261a0", "o"),
           "gaussian": ("Gaussian", "#c96519", "s"),
           "orthogonal": ("Orthogonal", "#7944a0", "^")}
STYLES = {"full": ("Full network", "#222222", "o"), **METHODS}
LEVELS = ("primary", "refined")


def digest(path):
    """Hash large trajectory archives without loading them into memory."""
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def owned(path):
    path = Path(path).resolve()
    if not path.is_relative_to(DATA_ROOT.resolve()) or path == DATA_ROOT.resolve():
        raise ValueError(f"Expected a path within this study's generated data: {path}")
    return path


def write_csv(path, fields, records):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows({key: record.get(key) for key in fields} for record in records)


def read_inputs(analysis, trajectory_roots=(), allow_unresolved=False):
    """Validate inventory and load only saved loss/time vectors from selected runs."""
    analysis = owned(analysis)
    trajectory_roots = tuple(owned(root) for root in trajectory_roots)
    hashes = {}

    def track(path, expected=None):
        path = owned(path)
        if str(path) not in hashes:
            hashes[str(path)] = digest(path)
        if expected is not None and hashes[str(path)] != expected:
            raise ValueError(f"Selected file no longer matches its final analysis hash: {path}")
        return path

    loaded = {}
    for name in ("summary.json", "metrics.json", "validation.json"):
        path = track(analysis / name)
        loaded[name] = json.loads(path.read_text())
    summary, rows, validation = (loaded[name] for name in
                                 ("summary.json", "metrics.json", "validation.json"))
    expected = {(case, method, p) for case in CASES for method in METHODS for p in ORDERS}
    actual = [(row["case"], row["method"], row["order"]) for row in rows]
    if (summary["width"] != WIDTH or sorted(summary["orders"]) != list(ORDERS)
            or set(summary["cases"]) != set(CASES)
            or len(actual) != len(expected) or set(actual) != expected):
        raise ValueError("Expected exactly width 4096, the two discovery cases, p1/3/5/7, and three methods")
    if not allow_unresolved and (not summary["all_comparisons_valid"] or not all(row["valid"] for row in rows)):
        raise ValueError("Unresolved endpoint-tolerance comparison: use --allow-unresolved to retain it with explicit markings")
    for row in rows:
        k1, k2 = DIMENSIONS[row["order"]]
        if (row["k1"], row["k2"], row["dictionary_columns"]) != (k1, k2, k1 + k2):
            raise ValueError(f"Unexpected dictionary dimensions: {row['case']} {row['model']}")
        if not all(isinstance(row[key], (int, float)) and math.isfinite(row[key]) and row[key] > 0
                   for key in ("l2", "refined_l2")):
            raise ValueError(f"Missing/nonpositive saved RMS: {row['case']} {row['model']}")

    expected_cells = {f"{case}_full" for case in CASES}
    expected_cells.update(f"{case}_{method}_p{p}" for case, method, p in expected)
    if set(validation) != expected_cells:
        raise ValueError("Validation inventory differs from the requested full/closure cells")

    # Check every metric's endpoint pointers against the authoritative selections.
    for row in rows:
        expected_valid = (validation[f"{row['case']}_{row['model']}"]["valid"]
                          and validation[f"{row['case']}_full"]["valid"])
        if row["valid"] != expected_valid:
            raise ValueError(f"Metric/validation validity mismatch: {row['case']} {row['model']}")
        for cell, level, prefix in (
                (f"{row['case']}_{row['model']}", "primary", ""),
                (f"{row['case']}_{row['model']}", "refined", "refined_"),
                (f"{row['case']}_full", "primary", "full_"),
                (f"{row['case']}_full", "refined", "full_refined_")):
            record = validation[cell][level]
            if owned(row[prefix + "directory"]) != owned(record["directory"]):
                raise ValueError(f"Metric/validation directory mismatch: {cell} {level}")
            for field in ("rtol", "atol", "status", "time", "loss"):
                if row[prefix + field] != record[field]:
                    raise ValueError(f"Metric/validation {field} mismatch: {cell} {level}")

    traces = {}
    configs = {}
    for case in CASES:
        models = [("full", "full", None)] + [
            (f"{method}_p{p}", method, p) for p in ORDERS for method in METHODS]
        for model, method, order in models:
            cell = f"{case}_{model}"
            pair = validation[cell]
            if not pair["valid"]:
                discrepancy = pair["step_refinement_endpoint_max"]
                tolerance_only = (isinstance(discrepancy, (int, float)) and math.isfinite(discrepancy)
                                  and discrepancy > summary["refinement_gate"] and pair["reasons"]
                                  and all(reason.startswith("endpoint refinement discrepancy ")
                                          for reason in pair["reasons"]))
                if not allow_unresolved or not tolerance_only:
                    raise ValueError(f"Selected trajectory pair has an unallowed unresolved check: {cell}")
            for level in LEVELS:
                record = pair[level]
                directory = owned(record["directory"])
                if trajectory_roots and not any(directory.is_relative_to(root) for root in trajectory_roots):
                    raise ValueError(f"Selected directory lies outside supplied trajectory roots: {directory}")
                if record["status"] != "fitted" or not record["fitted"] or not record["replay_valid"]:
                    raise ValueError(f"Selected endpoint is not fitted/replayed: {cell} {level}")
                declared_hashes = {str(Path(path).resolve()): value for path, value in record["files"].items()}
                arrays_path, raw_summary_path = directory / "arrays.npz", directory / "summary.json"
                for path in (arrays_path, raw_summary_path):
                    if str(path) not in declared_hashes:
                        raise ValueError(f"Final validation lacks the selected file hash: {path}")
                    track(path, declared_hashes[str(path)])
                config_path = track(record["config_path"])
                if str(config_path) not in configs:
                    configs[str(config_path)] = json.loads(config_path.read_text())
                config = configs[str(config_path)]
                if config["width"] != WIDTH or config["threshold"] != summary["threshold"]:
                    raise ValueError(f"Trajectory config has a different width/threshold: {config_path}")
                raw_summary = json.loads(raw_summary_path.read_text())
                if any(raw_summary[field] != record[field] for field in ("time", "loss", "status", "rtol", "atol")):
                    raise ValueError(f"Trajectory summary differs from final validation: {directory}")
                with np.load(arrays_path, allow_pickle=False) as arrays:
                    times, losses = arrays["times"], arrays["losses"]
                if (times.ndim != 1 or times.shape != losses.shape or len(times) < 2
                        or not np.isfinite(times).all() or not np.isfinite(losses).all()
                        or times[0] != 0 or not np.all(times[1:] > times[:-1])
                        or not np.all(losses > 0)
                        or times[-1] != record["time"] or losses[-1] != record["loss"]):
                    raise ValueError(f"Malformed saved physical-time/MSE trace: {cell} {level}")
                traces[case, model, level] = {
                    "case": case, "model": model, "method": method, "order": order,
                    "level": level, "attempt_name": record["name"], "directory": str(directory),
                    "rtol": record["rtol"], "atol": record["atol"], "status": record["status"],
                    "valid": pair["valid"], "times": times, "losses": losses,
                    "fitted": record["fitted"], "replay_valid": record["replay_valid"],
                    "endpoint_refinement_max": pair["step_refinement_endpoint_max"],
                    "samples": len(times), "endpoint_time": record["time"], "endpoint_mse": record["loss"],
                }
    return rows, summary, traces, hashes


def log_bounds(values):
    values = list(values)
    return min(values) * .8, max(values) * 1.25


def decorate(ax):
    ax.set_yscale("log")
    ax.grid(which="major", axis="y", color="#dddddd", linewidth=.7)
    ax.grid(which="major", axis="x", color="#eeeeee", linewidth=.6)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=10)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value:g}"))


def save_figure(fig, directory, stem, bundle):
    paths = []
    for extension in ("png", "pdf", "svg"):
        path = directory / f"{stem}.{extension}"
        fig.savefig(path, dpi=180, facecolor="white")
        paths.append(path)
    bundle.savefig(fig, facecolor="white")
    plt.close(fig)
    return paths


def draw_rms(rows, case, directory, summary, bounds, bundle):
    fig, ax = plt.subplots(figsize=(9.2, 6.3))
    for method, (label, color, marker) in METHODS.items():
        selected = sorted((r for r in rows if r["case"] == case and r["method"] == method),
                          key=lambda r: r["order"])
        xs = [r["dictionary_columns"] for r in selected]
        ax.plot(xs, [r["l2"] for r in selected], color=color, lw=1.2, ls="--", alpha=.65,
                marker=marker, ms=6.5, markerfacecolor="white", zorder=2)
        ax.plot(xs, [r["refined_l2"] for r in selected], color=color, lw=2.1,
                marker=marker, ms=4.5, label=label, zorder=3)
        unresolved = [r for r in selected if not r["valid"]]
        if unresolved:
            ux = [r["dictionary_columns"] for r in unresolved]
            ax.scatter(ux, [r["l2"] for r in unresolved], color=color, marker="x",
                       s=95, linewidths=2, zorder=6)
            ax.scatter(ux, [r["refined_l2"] for r in unresolved], color=color, marker="X",
                       s=95, edgecolors="white", linewidths=.6, zorder=7)
    decorate(ax)
    ax.set_xlim(0, 400)
    ax.set_xticks(range(0, 401, 50))
    ax.set_ylim(*bounds)
    ax.set_xlabel("Number of dictionary vectors K₁ + K₂ (linear scale)", labelpad=9)
    ax.set_ylabel("RMS error against the full network (log scale)", labelpad=9)
    fig.suptitle(f"{CASES[case]} · width {WIDTH:,}", y=.985, fontsize=16)
    fig.legend(*ax.get_legend_handles_labels(), loc="upper center", bbox_to_anchor=(.5, .928),
               ncol=3, frameon=False, fontsize=11)
    fig.text(.5, .092,
             "Solid / filled: selected finer tolerance · Dashed / open: selected coarser tolerance\n"
             f"Own training-MSE {summary['threshold']:g} crossings · RMS copied from the final 8,192-angle analysis",
             ha="center", fontsize=9, color="#444444", linespacing=1.6)
    fig.text(.5, .025, "Tested p: 1, 3, 5, 7 → columns: 8, 45, 149, 369. Lines connect tested points.",
             ha="center", fontsize=9, color="#444444")
    unresolved = [r for r in rows if r["case"] == case and not r["valid"]]
    if unresolved:
        cells = ", ".join(f"{METHODS[r['method']][0]} p{r['order']}" for r in unresolved)
        fig.text(.5, .17, f"× / X: endpoint tolerance unresolved ({cells}); fitted values retained.",
                 ha="center", fontsize=9, color="#8a4200")
    fig.subplots_adjust(left=.12, right=.975, bottom=.275 if unresolved else .235, top=.84)
    return save_figure(fig, directory, "rms_vs_dictionary_columns", bundle)


def draw_losses(traces, case, directory, summary, bounds, bundle):
    fig, axes = plt.subplots(2, 2, figsize=(12.2, 8.6), sharex=True, sharey=True)
    case_traces = [trace for (name, _, _), trace in traces.items() if name == case]
    xmax = max(float(trace["times"][-1]) for trace in case_traces) * 1.04
    for ax, p in zip(axes.flat, ORDERS):
        unresolved_methods = []
        for method, (label, color, _) in STYLES.items():
            model = "full" if method == "full" else f"{method}_p{p}"
            if not traces[case, model, "refined"]["valid"]:
                unresolved_methods.append(label)
            for level in LEVELS:
                trace = traces[case, model, level]
                finer = level == "refined"
                ax.plot(trace["times"], trace["losses"], color=color,
                        lw=1.75 if finer else 1.05, ls="-" if finer else "--", alpha=1 if finer else .6)
                ax.plot(trace["times"][-1], trace["losses"][-1], marker="o" if trace["valid"] else "X",
                        ms=(3.3 if finer else 4.5) if trace["valid"] else 6.5,
                        color=color, markerfacecolor=color if finer else "white", zorder=4)
        ax.axhline(summary["threshold"], color="#888888", lw=.8, ls=":", zorder=1)
        decorate(ax)
        ax.set_xlim(0, xmax)
        ax.set_ylim(*bounds)
        k1, k2 = DIMENSIONS[p]
        ax.set_title(f"p = {p} · {k1 + k2} dictionary vectors", fontsize=12, pad=9)
        if unresolved_methods:
            ax.text(.97, .95, ", ".join(unresolved_methods) + ": endpoint tolerance unresolved\nTraining fit succeeded",
                    transform=ax.transAxes, ha="right", va="top", fontsize=9, color="#8a4200",
                    bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9, "pad": 3})
    for ax in axes[1]:
        ax.set_xlabel("Physical time", labelpad=8)
    for ax in axes[:, 0]:
        ax.set_ylabel("Training MSE (log scale)", labelpad=8)
    handles = [Line2D([0], [0], color=color, lw=2, label=label) for label, color, _ in STYLES.values()]
    fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(.5, .948), ncol=4,
               frameon=False, fontsize=11)
    fig.suptitle(f"{CASES[case]} · training loss · width {WIDTH:,}", y=.99, fontsize=16)
    fig.text(.5, .045,
             "Solid: selected finer tolerance · Dashed: selected coarser tolerance\n"
             f"Saved accepted-step losses; each trace ends at its own MSE {summary['threshold']:g} crossing. "
             "The same full-network reference is repeated in every panel.",
             ha="center", fontsize=9, color="#444444", linespacing=1.6)
    fig.subplots_adjust(left=.085, right=.978, bottom=.16, top=.85, hspace=.24, wspace=.12)
    return save_figure(fig, directory, "training_mse_vs_physical_time", bundle), xmax


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--analysis", type=Path, required=True, help="Final selected-level analysis directory")
    parser.add_argument("--out", type=Path, required=True, help="New output directory within this study's generated data")
    parser.add_argument("--trajectory-root", type=Path, action="append", default=[],
                        help="Optional allowed selected-trajectory root; repeat for primary/refined/extra roots")
    parser.add_argument("--allow-unresolved", action="store_true",
                        help="Retain fitted/replayed endpoint-tolerance failures with explicit plot markings; default is strict")
    args = parser.parse_args()
    out = owned(args.out)
    if out.exists():
        raise FileExistsError(out)
    rows, summary, traces, hashes = read_inputs(args.analysis, args.trajectory_root, args.allow_unresolved)
    out.mkdir(parents=True, exist_ok=False)
    rms_csv, trace_csv, selection_csv = (out / name for name in
                                       ("plotted_rms.csv", "training_mse.csv", "selected_trajectories.csv"))
    rms_fields = ("case", "method", "order", "k1", "k2", "dictionary_columns", "l2", "refined_l2", "valid",
                  "directory", "refined_directory", "full_directory", "full_refined_directory")
    write_csv(rms_csv, rms_fields, rows)
    metadata_fields = ("case", "model", "method", "order", "level", "attempt_name", "directory",
                       "rtol", "atol", "status", "valid", "fitted", "replay_valid", "endpoint_refinement_max",
                       "samples", "endpoint_time", "endpoint_mse")
    write_csv(selection_csv, metadata_fields, traces.values())

    def samples():
        for trace in traces.values():
            for index, (time, loss) in enumerate(zip(trace["times"], trace["losses"])):
                yield {**{key: trace[key] for key in metadata_fields},
                       "sample_index": index, "physical_time": float(time), "training_mse": float(loss)}

    write_csv(trace_csv, metadata_fields + ("sample_index", "physical_time", "training_mse"), samples())
    rms_bounds = log_bounds(row[field] for row in rows for field in ("l2", "refined_l2"))
    loss_bounds = log_bounds(value for trace in traces.values()
                             for value in (float(trace["losses"].min()), float(trace["losses"].max())))
    bundle_path = out / "width4096_rms_and_training_loss.pdf"
    outputs = [rms_csv, trace_csv, selection_csv, bundle_path]
    limits = {}
    with PdfPages(bundle_path) as bundle:
        for case in CASES:
            target = out / case
            target.mkdir()
            outputs.extend(draw_rms(rows, case, target, summary, rms_bounds, bundle))
            generated, xmax = draw_losses(traces, case, target, summary, loss_bounds, bundle)
            outputs.extend(generated)
            limits[case] = {"rms": {"x": [0, 400], "y": list(rms_bounds)},
                            "training_mse": {"x": [0, xmax], "y": list(loss_bounds)}}
    provenance = {
        "command": [sys.executable, "-B", *sys.argv], "cwd": str(Path.cwd()),
        "source_hashes": {str(Path(__file__).resolve()): digest(Path(__file__))},
        "input_hashes": hashes,
        "output_hashes": {str(path.relative_to(out)): digest(path) for path in outputs},
        "python": sys.version, "matplotlib": matplotlib.__version__, "numpy": np.__version__,
        "analysis": str(owned(args.analysis)), "width": WIDTH, "cases": list(CASES), "orders": list(ORDERS),
        "comparison_rows": len(rows), "selected_trajectories": len(traces),
        "valid_comparisons": sum(bool(row["valid"]) for row in rows),
        "allow_unresolved": args.allow_unresolved,
        "unresolved_comparisons": [{key: row[key] for key in
                                    ("case", "model", "order", "method", "reasons", "step_refinement_endpoint_max")}
                                   for row in rows if not row["valid"]],
        "training_samples": sum(trace["samples"] for trace in traces.values()),
        "axis_limits": limits, "x_scale": "linear", "y_scale": "log",
        "selection": "Only primary/refined endpoint directories selected by final validation.json; "
                     "each pointer and endpoint metadata cross-checked against metrics.json. "
                     "Each selected arrays.npz and summary.json matches its retained validation hash.",
        "numerical_levels": "Primary/coarser and refined/finer are per-cell selected levels, "
                            "not uniform tolerance values or seed uncertainty intervals.",
        "unresolved_display": "All fitted/replayed values are retained. Endpoint-tolerance unresolved RMS points "
                              "use x/X markers and a footnote; the affected training-loss control/panel is labeled. "
                              "A successful training fit does not validate its endpoint-tolerance comparison.",
        "full_reference": "One selected full-network pair per case, repeated across p panels; "
                          "exported once per selected level in the trajectory CSV.",
        "scope": "Copied saved RMS and accepted-step physical times/training MSE only; "
                 "no network evaluation, loss/RMS recomputation, baseline selection, or training.",
    }
    (out / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print(json.dumps({"out": str(out), "comparisons": len(rows), "selected_trajectories": len(traces),
                      "training_samples": provenance["training_samples"], "output_files": len(outputs)}))


if __name__ == "__main__":
    main()
