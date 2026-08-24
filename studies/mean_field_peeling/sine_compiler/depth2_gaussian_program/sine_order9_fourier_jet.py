#!/usr/bin/env python3
"""Finite Fourier--Gaussian depth-2 sine jet through order nine.

This implements the two coefficient routes frozen in ``ORDER9_PROTOCOL.md``:

* ``taylor_jet`` stores ordinary Taylor coefficients;
* ``derivative_jet`` stores actual derivatives at zero.

The routes share only sparse Fourier-polynomial arithmetic and the exact
tilted-Wick expectation primitive.  In particular, the Volterra and product
weights are assembled separately in the two routes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, Sequence

import mpmath as mp


HERE = Path(__file__).resolve().parent
PROTOCOL = HERE / "ORDER9_PROTOCOL.md"
EXPECTED_PROTOCOL_SHA256 = (
    "366ae94d52a4b4aa7d741f807f4afe4e05a4a014e2f408837c4301ff0402bb37"
)

Powers = tuple[int, ...]
Term = tuple[Powers, int]
FourierPolynomial = dict[Term, mp.mpc]
Progress = Callable[[str], None]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _zero_powers(dimension: int) -> Powers:
    return (0,) * dimension


class SparseFourierAlgebra:
    """Sparse sums of ``c * G**alpha * exp(i*m*G_star)``."""

    def __init__(self, dimension: int, dps: int) -> None:
        self.dimension = dimension
        self.dps = dps
        self.drop_relative = mp.power(10, -dps + 20)

    def constant(self, value: object) -> FourierPolynomial:
        coefficient = mp.mpc(value)
        if coefficient == 0:
            return {}
        return {(_zero_powers(self.dimension), 0): coefficient}

    def variable(self, index: int) -> FourierPolynomial:
        powers = [0] * self.dimension
        powers[index] = 1
        return {(tuple(powers), 0): mp.mpc(1)}

    def sine(self, distinguished: int, scale: mp.mpf) -> FourierPolynomial:
        del distinguished  # The distinguished coordinate is implicit in m.
        zero = _zero_powers(self.dimension)
        return {
            (zero, 1): -mp.j * scale / 2,
            (zero, -1): mp.j * scale / 2,
        }

    def cosine(self, distinguished: int, scale: mp.mpf) -> FourierPolynomial:
        del distinguished
        zero = _zero_powers(self.dimension)
        return {
            (zero, 1): mp.mpc(scale / 2),
            (zero, -1): mp.mpc(scale / 2),
        }

    def clean(self, polynomial: FourierPolynomial) -> FourierPolynomial:
        if not polynomial:
            return {}
        largest = max(abs(value) for value in polynomial.values())
        if largest == 0:
            return {}
        cutoff = self.drop_relative * max(mp.mpf(1), largest)
        return {
            term: value
            for term, value in polynomial.items()
            if abs(value) > cutoff
        }

    def add(self, *polynomials: FourierPolynomial) -> FourierPolynomial:
        result: FourierPolynomial = {}
        for polynomial in polynomials:
            for term, coefficient in polynomial.items():
                result[term] = result.get(term, mp.mpc(0)) + coefficient
        return self.clean(result)

    def scale(
        self, polynomial: FourierPolynomial, scalar: object
    ) -> FourierPolynomial:
        scalar_mp = mp.mpc(scalar)
        if scalar_mp == 0 or not polynomial:
            return {}
        if scalar_mp == 1:
            return polynomial.copy()
        return self.clean({
            term: scalar_mp * coefficient
            for term, coefficient in polynomial.items()
        })

    def multiply(
        self, left: FourierPolynomial, right: FourierPolynomial
    ) -> FourierPolynomial:
        if not left or not right:
            return {}
        result: FourierPolynomial = {}
        for (left_powers, left_frequency), left_coefficient in left.items():
            for (
                right_powers,
                right_frequency,
            ), right_coefficient in right.items():
                powers = tuple(
                    left_power + right_power
                    for left_power, right_power in zip(
                        left_powers, right_powers
                    )
                )
                term = (powers, left_frequency + right_frequency)
                result[term] = (
                    result.get(term, mp.mpc(0))
                    + left_coefficient * right_coefficient
                )
        return self.clean(result)

    def product(self, *polynomials: FourierPolynomial) -> FourierPolynomial:
        if not polynomials:
            return self.constant(1)
        result = polynomials[0]
        for polynomial in polynomials[1:]:
            result = self.multiply(result, polynomial)
            if not result:
                break
        return result


class TiltedGaussianExpectation:
    """Chronological Gaussian expectation with one Fourier coordinate."""

    def __init__(
        self,
        algebra: SparseFourierAlgebra,
        distinguished: int,
        *,
        unit_base_index: int | None = None,
    ) -> None:
        self.algebra = algebra
        self.dimension = algebra.dimension
        self.distinguished = distinguished
        self.dps = algebra.dps
        self.covariance = [
            [mp.mpf(0) for _ in range(self.dimension)]
            for _ in range(self.dimension)
        ]
        if unit_base_index is not None:
            self.covariance[unit_base_index][unit_base_index] = mp.mpf(1)
        self.cache: dict[Term, mp.mpc] = {}

    def set_covariance(self, left: int, right: int, value: object) -> None:
        value_mp = self.real(value, label=f"covariance({left},{right})")
        current = self.covariance[left][right]
        tolerance = mp.power(10, -self.dps + 15) * max(
            mp.mpf(1), abs(current), abs(value_mp)
        )
        if current and abs(current - value_mp) > tolerance:
            raise ArithmeticError(
                f"attempted to change covariance ({left}, {right}) "
                f"from {current} to {value_mp}"
            )
        self.covariance[left][right] = value_mp
        self.covariance[right][left] = value_mp

    def tilted_moment(self, powers: Powers, frequency: int) -> mp.mpc:
        key = (powers, frequency)
        cached = self.cache.get(key)
        if cached is not None:
            return cached
        total_power = sum(powers)
        if total_power == 0:
            variance = self.covariance[
                self.distinguished
            ][self.distinguished]
            value = mp.exp(-mp.mpf(frequency * frequency) * variance / 2)
            answer = mp.mpc(value)
            self.cache[key] = answer
            return answer

        left = next(index for index, power in enumerate(powers) if power)
        remainder = list(powers)
        remainder[left] -= 1
        remainder_tuple = tuple(remainder)
        value = (
            mp.j
            * frequency
            * self.covariance[left][self.distinguished]
            * self.tilted_moment(remainder_tuple, frequency)
        )
        for right, multiplicity in enumerate(remainder):
            covariance = self.covariance[left][right]
            if not multiplicity or not covariance:
                continue
            remainder[right] -= 1
            value += (
                multiplicity
                * covariance
                * self.tilted_moment(tuple(remainder), frequency)
            )
            remainder[right] += 1
        self.cache[key] = value
        return value

    def __call__(self, polynomial: FourierPolynomial) -> mp.mpc:
        return mp.fsum(
            coefficient * self.tilted_moment(powers, frequency)
            for (powers, frequency), coefficient in polynomial.items()
        )

    def product_expectation(
        self, left: FourierPolynomial, right: FourierPolynomial
    ) -> mp.mpc:
        values: list[mp.mpc] = []
        for (left_powers, left_frequency), left_coefficient in left.items():
            for (
                right_powers,
                right_frequency,
            ), right_coefficient in right.items():
                powers = tuple(
                    left_power + right_power
                    for left_power, right_power in zip(
                        left_powers, right_powers
                    )
                )
                values.append(
                    left_coefficient
                    * right_coefficient
                    * self.tilted_moment(
                        powers, left_frequency + right_frequency
                    )
                )
        return mp.fsum(values)

    def derivative_expectation(
        self, polynomial: FourierPolynomial, index: int
    ) -> mp.mpc:
        values: list[mp.mpc] = []
        for (powers, frequency), coefficient in polynomial.items():
            power = powers[index]
            if power:
                child = list(powers)
                child[index] -= 1
                values.append(
                    power
                    * coefficient
                    * self.tilted_moment(tuple(child), frequency)
                )
            if index == self.distinguished and frequency:
                values.append(
                    mp.j
                    * frequency
                    * coefficient
                    * self.tilted_moment(powers, frequency)
                )
        return mp.fsum(values)

    def real(self, value: object, *, label: str) -> mp.mpf:
        value_mp = mp.mpc(value)
        tolerance = mp.power(10, -self.dps + 15) * max(
            mp.mpf(1), abs(value_mp)
        )
        if abs(mp.im(value_mp)) > tolerance:
            raise ArithmeticError(
                f"{label} retained imaginary part {mp.im(value_mp)}"
            )
        return mp.re(value_mp)


@dataclass
class JetResult:
    route: str
    activation: str
    scale: mp.mpf
    dps: int
    derivatives: list[mp.mpf]
    even_residuals: list[mp.mpf]
    elapsed_seconds: float
    term_counts: list[dict[str, int]]
    tilted_wick_cache_sizes: dict[str, int]


def _activation_scale(name: str) -> mp.mpf:
    if name == "raw":
        return mp.mpf(1)
    if name == "unit":
        return mp.sqrt(mp.mpf(2) / (1 - mp.exp(-2)))
    raise ValueError(f"unknown activation {name!r}")


def _state_sizes(
    degree: int,
    X: Sequence[FourierPolynomial],
    C: Sequence[FourierPolynomial],
    A: Sequence[FourierPolynomial],
    Z: Sequence[FourierPolynomial],
    G: Sequence[FourierPolynomial],
    E: Sequence[FourierPolynomial],
    B: Sequence[FourierPolynomial],
    R: Sequence[FourierPolynomial],
) -> dict[str, int]:
    return {
        "degree": degree,
        "X": len(X[degree]),
        "C": len(C[degree]),
        "A": len(A[degree]),
        "Z": len(Z[degree]),
        "G": len(G[degree]),
        "E": len(E[degree]),
        "B": len(B[degree]),
        "R": len(R[degree]),
    }


def _progress_line(
    route: str, activation: str, sizes: dict[str, int], elapsed: float
) -> str:
    state = " ".join(
        f"{name}={value}"
        for name, value in sizes.items()
        if name != "degree"
    )
    return (
        f"[{activation}/{route}] k={sizes['degree']} {state} "
        f"elapsed={elapsed:.3f}s"
    )


def _setup(
    max_order: int, dps: int, activation: str
) -> tuple[
    SparseFourierAlgebra,
    TiltedGaussianExpectation,
    TiltedGaussianExpectation,
    mp.mpf,
]:
    mp.mp.dps = dps
    dimension = max_order + 2
    algebra = SparseFourierAlgebra(dimension, dps)
    column = TiltedGaussianExpectation(
        algebra, distinguished=0, unit_base_index=0
    )
    row = TiltedGaussianExpectation(
        algebra, distinguished=1, unit_base_index=0
    )
    return algebra, column, row, _activation_scale(activation)


def taylor_jet(
    max_order: int = 9,
    *,
    dps: int = 100,
    activation: str = "raw",
    progress: Progress | None = None,
) -> JetResult:
    """Primary route using ordinary Taylor coefficients."""

    if max_order < 0:
        raise ValueError("max_order must be nonnegative")
    started = time.perf_counter()
    alg, column, row, scale = _setup(max_order, dps, activation)

    X: list[FourierPolynomial] = []
    C: list[FourierPolynomial] = []
    A: list[FourierPolynomial] = []
    Z: list[FourierPolynomial] = []
    G: list[FourierPolynomial] = []
    E: list[FourierPolynomial] = []
    B: list[FourierPolynomial] = []
    R: list[FourierPolynomial] = []
    counts: list[dict[str, int]] = []

    for degree in range(max_order + 1):
        if degree == 0:
            X.append(alg.sine(0, scale))
            C.append(alg.cosine(0, scale))
            A.append(alg.variable(0))
        else:
            x_terms: list[FourierPolynomial] = []
            c_terms: list[FourierPolynomial] = []
            target = degree - 1
            for left in range(target + 1):
                for middle in range(target - left + 1):
                    right = target - left - middle
                    x_terms.append(alg.product(C[left], C[middle], R[right]))
                    c_terms.append(alg.product(X[left], C[middle], R[right]))
            X.append(alg.scale(alg.add(*x_terms), mp.mpf(1) / degree))
            C.append(alg.scale(alg.add(*c_terms), -mp.mpf(1) / degree))
            A.append(alg.scale(G[degree - 1], mp.mpf(1) / degree))

        eta_index = degree + 1
        for other in range(degree + 1):
            covariance = column.real(
                column.product_expectation(X[degree], X[other]),
                label=f"E[X_{degree} X_{other}]",
            )
            row.set_covariance(eta_index, other + 1, covariance)

        forward = alg.variable(eta_index)
        for other in range(degree):
            response = column.real(
                column.derivative_expectation(X[degree], other + 1),
                label=f"E[d_xi_{other} X_{degree}]",
            )
            if response:
                forward = alg.add(forward, alg.scale(B[other], response))

        z_terms = [forward]
        for b_degree in range(degree):
            for x_left in range(degree - b_degree):
                x_right = degree - 1 - b_degree - x_left
                overlap = column.real(
                    column.product_expectation(X[x_left], X[x_right]),
                    label=f"E[X_{x_left} X_{x_right}]",
                )
                z_terms.append(alg.scale(
                    B[b_degree],
                    overlap / (b_degree + x_left + 1),
                ))
        Z.append(alg.add(*z_terms))

        if degree == 0:
            G.append(alg.sine(1, scale))
            E.append(alg.cosine(1, scale))
        else:
            g_terms: list[FourierPolynomial] = []
            e_terms: list[FourierPolynomial] = []
            for e_degree in range(degree):
                z_degree = degree - e_degree
                g_terms.append(alg.scale(
                    alg.multiply(E[e_degree], Z[z_degree]), z_degree
                ))
                e_terms.append(alg.scale(
                    alg.multiply(G[e_degree], Z[z_degree]), -z_degree
                ))
            G.append(alg.scale(alg.add(*g_terms), mp.mpf(1) / degree))
            E.append(alg.scale(alg.add(*e_terms), mp.mpf(1) / degree))

        B.append(alg.add(*(
            alg.multiply(A[left], E[degree - left])
            for left in range(degree + 1)
        )))

        xi_index = degree + 1
        for other in range(degree + 1):
            covariance = row.real(
                row.product_expectation(B[degree], B[other]),
                label=f"E[B_{degree} B_{other}]",
            )
            column.set_covariance(xi_index, other + 1, covariance)

        backward = alg.variable(xi_index)
        for other in range(degree + 1):
            response = row.real(
                row.derivative_expectation(B[degree], other + 1),
                label=f"E[d_eta_{other} B_{degree}]",
            )
            if response:
                backward = alg.add(
                    backward, alg.scale(X[other], response)
                )

        r_terms = [backward]
        for x_degree in range(degree):
            for b_left in range(degree - x_degree):
                b_right = degree - 1 - x_degree - b_left
                overlap = row.real(
                    row.product_expectation(B[b_left], B[b_right]),
                    label=f"E[B_{b_left} B_{b_right}]",
                )
                r_terms.append(alg.scale(
                    X[x_degree],
                    overlap / (x_degree + b_left + 1),
                ))
        R.append(alg.add(*r_terms))

        current_sizes = _state_sizes(
            degree, X, C, A, Z, G, E, B, R
        )
        counts.append(current_sizes)
        if progress:
            progress(_progress_line(
                "taylor", activation, current_sizes,
                time.perf_counter() - started,
            ))

    derivatives: list[mp.mpf] = []
    even_residuals: list[mp.mpf] = []
    for degree in range(max_order + 1):
        coefficient = row.real(
            mp.fsum(
                row.product_expectation(A[left], G[degree - left])
                for left in range(degree + 1)
            ),
            label=f"Taylor F coefficient {degree}",
        )
        derivative = math.factorial(degree) * coefficient
        derivatives.append(derivative)
        if degree % 2 == 0:
            even_residuals.append(abs(derivative))

    return JetResult(
        route="taylor",
        activation=activation,
        scale=scale,
        dps=dps,
        derivatives=derivatives,
        even_residuals=even_residuals,
        elapsed_seconds=time.perf_counter() - started,
        term_counts=counts,
        tilted_wick_cache_sizes={
            "column": len(column.cache),
            "row": len(row.cache),
        },
    )


def derivative_jet(
    max_order: int = 9,
    *,
    dps: int = 100,
    activation: str = "raw",
    progress: Progress | None = None,
) -> JetResult:
    """Independent route using derivative-normalized coefficients."""

    if max_order < 0:
        raise ValueError("max_order must be nonnegative")
    started = time.perf_counter()
    alg, column, row, scale = _setup(max_order, dps, activation)

    X: list[FourierPolynomial] = []
    C: list[FourierPolynomial] = []
    A: list[FourierPolynomial] = []
    Z: list[FourierPolynomial] = []
    G: list[FourierPolynomial] = []
    E: list[FourierPolynomial] = []
    B: list[FourierPolynomial] = []
    R: list[FourierPolynomial] = []
    counts: list[dict[str, int]] = []

    for degree in range(max_order + 1):
        if degree == 0:
            X.append(alg.sine(0, scale))
            C.append(alg.cosine(0, scale))
            A.append(alg.variable(0))
        else:
            target = degree - 1
            x_terms: list[FourierPolynomial] = []
            c_terms: list[FourierPolynomial] = []
            for left in range(target + 1):
                for middle in range(target - left + 1):
                    right = target - left - middle
                    weight = (
                        math.factorial(target)
                        // (
                            math.factorial(left)
                            * math.factorial(middle)
                            * math.factorial(right)
                        )
                    )
                    x_terms.append(alg.scale(
                        alg.product(C[left], C[middle], R[right]), weight
                    ))
                    c_terms.append(alg.scale(
                        alg.product(X[left], C[middle], R[right]), -weight
                    ))
            X.append(alg.add(*x_terms))
            C.append(alg.add(*c_terms))
            A.append(G[degree - 1].copy())

        eta_index = degree + 1
        for other in range(degree + 1):
            covariance = column.real(
                column.product_expectation(X[degree], X[other]),
                label=f"E[X^{degree} X^{other}]",
            )
            row.set_covariance(eta_index, other + 1, covariance)

        forward = alg.variable(eta_index)
        for other in range(degree):
            response = column.real(
                column.derivative_expectation(X[degree], other + 1),
                label=f"E[d_xi_{other} X^{degree}]",
            )
            if response:
                forward = alg.add(forward, alg.scale(B[other], response))

        z_terms = [forward]
        for b_degree in range(degree):
            for x_left in range(degree - b_degree):
                x_right = degree - 1 - b_degree - x_left
                weight = math.comb(degree, x_right) * math.comb(
                    b_degree + x_left, b_degree
                )
                overlap = column.real(
                    column.product_expectation(X[x_left], X[x_right]),
                    label=f"E[X^{x_left} X^{x_right}]",
                )
                z_terms.append(alg.scale(
                    B[b_degree], weight * overlap
                ))
        Z.append(alg.add(*z_terms))

        if degree == 0:
            G.append(alg.sine(1, scale))
            E.append(alg.cosine(1, scale))
        else:
            G.append(alg.add(*(
                alg.scale(
                    alg.multiply(E[left], Z[degree - left]),
                    math.comb(degree - 1, left),
                )
                for left in range(degree)
            )))
            E.append(alg.add(*(
                alg.scale(
                    alg.multiply(G[left], Z[degree - left]),
                    -math.comb(degree - 1, left),
                )
                for left in range(degree)
            )))

        B.append(alg.add(*(
            alg.scale(
                alg.multiply(A[left], E[degree - left]),
                math.comb(degree, left),
            )
            for left in range(degree + 1)
        )))

        xi_index = degree + 1
        for other in range(degree + 1):
            covariance = row.real(
                row.product_expectation(B[degree], B[other]),
                label=f"E[B^{degree} B^{other}]",
            )
            column.set_covariance(xi_index, other + 1, covariance)

        backward = alg.variable(xi_index)
        for other in range(degree + 1):
            response = row.real(
                row.derivative_expectation(B[degree], other + 1),
                label=f"E[d_eta_{other} B^{degree}]",
            )
            if response:
                backward = alg.add(
                    backward, alg.scale(X[other], response)
                )

        r_terms = [backward]
        for x_degree in range(degree):
            for b_left in range(degree - x_degree):
                b_right = degree - 1 - x_degree - b_left
                weight = math.comb(degree, b_right) * math.comb(
                    x_degree + b_left, x_degree
                )
                overlap = row.real(
                    row.product_expectation(B[b_left], B[b_right]),
                    label=f"E[B^{b_left} B^{b_right}]",
                )
                r_terms.append(alg.scale(
                    X[x_degree], weight * overlap
                ))
        R.append(alg.add(*r_terms))

        current_sizes = _state_sizes(
            degree, X, C, A, Z, G, E, B, R
        )
        counts.append(current_sizes)
        if progress:
            progress(_progress_line(
                "derivative", activation, current_sizes,
                time.perf_counter() - started,
            ))

    derivatives: list[mp.mpf] = []
    even_residuals: list[mp.mpf] = []
    for degree in range(max_order + 1):
        derivative = row.real(
            mp.fsum(
                math.comb(degree, left)
                * row.product_expectation(A[left], G[degree - left])
                for left in range(degree + 1)
            ),
            label=f"Derivative F^{degree}",
        )
        derivatives.append(derivative)
        if degree % 2 == 0:
            even_residuals.append(abs(derivative))

    return JetResult(
        route="derivative",
        activation=activation,
        scale=scale,
        dps=dps,
        derivatives=derivatives,
        even_residuals=even_residuals,
        elapsed_seconds=time.perf_counter() - started,
        term_counts=counts,
        tilted_wick_cache_sizes={
            "column": len(column.cache),
            "row": len(row.cache),
        },
    )


def relative_error(left: object, right: object) -> mp.mpf:
    left_mp = mp.mpf(left)
    right_mp = mp.mpf(right)
    return abs(left_mp - right_mp) / max(
        mp.mpf(1), abs(left_mp), abs(right_mp)
    )


def _assert_frozen_prefix(result: JetResult) -> None:
    controls = {
        "raw": {
            1: mp.mpf("1"),
            3: mp.mpf(
                "-1.886999827305931100883737327378247266466322061040333546307940021536186"
            ),
            5: mp.mpf(
                "79.41498981614465305749487667598359722832666710865177953401263030229069"
            ),
        },
        "unit": {
            1: mp.mpf(
                "4.037096946465641770044150036061438410171402282463690230320786544802301"
            ),
            3: mp.mpf(
                "-103.2573311467741889140412475573025922826622454848942874837843393529655"
            ),
            5: mp.mpf(
                "29944.43234293728236390344108299615290639013823097744233193199439481046"
            ),
        },
    }
    tolerance = mp.power(10, -min(60, result.dps - 25))
    for order, expected in controls[result.activation].items():
        if order >= len(result.derivatives):
            continue
        error = relative_error(result.derivatives[order], expected)
        if error > tolerance:
            raise AssertionError(
                f"{result.activation}/{result.route} frozen F^{order} "
                f"gate failed: relative error {error}"
            )


def validate_results(results: Iterable[JetResult], max_order: int) -> None:
    results = list(results)
    for result in results:
        _assert_frozen_prefix(result)
        even_limit = mp.power(10, -min(70, result.dps - 20))
        if any(residual > even_limit for residual in result.even_residuals):
            raise AssertionError(
                f"{result.activation}/{result.route} parity gate failed: "
                f"{result.even_residuals}"
            )
    grouped: dict[tuple[str, int], list[JetResult]] = {}
    for result in results:
        grouped.setdefault((result.activation, result.dps), []).append(result)
    for (activation, dps), group in grouped.items():
        if len(group) != 2:
            continue
        errors = [
            relative_error(left, right)
            for left, right in zip(
                group[0].derivatives, group[1].derivatives
            )
        ]
        limit = mp.power(10, -min(65, dps - 25))
        if max(errors[: max_order + 1], default=mp.mpf(0)) > limit:
            raise AssertionError(
                f"{activation} routes disagree: max error {max(errors)}"
            )


def _serialize_result(result: JetResult, digits: int = 80) -> dict[str, object]:
    return {
        "route": result.route,
        "activation": result.activation,
        "scale": mp.nstr(result.scale, digits),
        "dps": result.dps,
        "derivatives": [mp.nstr(value, digits) for value in result.derivatives],
        "even_residuals": [
            mp.nstr(value, 12) for value in result.even_residuals
        ],
        "elapsed_seconds": result.elapsed_seconds,
        "term_counts": result.term_counts,
        "tilted_wick_cache_sizes": result.tilted_wick_cache_sizes,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-order", type=int, default=9)
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument(
        "--activation", choices=("raw", "unit", "both"), default="both"
    )
    parser.add_argument(
        "--route", choices=("taylor", "derivative", "both"), default="both"
    )
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    actual_protocol_hash = sha256(PROTOCOL)
    if actual_protocol_hash != EXPECTED_PROTOCOL_SHA256:
        raise AssertionError(
            f"protocol SHA-256 gate failed: got {actual_protocol_hash}, "
            f"expected {EXPECTED_PROTOCOL_SHA256}"
        )

    progress: Progress | None = None if args.quiet else print
    activations = (
        ("raw", "unit") if args.activation == "both" else (args.activation,)
    )
    routes = (
        ("taylor", "derivative") if args.route == "both" else (args.route,)
    )
    results: list[JetResult] = []
    for activation in activations:
        for route in routes:
            assembler = taylor_jet if route == "taylor" else derivative_jet
            results.append(assembler(
                args.max_order,
                dps=args.dps,
                activation=activation,
                progress=progress,
            ))
    validate_results(results, args.max_order)

    payload = {
        "model": "equal-width-two-hidden-layer-sine",
        "max_order": args.max_order,
        "protocol_sha256": actual_protocol_hash,
        "validation": "passed",
        "results": [_serialize_result(result) for result in results],
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        for result in results:
            values = ", ".join(
                f"F^{order}={mp.nstr(value, 30)}"
                for order, value in enumerate(result.derivatives)
            )
            print(f"{result.activation}/{result.route}: {values}")
        print("validation: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
