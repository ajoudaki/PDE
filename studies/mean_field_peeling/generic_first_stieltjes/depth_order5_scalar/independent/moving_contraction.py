"""Independent deterministic contraction of the moving-gradient sectors.

This module continues the frozen-line contraction without importing either
depth-order-five producer.  It uses four chronological scalar passes:

1. moving feature derivative two;
2. moving gradient derivative two;
3. moving feature derivative three;
4. moving gradient derivative three.

Together with ``forward_contraction`` and ``reverse_contraction`` these
passes evaluate the compact exact identity

    D^5 f = 2 S5 + 10 <A,C> + 10 <B,m2>
             + 4 <m2,m2> + 12 <A,m3>.

All local Gaussian variables below are derivation-only.  ``emit`` removes
them completely and freezes literal M-only scalar transition tables.
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

try:
    from .forward_contraction import (
        SMonomial, SPoly, format_poly, moment, sa, sc, serialise,
        sm, sproduct, ss, sv,
    )
except ImportError:
    from forward_contraction import (
        SMonomial, SPoly, format_poly, moment, sa, sc, serialise,
        sm, sproduct, ss, sv,
    )


@dataclass(frozen=True, order=True)
class RMonomial:
    activation: tuple[int, ...]
    forward: tuple[int, ...]  # F1,F2(frozen),F2(moving),F3(moving)
    reverse: tuple[int, ...]  # E0,E1,E2(frozen),E2(moving),E3(moving)


RPoly = dict[RMonomial, SPoly]
RZERO = RMonomial((0,) * 6, (0,) * 4, (0,) * 5)


def rc(value: int | Fraction) -> RPoly:
    coefficient = sc(value)
    return {} if not coefficient else {RZERO: coefficient}


def r_from_scalar(value: Mapping[SMonomial, Fraction]) -> RPoly:
    return {} if not value else {RZERO: dict(value)}


def rg(kind: str, index: int) -> RPoly:
    activation = [0] * 6
    forward = [0] * 4
    reverse = [0] * 5
    if kind == "p":
        activation[index] = 1
    elif kind == "f":
        forward[index - 1] = 1
    elif kind == "e":
        reverse[index] = 1
    else:
        raise ValueError(kind)
    return {RMonomial(tuple(activation), tuple(forward), tuple(reverse)): sc(1)}


def ra(*values: Mapping[RMonomial, SPoly]) -> RPoly:
    out: dict[RMonomial, SPoly] = {}
    for value in values:
        for monomial, coefficient in value.items():
            out[monomial] = sa(out.get(monomial, {}), coefficient)
            if not out[monomial]:
                del out[monomial]
    return out


def rs(value: Mapping[RMonomial, SPoly], factor: int | Fraction) -> RPoly:
    return {
        monomial: scaled
        for monomial, coefficient in value.items()
        if (scaled := ss(coefficient, factor))
    }


def rm(left: Mapping[RMonomial, SPoly], right: Mapping[RMonomial, SPoly]) -> RPoly:
    out: dict[RMonomial, SPoly] = {}
    for lm, lc in left.items():
        for rm_, rc_ in right.items():
            target = RMonomial(
                tuple(a + b for a, b in zip(lm.activation, rm_.activation)),
                tuple(a + b for a, b in zip(lm.forward, rm_.forward)),
                tuple(a + b for a, b in zip(lm.reverse, rm_.reverse)),
            )
            out[target] = sa(out.get(target, {}), sm(lc, rc_))
            if not out[target]:
                del out[target]
    return out


def rproduct(*values: Mapping[RMonomial, SPoly]) -> RPoly:
    out = rc(1)
    for value in values:
        out = rm(out, value)
    return out


def r_derivative(value: Mapping[RMonomial, SPoly], kind: str, index: int) -> RPoly:
    out: dict[RMonomial, SPoly] = {}
    for monomial, coefficient in value.items():
        if kind == "f":
            count = monomial.forward[index - 1]
            if not count:
                continue
            forward = list(monomial.forward)
            forward[index - 1] -= 1
            target = RMonomial(monomial.activation, tuple(forward), monomial.reverse)
            out[target] = sa(out.get(target, {}), ss(coefficient, count))
        elif kind == "e":
            count = monomial.reverse[index]
            if not count:
                continue
            reverse = list(monomial.reverse)
            reverse[index] -= 1
            target = RMonomial(monomial.activation, monomial.forward, tuple(reverse))
            out[target] = sa(out.get(target, {}), ss(coefficient, count))
        elif kind == "f0":
            for derivative, count in enumerate(monomial.activation):
                if not count:
                    continue
                if derivative == 5:
                    raise RuntimeError("phi^(6) generated")
                activation = list(monomial.activation)
                activation[derivative] -= 1
                activation[derivative + 1] += 1
                target = RMonomial(tuple(activation), monomial.forward, monomial.reverse)
                out[target] = sa(out.get(target, {}), ss(coefficient, count))
        else:
            raise ValueError((kind, index))
    return out


# Frozen forward inputs.
U, W, Y = (sv(name) for name in ("u", "w", "y"))
L1 = sv("l1")

# Frozen reverse inputs.
B = sv("b")
E02, E11, E22 = (sv(name) for name in ("e02", "e11", "e22"))
C10, C21 = sv("c10"), sv("c21")

# Moving feature-2 inputs.
Q02, Q22, QFM, A2 = (sv(name) for name in ("q02", "q22", "qfm", "a2"))
L2 = sv("l2")

# Moving reverse-2 inputs.
R02, R22, RFM, D21 = (sv(name) for name in ("r02", "r22", "rfm", "d21"))

# Moving feature-3 inputs.
Q13, A30, A32 = (sv(name) for name in ("q13", "a30", "a32"))
L30, L32 = sv("l30"), sv("l32")

# Moving reverse-3 inputs.
R13, D30, D32 = (sv(name) for name in ("r13", "d30", "d32"))


def forward_covariance(i: int, j: int) -> SPoly:
    if i == 0 and j == 0:
        return sc(1)
    if i > j:
        i, j = j, i
    table: dict[tuple[int, int], SPoly] = {
        (0, 2): U,
        (0, 3): Q02,
        (1, 1): W,
        (1, 4): Q13,
        (2, 2): Y,
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
            raise RuntimeError("phi^(6) generated by Wick--Stein")
        target = list(counts)
        target[derivative] -= 1
        target[derivative + 1] += 1
        yield count, tuple(target)


@lru_cache(maxsize=None)
def wick_stein(monomial: RMonomial) -> SPoly:
    first_reverse = next((i for i, power in enumerate(monomial.reverse) if power), None)
    if first_reverse is not None:
        reverse = list(monomial.reverse)
        reverse[first_reverse] -= 1
        answer: SPoly = {}
        for other in range(first_reverse, 5):
            count = reverse[other]
            cov = reverse_covariance(first_reverse, other)
            if not count or not cov:
                continue
            paired = list(reverse)
            paired[other] -= 1
            target = RMonomial(monomial.activation, monomial.forward, tuple(paired))
            answer = sa(answer, sproduct(sc(count), cov, wick_stein(target)))
        return answer

    first_forward = next((i + 1 for i, power in enumerate(monomial.forward) if power), None)
    if first_forward is None:
        return moment(monomial.activation)
    forward = list(monomial.forward)
    forward[first_forward - 1] -= 1
    answer = {}
    for other in range(first_forward, 5):
        count = forward[other - 1]
        cov = forward_covariance(first_forward, other)
        if not count or not cov:
            continue
        paired = list(forward)
        paired[other - 1] -= 1
        target = RMonomial(monomial.activation, tuple(paired), monomial.reverse)
        answer = sa(answer, sproduct(sc(count), cov, wick_stein(target)))
    cov0 = forward_covariance(first_forward, 0)
    if cov0:
        for count, activation in activation_derivative(monomial.activation):
            target = RMonomial(activation, tuple(forward), monomial.reverse)
            answer = sa(answer, sproduct(sc(count), cov0, wick_stein(target)))
    return answer


def expectation(value: Mapping[RMonomial, SPoly]) -> SPoly:
    answer: SPoly = {}
    for monomial, coefficient in value.items():
        answer = sa(answer, sm(coefficient, wick_stein(monomial)))
    return answer


def local_polynomials() -> dict[str, RPoly]:
    p = [rg("p", i) for i in range(6)]
    f1, f2, g2, g3 = (rg("f", i) for i in range(1, 5))
    e0, e1, e2, j2, j3 = (rg("e", i) for i in range(5))

    d0 = rm(p[1], e0)
    z1 = ra(f1, rm(r_from_scalar(L1), d0))
    x0 = p[0]
    x1 = rm(p[1], z1)
    x2 = ra(rproduct(p[2], z1, z1), rm(p[1], f2))

    r1 = ra(e1, rm(r_from_scalar(C10), x0))
    d1 = ra(rproduct(p[2], z1, e0), rm(p[1], r1))

    z2 = ra(g2, rm(r_from_scalar(L2), d1))
    h2 = ra(rproduct(p[2], z1, z1), rm(p[1], z2))

    r2f = ra(e2, rm(r_from_scalar(C21), x1))
    d2f = ra(
        rproduct(p[3], z1, z1, e0), rproduct(p[2], f2, e0),
        rs(rproduct(p[2], z1, r1), 2), rm(p[1], r2f),
    )

    r2m = ra(j2, rm(r_from_scalar(D21), x1))
    d2m = ra(
        rproduct(p[3], z1, z1, e0), rproduct(p[2], z2, e0),
        rs(rproduct(p[2], z1, r1), 2), rm(p[1], r2m),
    )

    z3 = ra(g3, rm(r_from_scalar(L30), d0), rm(r_from_scalar(L32), d2m))
    h3 = ra(
        rproduct(p[3], z1, z1, z1),
        rs(rproduct(p[2], z1, z2), 3),
        rm(p[1], z3),
    )

    r3m = ra(j3, rm(r_from_scalar(D30), x0), rm(r_from_scalar(D32), h2))
    d3m = ra(
        rproduct(p[4], z1, z1, z1, e0),
        rs(rproduct(p[3], z1, z2, e0), 3),
        rproduct(p[2], z3, e0),
        rs(rproduct(p[3], z1, z1, r1), 3),
        rs(rproduct(p[2], z2, r1), 3),
        rs(rproduct(p[2], z1, r2m), 3),
        rm(p[1], r3m),
    )
    return {
        "x0": x0, "x1": x1, "x2": x2,
        "d0": d0, "d1": d1, "d2f": d2f,
        "h2": h2, "d2m": d2m, "h3": h3, "d3m": d3m,
    }


def transitions() -> dict[str, dict[str, SPoly]]:
    q = local_polynomials()
    source00 = expectation(rm(q["d0"], q["d0"]))
    source11 = expectation(rm(q["d1"], q["d1"]))
    source02m = expectation(rm(q["d0"], q["d2m"]))
    return {
        "feature2": {
            "q02_next": expectation(rm(q["x0"], q["h2"])),
            "q22_next": expectation(rm(q["h2"], q["h2"])),
            "qfm_next": expectation(rm(q["x2"], q["h2"])),
            "a2_next": expectation(r_derivative(q["h2"], "e", 1)),
        },
        "gradient2": {
            "source02m": source02m,
            "source22m": expectation(rm(q["d2m"], q["d2m"])),
            "sourcefm": expectation(rm(q["d2f"], q["d2m"])),
            "r02_next": source02m,
            "r22_next": expectation(rm(q["d2m"], q["d2m"])),
            "rfm_next": expectation(rm(q["d2f"], q["d2m"])),
            "d21_next": sa(source00, expectation(r_derivative(q["d2m"], "f", 1))),
        },
        "feature3": {
            "q13_next": expectation(rm(q["x1"], q["h3"])),
            "a30_next": expectation(r_derivative(q["h3"], "e", 0)),
            "a32_next": expectation(r_derivative(q["h3"], "e", 3)),
        },
        "gradient3": {
            "source13m": expectation(rm(q["d1"], q["d3m"])),
            "r13_next": expectation(rm(q["d1"], q["d3m"])),
            "d30_next": sa(
                ss(source02m, 4), ss(source11, 3),
                expectation(r_derivative(q["d3m"], "f0", 0)),
            ),
            "d32_next": sa(
                source00, expectation(r_derivative(q["d3m"], "f", 3)),
            ),
        },
    }


def emit(directory: Path | None = None) -> dict[str, object]:
    directory = Path(__file__).resolve().parent if directory is None else directory
    result = transitions()
    payload: dict[str, object] = {
        "contract": "independent four-pass moving-gradient scalar contraction",
        "states": {
            "feature2": ["q02", "q22", "qfm", "a2"],
            "gradient2": ["r02", "r22", "rfm", "d21"],
            "feature3": ["q13", "a30", "a32"],
            "gradient3": ["r13", "d30", "d32"],
        },
        "transition": {
            group: {name: serialise(poly) for name, poly in values.items()}
            for group, values in result.items()
        },
        "formatted": {
            group: {name: format_poly(poly) for name, poly in values.items()}
            for group, values in result.items()
        },
    }
    path = directory / "FROZEN_MOVING_RECURRENCE.json"
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    (directory / "FROZEN_MOVING_RECURRENCE.sha256").write_text(
        digest + "  " + path.name + "\n"
    )
    markdown = directory / "FROZEN_MOVING_TRANSITIONS.md"
    lines = [
        "# Explicit contracted moving-gradient transitions", "",
        "Generated from `moving_contraction.py`. Every right-hand side is a",
        "finite deterministic polynomial in M-atoms and prior scalar states.", "",
    ]
    for group, values in payload["formatted"].items():
        lines.extend((f"# {group}", ""))
        for name, formula in values.items():
            lines.extend((f"## `{name}`", "", "```text", f"{name} = {formula}", "```", ""))
    markdown.write_text("\n".join(lines))
    markdown_digest = hashlib.sha256(markdown.read_bytes()).hexdigest()
    (directory / "FROZEN_MOVING_TRANSITIONS.sha256").write_text(
        markdown_digest + "  " + markdown.name + "\n"
    )
    return {
        "path": str(path), "sha256": digest,
        "markdown": str(markdown), "markdown_sha256": markdown_digest,
        "payload": payload,
    }


if __name__ == "__main__":
    result = emit()
    print(result["path"])
    print(result["sha256"])
    for group, values in result["payload"]["formatted"].items():
        print("[", group, "]")
        for name, formula in values.items():
            print(name, "=", formula)
