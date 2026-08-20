from __future__ import annotations

import dataclasses
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

import numpy as np
from scipy.special import roots_hermitenorm


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(SOURCE / "src"))

import run_experiment as runner  # noqa: E402
import analyze_activation as analysis  # noqa: E402
from activations import get_activation  # noqa: E402
from dense_pde.operator_galerkin import (  # noqa: E402
    PDESpec,
    PDEState,
    build_hybrid_quadrature,
    initialize as initialize_pde,
    observe,
    solve_fields,
    vector_field,
)
from dense_reference import (  # noqa: E402
    FieldState,
    ModelSpec,
    forward_adjoint,
    initialize as initialize_dense,
    parameter_vector_field,
    tangent_kernel,
)
from study_cases import load_case  # noqa: E402


EXTENSION_ACTIVATIONS = ("identity", "tanh_c2", "tanh_c4", "linear_c2")


def _option(command: tuple[str, ...], name: str) -> str:
    index = command.index(name)
    return command[index + 1]


class ActivationFormulaTests(unittest.TestCase):
    def test_exact_continuation_values_derivatives_and_lipschitz_bound(self) -> None:
        z = np.linspace(-3.0, 3.0, 61)
        formulas = {
            "identity": (z, np.ones_like(z)),
            "tanh": (np.tanh(z), 1.0 - np.tanh(z) ** 2),
            "tanh_c2": (
                np.tanh(2.0 * z) / 2.0,
                1.0 - np.tanh(2.0 * z) ** 2,
            ),
            "tanh_c4": (
                np.tanh(4.0 * z) / 4.0,
                1.0 - np.tanh(4.0 * z) ** 2,
            ),
        }
        epsilon = 2e-6
        for name, (expected_value, expected_derivative) in formulas.items():
            with self.subTest(name=name):
                activation = get_activation(name)
                np.testing.assert_allclose(
                    activation.value(z), expected_value, rtol=0.0, atol=0.0
                )
                np.testing.assert_allclose(
                    activation.derivative(z),
                    expected_derivative,
                    rtol=0.0,
                    atol=2e-16,
                )
                finite_difference = (
                    activation.value(z + epsilon)
                    - activation.value(z - epsilon)
                ) / (2.0 * epsilon)
                np.testing.assert_allclose(
                    finite_difference,
                    activation.derivative(z),
                    rtol=2e-8,
                    atol=2e-10,
                )
                self.assertGreaterEqual(
                    float(np.min(activation.derivative(z))), 0.0
                )
                self.assertLessEqual(
                    float(np.max(activation.derivative(z))), 1.0
                )

    def test_linear_null_kappa_matches_frozen_1024_point_quadrature(self) -> None:
        nodes, weights = roots_hermitenorm(1024)
        kappa = float(
            np.sum(
                weights
                / np.sqrt(2.0 * np.pi)
                / np.cosh(2.0 * 0.65 * nodes) ** 2
            )
        )
        protocol = json.loads(runner.PROTOCOL_PATH.read_text())
        self.assertEqual(kappa, protocol["linear_null_definition"]["kappa_2"])
        activation = get_activation("linear_c2")
        z = np.array([-1.25, 0.0, 0.75])
        np.testing.assert_array_equal(activation.value(z), kappa * z)
        np.testing.assert_array_equal(
            activation.derivative(z), np.full_like(z, kappa)
        )


