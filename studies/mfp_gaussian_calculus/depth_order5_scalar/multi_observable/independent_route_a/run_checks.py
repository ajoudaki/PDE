"""Deterministic and tiny finite-width audits for independent Route A."""

from __future__ import annotations

from functools import lru_cache
import hashlib
import json
from math import factorial
from pathlib import Path

import numpy as np

from ....depth.model import sample_state
from ...independent import forward_contraction as fw
from . import gamma04_contraction as g4
from .f7_tree_roadmap import report as tree_report
from .finite_width_hidden import (
    feature_ascent_hidden_jet,
    raw_coordinate_q_derivatives,
)
from .numeric_head import compile_numeric, polynomial_moment
from .reduce_gamma04 import transitions as reduced_transitions


HERE = Path(__file__).resolve().parent


def _alt_wick(monomial: g4.RMonomial) -> fw.SPoly:
    return _alt_wick_cached(monomial)


@lru_cache(maxsize=None)
def _alt_wick_cached(monomial: g4.RMonomial) -> fw.SPoly:
    # Deliberately reverse the producer's elimination order: last forward
    # innovation first, then last reverse innovation.
    last_forward = next(
        (i + 1 for i in range(4, -1, -1) if monomial.forward[i]), None
    )
    if last_forward is not None:
        forward = list(monomial.forward)
        forward[last_forward - 1] -= 1
        answer: fw.SPoly = {}
        for other in range(last_forward, 0, -1):
            count = forward[other - 1]
            covariance = g4.forward_covariance(last_forward, other)
            if not count or not covariance:
                continue
            paired = list(forward)
            paired[other - 1] -= 1
            target = g4.RMonomial(
                monomial.activation, tuple(paired), monomial.reverse
            )
            answer = fw.sa(
                answer,
                fw.sproduct(fw.sc(count), covariance, _alt_wick_cached(target)),
            )
        covariance0 = g4.forward_covariance(last_forward, 0)
        if covariance0:
            for count, activation in g4.activation_derivative(monomial.activation):
                target = g4.RMonomial(
                    activation, tuple(forward), monomial.reverse
                )
                answer = fw.sa(
                    answer,
                    fw.sproduct(
                        fw.sc(count), covariance0, _alt_wick_cached(target)
                    ),
                )
        return answer

    last_reverse = next(
        (i for i in range(4, -1, -1) if monomial.reverse[i]), None
    )
    if last_reverse is not None:
        reverse = list(monomial.reverse)
        reverse[last_reverse] -= 1
        answer: fw.SPoly = {}
        for other in range(last_reverse, -1, -1):
            count = reverse[other]
            covariance = g4.reverse_covariance(last_reverse, other)
            if not count or not covariance:
                continue
            paired = list(reverse)
            paired[other] -= 1
            target = g4.RMonomial(
                monomial.activation, monomial.forward, tuple(paired)
            )
            answer = fw.sa(
                answer,
                fw.sproduct(fw.sc(count), covariance, _alt_wick_cached(target)),
            )
        return answer
    return fw.moment(monomial.activation)


def _alt_expectation(value: g4.RPoly) -> fw.SPoly:
    answer: fw.SPoly = {}
    for monomial, coefficient in value.items():
        answer = fw.sa(answer, fw.sm(coefficient, _alt_wick(monomial)))
    return answer


def test_independent_atom_canonicalization() -> None:
    q = g4.local_polynomials()
    targets = {
        "gamma04_next": g4.rm(q["x0"], q["h4"]),
        "a41_next": g4.r_derivative(q["h4"], "e", 1),
        "a43_next": g4.r_derivative(q["h4"], "e", 4),
    }
    producer = g4.transitions()
    for name, value in targets.items():
        assert _alt_expectation(value) == producer[name], name


def polynomial_oracle(coefficients):
    coefficients = np.asarray(coefficients, dtype=float)

    def oracle(order: int, value: np.ndarray) -> np.ndarray:
        current = coefficients.copy()
        for _ in range(order):
            current = np.arange(1, current.size) * current[1:]
        if not current.size:
            return np.zeros_like(value)
        answer = np.zeros_like(value)
        for coefficient in current[::-1]:
            answer = answer * value + coefficient
        return answer

    return oracle


def test_exact_finite_width_raw_ad() -> None:
    oracle = polynomial_oracle((0.3, -0.7, 0.4, 0.2, -0.1))
    for hidden_layers, width in ((1, 1), (1, 2), (2, 1), (2, 2), (3, 1)):
        state = sample_state(
            width, np.asarray([[1.0]]), hidden_layers, 10 + hidden_layers + width
        )
        series = feature_ascent_hidden_jet(
            state,
            np.asarray([[1.0]]),
            np.asarray([1.0]),
            oracle,
            order=4,
        ).q_derivatives
        raw = raw_coordinate_q_derivatives(state, oracle, order=4)
        np.testing.assert_allclose(series, raw, rtol=3e-11, atol=3e-8)


def test_gamma_dictionary_and_parity() -> None:
    oracle = polynomial_oracle((0.1, 0.7, -0.2, 0.05))
    state = sample_state(4, np.asarray([[1.0]]), 3, 812)
    jet = feature_ascent_hidden_jet(
        state, np.asarray([[1.0]]), np.asarray([1.0]), oracle, order=4
    )
    for layer, gamma in enumerate(jet.gamma):
        for k in range(5):
            expected = sum(
                factorial(k)
                / (factorial(r) * factorial(k - r))
                * gamma[r, k - r]
                for r in range(k + 1)
            )
            np.testing.assert_allclose(jet.q_derivatives[layer, k], expected)
    flipped = type(state)(
        state.first_preactivation, state.hidden_weights, -state.readout
    )
    negative = feature_ascent_hidden_jet(
        flipped, np.asarray([[1.0]]), np.asarray([1.0]), oracle, order=4
    )
    for layer in range(3):
        for order in range(5):
            np.testing.assert_allclose(
                negative.feature_coefficients[layer][order],
                (-1) ** order * jet.feature_coefficients[layer][order],
                rtol=3e-12,
                atol=3e-12,
            )


