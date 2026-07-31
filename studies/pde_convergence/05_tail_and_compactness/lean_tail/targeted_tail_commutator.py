"""Budget-capped parity-reduced Hermite tail diagnostic.

The script evolves only the highest requested odd Hermite truncation.  At a
checkpoint it projects that one state down the odd ladder and measures the
adjacent projection commutators

    Pi_low F_high(Y_high) - F_low(Pi_low Y_high).

This avoids evolving redundant low-order trajectories and targets the
high-to-low term that remains open in the convergence argument.
"""

from __future__ import annotations

import argparse
import dataclasses
import gc
import hashlib
import json
import math
from pathlib import Path
import sys
import time
from typing import Any, Iterable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
AUDIT_SOURCE = ROOT / "pde_proof_obligation_audit" / "source"
CANONICAL_SOURCE = ROOT / "activation_linearity_smoking_gun" / "source" / "src"
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
    project_state,
)
from dense_pde.operator_galerkin import (  # noqa: E402
    PDESpec,
    PDEState,
    _eval_hermite_basis,
    _multi_indices,
    _normal_hermite_tensor,
    _normal_sobol,
    initialize,
    vector_field,
)


PROTOCOL_PATH = (
    ROOT
    / "pde_proof_obligation_audit"
    / "protocol"
    / "preregistered_protocol.json"
)
ODD_DEGREES = (1, 3, 5, 7)


