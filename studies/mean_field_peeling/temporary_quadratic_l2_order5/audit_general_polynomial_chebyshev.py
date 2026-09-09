#!/usr/bin/env python3
"""Exact low-horizon audit of (27)--(30) in GENERAL_POLYNOMIAL_DEGREE_AUDIT.

No OMFP compiler is imported.  The scalar Euler recursion is expanded in
Q[h,A,Z], then compared with the independently assembled top formulas.
"""

from collections import defaultdict
from fractions import Fraction as Q
from math import comb


def add(*ps):
    out = defaultdict(Q)
    for p in ps:
        for mon, coeff in p.items():
            out[mon] += coeff
    return {m: c for m, c in out.items() if c}


def scale(c, p):
    c = Q(c)
    return {m: c * v for m, v in p.items() if c * v}


def mul(*ps):
    out = {(0, 0, 0): Q(1)}
    for p in ps:
        nxt = defaultdict(Q)
        for (h, a, z), c in out.items():
            for (i, j, k), v in p.items():
                nxt[(h + i, a + j, z + k)] += c * v
        out = {m: c for m, c in nxt.items() if c}
    return out


def power(p, k):
    out = {(0, 0, 0): Q(1)}
    for _ in range(k):
        out = mul(out, p)
    return out


def compose(coeffs, x):
    return add(*(scale(c, power(x, k)) for k, c in enumerate(coeffs)))


def derivative(coeffs):
    return [Q(k) * coeffs[k] for k in range(1, len(coeffs))]


def gm(k):
    if k & 1:
        return Q(0)
    ans = Q(1)
    for j in range(1, k, 2):
        ans *= j
    return ans


def expectation(p):
    by_h = defaultdict(Q)
    for (h, a, z), c in p.items():
        by_h[h] += c * gm(a) * gm(z)
    return dict(by_h)


def scalar_output(coeffs, steps):
    h = {(1, 0, 0): Q(1)}
    a = {(0, 1, 0): Q(1)}
    z = {(0, 0, 1): Q(1)}
    dp = derivative(coeffs)
    for _ in range(steps):
        old_a, old_z = a, z
        a = add(old_a, mul(h, compose(coeffs, old_z)))
        z = add(old_z, mul(h, old_a, compose(dp, old_z)))
    return expectation(mul(a, compose(coeffs, z)))


def univariate_mul(*ps):
    ans = [Q(1)]
    for p in ps:
        out = defaultdict(Q)
        for i, c in enumerate(ans):
            for j, v in enumerate(p):
                out[i + j] += c * v
        ans = [Q(0)] * (max(out, default=-1) + 1)
        for k, c in out.items():
            ans[k] = c
    return ans


def univariate_power(p, k):
    out = [Q(1)]
    for _ in range(k):
        out = univariate_mul(out, p)
    return out


def gaussian_integral(p):
    return sum(c * gm(k) for k, c in enumerate(p))


def shifted_moment(k, mu):
    return sum(Q(comb(k, j)) * mu ** (k - j) * gm(j) for j in range(k + 1))


def shifted_integral(p, mu):
    return sum(c * shifted_moment(k, mu) for k, c in enumerate(p))


def translate_polynomial(coeffs, mu):
    """Coefficients of P(y-mu)."""
    out = [Q(0)] * len(coeffs)
    for k, c in enumerate(coeffs):
        for j in range(k + 1):
            out[j] += c * Q(comb(k, j)) * (-mu) ** (k - j)
    return out


def gamma_top(d, leading, steps):
    # Coefficients of the top A/Z monomials in formal marks X,Y at time 1.
    ca = Q(1)
    cz = Q(1)
    for _ in range(1, steps):
        ca, cz = leading * cz**d, Q(d) * leading * ca * cz ** (d - 1)
    return leading * ca * cz**d


def predicted(coeffs, steps):
    d = len(coeffs) - 1
    m, n = d ** (steps - 1), d**steps
    gamma = gamma_top(d, coeffs[d], steps)
    p = coeffs
    dp = derivative(coeffs)
    top_z = gaussian_integral(
        univariate_mul(univariate_power(p, m), univariate_power(dp, n))
    )
    top = gamma * gm(n) * top_z
    low1 = gaussian_integral(
        univariate_mul(univariate_power(p, m - 1), univariate_power(dp, n))
    )
    zg = [Q(0), Q(1)]
    low2 = gaussian_integral(
        univariate_mul(
            zg, univariate_power(p, m), univariate_power(dp, n - 1)
        )
    )
    low_base = gamma * (Q(m) * gm(n + 1) * low1 + Q(n) * gm(n - 1) * low2)
    c_sub = coeffs[d - 1]
    low3 = gaussian_integral(
        univariate_mul(univariate_power(p, m), univariate_power(dp, n - 1))
    )
    extra = gamma * Q(m) * c_sub / coeffs[d] * gm(n - 1) * low3
    return top, low_base, extra


def predicted_depressed_odd(coeffs, steps):
    d = len(coeffs) - 1
    assert d % 2 == 1
    mu = coeffs[d - 1] / (Q(d) * coeffs[d])
    p = translate_polynomial(coeffs, mu)
    assert p[d - 1] == 0
    dp = derivative(p)
    m, n = d ** (steps - 1), d**steps
    gamma = gamma_top(d, p[d], steps)
    i1 = shifted_integral(
        univariate_mul(univariate_power(p, m - 1), univariate_power(dp, n)),
        mu,
    )
    zg = [Q(0), Q(1)]
    i2 = shifted_integral(
        univariate_mul(zg, univariate_power(p, m), univariate_power(dp, n - 1)),
        mu,
    )
    return gamma * (Q(m) * gm(n + 1) * i1 + Q(n) * gm(n - 1) * i2)


if __name__ == "__main__":
    cases = [
        ([Q(-5), Q(2), Q(1)], 2),
        ([Q(4), Q(-3), Q(2), Q(1)], 2),
        ([Q(-2), Q(1), Q(-1), Q(2), Q(1)], 2),
    ]
    for coeffs, steps in cases:
        d = len(coeffs) - 1
        delta = (d**steps - 1) // (d - 1)
        degree = (d + 1) * delta
        actual = scalar_output(coeffs, steps)
        top, low_base, extra = predicted(coeffs, steps)
        assert actual.get(degree, Q(0)) == top
        assert actual.get(degree - 1, Q(0)) == low_base + extra
        if d % 2 == 0:
            assert top > 0
        else:
            assert top == 0
            depressed = predicted_depressed_odd(coeffs, steps)
            assert depressed == actual.get(degree - 1, Q(0))
        print(
            f"PASS d={d}, N={steps}, top={top}, "
            f"next_base={low_base}, next_extra={extra}"
        )
