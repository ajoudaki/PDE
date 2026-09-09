"""Seedwise gate between the two independently written finite-width jets."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ...depth.model import DepthState
from ..common.finite_width_jet import feature_ascent_jet
from .finite_jets import moving_flow_jet, normalized_sine_activation, random_parameters


HERE = Path(__file__).resolve().parent


def common_derivative(activation):
    def oracle(order: int, x: np.ndarray) -> np.ndarray:
        flat = np.asarray(x).reshape(-1)
        values = [activation.derivatives(float(value), order)[order] for value in flat]
        return np.asarray(values, dtype=np.float64).reshape(np.asarray(x).shape)

    return oracle


def main() -> None:
    activation = normalized_sine_activation()
    oracle = common_derivative(activation)
    records = []
    worst = 0.0
    for depth in (3, 4):
        for width in (1, 2, 5):
            for seed in (17001, 17002, 17003):
                parameters = random_parameters(depth, width, seed + 1000 * depth + 10 * width)
                hostile = np.asarray(
                    moving_flow_jet(parameters, activation, q0=1.0, order=5),
                    dtype=np.float64,
                )
                state = DepthState(
                    np.asarray(parameters.first, dtype=np.float64)[:, None],
                    tuple(np.asarray(matrix, dtype=np.float64) for matrix in parameters.matrices),
                    np.asarray(parameters.readout, dtype=np.float64),
                )
                neutral = feature_ascent_jet(
                    state,
                    np.ones((1, 1), dtype=np.float64),
                    np.ones(1, dtype=np.float64),
                    oracle,
                    order=5,
                ).derivatives
                scale = np.maximum(1.0, np.maximum(np.abs(hostile), np.abs(neutral)))
                discrepancy = float(np.max(np.abs(hostile - neutral) / scale))
                worst = max(worst, discrepancy)
                records.append(
                    {
                        "depth": depth,
                        "width": width,
                        "seed": seed + 1000 * depth + 10 * width,
                        "scaled_discrepancy": discrepancy,
                    }
                )
    payload = {
        "activation": "sin(x)/sqrt((1-exp(-2))/2)",
        "metric": "max_k |hostile_k-neutral_k|/max(1,|hostile_k|,|neutral_k|)",
        "threshold": 1e-10,
        "worst_scaled_discrepancy": worst,
        "pass": worst <= 1e-10,
        "records": records,
    }
    path = HERE / "TWO_ORACLE_GATE.json"
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: payload[key] for key in ("worst_scaled_discrepancy", "pass")}))
    if not payload["pass"]:
        raise SystemExit("two-oracle gate failed")


if __name__ == "__main__":
    main()
