"""Deterministic C-H2 population/action prototype.

The arrays are quadrature of two retained populations, never a sampled dense
neural network. Initialization uses named Gaussian sources and frozen response
partials. No training integrator, Monte Carlo, or width limit is implemented.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
import json
import math
from pathlib import Path
from typing import Any, Iterable

import numpy as np


class ResourceLimit(ValueError):
    """The requested explicit tensor rule exceeds a declared resource limit."""


class NumericalInitializationError(ValueError):
    """Floating Gaussian or ridge algebra cannot resolve the requested input."""


def _integer(value: Any, name: str, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, (int, np.integer)):
        raise ValueError(f"{name} must be an integer")
    if value < minimum:
        raise ValueError(f"{name} must be at least {minimum}")
    return int(value)


def _array(value: Any, name: str, ndim: int | None = None) -> np.ndarray:
    original = np.asarray(value)
    if original.dtype.kind not in "iuf" or original.dtype.kind == "b":
        raise ValueError(f"{name} must contain real numbers")
    result = np.array(original, dtype=float, copy=True)
    if ndim is not None and result.ndim != ndim:
        raise ValueError(f"{name} must have {ndim} dimensions")
    if not np.all(np.isfinite(result)):
        raise ValueError(f"{name} must be finite")
    return result


def _probabilities(value: Any, count: int, name: str) -> np.ndarray:
    result = _array(value, name, 1)
    if result.shape != (count,) or count == 0:
        raise ValueError(f"{name} has the wrong nonempty shape")
    if np.any(result < 0) or not np.isclose(result.sum(), 1.0, rtol=0, atol=2e-12):
        raise ValueError(f"{name} must be nonnegative and sum to one")
    return result


@dataclass(frozen=True)
class Word:
    op: str
    population: int
    args: tuple["Word", ...] = ()
    scalar: Fraction | None = None
    mark: tuple[float, ...] = ()
    envelope: float | None = None

    @property
    def bounded(self) -> bool:
        return self.envelope is not None


def constant(population: int) -> Word:
    if population not in (1, 2):
        raise ValueError("population must be 1 or 2")
    return Word("one", population, envelope=1.0)


def seed(name: str) -> Word:
    if name in ("g1", "g2", "w1", "w2"):
        return Word(name, 1)
    if name == "c":
        # Bounded readout seed; its actual bound is a runtime/horizon premise.
        return Word(name, 2, envelope=float("inf"))
    raise ValueError("unknown seed")


def unary(op: str, word: Word) -> Word:
    if op not in ("sin", "cos", "tanh"):
        raise ValueError("unknown unary operation")
    return Word(op, word.population, (word,), envelope=1.0)


def add(left: Word, right: Word) -> Word:
    if left.population != right.population:
        raise ValueError("addition requires one population")
    bound = left.envelope + right.envelope if left.bounded and right.bounded else None
    return Word("add", left.population, (left, right), envelope=bound)


def multiply(left: Word, right: Word) -> Word:
    if left.population != right.population or not left.bounded or not right.bounded:
        raise ValueError("product operands must be bounded on one population")
    return Word("multiply", left.population, (left, right), envelope=left.envelope * right.envelope)


def scale(value: Fraction | int, word: Word) -> Word:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise ValueError("word scalars must be rational")
    value = Fraction(value)
    bound = abs(float(value)) * word.envelope if word.bounded else None
    return Word("scale", word.population, (word,), scalar=value, envelope=bound)


def action(word: Word) -> Word:
    if not word.bounded:
        raise ValueError("actions require a bounded word")
    return Word("action", 3 - word.population, (word,))


def frozen_z20(direction: Iterable[float]) -> Word:
    u = _array(tuple(direction), "direction", 1)
    if u.shape != (2,):
        raise ValueError("a frozen direction has two coordinates")
    return Word("frozen_z20", 2, mark=tuple(u))


def pair(a: int, b: int) -> int:
    a, b = _integer(a, "a"), _integer(b, "b")
    return (a + b) * (a + b + 1) // 2 + b


def unpair(k: int) -> tuple[int, int]:
    k = _integer(k, "code")
    total = (math.isqrt(8 * k + 1) - 1) // 2
    b = k - total * (total + 1) // 2
    return total - b, b


def rational_code(a: int) -> Fraction:
    p, q = unpair(a)
    signed = 0 if p == 0 else (p + 1) // 2 if p % 2 else -(p // 2)
    return Fraction(signed, q + 1)


@lru_cache(maxsize=100000)
def decode_word(n: int) -> Word | None:
    """Decode exactly the candidate's natural-number grammar; invalid is None."""
    n = _integer(n, "word code")
    if n < 4:
        return (constant(1), constant(2), seed("g1"), seed("g2"))[n]
    k, op = divmod(n - 4, 8)
    try:
        if op <= 3:
            child = decode_word(k)
            if child is None:
                return None
            return action(child) if op == 3 else unary(("sin", "cos", "tanh")[op], child)
        a, b = unpair(k)
        right = decode_word(b)
        if right is None:
            return None
        if op == 6:
            return scale(rational_code(a), right)
        left = decode_word(a)
        if left is None:
            return None
        return multiply(left, right) if op == 5 else add(left, right)
    except ValueError:
        return None


