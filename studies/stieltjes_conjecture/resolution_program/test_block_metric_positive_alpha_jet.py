"""Independent regressions for the exact beta=1 positive-alpha jet."""

from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "block_metric_positive_alpha_jet.py"
CERTIFICATE = HERE / "BLOCK_METRIC_POSITIVE_ALPHA_JET.json"


def load_source():
    spec = importlib.util.spec_from_file_location("positive_alpha_jet", SOURCE)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_stored_certificate_matches_source_table() -> None:
    module = load_source()
    document = json.loads(CERTIFICATE.read_text())
    stored = {
        int(order): tuple(int(value) for value in coefficients)
        for order, coefficients in document["feature_derivative_polynomials"].items()
    }
    assert stored == module.EXACT_JETS
    assert document["gates"]["full_fourteen_node_regeneration"] is True
    assert document["canonical_F13_at_alpha_one"] == str(
        module.evaluate_coefficients(module.EXACT_JETS[13], 1)
    )


def test_all_campaign4_beta_one_coefficients() -> None:
    module = load_source()
    campaign4 = module.campaign4_beta_one_jets()
    assert all(campaign4[order] == module.EXACT_JETS[order] for order in range(10))


def test_axis_recurrence_through_order_thirteen() -> None:
    module = load_source()
    derivatives = module.feature_derivatives(Fraction(0), 13)
    assert derivatives == [
        Fraction(module.evaluate_coefficients(module.EXACT_JETS[order], 0))
        for order in range(14)
    ]


def test_canonical_recurrence_through_order_nine() -> None:
    module = load_source()
    derivatives = module.feature_derivatives(Fraction(1), 9)
    assert derivatives == [
        Fraction(module.evaluate_coefficients(module.EXACT_JETS[order], 1))
        for order in range(10)
    ]
    assert derivatives[9] == 1181161141825400561664


def test_exact_interpolation_and_structural_bounds() -> None:
    module = load_source()
    for order, coefficients in module.EXACT_JETS.items():
        values = [
            Fraction(module.evaluate_coefficients(coefficients, node))
            for node in range(14)
        ]
        assert module.interpolate_at_nonnegative_integers(values) == coefficients
        assert len(coefficients) <= order + 1
        if order % 2 == 0:
            assert coefficients == ()
