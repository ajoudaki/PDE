"""Small exact formal-series primitives used by the proxy inventory.

All coefficients are :class:`fractions.Fraction`.  The routines are purposely
minimal: they implement only multiplication, composition, reciprocal series,
and reversion around a nonzero linear term.  This keeps the transformation
from accepted MFP jets to output-coordinate moments independently testable.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
from typing import Mapping, Sequence


Q = Fraction


def as_fraction(value: int | str | float | Fraction) -> Fraction:
    """Convert a public numeric input without inheriting binary-float noise."""
    if isinstance(value, Fraction):
        return value
    if isinstance(value, bool):
        raise TypeError("booleans are not rational coefficients")
    if isinstance(value, float):
        return Fraction(str(value))
    return Fraction(value)


def pad(series: Sequence[Fraction], degree: int) -> list[Fraction]:
    return list(series[: degree + 1]) + [Q(0)] * max(0, degree + 1 - len(series))


def multiply(
    left: Sequence[Fraction], right: Sequence[Fraction], degree: int
) -> list[Fraction]:
    out = [Q(0) for _ in range(degree + 1)]
    for i, a in enumerate(left):
        if i > degree or not a:
            continue
        for j, b in enumerate(right):
            if i + j > degree:
                break
            if b:
                out[i + j] += a * b
    return out


def compose(
    outer: Sequence[Fraction], inner: Sequence[Fraction], degree: int
) -> list[Fraction]:
    """Return ``outer(inner(x))`` through ``x**degree`` exactly."""
    inner = pad(inner, degree)
    if inner[0]:
        raise ValueError("composition requires an inner series with zero constant")
    out = [Q(0) for _ in range(degree + 1)]
    power = [Q(1)] + [Q(0)] * degree
    for coefficient in outer[: degree + 1]:
        if coefficient:
            for index, value in enumerate(power):
                out[index] += coefficient * value
        power = multiply(power, inner, degree)
    return out


def reciprocal(series: Sequence[Fraction], degree: int) -> list[Fraction]:
    """Return the reciprocal of a series with nonzero constant term."""
    series = pad(series, degree)
    if not series[0]:
        raise ZeroDivisionError("series reciprocal requires nonzero constant")
    out = [Q(0) for _ in range(degree + 1)]
    out[0] = 1 / series[0]
    for n in range(1, degree + 1):
        out[n] = -sum(series[k] * out[n - k] for k in range(1, n + 1)) / series[0]
    return out


def reverse(series: Sequence[Fraction], degree: int) -> list[Fraction]:
    """Reverse ``y=series(x)`` about zero through ``y**degree``."""
    series = pad(series, degree)
    if series[0]:
        raise ValueError("series reversion requires zero constant")
    if not series[1]:
        raise ValueError("series reversion requires nonzero linear coefficient")
    out = [Q(0) for _ in range(degree + 1)]
    out[1] = 1 / series[1]
    for order in range(2, degree + 1):
        # With out[order] temporarily zero, every nonlinear power is already
        # determined.  The missing contribution is series[1]*out[order].
        composed = compose(series, out, order)
        out[order] = -composed[order] / series[1]
    return out


def output_kernel_moments(
    odd_derivatives: Mapping[int, Fraction | int | str],
) -> tuple[Fraction, tuple[Fraction, ...]]:
    """Transform exact odd feature jets into ``K`` baseline and moments.

    ``odd_derivatives[k]`` is ``F^(k)(0)`` for consecutive positive odd
    orders.  If the largest supplied order is ``2m+3``, the return contains
    ``mu_0,...,mu_m`` for

    ``K(y) = K(0) + sum_r (-1)^r mu_r y^(2r+2)``.
    """
    derivatives = {int(k): as_fraction(v) for k, v in odd_derivatives.items()}
    if not derivatives or min(derivatives) != 1:
        raise ValueError("the order-one derivative is required")
    max_order = max(derivatives)
    expected = set(range(1, max_order + 1, 2))
    if set(derivatives) != expected:
        raise ValueError("odd derivatives must be consecutive")
    if not derivatives[1]:
        raise ValueError("F'(0) must be nonzero")

    degree = max_order - 1
    feature = [Q(0) for _ in range(max_order + 1)]
    derivative = [Q(0) for _ in range(degree + 1)]
    for order, value in derivatives.items():
        feature[order] = value / factorial(order)
        derivative[order - 1] = value / factorial(order - 1)

    inverse = reverse(feature, degree)
    kernel = compose(derivative, inverse, degree)
    moments = tuple(
        ((-1) ** r) * kernel[2 * r + 2]
        for r in range((max_order - 1) // 2)
    )
    if any(kernel[k] for k in range(1, degree + 1, 2)):
        raise ArithmeticError("parity regression: transformed kernel is not even")
    return kernel[0], moments


def companion_moments(
    odd_feature_derivatives: Mapping[int, Fraction | int | str],
    even_observable_derivatives: Mapping[int, Fraction | int | str],
) -> tuple[Fraction, tuple[Fraction, ...]]:
    """Transform an even observable to output coordinates exactly.

    For ``N(y)=Q(F^{-1}(y))`` the return is ``N(0)`` and the moments of
    ``(N(sqrt(x))-N(0))/x``.
    """
    f_derivatives = {
        int(k): as_fraction(v) for k, v in odd_feature_derivatives.items()
    }
    q_derivatives = {
        int(k): as_fraction(v) for k, v in even_observable_derivatives.items()
    }
    max_q = max(q_derivatives)
    if set(q_derivatives) != set(range(0, max_q + 1, 2)):
        raise ValueError("even observable derivatives must be consecutive")
    if max(f_derivatives) < max_q + 1:
        raise ValueError("feature jet must extend one order beyond observable jet")

    feature = [Q(0) for _ in range(max_q + 2)]
    for order, value in f_derivatives.items():
        if order <= max_q + 1:
            feature[order] = value / factorial(order)
    inverse = reverse(feature, max_q)
    observable = [Q(0) for _ in range(max_q + 1)]
    for order, value in q_derivatives.items():
        observable[order] = value / factorial(order)
    transformed = compose(observable, inverse, max_q)
    moments = tuple(
        ((-1) ** r) * transformed[2 * r + 2]
        for r in range(max_q // 2)
    )
    if any(transformed[k] for k in range(1, max_q + 1, 2)):
        raise ArithmeticError("parity regression: transformed observable is not even")
    return transformed[0], moments
