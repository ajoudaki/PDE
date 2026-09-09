"""Moving physical gradient-flow Taylor coefficients for one sample, L=2.

The raw network, residual f-y, squared loss (without one-half), and block
mobilities (n*kappa_1, kappa_2, n*kappa_3) are those of finite_network.
This bounded oracle accepts an existing finite state; it draws no weights.
It propagates ordinary coefficients through order three in float64. The
real-arithmetic recurrence is exact, but numerical evaluation is neither
exact arithmetic nor a population law or a finite-time flow solver.
"""

from dataclasses import dataclass
from math import factorial
from numbers import Integral
from typing import Callable

import numpy as np

from .finite_network import (
    Parameters, _array, _evaluate, _kappas, _labels, _scaled_product,
)


DerivativeOracle = Callable[[int, np.ndarray], np.ndarray]


@dataclass(frozen=True)
class FlowJet:
    """Ordinary coefficients v[k] = (d/dt)^k v(0) / k!.

    parameter_coefficients[k] is a Parameters in the existing raw storage.
    Each of the two preactivation_coefficients and hidden_coefficients
    arrays has shape (order+1,n,1); output_coefficients is (order+1,1).
    Layer tuple positions 0,1 mean layers 1,2. The middle weight entry
    [i,j] maps first-layer neuron j to second-layer neuron i.
    All arrays are mutable and independent of inputs and callback buffers.
    """

    parameter_coefficients: tuple[Parameters, ...]
    preactivation_coefficients: tuple[np.ndarray, np.ndarray]
    hidden_coefficients: tuple[np.ndarray, np.ndarray]
    output_coefficients: np.ndarray

    @property
    def output_derivatives(self) -> np.ndarray:
        """Return a new finite array of physical-time output derivatives."""
        factors = np.array([factorial(k) for k in range(len(self.output_coefficients))])
        return _array(_scaled_product(factors[:, None], self.output_coefficients),
                      "output derivatives")


def _compose(derivatives, series, degree, shift=0):
    """Coefficient of phi(series), or phi'(series) when shift=1."""
    if degree == 0:
        return derivatives[shift]
    value = derivatives[shift + 1] * series[degree]
    if degree == 2:
        value = value + 0.5 * derivatives[shift + 2] * series[1] ** 2
    if degree == 3:
        value = (value + derivatives[shift + 2] * series[1] * series[2]
                 + derivatives[shift + 3] * series[1] ** 3 / 6.0)
    return _array(value, "activation jet coefficient")


def _convolve(left, right, degree, product):
    """Coefficient of a bilinear product, retaining every degree split."""
    value = product(left[0], right[degree])
    for index in range(1, degree + 1):
        value = value + product(left[index], right[degree - index])
    return _array(value, "jet contraction")


