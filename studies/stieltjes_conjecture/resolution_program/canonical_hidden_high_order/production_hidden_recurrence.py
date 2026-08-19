#!/usr/bin/env python3
"""Exact canonical hidden-observable jets through order sixteen.

This production branch reuses the frozen canonical Gaussian-program recurrence
from ``../canonical_high_order/production_canonical_recurrence.py``.  Its new
terminal contractions are exact coefficient extractions:

    Q1(t) = E_C[X(t)],
    Q2(t) = E_R[Z(t)^2].

Thus ``Q1^(k)(0) = k! E_C[X_k]`` and
``Q2^(k)(0) = k! sum_{p+q=k} E_R[Z_p Z_q]``.  No trajectory closure or
floating-point approximation is introduced.  The recurrence is still run
through degree seventeen so that its complete frozen output jet through
``F^(17)(0)`` remains a mandatory regression gate, but the hidden contract
stops at degree sixteen and does not request ``F^(19)(0)``.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import platform
import sys
import time
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


Rat = Fraction

HERE = Path(__file__).resolve().parent
RESOLUTION = HERE.parent
REPO_ROOT = RESOLUTION.parents[2]
CANONICAL_DIR = RESOLUTION / "canonical_high_order"
BASE_SOURCE = CANONICAL_DIR / "production_canonical_recurrence.py"
BASE_RESULT = CANONICAL_DIR / "PRODUCTION_RESULT.json"
OWN_SOURCE = HERE / "production_hidden_recurrence.py"
CAMPAIGN1_RESULT = (
    RESOLUTION.parent.parent
    / "mean_field_peeling"
    / "quadratic_compiler"
    / "campaign1"
    / "results_order9_q2_order8.json"
)

BASE_SOURCE_SHA256 = (
    "bccec0577ffd205d5625d8e6e1d9c4dba7dab8a7a218edd5a58866ea8606d688"
)
BASE_RESULT_SHA256 = (
    "eadea98387abb473a4eef7c7ea1300b9b65b4d28217db8201b92722840052f4c"
)
CAMPAIGN1_RESULT_SHA256 = (
    "02215aa7c18f3550a19f34b89734b6bf5b66a2825e8aa5bc103517767982ee1a"
)


def _load_base():
    spec = importlib.util.spec_from_file_location(
        "canonical_hidden_frozen_production_base", BASE_SOURCE
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load frozen recurrence from {BASE_SOURCE}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


base = _load_base()


ACCEPTED_FEATURE_DERIVATIVES: tuple[int, ...] = (
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

ACCEPTED_Q1_PREFIX: tuple[int, ...] = (
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

ACCEPTED_Q2_PREFIX: tuple[int, ...] = (
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
class HiddenRecurrenceResult:
    feature_derivatives: list[int]
    q1_derivatives: list[int]
    q2_derivatives: list[int]
    degrees: list[base.DegreeDiagnostics]
    arithmetic: base.ArithmeticDiagnostics
    elapsed_seconds: float
    max_rss_mib: float
    row_wick_cache: int
    column_wick_cache: int


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frozen_hashes() -> dict[str, str]:
    return {
        "base_source": sha256(BASE_SOURCE),
        "base_result": sha256(BASE_RESULT),
        "campaign1_result": sha256(CAMPAIGN1_RESULT),
    }


def verify_frozen_inputs() -> None:
    expected = {
        "base_source": BASE_SOURCE_SHA256,
        "base_result": BASE_RESULT_SHA256,
        "campaign1_result": CAMPAIGN1_RESULT_SHA256,
    }
    actual = frozen_hashes()
    if actual != expected:
        raise AssertionError(
            f"frozen-input hash mismatch: actual={actual}, expected={expected}"
        )
    base.verify_frozen_inputs()

    retained = json.loads(BASE_RESULT.read_text())
    retained_feature = tuple(
        int(retained["feature_derivatives"][str(order)])
        for order in range(18)
    )
    if retained_feature != ACCEPTED_FEATURE_DERIVATIVES:
        raise AssertionError("frozen order-seventeen output jet changed")

    campaign = json.loads(CAMPAIGN1_RESULT.read_text())["observables"]
    campaign_q1 = tuple(
        int(item["lambda_one"]) for item in campaign["q1"]["jets"]
    )
    campaign_q2 = tuple(
        int(item["lambda_one"]) for item in campaign["q2"]["jets"]
    )
    if campaign_q1 != ACCEPTED_Q1_PREFIX:
        raise AssertionError("Campaign-1 canonical Q1 prefix changed")
    if campaign_q2 != ACCEPTED_Q2_PREFIX:
        raise AssertionError("Campaign-1 canonical Q2 prefix changed")


def symmetric_entry(rows: list[list[Rat]], left: int, right: int) -> Rat:
    return rows[left][right] if left >= right else rows[right][left]


def _integer(value: Rat, label: str) -> int:
    if value.denominator != 1:
        raise ArithmeticError(f"nonintegral {label}: {value}")
    return value.numerator


def canonical_hidden_recurrence(
    max_order: int = 17,
    *,
    hidden_max_order: int = 16,
    progress: bool = False,
    wall_cap_seconds: float | None = None,
    memory_cap_mib: float | None = None,
) -> HiddenRecurrenceResult:
    """Run the exact canonical recurrence and contract ``Q1`` and ``Q2``.

    The retained protocol permits at most recurrence degree seventeen and at
    most hidden degree sixteen.  A full production result must use
    ``(max_order, hidden_max_order)=(17,16)``; smaller values are allowed for
    regression tests.
    """

    if not 0 <= max_order <= 17:
        raise ValueError("max_order must lie between zero and seventeen")
    if not 0 <= hidden_max_order <= min(16, max_order):
        raise ValueError(
            "hidden_max_order must lie between zero and min(16, max_order)"
        )
    verify_frozen_inputs()

    dimension = max_order + 2
    arithmetic = base.PolynomialArithmetic()
    row = base.GaussianLaw(dimension, arithmetic)
    column = base.GaussianLaw(dimension, arithmetic)
    a = base.variable(0, dimension)
    u_squared = {tuple([2] + [0] * (dimension - 1)): Rat(1)}

    A = []
    X = []
    Y = []
    Z = []
    B = []
    Qstate = []
    R = []
    xx: list[list[Rat]] = []
    bb: list[list[Rat]] = []
    degree_diagnostics: list[base.DegreeDiagnostics] = []
    started = time.monotonic()

    def check_caps(degree: int) -> None:
        elapsed = time.monotonic() - started
        rss = base.max_rss_mib()
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

        y = base.variable(degree + 1, dimension)
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

            q = base.variable(degree + 1, dimension)
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
        diagnostic = base.DegreeDiagnostics(
            degree=degree,
            elapsed_seconds=elapsed,
            max_rss_mib=base.max_rss_mib(),
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

    q1_derivatives: list[int] = []
    q2_derivatives: list[int] = []
    for degree in range(hidden_max_order + 1):
        q1_coefficient = column.inner(X[degree], {base.zero_monomial(dimension): Rat(1)})
        q2_coefficient = sum(
            row.inner(Z[left], Z[degree - left])
            for left in range(degree + 1)
        )
        q1_derivatives.append(
            _integer(math.factorial(degree) * q1_coefficient, f"Q1^{degree}")
        )
        q2_derivatives.append(
            _integer(math.factorial(degree) * q2_coefficient, f"Q2^{degree}")
        )

    feature_derivatives: list[int] = []
    for degree in range(max_order + 1):
        coefficient = Rat(0)
        for left in range(degree + 1):
            coefficient += row.triple_with_base(Z[left], Z[degree - left])
        for p in range(1, degree + 1):
            q = degree + 1 - p
            coefficient += q * row.inner(A[p], A[q])
        feature_derivatives.append(
            _integer(math.factorial(degree) * coefficient, f"F^{degree}")
        )

    if tuple(feature_derivatives) != ACCEPTED_FEATURE_DERIVATIVES[: max_order + 1]:
        raise AssertionError("canonical output jet does not match frozen F through 17")
    if tuple(q1_derivatives[:9]) != ACCEPTED_Q1_PREFIX[: hidden_max_order + 1]:
        raise AssertionError("Q1 jet does not match Campaign-1 canonical prefix")
    if tuple(q2_derivatives[:9]) != ACCEPTED_Q2_PREFIX[: hidden_max_order + 1]:
        raise AssertionError("Q2 jet does not match Campaign-1 canonical prefix")

    for order in range(1, hidden_max_order + 1):
        expected_q1 = 8 * feature_derivatives[order - 1]
        if q1_derivatives[order] != expected_q1:
            raise AssertionError(
                f"Ward gate failed at order {order}: "
                f"{q1_derivatives[order]} != {expected_q1}"
            )
    if any(q1_derivatives[order] for order in range(1, hidden_max_order + 1, 2)):
        raise AssertionError("Q1 odd-parity gate failed")
    if any(q2_derivatives[order] for order in range(1, hidden_max_order + 1, 2)):
        raise AssertionError("Q2 odd-parity gate failed")

    elapsed = time.monotonic() - started
    check_caps(max_order)
    return HiddenRecurrenceResult(
        feature_derivatives=feature_derivatives,
        q1_derivatives=q1_derivatives,
        q2_derivatives=q2_derivatives,
        degrees=degree_diagnostics,
        arithmetic=arithmetic.diagnostics,
        elapsed_seconds=elapsed,
        max_rss_mib=base.max_rss_mib(),
        row_wick_cache=len(row.cache),
        column_wick_cache=len(column.cache),
    )


def as_document(result: HiddenRecurrenceResult) -> dict[str, object]:
    max_recurrence_order = len(result.feature_derivatives) - 1
    max_hidden_order = len(result.q1_derivatives) - 1
    return {
        "schema": "production_canonical_hidden_recurrence_v1",
        "metric": "D_a + D_u + D_W",
        "arithmetic": "exact fractions.Fraction",
        "recurrence": "equations (5)-(12), canonical specialization",
        "observable_definitions": {
            "q1": "Q1(t)=E_C[X(t)]",
            "q2": "Q2(t)=E_R[Z(t)^2]",
            "q1_contraction": "Q1^(k)(0)=k! E_C[X_k]",
            "q2_contraction": "Q2^(k)(0)=k! sum_{p+q=k} E_R[Z_p Z_q]",
        },
        "source": {
            "path": str(OWN_SOURCE.relative_to(REPO_ROOT)),
            "sha256": sha256(OWN_SOURCE),
        },
        "max_recurrence_order": max_recurrence_order,
        "max_hidden_order": max_hidden_order,
        "feature_derivatives": {
            str(order): str(value)
            for order, value in enumerate(result.feature_derivatives)
        },
        "q1_derivatives": {
            str(order): str(value)
            for order, value in enumerate(result.q1_derivatives)
        },
        "q2_derivatives": {
            str(order): str(value)
            for order, value in enumerate(result.q2_derivatives)
        },
        "gates": {
            "frozen_feature_jet_through_order17": max_recurrence_order == 17,
            "campaign1_q1_prefix_through_order8": max_hidden_order >= 8,
            "campaign1_q2_prefix_through_order8": max_hidden_order >= 8,
            "q1_ward_identity_through_hidden_order": True,
            "q1_q2_odd_derivatives_zero": True,
            "no_floating_point_in_recurrence": True,
            "hidden_terminal_contractions_exact": True,
            "f19_not_attempted": True,
        },
        "frozen_inputs": {
            "base_source": {
                "path": str(BASE_SOURCE.relative_to(REPO_ROOT)),
                "sha256": BASE_SOURCE_SHA256,
            },
            "base_result": {
                "path": str(BASE_RESULT.relative_to(REPO_ROOT)),
                "sha256": BASE_RESULT_SHA256,
            },
            "campaign1_result": {
                "path": str(CAMPAIGN1_RESULT.relative_to(REPO_ROOT)),
                "sha256": CAMPAIGN1_RESULT_SHA256,
            },
        },
        "resources": {
            "elapsed_seconds": result.elapsed_seconds,
            "max_rss_mib": result.max_rss_mib,
            "row_wick_cache_size": result.row_wick_cache,
            "column_wick_cache_size": result.column_wick_cache,
            "python": platform.python_version(),
            "platform": platform.platform(),
        },
        "arithmetic_diagnostics": vars(result.arithmetic),
        "degree_checkpoints": [
            {
                "degree": item.degree,
                "elapsed_seconds": item.elapsed_seconds,
                "max_rss_mib": item.max_rss_mib,
                "row_wick_cache": item.row_wick_cache,
                "column_wick_cache": item.column_wick_cache,
                "terms": item.terms,
            }
            for item in result.degrees
            if item.degree in {8, 13, 15, 17}
        ],
        "interpretation": (
            "finite fixed-order width-limit hidden jets only; Hankel tests "
            "and all-order/positive-time claims are downstream obligations"
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-order", type=int, default=17)
    parser.add_argument("--hidden-max-order", type=int, default=16)
    parser.add_argument("--progress", action="store_true")
    parser.add_argument("--wall-cap-seconds", type=float, default=1800.0)
    parser.add_argument("--memory-cap-mib", type=float, default=8192.0)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = canonical_hidden_recurrence(
        args.max_order,
        hidden_max_order=args.hidden_max_order,
        progress=args.progress,
        wall_cap_seconds=args.wall_cap_seconds,
        memory_cap_mib=args.memory_cap_mib,
    )
    rendered = json.dumps(as_document(result), indent=2) + "\n"
    if args.output is None:
        sys.stdout.write(rendered)
    else:
        args.output.write_text(rendered)
        print(
            f"wrote {args.output} sha256={sha256(args.output)}",
            file=sys.stderr,
            flush=True,
        )


if __name__ == "__main__":
    main()
