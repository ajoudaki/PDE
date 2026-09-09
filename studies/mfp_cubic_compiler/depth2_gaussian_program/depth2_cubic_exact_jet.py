#!/usr/bin/env python3
"""Exact width-limit feature jet for the raw cubic depth-2 network.

The calculation implements the Gaussian-program/detransposition recurrence
frozen in ``PROTOCOL.md``.  It contains two separately assembled routes:

* ``taylor_jet`` uses ordinary coefficients of powers ``t**k``;
* ``derivative_jet`` uses actual derivatives at zero and explicit
  binomial/multinomial product rules.

Only the sparse-polynomial arithmetic and exact Wick evaluator are shared.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from dataclasses import dataclass
from fractions import Fraction
from typing import Callable, Iterable


Q = Fraction
Monomial = tuple[int, ...]
Polynomial = dict[Monomial, Fraction]
Progress = Callable[[str], None]


def zero_monomial(dimension: int) -> Monomial:
    return (0,) * dimension


def variable(index: int, dimension: int) -> Polynomial:
    powers = [0] * dimension
    powers[index] = 1
    return {tuple(powers): Q(1)}


def add_polynomials(*polynomials: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            result[monomial] = result.get(monomial, Q(0)) + coefficient
    return {
        monomial: coefficient
        for monomial, coefficient in result.items()
        if coefficient
    }


def scale_polynomial(
    polynomial: Polynomial, scalar: int | Fraction
) -> Polynomial:
    scalar = Q(scalar)
    if not scalar or not polynomial:
        return {}
    if scalar == 1:
        return polynomial.copy()
    return {
        monomial: coefficient * scalar
        for monomial, coefficient in polynomial.items()
        if coefficient * scalar
    }


def multiply_polynomials(left: Polynomial, right: Polynomial) -> Polynomial:
    if not left or not right:
        return {}
    result: Polynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(
                left_power + right_power
                for left_power, right_power
                in zip(left_monomial, right_monomial)
            )
            result[monomial] = (
                result.get(monomial, Q(0))
                + left_coefficient * right_coefficient
            )
    return {
        monomial: coefficient
        for monomial, coefficient in result.items()
        if coefficient
    }


class GaussianExpectation:
    """Exact Wick expectation for a chronologically growing Gaussian law."""

    def __init__(self, dimension: int, *, unit_base: bool) -> None:
        self.dimension = dimension
        self.covariance = [
            [Q(0) for _ in range(dimension)] for _ in range(dimension)
        ]
        if unit_base:
            self.covariance[0][0] = Q(1)
        self.cache: dict[Monomial, Fraction] = {
            zero_monomial(dimension): Q(1)
        }

    def set_covariance(
        self, left: int, right: int, value: int | Fraction
    ) -> None:
        value = Q(value)
        current = self.covariance[left][right]
        if current and current != value:
            raise ArithmeticError(
                f"attempted to change covariance ({left}, {right}) "
                f"from {current} to {value}"
            )
        self.covariance[left][right] = value
        self.covariance[right][left] = value

    def monomial_moment(self, powers: Monomial) -> Fraction:
        cached = self.cache.get(powers)
        if cached is not None:
            return cached
        if sum(powers) % 2:
            self.cache[powers] = Q(0)
            return Q(0)
        left = next(index for index, power in enumerate(powers) if power)
        remainder = list(powers)
        remainder[left] -= 1
        value = Q(0)
        for right, multiplicity in enumerate(remainder):
            covariance = self.covariance[left][right]
            if not multiplicity or not covariance:
                continue
            remainder[right] -= 1
            value += (
                multiplicity
                * covariance
                * self.monomial_moment(tuple(remainder))
            )
            remainder[right] += 1
        self.cache[powers] = value
        return value

    def __call__(self, polynomial: Polynomial) -> Fraction:
        return sum(
            coefficient * self.monomial_moment(monomial)
            for monomial, coefficient in polynomial.items()
        )

    def product(self, left: Polynomial, right: Polynomial) -> Fraction:
        """Expect a product without retaining its sparse expansion."""
        value = Q(0)
        for left_monomial, left_coefficient in left.items():
            for right_monomial, right_coefficient in right.items():
                powers = tuple(
                    left_power + right_power
                    for left_power, right_power
                    in zip(left_monomial, right_monomial)
                )
                value += (
                    left_coefficient
                    * right_coefficient
                    * self.monomial_moment(powers)
                )
        return value

    def derivative(self, polynomial: Polynomial, index: int) -> Fraction:
        """Expect the formal partial derivative in one innovation."""
        value = Q(0)
        for monomial, coefficient in polynomial.items():
            power = monomial[index]
            if not power:
                continue
            child = list(monomial)
            child[index] -= 1
            value += (
                power * coefficient * self.monomial_moment(tuple(child))
            )
        return value


@dataclass
class JetResult:
    route: str
    derivatives: list[Fraction]
    elapsed_seconds: float
    monomial_counts: list[dict[str, int]]
    wick_cache_sizes: dict[str, int]


def _sizes(
    degree: int,
    U: list[Polynomial],
    X: list[Polynomial],
    A: list[Polynomial],
    Z: list[Polynomial],
    B: list[Polynomial],
    R: list[Polynomial],
) -> dict[str, int]:
    return {
        "degree": degree,
        "U": len(U[degree]),
        "X": len(X[degree]),
        "A": len(A[degree]),
        "Z": len(Z[degree]),
        "B": len(B[degree]),
        "R": len(R[degree]),
    }


def _format_progress(route: str, sizes: dict[str, int], elapsed: float) -> str:
    fields = " ".join(
        f"{name}={count}"
        for name, count in sizes.items()
        if name != "degree"
    )
    return f"[{route}] k={sizes['degree']} {fields} elapsed={elapsed:.3f}s"


def taylor_jet(max_order: int = 9, progress: Progress | None = None) -> JetResult:
    """Primary route using ordinary Taylor coefficients."""

    if max_order < 0:
        raise ValueError("max_order must be nonnegative")
    started = time.perf_counter()
    dimension = max_order + 2
    column = GaussianExpectation(dimension, unit_base=True)
    row = GaussianExpectation(dimension, unit_base=True)
    u0 = variable(0, dimension)
    a0 = variable(0, dimension)

    U: list[Polynomial] = []
    U2: list[Polynomial] = []
    X: list[Polynomial] = []
    A: list[Polynomial] = []
    Z: list[Polynomial] = []
    Z2: list[Polynomial] = []
    Z3: list[Polynomial] = []
    B: list[Polynomial] = []
    R: list[Polynomial] = []
    counts: list[dict[str, int]] = []

    for degree in range(max_order + 1):
        if degree == 0:
            U.append(u0)
            A.append(a0)
        else:
            U.append(scale_polynomial(add_polynomials(*(
                multiply_polynomials(U2[left], R[degree - 1 - left])
                for left in range(degree)
            )), Q(9, degree)))
            A.append(scale_polynomial(Z3[degree - 1], Q(1, degree)))

        U2.append(add_polynomials(*(
            multiply_polynomials(U[left], U[degree - left])
            for left in range(degree + 1)
        )))
        X.append(add_polynomials(*(
            multiply_polynomials(U2[left], U[degree - left])
            for left in range(degree + 1)
        )))

        eta_index = degree + 1
        for other in range(degree + 1):
            row.set_covariance(
                eta_index,
                other + 1,
                column.product(X[degree], X[other]),
            )
        forward = variable(eta_index, dimension)
        for other in range(degree):
            response = column.derivative(X[degree], other + 1)
            if response:
                forward = add_polynomials(
                    forward, scale_polynomial(B[other], response)
                )

        z_terms = [forward]
        for b_degree in range(degree):
            for x_left in range(degree - b_degree):
                x_right = degree - 1 - b_degree - x_left
                overlap = column.product(X[x_left], X[x_right])
                z_terms.append(scale_polynomial(
                    B[b_degree],
                    Q(3, b_degree + x_left + 1) * overlap,
                ))
        Z.append(add_polynomials(*z_terms))

        Z2.append(add_polynomials(*(
            multiply_polynomials(Z[left], Z[degree - left])
            for left in range(degree + 1)
        )))
        Z3.append(add_polynomials(*(
            multiply_polynomials(Z2[left], Z[degree - left])
            for left in range(degree + 1)
        )))
        B.append(add_polynomials(*(
            multiply_polynomials(A[left], Z2[degree - left])
            for left in range(degree + 1)
        )))

        xi_index = degree + 1
        for other in range(degree + 1):
            column.set_covariance(
                xi_index,
                other + 1,
                row.product(B[degree], B[other]),
            )
        backward = variable(xi_index, dimension)
        for other in range(degree + 1):
            response = row.derivative(B[degree], other + 1)
            if response:
                backward = add_polynomials(
                    backward, scale_polynomial(X[other], response)
                )

        r_terms = [backward]
        for x_degree in range(degree):
            for b_left in range(degree - x_degree):
                b_right = degree - 1 - x_degree - b_left
                overlap = row.product(B[b_left], B[b_right])
                r_terms.append(scale_polynomial(
                    X[x_degree],
                    Q(3, x_degree + b_left + 1) * overlap,
                ))
        R.append(add_polynomials(*r_terms))

        current_sizes = _sizes(degree, U, X, A, Z, B, R)
        counts.append(current_sizes)
        if progress:
            progress(_format_progress(
                "taylor", current_sizes, time.perf_counter() - started
            ))

    derivatives: list[Fraction] = []
    for degree in range(max_order + 1):
        coefficient = sum((
            row.product(A[left], Z3[degree - left])
            for left in range(degree + 1)
        ), Q(0))
        derivatives.append(math.factorial(degree) * coefficient)

    return JetResult(
        route="taylor",
        derivatives=derivatives,
        elapsed_seconds=time.perf_counter() - started,
        monomial_counts=counts,
        wick_cache_sizes={
            "column": len(column.cache),
            "row": len(row.cache),
        },
    )


def derivative_jet(
    max_order: int = 9, progress: Progress | None = None
) -> JetResult:
    """Independent route using derivative-normalized coefficient jets."""

    if max_order < 0:
        raise ValueError("max_order must be nonnegative")
    started = time.perf_counter()
    dimension = max_order + 2
    column = GaussianExpectation(dimension, unit_base=True)
    row = GaussianExpectation(dimension, unit_base=True)
    u0 = variable(0, dimension)
    a0 = variable(0, dimension)

    U: list[Polynomial] = []
    U2: list[Polynomial] = []
    X: list[Polynomial] = []
    A: list[Polynomial] = []
    Z: list[Polynomial] = []
    Z2: list[Polynomial] = []
    Z3: list[Polynomial] = []
    B: list[Polynomial] = []
    R: list[Polynomial] = []
    counts: list[dict[str, int]] = []

    for degree in range(max_order + 1):
        if degree == 0:
            U.append(u0)
            A.append(a0)
        else:
            U.append(scale_polynomial(add_polynomials(*(
                scale_polynomial(
                    multiply_polynomials(U2[left], R[degree - 1 - left]),
                    math.comb(degree - 1, left),
                )
                for left in range(degree)
            )), 9))
            A.append(Z3[degree - 1].copy())

        U2.append(add_polynomials(*(
            scale_polynomial(
                multiply_polynomials(U[left], U[degree - left]),
                math.comb(degree, left),
            )
            for left in range(degree + 1)
        )))
        X.append(add_polynomials(*(
            scale_polynomial(
                multiply_polynomials(U2[left], U[degree - left]),
                math.comb(degree, left),
            )
            for left in range(degree + 1)
        )))

        eta_index = degree + 1
        for other in range(degree + 1):
            row.set_covariance(
                eta_index,
                other + 1,
                column.product(X[degree], X[other]),
            )
        forward = variable(eta_index, dimension)
        for other in range(degree):
            response = column.derivative(X[degree], other + 1)
            if response:
                forward = add_polynomials(
                    forward, scale_polynomial(B[other], response)
                )

        z_terms = [forward]
        for b_degree in range(degree):
            for x_left in range(degree - b_degree):
                x_right = degree - 1 - b_degree - x_left
                weight = (
                    3
                    * math.comb(degree, x_right)
                    * math.comb(b_degree + x_left, b_degree)
                )
                z_terms.append(scale_polynomial(
                    B[b_degree],
                    weight * column.product(X[x_left], X[x_right]),
                ))
        Z.append(add_polynomials(*z_terms))

        Z2.append(add_polynomials(*(
            scale_polynomial(
                multiply_polynomials(Z[left], Z[degree - left]),
                math.comb(degree, left),
            )
            for left in range(degree + 1)
        )))
        Z3.append(add_polynomials(*(
            scale_polynomial(
                multiply_polynomials(Z2[left], Z[degree - left]),
                math.comb(degree, left),
            )
            for left in range(degree + 1)
        )))
        B.append(add_polynomials(*(
            scale_polynomial(
                multiply_polynomials(A[left], Z2[degree - left]),
                math.comb(degree, left),
            )
            for left in range(degree + 1)
        )))

        xi_index = degree + 1
        for other in range(degree + 1):
            column.set_covariance(
                xi_index,
                other + 1,
                row.product(B[degree], B[other]),
            )
        backward = variable(xi_index, dimension)
        for other in range(degree + 1):
            response = row.derivative(B[degree], other + 1)
            if response:
                backward = add_polynomials(
                    backward, scale_polynomial(X[other], response)
                )

        r_terms = [backward]
        for x_degree in range(degree):
            for b_left in range(degree - x_degree):
                b_right = degree - 1 - x_degree - b_left
                weight = (
                    3
                    * math.comb(degree, b_right)
                    * math.comb(x_degree + b_left, x_degree)
                )
                r_terms.append(scale_polynomial(
                    X[x_degree],
                    weight * row.product(B[b_left], B[b_right]),
                ))
        R.append(add_polynomials(*r_terms))

        current_sizes = _sizes(degree, U, X, A, Z, B, R)
        counts.append(current_sizes)
        if progress:
            progress(_format_progress(
                "derivative", current_sizes, time.perf_counter() - started
            ))

    derivatives: list[Fraction] = []
    for degree in range(max_order + 1):
        value = sum((
            math.comb(degree, left)
            * row.product(A[left], Z3[degree - left])
            for left in range(degree + 1)
        ), Q(0))
        derivatives.append(value)

    return JetResult(
        route="derivative",
        derivatives=derivatives,
        elapsed_seconds=time.perf_counter() - started,
        monomial_counts=counts,
        wick_cache_sizes={
            "column": len(column.cache),
            "row": len(row.cache),
        },
    )


def _serialize_fraction(value: Fraction) -> int | str:
    if value.denominator == 1:
        return value.numerator
    return f"{value.numerator}/{value.denominator}"


def _result_payload(result: JetResult) -> dict[str, object]:
    return {
        "route": result.route,
        "derivatives": [
            _serialize_fraction(value) for value in result.derivatives
        ],
        "elapsed_seconds": result.elapsed_seconds,
        "monomial_counts": result.monomial_counts,
        "wick_cache_sizes": result.wick_cache_sizes,
    }


def _assert_frozen_gates(
    results: Iterable[JetResult], max_order: int
) -> None:
    controls = {
        1: 305_775,
        3: 154_118_008_098_000,
        5: 302_467_842_967_104_331_335_000,
    }
    results = list(results)
    for result in results:
        for order, expected in controls.items():
            if order <= max_order and result.derivatives[order] != expected:
                raise AssertionError(
                    f"{result.route} lower-order gate F^{order}: "
                    f"got {result.derivatives[order]}, expected {expected}"
                )
        for order in range(0, max_order + 1, 2):
            if result.derivatives[order] != 0:
                raise AssertionError(
                    f"{result.route} parity gate F^{order}: "
                    f"got {result.derivatives[order]}"
                )
        if any(value.denominator != 1 for value in result.derivatives):
            raise AssertionError(
                f"{result.route} produced a noninteger output jet"
            )
    if len(results) == 2 and results[0].derivatives != results[1].derivatives:
        raise AssertionError("the two exact assemblers disagree")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-order", type=int, default=9)
    parser.add_argument(
        "--route", choices=("taylor", "derivative", "both"), default="both"
    )
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    progress: Progress | None = None if args.quiet else print
    results: list[JetResult] = []
    if args.route in ("taylor", "both"):
        results.append(taylor_jet(args.max_order, progress))
    if args.route in ("derivative", "both"):
        results.append(derivative_jet(args.max_order, progress))
    _assert_frozen_gates(results, args.max_order)

    payload = {
        "model": "raw-cubic-equal-width-two-hidden-layer",
        "max_order": args.max_order,
        "validation": "passed",
        "results": [_result_payload(result) for result in results],
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        for result in results:
            print(
                f"{result.route} derivatives: "
                + ", ".join(
                    f"F^{order}={_serialize_fraction(value)}"
                    for order, value in enumerate(result.derivatives)
                )
            )
        print("validation: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
