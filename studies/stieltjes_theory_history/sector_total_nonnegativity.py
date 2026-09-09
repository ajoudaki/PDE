#!/usr/bin/env python3
"""Exact audit of the derivative-order/Wick-sector coefficient matrix.

Rows are derivative orders 1,3,...,11. Columns are Wick-pair sectors P=1,...,12.
All entries are exact integers from the accepted MFP sector certificates.
"""

from __future__ import annotations

from itertools import combinations
from math import comb


C = (
    (36, 75),
    (15552, 243216, 760176, 666240),
    (11197440, 558565632, 5751565056, 21144930336,
     32357889792, 17576484864),
    (11287019520, 1453203763200, 34569399656448,
     297887755714560, 1191606495058944, 2419999440371712,
     2422966824972288, 947374026522624),
    (14627977297920, 4546495309086720, 211436756895006720,
     3490984312448606208, 27185927724027592704,
     114581150906254331904, 277387051973394751488,
     385587855340280672256, 285610646257352368128,
     87101527431460847616),
    (23170716039905280, 17433397654868459520,
     1428455842962100715520, 40114976109177824870400,
     530996753942041626279936, 3868170903724215843717120,
     16894189549156196962566144, 46146109609021522448793600,
     79443613137340581848727552, 83655641930747138444722176,
     49117046434067436406308864, 12285503181066227920404480),
)


def det_bareiss(matrix: list[list[int]]) -> int:
    """Fraction-free exact determinant with row pivoting."""
    n = len(matrix)
    if n == 0:
        return 1
    a = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot_value - a[i][k] * a[k][j]
                if numerator % previous:
                    raise ArithmeticError("Bareiss division was not exact")
                a[i][j] = numerator // previous
        previous = pivot_value
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[-1][-1]


def main() -> None:
    matrix = [list(row) + [0] * (12 - len(row)) for row in C]
    totals = {}
    positive = {}
    zero = {}
    negative = {}
    smallest_positive = {}
    for k in range(1, 7):
        totals[k] = comb(6, k) * comb(12, k)
        positive[k] = zero[k] = negative[k] = 0
        smallest = None
        for rows in combinations(range(6), k):
            for columns in combinations(range(12), k):
                minor = det_bareiss([[matrix[i][j] for j in columns] for i in rows])
                if minor > 0:
                    positive[k] += 1
                    smallest = minor if smallest is None else min(smallest, minor)
                elif minor == 0:
                    zero[k] += 1
                else:
                    negative[k] += 1
        smallest_positive[k] = smallest

    expected = sum(totals.values())
    assert expected == 18_563
    assert sum(negative.values()) == 0
    assert all(positive[k] + zero[k] == totals[k] for k in totals)
    assert [sum(row) for row in C] == [
        111,
        1685184,
        77400633120,
        7315868433079296,
        1181161141825400561664,
        291982832387585872335470592,
    ]

    print("matrix_rows_P1_upward=")
    for row in C:
        print(" ", list(row))
    print("total_minors=", expected)
    for k in range(1, 7):
        print(
            f"order={k} total={totals[k]} positive={positive[k]} "
            f"zero={zero[k]} negative={negative[k]} "
            f"smallest_positive={smallest_positive[k]}"
        )
    print("certificate=all_minors_nonnegative")


if __name__ == "__main__":
    main()
