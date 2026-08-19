"""Independent regressions for the exact block-metric counterexample."""

from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "block_metric_counterexample.py"
CERTIFICATE = HERE / "BLOCK_METRIC_COUNTEREXAMPLE.json"


def load_module():
    spec = importlib.util.spec_from_file_location("block_metric_counterexample", SOURCE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_exact_certificate_matches_regeneration() -> None:
    module = load_module()
    retained = json.loads(CERTIFICATE.read_text())
    assert module.build_certificate() == retained


def test_independent_derivation_prefix_and_parity() -> None:
    module = load_module()
    derivatives = module.feature_derivatives(13)
    assert derivatives[1::2] == [
        Fraction(63),
        Fraction(77760),
        Fraction(274547232),
        Fraction(2141006515200),
        Fraction(31149221916487680),
        Fraction(759035131220036321280),
        Fraction(28719223368439752070594560),
    ]
    assert derivatives[0::2] == [Fraction(0)] * 7


def test_direct_shifted_hankel_witness_is_negative() -> None:
    module = load_module()
    derivatives = module.feature_derivatives(13)
    h_moments = module.inverse_derivative_moments(derivatives, 7)
    mu = module.output_kernel_moments(h_moments)
    matrix = module.hankel(mu, 3, shift=1)
    vector = [
        40042013405871059816,
        -655956126345867302340,
        2310453239160606810795,
    ]
    assert module.determinant(matrix) == Fraction(
        -86245462994269879146938487857152,
        200150589172828762588730609071155193161975,
    )
    assert module.quadratic_form(matrix, vector) == Fraction(
        -54453896050746839005408691307243842778031040,
        4991679,
    )
