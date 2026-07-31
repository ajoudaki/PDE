from __future__ import annotations

import unittest

import numpy as np

from study_metrics import (
    BootstrapSamples,
    DenseEnsemble,
    MetadataMismatchError,
    TimeGridMismatchError,
    Trajectory,
    align_dense_depth,
    bootstrap_comparison_metrics,
    centered_simultaneous_ucb,
    centered_simultaneous_ucbs,
    comparison_metrics,
    observed_primary_metrics,
    plateau_metrics,
    stitch_pde_segments,
    trajectory_resample_counts,
    validate_pair,
)


def _metadata(m: int) -> dict:
    X = np.arange(1, 3 * m + 1, dtype=float).reshape(3, m)
    X /= np.linalg.norm(X, axis=0, keepdims=True)
    return {
        "case_sha256": f"case-{m}",
        "X": X.tolist(),
        "y": np.linspace(-0.4, 0.7, m).tolist(),
        "activation": "tanh",
        "sigma_w": 0.65,
        "A": 1.0,
        "gamma": 1.0,
    }


def _trajectory(
    m: int,
    *,
    times: np.ndarray | None = None,
    depth: int = 3,
    metadata: dict | None = None,
) -> Trajectory:
    if times is None:
        times = np.arange(5, dtype=float)
    f = np.outer(times, np.linspace(0.1, 0.2, m))
    grams = np.empty((times.size, depth, m, m))
    for t_index, time in enumerate(times):
        for d_index in range(depth):
            grams[t_index, d_index] = (
                (1.0 + 0.1 * time + 0.05 * d_index) * np.eye(m)
            )
    theta = np.broadcast_to(
        np.eye(m), (times.size, m, m)
    ).copy()
    return Trajectory(
        times=times,
        f=f,
        grams=grams,
        theta=theta,
        metadata=_metadata(m) if metadata is None else metadata,
    )


def _ensemble_from_trajectory(
    trajectory: Trajectory,
    *,
    members: int = 3,
    dense_depth: int | None = None,
) -> DenseEnsemble:
    if dense_depth is None or dense_depth == trajectory.grams.shape[1]:
        grams = trajectory.grams
    else:
        source_depths = np.linspace(0.0, 1.0, trajectory.grams.shape[1])
        target_depths = np.linspace(0.0, 1.0, dense_depth)
        grams = np.empty(
            (
                trajectory.times.size,
                dense_depth,
                trajectory.m,
                trajectory.m,
            )
        )
        for t in range(trajectory.times.size):
            for i in range(trajectory.m):
                for j in range(trajectory.m):
                    grams[t, :, i, j] = np.interp(
                        target_depths,
                        source_depths,
                        trajectory.grams[t, :, i, j],
                    )
    return DenseEnsemble(
        times=trajectory.times,
        f=np.repeat(trajectory.f[None, ...], members, axis=0),
        grams=np.repeat(grams[None, ...], members, axis=0),
        theta=np.repeat(trajectory.theta[None, ...], members, axis=0),
        metadata=trajectory.metadata,
    )


