"""Exact polynomial audit oracle for the joint fixed-depth/fixed-batch GNF.

This module is intentionally separate from both accepted one-axis
implementations.  It implements the response-aware coordinate recursion in
``DEPTH_FIXED_BATCH_GAUSSIAN_RECURSION.md`` with sparse multivariate polynomials and
exact Isserlis contractions.  It is an audit backend for polynomial
activations, not a Hermite approximation and not the theorem's numerical
implementation for a generic activation.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from typing import Sequence

from ..compiler.normal_form import PolynomialActivation


Number = int | Fraction
Matrix = list[list[Fraction]]
Poly = dict[tuple[int, ...], Fraction]


def _matrix(values: Sequence[Sequence[Number]]) -> Matrix:
    out = [[Fraction(value) for value in row] for row in values]
    if not out or any(len(row) != len(out) for row in out):
        raise ValueError("a covariance must be nonempty and square")
    if any(out[i][j] != out[j][i] for i in range(len(out)) for j in range(i)):
        raise ValueError("a covariance must be symmetric")
    return out


def _zeros(rows: int, columns: int) -> Matrix:
    return [[Fraction(0) for _ in range(columns)] for _ in range(rows)]


def _zero_poly(dimension: int) -> Poly:
    return {}


def _constant(dimension: int, value: Number) -> Poly:
    coefficient = Fraction(value)
    return {} if not coefficient else {(0,) * dimension: coefficient}


def _variable(dimension: int, index: int) -> Poly:
    exponent = [0] * dimension
    exponent[index] = 1
    return {tuple(exponent): Fraction(1)}


def _add(*values: Poly) -> Poly:
    out: Poly = {}
    for value in values:
        for exponent, coefficient in value.items():
            out[exponent] = out.get(exponent, Fraction(0)) + coefficient
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}


def _scale(value: Poly, coefficient: Number) -> Poly:
    coefficient = Fraction(coefficient)
    if not coefficient:
        return {}
    return {
        exponent: coefficient * entry
        for exponent, entry in value.items()
        if coefficient * entry
    }


def _mul(left: Poly, right: Poly) -> Poly:
    if not left or not right:
        return {}
    out: Poly = {}
    for alpha, ca in left.items():
        for beta, cb in right.items():
            exponent = tuple(a + b for a, b in zip(alpha, beta))
            out[exponent] = out.get(exponent, Fraction(0)) + ca * cb
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}


def _power(value: Poly, degree: int, *, dimension: int | None = None) -> Poly:
    if degree < 0:
        raise ValueError("polynomial powers must be nonnegative")
    if dimension is None:
        dimension = len(next(iter(value))) if value else 0
    out = _constant(dimension, 1)
    for _ in range(degree):
        out = _mul(out, value)
    return out


def _differentiate(value: Poly, variable: int) -> Poly:
    out: Poly = {}
    for exponent, coefficient in value.items():
        degree = exponent[variable]
        if degree:
            reduced = list(exponent)
            reduced[variable] -= 1
            key = tuple(reduced)
            out[key] = out.get(key, Fraction(0)) + degree * coefficient
    return {exponent: coefficient for exponent, coefficient in out.items() if coefficient}


def _pad(value: Poly, extra: int) -> Poly:
    if not extra:
        return dict(value)
    return {exponent + (0,) * extra: coefficient for exponent, coefficient in value.items()}


def _compose(coefficients: Sequence[Fraction], argument: Poly, dimension: int) -> Poly:
    out = _zero_poly(dimension)
    power = _constant(dimension, 1)
    for coefficient in coefficients:
        out = _add(out, _scale(power, coefficient))
        power = _mul(power, argument)
    return out


@lru_cache(maxsize=None)
def _moment(
    covariance: tuple[tuple[Fraction, ...], ...], exponent: tuple[int, ...]
) -> Fraction:
    total = sum(exponent)
    if not total:
        return Fraction(1)
    if total % 2:
        return Fraction(0)
    i = next(index for index, count in enumerate(exponent) if count)
    remainder = list(exponent)
    remainder[i] -= 1
    answer = Fraction(0)
    for j, count in enumerate(remainder):
        if not count:
            continue
        paired = list(remainder)
        paired[j] -= 1
        answer += count * covariance[i][j] * _moment(covariance, tuple(paired))
    return answer


def _expect(value: Poly, covariance: Matrix) -> Fraction:
    frozen = tuple(tuple(entry for entry in row) for row in covariance)
    return sum(
        (coefficient * _moment(frozen, exponent) for exponent, coefficient in value.items()),
        Fraction(0),
    )


def _quadratic_form(left: Sequence[Fraction], matrix: Matrix) -> Fraction:
    return sum(
        left[i] * matrix[i][j] * left[j]
        for i in range(len(left))
        for j in range(len(left))
    )


def _frobenius(left: Matrix, right: Matrix) -> Fraction:
    return sum(
        left[i][j] * right[i][j]
        for i in range(len(left))
        for j in range(len(left))
    )


@dataclass(frozen=True)
class _ForwardLayer:
    layer: int
    covariance: Matrix
    z: tuple[tuple[Poly, ...], ...]
    x: tuple[tuple[Poly, ...], ...]
    delta: tuple[Poly, ...]
    gram: tuple[tuple[tuple[tuple[Fraction, ...], ...], ...], ...]
    response: tuple[tuple[tuple[Fraction, ...], ...], ...]
    lambdas: tuple[tuple[tuple[Fraction, ...], ...], ...]
    reverse_offset: int


@dataclass(frozen=True)
class FixedDepthBatchPolynomialGNF:
    ntk: Fraction
    straight_line: Fraction
    hessian_square: Fraction
    correction: Fraction
    hessian_readout: Fraction
    hessian_layers: tuple[Fraction, ...]
    q: tuple[tuple[tuple[Fraction, ...], ...], ...]
    derivative_grams: tuple[tuple[tuple[Fraction, ...], ...], ...]
    theta: tuple[tuple[tuple[Fraction, ...], ...], ...]
    reverse_covariances: tuple[tuple[tuple[Fraction, ...], ...], ...]
    source_covariances: tuple[tuple[tuple[Fraction, ...], ...], ...]
    beta: tuple[tuple[tuple[Fraction, ...], ...], ...]
    chi: tuple[tuple[tuple[Fraction, ...], ...], ...]
    parity_cross_max: Fraction
    parity_response_max: Fraction


def evaluate_fixed_depth_batch_polynomial_gnf(
    input_gram: Sequence[Sequence[Number]],
    channel: Sequence[Number],
    hidden_layers: int,
    activation: PolynomialActivation,
) -> FixedDepthBatchPolynomialGNF:
    """Evaluate the candidate joint GNF exactly for a polynomial activation."""

    if hidden_layers < 1:
        raise ValueError("hidden_layers must be positive")
    q0 = _matrix(input_gram)
    batch = len(q0)
    c = [Fraction(value) for value in channel]
    if len(c) != batch:
        raise ValueError("channel and input Gram dimensions differ")
    h = hidden_layers

    # Base NNGP and derivative Grams.
    q: list[Matrix] = [q0]
    e: list[Matrix] = [_zeros(batch, batch)]
    for layer in range(1, h + 1):
        covariance = q[layer - 1]
        variables = [_variable(batch, index) for index in range(batch)]
        phi0 = [
            _compose(activation.derivative(0), variables[index], batch)
            for index in range(batch)
        ]
        phi1 = [
            _compose(activation.derivative(1), variables[index], batch)
            for index in range(batch)
        ]
        q.append(
            [[_expect(_mul(phi0[a], phi0[b]), covariance) for b in range(batch)] for a in range(batch)]
        )
        e.append(
            [[_expect(_mul(phi1[a], phi1[b]), covariance) for b in range(batch)] for a in range(batch)]
        )

    # Reverse carrier/source covariances.  Index zero is a harmless sentinel.
    reverse_covariance = [_zeros(batch, batch) for _ in range(h + 1)]
    source_covariance = [_zeros(batch, batch) for _ in range(h + 1)]
    reverse_covariance[h] = [[c[a] * c[b] for b in range(batch)] for a in range(batch)]
    for layer in range(h, 0, -1):
        source_covariance[layer] = [
            [reverse_covariance[layer][a][b] * e[layer][a][b] for b in range(batch)]
            for a in range(batch)
        ]
        if layer > 1:
            reverse_covariance[layer - 1] = [row[:] for row in source_covariance[layer]]

    theta: list[Matrix] = [q0]
    for layer in range(1, h + 1):
        theta.append(
            [
                [q[layer][a][b] + e[layer][a][b] * theta[layer - 1][a][b] for b in range(batch)]
                for a in range(batch)
            ]
        )

    layers: list[_ForwardLayer] = []
    prior_gram = None
    prior_response = None
    for layer in range(1, h + 1):
        if layer == 1:
            dimension = 2 * batch
            covariance = _zeros(dimension, dimension)
            for a in range(batch):
                for b in range(batch):
                    covariance[a][b] = q0[a][b]
                    covariance[batch + a][batch + b] = reverse_covariance[layer][a][b]
            base = [_variable(dimension, a) for a in range(batch)]
            reverse_offset = batch
            lambdas = [_zeros(batch, batch) for _ in range(4)]
        else:
            assert prior_gram is not None and prior_response is not None
            dimension = 5 * batch
            covariance = _zeros(dimension, dimension)
            for r in range(4):
                for s in range(4):
                    for a in range(batch):
                        for b in range(batch):
                            covariance[r * batch + a][s * batch + b] = prior_gram[r][s][a][b]
            reverse_offset = 4 * batch
            for a in range(batch):
                for b in range(batch):
                    covariance[reverse_offset + a][reverse_offset + b] = reverse_covariance[layer][a][b]
            base = [_variable(dimension, a) for a in range(batch)]
            lambdas = [_zeros(batch, batch) for _ in range(4)]
            for r in range(1, 4):
                for a in range(batch):
                    for b in range(batch):
                        lambdas[r][a][b] = (
                            prior_response[r][a][b]
                            + r * prior_gram[0][r - 1][a][b]
                        )

        phi = [
            [
                _compose(activation.derivative(order), base[a], dimension)
                for a in range(batch)
            ]
            for order in range(4)
        ]
        reverse = [_variable(dimension, reverse_offset + a) for a in range(batch)]
        delta = [_mul(phi[1][a], reverse[a]) for a in range(batch)]
        z: list[list[Poly]] = [[base[a] for a in range(batch)]]
        for r in range(1, 4):
            zr: list[Poly] = []
            for b in range(batch):
                if layer == 1:
                    value = _zero_poly(dimension)
                    if r == 1:
                        value = _add(
                            *[_scale(delta[a], q0[a][b]) for a in range(batch)]
                        )
                else:
                    value = _variable(dimension, r * batch + b)
                    value = _add(
                        value,
                        *[_scale(delta[a], lambdas[r][a][b]) for a in range(batch)],
                    )
                zr.append(value)
            z.append(zr)

        x0 = phi[0]
        x1 = [_mul(phi[1][a], z[1][a]) for a in range(batch)]
        x2 = [
            _add(
                _mul(phi[2][a], _power(z[1][a], 2, dimension=dimension)),
                _mul(phi[1][a], z[2][a]),
            )
            for a in range(batch)
        ]
        x3 = [
            _add(
                _mul(phi[3][a], _power(z[1][a], 3, dimension=dimension)),
                _scale(_mul(_mul(phi[2][a], z[1][a]), z[2][a]), 3),
                _mul(phi[1][a], z[3][a]),
            )
            for a in range(batch)
        ]
        x = [x0, x1, x2, x3]
        gram = [
            [
                [
                    [_expect(_mul(x[r][a], x[s][b]), covariance) for b in range(batch)]
                    for a in range(batch)
                ]
                for s in range(4)
            ]
            for r in range(4)
        ]
        response = [
            [
                [
                    _expect(_differentiate(x[r][b], reverse_offset + a), covariance)
                    for b in range(batch)
                ]
                for a in range(batch)
            ]
            for r in range(4)
        ]
        state = _ForwardLayer(
            layer=layer,
            covariance=covariance,
            z=tuple(tuple(value for value in row) for row in z),
            x=tuple(tuple(value for value in row) for row in x),
            delta=tuple(delta),
            gram=tuple(
                tuple(tuple(tuple(value for value in row) for row in block) for block in blocks)
                for blocks in gram
            ),
            response=tuple(
                tuple(tuple(value for value in row) for row in matrix)
                for matrix in response
            ),
            lambdas=tuple(
                tuple(tuple(value for value in row) for row in matrix)
                for matrix in lambdas
            ),
            reverse_offset=reverse_offset,
        )
        layers.append(state)
        prior_gram = gram
        prior_response = response

    top = layers[-1]
    straight_line = sum(
        (_expect(_mul(_variable(len(top.covariance), top.reverse_offset + a), top.x[3][a]), top.covariance) for a in range(batch)),
        Fraction(0),
    )
    straight_line += 3 * sum(
        c[a] * top.gram[0][2][a][b] * c[b]
        for a in range(batch)
        for b in range(batch)
    )

    beta = [_zeros(batch, batch) for _ in range(h + 1)]
    chi = [_zeros(batch, batch) for _ in range(h + 1)]
    max_cross = Fraction(0)
    max_higher_response = Fraction(0)
    for layer in range(h, 0, -1):
        state = layers[layer - 1]
        old_dimension = len(state.covariance)
        has_eta = layer < h
        extra = batch if has_eta else 0
        dimension = old_dimension + extra
        covariance = _zeros(dimension, dimension)
        for a in range(old_dimension):
            for b in range(old_dimension):
                covariance[a][b] = state.covariance[a][b]
        if has_eta:
            for a in range(batch):
                for b in range(batch):
                    covariance[old_dimension + a][old_dimension + b] = beta[layer + 1][a][b]

        x = [[_pad(value, extra) for value in row] for row in state.x]
        z = [[_pad(value, extra) for value in row] for row in state.z]
        delta = [_pad(value, extra) for value in state.delta]
        reverse = [
            _variable(dimension, state.reverse_offset + a) for a in range(batch)
        ]
        phi = [
            [
                _compose(activation.derivative(order), z[0][a], dimension)
                for a in range(batch)
            ]
            for order in range(4)
        ]
        if layer == h:
            projected = _add(*[_scale(x[0][s], c[s]) for s in range(batch)])
            reverse_dot = [_scale(projected, c[a]) for a in range(batch)]
        else:
            reverse_dot = []
            for b in range(batch):
                value = _variable(dimension, old_dimension + b)
                value = _add(
                    value,
                    *[_scale(x[0][a], chi[layer + 1][a][b]) for a in range(batch)],
                )
                reverse_dot.append(value)
        delta_dot = [
            _add(
                _mul(_mul(phi[2][a], z[1][a]), reverse[a]),
                _mul(phi[1][a], reverse_dot[a]),
            )
            for a in range(batch)
        ]
        beta[layer] = [
            [_expect(_mul(delta_dot[a], delta_dot[b]), covariance) for b in range(batch)]
            for a in range(batch)
        ]
        cross = [
            [_expect(_mul(delta[a], delta_dot[b]), covariance) for b in range(batch)]
            for a in range(batch)
        ]
        max_cross = max(max_cross, *(abs(value) for row in cross for value in row))

        if layer > 1:
            rho = []
            for r in range(4):
                rho.append(
                    [
                        [
                            _expect(_differentiate(delta_dot[b], r * batch + a), covariance)
                            for b in range(batch)
                        ]
                        for a in range(batch)
                    ]
                )
            max_higher_response = max(
                max_higher_response,
                *(abs(value) for r in range(1, 4) for row in rho[r] for value in row),
            )
            chi[layer] = [
                [source_covariance[layer][a][b] + rho[0][a][b] for b in range(batch)]
                for a in range(batch)
            ]

    hessian_readout = sum(
        c[a] * top.gram[1][1][a][b] * c[b]
        for a in range(batch)
        for b in range(batch)
    )
    hessian_layers = [Fraction(0)] * (h + 1)
    hessian_layers[1] = _frobenius(beta[1], q0)
    for layer in range(2, h + 1):
        hessian_layers[layer] = (
            _frobenius(beta[layer], q[layer - 1])
            + _frobenius(source_covariance[layer], [list(row) for row in layers[layer - 2].gram[1][1]])
        )
    hessian_square = hessian_readout + sum(hessian_layers[1:], Fraction(0))
    correction = 2 * straight_line + 4 * hessian_square

    ntk_blocks = _quadratic_form(c, q[h]) + sum(
        (_frobenius(source_covariance[layer], q[layer - 1]) for layer in range(1, h + 1)),
        Fraction(0),
    )
    ntk = _quadratic_form(c, theta[h])
    if ntk != ntk_blocks:
        raise AssertionError(f"NTK recursion/block mismatch: {ntk} != {ntk_blocks}")
    if max_cross or max_higher_response:
        raise AssertionError(
            "parity closure failed: "
            f"cross={max_cross}, higher_response={max_higher_response}"
        )

    freeze_matrix = lambda value: tuple(tuple(entry for entry in row) for row in value)
    return FixedDepthBatchPolynomialGNF(
        ntk=ntk,
        straight_line=straight_line,
        hessian_square=hessian_square,
        correction=correction,
        hessian_readout=hessian_readout,
        hessian_layers=tuple(hessian_layers),
        q=tuple(freeze_matrix(value) for value in q),
        derivative_grams=tuple(freeze_matrix(value) for value in e),
        theta=tuple(freeze_matrix(value) for value in theta),
        reverse_covariances=tuple(freeze_matrix(value) for value in reverse_covariance),
        source_covariances=tuple(freeze_matrix(value) for value in source_covariance),
        beta=tuple(freeze_matrix(value) for value in beta),
        chi=tuple(freeze_matrix(value) for value in chi),
        parity_cross_max=max_cross,
        parity_response_max=max_higher_response,
    )
