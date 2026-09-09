#!/usr/bin/env python3
"""Independent exact-rational audits for the quadratic order-five result."""

from fractions import Fraction as Q
from itertools import product
from math import prod
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
MFP = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(MFP))

from universal_euler_order5 import coefficient_at_integer  # noqa: E402
from quadratic_exact import (  # noqa: E402
    bp_add, bp_mul, bp_scale, cubic_J, exact_contractions, paired_coefficients,
)
from quadratic_euler_jet import (  # noqa: E402
    horizon_output, newton_coefficients, time_polynomial_from_newton,
)
from mfp_gaussian_calculus.depth_order5_scalar.primary.moving_scalar_extension import (  # noqa: E402
    assemble_moving_recurrence,
)
from mfp_gaussian_calculus.order5.compiler.factored_expression import (  # noqa: E402
    evaluate_polynomial_activation,
)


def s_add(*values):
    out = [Q(0)] * 6
    for value in values:
        for k, x in enumerate(value):
            out[k] += x
    return out


def s_mul(a, b):
    out = [Q(0)] * 6
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i+j <= 5:
                out[i+j] += x*y
    return out


def s_scale(c, a):
    return [Q(c)*x for x in a]


def s_pow(a, exponent):
    out = [Q(1),Q(0),Q(0),Q(0),Q(0),Q(0)]
    for _ in range(exponent):
        out = s_mul(out,a)
    return out


# A deliberately asymmetric degree-five polynomial on R^2, at theta0=0.
FPOLY = {
    (1,0): Q(2), (0,1): Q(-1),
    (2,0): Q(3,2), (1,1): Q(-2), (0,2): Q(5,2),
    (3,0): Q(2,3), (2,1): Q(-3,2), (1,2): Q(4,3), (0,3): Q(5,6),
    (4,0): Q(-1,4), (3,1): Q(2,3), (2,2): Q(5,4),
    (1,3): Q(-7,6), (0,4): Q(3,8),
    (5,0): Q(1,10), (4,1): Q(-2,5), (3,2): Q(7,12),
    (2,3): Q(-5,9), (1,4): Q(11,20), (0,5): Q(-1,15),
}


def derivative_poly(poly, coordinate):
    out = {}
    for exponent, coefficient in poly.items():
        if exponent[coordinate]:
            child = list(exponent)
            factor = child[coordinate]
            child[coordinate] -= 1
            out[tuple(child)] = coefficient*factor
    return out


def compose(poly, x, y):
    out = [Q(0)]*6
    for (i,j), coefficient in poly.items():
        out = s_add(out, s_scale(coefficient, s_mul(s_pow(x,i),s_pow(y,j))))
    return out


def direct_fifth(N):
    x = [Q(0)]*6
    y = [Q(0)]*6
    gx = derivative_poly(FPOLY,0)
    gy = derivative_poly(FPOLY,1)
    h = [Q(0),Q(1),Q(0),Q(0),Q(0),Q(0)]
    for _ in range(N):
        oldx, oldy = x, y
        x = s_add(oldx,s_mul(h,compose(gx,oldx,oldy)))
        y = s_add(oldy,s_mul(h,compose(gy,oldx,oldy)))
    return compose(FPOLY,x,y)[5]


def tensor(order):
    out = {}
    for indices in product(range(2), repeat=order):
        counts = (indices.count(0), indices.count(1))
        coefficient = FPOLY.get(counts,Q(0))
        # derivative of x^i y^j at zero
        fact = 1
        for k in range(1,counts[0]+1): fact *= k
        for k in range(1,counts[1]+1): fact *= k
        out[indices] = coefficient*fact
    return out


def contract(T, *vectors):
    return sum((value * prod(vectors[k][index] for k,index in enumerate(indices))
                for indices,value in T.items()),Q(0))


def matvec(H,v):
    return [sum((H[(i,j)]*v[j] for j in range(2)),Q(0)) for i in range(2)]


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),Q(0))


