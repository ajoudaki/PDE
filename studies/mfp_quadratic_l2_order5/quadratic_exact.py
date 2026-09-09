#!/usr/bin/env python3
"""Exact L=2 quadratic activation contractions and Euler coefficients.

The activation is psi(x)=p*x+q*x**2 with p**2+3*q**2=1.  To exhibit
the normalization rationally we first compute in unnormalised symbols
(a,b), then substitute p=a/sqrt(a**2+3*b**2),
q=b/sqrt(a**2+3*b**2).

Only exact Fraction arithmetic is used.  The six order-five contractions
are supplied by the audited fixed-depth scalar OMFP recurrence.
"""

from __future__ import annotations

from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from generic_first_stieltjes.depth_order5_scalar.primary.moving_scalar_extension import (  # noqa: E402
    assemble_moving_recurrence,
)


# A bivariate polynomial in (a,b), represented by (a-degree,b-degree)->Q.
BPoly = dict[tuple[int, int], Q]
# A polynomial in (a,b,x), used before Gaussian expectation.
TPoly = dict[tuple[int, int, int], Q]


def bp_add(*values: BPoly) -> BPoly:
    out: BPoly = {}
    for value in values:
        for key, coefficient in value.items():
            out[key] = out.get(key, Q(0)) + coefficient
    return {key: value for key, value in out.items() if value}


def bp_scale(c: int | Q, value: BPoly) -> BPoly:
    c = Q(c)
    return {key: c*x for key, x in value.items() if c*x}


def bp_mul(left: BPoly, right: BPoly) -> BPoly:
    out: BPoly = {}
    for (i, j), x in left.items():
        for (k, ell), y in right.items():
            key = (i+k, j+ell)
            out[key] = out.get(key, Q(0)) + x*y
    return {key: value for key, value in out.items() if value}


def bp_pow(value: BPoly, exponent: int) -> BPoly:
    out: BPoly = {(0, 0): Q(1)}
    base = value
    while exponent:
        if exponent & 1:
            out = bp_mul(out, base)
        exponent >>= 1
        if exponent:
            base = bp_mul(base, base)
    return out


def tp_mul(left: TPoly, right: TPoly) -> TPoly:
    out: TPoly = {}
    for (i, j, k), x in left.items():
        for (r, s, ell), y in right.items():
            key = (i+r, j+s, k+ell)
            out[key] = out.get(key, Q(0)) + x*y
    return {key: value for key, value in out.items() if value}


def tp_pow(value: TPoly, exponent: int) -> TPoly:
    out: TPoly = {(0, 0, 0): Q(1)}
    base = value
    while exponent:
        if exponent & 1:
            out = tp_mul(out, base)
        exponent >>= 1
        if exponent:
            base = tp_mul(base, base)
    return out


def gaussian_moment(k: int) -> int:
    if k & 1:
        return 0
    out = 1
    for odd in range(1, k, 2):
        out *= odd
    return out


@lru_cache(None)
def activation_atom(exponents: tuple[int, ...]) -> tuple[tuple[tuple[int, int], Q], ...]:
    derivatives: tuple[TPoly, ...] = (
        {(1, 0, 1): Q(1), (0, 1, 2): Q(1)},
        {(1, 0, 0): Q(1), (0, 1, 1): Q(2)},
        {(0, 1, 0): Q(2)},
        {}, {}, {},
    )
    value: TPoly = {(0, 0, 0): Q(1)}
    for order, count in enumerate(exponents):
        if count:
            value = tp_mul(value, tp_pow(derivatives[order], count))
            if not value:
                return ()
    out: BPoly = {}
    for (i, j, k), coefficient in value.items():
        coefficient *= gaussian_moment(k)
        if coefficient:
            out[(i, j)] = out.get((i, j), Q(0)) + coefficient
    return tuple(sorted((key, value) for key, value in out.items() if value))


def eval_expr(root) -> BPoly:
    memo = {}

    def visit(node):
        if node in memo:
            return memo[node]
        kind = node.node[0]
        if kind == "const":
            value = {(0, 0): node.node[1]} if node.node[1] else {}
        elif kind == "atom":
            if node.node[1] != "M":
                raise ValueError(node.node[1])
            value = dict(activation_atom(tuple(node.node[2])))
        elif kind == "add":
            value = bp_add(*(visit(child) for child in node.node[1]))
        elif kind == "mul":
            value = {(0, 0): Q(1)}
            for child in node.node[1]:
                value = bp_mul(value, visit(child))
        elif kind == "symbol":
            raise ValueError(f"unresolved symbol {node.node[1]}")
        else:
            raise ValueError(kind)
        memo[node] = value
        return value

    return visit(root)


