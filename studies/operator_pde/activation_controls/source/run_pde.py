#!/usr/bin/env python3
"""Run one operator-Galerkin PDE characteristic discretization."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from dense_pde.operator_galerkin import (  # noqa: E402
    PDESpec,
    PDEState,
    build_hybrid_quadrature,
    build_quadrature,
    build_tensor_quadrature,
    heun_step,
    initialize,
    observe,
    rk4_step,
)
from activations import ACTIVATION_NAMES  # noqa: E402
from study_cases import case_metadata, load_case  # noqa: E402


def _tag(value: float) -> str:
    return f"{value:g}".replace(".", "p").replace("-", "m")


def _array_sha256(array: np.ndarray) -> str:
    contiguous = np.ascontiguousarray(array)
    digest = hashlib.sha256()
    digest.update(str(contiguous.dtype).encode())
    digest.update(np.asarray(contiguous.shape, dtype=np.int64).tobytes())
    digest.update(contiguous.tobytes())
    return digest.hexdigest()


def _file_sha256(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def run(args: argparse.Namespace) -> Path:
    if args.case_id is not None:
        if args.case_registry is None:
            raise ValueError("--case-id requires --case-registry")
        case = load_case(args.case_registry, args.case_id)
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
        case_info = case_metadata(case)
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
            "X": X.tolist(),
            "y": y.tolist(),
            "m": int(y.size),
            "d": int(X.shape[0]),
            "activation": activation,
            "sigma_w": sigma_w,
            "A": A,
            "gamma": gamma,
        }
    if args.quadrature in ("gauss-hermite", "hybrid"):
        base_points = args.base_order ** (X.shape[0] + 1)
        fast_points = (
            args.fast_order ** args.P
            if args.quadrature == "gauss-hermite"
            else args.R
        )
    else:
        base_points = args.M
        fast_points = args.R
    spec = PDESpec(
        X=X,
        y=y,
        basis_size=args.P,
        depth_nodes=args.N,
        base_points=base_points,
        fast_points=fast_points,
        quadrature_seed=args.seed,
        sigma_w=sigma_w,
        A=A,
        gamma=gamma,
        activation=activation,
    )
    if args.quadrature == "gauss-hermite":
        quadrature = build_tensor_quadrature(
            spec,
            base_order=args.base_order,
            fast_order=args.fast_order,
        )
    elif args.quadrature == "hybrid":
        quadrature = build_hybrid_quadrature(
            spec,
            base_order=args.base_order,
        )
    else:
        quadrature = build_quadrature(spec)
    quadrature_hashes = {
        "base_latent_sha256": _array_sha256(quadrature.base_latent),
        "base_weights_sha256": _array_sha256(quadrature.base_weights),
        "phi_sha256": _array_sha256(quadrature.phi),
        "epsilon_sha256": _array_sha256(quadrature.epsilon),
        "fast_weights_sha256": _array_sha256(quadrature.fast_weights),
    }
    static_compiler = {
        "quadrature": args.quadrature,
        "base_order": (
            args.base_order
            if args.quadrature in ("gauss-hermite", "hybrid")
            else None
        ),
        "fast_order": (
            args.fast_order if args.quadrature == "gauss-hermite" else None
        ),
        "basis_size_P": spec.basis_size,
        "depth_nodes_N": spec.depth_nodes,
        "base_quadrature_M": spec.base_points,
        "fast_quadrature_R": spec.fast_points,
        "quadrature_seed": spec.quadrature_seed,
        "sigma_w": spec.sigma_w,
        "A": spec.A,
        "gamma": spec.gamma,
        "activation": spec.activation,
        "X": spec.X.tolist(),
        "y": spec.y.tolist(),
        "case_id": case_info["case_id"],
        "case_sha256": case_info["case_sha256"],
        "registry_sha256": case_info["registry_sha256"],
        "multi_indices": [list(a) for a in quadrature.multi_indices],
        **quadrature_hashes,
    }
    static_blob = json.dumps(
        static_compiler, sort_keys=True, separators=(",", ":")
    )
    static_compiler_sha256 = hashlib.sha256(static_blob.encode()).hexdigest()
    if args.restart_from is None:
        state = initialize(spec, quadrature)
        start_time = 0.0
        restart_source_sha256 = None
    else:
        restart_source_sha256 = _file_sha256(args.restart_from)
        restart = np.load(args.restart_from)
        source_metadata = json.loads(str(restart["metadata_json"]))
        source_static_hash = source_metadata.get("static_compiler_sha256")
        if source_static_hash is not None:
            if source_static_hash != static_compiler_sha256:
                raise ValueError(
                    "restart static compiler/quadrature hash mismatch"
                )
        else:
            # Backward-compatible strict check for pilot traces written
            # before the byte hashes were added.
            for key in (
                "quadrature",
                "basis_size_P",
                "depth_nodes_N",
                "base_quadrature_M",
                "fast_quadrature_R",
                "quadrature_seed",
                "sigma_w",
                "A",
                "gamma",
                "X",
                "y",
                "multi_indices",
            ):
                if source_metadata.get(key) != static_compiler[key]:
                    raise ValueError(
                        f"restart static field mismatch for {key}"
                    )
        state = PDEState(
            B=restart["final_B"].copy(),
            a=restart["final_a"].copy(),
            c=restart["final_c"].copy(),
        )
        expected_shape = (
            spec.depth_nodes,
            spec.base_points,
            spec.fast_points,
            spec.basis_size,
        )
        if state.c.shape != expected_shape:
            raise ValueError(
                f"restart c shape {state.c.shape} != {expected_shape}"
            )
        if state.B.shape != (spec.base_points, spec.X.shape[0]):
            raise ValueError("restart B shape mismatch")
        if state.a.shape != (spec.base_points,):
            raise ValueError("restart a shape mismatch")
        start_time = float(restart["times"][-1])
    steps = int(round(args.duration / args.dt))
    sample_stride = int(round(args.sample_dt / args.dt))
    if abs(steps * args.dt - args.duration) > 1e-12:
        raise ValueError("duration must be an integer multiple of dt")
    if sample_stride < 1 or abs(sample_stride * args.dt - args.sample_dt) > 1e-12:
        raise ValueError("sample_dt must be a positive integer multiple of dt")
    if steps % sample_stride:
        raise ValueError("duration must be an integer multiple of sample_dt")
    samples = steps // sample_stride + 1

    times = np.empty(samples)
    f = np.empty((samples, y.size))
    loss = np.empty(samples)
    grams = np.empty((samples, spec.depth_nodes + 1, y.size, y.size))
    theta = np.empty((samples, y.size, y.size))
    theta_min = np.empty(samples)
    residual = np.empty(samples)
    loss_dot = np.empty(samples)
    projected_energy = np.empty((samples, spec.depth_nodes, y.size))

    started = time.perf_counter()
    sample_index = 0
    for step in range(steps + 1):
        if step % sample_stride == 0:
            obs = observe(state, spec, quadrature)
            times[sample_index] = start_time + step * args.dt
            f[sample_index] = obs.f
            loss[sample_index] = obs.loss
            grams[sample_index] = obs.grams
            theta[sample_index] = obs.theta
            theta_min[sample_index] = obs.theta_min
            residual[sample_index] = obs.residual_norm
            loss_dot[sample_index] = obs.loss_dot
            projected_energy[sample_index] = obs.projected_energy
            sample_index += 1
        if step < steps:
            stepper = rk4_step if args.integrator == "rk4" else heun_step
            state = stepper(state, args.dt, spec, quadrature)

    elapsed = time.perf_counter() - started
    scientific_config = {
        "static_compiler_sha256": static_compiler_sha256,
        "integrator": args.integrator,
        "duration": args.duration,
        "start_time": start_time,
        "end_time": start_time + args.duration,
        "dt": args.dt,
        "sample_dt": args.sample_dt,
        "restart_source_sha256": restart_source_sha256,
    }
    scientific_config_sha256 = hashlib.sha256(
        json.dumps(
            scientific_config, sort_keys=True, separators=(",", ":")
        ).encode()
    ).hexdigest()
    config = {
        "model": "continuous-depth dense Euclidean-muP operator-Galerkin PDE",
        "solver": (
            "weighted Sobol/Hermite characteristics + "
            + args.integrator.upper()
        ),
        "integrator": args.integrator,
        "quadrature": args.quadrature,
        "base_order": (
            args.base_order
            if args.quadrature in ("gauss-hermite", "hybrid")
            else None
        ),
        "fast_order": args.fast_order if args.quadrature == "gauss-hermite" else None,
        "actual_width_independent_pde_run": True,
        "contains_dense_network_weight_matrix": False,
        "basis_size_P": spec.basis_size,
        "depth_nodes_N": spec.depth_nodes,
        "base_quadrature_M": spec.base_points,
        "fast_quadrature_R": spec.fast_points,
        "quadrature_seed": spec.quadrature_seed,
        "duration": args.duration,
        "start_time": start_time,
        "end_time": start_time + args.duration,
        "restart_from": (
            os.fspath(Path(args.restart_from).resolve())
            if args.restart_from is not None
            else None
        ),
        "restart_source_sha256": restart_source_sha256,
        "dt": args.dt,
        "sample_dt": args.sample_dt,
        "sigma_w": spec.sigma_w,
        "A": spec.A,
        "gamma": spec.gamma,
        "activation": spec.activation,
        "X": X.tolist(),
        "y": y.tolist(),
        "case_id": case_info["case_id"],
        "case_sha256": case_info["case_sha256"],
        "registry_sha256": case_info["registry_sha256"],
        "case_family": case_info.get("case_family"),
        "case_scope": case_info.get("case_scope"),
        "case_description": case_info.get("case_description"),
        "source_dimension_per_depth": int(
            X.shape[0] + 1 + 2 * spec.basis_size
        ),
        "dynamic_characteristic_scalars": int(
            state.B.size + state.a.size + state.c.size
        ),
        "elapsed_seconds": elapsed,
        "raw_basis_gram_error": quadrature.raw_basis_gram_error,
        "raw_basis_min_eigenvalue": quadrature.raw_basis_min_eigenvalue,
        "raw_basis_max_eigenvalue": quadrature.raw_basis_max_eigenvalue,
        "raw_basis_condition": quadrature.raw_basis_condition,
        "whitened_basis_gram_error": quadrature.whitened_basis_gram_error,
        "fast_mean_error": quadrature.fast_mean_error,
        "raw_fast_min_eigenvalue": quadrature.raw_fast_min_eigenvalue,
        "raw_fast_max_eigenvalue": quadrature.raw_fast_max_eigenvalue,
        "raw_fast_condition": quadrature.raw_fast_condition,
        "fast_cov_error": quadrature.fast_cov_error,
        "multi_indices": [list(a) for a in quadrature.multi_indices],
        **quadrature_hashes,
        "static_compiler_sha256": static_compiler_sha256,
        "scientific_config_sha256": scientific_config_sha256,
    }
    config["config_sha256"] = scientific_config_sha256

    output_dir = (
        Path(args.output_dir)
        if args.output_dir is not None
        else ROOT / "results" / "raw"
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    case_tag = case_info["case_id"]
    hash_tag = case_info["case_sha256"][:12]
    name = (
        f"pde_{case_tag}_{hash_tag}_"
        f"{'GH' if args.quadrature == 'gauss-hermite' else ('HYBRID' if args.quadrature == 'hybrid' else 'QMC')}"
        f"_P{args.P}_N{args.N}_M{spec.base_points}_R{spec.fast_points}"
        f"_s{args.seed}_dt{_tag(args.dt)}_T{_tag(args.duration)}"
        f"_cfg{scientific_config_sha256[:12]}.npz"
    )
    if args.integrator != "rk4":
        name = name.replace(".npz", f"_{args.integrator.upper()}.npz")
    if start_time:
        name = name.replace(
            ".npz",
            f"_from{_tag(start_time)}_to{_tag(start_time + args.duration)}.npz",
        )
    path = output_dir / name
    partial = path.with_suffix(path.suffix + ".partial")
    with partial.open("wb") as handle:
        np.savez_compressed(
            handle,
            times=times,
            f=f,
            loss=loss,
            grams=grams,
            theta=theta,
            theta_min=theta_min,
            residual_norm=residual,
            loss_dot=loss_dot,
            projected_energy=projected_energy,
            final_B=state.B,
            final_a=state.a,
            final_c=state.c,
            metadata_json=np.array(
                json.dumps(config, sort_keys=True, separators=(",", ":"))
            ),
        )
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(partial, path)
    print(
        json.dumps(
            {
                "path": os.fspath(path),
                "elapsed_seconds": elapsed,
                "initial_loss": float(loss[0]),
                "final_loss": float(loss[-1]),
                "min_theta": float(np.min(theta_min)),
                "min_projected_energy": float(np.min(projected_energy)),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--P", type=int, default=5)
    parser.add_argument("--N", type=int, default=8)
    parser.add_argument("--M", type=int, default=64)
    parser.add_argument("--R", type=int, default=16)
    parser.add_argument(
        "--quadrature",
        choices=("sobol", "gauss-hermite", "hybrid"),
        default="sobol",
    )
    parser.add_argument("--base-order", type=int, default=3)
    parser.add_argument("--fast-order", type=int, default=3)
    parser.add_argument("--seed", type=int, default=20260723)
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
    parser.add_argument(
        "--integrator",
        choices=("rk4", "heun"),
        default="rk4",
    )
    parser.add_argument("--restart-from")
    return parser.parse_args()


if __name__ == "__main__":
    run(parse_args())
