"""Study-local general-d dense observable closure; no neural-width parameter.

Uses the maintained arithmetic, source reverse differentiation and finite
integrator. The dimension adapter changes Gaussian seed coordinates only.
The theorem and explicit conditional scope are in CX1_CLOSURE_PROOF.md.
"""
from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
import json
import math
from pathlib import Path

import numpy as np
from pde.observable_arithmetic import Arithmetic, gaussian_points
from pde.observable_fixed import Fixed
from pde.observable_compiler import (GaussianCompiler, CompilerLimits,
    CompilerNumericalError, CompilerResourceLimit, Source, _Node)
from pde.observable_words import unpair, rational_code
from pde.observable_initialization import _all_exponents
from pde import observable_solver as _solver


def _positive(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, np.integer)) or value < 1:
        raise ValueError(name + " must be a positive integer")
    return int(value)


@dataclass(frozen=True, eq=False)
class Word:
    """Finite typed node; compiler merges literal structure without recursion."""
    op: str
    population: int
    args: tuple = ()
    scalar: object = None
    envelope: object = None

    @property
    def bounded(self):
        return self.envelope is not None


def node(op, *args, population=None, scalar=None):
    if op == "one":
        if args or population not in (1, 2):
            raise ValueError("constant needs a population")
        return Word(op, population, envelope=Fraction(1))
    if op.startswith("g") and op[1:].isdigit():
        if args or int(op[1:]) < 1 or population not in (None, 1):
            raise ValueError("invalid Gaussian seed")
        return Word(op, 1)
    arity = {"scale": 1, "sin": 1, "cos": 1, "tanh": 1, "action": 1,
             "add": 2, "multiply": 2}.get(op)
    if arity is None or len(args) != arity:
        raise ValueError("invalid word operation")
    pop = 3-args[0].population if op == "action" else args[0].population
    if op == "action":
        if not args[0].bounded:
            raise ValueError("action needs bounded input")
    elif any(a.population != pop for a in args):
        raise ValueError("mixed population coordinate operation")
    if op == "multiply" and not all(a.bounded for a in args):
        raise ValueError("product needs bounded inputs")
    bound = None
    if op in ("sin", "cos", "tanh"):
        bound = Fraction(1)
    elif op == "scale":
        scalar = Fraction(scalar)
        if args[0].bounded:
            bound = abs(scalar)*args[0].envelope
    elif op == "add" and all(a.bounded for a in args):
        bound = sum(a.envelope for a in args)
    elif op == "multiply":
        bound = args[0].envelope*args[1].envelope
    return Word(op, pop, tuple(args), scalar, bound)


@dataclass(frozen=True)
class Dictionary:
    dimension: int
    order: int
    first_words: tuple
    second_words: tuple
    core_dimensions: tuple
    tail_codes: tuple


