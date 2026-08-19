"""Audited initialization NTK normal form for two hidden layers, one input."""

from __future__ import annotations

from dataclasses import dataclass

from .normal_form import GaussianAtom, PhiFactor, Scalar, Symbol, add, atom, mul


@dataclass(frozen=True)
class L2B1Initialization:
    q0: Scalar
    q1: GaussianAtom
    d1: GaussianAtom
    q2: GaussianAtom
    d2: GaussianAtom
    ntk: Scalar


def initialization_normal_form(q0: Scalar | int = Symbol("q_0")) -> L2B1Initialization:
    """Return the literal GNF DAG for ``A = F'(0)``.

    Model convention:

        U_j ~ N(0,q0), H_j=phi(U_j),
        Z_i=n^{-1/2} sum_j W_ij H_j,
        f_n=n^{-1} sum_i a_i phi(Z_i),

    with raw-coordinate feature generator ``D_n=n grad(f_n).grad``.  The
    first-layer raw weights induce the scalar input metric ``q0``.
    """

    q1 = atom([[q0]], [PhiFactor(0, 0, 2)], tag="q_1")
    d1 = atom([[q0]], [PhiFactor(0, 1, 2)], tag="d_1")
    q2 = atom([[q1]], [PhiFactor(0, 0, 2)], tag="q_2")
    d2 = atom([[q1]], [PhiFactor(0, 1, 2)], tag="d_2")
    ntk = add(q2, mul(q1, d2), mul(q0, d1, d2))
    return L2B1Initialization(q0, q1, d1, q2, d2, ntk)
