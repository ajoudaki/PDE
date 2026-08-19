"""Execute the preregistered 7,700-network normalized-sine regression.

The population values are read only after the two-oracle gate has passed.
Each cell is checkpointed as an ``.npy`` vector so an interrupted run can be
resumed without changing seeds or selectively dropping observations.
"""

from __future__ import annotations

import json
from math import exp, sqrt
from pathlib import Path
import time

import numpy as np

from ...depth.model import DepthState
from ..common.finite_width_jet import feature_ascent_jet


HERE = Path(__file__).resolve().parent
COMMON = HERE.parent / "common"
ALLOCATIONS = {32: 1800, 64: 1200, 128: 600, 256: 250}
DEPTHS = (3, 4)
SEED_ORIGIN = 100_000_000
NORMALIZATION = sqrt((1.0 - exp(-2.0)) / 2.0)


def activation_derivative(order: int, x: np.ndarray) -> np.ndarray:
    phase = order % 4
    if phase == 0:
        value = np.sin(x)
    elif phase == 1:
        value = np.cos(x)
    elif phase == 2:
        value = -np.sin(x)
    else:
        value = -np.cos(x)
    return value / NORMALIZATION


def seed_for(cell: int, observation: int) -> int:
    return SEED_ORIGIN + 10_000 * cell + observation


