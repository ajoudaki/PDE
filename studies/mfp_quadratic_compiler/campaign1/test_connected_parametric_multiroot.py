#!/usr/bin/env python3
"""Build and exact-regression tests for the Campaign 1 C++ compiler."""

from __future__ import annotations

import json
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


HERE = Path(__file__).resolve().parent
COMPILER = HERE.parent
SOURCE = HERE / "connected_parametric_multiroot.cpp"
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import parametric_multiroot_reference as reference


class ProductionCompilerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temporary = tempfile.TemporaryDirectory(prefix="campaign1-cxx-")
        cls.binary = Path(cls.temporary.name) / "connected_parametric_multiroot"
        cls.output = Path(cls.temporary.name) / "smoke.json"
        subprocess.run(
            [
                "g++", "-std=c++17", "-O2", "-DNDEBUG",
                str(SOURCE), "-o", str(cls.binary),
            ],
            cwd=COMPILER,
            check=True,
            timeout=60,
        )
        subprocess.run(
            [
                str(cls.binary),
                "--max-f", "5",
                "--max-q2", "4",
                "--max-q1", "4",
                "--output", str(cls.output),
            ],
            cwd=COMPILER,
            check=True,
            timeout=60,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        cls.production = json.loads(cls.output.read_text(encoding="utf-8"))
        cls.transparent = reference.run(5, verify_parent_rewrites=True)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temporary.cleanup()

    def test_every_production_polynomial_matches_transparent_reference(self) -> None:
        limits = {"f": 5, "q1": 4, "q2": 4}
        for root, max_order in limits.items():
            actual = self.production["observables"][root]["jets"]
            expected = self.transparent["jets"][root]
            for order in range(max_order + 1):
                self.assertEqual(
                    [int(value) for value in actual[order]["lambda_coefficients"]],
                    expected[order],
                    (root, order),
                )

    def test_internal_regression_gate_passed(self) -> None:
        self.assertTrue(self.production["regression_gates_passed"])
        self.assertEqual(
            self.production["parent_source_sha256"],
            hashlib.sha256(
                (COMPILER / "sector_engine_checked.cpp").read_bytes()
            ).hexdigest(),
        )

    def test_order_cap_is_enforced(self) -> None:
        result = subprocess.run(
            [str(self.binary), "--max-f", "10"],
            cwd=COMPILER,
            timeout=10,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("safety cap", result.stderr)


if __name__ == "__main__":
    unittest.main()
