#!/usr/bin/env python3
"""Exact shifted 3x3 mu-Hankel threshold after the certified D11 jet."""
from fractions import Fraction
from math import factorial
import sys


def mul(a, b, n):
    c = [Fraction(0) for _ in range(n + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= n:
                c[i+j] += x*y
    return c


def compose_even_k(F, target, n):
    """Solve sum_j k_j F(t)^(2j) = target(t), through t^(2n)."""
    F2 = mul(F, F, 2*n)
    powers = [[Fraction(1)] + [Fraction(0)]*(2*n)]
    for _ in range(n):
        powers.append(mul(powers[-1], F2, 2*n))
    k = [target[0]]
    current = [Fraction(0)] * (2*n+1)
    current[0] = k[0]
    for j in range(1, n+1):
        degree = 2*j
        leading = powers[j][degree]
        kj = (target[degree] - current[degree]) / leading
        k.append(kj)
        for q, z in enumerate(powers[j]):
            current[q] += kj*z
    assert current == target
    return k


def det3(m):
    return (m[0][0] * (m[1][1]*m[2][2] - m[1][2]*m[2][1])
            - m[0][1] * (m[1][0]*m[2][2] - m[1][2]*m[2][0])
            + m[0][2] * (m[1][0]*m[2][1] - m[1][1]*m[2][0]))


D9 = sum([
    14627977297920, 4546495309086720, 211436756895006720,
    3490984312448606208, 27185927724027592704,
    114581150906254331904, 277387051973394751488,
    385587855340280672256, 285610646257352368128,
    87101527431460847616,
])
D11 = 291982832387585872335470592
D = [111, 1685184, 77400633120, 7315868433079296, D9, D11]


def determinant(D13):
    coeff = [Fraction(D[i], factorial(2*i+1)) for i in range(6)]
    coeff.append(Fraction(D13, factorial(13)))
    F = [Fraction(0)] * 14
    target = [Fraction(0)] * 13
    for r, ar in enumerate(coeff):
        F[2*r+1] = ar
        target[2*r] = (2*r+1)*ar
    k = compose_even_k(F, target, 6)
    mu = [(-1)**m * k[m+1] for m in range(6)]
    return det3([[mu[i+j+1] for j in range(3)] for i in range(3)]), mu


if __name__ == "__main__":
    A, mu0 = determinant(0)
    d1, _ = determinant(1)
    B = d1-A
    threshold = -A/B
    print("det(D13) = A + B*D13")
    print("A =", A)
    print("B =", B)
    print("B sign =", "negative" if B < 0 else "positive")
    print("D13 threshold =", threshold)
    print("threshold decimal =", float(threshold))
    if len(sys.argv) > 1:
        candidate = int(sys.argv[1])
        value, _ = determinant(candidate)
        print("candidate =", candidate)
        print("candidate exceeds threshold =", Fraction(candidate) > threshold)
        print("det(candidate) =", value)
        print("det numerator =", value.numerator)
        print("det denominator =", value.denominator)
    print("mu(D13=0):")
    for x in mu0:
        print(x)
