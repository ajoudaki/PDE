"""Immutable case loading and provenance for the PDE generalization study."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path

import numpy as np

Array = np.ndarray


@dataclass(frozen=True)
class StudyCase:
    case_id: str
    family: str
    scope: str
    description: str
    X: Array
    y: Array
    activation: str
    sigma_w: float
    A: float
    gamma: float
    case_sha256: str
    registry_sha256: str


def _canonical_json(value: object) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def load_case(registry_path: str | Path, case_id: str) -> StudyCase:
    path = Path(registry_path)
    raw_bytes = path.read_bytes()
    registry = json.loads(raw_bytes)
    cases = registry.get("cases", {})
    if case_id not in cases:
        raise KeyError(f"unknown case_id {case_id!r}")
    record = cases[case_id]
    payload = {
        "case_id": case_id,
        "X": record["X"],
        "y": record["y"],
        "activation": record["activation"],
        "sigma_w": record["sigma_w"],
        "A": record["A"],
        "gamma": record["gamma"],
    }
    X = np.asarray(record["X"], dtype=float)
    y = np.asarray(record["y"], dtype=float)
    if X.ndim != 2 or y.ndim != 1 or X.shape[1] != y.size:
        raise ValueError(f"invalid X/y shapes for {case_id}")
    if X.shape[0] != 3:
        raise ValueError("the fixed-P=5 study requires ambient dimension d=3")
    if not (2 <= y.size <= 5):
        raise ValueError("registered sample count must be between 2 and 5")
    if not np.all(np.isfinite(X)) or not np.all(np.isfinite(y)):
        raise ValueError("registered X/y must be finite")
    if np.max(np.abs(np.linalg.norm(X, axis=0) - 1.0)) > 2e-14:
        raise ValueError("all registered input columns must have unit norm")
    if record["activation"] not in {"tanh", "erf", "atan"}:
        raise ValueError(
            "study cases use only tanh, normalized erf, or normalized atan"
        )
    for key in ("sigma_w", "A", "gamma"):
        if not np.isfinite(record[key]) or record[key] <= 0:
            raise ValueError(f"{key} must be finite and positive")
    return StudyCase(
        case_id=case_id,
        family=record["family"],
        scope=record["scope"],
        description=record["description"],
        X=X,
        y=y,
        activation=record["activation"],
        sigma_w=float(record["sigma_w"]),
        A=float(record["A"]),
        gamma=float(record["gamma"]),
        case_sha256=hashlib.sha256(
            _canonical_json(payload).encode()
        ).hexdigest(),
        registry_sha256=hashlib.sha256(raw_bytes).hexdigest(),
    )


def case_metadata(case: StudyCase) -> dict:
    return {
        "case_id": case.case_id,
        "case_family": case.family,
        "case_scope": case.scope,
        "case_description": case.description,
        "case_sha256": case.case_sha256,
        "registry_sha256": case.registry_sha256,
        "X": case.X.tolist(),
        "y": case.y.tolist(),
        "m": int(case.y.size),
        "d": int(case.X.shape[0]),
        "activation": case.activation,
        "sigma_w": case.sigma_w,
        "A": case.A,
        "gamma": case.gamma,
    }
