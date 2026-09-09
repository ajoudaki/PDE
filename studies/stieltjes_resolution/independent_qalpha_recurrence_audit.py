#!/usr/bin/env python3
"""Independent Q[alpha]-valued audit of the positive-alpha jet.

This implementation follows equations (5)--(12) in
``POSITIVE_ALPHA_JET_DERIVATION.md`` directly.  It deliberately does not
import or inspect the production generator
``block_metric_positive_alpha_jet.py``.  Unlike that generator's scalar-node
interpolation route, all stochastic-polynomial coefficients here live in
Q[alpha] throughout the recurrence.
"""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Iterable


Q = Fraction
APoly = tuple[Fraction, ...]  # ascending powers of alpha; () is zero
Exponent = tuple[int, ...]
GPoly = dict[Exponent, APoly]

HERE = Path(__file__).resolve().parent
JET_CERTIFICATE = HERE / "BLOCK_METRIC_POSITIVE_ALPHA_JET.json"
INTERVAL_CERTIFICATE = HERE / "ALPHA_INTERVAL_CERTIFICATE.json"
ALPHA_DEGREE_CAP = 13


def apoly(values: Iterable[int | Fraction]) -> APoly:
    # The requested jet has alpha-degree at most 13.  Since the recurrence
    # uses only addition, multiplication, and rational scaling, discarded
    # higher alpha powers can never feed a coefficient of degree <=13.
    result = tuple(Q(value) for value in values)[: ALPHA_DEGREE_CAP + 1]
    end = len(result)
    while end and result[end - 1] == 0:
        end -= 1
    return result[:end]


AZERO: APoly = ()
AONE: APoly = (Q(1),)


def aadd(left: APoly, right: APoly) -> APoly:
    return apoly(
        (left[index] if index < len(left) else Q(0))
        + (right[index] if index < len(right) else Q(0))
        for index in range(max(len(left), len(right)))
    )


def aneg(value: APoly) -> APoly:
    return tuple(-coefficient for coefficient in value)


def ascale(value: APoly, scalar: int | Fraction) -> APoly:
    scalar = Q(scalar)
    return apoly(scalar * coefficient for coefficient in value)


def amul(left: APoly, right: APoly) -> APoly:
    if not left or not right:
        return AZERO
    result = [Q(0)] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] += left_value * right_value
    return apoly(result)


def alpha_times(value: APoly) -> APoly:
    return (Q(0),) + value if value else AZERO


def gvariable(variable: int, variable_count: int, power: int = 1) -> GPoly:
    exponent = [0] * variable_count
    exponent[variable] = power
    return {tuple(exponent): AONE}


def gconstant(value: APoly, variable_count: int) -> GPoly:
    return {tuple([0] * variable_count): value} if value else {}


def gadd(left: GPoly, right: GPoly) -> GPoly:
    result = dict(left)
    for exponent, coefficient in right.items():
        updated = aadd(result.get(exponent, AZERO), coefficient)
        if updated:
            result[exponent] = updated
        else:
            result.pop(exponent, None)
    return result


def gsum(values: Iterable[GPoly]) -> GPoly:
    result: GPoly = {}
    for value in values:
        result = gadd(result, value)
    return result


def gscale_alpha(value: GPoly, scalar: APoly) -> GPoly:
    if not scalar:
        return {}
    return {
        exponent: product
        for exponent, coefficient in value.items()
        if (product := amul(coefficient, scalar))
    }


def gscale_rational(value: GPoly, scalar: int | Fraction) -> GPoly:
    return {
        exponent: scaled
        for exponent, coefficient in value.items()
        if (scaled := ascale(coefficient, scalar))
    }


def gmul(left: GPoly, right: GPoly) -> GPoly:
    if not left or not right:
        return {}
    result: GPoly = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = tuple(
                left_value + right_value
                for left_value, right_value in zip(left_exponent, right_exponent)
            )
            coefficient = amul(left_coefficient, right_coefficient)
            updated = aadd(result.get(exponent, AZERO), coefficient)
            if updated:
                result[exponent] = updated
            else:
                result.pop(exponent, None)
    return result


