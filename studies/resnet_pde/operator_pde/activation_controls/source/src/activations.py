"""Closed activation registry shared by the PDE and dense reference.

The original tanh/erf/atan registry is extended only for the preregistered
activation-linearity falsification experiment.  The continuation family is

    phi_c(z) = tanh(c z) / c,  c > 0,       phi_0(z) = z.

A fixed linear control uses the initialization-Gaussian first-Hermite
coefficient of ``phi_c`` at preactivation standard deviation ``sigma_w=.65``.
Keeping values and exact derivatives in one immutable record prevents the
forward and adjoint implementations from silently selecting different laws.
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


def _identity(z: Array) -> Array:
    return z


def _identity_derivative(z: Array) -> Array:
    return np.ones_like(z)


def _tanh_c2(z: Array) -> Array:
    return np.tanh(2.0 * z) / 2.0


def _tanh_c2_derivative(z: Array) -> Array:
    value = np.tanh(2.0 * z)
    return 1.0 - value * value


def _tanh_c4(z: Array) -> Array:
    return np.tanh(4.0 * z) / 4.0


def _tanh_c4_derivative(z: Array) -> Array:
    value = np.tanh(4.0 * z)
    return 1.0 - value * value


# kappa_2 = E[sech^2(2 * 0.65 * Z)], Z ~ N(0,1), evaluated by
# 1024-point Gauss--Hermite quadrature before any training result was viewed.
_KAPPA_C2 = 0.5101185599716273


def _linear_c2(z: Array) -> Array:
    return _KAPPA_C2 * z


def _linear_c2_derivative(z: Array) -> Array:
    return np.full_like(z, _KAPPA_C2)


ACTIVATIONS: Mapping[str, Activation] = MappingProxyType(
    {
        "tanh": Activation("tanh", _tanh, _tanh_derivative),
        "erf": Activation("erf", _erf, _erf_derivative),
        "atan": Activation("atan", _atan, _atan_derivative),
        "identity": Activation("identity", _identity, _identity_derivative),
        "tanh_c2": Activation("tanh_c2", _tanh_c2, _tanh_c2_derivative),
        "tanh_c4": Activation("tanh_c4", _tanh_c4, _tanh_c4_derivative),
        "linear_c2": Activation(
            "linear_c2", _linear_c2, _linear_c2_derivative
        ),
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
