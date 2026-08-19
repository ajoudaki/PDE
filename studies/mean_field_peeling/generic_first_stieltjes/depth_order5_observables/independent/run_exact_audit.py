"""Run all post-freeze exact and seedwise audits for Route S."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

from ...depth.model import DepthState, sample_state
from .assemble_gamma04 import (
    compare_reduced_projection,
    compare_reference,
    exact_controls,
)
from .finite_width_hidden_jet import (
    coefficient_hidden_jet,
    derivative_hidden_jet,
    polynomial_oracle,
)
from .gamma04_contraction import local_audit


HERE = Path(__file__).resolve().parent


def _finite_width_gate() -> dict[str, object]:
    oracle = polynomial_oracle((1.0, -2.0, 1.0, 1.0, 0.2))
    maximum = 0.0
    cases = 0
    for depth in (1, 2, 3, 4):
        for width in (1, 2, 5):
            seed = 71_000 + 100 * depth + width
            state = sample_state(width, np.ones((1, 1)), depth, seed)
            coefficient = coefficient_hidden_jet(
                state, np.ones((1, 1)), np.ones(1), oracle
            )
            derivative = derivative_hidden_jet(
                state, np.ones((1, 1)), np.ones(1), oracle
            )
            for layer in range(depth):
                error = float(
                    np.max(
                        np.abs(
                            coefficient.derivatives[layer]
                            - derivative.derivatives[layer]
                        )
                    )
                )
                scale = float(
                    max(1.0, np.max(np.abs(coefficient.derivatives[layer])))
                )
                maximum = max(maximum, error / scale)
                cases += 1
    return {
        "cases": cases,
        "maximum_relative_or_absolute_scaled_error": maximum,
        "tolerance": 5e-11,
        "pass": maximum <= 5e-11,
    }


def _parity_gate() -> dict[str, object]:
    oracle = polynomial_oracle((0.3, -0.8, 0.2, 0.1, -0.03))
    state = sample_state(5, np.ones((1, 1)), 4, 72_019)
    reflected = DepthState(
        state.first_preactivation,
        state.hidden_weights,
        -state.readout,
    )
    positive = derivative_hidden_jet(
        state, np.ones((1, 1)), np.ones(1), oracle
    )
    negative = derivative_hidden_jet(
        reflected, np.ones((1, 1)), np.ones(1), oracle
    )
    maximum = 0.0
    for layer in range(4):
        expected = np.asarray(
            [(-1) ** order for order in range(5)], dtype=np.float64
        )[:, None, None] * positive.derivatives[layer]
        error = float(np.max(np.abs(negative.derivatives[layer] - expected)))
        scale = float(max(1.0, np.max(np.abs(expected))))
        maximum = max(maximum, error / scale)
    return {
        "readout_reflection_law": "X_l^(r)(R theta)=(-1)^r X_l^(r)(theta)",
        "maximum_scaled_error": maximum,
        "tolerance": 5e-11,
        "pass": maximum <= 5e-11,
    }


def _constant_seedwise_gate() -> dict[str, object]:
    oracle = polynomial_oracle((1.0,))
    state = sample_state(7, np.ones((1, 1)), 4, 72_021)
    jet = derivative_hidden_jet(state, np.ones((1, 1)), np.ones(1), oracle)
    maximum = max(
        float(np.max(np.abs(layer[1:]))) for layer in jet.derivatives
    )
    return {"maximum_nonzero_order_feature_derivative": maximum, "pass": maximum == 0.0}


def run() -> dict[str, object]:
    comparisons = {str(depth): compare_reference(depth) for depth in (2, 3, 4)}
    reduced = {
        str(depth): compare_reduced_projection(depth) for depth in (1, 2, 3, 4)
    }
    controls = exact_controls()
    finite_width = _finite_width_gate()
    parity = _parity_gate()
    constant_seedwise = _constant_seedwise_gate()
    pass_all = (
        all(value["total_discrepancies"] == 0 for value in comparisons.values())
        and all(value["total_discrepancies"] == 0 for value in reduced.values())
        and finite_width["pass"]
        and parity["pass"]
        and constant_seedwise["pass"]
        and local_audit()["maximum_activation_derivative"] <= 4
    )
    return {
        "route_s_freeze_sha256": hashlib.sha256(
            (HERE / "FROZEN_ROUTE_S_MANIFEST.json").read_bytes()
        ).hexdigest(),
        "local_contraction": local_audit(),
        "population_atomwise_comparisons": comparisons,
        "two_state_projection_comparisons": reduced,
        "finite_width_two_oracle_gate": finite_width,
        "readout_reflection_gate": parity,
        "constant_seedwise_gate": constant_seedwise,
        "exact_controls": controls,
        "decision": "pass" if pass_all else "fail",
        "claim_level": (
            "Exact finite-width differentiation gates and algebraically audited "
            "fixed-depth population normal forms; not yet the annealed theorem."
        ),
    }


if __name__ == "__main__":
    payload = run()
    path = HERE / "POST_FREEZE_EXACT_AUDIT.json"
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "decision": payload["decision"],
                "discrepancies": {
                    depth: value["total_discrepancies"]
                    for depth, value in payload["population_atomwise_comparisons"].items()
                },
                "finite_width": payload["finite_width_two_oracle_gate"],
                "parity": payload["readout_reflection_gate"],
            },
            indent=2,
            sort_keys=True,
        )
    )
