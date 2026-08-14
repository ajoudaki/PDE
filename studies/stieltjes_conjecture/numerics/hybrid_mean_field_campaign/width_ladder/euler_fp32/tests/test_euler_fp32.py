from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
import pytest
import torch


HERE = Path(__file__).resolve().parents[1]
REFERENCE = HERE.parents[2] / "global_proxy_campaign" / "reference"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REFERENCE))

import canonical_model  # noqa: E402
import analyze_stage_v  # noqa: E402
import euler_engine as engine  # noqa: E402
import nested_init  # noqa: E402
import run_stage_v_point  # noqa: E402


def tiny_point(*, max_steps: int = 2) -> dict:
    return {
        "id": "cpu_smoke",
        "integrator": "euler",
        "dtype": "float32",
        "target": 1.0,
        "width": 8,
        "lineage_start": 0,
        "lineage_stop": 1,
        "step": 1.0e-5,
        "max_time": 2.0e-5,
        "output_nodes": [0.0, 1.0e-5],
        "prefix_digest_sizes": [4, 8],
        "rng_row_block": 4,
        "w_monitor_sample_size": 16,
        "w_monitor_seed": 123,
        "w_monitor_extent": 8,
        "diagnostic_stride": 1,
        "wall_sync_stride": 1,
        "expected_full_w_checkpoint_steps": [0, 1, 2],
        "initial_mean_output_tolerance": 1.0e-7,
        "initial_symmetry_ulp_multiplier": 4.0,
        "monotonic_tolerance": 1.0e-6,
        "loss_nonincrease_tolerance": 1.0e-6,
        "caps": {
            "wall_seconds": 30.0,
            "max_steps_all_lineages": max_steps,
            "host_rss_gib": 6.0,
            "gpu_memory_gib": 12.0,
            "state_ceiling": 1.0e4,
            "kernel_floor": 1.0e-10,
            "kernel_ceiling": 1.0e10,
            "component_sum_ulp_multiplier": 8.0,
        },
    }


def test_nested_fp32_arrays_and_width_independent_prefix_digests():
    small = nested_init.generate_lineage(
        7, seed=91, lineage=3, row_block=2, prefix_sizes=(4, 7)
    )
    large = nested_init.generate_lineage(
        11, seed=91, lineage=3, row_block=5, prefix_sizes=(4, 7, 11)
    )
    for small_array, large_array in zip(small[:2], large[:2]):
        assert np.array_equal(small_array, large_array[:7])
    assert np.array_equal(small[2], large[2][:7, :7])
    assert small[3] != large[3]
    assert small[4][4] == large[4][4]
    assert small[4][7] == large[4][7]


def test_monitor_coordinates_are_deterministic_unique_and_hash_bound():
    first = nested_init.monitor_coordinates(31, seed=731, extent=17)
    second = nested_init.monitor_coordinates(31, seed=731, extent=17)
    assert all(np.array_equal(x, y) for x, y in zip(first[:2], second[:2]))
    assert first[2] == second[2]
    pairs = set(zip(first[0].tolist(), first[1].tolist()))
    assert len(pairs) == 31
    changed = nested_init.monitor_coordinates(31, seed=732, extent=17)
    assert first[2] != changed[2]


def test_fused_physical_gradient_and_kernel_match_autograd():
    generator = torch.Generator().manual_seed(202608200719)
    batch, width = 3, 5
    state = engine.State(
        torch.randn(batch, width, generator=generator, dtype=torch.float64),
        torch.randn(batch, width, width, generator=generator, dtype=torch.float64),
        torch.randn(batch, width, generator=generator, dtype=torch.float64),
    )
    tangent, obs = engine.fused_eval(state, target=1.0)
    a = state.a.clone().requires_grad_(True)
    W = state.W.clone().requires_grad_(True)
    u = state.u.clone().requires_grad_(True)
    z = torch.bmm(W, u.square().unsqueeze(-1)).squeeze(-1) / math.sqrt(width)
    output = torch.mean(a * z.square(), dim=1)
    ga, gW, gu = torch.autograd.grad(output.sum(), (a, W, u))
    factor = 2.0 * (1.0 - output)
    for actual, gradient, expand in (
        (tangent.a, ga, factor[:, None]),
        (tangent.W, gW, factor[:, None, None]),
        (tangent.u, gu, factor[:, None]),
    ):
        torch.testing.assert_close(
            actual, width * gradient * expand, rtol=2.0e-13, atol=2.0e-13
        )
    autograd_kernel = width * (
        ga.square().sum(dim=1)
        + gW.square().sum(dim=(1, 2))
        + gu.square().sum(dim=1)
    )
    torch.testing.assert_close(obs.output, output, rtol=2.0e-13, atol=2.0e-13)
    torch.testing.assert_close(
        obs.kernel, autograd_kernel, rtol=2.0e-13, atol=2.0e-13
    )
    torch.testing.assert_close(
        obs.kernel,
        obs.kernel_a + obs.kernel_W + obs.kernel_u,
        rtol=0.0,
        atol=0.0,
    )


