#!/usr/bin/env python3
"""Generate finite-network ensemble references for the PDE comparison.

These runs are references only.  They are never used to construct or fit the
PDE velocity.
"""

from __future__ import annotations

import argparse
import hashlib
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
from activations import ACTIVATION_NAMES  # noqa: E402
from study_cases import case_metadata, load_case  # noqa: E402


def _file_sha256(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _one_seed(payload: dict) -> dict:
    n = payload["n"]
    depth = payload["depth"]
    seed = payload["seed"]
    duration = payload["duration"]
    dt = payload["dt"]
    sample_dt = payload["sample_dt"]
    X = payload["X"]
    y = payload["y"]
    spec = ModelSpec(
        n=n,
        depth=depth,
        X=X,
        y=y,
        seed=seed,
        sigma_w=payload["sigma_w"],
        A=payload["A"],
        gamma=payload["gamma"],
        activation=payload["activation"],
    )
    state = initialize(spec)
    steps = int(round(duration / dt))
    stride = int(round(sample_dt / dt))
    samples = steps // stride + 1
    times = np.arange(samples, dtype=float) * sample_dt
    m = y.size
    f = np.empty((samples, m))
    grams = np.empty((samples, depth + 1, m, m))
    theta = np.empty((samples, m, m))
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
    if args.pde_seal is None:
        pde_seal_sha256 = None
        dynamics_sha256 = None
    else:
        pde_seal_path = Path(args.pde_seal)
        pde_seal_sha256 = _file_sha256(pde_seal_path)
        pde_seal = json.loads(pde_seal_path.read_text())
        dynamics_sha256 = pde_seal["dynamics_sha256"]
    if args.case_id is not None:
        if args.case_registry is None:
            raise ValueError("--case-id requires --case-registry")
        case = load_case(args.case_registry, args.case_id)
        case_info = case_metadata(case)
        X = case.X
        y = case.y
        activation = case.activation
        sigma_w = case.sigma_w
        A = case.A
        gamma = case.gamma
        for arg_name, expected in (
            ("sigma_w", sigma_w),
            ("A", A),
            ("gamma", gamma),
        ):
            override = getattr(args, arg_name)
            if override is not None and override != expected:
                raise ValueError(
                    f"--{arg_name.replace('_', '-')} conflicts with case registry"
                )
        if args.activation is not None and args.activation != activation:
            raise ValueError("--activation conflicts with case registry")
    else:
        X = np.eye(3)
        y = np.array([0.8, -0.55, 0.35])
        activation = args.activation or "tanh"
        sigma_w = 0.65 if args.sigma_w is None else args.sigma_w
        A = 1.0 if args.A is None else args.A
        gamma = 1.0 if args.gamma is None else args.gamma
        case_info = {
            "case_id": "legacy_B0",
            "case_sha256": "legacy",
            "registry_sha256": None,
            "case_family": "anchor",
            "case_scope": "original",
            "case_description": "Legacy hard-coded baseline",
        }
    payloads = [
        {
            "n": args.n,
            "depth": args.depth,
            "seed": args.seed_start + k,
            "duration": args.duration,
            "dt": args.dt,
            "sample_dt": args.sample_dt,
            "sigma_w": sigma_w,
            "A": A,
            "gamma": gamma,
            "activation": activation,
            "X": X,
            "y": y,
        }
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
    scientific_config = {
        "case_sha256": case_info["case_sha256"],
        "registry_sha256": case_info["registry_sha256"],
        "n": args.n,
        "depth": args.depth,
        "seed_start": args.seed_start,
        "seeds": args.seeds,
        "seed_ids": [args.seed_start + k for k in range(args.seeds)],
        "duration": args.duration,
        "dt": args.dt,
        "sample_dt": args.sample_dt,
        "sigma_w": sigma_w,
        "A": A,
        "gamma": gamma,
        "activation": activation,
        "X": X.tolist(),
        "y": y.tolist(),
        "pde_seal_sha256": pde_seal_sha256,
        "dynamics_sha256": dynamics_sha256,
    }
    scientific_config_sha256 = hashlib.sha256(
        json.dumps(
            scientific_config, sort_keys=True, separators=(",", ":")
        ).encode()
    ).hexdigest()
    metadata = {
        "role": "finite-network ensemble reference; never read by PDE drift",
        "model": "canonical fully dense residual network",
        "training": "ordinary Euclidean muP gradient flow",
        "n": args.n,
        "depth": args.depth,
        "seed_start": args.seed_start,
        "seeds": args.seeds,
        "duration": args.duration,
        "dt": args.dt,
        "sample_dt": args.sample_dt,
        "sigma_w": sigma_w,
        "A": A,
        "gamma": gamma,
        "activation": activation,
        "X": X.tolist(),
        "y": y.tolist(),
        "m": int(y.size),
        "d": int(X.shape[0]),
        "case_id": case_info["case_id"],
        "case_sha256": case_info["case_sha256"],
        "registry_sha256": case_info["registry_sha256"],
        "case_family": case_info.get("case_family"),
        "case_scope": case_info.get("case_scope"),
        "case_description": case_info.get("case_description"),
        "pde_seal": (
            os.fspath(Path(args.pde_seal).resolve())
            if args.pde_seal is not None
            else None
        ),
        "pde_seal_sha256": pde_seal_sha256,
        "dynamics_sha256": dynamics_sha256,
        "scientific_config_sha256": scientific_config_sha256,
        "config_sha256": scientific_config_sha256,
        "elapsed_seconds": elapsed,
    }
    output_dir = (
        Path(args.output_dir)
        if args.output_dir is not None
        else ROOT / "results" / "raw"
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    case_tag = case_info["case_id"]
    hash_tag = case_info["case_sha256"][:12]
    path = output_dir / (
        f"exact_{case_tag}_{hash_tag}_n{args.n}_L{args.depth}"
        f"_S{args.seeds}_seed{args.seed_start}"
        f"_dt{str(args.dt).replace('.', 'p')}"
        f"_T{str(args.duration).replace('.', 'p')}"
        f"_cfg{scientific_config_sha256[:12]}.npz"
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
    parser.add_argument("--sigma-w", type=float)
    parser.add_argument("--A", type=float)
    parser.add_argument("--gamma", type=float)
    parser.add_argument("--activation", choices=ACTIVATION_NAMES)
    parser.add_argument("--case-registry")
    parser.add_argument("--case-id")
    parser.add_argument("--output-dir")
    parser.add_argument("--pde-seal")
    return parser.parse_args()


if __name__ == "__main__":
    run(parse_args())
