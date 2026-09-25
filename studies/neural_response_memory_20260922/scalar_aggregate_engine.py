"""Scalar derivative hierarchy for canonical bias-free tanh gradient flow.

Inputs are rows U_a=x_a/sqrt(d), supplied already normalized. Parameter blocks
are (first_weights, hidden_weights..., readout), with two or three hidden
layers, output c @ h / n, mean squared loss and mobilities (n,1,...,1,n).

Initialization uses network arrays only once. The resulting coefficient dict
and ScalarHierarchy contain only sample-indexed scalar tensors. In particular,
the runtime RHS neither retains nor reconstructs neuron populations or weights.

C[a,b,c] = D_c Theta[a,b], Q[a,b,c,d] = D_d D_c Theta[a,b],
where D_c = (B grad f_c) . grad. Derivative indices are ORDERED: they must not
be symmetrized. The highest retained tensor is frozen, an approximation to
canonical flow, not an exact aggregate closure or a proven convergent family.
"""

from dataclasses import dataclass
from numbers import Integral

import numpy as np


def _positive_integer(value, name):
    if isinstance(value, bool) or not isinstance(value, Integral) or value < 1:
        raise ValueError(name + " must be a positive integer")
    return int(value)


def _order(value):
    if isinstance(value, bool) or not isinstance(value, Integral) or value not in (2, 3, 4):
        raise ValueError("order must be 2, 3 or 4")
    return int(value)


def initialize_network(width, input_dim, depth=2, seed=20260920):
    """Draw w, internal matrices, c in that order using default_rng.

    Standard deviations are 1, 1/sqrt(n), and 1/n respectively; the stored
    readout receives the additional 1/n only in the prediction definition.
    """
    n = _positive_integer(width, "width")
    d = _positive_integer(input_dim, "input_dim")
    if isinstance(depth, bool) or not isinstance(depth, Integral) or depth not in (2, 3):
        raise ValueError("depth must be 2 or 3")
    if isinstance(seed, bool) or not isinstance(seed, Integral) or seed < 0:
        raise ValueError("seed must be a nonnegative integer")
    rng = np.random.default_rng(int(seed))
    return (rng.standard_normal((n, d)),
            *(rng.standard_normal((n, n)) / np.sqrt(n) for _ in range(depth - 1)),
            rng.standard_normal(n) / n)


def _validated_network(params, inputs):
    params = tuple(np.asarray(p, dtype=float) for p in params)
    if len(params) not in (3, 4):
        raise ValueError("two or three hidden layers required")
    if params[0].ndim != 2 or min(params[0].shape) < 1:
        raise ValueError("first weights must have shape (n,d), n,d positive")
    n, d = params[0].shape
    shapes = ((n, d), *((n, n) for _ in params[1:-1]), (n,))
    if any(p.shape != shape for p, shape in zip(params, shapes)):
        raise ValueError("parameter block shapes disagree")
    inputs = np.asarray(inputs, dtype=float)
    if inputs.ndim != 2 or inputs.shape[1] != d or len(inputs) < 1:
        raise ValueError("inputs must have shape (M,d), M positive")
    if not all(np.isfinite(p).all() for p in (*params, inputs)):
        raise ValueError("network parameters and inputs must be finite")
    return params, inputs


def _validated_direction(params, direction):
    direction = tuple(np.asarray(p, dtype=float) for p in direction)
    if len(direction) != len(params) or any(a.shape != b.shape for a, b in zip(params, direction)):
        raise ValueError("direction must match parameter block shapes")
    if not all(np.isfinite(p).all() for p in direction):
        raise ValueError("direction must be finite")
    return direction


def _sample(sample, count):
    if isinstance(sample, bool) or not isinstance(sample, Integral) or not 0 <= sample < count:
        raise ValueError("sample index out of range")
    return int(sample)


