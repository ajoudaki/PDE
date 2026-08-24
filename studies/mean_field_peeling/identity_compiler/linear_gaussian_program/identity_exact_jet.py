#!/usr/bin/env python3
"""Exact width-limit jets for identity activation at hidden depths 2 and 3.

Every coordinate state remains linear-Gaussian, so chronological
detransposition reduces to rational covariance algebra.  Two separate
coefficient assemblers are supplied: ordinary Taylor coefficients and actual
derivatives at zero.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable


Q = Fraction
Vector = tuple[Fraction, ...]


def variable(index: int, dimension: int) -> Vector:
    values = [Q(0)] * dimension
    values[index] = Q(1)
    return tuple(values)


def scale(vector: Vector, scalar: Fraction) -> Vector:
    return tuple(scalar * value for value in vector)


def combine(dimension: int, terms: Iterable[tuple[Fraction, Vector]]) -> Vector:
    answer = [Q(0)] * dimension
    for scalar, vector in terms:
        if not scalar:
            continue
        for index, value in enumerate(vector):
            if value:
                answer[index] += scalar * value
    return tuple(answer)


class LinearGaussianLaw:
    """A centered Gaussian family used only through exact covariances."""

    def __init__(self, dimension: int, *, unit_base: bool = False) -> None:
        self.dimension = dimension
        self.covariance = [
            [Q(0) for _ in range(dimension)] for _ in range(dimension)
        ]
        if unit_base:
            self.covariance[0][0] = Q(1)

    def set_covariance(self, left: int, right: int, value: Fraction) -> None:
        current = self.covariance[left][right]
        if current and current != value:
            raise ArithmeticError(
                f"attempted to change covariance ({left}, {right}) "
                f"from {current} to {value}"
            )
        self.covariance[left][right] = value
        self.covariance[right][left] = value

    def inner(self, left: Vector, right: Vector) -> Fraction:
        answer = Q(0)
        for i, left_value in enumerate(left):
            if not left_value:
                continue
            row = self.covariance[i]
            for j, right_value in enumerate(right):
                if right_value and row[j]:
                    answer += left_value * row[j] * right_value
        return answer


@dataclass
class JetResult:
    depth: int
    route: str
    derivatives: list[Fraction]
    elapsed_seconds: float
    support_counts: list[dict[str, int]]


def _support(**fields: Vector) -> dict[str, int]:
    return {name: sum(bool(value) for value in vector) for name, vector in fields.items()}


def depth2_taylor(max_order: int) -> JetResult:
    started = time.perf_counter()
    dimension = max_order + 2
    bottom = LinearGaussianLaw(dimension, unit_base=True)
    top = LinearGaussianLaw(dimension, unit_base=True)
    u = variable(0, dimension)
    a = variable(0, dimension)

    A: list[Vector] = []
    X: list[Vector] = []
    Z: list[Vector] = []
    R: list[Vector] = []
    counts: list[dict[str, int]] = []

    for degree in range(max_order + 1):
        if degree == 0:
            A.append(a)
            X.append(u)
        else:
            A.append(scale(Z[degree - 1], Q(1, degree)))
            X.append(scale(R[degree - 1], Q(1, degree)))

        eta_index = degree + 1
        for other in range(degree + 1):
            top.set_covariance(
                eta_index, other + 1, bottom.inner(X[degree], X[other])
            )
        z_terms: list[tuple[Fraction, Vector]] = [(Q(1), variable(eta_index, dimension))]
        for other in range(degree):
            response = X[degree][other + 1]
            if response:
                z_terms.append((response, A[other]))
        for a_degree in range(degree):
            for x_left in range(degree - a_degree):
                x_right = degree - 1 - a_degree - x_left
                overlap = bottom.inner(X[x_left], X[x_right])
                z_terms.append((Q(overlap, a_degree + x_left + 1), A[a_degree]))
        Z.append(combine(dimension, z_terms))

        xi_index = degree + 1
        for other in range(degree + 1):
            bottom.set_covariance(
                xi_index, other + 1, top.inner(A[degree], A[other])
            )
        r_terms: list[tuple[Fraction, Vector]] = [(Q(1), variable(xi_index, dimension))]
        for other in range(degree + 1):
            response = A[degree][other + 1]
            if response:
                r_terms.append((response, X[other]))
        for x_degree in range(degree):
            for a_left in range(degree - x_degree):
                a_right = degree - 1 - x_degree - a_left
                overlap = top.inner(A[a_left], A[a_right])
                r_terms.append((Q(overlap, x_degree + a_left + 1), X[x_degree]))
        R.append(combine(dimension, r_terms))
        counts.append(_support(A=A[-1], X=X[-1], Z=Z[-1], R=R[-1]))

    derivatives = []
    for degree in range(max_order + 1):
        coefficient = sum(
            (top.inner(A[left], Z[degree - left]) for left in range(degree + 1)),
            Q(0),
        )
        derivatives.append(math.factorial(degree) * coefficient)
    return JetResult(2, "taylor", derivatives, time.perf_counter() - started, counts)


def depth2_derivative(max_order: int) -> JetResult:
    started = time.perf_counter()
    dimension = max_order + 2
    bottom = LinearGaussianLaw(dimension, unit_base=True)
    top = LinearGaussianLaw(dimension, unit_base=True)
    u = variable(0, dimension)
    a = variable(0, dimension)

    A: list[Vector] = []
    X: list[Vector] = []
    Z: list[Vector] = []
    R: list[Vector] = []
    counts: list[dict[str, int]] = []

    for degree in range(max_order + 1):
        if degree == 0:
            A.append(a)
            X.append(u)
        else:
            A.append(Z[degree - 1])
            X.append(R[degree - 1])

        eta_index = degree + 1
        for other in range(degree + 1):
            top.set_covariance(
                eta_index, other + 1, bottom.inner(X[degree], X[other])
            )
        z_terms: list[tuple[Fraction, Vector]] = [(Q(1), variable(eta_index, dimension))]
        for other in range(degree):
            response = X[degree][other + 1]
            if response:
                z_terms.append((response, A[other]))
        for a_degree in range(degree):
            for x_left in range(degree - a_degree):
                x_right = degree - 1 - a_degree - x_left
                weight = math.comb(degree, x_right) * math.comb(
                    a_degree + x_left, a_degree
                )
                overlap = bottom.inner(X[x_left], X[x_right])
                z_terms.append((Q(weight) * overlap, A[a_degree]))
        Z.append(combine(dimension, z_terms))

        xi_index = degree + 1
        for other in range(degree + 1):
            bottom.set_covariance(
                xi_index, other + 1, top.inner(A[degree], A[other])
            )
        r_terms: list[tuple[Fraction, Vector]] = [(Q(1), variable(xi_index, dimension))]
        for other in range(degree + 1):
            response = A[degree][other + 1]
            if response:
                r_terms.append((response, X[other]))
        for x_degree in range(degree):
            for a_left in range(degree - x_degree):
                a_right = degree - 1 - x_degree - a_left
                weight = math.comb(degree, a_right) * math.comb(
                    x_degree + a_left, x_degree
                )
                overlap = top.inner(A[a_left], A[a_right])
                r_terms.append((Q(weight) * overlap, X[x_degree]))
        R.append(combine(dimension, r_terms))
        counts.append(_support(A=A[-1], X=X[-1], Z=Z[-1], R=R[-1]))

    derivatives = []
    for degree in range(max_order + 1):
        value = sum(
            (
                Q(math.comb(degree, left))
                * top.inner(A[left], Z[degree - left])
                for left in range(degree + 1)
            ),
            Q(0),
        )
        derivatives.append(value)
    return JetResult(2, "derivative", derivatives, time.perf_counter() - started, counts)


def depth3_taylor(max_order: int) -> JetResult:
    started = time.perf_counter()
    bottom_dimension = max_order + 2
    middle_dimension = 2 * (max_order + 1)
    top_dimension = max_order + 2
    split = max_order + 1
    bottom = LinearGaussianLaw(bottom_dimension, unit_base=True)
    middle = LinearGaussianLaw(middle_dimension)
    top = LinearGaussianLaw(top_dimension, unit_base=True)
    u = variable(0, bottom_dimension)
    a = variable(0, top_dimension)

    A: list[Vector] = []
    X: list[Vector] = []
    Z: list[Vector] = []
    T: list[Vector] = []
    R2: list[Vector] = []
    R1: list[Vector] = []
    counts: list[dict[str, int]] = []

    for degree in range(max_order + 1):
        if degree == 0:
            A.append(a)
            X.append(u)
        else:
            A.append(scale(T[degree - 1], Q(1, degree)))
            X.append(scale(R1[degree - 1], Q(1, degree)))

        for other in range(degree + 1):
            middle.set_covariance(
                degree, other, bottom.inner(X[degree], X[other])
            )
        z_terms: list[tuple[Fraction, Vector]] = [
            (Q(1), variable(degree, middle_dimension))
        ]
        for other in range(degree):
            response = X[degree][other + 1]
            if response:
                z_terms.append((response, R2[other]))
        for r_degree in range(degree):
            for x_left in range(degree - r_degree):
                x_right = degree - 1 - r_degree - x_left
                overlap = bottom.inner(X[x_left], X[x_right])
                z_terms.append((Q(overlap, r_degree + x_left + 1), R2[r_degree]))
        Z.append(combine(middle_dimension, z_terms))

        eta_v_index = degree + 1
        for other in range(degree + 1):
            top.set_covariance(
                eta_v_index, other + 1, middle.inner(Z[degree], Z[other])
            )
        t_terms: list[tuple[Fraction, Vector]] = [
            (Q(1), variable(eta_v_index, top_dimension))
        ]
        for other in range(degree):
            response = Z[degree][split + other]
            if response:
                t_terms.append((response, A[other]))
        for a_degree in range(degree):
            for z_left in range(degree - a_degree):
                z_right = degree - 1 - a_degree - z_left
                overlap = middle.inner(Z[z_left], Z[z_right])
                t_terms.append((Q(overlap, a_degree + z_left + 1), A[a_degree]))
        T.append(combine(top_dimension, t_terms))

        xi_v_index = split + degree
        for other in range(degree + 1):
            middle.set_covariance(
                xi_v_index, split + other, top.inner(A[degree], A[other])
            )
        r2_terms: list[tuple[Fraction, Vector]] = [
            (Q(1), variable(xi_v_index, middle_dimension))
        ]
        for other in range(degree + 1):
            response = A[degree][other + 1]
            if response:
                r2_terms.append((response, Z[other]))
        for z_degree in range(degree):
            for a_left in range(degree - z_degree):
                a_right = degree - 1 - z_degree - a_left
                overlap = top.inner(A[a_left], A[a_right])
                r2_terms.append((Q(overlap, z_degree + a_left + 1), Z[z_degree]))
        R2.append(combine(middle_dimension, r2_terms))

        xi_w_index = degree + 1
        for other in range(degree + 1):
            bottom.set_covariance(
                xi_w_index, other + 1, middle.inner(R2[degree], R2[other])
            )
        r1_terms: list[tuple[Fraction, Vector]] = [
            (Q(1), variable(xi_w_index, bottom_dimension))
        ]
        for other in range(degree + 1):
            response = R2[degree][other]
            if response:
                r1_terms.append((response, X[other]))
        for x_degree in range(degree):
            for r_left in range(degree - x_degree):
                r_right = degree - 1 - x_degree - r_left
                overlap = middle.inner(R2[r_left], R2[r_right])
                r1_terms.append((Q(overlap, x_degree + r_left + 1), X[x_degree]))
        R1.append(combine(bottom_dimension, r1_terms))
        counts.append(_support(A=A[-1], X=X[-1], Z=Z[-1], T=T[-1], R2=R2[-1], R1=R1[-1]))

    derivatives = []
    for degree in range(max_order + 1):
        coefficient = sum(
            (top.inner(A[left], T[degree - left]) for left in range(degree + 1)),
            Q(0),
        )
        derivatives.append(math.factorial(degree) * coefficient)
    return JetResult(3, "taylor", derivatives, time.perf_counter() - started, counts)


def depth3_derivative(max_order: int) -> JetResult:
    started = time.perf_counter()
    bottom_dimension = max_order + 2
    middle_dimension = 2 * (max_order + 1)
    top_dimension = max_order + 2
    split = max_order + 1
    bottom = LinearGaussianLaw(bottom_dimension, unit_base=True)
    middle = LinearGaussianLaw(middle_dimension)
    top = LinearGaussianLaw(top_dimension, unit_base=True)
    u = variable(0, bottom_dimension)
    a = variable(0, top_dimension)

    A: list[Vector] = []
    X: list[Vector] = []
    Z: list[Vector] = []
    T: list[Vector] = []
    R2: list[Vector] = []
    R1: list[Vector] = []
    counts: list[dict[str, int]] = []

    for degree in range(max_order + 1):
        if degree == 0:
            A.append(a)
            X.append(u)
        else:
            A.append(T[degree - 1])
            X.append(R1[degree - 1])

        for other in range(degree + 1):
            middle.set_covariance(
                degree, other, bottom.inner(X[degree], X[other])
            )
        z_terms: list[tuple[Fraction, Vector]] = [
            (Q(1), variable(degree, middle_dimension))
        ]
        for other in range(degree):
            response = X[degree][other + 1]
            if response:
                z_terms.append((response, R2[other]))
        for r_degree in range(degree):
            for x_left in range(degree - r_degree):
                x_right = degree - 1 - r_degree - x_left
                weight = math.comb(degree, x_right) * math.comb(
                    r_degree + x_left, r_degree
                )
                overlap = bottom.inner(X[x_left], X[x_right])
                z_terms.append((Q(weight) * overlap, R2[r_degree]))
        Z.append(combine(middle_dimension, z_terms))

        eta_v_index = degree + 1
        for other in range(degree + 1):
            top.set_covariance(
                eta_v_index, other + 1, middle.inner(Z[degree], Z[other])
            )
        t_terms: list[tuple[Fraction, Vector]] = [
            (Q(1), variable(eta_v_index, top_dimension))
        ]
        for other in range(degree):
            response = Z[degree][split + other]
            if response:
                t_terms.append((response, A[other]))
        for a_degree in range(degree):
            for z_left in range(degree - a_degree):
                z_right = degree - 1 - a_degree - z_left
                weight = math.comb(degree, z_right) * math.comb(
                    a_degree + z_left, a_degree
                )
                overlap = middle.inner(Z[z_left], Z[z_right])
                t_terms.append((Q(weight) * overlap, A[a_degree]))
        T.append(combine(top_dimension, t_terms))

        xi_v_index = split + degree
        for other in range(degree + 1):
            middle.set_covariance(
                xi_v_index, split + other, top.inner(A[degree], A[other])
            )
        r2_terms: list[tuple[Fraction, Vector]] = [
            (Q(1), variable(xi_v_index, middle_dimension))
        ]
        for other in range(degree + 1):
            response = A[degree][other + 1]
            if response:
                r2_terms.append((response, Z[other]))
        for z_degree in range(degree):
            for a_left in range(degree - z_degree):
                a_right = degree - 1 - z_degree - a_left
                weight = math.comb(degree, a_right) * math.comb(
                    z_degree + a_left, z_degree
                )
                overlap = top.inner(A[a_left], A[a_right])
                r2_terms.append((Q(weight) * overlap, Z[z_degree]))
        R2.append(combine(middle_dimension, r2_terms))

        xi_w_index = degree + 1
        for other in range(degree + 1):
            bottom.set_covariance(
                xi_w_index, other + 1, middle.inner(R2[degree], R2[other])
            )
        r1_terms: list[tuple[Fraction, Vector]] = [
            (Q(1), variable(xi_w_index, bottom_dimension))
        ]
        for other in range(degree + 1):
            response = R2[degree][other]
            if response:
                r1_terms.append((response, X[other]))
        for x_degree in range(degree):
            for r_left in range(degree - x_degree):
                r_right = degree - 1 - x_degree - r_left
                weight = math.comb(degree, r_right) * math.comb(
                    x_degree + r_left, x_degree
                )
                overlap = middle.inner(R2[r_left], R2[r_right])
                r1_terms.append((Q(weight) * overlap, X[x_degree]))
        R1.append(combine(bottom_dimension, r1_terms))
        counts.append(_support(A=A[-1], X=X[-1], Z=Z[-1], T=T[-1], R2=R2[-1], R1=R1[-1]))

    derivatives = []
    for degree in range(max_order + 1):
        value = sum(
            (
                Q(math.comb(degree, left))
                * top.inner(A[left], T[degree - left])
                for left in range(degree + 1)
            ),
            Q(0),
        )
        derivatives.append(value)
    return JetResult(3, "derivative", derivatives, time.perf_counter() - started, counts)


def _serial(value: Fraction) -> int | str:
    return value.numerator if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def _payload(result: JetResult) -> dict[str, object]:
    return {
        "depth": result.depth,
        "route": result.route,
        "derivatives": [_serial(value) for value in result.derivatives],
        "elapsed_seconds": result.elapsed_seconds,
        "support_counts": result.support_counts,
    }


def validate(results: list[JetResult], max_order: int) -> dict[str, object]:
    controls = {
        2: {1: 3, 3: 48, 5: 1464},
        3: {1: 4, 3: 160, 5: 13888},
    }
    for result in results:
        for order, expected in controls[result.depth].items():
            if order <= max_order and result.derivatives[order] != expected:
                raise AssertionError(
                    f"depth {result.depth} {result.route} control F^{order}: "
                    f"got {result.derivatives[order]}, expected {expected}"
                )
        for order in range(0, max_order + 1, 2):
            if result.derivatives[order] != 0:
                raise AssertionError(
                    f"depth {result.depth} {result.route} parity F^{order}: "
                    f"got {result.derivatives[order]}"
                )
        if any(value.denominator != 1 for value in result.derivatives):
            raise AssertionError(
                f"depth {result.depth} {result.route} produced noninteger output"
            )

    for depth in (2, 3):
        matching = [result for result in results if result.depth == depth]
        if len(matching) == 2 and matching[0].derivatives != matching[1].derivatives:
            raise AssertionError(f"depth {depth} coefficient assemblers disagree")

    representative = {result.depth: result for result in results}
    retrospective = None
    if max_order >= 7 and 2 in representative:
        retrospective = representative[2].derivatives[7] == 76800
    return {
        "status": "passed",
        "frozen_controls": "passed",
        "parity": "passed",
        "integer_output": "passed",
        "two_route_agreement": (
            "passed" if all(len([r for r in results if r.depth == d]) == 2 for d in (2, 3))
            else "not_run_for_every_depth"
        ),
        "retrospective_depth2_F7_equals_76800": retrospective,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-order", type=int, default=11)
    parser.add_argument("--depth", choices=("2", "3", "both"), default="both")
    parser.add_argument("--route", choices=("taylor", "derivative", "both"), default="both")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.max_order < 0:
        raise ValueError("max-order must be nonnegative")

    depths = (2, 3) if args.depth == "both" else (int(args.depth),)
    routes = ("taylor", "derivative") if args.route == "both" else (args.route,)
    dispatch = {
        (2, "taylor"): depth2_taylor,
        (2, "derivative"): depth2_derivative,
        (3, "taylor"): depth3_taylor,
        (3, "derivative"): depth3_derivative,
    }
    results = [dispatch[(depth, route)](args.max_order) for depth in depths for route in routes]
    validation = validate(results, args.max_order)
    payload = {
        "model": "identity-equal-width-one-input-feature-ascent",
        "max_order": args.max_order,
        "validation": validation,
        "results": [_payload(result) for result in results],
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        for result in results:
            values = ", ".join(
                f"F^{order}={_serial(value)}"
                for order, value in enumerate(result.derivatives)
            )
            print(f"H={result.depth} {result.route}: {values}")
            print(f"elapsed={result.elapsed_seconds:.6f}s")
        print("validation: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
