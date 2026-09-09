#!/usr/bin/env python3
"""Frozen held-out ordered-limit audit.

Implements ORDERED_LIMIT_PREREGISTRATION.md.  This analysis never imports or
modifies the PDE solver and performs no coefficient fitting.
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
RAW = ROOT / "dense_mup_pde_repro" / "results" / "raw"
OUT = Path(__file__).resolve().parent
Y = np.asarray([0.8, -0.55, 0.35], dtype=float)
BOOTSTRAP_REPLICATES = 2000
BOOTSTRAP_SEED = 2026072314000

PDE_FILES = {
    "P5": "pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz",
    "P15": "pde_QMC_P15_N16_M256_R128_s20260723_dt0p02_T8.npz",
}

EXACT_FILES = {
    "n256_L32_seed6000_S32": (
        "exact_ensemble_n256_L32_S32_seed6000_dt0p02_T8p0.npz",
        256,
        32,
        6000,
        32,
        False,
    ),
    "n256_L32_seed8000_S32": (
        "exact_ensemble_n256_L32_S32_seed8000_dt0p02_T8p0.npz",
        256,
        32,
        8000,
        32,
        False,
    ),
    "n256_L32_seed10000_S64": (
        "exact_ensemble_n256_L32_S64_seed10000_dt0p02_T8p0.npz",
        256,
        32,
        10000,
        64,
        False,
    ),
    "n256_L64_seed7000_S16": (
        "exact_ensemble_n256_L64_S16_seed7000_dt0p02_T8p0.npz",
        256,
        64,
        7000,
        16,
        False,
    ),
    "n256_L64_seed12000_S48_HELDOUT": (
        "exact_ensemble_n256_L64_S48_seed12000_dt0p02_T8p0.npz",
        256,
        64,
        12000,
        48,
        True,
    ),
    "n512_L32_seed14000_S16_HELDOUT": (
        "exact_ensemble_n512_L32_S16_seed14000_dt0p02_T8p0.npz",
        512,
        32,
        14000,
        16,
        True,
    ),
}


@dataclass(frozen=True)
class Block:
    label: str
    path: Path
    n: int
    depth: int
    seed_start: int
    held_out: bool
    seeds: np.ndarray
    times: np.ndarray
    f: np.ndarray
    grams: np.ndarray
    theta: np.ndarray
    sha256: str

    @property
    def size(self) -> int:
        return int(self.seeds.size)


def stable_seed(label: str) -> int:
    digest = hashlib.sha256(label.encode("utf-8")).digest()
    return BOOTSTRAP_SEED + int.from_bytes(digest[:4], "little")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


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
    """Linearly interpolate (..., depth, m, m) on normalized depth."""
    depth_axis = values.ndim - 3
    source_nodes = values.shape[depth_axis]
    if source_nodes == target_nodes:
        return values.copy()
    source = np.linspace(0.0, 1.0, source_nodes)
    target = np.linspace(0.0, 1.0, target_nodes)
    moved = np.moveaxis(values, depth_axis, 0)
    flat = moved.reshape(source_nodes, -1)
    result = np.empty((target_nodes, flat.shape[1]), dtype=float)
    for column in range(flat.shape[1]):
        result[:, column] = np.interp(target, source, flat[:, column])
    reshaped = result.reshape((target_nodes,) + moved.shape[1:])
    return np.moveaxis(reshaped, 0, depth_axis)


def validate_symmetric_psd(name: str, value: np.ndarray) -> None:
    symmetry = float(np.max(np.abs(value - np.swapaxes(value, -1, -2))))
    if symmetry > 1e-12:
        raise ValueError(f"{name}: symmetry defect {symmetry}")
    minimum = float(np.min(np.linalg.eigvalsh(value.reshape(-1, 3, 3))))
    if minimum < -1e-10:
        raise ValueError(f"{name}: minimum eigenvalue {minimum}")


def load_exact(
    label: str,
    specification: tuple[str, int, int, int, int, bool],
) -> Block:
    filename, n, depth, seed_start, size, held_out = specification
    path = RAW / filename
    with np.load(path, allow_pickle=False) as data:
        metadata = json.loads(str(data["metadata_json"]))
        seeds = data["seeds"].copy()
        times = data["times"].copy()
        f = data["f"].copy()
        grams = data["grams"].copy()
        theta = data["theta"].copy()
        stored = {
            key: (
                data[f"{key}_mean"].copy(),
                data[f"{key}_sem"].copy(),
            )
            for key in ("f", "grams", "theta")
        }
    expected_metadata = {
        "n": n,
        "depth": depth,
        "seed_start": seed_start,
        "seeds": size,
        "duration": 8.0,
        "dt": 0.02,
        "sample_dt": 0.04,
        "model": "canonical fully dense residual tanh network",
        "training": "ordinary Euclidean muP gradient flow",
    }
    for key, expected in expected_metadata.items():
        if metadata.get(key) != expected:
            raise ValueError(
                f"{filename}: metadata {key}={metadata.get(key)!r}, "
                f"expected {expected!r}"
            )
    if not np.array_equal(seeds, np.arange(seed_start, seed_start + size)):
        raise ValueError(f"{filename}: unexpected seed sequence")
    if not np.allclose(
        times, np.linspace(0.0, 8.0, 201), rtol=0.0, atol=1e-14
    ):
        raise ValueError(f"{filename}: unexpected time grid")
    expected_shapes = {
        "f": (size, 201, 3),
        "grams": (size, 201, depth + 1, 3, 3),
        "theta": (size, 201, 3, 3),
    }
    values = {"f": f, "grams": grams, "theta": theta}
    for key, expected_shape in expected_shapes.items():
        value = values[key]
        if value.shape != expected_shape:
            raise ValueError(
                f"{filename}: {key} shape {value.shape}, "
                f"expected {expected_shape}"
            )
        if not np.all(np.isfinite(value)):
            raise ValueError(f"{filename}: nonfinite {key}")
        if not np.array_equal(stored[key][0], np.mean(value, axis=0)):
            raise ValueError(f"{filename}: stored {key} mean mismatch")
        sem = np.std(value, axis=0, ddof=1) / np.sqrt(size)
        if not np.array_equal(stored[key][1], sem):
            raise ValueError(f"{filename}: stored {key} SEM mismatch")
    validate_symmetric_psd(f"{filename}: grams", grams)
    validate_symmetric_psd(f"{filename}: theta", theta)
    return Block(
        label=label,
        path=path,
        n=n,
        depth=depth,
        seed_start=seed_start,
        held_out=held_out,
        seeds=seeds,
        times=times,
        f=f,
        grams=grams,
        theta=theta,
        sha256=file_sha256(path),
    )


def subset_block(
    block: Block,
    first: int,
    stop: int,
    label: str,
) -> Block:
    if not (0 <= first < stop <= block.size):
        raise ValueError("invalid subblock")
    return Block(
        label=label,
        path=block.path,
        n=block.n,
        depth=block.depth,
        seed_start=int(block.seeds[first]),
        held_out=block.held_out,
        seeds=block.seeds[first:stop].copy(),
        times=block.times,
        f=block.f[first:stop].copy(),
        grams=block.grams[first:stop].copy(),
        theta=block.theta[first:stop].copy(),
        sha256=block.sha256,
    )


def validation_row(block: Block) -> dict[str, Any]:
    tail_start = int(np.searchsorted(block.times, 4.0))
    mean_f = np.mean(block.f, axis=0)
    mean_g = np.mean(block.grams, axis=0)
    tail_output = np.linalg.norm(
        mean_f[tail_start:] - mean_f[tail_start : tail_start + 1],
        axis=-1,
    )
    tail_gram = np.linalg.norm(
        mean_g[tail_start:] - mean_g[tail_start : tail_start + 1],
        axis=(-2, -1),
    )
    member_output_endpoint = np.linalg.norm(
        block.f[:, -1] - block.f[:, tail_start], axis=-1
    )
    member_gram_endpoint = np.max(
        np.linalg.norm(
            block.grams[:, -1] - block.grams[:, tail_start],
            axis=(-2, -1),
        ),
        axis=1,
    )
    member_loss = 0.5 * np.sum(
        (block.f - Y[None, None, :]) ** 2, axis=-1
    )
    return {
        "block": block.label,
        "filename": block.path.name,
        "sha256": block.sha256,
        "held_out": block.held_out,
        "n": block.n,
        "depth": block.depth,
        "seeds": block.size,
        "integrity_validation_passed": True,
        "mean_tail_output_sup_drift_t4_to_t8": float(
            np.max(tail_output)
        ),
        "mean_tail_gram_sup_drift_t4_to_t8": float(np.max(tail_gram)),
        "member_output_endpoint_drift_t4_to_t8_max": float(
            np.max(member_output_endpoint)
        ),
        "member_gram_endpoint_drift_t4_to_t8_max": float(
            np.max(member_gram_endpoint)
        ),
        "member_final_loss_max": float(np.max(member_loss[:, -1])),
        "member_final_loss_mean": float(np.mean(member_loss[:, -1])),
    }


def pool(blocks: Sequence[Block], label: str) -> dict[str, Any]:
    if not blocks:
        raise ValueError("empty exact pool")
    first = blocks[0]
    for block in blocks[1:]:
        if block.n != first.n or block.depth != first.depth:
            raise ValueError(f"{label}: incompatible n/depth")
        if not np.array_equal(block.times, first.times):
            raise ValueError(f"{label}: incompatible times")
    seeds = np.concatenate([block.seeds for block in blocks])
    if np.unique(seeds).size != seeds.size:
        raise ValueError(f"{label}: overlapping seeds")
    return {
        "label": label,
        "n": first.n,
        "depth": first.depth,
        "times": first.times,
        "seeds": seeds,
        "f": np.concatenate([block.f for block in blocks], axis=0),
        "grams": np.concatenate([block.grams for block in blocks], axis=0),
        "theta": np.concatenate([block.theta for block in blocks], axis=0),
        "block_labels": [block.label for block in blocks],
        "block_sizes": [block.size for block in blocks],
    }


def reference_mean(reference: Mapping[str, Any]) -> dict[str, np.ndarray]:
    f = np.mean(reference["f"], axis=0)
    return {
        "label": str(reference["label"]),
        "times": np.asarray(reference["times"]),
        "f": f,
        "loss": 0.5 * np.sum((f - Y[None, :]) ** 2, axis=-1),
        "grams": np.mean(reference["grams"], axis=0),
        "theta": np.mean(reference["theta"], axis=0),
    }


def load_pde(label: str, filename: str) -> dict[str, np.ndarray]:
    path = RAW / filename
    with np.load(path, allow_pickle=False) as data:
        times = data["times"].copy()
        f = data["f"].copy()
        loss = data["loss"].copy()
        grams = data["grams"].copy()
        theta = data["theta"].copy()
        metadata = (
            json.loads(str(data["metadata_json"]))
            if "metadata_json" in data.files
            else {}
        )
    if not np.allclose(
        times, np.linspace(0.0, 8.0, 201), rtol=0.0, atol=1e-14
    ):
        raise ValueError(f"{filename}: unexpected time grid")
    if f.shape != (201, 3) or grams.shape != (201, 17, 3, 3):
        raise ValueError(f"{filename}: unexpected PDE shapes")
    if theta.shape != (201, 3, 3) or loss.shape != (201,):
        raise ValueError(f"{filename}: unexpected theta/loss shapes")
    for key, value in (
        ("f", f),
        ("loss", loss),
        ("grams", grams),
        ("theta", theta),
    ):
        if not np.all(np.isfinite(value)):
            raise ValueError(f"{filename}: nonfinite {key}")
    loss_defect = float(
        np.max(np.abs(loss - 0.5 * np.sum((f - Y[None, :]) ** 2, axis=-1)))
    )
    if loss_defect > 1e-12:
        raise ValueError(f"{filename}: loss identity defect {loss_defect}")
    validate_symmetric_psd(f"{filename}: grams", grams)
    validate_symmetric_psd(f"{filename}: theta", theta)
    return {
        "label": label,
        "filename": filename,
        "times": times,
        "f": f,
        "loss": loss,
        "grams": grams,
        "theta": theta,
        "metadata": metadata,
        "sha256": file_sha256(path),
    }


def curve_at_depth(
    curve: Mapping[str, np.ndarray],
    target_nodes: int,
) -> dict[str, np.ndarray]:
    return {
        **curve,
        "grams": interpolate_depth(np.asarray(curve["grams"]), target_nodes),
    }


def curve_metrics(
    left: Mapping[str, np.ndarray],
    right: Mapping[str, np.ndarray],
) -> dict[str, float]:
    if not np.array_equal(left["times"], right["times"]):
        raise ValueError("curve times differ")
    if left["grams"].shape != right["grams"].shape:
        raise ValueError("curve depth grids differ")
    f_gap = np.linalg.norm(left["f"] - right["f"], axis=-1)
    left_f_increment = left["f"] - left["f"][0:1]
    right_f_increment = right["f"] - right["f"][0:1]
    f_increment_gap = np.linalg.norm(
        left_f_increment - right_f_increment, axis=-1
    )
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
    left_motion = float(
        np.max(np.linalg.norm(left_increment[-1], axis=(-2, -1)))
    )
    right_motion = float(
        np.max(np.linalg.norm(right_increment[-1], axis=(-2, -1)))
    )
    location = np.unravel_index(np.argmax(increment_gap), increment_gap.shape)
    observed = float(np.max(increment_gap))
    return {
        "output_sup": float(np.max(f_gap)),
        "output_increment_sup": float(np.max(f_increment_gap)),
        "loss_of_mean_sup": float(
            np.max(np.abs(left["loss"] - right["loss"]))
        ),
        "gram_absolute_sup": float(np.max(gram_gap)),
        "gram_increment_sup": observed,
        "gram_increment_terminal": float(np.max(increment_gap[-1])),
        "gram_increment_time_of_max": float(left["times"][location[0]]),
        "gram_increment_depth_fraction_of_max": float(
            location[1] / (increment_gap.shape[1] - 1)
        ),
        "theta_sup": float(np.max(theta_gap)),
        "left_terminal_feature_motion": left_motion,
        "right_terminal_feature_motion": right_motion,
        "gram_increment_fraction_left_motion": (
            observed / left_motion if left_motion > 0 else np.nan
        ),
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
    parts = [
        rng.multinomial(
            size, np.full(size, 1.0 / size), size=count
        )
        for size in block_sizes
    ]
    return np.concatenate(parts, axis=1)


def schemes_for(reference: Mapping[str, Any]) -> tuple[str, ...]:
    if len(reference["block_sizes"]) > 1:
        return ("pooled", "stratified")
    return ("pooled",)


def one_reference_bootstrap(
    reference: Mapping[str, Any],
    scheme: str,
) -> dict[str, np.ndarray]:
    raw_f = np.asarray(reference["f"], dtype=float)
    raw_g = np.asarray(reference["grams"], dtype=float)
    raw_t = np.asarray(reference["theta"], dtype=float)
    total = raw_f.shape[0]
    full_f = np.mean(raw_f, axis=0)
    full_g = np.mean(raw_g, axis=0)
    full_t = np.mean(raw_t, axis=0)
    full_f_increment = full_f - full_f[0:1]
    full_g_increment = full_g - full_g[0:1]
    full_loss = 0.5 * np.sum((full_f - Y[None, :]) ** 2, axis=-1)
    flat_f = raw_f.reshape(total, -1)
    flat_g = raw_g.reshape(total, -1)
    flat_t = raw_t.reshape(total, -1)
    flat_f_increment = (raw_f - raw_f[:, 0:1]).reshape(total, -1)
    flat_g_increment = (raw_g - raw_g[:, 0:1]).reshape(total, -1)
    result = {
        key: np.empty(BOOTSTRAP_REPLICATES, dtype=float)
        for key in (
            "output_sup",
            "output_increment_sup",
            "loss_of_mean_sup",
            "gram_absolute_sup",
            "gram_increment_sup",
            "theta_sup",
        )
    }
    rng = np.random.default_rng(
        stable_seed(f"one:{reference['label']}:{scheme}")
    )
    batch_size = 10
    for start in range(0, BOOTSTRAP_REPLICATES, batch_size):
        stop = min(start + batch_size, BOOTSTRAP_REPLICATES)
        count = stop - start
        weights = bootstrap_counts(
            rng,
            total,
            reference["block_sizes"],
            scheme,
            count,
        )
        boot_f = (weights @ flat_f / total).reshape(
            (count,) + full_f.shape
        )
        output_error = np.linalg.norm(
            boot_f - full_f[None, ...], axis=-1
        )
        result["output_sup"][start:stop] = np.max(output_error, axis=1)
        boot_f_increment = (
            weights @ flat_f_increment / total
        ).reshape((count,) + full_f_increment.shape)
        result["output_increment_sup"][start:stop] = np.max(
            np.linalg.norm(
                boot_f_increment - full_f_increment[None, ...],
                axis=-1,
            ),
            axis=1,
        )
        boot_loss = 0.5 * np.sum(
            (boot_f - Y[None, None, :]) ** 2, axis=-1
        )
        result["loss_of_mean_sup"][start:stop] = np.max(
            np.abs(boot_loss - full_loss[None, :]), axis=1
        )
        boot_g = (weights @ flat_g / total).reshape(
            (count,) + full_g.shape
        )
        result["gram_absolute_sup"][start:stop] = np.max(
            np.linalg.norm(
                boot_g - full_g[None, ...], axis=(-2, -1)
            ),
            axis=(1, 2),
        )
        boot_g_increment = (
            weights @ flat_g_increment / total
        ).reshape((count,) + full_g_increment.shape)
        result["gram_increment_sup"][start:stop] = np.max(
            np.linalg.norm(
                boot_g_increment - full_g_increment[None, ...],
                axis=(-2, -1),
            ),
            axis=(1, 2),
        )
        boot_t = (weights @ flat_t / total).reshape(
            (count,) + full_t.shape
        )
        result["theta_sup"][start:stop] = np.max(
            np.linalg.norm(
                boot_t - full_t[None, ...], axis=(-2, -1)
            ),
            axis=1,
        )
    return result


def quantile_row(
    label: str,
    scheme: str,
    metric: str,
    values: np.ndarray,
    observed: float | None = None,
) -> dict[str, Any]:
    q90, q95, q99 = np.quantile(values, [0.90, 0.95, 0.99])
    row: dict[str, Any] = {
        "label": label,
        "scheme": scheme,
        "metric": metric,
        "replicates": values.size,
        "bootstrap_q90": float(q90),
        "bootstrap_q95": float(q95),
        "bootstrap_q99": float(q99),
    }
    if observed is not None:
        row.update(
            {
                "observed": float(observed),
                "observed_over_q95": float(observed / q95),
                "centered_bootstrap_tail_probability": float(
                    (1 + np.count_nonzero(values >= observed))
                    / (values.size + 1)
                ),
                "resolved_at_5pct_for_scheme": bool(observed > q95),
            }
        )
    return row


def two_reference_gram_bootstrap(
    left: Mapping[str, Any],
    right: Mapping[str, Any],
    target_nodes: int,
    scheme: str,
    label: str,
) -> np.ndarray:
    left_g = interpolate_depth(
        np.asarray(left["grams"], dtype=float), target_nodes
    )
    right_g = interpolate_depth(
        np.asarray(right["grams"], dtype=float), target_nodes
    )
    left_x = (left_g - left_g[:, 0:1]).reshape(left_g.shape[0], -1)
    right_x = (right_g - right_g[:, 0:1]).reshape(right_g.shape[0], -1)
    left_mean = np.mean(left_x, axis=0)
    right_mean = np.mean(right_x, axis=0)
    result = np.empty(BOOTSTRAP_REPLICATES, dtype=float)
    rng_left = np.random.default_rng(stable_seed(f"two:{label}:{scheme}:L"))
    rng_right = np.random.default_rng(
        stable_seed(f"two:{label}:{scheme}:R")
    )
    batch_size = 10
    shape = (201, target_nodes, 3, 3)
    for start in range(0, BOOTSTRAP_REPLICATES, batch_size):
        stop = min(start + batch_size, BOOTSTRAP_REPLICATES)
        count = stop - start
        left_weights = bootstrap_counts(
            rng_left,
            left_x.shape[0],
            left["block_sizes"],
            scheme,
            count,
        )
        right_weights = bootstrap_counts(
            rng_right,
            right_x.shape[0],
            right["block_sizes"],
            scheme,
            count,
        )
        left_deviation = (
            left_weights @ left_x / left_x.shape[0]
        ) - left_mean[None, :]
        right_deviation = (
            right_weights @ right_x / right_x.shape[0]
        ) - right_mean[None, :]
        centered = (left_deviation - right_deviation).reshape(
            (count,) + shape
        )
        result[start:stop] = np.max(
            np.linalg.norm(centered, axis=(-2, -1)),
            axis=(1, 2),
        )
    return result


def pde_improvement_bootstrap(
    reference: Mapping[str, Any],
    p5: Mapping[str, np.ndarray],
    p15: Mapping[str, np.ndarray],
    scheme: str,
) -> np.ndarray:
    target_nodes = int(reference["depth"]) + 1
    p5_g = interpolate_depth(p5["grams"], target_nodes)
    p15_g = interpolate_depth(p15["grams"], target_nodes)
    p5_increment = p5_g - p5_g[0:1]
    p15_increment = p15_g - p15_g[0:1]
    raw_g = np.asarray(reference["grams"], dtype=float)
    raw_x = (raw_g - raw_g[:, 0:1]).reshape(raw_g.shape[0], -1)
    total = raw_x.shape[0]
    result = np.empty(BOOTSTRAP_REPLICATES, dtype=float)
    rng = np.random.default_rng(
        stable_seed(f"improvement:{reference['label']}:{scheme}")
    )
    batch_size = 10
    shape = (201, target_nodes, 3, 3)
    for start in range(0, BOOTSTRAP_REPLICATES, batch_size):
        stop = min(start + batch_size, BOOTSTRAP_REPLICATES)
        count = stop - start
        weights = bootstrap_counts(
            rng,
            total,
            reference["block_sizes"],
            scheme,
            count,
        )
        boot = (weights @ raw_x / total).reshape((count,) + shape)
        d5 = np.max(
            np.linalg.norm(
                p5_increment[None, ...] - boot, axis=(-2, -1)
            ),
            axis=(1, 2),
        )
        d15 = np.max(
            np.linalg.norm(
                p15_increment[None, ...] - boot, axis=(-2, -1)
            ),
            axis=(1, 2),
        )
        result[start:stop] = d5 - d15
    return result


def main() -> None:
    blocks = {
        label: load_exact(label, specification)
        for label, specification in EXACT_FILES.items()
    }
    pdes = {
        label: load_pde(label, filename)
        for label, filename in PDE_FILES.items()
    }
    validation_rows = [
        validation_row(block) for block in blocks.values()
    ]

    l32_blocks = [
        blocks["n256_L32_seed6000_S32"],
        blocks["n256_L32_seed8000_S32"],
        blocks["n256_L32_seed10000_S64"],
    ]
    l64_old = blocks["n256_L64_seed7000_S16"]
    l64_new = blocks["n256_L64_seed12000_S48_HELDOUT"]
    n512 = blocks["n512_L32_seed14000_S16_HELDOUT"]
    references = {
        "E256_L32_S128": pool(l32_blocks, "E256_L32_S128"),
        "E256_L64_old_S16": pool([l64_old], "E256_L64_old_S16"),
        "E256_L64_new_S48": pool([l64_new], "E256_L64_new_S48"),
        "E256_L64_S64": pool(
            [l64_old, l64_new], "E256_L64_S64"
        ),
        "E512_L32_S16": pool([n512], "E512_L32_S16"),
    }

    if np.intersect1d(
        references["E256_L32_S128"]["seeds"],
        references["E256_L64_S64"]["seeds"],
    ).size:
        raise ValueError("seed overlap across n256 depth pools")

    # Deterministic sensitivity subblocks.
    l64_subblocks = [
        subset_block(
            l64_new,
            16 * index,
            16 * (index + 1),
            f"n256_L64_seed{12000 + 16 * index}_S16_SUBBLOCK",
        )
        for index in range(3)
    ]
    n512_halves = [
        subset_block(
            n512,
            8 * index,
            8 * (index + 1),
            f"n512_L32_seed{14000 + 8 * index}_S8_HALF",
        )
        for index in range(2)
    ]

    # Primary deterministic comparisons.
    curve_rows: list[dict[str, Any]] = []
    mean_curves = {
        label: reference_mean(reference)
        for label, reference in references.items()
    }

    exact_pairs = [
        (
            "width_n256_to_n512_at_L32",
            "E512_L32_S16",
            "E256_L32_S128",
            33,
        ),
        (
            "depth_L32_to_L64_at_n256",
            "E256_L64_S64",
            "E256_L32_S128",
            65,
        ),
        (
            "depth_old_L64_block_vs_L32",
            "E256_L64_old_S16",
            "E256_L32_S128",
            65,
        ),
        (
            "depth_heldout_L64_block_vs_L32",
            "E256_L64_new_S48",
            "E256_L32_S128",
            65,
        ),
    ]
    for label, left_label, right_label, target_nodes in exact_pairs:
        left = curve_at_depth(mean_curves[left_label], target_nodes)
        right = curve_at_depth(mean_curves[right_label], target_nodes)
        curve_rows.append(
            {
                "comparison_type": "exact_cauchy",
                "comparison": label,
                "left": left_label,
                "right": right_label,
                "left_seeds": references[left_label]["seeds"].size,
                "right_seeds": references[right_label]["seeds"].size,
                "depth_nodes_compared": target_nodes,
                **curve_metrics(left, right),
            }
        )

    for pde_label, pde in pdes.items():
        for reference_label, reference in references.items():
            target_nodes = int(reference["depth"]) + 1
            left = curve_at_depth(pde, target_nodes)
            right = mean_curves[reference_label]
            curve_rows.append(
                {
                    "comparison_type": "pde_reference",
                    "comparison": f"{pde_label}_vs_{reference_label}",
                    "left": pde_label,
                    "right": reference_label,
                    "left_seeds": "",
                    "right_seeds": reference["seeds"].size,
                    "depth_nodes_compared": target_nodes,
                    **curve_metrics(left, right),
                }
            )

    # Block, leave-one-file-out, and deterministic subblock diagnostics.
    diagnostic_groups: list[tuple[str, list[Block]]] = []
    diagnostic_groups.extend((block.label, [block]) for block in blocks.values())
    diagnostic_groups.extend((block.label, [block]) for block in l64_subblocks)
    diagnostic_groups.extend((block.label, [block]) for block in n512_halves)
    for index, omitted in enumerate(l32_blocks):
        diagnostic_groups.append(
            (
                f"E256_L32_leave_out_{omitted.label}",
                [block for j, block in enumerate(l32_blocks) if j != index],
            )
        )
    diagnostic_groups.extend(
        [
            ("E256_L64_leave_out_old", [l64_new]),
            ("E256_L64_leave_out_heldout", [l64_old]),
        ]
    )
    block_rows: list[dict[str, Any]] = []
    diagnostic_means: dict[str, dict[str, np.ndarray]] = {}
    diagnostic_pools: dict[str, dict[str, Any]] = {}
    for label, group_blocks in diagnostic_groups:
        diagnostic = pool(group_blocks, label)
        diagnostic_pools[label] = diagnostic
        mean = reference_mean(diagnostic)
        diagnostic_means[label] = mean
        for pde_label, pde in pdes.items():
            target_nodes = int(diagnostic["depth"]) + 1
            block_rows.append(
                {
                    "pde": pde_label,
                    "reference_block_or_pool": label,
                    "n": diagnostic["n"],
                    "depth": diagnostic["depth"],
                    "seeds": diagnostic["seeds"].size,
                    "held_out_content": any(
                        block.held_out for block in group_blocks
                    ),
                    **curve_metrics(
                        curve_at_depth(pde, target_nodes),
                        mean,
                    ),
                }
            )

    pairwise_rows: list[dict[str, Any]] = []
    pairwise_groups = [
        ("n256_L32_acquisition", l32_blocks),
        ("n256_L64_acquisition", [l64_old, l64_new]),
        ("n256_L64_heldout_subblocks", l64_subblocks),
        ("n512_L32_heldout_halves", n512_halves),
    ]
    for group_label, group_blocks in pairwise_groups:
        for left_index in range(len(group_blocks)):
            for right_index in range(left_index + 1, len(group_blocks)):
                left_block = group_blocks[left_index]
                right_block = group_blocks[right_index]
                left = reference_mean(pool([left_block], left_block.label))
                right = reference_mean(
                    pool([right_block], right_block.label)
                )
                pairwise_rows.append(
                    {
                        "group": group_label,
                        "left": left_block.label,
                        "right": right_block.label,
                        "left_seeds": left_block.size,
                        "right_seeds": right_block.size,
                        **curve_metrics(left, right),
                    }
                )

    # One-reference uncertainty.
    one_reference_rows: list[dict[str, Any]] = []
    distributions: dict[str, np.ndarray] = {}
    one_reference_stats: dict[tuple[str, str], dict[str, np.ndarray]] = {}
    for reference_label, reference in references.items():
        for scheme in schemes_for(reference):
            statistics = one_reference_bootstrap(reference, scheme)
            one_reference_stats[(reference_label, scheme)] = statistics
            for metric, values in statistics.items():
                distributions[
                    f"one__{reference_label}__{scheme}__{metric}"
                ] = values
                one_reference_rows.append(
                    quantile_row(
                        reference_label,
                        scheme,
                        metric,
                        values,
                    )
                )

    # Two-reference Cauchy uncertainty and decisions.
    cauchy_specifications = [
        (
            "width_n256_to_n512_at_L32",
            "E512_L32_S16",
            "E256_L32_S128",
            33,
        ),
        (
            "depth_L32_to_L64_at_n256",
            "E256_L64_S64",
            "E256_L32_S128",
            65,
        ),
    ]
    cauchy_rows: list[dict[str, Any]] = []
    cauchy_decisions: list[dict[str, Any]] = []
    for label, left_label, right_label, target_nodes in cauchy_specifications:
        observed_row = next(
            row
            for row in curve_rows
            if row["comparison"] == label
        )
        observed = float(observed_row["gram_increment_sup"])
        scheme_rows: list[dict[str, Any]] = []
        for scheme in ("pooled", "stratified"):
            values = two_reference_gram_bootstrap(
                references[left_label],
                references[right_label],
                target_nodes,
                scheme,
                label,
            )
            distributions[f"two__{label}__{scheme}"] = values
            row = quantile_row(
                label,
                scheme,
                "gram_increment_sup",
                values,
                observed,
            )
            row.update({"left": left_label, "right": right_label})
            cauchy_rows.append(row)
            scheme_rows.append(row)
        cauchy_decisions.append(
            {
                "comparison": label,
                "left": left_label,
                "right": right_label,
                "observed_gram_increment_sup": observed,
                "pooled_q95": next(
                    row["bootstrap_q95"]
                    for row in scheme_rows
                    if row["scheme"] == "pooled"
                ),
                "stratified_q95": next(
                    row["bootstrap_q95"]
                    for row in scheme_rows
                    if row["scheme"] == "stratified"
                ),
                "decision": (
                    "statistically_resolved_at_curvewise_5pct"
                    if all(
                        row["resolved_at_5pct_for_scheme"]
                        for row in scheme_rows
                    )
                    else "not_statistically_resolved_at_curvewise_5pct"
                ),
            }
        )

    # PDE/reference primary decisions from the one-reference distributions.
    pde_decision_rows: list[dict[str, Any]] = []
    for pde_label in pdes:
        for reference_label, reference in references.items():
            observed_row = next(
                row
                for row in curve_rows
                if row["comparison"] == f"{pde_label}_vs_{reference_label}"
            )
            observed = float(observed_row["gram_increment_sup"])
            scheme_details: list[dict[str, Any]] = []
            for scheme in schemes_for(reference):
                values = one_reference_stats[(reference_label, scheme)][
                    "gram_increment_sup"
                ]
                q95 = float(np.quantile(values, 0.95))
                scheme_details.append(
                    {
                        "scheme": scheme,
                        "q95": q95,
                        "p": float(
                            (1 + np.count_nonzero(values >= observed))
                            / (values.size + 1)
                        ),
                        "resolved": bool(observed > q95),
                    }
                )
            pde_decision_rows.append(
                {
                    "pde": pde_label,
                    "reference": reference_label,
                    "reference_seeds": reference["seeds"].size,
                    "observed_gram_increment_sup": observed,
                    "schemes": ";".join(
                        detail["scheme"] for detail in scheme_details
                    ),
                    "q95_by_scheme": ";".join(
                        f"{detail['scheme']}={detail['q95']:.17g}"
                        for detail in scheme_details
                    ),
                    "tail_probability_by_scheme": ";".join(
                        f"{detail['scheme']}={detail['p']:.17g}"
                        for detail in scheme_details
                    ),
                    "decision": (
                        "statistically_resolved_at_curvewise_5pct"
                        if all(detail["resolved"] for detail in scheme_details)
                        else "not_statistically_resolved_at_curvewise_5pct"
                    ),
                }
            )

    # P15-versus-P5 closeness direction.
    improvement_rows: list[dict[str, Any]] = []
    improvement_decisions: list[dict[str, Any]] = []
    for reference_label in (
        "E256_L32_S128",
        "E256_L64_S64",
        "E512_L32_S16",
    ):
        reference = references[reference_label]
        p5_observed = next(
            row
            for row in curve_rows
            if row["comparison"] == f"P5_vs_{reference_label}"
        )["gram_increment_sup"]
        p15_observed = next(
            row
            for row in curve_rows
            if row["comparison"] == f"P15_vs_{reference_label}"
        )["gram_increment_sup"]
        observed_improvement = float(p5_observed - p15_observed)
        scheme_rows = []
        for scheme in schemes_for(reference):
            values = pde_improvement_bootstrap(
                reference, pdes["P5"], pdes["P15"], scheme
            )
            distributions[
                f"improvement__{reference_label}__{scheme}"
            ] = values
            lower, median, upper = np.quantile(values, [0.025, 0.5, 0.975])
            if lower > 0:
                classification = "P15_closer"
            elif upper < 0:
                classification = "P15_farther"
            else:
                classification = "direction_unresolved"
            row = {
                "reference": reference_label,
                "scheme": scheme,
                "replicates": values.size,
                "observed_P5_minus_P15": observed_improvement,
                "bootstrap_ci95_lower": float(lower),
                "bootstrap_median": float(median),
                "bootstrap_ci95_upper": float(upper),
                "classification_for_scheme": classification,
            }
            improvement_rows.append(row)
            scheme_rows.append(row)
        classifications = {
            row["classification_for_scheme"] for row in scheme_rows
        }
        final_classification = (
            classifications.pop()
            if len(classifications) == 1
            else "direction_unresolved"
        )
        improvement_decisions.append(
            {
                "reference": reference_label,
                "observed_P5_gap": float(p5_observed),
                "observed_P15_gap": float(p15_observed),
                "observed_P5_minus_P15": observed_improvement,
                "decision": final_classification,
            }
        )

    write_csv(OUT / "ordered_limit_validation.csv", validation_rows)
    write_csv(OUT / "ordered_limit_curve_metrics.csv", curve_rows)
    write_csv(OUT / "ordered_limit_block_metrics.csv", block_rows)
    write_csv(OUT / "ordered_limit_pairwise_blocks.csv", pairwise_rows)
    write_csv(
        OUT / "ordered_limit_one_reference_bootstrap.csv",
        one_reference_rows,
    )
    write_csv(OUT / "ordered_limit_cauchy_bootstrap.csv", cauchy_rows)
    write_csv(OUT / "ordered_limit_cauchy_decisions.csv", cauchy_decisions)
    write_csv(OUT / "ordered_limit_pde_decisions.csv", pde_decision_rows)
    write_csv(
        OUT / "ordered_limit_p15_improvement.csv", improvement_rows
    )
    write_csv(
        OUT / "ordered_limit_p15_decisions.csv", improvement_decisions
    )
    np.savez_compressed(
        OUT / "ordered_limit_bootstrap_distributions.npz",
        **distributions,
    )

    summary = {
        "protocol": "ORDERED_LIMIT_PREREGISTRATION.md",
        "bootstrap_replicates": BOOTSTRAP_REPLICATES,
        "bootstrap_seed": BOOTSTRAP_SEED,
        "coefficient_fitting_performed": False,
        "validation": validation_rows,
        "exact_files": {
            label: {
                "filename": block.path.name,
                "sha256": block.sha256,
                "n": block.n,
                "depth": block.depth,
                "seeds": block.size,
                "held_out": block.held_out,
            }
            for label, block in blocks.items()
        },
        "pde_files": {
            label: {
                "filename": pde["filename"],
                "sha256": pde["sha256"],
            }
            for label, pde in pdes.items()
        },
        "cauchy_decisions": cauchy_decisions,
        "pde_decisions": pde_decision_rows,
        "p15_decisions": improvement_decisions,
        "curve_metrics": curve_rows,
    }
    (OUT / "ordered_limit_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "cauchy_decisions": cauchy_decisions,
                "pde_decisions": pde_decision_rows,
                "p15_decisions": improvement_decisions,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
