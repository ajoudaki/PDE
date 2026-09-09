#!/usr/bin/env python3
"""Exact production successor for the canonical jet through order seventeen.

This is the scalar-``alpha=1`` specialization of equations (5)--(12) in
``../POSITIVE_ALPHA_JET_DERIVATION.md``.  It intentionally leaves the frozen
order-thirteen generator and certificate untouched.  Sparse Gaussian
polynomials use exponent tuples and :class:`fractions.Fraction`, as in the
accepted production generator; no floating-point number enters the jet.

The terminal contraction uses the exact identity

    F(t) = E[A(t) Z(t)^2] = E[A(t) A'(t)],

which avoids constructing recurrence states that cannot affect the requested
order.  This is an algebraic dependency cut, not an approximation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import resource
import sys
import time
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


Rat = Fraction
Monomial = tuple[int, ...]
Polynomial = dict[Monomial, Rat]

HERE = Path(__file__).resolve().parent
RESOLUTION = HERE.parent
FROZEN_SOURCE = RESOLUTION / "block_metric_positive_alpha_jet.py"
FROZEN_CERTIFICATE = RESOLUTION / "BLOCK_METRIC_POSITIVE_ALPHA_JET.json"
FROZEN_SOURCE_SHA256 = (
    "4918c797a0290da950d8cb7ef665ded79bac166fdedf1d11c9415421c65f5a92"
)
FROZEN_CERTIFICATE_SHA256 = (
    "39d617e6f97cf9b3fc67904e7741df2936e8c93781823199ba79f9dfaa911e9b"
)

# This accepted prefix is duplicated deliberately: a new run must pass it
# before either new derivative can be accepted.
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


@dataclass
class ArithmeticDiagnostics:
    additions: int = 0
    scalings: int = 0
    polynomial_products: int = 0
    product_term_pairs: int = 0
    inner_products: int = 0
    inner_term_pairs: int = 0
    derivative_expectations: int = 0
    triple_contractions: int = 0
    triple_term_pairs: int = 0
    largest_polynomial_terms: int = 0

    def observe(self, polynomial: Polynomial) -> Polynomial:
        self.largest_polynomial_terms = max(
            self.largest_polynomial_terms, len(polynomial)
        )
        return polynomial


@dataclass
class DegreeDiagnostics:
    degree: int
    elapsed_seconds: float
    max_rss_mib: float
    row_wick_cache: int
    column_wick_cache: int
    terms: dict[str, int]


@dataclass
class RecurrenceResult:
    derivatives: list[int]
    degrees: list[DegreeDiagnostics]
    arithmetic: ArithmeticDiagnostics
    elapsed_seconds: float
    max_rss_mib: float
    row_wick_cache: int
    column_wick_cache: int


def max_rss_mib() -> float:
    """Return process peak RSS in MiB on the Linux campaign host."""

    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def zero_monomial(dimension: int) -> Monomial:
    return (0,) * dimension


def variable(index: int, dimension: int) -> Polynomial:
    powers = [0] * dimension
    powers[index] = 1
    return {tuple(powers): Rat(1)}


class PolynomialArithmetic:
    def __init__(self) -> None:
        self.diagnostics = ArithmeticDiagnostics()

    def add(self, *polynomials: Polynomial) -> Polynomial:
        self.diagnostics.additions += 1
        result: Polynomial = {}
        for polynomial in polynomials:
            for monomial, coefficient in polynomial.items():
                value = result.get(monomial, Rat(0)) + coefficient
                if value:
                    result[monomial] = value
                else:
                    result.pop(monomial, None)
        return self.diagnostics.observe(result)

    def add_scaled(
        self, target: Polynomial, source: Polynomial, scalar: Rat
    ) -> None:
        self.diagnostics.additions += 1
        self.diagnostics.scalings += 1
        if not scalar:
            return
        for monomial, coefficient in source.items():
            value = target.get(monomial, Rat(0)) + scalar * coefficient
            if value:
                target[monomial] = value
            else:
                target.pop(monomial, None)
        self.diagnostics.observe(target)

    def scale(self, polynomial: Polynomial, scalar: Rat) -> Polynomial:
        self.diagnostics.scalings += 1
        if not scalar:
            return {}
        return self.diagnostics.observe(
            {
                monomial: value
                for monomial, coefficient in polynomial.items()
                if (value := coefficient * scalar)
            }
        )

    def product(self, left: Polynomial, right: Polynomial) -> Polynomial:
        self.diagnostics.polynomial_products += 1
        self.diagnostics.product_term_pairs += len(left) * len(right)
        if len(left) > len(right):
            left, right = right, left
        result: Polynomial = {}
        for left_monomial, left_coefficient in left.items():
            for right_monomial, right_coefficient in right.items():
                monomial = tuple(
                    left_power + right_power
                    for left_power, right_power in zip(
                        left_monomial, right_monomial
                    )
                )
                value = (
                    result.get(monomial, Rat(0))
                    + left_coefficient * right_coefficient
                )
                if value:
                    result[monomial] = value
                else:
                    result.pop(monomial, None)
        return self.diagnostics.observe(result)

    def product_sum(
        self,
        terms: Iterable[tuple[Polynomial, Polynomial, Rat]],
    ) -> Polynomial:
        result: Polynomial = {}
        for left, right, scalar in terms:
            self.add_scaled(result, self.product(left, right), scalar)
        return self.diagnostics.observe(result)


class GaussianLaw:
    """Growing centered Gaussian law with an exact Wick cache."""

    def __init__(
        self, dimension: int, arithmetic: PolynomialArithmetic
    ) -> None:
        self.dimension = dimension
        self.arithmetic = arithmetic
        self.covariance = [
            [Rat(0) for _ in range(dimension)] for _ in range(dimension)
        ]
        self.covariance[0][0] = Rat(1)
        self.cache: dict[Monomial, Rat] = {
            zero_monomial(dimension): Rat(1)
        }
        self.cache_hits = 0
        self.cache_misses = 0

    def install_covariance(self, variable_index: int, values: list[Rat]) -> None:
        if len(values) != variable_index:
            raise ValueError("innovation covariance row has wrong length")
        for other in range(1, variable_index + 1):
            value = values[other - 1]
            self.covariance[variable_index][other] = value
            self.covariance[other][variable_index] = value

    def moment(self, powers: Monomial) -> Rat:
        cached = self.cache.get(powers)
        if cached is not None:
            self.cache_hits += 1
            return cached
        self.cache_misses += 1
        if sum(powers) % 2:
            self.cache[powers] = Rat(0)
            return Rat(0)
        left = next(index for index, power in enumerate(powers) if power)
        remainder = list(powers)
        remainder[left] -= 1
        value = Rat(0)
        for right, multiplicity in enumerate(remainder):
            covariance = self.covariance[left][right]
            if not multiplicity or not covariance:
                continue
            remainder[right] -= 1
            value += multiplicity * covariance * self.moment(tuple(remainder))
            remainder[right] += 1
        self.cache[powers] = value
        return value

    def inner(self, left: Polynomial, right: Polynomial) -> Rat:
        diagnostics = self.arithmetic.diagnostics
        diagnostics.inner_products += 1
        diagnostics.inner_term_pairs += len(left) * len(right)
        if len(left) > len(right):
            left, right = right, left
        return sum(
            left_coefficient
            * right_coefficient
            * self.moment(
                tuple(
                    left_power + right_power
                    for left_power, right_power in zip(
                        left_monomial, right_monomial
                    )
                )
            )
            for left_monomial, left_coefficient in left.items()
            for right_monomial, right_coefficient in right.items()
        )

    def derivative_expectation(
        self, polynomial: Polynomial, index: int
    ) -> Rat:
        self.arithmetic.diagnostics.derivative_expectations += 1
        result = Rat(0)
        for monomial, coefficient in polynomial.items():
            multiplicity = monomial[index]
            if not multiplicity:
                continue
            child = list(monomial)
            child[index] -= 1
            result += multiplicity * coefficient * self.moment(tuple(child))
        return result

    def triple_with_base(
        self, left: Polynomial, right: Polynomial
    ) -> Rat:
        """Return ``E[a * left * right]`` without forming the product."""

        diagnostics = self.arithmetic.diagnostics
        diagnostics.triple_contractions += 1
        diagnostics.triple_term_pairs += len(left) * len(right)
        if len(left) > len(right):
            left, right = right, left
        result = Rat(0)
        for left_monomial, left_coefficient in left.items():
            for right_monomial, right_coefficient in right.items():
                monomial = [
                    left_power + right_power
                    for left_power, right_power in zip(
                        left_monomial, right_monomial
                    )
                ]
                monomial[0] += 1
                result += (
                    left_coefficient
                    * right_coefficient
                    * self.moment(tuple(monomial))
                )
        return result


def frozen_hashes() -> dict[str, str]:
    return {
        "source": hashlib.sha256(FROZEN_SOURCE.read_bytes()).hexdigest(),
        "certificate": hashlib.sha256(
            FROZEN_CERTIFICATE.read_bytes()
        ).hexdigest(),
    }


def verify_frozen_inputs() -> None:
    hashes = frozen_hashes()
    if hashes["source"] != FROZEN_SOURCE_SHA256:
        raise AssertionError(f"frozen source hash mismatch: {hashes['source']}")
    if hashes["certificate"] != FROZEN_CERTIFICATE_SHA256:
        raise AssertionError(
            f"frozen certificate hash mismatch: {hashes['certificate']}"
        )
    certificate = json.loads(FROZEN_CERTIFICATE.read_text())
    recovered = []
    for order in range(14):
        coefficients = certificate["feature_derivative_polynomials"][str(order)]
        recovered.append(sum(int(value) for value in coefficients))
    if tuple(recovered) != ACCEPTED_PREFIX:
        raise AssertionError("accepted prefix disagrees with frozen certificate")


def symmetric_entry(rows: list[list[Rat]], left: int, right: int) -> Rat:
    return rows[left][right] if left >= right else rows[right][left]


def canonical_recurrence(
    max_order: int = 17,
    *,
    progress: bool = False,
    wall_cap_seconds: float | None = None,
    memory_cap_mib: float | None = None,
) -> RecurrenceResult:
    """Evaluate the exact canonical recurrence through ``max_order``.

    The retained campaign authorizes no extension beyond order seventeen, so
    this implementation refuses a larger request.
    """

    if not 0 <= max_order <= 17:
        raise ValueError("max_order must lie between zero and seventeen")
    verify_frozen_inputs()
    dimension = max_order + 2
    arithmetic = PolynomialArithmetic()
    row = GaussianLaw(dimension, arithmetic)
    column = GaussianLaw(dimension, arithmetic)
    a = variable(0, dimension)
    u_squared = {tuple([2] + [0] * (dimension - 1)): Rat(1)}

    A: list[Polynomial] = []
    X: list[Polynomial] = []
    Y: list[Polynomial] = []
    Z: list[Polynomial] = []
    B: list[Polynomial] = []
    Qstate: list[Polynomial] = []
    R: list[Polynomial] = []
    xx: list[list[Rat]] = []
    bb: list[list[Rat]] = []
    degree_diagnostics: list[DegreeDiagnostics] = []
    started = time.monotonic()

    def check_caps(degree: int) -> None:
        elapsed = time.monotonic() - started
        rss = max_rss_mib()
        if wall_cap_seconds is not None and elapsed > wall_cap_seconds:
            raise TimeoutError(
                f"wall cap exceeded after degree {degree}: {elapsed:.3f}s"
            )
        if memory_cap_mib is not None and rss > memory_cap_mib:
            raise MemoryError(
                f"memory cap exceeded after degree {degree}: {rss:.1f} MiB"
            )

    for degree in range(max_order + 1):
        if degree == 0:
            A.append(a)
            X.append(u_squared)
        else:
            A.append(
                arithmetic.product_sum(
                    (
                        Z[left],
                        Z[degree - 1 - left],
                        Rat(1, degree),
                    )
                    for left in range(degree)
                )
            )
            X.append(
                arithmetic.product_sum(
                    (
                        X[left],
                        R[degree - 1 - left],
                        Rat(8, degree),
                    )
                    for left in range(degree)
                )
            )

        xx_row = [column.inner(X[degree], X[j]) for j in range(degree + 1)]
        xx.append(xx_row)
        row.install_covariance(degree + 1, xx_row)

        y = variable(degree + 1, dimension)
        for j in range(degree):
            response = column.derivative_expectation(X[degree], j + 1)
            arithmetic.add_scaled(y, B[j], response)
        Y.append(y)

        z = dict(y)
        for b_degree in range(degree):
            remaining = degree - 1 - b_degree
            memory_weight = Rat(0)
            for x_left in range(remaining + 1):
                x_right = remaining - x_left
                memory_weight += (
                    Rat(2, b_degree + x_left + 1)
                    * symmetric_entry(xx, x_left, x_right)
                )
            arithmetic.add_scaled(z, B[b_degree], memory_weight)
        Z.append(arithmetic.diagnostics.observe(z))

        if degree == max_order:
            terms = {
                "A": len(A[-1]),
                "X": len(X[-1]),
                "Y": len(Y[-1]),
                "Z": len(Z[-1]),
                "B": 0,
                "Q": 0,
                "R": 0,
            }
        else:
            B.append(
                arithmetic.product_sum(
                    (A[left], Z[degree - left], Rat(1))
                    for left in range(degree + 1)
                )
            )
            bb_row = [row.inner(B[degree], B[j]) for j in range(degree + 1)]
            bb.append(bb_row)
            column.install_covariance(degree + 1, bb_row)

            q = variable(degree + 1, dimension)
            for j in range(degree + 1):
                response = row.derivative_expectation(B[degree], j + 1)
                arithmetic.add_scaled(q, X[j], response)
            Qstate.append(q)

            r = dict(q)
            for x_degree in range(degree):
                remaining = degree - 1 - x_degree
                memory_weight = Rat(0)
                for b_left in range(remaining + 1):
                    b_right = remaining - b_left
                    memory_weight += (
                        Rat(2, x_degree + b_left + 1)
                        * symmetric_entry(bb, b_left, b_right)
                    )
                arithmetic.add_scaled(r, X[x_degree], memory_weight)
            R.append(arithmetic.diagnostics.observe(r))
            terms = {
                "A": len(A[-1]),
                "X": len(X[-1]),
                "Y": len(Y[-1]),
                "Z": len(Z[-1]),
                "B": len(B[-1]),
                "Q": len(Qstate[-1]),
                "R": len(R[-1]),
            }

        elapsed = time.monotonic() - started
        diagnostic = DegreeDiagnostics(
            degree=degree,
            elapsed_seconds=elapsed,
            max_rss_mib=max_rss_mib(),
            row_wick_cache=len(row.cache),
            column_wick_cache=len(column.cache),
            terms=terms,
        )
        degree_diagnostics.append(diagnostic)
        if progress:
            print(
                f"degree={degree} elapsed={elapsed:.3f}s "
                f"rss={diagnostic.max_rss_mib:.1f}MiB "
                f"terms={json.dumps(terms, sort_keys=True)} "
                f"caches=({len(row.cache)},{len(column.cache)})",
                file=sys.stderr,
                flush=True,
            )
        check_caps(degree)

    derivatives: list[int] = []
    for degree in range(max_order + 1):
        # The unavailable p=0 term is contracted as
        # E[A_0 sum_{r+s=k} Z_r Z_s].
        coefficient = Rat(0)
        for left in range(degree + 1):
            coefficient += row.triple_with_base(Z[left], Z[degree - left])
        # All remaining A_p and A_q states have already been constructed.
        for p in range(1, degree + 1):
            q = degree + 1 - p
            coefficient += q * row.inner(A[p], A[q])
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
    check_caps(max_order)
    return RecurrenceResult(
        derivatives=derivatives,
        degrees=degree_diagnostics,
        arithmetic=arithmetic.diagnostics,
        elapsed_seconds=elapsed,
        max_rss_mib=max_rss_mib(),
        row_wick_cache=len(row.cache),
        column_wick_cache=len(column.cache),
    )


def as_document(result: RecurrenceResult, max_order: int) -> dict[str, object]:
    return {
        "schema": "production_canonical_recurrence_v1",
        "metric": "D_a + D_u + D_W",
        "alpha": "1",
        "arithmetic": "exact fractions.Fraction",
        "recurrence": "equations (5)-(12), canonical specialization",
        "observable_contraction": "F=E[A A']",
        "max_order": max_order,
        "feature_derivatives": {
            str(order): str(value)
            for order, value in enumerate(result.derivatives)
        },
        "new_F15": str(result.derivatives[15]) if max_order >= 15 else None,
        "new_F17": str(result.derivatives[17]) if max_order >= 17 else None,
        "gates": {
            "frozen_source_sha256": FROZEN_SOURCE_SHA256,
            "frozen_certificate_sha256": FROZEN_CERTIFICATE_SHA256,
            "accepted_prefix_through_order13": max_order >= 13,
            "all_even_derivatives_zero": all(
                result.derivatives[order] == 0
                for order in range(0, max_order + 1, 2)
            ),
            "no_floating_point_in_recurrence": True,
            "terminal_dependency_cut_exact": True,
        },
        "resources": {
            "elapsed_seconds": result.elapsed_seconds,
            "max_rss_mib": result.max_rss_mib,
            "python": platform.python_version(),
            "platform": platform.platform(),
        },
        "diagnostics": {
            "row_wick_cache_size": result.row_wick_cache,
            "column_wick_cache_size": result.column_wick_cache,
            "arithmetic": vars(result.arithmetic),
            "by_degree": [
                {
                    "degree": item.degree,
                    "elapsed_seconds": item.elapsed_seconds,
                    "max_rss_mib": item.max_rss_mib,
                    "row_wick_cache": item.row_wick_cache,
                    "column_wick_cache": item.column_wick_cache,
                    "terms": item.terms,
                }
                for item in result.degrees
            ],
        },
        "interpretation": (
            "finite fixed-order width-limit jet only; no all-order or "
            "positive-time trajectory claim"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-order", type=int, default=17)
    parser.add_argument("--progress", action="store_true")
    parser.add_argument("--wall-cap-seconds", type=float, default=1800.0)
    parser.add_argument("--memory-cap-mib", type=float, default=8192.0)
    args = parser.parse_args()
    result = canonical_recurrence(
        args.max_order,
        progress=args.progress,
        wall_cap_seconds=args.wall_cap_seconds,
        memory_cap_mib=args.memory_cap_mib,
    )
    json.dump(as_document(result, args.max_order), sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
