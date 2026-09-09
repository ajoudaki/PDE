#!/usr/bin/env python3
"""Independent corrected common-clock Loewner experiment."""

from __future__ import annotations

import hashlib
import json
import math
import platform
import sys
from pathlib import Path

import numpy as np
from numpy.polynomial import Chebyshev

import corrected_clock_core as core


HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "runs/corrected_clock_run_20260814"
SCIENCE_SEED_BASE = 2026081401
WIDTHS = (64, 128, 256)
PAIR_COUNTS = {64: 140, 128: 70, 256: 70}
BATCH_PAIRS = 35
S_MAX = 0.003
STEP = 0.00005
HALF_STEP = 0.000025
Y_NODES = np.array([0.04, 0.08, 0.12, 0.16], dtype=np.float64)
X_NODES = Y_NODES * Y_NODES
FIT_Y_MIN = 0.02
FIT_Y_MAX = 0.18
PRIMARY_BLOCKS = 7
PRIMARY_CUTOFF_POWER = 0.5
PRIMARY_DEGREE = 3
BOOTSTRAPS = 5000
ANGLE_BOOTSTRAPS = 500
FWER_ALPHA = 0.01
NUMBER_TESTS = 6
STATE_CEILING = 1.0e12

SPECS = (
    ("b7_sqrt", 7, 0.5),
    ("b5_sqrt", 5, 0.5),
    ("b7_linear", 7, 1.0),
    ("b5_linear", 5, 1.0),
)


def log_factory(path: Path):
    handle = path.open("w")

    def log(message: str) -> None:
        print(message, flush=True)
        print(message, file=handle, flush=True)

    return log, handle


def concat_batches(batches: list[dict[str, np.ndarray]]) -> dict[str, np.ndarray]:
    return {
        "times": batches[0]["times"],
        "pair_g": np.concatenate([b["pair_g"] for b in batches], axis=0),
        "pair_f_direct": np.concatenate(
            [b["pair_f_direct"] for b in batches], axis=0
        ),
        "escape_time": np.concatenate([b["escape_time"] for b in batches]),
        "initial_pair_g": np.concatenate([b["initial_pair_g"] for b in batches]),
        "initial_raw_f": np.concatenate([b["initial_raw_f"] for b in batches]),
    }


