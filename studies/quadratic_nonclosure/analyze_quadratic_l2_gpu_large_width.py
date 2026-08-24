"""Mechanical analysis for the frozen quadratic L=2 GPU width ladder."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

import numpy as np


FROZEN_WIDTHS = (2048, 4096, 8192, 16384, 32768)
FROZEN_KEYS = (9201, 9202, 9203, 9204, 9205, 9206)
COARSE_DELTA = 0.000625
FINE_DELTA = 0.0003125
FROZEN_HORIZON = 0.25
SCIENCE_THRESHOLDS = (0.25, 0.50, 0.75, 0.90)
SHRINK_THRESHOLDS = (0.25, 0.50, 0.75)
EARLY_GRID = (0.0, 0.0025, 0.005, 0.01, 0.02, 0.04, 0.06, 0.08, 0.10)


def qkey(q: float) -> str:
    return str(float(q))


def median(values) -> float:
    return float(np.median(np.asarray(values, dtype=float)))


def percentile(values, q: float) -> float:
    return float(np.quantile(np.asarray(values, dtype=float), q))


def loglog_slope(widths, values) -> float:
    return float(np.polyfit(np.log(widths), np.log(values), 1)[0])


def bootstrap_slope(grouped, seed: int, reps: int = 5000):
    widths = np.asarray(sorted(grouped), dtype=float)
    rng = np.random.default_rng(seed)
    draws = np.empty(reps, dtype=float)
    for index in range(reps):
        sampled_medians = []
        for n in widths.astype(int):
            values = np.asarray(grouped[n], dtype=float)
            sample = rng.choice(values, size=values.size, replace=True)
            sampled_medians.append(np.median(sample))
        draws[index] = loglog_slope(widths, sampled_medians)
    return [float(value) for value in np.quantile(draws, (0.025, 0.975))]


def load(path: Path):
    metadata = None
    runs = {}
    exceptional = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            if row["kind"] == "metadata":
                metadata = row
            elif row["kind"] == "bundle":
                for run in row["runs"]:
                    runs[(row["n"], row["key"], float(run["delta"]))] = run
            else:
                exceptional.append(row)
    if metadata is None:
        raise ValueError("missing metadata")
    return metadata, runs, exceptional


def record_at(run, t: float):
    index = int(round(t / run["delta"]))
    if index >= len(run["records"]):
        return None
    record = run["records"][index]
    if abs(record["t"] - t) > 1e-10:
        raise ValueError((record["t"], t, run["delta"]))
    return record


def paired_curve_error(coarse, fine):
    if not coarse["records"] or not fine["records"]:
        return None
    common_end = min(coarse["records"][-1]["t"], fine["records"][-1]["t"])
    errors = []
    for record in coarse["records"]:
        if record["t"] > common_end + 1e-12:
            break
        fine_record = record_at(fine, record["t"])
        if fine_record is None:
            return None
        errors.append(abs(record["f"] - fine_record["f"]))
    return float(max(errors)) if errors else None


def width_descriptives(grouped):
    return {
        str(n): {
            "median": median(grouped[n]),
            "min": float(min(grouped[n])),
            "max": float(max(grouped[n])),
        }
        for n in FROZEN_WIDTHS
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    metadata, runs, exceptional = load(args.input)
    config = metadata["arguments"]
    frozen_metadata = (
        tuple(config["widths"]) == FROZEN_WIDTHS
        and tuple(config["keys"]) == FROZEN_KEYS
        and tuple(float(value) for value in config["deltas"])
        == (COARSE_DELTA, FINE_DELTA)
        and float(config["horizon"]) == FROZEN_HORIZON
    )
    missing = [
        [n, key, delta]
        for n in FROZEN_WIDTHS
        for key in FROZEN_KEYS
        for delta in (COARSE_DELTA, FINE_DELTA)
        if (n, key, delta) not in runs
    ]

    numerical_failures = []
    for n in FROZEN_WIDTHS:
        for key in FROZEN_KEYS:
            for delta in (COARSE_DELTA, FINE_DELTA):
                run = runs.get((n, key, delta))
                if run is None:
                    continue
                reasons = []
                if not run["finite"]:
                    reasons.append("nonfinite")
                if run["hitting_times"].get(qkey(0.95)) is None:
                    reasons.append("did_not_reach_0.95")
                if not run["memory_cap_pass"]:
                    reasons.append("memory_cap")
                if reasons:
                    numerical_failures.append(
                        {"n": n, "key": key, "delta": delta, "reasons": reasons}
                    )

    validity = frozen_metadata and not exceptional and not missing and not numerical_failures
    step_audit = {}
    all_fine_loss_increases = []
    all_fine_flow_defects = []
    initial_pair_max_difference = 0.0
    for n in FROZEN_WIDTHS:
        curve_errors = []
        hit_differences = defaultdict(list)
        for key in FROZEN_KEYS:
            coarse = runs[(n, key, COARSE_DELTA)]
            fine = runs[(n, key, FINE_DELTA)]
            error = paired_curve_error(coarse, fine)
            if error is not None:
                curve_errors.append(error)
            initial_pair_max_difference = max(
                initial_pair_max_difference,
                abs(coarse["records"][0]["f"] - fine["records"][0]["f"]),
                abs(coarse["records"][0]["K"] - fine["records"][0]["K"]),
            )
            for q in SCIENCE_THRESHOLDS:
                tc = coarse["hitting_times"][qkey(q)]
                tf = fine["hitting_times"][qkey(q)]
                if tc is not None and tf is not None:
                    hit_differences[qkey(q)].append(abs(tc - tf))
            for record in fine["records"][:-1]:
                if record["loss_increment"] is not None:
                    all_fine_loss_increases.append(record["loss_increment"])
                if record["flow_defect"] is not None:
                    all_fine_flow_defects.append(record["flow_defect"])
        complete_curve_pairs = len(curve_errors) == len(FROZEN_KEYS)
        p95_curve_error = percentile(curve_errors, 0.95) if curve_errors else None
        hit_medians = {
            qkey(q): (
                median(hit_differences[qkey(q)])
                if len(hit_differences[qkey(q)]) == len(FROZEN_KEYS)
                else None
            )
            for q in SCIENCE_THRESHOLDS
        }
        step_audit[str(n)] = {
            "complete_curve_pairs": complete_curve_pairs,
            "curve_error_p95": p95_curve_error,
            "curve_error_max": float(max(curve_errors)) if curve_errors else None,
            "hitting_time_abs_diff_median": hit_medians,
        }
        validity &= (
            complete_curve_pairs
            and p95_curve_error is not None
            and p95_curve_error <= 0.01
            and all(
                value is not None and value <= 0.001
                for value in hit_medians.values()
            )
        )

    max_loss_increase = float(
        max(all_fine_loss_increases, default=float("inf"))
    )
    median_flow_defect = (
        median(all_fine_flow_defects) if all_fine_flow_defects else float("inf")
    )
    validity &= initial_pair_max_difference <= 1e-12
    validity &= max_loss_increase <= 1e-5 and median_flow_defect < 0.01

    hitting_summary = {}
    for q_index, q in enumerate(SCIENCE_THRESHOLDS):
        grouped = defaultdict(list)
        for n in FROZEN_WIDTHS:
            for key in FROZEN_KEYS:
                value = runs[(n, key, FINE_DELTA)]["hitting_times"][qkey(q)]
                if value is not None:
                    grouped[n].append(value)
        complete = all(len(grouped[n]) == len(FROZEN_KEYS) for n in FROZEN_WIDTHS)
        if complete and all(value > 0 for n in FROZEN_WIDTHS for value in grouped[n]):
            medians = {str(n): median(grouped[n]) for n in FROZEN_WIDTHS}
            median_values = [medians[str(n)] for n in FROZEN_WIDTHS]
            last_four = [medians[str(n)] for n in FROZEN_WIDTHS[1:]]
            hitting_summary[qkey(q)] = {
                "width_medians": medians,
                "endpoint_ratio_32768_over_2048": median_values[-1]
                / median_values[0],
                "loglog_slope": loglog_slope(FROZEN_WIDTHS, median_values),
                "bootstrap_95": bootstrap_slope(
                    grouped, 2026082700 + q_index, reps=5000
                ),
                "strictly_decreasing_last_four": all(
                    left > right for left, right in zip(last_four, last_four[1:])
                ),
            }
        else:
            hitting_summary[qkey(q)] = {
                "complete": False,
                "counts": {str(n): len(grouped[n]) for n in FROZEN_WIDTHS},
            }

    curve_medians = {}
    for n in FROZEN_WIDTHS:
        curve_medians[str(n)] = {}
        for t in EARLY_GRID:
            records = [record_at(runs[(n, key, FINE_DELTA)], t) for key in FROZEN_KEYS]
            curve_medians[str(n)][str(t)] = (
                median([record["f"] for record in records])
                if all(record is not None for record in records)
                else None
            )

    k0_grouped = defaultdict(list)
    kpre_grouped = defaultdict(list)
    condensation0_grouped = defaultdict(list)
    condensation_pre_grouped = defaultdict(list)
    maxima0 = {name: defaultdict(list) for name in ("a", "x", "z")}
    maxima_pre = {name: defaultdict(list) for name in ("a", "x", "z")}
    for n in FROZEN_WIDTHS:
        for key in FROZEN_KEYS:
            records = runs[(n, key, FINE_DELTA)]["records"]
            before = [record for record in records if record["f"] < 0.75]
            k0_grouped[n].append(records[0]["K"])
            kpre_grouped[n].append(max(record["K"] for record in before))
            condensation0_grouped[n].append(records[0]["readout_condensation"])
            condensation_pre_grouped[n].append(
                max(record["readout_condensation"] for record in before)
            )
            for name in maxima0:
                maxima0[name][n].append(records[0]["max_abs"][name])
                maxima_pre[name][n].append(
                    max(record["max_abs"][name] for record in before)
                )

    kernel_summary = {}
    for label, grouped in (("K0", k0_grouped), ("K_pre_f_075_max", kpre_grouped)):
        medians = {str(n): median(grouped[n]) for n in FROZEN_WIDTHS}
        values = [medians[str(n)] for n in FROZEN_WIDTHS]
        ratio = values[-1] / values[0]
        kernel_summary[label] = {
            "width_medians": medians,
            "symmetric_endpoint_factor": max(ratio, 1.0 / ratio),
            "loglog_slope": loglog_slope(FROZEN_WIDTHS, values),
        }

    tail_summary = {
        "readout_condensation_initial": width_descriptives(condensation0_grouped),
        "readout_condensation_max_pre_f_075": width_descriptives(
            condensation_pre_grouped
        ),
        "max_abs_initial": {
            name: width_descriptives(grouped) for name, grouped in maxima0.items()
        },
        "max_abs_pre_f_075": {
            name: width_descriptives(grouped) for name, grouped in maxima_pre.items()
        },
    }

    stable_conditions = []
    shrink_conditions = []
    for q in SCIENCE_THRESHOLDS:
        summary = hitting_summary[qkey(q)]
        if "width_medians" not in summary:
            stable_conditions.append(False)
            if q in SHRINK_THRESHOLDS:
                shrink_conditions.append(False)
            continue
        stable_conditions.append(
            0.80 <= summary["endpoint_ratio_32768_over_2048"] <= 1.20
            and -0.08 <= summary["loglog_slope"] <= 0.08
            and summary["bootstrap_95"][0] > -0.15
            and summary["bootstrap_95"][1] < 0.15
        )
        if q in SHRINK_THRESHOLDS:
            shrink_conditions.append(
                summary["endpoint_ratio_32768_over_2048"] < 0.70
                and summary["strictly_decreasing_last_four"]
                and summary["loglog_slope"] < -0.10
                and summary["bootstrap_95"][1] < -0.03
            )
    kernel_stable = all(
        item["symmetric_endpoint_factor"] < 1.5
        and item["loglog_slope"] < 0.10
        for item in kernel_summary.values()
    )
    early_values = [
        curve_medians[str(n)][str(0.005)] for n in FROZEN_WIDTHS[-3:]
    ]
    early_jump = all(value is not None for value in early_values)
    if early_jump:
        early_jump = (
            early_values[0] < early_values[1] < early_values[2]
            and early_values[2] > 0.75
        )
    stable = validity and all(stable_conditions) and kernel_stable
    shrinking = validity and (all(shrink_conditions) or early_jump)
    if shrinking:
        verdict = "evidence_for_visible_shrinking_boundary_layer"
    elif stable:
        verdict = "evidence_for_resolved_positive_time_scale"
    else:
        verdict = "inconclusive"

    peak_memory = {
        str(n): max(
            runs[(n, key, delta)]["peak_allocated_gib"]
            for key in FROZEN_KEYS
            for delta in (COARSE_DELTA, FINE_DELTA)
        )
        for n in FROZEN_WIDTHS
    }
    result = {
        "input": str(args.input),
        "metadata_frozen_grid_pass": bool(frozen_metadata),
        "exceptional_records": exceptional,
        "missing": missing,
        "numerical_failures": numerical_failures,
        "validity": {
            "passed": bool(validity),
            "initial_pair_max_difference": initial_pair_max_difference,
            "step_audit": step_audit,
            "max_fine_loss_increase": max_loss_increase,
            "median_fine_flow_defect": median_flow_defect,
            "peak_allocated_gib_by_width": peak_memory,
        },
        "hitting_times": hitting_summary,
        "fine_early_curve_medians": curve_medians,
        "kernel": kernel_summary,
        "tail_diagnostics": tail_summary,
        "criteria": {
            "stable_threshold_conditions": stable_conditions,
            "kernel_stable": kernel_stable,
            "shrink_threshold_conditions": shrink_conditions,
            "early_jump": bool(early_jump),
        },
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
                "hitting_times": hitting_summary,
                "kernel": kernel_summary,
                "step_audit": step_audit,
                "early_f_0005": {
                    str(n): curve_medians[str(n)][str(0.005)]
                    for n in FROZEN_WIDTHS
                },
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
