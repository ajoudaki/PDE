#!/usr/bin/env python3
"""Independent exact gates for ``quadratic_euler_jet``.

The all-distinct-time Newton coefficient Theta_{r,r} must equal the r-th
continuous feature-flow derivative.  We compare it against the independently
frozen layer-separated Gaussian normal form at orders 1, 3, and 5.  We also
check the already audited identity Euler horizon table and raw-quadratic
controls.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

from studies.mfp_gaussian_calculus.order5.compiler.artifact_evaluator import (
    evaluate_artifact_polynomial,
)
from studies.mfp_quadratic_l2_order5.quadratic_euler_jet import (
    evaluate_ab,
    horizon_output,
    newton_coefficients,
    normalized_numerator,
    time_polynomial_from_newton,
)
from math import comb


Q = Fraction
ROOT = Path(__file__).parents[1]
ARTIFACT = (
    ROOT
    / "mfp_gaussian_calculus"
    / "order5"
    / "compiler"
    / "LAYER_SEPARATED_ABC_NORMAL_FORM.txt"
)


def main() -> None:
    outputs = [horizon_output(n) for n in range(6)]
    theta = {
        degree: newton_coefficients(
            [output.h_coefficient(degree) for output in outputs[: degree + 1]]
        )
        for degree in (1, 3, 5)
    }

    # This uses a separately generated and independently audited Gaussian
    # normal form, not the chronological Euler recurrence under test.
    # Both routes are bivariate polynomials of separate degree at most 18 in
    # (a,b).  Agreement on the 19 by 19 tensor grid is therefore a literal
    # coefficientwise identity (successive univariate interpolation), not a
    # numerical spot check.
    for a in range(19):
        for b in range(19):
            frozen = evaluate_artifact_polynomial(ARTIFACT, [0, a, b], q0=1)
            observed = {
                "A": evaluate_ab(theta[1][1], Q(a), Q(b)),
                "B": evaluate_ab(theta[3][3], Q(a), Q(b)),
                "C": evaluate_ab(theta[5][5], Q(a), Q(b)),
            }
            assert observed == frozen, (a, b, observed, frozen)

    identity_c3 = [evaluate_ab(value.h_coefficient(3), Q(1), Q(0)) for value in outputs]
    identity_c5 = [evaluate_ab(value.h_coefficient(5), Q(1), Q(0)) for value in outputs]
    assert identity_c3 == [0, 0, 24, 120, 336, 720]
    assert identity_c5 == [0, 0, 20, 525, 3682, 14824]

    # Raw quadratic continuous-flow controls from the exact forest compiler.
    assert evaluate_ab(theta[1][1], Q(0), Q(1)) == 111
    assert evaluate_ab(theta[3][3], Q(0), Q(1)) == 1_685_184
    assert evaluate_ab(theta[5][5], Q(0), Q(1)) == 77_400_633_120

    # The readout-sign involution makes all even coefficients vanish for the
    # full nonlinear activation, not just at the two endpoints.
    for output in outputs:
        assert not output.h_coefficient(2)
        assert not output.h_coefficient(4)

    normalized_theta5 = [
        normalized_numerator(value, 9) for value in theta[5]
    ]
    gamma5 = time_polynomial_from_newton(normalized_theta5, 5)
    # The exact monomial-in-time signs are +,-,+,-,+ coefficientwise.
    for degree in range(1, 6):
        sign = 1 if degree % 2 else -1
        assert gamma5[degree]
        assert all(sign * coefficient > 0 for coefficient in gamma5[degree].values())

    denominator = {power: Q(comb(9, power) * 3**power) for power in range(10)}
    positive = [
        {power: ((-1) ** (degree + 1)) * coefficient
         for power, coefficient in gamma5[degree].items()}
        for degree in range(1, 5)
    ]
    ratios = [
        [polynomial[power] / denominator[power] for power in range(10)]
        for polynomial in positive
    ]
    assert min(ratios[3]) == Q(613, 12)
    assert max(ratios[3]) == Q(2_400_252_749, 19_683)
    assert all(row.index(max(row)) == 9 for row in ratios)
    assert all(all(row[k] < row[k + 1] for k in range(9)) for row in ratios)
    uniform_bound = 30 * max(ratios[0]) + 28 * max(ratios[1]) \
        + 24 * max(ratios[2]) + 16 * max(ratios[3])
    assert uniform_bound == Q(63_082_885_600, 6_561)

    # On the explicit near-identity interval |e| <= 1/100, monotonicity of
    # the coefficient ratios makes x=10^-4 the worst endpoint.
    x0 = Q(1, 10_000)
    denominator_at_x0 = (1 + 3 * x0) ** 9
    values_at_x0 = [
        sum(polynomial[power] * x0**power for power in range(10))
        / denominator_at_x0
        for polynomial in positive
    ]
    local_bound = 30 * values_at_x0[0] + 28 * values_at_x0[1] \
        + 24 * values_at_x0[2] + 16 * values_at_x0[3]
    assert local_bound < 4_634
    assert 16 * values_at_x0[3] < 835

    print("independent layer-separated coefficientwise normal-form gate: PASS")
    print("identity finite-horizon gates: PASS")
    print("raw-quadratic forest controls: PASS")
    print("even-parity gates: PASS")
    print("normalized sign, quartic lower bound, and uniform upper bound gates: PASS")


if __name__ == "__main__":
    main()
