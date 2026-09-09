"""Exact finite, equal-width MLP dynamics with the mean squared loss.

Inputs have shape (d, m). Stored hidden matrices act without an extra width
factor; output is readout @ last_hidden / n. First/readout blocks have
mobility n*kappa, while the other blocks have mobility kappa.
"""

from dataclasses import dataclass
from numbers import Integral, Real
from typing import Callable, Sequence

import numpy as np


def _array(value, name: str) -> np.ndarray:
    raw = np.asarray(value)
    if raw.dtype.kind not in "iuf":
        raise ValueError(f"{name} must contain real numbers")
    result = np.asarray(raw, dtype=np.float64)
    if not np.all(np.isfinite(result)):
        raise ValueError(f"{name} must be finite")
    return result


def _positive_integer(value, name: str) -> int:
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, Integral) or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return int(value)


def _scaled_product(*factors, addend=None):
    """Multiply a few finite factors without premature exponent-range loss.

    Optionally add a finite array before restoring the common exponent. This
    prevents a GD increment from overflowing before cancellation with a weight.
    Mantissa arithmetic still has ordinary float64 rounding.
    """
    arrays = np.broadcast_arrays(*[_array(f, "scaling factor") for f in factors])
    mantissa = np.ones_like(arrays[0])
    exponent = np.zeros(arrays[0].shape, dtype=np.int64)
    for factor in arrays:
        part, shift = np.frexp(factor)
        mantissa *= part
        exponent += shift
    with np.errstate(over="ignore", under="ignore", invalid="ignore"):
        if addend is not None:
            other, shift = np.frexp(_array(addend, "addend"))
            # Zero factors must not force scaling by an irrelevant exponent.
            exponent = np.where(mantissa == 0.0, 0, exponent)
            shift = np.where(other == 0.0, 0, shift)
            common = np.maximum(exponent, shift)
            mantissa = np.ldexp(mantissa, exponent - common) + np.ldexp(other, shift - common)
            exponent = common
        return np.ldexp(mantissa, exponent)


@dataclass(frozen=True)
class Activation:
    """A differentiable real function and derivative, both preserving shape.

    C2 activations meet the finite-flow regularity contract. This condition
    is the caller's responsibility for custom functions.
    """

    name: str
    value: Callable[[np.ndarray], np.ndarray]
    derivative: Callable[[np.ndarray], np.ndarray]

    def __post_init__(self):
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("activation name must be nonempty")
        if not callable(self.value) or not callable(self.derivative):
            raise TypeError("activation value and derivative must be callable")


def _tanh_derivative(z):
    # Avoid cancellation after tanh rounds to one, and premature squaring.
    with np.errstate(under="ignore"):
        u = np.exp(-np.abs(np.asarray(z, dtype=np.float64)))
        return (2.0 * u / (1.0 + u * u)) ** 2


def _arctan_derivative(z):
    x = np.abs(np.asarray(z, dtype=np.float64))
    result = np.empty_like(x)
    small = x <= 1.0
    result[small] = 1.0 / (1.0 + x[small] * x[small])
    with np.errstate(under="ignore"):
        u = 1.0 / x[~small]
        result[~small] = (u * u) / (1.0 + u * u)
    return result


TANH = Activation("tanh", np.tanh, _tanh_derivative)
ARCTAN = Activation("arctan", np.arctan, _arctan_derivative)
IDENTITY = Activation("identity", lambda z: z, np.ones_like)


@dataclass(frozen=True)
class Parameters:
    """Stored weights W1,...,WL and readout W(L+1).

    W1 is (n,d), every remaining matrix is (n,n), readout is (n,).
    Arrays are not implicitly copied; update functions return new arrays.
    The same structure represents a gradient or a velocity.
    """

    weights: tuple[np.ndarray, ...]
    readout: np.ndarray

    def __post_init__(self):
        object.__setattr__(self, "weights", tuple(
            _array(weight, f"weight {layer}")
            for layer, weight in enumerate(self.weights, 1)
        ))
        object.__setattr__(self, "readout", _array(self.readout, "readout"))
        self.validate()

    @property
    def depth(self) -> int:
        return len(self.weights)

    @property
    def width(self) -> int:
        return self.readout.size

    @property
    def input_dimension(self) -> int:
        return self.weights[0].shape[1]

    def validate(self) -> None:
        if not self.weights:
            raise ValueError("at least one hidden layer is required")
        if self.readout.ndim != 1 or self.readout.size < 1:
            raise ValueError("readout must be a nonempty vector")
        n = self.width
        first = self.weights[0]
        if first.ndim != 2 or first.shape[0] != n or first.shape[1] < 1:
            raise ValueError("first weight must have shape (n,d), with d positive")
        for layer, weight in enumerate(self.weights, 1):
            _array(weight, f"weight {layer}")
            if layer > 1 and weight.shape != (n, n):
                raise ValueError(f"weight {layer} must have shape ({n},{n})")
        _array(self.readout, "readout")


