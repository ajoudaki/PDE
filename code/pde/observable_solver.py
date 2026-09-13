"""Finite autonomous nonlinear observable dynamics, paired observations, restart.

The represented two-arc family has the proved scope T=1/200, |y|<=1.
Supplied finite DataLaw objects are exploratory unless covered by that theorem.
Population nodes integrate a joint law; M indexes features, not neurons.
"""
from dataclasses import dataclass, field
from decimal import Decimal
from fractions import Fraction
import json
from pathlib import Path
import sys

import numpy as np

from pde.observable_arithmetic import Arithmetic
from pde.observable_fixed import Fixed
from pde.observable_initialization import initialize_features


def _positive_integer(value, name):
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(name + " must be a positive integer")
    return value


def _probabilities(values, count, ar):
    values = ar.array(values)
    if values.shape != (count,) or not ar.finite(values) or any(x < 0 for x in values):
        raise ValueError("invalid probability vector")
    total = sum(values, ar.real(0))
    tolerance = ar.real("2e-12" if ar.digits is None else "1e-" + str(ar.digits-5))*max(1, count)
    if total <= 0 or abs(total-1) > tolerance:
        raise ValueError("probabilities must have unit positive mass at working precision")
    # Validation never evolves the data law through repeated renormalization.
    return values


def _unit_inputs(values, ar):
    values = ar.array(values)
    if values.ndim != 2 or len(values) == 0 or values.shape[1] != 2:
        raise ValueError("inputs must have nonempty shape (m,2)")
    tolerance = ar.real("2e-12" if ar.digits is None else "1e-" + str(ar.digits-5))
    if not ar.finite(values) or any(abs(x-1) > tolerance for x in np.sum(values*values, axis=1)):
        raise ValueError("inputs must lie on the unit circle at the working precision")
    return values


@dataclass
class DataLaw:
    inputs: np.ndarray
    labels: np.ndarray
    probabilities: np.ndarray
    metadata: dict = field(default_factory=dict)

    def validate(self, ar):
        with ar.context():
            self.inputs = _unit_inputs(self.inputs, ar)
            self.labels = ar.array(self.labels)
            if self.labels.shape != (len(self.inputs),) or not ar.finite(self.labels):
                raise ValueError("labels must be a finite vector matching inputs")
            self.probabilities = _probabilities(self.probabilities, len(self.inputs), ar)
        return self


@dataclass(frozen=True)
class ArcLaw:
    """Rational mixture of two arcs, including degenerate atomic intervals.

    Actual data are x=sqrt(2)u; the dynamics consume their normalized u.
    The second arc is rotated by the rational 3/5,4/5 rotation.
    """
    p: Fraction = Fraction(1, 2)
    a: Fraction = Fraction(-1, 20)
    b: Fraction = Fraction(1, 20)
    c: Fraction = Fraction(-1, 20)
    d: Fraction = Fraction(1, 20)

    def __post_init__(self):
        for name in ("p", "a", "b", "c", "d"):
            x = getattr(self, name)
            if isinstance(x, (float, bool)):
                raise ValueError("represented parameters must be exact rationals, integers, or rational strings")
            object.__setattr__(self, name, Fraction(x))
        if not Fraction(1, 3) <= self.p <= Fraction(2, 3):
            raise ValueError("mixture mass outside the supported family")
        if not -Fraction(1, 20) <= self.a <= self.b <= Fraction(1, 20):
            raise ValueError("first interval outside the supported family")
        if not -Fraction(1, 20) <= self.c <= self.d <= Fraction(1, 20):
            raise ValueError("second interval outside the supported family")

    def quadrature(self, nodes_per_arc, arithmetic):
        _positive_integer(nodes_per_arc, "nodes_per_arc")
        inputs, labels, weights = [], [], []
        for a, b, weight, label, rotate in ((self.a, self.b, self.p, 1, False),
                                           (self.c, self.d, 1-self.p, -1, True)):
            count = 1 if a == b else nodes_per_arc
            for j in range(count):
                s = a + (b-a)*Fraction(2*j+1, 2*count)
                u, v = (1-s*s)/(1+s*s), 2*s/(1+s*s)
                if rotate:
                    u, v = (3*u-4*v)/5, (4*u+3*v)/5
                inputs.append((u, v))
                labels.append(label)
                weights.append(weight/count)
        return DataLaw(arithmetic.array(inputs), arithmetic.array(labels), arithmetic.array(weights),
                       {"scope": "proved two-arc family through T=1/200",
                        "parameters": {k: str(getattr(self, k)) for k in ("p", "a", "b", "c", "d")},
                        "nodes_per_arc": nodes_per_arc}).validate(arithmetic)


