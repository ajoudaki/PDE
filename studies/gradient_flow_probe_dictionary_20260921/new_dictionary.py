"""Study-only derivative dictionaries on a canonical finite Gaussian carrier.

Levels 1, 2, 3 mean weight powers t^2, t^3, t^4. Probes are normalized
directions e_1,e_2, hence physical inputs sqrt(2)e_a. All marks are frozen
initialization functions. These population-derived spans do not assert exact
finite-width jets, initial-network preservation, or general-input closure.
"""
from functools import lru_cache
import json

import numpy as np
import torch

from pde.observable_torch_p1 import ClosureEngine, TensorState


@lru_cache(maxsize=1)
def _variance_rules():
    values = []
    for order in (128, 256):
        nodes, weights = np.polynomial.hermite.hermgauss(order)
        values.append(float(weights @ np.tanh(np.sqrt(2.0) * nodes) ** 2
                            / np.sqrt(np.pi)))
    return tuple(values)


def _quadrature_metadata():
    coarse, fine = _variance_rules()
    return {"v": fine, "v_128": coarse, "v_256": fine,
            "v_quadrature_absolute_discrepancy": abs(fine - coarse),
            "v_quadrature": "Gauss-Hermite 128/256; 256-node working value",
            "v_target": "E[tanh(G)^2], G standard normal",
            "v_discrepancy_is_error_bound": False}


def _validate_initial(initial, p):
    if isinstance(p, bool) or not isinstance(p, int) or p not in (1, 2, 3):
        raise ValueError("new dictionary level must be 1, 2, or 3")
    if not isinstance(initial, TensorState):
        raise ValueError("initial must be the canonical finite TensorState")
    if initial.w.ndim != 2 or initial.w.shape[1] != 2:
        raise ValueError("initial.w must have shape (n,2)")
    n = initial.w.shape[0]
    if n < 1 or initial.M.shape != (n, n) or initial.c.shape != (n,):
        raise ValueError("inconsistent equal-width finite initial state")
    if initial.w.dtype not in (torch.float32, torch.float64):
        raise ValueError("initial state must use float32 or float64")
    for value in (initial.w, initial.c, initial.M):
        if value.dtype != initial.w.dtype or value.device != initial.w.device:
            raise ValueError("initial state dtype/device mismatch")
        if not bool(torch.isfinite(value).all()):
            raise ValueError("nonfinite initial state")


def _initialized_fields(initial, p):
    h = torch.tanh(initial.w)
    H = torch.tanh(initial.M @ h)
    D = 1 - H.square()
    U = D[:, :, None] * H[:, None, :]
    fields = {"h": h, "H": H, "U": U}
    if p == 3:
        Q = (initial.M.T @ U.flatten(1)).reshape(-1, 2, 2)
        lower_gate_squared = (1 - h.square()).square()
        L = lower_gate_squared[:, :, None] * Q
        # Unit normalized probe Gram: R_a=(y_a/2) sum_b y_b F_ab.
        # Literal physical e_a probes would instead require 2*v*U here.
        F = _variance_rules()[1] * U + (initial.M @ L.flatten(1)).reshape(-1, 2, 2)
        fields.update(L=L, F=F)
    return fields


def _collected_upper(H, F):
    D, E = 1 - H.square(), -2 * H * (1 - H.square())

    def A(a, b, c):
        return D[:, a] * D[:, b] * F[:, b, c]

    def B(a, b, c):
        return H[:, c] * E[:, a] * F[:, a, b]

    return torch.stack((
        A(0, 0, 0) + 3 * B(0, 0, 0),
        A(0, 0, 1) + 3 * (B(0, 0, 1) + B(0, 1, 0)),
        A(0, 1, 0) + 3 * B(0, 1, 1),
        A(0, 1, 1),
        A(1, 0, 0),
        A(1, 0, 1) + 3 * B(1, 0, 0),
        A(1, 1, 0) + 3 * (B(1, 0, 1) + B(1, 1, 0)),
        A(1, 1, 1) + 3 * B(1, 1, 1),
    ), dim=1)


@torch.no_grad()
def raw_features(initial, p):
    """Return (lower table, upper table, JSON-safe metadata), without ridge.

    Column order is lower h1,h2,[L11,L12,L21,L22], and upper
    U11,U12,U21,U22,[C1,...,C8]. Both first levels have identical tables.
    C1...C4 multiply y1^4,y1^3*y2,y1^2*y2^2,y1*y2^3 in the h1
    coefficient; C5...C8 multiply y1^3*y2,...,y2^4 in h2. The actual
    feedback coefficient has an additional common factor 1/6.
    """
    _validate_initial(initial, p)
    fields = _initialized_fields(initial, p)
    lower, upper = fields["h"], fields["U"].flatten(1)
    if p == 3:
        lower = torch.cat((lower, fields["L"].flatten(1)), dim=1)
        upper = torch.cat((upper, _collected_upper(fields["H"], fields["F"])), dim=1)
    if not bool(torch.isfinite(lower).all() and torch.isfinite(upper).all()):
        raise ValueError("nonfinite derivative dictionary")
    metadata = {"dictionary": "derivative_collected_increment", "p": p,
                "maximum_weight_taylor_power": p + 1,
                "normalized_probes": [[1.0, 0.0], [0.0, 1.0]],
                "physical_probe_scale": float(np.sqrt(2.0)),
                "K1": lower.shape[1], "K2": upper.shape[1],
                "lower_column_order": ["h1", "h2"] +
                    (["L11", "L12", "L21", "L22"] if p == 3 else []),
                "upper_column_order": ["U11", "U12", "U21", "U22"] +
                    ([f"C{i}" for i in range(1, 9)] if p == 3 else []),
                "F_coefficient": "v*U + W0*L",
                "raw_column_rescaling": "none",
                "finite_jet_matching_claim": False,
                **_quadrature_metadata()}
    return lower.contiguous(), upper.contiguous(), metadata


