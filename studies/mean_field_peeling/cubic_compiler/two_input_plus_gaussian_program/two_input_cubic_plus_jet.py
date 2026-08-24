#!/usr/bin/env python3
"""Exact two-input raw-cubic plus-channel Gaussian-program jet.

Every scalar coefficient is a rational polynomial in the input correlation
``rho``.  Two independently normalized recurrences are implemented:

* ``taylor_jet`` stores ordinary Taylor coefficients;
* ``derivative_jet`` stores actual derivatives at zero.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable, Sequence


Q = Fraction
RhoPolynomial = tuple[Fraction, ...]
Monomial = tuple[int, ...]
StatePolynomial = dict[Monomial, RhoPolynomial]
Progress = Callable[[str], None]

HERE = Path(__file__).resolve().parent
PROTOCOL = HERE / "PROTOCOL.md"
EXPECTED_PROTOCOL_SHA256 = (
    "6742675cb0c40dcfb2652edab05ce078b00506bfdef4bfd25157a22b0dbea956"
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rho_trim(values: Iterable[Fraction | int]) -> RhoPolynomial:
    result = [Q(value) for value in values]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return tuple(result) if result else (Q(0),)


RHO_ZERO = rho_trim((0,))
RHO_ONE = rho_trim((1,))
RHO_VARIABLE = rho_trim((0, 1))


def rho_constant(value: Fraction | int) -> RhoPolynomial:
    return rho_trim((value,))


def rho_add(*polynomials: RhoPolynomial) -> RhoPolynomial:
    if not polynomials:
        return RHO_ZERO
    degree = max(len(polynomial) for polynomial in polynomials)
    return rho_trim(
        sum(
            (
                polynomial[index]
                if index < len(polynomial)
                else Q(0)
            )
            for polynomial in polynomials
        )
        for index in range(degree)
    )


def rho_scale(
    polynomial: RhoPolynomial, scalar: Fraction | int
) -> RhoPolynomial:
    scalar = Q(scalar)
    if not scalar or polynomial == RHO_ZERO:
        return RHO_ZERO
    return rho_trim(scalar * coefficient for coefficient in polynomial)


def rho_multiply(
    left: RhoPolynomial, right: RhoPolynomial
) -> RhoPolynomial:
    if left == RHO_ZERO or right == RHO_ZERO:
        return RHO_ZERO
    result = [Q(0) for _ in range(len(left) + len(right) - 1)]
    for left_degree, left_value in enumerate(left):
        if not left_value:
            continue
        for right_degree, right_value in enumerate(right):
            if right_value:
                result[left_degree + right_degree] += (
                    left_value * right_value
                )
    return rho_trim(result)


def rho_power(polynomial: RhoPolynomial, exponent: int) -> RhoPolynomial:
    result = RHO_ONE
    for _ in range(exponent):
        result = rho_multiply(result, polynomial)
    return result


def rho_evaluate(
    polynomial: RhoPolynomial, value: Fraction | int
) -> Fraction:
    value = Q(value)
    result = Q(0)
    for coefficient in reversed(polynomial):
        result = result * value + coefficient
    return result


def rho_to_strings(polynomial: RhoPolynomial) -> list[str]:
    return [fraction_string(coefficient) for coefficient in polynomial]


def fraction_string(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def rho_expression(polynomial: RhoPolynomial, variable: str = "rho") -> str:
    terms: list[str] = []
    for degree, coefficient in enumerate(polynomial):
        if not coefficient:
            continue
        magnitude = abs(coefficient)
        if degree == 0:
            body = fraction_string(magnitude)
        else:
            power = variable if degree == 1 else f"{variable}^{degree}"
            body = power if magnitude == 1 else f"{fraction_string(magnitude)}*{power}"
        if not terms:
            terms.append(body if coefficient > 0 else f"-{body}")
        else:
            terms.append((" + " if coefficient > 0 else " - ") + body)
    return "".join(terms) if terms else "0"


def zero_monomial(dimension: int) -> Monomial:
    return (0,) * dimension


class SparseStateAlgebra:
    """Sparse Gaussian-variable polynomials with QQ[rho] coefficients."""

    def __init__(self, dimension: int) -> None:
        self.dimension = dimension

    def variable(self, index: int) -> StatePolynomial:
        powers = [0] * self.dimension
        powers[index] = 1
        return {tuple(powers): RHO_ONE}

    def add(self, *polynomials: StatePolynomial) -> StatePolynomial:
        result: StatePolynomial = {}
        for polynomial in polynomials:
            for monomial, coefficient in polynomial.items():
                result[monomial] = rho_add(
                    result.get(monomial, RHO_ZERO), coefficient
                )
        return {
            monomial: coefficient
            for monomial, coefficient in result.items()
            if coefficient != RHO_ZERO
        }

    def scale(
        self,
        polynomial: StatePolynomial,
        scalar: RhoPolynomial | Fraction | int,
    ) -> StatePolynomial:
        scalar_polynomial = (
            scalar if isinstance(scalar, tuple) else rho_constant(scalar)
        )
        if scalar_polynomial == RHO_ZERO or not polynomial:
            return {}
        return {
            monomial: coefficient
            for monomial, old_coefficient in polynomial.items()
            if (
                coefficient := rho_multiply(
                    old_coefficient, scalar_polynomial
                )
            ) != RHO_ZERO
        }

    def multiply(
        self, left: StatePolynomial, right: StatePolynomial
    ) -> StatePolynomial:
        if not left or not right:
            return {}
        result: StatePolynomial = {}
        for left_monomial, left_coefficient in left.items():
            for right_monomial, right_coefficient in right.items():
                monomial = tuple(
                    left_power + right_power
                    for left_power, right_power in zip(
                        left_monomial, right_monomial
                    )
                )
                result[monomial] = rho_add(
                    result.get(monomial, RHO_ZERO),
                    rho_multiply(left_coefficient, right_coefficient),
                )
        return {
            monomial: coefficient
            for monomial, coefficient in result.items()
            if coefficient != RHO_ZERO
        }

    def product(self, *polynomials: StatePolynomial) -> StatePolynomial:
        if not polynomials:
            return {zero_monomial(self.dimension): RHO_ONE}
        result = polynomials[0]
        for polynomial in polynomials[1:]:
            result = self.multiply(result, polynomial)
            if not result:
                break
        return result


class PolynomialGaussianExpectation:
    """Exact Wick expectation with QQ[rho]-valued covariances."""

    def __init__(self, algebra: SparseStateAlgebra) -> None:
        self.algebra = algebra
        self.dimension = algebra.dimension
        self.covariance = [
            [RHO_ZERO for _ in range(self.dimension)]
            for _ in range(self.dimension)
        ]
        self.cache: dict[Monomial, RhoPolynomial] = {
            zero_monomial(self.dimension): RHO_ONE
        }

    def set_covariance(
        self, left: int, right: int, value: RhoPolynomial
    ) -> None:
        value = rho_trim(value)
        current = self.covariance[left][right]
        if current != RHO_ZERO and current != value:
            raise ArithmeticError(
                f"attempted to change covariance ({left}, {right}) "
                f"from {current} to {value}"
            )
        self.covariance[left][right] = value
        self.covariance[right][left] = value

    def monomial_moment(self, powers: Monomial) -> RhoPolynomial:
        cached = self.cache.get(powers)
        if cached is not None:
            return cached
        if sum(powers) % 2:
            self.cache[powers] = RHO_ZERO
            return RHO_ZERO
        left = next(index for index, power in enumerate(powers) if power)
        remainder = list(powers)
        remainder[left] -= 1
        value = RHO_ZERO
        for right, multiplicity in enumerate(remainder):
            covariance = self.covariance[left][right]
            if not multiplicity or covariance == RHO_ZERO:
                continue
            remainder[right] -= 1
            value = rho_add(
                value,
                rho_scale(
                    rho_multiply(
                        covariance, self.monomial_moment(tuple(remainder))
                    ),
                    multiplicity,
                ),
            )
            remainder[right] += 1
        self.cache[powers] = value
        return value

    def __call__(self, polynomial: StatePolynomial) -> RhoPolynomial:
        return rho_add(*(
            rho_multiply(coefficient, self.monomial_moment(monomial))
            for monomial, coefficient in polynomial.items()
        ))

    def product_expectation(
        self, left: StatePolynomial, right: StatePolynomial
    ) -> RhoPolynomial:
        terms: list[RhoPolynomial] = []
        for left_monomial, left_coefficient in left.items():
            for right_monomial, right_coefficient in right.items():
                monomial = tuple(
                    left_power + right_power
                    for left_power, right_power in zip(
                        left_monomial, right_monomial
                    )
                )
                terms.append(rho_multiply(
                    rho_multiply(left_coefficient, right_coefficient),
                    self.monomial_moment(monomial),
                ))
        return rho_add(*terms)

    def derivative_expectation(
        self, polynomial: StatePolynomial, index: int
    ) -> RhoPolynomial:
        terms: list[RhoPolynomial] = []
        for monomial, coefficient in polynomial.items():
            power = monomial[index]
            if not power:
                continue
            child = list(monomial)
            child[index] -= 1
            terms.append(rho_scale(
                rho_multiply(
                    coefficient, self.monomial_moment(tuple(child))
                ),
                power,
            ))
        return rho_add(*terms)


@dataclass
class JetResult:
    route: str
    derivatives: list[RhoPolynomial]
    sample_derivatives: list[list[RhoPolynomial]]
    elapsed_seconds: float
    state_counts: list[dict[str, int]]
    wick_cache_sizes: dict[str, int]


def column_base(sample: int) -> int:
    return sample


def xi_index(sample: int, degree: int) -> int:
    return 2 + 2 * degree + sample


def eta_index(sample: int, degree: int) -> int:
    return 1 + 2 * degree + sample


def input_gram(left: int, right: int) -> RhoPolynomial:
    return RHO_ONE if left == right else RHO_VARIABLE


def _setup(max_order: int):
    column_algebra = SparseStateAlgebra(2 + 2 * (max_order + 1))
    row_algebra = SparseStateAlgebra(1 + 2 * (max_order + 1))
    column = PolynomialGaussianExpectation(column_algebra)
    row = PolynomialGaussianExpectation(row_algebra)
    column.set_covariance(column_base(0), column_base(0), RHO_ONE)
    column.set_covariance(column_base(1), column_base(1), RHO_ONE)
    column.set_covariance(column_base(0), column_base(1), RHO_VARIABLE)
    row.set_covariance(0, 0, RHO_ONE)
    return column_algebra, row_algebra, column, row


def _state_counts(
    degree: int,
    U: Sequence[Sequence[StatePolynomial]],
    X: Sequence[Sequence[StatePolynomial]],
    A: Sequence[StatePolynomial],
    Z: Sequence[Sequence[StatePolynomial]],
    B: Sequence[Sequence[StatePolynomial]],
    R: Sequence[Sequence[StatePolynomial]],
) -> dict[str, int]:
    return {
        "degree": degree,
        "U": sum(len(U[sample][degree]) for sample in range(2)),
        "X": sum(len(X[sample][degree]) for sample in range(2)),
        "A": len(A[degree]),
        "Z": sum(len(Z[sample][degree]) for sample in range(2)),
        "B": sum(len(B[sample][degree]) for sample in range(2)),
        "R": sum(len(R[sample][degree]) for sample in range(2)),
    }


def _progress_line(route: str, counts: dict[str, int], elapsed: float) -> str:
    fields = " ".join(
        f"{name}={count}"
        for name, count in counts.items()
        if name != "degree"
    )
    return f"[{route}] k={counts['degree']} {fields} elapsed={elapsed:.3f}s"


def _set_forward_covariances(
    degree: int,
    X: Sequence[Sequence[StatePolynomial]],
    column: PolynomialGaussianExpectation,
    row: PolynomialGaussianExpectation,
) -> None:
    for sample in range(2):
        current = eta_index(sample, degree)
        for other_sample in range(2):
            for other_degree in range(degree + 1):
                other = eta_index(other_sample, other_degree)
                covariance = column.product_expectation(
                    X[sample][degree], X[other_sample][other_degree]
                )
                row.set_covariance(current, other, covariance)


def _set_backward_covariances(
    degree: int,
    B: Sequence[Sequence[StatePolynomial]],
    row: PolynomialGaussianExpectation,
    column: PolynomialGaussianExpectation,
) -> None:
    for sample in range(2):
        current = xi_index(sample, degree)
        for other_sample in range(2):
            for other_degree in range(degree + 1):
                other = xi_index(other_sample, other_degree)
                covariance = row.product_expectation(
                    B[sample][degree], B[other_sample][other_degree]
                )
                column.set_covariance(current, other, covariance)


def taylor_jet(
    max_order: int = 3, progress: Progress | None = None
) -> JetResult:
    """Ordinary-Taylor two-input recurrence."""

    if max_order < 0:
        raise ValueError("max_order must be nonnegative")
    started = time.perf_counter()
    col_alg, row_alg, column, row = _setup(max_order)

    U: list[list[StatePolynomial]] = [[], []]
    X: list[list[StatePolynomial]] = [[], []]
    Z: list[list[StatePolynomial]] = [[], []]
    G: list[list[StatePolynomial]] = [[], []]
    B: list[list[StatePolynomial]] = [[], []]
    R: list[list[StatePolynomial]] = [[], []]
    A: list[StatePolynomial] = []
    counts: list[dict[str, int]] = []

    for degree in range(max_order + 1):
        if degree == 0:
            for sample in range(2):
                U[sample].append(col_alg.variable(column_base(sample)))
            A.append(row_alg.variable(0))
        else:
            target = degree - 1
            for sample in range(2):
                terms: list[StatePolynomial] = []
                for source in range(2):
                    geometry = input_gram(sample, source)
                    for left in range(target + 1):
                        for middle in range(target - left + 1):
                            right = target - left - middle
                            terms.append(col_alg.scale(
                                col_alg.product(
                                    U[source][left],
                                    U[source][middle],
                                    R[source][right],
                                ),
                                geometry,
                            ))
                U[sample].append(col_alg.scale(
                    col_alg.add(*terms), Q(9, 2 * degree)
                ))
            A.append(row_alg.scale(
                row_alg.add(G[0][degree - 1], G[1][degree - 1]),
                Q(1, 2 * degree),
            ))

        for sample in range(2):
            X[sample].append(col_alg.add(*(
                col_alg.product(
                    U[sample][left],
                    U[sample][middle],
                    U[sample][degree - left - middle],
                )
                for left in range(degree + 1)
                for middle in range(degree - left + 1)
            )))

        _set_forward_covariances(degree, X, column, row)

        for sample in range(2):
            forward = row_alg.variable(eta_index(sample, degree))
            for source in range(2):
                for other_degree in range(degree):
                    response = column.derivative_expectation(
                        X[sample][degree],
                        xi_index(source, other_degree),
                    )
                    if response != RHO_ZERO:
                        forward = row_alg.add(
                            forward,
                            row_alg.scale(B[source][other_degree], response),
                        )

            z_terms = [forward]
            for source in range(2):
                for b_degree in range(degree):
                    for x_left in range(degree - b_degree):
                        x_right = degree - 1 - b_degree - x_left
                        overlap = column.product_expectation(
                            X[source][x_left], X[sample][x_right]
                        )
                        z_terms.append(row_alg.scale(
                            B[source][b_degree],
                            rho_scale(
                                overlap,
                                Q(3, 2 * (b_degree + x_left + 1)),
                            ),
                        ))
            Z[sample].append(row_alg.add(*z_terms))
            G[sample].append(row_alg.add(*(
                row_alg.product(
                    Z[sample][left],
                    Z[sample][middle],
                    Z[sample][degree - left - middle],
                )
                for left in range(degree + 1)
                for middle in range(degree - left + 1)
            )))
            B[sample].append(row_alg.add(*(
                row_alg.product(
                    A[left],
                    Z[sample][middle],
                    Z[sample][degree - left - middle],
                )
                for left in range(degree + 1)
                for middle in range(degree - left + 1)
            )))

        _set_backward_covariances(degree, B, row, column)

        for sample in range(2):
            backward = col_alg.variable(xi_index(sample, degree))
            for source in range(2):
                for other_degree in range(degree + 1):
                    response = row.derivative_expectation(
                        B[sample][degree],
                        eta_index(source, other_degree),
                    )
                    if response != RHO_ZERO:
                        backward = col_alg.add(
                            backward,
                            col_alg.scale(X[source][other_degree], response),
                        )

            r_terms = [backward]
            for source in range(2):
                for x_degree in range(degree):
                    for b_left in range(degree - x_degree):
                        b_right = degree - 1 - x_degree - b_left
                        overlap = row.product_expectation(
                            B[source][b_left], B[sample][b_right]
                        )
                        r_terms.append(col_alg.scale(
                            X[source][x_degree],
                            rho_scale(
                                overlap,
                                Q(3, 2 * (x_degree + b_left + 1)),
                            ),
                        ))
            R[sample].append(col_alg.add(*r_terms))

        current_counts = _state_counts(degree, U, X, A, Z, B, R)
        counts.append(current_counts)
        if progress:
            progress(_progress_line(
                "taylor", current_counts, time.perf_counter() - started
            ))

    sample_derivatives: list[list[RhoPolynomial]] = [[], []]
    for sample in range(2):
        for degree in range(max_order + 1):
            coefficient = rho_add(*(
                row.product_expectation(A[left], G[sample][degree - left])
                for left in range(degree + 1)
            ))
            sample_derivatives[sample].append(
                rho_scale(coefficient, math.factorial(degree))
            )
    derivatives = [
        rho_scale(
            rho_add(
                sample_derivatives[0][degree],
                sample_derivatives[1][degree],
            ),
            Q(1, 2),
        )
        for degree in range(max_order + 1)
    ]
    return JetResult(
        route="taylor",
        derivatives=derivatives,
        sample_derivatives=sample_derivatives,
        elapsed_seconds=time.perf_counter() - started,
        state_counts=counts,
        wick_cache_sizes={"column": len(column.cache), "row": len(row.cache)},
    )


def derivative_jet(
    max_order: int = 3, progress: Progress | None = None
) -> JetResult:
    """Derivative-normalized two-input recurrence."""

    if max_order < 0:
        raise ValueError("max_order must be nonnegative")
    started = time.perf_counter()
    col_alg, row_alg, column, row = _setup(max_order)

    U: list[list[StatePolynomial]] = [[], []]
    X: list[list[StatePolynomial]] = [[], []]
    Z: list[list[StatePolynomial]] = [[], []]
    G: list[list[StatePolynomial]] = [[], []]
    B: list[list[StatePolynomial]] = [[], []]
    R: list[list[StatePolynomial]] = [[], []]
    A: list[StatePolynomial] = []
    counts: list[dict[str, int]] = []

    for degree in range(max_order + 1):
        if degree == 0:
            for sample in range(2):
                U[sample].append(col_alg.variable(column_base(sample)))
            A.append(row_alg.variable(0))
        else:
            target = degree - 1
            for sample in range(2):
                terms: list[StatePolynomial] = []
                for source in range(2):
                    geometry = input_gram(sample, source)
                    for left in range(target + 1):
                        for middle in range(target - left + 1):
                            right = target - left - middle
                            weight = (
                                math.factorial(target)
                                // (
                                    math.factorial(left)
                                    * math.factorial(middle)
                                    * math.factorial(right)
                                )
                            )
                            terms.append(col_alg.scale(
                                col_alg.product(
                                    U[source][left],
                                    U[source][middle],
                                    R[source][right],
                                ),
                                rho_scale(geometry, weight),
                            ))
                U[sample].append(col_alg.scale(
                    col_alg.add(*terms), Q(9, 2)
                ))
            A.append(row_alg.scale(
                row_alg.add(G[0][degree - 1], G[1][degree - 1]),
                Q(1, 2),
            ))

        for sample in range(2):
            x_terms: list[StatePolynomial] = []
            for left in range(degree + 1):
                for middle in range(degree - left + 1):
                    right = degree - left - middle
                    weight = (
                        math.factorial(degree)
                        // (
                            math.factorial(left)
                            * math.factorial(middle)
                            * math.factorial(right)
                        )
                    )
                    x_terms.append(col_alg.scale(
                        col_alg.product(
                            U[sample][left],
                            U[sample][middle],
                            U[sample][right],
                        ),
                        weight,
                    ))
            X[sample].append(col_alg.add(*x_terms))

        _set_forward_covariances(degree, X, column, row)

        for sample in range(2):
            forward = row_alg.variable(eta_index(sample, degree))
            for source in range(2):
                for other_degree in range(degree):
                    response = column.derivative_expectation(
                        X[sample][degree],
                        xi_index(source, other_degree),
                    )
                    if response != RHO_ZERO:
                        forward = row_alg.add(
                            forward,
                            row_alg.scale(B[source][other_degree], response),
                        )

            z_terms = [forward]
            for source in range(2):
                for b_degree in range(degree):
                    for x_left in range(degree - b_degree):
                        x_right = degree - 1 - b_degree - x_left
                        weight = (
                            Q(3, 2)
                            * math.comb(degree, x_right)
                            * math.comb(b_degree + x_left, b_degree)
                        )
                        overlap = column.product_expectation(
                            X[source][x_left], X[sample][x_right]
                        )
                        z_terms.append(row_alg.scale(
                            B[source][b_degree],
                            rho_scale(overlap, weight),
                        ))
            Z[sample].append(row_alg.add(*z_terms))

            g_terms: list[StatePolynomial] = []
            b_terms: list[StatePolynomial] = []
            for left in range(degree + 1):
                for middle in range(degree - left + 1):
                    right = degree - left - middle
                    weight = (
                        math.factorial(degree)
                        // (
                            math.factorial(left)
                            * math.factorial(middle)
                            * math.factorial(right)
                        )
                    )
                    g_terms.append(row_alg.scale(
                        row_alg.product(
                            Z[sample][left],
                            Z[sample][middle],
                            Z[sample][right],
                        ),
                        weight,
                    ))
                    b_terms.append(row_alg.scale(
                        row_alg.product(
                            A[left],
                            Z[sample][middle],
                            Z[sample][right],
                        ),
                        weight,
                    ))
            G[sample].append(row_alg.add(*g_terms))
            B[sample].append(row_alg.add(*b_terms))

        _set_backward_covariances(degree, B, row, column)

        for sample in range(2):
            backward = col_alg.variable(xi_index(sample, degree))
            for source in range(2):
                for other_degree in range(degree + 1):
                    response = row.derivative_expectation(
                        B[sample][degree],
                        eta_index(source, other_degree),
                    )
                    if response != RHO_ZERO:
                        backward = col_alg.add(
                            backward,
                            col_alg.scale(X[source][other_degree], response),
                        )

            r_terms = [backward]
            for source in range(2):
                for x_degree in range(degree):
                    for b_left in range(degree - x_degree):
                        b_right = degree - 1 - x_degree - b_left
                        weight = (
                            Q(3, 2)
                            * math.comb(degree, b_right)
                            * math.comb(x_degree + b_left, x_degree)
                        )
                        overlap = row.product_expectation(
                            B[source][b_left], B[sample][b_right]
                        )
                        r_terms.append(col_alg.scale(
                            X[source][x_degree],
                            rho_scale(overlap, weight),
                        ))
            R[sample].append(col_alg.add(*r_terms))

        current_counts = _state_counts(degree, U, X, A, Z, B, R)
        counts.append(current_counts)
        if progress:
            progress(_progress_line(
                "derivative", current_counts, time.perf_counter() - started
            ))

    sample_derivatives: list[list[RhoPolynomial]] = [[], []]
    for sample in range(2):
        for degree in range(max_order + 1):
            sample_derivatives[sample].append(rho_add(*(
                rho_scale(
                    row.product_expectation(A[left], G[sample][degree - left]),
                    math.comb(degree, left),
                )
                for left in range(degree + 1)
            )))
    derivatives = [
        rho_scale(
            rho_add(
                sample_derivatives[0][degree],
                sample_derivatives[1][degree],
            ),
            Q(1, 2),
        )
        for degree in range(max_order + 1)
    ]
    return JetResult(
        route="derivative",
        derivatives=derivatives,
        sample_derivatives=sample_derivatives,
        elapsed_seconds=time.perf_counter() - started,
        state_counts=counts,
        wick_cache_sizes={"column": len(column.cache), "row": len(row.cache)},
    )


def analytic_initial_kernel() -> RhoPolynomial:
    """Independent gradient-block Wick audit for ``F_+'(0; rho)``."""

    c = rho_add(rho_scale(RHO_VARIABLE, 9), rho_scale(rho_power(RHO_VARIABLE, 3), 6))
    readout = rho_scale(
        rho_add(rho_constant(50_625), rho_scale(c, 2_025), rho_scale(rho_power(c, 3), 6)),
        Q(1, 2),
    )
    middle = rho_scale(
        rho_add(
            rho_constant(10_125),
            rho_multiply(c, rho_add(rho_constant(225), rho_scale(rho_power(c, 2), 2))),
        ),
        Q(9, 2),
    )
    bottom = rho_scale(
        rho_add(
            rho_constant(2_025),
            rho_multiply(
                rho_multiply(
                    RHO_VARIABLE,
                    rho_add(RHO_ONE, rho_scale(rho_power(RHO_VARIABLE, 2), 2)),
                ),
                rho_add(rho_constant(225), rho_scale(rho_power(c, 2), 2)),
            ),
        ),
        Q(81, 2),
    )
    return rho_add(readout, middle, bottom)


