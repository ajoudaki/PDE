"""Width-independent operator-Galerkin neural-PDE simulator."""

from activations import (
    ACTIVATIONS,
    ACTIVATION_NAMES,
    Activation,
    get_activation,
)

from .operator_galerkin import (
    Fields,
    Observable,
    PDEQuadrature,
    PDESpec,
    PDEState,
    build_quadrature,
    build_hybrid_quadrature,
    build_tensor_quadrature,
    heun_step,
    initialize,
    observe,
    rk4_step,
    solve_fields,
    vector_field,
)

__all__ = [
    "ACTIVATIONS",
    "ACTIVATION_NAMES",
    "Activation",
    "Fields",
    "Observable",
    "PDEQuadrature",
    "PDESpec",
    "PDEState",
    "build_quadrature",
    "build_hybrid_quadrature",
    "build_tensor_quadrature",
    "heun_step",
    "get_activation",
    "initialize",
    "observe",
    "rk4_step",
    "solve_fields",
    "vector_field",
]
