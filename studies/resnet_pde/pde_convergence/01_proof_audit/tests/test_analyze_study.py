"""Synthetic, non-scientific tests for the proof-obligation analyzer."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
if str(SOURCE) not in sys.path:
    sys.path.insert(0, str(SOURCE))

from analyze_study import (  # noqa: E402
    _mc_upper_quantile_index,
    AlignmentGrid,
    ArchiveValidationError,
    AttackCell,
    GateStatus,
    GeneratorResidualSeries,
    InnovationSamples,
    ObservableCurve,
    ObservableEnsemble,
    aggregate_error_ledger,
    analyze_attack_scaling,
    analyze_generator_residuals,
    analyze_homogenization,
    analyze_numerical_cauchy,
    analyze_ordered_scaling,
    finalize_runner_stage_archive,
    full_curve_distance,
    load_sealed_stage_archive,
    whole_root_familywise_bootstrap,
)
import run_study as runner  # noqa: E402


def _canonical_hash(value: object) -> str:
    payload = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode()
    return hashlib.sha256(payload).hexdigest()


def _curve(
    *,
    output_gain: float = 1.0,
    output_offset: float = 0.0,
    gram_gain: float = 1.0,
) -> ObservableCurve:
    times = np.array([0.0, 0.5, 1.0])
    depths = np.array([0.0, 0.5, 1.0])
    f = output_offset + output_gain * times[:, None]
    gram = np.empty((times.size, depths.size, 1, 1))
    gram[:, :, 0, 0] = (
        gram_gain * times[:, None] + 0.25 * depths[None, :]
    )
    return ObservableCurve(times, depths, f, gram)


class RunnerArchiveIntegrationTests(unittest.TestCase):
    def test_atomic_runner_archive_requires_explicit_sealing_then_analyzes(
        self,
    ) -> None:
        protocol_hash = "a" * 64
        source_hash = "b" * 64
        freeze_hash = "c" * 64
        config = {"case": {"id": "synthetic"}, "dt": 0.1}
        metadata = {
            "archive_schema": 1,
            "stage": "unit-analysis",
            "protocol_sha256": protocol_hash,
            "source_sha256": {"runner": source_hash},
            "config": config,
            "config_sha256": _canonical_hash(config),
        }
        curve = _curve()
        arrays = {
            "times": curve.times,
            "depths": curve.depths,
            "f": curve.f,
            "gram": curve.gram,
        }
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "runner-result.npz"
            self.assertEqual(
                runner.atomic_save_npz(path, arrays, metadata),
                "written",
            )
            with self.assertRaisesRegex(
                ArchiveValidationError, "missing provenance"
            ):
                load_sealed_stage_archive(
                    path,
                    required_config_keys=("case.id", "dt"),
                    required_arrays=tuple(arrays),
                )

            sealed = finalize_runner_stage_archive(
                path,
                frozen_inputs_sha256=freeze_hash,
                required_config_keys=("case.id", "dt"),
                required_arrays=tuple(arrays),
                expected_stage="unit-analysis",
                expected_protocol_sha256=protocol_hash,
                expected_source_hashes={"runner": source_hash},
            )
            loaded = load_sealed_stage_archive(
                sealed,
                required_config_keys=("case.id", "dt"),
                required_arrays=tuple(arrays),
                expected_stage="unit-analysis",
                expected_protocol_sha256=protocol_hash,
            )
            loaded_curve = ObservableCurve(
                loaded.arrays["times"],
                loaded.arrays["depths"],
                loaded.arrays["f"],
                loaded.arrays["gram"],
            )
            distance = full_curve_distance(
                loaded_curve,
                curve,
                grid=AlignmentGrid(curve.times, curve.depths),
                s_f=1.0,
                s_g=1.0,
            )
            self.assertEqual(distance.combined, 0.0)
            self.assertEqual(
                sealed.metadata["frozen_inputs_sha256"], freeze_hash
            )

            tampered = {
                "metadata": dict(sealed.metadata),
                "arrays": {
                    **sealed.arrays,
                    "f": sealed.arrays["f"] + 1.0,
                },
            }
            with self.assertRaisesRegex(
                ArchiveValidationError, "array hash mismatch"
            ):
                load_sealed_stage_archive(
                    tampered,
                    required_config_keys=("case.id",),
                    required_arrays=("f",),
                )

    def test_runner_finalizer_fails_on_missing_config_provenance(self) -> None:
        config = {"case": {"id": "synthetic"}}
        metadata = {
            "archive_schema": 1,
            "stage": "unit-analysis",
            "protocol_sha256": "a" * 64,
            "source_sha256": {"runner": "b" * 64},
            "config": config,
            "config_sha256": _canonical_hash(config),
        }
        with self.assertRaisesRegex(
            ArchiveValidationError, "missing required config key"
        ):
            finalize_runner_stage_archive(
                {"metadata": metadata, "arrays": {"x": np.ones(2)}},
                frozen_inputs_sha256="c" * 64,
                required_config_keys=("case.missing",),
                required_arrays=("x",),
            )


class DistanceAndBootstrapTests(unittest.TestCase):
    def test_alignment_absolute_and_motion_distances_are_fixed(self) -> None:
        left = _curve(output_gain=1.0)
        right = _curve(output_gain=2.0)
        grid = AlignmentGrid(
            np.linspace(0.0, 1.0, 5),
            np.linspace(0.0, 1.0, 5),
        )
        absolute = full_curve_distance(
            left,
            right,
            grid=grid,
            s_f=2.0,
            s_g=1.0,
            mode="absolute",
        )
        self.assertAlmostEqual(absolute.output, 0.5)
        self.assertAlmostEqual(absolute.gram, 0.0)
        self.assertAlmostEqual(absolute.combined, 0.5)

        motion = full_curve_distance(
            left,
            right,
            grid=grid,
            s_f=999.0,
            s_g=999.0,
            mode="motion",
        )
        self.assertAlmostEqual(motion.output_scale, 2.0)
        self.assertAlmostEqual(motion.output, 0.5)
        self.assertAlmostEqual(motion.gram, 0.0)

    def test_bootstrap_reuses_one_whole_root_draw_for_every_statistic(
        self,
    ) -> None:
        values = np.arange(8.0)

        def statistic(indices: np.ndarray) -> dict[str, float]:
            mean = float(np.mean(values[indices]))
            return {"first": mean, "translated": mean + 7.0}

        band = whole_root_familywise_bootstrap(
            root_count=values.size,
            statistic=statistic,
            replicates=80,
            pilot_replicates=20,
            seed=71,
            confidence=0.95,
            mc_failure_probability=0.2,
        )
        np.testing.assert_allclose(
            band.replicates["translated"] - band.replicates["first"],
            7.0,
            rtol=0.0,
            atol=1e-14,
        )
        self.assertGreaterEqual(band.critical_upper, 0.0)
        self.assertGreaterEqual(band.critical_lower, 0.0)
        self.assertEqual(band.critical_lower, band.critical_upper)
        self.assertEqual(band.pilot_replicates, 20)
        self.assertEqual(band.critical_replicates, 80)

    def test_finite_bootstrap_quantile_uses_binomial_mc_guard(self) -> None:
        index, assurance = _mc_upper_quantile_index(
            replicates=20000,
            probability=0.9976666666666667,
            failure_probability=0.001 / 13.0,
        )
        self.assertEqual(index, 19977)
        self.assertGreaterEqual(assurance, 1.0 - 0.001 / 13.0)
        with self.assertRaisesRegex(
            ValueError, "cannot attain the declared quantile assurance"
        ):
            _mc_upper_quantile_index(
                replicates=4000,
                probability=0.9976666666666667,
                failure_probability=0.001 / 13.0,
            )

    def test_familywise_band_is_invariant_to_statistic_units(self) -> None:
        values = np.linspace(-1.0, 2.0, 18)

        def statistic(indices: np.ndarray) -> dict[str, float]:
            mean = float(np.mean(values[indices]))
            return {"small_units": mean, "large_units": 1000.0 * mean}

        band = whole_root_familywise_bootstrap(
            root_count=values.size,
            statistic=statistic,
            replicates=120,
            pilot_replicates=30,
            seed=17,
            confidence=0.95,
            mc_failure_probability=0.2,
        )
        small_width = float(
            band.upper["small_units"] - band.point["small_units"]
        )
        large_width = float(
            band.upper["large_units"] - band.point["large_units"]
        )
        self.assertAlmostEqual(large_width / small_width, 1000.0, places=10)


class ScalingAndNumericsTests(unittest.TestCase):
    def _scaling_ensemble(
        self,
        width: int,
        physical_depth: int,
        root_effects: np.ndarray,
    ) -> ObservableEnsemble:
        times = np.array([0.0, 1.0])
        depths = np.array([0.0, 1.0])
        systematic = (
            0.08 * 128.0 / width
            + 0.06 * 16.0 / physical_depth
        )
        noise_scale = 0.002 * np.sqrt(128.0 / width)
        f = np.zeros((root_effects.size, times.size, 1))
        f[:, 1, 0] = (
            0.2 + systematic + noise_scale * root_effects
        )
        gram = np.zeros(
            (root_effects.size, times.size, depths.size, 1, 1)
        )
        return ObservableEnsemble(
            np.arange(root_effects.size),
            times,
            depths,
            f,
            gram,
        )

    def test_ordered_width_then_depth_scaling_and_conditional_tails(
        self,
    ) -> None:
        widths = (128, 256, 512, 1024)
        depths = (16, 32, 64, 128)
        root_effects = np.linspace(-1.0, 1.0, 24)
        ensembles = {
            (width, depth): self._scaling_ensemble(
                width, depth, root_effects
            )
            for width in widths
            for depth in depths
        }
        summary = analyze_ordered_scaling(
            ensembles,
            grid=AlignmentGrid([0.0, 1.0], [0.0, 1.0]),
            s_f=1.0,
            s_g=1.0,
            bootstrap_replicates=80,
            bootstrap_pilot_replicates=20,
            bootstrap_mc_failure_probability=0.99,
            bootstrap_seed=5,
        )
        self.assertEqual(summary.gate.status, GateStatus.PASS)
        for slope in summary.concentration_slopes.values():
            self.assertAlmostEqual(slope, -0.5, places=11)
        for ratios in summary.width_ratios.values():
            np.testing.assert_allclose(ratios, (0.5, 0.5), atol=1e-11)
        # Depth corrections conservatively include the width-tail balls on
        # both adjacent depth curves: (.03,.015,.0075) + .01 + .01.
        np.testing.assert_allclose(
            summary.depth_ratios, (0.7, 0.0275 / 0.035), atol=1e-11
        )
        self.assertTrue(
            summary.gate.metrics["conditional_geometric_tails"]
        )
        self.assertTrue(
            all(value is not None for value in summary.width_tail_conditional.values())
        )
        self.assertIsNotNone(summary.depth_tail_conditional)

    def test_numerical_cauchy_requires_bounds_and_applies_nuisance_rule(
        self,
    ) -> None:
        curves = {
            "base": _curve(),
            "refined": _curve(output_offset=0.001),
        }
        kwargs = dict(
            curves=curves,
            comparisons=(("dt", "base", "refined"),),
            grid=AlignmentGrid(
                np.linspace(0.0, 1.0, 5),
                np.linspace(0.0, 1.0, 5),
            ),
            s_f=1.0,
            s_g=1.0,
            allocation=0.005,
        )
        missing = analyze_numerical_cauchy(
            **kwargs,
            upper_bounds=None,
        )
        self.assertEqual(missing.gate.status, GateStatus.UNRESOLVED)
        self.assertIn(
            "CAUCHY_UNCERTAINTY_MISSING", missing.gate.reason_codes
        )
        passed = analyze_numerical_cauchy(
            **kwargs,
            upper_bounds={"dt": 0.004},
            discrepancy_lcb=0.03,
        )
        self.assertEqual(passed.gate.status, GateStatus.PASS)


class HomogenizationAndGeneratorTests(unittest.TestCase):
    def test_variance_bias_and_full_covariance_summaries(self) -> None:
        outer = 4
        replica_pattern = np.array([-1.0, 1.0, -1.0, 1.0])
        # Identical outer-root laws make the exact L^-1 construction
        # bootstrap-invariant; other tests exercise nonzero band widths.
        root_scale = np.ones(outer)
        base = (
            root_scale[:, None, None]
            * replica_pattern[None, :, None]
        )
        depths = (16, 32, 64, 128)
        hidden = {
            depth: InnovationSamples(base / np.sqrt(depth), layered=False)
            for depth in depths
        }
        candidate = {}
        for depth in depths:
            layered = (
                base[:, :, None, :]
                * np.ones((1, 1, depth, 1))
                / np.sqrt(depth)
            )
            candidate[depth] = InnovationSamples(layered, layered=True)
        summary = analyze_homogenization(
            {"hidden": hidden, "candidate_P15": candidate},
            model_free_fields=("hidden",),
            candidate_fields=("candidate_P15",),
            candidate_bias_allocation=10.0,
            bootstrap_replicates=60,
            bootstrap_pilot_replicates=20,
            bootstrap_mc_failure_probability=0.99,
            bootstrap_seed=9,
            conditional_mean_tested=True,
        )
        self.assertEqual(summary.gate.status, GateStatus.PASS)
        self.assertAlmostEqual(
            summary.fields["hidden"].variance_slope, -1.0, places=12
        )
        # Outer-root laws are identical in this fixture, so this nonzero
        # interval width can only come from the frozen within-root W-replica
        # resampling layer.
        self.assertGreater(
            summary.familywise_band.upper["hidden/variance/L16"],
            summary.familywise_band.lower["hidden/variance/L16"],
        )
        self.assertAlmostEqual(
            summary.fields[
                "candidate_P15"
            ].integrated_covariance_slope,
            -1.0,
            places=12,
        )
        for depth in depths:
            covariance = summary.fields[
                "candidate_P15"
            ].by_depth[depth].covariance
            self.assertEqual(covariance.shape, (depth, depth))
        self.assertEqual(
            summary.fields["candidate_P15"].bias_norm_at_max_depth,
            0.0,
        )
        unresolved = analyze_homogenization(
            {"hidden": hidden, "candidate_P15": candidate},
            model_free_fields=("hidden",),
            candidate_fields=("candidate_P15",),
            candidate_bias_allocation=10.0,
            bootstrap_replicates=20,
            bootstrap_pilot_replicates=10,
            bootstrap_mc_failure_probability=0.99,
            bootstrap_seed=10,
        )
        self.assertEqual(unresolved.gate.status, GateStatus.UNRESOLVED)
        self.assertIn(
            "HOMOGENIZATION_CONDITIONAL_MEAN_NOT_TESTED",
            unresolved.gate.reason_codes,
        )

    def test_all_negative_bias_u_statistic_keeps_signed_uncertainty(self) -> None:
        depths = (16, 32, 64, 128)
        root_scale = np.linspace(0.7, 1.4, 8)
        opposite_replicas = np.stack((root_scale, -root_scale), axis=1)[
            :, :, None
        ]
        samples = {
            depth: InnovationSamples(
                opposite_replicas / np.sqrt(depth),
                layered=False,
            )
            for depth in depths
        }
        summary = analyze_homogenization(
            {"candidate": samples},
            model_free_fields=("candidate",),
            candidate_fields=("candidate",),
            candidate_bias_allocation=0.001,
            bootstrap_replicates=200,
            bootstrap_pilot_replicates=40,
            bootstrap_mc_failure_probability=0.99,
            bootstrap_seed=911,
            conditional_mean_tested=True,
        )
        key = "candidate/bias_squared/L128"
        band = summary.familywise_band
        self.assertLess(band.point[key], 0.0)
        self.assertLess(band.upper[key], 0.0)
        self.assertGreater(band.upper[key], band.lower[key])
        self.assertLess(
            summary.fields["candidate"].bias_squared_at_max_depth, 0.0
        )
        self.assertEqual(
            summary.fields["candidate"].bias_norm_upper_at_max_depth,
            0.0,
        )

    def test_noncontracting_width_correction_is_unresolved_not_failure(
        self,
    ) -> None:
        depths = (16, 32, 64, 128)
        replica_pattern = np.asarray(
            [-3.0, -2.0, -1.0, 0.0, 0.0, 1.0, 2.0, 3.0]
        )[None, :, None]
        base = np.repeat(replica_pattern, 4, axis=0)
        scales = {128: 1.0, 256: 2.0, 512: 10.0}
        fields = {
            f"field_n{width}": {
                depth: InnovationSamples(
                    scale * base / np.sqrt(depth),
                    layered=False,
                )
                for depth in depths
            }
            for width, scale in scales.items()
        }
        summary = analyze_homogenization(
            fields,
            model_free_fields=tuple(fields),
            candidate_fields=(),
            candidate_bias_allocation=1.0,
            bootstrap_replicates=60,
            bootstrap_pilot_replicates=20,
            bootstrap_mc_failure_probability=0.99,
            bootstrap_seed=919,
            conditional_mean_tested=True,
            width_ladders={
                "field": {
                    width: f"field_n{width}" for width in scales
                }
            },
        )
        self.assertEqual(summary.gate.status, GateStatus.UNRESOLVED)
        self.assertIn(
            "HOMOGENIZATION_WIDTH_RESOLUTION_NONCONTRACTING",
            summary.gate.reason_codes,
        )
        self.assertNotIn(
            "HOMOGENIZATION_VARIANCE_NONDECAY",
            summary.gate.reason_codes,
        )
        self.assertGreaterEqual(
            summary.familywise_band.lower[
                "width/field/variance/ratio"
            ],
            1.0,
        )

    @staticmethod
    def _generator_series(level: float) -> GeneratorResidualSeries:
        roots = 6
        times = np.array([0.0, 1.0, 2.0])
        path = np.full((roots, times.size), level)
        shadow = np.full((roots, 2), 0.5 * level)
        return GeneratorResidualSeries(
            times,
            path,
            1.2 * path,
            0.8 * path,
            shadow,
        )

    def test_generator_direct_pair_is_diagnostic_and_chain_reaches_p70(
        self,
    ) -> None:
        series = {
            (5, 15): self._generator_series(1.0),
            (15, 35): self._generator_series(0.4),
            (5, 35): self._generator_series(0.6),
            (35, 70): self._generator_series(0.1),
        }
        bounds = {
            (pair, metric): 0.001
            for pair in series
            for metric in ("back", "outgoing", "observable", "shadow")
        }
        summary = analyze_generator_residuals(
            series,
            numerical_upper_bounds=bounds,
            numerics_allocation=0.005,
            bootstrap_replicates=40,
            bootstrap_pilot_replicates=20,
            bootstrap_mc_failure_probability=0.99,
            bootstrap_seed=13,
        )
        self.assertEqual(summary.gate.status, GateStatus.PASS)
        np.testing.assert_allclose(
            summary.contraction_ratios["back_integral"],
            (0.4, 0.25),
        )
        self.assertIn((5, 35), summary.pairs)

        without_extension = {
            pair: value for pair, value in series.items() if pair != (35, 70)
        }
        unresolved = analyze_generator_residuals(
            without_extension,
            numerical_upper_bounds={
                key: value
                for key, value in bounds.items()
                if key[0] != (35, 70)
            },
            numerics_allocation=0.005,
            bootstrap_replicates=20,
            bootstrap_pilot_replicates=10,
            bootstrap_mc_failure_probability=0.99,
            bootstrap_seed=13,
        )
        self.assertEqual(unresolved.gate.status, GateStatus.UNRESOLVED)
        self.assertIn(
            "GENERATOR_P70_EXTENSION_REQUIRED",
            unresolved.gate.reason_codes,
        )


class AttackAndLedgerTests(unittest.TestCase):
    def test_attack_width_depth_amplitude_scaling_and_coherent_semantics(
        self,
    ) -> None:
        root_factor = np.linspace(0.8, 1.2, 12)
        cells = {
            (width, depth, amplitude): AttackCell(
                0.001
                * amplitude
                * (256.0 / width)
                * (32.0 / depth)
                * root_factor,
                max_constraint_defect=1e-12,
            )
            for width in (256, 512)
            for depth in (32, 64)
            for amplitude in (0.25, 0.5, 1.0)
        }
        independent = analyze_attack_scaling(
            cells,
            attack_kind="independent",
            allocation=0.015,
            constraint_tolerance=1e-10,
            bootstrap_replicates=60,
            bootstrap_pilot_replicates=20,
            bootstrap_mc_failure_probability=0.99,
            bootstrap_seed=17,
        )
        self.assertEqual(independent.gate.status, GateStatus.PASS)
        for slope in independent.width_slopes.values():
            self.assertAlmostEqual(slope, -1.0, places=12)
        for slope in independent.depth_slopes.values():
            self.assertAlmostEqual(slope, -1.0, places=12)
        for slope in independent.amplitude_slopes.values():
            self.assertAlmostEqual(slope, 1.0, places=12)

        coherent = analyze_attack_scaling(
            cells,
            attack_kind="coherent",
            allocation=0.015,
            constraint_tolerance=1e-10,
            bootstrap_replicates=20,
            bootstrap_pilot_replicates=10,
            bootstrap_mc_failure_probability=0.99,
            bootstrap_seed=17,
        )
        self.assertEqual(coherent.gate.status, GateStatus.UNRESOLVED)
        self.assertEqual(
            coherent.gate.reason_codes,
            ("ATTACK_COHERENT_DIAGNOSTIC_ONLY",),
        )

    def test_error_ledger_reports_pass_fail_and_missing_components(
        self,
    ) -> None:
        allocations = {
            "PDE_numerics": 0.005,
            "dense_sampling": 0.005,
            "width_tail_conditional": 0.01,
            "depth_tail_conditional": 0.01,
            "amplified_closure": 0.015,
            "training_time_tail_conditional": 0.005,
        }
        bounds = {key: 0.5 * value for key, value in allocations.items()}
        passed = aggregate_error_ledger(
            bounds,
            allocations=allocations,
            target_total=0.05,
            conditional_validity={
                "width_tail_conditional": True,
                "depth_tail_conditional": True,
                "training_time_tail_conditional": True,
            },
            nuisance_discrepancy_lcb=0.02,
            nuisance_components=("PDE_numerics",),
        )
        self.assertEqual(passed.gate.status, GateStatus.PASS)
        self.assertLess(passed.total_bound, passed.target_total)
        self.assertEqual(
            passed.gate.to_dict()["status"], GateStatus.PASS.value
        )

        failed = aggregate_error_ledger(
            {**bounds, "amplified_closure": 0.02},
            allocations=allocations,
            target_total=0.05,
        )
        self.assertEqual(failed.gate.status, GateStatus.FAIL)
        self.assertIn(
            "LEDGER_ALLOCATION_EXCEEDED", failed.gate.reason_codes
        )

        missing = aggregate_error_ledger(
            {"PDE_numerics": 0.001},
            allocations=allocations,
            target_total=0.05,
        )
        self.assertEqual(missing.gate.status, GateStatus.UNRESOLVED)
        self.assertEqual(
            missing.gate.reason_codes, ("LEDGER_COMPONENT_MISSING",)
        )


if __name__ == "__main__":
    unittest.main()
