"""Exact float64 two-GPU width ladder for the quadratic L=2 model.

The scientific contract is frozen in
QUADRATIC_L2_GPU_LARGE_WIDTH_PREREGISTRATION_2026-08-23.md.
"""

from __future__ import annotations

import argparse
import gc
import hashlib
import json
import math
import multiprocessing as mp
import os
import platform
import queue
import sys
import time
import traceback
from pathlib import Path

os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")

import numpy as np
import torch


THRESHOLDS = (0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99)
SEED_SALT = 2026082302
STOP_THRESHOLD = 0.99
MINIMUM_STOP_TIME = 0.005
PEAK_MEMORY_CAP_GIB = 18.0
QUALIFICATION_LARGE_WIDTH = 32768
QUALIFICATION_KEY = 929999
FROZEN_WIDTHS = (2048, 4096, 8192, 16384, 32768)
FROZEN_KEYS = (9201, 9202, 9203, 9204, 9205, 9206)
FROZEN_DELTAS = (0.000625, 0.0003125)
FROZEN_HORIZON = 0.25


def script_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def seed_for(n: int, key: int) -> int:
    payload = f"quadratic-l2-gpu:{SEED_SALT}:{n}:{key}".encode("ascii")
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "little") & (
        (1 << 63) - 1
    )


def configure_device(device_index: int) -> torch.device:
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is unavailable")
    if device_index < 0 or device_index >= torch.cuda.device_count():
        raise ValueError(f"invalid CUDA device {device_index}")
    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)
    device = torch.device(f"cuda:{device_index}")
    torch.cuda.set_device(device)
    return device


def initialization(n: int, key: int, device: torch.device):
    generator = torch.Generator(device=device)
    generator.manual_seed(seed_for(n, key))
    x = torch.randn(n, generator=generator, device=device, dtype=torch.float64)
    a = torch.randn(n, generator=generator, device=device, dtype=torch.float64)
    w = torch.randn(
        (n, n), generator=generator, device=device, dtype=torch.float64
    )
    w.mul_(n ** -0.5)
    return a, x, w


def fields(a: torch.Tensor, x: torch.Tensor, w: torch.Tensor):
    h = 0.5 * x.square()
    z = torch.mv(w, h)
    nu = a * z
    dx = x * torch.mv(w.transpose(0, 1), nu)
    z2 = z.square()
    z4 = z2.square()
    f_tensor = 0.5 * torch.mean(a * z2)
    e0 = 0.25 * torch.mean(z4)
    e1 = torch.mean(h.square()) * torch.mean(nu.square())
    e2 = torch.mean(dx.square())
    readout_mass = torch.sum(z4)
    scalar_tensor = torch.stack(
        (
            f_tensor,
            e0,
            e1,
            e2,
            torch.max(torch.abs(a)),
            torch.max(torch.abs(x)),
            torch.max(torch.abs(z)),
            torch.max(z4) / readout_mass,
        )
    )
    values = scalar_tensor.detach().cpu().tolist()
    f = float(values[0])
    energies = tuple(float(value) for value in values[1:4])
    return {
        "h": h,
        "z": z,
        "z2": z2,
        "nu": nu,
        "dx": dx,
        "f": f,
        "e": 1.0 - f,
        "loss": (1.0 - f) ** 2,
        "energies": energies,
        "K": float(sum(energies)),
        "max_abs": {
            "a": float(values[4]),
            "x": float(values[5]),
            "z": float(values[6]),
        },
        "readout_condensation": float(values[7]),
    }


def finite_field(d: dict) -> bool:
    values = [
        d["f"],
        d["e"],
        d["loss"],
        d["K"],
        d["readout_condensation"],
        *d["energies"],
        *d["max_abs"].values(),
    ]
    return all(math.isfinite(value) for value in values)


