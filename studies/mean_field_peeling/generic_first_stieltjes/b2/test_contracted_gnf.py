"""Exact, width-limit tests for the contracted polynomial GNF reference."""

from __future__ import annotations

from fractions import Fraction

from .contracted_gnf_polynomial_reference import evaluate_contracted_directional_gnf
from ..compiler.l2_b1_correction import first_correction_normal_form
from ..compiler.normal_form import PolynomialActivation, evaluate_polynomial


def test_constant_and_linear_controls_for_arbitrary_geometry() -> None:
    q0 = [[1, Fraction(1, 3)], [Fraction(1, 3), 2]]
    c = [Fraction(2, 3), Fraction(-1, 4)]

    constant = evaluate_contracted_directional_gnf(
        q0, c, PolynomialActivation([1])
    )
    assert constant.ntk == sum(c) ** 2
    assert constant.correction == 0

    linear = evaluate_contracted_directional_gnf(
        q0, c, PolynomialActivation([0, 1])
    )
    q_eff = sum(c[a] * q0[a][b] * c[b] for a in range(2) for b in range(2))
    assert linear.ntk == 3 * q_eff
    assert linear.correction == 48 * q_eff**2


def test_quadratic_matches_accepted_two_input_campaign() -> None:
    activation = PolynomialActivation([0, 0, 1])
    for theta in (Fraction(-1, 2), Fraction(0), Fraction(1, 2), Fraction(1)):
        t = theta**2
        q0 = [[1, theta], [theta, 1]]
        plus = evaluate_contracted_directional_gnf(
            q0, [Fraction(1, 2), Fraction(1, 2)], activation
        )
        minus = evaluate_contracted_directional_gnf(
            q0, [Fraction(1, 2), Fraction(-1, 2)], activation
        )
        assert plus.ntk == 63 + 20 * t + 28 * t**2
        assert plus.correction == (
            279680
            + 423312 * t
            + 788336 * t**2
            + 143232 * t**3
            + 50624 * t**4
        )
        assert minus.ntk == 48 - 20 * t - 28 * t**2
        assert minus.correction == (
            168192
            - 91904 * t
            - 270144 * t**2
            + 143232 * t**3
            + 50624 * t**4
        )


def test_single_active_channel_reduces_to_b1_gnf_exactly() -> None:
    q = Fraction(3, 2)
    q0 = [[q, Fraction(1, 4)], [Fraction(1, 4), Fraction(5, 4)]]
    for coefficients in ([0, 1], [1, 1], [0, 0, 1], [0, 0, 0, 1]):
        activation = PolynomialActivation(coefficients)
        b2 = evaluate_contracted_directional_gnf(q0, [1, 0], activation)
        b1 = first_correction_normal_form(q)
        assert b2.ntk == evaluate_polynomial(b1.ntk, activation, {})
        assert b2.correction == evaluate_polynomial(b1.correction, activation, {})


def test_exact_channel_homogeneity() -> None:
    q0 = [[1, Fraction(-1, 5)], [Fraction(-1, 5), Fraction(4, 3)]]
    c = [Fraction(2, 7), Fraction(-3, 5)]
    activation = PolynomialActivation([1, -2, 1])
    base = evaluate_contracted_directional_gnf(q0, c, activation)
    for scale in (Fraction(-3, 2), Fraction(1, 3), Fraction(2)):
        scaled = evaluate_contracted_directional_gnf(
            q0, [scale * value for value in c], activation
        )
        assert scaled.ntk == scale**2 * base.ntk
        assert scaled.correction == scale**4 * base.correction


def test_arbitrary_fixed_batch_linear_control() -> None:
    q0 = [
        [1, Fraction(1, 5), Fraction(-1, 7)],
        [Fraction(1, 5), Fraction(4, 3), Fraction(1, 6)],
        [Fraction(-1, 7), Fraction(1, 6), Fraction(5, 4)],
    ]
    c = [Fraction(2, 5), Fraction(-1, 3), Fraction(3, 7)]
    result = evaluate_contracted_directional_gnf(
        q0, c, PolynomialActivation([0, 1])
    )
    q_eff = sum(c[a] * q0[a][b] * c[b] for a in range(3) for b in range(3))
    assert result.ntk == 3 * q_eff
    assert result.correction == 48 * q_eff**2
