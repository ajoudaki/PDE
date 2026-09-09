"""Exact moving-feature Taylor jet through order five at arbitrary depth.

This is a finite-width oracle, not a Gaussian-normal-form compiler.  It
propagates ordinary power-series coefficients of the exact ODE

    theta_dot = n * grad_theta(c.T f)

and therefore retains every finite-width equality sector automatically.
The implementation is kept outside both symbolic derivation routes and is
used only after their coefficient artifacts have been frozen.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import factorial, sqrt
from typing import Callable

import numpy as np

from ...depth.model import DepthState, as_oracle_tuple, validate_problem


DerivativeOracle = Callable[[int, np.ndarray], np.ndarray]


def _series_product_coefficient(
    left: list[np.ndarray], right: list[np.ndarray], degree: int
) -> np.ndarray:
    answer = np.zeros_like(left[0], dtype=np.float64)
    for index in range(degree + 1):
        answer += left[index] * right[degree - index]
    return answer


def compose_coefficient(
    derivative: DerivativeOracle,
    series: np.ndarray,
    degree: int,
    *,
    derivative_shift: int = 0,
) -> np.ndarray:
    """Return the degree coefficient of phi^(shift)(series(t)) exactly."""

    base = series[0]
    perturbation = [np.zeros_like(base)] + [
        np.asarray(series[index], dtype=np.float64)
        for index in range(1, degree + 1)
    ]
    power = [np.ones_like(base)] + [
        np.zeros_like(base) for _ in range(degree)
    ]
    answer = np.zeros_like(base, dtype=np.float64)
    for exponent in range(degree + 1):
        answer += (
            np.asarray(derivative(derivative_shift + exponent, base))
            * power[degree]
            / factorial(exponent)
        )
        if exponent != degree:
            power = [
                _series_product_coefficient(power, perturbation, index)
                for index in range(degree + 1)
            ]
    return answer


@dataclass(frozen=True)
class DepthOrderFiveJet:
    """Ordinary coefficients of the scalarized output."""

    ordinary_coefficients: np.ndarray
    hidden_layers: int
    batch: int
    width: int

    @property
    def derivatives(self) -> np.ndarray:
        return np.asarray(
            [
                factorial(order) * coefficient
                for order, coefficient in enumerate(self.ordinary_coefficients)
            ],
            dtype=np.float64,
        )


def feature_ascent_jet(
    state: DepthState,
    input_gram: np.ndarray,
    channel: np.ndarray,
    activation_derivative,
    *,
    order: int = 5,
) -> DepthOrderFiveJet:
    """Compile the exact finite-width moving-flow jet through order five."""

    if not 0 <= order <= 5:
        raise ValueError("order must lie between zero and five")
    gram, channel = validate_problem(state, input_gram, channel)
    hidden_layers = state.hidden_layers
    oracles = as_oracle_tuple(activation_derivative, hidden_layers)
    n, batch = state.width, gram.shape[0]
    inv_sqrt_n = 1.0 / sqrt(n)

    z = [
        np.zeros((order + 1, n, batch), dtype=np.float64)
        for _ in range(hidden_layers)
    ]
    h = [np.zeros_like(value) for value in z]
    phi_prime = [np.zeros_like(value) for value in z]
    delta = [np.zeros_like(value) for value in z]
    backward = [np.zeros_like(value) for value in z]

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

    for degree in range(order + 1):
        # Exact forward convolution.
        h[0][degree] = compose_coefficient(oracles[0], z[0], degree)
        for layer in range(1, hidden_layers):
            coefficient = np.zeros((n, batch), dtype=np.float64)
            for left in range(degree + 1):
                coefficient += (
                    weights[layer - 1][left]
                    @ h[layer - 1][degree - left]
                )
            z[layer][degree] = inv_sqrt_n * coefficient
            h[layer][degree] = compose_coefficient(
                oracles[layer], z[layer], degree
            )

        for left in range(degree + 1):
            output[degree] += np.mean(
                readout[left] * (h[-1][degree - left] @ channel)
            )

        if degree == order:
            break

        # Exact reverse convolution.
        for layer in range(hidden_layers):
            phi_prime[layer][degree] = compose_coefficient(
                oracles[layer],
                z[layer],
                degree,
                derivative_shift=1,
            )

        top = np.zeros((n, batch), dtype=np.float64)
        for left in range(degree + 1):
            top += (
                readout[left, :, None]
                * phi_prime[-1][degree - left]
            )
        delta[-1][degree] = top * channel[None, :]

        for layer in range(hidden_layers - 2, -1, -1):
            propagated = np.zeros((n, batch), dtype=np.float64)
            for left in range(degree + 1):
                propagated += (
                    weights[layer][left].T
                    @ delta[layer + 1][degree - left]
                )
            backward[layer][degree] = inv_sqrt_n * propagated

            current = np.zeros((n, batch), dtype=np.float64)
            for left in range(degree + 1):
                current += (
                    phi_prime[layer][left]
                    * backward[layer][degree - left]
                )
            delta[layer][degree] = current

        # Integrate the current coefficient of the vector field.
        readout[degree + 1] = (
            h[-1][degree] @ channel
        ) / (degree + 1)
        for layer in range(1, hidden_layers):
            right_hand_side = np.zeros((n, n), dtype=np.float64)
            for left in range(degree + 1):
                right_hand_side += (
                    delta[layer][left]
                    @ h[layer - 1][degree - left].T
                )
            weights[layer - 1][degree + 1] = (
                inv_sqrt_n
                * right_hand_side
                / (degree + 1)
            )
        z[0][degree + 1] = (
            delta[0][degree] @ gram
        ) / (degree + 1)

    return DepthOrderFiveJet(
        ordinary_coefficients=output,
        hidden_layers=hidden_layers,
        batch=batch,
        width=n,
    )
