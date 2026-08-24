"""Aggregate the preregistered middle-response experiment.

The aggregation convention is frozen in
EXPERIMENT_PREREGISTRATION_2026-08-23.md.  This script reads JSONL artifacts
and prints a machine-reproducible JSON summary; it never edits the inputs.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

import numpy as np


HORIZONS = (0.5, 1.0, 2.0)
FIELDS = ("r2", "r2_static", "r2_learned")
MOMENTS = (2, 4, 6, 8)
BOOTSTRAP_SEED = 2026082399
BOOTSTRAPS = 20_000


def load(path: Path | None):
    if path is None:
        return None, []
    with path.open(encoding="utf-8") as handle:
        lines = [json.loads(line) for line in handle if line.strip()]
    if not lines or lines[0].get("kind") != "metadata":
        raise ValueError(f"missing metadata line in {path}")
    return lines[0], lines[1:]


def run_main_values(run, horizon: float):
    records = [r for r in run["main"]["records"] if r["s"] <= horizon + 1e-12]
    out = {}
    for field in FIELDS:
        for p in MOMENTS:
            key = f"{field}.l{p}_over_p"
            out[key] = max(r[field][f"l{p}_over_p"] for r in records)
        out[f"{field}.condensation"] = max(
            r[field]["condensation"] for r in records
        )
        out[f"{field}.max"] = max(r[field]["max"] for r in records)
    for block in range(4):
        out[f"energy.{block}"] = max(r["energies"][block] for r in records)
    out["K"] = max(r["K"] for r in records)
    return out


def run_cavity_values(run, horizon: float):
    column_values = defaultdict(list)
    for cavity in run["cavities"]:
        records = [r for r in cavity["records"] if r["s"] <= horizon + 1e-12]
        for key in (
            "H_std",
            "delta_abs",
            "delta_relative",
            "b3_path_difference_l2",
        ):
            column_values[key].append(max(r[key] for r in records))
        column_values["sqrt_n_b3_path_difference_l2"].append(
            np.sqrt(run["n"])
            * max(r["b3_path_difference_l2"] for r in records)
        )
    return {
        key: float(np.median(values)) for key, values in column_values.items()
    } | {
        f"{key}.rms": float(np.sqrt(np.mean(np.square(values))))
        for key, values in column_values.items()
    }


def slope(widths, values):
    return float(np.polyfit(np.log(widths), np.log(np.maximum(values, np.finfo(float).tiny)), 1)[0])


def clustered_summary(grouped, rng):
    widths = np.array(sorted(grouped), dtype=float)
    medians = np.array([np.median(grouped[int(n)]) for n in widths])
    observed = slope(widths, medians)
    boot_medians = np.empty((BOOTSTRAPS, widths.size))
    for column, n in enumerate(widths.astype(int)):
        values = np.asarray(grouped[n], dtype=float)
        indices = rng.integers(0, values.size, size=(BOOTSTRAPS, values.size))
        boot_medians[:, column] = np.median(values[indices], axis=1)
    log_widths = np.log(widths)
    centered_widths = log_widths - np.mean(log_widths)
    log_boot = np.log(np.maximum(boot_medians, np.finfo(float).tiny))
    samples = (
        (log_boot - np.mean(log_boot, axis=1, keepdims=True)) @ centered_widths
        / np.sum(centered_widths * centered_widths)
    )
    return {
        "widths": widths.astype(int).tolist(),
        "medians": medians.tolist(),
        "small_to_large_ratio": float(medians[-1] / max(medians[0], np.finfo(float).tiny)),
        "slope": observed,
        "slope_ci95": np.quantile(samples, [0.025, 0.975]).tolist(),
    }


def aggregate_runs(runs, cavity: bool):
    rng = np.random.default_rng(BOOTSTRAP_SEED + int(cavity))
    result = {}
    extractor = run_cavity_values if cavity else run_main_values
    for horizon in HORIZONS:
        grouped_by_stat = defaultdict(lambda: defaultdict(list))
        for run in runs:
            values = extractor(run, horizon)
            for key, value in values.items():
                grouped_by_stat[key][run["n"]].append(value)
        result[str(horizon)] = {
            key: clustered_summary(grouped, rng)
            for key, grouped in sorted(grouped_by_stat.items())
        }
    return result


def solver_audit(coarse_runs, fine_runs, cavity: bool):
    coarse = {(r["n"], r["seed"]): r for r in coarse_runs}
    fine = {(r["n"], r["seed"]): r for r in fine_runs}
    common = sorted(set(coarse) & set(fine))
    extractor = run_cavity_values if cavity else run_main_values
    entries = []
    for key in common:
        for horizon in HORIZONS:
            left = extractor(coarse[key], horizon)
            right = extractor(fine[key], horizon)
            for stat in sorted(set(left) & set(right)):
                x, y = left[stat], right[stat]
                absolute = abs(x - y)
                symmetric = 2.0 * absolute / max(abs(x) + abs(y), np.finfo(float).tiny)
                threshold_ok = absolute <= 1e-3 if max(abs(x), abs(y)) < 0.02 else symmetric <= 0.05
                entries.append({
                    "n": key[0],
                    "seed": key[1],
                    "horizon": horizon,
                    "stat": stat,
                    "absolute": absolute,
                    "symmetric_relative": symmetric,
                    "pass": bool(threshold_ok),
                })
    identity_defects = [
        r["main"]["solver_identity_defect"] for r in coarse_runs + fine_runs
    ]
    if cavity:
        identity_defects.extend(
            cavity_record["solver_identity_defect"]
            for r in coarse_runs + fine_runs
            for cavity_record in r["cavities"]
        )
    return {
        "paired_runs": len(common),
        "comparisons": len(entries),
        "failures": [entry for entry in entries if not entry["pass"]],
        "max_symmetric_relative": max(
            (entry["symmetric_relative"] for entry in entries), default=None
        ),
        "max_identity_defect": max(identity_defects, default=None),
        "identity_pass": bool(
            all(defect <= 0.01 for defect in identity_defects)
        ),
    }


def interpretation(main_summary, cavity_summary):
    checks = []
    for horizon, stats in main_summary.items():
        for p in MOMENTS:
            item = stats[f"r2.l{p}_over_p"]
            checks.append({
                "condition": 1,
                "horizon": horizon,
                "p": p,
                "pass": item["small_to_large_ratio"] <= 1.5,
                "value": item["small_to_large_ratio"],
            })
            checks.append({
                "condition": 2,
                "horizon": horizon,
                "p": p,
                "pass": item["slope_ci95"][1] < 0.10,
                "value": item["slope_ci95"][1],
            })
        condensation = stats["r2.condensation"]
        medians = condensation["medians"]
        checks.append({
            "condition": 3,
            "horizon": horizon,
            "pass": bool(medians[-1] < 0.20 and medians[-1] < medians[0]),
            "value": {"first": medians[0], "last": medians[-1]},
        })
        for block in range(4):
            item = stats[f"energy.{block}"]
            checks.append({
                "condition": 5,
                "horizon": horizon,
                "block": block,
                "pass": item["small_to_large_ratio"] < 2.0,
                "value": item["small_to_large_ratio"],
            })
    if cavity_summary:
        for horizon, stats in cavity_summary.items():
            for key in ("delta_abs", "delta_relative"):
                item = stats[key]
                checks.append({
                    "condition": 4,
                    "horizon": horizon,
                    "stat": key,
                    "pass": item["slope_ci95"][1] < 0.10,
                    "value": item["slope_ci95"][1],
                })
    return {
        "checks": checks,
        "all_pass": bool(checks and all(check["pass"] for check in checks)),
        "fail_count": sum(not check["pass"] for check in checks),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--main", type=Path, required=True)
    parser.add_argument("--cavity", type=Path)
    parser.add_argument("--main-fine", type=Path)
    parser.add_argument("--cavity-fine", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    main_meta, main_runs = load(args.main)
    cavity_meta, cavity_runs = load(args.cavity)
    main_fine_meta, main_fine_runs = load(args.main_fine)
    cavity_fine_meta, cavity_fine_runs = load(args.cavity_fine)
    main_summary = aggregate_runs(main_runs, cavity=False)
    cavity_summary = aggregate_runs(cavity_runs, cavity=True) if cavity_runs else None
    result = {
        "metadata": {
            "bootstrap_seed": BOOTSTRAP_SEED,
            "bootstrap_replicates": BOOTSTRAPS,
            "inputs": {
                "main": main_meta,
                "cavity": cavity_meta,
                "main_fine": main_fine_meta,
                "cavity_fine": cavity_fine_meta,
            },
        },
        "main": main_summary,
        "cavity": cavity_summary,
        "interpretation": interpretation(main_summary, cavity_summary),
    }
    if main_fine_runs:
        coarse_subset = [r for r in main_runs if r["n"] in {128, 256}]
        result["main_solver_audit"] = solver_audit(
            coarse_subset, main_fine_runs, cavity=False
        )
    if cavity_fine_runs:
        coarse_subset = [r for r in cavity_runs if r["n"] in {128, 256}]
        result["cavity_solver_audit"] = solver_audit(
            coarse_subset, cavity_fine_runs, cavity=True
        )
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(payload, end="")
    else:
        args.output.write_text(payload, encoding="utf-8")


if __name__ == "__main__":
    main()
