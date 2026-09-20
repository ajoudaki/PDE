"""Study-owned finite-depth observable closure with exact working-state restart.

Population quadrature rows remain distinct for every hidden layer. An edge's
feature matrix and its transpose are the two directions of the same action.
This finite implementation does not certify hierarchy or training convergence.
"""
from dataclasses import dataclass, field
from decimal import Decimal
import json
from pathlib import Path
import sys

import numpy as np

from pde.observable_arithmetic import Arithmetic
from pde.observable_fixed import Fixed
from depth_initialization import initialize as initialize_marks


def _positive_integer(value, name):
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(name + " must be a positive integer")
    return value


def _tolerance(ar):
    return ar.real("2e-12" if ar.digits is None else "1e-" + str(ar.digits-5))


def _probabilities(values, count, ar, *, strictly_positive=False):
    values = ar.array(values)
    if (values.shape != (count,) or not ar.finite(values)
            or any(x <= 0 if strictly_positive else x < 0 for x in values)):
        raise ValueError("invalid probability vector")
    total = sum(values, ar.real(0))
    if total <= 0 or abs(total-1) > _tolerance(ar)*count:
        raise ValueError("probabilities must have unit positive mass")
    return values


def _unit_inputs(values, ar, dimension=None):
    values = ar.array(values)
    if (values.ndim != 2 or min(values.shape) < 1
            or (dimension is not None and values.shape[1] != dimension)):
        raise ValueError("inputs must have nonempty shape (samples,input_dimension)")
    # A fixed-dimensional dot product accumulates one rounding error per term.
    if not ar.finite(values) or any(abs(v-1) > _tolerance(ar)*values.shape[1]
                                  for v in np.sum(values*values, axis=1)):
        raise ValueError("inputs must lie on the unit sphere at working precision")
    return values


@dataclass
class DataLaw:
    inputs: np.ndarray
    labels: np.ndarray
    probabilities: np.ndarray
    metadata: dict = field(default_factory=dict)

    def validate(self, ar, dimension=None):
        with ar.context():
            self.inputs = _unit_inputs(self.inputs, ar, dimension)
            self.labels = ar.array(self.labels)
            if self.labels.shape != (len(self.inputs),) or not ar.finite(self.labels):
                raise ValueError("labels must be a finite vector matching inputs")
            self.probabilities = _probabilities(self.probabilities, len(self.inputs), ar,
                                               strictly_positive=True)
        return self


@dataclass
class State:
    b: list
    pi: list
    g: np.ndarray
    w: np.ndarray
    c: np.ndarray
    M: list
    D: list
    arithmetic: Arithmetic
    metadata: dict = field(default_factory=dict)

    @property
    def depth(self):
        return len(self.b)

    @property
    def dimension(self):
        return self.g.shape[1]

    def validate(self):
        ar = self.arithmetic
        if not isinstance(ar, Arithmetic):
            raise ValueError("state requires an Arithmetic backend")
        if (not all(isinstance(v, (list, tuple)) for v in (self.b, self.pi, self.M, self.D))
                or self.depth < 2 or len(self.pi) != self.depth
                or len(self.M) != self.depth-1 or len(self.D) != self.depth-1):
            raise ValueError("one population per layer and one matrix per adjacent edge required")
        arrays = list(self.b)+list(self.pi)+list(self.M)+list(self.D)+[self.g, self.w, self.c]
        if not all(isinstance(v, np.ndarray) and ar.finite(v) for v in arrays):
            raise ValueError("state arrays must be finite")
        if any(v.ndim != 2 or min(v.shape) < 1 for v in self.b):
            raise ValueError("feature tables must be nonempty matrices")
        if (self.g.ndim != 2 or self.g.shape[0] != len(self.b[0]) or self.g.shape[1] < 1
                or self.w.shape != self.g.shape or self.c.shape != (len(self.b[-1]),)):
            raise ValueError("invalid retained first rows or readout")
        with ar.context():
            for l, weights in enumerate(self.pi):
                _probabilities(weights, len(self.b[l]), ar)
            for l, (matrix, initial) in enumerate(zip(self.M, self.D)):
                expected = (self.b[l+1].shape[1], self.b[l].shape[1])
                if matrix.shape != expected or initial.shape != expected:
                    raise ValueError("M and D must index adjacent retained feature spaces")
        return self

    def copy(self):
        return State([v.copy() for v in self.b], [v.copy() for v in self.pi],
                     self.g.copy(), self.w.copy(), self.c.copy(),
                     [v.copy() for v in self.M], [v.copy() for v in self.D],
                     self.arithmetic, json.loads(json.dumps(self.metadata, allow_nan=False)))

    def dynamic_copy(self, w, c, M):
        """Stage state shares frozen marks and changes all dynamic blocks together."""
        return State(self.b, self.pi, self.g, w, c, M, self.D, self.arithmetic, self.metadata)


