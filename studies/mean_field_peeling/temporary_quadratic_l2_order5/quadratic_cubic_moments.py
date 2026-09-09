#!/usr/bin/env python3
"""Exact rational cubic invariant for psi_e=(x+e*x^2)/sqrt(1+3e^2).

Every expression is represented as P(y)/(1+3y)^k with y=e^2 and exact
Fraction coefficients.  This script has no third-party dependency.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction


def trim(p: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    q = list(p)
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return tuple(q)


def padd(p, q):
    n = max(len(p), len(q))
    return trim(tuple((p[i] if i < len(p) else 0) +
                      (q[i] if i < len(q) else 0) for i in range(n)))


def pmul(p, q):
    out = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(tuple(out))


def pscale(p, c):
    return trim(tuple(Fraction(c) * a for a in p))


D = (Fraction(1), Fraction(3))


def ppow(p, n):
    out = (Fraction(1),)
    for _ in range(n):
        out = pmul(out, p)
    return out


@dataclass(frozen=True)
class Rat:
    p: tuple[Fraction, ...]
    k: int

    def __add__(self, other: "Rat") -> "Rat":
        k = max(self.k, other.k)
        a = pmul(self.p, ppow(D, k - self.k))
        b = pmul(other.p, ppow(D, k - other.k))
        return Rat(padd(a, b), k)

    def __mul__(self, other: "Rat") -> "Rat":
        return Rat(pmul(self.p, other.p), self.k + other.k)

    def scale(self, c) -> "Rat":
        return Rat(pscale(self.p, c), self.k)


ONE = Rat((Fraction(1),), 0)


def show(name: str, z: Rat) -> None:
    terms = []
    for i, c in enumerate(z.p):
        if not c:
            continue
        terms.append(f"({c})*y^{i}")
    print(f"{name} = ({' + '.join(terms) or '0'})/(1+3y)^{z.k}")


def main() -> None:
    # Direct Gaussian moments; y=e^2.
    d = Rat((1, 4), 1)
    u = Rat((1, 24, 48), 2)
    v = Rat((0, 2), 1)
    # E[g p^2 q] = (10 y + 24 y^2)/(1+3y)^2.
    m = Rat((0, 10, 24), 2)
    s = Rat((0, 4), 1)
    ee = Rat((0, 4, 16), 2)
    # E[g^2 p^2] = (1 + 39 y + 60 y^2)/(1+3y)^2.
    ell = Rat((1, 39, 60), 2)

    c = ONE + d
    beta = v  # r=E[p psi''']=0.
    delta = d + c * s
    kval = d + beta + delta

    S = ((c * c * m).scale(3) +
         (d * u * beta).scale(3) +
         (d * kval * m).scale(3))
    H = (c * c * u + c * ell + (c * c * m).scale(2) +
         (c * c * c * ee).scale(3) + c * u * d * s +
         (u * d * d).scale(2) + (d * d * ee).scale(3) +
         kval * kval * ell + (d * kval * m).scale(2))
    J = S + H.scale(4)

    for name, value in [
        ("d", d), ("u", u), ("v", v), ("m", m), ("s", s),
        ("e_moment", ee), ("ell", ell), ("S", S), ("H", H),
        ("J", J),
    ]:
        show(name, value)

    # Identity control J(0)=48.
    assert J.p[0] == 48


if __name__ == "__main__":
    main()