class SharedDynamicsIdentityTests(unittest.TestCase):
    def test_dense_scaled_gradient_and_output_kernel_for_every_extension(self) -> None:
        X = np.eye(3)
        y = np.array([0.8, -0.55, 0.35])
        rng = np.random.default_rng(901)
        for activation in EXTENSION_ACTIVATIONS:
            with self.subTest(activation=activation):
                spec = ModelSpec(
                    n=7,
                    depth=3,
                    X=X,
                    y=y,
                    seed=773,
                    activation=activation,
                )
                state = initialize_dense(spec)

                def loss(candidate) -> float:
                    fields = forward_adjoint(candidate, spec)
                    residual = candidate.a @ fields.H[-1] / spec.n - spec.y
                    return float(0.5 * residual @ residual)

                velocity = parameter_vector_field(state, spec)
                epsilon = 2e-6
                multipliers = {"B": spec.n, "W": spec.depth, "a": spec.n}
                for name in ("B", "W", "a"):
                    direction = rng.normal(size=getattr(state, name).shape)
                    plus = type(state)(
                        state.B.copy(), state.W.copy(), state.a.copy()
                    )
                    minus = type(state)(
                        state.B.copy(), state.W.copy(), state.a.copy()
                    )
                    setattr(
                        plus,
                        name,
                        getattr(plus, name) + epsilon * direction,
                    )
                    setattr(
                        minus,
                        name,
                        getattr(minus, name) - epsilon * direction,
                    )
                    derivative = (loss(plus) - loss(minus)) / (2.0 * epsilon)
                    predicted = -float(
                        np.sum(getattr(velocity, name) * direction)
                    ) / multipliers[name]
                    self.assertLess(abs(derivative - predicted), 5e-8)

                fields = forward_adjoint(state, spec)
                f = state.a @ fields.H[-1] / spec.n
                residual = f - y
                theta = tangent_kernel(
                    FieldState(state.W, state.a, fields.H, fields.P),
                    spec,
                )
                step = 2e-7
                displaced = type(state)(
                    state.B + step * velocity.B,
                    state.W + step * velocity.W,
                    state.a + step * velocity.a,
                )
                displaced_fields = forward_adjoint(displaced, spec)
                f_next = displaced.a @ displaced_fields.H[-1] / spec.n
                self.assertLess(
                    np.linalg.norm((f_next - f) / step + theta @ residual),
                    3e-5,
                )
                self.assertGreaterEqual(
                    float(np.linalg.eigvalsh(theta)[0]), -1e-12
                )

    def test_pde_output_kernel_identity_for_every_extension(self) -> None:
        base_spec = PDESpec(
            X=np.eye(3),
            y=np.array([0.8, -0.55, 0.35]),
            basis_size=5,
            depth_nodes=3,
            base_points=81,
            fast_points=16,
            quadrature_seed=20260723,
            activation="identity",
        )
        quadrature = build_hybrid_quadrature(base_spec, base_order=3)
        for activation in EXTENSION_ACTIVATIONS:
            with self.subTest(activation=activation):
                spec = dataclasses.replace(base_spec, activation=activation)
                state = initialize_pde(spec, quadrature)
                fields = solve_fields(state, spec, quadrature)
                observable = observe(state, spec, quadrature, fields)
                velocity, _ = vector_field(state, spec, quadrature, fields)
                step = 2e-7
                displaced = PDEState(
                    B=state.B + step * velocity.B,
                    a=state.a + step * velocity.a,
                    c=state.c + step * velocity.c,
                )
                fdot = (
                    observe(displaced, spec, quadrature).f - observable.f
                ) / step
                predicted = -observable.theta @ (observable.f - spec.y)
                self.assertLess(np.linalg.norm(fdot - predicted), 4e-6)
                self.assertGreaterEqual(observable.theta_min, -1e-12)
                self.assertAlmostEqual(
                    observable.loss_dot,
                    -float(
                        (observable.f - spec.y)
                        @ observable.theta
                        @ (observable.f - spec.y)
                    ),
                    places=11,
                )