@dataclass
class State:
    b1: np.ndarray
    g: np.ndarray
    w: np.ndarray
    p1: np.ndarray
    b2: np.ndarray
    c: np.ndarray
    p2: np.ndarray
    M: np.ndarray
    D: np.ndarray
    arithmetic: Arithmetic
    metadata: dict = field(default_factory=dict)

    def validate(self):
        ar = self.arithmetic
        arrays = (self.b1, self.g, self.w, self.p1, self.b2, self.c, self.p2, self.M, self.D)
        if not all(isinstance(x, np.ndarray) and ar.finite(x) for x in arrays):
            raise ValueError("state arrays must be finite")
        if self.b1.ndim != 2 or self.b2.ndim != 2 or min(self.b1.shape+self.b2.shape) < 1:
            raise ValueError("empty or invalid feature tables")
        if self.g.shape != (len(self.b1), 2) or self.w.shape != self.g.shape:
            raise ValueError("first population must retain joint (b,g,w)")
        if self.c.shape != (len(self.b2),) or self.p1.shape != (len(self.b1),) or self.p2.shape != self.c.shape:
            raise ValueError("invalid population weights or readout")
        expected = (self.b2.shape[1], self.b1.shape[1])
        if self.M.shape != expected or self.D.shape != expected:
            raise ValueError("M,D must index retained features")
        with ar.context():
            tolerance = ar.real("2e-12" if ar.digits is None else "1e-" + str(ar.digits-5))
            for p in (self.p1, self.p2):
                if any(x < 0 for x in p) or abs(sum(p, ar.real(0))-1) > tolerance*len(p):
                    raise ValueError("population weights must have unit positive mass")
        return self

    def copy(self):
        return State(*(getattr(self, k).copy() for k in ("b1", "g", "w", "p1", "b2", "c", "p2", "M", "D")),
                     self.arithmetic, json.loads(json.dumps(self.metadata)))

    def dynamic_copy(self, w, c, M):
        """Private stage state shares fixed marks; no caller-visible mutation."""
        return State(self.b1, self.g, w, self.p1, self.b2, c, self.p2, M, self.D,
                     self.arithmetic, self.metadata)


def initialize(order=1, *, initialization_nodes=2048, population_nodes=1024,
               digits=None, backend="decimal", epsilon_cov="0.001", limits=None):
    ar = Arithmetic(digits, backend)
    with ar.context():
        init = initialize_features(order, arithmetic=ar, initialization_nodes=initialization_nodes,
                                   population_nodes=population_nodes, epsilon_cov=epsilon_cov, limits=limits)
        state = State(init.b1, init.g, init.g.copy(), init.p1, init.b2,
                      ar.zeros(len(init.b2)), init.p2, init.D.copy(), init.D, ar, init.metadata)
    return state.validate()


def _fields(state, inputs, backward=True):
    ar = state.arithmetic
    h1 = ar.tanh(state.w @ inputs.T)
    a = state.b1.T @ (state.p1[:, None]*h1)
    h2 = ar.tanh(state.b2 @ (state.M @ a))
    f = state.p2 @ (state.c[:, None]*h2)
    result = dict(h1=h1, a=a, h2=h2, f=f)
    if backward:
        d = state.b2.T @ (state.p2[:, None]*state.c[:, None]*(1-h2*h2))
        result.update(d=d, q=state.b1 @ (state.M.T @ d))
    return result


def circle_inputs(count, arithmetic):
    _positive_integer(count, "circle count")
    with arithmetic.context():
        angles = arithmetic.array(range(count))*2*arithmetic.pi()/arithmetic.real(count)
        return np.column_stack((arithmetic.trig(angles, cosine=True), arithmetic.trig(angles)))


