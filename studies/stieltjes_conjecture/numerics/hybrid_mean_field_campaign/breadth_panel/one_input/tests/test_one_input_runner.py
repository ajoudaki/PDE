from __future__ import annotations

from pathlib import Path
import hashlib
import json
import sys

import numpy as np
import pytest
import torch


HERE = Path(__file__).resolve().parents[1]
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import one_input_runner as runner  # noqa: E402
import run_one_input_point as cli  # noqa: E402


def small_point(configuration: str, step: float = 1e-5) -> dict:
    return {
        "key": "cpu-test",
        "purpose": "unit_test",
        "configuration": configuration,
        "width": 7,
        "step": step,
        "max_time": 4 * step,
        "lineage_start": 0,
        "lineage_stop": 1,
        "prefix_sizes": [5, 7],
        "rng_row_block": 4,
        "w_monitor_size": 16,
        "w_monitor_extent": 7,
        "w_monitor_seed": 1234,
        "diagnostic_stride": 2,
        "wall_sync_stride": 2,
        "caps": {
            "wall_seconds": 10,
            "max_steps_all_lineages": 4,
            "gpu_memory_gib": 1,
            "host_rss_gib": 4,
            "kernel_ceiling": 1e9,
            "state_ceiling": 1e6,
        },
    }


@pytest.mark.parametrize(
    "configuration",
    ("canonical", "centered_c1", "relative_metric_l2", "variance_vhalf"),
)
def test_small_cpu_euler_run_is_finite_and_driver_consistent(configuration):
    point = small_point(configuration)
    arrays, diagnostics = runner.run_point(
        point, seed=202608141, device=torch.device("cpu")
    )
    assert arrays["raw_output"].shape == (5, 2)
    assert arrays["raw_q2"].shape == (5, 2)
    assert arrays["column_lineage_id"].tolist() == [0, 0]
    assert arrays["antithetic_sign"].tolist() == [1, -1]
    assert np.all(np.isfinite(arrays["raw_kernel"]))
    assert diagnostics["steps"] == 4
    assert diagnostics["lineages"][0][
        "driver_max_relative_defect_through_y_0_95"
    ] < 0.02
    assert np.min(np.diff(arrays["raw_output"].mean(axis=1))) >= -1e-6
    assert np.max(np.diff(arrays["raw_loss"].mean(axis=1))) <= 1e-6


def test_variance_proxy_arrays_use_the_exact_coordinate_map():
    arrays, _ = runner.run_point(
        small_point("variance_vhalf"),
        seed=202608142,
        device=torch.device("cpu"),
    )
    np.testing.assert_array_equal(arrays["proxy_output"], 2.0 * arrays["raw_output"])
    np.testing.assert_array_equal(arrays["proxy_kernel"], 2.0 * arrays["raw_kernel"])
    np.testing.assert_array_equal(
        arrays["proxy_weighted_kernel"], 4.0 * arrays["raw_weighted_kernel"]
    )
    np.testing.assert_array_equal(arrays["proxy_q2"], 2.0 * arrays["raw_q2"])


def test_exact_step_cap_is_not_misclassified_as_an_overrun():
    _, diagnostics = runner.run_point(
        small_point("canonical"), seed=202608143, device=torch.device("cpu")
    )
    assert diagnostics["steps"] == 4


def test_malformed_step_budget_is_rejected_before_execution():
    point = small_point("canonical")
    point["lineage_stop"] = 2
    with pytest.raises(ValueError, match="step cap"):
        runner.run_point(point, seed=202608144, device=torch.device("cpu"))


def test_fractional_integer_field_is_not_silently_coerced():
    point = small_point("canonical")
    point["width"] = 7.5
    with pytest.raises(ValueError, match="JSON integers"):
        runner.validate_point(point)


def test_lock_bundle_and_one_attempt_ledger_are_fail_closed(tmp_path, monkeypatch):
    monkeypatch.setattr(cli, "REQUIRED_LOCK_PATHS", {"source.py"})
    monkeypatch.setattr(cli, "BREADTH_ROOT", tmp_path)
    source = tmp_path / "source.py"
    source.write_text("x = 1\n", encoding="utf-8")
    config = tmp_path / "FROZEN_ONE_INPUT_POINTS.json"
    point = small_point("canonical")
    config.write_text(json.dumps({"points": [point]}), encoding="utf-8")
    source_hash = cli.sha256(source)
    bundle = hashlib.sha256()
    bundle.update(b"source.py\0" + source_hash.encode("ascii") + b"\n")
    lock = tmp_path / "LOCK.json"
    lock.write_text(
        json.dumps(
            {
                "status": "frozen",
                "sha256": {"source.py": source_hash},
                "bundle_sha256": bundle.hexdigest(),
                "config_sha256": cli.sha256(config),
            }
        ),
        encoding="utf-8",
    )
    assert cli.verify_lock(lock, config)["bundle_sha256"] == bundle.hexdigest()

    output_root = tmp_path / "runs"
    unlock = {
        "status": "execution-authorized-once",
        "lock_sha256": cli.sha256(lock),
        "config_sha256": cli.sha256(config),
        "output_root": "runs",
        "allowed_points": {point["key"]: "cuda:0"},
        "allowed_gpu_names": ["test GPU"],
        "point_groups": {point["key"]: "canonical"},
        "cumulative_wall_seconds": 20,
        "per_group_wall_seconds": 20,
    }
    unlock_path = tmp_path / "UNLOCK.json"
    unlock_path.write_text(json.dumps(unlock), encoding="utf-8")
    loaded, root = cli.verify_unlock(
        unlock_path,
        lock,
        config,
        point,
        "cuda:0",
        output_root / point["key"],
    )
    ledger = cli.reserve_attempt(root, loaded, point, "cuda:0")
    assert json.loads(ledger.read_text())["attempts"][point["key"]]["status"] == "reserved"
    with pytest.raises(RuntimeError, match="already consumed"):
        cli.reserve_attempt(root, loaded, point, "cuda:0")


def test_invalid_bundle_digest_is_rejected(tmp_path, monkeypatch):
    monkeypatch.setattr(cli, "REQUIRED_LOCK_PATHS", {"source.py"})
    monkeypatch.setattr(cli, "BREADTH_ROOT", tmp_path)
    source = tmp_path / "source.py"
    source.write_text("x = 1\n", encoding="utf-8")
    config = tmp_path / "FROZEN_ONE_INPUT_POINTS.json"
    config.write_text("{}", encoding="utf-8")
    lock = tmp_path / "LOCK.json"
    lock.write_text(
        json.dumps(
            {
                "status": "frozen",
                "sha256": {"source.py": cli.sha256(source)},
                "bundle_sha256": "0" * 64,
                "config_sha256": cli.sha256(config),
            }
        ),
        encoding="utf-8",
    )
    with pytest.raises(RuntimeError, match="bundle digest"):
        cli.verify_lock(lock, config)


def test_every_required_lock_path_is_mandatory():
    complete = {path: "0" * 64 for path in cli.REQUIRED_LOCK_PATHS}
    cli.require_lock_paths(complete)
    for omitted in cli.REQUIRED_LOCK_PATHS:
        reduced = dict(complete)
        del reduced[omitted]
        with pytest.raises(RuntimeError, match="omits required paths"):
            cli.require_lock_paths(reduced)
