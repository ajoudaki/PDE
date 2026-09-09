"""Non-scientific integration tests for the frozen analysis driver."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
import sys
import tempfile
import unittest
from unittest.mock import patch

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
if str(SOURCE) not in sys.path:
    sys.path.insert(0, str(SOURCE))

from analyze_results import (  # noqa: E402
    _BASE_SOURCE_LABELS,
    _STRUCTURAL_SOURCE_LABELS,
    AnalysisError,
    AnalysisContext,
    LoadedEvidence,
    _canonical_json_bytes,
    _combine_structural_nuisance_upper_bound,
    _combine_stage1_sequential_results,
    _canonical_model_config,
    _conditional_geometric_amplification,
    _empirical_axis_sum_upper_bound,
    _expected_stage2_config,
    _expected_resolution_config,
    _expected_scaling_config,
    _expected_tail_dense_config,
    _expected_tail_pde_config,
    _finite_identification_gate,
    _finalize_stage2_gate,
    _geometric_tail_bound,
    _generator_total_residual_path,
    _has_cofinal_joint_corner_certificate,
    _attack_sequential_decision,
    _loo_curve_dispersion,
    _live_environment,
    _propagated_depth_bounds,
    _resampled_mean_curve_shift,
    _p70_state_machine,
    _post_active_tail_accounting,
    _require_exact_config,
    _sparse_refinement_upper_bound,
    _stage0_numerical_radius,
    _stage1_sequential_action,
    _structural_resolution_key,
    _validate_stage2_archive,
    _validate_tail_pde_archive,
    _sha256_bytes,
    analyze_all,
    analyze_stage0_numerics,
    analyze_stage5_gain,
    discover_evidence,
)
from analyze_study import (  # noqa: E402
    GateStatus,
    GateVerdict,
    build_sealed_archive,
    homogenization_expected_array_shapes,
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _make_empty_audit(path: Path) -> tuple[Path, dict[str, str]]:
    audit = path / "audit"
    protocol_path = audit / "protocol" / "preregistered_protocol.json"
    seal_path = audit / "results" / "seals" / "FROZEN_INPUTS.json"
    protocol_path.parent.mkdir(parents=True)
    seal_path.parent.mkdir(parents=True)
    protocol = {
        "schema_version": 1,
        "error_ledger": {
            "bootstrap_replicates": 20000,
            "bootstrap_pilot_replicates": 5000,
            "bootstrap_mc_failure_probability_per_call": 0.001 / 13.0,
            "data_alpha_total": 0.049,
            "bootstrap_mc_failure_total": 0.001,
            "maximum_bootstrap_calls": 13,
            "finite_sample_coverage_claimed": False,
            "bootstrap_seed": 2026072403,
            "independent_stochastic_families": 7,
            "stage_family_confidence": 0.993,
            "two_look_family_confidence": 0.9965,
            "three_look_family_confidence": 0.9976666666666667,
            "target_total_fraction": 0.05,
            "preallocated_components": {
                "PDE_numerics": 0.005,
                "dense_sampling": 0.005,
                "width_tail_conditional": 0.01,
                "depth_tail_conditional": 0.01,
                "amplified_closure": 0.015,
                "training_time_tail_conditional": 0.005,
            },
        },
    }
    protocol_path.write_bytes(_canonical_json_bytes(protocol))
    labels = {
        **_BASE_SOURCE_LABELS,
        **_STRUCTURAL_SOURCE_LABELS,
    }
    hashes_by_label = {
        label: hashlib.sha256(label.encode("utf-8")).hexdigest()
        for label in labels.values()
    }
    source_hashes = {
        key: hashes_by_label[label]
        for key, label in _BASE_SOURCE_LABELS.items()
    }
    seal = {
        "schema_version": 1,
        "protocol_sha256": _sha256(protocol_path),
        "files": [
            {
                "path": label,
                "sha256": hashes_by_label[label],
                "size_bytes": 0,
            }
            for label in labels.values()
        ],
        "environment": _live_environment(),
    }
    seal_path.write_bytes(_canonical_json_bytes(seal))
    return audit, source_hashes


def _write_archive(
    path: Path,
    *,
    stage: str,
    protocol_sha256: str,
    freeze_sha256: str,
    source_hashes: dict[str, str],
    environment_override: dict[str, str] | None = None,
) -> None:
    sealed = build_sealed_archive(
        stage=stage,
        config={"case": "synthetic"},
        arrays={"x": np.arange(3.0)},
        protocol_sha256=protocol_sha256,
        source_hashes=source_hashes,
    )
    metadata = dict(sealed.metadata)
    metadata["frozen_inputs_sha256"] = freeze_sha256
    environment = (
        _live_environment()
        if environment_override is None
        else environment_override
    )
    metadata["environment"] = environment
    metadata["python_version"] = environment["python"]
    metadata["platform"] = environment["platform"]
    metadata["numpy_version"] = environment["numpy"]
    metadata["scipy_version"] = environment["scipy"]
    metadata.pop("seal_sha256")
    metadata["seal_sha256"] = _sha256_bytes(
        _canonical_json_bytes(metadata)
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        path,
        metadata_json=np.asarray(
            json.dumps(
                metadata,
                sort_keys=True,
                separators=(",", ":"),
                allow_nan=False,
            )
        ),
        x=np.arange(3.0),
    )


def _tiny_stage2_protocol() -> dict[str, object]:
    return {
        "scope": {
            "canonical_model": {
                "X": [[1.0, 0.0], [0.0, 1.0]],
                "y": [0.5, -0.25],
                "activation": "tanh",
                "sigma_w": 0.65,
                "A": 1.0,
                "gamma": 1.0,
            }
        },
        "error_ledger": {"bootstrap_seed": 7401},
        "stage_1_ordered_target": {"dt": 0.02},
        "stage_2_homogenization": {
            "width": 4,
            "widths": [4],
            "depths": [2],
            "outer_B_a_roots": 2,
            "independent_W_replicas_per_outer_root": 2,
            "checkpoints": [0.0],
            "candidate_levels": [1],
        },
    }


def _tiny_stage2_item(
    protocol: dict[str, object],
    root: int,
) -> LoadedEvidence:
    config = _expected_stage2_config(protocol, root)
    shapes = homogenization_expected_array_shapes(
        widths=config["widths"],
        depths=config["depths"],
        checkpoints=config["checkpoints"],
        candidate_levels=config["candidate_levels"],
        replicas=int(config["replicas"]),
        input_dimension=2,
        sample_count=2,
    )
    arrays = {
        key: np.zeros(shape, dtype=float) for key, shape in shapes.items()
    }
    arrays["widths"] = np.asarray(config["widths"], dtype=np.int64)
    arrays["depths"] = np.asarray(config["depths"], dtype=np.int64)
    arrays["checkpoints"] = np.asarray(config["checkpoints"], dtype=float)
    rng = np.random.default_rng(int(config["outer_seed"]))
    arrays["shared_B_standard"] = rng.normal(size=(4, 2))
    arrays["shared_a_standard"] = rng.normal(size=4)
    arrays["W_replica_seeds"] = rng.integers(
        0,
        np.iinfo(np.uint64).max,
        size=2,
        dtype=np.uint64,
    )
    return LoadedEvidence(
        path=Path(f"stage2_root_{root}.npz"),
        stage="homogenization",
        archive=SimpleNamespace(
            metadata={"config": config},
            arrays=arrays,
        ),
        file_sha256="0" * 64,
    )


class DiscoveryAndMissingStageTests(unittest.TestCase):
    def test_empty_sealed_study_is_explicitly_unresolved_and_deterministic(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            audit, _source_hash = _make_empty_audit(Path(temporary))
            context = discover_evidence(
                audit_root=audit,
                verify_current_frozen_sources=False,
            )
            first, first_payloads = analyze_all(context)
            second, second_payloads = analyze_all(context)
            self.assertEqual(first["overall_gate"]["status"], "UNRESOLVED")
            self.assertEqual(first["archive_count"], 0)
            self.assertEqual(first, second)
            self.assertEqual(first_payloads, second_payloads)
            self.assertTrue(
                all(
                    value["gate"]["status"] == "UNRESOLVED"
                    for value in first["stage_results"].values()
                )
            )
            limits = " ".join(first["interpretive_limits"])
            self.assertIn("direct primary-to-joint", limits)
            self.assertIn("conditional P70 family has no joint", limits)

    def test_partial_file_and_unknown_stage_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            audit, source_hashes = _make_empty_audit(Path(temporary))
            partial = audit / "results" / "numerics" / "bad.npz.partial"
            partial.parent.mkdir(parents=True)
            partial.write_bytes(b"incomplete")
            with self.assertRaisesRegex(AnalysisError, "partial"):
                discover_evidence(
                    audit_root=audit,
                    verify_current_frozen_sources=False,
                )
            partial.unlink()
            protocol_hash = _sha256(
                audit / "protocol" / "preregistered_protocol.json"
            )
            freeze_hash = _sha256(
                audit / "results" / "seals" / "FROZEN_INPUTS.json"
            )
            _write_archive(
                audit / "results" / "unknown" / "one.npz",
                stage="not_declared",
                protocol_sha256=protocol_hash,
                freeze_sha256=freeze_hash,
                source_hashes=source_hashes,
            )
            with self.assertRaisesRegex(AnalysisError, "unrecognized"):
                discover_evidence(
                    audit_root=audit,
                    verify_current_frozen_sources=False,
                )

    def test_duplicate_configuration_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            audit, source_hashes = _make_empty_audit(Path(temporary))
            protocol_hash = _sha256(
                audit / "protocol" / "preregistered_protocol.json"
            )
            freeze_hash = _sha256(
                audit / "results" / "seals" / "FROZEN_INPUTS.json"
            )
            for name in ("one.npz", "two.npz"):
                _write_archive(
                    audit / "results" / "numerics" / name,
                    stage="numerics",
                    protocol_sha256=protocol_hash,
                    freeze_sha256=freeze_hash,
                    source_hashes=source_hashes,
                )
            with self.assertRaisesRegex(AnalysisError, "duplicate"):
                discover_evidence(
                    audit_root=audit,
                    verify_current_frozen_sources=False,
                )

    def test_direct_discovery_requires_exact_source_map_and_environment(
        self,
    ) -> None:
        mutations = ("swapped", "missing", "extra", "environment", "alias")
        for mutation in mutations:
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as temporary:
                audit, source_hashes = _make_empty_audit(
                    Path(temporary)
                )
                protocol_hash = _sha256(
                    audit
                    / "protocol"
                    / "preregistered_protocol.json"
                )
                freeze_path = (
                    audit
                    / "results"
                    / "seals"
                    / "FROZEN_INPUTS.json"
                )
                freeze_hash = _sha256(freeze_path)
                mutated_sources = dict(source_hashes)
                environment = None
                stage = "numerics"
                if mutation == "swapped":
                    left = mutated_sources["canonical_pde"]
                    right = mutated_sources["canonical_dense"]
                    mutated_sources["canonical_pde"] = right
                    mutated_sources["canonical_dense"] = left
                elif mutation == "missing":
                    mutated_sources.pop("runner")
                elif mutation == "extra":
                    freeze = json.loads(freeze_path.read_text())
                    by_label = {
                        item["path"]: item["sha256"]
                        for item in freeze["files"]
                    }
                    mutated_sources["pde_tangent"] = by_label[
                        _STRUCTURAL_SOURCE_LABELS["pde_tangent"]
                    ]
                elif mutation == "environment":
                    environment = {
                        **_live_environment(),
                        "numpy": "wrong-version",
                    }
                else:
                    stage = "generator_consistency"
                _write_archive(
                    audit / "results" / "numerics" / "one.npz",
                    stage=stage,
                    protocol_sha256=protocol_hash,
                    freeze_sha256=freeze_hash,
                    source_hashes=mutated_sources,
                    environment_override=environment,
                )
                expected = (
                    "unrecognized scientific stage"
                    if mutation == "alias"
                    else (
                        "environment"
                        if mutation == "environment"
                        else "source map"
                    )
                )
                with self.assertRaisesRegex(AnalysisError, expected):
                    discover_evidence(
                        audit_root=audit,
                        verify_current_frozen_sources=False,
                    )


class Stage2ValidationTests(unittest.TestCase):
    def test_exact_stage2_config_schema_and_rng_are_enforced(self) -> None:
        protocol = _tiny_stage2_protocol()
        item = _tiny_stage2_item(protocol, 0)
        self.assertEqual(_validate_stage2_archive(protocol, item), 0)

        bad_config = dict(item.archive.metadata["config"])
        bad_config["dt"] = float(np.nextafter(0.02, 1.0))
        with self.assertRaisesRegex(
            AnalysisError, "not exactly preregistered"
        ):
            _validate_stage2_archive(
                protocol,
                LoadedEvidence(
                    path=item.path,
                    stage=item.stage,
                    archive=SimpleNamespace(
                        metadata={"config": bad_config},
                        arrays=item.archive.arrays,
                    ),
                    file_sha256=item.file_sha256,
                ),
            )
        bad_arrays = dict(item.archive.arrays)
        bad_arrays["extra"] = np.zeros(1)
        with self.assertRaisesRegex(AnalysisError, "inventory mismatch"):
            _validate_stage2_archive(
                protocol,
                LoadedEvidence(
                    path=item.path,
                    stage=item.stage,
                    archive=SimpleNamespace(
                        metadata=item.archive.metadata,
                        arrays=bad_arrays,
                    ),
                    file_sha256=item.file_sha256,
                ),
            )
        wrong_rng = dict(item.archive.arrays)
        wrong_rng["shared_a_standard"] = (
            wrong_rng["shared_a_standard"] + 1.0
        )
        with self.assertRaisesRegex(
            AnalysisError, "does not match its outer seed"
        ):
            _validate_stage2_archive(
                protocol,
                LoadedEvidence(
                    path=item.path,
                    stage=item.stage,
                    archive=SimpleNamespace(
                        metadata=item.archive.metadata,
                        arrays=wrong_rng,
                    ),
                    file_sha256=item.file_sha256,
                ),
            )


class ExactConfigAdmissionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.protocol = json.loads(
            (
                ROOT / "protocol" / "preregistered_protocol.json"
            ).read_text()
        )

    @staticmethod
    def item(config, arrays=None) -> LoadedEvidence:
        return LoadedEvidence(
            path=Path("synthetic.npz"),
            stage="synthetic",
            archive=SimpleNamespace(
                config=config,
                arrays={} if arrays is None else arrays,
            ),
            file_sha256="0" * 64,
        )

    def test_scaling_and_tail_runtime_coordinates_are_exact(self) -> None:
        scaling = _expected_scaling_config(
            self.protocol, tier="screen", root_index=0
        )
        _require_exact_config(
            self.item(scaling), scaling, label="scaling"
        )
        for key, value in (
            ("T", np.nextafter(scaling["T"], np.inf)),
            ("T", 2.000019),
            ("dt", np.nextafter(scaling["dt"], 0.0)),
            ("dt", 0.0200001),
            ("root_seed", scaling["root_seed"] + 1),
        ):
            with self.subTest(stage="scaling", key=key, value=value):
                mutated = {**scaling, key: value}
                with self.assertRaisesRegex(
                    AnalysisError, "not exactly preregistered"
                ):
                    _require_exact_config(
                        self.item(mutated),
                        scaling,
                        label="scaling",
                    )

        tail_pde = _expected_tail_pde_config(
            self.protocol,
            seed=20260723,
            block_start=0.0,
            block_end=2.0,
            restart_seal_sha256=None,
        )
        tail_dense = _expected_tail_dense_config(
            self.protocol, root_index=0
        )
        for label, expected, key, value in (
            (
                "PDE-tail",
                tail_pde,
                "block_start",
                np.nextafter(0.0, np.inf),
            ),
            (
                "PDE-tail",
                tail_pde,
                "dt",
                np.nextafter(tail_pde["dt"], np.inf),
            ),
            (
                "dense-tail",
                tail_dense,
                "T",
                32.0003,
            ),
            (
                "dense-tail",
                tail_dense,
                "root_seed",
                tail_dense["root_seed"] + 1,
            ),
        ):
            with self.subTest(stage=label, key=key):
                mutated = {**expected, key: value}
                with self.assertRaisesRegex(
                    AnalysisError, "not exactly preregistered"
                ):
                    _require_exact_config(
                        self.item(mutated),
                        expected,
                        label=label,
                    )

    def test_structural_config_and_mirrored_arrays_are_exactly_typed(
        self,
    ) -> None:
        resolution = self.protocol[
            "stage_4_generator_consistency"
        ]["numerical_resolution"]
        seed = int(resolution["primary"]["scramble_seeds"][0])
        config = _expected_resolution_config(
            self.protocol,
            resolution,
            axis="primary",
            seed=seed,
            family="stage_4_generator_consistency_active",
        )
        arrays = {
            "numerical_resolution_axis_ascii": np.asarray(
                "primary", dtype="S16"
            ),
            "numerical_resolution_base_order": np.asarray(
                config["base_order"], dtype=np.int64
            ),
            "numerical_resolution_M": np.asarray(
                config["M"], dtype=np.int64
            ),
            "numerical_resolution_N": np.asarray(
                config["N"], dtype=np.int64
            ),
            "numerical_resolution_R": np.asarray(
                config["R"], dtype=np.int64
            ),
            "numerical_resolution_dt": np.asarray(
                config["dt"], dtype=np.float64
            ),
            "numerical_resolution_seed": np.asarray(
                config["seed"], dtype=np.int64
            ),
            "numerical_resolution_is_primary": np.asarray(
                1, dtype=np.uint8
            ),
        }
        item = self.item(config, arrays)
        self.assertEqual(
            _structural_resolution_key(
                protocol=self.protocol,
                stage_key="stage_4_generator_consistency",
                item=item,
                resolution=resolution,
            ),
            ("primary", seed),
        )
        mutated_config = {
            **config,
            "dt": float(np.nextafter(config["dt"], np.inf)),
        }
        with self.assertRaisesRegex(
            AnalysisError, "undeclared structural"
        ):
            _structural_resolution_key(
                protocol=self.protocol,
                stage_key="stage_4_generator_consistency",
                item=self.item(mutated_config, arrays),
                resolution=resolution,
            )
        mutated_arrays = dict(arrays)
        mutated_arrays["numerical_resolution_dt"] = np.asarray(
            np.nextafter(config["dt"], np.inf), dtype=np.float64
        )
        with self.assertRaisesRegex(
            AnalysisError, "resolution array"
        ):
            _structural_resolution_key(
                protocol=self.protocol,
                stage_key="stage_4_generator_consistency",
                item=self.item(config, mutated_arrays),
                resolution=resolution,
            )
        wrong_dtype = dict(arrays)
        wrong_dtype["numerical_resolution_N"] = np.asarray(
            config["N"], dtype=np.float64
        )
        with self.assertRaisesRegex(
            AnalysisError, "resolution array"
        ):
            _structural_resolution_key(
                protocol=self.protocol,
                stage_key="stage_4_generator_consistency",
                item=self.item(config, wrong_dtype),
                resolution=resolution,
            )

    def test_tail_sampled_and_restart_endpoints_are_exact(self) -> None:
        config = _expected_tail_pde_config(
            self.protocol,
            seed=20260723,
            block_start=0.0,
            block_end=2.0,
            restart_seal_sha256=None,
        )
        arrays = {
            "times": np.asarray([0.0, 1.0, 2.0], dtype=np.float64),
            "endpoint_time": np.asarray(2.0, dtype=np.float64),
        }
        _validate_tail_pde_archive(
            self.protocol,
            self.item(config, arrays),
            seed=20260723,
            block_start=0.0,
            block_end=2.0,
            restart_seal_sha256=None,
        )
        for key, values in (
            (
                "endpoint_time",
                np.asarray(
                    np.nextafter(2.0, np.inf), dtype=np.float64
                ),
            ),
            (
                "times",
                np.asarray(
                    [np.nextafter(0.0, np.inf), 1.0, 2.0],
                    dtype=np.float64,
                ),
            ),
            (
                "times",
                np.asarray(
                    [0.0, 1.0, np.nextafter(2.0, 0.0)],
                    dtype=np.float64,
                ),
            ),
        ):
            with self.subTest(key=key), self.assertRaisesRegex(
                AnalysisError, "endpoint"
            ):
                _validate_tail_pde_archive(
                    self.protocol,
                    self.item(
                        config,
                        {**arrays, key: values},
                    ),
                    seed=20260723,
                    block_start=0.0,
                    block_end=2.0,
                    restart_seal_sha256=None,
                )

    def test_extra_stage2_root_is_rejected(self) -> None:
        protocol = _tiny_stage2_protocol()
        item = _tiny_stage2_item(protocol, 0)
        config = dict(item.archive.metadata["config"])
        config["outer_root_index"] = 2
        with self.assertRaisesRegex(
            AnalysisError, "unexpected homogenization outer-root"
        ):
            _validate_stage2_archive(
                protocol,
                LoadedEvidence(
                    path=Path("extra_root.npz"),
                    stage="homogenization",
                    archive=SimpleNamespace(
                        metadata={"config": config},
                        arrays=item.archive.arrays,
                    ),
                    file_sha256="0" * 64,
                ),
            )

    def test_missing_actual_predictor_forces_unresolved(self) -> None:
        gate = _finalize_stage2_gate(
            GateVerdict(
                GateStatus.PASS,
                ("HOMOGENIZATION_VARIANCE_BIAS_COVARIANCE_PASS",),
            )
        )
        self.assertEqual(gate["status"], "UNRESOLVED")
        self.assertIn(
            "HOMOGENIZATION_ACTUAL_CONDITIONAL_ONSAGER_PREDICTOR_MISSING",
            gate["reason_codes"],
        )


class TailSemanticsTests(unittest.TestCase):
    def test_protocol_alpha_and_bootstrap_mc_budget_sum_to_five_percent(
        self,
    ) -> None:
        protocol = json.loads(
            (ROOT / "protocol" / "preregistered_protocol.json").read_text()
        )
        ledger = protocol["error_ledger"]
        self.assertAlmostEqual(
            float(ledger["data_alpha_total"])
            + float(ledger["bootstrap_mc_failure_total"]),
            0.05,
        )
        self.assertAlmostEqual(
            int(ledger["maximum_bootstrap_calls"])
            * float(ledger["bootstrap_mc_failure_probability_per_call"]),
            float(ledger["bootstrap_mc_failure_total"]),
        )
        self.assertFalse(ledger["finite_sample_coverage_claimed"])

    def test_geometric_tail_is_a_radius_around_the_finest_curve(self) -> None:
        self.assertAlmostEqual(
            _geometric_tail_bound(
                correction_upper=0.02,
                ratio_upper=0.5,
            ),
            0.02,
        )
        self.assertIsNone(
            _geometric_tail_bound(
                correction_upper=0.02,
                ratio_upper=1.0,
            )
        )

    def test_tail_budget_includes_every_measured_post_active_block(self) -> None:
        accounting = _post_active_tail_accounting(
            (0.20, 0.04, 0.02, 0.01),
            post_active_indices=(1, 2, 3),
            q_upper=0.5,
        )
        self.assertAlmostEqual(
            accounting["measured_post_active_upper_sum"], 0.07
        )
        self.assertAlmostEqual(
            accounting["future_beyond_maximum_horizon_upper"], 0.01
        )
        self.assertAlmostEqual(
            accounting["total_post_active_upper"], 0.08
        )

    def test_width_limit_balls_can_make_contracting_center_depths_unresolved(
        self,
    ) -> None:
        corrections, ratios = _propagated_depth_bounds(
            center_points=(0.04, 0.02, 0.01),
            center_lowers=(0.039, 0.019, 0.009),
            center_uppers=(0.041, 0.021, 0.011),
            width_tail_radii=(0.02, 0.02, 0.02, 0.02),
        )
        self.assertEqual(corrections[0]["lower"], 0.0)
        self.assertIsNone(ratios[0])
        # Raw center ratios are 1/2, but interval division is not allowed
        # because the preceding true-limit correction may be zero.
        self.assertAlmostEqual(
            corrections[1]["point"] / corrections[0]["point"],
            0.5,
        )

    def test_sparse_axis_bound_expands_with_scramble_uncertainty(self) -> None:
        self.assertAlmostEqual(
            _sparse_refinement_upper_bound(
                one_seed_axis_upper=0.002,
                primary_scramble_radius_upper=0.003,
                primary_sampling_upper=0.001,
            ),
            0.009,
        )

    def test_stage0_first_joint_correction_is_diagnostic_without_remainder(
        self,
    ) -> None:
        diagnostic, certified = _stage0_numerical_radius(
            primary_mean_shift_upper=0.003,
            primary_to_joint_upper=0.0,
            cofinal_remainder_upper=None,
        )
        self.assertAlmostEqual(diagnostic, 0.003)
        self.assertIsNone(certified)
        diagnostic, certified = _stage0_numerical_radius(
            primary_mean_shift_upper=0.003,
            primary_to_joint_upper=0.002,
            cofinal_remainder_upper=0.001,
        )
        self.assertAlmostEqual(diagnostic, 0.005)
        self.assertAlmostEqual(certified, 0.006)

    def test_completed_phase_b_emits_only_numerics_rows(self) -> None:
        protocol = json.loads(
            (
                ROOT / "protocol" / "preregistered_protocol.json"
            ).read_text()
        )
        stage = protocol["stage_0_integrity_and_numerics"]
        execution = stage["execution_inventory"]
        active_levels = tuple(
            int(value) for value in execution["active_levels"]
        )
        phase_a = execution["phase_A_primary_configs_per_level"]
        phase_b = execution[
            "phase_B_conditional_upward_configs_per_level"
        ]
        axis_by_coordinates = {
            (
                int(template["base_order"]),
                int(template["N"]),
                int(template["R"]),
                float(template["dt"]),
            ): str(template["axis"])
            for template in execution["phase_B_upward_templates"]
        }
        times = np.arange(
            0.0,
            float(stage["active_horizon"]) + 1e-12,
            float(protocol["norms"]["time_sampling"]),
        )
        times[-1] = float(stage["active_horizon"])
        sample_count = len(protocol["scope"]["canonical_model"]["y"])
        latent_dimension = (
            len(protocol["scope"]["canonical_model"]["X"]) + 1
        )
        evidence = []

        def add_item(
            *,
            P: int,
            declared: dict[str, object],
            execution_phase: str,
            numerical_axis: str,
            value: float,
        ) -> None:
            base_order = int(declared["base_order"])
            depth_nodes = int(declared["N"]) + 1
            config = {
                "P": P,
                "N": int(declared["N"]),
                "R": int(declared["R"]),
                "dt": float(declared["dt"]),
                "seed": int(declared["seed"]),
                "T": float(stage["active_horizon"]),
                "master_levels": [5, 15, 35, 70],
                "base_order": base_order,
                "M": base_order**latent_dimension,
                "conditional_p70_authorized": False,
                "phase_b_authorized": (
                    execution_phase == "phase_B_conditional"
                ),
                "execution_phase": execution_phase,
                "numerical_axis": numerical_axis,
                "canonical_model": _canonical_model_config(protocol),
            }
            arrays = {
                "times": times.copy(),
                "f": np.full(
                    (times.size, sample_count), value, dtype=float
                ),
                "grams": np.zeros(
                    (
                        times.size,
                        depth_nodes,
                        sample_count,
                        sample_count,
                    ),
                    dtype=float,
                ),
            }
            evidence.append(
                LoadedEvidence(
                    path=Path(
                        f"P{P}_{execution_phase}_{numerical_axis}_"
                        f"{config['seed']}.npz"
                    ),
                    stage="numerics",
                    archive=SimpleNamespace(
                        metadata={"config": config},
                        config=config,
                        arrays=arrays,
                    ),
                    file_sha256="0" * 64,
                )
            )

        level_value = {5: 0.0, 15: 0.1, 35: 0.2}
        for P in active_levels:
            for declared in phase_a:
                add_item(
                    P=P,
                    declared=declared,
                    execution_phase="phase_A_primary",
                    numerical_axis="primary",
                    value=level_value[P],
                )
            for declared in phase_b:
                coordinates = (
                    int(declared["base_order"]),
                    int(declared["N"]),
                    int(declared["R"]),
                    float(declared["dt"]),
                )
                add_item(
                    P=P,
                    declared=declared,
                    execution_phase="phase_B_conditional",
                    numerical_axis=axis_by_coordinates[coordinates],
                    value=level_value[P] + 0.001,
                )

        context = AnalysisContext(
            audit_root=ROOT,
            workspace_root=ROOT.parent,
            protocol_path=(
                ROOT / "protocol" / "preregistered_protocol.json"
            ),
            frozen_inputs_path=ROOT / "unused-freeze.json",
            results_root=ROOT / "results",
            processed_root=ROOT / "results" / "processed",
            protocol=protocol,
            frozen_inputs={},
            protocol_sha256="1" * 64,
            frozen_inputs_sha256="2" * 64,
            frozen_hashes=frozenset(),
            evidence=tuple(evidence),
        )
        with patch(
            "analyze_results._analysis_constants",
            return_value=(100, 20, 7401, 0.8, 0.1),
        ):
            result, rows = analyze_stage0_numerics(context)

        self.assertEqual(result["phase_A_gate"]["status"], "PASS")
        self.assertEqual(result["gate"]["status"], "UNRESOLVED")
        self.assertIn(
            "NUMERICS_COFINAL_REMAINDER_CERTIFICATE_MISSING",
            result["gate"]["reason_codes"],
        )
        self.assertIsNone(result["component_upper_bound"])
        self.assertTrue(rows)
        self.assertEqual({row["stage"] for row in rows}, {"numerics"})

    def test_structural_axis_nuisance_is_summed_not_maximized(self) -> None:
        self.assertAlmostEqual(
            _empirical_axis_sum_upper_bound(
                {"M": 0.001, "N": 0.002, "R": 0.003, "dt": 0.004}
            ),
            0.010,
        )
        bound, rule = _combine_structural_nuisance_upper_bound(
            {"M": 0.001, "N": 0.002, "R": 0.003, "dt": 0.004}
        )
        self.assertAlmostEqual(bound, 0.010)
        self.assertEqual(rule, "conservative_empirical_axis_sum")

    def test_joint_corner_replaces_axis_sum_as_direct_certificate(self) -> None:
        bound, rule = _combine_structural_nuisance_upper_bound(
            {
                "M": 0.001,
                "N": 0.002,
                "R": 0.003,
                "dt": 0.004,
                "joint": 0.006,
            }
        )
        self.assertAlmostEqual(bound, 0.006)
        self.assertEqual(rule, "direct_primary_to_joint_corner")

    def test_joint_certificate_requires_flag_and_exactly_one_job(self) -> None:
        joint = {
            "axis": "joint",
            "base_order": 6,
            "N": 12,
            "R": 256,
            "dt": 0.01,
            "seed": 20260723,
        }
        resolution = {
            "cofinal_joint_corner_certificate": True,
            "one_axis_refinements_at_seed_20260723": [joint],
        }
        self.assertTrue(_has_cofinal_joint_corner_certificate(resolution))
        self.assertFalse(
            _has_cofinal_joint_corner_certificate(
                {
                    **resolution,
                    "cofinal_joint_corner_certificate": False,
                }
            )
        )
        self.assertFalse(
            _has_cofinal_joint_corner_certificate(
                {
                    **resolution,
                    "one_axis_refinements_at_seed_20260723": [
                        joint,
                        dict(joint),
                    ],
                }
            )
        )

    def test_conditional_geometric_bound_needs_ratio_and_numerics(self) -> None:
        unresolved = _conditional_geometric_amplification(
            A15_point=0.010,
            A15_lower=0.009,
            A15_upper=0.011,
            A35_point=0.004,
            A35_lower=0.003,
            A35_upper=0.005,
            conditional_numerical_resolution_certified=False,
        )
        self.assertLess(unresolved["ratio_upper"], 1.0)
        self.assertIsNotNone(
            unresolved["candidate_P35_to_infinity_upper"]
        )
        self.assertIsNone(unresolved["ledger_component_upper_bound"])
        assumption_dependent = _conditional_geometric_amplification(
            A15_point=0.010,
            A15_lower=0.009,
            A15_upper=0.011,
            A35_point=0.004,
            A35_lower=0.003,
            A35_upper=0.005,
            conditional_numerical_resolution_certified=True,
            formal_statistical_coverage=False,
        )
        self.assertIsNone(
            assumption_dependent["ledger_component_upper_bound"]
        )
        certified = _conditional_geometric_amplification(
            A15_point=0.010,
            A15_lower=0.009,
            A15_upper=0.011,
            A35_point=0.004,
            A35_lower=0.003,
            A35_upper=0.005,
            conditional_numerical_resolution_certified=True,
            formal_statistical_coverage=True,
        )
        self.assertEqual(
            certified["ledger_component_upper_bound"],
            certified["candidate_P35_to_infinity_upper"],
        )
        noncontracting = _conditional_geometric_amplification(
            A15_point=0.010,
            A15_lower=0.005,
            A15_upper=0.012,
            A35_point=0.008,
            A35_lower=0.006,
            A35_upper=0.009,
            conditional_numerical_resolution_certified=True,
            formal_statistical_coverage=True,
        )
        self.assertGreaterEqual(noncontracting["ratio_upper"], 1.0)
        self.assertIsNone(
            noncontracting["candidate_P35_to_infinity_upper"]
        )
        self.assertIsNone(noncontracting["ledger_component_upper_bound"])

    def test_complete_conditional_gain_family_is_analyzed_but_unresolved(
        self,
    ) -> None:
        protocol = json.loads(
            (ROOT / "protocol" / "preregistered_protocol.json").read_text()
        )
        resolution = protocol["stage_0_integrity_and_numerics"][
            "P70_conditional_extension"
        ]["numerical_resolution"]
        entries = [
            (
                "primary",
                {
                    **{
                        key: resolution["primary"][key]
                        for key in ("base_order", "N", "R", "dt")
                    },
                    "seed": seed,
                },
            )
            for seed in resolution["primary"]["scramble_seeds"]
        ] + [
            (value["axis"], dict(value))
            for value in resolution[
                "one_axis_refinements_at_seed_20260723"
            ]
        ]
        evidence = []
        for grid in ("primary", "refined"):
            times = np.asarray(
                protocol["stage_5_amplification"]["time_grids"][grid],
                dtype=float,
            )
            for index, (axis, coordinates) in enumerate(entries):
                base_order = int(coordinates["base_order"])
                stage5 = protocol["stage_5_amplification"]
                family = "conditional_P70_gain"
                config = {
                    **_expected_resolution_config(
                        protocol,
                        resolution,
                        axis=axis,
                        seed=int(coordinates["seed"]),
                        family=family,
                    ),
                    "low_level": 35,
                    "high_level": 70,
                    "conditional_p70_authorized": True,
                    "closure_step_scope": str(
                        stage5["conditional_P70_extension"][
                            "interpretation"
                        ]
                    ),
                    "horizon": float(stage5["horizon"]),
                    "time_grid_name": grid,
                    "source_times": times.tolist(),
                    "observation_times": times.tolist(),
                    "residual_snapshot_times": times.tolist(),
                    "nonlinear_amplitudes": [
                        float(value)
                        for value in stage5[
                            "symmetric_nonlinear_amplitude_magnitudes"
                        ]
                    ],
                    "observable_blocks": ["f", "grams"],
                    "canonical_model": _canonical_model_config(protocol),
                }
                arrays = {
                    "numerical_resolution_family_ascii": np.asarray(
                        "conditional_P70_gain", dtype="S32"
                    ),
                    "numerical_resolution_axis_ascii": np.asarray(
                        axis, dtype="S16"
                    ),
                    "numerical_resolution_base_order": np.asarray(base_order),
                    "numerical_resolution_M": np.asarray(base_order**4),
                    "numerical_resolution_N": np.asarray(
                        int(coordinates["N"])
                    ),
                    "numerical_resolution_R": np.asarray(
                        int(coordinates["R"])
                    ),
                    "numerical_resolution_dt": np.asarray(
                        float(coordinates["dt"])
                    ),
                    "numerical_resolution_seed": np.asarray(
                        int(coordinates["seed"])
                    ),
                    "numerical_resolution_is_primary": np.asarray(
                        axis == "primary", dtype=np.uint8
                    ),
                    "residual_pair_levels": np.asarray([35, 70]),
                    "conditional_p70_authorized": np.asarray(
                        1, dtype=np.uint8
                    ),
                    "primary_residual_subspace_gain": np.asarray(1.0),
                    "residual_state_norm_L1_time_integral": np.asarray(
                        0.004
                    ),
                    "amplified_residual_bound_discrete": np.asarray(0.004),
                    "residual_snapshot_times": times,
                    "residual_basis_reconstruction_error": np.zeros(
                        times.size
                    ),
                    "residual_basis_relative_reconstruction_error": np.zeros(
                        times.size
                    ),
                    "nonlinear_plus_absolute_error": np.zeros(1),
                    "nonlinear_minus_absolute_error": np.zeros(1),
                    "nonlinear_symmetry_defect": np.zeros(1),
                }
                evidence.append(
                    LoadedEvidence(
                        path=Path(f"conditional_{grid}_{index}.npz"),
                        stage="amplification",
                        archive=SimpleNamespace(
                            config=config, arrays=arrays
                        ),
                        file_sha256="0" * 64,
                    )
                )
        context = AnalysisContext(
            audit_root=ROOT,
            workspace_root=ROOT.parent,
            protocol_path=ROOT
            / "protocol"
            / "preregistered_protocol.json",
            frozen_inputs_path=ROOT / "unused-freeze.json",
            results_root=ROOT / "results",
            processed_root=ROOT / "results" / "processed",
            protocol=protocol,
            frozen_inputs={},
            protocol_sha256="1" * 64,
            frozen_inputs_sha256="2" * 64,
            frozen_hashes=frozenset(),
            evidence=tuple(evidence),
        )
        result, rows = analyze_stage5_gain(
            context, _conditional_p70=True
        )
        self.assertIn("conditional_P70_family_complete", result, result)
        self.assertTrue(result["conditional_P70_family_complete"])
        self.assertFalse(
            result["conditional_numerical_resolution_certified"]
        )
        self.assertAlmostEqual(result["A35_point"], 0.004)
        self.assertIsNone(result["component_upper_bound"])
        self.assertIn(
            "AMPLIFICATION_P70_NUMERICS_UNRESOLVED_NO_LEDGER_BOUND",
            result["gate"]["reason_codes"],
        )
        self.assertNotIn(
            "AMPLIFICATION_P70_CONDITIONAL_ANALYSIS_PENDING",
            result["gate"]["reason_codes"],
        )
        self.assertTrue(rows)

    def test_nonzero_lift_low_is_a_residual_not_an_identity_failure(self) -> None:
        values = np.zeros((3, 4))
        values[:, 3] = (0.0, 0.001, 0.0033)
        path = _generator_total_residual_path(
            values,
            checkpoint_count=3,
            name="synthetic lift-low",
        )
        np.testing.assert_array_equal(path, values[:, 3])

    def test_p70_state_machine_requires_both_frozen_triggers(self) -> None:
        self.assertEqual(
            _p70_state_machine(
                p70_present=True,
                base_trigger_ready=True,
                p15_amplification_ready=True,
            ),
            "AUTHORIZED_EVALUATE",
        )
        for base_ready, gain_ready in (
            (False, False),
            (False, True),
            (True, False),
        ):
            self.assertEqual(
                _p70_state_machine(
                    p70_present=True,
                    base_trigger_ready=base_ready,
                    p15_amplification_ready=gain_ready,
                ),
                "DENIED_PROTOCOL_VIOLATION",
            )

    def test_large_central_pde_dense_gap_fails_identification(self) -> None:
        gate = _finite_identification_gate(
            tier="positive",
            lower=0.08,
            upper=0.10,
        )
        self.assertEqual(gate["status"], "FAIL")
        self.assertIn(
            "IDENTIFICATION_P35_DENSE_GAP_EXCEEDS_FIVE_PERCENT",
            gate["reason_codes"],
        )

    def test_loo_rms_is_not_an_empirical_q95_gate(self) -> None:
        f = np.asarray([[[0.0]], [[1.0]], [[2.0]], [[3.0]]])
        gram = np.zeros((4, 1, 1, 1, 1))
        summary = _loo_curve_dispersion(
            f,
            gram,
            np.arange(4),
            s_f=1.0,
            s_g=1.0,
        )
        self.assertGreater(summary["empirical_max"], summary["rms"])
        self.assertAlmostEqual(summary["mean_se"], summary["rms"] / 2.0)

    def test_mean_sampling_radius_uses_resampled_center_displacement(
        self,
    ) -> None:
        f = np.asarray([[[0.0]], [[1.0]], [[2.0]], [[3.0]]])
        gram = np.zeros((4, 1, 1, 1, 1))
        full_center = (np.mean(f, axis=0), np.mean(gram, axis=0))
        shift = _resampled_mean_curve_shift(
            f,
            gram,
            np.asarray([0, 0, 1, 1]),
            full_center=full_center,
            s_f=1.0,
            s_g=1.0,
        )
        loo = _loo_curve_dispersion(
            f,
            gram,
            np.arange(4),
            s_f=1.0,
            s_g=1.0,
        )
        self.assertAlmostEqual(shift, 1.0)
        self.assertNotAlmostEqual(shift, loo["mean_se"])

    def test_attack_null_screen_stops_without_confirmation(self) -> None:
        status, reasons, triggered = _attack_sequential_decision(
            screen_candidates=(),
            persistent_candidates=(),
            screen_constraints_pass=True,
            confirmation_constraints_pass=False,
            confirmation_complete=False,
            confirmation_present=False,
        )
        self.assertEqual(status.value, "UNRESOLVED")
        self.assertFalse(triggered)
        self.assertIn("ATTACK_NULL_SCREEN_NO_OFF_MANIFOLD_COUNTEREXAMPLE", reasons)

    def test_attack_trigger_requires_confirmation(self) -> None:
        status, reasons, triggered = _attack_sequential_decision(
            screen_candidates=((1.0, 0.5),),
            persistent_candidates=(),
            screen_constraints_pass=True,
            confirmation_constraints_pass=False,
            confirmation_complete=False,
            confirmation_present=False,
        )
        self.assertEqual(status.value, "UNRESOLVED")
        self.assertTrue(triggered)
        self.assertEqual(
            reasons, ["ATTACK_SCREEN_TRIGGERED_CONFIRMATION_INCOMPLETE"]
        )

    def test_failed_scaling_screen_cannot_be_erased_by_positive_grid(self) -> None:
        action = _stage1_sequential_action(
            screen_status=__import__("analyze_study").GateStatus.FAIL,
            positive_present=True,
            positive_complete=True,
        )
        self.assertEqual(
            action, "STOP_FAILED_SCREEN_WITH_EXTRANEOUS_POSITIVE"
        )

    def test_stage1_combined_result_retains_both_look_calibrations(
        self,
    ) -> None:
        screen_metrics = {
            "tier": "screen",
            "confidence": 0.9965,
            "critical_lower": 2.1,
            "critical_upper": 2.1,
            "bootstrap_calibration": {
                "pilot_replicates": 5000,
                "calibration_replicates": 20000,
                "critical_order_index": 19990,
            },
            "inference_scope": {
                "root_count": 24,
                "finite_sample_coverage_claimed": False,
                "semantics": "screen scope",
            },
        }
        positive_metrics = {
            "tier": "positive",
            "confidence": 0.9965,
            "critical_lower": 2.4,
            "critical_upper": 2.4,
            "bootstrap_calibration": {
                "pilot_replicates": 5000,
                "calibration_replicates": 20000,
                "critical_order_index": 19991,
            },
            "inference_scope": {
                "root_count": 12,
                "finite_sample_coverage_claimed": False,
                "semantics": "positive scope",
            },
        }
        screen_result = {
            "gate": {
                "status": "UNRESOLVED",
                "reason_codes": ["ORDERED_POSITIVE_GRID_REQUIRED"],
                "metrics": {"tier": "screen"},
            },
            "metrics": screen_metrics,
            "missing": [],
            "component_bounds": {"dense_sampling": 0.001},
        }
        positive_result = {
            "gate": {
                "status": "PASS",
                "reason_codes": [
                    "ORDERED_SCALING_AND_NORM_BALL_TAILS_PASS"
                ],
                "metrics": {"tier": "positive"},
            },
            "metrics": positive_metrics,
            "missing": [],
            "component_bounds": {"dense_sampling": 0.0005},
        }

        combined = _combine_stage1_sequential_results(
            screen_result=screen_result,
            positive_result=positive_result,
        )

        self.assertEqual(combined["gate"], positive_result["gate"])
        self.assertEqual(combined["metrics"], positive_metrics)
        self.assertEqual(combined["screen_gate"], screen_result["gate"])
        self.assertEqual(
            combined["sequential_looks"]["screen"]["metrics"],
            screen_metrics,
        )
        self.assertEqual(
            combined["sequential_looks"]["positive"]["metrics"],
            positive_metrics,
        )
        for look, expected in (
            ("screen", screen_metrics),
            ("positive", positive_metrics),
        ):
            retained = combined["sequential_looks"][look]["metrics"]
            for key in (
                "confidence",
                "critical_lower",
                "critical_upper",
                "bootstrap_calibration",
                "inference_scope",
            ):
                self.assertEqual(retained[key], expected[key])


if __name__ == "__main__":
    unittest.main()
