"""Cross-audits for the independently contracted fixed-depth B=1 recursion."""

from __future__ import annotations

from fractions import Fraction

import numpy as np

from ..compiler.l2_b1_correction import first_correction_normal_form
from ..compiler.normal_form import (
    PolynomialActivation,
    evaluate_polynomial,
    evaluate_quadrature,
)
from .gnf_audit_reference import evaluate_depth_b1_audit_recurrence
from .gnf_recursion import evaluate_depth_b1_gnf


def _polynomial(coefficients):
    polynomial = np.polynomial.Polynomial(coefficients)
    derivatives = [polynomial]
    for _ in range(3):
        derivatives.append(derivatives[-1].deriv())

    def oracle(order, x):
        return derivatives[order](x)

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


def _compare(q0, hidden_layers, oracle, *, order=80):
    """Compare the contracted scalar recursion to the four-Gaussian IR."""

    audit = evaluate_depth_b1_audit_recurrence(
        q0, hidden_layers, oracle, quadrature_order=order
    )
    full = evaluate_depth_b1_gnf(
        q0, hidden_layers, oracle, main_order=order
    )

    np.testing.assert_allclose(
        [
            audit.ntk,
            audit.straight_line,
            audit.hessian_square,
            audit.correction,
        ],
        [
            full.ntk,
            full.straight_third,
            full.hessian_square,
            full.correction,
        ],
        rtol=3.0e-11,
        atol=3.0e-11,
    )
    np.testing.assert_allclose(audit.q, full.q, rtol=3.0e-11, atol=3.0e-11)
    np.testing.assert_allclose(audit.d, full.d, rtol=3.0e-11, atol=3.0e-11)
    np.testing.assert_allclose(
        audit.reverse_variance,
        full.reverse_variances,
        rtol=3.0e-11,
        atol=3.0e-11,
    )
    np.testing.assert_allclose(
        audit.source_variance,
        full.source_variances,
        rtol=3.0e-11,
        atol=3.0e-11,
    )
    np.testing.assert_allclose(audit.beta, full.beta, rtol=3.0e-11, atol=3.0e-11)

    for layer, state in enumerate(full.layers, start=1):
        np.testing.assert_allclose(
            [audit.g11[layer], audit.g02[layer], audit.a3[layer]],
            [state.gram[1, 1], state.gram[0, 2], state.responses[3]],
            rtol=3.0e-11,
            atol=3.0e-11,
        )
        np.testing.assert_allclose(
            audit.chi[layer],
            full.source_variances[layer] + full.rho[layer],
            rtol=3.0e-11,
            atol=3.0e-11,
        )
        if layer == 1:
            expected_lambdas = [0.0, q0, 0.0, 0.0]
        else:
            expected_lambdas = [
                0.0,
                audit.theta[layer - 1],
                0.0,
                audit.a3[layer - 1] + 3.0 * audit.g02[layer - 1],
            ]
        np.testing.assert_allclose(
            state.lambdas,
            expected_lambdas,
            rtol=3.0e-11,
            atol=3.0e-11,
        )


def test_independent_contraction_matches_full_ir_through_h4() -> None:
    cases = (
        (0.0, _polynomial([1.0, 1.0])),
        (0.9, _polynomial([0.3, 1.0])),
        (0.7, _polynomial([0.0, 0.0, 1.0])),
        (0.2, _polynomial([0.0, 0.0, 0.0, 1.0])),
        (1.0, _sine),
        (0.9, _tanh),
    )
    for q0, oracle in cases:
        for hidden_layers in range(1, 5):
            _compare(q0, hidden_layers, oracle)


def test_independent_h2_contraction_matches_both_accepted_branches() -> None:
    accepted = first_correction_normal_form()
    for coefficients, q0 in (
        ([2], Fraction(7, 5)),
        ([0, 1], Fraction(7, 5)),
        ([1, 1], Fraction(4, 5)),
        ([0, 0, 1], Fraction(7, 10)),
        ([0, 0, 0, 1], Fraction(1, 2)),
    ):
        activation = PolynomialActivation(coefficients)
        result = evaluate_depth_b1_audit_recurrence(
            float(q0), 2, _polynomial(coefficients), quadrature_order=100
        )
        expected = [
            float(evaluate_polynomial(node, activation, {"q_0": q0}))
            for node in (
                accepted.ntk,
                accepted.straight_line_branch,
                accepted.hessian_branch,
                accepted.correction,
            )
        ]
        np.testing.assert_allclose(
            [
                result.ntk,
                result.straight_line,
                result.hessian_square,
                result.correction,
            ],
            expected,
            rtol=3.0e-12,
            atol=3.0e-8,
        )

    for q0, oracle, order in ((1.3, _sine, 48), (0.9, _tanh, 120)):
        result = evaluate_depth_b1_audit_recurrence(
            q0, 2, oracle, quadrature_order=order
        )
        expected = [
            evaluate_quadrature(node, oracle, {"q_0": q0}, order=order)
            for node in (
                accepted.ntk,
                accepted.straight_line_branch,
                accepted.hessian_branch,
                accepted.correction,
            )
        ]
        np.testing.assert_allclose(
            [
                result.ntk,
                result.straight_line,
                result.hessian_square,
                result.correction,
            ],
            expected,
            rtol=3.0e-11,
            atol=3.0e-11,
        )
