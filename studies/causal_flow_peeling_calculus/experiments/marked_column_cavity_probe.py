#!/usr/bin/env python3
"""Preregistered C1 marked-column cavity experiment.

The two copies differ only in one standardized column of the persistent top
source.  Forward and transpose actions always use the same matrix.  The JVP
mode differentiates the complete RK4 trajectory with ``torch.func.jvp``.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import platform
import sys
from pathlib import Path

import torch

from g2_reachable_gate_defect import (
    forward_backward,
    integrate,
    observables,
    seeded_state,
)


CHECKPOINTS = (0.0, 0.25, 0.5)
MARKED = 0


def clone_state(state):
    return tuple(value.clone() for value in state)


def normalized_l2(value):
    return torch.linalg.vector_norm(value).item() / math.sqrt(value.numel())


def normalized_fro(value):
    return torch.linalg.vector_norm(value).item() / math.sqrt(value.shape[0])


def power_operator_norm(value, iterations=30):
    """Deterministic power-iteration lower estimate and residual."""
    n = value.shape[1]
    if not bool(torch.any(value)):
        return 0.0, 0.0
    grid = torch.arange(1, n + 1, device=value.device, dtype=value.dtype)
    vector = torch.sin(grid * 0.7548776662466927)
    vector = vector / torch.linalg.vector_norm(vector)
    for _ in range(iterations):
        left = value @ vector
        right = value.T @ left
        scale = torch.linalg.vector_norm(right)
        if scale.item() == 0.0:
            return 0.0, 0.0
        vector = right / scale
    image = value @ vector
    sigma = torch.linalg.vector_norm(image)
    gram_image = value.T @ image
    residual = torch.linalg.vector_norm(
        gram_image - sigma.square() * vector
    ) / sigma.square().clamp_min(torch.finfo(value.dtype).tiny)
    return sigma.item(), residual.item()


def state_envelope(state):
    A, u, G1, G2 = state
    return max(
        normalized_l2(A),
        normalized_l2(u),
        normalized_fro(G1),
        normalized_fro(G2),
    )


def coupled_initial_state(width, trial, device, dtype):
    base = seeded_state(width, trial, 0.0, device, dtype)
    A, u, G1, G2 = base
    generator = torch.Generator(device=device)
    generator.manual_seed(99173 + 1000033 * width + 15485863 * trial)
    new_column = torch.randn(
        width, generator=generator, device=device, dtype=dtype
    )
    perturbed_G2 = G2.clone()
    perturbed_G2[:, MARKED] = new_column / math.sqrt(width)
    perturbed = (A.clone(), u.clone(), G1.clone(), perturbed_G2)
    old_column = math.sqrt(width) * G2[:, MARKED].clone()
    return clone_state(base), perturbed, old_column, new_column


def checkpoint_states(initial, dt):
    states = []
    state = clone_state(initial)
    previous = 0.0
    for checkpoint in CHECKPOINTS:
        state = integrate(state, checkpoint - previous, dt, 0.0)
        states.append(clone_state(state))
        previous = checkpoint
    return states


def replacement_row(
    base,
    perturbed,
    source_base,
    source_perturbed,
    old_column,
    new_column,
    width,
    trial,
    checkpoint,
):
    pred0, kernel0, fields0 = observables(base, 0.0)
    pred1, kernel1, fields1 = observables(perturbed, 0.0)
    # x1,z2,x2,z3,x3,b3,r2,b2,r1,b1
    x20, z30, b30, r20 = fields0[2], fields0[3], fields0[5], fields0[6]
    x21, z31, b31, r21 = fields1[2], fields1[3], fields1[5], fields1[6]

    delta_r2_bulk = r21 - r20
    delta_r2_bulk = delta_r2_bulk.clone()
    delta_r2_bulk[MARKED] = 0.0
    column_scale = normalized_l2(new_column - old_column)

    A0, u0, G10, G20 = base
    A1, u1, G11, G21 = perturbed
    _, _, source_G10, source_G20 = source_base
    _, _, source_G11, source_G21 = source_perturbed
    matrix_differences = {
        "G1_full": G11 - G10,
        "G2_full": G21 - G20,
        "G1_learned": (G11 - source_G11) - (G10 - source_G10),
        "G2_learned": (G21 - source_G21) - (G20 - source_G20),
    }

    row = {
        "kind": "replacement",
        "width": width,
        "trial": trial,
        "time": checkpoint,
        "column_delta_norm_n": column_scale,
        "marked_r2_abs": abs((r21[MARKED] - r20[MARKED]).item()),
        "marked_r2_over_column": abs(
            (r21[MARKED] - r20[MARKED]).item()
        ) / max(column_scale, 1e-30),
        "x2_diff_l2n": normalized_l2(x21 - x20),
        "z3_diff_l2n": normalized_l2(z31 - z30),
        "b3_diff_l2n": normalized_l2(b31 - b30),
        "u_diff_l2n": normalized_l2(u1 - u0),
        "A_diff_l2n": normalized_l2(A1 - A0),
        "r2_bulk_diff_l2n": normalized_l2(delta_r2_bulk),
        "predictor_abs_diff": abs(pred1 - pred0),
        "kernel_abs_diff": abs(kernel1 - kernel0),
        "base_envelope": state_envelope(base),
        "perturbed_envelope": state_envelope(perturbed),
        "all_finite": bool(
            all(torch.isfinite(value).all().item() for value in base + perturbed)
        ),
    }
    for name, difference in matrix_differences.items():
        operator, residual = power_operator_norm(difference)
        row[f"{name}_fro_over_sqrtn"] = normalized_fro(difference)
        row[f"{name}_operator_power"] = operator
        row[f"{name}_operator_residual"] = residual
    return row


def run_replacement(width, trial, device, dtype, dt):
    base0, perturbed0, old_column, new_column = coupled_initial_state(
        width, trial, device, dtype
    )
    source_base = clone_state(base0)
    source_perturbed = clone_state(perturbed0)
    base_states = checkpoint_states(base0, dt)
    perturbed_states = checkpoint_states(perturbed0, dt)
    rows = []
    with torch.no_grad():
        for checkpoint, base, perturbed in zip(
            CHECKPOINTS, base_states, perturbed_states
        ):
            rows.append(
                replacement_row(
                    base,
                    perturbed,
                    source_base,
                    source_perturbed,
                    old_column,
                    new_column,
                    width,
                    trial,
                    checkpoint,
                )
            )
    return rows


def trajectory_outputs(column, fixed_state, source_G2, dt):
    A0, u0, G10, G20 = fixed_state
    old_column = math.sqrt(column.numel()) * source_G2[:, MARKED]
    basis = torch.zeros_like(column)
    basis[MARKED] = 1.0
    initial_G2 = G20 + torch.outer(
        (column - old_column) / math.sqrt(column.numel()), basis
    )
    state = (A0, u0, G10, initial_G2)
    outputs = []
    previous = 0.0
    for checkpoint in CHECKPOINTS:
        state = integrate(state, checkpoint - previous, dt, 0.0)
        A, u, G1, G2 = state
        fields = forward_backward(state, 0.0)
        x2, z3, b3, r2 = fields[2], fields[3], fields[5], fields[6]
        mask = torch.ones_like(r2)
        mask[MARKED] = 0.0
        outputs.extend(
            (
                r2[MARKED],
                x2,
                z3,
                b3,
                u,
                A,
                r2 * mask,
                G1 - G10,
                G2 - initial_G2,
            )
        )
        previous = checkpoint
    return tuple(outputs)


def tangent_row(tangents, width, trial, direction, checkpoint):
    (
        marked_r2,
        x2,
        z3,
        b3,
        u,
        A,
        r2_bulk,
        G1_learned,
        G2_learned,
    ) = tangents
    row = {
        "kind": "jvp",
        "width": width,
        "trial": trial,
        "direction": direction,
        "time": checkpoint,
        "marked_r2_jvp_abs": abs(marked_r2.item()),
        "x2_jvp_l2n": normalized_l2(x2),
        "z3_jvp_l2n": normalized_l2(z3),
        "b3_jvp_l2n": normalized_l2(b3),
        "u_jvp_l2n": normalized_l2(u),
        "A_jvp_l2n": normalized_l2(A),
        "r2_bulk_jvp_l2n": normalized_l2(r2_bulk),
    }
    for name, value in (
        ("G1_learned_jvp", G1_learned),
        ("G2_learned_jvp", G2_learned),
    ):
        operator, residual = power_operator_norm(value)
        row[f"{name}_fro_over_sqrtn"] = normalized_fro(value)
        row[f"{name}_operator_power"] = operator
        row[f"{name}_operator_residual"] = residual
    return row


def run_jvp(width, trial, directions, device, dtype, dt):
    state = seeded_state(width, trial, 0.0, device, dtype)
    source_G2 = state[3].clone()
    standardized_column = math.sqrt(width) * source_G2[:, MARKED]
    generator = torch.Generator(device=device)
    generator.manual_seed(32452843 + 1000033 * width + 49999 * trial)
    rows = []
    for direction_index in range(directions):
        signs = torch.randint(
            0,
            2,
            (width,),
            generator=generator,
            device=device,
            dtype=torch.int64,
        ).to(dtype)
        tangent_column = 2.0 * signs - 1.0
        _, tangent_outputs = torch.func.jvp(
            lambda column: trajectory_outputs(column, state, source_G2, dt),
            (standardized_column,),
            (tangent_column,),
        )
        block = 9
        for checkpoint_index, checkpoint in enumerate(CHECKPOINTS):
            begin = checkpoint_index * block
            rows.append(
                tangent_row(
                    tangent_outputs[begin : begin + block],
                    width,
                    trial,
                    direction_index,
                    checkpoint,
                )
            )
        del tangent_outputs
    return rows


def source_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_csv(path, rows):
    if not rows:
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--widths", default="128,256,512,1024")
    parser.add_argument("--trials", default="0,1,2,3")
    parser.add_argument("--directions", type=int, default=2)
    parser.add_argument("--dt", type=float, default=1.0 / 1024.0)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=("float32", "float64"), default="float32")
    parser.add_argument(
        "--mode", choices=("replacement", "jvp", "both"), default="both"
    )
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    widths = [int(value) for value in args.widths.split(",") if value]
    trials = [int(value) for value in args.trials.split(",") if value]
    device = torch.device(args.device)
    dtype = torch.float32 if args.dtype == "float32" else torch.float64
    if device.type == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested but unavailable")
    torch.set_float32_matmul_precision("highest")

    replacement_rows = []
    jvp_rows = []
    for width in widths:
        for trial in trials:
            print(
                json.dumps(
                    {
                        "event": "start_cell",
                        "width": width,
                        "trial": trial,
                        "mode": args.mode,
                    }
                ),
                flush=True,
            )
            if args.mode in ("replacement", "both"):
                replacement_rows.extend(
                    run_replacement(width, trial, device, dtype, args.dt)
                )
            if args.mode in ("jvp", "both"):
                jvp_rows.extend(
                    run_jvp(
                        width,
                        trial,
                        args.directions,
                        device,
                        dtype,
                        args.dt,
                    )
                )
            if device.type == "cuda":
                torch.cuda.empty_cache()

    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    write_csv(output / "raw_replacement.csv", replacement_rows)
    write_csv(output / "raw_jvp.csv", jvp_rows)
    script_path = Path(__file__).resolve()
    dependency = script_path.with_name("g2_reachable_gate_defect.py")
    metadata = {
        "widths": widths,
        "trials": trials,
        "directions": args.directions,
        "checkpoints": CHECKPOINTS,
        "marked_column": MARKED,
        "dt": args.dt,
        "device": str(device),
        "dtype": args.dtype,
        "mode": args.mode,
        "torch": torch.__version__,
        "cuda_runtime": torch.version.cuda,
        "gpu": torch.cuda.get_device_name(device) if device.type == "cuda" else None,
        "python": platform.python_version(),
        "command": [sys.executable, *sys.argv],
        "script_sha256": source_hash(script_path),
        "dependency_sha256": source_hash(dependency),
        "replacement_rows": len(replacement_rows),
        "jvp_rows": len(jvp_rows),
    }
    (output / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps(metadata, indent=2), flush=True)


if __name__ == "__main__":
    main()
