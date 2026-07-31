#!/usr/bin/env python3
"""Generate finite-network ensemble references for the PDE comparison.

These runs are references only.  They are never used to construct or fit the
PDE velocity.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from dense_reference import (  # noqa: E402
    FieldState,
    ModelSpec,
    forward_adjoint,
    initialize,
    rk4_param_step,
    tangent_kernel,
)


def _one_seed(payload: tuple[int, int, int, float, float, float, float]) -> dict:
    n, depth, seed, duration, dt, sample_dt, sigma_w = payload
    X = np.eye(3)
    y = np.array([0.8, -0.55, 0.35])
    spec = ModelSpec(
        n=n,
        depth=depth,
        X=X,
        y=y,
        seed=seed,
        sigma_w=sigma_w,
        A=1.0,
        gamma=1.0,
    )
    state = initialize(spec)
    steps = int(round(duration / dt))
    stride = int(round(sample_dt / dt))
    samples = steps // stride + 1
    times = np.arange(samples, dtype=float) * sample_dt
    f = np.empty((samples, 3))
    grams = np.empty((samples, depth + 1, 3, 3))
    theta = np.empty((samples, 3, 3))
    sample = 0
    for step in range(steps + 1):
        if step % stride == 0:
            fields = forward_adjoint(state, spec)
            f[sample] = state.a @ fields.H[-1] / n
            grams[sample] = np.einsum(
                "lnr,lnq->lrq", fields.H, fields.H, optimize=True
            ) / n
            theta[sample] = tangent_kernel(
                FieldState(state.W, state.a, fields.H, fields.P), spec
            )
            sample += 1
        if step < steps:
            state = rk4_param_step(state, dt, spec)
    return {
        "seed": seed,
        "times": times,
        "f": f,
        "grams": grams,
        "theta": theta,
    }


def run(args: argparse.Namespace) -> Path:
    payloads = [
        (
            args.n,
            args.depth,
            args.seed_start + k,
            args.duration,
            args.dt,
            args.sample_dt,
            args.sigma_w,
        )
        for k in range(args.seeds)
    ]
    started = time.perf_counter()
    if args.workers == 1:
        results = [_one_seed(p) for p in payloads]
    else:
        with ProcessPoolExecutor(max_workers=args.workers) as pool:
            results = list(pool.map(_one_seed, payloads))
    elapsed = time.perf_counter() - started

    f = np.stack([r["f"] for r in results])
    grams = np.stack([r["grams"] for r in results])
    theta = np.stack([r["theta"] for r in results])
    times = results[0]["times"]
    metadata = {
        "role": "finite-network ensemble reference; never read by PDE drift",
        "model": "canonical fully dense residual tanh network",
        "training": "ordinary Euclidean muP gradient flow",
        "n": args.n,
        "depth": args.depth,
        "seed_start": args.seed_start,
        "seeds": args.seeds,
        "duration": args.duration,
        "dt": args.dt,
        "sample_dt": args.sample_dt,
        "sigma_w": args.sigma_w,
        "A": 1.0,
        "gamma": 1.0,
        "elapsed_seconds": elapsed,
    }
    output_dir = ROOT / "results" / "raw"
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / (
        f"exact_ensemble_n{args.n}_L{args.depth}"
        f"_S{args.seeds}_seed{args.seed_start}"
        f"_dt{str(args.dt).replace('.', 'p')}"
        f"_T{str(args.duration).replace('.', 'p')}.npz"
    )
    partial = path.with_suffix(path.suffix + ".partial")
    with partial.open("wb") as handle:
        np.savez_compressed(
            handle,
            times=times,
            seeds=np.array([r["seed"] for r in results]),
            f=f,
            grams=grams,
            theta=theta,
            f_mean=np.mean(f, axis=0),
            f_sem=np.std(f, axis=0, ddof=1) / np.sqrt(args.seeds),
            grams_mean=np.mean(grams, axis=0),
            grams_sem=np.std(grams, axis=0, ddof=1) / np.sqrt(args.seeds),
            theta_mean=np.mean(theta, axis=0),
            theta_sem=np.std(theta, axis=0, ddof=1) / np.sqrt(args.seeds),
            metadata_json=np.array(json.dumps(metadata, sort_keys=True)),
        )
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(partial, path)
    print(
        json.dumps(
            {
                "path": os.fspath(path),
                "elapsed_seconds": elapsed,
                "initial_mean_output": np.mean(f, axis=0)[0].tolist(),
                "max_output_sem_norm": float(
                    np.max(
                        np.linalg.norm(
                            np.std(f, axis=0, ddof=1)
                            / np.sqrt(args.seeds),
                            axis=-1,
                        )
                    )
                ),
                "max_gram_entry_sem": float(
                    np.max(np.std(grams, axis=0, ddof=1) / np.sqrt(args.seeds))
                ),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=64)
    parser.add_argument("--depth", type=int, default=16)
    parser.add_argument("--seeds", type=int, default=64)
    parser.add_argument("--seed-start", type=int, default=1000)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--duration", type=float, default=8.0)
    parser.add_argument("--dt", type=float, default=0.02)
    parser.add_argument("--sample-dt", type=float, default=0.04)
    parser.add_argument("--sigma-w", type=float, default=0.65)
    return parser.parse_args()


if __name__ == "__main__":
    run(parse_args())
