#!/usr/bin/env python3
"""Preregistered early-spike diagnostic for the doubly RMS-normalized model."""

from __future__ import annotations

import argparse
import json
import math
import time
from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass
class State:
    A: np.ndarray
    u: np.ndarray
    G: np.ndarray
    irow: np.ndarray
    icol: np.ndarray
    iloss: float


def add(x: State, y: State, scale: float) -> State:
    return State(
        x.A + scale * y.A,
        x.u + scale * y.u,
        x.G + scale * y.G,
        x.irow + scale * y.irow,
        x.icol + scale * y.icol,
        x.iloss + scale * y.iloss,
    )


def combine_rk4(x: State, ks: tuple[State, State, State, State], dt: float) -> State:
    k1, k2, k3, k4 = ks
    c = dt / 6.0
    return State(
        x.A + c * (k1.A + 2 * k2.A + 2 * k3.A + k4.A),
        x.u + c * (k1.u + 2 * k2.u + 2 * k3.u + k4.u),
        x.G + c * (k1.G + 2 * k2.G + 2 * k3.G + k4.G),
        x.irow + c * (k1.irow + 2 * k2.irow + 2 * k3.irow + k4.irow),
        x.icol + c * (k1.icol + 2 * k2.icol + 2 * k3.icol + k4.icol),
        x.iloss + c * (k1.iloss + 2 * k2.iloss + 2 * k3.iloss + k4.iloss),
    )


def diagnostics(x: State, epsilon: float, target: float, eta: float) -> dict[str, object]:
    n = x.A.size
    X = x.u * x.u
    alpha = math.sqrt(float(np.mean(X * X)) + epsilon)
    H = X / alpha
    Z = x.G @ H
    V = Z * Z
    beta = math.sqrt(float(np.mean(V * V)) + epsilon)
    Y = V / beta
    f = float(np.mean(x.A * Y))
    e = target - f
    C = x.A - f * Y
    R = (2.0 / beta) * Z * C
    g = x.G.T @ R
    T = g - H * float(np.mean(H * g))
    ka = float(np.mean(Y * Y))
    kg = float(np.mean(H * H) * np.mean(R * R))
    ku = float((4.0 / alpha) * np.mean(H * T * T))
    k = ka + kg + ku
    return {
        "X": X,
        "alpha": alpha,
        "H": H,
        "Z": Z,
        "beta": beta,
        "Y": Y,
        "f": f,
        "e": e,
        "C": C,
        "R": R,
        "g": g,
        "T": T,
        "ka": ka,
        "kg": kg,
        "ku": ku,
        "k": k,
        "loss": e * e,
        "factor": 2.0 * eta * e,
    }


def rhs(x: State, epsilon: float, target: float, eta: float) -> State:
    d = diagnostics(x, epsilon, target, eta)
    n = x.A.size
    factor = float(d["factor"])
    A = d["Y"]
    u = (2.0 / float(d["alpha"])) * x.u * d["T"]
    G = np.multiply.outer(d["R"], d["H"]) / n
    irow = -8.0 * eta * float(d["e"]) * float(d["f"]) * d["Y"] ** 2
    icol = (
        8.0
        * eta
        * float(d["e"])
        * epsilon
        * float(d["f"])
        / float(d["beta"]) ** 2
        * d["H"] ** 2
    )
    iloss = -4.0 * eta * float(d["e"]) ** 2 * float(d["k"])
    return State(factor * A, factor * u, factor * G, irow, icol, iloss)


def extrema(d: dict[str, object]) -> dict[str, float]:
    out: dict[str, float] = {}
    for name in ("A", "u", "Z", "H", "Y", "R", "T"):
        arr = d[name] if name in d else None
        if arr is None:
            continue
        out[name] = float(np.max(np.abs(arr)))
    return out


