#!/usr/bin/env python3
"""Independent exact scalar audit for the canonical hidden observables.

This program is downstream of both hidden-recurrence implementations.  It
does not import either recurrence or the primary hidden-moment postprocessor.
Instead it reconstructs the output coordinate through the even variable

    r = s**2,       x = F(s)**2 = r * A(r)**2,

where ``F(s)=s*A(r)``.  Reverting ``x=r*A(r)**2`` and composing the two hidden
jets gives the squared-RMS moment candidates.  A separate formal square-root
recursion gives the normalized literal-RMS candidates.  All arithmetic is
``fractions.Fraction`` and every accessible Hankel principal minor is tested
exactly.

The first-hidden observable receives one additional independent check from
the Ward identity: its moments obtained by direct composition must equal the
moments obtained by integrating the reciprocal output kernel.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Sequence


Rat = Fraction
HERE = Path(__file__).resolve().parent
PRODUCTION_DEFAULT = HERE / "PRODUCTION_HIDDEN_RESULT.json"
INDEPENDENT_DEFAULT = HERE / "INDEPENDENT_HIDDEN_RESULT.json"


ACCEPTED_FEATURE: tuple[int, ...] = (
    0,
    111,
    0,
    1_685_184,
    0,
    77_400_633_120,
    0,
    7_315_868_433_079_296,
    0,
    1_181_161_141_825_400_561_664,
    0,
    291_982_832_387_585_872_335_470_592,
    0,
    102_853_512_279_246_664_353_620_526_022_656,
    0,
    49_079_184_579_077_107_476_764_629_402_991_788_032,
    0,
    30_555_969_894_096_099_495_444_855_650_521_777_374_167_040,
)

ACCEPTED_Q1_THROUGH_EIGHT: tuple[int, ...] = (
    1,
    0,
    888,
    0,
    13_481_472,
    0,
    619_205_064_960,
    0,
    58_526_947_464_634_368,
)

ACCEPTED_Q2_THROUGH_EIGHT: tuple[int, ...] = (
    3,
    0,
    12_372,
    0,
    311_319_936,
    0,
    19_984_529_682_816,
    0,
    2_441_783_779_120_539_648,
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fraction_string(value: Rat) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def multiply(
    left: Sequence[Rat], right: Sequence[Rat], degree: int
) -> list[Rat]:
    """Multiply ordinary power series through ``degree``."""

    answer = [Rat(0) for _ in range(degree + 1)]
    for i, left_value in enumerate(left[: degree + 1]):
        if not left_value:
            continue
        for j, right_value in enumerate(right[: degree + 1 - i]):
            if right_value:
                answer[i + j] += left_value * right_value
    return answer


def compose(
    outer: Sequence[Rat], inner: Sequence[Rat], degree: int
) -> list[Rat]:
    """Return ``outer(inner(x))`` through ``degree`` for ``inner(0)=0``."""

    if inner and inner[0]:
        raise ValueError("formal composition requires inner(0)=0")
    answer = [Rat(0) for _ in range(degree + 1)]
    power = [Rat(1)] + [Rat(0) for _ in range(degree)]
    for coefficient in outer[: degree + 1]:
        if coefficient:
            for index, value in enumerate(power):
                answer[index] += coefficient * value
        power = multiply(power, inner, degree)
    return answer


def reverse(forward: Sequence[Rat], degree: int) -> list[Rat]:
    """Triangularly reverse a series with zero constant and nonzero slope."""

    if len(forward) < degree + 1:
        raise ValueError("forward series is shorter than the requested inverse")
    if forward[0] or not forward[1]:
        raise ValueError("reversion needs zero constant and nonzero slope")
    inverse = [Rat(0) for _ in range(degree + 1)]
    inverse[1] = 1 / forward[1]
    for current in range(2, degree + 1):
        known = compose(forward, inverse, current)[current]
        inverse[current] = -known / forward[1]
    identity = compose(forward, inverse, degree)
    expected = [Rat(0) for _ in range(degree + 1)]
    expected[1] = Rat(1)
    if identity != expected:
        raise AssertionError("x=r*A(r)^2 reversion identity failed")
    return inverse


def reciprocal(series: Sequence[Rat], degree: int) -> list[Rat]:
    """Return the exact reciprocal of a series through ``degree``."""

    if not series or not series[0]:
        raise ZeroDivisionError("reciprocal series has zero constant")
    padded = list(series[: degree + 1])
    padded.extend(Rat(0) for _ in range(degree + 1 - len(padded)))
    answer = [Rat(0) for _ in range(degree + 1)]
    answer[0] = 1 / padded[0]
    for current in range(1, degree + 1):
        answer[current] = -sum(
            padded[index] * answer[current - index]
            for index in range(1, current + 1)
        ) / padded[0]
    product = multiply(padded, answer, degree)
    if product != [Rat(1)] + [Rat(0) for _ in range(degree)]:
        raise AssertionError("reciprocal identity failed")
    return answer


def normalized_square_root(series: Sequence[Rat]) -> list[Rat]:
    """Square-root a rational series whose constant coefficient is one."""

    if not series or series[0] != 1:
        raise ValueError("normalized square root requires constant one")
    answer = [Rat(1)]
    for current in range(1, len(series)):
        quadratic = sum(
            answer[index] * answer[current - index]
            for index in range(1, current)
        )
        answer.append((series[current] - quadratic) / 2)
    if multiply(answer, answer, len(series) - 1) != list(series):
        raise AssertionError("formal square-root identity failed")
    return answer


def determinant(matrix: Sequence[Sequence[Rat]]) -> Rat:
    """Exact determinant by a pivoted rational elimination."""

    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("determinant requires a square matrix")
    if not size:
        return Rat(1)
    work = [[Rat(value) for value in row] for row in matrix]
    sign = 1
    result = Rat(1)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column]),
            None,
        )
        if pivot is None:
            return Rat(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign *= -1
        pivot_value = work[column][column]
        result *= pivot_value
        for row in range(column + 1, size):
            multiplier = work[row][column] / pivot_value
            for index in range(column + 1, size):
                work[row][index] -= multiplier * work[column][index]
    return sign * result


def principal_minor(
    matrix: Sequence[Sequence[Rat]], indices: Sequence[int]
) -> Rat:
    return determinant(
        [[matrix[row][column] for column in indices] for row in indices]
    )


def audit_matrix(matrix: Sequence[Sequence[Rat]]) -> dict[str, object]:
    """Test all principal minors, not only the leading determinant."""

    size = len(matrix)
    if any(
        matrix[row][column] != matrix[column][row]
        for row in range(size)
        for column in range(size)
    ):
        raise ValueError("Hankel audit received a nonsymmetric matrix")
    minors: dict[str, str] = {}
    values: list[Rat] = []
    for order in range(1, size + 1):
        for indices in itertools.combinations(range(size), order):
            value = principal_minor(matrix, indices)
            minors[",".join(str(index) for index in indices)] = fraction_string(value)
            values.append(value)
    leading = [
        determinant([list(row[:order]) for row in matrix[:order]])
        for order in range(1, size + 1)
    ]
    negative = sum(value < 0 for value in values)
    zero = sum(value == 0 for value in values)
    positive_definite = all(value > 0 for value in leading)
    positive_semidefinite = negative == 0
    return {
        "size": size,
        "entries": [[fraction_string(value) for value in row] for row in matrix],
        "determinant": fraction_string(determinant(matrix)),
        "leading_principal_determinants": [
            fraction_string(value) for value in leading
        ],
        "principal_minors": minors,
        "principal_minor_count": len(values),
        "negative_principal_minor_count": negative,
        "zero_principal_minor_count": zero,
        "all_principal_minors_strictly_positive": all(value > 0 for value in values),
        "positive_semidefinite": positive_semidefinite,
        "positive_definite": positive_definite,
        "decision": (
            "positive_definite"
            if positive_definite
            else "positive_semidefinite_singular"
            if positive_semidefinite
            else "not_positive_semidefinite"
        ),
    }


def audit_hankels(moments: Sequence[Rat]) -> dict[str, object]:
    """Build every ordinary and shifted Hankel matrix allowed by ``moments``."""

    families: dict[str, dict[str, object]] = {"ordinary": {}, "shifted": {}}
    for shift, family in ((0, "ordinary"), (1, "shifted")):
        size = 1
        while 2 * (size - 1) + shift < len(moments):
            matrix = [
                [moments[row + column + shift] for column in range(size)]
                for row in range(size)
            ]
            label = f"H{size - 1}" + ("_plus" if shift else "")
            families[family][label] = audit_matrix(matrix)
            size += 1
    records = [
        record
        for family in families.values()
        for record in family.values()
    ]
    return {
        **families,
        "accessible_matrix_count": len(records),
        "accessible_principal_minor_count": sum(
            int(record["principal_minor_count"]) for record in records
        ),
        "all_accessible_matrices_positive_semidefinite": all(
            bool(record["positive_semidefinite"]) for record in records
        ),
        "all_accessible_matrices_positive_definite": all(
            bool(record["positive_definite"]) for record in records
        ),
        "all_accessible_principal_minors_strictly_positive": all(
            bool(record["all_principal_minors_strictly_positive"])
            for record in records
        ),
    }


def parse_derivatives(document: dict[str, object], key: str) -> list[int]:
    raw = document.get(key)
    if not isinstance(raw, dict):
        raise ValueError(f"{key} is not a string-keyed derivative map")
    parsed: dict[int, int] = {}
    for raw_order, raw_value in raw.items():
        order = int(raw_order)
        value = Rat(str(raw_value))
        if value.denominator != 1:
            raise ValueError(f"{key}[{order}] is not integral: {value}")
        parsed[order] = value.numerator
    if sorted(parsed) != list(range(len(parsed))):
        raise ValueError(f"{key} orders are not contiguous from zero")
    return [parsed[order] for order in range(len(parsed))]


def _source_hash_gate(document: dict[str, object], expected_path: Path) -> bool:
    source = document.get("source")
    if not isinstance(source, dict) or "sha256" not in source:
        return False
    return str(source["sha256"]) == sha256(expected_path)


def _all_boolean_gates_true(document: dict[str, object]) -> bool:
    gates = document.get("gates")
    return isinstance(gates, dict) and bool(gates) and all(
        value is True for value in gates.values()
    )


def _hidden_moments(
    observable_in_x: Sequence[Rat], baseline: Rat
) -> tuple[list[Rat], list[Rat]]:
    if observable_in_x[0] != baseline:
        raise AssertionError(
            f"hidden baseline mismatch: {observable_in_x[0]} != {baseline}"
        )
    squared = [
        ((-1) ** index) * observable_in_x[index + 1]
        for index in range(len(observable_in_x) - 1)
    ]
    normalized = [value / baseline for value in observable_in_x]
    root = normalized_square_root(normalized)
    literal = [
        ((-1) ** index) * root[index + 1]
        for index in range(len(root) - 1)
    ]
    return squared, literal


def audit_documents(
    production_path: Path, independent_path: Path
) -> dict[str, object]:
    production = json.loads(production_path.read_text())
    independent = json.loads(independent_path.read_text())
    expected_schemas = {
        "production": "production_canonical_hidden_recurrence_v1",
        "independent": "independent_canonical_hidden_recurrence_v1",
    }
    schemas = {
        "production": production.get("schema"),
        "independent": independent.get("schema"),
    }
    if schemas != expected_schemas:
        raise AssertionError(f"unexpected recurrence schemas: {schemas}")

    production_series = {
        key: parse_derivatives(production, key)
        for key in ("feature_derivatives", "q1_derivatives", "q2_derivatives")
    }
    independent_series = {
        key: parse_derivatives(independent, key)
        for key in ("feature_derivatives", "q1_derivatives", "q2_derivatives")
    }
    if production_series != independent_series:
        differing = [
            key
            for key in production_series
            if production_series[key] != independent_series[key]
        ]
        raise AssertionError(
            "production and independent hidden jets differ: " + ", ".join(differing)
        )

    feature = production_series["feature_derivatives"]
    q1_recurrence = production_series["q1_derivatives"]
    q2 = production_series["q2_derivatives"]
    if tuple(feature) != ACCEPTED_FEATURE:
        raise AssertionError("feature jet does not equal the accepted order-17 jet")
    if len(q1_recurrence) != 17 or len(q2) != 17:
        raise AssertionError("both recurrence hidden jets must end at order sixteen")
    if tuple(q1_recurrence[:9]) != ACCEPTED_Q1_THROUGH_EIGHT:
        raise AssertionError("Q1 does not reproduce the accepted Campaign-1 prefix")
    if tuple(q2[:9]) != ACCEPTED_Q2_THROUGH_EIGHT:
        raise AssertionError("Q2 does not reproduce the accepted Campaign-1 prefix")
    if any(feature[order] for order in range(0, 18, 2)):
        raise AssertionError("feature parity failed")
    if any(q1_recurrence[order] for order in range(1, 17, 2)):
        raise AssertionError("Q1 parity failed")
    if any(q2[order] for order in range(1, 17, 2)):
        raise AssertionError("Q2 parity failed")
    if any(q1_recurrence[k] != 8 * feature[k - 1] for k in range(1, 17)):
        raise AssertionError("Q1 Ward identity failed on the recurrence output")

    # Ward extends Q1 two orders beyond the explicit hidden contractions.
    q1 = [1] + [8 * feature[order - 1] for order in range(1, 19)]
    if q1[:17] != q1_recurrence:
        raise AssertionError("Ward-extended Q1 disagrees with the recurrence prefix")

    # F(s)=s*A(r), r=s^2.  The last F17 coefficient determines A through r^8.
    a = [
        Rat(feature[2 * index + 1], math.factorial(2 * index + 1))
        for index in range(9)
    ]
    a_squared = multiply(a, a, 8)
    forward_x = [Rat(0)] + a_squared
    reverse_r = reverse(forward_x, 9)

    b1 = [
        Rat(q1[2 * index], math.factorial(2 * index))
        for index in range(10)
    ]
    b2 = [
        Rat(q2[2 * index], math.factorial(2 * index))
        for index in range(9)
    ]
    n1 = compose(b1, reverse_r, 9)
    n2 = compose(b2, reverse_r, 8)
    q1_squared, q1_literal = _hidden_moments(n1, Rat(1))
    q2_squared, q2_literal = _hidden_moments(n2, Rat(3))

    # Algebraically distinct Q1 route: K(F(s))=F'(s)=A(r)+2rA'(r).
    k_in_r = [Rat(2 * index + 1) * value for index, value in enumerate(a)]
    k_in_x = compose(k_in_r, reverse_r, 8)
    inverse_k = reciprocal(k_in_x, 8)
    q1_from_ward = [
        Rat(4, index + 1) * ((-1) ** index) * inverse_k[index]
        for index in range(9)
    ]
    if q1_from_ward != q1_squared:
        raise AssertionError(
            "direct Q1 composition disagrees with reciprocal-kernel Ward route"
        )

    families = {
        "q1_squared_rms": {
            "baseline": "1",
            "moment_symbol": "nu1",
            "moments": q1_squared,
            "literal_scale": "1",
        },
        "q1_normalized_literal_rms": {
            "baseline": "1",
            "moment_symbol": "omega1",
            "moments": q1_literal,
            "literal_scale": "1",
        },
        "q2_squared_rms": {
            "baseline": "3",
            "moment_symbol": "nu2",
            "moments": q2_squared,
            "literal_scale": "1",
        },
        "q2_normalized_literal_rms": {
            "baseline": "1",
            "moment_symbol": "omega2",
            "moments": q2_literal,
            "literal_scale": "sqrt(3)",
        },
    }
    serialized_families: dict[str, object] = {}
    all_psd = True
    all_pd = True
    for name, record in families.items():
        moments = record.pop("moments")
        hankels = audit_hankels(moments)
        all_psd = all_psd and bool(
            hankels["all_accessible_matrices_positive_semidefinite"]
        )
        all_pd = all_pd and bool(
            hankels["all_accessible_matrices_positive_definite"]
        )
        serialized_families[name] = {
            **record,
            "moment_count": len(moments),
            "moments": [fraction_string(value) for value in moments],
            "all_moments_strictly_positive": all(value > 0 for value in moments),
            "hankels": hankels,
        }

    source_gates = {
        "production_result_source_hash_matches_current_source": _source_hash_gate(
            production, HERE / "production_hidden_recurrence.py"
        ),
        "independent_result_source_hash_matches_current_source": _source_hash_gate(
            independent, HERE / "independent_hidden_recurrence.py"
        ),
        "production_embedded_gates_all_true": _all_boolean_gates_true(production),
        "independent_embedded_gates_all_true": _all_boolean_gates_true(independent),
    }
    if not all(source_gates.values()):
        failed = [name for name, passed in source_gates.items() if not passed]
        raise AssertionError("input provenance gate failed: " + ", ".join(failed))

    return {
        "schema": "independent_canonical_hidden_scalar_audit_v1",
        "arithmetic": "exact fractions.Fraction",
        "route": "reverse x=r*A(r)^2, then compose B_j(r(x))",
        "inputs": {
            "production": {
                "path": str(production_path),
                "sha256": sha256(production_path),
                "schema": schemas["production"],
            },
            "independent": {
                "path": str(independent_path),
                "sha256": sha256(independent_path),
                "schema": schemas["independent"],
            },
        },
        "source": {
            "path": str(Path(__file__).resolve()),
            "sha256": sha256(Path(__file__).resolve()),
        },
        "gates": {
            **source_gates,
            "two_recurrence_jets_match_exactly": True,
            "accepted_feature_jet_through_F17": True,
            "accepted_campaign1_hidden_prefixes": True,
            "feature_and_hidden_parity": True,
            "q1_ward_extension_through_order18": True,
            "x_rA2_reversion_identity": True,
            "q1_direct_and_reciprocal_ward_moments_match": True,
            "literal_rms_square_identities": True,
            "all_accessible_hidden_hankels_psd": all_psd,
            "all_accessible_hidden_hankels_pd": all_pd,
        },
        "construction": {
            "A_coefficients_in_r": [fraction_string(value) for value in a],
            "x_coefficients_in_r": [
                fraction_string(value) for value in forward_x
            ],
            "r_coefficients_in_x": [
                fraction_string(value) for value in reverse_r
            ],
            "N1_coefficients_in_x": [fraction_string(value) for value in n1],
            "N2_coefficients_in_x": [fraction_string(value) for value in n2],
            "inverse_K_coefficients_in_x": [
                fraction_string(value) for value in inverse_k
            ],
        },
        "families": serialized_families,
        "result": (
            "all four squared/normalized-literal hidden moment prefixes are "
            "strictly positive and every accessible ordinary/shifted Hankel "
            "matrix is positive definite"
            if all_pd
            else "at least one accessible hidden Hankel matrix is not positive definite"
        ),
        "interpretation_limit": (
            "finite fixed-order width-limit compatibility only; this audit "
            "does not prove an all-order Stieltjes representation or a "
            "positive-time mean-field identification"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--production", type=Path, default=PRODUCTION_DEFAULT)
    parser.add_argument("--independent", type=Path, default=INDEPENDENT_DEFAULT)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    document = audit_documents(args.production, args.independent)
    encoded = json.dumps(document, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        sys.stdout.write(encoded)
    else:
        args.output.write_text(encoded)
        print(f"wrote {args.output} sha256={sha256(args.output)}", file=sys.stderr)


if __name__ == "__main__":
    main()
