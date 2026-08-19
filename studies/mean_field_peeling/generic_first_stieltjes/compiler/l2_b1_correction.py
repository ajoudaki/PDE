"""Literal candidate GNF for ``C=lim E[D_n^3 f_n]`` at L=2, B=1.

Every primitive below is a one-dimensional Gaussian atom.  Auxiliary Python
names are finite-DAG common subexpressions; none denotes an unexpanded random
response field.  ``atom_inventory(correction)`` returns the complete list of
Gaussian integrations.
"""

from __future__ import annotations

from dataclasses import dataclass

from .normal_form import (
    GaussianAtom,
    PhiFactor,
    Scalar,
    Symbol,
    add,
    atom,
    mul,
    power,
)


def _univariate(
    variance: Scalar,
    derivatives: tuple[tuple[int, int], ...],
    tag: str,
) -> GaussianAtom:
    """Build ``E prod_r phi^(r)(X)^multiplicity``."""

    return atom(
        [[variance]],
        [
            PhiFactor(variable=0, derivative=order, multiplicity=multiplicity)
            for order, multiplicity in derivatives
        ],
        tag=tag,
    )


@dataclass(frozen=True)
class L2B1FirstCorrection:
    # First-layer atoms, U ~ N(0,q0).
    q0: Scalar
    Q: GaussianAtom
    d: GaussianAtom
    m4: GaussianAtom
    mA: GaussianAtom
    mB: GaussianAtom
    n21: GaussianAtom
    aX: GaussianAtom

    # Second-layer atoms, Z ~ N(0,Q).
    q2: GaussianAtom
    D: GaussianAtom
    z_phi_phi2: GaussianAtom
    z_phi2_sq: GaussianAtom
    z_phi1_phi3: GaussianAtom
    p1: GaussianAtom
    p3: GaussianAtom
    p4: GaussianAtom
    y14: GaussianAtom
    e0: GaussianAtom
    e12: GaussianAtom

    # Algebraic DAG nodes.
    alpha: Scalar
    V: Scalar
    kappa: Scalar
    c0: Scalar
    c1: Scalar
    b2: Scalar
    c: Scalar
    tangent_branch: Scalar
    straight_line_branch: Scalar
    hessian_branch: Scalar
    correction: Scalar
    ntk: Scalar


