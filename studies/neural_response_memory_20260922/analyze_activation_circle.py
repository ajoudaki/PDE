"""Rescore saved activation-circle runs; never evolve a network.

Usage: python -B analyze_activation_circle.py --runs ROOT [ROOT ...] --out FRESH
Primary .001 comparisons are pairwise. Common-loss fallbacks and common-time
diagnostics stay separate. A finished primary schedule may contain failures;
only integrity-validated completed trajectories enter scientific comparisons.
"""

from __future__ import annotations

import argparse
from dataclasses import replace
import json
import os
from pathlib import Path
import platform
import sys
import zipfile

import numpy as np

import analyze_deep_circle as core


STUDY = Path(__file__).resolve().parent
MILESTONES = (.9, .5, .1, .03, .01, .003, .001)
TIMES = (10., 100., 1000.)
PRIMARY_RTOLS = (1.25e-5, 3.125e-6)
MODELS = core.MODELS
ACTIVATIONS = ("relu", "gelu", "selu", "sigmoid")
DIAGNOSTIC_KEYS = tuple(f"feature_motion_h{layer}_rms" for layer in (1, 2, 3)) + (
    "w_motion_rms", "c_motion_rms", "activation_diagnostics")
SOURCES = ("analyze_activation_circle.py", "analyze_deep_circle.py",
           "ACTIVATION_CIRCLE_PROTOCOL.md", "activation_circle_cases.json", "run_activation_circle_campaign.py")
PRODUCER_SOURCES = {"activation_circle_run.py", "activation_moment_engine.py",
                    "deep_moment_engine.py", "moment_engine.py"}
FAST_PRODUCER_SOURCES = PRODUCER_SOURCES | {"activation_circle_fast_run.py", "activation_fast_engine.py"}
CAMPAIGN_SOURCES = PRODUCER_SOURCES | {"ACTIVATION_CIRCLE_PROTOCOL.md", "activation_circle_cases.json",
                                       "run_activation_circle_campaign.py"}
CONTROLS = dict(initial_step=.05, max_step=2., max_time=10000., max_steps=30000,
                max_wall_seconds=300., threads=1, bisection_iterations=32, target_loss=.001)


def time_label(value):
    return "time_" + format(value, ".12g")


def case_metadata(config, cases, summary=None, manifest=None):
    case = config.get("case", config.get("case_id"))
    core.require(case in cases, f"Unknown literal activation case: {case}")
    literal = cases[case]
    core.require(case == literal["activation"] + "__" + literal["task"],
                 "Literal composite case is inconsistent")
    for label, record in (("config", config), ("summary", summary), ("manifest", manifest)):
        if record is None:
            continue
        core.require(record.get("case", record.get("case_id")) == case,
                     f"{label} composite case mismatch")
        for key in ("activation", "task"):
            core.require(record.get(key) == literal[key], f"{label} {key} mismatch for {case}")
    core.require(config.get("model") in ("dense", "moment"), "Unknown physical model")
    model = "dense" if config["model"] == "dense" else f"P{config.get('order')}"
    core.require(model in MODELS, "Unscheduled moment order")
    return case, model


def finite_diagnostics(value, name):
    if isinstance(value, dict):
        for key, child in value.items():
            finite_diagnostics(child, name + "." + key)
    else:
        core.require(isinstance(value, (int, float)) and np.isfinite(value),
                     f"Nonfinite or nonnumeric diagnostic {name}")


def validate_config(config):
    for name, value in CONTROLS.items():
        core.require(config.get(name) == value, f"Frozen scientific control mismatch: {name}")
    core.require(tuple(config["milestones"]) == MILESTONES and
                 tuple(config["observation_times"]) == TIMES,
                 "Scientific observation schedule differs from frozen protocol")
    tol, phase = float(config["rtol"]), config.get("phase")
    core.require((tol in PRIMARY_RTOLS and phase == "primary") or
                 (tol == core.EXTRA_RTOL and phase == "refine"),
                 "Scientific phase/tolerance is not in the frozen schedule")


