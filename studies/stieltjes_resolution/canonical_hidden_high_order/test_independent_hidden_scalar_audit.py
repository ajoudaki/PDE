"""Tests for the algebraically independent hidden scalar audit."""

from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "independent_hidden_scalar_audit.py"
SPEC = importlib.util.spec_from_file_location(
    "independent_hidden_scalar_audit_under_test", SOURCE
)
assert SPEC is not None and SPEC.loader is not None
AUDIT = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = AUDIT
SPEC.loader.exec_module(AUDIT)

Rat = Fraction


class IndependentHiddenScalarAuditTests(unittest.TestCase):
    def test_x_reversion_and_square_root_primitives(self) -> None:
        forward = [Rat(0), Rat(4), Rat(0), Rat(9)]
        inverse = AUDIT.reverse(forward, 3)
        self.assertEqual(
            AUDIT.compose(forward, inverse, 3),
            [Rat(0), Rat(1), Rat(0), Rat(0)],
        )
        self.assertEqual(
            AUDIT.normalized_square_root([Rat(1), Rat(2), Rat(1)]),
            [Rat(1), Rat(1), Rat(0)],
        )

    def test_hankel_audit_distinguishes_pd_from_singular_psd(self) -> None:
        singular = AUDIT.audit_hankels([Rat(1), Rat(1), Rat(1)])
        ordinary_h1 = singular["ordinary"]["H1"]
        self.assertTrue(ordinary_h1["positive_semidefinite"])
        self.assertFalse(ordinary_h1["positive_definite"])
        self.assertEqual(ordinary_h1["determinant"], "0")

        indefinite = AUDIT.audit_hankels([Rat(1), Rat(2), Rat(1)])
        self.assertFalse(indefinite["ordinary"]["H1"]["positive_semidefinite"])

    def test_full_hidden_scalar_audit_when_recurrence_results_exist(self) -> None:
        production = HERE / "PRODUCTION_HIDDEN_RESULT.json"
        independent = HERE / "INDEPENDENT_HIDDEN_RESULT.json"
        if not production.exists() or not independent.exists():
            self.skipTest("full hidden recurrence results are still running")

        result = AUDIT.audit_documents(production, independent)
        self.assertTrue(all(result["gates"].values()))

        families = result["families"]
        q1 = families["q1_squared_rms"]
        q2 = families["q2_squared_rms"]
        self.assertEqual(q1["moment_count"], 9)
        self.assertEqual(q2["moment_count"], 8)
        self.assertEqual(
            q1["moments"][:4],
            [
                "4/111",
                "561728/50602347",
                "1100387825680/207616015289871",
                "477889187282572736/157745610337167536445",
            ],
        )
        self.assertEqual(
            q2["moments"][:4],
            [
                "2062/4107",
                "678331568/5616860517",
                "2090752728035608/38408962828626135",
                "137586915791251406192/4539568119702932437695",
            ],
        )

        for name, family in families.items():
            self.assertTrue(family["all_moments_strictly_positive"], name)
            self.assertTrue(
                family["hankels"][
                    "all_accessible_matrices_positive_definite"
                ],
                name,
            )
            expected_matrices = 9 if name.startswith("q1_") else 8
            expected_minors = 83 if name.startswith("q1_") else 52
            self.assertEqual(
                family["hankels"]["accessible_matrix_count"],
                expected_matrices,
            )
            self.assertEqual(
                family["hankels"]["accessible_principal_minor_count"],
                expected_minors,
            )

    def test_retained_audit_matches_fresh_reconstruction_when_present(self) -> None:
        production = HERE / "PRODUCTION_HIDDEN_RESULT.json"
        independent = HERE / "INDEPENDENT_HIDDEN_RESULT.json"
        retained = HERE / "INDEPENDENT_HIDDEN_SCALAR_AUDIT.json"
        if not production.exists() or not independent.exists() or not retained.exists():
            self.skipTest("retained independent scalar audit is not yet complete")
        fresh = AUDIT.audit_documents(production, independent)
        self.assertEqual(json.loads(retained.read_text()), fresh)


if __name__ == "__main__":
    unittest.main()
