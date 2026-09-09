#!/usr/bin/env python3
"""Exact width-limit jet for ``D_a + alpha D_u + D_W`` through order 13.

This is an implementation of the Gaussian tensor-program recurrence proved in
``POSITIVE_ALPHA_JET_DERIVATION.md``.  It does not enumerate derivative
forests.  Every scalar operation uses :class:`fractions.Fraction`; Gaussian
expectations use Wick's recurrence with exact covariance entries.

The stored coefficient vectors are in ascending powers of ``alpha``.  The
``--full`` gate independently evaluates the recurrence at alpha=0,...,13 and
recovers every vector by exact Newton interpolation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from multiprocessing import Pool
from pathlib import Path
from typing import Iterable


Q = Fraction
Monomial = tuple[int, ...]
Polynomial = dict[Monomial, Fraction]

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
CAMPAIGN4_RESULTS = (
    REPO
    / "studies/mean_field_peeling/quadratic_compiler/campaign4/results_order9.json"
)
CAMPAIGN4_RESULTS_SHA256 = (
    "530ef0818f4142eb162c28fa6b388d69a1e13eeb9de399d54a25008d591f6d5e"
)


# Coefficients of F_alpha^(k)(0), in ascending powers of alpha.
EXACT_JETS: dict[int, tuple[int, ...]] = {
    0: (),
    1: (63, 48),
    2: (),
    3: (77760, 625536, 754560, 227328),
    4: (),
    5: (
        274547232,
        4596735744,
        21436337664,
        31088738304,
        17024090112,
        2980184064,
    ),
    6: (),
    7: (
        2141006515200,
        51717526548480,
        443633644707840,
        1617194490200064,
        2564438160015360,
        1911736087216128,
        647577990070272,
        77429527805952,
    ),
    8: (),
    9: (
        31149221916487680,
        926397280733921280,
        11228797008295759872,
        68120013107843407872,
        216157343459495804928,
        360293373996617170944,
        325383748411160788992,
        157873329654523232256,
        37777979806259871744,
        3369009878554116096,
    ),
    10: (),
    11: (
        759035131220036321280,
        25594965804374979379200,
        383019483677094369755136,
        3183862200286963804176384,
        15561308094860120107253760,
        45191839708552427406360576,
        77732833310661790408900608,
        80037321953103213886439424,
        49156411552814847636799488,
        17330750388205451118379008,
        3157236628947852268142592,
        221895065540516313563136,
    ),
    12: (),
    13: (
        28719223368439752070594560,
        1049927070983648807603404800,
        17931688202114583797612298240,
        182535682557908834998152560640,
        1185389301689487145264541073408,
        4995568087297667723007295488000,
        13644399097739494223476842037248,
        23988792318732344423548176039936,
        27175238485927648131807568723968,
        19766556153143784452713000992768,
        9044046194292861476093351165952,
        2471574150367421186553069699072,
        359712824603649166641664622592,
        20689648397930917159577321472,
    ),
}


def zero_monomial(dimension: int) -> Monomial:
    return (0,) * dimension


def variable(index: int, dimension: int) -> Polynomial:
    powers = [0] * dimension
    powers[index] = 1
    return {tuple(powers): Q(1)}


def add_polynomials(*polynomials: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for polynomial in polynomials:
        for monomial, coefficient in polynomial.items():
            result[monomial] = result.get(monomial, Q(0)) + coefficient
    return {key: value for key, value in result.items() if value}


def scale_polynomial(polynomial: Polynomial, scalar: Fraction) -> Polynomial:
    if not scalar:
        return {}
    return {
        monomial: coefficient * scalar
        for monomial, coefficient in polynomial.items()
        if coefficient * scalar
    }


def multiply_polynomials(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(
                left_power + right_power
                for left_power, right_power in zip(left_monomial, right_monomial)
            )
            result[monomial] = (
                result.get(monomial, Q(0))
                + left_coefficient * right_coefficient
            )
    return {key: value for key, value in result.items() if value}


def differentiate_polynomial(polynomial: Polynomial, index: int) -> Polynomial:
    result: Polynomial = {}
    for monomial, coefficient in polynomial.items():
        power = monomial[index]
        if not power:
            continue
        child = list(monomial)
        child[index] -= 1
        child_monomial = tuple(child)
        result[child_monomial] = (
            result.get(child_monomial, Q(0)) + power * coefficient
        )
    return result


class GaussianExpectation:
    """Exact polynomial expectation for a growing centered Gaussian family.

    Variable zero is the independent base Gaussian (``a`` or ``u``).
    Variable ``r+1`` is the named Gaussian ``eta_r`` or ``xi_r``.  Covariance
    entries are installed before a polynomial containing the new variable is
    evaluated, so cached Wick moments never depend on an unfinished row.
    """

    def __init__(self, dimension: int) -> None:
        self.dimension = dimension
        self.covariance = [
            [Q(0) for _ in range(dimension)] for _ in range(dimension)
        ]
        self.covariance[0][0] = Q(1)
        self.cache: dict[Monomial, Fraction] = {
            zero_monomial(dimension): Q(1)
        }

    def set_covariance(self, left: int, right: int, value: Fraction) -> None:
        self.covariance[left][right] = value
        self.covariance[right][left] = value

    def monomial_moment(self, powers: Monomial) -> Fraction:
        cached = self.cache.get(powers)
        if cached is not None:
            return cached
        if sum(powers) % 2:
            return Q(0)
        left = next(index for index, power in enumerate(powers) if power)
        remainder = list(powers)
        remainder[left] -= 1
        value = Q(0)
        for right, multiplicity in enumerate(remainder):
            covariance = self.covariance[left][right]
            if not multiplicity or not covariance:
                continue
            remainder[right] -= 1
            value += (
                multiplicity
                * covariance
                * self.monomial_moment(tuple(remainder))
            )
            remainder[right] += 1
        self.cache[powers] = value
        return value

    def __call__(self, polynomial: Polynomial) -> Fraction:
        return sum(
            coefficient * self.monomial_moment(monomial)
            for monomial, coefficient in polynomial.items()
        )


def convolution(
    left: list[Polynomial], right: list[Polynomial], degree: int
) -> Polynomial:
    return add_polynomials(
        *(
            multiply_polynomials(left[index], right[degree - index])
            for index in range(degree + 1)
        )
    )


def feature_derivatives(alpha: Fraction, max_order: int = 13) -> list[Fraction]:
    """Evaluate the exact tensor-program recurrence at one rational alpha."""

    if max_order < 0:
        raise ValueError("max_order must be nonnegative")
    dimension = max_order + 2
    row_expectation = GaussianExpectation(dimension)
    column_expectation = GaussianExpectation(dimension)
    a = variable(0, dimension)
    u = variable(0, dimension)

    A: list[Polynomial] = []
    X: list[Polynomial] = []
    Y: list[Polynomial] = []
    Z: list[Polynomial] = []
    B: list[Polynomial] = []
    Q_series: list[Polynomial] = []
    R: list[Polynomial] = []

    def forward(degree: int) -> Polynomial:
        # eta_degree has covariance E_C[X_degree X_j].
        for index in range(degree + 1):
            row_expectation.set_covariance(
                degree + 1,
                index + 1,
                column_expectation(
                    multiply_polynomials(X[degree], X[index])
                ),
            )
        result = variable(degree + 1, dimension)
        # Detransposition response to prior W_0^T B_j multiplications.
        for index in range(degree):
            response = column_expectation(
                differentiate_polynomial(X[degree], index + 1)
            )
            if response:
                result = add_polynomials(
                    result, scale_polynomial(B[index], response)
                )
        return result

    def backward(degree: int) -> Polynomial:
        # xi_degree has covariance E_R[B_degree B_j].
        for index in range(degree + 1):
            column_expectation.set_covariance(
                degree + 1,
                index + 1,
                row_expectation(
                    multiply_polynomials(B[degree], B[index])
                ),
            )
        result = variable(degree + 1, dimension)
        # Detransposition response to all W_0 X_j multiplications so far.
        for index in range(degree + 1):
            response = row_expectation(
                differentiate_polynomial(B[degree], index + 1)
            )
            if response:
                result = add_polynomials(
                    result, scale_polynomial(X[index], response)
                )
        return result

    for degree in range(max_order + 1):
        if degree == 0:
            A.append(a)
            X.append(multiply_polynomials(u, u))
        else:
            A.append(
                scale_polynomial(
                    add_polynomials(
                        *(
                            multiply_polynomials(Z[left], Z[degree - 1 - left])
                            for left in range(degree)
                        )
                    ),
                    Q(1, degree),
                )
            )
            X.append(
                scale_polynomial(
                    add_polynomials(
                        *(
                            multiply_polynomials(X[left], R[degree - 1 - left])
                            for left in range(degree)
                        )
                    ),
                    Q(8, degree) * alpha,
                )
            )

        Y.append(forward(degree))

        z_memory: list[Polynomial] = []
        for b_degree in range(degree):
            for x_left_degree in range(degree - b_degree):
                x_right_degree = degree - 1 - b_degree - x_left_degree
                overlap = column_expectation(
                    multiply_polynomials(
                        X[x_left_degree], X[x_right_degree]
                    )
                )
                z_memory.append(
                    scale_polynomial(
                        B[b_degree],
                        Q(2, b_degree + x_left_degree + 1) * overlap,
                    )
                )
        Z.append(add_polynomials(Y[degree], *z_memory))
        B.append(convolution(A, Z, degree))
        Q_series.append(backward(degree))

        r_memory: list[Polynomial] = []
        for x_degree in range(degree):
            for b_left_degree in range(degree - x_degree):
                b_right_degree = degree - 1 - x_degree - b_left_degree
                overlap = row_expectation(
                    multiply_polynomials(
                        B[b_left_degree], B[b_right_degree]
                    )
                )
                r_memory.append(
                    scale_polynomial(
                        X[x_degree],
                        Q(2, x_degree + b_left_degree + 1) * overlap,
                    )
                )
        R.append(add_polynomials(Q_series[degree], *r_memory))

    derivatives: list[Fraction] = []
    for degree in range(max_order + 1):
        coefficient = add_polynomials(
            *(
                multiply_polynomials(
                    A[a_degree],
                    multiply_polynomials(
                        Z[z_left_degree],
                        Z[degree - a_degree - z_left_degree],
                    ),
                )
                for a_degree in range(degree + 1)
                for z_left_degree in range(degree - a_degree + 1)
            )
        )
        derivatives.append(
            math.factorial(degree) * row_expectation(coefficient)
        )
    return derivatives


def evaluate_coefficients(coefficients: Iterable[int], alpha: int) -> int:
    return sum(value * alpha**power for power, value in enumerate(coefficients))


def interpolate_at_nonnegative_integers(values: list[Fraction]) -> tuple[int, ...]:
    """Return power-basis coefficients using exact Newton differences."""

    differences = values[:]
    leading_differences: list[Fraction] = []
    while differences:
        leading_differences.append(differences[0])
        differences = [
            differences[index + 1] - differences[index]
            for index in range(len(differences) - 1)
        ]

    result = [Q(0) for _ in values]
    falling_factorial = [Q(1)]
    factorial = 1
    for degree, difference in enumerate(leading_differences):
        if degree:
            factorial *= degree
        for power, coefficient in enumerate(falling_factorial):
            result[power] += difference * coefficient / factorial
        following = [Q(0) for _ in range(len(falling_factorial) + 1)]
        for power, coefficient in enumerate(falling_factorial):
            following[power] -= degree * coefficient
            following[power + 1] += coefficient
        falling_factorial = following

    while result and not result[-1]:
        result.pop()
    if any(value.denominator != 1 for value in result):
        raise ArithmeticError("interpolated jet has a nonintegral coefficient")
    return tuple(value.numerator for value in result)


def _node_worker(alpha: int) -> tuple[int, list[Fraction]]:
    return alpha, feature_derivatives(Q(alpha), 13)


def regenerate_full_jet(workers: int = 1) -> dict[int, tuple[int, ...]]:
    """Regenerate the complete order-13 polynomial from fourteen exact nodes."""

    nodes = list(range(14))
    if workers == 1:
        evaluations = dict(_node_worker(node) for node in nodes)
    else:
        with Pool(processes=workers) as pool:
            evaluations = dict(pool.map(_node_worker, nodes))
    result: dict[int, tuple[int, ...]] = {}
    for order in range(14):
        coefficients = interpolate_at_nonnegative_integers(
            [evaluations[node][order] for node in nodes]
        )
        if len(coefficients) > order + 1:
            raise AssertionError("metric-degree bound failed")
        for node in nodes:
            if evaluate_coefficients(coefficients, node) != evaluations[node][order]:
                raise AssertionError("interpolation replay failed")
        result[order] = coefficients
    return result


def campaign4_beta_one_jets() -> dict[int, tuple[int, ...]]:
    digest = hashlib.sha256(CAMPAIGN4_RESULTS.read_bytes()).hexdigest()
    if digest != CAMPAIGN4_RESULTS_SHA256:
        raise AssertionError(f"Campaign-4 source hash mismatch: {digest}")
    document = json.loads(CAMPAIGN4_RESULTS.read_text())
    output: dict[int, tuple[int, ...]] = {}
    for jet in document["jets"]:
        order = int(jet["order"])
        coefficients = [0 for _ in range(order + 1)]
        for term in jet["monomials"]:
            # beta=1: sum all beta powers at each alpha power.
            coefficients[int(term["alpha_power"])] += int(term["value"])
        while coefficients and not coefficients[-1]:
            coefficients.pop()
        output[order] = tuple(coefficients)
    return output


def verify_quick_gates() -> dict[str, object]:
    campaign4 = campaign4_beta_one_jets()
    for order in range(10):
        if campaign4[order] != EXACT_JETS[order]:
            raise AssertionError(f"Campaign-4 mismatch at order {order}")

    axis = feature_derivatives(Q(0), 13)
    if any(
        value != evaluate_coefficients(EXACT_JETS[order], 0)
        for order, value in enumerate(axis)
    ):
        raise AssertionError("alpha=0 recurrence gate failed")

    canonical = feature_derivatives(Q(1), 11)
    if any(
        value != evaluate_coefficients(EXACT_JETS[order], 1)
        for order, value in enumerate(canonical)
    ):
        raise AssertionError("alpha=1 recurrence gate failed")
    if canonical[11] != Q(291982832387585872335470592):
        raise AssertionError("accepted canonical F11 gate failed")
    if any(EXACT_JETS[order] for order in range(0, 14, 2)):
        raise AssertionError("parity gate failed")
    if any(len(EXACT_JETS[order]) > order + 1 for order in range(14)):
        raise AssertionError("metric-degree gate failed")

    return {
        "campaign4_beta_one_through_order9": True,
        "campaign4_results_sha256": CAMPAIGN4_RESULTS_SHA256,
        "alpha_zero_through_order13": True,
        "alpha_one_through_order11": True,
        "accepted_canonical_F11": str(canonical[11]),
        "parity": True,
        "degree_bound": True,
    }


def certificate(full_regeneration: bool = False, workers: int = 1) -> dict[str, object]:
    gates = verify_quick_gates()
    if full_regeneration:
        regenerated = regenerate_full_jet(workers)
        if regenerated != EXACT_JETS:
            raise AssertionError("full order-13 regeneration mismatch")
        gates["full_fourteen_node_regeneration"] = True
        gates["full_regeneration_workers"] = workers
    return {
        "schema": "block_metric_positive_alpha_jet_v1",
        "metric": "D_a + alpha D_u + D_W",
        "domain": "formal alpha; theorem uses alpha >= 0",
        "max_order": 13,
        "coefficient_order": "ascending powers of alpha",
        "feature_derivative_polynomials": {
            str(order): [str(value) for value in EXACT_JETS[order]]
            for order in range(14)
        },
        "canonical_F13_at_alpha_one": str(
            evaluate_coefficients(EXACT_JETS[13], 1)
        ),
        "gates": gates,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--full",
        action="store_true",
        help="regenerate all polynomials at fourteen exact interpolation nodes",
    )
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args()
    if args.workers < 1:
        raise SystemExit("--workers must be positive")
    print(
        json.dumps(
            certificate(full_regeneration=args.full, workers=args.workers),
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
