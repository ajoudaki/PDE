"""Post-freeze atomwise comparison of the two scalar-sector derivations."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import json

from ..independent import forward_contraction as independent_forward
from ..independent import reverse_contraction as independent_reverse
from ...order5.compiler.coefficient_map import expand_coefficient_map
from .scalar_frozen_recurrence import backward_transition, forward_transition


Polynomial = dict[tuple[str, ...], Fraction]


def add(*values: Polynomial) -> Polynomial:
    answer: defaultdict[tuple[str, ...], Fraction] = defaultdict(Fraction)
    for value in values:
        for monomial, coefficient in value.items():
            answer[monomial] += coefficient
    return {key: value for key, value in answer.items() if value}


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    answer: defaultdict[tuple[str, ...], Fraction] = defaultdict(Fraction)
    for lm, lc in left.items():
        for rm, rc in right.items():
            answer[tuple(sorted(lm + rm))] += lc * rc
    return {key: value for key, value in answer.items() if value}


def scalar(value: int | Fraction) -> Polynomial:
    value = Fraction(value)
    return {} if not value else {(): value}


def variable(name: str) -> Polynomial:
    return {(name,): Fraction(1)}


def translate(poly, replacements: dict[str, Polynomial]) -> Polynomial:
    answer: Polynomial = {}
    for monomial, coefficient in poly.items():
        term = scalar(coefficient)
        for name in monomial:
            if name.startswith("M") and len(name) == 7:
                factor = variable("M_" + name[1:])
            else:
                factor = replacements.get(name, variable(name))
            term = multiply(term, factor)
        answer = add(answer, term)
    return answer


def discrepancy(left: Polynomial, right: Polynomial) -> int:
    return sum(
        left.get(key, 0) != right.get(key, 0)
        for key in set(left) | set(right)
    )


def run_comparison() -> dict[str, object]:
    common = {
        "u": variable("P"),
        "v": variable("Q"),
        "w": variable("V"),
        "x": variable("W"),
        "y": variable("S"),
        "j": variable("J3"),
        "k": variable("J5"),
        "b": variable("BASE_B"),
        "l1": variable("TAU"),
        "l3": add(variable("J3"), {("P",): Fraction(3)}),
        "l5": add(variable("J5"), {("Q",): Fraction(5)}),
    }
    primary_forward = forward_transition()
    forward_names = {
        "u_next": "P_NEXT",
        "v_next": "Q_NEXT",
        "w_next": "V_NEXT",
        "x_next": "W_NEXT",
        "y_next": "S_NEXT",
        "j_next": "J3_NEXT",
        "k_next": "J5_NEXT",
    }
    forward = {
        independent_name: discrepancy(
            translate(independent_forward.transition()[independent_name], common),
            expand_coefficient_map(primary_forward[primary_name]),
        )
        for independent_name, primary_name in forward_names.items()
    }

    reverse_replacements = {
        **common,
        "b": variable("B00"),
        "e02": variable("B02"),
        "e11": variable("B11"),
        "e13": variable("B13"),
        "e22": variable("B22"),
        "c10": variable("K10"),
        "c21": variable("K21"),
        "c30": variable("K30"),
        "c32": variable("K32"),
    }
    primary_reverse = backward_transition()
    reverse_names = {
        "source00": "B00_NEXT",
        "source02": "B02_NEXT",
        "source11": "B11_NEXT",
        "source13": "B13_NEXT",
        "source22": "B22_NEXT",
        "c10_next": "K10_NEXT",
        "c21_next": "K21_NEXT",
        "c30_next": "K30_NEXT",
        "c32_next": "K32_NEXT",
    }
    independent_reverse_result = independent_reverse.transition()
    reverse = {
        independent_name: discrepancy(
            translate(independent_reverse_result[independent_name], reverse_replacements),
            expand_coefficient_map(primary_reverse[primary_name]),
        )
        for independent_name, primary_name in reverse_names.items()
    }
    result = {
        "status": "PASS" if not any(forward.values()) and not any(reverse.values()) else "FAIL",
        "forward_discrepancies": forward,
        "reverse_discrepancies": reverse,
    }
    if result["status"] != "PASS":
        raise AssertionError(result)
    return result


if __name__ == "__main__":
    print(json.dumps(run_comparison(), indent=2, sort_keys=True))
