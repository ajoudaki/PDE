"""Deterministic supplementary checks for isolated promotion review A, v1.

These are boundary/algebra checks, not substitutes for the report's proofs.
Run with the Python standard library only.
"""
from fractions import Fraction as F
import math

K = 19
# For scalar source ascent with B0=W0=1, c0=0, c'=1+c^2.
c = [F(0)] * (K + 2)
for k in range(K + 1):
    c[k + 1] = (F(k == 0) + sum(c[i] * c[k - i] for i in range(k + 1))) / (k + 1)
source = [sum(c[i] * (k - i + 1) * c[k - i + 1]
              for i in range(k + 1)) for k in range(K + 1)]


def product(x, y):
    return [sum(x[i] * y[k - i] for i in range(k + 1)) for k in range(K + 1)]


def compose(poly, s):
    ans = [F(0)] * (K + 1)
    power = [F(1)] + [F(0)] * K
    for a in poly:
        ans = [x + a * y for x, y in zip(ans, power)]
        power = product(power, s)
    return ans


def physical(poly):
    # Each model uses its own source clock: s'=1-F(s), s(0)=0.
    s = [F(0)] * (K + 1)
    for k in range(K):
        out = compose(poly, s)
        s[k + 1] = (F(k == 0) - out[k]) / (k + 1)
    return compose(poly, s)


dense = physical(source)
for q in range(2, 13):
    closure = physical(source[:q])
    diff = [a - b for a, b in zip(dense, closure)]
    j = next(k for k, a in enumerate(diff) if a)
    assert j == 2 * (q // 2) + 1 and diff[j] == source[j]
    print("q", q, "first_difference", j, "coefficient", str(diff[j]), "own_feedback_check PASS")

x = 1 / 4096
xa = 1 / 512
print("analytic_self_map", 64 * ((1 - xa) ** -3 - 1),
      "analytic_lipschitz", 96 * xa / (1 - xa) ** 4)
print("real_self_map_factor", 64 * ((1 - x) ** -3 - 1),
      "real_lipschitz", 96 * x / (1 - x) ** 4)
print("tail_amplification", (1 + x) / (1 - x) ** 3 / (1 - 96 * x / (1 - x) ** 4))
for j in range(3, 1000, 2):
    assert (j + 1) * (j + 2) <= 4 ** j
    k = (j - 1) // 2
    assert F((k + 1) ** 2, 2 * 12 ** k) >= F(1, 8 ** j)
print("odd-order constant inequalities j=3..999 PASS")

for rho in (1 / 64, 1e-8, 1e-100):
    theta = rho * (2 ** -13) / 8
    kap = 16 * (1 + math.log(1 / theta) + math.log(8 / 3))
    for j in (1, 2, 3, 10, 100, 1000):
        N = math.ceil(kap * j)
        logratio = (math.log(8 / 3) + (2 * j + 1) * math.log(N)
                    - j * math.log(theta) - 2 * math.lgamma(j + 1) - N * math.log(4))
        assert logratio < 0
print("analytic-transfer tail comparisons for 18 cases PASS")
