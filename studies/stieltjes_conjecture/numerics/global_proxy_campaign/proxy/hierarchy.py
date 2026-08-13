"""Conditional Stieltjes rational hierarchy built one exact moment at a time."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import log
from typing import Iterable, Literal, Sequence

import numpy as np
import sympy as sp

from .exact_series import as_fraction, reciprocal


Side = Literal["lower", "upper"]


class MomentConeError(ValueError):
    """Raised when a supplied prefix cannot define a positive S-fraction."""


def stieltjes_s_fraction(
    moments: Sequence[Fraction | int | str | float],
) -> tuple[Fraction, ...]:
    """Return exact S-fraction coefficients ``beta_1,...``.

    For ``R(x)=sum (-1)^r mu_r x^r`` the convention is

    ``R(x)=mu_0/(1+beta_1*x/(1+beta_2*x/(...)))``.

    A strictly positive Stieltjes prefix produces positive beta coefficients.
    The identically zero measure is represented by an empty tuple.  Signed or
    inconsistent inputs fail closed rather than silently yielding a rational
    curve with no Stieltjes ordering theorem.
    """
    mu = tuple(as_fraction(value) for value in moments)
    if not mu:
        return ()
    if mu[0] < 0:
        raise MomentConeError("mu_0 is negative")
    if mu[0] == 0:
        if any(mu[1:]):
            raise MomentConeError("zero mass with nonzero higher moments")
        return ()

    tail = [(((-1) ** r) * value) / mu[0] for r, value in enumerate(mu)]
    betas: list[Fraction] = []
    while len(tail) > 1:
        inverse = reciprocal(tail, len(tail) - 1)
        quotient = inverse[1:]
        beta = quotient[0]
        if beta < 0:
            raise MomentConeError(f"negative S-fraction coefficient beta_{len(betas)+1}")
        if beta == 0:
            if any(quotient[1:]):
                raise MomentConeError("zero S-fraction coefficient with nonzero tail")
            break
        betas.append(beta)
        tail = [value / beta for value in quotient]
    return tuple(betas)


def _continued_fraction_value(mu0: float, betas: Sequence[float], x: float) -> float:
    denominator = 1.0
    for beta in reversed(betas):
        denominator = 1.0 + beta * x / denominator
    return mu0 / denominator


def _continued_fraction_exact(
    mu0: Fraction, betas: Sequence[Fraction], x: Fraction
) -> Fraction:
    denominator = Fraction(1)
    for beta in reversed(betas):
        denominator = 1 + beta * x / denominator
    return mu0 / denominator


@dataclass(frozen=True)
class KernelApproximation:
    """One conditional rational kernel approximation."""

    name: str
    baseline: Fraction
    information_moments: int
    side: Side
    mu0: Fraction | None
    betas: tuple[Fraction, ...] = ()

    def resolvent(self, x: float) -> float:
        if x < 0:
            raise ValueError("the Stieltjes proxy is restricted to x >= 0")
        if self.mu0 is None:
            return 0.0
        return _continued_fraction_value(
            float(self.mu0), tuple(float(beta) for beta in self.betas), float(x)
        )

    def resolvent_exact(self, x: Fraction | int | str) -> Fraction:
        xq = as_fraction(x)
        if xq < 0:
            raise ValueError("the Stieltjes proxy is restricted to x >= 0")
        if self.mu0 is None:
            return Fraction(0)
        return _continued_fraction_exact(self.mu0, self.betas, xq)

    def kernel(self, y: float) -> float:
        return float(self.baseline) + y * y * self.resolvent(y * y)

    def kernel_exact(self, y: Fraction | int | str) -> Fraction:
        yq = as_fraction(y)
        return self.baseline + yq * yq * self.resolvent_exact(yq * yq)


@dataclass(frozen=True)
class TaylorKernelApproximation:
    """Equal-information raw Taylor control; it carries no global ordering."""

    baseline: Fraction
    moments: tuple[Fraction, ...]

    @property
    def information_moments(self) -> int:
        return len(self.moments)

    @property
    def name(self) -> str:
        return f"taylor_{len(self.moments)}moments_unordered"

    def kernel(self, y: float) -> float:
        x = y * y
        resolvent = sum(((-1.0) ** r) * float(mu) * x**r
                        for r, mu in enumerate(self.moments))
        return float(self.baseline) + x * resolvent


@dataclass(frozen=True)
class KernelBracket:
    """Best lower/upper pair available after a given moment prefix."""

    information_moments: int
    lower: KernelApproximation
    upper: KernelApproximation

    def log_width(self, y: float) -> float:
        lower = self.lower.kernel(y)
        upper = self.upper.kernel(y)
        if lower <= 0 or upper <= 0:
            raise ValueError("logarithmic width requires positive kernels")
        return log(upper / lower)


def build_kernel_hierarchy(
    baseline: Fraction | int | str | float,
    moments: Sequence[Fraction | int | str | float],
) -> tuple[KernelApproximation, ...]:
    """Build NTK and every one-moment-at-a-time S-fraction convergent."""
    baseline_q = as_fraction(baseline)
    if baseline_q <= 0:
        raise ValueError("kernel baseline must be positive")
    mu = tuple(as_fraction(value) for value in moments)
    ntk = KernelApproximation(
        name="ntk_0moments_lower",
        baseline=baseline_q,
        information_moments=0,
        side="lower",
        mu0=None,
    )
    if not mu or (mu[0] == 0 and not any(mu[1:])):
        return (ntk,)
    betas = stieltjes_s_fraction(mu)
    levels: list[KernelApproximation] = [ntk]
    for count in range(1, len(mu) + 1):
        needed_betas = count - 1
        if needed_betas > len(betas):
            # A terminating finite-support fraction is already exact; further
            # redundant moments do not define a new level.
            break
        side: Side = "upper" if count % 2 else "lower"
        if side == "upper":
            nodes = (count + 1) // 2
            name = f"zero_radau_{nodes}node_{count}moments_upper"
        else:
            nodes = count // 2
            name = f"gauss_{nodes}node_{count}moments_lower"
        levels.append(KernelApproximation(
            name=name,
            baseline=baseline_q,
            information_moments=count,
            side=side,
            mu0=mu[0],
            betas=betas[:needed_betas],
        ))
    return tuple(levels)


def build_kernel_brackets(
    baseline: Fraction | int | str | float,
    moments: Sequence[Fraction | int | str | float],
) -> tuple[KernelBracket, ...]:
    """Return the nested conditional envelope after every usable moment."""
    hierarchy = build_kernel_hierarchy(baseline, moments)
    lower = hierarchy[0]
    upper: KernelApproximation | None = None
    brackets: list[KernelBracket] = []
    for approximation in hierarchy[1:]:
        if approximation.side == "lower":
            lower = approximation
        else:
            upper = approximation
        if upper is not None:
            brackets.append(KernelBracket(
                information_moments=approximation.information_moments,
                lower=lower,
                upper=upper,
            ))
    return tuple(brackets)


def build_taylor_controls(
    baseline: Fraction | int | str | float,
    moments: Sequence[Fraction | int | str | float],
) -> tuple[TaylorKernelApproximation, ...]:
    baseline_q = as_fraction(baseline)
    mu = tuple(as_fraction(value) for value in moments)
    return tuple(
        TaylorKernelApproximation(baseline_q, mu[:count])
        for count in range(1, len(mu) + 1)
    )


@dataclass(frozen=True)
class AtomicQuadrature:
    """Numerical nodes/weights plus the exact monic node polynomial."""

    kind: Literal["gauss", "zero_radau"]
    nodes: tuple[float, ...]
    weights: tuple[float, ...]
    monic_polynomial_ascending: tuple[Fraction, ...]

    def resolvent(self, x: float) -> float:
        return sum(weight / (1.0 + node * x)
                   for node, weight in zip(self.nodes, self.weights, strict=True))


def _sympy_rational(value: Fraction) -> sp.Rational:
    return sp.Rational(value.numerator, value.denominator)


def gaussian_quadrature(
    moments: Sequence[Fraction | int | str | float],
) -> AtomicQuadrature:
    """Construct the Gaussian rule from exactly ``2n`` moments."""
    mu = tuple(as_fraction(value) for value in moments)
    if not mu or len(mu) % 2:
        raise ValueError("Gaussian quadrature requires exactly 2n moments")
    n = len(mu) // 2
    hankel = sp.Matrix([
        [_sympy_rational(mu[i + j]) for j in range(n)]
        for i in range(n)
    ])
    right = sp.Matrix([-_sympy_rational(mu[i + n]) for i in range(n)])
    try:
        lower = hankel.inv() * right
    except Exception as exc:  # pragma: no cover - SymPy exception class varies
        raise MomentConeError("singular Gaussian moment matrix") from exc
    coefficients = tuple(
        Fraction(int(value.p), int(value.q)) for value in lower
    ) + (Fraction(1),)
    variable = sp.symbols("t")
    polynomial = sum(_sympy_rational(value) * variable**power
                     for power, value in enumerate(coefficients))
    roots = sp.nroots(polynomial, n=50, maxsteps=200)
    nodes: list[float] = []
    for root in roots:
        real, imag = float(sp.re(root)), float(sp.im(root))
        if abs(imag) > 1e-30:
            raise MomentConeError("Gaussian node polynomial has a nonreal root")
        if real < -1e-14:
            raise MomentConeError("Gaussian node polynomial has a negative root")
        nodes.append(max(0.0, real))
    nodes.sort()
    vandermonde = np.array([[node**power for node in nodes]
                            for power in range(n)], dtype=np.float64)
    weights = np.linalg.solve(vandermonde, np.array([float(value) for value in mu[:n]]))
    if np.min(weights) < -1e-12:
        raise MomentConeError("Gaussian quadrature has a negative weight")
    return AtomicQuadrature(
        kind="gauss",
        nodes=tuple(nodes),
        weights=tuple(float(max(0.0, value)) for value in weights),
        monic_polynomial_ascending=coefficients,
    )


def zero_radau_quadrature(
    moments: Sequence[Fraction | int | str | float],
) -> AtomicQuadrature:
    """Construct the zero-Radau rule from exactly ``2n+1`` moments."""
    mu = tuple(as_fraction(value) for value in moments)
    if not mu or len(mu) % 2 != 1:
        raise ValueError("zero-Radau quadrature requires exactly 2n+1 moments")
    if len(mu) == 1:
        return AtomicQuadrature(
            kind="zero_radau",
            nodes=(0.0,),
            weights=(float(mu[0]),),
            monic_polynomial_ascending=(Fraction(0), Fraction(1)),
        )
    shifted = gaussian_quadrature(mu[1:])
    if any(node <= 0 for node in shifted.nodes):
        raise MomentConeError("zero-Radau positive nodes must be strictly positive")
    positive_weights = tuple(weight / node for node, weight in zip(
        shifted.nodes, shifted.weights, strict=True
    ))
    zero_weight = float(mu[0]) - sum(positive_weights)
    if zero_weight < -1e-11:
        raise MomentConeError("zero-Radau rule has a negative zero-node weight")
    coefficients = (Fraction(0),) + shifted.monic_polynomial_ascending
    return AtomicQuadrature(
        kind="zero_radau",
        nodes=(0.0,) + shifted.nodes,
        weights=(max(0.0, zero_weight),) + positive_weights,
        monic_polynomial_ascending=coefficients,
    )


def quadrature_for_prefix(
    moments: Sequence[Fraction | int | str | float],
) -> AtomicQuadrature:
    """Return the Gaussian/even or zero-Radau/odd prefix rule."""
    return (zero_radau_quadrature(moments) if len(moments) % 2
            else gaussian_quadrature(moments))


def quadrature_moment_errors(
    rule: AtomicQuadrature,
    moments: Iterable[Fraction | int | str | float],
) -> tuple[float, ...]:
    return tuple(
        sum(weight * node**order for node, weight in zip(
            rule.nodes, rule.weights, strict=True
        )) - float(as_fraction(target))
        for order, target in enumerate(moments)
    )
