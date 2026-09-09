#!/usr/bin/env python3
"""Exact width-limit feature jet for the raw quadratic depth-3 network.

This implements the nested Gaussian-program/detransposition recurrence frozen
in ``PROTOCOL.md``.  It has two deliberately separate coefficient assemblers:

* ``taylor_jet`` stores coefficients of ordinary powers ``t**k``;
* ``derivative_jet`` stores actual derivatives at zero and uses explicit
  binomial/multinomial product rules.

They share only sparse-polynomial and exact Wick-expectation primitives.
No derivative forests or finite-width extrapolations are used.
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
    return {monomial: coefficient for monomial, coefficient in result.items()
            if coefficient}


def scale_polynomial(polynomial: Polynomial, scalar: Fraction) -> Polynomial:
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
                for left_power, right_power in zip(left_monomial, right_monomial)
            )
            result[monomial] = (
                result.get(monomial, Q(0))
                + left_coefficient * right_coefficient
            )
    return {monomial: coefficient for monomial, coefficient in result.items()
            if coefficient}


class GaussianExpectation:
    """Exact Wick expectation for a growing centered Gaussian family."""

    def __init__(self, dimension: int, unit_base: bool = False) -> None:
        self.dimension = dimension
        self.covariance = [
            [Q(0) for _ in range(dimension)] for _ in range(dimension)
        ]
        if unit_base:
            self.covariance[0][0] = Q(1)
        self.cache: dict[Monomial, Fraction] = {
            zero_monomial(dimension): Q(1)
        }

    def set_covariance(self, left: int, right: int, value: Fraction) -> None:
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
        """Expect a product without materializing its sparse expansion."""
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
        """Expect the formal partial derivative with respect to one variable."""
        value = Q(0)
        for monomial, coefficient in polynomial.items():
            power = monomial[index]
            if not power:
                continue
            child = list(monomial)
            child[index] -= 1
            value += power * coefficient * self.monomial_moment(tuple(child))
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
    X: list[Polynomial],
    Z: list[Polynomial],
    Y: list[Polynomial],
    T: list[Polynomial],
    B3: list[Polynomial],
    R2: list[Polynomial],
    B2: list[Polynomial],
    R1: list[Polynomial],
) -> dict[str, int]:
    return {
        "degree": degree,
        "X": len(X[degree]),
        "Z": len(Z[degree]),
        "Y": len(Y[degree]),
        "T": len(T[degree]),
        "B3": len(B3[degree]),
        "R2": len(R2[degree]),
        "B2": len(B2[degree]),
        "R1": len(R1[degree]),
    }


def _format_progress(route: str, sizes: dict[str, int], elapsed: float) -> str:
    fields = " ".join(
        f"{name}={count}"
        for name, count in sizes.items()
        if name != "degree"
    )
    return f"[{route}] k={sizes['degree']} {fields} elapsed={elapsed:.3f}s"


def taylor_jet(max_order: int = 9, progress: Progress | None = None) -> JetResult:
    """Primary assembler using ordinary Taylor coefficients."""

    if max_order < 0:
        raise ValueError("max_order must be nonnegative")
    started = time.perf_counter()
    bottom_dimension = max_order + 2
    middle_dimension = 2 * (max_order + 1)
    top_dimension = max_order + 2
    bottom = GaussianExpectation(bottom_dimension, unit_base=True)
    middle = GaussianExpectation(middle_dimension)
    top = GaussianExpectation(top_dimension, unit_base=True)
    u = variable(0, bottom_dimension)
    a = variable(0, top_dimension)
    middle_split = max_order + 1

    A: list[Polynomial] = []
    X: list[Polynomial] = []
    Z: list[Polynomial] = []
    Y: list[Polynomial] = []
    T: list[Polynomial] = []
    B3: list[Polynomial] = []
    R2: list[Polynomial] = []
    B2: list[Polynomial] = []
    R1: list[Polynomial] = []
    counts: list[dict[str, int]] = []

    for degree in range(max_order + 1):
        if degree == 0:
            A.append(a)
            X.append(multiply_polynomials(u, u))
        else:
            A.append(
                scale_polynomial(
                    add_polynomials(*(
                        multiply_polynomials(T[left], T[degree - 1 - left])
                        for left in range(degree)
                    )),
                    Q(1, degree),
                )
            )
            X.append(
                scale_polynomial(
                    add_polynomials(*(
                        multiply_polynomials(X[left], R1[degree - 1 - left])
                        for left in range(degree)
                    )),
                    Q(16, degree),
                )
            )

        # Fixed W_0 forward use, plus its prior-transpose Stein responses.
        for other in range(degree + 1):
            middle.set_covariance(
                degree,
                other,
                bottom.product(X[degree], X[other]),
            )
        w_forward = variable(degree, middle_dimension)
        for other in range(degree):
            response = bottom.derivative(X[degree], other + 1)
            if response:
                w_forward = add_polynomials(
                    w_forward, scale_polynomial(B2[other], response)
                )

        z_terms = [w_forward]
        for b_degree in range(degree):
            for x_left in range(degree - b_degree):
                x_right = degree - 1 - b_degree - x_left
                overlap = bottom.product(X[x_left], X[x_right])
                z_terms.append(
                    scale_polynomial(
                        B2[b_degree],
                        Q(4, b_degree + x_left + 1) * overlap,
                    )
                )
        Z.append(add_polynomials(*z_terms))
        Y.append(add_polynomials(*(
            multiply_polynomials(Z[left], Z[degree - left])
            for left in range(degree + 1)
        )))

        # Fixed V_0 forward use, plus its prior-transpose Stein responses.
        for other in range(degree + 1):
            top.set_covariance(
                degree + 1,
                other + 1,
                middle.product(Y[degree], Y[other]),
            )
        v_forward = variable(degree + 1, top_dimension)
        for other in range(degree):
            response = middle.derivative(Y[degree], middle_split + other)
            if response:
                v_forward = add_polynomials(
                    v_forward, scale_polynomial(B3[other], response)
                )

        t_terms = [v_forward]
        for b_degree in range(degree):
            for y_left in range(degree - b_degree):
                y_right = degree - 1 - b_degree - y_left
                overlap = middle.product(Y[y_left], Y[y_right])
                t_terms.append(
                    scale_polynomial(
                        B3[b_degree],
                        Q(2, b_degree + y_left + 1) * overlap,
                    )
                )
        T.append(add_polynomials(*t_terms))
        B3.append(add_polynomials(*(
            multiply_polynomials(A[left], T[degree - left])
            for left in range(degree + 1)
        )))

        # Fixed V_0 transpose use, including all current forward responses.
        xi_v_index = middle_split + degree
        for other in range(degree + 1):
            middle.set_covariance(
                xi_v_index,
                middle_split + other,
                top.product(B3[degree], B3[other]),
            )
        v_backward = variable(xi_v_index, middle_dimension)
        for other in range(degree + 1):
            response = top.derivative(B3[degree], other + 1)
            if response:
                v_backward = add_polynomials(
                    v_backward, scale_polynomial(Y[other], response)
                )

        r2_terms = [v_backward]
        for y_degree in range(degree):
            for b_left in range(degree - y_degree):
                b_right = degree - 1 - y_degree - b_left
                overlap = top.product(B3[b_left], B3[b_right])
                r2_terms.append(
                    scale_polynomial(
                        Y[y_degree],
                        Q(2, y_degree + b_left + 1) * overlap,
                    )
                )
        R2.append(add_polynomials(*r2_terms))
        B2.append(add_polynomials(*(
            multiply_polynomials(Z[left], R2[degree - left])
            for left in range(degree + 1)
        )))

        # Fixed W_0 transpose use, including all current forward responses.
        xi_w_index = degree + 1
        for other in range(degree + 1):
            bottom.set_covariance(
                xi_w_index,
                other + 1,
                middle.product(B2[degree], B2[other]),
            )
        w_backward = variable(xi_w_index, bottom_dimension)
        for other in range(degree + 1):
            response = middle.derivative(B2[degree], other)
            if response:
                w_backward = add_polynomials(
                    w_backward, scale_polynomial(X[other], response)
                )

        r1_terms = [w_backward]
        for x_degree in range(degree):
            for b_left in range(degree - x_degree):
                b_right = degree - 1 - x_degree - b_left
                overlap = middle.product(B2[b_left], B2[b_right])
                r1_terms.append(
                    scale_polynomial(
                        X[x_degree],
                        Q(4, x_degree + b_left + 1) * overlap,
                    )
                )
        R1.append(add_polynomials(*r1_terms))

        current_sizes = _sizes(degree, X, Z, Y, T, B3, R2, B2, R1)
        counts.append(current_sizes)
        if progress:
            progress(_format_progress(
                "taylor", current_sizes, time.perf_counter() - started
            ))

    derivatives: list[Fraction] = []
    for degree in range(max_order + 1):
        coefficient = Q(0)
        for a_degree in range(degree + 1):
            for t_left in range(degree - a_degree + 1):
                t_right = degree - a_degree - t_left
                coefficient += top.product(
                    A[a_degree],
                    multiply_polynomials(T[t_left], T[t_right]),
                )
        derivatives.append(math.factorial(degree) * coefficient)

    return JetResult(
        route="taylor",
        derivatives=derivatives,
        elapsed_seconds=time.perf_counter() - started,
        monomial_counts=counts,
        wick_cache_sizes={
            "bottom": len(bottom.cache),
            "middle": len(middle.cache),
            "top": len(top.cache),
        },
    )


def derivative_jet(
    max_order: int = 9, progress: Progress | None = None
) -> JetResult:
    """Independent assembler using derivative-normalized coefficient jets."""

    if max_order < 0:
        raise ValueError("max_order must be nonnegative")
    started = time.perf_counter()
    bottom_dimension = max_order + 2
    middle_dimension = 2 * (max_order + 1)
    top_dimension = max_order + 2
    bottom = GaussianExpectation(bottom_dimension, unit_base=True)
    middle = GaussianExpectation(middle_dimension)
    top = GaussianExpectation(top_dimension, unit_base=True)
    u = variable(0, bottom_dimension)
    a = variable(0, top_dimension)
    middle_split = max_order + 1

    A: list[Polynomial] = []
    X: list[Polynomial] = []
    Z: list[Polynomial] = []
    Y: list[Polynomial] = []
    T: list[Polynomial] = []
    B3: list[Polynomial] = []
    R2: list[Polynomial] = []
    B2: list[Polynomial] = []
    R1: list[Polynomial] = []
    counts: list[dict[str, int]] = []

    for degree in range(max_order + 1):
        if degree == 0:
            A.append(a)
            X.append(multiply_polynomials(u, u))
        else:
            A.append(add_polynomials(*(
                scale_polynomial(
                    multiply_polynomials(T[left], T[degree - 1 - left]),
                    Q(math.comb(degree - 1, left)),
                )
                for left in range(degree)
            )))
            X.append(scale_polynomial(add_polynomials(*(
                scale_polynomial(
                    multiply_polynomials(X[left], R1[degree - 1 - left]),
                    Q(math.comb(degree - 1, left)),
                )
                for left in range(degree)
            )), Q(16)))

        for other in range(degree + 1):
            middle.set_covariance(
                degree, other, bottom.product(X[degree], X[other])
            )
        w_forward = variable(degree, middle_dimension)
        for other in range(degree):
            response = bottom.derivative(X[degree], other + 1)
            if response:
                w_forward = add_polynomials(
                    w_forward, scale_polynomial(B2[other], response)
                )
        z_terms = [w_forward]
        for b_degree in range(degree):
            for x_left in range(degree - b_degree):
                x_right = degree - 1 - b_degree - x_left
                weight = (
                    4
                    * math.comb(degree, x_right)
                    * math.comb(b_degree + x_left, b_degree)
                )
                z_terms.append(scale_polynomial(
                    B2[b_degree],
                    Q(weight) * bottom.product(X[x_left], X[x_right]),
                ))
        Z.append(add_polynomials(*z_terms))
        Y.append(add_polynomials(*(
            scale_polynomial(
                multiply_polynomials(Z[left], Z[degree - left]),
                Q(math.comb(degree, left)),
            )
            for left in range(degree + 1)
        )))

        for other in range(degree + 1):
            top.set_covariance(
                degree + 1,
                other + 1,
                middle.product(Y[degree], Y[other]),
            )
        v_forward = variable(degree + 1, top_dimension)
        for other in range(degree):
            response = middle.derivative(Y[degree], middle_split + other)
            if response:
                v_forward = add_polynomials(
                    v_forward, scale_polynomial(B3[other], response)
                )
        t_terms = [v_forward]
        for b_degree in range(degree):
            for y_left in range(degree - b_degree):
                y_right = degree - 1 - b_degree - y_left
                weight = (
                    2
                    * math.comb(degree, y_right)
                    * math.comb(b_degree + y_left, b_degree)
                )
                t_terms.append(scale_polynomial(
                    B3[b_degree],
                    Q(weight) * middle.product(Y[y_left], Y[y_right]),
                ))
        T.append(add_polynomials(*t_terms))
        B3.append(add_polynomials(*(
            scale_polynomial(
                multiply_polynomials(A[left], T[degree - left]),
                Q(math.comb(degree, left)),
            )
            for left in range(degree + 1)
        )))

        xi_v_index = middle_split + degree
        for other in range(degree + 1):
            middle.set_covariance(
                xi_v_index,
                middle_split + other,
                top.product(B3[degree], B3[other]),
            )
        v_backward = variable(xi_v_index, middle_dimension)
        for other in range(degree + 1):
            response = top.derivative(B3[degree], other + 1)
            if response:
                v_backward = add_polynomials(
                    v_backward, scale_polynomial(Y[other], response)
                )
        r2_terms = [v_backward]
        for y_degree in range(degree):
            for b_left in range(degree - y_degree):
                b_right = degree - 1 - y_degree - b_left
                weight = (
                    2
                    * math.comb(degree, b_right)
                    * math.comb(y_degree + b_left, y_degree)
                )
                r2_terms.append(scale_polynomial(
                    Y[y_degree],
                    Q(weight) * top.product(B3[b_left], B3[b_right]),
                ))
        R2.append(add_polynomials(*r2_terms))
        B2.append(add_polynomials(*(
            scale_polynomial(
                multiply_polynomials(Z[left], R2[degree - left]),
                Q(math.comb(degree, left)),
            )
            for left in range(degree + 1)
        )))

        xi_w_index = degree + 1
        for other in range(degree + 1):
            bottom.set_covariance(
                xi_w_index,
                other + 1,
                middle.product(B2[degree], B2[other]),
            )
        w_backward = variable(xi_w_index, bottom_dimension)
        for other in range(degree + 1):
            response = middle.derivative(B2[degree], other)
            if response:
                w_backward = add_polynomials(
                    w_backward, scale_polynomial(X[other], response)
                )
        r1_terms = [w_backward]
        for x_degree in range(degree):
            for b_left in range(degree - x_degree):
                b_right = degree - 1 - x_degree - b_left
                weight = (
                    4
                    * math.comb(degree, b_right)
                    * math.comb(x_degree + b_left, x_degree)
                )
                r1_terms.append(scale_polynomial(
                    X[x_degree],
                    Q(weight) * middle.product(B2[b_left], B2[b_right]),
                ))
        R1.append(add_polynomials(*r1_terms))

        current_sizes = _sizes(degree, X, Z, Y, T, B3, R2, B2, R1)
        counts.append(current_sizes)
        if progress:
            progress(_format_progress(
                "derivative", current_sizes, time.perf_counter() - started
            ))

    derivatives: list[Fraction] = []
    for degree in range(max_order + 1):
        value = Q(0)
        for a_degree in range(degree + 1):
            for t_left in range(degree - a_degree + 1):
                t_right = degree - a_degree - t_left
                multinomial = (
                    math.factorial(degree)
                    // (
                        math.factorial(a_degree)
                        * math.factorial(t_left)
                        * math.factorial(t_right)
                    )
                )
                value += multinomial * top.product(
                    A[a_degree],
                    multiply_polynomials(T[t_left], T[t_right]),
                )
        derivatives.append(value)

    return JetResult(
        route="derivative",
        derivatives=derivatives,
        elapsed_seconds=time.perf_counter() - started,
        monomial_counts=counts,
        wick_cache_sizes={
            "bottom": len(bottom.cache),
            "middle": len(middle.cache),
            "top": len(top.cache),
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


def _assert_frozen_gates(results: Iterable[JetResult], max_order: int) -> None:
    controls = {
        1: 14_175,
        3: 139_445_032_896,
        5: 4_298_284_752_832_899_360,
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
            raise AssertionError(f"{result.route} produced a noninteger output jet")
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
        "model": "raw-quadratic-equal-width-three-hidden-layer",
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