def campaign_provenance(path, roots, config, summary, hash_cache):
    """Check a supplied campaign's frozen manifest when present; standalone fixtures are allowed."""
    records = []
    for parent in path.parents:
        if not any(parent == root or root in parent.parents for root in roots):
            continue
        target = parent / "manifest.json"
        if not target.is_file():
            continue
        manifest = core.read_json(target)
        core.require(manifest.get("phase") == config["phase"], "Campaign phase mismatch")
        source_hashes = manifest.get("source_sha256", {})
        core.require(set(source_hashes) == CAMPAIGN_SOURCES, "Campaign frozen source set mismatch")
        for name, expected in source_hashes.items():
            current = hash_cache.setdefault(str(STUDY / name), core.sha256(STUDY / name))
            core.require(current == expected, f"Campaign frozen source digest mismatch: {name}")
            if name in PRODUCER_SOURCES:
                core.require(summary["source_sha256"][name] == expected, "Campaign/run producer digest mismatch")
        records.append(dict(path=str(target), sha256=core.sha256(target), phase=manifest["phase"],
                            source_sha256=source_hashes))
    return records


def validate_observations(run):
    """Validate chronological event metadata and scalar checkpoints, including time events."""
    records = run.summary["observations"]
    core.require(records and records[0]["label"] == "initial" and records[-1]["label"] == "final",
                 "Observations must start with initial and end with final")
    record_times = np.asarray([record["time"] for record in records])
    core.require(np.isfinite(record_times).all() and np.all(np.diff(record_times) >= 0),
                 "Observation records are not chronological")
    core.require(record_times[0] == run.times[0] == 0 and record_times[-1] == run.times[-1],
                 "Observation endpoint times differ from accepted trace")
    observed_times = []
    for record in records:
        label = record["label"]
        if label.startswith("loss_"):
            loss = float(label[5:])
            core.require(loss in MILESTONES and label == core.milestone_label(loss),
                         "Unscheduled loss event")
            core.require(record.get("kind") == "loss" and record.get("requested_loss") == loss
                         and record.get("requested_time") is None, "Loss event request mismatch")
        elif label.startswith("time_"):
            requested = float(label[5:])
            core.require(requested in TIMES and label == time_label(requested), "Unscheduled time event")
            core.require(record.get("kind") == "time" and record.get("requested_time") == requested
                         and record.get("requested_loss") is None and record["time"] == requested,
                         "Time event request mismatch")
            if run.summary["status"] == "target_loss":
                core.require(requested < run.summary["time"], "Time event is not before fitted stopping event")
            observed_times.append(requested)
        else:
            core.require(label in ("initial", "final") and record.get("kind") == label
                         and record.get("requested_time") is None
                         and record.get("requested_loss") is None, "Unknown observation kind")
        if label.startswith(("loss_", "time_")):
            checkpoint = "checkpoint_" + label.replace(".", "p") + ".npz"
            core.require(checkpoint in run.summary["checkpoint_sha256"], "Event checkpoint missing")
            with np.load(run.path / checkpoint, allow_pickle=False) as saved:
                core.require(saved["physical_time"].shape == () and saved["training_mse"].shape == (),
                             "Checkpoint time/loss metadata must be scalar")
                core.require(float(saved["physical_time"]) == record["time"] and
                             abs(float(saved["training_mse"]) - record["training_mse"]) <= 2e-11,
                             "Event checkpoint scalar metadata mismatch")
        for key in DIAGNOSTIC_KEYS:
            core.require(key in record, f"Missing diagnostic {key}")
            finite_diagnostics(record[key], key)
        core.require(set(record["activation_diagnostics"]) == {"layer1", "layer2", "layer3"},
                     "Activation diagnostics must cover every hidden layer")
        run.observations[label].update({key: record[key] for key in
                                       ("kind", "requested_time", "requested_loss", *DIAGNOSTIC_KEYS)})
    core.require(observed_times == run.summary["observed_physical_times"], "Time event inventory mismatch")


