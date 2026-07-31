#!/usr/bin/env python3
"""Preregistered S=128 exact-reference noise update.

This script implements REFERENCE_NOISE_PREREGISTRATION.md verbatim. It never
imports or modifies the PDE solver and performs no coefficient fitting.
"""

from __future__ import annotations

import csv
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "results" / "raw"
OUT = Path(__file__).resolve().parent
Y = np.asarray([0.8, -0.55, 0.35], dtype=float)
BOOTSTRAP_REPLICATES = 2000
BOOTSTRAP_SEED = 2026072310000

PRIMARY_PDE = "pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz"
BLOCK_FILES = (
    "exact_ensemble_n256_L32_S32_seed6000_dt0p02_T8p0.npz",
    "exact_ensemble_n256_L32_S32_seed8000_dt0p02_T8p0.npz",
    "exact_ensemble_n256_L32_S64_seed10000_dt0p02_T8p0.npz",
)


@dataclass(frozen=True)
class Block:
    label: str
    path: Path
    seed_start: int
    seeds: np.ndarray
    times: np.ndarray
    f: np.ndarray
    grams: np.ndarray
    theta: np.ndarray
    sha256: str

    @property
    def size(self) -> int:
        return int(self.seeds.size)


def write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    fields: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row:
            if key not in seen:
                seen.add(key)
                fields.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def interpolate_depth(values: np.ndarray, target_nodes: int) -> np.ndarray:
    source = np.linspace(0.0, 1.0, values.shape[1])
    target = np.linspace(0.0, 1.0, target_nodes)
    flat = np.swapaxes(values, 0, 1).reshape(values.shape[1], -1)
    out = np.empty((target_nodes, flat.shape[1]), dtype=float)
    for column in range(flat.shape[1]):
        out[:, column] = np.interp(target, source, flat[:, column])
    return np.swapaxes(
        out.reshape((target_nodes,) + np.swapaxes(values, 0, 1).shape[1:]),
        0,
        1,
    )


def load_block(filename: str) -> Block:
    path = RAW / filename
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    with np.load(path, allow_pickle=False) as data:
        metadata = json.loads(str(data["metadata_json"]))
        seeds = data["seeds"].copy()
        times = data["times"].copy()
        f = data["f"].copy()
        grams = data["grams"].copy()
        theta = data["theta"].copy()
        stored_means = {
            name: data[f"{name}_mean"].copy()
            for name in ("f", "grams", "theta")
        }
        stored_sems = {
            name: data[f"{name}_sem"].copy()
            for name in ("f", "grams", "theta")
        }
    expected = {
        "n": 256,
        "depth": 32,
        "duration": 8.0,
        "dt": 0.02,
        "sample_dt": 0.04,
    }
    for key, value in expected.items():
        if metadata.get(key) != value:
            raise ValueError(
                f"{filename}: metadata {key}={metadata.get(key)!r}, "
                f"expected {value!r}"
            )
    if int(metadata["seeds"]) != seeds.size:
        raise ValueError(f"{filename}: seed count mismatch")
    if f.shape != (seeds.size, 201, 3):
        raise ValueError(f"{filename}: unexpected f shape {f.shape}")
    if grams.shape != (seeds.size, 201, 33, 3, 3):
        raise ValueError(f"{filename}: unexpected Gram shape {grams.shape}")
    if theta.shape != (seeds.size, 201, 3, 3):
        raise ValueError(f"{filename}: unexpected theta shape {theta.shape}")
    expected_seeds = np.arange(
        int(metadata["seed_start"]),
        int(metadata["seed_start"]) + seeds.size,
    )
    if not np.array_equal(seeds, expected_seeds):
        raise ValueError(f"{filename}: seeds are not the declared sequence")
    if not np.allclose(
        times, np.linspace(0.0, 8.0, 201), rtol=0.0, atol=1e-14
    ):
        raise ValueError(f"{filename}: unexpected time grid")
    for name, value in (("f", f), ("grams", grams), ("theta", theta)):
        if not np.all(np.isfinite(value)):
            raise ValueError(f"{filename}: nonfinite {name}")
        if not np.array_equal(stored_means[name], np.mean(value, axis=0)):
            raise ValueError(f"{filename}: stored {name} mean mismatch")
        recomputed_sem = np.std(value, axis=0, ddof=1) / np.sqrt(seeds.size)
        if not np.array_equal(stored_sems[name], recomputed_sem):
            raise ValueError(f"{filename}: stored {name} SEM mismatch")
    if np.max(np.abs(grams - np.swapaxes(grams, -1, -2))) > 1e-12:
        raise ValueError(f"{filename}: nonsymmetric Grams")
    if np.max(np.abs(theta - np.swapaxes(theta, -1, -2))) > 1e-12:
        raise ValueError(f"{filename}: nonsymmetric tangent kernels")
    if np.min(np.linalg.eigvalsh(grams.reshape(-1, 3, 3))) < -1e-10:
        raise ValueError(f"{filename}: non-PSD Gram")
    if np.min(np.linalg.eigvalsh(theta.reshape(-1, 3, 3))) < -1e-10:
        raise ValueError(f"{filename}: non-PSD tangent kernel")
    return Block(
        label=f"seed{metadata['seed_start']}_S{metadata['seeds']}",
        path=path,
        seed_start=int(metadata["seed_start"]),
        seeds=seeds,
        times=times,
        f=f,
        grams=grams,
        theta=theta,
        sha256=digest.hexdigest(),
    )


