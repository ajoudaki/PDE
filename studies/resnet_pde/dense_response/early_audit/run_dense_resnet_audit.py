#!/usr/bin/env python3
"""Reproducible numerical audit for dense Euclidean residual muP dynamics.

The experiments are deliberately modest enough to run on CPU.  They test:

* the exact finite-(n,L) gradient-flow normalization;
* the distinction between iid-in-depth initialization and a depth-regular
  Gaussian matrix field;
* truncated Dyson/backpropagation response words;
* PSD tangent-kernel reconstruction;
* depth-Galerkin/SVD compressibility of scalar response contractions;
* restart, near-alignment, nonnormality, and training-horizon stress tests.

This is an audit of a proposed compression mechanism, not a finite-width
surrogate advertised as the desired width-independent PDE.
"""

from __future__ import annotations

import argparse
import copy
import csv
import json
import math
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


Array = np.ndarray


def bounded_activation(x: Array, gain: float = 1.0) -> Array:
    """Smooth bounded activation tanh(gain*x)/gain with unit slope at zero."""
    return np.tanh(gain * x) / gain


def activation_prime_from_z(z: Array, gain: float = 1.0) -> Array:
    th = np.tanh(gain * z)
    return 1.0 - th * th


@dataclass
class State:
    B: Array
    W: Array
    a: Array
    gain: float = 1.0

    def clone(self) -> "State":
        return State(self.B.copy(), self.W.copy(), self.a.copy(), self.gain)


@dataclass
class Cache:
    H: List[Array]
    Z: List[Array]
    D: List[Array]
    Q: List[Array]
    Beta: List[Array]
    z0: Array
    d0: Array
    gamma: Array
    f: Array
    g: Array
    loss: float
    kernel: Array


def add_state(x: State, y: State, scale: float) -> State:
    return State(
        x.B + scale * y.B,
        x.W + scale * y.W,
        x.a + scale * y.a,
        x.gain,
    )


def combine_heun(x: State, k1: State, k2: State, dt: float) -> State:
    return State(
        x.B + 0.5 * dt * (k1.B + k2.B),
        x.W + 0.5 * dt * (k1.W + k2.W),
        x.a + 0.5 * dt * (k1.a + k2.a),
        x.gain,
    )


def make_data(
    m: int,
    d: int,
    seed: int,
    case: str = "generic",
) -> Tuple[Array, Array]:
    rng = np.random.default_rng(seed)
    if case == "aligned":
        x0 = rng.normal(size=d)
        x0 /= np.linalg.norm(x0)
        X = [x0]
        for _ in range(1, m):
            x = x0 + 0.035 * rng.normal(size=d)
            x /= np.linalg.norm(x)
            X.append(x)
        X = np.stack(X)
        y = np.linspace(-0.8, 0.9, m)
    else:
        raw = rng.normal(size=(d, m))
        q, _ = np.linalg.qr(raw)
        X = q[:, :m].T
        if case == "perturbed":
            X = X + 0.025 * rng.normal(size=X.shape)
            X /= np.linalg.norm(X, axis=1, keepdims=True)
        y = np.linspace(0.9, -0.7, m)
        if m >= 3:
            y[1] = 0.25
    return X, y


def _smooth_gaussian_field(
    n: int,
    depth_grid: Array,
    seed: int,
    modes: int = 5,
) -> Array:
    """Stationary smooth Gaussian field with N(0,1/n) pointwise marginals."""
    rng = np.random.default_rng(seed)
    g0 = rng.normal(size=(n, n))
    gc = rng.normal(size=(modes, n, n))
    gs = rng.normal(size=(modes, n, n))
    alpha = np.exp(-0.55 * np.arange(1, modes + 1))
    denom = math.sqrt(1.0 + float(np.sum(alpha * alpha)))
    W = np.empty((len(depth_grid), n, n), dtype=np.float64)
    for ell, s in enumerate(depth_grid):
        val = g0.copy()
        for k, ak in enumerate(alpha, start=1):
            val += ak * (
                math.cos(2.0 * math.pi * k * s) * gc[k - 1]
                + math.sin(2.0 * math.pi * k * s) * gs[k - 1]
            )
        W[ell] = val / (denom * math.sqrt(n))
    return W


