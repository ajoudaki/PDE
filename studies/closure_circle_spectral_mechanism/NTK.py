"""Deterministic frozen initial kernel for the canonical two-hidden tanh MLP.

Angles are radians and represent x=sqrt(2)*(cos(angle),sin(angle)).  The
kernel excludes the loss factor two.  Prediction uses zero initial output,
the full weighted squared loss, and physical time.  This is a numerical
Gaussian integral implementation, not an interval certificate.
"""

from functools import lru_cache
from numbers import Integral, Real

import numpy as np
from scipy.special import roots_hermitenorm


def _real_array(value, name):
    raw = np.asarray(value)
    if raw.dtype.kind not in "iuf":
        raise ValueError(f"{name} must contain real numbers")
    out = np.asarray(raw, dtype=np.float64)
    if not np.all(np.isfinite(out)):
        raise ValueError(f"{name} must be finite")
    return out


@lru_cache(maxsize=12)
def _rule(quad_nodes):
    if (isinstance(quad_nodes, (bool, np.bool_))
            or not isinstance(quad_nodes, Integral) or quad_nodes < 8):
        raise ValueError("quad_nodes must be an integer at least 8")
    z, w = roots_hermitenorm(int(quad_nodes))
    w = w / np.sqrt(2 * np.pi)
    z.setflags(write=False)
    w.setflags(write=False)
    return z, w


def _variance(variance, quad_nodes):
    z, w = _rule(quad_nodes)
    return float(w @ np.tanh(np.sqrt(variance) * z)**2)


def _covariance(correlation, variance, quad_nodes):
    """Symmetric two-dimensional Gauss--Hermite covariance contraction.

    Exact oddness in correlation and exact endpoint contractions are
    imposed analytically.  A block contains at most 16*n*n float64 values.
    """
    corr = np.asarray(correlation, dtype=float)
    flat = corr.ravel()
    if np.any(np.abs(flat) > 1 + 1e-12):
        raise ValueError("Gaussian correlation is outside [-1,1]")
    unique, inverse = np.unique(np.clip(np.abs(flat), 0, 1), return_inverse=True)
    result = np.empty_like(unique)
    z, w = _rule(quad_nodes)
    result[unique == 0] = 0.
    result[unique == 1] = _variance(variance, quad_nodes)
    active = np.flatnonzero((unique > 0) & (unique < 1))
    for start in range(0, len(active), 16):
        ids = active[start:start + 16]
        rho = unique[ids, None, None]
        common = np.sqrt(variance * (1 + rho) / 2) * z[None, :, None]
        difference = np.sqrt(variance * (1 - rho) / 2) * z[None, None, :]
        products = np.tanh(common + difference) * np.tanh(common - difference)
        result[ids] = np.einsum("a,b,iab->i", w, w, products, optimize=False)
    return (np.sign(flat) * result[inverse]).reshape(corr.shape)


def kernel(angle_diffs, quad_nodes=128):
    """Return k(theta) with shape preserved, for any finite real angle array.

    Let q=E tanh(Z)^2 for Z~N(0,1), and C_v(rho) be the tanh
    covariance of a Gaussian pair of variance v and correlation rho.
    Then k(theta)=C_q(C_1(cos(theta))/q).
    """
    angle = _real_array(angle_diffs, "angle_diffs")
    q = _variance(1., quad_nodes)
    inner = _covariance(np.cos(angle), 1., quad_nodes)
    return _covariance(inner / q, q, quad_nodes)


def _covariance_decrement(correlation_decrement, variance, quad_nodes):
    """Stable half squared increment, for correlations close to one."""
    loss = np.asarray(correlation_decrement, dtype=float)
    if np.any((loss < 0) | (loss > 2)):
        raise ValueError("correlation decrement must be in [0,2]")
    z, w = _rule(quad_nodes)
    out = np.empty(loss.size)
    flat = loss.ravel()
    for start in range(0, flat.size, 16):
        val = flat[start:start + 16, None, None]
        common = np.sqrt(variance * (1 - val / 2)) * z[None, :, None]
        difference = np.sqrt(variance * val / 2) * z[None, None, :]
        delta = np.tanh(common + difference) - np.tanh(common - difference)
        out[start:start + 16] = .5 * np.einsum("a,b,iab->i", w, w, delta**2)
    return out.reshape(loss.shape)


