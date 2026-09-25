"""Passive circle readouts for the scalar hierarchy, with no probe feedback.

Inputs have the original engine's normalization and are never rescaled here.
Probe tensors have shapes (N,), (N,M), (N,M,M), and (N,M,M,M). Only the M
training samples define parameter directions. Neuron arrays exist solely in
initialization and explicitly requested dense reference evaluation.
"""

from numbers import Integral

import numpy as np

import scalar_aggregate_engine as aggregate


def _fields(params, inputs):
    """Forward/backward fields, deliberately without any square sample kernel."""
    jet = isinstance(params[0], aggregate._Jet)
    value = aggregate._Jet.constant(inputs.T) if jet else inputs.T
    h = []
    for matrix in params[:-1]:
        value = matrix @ value
        value = value.tanh() if jet else np.tanh(value)
        h.append(value)
    delta = [None] * len(h)
    delta[-1] = params[-1][:, None] * (1 - h[-1] * h[-1])
    for layer in range(len(h) - 2, -1, -1):
        delta[layer] = (1 - h[layer] * h[layer]) * (params[layer + 1].T @ delta[layer + 1])
    n = params[0].v.shape[0] if jet else params[0].shape[0]
    return {"h": h, "delta": delta, "f": params[-1] @ h[-1] / n}


def _cross_kernel(probe, train, probe_inputs, train_inputs, n):
    """Rectangular N-by-M kernel, equally valid for ordinary arrays and jets."""
    theta = (probe["delta"][0].T @ train["delta"][0] / n) * (probe_inputs @ train_inputs.T)
    for layer in range(1, len(train["h"])):
        theta = theta + (probe["h"][layer - 1].T @ train["h"][layer - 1] / n) * (
            probe["delta"][layer].T @ train["delta"][layer] / n)
    return theta + probe["h"][-1].T @ train["h"][-1] / n


def forward_only(params, probe_inputs):
    """Dense-reference outputs without backward fields or a probe Gram matrix."""
    params, probe_inputs = aggregate._validated_network(params, probe_inputs)
    value = probe_inputs.T
    for matrix in params[:-1]:
        value = np.tanh(matrix @ value)
    return params[-1] @ value / len(params[-1])


def initialize_probe_coefficients(params, train_inputs, probe_inputs, order=4):
    """Initialize passive scalar tensors using training directions only.

    Q[q,b,c,d] is D_d(D_c Theta[q,b]), including Dg_c[g_d]. The mixed
    parameter jet has coefficients (theta, g_c, g_d, Dg_c[g_d]); the last
    component is essential. No N-by-N kernel or probe-direction tensor is
    formed. Temporary neuron fields and parameter directions are discarded.
    """
    order = aggregate._order(order)
    params, train_inputs = aggregate._validated_network(params, train_inputs)
    _, probe_inputs = aggregate._validated_network(params, probe_inputs)
    m, n, count = len(train_inputs), len(params[-1]), len(probe_inputs)
    train, probe = _fields(params, train_inputs), _fields(params, probe_inputs)
    result = {"f": probe["f"].copy(),
              "Theta": _cross_kernel(probe, train, probe_inputs, train_inputs, n)}
    if order == 2:
        return result
    result["C"] = np.empty((count, m, m))
    if order == 3:
        for c in range(m):
            gc = aggregate._direction_from_fields(train, train_inputs, c, n)
            jets = aggregate._parameter_jets(params, s=gc)
            result["C"][:, :, c] = _cross_kernel(
                _fields(jets, probe_inputs), _fields(jets, train_inputs),
                probe_inputs, train_inputs, n).s
        return result
    result["Q"] = np.empty((count, m, m, m))
    for d in range(m):
        gd = aggregate._direction_from_fields(train, train_inputs, d, n)
        directional_train = _fields(aggregate._parameter_jets(params, s=gd), train_inputs)
        for c in range(m):
            gc = aggregate._direction_from_fields(train, train_inputs, c, n)
            moving_gc = aggregate._direction_derivative_from_jets(directional_train, train_inputs, c, n)
            jets = aggregate._parameter_jets(params, s=gc, t=gd, st=moving_gc)
            theta = _cross_kernel(_fields(jets, probe_inputs), _fields(jets, train_inputs),
                                  probe_inputs, train_inputs, n)
            result["Q"][:, :, c, d] = theta.st
            if d == 0:
                result["C"][:, :, c] = theta.s
    return result