def from_initialization(initial):
    """Consume only the initializer's retained joint marks and contractions."""
    ar = initial["arithmetic"]
    return State([v.copy() for v in initial["b"]], [v.copy() for v in initial["pi"]],
                 initial["g"].copy(), initial["g"].copy(), ar.zeros(len(initial["b"][-1])),
                 [v.copy() for v in initial["D"]], [v.copy() for v in initial["D"]], ar,
                 json.loads(json.dumps(initial.get("metadata", {}), allow_nan=False))).validate()


def initialize(order=1, depth=3, dimension=2, **kwargs):
    return from_initialization(initialize_marks(order, depth, dimension, **kwargs))


def apply_action(state, edge, values, *, transpose=False, initial=False):
    """Apply edge 2..L to a source-population vector or column panel.

    Edge ell maps population ell-1 to ell; transpose=True uses its actual
    weighted adjoint. initial=True chooses the retained initial contraction D.
    """
    state.validate()
    _positive_integer(edge, "edge")
    if not 2 <= edge <= state.depth:
        raise ValueError("edge must be in 2..depth")
    if not isinstance(transpose, bool) or not isinstance(initial, bool):
        raise ValueError("transpose and initial must be booleans")
    source, target = (edge-1, edge-2) if transpose else (edge-2, edge-1)
    ar = state.arithmetic
    with ar.context():
        values = ar.array(values)
        if (values.ndim not in (1, 2) or len(values) != len(state.b[source])
                or (values.ndim == 2 and values.shape[1] == 0) or not ar.finite(values)):
            raise ValueError("action values must be a vector or nonempty panel in the source population")
        matrix = (state.D if initial else state.M)[edge-2]
        if transpose:
            matrix = matrix.T
        weights = state.pi[source] if values.ndim == 1 else state.pi[source][:, None]
        result = state.b[target] @ (matrix @ (state.b[source].T @ (weights*values)))
        if not ar.finite(result):
            raise ValueError("nonfinite action result")
        return result


def _fields(state, inputs, backward=True):
    ar = state.arithmetic
    z = [state.w @ inputs.T]
    h = [ar.tanh(z[0])]
    a = [state.b[0].T @ (state.pi[0][:, None]*h[0])]
    for l in range(1, state.depth):
        z.append(state.b[l] @ (state.M[l-1] @ a[l-1]))
        h.append(ar.tanh(z[l]))
        a.append(state.b[l].T @ (state.pi[l][:, None]*h[l]))
    result = dict(z=z, h=h, a=a, f=state.pi[-1] @ (state.c[:, None]*h[-1]))
    if backward:
        delta, d, p = [None]*state.depth, [None]*state.depth, [None]*(state.depth-1)
        delta[-1] = state.c[:, None]*(1-h[-1]*h[-1])
        for l in range(state.depth-1, -1, -1):
            d[l] = state.b[l].T @ (state.pi[l][:, None]*delta[l])
            if l:
                p[l-1] = state.b[l-1] @ (state.M[l-1].T @ d[l])
                delta[l-1] = (1-h[l-1]*h[l-1])*p[l-1]
        result.update(delta=delta, d=d, p=p)
    return result


def fields(state, inputs, backward=True):
    """Arrays have shape (population_nodes,samples), or (features,samples)."""
    state.validate()
    ar = state.arithmetic
    with ar.context():
        result = _fields(state, _unit_inputs(inputs, ar, state.dimension), backward)
        values = [result["f"]]+sum((result[k] for k in ("z", "h", "a")), [])
        if backward:
            values += result["delta"]+result["d"]+result["p"]
        if not all(ar.finite(v) for v in values):
            raise ValueError("nonfinite field")
        return result


