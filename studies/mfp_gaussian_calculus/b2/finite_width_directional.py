"""Direct fixed Tensor-Program evaluation of ``D_c^3 g_c`` for fixed B.

No width limit, Gaussian replacement, Hermite expansion, or Taylor-series
parameter propagation is used here.  The calculation is the vectorized
two-sample analogue of equation (3.10) in the B=1 probability ledger.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Callable

import numpy as np

from .model import B2State, validate_channel, validate_gram


DerivativeOracle = Callable[[int, np.ndarray], np.ndarray]


def _moment(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    """Return the normalized channel Gram ``left.T @ right / n``."""

    return left.T @ right / left.shape[0]


@dataclass(frozen=True)
class B2DirectionalContraction:
    straight_line: float
    hessian_readout: float
    hessian_middle: float
    hessian_first: float

    @property
    def value(self) -> float:
        return 2.0 * self.straight_line + 4.0 * (
            self.hessian_readout + self.hessian_middle + self.hessian_first
        )


@dataclass(frozen=True)
class FrozenMSEResponses:
    """The two extra cubic-response observables in the MSE loss jet.

    With ``p=grad(g_c)``, ``j_s=grad(f_s)``, and ``H_s=Hess(f_s)``, the
    three channel arrays are

    ``kernel_direction[s] = n * j_s.dot(p)``,
    ``straight_hessian[s] = n**2 * H_s[p,p]``, and
    ``gradient_response[s] = n**2 * j_s.dot(Hess(g_c) @ p)``.

    Consequently ``metric_response`` is exactly
    ``n**3 p.T @ ((1/B) sum_s j_s j_s.T) @ Hess(g_c) @ p``, while
    ``output_response`` is exactly
    ``(n**3/B) sum_s (j_s.dot(p)) H_s[p,p]``.
    """

    kernel_direction: np.ndarray
    straight_hessian: np.ndarray
    gradient_response: np.ndarray
    metric_response: float
    output_response: float


@dataclass(frozen=True)
class MSEThirdDerivative:
    """Exact finite-width third time derivative for MSE gradient flow."""

    value: float
    kernel_cube: float
    feature_correction: float
    metric_response: float
    output_response: float


def directional_third_contraction(
    state: B2State,
    input_gram: np.ndarray,
    channel: np.ndarray,
    activation_derivative: DerivativeOracle,
) -> B2DirectionalContraction:
    """Evaluate the exact finite-width scalar ``D_c^3 g_c``.

    Here ``g_c=c.T @ f`` and ``D_c=n*grad(g_c).grad``.  The first-layer
    parameter block is scalarized through its exact two-sample metric
    ``input_gram``.
    """

    input_gram = validate_gram(input_gram)
    batch = input_gram.shape[0]
    channel = validate_channel(channel, batch)
    n = state.width
    if state.first_preactivation.shape != (n, batch):
        raise ValueError("bad first-preactivation shape")
    if state.middle_weight.shape != (n, n):
        raise ValueError("bad middle-weight shape")

    middle = state.middle_weight / sqrt(n)
    readout = state.readout
    u = state.first_preactivation

    x0 = activation_derivative(0, u)
    x1 = activation_derivative(1, u)
    x2 = activation_derivative(2, u)
    x3 = activation_derivative(3, u)

    z = middle @ x0
    y0 = activation_derivative(0, z)
    y1 = activation_derivative(1, z)
    y2 = activation_derivative(2, z)
    y3 = activation_derivative(3, z)

    # P is the two-channel top backward source and R its transpose image.
    source = readout[:, None] * y1 * channel[None, :]
    backward = middle.T @ source

    q_n = _moment(x0, x0)
    first_velocity = (x1 * backward) @ input_gram
    h_dot = x1 * first_velocity

    # A_dot H = P Q_n and A H_dot is the propagated branch.
    zeta = source @ q_n + middle @ h_dot

    # Frozen-straight-line second and third hidden derivatives.
    h_ddot = x2 * first_velocity**2
    h_third = x3 * first_velocity**3
    cross_one = _moment(x0, h_dot)
    cross_two = _moment(x0, h_ddot)
    sigma = 2.0 * (source @ cross_one) + middle @ h_ddot
    tau = 3.0 * (source @ cross_two) + middle @ h_third

    readout_velocity = y0 @ channel
    source_dot = (
        readout_velocity[:, None] * y1
        + readout[:, None] * y2 * zeta
    ) * channel[None, :]

    source_gram = _moment(source, source)
    backward_dot = x0 @ source_gram + middle.T @ source_dot

    straight_line = float(
        np.mean(
            readout
            * (
                (
                    y3 * zeta**3
                    + 3.0 * y2 * zeta * sigma
                    + y1 * tau
                )
                @ channel
            )
            + 3.0
            * readout_velocity
            * ((y2 * zeta**2 + y1 * sigma) @ channel)
        )
    )

    readout_gradient_dot = (y1 * zeta) @ channel
    hessian_readout = float(np.mean(readout_gradient_dot**2))

    # ||P_dot H^T + P H_dot^T||_F^2/n^2, factored into 2x2 Moments.
    hessian_middle = float(
        np.trace(_moment(source_dot, source_dot) @ _moment(x0, x0))
        + np.trace(_moment(source, source) @ _moment(h_dot, h_dot))
        + 2.0 * np.trace(_moment(source_dot, source) @ _moment(h_dot, x0))
    )

    first_source_dot = x2 * first_velocity * backward + x1 * backward_dot
    hessian_first = float(
        np.trace(_moment(first_source_dot, first_source_dot) @ input_gram)
    )

    return B2DirectionalContraction(
        straight_line=straight_line,
        hessian_readout=hessian_readout,
        hessian_middle=hessian_middle,
        hessian_first=hessian_first,
    )


def frozen_mse_responses(
    state: B2State,
    input_gram: np.ndarray,
    channel: np.ndarray,
    activation_derivative: DerivativeOracle,
) -> FrozenMSEResponses:
    """Evaluate both additional MSE response scalars for a frozen channel.

    This is an exact finite-width fixed-batch program.  In particular, the
    zero width limits of these observables are *not* inserted here: the
    returned finite-width samples are generally nonzero.
    """

    input_gram = validate_gram(input_gram)
    batch = input_gram.shape[0]
    channel = validate_channel(channel, batch)
    n = state.width
    if state.first_preactivation.shape != (n, batch):
        raise ValueError("bad first-preactivation shape")
    if state.middle_weight.shape != (n, n):
        raise ValueError("bad middle-weight shape")

    middle = state.middle_weight / sqrt(n)
    readout = state.readout
    u = state.first_preactivation

    x0 = activation_derivative(0, u)
    x1 = activation_derivative(1, u)
    x2 = activation_derivative(2, u)
    z = middle @ x0
    y0 = activation_derivative(0, z)
    y1 = activation_derivative(1, z)
    y2 = activation_derivative(2, z)

    source = readout[:, None] * y1 * channel[None, :]
    backward = middle.T @ source
    q_n = _moment(x0, x0)
    first_velocity = (x1 * backward) @ input_gram
    h_dot = x1 * first_velocity
    zeta = source @ q_n + middle @ h_dot

    h_ddot = x2 * first_velocity**2
    sigma = 2.0 * (source @ _moment(x0, h_dot)) + middle @ h_ddot

    readout_velocity = y0 @ channel
    source_dot = (
        readout_velocity[:, None] * y1
        + readout[:, None] * y2 * zeta
    ) * channel[None, :]
    backward_dot = x0 @ _moment(source, source) + middle.T @ source_dot
    first_source_dot = x2 * first_velocity * backward + x1 * backward_dot
    readout_gradient_dot = (y1 * zeta) @ channel

    kernel_direction = np.empty(batch, dtype=np.float64)
    straight_hessian = np.empty(batch, dtype=np.float64)
    gradient_response = np.empty(batch, dtype=np.float64)
    for sample in range(batch):
        kernel_direction[sample] = np.mean(
            readout_velocity * y0[:, sample]
            + readout * y1[:, sample] * zeta[:, sample]
        )
        straight_hessian[sample] = np.mean(
            readout
            * (
                y2[:, sample] * zeta[:, sample] ** 2
                + y1[:, sample] * sigma[:, sample]
            )
            + 2.0
            * readout_velocity
            * y1[:, sample]
            * zeta[:, sample]
        )

        # P^[s], R^[s], and S^[s] are the three gradient coefficient
        # arrays for the individual output f_s.
        sample_source = np.zeros_like(source)
        sample_source[:, sample] = readout * y1[:, sample]
        sample_backward = middle.T @ sample_source
        sample_first_source = x1 * sample_backward

        gradient_response[sample] = (
            np.mean(y0[:, sample] * readout_gradient_dot)
            + np.trace(_moment(sample_source, source_dot) @ q_n)
            + np.trace(
                _moment(sample_source, source) @ _moment(h_dot, x0)
            )
            + np.trace(
                _moment(sample_first_source, first_source_dot) @ input_gram
            )
        )

    metric_response = float(
        np.dot(kernel_direction, gradient_response) / batch
    )
    output_response = float(
        np.dot(kernel_direction, straight_hessian) / batch
    )
    return FrozenMSEResponses(
        kernel_direction=kernel_direction,
        straight_hessian=straight_hessian,
        gradient_response=gradient_response,
        metric_response=metric_response,
        output_response=output_response,
    )


def mse_loss_third_derivative(
    state: B2State,
    input_gram: np.ndarray,
    labels: np.ndarray,
    activation_derivative: DerivativeOracle,
) -> MSEThirdDerivative:
    """Evaluate ``J'''(0)`` for ``J=||f-y||^2/B`` and ``theta'=-n grad J``.

    The residual channel is evaluated at the supplied finite-width state, so
    this routine is the exact residual-dependent identity rather than its
    centered-readout width limit.
    """

    input_gram = validate_gram(input_gram)
    batch = input_gram.shape[0]
    labels = validate_channel(labels, batch)
    n = state.width
    middle = state.middle_weight / sqrt(n)
    x0 = activation_derivative(0, state.first_preactivation)
    y0 = activation_derivative(0, middle @ x0)
    output = state.readout @ y0 / n
    residual = labels - output
    channel = residual / batch

    response = frozen_mse_responses(
        state, input_gram, channel, activation_derivative
    )
    kernel = np.column_stack(
        [
            frozen_mse_responses(
                state,
                input_gram,
                np.eye(batch, dtype=np.float64)[sample],
                activation_derivative,
            ).kernel_direction
            for sample in range(batch)
        ]
    )
    kernel_cube = float(residual @ kernel @ kernel @ kernel @ residual)
    feature_correction = directional_third_contraction(
        state, input_gram, channel, activation_derivative
    ).value
    value = (
        -64.0 * kernel_cube / batch**4
        - 16.0 * feature_correction
        + 128.0 * response.metric_response
        + 96.0 * response.output_response
    )
    return MSEThirdDerivative(
        value=value,
        kernel_cube=kernel_cube,
        feature_correction=feature_correction,
        metric_response=response.metric_response,
        output_response=response.output_response,
    )