def load_run(path, roots, cases, initial_hashes, hash_cache):
    config, summary, manifest = (core.read_json(path / name) for name in
                                  ("config.json", "summary.json", "manifest.json"))
    case_metadata(config, cases, summary, manifest)
    validate_config(config)
    core.require(summary.get("phase") == manifest.get("phase") == config["phase"], "Phase metadata mismatch")
    core.require(set(summary["source_sha256"]) in (PRODUCER_SOURCES, FAST_PRODUCER_SOURCES), "Frozen producer source set mismatch")
    if set(summary["source_sha256"]) == FAST_PRODUCER_SOURCES:
        core.require(config.get("execution_backend") in ("graphs", "batched_graphs") and
                     config["execution_backend"] == summary.get("execution_backend") == manifest.get("execution_backend"),
                     "Fast execution backend provenance mismatch")
    campaigns = campaign_provenance(path, roots, config, summary, hash_cache)
    run = core.load_run(path, roots, cases, initial_hashes, hash_cache)
    # Hashes preserve provenance; ZIP CRC validation additionally catches damaged members.
    for name in ("arrays.npz", *summary["checkpoints"]):
        with zipfile.ZipFile(path / name) as archive:
            core.require(archive.testzip() is None, f"Archive CRC failure: {path / name}")
    validate_observations(run)
    run.provenance.update(campaign_manifests=campaigns, campaign_manifest_status="validated" if campaigns else
                          "absent; standalone run/fixture checked using per-run provenance")
    return run


def excluded_phase(path, config):
    reason = core.excluded_phase(path, config)
    if reason:
        return reason
    if any(parent.name.startswith("activation_circle_") and
           any(word in parent.name.lower() for word in ("pilot", "repeat", "reproduction"))
           for parent in path.parents):
        return "pilot or reproduction campaign"
    return None


def enrich(row, cases, selected, label, comparison_type, unusable_refinements=None):
    row.update(activation=cases[row["case"]]["activation"], task=cases[row["case"]]["task"],
               comparison_type=comparison_type, available=True)
    for prefix, model in (("closure", f"P{row['P']}"), ("dense", "dense")):
        run = selected[(row["case"], model)][0]
        row[prefix + "_status"] = run.summary["status"]
        row[prefix + "_final_training_mse"] = run.summary["training_mse"]
        row[prefix + "_final_time"] = run.summary["time"]
        for key in DIAGNOSTIC_KEYS:
            row[prefix + "_" + key] = run.observations[label].get(key)
        if (row["case"], model) in (unusable_refinements or {}):
            gate = prefix + "_additional_resolution_unavailable"
            row["numerical_gates"][gate] = False
            row["failed_gates"].append(gate)
            row["numerical_pass"] = False
            row["scientific_verdict"] = "numerically_inconclusive"
    return row


def matched_time_comparison(case, order, requested, selected):
    """Reuse the numerical scorer with event aliases, then replace its loss gate."""
    label, alias = time_label(requested), core.milestone_label(requested)
    views = {}
    for model in ("dense", f"P{order}"):
        pair = selected.get((case, model))
        if not pair:
            return None
        views[(case, model)] = tuple(replace(run, observations={alias: run.observations[label]}
                                            if label in run.observations else {}) if run else None
                                     for run in pair)
    row = core.gate_comparison(case, order, requested, views)
    if row is None:
        return None
    row.pop("milestone")
    row["requested_time"] = requested
    gates = row["numerical_gates"]
    gates.pop("physical_loss")
    gates["physical_time"] = all(run is not None and label in run.observations and
                                 run.observations[label]["time"] == requested and
                                 run.observations[label].get("requested_time") == requested
                                 for model in ("dense", f"P{order}") for run in selected[(case, model)])
    row["failed_gates"] = [name for name, value in gates.items() if not value]
    row["numerical_pass"] = all(gates.values())
    row["scientific_verdict"] = "matched_time_diagnostic" if row["numerical_pass"] else "numerically_inconclusive"
    return row


