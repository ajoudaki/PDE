#!/usr/bin/env python3
"""Exact search for negative coefficients in the frozen paired defect."""

from fractions import Fraction as Q
from itertools import product
from math import isqrt

import quadratic_euler_jet as dag
from search_general_poly_comparison import raw_product_moment
from search_signfree_full_vs_frozen import frozen_output, hcoeff


def main():
    dag.MAX_H = 15
    checked = 0
    seen = set()
    for raw_int in product(range(-12, 13), repeat=4):
        if raw_int[-1] == 0 or not (min(raw_int) < 0 < max(raw_int)):
            continue
        first = next(x for x in raw_int if x)
        if first < 0:
            raw_int = tuple(-x for x in raw_int)
        if raw_int in seen:
            continue
        seen.add(raw_int)
        raw = tuple(map(Q, raw_int))
        norm2 = raw_product_moment(raw, (0, 0))
        nr, dr = isqrt(norm2.numerator), isqrt(norm2.denominator)
        if nr*nr != norm2.numerator or dr*dr != norm2.denominator:
            continue
        activation = tuple(x / Q(nr, dr) for x in raw)
        defect = frozen_output(2, activation)-frozen_output(1, activation, 2)
        coefficients = tuple(hcoeff(defect, k) for k in range(16))
        checked += 1
        negative = [(k, c) for k, c in enumerate(coefficients) if c < 0]
        if negative:
            print("FOUND", raw_int, "negative", negative)
            return
        if checked % 100 == 0:
            print("checked", checked)
        if checked >= 1000:
            break
    print("NO COUNTEREXAMPLE; checked", checked)


if __name__ == "__main__":
    main()
