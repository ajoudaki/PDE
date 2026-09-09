"""Exact symbolic population jet through order five.

This module implements the alternating Gaussian-matrix peel for the scalar
``H=2, B=1`` feature-flow ODE.  Ordinary Taylor coefficients are used
throughout.  The internal coordinate language contains fresh forward and
transpose Gaussian variables, but :func:`compile_population_jet` eliminates
all of them by exact Wick--Stein recursion.  Its returned objects are sparse
polynomials whose only atoms are one-dimensional activation moments.

The implementation is intentionally independent of the order-three compiler
in ``generic_first_stieltjes/compiler``.  It is also deliberately unit-metric
(``Q^0=1``), while retaining distinct first- and second-layer moment atoms;
this permits exact checks of the unnormalised quadratic activation, for which
``Q^1=3``.  Calling :meth:`MomentPolynomial.collapse_unit_layers` identifies
the two atom families and gives the requested ``Q^0=Q^1=Q^2=1`` grammar.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import factorial
from typing import Iterable, Mapping


# Two extra derivative slots are retained as an audit tripwire.  A valid
# order-five terminal expression must have zero support above derivative 5.
MAX_DERIV = 7
MAX_ORDER = 5

Exponent = tuple[int, ...]
Atom = tuple[str, Exponent]  # layer is "X", "Y", or "M" after collapse.
MomentMonomial = tuple[Atom, ...]


def _zero_exponent() -> Exponent:
    return (0,) * (MAX_DERIV + 1)


@dataclass(frozen=True)
class MomentPolynomial:
    """Sparse rational polynomial in literal one-dimensional moments."""

    terms: tuple[tuple[MomentMonomial, Fraction], ...]

    @staticmethod
    def zero() -> "MomentPolynomial":
        return MomentPolynomial(())

    @staticmethod
    def constant(value: int | Fraction) -> "MomentPolynomial":
        value = Fraction(value)
        return MomentPolynomial(()) if not value else MomentPolynomial((((), value),))

    @staticmethod
    def atom(layer: str, exponent: Exponent) -> "MomentPolynomial":
        if len(exponent) != MAX_DERIV + 1:
            raise ValueError("wrong moment exponent length")
        if not any(exponent):
            return MomentPolynomial.constant(1)
        return MomentPolynomial(((((layer, exponent),), Fraction(1)),))

    @staticmethod
    def from_dict(raw: Mapping[MomentMonomial, Fraction]) -> "MomentPolynomial":
        cleaned = tuple(sorted((key, Fraction(value)) for key, value in raw.items() if value))
        return MomentPolynomial(cleaned)

    def as_dict(self) -> dict[MomentMonomial, Fraction]:
        return dict(self.terms)

    def __bool__(self) -> bool:
        return bool(self.terms)

    def __neg__(self) -> "MomentPolynomial":
        return MomentPolynomial(tuple((key, -value) for key, value in self.terms))

    def __add__(self, other: "MomentPolynomial | int | Fraction") -> "MomentPolynomial":
        other = mp(other)
        raw = self.as_dict()
        for key, value in other.terms:
            raw[key] = raw.get(key, Fraction(0)) + value
        return MomentPolynomial.from_dict(raw)

    __radd__ = __add__

    def __sub__(self, other: "MomentPolynomial | int | Fraction") -> "MomentPolynomial":
        return self + (-mp(other))

    def __rsub__(self, other: "MomentPolynomial | int | Fraction") -> "MomentPolynomial":
        return mp(other) - self

    def __mul__(self, other: "MomentPolynomial | int | Fraction") -> "MomentPolynomial":
        other = mp(other)
        if not self or not other:
            return MomentPolynomial.zero()
        raw: dict[MomentMonomial, Fraction] = {}
        for left, cl in self.terms:
            for right, cr in other.terms:
                key = tuple(sorted(left + right))
                raw[key] = raw.get(key, Fraction(0)) + cl * cr
        return MomentPolynomial.from_dict(raw)

    __rmul__ = __mul__

    def __truediv__(self, value: int | Fraction) -> "MomentPolynomial":
        if isinstance(value, MomentPolynomial):
            raise TypeError("moment-polynomial division is outside the terminal grammar")
        return self * (Fraction(1) / Fraction(value))

    def pow(self, exponent: int) -> "MomentPolynomial":
        if exponent < 0:
            raise ValueError("negative polynomial power")
        out = MomentPolynomial.constant(1)
        base = self
        power = exponent
        while power:
            if power & 1:
                out = out * base
            power >>= 1
            if power:
                base = base * base
        return out

    def collapse_unit_layers(self) -> "MomentPolynomial":
        """Identify X and Y atoms with the canonical standard-normal M atom."""

        raw: dict[MomentMonomial, Fraction] = {}
        for monomial, coefficient in self.terms:
            collapsed = tuple(sorted(("M", exponent) for _, exponent in monomial))
            raw[collapsed] = raw.get(collapsed, Fraction(0)) + coefficient
        return MomentPolynomial.from_dict(raw)

    def maximum_derivative(self) -> int:
        answer = 0
        for monomial, _ in self.terms:
            for _, exponent in monomial:
                for derivative, count in enumerate(exponent):
                    if count:
                        answer = max(answer, derivative)
        return answer


def mp(value: MomentPolynomial | int | Fraction) -> MomentPolynomial:
    return value if isinstance(value, MomentPolynomial) else MomentPolynomial.constant(value)


@dataclass(frozen=True, order=True)
class CoordinateMonomial:
    """One coordinate monomial before the Gaussian auxiliaries are peeled."""

    a: int
    f: tuple[int, ...]  # F_1,...,F_5; F_0 is the Y activation argument.
    r: tuple[int, ...]  # R_0,...,R_4.
    x: Exponent
    y: Exponent

    @staticmethod
    def one() -> "CoordinateMonomial":
        return CoordinateMonomial(0, (0,) * MAX_ORDER, (0,) * MAX_ORDER, _zero_exponent(), _zero_exponent())

    def multiply(self, other: "CoordinateMonomial") -> "CoordinateMonomial":
        return CoordinateMonomial(
            self.a + other.a,
            tuple(x + y for x, y in zip(self.f, other.f)),
            tuple(x + y for x, y in zip(self.r, other.r)),
            tuple(x + y for x, y in zip(self.x, other.x)),
            tuple(x + y for x, y in zip(self.y, other.y)),
        )


@dataclass(frozen=True)
class CoordinatePolynomial:
    """Sparse coordinate polynomial with moment-polynomial coefficients."""

    terms: tuple[tuple[CoordinateMonomial, MomentPolynomial], ...]

    @staticmethod
    def zero() -> "CoordinatePolynomial":
        return CoordinatePolynomial(())

    @staticmethod
    def constant(value: int | Fraction | MomentPolynomial) -> "CoordinatePolynomial":
        value = mp(value)
        return CoordinatePolynomial(()) if not value else CoordinatePolynomial(((CoordinateMonomial.one(), value),))

    @staticmethod
    def variable(kind: str, index: int = 0) -> "CoordinatePolynomial":
        one = CoordinateMonomial.one()
        if kind == "A":
            key = CoordinateMonomial(1, one.f, one.r, one.x, one.y)
        elif kind == "F":
            f = list(one.f)
            if not 1 <= index <= MAX_ORDER:
                raise ValueError("fresh forward index must be 1,...,5")
            f[index - 1] = 1
            key = CoordinateMonomial(0, tuple(f), one.r, one.x, one.y)
        elif kind == "R":
            r = list(one.r)
            if not 0 <= index < MAX_ORDER:
                raise ValueError("fresh transpose index must be 0,...,4")
            r[index] = 1
            key = CoordinateMonomial(0, one.f, tuple(r), one.x, one.y)
        elif kind in {"X", "Y"}:
            exponent = [0] * (MAX_DERIV + 1)
            if not 0 <= index <= MAX_DERIV:
                raise ValueError("activation derivative exceeds audit capacity")
            exponent[index] = 1
            key = CoordinateMonomial(0, one.f, one.r, tuple(exponent) if kind == "X" else one.x, tuple(exponent) if kind == "Y" else one.y)
        else:
            raise ValueError(kind)
        return CoordinatePolynomial(((key, MomentPolynomial.constant(1)),))

    @staticmethod
    def from_dict(raw: Mapping[CoordinateMonomial, MomentPolynomial]) -> "CoordinatePolynomial":
        return CoordinatePolynomial(tuple(sorted((key, value) for key, value in raw.items() if value)))

    def as_dict(self) -> dict[CoordinateMonomial, MomentPolynomial]:
        return dict(self.terms)

    def __bool__(self) -> bool:
        return bool(self.terms)

    def __neg__(self) -> "CoordinatePolynomial":
        return CoordinatePolynomial(tuple((key, -value) for key, value in self.terms))

    def __add__(self, other: "CoordinatePolynomial | int | Fraction | MomentPolynomial") -> "CoordinatePolynomial":
        other = cp(other)
        raw = self.as_dict()
        for key, value in other.terms:
            raw[key] = raw.get(key, MomentPolynomial.zero()) + value
        return CoordinatePolynomial.from_dict(raw)

    __radd__ = __add__

    def __sub__(self, other: "CoordinatePolynomial | int | Fraction | MomentPolynomial") -> "CoordinatePolynomial":
        return self + (-cp(other))

    def __mul__(self, other: "CoordinatePolynomial | int | Fraction | MomentPolynomial") -> "CoordinatePolynomial":
        other = cp(other)
        if not self or not other:
            return CoordinatePolynomial.zero()
        raw: dict[CoordinateMonomial, MomentPolynomial] = {}
        for left, cl in self.terms:
            for right, cr in other.terms:
                key = left.multiply(right)
                raw[key] = raw.get(key, MomentPolynomial.zero()) + cl * cr
        return CoordinatePolynomial.from_dict(raw)

    __rmul__ = __mul__

    def divide(self, value: int) -> "CoordinatePolynomial":
        return self * Fraction(1, value)

    def pow(self, exponent: int) -> "CoordinatePolynomial":
        if exponent < 0:
            raise ValueError("negative coordinate power")
        out = CoordinatePolynomial.constant(1)
        base = self
        power = exponent
        while power:
            if power & 1:
                out = out * base
            power >>= 1
            if power:
                base = base * base
        return out

    def derivative(self, kind: str, index: int) -> "CoordinatePolynomial":
        raw: dict[CoordinateMonomial, MomentPolynomial] = {}

        def emit(key: CoordinateMonomial, coefficient: MomentPolynomial) -> None:
            raw[key] = raw.get(key, MomentPolynomial.zero()) + coefficient

        for key, coefficient in self.terms:
            if kind == "R":
                count = key.r[index]
                if count:
                    values = list(key.r)
                    values[index] -= 1
                    emit(CoordinateMonomial(key.a, key.f, tuple(values), key.x, key.y), count * coefficient)
            elif kind == "F" and index > 0:
                count = key.f[index - 1]
                if count:
                    values = list(key.f)
                    values[index - 1] -= 1
                    emit(CoordinateMonomial(key.a, tuple(values), key.r, key.x, key.y), count * coefficient)
            elif kind == "F" and index == 0:
                for derivative, count in enumerate(key.y[:-1]):
                    if not count:
                        continue
                    values = list(key.y)
                    values[derivative] -= 1
                    values[derivative + 1] += 1
                    emit(CoordinateMonomial(key.a, key.f, key.r, key.x, tuple(values)), count * coefficient)
            else:
                raise ValueError((kind, index))
        return CoordinatePolynomial.from_dict(raw)


def cp(value: CoordinatePolynomial | MomentPolynomial | int | Fraction) -> CoordinatePolynomial:
    return value if isinstance(value, CoordinatePolynomial) else CoordinatePolynomial.constant(value)


def _activation_coefficient(
    layer: str,
    perturbation: list[CoordinatePolynomial],
    degree: int,
    derivative_shift: int = 0,
) -> CoordinatePolynomial:
    """Coefficient of phi^(shift)(base + sum_{k>=1} t^k delta_k)."""

    if degree == 0:
        return CoordinatePolynomial.variable(layer, derivative_shift)
    delta = [CoordinatePolynomial.zero()] + perturbation[1 : degree + 1]
    answer = CoordinatePolynomial.zero()
    # coefficient of delta(t)^m at t^degree, built by truncated convolution.
    powers: list[list[CoordinatePolynomial]] = []
    p0 = [CoordinatePolynomial.zero()] * (degree + 1)
    p0[0] = CoordinatePolynomial.constant(1)
    powers.append(p0)
    for m in range(1, degree + 1):
        current = [CoordinatePolynomial.zero()] * (degree + 1)
        for left in range(1, degree + 1):
            if not delta[left]:
                continue
            for right in range(degree - left + 1):
                if powers[m - 1][right]:
                    current[left + right] = current[left + right] + delta[left] * powers[m - 1][right]
        powers.append(current)
    for m in range(degree + 1):
        if powers[m][degree]:
            answer = answer + CoordinatePolynomial.variable(layer, derivative_shift + m) * powers[m][degree] * Fraction(1, factorial(m))
    return answer


def _standard_gaussian_moment(power: int) -> int:
    if power % 2:
        return 0
    out = 1
    for value in range(1, power, 2):
        out *= value
    return out


class Peeler:
    """Wick--Stein eliminator with deterministic covariance polynomials."""

    def __init__(self) -> None:
        self.H: list[list[MomentPolynomial | None]] = [[None] * (MAX_ORDER + 1) for _ in range(MAX_ORDER + 1)]
        self.B: list[list[MomentPolynomial | None]] = [[None] * MAX_ORDER for _ in range(MAX_ORDER)]
        self._first_cache: dict[CoordinateMonomial, MomentPolynomial] = {}
        self._second_cache: dict[CoordinateMonomial, MomentPolynomial] = {}
        self._r_wick_cache: dict[tuple[int, ...], MomentPolynomial] = {}
        self._f_stein_cache: dict[tuple[tuple[int, ...], Exponent], MomentPolynomial] = {}

    def _r_wick(self, exponents: tuple[int, ...]) -> MomentPolynomial:
        if exponents in self._r_wick_cache:
            return self._r_wick_cache[exponents]
        if not any(exponents):
            answer = MomentPolynomial.constant(1)
        elif sum(exponents) % 2:
            answer = MomentPolynomial.zero()
        else:
            i = next(index for index, count in enumerate(exponents) if count)
            remainder = list(exponents)
            remainder[i] -= 1
            answer = MomentPolynomial.zero()
            for j, count in enumerate(remainder):
                if not count:
                    continue
                covariance = self.B[i][j]
                if covariance is None:
                    raise RuntimeError(f"B[{i},{j}] requested before construction")
                paired = list(remainder)
                paired[j] -= 1
                answer = answer + count * covariance * self._r_wick(tuple(paired))
        self._r_wick_cache[exponents] = answer
        return answer

    def first_monomial(self, key: CoordinateMonomial) -> MomentPolynomial:
        if key in self._first_cache:
            return self._first_cache[key]
        if key.a or any(key.f) or any(key.y):
            raise ValueError("second-side variable leaked into first-side expectation")
        atom = MomentPolynomial.atom("X", key.x)
        answer = atom * self._r_wick(key.r)
        self._first_cache[key] = answer
        return answer

    def first(self, polynomial: CoordinatePolynomial) -> MomentPolynomial:
        answer = MomentPolynomial.zero()
        for key, coefficient in polynomial.terms:
            answer = answer + coefficient * self.first_monomial(key)
        return answer

    def _f_stein(self, f_exponents: tuple[int, ...], y: Exponent) -> MomentPolynomial:
        state = (f_exponents, y)
        if state in self._f_stein_cache:
            return self._f_stein_cache[state]
        if not any(f_exponents):
            answer = MomentPolynomial.atom("Y", y)
        else:
            i0 = next(index for index, count in enumerate(f_exponents) if count)
            i = i0 + 1  # actual F index
            remainder = list(f_exponents)
            remainder[i0] -= 1
            answer = MomentPolynomial.zero()
            # Pair F_i with another explicit fresh F_j.
            for j0, count in enumerate(remainder):
                if not count:
                    continue
                covariance = self.H[i][j0 + 1]
                if covariance is None:
                    raise RuntimeError(f"H[{i},{j0 + 1}] requested before construction")
                paired = list(remainder)
                paired[j0] -= 1
                answer = answer + count * covariance * self._f_stein(tuple(paired), y)
            # Or contract F_i with F_0 and differentiate the Y integrand.
            covariance0 = self.H[i][0]
            if covariance0 is None:
                raise RuntimeError(f"H[{i},0] requested before construction")
            for derivative, count in enumerate(y[:-1]):
                if not count:
                    continue
                shifted = list(y)
                shifted[derivative] -= 1
                shifted[derivative + 1] += 1
                answer = answer + count * covariance0 * self._f_stein(tuple(remainder), tuple(shifted))
        self._f_stein_cache[state] = answer
        return answer

    def second_monomial(self, key: CoordinateMonomial) -> MomentPolynomial:
        if key in self._second_cache:
            return self._second_cache[key]
        if any(key.r) or any(key.x):
            raise ValueError("first-side variable leaked into second-side expectation")
        a_moment = _standard_gaussian_moment(key.a)
        answer = a_moment * self._f_stein(key.f, key.y)
        self._second_cache[key] = answer
        return answer

    def second(self, polynomial: CoordinatePolynomial) -> MomentPolynomial:
        answer = MomentPolynomial.zero()
        for key, coefficient in polynomial.terms:
            answer = answer + coefficient * self.second_monomial(key)
        return answer


@dataclass(frozen=True)
class PopulationJetResult:
    derivatives: tuple[MomentPolynomial, ...]
    H: tuple[tuple[MomentPolynomial | None, ...], ...]
    B: tuple[tuple[MomentPolynomial | None, ...], ...]
    alpha: tuple[tuple[MomentPolynomial, ...], ...]
    beta: tuple[tuple[MomentPolynomial, ...], ...]
    coordinate_term_counts: tuple[tuple[str, int], ...]

    @property
    def A(self) -> MomentPolynomial:
        return self.derivatives[1]

    @property
    def B3(self) -> MomentPolynomial:
        return self.derivatives[3]

    @property
    def C(self) -> MomentPolynomial:
        return self.derivatives[5]


def compile_population_jet(
    order: int = 5,
    *,
    verbose: bool = False,
    q0: MomentPolynomial | int | Fraction = 1,
) -> PopulationJetResult:
    """Compile the exact response-aware population jet and peel all auxiliaries."""

    if not 0 <= order <= MAX_ORDER:
        raise ValueError("order must be between zero and five")
    peeler = Peeler()
    u = [CoordinatePolynomial.zero() for _ in range(order + 1)]
    h = [CoordinatePolynomial.zero() for _ in range(order + 1)]
    hp = [CoordinatePolynomial.zero() for _ in range(order + 1)]
    z = [CoordinatePolynomial.zero() for _ in range(order + 1)]
    g = [CoordinatePolynomial.zero() for _ in range(order + 1)]
    yp = [CoordinatePolynomial.zero() for _ in range(order + 1)]
    a = [CoordinatePolynomial.zero() for _ in range(order + 1)]
    b = [CoordinatePolynomial.zero() for _ in range(order + 1)]
    r = [CoordinatePolynomial.zero() for _ in range(order)]
    output = [MomentPolynomial.zero() for _ in range(order + 1)]
    alpha: list[list[MomentPolynomial]] = [[] for _ in range(order + 1)]
    beta: list[list[MomentPolynomial]] = [[] for _ in range(order)]
    counts: list[tuple[str, int]] = []

    a[0] = CoordinatePolynomial.variable("A")

    for k in range(order + 1):
        h[k] = _activation_coefficient("X", u, k, 0)
        if k < order:
            hp[k] = _activation_coefficient("X", u, k, 1)

        # Covariances of the fresh forward Gaussian family.
        for ell in range(k + 1):
            value = peeler.first(h[k] * h[ell])
            peeler.H[k][ell] = value
            peeler.H[ell][k] = value

        if k == 0:
            # z_0 is the base Gaussian F_0, encoded implicitly as the argument
            # of every Y_r factor.
            g[0] = CoordinatePolynomial.variable("Y", 0)
            if order:
                yp[0] = CoordinatePolynomial.variable("Y", 1)
        else:
            alpha[k] = [peeler.first(h[k].derivative("R", s)) for s in range(k)]
            zk = CoordinatePolynomial.variable("F", k)
            for s in range(k):
                zk = zk + b[s] * alpha[k][s]
            # Exact low-rank contribution from M_m h_{k-m}.
            for m in range(1, k + 1):
                for p in range(m):
                    q = m - 1 - p
                    inner = peeler.first(h[q] * h[k - m])
                    zk = zk + b[p] * inner * Fraction(1, m)
            z[k] = zk
            g[k] = _activation_coefficient("Y", z, k, 0)
            if k < order:
                yp[k] = _activation_coefficient("Y", z, k, 1)

        # The output coefficient is now fully defined.
        outk = CoordinatePolynomial.zero()
        for left in range(k + 1):
            outk = outk + a[left] * g[k - left]
        output[k] = peeler.second(outk)
        counts.extend(((f"h{k}", len(h[k].terms)), (f"z{k}", len(z[k].terms)), (f"g{k}", len(g[k].terms)), (f"out{k}", len(output[k].terms))))
        if verbose:
            print(k, counts[-4:])

        if k == order:
            break

        a[k + 1] = g[k].divide(k + 1)
        bk = CoordinatePolynomial.zero()
        for left in range(k + 1):
            bk = bk + a[left] * yp[k - left]
        b[k] = bk

        # Covariances of the fresh transpose Gaussian family.
        for ell in range(k + 1):
            value = peeler.second(b[k] * b[ell])
            peeler.B[k][ell] = value
            peeler.B[ell][k] = value

        beta[k] = [peeler.second(b[k].derivative("F", s)) for s in range(k + 1)]
        rk = CoordinatePolynomial.variable("R", k)
        for s in range(k + 1):
            rk = rk + h[s] * beta[k][s]
        # Exact low-rank contribution from M_m^T b_{k-m}.
        for m in range(1, k + 1):
            for p in range(m):
                q = m - 1 - p
                inner = peeler.second(b[p] * b[k - m])
                rk = rk + h[q] * inner * Fraction(1, m)
        r[k] = rk

        uk1 = CoordinatePolynomial.zero()
        for left in range(k + 1):
            uk1 = uk1 + hp[left] * r[k - left]
        u[k + 1] = uk1.divide(k + 1) * mp(q0)
        counts.extend(((f"b{k}", len(b[k].terms)), (f"r{k}", len(r[k].terms)), (f"u{k+1}", len(u[k + 1].terms))))

    derivatives = tuple(factorial(k) * output[k] for k in range(order + 1))
    return PopulationJetResult(
        derivatives=derivatives,
        H=tuple(tuple(row[: order + 1]) for row in peeler.H[: order + 1]),
        B=tuple(tuple(row[:order]) for row in peeler.B[:order]),
        alpha=tuple(tuple(row) for row in alpha),
        beta=tuple(tuple(row) for row in beta),
        coordinate_term_counts=tuple(counts),
    )


def gaussian_raw_moment(power: int, variance: Fraction) -> Fraction:
    return Fraction(_standard_gaussian_moment(power)) * variance ** (power // 2)


def polynomial_derivative(coefficients: tuple[Fraction, ...], order: int) -> tuple[Fraction, ...]:
    values = list(coefficients)
    for _ in range(order):
        values = [Fraction(k) * values[k] for k in range(1, len(values))]
        if not values:
            return (Fraction(0),)
    return tuple(values)


def activation_product_moment(
    exponent: Exponent,
    coefficients: tuple[Fraction, ...],
    variance: Fraction,
) -> Fraction:
    polynomial = [Fraction(1)]
    for derivative, multiplicity in enumerate(exponent):
        factor = polynomial_derivative(coefficients, derivative)
        for _ in range(multiplicity):
            product = [Fraction(0)] * (len(polynomial) + len(factor) - 1)
            for i, left in enumerate(polynomial):
                for j, right in enumerate(factor):
                    product[i + j] += left * right
            polynomial = product
    return sum((coefficient * gaussian_raw_moment(power, variance) for power, coefficient in enumerate(polynomial)), Fraction(0))


def evaluate_polynomial_activation(
    expression: MomentPolynomial,
    coefficients: Iterable[int | Fraction],
    *,
    q0: int | Fraction = 1,
) -> Fraction:
    """Exact evaluator for the layer-separated arbitrary-forward-variance form."""

    coefficients = tuple(Fraction(value) for value in coefficients)
    q0 = Fraction(q0)
    x20 = [0] * (MAX_DERIV + 1)
    x20[0] = 2
    q1 = activation_product_moment(tuple(x20), coefficients, q0)
    cache: dict[Atom, Fraction] = {}

    def atom_value(atom: Atom) -> Fraction:
        if atom not in cache:
            layer, exponent = atom
            variance = q0 if layer == "X" else q1
            cache[atom] = activation_product_moment(exponent, coefficients, variance)
        return cache[atom]

    answer = Fraction(0)
    for monomial, coefficient in expression.terms:
        value = coefficient
        for atom in monomial:
            value *= atom_value(atom)
        answer += value
    return answer


def format_atom(atom: Atom, *, max_derivative: int = 5) -> str:
    layer, exponent = atom
    digits = "".join(str(value) for value in exponent[: max_derivative + 1])
    return f"{layer}_{{{digits}}}"


def format_polynomial(expression: MomentPolynomial, *, max_derivative: int = 5) -> str:
    """Deterministic one-term-per-line canonical sparse representation."""

    lines: list[str] = []
    for monomial, coefficient in expression.terms:
        factors = " ".join(format_atom(atom, max_derivative=max_derivative) for atom in monomial) or "1"
        lines.append(f"{coefficient}\t{factors}")
    return "\n".join(lines)