def loewner(r: np.ndarray, rp: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    size = len(X_NODES)
    A = np.empty((size, size), dtype=np.float64)
    B = np.empty_like(A)
    for i in range(size):
        for j in range(size):
            if i == j:
                A[i, i] = -rp[i]
                B[i, i] = r[i] + X_NODES[i] * rp[i]
            else:
                dx = X_NODES[i] - X_NODES[j]
                A[i, j] = -(r[i] - r[j]) / dx
                B[i, j] = (
                    X_NODES[i] * r[i] - X_NODES[j] * r[j]
                ) / dx
    return A, B


def cutoff(width: int, power: float) -> float:
    return 111.0 * width**power


def build_proxy(
    pair_g: np.ndarray,
    pair_f_direct: np.ndarray | None,
    width: int,
    blocks: int,
    cutoff_power: float,
    degree: int,
    step: float,
) -> dict[str, object]:
    cap = cutoff(width, cutoff_power)
    G = core.median_of_means(pair_g, blocks, cap)
    F = core.cumulative_simpson_uniform(G, step)
    if not np.all(np.isfinite(G)) or not np.all(np.diff(F) > 0.0):
        raise ValueError("Robust G is nonfinite or integrated F is not increasing")
    if F[-1] < FIT_Y_MAX or F[-1] < Y_NODES[-1]:
        raise ValueError("Robust clock does not bracket the frozen output nodes")

    X_curve = F * F
    delta_G = G - G[0]
    mask = (F >= FIT_Y_MIN) & (F <= FIT_Y_MAX)
    raw_R = delta_G[mask] / X_curve[mask]
    fit = Chebyshev.fit(
        X_curve[mask],
        raw_R,
        degree,
        domain=(FIT_Y_MIN**2, FIT_Y_MAX**2),
    )
    r_nodes = fit(X_NODES)
    rp_nodes = fit.deriv()(X_NODES)
    A, B = loewner(r_nodes, rp_nodes)
    residual = fit(X_curve[mask]) - raw_R

    direct_info: dict[str, float] | None = None
    direct_F = None
    if pair_f_direct is not None:
        direct_F = core.median_of_means(
            pair_f_direct, blocks, cap * S_MAX
        )
        comparison = direct_F - F
        direct_info = {
            "max_abs_difference": float(np.max(np.abs(comparison))),
            "end_difference": float(comparison[-1]),
            "max_abs_difference_over_end_F": float(
                np.max(np.abs(comparison)) / F[-1]
            ),
        }

    finite_g = pair_g[np.isfinite(pair_g)]
    return {
        "G": G,
        "F": F,
        "direct_F": direct_F,
        "G0": float(G[0]),
        "F_end": float(F[-1]),
        "cutoff": cap,
        "pairs_ever_clipped": int(np.sum(np.any(pair_g > cap, axis=1))),
        "clipped_entries": int(np.sum(pair_g > cap)),
        "raw_finite_g_max": float(np.max(finite_g)) if finite_g.size else math.inf,
        "fit_degree": degree,
        "fit_point_count": int(mask.sum()),
        "fit_rms": float(np.sqrt(np.mean(residual * residual))),
        "fit_max_abs": float(np.max(np.abs(residual))),
        "r_nodes": r_nodes,
        "rp_nodes": rp_nodes,
        "A": A,
        "B": B,
        "direct_F_diagnostic": direct_info,
    }


def proxy_json(proxy: dict[str, object], include_matrices: bool = True) -> dict:
    keys = (
        "G0", "F_end", "cutoff", "pairs_ever_clipped", "clipped_entries",
        "raw_finite_g_max", "fit_degree", "fit_point_count", "fit_rms",
        "fit_max_abs", "direct_F_diagnostic",
    )
    result = {key: proxy[key] for key in keys}
    result["r_nodes"] = np.asarray(proxy["r_nodes"]).tolist()
    result["rp_nodes"] = np.asarray(proxy["rp_nodes"]).tolist()
    if include_matrices:
        result["A"] = np.asarray(proxy["A"]).tolist()
        result["B"] = np.asarray(proxy["B"]).tolist()
        result["A_eigenvalues"] = np.linalg.eigvalsh(proxy["A"]).tolist()
        result["B_eigenvalues"] = np.linalg.eigvalsh(proxy["B"]).tolist()
    return result


def score(matrix: np.ndarray, vector: np.ndarray) -> float:
    return float(vector @ matrix @ vector)


def matrix_condition(matrix: np.ndarray) -> dict[str, object]:
    eigenvalues = np.linalg.eigvalsh(matrix)
    trace = float(np.trace(matrix))
    norm = float(np.max(np.abs(eigenvalues)))
    return {
        "eigenvalues": eigenvalues.tolist(),
        "trace": trace,
        "spectral_norm": norm,
        "min_over_trace": float(eigenvalues[0] / trace) if trace else math.nan,
        "min_over_spectral_norm": float(eigenvalues[0] / norm) if norm else math.nan,
        "lowest_eigengap": float(eigenvalues[1] - eigenvalues[0]),
    }


def bootstrap_confirmation(
    pair_g: np.ndarray,
    width: int,
    vectors: dict[str, np.ndarray],
    seed: int,
) -> tuple[dict[str, dict[str, float | int | bool]], dict[str, np.ndarray]]:
    rng = np.random.default_rng(seed)
    count = pair_g.shape[0]
    samples = {"A": np.empty(BOOTSTRAPS), "B": np.empty(BOOTSTRAPS)}
    failures = 0
    dummy_f = None
    for b in range(BOOTSTRAPS):
        idx = rng.integers(0, count, size=count)
        try:
            proxy = build_proxy(
                pair_g[idx], dummy_f, width, PRIMARY_BLOCKS,
                PRIMARY_CUTOFF_POWER, PRIMARY_DEGREE, STEP,
            )
            for name in ("A", "B"):
                samples[name][b] = score(proxy[name], vectors[name])
        except (ValueError, np.linalg.LinAlgError):
            failures += 1
            samples["A"][b] = np.nan
            samples["B"][b] = np.nan
    alpha_each = FWER_ALPHA / NUMBER_TESTS
    summaries = {}
    for name in ("A", "B"):
        finite = samples[name][np.isfinite(samples[name])]
        summaries[name] = {
            "bootstrap_count": BOOTSTRAPS,
            "finite_bootstrap_count": int(len(finite)),
            "shared_proxy_failures": failures,
            "mean": float(np.mean(finite)),
            "standard_deviation": float(np.std(finite, ddof=1)),
            "lower_percentile": float(
                np.quantile(finite, alpha_each, method="lower")
            ),
            "upper_percentile": float(
                np.quantile(finite, 1.0 - alpha_each, method="higher")
            ),
            "one_sided_alpha_each": alpha_each,
        }
    return summaries, samples


def discovery_angle_bootstrap(
    pair_g: np.ndarray,
    width: int,
    references: dict[str, np.ndarray],
    seed: int,
) -> dict[str, dict[str, float | int]]:
    rng = np.random.default_rng(seed)
    count = pair_g.shape[0]
    angles = {"A": [], "B": []}
    failures = 0
    for _ in range(ANGLE_BOOTSTRAPS):
        idx = rng.integers(0, count, size=count)
        try:
            proxy = build_proxy(
                pair_g[idx], None, width, PRIMARY_BLOCKS,
                PRIMARY_CUTOFF_POWER, PRIMARY_DEGREE, STEP,
            )
            for name in ("A", "B"):
                _, eigenvectors = np.linalg.eigh(proxy[name])
                cosine = min(
                    1.0, abs(float(np.dot(references[name], eigenvectors[:, 0])))
                )
                angles[name].append(math.degrees(math.acos(cosine)))
        except (ValueError, np.linalg.LinAlgError):
            failures += 1
    result = {}
    for name in ("A", "B"):
        values = np.asarray(angles[name])
        result[name] = {
            "count": int(len(values)),
            "shared_failures": failures,
            "median_degrees": float(np.median(values)),
            "q95_degrees": float(np.quantile(values, 0.95)),
        }
    return result


def exact_control(nodes: tuple[float, ...], weights: tuple[float, ...]) -> dict:
    lambdas = np.asarray(nodes)
    w = np.asarray(weights)
    denom = 1.0 + X_NODES[:, None] * lambdas[None, :]
    r = np.sum(w[None, :] / denom, axis=1)
    rp = -np.sum(w[None, :] * lambdas[None, :] / denom**2, axis=1)
    A, B = loewner(r, rp)
    return {
        "nodes": list(nodes),
        "weights": list(weights),
        "r_nodes": r.tolist(),
        "rp_nodes": rp.tolist(),
        "A": A.tolist(),
        "B": B.tolist(),
        "A_eigenvalues": np.linalg.eigvalsh(A).tolist(),
        "B_eigenvalues": np.linalg.eigvalsh(B).tolist(),
    }


def hash_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    OUTPUT.mkdir(exist_ok=True)
    log, log_handle = log_factory(OUTPUT / "run.log")
    log("command: " + " ".join(sys.argv))
    log(f"python={sys.version.split()[0]} numpy={np.__version__}")
    log(f"platform={platform.platform()}")
    log(f"output_y={Y_NODES.tolist()} x={X_NODES.tolist()}")

    summary: dict[str, object] = {
        "status": "corrected_conditional_typical_proxy_experiment",
        "estimand_warning": (
            "Median-of-means/clipped n-dependent typical proxy; not an ordinary "
            "finite-width expectation"
        ),
        "design": {
            "science_seed_base": SCIENCE_SEED_BASE,
            "batch_seed_rule": "SCIENCE_SEED_BASE + zero_based_batch_index",
            "widths": list(WIDTHS),
            "pair_counts": PAIR_COUNTS,
            "batch_pairs": BATCH_PAIRS,
            "s_max": S_MAX,
            "step": STEP,
            "half_step": HALF_STEP,
            "y_nodes": Y_NODES.tolist(),
            "x_nodes": X_NODES.tolist(),
            "fit_y_window": [FIT_Y_MIN, FIT_Y_MAX],
            "primary_blocks": PRIMARY_BLOCKS,
            "primary_cutoff_power": PRIMARY_CUTOFF_POWER,
            "primary_degree": PRIMARY_DEGREE,
            "specs": [list(spec) for spec in SPECS],
            "bootstraps": BOOTSTRAPS,
            "angle_bootstraps": ANGLE_BOOTSTRAPS,
            "fwer_alpha": FWER_ALPHA,
        },
        "controls": {
            "two_atom": exact_control((10.0, 100.0), (0.6, 0.4)),
            "three_atom": exact_control(
                (5.0, 40.0, 160.0), (0.5, 0.3, 0.2)
            ),
        },
        "widths": {},
    }

    for width in WIDTHS:
        batch_count = PAIR_COUNTS[width] // BATCH_PAIRS
        batches = []
        for batch in range(batch_count):
            seed = SCIENCE_SEED_BASE + batch
            log(
                f"START width={width} batch={batch + 1}/{batch_count} "
                f"pairs={BATCH_PAIRS} seed_base={seed} step={STEP}"
            )
            data = core.simulate_pair_curves(
                width, BATCH_PAIRS, seed, S_MAX, STEP, STATE_CEILING
            )
            batches.append(data)
        data = concat_batches(batches)
        split = PAIR_COUNTS[width] // 2
        discovery_g = data["pair_g"][:split]
        confirmation_g = data["pair_g"][split:]
        discovery_f = data["pair_f_direct"][:split]
        confirmation_f = data["pair_f_direct"][split:]

        full_primary = build_proxy(
            data["pair_g"], data["pair_f_direct"], width,
            PRIMARY_BLOCKS, PRIMARY_CUTOFF_POWER, PRIMARY_DEGREE, STEP,
        )
        discovery = build_proxy(
            discovery_g, discovery_f, width,
            PRIMARY_BLOCKS, PRIMARY_CUTOFF_POWER, PRIMARY_DEGREE, STEP,
        )
        confirmation = build_proxy(
            confirmation_g, confirmation_f, width,
            PRIMARY_BLOCKS, PRIMARY_CUTOFF_POWER, PRIMARY_DEGREE, STEP,
        )
        vectors = {}
        for name in ("A", "B"):
            _, eigenvectors = np.linalg.eigh(discovery[name])
            vectors[name] = eigenvectors[:, 0]

        bootstrap_summary, bootstrap_samples = bootstrap_confirmation(
            confirmation_g, width, vectors, SCIENCE_SEED_BASE + 10000 + width
        )
        angles = discovery_angle_bootstrap(
            discovery_g, width, vectors, SCIENCE_SEED_BASE + 20000 + width
        )

        sensitivity: dict[str, object] = {}
        sensitivity_scores = {"A": [], "B": []}
        for spec_name, blocks, power in SPECS:
            degrees = (2, 3, 4) if spec_name == "b7_sqrt" else (3,)
            for degree in degrees:
                label = f"{spec_name}_degree{degree}"
                proxy = build_proxy(
                    confirmation_g, confirmation_f, width,
                    blocks, power, degree, STEP,
                )
                item = proxy_json(proxy)
                item["A_fixed_discovery_score"] = score(proxy["A"], vectors["A"])
                item["B_fixed_discovery_score"] = score(proxy["B"], vectors["B"])
                sensitivity[label] = item
                sensitivity_scores["A"].append(item["A_fixed_discovery_score"])
                sensitivity_scores["B"].append(item["B_fixed_discovery_score"])

        log(f"START half-step validity width={width} pairs={BATCH_PAIRS}")
        half_data = core.simulate_pair_curves(
            width, BATCH_PAIRS, SCIENCE_SEED_BASE,
            S_MAX, HALF_STEP, STATE_CEILING,
        )
        main_first = batches[0]
        main_first_proxy = build_proxy(
            main_first["pair_g"], main_first["pair_f_direct"], width,
            PRIMARY_BLOCKS, PRIMARY_CUTOFF_POWER, PRIMARY_DEGREE, STEP,
        )
        half_proxy = build_proxy(
            half_data["pair_g"], half_data["pair_f_direct"], width,
            PRIMARY_BLOCKS, PRIMARY_CUTOFF_POWER, PRIMARY_DEGREE, HALF_STEP,
        )
        numerical = {}
        for name in ("A", "B"):
            difference = half_proxy[name] - main_first_proxy[name]
            projected = score(difference, vectors[name])
            bootstrap_sd = bootstrap_summary[name]["standard_deviation"]
            numerical[name] = {
                "spectral_matrix_difference": float(
                    np.linalg.norm(difference, ord=2)
                ),
                "max_abs_entry_difference": float(np.max(np.abs(difference))),
                "fixed_direction_difference": projected,
                "abs_fixed_direction_difference_over_bootstrap_sd": (
                    abs(projected) / bootstrap_sd if bootstrap_sd else math.nan
                ),
            }
        numerical["max_abs_r_node_difference"] = float(
            np.max(np.abs(half_proxy["r_nodes"] - main_first_proxy["r_nodes"]))
        )
        numerical["main_step_F_end"] = main_first_proxy["F_end"]
        numerical["half_step_F_end"] = half_proxy["F_end"]

        inference = {}
        for name in ("A", "B"):
            point = score(confirmation[name], vectors[name])
            upper = bootstrap_summary[name]["upper_percentile"]
            signs_survive = bool(np.all(np.asarray(sensitivity_scores[name]) < 0.0))
            inference[name] = {
                "discovery_vector": vectors[name].tolist(),
                "confirmation_fixed_direction_score": point,
                "bootstrap": bootstrap_summary[name],
                "all_sensitivity_point_scores_negative": signs_survive,
                "empirical_negative_confirmed": bool(upper < 0.0 and signs_survive),
                "full_matrix_condition": matrix_condition(full_primary[name]),
                "discovery_matrix_condition": matrix_condition(discovery[name]),
                "confirmation_matrix_condition": matrix_condition(confirmation[name]),
                "discovery_eigenvector_bootstrap": angles[name],
            }

        escape_count = int(np.isfinite(data["escape_time"]).sum())
        width_summary = {
            "pair_count": PAIR_COUNTS[width],
            "discovery_pairs": split,
            "confirmation_pairs": PAIR_COUNTS[width] - split,
            "raw_trajectory_escape_count": escape_count,
            "primary_full": proxy_json(full_primary),
            "primary_discovery": proxy_json(discovery),
            "primary_confirmation": proxy_json(confirmation),
            "inference": inference,
            "sensitivity": sensitivity,
            "numerical_step_halving": numerical,
        }
        summary["widths"][str(width)] = width_summary
        log(
            f"RESULT width={width} escapes={escape_count} "
            f"G0_full={full_primary['G0']:.12g} F_end={full_primary['F_end']:.12g}"
        )
        for name in ("A", "B"):
            inf = inference[name]
            log(
                f"RESULT width={width} {name} "
                f"full_eig={inf['full_matrix_condition']['eigenvalues']} "
                f"confirm_score={inf['confirmation_fixed_direction_score']:.12g} "
                f"bootstrap_upper={inf['bootstrap']['upper_percentile']:.12g} "
                f"confirmed={inf['empirical_negative_confirmed']}"
            )

        np.savez_compressed(
            OUTPUT / f"raw_width_{width}.npz",
            **data,
        )
        np.savez_compressed(
            OUTPUT / f"half_step_width_{width}.npz",
            **half_data,
        )
        np.savez_compressed(
            OUTPUT / f"bootstrap_scores_width_{width}.npz",
            A=bootstrap_samples["A"], B=bootstrap_samples["B"],
        )
        np.savez_compressed(
            OUTPUT / f"primary_proxy_width_{width}.npz",
            times=data["times"],
            full_G=full_primary["G"], full_F=full_primary["F"],
            discovery_G=discovery["G"], discovery_F=discovery["F"],
            confirmation_G=confirmation["G"], confirmation_F=confirmation["F"],
            full_A=full_primary["A"], full_B=full_primary["B"],
            discovery_A=discovery["A"], discovery_B=discovery["B"],
            confirmation_A=confirmation["A"], confirmation_B=confirmation["B"],
        )

    summary_path = OUTPUT / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    log("controls=" + json.dumps(summary["controls"], sort_keys=True))
    log_handle.close()

    artifact_paths = sorted(
        path for path in OUTPUT.iterdir() if path.name != "manifest.json"
    )
    manifest = {
        path.name: {"sha256": hash_file(path), "bytes": path.stat().st_size}
        for path in artifact_paths
    }
    for source in (
        Path(__file__), Path(core.__file__), HERE / "simulate_loewner.py",
        HERE / "corrected_clock_protocol.md",
    ):
        manifest["source/" + source.name] = {
            "sha256": hash_file(source), "bytes": source.stat().st_size
        }
    (OUTPUT / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    )
    print("COMPLETE", flush=True)


if __name__ == "__main__":
    main()
