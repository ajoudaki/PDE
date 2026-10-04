"""Current feature/readout covariance gate closure; no training on import.

Frozen theory: CURRENT_CORRELATION_ROUTE_A_20260930.md.
The state is a Gram matrix, never a population or collection of neurons.
"""
from __future__ import annotations

import numpy as np


class CurrentProjectedCorrelation:
    def __init__(self, labels, initial_gram, beta, query_cross, query_diagonal,
                 query_beta, *, metadata=None):
        self.labels = np.asarray(labels, dtype=float).copy()
        self.initial_gram = np.asarray(initial_gram, dtype=float).copy()
        self.beta = np.asarray(beta, dtype=float).copy()
        self.query_cross = np.asarray(query_cross, dtype=float).copy()
        self.query_diagonal = np.asarray(query_diagonal, dtype=float).copy()
        self.query_beta = np.asarray(query_beta, dtype=float).copy()
        self.m = len(self.labels)
        self.query_count = len(self.query_diagonal)
        m, nq = self.m, self.query_count
        if m == 0 or self.initial_gram.shape != (m, m) or self.beta.shape != (m, m):
            raise ValueError('Invalid training dimensions')
        if self.query_cross.shape != (nq, m) or self.query_beta.shape != (nq, m):
            raise ValueError('Invalid passive-query dimensions')
        arrays = (self.labels, self.initial_gram, self.beta, self.query_cross,
                  self.query_diagonal, self.query_beta)
        if not all(np.all(np.isfinite(a)) for a in arrays):
            raise ValueError('Nonfinite initialization')
        if not np.allclose(self.initial_gram, self.initial_gram.T):
            raise ValueError('Initial Gram must be symmetric')
        if not np.allclose(self.beta, self.beta.T):
            raise ValueError('Beta must be symmetric')
        if np.min(np.linalg.eigvalsh(self.initial_gram)) < -1e-10:
            raise ValueError('Initial Gram must be positive semidefinite')
        if np.min(np.linalg.eigvalsh(self.beta)) < -1e-10:
            raise ValueError('Beta must be positive semidefinite')
        self.initial_slack = 1-np.diag(self.initial_gram)
        self.query_initial_slack = 1-self.query_diagonal
        if np.any(self.initial_slack <= 0) or np.any(self.query_initial_slack <= 0):
            raise ValueError('Initial feature diagonals must be below one')
        self.lam = 2/self.initial_slack
        self.query_lam = 2/self.query_initial_slack
        self.alpha = 2/m
        self.triangle = np.triu_indices(m)
        self.gram_size = m*(m+1)//2
        self.training_size = m+self.gram_size+1
        self.size = self.training_size+nq*(m+2)
        self.gram_slice = slice(m, m+self.gram_size)
        self.q_index = m+self.gram_size
        self.query_slice = slice(self.training_size, self.size)
        self.blocks = [slice(0, m), self.gram_slice,
                       slice(self.q_index, self.q_index+1)]
        if nq:
            self.blocks.append(self.query_slice)
        self.metadata = dict(metadata or {})
        self.metadata.update(model='current_projected_correlation',
                             current_correlation='derived weighted gate Gram',
                             training_states=self.training_size,
                             passive_states_per_query=m+2,
                             total_states=self.size,
                             zero_initial_readout=True)

    def coefficient_dict(self):
        return {name: getattr(self, name) for name in
                ('labels', 'initial_gram', 'beta', 'query_cross',
                 'query_diagonal', 'query_beta')}

    def initial_state(self):
        state = np.zeros(self.size)
        state[:self.m] = -self.labels
        state[self.gram_slice] = self.initial_gram[self.triangle]
        if self.query_count:
            passive = state[self.query_slice].reshape(self.query_count, self.m+2)
            passive[:, :self.m] = self.query_cross
            passive[:, self.m+1] = self.query_diagonal
        return state

    def unpack(self, state):
        residual = state[:self.m]
        gram = np.empty((self.m, self.m))
        gram[self.triangle] = state[self.gram_slice]
        gram[self.triangle[::-1]] = state[self.gram_slice]
        passive = state[self.query_slice].reshape(self.query_count, self.m+2)
        return residual, gram, state[self.q_index], passive

    def residual(self, state):
        return np.asarray(state[:self.m])

    def _fields(self, residual, gram, q):
        f = self.labels+residual
        slack = 1-np.diag(gram)
        R = self.beta*slack[:, None]*slack[None, :]
        z = residual*self.lam*f
        t = R@residual
        diagonal = self.alpha*self.lam*(f*t-(R*gram)@z)
        A = self.alpha*z[:, None]*R+np.diag(diagonal)
        u = -self.alpha*t
        lf = self.lam*f
        gate_gram = slack[:, None]*slack[None, :]*(
            q-(self.lam*f*f)[:, None]-(self.lam*f*f)[None, :]
            +lf[:, None]*lf[None, :]*gram)
        tangent = self.beta*gate_gram
        return f, slack, z, A, u, gate_gram, tangent

    def rhs(self, at, state):
        del at
        r, K, q, passive = self.unpack(state)
        f, slack, z, A, u, _, tangent = self._fields(r, K, q)
        result = np.empty_like(state)
        result[:self.m] = -self.alpha*(K+tangent)@r
        Kdot = A.T@K+K@A+np.outer(u, f)+np.outer(f, u)
        result[self.gram_slice] = Kdot[self.triangle]
        result[self.q_index] = -2*self.alpha*(r@f)
        if self.query_count:
            cross = passive[:, :self.m]
            fx = passive[:, self.m]
            diagonal = passive[:, self.m+1]
            Rq = self.query_beta*(1-diagonal)[:, None]*slack[None, :]
            tq = Rq@r
            p = self.alpha*Rq*z[None, :]
            eta = self.alpha*self.query_lam*(fx*tq-np.sum(Rq*z*cross, axis=1))
            uq = -self.alpha*tq
            pdot = result[self.query_slice].reshape(self.query_count, self.m+2)
            pdot[:, :self.m] = (cross@A+fx[:, None]*u[None, :]+p@K
                                +eta[:, None]*cross+uq[:, None]*f[None, :])
            pdot[:, self.m] = (-self.alpha*(cross@r)+p@f+eta*fx+uq*q)
            pdot[:, self.m+1] = 2*(np.sum(cross*p, axis=1)+eta*diagonal+uq*fx)
        return result

    def predict(self, state):
        return self.unpack(state)[3][:, self.m].copy()

    def readout_energy(self, state):
        return float(state[self.q_index])

    def diagnostics(self, state):
        r, K, q, passive = self.unpack(state)
        f, _, _, A, u, G, N = self._fields(r, K, q)
        augmented = np.block([[K, f[:, None]], [f[None, :], np.array([[q]])]])
        generator = np.zeros((self.m+1, self.m+1))
        generator[:self.m, :self.m] = A
        generator[:self.m, self.m] = -self.alpha*r
        generator[self.m, :self.m] = u
        mdot = generator.T@augmented+augmented@generator
        expected_energy = -2*self.alpha*(r@f)
        fflow = -self.alpha*(K+N)@r
        mins = [float(np.linalg.eigvalsh(augmented)[0])]
        for row in passive:
            cross = np.r_[row[:self.m], row[self.m]]
            augq = np.block([[augmented, cross[:, None]],
                            [cross[None, :], np.array([[row[self.m+1]]])]])
            mins.append(float(np.linalg.eigvalsh(augq)[0]))
        return dict(train_mse=float(np.mean(r*r)), readout_energy=float(q),
                    energy_derivative=float(expected_energy),
                    energy_identity_residual=float(abs(mdot[-1, -1]-expected_energy)),
                    prediction_identity_residual=float(np.max(abs(mdot[:-1, -1]-fflow))),
                    min_gram_eigenvalue=float(np.linalg.eigvalsh(K)[0]),
                    min_augmented_gram_eigenvalue=min(mins),
                    min_kernel_eigenvalue=float(np.linalg.eigvalsh(K+N)[0]),
                    min_gate_gram_eigenvalue=float(np.linalg.eigvalsh(G)[0]),
                    maximum_train_diagonal=float(np.max(np.diag(K))),
                    maximum_query_diagonal=(float(np.max(passive[:, self.m+1]))
                                            if self.query_count else None),
                    maximum_query_bound_excess=(float(np.max(passive[:, self.m]**2-q))
                                               if self.query_count else None),
                    maximum_physical_gate_bound_excess=float(np.max(np.diag(G)-q)))


