#!/usr/bin/env python3
"""Frozen stopped-typical pair-median common-clock/Loewner experiment."""

from __future__ import annotations

import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
             "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_key] = "6"

import hashlib
import json
import math
import platform
import resource
import sys
from pathlib import Path

import numpy as np
from numpy.polynomial import Polynomial

HERE = Path(__file__).resolve().parent
DIRECT = HERE.parent / "direct_loewner"
sys.path.insert(0, str(DIRECT))
sys.path.insert(0, str(HERE))
import simulate_loewner as model  # noqa: E402
from corrected_clock_core import cumulative_simpson_uniform  # noqa: E402
from jet_control_variate import taylor_jet  # noqa: E402

WIDTHS = (128, 256)
PAIR_COUNT = 224
BATCH = 8
PAIR_SEED_BASE = 91723651
STEP = 0.00005
HALF_STEP = 0.000025
S_MAX = 0.003
HALF_PAIRS = 16
STATE_CEILING = 1e12
BOOTSTRAPS = 5000
Y_NODES = np.array([0.04, 0.08, 0.12, 0.16])
X_NODES = Y_NODES**2
R0 = 280864.0 / 4107.0
R1 = -38443196932.0 / 5616860517.0
R2 = 37578479127292096 / 12802987609542045
G0 = 111.0
G2 = 842592.0
AS_CAP = 8 * 1024**3
OUTPUT = HERE / "runs/positive_time_pair_median_run"
PROTOCOL = HERE / "POSITIVE_TIME_PROTOCOL.md"
LOCAL_ARCHIVE = HERE / "runs/fresh_pair_median_run"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def set_memory_cap() -> None:
    soft0, hard0 = resource.getrlimit(resource.RLIMIT_AS)
    hard = AS_CAP if hard0 == resource.RLIM_INFINITY else min(hard0, AS_CAP)
    resource.setrlimit(resource.RLIMIT_AS, (min(AS_CAP, hard), hard))


def log_factory(path: Path):
    handle = path.open("w")
    def log(message: str):
        print(message, flush=True)
        print(message, file=handle, flush=True)
    return log, handle


def generate(width: int, first: int, count: int) -> model.State:
    a0 = np.empty((count, width))
    u0 = np.empty_like(a0)
    W0 = np.empty((count, width, width))
    for local, index in enumerate(range(first, first + count)):
        rng = np.random.default_rng(np.random.SeedSequence([PAIR_SEED_BASE, width, index]))
        a0[local] = rng.standard_normal(width)
        u0[local] = rng.standard_normal(width)
        W0[local] = rng.standard_normal((width, width))
    a = np.stack((a0, -a0), axis=1).reshape(2 * count, width)
    u = np.repeat(u0[:, None, :], 2, axis=1).reshape(2 * count, width)
    W = np.repeat(W0[:, None, :, :], 2, axis=1).reshape(2 * count, width, width)
    return model.State(a, W, u)


