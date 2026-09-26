#!/usr/bin/env python3
"""Presentation-only summary of frozen activation-circle analyzer outputs.

Read the given metrics file and only the finest summaries explicitly selected
there. Do not recompute gates, select trajectories, or substitute fallback RMS.
The output directory must be fresh. No training dependencies are imported.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.patches import Rectangle
from matplotlib.ticker import LogFormatterMathtext


ACTIVATIONS = (("relu", "ReLU"), ("gelu", "GELU"),
               ("selu", "SELU"), ("sigmoid", "Sigmoid"))
TASKS = (("two_outliers_alternating", "Outliers"),
         ("quadrant_alternating", "Quadrant"))
CASES = [(f"{a}__{t}", a, t, f"{label}  /  {task_label}")
         for a, label in ACTIVATIONS for t, task_label in TASKS]
MODELS = ("dense", "P1", "P2", "P3")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def finite_nonnegative(value, name: str) -> float:
    result = float(value)
    require(math.isfinite(result) and result >= 0, f"Invalid {name}: {value}")
    return result


def load_cells(metrics_path: Path):
    raw = metrics_path.read_bytes()
    metrics = json.loads(raw)
    require(metrics.get("width") == 4096, "Expected frozen width 4096")
    case_names = {case for case, *_ in CASES}
    require(set(metrics["selected"]) == case_names, "Expected all eight selected-case entries")
    primary = {}
    for row in metrics["primary_comparisons"]:
        key = (row["case"], row["P"])
        require(key not in primary, f"Duplicate primary comparison: {key}")
        require(row.get("comparison_type") == "primary_matched_loss"
                and row.get("milestone") == .001, f"Not a primary .001 comparison: {key}")
        primary[key] = row
    require(set(primary) == {(case, p) for case in case_names for p in (1, 2, 3)},
            "Expected exactly 24 primary comparison entries")

    rms_cells, loss_cells, summary_hashes, initializations = [], [], {}, set()
    for case, activation, task, label in CASES:
        selected = metrics["selected"][case]
        require(set(selected).issubset(MODELS), f"Unknown model in {case}")
        for p in (1, 2, 3):
            row = primary[case, p]
            require(row.get("activation") == activation and row.get("task") == task,
                    f"Primary metadata mismatch: {case}, P{p}")
            cell = dict(case=case, model=f"P{p}", available=bool(row["available"]),
                        numerical_pass=bool(row["numerical_pass"]),
                        failed_gates=row.get("failed_gates", []), reason=row.get("reason"))
            if cell["available"]:
                require("dense" in selected and f"P{p}" in selected,
                        f"Available primary has no selected pair: {case}, P{p}")
                require(row["dense_run"] == selected["dense"]["finest"]
                        and row["closure_run"] == selected[f"P{p}"]["finest"],
                        f"Primary does not use selected common dense: {case}, P{p}")
                cell["value"] = finite_nonnegative(row["rms_8192"], "primary RMS")
            rms_cells.append(cell)

        for model in MODELS:
            cell = dict(case=case, model=model, available=model in selected)
            if cell["available"]:
                run = selected[model]["finest"]
                summary_path = Path(run) / "summary.json"
                summary_raw = summary_path.read_bytes()
                summary_hash = digest(summary_raw)
                require(summary_hash == metrics["provenance"][run]["summary_sha256"],
                        f"Selected summary changed since analysis: {summary_path}")
                summary = json.loads(summary_raw)
                require(all(summary.get(k) == v for k, v in
                            (("case", case), ("activation", activation), ("task", task),
                             ("width", 4096), ("hidden_layers", 3), ("seed", 20260920))),
                        f"Selected summary metadata mismatch: {summary_path}")
                require((summary.get("model"), summary.get("P")) ==
                        (("dense", None) if model == "dense" else ("moment", int(model[1:]))),
                        f"Selected model mismatch: {summary_path}")
                initializations.add(summary["initialization_hash"])
                cell.update(value=finite_nonnegative(summary["training_mse"], "final MSE"),
                            time=finite_nonnegative(summary["time"], "final time"),
                            status=summary["status"], rtol=summary["rtol"],
                            run=run, summary_sha256=summary_hash)
                summary_hashes[str(summary_path.resolve())] = summary_hash
            loss_cells.append(cell)
    require(len(initializations) <= 1, "Selected runs do not share one initialization")
    provisional = (not metrics.get("primary_schedule_complete", False)
                   or metrics.get("refinement_decisions_provisional", True)
                   or bool(metrics.get("required_refinements")))
    manifest = dict(schema_version=1, metrics_path=str(metrics_path.resolve()),
                    metrics_sha256=digest(raw),
                    inherited_analysis_source_sha256=metrics.get("source_sha256", {}),
                    selected_summary_sha256=summary_hashes,
                    initialization_hashes=sorted(initializations),
                    analysis_status=metrics.get("analysis_status"), provisional=provisional,
                    primary_schedule_complete=metrics.get("primary_schedule_complete"),
                    finished_primary_attempts=metrics.get("finished_primary_attempts"),
                    scheduled_primary_attempts=metrics.get("scheduled_primary_attempts"),
                    required_refinements=metrics.get("required_refinements", []),
                    row_order=[dict(case=case, label=label) for case, _, _, label in CASES],
                    primary_cells=rms_cells, final_loss_cells=loss_cells,
                    scope="Presentation only; analyzer selection and primary numerical gates retained verbatim.")
    return manifest


def bounds(cells, default_upper):
    values = [c["value"] for c in cells if c["available"]]
    # Shared fixed lower endpoint makes the two panels easy to read. Values
    # outside the default range expand it by whole decades; zero stays explicit.
    positive = [v for v in values if v > 0]
    # Bisection can put .001 crossings just below the decimal threshold; this
    # display-only rounding prevents an empty additional color-scale decade.
    low = min(1e-3, 10 ** math.floor(math.log10(min(positive)) + 1e-10)) if positive else 1e-3
    high = max(default_upper, 10 ** math.ceil(math.log10(max(positive)) - 1e-10)) if positive else default_upper
    return low, high


def text_color(rgba):
    return "#182331" if sum(w * c for w, c in zip((.2126, .7152, .0722), rgba)) > .55 else "white"


def draw_panel(ax, cells, columns, norm, cmap, final_loss=False):
    for i, cell in enumerate(cells):
        row, col = divmod(i, len(columns))
        color = cmap(norm(max(cell["value"], norm.vmin))) if cell["available"] else "#e5e7ea"
        ax.add_patch(Rectangle((col, row), 1, 1, facecolor=color, edgecolor="white", linewidth=2))
        if not cell["available"]:
            ax.text(col + .5, row + .5, "unavailable" if not final_loss else "no selected run",
                    ha="center", va="center", fontsize=9, color="#606975")
            continue
        foreground = text_color(color)
        value = f"{cell['value']:.3g}"
        if final_loss:
            ax.text(col + .5, row + .35, value, ha="center", va="center",
                    fontsize=11, color=foreground, weight="semibold")
            ax.text(col + .5, row + .69, f"t = {cell['time']:.3g}", ha="center", va="center",
                    fontsize=8.5, color=foreground)
        else:
            unresolved = not cell["numerical_pass"]
            if unresolved:
                ax.add_patch(Rectangle((col + .03, row + .03), .94, .94,
                                       fill=False, hatch="///", edgecolor=foreground, linewidth=1.2))
            ax.text(col + .5, row + .5, value + (" †" if unresolved else ""),
                    ha="center", va="center", fontsize=12, color=foreground,
                    weight="semibold", bbox=dict(facecolor=color, edgecolor="none", pad=2))
    ax.set(xlim=(0, len(columns)), ylim=(8, 0), xticks=[i + .5 for i in range(len(columns))],
           xticklabels=columns, yticks=[i + .5 for i in range(8)])
    ax.tick_params(axis="x", top=True, labeltop=True, bottom=False, labelbottom=False, length=0, pad=8)
    ax.tick_params(axis="y", length=0, pad=12)
    for y in (2, 4, 6):
        ax.axhline(y, color="#8893a1", linewidth=1)
    for spine in ax.spines.values():
        spine.set_visible(False)


def render(manifest, out: Path):
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "pdf.fonttype": 42, "ps.fonttype": 42})
    fig = plt.figure(figsize=(12.8, 8.4), facecolor="white")
    left = fig.add_axes((.205, .275, .315, .505))
    right = fig.add_axes((.565, .275, .41, .505))
    rms_bounds = bounds(manifest["primary_cells"], 10)
    loss_bounds = bounds(manifest["final_loss_cells"], 1)
    rms_norm, loss_norm = LogNorm(*rms_bounds), LogNorm(*loss_bounds)
    cmap = plt.get_cmap("viridis_r")
    draw_panel(left, manifest["primary_cells"], ("P1", "P2", "P3"), rms_norm, cmap)
    draw_panel(right, manifest["final_loss_cells"], ("Dense", "P1", "P2", "P3"), loss_norm, cmap, True)
    left.set_yticklabels([label for _, _, _, label in CASES], fontsize=10.5)
    right.set_yticklabels([])
    fig.text(.205, .84, "PRIMARY · circle prediction RMS", fontsize=12, weight="bold")
    fig.text(.565, .84, "Final training MSE · finest selected runs", fontsize=12, weight="bold")
    fig.text(.205, .812, "Each trajectory at its own MSE = 0.001 crossing", fontsize=9.5, color="#526071")
    fig.text(.565, .812, "Physical final times differ; t shown in each cell", fontsize=9.5, color="#526071")
    fig.text(.035, .944, "Activation and moment-closure summary", fontsize=20, weight="bold", color="#192534")
    status = (f"PROVISIONAL · {manifest['finished_primary_attempts']} / "
              f"{manifest['scheduled_primary_attempts']} primary attempts finished"
              if manifest["provisional"] else
              f"{manifest['finished_primary_attempts']} / {manifest['scheduled_primary_attempts']} primary attempts finished")
    if manifest["provisional"] and manifest["required_refinements"]:
        status += " · refinement pending"
    fig.text(.035, .897, status, fontsize=11, weight="bold", color="#835000" if manifest["provisional"] else "#526071")
    for x, width, norm, label in ((.205, .315, rms_norm, "Circle RMS · logarithmic color scale"),
                                  (.565, .41, loss_norm, "Training MSE · logarithmic color scale")):
        axis = fig.add_axes((x, .212, width, .018))
        bar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), cax=axis,
                           orientation="horizontal", format=LogFormatterMathtext())
        bar.ax.tick_params(labelsize=9, length=3)
        bar.set_label(label, fontsize=9, labelpad=4)
    caption = (
        "Gray: primary comparison unavailable, or no selected final run.  † + hatching: primary numerical gates unresolved.\n"
        "Width 4096 · 3 hidden layers · one shared initialization. RMS on 8192 circle points versus the same-activation,\n"
        "same-task finest dense reference; dense and closure use their own MSE = 0.001 crossings. No fallback RMS is shown.\n"
        "Outliers = two-outlier alternating labels; Quadrant = quadrant alternating labels. Final MSE is descriptive at each\n"
        "run's stopping time. Fixed scaling and budgets; this is not an activation-optimized ranking or a convergence claim."
    )
    fig.text(.035, .025, caption, fontsize=9.2, color="#425164", linespacing=1.55, va="bottom")
    manifest["caption"] = caption
    manifest["normalization"] = dict(cmap="viridis_r", primary_rms=list(rms_bounds),
                                      final_training_mse=list(loss_bounds),
                                      zero_color="lower endpoint; exact zero remains printed as 0")
    manifest["figure_layout"] = dict(rows=8, primary_columns=3, final_loss_columns=4)
    outputs = {}
    for suffix in ("png", "pdf"):
        path = out / f"activation_circle_summary.{suffix}"
        fig.savefig(path, dpi=220, facecolor="white")
        outputs[path.name] = digest(path.read_bytes())
    plt.close(fig)
    manifest["figure_sha256"] = outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--metrics", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True, help="Fresh output directory")
    args = parser.parse_args()
    require(not args.out.exists(), f"Output already exists: {args.out}")
    manifest = load_cells(args.metrics)
    manifest.update(source_path=str(Path(__file__).resolve()),
                    source_sha256=digest(Path(__file__).read_bytes()),
                    command=sys.argv, matplotlib_version=matplotlib.__version__)
    args.out.mkdir(parents=True)
    render(manifest, args.out)
    (args.out / "figure_manifest.json").write_text(json.dumps(manifest, indent=2, allow_nan=False) + "\n")
    print(json.dumps(dict(output=str(args.out.resolve()), provisional=manifest["provisional"],
                          primary_available=sum(c["available"] for c in manifest["primary_cells"]),
                          final_runs_available=sum(c["available"] for c in manifest["final_loss_cells"])), indent=2))


if __name__ == "__main__":
    main()
