from __future__ import annotations

import dataclasses
from pathlib import Path
import sys
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "source"))

from pde_tangent import (  # noqa: E402
    ResidualImpulse,
    block_state_arclength,
    coupled_rk4_step,
    flattened_response_svd,
    integrate_state_checkpoints,
    nonlinear_impulse_check,
    observable_jvp,
    pack_weighted_state,
    projected_back_residual,
    residual_subspace_l1_to_linf_gain,
    solve_fields_jvp,
    stage5_serializable_result,
    unpack_weighted_state,
    vector_field_jvp,
    weighted_tangent_inner_product,
    weighted_tangent_norm,
)
from cross_p import build_nested_quadratures  # noqa: E402
from dense_pde.operator_galerkin import (  # noqa: E402
    PDESpec,
    PDEState,
    build_quadrature,
    initialize,
    observe,
    rk4_step,
    solve_fields,
    vector_field,
)


def _spec(*, activation: str = "tanh") -> PDESpec:
    return PDESpec(
        X=np.array([[1.0, -0.35]]),
        y=np.array([0.65, -0.2]),
        basis_size=2,
        depth_nodes=2,
        base_points=8,
        fast_points=8,
        quadrature_seed=8675309,
        sigma_w=0.5,
        A=0.9,
        gamma=0.7,
        activation=activation,
    )


def _random_state_and_direction(
    spec: PDESpec, seed: int = 112
) -> tuple[object, PDEState, PDEState]:
    quadrature = build_quadrature(spec)
    state = initialize(spec, quadrature)
    rng = np.random.default_rng(seed)
    state.B += rng.normal(scale=0.08, size=state.B.shape)
    state.a += rng.normal(scale=0.08, size=state.a.shape)
    state.c += rng.normal(scale=0.06, size=state.c.shape)
    direction = PDEState(
        B=rng.normal(size=state.B.shape),
        a=rng.normal(size=state.a.shape),
        c=rng.normal(size=state.c.shape),
    )
    norm = float(weighted_tangent_norm(direction, quadrature))
    direction = _scale(direction, 1.0 / norm)
    return quadrature, state, direction


def _scale(state: PDEState, factor: float) -> PDEState:
    return PDEState(
        B=factor * state.B,
        a=factor * state.a,
        c=factor * state.c,
    )


def _shift(state: PDEState, direction: PDEState, step: float) -> PDEState:
    return PDEState(
        B=state.B + step * direction.B,
        a=state.a + step * direction.a,
        c=state.c + step * direction.c,
    )


def _central_state(
    plus: PDEState, minus: PDEState, step: float
) -> PDEState:
    return PDEState(
        B=(plus.B - minus.B) / (2.0 * step),
        a=(plus.a - minus.a) / (2.0 * step),
        c=(plus.c - minus.c) / (2.0 * step),
    )


