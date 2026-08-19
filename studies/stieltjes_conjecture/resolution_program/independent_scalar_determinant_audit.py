#!/usr/bin/env python3
"""Independent 37-node reconstruction of the alpha-dependent determinant.

This checker deliberately avoids the Q[alpha] inversion implementation.  At
each integer alpha=0,...,36 it first evaluates the retained feature jet, then
uses the older scalar Fraction/Lagrange-inversion path to construct the six
moments and shifted determinant.  Exact Newton interpolation of

    (63+48*alpha)^33 Delta(alpha)

then recovers the complete degree-36 numerator independently.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

from block_metric_counterexample import (
    determinant,
    hankel,
    inverse_derivative_moments,
    output_kernel_moments,
)


Q = Fraction
HERE = Path(__file__).resolve().parent
JET_PATH = HERE / "BLOCK_METRIC_POSITIVE_ALPHA_JET.json"
INTERVAL_PATH = HERE / "ALPHA_INTERVAL_CERTIFICATE.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evaluate_polynomial(coefficients: list[str], point: int) -> int:
    value = 0
    for coefficient in reversed(coefficients):
        value = value * point + int(coefficient)
    return value


def scalar_shifted_determinant(
    jets: dict[str, list[str]], alpha: int
) -> tuple[Fraction, list[Fraction]]:
    derivatives = [
        Q(evaluate_polynomial(jets[str(order)], alpha))
        for order in range(14)
    ]
    h_moments = inverse_derivative_moments(derivatives, 7)
    mu_moments = output_kernel_moments(h_moments)
    value = determinant(hankel(mu_moments, 3, shift=1))
    return value, mu_moments


def multiply_power_polynomials(
    left: list[Fraction], right: list[Fraction]
) -> list[Fraction]:
    result = [Q(0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] += left_value * right_value
    return result


def interpolate_integer_nodes(values: list[Fraction]) -> list[Fraction]:
    """Power coefficients from values at 0,1,... by exact Newton differences."""

    differences = values[:]
    leading: list[Fraction] = []
    while differences:
        leading.append(differences[0])
        differences = [
            differences[index + 1] - differences[index]
            for index in range(len(differences) - 1)
        ]

    result = [Q(0)] * len(values)
    falling = [Q(1)]
    factorial = 1
    for degree, difference in enumerate(leading):
        if degree:
            factorial *= degree
        for power, coefficient in enumerate(falling):
            result[power] += difference * coefficient / factorial
        falling = multiply_power_polynomials(falling, [Q(-degree), Q(1)])
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def fraction_string(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def build_audit() -> dict[str, object]:
    jet_document = json.loads(JET_PATH.read_text())
    interval_document = json.loads(INTERVAL_PATH.read_text())
    jets = jet_document["feature_derivative_polynomials"]

    sampled: list[Fraction] = []
    scalar_determinants: dict[int, Fraction] = {}
    scalar_moments: dict[int, list[Fraction]] = {}
    for alpha in range(37):
        value, moments = scalar_shifted_determinant(jets, alpha)
        scalar_determinants[alpha] = value
        scalar_moments[alpha] = moments
        sampled.append(value * Q(63 + 48 * alpha) ** 33)

    reconstructed = interpolate_integer_nodes(sampled)
    primitive = [
        int(value)
        for value in interval_document["primitive_numerator_ascending"]
    ]
    scale = Q(interval_document["positive_primitive_scale"])
    expected = [scale * coefficient for coefficient in primitive]
    if reconstructed != expected:
        raise AssertionError("37-node determinant numerator mismatch")

    epsilon = Q(1, 100)
    endpoint = Q(0)
    for coefficient in reversed(primitive):
        endpoint = endpoint * epsilon + coefficient
    if not (
        primitive[0] < 0
        and primitive[1] < 0
        and all(value > 0 for value in primitive[2:])
        and endpoint < 0
    ):
        raise AssertionError("independent convex interval sign gate failed")

    canonical_mu5 = scalar_moments[1][5]
    canonical_delta = scalar_determinants[1]
    expected_mu5 = Q(
        43091400402899303445912484475500496,
        66714012134145460981362191472284175,
    )
    expected_delta = Q(
        821121994467978760780817399151273570663517173613881280168626780102656,
        21875165394618842103069584785029512715749438929178771773425620184364845,
    )
    if canonical_mu5 != expected_mu5 or canonical_delta != expected_delta:
        raise AssertionError("canonical scalar reconstruction gate failed")

    coefficient_payload = json.dumps(
        [fraction_string(value) for value in reconstructed],
        separators=(",", ":"),
    ).encode()
    return {
        "schema": "independent_scalar_determinant_audit_v1",
        "method": (
            "37 scalar Fraction inversions followed by exact Newton "
            "interpolation"
        ),
        "alpha_nodes": list(range(37)),
        "imports_qalpha_inversion": False,
        "jet_certificate_sha256": sha256(JET_PATH),
        "interval_certificate_sha256": sha256(INTERVAL_PATH),
        "reconstructed_degree": len(reconstructed) - 1,
        "reconstructed_scaled_numerator_sha256": hashlib.sha256(
            coefficient_payload
        ).hexdigest(),
        "positive_scale": fraction_string(scale),
        "all_37_scaled_coefficients_match": True,
        "convex_interval_sign_reproduced": True,
        "epsilon": "1/100",
        "P_at_epsilon": fraction_string(endpoint),
        "canonical_mu5": fraction_string(canonical_mu5),
        "canonical_shifted_H2": fraction_string(canonical_delta),
        "decision": "independent scalar determinant reconstruction passed",
    }


def main() -> None:
    print(json.dumps(build_audit(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