def initialize(
    n: int,
    L: int,
    d: int,
    seed: int,
    depth_mode: str = "iid",
    nonnormal_strength: float = 0.0,
    gain: float = 1.0,
) -> State:
    rng = np.random.default_rng(seed)
    B = rng.normal(size=(n, d)) / math.sqrt(d)
    a = rng.normal(size=n)
    if depth_mode == "iid":
        W = rng.normal(size=(L, n, n)) / math.sqrt(n)
    elif depth_mode == "smooth":
        W = _smooth_gaussian_field(
            n=n,
            depth_grid=(np.arange(L) + 0.5) / L,
            seed=seed + 104729,
        )
    else:
        raise ValueError(f"unknown depth_mode={depth_mode}")

    if nonnormal_strength:
        u = rng.normal(size=n)
        u /= np.linalg.norm(u)
        v = rng.normal(size=n)
        v -= u * float(u @ v)
        v /= np.linalg.norm(v)
        for ell in range(L):
            amp = nonnormal_strength * (
                0.65 + 0.35 * math.sin(2.0 * math.pi * (ell + 0.5) / L)
            )
            W[ell] += amp * np.outer(u, v)
    return State(B=B, W=W, a=a, gain=float(gain))


def forward_and_adjoint(
    state: State,
    X: Array,
    y: Array,
    adjoint_order: Optional[int] = None,
) -> Cache:
    """Forward pass and unit-output adjoint.

    Q[L]=a.  Thus the raw derivative of f_r with respect to h_r^ell is
    Q[ell]/n.  adjoint_order=None is exact; an integer truncates the ordered
    response-word expansion of the backward product.
    """
    W, B, a = state.W, state.B, state.a
    gain = state.gain
    L, n, _ = W.shape
    delta = 1.0 / L
    z0 = X @ B.T
    d0 = activation_prime_from_z(z0, gain)
    H: List[Array] = [bounded_activation(z0, gain)]
    Z: List[Array] = []
    D: List[Array] = []
    for ell in range(L):
        z = H[-1] @ W[ell].T
        Z.append(z)
        D.append(activation_prime_from_z(z, gain))
        H.append(H[-1] + delta * bounded_activation(z, gain))

    f = (H[-1] @ a) / n
    g = f - y
    loss = 0.5 * float(g @ g)

    Q: List[Array] = [np.empty_like(H[0]) for _ in range(L + 1)]
    Q[L] = np.broadcast_to(a, H[L].shape).copy()
    if adjoint_order is None:
        for ell in range(L - 1, -1, -1):
            beta = D[ell] * Q[ell + 1]
            Q[ell] = Q[ell + 1] + delta * (beta @ W[ell])
    else:
        M = int(adjoint_order)
        pieces = [np.zeros_like(H[L]) for _ in range(M + 1)]
        pieces[0][...] = a
        for ell in range(L - 1, -1, -1):
            old = [p.copy() for p in pieces]
            for k in range(1, M + 1):
                pieces[k] = old[k] + delta * ((D[ell] * old[k - 1]) @ W[ell])
            pieces[0] = old[0]
            Q[ell] = sum(pieces)

    Beta = [D[ell] * Q[ell + 1] for ell in range(L)]
    gamma = d0 * Q[0]

    Gh_final = H[-1] @ H[-1].T / n
    Ggamma = gamma @ gamma.T / n
    kernel = Gh_final + (X @ X.T) * Ggamma
    for ell in range(L):
        Gh = H[ell] @ H[ell].T / n
        Gb = Beta[ell] @ Beta[ell].T / n
        kernel += delta * Gh * Gb

    return Cache(
        H=H,
        Z=Z,
        D=D,
        Q=Q,
        Beta=Beta,
        z0=z0,
        d0=d0,
        gamma=gamma,
        f=f,
        g=g,
        loss=loss,
        kernel=kernel,
    )


