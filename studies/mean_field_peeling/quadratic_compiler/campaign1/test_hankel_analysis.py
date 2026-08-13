#!/usr/bin/env python3
"""Independent exact audits of the Campaign 1 series/Hankel transform."""

from __future__ import annotations

import hashlib
import json
from math import factorial
from pathlib import Path
import sys
import unittest

import sympy as sp


HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import analyze_hankel as analysis


RAW_PATH = HERE / "results_order7_q2_order6.json"
CERTIFICATE_PATH = HERE / "hankel_certificates_order7_q2_order6.json"


def parse_certificate_expression(text: str) -> sp.Expr:
    return sp.cancel(sp.sympify(
        text.replace("^", "**").replace("lambda", "metric_parameter"),
        locals={"metric_parameter": analysis.lam},
    ))


class HankelAnalysisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.raw = json.loads(RAW_PATH.read_text(encoding="utf-8"))
        cls.certificate = json.loads(CERTIFICATE_PATH.read_text(encoding="utf-8"))
        cls.generated = analysis.analyze(cls.raw)
        cls.generated_by_name = {
            record["name"]: record for record in cls.generated["certificates"]
        }

    def test_raw_hash_and_source_hashes(self) -> None:
        self.assertEqual(
            hashlib.sha256(RAW_PATH.read_bytes()).hexdigest(),
            self.certificate["raw_result_sha256"],
        )
        # This is a historical lower-stage artifact.  Its exact wrapper source
        # hash is retained in the certificate, but the live wrapper has since
        # gained the authorized order-9/order-8 branch.  Do not relabel the old
        # result with the live source hash.  The fresh upper-stage rerun and its
        # full provenance are checked in test_order9_q2_order8.py.
        self.assertEqual(
            self.certificate["production_source_sha256"],
            "40bd92576fe917b54044f049b2c9f809a9f8cdb833f10a55d8e57f286ccdde55",
        )
        self.assertEqual(
            self.raw["parent_source_sha256"],
            self.certificate["parent_source_sha256"],
        )
        self.assertEqual(
            hashlib.sha256((HERE.parent / "component_recursion.cpp").read_bytes()).hexdigest(),
            self.raw["parent_source_sha256"],
        )

    def test_every_claimed_sign_has_a_coefficientwise_certificate(self) -> None:
        self.assertTrue(self.generated["all_listed_nonnegative_on_lambda_ge_0"])
        self.assertEqual(self.generated["falsified_quantities"], [])
        self.assertEqual(self.generated["unresolved_quantities"], [])
        for record in self.generated["certificates"]:
            self.assertEqual(
                record["status"],
                "certified_nonnegative_for_lambda_ge_0",
                record["name"],
            )

    def test_compact_certificate_equals_regenerated_expressions(self) -> None:
        compact = {}
        compact.update(self.certificate["output_moments"])
        compact["output_det_H1"] = self.certificate["output_det_H1"]
        compact.update(self.certificate["hidden_moments"])
        compact["hidden_det_H1"] = self.certificate["hidden_det_H1"]
        for name, expression in compact.items():
            expected = parse_certificate_expression(expression)
            actual = sp.sympify(
                self.generated_by_name[name]["factored_expression"].replace(
                    "lambda", "metric_parameter"
                ),
                locals={"metric_parameter": analysis.lam},
            )
            self.assertEqual(sp.cancel(actual - expected), 0, name)

    def test_direct_series_reversion_at_exact_parameter_values(self) -> None:
        f = analysis.jets(self.raw, "f")
        q2 = analysis.jets(self.raw, "q2")
        y, s, unknown = sp.symbols("y s unknown")

        moment_expressions = {
            name: sp.sympify(
                record["factored_expression"].replace(
                    "lambda", "metric_parameter"
                ),
                locals={"metric_parameter": analysis.lam},
            )
            for name, record in self.generated_by_name.items()
        }

        for parameter in (sp.Integer(0), sp.Rational(1, 2),
                          sp.Integer(1), sp.Integer(2)):
            f_series = sum(
                f[order].subs(analysis.lam, parameter)
                / factorial(order) * s**order
                for order in (1, 3, 5, 7)
            )
            q_series = 3 + sum(
                q2[order].subs(analysis.lam, parameter)
                / factorial(order) * s**order
                for order in (2, 4, 6)
            )

            linear = sp.expand(f_series).coeff(s, 1)
            inverse = y / linear
            for degree in (3, 5):
                trial = inverse + unknown * y**degree
                coefficient = sp.expand(f_series.subs(s, trial)).coeff(y, degree)
                solution = sp.solve(sp.Eq(coefficient, 0), unknown)
                self.assertEqual(len(solution), 1)
                inverse = sp.expand(trial.subs(unknown, solution[0]))

            identity = sp.expand(f_series.subs(s, inverse))
            self.assertEqual(identity.coeff(y, 1), 1)
            self.assertEqual(identity.coeff(y, 3), 0)
            self.assertEqual(identity.coeff(y, 5), 0)

            kernel = sp.expand(sp.diff(f_series, s).subs(s, inverse))
            visible_q2 = sp.expand(q_series.subs(s, inverse))
            direct = {
                "mu_0": kernel.coeff(y, 2),
                "mu_1": -kernel.coeff(y, 4),
                "mu_2": kernel.coeff(y, 6),
                "nu_0": visible_q2.coeff(y, 2),
                "nu_1": -visible_q2.coeff(y, 4),
                "nu_2": visible_q2.coeff(y, 6),
            }
            for name, value in direct.items():
                expected = moment_expressions[name].subs(analysis.lam, parameter)
                self.assertEqual(sp.factor(value - expected), 0,
                                 (parameter, name))


if __name__ == "__main__":
    unittest.main()
