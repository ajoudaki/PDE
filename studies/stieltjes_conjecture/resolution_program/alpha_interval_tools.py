#!/usr/bin/env python3
"""Exact univariate tools for the positive-alpha block-metric extension.

The coefficient convention is ascending throughout: ``p[k]`` is the
coefficient of ``alpha**k``.  The only rational functions needed by the
formal inversion have denominators which are powers of

    c(alpha) = F_alpha'(0).

Keeping that structure explicit avoids a dependency on a computer algebra
system and makes the final sign certificate independently reproducible with
the Python standard library.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Sequence


Q = Fraction
Poly = tuple[Fraction, ...]


def poly(values: Iterable[int | Fraction]) -> Poly:
    """Return a trimmed polynomial from ascending coefficients."""

    result = tuple(Q(value) for value in values)
    end = len(result)
    while end > 1 and result[end - 1] == 0:
        end -= 1
    return result[:end] if result else (Q(0),)


ZERO = poly([0])
ONE = poly([1])


def pneg(value: Poly) -> Poly:
    return poly(-coefficient for coefficient in value)


def padd(left: Poly, right: Poly) -> Poly:
    length = max(len(left), len(right))
    return poly(
        (left[index] if index < len(left) else Q(0))
        + (right[index] if index < len(right) else Q(0))
        for index in range(length)
    )


def pmul(left: Poly, right: Poly) -> Poly:
    result = [Q(0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] += left_value * right_value
    return poly(result)


def pscale(value: Poly, scalar: int | Fraction) -> Poly:
    scalar = Q(scalar)
    return poly(scalar * coefficient for coefficient in value)


def ppow(value: Poly, exponent: int) -> Poly:
    if exponent < 0:
        raise ValueError("polynomial exponent must be nonnegative")
    result = ONE
    base = value
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = pmul(result, base)
        base = pmul(base, base)
        remaining //= 2
    return result


def peval(value: Poly, point: int | Fraction) -> Fraction:
    point = Q(point)
    result = Q(0)
    for coefficient in reversed(value):
        result = result * point + coefficient
    return result


def pdivmod(dividend: Poly, divisor: Poly) -> tuple[Poly, Poly]:
    """Exact polynomial long division over the rationals."""

    if divisor == ZERO:
        raise ZeroDivisionError("polynomial division by zero")
    remainder = list(dividend)
    quotient = [Q(0)] * max(1, len(dividend) - len(divisor) + 1)
    while len(remainder) >= len(divisor) and any(remainder):
        offset = len(remainder) - len(divisor)
        factor = remainder[-1] / divisor[-1]
        quotient[offset] += factor
        for index, coefficient in enumerate(divisor):
            remainder[offset + index] -= factor * coefficient
        while len(remainder) > 1 and remainder[-1] == 0:
            remainder.pop()
    return poly(quotient), poly(remainder)


@dataclass(frozen=True)
class CPowerFraction:
    """A polynomial numerator divided by a nonnegative power of ``c``."""

    numerator: Poly
    c_power: int
    c: Poly

    def __post_init__(self) -> None:
        if self.c_power < 0:
            raise ValueError("negative denominator power")
        if self.c == ZERO:
            raise ValueError("the distinguished denominator is zero")
        numerator = poly(self.numerator)
        c_power = self.c_power
        if numerator == ZERO:
            c_power = 0
        else:
            # Formal inversion often creates a common factor c before an
            # addition aligns denominator powers.  Remove it exactly so the
            # structural powers mu_r:c^(3r+2), Delta:c^33 remain visible.
            while c_power:
                quotient, remainder = pdivmod(numerator, self.c)
                if remainder != ZERO:
                    break
                numerator = quotient
                c_power -= 1
        object.__setattr__(self, "numerator", numerator)
        object.__setattr__(self, "c_power", c_power)

    @classmethod
    def zero(cls, c: Poly) -> "CPowerFraction":
        return cls(ZERO, 0, c)

    def neg(self) -> "CPowerFraction":
        return CPowerFraction(pneg(self.numerator), self.c_power, self.c)

    def add(self, other: "CPowerFraction") -> "CPowerFraction":
        if self.c != other.c:
            raise ValueError("incompatible distinguished denominators")
        target = max(self.c_power, other.c_power)
        left = pmul(self.numerator, ppow(self.c, target - self.c_power))
        right = pmul(other.numerator, ppow(self.c, target - other.c_power))
        return CPowerFraction(padd(left, right), target, self.c)

    def mul(self, other: "CPowerFraction") -> "CPowerFraction":
        if self.c != other.c:
            raise ValueError("incompatible distinguished denominators")
        return CPowerFraction(
            pmul(self.numerator, other.numerator),
            self.c_power + other.c_power,
            self.c,
        )

    def mul_poly(self, value: Poly) -> "CPowerFraction":
        return CPowerFraction(pmul(self.numerator, value), self.c_power, self.c)

    def mul_c(self) -> "CPowerFraction":
        if self.c_power:
            return CPowerFraction(self.numerator, self.c_power - 1, self.c)
        return self.mul_poly(self.c)

    def div_c(self) -> "CPowerFraction":
        return CPowerFraction(self.numerator, self.c_power + 1, self.c)

    def to_power(self, target: int) -> "CPowerFraction":
        if target < self.c_power:
            raise ValueError("cannot lower the denominator power without division")
        return CPowerFraction(
            pmul(self.numerator, ppow(self.c, target - self.c_power)),
            target,
            self.c,
        )

    def evaluate(self, point: int | Fraction) -> Fraction:
        denominator = peval(self.c, point) ** self.c_power
        if not denominator:
            raise ZeroDivisionError("distinguished denominator vanishes")
        return peval(self.numerator, point) / denominator


def rat_sum(values: Iterable[CPowerFraction], c: Poly) -> CPowerFraction:
    result = CPowerFraction.zero(c)
    for value in values:
        result = result.add(value)
    return result


def series_product(
    left: Sequence[CPowerFraction],
    right: Sequence[CPowerFraction],
    length: int,
    c: Poly,
) -> list[CPowerFraction]:
    result = [CPowerFraction.zero(c) for _ in range(length)]
    for i, left_value in enumerate(left[:length]):
        for j, right_value in enumerate(right[: length - i]):
            result[i + j] = result[i + j].add(left_value.mul(right_value))
    return result


def series_power(
    value: Sequence[CPowerFraction], exponent: int, length: int, c: Poly
) -> list[CPowerFraction]:
    if exponent < 0:
        raise ValueError("series exponent must be nonnegative")
    result = [CPowerFraction(ONE, 0, c)] + [
        CPowerFraction.zero(c) for _ in range(length - 1)
    ]
    base = list(value[:length]) + [
        CPowerFraction.zero(c) for _ in range(max(0, length - len(value)))
    ]
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = series_product(result, base, length, c)
        base = series_product(base, base, length, c)
        remaining //= 2
    return result


def inverse_psi_series(psi: Sequence[Poly], length: int) -> list[CPowerFraction]:
    """Return the truncated reciprocal of ``sum psi[k] x**k``."""

    if not psi or psi[0] == ZERO:
        raise ValueError("psi must have nonzero constant polynomial")
    c = psi[0]
    result = [CPowerFraction(ONE, 1, c)]
    for degree in range(1, length):
        total = rat_sum(
            (
                result[degree - index].mul_poly(psi[index])
                for index in range(1, min(degree, len(psi) - 1) + 1)
            ),
            c,
        )
        result.append(total.neg().div_c())
    return result


def output_kernel_moments_from_jets(
    odd_derivative_polynomials: Sequence[Poly], count: int = 6
) -> list[CPowerFraction]:
    """Compute ``mu_0,...,mu_(count-1)`` from exact odd derivative jets.

    ``odd_derivative_polynomials[r]`` is ``F^(2r+1)(0)``.  Computing six
    output-kernel moments requires seven entries, through ``F^(13)(0)``.
    """

    if len(odd_derivative_polynomials) < count + 1:
        raise ValueError("insufficient odd derivatives")
    psi = [
        pscale(odd_derivative_polynomials[index], Q(1, math.factorial(2 * index + 1)))
        for index in range(count + 1)
    ]
    c = psi[0]
    inverse_psi = inverse_psi_series(psi, count + 1)

    # H_n=[x^n]psi(x)^(-(2n+1)); H(x)=G'(sqrt(x)).
    h_coefficients: list[CPowerFraction] = []
    for degree in range(count + 1):
        powered = series_power(inverse_psi, 2 * degree + 1, degree + 1, c)
        h_coefficients.append(powered[degree])

    # K=1/H, using H_0=1/c exactly.
    kernel = [CPowerFraction(c, 0, c)]
    for degree in range(1, count + 1):
        convolution = rat_sum(
            (
                h_coefficients[index].mul(kernel[degree - index])
                for index in range(1, degree + 1)
            ),
            c,
        )
        kernel.append(convolution.neg().mul_c())

    return [
        kernel[degree + 1] if degree % 2 == 0 else kernel[degree + 1].neg()
        for degree in range(count)
    ]


def determinant3(matrix: Sequence[Sequence[CPowerFraction]]) -> CPowerFraction:
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("expected a 3 by 3 matrix")
    c = matrix[0][0].c
    positive = rat_sum(
        (
            matrix[0][0].mul(matrix[1][1]).mul(matrix[2][2]),
            matrix[0][1].mul(matrix[1][2]).mul(matrix[2][0]),
            matrix[0][2].mul(matrix[1][0]).mul(matrix[2][1]),
        ),
        c,
    )
    negative = rat_sum(
        (
            matrix[0][2].mul(matrix[1][1]).mul(matrix[2][0]),
            matrix[0][1].mul(matrix[1][0]).mul(matrix[2][2]),
            matrix[0][0].mul(matrix[1][2]).mul(matrix[2][1]),
        ),
        c,
    )
    return positive.add(negative.neg())


def shifted_h2_from_jets(odd_derivative_polynomials: Sequence[Poly]) -> CPowerFraction:
    moments = output_kernel_moments_from_jets(odd_derivative_polynomials, 6)
    matrix = [[moments[row + column + 1] for column in range(3)] for row in range(3)]
    return determinant3(matrix).to_power(33)


def primitive_integer_polynomial(value: Poly) -> tuple[int, ...]:
    common_denominator = 1
    for coefficient in value:
        common_denominator = math.lcm(common_denominator, coefficient.denominator)
    integers = [
        coefficient.numerator * (common_denominator // coefficient.denominator)
        for coefficient in value
    ]
    divisor = math.gcd(*[abs(coefficient) for coefficient in integers])
    if not divisor:
        return (0,)
    return tuple(coefficient // divisor for coefficient in integers)


def elementary_negative_interval(value: Sequence[int], epsilon: Fraction | None = None) -> Fraction:
    """Return/check a rational interval using a positive-coefficient bound.

    For 0<=x<=epsilon<=1, x**k<=x for k>=1.  Dropping every negative
    nonconstant term therefore gives

        P(x) <= P(0) + x sum_{k>=1} max(P_k,0).

    """

    if not value or value[0] >= 0:
        raise ValueError("the constant coefficient must be negative")
    positive_tail = sum(max(coefficient, 0) for coefficient in value[1:])
    automatic = Q(1) if not positive_tail else min(Q(1), Q(-value[0], 2 * positive_tail))
    epsilon = automatic if epsilon is None else Q(epsilon)
    if epsilon <= 0 or epsilon > 1:
        raise ValueError("epsilon must lie in (0,1]")
    if positive_tail and value[0] + epsilon * positive_tail >= 0:
        raise ValueError("coefficient bound does not certify this epsilon")
    return epsilon


def bernstein_coefficients_on_interval(
    value: Sequence[int | Fraction], epsilon: int | Fraction
) -> tuple[Fraction, ...]:
    """Bernstein coefficients of ``P(epsilon*t)`` on ``0<=t<=1``."""

    epsilon = Q(epsilon)
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    degree = len(value) - 1
    power = [Q(coefficient) * epsilon**index for index, coefficient in enumerate(value)]
    return tuple(
        sum(
            power[index] * Q(math.comb(position, index), math.comb(degree, index))
            for index in range(position + 1)
        )
        for position in range(degree + 1)
    )


def certify_negative_by_bernstein(
    value: Sequence[int | Fraction], epsilon: int | Fraction
) -> tuple[Fraction, ...]:
    """Return an exact certificate if every Bernstein coefficient is negative."""

    coefficients = bernstein_coefficients_on_interval(value, epsilon)
    if not all(coefficient < 0 for coefficient in coefficients):
        raise ValueError("Bernstein coefficients do not all certify negativity")
    return coefficients


def fraction_string(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def build_interval_certificate(
    odd_derivative_polynomials: Sequence[Poly],
    epsilon: int | Fraction,
) -> dict[str, object]:
    """Build an exact sign certificate for the shifted Hankel determinant.

    The returned primitive polynomial ``P`` and positive scalar ``s`` obey

        Delta(alpha) = s P(alpha) / F_alpha'(0)**33.

    Negativity is checked twice: all Bernstein coefficients on the requested
    interval must be negative, and (when applicable) the compact convexity
    certificate ``P_0,P(epsilon)<0`` with ``P_k>0`` for ``k>=2`` is recorded.
    """

    epsilon = Q(epsilon)
    determinant = shifted_h2_from_jets(odd_derivative_polynomials)
    if determinant.c_power != 33:
        raise AssertionError(
            f"unexpected determinant denominator power {determinant.c_power}"
        )
    primitive = primitive_integer_polynomial(determinant.numerator)
    first_nonzero = next(index for index, value in enumerate(primitive) if value)
    scale = determinant.numerator[first_nonzero] / primitive[first_nonzero]
    if scale <= 0:
        raise AssertionError("primitive-polynomial scale must be positive")
    if any(
        determinant.numerator[index] != scale * primitive[index]
        for index in range(len(primitive))
    ):
        raise AssertionError("primitive-polynomial normalization failed")

    bernstein = certify_negative_by_bernstein(primitive, epsilon)
    endpoint = peval(poly(primitive), epsilon)
    convex_tail = all(coefficient > 0 for coefficient in primitive[2:])
    convexity_certificate = primitive[0] < 0 and endpoint < 0 and convex_tail
    maximum = max(bernstein)
    return {
        "baseline_polynomial_ascending": [fraction_string(value) for value in determinant.c],
        "denominator_power": determinant.c_power,
        "positive_primitive_scale": fraction_string(scale),
        "primitive_numerator_degree": len(primitive) - 1,
        "primitive_numerator_ascending": [str(value) for value in primitive],
        "epsilon": fraction_string(epsilon),
        "P_at_zero": str(primitive[0]),
        "P_at_epsilon": fraction_string(endpoint),
        "strictly_positive_coefficients_from_degree_2": convex_tail,
        "convexity_certificate": convexity_certificate,
        "bernstein_coefficient_count": len(bernstein),
        "all_bernstein_coefficients_strictly_negative": True,
        "largest_bernstein_coefficient_index": bernstein.index(maximum),
        "largest_bernstein_coefficient": fraction_string(maximum),
    }
