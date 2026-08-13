#!/usr/bin/env python3
"""Exact regression from odd F derivatives to the audited K coefficients."""

import sympy as sp


derivatives = [
    111,
    1_685_184,
    77_400_633_120,
    7_315_868_433_079_296,
    1_181_161_141_825_400_561_664,
    291_982_832_387_585_872_335_470_592,
]

s, y = sp.symbols("s y")
f_coefficients = [
    sp.Rational(value, sp.factorial(2 * r + 1))
    for r, value in enumerate(derivatives)
]
F = sum(a * s ** (2 * r + 1) for r, a in enumerate(f_coefficients))

unknown = sp.symbols(f"b0:{len(f_coefficients)}")
inverse = sum(b * y ** (2 * r + 1) for r, b in enumerate(unknown))
composition_order = 2 * len(f_coefficients) + 1
composition = sp.series(
    F.subs(s, inverse), y, 0, composition_order
).removeO().expand()
solution = {}
for r, b in enumerate(unknown):
    equation = sp.Eq(
        composition.subs(solution).coeff(y, 2 * r + 1),
        1 if r == 0 else 0,
    )
    solution[b] = sp.solve(equation, b)[0]

inverse = inverse.subs(solution)
K = sp.series(
    sp.diff(F, s).subs(s, inverse), y, 0, 2 * len(f_coefficients)
).removeO().expand()

expected = [
    sp.Integer(111),
    sp.Rational(280864, 4107),
    -sp.Rational(38443196932, 5616860517),
    sp.Rational(37578479127292096, 12802987609542045),
    -sp.Rational(
        21749547365571716077696,
        13618704359108797313085,
    ),
    sp.Rational(
        2463577914969508668234788122624,
        2514423905282563683042386470725,
    ),
]

for r, target in enumerate(expected):
    actual = sp.factor(K.coeff(y, 2 * r))
    if actual != target:
        raise SystemExit(f"regression failed at y^{2*r}: {actual} != {target}")
    print(f"[y^{2*r}] K = {actual}")

print("all exact coefficient regressions passed")
