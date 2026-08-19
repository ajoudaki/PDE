#!/usr/bin/env python3
"""Exact certificate for the (alpha,beta)=(0,1) block-metric counterexample.

The calculation uses only ``fractions.Fraction``.  It independently reduces
the width-limit feature jet to the two-variable derivation

    X = z^2 d/da + 6 a z d/dz

and then performs formal Lagrange inversion.  No floating-point arithmetic is
used in the certificate.
"""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable


Q = Fraction
Monomial = tuple[int, int]
Polynomial = dict[Monomial, Fraction]

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
CAMPAIGN4_RESULTS = (
    REPO
    / "studies/mean_field_peeling/quadratic_compiler/campaign4/results_order9.json"
)
CAMPAIGN4_RESULTS_SHA256 = (
    "530ef0818f4142eb162c28fa6b388d69a1e13eeb9de399d54a25008d591f6d5e"
)


def apply_limit_derivation(poly: Polynomial) -> Polynomial:
    """Apply X=z^2 partial_a+6az partial_z to a polynomial."""

    result: Polynomial = {}
    for (a_power, z_power), coefficient in poly.items():
        if a_power:
            key = (a_power - 1, z_power + 2)
            result[key] = result.get(key, Q(0)) + coefficient * a_power
        if z_power:
            key = (a_power + 1, z_power)
            result[key] = result.get(key, Q(0)) + 6 * coefficient * z_power
    return {key: value for key, value in result.items() if value}


def odd_double_factorial(number: int) -> int:
    """Return number!! for odd number >= -1."""

    if number in (-1, 0):
        return 1
    value = 1
    for factor in range(number, 0, -2):
        value *= factor
    return value