def vector_field(
    state: State,
    X: Array,
    y: Array,
    adjoint_order: Optional[int] = None,
) -> Tuple[State, Cache]:
    cache = forward_and_adjoint(state, X, y, adjoint_order=adjoint_order)
    L = state.W.shape[0]
    n = state.W.shape[1]
    Wdot = np.empty_like(state.W)
    for ell in range(L):
        Wdot[ell] = -(
            cache.Beta[ell].T @ (cache.g[:, None] * cache.H[ell])
        ) / n
    adot = -(cache.g[:, None] * cache.H[-1]).sum(axis=0)
    Bdot = -(cache.g[:, None] * cache.gamma).T @ X
    return State(B=Bdot, W=Wdot, a=adot, gain=state.gain), cache


def heun_step(
    state: State,
    X: Array,
    y: Array,
    dt: float,
    adjoint_order: Optional[int] = None,
) -> State:
    k1, _ = vector_field(state, X, y, adjoint_order=adjoint_order)
    trial = add_state(state, k1, dt)
    k2, _ = vector_field(trial, X, y, adjoint_order=adjoint_order)
    return combine_heun(state, k1, k2, dt)


def gram_stack(cache: Cache) -> Array:
    n = cache.H[0].shape[1]
    return np.stack([h @ h.T / n for h in cache.H])


def train(
    state: State,
    X: Array,
    y: Array,
    T: float,
    dt: float,
    adjoint_order: Optional[int] = None,
    record_every: int = 1,
) -> Tuple[State, Dict[str, Array]]:
    steps = int(round(T / dt))
    dt = T / max(steps, 1)
    times: List[float] = []
    outputs: List[Array] = []
    losses: List[float] = []
    grams: List[Array] = []
    eigmins: List[float] = []
    states: List[State] = []
    x = state.clone()
    for step in range(steps + 1):
        if step % record_every == 0 or step == steps:
            c = forward_and_adjoint(x, X, y, adjoint_order=adjoint_order)
            times.append(step * dt)
            outputs.append(c.f.copy())
            losses.append(c.loss)
            grams.append(gram_stack(c))
            eigmins.append(float(np.linalg.eigvalsh(c.kernel).min()))
            states.append(x.clone())
        if step < steps:
            x = heun_step(x, X, y, dt, adjoint_order=adjoint_order)
    return x, {
        "time": np.asarray(times),
        "output": np.asarray(outputs),
        "loss": np.asarray(losses),
        "gram": np.asarray(grams),
        "kernel_eigmin": np.asarray(eigmins),
        "states": np.asarray(states, dtype=object),
    }


def interpolate_depth_grams(grams: Array, target_L: int) -> Array:
    """Interpolate (..., L+1, m, m) to target_L+1 depth points."""
    source_L = grams.shape[-3] - 1
    s0 = np.linspace(0.0, 1.0, source_L + 1)
    s1 = np.linspace(0.0, 1.0, target_L + 1)
    moved = np.moveaxis(grams, -3, -1)
    flat = moved.reshape((-1, source_L + 1))
    out = np.stack([np.interp(s1, s0, row) for row in flat])
    shape = moved.shape[:-1] + (target_L + 1,)
    out = out.reshape(shape)
    return np.moveaxis(out, -1, -3)


