#!/usr/bin/env python3
"""Prespecified direct Loewner test for the quadratic feature-ascent model."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import platform
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
import scipy
from scipy import stats


HERE = Path(__file__).resolve().parent
X_NODES = np.array([0.0004, 0.0016, 0.0036, 0.0064], dtype=np.float64)
Y_NODES = np.sqrt(X_NODES)
WIDTHS = (64, 128, 256)
PAIR_COUNTS = {64: 96, 128: 64, 256: 32}
MAX_WIDTH = 256
SEED_BASE = 2026081201
MAIN_STEP = 0.001
HALF_STEP = 0.0005
VALIDATION_PAIRS = 8
FWER_ALPHA = 0.01
N_TESTS = 6
BOOTSTRAPS = 500


@dataclass
class State:
    a: np.ndarray
    W: np.ndarray
    u: np.ndarray


def rhs(state: State) -> State:
    """Feature-ascent vector field, batched on axis zero."""
    n = state.a.shape[1]
    inv_sqrt_n = 1.0 / math.sqrt(n)
    u2 = state.u * state.u
    z = inv_sqrt_n * np.einsum("bij,bj->bi", state.W, u2, optimize=True)
    az = state.a * z
    v = np.einsum("bij,bi->bj", state.W, az, optimize=True)
    da = z * z
    dW = (2.0 * inv_sqrt_n) * az[:, :, None] * u2[:, None, :]
    du = (4.0 * inv_sqrt_n) * state.u * v
    return State(da, dW, du)


def add_scaled(state: State, tangent: State, scale: float) -> State:
    return State(
        state.a + scale * tangent.a,
        state.W + scale * tangent.W,
        state.u + scale * tangent.u,
    )


def rk4_step(state: State, h: float) -> State:
    k1 = rhs(state)
    k2 = rhs(add_scaled(state, k1, 0.5 * h))
    k3 = rhs(add_scaled(state, k2, 0.5 * h))
    k4 = rhs(add_scaled(state, k3, h))
    return State(
        state.a + (h / 6.0) * (k1.a + 2.0 * k2.a + 2.0 * k3.a + k4.a),
        state.W + (h / 6.0) * (k1.W + 2.0 * k2.W + 2.0 * k3.W + k4.W),
        state.u + (h / 6.0) * (k1.u + 2.0 * k2.u + 2.0 * k3.u + k4.u),
    )


def observable_and_derivative(state: State) -> tuple[np.ndarray, np.ndarray]:
    """Return K_n and its exact derivative along the feature flow."""
    n = state.a.shape[1]
    inv_sqrt_n = 1.0 / math.sqrt(n)
    inv_n = 1.0 / n
    u2 = state.u * state.u
    z = inv_sqrt_n * np.einsum("bij,bj->bi", state.W, u2, optimize=True)
    az = state.a * z
    v = np.einsum("bij,bi->bj", state.W, az, optimize=True)

    sum_u4 = np.sum(u2 * u2, axis=1)
    sum_az2 = np.sum(az * az, axis=1)
    k1 = inv_n * np.sum(z**4, axis=1)
    k2 = 4.0 * inv_n**2 * sum_az2 * sum_u4
    k3 = 16.0 * inv_n**2 * np.sum(u2 * v * v, axis=1)
    kval = k1 + k2 + k3

    ds = (8.0 * inv_sqrt_n) * u2 * v
    dz = (
        2.0 * inv_n * az * sum_u4[:, None]
        + 8.0 * inv_n * np.einsum("bij,bj->bi", state.W, u2 * v, optimize=True)
    )
    dp = z**3 + state.a * dz
    dv = (
        2.0 * inv_sqrt_n * u2 * sum_az2[:, None]
        + np.einsum("bij,bi->bj", state.W, dp, optimize=True)
    )

    dk1 = 4.0 * inv_n * np.sum(z**3 * dz, axis=1)
    d_sum_az2 = 2.0 * np.sum(az * dp, axis=1)
    d_sum_u4 = 2.0 * np.sum(u2 * ds, axis=1)
    dk2 = 4.0 * inv_n**2 * (
        d_sum_az2 * sum_u4 + sum_az2 * d_sum_u4
    )
    dk3 = 16.0 * inv_n**2 * np.sum(
        ds * v * v + 2.0 * u2 * v * dv, axis=1
    )
    return kval, dk1 + dk2 + dk3


def generate_state(width: int, pair_count: int) -> State:
    """Generate nested/common Gaussian draws and antithetic a pairs."""
    a0 = np.empty((pair_count, width), dtype=np.float64)
    u0 = np.empty((pair_count, width), dtype=np.float64)
    W0 = np.empty((pair_count, width, width), dtype=np.float64)
    for r in range(pair_count):
        rng = np.random.default_rng(np.random.SeedSequence([SEED_BASE, r]))
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
    return State(a, W, u)


def pair_average(values: np.ndarray) -> np.ndarray:
    shape = values.shape
    return values.reshape(shape[0] // 2, 2, *shape[1:]).mean(axis=1)


def simulate(width: int, pair_count: int, step: float) -> dict[str, np.ndarray]:
    state = generate_state(width, pair_count)
    k0_raw, dk0_raw = observable_and_derivative(state)
    k0 = pair_average(k0_raw)
    dk0 = pair_average(dk0_raw)
    kvals = np.empty((pair_count, len(Y_NODES)), dtype=np.float64)
    dkvals = np.empty_like(kvals)

    target_steps = np.rint(Y_NODES / step).astype(int)
    if not np.allclose(target_steps * step, Y_NODES, rtol=0.0, atol=1e-14):
        raise ValueError("Output nodes are not exact step endpoints")
    target_map = {int(s): j for j, s in enumerate(target_steps)}
    for s in range(1, int(target_steps[-1]) + 1):
        state = rk4_step(state, step)
        if s in target_map:
            j = target_map[s]
            kr, dkr = observable_and_derivative(state)
            kvals[:, j] = pair_average(kr)
            dkvals[:, j] = pair_average(dkr)

    delta = kvals - k0[:, None]
    rvals = delta / X_NODES[None, :]
    rpvals = (
        dkvals / (2.0 * Y_NODES[None, :] ** 3)
        - delta / Y_NODES[None, :] ** 4
    )
    A, B = loewner_matrices(rvals, rpvals)
    return {
        "k0": k0,
        "dk0": dk0,
        "k": kvals,
        "dk": dkvals,
        "r": rvals,
        "rp": rpvals,
        "A": A,
        "B": B,
    }


def loewner_matrices(
    rvals: np.ndarray, rpvals: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    count, nodes = rvals.shape
    A = np.empty((count, nodes, nodes), dtype=np.float64)
    B = np.empty_like(A)
    for i in range(nodes):
        for j in range(nodes):
            if i == j:
                A[:, i, i] = -rpvals[:, i]
                B[:, i, i] = rvals[:, i] + X_NODES[i] * rpvals[:, i]
            else:
                dx = X_NODES[i] - X_NODES[j]
                A[:, i, j] = -(rvals[:, i] - rvals[:, j]) / dx
                B[:, i, j] = (
                    X_NODES[i] * rvals[:, i]
                    - X_NODES[j] * rvals[:, j]
                ) / dx
    return A, B


def exact_atomic_control(nodes: Iterable[float], weights: Iterable[float]) -> dict:
    lambdas = np.asarray(tuple(nodes), dtype=np.float64)
    w = np.asarray(tuple(weights), dtype=np.float64)
    denom = 1.0 + X_NODES[:, None] * lambdas[None, :]
    r = np.sum(w[None, :] / denom, axis=1)
    rp = -np.sum(w[None, :] * lambdas[None, :] / denom**2, axis=1)
    A, B = loewner_matrices(r[None, :], rp[None, :])
    return {
        "nodes": lambdas.tolist(),
        "weights": w.tolist(),
        "r": r.tolist(),
        "rp": rp.tolist(),
        "A_eigenvalues": np.linalg.eigvalsh(A[0]).tolist(),
        "B_eigenvalues": np.linalg.eigvalsh(B[0]).tolist(),
        "A": A[0].tolist(),
        "B": B[0].tolist(),
    }


def quadratic_scores(mats: np.ndarray, vector: np.ndarray) -> np.ndarray:
    return np.einsum("i,bij,j->b", vector, mats, vector, optimize=True)


def matrix_summary(mats: np.ndarray, matrix_name: str, width: int) -> dict:
    pair_count = mats.shape[0]
    split = pair_count // 2
    discovery = mats[:split]
    confirmation = mats[split:]
    disc_mean = discovery.mean(axis=0)
    full_mean = mats.mean(axis=0)
    eval_disc, evec_disc = np.linalg.eigh(disc_mean)
    vector = evec_disc[:, 0]
    scores = quadratic_scores(confirmation, vector)
    score_mean = float(scores.mean())
    score_se = float(stats.sem(scores))
    alpha_each = FWER_ALPHA / N_TESTS
    tcrit = float(stats.t.ppf(1.0 - alpha_each, df=len(scores) - 1))
    upper = score_mean + tcrit * score_se
    lower = score_mean - tcrit * score_se

    eval_full, evec_full = np.linalg.eigh(full_mean)
    trace = float(np.trace(full_mean))
    spectral_norm = float(np.max(np.abs(eval_full)))
    gap = float(eval_full[1] - eval_full[0])

    rng = np.random.default_rng(
        np.random.SeedSequence([SEED_BASE, width, 0 if matrix_name == "A" else 1])
    )
    angles = np.empty(BOOTSTRAPS, dtype=np.float64)
    reference = evec_disc[:, 0]
    for b in range(BOOTSTRAPS):
        idx = rng.integers(0, split, size=split)
        _, vb = np.linalg.eigh(discovery[idx].mean(axis=0))
        cosine = min(1.0, abs(float(np.dot(reference, vb[:, 0]))))
        angles[b] = math.degrees(math.acos(cosine))

    return {
        "width": width,
        "matrix": matrix_name,
        "pair_count": pair_count,
        "discovery_count": split,
        "confirmation_count": len(scores),
        "full_mean": full_mean.tolist(),
        "full_eigenvalues": eval_full.tolist(),
        "discovery_eigenvalues": eval_disc.tolist(),
        "discovery_vector": vector.tolist(),
        "confirmation_scores": scores.tolist(),
        "confirmation_mean": score_mean,
        "confirmation_se": score_se,
        "one_sided_alpha_each": alpha_each,
        "t_critical": tcrit,
        "confidence_lower": lower,
        "confidence_upper": upper,
        "negative_confirmed": bool(upper < 0.0),
        "trace": trace,
        "spectral_norm": spectral_norm,
        "min_over_trace": float(eval_full[0] / trace) if trace != 0 else math.nan,
        "min_over_spectral_norm": (
            float(eval_full[0] / spectral_norm) if spectral_norm != 0 else math.nan
        ),
        "lowest_eigengap": gap,
        "bootstrap_angle_degrees_median": float(np.median(angles)),
        "bootstrap_angle_degrees_q95": float(np.quantile(angles, 0.95)),
    }


def unique_matrix_entries(mats: np.ndarray) -> np.ndarray:
    idx = np.triu_indices(mats.shape[1])
    return mats[:, idx[0], idx[1]]


def validation_summary(
    main: dict[str, np.ndarray], half: dict[str, np.ndarray],
    summaries: dict[str, dict],
) -> dict:
    result = {}
    for name in ("A", "B"):
        delta = half[name].mean(axis=0) - main[name].mean(axis=0)
        main_norm = float(np.linalg.norm(main[name].mean(axis=0), ord=2))
        vector = np.asarray(summaries[name]["discovery_vector"])
        projected_delta = float(vector @ delta @ vector)
        confirm_se = summaries[name]["confirmation_se"]
        result[name] = {
            "max_abs_entry_difference": float(np.max(np.abs(delta))),
            "spectral_difference": float(np.linalg.norm(delta, ord=2)),
            "relative_spectral_difference": (
                float(np.linalg.norm(delta, ord=2) / main_norm)
                if main_norm != 0 else math.nan
            ),
            "projected_difference": projected_delta,
            "abs_projected_difference_over_confirmation_se": (
                abs(projected_delta) / confirm_se if confirm_se > 0 else math.nan
            ),
        }
    result["max_abs_r_difference"] = float(
        np.max(np.abs(half["r"].mean(axis=0) - main["r"].mean(axis=0)))
    )
    result["max_abs_rp_difference"] = float(
        np.max(np.abs(half["rp"].mean(axis=0) - main["rp"].mean(axis=0)))
    )
    return result


def write_raw_csv(path: Path, all_results: dict[int, dict[str, np.ndarray]]) -> None:
    fields = ["width", "pair"]
    fields += [f"k_x{i}" for i in range(len(X_NODES))]
    fields += [f"dk_x{i}" for i in range(len(X_NODES))]
    fields += [f"r_x{i}" for i in range(len(X_NODES))]
    fields += [f"rp_x{i}" for i in range(len(X_NODES))]
    for name in ("A", "B"):
        fields += [f"{name}_{i}{j}" for i in range(4) for j in range(i, 4)]
    fields += ["k0", "dk0", "k0_minus_111"]
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for width, data in all_results.items():
            Aflat = unique_matrix_entries(data["A"])
            Bflat = unique_matrix_entries(data["B"])
            for r in range(len(data["k0"])):
                row: dict[str, float | int] = {"width": width, "pair": r}
                for i in range(4):
                    row[f"k_x{i}"] = data["k"][r, i]
                    row[f"dk_x{i}"] = data["dk"][r, i]
                    row[f"r_x{i}"] = data["r"][r, i]
                    row[f"rp_x{i}"] = data["rp"][r, i]
                for name, flat in (("A", Aflat), ("B", Bflat)):
                    k = 0
                    for i in range(4):
                        for j in range(i, 4):
                            row[f"{name}_{i}{j}"] = flat[r, k]
                            k += 1
                row["k0"] = data["k0"][r]
                row["dk0"] = data["dk0"][r]
                row["k0_minus_111"] = data["k0"][r] - 111.0
                writer.writerow(row)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=HERE / "runs/run_output")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    log_path = args.output / "run.log"
    log_handle = log_path.open("w")

    def log(message: str) -> None:
        print(message, flush=True)
        print(message, file=log_handle, flush=True)

    log("command: " + " ".join(sys.argv))
    log(f"python={sys.version.split()[0]} numpy={np.__version__} scipy={scipy.__version__}")
    log(f"platform={platform.platform()}")
    log(f"x_nodes={X_NODES.tolist()} y_nodes={Y_NODES.tolist()}")
    log(f"widths={WIDTHS} pair_counts={PAIR_COUNTS}")

    all_results: dict[int, dict[str, np.ndarray]] = {}
    all_summary: dict[str, object] = {
        "design": {
            "x_nodes": X_NODES.tolist(),
            "y_nodes": Y_NODES.tolist(),
            "widths": list(WIDTHS),
            "pair_counts": PAIR_COUNTS,
            "seed_base": SEED_BASE,
            "main_step": MAIN_STEP,
            "half_step": HALF_STEP,
            "validation_pairs": VALIDATION_PAIRS,
            "fwer_alpha": FWER_ALPHA,
            "number_tests": N_TESTS,
        },
        "widths": {},
        "controls": {
            "two_atom": exact_atomic_control((10.0, 100.0), (0.6, 0.4)),
            "three_atom": exact_atomic_control(
                (5.0, 40.0, 160.0), (0.5, 0.3, 0.2)
            ),
        },
    }

    for width in WIDTHS:
        pair_count = PAIR_COUNTS[width]
        log(f"START width={width} pairs={pair_count} step={MAIN_STEP}")
        data = simulate(width, pair_count, MAIN_STEP)
        if not all(np.all(np.isfinite(value)) for value in data.values()):
            raise FloatingPointError(f"Nonfinite trajectory/output at width {width}")
        all_results[width] = data
        summaries = {
            name: matrix_summary(data[name], name, width) for name in ("A", "B")
        }
        log(
            f"width={width} k0_mean={data['k0'].mean():.12g} "
            f"k0_se={stats.sem(data['k0']):.6g} "
            f"mean_r={data['r'].mean(axis=0).tolist()}"
        )
        for name, summary in summaries.items():
            log(
                f"width={width} {name} eig={summary['full_eigenvalues']} "
                f"confirm_mean={summary['confirmation_mean']:.12g} "
                f"confirm_se={summary['confirmation_se']:.6g} "
                f"upper={summary['confidence_upper']:.12g} "
                f"negative_confirmed={summary['negative_confirmed']}"
            )

        log(
            f"START validation width={width} pairs={VALIDATION_PAIRS} "
            f"step={HALF_STEP}"
        )
        main_subset = {key: value[:VALIDATION_PAIRS] for key, value in data.items()}
        half = simulate(width, VALIDATION_PAIRS, HALF_STEP)
        validation = validation_summary(main_subset, half, summaries)
        log(f"width={width} validation={json.dumps(validation, sort_keys=True)}")

        np.savez_compressed(args.output / f"raw_width_{width}.npz", **data)
        np.savez_compressed(args.output / f"half_step_width_{width}.npz", **half)
        all_summary["widths"][str(width)] = {
            "k0_mean": float(data["k0"].mean()),
            "k0_se": float(stats.sem(data["k0"])),
            "k0_minus_111_mean": float(data["k0"].mean() - 111.0),
            "dk0_antithetic_max_abs": float(np.max(np.abs(data["dk0"]))),
            "mean_k": data["k"].mean(axis=0).tolist(),
            "se_k": stats.sem(data["k"], axis=0).tolist(),
            "mean_r": data["r"].mean(axis=0).tolist(),
            "se_r": stats.sem(data["r"], axis=0).tolist(),
            "mean_rp": data["rp"].mean(axis=0).tolist(),
            "se_rp": stats.sem(data["rp"], axis=0).tolist(),
            "A": summaries["A"],
            "B": summaries["B"],
            "validation": validation,
        }

    csv_path = args.output / "raw_replications.csv"
    write_raw_csv(csv_path, all_results)
    summary_path = args.output / "summary.json"
    with summary_path.open("w") as handle:
        json.dump(all_summary, handle, indent=2, sort_keys=True, allow_nan=True)
        handle.write("\n")

    log("controls=" + json.dumps(all_summary["controls"], sort_keys=True))
    log_handle.close()

    artifact_names = [
        "run.log", "raw_replications.csv", "summary.json",
        *[f"raw_width_{n}.npz" for n in WIDTHS],
        *[f"half_step_width_{n}.npz" for n in WIDTHS],
    ]
    manifest = {
        name: {"sha256": sha256(args.output / name), "bytes": (args.output / name).stat().st_size}
        for name in artifact_names
    }
    manifest["../simulate_loewner.py"] = {
        "sha256": sha256(Path(__file__)), "bytes": Path(__file__).stat().st_size
    }
    with (args.output / "manifest.json").open("w") as handle:
        json.dump(manifest, handle, indent=2, sort_keys=True)
        handle.write("\n")
    print("COMPLETE manifest=" + str(args.output / "manifest.json"), flush=True)


if __name__ == "__main__":
    main()
