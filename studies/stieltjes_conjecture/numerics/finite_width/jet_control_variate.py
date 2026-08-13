#!/usr/bin/env python3
"""Exact per-initialization Taylor jets and a preregistered CV proxy audit."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
from numpy.polynomial import Polynomial


HERE = Path(__file__).resolve().parent
DIRECT = HERE.parent / "direct_loewner"
sys.path.insert(0, str(DIRECT))
import corrected_clock_core as core  # noqa: E402


RUN = DIRECT / "runs/corrected_clock_run_20260814"
OUT = HERE / "runs/run_jet_cv_20260814"
WIDTHS = (64, 128, 256)
PAIR_COUNTS = {64: 140, 128: 70, 256: 70}
BATCH_PAIRS = 35
SEED_BASE = 2026081401
Y_NODES = np.array([0.04, 0.08, 0.12, 0.16])
X_NODES = Y_NODES**2
FIT_Y_MIN = 0.02
FIT_Y_MAX = 0.18
R0 = 280864.0 / 4107.0
R1 = -38443196932.0 / 5616860517.0
G0 = 111.0
G2 = 1685184.0 / 2.0
BOOTSTRAPS = 2000


def taylor_jet(state, order: int = 5) -> np.ndarray:
    """Ordinary f(s) coefficients for a small batch of canonical states."""
    batch, n = state.a.shape
    u = [state.u.copy()] + [np.zeros_like(state.u) for _ in range(order)]
    c = [state.a.copy()] + [np.zeros_like(state.a) for _ in range(order)]
    # B=W/sqrt(n), so the canonical equations have no hidden scaling below.
    B = [state.W.copy() / math.sqrt(n)] + [np.zeros_like(state.W) for _ in range(order)]
    v = [np.zeros_like(state.a) for _ in range(order + 1)]
    f = np.zeros((batch, order + 1), dtype=np.float64)

    def update_vf(k: int) -> None:
        vk = np.zeros_like(v[0])
        for p in range(k + 1):
            for q in range(k - p + 1):
                vk += np.einsum(
                    "bij,bj->bi", B[p], u[q] * u[k - p - q], optimize=True
                )
        v[k] = vk
        fk = np.zeros(batch)
        for p in range(k + 1):
            for q in range(k - p + 1):
                fk += np.sum(c[p] * v[q] * v[k - p - q], axis=1)
        f[:, k] = fk / n

    update_vf(0)
    for k in range(order):
        urhs = np.zeros_like(u[0])
        Brhs = np.zeros_like(B[0])
        for p in range(k + 1):
            for q in range(k - p + 1):
                for r in range(k - p - q + 1):
                    t = k - p - q - r
                    urhs += u[p] * np.einsum(
                        "bij,bi->bj", B[q], c[r] * v[t], optimize=True
                    )
                    Brhs += (
                        (c[p] * v[q])[:, :, None]
                        * (u[r] * u[t])[:, None, :]
                    )
        u[k + 1] = 4.0 * urhs / (k + 1)
        B[k + 1] = (2.0 / n) * Brhs / (k + 1)
        crhs = np.zeros_like(c[0])
        for p in range(k + 1):
            crhs += v[p] * v[k - p]
        c[k + 1] = crhs / (k + 1)
        update_vf(k + 1)
    return f


def regenerate_pair_jets(width: int) -> np.ndarray:
    chunks = []
    batches = PAIR_COUNTS[width] // BATCH_PAIRS
    for b in range(batches):
        state = core.generate_state(width, BATCH_PAIRS, SEED_BASE + b)
        jets = taylor_jet(state, 5).reshape(BATCH_PAIRS, 2, 6).mean(axis=1)
        chunks.append(jets)
    return np.concatenate(chunks, axis=0)


def aggregate(curves: np.ndarray, width: int, kind: str) -> np.ndarray:
    if kind == "mom7":
        return core.median_of_means(curves, 7, 111.0 * math.sqrt(width))
    if kind == "mom5":
        return core.median_of_means(curves, 5, 111.0 * math.sqrt(width))
    if kind == "mean":
        return np.mean(curves, axis=0)
    raise ValueError(kind)


def loewner(r: np.ndarray, rp: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    A = np.empty((4, 4))
    B = np.empty((4, 4))
    for i in range(4):
        for j in range(4):
            if i == j:
                A[i, i] = -rp[i]
                B[i, i] = r[i] + X_NODES[i] * rp[i]
            else:
                dx = X_NODES[i] - X_NODES[j]
                A[i, j] = -(r[i] - r[j]) / dx
                B[i, j] = (X_NODES[i] * r[i] - X_NODES[j] * r[j]) / dx
    return A, B


def proxy(curves: np.ndarray, times: np.ndarray, width: int, kind: str, degree: int):
    G = aggregate(curves, width, kind)
    F = core.cumulative_simpson_uniform(G, times[1] - times[0])
    if not np.all(np.diff(F) > 0) or F[-1] < FIT_Y_MAX:
        raise ValueError("invalid common clock")
    X = F**2
    mask = (F >= FIT_Y_MIN) & (F <= FIT_Y_MAX)
    raw_R = (G[mask] - G0) / X[mask]
    # Enforce the known intercept, and fit only the residual quotient q.
    q_data = (raw_R - R0) / X[mask]
    qfit = Polynomial.fit(X[mask], q_data, degree, domain=(FIT_Y_MIN**2, FIT_Y_MAX**2))
    q = qfit(X_NODES)
    qp = qfit.deriv()(X_NODES)
    r = R0 + X_NODES * q
    rp = q + X_NODES * qp
    A, B = loewner(r, rp)
    residual = R0 + X[mask] * qfit(X[mask]) - raw_R
    return {
        "G": G,
        "F": F,
        "q0": float(qfit(0.0)),
        "r": r,
        "rp": rp,
        "A": A,
        "B": B,
        "fit_rms": float(np.sqrt(np.mean(residual**2))),
        "fit_max": float(np.max(np.abs(residual))),
        "R0_numeric": float((G[1] - G0) / F[1] ** 2),
    }


def bootstrap(curves, times, width, kind, degree, seed):
    rng = np.random.default_rng(seed)
    q0 = []
    amin = []
    bmin = []
    for _ in range(BOOTSTRAPS):
        idx = rng.integers(0, len(curves), len(curves))
        try:
            p = proxy(curves[idx], times, width, kind, degree)
            q0.append(p["q0"])
            amin.append(np.linalg.eigvalsh(p["A"])[0])
            bmin.append(np.linalg.eigvalsh(p["B"])[0])
        except (ValueError, np.linalg.LinAlgError):
            pass
    def stats(x):
        a = np.asarray(x)
        return {
            "count": len(a), "mean": float(np.mean(a)), "sd": float(np.std(a, ddof=1)),
            "q005": float(np.quantile(a, 0.005)), "q025": float(np.quantile(a, 0.025)),
            "q975": float(np.quantile(a, 0.975)), "q995": float(np.quantile(a, 0.995)),
        }
    return {"q0": stats(q0), "A_min": stats(amin), "B_min": stats(bmin)}


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    results = {"constants": {"R0": R0, "held_out_R1": R1, "G0": G0, "G2": G2}, "widths": {}}
    for width in WIDTHS:
        print(f"jets width={width}", flush=True)
        raw = np.load(RUN / f"raw_width_{width}.npz")
        jets = regenerate_pair_jets(width)
        # Pair f jet is odd. G=f' has c0=f1 and c2=3f3.
        pair_c0 = jets[:, 1]
        pair_c2 = 3.0 * jets[:, 3]
        corrected = raw["pair_g"] + (G0 - pair_c0)[:, None] + (G2 - pair_c2)[:, None] * raw["times"][None, :] ** 2
        np.savez_compressed(OUT / f"jets_and_cv_width_{width}.npz", jets=jets, corrected=corrected)

        # Jet reconstruction is checked at the first two positive time points.
        predicted = pair_c0[:, None] + pair_c2[:, None] * raw["times"][None, 1:3] ** 2
        actual = raw["pair_g"][:, 1:3]
        jet_error = actual - predicted
        wout = {
            "pair_c0_mean": float(np.mean(pair_c0)),
            "pair_c2_mean": float(np.mean(pair_c2)),
            "pair_c2_median": float(np.median(pair_c2)),
            "jet_check_mean_abs": np.mean(np.abs(jet_error), axis=0).tolist(),
            "specs": {},
        }
        for kind in ("mom7", "mom5", "mean"):
            if len(corrected) % (7 if kind == "mom7" else 5 if kind == "mom5" else 1):
                continue
            for degree in (2, 3, 4):
                key = f"{kind}_degree{degree}"
                p = proxy(corrected, raw["times"], width, kind, degree)
                entry = {
                    "q0": p["q0"], "R0_numeric_first_step": p["R0_numeric"],
                    "fit_rms": p["fit_rms"], "fit_max": p["fit_max"],
                    "r": p["r"].tolist(), "rp": p["rp"].tolist(),
                    "A_eigenvalues": np.linalg.eigvalsh(p["A"]).tolist(),
                    "B_eigenvalues": np.linalg.eigvalsh(p["B"]).tolist(),
                }
                if kind == "mom7" and degree == 3:
                    entry["bootstrap"] = bootstrap(corrected, raw["times"], width, kind, degree, 2026081500 + width)
                wout["specs"][key] = entry
        results["widths"][str(width)] = wout
        print(width, wout["specs"]["mom7_degree3"]["q0"], flush=True)
    (OUT / "results.json").write_text(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