class ProtocolAndRunnerParityTests(unittest.TestCase):
    def test_scientific_patch_surface_is_exactly_allowlisted(self) -> None:
        lineage = runner._parent_source_lineage(runner._source_files())
        modified = {
            relative
            for relative, record in lineage["files"].items()
            if record["status"] == "modified"
        }
        new = {
            relative
            for relative, record in lineage["files"].items()
            if record["status"] == "new"
        }
        self.assertEqual(modified, runner.ALLOWED_SOURCE_PATCHES)
        self.assertEqual(new, set())
        self.assertEqual(
            lineage["parent_release_sha256"],
            runner.PARENT_RELEASE_SHA256,
        )

    def test_case_registry_is_the_exact_frozen_family(self) -> None:
        protocol = json.loads(runner.PROTOCOL_PATH.read_text())
        expected = {
            "C0": "identity",
            "C1": "tanh",
            "C2": "tanh_c2",
            "C4": "tanh_c4",
            "L2": "linear_c2",
        }
        self.assertEqual(
            tuple(protocol["primary_cases"] + protocol["linear_null_cases"]),
            runner.PRIMARY_CASES,
        )
        for case_id, activation in expected.items():
            case = load_case(runner.CASES_PATH, case_id)
            self.assertEqual(case.activation, activation)
            np.testing.assert_array_equal(case.X, np.eye(3))
            np.testing.assert_array_equal(case.y, [0.8, -0.55, 0.35])

    def test_every_pde_job_field_and_cli_matches_protocol(self) -> None:
        protocol = json.loads(runner.PROTOCOL_PATH.read_text())
        fixed = protocol["pde"]
        roles = {
            "primary": (
                runner.PRIMARY_CASES,
                fixed["seed"],
                fixed["N"],
            ),
            "scramble": (
                tuple(protocol["pde_numerical_controls"]["scramble_cases"]),
                protocol["pde_numerical_controls"][
                    "independent_scramble_seed"
                ],
                fixed["N"],
            ),
            "N32": (
                tuple(protocol["pde_depth_control"]["cases"]),
                fixed["seed"],
                protocol["pde_depth_control"]["N"],
            ),
        }
        for role, (case_ids, seed, N) in roles.items():
            jobs = runner._pde_jobs(role)
            self.assertEqual(tuple(job.case_id for job in jobs), case_ids)
            for job in jobs:
                expected = job.expected
                self.assertEqual(expected["basis_size_P"], fixed["P"])
                self.assertEqual(expected["depth_nodes_N"], N)
                self.assertEqual(expected["base_quadrature_M"], fixed["M"])
                self.assertEqual(expected["fast_quadrature_R"], fixed["R"])
                self.assertEqual(expected["quadrature_seed"], seed)
                for option, value in (
                    ("--P", fixed["P"]),
                    ("--N", N),
                    ("--M", fixed["M"]),
                    ("--R", fixed["R"]),
                    ("--seed", seed),
                    ("--quadrature", fixed["quadrature"]),
                    ("--base-order", fixed["base_order"]),
                    ("--integrator", fixed["integrator"]),
                    ("--dt", fixed["dt"]),
                    ("--sample-dt", fixed["sample_dt"]),
                    ("--duration", fixed["duration"]),
                ):
                    self.assertEqual(_option(job.command, option), str(value))

    def test_every_dense_job_field_and_cli_matches_protocol(self) -> None:
        protocol = json.loads(runner.PROTOCOL_PATH.read_text())
        tiers = {
            "primary": (runner.PRIMARY_CASES, protocol["dense_reference"]),
            "physical_depth": (
                tuple(protocol["physical_depth_control"]["cases"]),
                protocol["physical_depth_control"],
            ),
            "width": (
                tuple(protocol["physical_width_control"]["cases"]),
                protocol["physical_width_control"],
            ),
        }
        original_sha256 = runner._sha256

        def fake_sha256(path: Path) -> str:
            if Path(path) == runner.PDE_SEAL_PATH:
                return "pde-seal"
            return original_sha256(Path(path))

        with (
            mock.patch.object(
                runner,
                "_require_pde_seal",
                return_value={"dynamics_sha256": "dynamics"},
            ),
            mock.patch.object(runner, "_sha256", side_effect=fake_sha256),
        ):
            for role, (case_ids, tier) in tiers.items():
                jobs = runner._dense_jobs(role)
                self.assertEqual(tuple(job.case_id for job in jobs), case_ids)
                for job in jobs:
                    expected = job.expected
                    for field in (
                        "n",
                        "depth",
                        "seeds",
                        "seed_start",
                        "duration",
                        "dt",
                        "sample_dt",
                    ):
                        self.assertEqual(expected[field], tier[field])
                    for option, field in (
                        ("--n", "n"),
                        ("--depth", "depth"),
                        ("--seeds", "seeds"),
                        ("--seed-start", "seed_start"),
                        ("--duration", "duration"),
                        ("--dt", "dt"),
                        ("--sample-dt", "sample_dt"),
                    ):
                        self.assertEqual(
                            _option(job.command, option), str(tier[field])
                        )
                    self.assertEqual(
                        _option(job.command, "--pde-seal"),
                        str(runner.PDE_SEAL_PATH),
                    )
            primary = runner._dense_jobs("primary")
            self.assertEqual(
                {job.expected["seed_start"] for job in primary}, {61000}
            )
            self.assertEqual({job.expected["seeds"] for job in primary}, {16})