def finite_difference_scaling_audit(out_dir: Path) -> Dict[str, float]:
    n, L, d, m = 7, 5, 4, 3
    X, y = make_data(m, d, seed=11)
    state = initialize(n, L, d, seed=13, depth_mode="smooth")
    deriv, cache = vector_field(state, X, y)
    eps = 1e-6

    def loss_of(s: State) -> float:
        return forward_and_adjoint(s, X, y).loss

    checks: Dict[str, float] = {}
    probes = [
        ("a", (2,)),
        ("B", (3, 1)),
        ("W", (2, 4, 5)),
    ]
    for name, idx in probes:
        plus, minus = state.clone(), state.clone()
        arr_p = getattr(plus, name)
        arr_m = getattr(minus, name)
        arr_p[idx] += eps
        arr_m[idx] -= eps
        numerical = (loss_of(plus) - loss_of(minus)) / (2 * eps)
        if name == "a":
            analytic = -deriv.a[idx] / n
        elif name == "B":
            analytic = -deriv.B[idx] / n
        else:
            analytic = -deriv.W[idx] / L
        checks[f"{name}_abs_error"] = abs(float(numerical - analytic))
        checks[f"{name}_rel_error"] = abs(float(numerical - analytic)) / max(
            abs(float(numerical)), 1e-14
        )

    # Independent identity: f_dot = -Theta (f-y).
    h = 2e-7
    moved = add_state(state, deriv, h)
    fdot_num = (
        forward_and_adjoint(moved, X, y).f - cache.f
    ) / h
    fdot_kernel = -cache.kernel @ cache.g
    checks["kernel_identity_max_abs_error"] = float(
        np.max(np.abs(fdot_num - fdot_kernel))
    )
    (out_dir / "scaling_audit.json").write_text(
        json.dumps(checks, indent=2), encoding="utf-8"
    )
    return checks


def iid_depth_self_averaging(out_dir: Path) -> List[Dict[str, float]]:
    rows: List[Dict[str, float]] = []
    n, d, m = 40, 6, 3
    X, y = make_data(m, d, seed=19)
    for mode in ("iid", "smooth"):
        for L in (8, 16, 32, 64, 128):
            vals = []
            for seed in range(6):
                state = initialize(n, L, d, seed=100 + seed, depth_mode=mode)
                c = forward_and_adjoint(state, X, y)
                disp = np.linalg.norm(c.H[-1] - c.H[0]) / math.sqrt(n * m)
                vals.append(float(disp))
            rows.append(
                {
                    "depth_mode": mode,
                    "L": L,
                    "mean_terminal_displacement": float(np.mean(vals)),
                    "std_terminal_displacement": float(np.std(vals)),
                }
            )
    write_csv(out_dir / "depth_initialization_scaling.csv", rows)

    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    for mode, marker in (("iid", "o"), ("smooth", "s")):
        rr = [r for r in rows if r["depth_mode"] == mode]
        ax.errorbar(
            [r["L"] for r in rr],
            [r["mean_terminal_displacement"] for r in rr],
            yerr=[r["std_terminal_displacement"] for r in rr],
            marker=marker,
            capsize=3,
            label=mode,
        )
    ax.set_xscale("log", base=2)
    ax.set_yscale("log")
    ax.set_xlabel("depth L")
    ax.set_ylabel(r"$\|h^L-h^0\|/\sqrt{nm}$")
    ax.set_title("Initialization: iid depth self-averages; smooth depth does not")
    ax.grid(True, which="both", alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_dir / "depth_initialization_scaling.png", dpi=180)
    plt.close(fig)
    return rows


def depth_resolution_experiment(out_dir: Path) -> List[Dict[str, float]]:
    n, d, m = 24, 6, 3
    X, y = make_data(m, d, seed=23)
    T, dt = 1.2, 0.02
    runs: Dict[int, Dict[str, Array]] = {}
    for L in (12, 24, 48, 96):
        state = initialize(n, L, d, seed=29, depth_mode="smooth")
        _, hist = train(state, X, y, T=T, dt=dt, record_every=2)
        runs[L] = hist
    ref = runs[96]
    rows: List[Dict[str, float]] = []
    for L in (12, 24, 48):
        h = runs[L]
        g_interp = interpolate_depth_grams(h["gram"], target_L=96)
        out_err = float(np.max(np.abs(h["output"] - ref["output"])))
        gram_err = float(np.max(np.linalg.norm(g_interp - ref["gram"], axis=(-2, -1))))
        rows.append(
            {
                "L": L,
                "reference_L": 96,
                "sup_output_error": out_err,
                "sup_depth_gram_fro_error": gram_err,
            }
        )
    write_csv(out_dir / "smooth_depth_convergence.csv", rows)
    return rows


