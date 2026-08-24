#!/usr/bin/env python3
"""Finite-difference regression for the exact identities in Theorem 12.1.

This is an audit, not part of the analytic proof.  It checks every
output/parameter Jacobian entry, the scaled-kernel symmetry and positivity,
and the equality between chain-rule and kernel output velocities.
"""

from __future__ import annotations

import numpy as np


def sigmoid(x: np.ndarray | float) -> np.ndarray | float:
    return np.tanh(x)


def phi(theta: np.ndarray, x: float) -> float:
    alpha, omega, beta = theta
    return float(
        sigmoid(alpha) * sigmoid(sigmoid(omega) * x + sigmoid(beta))
    )


def grad_phi(theta: np.ndarray, x: float) -> np.ndarray:
    alpha, omega, beta = theta
    amplitude = sigmoid(alpha)
    slope = sigmoid(omega)
    bias = sigmoid(beta)
    hidden = slope * x + bias
    gate = 1.0 - sigmoid(hidden) ** 2
    return np.array(
        [
            (1.0 - amplitude**2) * sigmoid(hidden),
            amplitude * gate * (1.0 - slope**2) * x,
            amplitude * gate * (1.0 - bias**2),
        ]
    )


def dx_phi(theta: np.ndarray, x: float) -> float:
    alpha, omega, beta = theta
    amplitude = sigmoid(alpha)
    slope = sigmoid(omega)
    hidden = slope * x + sigmoid(beta)
    return float(amplitude * (1.0 - sigmoid(hidden) ** 2) * slope)


def forward(theta: np.ndarray, inputs: np.ndarray) -> np.ndarray:
    depth, width, _ = theta.shape
    batch = len(inputs)
    states = np.empty((batch, depth + 1))
    states[:, 0] = inputs
    for layer in range(depth):
        for sample in range(batch):
            increment = sum(
                phi(theta[layer, neuron], states[sample, layer])
                for neuron in range(width)
            )
            states[sample, layer + 1] = (
                states[sample, layer] + increment / (width * depth)
            )
    return states


def main() -> None:
    rng = np.random.default_rng(20260822)
    batch, width, depth = 2, 4, 3
    eta = 0.7
    inputs = np.array([0.4, -0.8])
    labels = np.array([0.3, -0.2])
    theta = rng.normal(size=(depth, width, 3))

    states = forward(theta, inputs)
    outputs = states[:, -1]

    sensitivity = np.ones((batch, depth + 1))
    for layer in range(depth - 1, -1, -1):
        for sample in range(batch):
            activation_derivative = sum(
                dx_phi(theta[layer, neuron], states[sample, layer])
                for neuron in range(width)
            ) / width
            sensitivity[sample, layer] = sensitivity[sample, layer + 1] * (
                1.0 + activation_derivative / depth
            )

    jacobian = np.empty((batch, depth, width, 3))
    for sample in range(batch):
        for layer in range(depth):
            for neuron in range(width):
                jacobian[sample, layer, neuron] = (
                    sensitivity[sample, layer + 1]
                    * grad_phi(theta[layer, neuron], states[sample, layer])
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
                        forward(theta_plus, inputs)[sample, -1]
                        - forward(theta_minus, inputs)[sample, -1]
                    ) / (2.0 * epsilon)
                    max_jacobian_error = max(
                        max_jacobian_error,
                        abs(
                            finite_difference
                            - jacobian[sample, layer, neuron, coordinate]
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

    symmetry_error = float(np.max(np.abs(kernel - kernel.T)))
    dynamics_error = float(np.max(np.abs(chain_velocity - kernel_velocity)))
    minimum_eigenvalue = float(np.linalg.eigvalsh(kernel).min())

    print(f"max_output_jacobian_error={max_jacobian_error:.16e}")
    print(f"kernel_symmetry_error={symmetry_error:.16e}")
    print(f"output_dynamics_error={dynamics_error:.16e}")
    print(f"kernel_min_eigenvalue={minimum_eigenvalue:.16e}")

    assert max_jacobian_error < 1.0e-8
    assert symmetry_error < 1.0e-13
    assert dynamics_error < 1.0e-13
    assert minimum_eigenvalue > -1.0e-12


if __name__ == "__main__":
    main()
