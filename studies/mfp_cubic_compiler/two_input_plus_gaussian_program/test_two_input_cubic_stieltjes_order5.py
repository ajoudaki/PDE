#!/usr/bin/env python3
"""Regression tests for the two-input cubic order-five Stieltjes audit."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
AUDIT_SOURCE = HERE / "two_input_cubic_stieltjes_order5.py"
AUDIT_RESULT = HERE / "stieltjes_order5_audit.json"


def load_audit_module():
    specification = importlib.util.spec_from_file_location(
        "two_input_cubic_stieltjes_order5_for_tests", AUDIT_SOURCE
    )
    if specification is None or specification.loader is None:
        raise ImportError(f"cannot load {AUDIT_SOURCE}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


audit = load_audit_module()


class TwoInputCubicStieltjesOrderFiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.stored = json.loads(AUDIT_RESULT.read_text())

    def test_retained_result_matches_live_exact_audit(self) -> None:
        output = subprocess.check_output(
            [sys.executable, str(AUDIT_SOURCE)], text=True
        )
        self.assertEqual(json.loads(output), self.stored)

    def test_full_domain_sign_certificates(self) -> None:
        for name in ("A", "P", "N"):
            certificate = self.stored["sturm_certificates"][name]
            self.assertEqual(certificate["distinct_roots_on_closed_interval"], 0)
            self.assertTrue(certificate["strictly_positive_on_closed_interval"])

    def test_requested_exact_values(self) -> None:
        expected = {
            "rho_0": (
                Fraction(47_090_556, 114_005),
                Fraction(9_007_737_597_469, 441_577_832_349_375),
            ),
            "rho_1_over_2": (
                Fraction(146_249_888, 319_225),
                Fraction(
                    2_226_187_969_218_708_704,
                    91_794_899_448_972_309_375,
                ),
            ),
            "rho_1": (
                Fraction(93_960_072, 114_005),
                Fraction(5_787_193_487_251, 147_192_610_783_125),
            ),
        }
        for name, values in expected.items():
            record = self.stored["exact_specializations"][name]
            self.assertEqual(Fraction(record["mu_0"]), values[0])
            self.assertEqual(Fraction(record["mu_1"]), values[1])

    def test_hankel_cutoff_is_explicit(self) -> None:
        conditions = self.stored["accessible_hankel_conditions"]
        self.assertIn("positive definite", conditions["H_0=[mu_0]"])
        self.assertIn("positive definite", conditions["H_0_plus=[mu_1]"])
        self.assertIn("requires mu_2", conditions["H_1"])


if __name__ == "__main__":
    unittest.main()
