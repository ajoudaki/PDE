"""Factored independent arbitrary-depth order-five compiler.

Random-coordinate polynomials are distributed, while deterministic Gaussian
moment arithmetic is retained in a hash-consed expression DAG.  This is the
same mathematical transfer as ``depth_compiler.py`` but avoids re-expanding
large order-four covariance polynomials at every later contraction.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from math import factorial
from typing import DefaultDict, Iterable, Mapping


MAX_DERIVATIVE = 9
NF = 5
NR = 5


@dataclass(frozen=True, eq=False)
class Expr:
    serial: int
    node: tuple

    def __hash__(self) -> int:
        return self.serial


class ExprFactory:
    def __init__(self, *, unit_gram: bool):
        self.unit_gram = unit_gram
        self._serial = 0
        self._constants: dict[Fraction, Expr] = {}
        self._atoms: dict[tuple[str, tuple[int, ...]], Expr] = {}
        self._adds: dict[tuple[int, ...], Expr] = {}
        self._muls: dict[tuple[int, ...], Expr] = {}
        self.zero = self.const(0)
        self.one = self.const(1)

    def _new(self, node: tuple) -> Expr:
        self._serial += 1
        return Expr(self._serial, node)

    def const(self, value: int | Fraction) -> Expr:
        value = Fraction(value)
        if value not in self._constants:
            self._constants[value] = self._new(("const", value))
        return self._constants[value]

    def atom(self, layer: int, counts: Iterable[int]) -> Expr:
        values = list(counts)
        while values and not values[-1]:
            values.pop()
        if not values:
            return self.one
        exponent = tuple(values)
        if self.unit_gram and exponent == (2,):
            return self.one
        tag = "M" if self.unit_gram else f"L{layer}"
        key = (tag, exponent)
        if key not in self._atoms:
            self._atoms[key] = self._new(("atom", tag, exponent))
        return self._atoms[key]

    def mul(self, *raw: Expr) -> Expr:
        rational = Fraction(1)
        factors: list[Expr] = []
        for expression in raw:
            if expression.node[0] == "const":
                rational *= expression.node[1]
            elif expression.node[0] == "mul":
                for child in expression.node[1]:
                    if child.node[0] == "const":
                        rational *= child.node[1]
                    else:
                        factors.append(child)
            else:
                factors.append(expression)
        if not rational:
            return self.zero
        if rational != 1:
            factors.append(self.const(rational))
        if not factors:
            return self.one
        factors.sort(key=lambda value: value.serial)
        if len(factors) == 1:
            return factors[0]
        key = tuple(value.serial for value in factors)
        if key not in self._muls:
            self._muls[key] = self._new(("mul", tuple(factors)))
        return self._muls[key]

    def _coefficient_core(self, expression: Expr) -> tuple[Fraction, Expr]:
        if expression.node[0] == "const":
            return expression.node[1], self.one
        if expression.node[0] != "mul":
            return Fraction(1), expression
        coefficient = Fraction(1)
        remaining = []
        for child in expression.node[1]:
            if child.node[0] == "const":
                coefficient *= child.node[1]
            else:
                remaining.append(child)
        return coefficient, self.mul(*remaining)

    def add(self, *raw: Expr) -> Expr:
        coefficients: dict[Expr, Fraction] = {}
        for expression in raw:
            children = expression.node[1] if expression.node[0] == "add" else (expression,)
            for child in children:
                coefficient, core = self._coefficient_core(child)
                coefficients[core] = coefficients.get(core, Fraction(0)) + coefficient
        terms = []
        for core, coefficient in coefficients.items():
            if not coefficient:
                continue
            terms.append(self.const(coefficient) if core is self.one else self.mul(self.const(coefficient), core))
        if not terms:
            return self.zero
        terms.sort(key=lambda value: value.serial)
        if len(terms) == 1:
            return terms[0]
        key = tuple(value.serial for value in terms)
        if key not in self._adds:
            self._adds[key] = self._new(("add", tuple(terms)))
        return self._adds[key]

    def scale(self, expression: Expr, scalar: int | Fraction) -> Expr:
        return self.mul(self.const(scalar), expression)

    def node_count(self) -> int:
        return self._serial


@dataclass(frozen=True, order=True)
class Skeleton:
    jets: tuple[tuple[int, ...], ...]
    readout: int
    forward: tuple[int, ...]
    reverse: tuple[int, ...]


RPoly = dict[Skeleton, Expr]


class Algebra:
    def __init__(self, hidden_layers: int, factory: ExprFactory):
        self.depth = hidden_layers
        self.matrices = hidden_layers - 1
        self.expr = factory
        self.zero_skeleton = Skeleton(
            tuple((0,) * MAX_DERIVATIVE for _ in range(hidden_layers)),
            0,
            (0,) * (self.matrices * NF),
            (0,) * (self.matrices * NR),
        )

    def const(self, value: int | Fraction) -> RPoly:
        expression = self.expr.const(value)
        return {} if expression is self.expr.zero else {self.zero_skeleton: expression}

    def scalar(self, expression: Expr) -> RPoly:
        return {} if expression is self.expr.zero else {self.zero_skeleton: expression}

    def generator(self, kind: str, first: int = 0, second: int = 0) -> RPoly:
        jets = [list(row) for row in self.zero_skeleton.jets]
        forward = list(self.zero_skeleton.forward)
        reverse = list(self.zero_skeleton.reverse)
        readout = 0
        if kind == "jet":
            jets[first][second] = 1
        elif kind == "readout":
            readout = 1
        elif kind == "forward":
            forward[first * NF + second - 1] = 1
        elif kind == "reverse":
            reverse[first * NR + second] = 1
        else:
            raise ValueError(kind)
        skeleton = Skeleton(
            tuple(tuple(row) for row in jets), readout, tuple(forward), tuple(reverse)
        )
        return {skeleton: self.expr.one}

    def add(self, *polynomials: Mapping[Skeleton, Expr]) -> RPoly:
        out: dict[Skeleton, Expr] = {}
        for polynomial in polynomials:
            for skeleton, coefficient in polynomial.items():
                out[skeleton] = self.expr.add(out.get(skeleton, self.expr.zero), coefficient)
                if out[skeleton] is self.expr.zero:
                    del out[skeleton]
        return out

    def scale(self, polynomial: Mapping[Skeleton, Expr], scalar: int | Fraction) -> RPoly:
        return {
            skeleton: value
            for skeleton, coefficient in polynomial.items()
            if (value := self.expr.scale(coefficient, scalar)) is not self.expr.zero
        }

    @staticmethod
    def _counts(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(a + b for a, b in zip(left, right))

    def mul(self, left: Mapping[Skeleton, Expr], right: Mapping[Skeleton, Expr]) -> RPoly:
        out: dict[Skeleton, Expr] = {}
        for lm, lc in left.items():
            for rm, rc in right.items():
                skeleton = Skeleton(
                    tuple(self._counts(a, b) for a, b in zip(lm.jets, rm.jets)),
                    lm.readout + rm.readout,
                    self._counts(lm.forward, rm.forward),
                    self._counts(lm.reverse, rm.reverse),
                )
                product = self.expr.mul(lc, rc)
                out[skeleton] = self.expr.add(out.get(skeleton, self.expr.zero), product)
                if out[skeleton] is self.expr.zero:
                    del out[skeleton]
        return out

    def derivative(self, polynomial: Mapping[Skeleton, Expr], kind: str, matrix: int, order: int) -> RPoly:
        out: dict[Skeleton, Expr] = {}
        for monomial, coefficient in polynomial.items():
            targets = []
            if kind == "reverse":
                position = matrix * NR + order
                count = monomial.reverse[position]
                if count:
                    reverse = list(monomial.reverse)
                    reverse[position] -= 1
                    targets.append((Skeleton(monomial.jets, monomial.readout, monomial.forward, tuple(reverse)), count))
            elif kind == "forward" and order > 0:
                position = matrix * NF + order - 1
                count = monomial.forward[position]
                if count:
                    forward = list(monomial.forward)
                    forward[position] -= 1
                    targets.append((Skeleton(monomial.jets, monomial.readout, tuple(forward), monomial.reverse), count))
            elif kind == "forward" and order == 0:
                destination = matrix + 1
                for derivative, count in enumerate(monomial.jets[destination][:-1]):
                    if count:
                        jets = [list(row) for row in monomial.jets]
                        jets[destination][derivative] -= 1
                        jets[destination][derivative + 1] += 1
                        targets.append((Skeleton(tuple(tuple(row) for row in jets), monomial.readout, monomial.forward, monomial.reverse), count))
            else:
                raise ValueError((kind, matrix, order))
            for target, multiplier in targets:
                piece = self.expr.scale(coefficient, multiplier)
                out[target] = self.expr.add(out.get(target, self.expr.zero), piece)
        return {key: value for key, value in out.items() if value is not self.expr.zero}

    def series_mul(self, left: list[RPoly], right: list[RPoly], order: int) -> list[RPoly]:
        return [
            self.add(*(self.mul(left[p], right[k - p]) for p in range(k + 1)))
            for k in range(order + 1)
        ]

    def phi_coefficient(self, layer: int, activation_derivative: int, delta: list[RPoly], order: int) -> RPoly:
        result: RPoly = {}
        powers = [self.const(1)] + [{} for _ in range(order)]
        for multiplicity in range(order + 1):
            if multiplicity:
                powers = self.series_mul(powers, delta, order)
            result = self.add(
                result,
                self.scale(
                    self.mul(self.generator("jet", layer, activation_derivative + multiplicity), powers[order]),
                    Fraction(1, factorial(multiplicity)),
                ),
            )
        return result


def _double_factorial(value: int) -> int:
    answer = 1
    for factor in range(value, 0, -2):
        answer *= factor
    return answer


class Eliminator:
    def __init__(self, algebra: Algebra):
        self.alg = algebra
        self.expr = algebra.expr
        self.H: list[dict[tuple[int, int], Expr]] = [dict() for _ in range(algebra.matrices)]
        self.B: list[dict[tuple[int, int], Expr]] = [dict() for _ in range(algebra.matrices)]
        self._r_cache = [dict() for _ in range(algebra.matrices)]
        self._f_cache = [dict() for _ in range(algebra.matrices)]
        self._kernel_cache: dict[tuple, Expr] = {}

    @staticmethod
    def entry(table: Mapping[tuple[int, int], Expr], i: int, j: int) -> Expr:
        return table[(max(i, j), min(i, j))]

    def wick_reverse(self, matrix: int, state: tuple[int, ...]) -> Expr:
        cache = self._r_cache[matrix]
        if state in cache:
            return cache[state]
        if not any(state):
            return self.expr.one
        if sum(state) % 2:
            cache[state] = self.expr.zero
            return self.expr.zero
        i = next(index for index, count in enumerate(state) if count)
        remainder = list(state)
        remainder[i] -= 1
        pieces = []
        for j, count in enumerate(remainder):
            if count:
                paired = list(remainder)
                paired[j] -= 1
                pieces.append(
                    self.expr.scale(
                        self.expr.mul(self.entry(self.B[matrix], i, j), self.wick_reverse(matrix, tuple(paired))),
                        count,
                    )
                )
        answer = self.expr.add(*pieces)
        cache[state] = answer
        return answer

    def stein_forward(self, matrix: int, state: tuple[int, ...], jets: tuple[int, ...]) -> dict[tuple[int, ...], Expr]:
        cache = self._f_cache[matrix]
        key = (state, jets)
        if key in cache:
            return cache[key]
        if not any(state):
            answer = {jets: self.expr.one}
            cache[key] = answer
            return answer
        i0 = next(index for index, count in enumerate(state) if count)
        i = i0 + 1
        remainder = list(state)
        remainder[i0] -= 1
        accumulated: dict[tuple[int, ...], Expr] = {}
        for j0, count in enumerate(remainder):
            if count:
                paired = list(remainder)
                paired[j0] -= 1
                covariance = self.entry(self.H[matrix], i, j0 + 1)
                for output, sub in self.stein_forward(matrix, tuple(paired), jets).items():
                    piece = self.expr.scale(self.expr.mul(covariance, sub), count)
                    accumulated[output] = self.expr.add(accumulated.get(output, self.expr.zero), piece)
        covariance0 = self.entry(self.H[matrix], i, 0)
        for derivative, count in enumerate(jets[:-1]):
            if count:
                raised = list(jets)
                raised[derivative] -= 1
                raised[derivative + 1] += 1
                for output, sub in self.stein_forward(matrix, tuple(remainder), tuple(raised)).items():
                    piece = self.expr.scale(self.expr.mul(covariance0, sub), count)
                    accumulated[output] = self.expr.add(accumulated.get(output, self.expr.zero), piece)
        answer = {key: value for key, value in accumulated.items() if value is not self.expr.zero}
        cache[key] = answer
        return answer

    def kernel(self, monomial: Skeleton) -> Expr:
        key = (monomial.jets, monomial.readout, monomial.forward, monomial.reverse)
        if key in self._kernel_cache:
            return self._kernel_cache[key]
        if monomial.readout % 2:
            self._kernel_cache[key] = self.expr.zero
            return self.expr.zero
        branches: dict[tuple[tuple[int, ...], ...], Expr] = {
            monomial.jets: self.expr.const(_double_factorial(monomial.readout - 1) if monomial.readout else 1)
        }
        for matrix in range(self.alg.matrices):
            state = monomial.reverse[matrix * NR : (matrix + 1) * NR]
            wick = self.wick_reverse(matrix, state)
            if wick is self.expr.zero:
                self._kernel_cache[key] = self.expr.zero
                return self.expr.zero
            branches = {jets: self.expr.mul(value, wick) for jets, value in branches.items()}
        for matrix in range(self.alg.matrices):
            state = monomial.forward[matrix * NF : (matrix + 1) * NF]
            destination = matrix + 1
            updated: dict[tuple[tuple[int, ...], ...], Expr] = {}
            for jets_by_layer, coefficient in branches.items():
                for output, factor in self.stein_forward(matrix, state, jets_by_layer[destination]).items():
                    jets = list(jets_by_layer)
                    jets[destination] = output
                    key_jets = tuple(jets)
                    piece = self.expr.mul(coefficient, factor)
                    updated[key_jets] = self.expr.add(updated.get(key_jets, self.expr.zero), piece)
            branches = updated
        pieces = []
        for jets_by_layer, coefficient in branches.items():
            atoms = [self.expr.atom(layer, counts) for layer, counts in enumerate(jets_by_layer, start=1)]
            pieces.append(self.expr.mul(coefficient, *atoms))
        answer = self.expr.add(*pieces)
        self._kernel_cache[key] = answer
        return answer

    def expectation(self, polynomial: Mapping[Skeleton, Expr]) -> Expr:
        return self.expr.add(
            *(self.expr.mul(coefficient, self.kernel(monomial)) for monomial, coefficient in polynomial.items())
        )


@dataclass
class FactoredDepthResult:
    hidden_layers: int
    q0: Fraction
    unit_gram: bool
    factory: ExprFactory
    A: Expr
    B: Expr
    C: Expr
    f_coefficients: tuple[Expr, ...]
    diagnostics: dict[str, object]


def compile_depth_factored(
    hidden_layers: int,
    *,
    q0: int | Fraction = 1,
    unit_gram: bool = False,
    progress: bool = False,
) -> FactoredDepthResult:
    if hidden_layers < 2:
        raise ValueError("at least two hidden layers are required")
    q0 = Fraction(q0)
    factory = ExprFactory(unit_gram=unit_gram)
    alg = Algebra(hidden_layers, factory)
    eliminate = Eliminator(alg)
    depth = hidden_layers
    matrices = depth - 1

    z_delta: list[list[RPoly]] = [[{}] for _ in range(depth)]
    h: list[list[RPoly]] = [[alg.generator("jet", layer, 0)] for layer in range(depth)]
    hp: list[list[RPoly]] = [[alg.generator("jet", layer, 1)] for layer in range(depth)]
    a: list[RPoly] = [alg.generator("readout")]
    b: list[list[RPoly]] = [[] for _ in range(depth)]
    reverse_actions: list[list[RPoly]] = [[] for _ in range(matrices)]

    for matrix in range(matrices):
        eliminate.H[matrix][(0, 0)] = eliminate.expectation(alg.mul(h[matrix][0], h[matrix][0]))
    b[-1].append(alg.mul(a[0], hp[-1][0]))
    for destination in range(depth - 1, 0, -1):
        matrix = destination - 1
        eliminate.B[matrix][(0, 0)] = eliminate.expectation(alg.mul(b[destination][0], b[destination][0]))
        beta = eliminate.expectation(alg.derivative(b[destination][0], "forward", matrix, 0))
        action = alg.add(
            alg.generator("reverse", matrix, 0),
            alg.mul(h[destination - 1][0], alg.scalar(beta)),
        )
        reverse_actions[matrix].append(action)
        b[destination - 1].append(alg.mul(hp[destination - 1][0], action))
    z_delta[0].append(alg.scale(b[0][0], q0))
    diagnostics: dict[str, object] = {}

    for order in range(1, 5):
        h[0].append(alg.phi_coefficient(0, 0, z_delta[0], order))
        hp[0].append(alg.phi_coefficient(0, 1, z_delta[0], order))
        for matrix in range(matrices):
            source, destination = matrix, matrix + 1
            for ell in range(order + 1):
                eliminate.H[matrix][(order, ell)] = eliminate.expectation(
                    alg.mul(h[source][order], h[source][ell])
                )
            responses = []
            for s in range(order):
                alpha = eliminate.expectation(
                    alg.derivative(h[source][order], "reverse", matrix, s)
                )
                responses.append(alg.mul(b[destination][s], alg.scalar(alpha)))
            low_rank = []
            for update in range(1, order + 1):
                for p in range(update):
                    q = update - 1 - p
                    covariance = eliminate.entry(eliminate.H[matrix], q, order - update)
                    low_rank.append(
                        alg.scale(
                            alg.mul(b[destination][p], alg.scalar(covariance)),
                            Fraction(1, update),
                        )
                    )
            z = alg.add(alg.generator("forward", matrix, order), *responses, *low_rank)
            z_delta[destination].append(z)
            h[destination].append(alg.phi_coefficient(destination, 0, z_delta[destination], order))
            hp[destination].append(alg.phi_coefficient(destination, 1, z_delta[destination], order))

        a.append(alg.scale(h[-1][order - 1], Fraction(1, order)))
        b[-1].append(
            alg.add(*(alg.mul(a[p], hp[-1][order - p]) for p in range(order + 1)))
        )
        for destination in range(depth - 1, 0, -1):
            matrix, source = destination - 1, destination - 1
            for ell in range(order + 1):
                eliminate.B[matrix][(order, ell)] = eliminate.expectation(
                    alg.mul(b[destination][order], b[destination][ell])
                )
            responses = []
            for s in range(order + 1):
                beta = eliminate.expectation(
                    alg.derivative(b[destination][order], "forward", matrix, s)
                )
                responses.append(alg.mul(h[source][s], alg.scalar(beta)))
            low_rank = []
            for update in range(1, order + 1):
                for p in range(update):
                    q = update - 1 - p
                    covariance = eliminate.entry(eliminate.B[matrix], p, order - update)
                    low_rank.append(
                        alg.scale(
                            alg.mul(h[source][q], alg.scalar(covariance)),
                            Fraction(1, update),
                        )
                    )
            action = alg.add(alg.generator("reverse", matrix, order), *responses, *low_rank)
            reverse_actions[matrix].append(action)
            b[source].append(
                alg.add(
                    *(
                        alg.mul(hp[source][p], reverse_actions[matrix][order - p])
                        for p in range(order + 1)
                    )
                )
            )
        z_delta[0].append(alg.scale(b[0][order], Fraction(q0, order + 1)))
        diagnostics[f"order_{order}"] = {
            "h_random_terms": [len(h[layer][order]) for layer in range(depth)],
            "b_random_terms": [len(b[layer][order]) for layer in range(depth)],
            "dag_nodes": factory.node_count(),
        }
        if progress:
            print(f"factored H={depth} order={order}: {diagnostics[f'order_{order}']}", flush=True)

    order = 5
    h[0].append(alg.phi_coefficient(0, 0, z_delta[0], order))
    hp[0].append(alg.phi_coefficient(0, 1, z_delta[0], order))
    for matrix in range(matrices):
        source, destination = matrix, matrix + 1
        eliminate.H[matrix][(order, 0)] = eliminate.expectation(
            alg.mul(h[source][order], h[source][0])
        )
        responses = []
        for s in range(order):
            alpha = eliminate.expectation(
                alg.derivative(h[source][order], "reverse", matrix, s)
            )
            responses.append(alg.mul(b[destination][s], alg.scalar(alpha)))
        low_rank = []
        for update in range(1, order + 1):
            for p in range(update):
                q = update - 1 - p
                covariance = eliminate.entry(eliminate.H[matrix], q, order - update)
                low_rank.append(
                    alg.scale(
                        alg.mul(b[destination][p], alg.scalar(covariance)),
                        Fraction(1, update),
                    )
                )
        z = alg.add(alg.generator("forward", matrix, order), *responses, *low_rank)
        z_delta[destination].append(z)
        h[destination].append(alg.phi_coefficient(destination, 0, z_delta[destination], order))
        hp[destination].append(alg.phi_coefficient(destination, 1, z_delta[destination], order))

    a.append(alg.scale(h[-1][4], Fraction(1, 5)))
    f_coefficients = []
    for order in range(6):
        f_coefficients.append(
            eliminate.expectation(
                alg.add(*(alg.mul(a[p], h[-1][order - p]) for p in range(order + 1)))
            )
        )
    return FactoredDepthResult(
        hidden_layers=depth,
        q0=q0,
        unit_gram=unit_gram,
        factory=factory,
        A=f_coefficients[1],
        B=factory.scale(f_coefficients[3], factorial(3)),
        C=factory.scale(f_coefficients[5], factorial(5)),
        f_coefficients=tuple(f_coefficients),
        diagnostics=diagnostics,
    )


def reachable(roots: Iterable[Expr]) -> tuple[Expr, ...]:
    seen: set[Expr] = set()
    ordered: list[Expr] = []

    def visit(expression: Expr) -> None:
        if expression in seen:
            return
        seen.add(expression)
        if expression.node[0] in {"add", "mul"}:
            for child in expression.node[1]:
                visit(child)
        ordered.append(expression)

    for root in roots:
        visit(root)
    return tuple(ordered)


def serialize_result(result: FactoredDepthResult) -> dict[str, object]:
    roots = {"A": result.A, "B": result.B, "C": result.C}
    nodes = reachable(roots.values())
    names = {node: index for index, node in enumerate(nodes)}
    records = []
    for node in nodes:
        kind = node.node[0]
        if kind == "const":
            record = {"kind": "const", "value": str(node.node[1])}
        elif kind == "atom":
            tag, exponent = node.node[1], node.node[2]
            record = {
                "kind": "atom",
                "name": f"{tag}_" + "".join(str(value) for value in exponent + (0,) * (max(6, len(exponent)) - len(exponent))),
            }
        else:
            record = {"kind": kind, "children": [names[child] for child in node.node[1]]}
        records.append(record)
    return {
        "format": "independent-depth-order5-factored-GNF-v1",
        "hidden_layers": result.hidden_layers,
        "Q0": str(result.q0),
        "unit_gram": result.unit_gram,
        "nodes": records,
        "roots": {name: names[root] for name, root in roots.items()},
        "parity_zero": [result.f_coefficients[index] is result.factory.zero for index in (0, 2, 4)],
        "diagnostics": result.diagnostics,
    }


def emit_text(result: FactoredDepthResult) -> str:
    roots = {"A": result.A, "B": result.B, "C": result.C}
    nodes = reachable(roots.values())
    compound = [node for node in nodes if node.node[0] in {"add", "mul"}]
    names = {node: f"t_{index:06d}" for index, node in enumerate(compound)}

    def render(node: Expr) -> str:
        kind = node.node[0]
        if kind == "const":
            return str(node.node[1])
        if kind == "atom":
            tag, exponent = node.node[1], node.node[2]
            return f"{tag}_{{{''.join(str(value) for value in exponent + (0,) * (max(6, len(exponent)) - len(exponent)))}}}"
        return names[node]

    lines = [
        "# Generated independent factored Gaussian normal form.",
        f"# H={result.hidden_layers}, Q0={result.q0}, unit_gram={result.unit_gram}",
        "# Every node is deterministic arithmetic or a one-dimensional activation moment.",
    ]
    for node in compound:
        operator = " + " if node.node[0] == "add" else " * "
        lines.append(f"{names[node]} = {operator.join(render(child) for child in node.node[1])}")
    for name, root in roots.items():
        lines.append(f"{name} = {render(root)}")
    return "\n".join(lines) + "\n"


def expand_expression(root: Expr) -> dict[tuple[str, ...], Fraction]:
    """Independent distributive canonicalizer, intended for bounded audits."""

    cache: dict[Expr, dict[tuple[str, ...], Fraction]] = {}

    def visit(node: Expr) -> dict[tuple[str, ...], Fraction]:
        if node in cache:
            return cache[node]
        kind = node.node[0]
        if kind == "const":
            answer = {(): node.node[1]} if node.node[1] else {}
        elif kind == "atom":
            tag, exponent = node.node[1], node.node[2]
            name = f"{tag}_" + "".join(str(value) for value in exponent + (0,) * (max(6, len(exponent)) - len(exponent)))
            answer = {(name,): Fraction(1)}
        elif kind == "add":
            answer: dict[tuple[str, ...], Fraction] = {}
            for child in node.node[1]:
                for monomial, coefficient in visit(child).items():
                    answer[monomial] = answer.get(monomial, Fraction(0)) + coefficient
            answer = {key: value for key, value in answer.items() if value}
        else:
            answer = {(): Fraction(1)}
            for child in node.node[1]:
                product: dict[tuple[str, ...], Fraction] = {}
                for left, lc in answer.items():
                    for right, rc in visit(child).items():
                        monomial = tuple(sorted(left + right))
                        product[monomial] = product.get(monomial, Fraction(0)) + lc * rc
                answer = {key: value for key, value in product.items() if value}
        cache[node] = answer
        return answer

    return visit(root)

