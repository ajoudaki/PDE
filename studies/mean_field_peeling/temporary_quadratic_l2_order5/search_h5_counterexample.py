#!/usr/bin/env python3
"""Search exact normalized rational cubic activations for failed domination."""

from fractions import Fraction as Q
from itertools import product
from math import isqrt

import quadratic_euler_jet as dag
from search_general_poly_comparison import raw_product_moment
from search_signfree_full_vs_frozen import difference_coefficients


def main():
    dag.MAX_H = 5
    checked = 0
    seen = set()
    for raw_int in product(range(-10, 11), repeat=4):
        if raw_int[-1] == 0 or not (min(raw_int) < 0 < max(raw_int)):
            continue
        # Quotient out an overall sign and common scalar cheaply.
        first = next(x for x in raw_int if x)
        if first < 0:
            raw_int = tuple(-x for x in raw_int)
        if raw_int in seen:
            continue
        seen.add(raw_int)
        raw = tuple(map(Q, raw_int))
        norm2 = raw_product_moment(raw, (0, 0))
        numroot, denroot = isqrt(norm2.numerator), isqrt(norm2.denominator)
        if numroot*numroot != norm2.numerator or denroot*denroot != norm2.denominator:
            continue
        norm = Q(numroot, denroot)
        activation = tuple(x/norm for x in raw)
        difference = difference_coefficients(activation)[2]
        checked += 1
        if difference[3] < 0 or difference[5] < 0:
            print("FOUND", raw_int, "norm", norm,
                  "d3", difference[3], "d5", difference[5])
            return
        if checked % 10 == 0:
            print("checked", checked, "last", raw_int,
                  "d3", difference[3], "d5", difference[5])
        if checked >= 60:
            break
    print("NO COUNTEREXAMPLE; checked", checked)


if __name__ == "__main__":
    main()
