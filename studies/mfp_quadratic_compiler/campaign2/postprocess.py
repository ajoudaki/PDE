#!/usr/bin/env python3
"""Exact Campaign-2 normalization and order-seven Hankel certificates."""

from __future__ import annotations

import argparse
from fractions import Fraction
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


def load_jets(path: Path) -> dict[int, sp.Poly]:
    data = json.loads(path.read_text())
    jets = {}
    for order in (1, 3, 5, 7):
        raw = [int(x) for x in data["raw_theta"][order]]
        divisor = 2 ** (order + 1)
        if any(coefficient % divisor for coefficient in raw):
            raise ArithmeticError(f"order {order} normalization is nonintegral")
        normalized = [coefficient // divisor for coefficient in raw]
        if any(normalized[index] for index in range(1, len(normalized), 2)):
            raise ArithmeticError(f"order {order} is not even in theta")
        jets[order] = sp.Poly(
            sum(normalized[2 * index] * t**index
                for index in range((len(normalized) + 1) // 2)), t,
            domain=sp.ZZ,
        )
    return jets


def divide_minus_endpoint(jets: dict[int, sp.Poly]) -> dict[int, sp.Poly]:
    out = {}
    for order, jet in jets.items():
        power = (order + 1) // 2
        quotient, remainder = sp.div(jet.as_expr(), (1 - t) ** power, t)
        if sp.expand(remainder) != 0:
            raise ArithmeticError(
                f"minus order {order} lacks forced endpoint power {power}"
            )
        out[order] = sp.Poly(quotient, t, domain=sp.ZZ)
    return out


def certificates(jets: dict[int, sp.Poly]) -> dict[str, sp.Expr]:
    a, b, c, d = (jets[k].as_expr() for k in (1, 3, 5, 7))
    # Universal reversion formulas for derivative jets.
    mu0 = sp.cancel(b / (2 * a**2))
    mu1 = sp.cancel((4 * b**2 - a * c) / (24 * a**5))
    mu2 = sp.cancel((a**2 * d - 26 * a * b * c + 70 * b**3)
                    / (720 * a**8))
    determinant = sp.cancel(mu0 * mu2 - mu1**2)
    expected = sp.cancel(
        (2 * a**2 * b * d - 5 * a**2 * c**2 - 12 * a * b**2 * c
         + 60 * b**4) / (2880 * a**10)
    )
    if sp.cancel(determinant - expected) != 0:
        raise AssertionError("universal determinant formula mismatch")
    return {"mu0": mu0, "mu1": mu1, "mu2": mu2,
            "ordinary_H1": determinant}


def sign_certificate(expression: sp.Expr) -> dict:
    numerator, denominator = map(sp.Poly, sp.fraction(sp.factor(expression)))
    numerator = sp.Poly(numerator, t, domain=sp.QQ)
    denominator = sp.Poly(denominator, t, domain=sp.QQ)
    # Positive-coefficient proof is exact on t>=0.  If unavailable, use exact
    # Sturm root counts together with endpoint signs on [0,1].
    num_coefficients = list(reversed(numerator.all_coeffs()))
    den_coefficients = list(reversed(denominator.all_coeffs()))
    num_positive = all(x > 0 for x in num_coefficients)
    den_positive = all(x > 0 for x in den_coefficients)
    method = "strict_coefficientwise_positive" if num_positive and den_positive \
        else "exact_sturm_no_roots_and_positive_endpoint"
    if method.startswith("exact_sturm"):
        for poly, name in ((numerator, "numerator"),
                           (denominator, "denominator")):
            roots = sp.polys.polytools.count_roots(poly, 0, 1)
            if roots != 0 or poly.eval(0) <= 0 or poly.eval(1) <= 0:
                raise ArithmeticError(f"{name} not strictly positive on [0,1]")
    return {
        "method": method,
        "strictly_positive_on_closed_unit_interval": True,
        "numerator_factorized": str(sp.factor(numerator.as_expr())),
        "denominator_factorized": str(sp.factor(denominator.as_expr())),
        "numerator_coefficients_ascending": [str(x) for x in num_coefficients],
        "denominator_coefficients_ascending": [str(x) for x in den_coefficients],
    }


def polynomial_json(poly: sp.Poly) -> list[str]:
    return [str(poly.nth(i)) for i in range(poly.degree() + 1)]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--plus", type=Path,
                        default=HERE / "frozen/plus_order7_raw.json")
    parser.add_argument("--minus", type=Path,
                        default=HERE / "frozen/minus_order7_raw.json")
    parser.add_argument("--output", type=Path,
                        default=HERE / "certificates_order7.json")
    args = parser.parse_args()

    plus = load_jets(args.plus)
    minus_raw = load_jets(args.minus)
    minus = divide_minus_endpoint(minus_raw)

    accepted = {1: 111, 3: 1_685_184, 5: 77_400_633_120,
                7: 7_315_868_433_079_296}
    for order, expected in accepted.items():
        if plus[order].eval(1) != expected:
            raise ArithmeticError(f"plus endpoint mismatch at order {order}")

    output = {
        "object": "Campaign 2 exact two-input natural-loss channels",
        "parameter": "t=theta^2 in [0,1]",
        "plus_raw_sha256": sha256(args.plus),
        "minus_raw_sha256": sha256(args.minus),
        "source_sha256": sha256(HERE / "two_input_connected.cpp"),
        "frozen_binary_sha256": sha256(HERE / "frozen/two_input_connected_vp"),
        "jets": {
            "plus": {str(k): polynomial_json(v) for k, v in plus.items()},
            "minus_raw": {str(k): polynomial_json(v)
                          for k, v in minus_raw.items()},
            "minus_normalized_h": {str(k): polynomial_json(v)
                                   for k, v in minus.items()},
        },
        "endpoint_audits": {
            "plus_t1_matches_single_input_through_order7": True,
            "minus_forced_powers_all_exact": True,
            "minus_raw_statement": (
                "raw g-minus has the same Hankel signs for 0<=t<1; "
                "t=1 is a degenerate zero direction without a local inverse"
            ),
        },
        "channels": {},
    }
    for name, jets in (("plus", plus), ("minus_normalized_h", minus)):
        values = certificates(jets)
        output["channels"][name] = {
            key: {
                "expression": str(sp.factor(value)),
                "certificate": sign_certificate(value),
            }
            for key, value in values.items()
        }
    args.output.write_text(json.dumps(output, indent=2) + "\n")
    print(args.output)


if __name__ == "__main__":
    main()

