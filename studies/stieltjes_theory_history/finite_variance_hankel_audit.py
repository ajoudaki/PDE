#!/usr/bin/env python3
"""Exact finite-order Hankel positivity along the middle-weight variance path."""

from __future__ import annotations

import json
from fractions import Fraction
from math import factorial
from pathlib import Path

import sympy as sp

from sector_total_nonnegativity import C


alpha = sp.symbols("alpha", nonnegative=True)


def determinant3(matrix: list[list[sp.Expr]]) -> sp.Expr:
    return sp.cancel(
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def positive_rational_certificate(name: str, expression: sp.Expr) -> dict:
    numerator, denominator = sp.fraction(sp.cancel(expression))
    numerator_poly = sp.Poly(numerator, alpha)
    denominator_poly = sp.Poly(denominator, alpha)
    numerator_coefficients = list(reversed(numerator_poly.all_coeffs()))
    denominator_coefficients = list(reversed(denominator_poly.all_coeffs()))
    assert all(coefficient > 0 for coefficient in numerator_coefficients)
    assert all(coefficient > 0 for coefficient in denominator_coefficients)
    return {
        "name": name,
        "numerator_degree": numerator_poly.degree(),
        "numerator_coefficient_count": len(numerator_coefficients),
        "denominator": str(sp.factor(denominator)),
        "all_reduced_numerator_coefficients_strictly_positive": True,
        "all_reduced_denominator_coefficients_strictly_positive": True,
    }


def main() -> None:
    # F_alpha^(2r+1)(0)/alpha has coefficient A_r in s^(2r+1).
    A = [
        sp.cancel(sum(sp.Integer(value) * alpha**p for p, value in enumerate(row))
                  / factorial(2 * r + 1))
        for r, row in enumerate(C)
    ]
    a0, a1, a2, a3, a4, a5 = A

    mu = [
        sp.cancel(3 * a1 / a0**2),
        sp.cancel((6 * a1**2 - 5 * a0 * a2) / a0**5),
        sp.cancel((7 * a0**2 * a3 - 26 * a0 * a1 * a2 + 21 * a1**3) / a0**8),
        sp.cancel((-9 * a0**3 * a4 + 48 * a0**2 * a1 * a3
                   + 20 * a0**2 * a2**2 - 144 * a0 * a1**2 * a2
                   + 90 * a1**4) / a0**11),
        sp.cancel((11 * a0**4 * a5 - 78 * a0**3 * a1 * a4
                   - 62 * a0**3 * a2 * a3 + 297 * a0**2 * a1**2 * a3
                   + 253 * a0**2 * a1 * a2**2 - 836 * a0 * a1**3 * a2
                   + 429 * a1**5) / a0**14),
    ]

    h1 = sp.cancel(mu[0] * mu[2] - mu[1] ** 2)
    h1_shifted = sp.cancel(mu[1] * mu[3] - mu[2] ** 2)
    h2 = determinant3([[mu[i + j] for j in range(3)] for i in range(3)])

    expressions = [(f"mu_{r}", value) for r, value in enumerate(mu)] + [
        ("det_H1", h1), ("det_H1_shifted", h1_shifted), ("det_H2", h2)
    ]
    certificates = [positive_rational_certificate(name, value)
                    for name, value in expressions]

    expected_boundary = [
        sp.Integer(6), sp.Rational(7, 18), sp.Rational(55, 972),
        sp.Rational(245, 23328), sp.Rational(19, 8640),
    ]
    assert [sp.factor(value.subs(alpha, 0)) for value in mu] == expected_boundary

    expected_derivatives = [
        sp.Rational(413, 6), sp.Rational(511, 216),
        sp.Rational(39121, 58320), sp.Rational(1759939, 9797760),
        sp.Rational(3699973, 75582720),
    ]
    assert [sp.factor(sp.diff(value, alpha).subs(alpha, 0)) for value in mu] == expected_derivatives

    certificate_path = Path(__file__).with_name("certificates_order11.json")
    exact_at_one = [Fraction(value) for value in json.loads(
        certificate_path.read_text(encoding="utf-8"))["mu"]]
    assert [Fraction(sp.factor(value.subs(alpha, 1))) for value in mu] == exact_at_one

    print(json.dumps({
        "variance_symbol": "alpha",
        "scope": "mu_0 through mu_4 and every Hankel condition decidable from them",
        "domain": "alpha >= 0",
        "certificates": certificates,
        "boundary_moments": [str(value) for value in expected_boundary],
        "boundary_derivatives": [str(value) for value in expected_derivatives],
        "alpha_one_matches_certificates_order11": True,
        "result": "all listed rational functions are strictly positive for alpha >= 0",
    }, indent=2))


if __name__ == "__main__":
    main()
