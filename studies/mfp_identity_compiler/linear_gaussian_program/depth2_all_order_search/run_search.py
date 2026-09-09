#!/usr/bin/env python3
"""Exact long-jet production and precommitted closure search for H=2 identity."""

from __future__ import annotations

import hashlib
import json
import math
import sys
import time
from fractions import Fraction
from functools import reduce
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.path.insert(0, str(PARENT))

from identity_exact_jet import depth2_derivative, depth2_taylor, validate  # noqa: E402
from identity_stieltjes_audit import (  # noqa: E402
    fraction_string,
    load_reversion_route,
    moments_from_triangular_identity,
)


Q = Fraction
MAX_ORDER = 81
DISCOVERY_LAST = 24
HOLDOUT_LAST = 39


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def multiply(left: list[Fraction], right: list[Fraction], degree: int) -> list[Fraction]:
    result = [Q(0) for _ in range(degree + 1)]
    for i, a in enumerate(left):
        if i > degree or not a:
            continue
        for j, b in enumerate(right):
            if i + j > degree:
                break
            if b:
                result[i + j] += a * b
    return result


def powers(series: list[Fraction], max_power: int, degree: int) -> list[list[Fraction]]:
    result = [[Q(1)] + [Q(0) for _ in range(degree)]]
    padded = series[: degree + 1] + [Q(0)] * max(0, degree + 1 - len(series))
    for _ in range(max_power):
        result.append(multiply(result[-1], padded, degree))
    return result