@dataclass(frozen=True)
class ForwardPass:
    """Per-layer (n,m) preactivations/activations and (m,) output."""

    preactivations: tuple[np.ndarray, ...]
    hidden: tuple[np.ndarray, ...]
    output: np.ndarray


def initialize(width: int, depth: int, input_dimension: int, *, seed: int) -> Parameters:
    """Independent Gaussian initialization in layer order, then readout.

    Variances: first weights 1, hidden weights 1/n, stored readout 1/n**2.
    An explicit nonnegative seed is required; the global RNG is untouched.
    """
    n = _positive_integer(width, "width")
    depth = _positive_integer(depth, "depth")
    d = _positive_integer(input_dimension, "input_dimension")
    if isinstance(seed, (bool, np.bool_)) or not isinstance(seed, Integral) or seed < 0:
        raise ValueError("seed must be a nonnegative integer")
    rng = np.random.default_rng(int(seed))
    weights = (rng.standard_normal((n, d)),) + tuple(
        rng.standard_normal((n, n)) / np.sqrt(n) for _ in range(depth - 1)
    )
    return Parameters(weights, rng.standard_normal(n) / n)


def _problem(parameters: Parameters, inputs, activation):
    if not isinstance(parameters, Parameters):
        raise TypeError("parameters must be Parameters")
    parameters.validate()
    x = _array(inputs, "inputs")
    if x.ndim != 2 or x.shape[0] != parameters.input_dimension or x.shape[1] < 1:
        raise ValueError("inputs must have shape (d,m), with m positive")
    if isinstance(activation, Activation):
        activations = (activation,) * parameters.depth
    else:
        if isinstance(activation, (str, bytes)) or not isinstance(activation, Sequence):
            raise TypeError("activation must be an Activation or a sequence of them")
        activations = tuple(activation)
        if len(activations) != parameters.depth:
            raise ValueError("provide exactly one activation per hidden layer")
        if not all(isinstance(item, Activation) for item in activations):
            raise TypeError("every layer activation must be an Activation")
    return x, activations


def _evaluate(function, z: np.ndarray, name: str) -> np.ndarray:
    # A custom callback may overwrite its argument or reuse an output buffer.
    value = _array(function(z.copy()), name)
    if value.shape != z.shape:
        raise ValueError(f"{name} must preserve the preactivation shape")
    return value.copy()


def _forward(parameters, x, activations) -> ForwardPass:
    preactivations, hidden = [], []
    h = x
    for layer, (weight, activation) in enumerate(zip(parameters.weights, activations)):
        z = weight @ h
        if layer == 0:
            z = z / np.sqrt(parameters.input_dimension)
        z = _array(z, "preactivation")
        h = _evaluate(activation.value, z, activation.name)
        preactivations.append(z)
        hidden.append(h)
    output = _array(parameters.readout @ h / parameters.width, "output")
    return ForwardPass(tuple(preactivations), tuple(hidden), output)


def forward(parameters: Parameters, inputs, activation=TANH) -> ForwardPass:
    """Evaluate the raw network, including x/sqrt(d) and readout/n.

    No normalization, whitening, clipping or Gram inversion is applied to
    the supplied samples. Unit input RMS is optional, not assumed.
    """
    x, activations = _problem(parameters, inputs, activation)
    return _forward(parameters, x, activations)


def _backward(parameters, fields, activations) -> tuple[np.ndarray, ...]:
    delta = [None] * parameters.depth
    propagated = parameters.readout[:, None]
    for layer in range(parameters.depth - 1, -1, -1):
        derivative = _evaluate(
            activations[layer].derivative, fields.preactivations[layer],
            activations[layer].name + " derivative",
        )
        delta[layer] = _array(derivative * propagated, "backward derivative")
        if layer:
            propagated = parameters.weights[layer].T @ delta[layer]
    return tuple(delta)


def backward(parameters: Parameters, inputs, activation=TANH) -> tuple[np.ndarray, ...]:
    """Return delta^(ell) = n * partial f / partial z^(ell), without residuals."""
    x, activations = _problem(parameters, inputs, activation)
    return _backward(parameters, _forward(parameters, x, activations), activations)


def _labels(labels, samples: int) -> np.ndarray:
    y = _array(labels, "labels")
    if y.shape != (samples,):
        raise ValueError("labels must have shape (m,)")
    return y


def _kappas(kappas, depth: int) -> np.ndarray:
    values = np.ones(depth + 1) if kappas is None else _array(kappas, "kappas")
    if values.shape != (depth + 1,) or np.any(values <= 0):
        raise ValueError("kappas must contain L+1 finite positive multipliers")
    return values


def loss(parameters: Parameters, inputs, labels, activation=TANH) -> float:
    """Mean squared loss sum((f-y)**2)/m, without a factor one-half."""
    fields = forward(parameters, inputs, activation)
    with np.errstate(over="ignore", invalid="ignore"):
        r = _array(fields.output - _labels(labels, fields.output.size), "residual")
        scale = float(np.max(np.abs(r)))
        if scale == 0.0:
            return 0.0
        mean_square = float(np.mean((r / scale) ** 2))
        result = (scale * mean_square) * scale
    if not np.isfinite(result):
        raise ValueError("loss is not representable as a finite float64")
    return result


