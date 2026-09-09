"""Stateful Stage 4 and finite-horizon Stage 6 scientific jobs.

This module is deliberately separate from :mod:`run_study`.  Ordinary
quadrature/time/depth refinement archives remain observables-only, while the
generator and tail jobs here hold one state in memory only as long as it is
needed.  No archive from this module is admissible unless the protocol and
all scientific source were frozen first.

The four CLI jobs are:

``generator``
    Integrate the common-master P=5,15,35 family at one exact member of the
    preregistered primary/M/N/R/dt numerical-resolution inventory and evaluate
    generator, shadow, and held-out basis diagnostics online.  A predeclared
    P=70 extension is available only behind an explicit conditional flag.

``tail-pde``
    Integrate one restartable P=5 horizon block and publish its exact endpoint
    state for the next block.

``tail-dense``
    Integrate one declared finite dense root through the protocol's fixed
    diagnostic horizon.

``gain``
    Measure the exact finite residual-dictionary group-L1/L2 gain on either
    the primary or midpoint-refined source-time grid and at one exact member
    of the preregistered primary/M/N/R/dt numerical-resolution inventory.
    High-level residual snapshots are projected online and all tangent
    responses are compacted to f/G data.  The active pairs are P=5,15 from
    Q=35; a Q=70 next-closure-step measurement is available only as the
    explicitly authorized P=35 from Q=70 conditional branch.

Stage 6 outputs are finite-horizon diagnostics.  They do not, by themselves,
constitute an infinite-time claim.
"""

from __future__ import annotations

import argparse
import gc
import json
from pathlib import Path
import sys
from typing import Any, Mapping, Sequence

import numpy as np


HERE = Path(__file__).resolve().parent
AUDIT_ROOT = HERE.parent
WORKSPACE_ROOT = AUDIT_ROOT.parent
STRUCTURAL_RUNNER_PATH = Path(__file__).resolve()

if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import run_study as common  # noqa: E402
from cross_p import (  # noqa: E402
    basis_diagnostic,
    build_nested_quadratures,
    generator_diagnostics,
    hermite_subspace,
    project_state,
    random_subspace,
    state_difference_norm,
    trajectory_pod_subspace,
    weighted_state_norm,
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
    ParamState,
    forward_adjoint,
    rk4_param_step,
    tangent_kernel,
)
from pde_tangent import (  # noqa: E402
    ObservableScales,
    projected_back_residual,
    stage5_serializable_result,
    weighted_tangent_norm,
)


Array = np.ndarray
PRIMARY_BASE_ORDER = 5
STRUCTURAL_STAGE_CODES = {
    "tail_dense": 607,
}


def _structural_provenance(
    protocol: Mapping[str, Any],
    stage: str,
    config: Mapping[str, Any],
) -> dict[str, Any]:
    provenance = common._provenance(protocol, stage, config)
    source_hashes = dict(provenance["source_hashes"])
    source_hashes["structural_runner"] = common._sha256_file(
        STRUCTURAL_RUNNER_PATH
    )
    source_hashes["pde_tangent"] = common._sha256_file(
        HERE / "pde_tangent.py"
    )
    provenance["source_hashes"] = source_hashes
    return provenance


def _primary_pde_config(protocol: Mapping[str, Any]) -> dict[str, Any]:
    ladder = protocol["stage_0_integrity_and_numerics"]["nested_ladder"]
    return {
        "N": int(ladder["primary_N"]),
        "R": int(ladder["primary_R"]),
        "dt": float(ladder["primary_dt"]),
        "base_order": int(ladder["primary_base_order"]),
        "M": int(ladder["primary_M"]),
    }


def _validate_structural_resolution(
    protocol: Mapping[str, Any],
    stage_key: str,
    args: argparse.Namespace,
) -> dict[str, Any]:
    """Admit one member of a stage's frozen structural-resolution family."""

    resolution = protocol[stage_key]["numerical_resolution"]
    return _validate_resolution_inventory(
        protocol,
        resolution,
        args,
        label=stage_key,
        family=f"{stage_key}_active",
    )


def _validate_resolution_inventory(
    protocol: Mapping[str, Any],
    resolution: Mapping[str, Any],
    args: argparse.Namespace,
    *,
    label: str,
    family: str,
) -> dict[str, Any]:
    """Admit exactly four primary scrambles or one declared axis refinement."""

    requested = {
        "base_order": int(args.base_order),
        "N": int(args.N),
        "R": int(args.R),
        "dt": float(args.dt),
        "seed": int(args.seed),
    }
    primary = resolution["primary"]
    def same_coordinates(
        candidate: Mapping[str, Any], *, include_seed: bool
    ) -> bool:
        integer_keys = ["base_order", "N", "R"]
        if include_seed:
            integer_keys.append("seed")
        return (
            all(
                int(requested[key]) == int(candidate[key])
                for key in integer_keys
            )
            and requested["dt"] == float(candidate["dt"])
        )

    if same_coordinates(primary, include_seed=False) and (
        requested["seed"] in primary["scramble_seeds"]
    ):
        axis = "primary"
    else:
        matches = []
        for candidate in resolution["one_axis_refinements_at_seed_20260723"]:
            if same_coordinates(candidate, include_seed=True):
                matches.append(str(candidate["axis"]))
        if len(matches) != 1:
            raise ValueError(
                f"{label} configuration is not in the preregistered "
                f"structural numerical-resolution inventory: {requested}"
            )
        axis = matches[0]
    model = common._canonical_model(protocol)
    return {
        **requested,
        "M": int(requested["base_order"])
        ** (model["X"].shape[0] + 1),
        "resolution_axis": axis,
        "resolution_is_primary": axis == "primary",
        "resolution_family": str(family),
    }


def _make_family(
    protocol: Mapping[str, Any],
    *,
    levels: Sequence[int],
    N: int,
    R: int,
    seed: int,
    base_order: int,
):
    model = common._canonical_model(protocol)
    latent_dim = model["X"].shape[0] + 1
    template = PDESpec(
        X=model["X"],
        y=model["y"],
        basis_size=max(levels),
        depth_nodes=int(N),
        base_points=int(base_order) ** latent_dim,
        fast_points=int(R),
        quadrature_seed=int(seed),
        sigma_w=model["sigma_w"],
        A=model["A"],
        gamma=model["gamma"],
        activation=model["activation"],
    )
    return build_nested_quadratures(
        template,
        levels=tuple(levels),
        base_order=int(base_order),
        master_levels=common.MASTER_LEVELS,
    )


def _state_subtract(left: PDEState, right: PDEState) -> PDEState:
    return PDEState(
        B=left.B - right.B,
        a=left.a - right.a,
        c=left.c - right.c,
    )


def initialization_subtracted_errors(
    f_difference: Array,
    gram_difference: Array,
    loss_difference: Array,
    state_difference: Sequence[PDEState],
    quadrature: Any,
) -> dict[str, Array]:
    """Norm raw differences and differences after removing their t=0 value."""

    f_difference = np.asarray(f_difference, dtype=float)
    gram_difference = np.asarray(gram_difference, dtype=float)
    loss_difference = np.asarray(loss_difference, dtype=float)
    if (
        f_difference.ndim != 2
        or gram_difference.ndim != 4
        or loss_difference.shape != (f_difference.shape[0],)
        or gram_difference.shape[0] != f_difference.shape[0]
        or len(state_difference) != f_difference.shape[0]
    ):
        raise ValueError("shadow difference arrays have incompatible shapes")
    initial_state = state_difference[0]
    raw_state = np.asarray(
        [weighted_state_norm(value, quadrature) for value in state_difference]
    )
    increment_state = np.asarray(
        [
            weighted_state_norm(
                _state_subtract(value, initial_state), quadrature
            )
            for value in state_difference
        ]
    )
    gram_increment = gram_difference - gram_difference[0]
    return {
        "raw_state": raw_state,
        "raw_f": np.linalg.norm(f_difference, axis=1),
        "raw_gram": np.max(
            np.linalg.norm(
                gram_difference.reshape(
                    gram_difference.shape[0],
                    gram_difference.shape[1],
                    -1,
                ),
                axis=2,
            ),
            axis=1,
        ),
        "raw_loss": np.abs(loss_difference),
        "increment_state": increment_state,
        "increment_f": np.linalg.norm(
            f_difference - f_difference[0], axis=1
        ),
        "increment_gram": np.max(
            np.linalg.norm(
                gram_increment.reshape(
                    gram_increment.shape[0],
                    gram_increment.shape[1],
                    -1,
                ),
                axis=2,
            ),
            axis=1,
        ),
        "increment_loss": np.abs(loss_difference - loss_difference[0]),
    }


def _shadow_errors(
    high_state: PDEState,
    low_spec: Any,
    high_spec: Any,
    low_quadrature: Any,
    high_quadrature: Any,
    *,
    horizon: float,
    dt: float,
    sample_dt: float,
) -> dict[str, Array]:
    low = project_state(high_state, low_spec.basis_size)
    high = high_state.copy()
    relative_times = common._event_times(horizon, sample_dt)
    current = 0.0
    tolerance = 128 * np.finfo(float).eps * max(1.0, horizon)
    f_difference: list[Array] = []
    gram_difference: list[Array] = []
    loss_difference: list[float] = []
    state_difference: list[PDEState] = []
    for target in relative_times:
        while current < target - tolerance:
            step = min(dt, float(target - current))
            high = rk4_step(high, step, high_spec, high_quadrature)
            low = rk4_step(low, step, low_spec, low_quadrature)
            current += step
        high_observable = observe(high, high_spec, high_quadrature)
        low_observable = observe(low, low_spec, low_quadrature)
        projected_high = project_state(high, low_spec.basis_size)
        state_difference.append(_state_subtract(projected_high, low))
        f_difference.append(high_observable.f - low_observable.f)
        gram_difference.append(
            high_observable.grams - low_observable.grams
        )
        loss_difference.append(
            high_observable.loss - low_observable.loss
        )
    errors = initialization_subtracted_errors(
        np.stack(f_difference),
        np.stack(gram_difference),
        np.asarray(loss_difference),
        state_difference,
        low_quadrature,
    )
    return {"times": relative_times, **errors}


