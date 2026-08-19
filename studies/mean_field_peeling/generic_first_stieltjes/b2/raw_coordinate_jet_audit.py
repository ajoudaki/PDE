"""Independent raw-coordinate third-order jet audit for the B=2 program.

This file deliberately does not use the feature-ascent ODE or any tangent
formula from ``finite_width_directional.py`` / ``finite_width_jet.py``.  It
evaluates the original network with a third-order multivariate jet in every
raw parameter and contracts the resulting gradient, Hessian, and third
derivative tensor with the exact identity for ``D_c^3 g_c``.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

import numpy as np

from .finite_width_directional import (
    directional_third_contraction,
    frozen_mse_responses,
    mse_loss_third_derivative,
)
from .model import B2State, gram_root
from .test_finite_width_directional import ACTIVATIONS


@dataclass(frozen=True)
class Jet3:
    value: float
    gradient: np.ndarray
    hessian: np.ndarray
    third: np.ndarray

    @classmethod
    def constant(cls, value: float, dimension: int) -> "Jet3":
        return cls(
            float(value),
            np.zeros(dimension),
            np.zeros((dimension, dimension)),
            np.zeros((dimension, dimension, dimension)),
        )

    @classmethod
    def variable(cls, value: float, dimension: int, index: int) -> "Jet3":
        gradient = np.zeros(dimension)
        gradient[index] = 1.0
        return cls(
            float(value),
            gradient,
            np.zeros((dimension, dimension)),
            np.zeros((dimension, dimension, dimension)),
        )

    def __add__(self, other: "Jet3 | float") -> "Jet3":
        if not isinstance(other, Jet3):
            other = Jet3.constant(float(other), self.gradient.size)
        return Jet3(
            self.value + other.value,
            self.gradient + other.gradient,
            self.hessian + other.hessian,
            self.third + other.third,
        )

    __radd__ = __add__

    def __neg__(self) -> "Jet3":
        return Jet3(-self.value, -self.gradient, -self.hessian, -self.third)

    def __sub__(self, other: "Jet3 | float") -> "Jet3":
        return self + (-other if isinstance(other, Jet3) else -float(other))

    def __rsub__(self, other: float) -> "Jet3":
        return (-self) + float(other)

    def __mul__(self, other: "Jet3 | float") -> "Jet3":
        if not isinstance(other, Jet3):
            other = Jet3.constant(float(other), self.gradient.size)
        x, y = self, other
        gradient = x.gradient * y.value + x.value * y.gradient
        hessian = (
            x.hessian * y.value
            + x.value * y.hessian
            + np.einsum("i,j->ij", x.gradient, y.gradient)
            + np.einsum("i,j->ij", y.gradient, x.gradient)
        )
        third = x.third * y.value + x.value * y.third
        third += np.einsum("ij,k->ijk", x.hessian, y.gradient)
        third += np.einsum("ik,j->ijk", x.hessian, y.gradient)
        third += np.einsum("jk,i->ijk", x.hessian, y.gradient)
        third += np.einsum("ij,k->ijk", y.hessian, x.gradient)
        third += np.einsum("ik,j->ijk", y.hessian, x.gradient)
        third += np.einsum("jk,i->ijk", y.hessian, x.gradient)
        return Jet3(x.value * y.value, gradient, hessian, third)

    __rmul__ = __mul__

    def __truediv__(self, other: float) -> "Jet3":
        return self * (1.0 / float(other))


def compose(jet: Jet3, values: tuple[float, float, float, float]) -> Jet3:
    """Return ``f(jet)`` from ``(f,f',f'',f''')`` at ``jet.value``."""

    f0, f1, f2, f3 = values
    gradient = f1 * jet.gradient
    hessian = f1 * jet.hessian + f2 * np.einsum(
        "i,j->ij", jet.gradient, jet.gradient
    )
    third = f1 * jet.third
    third += f2 * np.einsum("ij,k->ijk", jet.hessian, jet.gradient)
    third += f2 * np.einsum("ik,j->ijk", jet.hessian, jet.gradient)
    third += f2 * np.einsum("jk,i->ijk", jet.hessian, jet.gradient)
    third += f3 * np.einsum(
        "i,j,k->ijk", jet.gradient, jet.gradient, jet.gradient
    )
    return Jet3(f0, gradient, hessian, third)


def _raw_coordinate_outputs(
    first_weight: np.ndarray,
    middle_weight: np.ndarray,
    readout: np.ndarray,
    inputs: np.ndarray,
    activation_derivative,
) -> tuple[tuple[Jet3, ...], B2State, np.ndarray]:
    """Build the individual output jets directly in all raw coordinates."""

    width, input_dimension = first_weight.shape
    batch = inputs.shape[1]
    parameter_values = np.concatenate(
        (first_weight.ravel(), middle_weight.ravel(), readout.ravel())
    )
    dimension = parameter_values.size
    variables = [
        Jet3.variable(value, dimension, index)
        for index, value in enumerate(parameter_values)
    ]
    cursor = 0
    w = np.asarray(variables[cursor : cursor + width * input_dimension], dtype=object)
    w = w.reshape(width, input_dimension)
    cursor += width * input_dimension
    middle = np.asarray(variables[cursor : cursor + width * width], dtype=object)
    middle = middle.reshape(width, width)
    cursor += width * width
    a = np.asarray(variables[cursor : cursor + width], dtype=object)

    u = np.empty((width, batch), dtype=object)
    for j in range(width):
        for sample in range(batch):
            total = Jet3.constant(0.0, dimension)
            for coordinate in range(input_dimension):
                total += w[j, coordinate] * (
                    inputs[coordinate, sample] / sqrt(input_dimension)
                )
            u[j, sample] = total

    h = np.empty_like(u)
    for index in np.ndindex(h.shape):
        scalar = u[index]
        derivative_values = tuple(
            float(activation_derivative(order, np.asarray(scalar.value)))
            for order in range(4)
        )
        h[index] = compose(scalar, derivative_values)

    z = np.empty((width, batch), dtype=object)
    for i in range(width):
        for sample in range(batch):
            total = Jet3.constant(0.0, dimension)
            for j in range(width):
                total += middle[i, j] * h[j, sample] / sqrt(width)
            z[i, sample] = total

    y = np.empty_like(z)
    for index in np.ndindex(y.shape):
        scalar = z[index]
        derivative_values = tuple(
            float(activation_derivative(order, np.asarray(scalar.value)))
            for order in range(4)
        )
        y[index] = compose(scalar, derivative_values)

    outputs = []
    for sample in range(batch):
        output = Jet3.constant(0.0, dimension)
        for i in range(width):
            output += a[i] * y[i, sample] / width
        outputs.append(output)

    numeric_u = first_weight @ inputs / sqrt(input_dimension)
    gram = inputs.T @ inputs / input_dimension
    state = B2State(numeric_u, middle_weight, readout)
    return tuple(outputs), state, gram


def raw_coordinate_contraction(
    first_weight: np.ndarray,
    middle_weight: np.ndarray,
    readout: np.ndarray,
    inputs: np.ndarray,
    channel: np.ndarray,
    activation_derivative,
) -> tuple[float, B2State, np.ndarray]:
    """Compute ``D_c^3 g_c`` from the raw network's full derivative tensors."""

    outputs, state, gram = _raw_coordinate_outputs(
        first_weight,
        middle_weight,
        readout,
        inputs,
        activation_derivative,
    )
    dimension = outputs[0].gradient.size
    output = Jet3.constant(0.0, dimension)
    for coefficient, sample_output in zip(channel, outputs):
        output += coefficient * sample_output

    p = output.gradient
    hp = output.hessian @ p
    straight = np.einsum("ijk,i,j,k", output.third, p, p, p)
    width = first_weight.shape[0]
    contraction = float(width**3 * (4.0 * np.dot(hp, hp) + 2.0 * straight))

    return contraction, state, gram