class GaussianSpace:
    """Exact Wick functional with Q[alpha]-valued covariance entries."""

    def __init__(self, variable_count: int) -> None:
        self.variable_count = variable_count
        self.covariance = [
            [AZERO for _ in range(variable_count)] for _ in range(variable_count)
        ]
        self.covariance[0][0] = AONE
        self._moment_cache: dict[Exponent, APoly] = {
            tuple([0] * variable_count): AONE
        }

    def set_symbol_covariance(self, left: int, right: int, value: APoly) -> None:
        if left == 0 or right == 0:
            raise ValueError("base variables remain independent of Gaussian symbols")
        self.covariance[left][right] = value
        self.covariance[right][left] = value

    def moment(self, exponent: Exponent) -> APoly:
        cached = self._moment_cache.get(exponent)
        if cached is not None:
            return cached
        total_degree = sum(exponent)
        if total_degree % 2:
            self._moment_cache[exponent] = AZERO
            return AZERO
        first = next(index for index, value in enumerate(exponent) if value)
        after_first = list(exponent)
        after_first[first] -= 1
        result = AZERO
        for partner, multiplicity in enumerate(after_first):
            covariance = self.covariance[first][partner]
            if not multiplicity or not covariance:
                continue
            remainder = after_first[:]
            remainder[partner] -= 1
            term = amul(covariance, self.moment(tuple(remainder)))
            result = aadd(result, ascale(term, multiplicity))
        self._moment_cache[exponent] = result
        return result

    def expectation(self, value: GPoly) -> APoly:
        result = AZERO
        for exponent, coefficient in value.items():
            result = aadd(result, amul(coefficient, self.moment(exponent)))
        return result

    def product_expectation(self, left: GPoly, right: GPoly) -> APoly:
        result = AZERO
        for left_exponent, left_coefficient in left.items():
            for right_exponent, right_coefficient in right.items():
                exponent = tuple(
                    left_value + right_value
                    for left_value, right_value in zip(left_exponent, right_exponent)
                )
                moment = self.moment(exponent)
                if moment:
                    result = aadd(
                        result,
                        amul(amul(left_coefficient, right_coefficient), moment),
                    )
        return result

    def derivative_expectation(self, value: GPoly, variable: int) -> APoly:
        result = AZERO
        for exponent, coefficient in value.items():
            multiplicity = exponent[variable]
            if not multiplicity:
                continue
            derivative_exponent = list(exponent)
            derivative_exponent[variable] -= 1
            moment = self.moment(tuple(derivative_exponent))
            if moment:
                result = aadd(
                    result,
                    ascale(amul(coefficient, moment), multiplicity),
                )
        return result


