from __future__ import annotations

from dataclasses import replace
import json
from pathlib import Path

import numpy as np

from analysis.bootstrap import bootstrap_point
from analysis.pilot_runner import (
    _bundle_hash,
    _difference_interval,
    analyze_pilot,
    interval_overlap,
    paired_step_halving,
    projection_trend,
)
from analysis.reference_data import sha256
from analysis.tests.test_analysis import synthetic_physical_point
from proxy.hierarchy import build_kernel_brackets
from proxy.inventory import evaluate_family


def _configured_point(point_id: str, width: int, *, step: float, pairs: int):
    point = synthetic_physical_point(width=width, pairs=pairs)
    return replace(
        point,
        point_id=point_id,
        config={
            **point.config,
            "seed_base": 1234,
            "step": step,
            "max_time": 1.0,
            "integrator": "rk4",
            "microcanonical_readout": False,
        },
        diagnostics={
            **point.diagnostics,
            "max_projection_relative_norm": 0.1 if width == 256 else 0.06,
        },
    )


def test_paired_step_gate_uses_exact_subset_and_initial_lineages() -> None:
    coarse = _configured_point("coarse", 512, step=2e-4, pairs=12)
    extended = dict(coarse.arrays)
    extended_output = 1.25 * extended["raw_trajectory_output"]
    extended["raw_trajectory_output"] = extended_output
    extended["raw_trajectory_weighted_kernel"] = (
        (1.0 - extended_output) * extended["raw_trajectory_kernel"]
    )
    extended["raw_trajectory_loss"] = np.square(1.0 - extended_output)
    extended["output_nodes"] = np.array([0.0, 0.2, 0.4, 0.99])
    coarse = replace(coarse, arrays=extended)
    arrays = {}
    for key, value in coarse.arrays.items():
        if key.startswith("raw_trajectory_"):
            arrays[key] = value[:, :8]
        elif key.startswith("node_pair_"):
            arrays[key] = value[:, :4]
        elif key.startswith("node_raw_"):
            arrays[key] = value[:, :8]
        else:
            arrays[key] = value
    fine = replace(
        coarse,
        point_id="fine",
        antithetic_pairs=4,
        arrays=arrays,
        config={
            **coarse.config,
            "step": 1e-4,
            "analysis": {
                "paired_coarse_point_id": "coarse",
                "paired_lineage_indices": [0, 1, 2, 3],
            },
        },
    )
    # The fine fixture is the exact first-four-lineage restriction of coarse.
    result = paired_step_halving(
        {"coarse": coarse, "fine": fine},
        {
            "coarse_point_id": "coarse",
            "fine_point_id": "fine",
            "coarse_lineage_indices": [0, 1, 2, 3],
            "maximum_relative_change_through_y_0_95": 1e-12,
            "maximum_relative_change_at_y_0_99": 1e-12,
        },
    )
    assert result["passed"]
    assert result["initial_output_and_kernel_bitwise_equal"]


def test_projection_and_interval_gates_are_fail_closed() -> None:
    low = _configured_point("low", 256, step=2e-4, pairs=8)
    high = _configured_point("high", 512, step=2e-4, pairs=8)
    projection = projection_trend(
        {"low": low, "high": high},
        {
            "point_256": "low",
            "point_512": "high",
            "statistic": "max_projection_relative_norm",
            "maximum_scaled_rate_ratio": 2.0,
        },
    )
    assert projection["passed"]

    left = bootstrap_point(low, replicates=40, seed=10, confidence=0.9)
    right = bootstrap_point(high, replicates=40, seed=11, confidence=0.9)
    assert interval_overlap(left, right)["passed"]
    shifted_band = replace(
        right.band,
        estimate=right.band.estimate * 10.0,
        lower=right.band.lower * 10.0,
        upper=right.band.upper * 10.0,
    )
    assert not interval_overlap(left, replace(right, band=shifted_band))["passed"]