def first_correction_normal_form(
    q0: Scalar | int = Symbol("q_0"),
) -> L2B1FirstCorrection:
    """Emit the proposed explicit normal form for ``A`` and ``C``.

    The finite expression assumes the model frozen in ``README.md`` and
    activation derivatives through order three.  Establishing its
    finite-width-to-mean-field limit is a separate proof obligation.
    """

    # U ~ N(0,q0).
    Q = _univariate(q0, ((0, 2),), "Q=E_U[phi^2]")
    d = _univariate(q0, ((1, 2),), "d=E_U[phi1^2]")
    m4 = _univariate(q0, ((1, 4),), "m4=E_U[phi1^4]")
    mA = _univariate(
        q0, ((0, 1), (1, 2), (2, 1)), "mA=E_U[phi phi1^2 phi2]"
    )
    mB = _univariate(q0, ((1, 3), (3, 1)), "mB=E_U[phi1^3 phi3]")
    n21 = _univariate(q0, ((1, 2), (2, 2)), "n21=E_U[phi1^2 phi2^2]")
    aX = _univariate(q0, ((0, 2), (1, 2)), "aX=E_U[phi^2 phi1^2]")

    # Z ~ N(0,Q).
    q2 = _univariate(Q, ((0, 2),), "q2=E_Z[phi^2]")
    D = _univariate(Q, ((1, 2),), "D=E_Z[phi1^2]")
    z_phi_phi2 = _univariate(Q, ((0, 1), (2, 1)), "E_Z[phi phi2]")
    z_phi2_sq = _univariate(Q, ((2, 2),), "e2=E_Z[phi2^2]")
    z_phi1_phi3 = _univariate(Q, ((1, 1), (3, 1)), "E_Z[phi1 phi3]")
    p1 = _univariate(
        Q, ((0, 1), (1, 2), (2, 1)), "p1=E_Z[phi phi1^2 phi2]"
    )
    p3 = _univariate(Q, ((1, 3), (3, 1)), "p3=E_Z[phi1^3 phi3]")
    # The p4 occurrence is the same mathematical atom as z_phi1_phi3.  Keep
    # one DAG leaf so the emitted inventory matches the 17-atom normal form.
    p4 = z_phi1_phi3
    y14 = _univariate(Q, ((1, 4),), "y14=E_Z[phi1^4]")
    e0 = _univariate(Q, ((0, 2), (1, 2)), "e0=E_Z[phi^2 phi1^2]")
    e12 = _univariate(Q, ((1, 2), (2, 2)), "e12=E_Z[phi1^2 phi2^2]")

    c0 = add(D, z_phi_phi2)
    c1 = add(z_phi2_sq, z_phi1_phi3)
    alpha = add(Q, mul(q0, d))
    V = mul(power(q0, 2), m4, D)
    kappa = mul(power(q0, 2), D, mA)

    b2 = add(
        e0,
        mul(2, alpha, p1),
        mul(3, power(alpha, 2), e12),
        mul(V, z_phi2_sq),
    )
    c = add(D, c0, mul(alpha, c1))

    tangent_branch = add(
        mul(power(alpha, 2), p1),
        mul(V, z_phi_phi2),
        mul(kappa, c0),
        mul(power(alpha, 3), p3),
        mul(alpha, V, p4),
        mul(alpha, kappa, c1),
        mul(
            power(D, 2),
            add(mul(power(q0, 2), mA), mul(power(q0, 3), mB)),
        ),
    )

    hessian_branch = add(
        mul(power(alpha, 2), y14),
        mul(2, V, D),
        mul(Q, b2),
        mul(
            q0,
            add(
                mul(3, power(q0, 2), power(D, 2), n21),
                mul(power(c, 2), aX),
                mul(b2, d),
                mul(2, q0, D, c, mA),
            ),
        ),
    )

    # Rebuild canonical note equation (3.6) literally.  Analytically this is
    # 3*tangent_branch, but retaining the canonical sum makes an independent
    # structural-expression equality test possible without distributive
    # rewriting in the intentionally small IR.
    straight_kappa = add(
        mul(3, power(q0, 2), D, mA),
        mul(3, power(q0, 3), D, mB),
    )
    straight_line_branch = add(
        mul(3, power(alpha, 2), p1),
        mul(3, power(q0, 2), m4, D, z_phi_phi2),
        mul(3, power(q0, 2), D, mA, add(D, z_phi_phi2)),
        mul(3, power(alpha, 3), p3),
        mul(3, alpha, power(q0, 2), m4, D, z_phi1_phi3),
        mul(
            3,
            power(q0, 2),
            alpha,
            D,
            mA,
            add(z_phi1_phi3, z_phi2_sq),
        ),
        mul(straight_kappa, D),
    )
    correction = add(mul(2, straight_line_branch), mul(4, hessian_branch))
    ntk = add(q2, mul(Q, D), mul(q0, d, D))

    return L2B1FirstCorrection(
        q0=q0,
        Q=Q,
        d=d,
        m4=m4,
        mA=mA,
        mB=mB,
        n21=n21,
        aX=aX,
        q2=q2,
        D=D,
        z_phi_phi2=z_phi_phi2,
        z_phi2_sq=z_phi2_sq,
        z_phi1_phi3=z_phi1_phi3,
        p1=p1,
        p3=p3,
        p4=p4,
        y14=y14,
        e0=e0,
        e12=e12,
        alpha=alpha,
        V=V,
        kappa=kappa,
        c0=c0,
        c1=c1,
        b2=b2,
        c=c,
        tangent_branch=tangent_branch,
        straight_line_branch=straight_line_branch,
        hessian_branch=hessian_branch,
        correction=correction,
        ntk=ntk,
    )