def direct_qalpha_recurrence(
    max_order: int = 13, *, verbose: bool = False
) -> tuple[dict[int, APoly], dict]:
    """Run equations (5)--(12) directly over Q[alpha]."""

    variable_count = max_order + 2  # base variable and symbols 0,...,max_order
    row = GaussianSpace(variable_count)
    column = GaussianSpace(variable_count)

    A: list[GPoly] = [gvariable(0, variable_count)]
    X: list[GPoly] = [gvariable(0, variable_count, power=2)]
    Y: list[GPoly] = []
    Z: list[GPoly] = []
    B: list[GPoly] = []
    Qstate: list[GPoly] = []
    R: list[GPoly] = []
    exx: list[list[APoly]] = []
    ebb: list[list[APoly]] = []
    term_counts: list[dict[str, int]] = []

    for order in range(max_order + 1):
        if order:
            a_sum = gsum(
                gmul(Z[left], Z[order - 1 - left]) for left in range(order)
            )
            A.append(gscale_rational(a_sum, Q(1, order)))

            x_sum = gsum(
                gmul(X[left], R[order - 1 - left]) for left in range(order)
            )
            X.append(
                gscale_alpha(
                    gscale_rational(x_sum, Q(8, order)),
                    (Q(0), Q(1)),
                )
            )

        # (5), row-side Gaussian covariance from the X overlap.
        exx.append([AZERO for _ in range(order + 1)])
        for other in range(order + 1):
            overlap = column.product_expectation(X[order], X[other])
            exx[order][other] = overlap
            if other < order:
                exx[other].append(overlap)
            row.set_symbol_covariance(order + 1, other + 1, overlap)

        # (6): fixed-matrix forward product and response terms.
        y_order = gvariable(order + 1, variable_count)
        for other in range(order):
            response = column.derivative_expectation(X[order], other + 1)
            y_order = gadd(y_order, gscale_alpha(B[other], response))
        Y.append(y_order)

        # (10): integrated rank-one memory.
        z_order = y_order
        for b_order in range(order):
            remaining = order - 1 - b_order
            for left_x in range(remaining + 1):
                right_x = remaining - left_x
                scalar = ascale(
                    exx[left_x][right_x],
                    Q(2, b_order + left_x + 1),
                )
                z_order = gadd(z_order, gscale_alpha(B[b_order], scalar))
        Z.append(z_order)

        # F^max_order only needs A and Z at this last order.  B_max,
        # xi_max, Q_max, and R_max can affect only later Taylor orders.
        if order == max_order:
            term_counts.append(
                {
                    "order": order,
                    "A": len(A[order]),
                    "X": len(X[order]),
                    "Y": len(Y[order]),
                    "Z": len(Z[order]),
                    "B": 0,
                    "Q": 0,
                    "R": 0,
                }
            )
            if verbose:
                print(
                    "constructed-final-needed-states",
                    json.dumps(term_counts[-1], sort_keys=True),
                    f"row_cache={len(row._moment_cache)}",
                    f"column_cache={len(column._moment_cache)}",
                    file=sys.stderr,
                    flush=True,
                )
            continue

        # (9): B=A*Z coefficient.
        B.append(
            gsum(gmul(A[left], Z[order - left]) for left in range(order + 1))
        )

        # (5), column-side Gaussian covariance from the B overlap.
        ebb.append([AZERO for _ in range(order + 1)])
        for other in range(order + 1):
            overlap = row.product_expectation(B[order], B[other])
            ebb[order][other] = overlap
            if other < order:
                ebb[other].append(overlap)
            column.set_symbol_covariance(order + 1, other + 1, overlap)

        # (7): fixed-matrix backward product and response terms.
        q_order = gvariable(order + 1, variable_count)
        for other in range(order + 1):
            response = row.derivative_expectation(B[order], other + 1)
            q_order = gadd(q_order, gscale_alpha(X[other], response))
        Qstate.append(q_order)

        # (11): transposed integrated rank-one memory.
        r_order = q_order
        for x_order in range(order):
            remaining = order - 1 - x_order
            for left_b in range(remaining + 1):
                right_b = remaining - left_b
                scalar = ascale(
                    ebb[left_b][right_b],
                    Q(2, x_order + left_b + 1),
                )
                r_order = gadd(r_order, gscale_alpha(X[x_order], scalar))
        R.append(r_order)

        term_counts.append(
            {
                "order": order,
                "A": len(A[order]),
                "X": len(X[order]),
                "Y": len(Y[order]),
                "Z": len(Z[order]),
                "B": len(B[order]),
                "Q": len(Qstate[order]),
                "R": len(R[order]),
            }
        )
        if verbose:
            print(
                "constructed",
                json.dumps(term_counts[-1], sort_keys=True),
                f"row_cache={len(row._moment_cache)}",
                f"column_cache={len(column._moment_cache)}",
                file=sys.stderr,
                flush=True,
            )

    # Equation (8) gives [t^k]Z^2=(k+1)A_(k+1).  Therefore (12) can be
    # evaluated by pair overlaps rather than an expensive triple product:
    #
    #   [t^k]E[A Z^2] = sum_{p=0}^k (k-p+1) E[A_p A_(k-p+1)].
    #
    # Construct the sole additional state A_(max_order+1) needed here.
    next_a_order = max_order + 1
    A.append(
        gscale_rational(
            gsum(
                gmul(Z[left], Z[max_order - left])
                for left in range(max_order + 1)
            ),
            Q(1, next_a_order),
        )
    )
    if verbose:
        print(
            f"constructed A_{next_a_order} terms={len(A[next_a_order])}",
            file=sys.stderr,
            flush=True,
        )

    derivatives: dict[int, APoly] = {}
    for order in range(max_order + 1):
        coefficient = AZERO
        for a_order in range(order + 1):
            partner = order - a_order + 1
            overlap = row.product_expectation(A[a_order], A[partner])
            coefficient = aadd(coefficient, ascale(overlap, partner))
        derivatives[order] = ascale(coefficient, math.factorial(order))
        if verbose:
            print(
                f"feature order={order} degree={len(derivatives[order]) - 1}",
                file=sys.stderr,
                flush=True,
            )

    diagnostics = {
        "term_counts": term_counts,
        "row_wick_cache_size": len(row._moment_cache),
        "column_wick_cache_size": len(column._moment_cache),
    }
    return derivatives, diagnostics


