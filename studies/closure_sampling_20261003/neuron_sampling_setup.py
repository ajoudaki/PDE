"""Bounded, initialization-only practical neuron compression.

This is a truncated numerical variant of TWO_INPUT_CANONICAL_COMPRESSION.md,
not an implementation of its unbounded initial-jet construction.  It computes
only h(0), g(0), h''(0), g''(0), delta'(0), and their original-mixer partners.
Positive cubature is approximate and source spaces are rank truncated.

All input directions are ROWS: X.shape == (m, 2), and actual x = sqrt(2)*X.
The initialized readout is zero and loss is mean((f-y)**2), so velocities use
2/m.  The returned A, B, w, mu, nu are the complete network state and masses.
No full-width array is retained in the returned result.  ``prepare_witness``
is optional setup-only workspace and must be discarded after construction.
"""

from __future__ import annotations

import time
from typing import Any

import numpy as np
from scipy.linalg import qr
from scipy.optimize import minimize


def _matrix(x: Any, name: str) -> np.ndarray:
    out = np.asarray(x, dtype=np.float64)
    if out.ndim != 2 or not np.isfinite(out).all():
        raise ValueError(f"{name} must be a finite matrix")
    return out


def prepare_witness(A0, W0, X, labels, *, probe_count: int = 16) -> dict:
    """Compute a finite initial witness; never train or evaluate a future state.

    The circle probes cover [0,pi): every supplied source is odd in the query
    direction, so antipodal points add exactly redundant columns.  Training
    directions are appended explicitly.  Probe jets are exact algebraic
    second physical-time derivatives of the dense initialized equations.
    """
    begin = time.perf_counter()
    A0, W0, X = (_matrix(v, k) for v, k in ((A0, "A0"), (W0, "W0"), (X, "X")))
    labels = np.asarray(labels, dtype=np.float64)
    n, d = A0.shape
    if d != 2 or W0.shape != (n, n) or X.shape[1] != 2:
        raise ValueError("expected A0[n,2], W0[n,n], X[m,2]")
    if labels.shape != (len(X),) or len(X) < 1 or not np.isfinite(labels).all():
        raise ValueError("labels must be a finite length-m vector")
    if not np.allclose(np.linalg.norm(X, axis=1), 1.0, rtol=0, atol=1e-10):
        raise ValueError("X must contain unit directions as rows")
    if not isinstance(probe_count, (int, np.integer)) or probe_count < 4:
        raise ValueError("probe_count must be an integer >= 4")
    theta = np.pi * np.arange(probe_count) / probe_count
    probes = np.concatenate((X, np.column_stack((np.cos(theta), np.sin(theta)))))
    H = np.tanh(A0 @ probes.T)
    Z = W0 @ H
    G = np.tanh(Z)
    m = len(X)
    Htrain, Gtrain = H[:, :m], G[:, :m]
    factor = 2.0 / m
    wdot = factor * (Gtrain @ labels)
    delta_dot = wdot[:, None] * (1.0 - Gtrain * Gtrain)
    reverse = W0.T @ delta_dot
    A_ddot = factor * (((1.0 - Htrain * Htrain) * reverse) * labels) @ X
    H_ddot = (1.0 - H * H) * (A_ddot @ probes.T)
    WH_ddot = W0 @ H_ddot
    # W'' H is evaluated in factored form: the n-by-n W'' is never allocated.
    Z_ddot = WH_ddot + (factor / n) * (delta_dot * labels) @ (Htrain.T @ H)
    G_ddot = (1.0 - G * G) * Z_ddot
    groups1 = [("A0", A0, .25), ("h0", H, 1.0),
               ("reverse_delta1", reverse, .5), ("h2", H_ddot, .3)]
    groups2 = [("z0", Z, 1.0), ("g0", G, 1.0),
               ("delta1", delta_dot, .5), ("g2", G_ddot, .3),
               ("W_h2", WH_ddot, .3)]
    return dict(A0=A0, W0=W0, X=X, labels=labels, n=n, m=m,
                probe_count=probe_count, probes=probes, H=H, Z=Z, G=G,
                delta_dot=delta_dot, reverse=reverse, groups1=groups1,
                groups2=groups2, setup_seconds=time.perf_counter()-begin)