def _loss_contractions(parameters, inputs, labels, activation):
    """Raw derivative contractions; scalar loss/width factors remain separate."""
    x, activations = _problem(parameters, inputs, activation)
    fields = _forward(parameters, x, activations)
    delta = _backward(parameters, fields, activations)
    r = _array(fields.output - _labels(labels, x.shape[1]), "residual")
    sources = (x,) + fields.hidden[:-1]
    raw = tuple(_array((d * r) @ source.T, "raw gradient contraction")
                for d, source in zip(delta, sources))
    return x.shape[1], raw + (_array(fields.hidden[-1] @ r, "raw readout contraction"),)


def loss_gradients(parameters: Parameters, inputs, labels, activation=TANH) -> Parameters:
    """Ordinary Euclidean/Frobenius gradients of the mean squared loss."""
    samples, raw = _loss_contractions(parameters, inputs, labels, activation)
    gradients = tuple(_scaled_product(2.0, 1.0 / samples, 1.0 / parameters.width,
                                      1.0 / np.sqrt(parameters.input_dimension) if layer == 0 else 1,
                                      value)
                      for layer, value in enumerate(raw))
    return Parameters(gradients[:-1], gradients[-1])


def _physical_blocks(parameters, samples, raw, rates, step=1.0, *, add_weights=False):
    # Endpoint mobility cancels the gradient's 1/n. Retain the remaining
    # normalizers with the raw contraction until the final magnitude is known.
    factors = (1.0 / np.sqrt(parameters.input_dimension),) + (
        1.0 / parameters.width,) * (parameters.depth - 1) + (1.0,)
    weights = parameters.weights + (parameters.readout,)
    scaled = tuple(_scaled_product(-2.0, step, rate, 1.0 / samples, factor, value,
                                    addend=weight if add_weights else None)
                   for rate, factor, value, weight in zip(rates, factors, raw, weights))
    return Parameters(scaled[:-1], scaled[-1])


def flow_velocity(parameters: Parameters, inputs, labels, activation=TANH, *, kappas=None) -> Parameters:
    """Exact physical gradient-flow RHS -D grad(loss), not a time integrator."""
    samples, raw = _loss_contractions(parameters, inputs, labels, activation)
    mobility = _kappas(kappas, parameters.depth)
    return _physical_blocks(parameters, samples, raw, mobility)


def gd_step(parameters: Parameters, inputs, labels, eta: float, activation=TANH, *, kappas=None) -> Parameters:
    """One simultaneous raw-parameter GD update, theta + eta * velocity.

    Every block uses the same pre-update state; inputs and parameters are
    unchanged. This is exact GD, not an exact finite-time flow solution.
    No loss-decrease guarantee is imposed for an arbitrary step size.
    """
    if isinstance(eta, (bool, np.bool_)) or not isinstance(eta, Real):
        raise ValueError("eta must be finite and nonnegative")
    try:
        eta = float(eta)
    except (ValueError, OverflowError) as error:
        raise ValueError("eta must be finite and nonnegative") from error
    if not np.isfinite(eta) or eta < 0:
        raise ValueError("eta must be finite and nonnegative")
    x, activations = _problem(parameters, inputs, activation)
    y = _labels(labels, x.shape[1])
    rates = _kappas(kappas, parameters.depth)
    if eta == 0.0:
        return Parameters(tuple(w.copy() for w in parameters.weights), parameters.readout.copy())
    samples, raw = _loss_contractions(parameters, x, y, activations)
    return _physical_blocks(parameters, samples, raw, rates, eta, add_weights=True)


def kernel_blocks(parameters: Parameters, inputs, activation=TANH, *, kappas=None) -> np.ndarray:
    """Return the L+1 mobility-weighted raw kernel blocks, shape (L+1,m,m)."""
    x, activations = _problem(parameters, inputs, activation)
    fields = _forward(parameters, x, activations)
    delta = _backward(parameters, fields, activations)
    rates = _kappas(kappas, parameters.depth)
    n = parameters.width
    blocks = [_scaled_product(rates[0], 1.0 / parameters.input_dimension, 1.0 / n,
                              x.T @ x, delta[0].T @ delta[0])]
    for layer in range(1, parameters.depth):
        h = fields.hidden[layer - 1]
        blocks.append(_scaled_product(rates[layer], 1.0 / n, 1.0 / n, h.T @ h,
                                       delta[layer].T @ delta[layer]))
    h = fields.hidden[-1]
    blocks.append(_scaled_product(rates[-1], 1.0 / n, h.T @ h))
    return _array(np.stack(blocks), "kernel blocks")


def kernel(parameters: Parameters, inputs, activation=TANH, *, kappas=None) -> np.ndarray:
    """Sum the raw kernel blocks; no residual or loss factor is included."""
    with np.errstate(over="ignore", invalid="ignore"):
        total = kernel_blocks(parameters, inputs, activation, kappas=kappas).sum(axis=0)
    return _array(total, "total kernel")