SHADOW_OBSERVABLE_NORM_SEMANTICS = (
    "max(||delta f||_2/S_f, sup_depth ||delta G(s)||_F/S_G)"
)


def _add_shadow_archive_arrays(
    arrays: dict[str, Array],
    *,
    tag: str,
    horizon_tag: str,
    shadow_records: Sequence[Mapping[str, Array]],
    protocol: Mapping[str, Any],
) -> None:
    """Archive one shadow family with an explicit sup-depth norm contract."""

    if not shadow_records:
        raise ValueError("shadow_records must be nonempty")
    prefix = f"{tag}_shadow_{horizon_tag}"
    reference_times = np.asarray(shadow_records[0]["times"], dtype=float)
    if reference_times.ndim != 1 or reference_times.size < 2:
        raise ValueError("shadow times must be a one-dimensional grid")
    if not all(
        np.array_equal(
            np.asarray(value["times"], dtype=float), reference_times
        )
        for value in shadow_records
    ):
        raise ValueError("shadow records must share one exact time grid")
    arrays[f"{prefix}_times"] = reference_times
    for name in (
        "raw_state",
        "raw_f",
        "raw_gram",
        "raw_loss",
        "increment_state",
        "increment_f",
        "increment_gram",
        "increment_loss",
    ):
        arrays[f"{prefix}_{name}"] = np.stack(
            [np.asarray(value[name], dtype=float) for value in shadow_records]
        )

    S_f = float(protocol["norms"]["S_f"])
    S_G = float(protocol["norms"]["S_G"])
    raw_normalized = np.stack(
        [
            np.maximum(value["raw_f"] / S_f, value["raw_gram"] / S_G)
            for value in shadow_records
        ]
    )
    increment_normalized = np.stack(
        [
            np.maximum(
                value["increment_f"] / S_f,
                value["increment_gram"] / S_G,
            )
            for value in shadow_records
        ]
    )
    # The explicit keys are authoritative.  The aliases keep pre-freeze
    # consumers readable without asking them to infer a changed norm.
    arrays[f"{prefix}_raw_observable_normalized_sup_depth"] = raw_normalized
    arrays[
        f"{prefix}_increment_observable_normalized_sup_depth"
    ] = increment_normalized
    arrays[f"{prefix}_raw_observable_normalized"] = raw_normalized
    arrays[f"{prefix}_increment_observable_normalized"] = (
        increment_normalized
    )
    semantics = np.asarray(
        SHADOW_OBSERVABLE_NORM_SEMANTICS,
        dtype=f"S{len(SHADOW_OBSERVABLE_NORM_SEMANTICS.encode('ascii'))}",
    )
    existing = arrays.setdefault(
        "shadow_observable_normalized_norm_semantics_ascii", semantics
    )
    if not np.array_equal(existing, semantics):
        raise RuntimeError("shadow norm semantics changed within one archive")

    positive = np.flatnonzero(reference_times > 0.0)
    if positive.size == 0:
        raise ValueError("shadow time grid needs a positive time")
    first_positive = int(positive[0])
    initial_slopes = []
    for value in shadow_records:
        delta_time = float(reference_times[first_positive])
        initial_slopes.append(
            [
                value["increment_state"][first_positive] / delta_time,
                value["increment_f"][first_positive] / delta_time,
                value["increment_gram"][first_positive] / delta_time,
                value["increment_loss"][first_positive] / delta_time,
                max(
                    value["increment_f"][first_positive] / S_f,
                    value["increment_gram"][first_positive] / S_G,
                )
                / delta_time,
            ]
        )
    arrays[f"{prefix}_initial_slope"] = np.asarray(initial_slopes)


def _velocity_components(value: Any) -> Array:
    return np.asarray([value.Bdot, value.adot, value.cdot, value.total])


def _validated_lift_consistency_path(
    values: Sequence[Any], checkpoint_count: int, tag: str
) -> Array:
    """Return one finite checkpoint-by-component lift-consistency path."""

    result = np.asarray(values, dtype=float)
    expected = (int(checkpoint_count), len(GENERATOR_COMPONENT_NAMES))
    if result.shape != expected:
        raise RuntimeError(
            f"generator lift-consistency shape mismatch for {tag}: "
            f"{result.shape}, expected {expected}"
        )
    if not np.all(np.isfinite(result)):
        raise FloatingPointError(
            f"nonfinite generator lift consistency for {tag}"
        )
    return result


def _observable_components(value: Any) -> Array:
    # Loss is never mixed into the primary f/G generator metric.
    return np.asarray([value.f, value.grams])


def _normalized_observable_defect(
    value: Any, protocol: Mapping[str, Any]
) -> Array:
    f_difference = value.left.f - value.right.f
    gram_difference = value.left.grams - value.right.grams
    f_scaled = float(np.linalg.norm(f_difference)) / float(
        protocol["norms"]["S_f"]
    )
    gram_scaled = float(
        np.max(
            np.linalg.norm(
                gram_difference.reshape(gram_difference.shape[0], -1),
                axis=1,
            )
        )
    ) / float(protocol["norms"]["S_G"])
    return np.asarray([f_scaled, gram_scaled, max(f_scaled, gram_scaled)])


def _basis_components(
    value: Any, protocol: Mapping[str, Any]
) -> Array:
    return np.concatenate(
        (
            np.asarray([value.state_tail, value.generator_tail]),
            _velocity_components(value.feedback),
            _observable_components(value.observable_defect),
            _normalized_observable_defect(
                value.observable_defect, protocol
            ),
        )
    )


GENERATOR_COMPONENT_NAMES = (
    "Bdot",
    "adot",
    "cdot",
    "total",
)
OBSERVABLE_COMPONENT_NAMES = (
    "f",
    "grams",
)
NORMALIZED_OBSERVABLE_COMPONENT_NAMES = (
    "f_over_Sf",
    "sup_depth_gram_over_SG",
    "maximum",
)
BASIS_COMPONENT_NAMES = (
    "state_tail",
    "generator_tail",
    "feedback_Bdot",
    "feedback_adot",
    "feedback_cdot",
    "feedback_total",
    "observable_f",
    "observable_grams",
    "observable_f_over_Sf",
    "observable_sup_depth_gram_over_SG",
    "observable_maximum",
)


def _resolution_arrays(config: Mapping[str, Any]) -> dict[str, Array]:
    return {
        "numerical_resolution_axis_ascii": np.asarray(
            str(config["resolution_axis"]), dtype="S16"
        ),
        "numerical_resolution_family_ascii": np.asarray(
            str(config["resolution_family"]), dtype="S48"
        ),
        "numerical_resolution_is_primary": np.asarray(
            bool(config["resolution_is_primary"]), dtype=np.uint8
        ),
        "numerical_resolution_base_order": np.asarray(
            int(config["base_order"]), dtype=np.int64
        ),
        "numerical_resolution_M": np.asarray(
            int(config["M"]), dtype=np.int64
        ),
        "numerical_resolution_N": np.asarray(
            int(config["N"]), dtype=np.int64
        ),
        "numerical_resolution_R": np.asarray(
            int(config["R"]), dtype=np.int64
        ),
        "numerical_resolution_dt": np.asarray(float(config["dt"])),
        "numerical_resolution_seed": np.asarray(
            int(config["seed"]), dtype=np.int64
        ),
    }


def _validate_generator_config(
    protocol: Mapping[str, Any], args: argparse.Namespace
) -> dict[str, Any]:
    if args.max_level not in (35, 70):
        raise ValueError("generator max-level must be 35 or 70")
    if args.max_level == 35 and args.allow_conditional_p70:
        raise ValueError(
            "--allow-conditional-p70 is valid only for a max-level=70 "
            "generator job"
        )
    if args.max_level == 70 and not args.allow_conditional_p70:
        raise ValueError("P=70 generator extension requires explicit authorization")
    if args.max_level == 70:
        p70 = protocol["stage_0_integrity_and_numerics"][
            "P70_conditional_extension"
        ]
        numerical = _validate_resolution_inventory(
            protocol,
            p70["numerical_resolution"],
            args,
            label="conditional P70 generator",
            family="conditional_P70_nested",
        )
    else:
        numerical = _validate_structural_resolution(
            protocol, "stage_4_generator_consistency", args
        )
    levels = [5, 15, 35]
    pairs = [
        list(map(int, pair))
        for pair in protocol["stage_4_generator_consistency"]["pairs"]
    ]
    if args.max_level == 70:
        levels.append(70)
        pairs.append([35, 70])
    return {
        **numerical,
        "levels": levels,
        "pairs": pairs,
        "max_level": int(args.max_level),
        "conditional_p70_authorized": bool(args.allow_conditional_p70),
        "checkpoints": list(
            protocol["stage_4_generator_consistency"]["checkpoints"]
        ),
        "shadow_horizons": list(
            protocol["stage_4_generator_consistency"]["shadow_horizons"]
        ),
    }


