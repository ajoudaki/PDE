#!/usr/bin/env python3
"""Independent exact canonical recurrence for the quadratic feature jet.

This file deliberately does not import the production positive-alpha generator
or any of its retained output.  It implements equations (5)--(11) of
``POSITIVE_ALPHA_JET_DERIVATION.md`` directly at ``alpha = 1``.  Sparse
Gaussian polynomials use a packed base-256 monomial representation, while
Gaussian expectations are evaluated by an independent Isserlis recursion.

The observable is contracted through the identity

    F(t) = E[A(t) Z(t)^2] = E[A(t) A'(t)]
         = (1/2) d/dt E[A(t)^2].

All arithmetic is :class:`fractions.Fraction`; no floating-point value enters
the recurrence or any acceptance gate.
"""

from __future__ import annotations

import argparse
import json
import math
import resource
import sys
import time
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


Rat = Fraction
Monomial = int
Polynomial = dict[Monomial, Rat]

# One byte per Gaussian exponent.  Fixed orders through seventeen stay very
# far below exponent 255; addition of packed integers is therefore monomial
# multiplication without inter-byte carries.
EXPONENT_BITS = 8
EXPONENT_MASK = (1 << EXPONENT_BITS) - 1


# Accepted canonical prefix, copied as mathematical input rather than loaded
# from either implementation under comparison.  The run must reproduce every
# entry before a new order is emitted.
ACCEPTED_PREFIX: tuple[int, ...] = (
    0,
    111,
    0,
    1_685_184,
    0,
    77_400_633_120,
    0,
    7_315_868_433_079_296,
    0,
    1_181_161_141_825_400_561_664,
    0,
    291_982_832_387_585_872_335_470_592,
    0,
    102_853_512_279_246_664_353_620_526_022_656,
)


def unit(variable: int) -> Monomial:
    return 1 << (EXPONENT_BITS * variable)


def gaussian_variable(variable: int) -> Polynomial:
    return {unit(variable): Rat(1)}


def add_scaled(target: Polynomial, source: Polynomial, scalar: Rat) -> None:
    """Mutate ``target`` by adding ``scalar * source`` exactly."""

    if not scalar:
        return
    for monomial, coefficient in source.items():
        value = target.get(monomial, Rat(0)) + scalar * coefficient
        if value:
            target[monomial] = value
        elif monomial in target:
            del target[monomial]


def product(left: Polynomial, right: Polynomial) -> Polynomial:
    """Multiply sparse polynomials in the packed-monomial representation."""

    if len(left) > len(right):
        left, right = right, left
    answer: Polynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = left_monomial + right_monomial
            value = (
                answer.get(monomial, Rat(0))
                + left_coefficient * right_coefficient
            )
            if value:
                answer[monomial] = value
            elif monomial in answer:
                del answer[monomial]
    return answer


def product_sum(
    terms: Iterable[tuple[Polynomial, Polynomial, Rat]],
) -> Polynomial:
    answer: Polynomial = {}
    for left, right, scalar in terms:
        add_scaled(answer, product(left, right), scalar)
    return answer


def symmetric_entry(rows: list[list[Rat]], left: int, right: int) -> Rat:
    """Read a symmetric matrix retained by its growing lower triangle."""

    return rows[left][right] if left >= right else rows[right][left]