@torch.no_grad()
def run_delta(
    n: int,
    key: int,
    delta: float,
    horizon: float,
    device_index: int,
    stop_threshold: float = STOP_THRESHOLD,
):
    device = configure_device(device_index)
    torch.cuda.empty_cache()
    torch.cuda.reset_peak_memory_stats(device)
    start = time.monotonic()
    a, x, w = initialization(n, key, device)
    n_steps_float = horizon / delta
    if abs(n_steps_float - round(n_steps_float)) > 1e-10:
        raise ValueError("horizon must be an integer multiple of delta")
    n_steps = int(round(n_steps_float))
    records: list[dict] = []
    hitting = {str(q): None for q in THRESHOLDS}
    finite = True
    failure_time = None
    stopped_at_threshold = False
    previous = None

    for k in range(n_steps + 1):
        d = fields(a, x, w)
        if not finite_field(d):
            finite = False
            failure_time = float(k * delta)
            break
        record = {
            "t": float(k * delta),
            "f": d["f"],
            "loss": d["loss"],
            "K": d["K"],
            "energies": list(d["energies"]),
            "max_abs": d["max_abs"],
            "readout_condensation": d["readout_condensation"],
            "flow_defect": None,
            "loss_increment": None,
        }
        if previous is not None:
            old_record, old_e, old_k = previous
            predictor_slope = (record["f"] - old_record["f"]) / delta
            old_record["flow_defect"] = abs(
                predictor_slope - 2.0 * old_e * old_k
            ) / (1.0 + 2.0 * abs(old_e) * old_k)
            old_record["loss_increment"] = record["loss"] - old_record["loss"]
        records.append(record)

        if k == 0:
            for q in THRESHOLDS:
                if d["f"] >= q:
                    hitting[str(q)] = 0.0
        else:
            f_left = records[-2]["f"]
            f_right = record["f"]
            for q in THRESHOLDS:
                q_key = str(q)
                if hitting[q_key] is None and f_left < q <= f_right:
                    fraction = (q - f_left) / max(
                        f_right - f_left, np.finfo(float).tiny
                    )
                    hitting[q_key] = float((k - 1 + fraction) * delta)

        if d["f"] >= stop_threshold and record["t"] >= MINIMUM_STOP_TIME:
            stopped_at_threshold = True
            break
        if k == n_steps:
            break

        scale = 2.0 * delta * d["e"]
        # Exact simultaneous old-state update. addr_ avoids an n-by-n outer
        # product allocation while applying precisely the same rank-one step.
        a.add_(d["z2"], alpha=0.5 * scale)
        x.add_(d["dx"], alpha=scale)
        w.addr_(d["nu"], d["h"], beta=1.0, alpha=scale / n)
        previous = (record, d["e"], d["K"])

    torch.cuda.synchronize(device)
    peak_gib = torch.cuda.max_memory_allocated(device) / 2**30
    result = {
        "delta": float(delta),
        "seed": seed_for(n, key),
        "finite": finite,
        "failure_time": failure_time,
        "last_finite_time": records[-1]["t"] if records else None,
        "stopped_at_threshold": stopped_at_threshold,
        "hitting_times": hitting,
        "records": records,
        "peak_allocated_gib": float(peak_gib),
        "memory_cap_pass": bool(peak_gib < PEAK_MEMORY_CAP_GIB),
        "wall_seconds": time.monotonic() - start,
    }
    del d, a, x, w
    gc.collect()
    torch.cuda.empty_cache()
    return result


def run_bundle(
    n: int,
    key: int,
    deltas: tuple[float, ...],
    horizon: float,
    device_index: int,
):
    start = time.monotonic()
    runs = [
        run_delta(n, key, delta, horizon, device_index) for delta in deltas
    ]
    return {
        "kind": "bundle",
        "n": n,
        "key": key,
        "device_index": device_index,
        "runs": runs,
        "wall_seconds": time.monotonic() - start,
    }


def worker_main(
    device_index: int,
    tasks: list[tuple[int, int]],
    deltas: tuple[float, ...],
    horizon: float,
    result_queue,
):
    try:
        configure_device(device_index)
        for n, key in tasks:
            try:
                result = run_bundle(n, key, deltas, horizon, device_index)
            except Exception as exc:
                result = {
                    "kind": "error",
                    "n": n,
                    "key": key,
                    "device_index": device_index,
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                    "traceback": traceback.format_exc(),
                }
                result_queue.put(result)
                break
            result_queue.put(result)
    except Exception as exc:
        result_queue.put(
            {
                "kind": "worker_error",
                "device_index": device_index,
                "error_type": type(exc).__name__,
                "error": str(exc),
                "traceback": traceback.format_exc(),
            }
        )
    finally:
        result_queue.put({"kind": "worker_done", "device_index": device_index})


def numpy_fields(a: np.ndarray, x: np.ndarray, w: np.ndarray):
    h = 0.5 * x * x
    z = w @ h
    nu = a * z
    dx = x * (w.T @ nu)
    energies = np.asarray(
        [
            0.25 * np.mean(z**4),
            np.mean(h**2) * np.mean(nu**2),
            np.mean(dx**2),
        ]
    )
    return h, z, nu, dx, 0.5 * np.mean(a * z**2), energies


