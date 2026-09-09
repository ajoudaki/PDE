"""Deterministic gates for the fixed-depth one-sample Gaussian recursion."""

from __future__ import annotations

from math import pi, sqrt

import numpy as np
from numpy.polynomial.hermite import hermgauss

from ..compiler.l2_b1_correction import first_correction_normal_form
from ..compiler.normal_form import (
    PolynomialActivation,
    evaluate_polynomial,
    evaluate_quadrature,
)
from .gnf_recursion import evaluate_depth_b1_gnf


def _polynomial_oracle(activation: PolynomialActivation):
    def oracle(order, x):
        out = np.zeros_like(x, dtype=np.float64)
        for coefficient in reversed(activation.derivative(order)):
            out = out * x + float(coefficient)
        return out

    return oracle


def _sine(order, x):
    return (np.sin(x), np.cos(x), -np.sin(x), -np.cos(x))[order % 4]


def _tanh(order, x):
    t = np.tanh(x)
    return (
        t,
        1.0 - t * t,
        -2.0 * t * (1.0 - t * t),
        -2.0 * (1.0 - t * t) * (1.0 - 3.0 * t * t),
    )[order]


def _h1_formula(q0, oracle, order):
    nodes, weights = hermgauss(order)
    u = sqrt(2.0 * q0) * nodes
    weights = weights / sqrt(pi)
    p0, p1, p2, p3 = (oracle(k, u) for k in range(4))
    ntk = np.sum(weights * (p0 * p0 + q0 * p1 * p1))
    correction = np.sum(
        weights
        * (
            4.0 * q0**2 * p1**4
            + 4.0 * q0 * p0**2 * p1**2
            + 14.0 * q0**2 * p0 * p2 * p1**2
            + 12.0 * q0**3 * p2**2 * p1**2
            + 6.0 * q0**3 * p3 * p1**3
        )
    )
    return ntk, correction


def test_h1_matches_explicit_generic_formula() -> None:
    for q0, oracle, order in (
        (0.7, _polynomial_oracle(PolynomialActivation([0, 0, 1])), 24),
        (1.3, _sine, 48),
        (0.9, _tanh, 120),
    ):
        expected_a, expected_c = _h1_formula(q0, oracle, order)
        result = evaluate_depth_b1_gnf(q0, 1, oracle, main_order=order)
        np.testing.assert_allclose(result.ntk, expected_a, rtol=2e-13, atol=2e-13)
        np.testing.assert_allclose(
            result.correction, expected_c, rtol=2e-12, atol=2e-12
        )


def test_h2_matches_accepted_exact_polynomial_normal_form() -> None:
    accepted = first_correction_normal_form()
    for coefficients in ([0, 1], [1, 1], [0, 0, 1], [0, 0, 0, 1]):
        activation = PolynomialActivation(coefficients)
        result = evaluate_depth_b1_gnf(
            1.0, 2, _polynomial_oracle(activation), main_order=48
        )
        expected_a = float(evaluate_polynomial(accepted.ntk, activation, {"q_0": 1}))
        expected_c = float(
            evaluate_polynomial(accepted.correction, activation, {"q_0": 1})
        )
        np.testing.assert_allclose(result.ntk, expected_a, rtol=3e-13, atol=3e-13)
        np.testing.assert_allclose(
            result.correction, expected_c, rtol=4e-12, atol=4e-8
        )


def test_h2_matches_accepted_smooth_quadrature_normal_form() -> None:
    accepted = first_correction_normal_form()
    for oracle, order in ((_sine, 32), (_tanh, 120)):
        result = evaluate_depth_b1_gnf(1.0, 2, oracle, main_order=order)
        expected_a = evaluate_quadrature(
            accepted.ntk, oracle, {"q_0": 1.0}, order=order
        )
        expected_c = evaluate_quadrature(
            accepted.correction, oracle, {"q_0": 1.0}, order=order
        )
        np.testing.assert_allclose(result.ntk, expected_a, rtol=2e-12, atol=2e-12)
        np.testing.assert_allclose(
            result.correction, expected_c, rtol=2e-11, atol=2e-11
        )


def test_deep_linear_closed_form_through_h4() -> None:
    q0 = 0.7
    oracle = _polynomial_oracle(PolynomialActivation([0, 1]))
    for hidden_layers in range(1, 5):
        result = evaluate_depth_b1_gnf(
            q0, hidden_layers, oracle, main_order=10
        )
        expected_a = (hidden_layers + 1) * q0
        expected_c = (
            2.0
            / 3.0
            * hidden_layers
            * (hidden_layers + 1) ** 2
            * (hidden_layers + 2)
            * q0**2
        )
        np.testing.assert_allclose(result.ntk, expected_a, rtol=2e-13, atol=2e-13)
        np.testing.assert_allclose(
            result.straight_third, 0.0, rtol=0.0, atol=2e-11
        )
        np.testing.assert_allclose(
            result.correction, expected_c, rtol=3e-13, atol=3e-13
        )

