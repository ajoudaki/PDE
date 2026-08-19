"""Deterministic Gaussian evaluator for the fixed-depth, one-sample GNF.

The implementation follows ``DEPTH_B1_GAUSSIAN_RECURSION.md``.  It uses a
high-order Gauss--Hermite rule only in the activation argument and a small
exact Gaussian rule in auxiliary coordinates, where every integrand is a
polynomial of degree at most six.  Response derivatives are propagated
analytically; no finite differences are used.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import pi, sqrt
from typing import Callable

import numpy as np
from numpy.polynomial.hermite import hermgauss


DerivativeOracle = Callable[[int, np.ndarray], np.ndarray]


@dataclass(frozen=True)
class LayerGNFState:
    """Constant-size local state retained by the bottom-up pass."""

    layer: int
    source_gram: np.ndarray | None
    gram: np.ndarray
    responses: np.ndarray
    lambdas: np.ndarray
    reverse_variance: float
    source_variance: float
    readout_x3: float


@dataclass(frozen=True)
class DepthB1GNF:
    """Evaluated coefficients and audit state for one fixed hidden depth."""

    ntk: float
    correction: float
    straight_third: float
    hessian_square: float
    q: np.ndarray
    d: np.ndarray
    reverse_variances: np.ndarray
    source_variances: np.ndarray
    beta: np.ndarray
    rho: np.ndarray
    layers: tuple[LayerGNFState, ...]


def _rule(order: int) -> tuple[np.ndarray, np.ndarray]:
    if order < 1:
        raise ValueError("quadrature order must be positive")
    nodes, weights = hermgauss(order)
    return sqrt(2.0) * nodes, weights / sqrt(pi)


def _standard_grid(dimension: int, order: int) -> tuple[np.ndarray, np.ndarray]:
    """Tensor standard-normal rule in a small auxiliary dimension."""

    if dimension == 0:
        return np.zeros((1, 0)), np.ones(1)
    nodes, weights = _rule(order)
    meshes = np.meshgrid(*([nodes] * dimension), indexing="ij")
    points = np.stack([mesh.reshape(-1) for mesh in meshes], axis=1)
    weight_meshes = np.meshgrid(*([weights] * dimension), indexing="ij")
    total_weights = np.ones_like(weight_meshes[0])
    for weight_mesh in weight_meshes:
        total_weights *= weight_mesh
    return points, total_weights.reshape(-1)


def _psd_root(covariance: np.ndarray, tolerance: float = 2.0e-11) -> np.ndarray:
    covariance = 0.5 * (covariance + covariance.T)
    if covariance.size == 0:
        return np.zeros((0, 0))
    # Diagonal equilibration is essential for high-degree polynomial gates:
    # their legitimate covariance eigenvalues can differ by twenty orders of
    # magnitude.  Thresholding the raw spectrum would erase real low-variance
    # directions.  A correlation-scale eigendecomposition avoids that bug.
    diagonal = np.maximum(np.diag(covariance), 0.0)
    scales = np.sqrt(diagonal)
    active = scales > 0.0
    if not np.any(active):
        if np.max(np.abs(covariance), initial=0.0) > tolerance:
            raise ValueError("zero-variance Gaussian block has nonzero covariance")
        return np.zeros((covariance.shape[0], 0))
    inactive = ~active
    if np.any(inactive):
        leakage = covariance[np.ix_(inactive, active)]
        reference = max(1.0, float(np.max(diagonal)))
        if np.max(np.abs(leakage), initial=0.0) > tolerance * reference:
            raise ValueError("zero-variance coordinate has nonzero covariance")
    active_covariance = covariance[np.ix_(active, active)]
    active_scales = scales[active]
    correlation = active_covariance / np.outer(active_scales, active_scales)
    correlation = 0.5 * (correlation + correlation.T)
    values, vectors = np.linalg.eigh(correlation)
    if float(np.min(values)) < -tolerance:
        raise ValueError(f"Gaussian correlation is not PSD: {values}")
    keep = values > tolerance
    active_root = (
        active_scales[:, None]
        * vectors[:, keep]
        * np.sqrt(np.maximum(values[keep], 0.0))
    )
    root = np.zeros((covariance.shape[0], active_root.shape[1]))
    root[active] = active_root
    return root


def _conditional_rule(
    covariance: np.ndarray,
    extra_variances: tuple[float, ...],
    *,
    main_order: int,
    auxiliary_order: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Quadrature with a high-order rule in Gaussian coordinate zero.

    Returns ``(base, extras, weights)``.  Conditional Gaussian factorization
    isolates the activation argument, while all residual and extra Gaussian
    variables use the small auxiliary rule.  This is a numerical factorization
    only; the analytic recurrence itself never divides by a covariance.
    """

    covariance = np.asarray(covariance, dtype=np.float64)
    if covariance.ndim != 2 or covariance.shape[0] != covariance.shape[1]:
        raise ValueError("covariance must be square")
    dimension = covariance.shape[0]
    if dimension < 1:
        raise ValueError("at least one base Gaussian coordinate is required")
    covariance = 0.5 * (covariance + covariance.T)
    primary_variance = max(0.0, float(covariance[0, 0]))

    if primary_variance > 2.0e-14:
        main_nodes, main_weights = _rule(main_order)
        primary = sqrt(primary_variance) * main_nodes
        cross = covariance[1:, 0] / primary_variance
        residual_covariance = (
            covariance[1:, 1:]
            - np.outer(covariance[1:, 0], covariance[0, 1:])
            / primary_variance
        )
    else:
        primary = np.zeros(1)
        main_weights = np.ones(1)
        cross = np.zeros(dimension - 1)
        residual_covariance = covariance[1:, 1:]

    extra_variances_array = np.maximum(
        np.asarray(extra_variances, dtype=np.float64), 0.0
    )
    residual_dimension = dimension - 1
    combined_covariance = np.zeros(
        (residual_dimension + len(extra_variances),) * 2, dtype=np.float64
    )
    if residual_dimension:
        combined_covariance[:residual_dimension, :residual_dimension] = (
            residual_covariance
        )
    if len(extra_variances):
        combined_covariance[
            residual_dimension:, residual_dimension:
        ] = np.diag(extra_variances_array)

    root = _psd_root(combined_covariance)
    standard, auxiliary_weights = _standard_grid(root.shape[1], auxiliary_order)
    residual = standard @ root.T

    main_count = primary.shape[0]
    auxiliary_count = residual.shape[0]
    base = np.zeros((main_count * auxiliary_count, dimension), dtype=np.float64)
    base[:, 0] = np.repeat(primary, auxiliary_count)
    if residual_dimension:
        conditional_mean = primary[:, None] * cross[None, :]
        base[:, 1:] = (
            conditional_mean[:, None, :]
            + residual[None, :, :residual_dimension]
        ).reshape(-1, residual_dimension)

    extras = np.zeros(
        (main_count * auxiliary_count, len(extra_variances)), dtype=np.float64
    )
    if len(extra_variances):
        extras[:] = np.tile(residual[:, residual_dimension:], (main_count, 1))
    weights = np.repeat(main_weights, auxiliary_count) * np.tile(
        auxiliary_weights, main_count
    )
    return base, extras, weights


