#!/usr/bin/env python3
"""Exact width-first OMFP check of the one-step top h coefficient.

For psi(x)=a+b*x^2 and q0=E psi(G)^2, the hand calculation gives
    [h^7] F_1 = 1024*b^13*q0^3*(a+3*b)^2*(a+3*b*q0).
At RMS normalization q0=1 this reduces to
    1024*b^13*(a+3*b)^3.
The script checks the general identity at rational sample points in the
exact chronological Wick compiler.  In particular, a=-3,b=1 gives zero.
"""

from fractions import Fraction as Q
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "temporary_quadratic_l2_order5"))

import quadratic_euler_jet as dag  # noqa: E402
from search_signfree_full_vs_frozen import full_output, hcoeff  # noqa: E402


def expected(a, b):
    q0 = a * a + 2 * a * b + 3 * b * b
    return (Q(1024) * b ** 13 * q0 ** 3 * (a + 3 * b) ** 2
            * (a + 3 * b * q0))


def main():
    dag.MAX_H = 7
    for a, b in ((Q(-3), Q(1)), (Q(-4), Q(1)),
                 (Q(2), Q(3)), (Q(-1, 2), Q(2, 3))):
        got = hcoeff(full_output(1, (a, Q(0), b)), 7)
        want = expected(a, b)
        print(a, b, got)
        assert got == want, (a, b, got, want)
    print("centered-quadratic one-step top coefficient: PASS")


if __name__ == "__main__":
    main()