def test_two_width_percentile_trend_uses_declared_attempt_count() -> None:
    low = _configured_point("low", 256, step=2e-4, pairs=8)
    high = _configured_point("high", 512, step=2e-4, pairs=8)

    def metric(point, indices=None):
        values = np.arange(point.antithetic_pairs, dtype=float)
        if indices is not None:
            values = values[indices]
        return float(np.mean(values) / point.width)

    result = _difference_interval(
        low,
        high,
        metric=metric,
        seed=99,
        resamples=80,
        minimum_valid_fraction=0.95,
        lower_quantile=0.005,
        upper_quantile=0.995,
    )
    assert result["attempted_resamples"] == 80
    assert result["valid_resamples"] == 80
    assert result["equal_tail_interval"][0] <= result["equal_tail_interval"][1]


def _synthetic_arrays(mode: str, pairs: int, width: int) -> tuple[dict, dict]:
    nodes = np.array([0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99])
    family = evaluate_family("canonical")
    deepest = build_kernel_brackets(family.baseline, family.moments)[-1]
    kernel = np.array([
        0.5 * (deepest.lower.kernel(float(y)) + deepest.upper.kernel(float(y)))
        for y in nodes
    ])
    trajectories = 2 * pairs
    pair_axis = np.linspace(-1.0, 1.0, pairs)
    pair_axis -= np.mean(pair_axis)
    relative_scale = 2e-4 if width == 256 else 1e-4
    trajectory_scale = np.repeat(1.0 + relative_scale * pair_axis, 2)
    raw_kernel = kernel[:, None] * trajectory_scale[None, :]
    if mode == "physical":
        amplitude = 0.02 if width == 256 else 0.01
        signs = np.tile(np.array([1.0, -1.0]), pairs)
        raw_output = nodes[:, None] + (
            amplitude * (1.0 - nodes[:, None]) * signs[None, :]
        )
        weighted = (1.0 - raw_output) * raw_kernel
        loss = np.square(1.0 - raw_output)
        arrays = {
            "output_nodes": nodes,
            "raw_time": np.linspace(0.0, 0.024, len(nodes)),
            "raw_trajectory_output": raw_output,
            "raw_trajectory_kernel": raw_kernel,
            "raw_trajectory_weighted_kernel": weighted,
            "raw_trajectory_loss": loss,
            "node_pair_output": raw_output.reshape(len(nodes), pairs, 2).mean(2),
            "node_pair_kernel": raw_kernel.reshape(len(nodes), pairs, 2).mean(2),
            "node_pair_weighted_kernel": weighted.reshape(len(nodes), pairs, 2).mean(2),
        }
        diagnostics = {
            "max_abs_initial_output": amplitude,
            "max_abs_antithetic_initial_output_sum": 0.0,
            "minimum_mean_output_increment": 0.01,
            "maximum_mean_loss_increment": -1e-6,
            "maximum_output_variance_at_nodes": amplitude**2,
        }
    else:
        raw_output = np.repeat(nodes[:, None], trajectories, axis=1)
        loss = np.square(1.0 - raw_output)
        arrays = {
            "output_nodes": nodes,
            "raw_output_clock": nodes,
            "raw_trajectory_output": raw_output,
            "raw_trajectory_kernel": raw_kernel,
            "raw_trajectory_loss": loss,
            "node_pair_kernel": raw_kernel.reshape(len(nodes), pairs, 2).mean(2),
        }
        diagnostics = {
            "max_abs_initial_output": 0.0,
            "max_abs_antithetic_initial_output_sum": 0.0,
            "maximum_absolute_output_clock_defect": 0.0,
            "maximum_output_variance_at_nodes": 0.0,
            "max_projection_relative_norm": 0.1 if width == 256 else 0.06,
        }
    return arrays, diagnostics


