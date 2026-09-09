"""Exact seedwise audit of the B=2 directional Tensor Program."""

from __future__ import annotations

import numpy as np

from .finite_width_directional import (
    directional_third_contraction,
    frozen_mse_responses,
)
from .finite_width_jet import directional_feature_jet
from .model import B2State, equal_channel, opposite_channel, sample_state
from ..compiler.finite_width_contraction import third_derivative_contraction


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


ACTIVATIONS = {
    "linear": polynomial_oracle([0.0, 1.0]),
    "affine": polynomial_oracle([1.0, 1.0]),
    "quadratic": polynomial_oracle([0.0, 0.0, 1.0]),
    "cubic": polynomial_oracle([0.0, 0.0, 0.0, 1.0]),
    "sin": sine_derivative,
    "tanh": tanh_derivative,
}


GRAMS = (
    np.asarray([[1.0, 0.35], [0.35, 1.4]]),
    np.asarray([[0.7, 0.0], [0.0, 1.2]]),
    np.asarray([[1.0, -1.0], [-1.0, 1.0]]),
)


CHANNELS = (
    equal_channel(),
    opposite_channel(),
    np.asarray([0.25, -1.3]),
)


def test_direct_tensor_program_matches_independent_taylor_jet() -> None:
    for activation_name, oracle in ACTIVATIONS.items():
        for gram_index, gram in enumerate(GRAMS):
            for channel_name, channel in (
                ("equal", equal_channel()),
                ("opposite", opposite_channel()),
                ("generic", np.asarray([0.25, -1.3])),
            ):
                for width, seed in ((1, 0), (3, 7), (6, 19)):
                    state = sample_state(width, gram, seed)
                    direct = directional_third_contraction(
                        state, gram, channel, oracle
                    ).value
                    jet = directional_feature_jet(
                        state, gram, channel, oracle
                    ).derivatives[3]
                    np.testing.assert_allclose(
                        direct,
                        jet,
                        rtol=3.0e-12,
                        atol=3.0e-9,
                        err_msg=(
                            f"activation={activation_name}, gram={gram_index}, "
                            f"channel={channel_name}, width={width}, seed={seed}"
                        ),
                    )


def test_channel_homogeneity_and_named_specializations() -> None:
    gram = np.asarray([[1.0, -0.2], [-0.2, 0.8]])
    state = sample_state(5, gram, 23)
    oracle = tanh_derivative

    plus = directional_third_contraction(
        state, gram, equal_channel(), oracle
    ).value
    minus = directional_third_contraction(
        state, gram, opposite_channel(), oracle
    ).value
    # These are genuinely distinct channels on a generic two-sample state.
    assert not np.isclose(plus, minus, rtol=1.0e-8, atol=1.0e-10)

    base_channel = np.asarray([0.4, -0.9])
    base = directional_third_contraction(state, gram, base_channel, oracle).value
    for scale in (-1.7, 0.25, 2.0):
        scaled = directional_third_contraction(
            state, gram, scale * base_channel, oracle
        ).value
        np.testing.assert_allclose(
            scaled, scale**4 * base, rtol=3.0e-12, atol=3.0e-10
        )


def test_zero_channel_has_zero_directional_jet() -> None:
    gram = GRAMS[0]
    state = sample_state(4, gram, 5)
    zero = np.zeros(2)
    direct = directional_third_contraction(
        state, gram, zero, sine_derivative
    ).value
    jet = directional_feature_jet(
        state, gram, zero, sine_derivative
    ).derivatives
    assert direct == 0.0
    assert np.allclose(jet[1:], 0.0, atol=0.0, rtol=0.0)


def test_frozen_mse_response_scalars_and_readout_parity() -> None:
    """Audit the two extra arbitrary-label loss-response observables."""

    gram = np.asarray([[1.0, 0.31], [0.31, 0.8]])
    channel = np.asarray([0.37, -0.91])
    state = sample_state(5, gram, 1701)
    oracle = ACTIVATIONS["cubic"]
    response = frozen_mse_responses(state, gram, channel, oracle)

    # k.c=D_c g_c and c.(h+q)=D_c^2 g_c.  The right sides come from the
    # independently maintained feature-ODE power-series oracle.
    jet = directional_feature_jet(
        state, gram, channel, oracle, order=2
    ).derivatives
    np.testing.assert_allclose(
        channel @ response.kernel_direction,
        jet[1],
        rtol=4.0e-12,
        atol=4.0e-9,
    )
    np.testing.assert_allclose(
        channel @ (response.straight_hessian + response.gradient_response),
        jet[2],
        rtol=4.0e-12,
        atol=4.0e-9,
    )

    # The complete finite-width scalar, rather than a one-copy integrand,
    # is odd under the global centered-readout involution.
    flipped = B2State(
        state.first_preactivation,
        state.middle_weight,
        -state.readout,
    )
    odd = frozen_mse_responses(flipped, gram, channel, oracle)
    np.testing.assert_allclose(
        odd.kernel_direction,
        response.kernel_direction,
        rtol=4.0e-12,
        atol=4.0e-9,
    )
    np.testing.assert_allclose(
        odd.straight_hessian,
        -response.straight_hessian,
        rtol=4.0e-12,
        atol=4.0e-9,
    )
    np.testing.assert_allclose(
        odd.gradient_response,
        -response.gradient_response,
        rtol=4.0e-12,
        atol=4.0e-9,
    )
    np.testing.assert_allclose(
        (odd.metric_response, odd.output_response),
        (-response.metric_response, -response.output_response),
        rtol=4.0e-12,
        atol=4.0e-9,
    )
    assert max(abs(response.metric_response), abs(response.output_response)) > 1e-8


