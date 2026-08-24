"""Mechanical evaluator for the preregistered joint-limit side experiment."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

import numpy as np


SCIENCE_THRESHOLDS = (0.25, 0.50, 0.75, 0.90)
CURVE_GRID = (0.0, 0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.0, 2.0)


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
        raise IndexError((delta, t, index, len(run["records"])))
    record = run["records"][index]
    if abs(record["t"] - t) > 1e-9:
        raise ValueError((record["t"], t))
    return record


def paired_curve_error(coarse, fine):
    errors = []
    for record in coarse["records"]:
        errors.append(abs(record["f"] - record_at(fine, record["t"])["f"]))
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    metadata, runs, errors = load(args.input)
    config = metadata["arguments"]
    widths = sorted(config["widths"])
    keys = sorted(config["keys"])
    deltas = sorted(float(x) for x in config["deltas"])
    fine_delta = 0.0025
    coarse_delta = 0.005
    expected = len(widths) * len(keys) * len(deltas)

    missing = [
        [n, key, delta]
        for n in widths
        for key in keys
        for delta in deltas
        if (n, key, delta) not in runs
    ]
    nonfinite = [
        [n, key, delta]
        for (n, key, delta), run in runs.items()
        if not run["finite"]
    ]

    step_audit = {}
    all_loss_increases = []
    all_defects = []
    validity = not errors and not missing and not nonfinite
    for n in widths:
        curve_errors = []
        hitting_differences = defaultdict(list)
        for key in keys:
            coarse = runs[(n, key, coarse_delta)]
            fine = runs[(n, key, fine_delta)]
            curve_errors.append(paired_curve_error(coarse, fine))
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
        p95_curve = percentile(curve_errors, 0.95)
        hit_medians = {
            q: median(values) if values else None
            for q, values in hitting_differences.items()
        }
        step_audit[str(n)] = {
            "curve_error_p95": p95_curve,
            "curve_error_max": float(max(curve_errors)),
            "hitting_time_abs_diff_median": hit_medians,
        }
        validity &= p95_curve <= 0.01
        validity &= all(
            value is not None and value <= 0.01 for value in hit_medians.values()
        ) and len(hit_medians) == len(SCIENCE_THRESHOLDS)

    max_loss_increase = float(max(all_loss_increases, default=float("inf")))
    median_defect = median(all_defects) if all_defects else float("inf")
    validity &= max_loss_increase <= 1e-5 and median_defect <= 0.01

    hitting_summary = {}
    hitting_by_q = {}
    for q_index, q in enumerate(SCIENCE_THRESHOLDS):
        grouped = defaultdict(list)
        for n in widths:
            for key in keys:
                value = runs[(n, key, fine_delta)]["hitting_times"][qkey(q)]
                if value is not None:
                    grouped[n].append(value)
        hitting_by_q[qkey(q)] = grouped
        complete = all(len(grouped[n]) == len(keys) for n in widths)
        if complete:
            medians = {str(n): median(grouped[n]) for n in widths}
            values = [medians[str(n)] for n in widths]
            central = slope(np.asarray(widths), np.asarray(values))
            interval = bootstrap_slope(grouped, 2026082400 + q_index)
            endpoint_ratio = values[-1] / values[0]
            hitting_summary[qkey(q)] = {
                "width_medians": medians,
                "endpoint_ratio_2048_over_128": endpoint_ratio,
                "loglog_slope": central,
                "bootstrap_95": interval,
            }
        else:
            hitting_summary[qkey(q)] = {"complete": False}

    curve_medians = {}
    for n in widths:
        curve_medians[str(n)] = {
            str(t): median(
                [record_at(runs[(n, key, fine_delta)], t)["f"] for key in keys]
            )
            for t in CURVE_GRID
        }
    curve_difference_1024_2048 = max(
        abs(curve_medians["1024"][str(t)] - curve_medians["2048"][str(t)])
        for t in CURVE_GRID
    )

    k0_grouped = defaultdict(list)
    kpre_grouped = defaultdict(list)
    for n in widths:
        for key in keys:
            records = runs[(n, key, fine_delta)]["records"]
            k0_grouped[n].append(records[0]["K"])
            before = [record["K"] for record in records if record["f"] < 0.75]
            kpre_grouped[n].append(max(before))
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

    diagonal_delta = {128: 0.04, 256: 0.02, 512: 0.01, 1024: 0.005, 2048: 0.0025}
    diagonal_errors = {}
    for n in widths:
        errors_n = []
        for key in keys:
            diagonal = runs[(n, key, diagonal_delta[n])]
            fine = runs[(n, key, fine_delta)]
            errors_n.append(paired_curve_error(diagonal, fine))
        diagonal_errors[str(n)] = {
            "delta": diagonal_delta[n],
            "median_max_predictor_error_vs_fine": median(errors_n),
            "max_predictor_error_vs_fine": float(max(errors_n)),
        }

    regular_conditions = []
    jump_conditions = []
    for q in SCIENCE_THRESHOLDS:
        summary = hitting_summary[qkey(q)]
        if "width_medians" not in summary:
            regular_conditions.append(False)
            if q <= 0.75:
                jump_conditions.append(False)
            continue
        regular_conditions.append(
            0.75 <= summary["endpoint_ratio_2048_over_128"] <= 1.25
            and -0.10 <= summary["loglog_slope"] <= 0.10
            and summary["bootstrap_95"][0] > -0.20
            and summary["bootstrap_95"][1] < 0.20
        )
        if q <= 0.75:
            jump_conditions.append(
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
    last_three_f002 = [curve_medians[str(n)]["0.02"] for n in widths[-3:]]
    early_jump = last_three_f002[0] < last_three_f002[1] < last_three_f002[2]
    early_jump &= last_three_f002[-1] > 0.75
    jump = validity and (all(jump_conditions) or early_jump)
    if regular:
        verdict = "evidence_against_polynomially_visible_instantaneous_jump"
    elif jump:
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
            "step_audit": step_audit,
            "max_fine_step_loss_increase": max_loss_increase,
            "median_fine_step_flow_defect": median_defect,
        },
        "hitting_times": hitting_summary,
        "fine_predictor_width_medians": curve_medians,
        "max_curve_difference_1024_2048": float(curve_difference_1024_2048),
        "kernel": k_summary,
        "diagonal_sequence": diagonal_errors,
        "verdict": verdict,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps({
        "validity": result["validity"]["passed"],
        "verdict": verdict,
        "max_curve_difference_1024_2048": curve_difference_1024_2048,
        "hitting_times": {
            q: {
                "ratio": v.get("endpoint_ratio_2048_over_128"),
                "slope": v.get("loglog_slope"),
                "ci": v.get("bootstrap_95"),
            }
            for q, v in hitting_summary.items()
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
