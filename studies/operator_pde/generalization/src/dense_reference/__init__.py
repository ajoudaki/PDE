"""Exact finite dense-ResNet reference implementation."""

from activations import (
    ACTIVATIONS,
    ACTIVATION_NAMES,
    Activation,
    get_activation,
)

from .core import (
    FieldState,
    ModelSpec,
    ParamState,
    forward_adjoint,
    initialize,
    parameter_vector_field,
    rk4_param_step,
    tangent_kernel,
)

__all__ = [
    "ACTIVATIONS",
    "ACTIVATION_NAMES",
    "Activation",
    "FieldState",
    "ModelSpec",
    "ParamState",
    "forward_adjoint",
    "get_activation",
    "initialize",
    "parameter_vector_field",
    "rk4_param_step",
    "tangent_kernel",
]