def _run_generator(
    protocol: Mapping[str, Any],
    config: Mapping[str, Any],
) -> tuple[dict[str, Array], dict[str, Any]]:
    stage = protocol["stage_4_generator_consistency"]
    levels = tuple(int(value) for value in config["levels"])
    pairs = tuple(tuple(int(x) for x in pair) for pair in config["pairs"])
    checkpoints = np.asarray(config["checkpoints"], dtype=float)
    largest_level = max(levels)
    common.preflight_pde_memory(
        N=int(config["N"]),
        M=int(config["M"]),
        R=int(config["R"]),
        P=largest_level,
        retained_state_equivalents=(
            3.0
            + sum(level for level in levels if level < largest_level)
            / largest_level
            + 2.0
        ),
    )
    family = _make_family(
        protocol,
        levels=levels,
        N=int(config["N"]),
        R=int(config["R"]),
        seed=int(config["seed"]),
        base_order=int(config["base_order"]),
    )
    states = {
        level: initialize_pde(family.spec(level), family.quadrature(level))
        for level in levels
    }
    arrays: dict[str, Array] = {
        "checkpoints": checkpoints,
        "levels": np.asarray(levels, dtype=np.int64),
        "pairs": np.asarray(pairs, dtype=np.int64),
        "generator_component_names_ascii": np.asarray(
            GENERATOR_COMPONENT_NAMES, dtype="S16"
        ),
        "lift_consistency_component_names_ascii": np.asarray(
            GENERATOR_COMPONENT_NAMES, dtype="S16"
        ),
        "observable_component_names_ascii": np.asarray(
            OBSERVABLE_COMPONENT_NAMES, dtype="S16"
        ),
        "normalized_observable_component_names_ascii": np.asarray(
            NORMALIZED_OBSERVABLE_COMPONENT_NAMES, dtype="S32"
        ),
        "basis_component_names_ascii": np.asarray(
            BASIS_COMPONENT_NAMES, dtype="S24"
        ),
        "shadow_initial_slope_names_ascii": np.asarray(
            (
                "state",
                "f",
                "grams",
                "loss",
                "normalized_observable",
            ),
            dtype="S24",
        ),
    }
    arrays.update(_resolution_arrays(config))
    pair_records: dict[str, dict[str, list[Any]]] = {}
    for low, high in pairs:
        tag = f"P{low}_Q{high}"
        pair_records[tag] = {
            "lift_consistency": [],
            "R_out_lift": [],
            "R_out_high_state": [],
            "R_back": [],
            "lift_observable": [],
            "lift_observable_primary": [],
            "back_observable": [],
            "back_observable_primary": [],
            "lift_full_observable": [],
            "lift_full_observable_primary": [],
            "back_full_observable": [],
            "back_full_observable_primary": [],
        }
        for horizon in config["shadow_horizons"]:
            pair_records[tag][f"shadow_{float(horizon):.3f}"] = []

    basis_spec = stage["basis_diagnostics"]
    basis_level = 35
    rank = int(basis_spec["rank"])
    hermite_basis = hermite_subspace(basis_level, rank)
    random_seeds = tuple(int(seed) for seed in basis_spec["random_seeds"])
    random_bases = tuple(
        random_subspace(basis_level, rank, seed=seed)
        for seed in random_seeds
    )
    pilot_times = tuple(float(t) for t in basis_spec["POD_pilot_times"])
    heldout_times = tuple(float(t) for t in basis_spec["POD_heldout_times"])
    pilot_states: list[PDEState] = []
    pod_basis: Array | None = None
    hermite_records: list[Array] = []
    random_records: list[list[Array]] = [[] for _ in random_seeds]
    pod_records: list[Array] = []

    current = 0.0
    tolerance = 128 * np.finfo(float).eps * max(1.0, checkpoints[-1])
    for checkpoint in checkpoints:
        while current < checkpoint - tolerance:
            step = min(float(config["dt"]), float(checkpoint - current))
            for level in levels:
                states[level] = rk4_step(
                    states[level],
                    step,
                    family.spec(level),
                    family.quadrature(level),
                )
            current += step

        for level in levels:
            observable = observe(
                states[level],
                family.spec(level),
                family.quadrature(level),
            )
            for name, value in (
                ("f", observable.f),
                ("loss", observable.loss),
                ("grams", observable.grams),
                ("theta_min", observable.theta_min),
            ):
                key = f"P{level}_{name}"
                arrays.setdefault(key, [])
                arrays[key].append(np.asarray(value))

        for low, high in pairs:
            tag = f"P{low}_Q{high}"
            diagnostic = generator_diagnostics(
                states[low],
                states[high],
                family.spec(low),
                family.spec(high),
                family.quadrature(low),
                family.quadrature(high),
            )
            record = pair_records[tag]
            record["lift_consistency"].append(
                _velocity_components(diagnostic.lift_consistency)
            )
            record["R_out_lift"].append(
                diagnostic.lift_outgoing_high_cdot
            )
            record["R_out_high_state"].append(
                diagnostic.outgoing_high_cdot
            )
            record["R_back"].append(
                _velocity_components(diagnostic.high_to_low_feedback)
            )
            record["lift_observable"].append(
                _observable_components(diagnostic.lift_observable_defect)
            )
            record["lift_observable_primary"].append(
                _normalized_observable_defect(
                    diagnostic.lift_observable_defect, protocol
                )
            )
            record["back_observable"].append(
                _observable_components(
                    diagnostic.feedback_observable_defect
                )
            )
            record["back_observable_primary"].append(
                _normalized_observable_defect(
                    diagnostic.feedback_observable_defect, protocol
                )
            )
            record["lift_full_observable"].append(
                _observable_components(
                    diagnostic.lift_full_observable_defect
                )
            )
            record["lift_full_observable_primary"].append(
                _normalized_observable_defect(
                    diagnostic.lift_full_observable_defect, protocol
                )
            )
            record["back_full_observable"].append(
                _observable_components(
                    diagnostic.feedback_full_observable_defect
                )
            )
            record["back_full_observable_primary"].append(
                _normalized_observable_defect(
                    diagnostic.feedback_full_observable_defect, protocol
                )
            )
            for horizon in config["shadow_horizons"]:
                shadow = _shadow_errors(
                    states[high],
                    family.spec(low),
                    family.spec(high),
                    family.quadrature(low),
                    family.quadrature(high),
                    horizon=float(horizon),
                    dt=float(config["dt"]),
                    sample_dt=float(stage["diagnostic_time_step"]),
                )
                record[f"shadow_{float(horizon):.3f}"].append(shadow)

        high35 = states[basis_level]
        if any(np.isclose(checkpoint, value) for value in pilot_times):
            pilot_states.append(high35.copy())
            if np.isclose(checkpoint, max(pilot_times)):
                pod_basis = trajectory_pod_subspace(
                    pilot_states,
                    family.quadrature(basis_level),
                    rank,
                )
                pilot_states.clear()
        if any(np.isclose(checkpoint, value) for value in heldout_times):
            if pod_basis is None:
                raise RuntimeError("POD basis was not fit before held-out use")
            hermite_records.append(
                _basis_components(
                    basis_diagnostic(
                        high35,
                        family.spec(basis_level),
                        family.quadrature(basis_level),
                        hermite_basis,
                    ),
                    protocol,
                )
            )
            for index, basis in enumerate(random_bases):
                random_records[index].append(
                    _basis_components(
                        basis_diagnostic(
                            high35,
                            family.spec(basis_level),
                            family.quadrature(basis_level),
                            basis,
                        ),
                        protocol,
                    )
                )
            pod_records.append(
                _basis_components(
                    basis_diagnostic(
                        high35,
                        family.spec(basis_level),
                        family.quadrature(basis_level),
                        pod_basis,
                    ),
                    protocol,
                )
            )

    for key, values in tuple(arrays.items()):
        if isinstance(values, list):
            arrays[key] = np.stack(values)
    for tag, record in pair_records.items():
        for name in (
            "lift_consistency",
            "R_out_lift",
            "R_out_high_state",
            "R_back",
            "lift_observable",
            "lift_observable_primary",
            "back_observable",
            "back_observable_primary",
            "lift_full_observable",
            "lift_full_observable_primary",
            "back_full_observable",
            "back_full_observable_primary",
        ):
            arrays[f"{tag}_{name}"] = np.asarray(record[name])
        arrays[f"{tag}_lift_consistency"] = (
            _validated_lift_consistency_path(
                record["lift_consistency"], checkpoints.size, tag
            )
        )
        for horizon in config["shadow_horizons"]:
            shadow_records = record[f"shadow_{float(horizon):.3f}"]
            horizon_tag = f"h{int(round(1000 * float(horizon))):04d}"
            _add_shadow_archive_arrays(
                arrays,
                tag=tag,
                horizon_tag=horizon_tag,
                shadow_records=shadow_records,
                protocol=protocol,
            )

    arrays.update(
        {
            "basis_reference_level": np.asarray(basis_level),
            "basis_rank": np.asarray(rank),
            "basis_heldout_times": np.asarray(heldout_times),
            "basis_random_seeds": np.asarray(random_seeds, dtype=np.int64),
            "basis_hermite_coefficients": hermite_basis,
            "basis_random_coefficients": np.stack(random_bases),
            "basis_pod_coefficients": np.asarray(pod_basis),
            "basis_hermite_diagnostics": np.stack(hermite_records),
            "basis_random_diagnostics": np.stack(
                [np.stack(values) for values in random_records]
            ),
            "basis_pod_diagnostics": np.stack(pod_records),
        }
    )
    detail = {
        "generator_semantics": {
            "R_out_lift": (
                "weighted norm of high modes of F_Q(iota_P Y_P)"
            ),
            "R_back": (
                "weighted component norms of Pi_P F_Q(Y_Q) "
                "minus F_P(Pi_P Y_Q)"
            ),
            "observable": (
                "primary defect is max(||delta f||/S_f, "
                "max_s||delta G(s)||_F/S_G); loss is not mixed into it"
            ),
        },
        "shadow_semantics": (
            "raw errors retain the t=0 projection mismatch; increment errors "
            "subtract the signed/vector t=0 mismatch before taking a norm; "
            "initial slopes use the first strictly positive saved time; "
            f"the normalized observable norm is "
            f"{SHADOW_OBSERVABLE_NORM_SEMANTICS}"
        ),
        "basis_semantics": (
            "Hermite, eight seeded random bases, and one POD basis are all "
            "evaluated only at held-out times. POD coefficients use only "
            "the predeclared pilot states at t=0,.25,.5."
        ),
        "online_state_policy": (
            "full checkpoint states are not archived; diagnostics are "
            "computed online at the six declared checkpoints"
        ),
        "numerical_resolution_semantics": (
            "the residual, observable-generator, and shadow arrays in this "
            "archive are compared directly across the primary/M/N/R/dt "
            "structural configurations; Stage-0 curve Cauchy checks do not "
            "resolve this gate"
        ),
        "nested_pair_configuration_semantics": (
            "every level and every generator-defect pair in this archive "
            "uses the exact same M/N/R/dt/scramble configuration; for a "
            "conditional P70 archive the 15-to-35 comparator must be read "
            "from this archive, never borrowed from the active P35 family"
        ),
        "quadrature_sha256": {
            f"P{level}_phi": common._sha256_array(
                family.quadrature(level).phi
            )
            for level in levels
        }
        | {
            f"P{level}_epsilon": common._sha256_array(
                family.quadrature(level).epsilon
            )
            for level in levels
        }
        | {
            "raw_master_epsilon": common._sha256_array(family.raw_epsilon)
        },
    }
    return arrays, detail


