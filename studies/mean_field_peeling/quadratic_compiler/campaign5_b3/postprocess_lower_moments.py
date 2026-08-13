#!/usr/bin/env python3
"""Exact post-hoc lower necessary moment signs from accepted jets through F5.

This is intentionally not the preregistered Campaign-5 success test.  It can
certify only mu_0 and mu_1; mu_2 and the first ordinary Hankel determinant
require F^(7)(0), which was not computed.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
STAGE_A = HERE / "frozen" / "stage_a_connected_order3.json"
STAGE_B = HERE / "frozen" / "stage_b_connected_order5.json"
RHO = sp.Symbol("rho")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def polynomial(coefficients: list[str]) -> sp.Poly:
    return sp.Poly(
        sum(sp.Integer(value) * RHO**power
            for power, value in enumerate(coefficients)),
        RHO,
        domain=sp.ZZ,
    )


def exact_string(value: sp.Expr) -> str:
    return str(sp.factor(value))


def interval_certificate(poly: sp.Poly, left: sp.Rational,
                         right: sp.Rational) -> dict[str, object]:
    left_value = poly.eval(left)
    right_value = poly.eval(right)
    roots = int(poly.count_roots(left, right))
    return {
        "interval": [str(left), str(right)],
        "left_value": exact_string(left_value),
        "right_value": exact_string(right_value),
        "left_sign": int(sp.sign(left_value)),
        "right_sign": int(sp.sign(right_value)),
        "distinct_real_root_count": roots,
        "strictly_positive": left_value > 0 and right_value > 0 and roots == 0,
    }


def main() -> None:
    stage_a = json.loads(STAGE_A.read_text())
    stage_b = json.loads(STAGE_B.read_text())
    a_raw = polynomial(stage_a["raw_rho"][1])
    b_raw = polynomial(stage_a["raw_rho"][3])
    c_raw = polynomial(stage_b["raw_rho"][5])
    sign_raw = sp.Poly(4 * b_raw.as_expr() ** 2
                       - a_raw.as_expr() * c_raw.as_expr(), RHO)

    intervals = [(sp.Rational(-1, 2), sp.Rational(0)),
                 (sp.Rational(0), sp.Rational(1))]
    certificates = {
        name: [interval_certificate(poly, left, right)
               for left, right in intervals]
        for name, poly in (
            ("A", a_raw),
            ("B", b_raw),
            ("P", sign_raw),
        )
    }
    assert all(piece["strictly_positive"]
               for pieces in certificates.values() for piece in pieces)

    output = {
        "schema_version": 1,
        "classification": (
            "post-hoc lower necessary Stieltjes signs only; not the "
            "preregistered order-seven Hankel success test"
        ),
        "source_artifacts": {
            str(STAGE_A.relative_to(HERE)): sha256(STAGE_A),
            str(STAGE_B.relative_to(HERE)): sha256(STAGE_B),
        },
        "definitions": {
            "A": "J1",
            "B": "J3",
            "C": "J5",
            "P": "4*B^2-A*C",
            "mu0": "B/(2*A^2)",
            "mu1": "3*P/(8*A^5)",
        },
        "coefficients_ascending": {
            "A": [str(value) for value in reversed(a_raw.all_coeffs())],
            "B": [str(value) for value in reversed(b_raw.all_coeffs())],
            "C": [str(value) for value in reversed(c_raw.all_coeffs())],
            "P": [str(value) for value in reversed(sign_raw.all_coeffs())],
        },
        "sturm_certificates": certificates,
        "conclusions": {
            "A_positive_on_full_domain": True,
            "B_positive_on_full_domain": True,
            "P_positive_on_full_domain": True,
            "mu0_positive_on_full_domain": True,
            "mu1_positive_on_full_domain": True,
            "mu2_available": False,
            "ordinary_H1_available": False,
        },
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()

