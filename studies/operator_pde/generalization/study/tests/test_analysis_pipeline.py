from __future__ import annotations

import copy
from pathlib import Path
import sys
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from analyze_generalization import (  # noqa: E402
    AnalysisIntegrityError,
    CombinedDense,
    DenseBlock,
    combine_dense_blocks,
    gram_only_centered_ucb,
    joint_centered_bounds,
    normalized_plateau_window,
    select_final_tier,
    stratified_paired_counts,
)
from study_metrics import DenseEnsemble, Trajectory  # noqa: E402


def metadata(m: int, **overrides) -> dict:
    value = {
        "case_id": "C",
        "case_sha256": "case",
        "registry_sha256": "registry",
        "case_family": "test",
        "case_scope": "test",
        "case_description": "synthetic",
        "X": np.eye(3, m).tolist(),
        "y": np.zeros(m).tolist(),
        "m": m,
        "d": 3,
        "activation": "tanh",
        "sigma_w": 0.65,
        "A": 1.0,
        "gamma": 1.0,
        "n": 8,
        "depth": 2,
        "duration": 32.0,
        "dt": 0.02,
        "sample_dt": 4.0,
        "pde_seal_sha256": "seal",
        "dynamics_sha256": "dynamics",
    }
    value.update(overrides)
    return value


def ensemble(seed_start: int, members: int = 2, *, tweak: float = 0.0) -> DenseBlock:
    times = np.arange(0.0, 32.0 + 4.0, 4.0)
    m = 2
    f = np.zeros((members, times.size, m))
    f[:, :, 0] = tweak * times
    grams = np.zeros((members, times.size, 3, m, m))
    grams[:, :, :, 0, 0] = 1.0 + tweak * times[:, None]
    theta = np.zeros((members, times.size, m, m))
    meta = metadata(
        m,
        seed_start=seed_start,
        seeds=members,
        seed_ids=list(range(seed_start, seed_start + members)),
    )
    dense = DenseEnsemble(times, f, grams, theta, meta)
    return DenseBlock(
        Path(f"block-{seed_start}.npz"),
        dense,
        np.arange(seed_start, seed_start + members),
        meta,
    )


def expected_meta() -> dict:
    value = metadata(2)
    for key in ("seed_start", "seeds", "seed_ids"):
        value.pop(key, None)
    return value


class BlockCombinationTests(unittest.TestCase):
    def test_combines_in_frozen_order_and_rejects_duplicate_seeds(self) -> None:
        first = ensemble(100, tweak=0.1)
        second = ensemble(200, tweak=0.2)
        combined = combine_dense_blocks(
            [second, first],
            expected_seed_blocks=[[100, 2], [200, 2]],
            expected_metadata=expected_meta(),
        )
        self.assertIsInstance(combined, CombinedDense)
        np.testing.assert_array_equal(combined.seeds, [100, 101, 200, 201])
        self.assertEqual(combined.ensemble.members, 4)
        np.testing.assert_array_equal(combined.ensemble.f[:2], first.ensemble.f)

        duplicate = ensemble(101)
        duplicate_meta = dict(duplicate.metadata)
        duplicate_meta.update(
            seed_start=200, seeds=2, seed_ids=[200, 201]
        )
        duplicate = DenseBlock(
            duplicate.path,
            duplicate.ensemble,
            np.array([101, 102]),
            duplicate_meta,
        )
        with self.assertRaises(AnalysisIntegrityError):
            combine_dense_blocks(
                [first, duplicate],
                expected_seed_blocks=[[100, 2], [200, 2]],
                expected_metadata=expected_meta(),
            )

    def test_mismatched_config_seal_time_and_seed_are_rejected(self) -> None:
        first, second = ensemble(100), ensemble(200)
        for kind in ("seal", "time", "seed"):
            changed = second
            if kind == "seal":
                meta = dict(second.metadata)
                meta["pde_seal_sha256"] = "wrong"
                changed = DenseBlock(second.path, second.ensemble, second.seeds, meta)
            elif kind == "time":
                times = second.ensemble.times.copy()
                times[1] += 0.25
                dense = DenseEnsemble(
                    times,
                    second.ensemble.f,
                    second.ensemble.grams,
                    second.ensemble.theta,
                    second.metadata,
                )
                changed = DenseBlock(second.path, dense, second.seeds, second.metadata)
            else:
                changed = DenseBlock(
                    second.path, second.ensemble, np.array([200, 202]), second.metadata
                )
            with self.subTest(kind=kind):
                with self.assertRaises(AnalysisIntegrityError):
                    combine_dense_blocks(
                        [first, changed],
                        expected_seed_blocks=[[100, 2], [200, 2]],
                        expected_metadata=expected_meta(),
                    )


