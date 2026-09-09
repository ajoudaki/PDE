#!/usr/bin/env python3
"""Exact sparse frozen recursion for monomial activations x**d.

Used only to audit parity and the highest nonzero Gaussian coefficient.
Polynomials are in (h,A,Z), with integer coefficients.
"""

from collections import defaultdict


def add(*ps):
    out = defaultdict(int)
    for p in ps:
        for m, c in p.items():
            out[m] += c
    return {m: c for m, c in out.items() if c}


def mul(*ps):
    out = {(0, 0, 0): 1}
    for q in ps:
        nxt = defaultdict(int)
        for (i, a, z), c in out.items():
            for (j, b, w), e in q.items():
                nxt[(i + j, a + b, z + w)] += c * e
        out = {m: c for m, c in nxt.items() if c}
    return out


def scale(c, p):
    return {m: c * v for m, v in p.items() if c * v}


def power(p, k):
    out = {(0, 0, 0): 1}
    for _ in range(k):
        out = mul(out, p)
    return out


def gaussian_moment(k):
    if k & 1:
        return 0
    ans = 1
    for j in range(1, k, 2):
        ans *= j
    return ans


def expected_output(d, steps):
    h = {(1, 0, 0): 1}
    a = {(0, 1, 0): 1}
    z = {(0, 0, 1): 1}
    for _ in range(steps):
        old_a, old_z = a, z
        a = add(old_a, mul(h, power(old_z, d)))
        z = add(old_z, scale(d, mul(h, old_a, power(old_z, d - 1))))
    raw = mul(a, power(z, d))
    by_h = defaultdict(int)
    witnesses = defaultdict(list)
    for (k, r, s), c in raw.items():
        value = c * gaussian_moment(r) * gaussian_moment(s)
        if value:
            by_h[k] += value
            witnesses[k].append((r, s, c))
    return dict(by_h), witnesses


if __name__ == "__main__":
    for d in (2, 3, 4, 5):
        for n in (1, 2, 3):
            values, witnesses = expected_output(d, n)
            k = max(values)
            delta = (d**n - 1) // (d - 1)
            formal = (d + 1) * delta
            assert k == formal - (d & 1)
            pairs = {(r, s) for r, s, _ in witnesses[k]}
            if d % 2 == 0:
                assert (d**n, d ** (n + 1)) in pairs
            else:
                assert (d**n + 1, d ** (n + 1) - d) in pairs
                assert (d**n - 1, d ** (n + 1) - d + 2) in pairs
            print(
                f"d={d} N={n} max_expected_h={k} coeff={values[k]} "
                f"num_witnesses={len(witnesses[k])}"
            )
    print("PASS: parity and one-defect formulas through d=5, N=3")
