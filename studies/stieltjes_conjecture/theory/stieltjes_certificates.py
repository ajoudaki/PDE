#!/usr/bin/env python3
"""Create exact rational K, moment, and Hankel-determinant certificates."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def mul(a: list[Fraction], b: list[Fraction], degree: int) -> list[Fraction]:
    out = [Fraction(0) for _ in range(degree + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= degree:
                out[i + j] += x * y
    return out


def power(a: list[Fraction], exponent: int, degree: int) -> list[Fraction]:
    out = [Fraction(1)] + [Fraction(0)] * degree
    base = a[:degree + 1] + [Fraction(0)] * max(0, degree + 1 - len(a))
    while exponent:
        if exponent & 1:
            out = mul(out, base, degree)
        base = mul(base, base, degree)
        exponent >>= 1
    return out


def det_bareiss(a: list[list[Fraction]]) -> Fraction:
    n = len(a)
    if n == 0:
        return Fraction(1)
    z = [row[:] for row in a]
    sign = 1
    prev = Fraction(1)
    for k in range(n - 1):
        if z[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if z[i][k]), None)
            if swap is None:
                return Fraction(0)
            z[k], z[swap] = z[swap], z[k]
            sign *= -1
        pivot = z[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                z[i][j] = (z[i][j] * pivot - z[i][k] * z[k][j]) / prev
        prev = pivot
    return sign * z[n - 1][n - 1]


def fs(q: Fraction) -> str:
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def compute(derivatives: list[int]) -> dict:
    max_r = (len(derivatives) - 2) // 2
    a = [Fraction(derivatives[2*r + 1], math.factorial(2*r + 1)) for r in range(max_r + 1)]

    # Work in z=t^2.  F(t)^2 = z A(z)^2, and
    # F'(t) = sum_r (2r+1)a_r z^r.
    A = a[:]
    F2 = [Fraction(0)] + mul(A, A, max_r - 1)
    kappa = [a[0]]
    known = [kappa[0]] + [Fraction(0)] * max_r
    for m in range(1, max_r + 1):
        pm = power(F2, m, max_r)
        rhs = Fraction((2*m + 1)) * a[m] - known[m]
        km = rhs / pm[m]
        kappa.append(km)
        for j in range(max_r + 1):
            known[j] += km * pm[j]

    mu = [((-1) ** m) * kappa[m + 1] for m in range(len(kappa) - 1)]
    ordinary = []
    shifted = []
    d = 1
    while 2*d - 2 < len(mu):
        ordinary.append(det_bareiss([[mu[i+j] for j in range(d)] for i in range(d)]))
        d += 1
    d = 1
    while 2*d - 1 < len(mu):
        shifted.append(det_bareiss([[mu[i+j+1] for j in range(d)] for i in range(d)]))
        d += 1

    return {
        "a": [fs(v) for v in a],
        "kappa_K_even_coefficients": [fs(v) for v in kappa],
        "mu": [fs(v) for v in mu],
        "ordinary_hankel_determinants": [fs(v) for v in ordinary],
        "shifted_hankel_determinants": [fs(v) for v in shifted],
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("derivatives_json", type=Path)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    raw = json.loads(args.derivatives_json.read_text())
    result = compute([int(v) for v in raw["derivatives"]])
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
        print(hashlib.sha256(encoded.encode()).hexdigest())
    print(encoded, end="")


if __name__ == "__main__":
    main()