def validate_results(results: Iterable[JetResult], max_order: int) -> None:
    results = list(results)
    initial = analytic_initial_kernel()
    for result in results:
        if max_order >= 1 and result.derivatives[1] != initial:
            raise AssertionError(
                f"{result.route}: analytic initial-kernel gate failed"
            )
        for order in range(0, max_order + 1, 2):
            if result.derivatives[order] != RHO_ZERO:
                raise AssertionError(
                    f"{result.route}: parity gate F^{order} failed"
                )
        for sample in range(2):
            if result.sample_derivatives[sample] != result.derivatives:
                raise AssertionError(
                    f"{result.route}: exchange-symmetry gate failed"
                )
        if max_order >= 1:
            if rho_evaluate(result.derivatives[1], 1) != 305_775:
                raise AssertionError(f"{result.route}: rho=1 F^1 gate failed")
            if rho_evaluate(result.derivatives[1], -1) != 0:
                raise AssertionError(f"{result.route}: rho=-1 F^1 gate failed")
        if max_order >= 3:
            if (
                rho_evaluate(result.derivatives[3], 1)
                != 154_118_008_098_000
            ):
                raise AssertionError(f"{result.route}: rho=1 F^3 gate failed")
            if rho_evaluate(result.derivatives[3], -1) != 0:
                raise AssertionError(f"{result.route}: rho=-1 F^3 gate failed")
    if len(results) == 2 and results[0].derivatives != results[1].derivatives:
        raise AssertionError("Taylor and derivative-normalized routes disagree")