def comparison_tables(cases, selected, unusable_refinements=None):
    comparisons, primary, fallback, time_rows, missing, endpoints = [], [], [], [], [], {}
    for case, literal in cases.items():
        models = [model for model in MODELS if (case, model) in selected]
        common = [loss for loss in MILESTONES if len(models) == 4 and all(
            core.milestone_label(loss) in selected[(case, model)][0].observations for model in MODELS)]
        fallback_loss = min(common) if common and .001 not in common else None
        endpoints[case] = dict(common_milestones=common, selected_common_milestone=min(common) if common else None,
                               fallback_common_milestone=fallback_loss,
                               primary_available_orders=[], missing_models=[m for m in MODELS if m not in models])
        for order in (1, 2, 3):
            rows = {}
            if "dense" in models and f"P{order}" in models:
                for loss in MILESTONES:
                    row = core.gate_comparison(case, order, loss, selected)
                    if row:
                        rows[loss] = enrich(row, cases, selected, core.milestone_label(loss), "matched_loss", unusable_refinements)
                        comparisons.append(row)
                for requested in TIMES:
                    row = matched_time_comparison(case, order, requested, selected)
                    if row:
                        time_rows.append(enrich(row, cases, selected, time_label(requested), "matched_time_diagnostic", unusable_refinements))
                    else:
                        missing.append(dict(case=case, P=order, requested_time=requested,
                                            reason="finest dense or closure lacks time event"))
            for loss in MILESTONES:
                if loss not in rows:
                    missing.append(dict(case=case, P=order, milestone=loss,
                                        reason="finest dense or closure run/crossing unavailable"))
            if .001 in rows:
                primary.append(dict(rows[.001], comparison_type="primary_matched_loss"))
                endpoints[case]["primary_available_orders"].append(order)
            else:
                primary.append(dict(case=case, activation=literal["activation"], task=literal["task"], P=order,
                                    milestone=.001, comparison_type="primary_matched_loss", available=False,
                                    numerical_pass=False, scientific_verdict="primary_unavailable",
                                    reason="finest dense or closure lacks .001 crossing"))
            if fallback_loss in rows:
                fallback.append(dict(rows[fallback_loss], comparison_type="fallback_common_loss_not_primary"))
        endpoints[case]["primary_mse_001_jointly_reached"] = len(endpoints[case]["primary_available_orders"]) == 3
        endpoints[case]["plot_milestone"] = .001 if endpoints[case]["primary_available_orders"] else fallback_loss
    return comparisons, primary, fallback, time_rows, missing, endpoints


def schedule_status(cases, attempts, runs):
    expected = {(case, model, tol) for case in cases for model in MODELS for tol in PRIMARY_RTOLS}
    finished = {(row["case"], row["model"], row["rtol"]) for row in attempts
                if row.get("finished") and row.get("case") in cases and row.get("model") in MODELS}
    valid = {(run.case, run.model, run.rtol) for run in runs}
    return dict(primary_schedule_complete=expected <= finished, primary_inventory_complete=expected <= valid,
                scheduled_primary_attempts=len(expected), finished_primary_attempts=len(expected & finished),
                valid_primary_trajectories=len(expected & valid),
                unfinished_primary_keys=[dict(case=c, model=m, rtol=t) for c, m, t in sorted(expected - finished)],
                invalid_or_missing_primary_keys=[dict(case=c, model=m, rtol=t) for c, m, t in sorted(expected - valid)])


