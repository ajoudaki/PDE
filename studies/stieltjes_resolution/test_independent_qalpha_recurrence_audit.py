"""Bounded regressions for the independent direct-Q[alpha] audit."""

import json
from pathlib import Path

from independent_qalpha_recurrence_audit import (
    direct_qalpha_recurrence,
    retained_jets,
)


HERE = Path(__file__).resolve().parent
AUDIT = HERE / "INDEPENDENT_QALPHA_AUDIT.json"
JET_CERTIFICATE = HERE / "BLOCK_METRIC_POSITIVE_ALPHA_JET.json"


def test_direct_qalpha_recurrence_prefix() -> None:
    regenerated, _ = direct_qalpha_recurrence(5)
    retained = retained_jets()
    assert regenerated == {order: retained[order] for order in range(6)}


def test_retained_full_audit_matches_decisive_artifacts() -> None:
    audit = json.loads(AUDIT.read_text())
    jets = json.loads(JET_CERTIFICATE.read_text())
    assert audit["imports_production_generator"] is False
    assert audit["all_jet_coefficients_match"] is True
    assert audit["determinant_interval_matches"] is True
    assert audit["epsilon"] == "1/100"
    assert audit["decisive_F13_coefficients"] == jets[
        "feature_derivative_polynomials"
    ]["13"]