class FieldAndGeneratorJVPTests(unittest.TestCase):
    def test_all_field_arrays_match_centered_finite_differences(self) -> None:
        spec = _spec()
        quadrature, state, mixed = _random_state_and_direction(spec)
        zero_B = np.zeros_like(state.B)
        zero_a = np.zeros_like(state.a)
        zero_c = np.zeros_like(state.c)
        directions = {
            "B": PDEState(mixed.B, zero_a, zero_c),
            "a": PDEState(zero_B, mixed.a, zero_c),
            "c": PDEState(zero_B, zero_a, mixed.c),
            "mixed": mixed,
        }
        step = 2e-5
        for name, direction in directions.items():
            with self.subTest(direction=name):
                tangent, _ = solve_fields_jvp(
                    state, direction, spec, quadrature
                )
                plus = solve_fields(
                    _shift(state, direction, step), spec, quadrature
                )
                minus = solve_fields(
                    _shift(state, direction, -step), spec, quadrature
                )
                comparisons = (
                    ("h", tangent.dh, plus.h, minus.h),
                    ("p", tangent.dp, plus.p, minus.p),
                    ("z", tangent.dz, plus.z, minus.z),
                    ("D", tangent.dD, plus.D, minus.D),
                    ("beta", tangent.dbeta, plus.beta, minus.beta),
                    (
                        "hcoef",
                        tangent.dhcoef,
                        plus.hcoef,
                        minus.hcoef,
                    ),
                )
                for field_name, exact, upper, lower in comparisons:
                    with self.subTest(field=field_name):
                        finite_difference = (
                            upper - lower
                        ) / (2.0 * step)
                        np.testing.assert_allclose(
                            exact,
                            finite_difference,
                            rtol=3e-7,
                            atol=2e-9,
                        )

    def test_vector_field_jvp_converges_quadratically_in_fd_step(self) -> None:
        for activation in ("tanh", "identity"):
            with self.subTest(activation=activation):
                spec = _spec(activation=activation)
                quadrature, state, direction = _random_state_and_direction(
                    spec
                )
                exact = vector_field_jvp(
                    state, direction, spec, quadrature
                )
                errors = []
                for step in (4e-3, 2e-3, 1e-3):
                    plus, _ = vector_field(
                        _shift(state, direction, step),
                        spec,
                        quadrature,
                    )
                    minus, _ = vector_field(
                        _shift(state, direction, -step),
                        spec,
                        quadrature,
                    )
                    finite_difference = _central_state(plus, minus, step)
                    defect = PDEState(
                        B=finite_difference.B - exact.B,
                        a=finite_difference.a - exact.a,
                        c=finite_difference.c - exact.c,
                    )
                    errors.append(
                        float(weighted_tangent_norm(defect, quadrature))
                    )
                self.assertLess(errors[1], 0.28 * errors[0])
                self.assertLess(errors[2], 0.28 * errors[1])

    def test_observable_jvp_includes_all_depth_grams_and_theta(self) -> None:
        spec = _spec()
        quadrature, state, direction = _random_state_and_direction(spec)
        exact = observable_jvp(state, direction, spec, quadrature)
        step = 2e-5
        plus = observe(
            _shift(state, direction, step), spec, quadrature
        )
        minus = observe(
            _shift(state, direction, -step), spec, quadrature
        )
        np.testing.assert_allclose(
            exact.f,
            (plus.f - minus.f) / (2.0 * step),
            rtol=2e-7,
            atol=2e-9,
        )
        self.assertAlmostEqual(
            exact.loss,
            (plus.loss - minus.loss) / (2.0 * step),
            delta=2e-9,
        )
        self.assertEqual(
            exact.grams.shape,
            (spec.depth_nodes + 1, spec.y.size, spec.y.size),
        )
        np.testing.assert_allclose(
            exact.grams,
            (plus.grams - minus.grams) / (2.0 * step),
            rtol=3e-7,
            atol=3e-9,
        )
        np.testing.assert_allclose(
            exact.theta,
            (plus.theta - minus.theta) / (2.0 * step),
            rtol=5e-7,
            atol=4e-9,
        )
        np.testing.assert_allclose(exact.theta, exact.theta.T, atol=2e-14)


