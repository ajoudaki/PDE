"""Exact regressions for the raw-square shallow reduction."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from shallow_quadratic_certificate import (
    ACTIVATION_MULTIPLIER,
    BOUNDARY_CERTIFICATE,
    build_certificate,
    determinant3,
    riccati_algebra_gates,
)


HERE = Path(__file__).resolve().parent
RETAINED = HERE / "SHALLOW_QUADRATIC_CERTIFICATE.json"


def test_retained_certificate_regenerates_exactly() -> None:
    assert build_certificate() == json.loads(RETAINED.read_text())


def test_moment_and_hankel_scaling_are_rebuilt_from_boundary() -> None:
    boundary = json.loads(BOUNDARY_CERTIFICATE.read_text())
    reduced = [Fraction(value) for value in boundary["output_kernel_moments_mu"]]
    shallow = [
        value * ACTIVATION_MULTIPLIER ** (2 * order)
        for order, value in enumerate(reduced)
    ]
    assert shallow == [
        Fraction(480, 49),
        Fraction(43756, 16807),
        Fraction(7214528, 2470629),
        Fraction(37635527904, 9886633715),
        Fraction(171752915595136, 30520038278205),
        Fraction(2199776554157960896, 246754509479287425),
    ]

    shifted = [
        [shallow[row + column + 1] for column in range(3)]
        for row in range(3)
    ]
    determinant = determinant3(shifted)
    assert determinant == Fraction(
        -86245462994269879146938487857152,
        516623655319449980325461333747775,
    )
    assert determinant == (
        ACTIVATION_MULTIPLIER**18
        * Fraction(boundary["negative_shifted_H2_determinant"])
    )
    assert determinant < 0


def test_feature_derivative_scaling_has_baseline_seven() -> None:
    boundary = json.loads(BOUNDARY_CERTIFICATE.read_text())
    shallow = {
        int(order): Fraction(value) / ACTIVATION_MULTIPLIER ** (int(order) + 1)
        for order, value in boundary["feature_derivatives"].items()
    }
    assert shallow[1] == 7
    assert shallow[3] == 960
    assert shallow[13] == 6004476167091978240
    assert all(shallow[order] == 0 for order in range(0, 14, 2))


def test_riccati_and_D_solution_identities_are_exact() -> None:
    gates = riccati_algebra_gates()
    assert gates["neuron_invariant_lie_derivative_zero"] is True
    assert gates["D_first_integral_lie_derivative_zero"] is True
    assert gates["D_first_integral_initial_value_zero"] is True
    assert gates["riccati_residual_zero_after_D_equation"] is True
    assert gates["v_equation_residual_zero"] is True
    assert gates["a_prime_equals_v_squared_after_first_integral"] is True