def build_dictionary(dimension, order, *, max_features=4096, max_codes=100000):
    """Total-degree Chebyshev core plus the complete dimension-d word prefix.

    All bounded prefix outputs are retained, including literal duplicates.
    The finite resource bounds reject a request without changing its order.
    """
    d, p = _positive(dimension, "dimension"), _positive(order, "order")
    counts = (math.comb(p+2*d, 2*d), math.comb(p+d, d))
    if max(counts) > max_features or p+1 > max_codes:
        raise CompilerResourceLimit("requested dictionary exceeds its explicit resource limit")
    g = tuple(node("g"+str(i+1)) for i in range(d))
    h = tuple(node("tanh", z) for z in g)
    H = tuple(node("tanh", node("action", z)) for z in h)
    k = tuple(node("tanh", node("action", z)) for z in H)
    lists = []
    for population, coordinates in ((1, h+k), (2, H)):
        one = node("one", population=population)
        polys = []
        for x in coordinates:
            values = [one, x]
            for degree in range(1, p):
                values.append(node("add", node("scale", node("multiply", x, values[-1]), scalar=2),
                                   node("scale", values[-2], scalar=-1)))
            polys.append(values)
        outputs = []
        for powers in _all_exponents(p, len(coordinates)):
            factors = [polys[j][a] for j, a in enumerate(powers) if a]
            result = one if not factors else factors[0]
            for factor in factors[1:]:
                result = node("multiply", result, factor)
            outputs.append(result)
        lists.append(outputs)
    decoded = {0: node("one", population=1), 1: node("one", population=2)}
    decoded.update({i+2: value for i, value in enumerate(g)})
    tails = []
    for code in range(p+1):
        if code not in decoded:
            kcode, op = divmod(code-(d+2), 8)
            a, b = unpair(kcode)
            try:
                if op <= 3:
                    parent = decoded[kcode]
                    if parent is None:
                        raise ValueError("invalid dependency")
                    result = node(("sin", "cos", "tanh", "action")[op], parent)
                elif op == 6:
                    if decoded[b] is None:
                        raise ValueError("invalid dependency")
                    result = node("scale", decoded[b], scalar=rational_code(a))
                else:
                    if decoded[a] is None or decoded[b] is None:
                        raise ValueError("invalid dependency")
                    result = node("multiply" if op == 5 else "add", decoded[a], decoded[b])
            except ValueError:
                result = None
            decoded[code] = result
        word = decoded[code]
        if word is not None and word.bounded:
            lists[word.population-1].append(word)
            tails.append(code)
    if max(map(len, lists)) > max_features:
        raise CompilerResourceLimit("retained dictionary exceeds max_features")
    return Dictionary(d, p, tuple(lists[0]), tuple(lists[1]), counts, tuple(tails))


class DimensionCompiler(GaussianCompiler):
    """Maintained source compiler with d independent lower Gaussian seeds.

    Inherited: structural ingestion, frozen-source reverse AD, finite union,
    resource checks, source tables. Changed: seed validation/values and the
    lower Gaussian offset (d instead of two). No globals are patched.
    """
    def __init__(self, dimension, *args, **kwargs):
        self.dimension = _positive(dimension, "dimension")
        super().__init__(*args, **kwargs)

    def _node(self, op, population, args=(), scalar=None, allow_new=True):
        if op.startswith("g") and op[1:].isdigit():
            i = int(op[1:])
            if population != 1 or args or scalar is not None or not 1 <= i <= self.dimension:
                raise ValueError("Gaussian seed outside the declared dimension")
            key = op, population, args, scalar
            if key not in self._structural:
                if not allow_new:
                    raise ValueError("seed not in frozen union")
                if len(self.nodes) >= self.limits.max_nodes:
                    raise CompilerResourceLimit("finite program exceeds max_nodes")
                self._structural[key] = len(self.nodes)
                self.nodes.append(_Node(op, population, args, scalar, None))
            return self._structural[key]
        return super()._node(op, population, args, scalar, allow_new)

    def _normal_clouds(self, count):
        result = {}
        for population in (1, 2):
            dimension = (self.dimension if population == 1 else 0)+sum(
                n.op == "action" and n.population == population for n in self.nodes)
            cloud = np.asarray(self.gaussian_points(count, dimension, self.ar))
            if cloud.shape != (count, dimension) or not self.ar.finite(cloud):
                raise ValueError("invalid joint Gaussian cloud")
            result[population] = cloud
        return result

    def _value(self, index, values, normals, gaussian):
        op = self.nodes[index].op
        if op.startswith("g") and op[1:].isdigit():
            return normals[1][:, int(op[1:])-1].copy()
        return super()._value(index, values, normals, gaussian)

    def _new_source(self, index, values, gaussian):
        n, ar, q = self.nodes[index], self.ar, self.integration_count
        population, operand = n.population, n.args[0]
        previous, opposite = self.source_lists[population], self.source_lists[3-population]
        slot, value = len(previous), values[operand]
        variance = np.sum(value*value)/ar.real(q)+self.epsilon_cov
        cross = ar.array([np.sum(value*values[s.operand])/ar.real(q) for s in previous])
        lower, row = self.factors[population], ar.zeros(slot+1)
        for j in range(slot):
            row[j] = (cross[j]-np.sum(lower[j, :j]*row[:j]))/lower[j, j]
        schur = variance-np.sum(row[:slot]*row[:slot])
        if not ar.finite(np.asarray([schur])) or schur <= 0:
            raise CompilerNumericalError("positive covariance pivot unresolved; increase precision")
        row[slot] = ar.sqrt(schur)[()]
        lower[slot, :slot+1] = row
        base = self.dimension if population == 1 else 0
        gaussian[population][:, slot] = self._normals[population][:, base:base+slot+1] @ row
        coefficients = self._partials(operand, values, mean=True)
        response = tuple((s.operand, coefficients[j]) for j, s in enumerate(opposite))
        source = Source(index, operand, population, slot, response)
        self.sources[index] = source
        previous.append(source)
        self.diagnostics.append(dict(population=population, source_index=slot,
            variance=variance, cross=cross.copy(), innovation_variance=schur,
            response_coefficients=coefficients.copy()))

    def _at_count(self, population_count=None):
        if not self._compiled:
            raise ValueError("compile before evaluation")
        count = self.integration_count if population_count is None else _positive(population_count, "population_count")
        if count == self.integration_count:
            return self._values, self._normals
        if count == self._replay_count:
            return self._replay_values, self._replay_normals
        self._budget(count)
        with self.ar.context():
            normals = self._normal_clouds(count)
            gaussian = {pop: normals[pop][:, self.dimension if pop == 1 else 0:] @ self.factors[pop].T
                        for pop in (1, 2)}
            values = []
            for index in range(len(self.nodes)):
                values.append(self._value(index, values, normals, gaussian))
                if not self.ar.finite(values[-1]):
                    raise CompilerNumericalError("nonfinite initialized word replay")
        self._replay_count, self._replay_values, self._replay_normals = count, values, normals
        return values, normals