class WeightedCoordinatesAndRK4Tests(unittest.TestCase):
    def test_weighted_pack_realizes_cross_p_inner_product(self) -> None:
        spec = _spec()
        quadrature, state, left = _random_state_and_direction(spec)
        rng = np.random.default_rng(923)
        right = PDEState(
            B=rng.normal(size=state.B.shape),
            a=rng.normal(size=state.a.shape),
            c=rng.normal(size=state.c.shape),
        )
        packed_left = pack_weighted_state(left, quadrature)
        packed_right = pack_weighted_state(right, quadrature)
        self.assertAlmostEqual(
            float(packed_left @ packed_right),
            weighted_tangent_inner_product(left, right, quadrature),
            places=13,
        )
        self.assertAlmostEqual(
            float(np.linalg.norm(packed_left)),
            float(weighted_tangent_norm(left, quadrature)),
            places=13,
        )
        recovered = unpack_weighted_state(
            packed_right, state, quadrature
        )
        np.testing.assert_allclose(recovered.B, right.B, rtol=2e-16)
        np.testing.assert_allclose(recovered.a, right.a, rtol=2e-16)
        np.testing.assert_allclose(recovered.c, right.c, rtol=2e-16)

    def test_coupled_rk4_is_primal_rk4_and_derivative_of_its_map(self) -> None:
        spec = _spec()
        quadrature, state, direction = _random_state_and_direction(spec)
        dt = 0.015
        primal, tangent = coupled_rk4_step(
            state, direction, dt, spec, quadrature
        )
        canonical = rk4_step(state, dt, spec, quadrature)
        np.testing.assert_allclose(primal.B, canonical.B, atol=0.0, rtol=0.0)
        np.testing.assert_allclose(primal.a, canonical.a, atol=0.0, rtol=0.0)
        np.testing.assert_allclose(primal.c, canonical.c, atol=0.0, rtol=0.0)

        errors = []
        for step in (4e-3, 2e-3, 1e-3):
            plus = rk4_step(
                _shift(state, direction, step), dt, spec, quadrature
            )
            minus = rk4_step(
                _shift(state, direction, -step), dt, spec, quadrature
            )
            finite_difference = _central_state(plus, minus, step)
            defect = PDEState(
                B=finite_difference.B - tangent.B,
                a=finite_difference.a - tangent.a,
                c=finite_difference.c - tangent.c,
            )
            errors.append(
                float(weighted_tangent_norm(defect, quadrature))
            )
        self.assertLess(errors[1], 0.28 * errors[0])
        self.assertLess(errors[2], 0.28 * errors[1])


