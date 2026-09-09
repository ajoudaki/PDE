#!/usr/bin/env python3
"""Summarize preregistered O1 outputs without plotting dependencies."""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path

import numpy as np

if __package__:
    from ._analysis_paths import guard_outputs
else:
    from _analysis_paths import guard_outputs


def read_rows(paths):
    rows = []
    for path in paths:
        with Path(path).open() as handle:
            rows.extend(csv.DictReader(handle))
    return rows


def mean_sd(values):
    values = list(values)
    return {"mean": statistics.mean(values), "sd": statistics.pstdev(values)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--primary", nargs="+", required=True)
    parser.add_argument("--step", nargs="+", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    guard_outputs((args.output,), [
        *args.primary, *args.step,
        *(Path(path).with_name("metadata.json") for path in args.step),
    ])
    rows = read_rows(args.primary)
    summary = {"width": {}, "step_refinement": {}}
    widths = sorted({int(row["width"]) for row in rows})
    powers = [2, 3, 4, 6, 8, 10, 12, 16]
    for width in widths:
        raw = [
            row for row in rows
            if int(row["width"]) == width and row["time"] == "1.0" and row["clip"] == "raw"
        ]
        item = {}
        for key in ["r2_l2", "tau_1", "tau_1.5", "tau_2", "tau_2.5"]:
            item[key] = mean_sd(float(row[key]) for row in raw)
        for power in powers:
            for suffix in ["over_sqrtp", "over_p", "effective_count"]:
                key = f"M{power}_{suffix}"
                item[key] = mean_sd(float(row[key]) for row in raw)
        thresholds = np.asarray([1.0, 1.5, 2.0, 2.5])
        tails = np.asarray([
            item["tau_1"]["mean"], item["tau_1.5"]["mean"],
            item["tau_2"]["mean"], item["tau_2.5"]["mean"],
        ])
        y = np.log(tails)
        fits = {}
        for name, x in [("linear", thresholds), ("quadratic", thresholds**2)]:
            design = np.column_stack([np.ones(len(x)), x])
            coefficient = np.linalg.lstsq(design, y, rcond=None)[0]
            residual = y - design @ coefficient
            fits[name] = {
                "intercept": float(coefficient[0]),
                "slope": float(coefficient[1]),
                "rmse": float(np.sqrt(np.mean(residual**2))),
            }
        item["tail_fits"] = fits
        clips = {}
        for clip in ["1.0", "2.0", "3.0", "4.0", "6.0", "8.0"]:
            selected = [
                row for row in rows
                if int(row["width"]) == width and row["time"] == "1.0" and row["clip"] == clip
            ]
            clips[clip] = {
                key: mean_sd(float(row[key]) for row in selected)
                for key in ["r2_l2", "M8_over_sqrtp", "M10_over_p", "delta_u_raw"]
            }
        item["clips"] = clips
        summary["width"][str(width)] = item

    step_sets = []
    for path in args.step:
        rows_i = read_rows([path])
        metadata_path = Path(path).with_name("metadata.json")
        metadata = json.loads(metadata_path.read_text())
        step_sets.append((float(metadata["dt"]), rows_i))
    step_sets.sort(reverse=True)
    ref_dt, ref_rows = step_sets[-1]
    ref = {(r["trial"], r["time"], r["clip"]): r for r in ref_rows}
    for dt, rows_i in step_sets[:-1]:
        current = {(r["trial"], r["time"], r["clip"]): r for r in rows_i}
        item = {}
        for key in ["r2_l2", "M4", "M8", "M12", "tau_1", "tau_2", "predictor", "kernel"]:
            errors = [
                abs(float(row[key]) - float(ref[index][key]))
                for index, row in current.items() if index[1] == "1.0"
            ]
            item[key] = {"max_abs": max(errors), "mean_abs": statistics.mean(errors)}
        summary["step_refinement"][f"{dt:g}_vs_{ref_dt:g}"] = item

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({"output": str(out), "widths": widths, "reference_dt": ref_dt}, indent=2))


if __name__ == "__main__":
    main()
