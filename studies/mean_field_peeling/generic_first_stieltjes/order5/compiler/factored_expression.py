"""Hash-consed deterministic expression DAG for the order-five compiler.

The population jet distributes only in coordinate variables.  Deterministic
moment arithmetic remains canonically factored, which prevents the large
``H_{44}`` and ``B_{33}`` covariance polynomials from being re-expanded at
every later contraction.  The emitted DAG contains only rational arithmetic
and literal one-dimensional activation moments.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from typing import Iterable

from . import population_jet as expanded


Exponent = tuple[int, ...]


_SERIAL = 0


def _next_serial() -> int:
    global _SERIAL
    _SERIAL += 1
    return _SERIAL


@dataclass(frozen=True, eq=False)
class FactoredMomentExpression:
    node: tuple
    # Constructors below are hash-consed, so object identity is structural
    # identity within one compilation.  An O(1) hash is crucial: recursively
    # hashing a deeply shared expression DAG destroys the benefit of sharing.
    serial: int = field(default_factory=_next_serial)

    def __hash__(self) -> int:
        return self.serial

    @staticmethod
    def zero() -> "FactoredMomentExpression":
        return constant(0)

    @staticmethod
    def constant(value: int | Fraction) -> "FactoredMomentExpression":
        return constant(value)

    @staticmethod
    def atom(layer: str, exponent: Exponent) -> "FactoredMomentExpression":
        if not any(exponent):
            return constant(1)
        return atom(layer, exponent)

    @staticmethod
    def symbol(name: str) -> "FactoredMomentExpression":
        return symbol(name)

    @property
    def terms(self) -> tuple:
        """A diagnostic-only view used for progress counts by the jet code."""

        return self.node[1] if self.node[0] == "add" else (() if self.is_zero() else (self,))

    def is_zero(self) -> bool:
        return self.node == ("const", Fraction(0))

    def is_one(self) -> bool:
        return self.node == ("const", Fraction(1))

    def __bool__(self) -> bool:
        return not self.is_zero()

    def __neg__(self) -> "FactoredMomentExpression":
        return product((constant(-1), self))

    def __add__(self, other) -> "FactoredMomentExpression":
        return summation((self, factored(other)))

    __radd__ = __add__

    def __sub__(self, other) -> "FactoredMomentExpression":
        return self + (-factored(other))

    def __rsub__(self, other) -> "FactoredMomentExpression":
        return factored(other) - self

    def __mul__(self, other) -> "FactoredMomentExpression":
        return product((self, factored(other)))

    __rmul__ = __mul__

    def pow(self, exponent: int) -> "FactoredMomentExpression":
        if exponent < 0:
            raise ValueError("negative polynomial power")
        answer = constant(1)
        base = self
        power = exponent
        while power:
            if power & 1:
                answer = answer * base
            power >>= 1
            if power:
                base = base * base
        return answer

    def collapse_unit_layers(self) -> "FactoredMomentExpression":
        @lru_cache(None)
        def visit(expression: FactoredMomentExpression) -> FactoredMomentExpression:
            kind = expression.node[0]
            if kind in {"const", "symbol"}:
                return expression
            if kind == "atom":
                return atom("M", expression.node[2])
            children = expression.node[1]
            return summation(tuple(visit(child) for child in children)) if kind == "add" else product(tuple(visit(child) for child in children))

        return visit(self)

    def specialize_unit_gram(self) -> "FactoredMomentExpression":
        """Collapse layers and impose ``E[phi(G)^2]=1`` exactly."""

        base_variance = (2,) + (0,) * expanded.MAX_DERIV

        @lru_cache(None)
        def visit(expression: FactoredMomentExpression) -> FactoredMomentExpression:
            kind = expression.node[0]
            if kind == "const":
                return expression
            if kind == "symbol":
                return constant(1) if expression.node[1] == "Q0" else expression
            if kind == "atom":
                exponent = expression.node[2]
                return constant(1) if exponent == base_variance else atom("M", exponent)
            children = tuple(visit(child) for child in expression.node[1])
            return summation(children) if kind == "add" else product(children)

        return visit(self)

    def maximum_derivative(self) -> int:
        answer = 0
        for expression in walk(self):
            if expression.node[0] == "atom":
                for derivative, count in enumerate(expression.node[2]):
                    if count:
                        answer = max(answer, derivative)
        return answer


def _sort_key(expression: FactoredMomentExpression) -> int:
    return expression.serial


@lru_cache(None)
def constant(value: int | Fraction) -> FactoredMomentExpression:
    return FactoredMomentExpression(("const", Fraction(value)))


@lru_cache(None)
def atom(layer: str, exponent: Exponent) -> FactoredMomentExpression:
    return FactoredMomentExpression(("atom", layer, tuple(exponent)))


@lru_cache(None)
def symbol(name: str) -> FactoredMomentExpression:
    return FactoredMomentExpression(("symbol", name))


def factored(value) -> FactoredMomentExpression:
    return value if isinstance(value, FactoredMomentExpression) else constant(value)


@lru_cache(None)
def _product_cached(factors: tuple[FactoredMomentExpression, ...]) -> FactoredMomentExpression:
    return FactoredMomentExpression(("mul", factors))


def product(raw_factors: Iterable[FactoredMomentExpression]) -> FactoredMomentExpression:
    rational = Fraction(1)
    factors: list[FactoredMomentExpression] = []
    for raw in raw_factors:
        factor = factored(raw)
        if factor.node[0] == "const":
            rational *= factor.node[1]
        elif factor.node[0] == "mul":
            for child in factor.node[1]:
                if child.node[0] == "const":
                    rational *= child.node[1]
                else:
                    factors.append(child)
        else:
            factors.append(factor)
    if not rational:
        return constant(0)
    if rational != 1:
        factors.append(constant(rational))
    if not factors:
        return constant(1)
    factors.sort(key=_sort_key)
    return factors[0] if len(factors) == 1 else _product_cached(tuple(factors))


def _coefficient_and_core(expression: FactoredMomentExpression) -> tuple[Fraction, FactoredMomentExpression]:
    if expression.node[0] == "const":
        return expression.node[1], constant(1)
    if expression.node[0] != "mul":
        return Fraction(1), expression
    coefficient = Fraction(1)
    remaining: list[FactoredMomentExpression] = []
    for factor in expression.node[1]:
        if factor.node[0] == "const":
            coefficient *= factor.node[1]
        else:
            remaining.append(factor)
    core = product(tuple(remaining))
    return coefficient, core


@lru_cache(None)
def _summation_cached(terms: tuple[FactoredMomentExpression, ...]) -> FactoredMomentExpression:
    return FactoredMomentExpression(("add", terms))


def summation(raw_terms: Iterable[FactoredMomentExpression]) -> FactoredMomentExpression:
    coefficients: dict[FactoredMomentExpression, Fraction] = {}
    for raw in raw_terms:
        term = factored(raw)
        children = term.node[1] if term.node[0] == "add" else (term,)
        for child in children:
            coefficient, core = _coefficient_and_core(child)
            coefficients[core] = coefficients.get(core, Fraction(0)) + coefficient
    terms: list[FactoredMomentExpression] = []
    for core, coefficient in coefficients.items():
        if not coefficient:
            continue
        if core.is_one():
            terms.append(constant(coefficient))
        else:
            terms.append(product((constant(coefficient), core)))
    if not terms:
        return constant(0)
    terms.sort(key=_sort_key)
    return terms[0] if len(terms) == 1 else _summation_cached(tuple(terms))


def walk(root: FactoredMomentExpression) -> tuple[FactoredMomentExpression, ...]:
    seen: set[FactoredMomentExpression] = set()
    ordered: list[FactoredMomentExpression] = []

    def visit(expression: FactoredMomentExpression) -> None:
        if expression in seen:
            return
        seen.add(expression)
        if expression.node[0] in {"add", "mul"}:
            for child in expression.node[1]:
                visit(child)
        ordered.append(expression)

    visit(root)
    return tuple(ordered)


def compile_factored(
    order: int = 5,
    *,
    verbose: bool = False,
    arbitrary_q0: bool = False,
):
    """Run the common jet/peel logic with factored deterministic arithmetic."""

    old_type = expanded.MomentPolynomial
    old_mp = expanded.mp
    expanded.MomentPolynomial = FactoredMomentExpression
    expanded.mp = factored
    try:
        q0 = symbol("Q0") if arbitrary_q0 else constant(1)
        return expanded.compile_population_jet(order, verbose=verbose, q0=q0)
    finally:
        expanded.MomentPolynomial = old_type
        expanded.mp = old_mp


def evaluate_polynomial_activation(
    expression: FactoredMomentExpression,
    coefficients: Iterable[int | Fraction],
    *,
    q0: int | Fraction = 1,
) -> Fraction:
    coefficients = tuple(Fraction(value) for value in coefficients)
    q0 = Fraction(q0)
    x20 = [0] * (expanded.MAX_DERIV + 1)
    x20[0] = 2
    q1 = expanded.activation_product_moment(tuple(x20), coefficients, q0)
    memo: dict[FactoredMomentExpression, Fraction] = {}

    def visit(node: FactoredMomentExpression) -> Fraction:
        if node in memo:
            return memo[node]
        kind = node.node[0]
        if kind == "const":
            value = node.node[1]
        elif kind == "symbol":
            if node.node[1] != "Q0":
                raise KeyError(node.node[1])
            value = q0
        elif kind == "atom":
            layer, exponent = node.node[1], node.node[2]
            variance = q0 if layer in {"X", "M"} else q1
            value = expanded.activation_product_moment(exponent, coefficients, variance)
        elif kind == "add":
            value = sum((visit(child) for child in node.node[1]), Fraction(0))
        elif kind == "mul":
            value = Fraction(1)
            for child in node.node[1]:
                value *= visit(child)
        else:
            raise ValueError(kind)
        memo[node] = value
        return value

    return visit(expression)


def format_atom(expression: FactoredMomentExpression) -> str:
    _, layer, exponent = expression.node
    return f"{layer}_{{{''.join(str(value) for value in exponent[:6])}}}"


def emit_cse(
    roots: dict[str, FactoredMomentExpression],
) -> str:
    """Emit a complete dependency-first arithmetic DAG with named roots."""

    all_nodes: list[FactoredMomentExpression] = []
    seen: set[FactoredMomentExpression] = set()
    for root in roots.values():
        for node in walk(root):
            if node not in seen:
                seen.add(node)
                all_nodes.append(node)
    compound = [node for node in all_nodes if node.node[0] in {"add", "mul"}]
    names = {node: f"t_{index:05d}" for index, node in enumerate(compound)}

    def render(node: FactoredMomentExpression) -> str:
        kind = node.node[0]
        if kind == "const":
            return str(node.node[1])
        if kind == "symbol":
            return node.node[1]
        if kind == "atom":
            return format_atom(node)
        return names[node]

    lines: list[str] = []
    for node in compound:
        operator = " + " if node.node[0] == "add" else " * "
        lines.append(f"{names[node]} = {operator.join(render(child) for child in node.node[1])}")
    for name, root in roots.items():
        lines.append(f"{name} = {render(root)}")
    return "\n".join(lines)
