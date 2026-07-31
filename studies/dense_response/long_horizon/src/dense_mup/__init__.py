"""Reproducible dense-muP long-horizon response experiments."""

from .core import (
    FieldState,
    ModelSpec,
    ParamState,
    exact_training_derivatives,
    field_vector_field,
    fields_from_params,
    forward_adjoint,
    initialize,
    parameter_vector_field,
    rk4_field_step,
    rk4_param_step,
)

__all__ = [
    "FieldState",
    "ModelSpec",
    "ParamState",
    "exact_training_derivatives",
    "field_vector_field",
    "fields_from_params",
    "forward_adjoint",
    "initialize",
    "parameter_vector_field",
    "rk4_field_step",
    "rk4_param_step",
]