def _serialize_result(result: JetResult) -> dict[str, object]:
    return {
        "route": result.route,
        "derivatives_coefficient_lists": [
            rho_to_strings(polynomial) for polynomial in result.derivatives
        ],
        "derivatives_expressions": [
            rho_expression(polynomial) for polynomial in result.derivatives
        ],
        "elapsed_seconds": result.elapsed_seconds,
        "state_counts": result.state_counts,
        "wick_cache_sizes": result.wick_cache_sizes,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-order", type=int, default=3)
    parser.add_argument(
        "--route", choices=("taylor", "derivative", "both"), default="both"
    )
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    actual_hash = sha256(PROTOCOL)
    if actual_hash != EXPECTED_PROTOCOL_SHA256:
        raise AssertionError(
            f"protocol SHA-256 gate failed: got {actual_hash}, "
            f"expected {EXPECTED_PROTOCOL_SHA256}"
        )

    progress: Progress | None = None if args.quiet else print
    routes = (
        ("taylor", "derivative") if args.route == "both" else (args.route,)
    )
    results: list[JetResult] = []
    for route in routes:
        assembler = taylor_jet if route == "taylor" else derivative_jet
        results.append(assembler(args.max_order, progress))
    validate_results(results, args.max_order)

    payload = {
        "model": "two-input-equal-label-raw-cubic-depth2-plus-channel",
        "input_correlation_variable": "rho",
        "max_order": args.max_order,
        "protocol_sha256": actual_hash,
        "analytic_initial_kernel": rho_expression(analytic_initial_kernel()),
        "validation": "passed",
        "results": [_serialize_result(result) for result in results],
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        for result in results:
            print(
                f"{result.route}: "
                + ", ".join(
                    f"F^{order}={rho_expression(value)}"
                    for order, value in enumerate(result.derivatives)
                )
            )
        print("validation: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
