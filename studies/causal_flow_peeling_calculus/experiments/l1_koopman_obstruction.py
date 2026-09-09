#!/usr/bin/env python3
"""Preregistered K0 probe: Gaussian-seed obstruction to analytic time norms."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
import sys

import numpy as np
from scipy.special import gammaln, roots_hermitenorm


sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from studies._output_paths import StudyPaths

PATHS = StudyPaths(__file__)
K_MAX = 80
QUADRATURE_ORDERS = (256, 384)


def convolution_at(a: list[np.ndarray], b: list[np.ndarray], k: int) -> np.ndarray:
    return sum((a[i] * b[k - i] for i in range(k + 1)), start=np.zeros_like(a[0]))


def reciprocal_coefficient(
    denominator: list[np.ndarray], reciprocal: list[np.ndarray], k: int
) -> np.ndarray:
    if k == 0:
        return 1.0 / denominator[0]
    accumulated = sum(
        (denominator[i] * reciprocal[k - i] for i in range(1, k + 1)),
        start=np.zeros_like(denominator[0]),
    )
    return -accumulated / denominator[0]


def atan_coefficient(
    argument: list[np.ndarray], derivative_gate: list[np.ndarray], k: int
) -> np.ndarray:
    if k == 0:
        return np.arctan(argument[0])
    accumulated = sum(
        (derivative_gate[i] * (k - i) * argument[k - i] for i in range(k)),
        start=np.zeros_like(argument[0]),
    )
    return accumulated / k


def scalar_series(a0: np.ndarray, k_max: int) -> dict[str, object]:
    zero = np.zeros_like(a0)
    a = [a0.copy()]
    u = [zero.copy()]
    d: list[np.ndarray] = []
    x: list[np.ndarray] = []
    u_velocity: list[np.ndarray] = []
    denominator: list[np.ndarray] = []

    for k in range(k_max + 1):
        u_square = convolution_at(u, u, k)
        denominator.append(u_square + (1.0 if k == 0 else 0.0))
        d.append(reciprocal_coefficient(denominator, d, k))
        x.append(atan_coefficient(u, d, k))
        u_velocity.append(convolution_at(a, d, k))
        if k < k_max:
            a.append(x[k] / (k + 1))
            u.append(u_velocity[k] / (k + 1))

    f = [convolution_at(a, x, k) for k in range(k_max + 1)]
    x_square = [convolution_at(x, x, k) for k in range(k_max + 1)]
    velocity_square = [
        convolution_at(u_velocity, u_velocity, k) for k in range(k_max + 1)
    ]
    kernel = [x_square[k] + velocity_square[k] for k in range(k_max + 1)]
    gradient_residual = max(
        float(
            np.max(np.abs((k + 1) * f[k + 1] - kernel[k]))
            / (1.0 + np.max(np.abs(kernel[k])))
        )
        for k in range(k_max)
    )
    return {
        "a": a,
        "u": u,
        "d": d,
        "x": x,
        "u_velocity": u_velocity,
        "f": f,
        "kernel": kernel,
        "gradient_residual": gradient_residual,
    }


def inverse_leading_series(k_max: int) -> np.ndarray:
    # psi solves psi'=1/(1+psi^2), psi(0)=0.  The leading kernel is psi'^2.
    zero = np.zeros(1)
    psi = [zero.copy()]
    d: list[np.ndarray] = []
    denominator: list[np.ndarray] = []
    for k in range(k_max + 1):
        psi_square = convolution_at(psi, psi, k)
        denominator.append(psi_square + (1.0 if k == 0 else 0.0))
        d.append(reciprocal_coefficient(denominator, d, k))
        if k < k_max:
            psi.append(d[k] / (k + 1))
    return np.array([float(convolution_at(d, d, k)[0]) for k in range(k_max + 1)])


def normalized_hermite(nodes: np.ndarray, k_max: int) -> list[np.ndarray]:
    values = [np.ones_like(nodes), nodes.copy()]
    for k in range(1, k_max):
        values.append(
            (nodes * values[k] - math.sqrt(k) * values[k - 1]) / math.sqrt(k + 1)
        )
    return values[: k_max + 1]


def run_quadrature(order: int, leading: np.ndarray) -> dict[str, object]:
    nodes, weights = roots_hermitenorm(order)
    weights = weights / math.sqrt(2.0 * math.pi)
    jet = scalar_series(nodes, K_MAX)
    hermite = normalized_hermite(nodes, K_MAX + 2)
    signed = np.empty(K_MAX + 1)
    l2 = np.empty(K_MAX + 1)
    extracted_leading = np.empty(K_MAX + 1)
    for k, coefficient in enumerate(jet["kernel"]):
        signed[k] = np.dot(weights, coefficient)
        l2[k] = math.sqrt(max(0.0, np.dot(weights, coefficient * coefficient)))
        projection = np.dot(weights, coefficient * hermite[k + 2])
        extracted_leading[k] = projection * math.exp(-0.5 * gammaln(k + 3))
    return {
        "signed": signed,
        "l2": l2,
        "extracted_leading": extracted_leading,
        "leading": leading,
        "gradient_residual": jet["gradient_residual"],
    }


def positive_root(value: float, k: int) -> float:
    if k == 0 or value == 0.0:
        return 0.0
    return float(abs(value) ** (1.0 / k))


def main() -> None:
    OUT = PATHS.parse(output_relative="experiments/outputs/l1_koopman_obstruction_v2").output_dir
    OUT.mkdir(parents=True, exist_ok=True)
    leading = inverse_leading_series(K_MAX)
    results = {order: run_quadrature(order, leading) for order in QUADRATURE_ORDERS}

    with (OUT / "coefficients.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "k",
                "leading_inverse_series",
                *[
                    field
                    for order in QUADRATURE_ORDERS
                    for field in (
                        f"signed_q{order}",
                        f"l2_q{order}",
                        f"extracted_leading_q{order}",
                    )
                ],
            ]
        )
        for k in range(K_MAX + 1):
            row: list[object] = [k, f"{leading[k]:.18e}"]
            for order in QUADRATURE_ORDERS:
                row.extend(
                    [
                        f"{results[order]['signed'][k]:.18e}",
                        f"{results[order]['l2'][k]:.18e}",
                        f"{results[order]['extracted_leading'][k]:.18e}",
                    ]
                )
            writer.writerow(row)

    high = results[QUADRATURE_ORDERS[-1]]
    selected = {}
    for k in range(10, K_MAX + 1, 10):
        selected[str(k)] = {
            "signed_root": positive_root(float(high["signed"][k]), k),
            "l2_root": positive_root(float(high["l2"][k]), k),
            "leading_root": positive_root(float(leading[k]), k),
            "leading_relative_error": float(
                abs(high["extracted_leading"][k] - leading[k])
                / max(abs(leading[k]), 1e-300)
            ),
        }

    low, high_order = QUADRATURE_ORDERS
    reliable = []
    for k in range(K_MAX + 1):
        values = (results[low]["l2"][k], results[high_order]["l2"][k])
        scale = max(abs(values[0]), abs(values[1]), 1e-300)
        if all(np.isfinite(value) for value in values) and abs(values[0] - values[1]) / scale < 1e-8:
            reliable.append(k)

    report = {
        "k_max": K_MAX,
        "quadrature_orders": list(QUADRATURE_ORDERS),
        "gradient_identity_residuals": {
            str(order): results[order]["gradient_residual"]
            for order in QUADRATURE_ORDERS
        },
        "largest_l2_agreement_order": max(reliable),
        "selected_even_orders": selected,
    }
    (OUT / "summary.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
