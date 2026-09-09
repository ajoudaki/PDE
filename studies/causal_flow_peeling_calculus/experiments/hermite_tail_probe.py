#!/usr/bin/env python3
"""Preregistered H1 probe: Hermite tails of arctan and its derivative."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np
from scipy.special import roots_hermitenorm


OUT = Path(__file__).resolve().parent / "outputs" / "hermite_tail"
ORDERS = (512, 1024, 2048)
K_MAX = 240
ABS_AGREE = 1e-13
REL_AGREE = 1e-6


def coefficients(quadrature_order: int, k_max: int) -> dict[str, np.ndarray]:
    nodes, weights = roots_hermitenorm(quadrature_order)
    weights = weights / math.sqrt(2.0 * math.pi)
    functions = {
        "arctan": np.arctan(nodes),
        "d": 1.0 / (1.0 + nodes * nodes),
    }
    result = {name: np.empty(k_max + 1) for name in functions}

    h_prev = np.ones_like(nodes)
    for name, values in functions.items():
        result[name][0] = np.dot(weights, values * h_prev)
    if k_max == 0:
        return result

    h_curr = nodes.copy()
    for name, values in functions.items():
        result[name][1] = np.dot(weights, values * h_curr)

    for k in range(1, k_max):
        h_next = (nodes * h_curr - math.sqrt(k) * h_prev) / math.sqrt(k + 1)
        for name, values in functions.items():
            result[name][k + 1] = np.dot(weights, values * h_next)
        h_prev, h_curr = h_curr, h_next
    return result


def reliable_mask(values_a: np.ndarray, values_b: np.ndarray, parity: int) -> np.ndarray:
    scale = np.maximum(np.maximum(np.abs(values_a), np.abs(values_b)), 1e-300)
    agree = (np.abs(values_a - values_b) <= ABS_AGREE) | (
        np.abs(values_a - values_b) / scale <= REL_AGREE
    )
    k = np.arange(values_a.size)
    correct_parity = (k % 2) == parity
    above_floor = np.maximum(np.abs(values_a), np.abs(values_b)) >= 3e-14
    return agree & correct_parity & above_floor


def regression(k: np.ndarray, log_abs_c: np.ndarray, model: str) -> dict[str, object]:
    if model == "root":
        design = np.column_stack([np.ones_like(k), np.sqrt(k), np.log(k)])
    elif model == "linear":
        design = np.column_stack([np.ones_like(k), k, np.log(k)])
    else:
        raise ValueError(model)
    coef, *_ = np.linalg.lstsq(design, log_abs_c, rcond=None)
    pred = design @ coef
    rmse = float(np.sqrt(np.mean((pred - log_abs_c) ** 2)))
    return {"coefficients": coef.tolist(), "rmse": rmse}


def fit_with_holdout(k: np.ndarray, c: np.ndarray) -> dict[str, object]:
    order = np.argsort(k)
    k = k[order]
    y = np.log(np.abs(c[order]))
    split = max(4, len(k) // 2)
    k_fit, y_fit = k[:split], y[:split]
    k_val, y_val = k[split:], y[split:]
    report: dict[str, object] = {
        "fit_k": [int(k_fit[0]), int(k_fit[-1])],
        "validation_k": [int(k_val[0]), int(k_val[-1])] if len(k_val) else None,
    }
    for model in ("root", "linear"):
        fit = regression(k_fit, y_fit, model)
        coef = np.asarray(fit["coefficients"])
        if model == "root":
            val_design = np.column_stack(
                [np.ones_like(k_val), np.sqrt(k_val), np.log(k_val)]
            )
        else:
            val_design = np.column_stack([np.ones_like(k_val), k_val, np.log(k_val)])
        validation_rmse = (
            float(np.sqrt(np.mean((val_design @ coef - y_val) ** 2)))
            if len(k_val)
            else None
        )
        report[model] = {**fit, "validation_rmse": validation_rmse}
    return report


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    all_values = {order: coefficients(order, K_MAX) for order in ORDERS}

    with (OUT / "coefficients.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["function", "k", *[f"q{q}" for q in ORDERS]])
        for name in ("arctan", "d"):
            for k in range(K_MAX + 1):
                writer.writerow(
                    [name, k, *[f"{all_values[q][name][k]:.18e}" for q in ORDERS]]
                )

    q_a, q_b = ORDERS[-2:]
    summary: dict[str, object] = {
        "quadrature_orders": list(ORDERS),
        "k_max": K_MAX,
        "agreement": {"absolute": ABS_AGREE, "relative": REL_AGREE},
    }
    for name, parity in (("arctan", 1), ("d", 0)):
        a = all_values[q_a][name]
        b = all_values[q_b][name]
        mask = reliable_mask(a, b, parity)
        reliable_k = np.flatnonzero(mask)
        # Exclude the first few modes; the question concerns asymptotic decay.
        reliable_k = reliable_k[reliable_k >= 9]
        summary[name] = {
            "reliable_count": int(len(reliable_k)),
            "reliable_k_min": int(reliable_k[0]) if len(reliable_k) else None,
            "reliable_k_max": int(reliable_k[-1]) if len(reliable_k) else None,
            "parity_leak_max": float(
                np.max(np.abs(b[np.arange(K_MAX + 1) % 2 != parity]))
            ),
            "fits": fit_with_holdout(reliable_k, b[reliable_k])
            if len(reliable_k) >= 10
            else None,
        }

    (OUT / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