def gaussian_expectation(poly: Polynomial) -> Fraction:
    """Expectation for independent a~N(0,1), z~N(0,3)."""

    total = Q(0)
    for (a_power, z_power), coefficient in poly.items():
        if a_power % 2 or z_power % 2:
            continue
        total += (
            coefficient
            * odd_double_factorial(a_power - 1)
            * odd_double_factorial(z_power - 1)
            * 3 ** (z_power // 2)
        )
    return total


def feature_derivatives(max_order: int = 13) -> list[Fraction]:
    """Return F^(k)(0)=E[X^k(a z^2)] through ``max_order``."""

    poly: Polynomial = {(1, 2): Q(1)}
    derivatives: list[Fraction] = []
    for _ in range(max_order + 1):
        derivatives.append(gaussian_expectation(poly))
        poly = apply_limit_derivation(poly)
    return derivatives


def multiply_series(
    left: list[Fraction], right: list[Fraction], length: int
) -> list[Fraction]:
    result = [Q(0) for _ in range(length)]
    for i, left_value in enumerate(left[:length]):
        for j, right_value in enumerate(right[: length - i]):
            result[i + j] += left_value * right_value
    return result


def invert_series(series: list[Fraction], length: int) -> list[Fraction]:
    if not series or not series[0]:
        raise ValueError("series must have a nonzero constant term")
    result = [Q(0) for _ in range(length)]
    result[0] = 1 / series[0]
    for degree in range(1, length):
        result[degree] = -sum(
            series[index] * result[degree - index]
            for index in range(1, degree + 1)
        ) / series[0]
    return result


def power_series(
    series: list[Fraction], exponent: int, length: int
) -> list[Fraction]:
    if exponent < 0:
        return power_series(invert_series(series, length), -exponent, length)
    result = [Q(1)] + [Q(0) for _ in range(length - 1)]
    base = series[:length] + [Q(0) for _ in range(max(0, length - len(series)))]
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = multiply_series(result, base, length)
        base = multiply_series(base, base, length)
        remaining //= 2
    return result


def inverse_derivative_moments(
    derivatives: list[Fraction], count: int = 7
) -> list[Fraction]:
    """Compute h_n=(-1)^n[z^n]psi(z)^(-(2n+1))."""

    psi = [
        derivatives[2 * degree + 1] / math.factorial(2 * degree + 1)
        for degree in range(count)
    ]
    moments = []
    for degree in range(count):
        coefficient = power_series(psi, -(2 * degree + 1), degree + 1)[degree]
        moments.append((-1) ** degree * coefficient)
    return moments


def output_kernel_moments(h_moments: list[Fraction]) -> list[Fraction]:
    """Recover mu from 1/H(x)=K(sqrt(x))=c+xR(x)."""

    signed_h = [(-1) ** degree * value for degree, value in enumerate(h_moments)]
    reciprocal = invert_series(signed_h, len(signed_h))
    return [
        (-1) ** degree * reciprocal[degree + 1]
        for degree in range(len(h_moments) - 1)
    ]


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    """Exact determinant by fraction-preserving Gaussian elimination."""

    work = [row[:] for row in matrix]
    size = len(work)
    if any(len(row) != size for row in work):
        raise ValueError("determinant requires a square matrix")
    sign = 1
    value = Q(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column]), None
        )
        if pivot is None:
            return Q(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign *= -1
        pivot_value = work[column][column]
        value *= pivot_value
        for row in range(column + 1, size):
            ratio = work[row][column] / pivot_value
            for index in range(column, size):
                work[row][index] -= ratio * work[column][index]
    return sign * value


def hankel(moments: list[Fraction], size: int, shift: int = 0) -> list[list[Fraction]]:
    return [
        [moments[row + column + shift] for column in range(size)]
        for row in range(size)
    ]


def quadratic_form(matrix: list[list[Fraction]], vector: list[int | Fraction]) -> Fraction:
    return sum(
        Q(vector[row]) * matrix[row][column] * Q(vector[column])
        for row in range(len(matrix))
        for column in range(len(matrix))
    )


def lcm(values: Iterable[int]) -> int:
    result = 1
    for value in values:
        result = math.lcm(result, value)
    return result


def primitive_integer_vector(values: list[Fraction]) -> list[int]:
    denominator = lcm(value.denominator for value in values)
    integers = [value.numerator * (denominator // value.denominator) for value in values]
    divisor = math.gcd(*[abs(value) for value in integers])
    return [value // divisor for value in integers]


def shifted_schur_witness(moments: list[Fraction]) -> tuple[list[Fraction], list[int]]:
    """Return monic quadratic and primitive integer witness for shifted H_2."""

    mu1, mu2, mu3, mu4 = moments[1:5]
    delta = mu1 * mu3 - mu2 * mu2
    if delta <= 0:
        raise ValueError("leading shifted 2x2 block must be positive")
    constant = (mu2 * mu4 - mu3 * mu3) / delta
    linear = (mu2 * mu3 - mu1 * mu4) / delta
    rational = [constant, linear, Q(1)]
    return rational, primitive_integer_vector(rational)


def evaluate_campaign4_axis() -> dict[int, int]:
    """Evaluate retained Campaign-4 jets at alpha=0,beta=1."""

    digest = hashlib.sha256(CAMPAIGN4_RESULTS.read_bytes()).hexdigest()
    if digest != CAMPAIGN4_RESULTS_SHA256:
        raise AssertionError(f"Campaign-4 source hash mismatch: {digest}")
    document = json.loads(CAMPAIGN4_RESULTS.read_text())
    result: dict[int, int] = {}
    for jet in document["jets"]:
        order = int(jet["order"])
        result[order] = sum(
            int(term["value"])
            for term in jet["monomials"]
            if int(term["alpha_power"]) == 0
        )
    return result


def fraction_string(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def build_certificate() -> dict[str, object]:
    derivatives = feature_derivatives(13)
    h_moments = inverse_derivative_moments(derivatives, 7)
    mu_moments = output_kernel_moments(h_moments)
    campaign4 = evaluate_campaign4_axis()

    for order in range(10):
        if derivatives[order] != campaign4[order]:
            raise AssertionError(
                f"Campaign-4 mismatch at order {order}: "
                f"{derivatives[order]} != {campaign4[order]}"
            )

    ordinary_h3 = determinant(hankel(h_moments, 4))
    shifted_mu2_matrix = hankel(mu_moments, 3, shift=1)
    shifted_mu2 = determinant(shifted_mu2_matrix)
    rational_witness, integer_witness = shifted_schur_witness(mu_moments)
    rational_witness_value = quadratic_form(shifted_mu2_matrix, rational_witness)
    integer_witness_value = quadratic_form(shifted_mu2_matrix, integer_witness)

    expected_derivatives = {
        1: 63,
        3: 77760,
        5: 274547232,
        7: 2141006515200,
        9: 31149221916487680,
        11: 759035131220036321280,
        13: 28719223368439752070594560,
    }
    if any(derivatives[order] != value for order, value in expected_derivatives.items()):
        raise AssertionError("feature-derivative regression mismatch")
    if any(derivatives[order] for order in range(0, 14, 2)):
        raise AssertionError("feature parity failed")

    expected_mu_prefix = [
        Q(480, 49),
        Q(43756, 151263),
        Q(7214528, 200120949),
        Q(12545175968, 2402451992745),
    ]
    if mu_moments[:4] != expected_mu_prefix:
        raise AssertionError("retained Campaign-4 moment prefix mismatch")
    if shifted_mu2 >= 0 or ordinary_h3 >= 0:
        raise AssertionError("counterexample determinant is not negative")
    if rational_witness_value >= 0 or integer_witness_value >= 0:
        raise AssertionError("counterexample quadratic form is not negative")

    preceding_mu_minors = {
        "ordinary_H0": determinant(hankel(mu_moments, 1)),
        "ordinary_H1": determinant(hankel(mu_moments, 2)),
        "ordinary_H2": determinant(hankel(mu_moments, 3)),
        "shifted_H0": determinant(hankel(mu_moments, 1, shift=1)),
        "shifted_H1": determinant(hankel(mu_moments, 2, shift=1)),
    }
    if any(value <= 0 for value in preceding_mu_minors.values()):
        raise AssertionError("a preceding output-kernel Hankel minor is nonpositive")

    return {
        "schema": "block_metric_stieltjes_counterexample_v1",
        "metric": {"alpha": 0, "beta": 1},
        "limit_derivation": "X=z^2*d/da+6*a*z*d/dz",
        "initial_law": "a~N(0,1), z~N(0,3), independent",
        "campaign4_results_sha256": CAMPAIGN4_RESULTS_SHA256,
        "feature_derivatives": {
            str(order): fraction_string(derivatives[order]) for order in range(14)
        },
        "inverse_derivative_moments_h": [
            fraction_string(value) for value in h_moments
        ],
        "output_kernel_moments_mu": [
            fraction_string(value) for value in mu_moments
        ],
        "preceding_output_kernel_minors": {
            key: fraction_string(value) for key, value in preceding_mu_minors.items()
        },
        "negative_shifted_H2_determinant": fraction_string(shifted_mu2),
        "negative_inverse_ordinary_H3_determinant": fraction_string(ordinary_h3),
        "monic_witness_coefficients_constant_to_quadratic": [
            fraction_string(value) for value in rational_witness
        ],
        "monic_witness_L_lambda_p_squared": fraction_string(rational_witness_value),
        "primitive_integer_witness_constant_to_quadratic": integer_witness,
        "integer_witness_L_lambda_p_squared": fraction_string(integer_witness_value),
        "decision": "strong_block_metric_uniform_V1_is_false",
    }


def main() -> None:
    print(json.dumps(build_certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