def pool(blocks: Sequence[Block], label: str) -> dict[str, Any]:
    if not blocks:
        raise ValueError("empty pool")
    for block in blocks[1:]:
        if not np.array_equal(block.times, blocks[0].times):
            raise ValueError("block time grids differ")
    seeds = np.concatenate([block.seeds for block in blocks])
    if np.unique(seeds).size != seeds.size:
        raise ValueError(f"{label}: overlapping exact-network seeds")
    return {
        "label": label,
        "block_labels": ";".join(block.label for block in blocks),
        "seeds": seeds,
        "times": blocks[0].times,
        "f": np.concatenate([block.f for block in blocks], axis=0),
        "grams": np.concatenate([block.grams for block in blocks], axis=0),
        "theta": np.concatenate([block.theta for block in blocks], axis=0),
        "block_sizes": [block.size for block in blocks],
    }


def reference_mean(reference: Mapping[str, Any]) -> dict[str, np.ndarray]:
    f = np.mean(reference["f"], axis=0)
    return {
        "times": np.asarray(reference["times"]),
        "f": f,
        "loss": 0.5 * np.sum((f - Y[None, :]) ** 2, axis=-1),
        "grams": np.mean(reference["grams"], axis=0),
        "theta": np.mean(reference["theta"], axis=0),
    }


def load_pde(target_depth_nodes: int) -> dict[str, np.ndarray]:
    with np.load(RAW / PRIMARY_PDE, allow_pickle=False) as data:
        times = data["times"].copy()
        f = data["f"].copy()
        loss = data["loss"].copy()
        grams = data["grams"].copy()
        theta = data["theta"].copy()
    if times.shape != (201,) or not np.isclose(times[-1], 8.0):
        raise ValueError("primary PDE time grid changed")
    return {
        "times": times,
        "f": f,
        "loss": loss,
        "grams": interpolate_depth(grams, target_depth_nodes),
        "theta": theta,
    }