def test_fused_fp32_matches_checked_canonical_implementation():
    state, _, _ = engine._build_state(
        7, 1103, 2, torch.device("cpu"), 3, (4, 7)
    )
    tangent, obs = engine.fused_eval(state, target=1.0)
    canonical_state = canonical_model.State(state.a, state.W, state.u)
    expected_tangent, expected_obs = canonical_model.scaled_rhs(
        canonical_state, "physical", target=1.0
    )
    for actual, expected in (
        (tangent.a, expected_tangent.a),
        (tangent.W, expected_tangent.W),
        (tangent.u, expected_tangent.u),
        (obs.output, expected_obs.output),
        (obs.kernel, expected_obs.kernel),
        (obs.kernel_a, expected_obs.kernel_a),
        (obs.kernel_W, expected_obs.kernel_W),
        (obs.kernel_u, expected_obs.kernel_u),
    ):
        torch.testing.assert_close(
            actual,
            expected,
            rtol=8.0 * torch.finfo(torch.float32).eps,
            atol=8.0 * torch.finfo(torch.float32).eps,
        )


def test_antithetic_initialization_cancels_output_and_preserves_components():
    state, _, _ = engine._build_state(
        13, 909, 1, torch.device("cpu"), 4, (7, 13)
    )
    _, obs = engine.fused_eval(state)
    assert float(obs.output[0] + obs.output[1]) == 0.0
    for values in (obs.kernel_a, obs.kernel_W, obs.kernel_u, obs.kernel):
        assert float(values[0] - values[1]) == 0.0


def test_run_point_retains_distinct_estimands_monitors_and_actual_w_norms():
    heartbeat = []
    arrays, diagnostics = engine.run_point(
        tiny_point(),
        seed=42,
        device=torch.device("cpu"),
        progress_callback=heartbeat.append,
    )
    assert np.array_equal(arrays["w_norm_checkpoint_steps"], [0, 1, 2])
    assert arrays["w_actual_l2_at_checkpoints"].shape == (3, 2)
    assert arrays["state_w_ideal_recurrence_l2"].shape == (3, 2)
    assert len(heartbeat) == 3
    assert diagnostics["target"] == 1.0
    assert diagnostics["initial_mean_output"] == 0.0
    assert diagnostics["initial_antithetic_output_scaled_ulp_defect"] == 0.0
    assert diagnostics["initial_antithetic_component_scaled_ulp_defect"] == 0.0
    assert not np.array_equal(
        arrays["node_mean_physical_loss"], arrays["node_loss_of_mean_output"]
    )
    assert not np.array_equal(
        arrays["node_effective_kernel"], arrays["node_mean_direct_kernel"]
    )
    expected_weighted = (
        (np.float32(1.0) - arrays["raw_output"].astype(np.float32))
        * arrays["raw_kernel"].astype(np.float32)
    ).astype(np.float64)
    np.testing.assert_array_equal(arrays["raw_weighted_kernel"], expected_weighted)


def test_step_cap_is_checked_before_the_disallowed_step():
    with pytest.raises(engine.BudgetStop) as caught:
        engine.run_point(
            tiny_point(max_steps=1), seed=42, device=torch.device("cpu")
        )
    assert caught.value.point_diagnostics["steps"] == 1


def test_target_other_than_one_is_rejected_before_simulation():
    point = tiny_point()
    point["target"] = -1.0
    with pytest.raises(ValueError, match="target=1"):
        engine.run_point(point, seed=42, device=torch.device("cpu"))


def test_runner_forces_deterministic_ieee_fp32_mode():
    mode = run_stage_v_point.configure_ieee_fp32()
    assert mode["float32_matmul_precision"] == "highest"
    assert mode["cuda_matmul_allow_tf32"] is False
    assert mode["cudnn_allow_tf32"] is False
    assert mode["deterministic_algorithms"] is True
    assert mode["cublas_workspace_config"] == ":4096:8"


