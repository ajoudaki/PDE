"""Study-owned finite-depth initialized words and joint Gaussian compiler.

Each adjacent matrix has a distinct identity. Sources from different matrix /
orientation groups are independent, while covariance and transpose responses
within a group are retained. This is initialization, never neural training.
The maintained arithmetic and fixed-program implementation are dependencies.
"""
from fractions import Fraction
from itertools import combinations_with_replacement
import math

import numpy as np

from pde.observable_words import Word, unpair, rational_code
from pde.observable_compiler import (
    GaussianCompiler, CompilerLimits, CompilerResourceLimit,
    CompilerNumericalError, Source, _Node, _positive_integer,
)
from pde.observable_arithmetic import Arithmetic, gaussian_points


def _finite_float(value):
    """Optional reporting must not limit the exact arithmetic computation."""
    try:
        result = float(value)
        return result if math.isfinite(result) else None
    except (OverflowError, ValueError, TypeError):
        return None


def _condition_diagnostic(gram, eta):
    try:
        converted = np.asarray(gram, float)
        ridge = float(eta)
        if not np.all(np.isfinite(converted)) or not math.isfinite(ridge):
            return None
        return _finite_float(np.linalg.cond(converted+ridge*np.eye(len(converted))))
    except (OverflowError, ValueError, TypeError, np.linalg.LinAlgError):
        return None


class DepthWord(Word):
    __slots__ = ()

    def __init__(self, op, population, args=(), scalar=None):
        population = _positive_integer(population, "population")
        args = tuple(args)
        seed = op.startswith("g") and op[1:].isdigit() and int(op[1:]) >= 1
        arities = {"one": 0, "scale": 1, "sin": 1, "cos": 1,
                   "tanh": 1, "action": 1, "add": 2, "multiply": 2}
        if seed:
            arity = 0
        elif op in arities:
            arity = arities[op]
        else:
            raise ValueError("unsupported depth word operation")
        if len(args) != arity or any(not isinstance(a, DepthWord) for a in args):
            raise ValueError("invalid depth word operands")
        if seed and population != 1:
            raise ValueError("first-row roots belong to population one")
        if op == "action":
            if abs(args[0].population-population) != 1 or not args[0].bounded:
                raise ValueError("an initialized action joins adjacent populations on a bounded operand")
        elif any(a.population != population for a in args):
            raise ValueError("coordinate operations require the same population")
        if op == "multiply" and not all(a.bounded for a in args):
            raise ValueError("products require bounded operands")
        if op == "scale":
            if isinstance(scalar, bool) or not isinstance(scalar, (int, Fraction)):
                raise ValueError("word scalar must be an exact rational")
            scalar = Fraction(scalar)
        elif scalar is not None:
            raise ValueError("only scale has a scalar")
        bound = None
        if op in ("one", "sin", "cos", "tanh"):
            bound = Fraction(1)
        elif op == "scale" and args[0].bounded:
            bound = abs(scalar)*args[0].envelope
        elif op == "add" and all(a.bounded for a in args):
            bound = args[0].envelope+args[1].envelope
        elif op == "multiply":
            bound = args[0].envelope*args[1].envelope
        for key, value in (("op", op), ("population", population), ("args", args),
                           ("scalar", scalar), ("envelope", bound)):
            object.__setattr__(self, key, value)
        object.__setattr__(self, "_hash", hash((op, population, tuple(a._hash for a in args), scalar)))


def one(population):
    return DepthWord("one", population)


def root(coordinate):
    return DepthWord("g"+str(_positive_integer(coordinate, "coordinate")), 1)


def unary(op, word):
    return DepthWord(op, word.population, (word,))


def action(word, target):
    return DepthWord("action", target, (word,))


def add(left, right):
    return DepthWord("add", left.population, (left, right))


def scale(value, word):
    return DepthWord("scale", word.population, (word,), value)


def multiply(left, right):
    return DepthWord("multiply", left.population, (left, right))