def test_three_sample_program_matches_independent_taylor_jet() -> None:
    """The same equations extend literally from B=2 to arbitrary fixed B."""

    gram = np.asarray(
        [[1.0, 0.2, -0.1], [0.2, 0.8, 0.25], [-0.1, 0.25, 1.3]]
    )
    channel = np.asarray([0.4, -0.7, 0.2])
    for activation_name in ("linear", "quadratic", "sin", "tanh"):
        oracle = ACTIVATIONS[activation_name]
        for width, seed in ((1, 31), (4, 37), (7, 41)):
            state = sample_state(width, gram, seed)
            direct = directional_third_contraction(
                state, gram, channel, oracle
            ).value
            jet = directional_feature_jet(
                state, gram, channel, oracle
            ).derivatives[3]
            np.testing.assert_allclose(
                direct,
                jet,
                rtol=4.0e-12,
                atol=4.0e-9,
                err_msg=(
                    f"B=3 activation={activation_name}, width={width}, seed={seed}"
                ),
            )


def test_linear_channel_is_exact_effective_single_input() -> None:
    """For phi(x)=x, c.T f is the same network evaluated at X c."""

    oracle = ACTIVATIONS["linear"]
    for gram, channel, width, seed in (
        (GRAMS[0], np.asarray([0.25, -1.3]), 3, 41),
        (GRAMS[1], equal_channel(), 6, 43),
        (GRAMS[2], opposite_channel(), 4, 47),
    ):
        state = sample_state(width, gram, seed)
        q_effective = float(channel @ gram @ channel)
        effective_u = state.first_preactivation @ channel
        effective_state = B2State(
            np.column_stack((effective_u, np.zeros(width))),
            state.middle_weight,
            state.readout,
        )
        effective_gram = np.asarray([[q_effective, 0.0], [0.0, 0.0]])
        direct = directional_third_contraction(
            state, gram, channel, oracle
        )
        reduced = directional_third_contraction(
            effective_state,
            effective_gram,
            np.asarray([1.0, 0.0]),
            oracle,
        )
        np.testing.assert_allclose(
            (
                direct.straight_line,
                direct.hessian_readout,
                direct.hessian_middle,
                direct.hessian_first,
            ),
            (
                reduced.straight_line,
                reduced.hessian_readout,
                reduced.hessian_middle,
                reduced.hessian_first,
            ),
            rtol=3.0e-12,
            atol=3.0e-10,
        )


def test_single_active_sample_reduces_exactly_to_b1_program() -> None:
    """No inactive-sample or off-diagonal-Gram factor may leak into c=(1,0)."""

    for activation_name in ("linear", "quadratic", "sin", "tanh"):
        oracle = ACTIVATIONS[activation_name]
        for width, seed, q0 in ((1, 2, 0.4), (4, 13, 1.0), (7, 29, 1.8)):
            # Reproduce the B=1 draw order exactly for the active coordinates.
            rng = np.random.default_rng(seed)
            active_u = np.sqrt(q0) * rng.standard_normal(width)
            middle_weight = rng.standard_normal((width, width))
            readout = rng.standard_normal(width)
            b1_value = third_derivative_contraction(
                width, q0, oracle, seed
            ).value
            standard_inactive = np.random.default_rng(
                seed + 100_003
            ).standard_normal(width)
            for rho in (0.0, 0.35 * np.sqrt(q0)):
                inactive_variance = 1.0
                inactive_u = (
                    (rho / q0) * active_u
                    + np.sqrt(inactive_variance - rho**2 / q0)
                    * standard_inactive
                )
                state = B2State(
                    np.column_stack((active_u, inactive_u)),
                    middle_weight,
                    readout,
                )
                gram = np.asarray(
                    [[q0, rho], [rho, inactive_variance]]
                )
                b2_value = directional_third_contraction(
                    state, gram, np.asarray([1.0, 0.0]), oracle
                ).value
                np.testing.assert_allclose(
                    b2_value,
                    b1_value,
                    rtol=3.0e-12,
                    atol=3.0e-9,
                    err_msg=(
                        f"B=1 reduction failed for {activation_name}, "
                        f"width={width}, q0={q0}, rho={rho}"
                    ),
                )
