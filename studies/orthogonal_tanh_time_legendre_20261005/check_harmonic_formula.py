"""Exact algebra checks for RESULT.md; no network simulation or random data."""

from fractions import Fraction as F
from math import comb, factorial


def eigenvalue(d, p, k):
    if p < k or (p - k) % 2:
        return F(0)
    rising = F(1)
    for j in range((p + k) // 2):
        rising *= F(d, 2) + j
    return F(factorial(p), 2**p * factorial((p - k) // 2)) / rising


def legendre_polynomials(degree):
    polys = [[F(1)], [F(0), F(1)]]
    for k in range(2, degree + 1):
        poly = [F(0)] * (k + 1)
        for j, value in enumerate(polys[-1]):
            poly[j + 1] += F(2 * k - 1, k) * value
        for j, value in enumerate(polys[-2]):
            poly[j] -= F(k - 1, k) * value
        polys.append(poly)
    return polys


def run():
    checks = 0
    # On the circle the answer is a binomial Fourier coefficient.
    for p in range(33):
        for k in range(33):
            direct = F(0)
            if p >= k and (p - k) % 2 == 0:
                direct = F(comb(p, (p - k) // 2), 2**p)
            assert eigenvalue(2, p, k) == direct, (2, p, k)
            checks += 1

    # On S^2 integrate the independently generated Legendre polynomial.
    for k, polynomial in enumerate(legendre_polynomials(32)):
        for p in range(33):
            direct = sum(
                (value / (p + j + 1)
                 for j, value in enumerate(polynomial) if (p + j) % 2 == 0),
                F(0),
            )
            assert eigenvalue(3, p, k) == direct, (3, p, k)
            checks += 1

    # Check the telescoping quotient used in the lower bound.
    for d in range(2, 13):
        for p in range(1, 64, 2):
            q = (p - 1) // 2
            for k in range(1, p + 1, 2):
                product = F(1)
                for r in range((k - 1) // 2):
                    product *= F(q - r) / (F(q + 1 + r) + F(d, 2))
                assert eigenvalue(d, p, k) == eigenvalue(d, p, 1) * product
                checks += 1

    # Low-degree normalization checks in every inspected dimension.
    for d in range(2, 13):
        assert eigenvalue(d, 1, 1) == F(1, d)
        assert eigenvalue(d, 3, 1) == F(3, d * (d + 2))
        assert eigenvalue(d, 3, 3) == F(6, d * (d + 2) * (d + 4))
        checks += 3
    print(f"PASS: {checks} exact rational identities; no trained-network experiment.")


if __name__ == "__main__":
    run()
