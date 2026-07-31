"""Algebraic tests for the stateful Stage 4/6 runner.

These tests do not launch a scientific PDE or dense-network trajectory.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
from pathlib import Path
from types import SimpleNamespace
import sys
import tempfile
import unittest
from unittest import mock

import numpy as np


SOURCE = Path(__file__).resolve().parents[1] / "source"
if str(SOURCE) not in sys.path:
    sys.path.insert(0, str(SOURCE))

import structural_runner as runner  # noqa: E402
from dense_pde.operator_galerkin import PDEState  # noqa: E402
from dense_reference import ParamState  # noqa: E402


class ShadowNormalizationTests(unittest.TestCase):
    def test_initialization_subtraction_occurs_before_norm(self) -> None:
        quadrature = SimpleNamespace(
            base_weights=np.ones(1),
            fast_weights=np.ones(1),
            phi=np.ones((1, 1)),
            epsilon=np.ones((1, 1)),
        )

        def state(value: float) -> PDEState:
            return PDEState(
                B=np.asarray([[value]]),
                a=np.asarray([0.0]),
                c=np.zeros((1, 1, 1, 1)),
            )

        result = runner.initialization_subtracted_errors(
            f_difference=np.asarray([[2.0], [-1.0]]),
            gram_difference=np.asarray([[[[3.0]]], [[[-2.0]]]]),
            loss_difference=np.asarray([4.0, 1.0]),
            state_difference=(state(5.0), state(2.0)),
            quadrature=quadrature,
        )
        np.testing.assert_allclose(result["raw_f"], [2.0, 1.0])
        np.testing.assert_allclose(result["increment_f"], [0.0, 3.0])
        np.testing.assert_allclose(result["raw_gram"], [3.0, 2.0])
        np.testing.assert_allclose(result["increment_gram"], [0.0, 5.0])
        np.testing.assert_allclose(result["raw_loss"], [4.0, 1.0])
        np.testing.assert_allclose(result["increment_loss"], [0.0, 3.0])
        np.testing.assert_allclose(result["raw_state"], [5.0, 2.0])
        np.testing.assert_allclose(result["increment_state"], [0.0, 3.0])

    def test_gram_norm_is_sup_depth_frobenius_not_depth_rms(self) -> None:
        quadrature = SimpleNamespace(
            base_weights=np.ones(1),
            fast_weights=np.ones(1),
            phi=np.ones((1, 1)),
            epsilon=np.ones((1, 1)),
        )

        def state() -> PDEState:
            return PDEState(
                B=np.zeros((1, 1)),
                a=np.zeros(1),
                c=np.zeros((1, 1, 1, 1)),
            )

        gram = np.zeros((2, 4, 2, 2))
        gram[0, 1, 0, 0] = 6.0
        gram[1, 1, 0, 0] = 6.0
        gram[1, 3] = np.asarray([[3.0, 4.0], [0.0, 0.0]])
        result = runner.initialization_subtracted_errors(
            f_difference=np.zeros((2, 1)),
            gram_difference=gram,
            loss_difference=np.zeros(2),
            state_difference=(state(), state()),
            quadrature=quadrature,
        )
        # A depth-RMS norm would report 3 and 2.5 respectively.  The declared
        # observable norm is the largest Frobenius norm at any one depth.
        np.testing.assert_allclose(result["raw_gram"], [6.0, 6.0])
        np.testing.assert_allclose(result["increment_gram"], [0.0, 5.0])

    def test_shadow_archive_names_sup_depth_norm_explicitly(self) -> None:
        times = np.asarray([0.0, 0.25])
        record = {
            "times": times,
            "raw_state": np.asarray([0.0, 1.0]),
            "raw_f": np.asarray([2.0, 4.0]),
            "raw_gram": np.asarray([9.0, 3.0]),
            "raw_loss": np.asarray([0.0, 0.5]),
            "increment_state": np.asarray([0.0, 1.0]),
            "increment_f": np.asarray([0.0, 4.0]),
            "increment_gram": np.asarray([0.0, 3.0]),
            "increment_loss": np.asarray([0.0, 0.5]),
        }
        arrays: dict[str, np.ndarray] = {}
        runner._add_shadow_archive_arrays(
            arrays,
            tag="P5_Q15",
            horizon_tag="h0050",
            shadow_records=(record,),
            protocol={"norms": {"S_f": 2.0, "S_G": 3.0}},
        )
        prefix = "P5_Q15_shadow_h0050"
        np.testing.assert_allclose(
            arrays[f"{prefix}_raw_observable_normalized_sup_depth"],
            [[3.0, 2.0]],
        )
        np.testing.assert_allclose(
            arrays[
                f"{prefix}_increment_observable_normalized_sup_depth"
            ],
            [[0.0, 2.0]],
        )
        np.testing.assert_array_equal(
            arrays[f"{prefix}_raw_observable_normalized"],
            arrays[f"{prefix}_raw_observable_normalized_sup_depth"],
        )
        self.assertEqual(
            arrays[
                "shadow_observable_normalized_norm_semantics_ascii"
            ].item().decode("ascii"),
            "max(||delta f||_2/S_f, sup_depth ||delta G(s)||_F/S_G)",
        )


class GeneratorArchiveContractTests(unittest.TestCase):
    def test_lift_consistency_path_is_checkpoint_by_four_and_finite(self) -> None:
        values = [
            np.asarray([index, index + 1, index + 2, index + 3])
            for index in range(3)
        ]
        path = runner._validated_lift_consistency_path(values, 3, "P5_Q15")
        self.assertEqual(path.shape, (3, 4))
        with self.assertRaisesRegex(RuntimeError, "shape mismatch"):
            runner._validated_lift_consistency_path(
                [np.zeros(4), np.zeros(4)], 3, "P5_Q15"
            )
        with self.assertRaisesRegex(FloatingPointError, "nonfinite"):
            runner._validated_lift_consistency_path(
                [np.zeros(4), np.full(4, np.nan), np.zeros(4)],
                3,
                "P5_Q15",
            )


class GainAssemblyTests(unittest.TestCase):
    def test_all_source_helper_matches_legacy_per_source_response_assembly(
        self,
    ) -> None:
        template = runner.PDESpec(
            X=np.array([[1.0, -0.35]]),
            y=np.array([0.65, -0.2]),
            basis_size=2,
            depth_nodes=2,
            base_points=8,
            fast_points=8,
            quadrature_seed=8675309,
            sigma_w=0.5,
            A=0.9,
            gamma=0.7,
            activation="tanh",
        )
        family = runner.build_nested_quadratures(
            template, levels=(2, 3), base_order=3
        )
        low_spec = family.spec(2)
        high_spec = family.spec(3)
        low_q = family.quadrature(2)
        high_q = family.quadrature(3)
        low_initial = runner.initialize_pde(low_spec, low_q)
        high_initial = runner.initialize_pde(high_spec, high_q)
        source_times = np.asarray([0.0, 0.01])
        observation_times = np.asarray([0.0, 0.01, 0.02])
        high_states = (
            high_initial,
            runner.rk4_step(high_initial, 0.01, high_spec, high_q),
        )
        residuals = tuple(
            runner.projected_back_residual(
                state, low_spec, high_spec, low_q, high_q
            )
            for state in high_states
        )

        def run(sources: np.ndarray) -> SimpleNamespace:
            return runner.stage5_serializable_result(
                low_initial,
                (),
                source_times,
                low_spec,
                high_spec,
                low_q,
                high_q,
                impulse_times=sources,
                observation_times=observation_times,
                max_step=0.01,
                nonlinear_amplitudes=(1e-3,),
                precomputed_residuals=residuals,
                serialize_residual_states=False,
            )

        combined = run(source_times)
        singles = [run(np.asarray([source])) for source in source_times]
        np.testing.assert_array_equal(
            combined.arrays["flattened_response_columns"],
            np.concatenate(
                [
                    item.arrays["flattened_response_columns"]
                    for item in singles
                ],
                axis=1,
            ),
        )
        np.testing.assert_array_equal(
            combined.arrays["group_response_gains"],
            np.stack(
                [
                    item.arrays["group_response_gains"][0]
                    for item in singles
                ]
            ),
        )
        np.testing.assert_array_equal(
            combined.arrays["column_gains"],
            np.concatenate(
                [item.arrays["column_gains"] for item in singles]
            ),
        )
        source_gains = np.asarray(
            [
                float(item.arrays["primary_residual_subspace_gain"])
                for item in singles
            ]
        )
        selected = int(np.argmax(source_gains))
        self.assertEqual(
            float(combined.arrays["primary_residual_subspace_gain"]),
            float(source_gains[selected]),
        )
        self.assertEqual(
            int(combined.arrays["maximizing_indices"][1]), selected
        )
        for key in combined.arrays:
            if key.startswith("nonlinear_"):
                np.testing.assert_array_equal(
                    combined.arrays[key], singles[selected].arrays[key]
                )

    def test_all_source_helper_is_called_once_and_preserves_statistics(
        self,
    ) -> None:
        source_times = np.asarray([0.0, 0.5, 1.0])
        observation_times = source_times.copy()
        residual_state = PDEState(
            B=np.ones((1, 1)),
            a=np.ones(1),
            c=np.ones((1, 1, 1, 1)),
        )
        spec = SimpleNamespace()
        quadrature = SimpleNamespace(
            phi=np.ones((1, 1)),
            epsilon=np.ones((1, 1)),
        )
        family = SimpleNamespace(
            spec=lambda _level: spec,
            quadrature=lambda _level: quadrature,
            raw_epsilon=np.ones((1, 1)),
        )
        group_gains = np.asarray(
            [
                [[1.0, 0.5], [1.5, 0.7], [1.2, 0.6]],
                [[0.0, 0.0], [2.0, 0.8], [3.0, 0.9]],
                [[0.0, 0.0], [0.0, 0.0], [2.5, 1.0]],
            ]
        )
        helper_arrays = {
            "source_times": source_times,
            "observation_times": observation_times,
            "residual_snapshot_times": source_times,
            "residual_snapshot_norms": np.asarray([1.0, 2.0, 3.0]),
            "residual_basis_weighted_gram": np.eye(2),
            "residual_basis_coefficients": np.ones((3, 2)),
            "residual_basis_reconstruction_error": np.asarray(
                [0.1, 0.2, 0.3]
            ),
            "observable_block_sizes": np.asarray([1, 1]),
            "impulse_times": np.repeat(source_times, 2),
            "direction_norms": np.ones(6),
            "block_response_norms": np.zeros((6, 3, 2)),
            "group_response_gains": group_gains,
            "column_gains": np.asarray([1.0, 1.5, 2.0, 2.7, 2.5, 2.2]),
            "flattened_response_columns": np.zeros((6, 6)),
            "primary_residual_subspace_gain": np.asarray(3.0),
            "atom_l1_gain": np.asarray(2.7),
            "maximizing_indices": np.asarray([3, 1, 2, 0]),
            "maximizing_atom_coefficients": np.asarray(
                [0.0, 0.0, 0.6, 0.8, 0.0, 0.0]
            ),
            "secondary_l2_singular_values": np.asarray([4.0, 1.0]),
            "secondary_l2_left_vectors": np.zeros((6, 2)),
            "secondary_l2_right_vectors": np.zeros((6, 2)),
            "secondary_l2_time_weights": np.ones(3),
            "nonlinear_times": source_times,
            "nonlinear_amplitudes": np.asarray([0.25]),
            "nonlinear_central_absolute_error": np.asarray([0.01]),
            "nonlinear_central_relative_error": np.asarray([0.02]),
            "nonlinear_plus_absolute_error": np.asarray([0.03]),
            "nonlinear_minus_absolute_error": np.asarray([0.04]),
            "nonlinear_symmetry_defect": np.asarray([0.05]),
        }
        helper_result = SimpleNamespace(
            arrays=helper_arrays, detail={"full_state_gain_computed": False}
        )
        config = {
            "low_level": 35,
            "high_level": 70,
            "conditional_p70_authorized": True,
            "closure_step_scope": (
                "next measured closure step only; not a P-to-infinity claim"
            ),
            "source_times": source_times.tolist(),
            "observation_times": observation_times.tolist(),
            "N": 1,
            "M": 1,
            "R": 1,
            "seed": 1,
            "base_order": 1,
            "dt": 0.5,
            "horizon": 1.0,
            "nonlinear_amplitudes": [0.25],
            "observable_blocks": ["f", "grams"],
            "time_grid_name": "primary",
            "resolution_axis": "primary",
            "resolution_family": "test",
            "resolution_is_primary": True,
        }
        protocol = {"norms": {"S_f": 1.0, "S_G": 1.0}}
        with (
            mock.patch.object(runner, "_make_family", return_value=family),
            mock.patch.object(
                runner.common, "preflight_pde_memory"
            ) as preflight,
            mock.patch.object(
                runner, "initialize_pde", return_value=residual_state
            ),
            mock.patch.object(
                runner, "rk4_step", side_effect=lambda state, *_: state
            ),
            mock.patch.object(
                runner,
                "projected_back_residual",
                return_value=residual_state,
            ),
            mock.patch.object(
                runner,
                "stage5_serializable_result",
                return_value=helper_result,
            ) as helper,
        ):
            arrays, detail = runner._run_gain(protocol, config)

        self.assertEqual(helper.call_count, 1)
        self.assertEqual(preflight.call_count, 2)
        high_guard, low_guard = preflight.call_args_list
        self.assertEqual(high_guard.kwargs["P"], 70)
        self.assertEqual(
            high_guard.kwargs["retained_state_equivalents"], 1.5
        )
        self.assertEqual(low_guard.kwargs["P"], 35)
        self.assertEqual(
            low_guard.kwargs["retained_state_equivalents"], 6.0
        )
        np.testing.assert_array_equal(
            helper.call_args.kwargs["impulse_times"], source_times
        )
        np.testing.assert_allclose(
            arrays["source_primary_residual_subspace_gain"],
            [1.5, 3.0, 2.5],
        )
        np.testing.assert_allclose(
            arrays["source_atom_l1_gain"], [1.5, 2.7, 2.5]
        )
        np.testing.assert_array_equal(
            arrays["residual_pair_levels"], [35, 70]
        )
        self.assertEqual(arrays["conditional_p70_authorized"].item(), 1)
        self.assertEqual(
            detail["selected_nonlinear_source_index"], 1
        )
        self.assertIn("not a full-state", detail["nonlinear_validation_scope"])
        self.assertEqual(detail["residual_pair"], [35, 70])
        self.assertTrue(detail["conditional_p70_authorized"])
        # P35 is the low-level hash here; P70 is the dynamically named high.
        self.assertIn("P35_phi", detail["quadrature_sha256"])
        self.assertIn("P70_phi", detail["quadrature_sha256"])
        self.assertIn("next measured closure", detail["closure_step_scope"])


class DenseNormTests(unittest.TestCase):
    def test_dense_coordinate_norm_uses_declared_scaling(self) -> None:
        zero = ParamState(
            B=np.zeros((2, 1)),
            W=np.zeros((2, 2, 2)),
            a=np.zeros(2),
        )
        one = ParamState(
            B=np.ones((2, 1)),
            W=np.ones((2, 2, 2)),
            a=np.ones(2),
        )
        # B contribution 1, a contribution 1, W contribution 4.
        self.assertAlmostEqual(
            runner._dense_difference_norm(one, zero), np.sqrt(6.0)
        )


class StructuralProtocolTests(unittest.TestCase):
    def setUp(self) -> None:
        self.protocol = runner.common.load_protocol()

    def conditional_gain_protocol(self) -> dict:
        protocol = deepcopy(self.protocol)
        protocol["stage_5_amplification"]["conditional_P70_extension"] = {
            "residual_pair": [35, 70],
            "trigger": (
                "Run only after the preregistered Stage-4/5 trigger "
                "authorizes the next closure step."
            ),
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
            "execution_inventory": {
                "primary_jobs_per_time_grid": 4,
                "one_axis_refinement_jobs_per_time_grid": 4,
                "time_grids": ["primary", "refined"],
                "jobs_total": 16,
                "joint_corner": None,
            },
            "interpretation": (
                "next measured closure step only; does not establish "
                "P-to-infinity convergence"
            ),
        }
        return protocol

    def test_generator_resolution_inventory_and_p70_guard(self) -> None:
        base = dict(
            N=8,
            R=128,
            dt=0.02,
            base_order=5,
            seed=20260723,
            max_level=35,
            allow_conditional_p70=False,
        )
        config = runner._validate_generator_config(
            self.protocol, argparse.Namespace(**base)
        )
        self.assertEqual(config["pairs"][-1], [5, 35])
        self.assertEqual(config["resolution_axis"], "primary")
        self.assertEqual(config["M"], 625)
        refinements = {
            "M": {"base_order": 6},
            "N": {"N": 16},
            "R": {"R": 256},
            "dt": {"dt": 0.01},
        }
        for axis, updates in refinements.items():
            refined = runner._validate_generator_config(
                self.protocol,
                argparse.Namespace(**{**base, **updates}),
            )
            self.assertEqual(refined["resolution_axis"], axis)
            self.assertFalse(refined["resolution_is_primary"])
        joint = runner._validate_generator_config(
            self.protocol,
            argparse.Namespace(
                **{
                    **base,
                    "base_order": 6,
                    "N": 12,
                    "R": 256,
                    "dt": 0.01,
                }
            ),
        )
        self.assertEqual(joint["resolution_axis"], "joint")
        self.assertEqual(
            runner._validate_generator_config(
                self.protocol,
                argparse.Namespace(**{**base, "base_order": 6}),
            )["M"],
            1296,
        )
        resolution_arrays = runner._resolution_arrays(
            runner._validate_generator_config(
                self.protocol,
                argparse.Namespace(**{**base, "base_order": 6}),
            )
        )
        self.assertEqual(
            resolution_arrays[
                "numerical_resolution_axis_ascii"
            ].item(),
            b"M",
        )
        self.assertEqual(
            resolution_arrays["numerical_resolution_base_order"].item(),
            6,
        )
        self.assertEqual(
            resolution_arrays["numerical_resolution_M"].item(),
            1296,
        )
        self.assertEqual(
            resolution_arrays[
                "numerical_resolution_family_ascii"
            ].item(),
            b"stage_4_generator_consistency_active",
        )
        with self.assertRaisesRegex(
            ValueError, "structural numerical-resolution inventory"
        ):
            runner._validate_generator_config(
                self.protocol,
                argparse.Namespace(
                    **{**base, "R": 256, "seed": 20260724}
                ),
            )
        with self.assertRaisesRegex(
            ValueError, "structural numerical-resolution inventory"
        ):
            runner._validate_generator_config(
                self.protocol,
                argparse.Namespace(**{**base, "N": 16, "R": 256}),
            )
        with self.assertRaisesRegex(ValueError, "authorization"):
            runner._validate_generator_config(
                self.protocol,
                argparse.Namespace(**{**base, "max_level": 70}),
            )
        with self.assertRaisesRegex(ValueError, "only for a max-level=70"):
            runner._validate_generator_config(
                self.protocol,
                argparse.Namespace(
                    **{**base, "allow_conditional_p70": True}
                ),
            )
        p70_base = {
            **base,
            "max_level": 70,
            "allow_conditional_p70": True,
        }
        extended = runner._validate_generator_config(
            self.protocol,
            argparse.Namespace(**p70_base),
        )
        self.assertEqual(extended["pairs"][-1], [35, 70])
        self.assertIn([15, 35], extended["pairs"])
        self.assertEqual(
            extended["resolution_family"], "conditional_P70_nested"
        )
        for axis, updates in refinements.items():
            p70_refined = runner._validate_generator_config(
                self.protocol,
                argparse.Namespace(**{**p70_base, **updates}),
            )
            self.assertEqual(p70_refined["resolution_axis"], axis)
            self.assertEqual(
                p70_refined["resolution_family"],
                "conditional_P70_nested",
            )
        extended_M = runner._validate_generator_config(
            self.protocol,
            argparse.Namespace(
                **{
                    **p70_base,
                    "base_order": 6,
                }
            ),
        )
        self.assertEqual(extended_M["M"], 1296)
        with self.assertRaisesRegex(
            ValueError, "conditional P70 generator configuration"
        ):
            runner._validate_generator_config(
                self.protocol,
                argparse.Namespace(
                    **{
                        **p70_base,
                        "N": 16,
                        "R": 256,
                    }
                ),
            )

    def test_structural_and_tail_floats_require_exact_protocol_values(
        self,
    ) -> None:
        generator = dict(
            N=8,
            R=128,
            dt=0.02,
            base_order=5,
            seed=20260723,
            max_level=35,
            allow_conditional_p70=False,
        )
        runner._validate_generator_config(
            self.protocol, argparse.Namespace(**generator)
        )
        for nearby in (
            np.nextafter(0.02, 0.0),
            np.nextafter(0.02, np.inf),
            0.0200000000000005,
        ):
            with self.subTest(generator_dt=nearby), self.assertRaisesRegex(
                ValueError, "resolution inventory"
            ):
                runner._validate_generator_config(
                    self.protocol,
                    argparse.Namespace(
                        **{**generator, "dt": float(nearby)}
                    ),
                )

        tail_pde = dict(
            N=16,
            R=256,
            dt=0.02,
            base_order=5,
            seed=20260723,
            block_end=2.0,
            restart_from=None,
        )
        runner._validate_tail_pde_config(
            self.protocol, argparse.Namespace(**tail_pde)
        )
        for key, nearby in (
            ("dt", np.nextafter(0.02, np.inf)),
            ("dt", 0.0200001),
            ("block_end", np.nextafter(2.0, np.inf)),
            ("block_end", 2.000019),
        ):
            with self.subTest(key=key, value=nearby), self.assertRaises(
                ValueError
            ):
                runner._validate_tail_pde_config(
                    self.protocol,
                    argparse.Namespace(
                        **{**tail_pde, key: float(nearby)}
                    ),
                )

        tail_dense = dict(root_index=0, horizon=32.0, dt=0.02)
        runner._validate_tail_dense_config(
            self.protocol, argparse.Namespace(**tail_dense)
        )
        for key, nearby in (
            ("dt", np.nextafter(0.02, 0.0)),
            ("dt", 0.0200001),
            ("horizon", np.nextafter(32.0, np.inf)),
            ("horizon", 32.0003),
        ):
            with self.subTest(key=key, value=nearby), self.assertRaises(
                ValueError
            ):
                runner._validate_tail_dense_config(
                    self.protocol,
                    argparse.Namespace(
                        **{**tail_dense, key: float(nearby)}
                    ),
                )

    def test_tail_restart_config_and_endpoint_are_exact(self) -> None:
        primary = runner._primary_pde_config(self.protocol)
        base_config = {
            **primary,
            "P": 5,
            "seed": 20260723,
            "block_start": 0.0,
            "block_end": 2.0,
            "sample_dt": float(
                self.protocol["norms"]["time_sampling"]
            ),
            "finite_horizon_only": True,
            "restart_seal_sha256": None,
            "canonical_model": runner.common._jsonable(
                runner.common._canonical_model(self.protocol)
            ),
        }

        def write_restart(
            path: Path,
            *,
            config: dict,
            endpoint_time: float,
        ) -> None:
            arrays = {
                "endpoint_time": np.asarray(
                    endpoint_time, dtype=np.float64
                ),
                "endpoint_B": np.zeros((1, 1)),
                "endpoint_a": np.zeros(1),
                "endpoint_c": np.zeros((1, 1, 1, 1)),
            }
            sealed = runner.common.build_sealed_archive(
                stage="tail_pde",
                config=config,
                arrays=arrays,
                protocol_sha256=runner.common._sha256_file(
                    runner.common.PROTOCOL_PATH
                ),
                source_hashes={"unit": "a" * 64},
            )
            runner.common.atomic_save_npz(
                path, arrays, sealed.metadata
            )

        args = dict(
            N=16,
            R=256,
            dt=0.02,
            base_order=5,
            seed=20260723,
            block_end=4.0,
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            valid = root / "valid.npz"
            write_restart(
                valid, config=base_config, endpoint_time=2.0
            )
            accepted = runner._validate_tail_pde_config(
                self.protocol,
                argparse.Namespace(**args, restart_from=valid),
            )
            self.assertEqual(accepted["block_start"], 2.0)

            bad_config_path = root / "bad_config.npz"
            write_restart(
                bad_config_path,
                config={
                    **base_config,
                    "dt": float(np.nextafter(0.02, np.inf)),
                },
                endpoint_time=2.0,
            )
            with self.assertRaisesRegex(
                ValueError, "not exactly"
            ):
                runner._validate_tail_pde_config(
                    self.protocol,
                    argparse.Namespace(
                        **args, restart_from=bad_config_path
                    ),
                )

            bad_endpoint_path = root / "bad_endpoint.npz"
            write_restart(
                bad_endpoint_path,
                config=base_config,
                endpoint_time=float(np.nextafter(2.0, np.inf)),
            )
            with self.assertRaisesRegex(
                ValueError, "endpoint time"
            ):
                runner._validate_tail_pde_config(
                    self.protocol,
                    argparse.Namespace(
                        **args, restart_from=bad_endpoint_path
                    ),
                )

    def test_tail_boundaries_are_contiguous_and_finite(self) -> None:
        boundaries = runner._tail_boundaries(self.protocol)
        self.assertEqual(boundaries[0], (0.0, 2.0))
        self.assertEqual(boundaries[-1], (64.0, 128.0))
        for left, right in zip(boundaries[:-1], boundaries[1:]):
            self.assertEqual(left[1], right[0])
        inventory = runner.structural_inventory(self.protocol)
        self.assertIn("finite-horizon", inventory["claim_boundary"])
        self.assertEqual(
            inventory["generator"]["full_checkpoint_states_archived"], 0
        )
        self.assertEqual(
            inventory["generator"]["resolution_axes"],
            ["M", "N", "R", "dt", "joint"],
        )
        self.assertEqual(inventory["generator"]["jobs_total"], 9)
        self.assertEqual(
            inventory["generator"]["primary_numerics"]["N"], 8
        )
        self.assertEqual(
            inventory["generator"]["primary_numerics"]["R"], 128
        )
        self.assertEqual(
            inventory["generator"]["conditional_P70"]["jobs_total"], 8
        )
        self.assertEqual(
            inventory["generator"]["conditional_P70"][
                "primary_numerics"
            ]["N"],
            8,
        )
        self.assertEqual(inventory["gain"]["jobs_total"], 36)
        self.assertEqual(inventory["gain"]["primary_numerics"]["N"], 8)
        self.assertEqual(
            inventory["gain"]["full_high_level_states_archived"], 0
        )
        conditional_inventory = runner.structural_inventory(
            self.conditional_gain_protocol()
        )["gain"]
        self.assertTrue(
            conditional_inventory["conditional_P70"]["declared"]
        )
        self.assertEqual(
            conditional_inventory["conditional_P70"]["residual_pair"],
            [35, 70],
        )
        self.assertEqual(
            conditional_inventory["conditional_P70"]["jobs_per_time_grid"],
            8,
        )
        self.assertEqual(
            conditional_inventory["conditional_P70"]["jobs_total"], 16
        )
        self.assertEqual(
            conditional_inventory[
                "maximum_jobs_total_including_conditional_P70"
            ],
            52,
        )
        parser = runner.build_parser()
        parsed_generator = parser.parse_args(
            ["generator", "--seed", "20260723"]
        )
        parsed_gain = parser.parse_args(
            [
                "gain",
                "--seed",
                "20260723",
                "--low-level",
                "5",
                "--time-grid",
                "primary",
            ]
        )
        self.assertEqual(
            (parsed_generator.N, parsed_generator.R), (8, 128)
        )
        self.assertEqual((parsed_gain.N, parsed_gain.R), (8, 128))
        self.assertFalse(parsed_gain.allow_conditional_p70)

    def test_gain_grids_and_positive_amplitudes_are_frozen(self) -> None:
        base = dict(
            N=8,
            R=128,
            dt=0.02,
            base_order=5,
            seed=20260723,
            time_grid="primary",
            low_level=5,
        )
        primary = runner._validate_gain_config(
            self.protocol, argparse.Namespace(**base)
        )
        refined = runner._validate_gain_config(
            self.protocol,
            argparse.Namespace(**{**base, "time_grid": "refined"}),
        )
        self.assertEqual(primary["source_times"][0], 0.0)
        self.assertEqual(primary["source_times"][-1], 2.0)
        self.assertGreater(
            len(refined["source_times"]), len(primary["source_times"])
        )
        self.assertEqual(
            primary["nonlinear_amplitudes"], [0.25, 0.5, 1.0]
        )
        level15 = runner._validate_gain_config(
            self.protocol,
            argparse.Namespace(**{**base, "low_level": 15}),
        )
        self.assertEqual(primary["low_level"], 5)
        self.assertEqual(level15["low_level"], 15)
        for axis, updates in {
            "M": {"base_order": 6},
            "N": {"N": 16},
            "R": {"R": 256},
            "dt": {"dt": 0.01},
        }.items():
            resolved = runner._validate_gain_config(
                self.protocol,
                argparse.Namespace(**{**base, **updates}),
            )
            self.assertEqual(resolved["resolution_axis"], axis)
        joint = runner._validate_gain_config(
            self.protocol,
            argparse.Namespace(
                **{
                    **base,
                    "base_order": 6,
                    "N": 12,
                    "R": 256,
                    "dt": 0.01,
                }
            ),
        )
        self.assertEqual(joint["resolution_axis"], "joint")
        with self.assertRaisesRegex(
            ValueError, "structural numerical-resolution inventory"
        ):
            runner._validate_gain_config(
                self.protocol,
                argparse.Namespace(**{**base, "N": 16, "R": 256}),
            )
        with self.assertRaisesRegex(ValueError, "time grid"):
            runner._validate_gain_config(
                self.protocol,
                argparse.Namespace(**{**base, "time_grid": "rule"}),
            )

    def test_conditional_p70_gain_pair_and_authorization_are_exact(self) -> None:
        protocol = self.conditional_gain_protocol()
        base = dict(
            N=8,
            R=128,
            dt=0.02,
            base_order=5,
            seed=20260723,
            time_grid="primary",
            low_level=35,
            high_level=70,
            allow_conditional_p70=True,
        )
        primary = runner._validate_gain_config(
            protocol, argparse.Namespace(**base)
        )
        self.assertEqual(
            (primary["low_level"], primary["high_level"]), (35, 70)
        )
        self.assertTrue(primary["conditional_p70_authorized"])
        self.assertEqual(
            primary["resolution_family"], "conditional_P70_gain"
        )
        self.assertIn("next measured closure", primary["closure_step_scope"])
        for axis, updates in {
            "M": {"base_order": 6},
            "N": {"N": 16},
            "R": {"R": 256},
            "dt": {"dt": 0.01},
        }.items():
            refined = runner._validate_gain_config(
                protocol, argparse.Namespace(**{**base, **updates})
            )
            self.assertEqual(refined["resolution_axis"], axis)
            self.assertEqual(
                refined["resolution_family"], "conditional_P70_gain"
            )

        forbidden = (
            (
                {**base, "allow_conditional_p70": False},
                "explicit --allow-conditional-p70",
            ),
            ({**base, "high_level": 35}, "exactly low=35, high=70"),
            (
                {
                    **base,
                    "low_level": 15,
                    "high_level": 70,
                },
                "valid only for the exact",
            ),
        )
        for candidate, message in forbidden:
            with self.subTest(candidate=candidate):
                with self.assertRaisesRegex(ValueError, message):
                    runner._validate_gain_config(
                        protocol, argparse.Namespace(**candidate)
                    )

        missing = deepcopy(protocol)
        del missing["stage_5_amplification"][
            "conditional_P70_extension"
        ]
        with self.assertRaisesRegex(ValueError, "not preregistered"):
            runner._validate_gain_config(
                missing, argparse.Namespace(**base)
            )

        malformed = deepcopy(protocol)
        malformed["stage_5_amplification"][
            "conditional_P70_extension"
        ]["residual_pair"] = [15, 70]
        with self.assertRaisesRegex(ValueError, "exactly residual_pair"):
            runner._validate_gain_config(
                malformed, argparse.Namespace(**base)
            )
        malformed_inventory = self.conditional_gain_protocol()
        malformed_inventory["stage_5_amplification"][
            "conditional_P70_extension"
        ]["execution_inventory"]["jobs_total"] = 15
        with self.assertRaisesRegex(ValueError, "inventory mismatch"):
            runner._validate_gain_config(
                malformed_inventory, argparse.Namespace(**base)
            )

        parser = runner.build_parser()
        parsed = parser.parse_args(
            [
                "gain",
                "--seed",
                "20260723",
                "--low-level",
                "35",
                "--high-level",
                "70",
                "--time-grid",
                "refined",
                "--allow-conditional-p70",
            ]
        )
        parsed_config = runner._validate_gain_config(protocol, parsed)
        self.assertEqual(parsed_config["high_level"], 70)
        self.assertEqual(parsed_config["time_grid_name"], "refined")


if __name__ == "__main__":
    unittest.main()
