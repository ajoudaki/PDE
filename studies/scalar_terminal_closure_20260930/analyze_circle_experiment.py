"""Independently analyze saved circle runs; never train or import the producer.

Usage: python analyze_circle_experiment.py --run RUN --output FRESH_DIRECTORY
Incomplete results.json files are supported. Missing tasks remain visible in all
five-row figures. Summary disagreements produce artifacts and a nonzero exit.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import time

import numpy as np

CASES = (
    "two_outliers_alternating", "quadrant_alternating", "quadrant_pairs",
    "quadrant_center_edges", "equal_mixed_odd",
)
THRESHOLDS = (0.1, 0.01, 0.001)
COLORS = {"dense": "#111111", "q1": "#1764ab", "scalar": "#e87518",
          "static": "#888888", 0.1: "#8c4dad", 0.01: "#e87518", 0.001: "#229567"}
FIT = 1e-6
PLOT_LOSS_FLOOR = 1e-16


def read_json(path):
    return json.loads(Path(path).read_text())


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def rms(values):
    values = np.asarray(values, dtype=float)
    return float(np.sqrt(np.mean(values * values)))


def maximum(values):
    return float(np.max(np.abs(values)))


def basis(angles):
    """Independent real basis: odd cosines, then odd sines, 1 through 63."""
    phase = np.outer(np.asarray(angles, dtype=float), np.arange(1, 64, 2))
    return np.column_stack((np.cos(phase), np.sin(phase)))


def load_arrays(path):
    with np.load(path, allow_pickle=False) as source:
        arrays = {key: source[key] for key in source.files}
    for key, value in arrays.items():
        if not np.issubdtype(value.dtype, np.number) or not np.isfinite(value).all():
            raise ValueError(f"Nonfinite or nonnumeric array {path}:{key}")
    return arrays


def check_state_archive(path, verify, source_hashes):
    """Scan every saved array, including width-sized states, without retaining it."""
    with np.load(path, allow_pickle=False) as source:
        for key in source.files:
            value = source[key]
            finite = np.issubdtype(value.dtype, np.number) and bool(np.isfinite(value).all())
            verify.compare(f"{path.parent.parent.name}/{path.parent.name}/{path.name}:{key}_finite", finite, True)
    source_hashes[str(path)] = sha256(path)


class Verifier:
    def __init__(self):
        self.checks = []

    def compare(self, name, actual, expected, rtol=1e-9, atol=1e-12):
        if actual is None or expected is None:
            passed = actual is expected
            error = None
        elif isinstance(actual, (bool, str)) or isinstance(expected, (bool, str)):
            passed = actual == expected
            error = None
        else:
            a, b = np.asarray(actual), np.asarray(expected)
            passed = a.shape == b.shape and bool(np.allclose(a, b, rtol=rtol, atol=atol))
            error = maximum(a - b) if a.shape == b.shape and a.size else None
        self.checks.append(dict(name=name, passed=bool(passed), max_absolute_difference=error))

    def metrics(self, prefix, computed, recorded):
        for key, value in computed.items():
            if key in recorded:
                self.compare(f"{prefix}:{key}", value, recorded[key])

    @property
    def passed(self):
        return all(check["passed"] for check in self.checks)


def compare_refinement(first, second):
    a, b = load_arrays(first / "curves.npz"), load_arrays(second / "curves.npz")
    if not np.array_equal(a["angles"], b["angles"]):
        raise ValueError("Refinement endpoint queries are not identical")
    if abs(float(a["times"][-1] - b["times"][-1])) > 1e-10:
        raise ValueError("Refinement endpoints differ in physical time")
    result = {}
    for model in ("dense", "q1"):
        result[f"{model}_endpoint_rms"] = rms(a[f"{model}_output"] - b[f"{model}_output"])
        common = np.interp(a["times"], b["times"], b[f"{model}_loss"])
        result[f"{model}_loss_max"] = maximum(a[f"{model}_loss"] - common)
    query_basis = basis(a["angles"])
    for threshold in THRESHOLDS:
        tag = f"{threshold:g}"
        for model in ("scalar", "static"):
            key = f"{model}_output_{tag}"
            result[f"{model}_endpoint_rms_{tag}"] = rms(a[key] - b[key]) if key in a and key in b else None
        time_key, loss_key = f"scalar_times_{tag}", f"scalar_loss_{tag}"
        if time_key in a and time_key in b:
            if abs(float(a[time_key][0]-b[time_key][0])) > 1e-10:
                raise ValueError("Scalar refinement starts at unequal physical handoff times")
            result[f"scalar_loss_max_{tag}"] = maximum(a[loss_key]-np.interp(a[time_key], b[time_key], b[loss_key]))
            with np.load(first / f"handoff_{tag}.npz", allow_pickle=False) as left:
                left_coefficients = left["fourier"][:, 0]
            with np.load(second / f"handoff_{tag}.npz", allow_pickle=False) as right:
                right_coefficients = right["fourier"][:, 0]
            result[f"fourier_static_endpoint_rms_{tag}"] = rms(query_basis @ (left_coefficients-right_coefficients))
        else:
            result[f"scalar_loss_max_{tag}"] = None
            result[f"fourier_static_endpoint_rms_{tag}"] = None
    result["primary_scalar_endpoint_rms"] = result["scalar_endpoint_rms_0.01"]
    result["passed"] = bool(
        all(result[f"{model}_endpoint_rms"] <= .002 for model in ("dense", "q1"))
        and all(result[f"{model}_loss_max"] <= .001 for model in ("dense", "q1"))
        and result["primary_scalar_endpoint_rms"] is not None
        and result["primary_scalar_endpoint_rms"] <= .002)
    result["primary_scalar_loss_max"] = result["scalar_loss_max_0.01"]
    result["primary_scalar_loss_passed"] = (result["primary_scalar_loss_max"] is not None
                                             and result["primary_scalar_loss_max"] <= .001)
    result["passed_with_scalar_loss"] = result["passed"] and result["primary_scalar_loss_passed"]
    result["compared_resolutions"] = [first.name, second.name]
    return result


def outcome(refinement_passed, full_fit, fourier_fit, fidelity):
    if not refinement_passed:
        return "inconclusive_refinement"
    if not full_fit:
        return "inconclusive_unfinished_full_fit"
    if not fourier_fit:
        return "fail_fourier_function_fit"
    return "pass" if fidelity else "fail_fidelity"


def analyze_case(run, result, verify, source_hashes):
    check_start = len(verify.checks)
    case, selected = result["case"], result["selected"]
    if case not in CASES or selected not in ("fine", "refined"):
        raise ValueError(f"Unexpected case/resolution: {case}/{selected}")
    directory = run / case / selected
    summary = read_json(directory / "summary.json")
    curves = load_arrays(directory / "curves.npz")
    for name in ("summary.json", "curves.npz"):
        source_hashes[str(directory / name)] = sha256(directory / name)
    # Only inspect finished cases in the results snapshot; never an in-progress write.
    for resolution in ("coarse", "fine", "refined"):
        resolution_dir = run / case / resolution
        if not (resolution_dir / "summary.json").is_file():
            continue
        resolution_summary = read_json(resolution_dir / "summary.json")
        check_state_archive(resolution_dir / "endpoint_states.npz", verify, source_hashes)
        for captured in resolution_summary["handoffs"]:
            check_state_archive(resolution_dir / f"handoff_{captured['threshold']:g}.npz", verify, source_hashes)
    times, angles, labels = curves["times"], curves["angles"], curves["labels"]
    m = len(labels)
    if times.ndim != 1 or len(times) == 0 or np.any(np.diff(times) <= 0):
        raise ValueError(f"Invalid physical times for {case}")
    if angles.shape != (8192,) or np.any(np.diff(angles) <= 0):
        raise ValueError(f"Invalid query angles for {case}")
    if m != 8 or not np.all(np.isin(labels, (-1., 1.))):
        raise ValueError(f"Invalid binary training labels for {case}")
    if curves["q1_residual"].shape != (len(times), m):
        raise ValueError(f"Invalid q1 residual shape for {case}")
    for model in ("dense", "q1"):
        if curves[f"{model}_output"].shape != angles.shape or curves[f"{model}_loss"].shape != times.shape:
            raise ValueError(f"Invalid {model} output/loss shape for {case}")
    verify.compare(f"{case}:q1_loss_from_residuals", np.mean(curves["q1_residual"] ** 2, axis=1), curves["q1_loss"])
    dense, q1 = curves["dense_output"], curves["q1_output"]
    base = dict(final_time=float(times[-1]), dense_final_loss=float(curves["dense_loss"][-1]),
                q1_final_loss=float(np.mean(curves["q1_residual"][-1] ** 2)),
                q1_vs_dense_rms=rms(q1-dense), q1_vs_dense_max=maximum(q1-dense),
                q1_dense_sign_disagreement=float(np.mean(np.sign(q1) != np.sign(dense))))
    base["fitted"] = max(base["dense_final_loss"], base["q1_final_loss"]) <= FIT
    verify.metrics(f"{case}:disk_summary", base, summary)
    verify.metrics(f"{case}:results_summary", base, result[selected])
    n = int(summary["width"])
    counts = dict(moving_scalar_count=2*m+1, fixed_scalar_count=m*m+m+64*(m+2),
                  dense_moving_scalar_count=n*n+3*n, q1_moving_scalar_count=3*n+2*n*m+1,
                  q1_fixed_mixer_count=n*n)
    verify.metrics(f"{case}:independent_state_counts", counts, summary)
    verify.compare(f"{case}:planned_width", n, 1024)
    verify.compare(f"{case}:planned_seed", int(summary["seed"]), 20260920)
    verify.compare(f"{case}:recorded_time_step", np.diff(times), np.full(len(times)-1, summary["step"]))
    first = run / case / ("fine" if selected == "refined" else "coarse")
    refinement = compare_refinement(first, directory)
    source_hashes[str(first / "curves.npz")] = sha256(first / "curves.npz")
    verify.metrics(f"{case}:refinement", refinement, result["refinement"])
    rows = []
    summaries = {float(h["threshold"]): h for h in summary["handoffs"]}
    embedded = {float(h["threshold"]): h for h in result[selected]["handoffs"]}
    if set(summaries) != set(embedded):
        raise ValueError(f"Handoff list differs between summaries for {case}")
    for threshold in THRESHOLDS:
        if threshold not in summaries:
            continue
        tag = f"{threshold:g}"
        saved = summaries[threshold]
        handoff_path = directory / f"handoff_{tag}.npz"
        # Load only the saved scalar coefficients, not width-sized state arrays.
        with np.load(handoff_path, allow_pickle=False) as stored:
            handoff = {key: stored[key] for key in (
                "matrix", "drift", "residual", "fourier", "query_f", "query_c", "query_b", "time")}
        if not all(np.isfinite(value).all() for value in handoff.values()):
            raise ValueError(f"Nonfinite handoff coefficients in {handoff_path}")
        source_hashes[str(handoff_path)] = sha256(handoff_path)
        st = curves[f"scalar_state_{tag}"]
        scalar_times = curves[f"scalar_times_{tag}"]
        if st.shape != (len(scalar_times), 2*m+1) or len(st) == 0:
            raise ValueError(f"Invalid scalar state shape for {case}/{tag}")
        mask = times >= float(handoff["time"])
        verify.compare(f"{case}/{tag}:common_physical_times", scalar_times, times[mask], rtol=0, atol=1e-11)
        if len(scalar_times) != np.count_nonzero(mask):
            raise ValueError(f"Scalar/full loss arrays do not share times for {case}/{tag}")
        scalar_losses = np.mean(st[:, :m] ** 2, axis=1)
        verify.compare(f"{case}/{tag}:saved_scalar_losses", scalar_losses, curves[f"scalar_loss_{tag}"])
        weights = np.r_[1., -st[-1, m:2*m], st[-1, -1]]
        coefficients = handoff["fourier"] @ weights
        reconstructed = basis(angles) @ coefficients
        train_output = basis(curves["train_angles"]) @ coefficients
        fourier_static = basis(angles) @ handoff["fourier"][:, 0]
        fourier_static_train = basis(curves["train_angles"]) @ handoff["fourier"][:, 0]
        curves[f"fourier_static_output_{tag}"] = fourier_static
        scalar = curves[f"scalar_output_{tag}"]
        direct = curves[f"scalar_direct_output_{tag}"]
        static = curves[f"static_output_{tag}"]
        verify.compare(f"{case}/{tag}:Fourier_query_reconstruction", reconstructed, scalar)
        direct_check = (handoff["query_f"] - handoff["query_c"] @ st[-1, m:2*m]
                        + handoff["query_b"] * st[-1, -1])
        verify.compare(f"{case}/{tag}:untruncated_query_reconstruction", direct_check, direct)
        verify.compare(f"{case}/{tag}:static_query_reconstruction", handoff["query_f"], static)
        exact_train = (labels + handoff["residual"] - handoff["matrix"] @ st[-1, m:2*m]
                       + handoff["drift"] * st[-1, -1])
        away = np.abs(dense) >= .05
        disagreement = np.sign(scalar) != np.sign(dense)
        spatial_error = basis(angles) @ handoff["fourier"] - np.column_stack((
            handoff["query_f"], handoff["query_c"], handoff["query_b"]))
        sym = (handoff["matrix"] + handoff["matrix"].T) / 2
        metrics = dict(
            threshold=threshold, time=float(handoff["time"]),
            train_mse=float(np.mean(handoff["residual"] ** 2)),
            scalar_vs_dense_rms=rms(scalar-dense), scalar_vs_dense_max=maximum(scalar-dense),
            scalar_vs_q1_rms=rms(scalar-q1), scalar_vs_q1_max=maximum(scalar-q1),
            direct_scalar_vs_q1_rms=rms(direct-q1), direct_scalar_vs_q1_max=maximum(direct-q1),
            fourier_output_error_rms=rms(scalar-direct), fourier_output_error_max=maximum(scalar-direct),
            static_vs_q1_rms=rms(static-q1), static_vs_q1_max=maximum(static-q1),
            static_vs_dense_rms=rms(static-dense), static_vs_dense_max=maximum(static-dense),
            fourier_static_vs_q1_rms=rms(fourier_static-q1), fourier_static_vs_q1_max=maximum(fourier_static-q1),
            fourier_static_vs_dense_rms=rms(fourier_static-dense), fourier_static_vs_dense_max=maximum(fourier_static-dense),
            fourier_static_train_mse=float(np.mean((fourier_static_train-labels)**2)),
            fourier_static_representation_rms=rms(fourier_static-static),
            sign_disagreement=float(np.mean(disagreement)),
            sign_disagreement_away=float(np.mean(disagreement[away])) if np.any(away) else None,
            dense_away_fraction=float(np.mean(away)),
            scalar_final_loss=float(scalar_losses[-1]),
            fourier_predictor_train_mse=float(np.mean((train_output-labels) ** 2)),
            fourier_train_consistency_max=maximum(train_output-labels-st[-1, :m]),
            exact_train_observer_consistency_max=maximum(exact_train-labels-st[-1, :m]),
            max_loss_error_vs_q1=maximum(scalar_losses-curves["q1_loss"][mask]),
            max_loss_error_vs_dense=maximum(scalar_losses-curves["dense_loss"][mask]),
            scalar_final_residual=st[-1, :m].tolist(),
            margin=float(np.linalg.eigvalsh(sym)[0]-np.linalg.norm(handoff["drift"])),
            spatial_rms_by_field=np.sqrt(np.mean(spatial_error**2, axis=0)).tolist(),
            spatial_max_by_field=np.max(np.abs(spatial_error), axis=0).tolist())
        train_inputs = np.vstack((np.cos(curves["train_angles"]), np.sin(curves["train_angles"])))
        metrics["projected_margin"] = None
        if np.max(np.abs(train_inputs[:, :4]+train_inputs[:, 4:])) < 1e-12 and np.array_equal(labels[:4], -labels[4:]):
            odd = np.vstack((np.eye(4), -np.eye(4))) / np.sqrt(2)
            metrics["projected_margin"] = float(np.linalg.eigvalsh(odd.T @ sym @ odd)[0]
                                                - np.linalg.norm(odd.T @ handoff["drift"]))
        verify.metrics(f"{case}/{tag}:disk_summary", metrics, saved)
        verify.metrics(f"{case}/{tag}:results_summary", metrics, embedded[threshold])
        static_sensitivity = refinement[f"static_endpoint_rms_{tag}"]
        scalar_sensitivity = refinement[f"scalar_endpoint_rms_{tag}"]
        tail_sensitivity = (None if static_sensitivity is None else
                            static_sensitivity + refinement["q1_endpoint_rms"])
        matched_sensitivity = refinement[f"fourier_static_endpoint_rms_{tag}"]
        matched_tail_sensitivity = (None if matched_sensitivity is None else
                                    matched_sensitivity + refinement["q1_endpoint_rms"])
        metrics.update(
            case=case, selected=selected, step=float(summary["step"]), **base,
            refinement_passed=refinement["passed"],
            scalar_loss_refinement_passed=refinement["primary_scalar_loss_passed"],
            all_refinement_checks_passed=refinement["passed_with_scalar_loss"],
            scalar_loss_numerical_sensitivity=refinement[f"scalar_loss_max_{tag}"],
            scalar_endpoint_numerical_sensitivity=scalar_sensitivity,
            static_tail_numerical_sensitivity=tail_sensitivity,
            fourier_static_tail_numerical_sensitivity=matched_tail_sensitivity,
            scalar_ode_fitted=metrics["scalar_final_loss"] <= FIT,
            scalar_fourier_function_fitted=metrics["fourier_predictor_train_mse"] <= FIT,
            dense_imitation_threshold_met=metrics["scalar_vs_dense_rms"] <= .05 and metrics["sign_disagreement"] <= .01,
            q1_imitation_threshold_met=metrics["scalar_vs_q1_rms"] <= .01 and metrics["scalar_vs_q1_max"] <= .05,
            improvement_factor_over_static=(metrics["static_vs_q1_rms"]/metrics["scalar_vs_q1_rms"]
                if metrics["scalar_vs_q1_rms"] > 0 else None),
            static_tail_resolved=(tail_sensitivity is not None and metrics["static_vs_q1_rms"] > 10*tail_sensitivity),
            at_least_twofold_static_improvement=2*metrics["scalar_vs_q1_rms"] <= metrics["static_vs_q1_rms"],
            improvement_factor_over_fourier_static=(metrics["fourier_static_vs_q1_rms"]/metrics["scalar_vs_q1_rms"]
                if metrics["scalar_vs_q1_rms"] > 0 else None),
            fourier_static_tail_resolved=(matched_tail_sensitivity is not None
                and metrics["fourier_static_vs_q1_rms"] > 10*matched_tail_sensitivity),
            at_least_twofold_fourier_static_improvement=2*metrics["scalar_vs_q1_rms"] <= metrics["fourier_static_vs_q1_rms"])
        metrics["meaningful_static_improvement"] = bool(metrics["static_tail_resolved"]
            and metrics["at_least_twofold_static_improvement"] and refinement["passed_with_scalar_loss"])
        metrics["meaningful_fourier_static_improvement"] = bool(metrics["fourier_static_tail_resolved"]
            and metrics["at_least_twofold_fourier_static_improvement"] and refinement["passed_with_scalar_loss"])
        for target in ("dense", "q1"):
            metrics[f"{target}_imitation_outcome"] = outcome(refinement["passed_with_scalar_loss"], base["fitted"],
                metrics["scalar_fourier_function_fitted"], metrics[f"{target}_imitation_threshold_met"])
        rows.append(metrics)
    audit = dict(case=case, selected=selected, **base, refinement=refinement,
                 width=summary["width"], seed=summary["seed"], step=summary["step"],
                 missing_handoffs=[t for t in THRESHOLDS if t not in summaries], handoffs=rows)
    audit["artifact_checks_passed"] = all(check["passed"] for check in verify.checks[check_start:])
    if not audit["artifact_checks_passed"]:
        for row in rows:
            row["dense_imitation_outcome"] = "inconclusive_artifact_checks"
            row["q1_imitation_outcome"] = "inconclusive_artifact_checks"
    for key in ("wall_seconds", "peak_rss_bytes", "moving_scalar_count", "fixed_scalar_count",
                "dense_moving_scalar_count", "q1_moving_scalar_count", "q1_fixed_mixer_count",
                "a_initial_hash", "w0_initial_hash"):
        audit[key] = summary[key]
    return audit, curves


def make_plots(output, audits, arrays, titles):
    # Keep the backend and font cache inside this fresh analysis directory.
    os.environ["MPLCONFIGDIR"] = str(output / "matplotlib-cache")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 9, "axes.spines.top": False,
                         "axes.spines.right": False, "savefig.bbox": "tight"})

    def grid(sharex=True):
        return plt.subplots(5, 1, figsize=(12, 15), sharex=sharex, squeeze=False)

    def absent(ax, case):
        ax.text(.5, .5, "No completed selected run in results.json", ha="center", va="center", transform=ax.transAxes)
        ax.set_title(titles[case], loc="left")

    def finish(fig, name):
        fig.tight_layout(rect=(0, .025, 1, .975))
        for extension in ("png", "pdf"):
            fig.savefig(output / f"{name}.{extension}", dpi=180)
        plt.close(fig)

    fig, axes = grid()
    fig.suptitle("Signed circle predictions at the common endpoint — width 1024, one seed", fontsize=13)
    for ax, case in zip(axes[:, 0], CASES):
        if case not in audits:
            absent(ax, case)
            continue
        audit, data = audits[case], arrays[case]
        degrees = np.degrees(data["angles"])
        primary = next((h for h in audit["handoffs"] if h["threshold"] == .01), None)
        values = [data["dense_output"], data["q1_output"], data["labels"]]
        for model, label in (("dense", "Dense"), ("q1", "q=1")):
            ax.plot(degrees, data[f"{model}_output"], color=COLORS[model], lw=1.7, label=label)
        if primary:
            for model, label, style in (("scalar", "Scalar, handoff 0.01", "-"), ("fourier_static", "Static Fourier at handoff", "--")):
                values.append(data[f"{model}_output_0.01"])
                ax.plot(degrees, values[-1], color=COLORS["static" if model == "fourier_static" else model], lw=1.4, ls=style, label=label)
        ax.scatter(np.degrees(data["train_angles"]), data["labels"], s=26,
                   facecolors="white", edgecolors="black", zorder=6, label="Training labels")
        for x, y in zip(np.degrees(data["train_angles"]), data["labels"]):
            ax.annotate(f"{y:+.0f}", (x, y), xytext=(0, 5 if y > 0 else -12),
                        textcoords="offset points", ha="center", fontsize=6)
        lo = min(float(np.min(v)) for v in values)
        hi = max(float(np.max(v)) for v in values)
        pad = .09 * max(hi-lo, 1.)
        ax.set_ylim(lo-pad, hi+pad)
        ax.axhline(0, color="#dddddd", lw=.6)
        text = f"{titles[case]} | t={audit['final_time']:g}, dt={audit['step']:g}"
        text += f" | MSE dense={audit['dense_final_loss']:.2g}, q=1={audit['q1_final_loss']:.2g}"
        text += (f", scalar function={primary['fourier_predictor_train_mse']:.2g}" if primary else " | primary handoff unavailable")
        ax.set_title(text, loc="left", fontsize=9)
        ax.set_ylabel(r"$f(\theta)$")
        ax.grid(alpha=.15)
    for ax in axes[:, 0]:
        ax.set_xlim(0, 360)
        ax.set_xticks(np.arange(0, 361, 60))
    axes[-1, 0].set_xlabel("Angle (degrees)")
    for ax in axes[:, 0]:
        handles, labels = ax.get_legend_handles_labels()
        if handles:
            ax.legend(handles, labels, ncol=5, loc="lower left", fontsize=7)
            break
    fig.text(.01, .006, "Actual signed outputs; no model-specific rescaling. Dense is an imitation reference, not unknown test truth.", fontsize=9)
    finish(fig, "final-circle-functions")

    fig, axes = grid(sharex=False)
    fig.suptitle("Training loss at equal physical times — all three prespecified handoffs", fontsize=13)
    for ax, case in zip(axes[:, 0], CASES):
        if case not in audits:
            absent(ax, case)
            continue
        audit, data = audits[case], arrays[case]
        for model, label in (("dense", "Dense"), ("q1", "q=1")):
            ax.semilogy(data["times"], np.maximum(data[f"{model}_loss"], PLOT_LOSS_FLOOR),
                        color=COLORS[model], lw=1.6, label=label)
        for row in audit["handoffs"]:
            threshold = row["threshold"]
            tag = f"{threshold:g}"
            ax.semilogy(data[f"scalar_times_{tag}"], np.maximum(data[f"scalar_loss_{tag}"], PLOT_LOSS_FLOOR),
                        color=COLORS[threshold], lw=1.15, label=f"Scalar ODE, {tag}")
            ax.axvline(row["time"], color=COLORS[threshold], lw=.65, alpha=.4)
            ax.plot([audit["final_time"]], [max(row["fourier_predictor_train_mse"], PLOT_LOSS_FLOOR)],
                    marker="D", ms=5, mec=COLORS[threshold], mfc="none", ls="none")
        ax.axhline(FIT, color="#b22222", lw=.7, ls=":", label="Fit threshold")
        ax.set_title(f"{titles[case]} | refinement including scalar loss {'passed' if audit['refinement']['passed_with_scalar_loss'] else 'FAILED'}", loc="left")
        ax.set_ylabel("Training MSE")
        ax.grid(alpha=.15, which="both")
        ax.set_xlim(0, audit["final_time"]*1.02)
    axes[-1, 0].set_xlabel("Physical time")
    for ax in axes[:, 0]:
        if ax.get_legend_handles_labels()[0]:
            ax.legend(ncol=6, loc="upper right", fontsize=7)
            break
    fig.text(.01, .006, "Scalar lines: residual MSE. Diamonds: Fourier function MSE. Each row uses its recorded time range. Display floor: 1e-16.", fontsize=9)
    finish(fig, "losses")

    fig, axes = grid()
    fig.suptitle("Endpoint imitation errors versus handoff training MSE", fontsize=13)
    for ax, case in zip(axes[:, 0], CASES):
        if case not in audits:
            absent(ax, case)
            continue
        audit = audits[case]
        rows = sorted(audit["handoffs"], key=lambda row: row["train_mse"])
        x = [row["train_mse"] for row in rows]
        for key, label, color, style in (
            ("scalar_vs_q1_rms", "Scalar versus q=1", COLORS["scalar"], "-"),
            ("static_vs_q1_rms", "Static versus q=1", COLORS["static"], "--"),
            ("fourier_static_vs_q1_rms", "Static Fourier versus q=1", "#555555", "-."),
            ("scalar_vs_dense_rms", "Scalar versus dense", "#8c4dad", "-"),
            ("fourier_output_error_rms", "Fourier versus untruncated scalar", "#229567", ":")):
            ax.loglog(x, [max(row[key], PLOT_LOSS_FLOOR) for row in rows], marker="o", color=color, ls=style, label=label)
        ax.axhline(max(audit["q1_vs_dense_rms"], PLOT_LOSS_FLOOR), color=COLORS["q1"], label="q=1 versus dense")
        ax.axhline(.01, color="#e87518", alpha=.35, ls=":", lw=.8)
        ax.axhline(.05, color="#8c4dad", alpha=.35, ls=":", lw=.8)
        ax.set_title(titles[case], loc="left")
        ax.set_ylabel("Circle RMS error")
        ax.grid(alpha=.15, which="both")
    axes[-1, 0].set_xlabel("Actual q=1 training MSE at handoff (smaller means later)")
    for ax in axes[:, 0]:
        if ax.get_legend_handles_labels()[0]:
            ax.legend(ncol=3, fontsize=7, loc="best")
            break
    fig.text(.01, .006, "All prespecified switches are shown. Errors use the saved 8192-point circle grid; they are not uniform-circle certificates.", fontsize=9)
    finish(fig, "error-vs-handoff")
    return matplotlib.__version__


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    begin = time.perf_counter()
    run, output = args.run.resolve(), args.output.resolve()
    results_path = run / "results.json"
    if not results_path.is_file():
        parser.error(f"No completed-case results.json yet: {results_path}")
    results_bytes = results_path.read_bytes()
    results = json.loads(results_bytes)
    output.mkdir(parents=True, exist_ok=False)
    (output / "results_snapshot.json").write_bytes(results_bytes)
    shutil.copy2(__file__, output / Path(__file__).name)
    verify = Verifier()
    sources = {str(results_path): hashlib.sha256(results_bytes).hexdigest(), str(Path(__file__).resolve()): sha256(__file__)}
    audits, arrays = {}, {}
    for result in results["results"]:
        case = result["case"]
        if case in audits:
            raise ValueError(f"Duplicate result for {case}")
        audit, data = analyze_case(run, result, verify, sources)
        audits[case], arrays[case] = audit, data
    if results.get("complete", False) and set(audits) != set(CASES):
        raise ValueError("Run declares completion without all five planned cases")
    if audits:
        first_audit = next(iter(audits.values()))
        for case, audit in audits.items():
            for key in ("a_initial_hash", "w0_initial_hash"):
                verify.compare(f"{case}:shared_{key}", audit[key], first_audit[key])
    upstream_provenance = None
    for name in ("provenance.json", "CIRCLE_EXPERIMENT_PLAN.md", "circle_terminal_experiment.py"):
        path = run / name
        if path.is_file():
            sources[str(path)] = sha256(path)
            if name == "provenance.json":
                upstream_provenance = read_json(path)
    titles = {case: case.replace("_", " ").capitalize() for case in CASES}
    task_path = run / "circle_task_inputs.json"
    if task_path.is_file():
        sources[str(task_path)] = sha256(task_path)
        for task in read_json(task_path)["tasks"]:
            if task["case"] in titles:
                titles[task["case"]] = task.get("title", titles[task["case"]])
    mpl_version = make_plots(output, audits, arrays, titles)
    rows = [row for case in CASES if case in audits for row in audits[case]["handoffs"]]
    fields = ["case", "selected", "step", "threshold", "time", "train_mse", "final_time",
              "dense_final_loss", "q1_final_loss", "scalar_final_loss", "fourier_predictor_train_mse"]
    other = sorted({key for row in rows for key, value in row.items()
                    if not isinstance(value, (list, dict))} - set(fields))
    with (output / "metrics.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields+other, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    report = dict(
        run=str(run), run_complete=bool(results.get("complete", False)),
        available_cases=[case for case in CASES if case in audits],
        missing_cases=[case for case in CASES if case not in audits],
        summary_agreement=all(check["passed"] for check in verify.checks
            if any(token in check["name"] for token in (":disk_summary:", ":results_summary:", ":refinement:"))),
        all_checks_passed=verify.passed, checks=verify.checks,
        cases=[audits[case] for case in CASES if case in audits],
        primary_threshold=.01, all_thresholds=list(THRESHOLDS), fit_threshold=FIT,
        metric_definitions=dict(
            circle_error="Unweighted RMS and maximum on saved 8192 midpoint-shifted queries, in label units.",
            scalar_final_loss="Mean square of the scalar ODE residual state at the common physical endpoint.",
            fourier_predictor_train_mse="MSE of the saved 32-odd-frequency function evaluated independently at exact training angles.",
            dense_final_loss="Endpoint of saved dense training-loss curve; no independent dense state reevaluation in this analyzer.",
            static_tail_numerical_sensitivity="Sum of refinement RMS changes in static handoff function and final q=1 function.",
            fourier_static_baseline="The initial Fourier coefficient column evaluated without any scalar continuation; reported separately from direct handoff function.",
            supplemental_scalar_loss_refinement="Independently require primary scalar common-time loss step change <=0.001; original producer gate remains separately recorded.",
            meaningful_static_improvement="At least twofold RMS improvement, static movement >10 times its numerical sensitivity, and refinement gates pass.",
            imitation_outcomes="Require passed refinement, dense/q1 MSE <=1e-6, Fourier function MSE <=1e-6, then apply preregistered fidelity thresholds.",
            plot_loss_floor=PLOT_LOSS_FLOOR),
        limits=["One seed; five prespecified tasks; no retraining by analysis.",
                "Dense predictions are an imitation reference, not unknown test truth.",
                "Finite time and finite query grid, not an infinite-time or uniform-circle certificate.",
                "The scalar continuation starts from a full q=1 handoff; it is not initialization-only compression.",
                "Scalar ODE residual fitting does not establish fitting by its Fourier function."],
        provenance=dict(command=sys.argv, python=sys.version, executable=sys.executable,
                        numpy=np.__version__, matplotlib=mpl_version, source_hashes=sources,
                        upstream=upstream_provenance,
                        elapsed_seconds=time.perf_counter()-begin))
    write_json(output / "analysis.json", report)
    print(json.dumps(dict(output=str(output), cases=len(audits), handoffs=len(rows),
                          run_complete=report["run_complete"], summary_agreement=report["summary_agreement"],
                          all_checks_passed=verify.passed,
                          failed_checks=[c for c in verify.checks if not c["passed"]]), indent=2))
    return 0 if verify.passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