def _truncated_adjoint_from_cache(
    state: State,
    cache: Cache,
    order: int,
) -> Tuple[List[Array], List[Array]]:
    L = state.W.shape[0]
    delta = 1.0 / L
    pieces = [np.zeros_like(cache.H[-1]) for _ in range(order + 1)]
    pieces[0][...] = state.a
    Q = [np.empty_like(cache.H[0]) for _ in range(L + 1)]
    Q[L] = np.broadcast_to(state.a, cache.H[-1].shape).copy()
    for ell in range(L - 1, -1, -1):
        old = [p.copy() for p in pieces]
        for k in range(1, order + 1):
            pieces[k] = old[k] + delta * (
                (cache.D[ell] * old[k - 1]) @ state.W[ell]
            )
        pieces[0] = old[0]
        Q[ell] = sum(pieces)
    beta = [cache.D[ell] * Q[ell + 1] for ell in range(L)]
    return Q, beta


def response_snapshot_audit(
    state: State,
    X: Array,
    y: Array,
    orders: Sequence[int],
    out_dir: Path,
    tag: str,
) -> Tuple[List[Dict[str, float]], Array]:
    cache = forward_and_adjoint(state, X, y)
    L, n, _ = state.W.shape
    delta = 1.0 / L
    rows: List[Dict[str, float]] = []
    exact_q_norm = math.sqrt(
        sum(float(np.sum(q * q)) for q in cache.Q)
        / ((L + 1) * cache.Q[0].size)
    )

    for M in orders:
        Qm, betam = _truncated_adjoint_from_cache(state, cache, M)
        qerr = math.sqrt(
            sum(float(np.sum((Qm[k] - cache.Q[k]) ** 2)) for k in range(L + 1))
            / ((L + 1) * cache.Q[0].size)
        )
        gamma_m = cache.d0 * Qm[0]
        K = cache.H[-1] @ cache.H[-1].T / n
        K += (X @ X.T) * (gamma_m @ gamma_m.T / n)
        for ell in range(L):
            Gh = cache.H[ell] @ cache.H[ell].T / n
            Gb = betam[ell] @ betam[ell].T / n
            K += delta * Gh * Gb
        rows.append(
            {
                "tag": tag,
                "order": M,
                "adjoint_rms_error": qerr,
                "adjoint_relative_rms_error": qerr / max(exact_q_norm, 1e-14),
                "kernel_fro_error": float(np.linalg.norm(K - cache.kernel)),
                "reconstructed_psd_kernel_action_error": float(
                    np.linalg.norm((K - cache.kernel) @ cache.g)
                ),
                "reconstructed_psd_kernel_min_eigenvalue": float(
                    np.linalg.eigvalsh(K).min()
                ),
                "exact_kernel_min_eigenvalue": float(
                    np.linalg.eigvalsh(cache.kernel).min()
                ),
            }
        )

    # Build a representative scalar two-depth response field and its SVD.
    r = 0
    qsrc = min(1, len(y) - 1)
    R = np.zeros((L + 1, L + 1))
    for u in range(L):
        v = cache.D[u][r] * cache.Beta[u][qsrc]
        R[u, u] = float(cache.H[u][r] @ v) / n
        cur = v.copy()
        for ell in range(u, L):
            cur = cur + delta * (
                cache.D[ell][r] * (state.W[ell] @ cur)
            )
            R[ell + 1, u] = float(cache.H[ell + 1][r] @ cur) / n
    singular = np.linalg.svd(R, compute_uv=False)
    np.save(out_dir / f"response_singular_values_{tag}.npy", singular)
    write_csv(out_dir / f"response_snapshot_{tag}.csv", rows)

    gram_rows: List[Dict[str, float]] = []
    m = len(y)
    for ell in range(L + 1):
        gh = cache.H[ell] @ cache.H[ell].T / n
        gq = cache.Q[ell] @ cache.Q[ell].T / n
        gb = (
            cache.Beta[ell] @ cache.Beta[ell].T / n
            if ell < L
            else np.full((m, m), np.nan)
        )
        for r_idx in range(m):
            for q_idx in range(m):
                gram_rows.append(
                    {
                        "tag": tag,
                        "depth_index": ell,
                        "depth": ell / L,
                        "sample_r": r_idx,
                        "sample_q": q_idx,
                        "forward_h_gram": float(gh[r_idx, q_idx]),
                        "adjoint_q_gram": float(gq[r_idx, q_idx]),
                        "backprop_beta_gram": float(gb[r_idx, q_idx]),
                    }
                )
    write_csv(out_dir / f"gram_fields_{tag}_final.csv", gram_rows)
    return rows, singular