def test_exact_controls() -> None:
    controls = {
        "constant": ((1,), ((0, 0), (0, 0))),
        "linear": ((0, 1), ((6, 96), (18, 528))),
        "affine": (
            (fw.Fraction(3, 5), fw.Fraction(4, 5)),
            (
                (fw.Fraction(33792, 15625), fw.Fraction(172045824, 9765625)),
                (fw.Fraction(2221344, 390625), fw.Fraction(3705931776, 48828125)),
            ),
        ),
    }
    for _, (activation, target) in controls.items():
        result = compile_numeric(2, polynomial_moment(activation))
        observed = tuple(
            (result["layers"][layer]["Q2"], result["layers"][layer]["Q4"])
            for layer in (1, 2)
        )
        assert observed == target


def test_frozen_artifacts_and_ceiling() -> None:
    frozen = HERE / "FROZEN_GAMMA04_RECURRENCE.json"
    expected = "724da08f11bc3ec71b90ad12305a5e1ebed4f00a2a7e116f99f7d6ce02a401b5"
    assert hashlib.sha256(frozen.read_bytes()).hexdigest() == expected
    payload = json.loads(frozen.read_text())
    assert payload["state"] == ["gamma04", "a41", "a43"]
    assert [len(g4.transitions()[name]) for name in g4.transitions()] == [83, 20, 1]
    maximum = 0
    for polynomial in g4.transitions().values():
        for monomial in polynomial:
            for name in monomial:
                if name.startswith("M"):
                    maximum = max(
                        maximum,
                        max(
                            index
                            for index, count in enumerate(map(int, name[1:]))
                            if count
                        ),
                    )
    # The observable head itself reaches phi^(4); attaching it to the
    # universal order-five backbone does not raise that backbone's ceiling 5.
    assert maximum == 4


def test_postfreeze_reduction_and_route_s() -> None:
    full = g4.transitions()
    assert full["a43_next"] == {("M020000", "l43"): fw.Fraction(1)}
    reduced = reduced_transitions()
    assert {name: len(poly) for name, poly in reduced.items()} == {
        "gamma04_next": 64,
        "a41_next": 17,
    }
    reduced_path = HERE / "REDUCED_GAMMA04_RECURRENCE.json"
    assert hashlib.sha256(reduced_path.read_bytes()).hexdigest() == (
        "32b5ee0f87562b6f15e2139682d9437bd4f691f90ac9ffa495d3efd5ccfc033c"
    )
    route_s_path = (
        HERE.parents[2]
        / "depth_order5_observables/independent/FROZEN_GAMMA04_REDUCED_RECURRENCE.json"
    )
    assert hashlib.sha256(route_s_path.read_bytes()).hexdigest() == (
        "e97a3f6afda6ae17d1be498ac79b308b64fc71e7fd94a1f343e0e28844762122"
    )
    route_s = json.loads(route_s_path.read_text())["transition"]
    for name, candidate in reduced.items():
        reference = {
            tuple(monomial.split("*")) if monomial else (): fw.Fraction(coefficient)
            for monomial, coefficient in route_s[name].items()
        }
        assert candidate == reference, name


def test_time_change_formulas() -> None:
    # Exact rational ordinary-series composition, evaluated at a generic
    # point to make all A/B/q2/q4 branches nonzero.
    from fractions import Fraction

    c, A, B, q2, q4 = map(Fraction, (2, 3, 5, 7, 11))
    # Derivatives of s from s'=c(1-F(s)).
    s1 = c
    s2 = -c**2 * A
    s3 = c**3 * A**2
    s4 = -c**4 * (A**3 + B)
    observed = (
        q2 * s1**2,
        3 * q2 * s1 * s2,
        q4 * s1**4 + q2 * (4 * s1 * s3 + 3 * s2**2),
        10 * q4 * s1**3 * s2 + q2 * (5 * s1 * s4 + 10 * s2 * s3),
    )
    expected = (
        c**2 * q2,
        -3 * c**3 * A * q2,
        c**4 * (q4 + 7 * A**2 * q2),
        -5 * c**5 * ((3 * A**3 + B) * q2 + 2 * A * q4),
    )
    assert observed == expected


def test_nonpolynomial_regression_and_f7_roadmap() -> None:
    regression = json.loads((HERE / "NORMALIZED_SINE_GAMMA04_RESULT.json").read_text())
    assert regression["decision"] == "pass"
    assert regression["nonfinite_count"] == 0
    trees = tree_report()
    assert trees["D5_coefficients"] == [2, 14, 16, 22, 30, 36]
    assert trees["D7_family_count_route_A"] == 23
    assert trees["status"].startswith("roadmap-only")


def run_checks() -> None:
    tests = (
        test_independent_atom_canonicalization,
        test_exact_finite_width_raw_ad,
        test_gamma_dictionary_and_parity,
        test_exact_controls,
        test_frozen_artifacts_and_ceiling,
        test_postfreeze_reduction_and_route_s,
        test_time_change_formulas,
        test_nonpolynomial_regression_and_f7_roadmap,
    )
    for test in tests:
        test()
        print("PASS", test.__name__)


if __name__ == "__main__":
    run_checks()