def pilot_words() -> dict[str, Word]:
    g1, g2 = seed("g1"), seed("g2")
    h1, h2 = unary("sin", g1), unary("sin", g2)
    z1, z2 = action(h1), action(h2)
    s1, s2 = unary("sin", z1), unary("sin", z2)
    p1, p2 = action(s1), action(s2)
    return dict(one1=constant(1), g1=g1, g2=g2, h1=h1, h2=h2,
                z1=z1, z2=z2, s1=s1, s2=s2, p1=p1, p2=p2,
                t1=unary("tanh", p1), t2=unary("tanh", p2), one2=constant(2))


def initial_dictionary(order: int, max_codes: int = 10000) -> tuple[list[Word], list[Word], list[Word]]:
    order = _integer(order, "order", 1)
    if order > _integer(max_codes, "max_codes", 1):
        raise ResourceLimit("word prefix exceeds max_codes")
    targets = list(pilot_words().values())
    targets.extend(word for code in range(order + 1) if (word := decode_word(code)) is not None)
    first = [word for word in targets if word.population == 1 and word.bounded]
    second = [word for word in targets if word.population == 2 and word.bounded]
    return first, second, targets


@dataclass(frozen=True)
class QuadratureLimits:
    order: int = 5
    max_nodes: int = 100000
    max_innovation_dimension: int = 7
    max_named_sources: int = 32
    roundoff_tolerance: float = 2e-11

    def __post_init__(self) -> None:
        _integer(self.order, "quadrature order", 2)
        _integer(self.max_nodes, "max_nodes", 1)
        _integer(self.max_innovation_dimension, "max_innovation_dimension", 0)
        _integer(self.max_named_sources, "max_named_sources", 1)
        if not math.isfinite(self.roundoff_tolerance) or self.roundoff_tolerance < 0:
            raise ValueError("roundoff_tolerance must be finite and nonnegative")


def gaussian_rule(dimension: int, limits: QuadratureLimits) -> tuple[np.ndarray, np.ndarray]:
    dimension = _integer(dimension, "Gaussian dimension")
    nodes = limits.order ** dimension
    if dimension > limits.max_innovation_dimension or nodes > limits.max_nodes:
        raise ResourceLimit(f"GH rule requires dimension {dimension}, {nodes} nodes")
    if dimension == 0:
        return np.zeros((1, 0)), np.ones(1)
    x, p = np.polynomial.hermite.hermgauss(limits.order)
    x, p = np.sqrt(2.0) * x, p / np.sqrt(np.pi)
    index = np.indices((limits.order,) * dimension).reshape(dimension, -1).T
    return x[index], np.prod(p[index], axis=1)


@dataclass
class Source:
    name: str
    word: Word
    operand: Word
    gaussian_index: int
    response: tuple[tuple[Word, float], ...]


@dataclass
class _Carrier:
    population: int
    limits: QuadratureLimits
    factor: np.ndarray = field(default_factory=lambda: np.zeros((0, 0)))
    sources: list[Source] = field(default_factory=list)
    nodes: np.ndarray = field(init=False)
    weights: np.ndarray = field(init=False)
    gaussian: np.ndarray = field(init=False)

    def __post_init__(self) -> None:
        self.refresh()

    def refresh(self) -> None:
        base = 2 if self.population == 1 else 0
        self.nodes, self.weights = gaussian_rule(base + self.factor.shape[1], self.limits)
        self.gaussian = self.nodes[:, base:] @ self.factor.T


