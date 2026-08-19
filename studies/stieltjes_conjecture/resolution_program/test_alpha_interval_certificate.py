"""Regression tests for the retained strictly-positive-alpha certificate."""

import json
from fractions import Fraction
from pathlib import Path

from alpha_interval_certificate import ODD_JET_COEFFICIENTS, build_certificate
from alpha_interval_tools import peval, poly, shifted_h2_from_jets
from block_metric_counterexample import (
    determinant,
    hankel,
    inverse_derivative_moments,
    output_kernel_moments,
)


HERE = Path(__file__).resolve().parent
RETAINED = HERE / "ALPHA_INTERVAL_CERTIFICATE.json"


def test_retained_certificate_regenerates_exactly() -> None:
    assert build_certificate() == json.loads(RETAINED.read_text())


def test_interval_has_two_independent_exact_sign_checks() -> None:
    certificate = build_certificate()
    assert certificate["epsilon"] == "1/100"
    assert certificate["convexity_certificate"] is True
    assert certificate["strictly_positive_second_derivative_coefficients"] is True
    assert certificate["all_bernstein_coefficients_strictly_negative"] is True
    assert certificate["largest_bernstein_coefficient_index"] == 36


def test_scalar_reconstruction_matches_polynomial_postprocessor() -> None:
    jets = [poly(coefficients) for coefficients in ODD_JET_COEFFICIENTS]
    polynomial_determinant = shifted_h2_from_jets(jets)
    for alpha in (Fraction(0), Fraction(1, 100), Fraction(1, 3), Fraction(1)):
        derivatives = [Fraction(0)] * 14
        for index, jet in enumerate(jets):
            derivatives[2 * index + 1] = peval(jet, alpha)
        inverse_moments = inverse_derivative_moments(derivatives, 7)
        moments = output_kernel_moments(inverse_moments)
        scalar_determinant = determinant(hankel(moments, 3, shift=1))
        assert scalar_determinant == polynomial_determinant.evaluate(alpha)
