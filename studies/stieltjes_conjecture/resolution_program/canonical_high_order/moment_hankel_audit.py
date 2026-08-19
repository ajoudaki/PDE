#!/usr/bin/env python3
"""Exact canonical moment/Hankel audit through candidate orders 15 and 17.

This file is deliberately downstream of the feature-jet computation.  It
does not import the Gaussian-program recurrence, the decorated-forest
compiler, or the existing Lagrange-inversion implementation.  Instead it
reconstructs the inverse feature series by direct formal composition using
only the Python standard library and :class:`fractions.Fraction`.

With no arguments, the script checks the retained canonical jet through
``F^(13)(0)``.  ``--f15`` adds the next ordinary 4-by-4 Hankel gate; ``--f17``
requires ``--f15`` and adds the next shifted 4-by-4 gate.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from typing import Callable, Sequence


Q = Fraction

# Entries are F^(2*j+1)(0), j=0,...,6.  Candidate higher derivatives are
# intentionally absent from the retained baseline.
CANONICAL_ODD_DERIVATIVES = (
    Q(111),
    Q(1_685_184),
    Q(77_400_633_120),
    Q(7_315_868_433_079_296),
    Q(1_181_161_141_825_400_561_664),
    Q(291_982_832_387_585_872_335_470_592),
    Q(102_853_512_279_246_664_353_620_526_022_656),
)

EXPECTED_MOMENTS_THROUGH_MU5 = (
    Q(280_864, 4_107),
    Q(38_443_196_932, 5_616_860_517),
    Q(37_578_479_127_292_096, 12_802_987_609_542_045),
    Q(21_749_547_365_571_716_077_696, 13_618_704_359_108_797_313_085),
    Q(
        2_463_577_914_969_508_668_234_788_122_624,
        2_514_423_905_282_563_683_042_386_470_725,
    ),
    Q(
        43_091_400_402_899_303_445_912_484_475_500_496,
        66_714_012_134_145_460_981_362_191_472_284_175,
    ),
)

EXPECTED_ORDINARY_H2 = Q(
    42_273_773_754_433_588_306_428_104_138_747_323_807_188_416_493_518_848,
    2_776_475_335_096_136_409_875_341_498_138_426_752_685_624_541_508_375,
)
EXPECTED_SHIFTED_H2 = Q(
    821_121_994_467_978_760_780_817_399_151_273_570_663_517_173_613_881_280_168_626_780_102_656,
    21_875_165_394_618_842_103_069_584_785_029_512_715_749_438_929_178_771_773_425_620_184_364_845,
)


def parse_fraction(text: str) -> Fraction:
    """Parse a base-10 integer or ``numerator/denominator`` exactly."""

    try:
        return Q(text)
    except (ValueError, ZeroDivisionError) as error:
        raise argparse.ArgumentTypeError(f"not an exact rational: {text}") from error


def fraction_string(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def multiply_series(
    left: Sequence[Fraction], right: Sequence[Fraction], degree: int
) -> list[Fraction]:
    """Multiply ordinary power series modulo ``z**(degree+1)``."""

    result = [Q(0) for _ in range(degree + 1)]
    for left_degree, left_value in enumerate(left[: degree + 1]):
        if not left_value:
            continue
        for right_degree, right_value in enumerate(
            right[: degree + 1 - left_degree]
        ):
            if right_value:
                result[left_degree + right_degree] += left_value * right_value
    return result


def compose_series(
    outer: Sequence[Fraction], inner: Sequence[Fraction], degree: int
) -> list[Fraction]:
    """Return ``outer(inner(z))`` modulo ``z**(degree+1)``."""

    result = [Q(0) for _ in range(degree + 1)]
    power = [Q(1)] + [Q(0) for _ in range(degree)]
    inner_padded = list(inner[: degree + 1])
    inner_padded.extend(Q(0) for _ in range(degree + 1 - len(inner_padded)))
    for exponent, coefficient in enumerate(outer[: degree + 1]):
        if coefficient:
            for index, value in enumerate(power):
                result[index] += coefficient * value
        if exponent != degree:
            power = multiply_series(power, inner_padded, degree)
    return result


def direct_compositional_inverse(
    feature: Sequence[Fraction], degree: int
) -> list[Fraction]:
    """Solve ``feature(inverse(z))=z`` coefficient by coefficient.

    The feature series must have zero constant coefficient and nonzero linear
    coefficient.  At degree ``d``, the unknown inverse coefficient enters the
    composition only as ``feature[1] * inverse[d]``; hence the recurrence is
    exact and triangular.
    """

    if len(feature) < degree + 1:
        raise ValueError("feature series is shorter than the requested degree")
    if feature[0] or not feature[1]:
        raise ValueError("feature series must have zero constant and nonzero slope")

    inverse = [Q(0) for _ in range(degree + 1)]
    for current_degree in range(1, degree + 1):
        inverse[current_degree] = Q(0)
        known = compose_series(feature, inverse, current_degree)[current_degree]
        target = Q(1) if current_degree == 1 else Q(0)
        inverse[current_degree] = (target - known) / feature[1]

    identity = compose_series(feature, inverse, degree)
    expected = [Q(0) for _ in range(degree + 1)]
    expected[1] = Q(1)
    if identity != expected:
        raise AssertionError("formal compositional-reversion identity failed")
    return inverse


def reciprocal_series(series: Sequence[Fraction]) -> list[Fraction]:
    """Return the reciprocal through the final supplied degree."""

    if not series or not series[0]:
        raise ValueError("a reciprocal series needs a nonzero constant term")
    result = [Q(1, 1) / series[0]]
    for degree in range(1, len(series)):
        result.append(
            -sum(series[index] * result[degree - index] for index in range(1, degree + 1))
            / series[0]
        )
    return result


def output_kernel_moments(
    odd_derivatives: Sequence[int | Fraction],
) -> tuple[Fraction, ...]:
    """Map ``F^(1),F^(3),...`` to all determined output-kernel moments.

    If the final input is ``F^(2m+1)(0)``, the result is
    ``(mu_0,...,mu_(m-1))``.  The map is direct series composition, not the
    Lagrange coefficient formula used by the earlier scalar certificate.
    """

    if len(odd_derivatives) < 2:
        raise ValueError("at least F^(1)(0) and F^(3)(0) are required")
    maximum_degree = 2 * len(odd_derivatives) - 1
    feature = [Q(0) for _ in range(maximum_degree + 1)]
    for index, derivative in enumerate(odd_derivatives):
        degree = 2 * index + 1
        feature[degree] = Q(derivative) / math.factorial(degree)

    inverse = direct_compositional_inverse(feature, maximum_degree)
    # If G=F^{-1}, then H(x)=G'(sqrt(x)).
    inverse_derivative = tuple(
        Q(2 * index + 1) * inverse[2 * index + 1]
        for index in range(len(odd_derivatives))
    )
    # K(sqrt(x))=1/H(x)=F'(0)+x*sum_r (-1)^r mu_r x^r.
    kernel = reciprocal_series(inverse_derivative)
    return tuple(
        (-1) ** index * kernel[index + 1]
        for index in range(len(kernel) - 1)
    )


def determinant(matrix: Sequence[Sequence[Fraction]]) -> Fraction:
    """Exact square determinant by rational Gaussian elimination."""

    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("determinant needs a square matrix")
    if not size:
        return Q(1)
    work = [[Q(value) for value in row] for row in matrix]
    sign = 1
    determinant_value = Q(1)
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
        determinant_value *= pivot_value
        for row in range(column + 1, size):
            multiplier = work[row][column] / pivot_value
            for index in range(column + 1, size):
                work[row][index] -= multiplier * work[column][index]
    return sign * determinant_value


def hankel_matrix(
    moments: Sequence[Fraction], size: int, shift: int = 0
) -> tuple[tuple[Fraction, ...], ...]:
    if 2 * (size - 1) + shift >= len(moments):
        raise ValueError("insufficient moments for requested Hankel matrix")
    return tuple(
        tuple(Q(moments[row + column + shift]) for column in range(size))
        for row in range(size)
    )


def principal_minor(
    matrix: Sequence[Sequence[Fraction]], indices: Sequence[int]
) -> Fraction:
    return determinant([[matrix[row][column] for column in indices] for row in indices])


def exact_psd_gate(matrix: Sequence[Sequence[Fraction]]) -> dict[str, object]:
    """Classify a symmetric rational matrix using all principal minors."""

    size = len(matrix)
    if any(matrix[row][column] != matrix[column][row] for row in range(size) for column in range(size)):
        raise ValueError("PSD gate requires a symmetric matrix")
    minors: dict[str, str] = {}
    values: list[Fraction] = []
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
    psd = negative == 0
    if positive_definite:
        decision = "positive_definite"
    elif psd:
        decision = "positive_semidefinite_singular"
    else:
        decision = "not_positive_semidefinite"
    return {
        "size": size,
        "determinant": fraction_string(determinant(matrix)),
        "leading_principal_determinants": [fraction_string(value) for value in leading],
        "principal_minors": minors,
        "negative_principal_minor_count": negative,
        "zero_principal_minor_count": zero,
        "positive_semidefinite": psd,
        "positive_definite": positive_definite,
        "decision": decision,
    }


def affine_data(function: Callable[[Fraction], Fraction]) -> dict[str, str]:
    """Recover and verify an affine rational function from values at 0,1,2."""

    intercept = function(Q(0))
    slope = function(Q(1)) - intercept
    if function(Q(2)) != intercept + 2 * slope:
        raise AssertionError("claimed highest-derivative dependence is not affine")
    result = {
        "intercept": fraction_string(intercept),
        "slope": fraction_string(slope),
    }
    if slope:
        result["zero_threshold"] = fraction_string(-intercept / slope)
    return result


def available_hankel_gates(moments: Sequence[Fraction]) -> dict[str, object]:
    gates: dict[str, object] = {}
    for shift, family in ((0, "ordinary"), (1, "shifted")):
        maximum_size = (len(moments) - shift + 1) // 2
        for size in range(1, maximum_size + 1):
            matrix = hankel_matrix(moments, size, shift)
            gates[f"{family}_H{size - 1}"] = exact_psd_gate(matrix)
    return gates


def next_hankel_schur_threshold(
    known_moments: Sequence[Fraction], size: int, shift: int
) -> Fraction:
    """Return the final-moment threshold for the next Hankel PSD gate.

    All entries of the requested matrix except its bottom-right corner must be
    present.  If its leading block is positive definite, block elimination
    gives ``det(M)=det(B)*(last_moment-threshold)``.  Thus the full matrix is
    PSD exactly when the last moment is at least this threshold.
    """

    final_index = 2 * (size - 1) + shift
    if len(known_moments) != final_index:
        raise ValueError("expected moments exactly through the penultimate index")
    matrix = [
        [
            Q(0)
            if row == size - 1 and column == size - 1
            else Q(known_moments[row + column + shift])
            for column in range(size)
        ]
        for row in range(size)
    ]
    leading = [row[:-1] for row in matrix[:-1]]
    leading_determinant = determinant(leading)
    leading_gate = exact_psd_gate(leading)
    if not leading_gate["positive_definite"]:
        raise ValueError("Schur threshold requires a positive-definite leading block")
    return -determinant(matrix) / leading_determinant


def build_report(
    f15: int | Fraction | None = None,
    f17: int | Fraction | None = None,
) -> dict[str, object]:
    """Build the exact baseline or candidate high-order audit report."""

    if f17 is not None and f15 is None:
        raise ValueError("F^(17)(0) cannot be audited before F^(15)(0) is supplied")
    derivatives = list(CANONICAL_ODD_DERIVATIVES)
    if f15 is not None:
        derivatives.append(Q(f15))
    if f17 is not None:
        derivatives.append(Q(f17))
    moments = output_kernel_moments(derivatives)

    if moments[:6] != EXPECTED_MOMENTS_THROUGH_MU5:
        raise AssertionError("retained canonical mu_0,...,mu_5 cross-check failed")
    ordinary_h2 = determinant(hankel_matrix(moments, 3, shift=0))
    shifted_h2 = determinant(hankel_matrix(moments, 3, shift=1))
    if ordinary_h2 != EXPECTED_ORDINARY_H2 or shifted_h2 != EXPECTED_SHIFTED_H2:
        raise AssertionError("retained canonical 3-by-3 determinant cross-check failed")

    report: dict[str, object] = {
        "schema": "canonical_high_order_moment_hankel_audit_v1",
        "arithmetic": "Python standard-library fractions.Fraction",
        "reversion_method": "direct coefficientwise composition F(G(z))=z",
        "imports_production_recurrence": False,
        "highest_feature_derivative_order": 2 * len(derivatives) - 1,
        "odd_feature_derivatives": {
            str(2 * index + 1): fraction_string(value)
            for index, value in enumerate(derivatives)
        },
        "output_kernel_moments": {
            f"mu_{index}": fraction_string(value)
            for index, value in enumerate(moments)
        },
        "available_hankel_gates": available_hankel_gates(moments),
        "baseline_cross_checks": {
            "mu_0_through_mu_5_match": True,
            "ordinary_H2_matches": True,
            "shifted_H2_matches": True,
        },
    }

    def mu6_for(candidate: Fraction) -> Fraction:
        return output_kernel_moments((*CANONICAL_ODD_DERIVATIVES, candidate))[6]

    def ordinary_h3_for(candidate: Fraction) -> Fraction:
        candidate_moments = output_kernel_moments(
            (*CANONICAL_ODD_DERIVATIVES, candidate)
        )
        return determinant(hankel_matrix(candidate_moments, 4, shift=0))

    report["f15_affine_gate"] = {
        "mu_6_as_function_of_F15": affine_data(mu6_for),
        "det_ordinary_H3_as_function_of_F15": affine_data(ordinary_h3_for),
        "ordinary_H3_mu_6_schur_threshold": fraction_string(
            next_hankel_schur_threshold(moments[:6], size=4, shift=0)
        ),
        "exact_psd_condition": "mu_6 >= ordinary_H3_mu_6_schur_threshold",
        "exact_pd_condition": "mu_6 > ordinary_H3_mu_6_schur_threshold",
        "interpretation": (
            "a negative principal minor of ordinary_H3 disproves canonical V1; "
            "a positive gate is finite-order compatibility only"
        ),
    }

    if f15 is None:
        report["next_required"] = {
            "feature_derivative": "F^(15)(0)",
            "new_moment": "mu_6",
            "new_matrix": "ordinary_H3=(mu_(i+j))_(i,j=0)^3",
        }
        return report

    def mu7_for(candidate: Fraction) -> Fraction:
        return output_kernel_moments((*CANONICAL_ODD_DERIVATIVES, Q(f15), candidate))[7]

    def shifted_h3_for(candidate: Fraction) -> Fraction:
        candidate_moments = output_kernel_moments(
            (*CANONICAL_ODD_DERIVATIVES, Q(f15), candidate)
        )
        return determinant(hankel_matrix(candidate_moments, 4, shift=1))

    report["f17_affine_gate_given_f15"] = {
        "fixed_F15": fraction_string(Q(f15)),
        "mu_7_as_function_of_F17": affine_data(mu7_for),
        "det_shifted_H3_as_function_of_F17": affine_data(shifted_h3_for),
        "shifted_H3_mu_7_schur_threshold": fraction_string(
            next_hankel_schur_threshold(moments[:7], size=4, shift=1)
        ),
        "exact_psd_condition": "mu_7 >= shifted_H3_mu_7_schur_threshold",
        "exact_pd_condition": "mu_7 > shifted_H3_mu_7_schur_threshold",
        "interpretation": (
            "a negative principal minor of shifted_H3 disproves canonical V1; "
            "a positive gate is finite-order compatibility only"
        ),
    }
    ordinary_gate = report["available_hankel_gates"]["ordinary_H3"]
    if not ordinary_gate["positive_semidefinite"]:
        report["candidate_verdict"] = (
            "canonical_V1_disproved_by_ordinary_H3_finite_witness"
        )
    else:
        report["candidate_verdict"] = (
            "prefix_through_mu_6_compatible_canonical_V1_remains_open"
        )
    if f17 is None:
        report["next_required"] = {
            "feature_derivative": "F^(17)(0)",
            "new_moment": "mu_7",
            "new_matrix": "shifted_H3=(mu_(i+j+1))_(i,j=0)^3",
        }
    else:
        shifted_gate = report["available_hankel_gates"]["shifted_H3"]
        if not ordinary_gate["positive_semidefinite"] or not shifted_gate["positive_semidefinite"]:
            verdict = "canonical_V1_disproved_by_finite_Hankel_witness"
        else:
            verdict = "prefix_through_mu_7_compatible_canonical_V1_remains_open"
        report["candidate_verdict"] = verdict
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--f15", type=parse_fraction, help="exact candidate F^(15)(0)")
    parser.add_argument("--f17", type=parse_fraction, help="exact candidate F^(17)(0)")
    parser.add_argument("--compact", action="store_true", help="emit compact JSON")
    arguments = parser.parse_args()
    report = build_report(arguments.f15, arguments.f17)
    print(json.dumps(report, indent=None if arguments.compact else 2, sort_keys=True))


if __name__ == "__main__":
    main()
