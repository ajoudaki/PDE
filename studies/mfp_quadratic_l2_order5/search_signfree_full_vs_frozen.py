#!/usr/bin/env python3
"""Exact width-first low-order test of full L=2 versus frozen rows.

The chronological Gaussian/Wick recursion is the same inverse-free OMFP
DAG as quadratic_euler_jet.py, but activation coefficients are fixed
rational numbers and may have arbitrary signs.  The default activation
(-1-x-x^2+x^3)/4 has exactly unit Gaussian L2 norm.
"""

from fractions import Fraction as Q
import quadratic_euler_jet as dag


def power(x, n):
    y = dag.GPoly.constant(x.dimension)
    for _ in range(n):
        y = y.mul(x)
    return y


def compiler(coefficients):
    coefficients = tuple(Q(x) for x in coefficients)

    def activate(x):
        y = dag.GPoly.zero(x.dimension)
        for n, c in enumerate(coefficients):
            if c:
                y = y.add(power(x, n).scale(dag.Ring.scalar(c)))
        return y

    def derivative(x):
        y = dag.GPoly.zero(x.dimension)
        for n, c in enumerate(coefficients[1:], 1):
            if c:
                y = y.add(power(x, n-1).scale(dag.Ring.scalar(n*c)))
        return y

    return activate, derivative


def full_output(horizon, coefficients):
    old_activate = dag.activate
    old_derivative = dag.activation_derivative
    dag.activate, dag.activation_derivative = compiler(coefficients)
    try:
        return dag.horizon_output(horizon)
    finally:
        dag.activate, dag.activation_derivative = old_activate, old_derivative


def frozen_output(horizon, coefficients, step_scale=1):
    activate, derivative = compiler(coefficients)
    dim = 2
    expectation = dag.GaussianExpectation(dim)
    expectation.set_covariance(1, 1, dag.ONE)
    a = dag.GPoly.variable(dim, 0)
    z = dag.GPoly.variable(dim, 1)
    hs = dag.H.scale(step_scale)
    for _ in range(horizon):
        old_a, old_z = a, z
        a = old_a.add(activate(old_z).scale(hs))
        z = old_z.add(old_a.mul(derivative(old_z)).scale(hs))
    return expectation.expect(a.mul(activate(z)))


def hcoeff(ring, k):
    terms = ring.h_coefficient(k)
    assert all(key == (0, 0) for key in terms)
    return terms.get((0, 0), Q(0))


def difference_coefficients(coefficients):
    f1 = full_output(1, coefficients)
    f2 = full_output(2, coefficients)
    # Substitution h -> 2h multiplies the coefficient of h^k by 2^k;
    # it does not change the exponent.
    full_defect = f2 - dag.Ring.from_dict({(h,a,b): (2**h)*c
                                           for (h,a,b),c in f1.terms})
    r1 = frozen_output(1, coefficients, 2)
    r2 = frozen_output(2, coefficients, 1)
    frozen_defect = r2-r1
    difference = full_defect-frozen_defect
    return (tuple(hcoeff(full_defect,k) for k in range(dag.MAX_H+1)),
            tuple(hcoeff(frozen_defect,k) for k in range(dag.MAX_H+1)),
            tuple(hcoeff(difference,k) for k in range(dag.MAX_H+1)))


def test(coefficients):
    full, frozen, difference = difference_coefficients(coefficients)
    print("activation", coefficients)
    print("power full frozen full-frozen")
    for k in range(dag.MAX_H+1):
        print(k, full[k], frozen[k], difference[k])
    return difference


if __name__ == "__main__":
    dag.MAX_H = 7
    test((Q(-1,4), Q(-1,4), Q(-1,4), Q(1,4)))
