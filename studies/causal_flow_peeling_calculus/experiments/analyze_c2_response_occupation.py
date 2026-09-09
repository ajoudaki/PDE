#!/usr/bin/env python3
"""Analyze the locked C2 response-weighted occupation experiment."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
import statistics
import sys
from collections import defaultdict
from pathlib import Path


WIDTHS = (128, 256, 512, 1024)
TIMES = (0.0, 0.25, 0.5)
LAMBDAS = (0.05, 0.10, 0.20)
FIELDS = ("r2", "b2")
BOOTSTRAPS = 5000
BOOTSTRAP_SEED = 20260825


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def as_bool(value: str) -> bool:
    return value.lower() == "true"


def quantile(values: list[float], probability: float) -> float:
    ordered = sorted(values)
    if not ordered:
        return math.nan
    location = probability * (len(ordered) - 1)
    lower = int(math.floor(location))
    upper = int(math.ceil(location))
    if lower == upper:
        return ordered[lower]
    fraction = location - lower
    return ordered[lower] * (1.0 - fraction) + ordered[upper] * fraction


def slope(xs: list[float], ys: list[float]) -> float:
    xbar = statistics.fmean(xs)
    ybar = statistics.fmean(ys)
    denominator = sum((x - xbar) ** 2 for x in xs)
    return sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys)) / denominator


def summarize(values: list[float]) -> dict[str, float]:
    if not values:
        return {
            "mean": math.nan,
            "median": math.nan,
            "q10": math.nan,
            "q90": math.nan,
            "minimum": math.nan,
            "maximum": math.nan,
            "count": 0,
        }
    return {
        "mean": statistics.fmean(values),
        "median": statistics.median(values),
        "q10": quantile(values, 0.10),
        "q90": quantile(values, 0.90),
        "minimum": min(values),
        "maximum": max(values),
        "count": len(values),
    }


def key_for(row: dict[str, str]) -> tuple[str, float, float]:
    return row["field"], float(row["time"]), float(row["lambda"])


def collect_primary(primary_dirs: list[Path]) -> tuple[list[dict], list[dict], list[dict]]:
    metrics: list[dict] = []
    trajectories: list[dict] = []
    metadata: list[dict] = []
    for directory in primary_dirs:
        metrics.extend(read_csv(directory / "raw_metrics.csv"))
        trajectories.extend(read_csv(directory / "raw_trajectories.csv"))
        metadata.append(json.loads((directory / "metadata.json").read_text()))
    return metrics, trajectories, metadata


def indexed_data(metrics: list[dict]) -> dict[tuple, list[tuple[int, float, float]]]:
    grouped: dict[tuple, list[tuple[int, float, float]]] = defaultdict(list)
    for row in metrics:
        field, checkpoint, lam = key_for(row)
        if field not in FIELDS or lam not in LAMBDAS:
            continue
        width = int(row["width"])
        grouped[(field, checkpoint, lam, width)].append(
            (int(row["replicate"]), float(row["M"]), float(row["M_shuffle_mean"]))
        )
    for key in grouped:
        grouped[key].sort()
    return grouped


def validate_primary_shape(grouped: dict[tuple, list[tuple[int, float, float]]]) -> list[str]:
    errors = []
    for field in FIELDS:
        for checkpoint in TIMES:
            for lam in LAMBDAS:
                for width in WIDTHS:
                    rows = grouped.get((field, checkpoint, lam, width), [])
                    replicas = [item[0] for item in rows]
                    if replicas != list(range(48)):
                        errors.append(
                            f"missing/duplicate primary rows for {(field, checkpoint, lam, width)}: {replicas}"
                        )
    return errors


def estimates_from_values(
    values: dict[int, tuple[list[float], list[float]]]
) -> dict:
    log_widths = [math.log(width) for width in WIDTHS]
    mean_m = {width: statistics.fmean(values[width][0]) for width in WIDTHS}
    mean_shuffled = {
        width: statistics.fmean(values[width][1]) for width in WIDTHS
    }
    beta = slope(log_widths, [math.log(mean_m[width]) for width in WIDTHS])
    alignment = {
        width: math.log(mean_m[width] / mean_shuffled[width]) for width in WIDTHS
    }
    alpha = slope(log_widths, [alignment[width] for width in WIDTHS])
    return {
        "beta": beta,
        "alpha": alpha,
        "a1024": alignment[1024],
        "mean_M": mean_m,
        "mean_M_shuffle": mean_shuffled,
        "alignment": alignment,
    }


def point_estimates(grouped: dict) -> dict[tuple, dict]:
    result = {}
    for field in FIELDS:
        for checkpoint in TIMES:
            for lam in LAMBDAS:
                values = {}
                for width in WIDTHS:
                    rows = grouped[(field, checkpoint, lam, width)]
                    values[width] = (
                        [item[1] for item in rows],
                        [item[2] for item in rows],
                    )
                result[(field, checkpoint, lam)] = estimates_from_values(values)
    return result


def half_estimates(grouped: dict, start: int, stop: int) -> dict[tuple, dict]:
    result = {}
    for field in FIELDS:
        for checkpoint in TIMES:
            for lam in LAMBDAS:
                values = {}
                for width in WIDTHS:
                    rows = [
                        item
                        for item in grouped[(field, checkpoint, lam, width)]
                        if start <= item[0] < stop
                    ]
                    values[width] = (
                        [item[1] for item in rows],
                        [item[2] for item in rows],
                    )
                result[(field, checkpoint, lam)] = estimates_from_values(values)
    return result


def bootstrap_intervals(grouped: dict, points: dict) -> tuple[dict, dict]:
    keys = list(points)
    rng = random.Random(BOOTSTRAP_SEED)
    beta_samples = {key: [] for key in keys}
    alpha_samples = {key: [] for key in keys}
    a_samples = {key: [] for key in keys}
    rows_by_key = {
        (field, checkpoint, lam, width): grouped[(field, checkpoint, lam, width)]
        for field, checkpoint, lam in keys
        for width in WIDTHS
    }
    for _ in range(BOOTSTRAPS):
        indices = {
            width: [rng.randrange(48) for _ in range(48)] for width in WIDTHS
        }
        for key in keys:
            field, checkpoint, lam = key
            values = {}
            for width in WIDTHS:
                rows = rows_by_key[(field, checkpoint, lam, width)]
                selected = [rows[index] for index in indices[width]]
                values[width] = (
                    [item[1] for item in selected],
                    [item[2] for item in selected],
                )
            estimate = estimates_from_values(values)
            beta_samples[key].append(estimate["beta"])
            alpha_samples[key].append(estimate["alpha"])
            a_samples[key].append(estimate["a1024"])

    max_beta_deviation = [
        max(beta_samples[key][index] - points[key]["beta"] for key in keys)
        for index in range(BOOTSTRAPS)
    ]
    max_alpha_deviation = [
        max(alpha_samples[key][index] - points[key]["alpha"] for key in keys)
        for index in range(BOOTSTRAPS)
    ]
    max_a_up_deviation = [
        max(a_samples[key][index] - points[key]["a1024"] for key in keys)
        for index in range(BOOTSTRAPS)
    ]
    max_a_down_deviation = [
        max(points[key]["a1024"] - a_samples[key][index] for key in keys)
        for index in range(BOOTSTRAPS)
    ]
    q_beta = quantile(max_beta_deviation, 0.95)
    q_alpha = quantile(max_alpha_deviation, 0.95)
    q_a_up = quantile(max_a_up_deviation, 0.95)
    q_a_down = quantile(max_a_down_deviation, 0.95)
    intervals = {}
    for key in keys:
        intervals[key] = {
            "beta_cell_lower_95": quantile(beta_samples[key], 0.05),
            "beta_cell_upper_95": quantile(beta_samples[key], 0.95),
            "beta_familywise_upper_95": points[key]["beta"] + q_beta,
            "alpha_cell_lower_95": quantile(alpha_samples[key], 0.05),
            "alpha_cell_upper_95": quantile(alpha_samples[key], 0.95),
            "alpha_familywise_upper_95": points[key]["alpha"] + q_alpha,
            "a1024_cell_lower_95": quantile(a_samples[key], 0.05),
            "a1024_cell_upper_95": quantile(a_samples[key], 0.95),
            "a1024_familywise_lower_95": points[key]["a1024"] - q_a_down,
            "a1024_familywise_upper_95": points[key]["a1024"] + q_a_up,
        }
    diagnostics = {
        "bootstrap_replicates": BOOTSTRAPS,
        "bootstrap_seed": BOOTSTRAP_SEED,
        "familywise_beta_upper_deviation": q_beta,
        "familywise_alpha_upper_deviation": q_alpha,
        "familywise_a_upper_deviation": q_a_up,
        "familywise_a_lower_deviation": q_a_down,
    }
    return intervals, diagnostics


def primary_validity(
    trajectories: list[dict], metadata: list[dict], shape_errors: list[str]
) -> dict:
    by_width: dict[int, list[dict]] = defaultdict(list)
    for row in trajectories:
        by_width[int(row["width"])].append(row)
    width_summary = {}
    failures = list(shape_errors)
    for width in WIDTHS:
        rows = by_width[width]
        unique = {(int(row["replicate"])) for row in rows}
        valid = [
            row
            for row in rows
            if as_bool(row["all_finite"])
            and as_bool(row["below_envelope_gate"])
            and as_bool(row["time0_exact_zero"])
        ]
        width_summary[str(width)] = {
            "rows": len(rows),
            "unique_replicates": len(unique),
            "valid": len(valid),
            "maximum_absolute_entry": max(
                (float(row["maximum_absolute_entry"]) for row in rows), default=math.nan
            ),
            "maximum_time0_z2_error": max(
                (float(row["time0_V_z2_max"]) for row in rows), default=math.nan
            ),
            "maximum_time0_x2_error": max(
                (float(row["time0_V_x2_max"]) for row in rows), default=math.nan
            ),
        }
        if len(rows) != 48 or len(unique) != 48 or len(valid) < 46:
            failures.append(f"width {width} has {len(valid)}/48 valid trajectories")
    script_hashes = {item["script_sha256"] for item in metadata}
    lock_hashes = {item["lock_sha256"] for item in metadata}
    prereg_hashes = {item["preregistration_sha256"] for item in metadata}
    if len(script_hashes) != 1:
        failures.append("primary chunks used different script hashes")
    if len(lock_hashes) != 1 or len(prereg_hashes) != 1:
        failures.append("primary chunks used different preregistration hashes")
    return {
        "pass": not failures,
        "failures": failures,
        "by_width": width_summary,
        "script_hashes": sorted(script_hashes),
        "lock_hashes": sorted(lock_hashes),
        "preregistration_hashes": sorted(prereg_hashes),
    }


def control_validity(control_dir: Path) -> tuple[dict, list[dict]]:
    rows = read_csv(control_dir / "raw_controls.csv")
    failures = []
    expected = 2 * 2 * 8 * 3 * 2 * 4
    if len(rows) != expected:
        failures.append(f"expected {expected} control rows, found {len(rows)}")
    maxima = {}
    for kind in ("mesh", "precision"):
        selected = [row for row in rows if row["kind"] == kind]
        field_max = max(float(row["field_relative_l2"]) for row in selected)
        moment_max = max(float(row["M_relative_difference"]) for row in selected)
        finite = all(as_bool(row["all_finite"]) for row in selected)
        maxima[kind] = {
            "rows": len(selected),
            "maximum_field_relative_l2": field_max,
            "maximum_M_relative_difference": moment_max,
            "all_finite": finite,
        }
        field_gate = 5.0e-4 if kind == "mesh" else 1.0e-3
        moment_gate = 5.0e-3 if kind == "mesh" else 1.0e-2
        if not finite:
            failures.append(f"{kind} control contains nonfinite values")
        if field_max > field_gate:
            failures.append(f"{kind} field discrepancy {field_max} > {field_gate}")
        if moment_max > moment_gate:
            failures.append(f"{kind} moment discrepancy {moment_max} > {moment_gate}")
    return {"pass": not failures, "failures": failures, **maxima}, rows


def fd_validity(fd_dir: Path) -> tuple[dict, list[dict]]:
    rows = read_csv(fd_dir / "raw_finite_difference.csv")
    failures = []
    if len(rows) != 4 * 3 * 4 * 2:
        failures.append(f"expected 96 finite-difference rows, found {len(rows)}")
    indexed = {
        (
            int(row["replicate"]),
            float(row["time"]),
            row["field"],
            float(row["epsilon"]),
        ): row
        for row in rows
    }
    fine_epsilon = 2.0 ** -9
    coarse_epsilon = 2.0 ** -7
    maximum_relative = 0.0
    maximum_error_ratio = 0.0
    comparisons = []
    for replicate in range(4):
        for field in ("r2", "b2", "z2", "x2"):
            fine = indexed[(replicate, 0.5, field, fine_epsilon)]
            coarse = indexed[(replicate, 0.5, field, coarse_epsilon)]
            fine_relative = float(fine["relative_l2_error"])
            ratio = float(fine["absolute_l2_error"]) / max(
                float(coarse["absolute_l2_error"]), 1.0e-12
            )
            maximum_relative = max(maximum_relative, fine_relative)
            maximum_error_ratio = max(maximum_error_ratio, ratio)
            passed = (
                as_bool(fine["all_finite"])
                and fine_relative <= 2.0e-4
                and ratio <= 1.2
            )
            comparisons.append(
                {
                    "replicate": replicate,
                    "field": field,
                    "fine_relative_l2_error": fine_relative,
                    "fine_to_coarse_absolute_error_ratio": ratio,
                    "pass": passed,
                }
            )
            if not passed:
                failures.append(
                    f"FD gate failed for replicate {replicate}, field {field}: rel={fine_relative}, ratio={ratio}"
                )
    return {
        "pass": not failures,
        "failures": failures,
        "maximum_fine_relative_l2_error": maximum_relative,
        "maximum_fine_to_coarse_absolute_error_ratio": maximum_error_ratio,
        "comparisons": comparisons,
    }, rows


def tail_summaries(metrics: list[dict]) -> tuple[list[dict], dict]:
    names = (
        "rESS",
        "max_contribution_share",
        "response_tail5_share",
        "contribution_tail5_share",
        "response_tail1_share",
        "contribution_tail1_share",
        "weight_rESS",
        "max_weight_share",
        "M_rank_aligned",
        "M_shuffle_mean",
    )
    rows_out = []
    lookup = {}
    for field in FIELDS:
        for checkpoint in TIMES:
            for lam in LAMBDAS:
                for width in WIDTHS:
                    selected = [
                        row
                        for row in metrics
                        if row["field"] == field
                        and float(row["time"]) == checkpoint
                        and float(row["lambda"]) == lam
                        and int(row["width"]) == width
                    ]
                    output = {
                        "field": field,
                        "time": checkpoint,
                        "lambda": lam,
                        "width": width,
                    }
                    for name in names:
                        values = [float(row[name]) for row in selected]
                        values = [value for value in values if math.isfinite(value)]
                        stats = summarize(values)
                        for stat, value in stats.items():
                            output[f"{name}_{stat}"] = value
                    rank_ratios = [
                        float(row["M_rank_aligned"]) / float(row["M_shuffle_mean"])
                        for row in selected
                        if float(row["M_shuffle_mean"]) > 0.0
                    ]
                    output["rank_to_shuffle_ratio_median"] = statistics.median(rank_ratios)
                    rows_out.append(output)
                    lookup[(field, checkpoint, lam, width)] = output
    return rows_out, lookup


def tail_pass_and_fail(metrics: list[dict], tail_lookup: dict) -> tuple[bool, list[str]]:
    pass_ok = True
    fail_reasons = []
    for field in FIELDS:
        for checkpoint in TIMES:
            locked = tail_lookup[(field, checkpoint, 0.20, 1024)]
            if locked["rESS_median"] < 0.05 or locked["max_contribution_share_median"] > 0.10:
                pass_ok = False

            full_high = locked["max_contribution_share_median"]
            rare_half_failure = True
            for start, stop in ((0, 24), (24, 48)):
                medians = {}
                for width in (512, 1024):
                    values = [
                        float(row["max_contribution_share"])
                        for row in metrics
                        if row["field"] == field
                        and float(row["time"]) == checkpoint
                        and float(row["lambda"]) == 0.20
                        and int(row["width"]) == width
                        and start <= int(row["replicate"]) < stop
                    ]
                    medians[width] = statistics.median(values)
                if not (
                    medians[1024] > 0.20
                    and medians[1024] >= 1.5 * medians[512]
                ):
                    rare_half_failure = False
            if full_high > 0.20 and rare_half_failure:
                fail_reasons.append(
                    f"replicated rare-dominance fail for field={field}, time={checkpoint}"
                )
    return pass_ok, fail_reasons


def decision(
    points: dict,
    intervals: dict,
    halves: list[dict],
    numerical_valid: bool,
    tail_pass: bool,
    rare_fail_reasons: list[str],
) -> tuple[str, list[str], list[str]]:
    pass_reasons = []
    for key in points:
        interval = intervals[key]
        if interval["beta_familywise_upper_95"] > 0.20:
            pass_reasons.append(f"{key} familywise beta upper exceeds 0.20")
        if interval["alpha_familywise_upper_95"] > 0.10:
            pass_reasons.append(f"{key} familywise alpha upper exceeds 0.10")
        if interval["a1024_familywise_upper_95"] > 0.15:
            pass_reasons.append(f"{key} familywise a1024 upper exceeds 0.15")
        for half_index, half in enumerate(halves):
            estimate = half[key]
            if estimate["beta"] > 0.30 or (
                estimate["alpha"] > 0.15 and estimate["a1024"] > 0.30
            ):
                pass_reasons.append(
                    f"{key} confirmation half {half_index + 1} exceeds a fail point threshold"
                )
    if not tail_pass:
        pass_reasons.append("one or more locked n=1024 tail pass gates failed")

    fail_reasons = list(rare_fail_reasons)
    for field in FIELDS:
        for checkpoint in TIMES:
            for adjacent in ((0.05, 0.10), (0.10, 0.20)):
                keys = [(field, checkpoint, lam) for lam in adjacent]
                beta_full = all(
                    intervals[key]["beta_cell_lower_95"] > 0.30 for key in keys
                )
                beta_halves = all(
                    all(half[key]["beta"] > 0.30 for key in keys) for half in halves
                )
                alignment_full = all(
                    intervals[key]["alpha_cell_lower_95"] > 0.15
                    and intervals[key]["a1024_cell_lower_95"] > 0.30
                    for key in keys
                )
                alignment_halves = all(
                    all(
                        half[key]["alpha"] > 0.15 and half[key]["a1024"] > 0.30
                        for key in keys
                    )
                    for half in halves
                )
                if beta_full and beta_halves:
                    fail_reasons.append(
                        f"replicated beta fail for field={field}, time={checkpoint}, lambdas={adjacent}"
                    )
                if alignment_full and alignment_halves:
                    fail_reasons.append(
                        f"replicated alignment fail for field={field}, time={checkpoint}, lambdas={adjacent}"
                    )

    if not numerical_valid:
        return "inconclusive", pass_reasons, fail_reasons
    if fail_reasons:
        return "empirical_fail", pass_reasons, fail_reasons
    if not pass_reasons:
        return "empirical_pass", pass_reasons, fail_reasons
    return "inconclusive", pass_reasons, fail_reasons


def factorization_status(interval: dict) -> str:
    lower = interval["a1024_familywise_lower_95"]
    upper = interval["a1024_familywise_upper_95"]
    if lower >= -0.15 and upper <= 0.15 and lower <= 0.0 <= upper:
        return "compatible"
    if lower > 0.0:
        return "resolved_positive_alignment"
    if upper < 0.0:
        return "resolved_negative_alignment"
    return "inconclusive"


def secondary_summary(metrics: list[dict]) -> list[dict]:
    rows = []
    for field in ("z2", "x2"):
        for checkpoint in (0.25, 0.5):
            for lam in LAMBDAS:
                means = []
                for width in WIDTHS:
                    values = [
                        float(row["M"])
                        for row in metrics
                        if row["field"] == field
                        and float(row["time"]) == checkpoint
                        and float(row["lambda"]) == lam
                        and int(row["width"]) == width
                    ]
                    means.append(statistics.fmean(values))
                rows.append(
                    {
                        "field": field,
                        "time": checkpoint,
                        "lambda": lam,
                        "beta": slope(
                            [math.log(width) for width in WIDTHS],
                            [math.log(value) for value in means],
                        ),
                        **{f"mean_M_{width}": value for width, value in zip(WIDTHS, means)},
                    }
                )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--primary", nargs="+", required=True)
    parser.add_argument("--controls", required=True)
    parser.add_argument("--fd", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    primary_dirs = [Path(value) for value in args.primary]
    metrics, trajectories, primary_metadata = collect_primary(primary_dirs)
    grouped = indexed_data(metrics)
    shape_errors = validate_primary_shape(grouped)
    points = point_estimates(grouped)
    halves = [half_estimates(grouped, 0, 24), half_estimates(grouped, 24, 48)]
    intervals, bootstrap = bootstrap_intervals(grouped, points)
    primary_gate = primary_validity(trajectories, primary_metadata, shape_errors)
    control_gate, control_rows = control_validity(Path(args.controls))
    fd_gate, fd_rows = fd_validity(Path(args.fd))
    tail_rows, tail_lookup = tail_summaries(metrics)
    tail_pass, rare_fail_reasons = tail_pass_and_fail(metrics, tail_lookup)
    numerical_valid = primary_gate["pass"] and control_gate["pass"] and fd_gate["pass"]
    finite_decision, pass_obstacles, fail_reasons = decision(
        points, intervals, halves, numerical_valid, tail_pass, rare_fail_reasons
    )

    cell_rows = []
    for key in points:
        field, checkpoint, lam = key
        point = points[key]
        interval = intervals[key]
        cell_rows.append(
            {
                "field": field,
                "time": checkpoint,
                "lambda": lam,
                "beta": point["beta"],
                "beta_cell_lower_95": interval["beta_cell_lower_95"],
                "beta_cell_upper_95": interval["beta_cell_upper_95"],
                "beta_familywise_upper_95": interval["beta_familywise_upper_95"],
                "alpha": point["alpha"],
                "alpha_cell_lower_95": interval["alpha_cell_lower_95"],
                "alpha_cell_upper_95": interval["alpha_cell_upper_95"],
                "alpha_familywise_upper_95": interval["alpha_familywise_upper_95"],
                "a1024": point["a1024"],
                "a1024_cell_lower_95": interval["a1024_cell_lower_95"],
                "a1024_cell_upper_95": interval["a1024_cell_upper_95"],
                "a1024_familywise_lower_95": interval["a1024_familywise_lower_95"],
                "a1024_familywise_upper_95": interval["a1024_familywise_upper_95"],
                "factorization_status": factorization_status(interval),
                **{f"mean_M_{width}": point["mean_M"][width] for width in WIDTHS},
                **{
                    f"alignment_{width}": point["alignment"][width]
                    for width in WIDTHS
                },
                "half1_beta": halves[0][key]["beta"],
                "half2_beta": halves[1][key]["beta"],
                "half1_alpha": halves[0][key]["alpha"],
                "half2_alpha": halves[1][key]["alpha"],
                "half1_a1024": halves[0][key]["a1024"],
                "half2_a1024": halves[1][key]["a1024"],
            }
        )

    output = Path(args.output)
    if output.exists() and any(output.iterdir()):
        raise FileExistsError(f"refusing to overwrite nonempty output: {output}")
    output.mkdir(parents=True, exist_ok=True)
    write_csv(output / "cell_summary.csv", cell_rows)
    write_csv(output / "tail_summary.csv", tail_rows)
    write_csv(output / "secondary_summary.csv", secondary_summary(metrics))
    write_csv(output / "fd_gate_details.csv", fd_gate["comparisons"])

    control_metadata = json.loads((Path(args.controls) / "metadata.json").read_text())
    fd_metadata = json.loads((Path(args.fd) / "metadata.json").read_text())
    all_script_hashes = {
        item["script_sha256"] for item in primary_metadata
    } | {control_metadata["script_sha256"], fd_metadata["script_sha256"]}
    if len(all_script_hashes) != 1:
        numerical_valid = False
        finite_decision = "inconclusive"
        primary_gate["failures"].append("production/control source hashes differ")
        primary_gate["pass"] = False

    summary = {
        "analytic_conclusion": {
            "uniform_square_exponential_premise": "falsified_analytically_before_run",
            "reason": (
                "At finite n,t=0, conditional on u,G1,G2, r2_i is Gaussian in A "
                "with random variance of unbounded support, so E exp(lambda r2_i^2) "
                "is infinite for every lambda>0."
            ),
            "scope_of_numerics": "finite deliberately typical-sample diagnostic only",
        },
        "finite_sample_preregistered_decision": finite_decision,
        "numerical_validity": numerical_valid,
        "pass_obstacles": pass_obstacles,
        "fail_reasons": fail_reasons,
        "primary_validity": primary_gate,
        "control_validity": control_gate,
        "finite_difference_validity": fd_gate,
        "tail_pass_component": tail_pass,
        "bootstrap": bootstrap,
        "factorization_counts": {
            status: sum(row["factorization_status"] == status for row in cell_rows)
            for status in (
                "compatible",
                "resolved_positive_alignment",
                "resolved_negative_alignment",
                "inconclusive",
            )
        },
        "rank_control": {
            "minimum_median_rank_to_shuffle_ratio": min(
                row["rank_to_shuffle_ratio_median"] for row in tail_rows
            ),
            "maximum_median_rank_to_shuffle_ratio": max(
                row["rank_to_shuffle_ratio_median"] for row in tail_rows
            ),
        },
        "artifact_counts": {
            "metric_rows": len(metrics),
            "trajectory_rows": len(trajectories),
            "control_rows": len(control_rows),
            "finite_difference_rows": len(fd_rows),
        },
        "source_hashes": sorted(all_script_hashes),
        "primary_metadata": primary_metadata,
        "control_metadata": control_metadata,
        "fd_metadata": fd_metadata,
        "analysis": {
            "command": [sys.executable, *sys.argv],
            "script_sha256": sha256(Path(__file__).resolve()),
        },
    }
    (output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(
        json.dumps(
            {
                "analytic_uniform_claim": "falsified",
                "finite_sample_decision": finite_decision,
                "numerical_validity": numerical_valid,
                "factorization_counts": summary["factorization_counts"],
                "pass_obstacles": len(pass_obstacles),
                "fail_reasons": fail_reasons,
                "output": str(output),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
