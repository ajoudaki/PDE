"""Independent local Wick--Stein contraction for the moving ``Gamma_04`` head.

This file was written and frozen before any competing ``Gamma_04`` formula
was inspected.  It imports only the scalar-polynomial alphabet used by the
already frozen feature-ascent backbone.  The local Gaussian variables in this
source are derivation scaffolding: :func:`emit` removes all of them and writes
three literal M-only transition polynomials.

The three head states are ordinary-derivative quantities

    gamma04 = E[X_0 X_4],
    a41     = E[d X_4 / d E_1],
    a43     = E[d X_4 / d J_3].

No claim of dimension minimality is made.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from pathlib import Path
from typing import Mapping

from ...depth_order5_scalar.independent.forward_contraction import (
    SMonomial,
    SPoly,
    format_poly,
    moment,
    sa,
    sc,
    serialise,
    sm,
    sproduct,
    ss,
    sv,
)


@dataclass(frozen=True, order=True)
class LocalMonomial:
    activation: tuple[int, ...]
    forward: tuple[int, ...]  # F1,F2(frozen),F2,F3,F4(moving)
    reverse: tuple[int, ...]  # E0,E1,E2(frozen),E2,E3(moving)


LocalPoly = dict[LocalMonomial, SPoly]
ZERO = LocalMonomial((0,) * 6, (0,) * 5, (0,) * 5)


def lc(value: int | Fraction) -> LocalPoly:
    coefficient = sc(value)
    return {} if not coefficient else {ZERO: coefficient}


def lscalar(value: Mapping[SMonomial, Fraction]) -> LocalPoly:
    return {} if not value else {ZERO: dict(value)}


def lg(kind: str, index: int) -> LocalPoly:
    activation = [0] * 6
    forward = [0] * 5
    reverse = [0] * 5
    if kind == "p":
        activation[index] = 1
    elif kind == "f":
        forward[index - 1] = 1
    elif kind == "e":
        reverse[index] = 1
    else:
        raise ValueError(kind)
    return {
        LocalMonomial(tuple(activation), tuple(forward), tuple(reverse)): sc(1)
    }


def la(*values: Mapping[LocalMonomial, SPoly]) -> LocalPoly:
    out: dict[LocalMonomial, SPoly] = {}
    for value in values:
        for monomial, coefficient in value.items():
            out[monomial] = sa(out.get(monomial, {}), coefficient)
            if not out[monomial]:
                del out[monomial]
    return out


def ls(value: Mapping[LocalMonomial, SPoly], factor: int | Fraction) -> LocalPoly:
    return {
        monomial: scaled
        for monomial, coefficient in value.items()
        if (scaled := ss(coefficient, factor))
    }


def lm(
    left: Mapping[LocalMonomial, SPoly],
    right: Mapping[LocalMonomial, SPoly],
) -> LocalPoly:
    out: dict[LocalMonomial, SPoly] = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            target = LocalMonomial(
                tuple(
                    x + y
                    for x, y in zip(
                        left_monomial.activation, right_monomial.activation
                    )
                ),
                tuple(
                    x + y
                    for x, y in zip(left_monomial.forward, right_monomial.forward)
                ),
                tuple(
                    x + y
                    for x, y in zip(left_monomial.reverse, right_monomial.reverse)
                ),
            )
            out[target] = sa(
                out.get(target, {}), sm(left_coefficient, right_coefficient)
            )
            if not out[target]:
                del out[target]
    return out


def lproduct(*values: Mapping[LocalMonomial, SPoly]) -> LocalPoly:
    out = lc(1)
    for value in values:
        out = lm(out, value)
    return out


def lpower(value: Mapping[LocalMonomial, SPoly], power: int) -> LocalPoly:
    out = lc(1)
    for _ in range(power):
        out = lm(out, value)
    return out


def lderivative(
    value: Mapping[LocalMonomial, SPoly], kind: str, index: int
) -> LocalPoly:
    out: dict[LocalMonomial, SPoly] = {}
    for monomial, coefficient in value.items():
        if kind != "e":
            raise ValueError(kind)
        count = monomial.reverse[index]
        if not count:
            continue
        reverse = list(monomial.reverse)
        reverse[index] -= 1
        target = LocalMonomial(monomial.activation, monomial.forward, tuple(reverse))
        out[target] = sa(out.get(target, {}), ss(coefficient, count))
    return out


# Frozen backbone scalar inputs at the lower layer / current reverse layer.
U, W = (sv(name) for name in ("u", "w"))
Q02, Q22, QFM = (sv(name) for name in ("q02", "q22", "qfm"))
Q13, Q04 = (sv(name) for name in ("q13", "gamma04"))
B = sv("b")
E02, E11, E22 = (sv(name) for name in ("e02", "e11", "e22"))
C10, C21 = sv("c10"), sv("c21")
R02, R22, RFM, D21 = (sv(name) for name in ("r02", "r22", "rfm", "d21"))
R13, D30, D32 = (sv(name) for name in ("r13", "d30", "d32"))

L1, L2 = sv("l1"), sv("l2")
L30, L32 = sv("l30"), sv("l32")
L41, L43 = sv("l41"), sv("l43")


def forward_covariance(i: int, j: int) -> SPoly:
    if i == 0 and j == 0:
        return sc(1)
    if i > j:
        i, j = j, i
    table: dict[tuple[int, int], SPoly] = {
        (0, 2): U,
        (0, 3): Q02,
        (0, 5): Q04,
        (1, 1): W,
        (1, 4): Q13,
        (2, 2): sv("y"),
        (2, 3): QFM,
        (3, 3): Q22,
    }
    return table.get((i, j), {})


def reverse_covariance(i: int, j: int) -> SPoly:
    if i > j:
        i, j = j, i
    table: dict[tuple[int, int], SPoly] = {
        (0, 0): B,
        (0, 2): E02,
        (0, 3): R02,
        (1, 1): E11,
        (1, 4): R13,
        (2, 2): E22,
        (2, 3): RFM,
        (3, 3): R22,
    }
    return table.get((i, j), {})


def activation_derivative(counts: tuple[int, ...]):
    for derivative, count in enumerate(counts):
        if not count:
            continue
        if derivative == 5:
            raise RuntimeError("phi^(6) generated by Gamma_04 Wick--Stein")
        target = list(counts)
        target[derivative] -= 1
        target[derivative + 1] += 1
        yield count, tuple(target)


@lru_cache(maxsize=None)
def wick_stein(monomial: LocalMonomial) -> SPoly:
    """Eliminate all reverse Gaussians by Wick, then all forward by Stein."""

    first_reverse = next(
        (i for i, power in enumerate(monomial.reverse) if power), None
    )
    if first_reverse is not None:
        reverse = list(monomial.reverse)
        reverse[first_reverse] -= 1
        answer: SPoly = {}
        for other in range(first_reverse, len(reverse)):
            count = reverse[other]
            covariance = reverse_covariance(first_reverse, other)
            if not count or not covariance:
                continue
            paired = list(reverse)
            paired[other] -= 1
            target = LocalMonomial(
                monomial.activation, monomial.forward, tuple(paired)
            )
            answer = sa(
                answer,
                sproduct(sc(count), covariance, wick_stein(target)),
            )
        return answer

    first_forward = next(
        (i + 1 for i, power in enumerate(monomial.forward) if power), None
    )
    if first_forward is None:
        return moment(monomial.activation)

    forward = list(monomial.forward)
    forward[first_forward - 1] -= 1
    answer: SPoly = {}
    for other in range(first_forward, len(forward) + 1):
        count = forward[other - 1]
        covariance = forward_covariance(first_forward, other)
        if not count or not covariance:
            continue
        paired = list(forward)
        paired[other - 1] -= 1
        target = LocalMonomial(monomial.activation, tuple(paired), monomial.reverse)
        answer = sa(
            answer,
            sproduct(sc(count), covariance, wick_stein(target)),
        )

    covariance0 = forward_covariance(first_forward, 0)
    if covariance0:
        for count, activation in activation_derivative(monomial.activation):
            target = LocalMonomial(activation, tuple(forward), monomial.reverse)
            answer = sa(
                answer,
                sproduct(sc(count), covariance0, wick_stein(target)),
            )
    return answer


def expectation(value: Mapping[LocalMonomial, SPoly]) -> SPoly:
    answer: SPoly = {}
    for monomial, coefficient in value.items():
        answer = sa(answer, sm(coefficient, wick_stein(monomial)))
    return answer


def local_polynomials() -> dict[str, LocalPoly]:
    """Return the complete ordinary-derivative local feature skeleton."""

    p = [lg("p", i) for i in range(6)]
    f1, f2, g2, g3, g4 = (lg("f", i) for i in range(1, 6))
    e0, e1, e2, j2, j3 = (lg("e", i) for i in range(5))

    d0 = lm(p[1], e0)
    z1 = la(f1, lm(lscalar(L1), d0))
    x0 = p[0]
    x1 = lm(p[1], z1)
    x2 = la(lproduct(p[2], z1, z1), lm(p[1], f2))

    r1 = la(e1, lm(lscalar(C10), x0))
    d1 = la(lproduct(p[2], z1, e0), lm(p[1], r1))

    z2 = la(g2, lm(lscalar(L2), d1))
    h2 = la(lproduct(p[2], z1, z1), lm(p[1], z2))

    r2f = la(e2, lm(lscalar(C21), x1))
    d2f = la(
        lproduct(p[3], z1, z1, e0),
        lproduct(p[2], f2, e0),
        ls(lproduct(p[2], z1, r1), 2),
        lm(p[1], r2f),
    )

    r2m = la(j2, lm(lscalar(D21), x1))
    d2m = la(
        lproduct(p[3], z1, z1, e0),
        lproduct(p[2], z2, e0),
        ls(lproduct(p[2], z1, r1), 2),
        lm(p[1], r2m),
    )

    z3 = la(g3, lm(lscalar(L30), d0), lm(lscalar(L32), d2m))
    h3 = la(
        lproduct(p[3], z1, z1, z1),
        ls(lproduct(p[2], z1, z2), 3),
        lm(p[1], z3),
    )

    r3m = la(j3, lm(lscalar(D30), x0), lm(lscalar(D32), h2))
    d3m = la(
        lproduct(p[4], z1, z1, z1, e0),
        ls(lproduct(p[3], z1, z2, e0), 3),
        lproduct(p[2], z3, e0),
        ls(lproduct(p[3], z1, z1, r1), 3),
        ls(lproduct(p[2], z2, r1), 3),
        ls(lproduct(p[2], z1, r2m), 3),
        lm(p[1], r3m),
    )

    # Complete fourth ordinary derivative.  The 1,6,3,4,1 coefficients are
    # the five equality partitions of four in Faà di Bruno form.
    z4 = la(g4, lm(lscalar(L41), d1), lm(lscalar(L43), d3m))
    h4 = la(
        lproduct(p[4], z1, z1, z1, z1),
        ls(lproduct(p[3], z1, z1, z2), 6),
        ls(lproduct(p[2], z2, z2), 3),
        ls(lproduct(p[2], z1, z3), 4),
        lm(p[1], z4),
    )

    return {
        "x0": x0,
        "x1": x1,
        "x2": x2,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "d0": d0,
        "d1": d1,
        "d2f": d2f,
        "d2m": d2m,
        "d3m": d3m,
    }


def transitions() -> dict[str, SPoly]:
    local = local_polynomials()
    return {
        "gamma04_next": expectation(lm(local["x0"], local["h4"])),
        "a41_next": expectation(lderivative(local["h4"], "e", 1)),
        "a43_next": expectation(lderivative(local["h4"], "e", 4)),
    }


def local_audit() -> dict[str, object]:
    local = local_polynomials()
    raw_h4_terms = len(local["h4"])
    raw_partition_coefficients: dict[str, int] = defaultdict(int)
    # The explicit identity is deliberately recorded independently of the
    # contracted output so a later edit cannot silently drop a family.
    for name, coefficient in (
        ("phi4_z1^4", 1),
        ("phi3_z1^2_z2", 6),
        ("phi2_z2^2", 3),
        ("phi2_z1_z3", 4),
        ("phi1_z4", 1),
    ):
        raw_partition_coefficients[name] = coefficient
    contracted = transitions()
    # ``SPoly`` keys contain only terminal scalar symbol names.  The local
    # Gaussian exponents live in ``LocalMonomial`` and cannot be represented
    # in this terminal type at all.
    forbidden_prefixes = ("F", "R", "E", "J")
    residual_local_monomials = {
        name: sum(
            1
            for monomial in polynomial
            if any(symbol.startswith(forbidden_prefixes) for symbol in monomial)
        )
        for name, polynomial in contracted.items()
    }
    maximum_derivative = 0
    for polynomial in contracted.values():
        for monomial in polynomial:
            for atom_name in monomial:
                if atom_name.startswith("M"):
                    digits = atom_name[1:]
                    for derivative, count in enumerate(digits):
                        if count != "0":
                            maximum_derivative = max(maximum_derivative, derivative)
    return {
        "raw_h4_local_monomials": raw_h4_terms,
        "equality_partition_coefficients": dict(raw_partition_coefficients),
        "contracted_term_counts": {
            name: len(polynomial) for name, polynomial in contracted.items()
        },
        "residual_local_gaussian_monomials": residual_local_monomials,
        "maximum_activation_derivative": maximum_derivative,
    }


def emit(directory: Path | None = None) -> dict[str, object]:
    directory = Path(__file__).resolve().parent if directory is None else directory
    result = transitions()
    payload: dict[str, object] = {
        "contract": "independent one-pass moving Gamma_04 scalar head",
        "state": ["gamma04", "a41", "a43"],
        "initialization": {"gamma04": 0, "a41": 0, "a43": 0},
        "derived_abbreviations": {
            "l41": "9*q02 + 8*w + a41",
            "l43": "1 + a43",
        },
        "transition": {
            name: serialise(polynomial) for name, polynomial in result.items()
        },
        "formatted": {
            name: format_poly(polynomial) for name, polynomial in result.items()
        },
        "local_audit": local_audit(),
    }
    path = directory / "FROZEN_GAMMA04_RECURRENCE.json"
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    formula_path = directory / "FROZEN_GAMMA04_TRANSITIONS.md"
    lines = [
        "# Frozen independent `Gamma_04` transitions",
        "",
        "Every right-hand side is a literal deterministic polynomial in",
        "one-dimensional `M` atoms and prior scalar states.",
        "",
    ]
    for name, formula in payload["formatted"].items():
        lines.extend((f"## `{name}`", "", "```text", f"{name} = {formula}", "```", ""))
    formula_path.write_text("\n".join(lines))
    formula_digest = hashlib.sha256(formula_path.read_bytes()).hexdigest()
    return {
        "path": str(path),
        "sha256": digest,
        "formula_path": str(formula_path),
        "formula_sha256": formula_digest,
        "payload": payload,
    }


if __name__ == "__main__":
    emitted = emit()
    print(emitted["path"])
    print(emitted["sha256"])
    print(emitted["formula_path"])
    print(emitted["formula_sha256"])
    print(json.dumps(emitted["payload"]["local_audit"], indent=2, sort_keys=True))
