#!/usr/bin/env python3
"""Independent Wishart/rank-one spectral closure for depth-two identity."""

from __future__ import annotations

import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.path.insert(0, str(PARENT))

from identity_stieltjes_audit import (  # noqa: E402
    fraction_string,
    moments_from_triangular_identity,
)


Q = Fraction
MAX_FEATURE_ORDER = 81
MAX_R_ORDER = MAX_FEATURE_ORDER + 1
Polynomial = list[Fraction]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def trim(polynomial: Polynomial) -> Polynomial:
    result = list(polynomial)
    while len(result) > 1 and not result[-1]:
        result.pop()
    return result


def add(left: Polynomial, right: Polynomial) -> Polynomial:
    size = max(len(left), len(right))
    return trim([
        (left[index] if index < len(left) else Q(0))
        + (right[index] if index < len(right) else Q(0))
        for index in range(size)
    ])


def scale(polynomial: Polynomial, coefficient: Fraction | int) -> Polynomial:
    coefficient = Q(coefficient)
    return trim([coefficient * value for value in polynomial])


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result = [Q(0) for _ in range(len(left) + len(right) - 1)]
    for i, left_value in enumerate(left):
        if not left_value:
            continue
        for j, right_value in enumerate(right):
            if right_value:
                result[i + j] += left_value * right_value
    return trim(result)


def lambda_times(polynomial: Polynomial) -> Polynomial:
    return [Q(0)] + list(polynomial)


def catalan(index: int) -> int:
    return math.comb(2 * index, index) // (index + 1)


def inverse_series(series: list[Fraction], degree: int) -> list[Fraction]:
    if not series or not series[0]:
        raise ArithmeticError("series is not invertible")
    result = [Q(0) for _ in range(degree + 1)]
    result[0] = 1 / series[0]
    for order in range(1, degree + 1):
        result[order] = -sum(
            series[index] * result[order - index]
            for index in range(1, min(order, len(series) - 1) + 1)
        ) / series[0]
    return result


def initial_spectral_moments(max_degree: int) -> tuple[list[Fraction], list[Fraction]]:
    """Moments of rho_x and rho_v derived from MP(1), not feature jets.

    If m(w)=sum C_k w^(k+1) is the MP resolvent at infinity, the rank-one
    Sherman--Morrison identity gives g_x=m/(1+m).  The velocity measure is
    the size-biased MP law, so its kth moment is C_(k+1).
    """

    degree = max_degree + 1
    mp = [Q(0)] + [Q(catalan(index)) for index in range(max_degree + 1)]
    denominator = list(mp)
    denominator[0] += 1
    inverse = inverse_series(denominator, degree)
    product = [Q(0) for _ in range(degree + 1)]
    for i, left in enumerate(mp):
        for j, right in enumerate(inverse):
            if i + j <= degree:
                product[i + j] += left * right
    rho_x = [product[index + 1] for index in range(max_degree + 1)]
    rho_v = [Q(catalan(index + 1)) for index in range(max_degree + 1)]
    return rho_x, rho_v


def integrate(polynomial: Polynomial, moments: list[Fraction]) -> Fraction:
    if len(polynomial) > len(moments):
        raise ArithmeticError("not enough spectral moments")
    return sum(
        coefficient * moments[degree]
        for degree, coefficient in enumerate(polynomial)
    )


def spectral_fixed_point(max_r_order: int) -> tuple[list[Fraction], list[Polynomial], list[Polynomial]]:
    spectral_degree = max_r_order // 2 + 2
    rho_x, rho_v = initial_spectral_moments(spectral_degree)
    a: list[Polynomial] = [[Q(1)], [Q(0)]]
    b: list[Polynomial] = [[Q(0)], [Q(1)]]
    r: list[Fraction] = [Q(1), Q(0)]

    for degree in range(2, max_r_order + 1):
        prior = degree - 2
        rhs_a = lambda_times(a[prior])
        rhs_b = lambda_times(b[prior])
        potential_a = [Q(0)]
        potential_b = [Q(0)]
        for left in range(prior + 1):
            potential_a = add(potential_a, scale(a[prior - left], r[left]))
            potential_b = add(potential_b, scale(b[prior - left], r[left]))
        denominator = degree * (degree - 1)
        a.append(scale(add(rhs_a, scale(potential_a, 2)), Q(1, denominator)))
        b.append(scale(add(rhs_b, scale(potential_b, 2)), Q(1, denominator)))

        norm_coefficient_a = [Q(0)]
        norm_coefficient_b = [Q(0)]
        for left in range(degree + 1):
            norm_coefficient_a = add(
                norm_coefficient_a, multiply(a[left], a[degree - left])
            )
            norm_coefficient_b = add(
                norm_coefficient_b, multiply(b[left], b[degree - left])
            )
        r.append(
            integrate(norm_coefficient_a, rho_x)
            + integrate(norm_coefficient_b, rho_v)
        )
    return r, a, b