class ProvenanceAndStitchTests(unittest.TestCase):
    def test_every_required_metadata_mismatch_is_rejected(self) -> None:
        pde = _trajectory(3)
        dense = _ensemble_from_trajectory(pde)
        for key in (
            "case_sha256",
            "X",
            "y",
            "activation",
            "sigma_w",
            "A",
            "gamma",
        ):
            changed = dict(dense.metadata)
            if key == "case_sha256":
                changed[key] = "different"
            elif key == "X":
                changed[key] = np.asarray(changed[key]).copy()
                changed[key][0, 0] += 1e-15
            elif key == "y":
                changed[key] = np.asarray(changed[key]).copy()
                changed[key][0] += 1e-15
            elif key == "activation":
                changed[key] = "erf"
            else:
                changed[key] = float(changed[key]) + 1e-15
            other = DenseEnsemble(
                dense.times,
                dense.f,
                dense.grams,
                dense.theta,
                changed,
            )
            with self.subTest(key=key):
                with self.assertRaisesRegex(
                    MetadataMismatchError, f"mismatch for {key}"
                ):
                    validate_pair(pde, other)

    def test_time_grid_mismatch_is_rejected_exactly(self) -> None:
        pde = _trajectory(2)
        dense = _ensemble_from_trajectory(pde)
        shifted_times = dense.times.copy()
        shifted_times[2] += 1e-15
        shifted = DenseEnsemble(
            shifted_times,
            dense.f,
            dense.grams,
            dense.theta,
            dense.metadata,
        )
        with self.assertRaises(TimeGridMismatchError):
            validate_pair(pde, shifted)

    def test_stitch_removes_one_exact_restart_boundary(self) -> None:
        full = _trajectory(3)
        first = Trajectory(
            full.times[:3],
            full.f[:3],
            full.grams[:3],
            full.theta[:3],
            full.metadata,
        )
        second = Trajectory(
            full.times[2:],
            full.f[2:],
            full.grams[2:],
            full.theta[2:],
            full.metadata,
        )
        stitched = stitch_pde_segments([first, second])
        np.testing.assert_array_equal(stitched.times, full.times)
        np.testing.assert_array_equal(stitched.f, full.f)
        np.testing.assert_array_equal(stitched.grams, full.grams)
        self.assertEqual(stitched.metadata["stitched_segments"], 2)

        broken_f = second.f.copy()
        broken_f[0, 0] += 1e-12
        broken = Trajectory(
            second.times,
            broken_f,
            second.grams,
            second.theta,
            second.metadata,
        )
        with self.assertRaisesRegex(ValueError, "discontinuous f"):
            stitch_pde_segments([first, broken])

    def test_stitch_canonicalizes_only_roundoff_level_restart_times(self) -> None:
        sample_step = 0.04
        full = _trajectory(
            2, times=np.arange(401, dtype=float) * sample_step
        )
        first = Trajectory(
            full.times[:201],
            full.f[:201],
            full.grams[:201],
            full.theta[:201],
            full.metadata,
        )
        continuation_times = 8.0 + np.arange(201) * sample_step
        second = Trajectory(
            continuation_times,
            full.f[200:],
            full.grams[200:],
            full.theta[200:],
            full.metadata,
        )
        self.assertNotEqual(continuation_times[1], full.times[201])
        stitched = stitch_pde_segments([first, second])
        np.testing.assert_array_equal(stitched.times, full.times)

        wrong_times = continuation_times.copy()
        wrong_times[10] += 1e-6
        wrong = Trajectory(
            wrong_times,
            second.f,
            second.grams,
            second.theta,
            second.metadata,
        )
        with self.assertRaisesRegex(
            TimeGridMismatchError, "common sample step"
        ):
            stitch_pde_segments([first, wrong])


class AlignmentAndComparisonTests(unittest.TestCase):
    def test_depth_alignment_subsamples_then_interpolates(self) -> None:
        values = np.arange(5.0).reshape(1, 5, 1, 1)
        exact = align_dense_depth(values, 3)
        self.assertEqual(exact.method, "exact_subsample")
        self.assertEqual(exact.source_indices, (0, 2, 4))
        np.testing.assert_array_equal(
            exact.values.reshape(-1), np.array([0.0, 2.0, 4.0])
        )

        values = np.arange(4.0).reshape(1, 4, 1, 1)
        interpolated = align_dense_depth(values, 3)
        self.assertEqual(interpolated.method, "linear_interpolation")
        np.testing.assert_allclose(
            interpolated.values.reshape(-1),
            np.array([0.0, 1.5, 3.0]),
            rtol=0.0,
            atol=0.0,
        )

    def test_zero_error_for_all_study_sample_counts(self) -> None:
        for m in range(2, 6):
            pde = _trajectory(m, depth=3)
            dense = _ensemble_from_trajectory(
                pde, members=4, dense_depth=5
            )
            metrics = comparison_metrics(pde, dense)
            with self.subTest(m=m):
                self.assertEqual(
                    metrics["depth_alignment"]["method"],
                    "exact_subsample",
                )
                self.assertEqual(metrics["gram_increment"]["sup_fro"], 0.0)
                self.assertEqual(
                    metrics["gram_increment"]["normalized_sup"], 0.0
                )
                self.assertEqual(metrics["output_increment"]["sup_l2"], 0.0)
                self.assertEqual(
                    metrics["loss_of_ensemble_mean"]["sup_abs"], 0.0
                )
                self.assertEqual(metrics["gram_absolute"]["sup_fro"], 0.0)
                self.assertEqual(metrics["theta_absolute"]["sup_fro"], 0.0)

    def test_known_perturbations_and_max_locations(self) -> None:
        pde = _trajectory(2, depth=3)
        dense = _ensemble_from_trajectory(pde, members=2)
        dense_f = dense.f.copy()
        dense_grams = dense.grams.copy()
        dense_theta = dense.theta.copy()
        dense_f[:, 3, 0] += 0.2
        dense_f[:, 4, 0] += 0.1
        dense_grams[:, 4, 1, 0, 0] += 0.3
        dense_theta[:, 2, 0, 0] += 0.4
        perturbed = DenseEnsemble(
            dense.times,
            dense_f,
            dense_grams,
            dense_theta,
            dense.metadata,
        )
        metrics = comparison_metrics(pde, perturbed)
        self.assertAlmostEqual(
            metrics["output_increment"]["sup_l2"], 0.2
        )
        self.assertEqual(
            metrics["output_increment"]["max_time_index"], 3
        )
        self.assertAlmostEqual(
            metrics["gram_increment"]["sup_fro"], 0.3
        )
        self.assertEqual(metrics["gram_increment"]["max_time_index"], 4)
        self.assertEqual(metrics["gram_increment"]["max_depth_index"], 1)
        self.assertAlmostEqual(metrics["gram_absolute"]["sup_fro"], 0.3)
        self.assertAlmostEqual(metrics["theta_absolute"]["sup_fro"], 0.4)
        self.assertEqual(metrics["theta_absolute"]["max_time_index"], 2)
        self.assertGreater(
            metrics["loss_of_ensemble_mean"]["sup_abs"], 0.0
        )