def _ridge_basis(raw, eta):
    n, k = raw.shape
    gram = raw.T @ raw / n
    gram = (gram + gram.T) / 2
    identity = torch.eye(k, dtype=raw.dtype, device=raw.device)
    regularized = gram + eta * identity
    chol = torch.linalg.cholesky(regularized)
    basis = torch.linalg.solve_triangular(chol, raw.T, upper=False).T.contiguous()
    effective_gram = basis.T @ basis / n
    effective_gram = (effective_gram + effective_gram.T) / 2
    raw_eigs = torch.linalg.eigvalsh(gram)
    effective_eigs = torch.linalg.eigvalsh(effective_gram)
    eps = torch.finfo(raw.dtype).eps
    raw_threshold = max(n, k) * eps * max(float(raw_eigs[-1]), 0.0)
    effective_threshold = max(n, k) * eps * max(float(effective_eigs[-1]), 0.0)
    chol_inverse = torch.linalg.solve_triangular(chol, identity, upper=False)
    ridge_identity = effective_gram + eta * (chol_inverse @ chol_inverse.T)
    raw_norm = float(torch.linalg.norm(raw))
    triangular_error = float(torch.linalg.norm(basis @ chol.T - raw))
    triangular_residual = triangular_error / raw_norm if raw_norm else triangular_error
    diagnostics = {
        "raw_eigenvalues": raw_eigs.cpu().tolist(),
        "effective_eigenvalues": effective_eigs.cpu().tolist(),
        "raw_numerical_rank": int((raw_eigs > raw_threshold).sum()),
        "effective_numerical_rank": int((effective_eigs > effective_threshold).sum()),
        "raw_rank_threshold": raw_threshold,
        "effective_rank_threshold": effective_threshold,
        "rank_threshold_rule": "max(n,K)*dtype_epsilon*largest_Gram_eigenvalue",
        "filter_directions_above_half": int((effective_eigs > 0.5).sum()),
        "effective_degrees_of_freedom": float(effective_eigs.sum()),
        "ridge_condition": float((raw_eigs[-1] + eta) / (raw_eigs[0] + eta)),
        "cholesky_relative_residual": float(torch.linalg.norm(chol @ chol.T - regularized)
                                            / torch.linalg.norm(regularized)),
        "triangular_relative_residual": triangular_residual,
        "ridge_identity_residual_frobenius": float(torch.linalg.norm(ridge_identity - identity)),
        "ridge_condition_limit": 1e10,
        "triangular_relative_residual_limit": 1e-8,
    }
    # Reject unresolved diagnostics rather than serializing a silent bad pass.
    json.dumps(diagnostics, allow_nan=False)
    if not 1.0 <= diagnostics["ridge_condition"] <= 1e10:
        raise ValueError("derivative dictionary ridge condition exceeds 1e10")
    if triangular_residual > 1e-8:
        raise ValueError("derivative dictionary triangular residual exceeds 1e-8")
    return basis, diagnostics


@torch.no_grad()
def build(initial, p, *, block_size=512, forward_mode="auto"):
    """Return the maintained engine, coupled initial state, and diagnostics.

    Entire middle block is B2 M B1.T/n; there is no dense background.
    The original finite random readout is retained. Cholesky ridge and ordinary
    coordinate M dynamics follow the comparison method's filtered metric.
    """
    lower, upper, metadata = raw_features(initial, p)
    n = initial.w.shape[0]
    eta = 1.0 / (1024 * (p + 1) ** 2)
    b1, lower_diagnostics = _ridge_basis(lower, eta)
    b2, upper_diagnostics = _ridge_basis(upper, eta)
    M0 = b2.T @ (initial.M @ b1) / n
    metadata.update(eta=eta, lower=lower_diagnostics, upper=upper_diagnostics,
                    width=n, middle_parameter_count=b1.shape[1] * b2.shape[1],
                    retained_initial_readout=True, retained_dense_background=False,
                    normalization="raw Gram plus eta*I, inverse Cholesky transpose",
                    sign_folded=False, population_rule="finite Gaussian carrier",
                    nominal_population_nodes=n, omitted_inactive_constant_features=False)
    engine = ClosureEngine(b1, initial.w, b2, M0, device=initial.w.device,
                           dtype=initial.w.dtype, block_size=block_size,
                           forward_mode=forward_mode, representation=metadata)
    state = engine.state(initial.w, initial.c, M0)
    return engine, state, metadata
