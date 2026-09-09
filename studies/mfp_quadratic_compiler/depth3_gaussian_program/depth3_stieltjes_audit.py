#!/usr/bin/env python3
"""Exact Stieltjes-moment and accessible-Hankel audit for the depth-3 jet."""

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
INPUT = HERE / "results_order9.json"
PROTOCOL = HERE / "STIELTJES_PROTOCOL.md"
EXACT_SERIES = (
    REPO
    / "studies/stieltjes_conjecture/numerics/global_proxy_campaign/proxy/exact_series.py"
)

EXPECTED_SHA256 = {
    "input": "e6205be08cf663e64c259328afb276e03188845ef51a7001deef1a92e8778b3d",
    "protocol": "06e58ae90fbd6de9224489b4ad1f82e8d5e859bcbe9d5832de90109f6ab06f98",
    "exact_series_route": "d003563deb87c6baea7f423f954979f3082b306035eeba35cc223dda25d0ed60",
}


def load_existing_moment_transform():
    """Load the audited reversion route without altering Python's import path."""

    specification = importlib.util.spec_from_file_location(
        "depth3_audited_exact_series", EXACT_SERIES
    )
    if specification is None or specification.loader is None:
        raise ImportError(f"cannot load exact-series route from {EXACT_SERIES}")
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module.output_kernel_moments


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def power_series(series: Sequence[Fraction], exponent: int, degree: int) -> list[Fraction]:
    result = [Q(1)] + [Q(0) for _ in range(degree)]
    base = list(series[: degree + 1]) + [Q(0)] * max(0, degree + 1 - len(series))
    for _ in range(exponent):
        result = multiply_series(result, base, degree)
    return result


def moments_from_triangular_identity(
    odd_derivatives: dict[int, int],
) -> tuple[Fraction, tuple[Fraction, ...]]:
    """Solve F'(t)=K(F(t)) without constructing the inverse series."""

    max_order = max(odd_derivatives)
    if set(odd_derivatives) != set(range(1, max_order + 1, 2)):
        raise ValueError("odd derivatives must be consecutive")
    feature = [Q(0) for _ in range(max_order + 1)]
    feature_prime = [Q(0) for _ in range(max_order)]
    for order, derivative in odd_derivatives.items():
        feature[order] = Q(derivative, math.factorial(order))
        feature_prime[order - 1] = Q(derivative, math.factorial(order - 1))

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
            raise ArithmeticError("triangular kernel solve lost its leading term")
        kernel_terms[power] = (target - explained) / leading

    moments = tuple(
        ((-1) ** index) * kernel_terms[2 * index + 2]
        for index in range((max_order - 1) // 2)
    )
    return baseline, moments


def determinant(matrix: Sequence[Sequence[Fraction]]) -> Fraction:
    """Exact determinant by rational Gaussian elimination."""

    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("determinant requires a square matrix")
    if not size:
        return Q(1)
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


def principal_minors(matrix: Sequence[Sequence[Fraction]]) -> dict[str, Fraction]:
    result: dict[str, Fraction] = {}
    for size in range(1, len(matrix) + 1):
        for indices in combinations(range(len(matrix)), size):
            submatrix = [[matrix[i][j] for j in indices] for i in indices]
            label = ",".join(str(index) for index in indices)
            result[label] = determinant(submatrix)
    return result


def approximate_eigenvalues(matrix: Sequence[Sequence[Fraction]]) -> list[float]:
    if len(matrix) == 1:
        return [float(matrix[0][0])]
    if len(matrix) != 2:
        return []
    a, b = map(float, matrix[0])
    c = float(matrix[1][1])
    discriminant = math.sqrt((a - c) ** 2 + 4 * b * b)
    return sorted(((a + c - discriminant) / 2, (a + c + discriminant) / 2))


def fraction_string(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def audit_matrix(matrix: list[list[Fraction]]) -> dict[str, object]:
    minors = principal_minors(matrix)
    leading = [
        determinant([row[:size] for row in matrix[:size]])
        for size in range(1, len(matrix) + 1)
    ]
    return {
        "matrix": [[fraction_string(value) for value in row] for row in matrix],
        "principal_minors": {
            key: fraction_string(value) for key, value in minors.items()
        },
        "leading_principal_determinants": [
            fraction_string(value) for value in leading
        ],
        "approximate_eigenvalues": approximate_eigenvalues(matrix),
        "positive_semidefinite": all(value >= 0 for value in minors.values()),
        "positive_definite": all(value > 0 for value in leading),
    }


def audit_hankels(moments: Sequence[Fraction]) -> dict[str, object]:
    families: dict[str, dict[str, object]] = {"ordinary": {}, "shifted": {}}
    for shift, family in ((0, "ordinary"), (1, "shifted")):
        size = 1
        while 2 * (size - 1) + shift < len(moments):
            matrix = [
                [moments[row + column + shift] for column in range(size)]
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
        "all_accessible_matrices_positive_semidefinite": all(
            bool(record["positive_semidefinite"]) for record in records
        ),
        "all_accessible_matrices_positive_definite": all(
            bool(record["positive_definite"]) for record in records
        ),
    }


def main() -> int:
    actual_hashes = {
        "input": sha256(INPUT),
        "protocol": sha256(PROTOCOL),
        "exact_series_route": sha256(EXACT_SERIES),
    }
    if actual_hashes != EXPECTED_SHA256:
        raise AssertionError(
            f"SHA-256 gate failed: actual={actual_hashes}, expected={EXPECTED_SHA256}"
        )

    document = json.loads(INPUT.read_text())
    derivatives = {int(key): int(value) for key, value in document["derivatives"].items()}
    if sorted(derivatives) != list(range(10)):
        raise AssertionError("the input jet is not contiguous through order nine")
    if any(derivatives[order] for order in range(0, 10, 2)):
        raise AssertionError("input parity gate failed")
    odd_derivatives = {
        order: derivatives[order] for order in range(1, 10, 2)
    }

    baseline_a, moments_a = load_existing_moment_transform()(odd_derivatives)
    baseline_b, moments_b = moments_from_triangular_identity(odd_derivatives)
    if baseline_a != baseline_b or moments_a != moments_b:
        raise AssertionError("the two exact moment transformations disagree")
    if len(moments_a) != 4:
        raise AssertionError("order nine must determine exactly four moments")

    hankels = audit_hankels(moments_a)
    payload = {
        "model": document["model"],
        "max_feature_derivative_order": 9,
        "kernel_convention": (
            "K(y)=F'(F^{-1}(y))=F'(0)+sum_r (-1)^r mu_r y^(2r+2)"
        ),
        "kernel_baseline": fraction_string(baseline_a),
        "moments": {
            f"mu_{index}": {
                "exact": fraction_string(value),
                "decimal": float(value),
                "sign": "positive" if value > 0 else "zero" if value == 0 else "negative",
            }
            for index, value in enumerate(moments_a)
        },
        "hankel_audit": hankels,
        "moment_routes_agree": True,
        "validation": "passed",
        "verdict": (
            "all_accessible_hankel_matrices_positive_definite"
            if hankels["all_accessible_matrices_positive_definite"]
            else "at_least_one_accessible_hankel_matrix_not_positive_definite"
        ),
        "next_unavailable_conditions": {
            "mu_4_and_H_2": "require F^(11)(0)",
            "mu_5_and_H_2_plus": "require F^(13)(0)",
        },
        "sha256": actual_hashes,
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
