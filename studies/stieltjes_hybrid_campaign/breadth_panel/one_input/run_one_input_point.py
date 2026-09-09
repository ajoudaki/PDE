#!/usr/bin/env python3
"""Fail-closed CLI for one frozen one-input breadth point."""

from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time
import traceback


os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
os.environ["NVIDIA_TF32_OVERRIDE"] = "0"

import numpy as np  # noqa: E402
import torch  # noqa: E402

import one_input_runner as runner  # noqa: E402


BREADTH_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_LOCK_PATHS = {
    "PROTOCOL.md",
    "proxy_contract.py",
    "FROZEN_ONE_INPUT_POINTS.json",
    "one_input/one_input_engine.py",
    "one_input/one_input_runner.py",
    "one_input/run_one_input_point.py",
    "one_input/run_capped_one_input.sh",
    "one_input/tests/test_one_input_engine.py",
    "one_input/tests/test_one_input_runner.py",
    "tests/test_proxy_contract.py",
    "../width_ladder/euler_fp32/nested_init.py",
    "../width_ladder/euler_fp32/euler_engine.py",
    "../../global_proxy_campaign/proxy/inventory.py",
    "../../global_proxy_campaign/proxy/hierarchy.py",
    "../../global_proxy_campaign/proxy/exact_series.py",
    "../../../theory/certificates_order11.json",
    "../../../theory/sector_total_nonnegativity.py",
    "../../../theory/finite_variance_hankel_audit.py",
    "../../../theory/variance_homotopy_boundary_audit.py",
    "../../../../mean_field_peeling/quadratic_compiler/campaign1/results_order9_q2_order8.json",
    "../../../../mean_field_peeling/quadratic_compiler/campaign1/hankel_certificates_order9_q2_order8.json",
    "../../../../mean_field_peeling/quadratic_compiler/campaign2/certificates_order7.json",
    "../../../../mean_field_peeling/quadratic_compiler/campaign3/certificates_order7.json",
}


class ExternalTermination(RuntimeError):
    pass


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_lock_paths(entries: dict[str, str]) -> None:
    missing = REQUIRED_LOCK_PATHS - set(entries)
    if missing:
        raise RuntimeError(f"source lock omits required paths: {sorted(missing)}")


def write_json(path: Path, value: object) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    temporary.replace(path)


def verify_lock(lock_path: Path, config_path: Path) -> dict:
    if lock_path.parent.resolve() != BREADTH_ROOT:
        raise RuntimeError("source lock is not in the live breadth-panel root")
    if config_path.resolve() != BREADTH_ROOT / "FROZEN_ONE_INPUT_POINTS.json":
        raise RuntimeError("configuration is not the live frozen one-input file")
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    if lock.get("status") != "frozen":
        raise RuntimeError("source lock is not frozen")
    require_lock_paths(lock.get("sha256", {}))
    root = lock_path.parent
    for relative, expected in lock["sha256"].items():
        path = root / relative
        if not path.is_file() or sha256(path) != expected:
            raise RuntimeError(f"source-lock mismatch for {relative}")
    expected_config = lock["config_sha256"]
    if sha256(config_path) != expected_config:
        raise RuntimeError("configuration hash differs from source lock")
    bundle = hashlib.sha256()
    for relative, expected in sorted(lock["sha256"].items()):
        bundle.update(relative.encode("utf-8") + b"\0" + expected.encode("ascii") + b"\n")
    if bundle.hexdigest() != lock["bundle_sha256"]:
        raise RuntimeError("source bundle digest is not implied by the locked table")
    return lock


def verify_unlock(
    unlock_path: Path,
    lock_path: Path,
    config_path: Path,
    point: dict,
    device_name: str,
    output: Path,
) -> tuple[dict, Path]:
    unlock = json.loads(unlock_path.read_text(encoding="utf-8"))
    if unlock.get("status") != "execution-authorized-once":
        raise RuntimeError("execution unlock is not active")
    if unlock["lock_sha256"] != sha256(lock_path):
        raise RuntimeError("unlock does not bind the source lock")
    if unlock["config_sha256"] != sha256(config_path):
        raise RuntimeError("unlock does not bind the point config")
    if unlock["allowed_points"].get(point["key"]) != device_name:
        raise RuntimeError("point/device pair is not authorized")
    root = (unlock_path.parent / unlock["output_root"]).resolve()
    expected = root / point["key"]
    if output.resolve() != expected:
        raise RuntimeError("output directory differs from the authorized path")
    return unlock, root


