"""Exact annealed controls that require no sampling.

The width-one evaluator uses rational sparse polynomials and exact Gaussian
Wick moments.  The arbitrary-width linear formulas are the result of the
same equality-partition enumeration (recorded in the audit note).
"""

from __future__ import annotations

from fractions import Fraction


Exponent3 = tuple[int, int, int]
RationalPolynomial = dict[Exponent3, Fraction]
ZERO = (0, 0, 0)


def _add(left: RationalPolynomial, right: RationalPolynomial) -> RationalPolynomial:
    out = dict(left)
    for exponent, coefficient in right.items():
        out[exponent] = out.get(exponent, Fraction(0)) + coefficient
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}


def _multiply(left: RationalPolynomial, right: RationalPolynomial) -> RationalPolynomial:
    out: RationalPolynomial = {}
    for alpha, left_coefficient in left.items():
        for beta, right_coefficient in right.items():
            exponent = tuple(a + b for a, b in zip(alpha, beta))
            out[exponent] = out.get(exponent, Fraction(0)) + left_coefficient * right_coefficient
    return out


def _scale(poly: RationalPolynomial, scalar: Fraction) -> RationalPolynomial:
    return {exponent: scalar * coefficient for exponent, coefficient in poly.items() if scalar * coefficient}


def _power(poly: RationalPolynomial, exponent: int) -> RationalPolynomial:
    out = {ZERO: Fraction(1)}
    for _ in range(exponent):
        out = _multiply(out, poly)
    return out


def _compose(coefficients: tuple[Fraction, ...], poly: RationalPolynomial) -> RationalPolynomial:
    out: RationalPolynomial = {}
    for exponent, coefficient in enumerate(coefficients):
        out = _add(out, _scale(_power(poly, exponent), coefficient))
    return out


def _differentiate(poly: RationalPolynomial, coordinate: int) -> RationalPolynomial:
    out: RationalPolynomial = {}
    for exponent, coefficient in poly.items():
        power = exponent[coordinate]
        if power:
            reduced = list(exponent)
            reduced[coordinate] -= 1
            out[tuple(reduced)] = coefficient * power
    return out


def _operator(f: RationalPolynomial, g: RationalPolynomial) -> RationalPolynomial:
    out: RationalPolynomial = {}
    for coordinate in range(3):
        out = _add(
            out,
            _multiply(_differentiate(f, coordinate), _differentiate(g, coordinate)),
        )
    return out


def _double_factorial_odd(power_minus_one: int) -> int:
    value = 1
    for factor in range(power_minus_one, 0, -2):
        value *= factor
    return value


def _gaussian_expectation(poly: RationalPolynomial) -> Fraction:
    result = Fraction(0)
    for exponent, coefficient in poly.items():
        if any(power % 2 for power in exponent):
            continue
        term = coefficient
        for power in exponent:
            if power:
                term *= _double_factorial_odd(power - 1)
        result += term
    return result


def width_one_polynomial_annealed(coefficients, *, order: int = 5) -> tuple[Fraction, ...]:
    """Exact E[D^k f] at n=1, q0=1 for a polynomial activation."""

    coefficients = tuple(Fraction(value) for value in coefficients)
    x = {(1, 0, 0): Fraction(1)}
    middle = {(0, 1, 0): Fraction(1)}
    readout = {(0, 0, 1): Fraction(1)}
    hidden = _compose(coefficients, x)
    second_preactivation = _multiply(middle, hidden)
    output = _multiply(readout, _compose(coefficients, second_preactivation))
    current = output
    values = []
    for derivative_order in range(order + 1):
        values.append(_gaussian_expectation(current))
        if derivative_order != order:
            current = _operator(output, current)
    return tuple(values)


def linear_annealed(width: int) -> tuple[Fraction, ...]:
    """Exact all-width linear control through order five."""

    n = Fraction(width)
    return (
        Fraction(0),
        Fraction(3),
        Fraction(0),
        Fraction(48) + Fraction(60) / n,
        Fraction(0),
        Fraction(1464) + Fraction(4800) / n + Fraction(4320) / (n * n),
    )


QUADRATIC_LARGE_WIDTH = (Fraction(111), Fraction(1685184), Fraction(77400633120))


def linear_wick_enumeration(width: int, *, order: int = 5) -> tuple[Fraction, ...]:
    """Exact sparse-polynomial/Wick enumeration for the linear network.

    This is intended as a small-width audit oracle.  It expands the
    unnormalized trilinear polynomial

        P=sum_{i,j} a_i W_ij u_j

    with integer coefficients.  Since
    ``f=n^(-3/2)P`` and ``D=n grad(f).grad``,
    ``D^k f=n^{-(k+3)/2} (grad(P).grad)^k P``.
    Odd annealed derivative orders therefore have rational normalization;
    even ones vanish by parity.
    """

    if width < 1:
        raise ValueError("width must be positive")
    if not 0 <= order <= 5:
        raise ValueError("order must lie between zero and five")
    n = width
    dimension = n + n * n + n
    IntPolynomial = dict[tuple[int, ...], int]

    def variable(index: int) -> IntPolynomial:
        exponent = [0] * dimension
        exponent[index] = 1
        return {tuple(exponent): 1}

    def add(left: IntPolynomial, right: IntPolynomial) -> IntPolynomial:
        out = dict(left)
        for exponent, coefficient in right.items():
            out[exponent] = out.get(exponent, 0) + coefficient
        return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}

    def multiply(left: IntPolynomial, right: IntPolynomial) -> IntPolynomial:
        out: IntPolynomial = {}
        for alpha, left_coefficient in left.items():
            for beta, right_coefficient in right.items():
                exponent = tuple(a + b for a, b in zip(alpha, beta))
                out[exponent] = out.get(exponent, 0) + left_coefficient * right_coefficient
        return out

    def differentiate(poly: IntPolynomial, coordinate: int) -> IntPolynomial:
        out: IntPolynomial = {}
        for exponent, coefficient in poly.items():
            power = exponent[coordinate]
            if power:
                reduced = list(exponent)
                reduced[coordinate] -= 1
                out[tuple(reduced)] = coefficient * power
        return out

    def wick(poly: IntPolynomial) -> int:
        result = 0
        for exponent, coefficient in poly.items():
            if any(power % 2 for power in exponent):
                continue
            term = coefficient
            for power in exponent:
                if power:
                    term *= _double_factorial_odd(power - 1)
            result += term
        return result

    first = [variable(j) for j in range(n)]
    middle = [
        [variable(n + i * n + j) for j in range(n)]
        for i in range(n)
    ]
    readout = [variable(n + n * n + i) for i in range(n)]
    output: IntPolynomial = {}
    for i in range(n):
        for j in range(n):
            output = add(output, multiply(multiply(readout[i], middle[i][j]), first[j]))
    gradient_output = [differentiate(output, coordinate) for coordinate in range(dimension)]

    def unnormalized_operator(poly: IntPolynomial) -> IntPolynomial:
        result: IntPolynomial = {}
        for coordinate in range(dimension):
            result = add(
                result,
                multiply(gradient_output[coordinate], differentiate(poly, coordinate)),
            )
        return result

    values: list[Fraction] = []
    current = output
    for derivative_order in range(order + 1):
        expectation = wick(current)
        if expectation == 0:
            values.append(Fraction(0))
        else:
            normalization_power_twice = derivative_order + 3
            if normalization_power_twice % 2:
                raise AssertionError("a nonzero half-integral normalization survived parity")
            values.append(
                Fraction(expectation, n ** (normalization_power_twice // 2))
            )
        if derivative_order != order:
            current = unnormalized_operator(current)
    return tuple(values)