def raw_coordinate_mse_third_derivative(
    first_weight: np.ndarray,
    middle_weight: np.ndarray,
    readout: np.ndarray,
    inputs: np.ndarray,
    labels: np.ndarray,
    activation_derivative,
) -> tuple[float, B2State, np.ndarray]:
    """Compute the MSE flow third derivative from the full raw loss jet."""

    outputs, state, gram = _raw_coordinate_outputs(
        first_weight,
        middle_weight,
        readout,
        inputs,
        activation_derivative,
    )
    batch = len(outputs)
    dimension = outputs[0].gradient.size
    loss = Jet3.constant(0.0, dimension)
    for label, output in zip(labels, outputs):
        error = output - float(label)
        loss += error * error / batch

    gradient = loss.gradient
    hessian_gradient = loss.hessian @ gradient
    straight = np.einsum(
        "ijk,i,j,k", loss.third, gradient, gradient, gradient
    )
    width = first_weight.shape[0]
    derivative = -float(
        width**3
        * (4.0 * np.dot(hessian_gradient, hessian_gradient) + 2.0 * straight)
    )
    return derivative, state, gram


def raw_coordinate_frozen_responses(
    first_weight: np.ndarray,
    middle_weight: np.ndarray,
    readout: np.ndarray,
    inputs: np.ndarray,
    channel: np.ndarray,
    activation_derivative,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, B2State, np.ndarray]:
    """Compute every component of (k,h,q) from raw output Hessians."""

    outputs, state, gram = _raw_coordinate_outputs(
        first_weight,
        middle_weight,
        readout,
        inputs,
        activation_derivative,
    )
    dimension = outputs[0].gradient.size
    directional_output = Jet3.constant(0.0, dimension)
    for coefficient, output in zip(channel, outputs):
        directional_output += coefficient * output
    p = directional_output.gradient
    hp = directional_output.hessian @ p
    width = first_weight.shape[0]
    kernel_direction = np.asarray(
        [width * np.dot(output.gradient, p) for output in outputs]
    )
    straight_hessian = np.asarray(
        [
            width**2 * np.einsum("i,ij,j", p, output.hessian, p)
            for output in outputs
        ]
    )
    gradient_response = np.asarray(
        [width**2 * np.dot(output.gradient, hp) for output in outputs]
    )
    return kernel_direction, straight_hessian, gradient_response, state, gram


