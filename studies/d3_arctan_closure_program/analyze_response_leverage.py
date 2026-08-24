"""Aggregate the preregistered response-leverage experiment."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

import numpy as np


HORIZONS = (1.0, 2.0, 4.0)
STATS = (
    "frobenius",
    "entropy",
    "entropy_ratio",
    "inverse_participation",
    "max_n_weight",
    "top_one_percent_mass",
)


def load(path):
    with Path(path).open(encoding="utf-8") as handle:
        lines = [json.loads(line) for line in handle if line.strip()]
    if not lines or lines[0].get("kind") != "metadata":
        raise ValueError(f"missing metadata in {path}")
    return lines[0], lines[1:]


def maxima(run, horizon):
    rows = [row for row in run["records"] if row["s"] <= horizon + 1e-12]
    return {stat: max(row[stat] for row in rows) for stat in STATS}


def slope(widths, values):
    return float(np.polyfit(np.log(widths), np.log(np.maximum(values, 1e-300)), 1)[0])


def summarize(runs):
    result = {}
    for horizon in HORIZONS:
        grouped = {stat: defaultdict(list) for stat in STATS}
        for run in runs:
            for stat, value in maxima(run, horizon).items():
                grouped[stat][run["n"]].append(value)
        result[str(horizon)] = {}
        for stat in STATS:
            widths = np.array(sorted(grouped[stat]), dtype=float)
            medians = np.array(
                [np.median(grouped[stat][int(n)]) for n in widths], dtype=float
            )
            result[str(horizon)][stat] = {
                "widths": widths.astype(int).tolist(),
                "medians": medians.tolist(),
                "slope": slope(widths, medians),
                "small_to_large_ratio": float(medians[-1] / max(medians[0], 1e-300)),
            }
    return result


def paired_audit(coarse_runs, fine_runs):
    coarse = {(r["n"], r["seed"]): r for r in coarse_runs}
    fine = {(r["n"], r["seed"]): r for r in fine_runs}
    failures = []
    comparisons = 0
    for key in sorted(set(coarse) & set(fine)):
        for horizon in HORIZONS:
            left = maxima(coarse[key], horizon)
            right = maxima(fine[key], horizon)
            for stat in STATS:
                x, y = left[stat], right[stat]
                absolute = abs(x - y)
                symmetric = 2.0 * absolute / max(abs(x) + abs(y), 1e-300)
                passed = absolute <= 1e-3 if max(abs(x), abs(y)) < 0.02 else symmetric <= 0.10
                comparisons += 1
                if not passed:
                    failures.append({
                        "n": key[0], "seed": key[1], "horizon": horizon,
                        "stat": stat, "absolute": absolute,
                        "symmetric_relative": symmetric,
                    })
    return {
        "paired_runs": len(set(coarse) & set(fine)),
        "comparisons": comparisons,
        "failures": failures,
        "pass": bool(comparisons and not failures),
    }


def verdict(summary, solver_pass):
    against = []
    support = []
    for horizon in ("2.0", "4.0"):
        stats = summary[horizon]
        against.extend([
            stats["frobenius"]["slope"] >= 0.25,
            stats["inverse_participation"]["slope"] >= 0.30
            and stats["inverse_participation"]["medians"][-1] > 8.0,
            stats["top_one_percent_mass"]["medians"][-1] > 0.35
            and stats["top_one_percent_mass"]["medians"][-1]
            > stats["top_one_percent_mass"]["medians"][0],
            stats["entropy_ratio"]["medians"][-1] > 0.45
            and stats["entropy_ratio"]["medians"][-1]
            > stats["entropy_ratio"]["medians"][0],
        ])
        support.extend([
            stats["frobenius"]["slope"] < 0.15,
            stats["inverse_participation"]["slope"] < 0.15,
            stats["inverse_participation"]["medians"][-1] < 5.0,
            stats["top_one_percent_mass"]["medians"][-1] < 0.20,
            stats["entropy_ratio"]["medians"][-1] < 0.30,
        ])
    if not solver_pass:
        return "inconclusive_solver_audit"
    if any(against):
        return "evidence_against_delocalization"
    if all(support):
        return "mechanistic_support_only"
    return "inconclusive"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--coarse", required=True)
    parser.add_argument("--fine")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    coarse_meta, coarse_runs = load(args.coarse)
    result = {
        "coarse_metadata": coarse_meta,
        "summary": summarize(coarse_runs),
    }
    solver_pass = True
    if args.fine:
        fine_meta, fine_runs = load(args.fine)
        result["fine_metadata"] = fine_meta
        result["solver_audit"] = paired_audit(coarse_runs, fine_runs)
        solver_pass = result["solver_audit"]["pass"]
    result["verdict"] = verdict(result["summary"], solver_pass)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
