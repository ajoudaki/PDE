#!/usr/bin/env python3
"""Small deterministic checks for ANALYZE.py; no campaign data or training.

Scientific input scope: the supervisor's interface specification and ANALYZE.py.
These checks use analytic Fourier identities and scipy.linalg.expm as oracles.
Run from any directory; each execution keeps a fresh generated evidence folder.
"""

from __future__ import annotations

import contextlib
import datetime as dt
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import platform
import sys
import time
import types
import unittest

# Keep the tiny oracle computations within the assigned CPU budget.
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"

import numpy as np
import scipy
from scipy.linalg import expm


SOURCE = Path(__file__).with_name("ANALYZE.py")
SOURCE_SHA256 = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
MEASUREMENTS = {}
sys.dont_write_bytecode = True
_spec = importlib.util.spec_from_file_location("spectral_mechanism_analyze", SOURCE)
assert _spec is not None and _spec.loader is not None
analyze = importlib.util.module_from_spec(_spec)
sys.modules[_spec.name] = analyze
# The unused campaign-only NTK dependency is outside this assignment's inputs.
# Fail loudly if a synthetic check accidentally crosses into that dependency.
_ntk_sentinel = types.ModuleType("NTK")


def _forbidden_kernel(*args, **kwargs):
    raise AssertionError("The campaign NTK dependency is outside this check's input scope")


_ntk_sentinel.kernel = _forbidden_kernel
_prior_ntk = sys.modules.get("NTK")
sys.modules["NTK"] = _ntk_sentinel
try:
    _spec.loader.exec_module(analyze)
finally:
    if _prior_ntk is None:
        del sys.modules["NTK"]
    else:
        sys.modules["NTK"] = _prior_ntk


def assert_close(actual, expected, *, atol=2e-12, rtol=2e-12):
    np.testing.assert_allclose(actual, expected, atol=atol, rtol=rtol)


class SpectralChecks(unittest.TestCase):
    def test_one_sided_power_and_parseval(self):
        for n in (63, 64):
            theta = 2 * np.pi * np.arange(n) / n
            f = 0.3 + np.sin(theta) + 0.2 * np.cos(3 * theta)
            coeff, power = analyze.spectrum(f)
            with self.subTest(n=n):
                assert_close(coeff[0], 0.3)
                assert_close(coeff[1], -0.5j)
                assert_close(coeff[3], 0.1)
                assert_close(power[[0, 1, 3]], np.array([0.09, 0.5, 0.02]))
                assert_close(np.sum(power), np.mean(f**2))
        _, nyquist_power = analyze.spectrum((-1.0) ** np.arange(64))
        assert_close(nyquist_power[-1], 1)
        assert_close(np.sum(nyquist_power), 1)

    def test_exact_two_mode_signal(self):
        theta = 2 * np.pi * np.arange(720) / 720
        m = analyze.spectral_metrics(np.sin(theta) + 0.2 * np.sin(3 * theta))
        for key, expected in {
            "energy": 0.52,
            "k_rms": np.sqrt(1.36 / 1.04),
            "k99": 3,
            "tail_ge3": 0.04 / 1.04,
            "tail_ge5": 0,
            "tail_ge7": 0,
            "mode1_fraction": 1 / 1.04,
            "even_fraction": 0,
            "mean_fraction": 0,
        }.items():
            with self.subTest(metric=key):
                assert_close(m[key], expected)

    def test_phase_scale_and_grid_invariance(self):
        def signal(n, phase=0.0):
            theta = 2 * np.pi * np.arange(n) / n + phase
            return 0.3 + np.sin(theta) + 0.4 * np.cos(2 * theta) + 0.2 * np.sin(7 * theta)

        base = analyze.spectral_metrics(signal(720))
        for f, energy_factor in (
            (signal(720, 0.271), 1.0),
            (-3.25 * signal(720), 3.25**2),
            (signal(1440), 1.0),
        ):
            measured = analyze.spectral_metrics(f)
            for key in base:
                with self.subTest(metric=key, energy_factor=energy_factor, n=len(f)):
                    expected = base[key] * energy_factor if key == "energy" else base[key]
                    assert_close(measured[key], expected)

    def test_mean_even_modes_and_nyquist(self):
        theta = 2 * np.pi * np.arange(64) / 64
        f = 2 + 3 * np.cos(2 * theta) + np.sin(5 * theta)
        m = analyze.spectral_metrics(f)
        # Parseval: DC contributes 4, cos(2 theta) 9/2, sin(5 theta) 1/2.
        assert_close(m["energy"], 9)
        assert_close(m["mean_fraction"], 4 / 9)
        assert_close(m["even_fraction"], 0.5)
        assert_close(m["tail_ge3"], 1 / 18)
        assert_close(m["tail_ge5"], 1 / 18)
        assert_close(m["tail_ge7"], 0)
        assert_close(m["k_rms"], np.sqrt(30.5 / 9))
        nyquist = analyze.spectral_metrics((-1.0) ** np.arange(64))
        assert_close(nyquist["energy"], 1)
        assert_close(nyquist["k_rms"], 32)
        assert_close(nyquist["k99"], 32)