def _plain_fields(params, inputs):
    n = params[0].shape[0]
    h = []
    value = inputs.T
    for matrix in params[:-1]:
        value = np.tanh(matrix @ value)
        h.append(value)
    delta = [None] * len(h)
    delta[-1] = params[-1][:, None] * (1 - h[-1] ** 2)
    for layer in range(len(h) - 2, -1, -1):
        delta[layer] = (1 - h[layer] ** 2) * (params[layer + 1].T @ delta[layer + 1])
    theta = (inputs @ inputs.T) * (delta[0].T @ delta[0] / n)
    for layer in range(1, len(h)):
        theta += (h[layer - 1].T @ h[layer - 1] / n) * (delta[layer].T @ delta[layer] / n)
    theta += h[-1].T @ h[-1] / n
    return {"f": params[-1] @ h[-1] / n, "h": h, "delta": delta, "Theta": theta}


def network_fields(params, inputs):
    """Canonical predictions, n-by-M hidden/backward fields, and sample kernel."""
    return _plain_fields(*_validated_network(params, inputs))


def _direction_from_fields(fields, inputs, sample, n):
    h, delta = fields["h"], fields["delta"]
    return (np.outer(delta[0][:, sample], inputs[sample]),
            *(np.outer(delta[layer][:, sample], h[layer - 1][:, sample]) / n
              for layer in range(1, len(h))),
            h[-1][:, sample].copy())


def sample_direction(params, inputs, sample):
    """Return g_sample = B grad f_sample in physical parameter coordinates."""
    params, inputs = _validated_network(params, inputs)
    sample = _sample(sample, len(inputs))
    return _direction_from_fields(_plain_fields(params, inputs), inputs, sample, len(params[-1]))


def network_rhs(params, inputs, labels):
    """Canonical dense velocity, for explicit reference/check use only."""
    params, inputs = _validated_network(params, inputs)
    labels = np.asarray(labels, dtype=float)
    if labels.shape != (len(inputs),) or not np.isfinite(labels).all():
        raise ValueError("labels must be a finite M-vector")
    fields = _plain_fields(params, inputs)
    h, delta = fields["h"], fields["delta"]
    residual = fields["f"] - labels
    factor, n = -2 / len(inputs), len(params[-1])
    return (factor * (delta[0] * residual) @ inputs,
            *(factor / n * (delta[layer] * residual) @ h[layer - 1].T
              for layer in range(1, len(h))),
            factor * h[-1] @ residual)


def flatten_network(params):
    """Flatten parameter blocks for a separately constructed dense reference."""
    return np.concatenate([np.asarray(p, dtype=float).reshape(-1) for p in params])


def unflatten_network(state, shapes):
    """Parameter views for shapes=tuple(p.shape for p in params)."""
    state = np.asarray(state, dtype=float)
    shapes = tuple(tuple(shape) for shape in shapes)
    sizes = tuple(int(np.prod(shape)) for shape in shapes)
    if state.ndim != 1 or state.size != sum(sizes):
        raise ValueError("incorrect flat parameter size")
    result, start = [], 0
    for shape, size in zip(shapes, sizes):
        result.append(state[start:start + size].reshape(shape))
        start += size
    return tuple(result)