def normalized_numerator(poly: BPoly) -> tuple[BPoly, int]:
    """Return R,K with P(a/s,b/s)=R(a,b)/(a^2+3b^2)^K."""
    totals = {i+j for i, j in poly}
    if any(total & 1 for total in totals):
        raise AssertionError(f"odd activation degree(s): {sorted(totals)}")
    K = max(totals, default=0) // 2
    D = {(2, 0): Q(1), (0, 2): Q(3)}
    out: BPoly = {}
    for (i, j), coefficient in poly.items():
        lift = bp_scale(coefficient, {(i, j): Q(1)})
        lift = bp_mul(lift, bp_pow(D, K - (i+j)//2))
        out = bp_add(out, lift)
    return out, K


def fmt_fraction(x: Q) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def fmt_poly(poly: BPoly, avar: str = "a", bvar: str = "b") -> str:
    if not poly:
        return "0"
    terms = []
    for (i, j), coefficient in sorted(poly.items(), key=lambda item: (-sum(item[0]), -item[0][0])):
        factors = []
        if i:
            factors.append(avar if i == 1 else f"{avar}^{i}")
        if j:
            factors.append(bvar if j == 1 else f"{bvar}^{j}")
        monomial = "*".join(factors) or "1"
        terms.append(f"({fmt_fraction(coefficient)})*{monomial}")
    return " + ".join(terms)


def exact_contractions() -> dict[str, BPoly]:
    result = assemble_moving_recurrence(2)
    I1 = eval_expr(result.frozen.straight5)
    I2 = eval_expr(result.frozen.gram31)
    I3 = eval_expr(result.frozen.gram22)
    Bm2 = eval_expr(result.B_m2)
    M2 = eval_expr(result.m2_norm)
    Am3 = eval_expr(result.A_m3)
    I4 = bp_add(Bm2, bp_scale(-1, I3))
    I6 = bp_add(M2, I3, bp_scale(-2, Bm2))
    I5 = bp_scale(Q(1, 3), bp_add(Am3, bp_scale(-1, I2),
                                     bp_scale(-1, I4), bp_scale(-1, I6)))
    return {f"I{k}": value for k, value in enumerate((I1,I2,I3,I4,I5,I6), 1)}


PAIR_WEIGHTS = {
    # coefficient arrays in ascending t power, with index 0 unused
    "I1": (Q(0), Q(1,24), Q(0), Q(-1,3), Q(1,3)),
    "I2": (Q(0), Q(1,12), Q(35,12), Q(-23,3), Q(19,3)),
    "I3": (Q(0), Q(-1,4), Q(35,12), Q(-6), Q(13,3)),
    "I4": (Q(0), Q(-15,4), Q(203,12), Q(-27), Q(43,3)),
    "I5": (Q(0), Q(-7,2), Q(91,6), Q(-26), Q(46,3)),
    "I6": (Q(0), Q(-6), Q(70,3), Q(-28), Q(32,3)),
}


def paired_coefficients(invariants: dict[str, BPoly]) -> list[BPoly]:
    coefficients = [{} for _ in range(5)]
    for name, weights in PAIR_WEIGHTS.items():
        for degree in range(1,5):
            coefficients[degree] = bp_add(
                coefficients[degree], bp_scale(weights[degree], invariants[name])
            )
    return coefficients


def moment_of_products(*powers: int) -> BPoly:
    return dict(activation_atom(tuple(powers) + (0,)*(6-len(powers))))


def cubic_J() -> BPoly:
    # The exact L=2 nine-moment formula, evaluated for psi=a*x+b*x^2.
    d = moment_of_products(0,2)
    e = moment_of_products(0,4)
    m = moment_of_products(1,2,1)
    j = moment_of_products(0,3,0,1)
    ss = moment_of_products(0,2,2)
    ell = moment_of_products(2,2)
    bb = moment_of_products(1,0,1)
    rr = moment_of_products(0,1,0,1)
    v = moment_of_products(0,0,2)
    one = {(0,0): Q(1)}
    c = bp_add(one,d)
    beta = bp_add(bb,bp_mul(c,rr))
    delta = bp_add(d,bp_mul(c,v))
    k = bp_add(d,beta,delta)
    S = bp_add(
        bp_scale(3,bp_mul(bp_pow(c,2),m)),
        bp_scale(3,bp_mul(bp_pow(c,3),j)),
        bp_scale(3,bp_mul(bp_mul(d,e),beta)),
        bp_scale(3,bp_mul(bp_mul(d,k),m)),
        bp_scale(3,bp_mul(bp_pow(d,2),j)),
    )
    H = bp_add(
        bp_mul(bp_pow(c,2),e), bp_mul(c,ell),
        bp_scale(2,bp_mul(bp_pow(c,2),m)),
        bp_scale(3,bp_mul(bp_pow(c,3),ss)),
        bp_mul(bp_mul(bp_mul(c,e),d),v),
        bp_scale(2,bp_mul(e,bp_pow(d,2))),
        bp_scale(3,bp_mul(bp_pow(d,2),ss)),
        bp_mul(bp_pow(k,2),ell),
        bp_scale(2,bp_mul(bp_mul(d,k),m)),
    )
    return bp_add(S,bp_scale(4,H))


def main() -> None:
    invariants = exact_contractions()
    beta = paired_coefficients(invariants)
    J = cubic_J()
    print("normalized activation: psi=(a*x+b*x^2)/sqrt(D), D=a^2+3*b^2")
    print("\nCubic activation invariant J:")
    num, K = normalized_numerator(J)
    print(f"J = ({fmt_poly(num)}) / D^{K}")
    print("\nPaired fifth coefficient beta_t=sum_{r=1}^4 c_r t^r:")
    for degree in range(1,5):
        num, K = normalized_numerator(beta[degree])
        print(f"c{degree} = ({fmt_poly(num)}) / D^{K}")
    # Exact identity checks.
    def at_identity(poly):
        return poly.get((0,0),Q(0)) + sum(
            coefficient for (i,j),coefficient in poly.items() if i and not j
        )
    identity = [sum(c for (i,j),c in beta[d].items() if j == 0) for d in range(1,5)]
    expected = [Q(-369), Q(4403,3), Q(-1896), Q(2452,3)]
    if identity != expected:
        raise AssertionError((identity, expected))
    j_identity = sum(c for (i,j),c in J.items() if j == 0)
    if j_identity != 48:
        raise AssertionError((j_identity, 48))
    print("\nidentity gates: PASS")


if __name__ == "__main__":
    main()
