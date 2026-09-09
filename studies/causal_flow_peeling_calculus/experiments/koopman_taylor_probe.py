#!/usr/bin/env python3
"""Preregistered K1 probe: exact ODE Taylor jets for the L=2 arctan flow."""

from __future__ import annotations

import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp


OUT = Path(__file__).resolve().parent / "outputs" / "koopman_taylor_v3"
WIDTHS = (128, 256, 512)
REPLICATES = {128: 4, 256: 3, 512: 2}
K_MAX = 80
BASE_SEED = 20260825


@dataclass
class JetResult:
    state_a: list[np.ndarray]
    state_u: list[np.ndarray]
    state_g: list[np.ndarray]
    x: list[np.ndarray]
    z: list[np.ndarray]
    y: list[np.ndarray]
    d_u: list[np.ndarray]
    d_z: list[np.ndarray]
    b: list[np.ndarray]
    q: list[np.ndarray]
    u_velocity: list[np.ndarray]
    f: np.ndarray
    kernel: np.ndarray
    recurrence_residual: float


def convolution_at(a: list[np.ndarray], b: list[np.ndarray], k: int) -> np.ndarray:
    return sum((a[i] * b[k - i] for i in range(k + 1)), start=np.zeros_like(a[0]))


def reciprocal_coefficient(
    denominator: list[np.ndarray], reciprocal: list[np.ndarray], k: int
) -> np.ndarray:
    if k == 0:
        return 1.0 / denominator[0]
    accumulated = sum(
        (denominator[i] * reciprocal[k - i] for i in range(1, k + 1)),
        start=np.zeros_like(denominator[0]),
    )
    return -accumulated / denominator[0]


def atan_coefficient(
    argument: list[np.ndarray], derivative_gate: list[np.ndarray], k: int
) -> np.ndarray:
    if k == 0:
        return np.arctan(argument[0])
    accumulated = sum(
        (
            derivative_gate[i] * (k - i) * argument[k - i]
            for i in range(k)
        ),
        start=np.zeros_like(argument[0]),
    )
    return accumulated / k


def inner_series(a: list[np.ndarray], b: list[np.ndarray], k_max: int) -> np.ndarray:
    n = a[0].size
    return np.array(
        [
            sum(float(np.dot(a[i], b[k - i])) for i in range(k + 1)) / n
            for k in range(k_max + 1)
        ]
    )