class GaussianProgram:
    """Finite Gaussian-source compiler with frozen named-source derivatives.

    Each source covariance is the uncentered operand Gram. Each answer is its
    named centered source plus all opposite-input response terms. AD treats
    named correlated sources as formal independent coordinates, holding their
    law and all previously computed response coefficients fixed.
    """

    def __init__(self, limits: QuadratureLimits | None = None):
        self.limits = limits or QuadratureLimits()
        self.carriers = {i: _Carrier(i, self.limits) for i in (1, 2)}
        self.sources: dict[Word, Source] = {}
        self.diagnostics: list[dict[str, Any]] = []

    def compile(self, words: Iterable[Word]) -> "GaussianProgram":
        words = tuple(words)
        if not words:
            raise ValueError("a source program must request at least one word")
        for word in words:
            self._visit(word)
        return self

    def _visit(self, word: Word) -> None:
        if not isinstance(word, Word):
            raise ValueError("source programs require typed words")
        if word.op in ("c", "w1", "w2", "frozen_z20"):
            raise ValueError("initial programs use g and explicit initialized actions")
        for arg in word.args:
            self._visit(arg)
        if word.op == "action" and word not in self.sources:
            self._new_source(word)

    def evaluate(self, word: Word, derivative: bool = False) -> np.ndarray | tuple[np.ndarray, np.ndarray]:
        value, gradient = self._evaluate(word, {})
        if not np.all(np.isfinite(value)) or not np.all(np.isfinite(gradient)):
            raise NumericalInitializationError("nonfinite initialized word or named derivative")
        return (value.copy(), gradient.copy()) if derivative else value.copy()

    def _evaluate(self, word: Word, cache: dict[Word, tuple[np.ndarray, np.ndarray]]) -> tuple[np.ndarray, np.ndarray]:
        if word in cache:
            return cache[word]
        carrier = self.carriers[word.population]
        size, count = len(carrier.weights), len(carrier.sources)
        if word.op == "one":
            result = np.ones(size), np.zeros((size, count))
        elif word.op in ("g1", "g2"):
            result = carrier.nodes[:, int(word.op[1]) - 1], np.zeros((size, count))
        elif word.op == "action":
            if word not in self.sources:
                raise ValueError("action has not been compiled")
            source = self.sources[word]
            value = carrier.gaussian[:, source.gaussian_index].copy()
            gradient = np.zeros((size, count))
            gradient[:, source.gaussian_index] = 1.0
            for previous_input, coefficient in source.response:
                v, d = self._evaluate(previous_input, cache)
                value += coefficient * v
                gradient += coefficient * d
            result = value, gradient
        elif word.op in ("sin", "cos", "tanh"):
            v, d = self._evaluate(word.args[0], cache)
            if word.op == "sin":
                result = np.sin(v), np.cos(v)[:, None] * d
            elif word.op == "cos":
                result = np.cos(v), -np.sin(v)[:, None] * d
            else:
                value = np.tanh(v)
                result = value, (1 - value * value)[:, None] * d
        elif word.op == "scale":
            v, d = self._evaluate(word.args[0], cache)
            result = float(word.scalar) * v, float(word.scalar) * d
        elif word.op in ("add", "multiply"):
            v, dv = self._evaluate(word.args[0], cache)
            w, dw = self._evaluate(word.args[1], cache)
            result = (v + w, dv + dw) if word.op == "add" else (v * w, dv * w[:, None] + dw * v[:, None])
        else:
            raise ValueError(f"unsupported initialized operation {word.op}")
        cache[word] = result
        return result

    def expectation(self, word: Word) -> float:
        return float(self.carriers[word.population].weights @ self.evaluate(word))

    def _new_source(self, word: Word) -> None:
        operand = word.args[0]
        if not operand.bounded:
            raise ValueError("source operands must be bounded")
        out = self.carriers[word.population]
        inside = self.carriers[operand.population]
        if len(self.sources) >= self.limits.max_named_sources:
            raise ResourceLimit("source count exceeds max_named_sources")
        value, derivative = self._evaluate(operand, {})
        if not np.all(np.isfinite(value)) or not np.all(np.isfinite(derivative)):
            raise NumericalInitializationError("nonfinite Gaussian-source input")
        variance = float(inside.weights @ (value * value))
        previous = [self._evaluate(s.operand, {})[0] for s in out.sources]
        covariance = np.array([inside.weights @ (value * v) for v in previous])
        response = tuple((s.operand, float(inside.weights @ derivative[:, j]))
                         for j, s in enumerate(inside.sources))
        if not math.isfinite(variance) or not np.all(np.isfinite(covariance)) or not all(math.isfinite(c) for _, c in response):
            raise NumericalInitializationError("nonfinite Gaussian covariance or response")
        factor = out.factor
        innovation_count = factor.shape[1]
        if innovation_count:
            q, r = np.linalg.qr(factor, mode="reduced")
            try:
                coefficient = np.linalg.solve(r, q.T @ covariance)
            except np.linalg.LinAlgError as exc:
                raise NumericalInitializationError("unresolved Gaussian covariance range") from exc
        else:
            coefficient = np.zeros(0)
        mismatch = float(np.linalg.norm(factor @ coefficient - covariance))
        tolerance = self.limits.roundoff_tolerance * max(1.0, variance, float(np.linalg.norm(covariance)))
        if mismatch > tolerance:
            raise NumericalInitializationError("new covariance is outside the existing source range")
        schur = variance - float(coefficient @ coefficient)
        correction = 0.0
        if schur < 0:
            if schur < -tolerance:
                raise NumericalInitializationError("negative Gaussian Schur complement")
            correction, schur = -schur, 0.0
        # Retain every positive innovation, however small. Exact zero adds a
        # named derivative coordinate but needs no new independent Gaussian.
        positive = schur > 0
        new_factor = np.zeros((len(out.sources) + 1, innovation_count + int(positive)))
        new_factor[:-1, :innovation_count] = factor
        new_factor[-1, :innovation_count] = coefficient
        if positive:
            new_factor[-1, -1] = np.sqrt(schur)
        base = 2 if word.population == 1 else 0
        dimension = base + new_factor.shape[1]
        if dimension > self.limits.max_innovation_dimension or self.limits.order ** dimension > self.limits.max_nodes:
            raise ResourceLimit(f"new source would require dimension {dimension}, {self.limits.order ** dimension} GH nodes")
        name = ("F" if word.population == 2 else "R") + str(len(out.sources))
        source = Source(name, word, operand, len(out.sources), response)
        out.factor = new_factor
        out.sources.append(source)
        self.sources[word] = source
        out.refresh()
        self.diagnostics.append(dict(name=name, population=word.population,
                                     variance=variance, covariance=covariance.tolist(),
                                     response=[co for _, co in response],
                                     innovation_variance=schur,
                                     covariance_range_residual=mismatch,
                                     negative_schur_roundoff_correction=correction,
                                     named_sources=len(out.sources),
                                     independent_source_dimensions=new_factor.shape[1]))