def main() -> int:
    r, a, b = spectral_fixed_point(MAX_R_ORDER)
    derivatives = [
        Q(math.factorial(order + 1), 2) * r[order + 1]
        for order in range(MAX_FEATURE_ORDER + 1)
    ]
    accepted = json.loads((HERE / "RESULTS.json").read_text())
    accepted_derivatives = [Q(value) for value in accepted["derivatives"]]
    if derivatives != accepted_derivatives:
        mismatch = next(
            index for index, pair in enumerate(zip(derivatives, accepted_derivatives))
            if pair[0] != pair[1]
        )
        raise AssertionError(f"spectral closure first differs at F^{mismatch}")
    odd = {
        order: int(derivatives[order])
        for order in range(1, MAX_FEATURE_ORDER + 1, 2)
    }
    baseline, moments = moments_from_triangular_identity(odd)
    accepted_moments = tuple(Q(value) for value in accepted["moments"])
    if moments != accepted_moments:
        raise AssertionError("spectral closure output moments differ")

    rho_x, rho_v = initial_spectral_moments(12)
    payload = {
        "format": "identity-depth2-spectral-closure-v1",
        "finite_width_invariant": "C=B*B^T-x*x^T",
        "vector_equation": "x''=(C+||x||^2+||y||^2)*x",
        "width_limit_balance": "||x||^2=||y||^2=r",
        "spectral_measures": {
            "MP_density": "sqrt((4-lambda)/lambda)/(2*pi) on (0,4)",
            "rho_x_resolvent": "g_x=m_MP/(1+m_MP)",
            "rho_x_explicit": "(3/4)*delta_(-1/2) + sqrt(lambda*(4-lambda))/(2*pi*(1+2*lambda)) on (0,4)",
            "rho_v_explicit": "sqrt(lambda*(4-lambda))/(2*pi) on (0,4)",
            "rho_x_moments_0_through_12": [fraction_string(value) for value in rho_x],
            "rho_v_moments_0_through_12": [fraction_string(value) for value in rho_v],
        },
        "closed_fixed_point": {
            "mode_equations": [
                "a_lambda''=(lambda+2*r)*a_lambda, a_lambda(0)=1, a_lambda'(0)=0",
                "b_lambda''=(lambda+2*r)*b_lambda, b_lambda(0)=0, b_lambda'(0)=1",
            ],
            "self_consistency": "r=int a_lambda^2 d rho_x + int b_lambda^2 d rho_v",
            "feature": "F=r'/2",
        },
        "validation": {
            "derivatives_match_independent_gaussian_program_through_81": True,
            "moments_mu_0_through_39_match": True,
            "kernel_baseline": fraction_string(baseline),
            "max_a_polynomial_support": max(len(value) for value in a),
            "max_b_polynomial_support": max(len(value) for value in b),
        },
        "classification": (
            "exact all-fixed-order formal spectral closure, but not an elementary "
            "closed form for F or K and not an all-order Stieltjes proof"
        ),
        "sha256": {
            "accepted_comparison_input": sha256(HERE / "RESULTS.json"),
            "protocol": sha256(HERE / "SPECTRAL_CLOSURE_PROTOCOL.md"),
            "source": sha256(Path(__file__)),
        },
    }
    output = HERE / "SPECTRAL_CLOSURE_RESULTS.json"
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({
        "output": str(output),
        "derivative_match_through": MAX_FEATURE_ORDER,
        "moment_match_through": 39,
        "rho_x_prefix": payload["spectral_measures"]["rho_x_moments_0_through_12"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

