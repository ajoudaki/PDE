"""Exact M-only scalar contraction for the frozen-direction part of D^5 f.

This module deliberately does *not* import the depth-order-five population
compiler.  It starts from the frozen parameter line and performs every local
Wick--Stein contraction symbolically.  The resulting seven-scalar forward
and nine-scalar reverse transitions contain only rational arithmetic,
declared scalar states, and one-dimensional ``M`` atoms.

The contraction covers

    2 V[p^5] + 22 U[Hp,p,p,p] + 14 T[T[p,p],p,p],

and also recovers the complete order-three coefficient.  The remaining
three order-five tree families are intentionally not represented here.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import product as cartesian_product
from math import comb, factorial

from ...order5.compiler.factored_expression import (
    FactoredMomentExpression as Expr,
    atom,
    constant,
    emit_cse,
    product,
    summation,
    symbol,
    walk,
)


MAX_DERIVATIVE = 5
NF = 4  # F_1,...,F_4; F_5 drops out after d/dR of X^[5].
NE = 4  # E_0,...,E_3 in the differentiated reverse jet.


@dataclass(frozen=True, order=True)
class Monomial:
    f: tuple[int, ...]
    e: tuple[int, ...]
    phi: tuple[int, ...]

    @staticmethod
    def one() -> "Monomial":
        return Monomial((0,) * NF, (0,) * NE, (0,) * (MAX_DERIVATIVE + 1))

    def multiply(self, other: "Monomial") -> "Monomial":
        return Monomial(
            tuple(a + b for a, b in zip(self.f, other.f)),
            tuple(a + b for a, b in zip(self.e, other.e)),
            tuple(a + b for a, b in zip(self.phi, other.phi)),
        )


@dataclass(frozen=True)
class Polynomial:
    terms: tuple[tuple[Monomial, Expr], ...]

    @staticmethod
    def from_dict(raw: dict[Monomial, Expr]) -> "Polynomial":
        return Polynomial(tuple(sorted((key, value) for key, value in raw.items() if value)))

    @staticmethod
    def zero() -> "Polynomial":
        return Polynomial(())

    @staticmethod
    def scalar(value: int | Fraction | Expr) -> "Polynomial":
        value = value if isinstance(value, Expr) else constant(value)
        return Polynomial(()) if not value else Polynomial(((Monomial.one(), value),))

    def as_dict(self) -> dict[Monomial, Expr]:
        return dict(self.terms)

    def __bool__(self) -> bool:
        return bool(self.terms)

    def __add__(self, other: "Polynomial") -> "Polynomial":
        raw = self.as_dict()
        for key, value in other.terms:
            raw[key] = raw.get(key, constant(0)) + value
        return Polynomial.from_dict(raw)

    __radd__ = __add__

    def __mul__(self, other: "Polynomial") -> "Polynomial":
        if not self or not other:
            return Polynomial.zero()
        raw: dict[Monomial, Expr] = {}
        for left, cl in self.terms:
            for right, cr in other.terms:
                key = left.multiply(right)
                raw[key] = raw.get(key, constant(0)) + cl * cr
        return Polynomial.from_dict(raw)

    __rmul__ = __mul__

    def scale(self, value: int | Fraction | Expr) -> "Polynomial":
        return self * Polynomial.scalar(value)

    def power(self, exponent: int) -> "Polynomial":
        if exponent < 0:
            raise ValueError("negative polynomial power")
        answer = Polynomial.scalar(1)
        for _ in range(exponent):
            answer = answer * self
        return answer

    def derivative_f(self, order: int) -> "Polynomial":
        if not 1 <= order <= NF:
            raise ValueError(order)
        raw: dict[Monomial, Expr] = {}
        index = order - 1
        for key, coefficient in self.terms:
            count = key.f[index]
            if not count:
                continue
            values = list(key.f)
            values[index] -= 1
            target = Monomial(tuple(values), key.e, key.phi)
            raw[target] = raw.get(target, constant(0)) + count * coefficient
        return Polynomial.from_dict(raw)

    def derivative_e(self, order: int) -> "Polynomial":
        if not 0 <= order < NE:
            raise ValueError(order)
        raw: dict[Monomial, Expr] = {}
        for key, coefficient in self.terms:
            count = key.e[order]
            if not count:
                continue
            values = list(key.e)
            values[order] -= 1
            target = Monomial(key.f, tuple(values), key.phi)
            raw[target] = raw.get(target, constant(0)) + count * coefficient
        return Polynomial.from_dict(raw)

    def derivative_z(self) -> "Polynomial":
        raw: dict[Monomial, Expr] = {}
        for key, coefficient in self.terms:
            for derivative in range(MAX_DERIVATIVE):
                count = key.phi[derivative]
                if not count:
                    continue
                values = list(key.phi)
                values[derivative] -= 1
                values[derivative + 1] += 1
                target = Monomial(key.f, key.e, tuple(values))
                raw[target] = raw.get(target, constant(0)) + count * coefficient
        return Polynomial.from_dict(raw)


def scalar(value: int | Fraction | Expr) -> Polynomial:
    return Polynomial.scalar(value)


def fvar(order: int) -> Polynomial:
    key = Monomial.one()
    values = list(key.f)
    values[order - 1] = 1
    return Polynomial(((Monomial(tuple(values), key.e, key.phi), constant(1)),))


def evar(order: int) -> Polynomial:
    key = Monomial.one()
    values = list(key.e)
    values[order] = 1
    return Polynomial(((Monomial(key.f, tuple(values), key.phi), constant(1)),))


def phivar(order: int) -> Polynomial:
    if not 0 <= order <= MAX_DERIVATIVE:
        raise ValueError(order)
    key = Monomial.one()
    values = list(key.phi)
    values[order] = 1
    return Polynomial(((Monomial(key.f, key.e, tuple(values)), constant(1)),))


def _partitions_of_weight(weight: int) -> tuple[tuple[int, ...], ...]:
    """Return (k_1,...,k_weight) with sum j*k_j=weight."""

    if weight == 0:
        return ((),)
    answers: list[tuple[int, ...]] = []

    def visit(j: int, remaining: int, values: list[int]) -> None:
        if j > weight:
            if remaining == 0:
                answers.append(tuple(values))
            return
        for count in range(remaining // j + 1):
            values.append(count)
            visit(j + 1, remaining - j * count, values)
            values.pop()

    visit(1, weight, [])
    return tuple(answers)


def composition_derivative(
    z: list[Polynomial], degree: int, *, derivative_shift: int = 0
) -> Polynomial:
    """Ordinary derivative d^degree/dt^degree phi^(shift)(z(t)) at t=0."""

    if degree == 0:
        return phivar(derivative_shift)
    answer = Polynomial.zero()
    for counts in _partitions_of_weight(degree):
        number = sum(counts)
        coefficient = Fraction(factorial(degree), 1)
        term = phivar(derivative_shift + number)
        for j, count in enumerate(counts, 1):
            coefficient /= factorial(count) * factorial(j) ** count
            if count:
                term = term * z[j].power(count)
        answer = answer + term.scale(coefficient)
    return answer


def gaussian_moment(power: int) -> int:
    if power & 1:
        return 0
    answer = 1
    for value in range(1, power, 2):
        answer *= value
    return answer


class WickStein:
    """Local exact eliminator for independent F- and E-Gaussian blocks."""

    def __init__(
        self,
        f_covariance: dict[tuple[int, int], Expr],
        f_z_covariance: dict[int, Expr],
        e_covariance: dict[tuple[int, int], Expr],
    ) -> None:
        self.f_covariance = {
            (min(i, j), max(i, j)): value
            for (i, j), value in f_covariance.items()
            if value
        }
        self.f_z_covariance = {i: value for i, value in f_z_covariance.items() if value}
        self.e_covariance = {
            (min(i, j), max(i, j)): value
            for (i, j), value in e_covariance.items()
            if value
        }

    @lru_cache(None)
    def e_wick(self, exponents: tuple[int, ...]) -> Expr:
        if not any(exponents):
            return constant(1)
        if sum(exponents) & 1:
            return constant(0)
        i = next(index for index, count in enumerate(exponents) if count)
        remainder = list(exponents)
        remainder[i] -= 1
        terms: list[Expr] = []
        for j, count in enumerate(remainder):
            if not count:
                continue
            covariance = self.e_covariance.get((min(i, j), max(i, j)), constant(0))
            if not covariance:
                continue
            paired = list(remainder)
            paired[j] -= 1
            terms.append(count * covariance * self.e_wick(tuple(paired)))
        return summation(tuple(terms))

    @lru_cache(None)
    def f_stein(self, exponents: tuple[int, ...], phi: tuple[int, ...]) -> Expr:
        if not any(exponents):
            return atom("M", phi) if any(phi) else constant(1)
        i0 = next(index for index, count in enumerate(exponents) if count)
        i = i0 + 1
        remainder = list(exponents)
        remainder[i0] -= 1
        terms: list[Expr] = []
        for j0, count in enumerate(remainder):
            if not count:
                continue
            j = j0 + 1
            covariance = self.f_covariance.get((min(i, j), max(i, j)), constant(0))
            if not covariance:
                continue
            paired = list(remainder)
            paired[j0] -= 1
            terms.append(count * covariance * self.f_stein(tuple(paired), phi))
        covariance0 = self.f_z_covariance.get(i, constant(0))
        if covariance0:
            for derivative, count in enumerate(phi[:-1]):
                if not count:
                    continue
                shifted = list(phi)
                shifted[derivative] -= 1
                shifted[derivative + 1] += 1
                terms.append(
                    count
                    * covariance0
                    * self.f_stein(tuple(remainder), tuple(shifted))
                )
        return summation(tuple(terms))

    def expect(self, polynomial: Polynomial) -> Expr:
        return summation(
            coefficient * self.e_wick(key.e) * self.f_stein(key.f, key.phi)
            for key, coefficient in polynomial.terms
        )


FORWARD_NAMES = ("P", "V", "Q", "W", "S", "J3", "J5")
BACKWARD_NAMES = ("B00", "B02", "B11", "B13", "B22", "K10", "K21", "K30", "K32")


def _forward_coordinate_polynomials() -> tuple[list[Polynomial], list[Polynomial], WickStein]:
    p, v, q, w, s, j3, j5 = (symbol(name) for name in FORWARD_NAMES)
    a = symbol("TAU")
    b = symbol("BASE_B")
    c = j3 + 3 * p
    e = j5 + 5 * q
    z = [scalar(0) for _ in range(6)]
    z[1] = fvar(1) + (phivar(1) * evar(0)).scale(a)
    z[2] = fvar(2)
    z[3] = fvar(3) + (phivar(1) * evar(0)).scale(c)
    z[4] = fvar(4)
    z[5] = (phivar(1) * evar(0)).scale(e)
    x = [composition_derivative(z, degree) for degree in range(6)]
    peeler = WickStein(
        {(1, 1): v, (1, 3): w, (2, 2): s},
        {2: p, 4: q},
        {(0, 0): b},
    )
    return z, x, peeler


def forward_transition() -> dict[str, Expr]:
    _, x, peeler = _forward_coordinate_polynomials()
    return {
        "P_NEXT": peeler.expect(x[0] * x[2]),
        "V_NEXT": peeler.expect(x[1] * x[1]),
        "Q_NEXT": peeler.expect(x[0] * x[4]),
        "W_NEXT": peeler.expect(x[1] * x[3]),
        "S_NEXT": peeler.expect(x[2] * x[2]),
        "J3_NEXT": peeler.expect(x[3].derivative_e(0)),
        "J5_NEXT": peeler.expect(x[5].derivative_e(0)),
    }


def forward_initialization() -> dict[str, Expr]:
    b = symbol("BASE_B1")
    return {
        "P_1": b * atom("M", (1, 2, 1, 0, 0, 0)),
        "V_1": b * atom("M", (0, 4, 0, 0, 0, 0)),
        "Q_1": 3 * b * b * atom("M", (1, 4, 0, 0, 1, 0)),
        "W_1": 3 * b * b * atom("M", (0, 5, 0, 1, 0, 0)),
        "S_1": 3 * b * b * atom("M", (0, 4, 2, 0, 0, 0)),
        "J3_1": 3 * b * atom("M", (0, 3, 0, 1, 0, 0)),
        "J5_1": 15 * b * b * atom("M", (0, 5, 0, 0, 0, 1)),
    }


def _backward_polynomials_and_peeler() -> tuple[list[Polynomial], list[Polynomial], WickStein]:
    p, v, q, w, s, j3, j5 = (symbol(name) for name in FORWARD_NAMES)
    b00, b02, b11, b13, b22, k10, k21, k30, k32 = (
        symbol(name) for name in BACKWARD_NAMES
    )
    tau = symbol("TAU")
    c = j3 + 3 * p
    e = j5 + 5 * q
    z = [scalar(0) for _ in range(6)]
    z[1] = fvar(1) + (phivar(1) * evar(0)).scale(tau)
    z[2] = fvar(2)
    z[3] = fvar(3) + (phivar(1) * evar(0)).scale(c)
    z[4] = fvar(4)
    z[5] = (phivar(1) * evar(0)).scale(e)
    x = [composition_derivative(z, degree) for degree in range(6)]
    carrier = [Polynomial.zero() for _ in range(4)]
    carrier[0] = evar(0)
    carrier[1] = evar(1) + x[0].scale(k10)
    carrier[2] = evar(2) + x[1].scale(k21)
    carrier[3] = evar(3) + x[0].scale(k30) + x[2].scale(k32)
    activation_prime = [
        composition_derivative(z, degree, derivative_shift=1)
        for degree in range(4)
    ]
    source: list[Polynomial] = []
    for degree in range(4):
        value = Polynomial.zero()
        for left in range(degree + 1):
            value = value + (activation_prime[left] * carrier[degree - left]).scale(
                comb(degree, left)
            )
        source.append(value)
    peeler = WickStein(
        {(1, 1): v, (1, 3): w, (2, 2): s},
        {2: p, 4: q},
        {
            (0, 0): b00,
            (0, 2): b02,
            (1, 1): b11,
            (1, 3): b13,
            (2, 2): b22,
            # E_3^2 is never used by the retained transition.
        },
    )
    return source, x, peeler


def backward_transition() -> dict[str, Expr]:
    source, _, peeler = _backward_polynomials_and_peeler()
    b00 = peeler.expect(source[0] * source[0])
    b02 = peeler.expect(source[0] * source[2])
    b11 = peeler.expect(source[1] * source[1])
    b13 = peeler.expect(source[1] * source[3])
    b22 = peeler.expect(source[2] * source[2])
    rho10 = peeler.expect(source[1].derivative_z())
    rho21 = peeler.expect(source[2].derivative_f(1))
    rho30 = peeler.expect(source[3].derivative_z())
    rho32 = peeler.expect(source[3].derivative_f(2))
    return {
        "B00_NEXT": b00,
        "B02_NEXT": b02,
        "B11_NEXT": b11,
        "B13_NEXT": b13,
        "B22_NEXT": b22,
        "K10_NEXT": b00 + rho10,
        "K21_NEXT": rho21,
        "K30_NEXT": 3 * b02 + rho30,
        "K32_NEXT": rho32,
    }


def top_backward_initialization() -> dict[str, Expr]:
    """Apply the same local contraction to R_0=a,R_1=X_0,R_2=R_3=0."""

    generic = backward_transition()
    substitutions = {
        "B00": constant(1),
        "B02": constant(0),
        "B11": constant(0),
        "B13": constant(0),
        "B22": constant(0),
        "K10": constant(1),
        "K21": constant(0),
        "K30": constant(0),
        "K32": constant(0),
    }
    return {
        name.replace("_NEXT", "_H"): substitute_symbols(value, substitutions)
        for name, value in generic.items()
    }


def substitute_symbols(root: Expr, replacements: dict[str, Expr]) -> Expr:
    memo: dict[Expr, Expr] = {}

    def visit(node: Expr) -> Expr:
        if node in memo:
            return memo[node]
        kind = node.node[0]
        if kind == "const" or kind == "atom":
            answer = node
        elif kind == "symbol":
            answer = replacements.get(node.node[1], node)
        elif kind == "add":
            answer = summation(visit(child) for child in node.node[1])
        elif kind == "mul":
            answer = product(visit(child) for child in node.node[1])
        else:
            raise ValueError(kind)
        memo[node] = answer
        return answer

    return visit(root)


def terminal_contractions() -> dict[str, Expr]:
    """Per-layer summands and terminal frozen-family contractions."""

    p, v, _, w, s, j3, j5 = (symbol(name) for name in FORWARD_NAMES)
    b00, b02, b11, b13, b22, *_ = (symbol(name) for name in BACKWARD_NAMES)
    return {
        "STRAIGHT3": j3 + 3 * p,
        "STRAIGHT5": j5 + 5 * symbol("Q"),
        "GRAM11_LAYER": b00 * v + b11,
        "GRAM31_LAYER": b00 * w + 3 * b02 * v + 3 * b11 * p + b13,
        "GRAM22_LAYER": b00 * s + 2 * b02 * p + 4 * b11 * v + b22,
    }


def expr_power(base: Expr, exponent: int) -> Expr:
    answer = constant(1)
    for _ in range(exponent):
        answer = answer * base
    return answer


def tau(depth: int) -> Expr:
    d = atom("M", (0, 2, 0, 0, 0, 0))
    return summation(expr_power(d, exponent) for exponent in range(depth + 1))


@dataclass(frozen=True)
class FrozenRecurrenceResult:
    depth: int
    forward: tuple[dict[str, Expr], ...]
    backward: tuple[dict[str, Expr], ...]
    A: Expr
    B: Expr
    partial_C: Expr
    straight3: Expr
    straight5: Expr
    gram11: Expr
    gram31: Expr
    gram22: Expr


def _rename_roots(roots: dict[str, Expr], suffix: str) -> dict[str, Expr]:
    return {name.replace("_NEXT", suffix): value for name, value in roots.items()}


def assemble_frozen_recurrence(depth: int) -> FrozenRecurrenceResult:
    """Assemble the literal recurrence for a fixed depth.

    ``partial_C`` contains exactly the first three of the six universal
    fifth-derivative tree families.  It must never be presented as ``C``.
    """

    if depth < 1:
        raise ValueError("depth must be positive")
    d = atom("M", (0, 2, 0, 0, 0, 0))

    forward: list[dict[str, Expr]] = [{} for _ in range(depth + 1)]
    forward[1] = {
        name.rsplit("_", 1)[0]: value
        for name, value in forward_initialization().items()
    }
    forward[1] = {
        name: substitute_symbols(value, {"BASE_B1": expr_power(d, depth - 1)})
        for name, value in forward[1].items()
    }
    transition = forward_transition()
    for layer in range(2, depth + 1):
        replacements = {
            **{name: forward[layer - 1][name] for name in FORWARD_NAMES},
            "TAU": tau(layer - 1),
            "BASE_B": expr_power(d, depth - layer),
        }
        forward[layer] = {
            name.replace("_NEXT", ""): substitute_symbols(value, replacements)
            for name, value in transition.items()
        }

    backward: list[dict[str, Expr]] = [{} for _ in range(depth + 1)]
    top_replacements = {
        **(
            {name: forward[depth - 1][name] for name in FORWARD_NAMES}
            if depth >= 2
            else {name: constant(0) for name in FORWARD_NAMES}
        ),
        "TAU": tau(depth - 1),
    }
    top = top_backward_initialization()
    backward[depth] = {
        name.replace("_H", ""): substitute_symbols(value, top_replacements)
        for name, value in top.items()
    }
    reverse_transition = backward_transition()
    for layer in range(depth - 1, 0, -1):
        previous_forward = (
            forward[layer - 1]
            if layer >= 2
            else {name: constant(0) for name in FORWARD_NAMES}
        )
        replacements = {
            **{name: previous_forward[name] for name in FORWARD_NAMES},
            **{name: backward[layer + 1][name] for name in BACKWARD_NAMES},
            "TAU": tau(layer - 1),
        }
        backward[layer] = {
            name.replace("_NEXT", ""): substitute_symbols(value, replacements)
            for name, value in reverse_transition.items()
        }

    straight3 = forward[depth]["J3"] + 3 * forward[depth]["P"]
    straight5 = forward[depth]["J5"] + 5 * forward[depth]["Q"]
    gram11 = forward[depth]["V"] + backward[1]["B11"]
    gram31 = forward[depth]["W"] + backward[1]["B13"]
    gram22 = forward[depth]["S"] + backward[1]["B22"]
    for layer in range(2, depth + 1):
        x = forward[layer - 1]
        y = backward[layer]
        gram11 = gram11 + y["B00"] * x["V"] + y["B11"]
        gram31 = (
            gram31
            + y["B00"] * x["W"]
            + 3 * y["B02"] * x["V"]
            + 3 * y["B11"] * x["P"]
            + y["B13"]
        )
        gram22 = (
            gram22
            + y["B00"] * x["S"]
            + 2 * y["B02"] * x["P"]
            + 4 * y["B11"] * x["V"]
            + y["B22"]
        )
    coefficient_b = 2 * straight3 + 4 * gram11
    partial_c = 2 * straight5 + 22 * gram31 + 14 * gram22
    return FrozenRecurrenceResult(
        depth,
        tuple(forward),
        tuple(backward),
        tau(depth),
        coefficient_b,
        partial_c,
        straight3,
        straight5,
        gram11,
        gram31,
        gram22,
    )


def derivative_ceiling(roots: dict[str, Expr]) -> int:
    maximum = 0
    for root in roots.values():
        for node in walk(root):
            if node.node[0] != "atom":
                continue
            for derivative, count in enumerate(node.node[2]):
                if count:
                    maximum = max(maximum, derivative)
    return maximum


def emitted_sections() -> dict[str, str]:
    sections = {
        "FORWARD_INITIALIZATION": emit_cse(forward_initialization()),
        "FORWARD_TRANSITION": emit_cse(forward_transition()),
        "BACKWARD_TOP": emit_cse(top_backward_initialization()),
        "BACKWARD_TRANSITION": emit_cse(backward_transition()),
        "TERMINAL_CONTRACTIONS": emit_cse(terminal_contractions()),
    }
    return sections


if __name__ == "__main__":
    for title, body in emitted_sections().items():
        print(f"## {title}\n{body}\n")