def compare_histories(ref: Dict[str, Array], approx: Dict[str, Array]) -> Dict[str, float]:
    if len(ref["time"]) != len(approx["time"]):
        raise ValueError("history grids differ")
    out_err_t = np.linalg.norm(ref["output"] - approx["output"], axis=-1)
    gram_diff = ref["gram"] - approx["gram"]
    gram_err_t = np.max(np.linalg.norm(gram_diff, axis=(-2, -1)), axis=-1)
    return {
        "sup_output_l2_error": float(np.max(out_err_t)),
        "sup_all_depth_gram_fro_error": float(np.max(gram_err_t)),
        "final_output_l2_error": float(out_err_t[-1]),
        "final_all_depth_gram_fro_error": float(gram_err_t[-1]),
        "min_reconstructed_psd_kernel_eigenvalue": float(
            np.min(approx["kernel_eigmin"])
        ),
    }


def truncated_training_experiment(out_dir: Path) -> List[Dict[str, float]]:
    configs = [
        ("smooth_generic", "smooth", "generic", 0.0),
        ("iid_generic", "iid", "generic", 0.0),
        ("smooth_nonnormal", "smooth", "generic", 2.5),
        ("smooth_aligned", "smooth", "aligned", 0.0),
    ]
    rows: List[Dict[str, float]] = []
    n, L, d, m = 24, 40, 6, 3
    T, dt = 1.6, 0.025
    for ci, (tag, mode, data_case, nonnormal) in enumerate(configs):
        X, y = make_data(m, d, seed=41 + ci, case=data_case)
        initial = initialize(
            n,
            L,
            d,
            seed=53 + ci,
            depth_mode=mode,
            nonnormal_strength=nonnormal,
        )
        ref_state, ref = train(initial, X, y, T=T, dt=dt, record_every=2)
        gram_motion = float(
            np.max(
                np.linalg.norm(
                    ref["gram"][-1] - ref["gram"][0], axis=(-2, -1)
                )
            )
        )
        output_motion = float(np.linalg.norm(ref["output"][-1] - ref["output"][0]))
        residual_l1 = float(
            np.trapezoid(
                np.linalg.norm(ref["output"] - y[None, :], axis=1),
                ref["time"],
            )
        )
        for M in (1, 2, 4, 6, 8):
            _, approx = train(
                initial,
                X,
                y,
                T=T,
                dt=dt,
                adjoint_order=M,
                record_every=2,
            )
            result = compare_histories(ref, approx)
            result.update(
                {
                    "tag": tag,
                    "order": M,
                    "T": T,
                    "reference_final_loss": float(ref["loss"][-1]),
                    "approx_final_loss": float(approx["loss"][-1]),
                    "reference_max_depth_gram_motion": gram_motion,
                    "reference_output_motion": output_motion,
                    "reference_residual_L1": residual_l1,
                }
            )
            rows.append(result)
        response_snapshot_audit(
            ref_state,
            X,
            y,
            orders=(0, 1, 2, 4, 6, 8, 10),
            out_dir=out_dir,
            tag=tag,
        )
    write_csv(out_dir / "truncated_training.csv", rows)

    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.2))
    for tag, _, _, _ in configs:
        rr = [r for r in rows if r["tag"] == tag]
        axes[0].semilogy(
            [r["order"] for r in rr],
            [max(r["sup_output_l2_error"], 1e-15) for r in rr],
            marker="o",
            label=tag,
        )
        axes[1].semilogy(
            [r["order"] for r in rr],
            [max(r["sup_all_depth_gram_fro_error"], 1e-15) for r in rr],
            marker="o",
            label=tag,
        )
    axes[0].set_title("Truncated-response training: output")
    axes[1].set_title("Truncated-response training: hidden Grams")
    for ax in axes:
        ax.set_xlabel("Dyson/backprop word order M")
        ax.grid(True, which="both", alpha=0.25)
    axes[0].set_ylabel("sup error")
    axes[1].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out_dir / "truncated_training_errors.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    for tag, _, _, _ in configs:
        sv = np.load(out_dir / f"response_singular_values_{tag}.npy")
        ax.semilogy(
            np.arange(1, min(25, len(sv)) + 1),
            np.maximum(sv[:25] / max(sv[0], 1e-30), 1e-16),
            marker=".",
            label=tag,
        )
    ax.set_xlabel("singular-value index")
    ax.set_ylabel(r"$\sigma_k/\sigma_1$")
    ax.set_title("Representative two-depth response contraction")
    ax.grid(True, which="both", alpha=0.25)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out_dir / "response_singular_value_decay.png", dpi=180)
    plt.close(fig)
    return rows


