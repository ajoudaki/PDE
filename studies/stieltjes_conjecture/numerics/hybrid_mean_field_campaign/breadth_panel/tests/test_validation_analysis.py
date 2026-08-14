from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

import pytest


PANEL = Path(__file__).resolve().parents[1]
if str(PANEL) not in sys.path:
    sys.path.insert(0, str(PANEL))

import validation_analysis as analysis  # noqa: E402


@pytest.fixture(scope="module")
def result() -> dict:
    return analysis.analyze()


def test_tracked_outputs_are_exact_recomputation(result):
    analysis.check_outputs(result)
    tracked = json.loads(analysis.RESULT_PATH.read_text(encoding="utf-8"))
    assert tracked == result
    digest = hashlib.sha256(analysis.RESULT_PATH.read_bytes()).hexdigest()
    assert digest in analysis.REPORT_PATH.read_text(encoding="utf-8")


def test_exact_local_outcomes_and_global_hard_stop(result):
    configs = result["configurations"]
    assert configs["A"]["local_validation_status"] == "fail"
    assert configs["A"]["scientific_status"] == "inconclusive"
    assert configs["A"]["failed_gates"] == ["w_cosine", "driver_max"]
    assert configs["M"]["local_validation_status"] == "pass"
    assert configs["M"]["scientific_status"] == "local-pass-only"
    assert configs["M"]["failed_gates"] == []
    assert configs["V"]["local_validation_status"] == "fail"
    assert configs["V"]["scientific_status"] == "inconclusive"
    assert configs["V"]["failed_gates"] == ["w_cosine"]
    decision = result["global_decision"]
    assert decision["failed_local_configurations"] == ["A", "V"]
    assert decision["two_failure_hard_stop_triggered"] is True
    assert decision["width_screen_authorized_or_recorded"] is False
    assert decision["two_input_authorized_or_recorded"] is False
    assert len(decision["recorded_output_points"]) == 6
    assert decision["stieltjes_evidence_added"] is False


def test_common_output_clock_differences_are_reproduced(result):
    expected = {
        "A": (0.00025887739449992163, 0.00025922642974039815, 0.0001375218265934536),
        "M": (0.00040660010796863557, 0.0003995692605211546, 0.00020050086789687128),
        "V": (0.00019170176165809636, 0.00018810076250291925, 0.00009279266879139828),
    }
    for group, values in expected.items():
        comparisons = result["configurations"][group]["coarse_fine"]
        observed = tuple(
            comparisons[name]["max_symmetric_relative_difference"]
            for name in ("Keff", "Kdir", "Q2")
        )
        assert observed == pytest.approx(values, rel=0.0, abs=2e-17)
        assert comparisons["Keff"]["max_symmetric_relative_difference"] <= 0.002
    assert result["configurations"]["M"]["gate_pass"]["Q2_coarse_fine"] is True


def test_authority_is_fail_closed(result):
    authority = result["authority"]
    assert authority["attempts_verified"] == 6
    assert set(authority["attempt_statuses"].values()) == {"complete"}
    assert authority["recorded_attempt_ledgers"] == [
        "runs/validation_one_input_v1/ATTEMPTS.json"
    ]


def test_digest_mismatch_is_rejected(tmp_path):
    path = tmp_path / "raw.bin"
    path.write_bytes(b"first")
    digest = analysis.sha256(path)
    path.write_bytes(b"second")
    assert analysis.sha256(path) != digest
    with pytest.raises(analysis.ValidationError, match="synthetic digest mismatch"):
        analysis._require(analysis.sha256(path) == digest, "synthetic digest mismatch")
