"""Exact scalar Euler audit of the general-t narrow-transition symbol."""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial


ORDER = 5
ZERO_MONOMIAL = (0,) * 5  # powers of p, A, B, C, D
Polynomial = dict[tuple[int, ...], Fraction]
Series = list[Polynomial]


def poly_add(left: Polynomial, right: Polynomial) -> Polynomial:
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = out.get(monomial, Fraction(0)) + coefficient
    return {key: value for key, value in out.items() if value}


def poly_scale(poly: Polynomial, coefficient: Fraction) -> Polynomial:
    return {key: value * coefficient for key, value in poly.items() if value * coefficient}


def poly_mul(left: Polynomial, right: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for a, ca in left.items():
        for b, cb in right.items():
            key = tuple(x + y for x, y in zip(a, b))
            out[key] = out.get(key, Fraction(0)) + ca * cb
    return {key: value for key, value in out.items() if value}


def zero_series() -> Series:
    return [{} for _ in range(ORDER + 1)]


def series_add(left: Series, right: Series) -> Series:
    return [poly_add(a, b) for a, b in zip(left, right)]


def series_mul(left: Series, right: Series) -> Series:
    out = zero_series()
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= ORDER:
                out[i + j] = poly_add(out[i + j], poly_mul(a, b))
    return out


def series_power(series: Series, exponent: int) -> Series:
    out = zero_series()
    out[0] = {ZERO_MONOMIAL: Fraction(1)}
    for _ in range(exponent):
        out = series_mul(out, series)
    return out


VARIABLES = []
for index in range(5):
    exponent = [0] * 5
    exponent[index] = 1
    VARIABLES.append({tuple(exponent): Fraction(1)})


def compose(delta: Series, *, derivative_shift: int) -> Series:
    """Compose g or f with x+delta using derivatives p,A,B,C,D."""

    out = zero_series()
    for power, variable in enumerate(VARIABLES, start=derivative_shift):
        term = series_power(delta, power)
        scale = Fraction(1, factorial(power))
        term = [poly_mul(variable, poly_scale(coefficient, scale)) for coefficient in term]
        out = series_add(out, term)
    return out


def fifth_output_after_steps(steps: int) -> Polynomial:
    delta = zero_series()
    for _ in range(steps):
        gradient = compose(delta, derivative_shift=0)
        update = zero_series()
        for order in range(ORDER):
            update[order + 1] = gradient[order]
        delta = series_add(delta, update)
    return compose(delta, derivative_shift=1)[5]


MONOMIAL_D = (5, 0, 0, 0, 1)
MONOMIAL_CA = (4, 1, 0, 1, 0)
MONOMIAL_B2 = (4, 0, 2, 0, 0)


def local_weight(steps: int) -> Fraction:
    fifth = fifth_output_after_steps(steps)
    return (
        5 * fifth.get(MONOMIAL_D, Fraction(0))
        - fifth.get(MONOMIAL_CA, Fraction(0))
        + fifth.get(MONOMIAL_B2, Fraction(0))
    )


def binomial_formula(steps: int) -> Fraction:
    coefficients = (
        Fraction(1, 24),
        Fraction(19, 24),
        Fraction(13, 4),
        Fraction(9, 2),
        Fraction(2),
    )
    return sum(coefficient * comb(steps, index) for index, coefficient in enumerate(coefficients, 1))


def main() -> None:
    # The order-five chronology has degree at most five in the step count.
    # Six exact values therefore determine it.  Extra values are checked as
    # an independent recurrence guard.
    for steps in range(13):
        assert local_weight(steps) == binomial_formula(steps)

    for t in range(1, 7):
        paired = local_weight(2 * t) - 32 * local_weight(t)
        expected = -Fraction(8 * t**4 + 3 * t, 24)
        assert paired == expected
        print(t, paired)


if __name__ == "__main__":
    main()
