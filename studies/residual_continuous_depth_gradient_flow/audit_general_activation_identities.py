#!/usr/bin/env python3
"""Activation-diverse finite regression for the general ResNet identities.

This is not a premise of the proof.  It checks the activation-independent
adjoint, output Jacobian, scaled kernel, and output-flow formulas for several
members of the admissible class.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np


ArrayFn = Callable[[np.ndarray | float], np.ndarray | float]


@dataclass(frozen=True)
class Activation:
    name: str
    value: ArrayFn
    derivative: ArrayFn


ACTIVATIONS = (
    Activation("tanh", np.tanh, lambda z: 1.0 - np.tanh(z) ** 2),
    Activation("arctan", np.arctan, lambda z: 1.0 / (1.0 + z**2)),
    Activation("sine", np.sin, np.cos),
    Activation("identity", lambda z: z, lambda z: np.ones_like(z)),
    Activation(
        "softplus",
        lambda z: np.logaddexp(0.0, z),
        lambda z: 0.5 * (1.0 + np.tanh(z / 2.0)),
    ),
)


def phi(theta: np.ndarray, x: float, activation: Activation) -> float:
    alpha, omega, beta = theta
    amplitude = np.tanh(alpha)
    slope = np.tanh(omega)
    bias = np.tanh(beta)
    return float(amplitude * activation.value(slope * x + bias))


def grad_phi(
    theta: np.ndarray, x: float, activation: Activation
) -> np.ndarray:
    alpha, omega, beta = theta
    amplitude = np.tanh(alpha)
    slope = np.tanh(omega)
    bias = np.tanh(beta)
    hidden = slope * x + bias
    sigma = activation.value(hidden)
    dsigma = activation.derivative(hidden)
    return np.array(
        [
            (1.0 - amplitude**2) * sigma,
            amplitude * dsigma * (1.0 - slope**2) * x,
            amplitude * dsigma * (1.0 - bias**2),
        ],
        dtype=float,
    )


def dx_phi(theta: np.ndarray, x: float, activation: Activation) -> float:
    alpha, omega, beta = theta
    amplitude = np.tanh(alpha)
    slope = np.tanh(omega)
    bias = np.tanh(beta)
    hidden = slope * x + bias
    return float(amplitude * activation.derivative(hidden) * slope)


def forward(
    theta: np.ndarray, inputs: np.ndarray, activation: Activation
) -> np.ndarray:
    depth, width, _ = theta.shape
    states = np.empty((len(inputs), depth + 1))
    states[:, 0] = inputs
    for layer in range(depth):
        for sample in range(len(inputs)):
            increment = sum(
                phi(theta[layer, neuron], states[sample, layer], activation)
                for neuron in range(width)
            )
            states[sample, layer + 1] = (
                states[sample, layer] + increment / (width * depth)
            )
    return states


def audit(activation: Activation) -> tuple[float, float, float, float]:
    rng = np.random.default_rng(20260822)
    batch, width, depth = 2, 4, 3
    eta = 0.7
    inputs = np.array([0.4, -0.8])
    labels = np.array([0.3, -0.2])
    theta = rng.normal(size=(depth, width, 3))

    states = forward(theta, inputs, activation)
    outputs = states[:, -1]

    sensitivity = np.ones((batch, depth + 1))
    for layer in range(depth - 1, -1, -1):
        for sample in range(batch):
            averaged_dx = sum(
                dx_phi(
                    theta[layer, neuron], states[sample, layer], activation
                )
                for neuron in range(width)
            ) / width
            sensitivity[sample, layer] = sensitivity[sample, layer + 1] * (
                1.0 + averaged_dx / depth
            )

    jacobian = np.empty((batch, depth, width, 3))
    for sample in range(batch):
        for layer in range(depth):
            for neuron in range(width):
                jacobian[sample, layer, neuron] = (
                    sensitivity[sample, layer + 1]
                    * grad_phi(
                        theta[layer, neuron],
                        states[sample, layer],
                        activation,
                    )
                    / (width * depth)
                )

    epsilon = 2.0e-6
    max_jacobian_error = 0.0
    for sample in range(batch):
        for layer in range(depth):
            for neuron in range(width):
                for coordinate in range(3):
                    theta_plus = theta.copy()
                    theta_minus = theta.copy()
                    theta_plus[layer, neuron, coordinate] += epsilon
                    theta_minus[layer, neuron, coordinate] -= epsilon
                    finite_difference = (
                        forward(theta_plus, inputs, activation)[sample, -1]
                        - forward(theta_minus, inputs, activation)[sample, -1]
                    ) / (2.0 * epsilon)
                    max_jacobian_error = max(
                        max_jacobian_error,
                        abs(
                            finite_difference
                            - jacobian[
                                sample, layer, neuron, coordinate
                            ]
                        ),
                    )

    kernel = width * depth * np.einsum(
        "blik,clik->bc", jacobian, jacobian
    )
    loss_gradient = np.einsum(
        "b,blik->lik", (outputs - labels) / batch, jacobian
    )
    parameter_velocity = -eta * width * depth * loss_gradient
    chain_velocity = np.einsum(
        "blik,lik->b", jacobian, parameter_velocity
    )
    kernel_velocity = -eta * kernel @ (outputs - labels) / batch

    return (
        max_jacobian_error,
        float(np.max(np.abs(kernel - kernel.T))),
        float(np.max(np.abs(chain_velocity - kernel_velocity))),
        float(np.linalg.eigvalsh(kernel).min()),
    )


def main() -> None:
    for activation in ACTIVATIONS:
        jacobian_error, symmetry_error, dynamics_error, min_eigenvalue = (
            audit(activation)
        )
        print(
            f"{activation.name}: "
            f"jac={jacobian_error:.3e} "
            f"sym={symmetry_error:.3e} "
            f"dyn={dynamics_error:.3e} "
            f"lambda_min={min_eigenvalue:.3e}"
        )
        assert jacobian_error < 2.0e-8
        assert symmetry_error < 1.0e-13
        assert dynamics_error < 1.0e-13
        assert min_eigenvalue > -1.0e-12


if __name__ == "__main__":
    main()