def predict(state, inputs, *, block_size=16):
    """Evaluate any finite list on the entire input circle; no interpolation grid."""
    _positive_integer(block_size, "block_size")
    state.validate()
    ar = state.arithmetic
    with ar.context():
        inputs = _unit_inputs(inputs, ar)
        result = ar.zeros(len(inputs))
        for start in range(0, len(inputs), block_size):
            stop = min(start+block_size, len(inputs))
            result[start:stop] = _fields(state, inputs[start:stop], False)["f"]
    if not ar.finite(result):
        raise ValueError("nonfinite prediction")
    return result


def rhs(state, data, *, block_size=16):
    """The complete nonlinear gradient vector field in physical time."""
    _positive_integer(block_size, "block_size")
    state.validate()
    ar = state.arithmetic
    with ar.context():
        data.validate(ar)
        vw, vc, vM = ar.zeros(state.w.shape), ar.zeros(state.c.shape), ar.zeros(state.M.shape)
        for start in range(0, len(data.inputs), block_size):
            stop = min(start+block_size, len(data.inputs))
            u = data.inputs[start:stop]
            v = _fields(state, u)
            r = data.probabilities[start:stop]*(v["f"]-data.labels[start:stop])
            vw -= 2*((1-v["h1"]*v["h1"])*v["q"]*r) @ u
            vc -= 2*v["h2"] @ r
            vM -= 2*(v["d"]*r) @ v["a"].T
        if not all(ar.finite(x) for x in (vw, vc, vM)):
            raise ValueError("nonfinite velocity")
        return vw, vc, vM


def evolve(state, data, *, steps, step_size, block_size=16):
    """Fixed-step explicit Heun with linear within-step prediction convention.

    Returns a fresh final state. No history or absolute clock is retained.
    For an intermediate time, evolve to its containing node and interpolate
    that one step's two endpoint states using interpolate_state.
    """
    _positive_integer(steps, "steps")
    ar = state.arithmetic
    current = state.copy().validate()
    with ar.context():
        h = ar.real(step_size)
        if h <= 0:
            raise ValueError("step_size must be positive")
        for _ in range(steps):
            k = rhs(current, data, block_size=block_size)
            stage = current.dynamic_copy(current.w+h*k[0], current.c+h*k[1], current.M+h*k[2])
            l = rhs(stage, data, block_size=block_size)
            current = current.dynamic_copy(current.w+(h/2)*(k[0]+l[0]),
                                           current.c+(h/2)*(k[1]+l[1]), current.M+(h/2)*(k[2]+l[2]))
            current.validate()
    return current


def interpolate_state(left, right, fraction):
    """Interpolate endpoints of one step on their identical joint marks."""
    ar = left.arithmetic
    if (ar.digits, ar.backend) != (right.arithmetic.digits, right.arithmetic.backend):
        raise ValueError("interpolation requires identical arithmetic")
    for name in ("b1", "g", "p1", "b2", "p2", "D"):
        if not np.array_equal(getattr(left, name), getattr(right, name)):
            raise ValueError("interpolation requires identical frozen marks")
    with ar.context():
        q = ar.real(fraction)
        if not 0 <= q <= 1:
            raise ValueError("interpolation fraction must lie in [0,1]")
        return left.dynamic_copy((1-q)*left.w+q*right.w, (1-q)*left.c+q*right.c,
                                 (1-q)*left.M+q*right.M).validate()


