from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
import pytest
import torch


HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

import nested_rng  # noqa: E402
import run_width_point  # noqa: E402
import width_analysis as analysis  # noqa: E402
import width_engine as engine  # noqa: E402


def synthetic_dataset(width: int, *, lineages: int = 16, steps: int = 121):
    time = np.linspace(0.0, 0.024, steps)
    ids = np.arange(lineages, dtype=np.int64)
    output = np.empty((steps, 2 * lineages), dtype=np.float64)
    kernel = np.empty_like(output)
    rng = np.random.default_rng(202608190000 + width)
    initial_components = np.empty((lineages, 3), dtype=np.float64)
    exact_components = nested_rng.exact_initial_component_means(width)
    for lineage in range(lineages):
        f0 = 0.004 * rng.normal()
        rate = 250.0 + 8.0 * rng.normal()
        progress = 1.0 - np.exp(-rate * time)
        base_kernel = 150.0 + 0.001 * width + 2.0 * rng.normal()
        for branch, sign in enumerate((1.0, -1.0)):
            column = 2 * lineage + branch
            branch_f0 = sign * f0
            output[:, column] = branch_f0 + (1.0 - branch_f0) * progress
            kernel[:, column] = base_kernel + 15.0 * progress + sign * 0.2
        controls = rng.normal(size=3)
        initial_components[lineage] = exact_components + controls
    weighted = (1.0 - output) * kernel
    loss = (1.0 - output) ** 2
    return {
        "raw_time": time,
        "raw_output": output,
        "raw_kernel": kernel,
        "raw_weighted_kernel": weighted,
        "raw_loss": loss,
        "raw_q1": np.ones_like(output),
        "raw_q2": np.ones_like(output),
        "lineage_ids": ids,
        "initial_components": initial_components,
        "initial_total": initial_components.sum(axis=1),
        "initial_state_sha256": np.asarray(
            [f"{width:08x}{lineage:056x}".encode() for lineage in ids], dtype="S64"
        ),
        "output_nodes": np.r_[0.0, analysis.POSITIVE_NODES],
    }


def test_coordinate_rng_is_exactly_nested_and_digest_is_batch_independent():
    small_a = nested_rng.vector_normal(7, seed=91, lineage=3, domain="a")
    large_a = nested_rng.vector_normal(11, seed=91, lineage=3, domain="a")
    assert np.array_equal(small_a, large_a[:7])
    small_W = nested_rng.matrix_normal(7, seed=91, lineage=3, row_block=2)
    large_W = nested_rng.matrix_normal(11, seed=91, lineage=3, row_block=5)
    assert np.array_equal(small_W, large_W[:7, :7])

    state1, digest1 = nested_rng.generate_nested_antithetic_state(
        7,
        [3],
        91,
        device=torch.device("cpu"),
        return_digests=True,
        row_block=2,
    )
    state2, digest2 = nested_rng.generate_nested_antithetic_state(
        7,
        [3],
        91,
        device=torch.device("cpu"),
        return_digests=True,
        row_block=5,
    )
    assert np.array_equal(digest1, digest2)
    torch.testing.assert_close(state1.a, state2.a, rtol=0.0, atol=0.0)
    torch.testing.assert_close(state1.W, state2.W, rtol=0.0, atol=0.0)
    torch.testing.assert_close(state1.u, state2.u, rtol=0.0, atol=0.0)


def test_counter_normal_has_calibrated_low_moments():
    sample = nested_rng.normal_from_counters(
        np.arange(300_000, dtype=np.uint64), seed=731, lineage=11, domain="W"
    )
    assert abs(float(sample.mean())) < 0.008
    assert abs(float(np.mean(sample**2)) - 1.0) < 0.012
    assert abs(float(np.mean(sample**3))) < 0.04
    assert abs(float(np.mean(sample**4)) - 3.0) < 0.08


def test_exact_finite_n_initialization_means_follow_wick_algebra():
    # E u^2=1, E u^4=3, E u^6=15, E u^8=105.
    for n in (1, 7, 2048):
        e_s4_squared_over_n2 = (n * 105 + n * (n - 1) * 9) / n**2
        kernel_a = 3 * e_s4_squared_over_n2
        kernel_W = 4 * e_s4_squared_over_n2
        # For one row/column:
        # E[u_1^2 W_1^2 z^2] = [3 E u^6 +(n-1)E u^2 E u^4]/n.
        kernel_u = 16 * (3 * 15 + (n - 1) * 3) / n
        expected = np.array([kernel_a, kernel_W, kernel_u])
        np.testing.assert_allclose(
            nested_rng.exact_initial_component_means(n), expected, rtol=0, atol=2e-14
        )
        assert nested_rng.exact_initial_total_mean(n) == pytest.approx(
            float(expected.sum()), rel=0, abs=3e-13
        )


