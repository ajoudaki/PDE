"""Corrected independent Gamma_04 contraction with five forward slots.

Version 1 is intentionally retained as a falsified route: it accidentally
aliased the new fourth-jet innovation with the existing third-jet innovation.
This implementation embeds the frozen lower-order chaos in a genuinely new
five-forward-coordinate algebra.  It imports no Gamma_04 producer transition.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import json

from studies.mean_field_peeling.generic_first_stieltjes.depth_order5_scalar.independent import (
    moving_contraction as base,
)


@dataclass(frozen=True, order=True)
class Monomial:
    activation: tuple[int, ...]
    forward: tuple[int, ...]  # F1,F2-frozen,F2-moving,F3-moving,F4-moving
    reverse: tuple[int, ...]  # E0,E1,E2-frozen,E2-moving,E3-moving


ZERO = Monomial((0,) * 6, (0,) * 5, (0,) * 5)


def constant(value):
    coefficient = base.sc(value)
    return {} if not coefficient else {ZERO: coefficient}


def scalar(value):
    return {} if not value else {ZERO: dict(value)}


def gaussian(kind, index):
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
    return {Monomial(tuple(activation), tuple(forward), tuple(reverse)): base.sc(1)}


def embed(value):
    return {
        Monomial(m.activation, m.forward + (0,), m.reverse): dict(coefficient)
        for m, coefficient in value.items()
    }


def add(*values):
    answer = {}
    for value in values:
        for monomial, coefficient in value.items():
            answer[monomial] = base.sa(answer.get(monomial, {}), coefficient)
            if not answer[monomial]:
                del answer[monomial]
    return answer


def scale(value, factor):
    return {
        monomial: scaled
        for monomial, coefficient in value.items()
        if (scaled := base.ss(coefficient, factor))
    }


def multiply(left, right):
    answer = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            target = Monomial(
                tuple(a + b for a, b in zip(lm.activation, rm.activation)),
                tuple(a + b for a, b in zip(lm.forward, rm.forward)),
                tuple(a + b for a, b in zip(lm.reverse, rm.reverse)),
            )
            answer[target] = base.sa(answer.get(target, {}), base.sm(lc, rc))
            if not answer[target]:
                del answer[target]
    return answer


def product(*values):
    answer = constant(1)
    for value in values:
        answer = multiply(answer, value)
    return answer


def derivative(value, kind, index):
    answer = {}
    for monomial, coefficient in value.items():
        if kind == "e":
            count = monomial.reverse[index]
            if not count:
                continue
            reverse = list(monomial.reverse)
            reverse[index] -= 1
            target = Monomial(monomial.activation, monomial.forward, tuple(reverse))
        else:
            raise ValueError(kind)
        answer[target] = base.sa(answer.get(target, {}), base.ss(coefficient, count))
    return answer


GAMMA04 = base.sv("gamma04")
L41, L43 = base.sv("l41"), base.sv("l43")


def forward_covariance(i, j):
    if i == 0 and j == 0:
        return base.sc(1)
    if i > j:
        i, j = j, i
    table = {
        (0, 2): base.U,
        (0, 3): base.Q02,
        (0, 5): GAMMA04,
        (1, 1): base.W,
        (1, 4): base.Q13,
        (2, 2): base.Y,
        (2, 3): base.QFM,
        (3, 3): base.Q22,
    }
    return table.get((i, j), {})


def reverse_covariance(i, j):
    return base.reverse_covariance(i, j)


@lru_cache(maxsize=None)
def wick(monomial):
    first_reverse = next(
        (i for i, power in enumerate(monomial.reverse) if power), None
    )
    if first_reverse is not None:
        reverse = list(monomial.reverse)
        reverse[first_reverse] -= 1
        answer = {}
        for other in range(first_reverse, 5):
            count = reverse[other]
            covariance = reverse_covariance(first_reverse, other)
            if not count or not covariance:
                continue
            paired = list(reverse)
            paired[other] -= 1
            target = Monomial(monomial.activation, monomial.forward, tuple(paired))
            answer = base.sa(
                answer,
                base.sproduct(base.sc(count), covariance, wick(target)),
            )
        return answer

    first_forward = next(
        (i + 1 for i, power in enumerate(monomial.forward) if power), None
    )
    if first_forward is None:
        return base.moment(monomial.activation)

    forward = list(monomial.forward)
    forward[first_forward - 1] -= 1
    answer = {}
    for other in range(first_forward, 6):
        count = forward[other - 1]
        covariance = forward_covariance(first_forward, other)
        if not count or not covariance:
            continue
        paired = list(forward)
        paired[other - 1] -= 1
        target = Monomial(monomial.activation, tuple(paired), monomial.reverse)
        answer = base.sa(
            answer,
            base.sproduct(base.sc(count), covariance, wick(target)),
        )

    covariance0 = forward_covariance(first_forward, 0)
    if covariance0:
        for derivative_index, count in enumerate(monomial.activation):
            if not count:
                continue
            if derivative_index == 5:
                raise RuntimeError("phi^(6) generated")
            activation = list(monomial.activation)
            activation[derivative_index] -= 1
            activation[derivative_index + 1] += 1
            target = Monomial(tuple(activation), tuple(forward), monomial.reverse)
            answer = base.sa(
                answer,
                base.sproduct(base.sc(count), covariance0, wick(target)),
            )
    return answer


def expectation(value):
    answer = {}
    for monomial, coefficient in value.items():
        answer = base.sa(answer, base.sm(coefficient, wick(monomial)))
    return answer


def transitions():
    lower = {name: embed(value) for name, value in base.local_polynomials().items()}
    p = [gaussian("p", i) for i in range(6)]
    f1, g2, g3, g4 = (gaussian("f", i) for i in (1, 3, 4, 5))
    e0 = gaussian("e", 0)

    d0 = multiply(p[1], e0)
    z1 = add(f1, multiply(scalar(base.L1), d0))
    z2 = add(g2, multiply(scalar(base.L2), lower["d1"]))
    z3 = add(
        g3,
        multiply(scalar(base.L30), d0),
        multiply(scalar(base.L32), lower["d2m"]),
    )
    z4 = add(
        g4,
        multiply(scalar(L41), lower["d1"]),
        multiply(scalar(L43), lower["d3m"]),
    )

    x4 = add(
        product(p[4], z1, z1, z1, z1),
        scale(product(p[3], z1, z1, z2), 6),
        scale(product(p[2], z2, z2), 3),
        scale(product(p[2], z1, z3), 4),
        multiply(p[1], z4),
    )
    return {
        "gamma04_next": expectation(multiply(lower["x0"], x4)),
        "a41_next": expectation(derivative(x4, "e", 1)),
        "a43_next": expectation(derivative(x4, "e", 4)),
    }


def schedule():
    result = transitions()
    return {
        "initial": {"gamma04": "0", "a41": "0", "a43": "0"},
        "substitutions": {
            "l41": "9*q02 + 8*w + a41",
            "l43": "1 + a43",
        },
        "term_counts": {name: len(poly) for name, poly in result.items()},
        "transition": {name: base.format_poly(poly) for name, poly in result.items()},
    }


if __name__ == "__main__":
    print(json.dumps(schedule(), indent=2, sort_keys=True))