def paired_observations(state, data, *, block_size=16, include_pairs=True):
    """Same-population initial/current activations and training-averaged RMS.

    Pair arrays have shape (population_nodes,input_nodes,2). The law is weighted
    by p_l[i]*data.probabilities[j]; both layers share their own frozen marks.
    Frozen upper activations use D and g through the same retained action.
    """
    _positive_integer(block_size, "block_size")
    state.validate()
    ar = state.arithmetic
    with ar.context():
        data.validate(ar)
        sums = [ar.real(0), ar.real(0)]
        pairs = ([ar.zeros((len(state.b1), len(data.inputs), 2)),
                  ar.zeros((len(state.b2), len(data.inputs), 2))] if include_pairs else [None, None])
        for start in range(0, len(data.inputs), block_size):
            stop = min(start+block_size, len(data.inputs))
            u = data.inputs[start:stop]
            current = _fields(state, u, False)
            initial1 = ar.tanh(state.g @ u.T)
            initial2 = ar.tanh(state.b2 @ (state.D @ (state.b1.T @ (state.p1[:, None]*initial1))))
            for layer, initial, actual, p in ((0, initial1, current["h1"], state.p1),
                                               (1, initial2, current["h2"], state.p2)):
                sums[layer] += p @ ((actual-initial)**2) @ data.probabilities[start:stop]
                if include_pairs:
                    pairs[layer][:, start:stop, 0] = initial
                    pairs[layer][:, start:stop, 1] = actual
        return dict(first_pairs=pairs[0], second_pairs=pairs[1],
                    first_weights=state.p1.copy(), second_weights=state.p2.copy(),
                    input_weights=data.probabilities.copy(), inputs=data.inputs.copy(),
                    rms1=ar.sqrt(sums[0]).item(), rms2=ar.sqrt(sums[1]).item())


def loss(state, data, *, block_size=16):
    ar = state.arithmetic
    with ar.context():
        data.validate(ar)
        residual = predict(state, data.inputs, block_size=block_size)-data.labels
        return data.probabilities @ (residual*residual)


def state_bytes(state):
    """Retained array bytes, including Decimal objects; Python metadata separately."""
    result = 0
    for name in ("b1", "g", "w", "p1", "b2", "c", "p2", "M", "D"):
        a = getattr(state, name)
        result += a.nbytes
        if a.dtype == object:
            result += sum(sys.getsizeof(x) for x in a.flat)
            result += sum(sys.getsizeof(x.units)+sys.getsizeof(x.scale) for x in a.flat if isinstance(x, Fixed))
    return dict(arrays=result, metadata_utf8=len(json.dumps(state.metadata).encode()))


def save_restart(path, state, data):
    """Portable exact working-state values; no pickle, source tape, or clock."""
    state.validate()
    ar = state.arithmetic
    data.validate(ar)
    def encode(a):
        return {"shape": list(a.shape), "values": [float(x).hex() if ar.digits is None else (hex(x.units) if ar.backend == "rational" else str(x)) for x in a.flat]}
    record = dict(format="observable-solver-v1", digits=ar.digits, backend=ar.backend, metadata=state.metadata,
                  data_metadata=data.metadata,
                  state={k: encode(getattr(state, k)) for k in ("b1", "g", "w", "p1", "b2", "c", "p2", "M", "D")},
                  data={k: encode(getattr(data, k)) for k in ("inputs", "labels", "probabilities")})
    with Path(path).open("w", encoding="utf-8") as handle:
        json.dump(record, handle, separators=(",", ":"), allow_nan=False)


def load_restart(path):
    with Path(path).open(encoding="utf-8") as handle:
        record = json.load(handle)
    if set(record) != {"format", "digits", "backend", "metadata", "data_metadata", "state", "data"} or record["format"] != "observable-solver-v1":
        raise ValueError("unsupported restart schema")
    ar = Arithmetic(record["digits"], record["backend"])
    def decode(value):
        if set(value) != {"shape", "values"} or any(isinstance(x, bool) or not isinstance(x, int) or x < 0 for x in value["shape"]):
            raise ValueError("invalid restart array")
        a = [float.fromhex(x) if ar.digits is None else (Fixed.from_units(int(x, 16), ar.digits) if ar.backend == "rational" else Decimal(x)) for x in value["values"]]
        return np.asarray(a, dtype=ar.dtype).reshape(value["shape"])
    keys = ("b1", "g", "w", "p1", "b2", "c", "p2", "M", "D")
    if set(record["state"]) != set(keys) or set(record["data"]) != {"inputs", "labels", "probabilities"}:
        raise ValueError("invalid restart fields")
    state = State(*(decode(record["state"][k]) for k in keys), ar, record["metadata"]).validate()
    data = DataLaw(*(decode(record["data"][k]) for k in ("inputs", "labels", "probabilities")), record["data_metadata"])
    data.validate(ar)
    return state, data
