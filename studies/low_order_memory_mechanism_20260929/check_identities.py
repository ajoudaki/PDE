"""Deterministic algebra checks; no network training or empirical claim."""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import numpy as np
from numpy.polynomial import legendre, polynomial


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    rng = np.random.default_rng(29092026)
    points, weights = legendre.leggauss(64)
    u, weights = (points + 1) / 2, weights / 2
    tau = 2.7
    coefficients = rng.normal(size=(6, 5))

    def evaluate(x: np.ndarray, degree: int = 0) -> np.ndarray:
        return np.stack([
            polynomial.polyval(x, polynomial.polyder(c, m=degree))
            for c in coefficients.T
        ], axis=-1)

    values = evaluate(tau * u)
    now = evaluate(np.array(tau))
    errors: dict[str, float] = {}
    for q in range(1, 7):
        modes = np.stack([
            legendre.legval(2 * u - 1, np.eye(q)[k]) for k in range(q)
        ])
        mu = (modes * weights) @ values
        moments = tau * mu
        derivative_integral = (modes * weights) @ (
            values + (tau * u)[:, None] * evaluate(tau * u, 1)
        )
        d = 2 * np.arange(q) + 1
        damping = np.zeros_like(moments)
        for k in range(q):
            damping[k] = k * moments[k] + np.sum(
                d[:k, None] * moments[:k], axis=0
            )
        raw_rhs = now - damping / tau
        errors[f"q{q}_moment_integral_derivative"] = float(
            np.max(np.abs(derivative_integral - raw_rhs))
        )

        for k in range(q):
            import math
            derivative_moment = tau**k / math.factorial(k) * np.sum(
                (weights * (u * (1 - u))**k)[:, None] * evaluate(tau * u, k),
                axis=0,
            )
            errors[f"q{q}_mode{k}_weighted_derivative"] = float(
                np.max(np.abs(mu[k] - derivative_moment))
            )

        # Quotient differentiation independently verifies the log-clock filter.
        log_rhs = raw_rhs - mu
        triangular_rhs = now - mu - damping / tau
        errors[f"q{q}_log_filter"] = float(np.max(np.abs(log_rhs - triangular_rhs)))
        for k in range(1, q):
            errors[f"q{q}_mode{k}_consecutive_filter"] = float(np.max(np.abs(
                log_rhs[k] + (k + 1) * mu[k]
                - log_rhs[k - 1] + (k - 1) * mu[k - 1]
            )))

        v = np.sqrt(d)
        matrix = -np.tril(np.outer(v, v), -1) - np.diag(np.arange(q) + 0.5)
        errors[f"q{q}_passive_matrix"] = float(np.max(np.abs(
            matrix + matrix.T + np.outer(v, v)
        )))
        z = rng.normal(size=(q, 5))
        source = rng.normal(size=5)
        zdot = matrix @ z / tau + v[:, None] * source / np.sqrt(tau)
        endpoint = v @ z / np.sqrt(tau)
        errors[f"q{q}_energy_identity"] = float(abs(
            2 * np.sum(z * zdot)
            - np.sum(source**2) + np.sum((source - endpoint)**2)
        ))

        # A second independent identity: direct differentiation of paired moments.
        B = rng.normal(size=(q, 4))
        C = rng.normal(size=(q, 3))
        h = rng.normal(size=4)
        b = rng.normal(size=3)
        Bdot, Cdot = np.empty_like(B), np.empty_like(C)
        for k in range(q):
            Bdot[k] = h - (k * B[k] + np.sum(d[:k, None] * B[:k], axis=0)) / tau
            Cdot[k] = b - (k * C[k] + np.sum(d[:k, None] * C[:k], axis=0)) / tau
        paired = (C.T * d) @ B / tau
        paired_dot = ((Cdot.T * d) @ B + (C.T * d) @ Bdot) / tau - paired / tau
        hstar, bstar = d @ B / tau, d @ C / tau
        exact = np.outer(b, h) - np.outer(b - bstar, h - hstar)
        errors[f"q{q}_paired_velocity"] = float(np.max(np.abs(paired_dot - exact)))

    tolerance = 1e-9
    result = {
        "scope": "Deterministic identities only; no network trajectories or fitting experiment",
        "seed": 29092026,
        "python": platform.python_version(),
        "numpy": np.__version__,
        "tolerance": tolerance,
        "maximum_absolute_error": max(errors.values()),
        "checks": errors,
        "passed": all(x < tolerance for x in errors.values()),
        "source_sha256": {
            name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in ["check_identities.py", "MODEL.md", "PROJECTION_MECHANISM.md"]
        },
    }
    (args.output / "checks.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ["passed", "maximum_absolute_error", "scope"]}))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
