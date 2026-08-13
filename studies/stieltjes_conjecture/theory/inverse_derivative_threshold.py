#!/usr/bin/env python3
"""Exact h-Hankel threshold using only F through t^11."""
from fractions import Fraction
from math import factorial


def mul(a, b, n):
    c = [Fraction(0) for _ in range(n + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= n:
                c[i + j] += x * y
    return c


def inv(a, n):
    b = [Fraction(0) for _ in range(n + 1)]
    b[0] = 1 / a[0]
    for k in range(1, n + 1):
        b[k] = -sum(a[j] * b[k-j] for j in range(1, min(k, len(a)-1)+1)) / a[0]
    return b


def power(a, exponent, n):
    assert exponent < 0
    base = inv(a, n)
    out = [Fraction(1)] + [Fraction(0)] * n
    for _ in range(-exponent):
        out = mul(out, base, n)
    return out


def det3(m):
    return (m[0][0] * (m[1][1]*m[2][2] - m[1][2]*m[2][1])
            - m[0][1] * (m[1][0]*m[2][2] - m[1][2]*m[2][0])
            + m[0][2] * (m[1][0]*m[2][1] - m[1][1]*m[2][0]))


D = [
    111,
    1685184,
    77400633120,
    7315868433079296,
    sum([
        14627977297920, 4546495309086720, 211436756895006720,
        3490984312448606208, 27185927724027592704,
        114581150906254331904, 277387051973394751488,
        385587855340280672256, 285610646257352368128,
        87101527431460847616,
    ]),
]


def h_values(D11):
    phi = [Fraction(D[r], factorial(2*r+1)) for r in range(5)]
    phi.append(Fraction(D11, factorial(11)))
    return [(-1)**n * power(phi, -(2*n+1), n)[n] for n in range(6)]


def determinant(D11):
    h = h_values(D11)
    return det3([[h[i+j+1] for j in range(3)] for i in range(3)])


if __name__ == "__main__":
    A = determinant(0)
    B = determinant(1) - A
    threshold = -A / B
    print("D9 =", D[4])
    print("det(D11) = A + B*D11")
    print("A =", A)
    print("B =", B)
    print("B sign =", "negative" if B < 0 else "positive")
    print("D11 threshold =", threshold)
    print("threshold decimal =", float(threshold))
    for cap, z in [
        (2, 47549726635753458892800),
        (4, 3307693726260619821416448),
        (6, 19137221983807142685401088),
        (8, 52323627265312021203603456),
        (10, 92313546074432999279050752),
        (12, 135235415744792683804366848),
        (14, 171581079093364877390972928),
    ]:
        print(cap, z, "negative_certificate", Fraction(z) > threshold)
