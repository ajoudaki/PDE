#!/usr/bin/env python3
"""Analyze the preregistered forward-query characteristic-budget run."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


WIDTHS = (256, 512, 1024, 2048, 4096)
HORIZONS = (1.0, 2.0, 4.0)
MOMENTS = (2, 4, 6, 8)
LAMBDAS = (0.25, 0.5, 1.0)


def hkey(h):
    return str(h).replace(".", "p")


def load(path):
    return np.load(path, allow_pickle=False)


def slope(xs, ys):
    return float(np.polyfit(np.log(xs), np.log(ys), 1)[0])


def symrel(a, b):
    tiny = np.finfo(np.float64).tiny
    return 2.0 * np.abs(a - b) / np.maximum(np.abs(a) + np.abs(b), tiny)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--bootstrap", type=int, default=4000)
    args = parser.parse_args()
    main_data = {
        n: load(args.input_dir / f"forward_query_main_n{n}.npz")
        for n in WIDTHS
    }
    rng = np.random.default_rng(2026082330)
    results = {
        "main": {},
        "mesh_audit": {},
        "arithmetic_audit": {},
        "decomposition_residual": {},
        "ancillary": {},
    }
    primary_keys = []
    for horizon in HORIZONS:
        hk = hkey(horizon)
        for q in MOMENTS:
            primary_keys.append((horizon, f"s{hk}_full_q{q}", f"q{q}"))
        for lam in LAMBDAS:
            lk = str(lam).replace(".", "p")
            primary_keys.append(
                (horizon, f"s{hk}_full_lme{lk}", f"lme{lam}")
            )

    main_pass = True
    against = []
    for horizon, key, label in primary_keys:
        medians = np.asarray([np.median(main_data[n][key]) for n in WIDTHS])
        central = slope(np.asarray(WIDTHS), medians)
        boot = np.empty(args.bootstrap)
        for b in range(args.bootstrap):
            bmed = []
            for n in WIDTHS:
                values = main_data[n][key]
                sample = rng.choice(values, size=values.size, replace=True)
                bmed.append(np.median(sample))
            boot[b] = slope(np.asarray(WIDTHS), np.asarray(bmed))
        lo, hi = np.quantile(boot, (0.025, 0.975))
        ratio = float(medians[-1] / medians[0])
        cell_pass = central <= 0.08 and hi <= 0.15 and ratio <= 1.60
        main_pass = main_pass and cell_pass
        if label in ("lme0.5", "lme1.0") and horizon in (2.0, 4.0):
            if lo > 0.15 and ratio > 1.60:
                against.append((label, horizon))
        results["main"][f"s{horizon}_{label}"] = {
            "medians": {str(n): float(v) for n, v in zip(WIDTHS, medians)},
            "slope": central,
            "slope_ci95": [float(lo), float(hi)],
            "ratio_4096_over_256": ratio,
            "cell_pass": bool(cell_pass),
        }

    audit_keys = []
    for horizon in HORIZONS:
        hk = hkey(horizon)
        for q in MOMENTS:
            audit_keys.append(f"s{hk}_full_q{q}")
        for lam in LAMBDAS:
            lk = str(lam).replace(".", "p")
            audit_keys.append(f"s{hk}_full_lme{lk}")

    mesh_pass = True
    for n in (256, 512):
        coarse = load(args.input_dir / f"forward_query_audit_h001_n{n}.npz")
        fine = load(args.input_dir / f"forward_query_audit_h0005_n{n}.npz")
        for key in audit_keys:
            discrepancy = float(np.median(symrel(coarse[key], fine[key])))
            cell_pass = discrepancy <= 0.08
            mesh_pass = mesh_pass and cell_pass
            results["mesh_audit"][f"n{n}_{key}"] = {
                "median_symmetric_relative": discrepancy,
                "cell_pass": bool(cell_pass),
            }

    arithmetic_pass = True
    for n in (128, 256):
        fp32 = load(
            args.input_dir / f"forward_query_audit_fp32draw64_n{n}.npz"
        )
        fp64 = load(args.input_dir / f"forward_query_audit_fp64_n{n}.npz")
        for key in audit_keys:
            discrepancy = float(np.median(symrel(fp32[key], fp64[key])))
            cell_pass = discrepancy <= 0.08
            arithmetic_pass = arithmetic_pass and cell_pass
            results["arithmetic_audit"][f"n{n}_{key}"] = {
                "median_symmetric_relative": discrepancy,
                "cell_pass": bool(cell_pass),
            }

    residual_pass = True
    datasets = [
        *[(f"main_n{n}", main_data[n]) for n in WIDTHS],
        *[(
            f"mesh_fine_n{n}",
            load(args.input_dir / f"forward_query_audit_h0005_n{n}.npz"),
        ) for n in (256, 512)],
        *[(
            f"float64_n{n}",
            load(args.input_dir / f"forward_query_audit_fp64_n{n}.npz"),
        ) for n in (128, 256)],
    ]
    for label, dataset in datasets:
        dtype = str(dataset["dtype"].item())
        threshold = 1e-10 if dtype == "float64" else 1e-5
        maximum = max(
            float(np.max(dataset[f"s{hkey(h)}_decomposition_residual"]))
            for h in HORIZONS
        )
        cell_pass = maximum <= threshold
        residual_pass = residual_pass and cell_pass
        results["decomposition_residual"][label] = {
            "dtype": dtype,
            "maximum": maximum,
            "threshold": threshold,
            "cell_pass": bool(cell_pass),
        }

    for horizon in HORIZONS:
        hk = hkey(horizon)
        for label in ("full", "static", "learned"):
            for stat in ("quantile0p99", "quantile0p999", "max"):
                key = f"s{hk}_{label}_{stat}"
                results["ancillary"][f"s{horizon}_{label}_{stat}"] = {
                    str(n): float(np.median(main_data[n][key])) for n in WIDTHS
                }

    support = main_pass and mesh_pass and arithmetic_pass and residual_pass
    labels = {label for label, _ in against}
    evidence_against = (
        any((label, 2.0) in against and (label, 4.0) in against
            for label in labels)
        and mesh_pass and arithmetic_pass and residual_pass
    )
    results["verdict"] = {
        "formal_empirical_support": bool(support),
        "formal_empirical_evidence_against": bool(evidence_against),
        "main_cells_pass": bool(main_pass),
        "mesh_audit_pass": bool(mesh_pass),
        "arithmetic_audit_pass": bool(arithmetic_pass),
        "decomposition_residual_pass": bool(residual_pass),
        "against_cells": [[label, h] for label, h in against],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps(results["verdict"], sort_keys=True))


if __name__ == "__main__":
    main()
