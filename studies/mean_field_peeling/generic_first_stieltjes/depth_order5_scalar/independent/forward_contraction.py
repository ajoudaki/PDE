"""Independent analytic contraction of the frozen order-five forward jet.

This file deliberately contains no import from either depth-order-five
population compiler.  It starts from the literal frozen-line product and
chain rules and eliminates the local Gaussian coordinates by the elementary
one-coordinate Wick--Stein identity.  Its output is a seven-scalar,
unit-forward-Gram recurrence for the straight fifth directional derivative.

The recurrence is only one (important) sector of ``D^5 f``.  The companion
note ``ANALYTIC_ROUTE.md`` explains why it is not promoted to a recurrence
for the complete coefficient before the mixed Hessian sectors are closed.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from pathlib import Path
from typing import Iterable, Mapping


# ---------------------------------------------------------------------------
# Sparse deterministic commutative polynomials.
# ---------------------------------------------------------------------------

SMonomial = tuple[str, ...]
SPoly = dict[SMonomial, Fraction]


def sc(value: int | Fraction) -> SPoly:
    value = Fraction(value)
    return {} if not value else {(): value}


def sv(name: str) -> SPoly:
    return {(name,): Fraction(1)}


def sa(*values: Mapping[SMonomial, Fraction]) -> SPoly:
    out: defaultdict[SMonomial, Fraction] = defaultdict(Fraction)
    for value in values:
        for monomial, coefficient in value.items():
            out[monomial] += coefficient
    return {m: c for m, c in out.items() if c}


def ss(value: Mapping[SMonomial, Fraction], factor: int | Fraction) -> SPoly:
    factor = Fraction(factor)
    return {} if not factor else {m: factor * c for m, c in value.items() if c}


def sm(left: Mapping[SMonomial, Fraction], right: Mapping[SMonomial, Fraction]) -> SPoly:
    if not left or not right:
        return {}
    out: defaultdict[SMonomial, Fraction] = defaultdict(Fraction)
    for lm, lc in left.items():
        for rm, rc in right.items():
            out[tuple(sorted(lm + rm))] += lc * rc
    return {m: c for m, c in out.items() if c}


def sp(value: Mapping[SMonomial, Fraction], exponent: int) -> SPoly:
    if exponent < 0:
        raise ValueError("negative exponent")
    out = sc(1)
    base = dict(value)
    power = exponent
    while power:
        if power & 1:
            out = sm(out, base)
        power //= 2
        if power:
            base = sm(base, base)
    return out


def sproduct(*values: Mapping[SMonomial, Fraction]) -> SPoly:
    out = sc(1)
    for value in values:
        out = sm(out, value)
    return out


def atom_name(counts: tuple[int, ...]) -> str:
    if len(counts) != 6:
        raise ValueError(counts)
    if counts == (2, 0, 0, 0, 0, 0):
        return "1"
    return "M" + "".join(str(value) for value in counts)


def moment(counts: tuple[int, ...]) -> SPoly:
    name = atom_name(counts)
    return sc(1) if name == "1" else sv(name)


# ---------------------------------------------------------------------------
# Local random polynomials.  F_0 is the activation argument.  F_1,...,F_4
# and R are the only raw Gaussian coordinates which survive in the seven
# target contractions.
# ---------------------------------------------------------------------------


@dataclass(frozen=True, order=True)
class RMonomial:
    activation: tuple[int, ...]  # powers of phi^(0),...,phi^(5)
    forward: tuple[int, ...]     # powers of F_1,...,F_4
    reverse: int                 # power of R


RPoly = dict[RMonomial, SPoly]
RZERO = RMonomial((0,) * 6, (0,) * 4, 0)


def rc(value: int | Fraction) -> RPoly:
    scalar = sc(value)
    return {} if not scalar else {RZERO: scalar}


def r_from_scalar(value: Mapping[SMonomial, Fraction]) -> RPoly:
    return {} if not value else {RZERO: dict(value)}


def rg(kind: str, index: int = 0) -> RPoly:
    activation = [0] * 6
    forward = [0] * 4
    reverse = 0
    if kind == "p":
        activation[index] = 1
    elif kind == "f":
        if not 1 <= index <= 4:
            raise ValueError(index)
        forward[index - 1] = 1
    elif kind == "r":
        reverse = 1
    else:
        raise ValueError(kind)
    return {
        RMonomial(tuple(activation), tuple(forward), reverse): sc(1)
    }


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
            monomial = RMonomial(
                tuple(a + b for a, b in zip(lm.activation, rm_.activation)),
                tuple(a + b for a, b in zip(lm.forward, rm_.forward)),
                lm.reverse + rm_.reverse,
            )
            out[monomial] = sa(out.get(monomial, {}), sm(lc, rc_))
            if not out[monomial]:
                del out[monomial]
    return out


def rp(value: Mapping[RMonomial, SPoly], exponent: int) -> RPoly:
    if exponent < 0:
        raise ValueError("negative exponent")
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


def r_derivative(value: Mapping[RMonomial, SPoly], kind: str) -> RPoly:
    if kind != "r":
        raise ValueError(kind)
    out: dict[RMonomial, SPoly] = {}
    for monomial, coefficient in value.items():
        if not monomial.reverse:
            continue
        target = RMonomial(
            monomial.activation,
            monomial.forward,
            monomial.reverse - 1,
        )
        out[target] = sa(
            out.get(target, {}), ss(coefficient, monomial.reverse)
        )
    return out


# Covariances of F_1,...,F_4.  Entries not listed vanish by parity.
U, V, W, X, Y, B = (sv(name) for name in ("u", "v", "w", "x", "y", "b"))
L1, L3, L5 = (sv(name) for name in ("l1", "l3", "l5"))


def covariance(i: int, j: int) -> SPoly:
    if i == 0 and j == 0:
        return sc(1)
    if i > j:
        i, j = j, i
    table: dict[tuple[int, int], SPoly] = {
        (0, 2): U,
        (0, 4): V,
        (1, 1): W,
        (1, 3): X,
        (2, 2): Y,
    }
    return table.get((i, j), {})


def activation_derivative(counts: tuple[int, ...]) -> list[tuple[int, tuple[int, ...]]]:
    out: list[tuple[int, tuple[int, ...]]] = []
    for derivative, count in enumerate(counts):
        if not count:
            continue
        if derivative == 5:
            raise RuntimeError("the proposed terminal recurrence generated phi^(6)")
        target = list(counts)
        target[derivative] -= 1
        target[derivative + 1] += 1
        out.append((count, tuple(target)))
    return out


@lru_cache(maxsize=None)
def wick_stein(monomial: RMonomial) -> SPoly:
    """Eliminate R and F_1,...,F_4 exactly, leaving one M atom."""

    if monomial.reverse:
        exponent = monomial.reverse
        if exponent & 1:
            return {}
        coefficient = 1
        for odd in range(1, exponent, 2):
            coefficient *= odd
        target = RMonomial(monomial.activation, monomial.forward, 0)
        return sproduct(sc(coefficient), sp(B, exponent // 2), wick_stein(target))

    first = next((index + 1 for index, power in enumerate(monomial.forward) if power), None)
    if first is None:
        return moment(monomial.activation)

    forward = list(monomial.forward)
    forward[first - 1] -= 1

    answer: SPoly = {}
    for other in range(first, 5):
        count = forward[other - 1]
        cov = covariance(first, other)
        if not count or not cov:
            continue
        paired = list(forward)
        paired[other - 1] -= 1
        target = RMonomial(monomial.activation, tuple(paired), 0)
        answer = sa(answer, sproduct(sc(count), cov, wick_stein(target)))

    cov0 = covariance(first, 0)
    if cov0:
        for count, activation in activation_derivative(monomial.activation):
            target = RMonomial(activation, tuple(forward), 0)
            answer = sa(answer, sproduct(sc(count), cov0, wick_stein(target)))
    return answer


def expectation(value: Mapping[RMonomial, SPoly]) -> SPoly:
    answer: SPoly = {}
    for monomial, coefficient in value.items():
        answer = sa(answer, sm(coefficient, wick_stein(monomial)))
    return answer


# ---------------------------------------------------------------------------
# Literal Bell polynomials and the seven contractions.
# ---------------------------------------------------------------------------


def local_forward_polynomials() -> list[RPoly]:
    p = [rg("p", r) for r in range(6)]
    f = [None] + [rg("f", r) for r in range(1, 5)]
    r = rg("r")
    delta = rm(p[1], r)

    z: list[RPoly] = [rc(0)] * 6
    z[1] = ra(f[1], rm(r_from_scalar(L1), delta))
    z[2] = f[2]
    z[3] = ra(f[3], rm(r_from_scalar(L3), delta))
    z[4] = f[4]
    # X_5 itself contains Z_5, but neither G_04 nor d_R X_5 needs the fresh
    # F_5 term.  Retaining only its R-dependent part is therefore exact for
    # all seven displayed states.
    z[5] = rm(r_from_scalar(L5), delta)

    x: list[RPoly] = [rc(0)] * 6
    x[0] = p[0]
    x[1] = rm(p[1], z[1])
    x[2] = ra(rproduct(p[2], z[1], z[1]), rm(p[1], z[2]))
    x[3] = ra(
        rproduct(p[3], z[1], z[1], z[1]),
        rs(rproduct(p[2], z[1], z[2]), 3),
        rm(p[1], z[3]),
    )
    x[4] = ra(
        rproduct(p[4], z[1], z[1], z[1], z[1]),
        rs(rproduct(p[3], z[1], z[1], z[2]), 6),
        rs(rproduct(p[2], z[2], z[2]), 3),
        rs(rproduct(p[2], z[1], z[3]), 4),
        rm(p[1], z[4]),
    )
    x[5] = ra(
        rproduct(p[5], z[1], z[1], z[1], z[1], z[1]),
        rs(rproduct(p[4], z[1], z[1], z[1], z[2]), 10),
        rs(rproduct(p[3], z[1], z[2], z[2]), 15),
        rs(rproduct(p[3], z[1], z[1], z[3]), 10),
        rs(rproduct(p[2], z[2], z[3]), 10),
        rs(rproduct(p[2], z[1], z[4]), 5),
        rm(p[1], z[5]),
    )
    return x


def transition() -> dict[str, SPoly]:
    x = local_forward_polynomials()
    return {
        "u_next": expectation(rm(x[0], x[2])),
        "v_next": expectation(rm(x[0], x[4])),
        "w_next": expectation(rm(x[1], x[1])),
        "x_next": expectation(rm(x[1], x[3])),
        "y_next": expectation(rm(x[2], x[2])),
        "j_next": expectation(r_derivative(x[3], "r")),
        "k_next": expectation(r_derivative(x[5], "r")),
    }


def _format_monomial(monomial: SMonomial) -> str:
    if not monomial:
        return "1"
    counts: dict[str, int] = {}
    for value in monomial:
        counts[value] = counts.get(value, 0) + 1
    return "*".join(
        name if power == 1 else f"{name}^{power}"
        for name, power in sorted(counts.items())
    )


def format_poly(value: Mapping[SMonomial, Fraction]) -> str:
    pieces: list[str] = []
    for monomial, coefficient in sorted(value.items(), key=lambda item: item[0]):
        body = _format_monomial(monomial)
        if body == "1":
            term = str(abs(coefficient))
        elif abs(coefficient) == 1:
            term = body
        else:
            term = f"{abs(coefficient)}*{body}"
        if not pieces:
            pieces.append(("-" if coefficient < 0 else "") + term)
        else:
            pieces.append((" - " if coefficient < 0 else " + ") + term)
    return "".join(pieces) if pieces else "0"


def serialise(value: Mapping[SMonomial, Fraction]) -> dict[str, str]:
    return {
        "*".join(monomial): (
            str(coefficient.numerator)
            if coefficient.denominator == 1
            else f"{coefficient.numerator}/{coefficient.denominator}"
        )
        for monomial, coefficient in sorted(value.items())
    }


def emit(directory: Path | None = None) -> dict[str, object]:
    directory = Path(__file__).resolve().parent if directory is None else directory
    result = transition()
    payload: dict[str, object] = {
        "contract": "independent frozen-line seven-scalar unit-Gram contraction",
        "state": ["u", "v", "w", "x", "y", "j", "k"],
        "lambdas": {
            "l1": "tau_(ell-1)",
            "l3": "j+3*u",
            "l5": "k+5*v",
        },
        "transition": {name: serialise(value) for name, value in result.items()},
        "formatted": {name: format_poly(value) for name, value in result.items()},
        "terminal": "straight_fifth = k_H + 5*v_H",
        "derivative_ceiling": max(
            max(
                index
                for index, count in enumerate(tuple(int(digit) for digit in name[1:]))
                if count
            )
            for value in result.values()
            for monomial in value
            for name in monomial
            if name.startswith("M")
        ),
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True).encode()
    path = directory / "FROZEN_FORWARD_RECURRENCE.json"
    path.write_bytes(encoded + b"\n")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    (directory / "FROZEN_FORWARD_RECURRENCE.sha256").write_text(
        digest + "  " + path.name + "\n"
    )
    return {"path": str(path), "sha256": digest, "payload": payload}


if __name__ == "__main__":
    emitted = emit()
    print(emitted["path"])
    print(emitted["sha256"])
    for name, formula in emitted["payload"]["formatted"].items():
        print(name, "=", formula)