def refinement_decisions(comparisons, selected, schedule_complete, attempts=()):
    if not schedule_complete:
        return []
    # A missing crossing/resolution is inconclusive, not a measured tolerance failure.
    shared = [dict(row, failed_gates=[gate for gate in row["failed_gates"]
                                    if not gate.endswith("additional_resolution_unavailable")])
              for row in comparisons if all(row["numerical_gates"][prefix + "_refinement_available"]
                                            for prefix in ("dense", "closure"))]
    requests = {(row["case"], row["model"]): row for row in core.refinement_decisions(shared, selected)}
    # The protocol requires a third dense resolution alongside a third closure
    # resolution, even when the previous dense sensitivity passed on its own.
    for key, request in list(requests.items()):
        if key[1] == "dense" or not request["conditional_run_available"]:
            continue
        dense_key = (key[0], "dense")
        dense = selected[dense_key][0]
        if dense.rtol <= core.EXTRA_RTOL:
            continue
        paired = requests.setdefault(dense_key, dict(case=key[0], model="dense", reasons=[],
            finest_executed_rtol=dense.rtol, source_run=str(dense.path), requested_rtol=core.EXTRA_RTOL,
            requested_atol=core.EXTRA_RTOL / 100, conditional_run_available=True,
            action="one_predeclared_refinement"))
        paired["reasons"].append(dict(gates=["paired_dense_required_by_protocol"], closure_model=key[1]))
    # A failed/pending additional attempt consumes/reserves the only permitted
    # extra resolution. Never silently retry it using older valid comparisons.
    for attempt in attempts:
        if attempt.get("rtol") != core.EXTRA_RTOL or attempt.get("valid_scientific_run"):
            continue
        key = (attempt.get("case"), attempt.get("model"))
        request = requests.setdefault(key, dict(case=key[0], model=key[1], reasons=[],
            finest_executed_rtol=selected[key][0].rtol if key in selected else None,
            source_run=str(selected[key][0].path) if key in selected else None,
            requested_rtol=core.EXTRA_RTOL, requested_atol=core.EXTRA_RTOL / 100))
        request.update(conditional_run_available=False, additional_attempt=attempt["path"],
            additional_attempt_status=attempt["status"], action="unresolved_after_failed_refinement"
            if attempt.get("finished") else "additional_refinement_in_progress")
        request["reasons"].append(dict(gates=["additional_resolution_unavailable"], status=attempt["status"]))
    return sorted(requests.values(), key=lambda row: (row["case"], MODELS.index(row["model"])))