def pair_mean(values: np.ndarray) -> np.ndarray:
    return values.reshape(len(values) // 2, 2).mean(axis=1)


def simulate_batch(width: int, first: int, count: int, step: float):
    steps = round(S_MAX / step)
    times = np.arange(steps + 1) * step
    state = generate(width, first, count)
    jet = taylor_jet(state, 5).reshape(count, 2, 6).mean(axis=1)
    c0, c2 = jet[:, 1], 3.0 * jet[:, 3]
    raw = np.full((count, steps + 1), 111.0 * width)
    stopped = np.zeros(2 * count, dtype=bool)
    stop_time = np.full(2 * count, np.nan)
    kval, _ = model.observable_and_derivative(state)
    raw[:, 0] = np.clip(pair_mean(kval), 0.0, 111.0 * width)
    for t in range(1, steps + 1):
        with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
            state = model.rk4_step(state, step)
        amp = np.maximum.reduce((np.max(np.abs(state.a), axis=1),
                                 np.max(np.abs(state.W), axis=(1, 2)),
                                 np.max(np.abs(state.u), axis=1)))
        dead = (~np.isfinite(amp)) | (amp >= STATE_CEILING)
        new = dead & ~stopped
        stop_time[new] = times[t]
        stopped |= dead
        if np.any(stopped):
            state.a[stopped] = 0.0
            state.W[stopped] = 0.0
            state.u[stopped] = 0.0
        kval, _ = model.observable_and_derivative(state)
        pair_alive = ~stopped.reshape(count, 2).any(axis=1)
        values = pair_mean(kval)
        values[~pair_alive] = 111.0 * width
        raw[:, t] = np.clip(values, 0.0, 111.0 * width)
    cv = raw + (G0 - c0)[:, None] + (G2 - c2)[:, None] * times[None, :]**2
    return times, raw, cv, jet, stop_time


def simulate_width(width: int, step: float, count: int, log):
    pieces = []
    for first in range(0, count, BATCH):
        size = min(BATCH, count - first)
        pieces.append(simulate_batch(width, first, size, step))
        log(f"width={width} step={step} completed={first + size}/{count}")
    times = pieces[0][0]
    return {"times": times,
            "raw": np.concatenate([p[1] for p in pieces]),
            "cv": np.concatenate([p[2] for p in pieces]),
            "jet": np.concatenate([p[3] for p in pieces]),
            "stop_time": np.concatenate([p[4] for p in pieces])}


def loewner(r, rp):
    A = np.empty((4, 4)); B = np.empty((4, 4))
    for i in range(4):
        for j in range(4):
            if i == j:
                A[i, i] = -rp[i]; B[i, i] = r[i] + X_NODES[i] * rp[i]
            else:
                dx = X_NODES[i] - X_NODES[j]
                A[i, j] = -(r[i] - r[j]) / dx
                B[i, j] = (X_NODES[i] * r[i] - X_NODES[j] * r[j]) / dx
    return A, B


def proxy(curves, times, degree=3, window=(0.02, 0.18)):
    G = np.median(curves, axis=0)
    F = cumulative_simpson_uniform(G, times[1] - times[0])
    if not np.all(np.diff(F) > 0) or F[-1] < 0.18:
        raise ValueError("clock invalid")
    X = F**2
    mask = (F >= window[0]) & (F <= window[1])
    rawR = (G[mask] - G0) / X[mask]
    qdata = (rawR - R0) / X[mask]
    fit = Polynomial.fit(X[mask], qdata, degree, domain=(window[0]**2, window[1]**2))
    q = fit(X_NODES); qp = fit.deriv()(X_NODES)
    r = R0 + X_NODES * q
    rp = q + X_NODES * qp
    A, B = loewner(r, rp)
    residual = R0 + X[mask] * fit(X[mask]) - rawR
    return {"G": G, "F": F, "q0": float(fit(0)), "q1": float(fit.deriv()(0)),
            "r": r, "rp": rp, "A": A, "B": B,
            "fit_rms": float(np.sqrt(np.mean(residual**2))),
            "fit_max": float(np.max(np.abs(residual)))}


def json_proxy(p):
    return {k: (v.tolist() if isinstance(v, np.ndarray) else v)
            for k, v in p.items() if k not in ("G", "F")}


def bootstrap_local(curves, times, width):
    rng = np.random.default_rng(np.random.SeedSequence([731902, width, 0]))
    q0 = np.empty(BOOTSTRAPS); q1 = np.empty(BOOTSTRAPS)
    for b in range(BOOTSTRAPS):
        idx = rng.integers(0, len(curves), len(curves))
        p = proxy(curves[idx], times)
        q0[b], q1[b] = p["q0"], p["q1"]
    return q0, q1


def bootstrap_scores(curves, times, width, vectors):
    rng = np.random.default_rng(np.random.SeedSequence([731902, width, 1]))
    out = {"A": np.empty(BOOTSTRAPS), "B": np.empty(BOOTSTRAPS)}
    for b in range(BOOTSTRAPS):
        idx = rng.integers(0, len(curves), len(curves))
        p = proxy(curves[idx], times)
        for name in ("A", "B"):
            out[name][b] = vectors[name] @ p[name] @ vectors[name]
    return out


def qsummary(x):
    return {"mean": float(np.mean(x)), "sd": float(np.std(x, ddof=1)),
            "q0025": float(np.quantile(x, .0025)),
            "q005": float(np.quantile(x, .005)), "q025": float(np.quantile(x, .025)),
            "q975": float(np.quantile(x, .975)), "q995": float(np.quantile(x, .995)),
            "q9975": float(np.quantile(x, .9975))}


def atomic(lambdas, weights):
    lam = np.asarray(lambdas); w = np.asarray(weights)
    den = 1 + X_NODES[:, None] * lam
    r = np.sum(w / den, axis=1); rp = -np.sum(w * lam / den**2, axis=1)
    A, B = loewner(r, rp)
    return {"A_eigenvalues": np.linalg.eigvalsh(A).tolist(),
            "B_eigenvalues": np.linalg.eigvalsh(B).tolist()}


def main():
    set_memory_cap()
    OUTPUT.mkdir(exist_ok=False)
    log, handle = log_factory(OUTPUT / "console.log")
    sources = [PROTOCOL, Path(__file__).resolve(), DIRECT / "simulate_loewner.py",
               DIRECT / "corrected_clock_core.py", HERE / "jet_control_variate.py"]
    result = {"status": "running", "sources": {str(p): digest(p) for p in sources},
              "environment": {"python": sys.version, "numpy": np.__version__,
                              "platform": platform.platform(), "address_cap": AS_CAP,
                              "threads": 6}, "widths": {},
              "exact": {"R0": R0, "R1": R1, "R2": R2},
              "controls": {"two_atom": atomic((10, 100), (.6, .4)),
                           "three_atom": atomic((5, 40, 160), (.5, .3, .2))}}
    bootstrap_raw = {}
    for width in WIDTHS:
        data = simulate_width(width, STEP, PAIR_COUNT, log)
        half = simulate_width(width, HALF_STEP, HALF_PAIRS, log)
        archived = np.load(LOCAL_ARCHIVE / f"pair_values_width_{width}.npz")["f5"]
        f5 = data["jet"][:, 5]
        jet_rel = float(np.max(np.abs(f5 - archived) / np.maximum(1, np.abs(archived))))
        np.savez_compressed(OUTPUT / f"raw_width_{width}.npz", **data)
        np.savez_compressed(OUTPUT / f"half_step_width_{width}.npz", **half)
        full = proxy(data["cv"], data["times"])
        discovery = proxy(data["cv"][:112], data["times"])
        confirmation = proxy(data["cv"][112:], data["times"])
        vectors = {}
        for name in ("A", "B"):
            _, v = np.linalg.eigh(discovery[name]); vectors[name] = v[:, 0]
        score_samples = bootstrap_scores(data["cv"][112:], data["times"], width, vectors)
        q0s, q1s = bootstrap_local(data["cv"], data["times"], width)
        bootstrap_raw[width] = (score_samples, q0s, q1s)
        np.savez_compressed(OUTPUT / f"bootstrap_width_{width}.npz",
                            score_A=score_samples["A"], score_B=score_samples["B"],
                            q0=q0s, q1=q1s)
        sensitivities = {}
        for degree, window in ((2, (.02, .18)), (4, (.02, .18)),
                               (3, (.02, .16)), (3, (.03, .18))):
            key = f"degree{degree}_window{window[0]}_{window[1]}"
            pf = proxy(data["cv"], data["times"], degree, window)
            pc = proxy(data["cv"][112:], data["times"], degree, window)
            sensitivities[key] = {"full": json_proxy(pf),
                                  "confirmation_scores": {name: float(vectors[name] @ pc[name] @ vectors[name])
                                                          for name in ("A", "B")}}
        coarse16 = proxy(data["cv"][:HALF_PAIRS], data["times"])
        fine16 = proxy(half["cv"], half["times"])
        coarse_at_fine = half["cv"][:, ::2]
        g_rel = float(np.max(np.abs(coarse_at_fine - data["cv"][:HALF_PAIRS]) /
                             np.maximum(G0, np.abs(coarse_at_fine))))
        step_matrix = {name: {"relative_spectral": float(np.linalg.norm(fine16[name] - coarse16[name], 2) /
                                                           max(1.0, np.linalg.norm(fine16[name], 2)))}
                       for name in ("A", "B")}
        stopped_pairs = int(np.sum(np.isfinite(data["stop_time"].reshape(PAIR_COUNT, 2)).any(axis=1)))
        cap = 111.0 * width
        median_at_cap = bool(np.any(np.median(data["raw"], axis=0) >= cap))
        width_record = {"jet_archive_max_relative_error": jet_rel,
                        "stopped_pairs": stopped_pairs, "median_at_cap": median_at_cap,
                        "full": json_proxy(full), "discovery": json_proxy(discovery),
                        "confirmation": json_proxy(confirmation),
                        "discovery_vectors": {k: v.tolist() for k, v in vectors.items()},
                        "confirmation": {**json_proxy(confirmation),
                            "scores": {name: float(vectors[name] @ confirmation[name] @ vectors[name])
                                       for name in ("A", "B")}},
                        "bootstrap_local": {"q0": qsummary(q0s), "q1": qsummary(q1s)},
                        "bootstrap_scores": {name: qsummary(vals) for name, vals in score_samples.items()},
                        "sensitivities": sensitivities,
                        "step_halving": {"max_relative_pair_kernel": g_rel, "matrices": step_matrix}}
        result["widths"][str(width)] = width_record
    # All gates are evaluated only after both widths are complete.
    gates = {}
    for width in WIDTHS:
        w = result["widths"][str(width)]; b = w["bootstrap_local"]
        gates[f"clock_and_fit_{width}"] = w["full"]["fit_max"] <= 1e-5
        gates[f"q0_{width}"] = b["q0"]["q025"] <= R1 <= b["q0"]["q975"] and (b["q0"]["q975"] - b["q0"]["q025"] <= 10)
        gates[f"degree_sensitivity_{width}"] = all(
            abs(s["full"]["q0"] - w["full"]["q0"]) <= 1 and
            abs(s["full"]["q1"] - w["full"]["q1"]) <= 5
            for k, s in w["sensitivities"].items() if "window0.02_0.18" in k)
        gates[f"step_{width}"] = w["step_halving"]["max_relative_pair_kernel"] <= 1e-5 and all(
            x["relative_spectral"] <= 1e-3 for x in w["step_halving"]["matrices"].values())
        gates[f"stop_{width}"] = w["stopped_pairs"] <= .05 * PAIR_COUNT and not w["median_at_cap"]
        gates[f"jet_{width}"] = w["jet_archive_max_relative_error"] <= 1e-12
    b256 = result["widths"]["256"]["bootstrap_local"]["q1"]
    gates["heldout_q1_256"] = b256["q025"] <= R2 <= b256["q975"] and b256["q975"] - b256["q025"] <= 25
    q128 = result["widths"]["128"]["full"]["q1"]; q256 = result["widths"]["256"]["full"]["q1"]
    gates["heldout_cross_width"] = q128 > 0 and abs(q128 - q256) <= 10
    controls_ok = all(min(c[name]) >= -1e-10 for c in result["controls"].values()
                      for name in ("A_eigenvalues", "B_eigenvalues"))
    gates["atomic_controls"] = controls_ok
    valid = all(gates.values())
    inference = {"valid": valid, "classification": "invalid_inconclusive"}
    if valid:
        negative = []
        for name in ("A", "B"):
            ok = True; primary = []
            for width in WIDTHS:
                w = result["widths"][str(width)]
                upper = w["bootstrap_scores"][name]["q9975"]
                primary.append(w["confirmation"]["scores"][name])
                sensitivity_negative = all(s["confirmation_scores"][name] < 0 for s in w["sensitivities"].values())
                ok &= upper < 0 and sensitivity_negative
            ratio = abs(primary[1]) / max(1e-300, abs(primary[0]))
            if ok and .25 <= ratio <= 4: negative.append(name)
        compatible = True
        for width in WIDTHS:
            w = result["widths"][str(width)]
            for name in ("A", "B"):
                compatible &= w["bootstrap_scores"][name]["q0025"] >= 0
                compatible &= all(s["confirmation_scores"][name] >= 0 for s in w["sensitivities"].values())
        if negative:
            inference = {"valid": True, "classification": "empirical_negative_signal", "matrices": negative}
        elif compatible:
            inference = {"valid": True, "classification": "finite_node_compatibility"}
        else:
            inference = {"valid": True, "classification": "loewner_inconclusive"}
    result["gates"] = gates; result["inference"] = inference
    result["status"] = inference["classification"]
    result["peak_rss_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    (OUTPUT / "results.json").write_text(json.dumps(result, indent=2) + "\n")
    log(json.dumps({"status": result["status"], "gates": gates, "inference": inference}, indent=2))
    handle.close()

if __name__ == "__main__":
    main()