def _inputs(values, ar, dimension=None):
    values = ar.array(values)
    if values.ndim != 2 or min(values.shape) < 1 or (dimension is not None and values.shape[1] != dimension):
        raise ValueError("inputs must have nonempty shape (m,d)")
    tol = ar.real("2e-12" if ar.digits is None else "1e-"+str(ar.digits-5))*values.shape[1]
    if not ar.finite(values) or any(abs(x-1) > tol for x in np.sum(values*values, axis=1)):
        raise ValueError("normalized inputs must lie on the unit sphere")
    return values


class DataLaw(_solver.DataLaw):
    def validate(self, ar):
        with ar.context():
            self.inputs = _inputs(self.inputs, ar)
            self.labels = ar.array(self.labels)
            if self.labels.shape != (len(self.inputs),) or not ar.finite(self.labels):
                raise ValueError("invalid labels")
            self.probabilities = _solver._probabilities(self.probabilities, len(self.inputs), ar)
        return self


_ARRAYS = ("b1", "g", "w", "p1", "b2", "c", "p2", "M", "D")


class State(_solver.State):
    def validate(self):
        ar = self.arithmetic
        if not all(isinstance(getattr(self, k), np.ndarray) and ar.finite(getattr(self, k)) for k in _ARRAYS):
            raise ValueError("state arrays must be finite")
        if self.b1.ndim != 2 or self.b2.ndim != 2 or min(self.b1.shape+self.b2.shape) < 1:
            raise ValueError("empty feature populations")
        if self.g.ndim != 2 or self.g.shape[0] != len(self.b1) or self.g.shape[1] < 1 or self.w.shape != self.g.shape:
            raise ValueError("invalid joint row population")
        if self.c.shape != (len(self.b2),) or self.M.shape != (self.b2.shape[1], self.b1.shape[1]) or self.D.shape != self.M.shape:
            raise ValueError("invalid readout or feature matrix")
        _solver._probabilities(self.p1, len(self.b1), ar)
        _solver._probabilities(self.p2, len(self.b2), ar)
        return self

    def copy(self):
        return State(*(getattr(self, k).copy() for k in _ARRAYS), self.arithmetic,
                     json.loads(json.dumps(self.metadata)))

    def dynamic_copy(self, w, c, M):
        return State(self.b1, self.g, w, self.p1, self.b2, c, self.p2, M, self.D,
                     self.arithmetic, self.metadata)


