"""Frozen fixed-batch model and deterministic initialization utilities."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class B2State:
    """Historical name retained for compatibility; the batch size is dynamic."""

    first_preactivation: np.ndarray  # (n, B)
    middle_weight: np.ndarray  # raw iid N(0,1), (n, n)
    readout: np.ndarray  # (n,)

    @property
    def width(self) -> int:
        return int(self.readout.shape[0])


def validate_gram(gram: np.ndarray) -> np.ndarray:
    gram = np.asarray(gram, dtype=np.float64)
    if gram.ndim != 2 or gram.shape[0] < 1 or gram.shape[0] != gram.shape[1]:
        raise ValueError("the fixed-batch input Gram must be nonempty and square")
    if not np.allclose(gram, gram.T, atol=1.0e-13, rtol=0.0):
        raise ValueError("the input Gram must be symmetric")
    eigenvalues = np.linalg.eigvalsh(gram)
    tolerance = 1.0e-12 * max(1.0, float(np.max(np.abs(eigenvalues))))
    if float(np.min(eigenvalues)) < -tolerance:
        raise ValueError(f"the input Gram must be PSD, eigenvalues={eigenvalues}")
    return gram


def gram_root(gram: np.ndarray) -> np.ndarray:
    gram = validate_gram(gram)
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    return eigenvectors @ np.diag(np.sqrt(np.maximum(eigenvalues, 0.0)))


def sample_state(width: int, gram: np.ndarray, seed: int) -> B2State:
    """Draw one network; draw order is fixed for cross-route equality tests."""

    if width < 1:
        raise ValueError("width must be positive")
    root = gram_root(gram)
    rng = np.random.default_rng(seed)
    standard_first = rng.standard_normal((width, gram.shape[0]))
    first_preactivation = standard_first @ root.T
    middle_weight = rng.standard_normal((width, width))
    readout = rng.standard_normal(width)
    return B2State(first_preactivation, middle_weight, readout)


def validate_channel(channel: np.ndarray, batch: int | None = None) -> np.ndarray:
    channel = np.asarray(channel, dtype=np.float64)
    if channel.ndim != 1 or channel.shape[0] < 1:
        raise ValueError("the directional channel must be a nonempty vector")
    if batch is not None and channel.shape != (batch,):
        raise ValueError(f"the directional channel must have shape ({batch},)")
    return channel


def equal_channel() -> np.ndarray:
    """The unnormalized symmetric direction ``c_+=(1,1)``."""

    return np.asarray([1.0, 1.0])


def opposite_channel() -> np.ndarray:
    """The unnormalized antisymmetric direction ``c_-=(1,-1)``."""

    return np.asarray([1.0, -1.0])
