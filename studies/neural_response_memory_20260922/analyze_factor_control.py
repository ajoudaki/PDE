"""Analyze the prospectively specified direct-factor control without training.

Inputs are this study's frozen moment selection, the arrays named by that
selection, dense_reference01, and factor_control01. Only the explicitly named
archival dense pair for the two-outlier case is read outside this study.
Products are restricted to factor_analysis01. This is an author-side analysis,
not an independent reconstruction of the saved network states.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / "studies/neural_response_memory_20260922"
GENERATED = ROOT / "data/generated/neural_response_memory_20260922"
OUTPUT = GENERATED / "factor_analysis01"
os.environ.setdefault("MPLCONFIGDIR", str(OUTPUT / ".mpl-cache"))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

CASES = ("two_outliers_alternating", "quadrant_alternating", "quadrant_pairs",
         "quadrant_center_edges", "equal_mixed_odd")
ORDERS = (1, 3, 7)
SEEDS = (20260924, 20260925)
TITLES = ("Two outliers, alternating", "Quadrant, alternating",
          "Quadrant, paired labels", "Quadrant, center / edges",
          "Equal mixed odd (four representatives)")
LIMITS = dict(physical_mse_relative_error=.01, nested_grid_rms_difference=1e-5,
              endpoint_max_difference=.01, target_mse=.001, circle_nodes=8192)
STYLES = {"closure": ("Response-moment closure", "#0072b2", "o"),
          20260924: ("Direct factors: seed 20260924", "#d55e00", "^"),
          20260925: ("Direct factors: seed 20260925", "#009e73", "s")}


def relative(path):
    return str(Path(path).resolve().relative_to(ROOT))


def digest(path):
    result = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def array_digest(value):
    return hashlib.sha256(np.ascontiguousarray(value).tobytes()).hexdigest()


def rms(value):
    value = np.asarray(value)
    return float(np.sqrt(np.mean(value * value)))


def number(value):
    return "missing" if value is None else f"{value:.7g}"


def factor_score_text(row):
    if "status" in row and row["status"] != "fitted":
        return "not reached"
    return number(row.get("circle_rms"))


def read_arrays(path, extra=()):
    with np.load(path, allow_pickle=False) as archive:
        required = ("endpoint_prediction", "endpoint_angles")
        arrays = {name: archive[name] for name in required}
        arrays.update({name: archive[name] for name in extra if name in archive})
    return arrays


def validate_grid(arrays):
    angles, prediction = arrays["endpoint_angles"], arrays["endpoint_prediction"]
    expected = np.arange(LIMITS["circle_nodes"]) * (2 * np.pi / LIMITS["circle_nodes"])
    return bool(angles.shape == expected.shape and prediction.shape == expected.shape
                and np.all(np.isfinite(prediction)) and np.all(np.isfinite(angles))
                and np.allclose(angles, expected, atol=2e-14, rtol=0))


def error_metrics(arrays, reference):
    if not np.array_equal(arrays["endpoint_angles"], reference["endpoint_angles"]):
        raise ValueError("Endpoint grids differ; no interpolation or resampling is permitted")
    error = arrays["endpoint_prediction"] - reference["endpoint_prediction"]
    if not np.all(np.isfinite(error)):
        return dict(circle_rms=None, circle_rms_4096=None,
                    circle_sampled_max=None, nested_grid_rms_difference=None)
    full, nested = rms(error), rms(error[::2])
    return dict(circle_rms=full, circle_rms_4096=nested,
                circle_sampled_max=float(np.max(np.abs(error))),
                nested_grid_rms_difference=abs(full-nested))


def refinement(current, previous):
    if previous is None:
        return dict(endpoint_refinement_rms=None, endpoint_refinement_max=None)
    if not np.array_equal(current["endpoint_angles"], previous["endpoint_angles"]):
        raise ValueError("Refinement grids differ")
    difference = current["endpoint_prediction"] - previous["endpoint_prediction"]
    if not np.all(np.isfinite(difference)):
        return dict(endpoint_refinement_rms=None, endpoint_refinement_max=None)
    return dict(endpoint_refinement_rms=rms(difference),
                endpoint_refinement_max=float(np.max(np.abs(difference))))


def finalize_gates(row):
    row["gates"] = {key: bool(value) for key, value in row["gates"].items()}
    row["failed_gates"] = [key for key, passed in row["gates"].items() if not passed]
    row["valid"] = not row["failed_gates"]


def read_references(moment):
    references, metadata = {}, {}
    for case in CASES:
        fresh = moment["fresh_dense_references"].get(case)
        if fresh:
            selected_path = ROOT / fresh["selected_source"]
            previous_path = ROOT / fresh["previous_source"]
            summary = json.loads(selected_path.read_text())
            arrays_path, previous_arrays_path = (selected_path.with_name("arrays.npz"),
                                                previous_path.with_name("arrays.npz"))
            gates = dict(fit_status=summary["status"] == "fitted",
                         canonical_initialization=all(summary["initial_match"].values()),
                         physical_mse=abs(summary["loss"]/.001-1) <= .01,
                         previously_validated_reference=fresh["valid"])
            provenance = dict(kind="fresh dense reference", level=summary["level"],
                              source=relative(selected_path), source_sha256=digest(selected_path),
                              previous_source=relative(previous_path),
                              rtol=summary["rtol"], physical_training_mse=summary["loss"])
        else:
            if case != CASES[0]:
                raise ValueError(f"No frozen fresh reference for {case}")
            frozen = moment["dense_references"][case]
            arrays_path = ROOT / frozen["selected_archive"]
            previous_arrays_path = ROOT / frozen["coarser_archive"]
            gates = dict(previously_validated_reference=True)
            provenance = dict(kind="recorded refined archival dense reference",
                              source=relative(arrays_path),
                              previous_source=relative(previous_arrays_path),
                              validation_provenance="Prior moment campaign; archival training state is not replayed here.")
        arrays = read_arrays(arrays_path)
        previous = read_arrays(previous_arrays_path)
        change = refinement(arrays, previous)
        gates.update(uniform_8192_grid=validate_grid(arrays),
                     endpoint_refinement=change["endpoint_refinement_max"] is not None
                     and change["endpoint_refinement_max"] <= .01)
        row = dict(case=case, **provenance, **change, gates=gates,
                   arrays_source=relative(arrays_path), arrays_sha256=digest(arrays_path),
                   previous_arrays_source=relative(previous_arrays_path),
                   previous_endpoint_prediction_sha256=array_digest(previous["endpoint_prediction"]),
                   endpoint_prediction_sha256=array_digest(arrays["endpoint_prediction"]))
        finalize_gates(row)
        references[case], metadata[case] = arrays, row
    return references, metadata


def read_closures(moment, references, dense_metadata):
    selected, records = {}, {}
    for frozen in moment["selected"]:
        case, order = frozen["case"], int(frozen["P"])
        if case not in CASES or order not in ORDERS:
            continue
        path = (ROOT / frozen["source"]).with_name("arrays.npz")
        arrays = read_arrays(path, ("times", "losses", "training_inputs", "labels"))
        if array_digest(arrays["endpoint_prediction"]) != frozen["endpoint_prediction_sha256"]:
            raise ValueError(f"Frozen closure endpoint changed: {path}")
        previous_path = (ROOT / frozen["previous_level_source"]).with_name("arrays.npz")
        previous = read_arrays(previous_path)
        metrics = error_metrics(arrays, references[case])
        change = refinement(arrays, previous)
        gates = dict(prior_closure_numerical_gates=frozen["valid"],
                     common_dense_reference=dense_metadata[case]["valid"],
                     uniform_8192_grid=validate_grid(arrays),
                     endpoint_refinement=change["endpoint_refinement_max"] is not None
                     and change["endpoint_refinement_max"] <= .01,
                     nested_grid=metrics["nested_grid_rms_difference"] is not None
                     and metrics["nested_grid_rms_difference"] <= 1e-5)
        row = dict(case=case, P=order, rank=order*int(frozen["sample_count"]),
                   sample_count=int(frozen["sample_count"]), level=frozen["level"],
                   method="response_moment", source=frozen["source"],
                   source_sha256=frozen["source_sha256"], arrays_source=relative(path),
                   arrays_sha256=digest(path),
                   endpoint_prediction_sha256=array_digest(arrays["endpoint_prediction"]),
                   previous_arrays_source=relative(previous_path),
                   archival_target_circle_rms=frozen["circle_rms"],
                   physical_training_mse=frozen["physical_training_mse"],
                   time=frozen["time"], retained_W0_scalars=frozen["fixed_W0_scalars"],
                   moving_scalars=frozen["moving_scalars"],
                   prior_gates=frozen["gates"], gates=gates, **metrics, **change)
        row["numerical_sensitivity_max"] = max(change["endpoint_refinement_rms"],
                                                dense_metadata[case]["endpoint_refinement_rms"])
        row["precision_limited"] = (row["numerical_sensitivity_max"] >= row["circle_rms"]/3)
        finalize_gates(row)
        selected[(case, order)], records[(case, order)] = row, arrays
    missing = [(case, order) for case in CASES for order in ORDERS if (case, order) not in selected]
    if missing:
        raise ValueError(f"Frozen closure selection is incomplete: {missing}")
    return selected, records


def compare(closure, factor, dense):
    if factor is None:
        return dict(status="missing", directional_difference_resolved=False)
    factor_error, closure_error = factor["circle_rms"], closure["circle_rms"]
    sensitivities = [factor["endpoint_refinement_rms"],
                     closure["endpoint_refinement_rms"], dense["endpoint_refinement_rms"]]
    sensitivity = max(sensitivities) if all(value is not None for value in sensitivities) else None
    gap = factor_error-closure_error if factor_error is not None else None
    resolved = bool(factor["valid"] and closure["valid"] and gap is not None
                    and sensitivity is not None and abs(gap) > 3*sensitivity)
    ratio = factor_error/closure_error if factor_error is not None and closure_error > 0 else None
    substantial = bool(resolved and ratio is not None and (ratio >= 2 or ratio <= .5))
    if not factor["valid"] or not closure["valid"]:
        status = "inconclusive: numerical gate failure"
    elif not resolved:
        status = "numerically unresolved"
    else:
        status = ("closure lower" if gap > 0 else "factor lower") + (" (at least twofold)" if substantial else "")
    return dict(status=status, factor_minus_closure_rms=gap,
                factor_to_closure_rms_ratio=ratio, numerical_sensitivity_max=sensitivity,
                directional_difference_resolved=resolved, substantial_difference=substantial)


def panel_figure(title):
    fig, axes = plt.subplots(2, 3, figsize=(17, 9), squeeze=False)
    fig.suptitle(title+"\nWidth 2048; identical fixed W0; prescribed factor seeds reported separately", fontsize=14)
    fig.subplots_adjust(top=.87, bottom=.09, wspace=.29, hspace=.38)
    for ax, name in zip(axes.flat, TITLES):
        ax.set_title(name, fontsize=11)
        ax.grid(alpha=.2)
    axes.flat[-1].axis("off")
    return fig, list(axes.flat)


def save_figure(fig, stem):
    for extension in ("png", "pdf"):
        fig.savefig(OUTPUT / f"{stem}.{extension}", dpi=180, bbox_inches="tight")
    plt.close(fig)


def plot_scores(closures, factors, dense):
    fig, axes = panel_figure("Dense-function RMS at each model's own training-MSE 0.001 endpoint")
    for ax, case in zip(axes, CASES):
        for method in ("closure", *SEEDS):
            label, color, marker = STYLES[method]
            rows = [closures[(case, order)] if method == "closure" else factors.get((case, order, method))
                    for order in ORDERS]
            ranks = [order*closures[(case, order)]["sample_count"] for order in ORDERS]
            errors = [row["circle_rms"] if row and row["circle_rms"] is not None else np.nan for row in rows]
            ax.semilogy(ranks, errors, color=color, lw=1.9, label=label)
            for rank, error, row in zip(ranks, errors, rows):
                if row is None or not np.isfinite(error):
                    continue
                ax.plot(rank, error, marker, color=color, ms=6,
                        markerfacecolor=color if row["valid"] else "white")
                if row.get("precision_limited"):
                    ax.annotate("*", (rank, error), xytext=(4, 5), textcoords="offset points", color=color)
        ax.axhline(dense[case]["endpoint_refinement_rms"], color="#777777", ls=":", lw=1,
                   label="Dense refinement RMS scale")
        ticks = [closures[(case, order)]["rank"] for order in ORDERS]
        ax.set(xticks=ticks, xlabel="Rank of learned correction",
               ylabel="Circle RMS vs selected dense endpoint")
        ax.margins(x=.1, y=.2)
    handles, labels = axes[0].get_legend_handles_labels()
    axes[-1].legend(handles, labels, loc="upper left", frameon=False, fontsize=11)
    axes[-1].text(0, .58,
                  "Orders P=1,3,7; ranks matched within each task.\n\n"
                  "Missing or non-hit factors are omitted.\n"
                  "Hollow markers: numerical gates unresolved.\n"
                  "*: observed refinement sensitivity ≥ RMS / 3.\n\n"
                  "Dense refinement is an observed sensitivity,\nnot a certified error bound.",
                  transform=axes[-1].transAxes, fontsize=11, va="top")
    save_figure(fig, "rms_vs_rank")


def plot_functions(order, closures, closure_arrays, factors, factor_arrays, references):
    fig, axes = panel_figure(f"P={order}: learned functions at each model's own training-MSE 0.001 endpoint")
    for ax, case in zip(axes, CASES):
        reference = references[case]
        angles = np.rad2deg(reference["endpoint_angles"])
        ax.plot(angles, reference["endpoint_prediction"], color="black", lw=2, label="Selected dense endpoint")
        for method in ("closure", *SEEDS):
            label, color, _ = STYLES[method]
            row = closures[(case, order)] if method == "closure" else factors.get((case, order, method))
            arrays = closure_arrays[(case, order)] if method == "closure" else factor_arrays.get((case, order, method))
            if row is None or arrays is None:
                continue
            if method != "closure" and row["status"] != "fitted":
                continue
            ax.plot(angles, arrays["endpoint_prediction"], color=color, lw=1.3,
                    ls="-" if method == "closure" else "--" if method == SEEDS[0] else "-.",
                    label=label+("" if row["valid"] else " [unresolved]"))
        inputs = closure_arrays[(case, order)]["training_inputs"]
        training_angles = np.rad2deg(np.arctan2(inputs[:, 1], inputs[:, 0])) % 360
        ax.scatter(training_angles, closure_arrays[(case, order)]["labels"], color="black", marker="x", s=25,
                   label="Represented training labels", zorder=6)
        ax.set(xlabel="Angle (degrees)", ylabel="Network output", xlim=(0, 360))
    handles = [Line2D([], [], color="black", lw=2, label="Selected dense endpoint")]
    for method in ("closure", *SEEDS):
        label, color, _ = STYLES[method]
        handles.append(Line2D([], [], color=color, lw=1.3,
                              ls="-" if method == "closure" else "--" if method == SEEDS[0] else "-.", label=label))
    handles.append(Line2D([], [], color="black", marker="x", ls="none", label="Represented training labels"))
    axes[-1].legend(handles=handles, loc="upper left", frameon=False, fontsize=10)
    axes[-1].text(0, .53,
                  "Both seeds are retained without choosing a winner.\n"
                  "Missing or non-hit factors are omitted.\n\n"
                  "Models reach the same training-loss threshold\nat different physical times.\n\n"
                  "Full-circle discrepancy measures agreement\nwith the dense learned function.\n\n"
                  "No target label function is imposed on the circle.",
                  transform=axes[-1].transAxes, fontsize=11, va="top")
    save_figure(fig, f"endpoint_functions_P{order}")


def write_summary(payload):
    lines = ["# Direct-factor control versus response moments", "",
             "Primary metric: RMS prediction difference on 8192 uniform circle nodes from the same selected dense endpoint. Each model stops at its own first physical training-MSE 0.001 crossing.", "",
             "The direct control trains W2 = W0 + AB by Euclidean gradient flow with unit factor mobilities, A(0)=0, and independent B(0) entries of variance 1/r. Outer mobilities remain 2048. This matches the dense initial matrix velocity only in expectation over the factor draw; it defines a different realized flow.", "",
             "The finest saved numerical level is selected regardless of its score. Both prescribed factor seeds are reported separately; the range only spans those two seeds. No rates are fitted.", "",
             "| Case | P | Rank | Closure RMS | Factor seed 20260924 | Factor seed 20260925 | Two-seed range |",
             "|---|---:|---:|---:|---:|---:|---:|"]
    for row in payload["paired_comparisons"]:
        first, second = row["factors"]
        scores = [entry.get("circle_rms") for entry in (first, second)]
        interval = (f"[{number(min(scores))}, {number(max(scores))}]"
                    if all(value is not None for value in scores) else "incomplete")
        lines.append(f"| {row['case']} | {row['P']} | {row['rank']} | {number(row['closure']['circle_rms'])} | {factor_score_text(first)} | {factor_score_text(second)} | {interval} |")
    lines += ["", "Every row above uses the same dense target for all three models. 'Not reached' means the saved trajectory did not attain MSE 0.001; its terminal-state discrepancy is retained only as a diagnostic in the JSON and is omitted from the endpoint plots. Scores are approximation to dense learning, not held-out label error.", "",
              "| Case | P | Seed | Factor level | Checks | Factor refinement RMS / max | 3 × combined sensitivity | Comparison |",
              "|---|---:|---:|---:|---|---:|---:|---|"]
    for row in payload["paired_comparisons"]:
        for factor, comparison in zip(row["factors"], row["comparisons"]):
            sensitivity = comparison.get("numerical_sensitivity_max")
            lines.append(f"| {row['case']} | {row['P']} | {factor['factor_seed']} | {factor.get('level', 'missing')} | {factor.get('valid', False)} | {number(factor.get('endpoint_refinement_rms'))} / {number(factor.get('endpoint_refinement_max'))} | {number(3*sensitivity if sensitivity is not None else None)} | {comparison['status']} |")
    lines += ["", "A direction is resolved only when both methods pass their numerical gates and the RMS score gap exceeds three times the largest factor, closure, or dense refinement RMS change. Here each source uses its finest selected endpoint versus its nearest coarser endpoint; the maximum is across those three sources. Earlier adjacent factor changes remain in the JSON. A twofold difference is called substantial only after that check. These changes are empirical sensitivities, not certified bounds.", "",
              "Closure error precision flags:"]
    lines.extend(f"- {row['case']} P={row['P']}: RMS {number(row['circle_rms'])}; observed max(closure, dense) refinement RMS {number(row['numerical_sensitivity_max'])}."
                 for row in payload["closure_selected"] if row["precision_limited"])
    lines += ["", "Unresolved factor cells:"]
    failures = [row for row in payload["factor_selected"] if not row["valid"]]
    lines.extend(f"- {row['case']} P={row['P']} seed={row['factor_seed']}: {', '.join(row['failed_gates'])}." for row in failures)
    if not failures:
        lines.append("- None among saved selected endpoints.")
    lines += ["", "Missing primary trajectories and incomplete outputs:"]
    lines.extend(f"- {entry}" for entry in payload["missing_primary_trajectories"] + payload["incomplete_outputs"])
    if not payload["missing_primary_trajectories"] and not payload["incomplete_outputs"]:
        lines.append("- None.")
    lines += ["", "Dense target provenance:"]
    lines.extend(f"- {case}: `{row['arrays_source']}`; refinement RMS {number(row['endpoint_refinement_rms'])}; gates pass: {row['valid']}."
                 for case, row in payload["dense_references"].items())
    if payload["producer_source_discrepancies"]:
        lines += ["", "Producer source hashes differing from current frozen files:"]
        lines.extend(f"- `{row['source']}`: `{row['name']}` recorded `{row['recorded_sha256']}`, current `{row['current_sha256']}`."
                     for row in payload["producer_source_discrepancies"])
    lines += ["", "The correction rank bound is P times represented sample count: 8/24/56 for eight-sample cases and 4/12/28 for the exact four-representative antipodal quotient. Both methods retain dense W0; factor coordinate counts match the two history-factor arrays, while the closure has additional lifted state. Rank does not match total state, time, or compute.", "",
              "This analyzer recomputes circle discrepancies, nested-grid agreement, and saved endpoint refinement changes. Closure dynamical checks and factor initialization/physical-loss checks retain their stated producer provenance. This output is not an independent reconstruction audit.", "",
              "The JSON records all levels, failures, numerical gates, and source hashes. The scientific scope is the specified finite-width flows at the tested ranks and two fixed factor seeds; no optimality claim, fitted convergence rate, or general statistical conclusion follows. QR/SVD truncation and other low-rank algorithms are not evaluated."]
    (OUTPUT / "summary.md").write_text("\n".join(lines)+"\n")


def read_factors(references, dense_metadata):
    """Read every endpoint; highest level wins even when it is a failed run."""
    grouped, incomplete, seen = {}, [], set()
    manifest = []
    run_root = GENERATED / "factor_control01"
    for directory in sorted(path for path in run_root.glob("*_factor_P*_seed*_level*") if path.is_dir()):
        summary_path, arrays_path = directory / "summary.json", directory / "arrays.npz"
        config_path = directory / "config.json"
        if not all(path.exists() for path in (summary_path, arrays_path, config_path)):
            incomplete.append(dict(source=relative(directory), reason="missing summary, arrays, or config"))
            match = re.fullmatch(r"(.+)_factor_P(\d+)_seed(\d+)_level(\d+)", directory.name)
            if match:
                case, order, seed, level = match.group(1), *map(int, match.groups()[1:])
                if case in CASES and order in ORDERS and seed in SEEDS:
                    grouped.setdefault((case, order, seed), []).append(dict(level=level, unavailable=True))
            continue
        summary, config = json.loads(summary_path.read_text()), json.loads(config_path.read_text())
        case, order, seed, level = (summary["case"], int(summary["P"]),
                                   int(summary["factor_seed"]), int(summary["level"]))
        if case not in CASES or order not in ORDERS or seed not in SEEDS or level not in (0, 1, 2):
            raise ValueError(f"Unexpected factor cell in assigned run root: {directory}")
        for key, value in (("case", case), ("P", order), ("factor_seed", seed), ("level", level)):
            if config[key] != value:
                raise ValueError(f"Summary/config mismatch: {directory}: {key}")
        key = (case, order, seed)
        if (*key, level) in seen:
            raise ValueError(f"Duplicate factor level for {key}, level {level}")
        seen.add((*key, level))
        archive_hash = digest(arrays_path)
        if archive_hash != summary["arrays_sha256"]:
            raise ValueError(f"Factor archive SHA-256 mismatch: {arrays_path}")
        manifest.append(dict(case=case, P=order, factor_seed=seed, level=level,
                             status=summary["status"], source=relative(summary_path),
                             source_sha256=digest(summary_path), arrays_sha256=archive_hash,
                             config_sha256=digest(config_path),
                             producer_source_sha256=summary.get("source_sha256", {}),
                             integration_seconds=summary.get("integration_seconds", 0),
                             wall_seconds=summary.get("wall_seconds", 0),
                             exception=summary.get("exception")))
        required = ("endpoint_prediction", "endpoint_angles", "w", "c", "A", "B",
                    "training_prediction", "labels", "training_inputs", "reference_endpoint_prediction")
        with np.load(arrays_path, allow_pickle=False) as archive:
            missing = [name for name in required if name not in archive]
            if missing:
                incomplete.append(dict(case=case, P=order, factor_seed=seed, level=level,
                                       source=relative(arrays_path), status=summary["status"],
                                       reason="missing arrays: " + ", ".join(missing)))
                grouped.setdefault(key, []).append(dict(level=level, unavailable=True,
                                                        summary=summary, config=config))
                continue
            arrays = {name: archive[name] for name in required}
            arrays.update({name: archive[name] for name in ("times", "losses", "snapshot_times",
                                                           "matched_time_rms") if name in archive})
        state_finite = all(np.all(np.isfinite(arrays[name])) for name in ("w", "c", "A", "B"))
        rank, sample_count, width = config["rank"], config["sample_count"], config["width"]
        state_shapes = (arrays["w"].shape == (width, 2) and arrays["c"].shape == (width,)
                        and arrays["A"].shape == (width, rank) and arrays["B"].shape == (rank, width))
        # These arrays are no longer needed; an independent auditor replays them.
        for name in ("w", "c", "A", "B"):
            del arrays[name]
        metrics = error_metrics(arrays, references[case])
        physical_mse = float(np.mean((arrays["training_prediction"]-arrays["labels"])**2))
        checks, initial = summary.get("initial_checks") or {}, summary.get("initial_match") or {}
        expected_samples = 4 if case == "equal_mixed_odd" else 8
        gates = dict(fit_status=summary["status"] == "fitted",
                     protocol_configuration=width == 2048 and sample_count == expected_samples
                     and rank == order*expected_samples and config["network_seed"] == 20260920
                     and config["dtype"] == "float64"
                     and config["threshold"] == .001
                     and summary["rtol"] == config["rtol"] == 6.25e-5/4**level
                     and summary["atol"] == config["atol"] == 6.25e-7/4**level
                     and config["mobilities"] == dict(w=2048, c=2048, A=1, B=1),
                     canonical_initialization=all(initial.get(name) is True for name in ("w", "c", "W0")),
                     zero_initial_correction=checks.get("A_is_zero") is True
                     and checks.get("correction_frobenius") == 0,
                     nonzero_random_factor=checks.get("B_is_nonzero") is True,
                     finite_state=state_finite, expected_state_shapes=state_shapes,
                     uniform_8192_grid=validate_grid(arrays),
                     physical_mse=np.isfinite(physical_mse) and abs(physical_mse/.001-1) <= .01,
                     producer_loss_agreement=np.isfinite(physical_mse)
                     and np.isclose(physical_mse, summary.get("endpoint_loss_recomputed", np.nan),
                                    atol=1e-12, rtol=1e-10),
                     common_dense_reference=dense_metadata[case]["valid"],
                     nested_grid=metrics["nested_grid_rms_difference"] is not None
                     and metrics["nested_grid_rms_difference"] <= 1e-5)
        archived_error = arrays["endpoint_prediction"]-arrays["reference_endpoint_prediction"]
        archival_rms = rms(archived_error) if np.all(np.isfinite(archived_error)) else None
        gates["archival_score_agreement"] = (archival_rms is not None and
            np.isclose(archival_rms, summary.get("circle_rms", np.nan), atol=1e-12, rtol=1e-10))
        row = dict(case=case, P=order, rank=rank, factor_seed=seed, level=level,
                   method="direct_factor", status=summary["status"], rtol=summary["rtol"],
                   atol=summary["atol"], sample_count=sample_count, time=summary["time"],
                   physical_training_mse=physical_mse if np.isfinite(physical_mse) else None,
                   physical_loss_provenance="Recomputed MSE of producer-saved physical training predictions; state replay is a separate audit.",
                   source=relative(summary_path), source_sha256=digest(summary_path),
                   arrays_source=relative(arrays_path), arrays_sha256=archive_hash,
                   endpoint_prediction_sha256=array_digest(arrays["endpoint_prediction"]),
                   config_source=relative(config_path), config_sha256=digest(config_path),
                   producer_source_sha256=summary["source_sha256"],
                   archival_target_source=config["reference"], archival_target_circle_rms=archival_rms,
                   archival_endpoint_prediction_sha256=array_digest(arrays["reference_endpoint_prediction"]),
                   moving_scalars=config["moving_scalars"], fixed_W0_scalars=config["fixed_W0_scalars"],
                   initial_match=initial, initial_checks=checks, gates=gates, **metrics)
        row["terminal_function_metrics"] = dict(metrics)
        row["terminal_archival_target_circle_rms"] = archival_rms
        if summary["status"] != "fitted":
            # A capped terminal state is not an own-MSE-.001 endpoint.
            for name in ("circle_rms", "circle_rms_4096", "circle_sampled_max"):
                row[name] = None
            row["archival_target_circle_rms"] = None
        finalize_gates(row)
        grouped.setdefault(key, []).append(dict(level=level, unavailable=False, row=row, arrays=arrays))
    selected, selected_arrays, all_levels = {}, {}, []
    for key, records in grouped.items():
        records.sort(key=lambda record: record["level"])
        usable = [record for record in records if not record["unavailable"]]
        for record in usable:
            all_levels.append(record["row"])
        if not usable:
            continue
        record = usable[-1]
        row = dict(record["row"], gates=dict(record["row"]["gates"]))
        previous = usable[-2] if len(usable) > 1 else None
        change = refinement(record["arrays"], previous["arrays"] if previous else None)
        row.update(change)
        row["previous_source"] = previous["row"]["source"] if previous else None
        row["adjacent_refinement_changes"] = [dict(from_level=left["level"], to_level=right["level"],
             **refinement(right["arrays"], left["arrays"])) for left, right in zip(usable, usable[1:])]
        row["gates"].update(refinement_available=previous is not None,
                            primary_levels_present=all((*key, level) in seen for level in (0, 1)),
                            finer_attempt_complete=record["level"] == records[-1]["level"],
                            finer_than_comparison=previous is not None
                            and row["rtol"] < previous["row"]["rtol"],
                            coarser_endpoint_fitted=previous is not None and previous["row"]["status"] == "fitted",
                            endpoint_refinement=change["endpoint_refinement_max"] is not None
                            and change["endpoint_refinement_max"] <= .01)
        sensitivities = (change["endpoint_refinement_rms"], dense_metadata[key[0]]["endpoint_refinement_rms"])
        row["numerical_sensitivity_max"] = max(sensitivities) if all(value is not None for value in sensitivities) else None
        row["numerical_sensitivity_unavailable"] = row["numerical_sensitivity_max"] is None
        row["precision_limited"] = (row["numerical_sensitivity_max"] is not None and row["circle_rms"] is not None
                                     and row["numerical_sensitivity_max"] >= row["circle_rms"]/3)
        finalize_gates(row)
        selected[key], selected_arrays[key] = row, record["arrays"]
    missing = [dict(case=case, P=order, factor_seed=seed, level=level)
               for case in CASES for order in ORDERS for seed in SEEDS for level in (0, 1)
               if (case, order, seed, level) not in seen]
    return selected, selected_arrays, all_levels, manifest, missing, incomplete


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=OUTPUT)
    args = parser.parse_args()
    if args.out.resolve() != OUTPUT:
        parser.error("This scoped analyzer writes only factor_analysis01")
    moment_path = GENERATED / "analysis01/metrics.json"
    moment = json.loads(moment_path.read_text())
    references, dense = read_references(moment)
    closures, closure_arrays = read_closures(moment, references, dense)
    factors, factor_arrays, all_levels, manifest, missing, incomplete = read_factors(references, dense)
    paired = []
    for case in CASES:
        for order in ORDERS:
            closure = closures[(case, order)]
            entries = [factors.get((case, order, seed)) for seed in SEEDS]
            paired.append(dict(case=case, P=order, rank=closure["rank"], closure=closure,
                               factors=[row if row else dict(factor_seed=seed, circle_rms=None, valid=False)
                                        for seed, row in zip(SEEDS, entries)],
                               comparisons=[compare(closure, row, dense[case]) for row in entries]))
    source_paths = (Path(__file__), STUDY / "FACTOR_CONTROL_PROTOCOL.md", moment_path,
                    STUDY / "run_factor_control.py", STUDY / "factor_control_engine.py")
    producer_current_hashes = {name: digest(STUDY / name) for name in
                              ("FACTOR_CONTROL_PROTOCOL.md", "run_factor_control.py", "factor_control_engine.py")}
    source_discrepancies = [dict(source=row["source"], name=name,
                                 recorded_sha256=row["producer_source_sha256"].get(name),
                                 current_sha256=expected)
                           for row in manifest for name, expected in producer_current_hashes.items()
                           if row["producer_source_sha256"].get(name) != expected]
    payload = dict(created_utc=datetime.now(timezone.utc).isoformat(),
                   selection="Highest saved numerical level per (case,P,seed), regardless of score; a later incomplete attempt invalidates fallback. Refinement uses the nearest saved coarser endpoint; every adjacent change is also retained.",
                   metric="sqrt(mean((model_endpoint_prediction-dense_endpoint_prediction)**2)) on 8192 common uniform circle nodes; own training-MSE 0.001 endpoints.",
                   comparison_rule="Direction resolved only after numerical gates and |factor RMS-closure RMS| > 3*max(selected factor refinement RMS,selected closure refinement RMS,dense refinement RMS). At least twofold then means substantial.",
                   claim_scope="Specified finite-width trajectories and two fixed factor seeds; no seed selection, optimized factor scaling, full-circle target labels, or fitted asymptotic rates.",
                   validation_scope="Author-side analysis of saved endpoints; this does not replace an independent state reconstruction audit.",
                   factor_control=dict(matrix="W2=W0+A@B", initialization="A=0; independent B entries N(0,1/r)",
                                       factor_mobilities=dict(A=1, B=1), outer_mobilities=dict(w=2048, c=2048),
                                       network_seed=20260920, factor_seeds=list(SEEDS),
                                       velocity_caveat="Expected initial induced matrix velocity matches dense GF; realized factor GF is different."),
                   gates=LIMITS, seed_policy="Report both seeds individually and their range; no best-of-seeds method score.",
                   dense_references=dense, closure_selected=list(closures.values()),
                   factor_selected=list(factors.values()), factor_all_levels=all_levels,
                   run_manifest=manifest, paired_comparisons=paired,
                   missing_primary_trajectories=missing, incomplete_outputs=incomplete,
                   producer_source_discrepancies=source_discrepancies,
                   missing_selected_cells=[dict(case=case, P=order, factor_seed=seed)
                                           for case in CASES for order in ORDERS for seed in SEEDS
                                           if (case, order, seed) not in factors],
                   integration_budget=dict(recorded_trajectories=len(manifest),
                                           primary_trajectories=sum(row["level"] < 2 for row in manifest),
                                           conditional_level2_trajectories=sum(row["level"] == 2 for row in manifest),
                                           integration_seconds=sum(row["integration_seconds"] for row in manifest),
                                           wall_seconds=sum(row["wall_seconds"] for row in manifest),
                                           integration_seconds_cap=3600, primary_cap=60, level2_cap=15),
                   source_sha256={relative(path): digest(path) for path in source_paths})
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "metrics.json").write_text(json.dumps(payload, indent=2, allow_nan=False)+"\n")
    write_summary(payload)
    plot_scores(closures, factors, dense)
    for order in (3, 7):
        plot_functions(order, closures, closure_arrays, factors, factor_arrays, references)
    print(json.dumps(dict(output=relative(OUTPUT), saved_factor_cells=len(factors),
                          valid_factor_cells=sum(row["valid"] for row in factors.values()),
                          missing_primary_trajectories=missing, incomplete_outputs=incomplete,
                          missing_selected_cells=payload["missing_selected_cells"],
                          failed_selected=[dict(case=row["case"], P=row["P"], factor_seed=row["factor_seed"],
                                                level=row["level"], failed_gates=row["failed_gates"])
                                           for row in factors.values() if not row["valid"]]), indent=2))


if __name__ == "__main__":
    main()
