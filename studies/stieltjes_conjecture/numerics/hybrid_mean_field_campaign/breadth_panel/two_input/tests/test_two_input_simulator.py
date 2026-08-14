from __future__ import annotations

import json
import math
import os
import sys
from pathlib import Path

import numpy as np
import pytest
import torch


TWO_INPUT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TWO_INPUT))

import two_input_engine as model  # noqa: E402
import two_input_simulator as simulator  # noqa: E402
import run_two_input_point as cli  # noqa: E402


def _point(purpose="validation_fine", step=1e-5):
    return {
        "id": "test_point",
        "purpose": purpose,
        "seed": 17,
        "lineage": 2,
        "width": 16,
        "sigma": -1,
        "theta": math.sqrt(0.5),
        "step": step,
        "stop_g": 0.95,
        "output_nodes": [0.5, 0.75, 0.9, 0.95],
        "prefix_digest_sizes": [8, 16],
        "rng_row_block": 5,
        "w_monitor_seed": 31,
        "w_monitor_extent": 16,
        "w_monitor_sample_size": 32,
        "diagnostic_stride": 4,
        "wall_sync_stride": 1,
        "caps": {
            "wall_seconds": 30,
            "max_steps": 100,
            "host_rss_gib": 4,
            "gpu_memory_gib": 4,
            "state_abs_ceiling": 1e6,
            "kernel_ceiling": 1e8,
            "component_sum_ulp_multiplier": 64,
            "channel_psd_ulp_multiplier": 64,
            "mean_g_monotonicity_tolerance": 1e-6,
            "mean_loss_monotonicity_tolerance": 1e-6,
        },
    }


def test_point_contract_supports_only_the_validation_pair_and_fine_screens():
    simulator.validate_point(_point("validation_coarse", 2e-5))
    simulator.validate_point(_point("validation_fine", 1e-5))
    simulator.validate_point(_point("width_screen", 1e-5))
    with pytest.raises(ValueError, match="only h"):
        simulator.validate_point(_point("validation_fine", 5e-6))
    with pytest.raises(ValueError, match="coarse validation"):
        simulator.validate_point(_point("validation_coarse", 1e-5))


def test_source_lock_binds_config_sources_protocol_proxy_and_bundle(
    tmp_path, monkeypatch
):
    lock_root = tmp_path / "lock"
    lock_root.mkdir()
    copied_targets = {}
    for basename in sorted(cli.REQUIRED_LOCK_BASENAMES):
        path = lock_root / "copied" / basename
        path.parent.mkdir(exist_ok=True)
        path.write_text(f"frozen {basename}\n")
        copied_targets[basename] = path
    monkeypatch.setattr(cli, "REQUIRED_LOCK_TARGETS", copied_targets)
    config = tmp_path / "points.json"
    config.write_text('{"schema_version":1,"points":[]}\n')
    entries = {
        os.path.relpath(path.resolve(), lock_root): cli.sha256(path)
        for path in copied_targets.values()
    }
    lock = {
        "status": "frozen",
        "config_sha256": cli.sha256(config),
        "sha256": entries,
        "bundle_sha256": cli.source_bundle_sha256(lock_root, entries),
    }
    lock_path = lock_root / "LOCK.json"
    lock_path.write_text(json.dumps(lock))
    assert cli.verify_lock(lock_path, config)["bundle_sha256"] == lock[
        "bundle_sha256"
    ]
    copied_targets["proxy_contract.py"].write_text("post-hoc mutation\n")
    with pytest.raises(RuntimeError, match="source-lock mismatch"):
        cli.verify_lock(lock_path, config)


def test_unlock_and_atomic_attempt_budgets_are_fail_closed(tmp_path):
    config = tmp_path / "points.json"
    config.write_text("frozen config\n")
    lock = tmp_path / "LOCK.json"
    lock.write_text("frozen lock\n")
    point = _point()
    unlock = {
        "status": "execution-authorized-once",
        "lock_sha256": cli.sha256(lock),
        "config_sha256": cli.sha256(config),
        "output_root": "runs",
        "allowed_points": {point["id"]: "cuda:0"},
        "allowed_gpu_names": ["test GPU class"],
        "point_groups": {point["id"]: "Tminus"},
        "cumulative_wall_seconds": 60,
        "per_group_wall_seconds": 30,
    }
    unlock_path = tmp_path / "UNLOCK.json"
    unlock_path.write_text(json.dumps(unlock))
    output_root = tmp_path / "runs"
    loaded, root = cli.verify_unlock(
        unlock_path,
        lock,
        config,
        point,
        "cuda:0",
        output_root,
    )
    assert root == output_root.resolve()
    ledger_path = cli.reserve_attempt(root, loaded, point, "cuda:0")
    ledger = json.loads(ledger_path.read_text())
    assert ledger["attempts"][point["id"]]["status"] == "reserved"
    with pytest.raises(RuntimeError, match="already consumed"):
        cli.reserve_attempt(root, loaded, point, "cuda:0")

    second = dict(point, id="second")
    loaded["point_groups"]["second"] = "Tminus"
    with pytest.raises(RuntimeError, match="per-group"):
        cli.reserve_attempt(root, loaded, second, "cuda:1")

    third = dict(point, id="third")
    loaded["point_groups"]["third"] = "Tplus"
    loaded["cumulative_wall_seconds"] = 30
    with pytest.raises(RuntimeError, match="cumulative"):
        cli.reserve_attempt(root, loaded, third, "cuda:1")


