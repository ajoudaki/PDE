"""Closed activation registry shared by the PDE and dense reference.

All registered activations are smooth, odd, bounded, and normalized to
have derivative one at the origin.  Keeping each function and its exact
derivative in one immutable record prevents the forward and adjoint
implementations from silently selecting different nonlinearities.
"""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Callable, Mapping

import numpy as np
from scipy.special import erf

Array = np.ndarray
ArrayFunction = Callable[[Array], Array]


@dataclass(frozen=True)
class Activation:
    """An activation and its exact first derivative."""

    name: str
    value: ArrayFunction
    derivative: ArrayFunction

    def __call__(self, z: Array) -> Array:
        return self.value(z)


def _tanh(z: Array) -> Array:
    return np.tanh(z)


def _tanh_derivative(z: Array) -> Array:
    value = np.tanh(z)
    return 1.0 - value * value


def _erf(z: Array) -> Array:
    return erf(0.5 * np.sqrt(np.pi) * z)


def _erf_derivative(z: Array) -> Array:
    return np.exp(-0.25 * np.pi * z * z)


def _atan(z: Array) -> Array:
    return (2.0 / np.pi) * np.arctan(0.5 * np.pi * z)


def _atan_derivative(z: Array) -> Array:
    scaled = 0.5 * np.pi * z
    return 1.0 / (1.0 + scaled * scaled)


ACTIVATIONS: Mapping[str, Activation] = MappingProxyType(
    {
        "tanh": Activation("tanh", _tanh, _tanh_derivative),
        "erf": Activation("erf", _erf, _erf_derivative),
        "atan": Activation("atan", _atan, _atan_derivative),
    }
)
ACTIVATION_NAMES: tuple[str, ...] = tuple(ACTIVATIONS)


def get_activation(name: str) -> Activation:
    """Return a registered activation, rejecting aliases and unknown names."""

    try:
        return ACTIVATIONS[name]
    except (KeyError, TypeError) as exc:
        supported = ", ".join(ACTIVATION_NAMES)
        raise ValueError(
            f"unknown activation {name!r}; expected one of: {supported}"
        ) from exc


__all__ = [
    "ACTIVATIONS",
    "ACTIVATION_NAMES",
    "Activation",
    "get_activation",
]