def predict(state, inputs, *, block_size=16):
    _positive_integer(block_size, "block_size")
    state.validate()
    ar = state.arithmetic
    with ar.context():
        inputs = _unit_inputs(inputs, ar, state.dimension)
        result = ar.zeros(len(inputs))
        for start in range(0, len(inputs), block_size):
            stop = min(start+block_size, len(inputs))
            result[start:stop] = _fields(state, inputs[start:stop], False)["f"]
        if not ar.finite(result):
            raise ValueError("nonfinite prediction")
        return result


def rhs(state, data, *, block_size=16):
    """Return (w velocity, readout velocity, list of edge-matrix velocities)."""
    _positive_integer(block_size, "block_size")
    state.validate()
    ar = state.arithmetic
    with ar.context():
        data.validate(ar, state.dimension)
        vw, vc, vM = ar.zeros(state.w.shape), ar.zeros(state.c.shape), [ar.zeros(v.shape) for v in state.M]
        for start in range(0, len(data.inputs), block_size):
            stop = min(start+block_size, len(data.inputs))
            u = data.inputs[start:stop]
            value = _fields(state, u)
            r = data.probabilities[start:stop]*(value["f"]-data.labels[start:stop])
            vw -= 2*(value["delta"][0]*r) @ u
            vc -= 2*value["h"][-1] @ r
            for l in range(state.depth-1):
                vM[l] -= 2*(value["d"][l+1]*r) @ value["a"][l].T
        if not all(ar.finite(v) for v in [vw, vc]+vM):
            raise ValueError("nonfinite velocity")
        return vw, vc, vM


def evolve(state, data, *, steps, step_size, block_size=16):
    """Simultaneous explicit Heun; retain no history, stage tape, or clock."""
    _positive_integer(steps, "steps")
    ar = state.arithmetic
    current = state.copy().validate()
    with ar.context():
        h = ar.real(step_size)
        if h <= 0:
            raise ValueError("step_size must be positive")
        for _ in range(steps):
            k = rhs(current, data, block_size=block_size)
            stage = current.dynamic_copy(current.w+h*k[0], current.c+h*k[1],
                                         [v+h*dv for v, dv in zip(current.M, k[2])])
            q = rhs(stage, data, block_size=block_size)
            current = current.dynamic_copy(current.w+(h/2)*(k[0]+q[0]),
                                            current.c+(h/2)*(k[1]+q[1]),
                                            [v+(h/2)*(dv+dw) for v, dv, dw in zip(current.M, k[2], q[2])])
            current.validate()
    return current


def interpolate_state(left, right, fraction):
    left.validate()
    right.validate()
    ar = left.arithmetic
    if (ar.digits, ar.backend) != (right.arithmetic.digits, right.arithmetic.backend):
        raise ValueError("interpolation requires identical arithmetic")
    if left.depth != right.depth or not np.array_equal(left.g, right.g):
        raise ValueError("interpolation requires identical frozen marks")
    for group in ("b", "pi", "D"):
        if any(not np.array_equal(a, b) for a, b in zip(getattr(left, group), getattr(right, group))):
            raise ValueError("interpolation requires identical frozen marks")
    with ar.context():
        q = ar.real(fraction)
        if not 0 <= q <= 1:
            raise ValueError("interpolation fraction must lie in [0,1]")
        return left.dynamic_copy((1-q)*left.w+q*right.w, (1-q)*left.c+q*right.c,
                                 [(1-q)*a+q*b for a, b in zip(left.M, right.M)]).validate()


def paired_observations(state, data, *, block_size=16, include_pairs=True):
    """Same-row initial/current activations at every layer, with joint weights."""
    _positive_integer(block_size, "block_size")
    state.validate()
    ar = state.arithmetic
    with ar.context():
        data.validate(ar, state.dimension)
        sums = [ar.real(0) for _ in state.b]
        pairs = ([ar.zeros((len(b), len(data.inputs), 2)) for b in state.b]
                 if include_pairs else [None]*state.depth)
        initial = state.dynamic_copy(state.g, ar.zeros(state.c.shape), state.D)
        for start in range(0, len(data.inputs), block_size):
            stop = min(start+block_size, len(data.inputs))
            u = data.inputs[start:stop]
            before, after = _fields(initial, u, False)["h"], _fields(state, u, False)["h"]
            for l in range(state.depth):
                sums[l] += state.pi[l] @ ((after[l]-before[l])**2) @ data.probabilities[start:stop]
                if include_pairs:
                    pairs[l][:, start:stop, 0] = before[l]
                    pairs[l][:, start:stop, 1] = after[l]
        return dict(pairs=pairs, population_weights=[p.copy() for p in state.pi],
                    input_weights=data.probabilities.copy(), inputs=data.inputs.copy(),
                    squared_motion=sums, rms=[ar.sqrt(s).item() for s in sums])


