"""Independent B=1, arbitrary-fixed-depth order-five GNF compiler.

The implementation starts from the exact feature-ascent flow and maintains a
separate chronological forward/reverse response registry for every hidden
matrix.  All auxiliary Gaussians are removed by inverse-free Wick--Stein
recursions.  Terminal maps contain only layer-tagged one-dimensional
activation moments, or their unit-Gram quotient.
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

Atom = tuple[int, ...]  # (-layer, nu_0,nu_1,...); untagged atoms omit layer
MomentMonomial = tuple[Atom, ...]
MPoly = dict[MomentMonomial, Fraction]


def _activation_atom(counts: Iterable[int], layer: int) -> Atom:
    values = list(counts)
    while values and not values[-1]:
        values.pop()
    return () if not values else (-layer, *values)


def _unit_atom(atom: Atom) -> Atom:
    if not atom:
        return ()
    counts = tuple(atom[1:]) if atom[0] < 0 else atom
    return () if counts == (2,) else counts


def collapse_unit(polynomial: Mapping[MomentMonomial, Fraction]) -> MPoly:
    out: DefaultDict[MomentMonomial, Fraction] = defaultdict(Fraction)
    for monomial, coefficient in polynomial.items():
        atoms = tuple(sorted(value for atom in monomial if (value := _unit_atom(atom))))
        out[atoms] += coefficient
    return {key: value for key, value in out.items() if value}


def mp_const(value: int | Fraction) -> MPoly:
    value = Fraction(value)
    return {} if not value else {(): value}


def mp_add(*polynomials: Mapping[MomentMonomial, Fraction]) -> MPoly:
    out: DefaultDict[MomentMonomial, Fraction] = defaultdict(Fraction)
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            out[monomial] += coefficient
    return {key: value for key, value in out.items() if value}


def mp_scale(polynomial: Mapping[MomentMonomial, Fraction], scalar: int | Fraction) -> MPoly:
    scalar = Fraction(scalar)
    return {key: scalar * value for key, value in polynomial.items() if scalar * value}


def mp_mul(left: Mapping[MomentMonomial, Fraction], right: Mapping[MomentMonomial, Fraction]) -> MPoly:
    if not left or not right:
        return {}
    out: DefaultDict[MomentMonomial, Fraction] = defaultdict(Fraction)
    for lm, lc in left.items():
        for rm, rc in right.items():
            out[tuple(sorted(lm + rm))] += lc * rc
    return {key: value for key, value in out.items() if value}


@dataclass(frozen=True, order=True)
class RandomMonomial:
    jets: tuple[tuple[int, ...], ...]
    readout: int
    forward: tuple[int, ...]
    reverse: tuple[int, ...]
    moments: MomentMonomial = ()


RPoly = dict[RandomMonomial, Fraction]


class RandomAlgebra:
    def __init__(self, hidden_layers: int):
        self.depth = hidden_layers
        self.matrices = hidden_layers - 1
        self.zero = RandomMonomial(
            tuple((0,) * MAX_DERIVATIVE for _ in range(hidden_layers)),
            0,
            (0,) * (self.matrices * NF),
            (0,) * (self.matrices * NR),
            (),
        )

    def const(self, value: int | Fraction) -> RPoly:
        value = Fraction(value)
        return {} if not value else {self.zero: value}

    def generator(self, kind: str, first: int = 0, second: int = 0) -> RPoly:
        jets = [list(row) for row in self.zero.jets]
        forward = list(self.zero.forward)
        reverse = list(self.zero.reverse)
        readout = 0
        if kind == "jet":
            jets[first][second] = 1
        elif kind == "readout":
            readout = 1
        elif kind == "forward":
            # first is matrix registry index; second is Taylor-call order 1..5.
            forward[first * NF + second - 1] = 1
        elif kind == "reverse":
            reverse[first * NR + second] = 1
        else:
            raise ValueError(kind)
        monomial = RandomMonomial(
            tuple(tuple(row) for row in jets),
            readout,
            tuple(forward),
            tuple(reverse),
            (),
        )
        return {monomial: Fraction(1)}

    def from_mp(self, polynomial: Mapping[MomentMonomial, Fraction]) -> RPoly:
        return {
            RandomMonomial(
                self.zero.jets,
                0,
                self.zero.forward,
                self.zero.reverse,
                monomial,
            ): coefficient
            for monomial, coefficient in polynomial.items()
            if coefficient
        }

    @staticmethod
    def add(*polynomials: Mapping[RandomMonomial, Fraction]) -> RPoly:
        out: DefaultDict[RandomMonomial, Fraction] = defaultdict(Fraction)
        for polynomial in polynomials:
            for monomial, coefficient in polynomial.items():
                out[monomial] += coefficient
        return {key: value for key, value in out.items() if value}

    @staticmethod
    def scale(polynomial: Mapping[RandomMonomial, Fraction], scalar: int | Fraction) -> RPoly:
        scalar = Fraction(scalar)
        return {key: scalar * value for key, value in polynomial.items() if scalar * value}

    @staticmethod
    def _counts(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(a + b for a, b in zip(left, right))

    def mul(self, left: Mapping[RandomMonomial, Fraction], right: Mapping[RandomMonomial, Fraction]) -> RPoly:
        if not left or not right:
            return {}
        out: DefaultDict[RandomMonomial, Fraction] = defaultdict(Fraction)
        for lm, lc in left.items():
            for rm, rc in right.items():
                monomial = RandomMonomial(
                    tuple(self._counts(a, b) for a, b in zip(lm.jets, rm.jets)),
                    lm.readout + rm.readout,
                    self._counts(lm.forward, rm.forward),
                    self._counts(lm.reverse, rm.reverse),
                    tuple(sorted(lm.moments + rm.moments)),
                )
                out[monomial] += lc * rc
        return {key: value for key, value in out.items() if value}

    def derivative(self, polynomial: Mapping[RandomMonomial, Fraction], kind: str, matrix: int, order: int) -> RPoly:
        out: DefaultDict[RandomMonomial, Fraction] = defaultdict(Fraction)
        for monomial, coefficient in polynomial.items():
            if kind == "reverse":
                position = matrix * NR + order
                count = monomial.reverse[position]
                if not count:
                    continue
                reverse = list(monomial.reverse)
                reverse[position] -= 1
                target = RandomMonomial(monomial.jets, monomial.readout, monomial.forward, tuple(reverse), monomial.moments)
                out[target] += coefficient * count
            elif kind == "forward" and order > 0:
                position = matrix * NF + order - 1
                count = monomial.forward[position]
                if not count:
                    continue
                forward = list(monomial.forward)
                forward[position] -= 1
                target = RandomMonomial(monomial.jets, monomial.readout, tuple(forward), monomial.reverse, monomial.moments)
                out[target] += coefficient * count
            elif kind == "forward" and order == 0:
                destination = matrix + 1
                counts = monomial.jets[destination]
                for derivative, count in enumerate(counts[:-1]):
                    if not count:
                        continue
                    jets = [list(row) for row in monomial.jets]
                    jets[destination][derivative] -= 1
                    jets[destination][derivative + 1] += 1
                    target = RandomMonomial(tuple(tuple(row) for row in jets), monomial.readout, monomial.forward, monomial.reverse, monomial.moments)
                    out[target] += coefficient * count
            else:
                raise ValueError((kind, matrix, order))
        return {key: value for key, value in out.items() if value}

    def series_mul(self, left: list[RPoly], right: list[RPoly], order: int) -> list[RPoly]:
        return [
            self.add(*(self.mul(left[p], right[k - p]) for p in range(k + 1)))
            for k in range(order + 1)
        ]

    def phi_coefficient(self, layer: int, activation_derivative: int, delta: list[RPoly], order: int) -> RPoly:
        if not delta or delta[0]:
            raise ValueError("activation delta must have zero constant coefficient")
        result: RPoly = {}
        powers = [self.const(1)] + [{} for _ in range(order)]
        for multiplicity in range(order + 1):
            if multiplicity:
                powers = self.series_mul(powers, delta, order)
            derivative = activation_derivative + multiplicity
            if derivative >= MAX_DERIVATIVE:
                raise ValueError("increase MAX_DERIVATIVE")
            result = self.add(
                result,
                self.scale(
                    self.mul(self.generator("jet", layer, derivative), powers[order]),
                    Fraction(1, factorial(multiplicity)),
                ),
            )
        return result


def _double_factorial_odd(value: int) -> int:
    answer = 1
    for factor in range(value, 0, -2):
        answer *= factor
    return answer


class Eliminator:
    def __init__(self, algebra: RandomAlgebra, *, unit_gram: bool):
        self.alg = algebra
        self.unit_gram = unit_gram
        self.H = [dict() for _ in range(algebra.matrices)]
        self.B = [dict() for _ in range(algebra.matrices)]
        self._r_cache = [dict() for _ in range(algebra.matrices)]
        self._f_cache = [dict() for _ in range(algebra.matrices)]
        self._kernel_cache: dict[tuple, MPoly] = {}

    @staticmethod
    def _entry(table: Mapping[tuple[int, int], MPoly], i: int, j: int) -> MPoly:
        return table[(max(i, j), min(i, j))]

    def _wick_reverse(self, matrix: int, state: tuple[int, ...]) -> MPoly:
        cache = self._r_cache[matrix]
        if state in cache:
            return cache[state]
        if not any(state):
            return {(): Fraction(1)}
        if sum(state) % 2:
            cache[state] = {}
            return {}
        i = next(index for index, count in enumerate(state) if count)
        remainder = list(state)
        remainder[i] -= 1
        answer: MPoly = {}
        for j, count in enumerate(remainder):
            if not count:
                continue
            paired = list(remainder)
            paired[j] -= 1
            piece = mp_mul(self._entry(self.B[matrix], i, j), self._wick_reverse(matrix, tuple(paired)))
            answer = mp_add(answer, mp_scale(piece, count))
        cache[state] = answer
        return answer

    def _stein_forward(self, matrix: int, state: tuple[int, ...], jets: tuple[int, ...]) -> dict[tuple[int, ...], MPoly]:
        cache = self._f_cache[matrix]
        key = (state, jets)
        if key in cache:
            return cache[key]
        if not any(state):
            answer = {jets: {(): Fraction(1)}}
            cache[key] = answer
            return answer
        i0 = next(index for index, count in enumerate(state) if count)
        i = i0 + 1
        remainder = list(state)
        remainder[i0] -= 1
        accumulated: dict[tuple[int, ...], MPoly] = {}
        for j0, count in enumerate(remainder):
            if not count:
                continue
            paired = list(remainder)
            paired[j0] -= 1
            covariance = self._entry(self.H[matrix], i, j0 + 1)
            for output_jets, sub in self._stein_forward(matrix, tuple(paired), jets).items():
                piece = mp_scale(mp_mul(covariance, sub), count)
                accumulated[output_jets] = mp_add(accumulated.get(output_jets, {}), piece)
        covariance0 = self._entry(self.H[matrix], i, 0)
        for derivative, count in enumerate(jets[:-1]):
            if not count:
                continue
            raised = list(jets)
            raised[derivative] -= 1
            raised[derivative + 1] += 1
            for output_jets, sub in self._stein_forward(matrix, tuple(remainder), tuple(raised)).items():
                piece = mp_scale(mp_mul(covariance0, sub), count)
                accumulated[output_jets] = mp_add(accumulated.get(output_jets, {}), piece)
        answer = {key: value for key, value in accumulated.items() if value}
        cache[key] = answer
        return answer

    def _kernel(self, monomial: RandomMonomial) -> MPoly:
        key = (monomial.jets, monomial.readout, monomial.forward, monomial.reverse)
        if key in self._kernel_cache:
            return self._kernel_cache[key]
        if monomial.readout % 2:
            self._kernel_cache[key] = {}
            return {}
        readout_moment = _double_factorial_odd(monomial.readout - 1) if monomial.readout else 1
        branches: dict[tuple[tuple[int, ...], ...], MPoly] = {
            monomial.jets: {(): Fraction(readout_moment)}
        }
        for matrix in range(self.alg.matrices):
            rstate = monomial.reverse[matrix * NR : (matrix + 1) * NR]
            wick = self._wick_reverse(matrix, rstate)
            if not wick:
                self._kernel_cache[key] = {}
                return {}
            branches = {jets: mp_mul(value, wick) for jets, value in branches.items()}
        for matrix in range(self.alg.matrices):
            fstate = monomial.forward[matrix * NF : (matrix + 1) * NF]
            destination = matrix + 1
            updated: dict[tuple[tuple[int, ...], ...], MPoly] = {}
            for jets_by_layer, coefficient in branches.items():
                reductions = self._stein_forward(matrix, fstate, jets_by_layer[destination])
                for destination_jets, gaussian_factor in reductions.items():
                    jets = list(jets_by_layer)
                    jets[destination] = destination_jets
                    jets_tuple = tuple(jets)
                    piece = mp_mul(coefficient, gaussian_factor)
                    updated[jets_tuple] = mp_add(updated.get(jets_tuple, {}), piece)
            branches = updated
        answer: MPoly = {}
        for jets_by_layer, coefficient in branches.items():
            atoms = tuple(
                atom
                for layer, counts in enumerate(jets_by_layer, start=1)
                if (atom := _activation_atom(counts, layer))
            )
            for moment_monomial, value in coefficient.items():
                full = tuple(sorted(moment_monomial + atoms))
                answer[full] = answer.get(full, Fraction(0)) + value
        answer = {key: value for key, value in answer.items() if value}
        if self.unit_gram:
            answer = collapse_unit(answer)
        self._kernel_cache[key] = answer
        return answer

    def expectation(self, polynomial: Mapping[RandomMonomial, Fraction]) -> MPoly:
        answer: MPoly = {}
        for monomial, coefficient in polynomial.items():
            kernel = self._kernel(monomial)
            if not kernel:
                continue
            for gaussian_moments, gaussian_coefficient in kernel.items():
                full = tuple(sorted(gaussian_moments + monomial.moments))
                answer[full] = answer.get(full, Fraction(0)) + coefficient * gaussian_coefficient
                if not answer[full]:
                    del answer[full]
        return collapse_unit(answer) if self.unit_gram else answer


@dataclass
class DepthResult:
    hidden_layers: int
    q0: Fraction
    unit_gram: bool
    A: MPoly
    B: MPoly
    C: MPoly
    f_coefficients: list[MPoly]
    diagnostics: dict[str, object]


def compile_depth(
    hidden_layers: int,
    *,
    q0: int | Fraction = 1,
    unit_gram: bool = False,
    progress: bool = False,
) -> DepthResult:
    if hidden_layers < 2:
        raise ValueError("this matrix-response compiler requires at least two hidden layers")
    q0 = Fraction(q0)
    alg = RandomAlgebra(hidden_layers)
    eliminate = Eliminator(alg, unit_gram=unit_gram)
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

    b[depth - 1].append(alg.mul(a[0], hp[depth - 1][0]))
    for destination in range(depth - 1, 0, -1):
        matrix = destination - 1
        eliminate.B[matrix][(0, 0)] = eliminate.expectation(
            alg.mul(b[destination][0], b[destination][0])
        )
        beta00 = eliminate.expectation(
            alg.derivative(b[destination][0], "forward", matrix, 0)
        )
        action = alg.add(
            alg.generator("reverse", matrix, 0),
            alg.mul(h[destination - 1][0], alg.from_mp(beta00)),
        )
        reverse_actions[matrix].append(action)
        b[destination - 1].append(alg.mul(hp[destination - 1][0], action))

    z_delta[0].append(alg.scale(b[0][0], q0))
    diagnostics: dict[str, object] = {}

    for order in range(1, 5):
        h[0].append(alg.phi_coefficient(0, 0, z_delta[0], order))
        hp[0].append(alg.phi_coefficient(0, 1, z_delta[0], order))

        for matrix in range(matrices):
            source = matrix
            destination = matrix + 1
            for ell in range(order + 1):
                eliminate.H[matrix][(order, ell)] = eliminate.expectation(
                    alg.mul(h[source][order], h[source][ell])
                )
            responses = []
            for s in range(order):
                alpha = eliminate.expectation(
                    alg.derivative(h[source][order], "reverse", matrix, s)
                )
                responses.append(alg.mul(b[destination][s], alg.from_mp(alpha)))
            low_rank = []
            for update_order in range(1, order + 1):
                for p in range(update_order):
                    q = update_order - 1 - p
                    covariance = eliminate._entry(
                        eliminate.H[matrix], q, order - update_order
                    )
                    low_rank.append(
                        alg.scale(
                            alg.mul(b[destination][p], alg.from_mp(covariance)),
                            Fraction(1, update_order),
                        )
                    )
            zk = alg.add(
                alg.generator("forward", matrix, order), *responses, *low_rank
            )
            z_delta[destination].append(zk)
            h[destination].append(
                alg.phi_coefficient(destination, 0, z_delta[destination], order)
            )
            hp[destination].append(
                alg.phi_coefficient(destination, 1, z_delta[destination], order)
            )

        a.append(alg.scale(h[depth - 1][order - 1], Fraction(1, order)))
        b[depth - 1].append(
            alg.add(
                *(alg.mul(a[p], hp[depth - 1][order - p]) for p in range(order + 1))
            )
        )

        for destination in range(depth - 1, 0, -1):
            matrix = destination - 1
            source = destination - 1
            for ell in range(order + 1):
                eliminate.B[matrix][(order, ell)] = eliminate.expectation(
                    alg.mul(b[destination][order], b[destination][ell])
                )
            responses = []
            for s in range(order + 1):
                beta = eliminate.expectation(
                    alg.derivative(b[destination][order], "forward", matrix, s)
                )
                responses.append(alg.mul(h[source][s], alg.from_mp(beta)))
            low_rank = []
            for update_order in range(1, order + 1):
                for p in range(update_order):
                    q = update_order - 1 - p
                    covariance = eliminate._entry(
                        eliminate.B[matrix], p, order - update_order
                    )
                    low_rank.append(
                        alg.scale(
                            alg.mul(h[source][q], alg.from_mp(covariance)),
                            Fraction(1, update_order),
                        )
                    )
            action = alg.add(
                alg.generator("reverse", matrix, order), *responses, *low_rank
            )
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
            "h_terms": [len(h[layer][order]) for layer in range(depth)],
            "b_terms": [len(b[layer][order]) for layer in range(depth)],
            "forward_covariance_terms": [
                sum(len(value) for key, value in eliminate.H[matrix].items() if key[0] <= order)
                for matrix in range(matrices)
            ],
            "reverse_covariance_terms": [
                sum(len(value) for key, value in eliminate.B[matrix].items() if key[0] <= order)
                for matrix in range(matrices)
            ],
        }
        if progress:
            print(f"H={depth} order={order}: {diagnostics[f'order_{order}']}", flush=True)

    # Terminal forward sweep at order five.  Fresh order-five innovations are
    # linear in f_5, so only covariance with call zero is required.
    order = 5
    h[0].append(alg.phi_coefficient(0, 0, z_delta[0], order))
    hp[0].append(alg.phi_coefficient(0, 1, z_delta[0], order))
    for matrix in range(matrices):
        source = matrix
        destination = matrix + 1
        eliminate.H[matrix][(order, 0)] = eliminate.expectation(
            alg.mul(h[source][order], h[source][0])
        )
        responses = []
        for s in range(order):
            alpha = eliminate.expectation(
                alg.derivative(h[source][order], "reverse", matrix, s)
            )
            responses.append(alg.mul(b[destination][s], alg.from_mp(alpha)))
        low_rank = []
        for update_order in range(1, order + 1):
            for p in range(update_order):
                q = update_order - 1 - p
                covariance = eliminate._entry(
                    eliminate.H[matrix], q, order - update_order
                )
                low_rank.append(
                    alg.scale(
                        alg.mul(b[destination][p], alg.from_mp(covariance)),
                        Fraction(1, update_order),
                    )
                )
        zk = alg.add(alg.generator("forward", matrix, order), *responses, *low_rank)
        z_delta[destination].append(zk)
        h[destination].append(
            alg.phi_coefficient(destination, 0, z_delta[destination], order)
        )
        hp[destination].append(
            alg.phi_coefficient(destination, 1, z_delta[destination], order)
        )

    a.append(alg.scale(h[depth - 1][4], Fraction(1, 5)))
    f_coefficients = []
    for order in range(6):
        coefficient = eliminate.expectation(
            alg.add(
                *(alg.mul(a[p], h[depth - 1][order - p]) for p in range(order + 1))
            )
        )
        f_coefficients.append(coefficient)

    return DepthResult(
        hidden_layers=depth,
        q0=q0,
        unit_gram=unit_gram,
        A=mp_scale(f_coefficients[1], 1),
        B=mp_scale(f_coefficients[3], factorial(3)),
        C=mp_scale(f_coefficients[5], factorial(5)),
        f_coefficients=f_coefficients,
        diagnostics=diagnostics,
    )


def atom_name(atom: Atom) -> str:
    if atom and atom[0] < 0:
        layer = -atom[0]
        counts = atom[1:]
        width = max(6, len(counts))
        return f"L{layer}_" + "".join(str(value) for value in counts + (0,) * (width - len(counts)))
    width = max(6, len(atom))
    return "M_" + "".join(str(value) for value in atom + (0,) * (width - len(atom)))


def serializable(polynomial: Mapping[MomentMonomial, Fraction]) -> list[dict[str, object]]:
    return [
        {
            "atoms": [atom_name(atom) for atom in monomial],
            "coefficient": str(coefficient),
        }
        for monomial, coefficient in sorted(polynomial.items())
    ]