def decode_prefix(order, depth, dimension):
    """Exhaustive natural grammar, with every dependency below its code."""
    decoded = [one(l) for l in range(1, depth+1)] + [root(i) for i in range(1, dimension+1)]
    base, width = depth+dimension, 6+2*(depth-1)
    for code in range(base, order+1):
        k, operation = divmod(code-base, width)
        try:
            if operation < 3:
                word = unary(("sin", "cos", "tanh")[operation], decoded[k])
            elif operation < 6:
                a, b = unpair(k)
                if operation == 3:
                    word = add(decoded[a], decoded[b])
                elif operation == 4:
                    word = multiply(decoded[a], decoded[b])
                else:
                    word = scale(rational_code(a), decoded[b])
            else:
                edge, direction = divmod(operation-6, 2)
                lower = edge+1
                source, target = (lower, lower+1) if direction == 0 else (lower+1, lower)
                if decoded[k] is None or decoded[k].population != source:
                    raise ValueError("wrong edge orientation")
                word = action(decoded[k], target)
        except (ValueError, AttributeError):
            word = None
        decoded.append(word)
    return decoded[:order+1]


def exponents(total, dimension):
    # Combinations enumerate descending lexicographic exponent tuples without
    # recursion in the input dimension. In particular fixed d>500 does not
    # introduce an unrelated interpreter recursion ceiling.
    for indices in combinations_with_replacement(range(dimension), total):
        powers = [0]*dimension
        for coordinate in indices:
            powers[coordinate] += 1
        yield tuple(powers)


def dictionary(order, depth, dimension, max_features=4096):
    """Adjacent forward/reverse tanh core plus an exhaustive bounded prefix."""
    order = _positive_integer(order, "order")
    depth = _positive_integer(depth, "depth")
    dimension = _positive_integer(dimension, "dimension")
    if depth < 2:
        raise ValueError("depth must be at least two")
    if math.comb(order+2*dimension, 2*dimension)+order+1 > max_features:
        raise CompilerResourceLimit("declared dictionary feature allowance exceeded")
    hidden = [tuple(unary("tanh", root(i)) for i in range(1, dimension+1))]
    for l in range(2, depth+1):
        hidden.append(tuple(unary("tanh", action(h, l)) for h in hidden[-1]))
    coordinates = []
    for l in range(1, depth+1):
        reverse = () if l == depth else tuple(unary("tanh", action(h, l)) for h in hidden[l])
        coordinates.append(hidden[l-1]+reverse)
    lists = []
    for l, xs in enumerate(coordinates, 1):
        polys = []
        for x in xs:
            terms = [one(l), x]
            for j in range(1, order):
                terms.append(add(scale(2, multiply(x, terms[-1])), scale(-1, terms[-2])))
            polys.append(terms)
        outputs = []
        for total in range(order+1):
            for powers in exponents(total, len(xs)):
                factors = [polys[i][p] for i, p in enumerate(powers) if p]
                word = one(l) if not factors else factors[0]
                for factor in factors[1:]:
                    word = multiply(word, factor)
                outputs.append(word)
        lists.append(outputs)
    seen = [set(words) for words in lists]
    for word in decode_prefix(order, depth, dimension):
        if word is not None and word.bounded and word not in seen[word.population-1]:
            lists[word.population-1].append(word)
            seen[word.population-1].add(word)
    return tuple(tuple(words) for words in lists)


