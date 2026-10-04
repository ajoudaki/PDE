"""Sample-independent signed rank-one memory; research verification only.

The algorithm stores skinny factors, never its dense matrix. Dense matrices
are formed only in the deterministic independent checks in __main__.
No neural-network training experiment is performed by this file.
"""
from __future__ import annotations

import json
from pathlib import Path
import argparse
import numpy as np


class SpectralMemory:
    """Soft singular-value shrinkage after each signed rank-one insertion."""

    def __init__(self, rows: int, cols: int, rank: int):
        if not (rows > 0 and cols > 0 and 1 <= rank <= min(rows, cols)):
            raise ValueError("positive dimensions and admissible rank required")
        self.rows, self.cols, self.rank = rows, cols, rank
        self.u = np.empty((rows, 0))
        self.v = np.empty((cols, 0))
        self.s = np.empty(0)
        self.atomic_mass = 0.0
        self.shrink_sum = 0.0

    def action(self, x: np.ndarray) -> np.ndarray:
        return self.u @ (self.s * (self.v.T @ x))

    def transpose_action(self, y: np.ndarray) -> np.ndarray:
        return self.v @ (self.s * (self.u.T @ y))

    def insert(self, a: np.ndarray, b: np.ndarray) -> float:
        a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
        if a.shape != (self.rows,) or b.shape != (self.cols,):
            raise ValueError("rank-one factors have incompatible shape")
        if not (np.isfinite(a).all() and np.isfinite(b).all()):
            raise ValueError("finite factors required")
        mass = float(np.linalg.norm(a) * np.linalg.norm(b))
        if mass == 0.0:
            return 0.0
        self.atomic_mass += mass
        left = np.column_stack((self.u * self.s, a))
        right = np.column_stack((self.v, b))
        ql, rl = np.linalg.qr(left, mode="reduced")
        qr, rr = np.linalg.qr(right, mode="reduced")
        cu, sv, cvt = np.linalg.svd(rl @ rr.T, full_matrices=False)
        delta = float(sv[self.rank]) if len(sv) > self.rank else 0.0
        keep = min(self.rank, len(sv))
        self.u = ql @ cu[:, :keep]
        self.v = qr @ cvt.T[:, :keep]
        self.s = np.maximum(sv[:keep] - delta, 0.0)
        self.shrink_sum += delta
        return delta


def dense(memory: SpectralMemory) -> np.ndarray:
    """Independent verification only, deliberately not part of insertion."""
    return (memory.u * memory.s) @ memory.v.T


def verify() -> dict:
    rng = np.random.default_rng(5929)
    worst = {"operator_ratio": 0.0, "frobenius_ratio": 0.0,
             "dense_step_error": 0.0, "potential_excess": 0.0}
    checked = 0
    for rows, cols, rank in ((11, 9, 1), (11, 9, 3), (8, 8, 7), (7, 9, 7)):
        memory = SpectralMemory(rows, cols, rank)
        accumulator = np.zeros((rows, cols))
        for j in range(120):
            # Adaptive inputs explicitly depend on the retained state.
            a = np.sin(rng.normal(size=rows) + memory.action(rng.normal(size=cols)))
            b = np.cos(rng.normal(size=cols) + memory.transpose_action(rng.normal(size=rows)))
            a *= (-1.0 if j % 3 else 1.0) / (j + 2)
            before = dense(memory)
            candidate = before + np.outer(a, b)
            u, s, vt = np.linalg.svd(candidate, full_matrices=False)
            delta = s[rank] if rank < len(s) else 0.0
            expected = (u[:, :rank] * np.maximum(s[:rank] - delta, 0.0)) @ vt[:rank]
            memory.insert(a, b)
            accumulator += np.outer(a, b)
            result = dense(memory)
            err = accumulator - result
            op = float(np.linalg.norm(err, 2))
            fro = float(np.linalg.norm(err, "fro"))
            op_bound = memory.atomic_mass / (rank + 1)
            fro_bound = memory.atomic_mass / np.sqrt(rank + 1)
            tolerance = 2e-11 * max(1.0, memory.atomic_mass)
            assert op <= op_bound + tolerance
            assert fro <= fro_bound + tolerance
            step_error = float(np.linalg.norm(result - expected, "fro"))
            assert step_error <= tolerance
            excess = float(memory.s.sum() + (rank + 1) * memory.shrink_sum - memory.atomic_mass)
            assert excess <= tolerance
            worst["operator_ratio"] = max(worst["operator_ratio"], op / op_bound)
            worst["frobenius_ratio"] = max(worst["frobenius_ratio"], fro / fro_bound)
            worst["dense_step_error"] = max(worst["dense_step_error"], step_error)
            worst["potential_excess"] = max(worst["potential_excess"], excess)
            checked += 1

    # Exact sharp example for the per-insertion sketch bound.
    sharp = SpectralMemory(6, 6, 3)
    for i in range(4):
        sharp.insert(np.eye(6)[i], np.eye(6)[i])
    target = np.diag([1.0] * 4 + [0.0] * 2)
    sharp_error = target - dense(sharp)
    assert np.allclose(np.linalg.norm(sharp_error, 2), sharp.atomic_mass / 4)
    assert np.allclose(np.linalg.norm(sharp_error, "fro"), sharp.atomic_mass / 2)

    # Ordinary truncation repeatedly discards individually small coherent updates.
    hard = np.zeros((2, 2))
    soft = SpectralMemory(2, 2, 1)
    total = np.zeros((2, 2))
    for i in range(201):
        a = np.array([1.0, 0.0]) if i == 0 else np.array([0.0, 0.02])
        b = np.array([1.0, 0.0]) if i == 0 else np.array([0.0, 1.0])
        atom = np.outer(a, b)
        u, s, vt = np.linalg.svd(hard + atom, full_matrices=False)
        hard = s[0] * np.outer(u[:, 0], vt[0])
        soft.insert(a, b)
        total += atom
    hard_error = float(np.linalg.norm(total - hard, 2))
    soft_error = float(np.linalg.norm(total - dense(soft), 2))
    assert hard_error > soft.atomic_mass / 2
    assert soft_error <= soft.atomic_mass / 2 + 1e-12

    return {"status": "passed", "numpy_version": np.__version__,
            "seed": 5929, "adaptive_prefix_checks": checked, **worst,
            "sharp_operator_error": float(np.linalg.norm(sharp_error, 2)),
            "sharp_frobenius_error": float(np.linalg.norm(sharp_error, "fro")),
            "hard_truncation_error": hard_error, "soft_shrink_error": soft_error,
            "hard_soft_atomic_budget": soft.atomic_mass,
            "scope": "deterministic algebra and implementation checks; no training benchmark"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    result = verify()
    (args.out / "verification.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
