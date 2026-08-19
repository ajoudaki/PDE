"""Exact polynomial audit of the fully contracted fixed-batch GNF.

This is deliberately independent of the finite-width Tensor-Program and
Taylor-jet evaluators.  It evaluates the proposed width-limit formula after
all readout/fresh-Gaussian variables have been Wick contracted, leaving only
literal Gaussian expectations of activation derivatives at the two input
and two top preactivation coordinates.

The implementation is written for any fixed batch dimension, although the
audit suite uses B=1 and B=2.  It is an exact rational backend for polynomial
activations and is not a Hermite approximation.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from typing import Iterable, Sequence

from ..compiler.normal_form import (
    PhiFactor,
    PolynomialActivation,
    atom,
    evaluate_polynomial,
)


Number = int | Fraction
Matrix = list[list[Fraction]]


def _fraction_matrix(values: Sequence[Sequence[Number]]) -> Matrix:
    matrix = [[Fraction(value) for value in row] for row in values]
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("covariance must be nonempty and square")
    if any(matrix[i][j] != matrix[j][i] for i in range(len(matrix)) for j in range(i)):
        raise ValueError("covariance must be symmetric")
    return matrix


def _expectation(
    covariance: Matrix,
    factors: Iterable[tuple[int, int]],
    activation: PolynomialActivation,
) -> Fraction:
    return evaluate_polynomial(
        atom(
            covariance,
            [PhiFactor(variable=index, derivative=derivative) for index, derivative in factors],
        ),
        activation,
        {},
    )


@dataclass(frozen=True)
class ContractedDirectionalGNF:
    ntk: Fraction
    straight_line: Fraction
    hessian_readout: Fraction
    hessian_middle: Fraction
    hessian_first: Fraction

    @property
    def correction(self) -> Fraction:
        return 2 * self.straight_line + 4 * (
            self.hessian_readout + self.hessian_middle + self.hessian_first
        )


def evaluate_contracted_directional_gnf(
    input_gram: Sequence[Sequence[Number]],
    channel: Sequence[Number],
    activation: PolynomialActivation,
) -> ContractedDirectionalGNF:
    """Evaluate the contracted arbitrary-fixed-batch formula exactly."""

    q0 = _fraction_matrix(input_gram)
    batch = len(q0)
    c = [Fraction(value) for value in channel]
    if len(c) != batch:
        raise ValueError("channel and Gram dimensions differ")

    eu = lambda factors: _expectation(q0, factors, activation)

    q1 = [[eu(((a, 0), (b, 0))) for b in range(batch)] for a in range(batch)]
    d1 = [[eu(((a, 1), (b, 1))) for b in range(batch)] for a in range(batch)]
    ez = lambda factors: _expectation(q1, factors, activation)
    q2 = [[ez(((a, 0), (b, 0))) for b in range(batch)] for a in range(batch)]
    d2 = [[ez(((a, 1), (b, 1))) for b in range(batch)] for a in range(batch)]

    source_cov = [
        [c[a] * c[b] * d2[a][b] for b in range(batch)]
        for a in range(batch)
    ]
    response_l = [
        [q0[s][a] * d1[s][a] for a in range(batch)]
        for s in range(batch)
    ]
    tangent_c = [
        [q1[s][a] + response_l[s][a] for a in range(batch)]
        for s in range(batch)
    ]

    # P_a = phi'(U_a) sum_p Q0[a,p] phi'(U_p) R_p.
    tangent_cov = [[Fraction(0) for _ in range(batch)] for _ in range(batch)]
    for a, b in product(range(batch), repeat=2):
        tangent_cov[a][b] = sum(
            q0[a][p]
            * q0[b][r]
            * source_cov[p][r]
            * eu(((a, 1), (p, 1), (b, 1), (r, 1)))
            for p, r in product(range(batch), repeat=2)
        )

    # M[s,a] = E[X0_s X2_a t_a^2].
    second_cross = [[Fraction(0) for _ in range(batch)] for _ in range(batch)]
    # N[s,a] is the response of A[X3_a t_a^3] along source column s.
    third_response = [[Fraction(0) for _ in range(batch)] for _ in range(batch)]
    for s, a in product(range(batch), repeat=2):
        second_cross[s][a] = sum(
            q0[a][p]
            * q0[a][r]
            * source_cov[p][r]
            * eu(((s, 0), (a, 2), (p, 1), (r, 1)))
            for p, r in product(range(batch), repeat=2)
        )
        third_response[s][a] = 3 * q0[a][s] * sum(
            q0[a][p]
            * q0[a][r]
            * source_cov[p][r]
            * eu(((a, 3), (s, 1), (p, 1), (r, 1)))
            for p, r in product(range(batch), repeat=2)
        )
    tau_response = [
        [3 * second_cross[s][a] + third_response[s][a] for a in range(batch)]
        for s in range(batch)
    ]

    # Helpers expand h=sum_i c_i y0_i and v_a=sum_s C[s,a]c_s y1_s.
    def e_h_y2(a: int) -> Fraction:
        return sum(c[i] * ez(((i, 0), (a, 2))) for i in range(batch))

    def e_y3_v(a: int) -> Fraction:
        return sum(
            tangent_c[s][a] * c[s] * ez(((a, 3), (s, 1)))
            for s in range(batch)
        )

    # Fresh variance beta=E[B_a B_b] after readout/Gamma Wick contraction.
    beta = [[Fraction(0) for _ in range(batch)] for _ in range(batch)]
    for a, b in product(range(batch), repeat=2):
        ff = sum(
            c[i]
            * c[j]
            * ez(((i, 0), (a, 1), (j, 0), (b, 1)))
            for i, j in product(range(batch), repeat=2)
        )
        fg = sum(
            c[i]
            * tangent_c[j][b]
            * c[j]
            * ez(((i, 0), (a, 1), (b, 2), (j, 1)))
            for i, j in product(range(batch), repeat=2)
        )
        gf = sum(
            tangent_c[i][a]
            * c[i]
            * c[j]
            * ez(((a, 2), (i, 1), (j, 0), (b, 1)))
            for i, j in product(range(batch), repeat=2)
        )
        gg = sum(
            tangent_c[i][a]
            * c[i]
            * tangent_c[j][b]
            * c[j]
            * ez(((a, 2), (i, 1), (b, 2), (j, 1)))
            for i, j in product(range(batch), repeat=2)
        )
        beta[a][b] = c[a] * c[b] * (
            ff
            + fg
            + gf
            + 3 * gg
            + tangent_cov[a][b] * ez(((a, 2), (b, 2)))
        )

    # Nested A^T B response and the total differentiated-backward response.
    nested_response = [[Fraction(0) for _ in range(batch)] for _ in range(batch)]
    total_response = [[Fraction(0) for _ in range(batch)] for _ in range(batch)]
    for s, a in product(range(batch), repeat=2):
        nested_response[s][a] = c[a] * (
            c[s] * d2[s][a]
            + (e_h_y2(a) + e_y3_v(a) if s == a else 0)
            + c[s] * tangent_c[s][a] * ez(((s, 2), (a, 2)))
        )
        total_response[s][a] = source_cov[s][a] + nested_response[s][a]

    # H_a: integrate the readout and fresh first-tangent Gaussian exactly.
    hessian_readout = sum(
        c[a]
        * tangent_c[s][a]
        * c[s]
        * c[b]
        * tangent_c[r][b]
        * c[r]
        * ez(((a, 1), (s, 1), (b, 1), (r, 1)))
        for a, s, b, r in product(range(batch), repeat=4)
    )
    hessian_readout += sum(
        c[a] * c[b] * tangent_cov[a][b] * d2[a][b]
        for a, b in product(range(batch), repeat=2)
    )

    hessian_middle = sum(
        q1[a][b] * beta[a][b]
        + source_cov[a][b] * tangent_cov[a][b]
        for a, b in product(range(batch), repeat=2)
    )

    # Straight-line branch after Wick/Stein elimination of a,Gamma,Omega,Lambda.
    straight_line = Fraction(0)
    for a in range(batch):
        y3_v3 = sum(
            tangent_c[i][a]
            * c[i]
            * tangent_c[j][a]
            * c[j]
            * tangent_c[k][a]
            * c[k]
            * ez(((a, 3), (i, 1), (j, 1), (k, 1)))
            for i, j, k in product(range(batch), repeat=3)
        )
        y3_v = sum(
            tangent_c[i][a] * c[i] * ez(((a, 3), (i, 1)))
            for i in range(batch)
        )
        y1_w = sum(
            tau_response[s][a] * c[s] * d2[a][s]
            for s in range(batch)
        )
        h_y2_v2 = sum(
            c[i]
            * tangent_c[j][a]
            * c[j]
            * tangent_c[k][a]
            * c[k]
            * ez(((i, 0), (a, 2), (j, 1), (k, 1)))
            for i, j, k in product(range(batch), repeat=3)
        )
        straight_line += c[a] * (
            3 * y3_v3
            + 3 * tangent_cov[a][a] * y3_v
            + y1_w
            + 3 * h_y2_v2
            + 3 * tangent_cov[a][a] * e_h_y2(a)
        )
        for s in range(batch):
            omega_stein = (
                (y3_v if s == a else 0)
                + tangent_c[s][a] * c[s] * ez(((a, 2), (s, 2)))
                + c[s] * d2[s][a]
                + (e_h_y2(a) if s == a else 0)
            )
            straight_line += 3 * c[a] * second_cross[s][a] * omega_stein

    # H_U after Wick contraction of R and the fresh Eta field.
    hessian_first = Fraction(0)
    for a, b in product(range(batch), repeat=2):
        aa = sum(
            q0[a][p]
            * q0[b][r]
            * (
                source_cov[a][p] * source_cov[b][r]
                + source_cov[a][b] * source_cov[p][r]
                + source_cov[a][r] * source_cov[p][b]
            )
            * eu(((a, 2), (p, 1), (b, 2), (r, 1)))
            for p, r in product(range(batch), repeat=2)
        )
        bb = sum(
            total_response[s][a]
            * total_response[t][b]
            * eu(((a, 1), (s, 0), (b, 1), (t, 0)))
            for s, t in product(range(batch), repeat=2)
        )
        ba = sum(
            total_response[s][a]
            * q0[b][p]
            * source_cov[b][p]
            * eu(((a, 1), (s, 0), (b, 2), (p, 1)))
            for s, p in product(range(batch), repeat=2)
        )
        ab = sum(
            total_response[t][b]
            * q0[a][p]
            * source_cov[a][p]
            * eu(((b, 1), (t, 0), (a, 2), (p, 1)))
            for t, p in product(range(batch), repeat=2)
        )
        hessian_first += q0[a][b] * (
            aa + bb + ba + ab + beta[a][b] * d1[a][b]
        )

    ntk = sum(
        c[a]
        * c[b]
        * (
            q2[a][b]
            + q1[a][b] * d2[a][b]
            + q0[a][b] * d1[a][b] * d2[a][b]
        )
        for a, b in product(range(batch), repeat=2)
    )

    return ContractedDirectionalGNF(
        ntk=ntk,
        straight_line=straight_line,
        hessian_readout=hessian_readout,
        hessian_middle=hessian_middle,
        hessian_first=hessian_first,
    )