class KernelGeometryChecks(unittest.TestCase):
    def test_stationary_kernel_is_fourier_diagonal(self):
        theta = 2 * np.pi * np.arange(48) / 48
        delta = theta[:, None] - theta[None, :]
        kernel = 0.3 + np.cos(delta) + 0.2 * np.cos(3 * delta)
        metric = analyze.kernel_geometry(kernel)["offdiagonal_fraction"]
        assert_close(metric, 0, atol=2e-12)

    def test_rank_one_cosine_is_not_stationary(self):
        theta = 2 * np.pi * np.arange(48) / 48
        kernel = np.outer(np.cos(theta), np.cos(theta))
        metric = analyze.kernel_geometry(kernel)["offdiagonal_fraction"]
        # Four equal nonzero Fourier entries: two diagonal, two off diagonal.
        assert_close(metric, 0.5)


class FrozenKernelChecks(unittest.TestCase):
    def test_diagonal_physical_clock_and_cross_predictions(self):
        diagonal = np.array([1.0, 2.0, 4.0])
        weights = np.array([1 / 6, 1 / 3, 1 / 2])
        labels = np.array([1.0, -2.0, 0.5])
        cross = np.array([[0.5, -0.2, 1.2], [1.0, 0.5, 0.0]])
        model = analyze.FrozenKernel(np.diag(diagonal), cross, labels, weights)
        for t in (0.0, 0.013, 0.7, 4.0):
            expected_train = labels * (-np.expm1(-2 * diagonal * weights * t))
            with self.subTest(t=t):
                assert_close(model.train(t), expected_train)
                assert_close(model.predict(t), cross @ (expected_train / diagonal))
        assert_close(model.train(np.inf), labels)
        assert_close(model.predict(np.inf), cross @ (labels / diagonal))

    def test_nonuniform_weights_against_matrix_exponential(self):
        kernel = np.array([[2.0, 0.3], [0.3, 1.0]])
        weights = np.array([0.2, 0.8])
        labels = np.array([1.0, -2.0])
        cross = np.array([[0.1, 0.4], [2.0, -0.5], [0.3, 0.3]])
        model = analyze.FrozenKernel(kernel, cross, labels, weights)
        for t in (0.0, 1e-5, 0.2, 2.0, 10.0):
            expected_train = labels - expm(-2 * kernel @ np.diag(weights) * t) @ labels
            with self.subTest(t=t):
                assert_close(model.train(t), expected_train)
                assert_close(model.predict(t), cross @ np.linalg.solve(kernel, expected_train))
        assert_close(model.train(np.inf), labels)
        assert_close(model.predict(np.inf), cross @ np.linalg.solve(kernel, labels))

    def test_singular_consistent_and_conflicting_labels(self):
        kernel = np.ones((2, 2))
        cross = np.array([[2.0, 2.0], [-0.5, -0.5]])
        weights = np.array([0.25, 0.75])
        for labels in (np.array([2.0, 2.0]), np.array([1.0, -1.0])):
            model = analyze.FrozenKernel(kernel, cross, labels, weights)
            weighted_mean = weights @ labels
            for t in (0.0, 0.2, 3.0):
                fraction = -np.expm1(-2 * t)
                expected_train = np.full(2, weighted_mean * fraction)
                with self.subTest(labels=labels.tolist(), t=t):
                    assert_close(model.train(t), expected_train)
                    assert_close(model.predict(t), np.array([2.0, -0.5]) * weighted_mean * fraction)
            if np.all(labels == labels[0]):
                assert_close(model.train(np.inf), labels)
                assert_close(model.predict(np.inf), np.array([2.0, -0.5]) * weighted_mean)
            else:
                # This API reserves infinity for an interpolating endpoint and
                # explicitly rejects contradictory labels at numerical rank.
                with self.assertRaisesRegex(ValueError, "cannot interpolate"):
                    model.train(np.inf)
                with self.assertRaisesRegex(ValueError, "cannot interpolate"):
                    model.predict(np.inf)

    def test_infinite_time_is_exact_endpoint(self):
        # The second direction is far from its endpoint at a large finite time.
        kernel = np.diag([1.0, 1e-8])
        labels = np.array([1.0, -2.0])
        model = analyze.FrozenKernel(kernel, kernel, labels, np.array([0.5, 0.5]))
        self.assertGreater(abs(model.train(1e5)[1] - labels[1]), 1.9)
        assert_close(model.train(np.inf), labels)
        assert_close(model.predict(np.inf), labels)


