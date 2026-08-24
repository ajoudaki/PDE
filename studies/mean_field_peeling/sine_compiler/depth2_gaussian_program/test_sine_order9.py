#!/usr/bin/env python3
"""Regression tests for the sine order-nine jet and Stieltjes audit."""

from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent


def load_local_module(name: str, filename: str):
    specification = importlib.util.spec_from_file_location(name, HERE / filename)
    if specification is None or specification.loader is None:
        raise ImportError(f"cannot load {filename}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[name] = module
    specification.loader.exec_module(module)
    return module


jet = load_local_module("audited_sine_order9_jet", "sine_order9_fourier_jet.py")
audit = load_local_module(
    "audited_sine_order9_stieltjes", "sine_order9_stieltjes_audit.py"
)


EXPECTED_MOMENTS = {
    "raw": (
        "-0.9434999136529655504418686636891236332331610305201667731539700107680928",
        "-2.715496517630591577732843593792595655029759207956406961991441133730917",
        "-5.222603092247065806283137976963998408098232099621546702828924733368240",
        "-7.893144651688340729494564448635347142174077425496975479744701885906361",
    ),
    "unit": (
        "-3.167761986081301856339603192211488286866268849791970185139734630617375",
        "-3.039997378378462353769286037927400822815869841381064986206001805646702",
        "-2.209669949291420225769035078102751152560384613236352418337456165249762",
        "-1.597796844891077062398749838424655681819033506165232726651574566339681",
    ),
}


class SineOrderNineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        mp.mp.dps = 120
        cls.document = json.loads((HERE / "results_order9.json").read_text())
        cls.records: dict[str, dict[str, object]] = {}
        for name, record in cls.document["activations"].items():
            derivatives = [mp.mpf(value) for value in record["taylor_100dps"]]
            baseline_a, moments_a, _ = audit.moments_by_reversion(derivatives)
            baseline_b, moments_b, _ = audit.moments_by_triangular_identity(
                derivatives
            )
            cls.records[name] = {
                "baseline_a": baseline_a,
                "baseline_b": baseline_b,
                "moments_a": moments_a,
                "moments_b": moments_b,
                "hankels": audit.audit_hankels(moments_a),
            }

    def assertRelativeClose(self, left, right, tolerance="1e-65") -> None:
        self.assertLess(
            audit.relative_error(mp.mpf(left), mp.mpf(right)),
            mp.mpf(tolerance),
        )

    def test_protocol_and_provenance_hashes(self) -> None:
        actual = {
            "input": audit.sha256(audit.INPUT),
            "protocol": audit.sha256(audit.PROTOCOL),
            "engine": audit.sha256(audit.ENGINE),
        }
        self.assertEqual(actual, audit.EXPECTED_SHA256)
        self.assertEqual(
            actual["protocol"], jet.EXPECTED_PROTOCOL_SHA256
        )

    def test_stored_derivative_routes_and_precisions_agree(self) -> None:
        for record in self.document["activations"].values():
            taylor_100 = [mp.mpf(value) for value in record["taylor_100dps"]]
            derivative_100 = [
                mp.mpf(value) for value in record["derivative_100dps"]
            ]
            taylor_80 = [mp.mpf(value) for value in record["taylor_80dps"]]
            self.assertLess(
                max(
                    audit.relative_error(left, right)
                    for left, right in zip(taylor_100, derivative_100)
                ),
                mp.mpf("1e-65"),
            )
            self.assertLess(
                max(
                    audit.relative_error(left, right)
                    for left, right in zip(taylor_100, taylor_80)
                ),
                mp.mpf("1e-55"),
            )
            self.assertTrue(all(taylor_100[order] == 0 for order in range(0, 10, 2)))

    def test_live_low_order_independent_assemblers(self) -> None:
        for activation in ("raw", "unit"):
            taylor = jet.taylor_jet(3, dps=75, activation=activation)
            derivative = jet.derivative_jet(3, dps=75, activation=activation)
            jet.validate_results((taylor, derivative), 3)
            for left, right in zip(taylor.derivatives, derivative.derivatives):
                self.assertRelativeClose(left, right, "1e-60")

    def test_unit_activation_has_unit_gaussian_variance(self) -> None:
        for activation in ("raw", "unit"):
            algebra, column, _, scale = jet._setup(1, 100, activation)
            expected = (
                (1 - mp.exp(-2)) / 2 if activation == "raw" else mp.mpf(1)
            )
            activation_value = algebra.sine(0, scale)
            variance = column.real(
                column.product_expectation(activation_value, activation_value),
                label="activation variance",
            )
            self.assertRelativeClose(variance, expected, "1e-80")

    def test_two_moment_routes_and_frozen_moments(self) -> None:
        for name, record in self.records.items():
            self.assertRelativeClose(
                record["baseline_a"], record["baseline_b"]
            )
            for value_a, value_b, expected in zip(
                record["moments_a"],
                record["moments_b"],
                EXPECTED_MOMENTS[name],
            ):
                self.assertRelativeClose(value_a, value_b)
                self.assertRelativeClose(value_a, expected)

    def test_all_accessible_stieltjes_conditions_fail(self) -> None:
        for record in self.records.values():
            moments = record["moments_a"]
            hankels = record["hankels"]
            self.assertTrue(all(moment < 0 for moment in moments))
            self.assertFalse(
                hankels["all_accessible_matrices_positive_semidefinite"]
            )
            self.assertTrue(
                all(
                    not condition["holds"]
                    for condition in hankels["six_unique_psd_conditions"].values()
                )
            )
            self.assertFalse(hankels["cross_minor"]["nonnegative"])


if __name__ == "__main__":
    unittest.main()
