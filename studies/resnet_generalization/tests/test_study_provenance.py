from __future__ import annotations

import json
from pathlib import Path
import unittest

import numpy as np

from study_cases import load_case


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "protocol" / "cases.json"


class StudyProvenanceTests(unittest.TestCase):
    def test_all_active_cases_keep_fixed_d_and_p_rule(self) -> None:
        protocol = json.loads(
            (ROOT / "protocol" / "generalization_protocol.json").read_text()
        )
        hashes = set()
        sample_counts = set()
        for case_id in protocol["active_case_ids"]:
            case = load_case(REGISTRY, case_id)
            self.assertEqual(case.X.shape[0], 3)
            self.assertEqual(5, case.X.shape[0] + 2)
            self.assertEqual(case.X.shape[1], case.y.size)
            self.assertLess(
                np.max(np.abs(np.linalg.norm(case.X, axis=0) - 1.0)),
                2e-14,
            )
            hashes.add(case.case_sha256)
            sample_counts.add(case.y.size)
        self.assertEqual(len(hashes), len(protocol["active_case_ids"]))
        self.assertEqual(sample_counts, {2, 3, 4, 5})

    def test_exact_registered_geometry_and_label_boundaries(self) -> None:
        baseline = load_case(REGISTRY, "B0")
        local = load_case(REGISTRY, "Y1")
        correlated = load_case(REGISTRY, "X2")
        self.assertAlmostEqual(
            np.linalg.norm(local.y - baseline.y), 0.05, places=14
        )
        gram = correlated.X.T @ correlated.X
        self.assertLess(np.max(np.abs(np.diag(gram) - 1.0)), 2e-14)
        self.assertLess(
            np.max(np.abs(gram[np.triu_indices(3, 1)] - 0.85)),
            2e-14,
        )

    def test_activation_and_data_change_case_hash(self) -> None:
        b0 = load_case(REGISTRY, "B0")
        a1 = load_case(REGISTRY, "A1")
        a2 = load_case(REGISTRY, "A2")
        m5 = load_case(REGISTRY, "M5")
        i2 = load_case(REGISTRY, "I2")
        self.assertNotEqual(b0.case_sha256, a1.case_sha256)
        self.assertNotEqual(b0.case_sha256, a2.case_sha256)
        self.assertNotEqual(a1.case_sha256, a2.case_sha256)
        self.assertNotEqual(m5.case_sha256, i2.case_sha256)
        self.assertEqual(b0.X.tolist(), a1.X.tolist())
        self.assertEqual(b0.y.tolist(), a1.y.tolist())
        self.assertEqual(b0.X.tolist(), a2.X.tolist())
        self.assertEqual(b0.y.tolist(), a2.y.tolist())
        self.assertEqual(m5.X.tolist(), i2.X.tolist())
        self.assertEqual(m5.y.tolist(), i2.y.tolist())

    def test_wrong_or_unknown_case_is_rejected(self) -> None:
        with self.assertRaises(KeyError):
            load_case(REGISTRY, "NOT_A_CASE")


if __name__ == "__main__":
    unittest.main()
