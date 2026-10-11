"""Finite joint initialized-Gaussian compiler for observable dictionaries.

All arithmetic and Gaussian nodes are explicitly injected.  The compiler is
initialization-only: its output tables and contraction can outlive it.  Positive
epsilon_cov is a numerical source-covariance approximation, not an assertion of
exact canonical action laws at finite epsilon or cubature resolution.
"""
from dataclasses import dataclass
from fractions import Fraction
import math

import numpy as np


class CompilerResourceLimit(ValueError):
    """The requested finite program exceeds an explicit preallocation limit."""


class CompilerNumericalError(ValueError):
    """Arithmetic did not resolve a required positive covariance direction."""


def _positive_integer(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, np.integer)) or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return int(value)


@dataclass(frozen=True)
class CompilerLimits:
    max_nodes: int = 4096
    max_sources: int = 256
    max_points: int = 1000000
    max_working_bytes: int = 536870912
    max_work_units: int = 2000000000
    max_scalar_bits: int = 65536

    def __post_init__(self):
        for name in self.__dataclass_fields__:
            _positive_integer(getattr(self, name), name)


@dataclass(frozen=True)
class _Node:
    op: str
    population: int
    args: tuple = ()
    scalar: object = None
    bound: object = None


@dataclass(frozen=True)
class _ActionRequest:
    """Structural action wrapper; no dependency on a particular Word class."""
    operand: object

    @property
    def op(self):
        return "action"

    @property
    def population(self):
        return 3 - self.operand.population

    @property
    def args(self):
        return (self.operand,)


@dataclass(frozen=True)
class Source:
    node: int
    operand: int
    population: int
    index: int
    response: tuple


@dataclass
class RawInitialization:
    psi1: np.ndarray
    psi2: np.ndarray
    g: np.ndarray
    probabilities1: np.ndarray
    probabilities2: np.ndarray
    gram1: np.ndarray
    gram2: np.ndarray
    C: np.ndarray
    C_reverse: np.ndarray
    program: object
    metadata: dict


