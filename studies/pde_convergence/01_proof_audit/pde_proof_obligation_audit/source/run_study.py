"""Frozen-stage runner for the PDE proof-obligation audit.

The runner is intentionally orchestration-only.  It imports the canonical
PDE and dense-network dynamics and the diagnostic helpers in ``cross_p`` and
``dense_gates``; it does not carry a second implementation of either
scientific vector field.

Every scientific invocation writes exactly one self-describing ``.npz``
archive.  Archives are resumable only by exact provenance/configuration
match.  Writes use ``.partial`` + file ``fsync`` + atomic rename.  A stale
partial file is a hard error, never evidence to be resumed or overwritten.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
from typing import Any, Iterable, Mapping, Sequence

import numpy as np
import scipy


HERE = Path(__file__).resolve().parent
AUDIT_ROOT = HERE.parent
WORKSPACE_ROOT = AUDIT_ROOT.parent
PROTOCOL_PATH = AUDIT_ROOT / "protocol" / "preregistered_protocol.json"
FROZEN_INPUTS_PATH = (
    AUDIT_ROOT / "results" / "seals" / "FROZEN_INPUTS.json"
)
CANONICAL_ROOT = (
    WORKSPACE_ROOT / "activation_linearity_smoking_gun" / "source" / "src"
)
CANONICAL_PDE_PATH = CANONICAL_ROOT / "dense_pde" / "operator_galerkin.py"
CANONICAL_DENSE_PATH = CANONICAL_ROOT / "dense_reference" / "core.py"
CANONICAL_ACTIVATIONS_PATH = CANONICAL_ROOT / "activations.py"
RUNNER_PATH = Path(__file__).resolve()

if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
if str(CANONICAL_ROOT) not in sys.path:
    sys.path.insert(0, str(CANONICAL_ROOT))

from cross_p import build_nested_quadratures  # noqa: E402
from analyze_study import (  # noqa: E402
    build_sealed_archive,
    derive_homogenization_outer_seed,
    load_sealed_stage_archive,
    validate_homogenization_archive_schema,
)
from dense_gates import (  # noqa: E402
    GaussianMaster,
    empirical_hermite_phi,
    initialize_gaussian_master,
    materialize_coupled_state,
    retained_row_coefficients,
    simulate_checkpoints,
)
from dense_pde.operator_galerkin import (  # noqa: E402
    PDESpec,
    PDEState,
    initialize as initialize_pde,
    observe,
    rk4_step,
)
from dense_reference import (  # noqa: E402
    FieldState,
    ModelSpec,
    ParamState,
    forward_adjoint,
    parameter_vector_field,
    rk4_param_step,
    tangent_kernel,
)


Array = np.ndarray
ARCHIVE_SCHEMA = 1
MASTER_LEVELS = (5, 15, 35, 70)
PRIMARY_BASE_ORDER = 5
STAGE_CODES = {
    "scaling": 101,
    "homogenization": 202,
    "attack": 303,
}


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _sha256_array(array: Array) -> str:
    contiguous = np.ascontiguousarray(array)
    digest = hashlib.sha256()
    digest.update(str(contiguous.dtype).encode("ascii"))
    digest.update(json.dumps(contiguous.shape).encode("ascii"))
    digest.update(memoryview(contiguous).cast("B"))
    return digest.hexdigest()


def _jsonable(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonable(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, float):
        if not np.isfinite(value):
            raise ValueError("metadata may not contain nonfinite floats")
        return float(value)
    return value


def _canonical_json(value: Any) -> str:
    return json.dumps(
        _jsonable(value),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    )


def _reject_duplicate_json_pairs(
    pairs: list[tuple[str, Any]],
) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON key: {key}")
        value[key] = item
    return value


def _load_json_strict(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle, object_pairs_hook=_reject_duplicate_json_pairs)


def _hash_json(value: Any) -> str:
    return hashlib.sha256(_canonical_json(value).encode("utf-8")).hexdigest()


def _is_sha256(value: Any) -> bool:
    if not isinstance(value, str) or len(value) != 64:
        return False
    try:
        int(value, 16)
    except ValueError:
        return False
    return True


def _live_environment() -> dict[str, str]:
    """Return the exact execution environment fields bound by the freeze."""

    return {
        "python": sys.version,
        "platform": platform.platform(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
    }


def _resolve_frozen_label(label: str) -> Path:
    relative = Path(label)
    if (
        not label
        or relative.is_absolute()
        or ".." in relative.parts
        or "." in relative.parts
    ):
        raise ValueError(f"unsafe frozen source label: {label!r}")
    local = AUDIT_ROOT / relative
    workspace = WORKSPACE_ROOT / relative
    candidates = [path for path in (local, workspace) if path.is_file()]
    if len(candidates) != 1:
        if not candidates:
            raise FileNotFoundError(f"missing frozen source: {label}")
        raise ValueError(f"ambiguous frozen source label: {label}")
    return candidates[0]


def _verify_frozen_source_tree(
    manifest: Mapping[str, Any],
) -> dict[str, str]:
    """Fail closed unless every file bound by the freeze is still identical."""

    expected_manifest_keys = {
        "schema_version",
        "status",
        "protocol_sha256",
        "source_tree_sha256",
        "files",
        "environment",
        "scientific_evidence_count_at_freeze",
        "notes",
    }
    if (
        set(manifest) != expected_manifest_keys
        or manifest.get("schema_version") != 1
        or manifest.get("status")
        != "frozen_before_new_scientific_trajectories"
    ):
        raise ValueError("frozen-input manifest has invalid schema or status")
    if (
        not _is_sha256(manifest.get("protocol_sha256"))
        or not _is_sha256(manifest.get("source_tree_sha256"))
        or manifest.get("scientific_evidence_count_at_freeze") != 0
        or not isinstance(manifest.get("notes"), list)
        or not all(isinstance(item, str) for item in manifest["notes"])
    ):
        raise ValueError("frozen-input manifest has malformed identity fields")
    environment = manifest.get("environment")
    if (
        not isinstance(environment, Mapping)
        or set(environment) != {"python", "platform", "numpy", "scipy"}
        or not all(isinstance(value, str) for value in environment.values())
    ):
        raise ValueError("frozen-input manifest has malformed environment")
    files = manifest.get("files")
    if not isinstance(files, list) or not files:
        raise ValueError("frozen-input manifest has no source inventory")
    tree_digest = hashlib.sha256()
    hashes_by_label: dict[str, str] = {}
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
            raise ValueError("malformed frozen source path or hash")
        if label in hashes_by_label:
            raise ValueError(f"duplicate frozen source label: {label}")
        path = _resolve_frozen_label(label)
        if path.stat().st_size != size_bytes:
            raise ValueError(f"frozen source size mismatch: {label}")
        actual = _sha256_file(path)
        if actual != expected:
            raise ValueError(f"frozen source hash mismatch: {label}")
        hashes_by_label[label] = actual
        tree_digest.update(label.encode())
        tree_digest.update(b"\0")
        tree_digest.update(actual.encode())
        tree_digest.update(b"\0")
    if tree_digest.hexdigest() != manifest.get("source_tree_sha256"):
        raise ValueError("frozen source-tree hash mismatch")
    protocol_label = "protocol/preregistered_protocol.json"
    if hashes_by_label.get(protocol_label) != manifest["protocol_sha256"]:
        raise ValueError("frozen protocol hash is absent or inconsistent")
    return hashes_by_label


def load_protocol(path: Path = PROTOCOL_PATH) -> dict[str, Any]:
    protocol = _load_json_strict(path)
    if not isinstance(protocol, dict):
        raise ValueError("protocol root must be an object")
    if protocol.get("schema_version") != 1:
        raise ValueError("unsupported protocol schema")
    if protocol["stage_0_integrity_and_numerics"]["nested_ladder"][
        "predeclared_master_levels"
    ] != list(MASTER_LEVELS):
        raise ValueError("protocol master levels disagree with the runner")
    ladder = protocol["stage_0_integrity_and_numerics"]["nested_ladder"]
    if ladder["primary_base_order"] != PRIMARY_BASE_ORDER:
        raise ValueError("protocol primary base order disagrees with the runner")
    if PRIMARY_BASE_ORDER not in ladder["base_order_ladder"]:
        raise ValueError("primary base order is absent from its declared ladder")
    base_dimension = (
        len(protocol["scope"]["canonical_model"]["X"]) + 1
    )
    expected_M_ladder = [
        int(order) ** base_dimension
        for order in ladder["base_order_ladder"]
    ]
    if ladder["M_ladder"] != expected_M_ladder:
        raise ValueError("base-order and M ladders are inconsistent")
    p70 = protocol["stage_0_integrity_and_numerics"][
        "P70_conditional_extension"
    ]
    if int(p70["M"]) != int(p70["base_order"]) ** base_dimension:
        raise ValueError("P=70 primary base order and M are inconsistent")
    if int(p70["required_upward_M"]) != (
        int(p70["required_upward_base_order"]) ** base_dimension
    ):
        raise ValueError("P=70 upward base order and M are inconsistent")
    p70_resolution = p70["numerical_resolution"]
    p70_primary = p70_resolution["primary"]
    if (
        int(p70_primary["base_order"]) != int(p70["base_order"])
        or int(p70_primary["base_order"]) ** base_dimension
        != int(p70["M"])
    ):
        raise ValueError("P=70 primary numerical-resolution schema is inconsistent")
    p70_refinements = p70_resolution[
        "one_axis_refinements_at_seed_20260723"
    ]
    upward_M = [
        item for item in p70_refinements if item["axis"] == "M"
    ]
    if (
        len(upward_M) != 1
        or int(upward_M[0]["base_order"])
        != int(p70["required_upward_base_order"])
    ):
        raise ValueError("P=70 upward M refinement is missing or inconsistent")
    expected_p70_configs = [
        {
            "base_order": int(p70_primary["base_order"]),
            "N": int(p70_primary["N"]),
            "R": int(p70_primary["R"]),
            "dt": float(p70_primary["dt"]),
            "seed": int(seed),
        }
        for seed in p70_primary["scramble_seeds"]
    ] + [
        {
            key: (
                float(item[key])
                if key == "dt"
                else int(item[key])
            )
            for key in ("base_order", "N", "R", "dt", "seed")
        }
        for item in p70_refinements
    ]
    actual_p70_configs = protocol["stage_0_integrity_and_numerics"][
        "execution_inventory"
    ]["conditional_P70_configs"]
    if actual_p70_configs != expected_p70_configs:
        raise ValueError(
            "conditional P=70 execution inventory disagrees with its "
            "numerical-resolution schema"
        )
    execution = protocol["stage_0_integrity_and_numerics"][
        "execution_inventory"
    ]
    scramble_seeds = [int(seed) for seed in ladder["scramble_seeds"]]
    expected_phase_A = [
        {
            "base_order": int(ladder["primary_base_order"]),
            "N": int(ladder["primary_N"]),
            "R": int(ladder["primary_R"]),
            "dt": float(ladder["primary_dt"]),
            "seed": seed,
        }
        for seed in scramble_seeds
    ]
    if execution["phase_A_primary_configs_per_level"] != expected_phase_A:
        raise ValueError("Stage-0 Phase-A primary inventory is inconsistent")
    expected_phase_B = [
        {
            key: (
                float(template[key])
                if key == "dt"
                else int(template[key])
            )
            for key in ("base_order", "N", "R", "dt")
        }
        | {"seed": seed}
        for template in execution["phase_B_upward_templates"]
        for seed in scramble_seeds
    ]
    if (
        execution["phase_B_conditional_upward_configs_per_level"]
        != expected_phase_B
    ):
        raise ValueError("Stage-0 Phase-B paired inventory is inconsistent")
    expected_downward = [
        {
            key: (
                float(template[key])
                if key == "dt"
                else int(template[key])
            )
            for key in ("base_order", "N", "R", "dt", "seed")
        }
        for template in execution[
            "seed0_downward_diagnostic_templates"
        ]
    ]
    if (
        execution["seed0_downward_diagnostic_configs_per_level"]
        != expected_downward
    ):
        raise ValueError("Stage-0 downward diagnostic inventory is inconsistent")
    expected_active = expected_phase_A + expected_phase_B + expected_downward
    if execution["active_configs_per_level"] != expected_active:
        raise ValueError(
            "Stage-0 active inventory disagrees with its phased schema"
        )
    for config in expected_active + expected_p70_configs:
        R = int(config["R"])
        if R <= 0 or R & (R - 1):
            raise ValueError(
                "every declared Sobol fast-quadrature size R must be a "
                "positive power of two"
            )
    stage4_resolution = protocol["stage_4_generator_consistency"][
        "numerical_resolution"
    ]
    stage5_resolution = protocol["stage_5_amplification"][
        "numerical_resolution"
    ]
    if stage4_resolution != stage5_resolution:
        raise ValueError(
            "Stage 4 and active Stage 5 must use the same structural "
            "numerical-resolution family"
        )
    if stage4_resolution["primary"] != p70_resolution["primary"]:
        raise ValueError(
            "active structural primary configuration must equal the "
            "conditional P=70 primary configuration"
        )
    active_refinements = stage4_resolution[
        "one_axis_refinements_at_seed_20260723"
    ]
    active_core = [
        item for item in active_refinements if item.get("axis") != "joint"
    ]
    active_joint = [
        item for item in active_refinements if item.get("axis") == "joint"
    ]
    expected_active_joint = {
        "axis": "joint",
        "base_order": 6,
        "N": 12,
        "R": 256,
        "dt": 0.01,
        "seed": 20260723,
    }
    if active_core != p70_refinements:
        raise ValueError(
            "the active structural primary/four-axis core must equal the "
            "conditional P=70 numerical family"
        )
    if active_joint != [expected_active_joint]:
        raise ValueError(
            "the active structural family must contain exactly its declared "
            "cofinal joint refinement"
        )
    if stage4_resolution.get("cofinal_joint_corner_certificate") is not True:
        raise ValueError(
            "the active structural family must enable its joint certificate"
        )
    if (
        p70_resolution.get("cofinal_joint_corner_certificate") is not False
        or any(item.get("axis") == "joint" for item in p70_refinements)
    ):
        raise ValueError(
            "the conditional P=70 numerical family must remain joint-free"
        )
    conditional_gain = protocol["stage_5_amplification"].get(
        "conditional_P70_extension"
    )
    if not isinstance(conditional_gain, Mapping):
        raise ValueError("conditional P=70 Stage-5 declaration is missing")
    expected_gain_inventory = {
        "primary_jobs_per_time_grid": len(
            p70_resolution["primary"]["scramble_seeds"]
        ),
        "one_axis_refinement_jobs_per_time_grid": len(p70_refinements),
        "time_grids": ["primary", "refined"],
        "jobs_total": 2
        * (
            len(p70_resolution["primary"]["scramble_seeds"])
            + len(p70_refinements)
        ),
        "joint_corner": None,
    }
    if (
        conditional_gain.get("residual_pair") != [35, 70]
        or conditional_gain.get("authorization_flag")
        != "--allow-conditional-p70"
        or conditional_gain.get("numerical_resolution_source")
        != (
            "stage_0_integrity_and_numerics.P70_conditional_extension."
            "numerical_resolution"
        )
        or conditional_gain.get("time_grid_source")
        != "stage_5_amplification.time_grids"
        or conditional_gain.get("nonlinear_amplitude_source")
        != (
            "stage_5_amplification."
            "symmetric_nonlinear_amplitude_magnitudes"
        )
        or conditional_gain.get("execution_inventory")
        != expected_gain_inventory
    ):
        raise ValueError(
            "conditional P=70 Stage-5 declaration is inconsistent"
        )
    return protocol


def _canonical_model(protocol: Mapping[str, Any]) -> dict[str, Any]:
    model = protocol["scope"]["canonical_model"]
    return {
        "X": np.asarray(model["X"], dtype=float),
        "y": np.asarray(model["y"], dtype=float),
        "activation": str(model["activation"]),
        "sigma_w": float(model["sigma_w"]),
        "A": float(model["A"]),
        "gamma": float(model["gamma"]),
    }


def _provenance(
    protocol: Mapping[str, Any],
    stage: str,
    config: Mapping[str, Any],
) -> dict[str, Any]:
    if not FROZEN_INPUTS_PATH.is_file():
        raise FileNotFoundError(
            "scientific execution is forbidden before freezing inputs: "
            f"{FROZEN_INPUTS_PATH}"
        )
    frozen_inputs = _load_json_strict(FROZEN_INPUTS_PATH)
    if not isinstance(frozen_inputs, dict):
        raise ValueError("frozen-input manifest root must be an object")
    frozen_hashes = _verify_frozen_source_tree(frozen_inputs)
    live_environment = _live_environment()
    if frozen_inputs["environment"] != live_environment:
        raise ValueError(
            "live Python/platform/NumPy/SciPy environment does not exactly "
            "match the frozen execution environment"
        )
    protocol_sha256 = _sha256_file(PROTOCOL_PATH)
    if frozen_inputs.get("protocol_sha256") != protocol_sha256:
        raise ValueError("frozen-input manifest does not bind the current protocol")
    live_protocol = _load_json_strict(PROTOCOL_PATH)
    if (
        not isinstance(live_protocol, dict)
        or live_protocol.get("schema_version") != 1
        or live_protocol.get("status")
        != "preregistered_before_new_scientific_trajectories"
    ):
        raise ValueError("live protocol has invalid schema or preregistration status")
    if _canonical_json(protocol) != _canonical_json(live_protocol):
        raise ValueError("in-memory protocol does not match the frozen protocol file")
    source_labels = {
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
    missing_labels = [
        label for label in source_labels.values() if label not in frozen_hashes
    ]
    if missing_labels:
        raise ValueError(
            "frozen inventory is missing a runtime scientific source: "
            + ", ".join(missing_labels)
        )
    source_hashes = {
        key: frozen_hashes[label] for key, label in source_labels.items()
    }
    model = _canonical_model(protocol)
    clean_config = _jsonable(config)
    clean_config["canonical_model"] = _jsonable(model)
    return {
        "schema_version": ARCHIVE_SCHEMA,
        "stage": stage,
        "sealed": True,
        "protocol_path": str(PROTOCOL_PATH.relative_to(WORKSPACE_ROOT)),
        "protocol_sha256": protocol_sha256,
        "frozen_inputs_sha256": _sha256_file(FROZEN_INPUTS_PATH),
        "source_hashes": source_hashes,
        "config": clean_config,
        "config_sha256": _hash_json(clean_config),
        "environment": live_environment,
        "python_version": live_environment["python"],
        "platform": live_environment["platform"],
        "numpy_version": live_environment["numpy"],
        "scipy_version": live_environment["scipy"],
    }


def build_output_metadata(
    provenance: Mapping[str, Any],
    arrays: Mapping[str, Array],
    scientific_detail: Mapping[str, Any],
) -> dict[str, Any]:
    """Build the exact sealed schema consumed by ``analyze_study``."""

    sealed = build_sealed_archive(
        stage=str(provenance["stage"]),
        config=provenance["config"],
        arrays=arrays,
        protocol_sha256=str(provenance["protocol_sha256"]),
        source_hashes=provenance["source_hashes"],
        schema_version=int(provenance["schema_version"]),
    )
    metadata = dict(sealed.metadata)
    for key in (
        "frozen_inputs_sha256",
        "protocol_path",
        "environment",
        "python_version",
        "platform",
        "numpy_version",
        "scipy_version",
    ):
        metadata[key] = provenance[key]
    metadata["scientific_detail"] = _jsonable(scientific_detail)
    metadata.pop("seal_sha256")
    metadata["seal_sha256"] = _hash_json(metadata)
    return metadata


def _metadata_from_archive(path: Path) -> dict[str, Any]:
    try:
        with np.load(path, allow_pickle=False) as archive:
            if "metadata_json" not in archive.files:
                raise ValueError("archive has no metadata_json")
            raw = archive["metadata_json"]
            if raw.ndim != 0:
                raise ValueError("metadata_json must be a scalar")
            metadata = json.loads(str(raw.item()))
            for key in archive.files:
                if key == "metadata_json":
                    continue
                array = archive[key]
                if array.dtype.kind in "fc" and not np.all(np.isfinite(array)):
                    raise ValueError(f"archive array {key!r} is nonfinite")
    except Exception as exc:
        raise ValueError(f"invalid existing archive {path}: {exc}") from exc
    return metadata


def _resume_existing(path: Path, expected: Mapping[str, Any]) -> str:
    """Validate the immutable provenance prefix of an existing result."""

    partial_path = Path(path).with_name(Path(path).name + ".partial")
    if partial_path.exists():
        raise FileExistsError(
            f"stale partial archive blocks resume: {partial_path}"
        )
    archive = load_sealed_stage_archive(
        path,
        required_config_keys=(),
        required_arrays=(),
        expected_stage=str(expected["stage"]),
        expected_protocol_sha256=str(expected["protocol_sha256"]),
        expected_source_hashes=expected["source_hashes"],
    )
    existing = archive.metadata
    for key, value in expected.items():
        if key not in existing or _canonical_json(existing[key]) != _canonical_json(value):
            raise FileExistsError(
                f"existing archive provenance/config mismatch at {key!r}: {path}"
            )
    if str(expected["stage"]) == "homogenization":
        config = expected["config"]
        model = config["canonical_model"]
        X = np.asarray(model["X"], dtype=float)
        y = np.asarray(model["y"], dtype=float)
        if X.ndim != 2 or y.ndim != 1 or X.shape[1] != y.size:
            raise ValueError(
                "homogenization canonical-model dimensions are inconsistent"
            )
        validate_homogenization_archive_schema(
            archive.arrays,
            widths=config["widths"],
            depths=config["depths"],
            checkpoints=config["checkpoints"],
            candidate_levels=config["candidate_levels"],
            replicas=int(config["replicas"]),
            input_dimension=X.shape[0],
            sample_count=y.size,
            outer_seed=int(config["outer_seed"]),
        )
    return "reused"


def atomic_save_npz(
    path: Path,
    arrays: Mapping[str, Any],
    metadata: Mapping[str, Any],
) -> str:
    """Atomically save or exactly resume one archive.

    Returns ``"written"`` or ``"reused"``.  Existing archives are reusable
    only if the complete canonical metadata JSON matches.  A partial file is
    never removed automatically.
    """

    path = Path(path)
    if path.suffix != ".npz":
        raise ValueError("scientific outputs must use the .npz suffix")
    path.parent.mkdir(parents=True, exist_ok=True)
    partial = path.with_name(path.name + ".partial")
    expected_json = _canonical_json(metadata)
    if partial.exists():
        raise FileExistsError(f"stale partial archive blocks execution: {partial}")
    if path.exists():
        existing = _metadata_from_archive(path)
        if _canonical_json(existing) != expected_json:
            raise FileExistsError(
                f"existing archive provenance/config mismatch: {path}"
            )
        return "reused"

    payload: dict[str, Any] = {}
    for key, value in arrays.items():
        if not key or key == "metadata_json":
            raise ValueError(f"invalid or reserved array key: {key!r}")
        array = np.asarray(value)
        if array.dtype.kind == "O":
            raise ValueError(f"object arrays are forbidden: {key}")
        if array.dtype.kind in "fc" and not np.all(np.isfinite(array)):
            raise ValueError(f"refusing to save nonfinite array: {key}")
        payload[key] = array
    payload["metadata_json"] = np.asarray(expected_json)

    try:
        with partial.open("xb") as handle:
            np.savez_compressed(handle, **payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(partial, path)
        directory_fd = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    except BaseException:
        # Leave a nonempty partial file as an explicit failure witness.
        raise
    return "written"


def _output_path(args: argparse.Namespace, stage: str, config: Mapping[str, Any]) -> Path:
    if args.output is not None:
        return Path(args.output).resolve()
    output_dir = Path(args.output_dir).resolve()
    return output_dir / stage / f"{stage}_{_hash_json(config)[:20]}.npz"


def _event_times(horizon: float, sample_dt: float) -> Array:
    if horizon < 0.0 or sample_dt <= 0.0:
        raise ValueError("invalid horizon or sample interval")
    count = int(np.floor(horizon / sample_dt + 1e-12))
    times = sample_dt * np.arange(count + 1, dtype=float)
    if times.size == 0 or not np.isclose(times[-1], horizon):
        times = np.append(times, horizon)
    times[-1] = horizon
    return np.unique(np.round(times, 14))


def available_memory_bytes() -> int | None:
    """Return Linux MemAvailable when exposed, otherwise no estimate."""

    path = Path("/proc/meminfo")
    if not path.is_file():
        return None
    for line in path.read_text(encoding="ascii").splitlines():
        if line.startswith("MemAvailable:"):
            fields = line.split()
            if len(fields) >= 2:
                return int(fields[1]) * 1024
    return None


def preflight_pde_memory(
    *,
    N: int,
    M: int,
    R: int,
    P: int,
    retained_state_equivalents: float = 0.0,
) -> int:
    """Conservatively reject a PDE job likely to be killed by the OOM killer."""

    state_bytes = int(N) * int(M) * int(R) * int(P) * 8
    # RK4 retains the primal and four state-sized stages and creates
    # combinations; fields/einsum workspaces add a conservative margin.
    estimated_peak = int(
        state_bytes * (7.5 + float(retained_state_equivalents))
        + 1024**3
    )
    available = available_memory_bytes()
    if available is not None and estimated_peak > int(0.82 * available):
        raise MemoryError(
            "PDE job fails the preflight memory guard: estimated peak "
            f"{estimated_peak / 1024**3:.2f} GiB exceeds 82% of "
            f"MemAvailable={available / 1024**3:.2f} GiB. The declared "
            "configuration remains unresolved; it is not silently omitted."
        )
    return estimated_peak


def preflight_dense_scaling_memory(
    *,
    n_grid: Sequence[int],
    L_grid: Sequence[int],
    input_dim: int,
    sample_count: int,
    horizon: float,
    sample_dt: float,
) -> int:
    """Guard one coupled dense-scaling root against memory overcommit.

    The bound retains the largest Gaussian master, ten complete parameter
    states for the RK4 state/stages/shifts/array temporaries, eight copies of
    all forward/adjoint field arrays, two copies of the accumulated observable
    archive, and a fixed 1 GiB allocator/BLAS margin.  Jobs within a root run
    serially, so smaller grid members do not add simultaneous state storage.
    """

    widths = tuple(int(value) for value in n_grid)
    depths = tuple(int(value) for value in L_grid)
    if (
        not widths
        or not depths
        or min(widths) <= 0
        or min(depths) <= 0
        or input_dim <= 0
        or sample_count <= 0
        or horizon < 0.0
        or sample_dt <= 0.0
    ):
        raise ValueError("invalid dense-scaling memory-preflight dimensions")
    n_max = max(widths)
    L_max = max(depths)
    float_bytes = np.dtype(np.float64).itemsize
    parameter_elements = (
        L_max * n_max * n_max
        + n_max * int(input_dim)
        + n_max
    )
    master_bytes = parameter_elements * float_bytes
    parameter_bytes = parameter_elements * float_bytes
    field_elements = (
        2 * (L_max + 1) * n_max * int(sample_count)
        + 3 * L_max * n_max * int(sample_count)
    )
    field_workspace_bytes = 8 * field_elements * float_bytes
    time_count = int(np.ceil(float(horizon) / float(sample_dt))) + 1
    jobs = len(widths) * len(depths)
    observable_elements = jobs * time_count * (
        int(sample_count)
        + (L_max + 1) * int(sample_count) ** 2
        + 1
    )
    observable_bytes = 2 * observable_elements * float_bytes
    estimated_peak = int(
        master_bytes
        + 10 * parameter_bytes
        + field_workspace_bytes
        + observable_bytes
        + 1024**3
    )
    available = available_memory_bytes()
    if available is not None and estimated_peak > int(0.82 * available):
        raise MemoryError(
            "dense-scaling job fails the preflight memory guard: estimated "
            f"peak {estimated_peak / 1024**3:.2f} GiB exceeds 82% of "
            f"MemAvailable={available / 1024**3:.2f} GiB. The declared tier "
            "remains unresolved; it is not silently reduced."
        )
    return estimated_peak


def _integrate_dense_observables(
    initial_state: ParamState,
    spec: ModelSpec,
    *,
    horizon: float,
    dt: float,
    sample_dt: float,
    required_times: Sequence[float] = (),
) -> dict[str, Array]:
    """Integrate a dense model while retaining observables, never states."""

    times = _event_times(horizon, sample_dt)
    if required_times:
        required = np.asarray(tuple(required_times), dtype=float)
        if (
            required.ndim != 1
            or not np.all(np.isfinite(required))
            or np.any(required < 0.0)
            or np.any(required > horizon)
        ):
            raise ValueError("required times must lie in the integration interval")
        times = np.unique(
            np.round(np.concatenate((times, required)), decimals=14)
        )
    state = ParamState(
        initial_state.B.copy(),
        initial_state.W.copy(),
        initial_state.a.copy(),
    )
    f_path: list[Array] = []
    gram_path: list[Array] = []
    loss_path: list[float] = []
    current_time = 0.0
    tolerance = 128 * np.finfo(float).eps * max(1.0, horizon)
    for target in times:
        while current_time < target - tolerance:
            step = min(dt, float(target - current_time))
            state = rk4_param_step(state, step, spec)
            current_time += step
        fields = forward_adjoint(state, spec)
        f = state.a @ fields.H[-1] / spec.n
        gram = np.einsum(
            "lnr,lns->lrs", fields.H, fields.H, optimize=True
        ) / spec.n
        f_path.append(f)
        gram_path.append(gram)
        residual = f - spec.y
        loss_path.append(float(0.5 * residual @ residual))
    return {
        "times": times,
        "f": np.stack(f_path),
        "gram": np.stack(gram_path),
        "loss": np.asarray(loss_path),
    }


def align_normalized_depth(gram: Array, common_nodes: int = 17) -> Array:
    """Piecewise-linearly align ``(time,L+1,m,m)`` Grams to normalized depth."""

    gram = np.asarray(gram, dtype=float)
    if gram.ndim != 4 or gram.shape[1] < 2:
        raise ValueError("gram must have shape (time,L+1,m,m)")
    if common_nodes < 2:
        raise ValueError("common_nodes must be at least two")
    source = np.linspace(0.0, 1.0, gram.shape[1])
    target = np.linspace(0.0, 1.0, common_nodes)
    flat = gram.transpose(0, 2, 3, 1).reshape(-1, gram.shape[1])
    aligned = np.empty((flat.shape[0], common_nodes), dtype=float)
    for row, values in enumerate(flat):
        aligned[row] = np.interp(target, source, values)
    return aligned.reshape(
        gram.shape[0], gram.shape[2], gram.shape[3], common_nodes
    ).transpose(0, 3, 1, 2)


def _derive_seed(base_seed: int, stage: str, *coordinates: int) -> int:
    entropy = [int(base_seed), STAGE_CODES[stage], *(int(x) for x in coordinates)]
    return int(np.random.SeedSequence(entropy).generate_state(1, dtype=np.uint64)[0])


def _dense_spec(
    model: Mapping[str, Any],
    *,
    n: int,
    depth: int,
    seed: int,
) -> ModelSpec:
    spec = ModelSpec(
        n=int(n),
        depth=int(depth),
        X=np.asarray(model["X"], dtype=float),
        y=np.asarray(model["y"], dtype=float),
        seed=int(seed),
        sigma_w=float(model["sigma_w"]),
        A=float(model["A"]),
        gamma=float(model["gamma"]),
        activation=str(model["activation"]),
    )
    spec.validate()
    return spec


def _run_numerics(
    protocol: Mapping[str, Any],
    config: Mapping[str, Any],
) -> tuple[dict[str, Array], dict[str, Any]]:
    ladder = protocol["stage_0_integrity_and_numerics"]["nested_ladder"]
    model = _canonical_model(protocol)
    P = int(config["P"])
    estimated_peak_bytes = preflight_pde_memory(
        N=int(config["N"]),
        M=int(config["M"]),
        R=int(config["R"]),
        P=P,
    )
    template = PDESpec(
        X=model["X"],
        y=model["y"],
        basis_size=P,
        depth_nodes=int(config["N"]),
        base_points=int(config["M"]),
        fast_points=int(config["R"]),
        quadrature_seed=int(config["seed"]),
        sigma_w=model["sigma_w"],
        A=model["A"],
        gamma=model["gamma"],
        activation=model["activation"],
    )
    family = build_nested_quadratures(
        template,
        levels=(P,),
        base_order=int(config["base_order"]),
        master_levels=MASTER_LEVELS,
    )
    spec = family.spec(P)
    quadrature = family.quadrature(P)
    state = initialize_pde(spec, quadrature)
    horizon = float(config["T"])
    dt = float(config["dt"])
    sample_times = _event_times(
        horizon, float(protocol["norms"]["time_sampling"])
    )
    declared = np.asarray(
        protocol["stage_4_generator_consistency"]["checkpoints"], dtype=float
    )
    checkpoint_times = declared[declared <= horizon + 1e-14]
    event_times = np.unique(np.concatenate((sample_times, checkpoint_times, [horizon])))
    sample_lookup = {round(float(t), 13): i for i, t in enumerate(sample_times)}

    observables: dict[str, list[Any]] = {
        "f": [],
        "loss": [],
        "grams": [],
        "theta": [],
        "theta_min": [],
        "residual_norm": [],
        "loss_dot": [],
        "projected_energy": [],
    }
    current_time = 0.0
    tolerance = 128 * np.finfo(float).eps * max(1.0, horizon)
    for target in event_times:
        while current_time < target - tolerance:
            step = min(dt, float(target - current_time))
            state = rk4_step(state, step, spec, quadrature)
            current_time += step
        key = round(float(target), 13)
        if key in sample_lookup:
            obs = observe(state, spec, quadrature)
            observables["f"].append(obs.f)
            observables["loss"].append(obs.loss)
            observables["grams"].append(obs.grams)
            observables["theta"].append(obs.theta)
            observables["theta_min"].append(obs.theta_min)
            observables["residual_norm"].append(obs.residual_norm)
            observables["loss_dot"].append(obs.loss_dot)
            observables["projected_energy"].append(obs.projected_energy)
    arrays = {
        "times": sample_times,
        "f": np.stack(observables["f"]),
        "loss": np.asarray(observables["loss"]),
        "grams": np.stack(observables["grams"]),
        "theta": np.stack(observables["theta"]),
        "theta_min": np.asarray(observables["theta_min"]),
        "residual_norm": np.asarray(observables["residual_norm"]),
        "loss_dot": np.asarray(observables["loss_dot"]),
        "projected_energy": np.stack(observables["projected_energy"]),
        "checkpoint_times": checkpoint_times,
        "quadrature_base_latent": quadrature.base_latent,
        "quadrature_base_weights": quadrature.base_weights,
        "quadrature_phi": quadrature.phi,
        "quadrature_epsilon": quadrature.epsilon,
        "quadrature_fast_weights": quadrature.fast_weights,
    }
    detail = {
        "quadrature_sha256": {
            "base_latent": _sha256_array(quadrature.base_latent),
            "phi": _sha256_array(quadrature.phi),
            "epsilon": _sha256_array(quadrature.epsilon),
            "raw_master_epsilon": _sha256_array(family.raw_epsilon),
        },
        "state_checkpoint_semantics": (
            "ordinary numerical-refinement archives are observables-only; "
            "checkpoint_times are alignment metadata and no full PDE state "
            "is retained. Stage 4 owns its stateful online diagnostics."
        ),
        "memory_preflight_estimated_peak_bytes": estimated_peak_bytes,
    }
    return arrays, detail


def _validate_numerics_config(
    protocol: Mapping[str, Any],
    args: argparse.Namespace,
) -> dict[str, Any]:
    stage0 = protocol["stage_0_integrity_and_numerics"]
    ladder = stage0["nested_ladder"]
    inventory = stage0["execution_inventory"]
    P = int(args.P)
    conditional_p70_authorized = bool(
        getattr(args, "allow_conditional_p70", False)
    )
    phase_b_authorized = bool(
        getattr(args, "allow_phase_b_refinements", False)
    )
    allowed_active = set(ladder["active_levels_before_conditional_extension"])
    if P == 70:
        if phase_b_authorized:
            raise ValueError(
                "P=70 may not set the unrelated Phase-B authorization flag"
            )
        if not conditional_p70_authorized:
            raise ValueError("P=70 requires --allow-conditional-p70")
        p70 = stage0["P70_conditional_extension"]
        p70_resolution = p70["numerical_resolution"]
        allowed_p70_base_orders = {
            int(p70_resolution["primary"]["base_order"]),
            *(
                int(item["base_order"])
                for item in p70_resolution[
                    "one_axis_refinements_at_seed_20260723"
                ]
            ),
        }
        if int(args.base_order) not in allowed_p70_base_orders:
            raise ValueError(
                "P=70 requires a preregistered conditional base order"
            )
    else:
        if conditional_p70_authorized:
            raise ValueError(
                "active P<70 numerics may not set the conditional-P70 flag"
            )
        if P not in allowed_active:
            raise ValueError(f"unsupported P={P}")
    requested = {
        "base_order": int(args.base_order),
        "N": int(args.N),
        "R": int(args.R),
        "dt": float(args.dt),
        "seed": int(args.seed),
    }
    inventory_key = (
        "conditional_P70_configs"
        if P == 70
        else "active_configs_per_level"
    )
    allowed_configs = {
        _canonical_json(candidate)
        for candidate in inventory[inventory_key]
    }
    if _canonical_json(requested) not in allowed_configs:
        raise ValueError(
            "numerics configuration is not in the preregistered sparse "
            f"execution inventory for P={P}: {requested}"
        )
    requested_key = _canonical_json(requested)
    if P == 70:
        execution_phase = "conditional_P70"
        p70_resolution = stage0["P70_conditional_extension"][
            "numerical_resolution"
        ]
        primary = p70_resolution["primary"]
        primary_keys = {
            _canonical_json(
                {
                    "base_order": primary["base_order"],
                    "N": primary["N"],
                    "R": primary["R"],
                    "dt": primary["dt"],
                    "seed": seed,
                }
            )
            for seed in primary["scramble_seeds"]
        }
        if requested_key in primary_keys:
            numerical_axis = "primary"
        else:
            matched_axes = [
                str(item["axis"])
                for item in p70_resolution[
                    "one_axis_refinements_at_seed_20260723"
                ]
                if _canonical_json(
                    {
                        key: item[key]
                        for key in ("base_order", "N", "R", "dt", "seed")
                    }
                )
                == requested_key
            ]
            if len(matched_axes) != 1:
                raise ValueError("P=70 numerical-resolution axis is ambiguous")
            numerical_axis = matched_axes[0]
    else:
        phase_A_keys = {
            _canonical_json(item)
            for item in inventory["phase_A_primary_configs_per_level"]
        }
        phase_B_keys = {
            _canonical_json(item)
            for item in inventory[
                "phase_B_conditional_upward_configs_per_level"
            ]
        }
        if requested_key in phase_A_keys:
            execution_phase = "phase_A_primary"
            numerical_axis = "primary"
        elif requested_key in phase_B_keys:
            if not phase_b_authorized:
                raise ValueError(
                    "Stage-0 Phase-B refinement requires "
                    "--allow-phase-b-refinements after the frozen Phase-A "
                    "unlock gate passes"
                )
            execution_phase = "phase_B_conditional"
            coordinate_key = {
                key: requested[key] for key in ("base_order", "N", "R", "dt")
            }
            matched_axes = [
                str(item["axis"])
                for item in inventory["phase_B_upward_templates"]
                if _canonical_json(
                    {
                        key: item[key]
                        for key in ("base_order", "N", "R", "dt")
                    }
                )
                == _canonical_json(coordinate_key)
            ]
            if len(matched_axes) != 1:
                raise ValueError("Stage-0 Phase-B axis is ambiguous")
            numerical_axis = matched_axes[0]
        else:
            execution_phase = "downward_diagnostic"
            matched_axes = [
                str(item["axis"])
                for item in inventory[
                    "seed0_downward_diagnostic_templates"
                ]
                if _canonical_json(
                    {
                        key: item[key]
                        for key in ("base_order", "N", "R", "dt", "seed")
                    }
                )
                == requested_key
            ]
            if len(matched_axes) != 1:
                raise ValueError("Stage-0 diagnostic axis is ambiguous")
            numerical_axis = matched_axes[0]
    if phase_b_authorized and execution_phase != "phase_B_conditional":
        raise ValueError(
            "the Phase-B authorization flag is valid only for an actual "
            "Phase-B configuration"
        )
    if float(args.T) != float(stage0["active_horizon"]):
        raise ValueError("numerics T must equal the preregistered active horizon")
    return {
        "P": P,
        "N": int(args.N),
        "R": int(args.R),
        "dt": float(args.dt),
        "seed": int(args.seed),
        "T": float(args.T),
        "master_levels": list(MASTER_LEVELS),
        "base_order": int(args.base_order),
        "M": int(args.base_order) ** (
            _canonical_model(protocol)["X"].shape[0] + 1
        ),
        "conditional_p70_authorized": conditional_p70_authorized,
        "phase_b_authorized": phase_b_authorized,
        "execution_phase": execution_phase,
        "numerical_axis": numerical_axis,
    }


def _run_scaling(
    protocol: Mapping[str, Any],
    config: Mapping[str, Any],
) -> tuple[dict[str, Array], dict[str, Any]]:
    model = _canonical_model(protocol)
    stage = protocol["stage_1_ordered_target"]
    n_grid = tuple(int(x) for x in config["n_grid"])
    depth_grid = tuple(int(x) for x in config["L_grid"])
    root_seed = int(config["root_seed"])
    n_max, depth_max = max(n_grid), max(depth_grid)
    live_memory_estimate = preflight_dense_scaling_memory(
        n_grid=n_grid,
        L_grid=depth_grid,
        input_dim=int(model["X"].shape[0]),
        sample_count=int(model["X"].shape[1]),
        horizon=float(config["T"]),
        sample_dt=float(config["sample_dt"]),
    )
    if live_memory_estimate != int(
        config["memory_preflight_estimated_peak_bytes"]
    ):
        raise RuntimeError("dense-scaling memory estimate changed after validation")

    # The existing helper is the single source of truth for both the RNG
    # order and the top-left/Haar materialization law.
    master = initialize_gaussian_master(
        n_max=n_max,
        depth_max=depth_max,
        input_dim=model["X"].shape[0],
        seed=root_seed,
    )
    master_hashes = {
        "B_standard": _sha256_array(master.B_standard),
        "W_standard": _sha256_array(master.W_standard),
        "a_standard": _sha256_array(master.a_standard),
    }
    jobs: list[tuple[int, int]] = [
        (n, depth) for depth in depth_grid for n in n_grid
    ]
    f_paths: list[Array] = []
    gram_paths: list[Array] = []
    loss_paths: list[Array] = []
    common_times: Array | None = None
    for n, depth in jobs:
        spec = _dense_spec(model, n=n, depth=depth, seed=root_seed)
        initial = materialize_coupled_state(master, spec)
        trajectory = _integrate_dense_observables(
            initial,
            spec,
            horizon=float(config["T"]),
            dt=float(config["dt"]),
            sample_dt=float(protocol["norms"]["time_sampling"]),
        )
        if common_times is None:
            common_times = trajectory["times"]
        elif not np.array_equal(common_times, trajectory["times"]):
            raise RuntimeError("dense trajectory time grids disagree")
        f_paths.append(trajectory["f"])
        gram_paths.append(
            align_normalized_depth(
                trajectory["gram"],
                common_nodes=int(config["common_depth_nodes"]),
            )
        )
        loss_paths.append(trajectory["loss"])
    if common_times is None:
        raise RuntimeError("empty scaling grid")
    arrays = {
        "times": common_times,
        "job_n": np.asarray([job[0] for job in jobs], dtype=np.int64),
        "job_L": np.asarray([job[1] for job in jobs], dtype=np.int64),
        "f": np.stack(f_paths),
        "gram_common_depth": np.stack(gram_paths),
        "loss": np.stack(loss_paths),
        "common_depth_s": np.linspace(
            0.0, 1.0, int(config["common_depth_nodes"])
        ),
    }
    detail = {
        "coupled_root_sha256": master_hashes,
        "coupling": stage["coupling"],
        "memory_preflight": {
            "estimated_peak_bytes": int(
                config["memory_preflight_estimated_peak_bytes"]
            ),
            "threshold_fraction_of_MemAvailable": 0.82,
            "formula": (
                "largest Gaussian master + 10 largest parameter states + "
                "8 complete forward/adjoint field workspaces + 2 observable "
                "archives + 1 GiB allocator/BLAS margin"
            ),
        },
        "depth_alignment_semantics": (
            "piecewise-linear alignment on every node of the finest selected "
            f"depth grid ({int(config['common_depth_nodes'])} nodes); no "
            "coarse fixed-node reduction"
        ),
        "storage_semantics": (
            "only sampled f/loss/normalized-depth Gram paths are retained; "
            "no dense checkpoint state is stored"
        ),
    }
    return arrays, detail


def _parse_int_grid(text: str) -> tuple[int, ...]:
    try:
        values = tuple(int(part) for part in text.split(",") if part)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("expected comma-separated integers") from exc
    if not values or tuple(sorted(set(values))) != values:
        raise argparse.ArgumentTypeError("grid must be strictly increasing")
    return values


def _validate_scaling_config(
    protocol: Mapping[str, Any],
    args: argparse.Namespace,
) -> dict[str, Any]:
    stage = protocol["stage_1_ordered_target"]
    grid_key = f"{args.tier}_grid"
    if grid_key not in ("screen_grid", "positive_grid"):
        raise ValueError("unsupported scaling tier")
    declared = stage[grid_key]
    declared_n = tuple(int(value) for value in declared["n"])
    declared_L = tuple(int(value) for value in declared["L"])
    n_grid = declared_n if args.n_grid is None else tuple(args.n_grid)
    L_grid = declared_L if args.L_grid is None else tuple(args.L_grid)
    if n_grid != declared_n or L_grid != declared_L:
        raise ValueError(
            "scaling execution requires the exact complete declared tier grid"
        )
    if any(max(L_grid) % depth for depth in L_grid):
        raise ValueError("all selected depths must divide the maximum depth")
    roots = int(declared["coupled_roots"])
    if not 0 <= args.root_index < roots:
        raise ValueError(f"root-index must be in [0,{roots})")
    if float(args.T) != float(stage["active_horizon"]):
        raise ValueError("scaling T must equal the preregistered horizon")
    if float(args.dt) != float(stage["dt"]):
        raise ValueError("scaling dt must equal the preregistered step")
    base_seed = int(protocol["error_ledger"]["bootstrap_seed"])
    root_seed = _derive_seed(
        base_seed,
        "scaling",
        0 if args.tier == "screen" else 1,
        args.root_index,
    )
    model = _canonical_model(protocol)
    memory_estimate = preflight_dense_scaling_memory(
        n_grid=n_grid,
        L_grid=L_grid,
        input_dim=int(model["X"].shape[0]),
        sample_count=int(model["X"].shape[1]),
        horizon=float(args.T),
        sample_dt=float(protocol["norms"]["time_sampling"]),
    )
    return {
        "tier": args.tier,
        "n_grid": list(n_grid),
        "L_grid": list(L_grid),
        "root_index": int(args.root_index),
        "root_seed": root_seed,
        "T": float(args.T),
        "dt": float(args.dt),
        "sample_dt": float(protocol["norms"]["time_sampling"]),
        "common_depth_nodes": max(L_grid) + 1,
        "memory_preflight_estimated_peak_bytes": int(memory_estimate),
    }


def crossfit_means(values: Array) -> Array:
    """Leave-one-replica-out means along axis zero."""

    values = np.asarray(values, dtype=float)
    if values.ndim < 1 or values.shape[0] < 2:
        raise ValueError("cross-fitting requires at least two replicas")
    return (np.sum(values, axis=0, keepdims=True) - values) / (
        values.shape[0] - 1
    )


def full_layer_covariance(innovations: Array) -> Array:
    """Component-averaged replica covariance for every layer pair.

    Input shape is ``(replica, layer, ...)``.  Centering is across replicas
    separately at each layer, and no depth interpolation or cross-depth
    pooling occurs.
    """

    innovations = np.asarray(innovations, dtype=float)
    if innovations.ndim < 3 or innovations.shape[0] < 2:
        raise ValueError("expected (replica,layer,components...) innovations")
    centered = innovations - innovations.mean(axis=0, keepdims=True)
    flat = centered.reshape(centered.shape[0], centered.shape[1], -1)
    covariance = np.einsum("rlc,rkc->lk", flat, flat, optimize=True)
    covariance /= float((flat.shape[0] - 1) * flat.shape[2])
    return covariance


def cross_replica_bias_squared(residuals: Array) -> Array:
    """Unbiased off-diagonal estimate of squared conditional mean.

    The first axis is the independent-W replica axis.  The returned array has
    one entry for every second-axis layer (or one scalar if the residual has
    no layer axis after callers insert a singleton).  No diagonal
    self-products enter the estimate.
    """

    residuals = np.asarray(residuals, dtype=float)
    if residuals.ndim < 2 or residuals.shape[0] < 2:
        raise ValueError("bias estimation requires at least two replicas")
    flat = residuals.reshape(residuals.shape[0], residuals.shape[1], -1)
    summed = flat.sum(axis=0)
    numerator = np.sum(summed * summed, axis=1) - np.sum(
        flat * flat, axis=(0, 2)
    )
    denominator = (
        residuals.shape[0]
        * (residuals.shape[0] - 1)
        * flat.shape[2]
    )
    return numerator / float(denominator)


class LayerSummaryAccumulator:
    """Online sufficient statistics for a replica-by-layer random field.

    The accumulator deliberately never retains the layer field from an
    individual replica.  It retains only

    * one depth average per replica (needed for hierarchical uncertainty),
    * the sums required for the complete layer-by-layer covariance, and
    * the two frozen half-sums required for the signed off-diagonal
      squared-mean estimator.

    This is the archive boundary for Stage 2: full dense actions and
    projected actions are transient numerical work arrays, not evidence
    payloads.
    """

    def __init__(
        self,
        *,
        replicas: int,
        layers: int,
        feature_shape: Sequence[int],
    ) -> None:
        if replicas < 2 or replicas % 2:
            raise ValueError("replicas must be an even integer at least two")
        if layers < 1:
            raise ValueError("layers must be positive")
        feature_shape = tuple(int(value) for value in feature_shape)
        if not feature_shape or any(value < 1 for value in feature_shape):
            raise ValueError("feature_shape must contain positive dimensions")
        self.replicas = int(replicas)
        self.layers = int(layers)
        self.feature_shape = feature_shape
        self.feature_count = int(np.prod(feature_shape))
        self._seen = np.zeros(replicas, dtype=bool)
        self._layer_sum = np.zeros(
            (layers, self.feature_count), dtype=float
        )
        self._layer_inner_sum = np.zeros((layers, layers), dtype=float)
        self._half_layer_sum = np.zeros(
            (2, layers, self.feature_count), dtype=float
        )
        self._depth_average = np.empty(
            (replicas, *feature_shape), dtype=float
        )

    def add(self, replica: int, values: Array) -> None:
        if not 0 <= replica < self.replicas:
            raise ValueError("replica index is outside the accumulator")
        if self._seen[replica]:
            raise ValueError("replica was added more than once")
        values = np.asarray(values, dtype=float)
        expected = (self.layers, *self.feature_shape)
        if values.shape != expected:
            raise ValueError(
                f"layer field has shape {values.shape}, expected {expected}"
            )
        if not np.all(np.isfinite(values)):
            raise ValueError("layer field contains nonfinite values")
        flat = values.reshape(self.layers, self.feature_count)
        self._layer_sum += flat
        self._layer_inner_sum += flat @ flat.T
        half = int(replica >= self.replicas // 2)
        self._half_layer_sum[half] += flat
        self._depth_average[replica] = np.mean(values, axis=0)
        self._seen[replica] = True

    def finalize(self) -> dict[str, Array]:
        if not np.all(self._seen):
            missing = np.flatnonzero(~self._seen).tolist()
            raise ValueError(f"missing replicas in layer summary: {missing}")
        centered_inner = self._layer_inner_sum - (
            self._layer_sum @ self._layer_sum.T / self.replicas
        )
        covariance = centered_inner / (
            (self.replicas - 1) * self.feature_count
        )
        # Suppress only roundoff asymmetry; do not project to the PSD cone.
        covariance = 0.5 * (covariance + covariance.T)

        half_size = self.replicas // 2
        first_layer_mean = self._half_layer_sum[0] / half_size
        second_layer_mean = self._half_layer_sum[1] / half_size
        bias_squared_by_layer = np.einsum(
            "lc,lc->l",
            first_layer_mean,
            second_layer_mean,
            optimize=True,
        ) / self.feature_count

        depth_flat = self._depth_average.reshape(
            self.replicas, self.feature_count
        )
        first_depth_mean = np.mean(depth_flat[:half_size], axis=0)
        second_depth_mean = np.mean(depth_flat[half_size:], axis=0)
        depth_average_bias_squared = np.dot(
            first_depth_mean, second_depth_mean
        ) / self.feature_count
        integrated_covariance = np.mean(covariance)
        return {
            "depth_average": self._depth_average.copy(),
            "layer_covariance": covariance,
            "integrated_covariance": np.asarray(
                integrated_covariance, dtype=float
            ),
            "bias_squared_by_layer": bias_squared_by_layer,
            "depth_average_bias_squared": np.asarray(
                depth_average_bias_squared, dtype=float
            ),
        }


def summarize_layer_replicas(values: Array) -> dict[str, Array]:
    """Reference wrapper used by tests and small synthetic diagnostics."""

    values = np.asarray(values, dtype=float)
    if values.ndim < 3:
        raise ValueError("expected (replica,layer,components...) values")
    accumulator = LayerSummaryAccumulator(
        replicas=values.shape[0],
        layers=values.shape[1],
        feature_shape=values.shape[2:],
    )
    for replica in range(values.shape[0]):
        accumulator.add(replica, values[replica])
    return accumulator.finalize()


def _orthonormal_empirical_phi(
    initialization_state: ParamState,
    basis_size: int,
    readout_scale: float,
) -> Array:
    raw = empirical_hermite_phi(
        initialization_state,
        basis_size=basis_size,
        readout_scale=readout_scale,
    )
    Q, R = np.linalg.qr(raw, mode="reduced")
    if np.min(np.abs(np.diag(R))) <= 1e-12:
        raise ValueError("empirical Hermite span is numerically rank deficient")
    return Q


def _projected_layer_actions(
    state: ParamState,
    fields: Any,
    spec: ModelSpec,
    phi: Array,
) -> tuple[Array, Array]:
    activation_module = __import__("activations", fromlist=["get_activation"])
    activation = activation_module.get_activation(spec.activation)
    forward = np.empty_like(fields.T)
    backward = np.empty_like(fields.T)
    for ell in range(spec.depth):
        coefficients = retained_row_coefficients(state.W[ell], phi)
        projected_z = coefficients @ (phi.T @ fields.H[ell])
        forward[ell] = activation.value(projected_z)
        beta = fields.D[ell] * fields.P[ell + 1]
        backward[ell] = phi @ (coefficients.T @ beta)
    return forward, backward


def _checkpoint_tag(time: float) -> str:
    return f"t{int(round(1000.0 * time)):04d}"


def _run_homogenization(
    protocol: Mapping[str, Any],
    config: Mapping[str, Any],
) -> tuple[dict[str, Array], dict[str, Any]]:
    model = _canonical_model(protocol)
    widths = tuple(int(x) for x in config["widths"])
    depths = tuple(int(x) for x in config["depths"])
    width_max = max(widths)
    depth_max = max(depths)
    replicas = int(config["replicas"])
    checkpoints = np.asarray(config["checkpoints"], dtype=float)
    candidate_levels = tuple(int(x) for x in config["candidate_levels"])
    outer_seed = int(config["outer_seed"])
    rng = np.random.default_rng(outer_seed)
    B_standard = rng.normal(size=(width_max, model["X"].shape[0]))
    a_standard = rng.normal(size=width_max)
    W_seeds = rng.integers(
        0,
        np.iinfo(np.uint64).max,
        size=replicas,
        dtype=np.uint64,
    )

    arrays: dict[str, Array] = {
        "shared_B_standard": B_standard,
        "shared_a_standard": a_standard,
        "W_replica_seeds": W_seeds,
        "checkpoints": checkpoints,
        "widths": np.asarray(widths, dtype=np.int64),
        "depths": np.asarray(depths, dtype=np.int64),
    }
    per_block: dict[
        tuple[int, int, int],
        dict[str, Any],
    ] = {}
    for width in widths:
        feature_shape = (width, model["X"].shape[0])
        for depth in depths:
            for checkpoint_index in range(checkpoints.size):
                statistics = {
                    "forward_action": LayerSummaryAccumulator(
                        replicas=replicas,
                        layers=depth,
                        feature_shape=feature_shape,
                    ),
                    "transpose_action": LayerSummaryAccumulator(
                        replicas=replicas,
                        layers=depth,
                        feature_shape=feature_shape,
                    ),
                }
                for P in candidate_levels:
                    for direction in ("forward", "transpose"):
                        residual_name = (
                            f"forward_reconstruction_residual_P{P}"
                            if direction == "forward"
                            else f"transpose_projection_residual_P{P}"
                        )
                        statistics[residual_name] = LayerSummaryAccumulator(
                            replicas=replicas,
                            layers=depth,
                            feature_shape=feature_shape,
                        )
                per_block[(width, depth, checkpoint_index)] = {
                    "terminal_H": [None] * replicas,
                    "input_P": [None] * replicas,
                    "statistics": statistics,
                }

    W_master_hashes: list[str] = []
    for replica, W_seed in enumerate(W_seeds):
        W_rng = np.random.default_rng(int(W_seed))
        W_standard = W_rng.normal(
            size=(depth_max, width_max, width_max)
        )
        W_master_hashes.append(_sha256_array(W_standard))
        master = GaussianMaster(
            seed=int(W_seed),
            n_max=width_max,
            depth_max=depth_max,
            input_dim=model["X"].shape[0],
            B_standard=B_standard,
            W_standard=W_standard,
            a_standard=a_standard,
        )
        master.validate()
        for width in widths:
            for depth in depths:
                spec = _dense_spec(
                    model, n=width, depth=depth, seed=int(W_seed)
                )
                initial = materialize_coupled_state(master, spec)
                trajectory = simulate_checkpoints(
                    initial,
                    spec,
                    checkpoints,
                    dt=float(config["dt"]),
                )
                phi_by_level = {
                    P: _orthonormal_empirical_phi(initial, P, spec.A)
                    for P in candidate_levels
                }
                for checkpoint_index, state in enumerate(trajectory.states):
                    fields = forward_adjoint(state, spec)
                    raw_forward = fields.T
                    raw_transpose = np.empty_like(raw_forward)
                    for ell in range(depth):
                        beta = fields.D[ell] * fields.P[ell + 1]
                        raw_transpose[ell] = state.W[ell].T @ beta
                    block = per_block[(width, depth, checkpoint_index)]
                    block["terminal_H"][replica] = fields.H[-1].copy()
                    block["input_P"][replica] = fields.P[0].copy()
                    block["statistics"]["forward_action"].add(
                        replica, raw_forward
                    )
                    block["statistics"]["transpose_action"].add(
                        replica, raw_transpose
                    )
                    for P, phi in phi_by_level.items():
                        projected_forward, projected_transpose = (
                            _projected_layer_actions(
                                state, fields, spec, phi
                            )
                        )
                        block["statistics"][
                            f"forward_reconstruction_residual_P{P}"
                        ].add(
                            replica, raw_forward - projected_forward
                        )
                        block["statistics"][
                            f"transpose_projection_residual_P{P}"
                        ].add(
                            replica, raw_transpose - projected_transpose
                        )

    for (
        width,
        depth,
        checkpoint_index,
    ), block in per_block.items():
        prefix = (
            f"W{width}_D{depth}_"
            f"{_checkpoint_tag(checkpoints[checkpoint_index])}"
        )
        if any(value is None for value in block["terminal_H"]):
            raise RuntimeError(f"incomplete terminal field block: {prefix}")
        if any(value is None for value in block["input_P"]):
            raise RuntimeError(f"incomplete input-adjoint block: {prefix}")
        arrays[f"{prefix}_terminal_H"] = np.stack(block["terminal_H"])
        arrays[f"{prefix}_input_P"] = np.stack(block["input_P"])
        for name, accumulator in block["statistics"].items():
            summary = accumulator.finalize()
            for statistic_name, value in summary.items():
                arrays[
                    f"{prefix}_{name}_{statistic_name}"
                ] = value

    detail = {
        "global_master": {
            "n_max": width_max,
            "L_max": depth_max,
            "width_materialization": (
                "literal B/a prefixes and top-left W prefixes, with "
                "sigma_w/sqrt(n) reapplied at each requested width"
            ),
            "depth_materialization": (
                "consecutive finest-layer block sums divided by sqrt(block); "
                "equivalently the declared recursive Haar coupling"
            ),
            "shared_B_standard_sha256": _sha256_array(B_standard),
            "shared_a_standard_sha256": _sha256_array(a_standard),
            "W_standard_sha256_by_replica": W_master_hashes,
            "W_replica_seeds": [int(value) for value in W_seeds],
        },
        "storage_semantics": (
            "No raw layer action, projected action, or layerwise residual "
            "tensor is serialized. Each archive contains only replica-level "
            "terminal/input fields and depth averages, full L-by-L covariance "
            "summaries, signed split-half bias-squared summaries, and exact "
            "master provenance."
        ),
        "covariance_semantics": (
            "full L-by-L covariance after within-layer replica centering, "
            "averaged over finite-dense neuron/sample components; its stored "
            "integrated value is the L^-2 double sum"
        ),
        "bias_semantics": (
            "replicas are frozen into halves [0,R/2) and [R/2,R); the signed "
            "inner product of half-means is stored both by layer and after "
            "depth averaging, with no diagonal self-products"
        ),
        "candidate_basis_semantics": (
            "empirical Hermite span QR-orthonormalized separately at each "
            "declared P; the same finite-width Phi is used for W Phi and "
            "Phi^T W^T"
        ),
        "candidate_residual_semantics": {
            "forward": (
                "memberwise nonlinear reconstruction defect "
                "phi(W H)-phi(W Phi Phi^T H); this is generally not "
                "orthogonal to Phi and combines finite-P reconstruction "
                "error with remaining homogenization error"
            ),
            "transpose": (
                "memberwise raw minus same-member finite-P shared-transpose "
                "candidate (I-Phi Phi^T)W^T beta; this residual is "
                "orthogonal to Phi but does not claim identification of "
                "every possible Onsager/response term"
            ),
            "bias": (
                "fixed-half off-diagonal cross-replica inner products; the "
                "by-layer statistic has no cross-depth pooling, while the "
                "depth-average statistic is the L^-2 aggregate over all "
                "layer pairs"
            ),
            "identification_boundary": (
                "finite-P residual diagnostics are not evaluations of the trained "
                "conditional/shared-transpose/Onsager mean and can never turn "
                "the actual conditional-mean gate into a pass"
            ),
        },
    }
    return arrays, detail


def _validate_homogenization_config(
    protocol: Mapping[str, Any],
    args: argparse.Namespace,
) -> dict[str, Any]:
    stage = protocol["stage_2_homogenization"]
    if not 0 <= args.outer_root_index < stage["outer_B_a_roots"]:
        raise ValueError("outer-root-index is outside the declared range")
    depths = tuple(stage["depths"]) if args.depths is None else args.depths
    if depths != tuple(stage["depths"]):
        raise ValueError(
            "every homogenization outer-root bundle must use the complete "
            "frozen depth grid"
        )
    if any(max(depths) % depth for depth in depths):
        raise ValueError("all depths must divide the selected maximum")
    if args.replicas != stage["independent_W_replicas_per_outer_root"]:
        raise ValueError("replica count is frozen by the protocol")
    if float(args.dt) != float(
        protocol["stage_1_ordered_target"]["dt"]
    ):
        raise ValueError("homogenization dt must equal the dense canonical step")
    base_seed = int(protocol["error_ledger"]["bootstrap_seed"])
    widths = tuple(int(value) for value in stage["widths"])
    if tuple(sorted(set(widths))) != widths:
        raise ValueError("homogenization widths must be strictly increasing")
    if max(widths) != int(stage["global_master"]["n_max"]):
        raise ValueError("homogenization widths disagree with global n_max")
    if max(depths) != int(stage["global_master"]["L_max"]):
        raise ValueError("selected depths must retain the frozen global L_max")
    return {
        "widths": list(widths),
        "width": int(stage["width"]),
        "depths": list(depths),
        "outer_root_index": int(args.outer_root_index),
        "outer_seed": derive_homogenization_outer_seed(
            base_seed, args.outer_root_index
        ),
        "replicas": int(args.replicas),
        "checkpoints": list(stage["checkpoints"]),
        "candidate_levels": list(stage["candidate_levels"]),
        "dt": float(args.dt),
    }


def _orthonormal_span(matrix: Array) -> Array:
    """Return a numerically rank-revealing orthonormal column span."""

    matrix = np.asarray(matrix, dtype=float)
    if matrix.ndim != 2:
        raise ValueError("span input must be a matrix")
    if matrix.shape[1] == 0:
        return np.empty((matrix.shape[0], 0), dtype=float)
    U, singular_values, _ = np.linalg.svd(matrix, full_matrices=False)
    if singular_values.size == 0:
        return np.empty((matrix.shape[0], 0), dtype=float)
    tolerance = (
        max(matrix.shape)
        * np.finfo(float).eps
        * max(1.0, float(singular_values[0]))
    )
    return U[:, singular_values > tolerance]


def _project_off(span: Array, matrix: Array) -> Array:
    projected = np.asarray(matrix, dtype=float).copy()
    if span.shape[1]:
        projected -= span @ (span.T @ projected)
        projected -= span @ (span.T @ projected)
    return projected


def random_invisible_rank_one(
    phi: Array,
    hidden: Array,
    beta: Array,
    *,
    alpha: float,
    seed: int,
) -> tuple[Array, Array, Array]:
    """Draw a deterministic random invisible rank-one perturbation."""

    phi = np.asarray(phi, dtype=float)
    hidden = np.asarray(hidden, dtype=float)
    beta = np.asarray(beta, dtype=float)
    if phi.ndim != 2 or hidden.ndim != 2 or beta.ndim != 2:
        raise ValueError("phi, hidden, and beta must be matrices")
    n = phi.shape[0]
    if hidden.shape[0] != n or beta.shape[0] != n:
        raise ValueError("constraint matrices disagree on width")
    if alpha <= 0.0 or not np.isfinite(alpha):
        raise ValueError("alpha must be positive and finite")

    right_span = _orthonormal_span(np.column_stack((phi, hidden)))
    left_span = _orthonormal_span(beta)
    rng = np.random.default_rng(seed)

    def draw(projector: Array) -> Array:
        for _ in range(16):
            vector = rng.normal(size=n)
            vector = _project_off(projector, vector)
            norm = float(np.linalg.norm(vector))
            if norm > 1e-12:
                return vector / norm
        raise ValueError("constraint span leaves no stable random direction")

    u = draw(left_span)
    v = draw(right_span)
    delta = float(alpha) * np.outer(u, v)
    return u, v, delta


def coherent_invisible_rank_one(
    phi: Array,
    hidden: Array,
    beta: Array,
    hidden_velocity: Array,
    objective_cotangent: Array,
    *,
    objective_scale: float,
    fallback_seed: int,
) -> tuple[Array, Array, Array, float, str]:
    """Optimize one layer's declared linearized dot-Gram objective.

    The local objective gradient factors as

    ``objective_scale * objective_cotangent @ hidden_velocity.T``.

    Projecting both low-rank factors off the present-state constraint spans
    leaves a matrix of rank at most the training-sample count.  A small-core
    SVD therefore returns the exact best *per-layer rank-one* direction for
    this frozen linear objective without forming or decomposing an ``n x n``
    matrix.  This is not a global optimizer of the multilayer nonlinear
    restart trajectory.
    """

    phi = np.asarray(phi, dtype=float)
    hidden = np.asarray(hidden, dtype=float)
    beta = np.asarray(beta, dtype=float)
    hidden_velocity = np.asarray(hidden_velocity, dtype=float)
    objective_cotangent = np.asarray(objective_cotangent, dtype=float)
    matrices = (phi, hidden, beta, hidden_velocity, objective_cotangent)
    if any(matrix.ndim != 2 for matrix in matrices):
        raise ValueError("coherent attack inputs must be matrices")
    n = phi.shape[0]
    if any(matrix.shape[0] != n for matrix in matrices[1:]):
        raise ValueError("coherent attack inputs disagree on width")
    if hidden_velocity.shape[1] != objective_cotangent.shape[1]:
        raise ValueError("coherent objective factors disagree on samples")
    if not np.isfinite(objective_scale) or objective_scale <= 0.0:
        raise ValueError("objective_scale must be positive and finite")

    right_span = _orthonormal_span(np.column_stack((phi, hidden)))
    left_span = _orthonormal_span(beta)
    left_factor = _project_off(left_span, objective_cotangent)
    right_factor = _project_off(right_span, hidden_velocity)

    Ua, sa, Va_t = np.linalg.svd(left_factor, full_matrices=False)
    Ub, sb, Vb_t = np.linalg.svd(right_factor, full_matrices=False)
    tolerance = max(n, hidden_velocity.shape[1]) * np.finfo(float).eps
    rank_a = int(np.count_nonzero(sa > tolerance * max(1.0, sa[0])))
    rank_b = int(np.count_nonzero(sb > tolerance * max(1.0, sb[0])))
    if rank_a == 0 or rank_b == 0:
        u, v, delta = random_invisible_rank_one(
            phi,
            hidden,
            beta,
            alpha=1.0,
            seed=fallback_seed,
        )
        return u, v, delta, 0.0, "random_fallback_zero_linear_objective"

    core = (
        sa[:rank_a, None]
        * (Va_t[:rank_a] @ Vb_t[:rank_b].T)
        * sb[None, :rank_b]
    )
    core_u, core_s, core_v_t = np.linalg.svd(core, full_matrices=False)
    u = Ua[:, :rank_a] @ core_u[:, 0]
    v = Ub[:, :rank_b] @ core_v_t[0]
    u = _project_off(left_span, u)
    v = _project_off(right_span, v)
    u /= np.linalg.norm(u)
    v /= np.linalg.norm(v)
    delta = np.outer(u, v)
    score = float(
        objective_scale
        * np.sum(objective_cotangent * (delta @ hidden_velocity))
    )
    if score < 0.0:
        u = -u
        delta = -delta
        score = -score
    return (
        u,
        v,
        delta,
        score,
        "projected_low_rank_top_singular_linearized_dot_gram",
    )


def _dense_observables(state: ParamState, spec: ModelSpec) -> dict[str, Array]:
    fields = forward_adjoint(state, spec)
    f = state.a @ fields.H[-1] / spec.n
    gram = np.einsum(
        "lnr,lns->lrs", fields.H, fields.H, optimize=True
    ) / spec.n
    theta = tangent_kernel(
        FieldState(state.W, state.a, fields.H, fields.P), spec
    )
    return {
        "Z": fields.Z,
        "T": fields.T,
        "H": fields.H,
        "P": fields.P,
        "f": f,
        "gram": gram,
        "theta": theta,
    }


def _relative_defect(left: Array, right: Array) -> float:
    numerator = float(np.linalg.norm(np.asarray(left) - np.asarray(right)))
    denominator = max(
        1.0,
        float(np.linalg.norm(np.asarray(left))),
        float(np.linalg.norm(np.asarray(right))),
    )
    return numerator / denominator


def _present_state_defects(
    base: ParamState,
    attacked: ParamState,
    initialization: ParamState,
    spec: ModelSpec,
    basis_size: int,
) -> dict[str, float]:
    ladder = _present_state_defects_ladder(
        base,
        attacked,
        initialization,
        spec,
        (basis_size,),
    )
    suffix = f"P{basis_size}_retained_row_coefficients"
    return {
        **{
            key: value
            for key, value in ladder.items()
            if not key.endswith("_retained_row_coefficients")
        },
        "retained_row_coefficients": ladder[suffix],
    }


def _present_state_defects_ladder(
    base: ParamState,
    attacked: ParamState,
    initialization: ParamState,
    spec: ModelSpec,
    basis_sizes: Sequence[int],
) -> dict[str, float]:
    """Audit observables once and nested retained coordinates at every P."""

    levels = tuple(int(P) for P in basis_sizes)
    if not levels or tuple(sorted(set(levels))) != levels:
        raise ValueError("basis sizes must be nonempty, unique, and increasing")
    base_obs = _dense_observables(base, spec)
    attacked_obs = _dense_observables(attacked, spec)
    defects = {
        key: _relative_defect(base_obs[key], attacked_obs[key])
        for key in ("Z", "T", "H", "P", "f", "gram", "theta")
    }
    for basis_size in levels:
        phi = empirical_hermite_phi(
            initialization,
            basis_size=basis_size,
            readout_scale=spec.A,
        )
        coefficients_base = np.einsum(
            "lij,jp->lip", base.W, phi, optimize=True
        )
        coefficients_attacked = np.einsum(
            "lij,jp->lip", attacked.W, phi, optimize=True
        )
        defects[f"P{basis_size}_retained_row_coefficients"] = (
            _relative_defect(coefficients_base, coefficients_attacked)
        )
    return defects


def _copy_param_state(state: ParamState) -> ParamState:
    return ParamState(state.B.copy(), state.W.copy(), state.a.copy())


def _hidden_training_velocity(
    state: ParamState,
    spec: ModelSpec,
    fields: Any,
    velocity: ParamState,
) -> Array:
    """Differentiate the discrete forward recursion along parameter velocity."""

    hidden_velocity = np.empty_like(fields.H)
    hidden_velocity[0] = velocity.B @ spec.X
    scale = spec.gamma / spec.depth
    for layer in range(spec.depth):
        preactivation_velocity = (
            velocity.W[layer] @ fields.H[layer]
            + state.W[layer] @ hidden_velocity[layer]
        )
        hidden_velocity[layer + 1] = (
            hidden_velocity[layer]
            + scale * fields.D[layer] * preactivation_velocity
        )
    return hidden_velocity


def _terminal_dot_gram_cotangent(
    state: ParamState,
    spec: ModelSpec,
    fields: Any,
    hidden_velocity: Array,
) -> Array:
    """Backpropagate the fixed terminal dot-Gram objective to every depth."""

    sample_count = spec.y.size
    objective = (
        np.ones((sample_count, sample_count), dtype=float) / sample_count
    )
    cotangent = np.empty_like(hidden_velocity)
    cotangent[-1] = (
        fields.H[-1] @ (objective + objective.T) / spec.n
    )
    scale = spec.gamma / spec.depth
    for layer in range(spec.depth - 1, -1, -1):
        cotangent[layer] = cotangent[layer + 1] + scale * (
            state.W[layer].T
            @ (fields.D[layer] * cotangent[layer + 1])
        )
    return cotangent


def _apply_rank_one_layer_family(
    state: ParamState,
    U: Array,
    V: Array,
    *,
    amplitude: float,
) -> ParamState:
    if U.shape != V.shape or U.shape != (state.W.shape[0], state.W.shape[1]):
        raise ValueError("rank-one factor family has the wrong shape")
    attacked = _copy_param_state(state)
    for layer in range(state.W.shape[0]):
        attacked.W[layer] += float(amplitude) * np.outer(U[layer], V[layer])
    return attacked


def _run_attack(
    protocol: Mapping[str, Any],
    config: Mapping[str, Any],
) -> tuple[dict[str, Array], dict[str, Any]]:
    model = _canonical_model(protocol)
    spec = _dense_spec(
        model,
        n=int(config["n"]),
        depth=int(config["L"]),
        seed=int(config["root_seed"]),
    )
    master = initialize_gaussian_master(
        n_max=int(config["master_width"]),
        depth_max=int(config["master_depth"]),
        input_dim=model["X"].shape[0],
        seed=int(config["root_seed"]),
    )
    master_hashes = {
        "B_standard": _sha256_array(master.B_standard),
        "W_standard": _sha256_array(master.W_standard),
        "a_standard": _sha256_array(master.a_standard),
    }
    initialization = materialize_coupled_state(master, spec)
    checkpoint = float(config["checkpoint"])
    trained = simulate_checkpoints(
        initialization,
        spec,
        (0.0, checkpoint),
        dt=float(config["dt"]),
    ).final_state
    fields = forward_adjoint(trained, spec)
    basis_ladder = tuple(int(P) for P in config["basis_ladder"])
    primary_basis_size = int(config["primary_basis_size"])
    if primary_basis_size != basis_ladder[-1]:
        raise ValueError("the primary attack basis must be the ladder maximum")
    phi = empirical_hermite_phi(
        initialization,
        basis_size=primary_basis_size,
        readout_scale=spec.A,
    )
    amplitudes = tuple(float(value) for value in config["amplitudes"])
    restart_horizons = tuple(
        float(value) for value in config["restart_horizons"]
    )
    horizon = max(restart_horizons)
    tolerance = float(config["constraint_tolerance_relative"])
    arrays: dict[str, Array] = {
        "initial_B": initialization.B,
        "initial_a": initialization.a,
        "checkpoint_B": trained.B,
        "checkpoint_a": trained.a,
        "basis_ladder": np.asarray(basis_ladder, dtype=np.int64),
        "primary_basis_size": np.asarray(
            primary_basis_size, dtype=np.int64
        ),
        "amplitudes": np.asarray(amplitudes),
        "restart_horizons": np.asarray(restart_horizons),
    }
    detail: dict[str, Any] = {
        "multilayer": {},
        "coupled_root_sha256": master_hashes,
        "root_coupling": protocol["stage_3_same_state_attack"][
            "root_coupling"
        ],
        "basis_semantics": (
            "Every direction is orthogonal to the literal nested P=35 "
            "Hermite span. P=5, P=15, and P=35 retained-coordinate defects "
            "are audited separately; P=35 is primary."
        ),
        "off_manifold_semantics": (
            "Both attack families are off-manifold restart stresses. "
            "Absence of a continuation gap is UNRESOLVED and is never a "
            "positive state-sufficiency certificate."
        ),
        "coherent_objective": (
            "Per layer, the top rank-one direction of the P=35-invisible "
            "projection of the fixed terminal dot-Gram linearized objective. "
            "Layer scores are oriented positively. This is exact only for "
            "that local linear objective, not a global nonlinear optimizer."
        ),
    }

    velocity = parameter_vector_field(trained, spec)
    hidden_velocity = _hidden_training_velocity(
        trained, spec, fields, velocity
    )
    objective_cotangent = _terminal_dot_gram_cotangent(
        trained, spec, fields, hidden_velocity
    )
    independent_U = np.empty((spec.depth, spec.n), dtype=float)
    independent_V = np.empty_like(independent_U)
    coherent_U = np.empty_like(independent_U)
    coherent_V = np.empty_like(independent_U)
    coherent_scores = np.empty(spec.depth, dtype=float)
    independent_seeds = np.empty(spec.depth, dtype=np.uint64)
    coherent_fallback_seeds = np.empty(spec.depth, dtype=np.uint64)
    coherent_labels: list[str] = []
    direction_constraint_defects: dict[str, dict[str, float]] = {}
    for layer in range(spec.depth):
        beta = fields.D[layer] * fields.P[layer + 1]
        independent_seed = _derive_seed(
            int(config["root_seed"]), "attack", 1, layer
        )
        coherent_fallback_seed = _derive_seed(
            int(config["root_seed"]), "attack", 2, layer
        )
        independent_u, independent_v, independent_delta = (
            random_invisible_rank_one(
                phi,
                fields.H[layer],
                beta,
                alpha=1.0,
                seed=independent_seed,
            )
        )
        (
            coherent_u,
            coherent_v,
            coherent_delta,
            coherent_score,
            coherent_label,
        ) = coherent_invisible_rank_one(
            phi,
            fields.H[layer],
            beta,
            hidden_velocity[layer],
            fields.D[layer] * objective_cotangent[layer + 1],
            objective_scale=spec.gamma / spec.depth,
            fallback_seed=coherent_fallback_seed,
        )
        independent_U[layer] = independent_u
        independent_V[layer] = independent_v
        coherent_U[layer] = coherent_u
        coherent_V[layer] = coherent_v
        coherent_scores[layer] = coherent_score
        independent_seeds[layer] = independent_seed
        coherent_fallback_seeds[layer] = coherent_fallback_seed
        coherent_labels.append(coherent_label)
        for label, delta in (
            ("independent", independent_delta),
            ("coherent", coherent_delta),
        ):
            direction_constraint_defects[f"{label}_layer_{layer}"] = {
                "deltaW_P35_fro": float(np.linalg.norm(delta @ phi)),
                "deltaW_H_fro": float(
                    np.linalg.norm(delta @ fields.H[layer])
                ),
                "deltaW_T_beta_fro": float(
                    np.linalg.norm(delta.T @ beta)
                ),
                "unit_frobenius_error": float(
                    abs(np.linalg.norm(delta) - 1.0)
                ),
            }

    arrays["independent_U"] = independent_U
    arrays["independent_V"] = independent_V
    arrays["coherent_U"] = coherent_U
    arrays["coherent_V"] = coherent_V
    arrays["coherent_layer_linear_scores"] = coherent_scores
    arrays["coherent_orientation_signs"] = np.ones(
        spec.depth, dtype=np.int8
    )
    arrays["independent_direction_seeds"] = independent_seeds
    arrays["coherent_fallback_seeds"] = coherent_fallback_seeds
    diagnostic_layers = np.asarray(config["layers"], dtype=np.int64)
    arrays["diagnostic_layer_indices"] = diagnostic_layers
    arrays["diagnostic_layer_linear_scores"] = coherent_scores[
        diagnostic_layers
    ]

    sample_dt = min(
        float(protocol["norms"]["time_sampling"]),
        min(restart_horizons),
    )
    base_path = _integrate_dense_observables(
        trained,
        spec,
        horizon=horizon,
        dt=float(config["dt"]),
        sample_dt=sample_dt,
        required_times=restart_horizons,
    )
    arrays["restart_times"] = base_path["times"]
    horizon_indices = np.asarray(
        [
            int(
                np.flatnonzero(
                    np.isclose(
                        base_path["times"],
                        target,
                        rtol=0.0,
                        atol=1e-13,
                    )
                )[0]
            )
            for target in restart_horizons
        ],
        dtype=np.int64,
    )
    arrays["restart_horizon_indices"] = horizon_indices
    arrays["base_restart_f"] = base_path["f"]
    arrays["base_restart_gram"] = base_path["gram"]
    arrays["base_restart_loss"] = base_path["loss"]

    for label, U, V in (
        ("independent", independent_U, independent_V),
        ("coherent", coherent_U, coherent_V),
    ):
        f_differences: list[Array] = []
        gram_differences: list[Array] = []
        loss_differences: list[Array] = []
        defect_records: dict[str, Mapping[str, float]] = {}
        for amplitude in amplitudes:
            attacked = _apply_rank_one_layer_family(
                trained,
                U,
                V,
                amplitude=amplitude,
            )
            defects = _present_state_defects_ladder(
                trained,
                attacked,
                initialization,
                spec,
                basis_ladder,
            )
            if max(defects.values()) > tolerance:
                raise RuntimeError(
                    f"{label} multilayer attack at alpha={amplitude} violates "
                    "present-state tolerance: "
                    f"{max(defects.values()):.3e}"
                )
            attacked_path = _integrate_dense_observables(
                attacked,
                spec,
                horizon=horizon,
                dt=float(config["dt"]),
                sample_dt=sample_dt,
                required_times=restart_horizons,
            )
            if not np.array_equal(
                base_path["times"], attacked_path["times"]
            ):
                raise RuntimeError("attack restart time grids disagree")
            f_differences.append(attacked_path["f"] - base_path["f"])
            gram_differences.append(
                attacked_path["gram"] - base_path["gram"]
            )
            loss_differences.append(
                attacked_path["loss"] - base_path["loss"]
            )
            defect_records[f"alpha_{amplitude:g}"] = defects
        arrays[f"{label}_restart_f_difference"] = np.stack(f_differences)
        arrays[f"{label}_restart_gram_difference"] = np.stack(
            gram_differences
        )
        arrays[f"{label}_restart_loss_difference"] = np.stack(
            loss_differences
        )
        detail["multilayer"][label] = {
            "relative_present_state_defects_by_amplitude": defect_records,
            "layers_perturbed": spec.depth,
            "per_layer_frobenius_norm": "alpha",
            "manifold_status": "off-manifold restart stress",
        }
    detail["direction_constraint_defects"] = direction_constraint_defects
    detail["coherent_direction_labels"] = coherent_labels
    detail["direction_factor_sha256"] = {
        key: _sha256_array(arrays[key])
        for key in (
            "independent_U",
            "independent_V",
            "coherent_U",
            "coherent_V",
        )
    }
    detail["horizon_readout_semantics"] = {
        f"{target:g}": int(index)
        for target, index in zip(restart_horizons, horizon_indices)
    }
    detail["primary_diagnostic"] = (
        "coherent P=35 continuation gap; its directions are per-layer "
        "structured/local rather than a global nonlinear optimizer. A "
        "persistent gap is a structural warning, while no gap leaves "
        "sufficiency UNRESOLVED"
    )
    return arrays, detail


def _attack_layers(depth: int) -> tuple[int, ...]:
    # Zero-based cells nearest the declared quarter positions.
    layers = (
        max(0, depth // 4 - 1),
        max(0, depth // 2 - 1),
        max(0, 3 * depth // 4 - 1),
    )
    if len(set(layers)) != 3:
        raise ValueError("declared attack layers are not distinct")
    return layers


def _validate_attack_config(
    protocol: Mapping[str, Any],
    args: argparse.Namespace,
) -> dict[str, Any]:
    stage = protocol["stage_3_same_state_attack"]
    if args.n not in stage["widths"] or args.L not in stage["depths"]:
        raise ValueError("attack width/depth is outside the declared grid")
    if not 0 <= args.root_index < stage["heldout_roots"]:
        raise ValueError("attack root-index is outside the declared range")
    basis_ladder = tuple(int(P) for P in stage["basis_ladder"])
    if basis_ladder != (5, 15, 35):
        raise ValueError("attack basis ladder must remain exactly (5,15,35)")
    if int(stage["primary_basis_size"]) != basis_ladder[-1]:
        raise ValueError("P=35 must remain the primary attack basis")
    amplitudes = tuple(float(value) for value in stage["amplitudes"])
    restart_horizons = tuple(
        float(value) for value in stage["restart_horizons"]
    )
    if (
        not amplitudes
        or tuple(sorted(set(amplitudes))) != amplitudes
        or amplitudes[0] <= 0.0
    ):
        raise ValueError("attack amplitudes must be positive and increasing")
    if (
        not restart_horizons
        or tuple(sorted(set(restart_horizons))) != restart_horizons
        or restart_horizons[0] <= 0.0
    ):
        raise ValueError(
            "attack restart horizons must be positive and increasing"
        )
    dt = float(protocol["stage_1_ordered_target"]["dt"])
    root_seed = _derive_seed(
        int(protocol["error_ledger"]["bootstrap_seed"]),
        "attack",
        args.root_index,
    )
    return {
        "n": int(args.n),
        "L": int(args.L),
        "root_index": int(args.root_index),
        "root_seed": root_seed,
        "master_width": max(int(value) for value in stage["widths"]),
        "master_depth": max(int(value) for value in stage["depths"]),
        "checkpoint": float(stage["checkpoint"]),
        "layers": list(_attack_layers(args.L)),
        "basis_ladder": list(basis_ladder),
        "primary_basis_size": int(stage["primary_basis_size"]),
        "amplitudes": list(amplitudes),
        "restart_horizons": list(restart_horizons),
        "maximum_restart_horizon": max(restart_horizons),
        "constraint_tolerance_relative": float(
            stage["constraint_tolerance_relative"]
        ),
        "dt": dt,
    }


def dry_run_inventory(protocol: Mapping[str, Any]) -> dict[str, Any]:
    """Return the immutable job inventory and conservative resource proxies."""

    s0 = protocol["stage_0_integrity_and_numerics"]
    execution_inventory = s0["execution_inventory"]
    active_jobs = (
        len(execution_inventory["active_levels"])
        * len(execution_inventory["active_configs_per_level"])
    )
    phase_A_jobs = (
        len(execution_inventory["active_levels"])
        * len(execution_inventory["phase_A_primary_configs_per_level"])
    )
    phase_B_jobs = (
        len(execution_inventory["active_levels"])
        * len(
            execution_inventory[
                "phase_B_conditional_upward_configs_per_level"
            ]
        )
    )
    downward_diagnostic_jobs = (
        len(execution_inventory["active_levels"])
        * len(
            execution_inventory[
                "seed0_downward_diagnostic_configs_per_level"
            ]
        )
    )
    p70_jobs = len(execution_inventory["conditional_P70_configs"])
    base_dimension = len(_canonical_model(protocol)["X"]) + 1
    state_candidates: list[dict[str, Any]] = []
    for P in execution_inventory["active_levels"]:
        for config in execution_inventory["active_configs_per_level"]:
            M = int(config["base_order"]) ** base_dimension
            state_candidates.append(
                {
                    "P": int(P),
                    **{
                        key: config[key]
                        for key in ("base_order", "N", "R", "dt", "seed")
                    },
                    "M": M,
                    "state_bytes": (
                        int(config["N"])
                        * M
                        * int(config["R"])
                        * int(P)
                        * 8
                    ),
                }
            )
    for config in execution_inventory["conditional_P70_configs"]:
        M = int(config["base_order"]) ** base_dimension
        state_candidates.append(
            {
                "P": 70,
                **{
                    key: config[key]
                    for key in ("base_order", "N", "R", "dt", "seed")
                },
                "M": M,
                "state_bytes": (
                    int(config["N"])
                    * M
                    * int(config["R"])
                    * 70
                    * 8
                ),
            }
        )
    worst_state_config = max(
        state_candidates, key=lambda item: item["state_bytes"]
    )
    worst_pde_state_bytes = int(worst_state_config["state_bytes"])
    s1 = protocol["stage_1_ordered_target"]
    scaling: dict[str, Any] = {}
    for tier in ("screen", "positive"):
        grid = s1[f"{tier}_grid"]
        n_max, L_max = max(grid["n"]), max(grid["L"])
        root_bytes = (
            L_max * n_max * n_max + n_max * 4
        ) * 8
        scaling[tier] = {
            "coupled_roots": grid["coupled_roots"],
            "trajectories_per_root": len(grid["n"]) * len(grid["L"]),
            "total_trajectories": (
                grid["coupled_roots"] * len(grid["n"]) * len(grid["L"])
            ),
            "largest_root_bytes": root_bytes,
            "largest_dense_RK4_state_bytes_lower_bound": (
                (L_max * n_max * n_max + n_max * 4) * 8
            ),
        }
    s2 = protocol["stage_2_homogenization"]
    homogeneous_trajectories = (
        s2["outer_B_a_roots"]
        * s2["independent_W_replicas_per_outer_root"]
        * len(s2["widths"])
        * len(s2["depths"])
    )
    homogenization_statistics_per_field = 2 * (
        1 + len(s2["candidate_levels"])
    )
    homogenization_feature_count = _canonical_model(protocol)["X"].shape[0]
    homogenization_field_elements = (
        2
        * s2["independent_W_replicas_per_outer_root"]
        * homogenization_feature_count
        * sum(s2["widths"])
        * len(s2["depths"])
        * len(s2["checkpoints"])
    )
    homogenization_depth_average_elements = (
        homogenization_statistics_per_field
        * s2["independent_W_replicas_per_outer_root"]
        * homogenization_feature_count
        * sum(s2["widths"])
        * len(s2["depths"])
        * len(s2["checkpoints"])
    )
    homogenization_covariance_elements = (
        homogenization_statistics_per_field
        * len(s2["widths"])
        * len(s2["checkpoints"])
        * sum(depth * depth for depth in s2["depths"])
    )
    homogenization_bias_elements = (
        homogenization_statistics_per_field
        * len(s2["widths"])
        * len(s2["checkpoints"])
        * sum(s2["depths"])
    )
    homogenization_scalar_elements = (
        2
        * homogenization_statistics_per_field
        * len(s2["widths"])
        * len(s2["depths"])
        * len(s2["checkpoints"])
    )
    homogenization_provenance_elements = (
        int(s2["global_master"]["n_max"])
        * homogenization_feature_count
        + int(s2["global_master"]["n_max"])
        + s2["independent_W_replicas_per_outer_root"]
        + len(s2["checkpoints"])
        + len(s2["widths"])
        + len(s2["depths"])
    )
    homogenization_archive_uncompressed_bytes = 8 * (
        homogenization_field_elements
        + homogenization_depth_average_elements
        + homogenization_covariance_elements
        + homogenization_bias_elements
        + homogenization_scalar_elements
        + homogenization_provenance_elements
    )
    s3 = protocol["stage_3_same_state_attack"]
    attack_jobs = (
        len(s3["widths"])
        * len(s3["depths"])
        * s3["heldout_roots"]
    )
    return {
        "protocol_sha256": _sha256_file(PROTOCOL_PATH),
        "runner_sha256": _sha256_file(RUNNER_PATH),
        "numerics": {
            "active_jobs": active_jobs,
            "phase_A_primary_jobs": phase_A_jobs,
            "phase_B_conditional_jobs": phase_B_jobs,
            "downward_diagnostic_jobs": downward_diagnostic_jobs,
            "conditional_P70_jobs": p70_jobs,
            "worst_single_state_bytes": worst_pde_state_bytes,
            "worst_single_state_config": worst_state_config,
            "worst_stage0_preflight_estimated_peak_bytes": int(
                7.5 * worst_pde_state_bytes + 1024**3
            ),
            "ordinary_checkpoint_archive_state_bytes": 0,
            "checkpoint_policy": (
                "ordinary numerical refinement saves observables only; "
                "Stage 4 computes stateful diagnostics online"
            ),
            "warning": (
                "RK4 requires multiple state-sized work arrays; these figures "
                "are lower bounds, not scheduler memory requests"
            ),
        },
        "scaling": scaling,
        "homogenization": {
            "outer_jobs": s2["outer_B_a_roots"],
            "dense_trajectories": homogeneous_trajectories,
            "widths": list(s2["widths"]),
            "depths": list(s2["depths"]),
            "replicas_per_depth_block": (
                s2["independent_W_replicas_per_outer_root"]
            ),
            "full_covariance_matrices_per_outer_root": (
                len(s2["widths"])
                * len(s2["depths"])
                * len(s2["checkpoints"])
                * 2
                * (1 + len(s2["candidate_levels"]))
            ),
            "global_master_bytes_per_W_replica": (
                int(s2["global_master"]["L_max"])
                * int(s2["global_master"]["n_max"]) ** 2
                * 8
            ),
            "maximum_archive_uncompressed_array_bytes_estimate": int(
                homogenization_archive_uncompressed_bytes
            ),
            "raw_layer_tensors_archived": False,
            "archive_policy": (
                "replica terminal/input fields and depth averages; full "
                "L-by-L covariance and signed split-half bias summaries only"
            ),
        },
        "attack": {
            "selected_jobs": attack_jobs,
            "checkpoint_trainings_per_job": 1,
            "basis_ladder": list(s3["basis_ladder"]),
            "primary_basis_size": int(s3["primary_basis_size"]),
            "amplitudes_per_job": len(s3["amplitudes"]),
            "horizon_readouts_per_restart": len(s3["restart_horizons"]),
            "maximum_restart_horizon": max(s3["restart_horizons"]),
            "coherent_layer_diagnostics_per_job": len(s3["layers"]),
            "independent_multilayer_attacks_per_job": 1,
            "coherent_multilayer_stresses_per_job": 1,
            "restart_trajectories_per_job": (
                1 + 2 * len(s3["amplitudes"])
            ),
            "interpretation": (
                "one off-manifold falsification bundle per (n,L,root); "
                "absence of a gap is unresolved, never a sufficiency pass"
            ),
        },
    }


def _add_output_arguments(parser: argparse.ArgumentParser) -> None:
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path)
    group.add_argument(
        "--output-dir",
        type=Path,
        default=AUDIT_ROOT / "results",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run one frozen PDE proof-obligation audit job."
    )
    subparsers = parser.add_subparsers(dest="stage", required=True)
    subparsers.add_parser("dry-run", help="print inventory and resource proxies")

    numerics = subparsers.add_parser("numerics")
    numerics.add_argument("--P", type=int, required=True)
    numerics.add_argument("--N", type=int, required=True)
    numerics.add_argument("--R", type=int, required=True)
    numerics.add_argument("--dt", type=float, required=True)
    numerics.add_argument("--seed", type=int, required=True)
    numerics.add_argument(
        "--base-order", type=int, default=PRIMARY_BASE_ORDER
    )
    numerics.add_argument("--T", type=float, default=2.0)
    numerics.add_argument("--allow-conditional-p70", action="store_true")
    numerics.add_argument(
        "--allow-phase-b-refinements", action="store_true"
    )
    _add_output_arguments(numerics)

    scaling = subparsers.add_parser("scaling")
    scaling.add_argument("--tier", choices=("screen", "positive"), required=True)
    scaling.add_argument("--n-grid", type=_parse_int_grid)
    scaling.add_argument("--L-grid", type=_parse_int_grid)
    scaling.add_argument("--root-index", type=int, required=True)
    scaling.add_argument("--T", type=float, default=2.0)
    scaling.add_argument("--dt", type=float, default=0.02)
    _add_output_arguments(scaling)

    homogenization = subparsers.add_parser("homogenization")
    homogenization.add_argument("--outer-root-index", type=int, required=True)
    homogenization.add_argument("--depths", type=_parse_int_grid)
    homogenization.add_argument("--replicas", type=int, default=8)
    homogenization.add_argument("--dt", type=float, default=0.02)
    _add_output_arguments(homogenization)

    attack = subparsers.add_parser("attack")
    attack.add_argument("--n", type=int, required=True)
    attack.add_argument("--L", type=int, required=True)
    attack.add_argument("--root-index", type=int, required=True)
    _add_output_arguments(attack)
    return parser


def _execute(
    stage: str,
    protocol: Mapping[str, Any],
    config: Mapping[str, Any],
) -> tuple[dict[str, Array], dict[str, Any]]:
    if stage == "numerics":
        return _run_numerics(protocol, config)
    if stage == "scaling":
        return _run_scaling(protocol, config)
    if stage == "homogenization":
        return _run_homogenization(protocol, config)
    if stage == "attack":
        return _run_attack(protocol, config)
    raise ValueError(f"unsupported scientific stage: {stage}")


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    protocol = load_protocol()
    if args.stage == "dry-run":
        print(json.dumps(dry_run_inventory(protocol), indent=2, sort_keys=True))
        return 0
    validators = {
        "numerics": _validate_numerics_config,
        "scaling": _validate_scaling_config,
        "homogenization": _validate_homogenization_config,
        "attack": _validate_attack_config,
    }
    if args.stage not in validators:
        raise ValueError(f"unsupported stage: {args.stage}")
    config = validators[args.stage](protocol, args)
    metadata = _provenance(protocol, args.stage, config)
    output_path = _output_path(args, args.stage, config)
    partial_path = output_path.with_name(output_path.name + ".partial")
    if partial_path.exists():
        raise FileExistsError(
            f"stale partial archive blocks execution: {partial_path}"
        )
    if output_path.exists():
        status = _resume_existing(output_path, metadata)
        print(
            json.dumps(
                {"status": status, "stage": args.stage, "output": str(output_path)}
            )
        )
        return 0

    arrays, detail = _execute(args.stage, protocol, config)
    metadata = build_output_metadata(metadata, arrays, detail)
    status = atomic_save_npz(output_path, arrays, metadata)
    verified = load_sealed_stage_archive(
        output_path,
        required_config_keys=tuple(config),
        required_arrays=tuple(arrays),
        expected_stage=args.stage,
        expected_protocol_sha256=str(metadata["protocol_sha256"]),
        expected_source_hashes=metadata["source_hashes"],
    )
    if (
        verified.metadata.get("frozen_inputs_sha256")
        != metadata["frozen_inputs_sha256"]
    ):
        raise ValueError("published archive lost its frozen-input binding")
    print(
        json.dumps(
            {"status": status, "stage": args.stage, "output": str(output_path)}
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