def curve_metrics(
    pde: Mapping[str, np.ndarray],
    reference: Mapping[str, np.ndarray],
) -> dict[str, float]:
    if not np.array_equal(pde["times"], reference["times"]):
        raise ValueError("PDE/reference time grids differ")
    f_gap = np.linalg.norm(pde["f"] - reference["f"], axis=-1)
    gram_gap = np.linalg.norm(
        pde["grams"] - reference["grams"], axis=(-2, -1)
    )
    pde_increment = pde["grams"] - pde["grams"][0:1]
    ref_increment = reference["grams"] - reference["grams"][0:1]
    gram_increment_gap = np.linalg.norm(
        pde_increment - ref_increment, axis=(-2, -1)
    )
    theta_gap = np.linalg.norm(
        pde["theta"] - reference["theta"], axis=(-2, -1)
    )
    pde_motion = float(
        np.max(np.linalg.norm(pde_increment[-1], axis=(-2, -1)))
    )
    ref_motion = float(
        np.max(np.linalg.norm(ref_increment[-1], axis=(-2, -1)))
    )
    increment_sup = float(np.max(gram_increment_gap))
    return {
        "output_sup": float(np.max(f_gap)),
        "output_sup_after_t0": float(np.max(f_gap[1:])),
        "loss_of_mean_sup": float(
            np.max(np.abs(pde["loss"] - reference["loss"]))
        ),
        "gram_absolute_sup": float(np.max(gram_gap)),
        "gram_absolute_terminal": float(np.max(gram_gap[-1])),
        "gram_increment_sup": increment_sup,
        "gram_increment_terminal": float(
            np.max(gram_increment_gap[-1])
        ),
        "theta_sup": float(np.max(theta_gap)),
        "pde_terminal_feature_motion": pde_motion,
        "reference_terminal_feature_motion": ref_motion,
        "gram_increment_fraction_pde_motion": (
            increment_sup / pde_motion if pde_motion > 0 else np.nan
        ),
    }


def reference_pair_metrics(
    left: Mapping[str, np.ndarray],
    right: Mapping[str, np.ndarray],
) -> dict[str, float]:
    f_gap = np.linalg.norm(left["f"] - right["f"], axis=-1)
    gram_gap = np.linalg.norm(
        left["grams"] - right["grams"], axis=(-2, -1)
    )
    left_increment = left["grams"] - left["grams"][0:1]
    right_increment = right["grams"] - right["grams"][0:1]
    increment_gap = np.linalg.norm(
        left_increment - right_increment, axis=(-2, -1)
    )
    theta_gap = np.linalg.norm(
        left["theta"] - right["theta"], axis=(-2, -1)
    )
    return {
        "output_sup": float(np.max(f_gap)),
        "output_sup_after_t0": float(np.max(f_gap[1:])),
        "loss_of_mean_sup": float(
            np.max(np.abs(left["loss"] - right["loss"]))
        ),
        "gram_absolute_sup": float(np.max(gram_gap)),
        "gram_increment_sup": float(np.max(increment_gap)),
        "theta_sup": float(np.max(theta_gap)),
    }


def bootstrap_counts(
    rng: np.random.Generator,
    total: int,
    block_sizes: Sequence[int],
    scheme: str,
    count: int,
) -> np.ndarray:
    if scheme == "pooled":
        return rng.multinomial(
            total, np.full(total, 1.0 / total), size=count
        )
    if scheme != "stratified":
        raise ValueError(scheme)
    parts: list[np.ndarray] = []
    for size in block_sizes:
        parts.append(
            rng.multinomial(
                size, np.full(size, 1.0 / size), size=count
            )
        )
    return np.concatenate(parts, axis=1)


