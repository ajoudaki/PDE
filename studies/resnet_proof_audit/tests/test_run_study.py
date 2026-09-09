"""Small algebraic and orchestration tests for ``run_study``.

No test in this module launches a scientific PDE or dense-network trajectory.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

import numpy as np


SOURCE = Path(__file__).resolve().parents[1] / "source"
if str(SOURCE) not in sys.path:
    sys.path.insert(0, str(SOURCE))

import run_study as runner  # noqa: E402
from analyze_study import (  # noqa: E402
    ArchiveValidationError,
    homogenization_expected_array_shapes,
    validate_homogenization_archive_schema,
)


class AtomicArchiveTests(unittest.TestCase):
    def test_atomic_write_exact_resume_and_mismatch(self) -> None:
        metadata = {
            "archive_schema": 1,
            "stage": "unit",
            "config": {"x": 3},
        }
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "result.npz"
            self.assertEqual(
                runner.atomic_save_npz(
                    path, {"value": np.arange(4.0)}, metadata
                ),
                "written",
            )
            self.assertTrue(path.is_file())
            self.assertFalse(path.with_name(path.name + ".partial").exists())
            self.assertEqual(
                runner.atomic_save_npz(path, {}, metadata),
                "reused",
            )
            with self.assertRaises(FileExistsError):
                runner.atomic_save_npz(
                    path, {}, {**metadata, "config": {"x": 4}}
                )

    def test_stale_partial_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "result.npz"
            partial = path.with_name(path.name + ".partial")
            partial.write_bytes(b"interrupted")
            with self.assertRaises(FileExistsError):
                runner.atomic_save_npz(
                    path, {"x": np.zeros(1)}, {"stage": "unit"}
                )

    def test_stale_partial_blocks_existing_final_resume(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "result.npz"
            path.write_bytes(b"final-present")
            path.with_name(path.name + ".partial").write_bytes(
                b"interrupted"
            )
            with self.assertRaisesRegex(
                FileExistsError, "stale partial archive blocks resume"
            ):
                runner._resume_existing(
                    path,
                    {
                        "stage": "unit",
                        "protocol_sha256": "1" * 64,
                        "source_hashes": {"unit": "2" * 64},
                    },
                )

    def test_homogenization_resume_rejects_incomplete_sealed_archive(
        self,
    ) -> None:
        protocol = runner.load_protocol()
        outer_seed = 81231
        config = {
            "widths": [16],
            "width": 16,
            "depths": [2],
            "outer_root_index": 0,
            "outer_seed": outer_seed,
            "replicas": 2,
            "checkpoints": [0.0],
            "candidate_levels": [5],
            "dt": 0.02,
            "canonical_model": runner._jsonable(
                runner._canonical_model(protocol)
            ),
        }
        arrays, _detail = runner._run_homogenization(
            protocol,
            {
                "widths": config["widths"],
                "depths": config["depths"],
                "outer_seed": outer_seed,
                "replicas": config["replicas"],
                "checkpoints": config["checkpoints"],
                "candidate_levels": config["candidate_levels"],
                "dt": config["dt"],
            },
        )
        arrays.pop("W16_D2_t0000_terminal_H")
        environment = runner._live_environment()
        provenance = {
            "schema_version": 1,
            "stage": "homogenization",
            "sealed": True,
            "protocol_path": "protocol/test.json",
            "protocol_sha256": "2" * 64,
            "frozen_inputs_sha256": "3" * 64,
            "source_hashes": {"runner": "4" * 64},
            "config": config,
            "config_sha256": runner._hash_json(config),
            "environment": environment,
            "python_version": environment["python"],
            "platform": environment["platform"],
            "numpy_version": environment["numpy"],
            "scipy_version": environment["scipy"],
        }
        metadata = runner.build_output_metadata(
            provenance, arrays, {"semantics": "incomplete fixture"}
        )
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "homogenization.npz"
            runner.atomic_save_npz(path, arrays, metadata)
            with self.assertRaisesRegex(
                ArchiveValidationError, "inventory mismatch"
            ):
                runner._resume_existing(path, provenance)

    def test_runner_seal_is_accepted_by_analysis_loader(self) -> None:
        arrays = {
            "times": np.array([0.0, 0.04]),
            "f": np.zeros((2, 3)),
        }
        digest = "1" * 64
        environment = runner._live_environment()
        provenance = {
            "schema_version": 1,
            "stage": "unit_runner",
            "sealed": True,
            "protocol_path": "protocol/test.json",
            "protocol_sha256": "2" * 64,
            "frozen_inputs_sha256": "3" * 64,
            "source_hashes": {"runner": digest},
            "config": {"case": "synthetic"},
            "config_sha256": runner._hash_json({"case": "synthetic"}),
            "environment": environment,
            "python_version": environment["python"],
            "platform": environment["platform"],
            "numpy_version": environment["numpy"],
            "scipy_version": environment["scipy"],
        }
        metadata = runner.build_output_metadata(
            provenance, arrays, {"semantics": "synthetic unit test"}
        )
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "sealed.npz"
            runner.atomic_save_npz(path, arrays, metadata)
            loaded = runner.load_sealed_stage_archive(
                path,
                required_config_keys=("case",),
                required_arrays=("times", "f"),
                expected_stage="unit_runner",
                expected_protocol_sha256="2" * 64,
                expected_source_hashes={"runner": digest},
            )
        self.assertTrue(loaded.metadata["sealed"])
        self.assertEqual(loaded.metadata["frozen_inputs_sha256"], "3" * 64)
        self.assertEqual(loaded.metadata["environment"], environment)
        self.assertEqual(set(loaded.metadata["array_hashes"]), set(arrays))

    def test_provenance_requires_exact_frozen_environment(self) -> None:
        protocol = runner.load_protocol()
        protocol = json.loads(json.dumps(protocol))
        protocol["status"] = (
            "preregistered_before_new_scientific_trajectories"
        )
        source_labels = {
            "activation_linearity_smoking_gun/source/src/"
            "dense_pde/operator_galerkin.py",
            "activation_linearity_smoking_gun/source/src/"
            "dense_reference/core.py",
            "activation_linearity_smoking_gun/source/src/activations.py",
            "source/cross_p.py",
            "source/dense_gates.py",
            "source/run_study.py",
        }
        frozen_hashes = {label: "a" * 64 for label in source_labels}
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary)
            protocol_path = (
                workspace
                / "pde_proof_obligation_audit"
                / "protocol"
                / "preregistered_protocol.json"
            )
            protocol_path.parent.mkdir(parents=True)
            protocol_path.write_text(
                json.dumps(protocol, sort_keys=True), encoding="utf-8"
            )
            freeze_path = workspace / "FROZEN_INPUTS.json"
            environment = runner._live_environment()
            freeze = {
                "protocol_sha256": runner._sha256_file(protocol_path),
                "environment": environment,
            }
            freeze_path.write_text(json.dumps(freeze), encoding="utf-8")
            patches = (
                mock.patch.object(runner, "WORKSPACE_ROOT", workspace),
                mock.patch.object(runner, "PROTOCOL_PATH", protocol_path),
                mock.patch.object(runner, "FROZEN_INPUTS_PATH", freeze_path),
                mock.patch.object(
                    runner,
                    "_verify_frozen_source_tree",
                    return_value=frozen_hashes,
                ),
            )
            with patches[0], patches[1], patches[2], patches[3]:
                provenance = runner._provenance(
                    protocol, "scaling", {"case": "synthetic"}
                )
            self.assertEqual(provenance["environment"], environment)
            self.assertIn(
                "canonical_activations", provenance["source_hashes"]
            )
            freeze["environment"] = {**environment, "numpy": "poisoned"}
            freeze_path.write_text(json.dumps(freeze), encoding="utf-8")
            with (
                mock.patch.object(runner, "WORKSPACE_ROOT", workspace),
                mock.patch.object(runner, "PROTOCOL_PATH", protocol_path),
                mock.patch.object(
                    runner, "FROZEN_INPUTS_PATH", freeze_path
                ),
                mock.patch.object(
                    runner,
                    "_verify_frozen_source_tree",
                    return_value=frozen_hashes,
                ),
            ):
                with self.assertRaisesRegex(ValueError, "environment"):
                    runner._provenance(
                        protocol, "scaling", {"case": "synthetic"}
                    )


class NumericalHelperTests(unittest.TestCase):
    def test_memory_preflight_fails_cleanly(self) -> None:
        with mock.patch.object(
            runner, "available_memory_bytes", return_value=2 * 1024**3
        ):
            with self.assertRaisesRegex(MemoryError, "not silently omitted"):
                runner.preflight_pde_memory(
                    N=32, M=625, R=512, P=35
                )

    def test_dense_scaling_memory_preflight_counts_master_and_rk4(self) -> None:
        arguments = dict(
            n_grid=(128, 256, 512, 1024),
            L_grid=(16, 32, 64, 128),
            input_dim=3,
            sample_count=3,
            horizon=2.0,
            sample_dt=0.04,
        )
        with mock.patch.object(
            runner, "available_memory_bytes", return_value=512 * 1024**3
        ):
            estimate = runner.preflight_dense_scaling_memory(**arguments)
        master_bytes = (128 * 1024 * 1024 + 4 * 1024) * 8
        self.assertGreater(estimate, 11 * master_bytes)
        with mock.patch.object(
            runner, "available_memory_bytes", return_value=2 * 1024**3
        ):
            with self.assertRaisesRegex(MemoryError, "dense-scaling"):
                runner.preflight_dense_scaling_memory(**arguments)

    def test_redesigned_sparse_corners_fit_same_preflight(self) -> None:
        retained_stage4 = 3.0 + (5 + 15) / 35 + 2.0
        retained_stage5 = 11 * 15 / 35
        retained_p70 = 3.0 + (5 + 15 + 35) / 70 + 2.0
        with mock.patch.object(
            runner, "available_memory_bytes", return_value=20 * 1024**3
        ):
            for arguments in (
                dict(N=20, M=625, R=512, P=35),
                dict(
                    N=8,
                    M=1296,
                    R=128,
                    P=35,
                    retained_state_equivalents=retained_stage4,
                ),
                dict(
                    N=8,
                    M=1296,
                    R=128,
                    P=35,
                    retained_state_equivalents=retained_stage5,
                ),
                dict(
                    N=8,
                    M=1296,
                    R=128,
                    P=70,
                    retained_state_equivalents=retained_p70,
                ),
                dict(
                    N=12,
                    M=1296,
                    R=256,
                    P=35,
                    retained_state_equivalents=retained_stage4,
                ),
                dict(
                    N=12,
                    M=1296,
                    R=256,
                    P=35,
                    retained_state_equivalents=retained_stage5,
                ),
                dict(
                    N=12,
                    M=1296,
                    R=256,
                    P=15,
                    retained_state_equivalents=22,
                ),
            ):
                self.assertGreater(
                    runner.preflight_pde_memory(**arguments), 0
                )
            with self.assertRaisesRegex(
                MemoryError, "not silently omitted"
            ):
                runner.preflight_pde_memory(
                    N=32, M=625, R=512, P=35
                )

    def test_normalized_depth_alignment_is_linear_exact(self) -> None:
        source_s = np.linspace(0.0, 1.0, 5)
        gram = np.zeros((2, 5, 2, 2))
        for time in range(2):
            for index, s in enumerate(source_s):
                gram[time, index] = (time + 2.0 * s) * np.eye(2)
        aligned = runner.align_normalized_depth(gram, common_nodes=17)
        target_s = np.linspace(0.0, 1.0, 17)
        self.assertEqual(aligned.shape, (2, 17, 2, 2))
        np.testing.assert_allclose(
            aligned[1, :, 0, 0], 1.0 + 2.0 * target_s
        )

    def test_crossfit_is_leave_one_out_and_covariance_is_full(self) -> None:
        values = np.arange(3 * 2 * 2, dtype=float).reshape(3, 2, 2)
        means = runner.crossfit_means(values)
        np.testing.assert_allclose(means[0], 0.5 * (values[1] + values[2]))
        innovations = values - means
        covariance = runner.full_layer_covariance(innovations)
        self.assertEqual(covariance.shape, (2, 2))
        np.testing.assert_allclose(covariance, covariance.T)
        self.assertGreaterEqual(np.linalg.eigvalsh(covariance)[0], -1e-12)

    def test_bias_squared_uses_only_cross_replica_pairs(self) -> None:
        # Constant residual has bias squared 4.  Antisymmetric zero-mean
        # residuals have a negative finite-sample off-diagonal estimate,
        # demonstrating that no positive diagonal variance leaked in.
        constant = 2.0 * np.ones((4, 3, 2))
        np.testing.assert_allclose(
            runner.cross_replica_bias_squared(constant), 4.0
        )
        zero_mean = np.array([-1.0, -1.0, 1.0, 1.0])[:, None, None]
        estimate = runner.cross_replica_bias_squared(zero_mean)
        self.assertLess(float(estimate[0]), 0.0)

    def test_online_layer_summary_matches_batch_sufficient_statistics(
        self,
    ) -> None:
        rng = np.random.default_rng(202)
        values = rng.normal(size=(8, 7, 4, 3))
        summary = runner.summarize_layer_replicas(values)
        np.testing.assert_allclose(
            summary["depth_average"], np.mean(values, axis=1)
        )
        np.testing.assert_allclose(
            summary["layer_covariance"],
            runner.full_layer_covariance(values),
            rtol=2e-13,
            atol=2e-14,
        )
        self.assertAlmostEqual(
            float(summary["integrated_covariance"]),
            float(np.mean(summary["layer_covariance"])),
            places=15,
        )
        depth_average = summary["depth_average"].reshape(8, -1)
        centered_average = depth_average - np.mean(
            depth_average, axis=0, keepdims=True
        )
        depth_average_variance = np.sum(
            centered_average * centered_average
        ) / ((8 - 1) * depth_average.shape[1])
        self.assertAlmostEqual(
            float(summary["integrated_covariance"]),
            float(depth_average_variance),
            places=14,
        )
        flattened = values.reshape(8, 7, -1)
        first = np.mean(flattened[:4], axis=0)
        second = np.mean(flattened[4:], axis=0)
        expected_by_layer = np.mean(first * second, axis=1)
        np.testing.assert_allclose(
            summary["bias_squared_by_layer"], expected_by_layer
        )
        first_average = np.mean(np.mean(flattened[:4], axis=1), axis=0)
        second_average = np.mean(np.mean(flattened[4:], axis=1), axis=0)
        self.assertAlmostEqual(
            float(summary["depth_average_bias_squared"]),
            float(np.mean(first_average * second_average)),
            places=15,
        )
        # The accumulator's public payload is the complete compact schema;
        # no replica-by-layer action tensor survives finalization.
        self.assertEqual(
            set(summary),
            {
                "depth_average",
                "layer_covariance",
                "integrated_covariance",
                "bias_squared_by_layer",
                "depth_average_bias_squared",
            },
        )

    def test_tiny_homogenization_execution_uses_compact_schema(self) -> None:
        protocol = runner.load_protocol()
        arrays, detail = runner._run_homogenization(
            protocol,
            {
                "widths": [16],
                "depths": [2],
                "replicas": 2,
                "checkpoints": [0.0],
                "candidate_levels": [5, 15],
                "outer_seed": 551,
                "dt": 0.02,
            },
        )
        prefix = "W16_D2_t0000"
        expected_names = (
            "forward_action",
            "transpose_action",
            "forward_reconstruction_residual_P5",
            "transpose_projection_residual_P5",
            "forward_reconstruction_residual_P15",
            "transpose_projection_residual_P15",
        )
        for name in expected_names:
            self.assertEqual(
                arrays[f"{prefix}_{name}_depth_average"].shape,
                (2, 16, 3),
            )
            self.assertEqual(
                arrays[f"{prefix}_{name}_layer_covariance"].shape,
                (2, 2),
            )
            self.assertEqual(
                arrays[f"{prefix}_{name}_bias_squared_by_layer"].shape,
                (2,),
            )
            self.assertEqual(
                arrays[
                    f"{prefix}_{name}_depth_average_bias_squared"
                ].shape,
                (),
            )
        self.assertEqual(arrays[f"{prefix}_terminal_H"].shape, (2, 16, 3))
        self.assertEqual(arrays[f"{prefix}_input_P"].shape, (2, 16, 3))
        expected_shapes = homogenization_expected_array_shapes(
            widths=[16],
            depths=[2],
            checkpoints=[0.0],
            candidate_levels=[5, 15],
            replicas=2,
            input_dimension=3,
            sample_count=3,
        )
        self.assertEqual(set(arrays), set(expected_shapes))
        validate_homogenization_archive_schema(
            arrays,
            widths=[16],
            depths=[2],
            checkpoints=[0.0],
            candidate_levels=[5, 15],
            replicas=2,
            input_dimension=3,
            sample_count=3,
            outer_seed=551,
        )
        forbidden_fragments = (
            "_raw_forward",
            "_raw_transpose",
            "_projected_action",
            "_projected_innovation",
            "_projection_residual_P5_layer_values",
            "_projection_residual_P15_layer_values",
        )
        for key in arrays:
            self.assertFalse(
                any(fragment in key for fragment in forbidden_fragments),
                key,
            )
        self.assertIn("never stores raw layer actions", " ".join(
            (
                protocol["stage_2_homogenization"]["archive_boundary"],
                detail["storage_semantics"],
            )
        ).lower())

    def test_homogenization_schema_rejects_inventory_shape_and_rng_drift(
        self,
    ) -> None:
        protocol = runner.load_protocol()
        arguments = {
            "widths": [16],
            "depths": [2],
            "replicas": 2,
            "checkpoints": [0.0],
            "candidate_levels": [5],
            "outer_seed": 991,
            "dt": 0.02,
        }
        arrays, _detail = runner._run_homogenization(protocol, arguments)
        validator = dict(
            widths=[16],
            depths=[2],
            checkpoints=[0.0],
            candidate_levels=[5],
            replicas=2,
            input_dimension=3,
            sample_count=3,
            outer_seed=991,
        )
        validate_homogenization_archive_schema(arrays, **validator)

        missing = dict(arrays)
        missing.pop("W16_D2_t0000_terminal_H")
        with self.assertRaisesRegex(
            ArchiveValidationError, "inventory mismatch"
        ):
            validate_homogenization_archive_schema(missing, **validator)

        extra = dict(arrays)
        extra["not_preregistered"] = np.zeros(1)
        with self.assertRaisesRegex(
            ArchiveValidationError, "inventory mismatch"
        ):
            validate_homogenization_archive_schema(extra, **validator)

        malformed = dict(arrays)
        malformed["W16_D2_t0000_terminal_H"] = np.zeros((2, 15, 3))
        with self.assertRaisesRegex(
            ArchiveValidationError, "shape mismatch"
        ):
            validate_homogenization_archive_schema(malformed, **validator)

        wrong_dtype = dict(arrays)
        wrong_dtype["W16_D2_t0000_terminal_H"] = np.asarray(
            arrays["W16_D2_t0000_terminal_H"], dtype=np.float32
        )
        with self.assertRaisesRegex(
            ArchiveValidationError, "dtype mismatch"
        ):
            validate_homogenization_archive_schema(
                wrong_dtype, **validator
            )

        wrong_seed = dict(arrays)
        wrong_seed["W_replica_seeds"] = np.asarray(
            arrays["W_replica_seeds"]
        )[::-1]
        with self.assertRaisesRegex(
            ArchiveValidationError, "do not match the outer seed"
        ):
            validate_homogenization_archive_schema(wrong_seed, **validator)

    def test_forward_reconstruction_is_not_a_projection_tail(self) -> None:
        protocol = runner.load_protocol()
        model = runner._canonical_model(protocol)
        spec = runner._dense_spec(model, n=32, depth=4, seed=7401)
        master = runner.initialize_gaussian_master(
            n_max=32,
            depth_max=4,
            input_dim=3,
            seed=7401,
        )
        state = runner.materialize_coupled_state(master, spec)
        fields = runner.forward_adjoint(state, spec)
        phi = runner._orthonormal_empirical_phi(state, 5, spec.A)
        projected_forward, projected_transpose = (
            runner._projected_layer_actions(state, fields, spec, phi)
        )
        raw_forward = fields.T
        raw_transpose = np.empty_like(raw_forward)
        for layer in range(spec.depth):
            beta = fields.D[layer] * fields.P[layer + 1]
            raw_transpose[layer] = state.W[layer].T @ beta
        forward_residual = raw_forward - projected_forward
        transpose_residual = raw_transpose - projected_transpose
        forward_retained = max(
            np.linalg.norm(phi.T @ value) for value in forward_residual
        )
        transpose_retained = max(
            np.linalg.norm(phi.T @ value) for value in transpose_residual
        )
        self.assertGreater(forward_retained, 1e-6)
        self.assertLess(transpose_retained, 2e-12)

    def test_random_rank_one_satisfies_every_constraint(self) -> None:
        rng = np.random.default_rng(7)
        n = 24
        phi = rng.normal(size=(n, 5))
        hidden = rng.normal(size=(n, 3))
        beta = rng.normal(size=(n, 3))
        _, _, delta = runner.random_invisible_rank_one(
            phi, hidden, beta, alpha=0.5, seed=11
        )
        self.assertAlmostEqual(np.linalg.norm(delta), 0.5, places=12)
        self.assertLess(np.linalg.norm(delta @ phi), 2e-12)
        self.assertLess(np.linalg.norm(delta @ hidden), 2e-12)
        self.assertLess(np.linalg.norm(delta.T @ beta), 2e-12)
        self.assertAlmostEqual(
            np.sqrt(np.mean(delta * delta)), 0.5 / n, places=14
        )

    def test_coherent_rank_one_is_constrained_and_locally_optimal(self) -> None:
        rng = np.random.default_rng(71)
        n = 32
        phi = rng.normal(size=(n, 15))
        hidden = rng.normal(size=(n, 3))
        beta = rng.normal(size=(n, 3))
        hidden_velocity = rng.normal(size=(n, 3))
        cotangent = rng.normal(size=(n, 3))
        scale = 0.125
        u, v, delta, score, label = runner.coherent_invisible_rank_one(
            phi,
            hidden,
            beta,
            hidden_velocity,
            cotangent,
            objective_scale=scale,
            fallback_seed=19,
        )
        self.assertEqual(u.shape, (n,))
        self.assertEqual(v.shape, (n,))
        self.assertAlmostEqual(np.linalg.norm(delta), 1.0, places=12)
        self.assertLess(np.linalg.norm(delta @ phi), 5e-12)
        self.assertLess(np.linalg.norm(delta @ hidden), 5e-12)
        self.assertLess(np.linalg.norm(delta.T @ beta), 5e-12)
        self.assertGreater(score, 0.0)
        self.assertIn("linearized_dot_gram", label)
        direct = scale * np.sum(cotangent * (delta @ hidden_velocity))
        self.assertAlmostEqual(score, direct, places=11)
        for seed in range(20):
            _, _, candidate = runner.random_invisible_rank_one(
                phi,
                hidden,
                beta,
                alpha=1.0,
                seed=seed,
            )
            candidate_score = abs(
                scale
                * np.sum(cotangent * (candidate @ hidden_velocity))
            )
            self.assertLessEqual(candidate_score, score + 2e-11)

    def test_rank_one_factor_bundle_reconstructs_without_delta_stack(self) -> None:
        rng = np.random.default_rng(91)
        depth, n = 4, 7
        state = runner.ParamState(
            B=np.zeros((n, 2)),
            W=rng.normal(size=(depth, n, n)),
            a=np.zeros(n),
        )
        U = rng.normal(size=(depth, n))
        V = rng.normal(size=(depth, n))
        U /= np.linalg.norm(U, axis=1, keepdims=True)
        V /= np.linalg.norm(V, axis=1, keepdims=True)
        amplitude = 0.25
        attacked = runner._apply_rank_one_layer_family(
            state, U, V, amplitude=amplitude
        )
        for layer in range(depth):
            np.testing.assert_allclose(
                attacked.W[layer] - state.W[layer],
                amplitude * np.outer(U[layer], V[layer]),
            )
        np.testing.assert_array_equal(state.B, attacked.B)
        np.testing.assert_array_equal(state.a, attacked.a)


class ProtocolTests(unittest.TestCase):
    def setUp(self) -> None:
        self.protocol = runner.load_protocol()

    def test_dry_run_has_frozen_job_counts(self) -> None:
        inventory = runner.dry_run_inventory(self.protocol)
        self.assertEqual(inventory["numerics"]["active_jobs"], 78)
        self.assertEqual(
            inventory["numerics"]["phase_A_primary_jobs"], 12
        )
        self.assertEqual(
            inventory["numerics"]["phase_B_conditional_jobs"], 60
        )
        self.assertEqual(
            inventory["numerics"]["downward_diagnostic_jobs"], 6
        )
        self.assertEqual(inventory["numerics"]["conditional_P70_jobs"], 8)
        self.assertEqual(
            inventory["scaling"]["screen"]["total_trajectories"], 216
        )
        self.assertEqual(
            inventory["scaling"]["positive"]["total_trajectories"], 192
        )
        self.assertEqual(inventory["homogenization"]["dense_trajectories"], 384)
        self.assertEqual(
            inventory["homogenization"]["widths"], [128, 256, 512]
        )
        self.assertEqual(
            inventory["homogenization"]["depths"], [16, 32, 64, 128]
        )
        self.assertFalse(
            inventory["homogenization"]["raw_layer_tensors_archived"]
        )
        self.assertEqual(
            inventory["homogenization"][
                "maximum_archive_uncompressed_array_bytes_estimate"
            ],
            26039056,
        )
        self.assertEqual(
            inventory["homogenization"][
                "full_covariance_matrices_per_outer_root"
            ],
            216,
        )
        self.assertEqual(inventory["attack"]["selected_jobs"], 32)
        self.assertEqual(
            inventory["attack"]["checkpoint_trainings_per_job"], 1
        )
        self.assertEqual(
            inventory["attack"]["restart_trajectories_per_job"], 7
        )
        self.assertEqual(
            inventory["attack"]["basis_ladder"], [5, 15, 35]
        )
        self.assertEqual(inventory["attack"]["primary_basis_size"], 35)
        self.assertGreater(
            inventory["numerics"]["worst_single_state_bytes"], 0
        )
        self.assertEqual(
            inventory["numerics"]["worst_single_state_config"]["N"], 20
        )
        self.assertEqual(
            inventory["numerics"]["worst_single_state_config"]["R"], 512
        )
        self.assertEqual(
            inventory["numerics"]["worst_single_state_config"]["P"], 35
        )

    def test_active_structural_joint_is_exact_and_p70_stays_joint_free(
        self,
    ) -> None:
        stage4 = self.protocol["stage_4_generator_consistency"][
            "numerical_resolution"
        ]
        stage5 = self.protocol["stage_5_amplification"][
            "numerical_resolution"
        ]
        self.assertEqual(stage4, stage5)
        joints = [
            value
            for value in stage4[
                "one_axis_refinements_at_seed_20260723"
            ]
            if value["axis"] == "joint"
        ]
        self.assertEqual(
            joints,
            [
                {
                    "axis": "joint",
                    "base_order": 6,
                    "N": 12,
                    "R": 256,
                    "dt": 0.01,
                    "seed": 20260723,
                }
            ],
        )
        p70 = self.protocol["stage_0_integrity_and_numerics"][
            "P70_conditional_extension"
        ]["numerical_resolution"]
        self.assertFalse(p70["cofinal_joint_corner_certificate"])
        self.assertNotIn(
            "joint",
            [
                value["axis"]
                for value in p70[
                    "one_axis_refinements_at_seed_20260723"
                ]
            ],
        )

        malformed = json.loads(json.dumps(self.protocol))
        malformed["stage_5_amplification"]["numerical_resolution"][
            "one_axis_refinements_at_seed_20260723"
        ] = malformed["stage_5_amplification"]["numerical_resolution"][
            "one_axis_refinements_at_seed_20260723"
        ][:-1]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "protocol.json"
            path.write_text(json.dumps(malformed), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Stage 4 and active"):
                runner.load_protocol(path)

    def test_numerics_rejects_undeclared_and_guards_P70(self) -> None:
        base = dict(
            P=70,
            N=8,
            R=128,
            dt=0.02,
            seed=20260723,
            T=2.0,
            base_order=5,
            allow_conditional_p70=False,
        )
        with self.assertRaisesRegex(ValueError, "conditional"):
            runner._validate_numerics_config(
                self.protocol, argparse.Namespace(**base)
            )
        accepted = runner._validate_numerics_config(
            self.protocol,
            argparse.Namespace(**{**base, "allow_conditional_p70": True}),
        )
        self.assertEqual(accepted["master_levels"], [5, 15, 35, 70])
        with self.assertRaisesRegex(ValueError, "unrelated Phase-B"):
            runner._validate_numerics_config(
                self.protocol,
                argparse.Namespace(
                    **{
                        **base,
                        "allow_conditional_p70": True,
                        "allow_phase_b_refinements": True,
                    }
                ),
            )
        upward_p70 = runner._validate_numerics_config(
            self.protocol,
            argparse.Namespace(
                **{
                    **base,
                    "base_order": 6,
                    "allow_conditional_p70": True,
                }
            ),
        )
        self.assertEqual(upward_p70["M"], 1296)
        for updates in (
            {"N": 16},
            {"R": 256},
            {"dt": 0.01},
        ):
            refined = runner._validate_numerics_config(
                self.protocol,
                argparse.Namespace(
                    **{
                        **base,
                        **updates,
                        "allow_conditional_p70": True,
                    }
                ),
            )
            self.assertEqual(refined["P"], 70)
        with self.assertRaisesRegex(ValueError, "execution inventory"):
            runner._validate_numerics_config(
                self.protocol,
                argparse.Namespace(
                    **{
                        **base,
                        "N": 16,
                        "R": 256,
                        "allow_conditional_p70": True,
                    }
                ),
            )
        upward_active = runner._validate_numerics_config(
            self.protocol,
            argparse.Namespace(
                **{
                    **base,
                    "P": 35,
                    "N": 16,
                    "R": 256,
                    "base_order": 6,
                    "allow_conditional_p70": False,
                    "allow_phase_b_refinements": True,
                }
            ),
        )
        self.assertEqual(upward_active["M"], 1296)
        phase_b_without_unlock = argparse.Namespace(
            P=35,
            N=20,
            R=512,
            dt=0.01,
            seed=20260723,
            T=2.0,
            base_order=5,
            allow_conditional_p70=False,
            allow_phase_b_refinements=False,
        )
        with self.assertRaisesRegex(ValueError, "Phase-B"):
            runner._validate_numerics_config(
                self.protocol, phase_b_without_unlock
            )
        feasible_joint = runner._validate_numerics_config(
            self.protocol,
            argparse.Namespace(
                P=35,
                N=20,
                R=512,
                dt=0.01,
                seed=20260723,
                T=2.0,
                base_order=5,
                allow_conditional_p70=False,
                allow_phase_b_refinements=True,
            ),
        )
        self.assertEqual(feasible_joint["N"], 20)
        self.assertEqual(feasible_joint["R"], 512)
        self.assertEqual(
            feasible_joint["execution_phase"], "phase_B_conditional"
        )
        self.assertEqual(feasible_joint["numerical_axis"], "joint")
        paired_seed_joint = runner._validate_numerics_config(
            self.protocol,
            argparse.Namespace(
                P=35,
                N=20,
                R=512,
                dt=0.01,
                seed=20260726,
                T=2.0,
                base_order=5,
                allow_conditional_p70=False,
                allow_phase_b_refinements=True,
            ),
        )
        self.assertEqual(
            paired_seed_joint["execution_phase"], "phase_B_conditional"
        )
        phase_A = runner._validate_numerics_config(
            self.protocol,
            argparse.Namespace(
                P=35,
                N=16,
                R=256,
                dt=0.02,
                seed=20260726,
                T=2.0,
                base_order=5,
                allow_conditional_p70=False,
                allow_phase_b_refinements=False,
            ),
        )
        self.assertEqual(phase_A["execution_phase"], "phase_A_primary")
        self.assertEqual(phase_A["numerical_axis"], "primary")
        with self.assertRaisesRegex(ValueError, "conditional-P70"):
            runner._validate_numerics_config(
                self.protocol,
                argparse.Namespace(
                    P=35,
                    N=16,
                    R=256,
                    dt=0.02,
                    seed=20260726,
                    T=2.0,
                    base_order=5,
                    allow_conditional_p70=True,
                    allow_phase_b_refinements=False,
                ),
            )
        with self.assertRaisesRegex(ValueError, "only for an actual Phase-B"):
            runner._validate_numerics_config(
                self.protocol,
                argparse.Namespace(
                    P=35,
                    N=16,
                    R=256,
                    dt=0.02,
                    seed=20260726,
                    T=2.0,
                    base_order=5,
                    allow_conditional_p70=False,
                    allow_phase_b_refinements=True,
                ),
            )
        with self.assertRaisesRegex(ValueError, "execution inventory"):
            runner._validate_numerics_config(
                self.protocol,
                argparse.Namespace(
                    P=35,
                    N=32,
                    R=512,
                    dt=0.01,
                    seed=20260723,
                    T=2.0,
                    base_order=5,
                    allow_conditional_p70=False,
                    allow_phase_b_refinements=True,
                ),
            )
        with self.assertRaisesRegex(ValueError, "sparse execution inventory"):
            runner._validate_numerics_config(
                self.protocol,
                argparse.Namespace(
                    **{
                        **base,
                        "P": 5,
                        "R": 64,
                        "allow_conditional_p70": False,
                    }
                ),
            )

    def test_numerics_horizon_requires_exact_frozen_float(self) -> None:
        base = dict(
            P=70,
            N=8,
            R=128,
            dt=0.02,
            seed=20260723,
            T=2.0,
            base_order=5,
            allow_conditional_p70=True,
            allow_phase_b_refinements=False,
        )
        runner._validate_numerics_config(
            self.protocol, argparse.Namespace(**base)
        )
        for nearby in (
            np.nextafter(2.0, 0.0),
            np.nextafter(2.0, np.inf),
            2.000019,
        ):
            with self.subTest(T=nearby), self.assertRaisesRegex(
                ValueError, "active horizon"
            ):
                runner._validate_numerics_config(
                    self.protocol,
                    argparse.Namespace(**{**base, "T": float(nearby)}),
                )

        # All individual coordinates exist in a ladder, but this unplanned
        # Cartesian combination is not part of the sparse execution set.
        with self.assertRaisesRegex(ValueError, "execution inventory"):
            runner._validate_numerics_config(
                self.protocol,
                argparse.Namespace(
                    P=5,
                    N=32,
                    R=128,
                    dt=0.01,
                    seed=20260724,
                    T=2.0,
                    base_order=4,
                    allow_conditional_p70=False,
                ),
            )

    def test_attack_validator_bundles_ladder_amplitudes_and_horizons(self) -> None:
        config = runner._validate_attack_config(
            self.protocol,
            argparse.Namespace(n=256, L=32, root_index=0),
        )
        self.assertEqual(config["basis_ladder"], [5, 15, 35])
        self.assertEqual(config["primary_basis_size"], 35)
        self.assertEqual(config["amplitudes"], [0.25, 0.5, 1.0])
        self.assertEqual(config["restart_horizons"], [0.1, 0.5])
        self.assertEqual(config["maximum_restart_horizon"], 0.5)

    def test_homogenization_validator_requires_complete_coupled_grid(
        self,
    ) -> None:
        config = runner._validate_homogenization_config(
            self.protocol,
            argparse.Namespace(
                outer_root_index=2,
                depths=None,
                replicas=8,
                dt=0.02,
            ),
        )
        self.assertEqual(config["widths"], [128, 256, 512])
        self.assertEqual(config["depths"], [16, 32, 64, 128])
        self.assertEqual(config["width"], 512)
        with self.assertRaisesRegex(ValueError, "complete frozen depth grid"):
            runner._validate_homogenization_config(
                self.protocol,
                argparse.Namespace(
                    outer_root_index=2,
                    depths=(32, 64, 128),
                    replicas=8,
                    dt=0.02,
                ),
            )
        for nearby_dt in (
            np.nextafter(0.02, 0.0),
            np.nextafter(0.02, 1.0),
        ):
            with self.assertRaisesRegex(
                ValueError, "dense canonical step"
            ):
                runner._validate_homogenization_config(
                    self.protocol,
                    argparse.Namespace(
                        outer_root_index=2,
                        depths=None,
                        replicas=8,
                        dt=float(nearby_dt),
                    ),
                )

    def test_attack_roots_are_jointly_width_depth_coupled(self) -> None:
        configs = {
            (n, depth): runner._validate_attack_config(
                self.protocol,
                argparse.Namespace(n=n, L=depth, root_index=3),
            )
            for n in (256, 512)
            for depth in (32, 64)
        }
        self.assertEqual(
            {config["root_seed"] for config in configs.values()},
            {configs[(512, 64)]["root_seed"]},
        )
        self.assertEqual(
            {
                (config["master_width"], config["master_depth"])
                for config in configs.values()
            },
            {(512, 64)},
        )
        model = runner._canonical_model(self.protocol)
        master = runner.initialize_gaussian_master(
            n_max=512,
            depth_max=64,
            input_dim=3,
            seed=configs[(512, 64)]["root_seed"],
        )
        states = {}
        for (n, depth), config in configs.items():
            spec = runner._dense_spec(
                model,
                n=n,
                depth=depth,
                seed=config["root_seed"],
            )
            states[(n, depth)] = runner.materialize_coupled_state(
                master, spec
            )
        finest = states[(512, 64)]
        narrow = states[(256, 64)]
        coarse = states[(512, 32)]
        small = states[(256, 32)]
        np.testing.assert_array_equal(narrow.B, finest.B[:256])
        np.testing.assert_array_equal(narrow.a, finest.a[:256])
        np.testing.assert_allclose(
            narrow.W,
            np.sqrt(2.0) * finest.W[:, :256, :256],
            rtol=0.0,
            atol=2e-16,
        )
        np.testing.assert_allclose(
            coarse.W,
            (
                finest.W[0::2]
                + finest.W[1::2]
            )
            / np.sqrt(2.0),
            rtol=0.0,
            atol=2e-16,
        )
        np.testing.assert_allclose(
            small.W,
            finest.W[0::2, :256, :256]
            + finest.W[1::2, :256, :256],
            rtol=0.0,
            atol=3e-16,
        )

    def test_scaling_uses_complete_finest_depth_grid(self) -> None:
        common = dict(
            root_index=0,
            T=2.0,
            dt=0.02,
            n_grid=None,
            L_grid=None,
        )
        screen = runner._validate_scaling_config(
            self.protocol,
            argparse.Namespace(tier="screen", **common),
        )
        positive = runner._validate_scaling_config(
            self.protocol,
            argparse.Namespace(tier="positive", **common),
        )
        self.assertEqual(screen["common_depth_nodes"], 65)
        self.assertEqual(positive["common_depth_nodes"], 129)
        self.assertGreater(
            positive["memory_preflight_estimated_peak_bytes"], 0
        )
        with self.assertRaisesRegex(ValueError, "exact complete"):
            runner._validate_scaling_config(
                self.protocol,
                argparse.Namespace(
                    tier="positive",
                    root_index=0,
                    T=2.0,
                    dt=0.02,
                    n_grid=(128, 256, 512),
                    L_grid=(16, 32, 64, 128),
                ),
            )

    def test_scaling_horizon_and_step_require_exact_frozen_floats(
        self,
    ) -> None:
        base = dict(
            tier="screen",
            root_index=0,
            T=2.0,
            dt=0.02,
            n_grid=None,
            L_grid=None,
        )
        with mock.patch.object(
            runner,
            "available_memory_bytes",
            return_value=512 * 1024**3,
        ):
            runner._validate_scaling_config(
                self.protocol, argparse.Namespace(**base)
            )
            mutations = (
                ("T", np.nextafter(2.0, 0.0)),
                ("T", 2.000019),
                ("dt", np.nextafter(0.02, np.inf)),
                ("dt", 0.0200001),
            )
            for key, value in mutations:
                with self.subTest(key=key, value=value), self.assertRaises(
                    ValueError
                ):
                    runner._validate_scaling_config(
                        self.protocol,
                        argparse.Namespace(
                            **{**base, key: float(value)}
                        ),
                    )


if __name__ == "__main__":
    unittest.main()