def initialize(dimension, order=1, *, initialization_nodes=128, population_nodes=64,
               epsilon_cov=Fraction(1, 1000), digits=None, backend="decimal",
               limits=None, max_features=4096, max_codes=100000):
    """Complete generic initializer at every admitted d/order; no p=1 shortcut.

    Q computes source coefficients and Grams; P separately replays frozen joint
    laws. Positive covariance regularization is removed only in its own limit.
    """
    dictionary = build_dictionary(dimension, order, max_features=max_features, max_codes=max_codes)
    dimension, order = dictionary.dimension, dictionary.order
    ar = Arithmetic(digits, backend)
    first, second = dictionary.first_words, dictionary.second_words
    forward = tuple(node("action", w) for w in first)
    reverse = tuple(node("action", w) for w in second)
    program = DimensionCompiler(dimension, ar, gaussian_points, initialization_nodes,
                                epsilon_cov, limits or CompilerLimits())
    program._raw_dimensions = len(first), len(second)
    program.compile(first+second+forward+reverse, population_nodes=population_nodes)
    with ar.context():
        q, p = ar.real(initialization_nodes), _positive(population_nodes, "population_nodes")
        r1, r2 = program.table(first), program.table(second)
        G1, G2 = r1.T @ r1/q, r2.T @ r2/q
        C = r2.T @ program.table(forward)/q
        eta = ar.real(Fraction(1, 1024*(order+1)**2))
        L1 = ar.inverse_lower(ar.cholesky(G1+eta*ar.eye(len(first))))
        L2 = ar.inverse_lower(ar.cholesky(G2+eta*ar.eye(len(second))))
        b1, b2 = program.table(first, p) @ L1.T, program.table(second, p) @ L2.T
        D = L2 @ C @ L1.T
        _, normals = program._at_count(p)
        g = normals[1][:, :dimension].copy()
        weights = np.full(p, ar.real(1)/ar.real(p), dtype=ar.dtype)
        metadata = dict(scheme="cx1-general-d-dense-v1", dimension=dimension, order=order,
            feature_dimensions=[len(first), len(second)], core_dimensions=list(dictionary.core_dimensions),
            prefix_codes=list(dictionary.tail_codes), source_counts=[len(program.source_lists[i]) for i in (1, 2)],
            initialization_nodes=initialization_nodes, population_nodes=population_nodes,
            epsilon_cov=str(epsilon_cov), ridge=str(Fraction(1, 1024*(order+1)**2)),
            exact_initialized_law=False, initializer="complete-joint-Gaussian-program")
        return State(b1, g, g.copy(), weights, b2, ar.zeros(p), weights.copy(), D.copy(), D,
                     ar, metadata).validate()


def fields(state, inputs, *, backward=True):
    state.validate()
    with state.arithmetic.context():
        u = _inputs(inputs, state.arithmetic, state.g.shape[1])
        return _solver._fields(state, u, backward)


def predict(state, inputs):
    return fields(state, inputs, backward=False)["f"]


def rhs(state, data, *, block_size=16):
    data.validate(state.arithmetic)
    if data.inputs.shape[1] != state.g.shape[1]:
        raise ValueError("data dimension does not match state")
    return _solver.rhs(state, data, block_size=block_size)


# The maintained integrator is dimension independent: its stage construction
# dispatches to State.dynamic_copy and validations dispatch to these subclasses.
evolve = _solver.evolve
interpolate_state = _solver.interpolate_state
paired_observations = _solver.paired_observations
state_bytes = _solver.state_bytes
save_restart = _solver.save_restart


