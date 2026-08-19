"""Independent raw-coordinate multivariate Taylor AD through order five.

This route does not evolve the feature ODE.  It expands the original network
in every active raw parameter, applies ``n grad(f).grad`` algebraically five
times, and (optionally) materializes the derivative tensors for the six-family
identity.  It is deliberately limited to tiny widths by its audit purpose.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import factorial, sqrt
from typing import Callable

import numpy as np

from .feature_flow import InitialState


DerivativeOracle = Callable[[int, np.ndarray], np.ndarray]
Exponent = tuple[int, ...]
Polynomial = dict[Exponent, float]


def _zero(dimension: int) -> Exponent:
    return (0,) * dimension


def _constant(value: float, dimension: int) -> Polynomial:
    return {} if value == 0.0 else {_zero(dimension): float(value)}


def _variable(value: float, dimension: int, index: int) -> Polynomial:
    out = _constant(value, dimension)
    exponent = [0] * dimension
    exponent[index] = 1
    out[tuple(exponent)] = 1.0
    return out


def _add(left: Polynomial, right: Polynomial) -> Polynomial:
    out = dict(left)
    for exponent, coefficient in right.items():
        value = out.get(exponent, 0.0) + coefficient
        if value == 0.0:
            out.pop(exponent, None)
        else:
            out[exponent] = value
    return out


def _scale(poly: Polynomial, scalar: float) -> Polynomial:
    if scalar == 0.0:
        return {}
    return {exponent: scalar * coefficient for exponent, coefficient in poly.items()}


def _multiply(left: Polynomial, right: Polynomial, max_degree: int) -> Polynomial:
    out: Polynomial = {}
    for alpha, left_coefficient in left.items():
        left_degree = sum(alpha)
        for beta, right_coefficient in right.items():
            if left_degree + sum(beta) > max_degree:
                continue
            exponent = tuple(a + b for a, b in zip(alpha, beta))
            out[exponent] = out.get(exponent, 0.0) + left_coefficient * right_coefficient
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient != 0.0}


def _differentiate(poly: Polynomial, coordinate: int) -> Polynomial:
    out: Polynomial = {}
    for exponent, coefficient in poly.items():
        power = exponent[coordinate]
        if power == 0:
            continue
        reduced = list(exponent)
        reduced[coordinate] -= 1
        key = tuple(reduced)
        out[key] = out.get(key, 0.0) + power * coefficient
    return out


def _compose(
    poly: Polynomial,
    derivative: DerivativeOracle,
    dimension: int,
    max_degree: int,
) -> Polynomial:
    origin = poly.get(_zero(dimension), 0.0)
    delta = dict(poly)
    delta.pop(_zero(dimension), None)
    power = _constant(1.0, dimension)
    out: Polynomial = {}
    scalar_origin = np.asarray(origin, dtype=np.float64)
    for degree in range(max_degree + 1):
        coefficient = float(derivative(degree, scalar_origin)) / factorial(degree)
        out = _add(out, _scale(power, coefficient))
        if degree != max_degree:
            power = _multiply(power, delta, max_degree)
    return out


def _value(poly: Polynomial, dimension: int) -> float:
    return float(poly.get(_zero(dimension), 0.0))


def _derivative_tensor(poly: Polynomial, dimension: int, rank: int) -> np.ndarray:
    shape = (dimension,) * rank
    out = np.empty(shape, dtype=np.float64)
    cache: dict[Exponent, float] = {}
    for indices in product(range(dimension), repeat=rank):
        exponent_list = [0] * dimension
        for index in indices:
            exponent_list[index] += 1
        exponent = tuple(exponent_list)
        if exponent not in cache:
            multiplier = 1
            for count in exponent:
                multiplier *= factorial(count)
            cache[exponent] = poly.get(exponent, 0.0) * multiplier
        out[indices] = cache[exponent]
    return out


@dataclass(frozen=True)
class SixFamilyContraction:
    fifth: float
    fourth_hp: float
    third_tpp: float
    third_h2p: float
    third_hp_hp: float
    h2p_square: float

    @property
    def weighted_families(self) -> tuple[float, ...]:
        return (
            2.0 * self.fifth,
            22.0 * self.fourth_hp,
            14.0 * self.third_tpp,
            30.0 * self.third_h2p,
            36.0 * self.third_hp_hp,
            16.0 * self.h2p_square,
        )

    @property
    def value(self) -> float:
        return float(sum(self.weighted_families))


@dataclass(frozen=True)
class RawADResult:
    derivatives: np.ndarray
    six_families: SixFamilyContraction


def _build_output_polynomial(
    state: InitialState,
    q0: float,
    activation_derivative: DerivativeOracle,
    max_degree: int,
) -> tuple[Polynomial, int]:
    n = state.width
    dimension = n + n * n + n
    variables: list[Polynomial] = []
    values = np.concatenate(
        (state.first_standard, state.middle_raw.ravel(), state.readout)
    )
    for index, value in enumerate(values):
        variables.append(_variable(float(value), dimension, index))

    cursor = 0
    first = variables[cursor : cursor + n]
    cursor += n
    middle = np.asarray(variables[cursor : cursor + n * n], dtype=object).reshape(n, n)
    cursor += n * n
    readout = variables[cursor : cursor + n]

    h: list[Polynomial] = []
    for first_coordinate in first:
        u = _scale(first_coordinate, sqrt(q0))
        h.append(_compose(u, activation_derivative, dimension, max_degree))

    y: list[Polynomial] = []
    for i in range(n):
        z: Polynomial = {}
        for j in range(n):
            z = _add(
                z,
                _scale(_multiply(middle[i, j], h[j], max_degree), 1.0 / sqrt(n)),
            )
        y.append(_compose(z, activation_derivative, dimension, max_degree))

    output: Polynomial = {}
    for i in range(n):
        output = _add(
            output, _scale(_multiply(readout[i], y[i], max_degree), 1.0 / n)
        )
    return output, dimension


def _operator_derivatives(f: Polynomial, dimension: int, width: int, order: int) -> np.ndarray:
    gradient_f = [_differentiate(f, coordinate) for coordinate in range(dimension)]
    current = f
    values = [_value(current, dimension)]
    for derivative_order in range(1, order + 1):
        target_degree = order - derivative_order
        next_poly: Polynomial = {}
        for coordinate in range(dimension):
            term = _multiply(
                gradient_f[coordinate],
                _differentiate(current, coordinate),
                target_degree,
            )
            next_poly = _add(next_poly, term)
        current = _scale(next_poly, float(width))
        values.append(_value(current, dimension))
    return np.asarray(values, dtype=np.float64)


def _six_family_contraction(f: Polynomial, dimension: int, width: int) -> SixFamilyContraction:
    p = _derivative_tensor(f, dimension, 1)
    hessian = _derivative_tensor(f, dimension, 2)
    third = _derivative_tensor(f, dimension, 3)
    fourth = _derivative_tensor(f, dimension, 4)
    fifth = _derivative_tensor(f, dimension, 5)
    hp = hessian @ p
    h2p = hessian @ hp
    tpp = np.einsum("ijk,j,k->i", third, p, p)
    scale = float(width**5)
    return SixFamilyContraction(
        fifth=scale * float(np.einsum("ijklm,i,j,k,l,m", fifth, p, p, p, p, p)),
        fourth_hp=scale * float(np.einsum("ijkl,i,j,k,l", fourth, hp, p, p, p)),
        third_tpp=scale * float(np.einsum("ijk,i,j,k", third, tpp, p, p)),
        third_h2p=scale * float(np.einsum("ijk,i,j,k", third, h2p, p, p)),
        third_hp_hp=scale * float(np.einsum("ijk,i,j,k", third, hp, hp, p)),
        h2p_square=scale * float(np.dot(h2p, h2p)),
    )


def raw_coordinate_jet(
    state: InitialState,
    q0: float,
    activation_derivative: DerivativeOracle,
    *,
    order: int = 5,
) -> RawADResult:
    """Apply D_n repeatedly to the original raw network polynomial jet."""

    if not 0 <= order <= 5:
        raise ValueError("order must lie between zero and five")
    if q0 < 0:
        raise ValueError("q0 must be nonnegative")
    if state.width > 2:
        raise ValueError("raw multivariate audit is intentionally limited to width <= 2")
    f, dimension = _build_output_polynomial(
        state, q0, activation_derivative, max_degree=5
    )
    derivatives = _operator_derivatives(f, dimension, state.width, order)
    families = _six_family_contraction(f, dimension, state.width)
    return RawADResult(derivatives=derivatives, six_families=families)