def ridge_features(raw: Any, probabilities: Any, order: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    raw = _array(raw, "raw dictionary", 2)
    if min(raw.shape) == 0:
        raise ValueError("dictionary must have nonempty rows and columns")
    probabilities = _probabilities(probabilities, len(raw), "dictionary probabilities")
    order = _integer(order, "order", 1)
    eta = math.ldexp(1.0, -order)
    if eta == 0:
        raise NumericalInitializationError("requested ridge underflows float64")
    gram = raw.T @ (probabilities[:, None] * raw)
    if not np.all(np.isfinite(gram)):
        raise NumericalInitializationError("nonfinite dictionary Gram")
    regularized = (gram + gram.T) / 2 + eta * np.eye(raw.shape[1])
    eigenvalues, eigenvectors = np.linalg.eigh(regularized)
    if np.any(eigenvalues <= 0):
        raise NumericalInitializationError("positive ridge is unresolved in float64; no modes were dropped")
    transform = (eigenvectors * (1 / np.sqrt(eigenvalues))) @ eigenvectors.T
    features = raw @ transform.T
    if not np.all(np.isfinite(features)):
        raise NumericalInitializationError("nonfinite ridge features")
    return features, transform, gram


@dataclass
class Population1:
    b: np.ndarray
    g: np.ndarray
    w: np.ndarray
    probabilities: np.ndarray

    def __post_init__(self) -> None:
        self.b, self.g, self.w = (_array(getattr(self, k), k, 2) for k in ("b", "g", "w"))
        if min(self.b.shape) == 0 or self.g.shape != (len(self.b), 2) or self.w.shape != self.g.shape:
            raise ValueError("population 1 requires nonempty (b,g,w), with two-dimensional g,w")
        self.probabilities = _probabilities(self.probabilities, len(self.b), "population 1 probabilities")


@dataclass
class Population2:
    b: np.ndarray
    c: np.ndarray
    probabilities: np.ndarray

    def __post_init__(self) -> None:
        self.b, self.c = _array(self.b, "b", 2), _array(self.c, "c", 1)
        if min(self.b.shape) == 0 or self.c.shape != (len(self.b),):
            raise ValueError("population 2 requires nonempty (b,c)")
        self.probabilities = _probabilities(self.probabilities, len(self.b), "population 2 probabilities")


@dataclass
class State:
    first: Population1
    second: Population2
    M: np.ndarray
    D: np.ndarray
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.M, self.D = _array(self.M, "M", 2), _array(self.D, "D", 2)
        expected = (self.second.b.shape[1], self.first.b.shape[1])
        if self.M.shape != expected or self.D.shape != expected:
            raise ValueError("M and D must index the two retained feature lists")

    def copy(self) -> "State":
        return State(Population1(self.first.b, self.first.g, self.first.w, self.first.probabilities),
                     Population2(self.second.b, self.second.c, self.second.probabilities),
                     self.M, self.D, json.loads(json.dumps(self.metadata)))


@dataclass
class DataLaw:
    inputs: np.ndarray
    labels: np.ndarray
    probabilities: np.ndarray

    def __post_init__(self) -> None:
        self.inputs = _array(self.inputs, "inputs", 2)
        self.labels = _array(self.labels, "labels", 1)
        if len(self.inputs) == 0 or self.inputs.shape[1] != 2 or self.labels.shape != (len(self.inputs),):
            raise ValueError("nonempty data require (m,2) unit inputs and m labels")
        if not np.allclose(np.linalg.norm(self.inputs, axis=1), 1, rtol=0, atol=2e-12):
            raise ValueError("inputs must lie on the unit circle")
        self.probabilities = _probabilities(self.probabilities, len(self.inputs), "data probabilities")


@dataclass
class Velocity:
    w: np.ndarray
    c: np.ndarray
    M: np.ndarray


def _word_record(word: Word) -> dict[str, Any]:
    return dict(op=word.op, population=word.population, args=[_word_record(a) for a in word.args],
                scalar=None if word.scalar is None else [word.scalar.numerator, word.scalar.denominator])


def initialize(order: int = 1, limits: QuadratureLimits | None = None) -> tuple[State, GaussianProgram]:
    order = _integer(order, "order", 1)
    if order > 1074 or math.ldexp(1.0, -order) == 0:
        raise NumericalInitializationError("requested ridge underflows float64")
    first_words, second_words, targets = initial_dictionary(order)
    program = GaussianProgram(limits).compile(targets)
    # Compile the entire raw contraction union before extracting either law.
    forward_words = [action(word) for word in first_words]
    program.compile(forward_words)
    raw1 = np.column_stack([program.evaluate(word) for word in first_words])
    raw2 = np.column_stack([program.evaluate(word) for word in second_words])
    weights1, weights2 = (program.carriers[i].weights for i in (1, 2))
    b1, transform1, gram1 = ridge_features(raw1, weights1, order)
    b2, transform2, gram2 = ridge_features(raw2, weights2, order)
    raw_forward = np.column_stack([program.evaluate(word) for word in forward_words])
    contraction = raw2.T @ (weights2[:, None] * raw_forward)
    D = transform2 @ contraction @ transform1
    g = program.carriers[1].nodes[:, :2]
    metadata = dict(format="C-H2-quadrature-v1", hierarchy_order=order, ridge=math.ldexp(1.0, -order),
                    gaussian_order=program.limits.order, exact_initial_law=False,
                    dictionary1=[_word_record(w) for w in first_words],
                    dictionary2=[_word_record(w) for w in second_words],
                    source_diagnostics=program.diagnostics,
                    gram1=gram1.tolist(), gram2=gram2.tolist(),
                    normalization1=transform1.tolist(), normalization2=transform2.tolist(),
                    initialization_operator_norm=float(np.linalg.norm(D, ord=2)))
    state = State(Population1(b1, g, g, weights1), Population2(b2, np.zeros(len(b2)), weights2), D, D, metadata)
    return state, program


def _validate_state(state: State) -> None:
    # Arrays remain mutable for supplied-state work, so reject corruptions at
    # every evaluation rather than relying on constructor validation alone.
    for name, array in (("w", state.first.w), ("c", state.second.c), ("M", state.M),
                        ("b1", state.first.b), ("g", state.first.g), ("b2", state.second.b), ("D", state.D)):
        if not np.all(np.isfinite(array)):
            raise ValueError(f"nonfinite state coordinate {name}")
    if state.first.w.shape != state.first.g.shape or state.first.g.shape != (len(state.first.b), 2):
        raise ValueError("invalid first-population state shape")
    if state.second.c.shape != (len(state.second.b),):
        raise ValueError("invalid second-population state shape")
    expected = (state.second.b.shape[1], state.first.b.shape[1])
    if state.M.shape != expected or state.D.shape != expected:
        raise ValueError("invalid action matrix shape")
    _probabilities(state.first.probabilities, len(state.first.b), "first probabilities")
    _probabilities(state.second.probabilities, len(state.second.b), "second probabilities")


def apply_action(state: State, input_population: int, values: Any, frozen: bool = False) -> np.ndarray:
    _validate_state(state)
    if input_population not in (1, 2):
        raise ValueError("input population must be 1 or 2")
    values = _array(values, "action values")
    population = state.first if input_population == 1 else state.second
    if values.ndim not in (1, 2) or values.shape[0] != len(population.b):
        raise ValueError("action values must use the retained input population")
    scalar = values.ndim == 1
    if scalar:
        values = values[:, None]
    matrix = state.D if frozen else state.M
    coefficients = population.b.T @ (population.probabilities[:, None] * values)
    output = state.second.b @ matrix @ coefficients if input_population == 1 else state.first.b @ matrix.T @ coefficients
    if not np.all(np.isfinite(output)):
        raise ValueError("nonfinite action output")
    return output[:, 0] if scalar else output


def fields(state: State, inputs: Any) -> dict[str, np.ndarray]:
    _validate_state(state)
    inputs = _array(inputs, "observation inputs", 2)
    if len(inputs) == 0 or inputs.shape[1] != 2:
        raise ValueError("observation inputs must have nonempty shape (m,2)")
    first, second = state.first, state.second
    h1 = np.tanh(first.w @ inputs.T)
    a = first.b.T @ (first.probabilities[:, None] * h1)
    z2 = second.b @ state.M @ a
    h2 = np.tanh(z2)
    delta2 = second.c[:, None] * (1 - h2 * h2)
    d = second.b.T @ (second.probabilities[:, None] * delta2)
    q = first.b @ state.M.T @ d
    f = second.probabilities @ (second.c[:, None] * h2)
    result = dict(h1=h1, a=a, z2=z2, h2=h2, delta2=delta2, d=d, q=q, f=f)
    if not all(np.all(np.isfinite(v)) for v in result.values()):
        raise ValueError("nonfinite evaluated field")
    return result


def loss(state: State, data: DataLaw) -> float:
    DataLaw(data.inputs, data.labels, data.probabilities)
    residual = fields(state, data.inputs)["f"] - data.labels
    result = float(data.probabilities @ (residual * residual))
    if not math.isfinite(result):
        raise ValueError("nonfinite loss")
    return result


def rhs(state: State, data: DataLaw) -> Velocity:
    DataLaw(data.inputs, data.labels, data.probabilities)
    values = fields(state, data.inputs)
    weighted_residual = data.probabilities * (values["f"] - data.labels)
    w = -2 * ((1 - values["h1"] ** 2) * values["q"] * weighted_residual) @ data.inputs
    c = -2 * values["h2"] @ weighted_residual
    M = -2 * (values["d"] * weighted_residual) @ values["a"].T
    return Velocity(w, c, M)


def velocity_squared_norm(state: State, velocity: Velocity) -> float:
    return float(state.first.probabilities @ np.sum(velocity.w ** 2, axis=1)
                 + state.second.probabilities @ (velocity.c ** 2) + np.sum(velocity.M ** 2))


def algebraic_update(state: State, velocity: Velocity, step: float) -> State:
    """One simultaneous algebraic state map; this is not a trajectory solver."""
    if isinstance(step, bool) or not math.isfinite(step):
        raise ValueError("step must be a finite real scalar")
    result = state.copy()
    if velocity.w.shape != result.first.w.shape or velocity.c.shape != result.second.c.shape or velocity.M.shape != result.M.shape:
        raise ValueError("velocity shape mismatch")
    result.first.w += step * velocity.w
    result.second.c += step * velocity.c
    result.M += step * velocity.M
    _validate_state(result)
    return result


def observe(state: State, word: Word) -> np.ndarray:
    _validate_state(state)
    cache: dict[Word, np.ndarray] = {}

    def visit(node: Word) -> np.ndarray:
        if node in cache:
            return cache[node]
        population = state.first if node.population == 1 else state.second
        if node.op == "one":
            result = np.ones(len(population.b))
        elif node.op in ("g1", "g2", "w1", "w2"):
            coordinates = state.first.g if node.op[0] == "g" else state.first.w
            result = coordinates[:, int(node.op[1]) - 1]
        elif node.op == "c":
            result = state.second.c
        elif node.op == "frozen_z20":
            result = apply_action(state, 1, np.tanh(state.first.g @ np.asarray(node.mark)), frozen=True)
        elif node.op == "action":
            result = apply_action(state, node.args[0].population, visit(node.args[0]))
        elif node.op in ("sin", "cos", "tanh"):
            result = getattr(np, node.op)(visit(node.args[0]))
        elif node.op == "scale":
            result = float(node.scalar) * visit(node.args[0])
        elif node.op == "add":
            result = visit(node.args[0]) + visit(node.args[1])
        elif node.op == "multiply":
            result = visit(node.args[0]) * visit(node.args[1])
        else:
            raise ValueError("unknown observation node")
        cache[node] = result
        return result

    result = visit(word)
    if not np.all(np.isfinite(result)):
        raise ValueError("nonfinite observation")
    return result.copy()


def joint_observe(state: State, words: Iterable[Word]) -> tuple[np.ndarray, np.ndarray]:
    words = tuple(words)
    if not words or any(word.population != words[0].population for word in words):
        raise ValueError("joint observations require a nonempty same-population tuple")
    population = state.first if words[0].population == 1 else state.second
    return np.column_stack([observe(state, word) for word in words]), population.probabilities.copy()


def save_restart(path: str | Path, state: State, data: DataLaw) -> None:
    """Save complete current quadrature populations, fixed inputs, and M; no clock."""
    _validate_state(state)
    DataLaw(data.inputs, data.labels, data.probabilities)
    with Path(path).open("wb") as handle:
        np.savez_compressed(handle, b1=state.first.b, g=state.first.g, w=state.first.w,
                            p1=state.first.probabilities, b2=state.second.b, c=state.second.c,
                            p2=state.second.probabilities, M=state.M, D=state.D,
                            inputs=data.inputs, labels=data.labels, data_p=data.probabilities,
                            metadata=np.array(json.dumps(state.metadata, sort_keys=True)))


def load_restart(path: str | Path) -> tuple[State, DataLaw]:
    with np.load(path, allow_pickle=False) as saved:
        expected = {"b1", "g", "w", "p1", "b2", "c", "p2", "M", "D", "inputs", "labels", "data_p", "metadata"}
        if set(saved.files) != expected:
            raise ValueError("invalid restart schema")
        metadata = json.loads(str(saved["metadata"]))
        if metadata.get("format") != "C-H2-quadrature-v1":
            raise ValueError("unsupported restart format")
        state = State(Population1(saved["b1"], saved["g"], saved["w"], saved["p1"]),
                      Population2(saved["b2"], saved["c"], saved["p2"]), saved["M"], saved["D"], metadata)
        data = DataLaw(saved["inputs"], saved["labels"], saved["data_p"])
    return state, data