def test_common_g_clock_uses_one_ensemble_clock_not_individual_hits():
    time = np.array([0.0, 1.0, 2.0])
    g = np.array([[0.0, 0.0], [0.4, 0.6], [0.8, 1.2]])
    field = np.stack((time, 10.0 + 2.0 * time), axis=1)
    result = simulator.common_g_clock(
        time, g, {"probe": field, "g": g}, np.array([0.25, 0.75])
    )
    np.testing.assert_allclose(result["node_time"], [0.5, 1.5])
    np.testing.assert_allclose(
        np.mean(result["node_g"], axis=1), [0.25, 0.75]
    )
    np.testing.assert_allclose(
        result["node_probe"], [[0.5, 11.0], [1.5, 13.0]]
    )


def test_exact_channel_driver_diagnostic_has_zero_defect_for_exact_trace():
    time = np.array([0.0, 0.1, 0.2, 0.3])
    g = np.stack((2.0 * time, 4.0 * time), axis=1)
    # mean g has derivative 3, so mean effective numerator must be 1.5.
    numerator = np.full_like(g, 1.5)
    result = simulator.driver_diagnostics(
        time, g, numerator, through_g=1.0
    )
    assert result["driver_max_relative_defect"] < 2e-15
    assert result["driver_relative_rms_defect"] < 2e-15
    assert result["driver_cumulative_relative_defect"] < 2e-15


def test_leakage_terms_match_the_declared_three_term_score():
    g = np.array([[0.2, 0.4], [0.5, 0.5]])
    delta = np.array([[0.1, -0.1], [0.2, 0.2]])
    kg = np.full_like(g, 4.0)
    kd = np.full_like(g, 9.0)
    cross = np.full_like(g, 1.5)
    series = simulator.leakage_series(g, delta, kg, kd, cross)
    np.testing.assert_allclose(
        series["leakage_delta_rms_over_residual"],
        [0.1 / 0.7, 0.2 / 0.5],
    )
    np.testing.assert_allclose(
        series["leakage_delta_C_over_longitudinal"],
        [0.0, 0.3 / 2.0],
    )
    np.testing.assert_allclose(series["leakage_cross_correlation"], 0.25)
    summary = simulator.leakage_diagnostics(
        g, delta, kg, kd, cross, through_g=0.6
    )
    assert summary["maximum_leakage_score"] == pytest.approx(0.4)


def test_monotonicity_is_fail_closed_at_the_declared_tolerances():
    good = simulator.monotonicity_diagnostics(
        np.array([[0.0, 0.0], [0.1, 0.2], [0.3, 0.4]]),
        np.array([[1.0, 1.0], [0.8, 0.9], [0.5, 0.6]]),
        g_tolerance=1e-6,
        loss_tolerance=1e-6,
    )
    assert good["mean_g_nondecreasing"]
    assert good["mean_loss_nonincreasing"]
    bad = simulator.monotonicity_diagnostics(
        np.array([[0.0, 0.0], [0.2, 0.2], [0.19, 0.19]]),
        np.array([[1.0, 1.0], [0.8, 0.8], [0.81, 0.81]]),
        g_tolerance=1e-4,
        loss_tolerance=1e-4,
    )
    assert not bad["mean_g_nondecreasing"]
    assert not bad["mean_loss_nonincreasing"]


def test_small_cpu_smoke_records_clock_and_strided_full_W_checks():
    point = _point("validation_fine", 1e-5)
    point["stop_g"] = 5e-3
    point["output_nodes"] = [2.5e-3, 5e-3]
    point["caps"]["max_steps"] = 20
    point["diagnostic_stride"] = 2
    arrays, diagnostics = simulator.simulate_point(
        point, device=torch.device("cpu")
    )
    assert diagnostics["reached_stop_g"]
    assert diagnostics["completed_steps"] >= 1
    assert arrays["g"].shape[1] == 2
    assert arrays["output"].shape[1:] == (2, 2)
    assert arrays["kernel_matrix"].shape[1:] == (2, 2, 2)
    assert arrays["a_update_cosine"].shape[0] == diagnostics["completed_steps"]
    np.testing.assert_array_equal(arrays["full_w_check_steps"], [0, 2, 3])
    assert arrays["full_w_max_abs_at_checks"].shape == (3, 2)
    np.testing.assert_allclose(
        np.mean(arrays["node_g"], axis=1), point["output_nodes"], atol=2e-10
    )
    assert "driver_max_relative_defect" in diagnostics["driver"]
    assert "maximum_leakage_score" in diagnostics["leakage"]


@pytest.mark.parametrize("configuration", model.CORE_CONFIGURATIONS)
def test_transformed_prefix_hashes_match_across_widths(configuration):
    _, smaller = model.build_antithetic_state(
        configuration,
        7,
        seed=1234,
        lineage=5,
        device=torch.device("cpu"),
        row_block=3,
        prefix_sizes=(7,),
    )
    _, larger = model.build_antithetic_state(
        configuration,
        11,
        seed=1234,
        lineage=5,
        device=torch.device("cpu"),
        row_block=3,
        prefix_sizes=(7, 11),
    )
    assert smaller["physical_state_sha256"] == larger[
        "physical_prefix_sha256"
    ][7]
    assert smaller["physical_prefix_sha256"][7] == larger[
        "physical_prefix_sha256"
    ][7]
