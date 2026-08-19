"""Typed Gaussian-normal-form expressions for the first-Stieltjes program.

The module deliberately keeps the symbolic language small.  A scalar is a
finite DAG made from rational constants, named scalars, sums, products,
nonnegative integer powers, and literal Gaussian atoms

    E[prod_j phi^(r_j)(X_{i_j})],   X ~ N(0, Sigma).

Covariance entries are themselves scalar expressions, so layerwise Gaussian
recursions can be represented without hiding a numerical quadrature or an
unbounded random object in a node.  ``evaluate_polynomial`` is an independent
exact Wick evaluator used by the linear/quadratic regression gates.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import prod as integer_product
from typing import Callable, Iterable, Mapping, Sequence, TypeAlias

import numpy as np
from numpy.polynomial.hermite import hermgauss


Number = int | Fraction


class Scalar:
    """Marker base class for scalar Gaussian-normal-form nodes."""


@dataclass(frozen=True)
class Rational(Scalar):
    value: Fraction

    def __init__(self, value: Number):
        object.__setattr__(self, "value", Fraction(value))


@dataclass(frozen=True)
class Symbol(Scalar):
    name: str

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("symbol name must be nonempty")


@dataclass(frozen=True)
class Sum(Scalar):
    terms: tuple[Scalar, ...]


@dataclass(frozen=True)
class Product(Scalar):
    factors: tuple[Scalar, ...]


@dataclass(frozen=True)
class Power(Scalar):
    base: Scalar
    exponent: int

    def __post_init__(self) -> None:
        if self.exponent < 0:
            raise ValueError("only nonnegative powers belong to the GNF IR")


@dataclass(frozen=True, order=True)
class PhiFactor:
    """One or more copies of ``phi^(derivative)(X_variable)``."""

    variable: int
    derivative: int = 0
    multiplicity: int = 1

    def __post_init__(self) -> None:
        if self.variable < 0:
            raise ValueError("Gaussian variable index must be nonnegative")
        if self.derivative < 0:
            raise ValueError("activation derivative order must be nonnegative")
        if self.multiplicity < 1:
            raise ValueError("factor multiplicity must be positive")


@dataclass(frozen=True)
class GaussianAtom(Scalar):
    """A literal centered multivariate-Gaussian expectation."""

    covariance: tuple[tuple[Scalar, ...], ...]
    factors: tuple[PhiFactor, ...]
    tag: str = ""

    def __post_init__(self) -> None:
        dimension = len(self.covariance)
        if dimension < 1:
            raise ValueError("a Gaussian atom must have positive dimension")
        if any(len(row) != dimension for row in self.covariance):
            raise ValueError("Gaussian covariance must be square")
        for i in range(dimension):
            for j in range(i):
                if self.covariance[i][j] != self.covariance[j][i]:
                    raise ValueError("Gaussian covariance must be symmetric")
        if any(factor.variable >= dimension for factor in self.factors):
            raise ValueError("factor references a missing Gaussian variable")


ScalarLike: TypeAlias = Scalar | Number


def scalar(value: ScalarLike) -> Scalar:
    return value if isinstance(value, Scalar) else Rational(value)


def _key(expr: Scalar) -> str:
    """Stable structural key used only for deterministic canonical ordering."""

    return repr(expr)


def add(*terms: ScalarLike) -> Scalar:
    flat: list[Scalar] = []
    constant = Fraction(0)
    for raw in terms:
        term = scalar(raw)
        children = term.terms if isinstance(term, Sum) else (term,)
        for child in children:
            if isinstance(child, Rational):
                constant += child.value
            else:
                flat.append(child)
    if constant:
        flat.append(Rational(constant))
    if not flat:
        return Rational(0)
    flat.sort(key=_key)
    return flat[0] if len(flat) == 1 else Sum(tuple(flat))


def mul(*factors: ScalarLike) -> Scalar:
    flat: list[Scalar] = []
    constant = Fraction(1)
    for raw in factors:
        factor = scalar(raw)
        children = factor.factors if isinstance(factor, Product) else (factor,)
        for child in children:
            if isinstance(child, Rational):
                constant *= child.value
            else:
                flat.append(child)
    if constant == 0:
        return Rational(0)
    exponents: dict[Scalar, int] = {}
    for child in flat:
        if isinstance(child, Power):
            exponents[child.base] = exponents.get(child.base, 0) + child.exponent
        else:
            exponents[child] = exponents.get(child, 0) + 1
    canonical = [
        base if exponent == 1 else Power(base, exponent)
        for base, exponent in exponents.items()
        if exponent
    ]
    if constant != 1 or not canonical:
        canonical.append(Rational(constant))
    canonical.sort(key=_key)
    return canonical[0] if len(canonical) == 1 else Product(tuple(canonical))


def power(base: ScalarLike, exponent: int) -> Scalar:
    base = scalar(base)
    if exponent < 0:
        raise ValueError("negative powers are not allowed")
    if exponent == 0:
        return Rational(1)
    if exponent == 1:
        return base
    if isinstance(base, Rational):
        return Rational(base.value**exponent)
    if isinstance(base, Power):
        return Power(base.base, base.exponent * exponent)
    return Power(base, exponent)


def atom(
    covariance: Sequence[Sequence[ScalarLike]],
    factors: Iterable[PhiFactor],
    *,
    tag: str = "",
) -> GaussianAtom:
    cov = tuple(tuple(scalar(entry) for entry in row) for row in covariance)
    merged: dict[tuple[int, int], int] = {}
    for factor in factors:
        key = (factor.variable, factor.derivative)
        merged[key] = merged.get(key, 0) + factor.multiplicity
    canonical_factors = tuple(
        PhiFactor(variable, derivative, multiplicity)
        for (variable, derivative), multiplicity in sorted(merged.items())
    )
    return GaussianAtom(cov, canonical_factors, tag)


@dataclass(frozen=True)
class PolynomialActivation:
    """Exact polynomial activation, coefficients in increasing degree."""

    coefficients: tuple[Fraction, ...]

    def __init__(self, coefficients: Sequence[Number]):
        values = [Fraction(value) for value in coefficients]
        while len(values) > 1 and values[-1] == 0:
            values.pop()
        if not values:
            values = [Fraction(0)]
        object.__setattr__(self, "coefficients", tuple(values))

    def derivative(self, order: int) -> tuple[Fraction, ...]:
        if order < 0:
            raise ValueError("derivative order must be nonnegative")
        values = list(self.coefficients)
        for _ in range(order):
            values = [Fraction(k) * values[k] for k in range(1, len(values))]
            if not values:
                return (Fraction(0),)
        return tuple(values)


Poly = dict[tuple[int, ...], Fraction]


def _poly_mul(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for alpha, ca in left.items():
        for beta, cb in right.items():
            exponent = tuple(a + b for a, b in zip(alpha, beta))
            out[exponent] = out.get(exponent, Fraction(0)) + ca * cb
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}


def _factor_polynomial(
    dimension: int,
    factor: PhiFactor,
    activation: PolynomialActivation,
) -> Poly:
    derivative = activation.derivative(factor.derivative)
    base: Poly = {}
    for degree, coefficient in enumerate(derivative):
        if coefficient:
            exponent = [0] * dimension
            exponent[factor.variable] = degree
            base[tuple(exponent)] = coefficient
    out: Poly = {(0,) * dimension: Fraction(1)}
    for _ in range(factor.multiplicity):
        out = _poly_mul(out, base)
    return out


def _gaussian_monomial(
    exponent: tuple[int, ...], covariance: tuple[tuple[Fraction, ...], ...]
) -> Fraction:
    """Exact Isserlis recursion for one centered Gaussian monomial."""

    @lru_cache(None)
    def moment(alpha: tuple[int, ...]) -> Fraction:
        total = sum(alpha)
        if total == 0:
            return Fraction(1)
        if total % 2:
            return Fraction(0)
        i = next(index for index, count in enumerate(alpha) if count)
        remainder = list(alpha)
        remainder[i] -= 1
        answer = Fraction(0)
        for j, count in enumerate(remainder):
            if not count:
                continue
            paired = list(remainder)
            paired[j] -= 1
            answer += count * covariance[i][j] * moment(tuple(paired))
        return answer

    return moment(exponent)


def evaluate_polynomial(
    expr: ScalarLike,
    activation: PolynomialActivation,
    symbols: Mapping[str, Number],
) -> Fraction:
    """Evaluate a GNF expression exactly for a polynomial activation."""

    node = scalar(expr)
    if isinstance(node, Rational):
        return node.value
    if isinstance(node, Symbol):
        if node.name not in symbols:
            raise KeyError(f"missing scalar symbol {node.name!r}")
        return Fraction(symbols[node.name])
    if isinstance(node, Sum):
        return sum(
            (evaluate_polynomial(term, activation, symbols) for term in node.terms),
            Fraction(0),
        )
    if isinstance(node, Product):
        return integer_product(
            evaluate_polynomial(factor, activation, symbols) for factor in node.factors
        )
    if isinstance(node, Power):
        return evaluate_polynomial(node.base, activation, symbols) ** node.exponent
    if isinstance(node, GaussianAtom):
        covariance = tuple(
            tuple(evaluate_polynomial(entry, activation, symbols) for entry in row)
            for row in node.covariance
        )
        dimension = len(covariance)
        integrand: Poly = {(0,) * dimension: Fraction(1)}
        for factor in node.factors:
            integrand = _poly_mul(
                integrand, _factor_polynomial(dimension, factor, activation)
            )
        return sum(
            (
                coefficient * _gaussian_monomial(exponent, covariance)
                for exponent, coefficient in integrand.items()
            ),
            Fraction(0),
        )
    raise TypeError(f"unsupported GNF node {type(node)!r}")


DerivativeOracle = Callable[[int, np.ndarray], np.ndarray]


def evaluate_quadrature(
    expr: ScalarLike,
    activation_derivative: DerivativeOracle,
    symbols: Mapping[str, float],
    *,
    order: int = 32,
) -> float:
    """Deterministic tensor Gauss--Hermite audit evaluator.

    This backend is intentionally not part of the theorem: its cost is
    ``order ** dimension`` and it is used only on the small atoms emitted by
    the base-case compiler.
    """

    node = scalar(expr)
    if isinstance(node, Rational):
        return float(node.value)
    if isinstance(node, Symbol):
        return float(symbols[node.name])
    if isinstance(node, Sum):
        return sum(
            evaluate_quadrature(term, activation_derivative, symbols, order=order)
            for term in node.terms
        )
    if isinstance(node, Product):
        return float(
            np.prod(
                [
                    evaluate_quadrature(factor, activation_derivative, symbols, order=order)
                    for factor in node.factors
                ]
            )
        )
    if isinstance(node, Power):
        return evaluate_quadrature(
            node.base, activation_derivative, symbols, order=order
        ) ** node.exponent
    if isinstance(node, GaussianAtom):
        covariance = np.asarray(
            [
                [
                    evaluate_quadrature(entry, activation_derivative, symbols, order=order)
                    for entry in row
                ]
                for row in node.covariance
            ],
            dtype=np.float64,
        )
        covariance = 0.5 * (covariance + covariance.T)
        eigenvalues, eigenvectors = np.linalg.eigh(covariance)
        tolerance = 1.0e-11 * max(1.0, float(np.max(np.abs(eigenvalues))))
        if float(np.min(eigenvalues)) < -tolerance:
            raise ValueError(f"Gaussian covariance is not PSD: {eigenvalues}")
        root = eigenvectors @ np.diag(np.sqrt(np.maximum(eigenvalues, 0.0)))
        nodes, weights = hermgauss(order)
        nodes = np.sqrt(2.0) * nodes
        weights = weights / np.sqrt(np.pi)
        answer = 0.0
        dimension = len(covariance)
        for index in product(range(order), repeat=dimension):
            standard = np.asarray([nodes[k] for k in index])
            gaussian = root @ standard
            value = 1.0
            for factor in node.factors:
                value *= float(
                    activation_derivative(
                        factor.derivative,
                        np.asarray(gaussian[factor.variable]),
                    )
                ) ** factor.multiplicity
            answer += float(np.prod([weights[k] for k in index])) * value
        return answer
    raise TypeError(f"unsupported GNF node {type(node)!r}")


def _latex_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return rf"\frac{{{value.numerator}}}{{{value.denominator}}}"


def to_latex(expr: ScalarLike) -> str:
    """Render the literal GNF expression without assigning hidden semantics."""

    node = scalar(expr)
    if isinstance(node, Rational):
        return _latex_fraction(node.value)
    if isinstance(node, Symbol):
        return node.name
    if isinstance(node, Sum):
        return " + ".join(to_latex(term) for term in node.terms)
    if isinstance(node, Product):
        return " ".join(
            rf"\left({to_latex(factor)}\right)" if isinstance(factor, Sum) else to_latex(factor)
            for factor in node.factors
        )
    if isinstance(node, Power):
        return rf"\left({to_latex(node.base)}\right)^{{{node.exponent}}}"
    if isinstance(node, GaussianAtom):
        factors = []
        for factor in node.factors:
            derivative = "" if factor.derivative == 0 else rf"^{{({factor.derivative})}}"
            power_suffix = "" if factor.multiplicity == 1 else rf"^{{{factor.multiplicity}}}"
            factors.append(
                rf"\phi{derivative}(X_{{{factor.variable + 1}}}){power_suffix}"
            )
        covariance = ";".join(
            ",".join(to_latex(entry) for entry in row) for row in node.covariance
        )
        integrand = " ".join(factors) if factors else "1"
        return rf"\mathbb{{E}}_{{X\sim N(0,[{covariance}])}}[{integrand}]"
    raise TypeError(f"unsupported GNF node {type(node)!r}")


def atom_inventory(expr: ScalarLike) -> tuple[GaussianAtom, ...]:
    """Return unique atoms in dependency-first order."""

    seen: set[GaussianAtom] = set()
    ordered: list[GaussianAtom] = []

    def visit(node: Scalar) -> None:
        if isinstance(node, (Rational, Symbol)):
            return
        if isinstance(node, Sum):
            for term in node.terms:
                visit(term)
            return
        if isinstance(node, Product):
            for factor in node.factors:
                visit(factor)
            return
        if isinstance(node, Power):
            visit(node.base)
            return
        if isinstance(node, GaussianAtom):
            for row in node.covariance:
                for entry in row:
                    visit(entry)
            if node not in seen:
                seen.add(node)
                ordered.append(node)
            return
        raise TypeError(type(node))

    visit(scalar(expr))
    return tuple(ordered)


def maximum_activation_derivative(expr: ScalarLike) -> int:
    atoms = atom_inventory(expr)
    return max(
        (factor.derivative for item in atoms for factor in item.factors),
        default=0,
    )


def to_data(expr: ScalarLike) -> dict:
    """Return a lossless JSON-serializable representation of one GNF DAG."""

    node = scalar(expr)
    if isinstance(node, Rational):
        return {
            "type": "rational",
            "numerator": node.value.numerator,
            "denominator": node.value.denominator,
        }
    if isinstance(node, Symbol):
        return {"type": "symbol", "name": node.name}
    if isinstance(node, Sum):
        return {"type": "sum", "terms": [to_data(term) for term in node.terms]}
    if isinstance(node, Product):
        return {
            "type": "product",
            "factors": [to_data(factor) for factor in node.factors],
        }
    if isinstance(node, Power):
        return {
            "type": "power",
            "base": to_data(node.base),
            "exponent": node.exponent,
        }
    if isinstance(node, GaussianAtom):
        return {
            "type": "gaussian_atom",
            "tag": node.tag,
            "covariance": [
                [to_data(entry) for entry in row] for row in node.covariance
            ],
            "factors": [
                {
                    "variable": factor.variable,
                    "derivative": factor.derivative,
                    "multiplicity": factor.multiplicity,
                }
                for factor in node.factors
            ],
        }
    raise TypeError(f"unsupported GNF node {type(node)!r}")