@dataclass(frozen=True)
class _Jet:
    """Coefficients of 1,s,t,st, with s^2=t^2=0; st has no factorial."""

    v: np.ndarray
    s: np.ndarray
    t: np.ndarray
    st: np.ndarray

    @classmethod
    def constant(cls, value):
        value = np.asarray(value, dtype=float)
        return cls(value, *(np.zeros_like(value) for _ in range(3)))

    def __add__(self, other):
        other = other if isinstance(other, _Jet) else _Jet.constant(other)
        return _Jet(*(a + b for a, b in zip(self.parts(), other.parts())))

    __radd__ = __add__

    def __neg__(self):
        return _Jet(*(-a for a in self.parts()))

    def __sub__(self, other):
        return self + (-other if isinstance(other, _Jet) else -np.asarray(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        other = other if isinstance(other, _Jet) else _Jet.constant(other)
        a, b = self, other
        return _Jet(a.v * b.v, a.s * b.v + a.v * b.s,
                    a.t * b.v + a.v * b.t,
                    a.st * b.v + a.s * b.t + a.t * b.s + a.v * b.st)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        if not np.isscalar(scalar) or scalar == 0:
            raise ValueError("jets only divide by nonzero fixed scalars")
        return _Jet(*(a / scalar for a in self.parts()))

    def __matmul__(self, other):
        other = other if isinstance(other, _Jet) else _Jet.constant(other)
        a, b = self, other
        return _Jet(a.v @ b.v, a.s @ b.v + a.v @ b.s,
                    a.t @ b.v + a.v @ b.t,
                    a.st @ b.v + a.s @ b.t + a.t @ b.s + a.v @ b.st)

    @property
    def T(self):
        return _Jet(*(a.T for a in self.parts()))

    def __getitem__(self, index):
        return _Jet(*(a[index] for a in self.parts()))

    def parts(self):
        return self.v, self.s, self.t, self.st

    def tanh(self):
        h = np.tanh(self.v)
        derivative = 1 - h * h
        return _Jet(h, derivative * self.s, derivative * self.t,
                    derivative * self.st - 2 * h * derivative * self.s * self.t)


def _parameter_jets(params, s=None, t=None, st=None):
    zeros = tuple(np.zeros_like(p) for p in params)
    return tuple(_Jet(*items) for items in zip(params, s or zeros, t or zeros, st or zeros))


def _jet_fields(params, inputs):
    n = params[0].v.shape[0]
    h = []
    value = _Jet.constant(inputs.T)
    for matrix in params[:-1]:
        value = (matrix @ value).tanh()
        h.append(value)
    delta = [None] * len(h)
    delta[-1] = params[-1][:, None] * (1 - h[-1] * h[-1])
    for layer in range(len(h) - 2, -1, -1):
        delta[layer] = (1 - h[layer] * h[layer]) * (params[layer + 1].T @ delta[layer + 1])
    theta = _Jet.constant(inputs @ inputs.T) * (delta[0].T @ delta[0] / n)
    for layer in range(1, len(h)):
        theta = theta + (h[layer - 1].T @ h[layer - 1] / n) * (delta[layer].T @ delta[layer] / n)
    theta = theta + h[-1].T @ h[-1] / n
    return {"f": params[-1] @ h[-1] / n, "h": h, "delta": delta, "Theta": theta}


def _direction_derivative_from_jets(fields, inputs, sample, n):
    h, delta = fields["h"], fields["delta"]
    return (np.outer(delta[0].s[:, sample], inputs[sample]),
            *((np.outer(delta[layer].s[:, sample], h[layer - 1].v[:, sample])
               + np.outer(delta[layer].v[:, sample], h[layer - 1].s[:, sample])) / n
              for layer in range(1, len(h))),
            h[-1].s[:, sample].copy())


def direction_derivative(params, inputs, sample, direction):
    """Return Dg_sample[direction], including all forward/backward dependence."""
    params, inputs = _validated_network(params, inputs)
    sample = _sample(sample, len(inputs))
    direction = _validated_direction(params, direction)
    fields = _jet_fields(_parameter_jets(params, s=direction), inputs)
    return _direction_derivative_from_jets(fields, inputs, sample, len(params[-1]))


def initialize_coefficients(params, inputs, order=4):
    """Compute the scalar tensors with analytic directional jets, once.

    For Q[:,:,c,d], the parameter jet is
    theta+s*g_c+t*g_d+st*Dg_c[g_d]. Its st coefficient includes the
    moving-direction term required by D_d(D_c Theta). This routine never
    forms a parameter Hessian, and its return value contains no parameters,
    neuron fields, input vectors, callbacks or hidden initialization state.
    """
    order = _order(order)
    params, inputs = _validated_network(params, inputs)
    m, n = len(inputs), len(params[-1])
    base = _plain_fields(params, inputs)
    result = {"f": base["f"].copy(), "Theta": base["Theta"].copy()}
    if order == 2:
        return result
    result["C"] = np.empty((m, m, m), dtype=float)
    for c in range(m):
        gc = _direction_from_fields(base, inputs, c, n)
        result["C"][:, :, c] = _jet_fields(_parameter_jets(params, s=gc), inputs)["Theta"].s
    if order == 3:
        return result
    result["Q"] = np.empty((m, m, m, m), dtype=float)
    for d in range(m):
        gd = _direction_from_fields(base, inputs, d, n)
        directional_fields = _jet_fields(_parameter_jets(params, s=gd), inputs)
        for c in range(m):
            gc = _direction_from_fields(base, inputs, c, n)
            moving_gc = _direction_derivative_from_jets(directional_fields, inputs, c, n)
            theta_jet = _jet_fields(_parameter_jets(params, s=gc, t=gd, st=moving_gc), inputs)["Theta"]
            result["Q"][:, :, c, d] = theta_jet.st
    return result


class ScalarHierarchy:
    """Autonomous sample-indexed tensors only; directly compatible with solve_ivp.

    Order 2 freezes Theta, order 3 freezes C, and order 4 freezes Q. This
    terminal tensor is stored outside the moving state. Thus the moving
    blocks are f; (f,Theta); or (f,Theta,C), respectively.
    The initial state is retained as scalar storage for initial_state(); no
    runtime method consults the network or reinitializes coefficients.
    """

    def __init__(self, coefficients, labels, order=4):
        self.order = _order(order)
        self.labels = np.array(labels, dtype=float, copy=True)
        if self.labels.ndim != 1 or len(self.labels) < 1 or not np.isfinite(self.labels).all():
            raise ValueError("labels must be a finite nonempty vector")
        self.labels.setflags(write=False)
        self.M = len(self.labels)
        self.all_names = ("f", "Theta", "C", "Q")[:self.order]
        self.names = self.all_names[:-1]
        self.terminal_name = self.all_names[-1]
        self.terminal = np.array(coefficients[self.terminal_name], dtype=float, copy=True)
        if self.terminal.shape != (self.M,) * self.order or not np.isfinite(self.terminal).all():
            raise ValueError("invalid terminal scalar tensor " + self.terminal_name)
        self.terminal.setflags(write=False)
        self.shapes = {name: (self.M,) * degree for degree, name in enumerate(self.names, 1)}
        self.slices = {}
        start = 0
        for name in self.names:
            stop = start + self.M ** len(self.shapes[name])
            self.slices[name] = slice(start, stop)
            start = stop
        self.size = start
        self._initial = self.pack(coefficients)

    def pack(self, tensors):
        """Pack the requested order; higher-order keys, if present, are ignored."""
        values = []
        for name in self.names:
            value = np.asarray(tensors[name], dtype=float)
            if value.shape != self.shapes[name] or not np.isfinite(value).all():
                raise ValueError("invalid scalar tensor " + name)
            values.append(value.reshape(-1))
        return np.concatenate(values)

    def unpack(self, state):
        """Return sample-tensor views of a flat scalar state, without mutation."""
        state = np.asarray(state, dtype=float)
        if state.shape != (self.size,):
            raise ValueError("incorrect scalar state size")
        return {name: state[self.slices[name]].reshape(self.shapes[name]) for name in self.names}

    def initial_state(self):
        return self._initial.copy()

    def tensors(self, state):
        """All current scalar tensors, including the fixed terminal tensor."""
        result = self.unpack(state)
        result[self.terminal_name] = self.terminal
        return result

    def rhs(self, time, state):
        """No explicit time dependence; terminal coefficient derivative is zero."""
        values = self.tensors(state)
        residual = values["f"] - self.labels
        result = np.zeros(self.size, dtype=float)
        factor = -2 / self.M
        for name, next_name in zip(self.all_names[:-1], self.all_names[1:]):
            derivative = factor * np.tensordot(values[next_name], residual, axes=([-1], [0]))
            result[self.slices[name]] = derivative.reshape(-1)
        return result

    def counts(self):
        """Explicit moving state and stored initialization/label scalar counts."""
        return {"samples": self.M, "order": self.order,
                "state_scalars": self.size,
                "tensor_scalars": {name: self.M ** len(shape) for name, shape in self.shapes.items()},
                "terminal_scalars": self.terminal.size,
                "aggregate_scalars": self.size + self.terminal.size,
                "stored_initial_scalars": self._initial.size,
                "label_scalars": self.labels.size,
                "engine_array_scalars": self._initial.size + self.labels.size + self.terminal.size,
                "neuron_scalars": 0, "network_parameter_scalars": 0}
