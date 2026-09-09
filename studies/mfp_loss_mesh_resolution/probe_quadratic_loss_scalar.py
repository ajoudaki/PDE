#!/usr/bin/env python3
"""Exact-rational frozen scalar population recursion for pure quadratic loss GD.

This is a discovery probe, not a theorem.  It evolves A,Z as polynomials in
independent standard Gaussian A0,Z0 and computes the population residual
exactly after every step.
"""

from fractions import Fraction as Q
import math
import sys


Poly = dict[tuple[int, int], Q]


def add(*xs: Poly) -> Poly:
    out: Poly = {}
    for x in xs:
        for k, v in x.items():
            out[k] = out.get(k, Q(0)) + v
    return {k: v for k, v in out.items() if v}


def scale(c: Q, x: Poly) -> Poly:
    return {k: c * v for k, v in x.items() if c * v}


def mul(x: Poly, y: Poly) -> Poly:
    out: Poly = {}
    for (i, j), a in x.items():
        for (k, ell), b in y.items():
            key = (i + k, j + ell)
            out[key] = out.get(key, Q(0)) + a * b
    return {k: v for k, v in out.items() if v}


def gm(k: int) -> int:
    if k % 2:
        return 0
    ans = 1
    for j in range(1, k, 2):
        ans *= j
    return ans


def expect(x: Poly) -> Q:
    return sum(v * gm(i) * gm(j) for (i, j), v in x.items())


def run(n: int, h: Q, q: Q = Q(1)) -> list[Q]:
    a: Poly = {(1, 0): Q(1)}
    z: Poly = {(0, 1): Q(1)}
    fs = [q * expect(mul(a, mul(z, z)))]
    for _ in range(n):
        lam = h * (1 - fs[-1])
        a, z = (
            add(a, scale(lam * q, mul(z, z))),
            add(z, scale(2 * lam * q, mul(a, z))),
        )
        fs.append(q * expect(mul(a, mul(z, z))))
    return fs


def main() -> None:
    sys.set_int_max_str_digits(1_000_000)
    horizon = Q(sys.argv[1]) if len(sys.argv) > 1 else Q(1, 10)
    max_n = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    for n in range(1, max_n + 1):
        vals = run(n, horizon / n)
        f = vals[-1]
        loss = (1 - f) ** 2 / 2
        logabs = math.log10(abs(f.numerator)) - math.log10(f.denominator) if f else float("-inf")
        fshow = float(f) if logabs < 300 else ("+huge" if f > 0 else "-huge")
        print(n, "coefficient_digits", len(str(abs(f.numerator))), "log10|f|", logabs, "f", fshow, "loss_digits", len(str(loss.numerator)))
        print(" path", [float(x) if abs(x) < 10**100 else ("+huge" if x > 0 else "-huge") for x in vals])


if __name__ == "__main__":
    main()
