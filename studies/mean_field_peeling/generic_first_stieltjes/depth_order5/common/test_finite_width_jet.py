"""Cross-checks for the neutral arbitrary-depth finite-width oracle."""

from __future__ import annotations

import numpy as np

from ...depth.model import sample_state
from ...order5.finite_width.feature_flow import (
    InitialState,
    feature_flow_jet as h2_feature_flow_jet,
)
from .finite_width_jet import feature_ascent_jet


def _polynomial_oracle(coefficients):
    coefficients = np.asarray(coefficients, dtype=np.float64)

    def oracle(order: int, value: np.ndarray) -> np.ndarray:
        current = coefficients.copy()
        for _ in range(order):
            current = np.arange(1, current.size) * current[1:]
        if current.size == 0:
            return np.zeros_like(value)
        answer = np.zeros_like(value, dtype=np.float64)
        for coefficient in current[::-1]:
            answer = answer * value + coefficient
        return answer

    return oracle


def test_h2_is_seedwise_identical_to_accepted_order_five_oracle() -> None:
    oracle = _polynomial_oracle((1, -2, 1, 1))
    for q0 in (0.4, 1.0, 2.3):
        for width in (1, 3, 7):
            for seed in (0, 5):
                state = sample_state(width, np.asarray([[q0]]), 2, seed)
                current = feature_ascent_jet(
                    state,
                    np.asarray([[q0]]),
                    np.asarray([1.0]),
                    oracle,
                ).derivatives
                accepted = h2_feature_flow_jet(
                    InitialState(
                        first_standard=state.first_preactivation[:, 0]
                        / np.sqrt(q0),
                        middle_raw=state.hidden_weights[0],
                        readout=state.readout,
                    ),
                    q0,
                    oracle,
                ).derivatives
                np.testing.assert_allclose(
                    current, accepted, rtol=2e-12, atol=2e-12
                )


def test_readout_sign_parity_at_arbitrary_depth() -> None:
    oracle = _polynomial_oracle((0, 1, 1))
    for hidden_layers in (1, 2, 3, 4):
        state = sample_state(4, np.asarray([[1.0]]), hidden_layers, 19)
        flipped = type(state)(
            state.first_preactivation,
            state.hidden_weights,
            -state.readout,
        )
        positive = feature_ascent_jet(
            state, np.asarray([[1.0]]), np.asarray([1.0]), oracle
        ).derivatives
        negative = feature_ascent_jet(
            flipped, np.asarray([[1.0]]), np.asarray([1.0]), oracle
        ).derivatives
        expected = np.asarray(
            [(-1) ** (order + 1) for order in range(6)],
            dtype=np.float64,
        )
        np.testing.assert_allclose(
            negative, expected * positive, rtol=3e-12, atol=3e-12
        )


def run_checks() -> None:
    tests = (
        test_h2_is_seedwise_identical_to_accepted_order_five_oracle,
        test_readout_sign_parity_at_arbitrary_depth,
    )
    for test in tests:
        test()
        print(f"PASS {test.__name__}")


if __name__ == "__main__":
    run_checks()
