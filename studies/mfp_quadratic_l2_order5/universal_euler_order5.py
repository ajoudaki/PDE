#!/usr/bin/env python3
"""Universal order-five coefficient for repeated Euler steps of grad f.

This script uses only the six scalar contractions

 I1=V[p,p,p,p,p], I2=U[A,p,p,p], I3=<B,B>,
 I4=<B,c>, I5=T[A,A,p], I6=<c,c>,

where p=grad f, A=Hp, B=T[p,p], c=H^2p.  It derives the
coefficient of h**5 in f(theta_N), then the fine-minus-coarse paired
coefficient.  All arithmetic is exact.
"""

from fractions import Fraction as Q


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def scale(c, x):
    return tuple(c * a for a in x)


def unit(i):
    return tuple(Q(j == i) for j in range(6))


def coefficient_at_integer(N: int):
    # Scalar coefficients in v1=a*p, v2=b*A,
    # v3=c3*(H A)+d3*B, and
    # v4=e4*(H^3p)+f4*(HB)+g4*T[p,A]+q4*U[p^3].
    a = b = c3 = d3 = e4 = f4 = g4 = q4 = Q(0)
    # p . v5, kept directly in the six-invariant basis.
    pv5 = (Q(0),) * 6

    for _s in range(N):
        # v5 increment, evaluated with the old v1,...,v4.
        inc = (Q(0),) * 6
        # p.Hv4
        inc = add(inc, (0, q4, 0, f4, g4, e4))
        # p.T[v1,v3]
        inc = add(inc, (0, 0, a*d3, a*c3, 0, 0))
        # (1/2)p.T[v2,v2]
        inc = add(inc, scale(Q(1, 2)*b**2, unit(4)))
        # (1/2)p.U[v1,v1,v2]
        inc = add(inc, scale(Q(1, 2)*a**2*b, unit(1)))
        # (1/24)p.V[v1^4]
        inc = add(inc, scale(Q(1, 24)*a**4, unit(0)))
        pv5 = add(pv5, inc)

        # Advance v4, v3, v2, v1, always from old values.
        e4_new = e4 + c3
        f4_new = f4 + d3
        g4_new = g4 + a*b
        q4_new = q4 + Q(1, 6)*a**3
        c3_new = c3 + b
        d3_new = d3 + Q(1, 2)*a**2
        b_new = b + a
        a_new = a + 1
        a, b, c3, d3 = a_new, b_new, c3_new, d3_new
        e4, f4, g4, q4 = e4_new, f4_new, g4_new, q4_new

    # Add the direct Taylor expansion of f(theta_0 + delta_N).
    out = pv5
    # H[v1,v4]
    out = add(out, (0, a*q4, 0, a*f4, a*g4, a*e4))
    # H[v2,v3]
    out = add(out, (0, 0, 0, b*d3, 0, b*c3))
    # 1/2 T[v1,v1,v3]
    out = add(out, (0, 0, Q(1,2)*a**2*d3,
                    Q(1,2)*a**2*c3, 0, 0))
    # 1/2 T[v1,v2,v2]
    out = add(out, scale(Q(1,2)*a*b**2, unit(4)))
    # 1/6 U[v1,v1,v1,v2]
    out = add(out, scale(Q(1,6)*a**3*b, unit(1)))
    # 1/120 V[v1^5]
    out = add(out, scale(Q(1,120)*a**5, unit(0)))
    return out


def poly_add(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_scale(c, a):
    return [c*x for x in a]


def poly_mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def interpolate_forward(values):
    """Degree <=5 polynomial through values at 0,...,5."""
    diffs = [Q(x) for x in values]
    result = [Q(0)]
    falling = [Q(1)]
    factorial = 1
    for k in range(len(values)):
        if k:
            falling = poly_mul(falling, [Q(-(k-1)), Q(1)])
            factorial *= k
        result = poly_add(result, poly_scale(diffs[0] / factorial, falling))
        diffs = [diffs[i+1] - diffs[i] for i in range(len(diffs)-1)]
    return result


def poly_substitute_scale(poly, scale_factor):
    return [c * Q(scale_factor)**k for k, c in enumerate(poly)]


def fmt(poly, var):
    terms = []
    for k, c in enumerate(poly):
        if not c:
            continue
        terms.append(f"({c})*{var}^{k}")
    return " + ".join(terms) if terms else "0"


def interpolate():
    vals = [coefficient_at_integer(k) for k in range(6)]
    polys = []
    for i in range(6):
        polys.append(interpolate_forward([vals[k][i] for k in range(6)]))
    paired = [poly_add(poly_substitute_scale(p, 2), poly_scale(-32, p))
              for p in polys]
    return vals, tuple(polys), tuple(paired)


if __name__ == "__main__":
    vals, polys, paired = interpolate()
    print("[h^5] F_N coefficient weights on (I1,...,I6):")
    for i, p in enumerate(polys, 1):
        print(f"I{i}: {fmt(p, 'N')}")
    print("\n[h^5](F_2t(h)-F_t(2h)) weights:")
    for i, p in enumerate(paired, 1):
        print(f"I{i}: {fmt(p, 't')}")
    print("\nidentity L=2 check requires contractions from the separate Gaussian route")