def run() -> None:
    cases = (
        (1, "affine", np.asarray([0.4, -1.2])),
        (1, "cubic", np.asarray([1.0, 0.3])),
        (2, "tanh", np.asarray([0.25, -1.3])),
        (2, "sin", np.asarray([1.0, 1.0])),
    )
    grams = (
        np.asarray([[1.1, -0.27], [-0.27, 0.65]]),
        np.asarray([[0.8, 0.8], [0.8, 0.8]]),
    )
    rng = np.random.default_rng(4817)
    checked = 0
    worst_relative = 0.0
    for width, activation_name, channel in cases:
        for gram in grams:
            inputs = sqrt(2.0) * gram_root(gram).T
            first_weight = rng.standard_normal((width, 2))
            middle_weight = rng.standard_normal((width, width))
            readout = rng.standard_normal(width)
            oracle = ACTIVATIONS[activation_name]
            raw, state, recovered_gram = raw_coordinate_contraction(
                first_weight,
                middle_weight,
                readout,
                inputs,
                channel,
                oracle,
            )
            direct = directional_third_contraction(
                state, recovered_gram, channel, oracle
            ).value
            scale = max(1.0, abs(raw), abs(direct))
            relative = abs(raw - direct) / scale
            worst_relative = max(worst_relative, relative)
            np.testing.assert_allclose(raw, direct, rtol=1.0e-10, atol=1.0e-10)
            checked += 1

    response_checked = 0
    for width, activation_name, channel in cases[:4]:
        gram = grams[response_checked % len(grams)]
        inputs = sqrt(2.0) * gram_root(gram).T
        first_weight = rng.standard_normal((width, 2))
        middle_weight = rng.standard_normal((width, width))
        readout = rng.standard_normal(width)
        oracle = ACTIVATIONS[activation_name]
        raw_k, raw_h, raw_q, state, recovered_gram = (
            raw_coordinate_frozen_responses(
                first_weight,
                middle_weight,
                readout,
                inputs,
                channel,
                oracle,
            )
        )
        direct = frozen_mse_responses(
            state, recovered_gram, channel, oracle
        )
        np.testing.assert_allclose(
            np.concatenate((raw_k, raw_h, raw_q)),
            np.concatenate(
                (
                    direct.kernel_direction,
                    direct.straight_hessian,
                    direct.gradient_response,
                )
            ),
            rtol=1.0e-10,
            atol=1.0e-10,
        )
        response_checked += 1

    loss_checked = 0
    loss_cases = (
        (1, "affine", np.asarray([0.7, -1.1])),
        (1, "cubic", np.asarray([-0.2, 0.9])),
        (2, "tanh", np.asarray([1.3, -0.4])),
        (2, "sin", np.asarray([0.1, 0.6])),
    )
    for width, activation_name, labels in loss_cases:
        gram = grams[loss_checked % len(grams)]
        inputs = sqrt(2.0) * gram_root(gram).T
        first_weight = rng.standard_normal((width, 2))
        middle_weight = rng.standard_normal((width, width))
        readout = rng.standard_normal(width)
        oracle = ACTIVATIONS[activation_name]
        raw, state, recovered_gram = raw_coordinate_mse_third_derivative(
            first_weight,
            middle_weight,
            readout,
            inputs,
            labels,
            oracle,
        )
        direct = mse_loss_third_derivative(
            state, recovered_gram, labels, oracle
        ).value
        scale = max(1.0, abs(raw), abs(direct))
        relative = abs(raw - direct) / scale
        worst_relative = max(worst_relative, relative)
        np.testing.assert_allclose(raw, direct, rtol=1.0e-10, atol=1.0e-10)
        loss_checked += 1
    print(
        f"PASS {checked} feature, {response_checked} response, and "
        f"{loss_checked} MSE independent "
        "raw-coordinate third-jet checks; "
        f"worst scaled error={worst_relative:.3e}"
    )


if __name__ == "__main__":
    run()