class SignatureHierarchy:
    """Existing training hierarchy plus z, I and J, driven only by its residuals.

    z'_b=-2(f_b-y_b)/M, I'_bc=z_c z'_b, J'_bcd=I_cd z'_b.
    Order two retains z, order three z/I, and order four z/I/J. Flat states
    start with the unmodified ScalarHierarchy state. All runtime storage and
    contractions are independent of network width and number of probe points.
    """

    def __init__(self, coefficients, labels, order=4):
        self.training = aggregate.ScalarHierarchy(coefficients, labels, order)
        self.order, self.M = self.training.order, self.training.M
        self.labels = self.training.labels
        self.training_size = self.training.size
        self.signature_names = ("z", "I", "J")[:self.order - 1]
        self.signature_shapes = {name: (self.M,) * degree
                                 for degree, name in enumerate(self.signature_names, 1)}
        self.signature_slices = {}
        start = self.training_size
        for name, shape in self.signature_shapes.items():
            stop = start + int(np.prod(shape))
            self.signature_slices[name] = slice(start, stop)
            start = stop
        self.size = start

    def _state(self, state):
        state = np.asarray(state, dtype=float)
        if state.shape != (self.size,):
            raise ValueError("incorrect signature state size")
        return state

    def training_state(self, state):
        """View of the unchanged training engine's moving state."""
        return self._state(state)[:self.training_size]

    def signatures(self, state):
        state = self._state(state)
        return {name: state[self.signature_slices[name]].reshape(shape)
                for name, shape in self.signature_shapes.items()}

    def unpack(self, state):
        """All training tensors (including the frozen tensor) and signatures."""
        return {**self.training.tensors(self.training_state(state)), **self.signatures(state)}

    def initial_state(self):
        return np.concatenate((self.training.initial_state(),
                               np.zeros(self.size - self.training_size)))

    def rhs(self, time, state):
        state = self._state(state)
        training_state, sig = self.training_state(state), self.signatures(state)
        velocity = -2 / self.M * (self.training.unpack(training_state)["f"] - self.labels)
        result = np.empty(self.size)
        result[:self.training_size] = self.training.rhs(time, training_state)
        result[self.signature_slices["z"]] = velocity
        if self.order >= 3:
            result[self.signature_slices["I"]] = np.outer(velocity, sig["z"]).reshape(-1)
        if self.order >= 4:
            result[self.signature_slices["J"]] = (velocity[:, None, None] * sig["I"]).reshape(-1)
        return result

    __call__ = rhs

    def readout(self, coefficients, state):
        """Read passive outputs or complex Fourier modes from scalar coefficients.

        The first coefficient axis may be probe points or Fourier modes. No
        probe coefficient is stored by the dynamical system. Complex inputs
        stay complex, allowing Fourier compression before the final readout.
        """
        sig = self.signatures(state)
        result = np.array(coefficients["f"], copy=True)
        if result.ndim != 1:
            raise ValueError("passive f must have one probe or Fourier axis")
        count = len(result)
        for degree, (name, signature) in enumerate(
                zip(("Theta", "C", "Q"), self.signature_names), 1):
            value = np.asarray(coefficients[name])
            if value.shape != (count,) + (self.M,) * degree:
                raise ValueError("invalid passive coefficient " + name)
            axes = tuple(range(1, degree + 1))
            result = result + np.tensordot(value, sig[signature], axes=(axes, tuple(range(degree))))
        return result


def fit_fourier(values, max_mode):
    """Uniform theta_j=2*pi*j/N samples to normalized complex modes 0..K.

    For real values, evaluation is F_0 + 2 Re(sum_{k=1}^K F_k exp(ik theta)).
    Require 2*K<N so that every retained nonconstant mode has its distinct
    negative-frequency partner; a Nyquist mode is deliberately unsupported.
    Trailing scalar-tensor axes are preserved. Stored size depends on K and
    those axes, never on width, training steps or the sampled grid size N.
    """
    values = np.asarray(values)
    if values.ndim < 1 or len(values) < 1 or np.iscomplexobj(values) or not np.isfinite(values).all():
        raise ValueError("Fourier samples must be finite real arrays with a nonempty first axis")
    if isinstance(max_mode, bool) or not isinstance(max_mode, Integral) or not 0 <= 2 * max_mode < len(values):
        raise ValueError("max_mode must be a nonnegative integer with 2*max_mode<N")
    return (np.fft.rfft(values, axis=0)[:int(max_mode) + 1] / len(values)).copy()


def evaluate_fourier(modes, angles):
    """Evaluate real Fourier series; output shape is angles.shape+modes.shape[1:]."""
    modes, angles = np.asarray(modes), np.asarray(angles, dtype=float)
    if modes.ndim < 1 or len(modes) < 1 or not np.isfinite(modes).all() or not np.isfinite(angles).all():
        raise ValueError("Fourier modes and angles must be finite, with at least a constant mode")
    phase = np.exp(1j * np.multiply.outer(angles, np.arange(1, len(modes))))
    return modes[0].real + 2 * np.tensordot(phase, modes[1:], axes=([-1], [0])).real


def fit_fourier_coefficients(coefficients, max_mode):
    """Apply fit_fourier to each initialized passive scalar tensor."""
    return {name: fit_fourier(value, max_mode) for name, value in coefficients.items()}


def evaluate_fourier_coefficients(coefficients, angles):
    """Evaluate each Fourier coefficient tensor at requested angles."""
    return {name: evaluate_fourier(value, angles) for name, value in coefficients.items()}
