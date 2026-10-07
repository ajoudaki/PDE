"""Exact finite checks for WB.2 and the generator's conditional transition law.

This checks small algebraic instances, not the general theorem or the neural
source. Fixed exhaustive instance: two-bit blocks, two states, two recursion
levels; no random sampling, file writes, or network access.
"""

from fractions import Fraction
from itertools import product


def toeplitz(seed, value, width=2):
    diagonals, offset = seed
    result = offset
    for row in range(width):
        parity = 0
        for column in range(width):
            parity ^= ((diagonals >> (row - column + width - 1)) & 1) & (
                (value >> column) & 1
            )
        result ^= parity << row
    return result


hashes = list(product(range(8), range(4)))
points = range(4)
for x in points:
    for y in points:
        if x == y:
            continue
        counts = {(a, b): 0 for a in points for b in points}
        for seed in hashes:
            counts[toeplitz(seed, x), toeplitz(seed, y)] += 1
        assert set(counts.values()) == {2}

for amask in range(16):
    for bmask in range(16):
        a = {x for x in points if (amask >> x) & 1}
        b = {x for x in points if (bmask >> x) & 1}
        mua, mub = Fraction(len(a), 4), Fraction(len(b), 4)
        variance = sum(
            (
                Fraction(sum(toeplitz(seed, x) in b for x in a), 4)
                - mua * mub
            )
            ** 2
            for seed in hashes
        ) / len(hashes)
        assert variance == Fraction(1, 4) * mua * mub * (1 - mub)

# For each transition table and fixed lower hash, verify that averaging the
# upper hash gives the square of the lower transition matrix. WB.3 controls
# the norm before that average; this identity is a separate exact sanity check.
for table_code in range(256):
    table = [
        [(table_code >> (4 * state + x)) & 1 for x in points]
        for state in range(2)
    ]
    for lower in hashes:
        lower_end = [
            [table[table[state][x]][toeplitz(lower, x)] for x in points]
            for state in range(2)
        ]
        matrix = [
            [Fraction(sum(end == target for end in ends), 4) for target in range(2)]
            for ends in lower_end
        ]
        squared = [
            [sum(matrix[i][h] * matrix[h][j] for h in range(2)) for j in range(2)]
            for i in range(2)
        ]
        actual = [[Fraction(0) for _ in range(2)] for _ in range(2)]
        for upper in hashes:
            for initial in range(2):
                for x in points:
                    final = lower_end[lower_end[initial][x]][toeplitz(upper, x)]
                    actual[initial][final] += Fraction(1, 128)
        assert actual == squared

print("PASS: affine pairwise independence, exact WB.2, shared-hash transition law")
