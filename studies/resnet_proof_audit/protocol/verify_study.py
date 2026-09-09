#!/usr/bin/env python3
"""Verify frozen inputs and every completed scientific archive fail-closed."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys
from typing import Any, Mapping

import numpy as np
import scipy


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
SEAL = ROOT / "results" / "seals" / "FROZEN_INPUTS.json"
PROTOCOL_LABEL = "protocol/preregistered_protocol.json"
SOURCE = ROOT / "source"
if str(SOURCE) not in sys.path:
    sys.path.insert(0, str(SOURCE))

from analyze_study import load_sealed_stage_archive  # noqa: E402


MANIFEST_KEYS = {
    "schema_version",
    "status",
    "protocol_sha256",
    "source_tree_sha256",
    "files",
    "environment",
    "scientific_evidence_count_at_freeze",
    "notes",
}
BASE_SOURCE_LABELS = {
    "canonical_pde": (
        "activation_linearity_smoking_gun/source/src/"
        "dense_pde/operator_galerkin.py"
    ),
    "canonical_dense": (
        "activation_linearity_smoking_gun/source/src/"
        "dense_reference/core.py"
    ),
    "canonical_activations": (
        "activation_linearity_smoking_gun/source/src/activations.py"
    ),
    "cross_p": "source/cross_p.py",
    "dense_gates": "source/dense_gates.py",
    "runner": "source/run_study.py",
}
STRUCTURAL_SOURCE_LABELS = {
    "structural_runner": "source/structural_runner.py",
    "pde_tangent": "source/pde_tangent.py",
}
RUN_STUDY_STAGES = {"numerics", "scaling", "homogenization", "attack"}
STRUCTURAL_STAGES = {"generator", "gain", "tail_pde", "tail_dense"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _is_sha256(value: Any) -> bool:
    if not isinstance(value, str) or len(value) != 64:
        return False
    try:
        int(value, 16)
    except ValueError:
        return False
    return True


def _reject_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_json_text(text: str) -> Any:
    return json.loads(text, object_pairs_hook=_reject_duplicate_pairs)


def live_environment() -> dict[str, str]:
    return {
        "python": sys.version,
        "platform": platform.platform(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
    }


def resolve(label: str) -> Path:
    relative = Path(label)
    if (
        not label
        or relative.is_absolute()
        or ".." in relative.parts
        or "." in relative.parts
    ):
        raise ValueError(f"unsafe frozen source label: {label!r}")
    candidates = [
        path
        for path in (ROOT / relative, WORKSPACE / relative)
        if path.is_file()
    ]
    if len(candidates) != 1:
        if not candidates:
            raise FileNotFoundError(f"missing frozen file: {label}")
        raise ValueError(f"ambiguous frozen source label: {label}")
    return candidates[0]


def validate_manifest(seal: Mapping[str, Any]) -> dict[str, str]:
    """Validate the manifest itself and recompute its exact frozen tree."""

    if (
        not isinstance(seal, Mapping)
        or set(seal) != MANIFEST_KEYS
        or seal.get("schema_version") != 1
        or seal.get("status")
        != "frozen_before_new_scientific_trajectories"
    ):
        raise ValueError("freeze manifest has invalid schema or status")
    if (
        not _is_sha256(seal.get("protocol_sha256"))
        or not _is_sha256(seal.get("source_tree_sha256"))
        or seal.get("scientific_evidence_count_at_freeze") != 0
        or not isinstance(seal.get("notes"), list)
        or not all(isinstance(note, str) for note in seal["notes"])
    ):
        raise ValueError("freeze manifest has malformed identity fields")
    environment = seal.get("environment")
    if (
        not isinstance(environment, Mapping)
        or set(environment) != {"python", "platform", "numpy", "scipy"}
        or not all(isinstance(value, str) for value in environment.values())
    ):
        raise ValueError("freeze manifest has malformed environment")
    if dict(environment) != live_environment():
        raise ValueError("live execution environment differs from the freeze")
    files = seal.get("files")
    if not isinstance(files, list) or not files:
        raise ValueError("freeze manifest has no source inventory")
    hashes: dict[str, str] = {}
    tree = hashlib.sha256()
    for item in files:
        if not isinstance(item, Mapping) or set(item) != {
            "path",
            "sha256",
            "size_bytes",
        }:
            raise ValueError("malformed frozen source record")
        label = item.get("path")
        expected = item.get("sha256")
        size_bytes = item.get("size_bytes")
        if (
            not isinstance(label, str)
            or not _is_sha256(expected)
            or isinstance(size_bytes, bool)
            or not isinstance(size_bytes, int)
            or size_bytes < 0
        ):
            raise ValueError("malformed frozen source identity")
        if label in hashes:
            raise ValueError(f"duplicate frozen source label: {label}")
        path = resolve(label)
        if path.stat().st_size != size_bytes:
            raise ValueError(f"size mismatch: {label}")
        actual = sha256(path)
        if actual != expected:
            raise ValueError(f"hash mismatch: {label} {actual} != {expected}")
        hashes[label] = actual
        tree.update(label.encode())
        tree.update(b"\0")
        tree.update(actual.encode())
        tree.update(b"\0")
    if tree.hexdigest() != seal["source_tree_sha256"]:
        raise ValueError("source-tree digest mismatch")
    if hashes.get(PROTOCOL_LABEL) != seal["protocol_sha256"]:
        raise ValueError("manifest protocol identity is inconsistent")
    protocol_path = ROOT / PROTOCOL_LABEL
    if not protocol_path.is_file() or sha256(protocol_path) != seal[
        "protocol_sha256"
    ]:
        raise ValueError("live protocol does not match the freeze")
    protocol = strict_json_text(protocol_path.read_text(encoding="utf-8"))
    if (
        not isinstance(protocol, Mapping)
        or protocol.get("schema_version") != 1
        or protocol.get("status")
        != "preregistered_before_new_scientific_trajectories"
    ):
        raise ValueError("frozen protocol has invalid schema or status")
    return hashes


def expected_source_hashes(
    stage: str,
    frozen_hashes: Mapping[str, str],
) -> dict[str, str]:
    """Derive the one admissible per-run source map from frozen paths."""

    if stage in RUN_STUDY_STAGES:
        labels = dict(BASE_SOURCE_LABELS)
    elif stage in STRUCTURAL_STAGES:
        labels = {**BASE_SOURCE_LABELS, **STRUCTURAL_SOURCE_LABELS}
    else:
        raise ValueError(f"unknown scientific archive stage: {stage!r}")
    missing = [label for label in labels.values() if label not in frozen_hashes]
    if missing:
        raise ValueError(
            "freeze inventory lacks a required runtime source: "
            + ", ".join(missing)
        )
    return {key: frozen_hashes[label] for key, label in labels.items()}


def metadata_from_npz(path: Path) -> dict[str, Any]:
    with np.load(path, allow_pickle=False) as archive:
        if "metadata_json" not in archive:
            raise ValueError(f"{path} has no metadata_json")
        raw = np.asarray(archive["metadata_json"])
        if raw.shape != ():
            raise ValueError(f"{path} metadata_json is not scalar")
        text = raw.item()
        if isinstance(text, bytes):
            text = text.decode("utf-8")
        if not isinstance(text, str):
            raise ValueError(f"{path} metadata_json is not text")
        metadata = strict_json_text(text)
    if not isinstance(metadata, dict):
        raise ValueError(f"{path} metadata is not an object")
    return metadata


def verify_archive(
    path: Path,
    *,
    seal: Mapping[str, Any],
    seal_sha256: str,
    frozen_hashes: Mapping[str, str],
) -> None:
    """Validate bytes, freeze binding, environment, and exact source map."""

    raw_metadata = metadata_from_npz(path)
    stage = raw_metadata.get("stage")
    if not isinstance(stage, str):
        raise ValueError("archive stage is missing or malformed")
    expected_sources = expected_source_hashes(stage, frozen_hashes)
    archive = load_sealed_stage_archive(
        path,
        required_config_keys=(),
        required_arrays=(),
        expected_stage=stage,
        expected_protocol_sha256=str(seal["protocol_sha256"]),
        expected_source_hashes=expected_sources,
    )
    metadata = archive.metadata
    if dict(metadata.get("source_hashes", {})) != expected_sources:
        raise ValueError("archive source map is not exactly the frozen stage map")
    if metadata.get("frozen_inputs_sha256") != seal_sha256:
        raise ValueError("archive has the wrong freeze binding")
    expected_environment = dict(seal["environment"])
    if metadata.get("environment") != expected_environment:
        raise ValueError("archive environment map differs from the freeze")
    scalar_environment = {
        "python_version": expected_environment["python"],
        "platform": expected_environment["platform"],
        "numpy_version": expected_environment["numpy"],
        "scipy_version": expected_environment["scipy"],
    }
    for key, expected in scalar_environment.items():
        if metadata.get(key) != expected:
            raise ValueError(f"archive {key} differs from the freeze")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check-evidence",
        action="store_true",
        help="also validate every NPZ archive beneath results",
    )
    args = parser.parse_args()
    if not SEAL.is_file():
        raise FileNotFoundError(f"missing freeze seal: {SEAL}")
    seal = strict_json_text(SEAL.read_text(encoding="utf-8"))
    if not isinstance(seal, dict):
        raise ValueError("freeze manifest is not an object")
    errors: list[str] = []
    try:
        frozen_hashes = validate_manifest(seal)
    except Exception as exc:
        raise SystemExit(f"invalid freeze manifest: {exc}") from exc
    partials = sorted((ROOT / "results").rglob("*.partial"))
    if partials:
        errors.extend(f"partial archive: {path}" for path in partials)
    evidence_count = 0
    seal_digest = sha256(SEAL)
    if args.check_evidence:
        for path in sorted((ROOT / "results").rglob("*.npz")):
            evidence_count += 1
            try:
                verify_archive(
                    path,
                    seal=seal,
                    seal_sha256=seal_digest,
                    frozen_hashes=frozen_hashes,
                )
            except Exception as exc:
                errors.append(f"invalid sealed archive {path}: {exc}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(
        json.dumps(
            {
                "status": "verified",
                "frozen_file_count": len(seal["files"]),
                "evidence_count": evidence_count,
                "seal_sha256": seal_digest,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
