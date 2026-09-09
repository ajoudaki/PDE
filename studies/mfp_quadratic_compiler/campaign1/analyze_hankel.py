#!/usr/bin/env python3
"""Exact Hankel postprocessor for Campaign 1 production jets.

The input is the JSON emitted by ``connected_parametric_multiroot.cpp``.
All series operations and sign checks use exact SymPy integers/rationals.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import factorial
import json
from pathlib import Path

import sympy as sp


lam = sp.symbols("lambda", nonnegative=True)


def polynomial(coefficients: list[str]) -> sp.Expr:
    return sp.Add(*(
        sp.Integer(value) * lam**degree
        for degree, value in enumerate(coefficients)
    ))


def jets(document: dict, root: str) -> list[sp.Expr]:
    records = document["observables"][root]["jets"]
    for expected, record in enumerate(records):
        if record["order"] != expected:
            raise ValueError(f"nonconsecutive {root} jet at order {expected}")
    return [polynomial(record["lambda_coefficients"]) for record in records]


def ascending_coefficients(poly: sp.Poly) -> list[sp.Integer]:
    return [sp.Integer(poly.nth(index)) for index in range(poly.degree() + 1)]


def sign_certificate(name: str, expression: sp.Expr) -> dict:
    expression = sp.cancel(expression)
    numerator, denominator = sp.fraction(expression)
    numerator_poly = sp.Poly(numerator, lam)
    denominator_poly = sp.Poly(denominator, lam)
    numerator_coefficients = ascending_coefficients(numerator_poly)
    denominator_coefficients = ascending_coefficients(denominator_poly)

    sample_points = [
        sp.Integer(0), sp.Rational(1, 100), sp.Rational(1, 10),
        sp.Rational(1, 2), sp.Integer(1), sp.Integer(2),
        sp.Integer(10), sp.Integer(100),
    ]
    sample_signs = []
    negative_sample = None
    for point in sample_points:
        value = sp.factor(expression.subs(lam, point))
        sign = 1 if value > 0 else -1 if value < 0 else 0
        sample_signs.append({"lambda": str(point), "sign": sign})
        if sign < 0 and negative_sample is None:
            negative_sample = str(point)

    numerator_nonnegative = all(value >= 0 for value in numerator_coefficients)
    denominator_positive = all(value >= 0 for value in denominator_coefficients)
    denominator_positive = denominator_positive and any(
        value > 0 for value in denominator_coefficients
    )
    if negative_sample is not None:
        status = "falsified_at_exact_sample"
    elif numerator_nonnegative and denominator_positive:
        status = "certified_nonnegative_for_lambda_ge_0"
    else:
        status = "unresolved_by_coefficient_sign_and_exact_stress_grid"

    return {
        "name": name,
        "status": status,
        "factored_expression": str(sp.factor(expression)),
        "numerator_degree": numerator_poly.degree(),
        "denominator_degree": denominator_poly.degree(),
        "numerator_coefficients_ascending": [
            str(value) for value in numerator_coefficients
        ],
        "denominator_coefficients_ascending": [
            str(value) for value in denominator_coefficients
        ],
        "exact_sample_signs": sample_signs,
    }


def analyze(document: dict) -> dict:
    if not document.get("regression_gates_passed"):
        raise ValueError("compiler regression gates did not pass")
    if document.get("metric_exponents") != {"a": 0, "u": 1, "w": 1}:
        raise ValueError("postprocessor is frozen to D_a+lambda(D_u+D_W)")

    f = jets(document, "f")
    q2 = jets(document, "q2")
    if len(f) <= 7 or len(q2) <= 6:
        raise ValueError("need f through order 7 and Q2 through order 6")

    # Ordinary Taylor coefficients in feature time s.
    a = f[1]
    b = f[3] / factorial(3)
    c = f[5] / factorial(5)
    d = f[7] / factorial(7)
    p = q2[2] / factorial(2)
    r = q2[4] / factorial(4)
    t = q2[6] / factorial(6)

    # Output-kernel moments for K(y)=a+mu0*y^2-mu1*y^4+mu2*y^6+...
    mu0 = sp.cancel(3 * b / a**2)
    mu1 = sp.cancel((6 * b**2 - 5 * a * c) / a**5)
    mu2 = sp.cancel((7 * a**2 * d - 26 * a * b * c + 21 * b**3) / a**8)
    output_h1 = sp.cancel(mu0 * mu2 - mu1**2)

    # F^{-1}(y)=alpha*y+beta*y^3+chi*y^5+O(y^7).
    alpha = sp.cancel(1 / a)
    beta = sp.cancel(-b / a**4)
    chi = sp.cancel(3 * b**2 / a**7 - c / a**6)

    # V2(y)=Q2(F^{-1}(y))=3+c1*y^2+c2*y^4+c3*y^6+...
    c1 = sp.cancel(p * alpha**2)
    c2 = sp.cancel(2 * p * alpha * beta + r * alpha**4)
    c3 = sp.cancel(
        p * (2 * alpha * chi + beta**2)
        + 4 * r * alpha**3 * beta
        + t * alpha**6
    )

    # T2(x)=(V2(sqrt(x))-3)/x=nu0-nu1*x+nu2*x^2+...
    nu0 = c1
    nu1 = sp.cancel(-c2)
    nu2 = c3
    hidden_h1 = sp.cancel(nu0 * nu2 - nu1**2)

    # The output values at lambda=1 are an independent transformation gate.
    expected_mu = [
        sp.Rational(280864, 4107),
        sp.Rational(38443196932, 5616860517),
        sp.Rational(37578479127292096, 12802987609542045),
    ]
    actual_mu = [sp.factor(value.subs(lam, 1)) for value in (mu0, mu1, mu2)]
    if actual_mu != expected_mu:
        raise AssertionError(f"canonical output moments differ: {actual_mu}")

    expressions = {
        "mu_0": mu0,
        "mu_1": mu1,
        "mu_2": mu2,
        "output_det_H1": output_h1,
        "nu_0": nu0,
        "nu_1": nu1,
        "nu_2": nu2,
        "hidden_det_H1": hidden_h1,
    }
    certificates = [
        sign_certificate(name, expression)
        for name, expression in expressions.items()
    ]
    statuses = {record["name"]: record["status"] for record in certificates}
    falsified = [
        name for name, status in statuses.items()
        if status == "falsified_at_exact_sample"
    ]
    unresolved = [
        name for name, status in statuses.items()
        if status.startswith("unresolved")
    ]

    return {
        "schema_version": 1,
        "source_parent_sha256": document["parent_source_sha256"],
        "metric_line": "D_lambda = D_a + lambda(D_u + D_W)",
        "scope": "mu_0..mu_2, nu_0..nu_2, and ordinary 2x2 Hankel tests",
        "canonical_output_moment_regression_passed": True,
        "canonical_hidden_moments": [
            str(sp.factor(value.subs(lam, 1)))
            for value in (nu0, nu1, nu2)
        ],
        "certificates": certificates,
        "falsified_quantities": falsified,
        "unresolved_quantities": unresolved,
        "all_listed_nonnegative_on_lambda_ge_0": not falsified and not unresolved,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = analyze(json.loads(args.input.read_text(encoding="utf-8")))
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
        print(f"wrote={args.output}")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