@torch.no_grad()
def cross_backend_qualification(device_index: int):
    device = configure_device(device_index)
    n = 37
    delta = 0.0003125
    rng = np.random.default_rng(202608230299)
    x_np = rng.normal(size=n)
    a_np = rng.normal(size=n)
    w_np = rng.normal(size=(n, n)) / np.sqrt(n)
    h_np, z_np, nu_np, dx_np, f_np, energies_np = numpy_fields(
        a_np, x_np, w_np
    )
    a = torch.as_tensor(a_np, device=device)
    x = torch.as_tensor(x_np, device=device)
    w = torch.as_tensor(w_np, device=device)
    d = fields(a, x, w)
    field_errors = {
        "f": abs(d["f"] - float(f_np)),
        "energies_max": float(
            np.max(np.abs(np.asarray(d["energies"]) - energies_np))
        ),
        "h_max": float(np.max(np.abs(d["h"].cpu().numpy() - h_np))),
        "z_max": float(np.max(np.abs(d["z"].cpu().numpy() - z_np))),
        "nu_max": float(np.max(np.abs(d["nu"].cpu().numpy() - nu_np))),
        "dx_max": float(np.max(np.abs(d["dx"].cpu().numpy() - dx_np))),
    }
    scale = 2.0 * delta * (1.0 - f_np)
    a_np_next = a_np + scale * 0.5 * z_np**2
    x_np_next = x_np + scale * dx_np
    w_np_next = w_np + (scale / n) * np.outer(nu_np, h_np)
    a.add_(d["z2"], alpha=0.5 * scale)
    x.add_(d["dx"], alpha=scale)
    w.addr_(d["nu"], d["h"], beta=1.0, alpha=scale / n)
    update_errors = {
        "a_max": float(np.max(np.abs(a.cpu().numpy() - a_np_next))),
        "x_max": float(np.max(np.abs(x.cpu().numpy() - x_np_next))),
        "w_max": float(np.max(np.abs(w.cpu().numpy() - w_np_next))),
    }
    maximum_error = max(*field_errors.values(), *update_errors.values())
    return {
        "device_index": device_index,
        "field_errors": field_errors,
        "update_errors": update_errors,
        "maximum_error": maximum_error,
        "passed": bool(maximum_error <= 1e-10),
    }


@torch.no_grad()
def replay_qualification(device_index: int):
    run1 = run_delta(256, QUALIFICATION_KEY, 0.0003125, 0.003125, device_index, 2.0)
    run2 = run_delta(256, QUALIFICATION_KEY, 0.0003125, 0.003125, device_index, 2.0)
    digest1 = hashlib.sha256(
        json.dumps(run1["records"], sort_keys=True).encode("utf-8")
    ).hexdigest()
    digest2 = hashlib.sha256(
        json.dumps(run2["records"], sort_keys=True).encode("utf-8")
    ).hexdigest()
    return {
        "device_index": device_index,
        "digest1": digest1,
        "digest2": digest2,
        "passed": digest1 == digest2 and run1["finite"] and run2["finite"],
    }


def qualification(output: Path):
    if torch.cuda.device_count() < 2:
        raise RuntimeError("two CUDA devices are required")
    start = time.monotonic()
    cross_backend = [cross_backend_qualification(index) for index in (0, 1)]
    replay = [replay_qualification(index) for index in (0, 1)]
    large = run_delta(
        QUALIFICATION_LARGE_WIDTH,
        QUALIFICATION_KEY,
        0.0003125,
        0.0009375,
        0,
        2.0,
    )
    passed = (
        all(item["passed"] for item in cross_backend)
        and all(item["passed"] for item in replay)
        and large["finite"]
        and large["memory_cap_pass"]
        and len(large["records"]) == 4
    )
    result = {
        "kind": "qualification",
        "status": "non_scientific_qualification_only",
        "script_sha256": script_sha256(),
        "python": sys.version,
        "torch": torch.__version__,
        "torch_cuda": torch.version.cuda,
        "cross_backend": cross_backend,
        "deterministic_replay": replay,
        "large_width_three_step": {
            "n": QUALIFICATION_LARGE_WIDTH,
            "finite": large["finite"],
            "record_count": len(large["records"]),
            "peak_allocated_gib": large["peak_allocated_gib"],
            "memory_cap_pass": large["memory_cap_pass"],
            "wall_seconds": large["wall_seconds"],
        },
        "passed": passed,
        "wall_seconds": time.monotonic() - start,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps(result, indent=2, sort_keys=True), flush=True)
    return 0 if passed else 2


def gpu_metadata():
    devices = []
    for index in range(torch.cuda.device_count()):
        props = torch.cuda.get_device_properties(index)
        free, total = torch.cuda.mem_get_info(index)
        devices.append(
            {
                "index": index,
                "name": props.name,
                "capability": [props.major, props.minor],
                "total_memory_gib": total / 2**30,
                "free_memory_gib_at_launch": free / 2**30,
            }
        )
    return devices