def _conditional_gain_declaration(
    protocol: Mapping[str, Any], *, required: bool
) -> Mapping[str, Any] | None:
    """Validate the frozen declaration for the sole conditional gain pair."""

    stage = protocol["stage_5_amplification"]
    declaration = stage.get("conditional_P70_extension")
    if declaration is None:
        if required:
            raise ValueError(
                "conditional P70 gain extension is not preregistered"
            )
        return None
    if not isinstance(declaration, Mapping):
        raise ValueError("conditional P70 gain declaration must be a mapping")
    if tuple(
        int(value) for value in declaration.get("residual_pair", ())
    ) != (35, 70):
        raise ValueError(
            "conditional P70 gain declaration must contain exactly "
            "residual_pair [35, 70]"
        )
    exact_strings = {
        "authorization_flag": "--allow-conditional-p70",
        "numerical_resolution_source": (
            "stage_0_integrity_and_numerics.P70_conditional_extension."
            "numerical_resolution"
        ),
        "time_grid_source": "stage_5_amplification.time_grids",
        "nonlinear_amplitude_source": (
            "stage_5_amplification."
            "symmetric_nonlinear_amplitude_magnitudes"
        ),
    }
    for key, expected in exact_strings.items():
        if declaration.get(key) != expected:
            raise ValueError(
                f"conditional P70 gain {key} must equal {expected!r}"
            )
    for key in ("trigger", "interpretation"):
        if not isinstance(declaration.get(key), str) or not declaration[key]:
            raise ValueError(
                f"conditional P70 gain {key} must be a nonempty string"
            )

    p70_resolution = protocol["stage_0_integrity_and_numerics"][
        "P70_conditional_extension"
    ]["numerical_resolution"]
    expected_primary = len(p70_resolution["primary"]["scramble_seeds"])
    expected_refinements = len(
        p70_resolution["one_axis_refinements_at_seed_20260723"]
    )
    execution = declaration.get("execution_inventory")
    if not isinstance(execution, Mapping):
        raise ValueError(
            "conditional P70 gain execution_inventory must be a mapping"
        )
    expected_execution = {
        "primary_jobs_per_time_grid": expected_primary,
        "one_axis_refinement_jobs_per_time_grid": expected_refinements,
        "time_grids": ["primary", "refined"],
        "jobs_total": 2 * (expected_primary + expected_refinements),
        "joint_corner": None,
    }
    for key, expected in expected_execution.items():
        if key not in execution or execution[key] != expected:
            raise ValueError(
                "conditional P70 gain execution inventory mismatch for "
                f"{key}: expected {expected!r}"
            )
    return declaration


def _validate_gain_config(
    protocol: Mapping[str, Any], args: argparse.Namespace
) -> dict[str, Any]:
    stage = protocol["stage_5_amplification"]
    declared_active_pairs = tuple(
        tuple(int(value) for value in pair)
        for pair in stage["residual_pairs"]
    )
    if declared_active_pairs != ((5, 35), (15, 35)):
        raise ValueError(
            "active Stage-5 gain pairs must be exactly "
            "[(5, 35), (15, 35)]"
        )
    if tuple(int(value) for value in stage["low_levels"]) != (5, 15):
        raise ValueError("active Stage-5 low levels must be exactly [5, 15]")
    low_level = int(args.low_level)
    requested_high = getattr(args, "high_level", None)
    if requested_high is not None:
        requested_high = int(requested_high)
    conditional_authorized = bool(
        getattr(args, "allow_conditional_p70", False)
    )

    if low_level == 35:
        if not conditional_authorized:
            raise ValueError(
                "P=35 from Q=70 gain extension requires explicit "
                "--allow-conditional-p70 authorization"
            )
        declaration = _conditional_gain_declaration(
            protocol, required=True
        )
        assert declaration is not None
        if requested_high is not None and requested_high != 70:
            raise ValueError(
                "conditional P70 gain supports exactly low=35, high=70"
            )
        p70_resolution = protocol["stage_0_integrity_and_numerics"][
            "P70_conditional_extension"
        ]["numerical_resolution"]
        numerical = _validate_resolution_inventory(
            protocol,
            p70_resolution,
            args,
            label="conditional P70 gain",
            family="conditional_P70_gain",
        )
        high_level = 70
        closure_step_scope = str(
            declaration.get(
                "interpretation",
                "next measured closure step only; not a P-to-infinity claim",
            )
        )
    else:
        if conditional_authorized:
            raise ValueError(
                "--allow-conditional-p70 is valid only for the exact "
                "low=35, high=70 gain pair"
            )
        active_pairs = [
            pair for pair in declared_active_pairs if pair[0] == low_level
        ]
        if low_level not in stage["low_levels"] or len(active_pairs) != 1:
            raise ValueError("gain low level is not preregistered")
        high_level = active_pairs[0][1]
        if requested_high is not None and requested_high != high_level:
            raise ValueError(
                f"gain pair low={low_level}, high={requested_high} is not "
                "preregistered"
            )
        numerical = _validate_structural_resolution(
            protocol, "stage_5_amplification", args
        )
        closure_step_scope = (
            "active finite residual-dictionary closure measurement"
        )

    if args.time_grid not in ("primary", "refined"):
        raise ValueError("gain time grid is not preregistered")
    grid = list(map(float, stage["time_grids"][args.time_grid]))
    if not np.isclose(grid[0], 0.0) or not np.isclose(
        grid[-1], stage["horizon"]
    ):
        raise ValueError("gain time grid must span the complete horizon")
    if args.time_grid == "primary" and grid != list(stage["impulse_times"]):
        raise ValueError("primary gain grid must equal declared impulse_times")
    return {
        **numerical,
        "low_level": low_level,
        "high_level": high_level,
        "conditional_p70_authorized": conditional_authorized,
        "closure_step_scope": closure_step_scope,
        "horizon": float(stage["horizon"]),
        "time_grid_name": str(args.time_grid),
        "source_times": grid,
        "observation_times": grid,
        "residual_snapshot_times": grid,
        "nonlinear_amplitudes": list(
            map(float, stage["symmetric_nonlinear_amplitude_magnitudes"])
        ),
        "observable_blocks": ["f", "grams"],
    }