class DepthGaussianCompiler(GaussianCompiler):
    """Maintained scalar AD/replay with explicit adjacent matrix identities."""
    def __init__(self, depth, dimension, *args, **kwargs):
        self.depth = _positive_integer(depth, "depth")
        self.dimension = _positive_integer(dimension, "dimension")
        super().__init__(*args, **kwargs)
        self.source_lists = {l: [] for l in range(1, self.depth+1)}

    def _node(self, op, population, args=(), scalar=None, allow_new=True):
        if isinstance(population, bool) or population not in self.source_lists:
            raise ValueError("population outside declared depth")
        seed = op.startswith("g") and op[1:].isdigit() and 1 <= int(op[1:]) <= self.dimension
        arities = {"one": 0, "scale": 1, "sin": 1, "cos": 1, "tanh": 1,
                   "action": 1, "add": 2, "multiply": 2}
        if (not seed and op not in arities) or len(args) != (0 if seed else arities[op]):
            raise ValueError("unsupported word operation or arity")
        parents = [self.nodes[i] for i in args]
        if seed and population != 1:
            raise ValueError("Gaussian roots belong to population one")
        if op == "action":
            if abs(parents[0].population-population) != 1 or parents[0].bound is None:
                raise ValueError("action requires a bounded adjacent-population operand")
        elif any(p.population != population for p in parents):
            raise ValueError("coordinate operations require one population")
        if op == "multiply" and any(p.bound is None for p in parents):
            raise ValueError("products require bounded operands")
        if op == "scale":
            scalar = self._fraction(scalar)
        elif scalar is not None:
            raise ValueError("only scale has a scalar")
        key = op, population, args, scalar
        if key in self._structural:
            return self._structural[key]
        if not allow_new:
            raise ValueError("word not in frozen finite union")
        if len(self.nodes) >= self.limits.max_nodes:
            raise CompilerResourceLimit("finite program exceeds max_nodes")
        bound = None
        if op in ("one", "sin", "cos", "tanh"):
            bound = Fraction(1)
        elif op == "scale" and parents[0].bound is not None:
            bound = abs(scalar)*parents[0].bound
        elif op == "add" and all(p.bound is not None for p in parents):
            bound = parents[0].bound+parents[1].bound
        elif op == "multiply":
            bound = parents[0].bound*parents[1].bound
        if bound is not None and max(bound.numerator.bit_length(), bound.denominator.bit_length()) > self.limits.max_scalar_bits:
            raise CompilerResourceLimit("word envelope exceeds scalar allowance")
        index = len(self.nodes)
        self.nodes.append(_Node(op, population, args, scalar, bound))
        self._structural[key] = index
        return index

    def _normal_clouds(self, count):
        result = {}
        for l in self.source_lists:
            size = (self.dimension if l == 1 else 0)+sum(n.op == "action" and n.population == l for n in self.nodes)
            values = np.asarray(self.gaussian_points(count, size, self.ar))
            if values.shape != (count, size) or not self.ar.finite(values):
                raise ValueError("invalid Gaussian cubature cloud")
            result[l] = values
        return result

    def compile(self, words, population_nodes=None):
        if self._started:
            raise ValueError("compile is one-shot")
        self._started = True
        words = tuple(words)
        if not words:
            raise ValueError("nonempty finite union required")
        for word in words:
            self._word(word)
        self.resource_estimate = self._budget(population_nodes)
        with self.ar.context():
            self._normals = self._normal_clouds(self.integration_count)
            gaussian = {}
            for l in self.source_lists:
                count = sum(n.op == "action" and n.population == l for n in self.nodes)
                self.factors[l] = self.ar.zeros((count, count))
                gaussian[l] = self.ar.zeros((self.integration_count, count))
            values = []
            for index, node in enumerate(self.nodes):
                if node.op == "action":
                    self._new_source(index, values, gaussian)
                values.append(self._value(index, values, self._normals, gaussian))
                if not self.ar.finite(values[-1]):
                    raise CompilerNumericalError("nonfinite initialized word")
        self._values, self._compiled = values, True
        return self

    def _value(self, index, values, normals, gaussian):
        op = self.nodes[index].op
        if op.startswith("g") and op[1:].isdigit():
            return normals[1][:, int(op[1:])-1].copy()
        return super()._value(index, values, normals, gaussian)

    def _new_source(self, index, values, gaussian):
        node, ar, q = self.nodes[index], self.ar, self.integration_count
        target, operand = node.population, node.args[0]
        origin = self.nodes[operand].population
        # SAME matrix and SAME orientation for covariance; SAME matrix and
        # OPPOSITE orientation for response. Other adjacent edges are excluded.
        previous = [s for s in self.source_lists[target] if self.nodes[s.operand].population == origin]
        opposite = [s for s in self.source_lists[origin] if self.nodes[s.operand].population == target]
        slot = len(self.source_lists[target])
        indices = [s.index for s in previous]
        variance = np.sum(values[operand]**2)/ar.real(q)+self.epsilon_cov
        cross = [np.sum(values[operand]*values[s.operand])/ar.real(q) for s in previous]
        lower, row = self.factors[target], ar.zeros(slot+1)
        for k, j in enumerate(indices):
            row[j] = (cross[k]-np.sum(lower[j, :j]*row[:j]))/lower[j, j]
        schur = variance-np.sum(row[:slot]**2)
        if not ar.finite(np.asarray([schur])) or schur <= 0:
            raise CompilerNumericalError("positive covariance pivot unresolved")
        row[slot] = ar.sqrt(schur)[()]
        lower[slot, :slot+1] = row
        base = self.dimension if target == 1 else 0
        gaussian[target][:, slot] = self._normals[target][:, base:base+slot+1] @ row
        coefficients = self._partials(operand, values, mean=True)
        response = tuple((s.operand, coefficients[s.index]) for s in opposite)
        source = Source(index, operand, target, slot, response)
        self.sources[index] = source
        self.source_lists[target].append(source)
        self.diagnostics.append(dict(matrix=max(origin, target), origin=origin,
                                     target=target, source_index=slot,
                                     variance=variance, innovation_variance=schur))

    def _at_count(self, population_count=None):
        if not self._compiled:
            raise ValueError("compile first")
        count = self.integration_count if population_count is None else _positive_integer(population_count, "population_count")
        if count == self.integration_count:
            return self._values, self._normals
        if count == self._replay_count:
            return self._replay_values, self._replay_normals
        self._budget(count)
        self._replay_values = self._replay_normals = None
        with self.ar.context():
            normals = self._normal_clouds(count)
            gaussian = {}
            for l in self.source_lists:
                base = self.dimension if l == 1 else 0
                gaussian[l] = normals[l][:, base:] @ self.factors[l].T
            values = []
            for i in range(len(self.nodes)):
                values.append(self._value(i, values, normals, gaussian))
                if not self.ar.finite(values[-1]):
                    raise CompilerNumericalError("nonfinite source replay")
        self._replay_count, self._replay_values, self._replay_normals = count, values, normals
        return values, normals