class SafeResumeTests(unittest.TestCase):
    @staticmethod
    def _job(directory: Path) -> runner.Job:
        expected = {"case_id": "C2", "token": 7}

        def validate(
            path: Path, required: dict[str, object]
        ) -> dict[str, object]:
            metadata = runner._metadata(path)
            runner._require_metadata(path, metadata, required)
            return metadata

        return runner.Job(
            role="synthetic",
            case_id="C2",
            command=("unused",),
            output_dir=directory,
            expected=expected,
            collision=lambda metadata: metadata.get("case_id") == "C2",
            validator=validate,
        )

    @staticmethod
    def _write(path: Path, metadata: dict[str, object]) -> None:
        np.savez_compressed(
            path,
            metadata_json=np.array(json.dumps(metadata, sort_keys=True)),
        )

    def test_resume_accepts_only_one_exact_metadata_match(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            path = directory / "result.npz"
            self._write(path, {"case_id": "C2", "token": 7})
            self.assertEqual(runner._find_completed(self._job(directory)), path)

    def test_resume_rejects_mismatch_duplicate_and_partial(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            job = self._job(directory)
            self._write(
                directory / "wrong.npz",
                {"case_id": "C2", "token": 8},
            )
            with self.assertRaises(runner.IntegrityError):
                runner._find_completed(job)

        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            job = self._job(directory)
            self._write(directory / "one.npz", {"case_id": "C2", "token": 7})
            self._write(directory / "two.npz", {"case_id": "C2", "token": 7})
            with self.assertRaises(runner.IntegrityError):
                runner._find_completed(job)

        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            job = self._job(directory)
            (directory / "interrupted.npz.partial").write_bytes(b"incomplete")
            with self.assertRaises(runner.IntegrityError):
                runner._find_completed(job)

    def test_first_freeze_rejects_preexisting_result_files(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results = Path(temporary) / "results"
            results.mkdir()
            (results / "unsealed-result.txt").write_text("too early")
            manifest = results / "FROZEN_INPUTS.json"
            with (
                mock.patch.object(runner, "RESULTS", results),
                mock.patch.object(runner, "INPUT_MANIFEST_PATH", manifest),
                mock.patch.object(
                    runner,
                    "_input_record",
                    return_value={"schema_version": 1},
                ),
            ):
                with self.assertRaises(runner.IntegrityError):
                    runner._create_input_manifest()


class AnalyzerPureFunctionTests(unittest.TestCase):
    @staticmethod
    def _curve(scale: float) -> analysis.Curve:
        times = np.array([0.0, 1.0, 2.0])
        f = np.array([[0.8], [0.8 - 0.1 * scale], [0.8 - 0.2 * scale]])
        grams = np.zeros((3, 2, 1, 1))
        grams[:, 0, 0, 0] = 1.0 + scale * np.array([0.0, 0.2, 0.4])
        grams[:, 1, 0, 0] = 2.0 + scale * np.array([0.0, 0.3, 0.6])
        return analysis.Curve(times, f, grams, {})

    def test_point_common_scales_equal_batch_one_scales(self) -> None:
        y = np.array([0.0])
        pde = {
            case_id: self._curve(0.5 + index)
            for index, case_id in enumerate(analysis.CASE_IDS)
        }
        dense = {
            case_id: self._curve(1.0 + 0.7 * index)
            for index, case_id in enumerate(analysis.CASE_IDS)
        }
        point = analysis._common_scales(pde, dense, y)
        batch = analysis._common_scales_batch(
            pde,
            {
                case_id: curve.f[None, ...]
                for case_id, curve in dense.items()
            },
            {
                case_id: curve.grams[None, ...]
                for case_id, curve in dense.items()
            },
            y,
        )
        for name in analysis.METRIC_NAMES:
            self.assertEqual(batch[name].shape, (1,))
            self.assertAlmostEqual(float(batch[name][0]), point[name], places=15)

    def test_centered_basic_interval_uses_deviations_from_point(self) -> None:
        interval = analysis._basic_interval(
            10.0,
            np.array([8.0, 9.0, 10.0, 11.0, 12.0]),
            confidence=0.8,
        )
        self.assertTrue(interval["available"])
        self.assertEqual(interval["lcb"], 8.0)
        self.assertEqual(interval["ucb"], 12.0)
        self.assertEqual(interval["method"], "one-sided centered/basic bootstrap")

    @staticmethod
    def _clock_curve(q: np.ndarray, *, altered: bool = False) -> tuple:
        initial_loss = 1.0
        terminal_loss = 0.01
        loss = initial_loss - q * (initial_loss - terminal_loss)
        f = np.sqrt(2.0 * loss)[:, None]
        grams = np.zeros((q.size, 2, 1, 1))
        grams[:, 0, 0, 0] = 1.0 + 0.4 * q
        grams[:, 1, 0, 0] = 2.0 + 0.8 * q
        if altered:
            grams[:, 1, 0, 0] += 0.3 * q * (1.0 - q)
        return f, grams

    def test_progress_alignment_removes_clock_but_detects_path_change(self) -> None:
        y = np.array([0.0])
        q_fast = np.array([0.0, 0.2, 0.5, 0.8, 1.0])
        q_slow = np.array([0.0, 0.05, 0.25, 0.7, 1.0])
        fast_f, fast_g = self._clock_curve(q_fast)
        slow_f, slow_g = self._clock_curve(q_slow)
        fast_path, fast_diagnostic = analysis._progress_path(
            fast_f, fast_g, y, 1.0
        )
        slow_path, slow_diagnostic = analysis._progress_path(
            slow_f, slow_g, y, 1.0
        )
        self.assertTrue(fast_diagnostic["valid"])
        self.assertTrue(slow_diagnostic["valid"])
        self.assertIsNotNone(fast_path)
        self.assertIsNotNone(slow_path)
        np.testing.assert_allclose(fast_path, slow_path, atol=1e-15, rtol=0.0)

        altered_f, altered_g = self._clock_curve(q_slow, altered=True)
        altered_path, altered_diagnostic = analysis._progress_path(
            altered_f, altered_g, y, 1.0
        )
        self.assertTrue(altered_diagnostic["valid"])
        self.assertIsNotNone(altered_path)
        self.assertGreater(
            analysis._progress_metric(
                fast_path, altered_path, scale=1.0
            )["raw"],
            0.05,
        )

        insufficient_loss = np.linspace(1.0, 0.1, q_fast.size)
        insufficient_f = np.sqrt(2.0 * insufficient_loss)[:, None]
        invalid_path, invalid_diagnostic = analysis._progress_path(
            insufficient_f, fast_g, y, 1.0
        )
        self.assertIsNone(invalid_path)
        self.assertFalse(invalid_diagnostic["valid"])
        self.assertLess(
            invalid_diagnostic["terminal_reduction_fraction"], 0.95
        )

    @staticmethod
    def _bound(*, lcb: float = 0.1, ucb: float = 0.01) -> dict:
        return {"available": True, "lcb": lcb, "ucb": ucb}

    def _verdict_inputs(self) -> tuple[dict, dict, dict, dict, dict, dict]:
        bounds: dict[str, dict] = {}
        for metric in analysis.METRIC_NAMES:
            bounds[f"dense_separation_C2_C0_{metric}"] = self._bound(
                lcb=0.08, ucb=0.12
            )
            bounds[f"matched_C2_{metric}"] = self._bound(
                lcb=0.005, ucb=0.02
            )
            bounds[f"identity_margin_C2_{metric}"] = self._bound(
                lcb=0.03, ucb=0.08
            )
            bounds[f"matched_C0_{metric}"] = self._bound(
                lcb=0.005, ucb=0.02
            )
        bounds["dense_separation_C2_L2_gram"] = self._bound(
            lcb=0.08, ucb=0.12
        )
        bounds["linear_null_margin_C2_gram"] = self._bound(
            lcb=0.02, ucb=0.08
        )
        bounds["progress_separation_C2_C0_gram"] = self._bound(
            lcb=0.08, ucb=0.12
        )
        bounds["progress_clock_margin_C2_gram"] = self._bound(
            lcb=0.02, ucb=0.08
        )
        observed = {
            "dense_separation_C2_C0_gram": 0.1,
            "matched_C2_gram": 0.02,
            "identity_margin_C2_gram": 0.06,
        }
        numerical = {
            "central_C0_C2_gram_pass": True,
            "all_metrics_pass": True,
        }
        controls = {
            "physical_depth_L64": {"criterion_pass": True},
            "physical_width_n256": {"point_criterion_pass": True},
        }
        plateau = {
            source: {
                case_id: {"pass": True}
                for case_id in ("C0", "C2")
            }
            for source in ("pde", "dense")
        }
        progress = {"valid": False}
        return bounds, observed, numerical, controls, plateau, progress

    def test_verdict_full_and_identity_only_require_all_gates(self) -> None:
        bounds, observed, numerical, controls, plateau, progress = (
            self._verdict_inputs()
        )
        result = analysis._decision_summary(
            bounds=bounds,
            observed=observed,
            numerical=numerical,
            controls=controls,
            plateau=plateau,
            progress=progress,
        )
        self.assertEqual(result["status"], "full_nonlinear_smoking_gun")
        self.assertTrue(result["full_nonlinear_smoking_gun"])

        for gate in ("numerical", "L64"):
            with self.subTest(gate=gate):
                changed_numerical = dict(numerical)
                changed_controls = {
                    key: dict(value) for key, value in controls.items()
                }
                if gate == "numerical":
                    changed_numerical["central_C0_C2_gram_pass"] = False
                else:
                    changed_controls["physical_depth_L64"][
                        "criterion_pass"
                    ] = False
                changed = analysis._decision_summary(
                    bounds=bounds,
                    observed=observed,
                    numerical=changed_numerical,
                    controls=changed_controls,
                    plateau=plateau,
                    progress=progress,
                )
                self.assertFalse(changed["full_nonlinear_smoking_gun"])
                self.assertNotEqual(changed["status"], "identity_only")

        no_hermite = {key: dict(value) for key, value in bounds.items()}
        no_hermite["dense_separation_C2_L2_gram"] = self._bound(
            lcb=0.04, ucb=0.08
        )
        identity_only = analysis._decision_summary(
            bounds=no_hermite,
            observed=observed,
            numerical=numerical,
            controls=controls,
            plateau=plateau,
            progress=progress,
        )
        self.assertFalse(identity_only["full_nonlinear_smoking_gun"])
        self.assertEqual(identity_only["status"], "identity_only")


if __name__ == "__main__":
    unittest.main()
