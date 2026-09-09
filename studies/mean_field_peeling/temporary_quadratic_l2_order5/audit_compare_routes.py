#!/usr/bin/env python3
"""Coefficientwise comparison of two independent quadratic order-five routes."""

from fractions import Fraction as Q

import quadratic_exact as contraction_route
import quadratic_euler_jet as chronological_route


def main() -> None:
    invariants = contraction_route.exact_contractions()
    paired_a = contraction_route.paired_coefficients(invariants)

    outputs = [chronological_route.horizon_output(n) for n in range(6)]
    theta = chronological_route.newton_coefficients(
        [output.h_coefficient(5) for output in outputs]
    )
    gamma = chronological_route.time_polynomial_from_newton(theta, 5)

    # If A_5(N)=sum_d gamma_d N^d, then
    # A_5(2t)-32 A_5(t)=sum_{d=1}^4 (2^d-32) gamma_d t^d.
    paired_b = [{} for _ in range(5)]
    for degree in range(1, 5):
        paired_b[degree] = {
            monomial: Q(2**degree - 32) * coefficient
            for monomial, coefficient in gamma[degree].items()
            if coefficient
        }

    # The two raw formulas use different homogeneous representatives before
    # imposing a^2+3b^2=1.  Compare their canonical normalized numerators
    # after a=1/sqrt(1+3e^2), b=e/sqrt(1+3e^2).
    paired_a_normalized = [
        chronological_route.normalized_numerator(value, 9)
        for value in paired_a
    ]
    paired_b_normalized = [
        chronological_route.normalized_numerator(value, 9)
        for value in paired_b
    ]
    for degree in range(1, 5):
        if paired_a_normalized[degree] != paired_b_normalized[degree]:
            left = paired_a_normalized[degree]
            right = paired_b_normalized[degree]
            keys = set(left) | set(right)
            mismatch = {
                key: (left.get(key, Q(0)), right.get(key, Q(0)))
                for key in keys
                if left.get(key, Q(0)) != right.get(key, Q(0))
            }
            raise AssertionError((degree, mismatch))

    # Structural signs: c_1,c_3 strictly negative coefficientwise and
    # c_2,c_4 strictly positive coefficientwise.
    expected_sign = {1: -1, 2: 1, 3: -1, 4: 1}
    for degree, sign in expected_sign.items():
        assert paired_a_normalized[degree]
        assert all(sign * coefficient > 0 for coefficient in paired_a_normalized[degree].values())

    # The t^5 coefficient of F_t is strictly positive coefficientwise.
    gamma5_normalized = chronological_route.normalized_numerator(gamma[5], 9)
    assert gamma5_normalized
    assert all(coefficient > 0 for coefficient in gamma5_normalized.values())

    # Cubic route: K_3(t)=J*t*(2t-1)/2.
    cubic_values = [output.h_coefficient(3) for output in outputs[:4]]
    cubic_theta = chronological_route.newton_coefficients(cubic_values)
    cubic_gamma = chronological_route.time_polynomial_from_newton(cubic_theta, 3)
    cubic_paired = [{} for _ in range(3)]
    for degree in (1, 2):
        raw = {
            monomial: Q(2**degree - 8) * coefficient
            for monomial, coefficient in cubic_gamma[degree].items()
            if coefficient
        }
        cubic_paired[degree] = chronological_route.normalized_numerator(raw, 6)
    cubic_j_raw = contraction_route.cubic_J()
    cubic_j = chronological_route.normalized_numerator(cubic_j_raw, 6)
    assert cubic_paired[1] == {k: -v / 2 for k, v in cubic_j.items()}
    assert cubic_paired[2] == cubic_j

    print("coefficientwise route comparison: PASS")
    print("paired coefficient sign audit: PASS")
    print("raw F_t t^5-leading coefficient positivity: PASS")
    print("cubic invariant comparison: PASS")


if __name__ == "__main__":
    main()
