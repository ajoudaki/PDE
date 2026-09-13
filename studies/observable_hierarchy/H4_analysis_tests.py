"""Deterministic archive-algebra tests; no solver or initialization is called.

Predeclared allowance: 30 CPU / 60 wall seconds, one numerical thread. This
is part of the edition's 600-CPU-second deterministic-test envelope. Set
TMPDIR to the fresh study-owned test directory before execution.
"""
from fractions import Fraction
import json
from pathlib import Path
import tempfile
import unittest

import numpy as np

from scripts import analyze_observable_horizon as analysis


class ArchiveChecks(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.folder = Path(temporary.name)
        pair = np.array([[[0, .5], [0, -.5]], [[0, .25], [0, -.25]]])
        weights = np.array([.25, .75])
        motion = np.sqrt(7/64)
        self.data = dict(circle=np.array([[1, 0], [0, 1]]), prediction=np.array([.5, -.5]),
                         training_prediction=np.array([.5, -.5]), labels=np.array([1., -1.]), loss=np.array(.25),
                         first_pairs=pair, second_pairs=pair.copy(), first_weights=weights,
                         second_weights=weights.copy(), input_weights=np.array([.5, .5]),
                         inputs=np.array([[1, 0], [0, 1]]), rms1=np.array(motion), rms2=np.array(motion))
        self.item = dict(time="40", npz="observation.npz", exact_json="exact.json", loss=.25, rms1=motion, rms2=motion)
        self.dimensions = dict(first_nodes=2, second_nodes=2, input_nodes=2)
        (self.folder / "exact.json").write_text(json.dumps({"fixture": "presence only; exact encoder checked by producer tests"}))
        self.save()

    def save(self):
        np.savez(self.folder / "observation.npz", **self.data)

    def test_independent_weighted_pair_and_risk_recomputation(self):
        _, result = analysis.read_observation(self.folder, self.item, self.dimensions, 2)
        self.assertEqual(result["recomputed"]["loss"], .25)
        self.assertAlmostEqual(result["recomputed"]["rms1"] ** 2, 7/64)
        self.assertEqual(result["paired_moments"]["first"]["initial_current_product"], 0)

    def test_pair_corruption_and_time_zero_mismatch_fail(self):
        with self.assertRaises(ValueError):
            analysis.read_observation(self.folder, dict(self.item, time="0"), self.dimensions, 2)
        self.data["first_pairs"][0, 0, 1] += .1
        self.save()
        with self.assertRaises(ValueError):
            analysis.read_observation(self.folder, self.item, self.dimensions, 2)

    def test_exact_archive_presence_and_safe_names(self):
        (self.folder / "exact.json").unlink()
        with self.assertRaises(ValueError):
            analysis.read_observation(self.folder, self.item, self.dimensions, 2)
        for value in ("../escape.npz", "", ".", "..", "/tmp/out"):
            with self.assertRaises(ValueError):
                analysis.basename(value)

    def test_numerical_comparison_keeps_scope_and_sign(self):
        config = dict(id="left", law="arc", order=1, steps=800, digits=24, backend="rational")
        right = dict(config, id="right", digits=36)
        data = {key: value.copy() for key, value in self.data.items()}
        data["prediction"] += .125
        result = analysis.comparison(dict(configuration=config), dict(configuration=right),
                                     {"40": self.data}, {"40": data})
        self.assertEqual(result["kind"], "arithmetic")
        self.assertEqual(result["maximum_over_saved_times_and_panel"], .125)
        self.assertIsNone(analysis.comparison(dict(configuration=config),
                          dict(configuration=dict(right, law="different")), {"40": self.data}, {"40": data}))


if __name__ == "__main__":
    unittest.main(verbosity=2)
