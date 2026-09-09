#!/usr/bin/env python3
"""Exact order-five width-first Euler DAG for a quadratic activation.

The activation is ``psi(x) = a*x + b*x*x``.  All calculations are in
Q[a,b,h]/(h**6).  The Gaussian source variables are retained as sparse
polynomials and all expectations are evaluated by Wick recurrence with the
chronologically constructed OMFP covariance matrices.

This is deliberately independent of the continuous-gradient-flow graph
compiler in ``quadratic_compiler``: it computes the discrete Euler horizons
N=0,...,5 needed for the Newton coefficients of an arbitrary horizon.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import comb
from typing import Dict, Iterable, Tuple


Q = Fraction
MAX_H = 5
RingMonomial = Tuple[int, int, int]  # (power of h, power of a, power of b)
GaussianMonomial = Tuple[int, ...]


@dataclass(frozen=True)
class Ring:
    """A sparse element of Q[h,a,b]/(h**6)."""

    terms: Tuple[Tuple[RingMonomial, Fraction], ...] = ()

    @staticmethod
    def from_dict(raw: Dict[RingMonomial, Fraction]) -> "Ring":
        return Ring(tuple(sorted((m, Q(c)) for m, c in raw.items() if c)))

    @staticmethod
    def scalar(value: int | Fraction) -> "Ring":
        value = Q(value)
        return Ring.from_dict({(0, 0, 0): value}) if value else ZERO

    @staticmethod
    def monomial(h: int = 0, a: int = 0, b: int = 0,
                 coefficient: int | Fraction = 1) -> "Ring":
        if h > MAX_H:
            return ZERO
        return Ring.from_dict({(h, a, b): Q(coefficient)})

    def as_dict(self) -> Dict[RingMonomial, Fraction]:
        return dict(self.terms)

    def __bool__(self) -> bool:
        return bool(self.terms)

    def __neg__(self) -> "Ring":
        return Ring(tuple((m, -c) for m, c in self.terms))

    def __add__(self, other: "Ring") -> "Ring":
        out = self.as_dict()
        for monomial, coefficient in other.terms:
            out[monomial] = out.get(monomial, Q(0)) + coefficient
        return Ring.from_dict(out)

    def __sub__(self, other: "Ring") -> "Ring":
        return self + (-other)

    def __mul__(self, other: "Ring") -> "Ring":
        if not self or not other:
            return ZERO
        out: Dict[RingMonomial, Fraction] = {}
        for (h1, a1, b1), c1 in self.terms:
            for (h2, a2, b2), c2 in other.terms:
                h = h1 + h2
                if h > MAX_H:
                    continue
                key = (h, a1 + a2, b1 + b2)
                out[key] = out.get(key, Q(0)) + c1 * c2
        return Ring.from_dict(out)

    def scale(self, value: int | Fraction) -> "Ring":
        value = Q(value)
        if not value:
            return ZERO
        return Ring(tuple((m, value * c) for m, c in self.terms))

    def h_coefficient(self, degree: int) -> Dict[Tuple[int, int], Fraction]:
        out: Dict[Tuple[int, int], Fraction] = {}
        for (h, a, b), coefficient in self.terms:
            if h == degree:
                out[(a, b)] = out.get((a, b), Q(0)) + coefficient
        return {m: c for m, c in out.items() if c}


ZERO = Ring(())
ONE = Ring.from_dict({(0, 0, 0): Q(1)})
H = Ring.from_dict({(1, 0, 0): Q(1)})
AA = Ring.from_dict({(0, 1, 0): Q(1)})
BB = Ring.from_dict({(0, 0, 1): Q(1)})


@dataclass
class GPoly:
    """Sparse polynomial in one chronological Gaussian source block."""

    dimension: int
    terms: Dict[GaussianMonomial, Ring]

    @staticmethod
    def zero(dimension: int) -> "GPoly":
        return GPoly(dimension, {})

    @staticmethod
    def constant(dimension: int, coefficient: Ring = ONE) -> "GPoly":
        return GPoly(dimension, {(0,) * dimension: coefficient}) if coefficient else GPoly.zero(dimension)

    @staticmethod
    def variable(dimension: int, index: int) -> "GPoly":
        powers = [0] * dimension
        powers[index] = 1
        return GPoly(dimension, {tuple(powers): ONE})

    def add(self, other: "GPoly") -> "GPoly":
        assert self.dimension == other.dimension
        out = self.terms.copy()
        for monomial, coefficient in other.terms.items():
            out[monomial] = out.get(monomial, ZERO) + coefficient
            if not out[monomial]:
                del out[monomial]
        return GPoly(self.dimension, out)

    def scale(self, coefficient: Ring) -> "GPoly":
        if not coefficient:
            return GPoly.zero(self.dimension)
        return GPoly(
            self.dimension,
            {m: c * coefficient for m, c in self.terms.items() if c * coefficient},
        )

    def mul(self, other: "GPoly") -> "GPoly":
        assert self.dimension == other.dimension
        out: Dict[GaussianMonomial, Ring] = {}
        for left, c_left in self.terms.items():
            for right, c_right in other.terms.items():
                coefficient = c_left * c_right
                if not coefficient:
                    continue
                monomial = tuple(x + y for x, y in zip(left, right))
                out[monomial] = out.get(monomial, ZERO) + coefficient
                if not out[monomial]:
                    del out[monomial]
        return GPoly(self.dimension, out)

    def derivative(self, index: int) -> "GPoly":
        out: Dict[GaussianMonomial, Ring] = {}
        for monomial, coefficient in self.terms.items():
            power = monomial[index]
            if not power:
                continue
            child = list(monomial)
            child[index] -= 1
            key = tuple(child)
            out[key] = out.get(key, ZERO) + coefficient.scale(power)
        return GPoly(self.dimension, out)


class GaussianExpectation:
    """Wick expectation over a centered Gaussian with Ring covariances."""

    def __init__(self, dimension: int) -> None:
        self.dimension = dimension
        self.covariance = [[ZERO for _ in range(dimension)] for _ in range(dimension)]
        self.covariance[0][0] = ONE
        self._cache: Dict[GaussianMonomial, Ring] = {(0,) * dimension: ONE}

    def set_covariance(self, left: int, right: int, value: Ring) -> None:
        current = self.covariance[left][right]
        if current and current != value:
            raise ArithmeticError(f"attempted to change covariance {(left, right)}")
        self.covariance[left][right] = value
        self.covariance[right][left] = value
        self._cache = {(0,) * self.dimension: ONE}

    def moment(self, powers: GaussianMonomial) -> Ring:
        cached = self._cache.get(powers)
        if cached is not None:
            return cached
        if sum(powers) % 2:
            self._cache[powers] = ZERO
            return ZERO
        left = next(i for i, power in enumerate(powers) if power)
        remainder = list(powers)
        remainder[left] -= 1
        answer = ZERO
        for right, multiplicity in enumerate(remainder):
            covariance = self.covariance[left][right]
            if not multiplicity or not covariance:
                continue
            remainder[right] -= 1
            answer = answer + covariance * self.moment(tuple(remainder)).scale(multiplicity)
            remainder[right] += 1
        self._cache[powers] = answer
        return answer

    def expect(self, polynomial: GPoly) -> Ring:
        assert polynomial.dimension == self.dimension
        answer = ZERO
        for monomial, coefficient in polynomial.terms.items():
            answer = answer + coefficient * self.moment(monomial)
        return answer

    def product(self, left: GPoly, right: GPoly) -> Ring:
        return self.expect(left.mul(right))


def activate(value: GPoly) -> GPoly:
    return value.scale(AA).add(value.mul(value).scale(BB))


def activation_derivative(value: GPoly) -> GPoly:
    return GPoly.constant(value.dimension, AA).add(value.scale(BB.scale(2)))


def linear_combination(terms: Iterable[Tuple[Ring, GPoly]], dimension: int) -> GPoly:
    answer = GPoly.zero(dimension)
    for coefficient, polynomial in terms:
        answer = answer.add(polynomial.scale(coefficient))
    return answer


def horizon_output(horizon: int) -> Ring:
    """Return F_horizon(h) modulo h**6, exactly in Q[a,b]."""

    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    dimension = horizon + 2  # base mark plus sources 0,...,horizon
    column = GaussianExpectation(dimension)  # U, chi_0,...
    row = GaussianExpectation(dimension)     # A, xi_0,...
    U = GPoly.variable(dimension, 0)
    Astate = GPoly.variable(dimension, 0)
    X: list[GPoly] = []
    C: list[GPoly] = []
    Y: list[GPoly] = []

    for step in range(horizon + 1):
        X_step = activate(U)
        X.append(X_step)

        # Chronologically add the new forward innovation xi_step.
        for previous in range(step + 1):
            q = column.product(X[previous], X_step)
            row.set_covariance(previous + 1, step + 1, q)

        z_terms: list[Tuple[Ring, GPoly]] = [(ONE, GPoly.variable(dimension, step + 1))]
        for previous in range(step):
            rho = column.expect(X_step.derivative(previous + 1))
            q = column.product(X[previous], X_step)
            z_terms.append((rho + H * q, C[previous]))
        z = linear_combination(z_terms, dimension)
        Y_step = activate(z)
        Y.append(Y_step)

        if step == horizon:
            return row.product(Astate, Y_step)

        C_step = Astate.mul(activation_derivative(z))
        C.append(C_step)

        # Chronologically add the new transpose innovation chi_step.
        for previous in range(step + 1):
            k = row.product(C[previous], C_step)
            column.set_covariance(previous + 1, step + 1, k)

        b_terms: list[Tuple[Ring, GPoly]] = [(ONE, GPoly.variable(dimension, step + 1))]
        for previous in range(step + 1):
            sigma = row.expect(C_step.derivative(previous + 1))
            if previous < step:
                k = row.product(C[previous], C_step)
                sigma = sigma + H * k
            b_terms.append((sigma, X[previous]))
        back = linear_combination(b_terms, dimension)

        U = U.add(activation_derivative(U).mul(back).scale(H))
        Astate = Astate.add(Y_step.scale(H))

    raise AssertionError("unreachable")


def poly_add(left: Dict[Tuple[int, int], Fraction],
             right: Dict[Tuple[int, int], Fraction],
             scale: Fraction = Q(1)) -> Dict[Tuple[int, int], Fraction]:
    out = left.copy()
    for key, value in right.items():
        out[key] = out.get(key, Q(0)) + scale * value
    return {key: value for key, value in out.items() if value}


def newton_coefficients(values: list[Dict[Tuple[int, int], Fraction]]) -> list[Dict[Tuple[int, int], Fraction]]:
    """Forward differences at zero, including Theta_0."""
    row = [value.copy() for value in values]
    answer = [row[0]]
    while len(row) > 1:
        row = [poly_add(row[i + 1], row[i], Q(-1)) for i in range(len(row) - 1)]
        answer.append(row[0])
    return answer


def evaluate_ab(polynomial: Dict[Tuple[int, int], Fraction], a: Fraction, b: Fraction) -> Fraction:
    return sum(c * a**pa * b**pb for (pa, pb), c in polynomial.items())


def format_q(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def format_ab(polynomial: Dict[Tuple[int, int], Fraction]) -> str:
    if not polynomial:
        return "0"
    pieces = []
    for (pa, pb), coefficient in sorted(polynomial.items(), key=lambda item: (sum(item[0]), item[0]), reverse=True):
        factors = []
        if pa:
            factors.append("a" if pa == 1 else f"a^{pa}")
        if pb:
            factors.append("b" if pb == 1 else f"b^{pb}")
        monomial = "*".join(factors) if factors else "1"
        pieces.append(f"({format_q(coefficient)})*{monomial}")
    return " + ".join(pieces).replace("+ (-", "- (")


def univariate_add(left: Dict[int, Fraction], right: Dict[int, Fraction],
                   scale: Fraction = Q(1)) -> Dict[int, Fraction]:
    out = left.copy()
    for power, coefficient in right.items():
        out[power] = out.get(power, Q(0)) + scale * coefficient
    return {power: coefficient for power, coefficient in out.items() if coefficient}


def univariate_mul(left: Dict[int, Fraction], right: Dict[int, Fraction]) -> Dict[int, Fraction]:
    out: Dict[int, Fraction] = {}
    for p, c in left.items():
        for q, d in right.items():
            out[p + q] = out.get(p + q, Q(0)) + c * d
    return {power: coefficient for power, coefficient in out.items() if coefficient}


def one_plus_3x(power: int) -> Dict[int, Fraction]:
    return {k: Q(comb(power, k) * 3**k) for k in range(power + 1)}


def normalized_numerator(polynomial: Dict[Tuple[int, int], Fraction],
                         denominator_power: int) -> Dict[int, Fraction]:
    """Substitute a=1/s, b=e/s, s^2=1+3e^2.

    Returns P(x) such that the result is P(e^2)/(1+3e^2)^denominator_power.
    Every accepted output coefficient has even b power and even total
    activation degree; assertions below make that structural fact auditable.
    """
    answer: Dict[int, Fraction] = {}
    for (pa, pb), coefficient in polynomial.items():
        assert pb % 2 == 0, (pa, pb)
        assert (pa + pb) % 2 == 0, (pa, pb)
        native_denominator = (pa + pb) // 2
        assert native_denominator <= denominator_power
        term = {
            power + pb // 2: coefficient * expansion_coefficient
            for power, expansion_coefficient
            in one_plus_3x(denominator_power - native_denominator).items()
        }
        answer = univariate_add(answer, term)
    return answer


def format_x(polynomial: Dict[int, Fraction]) -> str:
    if not polynomial:
        return "0"
    pieces = []
    for power in sorted(polynomial, reverse=True):
        coefficient = polynomial[power]
        monomial = "1" if power == 0 else ("x" if power == 1 else f"x^{power}")
        pieces.append(f"({format_q(coefficient)})*{monomial}")
    return " + ".join(pieces).replace("+ (-", "- (")


def time_polynomial_from_newton(theta: list[Dict[int, Fraction]], order: int) -> list[Dict[int, Fraction]]:
    """Monomial-in-N coefficients of sum_j binom(N,j) theta[j]."""
    # Exact signed-Stirling expansion of falling factorial by elementary DP.
    result = [{} for _ in range(order + 1)]
    falling: list[Dict[int, Fraction]] = [{0: Q(1)}]
    for j in range(1, order + 1):
        previous = falling[-1]
        current: Dict[int, Fraction] = {}
        for degree, coefficient in previous.items():
            current[degree + 1] = current.get(degree + 1, Q(0)) + coefficient
            current[degree] = current.get(degree, Q(0)) - Q(j - 1) * coefficient
        falling.append({degree: coefficient for degree, coefficient in current.items() if coefficient})
    for j in range(1, order + 1):
        for degree, scalar in falling[j].items():
            result[degree] = univariate_add(result[degree], theta[j], scalar / Q(__import__('math').factorial(j)))
    return result


def main() -> None:
    outputs = [horizon_output(n) for n in range(6)]
    for degree in (1, 2, 3, 4, 5):
        values = [output.h_coefficient(degree) for output in outputs]
        print(f"h^{degree} horizon values")
        for horizon, value in enumerate(values):
            print(horizon, format_ab(value))
        if degree in (3, 5):
            theta = newton_coefficients(values)
            print(f"h^{degree} Newton coefficients")
            for index, value in enumerate(theta):
                print(index, format_ab(value))

            denominator_power = 6 if degree == 3 else 9
            normalized_theta = [normalized_numerator(value, denominator_power) for value in theta]
            print(f"h^{degree} normalized Newton numerators over (1+3x)^{denominator_power}")
            for index, value in enumerate(normalized_theta):
                print(index, format_x(value))
            time_coefficients = time_polynomial_from_newton(normalized_theta, degree)
            print(f"h^{degree} normalized monomial-in-N numerators")
            for index, value in enumerate(time_coefficients):
                print(index, format_x(value))

    # Mandatory exact identity-activation gates.
    c3 = [evaluate_ab(output.h_coefficient(3), Q(1), Q(0)) for output in outputs]
    c5 = [evaluate_ab(output.h_coefficient(5), Q(1), Q(0)) for output in outputs]
    assert c3 == [Q(0), Q(0), Q(24), Q(120), Q(336), Q(720)], c3
    assert c5 == [Q(0), Q(0), Q(20), Q(525), Q(3682), Q(14824)], c5
    theta5 = newton_coefficients([output.h_coefficient(5) for output in outputs])
    assert [evaluate_ab(v, Q(1), Q(0)) for v in theta5] == [0, 0, 20, 465, 1702, 1464]
    print("identity gates: PASS")


if __name__ == "__main__":
    main()