def integrate(
    A0: np.ndarray,
    u0: np.ndarray,
    W0: np.ndarray,
    dt: float,
    horizon: float,
    epsilon: float,
    target: float,
    eta: float,
    sample_dt: float,
) -> dict[str, object]:
    n = A0.size
    G0 = W0 / math.sqrt(n)
    x = State(A0.copy(), u0.copy(), G0.copy(), np.zeros(n), np.zeros(n), 0.0)
    row0 = np.sum(W0 * W0, axis=1) - 2.0 * A0 * A0
    col0 = np.sum(W0 * W0, axis=0) - 0.5 * u0 * u0
    d0 = diagnostics(x, epsilon, target, eta)
    loss0 = float(d0["loss"])
    max_k = float(d0["k"])
    max_k_time = 0.0
    max_coords = extrema({**d0, "A": x.A, "u": x.u})
    hit = {0.05: None, 0.10: None}
    times = [0.0]
    fs = [float(d0["f"])]
    ks = [float(d0["k"])]
    kas = [float(d0["ka"])]
    kgs = [float(d0["kg"])]
    kus = [float(d0["ku"])]
    sample_every = max(1, int(round(sample_dt / dt)))
    steps = int(round(horizon / dt))
    prior_f = float(d0["f"])
    prior_t = 0.0

    for step in range(1, steps + 1):
        k1 = rhs(x, epsilon, target, eta)
        k2 = rhs(add(x, k1, dt / 2), epsilon, target, eta)
        k3 = rhs(add(x, k2, dt / 2), epsilon, target, eta)
        k4 = rhs(add(x, k3, dt), epsilon, target, eta)
        x = combine_rk4(x, (k1, k2, k3, k4), dt)
        t = step * dt
        if not (
            np.all(np.isfinite(x.A))
            and np.all(np.isfinite(x.u))
            and np.all(np.isfinite(x.G))
        ):
            raise FloatingPointError(f"nonfinite state at t={t}")
        d = diagnostics(x, epsilon, target, eta)
        f = float(d["f"])
        kval = float(d["k"])
        if kval > max_k:
            max_k = kval
            max_k_time = t
        now = extrema({**d, "A": x.A, "u": x.u})
        for key, value in now.items():
            max_coords[key] = max(max_coords.get(key, 0.0), value)
        for level in hit:
            if hit[level] is None and prior_f < level <= f:
                frac = (level - prior_f) / max(f - prior_f, np.finfo(float).tiny)
                hit[level] = prior_t + frac * (t - prior_t)
        prior_f, prior_t = f, t
        if step % sample_every == 0:
            times.append(t)
            fs.append(f)
            ks.append(kval)
            kas.append(float(d["ka"]))
            kgs.append(float(d["kg"]))
            kus.append(float(d["ku"]))

    dfinal = diagnostics(x, epsilon, target, eta)
    W = math.sqrt(n) * x.G
    row = np.sum(W * W, axis=1) - 2.0 * x.A * x.A
    col = np.sum(W * W, axis=0) - 0.5 * x.u * x.u
    row_resid = row - row0 - x.irow
    col_resid = col - col0 - x.icol
    row_scale = max(1.0, float(np.max(np.abs(row0))), float(np.max(np.abs(row))))
    col_scale = max(1.0, float(np.max(np.abs(col0))), float(np.max(np.abs(col))))
    loss_resid = float(dfinal["loss"]) - loss0 - x.iloss

    return {
        "n": n,
        "dt": dt,
        "horizon": horizon,
        "initial_f": float(d0["f"]),
        "final_f": float(dfinal["f"]),
        "initial_k": float(d0["k"]),
        "final_k": float(dfinal["k"]),
        "max_k": max_k,
        "max_k_time": max_k_time,
        "hit_005": hit[0.05],
        "hit_010": hit[0.10],
        "max_coords": max_coords,
        "min_alpha_beta": min(float(d0["alpha"]), float(d0["beta"]), float(dfinal["alpha"]), float(dfinal["beta"])),
        "row_balance_rel": float(np.max(np.abs(row_resid))) / row_scale,
        "col_balance_rel": float(np.max(np.abs(col_resid))) / col_scale,
        "loss_balance_abs": abs(loss_resid),
        "times": times,
        "f_series": fs,
        "k_series": ks,
        "ka_series": kas,
        "kg_series": kgs,
        "ku_series": kus,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-width", type=int, default=1024)
    args = parser.parse_args()
    widths = [n for n in (128, 256, 512, 1024) if n <= args.max_width]
    seeds = [31001, 31002, 31003, 31004]
    epsilon = 1.0
    target = 1.0
    eta = 1.0
    horizon = 0.25
    primary_dt = 5e-4
    control_dt = 2.5e-4
    records: list[dict[str, object]] = []
    started = time.time()

    for seed in seeds:
        root = np.random.SeedSequence(seed)
        sa, su, sw = root.spawn(3)
        Amax = np.random.default_rng(sa).standard_normal(args.max_width)
        umax = np.random.default_rng(su).standard_normal(args.max_width)
        Wmax = np.random.default_rng(sw).standard_normal((args.max_width, args.max_width))
        for n in widths:
            A0 = Amax[:n]
            u0 = umax[:n]
            W0 = Wmax[:n, :n]
            primary = integrate(A0, u0, W0, primary_dt, horizon, epsilon, target, eta, primary_dt)
            control = integrate(A0, u0, W0, control_dt, horizon, epsilon, target, eta, primary_dt)
            fdelta = float(np.max(np.abs(np.asarray(primary["f_series"]) - np.asarray(control["f_series"]))))
            record = {
                "seed": seed,
                "n": n,
                "primary": primary,
                "control": control,
                "max_f_step_delta": fdelta,
                "elapsed_seconds": time.time() - started,
            }
            records.append(record)
            print(json.dumps({
                "seed": seed,
                "n": n,
                "max_k": primary["max_k"],
                "hit_010": primary["hit_010"],
                "f_step_delta": fdelta,
                "elapsed_seconds": record["elapsed_seconds"],
            }), flush=True)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({
        "protocol": "EARLY_SPIKE_EXPERIMENT_PROTOCOL.md",
        "epsilon": epsilon,
        "target": target,
        "eta": eta,
        "records": records,
        "elapsed_seconds": time.time() - started,
    }, indent=2))


if __name__ == "__main__":
    main()
