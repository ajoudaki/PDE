#!/usr/bin/env python3
"""Exact width-first failure of coefficientwise full/frozen deletion order."""

from fractions import Fraction as Q
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "temporary_quadratic_l2_order5"))

import quadratic_euler_jet as dag  # noqa: E402
from search_signfree_full_vs_frozen import difference_coefficients  # noqa: E402


EXPECTED_H11 = Q(
    -50342126934494248177872714327572247743518720000000000,
    375710212613636260325580163599137907799836383538729,
)


def main():
    # a^2+2ab+3b^2=1 exactly.
    activation = (Q(-11, 9), Q(0), Q(10, 27))
    dag.MAX_H = 49
    full_minus_frozen = difference_coefficients(activation)[2]
    assert full_minus_frozen[11] == EXPECTED_H11
    assert EXPECTED_H11 < 0
    print("[h^11](Delta_full-Delta_frozen) =", EXPECTED_H11)
    print("signed deletion coefficientwise order: FAIL (certified)")


if __name__ == "__main__":
    main()