class TierAndBootstrapTests(unittest.TestCase):
    def test_frozen_tier_selection(self) -> None:
        plan = {
            "final_reference_selection": {
                "heldout_cases": ["Y1", "I2"],
            }
        }
        self.assertEqual(select_final_tier("Y1", plan), "confirmation")
        self.assertEqual(select_final_tier("B0", plan), "screening")

    def test_stratified_counts_are_deterministic_and_common_sized(self) -> None:
        protocol = {
            "screening_reference": {"seed_blocks": [[1, 3], [10, 3]]},
            "heldout_confirmation": {"seed_blocks": [[20, 2], [30, 2]]},
        }
        first = stratified_paired_counts(protocol, replicates=11, seed=7)
        second = stratified_paired_counts(protocol, replicates=11, seed=7)
        np.testing.assert_array_equal(first["screening"], second["screening"])
        np.testing.assert_array_equal(first["confirmation"], second["confirmation"])
        np.testing.assert_array_equal(first["screening"].sum(axis=1), 6)
        np.testing.assert_array_equal(first["confirmation"].sum(axis=1), 4)

    def test_joint_bounds_use_one_case_metric_max_and_higher_quantile(self) -> None:
        observed = {
            "a": {"gram_error": 1.0, "output_error": 2.0, "loss_error": 3.0},
            "b": {"gram_error": 4.0, "output_error": 5.0, "loss_error": 6.0},
        }
        bootstrap = {
            case: {
                metric: np.array([value, value + 1.0, value - 2.0])
                for metric, value in metrics.items()
            }
            for case, metrics in observed.items()
        }
        result = joint_centered_bounds(observed, bootstrap, confidence=0.8)
        self.assertEqual(result["upper_critical_value"], 1.0)
        self.assertEqual(result["lower_critical_value"], 2.0)
        self.assertEqual(result["bounds"]["b"]["loss_error"]["ucb"], 7.0)
        self.assertEqual(result["bounds"]["a"]["gram_error"]["lcb"], -1.0)
        self.assertEqual(result["quantile_method"], "higher")

    def test_centered_critical_values_are_not_posthoc_clipped(self) -> None:
        observed = {
            "a": {"gram_error": 2.0, "output_error": 2.0, "loss_error": 2.0}
        }
        bootstrap = {
            "a": {
                metric: np.array([1.0, 1.0, 1.0])
                for metric in observed["a"]
            }
        }
        result = joint_centered_bounds(observed, bootstrap, confidence=0.95)
        self.assertEqual(result["upper_critical_value"], -1.0)
        self.assertEqual(result["bounds"]["a"]["gram_error"]["ucb"], 1.0)
        gram = gram_only_centered_ucb(
            observed, bootstrap, confidence=0.95
        )
        self.assertEqual(gram["critical_value"], -1.0)
        self.assertEqual(gram["upper_bounds"]["a"], 1.0)


class PlateauTests(unittest.TestCase):
    def test_exact_window_and_normalization(self) -> None:
        times = np.arange(0.0, 32.0 + 4.0, 4.0)
        m = 2
        f = np.zeros((times.size, m))
        f[times == 16.0, 0] = 0.2
        grams = np.zeros((times.size, 3, m, m))
        grams[:, :, 0, 0] = 1.0
        grams[times == 16.0, :, 0, 0] = 1.4
        theta = np.zeros((times.size, m, m))
        traj = Trajectory(times, f, grams, theta, metadata(m))
        thresholds = {
            "endpoint_output_or_gram_drift": 1.0,
            "output_or_gram_tail_arclength": 2.0,
            "analytic_output_speed": 1.0,
            "loss_drift": 1.0,
            "memberwise_p95": 1.0,
        }
        result = normalized_plateau_window(
            traj,
            start=8.0,
            end=16.0,
            output_scale=2.0,
            gram_scale=4.0,
            thresholds=thresholds,
        )
        self.assertAlmostEqual(result["values"]["endpoint_output_drift"], 0.1)
        self.assertAlmostEqual(result["values"]["endpoint_gram_drift"], 0.1)
        self.assertAlmostEqual(result["values"]["output_tail_arclength"], 0.1)
        self.assertAlmostEqual(result["values"]["gram_tail_arclength"], 0.1)
        with self.assertRaises(AnalysisIntegrityError):
            normalized_plateau_window(
                traj,
                start=7.0,
                end=16.0,
                output_scale=2.0,
                gram_scale=4.0,
                thresholds=thresholds,
            )


if __name__ == "__main__":
    unittest.main()
