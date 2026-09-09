#!/usr/bin/env python3
"""Apply the frozen Stage-V gates to the two completed validation points."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import numpy as np


HERE = Path(__file__).resolve().parent
CONFIG = HERE / "configs" / "FROZEN_STAGE_V.json"
PROTOCOL = HERE / "PROTOCOL.md"
LOCK = HERE / "FROZEN_STAGE_V_MANIFEST.json"
UNLOCK = HERE / "STAGE_V_UNLOCK.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_authority(run_root: Path) -> dict[str, str]:
    lock = load_json(LOCK)
    if lock.get("status") != "frozen_after_hostile_audit":
        raise RuntimeError("Stage-V source lock is not hostile-audit frozen")
    for relative, expected in lock.get("files", {}).items():
        path = HERE / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(f"locked source mismatch: {relative}")
    lock_sha = sha256(LOCK)
    unlock = load_json(UNLOCK)
    if unlock.get("status") != "authorized_stage_v_only":
        raise RuntimeError("Stage-V unlock is absent or invalid")
    if unlock.get("frozen_manifest_sha256") != lock_sha:
        raise RuntimeError("unlock does not bind the source lock")
    if unlock.get("config_sha256") != sha256(CONFIG):
        raise RuntimeError("unlock does not bind the config")
    if (HERE / unlock.get("run_root", "")).resolve() != run_root.resolve():
        raise RuntimeError("unlock does not bind this run root")
    return {
        "config_sha256": sha256(CONFIG),
        "protocol_sha256": sha256(PROTOCOL),
        "frozen_manifest_sha256": lock_sha,
        "unlock_sha256": sha256(UNLOCK),
    }


def load_point(
    run_root: Path,
    point: dict[str, Any],
    authority: dict[str, str],
) -> tuple[dict, dict[str, np.ndarray], str]:
    point_id = str(point["id"])
    point_dir = run_root / point_id
    manifest_path = point_dir / "manifest.json"
    manifest = load_json(manifest_path)
    if manifest.get("status") != "complete_validation_valid":
        raise RuntimeError(f"{point_id} is not a completed validation point")
    for key, expected in authority.items():
        if manifest.get(key) != expected:
            raise RuntimeError(f"{point_id} manifest authority mismatch: {key}")
    if manifest.get("point_config") != point:
        raise RuntimeError(f"{point_id} manifest point config mismatch")
    if manifest.get("scientific_evidence_admissible") is not False:
        raise RuntimeError(f"{point_id} is incorrectly labeled scientific evidence")
    arrays_path = point_dir / str(manifest["arrays_file"])
    arrays_sha = sha256(arrays_path)
    if arrays_sha != manifest["arrays_sha256"]:
        raise RuntimeError(f"{point_id} arrays hash mismatch")
    arrays = {key: value for key, value in np.load(arrays_path).items()}
    expected_nodes = np.asarray(point["output_nodes"], dtype=np.float64)
    expected_positive = expected_nodes[expected_nodes > 0.0]
    expected_prefix = np.asarray(point["prefix_digest_sizes"], dtype=np.int64)
    expected_checkpoints = np.asarray(
        point["expected_full_w_checkpoint_steps"], dtype=np.int64
    )
    for name, actual, expected in (
        ("output nodes", arrays["output_nodes"], expected_nodes),
        ("progress nodes", arrays["normalized_progress_nodes"], expected_positive),
        ("prefix sizes", arrays["prefix_digest_sizes"], expected_prefix),
        ("full-W checkpoints", arrays["w_norm_checkpoint_steps"], expected_checkpoints),
    ):
        if not np.array_equal(actual, expected):
            raise RuntimeError(f"{point_id} {name} mismatch")
    if arrays["w_monitor_rows"].size != int(point["w_monitor_sample_size"]):
        raise RuntimeError(f"{point_id} W-monitor size mismatch")
    if arrays["w_monitor_cols"].shape != arrays["w_monitor_rows"].shape:
        raise RuntimeError(f"{point_id} W-monitor coordinate shape mismatch")
    if arrays["w_actual_l2_at_checkpoints"].shape[0] != len(expected_checkpoints):
        raise RuntimeError(f"{point_id} full-W norm table mismatch")
    return manifest, arrays, arrays_sha


def max_relative(a: np.ndarray, b: np.ndarray) -> float:
    # Frozen symmetric relative difference: neither step is privileged in the
    # denominator.  This is stricter than dividing by max(|a|,|b|).
    scale = np.maximum(0.5 * (np.abs(a) + np.abs(b)), 1e-12)
    return float(np.max(np.abs(a - b) / scale))


def evaluate(run_root: Path) -> dict[str, Any]:
    config = load_json(CONFIG)
    authority = validate_authority(run_root)
    gates = config["decision_gates"]
    coarse_point, fine_point = config["points"]
    coarse_id, fine_id = coarse_point["id"], fine_point["id"]
    coarse_manifest, coarse, coarse_arrays_sha = load_point(
        run_root, coarse_point, authority
    )
    fine_manifest, fine, fine_arrays_sha = load_point(
        run_root, fine_point, authority
    )
    dc, df = coarse_manifest["diagnostics"], fine_manifest["diagnostics"]

    checks: dict[str, dict[str, Any]] = {}

    def check(name: str, value: float | bool, relation: str, threshold: float | None = None):
        if relation == "bool":
            passed = bool(value)
        elif relation == "le":
            passed = float(value) <= float(threshold)
        elif relation == "ge":
            passed = float(value) >= float(threshold)
        else:
            raise ValueError(relation)
        checks[name] = {"value": value, "relation": relation,
                        "threshold": threshold, "passed": passed}

    check(
        "identical_full_state_digest",
        bool(np.array_equal(coarse["initial_state_sha256"], fine["initial_state_sha256"])),
        "bool",
    )
    check(
        "identical_prefix_digests",
        bool(np.array_equal(coarse["initial_prefix_sha256"], fine["initial_prefix_sha256"])),
        "bool",
    )
    check(
        "identical_monitor",
        bool(
            np.array_equal(coarse["w_monitor_sha256"], fine["w_monitor_sha256"])
            and np.array_equal(coarse["w_monitor_rows"], fine["w_monitor_rows"])
            and np.array_equal(coarse["w_monitor_cols"], fine["w_monitor_cols"])
        ),
        "bool",
    )
    nodes = fine["output_nodes"]
    through = nodes <= 0.9
    eff = max_relative(
        coarse["node_effective_kernel"][through],
        fine["node_effective_kernel"][through],
    )
    check("effective_kernel_coarse_fine", eff, "le",
          gates["max_relative_effective_and_progress_difference_through_y_0_9"])
    progress_nodes = fine["normalized_progress_nodes"]
    progress_through = progress_nodes <= 0.9
    progress = max_relative(
        coarse["normalized_progress_kernel"][progress_through],
        fine["normalized_progress_kernel"][progress_through],
    )
    check("progress_kernel_coarse_fine", progress, "le",
          gates["max_relative_effective_and_progress_difference_through_y_0_9"])
    for suffix in ("a", "W", "u"):
        value = max_relative(
            coarse[f"node_mean_kernel_{suffix}"][through],
            fine[f"node_mean_kernel_{suffix}"][through],
        )
        check(f"component_{suffix}_coarse_fine", value, "le",
              gates["max_relative_component_difference_through_y_0_9"])

    for field, threshold_key in (
        ("maximum_a_unchanged_fraction_through_y_0_9", "max_a_unchanged_fraction"),
        ("maximum_u_unchanged_fraction_through_y_0_9", "max_u_unchanged_fraction"),
        ("maximum_w_sample_unchanged_fraction_through_y_0_9", "max_w_sample_unchanged_fraction"),
    ):
        check(field, df[field], "le", gates[threshold_key])
    for prefix in ("a", "u"):
        check(f"{prefix}_norm_ratio_min", df[f"minimum_{prefix}_applied_to_ideal_ratio_through_y_0_9"],
              "ge", gates["a_u_norm_ratio_min"])
        check(f"{prefix}_norm_ratio_max", df[f"maximum_{prefix}_applied_to_ideal_ratio_through_y_0_9"],
              "le", gates["a_u_norm_ratio_max"])
        check(f"{prefix}_cosine_min", df[f"minimum_{prefix}_update_cosine_through_y_0_9"],
              "ge", gates["a_u_min_cosine"])
    check("W_norm_ratio_min", df["minimum_w_sample_applied_to_ideal_ratio_through_y_0_9"],
          "ge", gates["w_sample_norm_ratio_min"])
    check("W_norm_ratio_max", df["maximum_w_sample_applied_to_ideal_ratio_through_y_0_9"],
          "le", gates["w_sample_norm_ratio_max"])
    check("W_cosine_min", df["minimum_w_sample_update_cosine_through_y_0_9"],
          "ge", gates["w_sample_min_cosine"])

    driver_fields = (
        ("driver_max_relative_defect_through_y_0_9", "driver_max_relative"),
        ("driver_relative_rms_defect_through_y_0_9", "driver_relative_rms"),
        ("driver_cumulative_relative_defect_through_y_0_9", "driver_cumulative_relative"),
    )
    for field, threshold_key in driver_fields:
        check(f"fine_{field}", df[field], "le", gates[threshold_key])
        improvement_bound = (
            gates["fine_vs_coarse_factor"] * dc[field]
            + gates["fine_vs_coarse_absolute_slack"]
        )
        check(f"fine_improves_{field}", df[field], "le", improvement_bound)

    passed = all(item["passed"] for item in checks.values())
    return {
        "schema_version": 1,
        "status": "eligible_to_freeze_stage_W" if passed else "Euler_FP32_h5_invalid_or_inconclusive",
        "stage_v_passed": passed,
        "scientific_evidence_admissible": False,
        **authority,
        "point_manifests": {
            coarse_id: sha256(run_root / coarse_id / "manifest.json"),
            fine_id: sha256(run_root / fine_id / "manifest.json"),
        },
        "point_arrays": {
            coarse_id: coarse_arrays_sha,
            fine_id: fine_arrays_sha,
        },
        "checks": checks,
        "descriptive": {
            "exact_finite_width_mean_initial_kernel": 111.0 + 1344.0 / 8192.0,
            "fine_all_time_unchanged": {
                key: value for key, value in df.items()
                if key.endswith("_unchanged_fraction_all_time")
            },
            "fine_maximum_w_ideal_recurrence_relative_error_through_y_0_9":
                df["maximum_w_ideal_recurrence_relative_error_through_y_0_9"],
            "node_tables": {
                point_id: {
                    "output_nodes": arrays["output_nodes"].tolist(),
                    "effective_kernel": arrays["node_effective_kernel"].tolist(),
                    "direct_kernel": arrays["node_mean_direct_kernel"].tolist(),
                    "kernel_a": arrays["node_mean_kernel_a"].tolist(),
                    "kernel_W": arrays["node_mean_kernel_W"].tolist(),
                    "kernel_u": arrays["node_mean_kernel_u"].tolist(),
                    "mean_physical_loss": arrays["node_mean_physical_loss"].tolist(),
                    "loss_of_mean_output": arrays["node_loss_of_mean_output"].tolist(),
                }
                for point_id, arrays in ((coarse_id, coarse), (fine_id, fine))
            },
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise RuntimeError(f"refusing to overwrite {args.output}")
    result = evaluate(args.run_root)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"],
                      "stage_v_passed": result["stage_v_passed"]}, sort_keys=True))
    return 0 if result["stage_v_passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
