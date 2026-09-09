#!/usr/bin/env python3
"""Exact five-moment Stieltjes/Hankel audit for identity depths two and three."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Sequence


Q = Fraction
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
INPUT = HERE / "RESULTS.json"
PROTOCOL = HERE / "STIELTJES_PROTOCOL.md"
EXACT_SERIES = (
    REPO
    / "studies/stieltjes_conjecture/numerics/global_proxy_campaign/proxy/exact_series.py"
)
EXPECTED_INPUT_SHA256 = "6acac5edc920a02b68ea0d0f53f9fac675cacdca5a750309b51654b8fc1d19c3"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_reversion_route():
    specification = importlib.util.spec_from_file_location(
        "identity_audited_exact_series", EXACT_SERIES
    )
    if specification is None or specification.loader is None:
        raise ImportError(f"cannot load exact-series route from {EXACT_SERIES}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module.output_kernel_moments


def multiply_series(
    left: Sequence[Fraction], right: Sequence[Fraction], degree: int
) -> list[Fraction]:
    result = [Q(0) for _ in range(degree + 1)]
    for i, left_value in enumerate(left):
        if i > degree or not left_value:
            continue
        for j, right_value in enumerate(right):
            if i + j > degree:
                break
            if right_value:
                result[i + j] += left_value * right_value
    return result


def power_series(
    series: Sequence[Fraction], exponent: int, degree: int
) -> list[Fraction]:
    result = [Q(1)] + [Q(0) for _ in range(degree)]
    base = list(series[: degree + 1])
    base += [Q(0)] * max(0, degree + 1 - len(base))
    for _ in range(exponent):
        result = multiply_series(result, base, degree)
    return result


def moments_from_triangular_identity(
    odd_derivatives: dict[int, int],
) -> tuple[Fraction, tuple[Fraction, ...]]:
    """Solve F'(t)=K(F(t)) coefficient by coefficient."""

    max_order = max(odd_derivatives)
    if set(odd_derivatives) != set(range(1, max_order + 1, 2)):
        raise ValueError("odd derivatives must be consecutive")
    feature = [Q(0) for _ in range(max_order + 1)]
    feature_prime = [Q(0) for _ in range(max_order)]
    for order, derivative in odd_derivatives.items():
        feature[order] = Q(derivative, math.factorial(order))
        feature_prime[order - 1] = Q(
            derivative, math.factorial(order - 1)
        )

    baseline = Q(odd_derivatives[1])
    kernel_terms: dict[int, Fraction] = {}
    for power in range(2, max_order, 2):
        target = feature_prime[power]
        explained = Q(0)
        for prior_power, coefficient in kernel_terms.items():
            explained += coefficient * power_series(
                feature, prior_power, power
            )[power]
        leading = power_series(feature, power, power)[power]
        if not leading:
            raise ArithmeticError("triangular solve lost its leading term")
        kernel_terms[power] = (target - explained) / leading

    moments = tuple(
        ((-1) ** index) * kernel_terms[2 * index + 2]
        for index in range((max_order - 1) // 2)
    )
    return baseline, moments


def determinant(matrix: Sequence[Sequence[Fraction]]) -> Fraction:
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("determinant requires a square matrix")
    work = [list(row) for row in matrix]
    sign = 1
    value = Q(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column]), None
        )
        if pivot is None:
            return Q(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign *= -1
        pivot_value = work[column][column]
        value *= pivot_value
        for row in range(column + 1, size):
            ratio = work[row][column] / pivot_value
            if not ratio:
                continue
            for following in range(column + 1, size):
                work[row][following] -= ratio * work[column][following]
    return sign * value


def principal_minors(
    matrix: Sequence[Sequence[Fraction]],
) -> dict[str, Fraction]:
    result: dict[str, Fraction] = {}
    for size in range(1, len(matrix) + 1):
        for indices in combinations(range(len(matrix)), size):
            submatrix = [
                [matrix[i][j] for j in indices] for i in indices
            ]
            result[",".join(str(index) for index in indices)] = determinant(
                submatrix
            )
    return result


def fraction_string(value: Fraction) -> str:
    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


def signed_record(value: Fraction) -> dict[str, object]:
    return {
        "exact": fraction_string(value),
        "decimal": float(value),
        "sign": "positive" if value > 0 else "zero" if value == 0 else "negative",
        "nonnegative": value >= 0,
    }


def audit_matrix(matrix: list[list[Fraction]]) -> dict[str, object]:
    minors = principal_minors(matrix)
    leading = [
        determinant([row[:size] for row in matrix[:size]])
        for size in range(1, len(matrix) + 1)
    ]
    return {
        "matrix": [
            [fraction_string(value) for value in row] for row in matrix
        ],
        "principal_minors": {
            key: signed_record(value) for key, value in minors.items()
        },
        "leading_principal_determinants": [
            signed_record(value) for value in leading
        ],
        "positive_semidefinite": all(value >= 0 for value in minors.values()),
        "positive_definite": all(value > 0 for value in leading),
    }


def audit_hankels(moments: Sequence[Fraction]) -> dict[str, object]:
    families: dict[str, dict[str, object]] = {
        "ordinary": {},
        "shifted": {},
    }
    for shift, family in ((0, "ordinary"), (1, "shifted")):
        size = 1
        while 2 * (size - 1) + shift < len(moments):
            matrix = [
                [
                    moments[row + column + shift]
                    for column in range(size)
                ]
                for row in range(size)
            ]
            label = f"H_{size - 1}" + ("_plus" if shift else "")
            families[family][label] = audit_matrix(matrix)
            size += 1
    records = [
        record for family in families.values() for record in family.values()
    ]
    return {
        **families,
        "accessible_matrix_count": len(records),
        "enumerated_principal_minor_count_with_duplicates": sum(
            len(record["principal_minors"]) for record in records
        ),
        "all_accessible_matrices_positive_semidefinite": all(
            bool(record["positive_semidefinite"]) for record in records
        ),
        "all_accessible_matrices_positive_definite": all(
            bool(record["positive_definite"]) for record in records
        ),
    }


def all_distinct_two_by_two(moments: Sequence[Fraction]) -> dict[str, object]:
    mu = moments
    formulas = {
        "mu_0*mu_2-mu_1^2": mu[0] * mu[2] - mu[1] ** 2,
        "mu_0*mu_3-mu_1*mu_2": mu[0] * mu[3] - mu[1] * mu[2],
        "mu_0*mu_4-mu_1*mu_3": mu[0] * mu[4] - mu[1] * mu[3],
        "mu_0*mu_4-mu_2^2": mu[0] * mu[4] - mu[2] ** 2,
        "mu_1*mu_3-mu_2^2": mu[1] * mu[3] - mu[2] ** 2,
        "mu_1*mu_4-mu_2*mu_3": mu[1] * mu[4] - mu[2] * mu[3],
        "mu_2*mu_4-mu_3^2": mu[2] * mu[4] - mu[3] ** 2,
    }
    return {
        "minors": {formula: signed_record(value) for formula, value in formulas.items()},
        "all_nonnegative": all(value >= 0 for value in formulas.values()),
        "all_positive": all(value > 0 for value in formulas.values()),
    }


def audit_depth(
    depth: int, derivatives: Sequence[int], reversion_route
) -> dict[str, object]:
    if len(derivatives) != 12:
        raise AssertionError(f"depth {depth}: input is not contiguous through order 11")
    if any(derivatives[order] for order in range(0, 12, 2)):
        raise AssertionError(f"depth {depth}: parity gate failed")
    odd = {order: derivatives[order] for order in range(1, 12, 2)}
    baseline_a, moments_a = reversion_route(odd)
    baseline_b, moments_b = moments_from_triangular_identity(odd)
    if baseline_a != baseline_b or moments_a != moments_b:
        raise AssertionError(f"depth {depth}: exact moment routes disagree")
    if len(moments_a) != 5:
        raise AssertionError("order 11 must determine exactly five moments")

    hankels = audit_hankels(moments_a)
    if hankels["accessible_matrix_count"] != 5:
        raise AssertionError("five moments must expose exactly five full matrices")
    two_by_two = all_distinct_two_by_two(moments_a)
    h2 = [
        [moments_a[row + column] for column in range(3)]
        for row in range(3)
    ]
    det_h2 = determinant(h2)
    compatible = bool(hankels["all_accessible_matrices_positive_semidefinite"])
    return {
        "depth": depth,
        "kernel_baseline": signed_record(baseline_a),
        "moments": {
            f"mu_{index}": signed_record(value)
            for index, value in enumerate(moments_a)
        },
        "hankel_audit": hankels,
        "distinct_accessible_two_by_two_hankel_minors": two_by_two,
        "det_H_2": signed_record(det_h2),
        "unique_scalar_psd_inequalities": 10,
        "all_accessible_total_positivity_minors_positive": (
            all(value > 0 for value in moments_a)
            and bool(two_by_two["all_positive"])
            and det_h2 > 0
        ),
        "moment_routes_agree": True,
        "verdict": (
            "all_accessible_stieltjes_hankel_conditions_pass_strictly"
            if compatible
            else "at_least_one_accessible_stieltjes_hankel_condition_fails"
        ),
    }


def main() -> int:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("accepted derivative-input SHA-256 changed")
    document = json.loads(INPUT.read_text())
    reversion_route = load_reversion_route()
    results = [
        audit_depth(
            int(depth), [int(value) for value in derivatives], reversion_route
        )
        for depth, derivatives in sorted(document["derivatives"].items())
    ]
    payload = {
        "format": "identity-order11-stieltjes-audit-v1",
        "model": document["model"],
        "max_feature_derivative_order": 11,
        "kernel_convention": (
            "K(y)=F'(F^{-1}(y))=F'(0)+sum_r (-1)^r mu_r y^(2r+2)"
        ),
        "determined_moments": ["mu_0", "mu_1", "mu_2", "mu_3", "mu_4"],
        "depths": results,
        "validation": "passed",
        "next_unavailable_conditions": {
            "mu_5_and_H_2_plus": "require F^(13)(0)"
        },
        "claim_boundary": (
            "finite order-11 compatibility only; no infinite Stieltjes sequence, "
            "representing measure, convergence, or positive-time claim"
        ),
        "sha256": {
            "input": sha256(INPUT),
            "protocol": sha256(PROTOCOL),
            "exact_series_route": sha256(EXACT_SERIES),
        },
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
