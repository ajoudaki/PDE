#!/usr/bin/env python3
"""Exact checks for the arbitrary-sign full-L2 audit boundary.

The calculations use the chronological inverse-free Gaussian/Wick DAG,
not finite-width Taylor expansion.  All represented coefficients are exact
Fractions (or formal powers of the normalization scalar b).
"""

from fractions import Fraction as Q

import quadratic_euler_jet as dag
from search_signfree_full_vs_frozen import (
    difference_coefficients,
    full_output,
    hcoeff,
)


def main():
    # Rationally normalized shifted quadratic:
    # psi=(10/27)(x^2-33/10)=-11/9+(10/27)x^2.
    K = Q(33, 10)
    b = Q(10, 27)
    activation = (-K*b, Q(0), b)
    assert b*b*(K*K-2*K+3) == 1

    dag.MAX_H = 7
    f1 = full_output(1, activation)
    asserted = Q(1024)*b**16*(3-K)**3
    assert hcoeff(f1, 7) == asserted < 0

    # The signed activation kills coefficientwise frozen/full deletion.
    dag.MAX_H = 49
    difference = difference_coefficients(activation)[2]
    negative_h11 = Q(
        -50342126934494248177872714327572247743518720000000000,
        375710212613636260325580163599137907799836383538729,
    )
    assert difference[11] == negative_h11 < 0

    # For the normalized K=3 activation b(x^2-3), b^2=1/6.
    # Keep b formal in the Ring, so no irrational arithmetic is needed.
    def centered_activate(x):
        return dag.GPoly.constant(x.dimension, dag.BB.scale(-3)).add(
            x.mul(x).scale(dag.BB)
        )

    def centered_derivative(x):
        return x.scale(dag.BB.scale(2))

    old_activate, old_derivative = dag.activate, dag.activation_derivative
    dag.activate, dag.activation_derivative = centered_activate, centered_derivative
    try:
        f2 = dag.horizon_output(2)
    finally:
        dag.activate, dag.activation_derivative = old_activate, old_derivative

    for degree in (49, 47, 45, 43, 41, 39):
        assert not f2.h_coefficient(degree)
    h37 = sum(
        coefficient * Q(1, 6)**(b_power//2)
        for (a_power, b_power), coefficient in f2.h_coefficient(37).items()
        if not a_power
    )
    assert h37 == Q(25734273826816, 68630377364883) > 0

    print("signed full-network bridge audit: PASS")


if __name__ == "__main__":
    main()