class PlateauTests(unittest.TestCase):
    def test_pde_plateau_uses_exact_final_half_and_analytic_speed(self) -> None:
        m = 2
        times = np.arange(5, dtype=float)
        metadata = _metadata(m)
        metadata["y"] = [0.0, 0.0]
        f = np.array(
            [[0.0, 0.0], [1.0, 0.0], [2.0, 0.0],
             [2.5, 0.0], [3.0, 0.0]]
        )
        grams = np.zeros((5, 3, m, m))
        grams[:, :, 0, 0] = np.array([0.0, 0.5, 1.0, 1.25, 1.5])[:, None]
        theta = np.broadcast_to(np.eye(m), (5, m, m)).copy()
        pde = Trajectory(times, f, grams, theta, metadata)
        metrics = plateau_metrics(pde)
        self.assertEqual(metrics["tail_start_index"], 2)
        self.assertEqual(metrics["tail_start_time"], 2.0)
        self.assertAlmostEqual(metrics["output_endpoint_drift_l2"], 1.0)
        self.assertAlmostEqual(metrics["output_discrete_arclength_l2"], 1.0)
        self.assertAlmostEqual(
            metrics["gram_endpoint_drift_sup_fro"], 0.5
        )
        self.assertAlmostEqual(
            metrics["gram_discrete_arclength_sum_step_sup_fro"], 0.5
        )
        self.assertAlmostEqual(metrics["analytic_output_speed_sup_l2"], 3.0)
        self.assertAlmostEqual(metrics["loss_endpoint_drift_abs"], 2.5)

    def test_dense_speed_is_mean_of_memberwise_products_and_has_p95(self) -> None:
        m = 2
        times = np.array([0.0, 1.0, 2.0])
        metadata = _metadata(m)
        metadata["y"] = [0.0, 0.0]
        f = np.zeros((2, 3, m))
        f[0, :, 0] = 1.0
        f[1, :, 0] = 3.0
        theta = np.zeros((2, 3, m, m))
        theta[0, :, 0, 0] = 2.0
        grams = np.zeros((2, 3, 2, m, m))
        dense = DenseEnsemble(times, f, grams, theta, metadata)
        metrics = plateau_metrics(dense)
        # mean_s[-Theta_s e_s] = (-2 + 0)/2 = -1, whereas
        # -mean(Theta_s) mean(e_s) would incorrectly have norm 2.
        self.assertAlmostEqual(metrics["analytic_output_speed_sup_l2"], 1.0)
        self.assertEqual(
            metrics["member_output_endpoint_drift_p95_l2"], 0.0
        )
        self.assertEqual(
            metrics["member_gram_endpoint_drift_p95_sup_fro"], 0.0
        )

    def test_missing_exact_midpoint_is_rejected(self) -> None:
        pde = _trajectory(2, times=np.array([0.0, 1.0, 3.0, 4.0]))
        with self.assertRaises(TimeGridMismatchError):
            plateau_metrics(pde)


