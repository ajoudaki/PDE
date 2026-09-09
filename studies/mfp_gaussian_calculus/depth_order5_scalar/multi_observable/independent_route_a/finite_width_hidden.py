"""Exact finite-width hidden-activation jets and an independent raw-AD audit.

The ordinary-series route integrates the feature-ascent ODE coefficient by
coefficient.  The raw route instead Taylor-expands the original network in
all parameters and applies ``D=n grad(f).grad`` algebraically.  Agreement at
tiny widths audits the finite-width layer product-rule schedule without using
the population Wick--Stein contraction.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import factorial, sqrt
from typing import Callable

import numpy as np

from ....depth.model import DepthState, as_oracle_tuple, validate_problem
from ....depth_order5.common.finite_width_jet import compose_coefficient
from ....order5.finite_width import raw_ad


DerivativeOracle = Callable[[int, np.ndarray], np.ndarray]


@dataclass(frozen=True)
class HiddenJet:
    feature_coefficients: tuple[np.ndarray, ...]
    gamma: tuple[np.ndarray, ...]
    q_derivatives: np.ndarray
    output_derivatives: np.ndarray


def feature_ascent_hidden_jet(
    state: DepthState,
    input_gram: np.ndarray,
    channel: np.ndarray,
    activation_derivative,
    *,
    order: int = 5,
) -> HiddenJet:
    """Return exact ordinary Taylor coefficients along feature ascent."""

    if not 0 <= order <= 5:
        raise ValueError("order must lie between zero and five")
    gram, channel = validate_problem(state, input_gram, channel)
    hidden_layers = state.hidden_layers
    oracles = as_oracle_tuple(activation_derivative, hidden_layers)
    n = state.width
    batch = gram.shape[0]
    if batch != 1:
        raise ValueError("this independent audit is restricted to B=1")
    inv_sqrt_n = 1.0 / sqrt(n)

    z = [np.zeros((order + 1, n, 1)) for _ in range(hidden_layers)]
    x = [np.zeros_like(value) for value in z]
    phi_prime = [np.zeros_like(value) for value in z]
    delta = [np.zeros_like(value) for value in z]
    backward = [np.zeros_like(value) for value in z]
    readout = np.zeros((order + 1, n))
    weights = [
        np.zeros((order + 1, n, n)) for _ in range(hidden_layers - 1)
    ]
    output = np.zeros(order + 1)

    z[0][0] = state.first_preactivation
    readout[0] = state.readout
    for layer, initial_weight in enumerate(state.hidden_weights):
        weights[layer][0] = initial_weight

    for degree in range(order + 1):
        x[0][degree] = compose_coefficient(oracles[0], z[0], degree)
        for layer in range(1, hidden_layers):
            coefficient = np.zeros((n, 1))
            for left in range(degree + 1):
                coefficient += weights[layer - 1][left] @ x[layer - 1][degree - left]
            z[layer][degree] = inv_sqrt_n * coefficient
            x[layer][degree] = compose_coefficient(oracles[layer], z[layer], degree)

        for left in range(degree + 1):
            output[degree] += np.mean(
                readout[left] * (x[-1][degree - left] @ channel)
            )
        if degree == order:
            break

        for layer in range(hidden_layers):
            phi_prime[layer][degree] = compose_coefficient(
                oracles[layer], z[layer], degree, derivative_shift=1
            )
        top = np.zeros((n, 1))
        for left in range(degree + 1):
            top += readout[left, :, None] * phi_prime[-1][degree - left]
        delta[-1][degree] = top * channel[None, :]

        for layer in range(hidden_layers - 2, -1, -1):
            propagated = np.zeros((n, 1))
            for left in range(degree + 1):
                propagated += weights[layer][left].T @ delta[layer + 1][degree - left]
            backward[layer][degree] = inv_sqrt_n * propagated
            current = np.zeros((n, 1))
            for left in range(degree + 1):
                current += phi_prime[layer][left] * backward[layer][degree - left]
            delta[layer][degree] = current

        readout[degree + 1] = (x[-1][degree] @ channel) / (degree + 1)
        for layer in range(1, hidden_layers):
            rhs = np.zeros((n, n))
            for left in range(degree + 1):
                rhs += delta[layer][left] @ x[layer - 1][degree - left].T
            weights[layer - 1][degree + 1] = inv_sqrt_n * rhs / (degree + 1)
        z[0][degree + 1] = delta[0][degree] @ gram / (degree + 1)

    gammas: list[np.ndarray] = []
    q_derivatives = np.zeros((hidden_layers, order + 1))
    for layer in range(hidden_layers):
        gamma = np.zeros((order + 1, order + 1))
        for r in range(order + 1):
            for s in range(order + 1):
                gamma[r, s] = (
                    factorial(r)
                    * factorial(s)
                    * float(np.mean(x[layer][r] * x[layer][s]))
                )
        gammas.append(gamma)
        for k in range(order + 1):
            q_derivatives[layer, k] = sum(
                factorial(k)
                * float(np.mean(x[layer][r] * x[layer][k - r]))
                for r in range(k + 1)
            )

    return HiddenJet(
        feature_coefficients=tuple(x),
        gamma=tuple(gammas),
        q_derivatives=q_derivatives,
        output_derivatives=np.asarray(
            [factorial(k) * output[k] for k in range(order + 1)]
        ),
    )


def _build_raw_network(
    state: DepthState,
    activation_derivative: DerivativeOracle,
    max_degree: int,
):
    """Build raw multivariate Taylor polynomials for B=1, Q0=1."""

    if state.batch != 1:
        raise ValueError("raw audit requires B=1")
    n = state.width
    h = state.hidden_layers
    dimension = n + (h - 1) * n * n + n
    values = np.concatenate(
        (
            state.first_preactivation[:, 0],
            *(weight.ravel() for weight in state.hidden_weights),
            state.readout,
        )
    )
    variables = [
        raw_ad._variable(float(value), dimension, index)
        for index, value in enumerate(values)
    ]
    cursor = 0
    z = variables[:n]
    cursor += n
    matrices = []
    for _ in range(h - 1):
        matrix = np.asarray(
            variables[cursor : cursor + n * n], dtype=object
        ).reshape(n, n)
        cursor += n * n
        matrices.append(matrix)
    readout = variables[cursor : cursor + n]
    cursor += n
    assert cursor == dimension

    hidden = []
    for layer in range(h):
        x = [
            raw_ad._compose(value, activation_derivative, dimension, max_degree)
            for value in z
        ]
        hidden.append(x)
        if layer == h - 1:
            break
        next_z = []
        for i in range(n):
            total = {}
            for j in range(n):
                total = raw_ad._add(
                    total,
                    raw_ad._scale(
                        raw_ad._multiply(matrices[layer][i, j], x[j], max_degree),
                        1.0 / sqrt(n),
                    ),
                )
            next_z.append(total)
        z = next_z

    output = {}
    for i in range(n):
        output = raw_ad._add(
            output,
            raw_ad._scale(
                raw_ad._multiply(readout[i], hidden[-1][i], max_degree),
                1.0 / n,
            ),
        )
    observables = []
    for x in hidden:
        q = {}
        for value in x:
            q = raw_ad._add(
                q,
                raw_ad._scale(raw_ad._multiply(value, value, max_degree), 1.0 / n),
            )
        observables.append(q)
    return output, observables, dimension


def _operator_on_observable(
    output,
    observable,
    dimension: int,
    width: int,
    order: int,
) -> np.ndarray:
    gradient_f = [raw_ad._differentiate(output, coordinate) for coordinate in range(dimension)]
    current = observable
    values = [raw_ad._value(current, dimension)]
    for derivative_order in range(1, order + 1):
        target_degree = order - derivative_order
        next_poly = {}
        for coordinate in range(dimension):
            next_poly = raw_ad._add(
                next_poly,
                raw_ad._multiply(
                    gradient_f[coordinate],
                    raw_ad._differentiate(current, coordinate),
                    target_degree,
                ),
            )
        current = raw_ad._scale(next_poly, float(width))
        values.append(raw_ad._value(current, dimension))
    return np.asarray(values)


def raw_coordinate_q_derivatives(
    state: DepthState,
    activation_derivative: DerivativeOracle,
    *,
    order: int = 4,
) -> np.ndarray:
    """Apply the exact Lie derivative to every hidden squared RMS."""

    if state.width > 2:
        raise ValueError("raw audit is intentionally limited to width <= 2")
    output, observables, dimension = _build_raw_network(
        state, activation_derivative, max_degree=order + 1
    )
    return np.asarray(
        [
            _operator_on_observable(
                output, observable, dimension, state.width, order
            )
            for observable in observables
        ]
    )

