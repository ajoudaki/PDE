#!/usr/bin/env python3
"""Exact jets and Stieltjes audit for the shallow normalized Hermite-2 model."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import time
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
LINEAR_PROGRAM = HERE.parent.parent / "identity_compiler" / "linear_gaussian_program"
SEARCH_PROGRAM = LINEAR_PROGRAM / "depth2_all_order_search"
sys.path.insert(0, str(LINEAR_PROGRAM))
sys.path.insert(0, str(SEARCH_PROGRAM))

from identity_order13_stieltjes_audit import (  # noqa: E402
    enumerate_accessible_hankel_minors,
    matrix_label,
)
from identity_stieltjes_audit import (  # noqa: E402
    audit_hankels,
    fraction_string,
    load_reversion_route,
    moments_from_triangular_identity,
    signed_record,
)
from run_search import algebraic_candidates, recurrence_candidates  # noqa: E402


Q = Fraction
Monomial = tuple[int, int]
Polynomial = dict[Monomial, Fraction]
DECISION_ORDER = 13
SEARCH_ORDER = 81


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def add(*polynomials: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            result[monomial] = result.get(monomial, Q(0)) + coefficient
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def scale(polynomial: Polynomial, coefficient: Fraction | int) -> Polynomial:
    coefficient = Q(coefficient)
    return {
        monomial: coefficient * value
        for monomial, value in polynomial.items()
        if coefficient * value
    }


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for (left_b, left_v), left_coefficient in left.items():
        for (right_b, right_v), right_coefficient in right.items():
            monomial = (left_b + right_b, left_v + right_v)
            result[monomial] = (
                result.get(monomial, Q(0))
                + left_coefficient * right_coefficient
            )
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def lie_derivative(polynomial: Polynomial) -> Polynomial:
    """Lie derivative for b'=v-1 and v'=2*b*v."""

    result: Polynomial = {}

    def accumulate(monomial: Monomial, coefficient: Fraction) -> None:
        result[monomial] = result.get(monomial, Q(0)) + coefficient

    for (b_power, v_power), coefficient in polynomial.items():
        if b_power:
            accumulate((b_power - 1, v_power + 1), coefficient * b_power)
            accumulate((b_power - 1, v_power), -coefficient * b_power)
        if v_power:
            accumulate((b_power + 1, v_power), 2 * coefficient * v_power)
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def odd_double_factorial(index: int) -> int:
    if index <= 0:
        return 1
    return math.prod(range(index, 0, -2))


def gaussian_expectation(polynomial: Polynomial) -> Fraction:
    """Expectation for independent b=sqrt(2)G_1 and v=G_2^2."""

    result = Q(0)
    for (b_power, v_power), coefficient in polynomial.items():
        if b_power % 2:
            continue
        b_half = b_power // 2
        b_moment = 2**b_half * odd_double_factorial(b_power - 1)
        v_moment = odd_double_factorial(2 * v_power - 1)
        result += coefficient * b_moment * v_moment
    return result


def lie_jet(max_order: int) -> tuple[list[Fraction], list[int]]:
    observable: Polynomial = {(1, 1): Q(1, 2), (1, 0): Q(-1, 2)}
    derivatives: list[Fraction] = []
    supports: list[int] = []
    current = observable
    for _ in range(max_order + 1):
        derivatives.append(gaussian_expectation(current))
        supports.append(len(current))
        current = lie_derivative(current)
    return derivatives, supports


def taylor_jet(max_order: int) -> tuple[list[Fraction], dict[str, list[int]]]:
    one: Polynomial = {(0, 0): Q(1)}
    b: list[Polynomial] = [{(1, 0): Q(1)}]
    v: list[Polynomial] = [{(0, 1): Q(1)}]

    for degree in range(max_order):
        velocity_b = add(v[degree], scale(one, -1) if degree == 0 else {})
        b.append(scale(velocity_b, Q(1, degree + 1)))
        convolution: Polynomial = {}
        for left in range(degree + 1):
            convolution = add(convolution, multiply(b[left], v[degree - left]))
        v.append(scale(convolution, Q(2, degree + 1)))

    derivatives: list[Fraction] = []
    output_supports: list[int] = []
    for degree in range(max_order + 1):
        coefficient: Polynomial = {}
        for left in range(degree + 1):
            right = degree - left
            v_minus_one = add(v[right], scale(one, -1) if right == 0 else {})
            coefficient = add(coefficient, multiply(b[left], v_minus_one))
        coefficient = scale(coefficient, Q(1, 2))
        derivatives.append(math.factorial(degree) * gaussian_expectation(coefficient))
        output_supports.append(len(coefficient))
    return derivatives, {
        "b": [len(polynomial) for polynomial in b],
        "v": [len(polynomial) for polynomial in v],
        "output": output_supports,
    }


def serialize_minors(moments: tuple[Fraction, ...]) -> dict[str, object]:
    families = enumerate_accessible_hankel_minors(moments)
    records: dict[str, object] = {}
    values: list[Fraction] = []
    for size, family in families.items():
        records[f"size_{size}"] = {}
        for matrix, value in sorted(family.items()):
            values.append(value)
            records[f"size_{size}"][matrix_label(matrix)] = {
                **signed_record(value),
                "moment_index_matrix": [list(row) for row in matrix],
            }
    counts = {str(size): len(family) for size, family in families.items()}
    if counts != {"1": 6, "2": 13, "3": 4}:
        raise AssertionError(f"unexpected minor counts: {counts}")
    return {
        "counts": counts,
        "families": records,
        "all_nonnegative": all(value >= 0 for value in values),
        "all_positive": all(value > 0 for value in values),
        "negative_labels": [
            matrix_label(matrix)
            for family in families.values()
            for matrix, value in family.items()
            if value < 0
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--long-search",
        action="store_true",
        help="extend the cheap exact Lie route through order 81 and run the frozen closure search",
    )
    args = parser.parse_args()
    lie_order = SEARCH_ORDER if args.long_search else DECISION_ORDER
    taylor_order = DECISION_ORDER
    started = time.perf_counter()
    lie, lie_support = lie_jet(lie_order)
    taylor, taylor_support = taylor_jet(taylor_order)
    if lie[: taylor_order + 1] != taylor:
        mismatch = next(
            index
            for index, pair in enumerate(zip(lie, taylor))
            if pair[0] != pair[1]
        )
        raise AssertionError(f"jet routes disagree first at order {mismatch}")
    if any(lie[order] for order in range(0, lie_order + 1, 2)):
        raise AssertionError("even-derivative parity failed")

    reversion = load_reversion_route()
    decision_odd = {
        order: int(lie[order])
        for order in range(1, DECISION_ORDER + 1, 2)
    }
    baseline_a, moments_a = moments_from_triangular_identity(decision_odd)
    baseline_b, moments_b = reversion(decision_odd)
    if baseline_a != baseline_b or moments_a != moments_b:
        raise AssertionError("order-13 moment routes disagree")

    algebraic: list[dict[str, object]] = []
    recurrences: list[dict[str, object]] = []
    long_search: dict[str, object]
    if args.long_search:
        long_odd = {
            order: int(lie[order])
            for order in range(1, SEARCH_ORDER + 1, 2)
        }
        long_baseline_a, long_moments_a = moments_from_triangular_identity(long_odd)
        long_baseline_b, long_moments_b = reversion(long_odd)
        if long_baseline_a != long_baseline_b or long_moments_a != long_moments_b:
            raise AssertionError("long-jet moment routes disagree")
        if tuple(long_moments_a[:6]) != moments_a:
            raise AssertionError("long moment route changed the order-13 prefix")
        algebraic = algebraic_candidates(list(long_moments_a))
        recurrences = recurrence_candidates(list(long_moments_a))
        long_search = {
            "status": "completed",
            "max_feature_derivative_order": SEARCH_ORDER,
            "moment_count": len(long_moments_a),
            "discovery_moments": [0, 24],
            "held_out_moments": [25, 39],
            "algebraic_ogf_candidates": algebraic,
            "p_recursive_candidates": recurrences,
            "claim_level": "held-out coefficient search; not an all-order proof",
        }
    else:
        long_search = {
            "status": "not_run_in_order13_production",
            "reason": "optional order-81 search is separate from the frozen order-13 decision",
        }
    minor_audit = serialize_minors(moments_a)
    hankel_audit = audit_hankels(moments_a)
    payload = {
        "format": "shallow-normalized-hermite2-order13-v1",
        "model": {
            "network": "n^-1 sum_i A_i*phi(u_i)",
            "activation": "phi(u)=(u^2-1)/sqrt(2)=He_2(u)/sqrt(2!)",
            "initialization": "A_i,u_i independent N(0,1)",
            "feature_flow": ["A'=phi(u)", "u'=A*phi'(u)"],
            "rational_coordinates": ["b=sqrt(2)A", "v=u^2"],
            "rational_flow": ["b'=v-1", "v'=2*b*v"],
            "observable": "F=E[b*(v-1)]/2",
        },
        "exact_coordinate_structure": {
            "invariant": "I=b^2-v+log(v)",
            "log_coordinate_equation": "q=log(v): q''=2*(exp(q)-1)",
            "first_integral": "q'^2=4*(I+exp(q)-q)",
            "quadrature": "dt=dq/(sign(b)*2*sqrt(I+exp(q)-q)) between turning points",
            "output_identity": "F(t)=(1/4)*d E[b(t)^2]/dt",
            "scope": "per-neuron implicit solution; not a closed scalar formula for the Gaussian average F",
        },
        "derivatives_through_13": [fraction_string(value) for value in lie[:14]],
        "kernel_baseline": signed_record(baseline_a),
        "moments_mu_0_through_5": [signed_record(value) for value in moments_a],
        "hankel_audit": hankel_audit,
        "all_23_accessible_hankel_minors": minor_audit,
        "long_jet_search": long_search,
        "validation": {
            "lie_and_taylor_routes_agree_through": taylor_order,
            "lie_route_extended_through": lie_order,
            "all_even_derivatives_zero_through": lie_order - (lie_order % 2),
            "two_exact_moment_routes_agree": True,
            "unit_gaussian_activation_variance": True,
        },
        "support_counts": {
            "lie": lie_support,
            "taylor": taylor_support,
        },
        "elapsed_seconds": time.perf_counter() - started,
        "sha256": {
            "protocol": sha256(HERE / "PROTOCOL.md"),
            "source": sha256(Path(__file__)),
        },
        "claim_boundary": (
            "The order-13 jet, six moments, and finite Hankel signs are exact. "
            "The coordinate quadrature is exact but is not a closed population F or K."
        ),
    }
    output = HERE / "RESULTS.json"
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "output": str(output),
        "elapsed_seconds": payload["elapsed_seconds"],
        "derivatives_through_13": payload["derivatives_through_13"],
        "moments": [record["exact"] for record in payload["moments_mu_0_through_5"]],
        "all_23_minors_positive": minor_audit["all_positive"],
        "negative_minor_labels": minor_audit["negative_labels"],
        "algebraic_candidate_count": len(algebraic),
        "recurrence_candidate_count": len(recurrences),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