def _run_gain(
    protocol: Mapping[str, Any],
    config: Mapping[str, Any],
) -> tuple[dict[str, Array], dict[str, Any]]:
    low_level = int(config["low_level"])
    high_level = int(config["high_level"])
    source_times = np.asarray(config["source_times"], dtype=float)
    observation_times = np.asarray(config["observation_times"], dtype=float)
    family = _make_family(
        protocol,
        levels=(low_level, high_level),
        N=int(config["N"]),
        R=int(config["R"]),
        seed=int(config["seed"]),
        base_order=int(config["base_order"]),
    )
    low_spec = family.spec(low_level)
    high_spec = family.spec(high_level)
    low_quadrature = family.quadrature(low_level)
    high_quadrature = family.quadrature(high_level)
    common.preflight_pde_memory(
        N=int(config["N"]),
        M=int(config["M"]),
        R=int(config["R"]),
        P=high_level,
        retained_state_equivalents=(
            source_times.size * low_level / high_level
        ),
    )
    common.preflight_pde_memory(
        N=int(config["N"]),
        M=int(config["M"]),
        R=int(config["R"]),
        P=low_level,
        retained_state_equivalents=(2.0 * source_times.size),
    )

    base_initial = initialize_pde(low_spec, low_quadrature)
    high_state = initialize_pde(high_spec, high_quadrature)
    residuals: list[PDEState] = []
    current = 0.0
    tolerance = 128 * np.finfo(float).eps * max(
        1.0, float(config["horizon"])
    )
    for target in source_times:
        while current < target - tolerance:
            step = min(float(config["dt"]), float(target - current))
            high_state = rk4_step(
                high_state, step, high_spec, high_quadrature
            )
            current += step
        residuals.append(
            projected_back_residual(
                high_state,
                low_spec,
                high_spec,
                low_quadrature,
                high_quadrature,
            )
        )
    # The high-level state has served its only purpose and is not archived.
    del high_state
    gc.collect()

    scales = ObservableScales(
        f=float(protocol["norms"]["S_f"]),
        grams=float(protocol["norms"]["S_G"]),
    )
    result = stage5_serializable_result(
        base_initial,
        (),
        source_times,
        low_spec,
        high_spec,
        low_quadrature,
        high_quadrature,
        impulse_times=source_times,
        observation_times=observation_times,
        max_step=float(config["dt"]),
        nonlinear_amplitudes=config["nonlinear_amplitudes"],
        observable_blocks=config["observable_blocks"],
        scales=scales,
        precomputed_residuals=residuals,
        serialize_residual_states=False,
    )
    helper = result.arrays
    helper_sources = np.asarray(helper["source_times"], dtype=float)
    if not np.array_equal(helper_sources, source_times):
        raise RuntimeError("all-source gain helper changed the source-time grid")
    group_gains = np.asarray(helper["group_response_gains"], dtype=float)
    if group_gains.shape[0] != source_times.size:
        raise RuntimeError("all-source gain helper returned the wrong group count")
    source_gain_array = np.max(group_gains, axis=(1, 2))
    impulse_times = np.asarray(helper["impulse_times"], dtype=float)
    column_gains = np.asarray(helper["column_gains"], dtype=float)
    source_atom_gains = np.asarray(
        [
            np.max(column_gains[np.isclose(impulse_times, source)])
            for source in source_times
        ]
    )
    maximizing_indices = np.asarray(
        helper["maximizing_indices"], dtype=np.int64
    )
    selected_source = int(maximizing_indices[1])
    if selected_source != int(np.argmax(source_gain_array)):
        raise RuntimeError("all-source gain helper selected an inconsistent source")
    primary_gain = float(helper["primary_residual_subspace_gain"])
    if not np.isclose(
        primary_gain,
        float(np.max(source_gain_array)),
        rtol=5e-13,
        atol=5e-15,
    ):
        raise RuntimeError("global and sourcewise residual gains disagree")

    coefficients = np.asarray(helper["residual_basis_coefficients"], dtype=float)
    reconstruction = np.asarray(
        helper["residual_basis_reconstruction_error"], dtype=float
    )
    residual_norms = np.asarray(helper["residual_snapshot_norms"], dtype=float)
    relative_reconstruction = reconstruction / np.maximum(
        residual_norms, 1e-15
    )
    residual_l1_integral = float(
        np.trapezoid(residual_norms, source_times)
    )
    residual_l2_time = float(
        np.sqrt(np.trapezoid(residual_norms**2, source_times))
    )
    output: dict[str, Array] = {
        "residual_pair_levels": np.asarray(
            [low_level, high_level], dtype=np.int64
        ),
        "conditional_p70_authorized": np.asarray(
            bool(config["conditional_p70_authorized"]), dtype=np.uint8
        ),
        "residual_snapshot_times": np.asarray(
            helper["residual_snapshot_times"]
        ),
        "residual_snapshot_norms": residual_norms,
        "residual_basis_weighted_gram": np.asarray(
            helper["residual_basis_weighted_gram"]
        ),
        "observable_block_sizes": np.asarray(
            helper["observable_block_sizes"]
        ),
        "source_times": source_times,
        "observation_times": observation_times,
        "impulse_times": impulse_times,
        "direction_norms": np.asarray(helper["direction_norms"]),
        "block_response_norms": np.asarray(
            helper["block_response_norms"]
        ),
        "group_response_gains": group_gains,
        "column_gains": column_gains,
        "flattened_response_columns": np.asarray(
            helper["flattened_response_columns"]
        ),
        "source_primary_residual_subspace_gain": source_gain_array,
        "source_atom_l1_gain": source_atom_gains,
        "primary_residual_subspace_gain": np.asarray(primary_gain),
        "atom_l1_gain": np.asarray(helper["atom_l1_gain"]),
        "maximizing_indices": maximizing_indices,
        "maximizing_atom_coefficients": np.asarray(
            helper["maximizing_atom_coefficients"]
        ),
        "secondary_l2_singular_values": np.asarray(
            helper["secondary_l2_singular_values"]
        ),
        "secondary_l2_left_vectors": np.asarray(
            helper["secondary_l2_left_vectors"]
        ),
        "secondary_l2_right_vectors": np.asarray(
            helper["secondary_l2_right_vectors"]
        ),
        "secondary_l2_time_weights": np.asarray(
            helper["secondary_l2_time_weights"]
        ),
        "residual_basis_reconstruction_coefficients": coefficients,
        "residual_basis_reconstruction_error": reconstruction,
        "residual_basis_relative_reconstruction_error": (
            relative_reconstruction
        ),
        "residual_state_norm_L1_time_integral": np.asarray(
            residual_l1_integral
        ),
        "residual_state_norm_L2_time": np.asarray(residual_l2_time),
        "amplified_residual_bound_discrete": np.asarray(
            primary_gain * residual_l1_integral
        ),
    }
    output.update(
        {
            key: np.asarray(value)
            for key, value in helper.items()
            if key.startswith("nonlinear_")
        }
    )
    output.update(_resolution_arrays(config))
    detail = {
        "primary_gain_scope": (
            "exact finite group-L1(time)/L2(direction)-to-Linf(f,G) "
            "gain on the selected residual/time dictionary; not full-state"
        ),
        "source_time_assembly": (
            "one all-source compact helper call; exact global gain is the "
            "maximum of the source-group spectral gains"
        ),
        "response_memory_policy": (
            "low-level primal/tangent states discarded after compact f/G "
            "response extraction; high-level states are projected online "
            "and never archived; full residual/basis state arrays are also "
            "omitted"
        ),
        "memory_preflight_semantics": (
            "separate fail-closed guards cover high-level integration while "
            "retaining every low residual snapshot, and low-level tangent "
            "analysis while retaining both the residual snapshots and a "
            "worst-case direction for each snapshot"
        ),
        "residual_pair": [low_level, high_level],
        "conditional_p70_authorized": bool(
            config["conditional_p70_authorized"]
        ),
        "closure_step_scope": str(config["closure_step_scope"]),
        "selected_nonlinear_source_index": selected_source,
        "selected_nonlinear_source_time": float(
            source_times[selected_source]
        ),
        "stage5_helper_detail": dict(result.detail),
        "nonlinear_validation_scope": (
            "finite-amplitude symmetric restart diagnostic on the single "
            "globally maximizing finite-dictionary direction; it is not a "
            "full-state stability certificate"
        ),
        "residual_integral_semantics": (
            "trapezoidal integral of the measured weighted state L2 norm; "
            "both L1-in-time and secondary L2-in-time summaries are saved"
        ),
        "amplified_bound_semantics": (
            "primary finite-dictionary gain times the sampled trapezoidal "
            "L1-time residual norm; reconstruction and time-grid differences "
            "remain separate ledger terms"
        ),
        "observable_scales": {
            "f": float(protocol["norms"]["S_f"]),
            "grams": float(protocol["norms"]["S_G"]),
        },
        "time_grid_name": config["time_grid_name"],
        "numerical_resolution_semantics": (
            "the residual integral, finite-dictionary gain, and amplified "
            "product in this archive are compared directly across the "
            "primary/M/N/R/dt Stage-5 configurations; Stage-0 curve Cauchy "
            "checks do not resolve this gate"
        ),
        "quadrature_sha256": {
            f"P{low_level}_phi": common._sha256_array(
                low_quadrature.phi
            ),
            f"P{low_level}_epsilon": common._sha256_array(
                low_quadrature.epsilon
            ),
            f"P{high_level}_phi": common._sha256_array(
                high_quadrature.phi
            ),
            f"P{high_level}_epsilon": common._sha256_array(
                high_quadrature.epsilon
            ),
            "raw_master_epsilon": common._sha256_array(family.raw_epsilon),
        },
    }
    return output, detail


def _tail_boundaries(protocol: Mapping[str, Any]) -> tuple[tuple[float, float], ...]:
    ends = tuple(
        float(value)
        for value in protocol["stage_6_all_time_tail"]["horizon_ladder"]
    )
    starts = (0.0,) + ends[:-1]
    return tuple(zip(starts, ends))


