"""Seedwise equality of two independent exact finite-width encodings."""

from __future__ import annotations

import numpy as np

from .finite_width_contraction import third_derivative_contraction
from .finite_width_jet import feature_jet


def polynomial_oracle(coefficients):
    coefficients = tuple(float(value) for value in coefficients)

    def derivative(order, x):
        values = list(coefficients)
        for _ in range(order):
            values = [k * values[k] for k in range(1, len(values))]
        out = np.zeros_like(x, dtype=np.float64)
        for coefficient in reversed(values):
            out = out * x + coefficient
        return out

    return derivative


def sine_derivative(order, x):
    return (np.sin(x), np.cos(x), -np.sin(x), -np.cos(x))[order % 4]


def tanh_derivative(order, x):
    t = np.tanh(x)
    return (
        t,
        1.0 - t * t,
        -2.0 * t * (1.0 - t * t),
        -2.0 * (1.0 - t * t) * (1.0 - 3.0 * t * t),
    )[order]


def test_direct_contraction_matches_feature_jet_seedwise() -> None:
    activations = {
        "linear": polynomial_oracle([0.0, 1.0]),
        "affine": polynomial_oracle([1.0, 1.0]),
        "quadratic": polynomial_oracle([0.0, 0.0, 1.0]),
        "cubic": polynomial_oracle([0.0, 0.0, 0.0, 1.0]),
        "sin": sine_derivative,
        "tanh": tanh_derivative,
    }
    for activation_name, oracle in activations.items():
        for width in (1, 2, 5, 9):
            for seed in (0, 3, 17):
                direct = third_derivative_contraction(width, 1.0, oracle, seed).value
                jet = feature_jet(width, 1.0, oracle, seed).derivatives[3]
                np.testing.assert_allclose(
                    direct,
                    jet,
                    rtol=2.0e-12,
                    atol=2.0e-10,
                    err_msg=(
                        f"equation (3.10) mismatch for {activation_name}, "
                        f"width={width}, seed={seed}"
                    ),
                )


def test_direct_contraction_respects_nonunit_input_metric() -> None:
    # The q0 powers in (3.2)--(3.10) are an independent normalization gate.
    for q0 in (0.25, 2.5):
        for oracle in (polynomial_oracle([1.0, 1.0]), sine_derivative, tanh_derivative):
            for width, seed in ((2, 5), (7, 11)):
                direct = third_derivative_contraction(width, q0, oracle, seed).value
                jet = feature_jet(width, q0, oracle, seed).derivatives[3]
                np.testing.assert_allclose(direct, jet, rtol=2.0e-12, atol=2.0e-10)