def one_jet(depth: int, width: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    state = DepthState(
        rng.standard_normal((width, 1)),
        tuple(rng.standard_normal((width, width)) for _ in range(depth - 1)),
        rng.standard_normal(width),
    )
    return feature_ascent_jet(
        state,
        np.ones((1, 1), dtype=np.float64),
        np.ones(1, dtype=np.float64),
        activation_derivative,
        order=5,
    ).derivatives[[1, 3, 5]]


def collect_cell(depth: int, width: int, count: int, cell: int) -> np.ndarray:
    path = HERE / f"normalized_sine_H{depth}_n{width}.npy"
    if path.exists():
        old = np.load(path)
        if old.ndim != 2 or old.shape[1] != 3 or len(old) > count:
            raise RuntimeError(f"invalid checkpoint {path}: {old.shape}")
        values = [row for row in old]
    else:
        values = []
    started = time.monotonic()
    for index in range(len(values), count):
        value = one_jet(depth, width, seed_for(cell, index))
        if not np.all(np.isfinite(value)):
            # Preserve the nonfinite observation; downstream validity must turn
            # the whole result inconclusive rather than delete the seed.
            values.append(value)
            np.save(path, np.asarray(values, dtype=np.float64))
            break
        values.append(value)
        if (index + 1) % 50 == 0 or index + 1 == count:
            np.save(path, np.asarray(values, dtype=np.float64))
            elapsed = time.monotonic() - started
            print(
                f"H={depth} n={width}: {index + 1}/{count}; "
                f"current C mean={np.mean(np.asarray(values)[:, 2]):.12g}; "
                f"segment {elapsed:.1f}s",
                flush=True,
            )
    return np.asarray(values, dtype=np.float64)


def cell_summary(values: np.ndarray, depth: int, width: int, cell: int) -> dict:
    count = len(values)
    finite = bool(np.all(np.isfinite(values)))
    if not finite or count != ALLOCATIONS[width]:
        return {
            "depth": depth,
            "width": width,
            "count": count,
            "expected_count": ALLOCATIONS[width],
            "finite": finite,
            "valid": False,
            "seed_first": seed_for(cell, 0),
            "seed_last": seed_for(cell, max(count - 1, 0)),
        }
    c = values[:, 2]
    mean = float(np.mean(c))
    sample_variance = float(np.var(c, ddof=1))
    se = sqrt(sample_variance / count)
    batch_records = []
    heavy_tail_pass = True
    for indices in np.array_split(np.arange(count), 4):
        batch = c[indices]
        batch_mean = float(np.mean(batch))
        batch_se = sqrt(float(np.var(batch, ddof=1)) / len(batch))
        deviation = abs(batch_mean - mean)
        passed = bool(deviation <= 5.0 * batch_se)
        heavy_tail_pass &= passed
        batch_records.append(
            {
                "count": len(batch),
                "mean": batch_mean,
                "standard_error": batch_se,
                "absolute_deviation_from_cell_mean": deviation,
                "five_standard_errors": 5.0 * batch_se,
                "pass": passed,
            }
        )
    return {
        "depth": depth,
        "width": width,
        "count": count,
        "expected_count": ALLOCATIONS[width],
        "finite": True,
        "means_A_B_C": [float(value) for value in np.mean(values, axis=0)],
        "C_sample_variance": sample_variance,
        "C_standard_error": se,
        "heavy_tail_batch_gate": heavy_tail_pass,
        "batches": batch_records,
        "valid": bool(np.isfinite(se) and se > 0 and heavy_tail_pass),
        "seed_first": seed_for(cell, 0),
        "seed_last": seed_for(cell, count - 1),
    }


def fit_depth(cells: list[dict], prediction: float) -> dict:
    if not all(record["valid"] for record in cells):
        return {"valid": False, "reason": "at least one cell failed a validity gate"}
    x = np.asarray([[1.0, 1.0 / record["width"]] for record in cells])
    y = np.asarray([record["means_A_B_C"][2] for record in cells])
    se = np.asarray([record["C_standard_error"] for record in cells])
    precision = 1.0 / se**2
    normal = x.T @ (precision[:, None] * x)
    covariance = np.linalg.inv(normal)
    coefficients = covariance @ (x.T @ (precision * y))
    residual = y - x @ coefficients
    chi_square = float(np.sum((residual / se) ** 2))
    degrees_of_freedom = len(cells) - 2
    # There are four widths, hence df=2; chi-square_2 survival is exp(-x/2).
    if degrees_of_freedom != 2:
        raise AssertionError(degrees_of_freedom)
    p_value = exp(-chi_square / 2.0)
    intercept_se = sqrt(float(covariance[0, 0]))
    z = (float(coefficients[0]) - prediction) / intercept_se
    fit_valid = bool(p_value >= 0.01 and np.isfinite(z))
    return {
        "valid": fit_valid,
        "intercept": float(coefficients[0]),
        "slope": float(coefficients[1]),
        "intercept_standard_error": intercept_se,
        "population_prediction": prediction,
        "z": z,
        "chi_square": chi_square,
        "degrees_of_freedom": degrees_of_freedom,
        "chi_square_p_value": p_value,
        "fit_validity_threshold": 0.01,
        "residuals": [float(value) for value in residual],
    }


def main() -> None:
    gate = json.loads((HERE / "TWO_ORACLE_GATE.json").read_text())
    if not gate["pass"]:
        raise RuntimeError("two-oracle gate did not pass")
    prediction_payload = json.loads(
        (COMMON / "NORMALIZED_SINE_FROZEN_PREDICTION.json").read_text()
    )
    predictions = {
        depth: float(prediction_payload["96"]["depths"][str(depth)]["C"])
        for depth in DEPTHS
    }
    summaries: dict[int, list[dict]] = {depth: [] for depth in DEPTHS}
    cell = 0
    for depth in DEPTHS:
        for width, count in ALLOCATIONS.items():
            values = collect_cell(depth, width, count, cell)
            summaries[depth].append(cell_summary(values, depth, width, cell))
            cell += 1
    fits = {depth: fit_depth(summaries[depth], predictions[depth]) for depth in DEPTHS}
    all_valid = all(fits[depth].get("valid", False) for depth in DEPTHS)
    if all_valid and all(abs(fits[depth]["z"]) <= 3.0 for depth in DEPTHS):
        decision = "pass"
    elif all_valid and any(abs(fits[depth]["z"]) > 5.0 for depth in DEPTHS):
        decision = "fail"
    else:
        decision = "inconclusive"
    output = {
        "contract": "../common/NONPOLYNOMIAL_EXPERIMENT_CONTRACT.md",
        "validity_addendum": "NONPOLYNOMIAL_VALIDITY_ADDENDUM.md",
        "two_oracle_gate": "TWO_ORACLE_GATE.json",
        "activation": "sin(x)/sqrt((1-exp(-2))/2)",
        "Q0": 1,
        "allocations_per_depth": {str(k): v for k, v in ALLOCATIONS.items()},
        "total_networks": sum(ALLOCATIONS.values()) * len(DEPTHS),
        "cells": {str(depth): summaries[depth] for depth in DEPTHS},
        "fits": {str(depth): fits[depth] for depth in DEPTHS},
        "decision": decision,
        "interpretation": (
            "Empirical discriminator only; it neither proves the equality-partition "
            "algebra nor the annealed large-width theorem."
        ),
    }
    path = HERE / "NORMALIZED_SINE_EXPERIMENT.json"
    path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"decision": decision, "fits": output["fits"]}, indent=2))


if __name__ == "__main__":
    main()
