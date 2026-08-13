#!/usr/bin/env python3
"""Exact Campaign-3 output-kernel moments and interval certificates."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
t = sp.symbols("t")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def polynomial(coefficients: list[str | int]) -> sp.Poly:
    return sp.Poly(sum(int(value)*t**q for q, value in enumerate(coefficients)),
                   t, domain=sp.ZZ)


def load_jets(path: Path) -> dict[int, sp.Poly]:
    data = json.loads(path.read_text())
    jets = {order: polynomial(data["jets_t"][order])
            for order in (1, 3, 5, 7)}
    for order in (0, 2, 4, 6):
        if any(int(value) for value in data["jets_t"][order]):
            raise ArithmeticError(f"even feature jet {order} is nonzero")
    for order, jet in jets.items():
        bound = 2*(order+1)
        if jet.degree() > bound:
            raise ArithmeticError(
                f"order {order} has degree {jet.degree()} > bound {bound}"
            )
    return jets


def stieltjes_expressions(jets: dict[int, sp.Poly]) -> dict[str, sp.Expr]:
    a, b, c5, d = (jets[order].as_expr() for order in (1, 3, 5, 7))
    mu0 = sp.cancel(b/(2*a**2))
    mu1 = sp.cancel((4*b**2-a*c5)/(24*a**5))
    mu2 = sp.cancel((a**2*d-26*a*b*c5+70*b**3)/(720*a**8))
    determinant = sp.cancel(mu0*mu2-mu1**2)
    audit = sp.cancel(
        (2*a**2*b*d-5*a**2*c5**2-12*a*b**2*c5+60*b**4)
        /(2880*a**10)
    )
    if sp.cancel(determinant-audit) != 0:
        raise AssertionError("universal ordinary-H1 identity failed")
    return {"mu0": mu0, "mu1": mu1, "mu2": mu2,
            "ordinary_H1": determinant}


def strict_polynomial_certificate(poly: sp.Poly, left: int, right: int) -> dict:
    """Certify strict positivity by exact Sturm root counting.

    The endpoint values are exact integers/rationals.  With no real root in
    the closed interval and a positive endpoint, continuity proves strict
    positivity throughout.  We retain the full Sturm sequence degrees and
    endpoint sign-variation counts as a durable, independently replayable
    certificate rather than relying on a floating grid.
    """
    poly = sp.Poly(poly, t, domain=sp.QQ)
    left_value, right_value = poly.eval(left), poly.eval(right)
    roots = int(sp.count_roots(poly, left, right))
    if left_value <= 0 or right_value <= 0 or roots != 0:
        raise ArithmeticError(
            f"polynomial not certified strictly positive on [{left},{right}]: "
            f"endpoints=({left_value},{right_value}), roots={roots}"
        )
    sturm = sp.sturm(poly.as_expr(), t)

    def sign_variations(point: int) -> int:
        signs = []
        for expression in sturm:
            value = sp.sign(sp.expand(expression).subs(t, point))
            if value:
                signs.append(int(value))
        return sum(x != y for x, y in zip(signs, signs[1:]))

    return {
        "interval": [left, right],
        "method": "exact_Sturm_no_roots_plus_positive_endpoints",
        "real_root_count_closed_interval": roots,
        "left_value": str(left_value),
        "right_value": str(right_value),
        "sturm_sequence_degrees": [sp.Poly(x, t).degree() for x in sturm],
        "sturm_endpoint_variations": [sign_variations(left),
                                       sign_variations(right)],
        "strictly_positive": True,
    }


def rational_certificate(expression: sp.Expr) -> dict:
    numerator, denominator = sp.fraction(sp.cancel(expression))
    numerator = sp.Poly(numerator, t, domain=sp.QQ)
    denominator = sp.Poly(denominator, t, domain=sp.QQ)
    return {
        "reduced_expression": str(sp.factor(expression)),
        "numerator_factorized": str(sp.factor(numerator.as_expr())),
        "denominator_factorized": str(sp.factor(denominator.as_expr())),
        "numerator_coefficients_ascending": [
            str(numerator.nth(q)) for q in range(numerator.degree()+1)
        ],
        "denominator_coefficients_ascending": [
            str(denominator.nth(q)) for q in range(denominator.degree()+1)
        ],
        "halves": {
            "centered_to_uncentered": {
                "c_interval": [0, 1], "t_interval": [0, 1],
                "numerator": strict_polynomial_certificate(numerator, 0, 1),
                "denominator": strict_polynomial_certificate(denominator, 0, 1),
            },
            "overcentered": {
                "c_interval": [1, 2], "t_interval": [-1, 0],
                "numerator": strict_polynomial_certificate(numerator, -1, 0),
                "denominator": strict_polynomial_certificate(denominator, -1, 0),
            },
        },
        "strictly_positive_for_c_in_0_2": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path,
                        default=HERE/"frozen/results_order7.json")
    parser.add_argument("--output", type=Path,
                        default=HERE/"certificates_order7.json")
    args = parser.parse_args()
    jets = load_jets(args.input)
    accepted = {1: 111, 3: 1_685_184, 5: 77_400_633_120,
                7: 7_315_868_433_079_296}
    for order, expected in accepted.items():
        if jets[order].eval(1) != expected:
            raise ArithmeticError(
                f"canonical t=1 mismatch at order {order}: "
                f"{jets[order].eval(1)} != {expected}"
            )
    first_expected = sp.Poly(60+44*t**2+7*t**4, t)
    if jets[1] != first_expected:
        raise ArithmeticError("F1 does not equal 60+44t^2+7t^4")
    expressions = stieltjes_expressions(jets)
    output = {
        "campaign": "centered quadratic first activation, exact order seven",
        "parameter": "t=1-c in [-1,1], equivalently c in [0,2]",
        "input_sha256": sha256(args.input),
        "source_sha256": sha256(HERE/"centered_connected.cpp"),
        "reference_source_sha256": sha256(HERE/"centered_reference.py"),
        "postprocess_source_sha256": sha256(Path(__file__)),
        "jets_t": {
            str(order): [str(jets[order].nth(q))
                         for q in range(jets[order].degree()+1)]
            for order in (1, 3, 5, 7)
        },
        "audits": {
            "all_even_feature_jets_zero_through_order_six": True,
            "degree_bound_Fk_at_most_2_times_k_plus_1": True,
            "canonical_t1_matches_accepted_orders_1_3_5_7": True,
            "F1_exact_formula": "60 + 44*t^2 + 7*t^4",
        },
        "certificates": {
            name: rational_certificate(value)
            for name, value in expressions.items()
        },
        "scope": (
            "Finite-order exact evidence only. Positivity of mu0,mu1,mu2 "
            "and ordinary H1 is not an all-order Stieltjes proof."
        ),
    }
    args.output.write_text(json.dumps(output, indent=2)+"\n")
    print(args.output)


if __name__ == "__main__":
    main()