def primitive_integer_vector(vector: sp.Matrix) -> tuple[int, ...]:
    rationals = [sp.Rational(value) for value in vector]
    denominator_lcm = math.lcm(*(int(value.q) for value in rationals))
    integers = [int(value * denominator_lcm) for value in rationals]
    common = reduce(math.gcd, (abs(value) for value in integers if value), 0)
    if not common:
        raise ArithmeticError("zero null vector")
    integers = [value // common for value in integers]
    first = next(value for value in integers if value)
    if first < 0:
        integers = [-value for value in integers]
    return tuple(integers)


def algebraic_candidates(moments: list[Fraction]) -> list[dict[str, object]]:
    max_degree = HOLDOUT_LAST
    moment_powers = powers(moments, 4, max_degree)
    candidates: list[dict[str, object]] = []
    seen: set[tuple[int, ...]] = set()
    q, z = sp.symbols("q z")

    boxes = []
    for degree_z in range(1, 5):
        for degree_q in range(0, 7):
            count = (degree_q + 1) * (degree_z + 1)
            if count <= DISCOVERY_LAST + 1:
                boxes.append((count, degree_z, degree_q))

    for _, degree_z, degree_q in sorted(boxes):
        terms = [
            (i, j)
            for i in range(degree_q + 1)
            for j in range(degree_z + 1)
        ]
        rows = []
        for order in range(DISCOVERY_LAST + 1):
            rows.append([
                sp.Rational(moment_powers[j][order - i].numerator,
                            moment_powers[j][order - i].denominator)
                if order >= i else sp.Integer(0)
                for i, j in terms
            ])
        nullspace = sp.Matrix(rows).nullspace()
        if len(nullspace) != 1:
            continue
        vector = primitive_integer_vector(nullspace[0])
        if vector in seen:
            continue
        nonzero_terms = [terms[index] for index, value in enumerate(vector) if value]
        if min(i for i, _ in nonzero_terms) != 0:
            continue
        if max(i for i, _ in nonzero_terms) != degree_q:
            continue
        if max(j for _, j in nonzero_terms) != degree_z:
            continue

        residuals: list[Fraction] = []
        for order in range(HOLDOUT_LAST + 1):
            value = Q(0)
            for coefficient, (i, j) in zip(vector, terms):
                if coefficient and order >= i:
                    value += coefficient * moment_powers[j][order - i]
            residuals.append(value)
        discovery_pass = all(value == 0 for value in residuals[: DISCOVERY_LAST + 1])
        holdout = residuals[DISCOVERY_LAST + 1 : HOLDOUT_LAST + 1]
        if not discovery_pass or not all(value == 0 for value in holdout):
            continue

        expression = sum(
            coefficient * q**i * z**j
            for coefficient, (i, j) in zip(vector, terms)
        )
        primitive = sp.Poly(expression, q, z, domain=sp.ZZ).primitive()[1]
        canonical = tuple(int(value) for value in primitive.coeffs())
        if canonical in seen:
            continue
        seen.add(vector)
        seen.add(canonical)
        candidates.append({
            "degree_q": degree_q,
            "degree_M": degree_z,
            "coefficient_count": len(terms),
            "polynomial": str(sp.factor(expression)),
            "terms": [
                {"q_power": i, "M_power": j, "coefficient": coefficient}
                for coefficient, (i, j) in zip(vector, terms)
                if coefficient
            ],
            "discovery_coefficients_zero": DISCOVERY_LAST + 1,
            "held_out_coefficients_zero": len(holdout),
            "held_out_exact_pass": True,
        })
    return candidates


def recurrence_candidates(moments: list[Fraction]) -> list[dict[str, object]]:
    candidates: list[dict[str, object]] = []
    seen: set[tuple[int, ...]] = set()
    r_symbol = sp.symbols("r")
    boxes = []
    for order in range(1, 5):
        for degree in range(0, 5):
            count = (order + 1) * (degree + 1)
            if count <= DISCOVERY_LAST + 1:
                boxes.append((count, order, degree))

    for _, recurrence_order, polynomial_degree in sorted(boxes):
        terms = [
            (shift, degree)
            for shift in range(recurrence_order + 1)
            for degree in range(polynomial_degree + 1)
        ]
        discovery_rows = range(0, DISCOVERY_LAST - recurrence_order + 1)
        rows = [
            [
                sp.Rational(moments[index + shift].numerator,
                            moments[index + shift].denominator)
                * index**degree
                for shift, degree in terms
            ]
            for index in discovery_rows
        ]
        nullspace = sp.Matrix(rows).nullspace()
        if len(nullspace) != 1:
            continue
        vector = primitive_integer_vector(nullspace[0])
        if vector in seen:
            continue
        if not any(
            coefficient
            for coefficient, (shift, _) in zip(vector, terms)
            if shift == recurrence_order
        ):
            continue
        if max(
            degree for coefficient, (_, degree) in zip(vector, terms) if coefficient
        ) != polynomial_degree:
            continue

        residuals = []
        for index in range(0, HOLDOUT_LAST - recurrence_order + 1):
            residuals.append(sum(
                Q(coefficient) * index**degree * moments[index + shift]
                for coefficient, (shift, degree) in zip(vector, terms)
            ))
        discovery_count = DISCOVERY_LAST - recurrence_order + 1
        holdout = residuals[discovery_count:]
        if not all(value == 0 for value in residuals[:discovery_count]):
            continue
        if not holdout or not all(value == 0 for value in holdout):
            continue

        polynomials = []
        for shift in range(recurrence_order + 1):
            expression = sum(
                coefficient * r_symbol**degree
                for coefficient, (candidate_shift, degree) in zip(vector, terms)
                if candidate_shift == shift
            )
            polynomials.append(sp.Poly(expression, r_symbol, domain=sp.ZZ))
        common = reduce(sp.gcd, polynomials)
        if common.degree() > 0:
            polynomials = [sp.exquo(poly, common) for poly in polynomials]
        canonical = tuple(
            int(coefficient)
            for poly in polynomials
            for coefficient in poly.all_coeffs()
        )
        if canonical in seen:
            continue
        seen.add(vector)
        seen.add(canonical)
        candidates.append({
            "order": recurrence_order,
            "polynomial_degree": polynomial_degree,
            "coefficient_count": len(terms),
            "polynomials_by_shift": [str(poly.as_expr()) for poly in polynomials],
            "meaning": "sum_j p_j(r)*mu_(r+j)=0",
            "discovery_equations_zero": discovery_count,
            "held_out_equations_zero": len(holdout),
            "held_out_exact_pass": True,
        })
    return candidates


def main() -> int:
    started = time.perf_counter()
    taylor = depth2_taylor(MAX_ORDER)
    derivative = depth2_derivative(MAX_ORDER)
    validation = validate([taylor, derivative], MAX_ORDER)
    if taylor.derivatives != derivative.derivatives:
        raise AssertionError("the two exact jet routes disagree")

    odd = {
        order: int(taylor.derivatives[order])
        for order in range(1, MAX_ORDER + 1, 2)
    }
    baseline_a, moments_a = moments_from_triangular_identity(odd)
    reversion = load_reversion_route()
    baseline_b, moments_b = reversion(odd)
    if baseline_a != baseline_b or moments_a != moments_b:
        raise AssertionError("the two exact moment routes disagree")
    if len(moments_a) != HOLDOUT_LAST + 1:
        raise AssertionError("order 81 must determine mu_0 through mu_39")

    moment_list = list(moments_a)
    algebraic = algebraic_candidates(moment_list)
    recurrences = recurrence_candidates(moment_list)
    payload = {
        "format": "identity-depth2-all-order-search-v1",
        "model": "one-input equal-width identity activation, two hidden layers",
        "max_feature_derivative_order": MAX_ORDER,
        "derivatives": [fraction_string(value) for value in taylor.derivatives],
        "kernel_baseline": fraction_string(baseline_a),
        "moments": [fraction_string(value) for value in moment_list],
        "discovery_moments": [0, DISCOVERY_LAST],
        "held_out_moments": [DISCOVERY_LAST + 1, HOLDOUT_LAST],
        "algebraic_ogf_candidates": algebraic,
        "p_recursive_candidates": recurrences,
        "validation": {
            **validation,
            "moment_routes_agree": True,
            "candidate_claim_level": "held-out exact coefficient identity only",
        },
        "elapsed_seconds": {
            "taylor": taylor.elapsed_seconds,
            "derivative": derivative.elapsed_seconds,
            "total": time.perf_counter() - started,
        },
        "sha256": {
            "protocol": sha256(HERE / "PROTOCOL.md"),
            "jet_source": sha256(PARENT / "identity_exact_jet.py"),
            "search_source": sha256(Path(__file__)),
        },
        "claim_boundary": (
            "A held-out pass is conjectural until independently derived; "
            "failure finds no formula only in the frozen bounded classes."
        ),
    }
    output = HERE / "RESULTS.json"
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "output": str(output),
        "elapsed_seconds": payload["elapsed_seconds"],
        "algebraic_candidate_count": len(algebraic),
        "recurrence_candidate_count": len(recurrences),
        "last_derivative": payload["derivatives"][-1],
        "last_moment": payload["moments"][-1],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

