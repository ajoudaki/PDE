#!/usr/bin/env python3
"""Exact low-horizon audit of the scalar all-order obstruction."""

from collections import defaultdict
from fractions import Fraction as Q

# monomial key: (h, A0, Z0, p, q)


def add(*polys):
    out = defaultdict(Q)
    for poly in polys:
        for key, value in poly.items():
            out[key] += value
    return {key: value for key, value in out.items() if value}


def scale(poly, coefficient):
    return {key: coefficient * value for key, value in poly.items() if value}


def mul(left, right):
    out = defaultdict(Q)
    for x, c in left.items():
        for y, d in right.items():
            out[tuple(a + b for a, b in zip(x, y))] += c * d
    return {key: value for key, value in out.items() if value}


def mono(h=0, a=0, z=0, p=0, q=0, c=1):
    return {(h, a, z, p, q): Q(c)}


H = mono(h=1)
P = mono(p=1)
QVAR = mono(q=1)
A0 = mono(a=1)
Z0 = mono(z=1)


def step(a, z, step_scale=1):
    phi_z = add(mul(P, z), mul(QVAR, mul(z, z)))
    dphi_z = add(P, scale(mul(QVAR, z), 2))
    hs = scale(H, step_scale)
    return add(a, mul(hs, phi_z)), add(z, mul(hs, mul(a, dphi_z)))


def output(a, z):
    return mul(a, add(mul(P, z), mul(QVAR, mul(z, z))))


def horizon(n, step_scale=1):
    a, z = A0, Z0
    for _ in range(n):
        a, z = step(a, z, step_scale)
    return output(a, z)


def gaussian_moment(power):
    if power % 2:
        return 0
    answer = 1
    for k in range(1, power, 2):
        answer *= k
    return answer


def expected(poly):
    out = defaultdict(Q)
    for (h, a, z, p, q), coefficient in poly.items():
        coefficient *= gaussian_moment(a) * gaussian_moment(z)
        if coefficient:
            out[(h, p, q)] += coefficient
    return dict(out)


def main():
    for t in (1, 2):
        fine = horizon(2 * t, 1)
        coarse = horizon(t, 2)
        defect = add(fine, scale(coarse, -1))
        assert all(value >= 0 for value in defect.values())
        expected_defect = expected(defect)
        assert all(value >= 0 for value in expected_defect.values())

        top_h = 3 * (2 ** (2 * t) - 1)
        top = {
            key: value for key, value in expected_defect.items()
            if key[0] == top_h
        }
        assert top and all(value > 0 for value in top.values())
        assert all(h <= 3 * (2**t - 1) for h, _, _ in expected(coarse))
        print(f"t={t}: positivity/top-degree audit PASS; top={top}")


if __name__ == "__main__":
    main()
