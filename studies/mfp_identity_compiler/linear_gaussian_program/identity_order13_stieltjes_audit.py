#!/usr/bin/env python3
"""Exact order-13 Stieltjes/Hankel extension for identity depths two and three."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Sequence

try:
    from .identity_stieltjes_audit import (
        audit_hankels,
        determinant,
        load_reversion_route,
        moments_from_triangular_identity,
        signed_record,
    )
except ImportError:  # Allow direct execution from this directory.
    from identity_stieltjes_audit import (
        audit_hankels,
        determinant,
        load_reversion_route,
        moments_from_triangular_identity,
        signed_record,
    )


Q = Fraction
HERE = Path(__file__).resolve().parent
INPUT = HERE / "RESULTS_ORDER13.json"
PROTOCOL = HERE / "ORDER13_PROTOCOL.md"
EXPECTED_INPUT_SHA256 = "4b4f8d2922f7c547ef9a0472025fc0c780c676454f36d366698bec1130814165"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sum_matrix(
    rows: tuple[int, ...], columns: tuple[int, ...]
) -> tuple[tuple[int, ...], ...]:
    matrix = tuple(
        tuple(row + column for column in columns) for row in rows
    )
    transpose = tuple(
        tuple(matrix[j][i] for j in range(len(rows)))
        for i in range(len(columns))
    )
    return min(matrix, transpose)


def enumerate_accessible_hankel_minors(
    moments: Sequence[Fraction],
) -> dict[int, dict[tuple[tuple[int, ...], ...], Fraction]]:
    max_index = len(moments) - 1
    records: dict[int, dict[tuple[tuple[int, ...], ...], Fraction]] = {}
    for size in range(1, max_index + 2):
        family: dict[tuple[tuple[int, ...], ...], Fraction] = {}
        for rows in combinations(range(max_index + 1), size):
            for columns in combinations(range(max_index + 1), size):
                if rows[-1] + columns[-1] > max_index:
                    continue
                key = canonical_sum_matrix(rows, columns)
                matrix = [
                    [moments[index] for index in row] for row in key
                ]
                value = determinant(matrix)
                prior = family.get(key)
                if prior is not None and prior != value:
                    raise ArithmeticError("canonical Hankel minor changed value")
                family[key] = value
        if family:
            records[size] = family
    return records


def matrix_label(matrix: tuple[tuple[int, ...], ...]) -> str:
    if len(matrix) == 1:
        return f"mu_{matrix[0][0]}"
    if len(matrix) == 2:
        a, b = matrix[0]
        c, d = matrix[1]
        return f"mu_{a}*mu_{d}-mu_{b}*mu_{c}"
    return "det[[" + ";".join(
        ",".join(f"mu_{index}" for index in row) for row in matrix
    ) + "]]"


def serialize_minor_family(
    family: dict[tuple[tuple[int, ...], ...], Fraction]
) -> dict[str, object]:
    return {
        matrix_label(matrix): {
            **signed_record(value),
            "moment_index_matrix": [list(row) for row in matrix],
        }
        for matrix, value in sorted(family.items())
    }


def audit_depth_order13(
    depth: int, derivatives: Sequence[int], reversion_route
) -> dict[str, object]:
    if len(derivatives) != 14:
        raise AssertionError(f"depth {depth}: jet is not contiguous through order 13")
    if any(derivatives[order] for order in range(0, 14, 2)):
        raise AssertionError(f"depth {depth}: parity gate failed")
    odd = {order: derivatives[order] for order in range(1, 14, 2)}
    baseline_a, moments_a = reversion_route(odd)
    baseline_b, moments_b = moments_from_triangular_identity(odd)
    if baseline_a != baseline_b or moments_a != moments_b:
        raise AssertionError(f"depth {depth}: exact moment routes disagree")
    if len(moments_a) != 6:
        raise AssertionError("order 13 must determine exactly six moments")

    hankels = audit_hankels(moments_a)
    if hankels["accessible_matrix_count"] != 6:
        raise AssertionError("six moments must expose six complete Hankel matrices")
    minors = enumerate_accessible_hankel_minors(moments_a)
    expected_counts = {1: 6, 2: 13, 3: 4}
    actual_counts = {size: len(family) for size, family in minors.items()}
    if actual_counts != expected_counts:
        raise AssertionError(
            f"accessible-minor count mismatch: {actual_counts} != {expected_counts}"
        )
    all_values = [value for family in minors.values() for value in family.values()]
    h2_plus = hankels["shifted"]["H_2_plus"]
    return {
        "depth": depth,
        "new_derivative": {
            "F_12": derivatives[12],
            "F_13": derivatives[13],
        },
        "kernel_baseline": signed_record(baseline_a),
        "moments": {
            f"mu_{index}": signed_record(value)
            for index, value in enumerate(moments_a)
        },
        "new_moment_mu_5": signed_record(moments_a[5]),
        "hankel_audit": hankels,
        "new_shifted_H_2_plus": h2_plus,
        "all_unique_accessible_hankel_minors": {
            f"size_{size}": serialize_minor_family(family)
            for size, family in minors.items()
        },
        "unique_minor_counts": actual_counts,
        "unique_scalar_psd_inequalities": 14,
        "all_23_accessible_minors_nonnegative": all(value >= 0 for value in all_values),
        "all_23_accessible_minors_positive": all(value > 0 for value in all_values),
        "moment_routes_agree": True,
        "verdict": (
            "all_accessible_order13_stieltjes_hankel_conditions_pass_strictly"
            if all(value > 0 for value in all_values)
            else "at_least_one_accessible_order13_hankel_minor_is_nonpositive"
        ),
    }


def main() -> int:
    if sha256(INPUT) != EXPECTED_INPUT_SHA256:
        raise AssertionError("accepted order-13 derivative-input SHA-256 changed")
    document = json.loads(INPUT.read_text())
    route = load_reversion_route()
    results = [
        audit_depth_order13(
            int(depth), [int(value) for value in derivatives], route
        )
        for depth, derivatives in sorted(document["derivatives"].items())
    ]
    payload = {
        "format": "identity-order13-stieltjes-audit-v1",
        "model": document["model"],
        "max_feature_derivative_order": 13,
        "kernel_convention": (
            "K(y)=F'(F^{-1}(y))=F'(0)+sum_r (-1)^r mu_r y^(2r+2)"
        ),
        "determined_moments": [
            "mu_0", "mu_1", "mu_2", "mu_3", "mu_4", "mu_5"
        ],
        "depths": results,
        "validation": "passed",
        "next_unavailable_conditions": {
            "mu_6_and_H_3": "require F^(15)(0)",
            "mu_7_and_H_3_plus": "require F^(17)(0)"
        },
        "claim_boundary": (
            "finite order-13 compatibility only; no infinite Stieltjes sequence, "
            "representing measure, convergence, or positive-time claim"
        ),
        "sha256": {
            "input": sha256(INPUT),
            "protocol": sha256(PROTOCOL),
        },
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
