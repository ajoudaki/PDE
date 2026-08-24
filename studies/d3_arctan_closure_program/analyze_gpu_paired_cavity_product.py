#!/usr/bin/env python3
"""Analyze the preregistered genuine paired-cavity product experiment."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


WIDTHS = (128, 256, 512, 1024, 2048)
HORIZONS = (1.0, 2.0, 4.0)
MOMENTS = (2, 4, 6, 8)


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
        n: load(args.input_dir / f"paired_product_main_h001_fp32_n{n}.npz")
        for n in WIDTHS
    }
    rng = np.random.default_rng(2026082318)
    results = {
        "main": {},
        "mesh_audit": {},
        "arithmetic_audit": {},
        "cavity_zero_max": {},
    }
    all_main_pass = True
    against_cells = []
    for horizon in HORIZONS:
        hk = hkey(horizon)
        for q in MOMENTS:
            key = f"s{hk}_j{q}"
            medians = np.asarray([
                np.median(main_data[n][key]) for n in WIDTHS
            ])
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
            ratio = float(medians[-1] / medians[1])
            cell_pass = central <= 0.08 and hi <= 0.15 and ratio <= 1.60
            all_main_pass = all_main_pass and cell_pass
            if q >= 4 and horizon in (2.0, 4.0) and lo > 0.15 and ratio > 1.60:
                against_cells.append((q, horizon))
            results["main"][f"s{horizon}_q{q}"] = {
                "medians": {
                    str(n): float(v) for n, v in zip(WIDTHS, medians)
                },
                "slope": central,
                "slope_ci95": [float(lo), float(hi)],
                "ratio_2048_over_256": ratio,
                "cell_pass": bool(cell_pass),
            }

    mesh_pass = True
    for n in (256, 512):
        coarse = load(
            args.input_dir / f"paired_product_audit_h001_fp32_n{n}.npz"
        )
        fine = load(
            args.input_dir / f"paired_product_audit_h0005_fp32_n{n}.npz"
        )
        for horizon in HORIZONS:
            hk = hkey(horizon)
            for q in MOMENTS:
                key = f"s{hk}_j{q}"
                discrepancy = float(np.median(symrel(coarse[key], fine[key])))
                cell_pass = discrepancy <= 0.08
                mesh_pass = mesh_pass and cell_pass
                results["mesh_audit"][f"n{n}_s{horizon}_q{q}"] = {
                    "median_symmetric_relative": discrepancy,
                    "cell_pass": bool(cell_pass),
                }

    arithmetic_pass = True
    for n in (128, 256):
        fp32 = load(
            args.input_dir
            / f"paired_product_audit_h001_fp32draw64_n{n}.npz"
        )
        fp64 = load(
            args.input_dir / f"paired_product_audit_h001_fp64_n{n}.npz"
        )
        for horizon in HORIZONS:
            hk = hkey(horizon)
            for q in MOMENTS:
                key = f"s{hk}_j{q}"
                discrepancy = float(np.median(symrel(fp32[key], fp64[key])))
                cell_pass = discrepancy <= 0.08
                arithmetic_pass = arithmetic_pass and cell_pass
                results["arithmetic_audit"][f"n{n}_s{horizon}_q{q}"] = {
                    "median_symmetric_relative": discrepancy,
                    "cell_pass": bool(cell_pass),
                }

    zero_pass = True
    for label, dataset in [
        *[(f"main_n{n}", main_data[n]) for n in WIDTHS],
        (
            "mesh_fine_n256",
            load(args.input_dir / "paired_product_audit_h0005_fp32_n256.npz"),
        ),
        (
            "mesh_fine_n512",
            load(args.input_dir / "paired_product_audit_h0005_fp32_n512.npz"),
        ),
        (
            "float64_n128",
            load(args.input_dir / "paired_product_audit_h001_fp64_n128.npz"),
        ),
        (
            "float64_n256",
            load(args.input_dir / "paired_product_audit_h001_fp64_n256.npz"),
        ),
    ]:
        dtype = str(dataset["dtype"].item())
        threshold = 1e-10 if dtype == "float64" else 1e-5
        maximum = 0.0
        for horizon in HORIZONS:
            hk = hkey(horizon)
            maximum = max(
                maximum,
                float(np.max(dataset[f"s{hk}_cavity_zero_z"])),
                float(np.max(dataset[f"s{hk}_cavity_zero_r"])),
            )
        cell_pass = maximum <= threshold
        zero_pass = zero_pass and cell_pass
        results["cavity_zero_max"][label] = {
            "dtype": dtype,
            "maximum": maximum,
            "threshold": threshold,
            "cell_pass": bool(cell_pass),
        }

    support = all_main_pass and mesh_pass and arithmetic_pass and zero_pass
    evidence_against = (
        len({q for q, _ in against_cells}) > 0
        and all(
            (q, 2.0) in against_cells and (q, 4.0) in against_cells
            for q in {q for q, _ in against_cells}
        )
        and mesh_pass and arithmetic_pass and zero_pass
    )
    results["verdict"] = {
        "formal_empirical_support": bool(support),
        "formal_empirical_evidence_against": bool(evidence_against),
        "main_cells_pass": bool(all_main_pass),
        "mesh_audit_pass": bool(mesh_pass),
        "arithmetic_audit_pass": bool(arithmetic_pass),
        "cavity_zero_pass": bool(zero_pass),
        "against_cells": [[q, h] for q, h in against_cells],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(json.dumps(results["verdict"], sort_keys=True))


if __name__ == "__main__":
    main()