class DistanceChecks(unittest.TestCase):
    def test_amplitude_error_and_separate_shape_normalization(self):
        b = np.array([3.0, 4.0])
        m = analyze.distance(2 * b, b, 5.0)
        assert_close(m["rms"], np.sqrt(12.5))
        assert_close(m["max"], 4)
        assert_close(m["relative_rms"], 1)
        assert_close(m["normalized_shape_rms"], 0)

        m = analyze.distance(-b, b, 5.0)
        assert_close(m["normalized_shape_rms"], 2)
        m = analyze.distance(np.array([1.0, 0.0]), np.ones(2), 1.0)
        assert_close(m["rms"], np.sqrt(0.5))
        assert_close(m["relative_rms"], np.sqrt(0.5))
        assert_close(m["normalized_shape_rms"], np.sqrt(2 - np.sqrt(2)))

    def test_reference_floor(self):
        m = analyze.distance(np.array([1.0, -1.0]), np.zeros(2), 5.0)
        assert_close(m["rms"], 1)
        assert_close(m["max"], 1)
        assert_close(m["relative_rms"], 1 / (5e-12))


class TemplateFitChecks(unittest.TestCase):
    def test_normalized_tanh_sine_recovers_known_parameter(self):
        theta = 2 * np.pi * np.arange(720) / 720
        kappa, amplitude = 2.3, 0.2
        midpoint, separation = np.deg2rad([45.0, 30.0])
        f = amplitude * np.tanh(kappa * np.sin(theta - midpoint)) / np.tanh(
            kappa * np.sin(separation / 2)
        )
        fits, curves = analyze.fit_templates(
            f, {"kind": "pair", "rotation": 45.0, "delta": 30.0, "amplitude": amplitude}
        )
        fit = fits["normalized_tanh_sine"]
        self.assertLess(abs(fit["kappa"] - kappa), 1e-4)
        self.assertLess(fit["heldout"]["relative_rms"], 1e-6)
        self.assertFalse(fit["at_boundary"])
        self.assertLess(np.sqrt(np.mean((curves["template_normalized_tanh_sine"] - f) ** 2)), 1e-6)
        MEASUREMENTS["normalized_tanh_sine"] = {
            "expected_kappa": kappa,
            "recovered_kappa": fit["kappa"],
            "heldout_relative_rms": fit["heldout"]["relative_rms"],
        }

    def test_odd_fourier_menu_resolves_third_mode(self):
        theta = 2 * np.pi * np.arange(720) / 720
        f = np.sin(theta) + 0.2 * np.cos(3 * theta)
        fits, curves = analyze.fit_templates(f, {"kind": "synthetic", "amplitude": 1.0})
        lower, exact = fits["odd_through_1"], fits["odd_through_3"]
        assert_close(exact["coefficients"], np.array([0.0, 1.0, 0.2, 0.0]))
        assert_close(curves["template_odd_through_3"], f)
        assert_close(curves["template_odd_through_1"], np.sin(theta))
        for partition in ("whole", "fit", "heldout"):
            with self.subTest(partition=partition):
                self.assertLess(exact[partition]["relative_rms"], 1e-12)
                assert_close(lower[partition]["relative_rms"], 0.2 / np.sqrt(1.04))
        self.assertGreater(lower["heldout"]["relative_rms"], 0.1)
        MEASUREMENTS["odd_fourier_menu"] = {
            "through_1_heldout_relative_rms": lower["heldout"]["relative_rms"],
            "through_3_heldout_relative_rms": exact["heldout"]["relative_rms"],
        }


def main():
    started = time.process_time()
    root = SOURCE.parents[2]
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    output = root / "data/generated/closure_circle_spectral_mechanism" / f"analysis_checks_{stamp}"
    output.mkdir(parents=True, exist_ok=False)
    captured = io.StringIO()
    suite = unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__])
    with contextlib.redirect_stdout(captured):
        result = unittest.TextTestRunner(stream=captured, verbosity=2).run(suite)
    report = {
        "source": str(SOURCE.relative_to(root)),
        "source_sha256": SOURCE_SHA256,
        "source_unchanged_during_check": hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
        "check_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scientific_inputs": ["supervisor interface specification", "ANALYZE.py"],
        "dependency_scope": "The unused NTK import is replaced by a raising sentinel; this does not test full campaign import integration.",
        "command": f"python {Path(__file__).relative_to(root)}",
        "python": platform.python_version(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "thread_environment": {key: os.environ[key] for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
        "tests_run": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "passed": result.wasSuccessful() and hashlib.sha256(SOURCE.read_bytes()).hexdigest() == SOURCE_SHA256,
        "cpu_seconds": time.process_time() - started,
        "template_measurements": MEASUREMENTS,
        "scope": "Synthetic analyzer verification only; no empirical campaign inputs or training.",
    }
    (output / "check.log").write_text(captured.getvalue())
    (output / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(captured.getvalue(), end="")
    print(json.dumps(report, indent=2))
    print(f"Evidence: {output}")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
