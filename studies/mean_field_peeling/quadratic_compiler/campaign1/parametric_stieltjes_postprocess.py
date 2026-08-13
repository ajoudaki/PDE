#!/usr/bin/env python3
"""Exact Stieltjes postprocessing for Campaign 1 jets.

The peeling compiler emits exact derivatives as dense polynomials in one
metric parameter.  This module performs the logically separate formal-series
calculation needed for the finite Stieltjes tests.  In the notation used here,

    F(s) = s A(s**2),
    Q2(s) = B(s**2),
    x = F(s)**2 = r A(r)**2,       r = s**2.

After reversing ``x = r A(r)^2`` as ``r=r(x)``, the two tested functions are

    (K(sqrt(x)) - K(0))/x,
    (B(r(x)) - 3)/x,

where ``K(F(s)) = F'(s)``.  Their alternating coefficients are the output
moments ``mu`` and hidden-observable moments ``nu``.

All arithmetic is exact.  SymPy is used only for rational-function algebra,
polynomial factorization, and exact real-root isolation.  No numerical sample
is accepted as a sign certificate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Iterable, Sequence

import sympy as sp


def _cancel(value: sp.Expr) -> sp.Expr:
    """Return a cancelled exact rational expression."""
    return sp.cancel(value)


def _parse_exact(value: Any) -> sp.Expr:
    if isinstance(value, bool):
        raise TypeError("booleans are not exact jet coefficients")
    if isinstance(value, int):
        return sp.Integer(value)
    if isinstance(value, str):
        return sp.Rational(value)
    raise TypeError(f"unsupported exact coefficient {value!r}")


def dense_parameter_polynomial(
    coefficients: Sequence[Any], parameter: sp.Symbol
) -> sp.Expr:
    return sum(
        _parse_exact(coefficient) * parameter**degree
        for degree, coefficient in enumerate(coefficients)
    )


def _series_mul(
    left: Sequence[sp.Expr],
    right: Sequence[sp.Expr],
    degree: int,
) -> list[sp.Expr]:
    result = [sp.Integer(0) for _ in range(degree + 1)]
    for i, a in enumerate(left):
        if i > degree or a == 0:
            continue
        for j, b in enumerate(right):
            if i + j > degree:
                break
            if b:
                result[i + j] += a * b
    return [_cancel(value) for value in result]


def _series_power(
    series: Sequence[sp.Expr], exponent: int, degree: int
) -> list[sp.Expr]:
    if exponent < 0:
        raise ValueError("series exponent must be nonnegative")
    result = [sp.Integer(1)] + [sp.Integer(0)] * degree
    base = list(series[: degree + 1])
    base += [sp.Integer(0)] * (degree + 1 - len(base))
    while exponent:
        if exponent & 1:
            result = _series_mul(result, base, degree)
        exponent >>= 1
        if exponent:
            base = _series_mul(base, base, degree)
    return result


def _series_compose(
    outer: Sequence[sp.Expr],
    inner: Sequence[sp.Expr],
    degree: int,
) -> list[sp.Expr]:
    """Return ``outer(inner(x))`` through ``x**degree``.

    The inner series must have zero constant term.  This is the only
    composition needed by the postprocessor.
    """
    if inner and inner[0] != 0:
        raise ValueError("inner series must have zero constant coefficient")
    result = [sp.Integer(0) for _ in range(degree + 1)]
    power = [sp.Integer(1)] + [sp.Integer(0)] * degree
    for coefficient in outer[: degree + 1]:
        if coefficient:
            for index in range(degree + 1):
                result[index] += coefficient * power[index]
        power = _series_mul(power, inner, degree)
    return [_cancel(value) for value in result]


def reverse_r_times_a_squared(
    a: Sequence[sp.Expr], degree: int
) -> list[sp.Expr]:
    """Reverse ``x=r*A(r)^2`` through ``x**degree`` exactly."""
    if degree < 1:
        return [sp.Integer(0)]
    if not a or a[0] == 0:
        raise ValueError("F'(0)=A(0) must be nonzero")

    a_squared = _series_mul(a, a, max(0, degree - 1))
    forward = [sp.Integer(0)] + a_squared[:degree]
    linear = forward[1]

    reverse = [sp.Integer(0) for _ in range(degree + 1)]
    reverse[1] = _cancel(1 / linear)
    for order in range(2, degree + 1):
        # The coefficient of the new unknown reverse[order] is exactly the
        # linear coefficient of the forward series.  Terms of forward degree
        # >=2 cannot contain it at total x-degree ``order``.
        composed = _series_compose(forward, reverse, order)
        reverse[order] = _cancel(-composed[order] / linear)
    return reverse


def determinant(matrix: Sequence[Sequence[sp.Expr]]) -> sp.Expr:
    if not matrix:
        return sp.Integer(1)
    return _cancel(sp.Matrix(matrix).det(method="bareiss"))


def hankel_determinants(moments: Sequence[sp.Expr]) -> dict[str, list[sp.Expr]]:
    ordinary: list[sp.Expr] = []
    shifted: list[sp.Expr] = []
    size = 1
    while 2 * size - 2 < len(moments):
        ordinary.append(determinant([
            [moments[i + j] for j in range(size)]
            for i in range(size)
        ]))
        size += 1
    size = 1
    while 2 * size - 1 < len(moments):
        shifted.append(determinant([
            [moments[i + j + 1] for j in range(size)]
            for i in range(size)
        ]))
        size += 1
    return {"ordinary": ordinary, "shifted": shifted}


def _valuation_at_zero(poly: sp.Poly) -> int:
    if poly.is_zero:
        return math.inf
    return min(monomial[0] for monomial, coefficient in poly.terms()
               if coefficient)


def rational_valuation_at_zero(expression: sp.Expr, parameter: sp.Symbol) -> int:
    numerator, denominator = sp.fraction(_cancel(expression))
    num_poly = sp.Poly(numerator, parameter, domain=sp.QQ)
    den_poly = sp.Poly(denominator, parameter, domain=sp.QQ)
    if num_poly.is_zero:
        return math.inf
    return _valuation_at_zero(num_poly) - _valuation_at_zero(den_poly)


def _rational_midpoint(left: sp.Rational, right: sp.Rational) -> sp.Rational:
    return (left + right) / 2


def _refine_away_from_zero(
    poly: sp.Poly, left: sp.Rational, right: sp.Rational
) -> tuple[sp.Rational, sp.Rational]:
    if left < 0 < right or left == 0 < right:
        if poly.eval(0) == 0:
            return left, right
        left, right = poly.refine_root(
            left, right, eps=sp.Rational(1, 10**30)
        )
    return left, right


def polynomial_sign_on_nonnegative(
    expression: sp.Expr, parameter: sp.Symbol
) -> dict[str, Any]:
    """Certify the signs assumed by a rational polynomial on ``[0,infty)``.

    The fast certificate is coefficientwise.  If coefficients have mixed
    signs, exact real-root isolation partitions the ray and a rational point
    is evaluated in every open component.  The returned witnesses are exact
    rational numbers.
    """
    poly = sp.Poly(expression, parameter, domain=sp.QQ)
    if poly.is_zero:
        return {
            "signs": ["zero"],
            "method": "identically_zero",
            "zero_on_domain": True,
        }

    coefficients = poly.all_coeffs()
    if all(value >= 0 for value in coefficients):
        signs = ["positive"]
        zero_on_domain = poly.eval(0) == 0
        if zero_on_domain:
            signs.append("zero")
        return {
            "signs": signs,
            "method": "coefficientwise_nonnegative",
            "zero_on_domain": zero_on_domain,
        }
    if all(value <= 0 for value in coefficients):
        signs = ["negative"]
        zero_on_domain = poly.eval(0) == 0
        if zero_on_domain:
            signs.append("zero")
        return {
            "signs": signs,
            "method": "coefficientwise_nonpositive",
            "zero_on_domain": zero_on_domain,
        }

    intervals: list[tuple[sp.Rational, sp.Rational, int]] = []
    zero_on_domain = poly.eval(0) == 0
    for (left, right), multiplicity in poly.intervals():
        left = sp.Rational(left)
        right = sp.Rational(right)
        if right < 0:
            continue
        if left == right == 0:
            continue
        left, right = _refine_away_from_zero(poly, left, right)
        if right <= 0:
            continue
        if left <= 0:
            # This can only remain unresolved if root isolation failed to
            # distinguish a nonzero root from zero.  Be conservative.
            return {
                "signs": ["unknown"],
                "method": "root_isolation_inconclusive_at_zero",
                "zero_on_domain": zero_on_domain,
            }
        intervals.append((left, right, multiplicity))
        zero_on_domain = True

    samples: list[sp.Rational] = []
    if intervals:
        samples.append(intervals[0][0] / 2)
        for (_, previous_right, _), (next_left, _, _) in zip(
            intervals, intervals[1:], strict=False
        ):
            samples.append(_rational_midpoint(previous_right, next_left))
        samples.append(intervals[-1][1] + 1)
    else:
        samples.append(sp.Integer(0) if poly.eval(0) else sp.Integer(1))

    signs: set[str] = set()
    witnesses: dict[str, str] = {}
    for sample in samples:
        value = sp.sign(poly.eval(sample))
        if value > 0:
            signs.add("positive")
            witnesses.setdefault("positive", str(sample))
        elif value < 0:
            signs.add("negative")
            witnesses.setdefault("negative", str(sample))
        else:
            # A partition sample should never be a root.  Refuse to certify
            # rather than silently relying on a malformed isolating interval.
            signs.add("unknown")
    if zero_on_domain:
        signs.add("zero")
    return {
        "signs": sorted(signs),
        "method": "exact_real_root_isolation",
        "zero_on_domain": zero_on_domain,
        "positive_root_intervals": [
            [str(left), str(right), multiplicity]
            for left, right, multiplicity in intervals
        ],
        "rational_witnesses": witnesses,
    }


def certify_rational_nonnegative(
    expression: sp.Expr, parameter: sp.Symbol
) -> dict[str, Any]:
    """Give an exact certificate or exact counter-witness on ``[0,infty)``."""
    expression = _cancel(expression)
    numerator, denominator = sp.fraction(expression)
    numerator = sp.factor(numerator)
    denominator = sp.factor(denominator)
    numerator_sign = polynomial_sign_on_nonnegative(numerator, parameter)
    denominator_sign = polynomial_sign_on_nonnegative(denominator, parameter)

    denominator_signs = set(denominator_sign["signs"])
    numerator_signs = set(numerator_sign["signs"])
    if "unknown" in denominator_signs or "zero" in denominator_signs:
        status = "unresolved_or_singular"
    elif denominator_signs == {"positive"}:
        if "unknown" in numerator_signs:
            status = "unresolved"
        elif "negative" in numerator_signs:
            status = "falsified"
        elif numerator_signs == {"positive"}:
            status = "strictly_positive"
        elif numerator_signs == {"zero"}:
            status = "identically_zero"
        else:
            status = "nonnegative"
    elif denominator_signs == {"negative"}:
        if "unknown" in numerator_signs:
            status = "unresolved"
        elif "positive" in numerator_signs:
            status = "falsified"
        elif numerator_signs == {"negative"}:
            status = "strictly_positive"
        elif numerator_signs == {"zero"}:
            status = "identically_zero"
        else:
            status = "nonnegative"
    else:
        status = "unresolved_or_singular"

    return {
        "status": status,
        "expression": str(sp.factor(expression)),
        "numerator": str(numerator),
        "denominator": str(denominator),
        "numerator_sign": numerator_sign,
        "denominator_sign": denominator_sign,
    }


def _serialize(expressions: Iterable[sp.Expr]) -> list[str]:
    return [str(sp.factor(value)) for value in expressions]


def _certify_determinants(
    determinants: dict[str, list[sp.Expr]], parameter: sp.Symbol
) -> dict[str, list[dict[str, Any]]]:
    return {
        kind: [certify_rational_nonnegative(value, parameter) for value in values]
        for kind, values in determinants.items()
    }


def _normalize_forced_moment_powers(
    moments: Sequence[sp.Expr], parameter: sp.Symbol
) -> dict[str, Any]:
    expected_powers = list(range(1, len(moments) + 1))
    valuations = [rational_valuation_at_zero(value, parameter) for value in moments]
    normalized = [
        _cancel(value / parameter**power)
        for value, power in zip(moments, expected_powers, strict=True)
    ]
    exact_scaling_holds = all(
        valuation == power
        for valuation, power in zip(valuations, expected_powers, strict=True)
    )
    divisibility_holds = all(
        valuation >= power
        for valuation, power in zip(valuations, expected_powers, strict=True)
    )
    return {
        "expected_powers": expected_powers,
        "valuations_at_zero": [
            "infinity" if valuation == math.inf else valuation
            for valuation in valuations
        ],
        "expected_divisibility_holds": divisibility_holds,
        "exact_expected_valuation": exact_scaling_holds,
        "normalized": normalized,
        "ordinary_determinant_factor_for_size_d": "lambda^(d^2)",
        "shifted_determinant_factor_for_size_d": "lambda^(d*(d+1))",
        "congruence_note": (
            "If m_r=lambda^(r+1)*mbar_r, then H_d=lambda*D*Hbar_d*D "
            "and Hplus_d=lambda^2*D*Hbarplus_d*D, with "
            "D=diag(1,lambda,...,lambda^(d-1))."
        ),
    }


def _extract_dense_jets(raw: dict[str, Any], root: str) -> list[Sequence[Any]]:
    """Accept both the transparent Python and checked C++ result schemas."""
    if "jets" in raw:
        try:
            return raw["jets"][root]
        except (KeyError, TypeError) as error:
            raise ValueError(f"input does not contain jets.{root}") from error
    try:
        records = raw["observables"][root]["jets"]
    except (KeyError, TypeError) as error:
        raise ValueError(
            f"input does not contain observables.{root}.jets"
        ) from error
    orders = [int(record["order"]) for record in records]
    if orders != list(range(len(records))):
        raise ValueError(f"{root} production jets must contain contiguous orders from 0")
    return [record["lambda_coefficients"] for record in records]


def compute(raw: dict[str, Any], parameter_name: str = "lambda") -> dict[str, Any]:
    parameter = sp.Symbol(parameter_name, real=True, nonnegative=True)
    raw_f = _extract_dense_jets(raw, "f")
    raw_q2 = _extract_dense_jets(raw, "q2")

    f = [dense_parameter_polynomial(values, parameter) for values in raw_f]
    q2 = [dense_parameter_polynomial(values, parameter) for values in raw_q2]
    if any(f[order] != 0 for order in range(0, len(f), 2)):
        raise ValueError("output jet violates required odd parity")
    if any(q2[order] != 0 for order in range(1, len(q2), 2)):
        raise ValueError("Q2 jet violates required even parity")
    if not q2 or q2[0] != 3:
        raise ValueError(f"canonical Q2 initial value must be 3, got {q2[0]}")

    a = [
        _cancel(f[order] / math.factorial(order))
        for order in range(1, len(f), 2)
    ]
    b = [
        _cancel(q2[order] / math.factorial(order))
        for order in range(0, len(q2), 2)
    ]
    if not a or a[0] == 0:
        raise ValueError("the supplied output jet has F'(0)=0")

    a_degree = len(a) - 1
    b_degree = len(b) - 1
    q2_x_degree = min(b_degree, a_degree + 1)
    reverse_degree = max(a_degree, q2_x_degree)
    reverse = reverse_r_times_a_squared(a, reverse_degree)

    # Since F(s)=s*A(r), F'(s)=A(r)+2r*A'(r), hence the coefficient
    # of r**j is (2j+1)*a[j].
    k_in_r = [(2 * index + 1) * value for index, value in enumerate(a)]
    k_in_x = _series_compose(k_in_r, reverse, a_degree)
    mu = [
        _cancel((-1)**index * k_in_x[index + 1])
        for index in range(a_degree)
    ]

    q2_in_x = _series_compose(b, reverse, q2_x_degree)
    nu = [
        _cancel((-1)**index * q2_in_x[index + 1])
        for index in range(q2_x_degree)
    ]

    mu_hankel = hankel_determinants(mu)
    nu_hankel = hankel_determinants(nu)
    mu_scaling = _normalize_forced_moment_powers(mu, parameter)
    nu_scaling = _normalize_forced_moment_powers(nu, parameter)
    mu_bar_hankel = hankel_determinants(mu_scaling["normalized"])
    nu_bar_hankel = hankel_determinants(nu_scaling["normalized"])

    return {
        "schema_version": 1,
        "parameter": parameter_name,
        "construction": {
            "A_coefficients_in_r": _serialize(a),
            "B_coefficients_in_r": _serialize(b),
            "reverse_r_coefficients_in_x": _serialize(reverse),
            "K_coefficients_in_x": _serialize(k_in_x),
            "Q2_coefficients_in_x": _serialize(q2_in_x),
        },
        "output_kernel": {
            "moments_mu": _serialize(mu),
            "forced_scaling": {
                **{key: value for key, value in mu_scaling.items()
                   if key != "normalized"},
                "normalized_moments_mu_bar": _serialize(mu_scaling["normalized"]),
            },
            "raw_hankel_determinants": {
                kind: _serialize(values) for kind, values in mu_hankel.items()
            },
            "normalized_hankel_determinants": {
                kind: _serialize(values) for kind, values in mu_bar_hankel.items()
            },
            "raw_sign_certificates": _certify_determinants(mu_hankel, parameter),
            "normalized_sign_certificates": _certify_determinants(
                mu_bar_hankel, parameter
            ),
        },
        "second_hidden_norm": {
            "definition": "T2(x)=(Q2(F^{-1}(sqrt(x)))-3)/x",
            "moments_nu": _serialize(nu),
            "forced_scaling": {
                **{key: value for key, value in nu_scaling.items()
                   if key != "normalized"},
                "normalized_moments_nu_bar": _serialize(nu_scaling["normalized"]),
            },
            "raw_hankel_determinants": {
                kind: _serialize(values) for kind, values in nu_hankel.items()
            },
            "normalized_hankel_determinants": {
                kind: _serialize(values) for kind, values in nu_bar_hankel.items()
            },
            "raw_sign_certificates": _certify_determinants(nu_hankel, parameter),
            "normalized_sign_certificates": _certify_determinants(
                nu_bar_hankel, parameter
            ),
        },
        "interpretation_limit": (
            "Certificates establish only the displayed finite Hankel tests for "
            "the supplied formal mean-field jets; they do not prove either "
            "all-order Stieltjes conjecture or global trajectory identification."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json", type=Path)
    parser.add_argument("--parameter", default="lambda")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    input_bytes = args.input_json.read_bytes()
    raw = json.loads(input_bytes)
    result = compute(raw, args.parameter)
    result["provenance"] = {
        "input": str(args.input_json),
        "input_sha256": hashlib.sha256(input_bytes).hexdigest(),
        "postprocessor_sha256": hashlib.sha256(
            Path(__file__).read_bytes()
        ).hexdigest(),
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
        print(f"sha256={hashlib.sha256(encoded.encode()).hexdigest()}")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
