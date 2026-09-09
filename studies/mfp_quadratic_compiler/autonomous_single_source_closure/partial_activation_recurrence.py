#!/usr/bin/env python3
"""Exact fixed-order Gaussian recurrences for partially quadratic depth two.

The three modes are

``inner``
    phi_1(u)=u^2 and phi_2(z)=z;
``outer``
    phi_1(u)=u and phi_2(z)=z^2;
``both``
    phi_1(u)=u^2 and phi_2(z)=z^2 (the canonical control).

The calculation is the coefficient form of the exact rank-one elimination
of the moving middle matrix, followed by Gaussian detransposition.  It is a
fixed-order width-limit calculation, not a positive-time closure theorem.
All arithmetic is exact.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction


Rat = Fraction
Monomial = tuple[int, ...]
Polynomial = dict[Monomial, Rat]


def variable(index: int, dimension: int, exponent: int = 1) -> Polynomial:
    powers = [0] * dimension
    powers[index] = exponent
    return {tuple(powers): Rat(1)}


def add_scaled(target: Polynomial, source: Polynomial, scalar: Rat) -> None:
    if not scalar:
        return
    for monomial, coefficient in source.items():
        value = target.get(monomial, Rat(0)) + scalar * coefficient
        if value:
            target[monomial] = value
        else:
            target.pop(monomial, None)


def scale(source: Polynomial, scalar: Rat) -> Polynomial:
    return {
        monomial: scalar * coefficient
        for monomial, coefficient in source.items()
        if scalar * coefficient
    }


def product(left: Polynomial, right: Polynomial) -> Polynomial:
    if len(left) > len(right):
        left, right = right, left
    answer: Polynomial = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            monomial = tuple(a + b for a, b in zip(lm, rm))
            value = answer.get(monomial, Rat(0)) + lc * rc
            if value:
                answer[monomial] = value
            else:
                answer.pop(monomial, None)
    return answer


def convolution(
    left: list[Polynomial], right: list[Polynomial], degree: int
) -> Polynomial:
    answer: Polynomial = {}
    for p in range(degree + 1):
        add_scaled(answer, product(left[p], right[degree - p]), Rat(1))
    return answer


class GaussianLaw:
    def __init__(self, dimension: int) -> None:
        self.dimension = dimension
        self.covariance = [
            [Rat(0) for _ in range(dimension)] for _ in range(dimension)
        ]
        self.covariance[0][0] = Rat(1)
        self.cache: dict[Monomial, Rat] = {(0,) * dimension: Rat(1)}

    def install_covariance(self, index: int, values: list[Rat]) -> None:
        if len(values) != index:
            raise ValueError("wrong covariance-row length")
        for other in range(1, index + 1):
            value = values[other - 1]
            self.covariance[index][other] = value
            self.covariance[other][index] = value

    def moment(self, powers: Monomial) -> Rat:
        cached = self.cache.get(powers)
        if cached is not None:
            return cached
        if sum(powers) & 1:
            self.cache[powers] = Rat(0)
            return Rat(0)
        left = next(i for i, power in enumerate(powers) if power)
        remainder = list(powers)
        remainder[left] -= 1
        answer = Rat(0)
        for right, multiplicity in enumerate(remainder):
            covariance = self.covariance[left][right]
            if multiplicity and covariance:
                remainder[right] -= 1
                answer += (
                    multiplicity * covariance * self.moment(tuple(remainder))
                )
                remainder[right] += 1
        self.cache[powers] = answer
        return answer

    def inner(self, left: Polynomial, right: Polynomial) -> Rat:
        return sum(
            lc
            * rc
            * self.moment(tuple(a + b for a, b in zip(lm, rm)))
            for lm, lc in left.items()
            for rm, rc in right.items()
        )

    def expected_partial(self, polynomial: Polynomial, index: int) -> Rat:
        answer = Rat(0)
        for monomial, coefficient in polynomial.items():
            multiplicity = monomial[index]
            if multiplicity:
                powers = list(monomial)
                powers[index] -= 1
                answer += multiplicity * coefficient * self.moment(tuple(powers))
        return answer


def symmetric(rows: list[list[Rat]], left: int, right: int) -> Rat:
    return rows[left][right] if left >= right else rows[right][left]


def recurrence(mode: str, max_order: int) -> list[int]:
    if mode not in {"inner", "outer", "both"}:
        raise ValueError(mode)
    dimension = max_order + 2
    row = GaussianLaw(dimension)
    column = GaussianLaw(dimension)
    A = [variable(0, dimension)]
    X = [variable(0, dimension, 2 if mode in {"inner", "both"} else 1)]
    Y: list[Polynomial] = []
    Z: list[Polynomial] = []
    B: list[Polynomial] = []
    Q: list[Polynomial] = []
    R: list[Polynomial] = []
    xx: list[list[Rat]] = []
    bb: list[list[Rat]] = []
    memory_factor = Rat(1 if mode == "inner" else 2)

    for k in range(max_order + 1):
        if k:
            if mode == "inner":
                A.append(scale(Z[k - 1], Rat(1, k)))
                xk: Polynomial = {}
                for p in range(k):
                    add_scaled(xk, product(X[p], R[k - 1 - p]), Rat(4, k))
                X.append(xk)
            else:
                ak: Polynomial = {}
                for p in range(k):
                    add_scaled(ak, product(Z[p], Z[k - 1 - p]), Rat(1, k))
                A.append(ak)
                if mode == "outer":
                    X.append(scale(R[k - 1], Rat(2, k)))
                else:
                    xk = {}
                    for p in range(k):
                        add_scaled(
                            xk, product(X[p], R[k - 1 - p]), Rat(8, k)
                        )
                    X.append(xk)

        xx_row = [column.inner(X[k], X[j]) for j in range(k + 1)]
        xx.append(xx_row)
        row.install_covariance(k + 1, xx_row)

        y = variable(k + 1, dimension)
        for j in range(k):
            add_scaled(y, B[j], column.expected_partial(X[k], j + 1))
        Y.append(y)

        z = dict(y)
        for p in range(k):
            remaining = k - 1 - p
            weight = Rat(0)
            for q in range(remaining + 1):
                rr = remaining - q
                weight += memory_factor * symmetric(xx, q, rr) / (p + q + 1)
            add_scaled(z, B[p], weight)
        Z.append(z)

        if mode == "inner":
            B.append(dict(A[k]))
        else:
            B.append(convolution(A, Z, k))

        bb_row = [row.inner(B[k], B[j]) for j in range(k + 1)]
        bb.append(bb_row)
        column.install_covariance(k + 1, bb_row)

        qpoly = variable(k + 1, dimension)
        for j in range(k + 1):
            add_scaled(qpoly, X[j], row.expected_partial(B[k], j + 1))
        Q.append(qpoly)

        rpoly = dict(qpoly)
        for p in range(k):
            remaining = k - 1 - p
            weight = Rat(0)
            for q in range(remaining + 1):
                rr = remaining - q
                weight += memory_factor * symmetric(bb, q, rr) / (p + q + 1)
            add_scaled(rpoly, X[p], weight)
        R.append(rpoly)

    derivatives: list[int] = []
    for k in range(max_order + 1):
        coefficient = Rat(0)
        if mode == "inner":
            for p in range(k + 1):
                coefficient += row.inner(A[p], Z[k - p])
        else:
            for p in range(k + 1):
                for q in range(k - p + 1):
                    coefficient += row.inner(
                        A[p], product(Z[q], Z[k - p - q])
                    )
        derivative = math.factorial(k) * coefficient
        if derivative.denominator != 1:
            raise ArithmeticError((mode, k, derivative))
        derivatives.append(derivative.numerator)
    return derivatives


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("inner", "outer", "both"), required=True)
    parser.add_argument("--max-order", type=int, default=9)
    args = parser.parse_args()
    values = recurrence(args.mode, args.max_order)
    print(json.dumps({"mode": args.mode, "derivatives": values}, indent=2))


if __name__ == "__main__":
    main()
