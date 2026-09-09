"""Exact audits for the independently frozen scalar sector recurrence."""

from __future__ import annotations

from fractions import Fraction
import json

from ..audit.exact_controls import evaluate
from ..audit.reference_maps import difference, load_reference
from ...order5.compiler.coefficient_map import expand_coefficient_map
from ...order5.compiler.factored_expression import atom, symbol
from .scalar_frozen_recurrence import (
    assemble_frozen_recurrence,
    backward_transition,
    derivative_ceiling,
    forward_transition,
)


def _map(expression):
    return expand_coefficient_map(expression)


def projection_audit() -> dict[str, int]:
    d = atom("M", (0, 2, 0, 0, 0, 0))
    u = atom("M", (0, 4, 0, 0, 0, 0))
    v = atom("M", (1, 0, 1, 0, 0, 0))
    m = atom("M", (1, 2, 1, 0, 0, 0))
    r = atom("M", (0, 1, 0, 1, 0, 0))
    s = atom("M", (0, 0, 2, 0, 0, 0))
    j = atom("M", (0, 3, 0, 1, 0, 0))
    e = atom("M", (0, 2, 2, 0, 0, 0))
    h = atom("M", (2, 2, 0, 0, 0, 0))
    p, vv, j3 = symbol("P"), symbol("V"), symbol("J3")
    tau, base = symbol("TAU"), symbol("BASE_B")
    f = forward_transition()
    expected_forward = {
        "V_NEXT": d * vv + tau * tau * base * u,
        "P_NEXT": v * vv + tau * tau * base * m + (d + v) * p,
        "J3_NEXT": (
            3 * tau * vv * r
            + 3 * tau * tau * tau * base * j
            + 3 * tau * p * (r + s)
            + (j3 + 3 * p) * d
        ),
    }
    b00, b11, k10 = symbol("B00"), symbol("B11"), symbol("K10")
    b = backward_transition()
    expected_backward = {
        "B11_NEXT": (
            base * 0  # keeps the expression visibly tied to the same alphabet
            + b00 * vv * s
            + 3 * tau * tau * b00 * b00 * e
            + d * b11
            + k10 * k10 * h
            + 2 * tau * k10 * b00 * m
        ),
        "K10_NEXT": d * b00 + tau * b00 * (r + s) + k10 * (v + d),
    }
    discrepancies: dict[str, int] = {}
    for name, expected in {**expected_forward, **expected_backward}.items():
        got = f[name] if name in f else b[name]
        discrepancies[name] = len(
            {
                key
                for key in set(_map(got)) | set(_map(expected))
                if _map(got).get(key, 0) != _map(expected).get(key, 0)
            }
        )
    return discrepancies


def run_audit() -> dict[str, object]:
    result: dict[str, object] = {
        "scope": "frozen first-three D5 tensor families; not a full C witness",
        "projection_transition_discrepancies": projection_audit(),
        "depths": {},
    }
    for depth in (2, 3, 4):
        recurrence = assemble_frozen_recurrence(depth)
        reference = load_reference(depth)
        candidate_a = _map(recurrence.A)
        candidate_b = _map(recurrence.B)
        candidate_partial_c = _map(recurrence.partial_C)
        controls = {
            "constant_1": str(evaluate(candidate_partial_c, (1,))),
            "linear": str(evaluate(candidate_partial_c, (0, 1))),
            "unit_affine_3_4": str(
                evaluate(candidate_partial_c, (Fraction(3, 5), Fraction(4, 5)))
            ),
        }
        result["depths"][str(depth)] = {
            "A": difference(candidate_a, reference["A"]),
            "B": difference(candidate_b, reference["B"]),
            "partial_C_vs_full_C": difference(candidate_partial_c, reference["C"]),
            "partial_C_count": len(candidate_partial_c),
            "derivative_ceiling": derivative_ceiling(
                {"A": recurrence.A, "B": recurrence.B, "partial_C": recurrence.partial_C}
            ),
            "partial_C_controls": controls,
        }
    if any(result["projection_transition_discrepancies"].values()):
        raise AssertionError(result["projection_transition_discrepancies"])
    for depth, audit in result["depths"].items():
        if audit["A"]["discrepancy_count"] or audit["B"]["discrepancy_count"]:
            raise AssertionError((depth, audit))
        if audit["derivative_ceiling"] > 5:
            raise AssertionError((depth, audit["derivative_ceiling"]))
    return result


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, sort_keys=True))
