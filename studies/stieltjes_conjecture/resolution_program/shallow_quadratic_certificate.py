#!/usr/bin/env python3
"""Exact downstream certificate for the shallow raw-square reduction.

The accepted boundary calculation is stored in
``BLOCK_METRIC_COUNTEREXAMPLE.json``.  This checker does not recompute that
Gaussian/Wick calculation.  It independently applies the exact positive
scaling from the boundary model (activation multiplier three) to the
conventionally normalized shallow model, rebuilds the decisive Hankel
determinant, and checks the algebra behind the Riccati characteristics.

Only the Python standard library is used.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable


Q = Fraction
Monomial = tuple[int, ...]
Polynomial = dict[Monomial, Fraction]

HERE = Path(__file__).resolve().parent
BOUNDARY_CERTIFICATE = HERE / "BLOCK_METRIC_COUNTEREXAMPLE.json"
BOUNDARY_CERTIFICATE_SHA256 = (
    "30f01203422f989924ffe32e5c84f3e7f40129dc9aac2f9e23c980958f27a447"
)
ACTIVATION_MULTIPLIER = 3


def parse_fraction(value: str) -> Fraction:
    return Q(value)


def fraction_string(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def determinant3(matrix: list[list[Fraction]]) -> Fraction:
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("expected a 3 by 3 matrix")
    return (
        matrix[0][0]
        * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1]
        * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2]
        * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def polynomial(values: Iterable[tuple[Monomial, int | Fraction]]) -> Polynomial:
    result: Polynomial = {}
    for monomial, coefficient in values:
        coefficient = Q(coefficient)
        if coefficient:
            result[monomial] = result.get(monomial, Q(0)) + coefficient
    return {key: value for key, value in result.items() if value}


def variable(index: int, dimension: int) -> Polynomial:
    powers = [0] * dimension
    powers[index] = 1
    return {tuple(powers): Q(1)}


def add(*values: Polynomial) -> Polynomial:
    return polynomial(
        (monomial, coefficient)
        for value in values
        for monomial, coefficient in value.items()
    )


def scale(value: Polynomial, coefficient: int | Fraction) -> Polynomial:
    coefficient = Q(coefficient)
    return {
        monomial: coefficient * scalar
        for monomial, scalar in value.items()
        if coefficient * scalar
    }


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    return polynomial(
        (
            tuple(a + b for a, b in zip(left_monomial, right_monomial)),
            left_coefficient * right_coefficient,
        )
        for left_monomial, left_coefficient in left.items()
        for right_monomial, right_coefficient in right.items()
    )


def differentiate(value: Polynomial, index: int) -> Polynomial:
    terms: list[tuple[Monomial, Fraction]] = []
    for monomial, coefficient in value.items():
        exponent = monomial[index]
        if not exponent:
            continue
        child = list(monomial)
        child[index] -= 1
        terms.append((tuple(child), exponent * coefficient))
    return polynomial(terms)


def lie_derivative(value: Polynomial, field: list[Polynomial]) -> Polynomial:
    return add(
        *(
            multiply(differentiate(value, index), velocity)
            for index, velocity in enumerate(field)
        )
    )


def riccati_algebra_gates() -> dict[str, object]:
    """Check the characteristic identities as exact polynomial identities."""

    # Neuron system a'=v^2, v'=2av and c=a^2-v^2/2.
    a = variable(0, 2)
    v = variable(1, 2)
    a_squared = multiply(a, a)
    v_squared = multiply(v, v)
    invariant = add(a_squared, scale(v_squared, Q(-1, 2)))
    neuron_field = [v_squared, scale(multiply(a, v), 2)]
    invariant_derivative = lie_derivative(invariant, neuron_field)
    if invariant_derivative:
        raise AssertionError("Riccati invariant failed")

    # For D'=E and E'=4cD, J=E^2-4cD^2-2v0^2 is conserved.
    d = variable(0, 4)
    e = variable(1, 4)
    c = variable(2, 4)
    v0 = variable(3, 4)
    first_integral = add(
        multiply(e, e),
        scale(multiply(c, multiply(d, d)), -4),
        scale(multiply(v0, v0), -2),
    )
    d_field = [e, scale(multiply(c, d), 4), {}, {}]
    first_integral_derivative = lie_derivative(first_integral, d_field)
    if first_integral_derivative:
        raise AssertionError("D first integral is not conserved")

    # At D(0)=1, E(0)=-2a0, c=a0^2-v0^2/2, J(0)=0.
    a0 = variable(0, 2)
    initial_v0 = variable(1, 2)
    initial_identity = add(
        scale(multiply(a0, a0), 4),
        scale(
            add(
                multiply(a0, a0),
                scale(multiply(initial_v0, initial_v0), Q(-1, 2)),
            ),
            -4,
        ),
        scale(multiply(initial_v0, initial_v0), -2),
    )
    if initial_identity:
        raise AssertionError("D first integral has the wrong initial value")

    # Clearing denominators after a=-E/(2D), v=v0/D gives identities:
    #   2D^2[a'-2(a^2-c)] = 0,
    #   D^2[v'-2av] = 0,
    # while J=0 upgrades the Riccati equation to a'=v^2.
    a_prime_numerator = add(
        multiply(e, e), scale(multiply(c, multiply(d, d)), -4)
    )
    riccati_rhs_numerator = add(
        multiply(e, e), scale(multiply(c, multiply(d, d)), -4)
    )
    riccati_residual = add(
        a_prime_numerator, scale(riccati_rhs_numerator, -1)
    )
    v_prime_numerator = scale(multiply(v0, e), -1)
    v_rhs_numerator = scale(multiply(v0, e), -1)
    v_residual = add(v_prime_numerator, scale(v_rhs_numerator, -1))
    if riccati_residual or v_residual:
        raise AssertionError("D substitution does not solve the neuron system")
    a_equals_v_residual = add(
        a_prime_numerator, scale(multiply(v0, v0), -2)
    )
    if a_equals_v_residual != first_integral:
        raise AssertionError("a'=v^2 is not equivalent to the first integral")

    return {
        "neuron_invariant": "c=a0^2-v0^2/2",
        "neuron_invariant_lie_derivative_zero": True,
        "D_equation": "D''=4*c*D, D(0)=1, D'(0)=-2*a0",
        "D_first_integral": "D'^2-4*c*D^2-2*v0^2=0",
        "D_first_integral_lie_derivative_zero": True,
        "D_first_integral_initial_value_zero": True,
        "solution": "a=-D'/(2*D), v=v0/D",
        "riccati_residual_zero_after_D_equation": True,
        "v_equation_residual_zero": True,
        "a_prime_equals_v_squared_after_first_integral": True,
    }


def build_certificate() -> dict[str, object]:
    digest = hashlib.sha256(BOUNDARY_CERTIFICATE.read_bytes()).hexdigest()
    if digest != BOUNDARY_CERTIFICATE_SHA256:
        raise AssertionError(f"boundary certificate hash mismatch: {digest}")
    boundary = json.loads(BOUNDARY_CERTIFICATE.read_text())
    if boundary["metric"] != {"alpha": 0, "beta": 1}:
        raise AssertionError("unexpected source metric")

    reduced_moments = [
        parse_fraction(value) for value in boundary["output_kernel_moments_mu"]
    ]
    shallow_moments = [
        moment * ACTIVATION_MULTIPLIER ** (2 * order)
        for order, moment in enumerate(reduced_moments)
    ]
    shifted = [
        [shallow_moments[row + column + 1] for column in range(3)]
        for row in range(3)
    ]
    shallow_determinant = determinant3(shifted)
    reduced_determinant = parse_fraction(
        boundary["negative_shifted_H2_determinant"]
    )
    determinant_scale = ACTIVATION_MULTIPLIER**18
    if shallow_determinant != determinant_scale * reduced_determinant:
        raise AssertionError("Hankel determinant congruence failed")
    if shallow_determinant >= 0:
        raise AssertionError("shallow determinant is not negative")

    shallow_derivatives: dict[str, str] = {}
    for order_string, value_string in boundary["feature_derivatives"].items():
        order = int(order_string)
        value = parse_fraction(value_string)
        scaled = value / ACTIVATION_MULTIPLIER ** (order + 1)
        shallow_derivatives[order_string] = fraction_string(scaled)

    if shallow_derivatives["1"] != "7":
        raise AssertionError("shallow kernel baseline is not seven")

    return {
        "schema": "shallow_quadratic_stieltjes_counterexample_v1",
        "source": {
            "path": BOUNDARY_CERTIFICATE.name,
            "sha256": BOUNDARY_CERTIFICATE_SHA256,
            "metric": {"alpha": 0, "beta": 1},
        },
        "finite_width_reduction": {
            "m_n": "n^-1*sum_j(u_j^4)",
            "v_i": "z_i/sqrt(m_n)",
            "output": "m_n*n^-1*sum_i(a_i*v_i^2)",
            "feature_flow": ["a_i'=m_n*v_i^2", "v_i'=2*m_n*a_i*v_i"],
            "conditional_initial_law": "a_i,v_i iid N(0,1); v is independent of m_n",
            "fixed_order_limit": "m_n -> 3 in every finite L^p",
        },
        "scaling": {
            "activation_multiplier": ACTIVATION_MULTIPLIER,
            "F_relation": "F_3(s)=3*F_1(3*s)",
            "K_relation": "K_3(y)=9*K_1(y/3)",
            "R_relation": "R_3(x)=R_1(x/9)",
            "moment_relation": "mu_r^(3)=9^(-r)*mu_r^(1)",
            "shifted_H2_determinant_relation": "Delta_1=3^18*Delta_3",
            "determinant_scale": str(determinant_scale),
        },
        "conventional_shallow": {
            "network": "n^-1*sum_i(a_i*v_i^2)",
            "kernel_baseline": "7",
            "feature_derivatives": dict(
                sorted(shallow_derivatives.items(), key=lambda item: int(item[0]))
            ),
            "output_kernel_moments_mu": [
                fraction_string(value) for value in shallow_moments
            ],
            "negative_shifted_H2_determinant": fraction_string(
                shallow_determinant
            ),
        },
        "riccati": riccati_algebra_gates(),
        "decision": (
            "the conventional one-input iid-Gaussian raw-square shallow "
            "formal output-kernel moment sequence is not Stieltjes"
        ),
        "scope": (
            "fixed-order width-limit formal jet; no positive-time Gaussian "
            "population curve or closed scalar loss ODE is asserted"
        ),
    }


def main() -> None:
    print(json.dumps(build_certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
