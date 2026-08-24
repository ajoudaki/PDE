"""Evaluate the separately preregistered quadratic step-halving confirmation."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

import numpy as np

from analyze_quadratic_l2_joint_limit import (
    CURVE_GRID,
    SCIENCE_THRESHOLDS,
    bootstrap_slope,
    finite_through_registered_endpoint,
    load,
    median,
    paired_curve_error,
    percentile,
    qkey,
    record_at,
    slope,
)


FINE_DELTA = 0.000625
COMPARISON_DELTA = 0.00125
OLD_COMPARISON_DELTA = 0.0025


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--confirmation", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    primary_meta, primary_runs, primary_errors = load(args.primary)
    confirm_meta, confirm_runs, confirm_errors = load(args.confirmation)
    primary_config = primary_meta["arguments"]
    confirm_config = confirm_meta["arguments"]
    for field in ("widths", "keys", "horizon"):
        if primary_config[field] != confirm_config[field]:
            raise ValueError(f"mismatched {field}")
    if [float(value) for value in confirm_config["deltas"]] != [FINE_DELTA]:
        raise ValueError("confirmation contains an unregistered step size")

    widths = sorted(primary_config["widths"])
    keys = sorted(primary_config["keys"])
    horizon = float(primary_config["horizon"])
    runs = dict(primary_runs)
    overlap = set(runs).intersection(confirm_runs)
    if overlap:
        raise ValueError(f"duplicate runs: {sorted(overlap)[:3]}")
    runs.update(confirm_runs)
    missing_confirmation = [
        [n, key]
        for n in widths
        for key in keys
        if (n, key, FINE_DELTA) not in runs
    ]
    nonfinite_confirmation = [
        {
            "n": n,
            "key": key,
            "failure_time": runs[(n, key, FINE_DELTA)].get("failure_time"),
        }
        for n in widths
        for key in keys
        if (n, key, FINE_DELTA) in runs
        and not runs[(n, key, FINE_DELTA)]["finite"]
    ]
    fine_endpoint_failures = [
        [n, key]
        for n in widths
        for key in keys
        if (n, key, FINE_DELTA) not in runs
        or not finite_through_registered_endpoint(
            runs[(n, key, FINE_DELTA)], horizon
        )
    ]

    validity = (
        not primary_errors
        and not confirm_errors
        and not missing_confirmation
        and not fine_endpoint_failures
    )
    step_audit = {}
    all_loss_increases = []
    all_defects = []
    for n in widths:
        new_errors = []
        old_errors = []
        hitting_differences = defaultdict(list)
        for key in keys:
            fine = runs[(n, key, FINE_DELTA)]
            comparison = runs[(n, key, COMPARISON_DELTA)]
            old_comparison = runs[(n, key, OLD_COMPARISON_DELTA)]
            new_error = paired_curve_error(comparison, fine, horizon)
            old_error = paired_curve_error(old_comparison, comparison, horizon)
            if new_error is not None:
                new_errors.append(new_error)
            if old_error is not None:
                old_errors.append(old_error)
            for q in SCIENCE_THRESHOLDS:
                tc = comparison["hitting_times"][qkey(q)]
                tf = fine["hitting_times"][qkey(q)]
                if tc is not None and tf is not None:
                    hitting_differences[qkey(q)].append(abs(tc - tf))
            for record in fine["records"][:-1]:
                if record["loss_increment"] is not None:
                    all_loss_increases.append(record["loss_increment"])
                if record["flow_defect"] is not None:
                    all_defects.append(record["flow_defect"])
        complete = len(new_errors) == len(keys)
        p95 = percentile(new_errors, 0.95) if new_errors else None
        hit_medians = {
            qkey(q): (
                median(hitting_differences[qkey(q)])
                if len(hitting_differences[qkey(q)]) == len(keys)
                else None
            )
            for q in SCIENCE_THRESHOLDS
        }
        new_median = median(new_errors) if new_errors else None
        old_median = median(old_errors) if old_errors else None
        step_audit[str(n)] = {
            "complete_curve_pairs": complete,
            "curve_error_p95": p95,
            "curve_error_max": float(max(new_errors)) if new_errors else None,
            "curve_error_median": new_median,
            "old_over_new_median_error_ratio": (
                old_median / new_median
                if old_median is not None and new_median not in (None, 0.0)
                else None
            ),
            "hitting_time_abs_diff_median": hit_medians,
        }
        validity &= complete and p95 is not None and p95 <= 0.01
        validity &= all(
            value is not None and value <= 0.005 for value in hit_medians.values()
        )

    max_loss_increase = float(max(all_loss_increases, default=float("inf")))
    median_defect = median(all_defects) if all_defects else float("inf")
    validity &= max_loss_increase <= 1e-5 and median_defect < 0.01

    hitting_summary = {}
    for q_index, q in enumerate(SCIENCE_THRESHOLDS):
        grouped = defaultdict(list)
        for n in widths:
            for key in keys:
                value = runs[(n, key, FINE_DELTA)]["hitting_times"][qkey(q)]
                if value is not None:
                    grouped[n].append(value)
        complete = all(len(grouped[n]) == len(keys) for n in widths)
        if complete and all(value > 0.0 for n in widths for value in grouped[n]):
            medians = {str(n): median(grouped[n]) for n in widths}
            values = [medians[str(n)] for n in widths]
            hitting_summary[qkey(q)] = {
                "width_medians": medians,
                "endpoint_ratio_2048_over_128": values[-1] / values[0],
                "loglog_slope": slope(np.asarray(widths), np.asarray(values)),
                "bootstrap_95": bootstrap_slope(grouped, 2026082600 + q_index),
            }
        else:
            hitting_summary[qkey(q)] = {"complete": False}

    curve_medians = {}
    for n in widths:
        curve_medians[str(n)] = {
            str(t): median(
                [
                    record_at(runs[(n, key, FINE_DELTA)], t)["f"]
                    for key in keys
                ]
            )
            for t in CURVE_GRID
        }
    curve_difference_1024_2048 = max(
        abs(curve_medians["1024"][str(t)] - curve_medians["2048"][str(t)])
        for t in CURVE_GRID
    )

    k0_grouped = defaultdict(list)
    kpre_grouped = defaultdict(list)
    condensation0_grouped = defaultdict(list)
    condensation_pre_grouped = defaultdict(list)
    for n in widths:
        for key in keys:
            records = runs[(n, key, FINE_DELTA)]["records"]
            before = [record for record in records if record["f"] < 0.75]
            k0_grouped[n].append(records[0]["K"])
            kpre_grouped[n].append(max(record["K"] for record in before))
            condensation0_grouped[n].append(records[0]["readout_condensation"])
            condensation_pre_grouped[n].append(
                max(record["readout_condensation"] for record in before)
            )
    k_summary = {}
    for label, grouped in (("K0", k0_grouped), ("K_pre_f_075_max", kpre_grouped)):
        medians = {str(n): median(grouped[n]) for n in widths}
        values = [medians[str(n)] for n in widths]
        ratio = values[-1] / values[0]
        k_summary[label] = {
            "width_medians": medians,
            "symmetric_endpoint_factor": max(ratio, 1.0 / ratio),
            "loglog_slope": slope(np.asarray(widths), np.asarray(values)),
        }
    tail_summary = {
        label: {
            "width_medians": {str(n): median(grouped[n]) for n in widths}
        }
        for label, grouped in (
            ("readout_condensation_initial", condensation0_grouped),
            ("readout_condensation_max_pre_f_075", condensation_pre_grouped),
        )
    }

    regular_conditions = []
    boundary_conditions = []
    for q in SCIENCE_THRESHOLDS:
        summary = hitting_summary[qkey(q)]
        if "width_medians" not in summary:
            regular_conditions.append(False)
            if q <= 0.75:
                boundary_conditions.append(False)
            continue
        regular_conditions.append(
            0.75 <= summary["endpoint_ratio_2048_over_128"] <= 1.25
            and -0.10 <= summary["loglog_slope"] <= 0.10
            and summary["bootstrap_95"][0] > -0.20
            and summary["bootstrap_95"][1] < 0.20
        )
        if q <= 0.75:
            boundary_conditions.append(
                summary["endpoint_ratio_2048_over_128"] < 0.5
                and summary["bootstrap_95"][1] < -0.20
            )
    k_regular = all(
        value["symmetric_endpoint_factor"] < 1.5
        and value["loglog_slope"] < 0.20
        for value in k_summary.values()
    )
    regular = (
        validity
        and all(regular_conditions)
        and curve_difference_1024_2048 <= 0.05
        and k_regular
    )
    last_three_f001 = [curve_medians[str(n)][str(0.01)] for n in widths[-3:]]
    early_boundary = (
        last_three_f001[0] < last_three_f001[1] < last_three_f001[2]
        and last_three_f001[-1] > 0.75
    )
    boundary = validity and (all(boundary_conditions) or early_boundary)
    if regular:
        verdict = "confirmatory_evidence_against_polynomially_visible_instantaneous_jump"
    elif boundary:
        verdict = "confirmatory_evidence_for_visible_shrinking_boundary_layer"
    else:
        verdict = "confirmatory_experiment_inconclusive"

    result = {
        "primary": str(args.primary),
        "confirmation": str(args.confirmation),
        "primary_historical_verdict": "inconclusive",
        "errors": primary_errors + confirm_errors,
        "missing_confirmation": missing_confirmation,
        "nonfinite_confirmation": nonfinite_confirmation,
        "validity": {
            "passed": bool(validity),
            "fine_endpoint_failures": fine_endpoint_failures,
            "step_audit": step_audit,
            "max_fine_step_loss_increase": max_loss_increase,
            "median_fine_step_flow_defect": median_defect,
        },
        "hitting_times": hitting_summary,
        "fine_predictor_width_medians": curve_medians,
        "max_curve_difference_1024_2048": float(curve_difference_1024_2048),
        "kernel": k_summary,
        "tail_diagnostics": tail_summary,
        "verdict": verdict,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(
        json.dumps(
            {
                "validity": validity,
                "verdict": verdict,
                "step_audit": step_audit,
                "hitting_times": hitting_summary,
                "max_curve_difference_1024_2048": curve_difference_1024_2048,
                "kernel": k_summary,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
