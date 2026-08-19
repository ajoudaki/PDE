"""Seedwise gates for the arbitrary-depth finite-width Taylor compiler."""

from __future__ import annotations

from math import sqrt

import numpy as np

from ..b2.finite_width_jet import directional_feature_jet
from ..b2.model import B2State, gram_root, sample_state as sample_b2_state
from .finite_width_jet import feature_ascent_jet
from .model import DepthState, sample_state
from .raw_coordinate_jet_audit import raw_coordinate_derivatives


def polynomial_oracle(coefficients):
    coefficients = tuple(float(value) for value in coefficients)

    def derivative(order, x):
        values = list(coefficients)
        for _ in range(order):
            values = [k * values[k] for k in range(1, len(values))]
        out = np.zeros_like(x, dtype=np.float64)
        for coefficient in reversed(values):
            out = out * x + coefficient
        return out

    return derivative


def sine_derivative(order, x):
    return (np.sin(x), np.cos(x), -np.sin(x), -np.cos(x))[order % 4]


def tanh_derivative(order, x):
    t = np.tanh(x)
    return (
        t,
        1.0 - t * t,
        -2.0 * t * (1.0 - t * t),
        -2.0 * (1.0 - t * t) * (1.0 - 3.0 * t * t),
    )[order]


LINEAR = polynomial_oracle([0.0, 1.0])
AFFINE = polynomial_oracle([0.7, 1.0])
QUADRATIC = polynomial_oracle([0.0, 0.0, 1.0])
CUBIC = polynomial_oracle([0.0, 0.0, 0.0, 1.0])


def test_h2_is_seedwise_identical_to_existing_fixed_batch_compiler() -> None:
    """The depth recursion must specialize exactly to the accepted H=2 code."""

    cases = (
        (
            np.asarray([[1.0, 0.25], [0.25, 0.8]]),
            np.asarray([0.4, -1.3]),
        ),
        (
            np.asarray([[1.0, -1.0], [-1.0, 1.0]]),
            np.asarray([1.0, 0.3]),
        ),
        (
            np.asarray([[1.0, 0.2], [-0.4, 0.8], [0.3, -0.7]])
            @ np.asarray([[1.0, -0.4, 0.3], [0.2, 0.8, -0.7]]),
            np.asarray([0.2, -0.8, 0.5]),
        ),
    )

    activations = (LINEAR, AFFINE, QUADRATIC, CUBIC, sine_derivative, tanh_derivative)
    for case_index, (gram, channel) in enumerate(cases):
        for activation_index, oracle in enumerate(activations):
            for width, seed in ((1, 0), (3, 7), (6, 19)):
                old_state = sample_b2_state(width, gram, seed)
                new_state = sample_state(width, gram, 2, seed)
                np.testing.assert_array_equal(
                    new_state.first_preactivation, old_state.first_preactivation
                )
                np.testing.assert_array_equal(
                    new_state.hidden_weights[0], old_state.middle_weight
                )
                np.testing.assert_array_equal(new_state.readout, old_state.readout)
                old = directional_feature_jet(
                    old_state, gram, channel, oracle
                ).ordinary_coefficients
                new = feature_ascent_jet(
                    new_state, gram, channel, oracle
                ).ordinary_coefficients
                np.testing.assert_allclose(
                    new,
                    old,
                    rtol=2.0e-13,
                    atol=2.0e-11,
                    err_msg=(
                        f"case={case_index}, activation={activation_index}, "
                        f"width={width}, seed={seed}"
                    ),
                )


