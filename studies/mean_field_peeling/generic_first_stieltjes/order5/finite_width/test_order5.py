from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path

import numpy as np

from .exact_controls import (
    QUADRATIC_LARGE_WIDTH,
    linear_annealed,
    linear_wick_enumeration,
    width_one_polynomial_annealed,
)
from .feature_flow import draw_state, feature_flow_jet
from .oracles import polynomial_oracle, sine_oracle, tanh_oracle
from .raw_ad import raw_coordinate_jet
from .regression import certify_seedwise_routes


def _assert_routes(width, seed, q0, oracle):
    state = draw_state(width, seed)
    moving = feature_flow_jet(state, q0, oracle).derivatives
    raw = raw_coordinate_jet(state, q0, oracle)
    np.testing.assert_allclose(moving, raw.derivatives, rtol=2.0e-11, atol=2.0e-11)
    np.testing.assert_allclose(
        moving[5], raw.six_families.value, rtol=2.0e-10, atol=2.0e-10
    )
    assert len(raw.six_families.weighted_families) == 6


def test_two_independent_routes_seedwise() -> None:
    activations = (
        polynomial_oracle([0.0, 1.0]),
        polynomial_oracle([0.3, -0.7, 0.2, 0.1]),
        tanh_oracle,
        sine_oracle,
    )
    for width in (1, 2):
        for seed, oracle in enumerate(activations, start=17):
            _assert_routes(width, seed, 0.73, oracle)


def test_constant_and_affine_exact_width_one_controls() -> None:
    assert width_one_polynomial_annealed([2]) == (
        Fraction(0), Fraction(4), Fraction(0), Fraction(0), Fraction(0), Fraction(0)
    )
    assert width_one_polynomial_annealed([1, 2]) == (
        Fraction(0),
        Fraction(57),
        Fraction(0),
        Fraction(34832),
        Fraction(0),
        Fraction(58495488),
    )


def test_linear_exact_controls() -> None:
    assert width_one_polynomial_annealed([0, 1]) == linear_annealed(1)
    for width in (1, 2, 3):
        assert linear_wick_enumeration(width) == linear_annealed(width)
    for width in (1, 2, 7, 101):
        target = linear_annealed(width)
        assert target[1] == 3
        assert target[3] == Fraction(48) + Fraction(60, width)
        assert target[5] == Fraction(1464) + Fraction(4800, width) + Fraction(4320, width**2)


def test_quadratic_width_one_exact_wick_control() -> None:
    assert width_one_polynomial_annealed([0, 0, 1]) == (
        Fraction(0),
        Fraction(1455),
        Fraction(0),
        Fraction(25604087040),
        Fraction(0),
        Fraction(13167513029295424800),
    )


def test_generic_quadratic_matches_accepted_finite_width_compiler() -> None:
    path = Path(__file__).resolve().parents[3] / "quadratic_compiler" / "finite_width_jet_reference.py"
    spec = importlib.util.spec_from_file_location("quadratic_order5_reference", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    oracle = polynomial_oracle([0.0, 0.0, 1.0])
    for width in (1, 2, 5):
        for seed in (0, 7):
            generic = feature_flow_jet(draw_state(width, seed), 1.0, oracle).ordinary_coefficients
            accepted = module.feature_jet(width, 5, 1.0, seed)
            np.testing.assert_allclose(generic, accepted, rtol=3.0e-13, atol=3.0e-10)


def test_quadratic_exact_frozen_large_width_endpoint() -> None:
    path = (
        Path(__file__).resolve().parents[3]
        / "quadratic_compiler"
        / "campaign2"
        / "frozen"
        / "plus_order7_raw.json"
    )
    data = json.loads(path.read_text())
    endpoints = []
    for order in (1, 3, 5):
        raw = tuple(int(value) for value in data["raw_theta"][order])
        assert all(value == 0 for value in raw[1::2])
        numerator = sum(raw[0::2])
        denominator = 2 ** (order + 1)
        assert numerator % denominator == 0
        endpoints.append(Fraction(numerator, denominator))
    assert tuple(endpoints) == QUADRATIC_LARGE_WIDTH


def test_preregistered_sine_exact_pre_gate_only() -> None:
    # This intentionally does not execute or inspect the large-width panel.
    assert certify_seedwise_routes() < 5.0e-10