def scalar_convolution(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    k_max = min(len(a), len(b)) - 1
    return np.array(
        [sum(a[i] * b[k - i] for i in range(k + 1)) for k in range(k_max + 1)]
    )


def build_jet(a0: np.ndarray, u0: np.ndarray, g0: np.ndarray, k_max: int) -> JetResult:
    n = a0.size
    state_a = [a0.copy()]
    state_u = [u0.copy()]
    state_g = [g0.copy()]

    x: list[np.ndarray] = []
    z: list[np.ndarray] = []
    y: list[np.ndarray] = []
    d_u: list[np.ndarray] = []
    d_z: list[np.ndarray] = []
    b: list[np.ndarray] = []
    q: list[np.ndarray] = []
    u_velocity: list[np.ndarray] = []
    denominator_u: list[np.ndarray] = []
    denominator_z: list[np.ndarray] = []
    recurrence_residual = 0.0

    for k in range(k_max + 1):
        u_square_k = convolution_at(state_u, state_u, k)
        denominator_u.append(u_square_k + (1.0 if k == 0 else 0.0))
        d_u.append(reciprocal_coefficient(denominator_u, d_u, k))
        x.append(atan_coefficient(state_u, d_u, k))

        z_k = sum(
            (state_g[i] @ x[k - i] for i in range(k + 1)),
            start=np.zeros(n),
        )
        z.append(z_k)
        z_square_k = convolution_at(z, z, k)
        denominator_z.append(z_square_k + (1.0 if k == 0 else 0.0))
        d_z.append(reciprocal_coefficient(denominator_z, d_z, k))
        y.append(atan_coefficient(z, d_z, k))

        b.append(convolution_at(state_a, d_z, k))
        q_k = sum(
            (state_g[i].T @ b[k - i] for i in range(k + 1)),
            start=np.zeros(n),
        )
        q.append(q_k)
        u_velocity_k = convolution_at(d_u, q, k)
        u_velocity.append(u_velocity_k)

        if k < k_max:
            g_velocity_k = sum(
                (
                    np.outer(b[i], x[k - i]) / n
                    for i in range(k + 1)
                ),
                start=np.zeros((n, n)),
            )
            state_a.append(y[k] / (k + 1))
            state_u.append(u_velocity_k / (k + 1))
            state_g.append(g_velocity_k / (k + 1))

            for lhs, rhs in (
                ((k + 1) * state_a[k + 1], y[k]),
                ((k + 1) * state_u[k + 1], u_velocity_k),
                ((k + 1) * state_g[k + 1], g_velocity_k),
            ):
                relative_residual = float(
                    np.max(np.abs(lhs - rhs)) / (1.0 + np.max(np.abs(rhs)))
                )
                recurrence_residual = max(recurrence_residual, relative_residual)

    f = inner_series(state_a, y, k_max)
    norm_y = inner_series(y, y, k_max)
    norm_b = inner_series(b, b, k_max)
    norm_x = inner_series(x, x, k_max)
    norm_u_velocity = inner_series(u_velocity, u_velocity, k_max)
    kernel = norm_y + scalar_convolution(norm_b, norm_x) + norm_u_velocity

    return JetResult(
        state_a=state_a,
        state_u=state_u,
        state_g=state_g,
        x=x,
        z=z,
        y=y,
        d_u=d_u,
        d_z=d_z,
        b=b,
        q=q,
        u_velocity=u_velocity,
        f=f,
        kernel=kernel,
        recurrence_residual=recurrence_residual,
    )


def evaluate_series(coefficients: list[np.ndarray], t: float) -> np.ndarray:
    result = np.zeros_like(coefficients[0])
    for coefficient in reversed(coefficients):
        result = result * t + coefficient
    return result


def validation() -> dict[str, object]:
    n = 6
    rng = np.random.default_rng(910247)
    a0 = rng.standard_normal(n)
    u0 = rng.standard_normal(n)
    g0 = rng.standard_normal((n, n)) / math.sqrt(n)
    jet = build_jet(a0, u0, g0, 14)

    initial = np.concatenate([a0, u0, g0.ravel()])

    def rhs(_: float, flat: np.ndarray) -> np.ndarray:
        a = flat[:n]
        u = flat[n : 2 * n]
        g = flat[2 * n :].reshape(n, n)
        x = np.arctan(u)
        z = g @ x
        y = np.arctan(z)
        d_u = 1.0 / (1.0 + u * u)
        d_z = 1.0 / (1.0 + z * z)
        b = a * d_z
        q = g.T @ b
        return np.concatenate([y, d_u * q, (np.outer(b, x) / n).ravel()])

    times = (0.005, 0.01, 0.02)
    solution = solve_ivp(
        rhs,
        (0.0, max(times)),
        initial,
        t_eval=times,
        rtol=2e-13,
        atol=2e-14,
        method="DOP853",
    )
    comparisons = []
    for index, t in enumerate(times):
        approximate = np.concatenate(
            [
                evaluate_series(jet.state_a, t),
                evaluate_series(jet.state_u, t),
                evaluate_series(jet.state_g, t).ravel(),
            ]
        )
        reference = solution.y[:, index]
        comparisons.append(
            {
                "t": t,
                "absolute_max_error": float(np.max(np.abs(approximate - reference))),
                "relative_l2_error": float(
                    np.linalg.norm(approximate - reference) / np.linalg.norm(reference)
                ),
            }
        )
    gradient_identity_residual = max(
        abs((k + 1) * jet.f[k + 1] - jet.kernel[k])
        / (1.0 + abs(jet.kernel[k]))
        for k in range(14)
    )
    return {
        "recurrence_residual": jet.recurrence_residual,
        "gradient_identity_residual": float(gradient_identity_residual),
        "solve_ivp_success": bool(solution.success),
        "comparisons": comparisons,
    }


def root(value: float, k: int) -> float:
    return float(abs(value) ** (1.0 / k)) if value != 0.0 else 0.0


def summarize(records: list[dict[str, float]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for n in WIDTHS:
        group = [record for record in records if int(record["n"]) == n]
        per_order = {}
        for k in range(1, K_MAX + 1):
            f_roots = np.array([record[f"f_root_{k}"] for record in group])
            kernel_roots = np.array(
                [record[f"kernel_root_{k}"] for record in group]
            )
            per_order[str(k)] = {
                "f_median": float(np.median(f_roots)),
                "f_q90": float(np.quantile(f_roots, 0.9)),
                "kernel_median": float(np.median(kernel_roots)),
                "kernel_q90": float(np.quantile(kernel_roots, 0.9)),
            }
        result[str(n)] = {
            "replicates": len(group),
            "max_recurrence_residual": float(
                max(record["recurrence_residual"] for record in group)
            ),
            "orders": per_order,
        }
    return result


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    validation_report = validation()
    print("validation", json.dumps(validation_report), flush=True)

    seed_sequence = np.random.SeedSequence(BASE_SEED)
    children = seed_sequence.spawn(sum(REPLICATES.values()))
    records: list[dict[str, float]] = []
    seed_index = 0
    coefficient_rows: list[dict[str, float]] = []
    for n in WIDTHS:
        for replicate in range(REPLICATES[n]):
            rng = np.random.default_rng(children[seed_index])
            seed_index += 1
            a0 = rng.standard_normal(n)
            u0 = rng.standard_normal(n)
            g0 = rng.standard_normal((n, n)) / math.sqrt(n)
            jet = build_jet(a0, u0, g0, K_MAX)
            record: dict[str, float] = {
                "n": float(n),
                "replicate": float(replicate),
                "recurrence_residual": jet.recurrence_residual,
            }
            for k in range(1, K_MAX + 1):
                record[f"f_root_{k}"] = root(float(jet.f[k]), k)
                record[f"kernel_root_{k}"] = root(float(jet.kernel[k]), k)
                coefficient_rows.append(
                    {
                        "n": float(n),
                        "replicate": float(replicate),
                        "k": float(k),
                        "f_coefficient": float(jet.f[k]),
                        "kernel_coefficient": float(jet.kernel[k]),
                    }
                )
            records.append(record)
        print(f"completed n={n} replicates={REPLICATES[n]}", flush=True)

    with (OUT / "coefficients.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(coefficient_rows[0].keys()))
        writer.writeheader()
        writer.writerows(coefficient_rows)

    report = {
        "base_seed": BASE_SEED,
        "k_max": K_MAX,
        "widths": list(WIDTHS),
        "replicates": REPLICATES,
        "validation": validation_report,
        "summary": summarize(records),
    }
    (OUT / "summary.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report))


if __name__ == "__main__":
    main()