class GaussianLaw:
    """Growing centered Gaussian law with exact covariance and Wick cache."""

    def __init__(self, variables: int) -> None:
        self.variables = variables
        self.covariance = [
            [Rat(0) for _ in range(variables)] for _ in range(variables)
        ]
        self.covariance[0][0] = Rat(1)
        self.cache: dict[Monomial, Rat] = {0: Rat(1)}

    def install_covariance(self, variable: int, values: list[Rat]) -> None:
        """Install all covariances of a newly exposed innovation variable."""

        if len(values) != variable:
            raise ValueError("a new variable needs covariances through itself")
        # The base scalar is independent of all innovation Gaussians.
        self.covariance[variable][0] = Rat(0)
        self.covariance[0][variable] = Rat(0)
        for other in range(1, variable + 1):
            value = values[other - 1]
            self.covariance[variable][other] = value
            self.covariance[other][variable] = value

    def moment(self, monomial: Monomial) -> Rat:
        cached = self.cache.get(monomial)
        if cached is not None:
            return cached

        scan = monomial
        total_degree = 0
        first = -1
        variable = 0
        while scan:
            exponent = scan & EXPONENT_MASK
            if exponent and first < 0:
                first = variable
            total_degree += exponent
            scan >>= EXPONENT_BITS
            variable += 1
        if total_degree & 1:
            self.cache[monomial] = Rat(0)
            return Rat(0)
        if first < 0:
            return Rat(1)

        first_unit = unit(first)
        remainder = monomial - first_unit
        answer = Rat(0)
        scan = remainder
        other = 0
        while scan:
            multiplicity = scan & EXPONENT_MASK
            covariance = self.covariance[first][other]
            if multiplicity and covariance:
                answer += (
                    multiplicity
                    * covariance
                    * self.moment(remainder - unit(other))
                )
            scan >>= EXPONENT_BITS
            other += 1
        self.cache[monomial] = answer
        return answer

    def expectation(self, polynomial: Polynomial) -> Rat:
        return sum(
            coefficient * self.moment(monomial)
            for monomial, coefficient in polynomial.items()
        )

    def inner(self, left: Polynomial, right: Polynomial) -> Rat:
        """Compute E[left * right] without materializing the product."""

        if len(left) > len(right):
            left, right = right, left
        answer = Rat(0)
        for left_monomial, left_coefficient in left.items():
            for right_monomial, right_coefficient in right.items():
                answer += (
                    left_coefficient
                    * right_coefficient
                    * self.moment(left_monomial + right_monomial)
                )
        return answer

    def expected_partial(self, polynomial: Polynomial, variable: int) -> Rat:
        """Compute E[partial_variable polynomial] without a derivative map."""

        shift = EXPONENT_BITS * variable
        variable_unit = unit(variable)
        answer = Rat(0)
        for monomial, coefficient in polynomial.items():
            exponent = (monomial >> shift) & EXPONENT_MASK
            if exponent:
                answer += (
                    exponent
                    * coefficient
                    * self.moment(monomial - variable_unit)
                )
        return answer

    def triple_with_monomial(
        self,
        monomial: Monomial,
        left: Polynomial,
        right: Polynomial,
    ) -> Rat:
        """Compute E[monomial * left * right] without a product map."""

        if len(left) > len(right):
            left, right = right, left
        answer = Rat(0)
        for left_monomial, left_coefficient in left.items():
            for right_monomial, right_coefficient in right.items():
                answer += (
                    left_coefficient
                    * right_coefficient
                    * self.moment(monomial + left_monomial + right_monomial)
                )
        return answer


@dataclass
class DegreeDiagnostic:
    degree: int
    elapsed_seconds: float
    max_rss_mib: float
    row_wick_cache: int
    column_wick_cache: int
    terms: dict[str, int]


@dataclass
class RecurrenceResult:
    derivatives: list[int]
    diagnostics: list[DegreeDiagnostic]
    elapsed_seconds: float
    max_rss_mib: float