def initialize_with_queries(w, W, inputs, labels, queries):
    """Contract one exact initialized tanh realization; discard neural arrays.

    w has shape (n,d), W (n,n), inputs (m,d), queries (nq,d).
    The input preactivation is w @ x, without another dimension scaling.
    """
    w = np.asarray(w, dtype=float)
    W = np.asarray(W, dtype=float)
    inputs = np.asarray(inputs, dtype=float)
    queries = np.asarray(queries, dtype=float)
    if w.ndim != 2 or W.shape != (len(w), len(w)):
        raise ValueError('Invalid initialized weight shapes')
    if inputs.ndim != 2 or queries.ndim != 2 or inputs.shape[1] != w.shape[1] or queries.shape[1] != w.shape[1]:
        raise ValueError('Invalid input shapes')
    n = len(w)
    m = len(inputs)
    h1 = np.tanh(inputs@w.T)
    h2 = np.tanh(h1@W.T)
    d1 = 1-h1*h1
    column_norm = np.sum(W*W, axis=0)
    K0 = h2@h2.T/n
    beta = h1@h1.T/n+(inputs@inputs.T)*((d1*column_norm)@d1.T/n)
    nq = len(queries)
    cross = np.empty((nq, m))
    diagonal = np.empty(nq)
    query_beta = np.empty((nq, m))
    # Batches are transient initialization contractions, never evolving states.
    for start in range(0, nq, 64):
        stop = min(start+64, nq)
        qx = queries[start:stop]
        qh1 = np.tanh(qx@w.T)
        qh2 = np.tanh(qh1@W.T)
        qd1 = 1-qh1*qh1
        cross[start:stop] = qh2@h2.T/n
        diagonal[start:stop] = np.mean(qh2*qh2, axis=1)
        query_beta[start:stop] = qh1@h1.T/n+(qx@inputs.T)*((qd1*column_norm)@d1.T/n)
    return CurrentProjectedCorrelation(labels, K0, beta, cross, diagonal,
                                       query_beta, metadata={
                                           'width_used_only_in_initialization': int(n),
                                           'initializer_query_batch_size': 64,
                                           'beta': 'realized trace of exact initial preactivation response',
                                           'coefficient_provenance': 'initial weights and inputs only',
                                       })


def from_coefficients(coeff_dict):
    """Rebuild the identical scalar model without initialized neural arrays."""
    names = ('labels', 'initial_gram', 'beta', 'query_cross',
             'query_diagonal', 'query_beta')
    return CurrentProjectedCorrelation(**{name: coeff_dict[name] for name in names})
