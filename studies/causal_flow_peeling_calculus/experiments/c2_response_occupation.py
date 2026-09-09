#!/usr/bin/env python3
"""C2: preregistered response-weighted full-trajectory JVP audit.

This file implements only the finite D=3 model recorded in the C2 lock.
The tangent-linear system is the exact directional derivative of the full
primal ODE and is advanced at every RK4 stage.  It deliberately retains the
locked square-exponential diagnostics even though the post-lock analytic
caveat shows their annealed expectations are infinite.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import os
import platform
import sys
import time
from pathlib import Path
from typing import Iterable

os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
import torch


CHECKPOINTS = (0.0, 0.25, 0.5)
LAMBDAS = (0.0, 0.05, 0.10, 0.20)
MARKED = 0
MODEL_ROOT_SEED = 20260824
BOOTSTRAP_ROOT_SEED = 20260825
SHUFFLE_ROOT_SEED = 20260826
N_SHUFFLES = 32
PRIMARY_FIELDS = ("r2", "b2")
ALL_FIELDS = ("r2", "b2", "z2", "x2")

State = tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bmv(matrix: torch.Tensor, vector: torch.Tensor) -> torch.Tensor:
    return torch.bmm(matrix, vector.unsqueeze(-1)).squeeze(-1)


def outer(left: torch.Tensor, right: torch.Tensor) -> torch.Tensor:
    return left.unsqueeze(-1) * right.unsqueeze(-2)


def phi(value: torch.Tensor) -> torch.Tensor:
    return torch.atan(value)


def dphi(value: torch.Tensor) -> torch.Tensor:
    return torch.reciprocal(1.0 + value.square())


def ddphi(value: torch.Tensor) -> torch.Tensor:
    denominator = 1.0 + value.square()
    return -2.0 * value / denominator.square()


def forward_fields(state: State) -> dict[str, torch.Tensor]:
    A, u, G1, G2 = state
    x1 = phi(u)
    z2 = bmv(G1, x1)
    x2 = phi(z2)
    z3 = bmv(G2, x2)
    x3 = phi(z3)
    p3 = dphi(z3)
    b3 = A * p3
    r2 = bmv(G2.transpose(1, 2), b3)
    p2 = dphi(z2)
    b2 = p2 * r2
    r1 = bmv(G1.transpose(1, 2), b2)
    p1 = dphi(u)
    b1 = p1 * r1
    return {
        "x1": x1,
        "z2": z2,
        "x2": x2,
        "z3": z3,
        "x3": x3,
        "p3": p3,
        "b3": b3,
        "r2": r2,
        "p2": p2,
        "b2": b2,
        "r1": r1,
        "p1": p1,
        "b1": b1,
    }


def tangent_fields(
    state: State, tangent: State, fields: dict[str, torch.Tensor]
) -> dict[str, torch.Tensor]:
    A, u, G1, G2 = state
    dA, du, dG1, dG2 = tangent
    x1 = fields["x1"]
    z2 = fields["z2"]
    x2 = fields["x2"]
    z3 = fields["z3"]
    b3 = fields["b3"]
    r2 = fields["r2"]
    b2 = fields["b2"]
    r1 = fields["r1"]

    dx1 = fields["p1"] * du
    dz2 = bmv(dG1, x1) + bmv(G1, dx1)
    dx2 = fields["p2"] * dz2
    dz3 = bmv(dG2, x2) + bmv(G2, dx2)
    dx3 = fields["p3"] * dz3
    db3 = dA * fields["p3"] + A * ddphi(z3) * dz3
    dr2 = bmv(dG2.transpose(1, 2), b3) + bmv(
        G2.transpose(1, 2), db3
    )
    db2 = ddphi(z2) * dz2 * r2 + fields["p2"] * dr2
    dr1 = bmv(dG1.transpose(1, 2), b2) + bmv(
        G1.transpose(1, 2), db2
    )
    db1 = ddphi(u) * du * r1 + fields["p1"] * dr1
    return {
        "x1": dx1,
        "z2": dz2,
        "x2": dx2,
        "z3": dz3,
        "x3": dx3,
        "b3": db3,
        "r2": dr2,
        "b2": db2,
        "r1": dr1,
        "b1": db1,
    }


def rhs_pair(state: State, tangent: State) -> tuple[State, State]:
    fields = forward_fields(state)
    dfields = tangent_fields(state, tangent, fields)
    n = state[0].shape[-1]
    primal_rhs = (
        fields["x3"],
        fields["b1"],
        outer(fields["b2"], fields["x1"]) / n,
        outer(fields["b3"], fields["x2"]) / n,
    )
    tangent_rhs = (
        dfields["x3"],
        dfields["b1"],
        (
            outer(dfields["b2"], fields["x1"])
            + outer(fields["b2"], dfields["x1"])
        )
        / n,
        (
            outer(dfields["b3"], fields["x2"])
            + outer(fields["b3"], dfields["x2"])
        )
        / n,
    )
    return primal_rhs, tangent_rhs


def rhs_primal(state: State) -> State:
    fields = forward_fields(state)
    n = state[0].shape[-1]
    return (
        fields["x3"],
        fields["b1"],
        outer(fields["b2"], fields["x1"]) / n,
        outer(fields["b3"], fields["x2"]) / n,
    )


def axpy(values: State, increments: State, scale: float) -> State:
    return tuple(x + scale * dx for x, dx in zip(values, increments))  # type: ignore[return-value]


def rk4_pair(state: State, tangent: State, dt: float) -> tuple[State, State]:
    k1, l1 = rhs_pair(state, tangent)
    k2, l2 = rhs_pair(axpy(state, k1, 0.5 * dt), axpy(tangent, l1, 0.5 * dt))
    k3, l3 = rhs_pair(axpy(state, k2, 0.5 * dt), axpy(tangent, l2, 0.5 * dt))
    k4, l4 = rhs_pair(axpy(state, k3, dt), axpy(tangent, l3, dt))
    next_state = tuple(
        x + (dt / 6.0) * (a + 2.0 * b + 2.0 * c + d)
        for x, a, b, c, d in zip(state, k1, k2, k3, k4)
    )
    next_tangent = tuple(
        x + (dt / 6.0) * (a + 2.0 * b + 2.0 * c + d)
        for x, a, b, c, d in zip(tangent, l1, l2, l3, l4)
    )
    return next_state, next_tangent  # type: ignore[return-value]


def rk4_primal(state: State, dt: float) -> State:
    k1 = rhs_primal(state)
    k2 = rhs_primal(axpy(state, k1, 0.5 * dt))
    k3 = rhs_primal(axpy(state, k2, 0.5 * dt))
    k4 = rhs_primal(axpy(state, k3, dt))
    return tuple(
        x + (dt / 6.0) * (a + 2.0 * b + 2.0 * c + d)
        for x, a, b, c, d in zip(state, k1, k2, k3, k4)
    )  # type: ignore[return-value]


def max_abs(values: Iterable[torch.Tensor]) -> torch.Tensor:
    result = None
    for value in values:
        current = value.abs().reshape(value.shape[0], -1).max(dim=1).values
        result = current if result is None else torch.maximum(result, current)
    assert result is not None
    return result


def measurement(state: State, tangent: State) -> dict[str, torch.Tensor]:
    fields = forward_fields(state)
    dfields = tangent_fields(state, tangent, fields)
    return {
        "r2": fields["r2"],
        "V_r2": dfields["r2"],
        "V_b2": dfields["b2"],
        "V_z2": dfields["z2"],
        "V_x2": dfields["x2"],
        "derived_max": max_abs(tuple(fields.values()) + tuple(dfields.values())),
    }


def primal_measurement(state: State) -> dict[str, torch.Tensor]:
    fields = forward_fields(state)
    return {name: fields[name] for name in ALL_FIELDS}


def integrate_pair(
    initial: State, tangent: State, dt: float
) -> tuple[list[dict[str, torch.Tensor]], torch.Tensor]:
    total_steps_float = CHECKPOINTS[-1] / dt
    total_steps = int(round(total_steps_float))
    if abs(total_steps - total_steps_float) > 1e-12:
        raise ValueError("dt must exactly divide the final checkpoint")
    checkpoint_steps = {int(round(t / dt)): t for t in CHECKPOINTS}
    state = tuple(x.clone() for x in initial)
    direction = tuple(x.clone() for x in tangent)
    envelope = max_abs(state + direction)
    outputs: list[dict[str, torch.Tensor]] = []
    for step in range(total_steps + 1):
        if step in checkpoint_steps:
            item = measurement(state, direction)
            item["time"] = torch.tensor(
                checkpoint_steps[step], device=state[0].device, dtype=torch.float64
            )
            outputs.append(item)
            envelope = torch.maximum(envelope, item["derived_max"])
        if step < total_steps:
            state, direction = rk4_pair(state, direction, dt)
            envelope = torch.maximum(envelope, max_abs(state + direction))
    return outputs, envelope


def integrate_primal_checkpoints(
    initial: State, dt: float
) -> list[dict[str, torch.Tensor]]:
    total_steps_float = CHECKPOINTS[-1] / dt
    total_steps = int(round(total_steps_float))
    if abs(total_steps - total_steps_float) > 1e-12:
        raise ValueError("dt must exactly divide the final checkpoint")
    checkpoint_steps = {int(round(t / dt)): t for t in CHECKPOINTS}
    state = tuple(x.clone() for x in initial)
    outputs: list[dict[str, torch.Tensor]] = []
    for step in range(total_steps + 1):
        if step in checkpoint_steps:
            item = primal_measurement(state)
            item["time"] = torch.tensor(
                checkpoint_steps[step], device=state[0].device, dtype=torch.float64
            )
            outputs.append(item)
        if step < total_steps:
            state = rk4_primal(state, dt)
    return outputs


def model_seed(width: int, replicate: int) -> int:
    return MODEL_ROOT_SEED + 1_000_003 * width + 7_919 * replicate


def direction_seed(width: int, replicate: int) -> int:
    return MODEL_ROOT_SEED + 32452843 + 1_000_033 * width + 49_999 * replicate


def shuffle_seed(width: int, replicate: int, time_index: int) -> int:
    return (
        SHUFFLE_ROOT_SEED
        + 15_485_863 * width
        + 32452843 * replicate
        + 49999 * time_index
    )


def canonical_batch(
    width: int, replicates: list[int], device: torch.device
) -> tuple[State, State, list[dict[str, int]]]:
    states: list[State] = []
    tangents: list[State] = []
    seed_rows = []
    scale = 1.0 / math.sqrt(width)
    for replicate in replicates:
        generator = torch.Generator(device=device)
        mseed = model_seed(width, replicate)
        generator.manual_seed(mseed)
        A = torch.randn(width, generator=generator, device=device, dtype=torch.float64)
        u = torch.randn(width, generator=generator, device=device, dtype=torch.float64)
        G1 = (
            torch.randn(
                (width, width), generator=generator, device=device, dtype=torch.float64
            )
            * scale
        )
        G2 = (
            torch.randn(
                (width, width), generator=generator, device=device, dtype=torch.float64
            )
            * scale
        )

        dgenerator = torch.Generator(device=device)
        dseed = direction_seed(width, replicate)
        dgenerator.manual_seed(dseed)
        h = torch.randn(
            width, generator=dgenerator, device=device, dtype=torch.float64
        )
        direction = h / torch.linalg.vector_norm(h)
        dA = torch.zeros_like(A)
        du = torch.zeros_like(u)
        dG1 = torch.zeros_like(G1)
        dG2 = torch.zeros_like(G2)
        dG2[:, MARKED] = direction
        states.append((A, u, G1, G2))
        tangents.append((dA, du, dG1, dG2))
        seed_rows.append(
            {
                "width": width,
                "replicate": replicate,
                "model_seed": mseed,
                "direction_seed": dseed,
            }
        )

    def stack(component: int, collection: list[State]) -> torch.Tensor:
        return torch.stack([item[component] for item in collection], dim=0)

    state_batch: State = tuple(stack(i, states) for i in range(4))  # type: ignore[assignment]
    tangent_batch: State = tuple(stack(i, tangents) for i in range(4))  # type: ignore[assignment]
    return state_batch, tangent_batch, seed_rows


def cast_state(state: State, dtype: torch.dtype) -> State:
    return tuple(value.to(dtype=dtype) for value in state)  # type: ignore[return-value]


def cpu_measurements(
    measurements: list[dict[str, torch.Tensor]]
) -> list[dict[str, torch.Tensor]]:
    return [
        {
            key: value.detach().to(device="cpu", dtype=torch.float64)
            for key, value in item.items()
        }
        for item in measurements
    ]


def safe_ratio(numerator: float, denominator: float) -> float:
    if denominator == 0.0:
        return 0.0 if numerator == 0.0 else math.inf
    return numerator / denominator


def contribution_metrics(
    r2: torch.Tensor,
    response: torch.Tensor,
    lam: float,
    permutations: list[torch.Tensor],
) -> tuple[dict[str, float], list[dict[str, float]]]:
    r = r2[1:].to(torch.float64)
    v2 = response[1:].to(torch.float64).square()
    weights = torch.exp(lam * r.square())
    contributions = weights * v2
    m_value = contributions.sum().item()
    m0 = v2.sum().item()
    w_sum = weights.sum().item()
    w_mean = weights.mean().item()
    c2_sum = contributions.square().sum().item()
    w2_sum = weights.square().sum().item()
    count = r.numel()

    shuffle_rows = []
    shuffled_values = []
    for index, permutation in enumerate(permutations):
        shuffled = torch.dot(weights[permutation], v2).item()
        shuffled_values.append(shuffled)
        shuffle_rows.append(
            {
                "shuffle": index,
                "M_shuffle": shuffled,
                "F_shuffle": safe_ratio(shuffled, m0 * w_mean),
            }
        )

    sorted_weights = torch.sort(weights).values
    sorted_energy = torch.sort(v2).values
    rank_aligned = torch.dot(sorted_weights, sorted_energy).item()
    order = torch.argsort(r.abs(), descending=True)

    def tail_fraction(fraction: float, values: torch.Tensor) -> float:
        number = max(1, int(math.ceil(fraction * count)))
        total = values.sum().item()
        return safe_ratio(values[order[:number]].sum().item(), total)

    result = {
        "M": m_value,
        "M0": m0,
        "weight_sum": w_sum,
        "weight_mean": w_mean,
        "F": safe_ratio(m_value, m0 * w_mean),
        "M_shuffle_mean": sum(shuffled_values) / len(shuffled_values),
        "M_shuffle_min": min(shuffled_values),
        "M_shuffle_max": max(shuffled_values),
        "M_rank_aligned": rank_aligned,
        "max_contribution_share": safe_ratio(contributions.max().item(), m_value),
        "rESS": safe_ratio(m_value * m_value, count * c2_sum),
        "max_weight_share": safe_ratio(weights.max().item(), w_sum),
        "weight_rESS": safe_ratio(w_sum * w_sum, count * w2_sum),
        "response_tail5_share": tail_fraction(0.05, v2),
        "contribution_tail5_share": tail_fraction(0.05, contributions),
        "response_tail1_share": tail_fraction(0.01, v2) if count >= 255 else math.nan,
        "contribution_tail1_share": (
            tail_fraction(0.01, contributions) if count >= 255 else math.nan
        ),
        "r2_abs_max": r.abs().max().item(),
        "response_l2": torch.linalg.vector_norm(response[1:].to(torch.float64)).item(),
        "all_finite": bool(
            torch.isfinite(r).all()
            and torch.isfinite(v2).all()
            and torch.isfinite(weights).all()
            and torch.isfinite(contributions).all()
        ),
    }
    return result, shuffle_rows


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def batches(values: list[int], size: int) -> Iterable[list[int]]:
    for start in range(0, len(values), size):
        yield values[start : start + size]


def main_rows_for_measurements(
    width: int,
    replicates: list[int],
    measurements: list[dict[str, torch.Tensor]],
    envelope: torch.Tensor,
) -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    metric_rows: list[dict] = []
    shuffle_rows: list[dict] = []
    trajectory_rows: list[dict] = []
    vector_rows: list[dict] = []
    envelope_value = envelope.detach().cpu().to(torch.float64)

    for local, replicate in enumerate(replicates):
        trajectory_finite = True
        exact_z2 = 0.0
        exact_x2 = 0.0
        for time_index, item in enumerate(measurements):
            checkpoint = CHECKPOINTS[time_index]
            r2 = item["r2"][local]
            vectors = {
                "r2": item["V_r2"][local],
                "b2": item["V_b2"][local],
                "z2": item["V_z2"][local],
                "x2": item["V_x2"][local],
            }
            permutation_generator = torch.Generator(device="cpu")
            pseed = shuffle_seed(width, replicate, time_index)
            permutation_generator.manual_seed(pseed)
            permutations = [
                torch.randperm(
                    width - 1, generator=permutation_generator, device="cpu"
                )
                for _ in range(N_SHUFFLES)
            ]
            for field_name, response in vectors.items():
                vector_rows.append(
                    {
                        "width": width,
                        "replicate": replicate,
                        "time": checkpoint,
                        "field": field_name,
                        "r2": r2.detach().cpu().to(torch.float32),
                        "response": response.detach().cpu().to(torch.float32),
                    }
                )
                if checkpoint == 0.0 and field_name == "z2":
                    exact_z2 = max(exact_z2, response.abs().max().item())
                if checkpoint == 0.0 and field_name == "x2":
                    exact_x2 = max(exact_x2, response.abs().max().item())
                for lam in LAMBDAS:
                    metrics, individual_shuffles = contribution_metrics(
                        r2.detach().cpu(), response.detach().cpu(), lam, permutations
                    )
                    row = {
                        "width": width,
                        "replicate": replicate,
                        "time": checkpoint,
                        "field": field_name,
                        "lambda": lam,
                        "shuffle_seed": pseed,
                        **metrics,
                    }
                    metric_rows.append(row)
                    trajectory_finite = trajectory_finite and bool(metrics["all_finite"])
                    for shuffle in individual_shuffles:
                        shuffle_rows.append(
                            {
                                "width": width,
                                "replicate": replicate,
                                "time": checkpoint,
                                "field": field_name,
                                "lambda": lam,
                                "shuffle_seed": pseed,
                                **shuffle,
                            }
                        )
        maximum = envelope_value[local].item() if envelope_value.ndim else envelope_value.item()
        trajectory_rows.append(
            {
                "width": width,
                "replicate": replicate,
                "maximum_absolute_entry": maximum,
                "all_finite": trajectory_finite and math.isfinite(maximum),
                "below_envelope_gate": maximum <= 1.0e6,
                "time0_V_z2_max": exact_z2,
                "time0_V_x2_max": exact_x2,
                "time0_exact_zero": exact_z2 == 0.0 and exact_x2 == 0.0,
            }
        )
    return metric_rows, shuffle_rows, trajectory_rows, vector_rows


def run_main(args: argparse.Namespace, output: Path) -> dict:
    dtype = torch.float32 if args.dtype == "float32" else torch.float64
    widths = parse_int_list(args.widths)
    replicate_values = parse_replicates(args.replicates)
    all_metrics: list[dict] = []
    all_shuffles: list[dict] = []
    all_trajectories: list[dict] = []
    all_vectors: list[dict] = []
    all_seeds: list[dict] = []
    started = time.time()
    for width in widths:
        for group in batches(replicate_values, args.batch_size):
            print(
                json.dumps(
                    {"event": "main_batch", "width": width, "replicates": group}
                ),
                flush=True,
            )
            canonical, tangent, seeds = canonical_batch(width, group, args.device_obj)
            state = cast_state(canonical, dtype)
            direction = cast_state(tangent, dtype)
            with torch.no_grad():
                measured, envelope = integrate_pair(state, direction, args.dt)
            measured_cpu = cpu_measurements(measured)
            rows = main_rows_for_measurements(
                width, group, measured_cpu, envelope.detach().cpu()
            )
            all_metrics.extend(rows[0])
            all_shuffles.extend(rows[1])
            all_trajectories.extend(rows[2])
            all_vectors.extend(rows[3])
            all_seeds.extend(seeds)
            del canonical, tangent, state, direction, measured, measured_cpu, envelope
            torch.cuda.empty_cache()
    write_csv(output / "raw_metrics.csv", all_metrics)
    write_csv(output / "raw_shuffles.csv", all_shuffles)
    write_csv(output / "raw_trajectories.csv", all_trajectories)
    write_csv(output / "seed_map.csv", all_seeds)
    torch.save(all_vectors, output / "raw_vectors.pt")
    return {
        "widths": widths,
        "replicates": replicate_values,
        "metric_rows": len(all_metrics),
        "shuffle_rows": len(all_shuffles),
        "trajectory_rows": len(all_trajectories),
        "vector_records": len(all_vectors),
        "elapsed_seconds": time.time() - started,
    }


def bulk_relative_l2(first: torch.Tensor, second: torch.Tensor) -> float:
    a = first[1:].to(torch.float64)
    b = second[1:].to(torch.float64)
    denominator = max(
        torch.linalg.vector_norm(a).item(),
        torch.linalg.vector_norm(b).item(),
        1.0e-30,
    )
    return torch.linalg.vector_norm(a - b).item() / denominator


def moment_value(r2: torch.Tensor, response: torch.Tensor, lam: float) -> float:
    r = r2[1:].to(torch.float64)
    v = response[1:].to(torch.float64)
    return torch.sum(torch.exp(lam * r.square()) * v.square()).item()


def compare_measurement_sets(
    kind: str,
    width: int,
    replicates: list[int],
    first: list[dict[str, torch.Tensor]],
    second: list[dict[str, torch.Tensor]],
) -> list[dict]:
    rows: list[dict] = []
    for local, replicate in enumerate(replicates):
        for time_index, (left, right) in enumerate(zip(first, second)):
            for field in PRIMARY_FIELDS:
                key = f"V_{field}"
                field_relative = bulk_relative_l2(left[key][local], right[key][local])
                for lam in LAMBDAS:
                    m_left = moment_value(left["r2"][local], left[key][local], lam)
                    m_right = moment_value(right["r2"][local], right[key][local], lam)
                    m_relative = abs(m_left - m_right) / max(
                        abs(m_left), abs(m_right), 1.0e-30
                    )
                    rows.append(
                        {
                            "kind": kind,
                            "width": width,
                            "replicate": replicate,
                            "time": CHECKPOINTS[time_index],
                            "field": field,
                            "lambda": lam,
                            "field_relative_l2": field_relative,
                            "M_first": m_left,
                            "M_second": m_right,
                            "M_relative_difference": m_relative,
                            "all_finite": all(
                                math.isfinite(value)
                                for value in (field_relative, m_left, m_right, m_relative)
                            ),
                        }
                    )
    return rows


def run_controls(args: argparse.Namespace, output: Path) -> dict:
    widths = parse_int_list(args.widths)
    replicate_values = parse_replicates(args.replicates)
    rows: list[dict] = []
    seed_rows: list[dict] = []
    started = time.time()
    for width in widths:
        for group in batches(replicate_values, args.batch_size):
            print(
                json.dumps(
                    {"event": "control_batch", "width": width, "replicates": group}
                ),
                flush=True,
            )
            canonical, tangent, seeds = canonical_batch(width, group, args.device_obj)
            seed_rows.extend(seeds)
            state32 = cast_state(canonical, torch.float32)
            tangent32 = cast_state(tangent, torch.float32)
            with torch.no_grad():
                base, _ = integrate_pair(state32, tangent32, 1.0 / 64.0)
            base_cpu = cpu_measurements(base)
            del base
            torch.cuda.empty_cache()

            state32_refined = cast_state(canonical, torch.float32)
            tangent32_refined = cast_state(tangent, torch.float32)
            with torch.no_grad():
                refined, _ = integrate_pair(
                    state32_refined, tangent32_refined, 1.0 / 128.0
                )
            refined_cpu = cpu_measurements(refined)
            rows.extend(
                compare_measurement_sets(
                    "mesh", width, group, base_cpu, refined_cpu
                )
            )
            del refined, refined_cpu, state32_refined, tangent32_refined
            torch.cuda.empty_cache()

            state64 = cast_state(canonical, torch.float64)
            tangent64 = cast_state(tangent, torch.float64)
            with torch.no_grad():
                precise, _ = integrate_pair(state64, tangent64, 1.0 / 64.0)
            precise_cpu = cpu_measurements(precise)
            rows.extend(
                compare_measurement_sets(
                    "precision", width, group, base_cpu, precise_cpu
                )
            )
            del (
                canonical,
                tangent,
                state32,
                tangent32,
                state64,
                tangent64,
                precise,
                precise_cpu,
                base_cpu,
            )
            torch.cuda.empty_cache()
    write_csv(output / "raw_controls.csv", rows)
    write_csv(output / "seed_map.csv", seed_rows)
    return {
        "widths": widths,
        "replicates": replicate_values,
        "control_rows": len(rows),
        "elapsed_seconds": time.time() - started,
    }


def perturb_initial(initial: State, tangent: State, scale: float) -> State:
    return axpy(initial, tangent, scale)


def run_fd(args: argparse.Namespace, output: Path) -> dict:
    widths = parse_int_list(args.widths)
    if widths != [128]:
        raise ValueError("the locked finite-difference control is width 128 only")
    replicate_values = parse_replicates(args.replicates)
    if replicate_values != [0, 1, 2, 3]:
        raise ValueError("the locked finite-difference replicates are 0,1,2,3")
    epsilons = (2.0 ** -7, 2.0 ** -9)
    rows: list[dict] = []
    seed_rows: list[dict] = []
    started = time.time()
    width = 128
    for group in batches(replicate_values, args.batch_size):
        canonical, tangent, seeds = canonical_batch(width, group, args.device_obj)
        seed_rows.extend(seeds)
        with torch.no_grad():
            tangent_measurements, _ = integrate_pair(
                cast_state(canonical, torch.float64),
                cast_state(tangent, torch.float64),
                1.0 / 64.0,
            )
        tangent_cpu = cpu_measurements(tangent_measurements)
        for epsilon in epsilons:
            plus = perturb_initial(canonical, tangent, epsilon)
            minus = perturb_initial(canonical, tangent, -epsilon)
            with torch.no_grad():
                plus_measurements = integrate_primal_checkpoints(plus, 1.0 / 64.0)
                minus_measurements = integrate_primal_checkpoints(minus, 1.0 / 64.0)
            plus_cpu = cpu_measurements(plus_measurements)
            minus_cpu = cpu_measurements(minus_measurements)
            for local, replicate in enumerate(group):
                for time_index in range(len(CHECKPOINTS)):
                    for field in ALL_FIELDS:
                        finite_difference = (
                            plus_cpu[time_index][field][local]
                            - minus_cpu[time_index][field][local]
                        ) / (2.0 * epsilon)
                        tangent_value = tangent_cpu[time_index][f"V_{field}"][local]
                        fd_bulk = finite_difference[1:].to(torch.float64)
                        tangent_bulk = tangent_value[1:].to(torch.float64)
                        error = torch.linalg.vector_norm(fd_bulk - tangent_bulk).item()
                        tangent_norm = torch.linalg.vector_norm(tangent_bulk).item()
                        fd_norm = torch.linalg.vector_norm(fd_bulk).item()
                        relative = error / max(tangent_norm, fd_norm, 1.0e-30)
                        rows.append(
                            {
                                "width": width,
                                "replicate": replicate,
                                "time": CHECKPOINTS[time_index],
                                "field": field,
                                "epsilon": epsilon,
                                "absolute_l2_error": error,
                                "relative_l2_error": relative,
                                "tangent_l2": tangent_norm,
                                "finite_difference_l2": fd_norm,
                                "all_finite": all(
                                    math.isfinite(value)
                                    for value in (error, relative, tangent_norm, fd_norm)
                                ),
                            }
                        )
            del plus, minus, plus_measurements, minus_measurements, plus_cpu, minus_cpu
            torch.cuda.empty_cache()
        del canonical, tangent, tangent_measurements, tangent_cpu
        torch.cuda.empty_cache()
    write_csv(output / "raw_finite_difference.csv", rows)
    write_csv(output / "seed_map.csv", seed_rows)
    return {
        "widths": widths,
        "replicates": replicate_values,
        "epsilons": epsilons,
        "finite_difference_rows": len(rows),
        "elapsed_seconds": time.time() - started,
    }


def parse_int_list(raw: str) -> list[int]:
    return [int(item) for item in raw.split(",") if item]


def parse_replicates(raw: str) -> list[int]:
    if ":" in raw:
        start, stop = raw.split(":", maxsplit=1)
        return list(range(int(start), int(stop)))
    return parse_int_list(raw)


def environment_metadata(args: argparse.Namespace, run: dict, output: Path) -> dict:
    script = Path(__file__).resolve()
    preregistration = script.with_name("PREREGISTRATION.md")
    lock = script.with_name("C2_PREREGISTRATION_LOCK.md")
    return {
        "experiment": "C2_response_weighted_bulk_JVP_occupation",
        "mode": args.mode,
        "run": run,
        "checkpoints": CHECKPOINTS,
        "lambdas": LAMBDAS,
        "marked_column": MARKED,
        "n_shuffles": N_SHUFFLES,
        "model_root_seed": MODEL_ROOT_SEED,
        "bootstrap_root_seed": BOOTSTRAP_ROOT_SEED,
        "shuffle_root_seed": SHUFFLE_ROOT_SEED,
        "direction_definition": "Delta G2[:,0]=h/||h||_2; all other initial tangents zero",
        "normal_generation": "canonical float64 CUDA normals, scaled then cast",
        "dt_argument": args.dt,
        "dtype_argument": args.dtype,
        "batch_size": args.batch_size,
        "device": str(args.device_obj),
        "gpu": torch.cuda.get_device_name(args.device_obj),
        "gpu_total_memory": torch.cuda.get_device_properties(args.device_obj).total_memory,
        "torch": torch.__version__,
        "cuda_runtime": torch.version.cuda,
        "python": platform.python_version(),
        "python_executable": sys.executable,
        "command": [sys.executable, *sys.argv],
        "cwd": str(Path.cwd()),
        "cublas_workspace_config": os.environ.get("CUBLAS_WORKSPACE_CONFIG"),
        "float32_matmul_precision": torch.get_float32_matmul_precision(),
        "deterministic_algorithms": torch.are_deterministic_algorithms_enabled(),
        "script_sha256": file_sha256(script),
        "preregistration_sha256": file_sha256(preregistration),
        "lock_sha256": file_sha256(lock),
        "output": str(output.resolve()),
        "analytic_caveat": (
            "For every lambda>0 the annealed E exp(lambda r2_i^2) is infinite; "
            "this run is only a finite typical-sample diagnostic."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("main", "controls", "fd"), required=True)
    parser.add_argument("--widths", default="128,256,512,1024")
    parser.add_argument("--replicates", default="0:48")
    parser.add_argument("--dt", type=float, default=1.0 / 64.0)
    parser.add_argument("--dtype", choices=("float32", "float64"), default="float32")
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    args.device_obj = torch.device(args.device)
    if args.device_obj.type != "cuda" or not torch.cuda.is_available():
        raise RuntimeError("C2 production modes require an available CUDA device")
    if args.mode == "main" and (
        abs(args.dt - 1.0 / 64.0) > 1e-15 or args.dtype != "float32"
    ):
        raise ValueError("locked main mode requires float32 and dt=1/64")
    if args.mode == "controls":
        if parse_int_list(args.widths) != [256, 1024]:
            raise ValueError("locked controls require widths 256,1024")
        if parse_replicates(args.replicates) != list(range(8)):
            raise ValueError("locked controls require replicates 0:8")
    torch.set_float32_matmul_precision("highest")
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    torch.use_deterministic_algorithms(True)

    output = Path(args.output)
    if output.exists() and any(output.iterdir()):
        raise FileExistsError(f"refusing to overwrite nonempty output: {output}")
    output.mkdir(parents=True, exist_ok=True)
    if args.mode == "main":
        run = run_main(args, output)
    elif args.mode == "controls":
        run = run_controls(args, output)
    else:
        run = run_fd(args, output)
    metadata = environment_metadata(args, run, output)
    (output / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps(metadata, indent=2), flush=True)


if __name__ == "__main__":
    main()