def _basis(priority: np.ndarray, groups: list, rank: int, tolerance: float):
    """Keep training priorities first, then use a weighted source SVD."""
    n = priority.shape[0]
    priority_u, priority_s, _ = np.linalg.svd(priority, full_matrices=False)
    priority_keep = min(rank, int(np.sum(priority_s > tolerance * max(priority_s[0], 1.0))))
    basis = priority_u[:, :priority_keep]
    columns = []
    skipped = []
    for name, source, weight in groups:
        rms = np.sqrt(np.mean(source * source, axis=0))
        keep = rms > tolerance
        skipped.append(dict(source=name, zero_or_tiny_columns=int(np.sum(~keep))))
        if np.any(keep):
            columns.append(weight * source[:, keep] / rms[keep] / np.sqrt(np.sum(keep)))
    source_matrix = np.concatenate(columns, axis=1)
    remainder = source_matrix - basis @ (basis.T @ source_matrix)
    u, singular, _ = np.linalg.svd(remainder, full_matrices=False)
    available = int(np.sum(singular > tolerance * max(singular[0], 1.0)))
    keep = min(rank - priority_keep, available)
    basis = np.concatenate((basis, u[:, :keep]), axis=1)
    # A second QR removes roundoff overlap between the priority and remainder.
    basis, _ = np.linalg.qr(basis, mode="reduced")
    diagnostics = dict(requested_rank=rank, retained_rank=basis.shape[1],
                       priority_rank=priority_keep,
                       discarded_priority_directions=max(0, int(np.sum(
                           priority_s > tolerance * max(priority_s[0], 1.0)))-priority_keep),
                       priority_singular_values=priority_s.tolist(),
                       remainder_singular_values=singular.tolist(),
                       discarded_resolved_directions=max(0, available-keep),
                       tiny_source_columns=skipped, source_residuals={})
    for name, source, _ in groups:
        error = source - basis @ (basis.T @ source)
        norm = float(np.linalg.norm(source))
        diagnostics["source_residuals"][name] = dict(
            relative_frobenius=float(np.linalg.norm(error) / norm) if norm else 0.,
            maximum_absolute=float(np.max(np.abs(error))))
    return basis * np.sqrt(n), diagnostics


def _positive_cubature(V: np.ndarray, count: int, floor_fraction: float):
    """Deterministic QR seed, greedy additions, bounded simplex weight fits."""
    n, rank = V.shape
    ii, jj = np.triu_indices(rank)
    product = V[:, ii] * V[:, jj]
    product[:, ii != jj] *= np.sqrt(2.0)
    feature = np.column_stack((np.ones(n), product)).T
    scale = np.sqrt(np.mean(feature * feature, axis=1))
    feature /= np.maximum(scale[:, None], 1e-14)
    target = feature.mean(axis=1)
    _, _, pivots = qr(V.T, mode="economic", pivoting=True)
    selected = list(map(int, pivots[:min(rank, count)]))
    floor = floor_fraction / count
    fits = []
    weights = None
    while True:
        F = feature[:, selected]
        initial = np.full(len(selected), 1.0 / len(selected))
        if weights is not None:
            initial[:-1] = weights * (1.0 - floor)
            initial[-1] = floor
        def objective(p):
            residual = F @ p - target
            return .5 * float(residual @ residual)
        def derivative(p):
            return F.T @ (F @ p - target)
        result = minimize(objective, initial, jac=derivative, method="SLSQP",
                          bounds=[(floor, 1.0)] * len(selected),
                          constraints=[dict(type="eq", fun=lambda p: np.sum(p)-1.,
                                            jac=lambda p: np.ones_like(p))],
                          options=dict(ftol=1e-12, maxiter=150, disp=False))
        weights = np.asarray(result.x)
        if (not np.isfinite(weights).all() or
                abs(weights.sum()-1.) > 1e-8 or weights.min() < floor-1e-9):
            raise RuntimeError("cubature optimizer returned invalid positive masses")
        # Restore the strict prescribed floor and unit sum at roundoff level.
        excess = np.maximum(weights-floor, 0.0)
        weights = floor + (1.0-len(selected)*floor) * excess / excess.sum()
        fits.append(dict(success=bool(result.success), status=int(result.status),
                         iterations=int(result.nit), objective=objective(weights)))
        if len(selected) == count:
            break
        residual = target - F @ weights
        direction = feature - (F @ weights)[:, None]
        score = direction.T @ residual / np.maximum(np.linalg.norm(direction, axis=0), 1e-14)
        score[selected] = -np.inf
        selected.append(int(np.argmax(score)))
    selected = np.asarray(selected, dtype=np.int64)
    gram = V[selected].T @ (weights[:, None] * V[selected])
    diagnostics = dict(min_mass=float(weights.min()), max_mass=float(weights.max()),
                       mass_ratio=float(weights.max()/weights.min()),
                       mass_sum=float(weights.sum()), floor_fraction=floor_fraction,
                       gram_frobenius_error=float(np.linalg.norm(gram-np.eye(rank))),
                       gram_operator_error=float(np.linalg.norm(gram-np.eye(rank), 2)),
                       gram_eigenvalues=np.linalg.eigvalsh(gram).tolist(), fits=fits)
    return selected, weights, diagnostics