def _validate_tail_pde_config(
    protocol: Mapping[str, Any], args: argparse.Namespace
) -> dict[str, Any]:
    primary = _primary_pde_config(protocol)
    for key in ("N", "R"):
        if int(getattr(args, key)) != int(primary[key]):
            raise ValueError(
                f"tail PDE {key} must equal the primary value {primary[key]}"
            )
    if float(args.dt) != float(primary["dt"]):
        raise ValueError(
            "tail PDE dt must equal the primary value "
            f"{primary['dt']}"
        )
    if args.base_order != PRIMARY_BASE_ORDER:
        raise ValueError("tail PDE is frozen to base order 5")
    ladder = protocol["stage_0_integrity_and_numerics"]["nested_ladder"]
    if args.seed not in ladder["scramble_seeds"]:
        raise ValueError("tail PDE seed is not declared")
    matches = [
        pair
        for pair in _tail_boundaries(protocol)
        if pair[1] == float(args.block_end)
    ]
    if len(matches) != 1:
        raise ValueError("block-end is not in the declared horizon ladder")
    start, end = matches[0]
    if start == 0.0 and args.restart_from is not None:
        raise ValueError("the first PDE tail block may not have a restart")
    if start > 0.0 and args.restart_from is None:
        raise ValueError("later PDE tail blocks require --restart-from")
    config: dict[str, Any] = {
        **primary,
        "P": 5,
        "seed": int(args.seed),
        "block_start": start,
        "block_end": end,
        "sample_dt": float(protocol["norms"]["time_sampling"]),
        "finite_horizon_only": True,
    }
    if args.restart_from is not None:
        previous = common.load_sealed_stage_archive(
            args.restart_from,
            required_config_keys=(
                "P",
                "N",
                "R",
                "dt",
                "base_order",
                "seed",
                "block_end",
            ),
            required_arrays=(
                "endpoint_time",
                "endpoint_B",
                "endpoint_a",
                "endpoint_c",
            ),
            expected_stage="tail_pde",
            expected_protocol_sha256=common._sha256_file(
                common.PROTOCOL_PATH
            ),
        )
        previous_config = previous.config
        previous_boundaries = {
            block_end: block_start
            for block_start, block_end in _tail_boundaries(protocol)
        }
        expected_previous = {
            **primary,
            "P": 5,
            "seed": int(args.seed),
            "block_start": previous_boundaries[start],
            "block_end": start,
            "sample_dt": float(protocol["norms"]["time_sampling"]),
            "finite_horizon_only": True,
        }
        previous_restart = previous_config.get("restart_seal_sha256")
        if expected_previous["block_start"] == 0.0:
            if previous_restart is not None:
                raise ValueError(
                    "initial restart archive has a predecessor seal"
                )
        elif not common._is_sha256(previous_restart):
            raise ValueError(
                "noninitial restart archive lacks a predecessor seal"
            )
        expected_previous["restart_seal_sha256"] = previous_restart
        expected_previous["canonical_model"] = common._jsonable(
            common._canonical_model(protocol)
        )
        if common._canonical_json(previous_config) != common._canonical_json(
            expected_previous
        ):
            raise ValueError(
                "restart archive config is not exactly the declared "
                "immediately prior block"
            )
        endpoint_time = np.asarray(previous.arrays["endpoint_time"])
        if endpoint_time.shape != () or float(endpoint_time) != start:
            raise ValueError("restart endpoint time disagrees with its config")
        config["restart_seal_sha256"] = previous.metadata["seal_sha256"]
    else:
        config["restart_seal_sha256"] = None
    return config


def _load_tail_restart(
    path: Path,
    config: Mapping[str, Any],
    provenance: Mapping[str, Any],
) -> PDEState:
    archive = common.load_sealed_stage_archive(
        path,
        required_config_keys=(
            "P",
            "N",
            "R",
            "dt",
            "base_order",
            "seed",
            "block_end",
        ),
        required_arrays=(
            "endpoint_time",
            "endpoint_B",
            "endpoint_a",
            "endpoint_c",
        ),
        expected_stage="tail_pde",
        expected_protocol_sha256=str(provenance["protocol_sha256"]),
        expected_source_hashes=provenance["source_hashes"],
    )
    if archive.metadata["seal_sha256"] != config["restart_seal_sha256"]:
        raise ValueError("restart archive seal changed after validation")
    return PDEState(
        B=archive.arrays["endpoint_B"].copy(),
        a=archive.arrays["endpoint_a"].copy(),
        c=archive.arrays["endpoint_c"].copy(),
    )


def _run_tail_pde(
    protocol: Mapping[str, Any],
    config: Mapping[str, Any],
    *,
    restart_path: Path | None,
    provenance: Mapping[str, Any],
) -> tuple[dict[str, Array], dict[str, Any]]:
    family = _make_family(
        protocol,
        levels=(5,),
        N=int(config["N"]),
        R=int(config["R"]),
        seed=int(config["seed"]),
        base_order=int(config["base_order"]),
    )
    spec = family.spec(5)
    quadrature = family.quadrature(5)
    if restart_path is None:
        state = initialize_pde(spec, quadrature)
    else:
        state = _load_tail_restart(
            restart_path, config, provenance
        )
    expected_shape = (
        spec.depth_nodes,
        spec.base_points,
        spec.fast_points,
        spec.basis_size,
    )
    if state.c.shape != expected_shape:
        raise ValueError("restart endpoint state has the wrong PDE shape")

    start = float(config["block_start"])
    end = float(config["block_end"])
    relative_times = common._event_times(
        end - start, float(config["sample_dt"])
    )
    times = start + relative_times
    initial_observable = observe(state, spec, quadrature)
    f_values: list[Array] = []
    gram_values: list[Array] = []
    loss_values: list[float] = []
    theta_min_values: list[float] = []
    residual_values: list[float] = []
    f_drift: list[float] = []
    gram_drift: list[float] = []
    step_times: list[float] = []
    arclength_increment: list[float] = []
    current = start
    tolerance = 128 * np.finfo(float).eps * max(1.0, end)
    for target in times:
        while current < target - tolerance:
            step = min(float(config["dt"]), float(target - current))
            previous = state
            state = rk4_step(state, step, spec, quadrature)
            current += step
            step_times.append(current)
            arclength_increment.append(
                float(state_difference_norm(state, previous, quadrature))
            )
        observable = observe(state, spec, quadrature)
        f_values.append(observable.f)
        gram_values.append(observable.grams)
        loss_values.append(observable.loss)
        theta_min_values.append(observable.theta_min)
        residual_values.append(observable.residual_norm)
        f_drift.append(
            float(np.linalg.norm(observable.f - initial_observable.f))
        )
        gram_drift.append(
            float(
                np.linalg.norm(
                    observable.grams - initial_observable.grams
                )
                / np.sqrt(observable.grams.shape[0])
            )
        )
    increments = np.asarray(arclength_increment)
    f_array = np.stack(f_values)
    gram_array = np.stack(gram_values)
    f_drift_array = np.asarray(f_drift)
    gram_drift_array = np.asarray(gram_drift)
    normalized_f_drift = np.linalg.norm(
        f_array - f_array[0], axis=1
    ) / float(protocol["norms"]["S_f"])
    gram_difference = gram_array - gram_array[0]
    normalized_gram_drift = np.max(
        np.linalg.norm(
            gram_difference.reshape(
                gram_difference.shape[0], gram_difference.shape[1], -1
            ),
            axis=2,
        ),
        axis=1,
    ) / float(protocol["norms"]["S_G"])
    normalized_observable_drift = np.maximum(
        normalized_f_drift, normalized_gram_drift
    )
    successive_f = np.linalg.norm(
        np.diff(f_array, axis=0), axis=1
    ) / float(protocol["norms"]["S_f"])
    successive_gram_raw = np.diff(gram_array, axis=0)
    successive_gram = np.max(
        np.linalg.norm(
            successive_gram_raw.reshape(
                successive_gram_raw.shape[0],
                successive_gram_raw.shape[1],
                -1,
            ),
            axis=2,
        ),
        axis=1,
    ) / float(protocol["norms"]["S_G"])
    normalized_total_variation = float(
        np.sum(np.maximum(successive_f, successive_gram))
    )
    arrays = {
        "times": times,
        "f": f_array,
        "grams": gram_array,
        "loss": np.asarray(loss_values),
        "theta_min": np.asarray(theta_min_values),
        "residual_norm": np.asarray(residual_values),
        "f_drift_from_block_start": f_drift_array,
        "gram_drift_from_block_start": gram_drift_array,
        "normalized_observable_drift_from_block_start": (
            normalized_observable_drift
        ),
        "arclength_step_times": np.asarray(step_times),
        "arclength_step_increment": increments,
        "arclength_cumulative": np.concatenate(
            (np.zeros(1), np.cumsum(increments))
        ),
        "block_arclength": np.asarray(np.sum(increments)),
        "block_normalized_observable_drift": np.asarray(
            normalized_observable_drift[-1]
        ),
        "block_normalized_observable_drift_sup": np.asarray(
            np.max(normalized_observable_drift)
        ),
        "block_normalized_observable_total_variation": np.asarray(
            normalized_total_variation
        ),
        "endpoint_time": np.asarray(end),
        "endpoint_B": state.B,
        "endpoint_a": state.a,
        "endpoint_c": state.c,
    }
    detail = {
        "arclength_semantics": (
            "sum of weighted state-increment norms at every accepted RK4 "
            "step; a convergent polygonal approximation to integral ||Ydot||. "
            "It is reported separately and is not compared directly with "
            "the 0.005 observable-tail allocation without a late-time gain."
        ),
        "restart_semantics": (
            "the exact hash-bound endpoint state of the immediately prior "
            "declared block, or canonical initialization for [0,2]"
        ),
        "interpretation": (
            "finite-horizon block evidence only; no literal all-time claim"
        ),
        "quadrature_sha256": {
            "phi": common._sha256_array(quadrature.phi),
            "epsilon": common._sha256_array(quadrature.epsilon),
            "raw_master_epsilon": common._sha256_array(family.raw_epsilon),
        },
    }
    return arrays, detail