def _schedule(max_degree: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    if max_degree not in ODD_DEGREES:
        raise ValueError(f"max_degree must be one of {ODD_DEGREES}")
    full = _multi_indices(4, math.comb(max_degree + 4, 4))
    odd = tuple(index for index in full if sum(index) % 2 == 1)
    ends: list[int] = []
    for degree in ODD_DEGREES:
        if degree > max_degree:
            break
        ends.append(sum(sum(index) <= degree for index in odd))
    return odd, tuple(ends)


def _odd_family(
    template: PDESpec,
    *,
    max_degree: int,
    base_order: int,
) -> tuple[NestedQuadratureFamily, tuple[int, ...]]:
    indices, levels = _schedule(max_degree)
    full_count = math.comb(max_degree + 4, 4)
    full_indices = _multi_indices(4, full_count)
    odd_positions = np.asarray(
        [position for position, index in enumerate(full_indices) if sum(index) % 2],
        dtype=np.int64,
    )
    if len(indices) != levels[-1] or len(indices) != len(odd_positions):
        raise AssertionError("odd Hermite schedule is inconsistent")
    if template.fast_points % 2:
        raise ValueError("antithetic cubature requires even R")
    if template.fast_points // 2 < levels[-1]:
        raise ValueError(
            "R/2 must be at least the number of active odd modes "
            f"({levels[-1]})"
        )

    base_latent, base_weights = _normal_hermite_tensor(base_order, 4)
    raw_phi = _eval_hermite_basis(base_latent, indices)
    phi = _block_orthonormalize(
        raw_phi, base_weights, levels, center=False
    )

    half_full = _normal_sobol(
        template.fast_points // 2,
        full_count,
        template.quadrature_seed + 104729,
    )
    half = half_full[:, odd_positions]
    raw_epsilon = np.concatenate((half, -half), axis=0)
    fast_weights = np.full(
        template.fast_points, 1.0 / template.fast_points, dtype=float
    )
    epsilon = _block_orthonormalize(
        raw_epsilon, fast_weights, levels, center=True
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
    return (
        NestedQuadratureFamily(
            levels=levels,
            master_levels=levels,
            specs=specs,
            quadratures=quadratures,
            raw_epsilon=raw_epsilon,
            base_order=base_order,
        ),
        np.asarray([sum(index) for index in indices], dtype=np.int64),
    )


def _add_scaled(state: PDEState, direction: PDEState, scale: float) -> PDEState:
    return PDEState(
        B=state.B + scale * direction.B,
        a=state.a + scale * direction.a,
        c=state.c + scale * direction.c,
    )


def _midpoint_step(
    state: PDEState,
    dt: float,
    spec: PDESpec,
    quadrature: Any,
) -> PDEState:
    """Second-order step with a three-large-array peak."""

    first, fields = vector_field(state, spec, quadrature)
    del fields
    midpoint = _add_scaled(state, first, 0.5 * dt)
    del first
    gc.collect()
    second, fields = vector_field(midpoint, spec, quadrature)
    del fields, midpoint
    gc.collect()
    result = _add_scaled(state, second, dt)
    del second
    return result


def _normalized_observable_defect(
    left: PDEState,
    right: PDEState,
    state: PDEState,
    spec: PDESpec,
    quadrature: Any,
    protocol: dict[str, Any],
) -> dict[str, float]:
    left_obs = centered_observable_derivative(state, left, spec, quadrature)
    right_obs = centered_observable_derivative(state, right, spec, quadrature)
    defect = _observable_derivative_defect(left_obs, right_obs)
    f_scaled = float(np.linalg.norm(defect.left.f - defect.right.f)) / float(
        protocol["norms"]["S_f"]
    )
    gram_scaled = float(
        np.max(
            np.linalg.norm(
                (defect.left.grams - defect.right.grams).reshape(
                    defect.left.grams.shape[0], -1
                ),
                axis=1,
            )
        )
    ) / float(protocol["norms"]["S_G"])
    return {
        "observable_f_over_Sf": f_scaled,
        "observable_gram_over_SG": gram_scaled,
        "observable_max": max(f_scaled, gram_scaled),
    }


def _mode_energies(
    state: PDEState,
    velocity: PDEState,
    fields: Any,
    quadrature: Any,
) -> dict[str, np.ndarray]:
    wb = quadrature.base_weights
    wf = quadrature.fast_weights
    pcoef = np.einsum(
        "ip,i,lim->lpm", quadrature.phi, wb, fields.p, optimize=True
    )
    return {
        "c": np.einsum(
            "i,r,lirp,lirp->p",
            wb,
            wf,
            state.c,
            state.c,
            optimize=True,
        )
        / state.c.shape[0],
        "cdot": np.einsum(
            "i,r,lirp,lirp->p",
            wb,
            wf,
            velocity.c,
            velocity.c,
            optimize=True,
        )
        / velocity.c.shape[0],
        "hcoef": np.mean(
            np.sum(fields.hcoef * fields.hcoef, axis=2), axis=0
        ),
        "pcoef": np.mean(np.sum(pcoef * pcoef, axis=2), axis=0),
    }


def _shell_summary(
    energies: dict[str, np.ndarray], degrees: np.ndarray
) -> dict[str, np.ndarray]:
    maximum = int(np.max(degrees))
    shell_degrees = np.arange(1, maximum + 1, 2, dtype=np.int64)
    result: dict[str, np.ndarray] = {
        "degrees": shell_degrees,
        "mode_counts": np.asarray(
            [np.sum(degrees == degree) for degree in shell_degrees],
            dtype=np.int64,
        ),
    }
    for name, values in energies.items():
        totals = []
        effective = []
        maxima = []
        for degree in shell_degrees:
            shell = np.asarray(values[degrees == degree], dtype=float)
            total = float(np.sum(shell))
            totals.append(total)
            effective.append(
                0.0
                if total == 0.0
                else total * total / float(np.sum(shell * shell))
            )
            maxima.append(0.0 if total == 0.0 else float(np.max(shell) / total))
        result[f"{name}_norm"] = np.sqrt(np.asarray(totals))
        result[f"{name}_effective_modes"] = np.asarray(effective)
        result[f"{name}_max_energy_fraction"] = np.asarray(maxima)
    return result


def _adjacent_commutators(
    state: PDEState,
    family: NestedQuadratureFamily,
    protocol: dict[str, Any],
) -> tuple[dict[str, float], dict[str, np.ndarray], dict[str, np.ndarray]]:
    levels = family.levels
    high = levels[-1]
    high_spec = family.spec(high)
    high_q = family.quadrature(high)
    high_velocity, high_fields = vector_field(state, high_spec, high_q)
    energies = _mode_energies(state, high_velocity, high_fields, high_q)
    del high_fields
    shell = _shell_summary(
        energies,
        np.asarray(
            [sum(index) for index in high_q.multi_indices], dtype=np.int64
        ),
    )

    states: dict[int, PDEState] = {high: state}
    velocities: dict[int, PDEState] = {high: high_velocity}
    for level in reversed(levels[:-1]):
        states[level] = project_state(state, level)
        velocities[level], fields = vector_field(
            states[level], family.spec(level), family.quadrature(level)
        )
        del fields

    metrics: dict[str, float] = {}
    arrays: dict[str, np.ndarray] = {}
    for low, upper in zip(levels[:-1], levels[1:]):
        left = project_state(velocities[upper], low)
        right = velocities[low]
        defect = _velocity_defect(left, right, family.quadrature(low))
        tag = f"d{2 * levels.index(low) + 1}_to_d{2 * levels.index(upper) + 1}"
        metrics[f"{tag}_Bdot"] = defect.Bdot
        metrics[f"{tag}_adot"] = defect.adot
        metrics[f"{tag}_cdot"] = defect.cdot
        metrics[f"{tag}_total"] = defect.total
        metrics.update(
            {
                f"{tag}_{name}": value
                for name, value in _normalized_observable_defect(
                    left,
                    right,
                    states[low],
                    family.spec(low),
                    family.quadrature(low),
                    protocol,
                ).items()
            }
        )
        arrays[f"{tag}_Bdot_signed"] = left.B - right.B
        arrays[f"{tag}_adot_signed"] = left.a - right.a
        del left

    for mapping in (states, velocities):
        for level in tuple(mapping):
            if mapping[level] is not state:
                del mapping[level]
    del high_velocity
    gc.collect()
    return metrics, arrays, shell


def _parse_checkpoints(value: str) -> tuple[float, ...]:
    result = tuple(float(item) for item in value.split(","))
    if not result or result[0] < 0.0 or any(
        right <= left for left, right in zip(result, result[1:])
    ):
        raise argparse.ArgumentTypeError(
            "checkpoints must be strictly increasing and nonnegative"
        )
    return result


def run(args: argparse.Namespace) -> dict[str, np.ndarray]:
    protocol = json.loads(PROTOCOL_PATH.read_text())
    model = common._canonical_model(protocol)
    indices, levels = _schedule(args.max_degree)
    template = PDESpec(
        X=model["X"],
        y=model["y"],
        basis_size=len(indices),
        depth_nodes=args.N,
        base_points=args.base_order**4,
        fast_points=args.R,
        quadrature_seed=args.seed,
        sigma_w=model["sigma_w"],
        A=model["A"],
        gamma=model["gamma"],
        activation=model["activation"],
    )
    family, degrees = _odd_family(
        template, max_degree=args.max_degree, base_order=args.base_order
    )
    state = initialize(family.spec(levels[-1]), family.quadrature(levels[-1]))

    output: dict[str, Any] = {
        "checkpoints": np.asarray(args.checkpoints),
        "levels": np.asarray(levels, dtype=np.int64),
        "degrees": degrees,
    }
    records: dict[str, list[Any]] = {}
    current = 0.0
    tolerance = 128 * np.finfo(float).eps * max(1.0, args.checkpoints[-1])
    started = time.perf_counter()
    for checkpoint in args.checkpoints:
        while current < checkpoint - tolerance:
            step = min(args.dt, checkpoint - current)
            new_state = _midpoint_step(
                state,
                step,
                family.spec(levels[-1]),
                family.quadrature(levels[-1]),
            )
            del state
            state = new_state
            current += step
            gc.collect()

        metrics, signed, shell = _adjacent_commutators(
            state, family, protocol
        )
        for name, value in metrics.items():
            records.setdefault(name, []).append(value)
        for name, value in signed.items():
            records.setdefault(name, []).append(value)
        for name, value in shell.items():
            records.setdefault(f"shell_{name}", []).append(value)

    for name, values in records.items():
        output[name] = np.asarray(values)
    metadata = {
        "max_degree": int(args.max_degree),
        "active_odd_modes": int(levels[-1]),
        "full_modes_through_degree": math.comb(args.max_degree + 4, 4),
        "levels": list(levels),
        "seed": int(args.seed),
        "N": int(args.N),
        "R": int(args.R),
        "base_order": int(args.base_order),
        "M": int(args.base_order**4),
        "dt": float(args.dt),
        "integrator": "explicit midpoint",
        "checkpoints": list(args.checkpoints),
        "wall_seconds": time.perf_counter() - started,
        "protocol_sha256": hashlib.sha256(PROTOCOL_PATH.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "claim_scope": (
            "single-high-reference parity-reduced commutator diagnostic; "
            "not a convergence proof"
        ),
    }
    output["metadata_json"] = np.asarray(json.dumps(metadata, sort_keys=True))
    return {name: np.asarray(value) for name, value in output.items()}


def _summary(arrays: dict[str, np.ndarray]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "metadata": json.loads(str(arrays["metadata_json"])),
        "commutators": {},
        "shells": {},
    }
    for name in arrays:
        if name.endswith("_total"):
            tag = name[: -len("_total")]
            result["commutators"][tag] = {
                suffix: arrays[f"{tag}_{suffix}"].tolist()
                for suffix in (
                    "Bdot",
                    "adot",
                    "cdot",
                    "total",
                    "observable_f_over_Sf",
                    "observable_gram_over_SG",
                    "observable_max",
                )
            }
    for name in arrays:
        if name.startswith("shell_"):
            result["shells"][name[len("shell_") :]] = arrays[name].tolist()
    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-degree", type=int, choices=ODD_DEGREES, required=True)
    parser.add_argument("--seed", type=int, default=20260723)
    parser.add_argument("--N", type=int, default=1)
    parser.add_argument("--R", type=int, required=True)
    parser.add_argument("--base-order", type=int, required=True)
    parser.add_argument("--dt", type=float, default=0.025)
    parser.add_argument(
        "--checkpoints", type=_parse_checkpoints, default=(0.25,)
    )
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