def universal_audit():
    p = [FPOLY.get((1,0),Q(0)),FPOLY.get((0,1),Q(0))]
    H,T,U,V = tensor(2),tensor(3),tensor(4),tensor(5)
    A = matvec(H,p)
    B = [sum((T[(i,j,k)]*p[j]*p[k] for j in range(2) for k in range(2)),Q(0)) for i in range(2)]
    c = matvec(H,A)
    invariants = (
        contract(V,p,p,p,p,p), contract(U,A,p,p,p), dot(B,B), dot(B,c),
        contract(T,A,A,p), dot(c,c),
    )
    for N in range(9):
        weights = coefficient_at_integer(N)
        predicted = sum((x*y for x,y in zip(weights,invariants)),Q(0))
        actual = direct_fifth(N)
        if predicted != actual:
            raise AssertionError((N,predicted,actual))


def bp_eval(poly,a,b):
    return sum((coefficient*a**i*b**j for (i,j),coefficient in poly.items()),Q(0))


def unit_ellipse_reduction(poly):
    """Reduce an even polynomial using a^2=1-3y, b^2=y."""
    out = {}
    from math import comb
    for (pa,pb),coefficient in poly.items():
        if pa % 2 or pb % 2:
            raise AssertionError((pa,pb))
        ia,ib=pa//2,pb//2
        for k in range(ia+1):
            degree=ib+k
            out[degree]=out.get(degree,Q(0))+coefficient*comb(ia,k)*Q(-3)**k
    return {k:v for k,v in out.items() if v}


def quadratic_contraction_audit():
    # p=q=1/2 is exactly normalized: p^2+3q^2=1.
    activation = (Q(0),Q(1,2),Q(1,2))
    assembled = assemble_moving_recurrence(2)
    invariants = exact_contractions()
    expressions = {
        "I1": assembled.frozen.straight5,
        "I2": assembled.frozen.gram31,
        "I3": assembled.frozen.gram22,
    }
    for name,expr in expressions.items():
        actual = evaluate_polynomial_activation(expr,activation)
        predicted = bp_eval(invariants[name],Q(1,2),Q(1,2))
        if actual != predicted:
            raise AssertionError((name,predicted,actual))

    I1,I2,I3,I4,I5,I6=(invariants[f"I{k}"] for k in range(1,7))
    reconstructed_C = bp_add(
        bp_scale(2,I1),bp_scale(22,I2),bp_scale(14,I3),bp_scale(30,I4),
        bp_scale(36,I5),bp_scale(16,I6),
    )
    actual_C = evaluate_polynomial_activation(assembled.C,activation)
    predicted_C = bp_eval(reconstructed_C,Q(1,2),Q(1,2))
    if actual_C != predicted_C:
        raise AssertionError((predicted_C,actual_C))


def chronological_dag_audit():
    """Compare every paired t coefficient against the direct OMFP DAG."""
    outputs = [horizon_output(N) for N in range(6)]

    fifth_values = [output.h_coefficient(5) for output in outputs]
    fifth_newton = newton_coefficients(fifth_values)
    gamma5 = time_polynomial_from_newton(fifth_newton,5)
    direct_pair5 = [bp_scale(Q(2**d-32),gamma5[d]) for d in range(5)]
    contraction_pair5 = paired_coefficients(exact_contractions())
    for d in range(1,5):
        discrepancy=bp_add(direct_pair5[d],bp_scale(-1,contraction_pair5[d]))
        if unit_ellipse_reduction(discrepancy):
            raise AssertionError(("fifth paired coefficient",d,
                                  unit_ellipse_reduction(discrepancy)))
    if gamma5[5] and bp_scale(Q(32-32),gamma5[5]):
        raise AssertionError("degree-five cancellation failed")

    third_values = [output.h_coefficient(3) for output in outputs[:4]]
    third_newton = newton_coefficients(third_values)
    gamma3 = time_polynomial_from_newton(third_newton,3)
    direct_pair3 = [bp_scale(Q(2**d-8),gamma3[d]) for d in range(4)]
    J = cubic_J()
    expected_pair3 = [{},bp_scale(Q(-1,2),J),J,{}]
    for d in range(1,4):
        discrepancy=bp_add(direct_pair3[d],bp_scale(-1,expected_pair3[d]))
        if unit_ellipse_reduction(discrepancy):
            raise AssertionError(("cubic paired coefficient",d,
                                  unit_ellipse_reduction(discrepancy)))


if __name__ == "__main__":
    universal_audit()
    quadratic_contraction_audit()
    chronological_dag_audit()
    print("PASS: independent 2D Euler jet, chronological OMFP DAG, and exact quadratic contraction audits")