def max_rss_mib() -> float:
    # Linux reports ru_maxrss in KiB.
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def canonical_recurrence(
    max_order: int,
    *,
    progress: bool = False,
    wall_cap_seconds: float | None = None,
    memory_cap_mib: float | None = None,
) -> RecurrenceResult:
    """Run the exact alpha=1 coefficient recursion through ``max_order``."""

    if max_order < 0:
        raise ValueError("max_order must be nonnegative")
    variable_count = max_order + 2
    row_law = GaussianLaw(variable_count)
    column_law = GaussianLaw(variable_count)
    a = gaussian_variable(0)
    u_squared = {2: Rat(1)}  # packed exponent two of the column base Gaussian

    A: list[Polynomial] = []
    X: list[Polynomial] = []
    Y: list[Polynomial] = []
    Z: list[Polynomial] = []
    B: list[Polynomial] = []
    Q: list[Polynomial] = []
    R: list[Polynomial] = []
    xx: list[list[Rat]] = []
    bb: list[list[Rat]] = []
    diagnostics: list[DegreeDiagnostic] = []
    started = time.monotonic()

    for degree in range(max_order + 1):
        if degree == 0:
            A.append(a)
            X.append(u_squared)
        else:
            # A_k = k^{-1} sum_{p+q=k-1} Z_p Z_q.  Combine symmetric
            # pairs explicitly; this is algebraically distinct from the
            # production convolution loop and halves the large products.
            a_terms: list[tuple[Polynomial, Polynomial, Rat]] = []
            for left in range((degree - 1) // 2 + 1):
                right = degree - 1 - left
                multiplicity = 1 if left == right else 2
                a_terms.append((Z[left], Z[right], Rat(multiplicity, degree)))
            A.append(product_sum(a_terms))

            X.append(
                product_sum(
                    (
                        X[left],
                        R[degree - 1 - left],
                        Rat(8, degree),
                    )
                    for left in range(degree)
                )
            )

        # Equation (5), row innovation covariance E_C[X_k X_j].
        xx_row = [column_law.inner(X[degree], X[j]) for j in range(degree + 1)]
        xx.append(xx_row)
        row_law.install_covariance(degree + 1, xx_row)

        # Equation (6), including only already exposed transpose queries.
        y = gaussian_variable(degree + 1)
        for j in range(degree):
            response = column_law.expected_partial(X[degree], j + 1)
            add_scaled(y, B[j], response)
        Y.append(y)

        # Equation (10), consolidated by B_p so no same polynomial is added
        # repeatedly to a growing dictionary.
        z = dict(y)
        for p in range(degree):
            memory_weight = Rat(0)
            remaining = degree - 1 - p
            for q in range(remaining + 1):
                r = remaining - q
                memory_weight += (
                    Rat(2, p + q + 1) * symmetric_entry(xx, q, r)
                )
            add_scaled(z, B[p], memory_weight)
        Z.append(z)

        # Nothing downstream of Z_max can affect F through max_order.  In
        # particular B_max, xi_max, Q_max, and R_max are unnecessary.  This
        # terminal cut is a dependency consequence of (8)--(12), not a
        # numerical approximation.
        if degree == max_order:
            elapsed = time.monotonic() - started
            rss = max_rss_mib()
            diagnostic = DegreeDiagnostic(
                degree=degree,
                elapsed_seconds=elapsed,
                max_rss_mib=rss,
                row_wick_cache=len(row_law.cache),
                column_wick_cache=len(column_law.cache),
                terms={
                    "A": len(A[-1]),
                    "X": len(X[-1]),
                    "Y": len(Y[-1]),
                    "Z": len(Z[-1]),
                    "B": 0,
                    "Q": 0,
                    "R": 0,
                },
            )
            diagnostics.append(diagnostic)
            if progress:
                print(
                    "degree=" + str(degree)
                    + " elapsed=" + f"{elapsed:.3f}s"
                    + " rss=" + f"{rss:.1f}MiB"
                    + " terminal_after=Z"
                    + " terms=" + json.dumps(diagnostic.terms, sort_keys=True),
                    file=sys.stderr,
                    flush=True,
                )
            if wall_cap_seconds is not None and elapsed > wall_cap_seconds:
                raise TimeoutError(
                    f"wall cap exceeded after degree {degree}: {elapsed:.3f}s"
                )
            if memory_cap_mib is not None and rss > memory_cap_mib:
                raise MemoryError(
                    f"memory cap exceeded after degree {degree}: {rss:.1f} MiB"
                )
            break

        # Equation (9).
        B.append(
            product_sum(
                (A[p], Z[degree - p], Rat(1))
                for p in range(degree + 1)
            )
        )

        # Equation (5), column innovation covariance E_R[B_k B_j].
        bb_row = [row_law.inner(B[degree], B[j]) for j in range(degree + 1)]
        bb.append(bb_row)
        column_law.install_covariance(degree + 1, bb_row)

        # Equation (7), including the forward query at this same degree.
        q_polynomial = gaussian_variable(degree + 1)
        for j in range(degree + 1):
            response = row_law.expected_partial(B[degree], j + 1)
            add_scaled(q_polynomial, X[j], response)
        Q.append(q_polynomial)

        # Equation (11), again consolidated by X_p.
        r_polynomial = dict(q_polynomial)
        for p in range(degree):
            memory_weight = Rat(0)
            remaining = degree - 1 - p
            for q in range(remaining + 1):
                r = remaining - q
                memory_weight += (
                    Rat(2, p + q + 1) * symmetric_entry(bb, q, r)
                )
            add_scaled(r_polynomial, X[p], memory_weight)
        R.append(r_polynomial)

        elapsed = time.monotonic() - started
        rss = max_rss_mib()
        diagnostic = DegreeDiagnostic(
            degree=degree,
            elapsed_seconds=elapsed,
            max_rss_mib=rss,
            row_wick_cache=len(row_law.cache),
            column_wick_cache=len(column_law.cache),
            terms={
                "A": len(A[-1]),
                "X": len(X[-1]),
                "Y": len(Y[-1]),
                "Z": len(Z[-1]),
                "B": len(B[-1]),
                "Q": len(Q[-1]),
                "R": len(R[-1]),
            },
        )
        diagnostics.append(diagnostic)
        if progress:
            print(
                "degree=" + str(degree)
                + " elapsed=" + f"{elapsed:.3f}s"
                + " rss=" + f"{rss:.1f}MiB"
                + " terms=" + json.dumps(diagnostic.terms, sort_keys=True),
                file=sys.stderr,
                flush=True,
            )
        if wall_cap_seconds is not None and elapsed > wall_cap_seconds:
            raise TimeoutError(
                f"wall cap exceeded after degree {degree}: {elapsed:.3f}s"
            )
        if memory_cap_mib is not None and rss > memory_cap_mib:
            raise MemoryError(
                f"memory cap exceeded after degree {degree}: {rss:.1f} MiB"
            )

    # F_k/k! is [t^k] E[A A'].  Terms involving A_1,...,A_k use pairwise
    # inner products.  The sole unavailable coefficient A_{k+1} occurs as
    # (k+1) E[A_0 A_{k+1}] = E[A_0 sum_{r+s=k} Z_r Z_s], which is contracted
    # directly without constructing the next recurrence degree.
    derivatives: list[int] = []
    for degree in range(max_order + 1):
        coefficient = Rat(0)
        for left in range(degree // 2 + 1):
            right = degree - left
            multiplicity = 1 if left == right else 2
            coefficient += multiplicity * row_law.triple_with_monomial(
                unit(0), Z[left], Z[right]
            )
        for p in range(1, degree + 1):
            q = degree + 1 - p
            coefficient += q * row_law.inner(A[p], A[q])
        derivative = math.factorial(degree) * coefficient
        if derivative.denominator != 1:
            raise ArithmeticError(
                f"nonintegral feature derivative at order {degree}: {derivative}"
            )
        derivatives.append(derivative.numerator)

    for degree, expected in enumerate(ACCEPTED_PREFIX):
        if degree <= max_order and derivatives[degree] != expected:
            raise AssertionError(
                f"accepted-prefix mismatch at order {degree}: "
                f"{derivatives[degree]} != {expected}"
            )
    for degree in range(0, max_order + 1, 2):
        if derivatives[degree]:
            raise AssertionError(
                f"parity gate failed: F^({degree})(0)={derivatives[degree]}"
            )

    elapsed = time.monotonic() - started
    return RecurrenceResult(
        derivatives=derivatives,
        diagnostics=diagnostics,
        elapsed_seconds=elapsed,
        max_rss_mib=max_rss_mib(),
    )


def as_document(result: RecurrenceResult, max_order: int) -> dict[str, object]:
    return {
        "schema": "independent_canonical_recurrence_v1",
        "metric": "D_a + D_u + D_W",
        "alpha": "1",
        "arithmetic": "exact Fraction",
        "max_order": max_order,
        "feature_derivatives": {
            str(order): str(value)
            for order, value in enumerate(result.derivatives)
        },
        "accepted_prefix_through_order13": max_order >= 13,
        "all_even_derivatives_zero": all(
            result.derivatives[k] == 0 for k in range(0, max_order + 1, 2)
        ),
        "elapsed_seconds": result.elapsed_seconds,
        "max_rss_mib": result.max_rss_mib,
        "diagnostics": [
            {
                "degree": item.degree,
                "elapsed_seconds": item.elapsed_seconds,
                "max_rss_mib": item.max_rss_mib,
                "row_wick_cache": item.row_wick_cache,
                "column_wick_cache": item.column_wick_cache,
                "terms": item.terms,
            }
            for item in result.diagnostics
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-order", type=int, default=15)
    parser.add_argument("--progress", action="store_true")
    parser.add_argument("--wall-cap-seconds", type=float)
    parser.add_argument("--memory-cap-mib", type=float)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = canonical_recurrence(
        args.max_order,
        progress=args.progress,
        wall_cap_seconds=args.wall_cap_seconds,
        memory_cap_mib=args.memory_cap_mib,
    )
    document = as_document(result, args.max_order)
    rendered = json.dumps(document, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(rendered)
    else:
        sys.stdout.write(rendered)


if __name__ == "__main__":
    main()