def test_full_frozen_runner_on_synthetic_hash_bound_run(tmp_path: Path) -> None:
    """Exercise the production schema without opening any scientific NPZ."""

    repository = Path(__file__).resolve().parents[2]
    real_config = repository / "reference/configs/FROZEN_SUCCESSOR_02.json"
    real_analysis = repository / "reference/configs/FROZEN_SUCCESSOR_02_ANALYSIS.json"
    campaign = tmp_path / "campaign"
    reference = campaign / "reference"
    configs = reference / "configs"
    run_dir = reference / "runs" / "synthetic"
    configs.mkdir(parents=True)
    run_dir.mkdir(parents=True)
    config_path = configs / real_config.name
    analysis_path = configs / real_analysis.name
    config_path.write_bytes(real_config.read_bytes())
    analysis_path.write_bytes(real_analysis.read_bytes())
    config = json.loads(config_path.read_text())
    protocol_path = campaign / "SUCCESSOR_02_PROTOCOL.md"
    protocol_path.write_text("synthetic frozen protocol\n")

    records = []
    coarse_n512_arrays = None
    coarse_n512_diagnostics = None
    for point in config["points"]:
        if point["id"] == "canonical_physical_n512_r4_halfstep":
            assert coarse_n512_arrays is not None
            arrays = {}
            for key, value in coarse_n512_arrays.items():
                if key.startswith("raw_trajectory_") or key.startswith("node_raw_"):
                    arrays[key] = value[:, :8]
                elif key.startswith("node_pair_"):
                    arrays[key] = value[:, :4]
                else:
                    arrays[key] = value
            diagnostics = dict(coarse_n512_diagnostics)
        else:
            arrays, diagnostics = _synthetic_arrays(
                str(point["mode"]), int(point["antithetic_pairs"]), int(point["width"])
            )
        if point["id"] == "canonical_physical_n512_r16":
            coarse_n512_arrays = arrays
            coarse_n512_diagnostics = diagnostics
        npz = run_dir / f"{point['id']}.npz"
        np.savez_compressed(npz, **arrays)
        records.append({
            "id": point["id"],
            "status": "complete_scientific_point",
            "scientific_evidence_admissible": True,
            "arrays_file": npz.name,
            "arrays_sha256": sha256(npz),
            "diagnostics": diagnostics,
        })

    source = reference / "synthetic_engine.py"
    source.write_text("# immutable synthetic producer\n")
    source_hashes = {source.name: sha256(source)}
    source_bundle = _bundle_hash(source_hashes)
    summary = {
        "status": "complete_scientific_run",
        "scientific_evidence_admissible": True,
        "config_name": config_path.name,
        "config_sha256": sha256(config_path),
        "source_sha256": source_hashes,
        "source_bundle_sha256": source_bundle,
        "points": records,
    }
    summary_path = run_dir / "summary.json"
    summary_path.write_text(json.dumps(summary))
    unlock = {
        "status": "protocol_frozen_and_execution_authorized",
        "config_name": config_path.name,
        "config_sha256": sha256(config_path),
        "protocol_name": protocol_path.name,
        "protocol_sha256": sha256(protocol_path),
        "analysis_config_name": analysis_path.name,
        "analysis_config_sha256": sha256(analysis_path),
        "source_bundle_sha256": source_bundle,
    }
    (reference / "PRODUCTION_UNLOCK.json").write_text(json.dumps(unlock))

    result = analyze_pilot(summary_path, config_path, analysis_path)
    assert result["status"] == "complete_offline_analysis"
    # With the literal frozen schema, y=0 is in every containment test even
    # though every rational bracket collapses to the point K(0)=111 there.
    # A nondegenerate honest band therefore remains inconclusive, never a
    # false compatibility claim.  The independent Stage-2 resolution branch
    # is nevertheless authorized when every validity gate passes.
    assert result["protocol_result"] == "inconclusive"
    assert result["stage3_branch_authorized"]
    assert all(result["validity_gates"].values())
    assert all(
        value["band"]["attempted_replicates"] == 2000
        for value in result["point_bootstraps"].values()
    )
