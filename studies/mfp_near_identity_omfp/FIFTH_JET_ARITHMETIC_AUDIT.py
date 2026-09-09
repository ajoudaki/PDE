"""Exact rational checks for FIFTH_JET_POLYNOMIAL_THEOREM.md."""

from fractions import Fraction as Q
from math import comb


def matmul(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def padd(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return out


def pscale(a, c):
    return [c * x for x in a]


def ptrim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def pmul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def binomial_polynomial(scale, degree):
    """Coefficients of binom(scale*t, degree), in ascending powers of t."""
    out = [Q(1)]
    for j in range(degree):
        out = pmul(out, [Q(-j), Q(scale)])
    return pscale(out, Q(1, 1 if degree == 0 else 1) / Q(factorial(degree)))


def factorial(n):
    out = 1
    for j in range(2, n + 1):
        out *= j
    return out


V = [[Q(m**d) for d in range(1, 6)] for m in range(1, 6)]
Vinv = [
    [Q(5), Q(-5), Q(10, 3), Q(-5, 4), Q(1, 5)],
    [Q(-77, 12), Q(107, 12), Q(-13, 2), Q(61, 24), Q(-5, 12)],
    [Q(71, 24), Q(-59, 12), Q(49, 12), Q(-41, 24), Q(7, 24)],
    [Q(-7, 12), Q(13, 12), Q(-1), Q(11, 24), Q(-1, 12)],
    [Q(1, 24), Q(-1, 12), Q(1, 12), Q(-1, 24), Q(1, 120)],
]

identity = [[Q(i == j) for j in range(5)] for i in range(5)]
assert matmul(Vinv, V) == identity

row_norms = [sum(abs(x) for x in row) for row in Vinv]
assert row_norms == [Q(887, 60), Q(595, 24), Q(335, 24), Q(77, 24), Q(31, 120)]
assert sum(abs(2**d - 32) * row_norms[d - 1] for d in range(1, 5)) == 1524

# Newton step-doubling polynomials d_{5,j}(t)=binom(2t,j)-32 binom(t,j).
d = [
    ptrim(padd(binomial_polynomial(2, j), pscale(binomial_polynomial(1, j), -32)))
    for j in range(1, 6)
]
expected_d = [
    [Q(0), Q(-30)],
    [Q(0), Q(15), Q(-14)],
    [Q(0), Q(-10), Q(14), Q(-4)],
    [Q(0), Q(Q(15, 2)), Q(Q(-77, 6)), Q(6), Q(Q(-2, 3))],
    [Q(0), Q(-6), Q(35, 3), Q(-7), Q(4, 3)],
]
assert d == expected_d

# L=1 identity: [eta^5]F_N=binom(2N,5).
delta_l1 = padd(binomial_polynomial(4, 5), pscale(binomial_polynomial(2, 5), -32))
assert delta_l1 == [Q(0), Q(-12), Q(140, 3), Q(-56), Q(64, 3), Q(0)]

# Independent L=2 identity polynomial quoted in the audit.
# c5(N)=20 C(N,2)+465 C(N,3)+1702 C(N,4)+1464 C(N,5).
c5_l2 = [Q(0)]
for coefficient, degree in [(20, 2), (465, 3), (1702, 4), (1464, 5)]:
    c5_l2 = padd(c5_l2, pscale(binomial_polynomial(1, degree), coefficient))
assert c5_l2 == [Q(0), Q(123, 10), Q(-629, 12), Q(79), Q(-613, 12), Q(61, 5)]

delta_l2 = [Q(0)] * 6
for power, gamma in enumerate(c5_l2):
    delta_l2[power] = gamma * (2**power - 32)
assert delta_l2 == [Q(0), Q(-369), Q(4403, 3), Q(-1896), Q(2452, 3), Q(0)]

print("PASS: inverse Vandermonde, row norms, 1524, Newton polynomials, and L=1/L=2 checks")