def _isometric_frame(rows, masses, tolerance):
    gram = rows.T @ (masses[:, None] * rows)
    values, vectors = np.linalg.eigh(gram)
    cutoff = tolerance * max(1., float(values[-1]))
    keep = values > cutoff
    inverse_sqrt = (vectors[:, keep] / np.sqrt(values[keep])) @ vectors[:, keep].T
    frame = np.sqrt(masses)[:, None] * rows @ inverse_sqrt
    return frame, dict(gram_eigenvalues=values.tolist(), threshold=cutoff,
                       retained_directions=int(np.sum(keep)),
                       discarded_directions=int(np.sum(~keep)),
                       frame_operator_norm=float(np.linalg.norm(frame, 2)))


def _weighted_error(actual, target, masses):
    error = actual-target
    rms = np.sqrt(np.sum(masses[:, None] * error * error, axis=0))
    size = np.sqrt(np.sum(masses[:, None] * target * target, axis=0))
    return dict(maximum_weighted_rms=float(rms.max()),
                mean_weighted_rms=float(np.mean(rms)),
                maximum_absolute=float(np.abs(error).max()),
                relative_combined_rms=float(np.linalg.norm(rms)/max(np.linalg.norm(size),1e-30)))


def build_sampler(A0, W0, X, labels, n_selected: int, *, probe_count: int = 16,
                  basis_rank: int | None = None, mass_floor: float = .05,
                  singular_tolerance: float = 1e-10, witness: dict | None = None) -> dict:
    """Return selected A, projected B, zero w, positive mu/nu, diagnostics.

    B is formed in square-root-mass coordinates.  Writing C=U.T W0 V/n,
    Q1=sqrt(mu)*V[I]*G1**(-1/2), Q2=sqrt(nu)*U[J]*G2**(-1/2), the
    operator is T=Q2 C Q1.T and B=diag(nu)**(-1/2) T diag(mu)**(1/2).
    The frames are partial isometries if singular directions are discarded.
    Thus ||T|| <= ||C|| <= ||W0|| in exact arithmetic.  Its reverse action
    MUST be B*=diag(mu)**(-1) B.T diag(nu), not the ordinary transpose.
    Neither exact cubature nor exact initial derivative matching is claimed.
    """
    begin = time.perf_counter()
    if not isinstance(n_selected, (int, np.integer)) or n_selected < 4:
        raise ValueError("n_selected must be an integer >= 4")
    if not 0. < mass_floor < 1. or not 0. < singular_tolerance < 1.:
        raise ValueError("require 0 < mass_floor, singular_tolerance < 1")
    if witness is None:
        witness = prepare_witness(A0, W0, X, labels, probe_count=probe_count)
    else:
        # Check provenance rather than silently reusing another label task.
        if not (np.array_equal(witness["A0"], np.asarray(A0)) and
                np.array_equal(witness["W0"], np.asarray(W0)) and
                np.array_equal(witness["X"], np.asarray(X)) and
                np.array_equal(witness["labels"], np.asarray(labels)) and
                witness["probe_count"] == probe_count):
            raise ValueError("witness does not match supplied initialization/task")
    n, m = witness["n"], witness["m"]
    if n_selected > n:
        raise ValueError("cannot select more than n neurons")
    if basis_rank is None:
        basis_rank = min(n_selected-1, 8)
    if not isinstance(basis_rank, (int, np.integer)) or not 1 <= basis_rank <= n_selected:
        raise ValueError("basis_rank must be an integer from 1 to n_selected")
    H, G, Z = witness["H"], witness["G"], witness["Z"]
    V, vinfo = _basis(H[:, :m], witness["groups1"], basis_rank, singular_tolerance)
    U, uinfo = _basis(np.column_stack((G[:, :m], Z[:, :m])), witness["groups2"],
                      basis_rank, singular_tolerance)
    I, mu, mass1 = _positive_cubature(V, n_selected, mass_floor)
    J, nu, mass2 = _positive_cubature(U, n_selected, mass_floor)
    Q1, frame1 = _isometric_frame(V[I], mu, singular_tolerance)
    Q2, frame2 = _isometric_frame(U[J], nu, singular_tolerance)
    C = U.T @ (witness["W0"] @ V) / n
    T = Q2 @ C @ Q1.T
    B = T * np.sqrt(mu)[None, :] / np.sqrt(nu)[:, None]
    A = witness["A0"][I].copy()
    w = np.zeros(n_selected, dtype=np.float64)
    Bstar = B.T * nu[None, :] / mu[:, None]
    Gcompressed = np.tanh(B @ H[I])
    factor = 2.0 / m
    delta_compressed_dot = (factor * (Gcompressed[:, :m] @ witness["labels"]))[:, None] * (
        1.0 - Gcompressed[:, :m]**2)
    A_compressed_ddot = factor * (((1.0-H[I, :m]**2) * (Bstar @ delta_compressed_dot)) *
                                   witness["labels"]) @ witness["X"]
    H_compressed_ddot = (1.0-H[I]**2) * (A_compressed_ddot @ witness["probes"].T)
    G_compressed_ddot = (1.0-Gcompressed**2) * (B @ H_compressed_ddot + factor *
        (delta_compressed_dot * witness["labels"]) @ (H[I, :m].T @ (mu[:, None] * H[I])))
    gram_dense = G[:, :m].T @ G[:, :m] / n
    gram_compressed = Gcompressed[:, :m].T @ (nu[:, None] * Gcompressed[:, :m])
    gram_selected = G[J, :m].T @ (nu[:, None] * G[J, :m])
    diagnostics = dict(
        variant="bounded_initial_jets_2_positive_approximate_cubature_isometric_projection_v1",
        theorem_implementation=False, trained_snapshots_used=False,
        initial_forward_derivative_order=2, initial_reverse_derivative_order=1,
        dense_width=n, selected_first=n_selected, selected_second=n_selected,
        probe_count=witness["probe_count"], training_count=m,
        basis1=vinfo, basis2=uinfo, cubature1=mass1, cubature2=mass2,
        frame1=frame1, frame2=frame2,
        projected_core_operator_norm=float(np.linalg.norm(C, 2)),
        weighted_B_operator_norm=float(np.linalg.norm(T, 2)),
        forward_initial=_weighted_error(B @ H[I], Z[J], nu),
        forward_second_jet=_weighted_error(B @ witness["groups1"][-1][1][I],
                                           witness["groups2"][-1][1][J], nu),
        reverse_initial_jet=_weighted_error(Bstar @ witness["delta_dot"][J],
                                            witness["reverse"][I], mu),
        feature_initial=_weighted_error(Gcompressed, G[J], nu),
        own_first_feature_second_jet=_weighted_error(H_compressed_ddot,
                                                    witness["groups1"][-1][1][I], mu),
        own_second_feature_second_jet=_weighted_error(G_compressed_ddot,
                                                     witness["groups2"][-2][1][J], nu),
        dense_initial_training_gram=gram_dense.tolist(),
        selected_target_training_gram=gram_selected.tolist(),
        compressed_initial_training_gram=gram_compressed.tolist(),
        training_gram_frobenius_error=float(np.linalg.norm(gram_compressed-gram_dense)),
        dense_initial_gram_gap=float(np.linalg.eigvalsh(gram_dense)[0]),
        compressed_initial_gram_gap=float(np.linalg.eigvalsh(gram_compressed)[0]),
        moving_scalar_count=int(A.size+B.size+w.size),
        fixed_mass_scalar_count=int(mu.size+nu.size),
        shared_data_scalar_count=int(3*m),
        network_and_mass_scalar_count=int(A.size+B.size+w.size+mu.size+nu.size),
        selected_index_archive_count=int(I.size+J.size),
        witness_setup_seconds=witness["setup_seconds"],
        sampler_seconds=time.perf_counter()-begin)
    for array in (A, B, w, mu, nu):
        if not np.isfinite(array).all():
            raise RuntimeError("nonfinite retained sampler state")
    return dict(A=A, B=B, w=w, mu=mu, nu=nu,
                selected_first=I, selected_second=J, diagnostics=diagnostics)
