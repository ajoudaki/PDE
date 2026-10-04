"""Energy-consistent moving-Gram candidate; initialization contractions only.

This candidate preserves the *training* cubic response. Its passive query
extension does not preserve the orthogonal initial-readout contribution to
the arbitrary-query cubic response; see CUBIC_ENERGY_REPAIR_ROUTE_20260930.md.
No integration or training runs on import or when executed directly.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class GramQueryCoefficients:
    """S[q,e,c,f] is S0_((query_q,e),(train_c,f))."""

    cross_gram: np.ndarray
    initial_diagonal: np.ndarray
    response_gram: np.ndarray


class BoundedGramModel:
    """O(m²) training state plus m+1 passive states per initialized query.

    State order: training residual, packed upper-triangle K, then for each
    query its m cross-Gram entries and one diagonal entry. Query coordinates
    never affect the training RHS. Set gated=False for the matched g=1
    ablation. Both variants obey the exact surrogate readout-energy identity;
    only the gated variant has the feature-diagonal bound.
    """

    def __init__(self, labels, initial_gram, response_gram,
                 query_coefficients=None, *, gated=True):
        self.labels = np.asarray(labels, dtype=float).copy()
        self.initial_gram = np.asarray(initial_gram, dtype=float).copy()
        self.response_gram = np.asarray(response_gram, dtype=float).copy()
        self.m = len(self.labels)
        m = self.m
        if self.initial_gram.shape != (m, m):
            raise ValueError('Initial Gram shape does not match labels')
        if self.response_gram.shape != (m, m, m, m):
            raise ValueError('Response tensor shape does not match labels')
        if not np.allclose(self.initial_gram, self.initial_gram.T):
            raise ValueError('Initial Gram must be symmetric')
        np.linalg.cholesky(self.initial_gram)
        self.initial_slack = 1-np.diag(self.initial_gram)
        if np.min(self.initial_slack) <= 0:
            raise ValueError('Initial feature Gram diagonal must be below one')
        self.inverse_gram = np.linalg.solve(self.initial_gram, np.eye(m))
        self.alpha = 2/m
        self.gated = bool(gated)
        self.triangle = np.triu_indices(m)
        self.gram_size = len(self.triangle[0])
        self.training_size = m+self.gram_size
        self.query = query_coefficients
        self.query_count = 0
        if self.query is not None:
            self.query = GramQueryCoefficients(
                np.asarray(self.query.cross_gram, dtype=float).copy(),
                np.asarray(self.query.initial_diagonal, dtype=float).copy(),
                np.asarray(self.query.response_gram, dtype=float).copy())
            self.query_count = len(self.query.initial_diagonal)
            count = self.query_count
            if (self.query.cross_gram.shape != (count, m)
                    or self.query.response_gram.shape != (count, m, m, m)):
                raise ValueError('Query coefficient dimensions do not match')
            if np.any(self.query.initial_diagonal >= 1):
                raise ValueError('Initial query feature diagonal must be below one')
        self.size = self.training_size+self.query_count*(m+1)
        self.slices = (slice(0, m), slice(m, self.training_size),
                       slice(self.training_size, self.size))
        self.blocks = [sl for sl in self.slices if sl.stop > sl.start]

    def initial_state(self):
        state = np.zeros(self.size)
        state[:self.m] = -self.labels
        state[self.slices[1]] = self.initial_gram[self.triangle]
        if self.query_count:
            passive = state[self.slices[2]].reshape(self.query_count, self.m+1)
            passive[:, :self.m] = self.query.cross_gram
            passive[:, self.m] = self.query.initial_diagonal
        return state

    def unpack(self, state):
        residual = state[:self.m]
        gram = np.empty((self.m, self.m))
        gram[self.triangle] = state[self.slices[1]]
        gram[self.triangle[::-1]] = state[self.slices[1]]
        passive = state[self.slices[2]].reshape(self.query_count, self.m+1)
        return residual, gram, passive

    def residual(self, state):
        return np.asarray(state[:self.m])

    def _training_fields(self, residual, gram):
        prediction = self.labels+residual
        gate = ((1-np.diag(gram))/self.initial_slack
                if self.gated else np.ones(self.m))
        # w = A.T @ v, A=K K0^-1, v=K^-1 f; this expression avoids
        # solving the evolving Gram in the vector field.
        w = self.inverse_gram@prediction
        A = gram@self.inverse_gram
        T = -self.alpha*np.einsum('a,c,c,f,aecf->ea',
                                  gate, residual, gate, w,
                                  self.response_gram, optimize=True)
        C = self.inverse_gram@T
        tangent = np.einsum('a,c,e,f,aecf->ac', gate, gate, w, w,
                            self.response_gram, optimize=True)
        return gate, w, A, T, C, tangent

    def rhs(self, at, state):
        del at
        residual, gram, passive = self.unpack(state)
        gate, w, A, _, C, tangent = self._training_fields(residual, gram)
        result = np.empty_like(state)
        result[:self.m] = -self.alpha*((gram+tangent)@residual)
        gram_dot = gram@C+C.T@gram
        result[self.slices[1]] = gram_dot[self.triangle]
        if self.query_count:
            cross, diagonal = passive[:, :self.m], passive[:, self.m]
            query_gate = ((1-diagonal)/(1-self.query.initial_diagonal)
                          if self.gated else np.ones(self.query_count))
            Tx = -self.alpha*np.einsum('q,c,c,f,qecf->qe',
                                       query_gate, residual, gate, w,
                                       self.query.response_gram, optimize=True)
            passive_dot = result[self.slices[2]].reshape(
                self.query_count, self.m+1)
            passive_dot[:, :self.m] = cross@C+Tx@A.T
            passive_dot[:, self.m] = 2*np.einsum(
                'qe,qe->q', cross@self.inverse_gram, Tx)
        return result

    def predict(self, state):
        residual, gram, passive = self.unpack(state)
        readout = np.linalg.solve(gram, self.labels+residual)
        return passive[:, :self.m]@readout

    def readout_energy(self, state):
        residual, gram, _ = self.unpack(state)
        prediction = self.labels+residual
        return float(prediction@np.linalg.solve(gram, prediction))

    def diagnostics(self, state):
        residual, gram, passive = self.unpack(state)
        _, _, _, _, _, tangent = self._training_fields(residual, gram)
        prediction = self.labels+residual
        readout = np.linalg.solve(gram, prediction)
        energy = float(prediction@readout)
        query_prediction = passive[:, :self.m]@readout
        return dict(
            train_mse=float(np.mean(residual**2)),
            readout_energy=energy,
            energy_derivative=float(-2*self.alpha*(residual@prediction)),
            min_gram_eigenvalue=float(np.linalg.eigvalsh(gram)[0]),
            min_kernel_eigenvalue=float(np.linalg.eigvalsh(gram+tangent)[0]),
            maximum_train_diagonal=float(np.max(np.diag(gram))),
            maximum_query_diagonal=(float(np.max(passive[:, self.m]))
                                    if self.query_count else None),
            maximum_query_bound_excess=(float(np.max(query_prediction**2-energy))
                                       if self.query_count else None),
            maximum_query_schur_excess=(float(np.max(
                np.einsum('qa,aq->q', passive[:, :self.m],
                          np.linalg.solve(gram, passive[:, :self.m].T))
                -passive[:, self.m])) if self.query_count else None))


def training_alias_coefficients(initial_gram, response_gram):
    """Use the training points as queries, for an exact alias check."""
    return GramQueryCoefficients(np.asarray(initial_gram),
        np.diag(initial_gram), np.asarray(response_gram))


def check_structural_identities():
    """Algebraic checks on synthetic contractions; no ODE integration."""
    rng = np.random.default_rng(930)
    m = 3
    R = rng.normal(size=(m, m))
    K0 = .04*(R@R.T)+.1*np.eye(m)
    R = rng.normal(size=(m*m, 2*m*m))
    S = (R@R.T/(2*m*m)).reshape(m, m, m, m)
    aliases = training_alias_coefficients(K0, S)
    errors = {}
    for gated in (True, False):
        model = BoundedGramModel(np.array([1., -.7, .3]), K0, S,
                                 aliases, gated=gated)
        state = model.initial_state()
        state[:m] += np.array([.13, -.08, .02])
        derivative = model.rhs(0., state)
        residual, gram, passive = model.unpack(state)
        rdot, Kdot, pdot = model.unpack(derivative)
        f = model.labels+residual
        v = np.linalg.solve(gram, f)
        energy_dot = 2*v@rdot-v@Kdot@v
        expected = -2*model.alpha*(residual@f)
        alias_state = np.max(np.abs(model.predict(state)-f))
        alias_flow = max(np.max(np.abs(pdot[:, :m]-Kdot)),
                         np.max(np.abs(pdot[:, m]-np.diag(Kdot))))
        _, _, _, _, _, tangent = model._training_fields(residual, gram)
        psd_error = max(0., -np.linalg.eigvalsh(tangent)[0])
        errors['gated' if gated else 'ungated'] = dict(
            energy_identity_error=float(abs(energy_dot-expected)),
            alias_state_error=float(alias_state),
            alias_flow_error=float(alias_flow),
            tangent_psd_error=float(psd_error))
        assert max(abs(energy_dot-expected), alias_state,
                   alias_flow, psd_error) < 1e-12
    return errors


if __name__ == '__main__':
    print(check_structural_identities())
