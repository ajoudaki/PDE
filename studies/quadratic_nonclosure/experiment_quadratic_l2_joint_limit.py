"""Preregistered joint width/step experiment for the quadratic L=2 model.

See QUADRATIC_L2_JOINT_LIMIT_PREREGISTRATION_2026-08-23.md.  The update is
the exact simultaneous metric-gradient step in the original parameters.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import platform
import time
from pathlib import Path

import numpy as np


THRESHOLDS = (0.10, 0.25, 0.50, 0.75, 0.90, 0.95)
SEED_SALT = 20260824


def initialization(n: int, key: int):
    rng = np.random.default_rng(np.random.SeedSequence([key, n, SEED_SALT]))
    x = rng.normal(size=n)
    a = rng.normal(size=n)
    w = rng.normal(size=(n, n)) / np.sqrt(n)
    return a, x, w


def fields(a: np.ndarray, x: np.ndarray, w: np.ndarray):
    """Return the predictor, exact tangent-kernel blocks, and update fields."""
    with np.errstate(over="ignore", invalid="ignore"):
        h = 0.5 * x * x
        z = w @ h
        nu = a * z
        dx = x * (w.T @ nu)
        z2 = z * z
        z4 = z2 * z2
        f = float(0.5 * np.mean(a * z2))
        energies = (
            float(0.25 * np.mean(z4)),
            float(np.mean(h * h) * np.mean(nu * nu)),
            float(np.mean(dx * dx)),
        )
        readout_mass = float(np.sum(z4))
        readout_condensation = (
            float(np.max(z4) / readout_mass)
            if readout_mass > 0.0 and np.isfinite(readout_mass)
            else float("nan")
        )
        max_abs = {
            "a": float(np.max(np.abs(a))),
            "x": float(np.max(np.abs(x))),
            "z": float(np.max(np.abs(z))),
        }
    return {
        "h": h,
        "z": z,
        "nu": nu,
        "dx": dx,
        "f": f,
        "e": 1.0 - f,
        "loss": (1.0 - f) ** 2,
        "energies": energies,
        "K": float(sum(energies)),
        "max_abs": max_abs,
        "readout_condensation": readout_condensation,
    }


def finite_field(d) -> bool:
    scalars = [
        d["f"],
        d["e"],
        d["loss"],
        d["K"],
        d["readout_condensation"],
        *d["energies"],
        *d["max_abs"].values(),
    ]
    return bool(np.all(np.isfinite(scalars)))


def run_delta(n: int, key: int, delta: float, horizon: float):
    a0, x0, w0 = initialization(n, key)
    a = a0.copy()
    x = x0.copy()
    w = w0.copy()
    n_steps_float = horizon / delta
    if abs(n_steps_float - round(n_steps_float)) > 1e-10:
        raise ValueError("horizon must be an integer multiple of delta")
    n_steps = int(round(n_steps_float))
    records = []
    hitting = {str(q): None for q in THRESHOLDS}
    finite = True
    failure_time = None
    start = time.monotonic()

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
            slope = (record["f"] - old_record["f"]) / delta
            old_record["flow_defect"] = abs(slope - 2.0 * old_e * old_k) / (
                1.0 + 2.0 * abs(old_e) * old_k
            )
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

        if k == n_steps:
            break

        scale = 2.0 * delta * d["e"]
        # Simultaneous update: every increment uses the old state.
        with np.errstate(over="ignore", invalid="ignore"):
            a += scale * (0.5 * d["z"] * d["z"])
            x += scale * d["dx"]
            w += (scale / n) * np.multiply.outer(d["nu"], d["h"])
        previous = (record, d["e"], d["K"])

    return {
        "delta": float(delta),
        "finite": finite,
        "failure_time": failure_time,
        "last_finite_time": records[-1]["t"] if records else None,
        "hitting_times": hitting,
        "records": records,
        "wall_seconds": time.monotonic() - start,
    }


def run_bundle(n: int, key: int, deltas: tuple[float, ...], horizon: float):
    start = time.monotonic()
    runs = [run_delta(n, key, delta, horizon) for delta in deltas]
    return {
        "kind": "bundle",
        "n": n,
        "key": key,
        "runs": runs,
        "wall_seconds": time.monotonic() - start,
    }


def script_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--widths", type=int, nargs="+", required=True)
    parser.add_argument("--keys", type=int, nargs="+", required=True)
    parser.add_argument("--deltas", type=float, nargs="+", required=True)
    parser.add_argument("--horizon", type=float, default=2.0)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.workers < 1 or args.workers > 6:
        raise ValueError("workers must lie in [1,6]")
    deltas = tuple(float(value) for value in args.deltas)
    metadata = {
        "kind": "metadata",
        "script_sha256": script_sha256(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "platform": platform.platform(),
        "arguments": {
            "widths": args.widths,
            "keys": args.keys,
            "deltas": list(deltas),
            "horizon": args.horizon,
            "workers": args.workers,
            "output": str(args.output),
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    tasks = [(n, key) for n in args.widths for key in args.keys]
    with args.output.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(metadata, sort_keys=True) + "\n")
        handle.flush()
        with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as pool:
            futures = {
                pool.submit(run_bundle, n, key, deltas, args.horizon): (n, key)
                for n, key in tasks
            }
            for future in concurrent.futures.as_completed(futures):
                n, key = futures[future]
                try:
                    result = future.result()
                except Exception as exc:  # retained as an explicit failed run
                    result = {
                        "kind": "error",
                        "n": n,
                        "key": key,
                        "error_type": type(exc).__name__,
                        "error": str(exc),
                    }
                handle.write(json.dumps(result, sort_keys=True) + "\n")
                handle.flush()
                print(
                    f"n={n} key={key} kind={result['kind']} "
                    f"wall={result.get('wall_seconds', float('nan')):.2f}s",
                    flush=True,
                )


if __name__ == "__main__":
    main()
