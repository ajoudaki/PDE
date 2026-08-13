#!/usr/bin/env python3
"""Exact Sturm-isolation audit for the six sector polynomials."""

from __future__ import annotations

import sympy as sp

from sector_total_nonnegativity import C


def main() -> None:
    x = sp.symbols("x")
    for r, row in enumerate(C):
        # F_lambda^(2r+1)(0)/lambda = sum_P C[r,P] lambda^(P-1).
        polynomial = sp.Poly(sum(sp.Integer(value) * x**p
                                 for p, value in enumerate(row)), x)
        intervals = polynomial.intervals(eps=sp.Rational(1, 10**30))
        assert len(intervals) == polynomial.degree()
        assert all(multiplicity == 1 for _, multiplicity in intervals)
        assert all(upper < 0 for (_, upper), _ in intervals)
        print(
            f"derivative_order={2*r+1} degree={polynomial.degree()} "
            f"isolated_real_simple_negative_roots={len(intervals)}"
        )
    print("certificate=all_six_sector_polynomials_have_only_simple_negative_roots")


if __name__ == "__main__":
    main()
