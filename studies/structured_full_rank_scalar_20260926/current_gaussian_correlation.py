"""Frozen current Gaussian covariance closure; no neuron state in its RHS.

Scientific contract: CURRENT_CORRELATION_ROUTE_B_20260930.md.
Only the scalar radial tanh link uses fixed numerical quadrature.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.special import roots_legendre


class RadialTanhLink:
    """Positive one-dimensional quadrature with an exact link derivative."""

    def __init__(self, order=128):
        nodes, weights = roots_legendre(order)
        nodes = 6.0 * (nodes + 1.0)
        weights = 6.0 * weights * math.sqrt(2.0 / math.pi) * np.exp(-nodes**2 / 2.0)
        weights /= weights.sum()
        nodes /= math.sqrt(float(weights @ nodes**2))
        self.nodes, self.weights = nodes, weights
        self.order = int(order)

    def evaluate(self, variances):
        v = np.asarray(variances, dtype=float)
        if not np.all(np.isfinite(v)):
            raise FloatingPointError('nonfinite Gaussian variance')
        # Permit only rounding-sized violations of the exact PSD invariant.
        if np.min(v, initial=0.0) < -1e-10:
            raise FloatingPointError('negative Gaussian variance')
        v = np.maximum(v, 0.0)
        z = np.sqrt(v)[..., None] * self.nodes
        th = np.tanh(z)
        small = np.abs(z) < 1e-3
        zsafe = np.where(small, 1.0, z)
        a = th / zsafe
        b = (z * (1.0 - th * th) - th) / zsafe**3
        z2 = z * z
        # Removable-singularity evaluation of scalar functions only.
        a = np.where(small, 1.0 + z2 * (-1/3 + z2 * (2/15 - 17*z2/315)), a)
        b = np.where(small, -2/3 + z2 * (8/15 + z2 * (-34/105 + 496*z2/2835)), b)
        s = (a * self.nodes**2) @ self.weights
        t = (b * self.nodes**4) @ self.weights
        return s, t


class CurrentGaussianCorrelationModel:
    """Exact aggregate transport representation of the covariance candidate.

    Every query is decoded from the same m*m+m training state. The covariance
    derivation is unchanged; R and bcoef retain initial/current overlaps.
    """
    def __init__(self, labels, A, V0, query_A, query_V0, query_var0,
                 *, metadata=None, initial_tanh_gram=None,
                 link_nodes=None, link_weights=None):
        self.labels = np.asarray(labels, dtype=float).copy()
        self.m = len(self.labels)
        self.alpha = 2.0 / self.m
        self.A = np.asarray(A, dtype=float).copy()
        self.V0 = np.asarray(V0, dtype=float).copy()
        self.query_A = np.asarray(query_A, dtype=float).reshape(-1, self.m).copy()
        self.query_V0 = np.asarray(query_V0, dtype=float).reshape(-1, self.m).copy()
        self.query_var0 = np.asarray(query_var0, dtype=float).copy()
        self.nquery = len(self.query_var0)
        if self.A.shape != (self.m, self.m) or self.V0.shape != (self.m, self.m):
            raise ValueError('A and V0 must have shape (m,m)')
        if self.query_A.shape != (self.nquery, self.m) or self.query_V0.shape != (self.nquery, self.m):
            raise ValueError('inconsistent query coefficient shapes')
        eigA = np.linalg.eigvalsh(self.A)
        if eigA[0] <= 0:
            raise ValueError('transport candidate requires positive definite frozen A; no eigenvalue is discarded')
        self.query_l = np.linalg.solve(self.A, self.query_A.T).T
        self.link = RadialTanhLink(128)
        if link_nodes is not None:
            self.link.nodes = np.asarray(link_nodes, dtype=float).copy()
            self.link.weights = np.asarray(link_weights, dtype=float).copy()
            self.link.order = len(self.link.nodes)
        self.training_size = self.m*self.m+self.m
        self.size = self.training_size
        self.blocks = {'R': slice(0, self.m*self.m), 'bcoef': slice(self.m*self.m, self.size)}
        self.metadata = dict(metadata or {})
        self.metadata.update({'candidate': 'current_gaussian_correlation_B',
                              'representation': 'exact aggregate transport of Gaussian moment closure',
                              'quadrature_order': self.link.order, 'training_size': self.training_size,
                              'size': self.size, 'nquery': self.nquery, 'query_dynamic_size': 0,
                              'input_readout': 'exactly zero', 'dynamic_neurons_retained': 0,
                              'initial_covariance_min_eigenvalue': float(np.linalg.eigvalsh(self.V0)[0]),
                              'hidden_mobility_min_eigenvalue': float(eigA[0]),
                              'hidden_mobility_condition_number': float(eigA[-1]/eigA[0]),
                              'query_mobility_solve_maxabs_residual': float(np.max(np.abs(self.query_l @ self.A-self.query_A), initial=0.0))})
        self.initial_tanh_gram = None if initial_tanh_gram is None else np.asarray(initial_tanh_gram).copy()
        if self.initial_tanh_gram is not None:
            self.metadata.update(initial_kernel_diagnostics(self.V0, self.initial_tanh_gram, self.link))

    def initial_state(self):
        state = np.zeros(self.size)
        state[self.blocks['R']] = np.eye(self.m).ravel()
        return state

    def unpack(self, state):
        state = np.asarray(state)
        return state[self.blocks['R']].reshape(self.m, self.m), state[self.blocks['bcoef']]

    def moments(self, state):
        R, beta = self.unpack(state)
        initial_readout = self.V0 @ beta
        q = float(beta @ initial_readout)
        u = R.T @ initial_readout
        V = R.T @ self.V0 @ R
        return q, u, V

    def query_moments(self, state):
        R, beta = self.unpack(state)
        displacement = self.query_l @ (R-np.eye(self.m)).T
        initial_pairing = self.query_V0+displacement @ self.V0
        uq = initial_pairing @ beta
        varq = self.query_var0+2*np.sum(self.query_V0*displacement, axis=1)+np.sum((displacement @ self.V0)*displacement, axis=1)
        Vq = initial_pairing @ R
        return uq, varq, Vq

    def training_prediction(self, state):
        _, u, V = self.moments(state)
        s, _ = self.link.evaluate(np.diag(V))
        return u*s

    def residual(self, state):
        return self.training_prediction(state)-self.labels

    def predict(self, state):
        uq, varq, _ = self.query_moments(state)
        s, _ = self.link.evaluate(varq)
        return uq*s

    def rhs(self, time, state):
        del time
        R, beta = self.unpack(state)
        _, u, V = self.moments(state)
        s, t = self.link.evaluate(np.diag(V))
        r = u*s-self.labels
        rs = r*s
        Rdot = -self.alpha*(np.outer(beta, rs)+R*(r*u*t)[None, :]) @ self.A
        betadot = -self.alpha*(R @ rs)
        return np.r_[Rdot.ravel(), betadot]

    def tangent_kernel(self, state):
        q, u, V = self.moments(state)
        s, t = self.link.evaluate(np.diag(V))
        d, ut = u*u*t, u*t
        B = q*np.outer(s, s)+np.outer(s, d)+np.outer(d, s)+np.outer(ut, ut)*V
        return np.outer(s, s)*V+self.A*B

    def moment_derivatives(self, state):
        R, beta = self.unpack(state)
        Rdot, betadot = self.unpack(self.rhs(0, state))
        qdot = 2*float(beta @ self.V0 @ betadot)
        udot = Rdot.T @ self.V0 @ beta+R.T @ self.V0 @ betadot
        Vdot = Rdot.T @ self.V0 @ R+R.T @ self.V0 @ Rdot
        return qdot, udot, Vdot

    def diagnostics(self, state):
        q, u, V = self.moments(state)
        uq, vq, Vq = self.query_moments(state)
        qdot, udot, Vdot = self.moment_derivatives(state)
        s, t = self.link.evaluate(np.diag(V))
        f, r = u*s, u*s-self.labels
        theta = self.tangent_kernel(state)
        fdot = s*udot+0.5*u*t*np.diag(Vdot)
        covariance = np.block([[np.array([[q]]), u[None, :]], [u[:, None], V]])
        pred = self.predict(state)
        min_aug = float(np.linalg.eigvalsh(covariance)[0])
        for j in range(self.nquery):
            cross = np.r_[uq[j], Vq[j]]
            aug = np.block([[covariance, cross[:, None]], [cross[None, :], np.array([[vq[j]]])]])
            min_aug = min(min_aug, float(np.linalg.eigvalsh(aug)[0]))
        aliases = self.metadata.get('query_training_aliases', [-1]*self.nquery)
        alias_error = 0.0
        for j, a in enumerate(aliases):
            if a >= 0:
                alias_error = max(alias_error, abs(float(pred[j]-f[a])))
        # Compare to a second, univariate-only link evaluation; no state changes.
        scheck, tcheck = RadialTanhLink(256).evaluate(np.r_[np.diag(V), vq])
        sall, tall = self.link.evaluate(np.r_[np.diag(V), vq])
        return {'mse': float(np.mean(r*r)), 'q': q,
                'training_covariance_min_eigenvalue': float(np.linalg.eigvalsh(covariance)[0]),
                'augmented_covariance_min_eigenvalue': min_aug,
                'kernel_min_eigenvalue': float(np.linalg.eigvalsh(theta)[0]),
                'loss_derivative': float(-4/self.m**2*(r @ theta @ r)),
                'readout_energy_derivative_error': abs(float(qdot+2*self.alpha*(r @ f))),
                'prediction_derivative_error': float(np.max(np.abs(fdot+self.alpha*(theta @ r)))),
                'training_energy_bound_excess': float(max(0.0, np.max(f*f-q))),
                'query_energy_bound_excess': float(max(0.0, np.max(pred*pred-q, initial=0.0))),
                'training_alias_error': alias_error,
                'max_variance': float(max(np.max(np.diag(V)), np.max(vq, initial=0.0))),
                'quadrature_refinement_s_maxabs': float(np.max(np.abs(scheck-sall), initial=0.0)),
                'quadrature_refinement_t_maxabs': float(np.max(np.abs(tcheck-tall), initial=0.0)),
                'finite': bool(np.all(np.isfinite(state)) and np.all(np.isfinite(self.rhs(0, state))))}

    def coefficient_dict(self):
        import json
        result = {'labels': self.labels, 'A': self.A, 'V0': self.V0,
                  'query_A': self.query_A, 'query_V0': self.query_V0,
                  'query_var0': self.query_var0, 'link_nodes': self.link.nodes,
                  'link_weights': self.link.weights,
                  'metadata_json': np.array(json.dumps(self.metadata, sort_keys=True))}
        if self.initial_tanh_gram is not None:
            result['initial_tanh_gram'] = self.initial_tanh_gram
        return result


def from_coefficients(coefficients):
    import json
    metadata = json.loads(str(np.asarray(coefficients['metadata_json']).item())) if 'metadata_json' in coefficients else {}
    return CurrentGaussianCorrelationModel(coefficients['labels'], coefficients['A'], coefficients['V0'],
        coefficients['query_A'], coefficients['query_V0'], coefficients['query_var0'], metadata=metadata,
        initial_tanh_gram=coefficients.get('initial_tanh_gram'),
        link_nodes=coefficients.get('link_nodes'), link_weights=coefficients.get('link_weights'))


def initial_kernel_diagnostics(V0, K0, link):
    s, _ = link.evaluate(np.diag(V0))
    Klinear = np.outer(s, s)*V0
    vals, vecs = np.linalg.eigh(K0)
    direction = vecs[:, 0]
    ray = float(direction @ Klinear @ direction)
    scale = max(float(vals[0]), np.finfo(float).tiny)
    return {'initial_kernel_relative_frobenius_change': float(np.linalg.norm(Klinear-K0)/max(np.linalg.norm(K0), np.finfo(float).tiny)),
            'initial_tanh_kernel_min_eigenvalue': float(vals[0]),
            'initial_linear_kernel_min_eigenvalue': float(np.linalg.eigvalsh(Klinear)[0]),
            'initial_weak_direction_linear_rayleigh': ray,
            'initial_weak_direction_kernel_ratio': ray/scale,
            'initial_empirical_kernel_difference_min_eigenvalue': float(np.linalg.eigvalsh(K0-Klinear)[0])}


def initialize_with_queries(w, W, inputs, labels, queries, input_scale=1.0):
    """Contract initialization and release every width-dependent local array.

    Circle convention is input_scale=1. For the book convention use 1/sqrt(d).
    w has shape (n,d), W (n,n), inputs (m,d), queries (Q,d).
    """
    w, W = np.asarray(w, dtype=float), np.asarray(W, dtype=float)
    inputs, labels = np.asarray(inputs, dtype=float), np.asarray(labels, dtype=float)
    queries = np.asarray(queries, dtype=float).reshape(-1, inputs.shape[1])
    n, d = w.shape
    if W.shape != (n, n) or inputs.shape != (len(labels), d):
        raise ValueError('inconsistent network/input shapes')
    x = inputs * float(input_scale)
    xq = queries * float(input_scale)
    h1 = np.tanh(w @ x.T)
    d1 = 1-h1*h1
    z = W @ h1
    h = np.tanh(z)
    colnorms = np.sum(W*W, axis=0)
    K1 = h1.T @ h1 / n
    J1 = d1.T @ (colnorms[:, None]*d1) / n
    A = K1+(x @ x.T)*J1
    V0 = z.T @ z/n
    K0 = h.T @ h/n
    Q = len(queries)
    query_A = np.empty((Q, len(labels)))
    query_V0 = np.empty_like(query_A)
    query_var0 = np.empty(Q)
    # Batch width-dependent query temporaries without retaining them in the model.
    for start in range(0, Q, 64):
        stop = min(start+64, Q)
        h1q = np.tanh(w @ xq[start:stop].T)
        d1q = 1-h1q*h1q
        zq = W @ h1q
        query_A[start:stop] = h1q.T @ h1/n + (xq[start:stop] @ x.T)*(d1q.T @ (colnorms[:, None]*d1)/n)
        query_V0[start:stop] = zq.T @ z/n
        query_var0[start:stop] = np.sum(zq*zq, axis=0)/n
    aliases = []
    antipodes = []
    for query in queries:
        matches = np.flatnonzero(np.all(query[None, :]==inputs, axis=1))
        opposites = np.flatnonzero(np.all(query[None, :]==-inputs, axis=1))
        aliases.append(int(matches[0]) if len(matches) else -1)
        antipodes.append(int(opposites[0]) if len(opposites) else -1)
    metadata = {'width_used_only_for_initialization': n, 'input_dimension': d,
                'input_scale': float(input_scale), 'query_training_aliases': aliases,
                'query_antipodal_aliases': antipodes,
                'initial_hidden_mobility': 'exact initial trace, frozen scalar operator',
                'readout_preinitialization_variance': 0.0}
    model = CurrentGaussianCorrelationModel(labels, A, V0, query_A, query_V0, query_var0,
                                            metadata=metadata, initial_tanh_gram=K0)
    s, _ = model.link.evaluate(np.diag(V0))
    eps = h-z*s[None, :]
    residual_gram = eps.T @ eps/n
    cross = z.T @ eps/n
    values, vectors = np.linalg.eigh(K0)
    direction = vectors[:, 0]
    model.metadata.update({'initial_feature_projection_residual_gram_trace': float(np.trace(residual_gram)),
                           'initial_gaussian_regression_cross_norm': float(np.linalg.norm(cross)),
                           'initial_weak_direction_projection_residual_ratio': float(direction @ residual_gram @ direction/max(values[0], np.finfo(float).tiny)),
                           'initial_empirical_mean_maxabs': float(np.max(np.abs(np.mean(z, axis=0))))})
    return model