class StabilityInfrastructureTests(unittest.TestCase):
    def test_compact_responses_are_numerically_identical(self) -> None:
        spec = _spec()
        quadrature, state, direction = _random_state_and_direction(spec)
        arguments = dict(
            initial_state=state,
            impulses=(ResidualImpulse(0.0, direction, "unit"),),
            observation_times=(0.0, 0.01, 0.02),
            max_step=0.01,
            spec=spec,
            quadrature=quadrature,
            observable_blocks=("f", "grams"),
        )
        full = residual_subspace_l1_to_linf_gain(
            **arguments, retain_response_states=True
        )
        compact = residual_subspace_l1_to_linf_gain(
            **arguments, retain_response_states=False
        )
        self.assertAlmostEqual(full.gain, compact.gain, places=14)
        np.testing.assert_array_equal(
            full.flattened_response_columns,
            compact.flattened_response_columns,
        )
        self.assertTrue(full.responses[0].trajectory.states)
        self.assertFalse(compact.responses[0].trajectory.states)
        self.assertFalse(compact.responses[0].trajectory.tangents)

    def test_single_direction_groups_reduce_to_exact_max_column(self) -> None:
        spec = _spec()
        quadrature, state, direction = _random_state_and_direction(spec)
        impulses = (
            ResidualImpulse(0.0, direction, "unit"),
            # Same atom at a later time and with arbitrary raw scaling.  The
            # routine must normalize with the weighted state norm.
            ResidualImpulse(0.01, _scale(direction, -3.5), "late_scaled"),
        )
        result = residual_subspace_l1_to_linf_gain(
            state,
            impulses,
            (0.0, 0.01, 0.02),
            max_step=0.01,
            spec=spec,
            quadrature=quadrature,
            observable_blocks=("f", "grams"),
        )
        self.assertAlmostEqual(result.gain, float(np.max(result.column_gains)))
        self.assertAlmostEqual(result.atom_l1_gain, result.gain)
        self.assertAlmostEqual(
            result.gain, float(np.max(result.block_response_norms))
        )
        self.assertEqual(
            result.block_response_norms.shape,
            (
                2,
                3,
                1 + spec.depth_nodes + 1,
            ),
        )
        np.testing.assert_array_equal(
            result.block_response_norms[1, 0], 0.0
        )
        self.assertIn("not a full-state", result.scope)
        self.assertAlmostEqual(result.direction_norms[0], 1.0, places=13)
        self.assertAlmostEqual(result.direction_norms[1], 3.5, places=12)

        svd = flattened_response_svd(result)
        independently = np.linalg.svd(
            svd.weighted_response_matrix,
            compute_uv=False,
        )
        np.testing.assert_allclose(svd.singular_values, independently)
        self.assertAlmostEqual(svd.operator_norm, independently[0])
        self.assertIn("secondary", svd.scope)

    def test_group_l1_l2_gain_matches_blockwise_spectral_norm(self) -> None:
        spec = _spec()
        quadrature, state, first = _random_state_and_direction(spec, seed=121)
        _, _, raw_second = _random_state_and_direction(spec, seed=122)
        coefficient = weighted_tangent_inner_product(
            first, raw_second, quadrature
        )
        second = PDEState(
            B=raw_second.B - coefficient * first.B,
            a=raw_second.a - coefficient * first.a,
            c=raw_second.c - coefficient * first.c,
        )
        second = _scale(
            second,
            1.0 / float(weighted_tangent_norm(second, quadrature)),
        )
        result = residual_subspace_l1_to_linf_gain(
            state,
            (
                ResidualImpulse(0.0, first, "first"),
                ResidualImpulse(0.0, second, "second"),
            ),
            (0.0, 0.01, 0.02),
            max_step=0.01,
            spec=spec,
            quadrature=quadrature,
            observable_blocks=("f", "grams"),
        )
        flat = result.flattened_response_columns.reshape(
            result.observation_times.size,
            result.flattened_observable_dimension,
            2,
        )
        offsets = np.cumsum((0,) + result.block_sizes)
        expected = 0.0
        for time_index in range(result.observation_times.size):
            for block_index in range(len(result.block_sizes)):
                matrix = flat[
                    time_index,
                    offsets[block_index] : offsets[block_index + 1],
                    :,
                ]
                expected = max(
                    expected,
                    float(np.linalg.svd(matrix, compute_uv=False)[0]),
                )
        self.assertAlmostEqual(result.gain, expected, places=13)
        self.assertGreaterEqual(
            result.gain + 1e-14, result.atom_l1_gain
        )
        self.assertAlmostEqual(
            np.linalg.norm(result.maximizing_atom_coefficients),
            1.0,
            places=13,
        )

    def test_symmetric_nonlinear_impulses_converge_to_tangent(self) -> None:
        spec = _spec()
        quadrature, state, direction = _random_state_and_direction(spec)
        result = nonlinear_impulse_check(
            state,
            direction,
            (0.0, 0.01, 0.02),
            (4e-3, 2e-3, 1e-3),
            max_step=0.01,
            spec=spec,
            quadrature=quadrature,
            observable_blocks=("f", "grams"),
        )
        errors = [
            record.central_absolute_error for record in result.checks
        ]
        self.assertLess(errors[1], 0.3 * errors[0])
        self.assertLess(errors[2], 0.3 * errors[1])
        plus_errors = [
            record.plus_absolute_error for record in result.checks
        ]
        self.assertLess(plus_errors[-1], plus_errors[0])
        self.assertTrue(
            all(record.symmetry_defect >= 0.0 for record in result.checks)
        )

    def test_block_arclength_is_zero_for_a_frozen_state(self) -> None:
        spec = _spec()
        quadrature = build_quadrature(spec)
        state = initialize(spec, quadrature)
        current_f = observe(state, spec, quadrature).f
        frozen_spec = dataclasses.replace(spec, y=current_f)
        states = integrate_state_checkpoints(
            state,
            (0.0, 0.02, 0.05),
            max_step=0.01,
            spec=frozen_spec,
            quadrature=quadrature,
        )
        arc = block_state_arclength(
            states,
            (0.0, 0.02, 0.05),
            frozen_spec,
            quadrature,
        )
        np.testing.assert_array_equal(arc.B_speed, 0.0)
        np.testing.assert_array_equal(arc.a_speed, 0.0)
        np.testing.assert_array_equal(arc.c_speed, 0.0)
        np.testing.assert_array_equal(arc.total_speed, 0.0)
        self.assertEqual(arc.B, 0.0)
        self.assertEqual(arc.a, 0.0)
        self.assertEqual(arc.c, 0.0)
        self.assertEqual(arc.total, 0.0)

    def test_stage5_helper_returns_archive_ready_finite_arrays(self) -> None:
        template = _spec()
        family = build_nested_quadratures(
            template, levels=(2, 3), base_order=3
        )
        low_spec = family.spec(2)
        high_spec = family.spec(3)
        low_q = family.quadrature(2)
        high_q = family.quadrature(3)
        low_initial = initialize(low_spec, low_q)
        high_initial = initialize(high_spec, high_q)
        high_states = integrate_state_checkpoints(
            high_initial,
            (0.0, 0.01),
            max_step=0.01,
            spec=high_spec,
            quadrature=high_q,
        )
        result = stage5_serializable_result(
            low_initial,
            high_states,
            (0.0, 0.01),
            low_spec,
            high_spec,
            low_q,
            high_q,
            impulse_times=(0.0, 0.01),
            observation_times=(0.0, 0.01, 0.02),
            max_step=0.01,
            nonlinear_amplitudes=(1e-3,),
        )
        residuals = tuple(
            projected_back_residual(
                state,
                low_spec,
                high_spec,
                low_q,
                high_q,
            )
            for state in high_states
        )
        precomputed = stage5_serializable_result(
            low_initial,
            (),
            (0.0, 0.01),
            low_spec,
            high_spec,
            low_q,
            high_q,
            impulse_times=(0.0, 0.01),
            observation_times=(0.0, 0.01, 0.02),
            max_step=0.01,
            nonlinear_amplitudes=(1e-3,),
            precomputed_residuals=residuals,
        )
        compact = stage5_serializable_result(
            low_initial,
            (),
            (0.0, 0.01),
            low_spec,
            high_spec,
            low_q,
            high_q,
            impulse_times=(0.0, 0.01),
            observation_times=(0.0, 0.01, 0.02),
            max_step=0.01,
            nonlinear_amplitudes=(1e-3,),
            precomputed_residuals=residuals,
            serialize_residual_states=False,
        )
        self.assertEqual(set(result.arrays), set(precomputed.arrays))
        for key in result.arrays:
            np.testing.assert_array_equal(
                result.arrays[key], precomputed.arrays[key]
            )
        omitted = {
            "residual_snapshot_B",
            "residual_snapshot_a",
            "residual_snapshot_c",
            "residual_basis_B",
            "residual_basis_a",
            "residual_basis_c",
        }
        self.assertTrue(omitted.isdisjoint(compact.arrays))
        for key in set(result.arrays) - omitted:
            np.testing.assert_array_equal(
                result.arrays[key], compact.arrays[key]
            )
        self.assertTrue(result.arrays)
        self.assertTrue(
            all(
                isinstance(value, np.ndarray)
                and np.all(np.isfinite(value))
                for value in result.arrays.values()
            )
        )
        gram = result.arrays["residual_basis_weighted_gram"]
        np.testing.assert_allclose(gram, np.eye(gram.shape[0]), atol=5e-12)
        self.assertFalse(result.detail["full_state_gain_computed"])
        self.assertIn(
            "P3 states into P2",
            result.detail["residual_snapshot_source"],
        )
        self.assertIn(
            "P2/P3 quadrature",
            precomputed.detail["residual_snapshot_source"],
        )
        self.assertIn(
            "response-matrix spectral norm",
            result.detail["primary_gain_definition"],
        )
        self.assertIn("group-L1", result.detail["primary_gain_definition"])


if __name__ == "__main__":
    unittest.main()
