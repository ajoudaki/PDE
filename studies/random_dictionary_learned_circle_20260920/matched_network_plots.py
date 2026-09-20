"""Display saved width-1024 matched-network RMS and training-loss results.

Only previously saved scalar metrics and loss/time arrays are read. There is
no predictor evaluation, loss calculation, fitting, or metric recomputation.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
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
WIDTH, ORDERS = 1024, (1, 3, 5)
DIMENSIONS = {1: (5, 3), 3: (35, 10), 5: (128, 21)}
CASES = {"quadrant_alternating": "Tight alternating labels",
         "two_outliers_alternating": "Alternating labels + two outliers"}
METHODS = {"ours": ("Ours", "#1261a0", "o"),
           "small_trainable": ("Trainable-count match", "#c96519", "s"),
           "small_total": ("Total-size match", "#7944a0", "^")}
STYLES = {"full": ("Full network (n = 1,024)", "#222222", "o"), **METHODS}
LEVELS = ("primary", "refined")


def digest(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def owned(path):
    path = Path(path).resolve()
    if not path.is_relative_to(DATA_ROOT.resolve()) or path == DATA_ROOT.resolve():
        raise ValueError(f"Expected this study's generated-data path: {path}")
    if not path.relative_to(DATA_ROOT.resolve()).parts[0].startswith("matched_network_"):
        raise ValueError(f"Expected the matched-network namespace: {path}")
    return path


def write_csv(path, fields, records):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows({key: record.get(key) for key in fields} for record in records)


def read_inputs(analysis, allow_unresolved=False):
    analysis = owned(analysis)
    hashes, loaded = {}, {}

    def track(path, expected=None):
        path = owned(path)
        if str(path) not in hashes:
            hashes[str(path)] = digest(path)
        if expected is not None and hashes[str(path)] != expected:
            raise ValueError(f"Selected input differs from its analyzed hash: {path}")
        return path

    for name in ("metrics.json", "summary.json", "selected_levels.json"):
        loaded[name] = json.loads(track(analysis / name).read_text())
    rows, summary, selection = (loaded[n] for n in
                                ("metrics.json", "summary.json", "selected_levels.json"))
    expected = {(case, method, p) for case in CASES for method in METHODS for p in ORDERS}
    actual = [(r["case"], r["method"], r["order"]) for r in rows]
    if len(actual) != len(expected) or set(actual) != expected:
        raise ValueError("Expected the two matched-network cases, p1/3/5, and exactly three methods")
    if summary["width"] != WIDTH or sorted(summary["orders"]) != list(ORDERS):
        raise ValueError("Incorrect full-network width or dictionary orders")
    cells = selection["cells"]
    expected_cells = {f"{case}_full" for case in CASES}
    expected_cells.update(f"{case}_{method}_p{p}" for case, method, p in expected)
    if set(cells) != expected_cells:
        raise ValueError("Selected trajectory inventory differs from expected matched-network cells")
    if not allow_unresolved and (not all(r["valid"] for r in rows)
                                or not all(c["valid"] for c in cells.values())):
        raise ValueError("Unresolved checks present; use --allow-unresolved for explicitly marked display")
    for row in rows:
        k1, k2 = DIMENSIONS[row["order"]]
        if (row["k1"], row["k2"], row["dictionary_vectors"]) != (k1, k2, k1 + k2):
            raise ValueError("Saved dictionary dimensions differ from the protocol")
        train, total = 3 * WIDTH + k1 * k2, WIDTH * (k1 + k2) + 3 * WIDTH + k1 * k2
        if row["method"] == "ours":
            expected_counts = (WIDTH, train, total)
        else:
            m = row["width"]
            budget = train if row["method"] == "small_trainable" else total
            if not (m - 1) ** 2 + 3 * (m - 1) < budget <= m * m + 3 * m:
                raise ValueError("Small width does not implement the predeclared upward parameter match")
            expected_counts = (m, m * m + 3 * m, m * m + 3 * m)
        if (row["width"], row["trainable_parameters"], row["model_parameters"]) != expected_counts:
            raise ValueError("Saved parameter counts differ from declared representation")
        for level in LEVELS:
            record = cells[f"{row['case']}_{row['model']}"][level]
            if owned(row[f"{level}_directory"]) != owned(record["directory"]):
                raise ValueError("Selected trajectory differs from metric endpoint")
            value = row[f"{level}_rms"]
            if not isinstance(value, (float, int)) or not np.isfinite(value) or value <= 0:
                raise ValueError("Plot requires a finite positive saved RMS value")

    traces = {}
    for cell, pair in cells.items():
        case, model = pair["case"], pair["model"]
        method = "full" if model == "full" else model.rsplit("_p", 1)[0]
        order = None if model == "full" else int(model.rsplit("_p", 1)[1])
        for level in LEVELS:
            record = pair[level]
            directory = owned(record["directory"])
            if not record["fitted"] or not record["replay_valid"] or record["status"] != "fitted":
                raise ValueError(f"Cannot display an unfitted or unreplayed trajectory: {cell} {level}")
            declared = {str(Path(p).resolve()): v for p, v in record["files"].items()}
            for name in ("arrays.npz", "summary.json"):
                path = directory / name
                if str(path) not in declared:
                    raise ValueError(f"Analysis lacks selected file hash: {path}")
                track(path, declared[str(path)])
            raw = json.loads((directory / "summary.json").read_text())
            if any(raw[k] != record[k] for k in ("status", "time", "loss", "rtol", "atol")):
                raise ValueError(f"Selected trajectory metadata mismatch: {cell} {level}")
            with np.load(directory / "arrays.npz", allow_pickle=False) as arrays:
                times, losses = arrays["times"], arrays["losses"]
            if (times.ndim != 1 or times.shape != losses.shape or len(times) < 2
                    or not np.isfinite(times).all() or not np.isfinite(losses).all()
                    or times[0] != 0 or not np.all(np.diff(times) > 0)
                    or not np.all(losses > 0) or times[-1] != record["time"]
                    or losses[-1] != record["loss"]):
                raise ValueError(f"Malformed saved time/loss vectors: {cell} {level}")
            traces[case, model, level] = dict(case=case, model=model, method=method,
                order=order, selected=level, numerical_level=record["level"],
                directory=str(directory), rtol=record["rtol"], atol=record["atol"],
                valid=pair["valid"], reasons=pair["reasons"],
                refinement_endpoint_max=pair["refinement_endpoint_max"],
                times=times, losses=losses, samples=len(times),
                endpoint_time=record["time"], endpoint_mse=record["loss"])
    return rows, summary, selection, traces, hashes


def log_bounds(values):
    values = list(values)
    return min(values) * .8, max(values) * 1.25


def decorate(ax):
    ax.set_yscale("log")
    ax.grid(axis="y", color="#dddddd", linewidth=.7)
    ax.grid(axis="x", color="#eeeeee", linewidth=.6)
    ax.spines[["top", "right"]].set_visible(False)
    ax.tick_params(labelsize=10)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value:g}"))


def parameter_rows(rows, case):
    result = []
    for p in ORDERS:
        selected = {r["method"]: r for r in rows if r["case"] == case and r["order"] == p}
        ours, train, total = (selected[m] for m in METHODS)
        result.append([str(p), str(ours["dictionary_vectors"]),
            f"{ours['trainable_parameters']:,} / {ours['model_parameters']:,}",
            f"m={train['width']}: {train['trainable_parameters']:,}",
            f"m={total['width']}: {total['trainable_parameters']:,}"])
    return result


def add_parameter_table(fig, rows, case, box):
    ax = fig.add_axes(box)
    ax.axis("off")
    table = ax.table(cellText=parameter_rows(rows, case),
        colLabels=["p", "Vectors", "Ours: trained / total", "Trainable-count match", "Total-size match"],
        colWidths=[.04, .075, .28, .30, .305], loc="center", cellLoc="center", bbox=[0, 0, 1, 1])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    for (row, _), cell in table.get_celld().items():
        cell.set_linewidth(.35)
        cell.set_edgecolor("#dddddd")
        if row == 0:
            cell.set_facecolor("#f4f4f4")


def save_figure(fig, out, stem, bundle):
    paths = []
    for extension in ("png", "pdf", "svg"):
        path = out / f"{stem}.{extension}"
        fig.savefig(path, dpi=180, facecolor="white")
        paths.append(path)
    bundle.savefig(fig, facecolor="white")
    plt.close(fig)
    return paths


def draw_rms(rows, case, out, summary, bounds, bundle):
    fig, ax = plt.subplots(figsize=(10, 7.3))
    for method, (label, color, marker) in METHODS.items():
        selected = sorted((r for r in rows if r["case"] == case and r["method"] == method),
                          key=lambda r: r["order"])
        x = [r["dictionary_vectors"] for r in selected]
        for level in LEVELS:
            finer = level == "refined"
            ax.plot(x, [r[f"{level}_rms"] for r in selected], color=color,
                lw=2 if finer else 1.2, ls="-" if finer else "--", alpha=1 if finer else .65,
                marker=marker, ms=5 if finer else 6.5, markerfacecolor=color if finer else "white",
                label=label if finer else None)
            unresolved = [r for r in selected if not r["valid"]]
            if unresolved:
                ax.scatter([r["dictionary_vectors"] for r in unresolved],
                    [r[f"{level}_rms"] for r in unresolved], color=color,
                    marker="X" if finer else "x", s=90, linewidths=1.5, zorder=6)
    decorate(ax)
    ax.set_xlim(0, max(sum(d) for d in DIMENSIONS.values()) * 1.07)
    ax.set_xticks([0, 8, 45, 100, 149])
    ax.set_ylim(*bounds)
    ax.set_xlabel("Dictionary vectors K₁ + K₂ (linear scale)", labelpad=8)
    ax.set_ylabel("RMS discrepancy from the full network (log scale)", labelpad=8)
    fig.suptitle(f"{CASES[case]} · closure / full width n = 1,024", y=.98, fontsize=15)
    fig.legend(*ax.get_legend_handles_labels(), loc="upper center", bbox_to_anchor=(.5, .925),
               ncol=3, frameon=False, fontsize=10.5)
    fig.text(.5, .305, "Solid / filled: selected finer level · Dashed / open: selected coarser level",
             ha="center", fontsize=9.5)
    add_parameter_table(fig, rows, case, [.085, .105, .9, .155])
    fig.text(.5, .072, "Small exact networks: all listed parameters trained. Full reference: 1,051,648 trained / total.",
             ha="center", fontsize=9)
    fig.text(.5, .035, f"Each model's own training-MSE {summary['threshold']:g} crossing · RMS: 8,192 angles · Full versus itself: 0 (outside log axis)",
             ha="center", fontsize=9)
    if any(not r["valid"] for r in rows if r["case"] == case):
        fig.text(.5, .276, "× / X: numerical comparison unresolved; fitted values retained.",
                 ha="center", fontsize=9, color="#8a4200")
    fig.subplots_adjust(left=.105, right=.98, bottom=.4, top=.84)
    return save_figure(fig, out, f"{case}_rms", bundle)


def draw_losses(rows, traces, case, out, summary, bounds, bundle):
    fig, axes = plt.subplots(1, 3, figsize=(14, 6.3), sharex=True, sharey=True)
    xmax = max(t["endpoint_time"] for (c, _, _), t in traces.items() if c == case) * 1.035
    for ax, p in zip(axes, ORDERS):
        unresolved = []
        for method, (label, color, _) in STYLES.items():
            model = "full" if method == "full" else f"{method}_p{p}"
            if not traces[case, model, "refined"]["valid"]:
                unresolved.append("Full" if method == "full" else METHODS[method][0])
            for level in LEVELS:
                trace, finer = traces[case, model, level], level == "refined"
                ax.plot(trace["times"], trace["losses"], color=color, lw=1.8 if finer else 1,
                        ls="-" if finer else "--", alpha=1 if finer else .6)
                ax.plot(trace["endpoint_time"], trace["endpoint_mse"], color=color,
                    marker="o" if trace["valid"] else "X", ms=4 if trace["valid"] else 6.5,
                    markerfacecolor=color if finer else "white")
        ax.axhline(summary["threshold"], color="#888888", ls=":", lw=.8)
        decorate(ax)
        ax.set_xlim(0, xmax)
        ax.set_ylim(*bounds)
        ax.set_xlabel("Physical time", labelpad=7)
        ax.set_title(f"p = {p} · {sum(DIMENSIONS[p])} dictionary vectors", fontsize=11)
        if unresolved:
            ax.text(.97, .97, "Unresolved comparison:\n" + "\n".join(unresolved),
                    transform=ax.transAxes, ha="right", va="top", fontsize=8.5, color="#8a4200",
                    bbox={"facecolor": "white", "edgecolor": "none", "alpha": .9})
    axes[0].set_ylabel("Training MSE (log scale)", labelpad=8)
    fig.suptitle(f"{CASES[case]} · training loss · closure / full n = 1,024", y=.985, fontsize=16)
    handles = [Line2D([0], [0], color=color, lw=2, label=label)
               for label, color, _ in STYLES.values()]
    fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(.5, .925),
               ncol=4, frameon=False, fontsize=10.5)
    add_parameter_table(fig, rows, case, [.14, .085, .74, .16])
    fig.text(.5, .282, "Solid: selected finer level · Dashed: selected coarser level · Same full reference repeated in every panel",
             ha="center", fontsize=9)
    fig.text(.5, .035, f"Saved accepted-step losses, ending at each model's own MSE {summary['threshold']:g} crossing. Full network: 1,051,648 parameters.",
             ha="center", fontsize=9)
    fig.subplots_adjust(left=.065, right=.985, top=.82, bottom=.38, wspace=.09)
    return save_figure(fig, out, f"{case}_training_loss", bundle), xmax


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--analysis", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--allow-unresolved", action="store_true")
    args = parser.parse_args()
    out = owned(args.out)
    if out.exists():
        raise FileExistsError(out)
    rows, summary, selection, traces, hashes = read_inputs(args.analysis, args.allow_unresolved)
    out.mkdir(parents=True)
    fields = ("case", "model", "method", "order", "width", "k1", "k2", "dictionary_vectors",
              "trainable_parameters", "model_parameters", "matched_budget", "valid", "reasons",
              "primary_rms", "refined_rms", "primary_directory", "refined_directory")
    write_csv(out / "plotted_rms.csv", fields, rows)
    meta = ("case", "model", "method", "order", "selected", "numerical_level", "directory", "rtol", "atol",
            "valid", "reasons", "refinement_endpoint_max", "samples", "endpoint_time", "endpoint_mse")
    write_csv(out / "selected_trajectories.csv", meta, traces.values())
    write_csv(out / "training_mse.csv", meta + ("sample_index", "physical_time", "training_mse"),
        ({**trace, "sample_index": i, "physical_time": float(t), "training_mse": float(loss)}
         for trace in traces.values() for i, (t, loss) in enumerate(zip(trace["times"], trace["losses"]))))
    rms_bounds = log_bounds(row[f"{level}_rms"] for row in rows for level in LEVELS)
    loss_bounds = log_bounds(v for trace in traces.values()
                             for v in (float(trace["losses"].min()), float(trace["losses"].max())))
    axes = {}
    with PdfPages(out / "matched_network_rms_and_training_loss.pdf") as bundle:
        for case in CASES:
            draw_rms(rows, case, out, summary, rms_bounds, bundle)
            _, xmax = draw_losses(rows, traces, case, out, summary, loss_bounds, bundle)
            axes[case] = dict(rms_y=rms_bounds, loss_y=loss_bounds, time_x=[0, xmax])
    provenance = dict(command=[sys.executable, "-B", *sys.argv], cwd=str(Path.cwd()),
        source_hashes={str(Path(__file__).resolve()): digest(__file__)}, input_hashes=hashes,
        output_hashes={p.name: digest(p) for p in out.iterdir()},
        python=sys.version, numpy=np.__version__, matplotlib=matplotlib.__version__,
        analysis=str(owned(args.analysis)), comparison_rows=len(rows), selected_trajectories=len(traces),
        training_samples=sum(t["samples"] for t in traces.values()), axis_limits=axes,
        unresolved_cells={cell: p["reasons"] for cell, p in selection["cells"].items() if not p["valid"]},
        selection="Latest selected pair per cell, exactly as recorded in selected_levels.json",
        scientific_scope="Copies saved RMS and accepted-step time/MSE; no scientific recomputation or training",
        numerical_levels="Per-cell numerical levels; not seed uncertainty", full_reference="RMS=0 is excluded from logarithmic axis; full trajectories appear in every loss panel")
    (out / "provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    print(json.dumps({"out": str(out), "rows": len(rows), "traces": len(traces)}))


if __name__ == "__main__":
    main()