def bootstrap_statistics(
    reference: Mapping[str, Any],
    scheme: str,
) -> dict[str, np.ndarray]:
    raw_f = np.asarray(reference["f"], dtype=float)
    raw_g = np.asarray(reference["grams"], dtype=float)
    raw_t = np.asarray(reference["theta"], dtype=float)
    total = raw_f.shape[0]
    full_f = np.mean(raw_f, axis=0)
    full_g = np.mean(raw_g, axis=0)
    full_g_increment = full_g - full_g[0:1]
    full_t = np.mean(raw_t, axis=0)
    full_loss = 0.5 * np.sum((full_f - Y[None, :]) ** 2, axis=-1)
    flat_f = raw_f.reshape(total, -1)
    flat_g = raw_g.reshape(total, -1)
    raw_g_increment = raw_g - raw_g[:, 0:1]
    flat_g_increment = raw_g_increment.reshape(total, -1)
    flat_t = raw_t.reshape(total, -1)

    statistics = {
        key: np.empty(BOOTSTRAP_REPLICATES, dtype=float)
        for key in (
            "output_sup",
            "output_sup_after_t0",
            "loss_of_mean_sup",
            "gram_absolute_sup",
            "gram_increment_sup",
            "theta_sup",
        )
    }
    # Scheme-specific fixed substreams make reruns independent of loop order.
    offset = 0 if scheme == "pooled" else 104729
    rng = np.random.default_rng(BOOTSTRAP_SEED + offset)
    batch_size = 20
    for start in range(0, BOOTSTRAP_REPLICATES, batch_size):
        stop = min(BOOTSTRAP_REPLICATES, start + batch_size)
        counts = bootstrap_counts(
            rng,
            total,
            reference["block_sizes"],
            scheme,
            stop - start,
        )
        boot_f = (counts @ flat_f / total).reshape(
            (stop - start,) + full_f.shape
        )
        output_error = np.linalg.norm(
            boot_f - full_f[None, ...], axis=-1
        )
        statistics["output_sup"][start:stop] = np.max(
            output_error, axis=1
        )
        statistics["output_sup_after_t0"][start:stop] = np.max(
            output_error[:, 1:], axis=1
        )
        boot_loss = 0.5 * np.sum(
            (boot_f - Y[None, None, :]) ** 2, axis=-1
        )
        statistics["loss_of_mean_sup"][start:stop] = np.max(
            np.abs(boot_loss - full_loss[None, :]), axis=1
        )

        boot_g = (counts @ flat_g / total).reshape(
            (stop - start,) + full_g.shape
        )
        statistics["gram_absolute_sup"][start:stop] = np.max(
            np.linalg.norm(
                boot_g - full_g[None, ...], axis=(-2, -1)
            ),
            axis=(1, 2),
        )
        boot_g_increment = (counts @ flat_g_increment / total).reshape(
            (stop - start,) + full_g_increment.shape
        )
        statistics["gram_increment_sup"][start:stop] = np.max(
            np.linalg.norm(
                boot_g_increment - full_g_increment[None, ...],
                axis=(-2, -1),
            ),
            axis=(1, 2),
        )

        boot_t = (counts @ flat_t / total).reshape(
            (stop - start,) + full_t.shape
        )
        statistics["theta_sup"][start:stop] = np.max(
            np.linalg.norm(
                boot_t - full_t[None, ...], axis=(-2, -1)
            ),
            axis=1,
        )
    return statistics


