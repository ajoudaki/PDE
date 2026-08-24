#!/usr/bin/env python3
"""Analyze the frozen causal susceptibility-trace experiment."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


WIDTHS = (128, 256, 512)
HORIZONS = (1, 2, 4)


def load(path: Path):
    return np.load(path, allow_pickle=False)


def main_path(root: Path, n: int, horizon: int):
    return root / f"susceptibility_main_n{n}_h0.02_T{horizon}.npz"


def interval(x):
    return [float(np.quantile(x, 0.025)), float(np.quantile(x, 0.975))]


def bootstrap_slope(groups, x, rng, draws=20000):
    slopes = np.empty(draws)
    for b in range(draws):
        med = []
        for values in groups:
            sample = values[rng.integers(0, len(values), len(values))]
            med.append(np.median(sample))
        slopes[b] = np.polyfit(x, np.log(np.maximum(med, 1.0e-30)), 1)[0]
    point = np.polyfit(x, np.log([np.median(g) for g in groups]), 1)[0]
    return float(point), interval(slopes)


def finite_difference_audit(datasets):
    records = []
    passed = True
    for name, z in datasets:
        raw = str(z["fd_json"].item())
        for orbit, items in enumerate(json.loads(raw)):
            for item in items:
                scale = max(abs(item["ad"]), abs(item["fd"]))
                tolerance = max(5.0e-4, 0.05 * scale)
                ok = item["abs_error"] <= tolerance
                passed = passed and ok
                records.append({"dataset": name, "orbit": orbit,
                                **item, "tolerance": tolerance, "pass": ok})
    return passed, records


def arithmetic_audit(root: Path):
    p32 = root / "susceptibility_arithmetic32_n128_h0.02_T4.npz"
    p64 = root / "susceptibility_arithmetic64_n128_h0.02_T4.npz"
    z32, z64 = load(p32), load(p64)
    metrics = {}
    passed = True
    for key in ("tv", "signed", "positive", "negative", "last_rate"):
        a, b = z32[key], z64[key]
        rel = np.abs(a - b) / np.maximum(np.maximum(np.abs(a), np.abs(b)),
                                         1.0e-8)
        metrics[key] = {"max_relative": float(np.max(rel)),
                        "median_relative": float(np.median(rel))}
        passed = passed and bool(np.max(rel) <= 0.05 or np.max(np.abs(a-b)) <= 5e-4)
    a, b = z32["kappa"], z64["kappa"]
    rmse = np.sqrt(np.mean((a-b)**2, axis=1))
    scale = np.sqrt(np.mean(b**2, axis=1))
    rel = rmse / np.maximum(scale, 1.0e-10)
    metrics["kappa_rmse"] = {"max_relative": float(np.max(rel)),
                              "median_relative": float(np.median(rel))}
    passed = passed and bool(np.max(rel) <= 0.05)
    return passed, metrics


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--json-output", type=Path, required=True)
    parser.add_argument("--md-output", type=Path, required=True)
    args = parser.parse_args()
    root = args.input_dir
    rng = np.random.default_rng(2026082312)

    main_data = {(T, n): load(main_path(root, n, T))
                 for T in HORIZONS for n in WIDTHS}
    extra_t4 = {
        n: load(root / f"susceptibility_main_extra_n{n}_h0.02_T4.npz")
        for n in WIDTHS
    }

    def values(T, n, field):
        base = main_data[T, n][field]
        if T == 4:
            return np.concatenate([base, extra_t4[n][field]], axis=0)
        return base

    summaries = {}
    width_slopes = {}
    half_values = []
    all_coefficients = []
    for T in HORIZONS:
        for n in WIDTHS:
            key = f"T{T}_n{n}"
            summaries[key] = {
                field: float(np.median(values(T, n, field)))
                for field in ("tv", "signed", "positive", "negative",
                              "half_rel_tv", "last_rate", "max_rate")
            }
            half_values.extend(values(T, n, "half_rel_tv").tolist())
            all_coefficients.append(values(T, n, "kappa").ravel())
        groups = [values(T, n, "tv") for n in WIDTHS]
        point, ci = bootstrap_slope(groups, np.log(np.asarray(WIDTHS)), rng)
        width_slopes[f"T{T}"] = {"point": point, "ci95": ci}

    mesh_files = [
        root / "susceptibility_main_n128_h0.02_T4.npz",
        root / "susceptibility_refine_n128_h0.01_T4.npz",
        root / "susceptibility_fine_n128_h0.005_T4.npz",
    ]
    mesh_data = [load(p) for p in mesh_files]
    mesh_groups = [values(4, 128, "tv"), mesh_data[1]["tv"],
                   mesh_data[2]["tv"]]
    mesh_x = np.log(1.0 / np.asarray([0.02, 0.01, 0.005]))
    mesh_point, mesh_ci = bootstrap_slope(mesh_groups, mesh_x, rng)

    fd_sets = []
    for n in WIDTHS:
        fd_sets.append((f"main_T4_n{n}", main_data[4, n]))
    fd_sets.extend([
        ("refine_n128", mesh_data[1]),
        ("fine_n128", mesh_data[2]),
        ("refine_n256", load(root / "susceptibility_refine_n256_h0.01_T4.npz")),
    ])
    fd_pass, fd_records = finite_difference_audit(fd_sets)
    arithmetic_pass, arithmetic = arithmetic_audit(root)

    coeff = np.concatenate(all_coefficients)
    half_values = np.asarray(half_values)
    half_summary = {
        "median": float(np.median(half_values)),
        "p95": float(np.quantile(half_values, 0.95)),
    }
    sign_summary = {
        "negative_coefficient_fraction": float(np.mean(coeff < 0)),
        "minimum_coefficient": float(np.min(coeff)),
        "maximum_coefficient": float(np.max(coeff)),
    }
    numerical_valid = bool(fd_pass and arithmetic_pass)
    formal_support = bool(
        numerical_valid
        and width_slopes["T2"]["ci95"][1] < 0.15
        and width_slopes["T4"]["ci95"][1] < 0.15
        and mesh_ci[1] < 0.20
        and half_summary["median"] < 0.15
        and half_summary["p95"] < 0.35
    )
    formal_evidence_against = bool(
        numerical_valid and (
            width_slopes["T2"]["ci95"][0] > 0.25
            or width_slopes["T4"]["ci95"][0] > 0.25
            or mesh_ci[0] > 0.35
        )
    )
    result = {
        "summaries": summaries,
        "width_slopes": width_slopes,
        "mesh_divergence_exponent_n128_T4": {
            "point": mesh_point, "ci95": mesh_ci,
        },
        "half_probe": half_summary,
        "sign": sign_summary,
        "finite_difference_pass": fd_pass,
        "finite_difference_records": fd_records,
        "arithmetic_pass": arithmetic_pass,
        "arithmetic": arithmetic,
        "numerical_valid": numerical_valid,
        "formal_support": formal_support,
        "formal_evidence_against": formal_evidence_against,
        "claim_boundary": "Empirical diagnostic only; no theorem rung is promoted.",
    }
    args.json_output.write_text(json.dumps(result, indent=2) + "\n")

    lines = [
        "# GPU causal susceptibility-trace results",
        "",
        f"- Numerical audits valid: **{numerical_valid}**.",
        f"- Frozen formal-support rule: **{formal_support}**.",
        f"- Frozen evidence-against rule: **{formal_evidence_against}**.",
        "- These are empirical statements only; C3--C5 remain proof obligations.",
        "",
        "## Main medians",
        "",
        "| horizon | width | TV | signed | negative TV | half-probe discrepancy |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for T in HORIZONS:
        for n in WIDTHS:
            s = summaries[f"T{T}_n{n}"]
            lines.append(f"| {T} | {n} | {s['tv']:.6g} | {s['signed']:.6g} | "
                         f"{s['negative']:.6g} | {s['half_rel_tv']:.4g} |")
    lines.extend(["", "## Frozen fits", ""])
    for T in HORIZONS:
        s = width_slopes[f"T{T}"]
        lines.append(f"- T={T} width slope: {s['point']:.4f}, "
                     f"95% CI [{s['ci95'][0]:.4f}, {s['ci95'][1]:.4f}].")
    lines.append(f"- T=4, n=128 mesh-divergence exponent: {mesh_point:.4f}, "
                 f"95% CI [{mesh_ci[0]:.4f}, {mesh_ci[1]:.4f}].")
    lines.append(f"- Pooled half-probe discrepancy: median {half_summary['median']:.4f}, "
                 f"95th percentile {half_summary['p95']:.4f}.")
    lines.extend(["", "## Mechanism diagnostic", "",
                  f"Across all main orbit/time coefficients, the negative fraction was "
                  f"{sign_summary['negative_coefficient_fraction']:.6g}; the observed range was "
                  f"[{sign_summary['minimum_coefficient']:.6g}, "
                  f"{sign_summary['maximum_coefficient']:.6g}].  This motivates, but does not "
                  "establish, a positivity/passivity proof search.", ""])
    args.md_output.write_text("\n".join(lines))
    print(json.dumps({k: result[k] for k in
                      ("numerical_valid", "formal_support",
                       "formal_evidence_against")}, indent=2))


if __name__ == "__main__":
    main()
