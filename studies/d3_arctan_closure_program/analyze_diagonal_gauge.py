#!/usr/bin/env python3
"""Apply the frozen diagonal-gauge experiment verdict mechanically."""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path

import numpy as np


P_ORDERS = (2, 4, 6, 8)
CAVITY_KEYS = (
    "sqrt_n_dz2_l2",
    "sqrt_n_dtheta2_l2",
    "sqrt_n_dz3_l2",
    "sqrt_n_dtheta3_l2",
)


def load_runs(path: Path):
    metadata = None
    runs = []
    with path.open() as handle:
        for line in handle:
            item = json.loads(line)
            if item.get("kind") == "metadata":
                metadata = item
            else:
                runs.append(item)
    return metadata, runs


def last_at(records, horizon):
    eligible = [row for row in records if row["s"] <= horizon + 1e-12]
    return max(eligible, key=lambda row: row["s"])


def summarize_run(run, horizon):
    records = [row for row in run["records"] if row["s"] <= horizon + 1e-12]
    out = {
        "min_kappa2_q01": min(row["kappa2_quantiles"]["0.01"] for row in records),
        "min_kappa3_q01": min(
            row["sampled_kappa3_quantiles"]["0.01"] for row in records
        ),
        "max_leverage": max(row["leverage_c2_top1pct_r2"] for row in records),
        "endpoint_f": last_at(records, horizon)["f"],
        "endpoint_K": last_at(records, horizon)["K"],
    }
    for field in ("y2", "c2", "sampled_y3", "sampled_c3"):
        for p in P_ORDERS:
            key = f"{field}_l{p}_over_p"
            out[key] = max(row[field][f"l{p}_over_p"] for row in records)

    cavity_values = defaultdict(list)
    for cavity in run["cavities"]:
        rows = [row for row in cavity["records"] if row["s"] <= horizon + 1e-12]
        for key in CAVITY_KEYS:
            cavity_values[key].append(max(row[key] for row in rows))
    for key, values in cavity_values.items():
        # First aggregate within a seed; widths are aggregated across seeds below.
        out[key] = float(np.median(values))
    out["solver_defect"] = max(
        [run["main_solver_identity_defect"]]
        + [cavity["solver_identity_defect"] for cavity in run["cavities"]]
    )
    return out


def width_summaries(runs, horizon):
    grouped = defaultdict(list)
    for run in runs:
        grouped[run["n"]].append(summarize_run(run, horizon))
    result = {}
    for width, summaries in sorted(grouped.items()):
        keys = summaries[0].keys()
        result[width] = {
            key: float(np.median([summary[key] for summary in summaries]))
            for key in keys
        }
    return result


def slope(table, key):
    widths = np.asarray(sorted(table), dtype=float)
    values = np.asarray([table[int(width)][key] for width in widths], dtype=float)
    if len(widths) < 2 or np.any(values <= 0):
        return math.nan
    return float(np.polyfit(np.log(widths), np.log(values), 1)[0])


def endpoint_factor(table, key):
    widths = sorted(table)
    a, b = table[widths[0]][key], table[widths[-1]][key]
    if a == 0 or b == 0:
        return math.inf if a != b else 1.0
    return max(a / b, b / a)


