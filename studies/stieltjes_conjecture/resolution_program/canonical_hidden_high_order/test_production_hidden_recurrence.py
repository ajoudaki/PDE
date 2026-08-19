"""Regression gates for the exact canonical hidden production jet."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pytest


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "production_hidden_recurrence.py"
RESULT = HERE / "PRODUCTION_HIDDEN_RESULT.json"


def load_source():
    spec = importlib.util.spec_from_file_location(
        "production_hidden_recurrence_tested", SOURCE
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def retained():
    return json.loads(RESULT.read_text())


def exact_map(name: str) -> dict[int, int]:
    return {int(order): int(value) for order, value in retained()[name].items()}


def test_result_is_source_bound_and_frozen_inputs_are_intact() -> None:
    module = load_source()
    document = retained()
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == document["source"][
        "sha256"
    ]
    module.verify_frozen_inputs()
    assert document["frozen_inputs"] == {
        "base_source": {
            "path": "studies/stieltjes_conjecture/resolution_program/canonical_high_order/production_canonical_recurrence.py",
            "sha256": module.BASE_SOURCE_SHA256,
        },
        "base_result": {
            "path": "studies/stieltjes_conjecture/resolution_program/canonical_high_order/PRODUCTION_RESULT.json",
            "sha256": module.BASE_RESULT_SHA256,
        },
        "campaign1_result": {
            "path": "studies/mean_field_peeling/quadratic_compiler/campaign1/results_order9_q2_order8.json",
            "sha256": module.CAMPAIGN1_RESULT_SHA256,
        },
    }


def test_retained_feature_and_hidden_jets() -> None:
    module = load_source()
    feature = exact_map("feature_derivatives")
    q1 = exact_map("q1_derivatives")
    q2 = exact_map("q2_derivatives")
    assert tuple(feature[k] for k in range(18)) == (
        module.ACCEPTED_FEATURE_DERIVATIVES
    )
    assert tuple(q1[k] for k in range(9)) == module.ACCEPTED_Q1_PREFIX
    assert tuple(q2[k] for k in range(9)) == module.ACCEPTED_Q2_PREFIX
    assert q1[16] == 392_633_476_632_616_859_814_117_035_223_934_304_256
    assert q2[16] == 33_941_339_036_399_103_897_550_977_212_861_900_095_488
    assert all(q1[k] == 0 and q2[k] == 0 for k in range(1, 17, 2))


def test_q1_ward_identity_and_production_gates() -> None:
    document = retained()
    feature = exact_map("feature_derivatives")
    q1 = exact_map("q1_derivatives")
    assert all(q1[k] == 8 * feature[k - 1] for k in range(1, 17))
    assert document["max_recurrence_order"] == 17
    assert document["max_hidden_order"] == 16
    assert all(document["gates"].values())
    assert document["resources"]["elapsed_seconds"] < 1800
    assert document["resources"]["max_rss_mib"] < 8192


def test_fresh_exact_campaign1_prefix_smoke() -> None:
    module = load_source()
    result = module.canonical_hidden_recurrence(
        9,
        hidden_max_order=8,
        wall_cap_seconds=120,
        memory_cap_mib=1024,
    )
    assert tuple(result.feature_derivatives) == (
        module.ACCEPTED_FEATURE_DERIVATIVES[:10]
    )
    assert tuple(result.q1_derivatives) == module.ACCEPTED_Q1_PREFIX
    assert tuple(result.q2_derivatives) == module.ACCEPTED_Q2_PREFIX


def test_protocol_refuses_unapproved_orders() -> None:
    module = load_source()
    with pytest.raises(ValueError, match="seventeen"):
        module.canonical_hidden_recurrence(19, hidden_max_order=16)
    with pytest.raises(ValueError, match="hidden_max_order"):
        module.canonical_hidden_recurrence(17, hidden_max_order=17)