def bootstrap_rows(
    statistics: Mapping[str, np.ndarray],
    scheme: str,
    observed: Mapping[str, float],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for metric, values in statistics.items():
        obs = float(observed[metric])
        p_value = float(
            (1 + np.count_nonzero(values >= obs))
            / (values.size + 1)
        )
        q90, q95, q99 = np.quantile(values, [0.90, 0.95, 0.99])
        rows.append(
            {
                "scheme": scheme,
                "metric": metric,
                "replicates": values.size,
                "observed_pde_gap": obs,
                "bootstrap_q90": float(q90),
                "bootstrap_q95": float(q95),
                "bootstrap_q99": float(q99),
                "observed_over_q95": float(obs / q95),
                "centered_bootstrap_tail_probability": p_value,
                "resolved_at_5pct": bool(obs > q95),
            }
        )
    return rows


def main() -> None:
    blocks = [load_block(filename) for filename in BLOCK_FILES]
    all_seeds = np.concatenate([block.seeds for block in blocks])
    if np.unique(all_seeds).size != 128:
        raise ValueError("expected 128 distinct exact-network seeds")

    pools: list[dict[str, Any]] = [
        pool([block], block.label) for block in blocks
    ]
    pools.extend(
        [
            pool(blocks[:2], "existing_seed6000_8000_S64"),
            pool(blocks, "full_seed6000_8000_10000_S128"),
            pool(blocks[1:], "leave_out_seed6000_S96"),
            pool((blocks[0], blocks[2]), "leave_out_seed8000_S96"),
            pool(blocks[:2], "leave_out_seed10000_S64"),
        ]
    )
    target_nodes = blocks[0].grams.shape[2]
    pde = load_pde(target_nodes)

    metric_rows: list[dict[str, Any]] = []
    means: dict[str, dict[str, np.ndarray]] = {}
    for reference in pools:
        mean = reference_mean(reference)
        means[reference["label"]] = mean
        metric_rows.append(
            {
                "pool": reference["label"],
                "blocks": reference["block_labels"],
                "seeds": reference["seeds"].size,
                **curve_metrics(pde, mean),
            }
        )

    block_pair_rows: list[dict[str, Any]] = []
    for left_index in range(len(blocks)):
        for right_index in range(left_index + 1, len(blocks)):
            left = blocks[left_index]
            right = blocks[right_index]
            left_mean = means[left.label]
            right_mean = means[right.label]
            block_pair_rows.append(
                {
                    "left": left.label,
                    "right": right.label,
                    "left_seeds": left.size,
                    "right_seeds": right.size,
                    **reference_pair_metrics(left_mean, right_mean),
                }
            )

    full_reference = next(
        item
        for item in pools
        if item["label"] == "full_seed6000_8000_10000_S128"
    )
    full_observed = next(
        item
        for item in metric_rows
        if item["pool"] == "full_seed6000_8000_10000_S128"
    )
    bootstrap_table: list[dict[str, Any]] = []
    distributions: dict[str, np.ndarray] = {}
    for scheme in ("pooled", "stratified"):
        stats = bootstrap_statistics(full_reference, scheme)
        for metric, values in stats.items():
            distributions[f"{scheme}_{metric}"] = values
        bootstrap_table.extend(
            bootstrap_rows(stats, scheme, full_observed)
        )

    primary_rows = [
        row
        for row in bootstrap_table
        if row["metric"] == "gram_increment_sup"
    ]
    primary_resolved = all(row["resolved_at_5pct"] for row in primary_rows)
    primary_decision = (
        "statistically_resolved_at_curvewise_5pct"
        if primary_resolved
        else "not_statistically_resolved_at_curvewise_5pct"
    )

    write_csv(OUT / "reference_noise_block_metrics.csv", metric_rows)
    write_csv(
        OUT / "reference_noise_block_pairwise.csv", block_pair_rows
    )
    write_csv(OUT / "reference_noise_bootstrap.csv", bootstrap_table)
    np.savez_compressed(
        OUT / "reference_noise_bootstrap_distributions.npz",
        **distributions,
    )
    summary = {
        "protocol": "REFERENCE_NOISE_PREREGISTRATION.md",
        "pde": PRIMARY_PDE,
        "block_files": list(BLOCK_FILES),
        "block_sha256": {
            block.path.name: block.sha256 for block in blocks
        },
        "total_distinct_seeds": int(all_seeds.size),
        "bootstrap_replicates": BOOTSTRAP_REPLICATES,
        "bootstrap_seed": BOOTSTRAP_SEED,
        "primary_metric": "gram_increment_sup",
        "primary_decision": primary_decision,
        "full_pool_metrics": full_observed,
        "bootstrap": bootstrap_table,
        "block_metrics": metric_rows,
        "block_pairwise": block_pair_rows,
        "coefficient_fitting_performed": False,
    }
    (OUT / "reference_noise_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "primary_decision": primary_decision,
                "full_pool_metrics": full_observed,
                "primary_bootstrap": primary_rows,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
