"""Exact deterministic check of Gaussian parameter calculus at changing rank.

Uses only rational sparse-polynomial arithmetic and independent scalar Gaussian
moments. It is an algebraic check, not a training experiment or a proof of the
uniform neural estimates. Run with --output in the study's generated namespace.
"""

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform


ZERO = (0, 0, 0, 0)  # s, t, x0, x1 (or g0, g1 after substitution)


def add(*polys):
    result = {}
    for poly in polys:
        for exponent, coefficient in poly.items():
            result[exponent] = result.get(exponent, Fraction(0)) + coefficient
    return {e: c for e, c in result.items() if c}


def scale(poly, factor):
    return {e: c * factor for e, c in poly.items() if c * factor}


def mul(left, right):
    result = {}
    for a, ca in left.items():
        for b, cb in right.items():
            e = tuple(x + y for x, y in zip(a, b))
            result[e] = result.get(e, Fraction(0)) + ca * cb
    return {e: c for e, c in result.items() if c}


def power(poly, exponent):
    result = {ZERO: Fraction(1)}
    for _ in range(exponent):
        result = mul(result, poly)
    return result


def diff(poly, coordinate):
    result = {}
    for e, c in poly.items():
        if e[coordinate]:
            ee = list(e)
            ee[coordinate] -= 1
            result[tuple(ee)] = c * e[coordinate]
    return result


def normal_moment(exponent):
    if exponent % 2:
        return 0
    result = 1
    for k in range(1, exponent, 2):
        result *= k
    return result


def expectation(poly):
    # Independent oracle: substitute X=(G0+s G1, G0+t G1) and integrate
    # monomials in two independent standard normals. No covariance derivative
    # identity or Wick-pairing implementation is used in this calculation.
    x0 = {(0, 0, 1, 0): Fraction(1), (1, 0, 0, 1): Fraction(1)}
    x1 = {(0, 0, 1, 0): Fraction(1), (0, 1, 0, 1): Fraction(1)}
    terms = []
    for (a, b, c, d), coefficient in poly.items():
        expanded = mul({(a, b, 0, 0): coefficient},
                       mul(power(x0, c), power(x1, d)))
        for (aa, bb, gg, hh), value in expanded.items():
            terms.append({(aa, bb, 0, 0):
                          value * normal_moment(gg) * normal_moment(hh)})
    return add(*terms)


def run():
    one = {ZERO: Fraction(1)}
    covariance = [
        [add(one, {(2, 0, 0, 0): Fraction(1)}),
         add(one, {(1, 1, 0, 0): Fraction(1)})],
        [add(one, {(1, 1, 0, 0): Fraction(1)}),
         add(one, {(0, 2, 0, 0): Fraction(1)})],
    ]
    observables = [
        {(0, 0, 4, 2): Fraction(1), (0, 0, 2, 2): Fraction(1),
         (1, 1, 2, 2): Fraction(1), (1, 0, 4, 0): Fraction(1),
         (0, 1, 0, 2): Fraction(1)},
        {(1, 0, 1, 1): Fraction(1), (0, 2, 1, 1): Fraction(1),
         (0, 0, 3, 3): Fraction(1)},
    ]
    checks = []
    for number, q in enumerate(observables):
        for parameter in (0, 1):
            rhs = expectation(diff(q, parameter))
            for i in range(2):
                for j in range(2):
                    rhs = add(rhs, scale(mul(
                        diff(covariance[i][j], parameter),
                        expectation(diff(diff(q, i + 2), j + 2))), Fraction(1, 2)))
            direct = diff(expectation(q), parameter)
            assert rhs == direct, (number, parameter, rhs, direct)
            checks.append(f"observable {number}: first derivative {parameter}")
        rhs = expectation(diff(diff(q, 0), 1))
        for i in range(2):
            for j in range(2):
                qij = diff(diff(q, i + 2), j + 2)
                rhs = add(rhs, scale(mul(diff(diff(covariance[i][j], 0), 1),
                                        expectation(qij)), Fraction(1, 2)))
                for a, b in ((0, 1), (1, 0)):
                    rhs = add(rhs, scale(mul(diff(covariance[i][j], a),
                        expectation(diff(qij, b))), Fraction(1, 2)))
                for k in range(2):
                    for l in range(2):
                        rhs = add(rhs, scale(mul(
                            mul(diff(covariance[i][j], 0),
                                diff(covariance[k][l], 1)),
                            expectation(diff(diff(qij, k + 2), l + 2))),
                            Fraction(1, 4)))
        direct = diff(diff(expectation(q), 0), 1)
        assert rhs == direct, (number, rhs, direct)
        checks.append(f"observable {number}: mixed second derivative")
    return {
        "status": "PASS", "checks": checks,
        "covariance": "[[1+s^2,1+st],[1+st,1+t^2]]; determinant (s-t)^2",
        "coverage": "Polynomial identities for every s,t, including the rank-one line s=t.",
        "method": "Exact rational arithmetic; independent-normal substitution oracle.",
        "limitation": "Checks algebraic covariance differentiation factors only; no neural bound is inferred.",
        "python": platform.python_version(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    report = run()
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
