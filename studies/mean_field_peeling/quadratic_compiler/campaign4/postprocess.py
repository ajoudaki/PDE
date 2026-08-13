#!/usr/bin/env python3
"""Exact bivariate moments and shifted-Hankel decision for Campaign 4."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import tempfile
import os
from typing import Iterable

import sympy as sp


HERE = Path(__file__).resolve().parent
alpha, beta = sp.symbols("alpha beta", nonnegative=True, real=True)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def atomic_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(
        prefix=path.name+".", suffix=".tmp", dir=path.parent
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            json.dump(value, stream, indent=2, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def load_derivatives(path: Path) -> list[sp.Expr]:
    raw = json.loads(path.read_text())
    derivatives = [sp.Integer(0)]*10
    for record in raw["jets"]:
        order = int(record["order"])
        expression = sp.Integer(0)
        for term in record["monomials"]:
            expression += (sp.Integer(term["value"])
                           * alpha**int(term["alpha_power"])
                           * beta**int(term["beta_power"]))
        derivatives[order] = sp.expand(expression)
    if any(derivatives[k] != 0 for k in (0, 2, 4, 6, 8)):
        raise ArithmeticError("feature parity failure")
    return derivatives


def moments(derivatives: list[sp.Expr]) -> list[sp.Expr]:
    a0, a1, a2, a3, a4 = [
        sp.cancel(derivatives[k]/sp.factorial(k))
        for k in (1, 3, 5, 7, 9)
    ]
    return [
        sp.cancel(3*a1/a0**2),
        sp.cancel((6*a1**2-5*a0*a2)/a0**5),
        sp.cancel((7*a0**2*a3-26*a0*a1*a2+21*a1**3)/a0**8),
        sp.cancel((-9*a0**3*a4+48*a0**2*a1*a3+20*a0**2*a2**2
                   -144*a0*a1**2*a2+90*a1**4)/a0**11),
    ]


def coefficient_table(poly: sp.Poly) -> list[dict[str, str | int]]:
    return [
        {"alpha_power": monomial[0], "beta_power": monomial[1],
         "coefficient": str(coefficient)}
        for monomial, coefficient in sorted(poly.terms())
    ]


def exact_grid_witness(poly: sp.Poly, maximum: int = 12):
    """Search exact rational/integer points only as a falsification route."""
    for denominator in (1, 2, 3, 4, 5, 7, 10):
        for numerator_a in range(maximum*denominator+1):
            for numerator_b in range(maximum*denominator+1):
                point_a = sp.Rational(numerator_a, denominator)
                point_b = sp.Rational(numerator_b, denominator)
                value = poly.eval({alpha: point_a, beta: point_b})
                if value < 0:
                    return {
                        "alpha": str(point_a), "beta": str(point_b),
                        "numerator_value": str(value),
                    }
    return None


def decide_numerator(poly: sp.Poly) -> dict:
    coefficients = [coefficient for _, coefficient in poly.terms()]
    if all(value >= 0 for value in coefficients):
        positive_support = [
            monomial for monomial, value in poly.terms() if value > 0
        ]
        strata = {
            "origin": (0, 0) in positive_support,
            "positive_alpha_axis": any(
                alpha_power > 0 and beta_power == 0
                for alpha_power, beta_power in positive_support
            ) or (0, 0) in positive_support,
            "positive_beta_axis": any(
                alpha_power == 0 and beta_power > 0
                for alpha_power, beta_power in positive_support
            ) or (0, 0) in positive_support,
            "strictly_positive_interior": bool(positive_support),
        }
        zero_strata = [name for name, positive in strata.items()
                       if not positive]
        return {
            "status": "nonnegative_on_quadrant",
            "method": "coefficientwise_nonnegative",
            "strictness_by_closed_quadrant_stratum": strata,
            "zero_set_on_closed_quadrant": (
                "empty" if not zero_strata else
                "union_of_strata: " + ", ".join(zero_strata)
            ),
            "negative_witness": None,
        }
    witness = exact_grid_witness(poly)
    if witness is not None:
        return {
            "status": "falsified",
            "method": "exact_rational_counterexample",
            "negative_witness": witness,
        }
    return {
        "status": "unresolved",
        "method": "mixed_coefficients_and_no_small_rational_witness",
        "negative_witness": None,
        "note": (
            "A numerical grid cannot certify positivity. Exact Bernstein, "
            "CAD, SOS, or another semialgebraic certificate is required."
        ),
    }


def rational_certificate(expression: sp.Expr, name: str) -> dict:
    expression = sp.cancel(expression)
    numerator, denominator = sp.fraction(expression)
    numerator = sp.Poly(sp.expand(numerator), alpha, beta, domain=sp.QQ)
    denominator = sp.Poly(sp.expand(denominator), alpha, beta, domain=sp.QQ)
    denominator_coefficients = [value for _, value in denominator.terms()]
    denominator_origin = denominator.eval({alpha: 0, beta: 0})
    if not all(value >= 0 for value in denominator_coefficients):
        raise ArithmeticError(f"{name} denominator has a negative coefficient")
    if denominator_origin <= 0:
        raise ArithmeticError(
            f"{name} denominator is not certified positive at the origin"
        )
    return {
        "name": name,
        "expression": str(sp.factor(expression)),
        "numerator_total_degree": numerator.total_degree(),
        "numerator_term_count": len(numerator.terms()),
        "numerator_coefficients": coefficient_table(numerator),
        "denominator_factorized": str(sp.factor(denominator.as_expr())),
        "denominator_at_origin": str(denominator_origin),
        "denominator_certificate": (
            "the expanded denominator has only nonnegative coefficients "
            "and has a strictly positive constant term; hence it is "
            "strictly positive on the entire closed nonnegative quadrant"
        ),
        "decision": decide_numerator(numerator),
    }


def compute(path: Path) -> dict:
    derivatives = load_derivatives(path)
    mu = moments(derivatives)
    ordinary = sp.cancel(mu[0]*mu[2]-mu[1]**2)
    shifted = sp.cancel(mu[1]*mu[3]-mu[2]**2)
    moment_certificates = [
        rational_certificate(value, f"mu_{index}")
        for index, value in enumerate(mu)
    ]
    ordinary_certificate = rational_certificate(ordinary, "ordinary_H1")
    shifted_certificate = rational_certificate(shifted, "shifted_H1")
    return {
        "schema_version": 2,
        "metric": "D_a + alpha D_u + beta D_W",
        "domain": "alpha>=0, beta>=0",
        "moments_mu": [str(sp.factor(value)) for value in mu],
        "moment_certificates": moment_certificates,
        "ordinary_H1": ordinary_certificate,
        "shifted_H1": shifted_certificate,
        "input_sha256": sha256(path),
        "postprocessor_sha256": sha256(Path(__file__)),
        "interpretation_limit": (
            "Finite-order formal-jet result only; not an all-order theorem "
            "or a global mean-field trajectory-identification result."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path,
                        default=HERE/"results_order9.json")
    parser.add_argument("--output", type=Path,
                        default=HERE/"certificates_order9.json")
    args = parser.parse_args()
    result = compute(args.input)
    atomic_json(args.output, result)
    print(json.dumps({
        "output": str(args.output), "sha256": sha256(args.output),
        "status": result["shifted_H1"]["decision"]["status"],
        "term_count": result["shifted_H1"]["numerator_term_count"],
    }))


if __name__ == "__main__":
    main()
