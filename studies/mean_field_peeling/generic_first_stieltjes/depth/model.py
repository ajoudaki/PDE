"""Finite-width state and validation helpers for arbitrary fixed depth."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

from ..b2.model import gram_root, validate_channel, validate_gram


@dataclass(frozen=True)
class DepthState:
    """Raw parameters after scalarizing the first layer by its batch Gram.

    ``first_preactivation`` is ``z^1`` and has shape ``(n, B)``.  The tuple
    ``hidden_weights`` contains raw matrices ``W^2,...,W^H`` (without their
    ``1/sqrt(n)`` forward factors).  Thus its length is ``H-1``.  An empty
    tuple is the one-hidden-layer case ``H=1``.
    """

    first_preactivation: np.ndarray
    hidden_weights: tuple[np.ndarray, ...]
    readout: np.ndarray

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "first_preactivation",
            np.asarray(self.first_preactivation, dtype=np.float64),
        )
        object.__setattr__(
            self,
            "hidden_weights",
            tuple(np.asarray(weight, dtype=np.float64) for weight in self.hidden_weights),
        )
        object.__setattr__(self, "readout", np.asarray(self.readout, dtype=np.float64))

    @property
    def width(self) -> int:
        if self.readout.ndim != 1:
            raise ValueError("the readout must be a vector")
        return int(self.readout.shape[0])

    @property
    def hidden_layers(self) -> int:
        return len(self.hidden_weights) + 1

    @property
    def batch(self) -> int:
        if self.first_preactivation.ndim != 2:
            raise ValueError("the first preactivation must be a matrix")
        return int(self.first_preactivation.shape[1])

    def validate(self, batch: int | None = None) -> "DepthState":
        n = self.width
        if n < 1:
            raise ValueError("the width must be positive")
        if self.first_preactivation.ndim != 2:
            raise ValueError("the first preactivation must be a matrix")
        if self.first_preactivation.shape[0] != n:
            raise ValueError("the first-preactivation width disagrees with the readout")
        if batch is not None and self.first_preactivation.shape[1] != batch:
            raise ValueError(
                "the first-preactivation batch dimension disagrees with the Gram"
            )
        for layer, weight in enumerate(self.hidden_weights, start=2):
            if weight.shape != (n, n):
                raise ValueError(f"W^{layer} must have shape ({n}, {n})")
        return self


def sample_state(
    width: int,
    input_gram: np.ndarray,
    hidden_layers: int,
    seed: int,
) -> DepthState:
    """Draw a Gaussian state with a fixed, cross-audit-compatible draw order.

    For ``H=2`` the draw order is exactly the one in ``b2.model.sample_state``:
    first-preactivation standard normals, ``W^2``, then the readout.
    """

    if width < 1:
        raise ValueError("the width must be positive")
    if hidden_layers < 1:
        raise ValueError("the number of hidden layers H must be positive")
    gram = validate_gram(input_gram)
    root = gram_root(gram)
    rng = np.random.default_rng(seed)
    first_preactivation = rng.standard_normal((width, gram.shape[0])) @ root.T
    hidden_weights = tuple(
        rng.standard_normal((width, width)) for _ in range(hidden_layers - 1)
    )
    readout = rng.standard_normal(width)
    return DepthState(first_preactivation, hidden_weights, readout).validate(
        gram.shape[0]
    )


def validate_problem(
    state: DepthState,
    input_gram: np.ndarray,
    channel: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    gram = validate_gram(input_gram)
    state.validate(gram.shape[0])
    return gram, validate_channel(channel, gram.shape[0])


def as_oracle_tuple(activation_derivative, hidden_layers: int) -> tuple:
    """Normalize one shared oracle or a per-layer oracle sequence."""

    if callable(activation_derivative):
        return (activation_derivative,) * hidden_layers
    if not isinstance(activation_derivative, Sequence):
        raise TypeError("activation_derivative must be callable or a sequence")
    result = tuple(activation_derivative)
    if len(result) != hidden_layers:
        raise ValueError(
            f"expected {hidden_layers} activation oracles, received {len(result)}"
        )
    if not all(callable(oracle) for oracle in result):
        raise TypeError("every activation oracle must be callable")
    return result
