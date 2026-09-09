#!/usr/bin/env python3
"""Formal h^5 coefficient of the frozen scalar paired Euler defect.

No symbolic dependency is used. A monomial key is
    (power_h, power_A, power_p0, ..., power_p7).
"""

from fractions import Fraction as Q
from math import factorial

NVAR = 10
H, AVAR = 0, 1
P0 = 2
MAX_H = 5


class Poly:
    def __init__(self, terms=None):
        self.terms = {k: Q(v) for k, v in (terms or {}).items() if v}

    @staticmethod
    def one():
        return Poly({(0,) * NVAR: Q(1)})

    @staticmethod
    def var(index):
        key = [0] * NVAR
        key[index] = 1
        return Poly({tuple(key): Q(1)})

    def __add__(self, other):
        out = self.terms.copy()
        for k, v in other.terms.items():
            out[k] = out.get(k, Q(0)) + v
            if not out[k]:
                del out[k]
        return Poly(out)

    def __neg__(self):
        return self.scale(-1)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        out = {}
        for left, c in self.terms.items():
            for right, d in other.terms.items():
                key = tuple(x + y for x, y in zip(left, right))
                if key[H] <= MAX_H:
                    out[key] = out.get(key, Q(0)) + c * d
        return Poly(out)

    def scale(self, scalar):
        scalar = Q(scalar)
        return Poly({k: scalar * v for k, v in self.terms.items()})

    def power(self, n):
        answer = Poly.one()
        for _ in range(n):
            answer = answer * self
        return answer


h = Poly.var(H)
a = Poly.var(AVAR)
p = [Poly.var(P0 + k) for k in range(8)]


def phi_shift(delta):
    answer = Poly()
    for k in range(7):
        answer = answer + p[k] * delta.power(k).scale(Q(1, factorial(k)))
    return answer


def dphi_shift(delta):
    answer = Poly()
    for k in range(6):
        answer = answer + p[k + 1] * delta.power(k).scale(Q(1, factorial(k)))
    return answer


a1 = a + h * p[0]
dz1 = h * a * p[1]
a2 = a1 + h * phi_shift(dz1)
dz2 = dz1 + h * a1 * dphi_shift(dz1)
f2 = a2 * phi_shift(dz2)

ac = a + h.scale(2) * p[0]
dzc = h.scale(2) * a * p[1]
fc = ac * phi_shift(dzc)


def gaussian_moment(power):
    if power % 2:
        return 0
    answer = 1
    for j in range(1, power, 2):
        answer *= j
    return answer


def expected_coefficient(order):
    answer = {}
    for key, coefficient in (f2 - fc).terms.items():
        if key[H] != order:
            continue
        moment = gaussian_moment(key[AVAR])
        if not moment:
            continue
        pkey = key[P0:]
        answer[pkey] = answer.get(pkey, Q(0)) + coefficient * moment
    return {k: v for k, v in answer.items() if v}


expected = expected_coefficient(5)


def format_monomial(key):
    factors = []
    for i, power in enumerate(key):
        if power:
            factors.append(f"p{i}" if power == 1 else f"p{i}^{power}")
    return "*".join(factors) or "1"


print("H3:")
for key, value in sorted(expected_coefficient(3).items()):
    print(value, format_monomial(key))

print("H5:")
for key in sorted(expected):
    print(expected[key], format_monomial(key))

for key, value in sorted(expected.items()):
    if key[3] >= 2:
        print("P3-SQUARED TERM", value, format_monomial(key))
