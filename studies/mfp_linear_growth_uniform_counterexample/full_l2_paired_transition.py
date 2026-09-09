"""Exact response-aware order-five map for the L=2 paired Euler defect.

This file deliberately reuses only the typed coordinate algebra and the
Wick--Stein peeler from ``generic_first_stieltjes/order5``.  It changes the
curve whose fifth output coefficient is compiled.  For weights

    lam = (lam_0, ..., lam_4),

the formal parameter curve is defined coefficientwise by

    theta_{k+1} = lam_k [h^k] grad f(theta(h)).

The ordinary gradient-flow jet is lam_k=1/(k+1).  Sparse choices of lam
isolate the six fifth-order gradient elementary differentials.  In
particular the fine-minus-coarse two-versus-one Euler coefficient is the
linear combination ``-8 Q0 + 7 Q1 + 3 Q2 + Q3 + 2 Q4`` compiled below.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import importlib.util
import json
import sys


HERE = Path(__file__).resolve().parent
PJ_PATH = (
    HERE.parent
    / "generic_first_stieltjes"
    / "order5"
    / "compiler"
    / "population_jet.py"
)


def _load_population_jet():
    spec = importlib.util.spec_from_file_location("mfp_population_jet", PJ_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load population_jet.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


pj = _load_population_jet()


def compile_weighted_path(
    weights: tuple[Fraction, ...], *, order: int = 5, verbose: bool = False
):
    """Compile [h^5] f(theta(h)) for the coefficient-weighted gradient path.

    This is the exact ``compile_population_jet`` chronology with every
    integration factor 1/(k+1) replaced by the supplied coefficient weight.
    The replacement is made simultaneously in the readout, dense-layer
    rank-one update, and first-layer update.  Consequently all transpose
    responses and reused-matrix covariances remain present.
    """

    if not 0 <= order <= 5 or len(weights) != order:
        raise ValueError("weights must have length order, with 0 <= order <= 5")
    weights = tuple(Fraction(value) for value in weights)
    peeler = pj.Peeler()
    zero = pj.CoordinatePolynomial.zero
    u = [zero() for _ in range(order + 1)]
    h = [zero() for _ in range(order + 1)]
    hp = [zero() for _ in range(order + 1)]
    z = [zero() for _ in range(order + 1)]
    g = [zero() for _ in range(order + 1)]
    yp = [zero() for _ in range(order + 1)]
    a = [zero() for _ in range(order + 1)]
    b = [zero() for _ in range(order + 1)]
    r = [zero() for _ in range(order)]
    output = [pj.MomentPolynomial.zero() for _ in range(order + 1)]
    a[0] = pj.CoordinatePolynomial.variable("A")

    for k in range(order + 1):
        h[k] = pj._activation_coefficient("X", u, k, 0)
        if k < order:
            hp[k] = pj._activation_coefficient("X", u, k, 1)

        for ell in range(k + 1):
            value = peeler.first(h[k] * h[ell])
            peeler.H[k][ell] = value
            peeler.H[ell][k] = value

        if k == 0:
            g[0] = pj.CoordinatePolynomial.variable("Y", 0)
            yp[0] = pj.CoordinatePolynomial.variable("Y", 1)
        else:
            alpha = [peeler.first(h[k].derivative("R", s)) for s in range(k)]
            zk = pj.CoordinatePolynomial.variable("F", k)
            for s in range(k):
                zk = zk + b[s] * alpha[s]
            for m in range(1, k + 1):
                rank_weight = weights[m - 1]
                if not rank_weight:
                    continue
                for left in range(m):
                    right = m - 1 - left
                    gram = peeler.first(h[right] * h[k - m])
                    zk = zk + rank_weight * b[left] * gram
            z[k] = zk
            g[k] = pj._activation_coefficient("Y", z, k, 0)
            if k < order:
                yp[k] = pj._activation_coefficient("Y", z, k, 1)

        outk = zero()
        for left in range(k + 1):
            outk = outk + a[left] * g[k - left]
        output[k] = peeler.second(outk)
        if verbose:
            print("forward", k, len(h[k].terms), len(z[k].terms), len(g[k].terms), len(output[k].terms))
        if k == order:
            break

        a[k + 1] = weights[k] * g[k]
        bk = zero()
        for left in range(k + 1):
            bk = bk + a[left] * yp[k - left]
        b[k] = bk

        for ell in range(k + 1):
            value = peeler.second(b[k] * b[ell])
            peeler.B[k][ell] = value
            peeler.B[ell][k] = value

        beta = [peeler.second(b[k].derivative("F", s)) for s in range(k + 1)]
        rk = pj.CoordinatePolynomial.variable("R", k)
        for s in range(k + 1):
            rk = rk + h[s] * beta[s]
        for m in range(1, k + 1):
            rank_weight = weights[m - 1]
            if not rank_weight:
                continue
            for left in range(m):
                right = m - 1 - left
                gram = peeler.second(b[left] * b[k - m])
                rk = rk + rank_weight * h[right] * gram
        r[k] = rk

        uk1 = zero()
        for left in range(k + 1):
            uk1 = uk1 + hp[left] * r[k - left]
        u[k + 1] = weights[k] * uk1

    return output[order]


PATHS = (
    (Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
    (Fraction(1), Fraction(0), Fraction(1), Fraction(1), Fraction(0)),
    (Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
)
COMBINATION = (Fraction(-8), Fraction(7), Fraction(3), Fraction(1), Fraction(2))


def compile_elementary_maps(*, verbose: bool = False):
    """Compile the six independent order-five elementary differentials.

    The first five are recovered triangularly from ``PATHS``.  For the
    sparse path ``q5=(1,1,1,0,0)``, direct Taylor expansion gives

    ``q5=E1/120+E2/6+E3/4+E4+E5/2+E6``.

    It therefore isolates the sixth source without compiling the much
    denser ordinary-flow path.  This avoids assuming that the t=1 paired
    support, where the sixth weight vanishes, is the support at a general
    horizon.
    """

    paths = [compile_weighted_path(path, verbose=verbose) for path in PATHS]
    q0, q1, q2, q3, q4 = paths
    e1 = 120 * q0
    e2 = 6 * (q1 - q0)
    e3 = 4 * (q2 - q0)
    e4 = 2 * (q3 - q1 - q2 + q0)
    e5 = 2 * (q4 - q1)
    q5 = compile_weighted_path(
        (Fraction(1), Fraction(1), Fraction(1), Fraction(0), Fraction(0)),
        verbose=verbose,
    )
    e6 = q5 - q0 + 2 * q1 + q2 - 2 * q3 - q4
    return tuple(paths), (e1, e2, e3, e4, e5, e6)


def compile_paired_map(*, verbose: bool = False):
    maps = []
    for index, path in enumerate(PATHS):
        if verbose:
            print("path", index, path)
        maps.append(compile_weighted_path(path, verbose=verbose))
    paired = pj.MomentPolynomial.zero()
    for coefficient, expression in zip(COMBINATION, maps):
        paired = paired + coefficient * expression
    return maps, paired


def compile_paired_cubic_map(*, verbose: bool = False):
    """Compile 1/2*T[g,g,g] + 2*||H g||^2 exactly."""

    q0 = compile_weighted_path(
        (Fraction(1), Fraction(0), Fraction(0)), order=3, verbose=verbose
    )
    q1 = compile_weighted_path(
        (Fraction(1), Fraction(1), Fraction(0)), order=3, verbose=verbose
    )
    return q0 + 2 * q1


def atom_record(atom):
    layer, exponent = atom
    return {"layer": layer, "exponent": list(exponent[:6])}


def expression_record(expression):
    return [
        {
            "coefficient": str(coefficient),
            "atoms": [atom_record(atom) for atom in monomial],
        }
        for monomial, coefficient in expression.terms
    ]


def main() -> None:
    maps, paired = compile_paired_map(verbose=True)
    cubic = compile_paired_cubic_map(verbose=True)
    out = {
        "paths": [[str(value) for value in path] for path in PATHS],
        "combination": [str(value) for value in COMBINATION],
        "path_term_counts": [len(expression.terms) for expression in maps],
        "paired_term_count": len(paired.terms),
        "maximum_derivative": paired.maximum_derivative(),
        "paired_map": expression_record(paired),
        "paired_cubic_term_count": len(cubic.terms),
        "paired_cubic_map": expression_record(cubic),
    }
    destination = HERE / "FULL_L2_PAIRED_ORDER5_MAP.json"
    destination.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(destination)
    print(out["path_term_counts"], out["paired_term_count"], out["maximum_derivative"])


if __name__ == "__main__":
    main()