def make_plots(out, cases, selected, primary, endpoints, comparisons):
    os.environ.setdefault("MPLCONFIGDIR", str(out / ".matplotlib"))
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9, "pdf.fonttype": 42,
                         "axes.spines.top": False, "axes.spines.right": False, "savefig.dpi": 180})
    artifacts, panel_counts = [], {}
    index = {(row["case"], row["milestone"], row["P"]): row for row in comparisons}

    def save(fig, name):
        panel_counts[name] = len(fig.axes)
        for suffix in ("png", "pdf"):
            target = name + "." + suffix
            fig.savefig(out / target, bbox_inches="tight", facecolor="white")
            artifacts.append(target)
        plt.close(fig)

    for kind in ("rms_vs_order", "function_curves", "endpoint_differences", "loss_trajectories"):
        fig, axes = plt.subplots(4, 2, figsize=(12, 13.2), squeeze=False)
        for ax, (case, literal) in zip(axes.flat, cases.items()):
            loss = endpoints[case]["plot_milestone"]
            title = literal["activation"].upper() + " · " + core.CASE_TITLES[literal["task"]]
            ax.set_title(title, loc="left", fontsize=10)
            if kind == "loss_trajectories":
                for model in MODELS:
                    if (case, model) not in selected:
                        continue
                    run = selected[(case, model)][0]
                    ax.plot(run.times, np.maximum(run.losses, 1e-18), color=core.COLORS[model], lw=1.3)
                    if run.summary["status"] != "target_loss":
                        ax.plot(run.times[-1], max(run.losses[-1], 1e-18), "x", color=core.COLORS[model])
                ax.set(xlabel="Physical training time", ylabel="Training MSE", yscale="log")
                ax.axhline(.001, color="#888888", ls=":", lw=.8)
            elif kind == "rms_vs_order":
                # The primary figure never substitutes an easier fallback score.
                rows = [row for row in primary if row["case"] == case]
                available = [row for row in rows if row["available"]]
                if available:
                    ax.plot([r["P"] for r in available], [max(r["rms_8192"], 1e-16) for r in available],
                            color="#666666", lw=1)
                for row in rows:
                    if row["available"]:
                        color = core.COLORS[f"P{row['P']}"]
                        ax.plot(row["P"], max(row["rms_8192"], 1e-16), "o", color=color,
                                markerfacecolor=color if row["numerical_pass"] else "white", ms=7)
                    else:
                        ax.text(row["P"], .03, "unavailable", rotation=90, va="bottom", ha="center",
                                transform=ax.get_xaxis_transform(), color="#777777", fontsize=8)
                ax.set(xlabel="Retained history modes P", ylabel="Circle RMS from dense", xticks=[1, 2, 3],
                       xlim=(.65, 3.35), yscale="log")
                ax.axhline(.1, ls=":", color="#888888", lw=.8)
                ax.text(.98, .95, "Primary training MSE .001", transform=ax.transAxes, ha="right", va="top", fontsize=8)
            elif loss is None:
                ax.text(.5, .5, "No fitted primary pair or all-model common loss", transform=ax.transAxes,
                        ha="center", wrap=True, fontsize=8)
                ax.set(xlabel="Input direction (degrees)", ylabel="Prediction")
            else:
                label = core.milestone_label(loss)
                dense = selected[(case, "dense")][0]
                reference, degrees = dense.observations[label]["prediction"], np.rad2deg(dense.angles)
                omitted = []
                for model in MODELS:
                    if kind == "endpoint_differences" and model == "dense":
                        continue
                    pair = selected.get((case, model))
                    if not pair or label not in pair[0].observations:
                        omitted.append(model)
                        continue
                    prediction = pair[0].observations[label]["prediction"]
                    row = index.get((case, loss, int(model[1:]))) if model != "dense" else None
                    ax.plot(degrees, prediction - reference if kind == "endpoint_differences" else prediction,
                            color=core.COLORS[model], lw=1.25, ls="-" if row is None or row["numerical_pass"] else "--")
                if kind == "function_curves":
                    ax.scatter(literal["angles_degrees"], literal["labels"], c="#202124", s=19, zorder=4)
                else:
                    ax.axhline(0, color="#888888", lw=.7)
                note = ("Primary" if loss == .001 else "FALLBACK") + f" training MSE {loss:g}"
                if omitted:
                    note += "\nUnavailable: " + ", ".join(omitted)
                ax.text(.98, .96, note, transform=ax.transAxes, ha="right", va="top", fontsize=8)
                ax.set(xlim=(0, 360), xticks=[0, 90, 180, 270, 360], xlabel="Input direction (degrees)",
                       ylabel="Closure minus dense" if kind == "endpoint_differences" else "Prediction")
            ax.grid(alpha=.2, lw=.6)
        handles = [Line2D([0], [0], color=core.COLORS[model], lw=1.5, label=model) for model in MODELS]
        fig.legend(handles=handles, loc="lower center", ncol=4, bbox_to_anchor=(.5, .025), frameon=False)
        fig.suptitle({"rms_vs_order": "Primary prediction discrepancy at each model's own MSE .001 crossing",
                      "function_curves": "Circle predictions at matched training loss",
                      "endpoint_differences": "Circle differences from one finest dense reference per activation/task",
                      "loss_trajectories": "Training loss along each finest numerical trajectory"}[kind], fontsize=13)
        fig.text(.5, .008, "Hollow markers / dashed closure curves: unresolved numerical gates. Crosses: stopped without fitting.\n"
                 "Fallback panels state their training loss. One seed; no hierarchy-convergence claim.",
                 ha="center", fontsize=8, color="#555555")
        fig.tight_layout(rect=[0, .065, 1, .97], h_pad=2)
        save(fig, kind)
    return artifacts, panel_counts


