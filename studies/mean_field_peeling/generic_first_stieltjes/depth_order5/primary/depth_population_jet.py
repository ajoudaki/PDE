"""Exact fixed-depth population jet through order five.

The compiler implements the chronological forward/backward matrix peel for a
single input and an arbitrary fixed number of hidden layers.  Temporary
Gaussian matrix innovations are eliminated internally by Wick--Stein
recursion.  Returned expressions contain only deterministic arithmetic and
one-dimensional layer-tagged activation moments.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial
from typing import Iterable

from ...order5.compiler.factored_expression import (
    FactoredMomentExpression as DExpr,
    atom,
    constant,
    product,
    summation,
    symbol,
    walk,
)
from ...order5.compiler.population_jet import activation_product_moment


MAX_ORDER = 5
MAX_DERIV = 10  # audit headroom; every terminal atom must vanish above five.


@dataclass(frozen=True)
class Layout:
    depth: int

    def __post_init__(self) -> None:
        if self.depth < 2:
            raise ValueError("depth must be at least two")

    @property
    def f_size(self) -> int:
        return (self.depth - 1) * MAX_ORDER

    @property
    def r_size(self) -> int:
        return (self.depth - 1) * MAX_ORDER

    @property
    def phi_size(self) -> int:
        return self.depth * (MAX_DERIV + 1)

    def f_index(self, matrix_layer: int, order: int) -> int:
        if not (2 <= matrix_layer <= self.depth and 1 <= order <= MAX_ORDER):
            raise ValueError((matrix_layer, order))
        return (matrix_layer - 2) * MAX_ORDER + order - 1

    def r_index(self, matrix_layer: int, order: int) -> int:
        if not (2 <= matrix_layer <= self.depth and 0 <= order < MAX_ORDER):
            raise ValueError((matrix_layer, order))
        return (matrix_layer - 2) * MAX_ORDER + order

    def phi_index(self, layer: int, derivative: int) -> int:
        if not (1 <= layer <= self.depth and 0 <= derivative <= MAX_DERIV):
            raise ValueError((layer, derivative))
        return (layer - 1) * (MAX_DERIV + 1) + derivative

    def f_slice(self, values: tuple[int, ...], matrix_layer: int) -> tuple[int, ...]:
        start = (matrix_layer - 2) * MAX_ORDER
        return values[start : start + MAX_ORDER]

    def r_slice(self, values: tuple[int, ...], matrix_layer: int) -> tuple[int, ...]:
        start = (matrix_layer - 2) * MAX_ORDER
        return values[start : start + MAX_ORDER]

    def phi_slice(self, values: tuple[int, ...], layer: int) -> tuple[int, ...]:
        start = (layer - 1) * (MAX_DERIV + 1)
        return values[start : start + MAX_DERIV + 1]


@dataclass(frozen=True, order=True)
class CoordinateMonomial:
    a: int
    f: tuple[int, ...]
    r: tuple[int, ...]
    phi: tuple[int, ...]

    @staticmethod
    def one(layout: Layout) -> "CoordinateMonomial":
        return CoordinateMonomial(
            0,
            (0,) * layout.f_size,
            (0,) * layout.r_size,
            (0,) * layout.phi_size,
        )

    def multiply(self, other: "CoordinateMonomial") -> "CoordinateMonomial":
        return CoordinateMonomial(
            self.a + other.a,
            tuple(x + y for x, y in zip(self.f, other.f)),
            tuple(x + y for x, y in zip(self.r, other.r)),
            tuple(x + y for x, y in zip(self.phi, other.phi)),
        )


@dataclass(frozen=True)
class CoordinatePolynomial:
    terms: tuple[tuple[CoordinateMonomial, DExpr], ...]

    @staticmethod
    def zero() -> "CoordinatePolynomial":
        return CoordinatePolynomial(())

    @staticmethod
    def constant(layout: Layout, value: int | Fraction | DExpr) -> "CoordinatePolynomial":
        value = dexpr(value)
        return CoordinatePolynomial(()) if not value else CoordinatePolynomial(((CoordinateMonomial.one(layout), value),))

    @staticmethod
    def from_dict(raw: dict[CoordinateMonomial, DExpr]) -> "CoordinatePolynomial":
        return CoordinatePolynomial(tuple(sorted((key, value) for key, value in raw.items() if value)))

    def as_dict(self) -> dict[CoordinateMonomial, DExpr]:
        return dict(self.terms)

    def __bool__(self) -> bool:
        return bool(self.terms)

    def __neg__(self) -> "CoordinatePolynomial":
        return CoordinatePolynomial(tuple((key, -value) for key, value in self.terms))

    def __add__(self, other: "CoordinatePolynomial") -> "CoordinatePolynomial":
        raw = self.as_dict()
        for key, value in other.terms:
            raw[key] = raw.get(key, constant(0)) + value
        return CoordinatePolynomial.from_dict(raw)

    __radd__ = __add__

    def __mul__(self, other: "CoordinatePolynomial") -> "CoordinatePolynomial":
        if not self or not other:
            return CoordinatePolynomial.zero()
        raw: dict[CoordinateMonomial, DExpr] = {}
        for left, cl in self.terms:
            for right, cr in other.terms:
                key = left.multiply(right)
                raw[key] = raw.get(key, constant(0)) + cl * cr
        return CoordinatePolynomial.from_dict(raw)

    __rmul__ = __mul__

    def scale(self, layout: Layout, value: int | Fraction | DExpr) -> "CoordinatePolynomial":
        return self * CoordinatePolynomial.constant(layout, value)

    def divide(self, layout: Layout, value: int) -> "CoordinatePolynomial":
        return self.scale(layout, Fraction(1, value))

    def derivative_f(
        self, layout: Layout, matrix_layer: int, order: int
    ) -> "CoordinatePolynomial":
        raw: dict[CoordinateMonomial, DExpr] = {}

        def emit(key: CoordinateMonomial, coefficient: DExpr) -> None:
            raw[key] = raw.get(key, constant(0)) + coefficient

        for key, coefficient in self.terms:
            if order > 0:
                index = layout.f_index(matrix_layer, order)
                count = key.f[index]
                if count:
                    values = list(key.f)
                    values[index] -= 1
                    emit(CoordinateMonomial(key.a, tuple(values), key.r, key.phi), count * coefficient)
            else:
                for derivative in range(MAX_DERIV):
                    index = layout.phi_index(matrix_layer, derivative)
                    count = key.phi[index]
                    if not count:
                        continue
                    values = list(key.phi)
                    values[index] -= 1
                    values[index + 1] += 1
                    emit(CoordinateMonomial(key.a, key.f, key.r, tuple(values)), count * coefficient)
        return CoordinatePolynomial.from_dict(raw)

    def derivative_r(
        self, layout: Layout, matrix_layer: int, order: int
    ) -> "CoordinatePolynomial":
        raw: dict[CoordinateMonomial, DExpr] = {}
        index = layout.r_index(matrix_layer, order)
        for key, coefficient in self.terms:
            count = key.r[index]
            if not count:
                continue
            values = list(key.r)
            values[index] -= 1
            new_key = CoordinateMonomial(key.a, key.f, tuple(values), key.phi)
            raw[new_key] = raw.get(new_key, constant(0)) + count * coefficient
        return CoordinatePolynomial.from_dict(raw)


def dexpr(value: int | Fraction | DExpr) -> DExpr:
    return value if isinstance(value, DExpr) else constant(value)


def cp_constant(layout: Layout, value: int | Fraction | DExpr) -> CoordinatePolynomial:
    return CoordinatePolynomial.constant(layout, value)


def cp_a(layout: Layout) -> CoordinatePolynomial:
    key = CoordinateMonomial.one(layout)
    return CoordinatePolynomial(((CoordinateMonomial(1, key.f, key.r, key.phi), constant(1)),))


def cp_f(layout: Layout, matrix_layer: int, order: int) -> CoordinatePolynomial:
    key = CoordinateMonomial.one(layout)
    values = list(key.f)
    values[layout.f_index(matrix_layer, order)] = 1
    return CoordinatePolynomial(((CoordinateMonomial(0, tuple(values), key.r, key.phi), constant(1)),))


def cp_r(layout: Layout, matrix_layer: int, order: int) -> CoordinatePolynomial:
    key = CoordinateMonomial.one(layout)
    values = list(key.r)
    values[layout.r_index(matrix_layer, order)] = 1
    return CoordinatePolynomial(((CoordinateMonomial(0, key.f, tuple(values), key.phi), constant(1)),))


def cp_phi(layout: Layout, layer: int, derivative: int) -> CoordinatePolynomial:
    key = CoordinateMonomial.one(layout)
    values = list(key.phi)
    values[layout.phi_index(layer, derivative)] = 1
    return CoordinatePolynomial(((CoordinateMonomial(0, key.f, key.r, tuple(values)), constant(1)),))


def activation_coefficient(
    layout: Layout,
    layer: int,
    perturbation: list[CoordinatePolynomial],
    degree: int,
    derivative_shift: int = 0,
) -> CoordinatePolynomial:
    if degree == 0:
        return cp_phi(layout, layer, derivative_shift)
    delta = [CoordinatePolynomial.zero()] + perturbation[1 : degree + 1]
    powers: list[list[CoordinatePolynomial]] = []
    p0 = [CoordinatePolynomial.zero()] * (degree + 1)
    p0[0] = cp_constant(layout, 1)
    powers.append(p0)
    for exponent in range(1, degree + 1):
        current = [CoordinatePolynomial.zero()] * (degree + 1)
        for left in range(1, degree + 1):
            if not delta[left]:
                continue
            for right in range(degree - left + 1):
                if powers[exponent - 1][right]:
                    current[left + right] = current[left + right] + delta[left] * powers[exponent - 1][right]
        powers.append(current)
    answer = CoordinatePolynomial.zero()
    for exponent in range(degree + 1):
        if powers[exponent][degree]:
            answer = answer + (
                cp_phi(layout, layer, derivative_shift + exponent)
                * powers[exponent][degree]
            ).scale(layout, Fraction(1, factorial(exponent)))
    return answer


def standard_gaussian_moment(power: int) -> int:
    if power % 2:
        return 0
    answer = 1
    for value in range(1, power, 2):
        answer *= value
    return answer


class Peeler:
    def __init__(self, layout: Layout):
        self.layout = layout
        self.H: dict[tuple[int, int, int], DExpr] = {}
        self.B: dict[tuple[int, int, int], DExpr] = {}
        self._r_cache: dict[tuple[int, tuple[int, ...]], DExpr] = {}
        self._f_cache: dict[tuple[int, tuple[int, ...], tuple[int, ...]], DExpr] = {}
        self._monomial_cache: dict[CoordinateMonomial, DExpr] = {}

    def set_h(self, matrix_layer: int, k: int, ell: int, value: DExpr) -> None:
        self.H[(matrix_layer, k, ell)] = value
        self.H[(matrix_layer, ell, k)] = value

    def set_b(self, matrix_layer: int, k: int, ell: int, value: DExpr) -> None:
        self.B[(matrix_layer, k, ell)] = value
        self.B[(matrix_layer, ell, k)] = value

    def r_wick(self, matrix_layer: int, exponents: tuple[int, ...]) -> DExpr:
        state = (matrix_layer, exponents)
        if state in self._r_cache:
            return self._r_cache[state]
        if not any(exponents):
            answer = constant(1)
        elif sum(exponents) % 2:
            answer = constant(0)
        else:
            i = next(index for index, count in enumerate(exponents) if count)
            remainder = list(exponents)
            remainder[i] -= 1
            terms: list[DExpr] = []
            for j, count in enumerate(remainder):
                if not count:
                    continue
                covariance = self.B.get((matrix_layer, i, j))
                if covariance is None:
                    raise RuntimeError(f"B[{matrix_layer},{i},{j}] missing")
                paired = list(remainder)
                paired[j] -= 1
                terms.append(count * covariance * self.r_wick(matrix_layer, tuple(paired)))
            answer = summation(tuple(terms))
        self._r_cache[state] = answer
        return answer

    def f_stein(
        self,
        matrix_layer: int,
        exponents: tuple[int, ...],
        phi_exponents: tuple[int, ...],
    ) -> DExpr:
        state = (matrix_layer, exponents, phi_exponents)
        if state in self._f_cache:
            return self._f_cache[state]
        if not any(exponents):
            answer = atom(f"L{matrix_layer}", phi_exponents) if any(phi_exponents) else constant(1)
        else:
            i0 = next(index for index, count in enumerate(exponents) if count)
            i = i0 + 1
            remainder = list(exponents)
            remainder[i0] -= 1
            terms: list[DExpr] = []
            for j0, count in enumerate(remainder):
                if not count:
                    continue
                covariance = self.H.get((matrix_layer, i, j0 + 1))
                if covariance is None:
                    raise RuntimeError(f"H[{matrix_layer},{i},{j0 + 1}] missing")
                paired = list(remainder)
                paired[j0] -= 1
                terms.append(count * covariance * self.f_stein(matrix_layer, tuple(paired), phi_exponents))
            covariance0 = self.H.get((matrix_layer, i, 0))
            if covariance0 is None:
                raise RuntimeError(f"H[{matrix_layer},{i},0] missing")
            for derivative, count in enumerate(phi_exponents[:-1]):
                if not count:
                    continue
                shifted = list(phi_exponents)
                shifted[derivative] -= 1
                shifted[derivative + 1] += 1
                terms.append(count * covariance0 * self.f_stein(matrix_layer, tuple(remainder), tuple(shifted)))
            answer = summation(tuple(terms))
        self._f_cache[state] = answer
        return answer

    def monomial(self, key: CoordinateMonomial) -> DExpr:
        if key in self._monomial_cache:
            return self._monomial_cache[key]
        answer = constant(standard_gaussian_moment(key.a))
        if not answer:
            self._monomial_cache[key] = answer
            return answer
        layer1 = self.layout.phi_slice(key.phi, 1)
        if any(layer1):
            answer = answer * atom("L1", layer1)
        for matrix_layer in range(2, self.layout.depth + 1):
            answer = answer * self.r_wick(
                matrix_layer, self.layout.r_slice(key.r, matrix_layer)
            )
            if not answer:
                break
            answer = answer * self.f_stein(
                matrix_layer,
                self.layout.f_slice(key.f, matrix_layer),
                self.layout.phi_slice(key.phi, matrix_layer),
            )
        self._monomial_cache[key] = answer
        return answer

    def expect(self, polynomial: CoordinatePolynomial) -> DExpr:
        return summation(
            tuple(coefficient * self.monomial(key) for key, coefficient in polynomial.terms)
        )


@dataclass(frozen=True)
class DepthJetResult:
    depth: int
    derivatives: tuple[DExpr, ...]
    alpha: dict[tuple[int, int, int], DExpr]
    beta: dict[tuple[int, int, int], DExpr]
    H: dict[tuple[int, int, int], DExpr]
    Bcov: dict[tuple[int, int, int], DExpr]
    counts: tuple[tuple[str, int], ...]

    @property
    def A(self) -> DExpr:
        return self.derivatives[1]

    @property
    def B(self) -> DExpr:
        return self.derivatives[3]

    @property
    def C(self) -> DExpr:
        return self.derivatives[5]


def compile_depth(
    depth: int,
    *,
    order: int = 5,
    arbitrary_q0: bool = True,
    verbose: bool = False,
) -> DepthJetResult:
    if not (0 <= order <= MAX_ORDER):
        raise ValueError("order must lie between zero and five")
    layout = Layout(depth)
    q0 = symbol("Q0") if arbitrary_q0 else constant(1)
    peeler = Peeler(layout)

    u = {layer: [CoordinatePolynomial.zero() for _ in range(order + 1)] for layer in range(1, depth + 1)}
    h = {layer: [CoordinatePolynomial.zero() for _ in range(order + 1)] for layer in range(1, depth + 1)}
    hp = {layer: [CoordinatePolynomial.zero() for _ in range(order + 1)] for layer in range(1, depth + 1)}
    b = {layer: [CoordinatePolynomial.zero() for _ in range(order)] for layer in range(1, depth + 1)}
    r = {
        matrix_layer: [CoordinatePolynomial.zero() for _ in range(order)]
        for matrix_layer in range(2, depth + 1)
    }
    a = [CoordinatePolynomial.zero() for _ in range(order + 1)]
    output = [constant(0) for _ in range(order + 1)]
    alpha: dict[tuple[int, int, int], DExpr] = {}
    beta: dict[tuple[int, int, int], DExpr] = {}
    counts: list[tuple[str, int]] = []
    a[0] = cp_a(layout)

    for k in range(order + 1):
        h[1][k] = activation_coefficient(layout, 1, u[1], k)
        if k < order:
            hp[1][k] = activation_coefficient(layout, 1, u[1], k, 1)

        for layer in range(2, depth + 1):
            for ell in range(k + 1):
                peeler.set_h(layer, k, ell, peeler.expect(h[layer - 1][k] * h[layer - 1][ell]))
            if k > 0:
                for s in range(k):
                    alpha[(layer, k, s)] = peeler.expect(
                        h[layer - 1][k].derivative_r(layout, layer, s)
                    )
                uk = cp_f(layout, layer, k)
                for s in range(k):
                    uk = uk + b[layer][s].scale(layout, alpha[(layer, k, s)])
                for degree in range(1, k + 1):
                    for p in range(degree):
                        q = degree - 1 - p
                        inner = peeler.expect(
                            h[layer - 1][q] * h[layer - 1][k - degree]
                        )
                        uk = uk + b[layer][p].scale(
                            layout, Fraction(1, degree) * inner
                        )
                u[layer][k] = uk
            h[layer][k] = activation_coefficient(layout, layer, u[layer], k)
            if k < order:
                hp[layer][k] = activation_coefficient(layout, layer, u[layer], k, 1)

        outk = CoordinatePolynomial.zero()
        for left in range(k + 1):
            outk = outk + a[left] * h[depth][k - left]
        output[k] = peeler.expect(outk)
        counts.append((f"out{k}", len(output[k].terms)))
        for layer in range(1, depth + 1):
            counts.append((f"h{layer}_{k}", len(h[layer][k].terms)))
        if verbose:
            print(f"k={k}", counts[-(depth + 1) :], flush=True)

        if k == order:
            break

        a[k + 1] = h[depth][k].divide(layout, k + 1)
        top = CoordinatePolynomial.zero()
        for left in range(k + 1):
            top = top + a[left] * hp[depth][k - left]
        b[depth][k] = top

        for matrix_layer in range(depth, 1, -1):
            for ell in range(k + 1):
                peeler.set_b(
                    matrix_layer,
                    k,
                    ell,
                    peeler.expect(b[matrix_layer][k] * b[matrix_layer][ell]),
                )
            for s in range(k + 1):
                beta[(matrix_layer, k, s)] = peeler.expect(
                    b[matrix_layer][k].derivative_f(layout, matrix_layer, s)
                )
            rk = cp_r(layout, matrix_layer, k)
            for s in range(k + 1):
                rk = rk + h[matrix_layer - 1][s].scale(
                    layout, beta[(matrix_layer, k, s)]
                )
            for degree in range(1, k + 1):
                for p in range(degree):
                    q = degree - 1 - p
                    inner = peeler.expect(
                        b[matrix_layer][p] * b[matrix_layer][k - degree]
                    )
                    rk = rk + h[matrix_layer - 1][q].scale(
                        layout, Fraction(1, degree) * inner
                    )
            r[matrix_layer][k] = rk
            lower = CoordinatePolynomial.zero()
            for left in range(k + 1):
                lower = (
                    lower
                    + hp[matrix_layer - 1][left]
                    * r[matrix_layer][k - left]
                )
            b[matrix_layer - 1][k] = lower

        u[1][k + 1] = b[1][k].scale(layout, q0).divide(layout, k + 1)

    derivatives = tuple(factorial(k) * output[k] for k in range(order + 1))
    return DepthJetResult(depth, derivatives, alpha, beta, peeler.H, peeler.B, tuple(counts))


def specialize_unit_gram(root: DExpr) -> DExpr:
    """Map every layer atom to M and impose Q0=M_200000=1."""

    base = (2,) + (0,) * MAX_DERIV
    memo: dict[DExpr, DExpr] = {}

    def visit(node: DExpr) -> DExpr:
        if node in memo:
            return memo[node]
        kind = node.node[0]
        if kind == "const":
            answer = node
        elif kind == "symbol":
            answer = constant(1) if node.node[1] == "Q0" else node
        elif kind == "atom":
            answer = constant(1) if node.node[2] == base else atom("M", node.node[2])
        elif kind == "add":
            answer = summation(tuple(visit(child) for child in node.node[1]))
        elif kind == "mul":
            answer = product(tuple(visit(child) for child in node.node[1]))
        else:
            raise ValueError(kind)
        memo[node] = answer
        return answer

    return visit(root)


def terminal_maximum_derivative(root: DExpr) -> int:
    maximum = 0
    for node in walk(root):
        if node.node[0] == "atom":
            for derivative, count in enumerate(node.node[2]):
                if count:
                    maximum = max(maximum, derivative)
    return maximum


def polynomial_forward_variances(
    depth: int,
    coefficients: Iterable[int | Fraction],
    *,
    q0: int | Fraction = 1,
) -> tuple[Fraction, ...]:
    """Return ``(Q^0,...,Q^depth)`` exactly for a polynomial control."""

    coefficients = tuple(Fraction(value) for value in coefficients)
    variances = [Fraction(q0)]
    square = (2,) + (0,) * MAX_DERIV
    for _ in range(depth):
        variances.append(
            activation_product_moment(square, coefficients, variances[-1])
        )
    return tuple(variances)


def evaluate_polynomial_activation(
    root: DExpr,
    depth: int,
    coefficients: Iterable[int | Fraction],
    *,
    q0: int | Fraction = 1,
) -> Fraction:
    """Evaluate a layer-tagged terminal DAG by exact Gaussian moments."""

    coefficients = tuple(Fraction(value) for value in coefficients)
    variances = polynomial_forward_variances(depth, coefficients, q0=q0)
    memo: dict[DExpr, Fraction] = {}

    def visit(node: DExpr) -> Fraction:
        if node in memo:
            return memo[node]
        kind = node.node[0]
        if kind == "const":
            answer = node.node[1]
        elif kind == "symbol":
            if node.node[1] != "Q0":
                raise KeyError(node.node[1])
            answer = Fraction(q0)
        elif kind == "atom":
            tag, exponent = node.node[1], node.node[2]
            if not tag.startswith("L"):
                raise KeyError(tag)
            layer = int(tag[1:])
            if not 1 <= layer <= depth:
                raise KeyError(tag)
            answer = activation_product_moment(
                exponent, coefficients, variances[layer - 1]
            )
        elif kind == "add":
            answer = sum((visit(child) for child in node.node[1]), Fraction(0))
        elif kind == "mul":
            answer = Fraction(1)
            for child in node.node[1]:
                answer *= visit(child)
        else:
            raise ValueError(kind)
        memo[node] = answer
        return answer

    return visit(root)