def loss(state, data, *, block_size=16):
    ar = state.arithmetic
    with ar.context():
        data.validate(ar, state.dimension)
        r = predict(state, data.inputs, block_size=block_size)-data.labels
        return data.probabilities @ (r*r)


def _array_bytes(arrays):
    size = 0
    for a in arrays:
        size += a.nbytes
        if a.dtype == object:
            size += sum(sys.getsizeof(v) for v in a.flat)
            size += sum(sys.getsizeof(v.units)+sys.getsizeof(v.scale) for v in a.flat if isinstance(v, Fixed))
    return size


def state_bytes(state, data=None):
    """Retained array bytes incl. scalar objects; metadata and data accounted separately."""
    result = dict(arrays=_array_bytes(list(state.b)+list(state.pi)+list(state.M)+list(state.D)+[state.g, state.w, state.c]),
                  metadata_utf8=len(json.dumps(state.metadata, allow_nan=False).encode()))
    if data is not None:
        result.update(data_arrays=_array_bytes([data.inputs, data.labels, data.probabilities]),
                      data_metadata_utf8=len(json.dumps(data.metadata, allow_nan=False).encode()))
    return result


def save_restart(path, state, data):
    """Exact working scalars, complete frozen marks and current state; no pickle."""
    state.validate()
    ar = state.arithmetic
    data.validate(ar, state.dimension)
    def encode(a):
        return dict(shape=list(a.shape), values=[float(v).hex() if ar.digits is None else
                    (hex(v.units) if ar.backend == "rational" else str(v)) for v in a.flat])
    encoded = {k: [encode(v) for v in getattr(state, k)] for k in ("b", "pi", "M", "D")}
    encoded.update({k: encode(getattr(state, k)) for k in ("g", "w", "c")})
    record = dict(format="depth-closure-v1", digits=ar.digits, backend=ar.backend,
                  metadata=state.metadata, data_metadata=data.metadata, state=encoded,
                  data={k: encode(getattr(data, k)) for k in ("inputs", "labels", "probabilities")})
    with Path(path).open("w", encoding="utf-8") as handle:
        json.dump(record, handle, separators=(",", ":"), allow_nan=False)


def load_restart(path):
    with Path(path).open(encoding="utf-8") as handle:
        record = json.load(handle)
    if (not isinstance(record, dict) or set(record) != {"format", "digits", "backend", "metadata", "data_metadata", "state", "data"}
            or record["format"] != "depth-closure-v1"):
        raise ValueError("unsupported restart schema")
    ar = Arithmetic(record["digits"], record["backend"])
    def decode(encoded):
        if (not isinstance(encoded, dict) or set(encoded) != {"shape", "values"}
                or not isinstance(encoded["shape"], list)
                or any(isinstance(v, bool) or not isinstance(v, int) or v < 0 for v in encoded["shape"])
                or not isinstance(encoded["values"], list)
                or any(not isinstance(v, str) for v in encoded["values"])):
            raise ValueError("invalid restart array")
        values = [float.fromhex(v) if ar.digits is None else
                  (Fixed.from_units(int(v, 16), ar.digits) if ar.backend == "rational" else Decimal(v))
                  for v in encoded["values"]]
        return np.asarray(values, dtype=ar.dtype).reshape(encoded["shape"])
    if (set(record["state"]) != {"b", "pi", "g", "w", "c", "M", "D"}
            or set(record["data"]) != {"inputs", "labels", "probabilities"}):
        raise ValueError("invalid restart fields")
    vectors = {k: [decode(v) for v in record["state"][k]] for k in ("b", "pi", "M", "D")}
    vectors.update({k: decode(record["state"][k]) for k in ("g", "w", "c")})
    state = State(**vectors, arithmetic=ar, metadata=record["metadata"]).validate()
    data = DataLaw(*(decode(record["data"][k]) for k in ("inputs", "labels", "probabilities")),
                   record["data_metadata"]).validate(ar, state.dimension)
    return state, data
