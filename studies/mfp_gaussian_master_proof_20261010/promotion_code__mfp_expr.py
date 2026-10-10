"""Dependency-free scalar expressions for the finite typed Gaussian calculus.

Build expressions with ``const``, ``symbol``, ``phi`` and ordinary arithmetic.
``phi(x, r)`` denotes the r-th derivative of one fixed smooth activation, whose
every derivative has polynomial growth. This analytic contract is assumed, not
checked by the symbolic kernel. Symbols are identified only by their names:
even Gaussian coordinates equal almost surely remain different formal symbols.

Only constant division and nonnegative integer powers are admitted. Expectation
atoms are allocated by a caller-supplied callback; no quadrature is performed.
Finite float inputs denote the exact decimal rational ``Fraction(str(value))``;
all subsequent symbolic constant arithmetic is exact. Arithmetic already done
in Python before constructing an expression is outside this guarantee.
Software checks do not replace the mathematical hypotheses in the guide.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import isfinite
from typing import Callable, Mapping, Sequence


Number = int | Fraction | float


class UnsupportedExpression(ValueError):
    """The requested expression or reduction lies outside the declared language."""


@dataclass(frozen=True, slots=True)
class Expr:
    """Immutable syntax node; use the factory functions for canonical forms.

    ``op`` is const, symbol, add, mul, pow, or phi. ``value`` stores the
    constant, symbol name, power, or activation derivative order respectively;
    composite arguments are the tuple ``args``.
    """

    op: str
    args: tuple[Expr, ...] = ()
    value: Number | str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.args, tuple) or not all(isinstance(a, Expr) for a in self.args):
            raise UnsupportedExpression("expression arguments must be a tuple of Expr")
        if self.op == "const":
            if self.args:
                raise UnsupportedExpression("constants have no arguments")
            object.__setattr__(self, "value", _number(self.value))
        elif self.op == "symbol":
            if self.args or not isinstance(self.value, str) or not self.value:
                raise UnsupportedExpression("a symbol needs a nonempty string name")
        elif self.op in ("phi", "pow"):
            if len(self.args) != 1 or type(self.value) is not int or self.value < 0:
                raise UnsupportedExpression("phi/pow needs one argument and a nonnegative integer")
        elif self.op in ("add", "mul"):
            if len(self.args) < 2 or self.value is not None:
                raise UnsupportedExpression("add/mul needs at least two arguments and no value")
        else:
            raise UnsupportedExpression(f"unsupported operation: {self.op!r}")

    def __add__(self, other: Expr | Number) -> Expr:
        return _add(self, _coerce(other))

    def __radd__(self, other: Expr | Number) -> Expr:
        return _add(_coerce(other), self)

    def __sub__(self, other: Expr | Number) -> Expr:
        return _add(self, -_coerce(other))

    def __rsub__(self, other: Expr | Number) -> Expr:
        return _add(_coerce(other), -self)

    def __neg__(self) -> Expr:
        return _mul(const(-1), self)

    def __mul__(self, other: Expr | Number) -> Expr:
        return _mul(self, _coerce(other))

    def __rmul__(self, other: Expr | Number) -> Expr:
        return _mul(_coerce(other), self)

    def __truediv__(self, other: Expr | Number) -> Expr:
        denominator = _coerce(other)
        if denominator.op != "const":
            raise UnsupportedExpression("division is allowed only by a numeric constant")
        if denominator.value == 0:
            raise ZeroDivisionError("division by zero")
        return self * const(1 / denominator.value)

    def __rtruediv__(self, other: Expr | Number) -> Expr:
        return _coerce(other).__truediv__(self)

    def __pow__(self, exponent: int) -> Expr:
        return _pow(self, exponent)

    def __str__(self) -> str:
        return render(self)


def _number(value: object) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, float) and isfinite(value):
        return Fraction(str(value))
    raise UnsupportedExpression("constants must be int, Fraction, or finite float")


def const(value: Number) -> Expr:
    """Exact rational constant; finite floats use their decimal ``str`` value."""
    return Expr("const", value=_number(value))


def symbol(name: str) -> Expr:
    return Expr("symbol", value=name)


def _coerce(value: Expr | Number) -> Expr:
    return value if isinstance(value, Expr) else const(value)


def phi(x: Expr | Number, order: int = 0) -> Expr:
    """The formal derivative ``phi^(order)(x)`` of the generic activation."""
    return Expr("phi", (_coerce(x),), order)


@lru_cache(maxsize=32768)
def _key(expression: Expr) -> tuple:
    if expression.op == "const":
        rational = expression.value
        return (0, rational.numerator, rational.denominator)
    if expression.op == "symbol":
        return (1, expression.value)
    rank = {"phi": 2, "pow": 3, "mul": 4, "add": 5}[expression.op]
    return (rank, expression.value or 0, tuple(_key(a) for a in expression.args))


def _coefficient(expression: Expr) -> tuple[Fraction, Expr]:
    if expression.op == "const":
        return expression.value, const(1)
    if expression.op == "mul" and expression.args[0].op == "const":
        return expression.args[0].value, _mul(*expression.args[1:])
    return Fraction(1), expression


def _add(*expressions: Expr) -> Expr:
    terms: dict[Expr, Fraction] = {}
    pending = list(expressions)
    while pending:
        expression = pending.pop()
        if expression.op == "add":
            pending.extend(expression.args)
            continue
        coefficient, body = _coefficient(expression)
        if body.op == "add":
            pending.extend(_mul(const(coefficient), term) for term in body.args)
            continue
        terms[body] = _number(terms.get(body, Fraction(0)) + coefficient)
    result = [_mul(const(c), body) for body, c in terms.items() if c != 0]
    result.sort(key=_key)
    if not result:
        return const(0)
    if len(result) == 1:
        return result[0]
    return Expr("add", tuple(result))


def _mul(*expressions: Expr) -> Expr:
    coefficient: Fraction = Fraction(1)
    powers: dict[Expr, int] = {}
    pending = list(expressions)
    while pending:
        expression = pending.pop()
        if expression.op == "const":
            coefficient = _number(coefficient * expression.value)
            if coefficient == 0:
                return const(0)
        elif expression.op == "mul":
            pending.extend(expression.args)
        elif expression.op == "pow":
            base, exponent = expression.args[0], expression.value
            powers[base] = powers.get(base, 0) + exponent
        else:
            powers[expression] = powers.get(expression, 0) + 1
    result = [_pow(base, exponent) for base, exponent in powers.items()]
    result.sort(key=_key)
    if coefficient != 1 or not result:
        result.insert(0, const(coefficient))
    if len(result) == 1:
        return result[0]
    return Expr("mul", tuple(result))


def _pow(base: Expr, exponent: int) -> Expr:
    if type(exponent) is not int or exponent < 0:
        raise UnsupportedExpression("powers must be nonnegative integers")
    if exponent == 0:
        return const(1)
    if exponent == 1:
        return base
    if base.op == "const":
        return const(base.value**exponent)
    if base.op == "pow":
        return _pow(base.args[0], base.value * exponent)
    if base.op == "mul":
        return _mul(*(_pow(a, exponent) for a in base.args))
    return Expr("pow", (base,), exponent)


@lru_cache(maxsize=32768)
def symbols(expression: Expr) -> frozenset[Expr]:
    """All formal symbols, including those inside nonlinear arguments."""
    expression = _coerce(expression)
    if expression.op == "symbol":
        return frozenset((expression,))
    return frozenset().union(*(symbols(a) for a in expression.args))


@lru_cache(maxsize=32768)
def diff(expression: Expr, variable: Expr) -> Expr:
    """Formal partial derivative, keeping every other symbol fixed."""
    expression = _coerce(expression)
    if not isinstance(variable, Expr) or variable.op != "symbol":
        raise UnsupportedExpression("differentiate with respect to a symbol")
    if variable not in symbols(expression):
        return const(0)
    if expression.op == "symbol":
        return const(1)
    if expression.op == "add":
        return _add(*(diff(a, variable) for a in expression.args))
    if expression.op == "mul":
        terms = []
        for index, argument in enumerate(expression.args):
            derivative = diff(argument, variable)
            if derivative != const(0):
                terms.append(_mul(derivative, *expression.args[:index], *expression.args[index + 1:]))
        return _add(*terms)
    if expression.op == "pow":
        return expression.value * expression.args[0] ** (expression.value - 1) * diff(expression.args[0], variable)
    if expression.op == "phi":
        return phi(expression.args[0], expression.value + 1) * diff(expression.args[0], variable)
    raise UnsupportedExpression(f"cannot differentiate {expression.op!r}")


def substitute(expression: Expr, mapping: Mapping[Expr, Expr | Number]) -> Expr:
    """Simultaneous structural substitution; replacement values are not revisited."""
    replacements = {key: _coerce(value) for key, value in mapping.items()}
    if not all(isinstance(key, Expr) for key in replacements):
        raise UnsupportedExpression("substitution keys must be expressions")

    @lru_cache(maxsize=None)
    def visit(node: Expr) -> Expr:
        if node in replacements:
            return replacements[node]
        if not node.args:
            return node
        args = tuple(visit(a) for a in node.args)
        if node.op == "add":
            return _add(*args)
        if node.op == "mul":
            return _mul(*args)
        if node.op == "pow":
            return _pow(args[0], node.value)
        return phi(args[0], node.value)

    return visit(_coerce(expression))


@lru_cache(maxsize=32768)
def expand(expression: Expr) -> Expr:
    """Distribute finite products and integer powers, including inside phi."""
    expression = _coerce(expression)
    if not expression.args:
        return expression
    args = tuple(expand(a) for a in expression.args)
    if expression.op == "add":
        return _add(*args)
    if expression.op == "phi":
        return phi(args[0], expression.value)

    def distributed_product(factors: Sequence[Expr]) -> Expr:
        terms = [const(1)]
        for factor in factors:
            alternatives = factor.args if factor.op == "add" else (factor,)
            terms = [_mul(term, alternative) for term in terms for alternative in alternatives]
        return _add(*terms)

    if expression.op == "pow":
        return distributed_product((args[0],) * expression.value)
    return distributed_product(args)


def render(expression: Expr) -> str:
    """Deterministic plain-text representation with explicit parentheses."""
    expression = _coerce(expression)
    if expression.op == "const":
        return str(expression.value)
    if expression.op == "symbol":
        return expression.value
    if expression.op == "phi":
        function = "phi" if expression.value == 0 else f"phi^({expression.value})"
        return f"{function}({render(expression.args[0])})"
    if expression.op == "pow":
        return f"({render(expression.args[0])})^{expression.value}"
    separator = " + " if expression.op == "add" else " * "
    return "(" + separator.join(render(a) for a in expression.args) + ")"


def evaluate(
    expression: Expr,
    values: Mapping[Expr, Number],
    activation: Callable[[int, Number], Number],
) -> Number:
    """Evaluate using symbol values and ``activation(order, argument)``."""
    @lru_cache(maxsize=None)
    def visit(node: Expr) -> Number:
        if node.op == "const":
            return node.value
        if node.op == "symbol":
            return values[node]
        if node.op == "add":
            return sum(visit(a) for a in node.args)
        if node.op == "mul":
            result: Number = 1
            for argument in node.args:
                result *= visit(argument)
            return result
        if node.op == "pow":
            return visit(node.args[0]) ** node.value
        return activation(node.value, visit(node.args[0]))

    return visit(_coerce(expression))


def gaussian_expectation(
    expression: Expr,
    gaussian_symbols: Sequence[Expr],
    covariance: Mapping[tuple[Expr, Expr], Expr | Number],
    atom: Callable[[Expr], Expr],
    flat_only: bool = False,
) -> Expr:
    """Reduce an expectation over the named *centered* Gaussian coordinates.

    Covariance entries may contain deterministic symbols but not the Gaussian
    coordinates themselves. Either matrix orientation can be supplied; missing
    entries mean zero. Distinct symbol names are never identified, including for
    singular covariance. Positive semidefiniteness is the caller's obligation.

    For flat activation products use E[G_i F] = sum_j K_ij E[d_j F], removing
    explicit polynomial factors in finitely many steps. Pure polynomials reduce
    by Wick's rule. An integrand containing a non-flat activation is retained as
    a general atom after linearity and deterministic-factor extraction: Stein
    differentiation of nested arguments need not decrease polynomial degree.
    With ``flat_only=True`` every phi argument must instead be literally one
    declared Gaussian symbol, or UnsupportedExpression is raised.
    """
    expression = _coerce(expression)
    coordinates = tuple(gaussian_symbols)
    if any(not isinstance(g, Expr) or g.op != "symbol" for g in coordinates):
        raise UnsupportedExpression("Gaussian coordinates must be symbols")
    source_set = frozenset(coordinates)
    if len(source_set) != len(coordinates):
        raise UnsupportedExpression("Gaussian coordinate names must be distinct")
    entries: dict[tuple[Expr, Expr], Expr] = {}
    for pair, value in covariance.items():
        if not isinstance(pair, tuple) or len(pair) != 2 or any(g not in source_set for g in pair):
            raise UnsupportedExpression("covariance keys must pair declared Gaussian symbols")
        value = _coerce(value)
        if symbols(value) & source_set:
            raise UnsupportedExpression("covariance entries must be independent of formal Gaussian coordinates")
        reverse = (pair[1], pair[0])
        if reverse in entries and entries[reverse] != value:
            raise UnsupportedExpression("conflicting symmetric covariance entries")
        entries[pair] = value
        entries[reverse] = value

    @lru_cache(maxsize=None)
    def is_flat(node: Expr) -> bool:
        if node.op == "phi":
            return node.args[0] in source_set
        return all(is_flat(argument) for argument in node.args)

    if flat_only and not is_flat(expression):
        raise UnsupportedExpression("flat moment reduction requires phi^(r) of a single Gaussian symbol")

    def new_atom(integrand: Expr) -> Expr:
        result = _coerce(atom(integrand))
        if symbols(result) & source_set:
            raise UnsupportedExpression("an expectation atom must be independent of Gaussian coordinates")
        return result

    @lru_cache(maxsize=None)
    def reduce(node: Expr) -> Expr:
        node = expand(node)
        if node.op == "add":
            return _add(*(reduce(a) for a in node.args))
        factors = node.args if node.op == "mul" else (node,)
        fixed = _mul(*(f for f in factors if not (symbols(f) & source_set)))
        random_factors = tuple(f for f in factors if symbols(f) & source_set)
        if not random_factors:
            return fixed
        random_part = _mul(*random_factors)
        if not is_flat(random_part):
            return fixed * new_atom(random_part)
        for index, factor in enumerate(random_factors):
            base = factor.args[0] if factor.op == "pow" else factor
            if base not in source_set:
                continue
            exponent = factor.value if factor.op == "pow" else 1
            remainder = _mul(base ** (exponent - 1), *random_factors[:index], *random_factors[index + 1:])
            terms = []
            for coordinate in coordinates:
                entry = entries.get((base, coordinate), const(0))
                if entry != const(0):
                    derivative = diff(remainder, coordinate)
                    if derivative != const(0):
                        terms.append(entry * reduce(derivative))
            return fixed * _add(*terms)
        return fixed * new_atom(random_part)

    return reduce(expression)
