from __future__ import annotations

import math

from dmft_contact_prototype import (
    conditional_second_moment,
    exact_initialization,
    run_contact_audit,
)
from truncated_mfp_reference import compute_jets


def test_gaussian_mfp_recovery_through_order_five() -> None:
    result = compute_jets(cutoff=None, max_order=5, dps=50)
    observed = [round(float(value)) for value in result["derivatives"]]
    assert observed == [0, 111, 0, 1_685_184, 0, 77_400_633_120]


def test_A3_truncated_mfp_reference() -> None:
    result = compute_jets(cutoff=3.0, max_order=5, dps=50)
    observed = [float(value) for value in result["derivatives"]]
    assert math.isclose(observed[1], 108.76030167165348, rel_tol=1e-14)
    assert math.isclose(observed[3], 1_610_470.7911171291, rel_tol=1e-14)
    assert math.isclose(observed[5], 72_197_074_701.38583, rel_tol=1e-14)


def test_exact_A3_initialization() -> None:
    m2 = conditional_second_moment(3.0)
    assert math.isclose(m2, 0.9733369246625415, rel_tol=1e-15)
    exact = exact_initialization(3.0)
    assert math.isclose(exact["kernel"], 27.0 + 84.0 * m2, rel_tol=1e-15)


def test_frozen_contact_audit_and_preserved_sampling_failure() -> None:
    result = run_contact_audit()
    assert result["status"] == "stage0_contact_only_no_positive_time_dmft"
    assert result["gates"]["A_contact"]
    assert result["gates"]["B_contact"]
    assert result["gates"]["response_free_ablation_fails"]
    # The frozen S=4096 Sobol initialization sample missed its preregistered
    # component tolerances.  This is a preserved validity failure, not a test
    # to be tuned away after inspection.
    assert not result["gates"]["components_within_0p5_percent"]
    assert not result["gates"]["kernel_within_0p25_percent"]
    assert not result["all_contact_and_initialization_gates_passed"]
