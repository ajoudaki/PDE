"""Exact monomial moments of centered Gaussian vectors with rational covariance."""

from collections.abc import Sequence
from fractions import Fraction
from functools import lru_cache
from numbers import Integral


def _sequence(value, name):
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        raise TypeError(f"{name} must be a finite sequence")
    return value


def _rational(value):
    if isinstance(value, Fraction):
        return value
    if isinstance(value, Integral) and not isinstance(value, bool):
        return Fraction(int(value))
    raise TypeError("covariance entries must be integers or Fraction values")


def _validate_psd(covariance):
    """Exact Schur-complement test, including zero pivots of singular matrices."""
    matrix = covariance
    while matrix:
        pivot = matrix[0][0]
        if pivot < 0:
            raise ValueError("covariance must be positive semidefinite")
        if pivot == 0:
            # A PSD matrix with a zero diagonal entry has a zero corresponding
            # row: otherwise its 2-by-2 principal minor is strictly negative.
            if any(matrix[0][1:]):
                raise ValueError("a zero covariance pivot must have a zero row")
            matrix = tuple(row[1:] for row in matrix[1:])
        else:
            matrix = tuple(
                tuple(
                    matrix[i][j] - matrix[i][0] * matrix[0][j] / pivot
                    for j in range(1, len(matrix))
                )
                for i in range(1, len(matrix))
            )


def gaussian_moment(
    covariance: Sequence[Sequence[int | Fraction]],
    powers: Sequence[int],
) -> Fraction:
    """Return E[prod_i X_i**powers[i]] for X ~ N(0, covariance), exactly.

    Covariance must be a nonempty square symmetric PSD matrix whose entries
    are integers or Fraction values. Singular and zero covariance are valid;
    floats, booleans and approximate PSD tolerances are not used. Powers must
    be a finite sequence of nonnegative integers of matching length.

    Every argument is validated even for an odd or zero total degree. All
    zero powers give Fraction(1); odd total degree gives Fraction(0).
    Type errors raise TypeError; shape, degree and PSD errors raise ValueError.
    Inputs are never modified. Use lists or tuples for the finite sequences.

    Validation takes O(d**3) rational operations. The locally memoized Wick
    recurrence visits at most prod_i(powers[i]+1) exponent states, with O(d)
    transitions per state and recursion depth at most 1 + sum(powers)//2. Rational
    bit sizes and the number of states can grow rapidly; this is a small-order
    exact building block, not a high-order enumeration engine. No cache is
    shared between calls and no numerical integration is performed.
    """
    rows = _sequence(covariance, "covariance")
    d = len(rows)
    if d == 0:
        raise ValueError("covariance must be nonempty")
    sigma = []
    for row in rows:
        row = _sequence(row, "covariance row")
        if len(row) != d:
            raise ValueError("covariance must be square")
        sigma.append(tuple(_rational(value) for value in row))
    sigma = tuple(sigma)
    if any(sigma[i][j] != sigma[j][i] for i in range(d) for j in range(i)):
        raise ValueError("covariance must be symmetric")

    powers = _sequence(powers, "powers")
    if len(powers) != d:
        raise ValueError("powers must match the covariance dimension")
    if any(isinstance(p, bool) or not isinstance(p, Integral) for p in powers):
        raise TypeError("powers must be nonnegative integers")
    powers = tuple(int(p) for p in powers)
    if any(p < 0 for p in powers):
        raise ValueError("powers must be nonnegative")
    _validate_psd(sigma)

    @lru_cache(maxsize=None)
    def moment(alpha):
        degree = sum(alpha)
        if degree == 0:
            return Fraction(1)
        if degree % 2:
            return Fraction(0)
        i = next(index for index, count in enumerate(alpha) if count)
        remainder = list(alpha)
        remainder[i] -= 1
        result = Fraction(0)
        for j, count in enumerate(remainder):
            if count and sigma[i][j]:
                paired = remainder.copy()
                paired[j] -= 1
                result += count * sigma[i][j] * moment(tuple(paired))
        return result

    try:
        return moment(powers)
    finally:
        moment.cache_clear()