def restart_and_horizon_experiment(out_dir: Path) -> Tuple[List[Dict[str, float]], List[Dict[str, float]]]:
    n, L, d, m = 22, 36, 6, 3
    X, y = make_data(m, d, seed=71)
    initial = initialize(n, L, d, seed=73, depth_mode="smooth")

    # Horizon audit: a single long run per order, then prefix suprema.
    T, dt = 3.2, 0.025
    _, ref = train(initial, X, y, T=T, dt=dt, record_every=2)
    horizon_rows: List[Dict[str, float]] = []
    for M in (1, 2, 4, 6, 8):
        _, approx = train(
            initial,
            X,
            y,
            T=T,
            dt=dt,
            adjoint_order=M,
            record_every=2,
        )
        for horizon in (0.4, 0.8, 1.6, 3.2):
            mask = ref["time"] <= horizon + 1e-12
            sub_ref = {k: v[mask] for k, v in ref.items() if k not in ("states",)}
            sub_app = {k: v[mask] for k, v in approx.items() if k not in ("states",)}
            result = compare_histories(sub_ref, sub_app)
            result.update(
                {
                    "order": M,
                    "horizon": horizon,
                    "reference_final_loss": float(sub_ref["loss"][-1]),
                    "reference_residual_L1": float(
                        np.trapezoid(
                            np.linalg.norm(
                                sub_ref["output"] - y[None, :], axis=1
                            ),
                            sub_ref["time"],
                        )
                    ),
                }
            )
            horizon_rows.append(result)
    write_csv(out_dir / "horizon_stabilization.csv", horizon_rows)

    # Restart at positive time, with label perturbation and a small state perturbation.
    _, pre = train(initial, X, y, T=0.6, dt=dt, record_every=1)
    restart_state = pre["states"][-1].clone()
    rng = np.random.default_rng(79)
    perturbed_state = restart_state.clone()
    perturbed_state.B += 2e-3 * rng.normal(size=perturbed_state.B.shape)
    perturbed_state.W += 2e-4 * rng.normal(size=perturbed_state.W.shape)
    y2 = y + np.array([0.03, -0.02, 0.015])

    restart_rows: List[Dict[str, float]] = []
    for restart_tag, rs, labels in (
        ("exact_state_new_labels", restart_state, y2),
        ("perturbed_state_new_labels", perturbed_state, y2),
    ):
        _, rr = train(rs, X, labels, T=1.2, dt=dt, record_every=2)
        for M in (2, 4, 6, 8):
            _, aa = train(
                rs,
                X,
                labels,
                T=1.2,
                dt=dt,
                adjoint_order=M,
                record_every=2,
            )
            result = compare_histories(rr, aa)
            result.update({"restart_tag": restart_tag, "order": M})
            restart_rows.append(result)
    write_csv(out_dir / "restart_robustness.csv", restart_rows)
    return horizon_rows, restart_rows