def test_stage_v_analyzer_accepts_a_synthetic_gate_pass(tmp_path, monkeypatch):
    config = analyze_stage_v.load_json(analyze_stage_v.CONFIG)
    nodes = np.asarray([0.0, 0.5, 0.9, 0.95])
    # Use the exact frozen node and provenance arrays.  The values themselves
    # are synthetic but satisfy all frozen comparisons.
    nodes = np.asarray(config["points"][0]["output_nodes"], dtype=np.float64)
    progress_nodes = nodes[nodes > 0.0]
    prefix_sizes = np.asarray(
        config["points"][0]["prefix_digest_sizes"], dtype=np.int64
    )
    checkpoints = np.asarray(
        config["points"][0]["expected_full_w_checkpoint_steps"], dtype=np.int64
    )
    monitor_size = int(config["points"][0]["w_monitor_sample_size"])
    kernel_curve = 111.0 + 60.0 * nodes**2
    arrays = {
        "initial_state_sha256": np.asarray([b"a" * 64]),
        "initial_prefix_sha256": np.asarray([[b"b" * 64] * 3]),
        "prefix_digest_sizes": prefix_sizes,
        "w_monitor_sha256": np.asarray(b"c" * 64),
        "w_monitor_rows": np.arange(monitor_size, dtype=np.int64) % 2048,
        "w_monitor_cols": np.arange(monitor_size, dtype=np.int64)[::-1] % 2048,
        "w_norm_checkpoint_steps": checkpoints,
        "w_actual_l2_at_checkpoints": np.ones((len(checkpoints), 2)),
        "output_nodes": nodes,
        "node_effective_kernel": kernel_curve,
        "node_mean_direct_kernel": kernel_curve + 0.1,
        "normalized_progress_nodes": progress_nodes,
        "normalized_progress_kernel": np.stack(
            (111.0 + 60.0 * progress_nodes**2,) * 2, axis=1
        ),
        "node_mean_kernel_a": 27.0 + 10.0 * nodes**2,
        "node_mean_kernel_W": 36.0 + 20.0 * nodes**2,
        "node_mean_kernel_u": 48.0 + 30.0 * nodes**2,
        "node_mean_physical_loss": (1.0 - nodes) ** 2 + 1.0e-4,
        "node_loss_of_mean_output": (1.0 - nodes) ** 2,
    }
    diagnostics = {
        "maximum_a_unchanged_fraction_through_y_0_9": 0.01,
        "maximum_u_unchanged_fraction_through_y_0_9": 0.001,
        "maximum_w_sample_unchanged_fraction_through_y_0_9": 0.5,
        "minimum_a_applied_to_ideal_ratio_through_y_0_9": 0.99,
        "maximum_a_applied_to_ideal_ratio_through_y_0_9": 1.01,
        "minimum_u_applied_to_ideal_ratio_through_y_0_9": 0.99,
        "maximum_u_applied_to_ideal_ratio_through_y_0_9": 1.01,
        "minimum_w_sample_applied_to_ideal_ratio_through_y_0_9": 0.9,
        "maximum_w_sample_applied_to_ideal_ratio_through_y_0_9": 1.1,
        "minimum_a_update_cosine_through_y_0_9": 0.9999,
        "minimum_u_update_cosine_through_y_0_9": 0.9999,
        "minimum_w_sample_update_cosine_through_y_0_9": 0.999,
        "driver_max_relative_defect_through_y_0_9": 1.0e-4,
        "driver_relative_rms_defect_through_y_0_9": 1.0e-4,
        "driver_cumulative_relative_defect_through_y_0_9": 1.0e-4,
        "maximum_w_ideal_recurrence_relative_error_through_y_0_9": 1.0e-6,
        "maximum_a_unchanged_fraction_all_time": 0.02,
        "maximum_u_unchanged_fraction_all_time": 0.002,
        "maximum_w_sample_unchanged_fraction_all_time": 0.6,
    }
    lock_path = tmp_path / "LOCK.json"
    lock_path.write_text(__import__("json").dumps({
        "status": "frozen_after_hostile_audit", "files": {}
    }))
    unlock_path = tmp_path / "UNLOCK.json"
    unlock_path.write_text(__import__("json").dumps({
        "status": "authorized_stage_v_only",
        "frozen_manifest_sha256": analyze_stage_v.sha256(lock_path),
        "config_sha256": analyze_stage_v.sha256(analyze_stage_v.CONFIG),
        "run_root": str(tmp_path),
    }))
    monkeypatch.setattr(analyze_stage_v, "LOCK", lock_path)
    monkeypatch.setattr(analyze_stage_v, "UNLOCK", unlock_path)
    authority = {
        "config_sha256": analyze_stage_v.sha256(analyze_stage_v.CONFIG),
        "protocol_sha256": analyze_stage_v.sha256(analyze_stage_v.PROTOCOL),
        "frozen_manifest_sha256": analyze_stage_v.sha256(lock_path),
        "unlock_sha256": analyze_stage_v.sha256(unlock_path),
    }
    for point in config["points"]:
        point_id = point["id"]
        point_dir = tmp_path / point_id
        point_dir.mkdir()
        path = point_dir / "arrays.npz"
        point_arrays = dict(arrays)
        point_checkpoints = np.asarray(
            point["expected_full_w_checkpoint_steps"], dtype=np.int64
        )
        point_arrays["w_norm_checkpoint_steps"] = point_checkpoints
        point_arrays["w_actual_l2_at_checkpoints"] = np.ones(
            (len(point_checkpoints), 2)
        )
        np.savez_compressed(path, **point_arrays)
        point_diagnostics = dict(diagnostics)
        if point_id.endswith("h1e5"):
            for key in tuple(point_diagnostics):
                if key.startswith("driver_"):
                    point_diagnostics[key] = 1.0e-3
        manifest = {
            "status": "complete_validation_valid",
            "point_config": point,
            "scientific_evidence_admissible": False,
            "arrays_file": path.name,
            "arrays_sha256": analyze_stage_v.sha256(path),
            "diagnostics": point_diagnostics,
            **authority,
        }
        (point_dir / "manifest.json").write_text(
            __import__("json").dumps(manifest)
        )
    result = analyze_stage_v.evaluate(tmp_path)
    assert result["stage_v_passed"] is True
    assert result["status"] == "eligible_to_freeze_stage_W"