def loss(state, data):
    data.validate(state.arithmetic)
    with state.arithmetic.context():
        residual = predict(state, data.inputs)-data.labels
        return data.probabilities @ (residual*residual)


def apply_action(state, values, *, reverse=False, frozen=False):
    """Finite feature contraction on a declared retained population table."""
    state.validate()
    ar = state.arithmetic
    with ar.context():
        value = ar.array(values)
        source, weights, target = ((state.b2, state.p2, state.b1) if reverse else
                                    (state.b1, state.p1, state.b2))
        if value.ndim not in (1, 2) or len(value) != len(source):
            raise ValueError("action values must use the source population")
        matrix = state.D if frozen else state.M
        if reverse:
            matrix = matrix.T
        weighted = weights*value if value.ndim == 1 else weights[:, None]*value
        return target @ (matrix @ (source.T @ weighted))


def observe(state, words):
    """Same-population finite joint initialized/current action observations.

    Use Word('w1',1), ..., Word('c',2) for moving seeds; g seeds
    stay frozen. Word('frozen_z20',2,scalar=tuple(u)) reconstructs frozen z2.
    All current action nodes use M, including repeated forward/reverse calls.
    """
    state.validate()
    words = tuple(words)
    if not words or len({w.population for w in words}) != 1:
        raise ValueError("observation tuple must use one population")
    values, ar = {}, state.arithmetic
    with ar.context():
        for output in words:
            pending = [(output, False)]
            while pending:
                word, done = pending.pop()
                if id(word) in values:
                    continue
                if not done:
                    pending.append((word, True))
                    pending.extend((a, False) for a in reversed(word.args))
                    continue
                op = word.op
                if op[0:1] in ("g", "w") and op[1:].isdigit():
                    base = state.g if op[0] == "g" else state.w
                    result = base[:, int(op[1:])-1]
                elif op == "c":
                    result = state.c
                elif op == "frozen_z20":
                    u = _inputs([word.scalar], ar, state.g.shape[1])[0]
                    result = apply_action(state, ar.tanh(state.g @ u), frozen=True)
                elif op == "one":
                    result = np.full(len(state.b1 if word.population == 1 else state.b2), ar.real(1), dtype=ar.dtype)
                else:
                    a = values[id(word.args[0])]
                    if op == "action":
                        result = apply_action(state, a, reverse=word.population == 1)
                    elif op == "scale":
                        result = ar.real(word.scalar)*a
                    elif op == "add":
                        result = a+values[id(word.args[1])]
                    elif op == "multiply":
                        result = a*values[id(word.args[1])]
                    elif op == "tanh":
                        result = ar.tanh(a)
                    elif op in ("sin", "cos"):
                        result = ar.trig(a, cosine=op == "cos")
                    else:
                        raise ValueError("unsupported observation instruction")
                values[id(word)] = result
        table = np.column_stack([values[id(w)] for w in words])
        return table, (state.p1 if words[0].population == 1 else state.p2).copy()


def load_restart(path):
    """Read exact working values without executing an initializer or source tape."""
    record = json.loads(Path(path).read_text())
    if record.get("format") != "observable-solver-v1" or record.get("metadata", {}).get("scheme") != "cx1-general-d-dense-v1":
        raise ValueError("not a CX1 closure checkpoint")
    ar = Arithmetic(record["digits"], record["backend"])
    def decode(value):
        a = [float.fromhex(x) if ar.digits is None else
             (Fixed.from_units(int(x, 16), ar.digits) if ar.backend == "rational" else Decimal(x))
             for x in value["values"]]
        return np.asarray(a, dtype=ar.dtype).reshape(value["shape"])
    state = State(*(decode(record["state"][k]) for k in _ARRAYS), ar, record["metadata"]).validate()
    data = DataLaw(*(decode(record["data"][k]) for k in ("inputs", "labels", "probabilities")),
                   record["data_metadata"]).validate(ar)
    return state, data