def _dense_difference_norm(left: ParamState, right: ParamState) -> float:
    n = left.B.shape[0]
    depth = left.W.shape[0]
    if (
        left.B.shape != right.B.shape
        or left.W.shape != right.W.shape
        or left.a.shape != right.a.shape
    ):
        raise ValueError("dense states have incompatible shapes")
    squared = (
        np.sum((left.B - right.B) ** 2) / n
        + np.sum((left.a - right.a) ** 2) / n
        + np.sum((left.W - right.W) ** 2) / depth
    )
    return float(np.sqrt(max(float(squared), 0.0)))


def _dense_observe_tail(state: ParamState, spec: Any) -> dict[str, Any]:
    fields = forward_adjoint(state, spec)
    f = state.a @ fields.H[-1] / spec.n
    grams = np.einsum(
        "lnr,lns->lrs", fields.H, fields.H, optimize=True
    ) / spec.n
    theta = tangent_kernel(
        FieldState(state.W, state.a, fields.H, fields.P), spec
    )
    residual = f - spec.y
    return {
        "f": f,
        "grams": grams,
        "loss": float(0.5 * residual @ residual),
        "theta_min": float(np.linalg.eigvalsh(theta)[0]),
    }


def _validate_tail_dense_config(
    protocol: Mapping[str, Any], args: argparse.Namespace
) -> dict[str, Any]:
    stage = protocol["stage_6_all_time_tail"]["dense_diagnostic"]
    horizon = (
        float(stage["maximum_horizon"])
        if args.horizon is None
        else float(args.horizon)
    )
    if not 0 <= args.root_index < int(stage["roots"]):
        raise ValueError("dense tail root-index is outside the declared range")
    if horizon != float(stage["maximum_horizon"]):
        raise ValueError("dense tail horizon must equal the declared maximum")
    dt = float(protocol["stage_1_ordered_target"]["dt"])
    if float(args.dt) != dt:
        raise ValueError("dense tail dt must equal the canonical dense step")
    base_seed = int(protocol["error_ledger"]["bootstrap_seed"])
    root_seed = int(
        np.random.SeedSequence(
            [
                base_seed,
                STRUCTURAL_STAGE_CODES["tail_dense"],
                int(args.root_index),
            ]
        ).generate_state(1, dtype=np.uint64)[0]
    )
    return {
        "n": int(stage["n"]),
        "L": int(stage["L"]),
        "root_index": int(args.root_index),
        "root_seed": root_seed,
        "T": horizon,
        "dt": dt,
        "sample_dt": float(protocol["norms"]["time_sampling"]),
        "finite_horizon_only": True,
    }


def _run_tail_dense(
    protocol: Mapping[str, Any],
    config: Mapping[str, Any],
) -> tuple[dict[str, Array], dict[str, Any]]:
    model = common._canonical_model(protocol)
    spec = common._dense_spec(
        model,
        n=int(config["n"]),
        depth=int(config["L"]),
        seed=int(config["root_seed"]),
    )
    master = common.initialize_gaussian_master(
        n_max=spec.n,
        depth_max=spec.depth,
        input_dim=spec.X.shape[0],
        seed=int(config["root_seed"]),
    )
    state = common.materialize_coupled_state(master, spec)
    times = common._event_times(float(config["T"]), float(config["sample_dt"]))
    initial_observable = _dense_observe_tail(state, spec)
    f_values: list[Array] = []
    gram_values: list[Array] = []
    loss_values: list[float] = []
    theta_min_values: list[float] = []
    f_drift: list[float] = []
    gram_drift: list[float] = []
    step_times: list[float] = []
    increments: list[float] = []
    current = 0.0
    tolerance = 128 * np.finfo(float).eps * max(1.0, float(config["T"]))
    for target in times:
        while current < target - tolerance:
            step = min(float(config["dt"]), float(target - current))
            previous = state
            state = rk4_param_step(state, step, spec)
            current += step
            step_times.append(current)
            increments.append(_dense_difference_norm(state, previous))
        observable = _dense_observe_tail(state, spec)
        f_values.append(observable["f"])
        gram_values.append(observable["grams"])
        loss_values.append(observable["loss"])
        theta_min_values.append(observable["theta_min"])
        f_drift.append(
            float(
                np.linalg.norm(
                    observable["f"] - initial_observable["f"]
                )
            )
        )
        gram_drift.append(
            float(
                np.linalg.norm(
                    observable["grams"] - initial_observable["grams"]
                )
                / np.sqrt(observable["grams"].shape[0])
            )
        )
    increments_array = np.asarray(increments)
    block_pairs = tuple(
        pair
        for pair in _tail_boundaries(protocol)
        if pair[1] <= float(config["T"])
    )
    step_times_array = np.asarray(step_times)
    block_arclength: list[float] = []
    block_f_drift: list[float] = []
    block_gram_drift: list[float] = []
    block_normalized_drift: list[float] = []
    block_normalized_drift_sup: list[float] = []
    block_normalized_total_variation: list[float] = []
    block_theta_min: list[float] = []
    f_array = np.stack(f_values)
    gram_array = np.stack(gram_values)
    theta_array = np.asarray(theta_min_values)
    for start, end in block_pairs:
        step_mask = (step_times_array > start + 1e-13) & (
            step_times_array <= end + 1e-13
        )
        block_arclength.append(float(np.sum(increments_array[step_mask])))
        start_index = int(np.argmin(np.abs(times - start)))
        end_index = int(np.argmin(np.abs(times - end)))
        block_f_drift.append(
            float(np.linalg.norm(f_array[end_index] - f_array[start_index]))
        )
        block_gram_drift.append(
            float(
                np.linalg.norm(
                    gram_array[end_index] - gram_array[start_index]
                )
                / np.sqrt(gram_array.shape[1])
            )
        )
        time_mask = (times >= start - 1e-13) & (times <= end + 1e-13)
        block_f_path = f_array[time_mask]
        block_gram_path = gram_array[time_mask]
        normalized_f_path = np.linalg.norm(
            block_f_path - block_f_path[0], axis=1
        ) / float(protocol["norms"]["S_f"])
        block_gram_difference = block_gram_path - block_gram_path[0]
        normalized_gram_path = np.max(
            np.linalg.norm(
                block_gram_difference.reshape(
                    block_gram_difference.shape[0],
                    block_gram_difference.shape[1],
                    -1,
                ),
                axis=2,
            ),
            axis=1,
        ) / float(protocol["norms"]["S_G"])
        normalized_path = np.maximum(
            normalized_f_path, normalized_gram_path
        )
        block_normalized_drift.append(float(normalized_path[-1]))
        block_normalized_drift_sup.append(float(np.max(normalized_path)))
        successive_f = np.linalg.norm(
            np.diff(block_f_path, axis=0), axis=1
        ) / float(protocol["norms"]["S_f"])
        successive_gram_raw = np.diff(block_gram_path, axis=0)
        successive_gram = np.max(
            np.linalg.norm(
                successive_gram_raw.reshape(
                    successive_gram_raw.shape[0],
                    successive_gram_raw.shape[1],
                    -1,
                ),
                axis=2,
            ),
            axis=1,
        ) / float(protocol["norms"]["S_G"])
        block_normalized_total_variation.append(
            float(np.sum(np.maximum(successive_f, successive_gram)))
        )
        block_theta_min.append(float(np.min(theta_array[time_mask])))
    f_drift_array = np.asarray(f_drift)
    gram_drift_array = np.asarray(gram_drift)
    full_gram_difference = gram_array - gram_array[0]
    normalized_full_gram_drift = np.max(
        np.linalg.norm(
            full_gram_difference.reshape(
                full_gram_difference.shape[0],
                full_gram_difference.shape[1],
                -1,
            ),
            axis=2,
        ),
        axis=1,
    ) / float(protocol["norms"]["S_G"])
    arrays = {
        "times": times,
        "f": f_array,
        "grams": gram_array,
        "loss": np.asarray(loss_values),
        "theta_min": theta_array,
        "f_drift_from_initialization": f_drift_array,
        "gram_drift_from_initialization": gram_drift_array,
        "normalized_observable_drift_from_initialization": np.maximum(
            f_drift_array / float(protocol["norms"]["S_f"]),
            normalized_full_gram_drift,
        ),
        "arclength_step_times": step_times_array,
        "arclength_step_increment": increments_array,
        "arclength_cumulative": np.concatenate(
            (np.zeros(1), np.cumsum(increments_array))
        ),
        "block_starts": np.asarray([pair[0] for pair in block_pairs]),
        "block_ends": np.asarray([pair[1] for pair in block_pairs]),
        "block_arclength": np.asarray(block_arclength),
        "block_f_drift": np.asarray(block_f_drift),
        "block_gram_drift": np.asarray(block_gram_drift),
        "block_normalized_observable_drift": np.asarray(
            block_normalized_drift
        ),
        "block_normalized_observable_drift_sup": np.asarray(
            block_normalized_drift_sup
        ),
        "block_normalized_observable_total_variation": np.asarray(
            block_normalized_total_variation
        ),
        "block_theta_min": np.asarray(block_theta_min),
    }
    detail = {
        "arclength_semantics": (
            "sum at every RK4 step of the preregistered dense-coordinate "
            "norm of consecutive parameter states; it is reported separately "
            "from normalized f/G drift and needs a measured late-time gain "
            "before comparison with the 0.005 observable-tail allocation"
        ),
        "theta_semantics": (
            "exact finite-network muP tangent-kernel minimum eigenvalue at "
            "every saved time"
        ),
        "interpretation": (
            f"finite dense comparison through t={config['T']:g} only; no "
            "extrapolation or infinite-time conclusion is embedded in this "
            "archive"
        ),
    }
    return arrays, detail


