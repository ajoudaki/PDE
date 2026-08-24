#!/usr/bin/env python3
"""Frozen finite-width physical-flow boundary-layer diagnostic."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass

import numpy as np
from scipy.integrate import solve_ivp


@dataclass
class RunResult:
    width: int
    seed: int
    event_time: float | None
    initial_kernel: float
    max_invariant_error: float
    residual_magnitude_monotone: bool
    solver_success: bool
    function_evaluations: int


def unpack(state: np.ndarray, width: int):
    a = state[:width]
    u = state[width : 2 * width]
    g = state[2 * width : 2 * width + width * width].reshape(width, width)
    e = float(state[-1])
    return a, u, g, e


def observables(state: np.ndarray, width: int):
    a, u, g, e = unpack(state, width)
    x = u * u
    z = g @ x
    b = a * z
    r = g.T @ b
    f = float(np.mean(a * z**2))
    kernel = float(
        np.mean(z**4)
        + 4 * np.mean(b**2) * np.mean(x**2)
        + 16 * np.mean(x * r**2)
    )
    return f, kernel, e


def initial_state(width: int, seed: int):
    rng = np.random.default_rng(seed)
    a = rng.normal(size=width)
    u = rng.normal(size=width)
    g = rng.normal(size=(width, width)) / np.sqrt(width)
    provisional = np.concatenate((a, u, g.ravel(), np.array([0.0])))
    f0, kernel0, _ = observables(provisional, width)
    state = provisional.copy()
    state[-1] = 1.0 - f0
    return state, kernel0


def solve_one(
    width: int,
    seed: int,
    rtol: float = 2.0e-9,
    atol: float = 2.0e-11,
):
    state0, kernel0 = initial_state(width, seed)
    residual0 = float(state0[-1])

    def rhs(_time, state):
        a, u, g, e = unpack(state, width)
        x = u * u
        z = g @ x
        b = a * z
        r = g.T @ b
        kernel = (
            np.mean(z**4)
            + 4 * np.mean(b**2) * np.mean(x**2)
            + 16 * np.mean(x * r**2)
        )
        da = 2 * e * z**2
        du = 8 * e * u * r
        dg = 4 * e * np.outer(b, x) / width
        de = -2 * e * kernel
        return np.concatenate((da, du, dg.ravel(), np.array([de])))

    def event(_time, state):
        return state[-1] - residual0 / 2

    event.terminal = True
    event.direction = 0
    solution = solve_ivp(
        rhs,
        (0.0, 0.05),
        state0,
        method="DOP853",
        rtol=rtol,
        atol=atol,
        max_step=2.5e-4,
        events=event,
    )
    event_time = (
        float(solution.t_events[0][0]) if len(solution.t_events[0]) else None
    )
    invariant_errors = []
    residuals = []
    for state in solution.y.T:
        f, _kernel, e = observables(state, width)
        invariant_errors.append(abs(f + e - 1.0))
        residuals.append(e)
    result = RunResult(
        width=width,
        seed=seed,
        event_time=event_time,
        initial_kernel=kernel0,
        max_invariant_error=max(invariant_errors),
        residual_magnitude_monotone=bool(
            np.all(np.diff(np.abs(residuals)) <= 1.0e-10)
        ),
        solver_success=bool(solution.success),
        function_evaluations=int(solution.nfev),
    )
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--widths", nargs="+", type=int, default=[32, 64, 128, 256])
    parser.add_argument("--seeds", type=int, default=6)
    parser.add_argument("--output")
    args = parser.parse_args()

    results = []
    for width in args.widths:
        for seed_index in range(args.seeds):
            seed = 2026082100 + 1000 * width + seed_index
            results.append(asdict(solve_one(width, seed)))

    audit_seed = 2026082100 + 1000 * 128
    coarse = solve_one(128, audit_seed)
    fine = solve_one(128, audit_seed, rtol=2.0e-10, atol=2.0e-12)
    payload = {
        "configuration": {
            "widths": args.widths,
            "seeds_per_width": args.seeds,
            "target": 1.0,
            "eta": 1.0,
            "rtol": 2.0e-9,
            "atol": 2.0e-11,
            "max_step": 2.5e-4,
        },
        "results": results,
        "tolerance_audit": {
            "coarse_event_time": coarse.event_time,
            "fine_event_time": fine.event_time,
        },
    }
    rendered = json.dumps(payload, indent=2)
    if args.output:
        raise RuntimeError(
            "This frozen script prints JSON; redirecting output is intentionally external."
        )
    print(rendered)


if __name__ == "__main__":
    main()
