"""Numerical/exact evaluator for the independently frozen Gamma_04 head.

The evaluator is deliberately separate from the symbolic contraction.  It
loads the universal backbone transition producers and attaches the frozen
three-state observable head after R3.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import exp, pi, sqrt
from typing import Callable, Iterable, Mapping

import numpy as np
from numpy.polynomial.hermite import hermgauss

from ...audit.exact_controls import activation_atom
from ...independent import forward_contraction as fw
from ...independent import moving_contraction as mv
from ...independent import reverse_contraction as rv
from . import gamma04_contraction as g4


Number = Fraction | float
Moment = Callable[[str], Number]


def evaluate(
    polynomial: Mapping[fw.SMonomial, Fraction],
    values: Mapping[str, Number],
    moment: Moment,
) -> Number:
    answer: Number = Fraction(0)
    for monomial, coefficient in polynomial.items():
        term: Number = coefficient
        for name in monomial:
            term *= moment(name) if name.startswith("M") else values[name]
        answer += term
    return answer


def polynomial_moment(activation: Iterable[int | Fraction]) -> Moment:
    activation = tuple(Fraction(value) for value in activation)

    @lru_cache(maxsize=None)
    def value(name: str) -> Fraction:
        return activation_atom("M_" + name.removeprefix("M"), activation)

    return value


def normalized_sine_moment(quadrature_order: int = 96) -> Moment:
    nodes, weights = hermgauss(quadrature_order)
    gaussian = sqrt(2.0) * nodes
    weights = weights / sqrt(pi)
    normalization = sqrt((1.0 - exp(-2.0)) / 2.0)

    @lru_cache(maxsize=None)
    def value(name: str) -> float:
        encoded = name.removeprefix("M")
        integrand = np.ones_like(gaussian)
        for derivative, multiplicity_text in enumerate(encoded):
            multiplicity = int(multiplicity_text)
            if multiplicity:
                derivative_value = (
                    np.sin(gaussian + derivative * pi / 2.0)
                    / normalization
                )
                integrand *= derivative_value**multiplicity
        return float(weights @ integrand)

    return value


def _zeros(names: tuple[str, ...]) -> dict[str, Number]:
    return {name: Fraction(0) for name in names}


def compile_numeric(hidden_layers: int, moment: Moment) -> dict[str, object]:
    if hidden_layers < 1:
        raise ValueError("hidden_layers must be positive")
    h = hidden_layers
    d = moment("M020000")
    tau: list[Number] = [Fraction(1)]
    for _ in range(h):
        tau.append(Fraction(1) + d * tau[-1])
    b: list[Number] = [Fraction(0)] + [
        d ** (h - layer) for layer in range(1, h + 1)
    ]

    forward_names = ("u", "v", "w", "x", "y", "j", "k")
    forward = [_zeros(forward_names) for _ in range(h + 1)]
    forward[1] = {
        "u": b[1] * moment("M121000"),
        "v": 3 * b[1] ** 2 * moment("M140010"),
        "w": b[1] * moment("M040000"),
        "x": 3 * b[1] ** 2 * moment("M050100"),
        "y": 3 * b[1] ** 2 * moment("M042000"),
        "j": 3 * b[1] * moment("M030100"),
        "k": 15 * b[1] ** 2 * moment("M050001"),
    }
    frozen_transition = fw.transition()
    for layer in range(2, h + 1):
        previous = forward[layer - 1]
        values = {
            **previous,
            "b": b[layer],
            "l1": tau[layer - 1],
            "l3": previous["j"] + 3 * previous["u"],
            "l5": previous["k"] + 5 * previous["v"],
        }
        forward[layer] = {
            name.removesuffix("_next"): evaluate(poly, values, moment)
            for name, poly in frozen_transition.items()
        }

    reverse_names = ("e02", "e11", "e13", "e22", "c10", "c21", "c30", "c32")
    reverse: list[dict[str, Number] | None] = [None] * (h + 1)
    frozen_sources: list[dict[str, Number] | None] = [None] * (h + 1)
    current = _zeros(reverse_names)
    current["c10"] = Fraction(1)
    reverse_transition = rv.transition()
    for layer in range(h, 0, -1):
        reverse[layer] = current
        previous = forward[layer - 1]
        values = {
            **previous,
            **current,
            "b": b[layer],
            "l1": tau[layer - 1],
            "l3": previous["j"] + 3 * previous["u"],
        }
        output = {
            name: evaluate(poly, values, moment)
            for name, poly in reverse_transition.items()
        }
        frozen_sources[layer] = {
            name: output[name]
            for name in ("source00", "source02", "source11", "source13", "source22")
        }
        current = {name: output[name + "_next"] for name in reverse_names}

    hessian_square: Number = forward[h]["w"]
    for layer in range(h, 0, -1):
        source = frozen_sources[layer]
        assert source is not None
        hessian_square += source["source11"]
        if layer > 1:
            hessian_square += source["source00"] * forward[layer - 1]["w"]

    moving = mv.transitions()
    q2_names = ("q02", "q22", "qfm", "a2")
    q2 = [_zeros(q2_names) for _ in range(h + 1)]
    for layer in range(1, h + 1):
        previous = forward[layer - 1]
        qprevious = q2[layer - 1]
        rcurrent = reverse[layer]
        assert rcurrent is not None
        values = {
            **previous,
            **qprevious,
            **rcurrent,
            "b": b[layer],
            "l1": tau[layer - 1],
            "l2": 1 + qprevious["a2"],
        }
        q2[layer] = {
            name.removesuffix("_next"): evaluate(poly, values, moment)
            for name, poly in moving["feature2"].items()
        }

    r2_names = ("r02", "r22", "rfm", "d21")
    r2: list[dict[str, Number] | None] = [None] * (h + 1)
    current = _zeros(r2_names)
    current["d21"] = Fraction(1)
    for layer in range(h, 0, -1):
        r2[layer] = current
        previous = forward[layer - 1]
        qprevious = q2[layer - 1]
        rcurrent = reverse[layer]
        assert rcurrent is not None
        values = {
            **previous,
            **qprevious,
            **rcurrent,
            **current,
            "b": b[layer],
            "l1": tau[layer - 1],
            "l2": 1 + qprevious["a2"],
        }
        output = {
            name: evaluate(poly, values, moment)
            for name, poly in moving["gradient2"].items()
        }
        current = {name: output[name + "_next"] for name in r2_names}

    q3_names = ("q13", "a30", "a32")
    q3 = [_zeros(q3_names) for _ in range(h + 1)]
    for layer in range(1, h + 1):
        previous = forward[layer - 1]
        qprevious = q2[layer - 1]
        q3previous = q3[layer - 1]
        rcurrent = reverse[layer]
        r2current = r2[layer]
        assert rcurrent is not None and r2current is not None
        values = {
            **previous,
            **qprevious,
            **q3previous,
            **rcurrent,
            **r2current,
            "b": b[layer],
            "l1": tau[layer - 1],
            "l2": 1 + qprevious["a2"],
            "l30": 4 * qprevious["q02"] + 3 * previous["w"] + q3previous["a30"],
            "l32": 1 + q3previous["a32"],
        }
        q3[layer] = {
            name.removesuffix("_next"): evaluate(poly, values, moment)
            for name, poly in moving["feature3"].items()
        }

    r3_names = ("r13", "d30", "d32")
    r3: list[dict[str, Number] | None] = [None] * (h + 1)
    current = _zeros(r3_names)
    current["d32"] = Fraction(1)
    for layer in range(h, 0, -1):
        r3[layer] = current
        previous = forward[layer - 1]
        qprevious = q2[layer - 1]
        q3previous = q3[layer - 1]
        rcurrent = reverse[layer]
        r2current = r2[layer]
        assert rcurrent is not None and r2current is not None
        values = {
            **previous,
            **qprevious,
            **q3previous,
            **rcurrent,
            **r2current,
            **current,
            "b": b[layer],
            "l1": tau[layer - 1],
            "l2": 1 + qprevious["a2"],
            "l30": 4 * qprevious["q02"] + 3 * previous["w"] + q3previous["a30"],
            "l32": 1 + q3previous["a32"],
        }
        output = {
            name: evaluate(poly, values, moment)
            for name, poly in moving["gradient3"].items()
        }
        current = {name: output[name + "_next"] for name in r3_names}

    head_transition = g4.transitions()
    head_names = ("gamma04", "a41", "a43")
    head = [_zeros(head_names) for _ in range(h + 1)]
    for layer in range(1, h + 1):
        previous = forward[layer - 1]
        qprevious = q2[layer - 1]
        q3previous = q3[layer - 1]
        head_previous = head[layer - 1]
        rcurrent = reverse[layer]
        r2current = r2[layer]
        r3current = r3[layer]
        assert rcurrent is not None and r2current is not None and r3current is not None
        values = {
            **previous,
            **qprevious,
            **q3previous,
            **head_previous,
            **rcurrent,
            **r2current,
            **r3current,
            "b": b[layer],
            "l1": tau[layer - 1],
            "l2": 1 + qprevious["a2"],
            "l30": 4 * qprevious["q02"] + 3 * previous["w"] + q3previous["a30"],
            "l32": 1 + q3previous["a32"],
            "l41": 9 * qprevious["q02"] + 8 * previous["w"] + head_previous["a41"],
            "l43": 1 + head_previous["a43"],
        }
        head[layer] = {
            name.removesuffix("_next"): evaluate(poly, values, moment)
            for name, poly in head_transition.items()
        }

    straight3 = forward[h]["j"] + 3 * forward[h]["u"]
    A: Number = tau[h]
    Bcoef: Number = 2 * straight3 + 4 * hessian_square
    layers: dict[int, dict[str, Number]] = {}
    for layer in range(1, h + 1):
        q2der = 2 * (forward[layer]["w"] + q2[layer]["q02"])
        q4der = 2 * head[layer]["gamma04"] + 8 * q3[layer]["q13"] + 6 * q2[layer]["q22"]
        layers[layer] = {
            "Gamma11": forward[layer]["w"],
            "Gamma02": q2[layer]["q02"],
            "Gamma22": q2[layer]["q22"],
            "Gamma13": q3[layer]["q13"],
            "Gamma04": head[layer]["gamma04"],
            "Q2": q2der,
            "Q4": q4der,
            "R2": q2der / 2,
            "R4": q4der / 2 - 3 * q2der**2 / 4,
        }
    return {
        "A": A,
        "B": Bcoef,
        "d": d,
        "tau": tau,
        "b": b,
        "forward": forward,
        "reverse": reverse,
        "q2": q2,
        "r2": r2,
        "q3": q3,
        "r3": r3,
        "head": head,
        "layers": layers,
    }

