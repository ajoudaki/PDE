#!/usr/bin/env python3
"""Exact cubic-invariant comparison for normalized polynomial activations.

This is deliberately independent of the order-five jet machinery.  All
arithmetic is Fraction arithmetic.  For a rational raw polynomial r, the
normalization psi=r/sqrt(E r(G)^2) only contributes even powers of the
square root to the L=1 and L=2 cubic invariants, so their values are
rational.
"""

from fractions import Fraction as Q
from itertools import product


def add(a, b):
    n = max(len(a), len(b))
    return tuple((a[i] if i < len(a) else Q(0)) +
                 (b[i] if i < len(b) else Q(0)) for i in range(n))


def mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return tuple(out)


def derivative(a, order=1):
    a = tuple(a)
    for _ in range(order):
        a = tuple((i+1)*a[i+1] for i in range(len(a)-1))
    return a or (Q(0),)


def gmoment(k):
    if k % 2:
        return 0
    ans = 1
    for j in range(1, k, 2):
        ans *= j
    return ans


def expect(a):
    return sum(x*gmoment(i) for i, x in enumerate(a))


def raw_product_moment(raw, derivative_orders):
    p = (Q(1),)
    for r in derivative_orders:
        p = mul(p, derivative(raw, r))
    return expect(p)


def normalized_moment(raw, derivative_orders):
    # Every use below has an even number of activation factors.
    k = len(derivative_orders)
    assert k % 2 == 0
    norm2 = raw_product_moment(raw, (0, 0))
    assert norm2 > 0
    return raw_product_moment(raw, derivative_orders) / norm2**(k//2)


def invariants(raw):
    M = lambda *orders: normalized_moment(raw, orders)
    # Shared atoms.
    d = M(1, 1)
    e4 = M(1, 1, 1, 1)
    m = M(0, 2, 1, 1)
    j = M(3, 1, 1, 1)
    ss = M(2, 2, 1, 1)
    ell = M(0, 0, 1, 1)
    b = M(0, 2)
    r = M(1, 3)
    v = M(2, 2)

    j1 = 3*j + 11*m + 4*e4 + 4*ell + 12*ss

    c = 1 + d
    beta = b + c*r
    delta = d + c*v
    k = d + beta + delta
    S = (3*c*c*m + 3*c**3*j + 3*d*e4*beta +
         3*d*k*m + 3*d*d*j)
    H = (c*c*e4 + c*ell + 2*c*c*m + 3*c**3*ss +
         c*e4*d*v + 2*e4*d*d + 3*d*d*ss +
         k*k*ell + 2*d*k*m)
    j2 = S + 4*H
    return j1, j2


def fmt(raw):
    return " + ".join(f"({c})x^{i}" for i, c in enumerate(raw) if c) or "0"


def main():
    found = []
    # Constant through quartic, excluding affine activations.  Quotient out
    # common integer scaling by fixing the leading coefficient to one.
    for degree in (2, 3, 4):
        for lower in product(range(-3, 4), repeat=degree):
            raw = tuple(map(Q, lower + (1,)))
            if raw_product_moment(raw, (0, 0)) == 0:
                continue
            j1, j2 = invariants(raw)
            if j2 < j1:
                found.append((degree, raw, j1, j2, j2-j1))
                print("COUNTEREXAMPLE", fmt(raw))
                print("J1 =", j1)
                print("J2 =", j2)
                print("J2-J1 =", j2-j1)
                break
        if found:
            break
    if not found:
        print("No J2<J1 example found in searched box")

    # Report a few sign-indefinite examples in either direction.
    for raw in ((Q(0),Q(1),Q(-1),Q(1)),
                (Q(0),Q(1),Q(1),Q(-1)),
                (Q(1),Q(-2),Q(1),Q(1)),
                (Q(0),Q(1),Q(-2),Q(1),Q(1))):
        j1,j2=invariants(raw)
        print("SAMPLE", fmt(raw), "J1", j1, "J2", j2, "diff", j2-j1)


if __name__ == "__main__":
    main()