class BootstrapTests(unittest.TestCase):
    def test_trajectory_bootstrap_is_deterministic_and_m_generic(self) -> None:
        for m in range(2, 6):
            pde = _trajectory(m)
            dense = _ensemble_from_trajectory(pde, members=4)
            f = dense.f.copy()
            grams = dense.grams.copy()
            theta = dense.theta.copy()
            for member in range(dense.members):
                f[member, :, 0] += 0.01 * member * pde.times
                grams[member, :, :, 0, 0] += (
                    0.005 * member * pde.times[:, None]
                )
                theta[member, :, 0, 0] += 0.02 * member
            varied = DenseEnsemble(
                dense.times, f, grams, theta, dense.metadata
            )
            first = bootstrap_comparison_metrics(
                pde,
                varied,
                replicates=31,
                seed=9876,
                batch_size=7,
            )
            second = bootstrap_comparison_metrics(
                pde,
                varied,
                replicates=31,
                seed=9876,
                batch_size=5,
            )
            with self.subTest(m=m):
                self.assertEqual(first.replicates, 31)
                for name in first.metrics:
                    np.testing.assert_array_equal(
                        first.metrics[name], second.metrics[name]
                    )
                    self.assertEqual(first.metrics[name].shape, (31,))

    def test_explicit_counts_support_paired_case_resampling(self) -> None:
        pde = _trajectory(3)
        dense = _ensemble_from_trajectory(pde, members=4)
        counts = trajectory_resample_counts(
            dense.members, replicates=19, seed=123
        )
        np.testing.assert_array_equal(
            np.sum(counts, axis=1), np.full(19, dense.members)
        )
        first = bootstrap_comparison_metrics(
            pde,
            dense,
            replicates=19,
            seed=1,
            resample_counts=counts,
        )
        second = bootstrap_comparison_metrics(
            pde,
            dense,
            replicates=19,
            seed=999,
            resample_counts=counts,
        )
        for name in first.metrics:
            np.testing.assert_array_equal(
                first.metrics[name], second.metrics[name]
            )
        with self.assertRaisesRegex(ValueError, "sum"):
            bootstrap_comparison_metrics(
                pde,
                dense,
                replicates=19,
                resample_counts=np.zeros_like(counts),
            )

    def test_centered_simultaneous_ucb_known_example(self) -> None:
        observed = {"a": 1.0, "b": 2.0}
        samples = {
            "a": np.array([1.0, 2.0, 0.0]),
            "b": np.array([2.0, 2.5, 3.0]),
        }
        result = centered_simultaneous_ucb(
            observed, samples, confidence=0.8
        )
        np.testing.assert_array_equal(
            result.centered_max_samples, np.array([0.0, 1.0, 1.0])
        )
        self.assertEqual(result.critical_value, 1.0)
        self.assertEqual(result.upper_bounds, {"a": 2.0, "b": 3.0})

    def test_multi_metric_wrapper_and_key_mismatch(self) -> None:
        pde = _trajectory(2)
        dense = _ensemble_from_trajectory(pde, members=3)
        comparison = comparison_metrics(pde, dense)
        observed = observed_primary_metrics(comparison)
        sample = bootstrap_comparison_metrics(
            pde, dense, replicates=7, seed=22
        )
        results = centered_simultaneous_ucbs(
            {"c1": observed, "c2": observed},
            {"c1": sample, "c2": sample},
        )
        self.assertEqual(set(results), set(observed))
        self.assertTrue(
            all(result.replicates == 7 for result in results.values())
        )
        with self.assertRaisesRegex(ValueError, "case keys"):
            centered_simultaneous_ucb(
                {"c1": 0.0},
                {"c2": np.zeros(3)},
            )
        broken = BootstrapSamples(
            seed=1,
            replicates=7,
            metrics={**sample.metrics, "extra": np.zeros(7)},
        )
        with self.assertRaisesRegex(ValueError, "same metrics"):
            centered_simultaneous_ucbs(
                {"c1": observed},
                {"c1": broken},
            )


if __name__ == "__main__":
    unittest.main()