def test_independent_raw_coordinate_jets_at_depths_one_two_three() -> None:
    """A full derivative tensor checks the moving-field ODE through order 3."""

    cases = (
        (
            1,
            np.asarray([[0.8]]),
            np.asarray([1.2]),
            (tanh_derivative,),
        ),
        (
            2,
            np.asarray([[1.0, -1.0], [-1.0, 1.0]]),
            np.asarray([0.4, -0.9]),
            (sine_derivative, AFFINE),
        ),
        (
            3,
            np.asarray(
                [[1.0, 0.3, -0.4], [0.3, 0.58, 0.26], [-0.4, 0.26, 0.52]]
            ),
            np.asarray([0.25, -0.7, 1.1]),
            (QUADRATIC, tanh_derivative, sine_derivative),
        ),
    )
    rng = np.random.default_rng(73019)
    saw_moving_field_difference = False
    for hidden_layers, gram, channel, oracles in cases:
        # Exact factorization: X.T X / d0 = Q, including singular Q.
        input_dimension = gram.shape[0]
        inputs = sqrt(input_dimension) * gram_root(gram).T
        first_weight = rng.standard_normal((1, input_dimension))
        hidden_weights = tuple(
            rng.standard_normal((1, 1)) for _ in range(hidden_layers - 1)
        )
        readout = rng.standard_normal(1)
        raw, state, recovered_gram, frozen_third = raw_coordinate_derivatives(
            first_weight,
            hidden_weights,
            readout,
            inputs,
            channel,
            oracles,
        )
        compiled = feature_ascent_jet(
            state, recovered_gram, channel, oracles
        ).derivatives
        np.testing.assert_allclose(
            compiled,
            raw,
            rtol=3.0e-11,
            atol=3.0e-10,
            err_msg=f"independent raw-coordinate mismatch at H={hidden_layers}",
        )
        if not np.isclose(raw[3], frozen_third, rtol=1.0e-7, atol=1.0e-9):
            saw_moving_field_difference = True
    assert saw_moving_field_difference, "the audit cases must distinguish a frozen line"


def test_arbitrary_batch_depth_singular_gram_and_layerwise_activations() -> None:
    """The executable recursion has no H=2, B=2, or invertibility branch."""

    feature_rows = np.asarray(
        [[1.0, 0.2], [-0.4, 0.7], [0.3, -1.1], [0.9, 0.5]]
    )
    gram = feature_rows @ feature_rows.T  # B=4, rank two.
    channel = np.asarray([0.4, -0.7, 0.2, 1.1])
    state = sample_state(4, gram, 5, 991)
    oracles = (sine_derivative, AFFINE, tanh_derivative, QUADRATIC, CUBIC)
    base = feature_ascent_jet(state, gram, channel, oracles).derivatives
    assert np.all(np.isfinite(base))

    # Since g_{lambda c}=lambda g_c and its vector field scales by lambda,
    # D_{lambda c}^k g_{lambda c}=lambda^(k+1) D_c^k g_c.
    for scale in (-1.3, 0.2, 1.7):
        scaled = feature_ascent_jet(
            state, gram, scale * channel, oracles
        ).derivatives
        expected = np.asarray(
            [scale ** (degree + 1) * value for degree, value in enumerate(base)]
        )
        np.testing.assert_allclose(scaled, expected, rtol=2.0e-11, atol=2.0e-8)

    zero = feature_ascent_jet(
        state, gram, np.zeros_like(channel), oracles
    ).derivatives
    np.testing.assert_array_equal(zero, np.zeros(4))


def test_one_hidden_layer_accepts_arbitrary_batch() -> None:
    gram = np.asarray(
        [[0.7, 0.1, -0.2], [0.1, 1.1, 0.3], [-0.2, 0.3, 0.9]]
    )
    channel = np.asarray([0.3, -0.5, 0.8])
    state = sample_state(7, gram, 1, 123)
    result = feature_ascent_jet(state, gram, channel, sine_derivative)
    assert result.hidden_layers == 1
    assert result.batch == 3
    assert result.width == 7
    assert np.all(np.isfinite(result.derivatives))


def test_depth_state_can_be_constructed_from_existing_h2_state() -> None:
    gram = np.asarray([[1.0, 0.2], [0.2, 0.6]])
    channel = np.asarray([1.0, -0.4])
    old = sample_b2_state(3, gram, 17)
    converted = DepthState(
        old.first_preactivation, (old.middle_weight,), old.readout
    )
    existing = directional_feature_jet(old, gram, channel, tanh_derivative)
    generalized = feature_ascent_jet(converted, gram, channel, tanh_derivative)
    np.testing.assert_allclose(
        generalized.derivatives, existing.derivatives, rtol=1.0e-13, atol=1.0e-12
    )
