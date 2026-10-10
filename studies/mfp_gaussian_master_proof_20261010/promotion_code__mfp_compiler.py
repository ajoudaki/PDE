"""Typed finite-program MFP compiler. See code/MFP_CALCULUS.md for the contract.

Only the Python standard library and sibling mfp_expr are used. Gaussian
expectations are symbolic integrals, not numerical approximations.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math
import re

from . import mfp_expr as ex


class ProgramError(ValueError):
    """An operation is outside the declared typed language."""


@dataclass(frozen=True, eq=False)
class Node:
    program: "Program"
    index: int
    op: str
    kind: str | None                 # None denotes a scalar
    args: tuple["Node", ...] = ()
    data: object = None

    def __add__(self, other):
        return self.program.binary("add", self, other)

    __radd__ = __add__

    def __mul__(self, other):
        return self.program.binary("mul", self, other)

    __rmul__ = __mul__

    def __neg__(self):
        return self * -1

    def __sub__(self, other):
        return self + (-self.program.coerce(other))

    def __rsub__(self, other):
        return self.program.coerce(other) + (-self)

    def __truediv__(self, other):
        if not isinstance(other, (int, float, Fraction)) or not other:
            raise ProgramError("Division is allowed only by a nonzero numeric constant")
        return self * (Fraction(1) / Fraction(str(other)))

    def __pow__(self, power):
        if type(power) is not int or power < 0:
            raise ProgramError("Only nonnegative integer powers are admitted")
        out = self.program.one(self.kind)
        for _ in range(power):
            out = out * self
        return out


@dataclass(frozen=True, eq=False)
class Matrix:
    program: "Program"
    name: str
    source: str
    target: str

    def __matmul__(self, vector):
        return self.program.call(self, vector)

    @property
    def T(self):
        return Transpose(self)

    def __add__(self, other):
        return self.program.represented(self) + other


@dataclass(frozen=True)
class Transpose:
    matrix: object

    def __matmul__(self, vector):
        return self.matrix.program.call(self.matrix, vector, transpose=True)

    @property
    def T(self):
        return self.matrix


@dataclass(frozen=True)
class RankMatrix:
    """base + sum coefficient * left * right.T / n; no dense direction."""
    program: "Program"
    source: str
    target: str
    base: Matrix | None = None
    terms: tuple[tuple[Node, Node, Node], ...] = ()

    def __matmul__(self, vector):
        return self.program.call(self, vector)

    @property
    def T(self):
        return Transpose(self)

    def __add__(self, other):
        if isinstance(other, Matrix):
            other = self.program.represented(other)
        if not isinstance(other, RankMatrix) or other.program is not self.program:
            raise ProgramError("Matrix addition requires a represented matrix in this program")
        if (self.source, self.target) != (other.source, other.target):
            raise ProgramError("Matrix types do not match")
        if self.base is not None and other.base is not None:
            raise ProgramError("A matrix state has at most one initialized base")
        return RankMatrix(self.program, self.source, self.target,
                          self.base or other.base, self.terms + other.terms)

    def __mul__(self, coefficient):
        if self.base is not None:
            raise ProgramError("Scale a matrix action, not an initialized matrix state")
        c = self.program.scalar(coefficient)
        return RankMatrix(self.program, self.source, self.target, None,
                          tuple((c * a, u, v) for a, u, v in self.terms))

    __rmul__ = __mul__

    def __neg__(self):
        return self * -1


def _name(name):
    if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", name):
        raise ProgramError("Names must be identifiers beginning with a letter")


class Program:
    """Build typed expressions, expand physical derivatives, then compile a limit."""

    def __init__(self):
        self.nodes = []
        self.types = set()
        self.names = set()
        self.matrices = []
        self.root_cov = {}
        self.root_mean = {}
        self.trace = []

    def _record(self, rule, **details):
        self.trace.append(dict(stage="finite", rule=rule, **details))

    def _node(self, op, kind=None, args=(), data=None):
        node = Node(self, len(self.nodes), op, kind, tuple(args), data)
        self.nodes.append(node)
        return node

    def _reserve(self, name):
        _name(name)
        if name in self.names:
            raise ProgramError(f"Name {name!r} is already in use; reuse its existing object")
        self.names.add(name)

    def vector_type(self, name):
        _name(name)
        if name in self.types:
            raise ProgramError(f"Vector type {name!r} already exists")
        self.types.add(name)
        return name

    def _type(self, kind):
        if kind not in self.types:
            raise ProgramError(f"Unknown vector type {kind!r}")

    def coerce(self, value):
        if isinstance(value, Node):
            if value.program is not self:
                raise ProgramError("Cannot combine different programs")
            return value
        if not isinstance(value, (int, float, Fraction)):
            raise ProgramError("Use typed nodes and real numeric constants, not text or arrays")
        return self._node("const", data=ex.const(value))

    def scalar(self, value):
        node = self.coerce(value)
        if node.kind is not None:
            raise ProgramError("Expected a scalar; use mean() for a normalized contraction")
        return node

    def parameter(self, name):
        """A fixed deterministic real scalar, also available to physical AD."""
        self._reserve(name)
        return self._node("parameter", data=name)

    def broadcast(self, value, kind):
        self._type(kind)
        return self._node("broadcast", kind, (self.scalar(value),))

    def one(self, kind=None):
        return self.coerce(1) if kind is None else self.broadcast(1, kind)

    def zero(self, kind=None):
        return self.coerce(0) if kind is None else self.broadcast(0, kind)

    def roots(self, kind, names, covariance, means=None):
        """One iid Gaussian tuple per neuron; separate calls are independent.

        Covariance entries are concrete real numeric constants; PSD is checked
        in exact rational arithmetic, allowing zero pivots and singular laws.
        """
        self._type(kind)
        names = tuple(names)
        if not names or len(set(names)) != len(names):
            raise ProgramError("A root tuple needs distinct names")
        for name in names:
            _name(name)
            if name in self.names:
                raise ProgramError(f"Name {name!r} already exists")
        size = len(names)
        try:
            rows = [list(row) for row in covariance]
            if any(not isinstance(value, (int, float, Fraction))
                   for row in rows for value in row):
                raise ProgramError("Covariance entries must be real numeric constants, not text")
            cov = [[Fraction(str(v)) for v in row] for row in rows]
        except (ValueError, TypeError, ZeroDivisionError) as error:
            raise ProgramError("Covariance must contain finite real numeric constants") from error
        if len(cov) != size or any(len(row) != size for row in cov):
            raise ProgramError("Covariance shape does not match the root tuple")
        if any(cov[i][j] != cov[j][i] for i in range(size) for j in range(size)):
            raise ProgramError("Covariance must be symmetric")
        residual = [row[:] for row in cov]
        for i in range(size):
            pivot = residual[i][i]
            if pivot < 0 or (pivot == 0 and any(residual[i][j] for j in range(i + 1, size))):
                raise ProgramError("Covariance is not positive semidefinite")
            if pivot:
                for j in range(i + 1, size):
                    for k in range(i + 1, size):
                        residual[j][k] -= residual[j][i] * residual[i][k] / pivot
        means = [0] * size if means is None else list(means)
        if len(means) != size:
            raise ProgramError("Mean shape does not match the root tuple")
        mean_expr = [ex.const(v) for v in means]
        nodes = []
        for name in names:
            self._reserve(name)
            nodes.append(self._node("root", kind, data=name))
        for i, node in enumerate(nodes):
            self.root_mean[node] = mean_expr[i]
            for j, other in enumerate(nodes):
                self.root_cov[node, other] = ex.const(cov[i][j])
        return tuple(nodes)

    def root(self, name, kind, variance=1, mean=0):
        return self.roots(kind, [name], [[variance]], [mean])[0]

    def matrix(self, name, source, target):
        self._type(source)
        self._type(target)
        if source == target:
            raise ProgramError("This theorem uses matrices between distinct vector types")
        self._reserve(name)
        matrix = Matrix(self, name, source, target)
        self.matrices.append(matrix)
        return matrix

    def binary(self, op, left, right):
        left, right = self.coerce(left), self.coerce(right)
        if left.kind is not None and right.kind is not None and left.kind != right.kind:
            raise ProgramError("Coordinate operations require matching vector types")
        return self._node(op, left.kind or right.kind, (left, right))

    def phi(self, vector, order=0):
        vector = self.coerce(vector)
        if vector.kind is None:
            raise ProgramError("Apply scalar nonlinearities via broadcast, phi, then mean")
        if type(order) is not int or order < 0:
            raise ProgramError("Activation derivative order must be a nonnegative integer")
        return self._node("phi", vector.kind, (vector,), order)

    def mean(self, vector):
        vector = self.coerce(vector)
        if vector.kind is None:
            raise ProgramError("mean() expects a vector")
        return self._node("mean", None, (vector,))

    def inner(self, left, right):
        left, right = self.coerce(left), self.coerce(right)
        if left.kind is None or left.kind != right.kind:
            raise ProgramError("inner() is the normalized same-type pairing u.T v / n")
        return self.mean(left * right)

    def freeze(self, value):
        """Declare an independent seed datum, evaluated from this base-state value.

        Physical AD holds this datum fixed; Gaussian source derivatives retain
        its explicit dependence. State substitution also preserves this original
        seed expression. To take a new snapshot, substitute the unfrozen value
        first, then freeze it. Freezing part of a primal network changes the
        physical derivative being requested.
        """
        value = self.coerce(value)
        return self._node("freeze", value.kind, (value,))

    def represented(self, base):
        if not isinstance(base, Matrix) or base.program is not self:
            raise ProgramError("Expected an initialized matrix from this program")
        return RankMatrix(self, base.source, base.target, base)

    def rank_one(self, left, right, coefficient=1):
        left, right = self.coerce(left), self.coerce(right)
        if left.kind is None or right.kind is None or left.kind == right.kind:
            raise ProgramError("A rank-one matrix needs vectors in distinct declared types")
        return RankMatrix(self, right.kind, left.kind, None,
                          ((self.scalar(coefficient), left, right),))

    def frobenius(self, left, right):
        """Exact contraction of pure represented matrix directions."""
        if (not isinstance(left, RankMatrix) or not isinstance(right, RankMatrix)
            or left.program is not self or right.program is not self
            or left.base is not None or right.base is not None
            or (left.source, left.target) != (right.source, right.target)):
            raise ProgramError("Frobenius contraction requires matching pure rank-one sums")
        value = self.coerce(0)
        for c, u, v in left.terms:
            for d, a, b in right.terms:
                value = value + c * d * self.inner(u,a) * self.inner(v,b)
        self._record("normalized matrix contraction", output=value.index)
        return value

    def call(self, matrix, vector, transpose=False):
        vector = self.coerce(vector)
        if not isinstance(matrix, (Matrix, RankMatrix)) or matrix.program is not self:
            raise ProgramError("Only named or represented matrices can be called")
        source, target = ((matrix.target, matrix.source) if transpose
                          else (matrix.source, matrix.target))
        if vector.kind != source:
            raise ProgramError(f"Matrix call needs type {source!r}, got {vector.kind!r}")
        if isinstance(matrix, Matrix):
            return self._node("matmul", target, (vector,), (matrix, bool(transpose)))
        result = (self.call(matrix.base, vector, transpose) if matrix.base
                  else self.zero(target))
        for coefficient, left, right in matrix.terms:
            if transpose:
                left, right = right, left
            result = result + coefficient * left * self.inner(right, vector)
        self._record("rank-one lowering", terms=len(matrix.terms), transpose=bool(transpose),
                     output=result.index)
        return result

    def _order(self, output):
        output = self.coerce(output)
        seen, order = set(), []
        def visit(node):
            if node in seen:
                return
            seen.add(node)
            for arg in node.args:
                visit(arg)
            order.append(node)
        visit(output)
        return order

    def _directions(self, directions):
        for key, value in directions.items():
            if isinstance(key, Node):
                if key.program is not self or key.op not in ("root", "parameter"):
                    raise ProgramError("Directions must target root vectors or scalar parameters")
                if not isinstance(value, Node) or value.program is not self or value.kind != key.kind:
                    raise ProgramError("A direction must match its parameter type")
            elif isinstance(key, Matrix):
                if (key.program is not self or not isinstance(value, RankMatrix)
                    or value.program is not self or value.base is not None
                    or (key.source, key.target) != (value.source, value.target)):
                    raise ProgramError("Matrix directions must be typed pure rank-one sums")
            else:
                raise ProgramError("Unsupported differentiation parameter")

    def directional(self, output, directions):
        """One exact derivative with inserted directions and frozen seed data fixed.

        Without explicit freeze nodes this is the ordinary Frechet derivative
        of the primal expression. Frozen occurrences are independent supplied
        data for this derivative, not a differentiated diagonal substitution.
        """
        output = self.coerce(output)
        self._directions(directions)
        values = {}
        for node in self._order(output):
            args = node.args
            if node.op in ("root", "parameter"):
                value = directions.get(node, self.zero(node.kind))
            elif node.op in ("const", "freeze"):
                value = self.zero(node.kind)
            elif node.op == "broadcast":
                value = self.broadcast(values[args[0]], node.kind)
            elif node.op == "add":
                value = values[args[0]] + values[args[1]]
            elif node.op == "mul":
                value = values[args[0]] * args[1] + args[0] * values[args[1]]
            elif node.op == "phi":
                value = self.phi(args[0], node.data + 1) * values[args[0]]
            elif node.op == "mean":
                value = self.mean(values[args[0]])
            elif node.op == "matmul":
                matrix, transpose = node.data
                value = self.call(matrix, values[args[0]], transpose)
                if matrix in directions:
                    value = value + self.call(directions[matrix], args[0], transpose)
            else:
                raise ProgramError(f"No derivative rule for {node.op}")
            values[node] = value
            self._record("physical derivative: " + node.op, input=node.index, output=value.index)
        return values[output]

    def derivatives(self, output, directions, order, moving=False):
        """Return derivatives 0..order; moving=True applies the vector field repeatedly."""
        if type(order) is not int or order < 0:
            raise ProgramError("Derivative order must be a nonnegative integer")
        self._directions(directions)
        if not moving:
            frozen = {}
            for key, value in directions.items():
                if isinstance(value, RankMatrix):
                    frozen[key] = RankMatrix(self, value.source, value.target, None,
                        tuple((self.freeze(c), self.freeze(u), self.freeze(v))
                              for c, u, v in value.terms))
                else:
                    frozen[key] = self.freeze(value)
            directions = frozen
        values = [self.coerce(output)]
        for _ in range(order):
            values.append(self.directional(values[-1], directions))
        self._record("moving flow derivatives" if moving else "frozen directional derivatives", order=order)
        return tuple(values)

    def jets(self, output, directions, order, moving=False):
        return tuple(value / math.factorial(r) for r, value in
                     enumerate(self.derivatives(output, directions, order, moving)))

    def curve_jets(self, output, coefficients, order):
        """Compose with theta(t)=theta+sum_{r>=1} coefficients[r-1]*t**r.

        Coefficients are fixed along this auxiliary curve, possibly functions
        of the base state. Return factorial-normalized observable jets 0..order.
        Matrix coefficients must be pure represented directions.
        """
        if type(order) is not int or order < 0:
            raise ProgramError("Jet order must be a nonnegative integer")
        coefficients = {key: tuple(values) for key, values in coefficients.items()}
        for key, values in coefficients.items():
            for value in values:
                self._directions({key: value})
        name = f"jetTime{len(self.nodes)}"
        while name in self.names:
            name += "x"
        time = self.parameter(name)
        replacements = {}
        for parameter, values in coefficients.items():
            state = self.represented(parameter) if isinstance(parameter, Matrix) else parameter
            for r, coefficient in enumerate(values[:order], 1):
                state = state + coefficient * (time ** r)
            replacements[parameter] = state
        curve = self.at(output, replacements)
        derivatives = self.derivatives(curve, {time: self.coerce(1)}, order)
        values = tuple(self.at(value, {time: self.coerce(0)}) / math.factorial(r)
                       for r, value in enumerate(derivatives))
        self._record("finite curve jets", order=order)
        return values

    def gradient(self, output, vectors=(), matrices=(), scalars=()):
        """Vector entries are n*grad, matrix entries are grad, scalars are grad.

        Differentiate the current-parameter template before substituting states.
        Any explicitly frozen seed data are held fixed, as in directional().
        """
        output = self.scalar(output)
        vectors, matrices, scalars = tuple(vectors), tuple(matrices), tuple(scalars)
        for node in vectors:
            if not isinstance(node, Node) or node.program is not self or node.op != "root":
                raise ProgramError("Trainable vector parameters must be root leaves")
        for node in scalars:
            if not isinstance(node, Node) or node.program is not self or node.op != "parameter":
                raise ProgramError("Trainable scalars must be deterministic parameter leaves")
        for matrix in matrices:
            if not isinstance(matrix, Matrix) or matrix.program is not self:
                raise ProgramError("Trainable matrices must be named parameter leaves")
        adj = {output: self.coerce(1)}
        matrix_adj = {}
        def add(node, value):
            adj[node] = adj[node] + value if node in adj else value
        for node in reversed(self._order(output)):
            if node not in adj:
                continue
            a, args = adj[node], node.args
            if node.op in ("add", "mul"):
                for i, arg in enumerate(args):
                    contribution = a if node.op == "add" else a * args[1 - i]
                    if node.kind is not None and arg.kind is None:
                        contribution = self.mean(contribution)
                    add(arg, contribution)
            elif node.op == "phi":
                add(args[0], a * self.phi(args[0], node.data + 1))
            elif node.op == "mean":
                add(args[0], self.broadcast(a, args[0].kind))
            elif node.op == "broadcast":
                add(args[0], self.mean(a))
            elif node.op == "matmul":
                matrix, transpose = node.data
                add(args[0], self.call(matrix, a, not transpose))
                term = (self.rank_one(args[0], a) if transpose
                        else self.rank_one(a, args[0]))
                matrix_adj[matrix] = matrix_adj[matrix] + term if matrix in matrix_adj else term
            elif node.op not in ("const", "root", "parameter", "freeze"):
                raise ProgramError(f"No adjoint rule for {node.op}")
            self._record("scaled adjoint: " + node.op, input=node.index, adjoint=a.index)
        result = {node: adj.get(node, self.zero(node.kind)) for node in (*vectors, *scalars)}
        result.update({matrix: matrix_adj.get(matrix, RankMatrix(self, matrix.source, matrix.target))
                       for matrix in matrices})
        return result

    def at(self, output, replacements):
        """Substitute current states simultaneously, preserving independent seeds.

        Replacement expressions are not revisited. A freeze node keeps its
        original defining expression: substitution does not refresh seed data.
        """
        output = self.coerce(output)
        for key, value in replacements.items():
            if isinstance(key, Node):
                if (key.program is not self or key.op not in ("root", "parameter")
                    or not isinstance(value, Node) or value.program is not self or value.kind != key.kind):
                    raise ProgramError("Substitutions must match leaf parameter types")
            elif isinstance(key, Matrix):
                if (not isinstance(value, (Matrix, RankMatrix)) or value.program is not self
                    or key.program is not self
                    or (key.source, key.target) != (value.source, value.target)):
                    raise ProgramError("Matrix substitution must preserve its type")
            else:
                raise ProgramError("Unsupported substitution target")
        values = {}
        for node in self._order(output):
            if node in replacements:
                value = replacements[node]
            elif node.op in ("const", "root", "parameter", "freeze"):
                value = node
            elif node.op == "matmul":
                matrix, transpose = node.data
                value = self.call(replacements.get(matrix, matrix), values[node.args[0]], transpose)
            else:
                value = self._node(node.op, node.kind, tuple(values[a] for a in node.args), node.data)
            values[node] = value
        self._record("simultaneous state substitution", input=output.index, output=values[output].index)
        return values[output]

    def _matrix_at(self, matrix, state):
        return RankMatrix(self, matrix.source, matrix.target, None,
            tuple((self.at(c, state), self.at(u, state), self.at(v, state))
                  for c, u, v in matrix.terms))

    def gradient_descent(self, loss, vectors=(), matrices=(), steps=1, step_size=1, mobilities=None):
        """Fixed simultaneous updates; differentiate one ambient loss template first."""
        if type(steps) is not int or steps < 0:
            raise ProgramError("Update count must be a fixed nonnegative integer")
        vectors, matrices = tuple(vectors), tuple(matrices)
        gradient = self.gradient(loss, vectors, matrices)
        factors = {} if mobilities is None else dict(mobilities)
        if any(key not in gradient for key in factors):
            raise ProgramError("Mobility supplied for an untrained parameter")
        eta = self.scalar(step_size)
        factors = {parameter: self.scalar(value) for parameter, value in factors.items()}
        for coefficient in (eta, *factors.values()):
            if any(node.op not in ("const", "parameter", "add", "mul")
                   for node in self._order(coefficient)):
                raise ProgramError("This optimizer helper requires fixed deterministic scalar coefficients")
        state = {v: v for v in vectors}
        state.update({w: self.represented(w) for w in matrices})
        for _ in range(steps):
            new = dict(state)
            for parameter, grad in gradient.items():
                factor = eta * self.scalar(factors.get(parameter, 1))
                if isinstance(parameter, Matrix):
                    new[parameter] = state[parameter] + self._matrix_at(grad, state) * -factor
                else:
                    new[parameter] = state[parameter] - factor * self.at(grad, state)
            state = new
        self._record("fixed gradient updates", steps=steps)
        return state

    def compile(self, output, *, preactivations=None):
        return GaussianCompiler(self, preactivations).compile(self.scalar(output))


@dataclass(frozen=True)
class Expectation:
    symbol: ex.Expr
    integrand: ex.Expr
    coordinates: tuple[ex.Expr, ...]
    covariance: tuple[tuple[ex.Expr, ...], ...]
    kind: str


@dataclass
class GaussianDAG:
    output: ex.Expr
    expectations: tuple[Expectation, ...]
    fields: dict[str, ex.Expr]
    sources: tuple[dict, ...]
    trace: tuple[dict, ...]
    normal_form: str

    def formula(self):
        lines = ["Infinite-width Gaussian calculation (not a finite-width expectation):"]
        for node in self.expectations:
            coords = ", ".join(map(ex.render, node.coordinates))
            covariance = "; ".join(", ".join(map(ex.render, row)) for row in node.covariance)
            lines.append(f"{ex.render(node.symbol)} = E[{ex.render(node.integrand)}], "
                         f"({coords}) ~ N(0, [{covariance}])")
        lines.append("output = " + ex.render(self.output))
        return "\n".join(lines)

    def to_dict(self):
        return dict(semantics="infinite-width limit", normal_form=self.normal_form,
            output=ex.render(self.output),
            expectations=[dict(name=ex.render(e.symbol), integrand=ex.render(e.integrand),
                coordinates=list(map(ex.render, e.coordinates)),
                covariance=[list(map(ex.render, row)) for row in e.covariance], kind=e.kind)
                for e in self.expectations], fields={k: ex.render(v) for k,v in self.fields.items()},
            sources=list(self.sources), trace=list(self.trace))


class GaussianCompiler:
    def __init__(self, program, preactivations=None):
        self.program = program
        self.preactivations = None if preactivations is None else frozenset(preactivations)
        if self.preactivations is not None:
            for node in self.preactivations:
                if not isinstance(node, Node) or node.program is not program or node.kind is None:
                    raise ProgramError("Preactivation declarations must be vector nodes of this program")
        self.fields = {}
        self.covariance = {}
        self.gaussians = {kind: [] for kind in program.types}
        self.calls = {}
        self.expectations = []
        self.integrals = {}
        self.trace = list(program.trace)
        self.sources = []
        self.aliases = {}

    def _cov(self, left, right):
        return self.covariance.get((left, right), ex.const(0))

    def _set_cov(self, left, right, value):
        self.covariance[left, right] = self.covariance[right, left] = value

    def _atom(self, expression, kind):
        # Preactivation aliases are integration coordinates only. They are never
        # used for formal source derivatives or collapsed using Gaussian support.
        if self.preactivations is not None:
            expression = ex.substitute(expression, {value[0]: alias for alias, value in self.aliases.items()
                                                   if value[1] == kind})
        coordinates = tuple(g for g in self.gaussians[kind] if g in ex.symbols(expression))
        coordinates += tuple(g for g, value in self.aliases.items()
                             if value[1] == kind and g in ex.symbols(expression))
        def has_phi(expr):
            return expr.op == "phi" or any(has_phi(arg) for arg in expr.args)
        if not coordinates and not has_phi(expression):
            return expression
        key = kind, expression
        if key in self.integrals:
            return self.integrals[key]
        symbol = ex.symbol(f"I_{len(self.expectations) + 1}")
        covariance = tuple(tuple(self._integration_cov(a,b) for b in coordinates) for a in coordinates)
        self.expectations.append(Expectation(symbol, expression, coordinates, covariance, kind))
        self.integrals[key] = symbol
        self.trace.append(dict(stage="Gaussian", rule="expectation", output=ex.render(symbol),
                               integrand=ex.render(expression)))
        return symbol

    def _linear(self, expression, kind):
        coefficients = {g: ex.diff(expression, g) for g in self.gaussians[kind]}
        sources = frozenset(self.gaussians[kind])
        if any(ex.symbols(c) & sources for c in coefficients.values()):
            raise ProgramError("Declared preactivation is not a Gaussian linear expression")
        remainder = ex.expand(expression - sum((c*g for g,c in coefficients.items()), ex.const(0)))
        if remainder != ex.const(0):
            raise ProgramError("Initialization normal form requires centered Gaussian preactivations")
        return coefficients

    def _integration_cov(self, left, right):
        a = self._linear(*self.aliases[left]) if left in self.aliases else {left: ex.const(1)}
        b = self._linear(*self.aliases[right]) if right in self.aliases else {right: ex.const(1)}
        return ex.expand(sum((c*d*self._cov(g,h) for g,c in a.items() for h,d in b.items()), ex.const(0)))

    def expectation(self, expression, kind):
        coordinates = list(self.gaussians[kind])
        if self.preactivations is not None:
            expression = ex.substitute(expression, {value[0]: alias for alias, value in self.aliases.items()
                                                   if value[1] == kind})
            coordinates.extend(alias for alias,value in self.aliases.items() if value[1] == kind)
        covariance = {(a,b): self._integration_cov(a,b) for a in coordinates for b in coordinates}
        value = ex.gaussian_expectation(expression, coordinates, covariance,
                                        lambda term: self._atom(term, kind),
                                        flat_only=self.preactivations is not None)
        # A nonlinearity of deterministic scalar feedback is a zero-dimensional
        # Gaussian integral. Retaining its atom makes the final assembly polynomial.
        substitutions = {}
        def visit(expr):
            if expr.op == "phi":
                substitutions[expr] = self._atom(expr, kind)
            else:
                for arg in expr.args:
                    visit(arg)
        visit(value)
        return ex.substitute(value, substitutions)

    def compile(self, output):
        for node in self.program._order(output):
            args = [self.fields[arg] for arg in node.args]
            if node.op == "const":
                value = node.data
            elif node.op == "parameter":
                value = ex.symbol("s_" + node.data)
            elif node.op == "root":
                source = ex.symbol("r_" + node.data)
                self.gaussians[node.kind].append(source)
                for old, rep in self.fields.items():
                    if old.op == "root" and old.kind == node.kind:
                        self._set_cov(source, ex.symbol("r_" + old.data),
                                      self.program.root_cov.get((node,old), ex.const(0)))
                self._set_cov(source, source, self.program.root_cov[node,node])
                value = source + self.program.root_mean[node]
                self.sources.append(dict(name=ex.render(source), kind=node.kind, group="root tuple",
                                         program_node=node.index))
            elif node.op in ("broadcast", "freeze"):
                value = args[0]
            elif node.op == "add":
                value = args[0] + args[1]
            elif node.op == "mul":
                value = args[0] * args[1]
            elif node.op == "phi":
                if self.preactivations is not None and node.args[0] not in self.preactivations:
                    raise ProgramError("Initialization normal form: nonlinear argument is not a declared preactivation")
                value = ex.phi(args[0], node.data)
            elif node.op == "mean":
                value = self.expectation(args[0], node.args[0].kind)
            elif node.op == "matmul":
                matrix, transpose = node.data
                key = matrix, transpose
                old_calls = self.calls.setdefault(key, [])
                source = ex.symbol(f"g_{matrix.name}_{'R' if transpose else 'F'}_{len(old_calls)+1}")
                inp, input_kind = args[0], node.args[0].kind
                for old_source, old_input in old_calls:
                    self._set_cov(source, old_source, self.expectation(inp * old_input, input_kind))
                self._set_cov(source, source, self.expectation(inp * inp, input_kind))
                self.gaussians[node.kind].append(source)
                value = source
                response = []
                for reverse_source, reverse_input in self.calls.get((matrix, not transpose), []):
                    derivative = ex.diff(inp, reverse_source)
                    coefficient = self.expectation(derivative, input_kind)
                    value = value + reverse_input * coefficient
                    response.append(dict(source=ex.render(reverse_source),
                                         formal_derivative=ex.render(derivative),
                                         coefficient=ex.render(coefficient)))
                old_calls.append((source, inp))
                self.sources.append(dict(name=ex.render(source), kind=node.kind,
                    group=matrix.name + (":reverse" if transpose else ":forward"), program_node=node.index))
                self.trace.append(dict(stage="Gaussian", rule="matrix source and response",
                    input=node.index, matrix=matrix.name, transpose=transpose, source=ex.render(source),
                    variance=ex.render(self._cov(source,source)),
                    covariance_with_previous={ex.render(g): ex.render(self._cov(source,g))
                                              for g, _ in old_calls[:-1]},
                    response=response, output=ex.render(value)))
            else:
                raise ProgramError(f"No Gaussian rule for {node.op}")
            self.fields[node] = value
            if self.preactivations is not None and node in self.preactivations:
                self._linear(value, node.kind)
                if value not in self.gaussians[node.kind]:
                    self.aliases[ex.symbol(f"z_{node.index}")] = (value, node.kind)
            self.trace.append(dict(stage="Gaussian", rule=node.op, input=node.index, output=ex.render(value)))
        for source in self.sources:
            coordinate = ex.symbol(source["name"])
            source["covariances"] = {ex.render(g): ex.render(self._cov(coordinate,g))
                                     for g in self.gaussians[source["kind"]]}
        return GaussianDAG(ex.expand(self.fields[output]), tuple(self.expectations),
            {f"v_{node.index}" if node.kind else f"s_{node.index}": value for node,value in self.fields.items()},
            tuple(self.sources), tuple(self.trace),
            "initialization activation moments" if self.preactivations is not None else "general Gaussian DAG")
