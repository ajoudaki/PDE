"""Regression gates for the retained canonical production extension."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pytest


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "production_canonical_recurrence.py"
RESULT = HERE / "PRODUCTION_RESULT.json"
INDEPENDENT_RESULT = HERE / "INDEPENDENT_RESULT.json"


def load_source():
    spec = importlib.util.spec_from_file_location("production_canonical", SOURCE)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_result_is_bound_to_source_and_frozen_inputs() -> None:
    module = load_source()
    document = json.loads(RESULT.read_text())
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == document["source"][
        "sha256"
    ]
    assert document["source"]["frozen_order13_source_sha256"] == (
        module.FROZEN_SOURCE_SHA256
    )
    assert document["source"]["frozen_order13_certificate_sha256"] == (
        module.FROZEN_CERTIFICATE_SHA256
    )
    module.verify_frozen_inputs()


def test_retained_exact_results_and_structural_gates() -> None:
    document = json.loads(RESULT.read_text())
    derivatives = {
        int(order): int(value)
        for order, value in document["feature_derivatives"].items()
    }
    assert tuple(derivatives[order] for order in range(14)) == load_source().ACCEPTED_PREFIX
    assert derivatives[15] == 49079184579077107476764629402991788032
    assert derivatives[17] == 30555969894096099495444855650521777374167040
    assert all(derivatives[order] == 0 for order in range(0, 18, 2))
    assert document["gates"]["order17_under_30_minute_8_GiB_cap"] is True
    assert document["order17_run"]["internal_elapsed_seconds"] < 1800
    assert document["order17_run"]["internal_max_rss_mib"] < 8192


def test_independent_route_agrees_exactly() -> None:
    production = json.loads(RESULT.read_text())["feature_derivatives"]
    independent = json.loads(INDEPENDENT_RESULT.read_text())["feature_derivatives"]
    assert production == independent


def test_fresh_exact_prefix_smoke() -> None:
    module = load_source()
    result = module.canonical_recurrence(
        9, wall_cap_seconds=120, memory_cap_mib=1024
    )
    assert tuple(result.derivatives) == module.ACCEPTED_PREFIX[:10]
    assert result.arithmetic.polynomial_products > 0
    assert result.row_wick_cache > 0
    assert result.column_wick_cache > 0


def test_protocol_refuses_order_nineteen() -> None:
    module = load_source()
    with pytest.raises(ValueError, match="seventeen"):
        module.canonical_recurrence(19)