class GaussianCompiler:
    """Compile one finite union, then replay its frozen source law.

    ``arithmetic`` supplies context/real/zeros/finite/sqrt/tanh/trig and a
    ``digits`` attribute, as in observable_arithmetic.Arithmetic.
    ``gaussian_points(count, dimension, arithmetic)`` supplies deterministic
    joint standard-Gaussian integration nodes.  Its convergence is a premise
    of numerical consistency, not inferred from its shape.

    Words are duck typed by op/population/args/scalar.  Only correctly typed
    bounded-operand initialized grammar is admitted.  Word-class identity is
    irrelevant: structural canonicalization shares identical action calls.
    ``compile`` is one-shot; enlarge a program by compiling its whole new union.
    """

    def __init__(self, arithmetic, gaussian_points, integration_count,
                 epsilon_cov, limits=None):
        self.ar = arithmetic
        self.gaussian_points = gaussian_points
        self.integration_count = _positive_integer(integration_count, "integration_count")
        self.limits = limits or CompilerLimits()
        if not isinstance(self.limits, CompilerLimits):
            raise ValueError("limits must be CompilerLimits")
        with self.ar.context():
            self.epsilon_cov = self.ar.real(epsilon_cov)
        if self.epsilon_cov <= 0:
            raise ValueError("epsilon_cov must be strictly positive")
        if not callable(gaussian_points):
            raise ValueError("gaussian_points must be callable")
        self.nodes = []
        self._structural = {}
        # Retaining these references prevents object-id reuse during ingestion.
        self._objects = {}
        self.sources = {}
        self.source_lists = {1: [], 2: []}
        self.factors = {}
        self.diagnostics = []
        self.resource_estimate = {}
        self._compiled = False
        self._started = False
        self._values = None
        self._normals = None
        self._replay_count = None
        self._replay_values = None
        self._replay_normals = None
        self._raw_dimensions = None

    def _fraction(self, value):
        if isinstance(value, bool):
            raise ValueError("word scalars must be finite real numbers")
        if isinstance(value, (float, np.floating)):
            if not math.isfinite(float(value)):
                raise ValueError("word scalars must be finite")
            result = Fraction(float(value))
        else:
            try:
                result = Fraction(value)
            except (TypeError, ValueError, OverflowError) as exc:
                raise ValueError("word scalar is not a finite rational value") from exc
        if max(result.numerator.bit_length(), result.denominator.bit_length()) > self.limits.max_scalar_bits:
            raise CompilerResourceLimit("word scalar exceeds max_scalar_bits")
        return result

    def _node(self, op, population, args=(), scalar=None, allow_new=True):
        if isinstance(population, bool) or population not in (1, 2):
            raise ValueError("word population must be 1 or 2")
        arities = {"one": 0, "g1": 0, "g2": 0, "scale": 1,
                   "sin": 1, "cos": 1, "tanh": 1, "action": 1,
                   "add": 2, "multiply": 2}
        if op not in arities or len(args) != arities[op]:
            raise ValueError(f"unsupported word operation or arity: {op}")
        if op in ("g1", "g2") and population != 1:
            raise ValueError("Gaussian seed belongs to population 1")
        parents = [self.nodes[i] for i in args]
        if op == "action":
            if parents[0].population != 3-population or parents[0].bound is None:
                raise ValueError("action requires a bounded opposite-population operand")
        elif any(parent.population != population for parent in parents):
            raise ValueError("coordinate operations require one population")
        if op == "multiply" and any(parent.bound is None for parent in parents):
            raise ValueError("products require two bounded operands")
        if op == "scale":
            scalar = self._fraction(scalar)
        elif scalar is not None:
            raise ValueError("only a scale node has a scalar")
        key = op, population, args, scalar
        if key in self._structural:
            return self._structural[key]
        if not allow_new:
            raise ValueError("word was not included in the frozen finite union")
        if len(self.nodes) >= self.limits.max_nodes:
            raise CompilerResourceLimit("finite program exceeds max_nodes")
        bound = None
        if op in ("one", "sin", "cos", "tanh"):
            bound = Fraction(1)
        elif op == "scale" and parents[0].bound is not None:
            bound = abs(scalar)*parents[0].bound
        elif op == "add" and all(parent.bound is not None for parent in parents):
            bound = parents[0].bound+parents[1].bound
        elif op == "multiply":
            bound = parents[0].bound*parents[1].bound
        if bound is not None and max(bound.numerator.bit_length(), bound.denominator.bit_length()) > self.limits.max_scalar_bits:
            raise CompilerResourceLimit("syntax envelope exceeds max_scalar_bits")
        index = len(self.nodes)
        self.nodes.append(_Node(op, population, args, scalar, bound))
        self._structural[key] = index
        return index

    def _word(self, word, allow_new=True):
        """Iterative ingestion avoids recursion in large finite DAGs."""
        results, active = {}, set()
        stack = [(word, False)]
        while stack:
            current, expanded = stack.pop()
            identity = id(current)
            if identity in self._objects:
                results[identity] = self._objects[identity][1]
                continue
            if identity in results:
                continue
            try:
                op, population = current.op, current.population
                args = tuple(getattr(current, "args", ()))
            except (AttributeError, TypeError) as exc:
                raise ValueError("inputs must be typed Word-like objects") from exc
            if not expanded:
                if identity in active:
                    raise ValueError("word graph contains a cycle")
                active.add(identity)
                stack.append((current, True))
                for child in reversed(args):
                    if id(child) in active:
                        raise ValueError("word graph contains a cycle")
                    stack.append((child, False))
                continue
            active.remove(identity)
            child_ids = tuple(results[id(child)] for child in args)
            if op in ("w1", "w2"):
                if args or population != 1:
                    raise ValueError("initialized row aliases require population 1")
                index = self._node("g"+op[1], 1, allow_new=allow_new)
            elif op == "c":
                if args or population != 2:
                    raise ValueError("initialized readout requires population 2")
                one = self._node("one", 2, allow_new=allow_new)
                index = self._node("scale", 2, (one,), Fraction(0), allow_new)
            elif op == "frozen_z20":
                if args or population != 2:
                    raise ValueError("frozen_z20 requires population 2")
                mark = tuple(getattr(current, "mark", ()))
                if len(mark) != 2:
                    raise ValueError("frozen_z20 requires a two-dimensional mark")
                terms = []
                for k in range(2):
                    seed = self._node("g"+str(k+1), 1, allow_new=allow_new)
                    terms.append(self._node("scale", 1, (seed,), self._fraction(mark[k]), allow_new))
                projection = self._node("add", 1, tuple(terms), allow_new=allow_new)
                hidden = self._node("tanh", 1, (projection,), allow_new=allow_new)
                index = self._node("action", 2, (hidden,), allow_new=allow_new)
            else:
                index = self._node(op, population, child_ids,
                                   getattr(current, "scalar", None), allow_new)
            results[identity] = index
            self._objects[identity] = current, index
        return results[id(word)]

    def _budget(self, replay_count=None):
        q = self.integration_count
        p = q if replay_count is None else _positive_integer(replay_count, "population_count")
        if max(p, q) > self.limits.max_points:
            raise CompilerResourceLimit("Gaussian cloud exceeds max_points")
        n = len(self.nodes)
        s = sum(node.op == "action" for node in self.nodes)
        if s > self.limits.max_sources:
            raise CompilerResourceLimit("finite program exceeds max_sources")
        edges = 2*n+s*s
        d = n if self._raw_dimensions is None else sum(self._raw_dimensions)
        if d > self.limits.max_nodes:
            raise CompilerResourceLimit("retained feature columns exceed max_nodes")
        units = q*(s*edges+4*s*s+3*d*d)+p*edges
        slots = (q+(p if p != q else 0))*(3*n+4*s+3*d+16)+8*s*s+6*d*d
        scalar_bytes = 8 if self.ar.digits is None else 160+4*((self.ar.digits+8)//9)
        memory = slots*scalar_bytes+512*n+1024*s*s
        result = dict(nodes=n, sources=s, initialization_nodes=q, population_nodes=p,
                      scalar_work_upper_bound=units, estimated_working_bytes=memory)
        if units > self.limits.max_work_units:
            raise CompilerResourceLimit(f"estimated scalar work {units} exceeds max_work_units")
        if memory > self.limits.max_working_bytes:
            raise CompilerResourceLimit(f"estimated working bytes {memory} exceeds max_working_bytes")
        return result

    def _normal_clouds(self, count):
        result = {}
        for population in (1, 2):
            dimension = (2 if population == 1 else 0)+sum(
                node.op == "action" and node.population == population for node in self.nodes)
            values = np.asarray(self.gaussian_points(count, dimension, self.ar))
            if values.shape != (count, dimension) or not self.ar.finite(values):
                raise ValueError("gaussian_points returned invalid joint nodes")
            result[population] = values
        return result

    def compile(self, words, population_nodes=None):
        if self._started:
            raise ValueError("compile is one-shot; rebuild the complete finite union")
        self._started = True
        words = tuple(words)
        if not words:
            raise ValueError("a finite program needs at least one requested word")
        for word in words:
            self._word(word)
        self.resource_estimate = self._budget(population_nodes)
        # All scalar/source/point/work/memory limits have passed before any
        # Gaussian cloud, node-value array, or factor is allocated.
        q, ar = self.integration_count, self.ar
        with ar.context():
            self._normals = self._normal_clouds(q)
            gaussian = {}
            for population in (1, 2):
                count = sum(node.op == "action" and node.population == population for node in self.nodes)
                self.factors[population] = ar.zeros((count, count))
                gaussian[population] = ar.zeros((q, count))
            values = []
            for index, node in enumerate(self.nodes):
                if node.op == "action":
                    self._new_source(index, values, gaussian)
                values.append(self._value(index, values, self._normals, gaussian))
                if not ar.finite(values[-1]):
                    raise CompilerNumericalError("nonfinite initialized word")
        self._values = values
        self._compiled = True
        return self

    def _value(self, index, values, normals, gaussian):
        node, ar = self.nodes[index], self.ar
        count = len(normals[node.population])
        if node.op == "one":
            return np.full(count, ar.real(1), dtype=ar.dtype)
        if node.op in ("g1", "g2"):
            return normals[1][:, int(node.op[1])-1].copy()
        if node.op == "action":
            source = self.sources[index]
            result = gaussian[node.population][:, source.index].copy()
            for operand, coefficient in source.response:
                if coefficient != 0:
                    result += coefficient*values[operand]
            return result
        first = values[node.args[0]]
        if node.op == "scale":
            return ar.real(node.scalar)*first
        if node.op == "sin":
            return ar.trig(first)
        if node.op == "cos":
            return ar.trig(first, cosine=True)
        if node.op == "tanh":
            return ar.tanh(first)
        if node.op == "add":
            return first+values[node.args[1]]
        if node.op == "multiply":
            return first*values[node.args[1]]
        raise ValueError("unimplemented initialized operation")

    def _partials(self, index, values, mean):
        """Reverse AD of the explicit source expression, covariance frozen."""
        ar = self.ar
        population = self.nodes[index].population
        count = len(values[index])
        source_count = len(self.source_lists[population])
        result = ar.zeros(source_count if mean else (count, source_count))
        adjoints = {index: np.full(count, ar.real(1), dtype=ar.dtype)}

        def push(target, contribution):
            if target in adjoints:
                adjoints[target] += contribution
            else:
                adjoints[target] = contribution.copy()

        for current in range(index, -1, -1):
            adjoint = adjoints.pop(current, None)
            if adjoint is None:
                continue
            node = self.nodes[current]
            if node.op == "action":
                source = self.sources[current]
                if mean:
                    result[source.index] += np.sum(adjoint)/ar.real(count)
                else:
                    result[:, source.index] += adjoint
                for operand, coefficient in source.response:
                    if coefficient != 0:
                        push(operand, adjoint*coefficient)
                # Its graph input is on the other population.  The scalar
                # answer is its named source plus response links, not a
                # differentiable matrix application to that input.
            elif node.op == "scale":
                push(node.args[0], adjoint*ar.real(node.scalar))
            elif node.op == "add":
                push(node.args[0], adjoint)
                push(node.args[1], adjoint)
            elif node.op == "multiply":
                push(node.args[0], adjoint*values[node.args[1]])
                push(node.args[1], adjoint*values[node.args[0]])
            elif node.op == "sin":
                push(node.args[0], adjoint*ar.trig(values[node.args[0]], cosine=True))
            elif node.op == "cos":
                push(node.args[0], -adjoint*ar.trig(values[node.args[0]]))
            elif node.op == "tanh":
                push(node.args[0], adjoint*(ar.real(1)-values[current]*values[current]))
            # Roots and constants have no named-source derivative.
        if not ar.finite(result):
            raise CompilerNumericalError("nonfinite frozen named-source derivative")
        return result

    def _new_source(self, index, values, gaussian):
        node, ar, q = self.nodes[index], self.ar, self.integration_count
        population, operand = node.population, node.args[0]
        previous = self.source_lists[population]
        opposite = self.source_lists[3-population]
        slot = len(previous)
        value = values[operand]
        variance = np.sum(value*value)/ar.real(q)+self.epsilon_cov
        cross = ar.zeros(slot)
        for k, source in enumerate(previous):
            cross[k] = np.sum(value*values[source.operand])/ar.real(q)
        lower = self.factors[population]
        row = ar.zeros(slot+1)
        for k in range(slot):
            row[k] = (cross[k]-np.sum(lower[k, :k]*row[:k]))/lower[k, k]
        schur = variance-np.sum(row[:slot]*row[:slot])
        if not ar.finite(np.asarray([schur])) or schur <= 0:
            raise CompilerNumericalError("positive covariance pivot unresolved; increase arithmetic precision")
        row[slot] = ar.sqrt(schur)[()]
        # Copy only the new row. Old factors, Gaussian variables and operand
        # values remain bit-for-bit unchanged inside this compilation.
        lower[slot, :slot+1] = row
        base = 2 if population == 1 else 0
        gaussian[population][:, slot] = self._normals[population][:, base:base+slot+1] @ row
        coefficients = self._partials(operand, values, mean=True)
        response = tuple((source.operand, coefficients[k]) for k, source in enumerate(opposite))
        source = Source(index, operand, population, slot, response)
        self.sources[index] = source
        previous.append(source)
        self.diagnostics.append(dict(population=population, source_index=slot,
                                     variance=variance, cross=cross.copy(),
                                     innovation_variance=schur,
                                     response_coefficients=coefficients.copy()))

    def _at_count(self, population_count=None):
        if not self._compiled:
            raise ValueError("compile a complete finite union before evaluation")
        count = self.integration_count if population_count is None else _positive_integer(population_count, "population_count")
        if count == self.integration_count:
            return self._values, self._normals
        if count == self._replay_count:
            return self._replay_values, self._replay_normals
        self._budget(count)
        # Keep at most one replay cache, in addition to the integration cloud.
        self._replay_values = self._replay_normals = None
        ar = self.ar
        with ar.context():
            normals = self._normal_clouds(count)
            gaussian = {}
            for population in (1, 2):
                base = 2 if population == 1 else 0
                gaussian[population] = normals[population][:, base:] @ self.factors[population].T
            values = []
            for index in range(len(self.nodes)):
                values.append(self._value(index, values, normals, gaussian))
                if not ar.finite(values[-1]):
                    raise CompilerNumericalError("nonfinite replayed initialized word")
        self._replay_count, self._replay_values, self._replay_normals = count, values, normals
        return values, normals

    def evaluate(self, word, population_count=None, derivative=False):
        if not isinstance(derivative, bool):
            raise ValueError("derivative must be boolean")
        index = self._word(word, allow_new=False)
        values, _ = self._at_count(population_count)
        with self.ar.context():
            if derivative:
                return values[index].copy(), self._partials(index, values, mean=False)
            return values[index].copy()

    def table(self, words, population_count=None):
        words = tuple(words)
        if not words:
            raise ValueError("table needs a nonempty same-population word list")
        indices = [self._word(word, allow_new=False) for word in words]
        if len({self.nodes[index].population for index in indices}) != 1:
            raise ValueError("table coordinates must belong to one population")
        values, _ = self._at_count(population_count)
        return np.column_stack([values[index] for index in indices])


def compile_raw_dictionary(first_words, second_words, *, arithmetic,
                           gaussian_points, initialization_nodes,
                           population_nodes, epsilon_cov, limits=None):
    """Return jointly sampled raw marks, raw Grams and one action contraction.

    Grams/C use the full Q-point integration union. The returned psi/g tables
    use a P-point replay of those *frozen* source factors and response numbers.
    C_reverse is a same-program diagnostic; C is never replaced or averaged
    with an independently estimated reverse map. Runtime uses normalized C
    and its transpose, and may discard ``program`` after initialization.
    """
    first_words, second_words = tuple(first_words), tuple(second_words)
    if not first_words or not second_words:
        raise ValueError("both raw dictionaries must be nonempty")
    for population, words in ((1, first_words), (2, second_words)):
        if any(getattr(word, "population", None) != population for word in words):
            raise ValueError("raw dictionary has an incorrect population")
    forward = tuple(_ActionRequest(word) for word in first_words)
    reverse = tuple(_ActionRequest(word) for word in second_words)
    program = GaussianCompiler(arithmetic, gaussian_points, initialization_nodes, epsilon_cov, limits)
    program._raw_dimensions = len(first_words), len(second_words)
    program.compile(first_words+second_words+forward+reverse, population_nodes=population_nodes)
    ar, q, p = arithmetic, program.integration_count, _positive_integer(population_nodes, "population_nodes")
    with ar.context():
        raw1q, raw2q = program.table(first_words), program.table(second_words)
        gram1, gram2 = raw1q.T @ raw1q/ar.real(q), raw2q.T @ raw2q/ar.real(q)
        C = raw2q.T @ program.table(forward)/ar.real(q)
        C_reverse = program.table(reverse).T @ raw1q/ar.real(q)
        psi1, psi2 = program.table(first_words, p), program.table(second_words, p)
        _, normals = program._at_count(p)
        g = normals[1][:, :2].copy()
        probabilities1 = np.full(p, ar.real(1)/ar.real(p), dtype=ar.dtype)
        probabilities2 = probabilities1.copy()
    metadata = dict(compiler="persistent-joint-Gaussian-v1", initialization_nodes=q,
                    population_nodes=p, epsilon_cov=str(program.epsilon_cov),
                    exact_canonical_gaussian_law=False,
                    contraction_orientation="forward; runtime reverse is transpose",
                    **{key: value for key, value in program.resource_estimate.items()
                       if key not in ("initialization_nodes", "population_nodes")})
    return RawInitialization(psi1, psi2, g, probabilities1, probabilities2,
                             gram1, gram2, C, C_reverse, program, metadata)
