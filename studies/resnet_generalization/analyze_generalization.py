#!/usr/bin/env python3
"""Preregistered analysis for the sparse P=5 PDE generalization study.

Archives are selected exclusively from their embedded metadata.  Filenames
are never used to select a case, seed block, or numerical configuration.
The analysis refuses an incomplete/different PDE seal, duplicate seeds,
unexpected archives, and any departure from the frozen case/tier schedule.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import sys
from typing import Any, Iterable, Mapping, Sequence

import matplotlib

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-analyze-generalization")
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, os.fspath(ROOT / "src"))

from study_cases import StudyCase, load_case  # noqa: E402
from study_metrics import (  # noqa: E402
    DenseEnsemble,
    Trajectory,
    align_dense_depth,
    bootstrap_comparison_metrics,
    comparison_metrics,
    observed_primary_metrics,
    stitch_pde_segments,
)

PRIMARY_NAMES = ("gram_error", "output_error", "loss_error")
BOOTSTRAP_KEYS = {
    "gram_error": "gram_increment_normalized_sup",
    "output_error": "output_increment_normalized_sup",
    "loss_error": "loss_of_ensemble_mean_normalized_sup",
}
ALLOWED_ARCHIVE_DIRS = {
    "pde_primary",
    "pde_scramble",
    "pde_audits",
    "pde_fallback",
    "dense_screen",
    "dense_confirm",
    "dense_depth",
}


class AnalysisIntegrityError(RuntimeError):
    """The evidence does not match the preregistered study."""


@dataclass(frozen=True)
class Descriptor:
    path: Path
    metadata: Mapping[str, Any]


@dataclass(frozen=True)
class DenseBlock:
    path: Path
    ensemble: DenseEnsemble
    seeds: np.ndarray
    metadata: Mapping[str, Any]


@dataclass(frozen=True)
class CombinedDense:
    ensemble: DenseEnsemble
    blocks: tuple[DenseBlock, ...]
    seeds: np.ndarray


def sha256_file(path: Path) -> str:
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
        raise AnalysisIntegrityError(f"{path} is not a JSON object")
    return value


def _metadata(path: Path) -> dict[str, Any]:
    try:
        with np.load(path, allow_pickle=False) as archive:
            if "metadata_json" not in archive.files:
                raise AnalysisIntegrityError(f"{path}: missing metadata_json")
            raw = archive["metadata_json"]
            if raw.shape != ():
                raise AnalysisIntegrityError(f"{path}: metadata_json is not scalar")
            value = json.loads(str(raw))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        if isinstance(error, AnalysisIntegrityError):
            raise
        raise AnalysisIntegrityError(f"cannot read archive metadata {path}") from error
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
    return bool(left == right)


def require_metadata(
    metadata: Mapping[str, Any],
    expected: Mapping[str, Any],
    *,
    label: str,
) -> None:
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
        "case_family": case.family,
        "case_scope": case.scope,
        "case_description": case.description,
        "X": case.X.tolist(),
        "y": case.y.tolist(),
        "m": int(case.y.size),
        "d": int(case.X.shape[0]),
        "activation": case.activation,
        "sigma_w": case.sigma_w,
        "A": case.A,
        "gamma": case.gamma,
    }


def _canonical_hash(value: Mapping[str, Any]) -> str:
    blob = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(blob.encode()).hexdigest()


def _validate_dense_config_hash(meta: Mapping[str, Any], label: str) -> None:
    fields = (
        "case_sha256",
        "registry_sha256",
        "n",
        "depth",
        "seed_start",
        "seeds",
        "seed_ids",
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
    missing = [key for key in fields if key not in meta]
    if missing:
        raise AnalysisIntegrityError(f"{label}: missing config fields {missing}")
    observed = _canonical_hash({key: meta[key] for key in fields})
    for key in ("scientific_config_sha256", "config_sha256"):
        if meta.get(key) != observed:
            raise AnalysisIntegrityError(f"{label}: invalid {key}")


def discover_metadata_archives(directory: Path) -> list[Descriptor]:
    """Discover all archives in one evidence directory without name filtering."""

    if not directory.is_dir():
        raise AnalysisIntegrityError(f"missing evidence directory {directory}")
    descriptors: list[Descriptor] = []
    for path in sorted(directory.iterdir()):
        if not path.is_file():
            raise AnalysisIntegrityError(f"unexpected non-file in {directory}: {path}")
        if path.suffix != ".npz":
            raise AnalysisIntegrityError(f"unexpected evidence file {path}")
        descriptors.append(Descriptor(path, _metadata(path)))
    return descriptors


def _inventory_archives(results: Path) -> set[Path]:
    observed: set[Path] = set()
    if not results.is_dir():
        raise AnalysisIntegrityError(f"missing results directory {results}")
    for path in results.rglob("*"):
        if not path.is_file():
            continue
        if ".npz" not in path.name:
            continue
        if path.suffix != ".npz":
            raise AnalysisIntegrityError(f"incomplete/unexpected archive {path}")
        if path.parent.name not in ALLOWED_ARCHIVE_DIRS:
            raise AnalysisIntegrityError(f"archive in unexpected directory {path}")
        observed.add(path.resolve())
    return observed


def verify_pde_seal(
    root: Path,
    results: Path,
    protocol: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any], str]:
    seal_path = results / "PDE_STAGE_SEAL.json"
    decision_path = results / "pde_numerical_decision.json"
    if not seal_path.is_file() or not decision_path.is_file():
        raise AnalysisIntegrityError("PDE seal and numerical decision are required")
    seal = _json(seal_path)
    decision = _json(decision_path)
    dynamics = _json(root / "protocol" / "FROZEN_DYNAMICS_MANIFEST.json")
    expected_dynamics = dynamics.get("aggregate_sha256")
    if seal.get("dynamics_sha256") != expected_dynamics:
        raise AnalysisIntegrityError("PDE seal has the wrong dynamics hash")
    if decision.get("dynamics_sha256") != expected_dynamics:
        raise AnalysisIntegrityError("numerical decision has the wrong dynamics hash")
    if seal.get("run_grid_sha256") != sha256_file(root / "protocol" / "run_grid.py"):
        raise AnalysisIntegrityError("PDE seal has the wrong execution-runner hash")
    if seal.get("pde_numerical_decision_sha256") != sha256_file(decision_path):
        raise AnalysisIntegrityError("PDE seal does not cover the numerical decision")
    if decision.get("analysis_source_sha256") != sha256_file(root / "pde_precheck.py"):
        raise AnalysisIntegrityError("numerical decision has the wrong precheck hash")
    files = seal.get("files")
    if not isinstance(files, dict) or seal.get("file_count") != len(files):
        raise AnalysisIntegrityError("invalid sealed file table")
    sealed_archives: set[Path] = set()
    root_resolved = root.resolve()
    for relative, digest in files.items():
        path = (root / relative).resolve()
        if root_resolved not in path.parents:
            raise AnalysisIntegrityError("sealed path escapes project root")
        if not path.is_file() or sha256_file(path) != digest:
            raise AnalysisIntegrityError(f"sealed PDE file mismatch: {relative}")
        if path.suffix == ".npz":
            if path.parent.name not in {
                "pde_primary", "pde_scramble", "pde_audits", "pde_fallback"
            }:
                raise AnalysisIntegrityError(
                    f"sealed archive in unexpected directory: {relative}"
                )
            sealed_archives.add(path)
        elif path != decision_path.resolve():
            raise AnalysisIntegrityError(f"unexpected non-archive in PDE seal: {relative}")
    observed = {
        path
        for path in _inventory_archives(results)
        if path.parent.name.startswith("pde_")
    }
    if observed != sealed_archives:
        raise AnalysisIntegrityError(
            "PDE archive inventory differs from the immutable seal"
        )
    seal_hash = sha256_file(seal_path)
    _validate_numerical_decision(decision, protocol)
    return seal, decision, seal_hash


def verify_dense_seal(
    root: Path,
    results: Path,
    *,
    dynamics_hash: str,
    pde_seal_hash: str,
) -> tuple[dict[str, Any], str]:
    """Verify the immutable dense-evidence seal and exact archive inventory."""

    path = results / "DENSE_STAGE_SEAL.json"
    if not path.is_file():
        raise AnalysisIntegrityError("DENSE_STAGE_SEAL.json is required")
    seal = _json(path)
    require_metadata(
        seal,
        {
            "dynamics_sha256": dynamics_hash,
            "run_grid_sha256": sha256_file(root / "protocol" / "run_grid.py"),
            "pde_seal_sha256": pde_seal_hash,
        },
        label=os.fspath(path),
    )
    files = seal.get("files")
    if not isinstance(files, dict) or seal.get("file_count") != len(files):
        raise AnalysisIntegrityError("invalid dense sealed file table")
    sealed: set[Path] = set()
    root_resolved = root.resolve()
    for relative, expected in files.items():
        target = (root / relative).resolve()
        if root_resolved not in target.parents:
            raise AnalysisIntegrityError("dense sealed path escapes project root")
        if target.suffix != ".npz" or target.parent.name not in {
            "dense_screen", "dense_confirm", "dense_depth"
        }:
            raise AnalysisIntegrityError(
                f"unexpected path in dense seal: {relative}"
            )
        if not target.is_file() or sha256_file(target) != expected:
            raise AnalysisIntegrityError(f"sealed dense file mismatch: {relative}")
        sealed.add(target)
    observed = {
        item for item in _inventory_archives(results)
        if item.parent.name.startswith("dense_")
    }
    if observed != sealed:
        raise AnalysisIntegrityError(
            "dense archive inventory differs from the immutable seal"
        )
    return seal, sha256_file(path)


def _validate_numerical_decision(
    decision: Mapping[str, Any], protocol: Mapping[str, Any]
) -> None:
    cases = set(protocol["active_case_ids"])
    qmc_cases = set(protocol["numerical_audits"]["qmc_crosscheck_cases"])
    refined = set(protocol["numerical_audits"]["N32_cases"])
    expected_sets = {
        "scramble": cases,
        "identity": cases,
        "qmc": qmc_cases,
        "depth": refined,
        "time_step": set(protocol["numerical_audits"]["dt001_cases"]),
    }
    for key, expected in expected_sets.items():
        value = decision.get(key)
        if not isinstance(value, dict) or set(value) != expected:
            raise AnalysisIntegrityError(f"numerical decision has wrong {key} cases")
    fallback = decision.get("r256_required")
    if not isinstance(fallback, list) or len(fallback) != len(set(fallback)):
        raise AnalysisIntegrityError("invalid r256_required list")
    tolerance = float(protocol["numerical_audits"][
        "scramble_tolerance_fraction_of_motion"
    ])
    derived = {
        case_id
        for case_id in cases
        if max(
            float(decision["scramble"][case_id]["gram_normalized"]),
            float(decision["scramble"][case_id]["output_normalized"]),
        ) > tolerance
    }
    if set(fallback) != derived:
        raise AnalysisIntegrityError("r256_required contradicts scramble metrics")


def evaluate_numerical_gates(
    decision: Mapping[str, Any], protocol: Mapping[str, Any]
) -> dict[str, Any]:
    audits = protocol["numerical_audits"]
    scramble_tolerance = float(
        audits["scramble_tolerance_fraction_of_motion"]
    )
    refinement_tolerance = float(
        audits["time_depth_tolerance_fraction_of_motion"]
    )
    qmc_tolerance = float(audits["qmc_tolerance_fraction_of_motion"])
    fallback = set(decision["r256_required"])
    cases: dict[str, Any] = {}
    for case_id in protocol["active_case_ids"]:
        identity = decision["identity"][case_id]
        identity_pass = (
            bool(identity["finite"])
            and float(identity["loss_energy_identity_defect"])
            <= float(audits["identity_loss_defect_tolerance"])
            and float(identity["minimum_theta_eigenvalue"])
            >= float(audits["identity_minimum_eigenvalue_tolerance"])
        )
        scramble_value = max(
            float(decision["scramble"][case_id]["gram_normalized"]),
            float(decision["scramble"][case_id]["output_normalized"]),
        )
        checks: dict[str, Any] = {
            "identity": identity_pass,
            "scramble": scramble_value <= scramble_tolerance,
            "fallback_required": case_id in fallback,
        }
        if case_id in decision["qmc"]:
            checks["qmc"] = max(
                float(decision["qmc"][case_id]["gram_normalized"]),
                float(decision["qmc"][case_id]["output_normalized"]),
            ) <= qmc_tolerance
        if case_id in decision["time_step"]:
            checks["time"] = max(
                float(decision["time_step"][case_id]["gram_normalized"]),
                float(decision["time_step"][case_id]["output_normalized"]),
            ) <= refinement_tolerance
        if case_id in decision["depth"]:
            checks["depth"] = max(
                float(decision["depth"][case_id]["gram_normalized"]),
                float(decision["depth"][case_id]["output_normalized"]),
            ) <= refinement_tolerance
        required = [value for key, value in checks.items() if key != "fallback_required"]
        cases[case_id] = {
            "checks": checks,
            "pass": bool(all(required) and case_id not in fallback),
            "status": (
                "pass" if all(required) and case_id not in fallback
                else "unresolved_fallback" if case_id in fallback
                else "fail"
            ),
        }
    return {
        "cases": cases,
        "overall_pass": all(item["pass"] for item in cases.values()),
        "source": decision,
    }


def _load_pde(path: Path, case: StudyCase) -> Trajectory:
    required = {"times", "f", "grams", "theta", "metadata_json"}
    try:
        with np.load(path, allow_pickle=False) as archive:
            if not required.issubset(archive.files):
                raise AnalysisIntegrityError(f"{path}: incomplete PDE schema")
            arrays = {key: archive[key].copy() for key in required - {"metadata_json"}}
    except (OSError, ValueError) as error:
        if isinstance(error, AnalysisIntegrityError):
            raise
        raise AnalysisIntegrityError(f"cannot load PDE archive {path}") from error
    meta = _metadata(path)
    require_metadata(meta, _case_metadata(case), label=os.fspath(path))
    return Trajectory(
        arrays["times"], arrays["f"], arrays["grams"], arrays["theta"], meta
    )


def _expected_primary_metadata(
    case: StudyCase, fixed: Mapping[str, Any], start: float, end: float
) -> dict[str, Any]:
    return {
        **_case_metadata(case),
        "actual_width_independent_pde_run": True,
        "contains_dense_network_weight_matrix": False,
        "quadrature": fixed["quadrature"],
        "basis_size_P": fixed["basis_size_P"],
        "depth_nodes_N": fixed["depth_nodes_N"],
        "base_order": fixed["base_order"],
        "base_quadrature_M": fixed["base_points_M"],
        "fast_quadrature_R": fixed["fast_points_R"],
        "quadrature_seed": fixed["primary_seed"],
        "integrator": fixed["integrator"],
        "dt": fixed["dt"],
        "sample_dt": fixed["sample_dt"],
        "start_time": start,
        "end_time": end,
        "duration": end - start,
    }


def load_primary_pdes(
    descriptors: Sequence[Descriptor],
    cases: Mapping[str, StudyCase],
    protocol: Mapping[str, Any],
) -> tuple[dict[str, Trajectory], dict[str, tuple[Path, Path]]]:
    fixed = protocol["fixed_pde"]
    expected_count = 2 * len(cases)
    if len(descriptors) != expected_count:
        raise AnalysisIntegrityError(
            f"expected {expected_count} primary PDE segments, got {len(descriptors)}"
        )
    output: dict[str, Trajectory] = {}
    paths: dict[str, tuple[Path, Path]] = {}
    used: set[Path] = set()
    for case_id, case in cases.items():
        matches: list[Descriptor] = []
        for start, end in (
            (0.0, float(fixed["initial_horizon"])),
            (
                float(fixed["initial_horizon"]),
                float(fixed["plateau_confirmation_horizon"]),
            ),
        ):
            expected = _expected_primary_metadata(case, fixed, start, end)
            found = [
                item for item in descriptors
                if all(_equal(item.metadata.get(key), value) for key, value in expected.items())
            ]
            if len(found) != 1:
                raise AnalysisIntegrityError(
                    f"{case_id} {start:g}->{end:g}: expected one primary segment, "
                    f"got {len(found)}"
                )
            matches.append(found[0])
            used.add(found[0].path)
        if matches[1].metadata.get("restart_source_sha256") != sha256_file(
            matches[0].path
        ):
            raise AnalysisIntegrityError(f"{case_id}: continuation source hash mismatch")
        if matches[0].metadata.get("static_compiler_sha256") != matches[1].metadata.get(
            "static_compiler_sha256"
        ):
            raise AnalysisIntegrityError(f"{case_id}: static compiler changed at restart")
        first = _load_pde(matches[0].path, case)
        second = _load_pde(matches[1].path, case)
        output[case_id] = stitch_pde_segments((first, second))
        paths[case_id] = (matches[0].path, matches[1].path)
    if used != {item.path for item in descriptors}:
        raise AnalysisIntegrityError("unexpected/duplicate primary PDE archive")
    return output, paths


def load_fallback_diagnostics(
    *,
    results: Path,
    cases: Mapping[str, StudyCase],
    protocol: Mapping[str, Any],
    decision: Mapping[str, Any],
    primary: Mapping[str, Trajectory],
) -> dict[str, Any]:
    """Describe preregistered R=256 runs without allowing them to rescue a gate."""

    case_ids = list(decision["r256_required"])
    directory = results / "pde_fallback"
    if not case_ids:
        if directory.is_dir() and any(directory.iterdir()):
            raise AnalysisIntegrityError("unexpected files in unused PDE fallback")
        return {}
    descriptors = discover_metadata_archives(directory)
    if len(descriptors) != len(case_ids):
        raise AnalysisIntegrityError("wrong number of R=256 fallback archives")
    fixed = protocol["fixed_pde"]
    output: dict[str, Any] = {}
    used: set[Path] = set()
    for case_id in case_ids:
        case = cases[case_id]
        expected = {
            **_case_metadata(case),
            "actual_width_independent_pde_run": True,
            "contains_dense_network_weight_matrix": False,
            "quadrature": fixed["quadrature"],
            "basis_size_P": fixed["basis_size_P"],
            "depth_nodes_N": fixed["depth_nodes_N"],
            "base_order": fixed["base_order"],
            "base_quadrature_M": fixed["base_points_M"],
            "fast_quadrature_R": protocol["numerical_audits"][
                "fallback_fast_points_R"
            ],
            "quadrature_seed": fixed["primary_seed"],
            "integrator": fixed["integrator"],
            "dt": fixed["dt"],
            "sample_dt": fixed["sample_dt"],
            "start_time": 0.0,
            "end_time": fixed["initial_horizon"],
            "duration": fixed["initial_horizon"],
        }
        matches = [
            item
            for item in descriptors
            if all(
                _equal(item.metadata.get(key), value)
                for key, value in expected.items()
            )
        ]
        if len(matches) != 1:
            raise AnalysisIntegrityError(
                f"{case_id}: expected exactly one R=256 fallback"
            )
        used.add(matches[0].path)
        refined = _load_pde(matches[0].path, case)
        source = primary[case_id]
        endpoint = np.flatnonzero(
            source.times == float(fixed["initial_horizon"])
        )
        if endpoint.size != 1:
            raise AnalysisIntegrityError(
                f"{case_id}: primary t=8 endpoint is absent"
            )
        stop = int(endpoint[0]) + 1
        primary_prefix = Trajectory(
            source.times[:stop],
            source.f[:stop],
            source.grams[:stop],
            source.theta[:stop],
            source.metadata,
        )
        output[case_id] = {
            "role": "directional diagnostic only; trigger remains unresolved",
            "r256_vs_r128": _normalized_observed(
                comparison_metrics(primary_prefix, refined)
            ),
            "source": os.fspath(matches[0].path.resolve().relative_to(ROOT)),
        }
    if used != {item.path for item in descriptors}:
        raise AnalysisIntegrityError("unexpected R=256 fallback archive")
    return output


def _load_dense_block(path: Path, case: StudyCase) -> DenseBlock:
    required = {"times", "seeds", "f", "grams", "theta", "metadata_json"}
    try:
        with np.load(path, allow_pickle=False) as archive:
            if not required.issubset(archive.files):
                raise AnalysisIntegrityError(f"{path}: incomplete dense schema")
            data = {key: archive[key].copy() for key in required - {"metadata_json"}}
    except (OSError, ValueError) as error:
        if isinstance(error, AnalysisIntegrityError):
            raise
        raise AnalysisIntegrityError(f"cannot load dense archive {path}") from error
    meta = _metadata(path)
    require_metadata(meta, _case_metadata(case), label=os.fspath(path))
    _validate_dense_config_hash(meta, os.fspath(path))
    seeds = np.asarray(data["seeds"])
    if seeds.ndim != 1 or not np.issubdtype(seeds.dtype, np.integer):
        raise AnalysisIntegrityError(f"{path}: invalid seed vector")
    ensemble = DenseEnsemble(
        data["times"], data["f"], data["grams"], data["theta"], meta
    )
    if ensemble.members != seeds.size:
        raise AnalysisIntegrityError(f"{path}: seed/member mismatch")
    return DenseBlock(path, ensemble, seeds.astype(np.int64), meta)


def combine_dense_blocks(
    blocks: Sequence[DenseBlock],
    *,
    expected_seed_blocks: Sequence[Sequence[int]],
    expected_metadata: Mapping[str, Any],
) -> CombinedDense:
    """Strictly pool the preregistered blocks, in preregistered block order."""

    if len(blocks) != len(expected_seed_blocks):
        raise AnalysisIntegrityError("wrong number of dense seed blocks")
    by_start: dict[int, DenseBlock] = {}
    for block in blocks:
        start = int(block.metadata.get("seed_start", -1))
        if start in by_start:
            raise AnalysisIntegrityError("duplicate dense seed block")
        by_start[start] = block
    ordered: list[DenseBlock] = []
    all_seeds: list[np.ndarray] = []
    for seed_start, members in expected_seed_blocks:
        seed_start, members = int(seed_start), int(members)
        if seed_start not in by_start:
            raise AnalysisIntegrityError(f"missing dense seed block {seed_start}")
        block = by_start[seed_start]
        require_metadata(
            block.metadata,
            {
                **expected_metadata,
                "seed_start": seed_start,
                "seeds": members,
                "seed_ids": list(range(seed_start, seed_start + members)),
            },
            label=os.fspath(block.path),
        )
        expected_seeds = np.arange(seed_start, seed_start + members, dtype=np.int64)
        if not np.array_equal(block.seeds, expected_seeds):
            raise AnalysisIntegrityError(f"{block.path}: stored seeds are not exact")
        ordered.append(block)
        all_seeds.append(block.seeds)
    first = ordered[0].ensemble
    for block in ordered[1:]:
        if not np.array_equal(first.times, block.ensemble.times):
            raise AnalysisIntegrityError("dense block time-grid mismatch")
        if first.grams.shape[2:] != block.ensemble.grams.shape[2:]:
            raise AnalysisIntegrityError("dense block observable-shape mismatch")
    seeds = np.concatenate(all_seeds)
    if np.unique(seeds).size != seeds.size:
        raise AnalysisIntegrityError("duplicate dense seeds across blocks")
    metadata = dict(first.metadata)
    metadata.update(
        {
            "seed_start": None,
            "seeds": int(seeds.size),
            "seed_ids": seeds.tolist(),
            "source_blocks": [os.fspath(item.path) for item in ordered],
        }
    )
    combined = DenseEnsemble(
        first.times,
        np.concatenate([item.ensemble.f for item in ordered], axis=0),
        np.concatenate([item.ensemble.grams for item in ordered], axis=0),
        np.concatenate([item.ensemble.theta for item in ordered], axis=0),
        metadata,
    )
    return CombinedDense(combined, tuple(ordered), seeds)


def select_final_tier(
    case_id: str, analysis_plan: Mapping[str, Any]
) -> str:
    heldout = set(analysis_plan["final_reference_selection"]["heldout_cases"])
    return "confirmation" if case_id in heldout else "screening"


def _tier_expected_metadata(
    case: StudyCase,
    tier: Mapping[str, Any],
    seal_hash: str,
    dynamics_hash: str,
) -> dict[str, Any]:
    return {
        **_case_metadata(case),
        "n": tier["width_n"],
        "depth": tier["depth_L"],
        "duration": tier["horizon"],
        "dt": tier["dt"],
        "sample_dt": tier["sample_dt"],
        "pde_seal_sha256": seal_hash,
        "dynamics_sha256": dynamics_hash,
    }


def discover_dense_descriptors(
    results: Path,
    cases: Mapping[str, StudyCase],
    protocol: Mapping[str, Any],
    seal_hash: str,
    dynamics_hash: str,
) -> dict[str, dict[str, list[Descriptor]]]:
    """Validate the exact dense archive inventory and group only by metadata."""

    schedules = {
        "screening": (
            "dense_screen",
            protocol["active_case_ids"],
            protocol["screening_reference"],
        ),
        "confirmation": (
            "dense_confirm",
            protocol["heldout_confirmation"]["case_ids"],
            protocol["heldout_confirmation"],
        ),
        "depth": (
            "dense_depth",
            protocol["depth_diagnostic"]["case_ids"],
            protocol["depth_diagnostic"],
        ),
    }
    grouped: dict[str, dict[str, list[Descriptor]]] = {}
    for tier_name, (directory_name, case_ids, tier) in schedules.items():
        descriptors = discover_metadata_archives(results / directory_name)
        expected_total = (
            len(case_ids) * len(tier["seed_blocks"])
            if "seed_blocks" in tier
            else len(case_ids)
        )
        if len(descriptors) != expected_total:
            raise AnalysisIntegrityError(
                f"{tier_name}: expected {expected_total} archives, got "
                f"{len(descriptors)}"
            )
        grouped[tier_name] = {case_id: [] for case_id in case_ids}
        for item in descriptors:
            case_id = item.metadata.get("case_id")
            if case_id not in grouped[tier_name]:
                raise AnalysisIntegrityError(
                    f"{tier_name}: unexpected case archive {case_id!r}"
                )
            expected = _tier_expected_metadata(
                cases[case_id], tier, seal_hash, dynamics_hash
            )
            require_metadata(item.metadata, expected, label=os.fspath(item.path))
            _validate_dense_config_hash(item.metadata, os.fspath(item.path))
            grouped[tier_name][case_id].append(item)
        expected_blocks = tier.get(
            "seed_blocks", [[tier["seed_start"], tier["ensemble_members"]]]
        )
        expected_starts = sorted(int(item[0]) for item in expected_blocks)
        for case_id, items in grouped[tier_name].items():
            starts = sorted(int(item.metadata.get("seed_start", -1)) for item in items)
            if starts != expected_starts:
                raise AnalysisIntegrityError(
                    f"{tier_name}/{case_id}: wrong seed-block inventory"
                )
    return grouped


def _load_combined_tier(
    descriptors: Sequence[Descriptor],
    case: StudyCase,
    tier: Mapping[str, Any],
    seal_hash: str,
    dynamics_hash: str,
) -> CombinedDense:
    blocks = [_load_dense_block(item.path, case) for item in descriptors]
    schedule = tier.get(
        "seed_blocks", [[tier["seed_start"], tier["ensemble_members"]]]
    )
    return combine_dense_blocks(
        blocks,
        expected_seed_blocks=schedule,
        expected_metadata=_tier_expected_metadata(
            case, tier, seal_hash, dynamics_hash
        ),
    )


def stratified_paired_counts(
    protocol: Mapping[str, Any],
    *,
    replicates: int,
    seed: int = 2026072301,
) -> dict[str, np.ndarray]:
    """Common trajectory-count draws within each reference tier."""

    if replicates < 1:
        raise ValueError("replicates must be positive")
    rng = np.random.default_rng(seed)
    result: dict[str, np.ndarray] = {}
    for name, key in (
        ("screening", "screening_reference"),
        ("confirmation", "heldout_confirmation"),
    ):
        blocks = protocol[key]["seed_blocks"]
        counts = [
            rng.multinomial(
                int(members),
                np.full(int(members), 1.0 / int(members)),
                size=replicates,
            )
            for _, members in blocks
        ]
        result[name] = np.concatenate(counts, axis=1)
    return result


def joint_centered_bounds(
    observed: Mapping[str, Mapping[str, float]],
    bootstrap: Mapping[str, Mapping[str, np.ndarray]],
    *,
    confidence: float = 0.95,
) -> dict[str, Any]:
    """One-sided centered bounds joint over every case and metric."""

    if not 0.0 < confidence < 1.0:
        raise ValueError("confidence must lie in (0,1)")
    if not observed or set(observed) != set(bootstrap):
        raise ValueError("observed/bootstrap case keys differ or are empty")
    upper_rows: list[np.ndarray] = []
    lower_rows: list[np.ndarray] = []
    replicates: int | None = None
    cleaned: dict[str, dict[str, float]] = {}
    for case_id in sorted(observed):
        if set(observed[case_id]) != set(PRIMARY_NAMES):
            raise ValueError("every case must expose exactly three primary metrics")
        if set(bootstrap[case_id]) != set(PRIMARY_NAMES):
            raise ValueError("bootstrap metrics differ from primary metrics")
        cleaned[case_id] = {}
        for metric in PRIMARY_NAMES:
            estimate = float(observed[case_id][metric])
            sample = np.asarray(bootstrap[case_id][metric], dtype=float)
            if not np.isfinite(estimate) or sample.ndim != 1 or not np.all(
                np.isfinite(sample)
            ):
                raise ValueError("non-finite or malformed bootstrap input")
            if replicates is None:
                replicates = int(sample.size)
            elif sample.size != replicates:
                raise ValueError("bootstrap replicate counts differ")
            cleaned[case_id][metric] = estimate
            upper_rows.append(sample - estimate)
            lower_rows.append(estimate - sample)
    assert replicates is not None and replicates > 0
    upper_max = np.max(np.stack(upper_rows), axis=0)
    lower_max = np.max(np.stack(lower_rows), axis=0)
    upper_critical = float(
        np.quantile(upper_max, confidence, method="higher")
    )
    lower_critical = float(
        np.quantile(lower_max, confidence, method="higher")
    )
    bounds = {
        case_id: {
            metric: {
                "observed": value,
                "ucb": value + upper_critical,
                "lcb": value - lower_critical,
            }
            for metric, value in metrics.items()
        }
        for case_id, metrics in cleaned.items()
    }
    return {
        "confidence": confidence,
        "replicates": replicates,
        "quantile_method": "higher",
        "upper_critical_value": upper_critical,
        "lower_critical_value": lower_critical,
        "bounds": bounds,
    }


def gram_only_centered_ucb(
    observed: Mapping[str, Mapping[str, float]],
    bootstrap: Mapping[str, Mapping[str, np.ndarray]],
    *,
    confidence: float = 0.95,
) -> dict[str, Any]:
    """Case-simultaneous Gram-only UCB used by the frozen 2.5% rule."""

    if not observed or set(observed) != set(bootstrap):
        raise ValueError("observed/bootstrap case keys differ or are empty")
    centered = []
    estimates: dict[str, float] = {}
    replicates: int | None = None
    for case_id in sorted(observed):
        estimate = float(observed[case_id]["gram_error"])
        sample = np.asarray(bootstrap[case_id]["gram_error"], dtype=float)
        if sample.ndim != 1 or not np.all(np.isfinite(sample)):
            raise ValueError("malformed Gram bootstrap sample")
        if replicates is None:
            replicates = sample.size
        elif sample.size != replicates:
            raise ValueError("bootstrap replicate counts differ")
        estimates[case_id] = estimate
        centered.append(sample - estimate)
    critical = float(
        np.quantile(
            np.max(np.stack(centered), axis=0),
            confidence,
            method="higher",
        )
    )
    return {
        "confidence": confidence,
        "replicates": int(replicates or 0),
        "quantile_method": "higher",
        "critical_value": critical,
        "upper_bounds": {
            case_id: estimate + critical
            for case_id, estimate in estimates.items()
        },
    }


def _exact_window(times: np.ndarray, start: float, end: float) -> slice:
    left = np.flatnonzero(times == start)
    right = np.flatnonzero(times == end)
    if left.size != 1 or right.size != 1 or left[0] >= right[0]:
        raise AnalysisIntegrityError(
            f"window endpoints {start:g},{end:g} are absent/ambiguous"
        )
    return slice(int(left[0]), int(right[0]) + 1)


def normalized_plateau_window(
    trajectory: Trajectory | DenseEnsemble,
    *,
    start: float,
    end: float,
    output_scale: float,
    gram_scale: float,
    thresholds: Mapping[str, float],
) -> dict[str, Any]:
    """Preregistered, exactly normalized diagnostics on one whole window."""

    if output_scale <= 0.0 or gram_scale <= 0.0:
        raise ValueError("normalization scales must be positive")
    window = _exact_window(trajectory.times, start, end)
    y = np.asarray(trajectory.metadata["y"], dtype=float)
    if isinstance(trajectory, Trajectory):
        f = trajectory.f
        grams = trajectory.grams
        speed = -np.einsum(
            "tij,tj->ti", trajectory.theta, trajectory.f - y, optimize=True
        )
        member_p95 = None
        kind = "pde"
    else:
        f = np.mean(trajectory.f, axis=0)
        grams = np.mean(trajectory.grams, axis=0)
        member_speed = -np.einsum(
            "stij,stj->sti",
            trajectory.theta,
            trajectory.f - y,
            optimize=True,
        )
        speed = np.mean(member_speed, axis=0)
        kind = "dense"
        start_index = window.start
        end_index = window.stop - 1
        member_output = np.linalg.norm(
            trajectory.f[:, end_index] - trajectory.f[:, start_index], axis=-1
        ) / output_scale
        member_gram = np.max(
            np.linalg.norm(
                trajectory.grams[:, end_index] - trajectory.grams[:, start_index],
                axis=(-2, -1),
            ),
            axis=-1,
        ) / gram_scale
        member_p95 = float(np.quantile(np.maximum(member_output, member_gram), 0.95))
    fw = f[window]
    gw = grams[window]
    sw = speed[window]
    initial_loss = 0.5 * float(np.sum(np.square(f[0] - y)))
    loss = 0.5 * np.sum(np.square(fw - y), axis=-1)
    values = {
        "endpoint_output_drift": float(np.linalg.norm(fw[-1] - fw[0]) / output_scale),
        "endpoint_gram_drift": float(
            np.max(np.linalg.norm(gw[-1] - gw[0], axis=(-2, -1))) / gram_scale
        ),
        "output_tail_arclength": float(
            np.sum(np.linalg.norm(np.diff(fw, axis=0), axis=-1)) / output_scale
        ),
        "gram_tail_arclength": float(
            np.sum(
                np.max(
                    np.linalg.norm(np.diff(gw, axis=0), axis=(-2, -1)), axis=1
                )
            ) / gram_scale
        ),
        "analytic_output_speed": float(
            np.max(np.linalg.norm(sw, axis=-1)) / output_scale
        ),
        "loss_drift": float(
            abs(float(loss[-1] - loss[0])) / max(initial_loss, 0.1)
        ),
    }
    if member_p95 is not None:
        values["memberwise_p95"] = member_p95
    checks = {
        "endpoint_output_drift": values["endpoint_output_drift"]
        <= thresholds["endpoint_output_or_gram_drift"],
        "endpoint_gram_drift": values["endpoint_gram_drift"]
        <= thresholds["endpoint_output_or_gram_drift"],
        "output_tail_arclength": values["output_tail_arclength"]
        <= thresholds["output_or_gram_tail_arclength"],
        "gram_tail_arclength": values["gram_tail_arclength"]
        <= thresholds["output_or_gram_tail_arclength"],
        "analytic_output_speed": values["analytic_output_speed"]
        <= thresholds["analytic_output_speed"],
        "loss_drift": values["loss_drift"] <= thresholds["loss_drift"],
    }
    if member_p95 is not None:
        checks["memberwise_p95"] = member_p95 <= thresholds["memberwise_p95"]
    return {
        "kind": kind,
        "window": [start, end],
        "output_scale": output_scale,
        "gram_scale": gram_scale,
        "values": values,
        "checks": checks,
        "pass": bool(all(checks.values())),
    }


def _normalized_observed(comparison: Mapping[str, Any]) -> dict[str, float]:
    primary = observed_primary_metrics(comparison)
    return {
        name: float(primary[key]) for name, key in BOOTSTRAP_KEYS.items()
    }


def _active_gram(
    comparison: Mapping[str, Any],
    dense: DenseEnsemble,
    target: int,
    *,
    motion_floor: float,
) -> dict:
    aligned = align_dense_depth(np.mean(dense.grams, axis=0), target).values
    baseline = float(np.max(np.linalg.norm(aligned[0], axis=(-2, -1))))
    motion = float(comparison["gram_increment"]["dense_motion_sup_fro"])
    ratio = motion / baseline if baseline > 0.0 else (0.0 if motion == 0.0 else None)
    return {
        "dense_initial_gram_scale": baseline,
        "dense_motion": motion,
        "motion_ratio": ratio,
        "active": bool(ratio is not None and ratio >= motion_floor),
    }


def _feature_ratio(comparison: Mapping[str, Any]) -> float | None:
    pde = float(comparison["gram_increment"]["pde_motion_sup_fro"])
    dense = float(comparison["gram_increment"]["dense_motion_sup_fro"])
    if dense == 0.0:
        return 1.0 if pde == 0.0 else None
    return pde / dense


def _per_element_rms(
    pde: Trajectory, dense: DenseEnsemble
) -> dict[str, float]:
    """True coordinatewise RMS values, not RMS matrix/vector norms."""

    dense_mean = dense.mean_trajectory()
    dense_grams = align_dense_depth(
        dense_mean.grams, pde.grams.shape[1]
    ).values
    gram_delta = (
        (pde.grams - pde.grams[0:1])
        - (dense_grams - dense_grams[0:1])
    )
    output_delta = (
        (pde.f - pde.f[0:1])
        - (dense_mean.f - dense_mean.f[0:1])
    )
    theta_delta = pde.theta - dense_mean.theta
    return {
        "gram_increment_rms_per_entry": float(
            np.sqrt(np.mean(np.square(gram_delta)))
        ),
        "output_increment_rms_per_sample": float(
            np.sqrt(np.mean(np.square(output_delta)))
        ),
        "theta_rms_per_entry": float(
            np.sqrt(np.mean(np.square(theta_delta)))
        ),
    }


def _block_diagnostics(pde: Trajectory, combined: CombinedDense) -> dict[str, Any]:
    result: dict[str, Any] = {"blocks": {}, "leave_one_block_out": {}}
    for index, block in enumerate(combined.blocks):
        result["blocks"][str(index)] = _normalized_observed(
            comparison_metrics(pde, block.ensemble)
        )
        kept = [item for j, item in enumerate(combined.blocks) if j != index]
        if not kept:
            continue
        if len(kept) == 1:
            loo = kept[0].ensemble
        else:
            first = kept[0].ensemble
            loo = DenseEnsemble(
                first.times,
                np.concatenate([item.ensemble.f for item in kept]),
                np.concatenate([item.ensemble.grams for item in kept]),
                np.concatenate([item.ensemble.theta for item in kept]),
                first.metadata,
            )
        result["leave_one_block_out"][str(index)] = _normalized_observed(
            comparison_metrics(pde, loo)
        )
    return result


def _case_verdict(
    bounds: Mapping[str, Mapping[str, float]],
    *,
    active: bool,
    gram_only_ucb: float,
    feature_ratio: float | None,
    numerical_pass: bool,
    plateau_pass: bool,
    plateau_mismatch: bool,
    equivalence_margin: float,
    near_original_margin: float,
    material_failure_margin: float,
    feature_motion_ratio_bounds: tuple[float, float],
) -> dict[str, Any]:
    judged = ("output_error", "loss_error") + (("gram_error",) if active else ())
    all_ucb = all(
        float(bounds[name]["ucb"]) <= equivalence_margin
        for name in judged
    )
    material = any(
        float(bounds[name]["lcb"]) > material_failure_margin
        for name in judged
    )
    ratio_lower, ratio_upper = feature_motion_ratio_bounds
    ratio_failure = active and (
        feature_ratio is None
        or not (ratio_lower <= feature_ratio <= ratio_upper)
    )
    material = bool(material or ratio_failure or plateau_mismatch)
    strong = bool(all_ucb and numerical_pass and plateau_pass and not material)
    return {
        "judged_metrics": list(judged),
        "strong_transfer": strong,
        "near_original_accuracy": bool(
            active and gram_only_ucb <= near_original_margin
        ),
        "near_original_gram_only_ucb": gram_only_ucb,
        "material_counterexample": material,
        "status": (
            "material_counterexample" if material
            else "strong_transfer" if strong
            else "boundary_or_unresolved"
        ),
    }


def _atomic_bytes(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    partial = path.with_name(path.name + ".partial")
    with partial.open("wb") as handle:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(partial, path)


def _atomic_text(path: Path, text: str) -> None:
    _atomic_bytes(path, text.encode())


def _atomic_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    if not rows:
        raise ValueError("CSV rows cannot be empty")
    fields = list(rows[0])
    fields.extend(
        key
        for row in rows[1:]
        for key in row
        if key not in fields
    )
    from io import StringIO

    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=fields, extrasaction="raise")
    writer.writeheader()
    writer.writerows(rows)
    _atomic_text(path, output.getvalue())


def _atomic_figure(path: Path, figure: plt.Figure) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    partial = path.with_name(path.name + ".partial")
    figure.savefig(partial, format="png", dpi=150, bbox_inches="tight")
    with partial.open("rb+") as handle:
        os.fsync(handle.fileno())
    os.replace(partial, path)
    plt.close(figure)


def _figures(
    cases: Mapping[str, Any],
    curves: Mapping[str, Any],
    output: Path,
) -> list[str]:
    case_ids = list(cases)
    x = np.arange(len(case_ids))
    figure, axis = plt.subplots(figsize=(12, 5))
    width = 0.25
    for offset, metric in enumerate(PRIMARY_NAMES):
        axis.bar(
            x + (offset - 1) * width,
            [cases[c]["bounds"][metric]["observed"] for c in case_ids],
            width,
            label=metric.replace("_error", ""),
        )
        axis.scatter(
            x + (offset - 1) * width,
            [cases[c]["bounds"][metric]["ucb"] for c in case_ids],
            s=12,
            c="black",
        )
    axis.axhline(0.05, color="tab:green", linestyle="--", linewidth=1)
    axis.axhline(0.10, color="tab:red", linestyle=":", linewidth=1)
    axis.set_xticks(x, case_ids)
    axis.set_ylabel("normalized full-curve error (dot: joint UCB)")
    axis.legend()
    error_path = output / "all_case_errors.png"
    _atomic_figure(error_path, figure)

    def curve_grid(name: str, ylabel: str) -> Path:
        figure, axes = plt.subplots(4, 4, figsize=(13, 10), sharex=True)
        for axis, case_id in zip(axes.flat, case_ids):
            record = curves[case_id]
            axis.plot(record["times"], record[f"pde_{name}"], label="PDE")
            axis.plot(record["times"], record[f"dense_{name}"], label="dense")
            axis.set_title(case_id)
        for axis in axes.flat[len(case_ids):]:
            axis.axis("off")
        axes.flat[0].legend()
        figure.supxlabel("training time")
        figure.supylabel(ylabel)
        path = output / f"{name}_curves.png"
        _atomic_figure(path, figure)
        return path

    loss_path = curve_grid("loss", "loss of predictor")
    gram_path = curve_grid("gram_motion", "max-depth Gram increment norm")
    return [os.fspath(error_path), os.fspath(loss_path), os.fspath(gram_path)]


def _report(summary: Mapping[str, Any]) -> str:
    lines = [
        "# Fixed-P PDE generalization study",
        "",
        "This report was generated from the preregistered metadata-selected "
        "analysis. No filename-based case selection or post-hoc reference-tier "
        "selection is used.",
        "",
        "The width-independent closure is fixed at the complete degree-one "
        "Hermite basis P=5 before all references. The matrix changes labels, "
        "input geometry, m=2 through 5, and two smooth bounded slope-matched "
        "activation alternatives, including two interaction cases.",
        "",
        "Only B0 and the exact-radius Y1 perturbation directly test the current "
        "narrow tanh conjecture. Every other case is extension evidence. This "
        "study does not prove the ordered width/depth limit, P-to-infinity "
        "convergence, or arbitrary-accuracy closure. In particular, the prior "
        "non-monotone P=5,15,35 observation is not revised by this fixed-P study.",
        "",
        f"- Bootstrap: B={summary['bootstrap']['replicates']}, "
        f"seed={summary['bootstrap']['seed']}, joint one-sided 95% bounds.",
        f"- Test override: `{summary['bootstrap']['test_override']}`.",
        f"- Numerical gates: `{summary['numerical_gates']['overall_pass']}`.",
        f"- Broad verdict: **{summary['broad_verdict']['status']}**.",
        "",
        "| case | tier | active Gram | Gram UCB | output UCB | loss UCB | verdict |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for case_id, record in summary["cases"].items():
        bounds = record["bounds"]
        lines.append(
            f"| {case_id} | {record['final_tier']} | "
            f"{record['active_gram']['active']} | "
            f"{bounds['gram_error']['ucb']:.5g} | "
            f"{bounds['output_error']['ucb']:.5g} | "
            f"{bounds['loss_error']['ucb']:.5g} | "
            f"{record['verdict']['status']} |"
        )
    lines += [
        "",
        "The joint critical values take a single maximum over "
        f"all {len(summary['cases'])} cases and all three normalized primary "
        "metrics. Inactive Gram cases are judged "
        "only on output and loss and do not count as Gram-transfer evidence. "
        "PDE and dense trajectories must independently pass both frozen plateau "
        "windows (8–16 and 16–32).",
        "",
        "A failed numerical gate or a common plateau failure is reported as "
        "unresolved rather than averaged away. A joint lower bound above 0.10, "
        "an active feature-motion ratio outside [0.5,2], or a plateau pass/fail "
        "mismatch is a material counterexample under the frozen rule.",
        "",
    ]
    return "\n".join(lines)


def _write_processed_seal(
    *,
    root: Path,
    results: Path,
    dynamics_hash: str,
    pde_seal_hash: str,
    dense_seal_hash: str,
    deliverables: Sequence[Path],
    bootstrap_replicates: int,
) -> None:
    root_resolved = root.resolve()
    files: dict[str, str] = {}
    for path in deliverables:
        resolved = path.resolve()
        if root_resolved not in resolved.parents or not resolved.is_file():
            raise AnalysisIntegrityError(
                f"processed deliverable is absent/outside project: {path}"
            )
        relative = os.fspath(resolved.relative_to(root_resolved))
        if relative in files:
            raise AnalysisIntegrityError("duplicate processed deliverable")
        files[relative] = sha256_file(resolved)
    record = {
        "dynamics_sha256": dynamics_hash,
        "pde_seal_sha256": pde_seal_hash,
        "dense_seal_sha256": dense_seal_hash,
        "analysis_source_sha256": sha256_file(Path(__file__)),
        "bootstrap_replicates": bootstrap_replicates,
        "bootstrap_test_override": bootstrap_replicates != 2000,
        "files": dict(sorted(files.items())),
        "file_count": len(files),
    }
    _atomic_text(
        results / "PROCESSED_STAGE_SEAL.json",
        json.dumps(record, indent=2, sort_keys=True, allow_nan=False) + "\n",
    )


def run_analysis(args: argparse.Namespace) -> dict[str, Any]:
    root = Path(args.root).resolve()
    results = Path(args.results_dir).resolve()
    output = Path(args.output_dir).resolve()
    figures_dir = Path(args.figures_dir).resolve()
    report_path = Path(args.report).resolve()
    protocol = _json(root / "protocol" / "generalization_protocol.json")
    plan = _json(root / "protocol" / "analysis_plan.json")
    registry = root / "protocol" / "cases.json"
    cases = {
        case_id: load_case(registry, case_id)
        for case_id in protocol["active_case_ids"]
    }
    if set(plan["final_reference_selection"]["heldout_cases"]) != set(
        protocol["heldout_confirmation"]["case_ids"]
    ):
        raise AnalysisIntegrityError("analysis-plan heldout tier differs from protocol")
    seal, decision, seal_hash = verify_pde_seal(root, results, protocol)
    dynamics_hash = str(seal["dynamics_sha256"])
    _, dense_seal_hash = verify_dense_seal(
        root,
        results,
        dynamics_hash=dynamics_hash,
        pde_seal_hash=seal_hash,
    )
    primary_descriptors = discover_metadata_archives(results / "pde_primary")
    pdes, pde_paths = load_primary_pdes(primary_descriptors, cases, protocol)
    fallback_diagnostics = load_fallback_diagnostics(
        results=results,
        cases=cases,
        protocol=protocol,
        decision=decision,
        primary=pdes,
    )
    dense_descriptors = discover_dense_descriptors(
        results, cases, protocol, seal_hash, dynamics_hash
    )
    counts = stratified_paired_counts(
        protocol,
        replicates=args.bootstrap_replicates,
        seed=int(plan["uncertainty"]["rng_seed"]),
    )
    numerical = evaluate_numerical_gates(decision, protocol)
    numerical["fallback_diagnostics"] = fallback_diagnostics
    observed: dict[str, dict[str, float]] = {}
    bootstrap: dict[str, dict[str, np.ndarray]] = {}
    records: dict[str, Any] = {}
    curves: dict[str, Any] = {}
    depth_diagnostics: dict[str, Any] = {}
    tier_keys = {
        "screening": "screening_reference",
        "confirmation": "heldout_confirmation",
        "depth": "depth_diagnostic",
    }
    for case_id, case in cases.items():
        tier_data: dict[str, CombinedDense] = {}
        tier_metrics: dict[str, Any] = {}
        for tier_name in ("screening", "confirmation"):
            if case_id not in dense_descriptors[tier_name]:
                continue
            combined = _load_combined_tier(
                dense_descriptors[tier_name][case_id],
                case,
                protocol[tier_keys[tier_name]],
                seal_hash,
                dynamics_hash,
            )
            tier_data[tier_name] = combined
            tier_metrics[tier_name] = {
                "comparison": _normalized_observed(
                    comparison_metrics(pdes[case_id], combined.ensemble)
                ),
                "block_diagnostics": _block_diagnostics(pdes[case_id], combined),
            }
        final_tier = select_final_tier(case_id, plan)
        final = tier_data[final_tier]
        comparison = comparison_metrics(pdes[case_id], final.ensemble)
        observed[case_id] = _normalized_observed(comparison)
        samples = bootstrap_comparison_metrics(
            pdes[case_id],
            final.ensemble,
            replicates=args.bootstrap_replicates,
            seed=int(plan["uncertainty"]["rng_seed"]),
            resample_counts=counts[final_tier],
        )
        bootstrap[case_id] = {
            name: samples.metrics[key] for name, key in BOOTSTRAP_KEYS.items()
        }
        active = _active_gram(
            comparison,
            final.ensemble,
            pdes[case_id].grams.shape[1],
            motion_floor=float(
                protocol["primary_metrics"]["nonlazy_motion_floor"]
            ),
        )
        output_scale = float(comparison["output_increment"]["denominator"])
        gram_scale = float(comparison["gram_increment"]["denominator"])
        dense_aligned = DenseEnsemble(
            final.ensemble.times,
            final.ensemble.f,
            align_dense_depth(
                final.ensemble.grams, pdes[case_id].grams.shape[1]
            ).values,
            final.ensemble.theta,
            final.ensemble.metadata,
        )
        plateau = {"pde": {}, "dense": {}}
        for start, end in plan["plateau"]["windows"]:
            key = f"{start:g}-{end:g}"
            plateau["pde"][key] = normalized_plateau_window(
                pdes[case_id],
                start=start,
                end=end,
                output_scale=output_scale,
                gram_scale=gram_scale,
                thresholds=plan["plateau"]["thresholds"],
            )
            plateau["dense"][key] = normalized_plateau_window(
                dense_aligned,
                start=start,
                end=end,
                output_scale=output_scale,
                gram_scale=gram_scale,
                thresholds=plan["plateau"]["thresholds"],
            )
        pde_plateau = all(item["pass"] for item in plateau["pde"].values())
        dense_plateau = all(item["pass"] for item in plateau["dense"].values())
        records[case_id] = {
            "family": case.family,
            "scope": case.scope,
            "final_tier": final_tier,
            "reference": {
                "n": final.ensemble.metadata["n"],
                "depth": final.ensemble.metadata["depth"],
                "members": final.ensemble.members,
                "seed_ids": final.seeds.tolist(),
            },
            "comparison": comparison,
            "secondary_errors": _per_element_rms(
                pdes[case_id], final.ensemble
            ),
            "observed": observed[case_id],
            "active_gram": active,
            "feature_motion_ratio": _feature_ratio(comparison),
            "plateau": plateau,
            "plateau_pass": pde_plateau and dense_plateau,
            "plateau_mismatch": any(
                plateau["pde"][key]["pass"] != plateau["dense"][key]["pass"]
                for key in plateau["pde"]
            ),
            "numerical_gate": numerical["cases"][case_id],
            "tier_diagnostics": tier_metrics,
            "pde_sources": [
                os.fspath(path.resolve().relative_to(root))
                for path in pde_paths[case_id]
            ],
        }
        y = case.y
        dense_mean = final.ensemble.mean_trajectory()
        dense_grams = align_dense_depth(
            dense_mean.grams, pdes[case_id].grams.shape[1]
        ).values
        curves[case_id] = {
            "times": pdes[case_id].times,
            "pde_loss": 0.5 * np.sum((pdes[case_id].f - y) ** 2, axis=-1),
            "dense_loss": 0.5 * np.sum((dense_mean.f - y) ** 2, axis=-1),
            "pde_gram_motion": np.max(
                np.linalg.norm(
                    pdes[case_id].grams - pdes[case_id].grams[0:1],
                    axis=(-2, -1),
                ),
                axis=1,
            ),
            "dense_gram_motion": np.max(
                np.linalg.norm(
                    dense_grams - dense_grams[0:1], axis=(-2, -1)
                ),
                axis=1,
            ),
        }
        if case_id in dense_descriptors["depth"]:
            depth = _load_combined_tier(
                dense_descriptors["depth"][case_id],
                case,
                protocol["depth_diagnostic"],
                seal_hash,
                dynamics_hash,
            )
            pde_depth = comparison_metrics(pdes[case_id], depth.ensemble)
            final_mean = final.ensemble.mean_trajectory()
            depth_cauchy = comparison_metrics(final_mean, depth.ensemble)
            depth_diagnostics[case_id] = {
                "pde_vs_L64": _normalized_observed(pde_depth),
                "L32_vs_L64": _normalized_observed(depth_cauchy),
                "L64_members": depth.ensemble.members,
            }
    confidence = float(protocol["primary_metrics"]["confidence"])
    bounds = joint_centered_bounds(
        observed, bootstrap, confidence=confidence
    )
    gram_bounds = gram_only_centered_ucb(
        observed, bootstrap, confidence=confidence
    )
    for case_id, record in records.items():
        record["bounds"] = bounds["bounds"][case_id]
        record["gram_only_ucb"] = gram_bounds["upper_bounds"][case_id]
        record["verdict"] = _case_verdict(
            record["bounds"],
            active=record["active_gram"]["active"],
            gram_only_ucb=record["gram_only_ucb"],
            feature_ratio=record["feature_motion_ratio"],
            numerical_pass=record["numerical_gate"]["pass"],
            plateau_pass=record["plateau_pass"],
            plateau_mismatch=record["plateau_mismatch"],
            equivalence_margin=float(
                protocol["primary_metrics"]["equivalence_margin"]
            ),
            near_original_margin=float(
                protocol["primary_metrics"]["near_original_gram_margin"]
            ),
            material_failure_margin=float(
                protocol["primary_metrics"]["material_failure_margin"]
            ),
            feature_motion_ratio_bounds=tuple(
                float(value)
                for value in protocol["primary_metrics"][
                    "feature_motion_ratio_bounds"
                ]
            ),
        )
    all_strong = all(record["verdict"]["strong_transfer"] for record in records.values())
    material = [
        case_id for case_id, record in records.items()
        if record["verdict"]["material_counterexample"]
    ]
    canonical_replicates = int(
        protocol["primary_metrics"]["bootstrap_replicates"]
    )
    test_override = args.bootstrap_replicates != canonical_replicates
    summary: dict[str, Any] = {
        "schema_version": 1,
        "provenance": {
            "dynamics_sha256": dynamics_hash,
            "pde_seal_sha256": seal_hash,
            "dense_seal_sha256": dense_seal_hash,
        },
        "analysis_plan_sha256": sha256_file(root / "protocol" / "analysis_plan.json"),
        "protocol_sha256": sha256_file(
            root / "protocol" / "generalization_protocol.json"
        ),
        "pde_seal_sha256": seal_hash,
        "decision_thresholds": protocol["primary_metrics"],
        "bootstrap": {
            "replicates": args.bootstrap_replicates,
            "default_replicates": canonical_replicates,
            "seed": int(plan["uncertainty"]["rng_seed"]),
            "stratified_blocks": True,
            "paired_common_counts_within_tier": True,
            "joint_over_cases_and_metrics": True,
            "quantile_method": "higher",
            "test_override": test_override,
        },
        "joint_bounds": {
            key: value for key, value in bounds.items() if key != "bounds"
        },
        "gram_only_bounds": {
            key: value
            for key, value in gram_bounds.items()
            if key != "upper_bounds"
        },
        "numerical_gates": numerical,
        "depth_diagnostics": depth_diagnostics,
        "cases": records,
        "broad_verdict": {
            "all_cases_strong_transfer": all_strong,
            "active_case_count": len(records),
            "material_counterexample_cases": material,
            "status": (
                "test_override_not_preregistered" if test_override
                else "broad_non_ad_hoc" if all_strong
                else "material_counterexample" if material
                else "boundary_or_unresolved"
            ),
        },
    }
    rows = []
    plateau_rows = []
    for case_id, record in records.items():
        row: dict[str, Any] = {
            "case_id": case_id,
            "family": record["family"],
            "scope": record["scope"],
            "final_tier": record["final_tier"],
            "active_gram": record["active_gram"]["active"],
            "active_gram_ratio": record["active_gram"]["motion_ratio"],
            "feature_motion_ratio": record["feature_motion_ratio"],
            "numerical_pass": record["numerical_gate"]["pass"],
            "plateau_pass": record["plateau_pass"],
            "verdict": record["verdict"]["status"],
        }
        for metric in PRIMARY_NAMES:
            row[f"{metric}_observed"] = record["bounds"][metric]["observed"]
            row[f"{metric}_ucb"] = record["bounds"][metric]["ucb"]
            row[f"{metric}_lcb"] = record["bounds"][metric]["lcb"]
        row["gram_only_case_simultaneous_ucb"] = record["gram_only_ucb"]
        row.update(record["secondary_errors"])
        rows.append(row)
        for kind in ("pde", "dense"):
            for window, item in record["plateau"][kind].items():
                plateau_rows.append(
                    {
                        "case_id": case_id,
                        "kind": kind,
                        "window": window,
                        **item["values"],
                        "pass": item["pass"],
                    }
                )
    numerical_rows = []
    for case_id in protocol["active_case_ids"]:
        numerical_rows.append(
            {
                "case_id": case_id,
                "status": numerical["cases"][case_id]["status"],
                "pass": numerical["cases"][case_id]["pass"],
                "scramble_gram_normalized": decision["scramble"][case_id][
                    "gram_normalized"
                ],
                "scramble_output_normalized": decision["scramble"][case_id][
                    "output_normalized"
                ],
                "qmc_gram_normalized": (
                    decision["qmc"][case_id]["gram_normalized"]
                    if case_id in decision["qmc"] else ""
                ),
                "qmc_output_normalized": (
                    decision["qmc"][case_id]["output_normalized"]
                    if case_id in decision["qmc"] else ""
                ),
                "time_gram_normalized": (
                    decision["time_step"][case_id]["gram_normalized"]
                    if case_id in decision["time_step"] else ""
                ),
                "time_output_normalized": (
                    decision["time_step"][case_id]["output_normalized"]
                    if case_id in decision["time_step"] else ""
                ),
                "depth_gram_normalized": (
                    decision["depth"][case_id]["gram_normalized"]
                    if case_id in decision["depth"] else ""
                ),
                "depth_output_normalized": (
                    decision["depth"][case_id]["output_normalized"]
                    if case_id in decision["depth"] else ""
                ),
                "identity_defect": decision["identity"][case_id][
                    "loss_energy_identity_defect"
                ],
                "minimum_theta_eigenvalue": decision["identity"][case_id][
                    "minimum_theta_eigenvalue"
                ],
                "fallback_r256_gram_vs_r128": (
                    fallback_diagnostics[case_id]["r256_vs_r128"][
                        "gram_error"
                    ]
                    if case_id in fallback_diagnostics else ""
                ),
                "fallback_r256_output_vs_r128": (
                    fallback_diagnostics[case_id]["r256_vs_r128"][
                        "output_error"
                    ]
                    if case_id in fallback_diagnostics else ""
                ),
            }
        )
    figure_paths = _figures(records, curves, figures_dir)
    summary["figures"] = [
        os.fspath(Path(path).resolve().relative_to(root))
        for path in figure_paths
    ]
    encoded = json.dumps(summary, indent=2, sort_keys=True, allow_nan=False) + "\n"
    _atomic_text(output / "summary.json", encoded)
    _atomic_csv(output / "case_metrics.csv", rows)
    _atomic_csv(output / "numerical_metrics.csv", numerical_rows)
    _atomic_csv(output / "plateau_metrics.csv", plateau_rows)
    _atomic_text(report_path, _report(summary))
    _write_processed_seal(
        root=root,
        results=results,
        dynamics_hash=dynamics_hash,
        pde_seal_hash=seal_hash,
        dense_seal_hash=dense_seal_hash,
        bootstrap_replicates=args.bootstrap_replicates,
        deliverables=(
            output / "summary.json",
            output / "case_metrics.csv",
            output / "numerical_metrics.csv",
            output / "plateau_metrics.csv",
            *(Path(path) for path in figure_paths),
            report_path,
        ),
    )
    return summary


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--results-dir", type=Path, default=ROOT / "results" / "generalization"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "results" / "generalization" / "processed",
    )
    parser.add_argument(
        "--figures-dir",
        type=Path,
        default=ROOT / "results" / "generalization" / "figures",
    )
    parser.add_argument(
        "--report", type=Path, default=ROOT / "REPORT.md"
    )
    parser.add_argument(
        "--bootstrap-replicates",
        type=int,
        default=2000,
        help="Preregistered default is 2000; lower values are test-only overrides.",
    )
    args = parser.parse_args(argv)
    if args.bootstrap_replicates < 1:
        parser.error("--bootstrap-replicates must be positive")
    return args


def main() -> None:
    args = parse_args()
    summary = run_analysis(args)
    print(
        json.dumps(
            {
                "summary": os.fspath(Path(args.output_dir) / "summary.json"),
                "broad_verdict": summary["broad_verdict"]["status"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
