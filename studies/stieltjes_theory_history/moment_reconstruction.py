#!/usr/bin/env python3
"""Deterministic atomic reconstructions from exact Stieltjes moments.

This does not infer a unique underlying measure from finitely many moments.
It constructs the canonical Gaussian quadrature using mu_0,...,mu_3 and the
zero-node Gauss--Radau quadrature using mu_0,...,mu_4.
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


getcontext().prec = 70


def solve2(a: Fraction, b: Fraction, c: Fraction,
           d: Fraction, e: Fraction, f: Fraction) -> tuple[Fraction, Fraction]:
    determinant = a * d - b * c
    if determinant == 0:
        raise ValueError("singular two-by-two moment system")
    return ((e * d - b * f) / determinant,
            (a * f - e * c) / determinant)


def dec(value: Fraction) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


def positive_quadratic_roots(c0: Fraction, c1: Fraction) -> tuple[Decimal, Decimal]:
    discriminant = dec(c1 * c1 - 4 * c0)
    if discriminant <= 0:
        raise ValueError("quadrature polynomial does not have two real roots")
    root = discriminant.sqrt()
    x1 = (-dec(c1) - root) / 2
    x2 = (-dec(c1) + root) / 2
    if x1 < 0 or x2 < 0:
        raise ValueError("quadrature has a negative node")
    return x1, x2


def two_positive_weights(m1: Fraction, m2: Fraction,
                         x1: Decimal, x2: Decimal) -> tuple[Decimal, Decimal]:
    # w1*x1 + w2*x2=m1 and w1*x1^2+w2*x2^2=m2.
    denominator = x1 * x2 * (x2 - x1)
    w1 = (dec(m1) * x2 * x2 - dec(m2) * x2) / denominator
    w2 = (dec(m2) * x1 - dec(m1) * x1 * x1) / denominator
    return w1, w2


def moment_error(nodes: list[Decimal], weights: list[Decimal],
                 moments: list[Fraction], through: int) -> list[str]:
    errors = []
    for order in range(through + 1):
        # Decimal defines 0**0 as invalid, while the order-zero moment uses
        # the conventional polynomial value lambda**0=1 also at lambda=0.
        estimate = sum(weights) if order == 0 else sum(
            w * (x ** order) for x, w in zip(nodes, weights))
        errors.append(str(estimate - dec(moments[order])))
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    raw = json.loads(args.certificate.read_text())
    moments = [Fraction(value) for value in raw["mu"]]
    if len(moments) < 5:
        raise ValueError("the Gaussian and Radau constructions need mu_0,...,mu_4")

    one_node = dec(moments[1] / moments[0])
    one_weight = dec(moments[0])

    # The monic polynomial x^2+c1*x+c0 is orthogonal to 1,x under rho.
    c0, c1 = solve2(moments[0], moments[1], moments[1], moments[2],
                    -moments[2], -moments[3])
    x1, x2 = positive_quadratic_roots(c0, c1)
    w1, w2 = two_positive_weights(moments[1], moments[2], x1, x2)

    # With a fixed node at zero, the two nonzero nodes are Gaussian nodes for
    # the shifted measure lambda*rho.  Thus the same polynomial system uses
    # mu_1,...,mu_4.
    r0, r1 = solve2(moments[1], moments[2], moments[2], moments[3],
                    -moments[3], -moments[4])
    y1, y2 = positive_quadratic_roots(r0, r1)
    v1, v2 = two_positive_weights(moments[1], moments[2], y1, y2)
    v0 = dec(moments[0]) - v1 - v2
    if min(v0, v1, v2) < 0:
        raise ValueError("zero-node Radau reconstruction has a negative weight")

    result = {
        "warning": "Finite moments define canonical atomic surrogates, not a unique true measure.",
        "one_atom_two_moments": {
            "nodes": [str(one_node)],
            "weights": [str(one_weight)],
            "moment_errors_0_through_1": moment_error(
                [one_node], [one_weight], moments, 1),
        },
        "two_atom_gauss_four_moments": {
            "nodes": [str(x1), str(x2)],
            "weights": [str(w1), str(w2)],
            "moment_errors_0_through_3": moment_error(
                [x1, x2], [w1, w2], moments, 3),
        },
        "three_atom_zero_radau_five_moments": {
            "nodes": ["0", str(y1), str(y2)],
            "weights": [str(v0), str(v1), str(v2)],
            "normalized_weights": [str(v / dec(moments[0])) for v in (v0, v1, v2)],
            "moment_errors_0_through_4": moment_error(
                [Decimal(0), y1, y2], [v0, v1, v2], moments, 4),
            "orthogonal_polynomial_exact": {
                "constant": f"{r0.numerator}/{r0.denominator}",
                "linear": f"{r1.numerator}/{r1.denominator}",
            },
        },
    }
    encoded = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
