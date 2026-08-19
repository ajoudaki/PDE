"""Independent Wick--Stein contraction of the frozen gradient jet.

Given the seven-scalar forward state from :mod:`forward_contraction`, this
module contracts one top-down layer of the ordinary frozen-line gradient jet
through derivative three.  The ten deterministic reverse scalars are the six
nonzero innovation pairings and four explicit feature coefficients permitted
by parity.  No Gaussian coordinate appears in the emitted transition.

This closes the ``<g_1,g_3>`` and ``<g_2,g_2>`` contractions.  It does not
close the three mixed ``H^2 p`` contractions in the full order-five tensor
identity; see ``ANALYTIC_ROUTE.md``.
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

try:  # package import
    from .forward_contraction import (
        SMonomial,
        SPoly,
        covariance as forward_covariance,
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
except ImportError:  # direct script execution
    from forward_contraction import (
        SMonomial,
        SPoly,
        covariance as forward_covariance,
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
class RMonomial:
    activation: tuple[int, ...]
    forward: tuple[int, ...]  # F_1,F_2,F_3
    reverse: tuple[int, ...]  # E_0,E_1,E_2,E_3


RPoly = dict[RMonomial, SPoly]
RZERO = RMonomial((0,) * 6, (0,) * 3, (0,) * 4)


def rc(value: int | Fraction) -> RPoly:
    coefficient = sc(value)
    return {} if not coefficient else {RZERO: coefficient}


def r_from_scalar(value: Mapping[SMonomial, Fraction]) -> RPoly:
    return {} if not value else {RZERO: dict(value)}


def rg(kind: str, index: int) -> RPoly:
    activation = [0] * 6
    forward = [0] * 3
    reverse = [0] * 4
    if kind == "p":
        activation[index] = 1
    elif kind == "f":
        if not 1 <= index <= 3:
            raise ValueError(index)
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


def rp(value: Mapping[RMonomial, SPoly], exponent: int) -> RPoly:
    out = rc(1)
    base = dict(value)
    power = exponent
    while power:
        if power & 1:
            out = rm(out, base)
        power //= 2
        if power:
            base = rm(base, base)
    return out


def rproduct(*values: Mapping[RMonomial, SPoly]) -> RPoly:
    out = rc(1)
    for value in values:
        out = rm(out, value)
    return out


def r_derivative(value: Mapping[RMonomial, SPoly], index: int) -> RPoly:
    """Syntactic derivative with respect to F_index, including F_0."""

    out: dict[RMonomial, SPoly] = {}
    for monomial, coefficient in value.items():
        if index:
            count = monomial.forward[index - 1]
            if not count:
                continue
            forward = list(monomial.forward)
            forward[index - 1] -= 1
            target = RMonomial(
                monomial.activation, tuple(forward), monomial.reverse
            )
            out[target] = sa(out.get(target, {}), ss(coefficient, count))
        else:
            for derivative, count in enumerate(monomial.activation):
                if not count:
                    continue
                if derivative == 5:
                    raise RuntimeError("phi^(6) generated in reverse contraction")
                activation = list(monomial.activation)
                activation[derivative] -= 1
                activation[derivative + 1] += 1
                target = RMonomial(
                    tuple(activation), monomial.forward, monomial.reverse
                )
                out[target] = sa(out.get(target, {}), ss(coefficient, count))
    return out


# Reverse-state names.  e00 is the known base variance b and is not stored.
# The variance e33 is deliberately absent: neither source13 nor source22 nor
# any response coefficient uses it, so liveness pruning removes it exactly.
E02, E11, E13, E22 = (
    sv(name) for name in ("e02", "e11", "e13", "e22")
)
C10, C21, C30, C32 = (sv(name) for name in ("c10", "c21", "c30", "c32"))
B = sv("b")
L1, L3 = sv("l1"), sv("l3")


def reverse_covariance(i: int, j: int) -> SPoly:
    if i > j:
        i, j = j, i
    table: dict[tuple[int, int], SPoly] = {
        (0, 0): B,
        (0, 2): E02,
        (1, 1): E11,
        (1, 3): E13,
        (2, 2): E22,
    }
    return table.get((i, j), {})


def activation_derivative(
    counts: tuple[int, ...],
) -> list[tuple[int, tuple[int, ...]]]:
    out: list[tuple[int, tuple[int, ...]]] = []
    for derivative, count in enumerate(counts):
        if not count:
            continue
        if derivative == 5:
            raise RuntimeError("phi^(6) generated in reverse Wick--Stein")
        target = list(counts)
        target[derivative] -= 1
        target[derivative + 1] += 1
        out.append((count, tuple(target)))
    return out


@lru_cache(maxsize=None)
def wick_stein(monomial: RMonomial) -> SPoly:
    # Eliminate reverse Gaussians first.  They are independent of F.
    first_reverse = next(
        (index for index, power in enumerate(monomial.reverse) if power), None
    )
    if first_reverse is not None:
        reverse = list(monomial.reverse)
        reverse[first_reverse] -= 1
        answer: SPoly = {}
        for other in range(first_reverse, 4):
            count = reverse[other]
            cov = reverse_covariance(first_reverse, other)
            if not count or not cov:
                continue
            paired = list(reverse)
            paired[other] -= 1
            target = RMonomial(
                monomial.activation, monomial.forward, tuple(paired)
            )
            answer = sa(answer, sproduct(sc(count), cov, wick_stein(target)))
        return answer

    first_forward = next(
        (index + 1 for index, power in enumerate(monomial.forward) if power),
        None,
    )
    if first_forward is None:
        return moment(monomial.activation)

    forward = list(monomial.forward)
    forward[first_forward - 1] -= 1
    answer = {}
    for other in range(first_forward, 4):
        count = forward[other - 1]
        cov = forward_covariance(first_forward, other)
        if not count or not cov:
            continue
        paired = list(forward)
        paired[other - 1] -= 1
        target = RMonomial(
            monomial.activation, tuple(paired), monomial.reverse
        )
        answer = sa(answer, sproduct(sc(count), cov, wick_stein(target)))

    cov0 = forward_covariance(first_forward, 0)
    if cov0:
        for count, activation in activation_derivative(monomial.activation):
            target = RMonomial(
                activation, tuple(forward), monomial.reverse
            )
            answer = sa(answer, sproduct(sc(count), cov0, wick_stein(target)))
    return answer


def expectation(value: Mapping[RMonomial, SPoly]) -> SPoly:
    answer: SPoly = {}
    for monomial, coefficient in value.items():
        answer = sa(answer, sm(coefficient, wick_stein(monomial)))
    return answer


def local_polynomials() -> tuple[list[RPoly], list[RPoly]]:
    p = [rg("p", r) for r in range(6)]
    f = [rc(0)] + [rg("f", r) for r in range(1, 4)]
    e = [rg("e", r) for r in range(4)]

    delta0 = rm(p[1], e[0])
    z = [rc(0)] * 4
    z[1] = ra(f[1], rm(r_from_scalar(L1), delta0))
    z[2] = f[2]
    z[3] = ra(f[3], rm(r_from_scalar(L3), delta0))

    x = [rc(0)] * 3
    x[0] = p[0]
    x[1] = rm(p[1], z[1])
    x[2] = ra(rproduct(p[2], z[1], z[1]), rm(p[1], z[2]))

    r = [rc(0)] * 4
    r[0] = e[0]
    r[1] = ra(e[1], rm(r_from_scalar(C10), x[0]))
    r[2] = ra(e[2], rm(r_from_scalar(C21), x[1]))
    r[3] = ra(
        e[3],
        rm(r_from_scalar(C30), x[0]),
        rm(r_from_scalar(C32), x[2]),
    )

    delta = [rc(0)] * 4
    delta[0] = rm(p[1], r[0])
    delta[1] = ra(rproduct(p[2], z[1], r[0]), rm(p[1], r[1]))
    delta[2] = ra(
        rproduct(p[3], z[1], z[1], r[0]),
        rproduct(p[2], z[2], r[0]),
        rs(rproduct(p[2], z[1], r[1]), 2),
        rm(p[1], r[2]),
    )
    delta[3] = ra(
        rproduct(p[4], z[1], z[1], z[1], r[0]),
        rs(rproduct(p[3], z[1], z[2], r[0]), 3),
        rproduct(p[2], z[3], r[0]),
        rs(rproduct(p[3], z[1], z[1], r[1]), 3),
        rs(rproduct(p[2], z[2], r[1]), 3),
        rs(rproduct(p[2], z[1], r[2]), 3),
        rm(p[1], r[3]),
    )
    return x, delta


def transition() -> dict[str, SPoly]:
    _, delta = local_polynomials()
    c00 = expectation(rm(delta[0], delta[0]))
    c02 = expectation(rm(delta[0], delta[2]))
    result = {
        "e02_next": c02,
        "e11_next": expectation(rm(delta[1], delta[1])),
        "e13_next": expectation(rm(delta[1], delta[3])),
        "e22_next": expectation(rm(delta[2], delta[2])),
        "c10_next": sa(c00, expectation(r_derivative(delta[1], 0))),
        "c21_next": expectation(r_derivative(delta[2], 1)),
        "c30_next": sa(ss(c02, 3), expectation(r_derivative(delta[3], 0))),
        "c32_next": expectation(r_derivative(delta[3], 2)),
        "source00": c00,
        "source02": c02,
        "source11": expectation(rm(delta[1], delta[1])),
        "source13": expectation(rm(delta[1], delta[3])),
        "source22": expectation(rm(delta[2], delta[2])),
    }
    return result


def emit(directory: Path | None = None) -> dict[str, object]:
    directory = Path(__file__).resolve().parent if directory is None else directory
    result = transition()
    payload: dict[str, object] = {
        "contract": "independent frozen-gradient ten-scalar unit-Gram contraction",
        "stored_state": [
            "e02", "e11", "e13", "e22",
            "c10", "c21", "c30", "c32",
        ],
        "known_state": ["e00=b"],
        "top_initialization": {
            "e02": "0", "e11": "0", "e13": "0", "e22": "0",
            "c10": "1", "c21": "0", "c30": "0", "c32": "0",
        },
        "transition": {name: serialise(value) for name, value in result.items()},
        "formatted": {name: format_poly(value) for name, value in result.items()},
    }
    path = directory / "FROZEN_REVERSE_RECURRENCE.json"
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    (directory / "FROZEN_REVERSE_RECURRENCE.sha256").write_text(
        digest + "  " + path.name + "\n"
    )
    markdown = directory / "FROZEN_REVERSE_TRANSITIONS.md"
    lines = [
        "# Explicit contracted reverse transition",
        "",
        "This appendix is generated from `reverse_contraction.py`.  Every",
        "right-hand side is a finite commutative polynomial; `*` is scalar",
        "multiplication and `^` is an ordinary nonnegative integer power.",
        "",
    ]
    for name, formula in payload["formatted"].items():
        lines.extend((f"## `{name}`", "", "```text", f"{name} = {formula}", "```", ""))
    markdown.write_text("\n".join(lines))
    markdown_digest = hashlib.sha256(markdown.read_bytes()).hexdigest()
    (directory / "FROZEN_REVERSE_TRANSITIONS.sha256").write_text(
        markdown_digest + "  " + markdown.name + "\n"
    )
    return {
        "path": str(path),
        "sha256": digest,
        "markdown": str(markdown),
        "markdown_sha256": markdown_digest,
        "payload": payload,
    }


if __name__ == "__main__":
    emitted = emit()
    print(emitted["path"])
    print(emitted["sha256"])
    for name, value in emitted["payload"]["formatted"].items():
        print(name, "=", value)
