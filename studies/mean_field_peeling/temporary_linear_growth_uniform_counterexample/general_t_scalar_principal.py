"""Exact rational scalar calculation of the general-t narrow-transition symbol."""

from fractions import Fraction
from math import factorial

# A polynomial is keyed by (h-degree, q0-degree,...,q5-degree).
Z = (0,) * 7


def const(x):
    return {Z: Fraction(x)}


def var_h():
    k = list(Z); k[0] = 1
    return {tuple(k): Fraction(1)}


def var_q(i):
    k = list(Z); k[i+1] = 1
    return {tuple(k): Fraction(1)}


def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, Fraction(0)) + v
    return {k: v for k, v in out.items() if v}


def scale(p, a):
    a = Fraction(a)
    return {k: a*v for k, v in p.items() if a*v}


def mul(p, q):
    out = {}
    for a, x in p.items():
        for b, y in q.items():
            k = tuple(a[i] + b[i] for i in range(7))
            if k[0] <= 5 and sum(k[1:]) <= 2:
                out[k] = out.get(k, Fraction(0)) + x*y
    return {k: v for k, v in out.items() if v}


def power(p, n):
    out = const(1)
    for _ in range(n):
        out = mul(out, p)
    return out


H = var_h()
Q = [var_q(i) for i in range(6)]


def qtaylor(dx):
    return add(*(scale(mul(Q[j], power(dx, j)), Fraction(1, factorial(j)))
                 for j in range(6)))


def ftaylor(dx):
    # Set v/s=r=c=1.  This preserves the common r^2*s*v^4 factor.
    out = add(dx, mul(Q[0], dx))
    for j in range(2, 7):
        out = add(out, scale(mul(Q[j-1], power(dx, j)), Fraction(1, factorial(j))))
    return out


def F(n, step_scale):
    dx = const(0)
    hs = scale(H, step_scale)
    for _ in range(n):
        dx = add(dx, mul(hs, add(const(1), qtaylor(dx))))
    return ftaylor(dx)


def principal(t):
    d = add(F(2*t, 1), scale(F(t, 2), -1))
    ans = {}
    for key, value in d.items():
        if key[0] == 5 and sum(key[1:]) == 2:
            derivative_weight = sum(i * key[i+1] for i in range(6))
            if derivative_weight == 4:
                ans[key[1:]] = value
    return ans


def cubic_principal(t):
    d = add(F(2*t, 1), scale(F(t, 2), -1))
    ans = {}
    for key, value in d.items():
        if key[0] == 3 and sum(key[1:]) == 2:
            derivative_weight = sum(i * key[i+1] for i in range(6))
            if derivative_weight == 2:
                ans[key[1:]] = value
    return ans


def differences(values):
    rows = [values]
    while len(rows[-1]) > 1:
        row = rows[-1]
        rows.append([row[i+1]-row[i] for i in range(len(row)-1)])
    return [row[0] for row in rows]


mons = []
for i in range(5):
    k = [0]*6; k[i] += 1; k[4-i] += 1
    kt = tuple(k)
    if kt not in mons:
        mons.append(kt)

vals = {m: [] for m in mons}
for t in range(1, 9):
    p = principal(t)
    print("t", t, {m: p.get(m, 0) for m in mons})
    for m in mons:
        vals[m].append(p.get(m, Fraction(0)))

print("Newton coefficients: p(t)=sum_k a_k*C(t-1,k)")
for m in mons:
    print(m, differences(vals[m]))

# After integration q0*q4 -> +I, q1*q3 -> -I, q2^2 -> +I.
integrated = []
for t in range(1, 9):
    p = principal(t)
    q0q4 = [0]*6; q0q4[0]=q0q4[4]=1
    q1q3 = [0]*6; q1q3[1]=q1q3[3]=1
    q2q2 = [0]*6; q2q2[2]=2
    integrated.append(p.get(tuple(q0q4),0)-p.get(tuple(q1q3),0)+p.get(tuple(q2q2),0))
print("integrated", integrated)
print("integrated Newton", differences(integrated))

# Cubic: q0*q2 integrates as -J and q1^2 as +J.
cubic = []
for t in range(1, 9):
    p = cubic_principal(t)
    q0q2 = [0]*6; q0q2[0]=q0q2[2]=1
    q1q1 = [0]*6; q1q1[1]=2
    cubic.append(-p.get(tuple(q0q2),0)+p.get(tuple(q1q1),0))
print("cubic integrated", cubic)
print("cubic Newton", differences(cubic))
