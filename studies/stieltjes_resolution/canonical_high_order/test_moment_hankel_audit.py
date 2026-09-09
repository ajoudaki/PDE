"""Regression tests for the independent canonical moment/Hankel audit."""

import json
from fractions import Fraction
from pathlib import Path

import pytest

from moment_hankel_audit import (
    CANONICAL_ODD_DERIVATIVES,
    EXPECTED_MOMENTS_THROUGH_MU5,
    build_report,
    output_kernel_moments,
)


Q = Fraction
HERE = Path(__file__).resolve().parent
ACCEPTED_F15_CANDIDATE = Q(49_079_184_579_077_107_476_764_629_402_991_788_032)
ACCEPTED_F17_CANDIDATE = Q(
    30_555_969_894_096_099_495_444_855_650_521_777_374_167_040
)


def test_direct_compositional_reversion_reproduces_mu0_through_mu5() -> None:
    assert output_kernel_moments(CANONICAL_ODD_DERIVATIVES) == (
        EXPECTED_MOMENTS_THROUGH_MU5
    )
    report = build_report()
    assert report["highest_feature_derivative_order"] == 13
    assert report["baseline_cross_checks"] == {
        "mu_0_through_mu_5_match": True,
        "ordinary_H2_matches": True,
        "shifted_H2_matches": True,
    }
    gates = report["available_hankel_gates"]
    assert gates["ordinary_H2"]["positive_definite"]
    assert gates["shifted_H2"]["positive_definite"]
    assert "ordinary_H3" not in gates


def test_retained_baseline_document_matches_live_reconstruction() -> None:
    retained = json.loads((HERE / "BASELINE_F13_AUDIT.json").read_text())
    live = build_report()
    assert retained["output_kernel_moments"] == live["output_kernel_moments"]
    assert retained["known_top_determinants"] == {
        "ordinary_H2": live["available_hankel_gates"]["ordinary_H2"][
            "determinant"
        ],
        "shifted_H2": live["available_hankel_gates"]["shifted_H2"][
            "determinant"
        ],
    }
    assert retained["F15_gate"]["exact_derivative_threshold"] == (
        live["f15_affine_gate"]["det_ordinary_H3_as_function_of_F15"][
            "zero_threshold"
        ]
    )


def test_retained_f15_document_matches_live_reconstruction() -> None:
    retained = json.loads((HERE / "F15_MOMENT_HANKEL_AUDIT.json").read_text())
    live = build_report(f15=ACCEPTED_F15_CANDIDATE)
    assert retained == live
    assert retained["output_kernel_moments"]["mu_6"] == (
        "233701098505506644778710348585571696126248608/"
        "523079786422749003601451969851378666466523525"
    )
    gate = retained["available_hankel_gates"]["ordinary_H3"]
    assert gate["positive_definite"]
    assert gate["negative_principal_minor_count"] == 0
    assert gate["zero_principal_minor_count"] == 0


def test_retained_f17_document_matches_live_reconstruction() -> None:
    retained = json.loads((HERE / "F17_MOMENT_HANKEL_AUDIT.json").read_text())
    live = build_report(
        f15=ACCEPTED_F15_CANDIDATE,
        f17=ACCEPTED_F17_CANDIDATE,
    )
    assert retained == live
    assert retained["output_kernel_moments"]["mu_7"] == (
        "70048496819304110407804100699554764688052780719822/"
        "218993917770958359962588987442799241938248378067125"
    )
    gate = retained["available_hankel_gates"]["shifted_H3"]
    assert gate["positive_definite"]
    assert gate["negative_principal_minor_count"] == 0
    assert gate["zero_principal_minor_count"] == 0
    assert retained["candidate_verdict"] == (
        "prefix_through_mu_7_compatible_canonical_V1_remains_open"
    )


def test_f15_threshold_is_exact_and_controls_ordinary_h3() -> None:
    baseline = build_report()
    threshold = Q(
        baseline["f15_affine_gate"]["det_ordinary_H3_as_function_of_F15"][
            "zero_threshold"
        ]
    )

    below = build_report(f15=threshold - 1)
    at = build_report(f15=threshold)
    above = build_report(f15=threshold + 1)
    assert not below["available_hankel_gates"]["ordinary_H3"][
        "positive_semidefinite"
    ]
    assert at["available_hankel_gates"]["ordinary_H3"]["determinant"] == "0"
    assert at["available_hankel_gates"]["ordinary_H3"][
        "decision"
    ] == "positive_semidefinite_singular"
    assert above["available_hankel_gates"]["ordinary_H3"][
        "positive_definite"
    ]
    assert below["candidate_verdict"] == (
        "canonical_V1_disproved_by_ordinary_H3_finite_witness"
    )
    assert above["candidate_verdict"] == (
        "prefix_through_mu_6_compatible_canonical_V1_remains_open"
    )
    assert above["next_required"]["feature_derivative"] == "F^(17)(0)"


def test_f17_threshold_is_exact_and_controls_shifted_h3() -> None:
    baseline = build_report()
    f15_threshold = Q(
        baseline["f15_affine_gate"]["det_ordinary_H3_as_function_of_F15"][
            "zero_threshold"
        ]
    )
    # Work strictly inside the ordinary-H3 pass side.
    f15 = f15_threshold + 1
    f15_report = build_report(f15=f15)
    f17_threshold = Q(
        f15_report["f17_affine_gate_given_f15"][
            "det_shifted_H3_as_function_of_F17"
        ]["zero_threshold"]
    )

    below = build_report(f15=f15, f17=f17_threshold - 1)
    at = build_report(f15=f15, f17=f17_threshold)
    above = build_report(f15=f15, f17=f17_threshold + 1)
    assert below["available_hankel_gates"]["shifted_H3"]["positive_definite"]
    assert at["available_hankel_gates"]["shifted_H3"]["determinant"] == "0"
    assert at["available_hankel_gates"]["shifted_H3"][
        "decision"
    ] == "positive_semidefinite_singular"
    assert not above["available_hankel_gates"]["shifted_H3"][
        "positive_semidefinite"
    ]
    assert above["candidate_verdict"] == (
        "canonical_V1_disproved_by_finite_Hankel_witness"
    )


def test_f17_requires_f15() -> None:
    with pytest.raises(ValueError, match=r"F\^\(17\)"):
        build_report(f17=1)
