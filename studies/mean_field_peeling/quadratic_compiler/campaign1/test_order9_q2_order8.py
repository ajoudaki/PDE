#!/usr/bin/env python3
"""Exact acceptance tests for the Campaign 1 order-9/order-8 result."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import unittest

import sympy as sp


HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import parametric_stieltjes_postprocess as postprocess


RAW = HERE / "results_order9_q2_order8.json"
COMPACT = HERE / "hankel_certificates_order9_q2_order8.json"
PROVENANCE = HERE / "order9_q2_order8_provenance.json"
SOURCE = HERE / "connected_parametric_multiroot.cpp"
PARENT = HERE.parent / "component_recursion.cpp"
POSTPROCESSOR = HERE / "parametric_stieltjes_postprocess.py"
GRADED_SOURCE = HERE / "graded_sector.cpp"
GRADED_RUNNER = HERE / "run_graded_campaign.py"
GRADED_PARENT = HERE.parent / "sector_engine_checked.cpp"
GRADED_TEST = HERE / "test_graded_sector.py"


def parse(text: str, parameter: sp.Symbol) -> sp.Expr:
    return sp.cancel(sp.sympify(
        text.replace("^", "**").replace("lambda", "metric_parameter"),
        locals={"metric_parameter": parameter},
    ))


class UpperCampaignAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.raw = json.loads(RAW.read_text(encoding="utf-8"))
        cls.compact = json.loads(COMPACT.read_text(encoding="utf-8"))
        cls.provenance = json.loads(PROVENANCE.read_text(encoding="utf-8"))
        cls.generated = postprocess.compute(cls.raw)
        cls.parameter = sp.Symbol("metric_parameter", real=True, nonnegative=True)

    def test_frozen_provenance_hashes(self) -> None:
        primary = self.provenance["primary_dense_run"]
        self.assertEqual(hashlib.sha256(RAW.read_bytes()).hexdigest(),
                         primary["result_sha256"])
        self.assertEqual(primary["result_sha256"],
                         self.compact["raw_result_sha256"])
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                         primary["production_source_sha256"])
        self.assertEqual(hashlib.sha256(PARENT.read_bytes()).hexdigest(),
                         primary["parent_source_sha256"])
        self.assertEqual(self.raw["parent_source_sha256"],
                         primary["parent_source_sha256"])
        self.assertTrue(self.raw["regression_gates_passed"])

        post = self.provenance["postprocessing"]
        self.assertEqual(hashlib.sha256(POSTPROCESSOR.read_bytes()).hexdigest(),
                         post["source_sha256"])
        self.assertEqual(hashlib.sha256(COMPACT.read_bytes()).hexdigest(),
                         post["compact_certificate_sha256"])

        graded = self.provenance["independent_double_graded_route"]
        self.assertEqual(hashlib.sha256(GRADED_SOURCE.read_bytes()).hexdigest(),
                         graded["source_sha256"])
        self.assertEqual(hashlib.sha256(GRADED_RUNNER.read_bytes()).hexdigest(),
                         graded["runner_sha256"])
        self.assertEqual(hashlib.sha256(GRADED_PARENT.read_bytes()).hexdigest(),
                         graded["parent_source_sha256"])
        lower_gate = self.provenance["graded_lower_stage_regression"]
        self.assertEqual(hashlib.sha256(GRADED_TEST.read_bytes()).hexdigest(),
                         lower_gate["test_source_sha256"])

    def test_highest_exact_jets(self) -> None:
        f9 = self.raw["observables"]["f"]["jets"][9]
        q2_8 = self.raw["observables"]["q2"]["jets"][8]
        self.assertEqual(f9["lambda_one"], "1181161141825400561664")
        self.assertEqual(q2_8["lambda_one"], "2441783779120539648")
        self.assertEqual(
            [int(value) for value in f9["lambda_coefficients"]],
            [0, 0, 0, 0, 2478851054278778880,
             32885131309935058944, 165198603388928974848,
             388905477453868400640, 423643509104850763776,
             168049569513538584576],
        )
        self.assertEqual(
            [int(value) for value in q2_8["lambda_coefficients"]],
            [0, 0, 0, 0, 14150574369616896, 157936407142173696,
             627373095171618816, 1040967770404737024,
             601355932032393216],
        )

    def test_forced_moment_scaling_is_r_plus_one(self) -> None:
        for observable in ("output_kernel", "second_hidden_norm"):
            scaling = self.generated[observable]["forced_scaling"]
            self.assertTrue(scaling["exact_expected_valuation"])
            self.assertEqual(scaling["valuations_at_zero"], [1, 2, 3, 4])
        self.assertEqual(
            self.compact["moment_scaling"],
            "m_r(lambda) = lambda^(r+1) * mbar_r(lambda)",
        )

    def test_both_shifted_2x2_certificates_match_and_are_strict(self) -> None:
        cases = (
            ("output_kernel", "output_shifted_2x2"),
            ("second_hidden_norm", "hidden_shifted_2x2"),
        )
        for generated_name, compact_name in cases:
            with self.subTest(observable=generated_name):
                expression = self.generated[generated_name][
                    "raw_hankel_determinants"
                ]["shifted"][1]
                expected = parse(
                    self.compact[compact_name]["raw_expression"],
                    self.parameter,
                )
                actual = parse(expression, self.parameter)
                self.assertEqual(sp.cancel(actual - expected), 0)
                certificate = self.generated[generated_name][
                    "normalized_sign_certificates"
                ]["shifted"][1]
                self.assertEqual(certificate["status"], "strictly_positive")
                coefficients = [
                    int(value) for value in
                    self.compact[compact_name][
                        "normalized_numerator_coefficients_descending"
                    ]
                ]
                self.assertTrue(all(value > 0 for value in coefficients))

    def test_secondary_q2_route_is_not_overclaimed(self) -> None:
        graded = self.provenance["independent_double_graded_route"]
        self.assertLess(graded["q2_order8_sectors_completed"],
                        graded["q2_order8_sectors_total"])
        self.assertIn("validates no", graded["acceptance_limit"])


if __name__ == "__main__":
    unittest.main()
