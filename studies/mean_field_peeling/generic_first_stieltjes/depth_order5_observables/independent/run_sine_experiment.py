"""Execute the preregistered 2,550-network normalized-sine Gamma04 panel."""

from __future__ import annotations

import hashlib
import json
from math import exp, sqrt
from pathlib import Path
import time

import numpy as np

from ...depth.model import DepthState
from .finite_width_hidden_jet import derivative_hidden_jet


HERE = Path(__file__).resolve().parent
RAW = HERE / "sine_raw"
ALLOCATIONS = {16: 1200, 32: 800, 64: 400, 128: 150}
SEED_ORIGIN = 88_000_000
PREDICTION_SHA256 = "18486522767f70596fa3f76058662fb4024e7c0c38fd0268005c1f77707aac27"
NORMALIZATION = sqrt((1.0 - exp(-2.0)) / 2.0)


def sine_derivative(order: int, value: np.ndarray) -> np.ndarray:
    phase = order % 4
    if phase == 0:
        result = np.sin(value)
    elif phase == 1:
        result = np.cos(value)
    elif phase == 2:
        result = -np.sin(value)
    else:
        result = -np.cos(value)
    return result / NORMALIZATION


def seed_for(cell: int, observation: int) -> int:
    return SEED_ORIGIN + 10_000 * cell + observation


def one_observation(width: int, seed: int) -> float:
    rng = np.random.default_rng(seed)
    state = DepthState(
        rng.standard_normal((width, 1)),
        (rng.standard_normal((width, width)),),
        rng.standard_normal(width),
    )
    jet = derivative_hidden_jet(
        state,
        np.ones((1, 1)),
        np.ones(1),
        sine_derivative,
        order=4,
    )
    return jet.gamma(2, 0, 4)


def collect(width: int, count: int, cell: int) -> np.ndarray:
    RAW.mkdir(exist_ok=True)
    path = RAW / f"gamma04_H2_n{width}.npy"
    if path.exists():
        values = list(np.asarray(np.load(path), dtype=np.float64))
        if len(values) > count:
            raise RuntimeError(f"checkpoint too long: {path}")
    else:
        values = []
    started = time.monotonic()
    for index in range(len(values), count):
        values.append(one_observation(width, seed_for(cell, index)))
        if (index + 1) % 100 == 0 or index + 1 == count:
            np.save(path, np.asarray(values, dtype=np.float64))
            print(
                f"n={width}: {index + 1}/{count}; mean={np.mean(values):.12g}; "
                f"segment={time.monotonic()-started:.1f}s",
                flush=True,
            )
    return np.asarray(values, dtype=np.float64)


def summarize(values: np.ndarray, width: int, cell: int) -> dict[str, object]:
    finite = bool(np.all(np.isfinite(values)))
    count = len(values)
    variance = float(np.var(values, ddof=1)) if count > 1 else float("nan")
    standard_error = sqrt(variance / count) if count else float("nan")
    valid = bool(
        finite
        and count == ALLOCATIONS[width]
        and np.isfinite(standard_error)
        and standard_error > 0
    )
    return {
        "width": width,
        "count": count,
        "expected_count": ALLOCATIONS[width],
        "finite": finite,
        "mean": float(np.mean(values)) if count else float("nan"),
        "sample_variance": variance,
        "standard_error": standard_error,
        "seed_first": seed_for(cell, 0),
        "seed_last": seed_for(cell, max(count - 1, 0)),
        "valid": valid,
    }


def fit(cells: list[dict[str, object]], prediction: float) -> dict[str, object]:
    if not all(bool(cell["valid"]) for cell in cells):
        return {"valid": False, "reason": "cell validity failure"}
    x = np.asarray([[1.0, 1.0 / int(cell["width"])] for cell in cells])
    y = np.asarray([float(cell["mean"]) for cell in cells])
    se = np.asarray([float(cell["standard_error"]) for cell in cells])
    precision = 1.0 / se**2
    normal = x.T @ (precision[:, None] * x)
    covariance = np.linalg.inv(normal)
    coefficients = covariance @ (x.T @ (precision * y))
    residual = y - x @ coefficients
    chi_square = float(np.sum((residual / se) ** 2))
    degrees_of_freedom = 2
    p_value = exp(-chi_square / 2.0)
    intercept_se = sqrt(float(covariance[0, 0]))
    z = (float(coefficients[0]) - prediction) / intercept_se
    return {
        "valid": bool(p_value >= 0.01 and np.isfinite(z)),
        "intercept": float(coefficients[0]),
        "slope": float(coefficients[1]),
        "intercept_standard_error": intercept_se,
        "population_prediction": prediction,
        "z": z,
        "chi_square": chi_square,
        "degrees_of_freedom": degrees_of_freedom,
        "chi_square_p_value": p_value,
        "residuals": [float(value) for value in residual],
    }


def main() -> None:
    exact = json.loads((HERE / "POST_FREEZE_EXACT_AUDIT.json").read_text())
    if exact["decision"] != "pass":
        raise RuntimeError("exact audit gate did not pass")
    prediction_path = HERE / "NORMALIZED_SINE_PREDICTION.json"
    digest = hashlib.sha256(prediction_path.read_bytes()).hexdigest()
    if digest != PREDICTION_SHA256:
        raise RuntimeError(f"prediction changed: {digest}")
    prediction_payload = json.loads(prediction_path.read_text())
    prediction = float(
        prediction_payload["orders"]["96"]["Gamma04_H2_layer2"]
    )

    cells: list[dict[str, object]] = []
    for cell, (width, count) in enumerate(ALLOCATIONS.items()):
        cells.append(summarize(collect(width, count, cell), width, cell))
    fitted = fit(cells, prediction)
    if fitted.get("valid") and abs(float(fitted["z"])) <= 3:
        decision = "pass"
    elif fitted.get("valid") and abs(float(fitted["z"])) > 5:
        decision = "fail"
    else:
        decision = "inconclusive"
    payload = {
        "contract": "NONPOLYNOMIAL_EXPERIMENT_CONTRACT.md",
        "prediction_sha256": digest,
        "activation": "sin(x)/sqrt((1-exp(-2))/2)",
        "hidden_depth": 2,
        "observed_layer": 2,
        "allocations": {str(key): value for key, value in ALLOCATIONS.items()},
        "total_networks": sum(ALLOCATIONS.values()),
        "cells": cells,
        "fit": fitted,
        "decision": decision,
        "claim_level": "empirical finite-width regression only",
    }
    path = HERE / "NORMALIZED_SINE_EXPERIMENT.json"
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"decision": decision, "fit": fitted}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
