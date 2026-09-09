"""Independent raw-coordinate derivative-tensor audit for arbitrary depth.

This route never evolves the feature-ascent ODE and does not import its
ordinary-series compiler.  It differentiates the original network in every
raw coordinate with a third-order multivariate jet, then uses the exact
gradient-flow identities

    g'   = n ||p||^2,
    g''  = 2 n^2 p.T H p,
    g''' = n^3 (4 ||H p||^2 + 2 T[p,p,p]),

where ``p=grad g``.  It is intentionally intended only for tiny audit cases.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

import numpy as np

from .model import DepthState, as_oracle_tuple


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
            np.zeros(dimension, dtype=np.float64),
            np.zeros((dimension, dimension), dtype=np.float64),
            np.zeros((dimension, dimension, dimension), dtype=np.float64),
        )

    @classmethod
    def variable(cls, value: float, dimension: int, index: int) -> "Jet3":
        gradient = np.zeros(dimension, dtype=np.float64)
        gradient[index] = 1.0
        return cls(
            float(value),
            gradient,
            np.zeros((dimension, dimension), dtype=np.float64),
            np.zeros((dimension, dimension, dimension), dtype=np.float64),
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
    """Apply a scalar function given ``(phi,phi',phi'',phi''')`` at the base."""

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
    return Jet3(float(f0), gradient, hessian, third)


def _jet_matrix(
    variables: list[Jet3], cursor: int, shape: tuple[int, ...]
) -> tuple[np.ndarray, int]:
    size = int(np.prod(shape))
    result = np.asarray(variables[cursor : cursor + size], dtype=object).reshape(shape)
    return result, cursor + size


def raw_coordinate_derivatives(
    first_weight: np.ndarray,
    hidden_weights: tuple[np.ndarray, ...],
    readout: np.ndarray,
    inputs: np.ndarray,
    channel: np.ndarray,
    activation_derivative,
) -> tuple[np.ndarray, DepthState, np.ndarray, float]:
    """Return exact ``(g,Dg,D^2g,D^3g)`` and the recovered scalarized state.

    The last returned scalar is the literal frozen-line third derivative
    ``n^3 T[p,p,p]``.  It is exposed only to make the moving-field distinction
    auditable.
    """

    first_weight = np.asarray(first_weight, dtype=np.float64)
    hidden_weights = tuple(np.asarray(weight, dtype=np.float64) for weight in hidden_weights)
    readout = np.asarray(readout, dtype=np.float64)
    inputs = np.asarray(inputs, dtype=np.float64)
    channel = np.asarray(channel, dtype=np.float64)
    if first_weight.ndim != 2:
        raise ValueError("first_weight must be a matrix")
    n, input_dimension = first_weight.shape
    if inputs.ndim != 2 or inputs.shape[0] != input_dimension:
        raise ValueError("inputs must have shape (input_dimension, batch)")
    batch = inputs.shape[1]
    if channel.shape != (batch,):
        raise ValueError(f"channel must have shape ({batch},)")
    if readout.shape != (n,):
        raise ValueError(f"readout must have shape ({n},)")
    if any(weight.shape != (n, n) for weight in hidden_weights):
        raise ValueError("every hidden weight must have shape (n,n)")
    hidden_layers = len(hidden_weights) + 1
    oracles = as_oracle_tuple(activation_derivative, hidden_layers)

    parameter_values = np.concatenate(
        (
            first_weight.ravel(),
            *(weight.ravel() for weight in hidden_weights),
            readout.ravel(),
        )
    )
    dimension = parameter_values.size
    variables = [
        Jet3.variable(value, dimension, index)
        for index, value in enumerate(parameter_values)
    ]
    cursor = 0
    first, cursor = _jet_matrix(variables, cursor, (n, input_dimension))
    middle = []
    for _ in hidden_weights:
        weight, cursor = _jet_matrix(variables, cursor, (n, n))
        middle.append(weight)
    a, cursor = _jet_matrix(variables, cursor, (n,))
    assert cursor == dimension

    z = np.empty((n, batch), dtype=object)
    for neuron in range(n):
        for sample in range(batch):
            total = Jet3.constant(0.0, dimension)
            for coordinate in range(input_dimension):
                total += first[neuron, coordinate] * (
                    inputs[coordinate, sample] / sqrt(input_dimension)
                )
            z[neuron, sample] = total

    h = np.empty_like(z)
    for layer, oracle in enumerate(oracles):
        for index in np.ndindex(z.shape):
            scalar = z[index]
            values = tuple(
                float(oracle(order, np.asarray(scalar.value))) for order in range(4)
            )
            h[index] = compose(scalar, values)
        if layer == hidden_layers - 1:
            break
        next_z = np.empty_like(z)
        for out_neuron in range(n):
            for sample in range(batch):
                total = Jet3.constant(0.0, dimension)
                for in_neuron in range(n):
                    total += middle[layer][out_neuron, in_neuron] * h[
                        in_neuron, sample
                    ] / sqrt(n)
                next_z[out_neuron, sample] = total
        z = next_z

    output = Jet3.constant(0.0, dimension)
    for neuron in range(n):
        for sample in range(batch):
            output += a[neuron] * h[neuron, sample] * (channel[sample] / n)

    p = output.gradient
    hp = output.hessian @ p
    p_h_p = float(p @ hp)
    third_contraction = float(np.einsum("ijk,i,j,k", output.third, p, p, p))
    derivatives = np.asarray(
        [
            output.value,
            n * float(p @ p),
            2.0 * n**2 * p_h_p,
            n**3 * (4.0 * float(hp @ hp) + 2.0 * third_contraction),
        ]
    )

    numeric_first_preactivation = first_weight @ inputs / sqrt(input_dimension)
    input_gram = inputs.T @ inputs / input_dimension
    state = DepthState(numeric_first_preactivation, hidden_weights, readout)
    frozen_third = n**3 * third_contraction
    return derivatives, state, input_gram, frozen_third
