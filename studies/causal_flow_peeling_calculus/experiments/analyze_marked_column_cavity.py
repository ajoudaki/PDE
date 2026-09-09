#!/usr/bin/env python3
"""Claim-level analysis for preregistered marked-column probe C1."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path


REPLACEMENT_METRICS = (
    "marked_r2_abs",
    "marked_r2_over_column",
    "x2_diff_l2n",
    "z3_diff_l2n",
    "b3_diff_l2n",
    "u_diff_l2n",
    "A_diff_l2n",
    "r2_bulk_diff_l2n",
    "predictor_abs_diff",
    "kernel_abs_diff",
    "G1_full_fro_over_sqrtn",
    "G1_full_operator_power",
    "G2_full_fro_over_sqrtn",
    "G2_full_operator_power",
    "G1_learned_fro_over_sqrtn",
    "G1_learned_operator_power",
    "G2_learned_fro_over_sqrtn",
    "G2_learned_operator_power",
)

JVP_METRICS = (
    "marked_r2_jvp_abs",
    "x2_jvp_l2n",
    "z3_jvp_l2n",
    "b3_jvp_l2n",
    "u_jvp_l2n",
    "A_jvp_l2n",
    "r2_bulk_jvp_l2n",
    "G1_learned_jvp_fro_over_sqrtn",
    "G1_learned_jvp_operator_power",
    "G2_learned_jvp_fro_over_sqrtn",
    "G2_learned_jvp_operator_power",
)

PRIMARY_BULK = (
    "x2_diff_l2n",
    "z3_diff_l2n",
    "b3_diff_l2n",
    "u_diff_l2n",
)

JVP_MATCH = {
    "marked_r2_abs": "marked_r2_jvp_abs",
    "x2_diff_l2n": "x2_jvp_l2n",
    "z3_diff_l2n": "z3_jvp_l2n",
    "b3_diff_l2n": "b3_jvp_l2n",
    "u_diff_l2n": "u_jvp_l2n",
}


def read_rows(directories, filename):
    rows = []
    for directory in directories:
        path = Path(directory) / filename
        if not path.exists():
            continue
        with path.open(newline="") as handle:
            for raw in csv.DictReader(handle):
                row = dict(raw)
                row["width"] = int(row["width"])
                row["trial"] = int(row["trial"])
                row["time"] = float(row["time"])
                if "direction" in row:
                    row["direction"] = int(row["direction"])
                rows.append(row)
    return rows


def rms(values):
    return math.sqrt(statistics.fmean(value * value for value in values))


def slope(widths, values):
    xs = [math.log(width) for width in widths]
    ys = [math.log(max(value, 1e-300)) for value in values]
    xbar = statistics.fmean(xs)
    ybar = statistics.fmean(ys)
    denominator = sum((value - xbar) ** 2 for value in xs)
    return sum(
        (x - xbar) * (y - ybar) for x, y in zip(xs, ys)
    ) / denominator


def scaling_summary(rows, metrics, kind):
    grouped = defaultdict(list)
    for row in rows:
        for metric in metrics:
            grouped[(row["time"], row["width"], metric)].append(float(row[metric]))
    times = sorted({row["time"] for row in rows})
    widths = sorted({row["width"] for row in rows})
    records = []
    for time in times:
        for metric in metrics:
            values = []
            if not all((time, width, metric) in grouped for width in widths):
                continue
            for width in widths:
                values.append(rms(grouped[(time, width, metric)]))
            records.append(
                {
                    "kind": kind,
                    "time": time,
                    "metric": metric,
                    "slope": slope(widths, values),
                    "widths": widths,
                    "rms_by_width": dict(zip(map(str, widths), values)),
                    "n_values_by_width": {
                        str(width): len(grouped[(time, width, metric)])
                        for width in widths
                    },
                }
            )
    return records


def index_scaling(records):
    return {
        (record["kind"], record["time"], record["metric"]): record
        for record in records
    }


def primary_decision(records):
    indexed = index_scaling(records)
    reasons = []
    fail_reasons = []
    for time in (0.25, 0.5):
        marked = indexed[("replacement", time, "marked_r2_abs")]
        if not (-0.25 <= marked["slope"] <= 0.25):
            reasons.append(
                f"marked slope at t={time} is {marked['slope']:.3f}, outside pass band"
            )
        if marked["slope"] > 0.25:
            fail_reasons.append(
                f"marked slope at t={time} is {marked['slope']:.3f} > 0.25"
            )
        for metric in PRIMARY_BULK:
            record = indexed[("replacement", time, metric)]
            values = record["rms_by_width"]
            if not (-0.8 <= record["slope"] <= -0.2):
                reasons.append(
                    f"{metric} slope at t={time} is {record['slope']:.3f}, outside pass band"
                )
            first = values[str(record["widths"][0])]
            last = values[str(record["widths"][-1])]
            if last > first:
                reasons.append(
                    f"{metric} RMS at t={time} increases from first to last width"
                )
            if record["slope"] > -0.2 and last >= 1.25 * first:
                fail_reasons.append(
                    f"{metric} meets preregistered bulk-amplification failure rule at t={time}"
                )

        for replacement_metric, jvp_metric in JVP_MATCH.items():
            replacement = indexed[("replacement", time, replacement_metric)]
            jvp = indexed.get(("jvp", time, jvp_metric))
            if jvp is None:
                reasons.append(f"missing JVP metric {jvp_metric} at t={time}")
                continue
            if abs(jvp["slope"] - replacement["slope"]) > 0.35:
                reasons.append(
                    f"JVP/replacement slope mismatch for {replacement_metric} at t={time}: "
                    f"{jvp['slope']:.3f} versus {replacement['slope']:.3f}"
                )
            if replacement_metric != "marked_r2_abs" and jvp["slope"] >= 0:
                reasons.append(
                    f"JVP bulk slope for {jvp_metric} at t={time} is nonnegative"
                )
            if replacement_metric == "marked_r2_abs" and not (
                -0.25 <= jvp["slope"] <= 0.25
            ):
                reasons.append(
                    f"marked JVP slope at t={time} is outside [-0.25,0.25]"
                )

    if fail_reasons:
        decision = "fail_if_numerical_controls_pass"
    elif reasons:
        decision = "inconclusive"
    else:
        decision = "pass_if_numerical_controls_pass"
    return {"decision": decision, "reasons": reasons, "fail_reasons": fail_reasons}


def exact_sanity(rows):
    time_zero = [row for row in rows if row["time"] == 0.0]
    exact_zero_fields = (
        "x2_diff_l2n",
        "u_diff_l2n",
        "A_diff_l2n",
        "G1_full_fro_over_sqrtn",
        "G1_learned_fro_over_sqrtn",
        "G2_learned_fro_over_sqrtn",
    )
    maximum = {
        metric: max(abs(float(row[metric])) for row in time_zero)
        for metric in exact_zero_fields
    }
    finite = all(row["all_finite"] == "True" for row in rows)
    envelope = max(
        max(float(row["base_envelope"]), float(row["perturbed_envelope"]))
        for row in rows
    )
    return {
        "time_zero_max_exact_zero_metrics": maximum,
        "all_finite": finite,
        "maximum_state_envelope": envelope,
        "pass": max(maximum.values()) == 0.0 and finite and envelope <= 100.0,
    }


def compare_resolution(primary, control, metrics, relative, absolute):
    primary_index = {
        (row["width"], row["trial"], row["time"]): row for row in primary
    }
    control_index = {
        (row["width"], row["trial"], row["time"]): row for row in control
    }
    comparisons = []
    for key in sorted(set(primary_index) & set(control_index)):
        p_row = primary_index[key]
        c_row = control_index[key]
        for metric in metrics:
            p = float(p_row[metric])
            c = float(c_row[metric])
            discrepancy = abs(c - p)
            threshold = max(relative * max(abs(p), abs(c)), absolute)
            comparisons.append(
                {
                    "width": key[0],
                    "trial": key[1],
                    "time": key[2],
                    "metric": metric,
                    "primary": p,
                    "control": c,
                    "absolute_discrepancy": discrepancy,
                    "threshold": threshold,
                    "pass": discrepancy <= threshold,
                }
            )
    nonzero = [item for item in comparisons if max(abs(item["primary"]), abs(item["control"])) > absolute]
    return {
        "comparisons": comparisons,
        "nonzero_count": len(nonzero),
        "nonzero_failures": sum(not item["pass"] for item in nonzero),
        "maximum_relative_discrepancy_nonzero": max(
            (
                item["absolute_discrepancy"]
                / max(abs(item["primary"]), abs(item["control"]))
                for item in nonzero
            ),
            default=0.0,
        ),
        "pass": all(item["pass"] for item in comparisons),
    }


def write_scaling_csv(path, records):
    fields = ("kind", "time", "metric", "slope", "rms_128", "rms_256", "rms_512", "rms_1024")
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for record in records:
            writer.writerow(
                {
                    "kind": record["kind"],
                    "time": record["time"],
                    "metric": record["metric"],
                    "slope": record["slope"],
                    **{
                        f"rms_{width}": record["rms_by_width"].get(str(width), "")
                        for width in (128, 256, 512, 1024)
                    },
                }
            )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--primary", nargs="+", required=True)
    parser.add_argument("--refined", nargs="*", default=[])
    parser.add_argument("--float64-coarse", nargs="*", default=[])
    parser.add_argument("--float64-fine", nargs="*", default=[])
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    primary_replacement = read_rows(args.primary, "raw_replacement.csv")
    primary_jvp = read_rows(args.primary, "raw_jvp.csv")
    scaling = scaling_summary(
        primary_replacement, REPLACEMENT_METRICS, "replacement"
    ) + scaling_summary(primary_jvp, JVP_METRICS, "jvp")
    decision = primary_decision(scaling)
    sanity = exact_sanity(primary_replacement)

    refined = read_rows(args.refined, "raw_replacement.csv")
    float64_coarse = read_rows(args.float64_coarse, "raw_replacement.csv")
    float64_fine = read_rows(args.float64_fine, "raw_replacement.csv")
    refinement_metrics = (
        "marked_r2_abs",
        "x2_diff_l2n",
        "z3_diff_l2n",
        "b3_diff_l2n",
        "u_diff_l2n",
        "A_diff_l2n",
        "r2_bulk_diff_l2n",
        "predictor_abs_diff",
        "kernel_abs_diff",
        "G1_learned_operator_power",
        "G2_learned_operator_power",
    )
    f32_refinement = compare_resolution(
        primary_replacement, refined, refinement_metrics, 0.05, 2e-6
    ) if refined else None
    f64_refinement = compare_resolution(
        float64_coarse, float64_fine, refinement_metrics, 0.05, 2e-9
    ) if float64_coarse and float64_fine else None

    controls_pass = sanity["pass"] and (
        f32_refinement is not None and f32_refinement["pass"]
    ) and (f64_refinement is not None and f64_refinement["pass"])
    final_decision = decision["decision"]
    if not controls_pass:
        final_decision = "inconclusive_numerical_validity"
    elif final_decision == "pass_if_numerical_controls_pass":
        final_decision = "pass_empirical_compatibility"
    elif final_decision == "fail_if_numerical_controls_pass":
        final_decision = "fail_cavity_hypothesis"

    result = {
        "claim_level": "empirical_only",
        "analysis_metadata": {
            "primary_directories": args.primary,
            "refined_directories": args.refined,
            "float64_coarse_directories": args.float64_coarse,
            "float64_fine_directories": args.float64_fine,
            "analyzer_sha256": hashlib.sha256(
                Path(__file__).resolve().read_bytes()
            ).hexdigest(),
        },
        "final_decision": final_decision,
        "scientific_decision_before_controls": decision,
        "exact_sanity": sanity,
        "float32_refinement": f32_refinement,
        "float64_refinement": f64_refinement,
        "scaling": scaling,
        "row_counts": {
            "primary_replacement": len(primary_replacement),
            "primary_jvp": len(primary_jvp),
            "refined_replacement": len(refined),
            "float64_coarse_replacement": len(float64_coarse),
            "float64_fine_replacement": len(float64_fine),
        },
    }
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    (output / "summary.json").write_text(json.dumps(result, indent=2) + "\n")
    write_scaling_csv(output / "width_scaling.csv", scaling)
    print(
        json.dumps(
            {
                "final_decision": final_decision,
                "scientific_decision": decision,
                "sanity": sanity,
                "float32_refinement_pass": None if f32_refinement is None else f32_refinement["pass"],
                "float64_refinement_pass": None if f64_refinement is None else f64_refinement["pass"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