def analyze(roots, out):
    roots, out = [Path(root).resolve() for root in roots], Path(out).resolve()
    core.require(not out.exists(), f"Output must be a fresh directory: {out}")
    cases = core.read_json(STUDY / "activation_circle_cases.json")
    core.require(len(cases) == 8, "Frozen campaign must contain eight composite cases")
    configs = sorted({path.resolve().parent for root in roots for path in root.rglob("config.json")})
    core.require(configs, "No run config.json files found")
    runs, attempts, unavailable, initial_hashes, hash_cache = [], [], [], {}, {}
    for path in configs:
        entry = dict(path=str(path), finished=False, valid_scientific_run=False)
        try:
            config = core.read_json(path / "config.json")
            reason = excluded_phase(path, config)
            if reason:
                unavailable.append(dict(entry, status="excluded", reason=reason))
                continue
            case, model = case_metadata(config, cases)
            validate_config(config)
            entry.update(case=case, model=model, activation=cases[case]["activation"],
                         task=cases[case]["task"], rtol=float(config["rtol"]))
            entry["finished"] = (path / "summary.json").is_file() or (path / "failure.json").is_file()
            if not (path / "summary.json").is_file():
                entry.update(status="failed" if entry["finished"] else "incomplete",
                             failure=core.read_json(path / "failure.json") if entry["finished"] else None)
                unavailable.append(entry)
            elif core.read_json(path / "summary.json").get("status") == "failed":
                entry.update(status="failed", failure=core.read_json(path / "summary.json").get("failure_detail"))
                unavailable.append(entry)
            else:
                run = load_run(path, roots, cases, initial_hashes, hash_cache)
                runs.append(run)
                entry.update(status=run.summary["status"], valid_scientific_run=True)
        except (ValueError, KeyError, OSError, TypeError, zipfile.BadZipFile) as exc:
            entry.update(status="invalid", reason=f"{type(exc).__name__}: {exc}")
            unavailable.append(entry)
        attempts.append(entry)
    # Execution variants retain the same frozen physical sources, panel and draw.
    if runs:
        for run in runs[1:]:
            for key in ("initialization_hash", "query_sha256"):
                core.require(run.provenance[key] == runs[0].provenance[key], f"Campaign-wide {key} differs")
            core.require(all(run.provenance["source_sha256"][name] == runs[0].provenance["source_sha256"][name]
                             for name in PRODUCER_SOURCES), "Campaign-wide frozen physical producer differs")
        for case in cases:
            core.require(len({r.provenance["data_sha256"] for r in runs if r.case == case}) <= 1,
                         f"Training data differ within {case}")
    selected = core.select_runs(runs)
    unusable = {(row["case"], row["model"]): row for row in attempts
                if row.get("rtol") == core.EXTRA_RTOL and not row.get("valid_scientific_run")}
    comparisons, primary, fallback, time_rows, missing, endpoints = comparison_tables(cases, selected, unusable)
    schedule = schedule_status(cases, attempts, runs)
    requests = refinement_decisions(comparisons, selected, schedule["primary_schedule_complete"], attempts)
    order_rows = core.order_comparisons(comparisons)
    for row in order_rows:
        row.update(activation=cases[row["case"]]["activation"], task=cases[row["case"]]["task"],
                   comparison_type="primary_matched_loss" if row["milestone"] == .001 else "secondary_matched_loss")
    inventory = []
    for run in runs:
        row = core.inventory_row(run)
        row.update(activation=run.config["activation"], task=run.config["task"], valid_scientific_run=True,
                   observed_physical_times=run.summary["observed_physical_times"], finished=True)
        row.update({key: run.observations["final"][key] for key in DIAGNOSTIC_KEYS})
        inventory.append(row)
    inventory.extend(unavailable)
    out.mkdir(parents=True, exist_ok=False)
    figures, panel_counts = make_plots(out, cases, selected, primary, endpoints, comparisons)
    complete = schedule["primary_schedule_complete"]
    result = dict(schema_version=1, architecture="three hidden layers, activation-specific", width=4096,
                  analysis_status="primary_schedule_finished" if complete else "partial_primary_schedule",
                  **schedule, refinement_decisions_provisional=not complete,
                  refinement_decision_status="evaluated" if complete else "deferred_until_all_64_attempts_finish",
                  run_roots=[str(root) for root in roots], endpoints=endpoints, comparisons=comparisons,
                  primary_comparisons=primary, endpoint_comparisons=[row for row in primary if row["available"]],
                  fallback_comparisons=fallback, matched_time_comparisons=time_rows, order_comparisons=order_rows,
                  refinement_requests=requests, required_refinements=[r for r in requests if r["conditional_run_available"]],
                  unresolved_after_refinement=[r for r in requests if not r["conditional_run_available"]],
                  missing_comparisons=missing, unavailable_or_excluded=unavailable, run_inventory=inventory,
                  attempts=attempts, selected={case: {model: dict(finest=str(selected[(case, model)][0].path),
                      previous=str(selected[(case, model)][1].path) if selected[(case, model)][1] else None)
                      for model in MODELS if (case, model) in selected} for case in cases},
                  resources=dict(scientific_trajectories=len(runs),
                      failed_or_invalid_or_incomplete=sum(item["status"] != "excluded" for item in unavailable),
                      integration_with_observations_seconds=sum(r.summary["integration_with_observations_seconds"] for r in runs),
                      integration_excluding_observations_seconds=sum(r.summary["integration_seconds_excluding_observations"] for r in runs),
                      capped_or_unfitted=[str(r.path) for r in runs if r.summary["status"] != "target_loss"],
                      scope="Valid supplied science runs; failed/pilot/repeat timing remains in campaign receipts"),
                  provenance={str(run.path): run.provenance for run in runs},
                  source_sha256={name: core.sha256(STUDY / name) for name in SOURCES},
                  environment=dict(python=sys.version, numpy=np.__version__, platform=platform.platform()),
                  command=sys.argv, figures=figures, figure_panel_counts=panel_counts,
                  caveats=["Primary comparisons use each model's own .001 loss crossing, pair by pair.",
                           "Fallback common-loss and matched-time observations are secondary; neither establishes fitted accuracy.",
                           "Observed tolerance sensitivities are empirical diagnostics, not certified error bounds.",
                           "Caps, failed runs, missing crossings and grid-only/time-only gates do not trigger solver refinement.",
                           "Checkpoint scalar metadata and hashes are checked; physical prediction replay is a separate audit.",
                           "One seed, three tested orders; no hierarchy convergence, width-uniform bound or speed advantage follows."])
    core.write_json(out / "metrics_summary.json", result)
    core.write_json(out / "refinement_requests.json", dict(provisional=not complete,
                    primary_schedule_complete=complete, primary_inventory_complete=schedule["primary_inventory_complete"],
                    required=result["required_refinements"], exhausted=result["unresolved_after_refinement"],
                    all_requests=requests, missing_comparisons=missing))
    for name, rows in (("comparison_metrics", comparisons), ("primary_metrics", primary),
                       ("endpoint_metrics", primary), ("fallback_metrics", fallback),
                       ("matched_time_metrics", time_rows), ("order_comparisons", order_rows), ("run_inventory", inventory)):
        core.write_csv(out / (name + ".csv"), rows)
    core.write_json(out / "artifact_manifest.json", {p.name: core.sha256(p) for p in sorted(out.iterdir()) if p.is_file()})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs", nargs="+", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    result = analyze(args.runs, args.out)
    print(json.dumps(dict(output=str(Path(args.out).resolve()), analysis_status=result["analysis_status"],
                          valid_runs=result["resources"]["scientific_trajectories"],
                          primary_available=len(result["endpoint_comparisons"]),
                          required_refinements=len(result["required_refinements"])), indent=2))


if __name__ == "__main__":
    main()
