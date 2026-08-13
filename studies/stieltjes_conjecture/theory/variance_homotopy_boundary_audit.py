#!/usr/bin/env python3
"""Exact series audit for the solvable variance boundary and first variation."""

from __future__ import annotations

import sympy as sp


s = sp.symbols("s")


def truncate(expression: sp.Expr, order: int = 14) -> sp.Expr:
    return sp.series(expression, s, 0, order).removeO().expand()


def inverse_composition_coefficient(g: sp.Expr, f: sp.Expr, degree: int) -> sp.Expr:
    """Return [z^degree] g(f^{-1}(z)) by Lagrange--Bürmann."""
    if degree == 0:
        return sp.simplify(g.subs(s, 0))
    expression = sp.diff(g, s) * (s / f) ** degree
    coefficient = sp.series(expression, s, 0, degree).removeO().expand().coeff(
        s, degree - 1
    )
    return sp.factor(coefficient / degree)


def det2(a: sp.Expr, b: sp.Expr, c: sp.Expr) -> sp.Expr:
    return sp.factor(a * c - b * b)


def main() -> None:
    f0 = 36 * s * sp.exp(72 * s**2)
    kappa0_as_s = sp.diff(f0, s)
    mu0 = [
        sp.factor((-1) ** r * inverse_composition_coefficient(
            kappa0_as_s, f0, 2 * r + 2
        ))
        for r in range(5)
    ]
    expected_mu0 = [
        sp.Integer(6), sp.Rational(7, 18), sp.Rational(55, 972),
        sp.Rational(245, 23328), sp.Rational(19, 8640),
    ]
    assert mu0 == expected_mu0

    # Exact truncated series for I(s)=int_0^s exp(72u^2)du.
    integral = sum(
        sp.Integer(72) ** k * s ** (2 * k + 1)
        / (sp.factorial(k) * (2 * k + 1))
        for k in range(8)
    )
    f1 = truncate(
        54 * (integral.subs(s, 2 * s) - integral)
        + 240 * s * sp.exp(144 * s**2)
        - (459 + 27648 * s**2) * s * sp.exp(72 * s**2)
        + 240 * (1 + 144 * s**2) * sp.exp(72 * s**2) * integral
    )
    q = 144 * s**2
    kappa1_as_s = truncate(
        sp.diff(f1, s) - 144 * s * (q + 3) / (q + 1) * f1
    )
    assert kappa1_as_s.subs(s, 0) == 75

    dot_mu = [
        sp.factor((-1) ** r * inverse_composition_coefficient(
            kappa1_as_s, f0, 2 * r + 2
        ))
        for r in range(5)
    ]
    expected_dot_mu = [
        sp.Rational(413, 6), sp.Rational(511, 216),
        sp.Rational(39121, 58320), sp.Rational(1759939, 9797760),
        sp.Rational(3699973, 75582720),
    ]
    assert dot_mu == expected_dot_mu
    shifted = det2(dot_mu[1], dot_mu[2], dot_mu[3])
    assert shifted == -sp.Rational(340410949, 13604889600)

    # p(t)=1-4t: L(t p(t)^2)=mu1-8mu2+16mu3.
    witness_variation = sp.factor(dot_mu[1] - 8 * dot_mu[2] + 16 * dot_mu[3])
    witness_boundary = sp.factor(mu0[1] - 8 * mu0[2] + 16 * mu0[3])
    assert witness_variation == -sp.Rational(3877, 30618)
    assert witness_boundary == sp.Rational(76, 729)

    print("boundary_moments=", mu0)
    print("first_variation_moments=", dot_mu)
    print("shifted_2x2_variation_determinant=", shifted)
    print("p=1-4t variation_witness=", witness_variation)
    print("p=1-4t boundary_witness=", witness_boundary)
    print("certificate=exact_boundary_and_first_variation_checks_pass")


if __name__ == "__main__":
    main()