def test_fused_eval_matches_checked_canonical_rhs_and_observables():
    state = nested_rng.generate_nested_antithetic_state(
        5, [0, 1], 202608190101, device=torch.device("cpu")
    )
    fused_rhs, fused_obs = engine.fused_physical_eval(state, target=1.0)
    canonical_rhs, canonical_obs = engine.canonical_model.scaled_rhs(
        state, "physical", target=1.0
    )
    for actual, expected in (
        (fused_rhs.a, canonical_rhs.a),
        (fused_rhs.W, canonical_rhs.W),
        (fused_rhs.u, canonical_rhs.u),
        (fused_obs.output, canonical_obs.output),
        (fused_obs.kernel, canonical_obs.kernel),
        (fused_obs.kernel_a, canonical_obs.kernel_a),
        (fused_obs.kernel_W, canonical_obs.kernel_W),
        (fused_obs.kernel_u, canonical_obs.kernel_u),
    ):
        torch.testing.assert_close(actual, expected, rtol=8e-15, atol=8e-15)


def test_canonical_analytic_gradient_and_kernel_match_autograd():
    state = nested_rng.generate_nested_antithetic_state(
        4, [0, 1], 202608190102, device=torch.device("cpu")
    )
    a = state.a.clone().requires_grad_(True)
    W = state.W.clone().requires_grad_(True)
    u = state.u.clone().requires_grad_(True)
    autograd_state = engine.canonical_model.State(a, W, u)
    outputs = engine.canonical_model.output(autograd_state)
    ga, gW, gu = torch.autograd.grad(outputs.sum(), (a, W, u))
    analytic = engine.canonical_model.feature_rhs(state)
    n = state.width
    torch.testing.assert_close(analytic.a, n * ga, rtol=1e-12, atol=1e-12)
    torch.testing.assert_close(analytic.W, n * gW, rtol=1e-12, atol=1e-12)
    torch.testing.assert_close(analytic.u, n * gu, rtol=1e-12, atol=1e-12)


def test_physical_estimands_use_mean_reinversion_and_normalized_path_progress():
    data = synthetic_dataset(2048)
    nodes = np.array([0.1, 0.5, 0.9])
    effective = analysis.lineage_outcomes(data, nodes, estimand="effective")
    progress = analysis.lineage_outcomes(data, nodes, estimand="progress")
    assert effective.shape == (16, 3)
    assert progress.shape == (16, 3)
    assert np.all(effective > 0)
    assert np.all(progress > 0)

    # A repeated-lineage resample changes the ensemble clock, hence the primary
    # outcomes; the pathwise progress cache only selects rows.
    indices = np.array([0] * 8 + [1] * 8)
    effective_resampled = analysis.lineage_outcomes(
        data, nodes, estimand="effective", indices=indices
    )
    progress_resampled = analysis.lineage_outcomes(
        data, nodes, estimand="progress", indices=indices
    )
    assert not np.allclose(effective_resampled[:8], effective[[0] * 8])
    np.testing.assert_allclose(progress_resampled, progress[indices])


def test_crossfit_is_refit_inside_bootstrap_resample():
    data = synthetic_dataset(2048)
    nodes = np.array([0.5, 0.9])
    original = analysis.estimate(
        data, 2048, nodes, estimand="effective", control="scalar"
    )
    indices, folds = analysis.stratified_bootstrap_indices(
        data["lineage_ids"], 1, 123
    )
    resampled = analysis.estimate(
        data,
        2048,
        nodes,
        estimand="effective",
        control="scalar",
        indices=indices[0],
        fold_labels=folds[0],
    )
    assert not np.array_equal(original.betas, resampled.betas)


def test_shard_merge_preserves_adjacent_pairs_and_lineage_order():
    full = synthetic_dataset(8192)

    def subset(which):
        columns = analysis._pair_columns(which).reshape(-1)
        result = {}
        for key, value in full.items():
            if key.startswith("raw_") and value.ndim == 2:
                result[key] = value[:, columns]
            elif key in {
                "lineage_ids",
                "initial_components",
                "initial_total",
                "initial_state_sha256",
            }:
                result[key] = value[which]
            else:
                result[key] = value
        return result

    merged = analysis.merge_shards([subset(np.arange(8, 16)), subset(np.arange(0, 8))])
    for key in (
        "lineage_ids",
        "raw_output",
        "raw_kernel",
        "raw_weighted_kernel",
        "initial_components",
        "initial_total",
        "initial_state_sha256",
    ):
        assert np.array_equal(merged[key], full[key])


def test_validation_runner_is_permanently_non_scientific(tmp_path):
    config_path = HERE / "configs/VALIDATION_CPU.json"
    config = json.loads(config_path.read_text())
    point = config["points"][0]
    arrays, diagnostics = engine.run_point(
        point, seed=config["seed"], device=torch.device("cpu")
    )
    assert diagnostics["lineage_count"] == 4
    assert arrays["initial_state_sha256"].shape == (4,)
    assert config["purpose"] == "validation_only_never_scientific"


def test_production_runner_fails_closed_without_source_lock_or_unlock(tmp_path):
    config_path = HERE / "configs/FROZEN_WIDTH_LADDER.json"
    with pytest.raises(RuntimeError):
        run_width_point.validate_unlock(
            None,
            lock_sha256="0" * 64,
            config_sha256=engine.sha256_file(config_path),
            point_id="n2048_r16",
            run_root=tmp_path,
        )
