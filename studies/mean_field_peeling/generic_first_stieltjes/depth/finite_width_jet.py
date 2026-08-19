"""Exact order-three ordinary-series compiler for arbitrary fixed depth.

The compiled curve is the nonlinear feature-ascent ODE

    theta_dot(t) = n * grad_theta g_c(theta(t)),
    g_c(theta) = c.T @ f(theta),

not the frozen straight line through the initial gradient.  Consequently the
returned derivatives are ``D_c^k g_c`` for the variable-coefficient operator
``D_c = n grad(g_c).grad``.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import factorial, sqrt
from typing import Callable

import numpy as np

from .model import DepthState, as_oracle_tuple, validate_problem


DerivativeOracle = Callable[[int, np.ndarray], np.ndarray]


def _compose(
    derivative: DerivativeOracle,
    series: np.ndarray,
    degree: int,
    *,
    derivative_order: int = 0,
) -> np.ndarray:
    """Coefficient ``[t^degree] phi^(derivative_order)(series(t))``."""

    evaluate = lambda order, x: derivative(order + derivative_order, x)
    x0 = series[0]
    if degree == 0:
        return np.asarray(evaluate(0, x0), dtype=np.float64)
    if degree == 1:
        return evaluate(1, x0) * series[1]
    if degree == 2:
        return evaluate(1, x0) * series[2] + 0.5 * evaluate(2, x0) * series[1] ** 2
    if degree == 3:
        return (
            evaluate(1, x0) * series[3]
            + evaluate(2, x0) * series[1] * series[2]
            + evaluate(3, x0) * series[1] ** 3 / 6.0
        )
    raise NotImplementedError("this exact compiler is capped at order three")


@dataclass(frozen=True)
class DepthJet:
    """Ordinary coefficients and diagnostics of ``g_c(theta(t))``."""

    ordinary_coefficients: np.ndarray
    hidden_layers: int
    batch: int
    width: int

    @property
    def derivatives(self) -> np.ndarray:
        return np.asarray(
            [factorial(k) * value for k, value in enumerate(self.ordinary_coefficients)],
            dtype=np.float64,
        )


def feature_ascent_jet(
    state: DepthState,
    input_gram: np.ndarray,
    channel: np.ndarray,
    activation_derivative,
    *,
    order: int = 3,
) -> DepthJet:
    """Compile the exact finite-width feature-ascent jet through order three.

    The activation argument may be one derivative oracle shared by all hidden
    layers or a sequence of ``H`` layer-specific oracles.  An oracle accepts
    ``(derivative_order, ndarray)`` and returns the corresponding derivative.
    No nonsingularity assumption is imposed on ``input_gram``.
    """

    if not 0 <= order <= 3:
        raise ValueError("order must lie between zero and three")
    gram, channel = validate_problem(state, input_gram, channel)
    hidden_layers = state.hidden_layers
    oracles = as_oracle_tuple(activation_derivative, hidden_layers)
    n, batch = state.width, gram.shape[0]
    inv_sqrt_n = 1.0 / sqrt(n)

    # z[l] and h[l] use zero-based Python layer indices l=0,...,H-1.
    z = [np.zeros((order + 1, n, batch), dtype=np.float64) for _ in range(hidden_layers)]
    h = [np.zeros_like(z_l) for z_l in z]
    phi_prime = [np.zeros_like(z_l) for z_l in z]
    delta = [np.zeros_like(z_l) for z_l in z]
    backward = [np.zeros_like(z_l) for z_l in z]

    readout = np.zeros((order + 1, n), dtype=np.float64)
    weights = [
        np.zeros((order + 1, n, n), dtype=np.float64)
        for _ in range(hidden_layers - 1)
    ]
    output = np.zeros(order + 1, dtype=np.float64)

    z[0][0] = state.first_preactivation
    readout[0] = state.readout
    for layer, initial_weight in enumerate(state.hidden_weights):
        weights[layer][0] = initial_weight

    for k in range(order + 1):
        # Forward pass at ordinary-series degree k.
        h[0][k] = _compose(oracles[0], z[0], k)
        for layer in range(1, hidden_layers):
            coefficient = np.zeros((n, batch), dtype=np.float64)
            for left in range(k + 1):
                coefficient += weights[layer - 1][left] @ h[layer - 1][k - left]
            z[layer][k] = inv_sqrt_n * coefficient
            h[layer][k] = _compose(oracles[layer], z[layer], k)

        for left in range(k + 1):
            output[k] += np.mean(
                readout[left] * (h[-1][k - left] @ channel)
            )

        if k == order:
            break

        # Reverse pass at degree k.  Only degrees through order-1 are needed
        # to integrate parameter coefficients through the requested order.
        for layer in range(hidden_layers):
            phi_prime[layer][k] = _compose(
                oracles[layer], z[layer], k, derivative_order=1
            )

        top = np.zeros((n, batch), dtype=np.float64)
        for left in range(k + 1):
            top += readout[left, :, None] * phi_prime[-1][k - left]
        delta[-1][k] = top * channel[None, :]

        for layer in range(hidden_layers - 2, -1, -1):
            propagated = np.zeros((n, batch), dtype=np.float64)
            for left in range(k + 1):
                propagated += (
                    weights[layer][left].T @ delta[layer + 1][k - left]
                )
            backward[layer][k] = inv_sqrt_n * propagated

            current_delta = np.zeros((n, batch), dtype=np.float64)
            for left in range(k + 1):
                current_delta += (
                    phi_prime[layer][left] * backward[layer][k - left]
                )
            delta[layer][k] = current_delta

        # Integrate [t^k] theta_dot to [t^(k+1)] theta.
        readout[k + 1] = (h[-1][k] @ channel) / (k + 1)
        for layer in range(1, hidden_layers):
            rhs = np.zeros((n, n), dtype=np.float64)
            for left in range(k + 1):
                rhs += delta[layer][left] @ h[layer - 1][k - left].T
            weights[layer - 1][k + 1] = inv_sqrt_n * rhs / (k + 1)
        z[0][k + 1] = (delta[0][k] @ gram) / (k + 1)

    return DepthJet(output, hidden_layers, batch, n)