def structural_inventory(protocol: Mapping[str, Any]) -> dict[str, Any]:
    stage4 = protocol["stage_4_generator_consistency"]
    stage6 = protocol["stage_6_all_time_tail"]
    stage5 = protocol["stage_5_amplification"]
    tail_primary = _primary_pde_config(protocol)
    model = common._canonical_model(protocol)

    def primary_config(resolution: Mapping[str, Any]) -> dict[str, Any]:
        value = resolution["primary"]
        base_order = int(value["base_order"])
        return {
            "N": int(value["N"]),
            "R": int(value["R"]),
            "dt": float(value["dt"]),
            "base_order": base_order,
            "M": base_order ** (model["X"].shape[0] + 1),
        }

    generator_resolution = stage4["numerical_resolution"]
    generator_primary_jobs = len(
        generator_resolution["primary"]["scramble_seeds"]
    )
    generator_refinement_jobs = len(
        generator_resolution["one_axis_refinements_at_seed_20260723"]
    )
    generator_jobs = generator_primary_jobs + generator_refinement_jobs
    gain_resolution = stage5["numerical_resolution"]
    gain_numerical_configs = (
        len(gain_resolution["primary"]["scramble_seeds"])
        + len(
            gain_resolution[
                "one_axis_refinements_at_seed_20260723"
            ]
        )
    )
    p70_resolution = protocol["stage_0_integrity_and_numerics"][
        "P70_conditional_extension"
    ]["numerical_resolution"]
    p70_primary_jobs = len(
        p70_resolution["primary"]["scramble_seeds"]
    )
    p70_refinement_jobs = len(
        p70_resolution["one_axis_refinements_at_seed_20260723"]
    )
    conditional_gain = _conditional_gain_declaration(
        protocol, required=False
    )
    conditional_gain_jobs = (
        2 * (p70_primary_jobs + p70_refinement_jobs)
        if conditional_gain is not None
        else 0
    )
    return {
        "generator": {
            "primary_jobs": generator_primary_jobs,
            "levels": stage4["levels"],
            "pairs": stage4["pairs"],
            "checkpoints": stage4["checkpoints"],
            "full_checkpoint_states_archived": 0,
            "primary_numerics": primary_config(generator_resolution),
            "one_axis_refinement_jobs": generator_refinement_jobs,
            "resolution_axes": [
                item["axis"]
                for item in generator_resolution[
                    "one_axis_refinements_at_seed_20260723"
                ]
            ],
            "jobs_total": generator_jobs,
            "conditional_P70": {
                "primary_jobs": p70_primary_jobs,
                "one_axis_refinement_jobs": p70_refinement_jobs,
                "jobs_total": p70_primary_jobs + p70_refinement_jobs,
                "primary_numerics": primary_config(p70_resolution),
                "resolution_axes": [
                    item["axis"]
                    for item in p70_resolution[
                        "one_axis_refinements_at_seed_20260723"
                    ]
                ],
                "joint_corner": None,
                "pair_configuration": (
                    "P5/P15/P35/P70 all share the same configuration "
                    "within each conditional generator archive"
                ),
            },
        },
        "gain": {
            "jobs_per_time_grid": (
                gain_numerical_configs * len(stage5["low_levels"])
            ),
            "low_levels": stage5["low_levels"],
            "jobs_total": (
                gain_numerical_configs
                * len(stage5["low_levels"])
                * 2
            ),
            "resolution_axes": [
                item["axis"]
                for item in gain_resolution[
                    "one_axis_refinements_at_seed_20260723"
                ]
            ],
            "primary_numerics": primary_config(gain_resolution),
            "time_grids": stage5["time_grids"],
            "positive_nonlinear_amplitudes": (
                stage5["symmetric_nonlinear_amplitude_magnitudes"]
            ),
            "full_high_level_states_archived": 0,
            "conditional_P70": {
                "declared": conditional_gain is not None,
                "authorization_flag": "--allow-conditional-p70",
                "residual_pair": (
                    [35, 70] if conditional_gain is not None else None
                ),
                "jobs_per_time_grid": (
                    p70_primary_jobs + p70_refinement_jobs
                    if conditional_gain is not None
                    else 0
                ),
                "jobs_total": conditional_gain_jobs,
                "primary_numerics": primary_config(p70_resolution),
                "resolution_axes": [
                    item["axis"]
                    for item in p70_resolution[
                        "one_axis_refinements_at_seed_20260723"
                    ]
                ],
                "time_grids": stage5["time_grids"],
                "positive_nonlinear_amplitudes": (
                    stage5["symmetric_nonlinear_amplitude_magnitudes"]
                ),
                "claim_scope": (
                    "next measured closure step only; it does not establish "
                    "P-to-infinity convergence"
                ),
            },
            "maximum_jobs_total_including_conditional_P70": (
                gain_numerical_configs
                * len(stage5["low_levels"])
                * 2
                + conditional_gain_jobs
            ),
        },
        "tail_pde": {
            "restartable_blocks": [
                list(pair) for pair in _tail_boundaries(protocol)
            ],
            "P": stage6["PDE_level"],
            "primary_numerics": tail_primary,
        },
        "tail_dense": stage6["dense_diagnostic"],
        "claim_boundary": (
            "all tail results are finite-horizon until a separately analyzed "
            "geometric envelope or trapping argument is established"
        ),
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
        description="Run one frozen stateful proof-obligation job."
    )
    subparsers = parser.add_subparsers(dest="stage", required=True)
    subparsers.add_parser("dry-run")

    generator = subparsers.add_parser("generator")
    generator.add_argument("--N", type=int, default=8)
    generator.add_argument("--R", type=int, default=128)
    generator.add_argument("--dt", type=float, default=0.02)
    generator.add_argument("--base-order", type=int, default=5)
    generator.add_argument("--seed", type=int, required=True)
    generator.add_argument("--max-level", type=int, default=35)
    generator.add_argument("--allow-conditional-p70", action="store_true")
    _add_output_arguments(generator)

    gain = subparsers.add_parser("gain")
    gain.add_argument("--N", type=int, default=8)
    gain.add_argument("--R", type=int, default=128)
    gain.add_argument("--dt", type=float, default=0.02)
    gain.add_argument("--base-order", type=int, default=5)
    gain.add_argument("--seed", type=int, required=True)
    gain.add_argument(
        "--low-level", type=int, choices=(5, 15, 35), required=True
    )
    gain.add_argument("--high-level", type=int, choices=(35, 70))
    gain.add_argument("--allow-conditional-p70", action="store_true")
    gain.add_argument(
        "--time-grid", choices=("primary", "refined"), required=True
    )
    _add_output_arguments(gain)

    tail_pde = subparsers.add_parser("tail-pde")
    tail_pde.add_argument("--block-end", type=float, required=True)
    tail_pde.add_argument("--restart-from", type=Path)
    tail_pde.add_argument("--N", type=int, default=16)
    tail_pde.add_argument("--R", type=int, default=256)
    tail_pde.add_argument("--dt", type=float, default=0.02)
    tail_pde.add_argument("--base-order", type=int, default=5)
    tail_pde.add_argument("--seed", type=int, default=20260723)
    _add_output_arguments(tail_pde)

    tail_dense = subparsers.add_parser("tail-dense")
    tail_dense.add_argument("--root-index", type=int, required=True)
    tail_dense.add_argument("--horizon", type=float)
    tail_dense.add_argument("--dt", type=float, default=0.02)
    _add_output_arguments(tail_dense)
    return parser


def _output_path(
    args: argparse.Namespace,
    stage: str,
    config: Mapping[str, Any],
) -> Path:
    if args.output is not None:
        return Path(args.output).resolve()
    return (
        Path(args.output_dir).resolve()
        / stage
        / f"{stage}_{common._hash_json(config)[:20]}.npz"
    )


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    protocol = common.load_protocol()
    if args.stage == "dry-run":
        print(json.dumps(structural_inventory(protocol), indent=2, sort_keys=True))
        return 0
    normalized_stage = args.stage.replace("-", "_")
    validators = {
        "generator": _validate_generator_config,
        "gain": _validate_gain_config,
        "tail_pde": _validate_tail_pde_config,
        "tail_dense": _validate_tail_dense_config,
    }
    config = validators[normalized_stage](protocol, args)
    provenance = _structural_provenance(
        protocol, normalized_stage, config
    )
    output_path = _output_path(args, normalized_stage, config)
    if output_path.exists():
        status = common._resume_existing(output_path, provenance)
        print(
            json.dumps(
                {
                    "status": status,
                    "stage": normalized_stage,
                    "output": str(output_path),
                }
            )
        )
        return 0
    if normalized_stage == "generator":
        arrays, detail = _run_generator(protocol, config)
    elif normalized_stage == "gain":
        arrays, detail = _run_gain(protocol, config)
    elif normalized_stage == "tail_pde":
        arrays, detail = _run_tail_pde(
            protocol,
            config,
            restart_path=args.restart_from,
            provenance=provenance,
        )
    elif normalized_stage == "tail_dense":
        arrays, detail = _run_tail_dense(protocol, config)
    else:  # pragma: no cover - parser and validator make this unreachable
        raise ValueError(f"unsupported structural stage: {normalized_stage}")
    metadata = common.build_output_metadata(
        provenance, arrays, detail
    )
    status = common.atomic_save_npz(output_path, arrays, metadata)
    verified = common.load_sealed_stage_archive(
        output_path,
        required_config_keys=tuple(config),
        required_arrays=tuple(arrays),
        expected_stage=normalized_stage,
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
            {
                "status": status,
                "stage": normalized_stage,
                "output": str(output_path),
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
