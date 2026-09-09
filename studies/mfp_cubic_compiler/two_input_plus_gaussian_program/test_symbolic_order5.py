#!/usr/bin/env python3
"""Fast regression tests for the stored symbolic order-five result."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
AUDIT = HERE / "audit_symbolic_order5.py"


def load_audit_module():
    specification = importlib.util.spec_from_file_location(
        "audit_symbolic_order5_for_tests", AUDIT
    )
    if specification is None or specification.loader is None:
        raise ImportError(f"cannot load {AUDIT}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    return module


audit = load_audit_module()


class SymbolicOrderFiveTests(unittest.TestCase):
    def setUp(self) -> None:
        self.document = audit.load_document()
        self.derivatives = audit.derivative_polynomials(self.document)

    def test_all_static_gates(self) -> None:
        audit.static_audit(self.document)

    def test_parity(self) -> None:
        for order in (0, 2, 4):
            self.assertEqual(self.derivatives[order], (Fraction(0),))

    def test_requested_correlations(self) -> None:
        for rho in (Fraction(0), Fraction(1, 2), Fraction(1)):
            values = [audit.evaluate(polynomial, rho) for polynomial in self.derivatives]
            self.assertEqual(values[0], 0)
            self.assertEqual(values[2], 0)
            self.assertEqual(values[4], 0)

    def test_fifth_derivative_degree(self) -> None:
        self.assertEqual(len(self.derivatives[5]) - 1, 27)
        self.assertNotEqual(self.derivatives[5][-1], 0)


if __name__ == "__main__":
    unittest.main()