def flow_jet(parameters: Parameters, inputs, labels,
             activation_derivative: DerivativeOracle, *, order: int = 3,
             kappas=None) -> FlowJet:
    """Compute the moving physical GF jet at the supplied state, orders 0..3.

    Only two hidden layers and one sample are accepted. Inputs retain shape
    (d,1), labels shape (1,), and arbitrary finite inputs (including zero)
    are allowed. kappas is the finite API's positive length-three vector.
    Import this function from pde.finite_jets; no package re-export is needed.

    activation_derivative(j,z) supplies the j-th derivative of ONE shared
    scalar C3 activation, coordinatewise, with j=0 meaning its value. Only
    j=0,...,order are requested, at initial preactivations of shape (n,1).
    Real finite shape-preserving outputs are required; scalar broadcasting
    is rejected even at width one. Each invocation receives a private copy
    and its output is copied immediately. In-place callbacks and shared
    output buffers are supported. Callbacks must give consistent actual
    derivatives and must not mutate unrelated external calculation state;
    these semantic and regularity conditions are the caller's obligation.

    All weight blocks, the reused transpose, and the residual move. These
    are not frozen-direction derivatives or feature-time coefficients.
    Scalar mobility/normalization factors use the finite API's scaled
    multiplication. Raw products, sums and composition powers still use
    float64 and may overflow or underflow; nonfinite evaluated coefficients
    raise ValueError. No correct-rounding or extreme-range guarantee is made.
    Order zero validates arguments and evaluates only activation values.
    """
    if not isinstance(parameters, Parameters):
        raise TypeError("parameters must be Parameters")
    parameters.validate()
    if parameters.depth != 2:
        raise ValueError("flow_jet requires exactly two hidden layers")
    if (isinstance(order, (bool, np.bool_)) or not isinstance(order, Integral)
            or not 0 <= order <= 3):
        raise ValueError("order must be an integer between zero and three")
    order = int(order)
    if not callable(activation_derivative):
        raise TypeError("activation_derivative must be callable")
    x = _array(inputs, "inputs")
    if x.shape != (parameters.input_dimension, 1):
        raise ValueError("inputs must have shape (d,1)")
    x = x.copy()
    y = _labels(labels, 1).copy()
    rates = _kappas(kappas, 2).copy()
    n, d = parameters.width, parameters.input_dimension
    first = np.zeros((order + 1, n, d))
    middle = np.zeros((order + 1, n, n))
    readout = np.zeros((order + 1, n))
    first[0], middle[0] = parameters.weights
    readout[0] = parameters.readout
    z = tuple(np.zeros((order + 1, n, 1)) for _ in range(2))
    h = tuple(np.zeros_like(z[0]) for _ in range(2))
    # The terminal backward coefficient is unused: phi^(order+1) is not needed.
    phi_prime = tuple(np.zeros((order, n, 1)) for _ in range(2))
    delta = tuple(np.zeros_like(phi_prime[0]) for _ in range(2))
    propagated = np.zeros_like(phi_prime[0])
    residual_delta = np.zeros_like(phi_prime[0])
    output = np.zeros((order + 1, 1))
    residual = np.zeros_like(output)
    derivatives = [None, None]

    with np.errstate(over="ignore", invalid="ignore", under="ignore"):
        for k in range(order + 1):
            # Normalize only after the first raw matrix contraction.
            z[0][k] = _array((first[k] @ x) / np.sqrt(d), "first preactivation")
            for layer in range(2):
                if layer == 1:
                    z[1][k] = _convolve(middle, h[0], k, np.matmul)
                if k == 0:
                    derivatives[layer] = tuple(
                        _evaluate(lambda arg, j=j: activation_derivative(j, arg),
                                  z[layer][0], f"activation derivative {j}")
                        for j in range(order + 1)
                    )
                h[layer][k] = _compose(derivatives[layer], z[layer], k)
            output[k] = _array(_convolve(readout, h[1], k, np.matmul) / n,
                               "output coefficient")
            if k == order:
                break
            residual[k] = _array(output[k] - y if k == 0 else output[k],
                                 "residual coefficient")
            for layer in range(2):
                phi_prime[layer][k] = _compose(derivatives[layer], z[layer], k, 1)
            delta[1][k] = _convolve(readout[:, :, None], phi_prime[1], k, np.multiply)
            # The SAME moving W^(2), with indices transposed, is used here.
            propagated[k] = _convolve(middle, delta[1], k, lambda w, v: w.T @ v)
            delta[0][k] = _convolve(phi_prime[0], propagated, k, np.multiply)
            residual_delta[k] = _convolve(residual, delta[1], k, np.multiply)
            raw = (
                _array(_convolve(residual, delta[0], k, np.multiply) @ x.T,
                       "first raw contraction"),
                _convolve(residual_delta, h[0], k, lambda v, u: v @ u.T),
                _convolve(h[1], residual, k, np.matmul),
            )
            for target, contraction, rate, normalizer in zip(
                    (first, middle, readout), raw, rates, (1.0 / np.sqrt(d), 1.0 / n, 1.0)):
                target[k + 1] = _array(
                    _scaled_product(-2.0, rate, normalizer, 1.0 / (k + 1), contraction),
                    "parameter coefficient",
                )

    coefficients = tuple(Parameters((first[k], middle[k]), readout[k])
                         for k in range(order + 1))
    return FlowJet(coefficients, z, h, output)
