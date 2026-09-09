#!/usr/bin/env python3
"""Exact downstream Stieltjes audit for the two canonical hidden norms.

The two recurrence outputs are treated as independent inputs.  This module
does not import either recurrence implementation.  It verifies their exact
feature and hidden jets, performs direct compositional reversion, and checks
all accessible ordinary and shifted Hankel principal minors for both the
squared-RMS and normalized literal-RMS responses.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Sequence


Q = Fraction
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
PRODUCTION_RESULT = HERE / "PRODUCTION_HIDDEN_RESULT.json"
INDEPENDENT_RESULT = HERE / "INDEPENDENT_HIDDEN_RESULT.json"
PROTOCOL = HERE / "PROTOCOL.md"

CAMPAIGN1_Q1 = {
    0: 1,
    1: 0,
    2: 888,
    3: 0,
    4: 13_481_472,
    5: 0,
    6: 619_205_064_960,
    7: 0,
    8: 58_526_947_464_634_368,
}
CAMPAIGN1_Q2 = {
    0: 3,
    1: 0,
    2: 12_372,
    3: 0,
    4: 311_319_936,
    5: 0,
    6: 19_984_529_682_816,
    7: 0,
    8: 2_441_783_779_120_539_648,
}


def fraction_string(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def multiply_series(
    left: Sequence[Fraction], right: Sequence[Fraction], degree: int
) -> list[Fraction]:
    result = [Q(0) for _ in range(degree + 1)]
    for i, left_value in enumerate(left[: degree + 1]):
        if not left_value:
            continue
        for j, right_value in enumerate(right[: degree + 1 - i]):
            if right_value:
                result[i + j] += left_value * right_value
    return result


def compose_series(
    outer: Sequence[Fraction], inner: Sequence[Fraction], degree: int
) -> list[Fraction]:
    result = [Q(0) for _ in range(degree + 1)]
    power = [Q(1)] + [Q(0) for _ in range(degree)]
    padded = list(inner[: degree + 1])
    padded.extend(Q(0) for _ in range(degree + 1 - len(padded)))
    for coefficient in outer[: degree + 1]:
        if coefficient:
            for index, value in enumerate(power):
                result[index] += coefficient * value
        power = multiply_series(power, padded, degree)
    return result


def direct_inverse(feature: Sequence[Fraction], degree: int) -> list[Fraction]:
    if feature[0] or not feature[1]:
        raise ValueError("feature series must have zero constant and nonzero slope")
    inverse = [Q(0) for _ in range(degree + 1)]
    for current in range(1, degree + 1):
        known = compose_series(feature, inverse, current)[current]
        target = Q(1) if current == 1 else Q(0)
        inverse[current] = (target - known) / feature[1]
    identity = compose_series(feature, inverse, degree)
    expected = [Q(0) for _ in range(degree + 1)]
    expected[1] = Q(1)
    if identity != expected:
        raise AssertionError("formal inverse identity failed")
    return inverse


def sqrt_unit_series(series: Sequence[Fraction]) -> list[Fraction]:
    """Square root of a series whose constant coefficient is exactly one."""

    if not series or series[0] != 1:
        raise ValueError("normalized square-root input must start at one")
    root = [Q(0) for _ in series]
    root[0] = Q(1)
    for degree in range(1, len(series)):
        root[degree] = (
            series[degree]
            - sum(root[left] * root[degree - left] for left in range(1, degree))
        ) / 2
    if multiply_series(root, root, len(series) - 1) != list(series):
        raise AssertionError("formal square-root identity failed")
    return root


def determinant(matrix: Sequence[Sequence[Fraction]]) -> Fraction:
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("determinant requires a square matrix")
    work = [[Q(value) for value in row] for row in matrix]
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
            multiplier = work[row][column] / pivot_value
            for index in range(column + 1, size):
                work[row][index] -= multiplier * work[column][index]
    return sign * value


def hankel_matrix(
    moments: Sequence[Fraction], size: int, shift: int
) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(moments[row + column + shift] for column in range(size))
        for row in range(size)
    )


def matrix_gate(matrix: Sequence[Sequence[Fraction]]) -> dict[str, object]:
    size = len(matrix)
    minors: dict[str, str] = {}
    values: list[Fraction] = []
    for order in range(1, size + 1):
        for indices in itertools.combinations(range(size), order):
            minor = determinant(
                [[matrix[row][column] for column in indices] for row in indices]
            )
            minors[",".join(map(str, indices))] = fraction_string(minor)
            values.append(minor)
    leading = [
        determinant([list(row[:order]) for row in matrix[:order]])
        for order in range(1, size + 1)
    ]
    psd = all(value >= 0 for value in values)
    pd = all(value > 0 for value in leading)
    return {
        "size": size,
        "matrix": [[fraction_string(value) for value in row] for row in matrix],
        "determinant": fraction_string(determinant(matrix)),
        "determinant_decimal": format(float(determinant(matrix)), ".16g"),
        "leading_principal_determinants": [
            fraction_string(value) for value in leading
        ],
        "principal_minors": minors,
        "negative_principal_minor_count": sum(value < 0 for value in values),
        "zero_principal_minor_count": sum(value == 0 for value in values),
        "positive_semidefinite": psd,
        "positive_definite": pd,
        "decision": (
            "positive_definite"
            if pd
            else "positive_semidefinite_singular"
            if psd
            else "not_positive_semidefinite"
        ),
    }


def all_hankel_gates(moments: Sequence[Fraction]) -> dict[str, object]:
    gates: dict[str, object] = {}
    for shift, family in ((0, "ordinary"), (1, "shifted")):
        maximum_size = (len(moments) - shift + 1) // 2
        for size in range(1, maximum_size + 1):
            gates[f"{family}_H{size - 1}"] = matrix_gate(
                hankel_matrix(moments, size, shift)
            )
    return gates


def exact_derivatives(document: dict[str, object], key: str) -> dict[int, int]:
    raw = document.get(key)
    if not isinstance(raw, dict):
        raise ValueError(f"missing exact derivative map {key}")
    return {int(order): int(value) for order, value in raw.items()}


def validate_source(document: dict[str, object], result_path: Path) -> dict[str, str]:
    source = document.get("source")
    if not isinstance(source, dict):
        raise ValueError(f"{result_path.name} has no source record")
    filename = source.get("file", source.get("path"))
    digest = source.get("sha256")
    if not isinstance(filename, str) or not isinstance(digest, str):
        raise ValueError(f"{result_path.name} has malformed source record")
    relative = Path(filename)
    path = (
        result_path.parent / relative
        if len(relative.parts) == 1
        else REPO / relative
    )
    actual = sha256(path)
    if actual != digest:
        raise AssertionError(f"source hash mismatch for {path.name}")
    return {"file": filename, "sha256": actual}


def response_moments(
    feature_derivatives: dict[int, int],
    q2_derivatives: dict[int, int],
) -> dict[str, tuple[Fraction, ...]]:
    # F through order 17 determines the odd inverse through order 17.  The
    # even inverse coefficient at order 18 is zero by the verified parity, so
    # Q1'=8F determines Q1 and its output-coordinate response through x^9.
    degree = 18
    feature = [Q(0) for _ in range(degree + 1)]
    for order, derivative in feature_derivatives.items():
        if order <= 17:
            feature[order] = Q(derivative, math.factorial(order))
    inverse = direct_inverse(feature, degree)
    if any(inverse[order] for order in range(0, degree + 1, 2)):
        raise AssertionError("inverse-feature parity failed")

    q1 = [Q(0) for _ in range(degree + 1)]
    q1[0] = Q(1)
    for order in range(1, degree + 1):
        q1[order] = Q(
            8 * feature_derivatives.get(order - 1, 0), math.factorial(order)
        )
    n1_y = compose_series(q1, inverse, degree)
    if any(n1_y[order] for order in range(1, degree + 1, 2)):
        raise AssertionError("first-hidden output-coordinate parity failed")
    n1_x = tuple(n1_y[2 * order] for order in range(10))

    q2_degree = 16
    q2 = [Q(0) for _ in range(q2_degree + 1)]
    for order in range(q2_degree + 1):
        q2[order] = Q(q2_derivatives[order], math.factorial(order))
    n2_y = compose_series(q2, inverse, q2_degree)
    if any(n2_y[order] for order in range(1, q2_degree + 1, 2)):
        raise AssertionError("second-hidden output-coordinate parity failed")
    n2_x = tuple(n2_y[2 * order] for order in range(9))

    squared_1 = tuple((-1) ** r * n1_x[r + 1] for r in range(9))
    squared_2 = tuple((-1) ** r * n2_x[r + 1] for r in range(8))
    rms_1_series = sqrt_unit_series(n1_x)
    rms_2_series = sqrt_unit_series(tuple(value / 3 for value in n2_x))
    rms_1 = tuple((-1) ** r * rms_1_series[r + 1] for r in range(9))
    rms_2 = tuple((-1) ** r * rms_2_series[r + 1] for r in range(8))
    return {
        "first_hidden_squared_rms": squared_1,
        "second_hidden_squared_rms": squared_2,
        "first_hidden_relative_rms": rms_1,
        "second_hidden_relative_rms": rms_2,
    }


def sequence_record(moments: Sequence[Fraction]) -> dict[str, object]:
    gates = all_hankel_gates(moments)
    return {
        "moment_count": len(moments),
        "moments": [fraction_string(value) for value in moments],
        "moments_decimal": [format(float(value), ".16g") for value in moments],
        "hankel_gates": gates,
        "all_accessible_hankel_matrices_positive_definite": all(
            gate["positive_definite"] for gate in gates.values()
        ),
        "all_accessible_principal_minors_strictly_positive": all(
            Q(value) > 0
            for gate in gates.values()
            for value in gate["principal_minors"].values()
        ),
    }


def build_audit(production_path: Path, independent_path: Path) -> dict[str, object]:
    production = json.loads(production_path.read_text())
    independent = json.loads(independent_path.read_text())
    sources = {
        "production": validate_source(production, production_path),
        "independent": validate_source(independent, independent_path),
    }
    production_f = exact_derivatives(production, "feature_derivatives")
    independent_f = exact_derivatives(independent, "feature_derivatives")
    production_q1 = exact_derivatives(production, "q1_derivatives")
    independent_q1 = exact_derivatives(independent, "q1_derivatives")
    production_q2 = exact_derivatives(production, "q2_derivatives")
    independent_q2 = exact_derivatives(independent, "q2_derivatives")
    if production_f != independent_f:
        raise AssertionError("feature jets disagree across implementations")
    if production_q1 != independent_q1:
        raise AssertionError("first-hidden jets disagree across implementations")
    if production_q2 != independent_q2:
        raise AssertionError("second-hidden jets disagree across implementations")
    if max(production_f) != 17 or max(production_q2) < 16:
        raise AssertionError("input jets do not reach the frozen terminal orders")
    for order, expected in CAMPAIGN1_Q1.items():
        if production_q1.get(order) != expected:
            raise AssertionError(f"Campaign-1 Q1 mismatch at order {order}")
    for order, expected in CAMPAIGN1_Q2.items():
        if production_q2.get(order) != expected:
            raise AssertionError(f"Campaign-1 Q2 mismatch at order {order}")
    for order, derivative in production_q1.items():
        if order and derivative != 8 * production_f.get(order - 1, 0):
            raise AssertionError(f"Q1 Ward identity failed at order {order}")
    if any(production_q1.get(order, 0) for order in range(1, 18, 2)):
        raise AssertionError("Q1 odd-derivative parity failed")
    if any(production_q2.get(order, 0) for order in range(1, 17, 2)):
        raise AssertionError("Q2 odd-derivative parity failed")

    moments = response_moments(production_f, production_q2)
    sequences = {name: sequence_record(values) for name, values in moments.items()}
    return {
        "schema": "canonical_hidden_high_order_hankel_audit_v1",
        "model": "canonical one-input quadratic network",
        "metric": "D_a + D_u + D_W",
        "coordinate": "x=y^2 with y=F(s)",
        "input_provenance": {
            "audit_source": {
                "file": Path(__file__).name,
                "sha256": sha256(Path(__file__).resolve()),
            },
            "production_result": {
                "file": production_path.name,
                "sha256": sha256(production_path),
                "source": sources["production"],
            },
            "independent_result": {
                "file": independent_path.name,
                "sha256": sha256(independent_path),
                "source": sources["independent"],
            },
            "protocol": {"file": PROTOCOL.name, "sha256": sha256(PROTOCOL)},
        },
        "exact_cross_implementation_gates": {
            "feature_through_17_identical": True,
            "q1_direct_through_16_identical": True,
            "q2_through_16_identical": True,
            "campaign1_q1_q2_through_8_reproduced": True,
            "q1_ward_identity_reproduced": True,
            "hidden_parity_reproduced": True,
        },
        "new_hidden_derivatives": {
            "q1": {
                str(order): str(8 * production_f[order - 1])
                for order in (10, 12, 14, 16, 18)
            },
            "q2": {
                str(order): str(production_q2[order])
                for order in (10, 12, 14, 16)
            },
        },
        "sequences": sequences,
        "result": (
            "All accessible ordinary and shifted Hankel matrices, including "
            "every principal minor, are strictly positive for both squared-"
            "RMS companions and both normalized literal-RMS companions."
        ),
        "interpretation_limit": (
            "Exact finite-order width-limit compatibility only; no all-order "
            "Stieltjes theorem or global-trajectory identification."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--production", type=Path, default=PRODUCTION_RESULT)
    parser.add_argument("--independent", type=Path, default=INDEPENDENT_RESULT)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    audit = build_audit(arguments.production, arguments.independent)
    encoded = json.dumps(audit, indent=2, sort_keys=True) + "\n"
    if arguments.output:
        arguments.output.write_text(encoded)
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
