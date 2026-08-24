#!/usr/bin/env python3
"""Exact order-five Stieltjes audit for the two-input cubic plus channel."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
INPUT = HERE / "results_symbolic_order5.json"
PROTOCOL = HERE / "STIELTJES_ORDER5_PROTOCOL.md"
EXPECTED_SHA256 = {
    "input": "ac948d64b979f226424e1ff745512f0f97e78e164708f4313c41a48d41591023",
    "protocol": "d30ccf7b183c79ce5ef3780bec9d0d9be9ab9788a27be062a7d1d67df3a79e90",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rational_string(value: sp.Rational) -> str:
    numerator, denominator = value.as_numer_denom()
    if denominator == 1:
        return str(numerator)
    return f"{numerator}/{denominator}"


def polynomial_from_strings(
    values: list[str], variable: sp.Symbol
) -> sp.Poly:
    expression = sp.Add(
        *(
            sp.Rational(Fraction(value).numerator, Fraction(value).denominator)
            * variable**degree
            for degree, value in enumerate(values)
        )
    )
    return sp.Poly(expression, variable, domain=sp.QQ)


def sturm_certificate(polynomial: sp.Poly, variable: sp.Symbol) -> dict[str, object]:
    sequence = sp.sturm(polynomial.as_expr(), variable)

    def signs_at(point: int) -> list[int]:
        signs: list[int] = []
        for member in sequence:
            value = sp.sign(sp.together(member.subs(variable, point)))
            if value:
                signs.append(int(value))
        return signs

    def variations(signs: list[int]) -> int:
        return sum(left != right for left, right in zip(signs, signs[1:]))

    left_signs = signs_at(-1)
    right_signs = signs_at(1)
    left_variations = variations(left_signs)
    right_variations = variations(right_signs)
    root_count = left_variations - right_variations
    if root_count != 0:
        raise AssertionError(f"unexpected roots on [-1,1]: {root_count}")
    left_value = polynomial.eval(-1)
    right_value = polynomial.eval(1)
    if left_value <= 0 or right_value <= 0:
        raise AssertionError("root-free polynomial does not have positive endpoints")
    return {
        "degree": polynomial.degree(),
        "sturm_sequence_length": len(sequence),
        "variations_at_minus_1": left_variations,
        "variations_at_plus_1": right_variations,
        "distinct_roots_on_closed_interval": root_count,
        "value_at_minus_1": rational_string(left_value),
        "value_at_plus_1": rational_string(right_value),
        "strictly_positive_on_closed_interval": True,
    }


def moment_formula_gate() -> None:
    time, output = sp.symbols("time output")
    a, b, c = sp.symbols("a b c", nonzero=True)
    feature = a * time + b * time**3 / 6 + c * time**5 / 120
    inverse = (
        output / a
        - b * output**3 / (6 * a**4)
        + (10 * b**2 - a * c) * output**5 / (120 * a**7)
    )
    composition = sp.series(feature.subs(time, inverse), output, 0, 7).removeO()
    if sp.expand(composition - output) != 0:
        raise AssertionError("formal inverse gate failed")

    kernel = sp.diff(feature, time).subs(time, inverse)
    kernel = sp.series(kernel, output, 0, 6).removeO().expand()
    mu0 = b / (2 * a**2)
    mu1 = (4 * b**2 - a * c) / (24 * a**5)
    expected = a + mu0 * output**2 - mu1 * output**4
    if sp.factor(kernel - expected) != 0:
        raise AssertionError("series-reversion moment formula gate failed")

    triangular = sp.series(
        expected.subs(output, feature), time, 0, 6
    ).removeO()
    if sp.factor(triangular - sp.diff(feature, time)) != 0:
        raise AssertionError("triangular moment formula gate failed")


def main() -> int:
    hashes = {"input": sha256(INPUT), "protocol": sha256(PROTOCOL)}
    if hashes != EXPECTED_SHA256:
        raise AssertionError(
            f"SHA-256 gate failed: actual={hashes}, expected={EXPECTED_SHA256}"
        )

    moment_formula_gate()
    document = json.loads(INPUT.read_text())
    rho = sp.symbols("rho")
    derivatives = document["derivatives"]
    a = polynomial_from_strings(derivatives["F_1"], rho)
    b = polynomial_from_strings(derivatives["F_3"], rho)
    c = polynomial_from_strings(derivatives["F_5"], rho)

    one_plus = sp.Poly(rho + 1, rho, domain=sp.QQ)

    def quotient(poly: sp.Poly, multiplicity: int) -> sp.Poly:
        divisor = one_plus**multiplicity
        answer, remainder = sp.div(poly, divisor)
        if not remainder.is_zero:
            raise AssertionError("forced (1+rho) factor is missing")
        if sp.rem(answer, one_plus).is_zero:
            raise AssertionError("forced factor multiplicity is not exact")
        return answer

    a_reduced = quotient(a, 1)
    b_reduced = quotient(b, 2)
    c_reduced = quotient(c, 3)
    numerator = sp.Poly(4 * b.as_expr() ** 2 - a.as_expr() * c.as_expr(), rho)
    numerator_reduced = quotient(numerator, 4)

    expected_constants = {
        "A": sp.Rational(81, 2),
        "P": sp.Integer(39366),
        "C": sp.Rational(14348907, 2),
        "N": sp.Rational(387420489, 4),
    }
    primitives: dict[str, sp.Poly] = {}
    for name, reduced in (
        ("A", a_reduced),
        ("P", b_reduced),
        ("C", c_reduced),
        ("N", numerator_reduced),
    ):
        content, primitive = reduced.primitive()
        if content != expected_constants[name]:
            raise AssertionError(
                f"unexpected {name} content: {content} != {expected_constants[name]}"
            )
        primitives[name] = primitive

    certificates = {
        name: sturm_certificate(polynomial, rho)
        for name, polynomial in primitives.items()
    }

    aa = a.as_expr()
    bb = b.as_expr()
    cc = c.as_expr()
    mu0 = sp.cancel(bb / (2 * aa**2))
    mu1 = sp.cancel((4 * bb**2 - aa * cc) / (24 * aa**5))

    expected_mu0 = sp.cancel(
        12 * primitives["P"].as_expr() / primitives["A"].as_expr() ** 2
    )
    expected_mu1 = sp.cancel(
        primitives["N"].as_expr()
        / (
            27
            * (rho + 1)
            * primitives["A"].as_expr() ** 5
        )
    )
    if sp.cancel(mu0 - expected_mu0) != 0:
        raise AssertionError("reduced mu_0 formula failed")
    if sp.cancel(mu1 - expected_mu1) != 0:
        raise AssertionError("reduced mu_1 formula failed")

    point_values: dict[str, dict[str, str]] = {}
    for label, value in (
        ("rho_0", sp.Rational(0)),
        ("rho_1_over_2", sp.Rational(1, 2)),
        ("rho_1", sp.Rational(1)),
    ):
        value0 = sp.factor(mu0.subs(rho, value))
        value1 = sp.factor(mu1.subs(rho, value))
        point_values[label] = {
            "rho": rational_string(value),
            "mu_0": rational_string(value0),
            "mu_0_decimal": str(sp.N(value0, 20)),
            "mu_1": rational_string(value1),
            "mu_1_decimal": str(sp.N(value1, 20)),
        }

    removable_mu0 = sp.factor(sp.limit(mu0, rho, -1, dir="+"))
    mu1_residue = sp.factor(sp.limit((rho + 1) * mu1, rho, -1, dir="+"))
    if removable_mu0 <= 0 or mu1_residue <= 0:
        raise AssertionError("degenerate-endpoint asymptotic sign failed")

    payload = {
        "model": document["model"],
        "kernel_convention": (
            "K_+(y;rho)=F_+'(F_+^(-1)(y;rho);rho)="
            "F_+'(0;rho)+sum_r (-1)^r mu_r(rho) y^(2r+2)"
        ),
        "highest_feature_derivative_order": 5,
        "determined_moments": ["mu_0", "mu_1"],
        "source_sha256": hashes,
        "factorizations": {
            "F_1": "81*(rho+1)*A(rho)/2",
            "F_3": "39366*(rho+1)^2*P(rho)",
            "F_5": "14348907*(rho+1)^3*C(rho)/2",
            "4*F_3^2-F_1*F_5": (
                "387420489*(rho+1)^4*N(rho)/4"
            ),
            "A_coefficients_ascending": [
                rational_string(value)
                for value in primitives["A"].all_coeffs()[::-1]
            ],
            "P_coefficients_ascending": [
                rational_string(value)
                for value in primitives["P"].all_coeffs()[::-1]
            ],
            "C_coefficients_ascending": [
                rational_string(value)
                for value in primitives["C"].all_coeffs()[::-1]
            ],
            "N_coefficients_ascending": [
                rational_string(value)
                for value in primitives["N"].all_coeffs()[::-1]
            ],
        },
        "moments": {
            "mu_0": "12*P(rho)/A(rho)^2",
            "mu_1": "N(rho)/(27*(rho+1)*A(rho)^5)",
        },
        "sturm_certificates": certificates,
        "exact_specializations": point_values,
        "rho_minus_1": {
            "status": "output-coordinate moments undefined because F_+'(0;-1)=0",
            "mu_0_removable_right_limit": rational_string(removable_mu0),
            "mu_0_limit_decimal": str(sp.N(removable_mu0, 20)),
            "mu_1_right_limit": "+infinity",
            "positive_simple_pole_residue": rational_string(mu1_residue),
            "positive_simple_pole_residue_decimal": str(sp.N(mu1_residue, 20)),
        },
        "accessible_hankel_conditions": {
            "H_0=[mu_0]": "positive definite for every -1<rho<=1",
            "H_0_plus=[mu_1]": "positive definite for every -1<rho<=1",
            "H_1": "undetermined; requires mu_2 and F_+^(7)(0;rho)",
        },
        "verdict": (
            "sign-consistent strict finite-prefix compatibility on "
            "-1<rho<=1; rho=-1 is degenerate, not a violation"
        ),
        "claim_boundary": (
            "Only the two one-by-one Hankel conditions are decided. "
            "No 2x2 Hankel determinant or all-order Stieltjes claim follows."
        ),
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