def reserve_attempt(
    root: Path,
    unlock: dict,
    point: dict,
    device_name: str,
) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    lock_path = root / ".attempts.lock"
    ledger_path = root / "ATTEMPTS.json"
    with lock_path.open("a+", encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        ledger = (
            json.loads(ledger_path.read_text(encoding="utf-8"))
            if ledger_path.exists()
            else {"schema": "breadth-attempt-ledger-v1", "attempts": {}}
        )
        if point["key"] in ledger["attempts"]:
            raise RuntimeError("point already consumed its one attempt")
        declared = float(point["caps"]["wall_seconds"])
        total = sum(float(value["declared_wall_seconds"]) for value in ledger["attempts"].values())
        if total + declared > float(unlock["cumulative_wall_seconds"]):
            raise RuntimeError("cumulative validation wall budget would be exceeded")
        group = unlock["point_groups"][point["key"]]
        group_total = sum(
            float(value["declared_wall_seconds"])
            for value in ledger["attempts"].values()
            if value["group"] == group
        )
        if group_total + declared > float(unlock["per_group_wall_seconds"]):
            raise RuntimeError("per-configuration validation budget would be exceeded")
        ledger["attempts"][point["key"]] = {
            "status": "reserved",
            "group": group,
            "device": device_name,
            "declared_wall_seconds": declared,
            "reserved_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        }
        write_json(ledger_path, ledger)
        fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
    return ledger_path


def finalize_attempt(ledger_path: Path, point_key: str, status: str) -> None:
    lock_path = ledger_path.parent / ".attempts.lock"
    with lock_path.open("a+", encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        ledger["attempts"][point_key].update(
            status=status,
            ended_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
        )
        write_json(ledger_path, ledger)
        fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def configure_determinism(device: torch.device) -> None:
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    if device.type == "cuda":
        torch.cuda.set_device(device)


def parse_cuda(name: str) -> torch.device:
    device = torch.device(name)
    if device.type != "cuda" or not torch.cuda.is_available():
        raise RuntimeError("scientific breadth points require CUDA")
    index = 0 if device.index is None else int(device.index)
    if index < 0 or index >= torch.cuda.device_count():
        raise RuntimeError("CUDA device index is unavailable")
    torch.cuda.set_device(index)
    torch.empty(1, dtype=torch.float32, device=device)
    torch.cuda.synchronize(device)
    return device


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--lock", type=Path, required=True)
    parser.add_argument("--unlock", type=Path, required=True)
    parser.add_argument("--point", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--device", required=True)
    parser.add_argument("--external-timeout-seconds", type=int, required=True)
    args = parser.parse_args()

    lock = verify_lock(args.lock.resolve(), args.config.resolve())
    config = json.loads(args.config.read_text(encoding="utf-8"))
    point_keys = [str(value.get("key", "")) for value in config["points"]]
    if not point_keys or len(set(point_keys)) != len(point_keys):
        raise ValueError("configuration point keys must be nonempty and unique")
    try:
        point = next(value for value in config["points"] if value["key"] == args.point)
    except StopIteration as exc:
        raise ValueError(f"point {args.point!r} is absent from config") from exc
    point = dict(point)
    runner.validate_point(point)
    output = args.output.resolve()
    device = parse_cuda(args.device)
    unlock, output_root = verify_unlock(
        args.unlock.resolve(),
        args.lock.resolve(),
        args.config.resolve(),
        point,
        args.device,
        output,
    )
    if torch.cuda.get_device_name(device) not in unlock["allowed_gpu_names"]:
        raise RuntimeError("GPU model is absent from the execution unlock")
    if unlock["external_timeout_seconds"].get(point["key"]) != args.external_timeout_seconds:
        raise RuntimeError("external timeout differs from the execution unlock")
    ledger_path = reserve_attempt(output_root, unlock, point, args.device)
    output.mkdir(parents=True, exist_ok=False)
    manifest_path = output / "manifest.json"
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    manifest: dict[str, object] = {
        "status": "running",
        "accepted_for_scientific_analysis": False,
        "point": args.point,
        "device": args.device,
        "started_utc": started,
        "command": sys.argv,
        "config_sha256": sha256(args.config),
        "lock_sha256": sha256(args.lock),
        "unlock_sha256": sha256(args.unlock),
        "source_bundle_sha256": lock["bundle_sha256"],
        "point_contract": point,
    }
    write_json(manifest_path, manifest)

    def terminate(signum, _frame):
        manifest.update(
            status="terminated",
            termination_signal=signum,
            ended_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
        )
        write_json(manifest_path, manifest)
        raise ExternalTermination(f"received external signal {signum}")

    signal.signal(signal.SIGTERM, terminate)
    outer_started = time.monotonic()
    try:
        configure_determinism(device)
        arrays, diagnostics = runner.run_point(
            point, seed=int(config["seed"]), device=device
        )
        raw_path = output / "arrays.npz"
        np.savez_compressed(raw_path, **arrays)
        torch.cuda.synchronize(device)
        outer_elapsed = time.monotonic() - outer_started
        host_gib = float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) / 2**20
        gpu_gib = float(torch.cuda.max_memory_allocated(device)) / 2**30
        if outer_elapsed >= float(point["caps"]["wall_seconds"]):
            raise runner.BudgetStop("wall cap crossed during serialization")
        if host_gib > float(point["caps"]["host_rss_gib"]):
            raise runner.BudgetStop("host cap crossed during serialization")
        if gpu_gib > float(point["caps"]["gpu_memory_gib"]):
            raise runner.BudgetStop("GPU cap crossed during serialization")
        manifest.update(
            status="complete",
            completed_under_caps=True,
            accepted_for_scientific_analysis=False,
            ended_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
            raw_sha256=sha256(raw_path),
            diagnostics=diagnostics,
            torch_version=torch.__version__,
            cuda_version=torch.version.cuda,
            deterministic_algorithms=torch.are_deterministic_algorithms_enabled(),
            cublas_workspace_config=os.environ["CUBLAS_WORKSPACE_CONFIG"],
            tf32_matmul=bool(torch.backends.cuda.matmul.allow_tf32),
            gpu_name=torch.cuda.get_device_name(device),
            gpu_index=device.index,
            outer_elapsed_seconds=outer_elapsed,
            outer_host_rss_gib=host_gib,
            outer_gpu_allocated_gib=gpu_gib,
        )
        write_json(manifest_path, manifest)
        finalize_attempt(ledger_path, point["key"], "complete")
        return 0
    except BaseException as exc:
        manifest.update(
            status=("terminated" if isinstance(exc, ExternalTermination) else "failed"),
            ended_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
            exception_type=type(exc).__name__,
            exception_message=str(exc),
            traceback=traceback.format_exc(),
        )
        write_json(manifest_path, manifest)
        finalize_attempt(
            ledger_path,
            point["key"],
            "terminated" if isinstance(exc, ExternalTermination) else "failed",
        )
        raise


if __name__ == "__main__":
    raise SystemExit(main())
