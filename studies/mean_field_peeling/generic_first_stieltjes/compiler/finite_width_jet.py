"""Independent finite-width feature-jet oracle for a generic smooth activation.

Arrays store ordinary Taylor coefficients, not derivatives.  This evaluator
does not perform a width extrapolation and therefore cannot certify a
mean-field formula.  It is a seedwise audit of the finite-width calculus and
an empirical regression gate for an emitted Gaussian normal form.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import factorial, sqrt
from typing import Callable

import numpy as np


DerivativeOracle = Callable[[int, np.ndarray], np.ndarray]


def _compose_coefficient(
    derivative: DerivativeOracle,
    series: np.ndarray,
    degree: int,
) -> np.ndarray:
    x0 = series[0]
    if degree == 0:
        return derivative(0, x0)
    if degree == 1:
        return derivative(1, x0) * series[1]
    if degree == 2:
        return derivative(1, x0) * series[2] + 0.5 * derivative(2, x0) * series[1] ** 2
    if degree == 3:
        return (
            derivative(1, x0) * series[3]
            + derivative(2, x0) * series[1] * series[2]
            + derivative(3, x0) * series[1] ** 3 / 6.0
        )
    raise NotImplementedError("the independent oracle is intentionally capped at order three")


def _compose_derivative_coefficient(
    derivative: DerivativeOracle,
    derivative_order: int,
    series: np.ndarray,
    degree: int,
) -> np.ndarray:
    shifted = lambda order, x: derivative(order + derivative_order, x)
    return _compose_coefficient(shifted, series, degree)


@dataclass(frozen=True)
class JetResult:
    ordinary_coefficients: np.ndarray

    @property
    def derivatives(self) -> np.ndarray:
        return np.asarray(
            [factorial(k) * value for k, value in enumerate(self.ordinary_coefficients)]
        )


def feature_jet(
    width: int,
    q0: float,
    activation_derivative: DerivativeOracle,
    seed: int,
    *,
    order: int = 3,
) -> JetResult:
    """Compute the exact finite-width Taylor jet through order three.

    ``q0`` is both the variance of the first preactivation and the induced
    first-layer optimizer metric.  This is the scalar reduction of raw
    first-layer weights for one input, not a freely chosen extra multiplier.
    """

    if width < 1:
        raise ValueError("width must be positive")
    if q0 < 0:
        raise ValueError("q0 must be nonnegative")
    if not 0 <= order <= 3:
        raise ValueError("order must lie between zero and three")

    rng = np.random.default_rng(seed)
    n = width
    inv_sqrt_n = 1.0 / sqrt(n)

    u = np.zeros((order + 1, n), dtype=np.float64)
    a = np.zeros_like(u)
    weights = np.zeros((order + 1, n, n), dtype=np.float64)
    h = np.zeros_like(u)
    hp = np.zeros_like(u)
    z = np.zeros_like(a)
    y = np.zeros_like(a)
    yp = np.zeros_like(a)
    xi = np.zeros_like(u)
    output = np.zeros(order + 1, dtype=np.float64)

    u[0] = sqrt(q0) * rng.standard_normal(n)
    weights[0] = rng.standard_normal((n, n))
    a[0] = rng.standard_normal(n)

    for k in range(order + 1):
        h[k] = _compose_coefficient(activation_derivative, u, k)

        zk = np.zeros(n)
        for left in range(k + 1):
            zk += weights[left] @ h[k - left]
        z[k] = inv_sqrt_n * zk
        y[k] = _compose_coefficient(activation_derivative, z, k)

        for left in range(k + 1):
            output[k] += np.dot(a[left], y[k - left]) / n

        # The terminal output coefficient uses phi through order three, but
        # its vector-field coefficient is unused.  Breaking here avoids an
        # artificial request for phi^(order+1).
        if k == order:
            break

        hp[k] = _compose_derivative_coefficient(activation_derivative, 1, u, k)
        yp[k] = _compose_derivative_coefficient(activation_derivative, 1, z, k)

        # xi = W^T (a * phi'(z)) / sqrt(n).
        xik = np.zeros(n)
        for w_degree in range(k + 1):
            remaining = k - w_degree
            source = np.zeros(n)
            for left in range(remaining + 1):
                source += a[left] * yp[remaining - left]
            xik += weights[w_degree].T @ source
        xi[k] = inv_sqrt_n * xik

        # a' = phi(z).
        a[k + 1] = y[k] / (k + 1)

        # W' = a phi'(z) phi(u)^T / sqrt(n).
        weight_rhs = np.zeros((n, n))
        for a_degree in range(k + 1):
            for p_degree in range(k - a_degree + 1):
                h_degree = k - a_degree - p_degree
                weight_rhs += np.outer(a[a_degree] * yp[p_degree], h[h_degree])
        weights[k + 1] = inv_sqrt_n * weight_rhs / (k + 1)

        # u' = q0 phi'(u) xi.
        u_rhs = np.zeros(n)
        for left in range(k + 1):
            u_rhs += hp[left] * xi[k - left]
        u[k + 1] = q0 * u_rhs / (k + 1)

    return JetResult(output)