def initialize(order, depth=3, dimension=2, *, initialization_nodes=256,
               population_nodes=128, epsilon_cov="0.0001", digits=None,
               backend="decimal", limits=None, max_features=4096):
    ar = Arithmetic(digits, backend)
    lists = dictionary(order, depth, dimension, max_features)
    forward = [tuple(action(w, l+2) for w in lists[l]) for l in range(depth-1)]
    reverse = [tuple(action(w, l+1) for w in lists[l+1]) for l in range(depth-1)]
    program = DepthGaussianCompiler(depth, dimension, ar, gaussian_points,
                                    initialization_nodes, epsilon_cov, limits)
    program._raw_dimensions = tuple(map(len, lists))
    union = sum(lists, ()) + sum(forward, ()) + sum(reverse, ())
    program.compile(union, population_nodes)
    with ar.context():
        q = ar.real(initialization_nodes)
        raw = [program.table(words) for words in lists]
        grams = [r.T @ r/q for r in raw]
        eta = ar.real(Fraction(1, 1024*(order+1)**2))
        lower = [ar.cholesky(g+eta*ar.eye(len(g))) for g in grams]
        inverse = [ar.inverse_lower(l) for l in lower]
        b = [program.table(words, population_nodes) @ inv.T for words, inv in zip(lists, inverse)]
        contractions = [raw[l+1].T @ program.table(forward[l])/q for l in range(depth-1)]
        D = [inverse[l+1] @ contractions[l] @ inverse[l].T for l in range(depth-1)]
        _, normals = program._at_count(population_nodes)
        g = normals[1][:, :dimension].copy()
        pi = [np.full(population_nodes, ar.real(1)/ar.real(population_nodes), dtype=ar.dtype) for _ in lists]
        reverse_error = [_finite_float(np.max(np.abs(contractions[l]-program.table(reverse[l]).T @ raw[l]/q))) for l in range(depth-1)]
    metadata = dict(order=order, depth=depth, dimension=dimension,
                    initialization_nodes=initialization_nodes, population_nodes=population_nodes,
                    epsilon_cov=str(epsilon_cov), ridge=str(Fraction(1, 1024*(order+1)**2)),
                    feature_counts=list(map(len, lists)),
                    reverse_contraction_discrepancies=reverse_error,
                    compiler="depth-joint-sources-v1", resource_estimate=program.resource_estimate,
                    initialized_gram_condition=[_condition_diagnostic(v, eta) for v in grams],
                    diagnostic_null="unresolved, nonfinite, or outside float64 reporting range")
    # No program, source transcript, or initialization cloud enters dynamics.
    return dict(b=b, pi=pi, g=g, D=D, arithmetic=ar, metadata=metadata)
