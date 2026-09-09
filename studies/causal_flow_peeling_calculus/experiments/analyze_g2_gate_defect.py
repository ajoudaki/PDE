#!/usr/bin/env python3
"""Summarize preregistered G2 local-defect slopes."""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path


METRICS = (
    "A_error",
    "u_error",
    "G1_fro_error",
    "G2_fro_error",
    "predictor_error",
    "kernel_error",
    "r2_error",
    "b2_error",
    "r1_error",
    "b1_error",
)


def linear_slope(xs, ys):
    xbar = statistics.fmean(xs)
    ybar = statistics.fmean(ys)
    denom = sum((x - xbar) ** 2 for x in xs)
    return sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys)) / denom


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    with Path(args.input).open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    grouped = defaultdict(list)
    for row in rows:
        key = (float(row["alpha"]), int(row["width"]), float(row["base_time"]), int(row["trial"]))
        grouped[key].append(row)

    slope_rows = []
    for (alpha, width, base_time, trial), items in grouped.items():
        items.sort(key=lambda r: float(r["h"]), reverse=True)
        result = {
            "alpha": alpha,
            "width": width,
            "base_time": base_time,
            "trial": trial,
            "max_top_constraint": max(float(r["top_constraint"]) for r in items),
            "max_r2": max(float(r["r2_max_reference"]) for r in items),
            "max_r2_l4_over_l2": max(float(r["r2_l4_over_l2"]) for r in items),
        }
        logs_h = [math.log(float(r["h"])) for r in items]
        for metric in METRICS:
            values = [max(float(r[metric]), 1e-30) for r in items]
            result[f"{metric}_slope_all"] = linear_slope(logs_h, [math.log(v) for v in values])
            result[f"{metric}_slope_small"] = linear_slope(
                logs_h[-3:], [math.log(v) for v in values[-3:]]
            )
            result[f"{metric}_over_h_smallest"] = values[-1] / float(items[-1]["h"])
            result[f"{metric}_over_h2_smallest"] = values[-1] / float(items[-1]["h"]) ** 2
        slope_rows.append(result)

    aggregate = []
    keys = sorted({(r["alpha"], r["width"], r["base_time"]) for r in slope_rows})
    for alpha, width, base_time in keys:
        subset = [r for r in slope_rows if (r["alpha"], r["width"], r["base_time"]) == (alpha, width, base_time)]
        out = {"alpha": alpha, "width": width, "base_time": base_time, "trials": len(subset)}
        for metric in METRICS:
            for suffix in ("slope_all", "slope_small", "over_h_smallest", "over_h2_smallest"):
                field = f"{metric}_{suffix}"
                vals = [r[field] for r in subset]
                out[f"median_{field}"] = statistics.median(vals)
                out[f"min_{field}"] = min(vals)
                out[f"max_{field}"] = max(vals)
        out["max_top_constraint"] = max(r["max_top_constraint"] for r in subset)
        out["median_max_r2"] = statistics.median(r["max_r2"] for r in subset)
        out["median_r2_l4_over_l2"] = statistics.median(r["max_r2_l4_over_l2"] for r in subset)
        aggregate.append(out)

    result = {"per_trial": slope_rows, "aggregate": aggregate, "metrics": METRICS}
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n")

    headline = []
    for row in aggregate:
        headline.append(
            {
                "alpha": row["alpha"],
                "width": row["width"],
                "base_time": row["base_time"],
                "u_slope": row["median_u_error_slope_small"],
                "G1_slope": row["median_G1_fro_error_slope_small"],
                "kernel_slope": row["median_kernel_error_slope_small"],
                "r2_slope": row["median_r2_error_slope_small"],
                "u_over_h": row["median_u_error_over_h_smallest"],
                "kernel_over_h": row["median_kernel_error_over_h_smallest"],
                "r2_max": row["median_max_r2"],
            }
        )
    print(json.dumps(headline, indent=2))


if __name__ == "__main__":
    main()
