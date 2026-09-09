#!/usr/bin/env python3
"""Core routines for the corrected common-clock Loewner experiment."""

from __future__ import annotations

import math

import numpy as np

import simulate_loewner as model


MAX_WIDTH = 256


def generate_state(width: int, pair_count: int, seed_base: int) -> model.State:
    """Generate common/nested Gaussian draws and antithetic a signs."""
    a0 = np.empty((pair_count, width), dtype=np.float64)
    u0 = np.empty((pair_count, width), dtype=np.float64)
    W0 = np.empty((pair_count, width, width), dtype=np.float64)
    for r in range(pair_count):
        rng = np.random.default_rng(np.random.SeedSequence([seed_base, r]))
        a_max = rng.standard_normal(MAX_WIDTH)
        u_max = rng.standard_normal(MAX_WIDTH)
        W_max = rng.standard_normal((MAX_WIDTH, MAX_WIDTH))
        a0[r] = a_max[:width]
        u0[r] = u_max[:width]
        W0[r] = W_max[:width, :width]
    a = np.stack((a0, -a0), axis=1).reshape(2 * pair_count, width)
    u = np.repeat(u0[:, None, :], 2, axis=1).reshape(2 * pair_count, width)
    W = np.repeat(W0[:, None, :, :], 2, axis=1).reshape(
        2 * pair_count, width, width
    )
    return model.State(a, W, u)


def f_value(state: model.State) -> np.ndarray:
    n = state.a.shape[1]
    u2 = state.u * state.u
    z = np.einsum("bij,bj->bi", state.W, u2, optimize=True) / math.sqrt(n)
    return np.mean(state.a * z * z, axis=1)


def max_component(state: model.State) -> np.ndarray:
    return np.maximum.reduce(
        (
            np.max(np.abs(state.a), axis=1),
            np.max(np.abs(state.W), axis=(1, 2)),
            np.max(np.abs(state.u), axis=1),
        )
    )


def pair_average(values: np.ndarray) -> np.ndarray:
    return values.reshape(values.shape[0] // 2, 2, *values.shape[1:]).mean(axis=1)


def simulate_pair_curves(
    width: int,
    pair_count: int,
    seed_base: int,
    s_max: float,
    step: float,
    state_ceiling: float = 1.0e12,
) -> dict[str, np.ndarray]:
    """Return raw per-pair G(s) and direct paired f-increment curves."""
    number_steps = int(round(s_max / step))
    if not math.isclose(number_steps * step, s_max, abs_tol=1e-15):
        raise ValueError("s_max must be an exact step endpoint")
    times = np.arange(number_steps + 1, dtype=np.float64) * step
    state = generate_state(width, pair_count, seed_base)
    f0_raw = f_value(state)
    k0_raw, _ = model.observable_and_derivative(state)
    pair_g = np.full((pair_count, number_steps + 1), np.inf, dtype=np.float64)
    pair_f = np.full_like(pair_g, np.inf)
    pair_g[:, 0] = pair_average(k0_raw)
    pair_f[:, 0] = 0.0
    trajectory_alive = np.ones(2 * pair_count, dtype=bool)
    escape_time = np.full(2 * pair_count, np.nan)

    for index in range(1, number_steps + 1):
        with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
            state = model.rk4_step(state, step)
        amplitude = max_component(state)
        newly_dead = trajectory_alive & (
            (~np.isfinite(amplitude)) | (amplitude >= state_ceiling)
        )
        escape_time[newly_dead] = times[index]
        trajectory_alive[newly_dead] = False
        if np.any(~trajectory_alive):
            state.a[~trajectory_alive] = 0.0
            state.W[~trajectory_alive] = 0.0
            state.u[~trajectory_alive] = 0.0

        kval, _ = model.observable_and_derivative(state)
        fval = f_value(state)
        kval[~trajectory_alive] = np.inf
        fval[~trajectory_alive] = np.inf
        paired_alive = trajectory_alive.reshape(pair_count, 2).all(axis=1)
        gpair = pair_average(kval)
        fpair = pair_average(fval - f0_raw)
        gpair[~paired_alive] = np.inf
        fpair[~paired_alive] = np.inf
        pair_g[:, index] = gpair
        pair_f[:, index] = fpair

    return {
        "times": times,
        "pair_g": pair_g,
        "pair_f_direct": pair_f,
        "escape_time": escape_time,
        "initial_pair_g": pair_g[:, 0],
        "initial_raw_f": f0_raw,
    }


def median_of_means(curves: np.ndarray, blocks: int, clip: float) -> np.ndarray:
    """Coordinatewise median of deterministic contiguous block means."""
    if curves.shape[0] % blocks:
        raise ValueError("pair count must be divisible by block count")
    clipped = np.clip(curves, -clip, clip)
    block_size = curves.shape[0] // blocks
    block_curves = clipped.reshape(blocks, block_size, curves.shape[1]).mean(axis=1)
    return np.median(block_curves, axis=0)


def cumulative_simpson_uniform(values: np.ndarray, step: float) -> np.ndarray:
    """Cumulative integral: Simpson on even indices, 3/8 for odd >=3, trapezoid at 1."""
    result = np.zeros_like(values)
    if len(values) > 1:
        result[1] = 0.5 * step * (values[0] + values[1])
    for j in range(2, len(values)):
        if j % 2 == 0:
            result[j] = result[j - 2] + (step / 3.0) * (
                values[j - 2] + 4.0 * values[j - 1] + values[j]
            )
        else:
            result[j] = result[j - 3] + (3.0 * step / 8.0) * (
                values[j - 3]
                + 3.0 * values[j - 2]
                + 3.0 * values[j - 1]
                + values[j]
            )
    return result
