"""Independent fixed-batch Taylor propagation for the feature-ascent ODE."""

from __future__ import annotations

from dataclasses import dataclass
from math import factorial, sqrt
from typing import Callable

import numpy as np

from .model import B2State, validate_channel, validate_gram


DerivativeOracle = Callable[[int, np.ndarray], np.ndarray]


def _compose(
    derivative: DerivativeOracle,
    series: np.ndarray,
    degree: int,
    *,
    derivative_order: int = 0,
) -> np.ndarray:
    evaluate = lambda order, x: derivative(order + derivative_order, x)
    x0 = series[0]
    if degree == 0:
        return evaluate(0, x0)
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
    raise NotImplementedError("the fixed-batch audit is capped at order three")


@dataclass(frozen=True)
class B2Jet:
    ordinary_coefficients: np.ndarray

    @property
    def derivatives(self) -> np.ndarray:
        return np.asarray(
            [factorial(k) * value for k, value in enumerate(self.ordinary_coefficients)]
        )


def directional_feature_jet(
    state: B2State,
    input_gram: np.ndarray,
    channel: np.ndarray,
    activation_derivative: DerivativeOracle,
    *,
    order: int = 3,
) -> B2Jet:
    """Propagate the exact finite-width ODE for ``g_c=c.T@f``."""

    input_gram = validate_gram(input_gram)
    batch = input_gram.shape[0]
    channel = validate_channel(channel, batch)
    if not 0 <= order <= 3:
        raise ValueError("order must lie between zero and three")
    n = state.width
    inv_sqrt_n = 1.0 / sqrt(n)

    if state.first_preactivation.shape != (n, batch):
        raise ValueError("bad first-preactivation shape")
    u = np.zeros((order + 1, n, batch), dtype=np.float64)
    readout = np.zeros((order + 1, n), dtype=np.float64)
    weight = np.zeros((order + 1, n, n), dtype=np.float64)
    h = np.zeros_like(u)
    h1 = np.zeros_like(u)
    z = np.zeros_like(u)
    y = np.zeros_like(u)
    y1 = np.zeros_like(u)
    source = np.zeros_like(u)
    backward = np.zeros_like(u)
    output = np.zeros(order + 1, dtype=np.float64)

    u[0] = state.first_preactivation
    readout[0] = state.readout
    weight[0] = state.middle_weight

    for k in range(order + 1):
        h[k] = _compose(activation_derivative, u, k)

        zk = np.zeros((n, batch))
        for left in range(k + 1):
            zk += weight[left] @ h[k - left]
        z[k] = inv_sqrt_n * zk
        y[k] = _compose(activation_derivative, z, k)

        for left in range(k + 1):
            output[k] += np.mean(readout[left] * (y[k - left] @ channel))

        if k == order:
            break

        h1[k] = _compose(activation_derivative, u, k, derivative_order=1)
        y1[k] = _compose(activation_derivative, z, k, derivative_order=1)

        source_k = np.zeros((n, batch))
        for left in range(k + 1):
            source_k += readout[left, :, None] * y1[k - left]
        source[k] = source_k * channel[None, :]

        backward_k = np.zeros((n, batch))
        for left in range(k + 1):
            backward_k += weight[left].T @ source[k - left]
        backward[k] = inv_sqrt_n * backward_k

        readout[k + 1] = (y[k] @ channel) / (k + 1)

        weight_rhs = np.zeros((n, n))
        for left in range(k + 1):
            weight_rhs += source[left] @ h[k - left].T
        weight[k + 1] = inv_sqrt_n * weight_rhs / (k + 1)

        u_rhs = np.zeros((n, batch))
        for left in range(k + 1):
            u_rhs += h1[left] * backward[k - left]
        u[k + 1] = (u_rhs @ input_gram) / (k + 1)

    return B2Jet(output)