def retained_jets() -> dict[int, APoly]:
    document = json.loads(JET_CERTIFICATE.read_text())
    return {
        int(order): apoly(Q(value) for value in coefficients)
        for order, coefficients in document["feature_derivative_polynomials"].items()
    }


def build_audit(*, verbose: bool = False) -> dict[str, object]:
    regenerated, diagnostics = direct_qalpha_recurrence(13, verbose=verbose)
    retained = retained_jets()
    if regenerated != retained:
        mismatches = {
            order: {
                "regenerated": [str(value) for value in regenerated[order]],
                "retained": [str(value) for value in retained[order]],
            }
            for order in range(14)
            if regenerated[order] != retained[order]
        }
        raise AssertionError(f"independent jet mismatch: {mismatches}")

    # Reuse only the separately audited inversion/sign checker, never the
    # production jet generator, and compare its full decisive output.
    from alpha_interval_tools import build_interval_certificate, poly

    odd_jets = [poly(regenerated[order]) for order in range(1, 14, 2)]
    interval = build_interval_certificate(odd_jets, Q(1, 100))
    retained_interval = json.loads(INTERVAL_CERTIFICATE.read_text())
    interval_keys = (
        "baseline_polynomial_ascending",
        "denominator_power",
        "positive_primitive_scale",
        "primitive_numerator_degree",
        "primitive_numerator_ascending",
        "epsilon",
        "P_at_zero",
        "P_at_epsilon",
        "convexity_certificate",
        "bernstein_coefficient_count",
        "all_bernstein_coefficients_strictly_negative",
        "largest_bernstein_coefficient_index",
        "largest_bernstein_coefficient",
    )
    if any(interval[key] != retained_interval[key] for key in interval_keys):
        raise AssertionError("independently regenerated interval certificate mismatch")

    return {
        "schema": "independent_qalpha_recurrence_audit_v1",
        "max_order": 13,
        "implementation": "direct Q[alpha] equations (5)-(12)",
        "imports_production_generator": False,
        "all_jet_coefficients_match": True,
        "decisive_F13_coefficients": [str(value) for value in regenerated[13]],
        "determinant_interval_matches": True,
        "epsilon": "1/100",
        "term_counts": diagnostics["term_counts"],
        "row_wick_cache_size": diagnostics["row_wick_cache_size"],
        "column_wick_cache_size": diagnostics["column_wick_cache_size"],
        "decision": "independent exact reproduction passed",
    }


def main() -> None:
    print(json.dumps(build_audit(verbose=True), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
