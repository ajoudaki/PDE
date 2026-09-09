#!/usr/bin/env python3
"""Durable exact-arithmetic and provenance checks for Campaign 6."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import coarse_sector_bounds as bounds


HERE = Path(__file__).resolve().parent


class Campaign6Tests(unittest.TestCase):
    def test_frozen_protocol_hash(self) -> None:
        expected = "1cdc9f40f8180e744275806f667a66e5c4194afe2884c4a57262c2fb7ec7ed43"
        actual = hashlib.sha256((HERE / "PROTOCOL.md").read_bytes()).hexdigest()
        self.assertEqual(actual, expected)

    def test_accepted_static_sector_tables(self) -> None:
        self.assertEqual(sum(bounds.EXACT_SECTORS[9]), bounds.EXACT_TOTALS[9])
        self.assertEqual(sum(bounds.EXACT_SECTORS[11]), bounds.EXACT_TOTALS[11])
        self.assertEqual(
            bounds.EXACT_SECTORS[11][-3:],
            [
                83655641930747138444722176,
                49117046434067436406308864,
                12285503181066227920404480,
            ],
        )

    def test_coarse_envelopes_cover_every_known_sector(self) -> None:
        for order in (9, 11):
            upper, _ = bounds.sector_envelope(order)
            self.assertTrue(
                all(exact <= cap for exact, cap in zip(bounds.EXACT_SECTORS[order], upper))
            )

    def test_wick_pair_sector_nomenclature(self) -> None:
        artifact = json.loads((HERE / "coarse_sector_bounds.json").read_text())
        for order in (9, 11, 13):
            row = artifact["orders"][str(order)]
            self.assertIn("upper_by_wick_pair_sector_P", row)
            self.assertNotIn("upper_by_component_sector", row)
            if order in (9, 11):
                self.assertTrue(row["static_reference_calibration_passed"])
                self.assertNotIn("regression_passed", row)
            for state in row["states"]:
                self.assertEqual(
                    state["wick_pair_sector_P"] + state["component_count_c"],
                    order + 2,
                )
                self.assertNotIn("components", state)

    def test_protocol_downgrade_is_explicit(self) -> None:
        artifact = json.loads((HERE / "coarse_sector_bounds.json").read_text())
        acceptance = artifact["protocol_acceptance"]
        self.assertFalse(acceptance["campaign6_certificate_accepted"])
        self.assertFalse(acceptance["independent_D9_sector_reproduction_completed"])
        self.assertFalse(acceptance["independent_D11_total_reproduction_completed"])
        self.assertFalse(acceptance["durable_per_run_provenance_completed"])
        self.assertIn("not protocol-accepted", artifact["claim_level"])

        report = (HERE / "CAMPAIGN_REPORT.md").read_text()
        self.assertIn("failed its frozen mandatory validity gate", report)
        self.assertIn("not protocol-accepted certificates", report)

    def test_decision_artifact_is_inconclusive(self) -> None:
        artifact = json.loads((HERE / "coarse_sector_bounds.json").read_text())
        decision = artifact["d13_decision"]
        threshold = bounds.THRESHOLD
        self.assertLess(Fraction(decision["known_certified_lower"], 1), threshold)
        self.assertGreater(Fraction(decision["candidate_coarse_upper"], 1), threshold)
        self.assertFalse(decision["lower_crosses_threshold"])
        self.assertFalse(decision["candidate_upper_is_below_threshold"])
        self.assertFalse(decision["campaign6_interval_certificate_accepted"])

    def test_factor_nine_target_is_explicitly_uncertified(self) -> None:
        artifact = json.loads((HERE / "coarse_sector_bounds.json").read_text())
        target = artifact["unsupported_sharpness_target"]
        self.assertFalse(target["certified"])
        self.assertEqual(
            target["S11_weighted_two_hit"],
            bounds.TWO_HIT_WEIGHTED_AGGREGATE_ORDER11,
        )
        self.assertNotEqual(target["S11_weighted_two_hit"], bounds.EXACT_TOTALS[11])

    def test_benchmarks_do_not_authorize_d13(self) -> None:
        artifact = json.loads((HERE / "benchmark_results.json").read_text())
        interpretation = artifact["interpretation"]
        self.assertFalse(interpretation["protocol_gates_completed"])
        self.assertFalse(interpretation["campaign6_certificate_accepted"])
        self.assertFalse(interpretation["D13_production_authorized"])
        self.assertEqual(len(interpretation["missing_gate_evidence"]), 3)
        exact_d9 = [
            b for b in artifact["benchmarks"]
            if b["order"] == 9 and b["mode"] == "exact"
        ]
        self.assertEqual(len(exact_d9), 1)
        self.assertTrue(exact_d9[0]["regression_passed"])


if __name__ == "__main__":
    unittest.main()
