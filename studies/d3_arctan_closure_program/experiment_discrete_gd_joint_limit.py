"""Preregistered joint width/step-size experiment for exact metric GD.

See DISCRETE_GD_JOINT_LIMIT_PREREGISTRATION_2026-08-23.md.  This script uses
the original u parameter, not an Euler step in its nonlinear r coordinate.
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


def initialization(n: int, key: int):
    rng = np.random.default_rng(np.random.SeedSequence([key, n, 20260823]))
    a = rng.normal(size=n)
    u = rng.normal(size=n)
    gamma1 = rng.normal(size=(n, n)) / np.sqrt(n)
    gamma2 = rng.normal(size=(n, n)) / np.sqrt(n)
    return a, u, gamma1, gamma2


def fields(a: np.ndarray, u: np.ndarray, g1: np.ndarray, g2: np.ndarray):
    d1 = 1.0 / (1.0 + u * u)
    x1 = np.arctan(u)
    z2 = g1 @ x1
    d2 = 1.0 / (1.0 + z2 * z2)
    x2 = np.arctan(z2)
    z3 = g2 @ x2
    d3 = 1.0 / (1.0 + z3 * z3)
    x3 = np.arctan(z3)
    b3 = a * d3
    r2 = g2.T @ b3
    b2 = d2 * r2
    q1 = g1.T @ b2
    f = float(np.mean(a * x3))
    energies = (
        float(np.mean(x3 * x3)),
        float(np.mean(b3 * b3) * np.mean(x2 * x2)),
        float(np.mean(b2 * b2) * np.mean(x1 * x1)),
        float(np.mean((d1 * q1) ** 2)),
    )
    r2_abs = np.abs(r2)
    r2_lps = {
        str(p): float(np.mean(r2_abs**p) ** (1.0 / p)) for p in (2, 4, 8)
    }
    return {
        "d1": d1,
        "x1": x1,
        "x2": x2,
        "x3": x3,
        "b3": b3,
        "b2": b2,
        "q1": q1,
        "r2": r2,
        "f": f,
        "e": 1.0 - f,
        "loss": (1.0 - f) ** 2,
        "energies": energies,
        "K": float(sum(energies)),
        "r2_lps": r2_lps,
    }


def finite_field(d) -> bool:
    scalars = [d["f"], d["e"], d["loss"], d["K"], *d["energies"]]
    scalars.extend(d["r2_lps"].values())
    return bool(np.all(np.isfinite(scalars)))


def run_delta(n: int, key: int, delta: float, horizon: float):
    a0, u0, gamma1, gamma2 = initialization(n, key)
    a = a0.copy()
    u = u0.copy()
    g1 = gamma1.copy()
    g2 = gamma2.copy()
    n_steps_float = horizon / delta
    if abs(n_steps_float - round(n_steps_float)) > 1e-10:
        raise ValueError("horizon must be an integer multiple of delta")
    n_steps = int(round(n_steps_float))
    records = []
    hitting = {str(q): None for q in THRESHOLDS}
    finite = True
    start = time.monotonic()

    previous = None
    for k in range(n_steps + 1):
        d = fields(a, u, g1, g2)
        if not finite_field(d):
            finite = False
            break
        record = {
            "t": float(k * delta),
            "f": d["f"],
            "loss": d["loss"],
            "K": d["K"],
            "energies": list(d["energies"]),
            "r2_lps": d["r2_lps"],
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
        a += scale * d["x3"]
        u += scale * d["d1"] * d["q1"]
        g1 += (scale / n) * np.multiply.outer(d["b2"], d["x1"])
        g2 += (scale / n) * np.multiply.outer(d["b3"], d["x2"])
        previous = (record, d["e"], d["K"])

    return {
        "delta": float(delta),
        "finite": finite,
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
    deltas = tuple(float(x) for x in args.deltas)
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
        with concurrent.futures.ProcessPoolExecutor(
            max_workers=args.workers
        ) as pool:
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
