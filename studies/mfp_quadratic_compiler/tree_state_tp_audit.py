#!/usr/bin/env python3
"""Exact refined-tree obstruction to a direct planar/LGV peeling lift.

`Term.x` stores the actual even exponent of the lower Gaussian variable.
Thus x=2h relative to the `Tree.h` convention in component_recursion.cpp.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations

import graph_compiler_reference as grammar


def unit(term: grammar.Term) -> grammar.Term:
    return grammar.Term(term.a, term.x, term.edges, term.power, 1)


def one_step(term: grammar.Term):
    """Canonical child -> (unit representative, coefficients by hit type)."""
    out = {}
    for hit, child in grammar.differentiate_by_rule(unit(term)):
        key = grammar.forest_key(child)
        if key not in out:
            out[key] = [unit(child), Counter()]
        out[key][1][hit] += child.coef
    return out


def descendants(term: grammar.Term, depth: int):
    """Canonical descendant -> (representative, coefficients by hit word)."""
    current = {grammar.forest_key(term): [unit(term), Counter({(): 1})]}
    for _ in range(depth):
        following = {}
        for representative, histories in current.values():
            for key, (child, hits) in one_step(representative).items():
                if key not in following:
                    following[key] = [child, Counter()]
                for word, old_coefficient in histories.items():
                    for hit, step_coefficient in hits.items():
                        following[key][1][word + (hit,)] += (
                            old_coefficient * step_coefficient
                        )
        current = following
    return current


def determinant2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


ROOT = grammar.Term((1,), (2, 2), ((1, 1),), 1, 1)

# The three canonical states after one derivative.  The labels a, x, w below
# refer to the first root hit.  E is a two-component forest; A and B are trees.
A = grammar.Term((0,), (2, 2, 2, 2), ((1, 1, 1, 1),), 1, 1)
B = grammar.Term(
    (1, 1), (2, 2, 2), ((1, 1, 0), (1, 0, 1)), 1, 1
)
E = grammar.Term((2,), (4, 2, 2), ((0, 1, 1),), 2, 1)
SOURCES = (A, B, E)

# Two connected descendants used for the simplest negative minor.
C = grammar.Term(
    (0, 1, 1),
    (2, 2, 2, 2, 2, 2),
    ((1, 1, 1, 1, 0, 0),
     (1, 0, 0, 0, 1, 0),
     (0, 1, 0, 0, 0, 1)),
    1,
    1,
)
D = grammar.Term(
    (0, 0),
    (2, 2, 2, 2, 2, 2, 2),
    ((1, 1, 1, 1, 0, 0, 0),
     (1, 0, 0, 0, 1, 1, 1)),
    1,
    1,
)

# Two further sinks used in the ordering-independent 3-by-3 obstruction.
Y = grammar.Term(
    (0, 1, 1),
    (2, 2, 2, 2, 2, 2),
    ((1, 1, 1, 1, 0, 0),
     (0, 0, 0, 1, 1, 0),
     (0, 0, 0, 0, 1, 1)),
    1,
    1,
)
Z = grammar.Term(
    (0, 2),
    (2, 2, 2, 4, 2, 2),
    ((1, 1, 1, 1, 0, 0),
     (0, 0, 0, 0, 1, 1)),
    2,
    1,
)


def main() -> None:
    # Independently regenerate and identify the three level-one states.
    generated = one_step(ROOT)
    expected_root_hits = {
        grammar.forest_key(A): Counter({"a": 1}),
        grammar.forest_key(B): Counter({"x": 16}),
        grammar.forest_key(E): Counter({"w": 4}),
    }
    assert {key: hits for key, (_, hits) in generated.items()} == expected_root_hits

    depth_two = [descendants(source, 2) for source in SOURCES]

    # The transparent Python Wick evaluator and the production C++
    # WickEvaluator independently return these same integers.
    wick_c = grammar.leading_expectation_fast(C)
    wick_d = grammar.leading_expectation_fast(D)
    assert (wick_c, wick_d) == (54, 1620)

    key_c, key_d = grammar.forest_key(C), grammar.forest_key(D)
    words = {
        "A->C": depth_two[0][key_c][1],
        "A->D": depth_two[0][key_d][1],
        "B->C": depth_two[1][key_c][1],
        "B->D": depth_two[1][key_d][1],
    }
    assert words == {
        "A->C": Counter({("x", "x"): 768}),
        "A->D": Counter({("x", "a"): 32}),
        "B->C": Counter({("a", "x"): 48, ("x", "a"): 16}),
        "B->D": Counter({("a", "a"): 2}),
    }
    raw_minor = [[768, 32], [64, 2]]
    weighted_minor = [
        [raw_minor[0][0] * wick_c, raw_minor[0][1] * wick_d],
        [raw_minor[1][0] * wick_c, raw_minor[1][1] * wick_d],
    ]
    assert determinant2(raw_minor) == -512
    assert determinant2(weighted_minor) == -44_789_760

    # Build the complete depth-two survivor kernel using common canonical keys.
    all_keys = sorted(set().union(*(set(desc) for desc in depth_two)))
    raw_columns = {}
    survivor_columns = {}
    for key in all_keys:
        representative = next(desc[key][0] for desc in depth_two if key in desc)
        wick = grammar.leading_expectation_fast(representative)
        if not wick:
            continue
        raw_columns[key] = tuple(
            sum(desc[key][1].values()) if key in desc else 0
            for desc in depth_two
        )
        survivor_columns[key] = tuple(value * wick for value in raw_columns[key])
    assert len(survivor_columns) == 22

    # The following three columns alone forbid every source/sink ordering.
    key_y, key_z = grammar.forest_key(Y), grammar.forest_key(Z)
    raw_obstruction = (
        raw_columns[key_c],
        raw_columns[key_y],
        raw_columns[key_z],
    )
    assert raw_obstruction == ((768, 64, 0), (256, 48, 0), (64, 8, 16))
    obstruction = (
        survivor_columns[key_c],
        survivor_columns[key_y],
        survivor_columns[key_z],
    )
    assert obstruction == (
        (41_472, 3_456, 0),
        (41_472, 7_776, 0),
        (25_920, 3_240, 6_480),
    )
    matrix3 = [[column[row] for column in obstruction] for row in range(3)]

    def is_tp2(row_order, column_order):
        for i0, i1 in combinations(range(3), 2):
            for j0, j1 in combinations(range(3), 2):
                i, k = row_order[i0], row_order[i1]
                j, ell = column_order[j0], column_order[j1]
                if (matrix3[i][j] * matrix3[k][ell]
                        - matrix3[i][ell] * matrix3[k][j]) < 0:
                    return False
        return True

    assert not any(
        is_tp2(row_order, column_order)
        for row_order in permutations(range(3))
        for column_order in permutations(range(3))
    )

    print("root hit multiplicities: A=1, B=16, E=4")
    print("two-step hit-word coefficients:", words)
    print("W(C), W(D):", wick_c, wick_d)
    print("raw 2x2:", raw_minor, "det=", determinant2(raw_minor))
    print("Wick-weighted 2x2:", weighted_minor,
          "det=", determinant2(weighted_minor))
    print("ordering-obstruction raw 3x3:",
          [[column[row] for column in raw_obstruction] for row in range(3)])
    print("ordering-obstruction 3x3:", matrix3)
    print("all 36 row/column ordering pairs fail TP2")


if __name__ == "__main__":
    main()
