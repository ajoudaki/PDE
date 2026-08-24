"""Mechanical evaluator for the preregistered quadratic L=2 experiment."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

import numpy as np


SCIENCE_THRESHOLDS = (0.25, 0.50, 0.75, 0.90)
CURVE_GRID = (0.0, 0.005, 0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.0, 2.0)
FINE_DELTA = 0.00125
COMPARISON_DELTA = 0.0025


def qkey(q: float) -> str:
    return str(float(q))


def percentile(values, q):
    return float(np.quantile(np.asarray(values, dtype=float), q))


def median(values):
    return float(np.median(np.asarray(values, dtype=float)))


def slope(widths, values):
    return float(np.polyfit(np.log(widths), np.log(values), 1)[0])


def bootstrap_slope(grouped, seed: int, reps: int = 5000):
    widths = np.asarray(sorted(grouped), dtype=float)
    rng = np.random.default_rng(seed)
    draws = np.empty(reps, dtype=float)
    for b in range(reps):
        width_medians = []
        for n in widths.astype(int):
            values = np.asarray(grouped[n], dtype=float)
            sample = rng.choice(values, size=values.size, replace=True)
            width_medians.append(np.median(sample))
        draws[b] = slope(widths, np.asarray(width_medians))
    return [float(x) for x in np.quantile(draws, [0.025, 0.975])]


def record_at(run, t: float):
    delta = run["delta"]
    index = int(round(t / delta))
    if index >= len(run["records"]):
        return None
    record = run["records"][index]
    if abs(record["t"] - t) > 1e-9:
        raise ValueError((record["t"], t, delta))
    return record


def paired_curve_error(coarse, fine, horizon: float):
    """Maximum discrepancy on the full registered common horizon."""
    errors = []
    for record in coarse["records"]:
        if record["t"] > horizon + 1e-12:
            break
        fine_record = record_at(fine, record["t"])
        if fine_record is None:
            return None
        errors.append(abs(record["f"] - fine_record["f"]))
    if not errors or coarse["records"][-1]["t"] < horizon - 1e-9:
        return None
    return float(max(errors))


def load(path: Path):
    metadata = None
    runs = {}
    errors = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            if row["kind"] == "metadata":
                metadata = row
            elif row["kind"] == "error":
                errors.append(row)
            elif row["kind"] == "bundle":
                for run in row["runs"]:
                    runs[(row["n"], row["key"], float(run["delta"]))] = run
            else:
                raise ValueError(f"unknown row kind {row['kind']}")
    if metadata is None:
        raise ValueError("missing metadata")
    return metadata, runs, errors


def finite_through_registered_endpoint(run, horizon: float):
    """Fine validity ends at the first .95 crossing, or T if no crossing."""
    t95 = run["hitting_times"].get(qkey(0.95))
    required = horizon if t95 is None else t95
    last = run.get("last_finite_time")
    return last is not None and last + 1e-9 >= required


def descriptive_width_summary(grouped, widths):
    return {
        str(n): {
            "median": median(grouped[n]),
            "min": float(min(grouped[n])),
            "max": float(max(grouped[n])),
        }
        for n in widths
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    metadata, runs, errors = load(args.input)
    config = metadata["arguments"]
    widths = sorted(config["widths"])
    keys = sorted(config["keys"])
    deltas = sorted(float(value) for value in config["deltas"])
    horizon = float(config["horizon"])
    expected = len(widths) * len(keys) * len(deltas)

    missing = [
        [n, key, delta]
        for n in widths
        for key in keys
        for delta in deltas
        if (n, key, delta) not in runs
    ]
    nonfinite = [
        {
            "n": n,
            "key": key,
            "delta": delta,
            "failure_time": run.get("failure_time"),
            "last_finite_time": run.get("last_finite_time"),
        }
        for (n, key, delta), run in sorted(runs.items())
        if not run["finite"]
    ]

    fine_endpoint_failures = []
    comparison_horizon_failures = []
    for n in widths:
        for key in keys:
            fine = runs.get((n, key, FINE_DELTA))
            comparison = runs.get((n, key, COMPARISON_DELTA))
            if fine is None or not finite_through_registered_endpoint(fine, horizon):
                fine_endpoint_failures.append([n, key])
            if (
                comparison is None
                or not comparison["records"]
                or comparison["records"][-1]["t"] < horizon - 1e-9
            ):
                comparison_horizon_failures.append([n, key])

    step_audit = {}
    all_loss_increases = []
    all_defects = []
    validity = (
        not errors
        and not missing
        and not fine_endpoint_failures
        and not comparison_horizon_failures
    )
    for n in widths:
        curve_errors = []
        hitting_differences = defaultdict(list)
        for key in keys:
            coarse = runs[(n, key, COMPARISON_DELTA)]
            fine = runs[(n, key, FINE_DELTA)]
            curve_error = paired_curve_error(coarse, fine, horizon)
            if curve_error is not None:
                curve_errors.append(curve_error)
            for q in SCIENCE_THRESHOLDS:
                tc = coarse["hitting_times"][qkey(q)]
                tf = fine["hitting_times"][qkey(q)]
                if tc is not None and tf is not None:
                    hitting_differences[qkey(q)].append(abs(tc - tf))
            for record in fine["records"][:-1]:
                if record["loss_increment"] is not None:
                    all_loss_increases.append(record["loss_increment"])
                if record["flow_defect"] is not None:
                    all_defects.append(record["flow_defect"])
        complete_curves = len(curve_errors) == len(keys)
        p95_curve = percentile(curve_errors, 0.95) if curve_errors else None
        hit_medians = {
            qkey(q): (
                median(hitting_differences[qkey(q)])
                if len(hitting_differences[qkey(q)]) == len(keys)
                else None
            )
            for q in SCIENCE_THRESHOLDS
        }
        step_audit[str(n)] = {
            "complete_curve_pairs": complete_curves,
            "curve_error_p95": p95_curve,
            "curve_error_max": float(max(curve_errors)) if curve_errors else None,
            "hitting_time_abs_diff_median": hit_medians,
        }
        validity &= complete_curves and p95_curve is not None and p95_curve <= 0.01
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
            central = slope(np.asarray(widths), np.asarray(values))
            interval = bootstrap_slope(grouped, 2026082500 + q_index)
            hitting_summary[qkey(q)] = {
                "width_medians": medians,
                "endpoint_ratio_2048_over_128": values[-1] / values[0],
                "loglog_slope": central,
                "bootstrap_95": interval,
            }
        else:
            hitting_summary[qkey(q)] = {
                "complete": False,
                "counts": {str(n): len(grouped[n]) for n in widths},
            }

    curve_medians = {}
    for n in widths:
        curve_medians[str(n)] = {}
        for t in CURVE_GRID:
            records = [record_at(runs[(n, key, FINE_DELTA)], t) for key in keys]
            curve_medians[str(n)][str(t)] = (
                median([record["f"] for record in records])
                if all(record is not None for record in records)
                else None
            )
    high_width_differences = []
    for t in CURVE_GRID:
        f1024 = curve_medians.get("1024", {}).get(str(t))
        f2048 = curve_medians.get("2048", {}).get(str(t))
        if f1024 is None or f2048 is None:
            high_width_differences = []
            break
        high_width_differences.append(abs(f1024 - f2048))
    curve_difference_1024_2048 = (
        float(max(high_width_differences)) if high_width_differences else None
    )

    k0_grouped = defaultdict(list)
    kpre_grouped = defaultdict(list)
    condensation0_grouped = defaultdict(list)
    condensation_pre_grouped = defaultdict(list)
    maxima0 = {name: defaultdict(list) for name in ("a", "x", "z")}
    maxima_pre = {name: defaultdict(list) for name in ("a", "x", "z")}
    for n in widths:
        for key in keys:
            records = runs[(n, key, FINE_DELTA)]["records"]
            k0_grouped[n].append(records[0]["K"])
            condensation0_grouped[n].append(records[0]["readout_condensation"])
            for name in maxima0:
                maxima0[name][n].append(records[0]["max_abs"][name])
            before = [record for record in records if record["f"] < 0.75]
            kpre_grouped[n].append(max(record["K"] for record in before))
            condensation_pre_grouped[n].append(
                max(record["readout_condensation"] for record in before)
            )
            for name in maxima_pre:
                maxima_pre[name][n].append(
                    max(record["max_abs"][name] for record in before)
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

    tail_diagnostics = {
        "readout_condensation_initial": descriptive_width_summary(
            condensation0_grouped, widths
        ),
        "readout_condensation_max_pre_f_075": descriptive_width_summary(
            condensation_pre_grouped, widths
        ),
        "max_abs_initial": {
            name: descriptive_width_summary(grouped, widths)
            for name, grouped in maxima0.items()
        },
        "max_abs_pre_f_075": {
            name: descriptive_width_summary(grouped, widths)
            for name, grouped in maxima_pre.items()
        },
    }

    diagonal_delta = {
        128: 0.02,
        256: 0.01,
        512: 0.005,
        1024: 0.0025,
        2048: 0.00125,
    }
    diagonal_errors = {}
    for n in widths:
        errors_n = []
        finite_n = []
        for key in keys:
            diagonal = runs[(n, key, diagonal_delta[n])]
            fine = runs[(n, key, FINE_DELTA)]
            error = paired_curve_error(diagonal, fine, horizon)
            if error is not None:
                errors_n.append(error)
            finite_n.append(diagonal["finite"])
        diagonal_errors[str(n)] = {
            "delta": diagonal_delta[n],
            "finite_count": int(sum(finite_n)),
            "complete_comparisons": len(errors_n),
            "median_max_predictor_error_vs_fine": (
                median(errors_n) if errors_n else None
            ),
            "max_predictor_error_vs_fine": (
                float(max(errors_n)) if errors_n else None
            ),
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
        and curve_difference_1024_2048 is not None
        and curve_difference_1024_2048 <= 0.05
        and k_regular
    )
    last_three_f001 = [curve_medians[str(n)][str(0.01)] for n in widths[-3:]]
    early_boundary = all(value is not None for value in last_three_f001)
    if early_boundary:
        early_boundary = (
            last_three_f001[0] < last_three_f001[1] < last_three_f001[2]
            and last_three_f001[-1] > 0.75
        )
    boundary = validity and (all(boundary_conditions) or early_boundary)
    if regular:
        verdict = "evidence_against_polynomially_visible_instantaneous_jump"
    elif boundary:
        verdict = "evidence_for_visible_shrinking_boundary_layer"
    else:
        verdict = "inconclusive"

    result = {
        "input": str(args.input),
        "expected_run_count": expected,
        "observed_run_count": len(runs),
        "errors": errors,
        "missing": missing,
        "nonfinite": nonfinite,
        "validity": {
            "passed": bool(validity),
            "fine_endpoint_failures": fine_endpoint_failures,
            "comparison_horizon_failures": comparison_horizon_failures,
            "step_audit": step_audit,
            "max_fine_step_loss_increase": max_loss_increase,
            "median_fine_step_flow_defect": median_defect,
        },
        "hitting_times": hitting_summary,
        "fine_predictor_width_medians": curve_medians,
        "max_curve_difference_1024_2048": curve_difference_1024_2048,
        "kernel": k_summary,
        "tail_diagnostics": tail_diagnostics,
        "diagonal_sequence": diagonal_errors,
        "verdict": verdict,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(
        json.dumps(
            {
                "validity": result["validity"]["passed"],
                "verdict": verdict,
                "max_curve_difference_1024_2048": curve_difference_1024_2048,
                "hitting_times": {
                    q: {
                        "ratio": value.get("endpoint_ratio_2048_over_128"),
                        "slope": value.get("loglog_slope"),
                        "ci": value.get("bootstrap_95"),
                    }
                    for q, value in hitting_summary.items()
                },
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
