"""Exact moving-feature Taylor jet through order five.

This is route A of the finite-width audit.  It evolves the exact feature
ascent ODE and stores ordinary Taylor coefficients (not derivatives).
"""

from __future__ import annotations

from dataclasses import dataclass
from math import factorial, sqrt
from typing import Callable

import numpy as np


DerivativeOracle = Callable[[int, np.ndarray], np.ndarray]


@dataclass(frozen=True)
class InitialState:
    """The active raw coordinates: standard first weight, W, and readout."""

    first_standard: np.ndarray
    middle_raw: np.ndarray
    readout: np.ndarray

    @property
    def width(self) -> int:
        return int(self.readout.size)


@dataclass(frozen=True)
class JetResult:
    ordinary_coefficients: np.ndarray

    @property
    def derivatives(self) -> np.ndarray:
        return np.asarray(
            [factorial(k) * value for k, value in enumerate(self.ordinary_coefficients)]
        )


def draw_state(width: int, seed: int) -> InitialState:
    if width < 1:
        raise ValueError("width must be positive")
    rng = np.random.default_rng(seed)
    return InitialState(
        first_standard=rng.standard_normal(width),
        middle_raw=rng.standard_normal((width, width)),
        readout=rng.standard_normal(width),
    )


def _series_product_coefficient(left: list[np.ndarray], right: list[np.ndarray], k: int):
    out = np.zeros_like(left[0], dtype=np.float64)
    for degree in range(k + 1):
        out += left[degree] * right[k - degree]
    return out


def compose_coefficient(
    derivative: DerivativeOracle,
    series: np.ndarray,
    degree: int,
    *,
    derivative_shift: int = 0,
) -> np.ndarray:
    """Coefficient of t**degree in phi^(shift)(series(t))."""

    x0 = series[0]
    delta = [np.zeros_like(x0, dtype=np.float64)] + [series[k] for k in range(1, degree + 1)]
    power = [np.ones_like(x0, dtype=np.float64)] + [
        np.zeros_like(x0, dtype=np.float64) for _ in range(degree)
    ]
    out = np.zeros_like(x0, dtype=np.float64)
    for exponent in range(degree + 1):
        out += derivative(derivative_shift + exponent, x0) * power[degree] / factorial(exponent)
        if exponent != degree:
            power = [
                _series_product_coefficient(power, delta, k) for k in range(degree + 1)
            ]
    return out


def feature_flow_jet(
    state: InitialState,
    q0: float,
    activation_derivative: DerivativeOracle,
    *,
    order: int = 5,
) -> JetResult:
    """Evaluate the exact finite-width flow jet for a fixed initialization."""

    if q0 < 0:
        raise ValueError("q0 must be nonnegative")
    if not 0 <= order <= 5:
        raise ValueError("order must lie between zero and five")
    n = state.width
    if state.first_standard.shape != (n,) or state.middle_raw.shape != (n, n):
        raise ValueError("inconsistent state shapes")
    inv_sqrt_n = 1.0 / sqrt(n)

    u = np.zeros((order + 1, n), dtype=np.float64)
    a = np.zeros_like(u)
    weights = np.zeros((order + 1, n, n), dtype=np.float64)
    h = np.zeros_like(u)
    hp = np.zeros_like(u)
    z = np.zeros_like(a)
    y = np.zeros_like(a)
    yp = np.zeros_like(a)
    backward = np.zeros_like(u)
    output = np.zeros(order + 1, dtype=np.float64)

    u[0] = sqrt(q0) * state.first_standard
    weights[0] = state.middle_raw
    a[0] = state.readout

    for k in range(order + 1):
        h[k] = compose_coefficient(activation_derivative, u, k)

        for left in range(k + 1):
            z[k] += inv_sqrt_n * (weights[left] @ h[k - left])
        y[k] = compose_coefficient(activation_derivative, z, k)

        for left in range(k + 1):
            output[k] += np.dot(a[left], y[k - left]) / n

        if k == order:
            break

        hp[k] = compose_coefficient(
            activation_derivative, u, k, derivative_shift=1
        )
        yp[k] = compose_coefficient(
            activation_derivative, z, k, derivative_shift=1
        )

        # backward = W^T (a phi'(z)) / sqrt(n), with full convolutions.
        for weight_degree in range(k + 1):
            source_degree = k - weight_degree
            source = np.zeros(n, dtype=np.float64)
            for left in range(source_degree + 1):
                source += a[left] * yp[source_degree - left]
            backward[k] += inv_sqrt_n * (weights[weight_degree].T @ source)

        a[k + 1] = y[k] / (k + 1)

        weight_rhs = np.zeros((n, n), dtype=np.float64)
        for a_degree in range(k + 1):
            for p_degree in range(k - a_degree + 1):
                h_degree = k - a_degree - p_degree
                weight_rhs += np.outer(
                    a[a_degree] * yp[p_degree], h[h_degree]
                )
        weights[k + 1] = inv_sqrt_n * weight_rhs / (k + 1)

        u_rhs = np.zeros(n, dtype=np.float64)
        for left in range(k + 1):
            u_rhs += hp[left] * backward[k - left]
        u[k + 1] = q0 * u_rhs / (k + 1)

    return JetResult(output)
