"""Lean parity-aware generator diagnostics for the neural-PDE study.

This is intentionally a small diagnostic wrapper around the frozen scientific
implementation.  It does not alter the canonical vector field.  Its two jobs
are:

* ``even-shell``: verify the quadratic Hermite shell is symmetry-suppressed
  and check the earlier P=15<-35 warning at a chosen numerical resolution.
* ``odd-ladder``: compare the parity-matched complete-degree steps
  P=5->35 and P=35->126.

The fast Gaussian cubature can be paired under the exact Hermite-parity map
``epsilon_nu -> (-1)^|nu| epsilon_nu``.  That is a quadrature symmetry
correction for the canonical Gaussian law, not a change to the PDE.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
from pathlib import Path
import sys
import time
from typing import Any, Iterable, Sequence

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
AUDIT_SOURCE = ROOT / "pde_proof_obligation_audit" / "source"
CANONICAL_SOURCE = (
    ROOT / "activation_linearity_smoking_gun" / "source" / "src"
)
for source in (AUDIT_SOURCE, CANONICAL_SOURCE):
    if str(source) not in sys.path:
        sys.path.insert(0, str(source))

import run_study as common  # noqa: E402
from cross_p import (  # noqa: E402
    NestedQuadratureFamily,
    _block_orthonormalize,
    _observable_derivative_defect,
    _quadrature_record,
    _velocity_defect,
    centered_observable_derivative,
    lift_state,
    project_state,
    weighted_state_norm,
)
from dense_pde.operator_galerkin import (  # noqa: E402
    PDESpec,
    PDEState,
    _eval_hermite_basis,
    _multi_indices,
    _normal_hermite_tensor,
    _normal_sobol,
    initialize,
    observe,
    rk4_step,
    vector_field,
)


PROTOCOL_PATH = (
    ROOT
    / "pde_proof_obligation_audit"
    / "protocol"
    / "preregistered_protocol.json"
)


def _levels_for_mode(mode: str) -> tuple[tuple[int, ...], tuple[tuple[int, int], ...]]:
    if mode == "even-shell":
        return (5, 15, 35), ((5, 15), (15, 35), (5, 35))
    if mode == "odd-ladder":
        return (5, 35, 126), ((5, 35), (35, 126))
    raise ValueError(f"unknown mode: {mode}")


def _master_levels(maximum: int) -> tuple[int, ...]:
    schedule = (5, 15, 35, 70, 126)
    return tuple(value for value in schedule if value <= maximum)


def _parity_paired_family(
    template: PDESpec,
    levels: Sequence[int],
    *,
    base_order: int,
) -> NestedQuadratureFamily:
    levels = tuple(int(value) for value in levels)
    master_levels = _master_levels(max(levels))
    pmax = master_levels[-1]
    if template.fast_points % 2:
        raise ValueError("parity-paired fast cubature requires even R")

    latent_dim = template.X.shape[0] + 1
    base_latent, base_weights = _normal_hermite_tensor(base_order, latent_dim)
    indices = _multi_indices(latent_dim, pmax)
    raw_phi = _eval_hermite_basis(base_latent, indices)
    phi = _block_orthonormalize(
        raw_phi, base_weights, master_levels, center=False
    )

    half = _normal_sobol(
        template.fast_points // 2,
        pmax,
        template.quadrature_seed + 104729,
    )
    parity = np.asarray(
        [(-1.0) ** sum(index) for index in indices], dtype=float
    )
    raw_epsilon = np.concatenate((half, half * parity[None, :]), axis=0)
    fast_weights = np.full(
        template.fast_points, 1.0 / template.fast_points, dtype=float
    )
    epsilon = _block_orthonormalize(
        raw_epsilon, fast_weights, master_levels, center=True
    )

    specs: dict[int, PDESpec] = {}
    quadratures: dict[int, Any] = {}
    for level in levels:
        spec = dataclasses.replace(
            template,
            basis_size=level,
            base_points=base_latent.shape[0],
        )
        spec.validate()
        specs[level] = spec
        quadratures[level] = _quadrature_record(
            base_latent=base_latent,
            base_weights=base_weights,
            raw_phi=raw_phi[:, :level],
            phi=phi[:, :level],
            raw_epsilon=raw_epsilon[:, :level],
            epsilon=epsilon[:, :level],
            fast_weights=fast_weights,
            multi_indices=indices[:level],
        )
    return NestedQuadratureFamily(
        levels=levels,
        master_levels=master_levels,
        specs=specs,
        quadratures=quadratures,
        raw_epsilon=raw_epsilon,
        base_order=base_order,
    )


def _standard_family(
    template: PDESpec,
    levels: Sequence[int],
    *,
    base_order: int,
) -> NestedQuadratureFamily:
    from cross_p import build_nested_quadratures

    return build_nested_quadratures(
        template,
        levels=tuple(levels),
        base_order=base_order,
        master_levels=_master_levels(max(levels)),
    )


def _state_shell_norms(
    state: PDEState,
    velocity: PDEState,
    fields: Any,
    quadrature: Any,
) -> dict[str, np.ndarray]:
    degrees = np.asarray(
        [sum(index) for index in quadrature.multi_indices], dtype=np.int64
    )
    wb = quadrature.base_weights
    wf = quadrature.fast_weights
    max_degree = int(np.max(degrees))
    c_norm = np.zeros(max_degree + 1)
    cdot_norm = np.zeros(max_degree + 1)
    hcoef_norm = np.zeros(max_degree + 1)
    pcoef_norm = np.zeros(max_degree + 1)
    pcoef = np.einsum(
        "ip,i,lim->lpm",
        quadrature.phi,
        wb,
        fields.p,
        optimize=True,
    )
    for degree in range(max_degree + 1):
        mask = degrees == degree
        c_norm[degree] = np.sqrt(
            np.einsum(
                "i,r,lirp,lirp->",
                wb,
                wf,
                state.c[..., mask],
                state.c[..., mask],
                optimize=True,
            )
            / state.c.shape[0]
        )
        cdot_norm[degree] = np.sqrt(
            np.einsum(
                "i,r,lirp,lirp->",
                wb,
                wf,
                velocity.c[..., mask],
                velocity.c[..., mask],
                optimize=True,
            )
            / velocity.c.shape[0]
        )
        hcoef_norm[degree] = np.sqrt(
            np.mean(np.sum(fields.hcoef[:, mask, :] ** 2, axis=(1, 2)))
        )
        pcoef_norm[degree] = np.sqrt(
            np.mean(np.sum(pcoef[:, mask, :] ** 2, axis=(1, 2)))
        )
    return {
        "degrees": np.arange(max_degree + 1, dtype=np.int64),
        "c": c_norm,
        "cdot": cdot_norm,
        "hcoef": hcoef_norm,
        "pcoef": pcoef_norm,
    }


def _normalized_observable_defect(
    defect: Any, protocol: dict[str, Any]
) -> tuple[float, float, float]:
    delta_f = defect.left.f - defect.right.f
    delta_g = defect.left.grams - defect.right.grams
    f_scaled = float(np.linalg.norm(delta_f)) / float(
        protocol["norms"]["S_f"]
    )
    g_scaled = float(
        np.max(
            np.linalg.norm(
                delta_g.reshape(delta_g.shape[0], -1), axis=1
            )
        )
    ) / float(protocol["norms"]["S_G"])
    return f_scaled, g_scaled, max(f_scaled, g_scaled)


def _pair_diagnostic(
    low: int,
    high: int,
    states: dict[int, PDEState],
    velocities: dict[int, PDEState],
    family: NestedQuadratureFamily,
    protocol: dict[str, Any],
) -> dict[str, float]:
    low_state = states[low]
    high_state = states[high]
    low_spec = family.spec(low)
    high_spec = family.spec(high)
    low_q = family.quadrature(low)
    high_q = family.quadrature(high)

    projected_high_state = project_state(high_state, low)
    projected_high_velocity = project_state(velocities[high], low)
    low_from_high_velocity, _ = vector_field(
        projected_high_state, low_spec, low_q
    )
    feedback = _velocity_defect(
        projected_high_velocity, low_from_high_velocity, low_q
    )

    lifted_low = lift_state(low_state, high)
    lifted_velocity, _ = vector_field(lifted_low, high_spec, high_q)
    outgoing = PDEState(
        B=np.zeros_like(lifted_velocity.B),
        a=np.zeros_like(lifted_velocity.a),
        c=lifted_velocity.c.copy(),
    )
    outgoing.c[..., :low] = 0.0
    outgoing_norm = float(weighted_state_norm(outgoing, high_q))

    projected_observable = centered_observable_derivative(
        projected_high_state,
        projected_high_velocity,
        low_spec,
        low_q,
    )
    closed_observable = centered_observable_derivative(
        projected_high_state,
        low_from_high_velocity,
        low_spec,
        low_q,
    )
    observable_defect = _observable_derivative_defect(
        projected_observable, closed_observable
    )
    obs_f, obs_g, obs_max = _normalized_observable_defect(
        observable_defect, protocol
    )
    return {
        "R_back_Bdot": feedback.Bdot,
        "R_back_adot": feedback.adot,
        "R_back_cdot": feedback.cdot,
        "R_back_total": feedback.total,
        "R_out_lift": outgoing_norm,
        "back_observable_f_over_Sf": obs_f,
        "back_observable_gram_over_SG": obs_g,
        "back_observable_max": obs_max,
    }


def _observable_distance(
    left: Any, right: Any, protocol: dict[str, Any]
) -> float:
    return max(
        float(np.linalg.norm(left.f - right.f))
        / float(protocol["norms"]["S_f"]),
        float(
            np.max(
                np.linalg.norm(
                    (left.grams - right.grams).reshape(
                        left.grams.shape[0], -1
                    ),
                    axis=1,
                )
            )
        )
        / float(protocol["norms"]["S_G"]),
    )


def _parse_checkpoints(value: str) -> tuple[float, ...]:
    result = tuple(float(item) for item in value.split(","))
    if not result or result[0] < 0 or any(
        right <= left for left, right in zip(result, result[1:])
    ):
        raise argparse.ArgumentTypeError(
            "checkpoints must be strictly increasing nonnegative times"
        )
    return result


def run(args: argparse.Namespace) -> dict[str, np.ndarray]:
    protocol = json.loads(PROTOCOL_PATH.read_text())
    model = common._canonical_model(protocol)
    levels, pairs = _levels_for_mode(args.mode)
    latent_dim = model["X"].shape[0] + 1
    template = PDESpec(
        X=model["X"],
        y=model["y"],
        basis_size=max(levels),
        depth_nodes=args.N,
        base_points=args.base_order**latent_dim,
        fast_points=args.R,
        quadrature_seed=args.seed,
        sigma_w=model["sigma_w"],
        A=model["A"],
        gamma=model["gamma"],
        activation=model["activation"],
    )
    builder = (
        _parity_paired_family if args.parity_paired else _standard_family
    )
    family = builder(template, levels, base_order=args.base_order)
    states = {
        level: initialize(family.spec(level), family.quadrature(level))
        for level in levels
    }

    arrays: dict[str, Any] = {
        "checkpoints": np.asarray(args.checkpoints),
        "levels": np.asarray(levels, dtype=np.int64),
        "pairs": np.asarray(pairs, dtype=np.int64),
    }
    records: dict[str, list[Any]] = {}
    current = 0.0
    tolerance = 128 * np.finfo(float).eps * max(1.0, args.checkpoints[-1])
    started = time.perf_counter()
    for checkpoint in args.checkpoints:
        while current < checkpoint - tolerance:
            step = min(args.dt, checkpoint - current)
            for level in levels:
                states[level] = rk4_step(
                    states[level],
                    step,
                    family.spec(level),
                    family.quadrature(level),
                )
            current += step

        velocities: dict[int, PDEState] = {}
        fields: dict[int, Any] = {}
        observations: dict[int, Any] = {}
        for level in levels:
            velocities[level], fields[level] = vector_field(
                states[level],
                family.spec(level),
                family.quadrature(level),
            )
            observations[level] = observe(
                states[level],
                family.spec(level),
                family.quadrature(level),
                fields[level],
            )
            shell = _state_shell_norms(
                states[level],
                velocities[level],
                fields[level],
                family.quadrature(level),
            )
            for name, value in shell.items():
                records.setdefault(f"P{level}_shell_{name}", []).append(value)
            records.setdefault(f"P{level}_f", []).append(observations[level].f)
            records.setdefault(f"P{level}_loss", []).append(
                observations[level].loss
            )
            records.setdefault(f"P{level}_grams", []).append(
                observations[level].grams
            )

        for low, high in pairs:
            tag = f"P{low}_Q{high}"
            diagnostic = _pair_diagnostic(
                low, high, states, velocities, family, protocol
            )
            for name, value in diagnostic.items():
                records.setdefault(f"{tag}_{name}", []).append(value)
            records.setdefault(f"{tag}_observable_distance", []).append(
                _observable_distance(
                    observations[low], observations[high], protocol
                )
            )

    for name, values in records.items():
        arrays[name] = np.asarray(values)
    wall_seconds = time.perf_counter() - started
    metadata = {
        "mode": args.mode,
        "parity_paired": bool(args.parity_paired),
        "seed": int(args.seed),
        "N": int(args.N),
        "R": int(args.R),
        "base_order": int(args.base_order),
        "M": int(args.base_order**latent_dim),
        "dt": float(args.dt),
        "checkpoints": list(args.checkpoints),
        "levels": list(levels),
        "pairs": [list(pair) for pair in pairs],
        "master_levels": list(family.master_levels),
        "wall_seconds": wall_seconds,
        "protocol_sha256": hashlib.sha256(PROTOCOL_PATH.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(
            Path(__file__).read_bytes()
        ).hexdigest(),
        "claim_scope": (
            "targeted diagnostic; not a preregistered full-gate certificate"
        ),
    }
    arrays["metadata_json"] = np.asarray(
        json.dumps(metadata, sort_keys=True)
    )
    return {name: np.asarray(value) for name, value in arrays.items()}


def _summary(arrays: dict[str, np.ndarray]) -> dict[str, Any]:
    metadata = json.loads(str(arrays["metadata_json"]))
    result: dict[str, Any] = {"metadata": metadata, "pairs": {}}
    for low, high in np.asarray(arrays["pairs"], dtype=int):
        tag = f"P{low}_Q{high}"
        result["pairs"][tag] = {
            "R_back_total": arrays[f"{tag}_R_back_total"].tolist(),
            "R_out_lift": arrays[f"{tag}_R_out_lift"].tolist(),
            "back_observable_max": arrays[
                f"{tag}_back_observable_max"
            ].tolist(),
            "observable_distance": arrays[
                f"{tag}_observable_distance"
            ].tolist(),
        }
    result["shells"] = {}
    for level in np.asarray(arrays["levels"], dtype=int):
        result["shells"][f"P{level}"] = {
            name: arrays[f"P{level}_shell_{name}"].tolist()
            for name in ("degrees", "c", "cdot", "hcoef", "pcoef")
        }
    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("even-shell", "odd-ladder"))
    parser.add_argument("--seed", type=int, default=20260723)
    parser.add_argument("--N", type=int, default=4)
    parser.add_argument("--R", type=int, default=128)
    parser.add_argument("--base-order", type=int, default=5)
    parser.add_argument("--dt", type=float, default=0.04)
    parser.add_argument(
        "--checkpoints", type=_parse_checkpoints, default=(0.25, 0.5)
    )
    parser.add_argument("--parity-paired", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    arrays = run(args)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(args.output, **arrays)
    print(json.dumps(_summary(arrays), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
