from __future__ import annotations

import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "independent_canonical_recurrence.py"
RESULT = HERE / "INDEPENDENT_RESULT.json"


def load_module():
    spec = importlib.util.spec_from_file_location(
        "independent_canonical_recurrence", SOURCE
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_wick_law_and_expected_partial_are_exact() -> None:
    module = load_module()
    law = module.GaussianLaw(3)
    # Base g is independent of (h0,h1), while Var(h0)=2,
    # Cov(h0,h1)=3, and Var(h1)=5.
    law.install_covariance(1, [Fraction(2)])
    law.install_covariance(2, [Fraction(3), Fraction(5)])
    g = module.gaussian_variable(0)
    h0 = module.gaussian_variable(1)
    h1 = module.gaussian_variable(2)
    assert law.inner(g, h0) == 0
    assert law.inner(h0, h1) == 3
    assert law.inner(module.product(h0, h0), module.product(h1, h1)) == 28
    polynomial = module.product(module.product(h0, h0), h1)
    assert law.expected_partial(polynomial, 1) == 6


def test_independent_recurrence_reproduces_prefix_through_seven() -> None:
    module = load_module()
    result = module.canonical_recurrence(7)
    assert result.derivatives == list(module.ACCEPTED_PREFIX[:8])


def test_retained_high_order_result_and_source_binding() -> None:
    module = load_module()
    document = json.loads(RESULT.read_text())
    derivatives = {
        int(order): int(value)
        for order, value in document["feature_derivatives"].items()
    }
    assert [derivatives[k] for k in range(14)] == list(module.ACCEPTED_PREFIX)
    assert derivatives[15] == 49079184579077107476764629402991788032
    assert derivatives[17] == 30555969894096099495444855650521777374167040
    assert all(derivatives[k] == 0 for k in range(0, 18, 2))

    import hashlib

    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == document["source"][
        "sha256"
    ]
    assert all(document["gates"].values())