def parameter_grid_experiment(out_dir: Path) -> List[Dict[str, float]]:
    """Small Latin-hypercube sweep over n, L, m, seeds, labels, and activation gain."""
    designs = [
        # n, L, m, gain, label scale, depth mode
        (16, 16, 2, 0.70, 0.65, "iid"),
        (16, 48, 4, 1.00, 1.25, "smooth"),
        (24, 24, 3, 1.30, 0.90, "iid"),
        (24, 64, 2, 0.85, 1.40, "smooth"),
        (32, 32, 4, 1.15, 0.75, "iid"),
        (32, 48, 3, 1.40, 1.10, "smooth"),
    ]
    rows: List[Dict[str, float]] = []
    d = 7
    for design_id, (n, L, m, gain, label_scale, mode) in enumerate(designs):
        for seed_offset in (0, 1):
            seed = 131 + 17 * design_id + seed_offset
            X, y = make_data(m, d, seed=seed)
            y = label_scale * y
            initial = initialize(
                n,
                L,
                d,
                seed=seed + 5,
                depth_mode=mode,
                gain=gain,
            )
            _, ref = train(initial, X, y, T=0.8, dt=0.025, record_every=2)
            _, approx = train(
                initial,
                X,
                y,
                T=0.8,
                dt=0.025,
                adjoint_order=4,
                record_every=2,
            )
            result = compare_histories(ref, approx)
            result.update(
                {
                    "design_id": design_id,
                    "seed": seed,
                    "n": n,
                    "L": L,
                    "m": m,
                    "activation_gain": gain,
                    "label_scale": label_scale,
                    "depth_mode": mode,
                    "reference_final_loss": float(ref["loss"][-1]),
                    "exact_kernel_min_eigenvalue": float(
                        np.min(ref["kernel_eigmin"])
                    ),
                }
            )
            rows.append(result)
    write_csv(out_dir / "parameter_grid.csv", rows)
    return rows


def write_csv(path: Path, rows: Sequence[Dict[str, object]]) -> None:
    if not rows:
        return
    keys: List[str] = []
    seen = set()
    for row in rows:
        for key in row:
            if key not in seen:
                keys.append(key)
                seen.add(key)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def summarize(out_dir: Path, payload: Dict[str, object]) -> None:
    (out_dir / "summary.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="results")
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Run only normalization and initialization-depth audits.",
    )
    args = parser.parse_args()
    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    payload: Dict[str, object] = {}
    payload["scaling"] = finite_difference_scaling_audit(out_dir)
    payload["depth_initialization"] = iid_depth_self_averaging(out_dir)
    if not args.quick:
        payload["smooth_depth_convergence"] = depth_resolution_experiment(out_dir)
        payload["truncated_training"] = truncated_training_experiment(out_dir)
        horizon, restart = restart_and_horizon_experiment(out_dir)
        payload["horizon"] = horizon
        payload["restart"] = restart
        payload["parameter_grid"] = parameter_grid_experiment(out_dir)
    summarize(out_dir, payload)
    print(json.dumps({"status": "ok", "out": str(out_dir)}, indent=2))


if __name__ == "__main__":
    main()