def kernel_decrement(angle_diffs, quad_nodes=128):
    """Numerically stable evaluation of k(0)-k(theta), even at tiny theta.

    This uses the Gaussian identity Var(tanh U)-Cov(tanh U,tanh V)
    =E[(tanh U-tanh V)^2]/2 twice.  At finite quadrature the identity's
    marginal integral need not equal the separately contracted 1D rule;
    that independent discrepancy is measured by NTK_CHECK.py.
    """
    angle = _real_array(angle_diffs, "angle_diffs")
    q = _variance(1., quad_nodes)
    lower_drop = _covariance_decrement(2 * np.sin(angle / 2)**2, 1., quad_nodes)
    return _covariance_decrement(np.clip(lower_drop / q, 0, 2), q, quad_nodes)


def predict(train_angles, labels, query_angles, t=np.inf, weights=None, quad_nodes=128):
    """Zero-start frozen-kernel gradient flow, including its t=infinity limit.

    The loss is sum_a weights[a]*(f[a]-labels[a])**2.  Weights default
    to 1/m, must be nonnegative and sum to one.  Zero-weight observations
    are omitted from the flow.  For t=infinity inconsistent labels in
    a numerical kernel nullspace raise ValueError; there is no ridge.
    Eigenvalues below 1e-12 of the maximum are treated as zero, and a
    negative eigenvalue below -2e-10 of the maximum is rejected.  Thus
    the interpolant has a stated finite-precision conditioning limit.
    """
    train = _real_array(train_angles, "train_angles")
    target = _real_array(labels, "labels")
    query = _real_array(query_angles, "query_angles")
    if train.ndim != 1 or train.size == 0 or target.shape != train.shape:
        raise ValueError("train_angles and labels must be nonempty matching vectors")
    if isinstance(t, (bool, np.bool_)) or not isinstance(t, Real) or np.isnan(t) or t < 0:
        raise ValueError("t must be a nonnegative real time or infinity")
    probability = (np.full(train.size, 1 / train.size) if weights is None
                   else _real_array(weights, "weights"))
    if (probability.shape != train.shape or np.any(probability < 0)
            or not np.isclose(probability.sum(), 1., rtol=0, atol=1e-12)):
        raise ValueError("weights must be nonnegative and sum to one")
    keep = probability > 0
    train, target, probability = train[keep], target[keep], probability[keep]
    root = np.sqrt(probability)
    gram = kernel(train[:, None] - train[None, :], quad_nodes)
    symmetric = root[:, None] * gram * root[None, :]
    eigenvalues, eigenvectors = np.linalg.eigh(symmetric)
    scale = max(float(eigenvalues[-1]), np.finfo(float).tiny)
    if eigenvalues[0] < -2e-10 * scale:
        raise ValueError("quadrature kernel fails the PSD tolerance; refine quadrature")
    eigenvalues = np.maximum(eigenvalues, 0)
    positive = eigenvalues > 1e-12 * scale
    coordinates = eigenvectors.T @ (root * target)
    if np.isinf(t):
        if np.linalg.norm(coordinates[~positive]) > 1e-9 * max(1., np.linalg.norm(target)):
            raise ValueError("labels cannot be interpolated at the numerical kernel rank")
        factors = np.zeros_like(eigenvalues)
        factors[positive] = 1 / eigenvalues[positive]
    else:
        # No rank truncation at finite times: the zero-eigenvalue factor
        # is the exact continuous extension 2*t.
        factors = np.full_like(eigenvalues, 2 * float(t))
        nonzero = eigenvalues > 0
        factors[nonzero] = -np.expm1(-2 * eigenvalues[nonzero] * t) / eigenvalues[nonzero]
    coefficients = root * (eigenvectors @ (factors * coordinates))
    cross = kernel(query.reshape(-1, 1) - train[None, :], quad_nodes)
    return (cross @ coefficients).reshape(query.shape)


def sample_kernel_power(grid_size=2048, quad_nodes=128):
    """Return periodic kernel samples and normalized complex Fourier power.

    coefficients[m]=M^-1 sum_j k(theta_j)*exp(-i*m*theta_j).
    Modes include negative integers in NumPy FFT order; power is the
    squared absolute coefficient with no positive/negative aggregation.
    """
    if (isinstance(grid_size, (bool, np.bool_))
            or not isinstance(grid_size, Integral) or grid_size < 8):
        raise ValueError("grid_size must be an integer at least 8")
    angles = 2 * np.pi * np.arange(grid_size) / grid_size
    values = kernel(angles, quad_nodes)
    coefficients = np.fft.fft(values) / grid_size
    return {"angles": angles, "values": values,
            "modes": np.rint(np.fft.fftfreq(grid_size) * grid_size).astype(int),
            "coefficients": coefficients, "power": np.abs(coefficients)**2}
