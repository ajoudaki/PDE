"""Two exact finite-width hidden-feature jet oracles through order four.

``coefficient_hidden_jet`` uses ordinary power-series coefficients and
convolution.  ``derivative_hidden_jet`` uses ordinary derivatives, binomial
product rules, and explicit Bell/Faà-di-Bruno composition.  Their seedwise
agreement is a finite-width differentiation gate; neither uses the population
``Gamma_04`` recurrence.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb, factorial, sqrt
from typing import Callable

import numpy as np

from ...depth.model import DepthState, as_oracle_tuple, validate_problem


DerivativeOracle = Callable[[int, np.ndarray], np.ndarray]


@dataclass(frozen=True)
class HiddenJet:
    derivatives: tuple[np.ndarray, ...]
    hidden_layers: int
    width: int
    batch: int

    def gamma(self, layer: int, left: int, right: int) -> float:
        values = self.derivatives[layer - 1]
        return float(np.mean(values[left] * values[right]))

    def q_derivative(self, layer: int, order: int) -> float:
        return sum(
            comb(order, left) * self.gamma(layer, left, order - left)
            for left in range(order + 1)
        )


def _series_product(left: list[np.ndarray], right: list[np.ndarray], k: int):
    answer = np.zeros_like(left[0], dtype=np.float64)
    for j in range(k + 1):
        answer += left[j] * right[k - j]
    return answer


def _compose_coefficient(
    oracle: DerivativeOracle,
    z: np.ndarray,
    degree: int,
    *,
    derivative_shift: int = 0,
) -> np.ndarray:
    base = z[0]
    perturbation = [np.zeros_like(base)] + [z[index] for index in range(1, degree + 1)]
    power = [np.ones_like(base)] + [np.zeros_like(base) for _ in range(degree)]
    answer = np.zeros_like(base, dtype=np.float64)
    for exponent in range(degree + 1):
        answer += oracle(derivative_shift + exponent, base) * power[degree] / factorial(exponent)
        if exponent != degree:
            power = [
                _series_product(power, perturbation, index)
                for index in range(degree + 1)
            ]
    return answer


def coefficient_hidden_jet(
    state: DepthState,
    input_gram: np.ndarray,
    channel: np.ndarray,
    activation_derivative,
    *,
    order: int = 4,
) -> HiddenJet:
    """Exact coefficient-convolution implementation."""

    if not 0 <= order <= 4:
        raise ValueError(order)
    gram, channel = validate_problem(state, input_gram, channel)
    hcount, n, batch = state.hidden_layers, state.width, gram.shape[0]
    oracles = as_oracle_tuple(activation_derivative, hcount)
    inv_sqrt_n = 1.0 / sqrt(n)

    z = [np.zeros((order + 1, n, batch)) for _ in range(hcount)]
    x = [np.zeros_like(value) for value in z]
    hp = [np.zeros_like(value) for value in z]
    delta = [np.zeros_like(value) for value in z]
    backward = [np.zeros_like(value) for value in z]
    readout = np.zeros((order + 1, n))
    weights = [np.zeros((order + 1, n, n)) for _ in range(hcount - 1)]

    z[0][0] = state.first_preactivation
    readout[0] = state.readout
    for layer, initial in enumerate(state.hidden_weights):
        weights[layer][0] = initial

    for degree in range(order + 1):
        x[0][degree] = _compose_coefficient(oracles[0], z[0], degree)
        for layer in range(1, hcount):
            for left in range(degree + 1):
                z[layer][degree] += (
                    weights[layer - 1][left] @ x[layer - 1][degree - left]
                ) * inv_sqrt_n
            x[layer][degree] = _compose_coefficient(oracles[layer], z[layer], degree)
        if degree == order:
            break

        for layer in range(hcount):
            hp[layer][degree] = _compose_coefficient(
                oracles[layer], z[layer], degree, derivative_shift=1
            )
        for left in range(degree + 1):
            delta[-1][degree] += (
                readout[left, :, None] * hp[-1][degree - left]
            ) * channel[None, :]
        for layer in range(hcount - 2, -1, -1):
            for left in range(degree + 1):
                backward[layer][degree] += (
                    weights[layer][left].T @ delta[layer + 1][degree - left]
                ) * inv_sqrt_n
            for left in range(degree + 1):
                delta[layer][degree] += hp[layer][left] * backward[layer][degree - left]

        readout[degree + 1] = (x[-1][degree] @ channel) / (degree + 1)
        for layer in range(1, hcount):
            for left in range(degree + 1):
                weights[layer - 1][degree + 1] += (
                    delta[layer][left] @ x[layer - 1][degree - left].T
                ) * inv_sqrt_n / (degree + 1)
        z[0][degree + 1] = (delta[0][degree] @ gram) / (degree + 1)

    derivatives = tuple(
        np.asarray(
            [factorial(degree) * value[degree] for degree in range(order + 1)]
        )
        for value in x
    )
    return HiddenJet(derivatives, hcount, n, batch)


def _compose_derivative(
    oracle: DerivativeOracle,
    z: np.ndarray,
    degree: int,
    *,
    derivative_shift: int = 0,
) -> np.ndarray:
    """Explicit Bell-polynomial composition through derivative four."""

    base = z[0]
    if degree == 0:
        return oracle(derivative_shift, base)
    if degree == 1:
        return oracle(derivative_shift + 1, base) * z[1]
    if degree == 2:
        return (
            oracle(derivative_shift + 2, base) * z[1] ** 2
            + oracle(derivative_shift + 1, base) * z[2]
        )
    if degree == 3:
        return (
            oracle(derivative_shift + 3, base) * z[1] ** 3
            + 3 * oracle(derivative_shift + 2, base) * z[1] * z[2]
            + oracle(derivative_shift + 1, base) * z[3]
        )
    if degree == 4:
        return (
            oracle(derivative_shift + 4, base) * z[1] ** 4
            + 6 * oracle(derivative_shift + 3, base) * z[1] ** 2 * z[2]
            + 3 * oracle(derivative_shift + 2, base) * z[2] ** 2
            + 4 * oracle(derivative_shift + 2, base) * z[1] * z[3]
            + oracle(derivative_shift + 1, base) * z[4]
        )
    raise ValueError(degree)


def derivative_hidden_jet(
    state: DepthState,
    input_gram: np.ndarray,
    channel: np.ndarray,
    activation_derivative,
    *,
    order: int = 4,
) -> HiddenJet:
    """Independent ordinary-derivative/binomial implementation."""

    if not 0 <= order <= 4:
        raise ValueError(order)
    gram, channel = validate_problem(state, input_gram, channel)
    hcount, n, batch = state.hidden_layers, state.width, gram.shape[0]
    oracles = as_oracle_tuple(activation_derivative, hcount)
    inv_sqrt_n = 1.0 / sqrt(n)

    z = [np.zeros((order + 1, n, batch)) for _ in range(hcount)]
    x = [np.zeros_like(value) for value in z]
    hp = [np.zeros_like(value) for value in z]
    delta = [np.zeros_like(value) for value in z]
    backward = [np.zeros_like(value) for value in z]
    readout = np.zeros((order + 1, n))
    weights = [np.zeros((order + 1, n, n)) for _ in range(hcount - 1)]

    z[0][0] = state.first_preactivation
    readout[0] = state.readout
    for layer, initial in enumerate(state.hidden_weights):
        weights[layer][0] = initial

    for degree in range(order + 1):
        x[0][degree] = _compose_derivative(oracles[0], z[0], degree)
        for layer in range(1, hcount):
            for left in range(degree + 1):
                z[layer][degree] += (
                    comb(degree, left)
                    * weights[layer - 1][left]
                    @ x[layer - 1][degree - left]
                    * inv_sqrt_n
                )
            x[layer][degree] = _compose_derivative(oracles[layer], z[layer], degree)
        if degree == order:
            break

        for layer in range(hcount):
            hp[layer][degree] = _compose_derivative(
                oracles[layer], z[layer], degree, derivative_shift=1
            )
        for left in range(degree + 1):
            delta[-1][degree] += (
                comb(degree, left)
                * readout[left, :, None]
                * hp[-1][degree - left]
                * channel[None, :]
            )
        for layer in range(hcount - 2, -1, -1):
            for left in range(degree + 1):
                backward[layer][degree] += (
                    comb(degree, left)
                    * weights[layer][left].T
                    @ delta[layer + 1][degree - left]
                    * inv_sqrt_n
                )
            for left in range(degree + 1):
                delta[layer][degree] += (
                    comb(degree, left)
                    * hp[layer][left]
                    * backward[layer][degree - left]
                )

        readout[degree + 1] = x[-1][degree] @ channel
        for layer in range(1, hcount):
            for left in range(degree + 1):
                weights[layer - 1][degree + 1] += (
                    comb(degree, left)
                    * delta[layer][left]
                    @ x[layer - 1][degree - left].T
                    * inv_sqrt_n
                )
        z[0][degree + 1] = delta[0][degree] @ gram

    return HiddenJet(tuple(np.asarray(value) for value in x), hcount, n, batch)


def polynomial_oracle(coefficients) -> DerivativeOracle:
    coefficients = np.asarray(coefficients, dtype=np.float64)

    def oracle(order: int, value: np.ndarray) -> np.ndarray:
        current = coefficients.copy()
        for _ in range(order):
            current = np.arange(1, current.size) * current[1:]
        answer = np.zeros_like(value, dtype=np.float64)
        for coefficient in current[::-1]:
            answer = answer * value + coefficient
        return answer

    return oracle
