"""Regression for the independent 37-node determinant reconstruction."""

import json
from pathlib import Path

from independent_scalar_determinant_audit import build_audit


HERE = Path(__file__).resolve().parent
RETAINED = HERE / "INDEPENDENT_SCALAR_DETERMINANT_AUDIT.json"


def test_retained_scalar_determinant_audit_regenerates_exactly() -> None:
    assert build_audit() == json.loads(RETAINED.read_text())


def test_scalar_audit_is_separate_from_qalpha_inversion() -> None:
    source = (HERE / "independent_scalar_determinant_audit.py").read_text()
    assert "alpha_interval_tools" not in source
    audit = build_audit()
    assert audit["all_37_scaled_coefficients_match"] is True
    assert audit["convex_interval_sign_reproduced"] is True
