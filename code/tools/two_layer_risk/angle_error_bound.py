#!/usr/bin/env python3
"""Exact rational verification of the circle quadrature error bound.

This evaluates derivative majorants, not the scientific coefficient.
All mathematical calculations use integers and fractions. Decimal strings
in the output are explanatory only; the acceptance assertion is exact.
"""
from fractions import Fraction as F
from math import comb, factorial, isqrt
import argparse
import json
from pathlib import Path


def bound(order=8, angles=256):
    n = order
    m = [F(factorial(j)) * F(4, 3)**j for j in range(n + 3)]
    m[:4] = [F(1), F(1), F(1), F(2)]
    mu = []
    for j in range(n + 1):
        if j % 2:
            mu.append(F(4, 5) * 2**((j-1)//2) * factorial((j-1)//2))
        else:
            v = 1
            for a in range(1, j, 2):
                v *= a
            mu.append(F(v))
    stirling = [[0]*(n+1) for _ in range(n+1)]
    stirling[0][0] = 1
    for k in range(1, n+1):
        for j in range(1, k+1):
            stirling[k][j] = stirling[k-1][j-1] + j*stirling[k-1][j]
    normal_l2_products = [F(1)]
    v = 1
    for j in range(1, n+1):
        v *= 2*j-1
        s = isqrt(v)
        normal_l2_products.append(F(s + (s*s != v)))
    sigma = [F(1)] + [sum(m[j]*stirling[k][j]*normal_l2_products[j]
                              for j in range(1, k+1)) for k in range(1, n+1)]
    bell = [[F(0)]*(n+1) for _ in range(n+1)]
    bell[0][0] = F(1)
    for k in range(1, n+1):
        for j in range(1, k+1):
            bell[k][j] = sum(F(comb(k-1, a-1))*sigma[a]*bell[k-a][j-1]
                             for a in range(1, k-j+2))
    lower = [[m[r]] + [sum(m[r+j]*stirling[k][j]*mu[j]
                              for j in range(1, k+1)) for k in range(1, n+1)]
             for r in range(3)]
    upper = [[m[r]] + [sum(m[r+j]*bell[k][j]*mu[j]
                              for j in range(1, k+1)) for k in range(1, n+1)]
             for r in range(3)]
    def product(a, b):
        return [sum(F(comb(k,j))*a[j]*b[k-j] for j in range(k+1))
                for k in range(n+1)]
    g = [F(1)]*(n+1)
    teacher = [F(3**k) for k in range(n+1)]
    v0 = product(lower[0], upper[1])
    v1 = product(g, product(lower[1], upper[1]))
    v2 = product(g, product(lower[2], upper[2]))
    p, beta = F(27, 50), F(1, 10)
    profile = [2*(p**3*(F(20,3)*v0[k] + 12*v1[k] + 4*v2[k]
                                + F(16,3)*upper[0][k])
                   + 2*beta*p*upper[0][k]) for k in range(n+1)]
    derivative = product(teacher, profile)[n]
    # zeta(n) <= 1 + integral_1^infty x^(-n) dx = n/(n-1).
    error = F(2*n, n-1)*derivative / angles**n
    assert error < F(1, 1_000_000), 'Chosen angle rule lacks the declared bound'
    return {'order':n, 'angles':angles, 'beta_required_abs_upper':'1/10',
            'label_abs_sum_upper':'27/50',
            'derivative_upper_exact':str(derivative),
            'angle_error_upper_exact':str(error),
            'angle_error_upper_decimal':format(float(error), '.17g'),
            'declared_angle_error_upper':'1/1000000',
            'arithmetic':'exact integer/Fraction; decimal display is not evidence',
            'status':'PASS, conditional on |beta| <= 1/10'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = bound()
    body = json.dumps(result, indent=2) + '\n'
    if args.output:
        args.output.mkdir(parents=True, exist_ok=False)
        (args.output/'result.json').write_text(body)
    print(body, end='')