def scientific_run(args):
    qualification_result = json.loads(args.qualification.read_text())
    if not qualification_result.get("passed"):
        raise RuntimeError("qualification did not pass")
    if qualification_result.get("script_sha256") != script_sha256():
        raise RuntimeError("script changed after qualification")
    if torch.cuda.device_count() < 2:
        raise RuntimeError("two CUDA devices are required")

    widths = tuple(args.widths)
    keys = tuple(args.keys)
    deltas = tuple(float(value) for value in args.deltas)
    if widths != FROZEN_WIDTHS:
        raise ValueError(f"widths must equal frozen grid {FROZEN_WIDTHS}")
    if keys != FROZEN_KEYS:
        raise ValueError(f"keys must equal frozen keys {FROZEN_KEYS}")
    if deltas != FROZEN_DELTAS:
        raise ValueError(f"deltas must equal frozen pair {FROZEN_DELTAS}")
    if args.horizon != FROZEN_HORIZON:
        raise ValueError(f"horizon must equal frozen value {FROZEN_HORIZON}")
    tasks_by_device = {0: [], 1: []}
    for n in sorted(widths, reverse=True):
        for key_index, key in enumerate(keys):
            tasks_by_device[key_index % 2].append((n, key))
    expected_bundles = len(widths) * len(keys)
    metadata = {
        "kind": "metadata",
        "schema": "quadratic-l2-gpu-large-width-v1",
        "script_sha256": script_sha256(),
        "qualification": str(args.qualification),
        "qualification_sha256": hashlib.sha256(
            args.qualification.read_bytes()
        ).hexdigest(),
        "python": sys.version,
        "platform": platform.platform(),
        "torch": torch.__version__,
        "torch_cuda": torch.version.cuda,
        "cublas_workspace_config": os.environ.get("CUBLAS_WORKSPACE_CONFIG"),
        "deterministic_algorithms": True,
        "devices": gpu_metadata(),
        "arguments": {
            "widths": list(widths),
            "keys": list(keys),
            "deltas": list(deltas),
            "horizon": args.horizon,
            "wall_limit_seconds": args.wall_limit_seconds,
            "output": str(args.output),
        },
    }

    ctx = mp.get_context("spawn")
    result_queue = ctx.Queue()
    processes = [
        ctx.Process(
            target=worker_main,
            args=(
                device_index,
                tasks_by_device[device_index],
                deltas,
                args.horizon,
                result_queue,
            ),
        )
        for device_index in (0, 1)
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    start = time.monotonic()
    done_workers: set[int] = set()
    observed_bundles = 0
    timed_out = False
    with args.output.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(metadata, sort_keys=True) + "\n")
        handle.flush()
        for process in processes:
            process.start()
        while len(done_workers) < len(processes):
            elapsed = time.monotonic() - start
            if elapsed > args.wall_limit_seconds:
                timed_out = True
                break
            try:
                result = result_queue.get(timeout=5.0)
            except queue.Empty:
                if all(not process.is_alive() for process in processes):
                    break
                continue
            if result["kind"] == "worker_done":
                done_workers.add(result["device_index"])
                continue
            if result["kind"] == "bundle":
                observed_bundles += 1
            handle.write(json.dumps(result, sort_keys=True) + "\n")
            handle.flush()
            print(
                f"kind={result['kind']} device={result.get('device_index')} "
                f"n={result.get('n')} key={result.get('key')} "
                f"wall={result.get('wall_seconds', float('nan')):.2f}s",
                flush=True,
            )

        if timed_out:
            timeout_record = {
                "kind": "timeout",
                "elapsed_seconds": time.monotonic() - start,
                "observed_bundles": observed_bundles,
                "expected_bundles": expected_bundles,
            }
            handle.write(json.dumps(timeout_record, sort_keys=True) + "\n")
            handle.flush()
        for process in processes:
            if process.is_alive():
                process.terminate()
            process.join(timeout=10.0)

    complete = (
        not timed_out
        and observed_bundles == expected_bundles
        and len(done_workers) == 2
        and all(process.exitcode == 0 for process in processes)
    )
    print(
        json.dumps(
            {
                "complete": complete,
                "observed_bundles": observed_bundles,
                "expected_bundles": expected_bundles,
                "done_workers": sorted(done_workers),
                "exitcodes": [process.exitcode for process in processes],
                "wall_seconds": time.monotonic() - start,
            },
            indent=2,
            sort_keys=True,
        ),
        flush=True,
    )
    return 0 if complete else 2


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="mode", required=True)
    qualification_parser = subparsers.add_parser("qualify")
    qualification_parser.add_argument("--output", type=Path, required=True)
    run_parser = subparsers.add_parser("run")
    run_parser.add_argument("--qualification", type=Path, required=True)
    run_parser.add_argument("--widths", type=int, nargs="+", required=True)
    run_parser.add_argument("--keys", type=int, nargs="+", required=True)
    run_parser.add_argument("--deltas", type=float, nargs="+", required=True)
    run_parser.add_argument("--horizon", type=float, required=True)
    run_parser.add_argument("--wall-limit-seconds", type=float, default=2700.0)
    run_parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.mode == "qualify":
        return qualification(args.output)
    return scientific_run(args)


if __name__ == "__main__":
    raise SystemExit(main())
