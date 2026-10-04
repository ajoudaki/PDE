"""One terminal-cubic response mode in an autonomous scalar bilinear GF.

Constructor access to initial weights is explicit and temporary. Returned
models and query coefficients contain no width-dependent fields or weights.
No training runs on import; this module deliberately has no integrator.
See CUBIC_MINIMAL_MODE_ROUTE_20260930.md for scope and cubic limitations.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.linalg import cho_solve


def _array(value, name, ndim):
    value = np.asarray(value, dtype=float)
    if value.ndim != ndim or not np.all(np.isfinite(value)):
        raise ValueError(f'{name} must be a finite {ndim}-dimensional array')
    return value


def _gram_factor(gram):
    values = np.linalg.eigvalsh(gram)
    if (values[0] <= 0 or not np.all(np.isfinite(values))
            or values[-1]/values[0] > 1e12):
        raise ValueError(f'Readout Gram fails conditioning gate: {values}')
    return np.linalg.cholesky(gram)


def _initial_fields(w, W, inputs):
    first = np.tanh(inputs @ w.T)
    second = np.tanh(first @ W.T)
    return first, second, 1-first*first, 1-second*second


def _responses(W, first_gate, second_gate, basis):
    m, n = first_gate.shape
    p = len(basis)
    gamma = second_gate[:, None, :]*basis[None, :, :]
    beta = ((gamma.reshape(m*p, n) @ W).reshape(m, p, n)
            * first_gate[:, None, :])
    return gamma, beta


def _coefficient_workspace(w, W, inputs, labels):
    """Private constructor workspace; no returned object retains this."""
    w, W = _array(w, 'w', 2), _array(W, 'W', 2)
    inputs, labels = _array(inputs, 'inputs', 2), _array(labels, 'labels', 1)
    if (w.shape[0] < 1 or len(inputs) < 1 or w.shape[1] != inputs.shape[1]
            or W.shape != (len(w), len(w)) or labels.shape != (len(inputs),)):
        raise ValueError('Incompatible weight, input, or label shapes')
    first, H, q, d = _initial_fields(w, W, inputs)
    m, n = H.shape
    K = H @ H.T/n
    factor = _gram_factor(K)
    gamma, beta = _responses(W, q, d, H)
    norm_y = np.linalg.norm(labels)
    metadata = dict(selection='fixed_kernel_terminal_cubic',
                    mode_status='zero_labels', mode_relative_norm=0.,
                    mode_orthogonality=0.)
    basis = H
    if norm_y > 0:
        values, vectors = np.linalg.eigh(K)
        # All positive common scalings disappear when the mode is normalized.
        values = values/values[0]
        projected = vectors.T @ (labels/norm_y)
        B = (projected[:, None, None]*projected[None, :, None]
             * projected[None, None, :]
             / (values[:, None, None]
                * (values[:, None, None]+values[None, :, None])
                * (values[:, None, None]+values[None, :, None]
                   + values[None, None, :])))
        B /= np.max(np.abs(B))
        B = np.einsum('ai,bj,ck,ijk->abc', vectors, vectors, vectors, B,
                      optimize=True)
        dot, first_gram = inputs @ inputs.T, first @ first.T/n
        raw = np.zeros(n)
        for a in range(m):
            t = np.einsum('bc,b,bcn->n', B[a], dot[a], beta,
                          optimize=True)
            s = np.einsum('bc,b,bcn->n', B[a], first_gram[a], gamma,
                          optimize=True)
            raw += d[a]*(W @ (q[a]*t)+s)
        raw_norm = np.linalg.norm(raw)/np.sqrt(n)
        orthogonal = raw.copy()
        for _ in range(2):
            projection = cho_solve((factor, True), H @ orthogonal/n,
                                   check_finite=False)
            orthogonal -= projection @ H
        mode_norm = np.linalg.norm(orthogonal)/np.sqrt(n)
        if raw_norm == 0:
            metadata['mode_status'] = 'exact_zero_response'
        elif mode_norm <= 1e-12*raw_norm:
            raise ValueError('Terminal response mode is numerically unresolved')
        else:
            mode = orthogonal/mode_norm
            basis = np.vstack((H, mode))
            metadata.update(mode_status='one_mode',
                            mode_relative_norm=float(mode_norm/raw_norm),
                            mode_orthogonality=float(np.max(np.abs(H @ mode/n))))
            gamma, beta = _responses(W, q, d, basis)
    return inputs, labels, first, H, q, d, basis, gamma, beta, metadata


@dataclass
class QueryCoefficients:
    cross_gram: np.ndarray  # (number of queries, p)
    response: np.ndarray  # (number of queries, p, m, p)

    @property
    def nbytes(self):
        return self.cross_gram.nbytes+self.response.nbytes


@dataclass
class MinimalModeModel:
    labels: np.ndarray
    readout_gram: np.ndarray
    training_cross_gram: np.ndarray
    response_gram: np.ndarray
    metadata: dict

    def __post_init__(self):
        self.labels = _array(self.labels, 'labels', 1).copy()
        self.readout_gram = _array(self.readout_gram, 'readout_gram', 2).copy()
        self.training_cross_gram = _array(
            self.training_cross_gram, 'training_cross_gram', 2).copy()
        self.response_gram = _array(self.response_gram, 'response_gram', 4).copy()
        self.metadata = dict(self.metadata)
        self.m = len(self.labels)
        self.p = len(self.readout_gram)
        if (self.m < 1 or self.p not in (self.m, self.m+1)
                or self.readout_gram.shape != (self.p, self.p)
                or self.training_cross_gram.shape != (self.m, self.p)
                or self.response_gram.shape != (self.m, self.p, self.m, self.p)):
            raise ValueError('Scalar coefficient dimensions do not agree')
        self.cholesky = _gram_factor(self.readout_gram)
        self.alpha = 2/self.m
        self.size = self.p*(self.m+1)
        self.slices = (slice(0, self.p), slice(self.p, self.size))

    @property
    def training_size(self):
        return self.size

    @property
    def coefficient_nbytes(self):
        return sum(a.nbytes for a in (self.labels, self.readout_gram,
                   self.training_cross_gram, self.response_gram, self.cholesky))

    def initial_state(self):
        return np.zeros(self.size)

    def unpack(self, state):
        return state[:self.p], state[self.p:].reshape(self.m, self.p)

    def solve_gram(self, rhs):
        return cho_solve((self.cholesky, True), rhs, check_finite=False)

    def feature_matrix(self, theta):
        return (self.training_cross_gram
                + np.einsum('aibj,bj->ai', self.response_gram, theta,
                            optimize=True))

    def training_prediction(self, state):
        v, theta = self.unpack(state)
        return self.feature_matrix(theta) @ v

    def residual(self, state):
        return self.training_prediction(state)-self.labels

    def rhs(self, at, state):
        v, theta = self.unpack(state)
        features = self.feature_matrix(theta)
        residual = features @ v-self.labels
        return np.concatenate((
            -self.alpha*self.solve_gram(features.T @ residual),
            (-self.alpha*np.outer(residual, v)).ravel()))

    def kernel(self, state):
        v, theta = self.unpack(state)
        features = self.feature_matrix(theta)
        return (features @ self.solve_gram(features.T)
                + np.einsum('i,j,aibj->ab', v, v, self.response_gram,
                            optimize=True))

    def readout_energy(self, state):
        v, _ = self.unpack(state)
        return float(v @ self.readout_gram @ v)

    def predict(self, state, coefficients):
        v, theta = self.unpack(state)
        if (coefficients.cross_gram.shape[1:] != (self.p,)
                or coefficients.response.shape != (
                    len(coefficients.cross_gram), self.p, self.m, self.p)):
            raise ValueError('Query coefficients do not match model')
        return ((coefficients.cross_gram
                 + np.einsum('qibj,bj->qi', coefficients.response, theta,
                             optimize=True)) @ v)


def initialize(w, W, inputs, labels):
    """Build a width-free model from the initial hidden network and labels.

    The initial readout is zero regardless of any readout in a caller's
    network. Construction raises rather than normalizing an unresolved mode.
    """
    (inputs, labels, first, H, _, _, basis, gamma, beta,
     metadata) = _coefficient_workspace(w, W, inputs, labels)
    m, n = H.shape
    p = len(basis)
    flat_beta, flat_gamma = beta.reshape(m*p, n), gamma.reshape(m*p, n)
    response = (
        (flat_beta @ flat_beta.T/n).reshape(m, p, m, p)
        * (inputs @ inputs.T)[:, None, :, None]
        + (flat_gamma @ flat_gamma.T/n).reshape(m, p, m, p)
        * (first @ first.T/n)[:, None, :, None])
    return MinimalModeModel(labels, basis @ basis.T/n, H @ basis.T/n,
                            response, metadata)


def query_coefficients(w, W, inputs, queries, labels, *, batch_size=16):
    """One-time passive coefficients; regenerates the same initial mode.

    Call during coefficient construction while initial weights are available.
    Query count and query values never enter the training model or mode choice.
    """
    (inputs, _, first, H, _, _, basis, gamma, beta,
     _) = _coefficient_workspace(w, W, inputs, labels)
    queries = _array(queries, 'queries', 2)
    if queries.shape[1] != inputs.shape[1]:
        raise ValueError('Query and input dimensions must agree')
    if not isinstance(batch_size, int) or isinstance(batch_size, bool) or batch_size < 1:
        raise ValueError('batch_size must be a positive integer')
    m, n = H.shape
    p = len(basis)
    cross = np.empty((len(queries), p))
    response = np.empty((len(queries), p, m, p))
    beta_flat, gamma_flat = beta.reshape(m*p, n), gamma.reshape(m*p, n)
    for start in range(0, len(queries), batch_size):
        stop = min(start+batch_size, len(queries))
        points = queries[start:stop]
        query_first, query_H, q, d = _initial_fields(np.asarray(w), np.asarray(W), points)
        query_gamma, query_beta = _responses(np.asarray(W), q, d, basis)
        length = len(points)
        cross[start:stop] = query_H @ basis.T/n
        response[start:stop] = (
            (query_beta.reshape(length*p, n) @ beta_flat.T/n)
            .reshape(length, p, m, p)*(points @ inputs.T)[:, None, :, None]
            + (query_gamma.reshape(length*p, n) @ gamma_flat.T/n)
            .reshape(length, p, m, p)*(query_first @ first.T/n)[:, None, :, None])
    return QueryCoefficients(cross, response)


def bounded_gram_coefficients(w, W, inputs, labels, queries, *, batch_size=16):
    """Initial scalar coefficients for the supervisor's gated overlap model.

    Returns exactly G, R0, S, kx, query_B, querydiag, mode_metadata.
    R0 has shape (p,m); query_B has shape (q,p,m,p). The response mode
    uses labels and initial hidden weights only. There is no integration.
    """
    (inputs, labels, first, H, _, _, basis, gamma, beta,
     metadata) = _coefficient_workspace(w, W, inputs, labels)
    queries = _array(queries, 'queries', 2)
    if queries.shape[1] != inputs.shape[1]:
        raise ValueError('Query and input dimensions must agree')
    if not isinstance(batch_size, int) or isinstance(batch_size, bool) or batch_size < 1:
        raise ValueError('batch_size must be a positive integer')
    m, n = H.shape
    p = len(basis)
    G = basis @ basis.T/n
    _gram_factor(G)
    R0 = np.zeros((p, m))
    R0[:m] = np.eye(m)
    beta_flat, gamma_flat = beta.reshape(m*p, n), gamma.reshape(m*p, n)
    S = ((beta_flat @ beta_flat.T/n).reshape(m, p, m, p)
         * (inputs @ inputs.T)[:, None, :, None]
         + (gamma_flat @ gamma_flat.T/n).reshape(m, p, m, p)
         * (first @ first.T/n)[:, None, :, None])
    kx = np.empty((len(queries), p))
    query_B = np.empty((len(queries), p, m, p))
    querydiag = np.empty(len(queries))
    for start in range(0, len(queries), batch_size):
        stop = min(start+batch_size, len(queries))
        points = queries[start:stop]
        query_first, query_H, q, d = _initial_fields(np.asarray(w), np.asarray(W), points)
        query_gamma, query_beta = _responses(np.asarray(W), q, d, basis)
        length = len(points)
        kx[start:stop] = query_H @ basis.T/n
        querydiag[start:stop] = np.mean(query_H*query_H, axis=1)
        query_B[start:stop] = (
            (query_beta.reshape(length*p, n) @ beta_flat.T/n)
            .reshape(length, p, m, p)*(points @ inputs.T)[:, None, :, None]
            + (query_gamma.reshape(length*p, n) @ gamma_flat.T/n)
            .reshape(length, p, m, p)*(query_first @ first.T/n)[:, None, :, None])
    return dict(G=G, R0=R0, S=S, kx=kx, query_B=query_B,
                querydiag=querydiag, mode_metadata=metadata)
