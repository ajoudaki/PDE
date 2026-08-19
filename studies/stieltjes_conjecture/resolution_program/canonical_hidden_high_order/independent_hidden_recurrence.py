#!/usr/bin/env python3
"""Independent exact canonical jets for both hidden squared-RMS observables.

This implementation extends the packed-monomial/Isserlis formulation in
``canonical_high_order/independent_canonical_recurrence.py``.  It deliberately
does not import the production hidden-observable implementation or any of its
results.  The only shared code is the already-audited independent sparse
polynomial and Gaussian-law substrate; the recurrence and all three observable
contractions are written here.

For the canonical metric ``D_a + D_u + D_W`` the scalar Taylor states are

    X(t) = u(t)^2,
    Z(t) = second-hidden preactivation,
    A(t) = readout,

and the exact width-limit observables are

    F(t)  = E[A(t) Z(t)^2],
    Q1(t) = E[X(t)],
    Q2(t) = E[Z(t)^2].

The program emits ordinary derivatives at zero, not divided-power
coefficients.  Every calculation uses :class:`fractions.Fraction`.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import resource
import sys
import time
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
BASE_SOURCE = (
    HERE.parent / "canonical_high_order" / "independent_canonical_recurrence.py"
)


def _load_independent_base():
    """Load only the pre-existing independent algebra substrate."""

    name = "_canonical_hidden_independent_base"
    specification = importlib.util.spec_from_file_location(name, BASE_SOURCE)
    if specification is None or specification.loader is None:
        raise ImportError(f"cannot load independent base from {BASE_SOURCE}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[name] = module
    specification.loader.exec_module(module)
    return module


BASE = _load_independent_base()
Rat = Fraction
Polynomial = dict[int, Rat]


# The output derivatives are established input to this hidden-observable run.
# Freezing the complete prefix through order seventeen turns the output into a
# regression gate rather than a new candidate result.
ACCEPTED_FEATURE: tuple[int, ...] = (
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
    0,
    49_079_184_579_077_107_476_764_629_402_991_788_032,
    0,
    30_555_969_894_096_099_495_444_855_650_521_777_374_167_040,
)


# Canonical lambda=1 rows from the frozen Campaign-1 multi-root result.
ACCEPTED_Q1: tuple[int, ...] = (
    1,
    0,
    888,
    0,
    13_481_472,
    0,
    619_205_064_960,
    0,
    58_526_947_464_634_368,
)

ACCEPTED_Q2: tuple[int, ...] = (
    3,
    0,
    12_372,
    0,
    311_319_936,
    0,
    19_984_529_682_816,
    0,
    2_441_783_779_120_539_648,
)


@dataclass
class DegreeDiagnostic:
    degree: int
    elapsed_seconds: float
    max_rss_mib: float
    row_wick_cache: int
    column_wick_cache: int
    terms: dict[str, int]


@dataclass
class HiddenRecurrenceResult:
    feature_derivatives: list[int]
    q1_derivatives: list[int]
    q2_derivatives: list[int]
    diagnostics: list[DegreeDiagnostic]
    elapsed_seconds: float
    max_rss_mib: float
    gates: dict[str, bool]


def max_rss_mib() -> float:
    """Return process peak RSS in MiB on Linux."""

    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def _integral(value: Rat, *, label: str) -> int:
    if value.denominator != 1:
        raise ArithmeticError(f"nonintegral {label}: {value}")
    return value.numerator


def _feature_derivatives(
    A: list[Polynomial],
    Z: list[Polynomial],
    row_law,
    max_order: int,
) -> list[int]:
    """Contract ``F=E[A A']`` without constructing ``A[max_order+1]``."""

    answer: list[int] = []
    for degree in range(max_order + 1):
        coefficient = Rat(0)
        # This is the missing (degree+1) E[A0 A_{degree+1}] contribution.
        for left in range(degree // 2 + 1):
            right = degree - left
            multiplicity = 1 if left == right else 2
            coefficient += multiplicity * row_law.triple_with_monomial(
                BASE.unit(0), Z[left], Z[right]
            )
        # All other coefficients are available as inner products of A rows.
        for left in range(1, degree + 1):
            right = degree + 1 - left
            coefficient += right * row_law.inner(A[left], A[right])
        derivative = math.factorial(degree) * coefficient
        answer.append(_integral(derivative, label=f"F derivative {degree}"))
    return answer


def _q1_derivatives(
    X: list[Polynomial],
    column_law,
    max_order: int,
) -> list[int]:
    """Contract ``Q1=E[X]`` from ordinary Taylor coefficients of X."""

    return [
        _integral(
            math.factorial(degree) * column_law.expectation(X[degree]),
            label=f"Q1 derivative {degree}",
        )
        for degree in range(max_order + 1)
    ]


def _q2_derivatives(
    Z: list[Polynomial],
    row_law,
    max_order: int,
) -> list[int]:
    """Contract ``Q2=E[Z^2]`` without materializing squared polynomials."""

    answer: list[int] = []
    for degree in range(max_order + 1):
        coefficient = Rat(0)
        for left in range(degree // 2 + 1):
            right = degree - left
            multiplicity = 1 if left == right else 2
            coefficient += multiplicity * row_law.inner(Z[left], Z[right])
        answer.append(
            _integral(
                math.factorial(degree) * coefficient,
                label=f"Q2 derivative {degree}",
            )
        )
    return answer


def canonical_hidden_recurrence(
    max_feature_order: int,
    max_hidden_order: int,
    *,
    progress: bool = False,
    wall_cap_seconds: float | None = None,
    memory_cap_mib: float | None = None,
) -> HiddenRecurrenceResult:
    """Run the exact canonical recurrence and contract F, Q1, and Q2."""

    if max_feature_order < 0 or max_hidden_order < 0:
        raise ValueError("orders must be nonnegative")
    if max_hidden_order > max_feature_order:
        raise ValueError("hidden order cannot exceed constructed feature order")

    variable_count = max_feature_order + 2
    row_law = BASE.GaussianLaw(variable_count)
    column_law = BASE.GaussianLaw(variable_count)
    a = BASE.gaussian_variable(0)
    u_squared = {2: Rat(1)}

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

    for degree in range(max_feature_order + 1):
        if degree == 0:
            A.append(a)
            X.append(u_squared)
        else:
            # A_k = k^{-1} sum_{p+q=k-1} Z_p Z_q.
            a_terms: list[tuple[Polynomial, Polynomial, Rat]] = []
            for left in range((degree - 1) // 2 + 1):
                right = degree - 1 - left
                multiplicity = 1 if left == right else 2
                a_terms.append((Z[left], Z[right], Rat(multiplicity, degree)))
            A.append(BASE.product_sum(a_terms))

            # X_k = (8/k) sum_{p+q=k-1} X_p R_q.
            X.append(
                BASE.product_sum(
                    (
                        X[left],
                        R[degree - 1 - left],
                        Rat(8, degree),
                    )
                    for left in range(degree)
                )
            )

        # Row innovation and fixed-matrix forward response.
        xx_row = [column_law.inner(X[degree], X[j]) for j in range(degree + 1)]
        xx.append(xx_row)
        row_law.install_covariance(degree + 1, xx_row)

        y = BASE.gaussian_variable(degree + 1)
        for j in range(degree):
            response = column_law.expected_partial(X[degree], j + 1)
            BASE.add_scaled(y, B[j], response)
        Y.append(y)

        z = dict(y)
        for p in range(degree):
            memory_weight = Rat(0)
            remaining = degree - 1 - p
            for q in range(remaining + 1):
                r = remaining - q
                memory_weight += Rat(2, p + q + 1) * BASE.symmetric_entry(
                    xx, q, r
                )
            BASE.add_scaled(z, B[p], memory_weight)
        Z.append(z)

        # Z at the terminal order suffices for F and Q2 through the requested
        # orders.  B/Q/R at that degree have no path back to an earlier row.
        terminal = degree == max_feature_order
        if not terminal:
            B.append(
                BASE.product_sum(
                    (A[p], Z[degree - p], Rat(1))
                    for p in range(degree + 1)
                )
            )

            bb_row = [row_law.inner(B[degree], B[j]) for j in range(degree + 1)]
            bb.append(bb_row)
            column_law.install_covariance(degree + 1, bb_row)

            q_polynomial = BASE.gaussian_variable(degree + 1)
            for j in range(degree + 1):
                response = row_law.expected_partial(B[degree], j + 1)
                BASE.add_scaled(q_polynomial, X[j], response)
            Q.append(q_polynomial)

            r_polynomial = dict(q_polynomial)
            for p in range(degree):
                memory_weight = Rat(0)
                remaining = degree - 1 - p
                for q in range(remaining + 1):
                    r = remaining - q
                    memory_weight += Rat(2, p + q + 1) * BASE.symmetric_entry(
                        bb, q, r
                    )
                BASE.add_scaled(r_polynomial, X[p], memory_weight)
            R.append(r_polynomial)

        diagnostic = DegreeDiagnostic(
            degree=degree,
            elapsed_seconds=time.monotonic() - started,
            max_rss_mib=max_rss_mib(),
            row_wick_cache=len(row_law.cache),
            column_wick_cache=len(column_law.cache),
            terms={
                "A": len(A[-1]),
                "X": len(X[-1]),
                "Y": len(Y[-1]),
                "Z": len(Z[-1]),
                "B": 0 if terminal else len(B[-1]),
                "Q": 0 if terminal else len(Q[-1]),
                "R": 0 if terminal else len(R[-1]),
            },
        )
        diagnostics.append(diagnostic)
        if progress:
            print(
                "degree=" + str(degree)
                + " elapsed=" + f"{diagnostic.elapsed_seconds:.3f}s"
                + " rss=" + f"{diagnostic.max_rss_mib:.1f}MiB"
                + (" terminal_after=Z" if terminal else "")
                + " terms=" + json.dumps(diagnostic.terms, sort_keys=True),
                file=sys.stderr,
                flush=True,
            )
        check_caps(degree)

    feature = _feature_derivatives(A, Z, row_law, max_feature_order)
    q1 = _q1_derivatives(X, column_law, max_hidden_order)
    q2 = _q2_derivatives(Z, row_law, max_hidden_order)

    gates = {
        "accepted_feature_prefix": all(
            feature[k] == expected
            for k, expected in enumerate(ACCEPTED_FEATURE)
            if k <= max_feature_order
        ),
        "accepted_campaign1_q1_prefix": all(
            q1[k] == expected
            for k, expected in enumerate(ACCEPTED_Q1)
            if k <= max_hidden_order
        ),
        "accepted_campaign1_q2_prefix": all(
            q2[k] == expected
            for k, expected in enumerate(ACCEPTED_Q2)
            if k <= max_hidden_order
        ),
        "feature_parity": all(
            feature[k] == 0 for k in range(0, max_feature_order + 1, 2)
        ),
        "q1_parity": all(
            q1[k] == 0 for k in range(1, max_hidden_order + 1, 2)
        ),
        "q2_parity": all(
            q2[k] == 0 for k in range(1, max_hidden_order + 1, 2)
        ),
        "q1_ward_identity": q1[0] == 1
        and all(
            q1[k] == 8 * feature[k - 1]
            for k in range(1, max_hidden_order + 1)
        ),
    }
    if not all(gates.values()):
        failed = [name for name, passed in gates.items() if not passed]
        raise AssertionError("hidden recurrence gates failed: " + ", ".join(failed))

    check_caps(max_feature_order)
    return HiddenRecurrenceResult(
        feature_derivatives=feature,
        q1_derivatives=q1,
        q2_derivatives=q2,
        diagnostics=diagnostics,
        elapsed_seconds=time.monotonic() - started,
        max_rss_mib=max_rss_mib(),
        gates=gates,
    )


def _series(values: list[int]) -> dict[str, str]:
    return {str(order): str(value) for order, value in enumerate(values)}


def as_document(
    result: HiddenRecurrenceResult,
    max_feature_order: int,
    max_hidden_order: int,
) -> dict[str, object]:
    source_path = Path(__file__).resolve()
    repository = HERE.parents[3]
    campaign1 = (
        HERE.parents[2]
        / "mean_field_peeling"
        / "quadratic_compiler"
        / "campaign1"
        / "results_order9_q2_order8.json"
    )
    return {
        "schema": "independent_canonical_hidden_recurrence_v1",
        "metric": "D_a + D_u + D_W",
        "alpha": "1",
        "arithmetic": "exact Fraction",
        "observable_definitions": {
            "Q1": "E[X]=E[u^2]",
            "Q2": "E[Z^2]",
        },
        "max_feature_order": max_feature_order,
        "max_hidden_order": max_hidden_order,
        "feature_derivatives": _series(result.feature_derivatives),
        "q1_derivatives": _series(result.q1_derivatives),
        "q2_derivatives": _series(result.q2_derivatives),
        "gates": result.gates,
        "elapsed_seconds": result.elapsed_seconds,
        "max_rss_mib": result.max_rss_mib,
        "source": {
            "path": str(source_path.relative_to(repository)),
            "sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
        },
        "independent_base": {
            "path": str(BASE_SOURCE.relative_to(repository)),
            "sha256": hashlib.sha256(BASE_SOURCE.read_bytes()).hexdigest(),
        },
        "campaign1_prefix_source": {
            "path": str(campaign1.relative_to(repository)),
            "sha256": hashlib.sha256(campaign1.read_bytes()).hexdigest(),
        },
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
    parser.add_argument("--max-feature-order", type=int, default=17)
    parser.add_argument("--max-hidden-order", type=int, default=16)
    parser.add_argument("--progress", action="store_true")
    parser.add_argument("--wall-cap-seconds", type=float)
    parser.add_argument("--memory-cap-mib", type=float)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = canonical_hidden_recurrence(
        args.max_feature_order,
        args.max_hidden_order,
        progress=args.progress,
        wall_cap_seconds=args.wall_cap_seconds,
        memory_cap_mib=args.memory_cap_mib,
    )
    document = as_document(result, args.max_feature_order, args.max_hidden_order)
    rendered = json.dumps(document, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(rendered)
    else:
        sys.stdout.write(rendered)


if __name__ == "__main__":
    main()
