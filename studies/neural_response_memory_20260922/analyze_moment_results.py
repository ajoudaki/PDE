"""Rerunnable, read-only analysis of the frozen orthogonal-moment campaign.

Reads only the three named study run roots, the local frozen recovery table,
and its selected dense endpoint archives. Writes only analysis01 products.
No model integration, fitting, source mutation, or archived state replay.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[2] /
                      "data/generated/neural_response_memory_20260922/analysis01/.mpl-cache"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / "studies/neural_response_memory_20260922"
GENERATED = ROOT / "data/generated/neural_response_memory_20260922"
RUN_ROOTS = ("orthogonal_primary01", "orthogonal_refined01", "orthogonal_fine01")
ORIGINAL_CASES = ("two_outliers_alternating", "quadrant_alternating", "quadrant_pairs")
CASES = ORIGINAL_CASES+("quadrant_center_edges", "equal_mixed_odd")
TITLES = {"two_outliers_alternating": "Two outliers, alternating labels",
          "quadrant_alternating": "One quadrant, alternating labels",
          "quadrant_pairs": "One quadrant, paired labels",
          "quadrant_center_edges": "One quadrant, center versus edges",
          "equal_mixed_odd": "Equal mixed odd (four antipodal representatives)"}
DENSE_ROOT = "data/generated/random_dictionary_learned_circle_20260920"
DENSE_PAIRS = {
    "two_outliers_alternating": ("scaling_discovery_primary01", "scaling_discovery_refined01"),
    "quadrant_alternating": ("diverse_refined01", "diverse_fine_early01"),
    "quadrant_pairs": ("scaling_discovery_primary01", "scaling_discovery_refined01"),
    "quadrant_center_edges": ("diverse_primary01", "diverse_refined01"),
    "equal_mixed_odd": ("diverse_primary01", "diverse_refined01"),
}
COLORS = {1: "#0072b2", 3: "#e69f00", 7: "#009e73", 15: "#cc79a7"}
SUBTITLE = "Width 2048; each model at its own training-MSE 0.001 endpoint; closure retains dense W0"
BUDGET_CAVEAT = "History/dictionary vector counts do not match total storage or compute; the response-moment closure retains dense W0."
LIMITS = dict(endpoint_max_difference=.01, activation_drift=.001,
              physical_mse_relative_error=.01, nested_grid_rms_difference=1e-5)


def relative(path):
    return str(path.relative_to(ROOT))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def array_digest(value):
    return hashlib.sha256(np.ascontiguousarray(value).tobytes()).hexdigest()


def rms(value):
    return float(np.sqrt(np.mean(np.square(value))))


def format_number(value):
    return "missing" if value is None else f"{value:.6g}"


def frozen_baselines():
    """Parse the literal n2048 table; preserve all unresolved flags."""
    result = []
    for line in (STUDY / "HARD_BENCHMARK_INPUTS.md").read_text().splitlines():
        cells = [item.strip() for item in line.strip().strip("|").split("|")]
        if len(cells) != 6 or not cells[0].startswith(("new_p", "old_p", "gaussian_p", "orthogonal_p")):
            continue
        method, order = cells[0].split("_p")
        for case, value in zip(ORIGINAL_CASES, cells[3:]):
            result.append(dict(case=case, method=method, order=int(order),
                               vectors=int(cells[2]), circle_rms=float(value.split()[0]),
                               valid="unresolved" not in value,
                               provenance="HARD_BENCHMARK_INPUTS.md: frozen final n2048 baseline table"))
    if len(result) != 39:
        raise ValueError("frozen baseline table was not parsed completely")
    additional = STUDY / "ADDITIONAL_BENCHMARK_INPUTS.md"
    if additional.exists():
        added = []
        for line in additional.read_text().splitlines():
            cells = [item.strip() for item in line.strip().strip("|").split("|")]
            if len(cells) != 7 or not cells[0].startswith(("new_p", "old_p", "gaussian_p", "orthogonal_p")):
                continue
            method, order = cells[0].split("_p")
            for case, primary, refined in (("quadrant_center_edges", cells[3], cells[4]),
                                           ("equal_mixed_odd", cells[5], cells[6])):
                added.append(dict(case=case, method=method, order=int(order), vectors=int(cells[2]),
                                  circle_rms=float(refined.split()[0]), primary_circle_rms=float(primary.split()[0]),
                                  valid="unresolved" not in refined,
                                  provenance="ADDITIONAL_BENCHMARK_INPUTS.md: frozen n2048 baseline table"))
        if len(added) != 26:
            raise ValueError("additional frozen baseline table was not parsed completely")
        result.extend(added)
    return result


def read_runs():
    runs, incomplete = {}, []
    for root_name in RUN_ROOTS:
        for path in sorted((GENERATED / root_name).glob("*/summary.json")):
            with path.open() as handle:
                summary = json.load(handle)
            if summary["variant"] != "orthogonal" or summary["case"] not in CASES:
                continue
            archive_path = path.with_name("arrays.npz")
            if not archive_path.exists():
                incomplete.append(relative(path))
                continue
            with np.load(archive_path, allow_pickle=False) as archive:
                arrays = {name: archive[name] for name in (
                    "endpoint_prediction", "endpoint_angles", "training_inputs", "labels",
                    "times", "losses", "snapshot_times", "matched_time_rms")}
            record = dict(summary=summary, arrays=arrays, summary_path=path,
                          archive_path=archive_path, summary_sha256=digest(path))
            runs.setdefault((summary["case"], summary["P"]), []).append(record)
    for values in runs.values():
        values.sort(key=lambda record: (-record["summary"]["rtol"], -record["summary"]["atol"],
                                        record["summary"]["level"], str(record["summary_path"])))
    return runs, incomplete


def read_reference(case):
    predictions, paths, hashes = [], [], []
    angles = None
    for run in DENSE_PAIRS[case]:
        path = ROOT / DENSE_ROOT / run / (case+"_full") / "arrays.npz"
        with np.load(path, allow_pickle=False) as archive:
            prediction, current_angles = archive["endpoint_prediction"], archive["endpoint_angles"]
        if angles is not None and not np.array_equal(angles, current_angles):
            raise ValueError("dense endpoint grids disagree")
        angles = current_angles
        paths.append(relative(path))
        predictions.append(prediction)
        hashes.append(array_digest(prediction))
    difference = predictions[1]-predictions[0]
    return dict(angles=angles, prediction=predictions[1], metadata=dict(
        coarser_archive=paths[0], selected_archive=paths[1], endpoint_prediction_sha256=hashes,
        endpoint_refinement_rms=rms(difference), endpoint_refinement_max=float(np.max(np.abs(difference))),
        interpretation="Observed dense numerical sensitivity; not a certified error bound."))


def activation_drift(summary):
    diagnostics = summary["diagnostics_final"]
    return max(float(diagnostics.get("h1_max", 0)), float(diagnostics.get("h2_max", 0)))


def endpoint_record(record, reference):
    summary, arrays = record["summary"], record["arrays"]
    if not np.array_equal(arrays["endpoint_angles"], reference["angles"]):
        raise ValueError("closure and dense endpoint grids differ")
    if summary["reference"] != reference["metadata"]["selected_archive"]:
        raise ValueError("run selected a different archived dense reference")
    error = arrays["endpoint_prediction"]-reference["prediction"]
    error_rms, nested_rms = rms(error), rms(error[::2])
    if not np.isclose(summary["circle_rms"], error_rms, atol=1e-12, rtol=1e-12):
        raise ValueError("saved summary RMS does not reproduce from predictions")
    physical_mse = float(summary["diagnostics_final"]["recomputed_loss"])
    drift = activation_drift(summary)
    gates = dict(fit_status=summary["status"] == "fit",
                 canonical_initialization=all(summary["initial_match"].values()),
                 endpoint_activation_drift=drift <= LIMITS["activation_drift"],
                 physical_mse=abs(physical_mse/.001-1) <= LIMITS["physical_mse_relative_error"],
                 nested_grid=abs(error_rms-nested_rms) <= LIMITS["nested_grid_rms_difference"])
    return dict(case=summary["case"], P=summary["P"], level=summary["level"],
                sample_count=summary["sample_count"],
                original_sample_count=summary.get("original_sample_count", summary["sample_count"]),
                antipodal_quotient=summary.get("antipodal_quotient", False),
                source=relative(record["summary_path"]), source_sha256=record["summary_sha256"],
                endpoint_prediction_sha256=array_digest(arrays["endpoint_prediction"]),
                rtol=summary["rtol"], atol=summary["atol"], status=summary["status"],
                time=summary["time"], lifted_training_mse=summary["training_mse"],
                physical_training_mse=physical_mse, endpoint_activation_drift=drift,
                activation_drift=None,
                h1_drift=summary["diagnostics_final"].get("h1_max"),
                h2_drift=summary["diagnostics_final"].get("h2_max"),
                maximum_saved_trajectory_drift=None,
                circle_rms=error_rms, circle_rms_4096=nested_rms,
                circle_sampled_max=float(np.max(np.abs(error))),
                nested_grid_rms_difference=abs(error_rms-nested_rms),
                history_vectors=summary["history_vectors"], history_rank_bound=summary["history_rank_bound"],
                moving_scalars=summary["moving_scalars"], fixed_W0_scalars=summary["fixed_W0_scalars"],
                activity=summary["activity"], accepted_steps=summary["accepted"],
                wall_seconds=summary["wall_seconds"],
                gates=gates,
                matched_times=arrays["snapshot_times"].tolist(),
                matched_time_rms=arrays["matched_time_rms"].tolist(),
                max_sampled_matched_time_rms=float(np.max(arrays["matched_time_rms"])))


def analyze(runs, references):
    selected, all_levels = [], []
    for (case, order), values in sorted(runs.items()):
        levels = []
        for value in values:
            row = endpoint_record(value, references[case])
            diagnostic_path = value["summary_path"].with_name("diagnostics.json")
            if diagnostic_path.exists():
                diagnostics = json.loads(diagnostic_path.read_text())
                complete = bool(diagnostics) and all(
                    all(name in item and np.isfinite(item[name]) for name in ("h1_max", "h2_max"))
                    for item in diagnostics)
                if complete:
                    row["maximum_saved_trajectory_drift"] = max(
                        max(item["h1_max"], item["h2_max"]) for item in diagnostics)
                    row["activation_drift"] = max(row["endpoint_activation_drift"], row["maximum_saved_trajectory_drift"])
            row["gates"]["trajectory_diagnostics_available"] = row["activation_drift"] is not None
            row["gates"]["activation_drift"] = (row["activation_drift"] is not None
                                                 and row["activation_drift"] <= LIMITS["activation_drift"])
            levels.append(row)
        row = dict(levels[-1])
        row["gates"] = dict(row["gates"])
        current = values[-1]
        previous_candidates = [value for value in values[:-1]
                               if value["summary"]["rtol"] > current["summary"]["rtol"]]
        row["previous_level_source"] = None
        row["endpoint_refinement_max"] = None
        row["endpoint_refinement_rms"] = None
        row["gates"].update(refinement_available=bool(previous_candidates),
                             endpoint_refinement=False, drift_decreases=False)
        if previous_candidates:
            previous = previous_candidates[-1]
            difference = current["arrays"]["endpoint_prediction"]-previous["arrays"]["endpoint_prediction"]
            row["previous_level_source"] = relative(previous["summary_path"])
            row["endpoint_refinement_max"] = float(np.max(np.abs(difference)))
            row["endpoint_refinement_rms"] = rms(difference)
            row["gates"]["endpoint_refinement"] = row["endpoint_refinement_max"] <= LIMITS["endpoint_max_difference"]
            previous_row = next(item for item in levels if item["source"] == row["previous_level_source"])
            row["gates"]["drift_decreases"] = (row["activation_drift"] is not None
                                                 and previous_row["activation_drift"] is not None
                                                 and row["activation_drift"] <= previous_row["activation_drift"])
        row["valid"] = all(row["gates"].values())
        row["failed_gates"] = [name for name, passed in row["gates"].items() if not passed]
        floor = references[case]["metadata"]["endpoint_refinement_rms"]
        row["dense_reference_refinement_rms"] = floor
        row["dense_refinement_to_closure_rms_ratio"] = floor/row["circle_rms"] if row["circle_rms"] else None
        row["dense_reference_sensitivity_comparable"] = floor >= row["circle_rms"]/3
        selected.append(row)
        all_levels.extend(levels)
    return selected, all_levels


def fresh_reference_analysis(runs, selected, archived):
    """Separate fresh-reference scores; never overwrite archived-target RMS."""
    grouped, records = {}, []
    for path in sorted((GENERATED / "dense_reference01").glob("*/summary.json")):
        summary = json.loads(path.read_text())
        case = summary.get("case", path.parent.name.split("_full_level")[0])
        if case not in archived or not path.with_name("arrays.npz").exists():
            continue
        with np.load(path.with_name("arrays.npz"), allow_pickle=False) as archive:
            prediction, angles = archive["endpoint_prediction"], archive["endpoint_angles"]
        if not np.array_equal(angles, archived[case]["angles"]):
            raise ValueError("fresh dense and archived circle grids disagree")
        record = dict(case=case, source=relative(path), source_sha256=digest(path),
                      rtol=summary["rtol"], atol=summary["atol"],
                      status=summary["status"], physical_loss=summary["loss"],
                      time=summary["time"], wall_seconds=summary["wall_seconds"],
                      initial_match=summary["initial_match"],
                      endpoint_prediction_sha256=array_digest(prediction),
                      arrays_sha256=summary.get("arrays_sha256"))
        records.append(record)
        grouped.setdefault(case, []).append((record, prediction))
    result = {}
    for case, levels in grouped.items():
        levels.sort(key=lambda item: -item[0]["rtol"])
        current, prediction = levels[-1]
        gates = dict(fit_status=current["status"] == "fitted",
                     canonical_initialization=all(current["initial_match"].values()),
                     physical_mse=abs(current["physical_loss"]/.001-1) <= .01,
                     refinement_available=len(levels) >= 2, endpoint_refinement=False)
        refinement_rms = refinement_max = None
        if len(levels) >= 2:
            difference = prediction-levels[-2][1]
            refinement_rms, refinement_max = rms(difference), float(np.max(np.abs(difference)))
            gates["endpoint_refinement"] = refinement_max <= .01
        result[case] = dict(selected_source=current["source"],
                            previous_source=levels[-2][0]["source"] if len(levels) >= 2 else None,
                            endpoint_refinement_rms=refinement_rms, endpoint_refinement_max=refinement_max,
                            selected_rtol=current["rtol"], gates=gates, valid=all(gates.values()),
                            rms_change_from_archived_target=rms(prediction-archived[case]["prediction"]),
                            interpretation="Fresh reference scores are separate from the archived-target historical comparisons.")
        for row in selected:
            if row["case"] != case:
                continue
            closure = runs[(case, row["P"])][-1]["arrays"]["endpoint_prediction"]
            difference = closure-prediction
            row["fresh_reference_circle_rms"] = rms(difference)
            row["fresh_reference_circle_rms_4096"] = rms(difference[::2])
            row["fresh_reference_circle_sampled_max"] = float(np.max(np.abs(difference)))
            row["fresh_reference_source"] = current["source"]
            row["fresh_reference_valid"] = (result[case]["valid"] and row["valid"]
                                            and abs(rms(difference)-rms(difference[::2])) <= 1e-5)
            row["fresh_reference_sensitivity_comparable"] = (refinement_rms is not None
                                                               and refinement_rms >= rms(difference)/3)
            sensitivities = [value for value in (row["endpoint_refinement_rms"], refinement_rms) if value is not None]
            row["numerical_sensitivity_max"] = max(sensitivities) if sensitivities else None
            row["numerical_sensitivity_comparable"] = (bool(sensitivities)
                                                         and max(sensitivities) >= rms(difference)/3)
            row["precision_comment"] = (
                "Refinement sensitivity is comparable to the fresh-reference discrepancy; passing gates does not resolve every reported digit."
                if row["numerical_sensitivity_comparable"] else
                "Observed closure/dense refinement sensitivity is below one third of the fresh-reference discrepancy; this is not a certified error bound.")
    return result, records


def save_figure(fig, directory, stem):
    fig.savefig(directory/(stem+".png"), dpi=180, bbox_inches="tight")
    fig.savefig(directory/(stem+".pdf"), bbox_inches="tight")
    plt.close(fig)


def panel_figure(cases, title):
    columns = min(len(cases), 3)
    rows = (len(cases)+columns-1)//columns
    fig, axes = plt.subplots(rows, columns, figsize=(6.0*columns, 4.6*rows), squeeze=False)
    fig.suptitle(title+"\n"+SUBTITLE, fontsize=12)
    fig.subplots_adjust(top=.87 if rows > 1 else .78, bottom=.1 if rows > 1 else .16, wspace=.25, hspace=.45)
    active = axes.flat[:len(cases)]
    for ax in axes.flat[len(cases):]:
        ax.set_visible(False)
    for ax, case in zip(active, cases):
        ax.set_title(TITLES[case], fontsize=11)
        ax.grid(True, alpha=.2)
    return fig, active


def plots(directory, runs, selected, references, baselines):
    cases = [case for case in CASES if case in references]
    rows = {(row["case"], row["P"]): row for row in selected}
    groups = {case: sorted((key for key in runs if key[0] == case), key=lambda key: key[1]) for case in cases}
    fig, axes = panel_figure(cases, "Training loss at each model's own endpoint")
    for ax, case in zip(axes, cases):
        for key in groups[case]:
            record, row = runs[key][-1], rows[key]
            color = COLORS.get(key[1], "#555555")
            label = f"P={key[1]}, level {row['level']}"+("" if row["valid"] else " [unresolved]")
            ax.semilogy(record["arrays"]["times"], record["arrays"]["losses"], color=color, label=label)
            ax.plot(row["time"], row["physical_training_mse"], "o", color=color, ms=4)
        ax.axhline(.001, color="black", lw=.8, ls=":")
        ax.set(xlabel="Physical time", ylabel="Lifted training MSE; endpoint dots: physical MSE")
        ax.legend(fontsize=8)
    save_figure(fig, directory, "loss_vs_time")

    fig, axes = panel_figure(cases, "Prediction error against dense gradient flow")
    method_styles = {"new": ("Derivative dictionary", "#666666", "s"),
                     "old": ("Action-word dictionary", "#9467bd", "^"),
                     "gaussian": ("Gaussian dictionary", "#bc6c25", "v"),
                     "orthogonal": ("Orthogonal dictionary", "#d45087", "D")}
    for ax, case in zip(axes, cases):
        for method, (label, color, marker) in method_styles.items():
            values = sorted((row for row in baselines if row["case"] == case and row["method"] == method), key=lambda row: row["vectors"])
            ax.semilogy([row["vectors"] for row in values], [row["circle_rms"] for row in values], color=color, lw=1, alpha=.7, label=label)
            for row in values:
                ax.plot(row["vectors"], row["circle_rms"], marker, color=color,
                        markerfacecolor=color if row["valid"] else "white", ms=5)
        values = [rows[key] for key in groups[case]]
        ax.semilogy([row["history_vectors"] for row in values], [row["circle_rms"] for row in values], color="#0072b2", lw=2.3, label="Response-moment closure")
        for row in values:
            ax.plot(row["history_vectors"], row["circle_rms"], "o", color="#0072b2", ms=7,
                    markerfacecolor="#0072b2" if row["valid"] else "white")
            ax.annotate(f"P={row['P']}"+("*" if row["dense_reference_sensitivity_comparable"] else ""),
                        (row["history_vectors"], row["circle_rms"]), xytext=(5, -13), textcoords="offset points", fontsize=8)
        floor = references[case]["metadata"]["endpoint_refinement_rms"]
        ax.axhline(floor, color="black", lw=.9, ls=":", label="Dense refinement RMS scale")
        ax.set(xlabel="History vectors or frozen dictionary vectors", ylabel="Circle RMS versus selected dense endpoint")
        ax.set_ylim(bottom=min(floor, min(row["circle_rms"] for row in values))/2)
    handles, labels = axes[0].get_legend_handles_labels()
    if len(fig.axes) > len(cases):
        note_ax = fig.axes[-1]
        note_ax.set_visible(True)
        note_ax.axis("off")
        note_ax.legend(handles, labels, loc="upper left", frameon=False, fontsize=10)
        note_ax.text(.025, .40,
                     "Vector counts do not match total storage or compute.\n\n"
                     "Hollow markers: unresolved numerical controls.\n\n"
                     "*: dense endpoint sensitivity is at least RMS / 3.\n"
                     "This is a numerical scale, not an error certificate.\n\n"
                     "The full circle has no target labels: curves measure\n"
                     "approximation to dense learning.",
                     transform=note_ax.transAxes, va="top", fontsize=10)
    else:
        fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(.5, .885), ncol=3, fontsize=8)
        fig.text(.5, .015, "Unequal total storage/compute. Hollow: unresolved. *: dense sensitivity at least RMS / 3.", ha="center", fontsize=8)
    save_figure(fig, directory, "rms_vs_vectors")

    fig, axes = panel_figure(cases, "Own-endpoint functions on the circle")
    for ax, case in zip(axes, cases):
        reference = references[case]
        ax.plot(np.rad2deg(reference["angles"]), reference["prediction"], color="black", lw=1.8, label="Selected dense endpoint")
        for key in groups[case]:
            record, row = runs[key][-1], rows[key]
            ax.plot(np.rad2deg(record["arrays"]["endpoint_angles"]), record["arrays"]["endpoint_prediction"],
                    color=COLORS.get(key[1], "#555555"), lw=1.2,
                    label=f"P={key[1]}"+("" if row["valid"] else " [unresolved]"))
        record = runs[groups[case][0]][-1]
        inputs = record["arrays"]["training_inputs"]
        angles = np.rad2deg(np.arctan2(inputs[:, 1], inputs[:, 0])) % 360
        ax.scatter(angles, record["arrays"]["labels"], c="black", marker="x", s=24, label="Training labels", zorder=5)
        ax.set(xlabel="Angle (degrees)", ylabel="Network output", xlim=(0, 360))
        ax.legend(fontsize=8)
    save_figure(fig, directory, "endpoint_functions")

    fig, axes = panel_figure(cases, "Stored matched-time circle RMS (2048-node snapshots)")
    for ax, case in zip(axes, cases):
        for key in groups[case]:
            row = rows[key]
            times, errors = np.asarray(row["matched_times"]), np.asarray(row["matched_time_rms"])
            usable = np.isfinite(errors) & (errors > 0)
            ax.semilogy(times[usable], errors[usable], "o-", ms=4, color=COLORS.get(key[1], "#555555"),
                        label=f"P={key[1]}"+("" if row["valid"] else " [unresolved]"))
        ax.set(xlabel="Physical time", ylabel="RMS versus archived dense at the same time")
        ax.legend(fontsize=8)
    save_figure(fig, directory, "matched_time_rms")


def fresh_reference_plot(directory, selected, archived, fresh):
    if not fresh:
        return
    cases = [case for case in CASES if case in archived]
    fig, axes = panel_figure(cases, "Response-moment closure: archived versus fresh dense targets")
    for ax, case in zip(axes, cases):
        rows = sorted((row for row in selected if row["case"] == case), key=lambda row: row["P"])
        ax.semilogy([row["history_vectors"] for row in rows], [row["circle_rms"] for row in rows],
                    "s--", color="#777777", ms=4, lw=1, label="Against archived dense target")
        available = [row for row in rows if "fresh_reference_circle_rms" in row]
        if available:
            ax.semilogy([row["history_vectors"] for row in available],
                        [row["fresh_reference_circle_rms"] for row in available],
                        color="#0072b2", lw=2, label="Against fresh refined dense target")
            for row in available:
                ax.plot(row["history_vectors"], row["fresh_reference_circle_rms"], "o", color="#0072b2",
                        markerfacecolor="#0072b2" if row["fresh_reference_valid"] else "white", ms=6)
                ax.annotate(f"P={row['P']}"+("*" if row["numerical_sensitivity_comparable"] else ""),
                            (row["history_vectors"], row["fresh_reference_circle_rms"]),
                            xytext=(4, -12), textcoords="offset points", fontsize=8)
            scale = fresh[case]["endpoint_refinement_rms"]
            if scale is not None:
                ax.axhline(scale, color="black", ls=":", lw=.9, label="Fresh dense refinement RMS scale")
        else:
            ax.text(.03, .04, "No fresh dense refinement available", transform=ax.transAxes, fontsize=8)
        ax.set(xlabel="History vectors", ylabel="Circle RMS against the named dense target")
        ax.margins(x=.12, y=.22)
    legend_axis = fig.axes[-1] if len(fig.axes) > len(cases) else None
    legend_handles, legend_labels = [], []
    for ax in axes:
        handles, labels = ax.get_legend_handles_labels()
        for handle, label in zip(handles, labels):
            if label not in legend_labels:
                legend_handles.append(handle)
                legend_labels.append(label)
    if legend_axis is not None:
        legend_axis.set_visible(True)
        legend_axis.axis("off")
        legend_axis.legend(legend_handles, legend_labels, loc="upper left", frameon=False, fontsize=10)
        legend_axis.text(.025, .55,
                         "This figure compares two numerical dense targets\n"
                         "for the same response-moment endpoints.\n\n"
                         "Frozen historical baseline errors remain tied to\n"
                         "the archived target in the main comparison.\n\n"
                         "*: max(closure, dense) refinement RMS is at least\n"
                         "one third of the fresh-target discrepancy.\n"
                         "Passing gates does not resolve every shown digit.\n\n"
                         "Hollow markers: fresh-reference or closure\n"
                         "numerical checks remain unresolved.",
                         transform=legend_axis.transAxes, va="top", fontsize=10)
    else:
        fig.legend(legend_handles, legend_labels, loc="upper center", bbox_to_anchor=(.5, .885), fontsize=8)
    save_figure(fig, directory, "fresh_reference_rms")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=str(GENERATED / "analysis01"))
    args = parser.parse_args()
    directory = Path(args.out).resolve()
    if directory != GENERATED / "analysis01":
        raise ValueError("this scoped helper writes only the assigned analysis01 directory")
    directory.mkdir(parents=True, exist_ok=True)
    runs, incomplete = read_runs()
    if not runs:
        raise ValueError("no completed moment outputs available")
    references = {case: read_reference(case) for case in CASES if any(key[0] == case for key in runs)}
    baselines = frozen_baselines()
    if any(case not in ORIGINAL_CASES for case in references) and not (STUDY / "ADDITIONAL_BENCHMARK_INPUTS.md").exists():
        raise ValueError("added cases require their frozen additional baseline input")
    selected, all_levels = analyze(runs, references)
    fresh_references, fresh_records = fresh_reference_analysis(runs, selected, references)
    missing_cells = [dict(case=case, P=order) for case in CASES for order in (1, 3, 7)
                     if (case, order) not in runs]
    payload = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                   selection="Finest available tolerance per cell; compared with nearest available coarser tolerance. No fallback to a prettier result.",
                   claim_scope="Realized trajectories and saved grids only; no asymptotic rate, statistical replication, or tracking theorem.",
                   budget_caveat=BUDGET_CAVEAT,
                   circle_metric="Difference from the selected dense model, not test-label error; circle labels are undefined.",
                   sample_budget="All cases use eight samples except equal_mixed_odd, whose exact four-representative antipodal quotient uses 8P history vectors rather than 16P.",
                   matched_time_metric="Producer-saved 2048-node snapshot differences; no independent dense trajectory replay in this analysis.",
                   dense_sensitivity_rule="Flag comparable when dense endpoint refinement RMS >= closure RMS/3; heuristic scale, not an error certificate.",
                   combined_sensitivity_rule="For fresh-reference scores, numerical_sensitivity_max=max(closure endpoint refinement RMS,dense endpoint refinement RMS); flag comparable at score/3. Passing validity gates does not resolve every displayed digit.",
                   gates=LIMITS, selected=selected, all_levels=all_levels, historical_baselines=baselines,
                   drift_gate="Maximum h1/h2 drift over every saved trajectory diagnostic and endpoint; finest level must pass and decrease versus previous level.",
                   integration_budget=dict(recorded_run_count=len(all_levels)+len(fresh_records),
                                           recorded_moment_run_count=len(all_levels),
                                           recorded_dense_run_count=len(fresh_records),
                                           recorded_total_run_count=len(all_levels)+len(fresh_records),
                                           recorded_wall_seconds=sum(row["wall_seconds"] for row in all_levels+fresh_records),
                                           trajectory_cap=44, wall_second_cap=3600,
                                           interpretation="Sum of producer-recorded integration wall_seconds; excludes plotting and short identity checks."),
                   dense_references={case: value["metadata"] for case, value in references.items()},
                   fresh_dense_references=fresh_references, fresh_dense_runs=fresh_records,
                   incomplete_summaries=incomplete,
                   missing_planned_cells=missing_cells,
                   source_sha256={"analysis_script": digest(Path(__file__)),
                                  "protocol": digest(STUDY / "MOMENT_EXPERIMENT_PROTOCOL.md"),
                                  "frozen_recovery": digest(STUDY / "HARD_BENCHMARK_INPUTS.md")})
    if (STUDY / "ADDITIONAL_BENCHMARK_INPUTS.md").exists():
        payload["source_sha256"]["additional_recovery"] = digest(STUDY / "ADDITIONAL_BENCHMARK_INPUTS.md")
    (directory / "metrics.json").write_text(json.dumps(payload, indent=2, allow_nan=False)+"\n")
    plots(directory, runs, selected, references, baselines)
    fresh_reference_plot(directory, selected, references, fresh_references)
    lines = ["# Moment campaign: current numerical selection", "", SUBTITLE+".", BUDGET_CAVEAT, "",
             "Finest available level per cell; `valid` means all stated numerical gates pass.", "",
             "| Case | P | Vectors | Level | Circle RMS | Refinement max | Sampled trajectory drift | Physical MSE | Valid |",
             "|---|---:|---:|---:|---:|---:|---:|---:|---|"]
    for row in selected:
        refinement = "missing" if row["endpoint_refinement_max"] is None else f"{row['endpoint_refinement_max']:.6g}"
        lines.append(f"| {row['case']} | {row['P']} | {row['history_vectors']} | {row['level']} | {row['circle_rms']:.8g} | {refinement} | {format_number(row['activation_drift'])} | {row['physical_training_mse']:.8g} | {row['valid']} |")
    lines += ["", "Primary drift failures retained:"]
    for row in all_levels:
        if row["level"] == 0 and not row["gates"]["activation_drift"]:
            lines.append(f"- {row['case']} P={row['P']}: sampled trajectory activation drift {format_number(row['activation_drift'])}; exceeds 0.001 or unavailable.")
    lines += ["", "Unresolved selected cells:"]
    for row in selected:
        if not row["valid"]:
            lines.append(f"- {row['case']} P={row['P']}: {', '.join(row['failed_gates'])}.")
    if all(row["valid"] for row in selected):
        lines.append("- None among currently available cells.")
    if missing_cells:
        lines += ["", "Planned cells without a saved endpoint:"]
        lines.extend(f"- {row['case']} P={row['P']}." for row in missing_cells)
    lines += ["", "Dense reference numerical sensitivity (not a certified error bound):"]
    for case, value in references.items():
        lines.append(f"- {case}: endpoint primary/refined RMS {value['metadata']['endpoint_refinement_rms']:.8g}.")
    if fresh_references:
        lines += ["", "Separate scores against fresh dense references (historical baseline scores above retain their archived target):", "",
                  "| Case | P | Archived-target RMS | Fresh-target RMS | Max refinement sensitivity | Comparable sensitivity | Checks pass |",
                  "|---|---:|---:|---:|---:|---|---|"]
        for row in selected:
            if "fresh_reference_circle_rms" in row:
                lines.append(f"| {row['case']} | {row['P']} | {row['circle_rms']:.8g} | {row['fresh_reference_circle_rms']:.8g} | {format_number(row['numerical_sensitivity_max'])} | {row['numerical_sensitivity_comparable']} | {row['fresh_reference_valid']} |")
        lines += ["", "Passing the numerical gates does not resolve every displayed digit. The sensitivity column is the larger of closure and dense endpoint-refinement RMS changes; it is an observed numerical scale, not a certified error bound."]
    lines += ["", "Maximum saved matched-time RMS (2048-node snapshots; no interpolation between saved comparison values):"]
    for row in selected:
        lines.append(f"- {row['case']} P={row['P']}: {row['max_sampled_matched_time_rms']:.8g}.")
    lines += ["", f"Recorded integration budget: {len(all_levels)} moment + {len(fresh_records)} fresh dense trajectories, {sum(row['wall_seconds'] for row in all_levels+fresh_records):.3f} summed wall-seconds; caps 44 trajectories / 3600 seconds."]
    lines += ["", "The equal_mixed_odd closure uses the exact four-representative antipodal quotient: history vectors are 8P; other cases use eight samples and 16P vectors. Dense W0 remains retained in every moment model."]
    lines += ["", "Circle differences are approximation errors against dense learning, not held-out label errors.",
              "Matched-time curves use producer-saved comparisons and do not constitute an independent trajectory replay."]
    (directory / "summary.md").write_text("\n".join(lines)+"\n")
    print(json.dumps(dict(output=relative(directory), cells=len(selected), valid=sum(row["valid"] for row in selected),
                          selected=[dict(case=row["case"], P=row["P"], level=row["level"], circle_rms=row["circle_rms"],
                                         valid=row["valid"], failed_gates=row["failed_gates"]) for row in selected]), indent=2))


if __name__ == "__main__":
    main()