def _mean(weights: np.ndarray, value: np.ndarray) -> np.ndarray:
    return np.tensordot(weights, value, axes=(0, 0))


def _activation_values(
    derivative: DerivativeOracle, z: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    return tuple(
        np.asarray(derivative(order, z), dtype=np.float64) for order in range(4)
    )  # type: ignore[return-value]


def _straight_layer(
    layer: int,
    derivative: DerivativeOracle,
    q0: float,
    source_gram: np.ndarray | None,
    prior_responses: np.ndarray | None,
    reverse_variance: float,
    *,
    main_order: int,
    auxiliary_order: int,
) -> LayerGNFState:
    if layer == 1:
        base_covariance = np.asarray([[q0]], dtype=np.float64)
        base, extras, weights = _conditional_rule(
            base_covariance,
            (reverse_variance,),
            main_order=main_order,
            auxiliary_order=auxiliary_order,
        )
        z = base[:, 0]
        reverse = extras[:, 0]
        phi0, phi1, phi2, phi3 = _activation_values(derivative, z)
        delta = phi1 * reverse
        z1 = q0 * delta
        z2 = np.zeros_like(z)
        z3 = np.zeros_like(z)
        dz1 = q0 * phi1
        dz2 = np.zeros_like(z)
        dz3 = np.zeros_like(z)
        lambdas = np.asarray([0.0, q0, 0.0, 0.0])
    else:
        if source_gram is None or prior_responses is None:
            raise ValueError("a hidden transition needs its source state")
        base, extras, weights = _conditional_rule(
            source_gram,
            (reverse_variance,),
            main_order=main_order,
            auxiliary_order=auxiliary_order,
        )
        z = base[:, 0]
        reverse = extras[:, 0]
        phi0, phi1, phi2, phi3 = _activation_values(derivative, z)
        delta = phi1 * reverse
        lambdas = np.zeros(4, dtype=np.float64)
        for order in range(1, 4):
            lambdas[order] = (
                prior_responses[order]
                + order * source_gram[0, order - 1]
            )
        z1 = base[:, 1] + lambdas[1] * delta
        z2 = base[:, 2] + lambdas[2] * delta
        z3 = base[:, 3] + lambdas[3] * delta
        dz1 = lambdas[1] * phi1
        dz2 = lambdas[2] * phi1
        dz3 = lambdas[3] * phi1

    x0 = phi0
    x1 = phi1 * z1
    x2 = phi2 * z1 * z1 + phi1 * z2
    x3 = phi3 * z1**3 + 3.0 * phi2 * z1 * z2 + phi1 * z3
    values = np.stack((x0, x1, x2, x3), axis=1)

    # Analytic dual propagation with respect to the local reverse carrier.
    dx0 = np.zeros_like(z)
    dx1 = phi1 * dz1
    dx2 = 2.0 * phi2 * z1 * dz1 + phi1 * dz2
    dx3 = (
        3.0 * phi3 * z1 * z1 * dz1
        + 3.0 * phi2 * (dz1 * z2 + z1 * dz2)
        + phi1 * dz3
    )
    response_values = np.stack((dx0, dx1, dx2, dx3), axis=1)

    gram = np.einsum("n,ni,nj->ij", weights, values, values)
    gram = 0.5 * (gram + gram.T)
    responses = _mean(weights, response_values)
    readout_x3 = float(_mean(weights, reverse * x3))
    return LayerGNFState(
        layer=layer,
        source_gram=None if source_gram is None else source_gram.copy(),
        gram=np.asarray(gram, dtype=np.float64),
        responses=np.asarray(responses, dtype=np.float64),
        lambdas=lambdas,
        reverse_variance=float(reverse_variance),
        source_variance=float(_mean(weights, delta * delta)),
        readout_x3=readout_x3,
    )


def _reverse_derivative_layer(
    state: LayerGNFState,
    derivative: DerivativeOracle,
    q0: float,
    eta_variance: float,
    response_multiplier: float,
    *,
    main_order: int,
    auxiliary_order: int,
) -> tuple[float, float, float]:
    """Return ``(beta, rho_0, E[Delta dotDelta])`` analytically."""

    if state.layer == 1:
        covariance = np.asarray([[q0]], dtype=np.float64)
        base, extras, weights = _conditional_rule(
            covariance,
            (state.reverse_variance, eta_variance),
            main_order=main_order,
            auxiliary_order=auxiliary_order,
        )
        z = base[:, 0]
        reverse, eta = extras.T
        phi0, phi1, phi2, phi3 = _activation_values(derivative, z)
        delta = phi1 * reverse
        zdot = q0 * delta
    else:
        if state.source_gram is None:
            raise ValueError("missing source Gram")
        tangent_covariance = state.source_gram[np.ix_((0, 1), (0, 1))]
        base, extras, weights = _conditional_rule(
            tangent_covariance,
            (state.reverse_variance, eta_variance),
            main_order=main_order,
            auxiliary_order=auxiliary_order,
        )
        z, fresh_tangent = base.T
        reverse, eta = extras.T
        phi0, phi1, phi2, phi3 = _activation_values(derivative, z)
        delta = phi1 * reverse
        zdot = fresh_tangent + state.lambdas[1] * delta

    reverse_dot = eta + response_multiplier * phi0
    delta_dot = phi2 * zdot * reverse + phi1 * reverse_dot
    beta = float(_mean(weights, delta_dot * delta_dot))
    cross = float(_mean(weights, delta * delta_dot))

    # Syntactic derivative with respect to the base forward innovation z,
    # holding the fresh tangent, reverse carrier, and eta fixed.
    zdot_z = state.lambdas[1] * phi2 * reverse
    reverse_dot_z = response_multiplier * phi1
    delta_dot_z = (
        phi3 * zdot * reverse
        + phi2 * zdot_z * reverse
        + phi2 * reverse_dot
        + phi1 * reverse_dot_z
    )
    rho = float(_mean(weights, delta_dot_z))
    return beta, rho, cross


def evaluate_depth_b1_gnf(
    q0: float,
    hidden_layers: int,
    activation_derivative: DerivativeOracle,
    *,
    main_order: int = 48,
    auxiliary_order: int = 5,
) -> DepthB1GNF:
    """Evaluate ``(A_H,C_H)`` from the fixed-depth one-sample recursion."""

    if q0 < 0.0:
        raise ValueError("q0 must be nonnegative")
    if hidden_layers < 1:
        raise ValueError("hidden_layers must be positive")
    if auxiliary_order < 4:
        raise ValueError("auxiliary_order must be at least four")

    h = hidden_layers
    q = np.zeros(h + 1, dtype=np.float64)
    d = np.zeros(h + 1, dtype=np.float64)
    q[0] = float(q0)
    one_nodes, one_weights = _rule(main_order)
    for layer in range(1, h + 1):
        z = sqrt(max(q[layer - 1], 0.0)) * one_nodes
        phi0 = np.asarray(activation_derivative(0, z), dtype=np.float64)
        phi1 = np.asarray(activation_derivative(1, z), dtype=np.float64)
        q[layer] = float(_mean(one_weights, phi0 * phi0))
        d[layer] = float(_mean(one_weights, phi1 * phi1))

    reverse_variances = np.zeros(h + 1, dtype=np.float64)
    source_variances = np.zeros(h + 1, dtype=np.float64)
    reverse_variances[h] = 1.0
    for layer in range(h, 0, -1):
        source_variances[layer] = d[layer] * reverse_variances[layer]
        if layer > 1:
            reverse_variances[layer - 1] = source_variances[layer]

    theta = q0
    for layer in range(1, h + 1):
        theta = q[layer] + d[layer] * theta

    layers: list[LayerGNFState] = []
    source_gram = None
    prior_responses = None
    for layer in range(1, h + 1):
        state = _straight_layer(
            layer,
            activation_derivative,
            q0,
            source_gram,
            prior_responses,
            reverse_variances[layer],
            main_order=main_order,
            auxiliary_order=auxiliary_order,
        )
        layers.append(state)
        source_gram = state.gram
        prior_responses = state.responses

    straight_third = layers[-1].readout_x3 + 3.0 * layers[-1].gram[0, 2]

    beta = np.zeros(h + 1, dtype=np.float64)
    rho = np.zeros(h + 1, dtype=np.float64)
    eta_variance = 0.0
    response_multiplier = 1.0  # top readout derivative is X_H.
    for layer in range(h, 0, -1):
        beta[layer], rho[layer], cross = _reverse_derivative_layer(
            layers[layer - 1],
            activation_derivative,
            q0,
            eta_variance,
            response_multiplier,
            main_order=main_order,
            auxiliary_order=auxiliary_order,
        )
        scale = max(1.0, abs(beta[layer]), abs(source_variances[layer]))
        if abs(cross) > 2.0e-9 * scale:
            raise AssertionError(
                f"parity certificate failed at layer {layer}: {cross}"
            )
        if layer > 1:
            eta_variance = beta[layer]
            response_multiplier = source_variances[layer] + rho[layer]

    hessian_square = layers[-1].gram[1, 1] + q0 * beta[1]
    for layer in range(2, h + 1):
        hessian_square += (
            q[layer - 1] * beta[layer]
            + source_variances[layer] * layers[layer - 2].gram[1, 1]
        )
    correction = 2.0 * straight_third + 4.0 * hessian_square

    return DepthB1GNF(
        ntk=float(theta),
        correction=float(correction),
        straight_third=float(straight_third),
        hessian_square=float(hessian_square),
        q=q,
        d=d,
        reverse_variances=reverse_variances,
        source_variances=source_variances,
        beta=beta,
        rho=rho,
        layers=tuple(layers),
    )