def compare_steps(coarse, fine):
    comparisons = []
    for width in sorted(set(coarse) & set(fine)):
        for key in coarse[width]:
            if key == "solver_defect":
                continue
            a, b = coarse[width][key], fine[width][key]
            relative = abs(a - b) / max(abs(a), abs(b), 1e-12)
            comparisons.append(
                {"width": width, "metric": key, "relative_change": relative}
            )
    return sorted(comparisons, key=lambda row: row["relative_change"], reverse=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--coarse", type=Path, required=True)
    parser.add_argument("--fine", type=Path)
    args = parser.parse_args()

    metadata, runs = load_runs(args.coarse)
    coarse_h1 = width_summaries(runs, 1.0)
    coarse_h2 = width_summaries(runs, 2.0)
    widths = sorted(coarse_h2)

    support_metrics = [
        *(f"{field}_l{p}_over_p" for field in ("y2", "c2") for p in P_ORDERS),
        *CAVITY_KEYS,
    ]
    slopes_h1 = {key: slope(coarse_h1, key) for key in support_metrics}
    slopes_h2 = {key: slope(coarse_h2, key) for key in support_metrics}
    factors_h2 = {key: endpoint_factor(coarse_h2, key) for key in support_metrics}
    leverage_slopes = {
        "h1": slope(coarse_h1, "max_leverage"),
        "h2": slope(coarse_h2, "max_leverage"),
    }
    kappa_slopes = {
        "kappa2_h1": slope(coarse_h1, "min_kappa2_q01"),
        "kappa2_h2": slope(coarse_h2, "min_kappa2_q01"),
        "kappa3_h1": slope(coarse_h1, "min_kappa3_q01"),
        "kappa3_h2": slope(coarse_h2, "min_kappa3_q01"),
    }

    all_run_summaries = [summarize_run(run, 2.0) for run in runs]
    maximum_solver_defect = max(row["solver_defect"] for row in all_run_summaries)
    global_min_kappa = min(
        min(row["min_kappa2_q01"], row["min_kappa3_q01"])
        for row in all_run_summaries
    )
    max_leverage_median = max(
        coarse_h2[width]["max_leverage"] for width in widths
    )

    fine_output = None
    solver_ok = maximum_solver_defect < 1e-4
    step_ok = False
    if args.fine:
        _, fine_runs = load_runs(args.fine)
        fine_h2 = width_summaries(fine_runs, 2.0)
        comparisons = compare_steps(coarse_h2, fine_h2)
        fine_defect = max(
            summarize_run(run, 2.0)["solver_defect"] for run in fine_runs
        )
        maximum_solver_defect = max(maximum_solver_defect, fine_defect)
        solver_ok = maximum_solver_defect < 1e-4
        step_ok = bool(comparisons) and comparisons[0]["relative_change"] <= 0.05
        fine_output = {
            "width_summaries": fine_h2,
            "largest_relative_changes": comparisons[:12],
            "maximum_relative_change": comparisons[0]["relative_change"],
        }

    support = {
        "solver_and_step_halving": solver_ok and step_ok,
        "kappa_floor": global_min_kappa > 0.02,
        "bath_factor": max(factors_h2[key] for key in support_metrics[:8]) <= 1.5,
        "bath_slope": max(slopes_h2[key] for key in support_metrics[:8]) <= 0.10,
        "cavity_factor": max(factors_h2[key] for key in CAVITY_KEYS) <= 1.5,
        "cavity_slope": max(slopes_h2[key] for key in CAVITY_KEYS) <= 0.10,
        "leverage_level": max_leverage_median < 4.0,
        "leverage_slope": leverage_slopes["h2"] <= 0.10,
    }
    support["all"] = all(support.values())

    growth_against = [
        key
        for key in support_metrics
        if slopes_h1[key] > 0.25 and slopes_h2[key] > 0.25
    ]
    kappa_against = [
        key.replace("_h1", "")
        for key in ("kappa2_h1", "kappa3_h1")
        if kappa_slopes[key] < -0.25
        and kappa_slopes[key.replace("h1", "h2")] < -0.25
    ]
    leverage_against = (
        leverage_slopes["h1"] > 0.25 and leverage_slopes["h2"] > 0.25
    )

    output = {
        "coarse_metadata": metadata,
        "coarse_run_count": len(runs),
        "coarse_width_summaries_h2": coarse_h2,
        "slopes_h1": slopes_h1,
        "slopes_h2": slopes_h2,
        "endpoint_factors_h2": factors_h2,
        "leverage_slopes": leverage_slopes,
        "kappa_slopes": kappa_slopes,
        "maximum_solver_defect": maximum_solver_defect,
        "global_min_reported_kappa_q01": global_min_kappa,
        "maximum_width_median_leverage": max_leverage_median,
        "fine": fine_output,
        "support_conditions": support,
        "evidence_against": {
            "growth_metrics": growth_against,
            "kappa_metrics": kappa_against,
            "leverage": leverage_against,
            "triggered": bool(growth_against or kappa_against or leverage_against),
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
