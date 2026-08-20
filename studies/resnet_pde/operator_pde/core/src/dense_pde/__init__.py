"""Width-independent operator-Galerkin neural-PDE simulator."""

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
    "Fields",
    "Observable",
    "PDEQuadrature",
    "PDESpec",
    "PDEState",
    "build_quadrature",
    "build_hybrid_quadrature",
    "build_tensor_quadrature",
    "heun_step",
    "initialize",
    "observe",
    "rk4_step",
    "solve_fields",
    "vector_field",
]
