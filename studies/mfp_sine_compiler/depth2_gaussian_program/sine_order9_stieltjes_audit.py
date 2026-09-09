#!/usr/bin/env python3
"""High-precision four-moment Stieltjes audit for the sine order-nine jets."""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Sequence

import mpmath as mp


HERE = Path(__file__).resolve().parent
INPUT = HERE / "results_order9.json"
PROTOCOL = HERE / "ORDER9_PROTOCOL.md"
ENGINE = HERE / "sine_order9_fourier_jet.py"
EXPECTED_SHA256 = {
    "input": "46b19909db25be639bfca3458c62da0784f7596566823725c80e7c4741152658",
    "protocol": "366ae94d52a4b4aa7d741f807f4afe4e05a4a014e2f408837c4301ff0402bb37",
    "engine": "4f71512d8f8990a8db0faf9d2f3e0b8db879ecb51c9d83afc78488c5eb602221",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def multiply_series(
    left: Sequence[mp.mpf], right: Sequence[mp.mpf], degree: int
) -> list[mp.mpf]:
    result = [mp.mpf(0) for _ in range(degree + 1)]
    for left_degree, left_value in enumerate(left):
        if left_degree > degree or not left_value:
            continue
        for right_degree, right_value in enumerate(right):
            total_degree = left_degree + right_degree
            if total_degree > degree:
                break
            if right_value:
                result[total_degree] += left_value * right_value
    return result


def power_series(
    series: Sequence[mp.mpf], exponent: int, degree: int
) -> list[mp.mpf]:
    result = [mp.mpf(1)] + [mp.mpf(0) for _ in range(degree)]
    base = list(series[: degree + 1])
    base += [mp.mpf(0)] * max(0, degree + 1 - len(base))
    for _ in range(exponent):
        result = multiply_series(result, base, degree)
    return result


def compose_series(
    outer: Sequence[mp.mpf], inner: Sequence[mp.mpf], degree: int
) -> list[mp.mpf]:
    result = [mp.mpf(0) for _ in range(degree + 1)]
    current_power = [mp.mpf(1)] + [mp.mpf(0) for _ in range(degree)]
    for exponent, coefficient in enumerate(outer):
        if exponent > degree:
            break
        if coefficient:
            for index, value in enumerate(current_power):
                result[index] += coefficient * value
        current_power = multiply_series(current_power, inner, degree)
    return result


def inverse_series(feature: Sequence[mp.mpf], degree: int) -> list[mp.mpf]:
    """Revert ``feature`` using its triangular linear coefficient."""

    if not feature[1]:
        raise ArithmeticError("feature series has zero linear coefficient")
    inverse = [mp.mpf(0) for _ in range(degree + 1)]
    inverse[1] = 1 / feature[1]
    for order in range(2, degree + 1):
        known = compose_series(feature, inverse, order)[order]
        inverse[order] = -known / feature[1]
    return inverse


def feature_series(derivatives: Sequence[mp.mpf]) -> list[mp.mpf]:
    return [
        derivative / math.factorial(order)
        for order, derivative in enumerate(derivatives)
    ]


def moments_by_reversion(
    derivatives: Sequence[mp.mpf], max_kernel_degree: int = 8
) -> tuple[mp.mpf, tuple[mp.mpf, ...], list[mp.mpf]]:
    """Compute ``F'(F^{-1}(y))`` by explicit reversion/composition."""

    feature = feature_series(derivatives)
    inverse = inverse_series(feature, max_kernel_degree)
    feature_prime = [
        derivatives[order + 1] / math.factorial(order)
        for order in range(max_kernel_degree + 1)
    ]
    kernel = compose_series(feature_prime, inverse, max_kernel_degree)
    moments = tuple(
        (-1) ** index * kernel[2 * index + 2]
        for index in range(max_kernel_degree // 2)
    )
    return kernel[0], moments, kernel


def moments_by_triangular_identity(
    derivatives: Sequence[mp.mpf], max_kernel_degree: int = 8
) -> tuple[mp.mpf, tuple[mp.mpf, ...], dict[int, mp.mpf]]:
    """Solve ``F'(t)=K(F(t))`` without reverting the feature series."""

    feature = feature_series(derivatives)
    feature_prime = [
        derivatives[order + 1] / math.factorial(order)
        for order in range(max_kernel_degree + 1)
    ]
    kernel_terms: dict[int, mp.mpf] = {}
    for power in range(2, max_kernel_degree + 1, 2):
        target = feature_prime[power]
        explained = mp.fsum(
            coefficient * power_series(feature, prior_power, power)[power]
            for prior_power, coefficient in kernel_terms.items()
        )
        leading = power_series(feature, power, power)[power]
        if not leading:
            raise ArithmeticError("triangular solve lost its leading term")
        kernel_terms[power] = (target - explained) / leading
    moments = tuple(
        (-1) ** index * kernel_terms[2 * index + 2]
        for index in range(max_kernel_degree // 2)
    )
    return derivatives[1], moments, kernel_terms


def relative_error(left: mp.mpf, right: mp.mpf) -> mp.mpf:
    return abs(left - right) / max(mp.mpf(1), abs(left), abs(right))


def sign(value: mp.mpf) -> str:
    return "positive" if value > 0 else "negative" if value < 0 else "zero"


def matrix_eigenvalues_2x2(matrix: Sequence[Sequence[mp.mpf]]) -> list[mp.mpf]:
    a, b = matrix[0]
    c = matrix[1][1]
    discriminant = mp.sqrt((a - c) ** 2 + 4 * b * b)
    return sorted(((a + c - discriminant) / 2, (a + c + discriminant) / 2))


def audit_matrix(matrix: list[list[mp.mpf]]) -> dict[str, object]:
    if len(matrix) == 1:
        minors = {"0": matrix[0][0]}
        eigenvalues = [matrix[0][0]]
    elif len(matrix) == 2:
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] ** 2
        minors = {
            "0": matrix[0][0],
            "1": matrix[1][1],
            "0,1": determinant,
        }
        eigenvalues = matrix_eigenvalues_2x2(matrix)
    else:
        raise ValueError("this order-nine audit only exposes 1x1 and 2x2 matrices")
    return {
        "matrix": [[mp.nstr(value, 70) for value in row] for row in matrix],
        "principal_minors": {
            label: mp.nstr(value, 70) for label, value in minors.items()
        },
        "approximate_eigenvalues": [
            mp.nstr(value, 30) for value in eigenvalues
        ],
        "positive_semidefinite": all(value >= 0 for value in minors.values()),
        "positive_definite": all(value > 0 for value in minors.values()),
    }


def audit_hankels(moments: Sequence[mp.mpf]) -> dict[str, object]:
    mu0, mu1, mu2, mu3 = moments
    matrices = {
        "H_0": [[mu0]],
        "H_0_plus": [[mu1]],
        "H_1": [[mu0, mu1], [mu1, mu2]],
        "H_1_plus": [[mu1, mu2], [mu2, mu3]],
    }
    audits = {name: audit_matrix(matrix) for name, matrix in matrices.items()}
    delta_1 = mu0 * mu2 - mu1**2
    delta_1_plus = mu1 * mu3 - mu2**2
    cross = mu0 * mu3 - mu1 * mu2
    conditions = {
        "mu_0 >= 0": mu0,
        "mu_1 >= 0": mu1,
        "mu_2 >= 0": mu2,
        "mu_3 >= 0": mu3,
        "mu_0*mu_2-mu_1^2 >= 0": delta_1,
        "mu_1*mu_3-mu_2^2 >= 0": delta_1_plus,
    }
    return {
        "matrices": audits,
        "six_unique_psd_conditions": {
            label: {
                "left_hand_side": mp.nstr(value, 70),
                "holds": value >= 0,
            }
            for label, value in conditions.items()
        },
        "all_accessible_matrices_positive_semidefinite": all(
            bool(record["positive_semidefinite"])
            for record in audits.values()
        ),
        "cross_minor": {
            "formula": "mu_0*mu_3-mu_1*mu_2",
            "value": mp.nstr(cross, 70),
            "nonnegative": cross >= 0,
        },
    }


def analyze_activation(name: str, record: dict[str, object]) -> dict[str, object]:
    runs = {
        key: [mp.mpf(value) for value in record[key]]
        for key in ("taylor_100dps", "derivative_100dps", "taylor_80dps")
    }
    for values in runs.values():
        if len(values) != 10:
            raise AssertionError(f"{name}: input jet is not contiguous through nine")
        if any(values[order] for order in range(0, 10, 2)):
            raise AssertionError(f"{name}: parity gate failed")

    route_errors = [
        relative_error(left, right)
        for left, right in zip(
            runs["taylor_100dps"], runs["derivative_100dps"]
        )
    ]
    precision_errors = [
        relative_error(left, right)
        for left, right in zip(
            runs["taylor_100dps"], runs["taylor_80dps"]
        )
    ]
    if max(route_errors) > mp.mpf("1e-65"):
        raise AssertionError(f"{name}: derivative routes disagree")
    if max(precision_errors) > mp.mpf("1e-55"):
        raise AssertionError(f"{name}: precision stability gate failed")

    moment_runs: dict[str, tuple[mp.mpf, tuple[mp.mpf, ...]]] = {}
    route_disagreements: dict[str, mp.mpf] = {}
    for precision_route in ("taylor_100dps", "taylor_80dps"):
        derivatives = runs[precision_route]
        baseline_a, moments_a, kernel = moments_by_reversion(derivatives)
        baseline_b, moments_b, terms = moments_by_triangular_identity(derivatives)
        errors = [relative_error(baseline_a, baseline_b)] + [
            relative_error(left, right)
            for left, right in zip(moments_a, moments_b)
        ]
        route_disagreements[precision_route] = max(errors)
        if max(errors) > mp.mpf("1e-65"):
            raise AssertionError(f"{name}: moment routes disagree")
        for odd_degree in range(1, 8, 2):
            if abs(kernel[odd_degree]) > mp.mpf("1e-80"):
                raise AssertionError(f"{name}: kernel parity gate failed")
        if any(
            relative_error(kernel[degree], terms[degree]) > mp.mpf("1e-65")
            for degree in range(2, 9, 2)
        ):
            raise AssertionError(f"{name}: kernel coefficients disagree")
        moment_runs[precision_route] = (baseline_a, moments_a)

    baseline, moments = moment_runs["taylor_100dps"]
    _, moments_80 = moment_runs["taylor_80dps"]
    moment_precision_errors = [
        relative_error(left, right)
        for left, right in zip(moments, moments_80)
    ]
    if max(moment_precision_errors) > mp.mpf("1e-55"):
        raise AssertionError(f"{name}: moment precision stability failed")
    if any(sign(left) != sign(right) for left, right in zip(moments, moments_80)):
        raise AssertionError(f"{name}: moment signs are precision-unstable")
    if any(abs(value) <= mp.mpf("1e-40") for value in moments):
        raise AssertionError(f"{name}: a moment sign is numerically inconclusive")

    hankels = audit_hankels(moments)
    return {
        "activation": record["formula"],
        "scale": record["scale"],
        "unit_variance": record["unit_variance"],
        "derivatives": [mp.nstr(value, 70) for value in runs["taylor_100dps"]],
        "derivative_validation": {
            "max_taylor_vs_derivative_relative_error": mp.nstr(
                max(route_errors), 12
            ),
            "max_80dps_vs_100dps_relative_error": mp.nstr(
                max(precision_errors), 12
            ),
            "even_orders": "exact zeros in sparse parity sectors",
        },
        "kernel_convention": (
            "K(y)=F'(F^{-1}(y))=F'(0)+sum_r (-1)^r mu_r y^(2r+2)"
        ),
        "kernel_baseline": mp.nstr(baseline, 70),
        "moments": {
            f"mu_{index}": {
                "value": mp.nstr(value, 70),
                "sign": sign(value),
            }
            for index, value in enumerate(moments)
        },
        "moment_validation": {
            "max_reversion_vs_triangular_relative_error": mp.nstr(
                max(route_disagreements.values()), 12
            ),
            "max_80dps_vs_100dps_relative_error": mp.nstr(
                max(moment_precision_errors), 12
            ),
            "signs_stable_80dps_vs_100dps": True,
        },
        "hankel_audit": hankels,
        "verdict": (
            "compatible_with_all_accessible_stieltjes_conditions"
            if hankels["all_accessible_matrices_positive_semidefinite"]
            else "violates_at_least_one_accessible_stieltjes_condition"
        ),
        "next_unavailable_conditions": {
            "mu_4_and_H_2": "require F^(11)(0)",
            "mu_5_and_H_2_plus": "require F^(13)(0)",
        },
    }


def main() -> int:
    mp.mp.dps = 120
    actual_hashes = {
        "input": sha256(INPUT),
        "protocol": sha256(PROTOCOL),
        "engine": sha256(ENGINE),
    }
    if actual_hashes != EXPECTED_SHA256:
        raise AssertionError(
            f"SHA-256 gate failed: actual={actual_hashes}, "
            f"expected={EXPECTED_SHA256}"
        )

    document = json.loads(INPUT.read_text())
    analyses = {
        name: analyze_activation(name, record)
        for name, record in document["activations"].items()
    }
    payload = {
        "model": document["model"],
        "max_feature_derivative_order": 9,
        "determined_moments": ["mu_0", "mu_1", "mu_2", "mu_3"],
        "accessible_hankel_matrices": ["H_0", "H_0_plus", "H_1", "H_1_plus"],
        "validation": "passed",
        "sha256": actual_hashes,
        "activations": analyses,
        "claim_boundary": (
            "Each verdict is a finite-order statement for the named sine "
            "activation under the frozen model; no arbitrary-order or "
            "positive-time conclusion is implied."
        ),
    }
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
