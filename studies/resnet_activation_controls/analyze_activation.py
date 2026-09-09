#!/usr/bin/env python3
"""Frozen analysis for the activation-linearity smoking-gun experiment.

The analysis is deliberately metadata driven.  Filenames are never used to
assign a case or an evidence role.  The exact expected inventory is

* five primary P=5, N=16 PDE trajectories;
* four independent-scramble N=16 PDE trajectories;
* C0 and C2 P=5, N=32 PDE depth controls;
* five n=128, L=32, S=16 dense ensembles;
* C0 and C2 n=128, L=64, S=8 dense depth controls; and
* C0 and C2 n=256, L=32, S=4 dense width diagnostics.

All primary cross-case quantities use the common normalizers frozen in
``preregistered_protocol.json``.  The normalizers are recomputed inside every
paired whole-trajectory bootstrap replicate exactly as preregistered.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
import hashlib
from io import StringIO
import json
import os
from pathlib import Path
import sys
from typing import Any, Iterable, Mapping, Sequence

import numpy as np


ROOT = Path(__file__).resolve().parent
sys.path.insert(0, os.fspath(ROOT / "source" / "src"))

from study_cases import StudyCase, load_case  # noqa: E402
from study_metrics import align_dense_depth  # noqa: E402


CASE_IDS = ("C0", "C1", "C2", "C4", "L2")
SCRAMBLE_IDS = ("C0", "C2", "C4", "L2")
DEPTH_IDS = ("C0", "C2")
CONFIRMATORY_ID = "C2"
DESCRIPTIVE_ID = "C4"
METRIC_NAMES = ("gram", "output", "loss")
PROGRESS_GRID = np.linspace(0.0, 0.95, 96)


class AnalysisIntegrityError(RuntimeError):
    """Raised when evidence differs from the frozen metadata inventory."""


@dataclass(frozen=True)
class Descriptor:
    path: Path
    metadata: Mapping[str, Any]


@dataclass(frozen=True)
class Curve:
    """A deterministic PDE curve or an already averaged dense curve."""

    times: np.ndarray
    f: np.ndarray
    grams: np.ndarray
    metadata: Mapping[str, Any]


@dataclass(frozen=True)
class PDEArchive:
    path: Path
    curve: Curve
    theta: np.ndarray
    metadata: Mapping[str, Any]


@dataclass(frozen=True)
class DenseArchive:
    path: Path
    times: np.ndarray
    seeds: np.ndarray
    f: np.ndarray
    grams: np.ndarray
    theta: np.ndarray
    metadata: Mapping[str, Any]

    def mean_curve(self, target_nodes: int = 17) -> Curve:
        aligned = align_dense_depth(self.grams, target_nodes)
        return Curve(
            times=self.times,
            f=np.mean(self.f, axis=0),
            grams=np.mean(aligned.values, axis=0),
            metadata=self.metadata,
        )


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        raise AnalysisIntegrityError(f"cannot read JSON {path}: {error}") from error
    if not isinstance(value, dict):
        raise AnalysisIntegrityError(f"{path}: expected a JSON object")
    return value


def _metadata(path: Path) -> dict[str, Any]:
    try:
        with np.load(path, allow_pickle=False) as archive:
            if "metadata_json" not in archive.files:
                raise AnalysisIntegrityError(f"{path}: missing metadata_json")
            raw = archive["metadata_json"]
            if raw.shape != ():
                raise AnalysisIntegrityError(
                    f"{path}: metadata_json must be a scalar"
                )
            value = json.loads(str(raw))
    except AnalysisIntegrityError:
        raise
    except (OSError, ValueError, json.JSONDecodeError) as error:
        raise AnalysisIntegrityError(
            f"cannot read archive metadata from {path}"
        ) from error
    if not isinstance(value, dict):
        raise AnalysisIntegrityError(f"{path}: metadata is not an object")
    return value


def _equal(left: Any, right: Any) -> bool:
    if isinstance(left, (list, tuple, np.ndarray)) or isinstance(
        right, (list, tuple, np.ndarray)
    ):
        try:
            return bool(np.array_equal(np.asarray(left), np.asarray(right)))
        except (TypeError, ValueError):
            return False
    if isinstance(left, (int, float, np.integer, np.floating)) and isinstance(
        right, (int, float, np.integer, np.floating)
    ):
        return bool(float(left) == float(right))
    return bool(left == right)


def _require_metadata(
    descriptor: Descriptor | Path,
    metadata: Mapping[str, Any],
    expected: Mapping[str, Any],
) -> None:
    label = descriptor.path if isinstance(descriptor, Descriptor) else descriptor
    for key, value in expected.items():
        if key not in metadata:
            raise AnalysisIntegrityError(f"{label}: missing metadata field {key}")
        if not _equal(metadata[key], value):
            raise AnalysisIntegrityError(
                f"{label}: metadata mismatch for {key}: "
                f"{metadata[key]!r} != {value!r}"
            )


def _case_metadata(case: StudyCase) -> dict[str, Any]:
    return {
        "case_id": case.case_id,
        "case_sha256": case.case_sha256,
        "registry_sha256": case.registry_sha256,
        "activation": case.activation,
        "X": case.X.tolist(),
        "y": case.y.tolist(),
        "sigma_w": case.sigma_w,
        "A": case.A,
        "gamma": case.gamma,
    }


def _discover(directory: Path) -> list[Descriptor]:
    if not directory.is_dir():
        raise AnalysisIntegrityError(f"missing evidence directory {directory}")
    output: list[Descriptor] = []
    for path in sorted(directory.iterdir()):
        if not path.is_file():
            raise AnalysisIntegrityError(f"unexpected non-file in {directory}: {path}")
        if path.suffix != ".npz":
            if ".npz" in path.name or path.suffix == ".partial":
                raise AnalysisIntegrityError(f"incomplete archive blocks analysis: {path}")
            continue
        output.append(Descriptor(path=path, metadata=_metadata(path)))
    return output


def _expected_times(duration: float, sample_dt: float) -> np.ndarray:
    count = int(round(duration / sample_dt)) + 1
    return np.arange(count, dtype=float) * sample_dt


def _finite(name: str, array: np.ndarray, path: Path) -> np.ndarray:
    value = np.asarray(array)
    if not np.all(np.isfinite(value)):
        raise AnalysisIntegrityError(f"{path}: non-finite values in {name}")
    return value


def _validate_scientific_hash(metadata: Mapping[str, Any], path: Path) -> None:
    """Validate the PDE scientific-config hash when its source fields exist."""

    fields = (
        "static_compiler_sha256",
        "integrator",
        "duration",
        "start_time",
        "end_time",
        "dt",
        "sample_dt",
        "restart_source_sha256",
    )
    if not all(key in metadata for key in fields):
        raise AnalysisIntegrityError(f"{path}: incomplete scientific config")
    payload = {key: metadata[key] for key in fields}
    blob = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    observed = hashlib.sha256(blob.encode()).hexdigest()
    for key in ("scientific_config_sha256", "config_sha256"):
        if metadata.get(key) != observed:
            raise AnalysisIntegrityError(f"{path}: invalid {key}")


def _load_pde(
    descriptor: Descriptor,
    case: StudyCase,
    expected: Mapping[str, Any],
) -> PDEArchive:
    _require_metadata(descriptor, descriptor.metadata, expected)
    _validate_scientific_hash(descriptor.metadata, descriptor.path)
    required = {
        "times",
        "f",
        "loss",
        "grams",
        "theta",
        "metadata_json",
    }
    try:
        with np.load(descriptor.path, allow_pickle=False) as archive:
            if not required.issubset(archive.files):
                missing = sorted(required - set(archive.files))
                raise AnalysisIntegrityError(
                    f"{descriptor.path}: incomplete PDE schema {missing}"
                )
            times = _finite("times", archive["times"], descriptor.path).copy()
            f = _finite("f", archive["f"], descriptor.path).copy()
            grams = _finite("grams", archive["grams"], descriptor.path).copy()
            theta = _finite("theta", archive["theta"], descriptor.path).copy()
            stored_loss = _finite(
                "loss", archive["loss"], descriptor.path
            ).copy()
    except AnalysisIntegrityError:
        raise
    except (OSError, ValueError) as error:
        raise AnalysisIntegrityError(
            f"cannot load PDE archive {descriptor.path}"
        ) from error
    expected_times = _expected_times(
        float(expected["duration"]), float(expected["sample_dt"])
    )
    m = case.y.size
    nodes = int(expected["depth_nodes_N"]) + 1
    if not np.array_equal(times, expected_times):
        raise AnalysisIntegrityError(f"{descriptor.path}: wrong time grid")
    if f.shape != (times.size, m):
        raise AnalysisIntegrityError(f"{descriptor.path}: wrong f shape {f.shape}")
    if grams.shape != (times.size, nodes, m, m):
        raise AnalysisIntegrityError(
            f"{descriptor.path}: wrong Gram shape {grams.shape}"
        )
    if theta.shape != (times.size, m, m):
        raise AnalysisIntegrityError(
            f"{descriptor.path}: wrong theta shape {theta.shape}"
        )
    recomputed_loss = 0.5 * np.sum(np.square(f - case.y), axis=-1)
    if not np.allclose(stored_loss, recomputed_loss, rtol=0.0, atol=2e-14):
        raise AnalysisIntegrityError(f"{descriptor.path}: stored loss is inconsistent")
    return PDEArchive(
        descriptor.path,
        Curve(times, f, grams, descriptor.metadata),
        theta,
        descriptor.metadata,
    )


def _validate_dense_hash(
    metadata: Mapping[str, Any],
    seeds: np.ndarray,
    path: Path,
) -> None:
    fields = (
        "case_sha256",
        "registry_sha256",
        "n",
        "depth",
        "seed_start",
        "seeds",
        "duration",
        "dt",
        "sample_dt",
        "sigma_w",
        "A",
        "gamma",
        "activation",
        "X",
        "y",
        "pde_seal_sha256",
        "dynamics_sha256",
    )
    if not all(key in metadata for key in fields):
        missing = [key for key in fields if key not in metadata]
        raise AnalysisIntegrityError(f"{path}: missing dense config fields {missing}")
    payload = {key: metadata[key] for key in fields}
    payload["seed_ids"] = [int(value) for value in seeds]
    # run_exact_reference inserts seed_ids after seeds in the dict, but
    # canonical sorting makes insertion order irrelevant.
    blob = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    observed = hashlib.sha256(blob.encode()).hexdigest()
    for key in ("scientific_config_sha256", "config_sha256"):
        if metadata.get(key) != observed:
            raise AnalysisIntegrityError(f"{path}: invalid {key}")


def _load_dense(
    descriptor: Descriptor,
    case: StudyCase,
    expected: Mapping[str, Any],
) -> DenseArchive:
    _require_metadata(descriptor, descriptor.metadata, expected)
    required = {
        "times",
        "seeds",
        "f",
        "grams",
        "theta",
        "f_mean",
        "grams_mean",
        "theta_mean",
        "metadata_json",
    }
    try:
        with np.load(descriptor.path, allow_pickle=False) as archive:
            if not required.issubset(archive.files):
                missing = sorted(required - set(archive.files))
                raise AnalysisIntegrityError(
                    f"{descriptor.path}: incomplete dense schema {missing}"
                )
            times = _finite("times", archive["times"], descriptor.path).copy()
            seeds = np.asarray(archive["seeds"]).copy()
            f = _finite("f", archive["f"], descriptor.path).copy()
            grams = _finite("grams", archive["grams"], descriptor.path).copy()
            theta = _finite("theta", archive["theta"], descriptor.path).copy()
            stored_f_mean = _finite(
                "f_mean", archive["f_mean"], descriptor.path
            ).copy()
            stored_grams_mean = _finite(
                "grams_mean", archive["grams_mean"], descriptor.path
            ).copy()
            stored_theta_mean = _finite(
                "theta_mean", archive["theta_mean"], descriptor.path
            ).copy()
    except AnalysisIntegrityError:
        raise
    except (OSError, ValueError) as error:
        raise AnalysisIntegrityError(
            f"cannot load dense archive {descriptor.path}"
        ) from error
    expected_times = _expected_times(
        float(expected["duration"]), float(expected["sample_dt"])
    )
    members = int(expected["seeds"])
    depth = int(expected["depth"])
    m = case.y.size
    expected_seeds = np.arange(
        int(expected["seed_start"]),
        int(expected["seed_start"]) + members,
        dtype=np.int64,
    )
    if not np.array_equal(times, expected_times):
        raise AnalysisIntegrityError(f"{descriptor.path}: wrong time grid")
    if not np.issubdtype(seeds.dtype, np.integer) or not np.array_equal(
        seeds.astype(np.int64), expected_seeds
    ):
        raise AnalysisIntegrityError(f"{descriptor.path}: wrong seed vector")
    if f.shape != (members, times.size, m):
        raise AnalysisIntegrityError(f"{descriptor.path}: wrong f shape {f.shape}")
    if grams.shape != (members, times.size, depth + 1, m, m):
        raise AnalysisIntegrityError(
            f"{descriptor.path}: wrong Gram shape {grams.shape}"
        )
    if theta.shape != (members, times.size, m, m):
        raise AnalysisIntegrityError(
            f"{descriptor.path}: wrong theta shape {theta.shape}"
        )
    for name, stored, recomputed in (
        ("f_mean", stored_f_mean, np.mean(f, axis=0)),
        ("grams_mean", stored_grams_mean, np.mean(grams, axis=0)),
        ("theta_mean", stored_theta_mean, np.mean(theta, axis=0)),
    ):
        if not np.array_equal(stored, recomputed):
            raise AnalysisIntegrityError(
                f"{descriptor.path}: stored {name} is inconsistent"
            )
    _validate_dense_hash(descriptor.metadata, expected_seeds, descriptor.path)
    return DenseArchive(
        descriptor.path,
        times,
        expected_seeds,
        f,
        grams,
        theta,
        descriptor.metadata,
    )


def _select_one(
    descriptors: Sequence[Descriptor],
    expected: Mapping[str, Any],
    *,
    label: str,
    used: set[Path],
) -> Descriptor:
    matches = [
        item
        for item in descriptors
        if all(_equal(item.metadata.get(key), value) for key, value in expected.items())
    ]
    if len(matches) != 1:
        raise AnalysisIntegrityError(
            f"{label}: expected exactly one metadata match, got {len(matches)}"
        )
    if matches[0].path in used:
        raise AnalysisIntegrityError(f"{label}: archive selected twice")
    used.add(matches[0].path)
    return matches[0]


def _load_inventory(
    *,
    pde_dir: Path,
    dense_dir: Path,
    cases: Mapping[str, StudyCase],
    protocol: Mapping[str, Any],
) -> tuple[
    dict[str, PDEArchive],
    dict[str, PDEArchive],
    dict[str, PDEArchive],
    dict[str, DenseArchive],
    dict[str, DenseArchive],
    dict[str, DenseArchive],
]:
    pde_descriptors = _discover(pde_dir)
    dense_descriptors = _discover(dense_dir)
    fixed = protocol["pde"]
    common_pde = {
        "quadrature": fixed["quadrature"],
        "base_order": int(fixed["base_order"]),
        "basis_size_P": int(fixed["P"]),
        "base_quadrature_M": int(fixed["M"]),
        "fast_quadrature_R": int(fixed["R"]),
        "integrator": fixed["integrator"],
        "duration": float(fixed["duration"]),
        "start_time": 0.0,
        "end_time": float(fixed["duration"]),
        "dt": float(fixed["dt"]),
        "sample_dt": float(fixed["sample_dt"]),
        "restart_source_sha256": None,
    }
    pde_primary: dict[str, PDEArchive] = {}
    pde_scramble: dict[str, PDEArchive] = {}
    pde_n32: dict[str, PDEArchive] = {}
    used_pde: set[Path] = set()
    for case_id in CASE_IDS:
        expected = {
            **_case_metadata(cases[case_id]),
            **common_pde,
            "depth_nodes_N": int(fixed["N"]),
            "quadrature_seed": int(fixed["seed"]),
        }
        item = _select_one(
            pde_descriptors,
            expected,
            label=f"primary PDE {case_id}",
            used=used_pde,
        )
        pde_primary[case_id] = _load_pde(item, cases[case_id], expected)
    for case_id in protocol["pde_numerical_controls"]["scramble_cases"]:
        expected = {
            **_case_metadata(cases[case_id]),
            **common_pde,
            "depth_nodes_N": int(fixed["N"]),
            "quadrature_seed": int(
                protocol["pde_numerical_controls"]["independent_scramble_seed"]
            ),
        }
        item = _select_one(
            pde_descriptors,
            expected,
            label=f"scramble PDE {case_id}",
            used=used_pde,
        )
        pde_scramble[case_id] = _load_pde(item, cases[case_id], expected)
    for case_id in protocol["pde_depth_control"]["cases"]:
        expected = {
            **_case_metadata(cases[case_id]),
            **common_pde,
            "depth_nodes_N": int(protocol["pde_depth_control"]["N"]),
            "quadrature_seed": int(fixed["seed"]),
        }
        item = _select_one(
            pde_descriptors,
            expected,
            label=f"N32 PDE {case_id}",
            used=used_pde,
        )
        pde_n32[case_id] = _load_pde(item, cases[case_id], expected)
    if used_pde != {item.path for item in pde_descriptors}:
        extras = sorted(
            os.fspath(item.path)
            for item in pde_descriptors
            if item.path not in used_pde
        )
        raise AnalysisIntegrityError(f"unexpected PDE archives: {extras}")

    dense_primary: dict[str, DenseArchive] = {}
    dense_l64: dict[str, DenseArchive] = {}
    dense_n256: dict[str, DenseArchive] = {}
    used_dense: set[Path] = set()
    pde_seal_hashes = {
        str(item.metadata.get("pde_seal_sha256"))
        for item in dense_descriptors
    }
    dynamics_hashes = {
        str(item.metadata.get("dynamics_sha256"))
        for item in dense_descriptors
    }
    if len(pde_seal_hashes) != 1 or len(dynamics_hashes) != 1:
        raise AnalysisIntegrityError(
            "dense archives do not share one PDE seal and dynamics hash"
        )
    for role, tier_key, role_cases, destination in (
        ("primary", "dense_reference", CASE_IDS, dense_primary),
        (
            "physical depth",
            "physical_depth_control",
            tuple(protocol["physical_depth_control"]["cases"]),
            dense_l64,
        ),
        (
            "physical width",
            "physical_width_control",
            tuple(protocol["physical_width_control"]["cases"]),
            dense_n256,
        ),
    ):
        tier = protocol[tier_key]
        for case_id in role_cases:
            expected = {
                **_case_metadata(cases[case_id]),
                "n": int(tier["n"]),
                "depth": int(tier["depth"]),
                "seeds": int(tier["seeds"]),
                "seed_start": int(tier["seed_start"]),
                "duration": float(tier["duration"]),
                "dt": float(tier["dt"]),
                "sample_dt": float(tier["sample_dt"]),
                "pde_seal_sha256": next(iter(pde_seal_hashes)),
                "dynamics_sha256": next(iter(dynamics_hashes)),
            }
            item = _select_one(
                dense_descriptors,
                expected,
                label=f"{role} dense {case_id}",
                used=used_dense,
            )
            destination[case_id] = _load_dense(item, cases[case_id], expected)
    if used_dense != {item.path for item in dense_descriptors}:
        extras = sorted(
            os.fspath(item.path)
            for item in dense_descriptors
            if item.path not in used_dense
        )
        raise AnalysisIntegrityError(f"unexpected dense archives: {extras}")
    return (
        pde_primary,
        pde_scramble,
        pde_n32,
        dense_primary,
        dense_l64,
        dense_n256,
    )


def _verify_seal(
    path: Path,
    *,
    expected_stage: str,
    expected_paths: Iterable[Path],
    root: Path,
) -> dict[str, Any]:
    if not path.is_file():
        raise AnalysisIntegrityError(f"required evidence seal is missing: {path}")
    record = _json(path)
    if record.get("stage") != expected_stage:
        raise AnalysisIntegrityError(f"{path}: wrong stage")
    files = record.get("files")
    if not isinstance(files, dict) or record.get("file_count") != len(files):
        raise AnalysisIntegrityError(f"{path}: malformed file map")
    expected = {item.resolve() for item in expected_paths}
    observed: set[Path] = set()
    root_resolved = root.resolve()
    for relative, digest in files.items():
        target = (root / relative).resolve()
        if target != root_resolved and root_resolved not in target.parents:
            raise AnalysisIntegrityError(f"{path}: sealed path escapes root")
        if not target.is_file() or _sha256(target) != digest:
            raise AnalysisIntegrityError(f"{path}: sealed file mismatch {relative}")
        observed.add(target)
    if observed != expected:
        raise AnalysisIntegrityError(f"{path}: archive inventory differs from seal")
    inventory = record.get("inventory")
    if not isinstance(inventory, list) or len(inventory) != len(files):
        raise AnalysisIntegrityError(f"{path}: malformed inventory")
    for item in inventory:
        if not isinstance(item, dict) or "path" not in item or "sha256" not in item:
            raise AnalysisIntegrityError(f"{path}: malformed inventory row")
        target = (root / item["path"]).resolve()
        if target not in expected or item["sha256"] != _sha256(target):
            raise AnalysisIntegrityError(f"{path}: inventory row mismatch")
    return record


def _loss(f: np.ndarray, y: np.ndarray) -> np.ndarray:
    return 0.5 * np.sum(np.square(f - y), axis=-1)


def _gram_motion(grams: np.ndarray) -> float:
    increments = grams - grams[0:1]
    return float(np.max(np.linalg.norm(increments, axis=(-2, -1))))


def _output_motion(f: np.ndarray) -> float:
    return float(np.max(np.linalg.norm(f - f[0:1], axis=-1)))


def _common_scales(
    pde_curves: Mapping[str, Curve],
    dense_curves: Mapping[str, Curve],
    y: np.ndarray,
) -> dict[str, float]:
    curves = [
        curve
        for source in (pde_curves, dense_curves)
        for curve in source.values()
    ]
    return {
        "gram": max(0.05, *(_gram_motion(curve.grams) for curve in curves)),
        "output": max(0.05, *(_output_motion(curve.f) for curve in curves)),
        "loss": max(
            0.05,
            *(float(np.max(_loss(curve.f, y))) for curve in curves),
        ),
    }


def _common_scales_batch(
    pde_curves: Mapping[str, Curve],
    dense_f: Mapping[str, np.ndarray],
    dense_g: Mapping[str, np.ndarray],
    y: np.ndarray,
) -> dict[str, np.ndarray]:
    """Recompute the three common Q values in every bootstrap replicate."""

    first = next(iter(dense_f.values()))
    batch = first.shape[0]
    pde_gram = max(_gram_motion(item.grams) for item in pde_curves.values())
    pde_output = max(_output_motion(item.f) for item in pde_curves.values())
    pde_loss = max(
        float(np.max(_loss(item.f, y))) for item in pde_curves.values()
    )
    dense_gram = np.full(batch, 0.0)
    dense_output = np.full(batch, 0.0)
    dense_loss = np.full(batch, 0.0)
    for case_id in CASE_IDS:
        g_inc = dense_g[case_id] - dense_g[case_id][:, 0:1]
        dense_gram = np.maximum(
            dense_gram,
            np.max(np.linalg.norm(g_inc, axis=(-2, -1)), axis=(1, 2)),
        )
        f_inc = dense_f[case_id] - dense_f[case_id][:, 0:1]
        dense_output = np.maximum(
            dense_output,
            np.max(np.linalg.norm(f_inc, axis=-1), axis=1),
        )
        dense_loss = np.maximum(
            dense_loss,
            np.max(_loss(dense_f[case_id], y), axis=1),
        )
    return {
        "gram": np.maximum.reduce(
            (np.full(batch, 0.05), np.full(batch, pde_gram), dense_gram)
        ),
        "output": np.maximum.reduce(
            (np.full(batch, 0.05), np.full(batch, pde_output), dense_output)
        ),
        "loss": np.maximum.reduce(
            (np.full(batch, 0.05), np.full(batch, pde_loss), dense_loss)
        ),
    }


def _curve_components(
    curve: Curve,
    y: np.ndarray,
) -> dict[str, np.ndarray]:
    return {
        "gram": curve.grams - curve.grams[0:1],
        "output": curve.f - curve.f[0:1],
        "loss": _loss(curve.f, y),
    }


def _point_metric(
    left: Curve,
    right: Curve,
    scales: Mapping[str, float],
    y: np.ndarray,
) -> dict[str, dict[str, Any]]:
    if not np.array_equal(left.times, right.times):
        raise AnalysisIntegrityError("point-comparison time grids differ")
    if left.grams.shape != right.grams.shape:
        raise AnalysisIntegrityError("point-comparison Gram shapes differ")
    a = _curve_components(left, y)
    b = _curve_components(right, y)
    gram_norm = np.linalg.norm(a["gram"] - b["gram"], axis=(-2, -1))
    gram_flat = int(np.argmax(gram_norm))
    gt, gd = np.unravel_index(gram_flat, gram_norm.shape)
    output_norm = np.linalg.norm(a["output"] - b["output"], axis=-1)
    ot = int(np.argmax(output_norm))
    loss_abs = np.abs(a["loss"] - b["loss"])
    lt = int(np.argmax(loss_abs))
    raw = {
        "gram": float(gram_norm[gt, gd]),
        "output": float(output_norm[ot]),
        "loss": float(loss_abs[lt]),
    }
    return {
        "gram": {
            "raw": raw["gram"],
            "denominator": float(scales["gram"]),
            "normalized": raw["gram"] / float(scales["gram"]),
            "max_time": float(left.times[gt]),
            "max_depth_index": int(gd),
            "max_depth_fraction": gd / (left.grams.shape[1] - 1),
        },
        "output": {
            "raw": raw["output"],
            "denominator": float(scales["output"]),
            "normalized": raw["output"] / float(scales["output"]),
            "max_time": float(left.times[ot]),
        },
        "loss": {
            "raw": raw["loss"],
            "denominator": float(scales["loss"]),
            "normalized": raw["loss"] / float(scales["loss"]),
            "max_time": float(left.times[lt]),
        },
    }


def _contrast_arrays(
    case_curve: Curve,
    base_curve: Curve,
    y: np.ndarray,
) -> dict[str, np.ndarray]:
    case = _curve_components(case_curve, y)
    base = _curve_components(base_curve, y)
    return {name: case[name] - base[name] for name in METRIC_NAMES}


def _contrast_metric(
    pde_case: Curve,
    pde_base: Curve,
    dense_case: Curve,
    dense_base: Curve,
    scales: Mapping[str, float],
    y: np.ndarray,
) -> dict[str, dict[str, Any]]:
    pde = _contrast_arrays(pde_case, pde_base, y)
    dense = _contrast_arrays(dense_case, dense_base, y)
    output: dict[str, dict[str, Any]] = {}
    axes_by_name = {
        "gram": (-2, -1),
        "output": (-1,),
        "loss": (),
    }
    for name in METRIC_NAMES:
        delta = pde[name] - dense[name]
        if name == "gram":
            error = float(np.max(np.linalg.norm(delta, axis=(-2, -1))))
            separation = float(
                np.max(np.linalg.norm(dense[name], axis=(-2, -1)))
            )
        elif name == "output":
            error = float(np.max(np.linalg.norm(delta, axis=-1)))
            separation = float(np.max(np.linalg.norm(dense[name], axis=-1)))
        else:
            error = float(np.max(np.abs(delta)))
            separation = float(np.max(np.abs(dense[name])))
        pde_flat = pde[name].reshape(-1)
        dense_flat = dense[name].reshape(-1)
        product = float(np.linalg.norm(pde_flat) * np.linalg.norm(dense_flat))
        cosine = (
            float(np.dot(pde_flat, dense_flat) / product)
            if product > 0.0
            else None
        )
        pde_norm = float(np.linalg.norm(pde_flat))
        dense_norm = float(np.linalg.norm(dense_flat))
        output[name] = {
            "raw": error,
            "denominator": float(scales[name]),
            "normalized": error / float(scales[name]),
            "dense_separation_raw": separation,
            "dense_separation_normalized": separation / float(scales[name]),
            "error_to_separation_ratio": (
                error / separation if separation > 0.0 else None
            ),
            "flattened_cosine": cosine,
            "flattened_amplitude_ratio": (
                pde_norm / dense_norm if dense_norm > 0.0 else None
            ),
            "norm_axes": list(axes_by_name[name]),
        }
    return output


def _batch_metric_raw(
    left_f: np.ndarray,
    left_g: np.ndarray,
    right_f: np.ndarray,
    right_g: np.ndarray,
    y: np.ndarray,
) -> dict[str, np.ndarray]:
    left_g_inc = left_g - left_g[:, 0:1]
    right_g_inc = right_g - right_g[:, 0:1]
    gram = np.max(
        np.linalg.norm(left_g_inc - right_g_inc, axis=(-2, -1)),
        axis=(1, 2),
    )
    left_f_inc = left_f - left_f[:, 0:1]
    right_f_inc = right_f - right_f[:, 0:1]
    output = np.max(
        np.linalg.norm(left_f_inc - right_f_inc, axis=-1),
        axis=1,
    )
    loss = np.max(
        np.abs(_loss(left_f, y) - _loss(right_f, y)),
        axis=1,
    )
    return {"gram": gram, "output": output, "loss": loss}


def _repeat_curve(curve: Curve, batch: int) -> tuple[np.ndarray, np.ndarray]:
    return (
        np.broadcast_to(curve.f, (batch,) + curve.f.shape),
        np.broadcast_to(curve.grams, (batch,) + curve.grams.shape),
    )


def _batch_contrast_error_raw(
    pde_case: Curve,
    pde_base: Curve,
    dense_case_f: np.ndarray,
    dense_case_g: np.ndarray,
    dense_base_f: np.ndarray,
    dense_base_g: np.ndarray,
    y: np.ndarray,
) -> dict[str, np.ndarray]:
    batch = dense_case_f.shape[0]
    pde_case_f, pde_case_g = _repeat_curve(pde_case, batch)
    pde_base_f, pde_base_g = _repeat_curve(pde_base, batch)
    pde_case_components = {
        "gram": pde_case_g - pde_case_g[:, 0:1],
        "output": pde_case_f - pde_case_f[:, 0:1],
        "loss": _loss(pde_case_f, y),
    }
    pde_base_components = {
        "gram": pde_base_g - pde_base_g[:, 0:1],
        "output": pde_base_f - pde_base_f[:, 0:1],
        "loss": _loss(pde_base_f, y),
    }
    dense_case_components = {
        "gram": dense_case_g - dense_case_g[:, 0:1],
        "output": dense_case_f - dense_case_f[:, 0:1],
        "loss": _loss(dense_case_f, y),
    }
    dense_base_components = {
        "gram": dense_base_g - dense_base_g[:, 0:1],
        "output": dense_base_f - dense_base_f[:, 0:1],
        "loss": _loss(dense_base_f, y),
    }
    delta = {
        name: (
            pde_case_components[name]
            - pde_base_components[name]
            - dense_case_components[name]
            + dense_base_components[name]
        )
        for name in METRIC_NAMES
    }
    return {
        "gram": np.max(
            np.linalg.norm(delta["gram"], axis=(-2, -1)), axis=(1, 2)
        ),
        "output": np.max(
            np.linalg.norm(delta["output"], axis=-1), axis=1
        ),
        "loss": np.max(np.abs(delta["loss"]), axis=1),
    }


def _progress_path(
    f: np.ndarray,
    grams: np.ndarray,
    y: np.ndarray,
    loss_scale: float,
    *,
    q_grid: np.ndarray = PROGRESS_GRID,
) -> tuple[np.ndarray | None, dict[str, Any]]:
    loss = _loss(f, y)
    initial = float(loss[0])
    terminal = float(loss[-1])
    drop = initial - terminal
    reduction = drop / initial if initial > 0.0 else 0.0
    increases = np.diff(loss)
    max_increase = max(0.0, float(np.max(increases)))
    tolerance = 1e-8 * float(loss_scale)
    valid = bool(drop > 0.0 and reduction >= 0.95 and max_increase <= tolerance)
    diagnostic = {
        "initial_loss": initial,
        "terminal_loss": terminal,
        "terminal_reduction_fraction": reduction,
        "max_saved_step_loss_increase": max_increase,
        "allowed_saved_step_loss_increase": tolerance,
        "valid": valid,
    }
    if not valid:
        return None, diagnostic
    q = (initial - loss) / drop
    # Only violations already certified as numerical-tolerance-sized are
    # clipped.  No scientifically material reversal is monotonicized.
    q = np.maximum.accumulate(q)
    if q[0] != 0.0:
        q[0] = 0.0
    q[-1] = max(q[-1], 1.0)
    positions = np.searchsorted(q, q_grid, side="left")
    positions = np.clip(positions, 1, q.size - 1)
    left = positions - 1
    right = positions
    q_left = q[left]
    q_right = q[right]
    span = q_right - q_left
    weight = np.divide(
        q_grid - q_left,
        span,
        out=np.zeros_like(q_grid),
        where=span > 0.0,
    )
    shape = (q_grid.size,) + (1,) * (grams.ndim - 1)
    interpolated = (
        (1.0 - weight.reshape(shape)) * grams[left]
        + weight.reshape(shape) * grams[right]
    )
    interpolated -= interpolated[0:1]
    return interpolated, diagnostic


def _progress_batch(
    f: np.ndarray,
    grams: np.ndarray,
    y: np.ndarray,
    loss_scales: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    batch = f.shape[0]
    output = np.full(
        (batch, PROGRESS_GRID.size) + grams.shape[2:],
        np.nan,
        dtype=float,
    )
    valid = np.zeros(batch, dtype=bool)
    for index in range(batch):
        path, diagnostic = _progress_path(
            f[index], grams[index], y, float(loss_scales[index])
        )
        if path is not None:
            output[index] = path
            valid[index] = bool(diagnostic["valid"])
    return output, valid


def _progress_scale_point(
    paths: Mapping[str, Mapping[str, np.ndarray]],
) -> float:
    values = [
        float(np.max(np.linalg.norm(path, axis=(-2, -1))))
        for source in ("pde", "dense")
        for path in paths[source].values()
    ]
    return max(0.05, *values)


def _progress_metric(
    left: np.ndarray,
    right: np.ndarray,
    scale: float,
) -> dict[str, float]:
    raw = float(np.max(np.linalg.norm(left - right, axis=(-2, -1))))
    return {
        "raw": raw,
        "denominator": float(scale),
        "normalized": raw / float(scale),
    }


def _bootstrap_counts(
    rng: np.random.Generator,
    members: int,
    replicates: int,
) -> np.ndarray:
    return rng.multinomial(
        members,
        np.full(members, 1.0 / members),
        size=replicates,
    )


def _basic_interval(
    estimate: float,
    samples: np.ndarray,
    *,
    confidence: float,
) -> dict[str, Any]:
    values = np.asarray(samples, dtype=float)
    finite = np.isfinite(values)
    result: dict[str, Any] = {
        "observed": float(estimate),
        "replicates": int(values.size),
        "finite_replicates": int(np.sum(finite)),
        "confidence": float(confidence),
        "method": "one-sided centered/basic bootstrap",
    }
    if not np.all(finite):
        result.update(
            {
                "available": False,
                "lcb": None,
                "ucb": None,
                "central_low": None,
                "central_high": None,
                "bootstrap_mean": None,
                "bootstrap_sd": None,
            }
        )
        return result
    alpha = 1.0 - confidence
    deviations = values - float(estimate)
    q_high = float(np.quantile(deviations, confidence, method="higher"))
    q_low = float(np.quantile(deviations, alpha, method="lower"))
    q_central_high = float(
        np.quantile(deviations, 1.0 - alpha / 2.0, method="higher")
    )
    q_central_low = float(
        np.quantile(deviations, alpha / 2.0, method="lower")
    )
    result.update(
        {
            "available": True,
            "lcb": float(estimate - q_high),
            "ucb": float(estimate - q_low),
            "central_low": float(estimate - q_central_high),
            "central_high": float(estimate - q_central_low),
            "bootstrap_mean": float(np.mean(values)),
            "bootstrap_sd": float(np.std(values, ddof=1)),
        }
    )
    return result


def _atomic_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    partial = path.with_name(path.name + ".partial")
    with partial.open("w") as handle:
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(partial, path)


def _atomic_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    if not rows:
        raise ValueError(f"cannot write empty CSV {path}")
    fields = list(rows[0])
    for row in rows[1:]:
        for key in row:
            if key not in fields:
                fields.append(key)
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=fields, extrasaction="raise")
    writer.writeheader()
    writer.writerows(rows)
    _atomic_text(path, output.getvalue())


def _to_builtin(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _to_builtin(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_to_builtin(item) for item in value]
    if isinstance(value, np.ndarray):
        return [_to_builtin(item) for item in value.tolist()]
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.bool_,)):
        return bool(value)
    if isinstance(value, (np.floating,)):
        result = float(value)
        return result if np.isfinite(result) else None
    if isinstance(value, float):
        return value if np.isfinite(value) else None
    if isinstance(value, Path):
        return os.fspath(value)
    return value


def _evaluate_primary_batch(
    *,
    pde_curves: Mapping[str, Curve],
    dense_f: Mapping[str, np.ndarray],
    dense_g: Mapping[str, np.ndarray],
    y: np.ndarray,
) -> tuple[dict[str, np.ndarray], dict[str, np.ndarray], dict[str, Any]]:
    """Evaluate every preregistered statistic for a batch of dense means."""

    batch = next(iter(dense_f.values())).shape[0]
    scales = _common_scales_batch(pde_curves, dense_f, dense_g, y)
    stats: dict[str, np.ndarray] = {}
    matched: dict[str, dict[str, np.ndarray]] = {}
    for case_id in CASE_IDS:
        pde_f, pde_g = _repeat_curve(pde_curves[case_id], batch)
        raw = _batch_metric_raw(
            pde_f, pde_g, dense_f[case_id], dense_g[case_id], y
        )
        matched[case_id] = {
            name: raw[name] / scales[name] for name in METRIC_NAMES
        }
        for name in METRIC_NAMES:
            stats[f"matched_{case_id}_{name}"] = matched[case_id][name]

    separations: dict[tuple[str, str], dict[str, np.ndarray]] = {}
    for case_id, base_id in (
        ("C1", "C0"),
        ("C2", "C0"),
        ("C4", "C0"),
        ("C2", "L2"),
    ):
        raw = _batch_metric_raw(
            dense_f[case_id],
            dense_g[case_id],
            dense_f[base_id],
            dense_g[base_id],
            y,
        )
        normalized = {
            name: raw[name] / scales[name] for name in METRIC_NAMES
        }
        separations[(case_id, base_id)] = normalized
        for name in METRIC_NAMES:
            stats[f"dense_separation_{case_id}_{base_id}_{name}"] = (
                normalized[name]
            )

    for case_id in ("C2", "C4"):
        raw = _batch_contrast_error_raw(
            pde_curves[case_id],
            pde_curves["C0"],
            dense_f[case_id],
            dense_g[case_id],
            dense_f["C0"],
            dense_g["C0"],
            y,
        )
        for name in METRIC_NAMES:
            stats[f"contrast_error_{case_id}_C0_{name}"] = (
                raw[name] / scales[name]
            )

    # Confirmatory signed margins are bootstrapped directly.  This avoids the
    # invalid percentile-LCB shortcut for nonnegative sup norms.
    for name in METRIC_NAMES:
        separation = separations[("C2", "C0")][name]
        error = matched["C2"][name]
        stats[f"identity_margin_C2_{name}"] = separation - 2.0 * error
        hermite = separations[("C2", "L2")][name]
        stats[f"linear_null_margin_C2_{name}"] = hermite - 1.5 * error

    progress_diagnostics: dict[str, Any] = {
        "valid_counts": {},
        "replicates": batch,
    }
    pde_progress: dict[str, np.ndarray | None] = {}
    # The path itself does not depend on Q_L; only the frozen numerical
    # monotonicity tolerance does.  The minimum batch Q_L is conservative.
    min_loss_scale = float(np.min(scales["loss"]))
    for case_id in ("C0", "C2"):
        path, diagnostic = _progress_path(
            pde_curves[case_id].f,
            pde_curves[case_id].grams,
            y,
            min_loss_scale,
        )
        pde_progress[case_id] = path
        progress_diagnostics[f"pde_{case_id}"] = diagnostic
    dense_progress: dict[str, np.ndarray] = {}
    dense_valid: dict[str, np.ndarray] = {}
    for case_id in ("C0", "C2"):
        path, valid = _progress_batch(
            dense_f[case_id], dense_g[case_id], y, scales["loss"]
        )
        dense_progress[case_id] = path
        dense_valid[case_id] = valid
        progress_diagnostics["valid_counts"][f"dense_{case_id}"] = int(
            np.sum(valid)
        )
    all_valid = dense_valid["C0"] & dense_valid["C2"]
    if pde_progress["C0"] is None or pde_progress["C2"] is None:
        all_valid[:] = False
    progress_diagnostics["valid_counts"]["joint"] = int(np.sum(all_valid))

    progress_scale = np.full(batch, np.nan)
    progress_separation = np.full(batch, np.nan)
    progress_contrast_error = np.full(batch, np.nan)
    if pde_progress["C0"] is not None and pde_progress["C2"] is not None:
        pde_c0 = pde_progress["C0"]
        pde_c2 = pde_progress["C2"]
        assert pde_c0 is not None and pde_c2 is not None
        pde_motion = max(
            float(np.max(np.linalg.norm(pde_c0, axis=(-2, -1)))),
            float(np.max(np.linalg.norm(pde_c2, axis=(-2, -1)))),
        )
        valid_indices = np.flatnonzero(all_valid)
        for index in valid_indices:
            dense_c0 = dense_progress["C0"][index]
            dense_c2 = dense_progress["C2"][index]
            dense_motion = max(
                float(np.max(np.linalg.norm(dense_c0, axis=(-2, -1)))),
                float(np.max(np.linalg.norm(dense_c2, axis=(-2, -1)))),
            )
            q_scale = max(0.05, pde_motion, dense_motion)
            progress_scale[index] = q_scale
            progress_separation[index] = float(
                np.max(np.linalg.norm(dense_c2 - dense_c0, axis=(-2, -1)))
                / q_scale
            )
            progress_contrast_error[index] = float(
                np.max(
                    np.linalg.norm(
                        (pde_c2 - pde_c0) - (dense_c2 - dense_c0),
                        axis=(-2, -1),
                    )
                )
                / q_scale
            )
    stats["progress_separation_C2_C0_gram"] = progress_separation
    stats["progress_contrast_error_C2_C0_gram"] = progress_contrast_error
    stats["progress_clock_margin_C2_gram"] = (
        progress_separation - 2.0 * progress_contrast_error
    )
    progress_diagnostics["scale"] = progress_scale
    progress_diagnostics["joint_valid"] = all_valid
    return stats, scales, progress_diagnostics


def _primary_bootstrap(
    *,
    pde_curves: Mapping[str, Curve],
    dense: Mapping[str, DenseArchive],
    y: np.ndarray,
    replicates: int,
    seed: int,
    batch_size: int = 20,
) -> tuple[
    dict[str, float],
    dict[str, np.ndarray],
    dict[str, np.ndarray],
    dict[str, Any],
    np.ndarray,
]:
    members = next(iter(dense.values())).seeds.size
    expected_seeds = next(iter(dense.values())).seeds
    for case_id in CASE_IDS:
        if not np.array_equal(dense[case_id].seeds, expected_seeds):
            raise AnalysisIntegrityError(
                "primary dense cases do not share common random-number seeds"
            )
    aligned = {
        case_id: align_dense_depth(dense[case_id].grams, 17).values
        for case_id in CASE_IDS
    }
    mean_f = {
        case_id: np.mean(dense[case_id].f, axis=0, keepdims=True)
        for case_id in CASE_IDS
    }
    mean_g = {
        case_id: np.mean(aligned[case_id], axis=0, keepdims=True)
        for case_id in CASE_IDS
    }
    point_stats_array, point_scales_array, point_progress = (
        _evaluate_primary_batch(
            pde_curves=pde_curves,
            dense_f=mean_f,
            dense_g=mean_g,
            y=y,
        )
    )
    observed = {
        name: float(values[0]) for name, values in point_stats_array.items()
    }
    rng = np.random.default_rng(seed)
    counts = _bootstrap_counts(rng, members, replicates)
    samples = {
        name: np.empty(replicates, dtype=float) for name in observed
    }
    scale_samples = {
        name: np.empty(replicates, dtype=float) for name in METRIC_NAMES
    }
    progress_valid = np.zeros(replicates, dtype=bool)
    for start in range(0, replicates, batch_size):
        stop = min(start + batch_size, replicates)
        weights = counts[start:stop].astype(float) / members
        dense_f = {
            case_id: np.einsum(
                "bs,stm->btm", weights, dense[case_id].f, optimize=True
            )
            for case_id in CASE_IDS
        }
        dense_g = {
            case_id: np.einsum(
                "bs,stdij->btdij",
                weights,
                aligned[case_id],
                optimize=True,
            )
            for case_id in CASE_IDS
        }
        batch_stats, batch_scales, batch_progress = _evaluate_primary_batch(
            pde_curves=pde_curves,
            dense_f=dense_f,
            dense_g=dense_g,
            y=y,
        )
        for name in samples:
            samples[name][start:stop] = batch_stats[name]
        for name in METRIC_NAMES:
            scale_samples[name][start:stop] = batch_scales[name]
        progress_valid[start:stop] = batch_progress["joint_valid"]
    diagnostics = {
        "point_scales": {
            name: float(point_scales_array[name][0]) for name in METRIC_NAMES
        },
        "point_progress": {
            key: value
            for key, value in point_progress.items()
            if key not in {"scale", "joint_valid"}
        },
        "progress_valid_replicates": int(np.sum(progress_valid)),
        "progress_invalid_replicates": int(np.sum(~progress_valid)),
        "common_seed_ids": expected_seeds.tolist(),
    }
    return observed, samples, scale_samples, diagnostics, counts


def _point_cross_metrics(
    *,
    pde_curves: Mapping[str, Curve],
    dense_curves: Mapping[str, Curve],
    scales: Mapping[str, float],
    y: np.ndarray,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    matrix: dict[str, Any] = {}
    rows: list[dict[str, Any]] = []
    for predictor in CASE_IDS:
        matrix[predictor] = {}
        for target in CASE_IDS:
            metrics = _point_metric(
                pde_curves[predictor],
                dense_curves[target],
                scales,
                y,
            )
            matrix[predictor][target] = metrics
            for name in METRIC_NAMES:
                rows.append(
                    {
                        "predictor_case": predictor,
                        "target_case": target,
                        "metric": name,
                        **metrics[name],
                        "matched": predictor == target,
                    }
                )
    return matrix, rows


def _point_activation_evidence(
    *,
    pde_curves: Mapping[str, Curve],
    dense_curves: Mapping[str, Curve],
    cross: Mapping[str, Any],
    scales: Mapping[str, float],
    y: np.ndarray,
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for case_id in ("C1", "C2", "C4"):
        dense_separation = _point_metric(
            dense_curves[case_id], dense_curves["C0"], scales, y
        )
        pde_separation = _point_metric(
            pde_curves[case_id], pde_curves["C0"], scales, y
        )
        contrast = _contrast_metric(
            pde_curves[case_id],
            pde_curves["C0"],
            dense_curves[case_id],
            dense_curves["C0"],
            scales,
            y,
        )
        metrics: dict[str, Any] = {}
        for name in METRIC_NAMES:
            matched = float(cross[case_id][case_id][name]["normalized"])
            separation = float(dense_separation[name]["normalized"])
            identity_pde_to_target = float(
                cross["C0"][case_id][name]["normalized"]
            )
            metrics[name] = {
                "dense_Cc_vs_C0_separation": dense_separation[name],
                "pde_Cc_vs_C0_separation": pde_separation[name],
                "matched_pde_error": cross[case_id][case_id][name],
                "identity_pde_to_target_error": cross["C0"][case_id][name],
                "separation_to_matched_error_ratio": (
                    separation / matched if matched > 0.0 else None
                ),
                "identity_pde_to_target_advantage_ratio": (
                    identity_pde_to_target / matched if matched > 0.0 else None
                ),
                "identity_signed_margin_S_minus_2E": (
                    separation - 2.0 * matched
                ),
                "contrast_fidelity": contrast[name],
            }
        result[case_id] = {
            "inference_role": (
                "confirmatory" if case_id == "C2" else "descriptive"
            ),
            "metrics": metrics,
        }
    return result


def _linear_null_evidence(
    *,
    pde_curves: Mapping[str, Curve],
    dense_curves: Mapping[str, Curve],
    cross: Mapping[str, Any],
    scales: Mapping[str, float],
    y: np.ndarray,
) -> dict[str, Any]:
    separation = _point_metric(
        dense_curves["L2"], dense_curves["C2"], scales, y
    )
    output: dict[str, Any] = {}
    for name in METRIC_NAMES:
        h_value = float(separation[name]["normalized"])
        matched = float(cross["C2"]["C2"][name]["normalized"])
        null_predictor = float(cross["L2"]["C2"][name]["normalized"])
        output[name] = {
            "dense_L2_vs_C2_separation": separation[name],
            "matched_C2_pde_error": cross["C2"]["C2"][name],
            "L2_pde_to_dense_C2_error": cross["L2"]["C2"][name],
            "separation_to_matched_error_ratio": (
                h_value / matched if matched > 0.0 else None
            ),
            "linear_null_pde_advantage_ratio": (
                null_predictor / matched if matched > 0.0 else None
            ),
            "signed_margin_H_minus_1p5E": h_value - 1.5 * matched,
        }
    return output


def _point_progress_evidence(
    *,
    pde_curves: Mapping[str, Curve],
    dense_curves: Mapping[str, Curve],
    scales: Mapping[str, float],
    y: np.ndarray,
) -> dict[str, Any]:
    paths: dict[str, dict[str, np.ndarray]] = {"pde": {}, "dense": {}}
    diagnostics: dict[str, Any] = {"pde": {}, "dense": {}}
    for source_name, curves in (("pde", pde_curves), ("dense", dense_curves)):
        for case_id in ("C0", "C2"):
            path, diagnostic = _progress_path(
                curves[case_id].f,
                curves[case_id].grams,
                y,
                float(scales["loss"]),
            )
            diagnostics[source_name][case_id] = diagnostic
            if path is not None:
                paths[source_name][case_id] = path
    valid = all(
        case_id in paths[source]
        for source in ("pde", "dense")
        for case_id in ("C0", "C2")
    )
    result: dict[str, Any] = {
        "q_definition": "(L(0)-L(t))/(L(0)-L(T))",
        "q_grid": PROGRESS_GRID.tolist(),
        "diagnostics": diagnostics,
        "valid": valid,
        "common_progress_gram_scale": None,
        "dense_C2_vs_C0_separation": None,
        "matched_C2_error": None,
        "activation_contrast_error": None,
        "signed_clock_margin": None,
    }
    if not valid:
        return result
    q_scale = _progress_scale_point(paths)
    separation = _progress_metric(
        paths["dense"]["C2"], paths["dense"]["C0"], q_scale
    )
    matched = _progress_metric(
        paths["pde"]["C2"], paths["dense"]["C2"], q_scale
    )
    contrast_error = _progress_metric(
        paths["pde"]["C2"] - paths["pde"]["C0"],
        paths["dense"]["C2"] - paths["dense"]["C0"],
        q_scale,
    )
    result.update(
        {
            "common_progress_gram_scale": q_scale,
            "dense_C2_vs_C0_separation": separation,
            "matched_C2_error": matched,
            "activation_contrast_error": contrast_error,
            "signed_clock_margin": (
                separation["normalized"]
                - 2.0 * contrast_error["normalized"]
            ),
        }
    )
    return result


def _aligned_curve(curve: Curve, target_nodes: int = 17) -> Curve:
    aligned = align_dense_depth(curve.grams, target_nodes)
    return Curve(curve.times, curve.f, aligned.values, curve.metadata)


def _pde_numerical_controls(
    *,
    primary: Mapping[str, PDEArchive],
    scramble: Mapping[str, PDEArchive],
    n32: Mapping[str, PDEArchive],
    scales: Mapping[str, float],
    y: np.ndarray,
    threshold: float,
) -> dict[str, Any]:
    scramble_metrics: dict[str, Any] = {}
    for case_id in SCRAMBLE_IDS:
        metric = _point_metric(
            primary[case_id].curve,
            scramble[case_id].curve,
            scales,
            y,
        )
        scramble_metrics[case_id] = {
            "metrics": metric,
            "pass_by_metric": {
                name: metric[name]["normalized"] <= threshold
                for name in METRIC_NAMES
            },
        }
    scramble_contrasts: dict[str, Any] = {}
    for case_id in ("C2", "C4"):
        if case_id not in scramble:
            continue
        metric = _contrast_metric(
            primary[case_id].curve,
            primary["C0"].curve,
            scramble[case_id].curve,
            scramble["C0"].curve,
            scales,
            y,
        )
        scramble_contrasts[case_id] = {
            "metrics": metric,
            "pass_by_metric": {
                name: metric[name]["normalized"] <= threshold
                for name in METRIC_NAMES
            },
        }

    n32_metrics: dict[str, Any] = {}
    aligned_n32: dict[str, Curve] = {}
    for case_id in DEPTH_IDS:
        aligned_n32[case_id] = _aligned_curve(n32[case_id].curve, 17)
        metric = _point_metric(
            primary[case_id].curve,
            aligned_n32[case_id],
            scales,
            y,
        )
        n32_metrics[case_id] = {
            "alignment": {
                "source_nodes": 33,
                "target_nodes": 17,
                "source_indices": list(range(0, 33, 2)),
            },
            "metrics": metric,
            "pass_by_metric": {
                name: metric[name]["normalized"] <= threshold
                for name in METRIC_NAMES
            },
        }
    n32_contrast = _contrast_metric(
        primary["C2"].curve,
        primary["C0"].curve,
        aligned_n32["C2"],
        aligned_n32["C0"],
        scales,
        y,
    )
    n32_contrast_record = {
        "metrics": n32_contrast,
        "pass_by_metric": {
            name: n32_contrast[name]["normalized"] <= threshold
            for name in METRIC_NAMES
        },
    }
    central_gram_pass = bool(
        scramble_metrics["C0"]["pass_by_metric"]["gram"]
        and scramble_metrics["C2"]["pass_by_metric"]["gram"]
        and scramble_contrasts["C2"]["pass_by_metric"]["gram"]
        and n32_metrics["C0"]["pass_by_metric"]["gram"]
        and n32_metrics["C2"]["pass_by_metric"]["gram"]
        and n32_contrast_record["pass_by_metric"]["gram"]
    )
    return {
        "threshold": threshold,
        "scramble": scramble_metrics,
        "scramble_activation_contrast": scramble_contrasts,
        "N32": n32_metrics,
        "N32_activation_contrast": n32_contrast_record,
        "central_C0_C2_gram_pass": central_gram_pass,
        "all_metrics_pass": bool(
            all(
                all(item["pass_by_metric"].values())
                for item in scramble_metrics.values()
            )
            and all(
                all(item["pass_by_metric"].values())
                for item in scramble_contrasts.values()
            )
            and all(
                all(item["pass_by_metric"].values())
                for item in n32_metrics.values()
            )
            and all(n32_contrast_record["pass_by_metric"].values())
        ),
    }


def _control_bootstrap(
    *,
    pde_curves: Mapping[str, Curve],
    primary_dense: Mapping[str, DenseArchive],
    dense_l64: Mapping[str, DenseArchive],
    dense_n256: Mapping[str, DenseArchive],
    scales: Mapping[str, float],
    primary_scale_samples: Mapping[str, np.ndarray],
    y: np.ndarray,
    replicates: int,
    seed: int,
    confidence: float,
    batch_size: int = 32,
) -> dict[str, Any]:
    """Depth and width controls with paired C0/C2 trajectory resampling."""

    rng = np.random.default_rng(seed)
    # Advance over the exact primary draw made in _primary_bootstrap.
    _bootstrap_counts(rng, 16, replicates)
    counts_l64 = _bootstrap_counts(rng, 8, replicates)
    counts_n256 = _bootstrap_counts(rng, 4, replicates)

    aligned_primary = {
        case_id: align_dense_depth(primary_dense[case_id].grams, 17).values
        for case_id in DEPTH_IDS
    }
    aligned_l64 = {
        case_id: align_dense_depth(dense_l64[case_id].grams, 17).values
        for case_id in DEPTH_IDS
    }
    aligned_n256 = {
        case_id: align_dense_depth(dense_n256[case_id].grams, 17).values
        for case_id in DEPTH_IDS
    }
    if not np.array_equal(
        primary_dense["C0"].seeds[:8], dense_l64["C0"].seeds
    ) or not np.array_equal(
        primary_dense["C2"].seeds[:8], dense_l64["C2"].seeds
    ):
        raise AnalysisIntegrityError(
            "L64 seeds are not the preregistered L32 paired prefix"
        )
    for source in (dense_l64, dense_n256):
        if not np.array_equal(source["C0"].seeds, source["C2"].seeds):
            raise AnalysisIntegrityError(
                "C0/C2 control ensembles do not share paired seeds"
            )

    def point_control(
        source: Mapping[str, DenseArchive],
        aligned: Mapping[str, np.ndarray],
        *,
        l32_prefix: bool,
    ) -> dict[str, float]:
        f0 = np.mean(source["C0"].f, axis=0, keepdims=True)
        f2 = np.mean(source["C2"].f, axis=0, keepdims=True)
        g0 = np.mean(aligned["C0"], axis=0, keepdims=True)
        g2 = np.mean(aligned["C2"], axis=0, keepdims=True)
        sep = _batch_metric_raw(f2, g2, f0, g0, y)["gram"][0]
        pde_f, pde_g = _repeat_curve(pde_curves["C2"], 1)
        err = _batch_metric_raw(pde_f, pde_g, f2, g2, y)["gram"][0]
        output = {
            "separation": float(sep / scales["gram"]),
            "matched_C2_error": float(err / scales["gram"]),
        }
        if l32_prefix:
            p_f0 = np.mean(primary_dense["C0"].f[:8], axis=0, keepdims=True)
            p_f2 = np.mean(primary_dense["C2"].f[:8], axis=0, keepdims=True)
            p_g0 = np.mean(
                aligned_primary["C0"][:8], axis=0, keepdims=True
            )
            p_g2 = np.mean(
                aligned_primary["C2"][:8], axis=0, keepdims=True
            )
            l32_sep = _batch_metric_raw(
                p_f2, p_g2, p_f0, p_g0, y
            )["gram"][0]
            output["paired_L32_separation"] = float(
                l32_sep / scales["gram"]
            )
            output["retention_ratio"] = (
                float(sep / l32_sep) if l32_sep > 0.0 else np.nan
            )
        else:
            primary_f0 = np.mean(
                primary_dense["C0"].f, axis=0, keepdims=True
            )
            primary_f2 = np.mean(
                primary_dense["C2"].f, axis=0, keepdims=True
            )
            primary_g0 = np.mean(
                aligned_primary["C0"], axis=0, keepdims=True
            )
            primary_g2 = np.mean(
                aligned_primary["C2"], axis=0, keepdims=True
            )
            l32_sep = _batch_metric_raw(
                primary_f2, primary_g2, primary_f0, primary_g0, y
            )["gram"][0]
            output["n128_L32_separation"] = float(
                l32_sep / scales["gram"]
            )
            output["retention_ratio"] = (
                float(sep / l32_sep) if l32_sep > 0.0 else np.nan
            )
        return output

    point_l64 = point_control(dense_l64, aligned_l64, l32_prefix=True)
    point_n256 = point_control(
        dense_n256, aligned_n256, l32_prefix=False
    )

    l64_samples = {
        "separation": np.empty(replicates),
        "matched_C2_error": np.empty(replicates),
        "paired_L32_separation": np.empty(replicates),
        "retention_ratio": np.empty(replicates),
    }
    width_samples = {
        "separation": np.empty(replicates),
        "matched_C2_error": np.empty(replicates),
    }
    for start in range(0, replicates, batch_size):
        stop = min(start + batch_size, replicates)
        qg = primary_scale_samples["gram"][start:stop]
        w8 = counts_l64[start:stop].astype(float) / 8.0
        l64_f = {
            case_id: np.einsum(
                "bs,stm->btm", w8, dense_l64[case_id].f, optimize=True
            )
            for case_id in DEPTH_IDS
        }
        l64_g = {
            case_id: np.einsum(
                "bs,stdij->btdij",
                w8,
                aligned_l64[case_id],
                optimize=True,
            )
            for case_id in DEPTH_IDS
        }
        l32_f = {
            case_id: np.einsum(
                "bs,stm->btm",
                w8,
                primary_dense[case_id].f[:8],
                optimize=True,
            )
            for case_id in DEPTH_IDS
        }
        l32_g = {
            case_id: np.einsum(
                "bs,stdij->btdij",
                w8,
                aligned_primary[case_id][:8],
                optimize=True,
            )
            for case_id in DEPTH_IDS
        }
        sep64_raw = _batch_metric_raw(
            l64_f["C2"], l64_g["C2"], l64_f["C0"], l64_g["C0"], y
        )["gram"]
        pde_f, pde_g = _repeat_curve(pde_curves["C2"], stop - start)
        err64_raw = _batch_metric_raw(
            pde_f, pde_g, l64_f["C2"], l64_g["C2"], y
        )["gram"]
        sep32_raw = _batch_metric_raw(
            l32_f["C2"], l32_g["C2"], l32_f["C0"], l32_g["C0"], y
        )["gram"]
        l64_samples["separation"][start:stop] = sep64_raw / qg
        l64_samples["matched_C2_error"][start:stop] = err64_raw / qg
        l64_samples["paired_L32_separation"][start:stop] = sep32_raw / qg
        l64_samples["retention_ratio"][start:stop] = np.divide(
            sep64_raw,
            sep32_raw,
            out=np.full(stop - start, np.nan),
            where=sep32_raw > 0.0,
        )

        w4 = counts_n256[start:stop].astype(float) / 4.0
        width_f = {
            case_id: np.einsum(
                "bs,stm->btm", w4, dense_n256[case_id].f, optimize=True
            )
            for case_id in DEPTH_IDS
        }
        width_g = {
            case_id: np.einsum(
                "bs,stdij->btdij",
                w4,
                aligned_n256[case_id],
                optimize=True,
            )
            for case_id in DEPTH_IDS
        }
        sep_width_raw = _batch_metric_raw(
            width_f["C2"],
            width_g["C2"],
            width_f["C0"],
            width_g["C0"],
            y,
        )["gram"]
        err_width_raw = _batch_metric_raw(
            pde_f, pde_g, width_f["C2"], width_g["C2"], y
        )["gram"]
        width_samples["separation"][start:stop] = sep_width_raw / qg
        width_samples["matched_C2_error"][start:stop] = err_width_raw / qg

    l64_bounds = {
        name: _basic_interval(
            point_l64[name],
            values,
            confidence=confidence,
        )
        for name, values in l64_samples.items()
    }
    width_bounds = {
        name: _basic_interval(
            point_n256[name],
            values,
            confidence=confidence,
        )
        for name, values in width_samples.items()
    }
    l64_pass = bool(
        l64_bounds["separation"]["available"]
        and l64_bounds["separation"]["lcb"] > 0.05
        and l64_bounds["matched_C2_error"]["ucb"] < 0.05
        and point_l64["retention_ratio"] >= 0.5
    )
    width_point_pass = bool(
        point_n256["separation"] > 0.05
        and point_n256["retention_ratio"] >= 0.5
        and point_n256["matched_C2_error"] < 0.05
    )
    return {
        "physical_depth_L64": {
            "point": point_l64,
            "bounds": l64_bounds,
            "criterion_pass": l64_pass,
            "alignment": {
                "L32_to_N16_indices": list(range(0, 33, 2)),
                "L64_to_N16_indices": list(range(0, 65, 4)),
            },
            "paired_seed_ids": dense_l64["C0"].seeds.tolist(),
        },
        "physical_width_n256": {
            "point": point_n256,
            "bounds_descriptive_only": width_bounds,
            "point_criterion_pass": width_point_pass,
            "diagnostic_only_reason": "S=4",
            "seed_ids": dense_n256["C0"].seeds.tolist(),
        },
    }


def _plateau_record(
    curve: Curve,
    *,
    y: np.ndarray,
    q_gram: float,
    window: Sequence[float],
) -> dict[str, Any]:
    start_matches = np.flatnonzero(curve.times == float(window[0]))
    end_matches = np.flatnonzero(curve.times == float(window[1]))
    if start_matches.size != 1 or end_matches.size != 1:
        raise AnalysisIntegrityError("plateau window endpoints absent from time grid")
    start = int(start_matches[0])
    end = int(end_matches[0])
    loss = _loss(curve.f, y)
    loss_ratio = float(loss[-1] / loss[0]) if loss[0] > 0.0 else np.inf
    gram_drift = float(
        np.max(
            np.linalg.norm(
                curve.grams[end] - curve.grams[start], axis=(-2, -1)
            )
        )
    )
    gram_drift_normalized = gram_drift / q_gram
    loss_pass = loss_ratio <= 1e-6
    gram_pass = gram_drift_normalized <= 0.005
    return {
        "window": [float(window[0]), float(window[1])],
        "initial_loss": float(loss[0]),
        "terminal_loss": float(loss[-1]),
        "terminal_to_initial_loss_ratio": loss_ratio,
        "endpoint_gram_drift_raw": gram_drift,
        "endpoint_gram_drift_normalized": gram_drift_normalized,
        "loss_pass": loss_pass,
        "gram_pass": gram_pass,
        "pass": bool(loss_pass and gram_pass),
    }


def _verify_frozen_maps(record: Mapping[str, Any], root: Path, label: str) -> None:
    for map_name in ("source_files", "protocol_files", "execution_files"):
        files = record.get(map_name)
        if not isinstance(files, dict) or not files:
            raise AnalysisIntegrityError(f"{label}: missing {map_name}")
        for relative, digest in files.items():
            path = (root / relative).resolve()
            if not path.is_file() or _sha256(path) != digest:
                raise AnalysisIntegrityError(
                    f"{label}: frozen file mismatch {relative}"
                )


def _metric_rows(
    *,
    cross_rows: Sequence[Mapping[str, Any]],
    activation: Mapping[str, Any],
    linear_null: Mapping[str, Any],
    progress: Mapping[str, Any],
    numerical: Mapping[str, Any],
    controls: Mapping[str, Any],
    bounds: Mapping[str, Any],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in cross_rows:
        rows.append({"category": "cross_prediction", **row})
    for case_id, case_record in activation.items():
        for metric, record in case_record["metrics"].items():
            mapping = (
                (
                    "dense_separation",
                    record["dense_Cc_vs_C0_separation"]["normalized"],
                    f"dense_separation_{case_id}_C0_{metric}",
                ),
                (
                    "pde_separation",
                    record["pde_Cc_vs_C0_separation"]["normalized"],
                    None,
                ),
                (
                    "matched_pde_error",
                    record["matched_pde_error"]["normalized"],
                    f"matched_{case_id}_{metric}",
                ),
                (
                    "identity_pde_to_target_error",
                    record["identity_pde_to_target_error"]["normalized"],
                    None,
                ),
                (
                    "contrast_error",
                    record["contrast_fidelity"]["normalized"],
                    f"contrast_error_{case_id}_C0_{metric}",
                ),
                (
                    "identity_margin_S_minus_2E",
                    record["identity_signed_margin_S_minus_2E"],
                    (
                        f"identity_margin_{case_id}_{metric}"
                        if case_id == "C2"
                        else None
                    ),
                ),
            )
            for quantity, value, bootstrap_key in mapping:
                row = {
                    "category": "activation_evidence",
                    "case_id": case_id,
                    "inference_role": case_record["inference_role"],
                    "metric": metric,
                    "quantity": quantity,
                    "normalized": value,
                }
                if bootstrap_key in bounds:
                    row.update(
                        {
                            "lcb": bounds[bootstrap_key]["lcb"],
                            "ucb": bounds[bootstrap_key]["ucb"],
                        }
                    )
                rows.append(row)
    for metric, record in linear_null.items():
        for quantity, value, bootstrap_key in (
            (
                "dense_L2_vs_C2_separation",
                record["dense_L2_vs_C2_separation"]["normalized"],
                f"dense_separation_C2_L2_{metric}",
            ),
            (
                "matched_C2_pde_error",
                record["matched_C2_pde_error"]["normalized"],
                f"matched_C2_{metric}",
            ),
            (
                "linear_null_margin_H_minus_1p5E",
                record["signed_margin_H_minus_1p5E"],
                f"linear_null_margin_C2_{metric}",
            ),
        ):
            row = {
                "category": "linear_null",
                "case_id": "C2",
                "comparison_case": "L2",
                "metric": metric,
                "quantity": quantity,
                "normalized": value,
            }
            if bootstrap_key in bounds:
                row.update(
                    {
                        "lcb": bounds[bootstrap_key]["lcb"],
                        "ucb": bounds[bootstrap_key]["ucb"],
                    }
                )
            rows.append(row)
    if progress["valid"]:
        for quantity, value, bootstrap_key in (
            (
                "dense_progress_separation",
                progress["dense_C2_vs_C0_separation"]["normalized"],
                "progress_separation_C2_C0_gram",
            ),
            (
                "matched_progress_error",
                progress["matched_C2_error"]["normalized"],
                None,
            ),
            (
                "progress_contrast_error",
                progress["activation_contrast_error"]["normalized"],
                "progress_contrast_error_C2_C0_gram",
            ),
            (
                "progress_clock_margin",
                progress["signed_clock_margin"],
                "progress_clock_margin_C2_gram",
            ),
        ):
            row = {
                "category": "loss_progress",
                "case_id": "C2",
                "comparison_case": "C0",
                "metric": "gram",
                "quantity": quantity,
                "normalized": value,
            }
            if bootstrap_key in bounds:
                row.update(
                    {
                        "lcb": bounds[bootstrap_key]["lcb"],
                        "ucb": bounds[bootstrap_key]["ucb"],
                    }
                )
            rows.append(row)
    for role in ("scramble", "N32"):
        for case_id, record in numerical[role].items():
            for metric in METRIC_NAMES:
                rows.append(
                    {
                        "category": f"pde_{role}",
                        "case_id": case_id,
                        "metric": metric,
                        "quantity": "discrepancy",
                        "raw": record["metrics"][metric]["raw"],
                        "denominator": record["metrics"][metric]["denominator"],
                        "normalized": record["metrics"][metric]["normalized"],
                        "pass": record["pass_by_metric"][metric],
                    }
                )
    for role in ("scramble_activation_contrast", "N32_activation_contrast"):
        source = numerical[role]
        items = source.items() if role == "scramble_activation_contrast" else [
            ("C2", source)
        ]
        for case_id, record in items:
            for metric in METRIC_NAMES:
                rows.append(
                    {
                        "category": f"pde_{role}",
                        "case_id": case_id,
                        "comparison_case": "C0",
                        "metric": metric,
                        "quantity": "activation_contrast_discrepancy",
                        "normalized": record["metrics"][metric]["normalized"],
                        "pass": record["pass_by_metric"][metric],
                    }
                )
    for control_name, record in controls.items():
        point = record["point"]
        bound_key = (
            "bounds" if "bounds" in record else "bounds_descriptive_only"
        )
        for quantity, value in point.items():
            interval = record[bound_key].get(quantity)
            rows.append(
                {
                    "category": control_name,
                    "case_id": "C2",
                    "comparison_case": "C0",
                    "metric": "gram",
                    "quantity": quantity,
                    "normalized": value,
                    "lcb": interval.get("lcb") if interval else None,
                    "ucb": interval.get("ucb") if interval else None,
                }
            )
    return rows


def _figure_rows(
    *,
    pde_curves: Mapping[str, Curve],
    dense_curves: Mapping[str, Curve],
    dense_primary: Mapping[str, DenseArchive],
    dense_l64: Mapping[str, DenseArchive],
    dense_n256: Mapping[str, DenseArchive],
    activation: Mapping[str, Any],
    bounds: Mapping[str, Any],
    progress: Mapping[str, Any],
    scales: Mapping[str, float],
    y: np.ndarray,
) -> dict[str, list[dict[str, Any]]]:
    time_rows: list[dict[str, Any]] = []
    gram_rows: list[dict[str, Any]] = []
    for source, curves in (("PDE", pde_curves), ("dense", dense_curves)):
        for case_id, curve in curves.items():
            loss = _loss(curve.f, y)
            f_motion = np.linalg.norm(curve.f - curve.f[0:1], axis=-1)
            g_motion = np.linalg.norm(
                curve.grams - curve.grams[0:1], axis=(-2, -1)
            )
            for index, time in enumerate(curve.times):
                time_rows.append(
                    {
                        "source": source,
                        "case_id": case_id,
                        "time": float(time),
                        "loss": float(loss[index]),
                        "output_increment_l2": float(f_motion[index]),
                        "max_depth_gram_increment_fro": float(
                            np.max(g_motion[index])
                        ),
                    }
                )
                for depth in range(curve.grams.shape[1]):
                    gram_rows.append(
                        {
                            "source": source,
                            "case_id": case_id,
                            "time": float(time),
                            "depth_index": depth,
                            "depth_fraction": depth
                            / (curve.grams.shape[1] - 1),
                            "gram_increment_fro": float(
                                g_motion[index, depth]
                            ),
                            "gram_increment_normalized": float(
                                g_motion[index, depth] / scales["gram"]
                            ),
                        }
                    )

    activation_rows: list[dict[str, Any]] = []
    for case_id, case_record in activation.items():
        for metric, record in case_record["metrics"].items():
            for quantity, value, bound_key in (
                (
                    "dense_separation",
                    record["dense_Cc_vs_C0_separation"]["normalized"],
                    f"dense_separation_{case_id}_C0_{metric}",
                ),
                (
                    "matched_error",
                    record["matched_pde_error"]["normalized"],
                    f"matched_{case_id}_{metric}",
                ),
                (
                    "contrast_error",
                    record["contrast_fidelity"]["normalized"],
                    f"contrast_error_{case_id}_C0_{metric}",
                ),
            ):
                interval = bounds.get(bound_key)
                activation_rows.append(
                    {
                        "case_id": case_id,
                        "inference_role": case_record["inference_role"],
                        "metric": metric,
                        "quantity": quantity,
                        "estimate": value,
                        "lcb": interval["lcb"] if interval else None,
                        "ucb": interval["ucb"] if interval else None,
                    }
                )

    progress_rows: list[dict[str, Any]] = []
    if progress["valid"]:
        for source, curves in (("PDE", pde_curves), ("dense", dense_curves)):
            for case_id in ("C0", "C2"):
                path, diagnostic = _progress_path(
                    curves[case_id].f,
                    curves[case_id].grams,
                    y,
                    scales["loss"],
                )
                if path is None:
                    raise AnalysisIntegrityError(
                        "progress became invalid while preparing figure data"
                    )
                norm = np.linalg.norm(path, axis=(-2, -1))
                for q_index, q in enumerate(PROGRESS_GRID):
                    for depth in range(path.shape[1]):
                        progress_rows.append(
                            {
                                "source": source,
                                "case_id": case_id,
                                "fractional_loss_progress": float(q),
                                "depth_index": depth,
                                "depth_fraction": depth / (path.shape[1] - 1),
                                "gram_increment_fro": float(
                                    norm[q_index, depth]
                                ),
                                "progress_path_scale": progress[
                                    "common_progress_gram_scale"
                                ],
                                "terminal_loss_reduction_fraction": diagnostic[
                                    "terminal_reduction_fraction"
                                ],
                            }
                        )
    control_rows: list[dict[str, Any]] = []
    control_sources = (
        ("n128_L32_S16", dense_primary),
        ("n128_L64_S8", dense_l64),
        ("n256_L32_S4", dense_n256),
    )
    for source_name, archives in control_sources:
        mean_curves = {
            case_id: archives[case_id].mean_curve(17) for case_id in DEPTH_IDS
        }
        contrast = (
            mean_curves["C2"].grams
            - mean_curves["C2"].grams[0:1]
            - mean_curves["C0"].grams
            + mean_curves["C0"].grams[0:1]
        )
        norms = np.linalg.norm(contrast, axis=(-2, -1))
        for time_index, time in enumerate(mean_curves["C0"].times):
            for depth in range(17):
                control_rows.append(
                    {
                        "control": source_name,
                        "time": float(time),
                        "depth_index": depth,
                        "depth_fraction": depth / 16,
                        "C2_minus_C0_contrast_fro": float(
                            norms[time_index, depth]
                        ),
                        "contrast_normalized": float(
                            norms[time_index, depth] / scales["gram"]
                        ),
                    }
                )
    interval_rows = [
        {"statistic": name, **record} for name, record in bounds.items()
    ]
    return {
        "figure_time_curves.csv": time_rows,
        "figure_gram_depth_curves.csv": gram_rows,
        "figure_activation_evidence.csv": activation_rows,
        "figure_progress_gram_paths.csv": progress_rows,
        "figure_depth_width_controls.csv": control_rows,
        "figure_bootstrap_intervals.csv": interval_rows,
    }


def _decision_summary(
    *,
    bounds: Mapping[str, Any],
    observed: Mapping[str, float],
    numerical: Mapping[str, Any],
    controls: Mapping[str, Any],
    plateau: Mapping[str, Any],
    progress: Mapping[str, Any],
) -> dict[str, Any]:
    identity_by_metric: dict[str, Any] = {}
    for metric in METRIC_NAMES:
        separation = bounds[f"dense_separation_C2_C0_{metric}"]
        matched = bounds[f"matched_C2_{metric}"]
        margin = bounds[f"identity_margin_C2_{metric}"]
        c0_control = bounds[f"matched_C0_{metric}"]
        checks = {
            "separation_lcb_above_5pct": bool(
                separation["available"] and separation["lcb"] > 0.05
            ),
            "matched_C2_error_ucb_below_5pct": bool(
                matched["available"] and matched["ucb"] < 0.05
            ),
            "S_minus_2E_lcb_positive": bool(
                margin["available"] and margin["lcb"] > 0.0
            ),
            "matched_C0_error_ucb_below_5pct": bool(
                c0_control["available"] and c0_control["ucb"] < 0.05
            ),
        }
        identity_by_metric[metric] = {
            "checks": checks,
            "pass": bool(all(checks.values())),
        }
    linear_bound = bounds["linear_null_margin_C2_gram"]
    linear_separation_bound = bounds[
        "dense_separation_C2_L2_gram"
    ]
    linear_checks = {
        "L2_vs_C2_separation_lcb_above_5pct": bool(
            linear_separation_bound["available"]
            and linear_separation_bound["lcb"] > 0.05
        ),
        "H_minus_1p5E_lcb_positive": bool(
            linear_bound["available"] and linear_bound["lcb"] > 0.0
        ),
    }
    linear_rule = {
        "separation": linear_separation_bound,
        "margin": linear_bound,
        "checks": linear_checks,
        "pass": bool(all(linear_checks.values())),
    }
    plateau_clock_pass = all(
        plateau[source][case_id]["pass"]
        for source in ("pde", "dense")
        for case_id in ("C0", "C2")
    )
    progress_separation = bounds["progress_separation_C2_C0_gram"]
    progress_margin = bounds["progress_clock_margin_C2_gram"]
    clock_checks = {
        "point_paths_valid": bool(progress["valid"]),
        "all_bootstrap_paths_valid": bool(
            progress_separation["available"] and progress_margin["available"]
        ),
        "plateau_C0_C2_pde_dense_pass": plateau_clock_pass,
        "progress_separation_lcb_above_5pct": bool(
            progress_separation["available"]
            and progress_separation["lcb"] > 0.05
        ),
        "progress_contrast_margin_lcb_positive": bool(
            progress_margin["available"] and progress_margin["lcb"] > 0.0
        ),
    }
    clock_rule = {"checks": clock_checks, "pass": bool(all(clock_checks.values()))}
    central_numerical = bool(numerical["central_C0_C2_gram_pass"])
    physical_depth_pass = bool(
        controls["physical_depth_L64"]["criterion_pass"]
    )
    full_nonlinear = bool(
        identity_by_metric["gram"]["pass"]
        and linear_rule["pass"]
        and central_numerical
        and physical_depth_pass
    )
    identity_supported = bool(
        identity_by_metric["gram"]["pass"]
        and central_numerical
        and physical_depth_pass
    )
    joint_curve = bool(
        full_nonlinear
        and identity_by_metric["output"]["pass"]
        and identity_by_metric["loss"]["pass"]
        and numerical["all_metrics_pass"]
    )
    strongest = bool(full_nonlinear and clock_rule["pass"])
    sep_point = observed["dense_separation_C2_C0_gram"]
    matched_point = observed["matched_C2_gram"]
    identity_margin_point = observed["identity_margin_C2_gram"]
    if strongest:
        status = "strongest_not_just_a_clock"
    elif full_nonlinear:
        status = "full_nonlinear_smoking_gun"
    elif identity_supported and not linear_rule["pass"]:
        status = "identity_only"
    elif (
        sep_point <= 0.05
        or matched_point >= 0.05
        or identity_margin_point <= 0.0
    ):
        status = "no_smoking_gun"
    else:
        status = "descriptive_only"
    return {
        "confirmatory_case": "C2",
        "C4_role": "descriptive dose-response only",
        "identity_rule_by_metric": identity_by_metric,
        "beyond_first_hermite_rule": linear_rule,
        "central_numerical_C0_C2_gram_pass": central_numerical,
        "all_observable_numerical_pass": bool(numerical["all_metrics_pass"]),
        "physical_depth_L64_pass": physical_depth_pass,
        "physical_width_n256_diagnostic": controls[
            "physical_width_n256"
        ]["point_criterion_pass"],
        "identity_supported_after_numerical_depth_gates": identity_supported,
        "not_just_a_clock_rule": clock_rule,
        "full_nonlinear_smoking_gun": full_nonlinear,
        "joint_curve_smoking_gun": joint_curve,
        "clock_robust_strongest_tier": strongest,
        "status": status,
    }


def _array_sha256(array: np.ndarray) -> str:
    value = np.ascontiguousarray(array)
    digest = hashlib.sha256()
    digest.update(str(value.dtype).encode())
    digest.update(np.asarray(value.shape, dtype=np.int64).tobytes())
    digest.update(value.tobytes())
    return digest.hexdigest()


def run_analysis(args: argparse.Namespace) -> dict[str, Any]:
    root = Path(args.root).resolve()
    protocol_path = Path(args.protocol).resolve()
    cases_path = Path(args.cases).resolve()
    pde_dir = Path(args.pde_dir).resolve()
    dense_dir = Path(args.dense_dir).resolve()
    output_dir = Path(args.output_dir).resolve()
    protocol = _json(protocol_path)
    if tuple(protocol.get("primary_cases", ())) != ("C0", "C1", "C2", "C4"):
        raise AnalysisIntegrityError("unexpected primary-case registry")
    if tuple(protocol.get("linear_null_cases", ())) != ("L2",):
        raise AnalysisIntegrityError("unexpected linear-null registry")
    if int(protocol["bootstrap"]["replicates"]) != 4000:
        raise AnalysisIntegrityError("frozen bootstrap replicate count is not 4000")
    cases = {
        case_id: load_case(cases_path, case_id) for case_id in CASE_IDS
    }
    y = np.asarray(protocol["model"]["y"], dtype=float)
    for case in cases.values():
        if not np.array_equal(case.y, y):
            raise AnalysisIntegrityError("all cases must share the frozen labels")

    (
        pde_primary,
        pde_scramble,
        pde_n32,
        dense_primary,
        dense_l64,
        dense_n256,
    ) = _load_inventory(
        pde_dir=pde_dir,
        dense_dir=dense_dir,
        cases=cases,
        protocol=protocol,
    )
    pde_paths = [
        archive.path
        for source in (pde_primary, pde_scramble, pde_n32)
        for archive in source.values()
    ]
    dense_paths = [
        archive.path
        for source in (dense_primary, dense_l64, dense_n256)
        for archive in source.values()
    ]
    results_dir = pde_dir.parent
    pde_seal_path = results_dir / "PDE_STAGE_SEAL.json"
    dense_seal_path = results_dir / "DENSE_STAGE_SEAL.json"
    pde_seal = _verify_seal(
        pde_seal_path,
        expected_stage="activation_linearity_pde",
        expected_paths=pde_paths,
        root=root,
    )
    dense_seal = _verify_seal(
        dense_seal_path,
        expected_stage="activation_linearity_dense",
        expected_paths=dense_paths,
        root=root,
    )
    _verify_frozen_maps(pde_seal, root, "PDE seal")
    _verify_frozen_maps(dense_seal, root, "dense seal")
    if dense_seal.get("pde_seal_sha256") != _sha256(pde_seal_path):
        raise AnalysisIntegrityError("dense seal references another PDE seal")
    if dense_seal.get("dynamics_sha256") != pde_seal.get("dynamics_sha256"):
        raise AnalysisIntegrityError("PDE and dense seals have different dynamics")
    for archive in dense_paths:
        metadata = _metadata(archive)
        if metadata.get("pde_seal_sha256") != _sha256(pde_seal_path):
            raise AnalysisIntegrityError(
                f"{archive}: embedded PDE seal hash is wrong"
            )

    pde_curves = {
        case_id: archive.curve for case_id, archive in pde_primary.items()
    }
    dense_curves = {
        case_id: archive.mean_curve(17)
        for case_id, archive in dense_primary.items()
    }
    reference_times = pde_curves["C0"].times
    for source_name, curves in (("PDE", pde_curves), ("dense", dense_curves)):
        for case_id, curve in curves.items():
            if not np.array_equal(curve.times, reference_times):
                raise AnalysisIntegrityError(
                    f"{source_name}/{case_id}: primary time grid differs"
                )
            if curve.grams.shape[1] != 17:
                raise AnalysisIntegrityError(
                    f"{source_name}/{case_id}: primary Grams not on N16 nodes"
                )
    common_scales = _common_scales(pde_curves, dense_curves, y)
    cross, cross_rows = _point_cross_metrics(
        pde_curves=pde_curves,
        dense_curves=dense_curves,
        scales=common_scales,
        y=y,
    )
    activation = _point_activation_evidence(
        pde_curves=pde_curves,
        dense_curves=dense_curves,
        cross=cross,
        scales=common_scales,
        y=y,
    )
    linear_null = _linear_null_evidence(
        pde_curves=pde_curves,
        dense_curves=dense_curves,
        cross=cross,
        scales=common_scales,
        y=y,
    )
    progress = _point_progress_evidence(
        pde_curves=pde_curves,
        dense_curves=dense_curves,
        scales=common_scales,
        y=y,
    )

    replicates = int(protocol["bootstrap"]["replicates"])
    bootstrap_seed = int(protocol["bootstrap"]["seed"])
    confidence = float(protocol["bootstrap"]["confidence"])
    (
        observed,
        bootstrap_samples,
        scale_samples,
        bootstrap_diagnostics,
        primary_counts,
    ) = _primary_bootstrap(
        pde_curves=pde_curves,
        dense=dense_primary,
        y=y,
        replicates=replicates,
        seed=bootstrap_seed,
    )
    for name in METRIC_NAMES:
        if abs(
            bootstrap_diagnostics["point_scales"][name] - common_scales[name]
        ) > 4e-15 * max(1.0, common_scales[name]):
            raise AnalysisIntegrityError(
                f"point and batch common {name} scales disagree"
            )
    bounds = {
        name: _basic_interval(
            observed[name],
            values,
            confidence=confidence,
        )
        for name, values in bootstrap_samples.items()
    }

    numerical = _pde_numerical_controls(
        primary=pde_primary,
        scramble=pde_scramble,
        n32=pde_n32,
        scales=common_scales,
        y=y,
        threshold=float(
            protocol["pde_numerical_controls"]["pass_margin_normalized"]
        ),
    )
    controls = _control_bootstrap(
        pde_curves=pde_curves,
        primary_dense=dense_primary,
        dense_l64=dense_l64,
        dense_n256=dense_n256,
        scales=common_scales,
        primary_scale_samples=scale_samples,
        y=y,
        replicates=replicates,
        seed=bootstrap_seed,
        confidence=confidence,
    )
    plateau: dict[str, dict[str, Any]] = {"pde": {}, "dense": {}}
    plateau_window = protocol["plateau_reporting_rule"]["check_window"]
    for source_name, curves in (("pde", pde_curves), ("dense", dense_curves)):
        for case_id, curve in curves.items():
            plateau[source_name][case_id] = _plateau_record(
                curve,
                y=y,
                q_gram=common_scales["gram"],
                window=plateau_window,
            )
    decision = _decision_summary(
        bounds=bounds,
        observed=observed,
        numerical=numerical,
        controls=controls,
        plateau=plateau,
        progress=progress,
    )

    metrics_rows = _metric_rows(
        cross_rows=cross_rows,
        activation=activation,
        linear_null=linear_null,
        progress=progress,
        numerical=numerical,
        controls=controls,
        bounds=bounds,
    )
    figure_rows = _figure_rows(
        pde_curves=pde_curves,
        dense_curves=dense_curves,
        dense_primary=dense_primary,
        dense_l64=dense_l64,
        dense_n256=dense_n256,
        activation=activation,
        bounds=bounds,
        progress=progress,
        scales=common_scales,
        y=y,
    )
    figure_rows["figure_cross_prediction.csv"] = list(cross_rows)
    if not figure_rows["figure_progress_gram_paths.csv"]:
        figure_rows["figure_progress_gram_paths.csv"] = [
            {
                "source": None,
                "case_id": None,
                "fractional_loss_progress": None,
                "depth_index": None,
                "depth_fraction": None,
                "gram_increment_fro": None,
                "progress_path_scale": None,
                "terminal_loss_reduction_fraction": None,
                "valid": False,
            }
        ]

    provenance = {
        "analysis_source": os.fspath(Path(__file__).resolve()),
        "analysis_source_sha256": _sha256(Path(__file__).resolve()),
        "protocol_path": os.fspath(protocol_path),
        "protocol_sha256": _sha256(protocol_path),
        "cases_path": os.fspath(cases_path),
        "cases_sha256": _sha256(cases_path),
        "pde_seal_path": os.fspath(pde_seal_path),
        "pde_seal_sha256": _sha256(pde_seal_path),
        "dense_seal_path": os.fspath(dense_seal_path),
        "dense_seal_sha256": _sha256(dense_seal_path),
        "dynamics_sha256": pde_seal["dynamics_sha256"],
        "pde_archives": {
            os.fspath(path.relative_to(root)): _sha256(path)
            for path in sorted(pde_paths)
        },
        "dense_archives": {
            os.fspath(path.relative_to(root)): _sha256(path)
            for path in sorted(dense_paths)
        },
    }
    summary: dict[str, Any] = {
        "schema_version": 1,
        "study": "activation-linearity smoking gun",
        "scientific_question": protocol["scientific_question"],
        "inference_roles": {
            "confirmatory_case": "C2",
            "descriptive_dose_response": "C4",
            "identity_null": "C0",
            "first_Hermite_linear_null": "L2",
        },
        "common_normalizers": {
            "formula": protocol["primary_metrics"]["common_normalizers"],
            "observed": common_scales,
            "bootstrap_recomputed_per_replicate": True,
            "depth_alignment": {
                "dense_L32_to_PDE_N16": list(range(0, 33, 2)),
                "dense_L64_to_PDE_N16": list(range(0, 65, 4)),
            },
        },
        "cross_prediction_matrix": cross,
        "activation_evidence": activation,
        "linear_null_evidence": linear_null,
        "loss_progress_evidence": progress,
        "bootstrap": {
            "replicates": replicates,
            "seed": bootstrap_seed,
            "resampling": protocol["bootstrap"]["resampling"],
            "interval": protocol["bootstrap"]["interval"],
            "primary_count_matrix_sha256": _array_sha256(primary_counts),
            "primary_common_seed_ids": dense_primary["C0"].seeds.tolist(),
            "bounds": bounds,
            "diagnostics": bootstrap_diagnostics,
        },
        "pde_numerical_controls": numerical,
        "finite_depth_width_controls": controls,
        "plateau_reporting": plateau,
        "decision": decision,
        "provenance": provenance,
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    metrics_path = output_dir / "metrics.csv"
    summary_path = output_dir / "summary.json"
    _atomic_csv(metrics_path, _to_builtin(metrics_rows))
    for name, rows in figure_rows.items():
        _atomic_csv(output_dir / name, _to_builtin(rows))
    summary["deliverables"] = {
        "summary": os.fspath(summary_path),
        "metrics": os.fspath(metrics_path),
        "figure_csvs": [
            os.fspath(output_dir / name) for name in sorted(figure_rows)
        ],
    }
    _atomic_text(
        summary_path,
        json.dumps(
            _to_builtin(summary),
            indent=2,
            sort_keys=True,
            allow_nan=False,
        )
        + "\n",
    )
    return summary


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze the frozen activation-linearity experiment"
    )
    parser.add_argument("--root", default=os.fspath(ROOT))
    parser.add_argument(
        "--protocol",
        default=os.fspath(ROOT / "protocol" / "preregistered_protocol.json"),
    )
    parser.add_argument(
        "--cases",
        default=os.fspath(ROOT / "protocol" / "cases.json"),
    )
    parser.add_argument(
        "--pde-dir",
        default=os.fspath(ROOT / "results" / "pde"),
    )
    parser.add_argument(
        "--dense-dir",
        default=os.fspath(ROOT / "results" / "dense"),
    )
    parser.add_argument(
        "--output-dir",
        default=os.fspath(ROOT / "results" / "processed"),
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    summary = run_analysis(parse_args(argv))
    print(
        json.dumps(
            {
                "status": summary["decision"]["status"],
                "summary": summary["deliverables"]["summary"],
                "metrics": summary["deliverables"]["metrics"],
                "figure_csv_count": len(
                    summary["deliverables"]["figure_csvs"]
                ),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
