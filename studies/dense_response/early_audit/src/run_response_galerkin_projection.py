#!/usr/bin/env python3
"""Predetermined triangular-polynomial projection of response contractions.

This is an approximation-theory diagnostic only.  Coefficients are fitted to
an exact finite-width snapshot, so it is intentionally *not* presented as the
non-oracular autonomous compiler sought in the conjecture.
"""

from __future__ import annotations

import csv
import math
import os
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.legendre import legvander

from src.run_dense_resnet_audit import (
    State,
    forward_and_adjoint,
    initialize,
    make_data,
    train,
)


def response_contraction(state: State, X: np.ndarray, y: np.ndarray) -> np.ndarray:
    cache = forward_and_adjoint(state, X, y)
    L, n, _ = state.W.shape
    delta = 1.0 / L
    r = 0
    qsrc = min(1, len(y) - 1)
    R = np.full((L + 1, L + 1), np.nan)
    for u in range(L + 1):
        if u == L:
            source = cache.Q[L][qsrc]
        else:
            source = cache.D[u][r] * cache.Beta[u][qsrc]
        cur = source.copy()
        R[u, u] = float(cache.H[u][r] @ cur) / n
        for ell in range(u, L):
            cur = cur + delta * (cache.D[ell][r] * (state.W[ell] @ cur))
            R[ell + 1, u] = float(cache.H[ell + 1][r] @ cur) / n
    return R


def triangular_legendre_projection(
    R: np.ndarray, degree: int
) -> Tuple[np.ndarray, float, float]:
    L = R.shape[0] - 1
    s_idx, u_idx = np.where(np.isfinite(R))
    s = s_idx / L
    u = u_idx / L
    vs = legvander(2.0 * s - 1.0, degree)
    vu = legvander(2.0 * u - 1.0, degree)
    pairs = [(i, j) for i in range(degree + 1) for j in range(degree + 1 - i)]
    design = np.stack([vs[:, i] * vu[:, j] for i, j in pairs], axis=1)
    target = R[s_idx, u_idx]
    coef, *_ = np.linalg.lstsq(design, target, rcond=None)
    pred = design @ coef
    abs_err = float(np.max(np.abs(pred - target)))
    rel_fro = float(np.linalg.norm(pred - target) / max(np.linalg.norm(target), 1e-30))
    fit = np.full_like(R, np.nan)
    fit[s_idx, u_idx] = pred
    return fit, abs_err, rel_fro


def write_rows(path: Path, rows: Sequence[Dict[str, object]]) -> None:
    keys = list(rows[0])
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    out = Path(os.environ.get("GALERKIN_OUT", "results/final")).resolve()
    out.mkdir(parents=True, exist_ok=True)
    cases = [
        ("iid_generic", "iid", 0.0),
        ("smooth_generic", "smooth", 0.0),
        ("smooth_nonnormal", "smooth", 2.5),
    ]
    rows: List[Dict[str, object]] = []
    n, L, d, m = 24, 40, 6, 3
    for ci, (tag, mode, nonnormal) in enumerate(cases):
        X, y = make_data(m, d, seed=41 + ci)
        initial = initialize(
            n,
            L,
            d,
            seed=53 + ci,
            depth_mode=mode,
            nonnormal_strength=nonnormal,
        )
        final, _ = train(initial, X, y, T=1.6, dt=0.025, record_every=8)
        R = response_contraction(final, X, y)
        for degree in range(1, 11):
            _, max_abs, rel_fro = triangular_legendre_projection(R, degree)
            rows.append(
                {
                    "tag": tag,
                    "total_degree": degree,
                    "coefficient_count": (degree + 1) * (degree + 2) // 2,
                    "max_abs_error": max_abs,
                    "relative_fro_error": rel_fro,
                }
            )
    write_rows(out / "triangular_galerkin_projection.csv", rows)

    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.2))
    for tag, _, _ in cases:
        rr = [r for r in rows if r["tag"] == tag]
        axes[0].semilogy(
            [r["coefficient_count"] for r in rr],
            [r["max_abs_error"] for r in rr],
            marker="o",
            label=tag,
        )
        axes[1].semilogy(
            [r["coefficient_count"] for r in rr],
            [r["relative_fro_error"] for r in rr],
            marker="o",
            label=tag,
        )
    axes[0].set_ylabel("max absolute error")
    axes[1].set_ylabel("relative Frobenius error")
    for ax in axes:
        ax.set_xlabel("triangular Legendre coefficients")
        ax.grid(True, which="both", alpha=0.25)
    axes[0].set_title("Snapshot response projection")
    axes[1].set_title("Snapshot response projection")
    axes[1].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out / "triangular_galerkin_projection.png", dpi=180)
    plt.close(fig)
    print(out / "triangular_galerkin_projection.csv")


if __name__ == "__main__":
    main()
