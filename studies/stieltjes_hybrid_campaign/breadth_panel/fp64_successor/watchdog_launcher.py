#!/usr/bin/env python3
"""Canonical external watchdog for the FP64 preflight and A/M/V pairs."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import fcntl
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from typing import Any


SUCCESSOR_RELATIVE = Path(
    "studies/stieltjes_conjecture/numerics/hybrid_mean_field_campaign/"
    "breadth_panel/fp64_successor"
)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeError(f"{path} is not a JSON object")
    return value


def write_exclusive(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
        handle.write(json.dumps(value, indent=2, sort_keys=True) + "\n")


def write_atomic(path: Path, value: dict[str, Any]) -> None:
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def sha256_file(path: Path) -> str:
    import hashlib

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def finalize_external_group_failure(
    ledger_path: Path,
    attempt_path: Path,
    group: str,
    elapsed_seconds: float,
    error_type: str,
    error: str,
) -> None:
    stage_lock = ledger_path.parent / ".attempts.lock"
    with stage_lock.open("a+", encoding="utf-8") as lock_handle:
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_EX)
        ledger = read_json(ledger_path)
        record = ledger["attempts"][group]
        if record.get("status") not in {"reserved", "running"}:
            return
        attempt = read_json(attempt_path)
        ended = utc_now()
        attempt.update(
            status="failed",
            ended_utc=ended,
            error_type=error_type,
            error=error,
            gpu_seconds=float(elapsed_seconds),
        )
        write_atomic(attempt_path, attempt)
        record.update(
            status="failed",
            ended_utc=ended,
            error_type=error_type,
            error=error,
            gpu_seconds=float(elapsed_seconds),
            all_local_gates_pass=False,
            attempt_sha256=sha256_file(attempt_path),
        )
        consumed = sum(
            float(value.get("gpu_seconds", 0.0))
            for value in ledger["attempts"].values()
        )
        ledger["consumed_gpu_seconds"] = consumed
        ledger["stage_budget_pass"] = consumed <= float(
            ledger["stage_gpu_seconds_ceiling"]
        )
        write_atomic(ledger_path, ledger)
        fcntl.flock(lock_handle.fileno(), fcntl.LOCK_UN)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--mode", choices=("preflight", "group"), required=True)
    parser.add_argument("--group", choices=("A", "M", "V"))
    parser.add_argument("--device", required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    successor = (repo / SUCCESSOR_RELATIVE).resolve()
    if Path(__file__).resolve() != successor / "watchdog_launcher.py":
        raise RuntimeError("watchdog launcher is not running from the canonical successor")
    if args.device != "cuda:0":
        raise RuntimeError("the frozen watchdog permits only cuda:0")
    if (args.mode == "group") != (args.group is not None):
        raise RuntimeError("group is required exactly for group mode")

    config = successor / "FROZEN_LOCAL_QUALIFICATION.json"
    lock = successor / "FROZEN_LOCAL_QUALIFICATION_LOCK.json"
    unlock = successor / "LOCAL_QUALIFICATION_UNLOCK.json"
    frozen = read_json(config)
    watchdogs = frozen["external_watchdogs"]
    key = args.group if args.mode == "group" else "preflight"
    record_path = successor / "watchdog_records" / f"{key}.json"
    if record_path.exists():
        raise RuntimeError(f"the one-shot watchdog record for {key} already exists")

    if args.mode == "group":
        if str(successor) not in sys.path:
            sys.path.insert(0, str(successor))
        import run_local_qualification as local

        provenance = local.verify_lock(
            repo,
            config,
            lock,
            unlock,
            str(args.group),
            args.device,
        )
        output, ledger_path, attempt = local.reserve_canonical_attempt(
            repo,
            frozen,
            str(args.group),
            args.device,
            provenance,
        )
        attempt_path = output / "ATTEMPT.json"
        attempt = {"schema": "breadth-fp64-local-attempt-v1", **attempt}
        write_exclusive(attempt_path, attempt)
        timeout_seconds = float(attempt["watchdog_timeout_seconds"])
    else:
        ledger_path = None
        timeout_seconds = float(watchdogs["gpu_preflight_seconds"])

    started = {
        "schema": "breadth-fp64-external-watchdog-v1",
        "status": "running",
        "mode": args.mode,
        "group": args.group,
        "device": args.device,
        "launcher_pid": os.getpid(),
        "timeout_seconds": timeout_seconds,
        "started_utc": utc_now(),
    }
    if args.mode == "group":
        started["stage_gpu_seconds_before"] = attempt["stage_gpu_seconds_before"]
    write_exclusive(record_path, started)

    if args.mode == "preflight":
        script = successor / "gpu_preflight.py"
        command = [
            sys.executable,
            str(script),
            "--repo",
            str(repo),
            "--config",
            str(config),
            "--lock",
            str(lock),
            "--device",
            args.device,
        ]
        result_path = successor / "GPU_PREFLIGHT.json"
        attempt_path = successor / "GPU_PREFLIGHT_ATTEMPT.json"
    else:
        script = successor / "run_local_qualification.py"
        command = [
            sys.executable,
            str(script),
            "--repo",
            str(repo),
            "--config",
            str(config),
            "--lock",
            str(lock),
            "--unlock",
            str(unlock),
            "--group",
            str(args.group),
            "--device",
            args.device,
        ]
        result_path = successor / "runs/local_v1" / str(args.group) / "RESULT.json"
        attempt_path = successor / "runs/local_v1" / str(args.group) / "ATTEMPT.json"

    environment = os.environ.copy()
    timeout_text = (
        local.format_seconds(timeout_seconds)
        if args.mode == "group"
        else format(timeout_seconds, ".12g")
    )
    environment["FP64_WATCHDOG_ACTIVE"] = f"{args.mode}:{key}:{timeout_text}"
    started["command"] = command
    write_atomic(record_path, started)
    monotonic_started = time.monotonic()
    try:
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            env=environment,
            timeout=timeout_seconds,
        )
        elapsed = time.monotonic() - monotonic_started
        status = "completed" if completed.returncode == 0 else "child_exit_nonzero"
        if args.mode == "group" and completed.returncode != 0:
            assert ledger_path is not None
            finalize_external_group_failure(
                ledger_path,
                attempt_path,
                str(args.group),
                elapsed,
                "ExternalChildExit",
                f"watchdog child exited with code {completed.returncode}",
            )
        record = {
            **started,
            "status": status,
            "ended_utc": utc_now(),
            "elapsed_seconds": elapsed,
            "returncode": completed.returncode,
            "stdout": completed.stdout,
            "stderr": completed.stderr,
            "result_sha256": sha256_file(result_path) if result_path.is_file() else None,
            "attempt_sha256": sha256_file(attempt_path) if attempt_path.is_file() else None,
        }
        write_atomic(record_path, record)
        if completed.stdout:
            print(completed.stdout, end="")
        if completed.stderr:
            print(completed.stderr, end="", file=sys.stderr)
        return int(completed.returncode)
    except subprocess.TimeoutExpired as exc:
        elapsed = time.monotonic() - monotonic_started
        if args.mode == "group":
            assert ledger_path is not None
            finalize_external_group_failure(
                ledger_path,
                attempt_path,
                str(args.group),
                elapsed,
                "ExternalWatchdogTimeout",
                f"external watchdog expired after {timeout_seconds} seconds",
            )
        record = {
            **started,
            "status": "timed_out",
            "ended_utc": utc_now(),
            "elapsed_seconds": elapsed,
            "returncode": 124,
            "stdout": exc.stdout.decode() if isinstance(exc.stdout, bytes) else (exc.stdout or ""),
            "stderr": exc.stderr.decode() if isinstance(exc.stderr, bytes) else (exc.stderr or ""),
            "result_sha256": sha256_file(result_path) if result_path.is_file() else None,
            "attempt_sha256": sha256_file(attempt_path) if attempt_path.is_file() else None,
        }
        write_atomic(record_path, record)
        return 124
    except BaseException as exc:
        elapsed = time.monotonic() - monotonic_started
        if args.mode == "group":
            assert ledger_path is not None
            finalize_external_group_failure(
                ledger_path,
                attempt_path,
                str(args.group),
                elapsed,
                "ExternalLauncherError",
                f"external watchdog launcher failed: {type(exc).__name__}: {exc}",
            )
        record = {
            **started,
            "status": "launcher_error",
            "ended_utc": utc_now(),
            "elapsed_seconds": elapsed,
            "returncode": 125,
            "error_type": type(exc).__name__,
            "error": str(exc),
            "result_sha256": sha256_file(result_path) if result_path.is_file() else None,
            "attempt_sha256": sha256_file(attempt_path) if attempt_path.is_file() else None,
        }
        write_atomic(record_path, record)
        raise


if __name__ == "__main__":
    raise SystemExit(main())
