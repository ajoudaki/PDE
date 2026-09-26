"""Analyze frozen three-hidden-layer circle runs without evolving a network.

Usage: python -B analyze_deep_circle.py --runs PRIMARY [REFINED ...] --out FRESH
Pilots and repetitions are inventoried but excluded from scientific selection.
Predictions are scored as saved; independent checkpoint reconstruction belongs
to check_deep_circle.py. Refinement differences are sensitivities, not bounds.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import sys

import numpy as np


STUDY = Path(__file__).resolve().parent
MILESTONES = (.1, .03, .01, .003, .001)
MODELS = ("dense", "P1", "P2", "P3")
EXTRA_RTOL = 7.8125e-7
CASE_TITLES = {
    "two_outliers_alternating": "Two outliers, alternating",
    "quadrant_alternating": "Quadrant, alternating",
    "quadrant_pairs": "Quadrant, paired labels",
    "quadrant_center_edges": "Quadrant, center / edges",
    "equal_mixed_odd": "Equally spaced, mixed odd",
}
COLORS = {"dense": "#202124", "P1": "#D55E00", "P2": "#0072B2", "P3": "#009E73"}


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def add_array_hash(digest, value):
    value = np.ascontiguousarray(value)
    digest.update(str(value.shape).encode())
    digest.update(str(value.dtype).encode())
    digest.update(memoryview(value).cast("B"))


def array_hash(*values):
    digest = hashlib.sha256()
    for value in values:
        add_array_hash(digest, value)
    return digest.hexdigest()


def initialization_hash(width, seed):
    """Regenerate canonical draws in sequence, retaining at most one dense array."""
    rng = np.random.default_rng(seed)
    digest = hashlib.sha256()
    add_array_hash(digest, rng.standard_normal((width, 2)))
    for _ in range(2):
        add_array_hash(digest, rng.standard_normal((width, width)) / math.sqrt(width))
    add_array_hash(digest, rng.standard_normal(width) / width)
    return digest.hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def rms(value):
    return float(np.sqrt(np.mean(np.square(value))))


def read_json(path):
    return json.loads(Path(path).read_text())


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def write_csv(path, rows):
    keys = list(dict.fromkeys(key for row in rows for key in row))
    with Path(path).open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=keys)
        writer.writeheader()
        writer.writerows({key: json.dumps(value) if isinstance(value, (list, dict)) else value
                         for key, value in row.items()} for row in rows)


def excluded_phase(path, config):
    phase = str(config.get("phase", "")).lower()
    marker = " ".join((phase, str(config.get("run_id", "")).lower(), path.name.lower()))
    if any(word in marker for word in ("pilot", "reproduction", "repeat")):
        return "pilot or repeat; not a new scientific resolution"
    # A parent campaign name is also authoritative when the producer omitted phase.
    if any(any(word in parent.name.lower() for word in ("pilot", "reproduction"))
           for parent in path.parents if parent.name.startswith("deep_circle_")):
        return "pilot or reproduction campaign"
    return None


@dataclass
class Run:
    path: Path
    config: dict
    summary: dict
    case: str
    model: str
    observations: dict
    angles: np.ndarray
    times: np.ndarray
    losses: np.ndarray
    provenance: dict

    @property
    def rtol(self):
        return float(self.config["rtol"])


def source_file(path, roots, name, expected, hash_cache):
    require(Path(name).name == name, "source manifest must use plain filenames")
    candidates = []
    for parent in (path, *path.parents):
        if any(parent == root or root in parent.parents for root in roots):
            candidates.extend((parent / "source_snapshots" / name,
                               parent / "source_snapshots" / "source" / name))
    candidates.append(STUDY / name)
    for candidate in candidates:
        if not candidate.is_file():
            continue
        actual = hash_cache.setdefault(str(candidate), sha256(candidate))
        if actual == expected:
            return str(candidate.resolve())
    raise ValueError(f"No source file matches frozen digest for {name} in {path}")


def load_run(path, roots, cases, initial_hashes, hash_cache):
    config = read_json(path / "config.json")
    summary = read_json(path / "summary.json")
    manifest = read_json(path / "manifest.json")
    case = summary.get("case") or config.get("case") or config.get("case_id")
    require(case in cases, f"Unknown circle case in {path}: {case}")
    model = "dense" if config["model"] == "dense" else f"P{int(config['order'])}"
    require(model in MODELS, f"Unknown model in {path}")
    require(summary["model"] == config["model"], f"Model mismatch in {path}")
    require(summary["hidden_layers"] == 3 and summary["d"] == 2,
            f"Incorrect architecture in {path}")
    require(config["width"] == 4096 and config["seed"] == 20260920,
            f"Scientific run must use frozen width 4096 and seed 20260920: {path}")
    require(float(config["rtol"]) in (1.25e-5, 3.125e-6, EXTRA_RTOL),
            f"Unscheduled scientific tolerance in {path}")
    for key in ("width", "seed", "rtol", "atol", "query_count"):
        require(summary[key] == config[key], f"Config/summary {key} mismatch in {path}")
    require(config["query_count"] == 8192, f"Scientific panel must have 8192 points: {path}")
    require(summary["dtype"] == "float64", f"Unexpected scientific precision: {path}")
    require(float(config["atol"]) == float(config["rtol"]) / 100,
            f"Incorrect tolerance pairing in {path}")
    if model != "dense":
        require(summary["P"] == int(config["order"]), f"Order mismatch in {path}")
    cfg_hash = sha256(path / "config.json")
    require(summary["effective_config_sha256"] == cfg_hash,
            f"Effective config hash mismatch in {path}")
    for key in ("effective_config_sha256", "initialization_hash", "data_sha256",
                "query_sha256", "source_sha256"):
        require(manifest[key] == summary[key], f"Manifest/summary {key} mismatch in {path}")
    arr_hash = sha256(path / "arrays.npz")
    require(arr_hash == summary["arrays_sha256"], f"Array hash mismatch in {path}")
    init_key = (int(config["width"]), int(config["seed"]))
    if init_key not in initial_hashes:
        initial_hashes[init_key] = initialization_hash(*init_key)
    require(summary["initialization_hash"] == initial_hashes[init_key],
            f"Canonical initialization hash mismatch in {path}")
    sources = {name: source_file(path, roots, name, expected, hash_cache)
               for name, expected in summary["source_sha256"].items()}
    checkpoint_hashes = summary["checkpoint_sha256"]
    require(set(summary["checkpoints"]) == set(checkpoint_hashes),
            f"Checkpoint list/hash mismatch in {path}")
    for name, expected in checkpoint_hashes.items():
        require(Path(name).name == name, "Checkpoint must be a filename")
        require(sha256(path / name) == expected, f"Checkpoint hash mismatch: {path / name}")
    keys = ("circle_angles", "circle_inputs", "circle_predictions", "train_inputs",
            "train_labels", "train_predictions", "observation_times", "observation_training_mse",
            "observation_labels", "times", "losses", "accepted_steps", "local_error_ratios")
    with np.load(path / "arrays.npz", allow_pickle=False) as archive:
        arrays = {key: archive[key] for key in keys}
    for key, value in arrays.items():
        if value.dtype.kind in "biufc":
            require(np.isfinite(value).all(), f"Nonfinite {key} in {path}")
    inputs, labels = arrays["train_inputs"], arrays["train_labels"]
    require(np.array_equal(inputs, np.asarray(config["inputs"], dtype=np.float64))
            and np.array_equal(labels, np.asarray(config["labels"], dtype=np.float64)),
            f"Stored training arrays differ from configuration in {path}")
    case_angles = np.deg2rad(cases[case]["angles_degrees"])
    expected_inputs = np.column_stack((np.cos(case_angles), np.sin(case_angles)))
    require(inputs.shape == expected_inputs.shape and
            np.allclose(inputs, expected_inputs, rtol=0, atol=1e-14) and
            np.array_equal(labels, np.asarray(cases[case]["labels"])),
            f"Training data do not match the frozen case in {path}")
    require(len(inputs) == summary["sample_count"], f"Sample count mismatch in {path}")
    require(array_hash(inputs, labels) == summary["data_sha256"], f"Training hash mismatch in {path}")
    angles = 2 * np.pi * np.arange(8192) / 8192
    panel = np.column_stack((np.cos(angles), np.sin(angles)))
    require(np.array_equal(arrays["circle_angles"], angles) and
            np.array_equal(arrays["circle_inputs"], panel), f"Incorrect nested circle panel in {path}")
    require(array_hash(panel) == summary["query_sha256"], f"Query hash mismatch in {path}")
    count = len(arrays["observation_labels"])
    require(arrays["circle_predictions"].shape == (count, 8192) and
            arrays["train_predictions"].shape == (count, len(labels)),
            f"Observation shapes mismatch in {path}")
    require(len(summary["observations"]) == count, f"Observation record count mismatch in {path}")
    times, losses = arrays["times"], arrays["losses"]
    require(len(times) == len(losses) == len(arrays["accepted_steps"]) + 1,
            f"Accepted trace sizes mismatch in {path}")
    require(len(arrays["local_error_ratios"]) == len(times) - 1 and
            np.all(np.diff(times) > 0) and np.all(arrays["accepted_steps"] > 0) and
            np.all(arrays["local_error_ratios"] <= 1 + 1e-12) and
            np.all(arrays["local_error_ratios"] >= 0), f"Invalid accepted trace in {path}")
    require(np.allclose(np.diff(times), arrays["accepted_steps"], rtol=1e-11, atol=1e-11),
            f"Accepted times/steps mismatch in {path}")
    require(float(times[-1]) == summary["time"] and float(losses[-1]) == summary["training_mse"],
            f"Final trace/summary mismatch in {path}")
    observations = {}
    for index, label in enumerate(arrays["observation_labels"].tolist()):
        require(label not in observations, f"Duplicate observation {label} in {path}")
        record = summary["observations"][index]
        loss = float(np.mean(np.square(arrays["train_predictions"][index] - labels)))
        stored_loss = float(arrays["observation_training_mse"][index])
        require(record["label"] == label and record["time"] == float(arrays["observation_times"][index]),
                f"Observation metadata mismatch in {path}")
        require(abs(loss - stored_loss) <= 2e-11 * max(1., abs(loss)) and
                abs(loss - float(record["training_mse"])) <= 2e-11 * max(1., abs(loss)),
                f"Saved physical loss mismatch in {path}")
        observations[label] = {"time": float(record["time"]), "physical_mse": loss,
                               "prediction": arrays["circle_predictions"][index]}
        if label.startswith("loss_"):
            checkpoint = "checkpoint_" + label.replace(".", "p") + ".npz"
            require(checkpoint in checkpoint_hashes, f"Missing checkpoint for {label} in {path}")
            with np.load(path / checkpoint, allow_pickle=False) as saved:
                require(float(saved["physical_time"]) == float(record["time"]) and
                        abs(float(saved["training_mse"]) - loss) <= 2e-11,
                        f"Checkpoint scalar metadata mismatch: {path / checkpoint}")
    found_losses = sorted((float(label[5:]) for label in observations if label.startswith("loss_")), reverse=True)
    require(found_losses == summary["crossed_losses"], f"Crossing inventory mismatch in {path}")
    return Run(path, config, summary, case, model, observations, angles, times, losses,
               dict(summary_sha256=sha256(path / "summary.json"), config_sha256=cfg_hash,
                    manifest_sha256=sha256(path / "manifest.json"), arrays_sha256=arr_hash,
                    source_paths=sources, source_sha256=summary["source_sha256"],
                    checkpoint_sha256=checkpoint_hashes, initialization_hash=summary["initialization_hash"],
                    data_sha256=summary["data_sha256"], query_sha256=summary["query_sha256"]))


def milestone_label(loss):
    return "loss_" + format(loss, ".12g")


def gate_comparison(case, order, loss, selected):
    model = f"P{order}"
    fine, previous = selected[(case, model)]
    dense, dense_previous = selected[(case, "dense")]
    label = milestone_label(loss)
    if label not in fine.observations or label not in dense.observations:
        return None
    a, b = fine.observations[label], dense.observations[label]
    difference = a["prediction"] - b["prediction"]
    error = rms(difference)
    nested = rms(difference[::2])
    old_a = previous.observations.get(label) if previous else None
    old_b = dense_previous.observations.get(label) if dense_previous else None
    closure_change = rms(a["prediction"] - old_a["prediction"]) if old_a else None
    dense_change = rms(b["prediction"] - old_b["prediction"]) if old_b else None
    physical = {"closure_fine": a["physical_mse"], "dense_fine": b["physical_mse"],
                "closure_previous": old_a["physical_mse"] if old_a else None,
                "dense_previous": old_b["physical_mse"] if old_b else None}
    gates = {
        "closure_refinement_available": closure_change is not None,
        "dense_refinement_available": dense_change is not None,
        "closure_absolute": closure_change is not None and closure_change <= .005,
        "dense_absolute": dense_change is not None and dense_change <= .005,
        "closure_relative": closure_change is not None and closure_change <= .1 * error,
        "dense_relative": dense_change is not None and dense_change <= .1 * error,
        "grid": abs(error - nested) <= 1e-5,
        "physical_loss": all(value is not None and abs(value / loss - 1) <= .01
                             for value in physical.values()),
    }
    passed = all(gates.values())
    return dict(case=case, P=order, milestone=loss, closure_run=str(fine.path),
                dense_run=str(dense.path), closure_previous=str(previous.path) if previous else None,
                dense_previous=str(dense_previous.path) if dense_previous else None,
                closure_rtol=fine.rtol, dense_rtol=dense.rtol,
                closure_previous_rtol=previous.rtol if previous else None,
                dense_previous_rtol=dense_previous.rtol if dense_previous else None,
                rms_8192=error, rms_4096=nested, nested_grid_change=abs(error - nested),
                closure_refinement_rms=closure_change, dense_refinement_rms=dense_change,
                combined_sensitivity=closure_change + dense_change
                if closure_change is not None and dense_change is not None else None,
                closure_time=a["time"], dense_time=b["time"], physical_losses=physical,
                numerical_gates=gates, numerical_pass=passed,
                failed_gates=[name for name, value in gates.items() if not value],
                measured_coarse_agreement=error <= .1,
                scientific_verdict=("coarse_agreement" if error <= .1 else "coarse_disagreement")
                if passed else "numerically_inconclusive")


def select_runs(runs):
    groups = {}
    for run in runs:
        groups.setdefault((run.case, run.model), []).append(run)
    selected = {}
    for key, values in groups.items():
        values.sort(key=lambda run: run.rtol)
        require(len({run.rtol for run in values}) == len(values),
                f"Duplicate scientific resolution for {key}; exclude repeats or choose roots explicitly")
        selected[key] = (values[0], values[1] if len(values) > 1 else None)
    return selected


def common_milestones(case, selected):
    if any((case, model) not in selected for model in MODELS):
        return []
    return [loss for loss in MILESTONES if all(
        run is not None and milestone_label(loss) in run.observations
        for model in MODELS for run in selected[(case, model)])]


def refinement_decisions(comparisons, selected):
    requests = {}
    for row in comparisons:
        for model, prefix in ((f"P{row['P']}", "closure"), ("dense", "dense")):
            # Missing primary evidence is inconclusive, not a measured tolerance
            # failure authorizing the next, third numerical resolution.
            if not row["numerical_gates"][prefix + "_refinement_available"]:
                continue
            reasons = [name for name in row["failed_gates"] if name.startswith(prefix + "_")]
            physical_keys = [prefix + "_fine", prefix + "_previous"]
            if any(row["physical_losses"][key] is not None and
                   abs(row["physical_losses"][key] / row["milestone"] - 1) > .01
                   for key in physical_keys):
                reasons.append("physical_loss")
            if not reasons:
                continue
            key = (row["case"], model)
            request = requests.setdefault(key, dict(case=key[0], model=model, reasons=[]))
            request["reasons"].append(dict(milestone=row["milestone"], comparison_P=row["P"], gates=reasons))
    for key, request in requests.items():
        fine, _ = selected[key]
        request.update(finest_executed_rtol=fine.rtol, source_run=str(fine.path),
                       requested_rtol=EXTRA_RTOL, requested_atol=EXTRA_RTOL / 100,
                       conditional_run_available=fine.rtol > EXTRA_RTOL * (1 + 1e-12),
                       action="one_predeclared_refinement" if fine.rtol > EXTRA_RTOL * (1 + 1e-12)
                       else "unresolved_after_allowed_refinement")
    return sorted(requests.values(), key=lambda row: (row["case"], MODELS.index(row["model"])))


def order_comparisons(comparisons):
    rows = []
    indexed = {(row["case"], row["milestone"], row["P"]): row for row in comparisons}
    for case, loss in sorted({(row["case"], row["milestone"]) for row in comparisons}):
        for lower, higher in ((1, 2), (1, 3), (2, 3)):
            a, b = indexed.get((case, loss, lower)), indexed.get((case, loss, higher))
            if not a or not b:
                continue
            gap = a["rms_8192"] - b["rms_8192"]
            margin = (a["combined_sensitivity"] + b["combined_sensitivity"]
                      if a["combined_sensitivity"] is not None and b["combined_sensitivity"] is not None else None)
            resolved = (a["numerical_pass"] and b["numerical_pass"] and margin is not None and abs(gap) > margin)
            rows.append(dict(case=case, milestone=loss, lower_P=lower, higher_P=higher,
                             lower_minus_higher_rms=gap, summed_observed_sensitivity=margin,
                             both_numerical_gates_pass=a["numerical_pass"] and b["numerical_pass"],
                             resolved=resolved,
                             verdict=("higher_order_improves" if gap > 0 else "higher_order_worsens")
                             if resolved else "unresolved"))
    return rows


def inventory_row(run):
    summary = run.summary
    row = dict(case=run.case, model=run.model, path=str(run.path), rtol=run.rtol,
               atol=run.config["atol"], width=summary["width"], M=summary["sample_count"],
               status=summary["status"], target_reached=milestone_label(.001) in run.observations,
               final_time=summary["time"], final_training_mse=summary["training_mse"],
               accepted=summary["accepted"], rejected=summary["rejected"],
               crossed_losses=summary["crossed_losses"])
    for key, value in summary.items():
        if any(token in key for token in ("seconds", "bytes", "scalars", "rank")) and isinstance(value, (int, float)):
            row[key] = value
    if "moving_state_bytes" in summary and "fixed_hidden_bytes" in summary:
        row["moving_plus_fixed_bytes"] = summary["moving_state_bytes"] + summary["fixed_hidden_bytes"]
    return row


def make_plots(out, cases, selected, endpoints, comparisons):
    os.environ.setdefault("MPLCONFIGDIR", str(out / ".matplotlib"))
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "axes.titlesize": 11, "axes.labelsize": 10, "legend.fontsize": 9,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "axes.linewidth": .7, "grid.alpha": .22, "pdf.fonttype": 42,
                         "savefig.dpi": 300})
    case_order = list(cases)
    index = {(row["case"], row["milestone"], row["P"]): row for row in comparisons}
    artifacts = []

    def save(fig, stem):
        for extension in ("png", "pdf"):
            filename = stem + "." + extension
            fig.savefig(out / filename, bbox_inches="tight", facecolor="white")
            artifacts.append(filename)
        plt.close(fig)

    fig, ax = plt.subplots(figsize=(9.6, 5.6))
    palette = ("#0072B2", "#D55E00", "#009E73", "#CC79A7", "#E69F00")
    has_data = False
    for number, case in enumerate(case_order):
        loss = endpoints[case]["selected_common_milestone"]
        if loss is None:
            continue
        rows = [index.get((case, loss, order)) for order in (1, 2, 3)]
        xs, ys = [row["P"] for row in rows if row], [max(row["rms_8192"], 1e-16) for row in rows if row]
        if not xs:
            continue
        has_data = True
        label = CASE_TITLES[case] + (f" (MSE {loss:g})" if loss != .001 else "")
        ax.plot(xs, ys, color=palette[number], lw=1.4, alpha=.8, label=label)
        for row in rows:
            if row:
                ax.plot(row["P"], max(row["rms_8192"], 1e-16), "o", ms=6.5,
                        color=palette[number], markerfacecolor=palette[number] if row["numerical_pass"] else "white",
                        markeredgewidth=1.4)
    ax.set(xticks=[1, 2, 3], xlabel="Retained history modes P", ylabel="Circle prediction RMS from dense",
           title="Three hidden tanh layers, width 4096 · each model at its own loss crossing")
    ax.set_yscale("log")
    ax.grid(axis="y", which="both", linewidth=.6)
    if has_data:
        ax.legend(loc="best", frameon=False)
    else:
        ax.text(.5, .5, "No common saved loss milestone", transform=ax.transAxes, ha="center")
    fig.text(.5, .01, "Filled markers pass all numerical gates; hollow markers remain unresolved.\n"
             "One common finest dense reference per task. No asymptotic order rate is implied.",
             ha="center", fontsize=9, color="#555555")
    fig.subplots_adjust(bottom=.18)
    save(fig, "rms_vs_order")

    handles = [Line2D([0], [0], color=COLORS[model], lw=1.8, label=model.replace("P", "P=")) for model in MODELS]
    for kind in ("function_curves", "endpoint_differences", "loss_trajectories"):
        fig, axes = plt.subplots(3, 2, figsize=(11.4, 10.2))
        for ax, case in zip(axes.flat, case_order):
            loss = endpoints[case]["selected_common_milestone"]
            ax.set_title(CASE_TITLES[case], loc="left", fontweight="medium")
            if kind == "loss_trajectories":
                for model in MODELS:
                    pair = selected.get((case, model))
                    if pair:
                        run = pair[0]
                        ax.plot(run.times, np.maximum(run.losses, 1e-18), color=COLORS[model], lw=1.4)
                        if run.summary["status"] != "target_loss":
                            ax.plot(run.times[-1], max(run.losses[-1], 1e-18), "x", color=COLORS[model], ms=7)
                ax.set_yscale("log")
                ax.axhline(.001, color="#999999", ls=":", lw=.8)
                ax.set(xlabel="Physical training time", ylabel="Training MSE")
            elif loss is None:
                ax.text(.5, .5, "No common saved loss milestone", transform=ax.transAxes, ha="center")
                ax.set(xlabel="Input direction (degrees)", ylabel="Prediction")
            else:
                label = milestone_label(loss)
                dense = selected[(case, "dense")][0]
                reference = dense.observations[label]["prediction"]
                degree = np.rad2deg(dense.angles)
                for model in MODELS:
                    if kind == "endpoint_differences" and model == "dense":
                        continue
                    run = selected[(case, model)][0]
                    prediction = run.observations[label]["prediction"]
                    value = prediction - reference if kind == "endpoint_differences" else prediction
                    ax.plot(degree, value, color=COLORS[model], lw=1.2 if model != "dense" else 1.8,
                            alpha=.9, zorder=2 if model != "dense" else 3)
                if kind == "function_curves":
                    angles = cases[case].get("original_angles_degrees", cases[case]["angles_degrees"])
                    labels = cases[case].get("original_labels", cases[case]["labels"])
                    ax.scatter(angles, labels, s=28, c="#171717", edgecolors="white", linewidths=.6, zorder=4)
                else:
                    ax.axhline(0, color="#666666", lw=.7, zorder=0)
                ax.set(xlim=(0, 360), xticks=[0, 90, 180, 270, 360], xlabel="Input direction (degrees)",
                       ylabel="Closure minus dense" if kind == "endpoint_differences" else "Prediction")
                ax.text(.97, .96, f"Own MSE {loss:g}" + (" · fallback milestone" if loss != .001 else ""),
                        transform=ax.transAxes, ha="right", va="top", fontsize=8, color="#666666")
            ax.grid(linewidth=.6)
        axes.flat[-1].set_axis_off()
        axes.flat[-1].legend(handles=handles if kind != "endpoint_differences" else handles[1:],
                             loc="center", frameon=False, ncol=2)
        axes.flat[-1].text(.5, .2, "Black points: original training labels" if kind == "function_curves" else
                          ("Crosses mark capped/unfinished trajectories" if kind == "loss_trajectories" else
                           "Differences use one finest dense reference"),
                          transform=axes.flat[-1].transAxes, ha="center", fontsize=9, color="#555555")
        fig.suptitle({"function_curves": "Functions on the circle at matched training loss",
                      "endpoint_differences": "Prediction differences on the circle",
                      "loss_trajectories": "Training loss along each finest numerical trajectory"}[kind],
                     y=.985, fontsize=15)
        fig.tight_layout(rect=[0, 0, 1, .96], h_pad=2, w_pad=2)
        save(fig, kind)
    return artifacts


def analyze(roots, out):
    roots = [Path(root).resolve() for root in roots]
    out = Path(out).resolve()
    require(not out.exists(), f"Output must be a fresh directory: {out}")
    cases = read_json(STUDY / "deep_circle_cases.json")
    configs = sorted({path.resolve().parent for root in roots for path in root.rglob("config.json")})
    require(configs, "No run config.json files found")
    initial_hashes, hash_cache, runs, unavailable = {}, {}, [], []
    for path in configs:
        config = read_json(path / "config.json")
        excluded = excluded_phase(path, config)
        if excluded:
            unavailable.append(dict(path=str(path), status="excluded", reason=excluded))
            continue
        if not (path / "summary.json").is_file():
            failure = read_json(path / "failure.json") if (path / "failure.json").is_file() else None
            unavailable.append(dict(path=str(path), status="failed" if failure else "incomplete",
                                    case=config.get("case", config.get("case_id")), model=config.get("model"),
                                    P=config.get("order"), rtol=config.get("rtol"), failure=failure))
            continue
        runs.append(load_run(path, roots, cases, initial_hashes, hash_cache))
    require(runs, "No completed scientific runs found; exclusions/failures cannot define a comparison")
    # Every comparison must share the model definition, initialization, and query panel.
    baseline = runs[0]
    for run in runs[1:]:
        for key in ("initialization_hash", "query_sha256", "source_sha256"):
            require(run.provenance[key] == baseline.provenance[key], f"Campaign-wide {key} differs: {run.path}")
        if run.case == baseline.case:
            require(run.provenance["data_sha256"] == baseline.provenance["data_sha256"], "Training data differ within case")
    for case in cases:
        same_case = [run for run in runs if run.case == case]
        require(len({run.provenance["data_sha256"] for run in same_case}) <= 1, f"Training data differ for {case}")
    selected = select_runs(runs)
    comparisons, endpoints, endpoint_rows, missing = [], {}, [], []
    for case in cases:
        present = [model for model in MODELS if (case, model) in selected]
        absent = [model for model in MODELS if model not in present]
        common = common_milestones(case, selected)
        endpoint = min(common) if common else None
        endpoints[case] = dict(common_milestones=common, selected_common_milestone=endpoint,
                               primary_mse_001_jointly_reached=.001 in common, missing_models=absent,
                               endpoint_interpretation="primary_matched_loss" if endpoint == .001 else
                               ("earlier_common_milestone_not_primary_endpoint" if endpoint else "no_common_endpoint"))
        for model in absent:
            missing.append(dict(case=case, model=model, reason="no completed scientific run"))
        for order in (1, 2, 3):
            if (case, "dense") not in selected or (case, f"P{order}") not in selected:
                continue
            for loss in MILESTONES:
                row = gate_comparison(case, order, loss, selected)
                if row:
                    comparisons.append(row)
                    if loss == endpoint:
                        endpoint_row = dict(row)
                        for prefix, model in (("closure", f"P{order}"), ("dense", "dense")):
                            selected_run = selected[(case, model)][0]
                            endpoint_row[prefix + "_status"] = selected_run.summary["status"]
                            endpoint_row[prefix + "_integration_wall_seconds"] = selected_run.summary["integration_with_observations_seconds"]
                            for name in ("moving_state_bytes", "fixed_hidden_bytes", "peak_cuda_allocated_bytes"):
                                endpoint_row[prefix + "_" + name] = selected_run.summary.get(name)
                        endpoint_rows.append(endpoint_row)
                else:
                    missing.append(dict(case=case, model=f"P{order}", milestone=loss,
                                        reason="finest closure or finest dense lacks the crossing"))
    requests = refinement_decisions(comparisons, selected)
    available_resolutions = {(run.case, run.model, run.rtol) for run in runs}
    primary_complete = all((case, model, rtol) in available_resolutions
                           for case in cases for model in MODELS for rtol in (1.25e-5, 3.125e-6))
    for request in requests:
        request["provisional_until_primary_inventory_complete"] = not primary_complete
    order_rows = order_comparisons(comparisons)
    inventory = [inventory_row(run) for run in runs]
    resources = dict(scientific_trajectories=len(runs),
                     failed_or_incomplete=len([item for item in unavailable if item["status"] != "excluded"]),
                     integration_with_observations_seconds=sum(run.summary["integration_with_observations_seconds"] for run in runs),
                     integration_excluding_observations_seconds=sum(run.summary["integration_seconds_excluding_observations"] for run in runs),
                     capped_or_unfitted=[str(run.path) for run in runs if run.summary["status"] != "target_loss"],
                     scope="Only supplied completed science runs; pilot/repeat and failed-process time belongs to campaign receipt")
    out.mkdir(parents=True, exist_ok=False)
    artifacts = make_plots(out, cases, selected, endpoints, comparisons)
    result = dict(schema_version=1, architecture="three hidden tanh layers", width=baseline.summary["width"],
                  analysis_status="primary_inventory_complete" if primary_complete else "partial_primary_inventory",
                  primary_inventory_complete=primary_complete,
                  refinement_decisions_provisional=not primary_complete,
                  run_roots=[str(root) for root in roots], endpoints=endpoints, comparisons=comparisons,
                  endpoint_comparisons=endpoint_rows, order_comparisons=order_rows,
                  refinement_requests=requests,
                  required_refinements=[item for item in requests if item["conditional_run_available"]],
                  unresolved_after_refinement=[item for item in requests if not item["conditional_run_available"]],
                  missing_comparisons=missing, unavailable_or_excluded=unavailable, run_inventory=inventory,
                  selected={case: {model: dict(finest=str(selected[(case, model)][0].path),
                                previous=str(selected[(case, model)][1].path) if selected[(case, model)][1] else None)
                                for model in MODELS if (case, model) in selected} for case in cases},
                  resources=resources, provenance={str(run.path): run.provenance for run in runs},
                  source_sha256={name: sha256(STUDY / name) for name in
                                 ("analyze_deep_circle.py", "deep_circle_cases.json", "DEEP_CIRCLE_PROTOCOL.md")},
                  environment=dict(python=sys.version, numpy=np.__version__, platform=platform.platform()),
                  command=sys.argv, figures=artifacts,
                  caveats=["Each model is compared at its own loss crossing, not at a common physical time.",
                           "Observed refinement changes are sensitivities, not rigorous error bars or confidence intervals.",
                           "Saved predictions and hashes are checked; full independent checkpoint reconstruction is a separate audit.",
                           "No numerical order trend establishes hierarchy convergence or width-uniform accuracy."])
    write_json(out / "metrics_summary.json", result)
    write_json(out / "refinement_requests.json", dict(provisional=not primary_complete,
               required=result["required_refinements"],
               exhausted=result["unresolved_after_refinement"], all_requests=requests,
               missing_comparisons=missing))
    write_csv(out / "comparison_metrics.csv", comparisons)
    write_csv(out / "endpoint_metrics.csv", endpoint_rows)
    write_csv(out / "order_comparisons.csv", order_rows)
    write_csv(out / "run_inventory.csv", inventory)
    lines = ["# Three-hidden-layer circle analysis" + (" — partial inventory" if not primary_complete else ""), "",
             "Own-loss endpoints; one common finest dense reference per task. Numerical sensitivities are not certified error bounds.", "",
             "| Task | Common MSE | P1 RMS | P2 RMS | P3 RMS | Numerical gates P1/P2/P3 |", "|---|---:|---:|---:|---:|---|"]
    for case in cases:
        loss = endpoints[case]["selected_common_milestone"]
        rows = {row["P"]: row for row in endpoint_rows if row["case"] == case}
        values = [f"{rows[p]['rms_8192']:.9g}" if p in rows else "unavailable" for p in (1, 2, 3)]
        gates = ["pass" if rows[p]["numerical_pass"] else "unresolved" if p in rows else "unavailable" for p in (1, 2, 3)] if len(rows) == 3 else ["unavailable"] * 3
        lines.append(f"| {case} | {loss if loss is not None else 'unavailable'} | " + " | ".join(values) + " | " + "/".join(gates) + " |")
    lines.extend(["", f"Completed scientific trajectories: {len(runs)}. Capped or unfitted: {len(resources['capped_or_unfitted'])}.",
                  "Primary inventory complete: " + ("yes." if primary_complete else "no; all branch decisions remain provisional."),
                  f"Summed integration wall time including observations: {resources['integration_with_observations_seconds']:.3f} seconds.",
                  f"Predeclared additional refinements requested: {len(result['required_refinements'])}.",
                  f"Unresolved after the allowed refinement: {len(result['unresolved_after_refinement'])}.", "",
                  "| Task | Model | Finest rtol | Status | Stop time | Integration wall seconds | Moving MiB | Fixed hidden MiB | CUDA peak MiB |",
                  "|---|---|---:|---|---:|---:|---:|---:|---:|"])
    for case in cases:
        for model in MODELS:
            if (case, model) not in selected:
                continue
            run = selected[(case, model)][0]
            record = run.summary
            sizes = [f"{record[name] / (1 << 20):.3f}" if name in record else "unavailable"
                     for name in ("moving_state_bytes", "fixed_hidden_bytes", "peak_cuda_allocated_bytes")]
            lines.append(f"| {case} | {model} | {run.rtol:g} | {record['status']} | {record['time']:.5f} | "
                         f"{record['integration_with_observations_seconds']:.3f} | " + " | ".join(sizes) + " |")
    lines.extend(["",
                  "Timing, storage, peak allocations, statuses and limits are recorded per run in run_inventory.csv.",
                  "All milestone scores, physical-loss/grid/refinement gates, selection provenance and unresolved comparisons are retained in metrics_summary.json.",
                  "A common milestone above .001 is explicitly a fallback observation, not a fitted primary endpoint.", ""])
    (out / "summary.md").write_text("\n".join(lines))
    write_json(out / "artifact_manifest.json", {path.name: sha256(path) for path in sorted(out.iterdir()) if path.is_file()})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs", nargs="+", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    result = analyze(args.runs, args.out)
    print(json.dumps(dict(output=str(Path(args.out).resolve()), runs=result["resources"]["scientific_trajectories"],
                          analysis_status=result["analysis_status"],
                          comparisons=len(result["comparisons"]), required_refinements=len(result["required_refinements"]),
                          unresolved=len(result["unresolved_after_refinement"])), indent=2))


if __name__ == "__main__":
    main()
