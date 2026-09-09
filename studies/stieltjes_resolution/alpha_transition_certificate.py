#!/usr/bin/env python3
"""Exact six-moment transition certificate on the beta=1 metric ray.

This is a downstream sign audit of the already accepted polynomial jet in
``alpha_interval_certificate.py``.  It does not compute a new neural jet.
All polynomial coefficients are stored in ascending powers of ``alpha``.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Sequence

from alpha_interval_certificate import ODD_JET_COEFFICIENTS
from alpha_interval_tools import (
    CPowerFraction,
    output_kernel_moments_from_jets,
    peval,
    poly,
    primitive_integer_polynomial,
    rat_sum,
)


Q = Fraction
HERE = Path(__file__).resolve().parent
JET_SOURCE = HERE / "alpha_interval_certificate.py"
INTERVAL_SOURCE = HERE / "ALPHA_INTERVAL_CERTIFICATE.json"

# A tight rational isolating interval for the unique positive zero of the
# accepted degree-36 shifted-H2 numerator.
ROOT_LOWER = Q(17_519_225_541_486, 10**15)
ROOT_UPPER = Q(17_519_225_541_487, 10**15)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def determinant(
    matrix: Sequence[Sequence[CPowerFraction]],
) -> CPowerFraction:
    """Exact Leibniz determinant for matrices of size at most three."""

    size = len(matrix)
    if not size or any(len(row) != size for row in matrix):
        raise ValueError("determinant requires a nonempty square matrix")
    c = matrix[0][0].c
    terms: list[CPowerFraction] = []
    for permutation in itertools.permutations(range(size)):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(size)
            for right in range(left + 1, size)
        )
        term = CPowerFraction(poly([1]), 0, c)
        for row, column in enumerate(permutation):
            term = term.mul(matrix[row][column])
        terms.append(term if inversions % 2 == 0 else term.neg())
    return rat_sum(terms, c)


def primitive_record(value: CPowerFraction) -> dict[str, object]:
    primitive = primitive_integer_polynomial(value.numerator)
    first = next(index for index, coefficient in enumerate(primitive) if coefficient)
    scale = value.numerator[first] / primitive[first]
    if scale <= 0:
        raise AssertionError("expected a positive primitive scale")
    if any(
        value.numerator[index] != scale * primitive[index]
        for index in range(len(primitive))
    ):
        raise AssertionError("primitive normalization mismatch")
    return {
        "degree": len(primitive) - 1,
        "denominator_power": value.c_power,
        "coefficient_count": len(primitive),
        "all_primitive_coefficients_strictly_positive": all(
            coefficient > 0 for coefficient in primitive
        ),
        "primitive_signs_ascending": [
            1 if coefficient > 0 else -1 if coefficient < 0 else 0
            for coefficient in primitive
        ],
    }


def build_certificate() -> dict[str, object]:
    jets = [poly(coefficients) for coefficients in ODD_JET_COEFFICIENTS]
    moments = output_kernel_moments_from_jets(jets, 6)
    c = moments[0].c
    if c != poly([63, 48]):
        raise AssertionError("unexpected beta=1 baseline")

    gates: dict[str, CPowerFraction] = {
        f"mu_{index}": moment for index, moment in enumerate(moments)
    }
    for shift, label in ((0, "H"), (1, "H_plus")):
        for size in range(1, 4):
            if 2 * (size - 1) + shift >= len(moments):
                continue
            matrix = [
                [moments[row + column + shift] for column in range(size)]
                for row in range(size)
            ]
            gates[f"{label}_{size - 1}_det"] = determinant(matrix)

    records = {name: primitive_record(value) for name, value in gates.items()}
    exceptional = "H_plus_2_det"
    if not all(
        record["all_primitive_coefficients_strictly_positive"]
        for name, record in records.items()
        if name != exceptional
    ):
        raise AssertionError("a preceding six-moment gate lacks coefficient positivity")

    numerator = primitive_integer_polynomial(gates[exceptional].numerator)
    if not (numerator[0] < 0 and numerator[1] < 0):
        raise AssertionError("shifted-H2 low coefficients changed sign")
    if not all(coefficient > 0 for coefficient in numerator[2:]):
        raise AssertionError("shifted-H2 positive tail changed sign")

    lower_value = peval(poly(numerator), ROOT_LOWER)
    upper_value = peval(poly(numerator), ROOT_UPPER)
    if not (lower_value < 0 < upper_value):
        raise AssertionError("the proposed root bracket is not sign separating")

    # In descending order the signs are +,...,+,-,-, so Descartes' rule gives
    # at most one positive root.  The sign-changing rational bracket gives at
    # least one; therefore it contains the unique positive root.
    records[exceptional].update(
        {
            "constant_and_linear_coefficients_negative": True,
            "coefficients_degree_2_through_36_positive": True,
            "positive_root_count": 1,
            "root_count_proof": "Descartes_one_sign_change_plus_rational_bracket",
        }
    )

    retained_interval = json.loads(INTERVAL_SOURCE.read_text())
    if [str(value) for value in numerator] != retained_interval[
        "primitive_numerator_ascending"
    ]:
        raise AssertionError("retained determinant numerator mismatch")

    return {
        "schema": "beta1_six_moment_transition_v1",
        "scope": {
            "beta": 1,
            "alpha_domain": "alpha>=0",
            "moments": "mu_0,...,mu_5",
            "claim": "finite_prefix_only_not_all_order",
        },
        "provenance": {
            "jet_source": JET_SOURCE.name,
            "jet_source_sha256": sha256(JET_SOURCE),
            "retained_interval_source": INTERVAL_SOURCE.name,
            "retained_interval_source_sha256": sha256(INTERVAL_SOURCE),
        },
        "leading_gate_records": records,
        "unique_positive_transition": {
            "symbol": "alpha_star",
            "exact_definition": "unique positive root of retained primitive P",
            "lower_bound": str(ROOT_LOWER),
            "upper_bound": str(ROOT_UPPER),
            "decimal_display": "0.017519225541486...",
            "P_at_lower_sign": "negative",
            "P_at_upper_sign": "positive",
        },
        "classification": {
            "0<=alpha<alpha_star": "shifted_H2_indefinite",
            "alpha=alpha_star": "all_leading_gates_nonnegative_shifted_H2_singular",
            "alpha>alpha_star": "all_available_ordinary_and_shifted_Hankel_matrices_positive_definite",
        },
    }


def main() -> None:
    print(json.dumps(build_certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
