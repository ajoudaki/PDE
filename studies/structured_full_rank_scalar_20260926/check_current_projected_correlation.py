"""Instantaneous algebra checks only; no ODE integration or training."""
from __future__ import annotations

import json
import numpy as np

from current_projected_correlation import initialize_with_queries, from_coefficients


def checks():
    rng = np.random.default_rng(20260930)
    n, m = 19, 3
    w = rng.normal(size=(n, 2))
    W = rng.normal(size=(n, n))/np.sqrt(n)
    inputs = rng.normal(size=(m, 2))
    labels = np.array([.8, -.6, .2])
    queries = np.vstack((inputs, rng.normal(size=(2, 2))))
    model = initialize_with_queries(w, W, inputs, labels, queries)
    state = model.initial_state()
    initial_dot = model.rhs(0., state)
    expected = -model.alpha*model.initial_gram@(-labels)
    iqdot = initial_dot[model.query_slice].reshape(len(queries), m+2)
    errors = {'zero_readout_rhs': float(np.max(abs(initial_dot[:m]-expected))),
              'zero_readout_training_geometry_rhs': float(np.max(abs(initial_dot[m:model.training_size]))),
              'zero_readout_query_geometry_rhs': float(max(np.max(abs(iqdot[:, :m])), np.max(abs(iqdot[:, m+1])))),
              'zero_readout_query_prediction_rhs': float(np.max(abs(iqdot[:, m]+model.alpha*model.query_cross@(-labels))))}
    h1 = np.tanh(inputs@w.T)
    d1 = 1-h1*h1
    beta_direct = np.empty((m, m))
    for a in range(m):
        for b in range(m):
            B = (h1[a]@h1[b]/n)*np.eye(n)+(inputs[a]@inputs[b])*((W*(d1[a]*d1[b]))@W.T)
            beta_direct[a, b] = np.trace(B)/n
    errors['beta_trace'] = float(np.max(abs(beta_direct-model.beta)))
    H = .3*rng.normal(size=(n, m))
    c = .2*rng.normal(size=n)
    HX = np.column_stack((H, .3*rng.normal(size=(n, 2))))
    K = H.T@H/n
    f = H.T@c/n
    q = c@c/n
    state[:m] = f-labels
    state[model.gram_slice] = K[model.triangle]
    state[model.q_index] = q
    passive = state[model.query_slice].reshape(len(queries), m+2)
    passive[:, :m] = HX.T@H/n
    passive[:, m] = HX.T@c/n
    passive[:, m+1] = np.mean(HX*HX, axis=0)
    r = f-labels
    cdot = -model.alpha*H@r
    D = [(1-K[a, a])*(np.eye(n)-model.lam[a]*np.outer(H[:, a], H[:, a])/n)
         for a in range(m)]
    Hdot = np.column_stack([-model.alpha*sum(r[b]*model.beta[a, b]*(D[a]@D[b]@c)
                                            for b in range(m)) for a in range(m)])
    HXdot = np.empty_like(HX)
    for x in range(len(queries)):
        Dx = (1-passive[x, m+1])*(np.eye(n)-model.query_lam[x]*np.outer(HX[:, x], HX[:, x])/n)
        HXdot[:, x] = -model.alpha*sum(r[b]*model.query_beta[x, b]*(Dx@D[b]@c)
                                      for b in range(m))
    actual = model.rhs(0., state)
    rebuilt = from_coefficients(model.coefficient_dict())
    errors['coefficient_restart_rhs'] = float(np.max(abs(actual-rebuilt.rhs(0., state))))
    expected = np.empty_like(actual)
    expected[:m] = (Hdot.T@c+H.T@cdot)/n
    expected[model.gram_slice] = ((Hdot.T@H+H.T@Hdot)/n)[model.triangle]
    expected[model.q_index] = 2*c@cdot/n
    exq = expected[model.query_slice].reshape(len(queries), m+2)
    exq[:, :m] = (HXdot.T@H+HX.T@Hdot)/n
    exq[:, m] = (HXdot.T@c+HX.T@cdot)/n
    exq[:, m+1] = 2*np.sum(HX*HXdot, axis=0)/n
    errors['explicit_operator_rhs'] = float(np.max(abs(actual-expected)))
    errors['alias_prediction'] = float(np.max(abs(model.predict(state)[:m]-f)))
    pqdot = actual[model.query_slice].reshape(len(queries), m+2)
    _, Kdot, _, _ = model.unpack(actual)
    errors['alias_cross_derivative'] = float(np.max(abs(pqdot[:m, :m]-Kdot)))
    errors['alias_output_derivative'] = float(np.max(abs(pqdot[:m, m]-actual[:m])))
    errors['alias_diagonal_derivative'] = float(np.max(abs(pqdot[:m, m+1]-np.diag(Kdot))))
    diag = model.diagnostics(state)
    errors['energy_identity'] = diag['energy_identity_residual']
    errors['prediction_identity'] = diag['prediction_identity_residual']
    errors['kernel_psd_violation'] = max(0., -diag['min_kernel_eigenvalue'])
    errors['gate_psd_violation'] = max(0., -diag['min_gate_gram_eigenvalue'])
    errors['augmented_psd_violation'] = max(0., -diag['min_augmented_gram_eigenvalue'])
    boundary = state.copy()
    boundary_K = K.copy()
    boundary_K[0, 0] = 1.
    boundary[model.gram_slice] = boundary_K[model.triangle]
    _, boundary_Kdot, _, _ = model.unpack(model.rhs(0., boundary))
    errors['saturation_boundary_tangent'] = float(abs(boundary_Kdot[0, 0]))
    empty = initialize_with_queries(w, W, inputs, labels, np.empty((0, 2)))
    assert empty.predict(empty.initial_state()).shape == (0,)
    assert model.training_size == m+m*(m+1)//2+1
    assert model.size == model.training_size+len(queries)*(m+2)
    assert max(errors.values()) < 1e-12, errors
    return {'status': 'PASS', 'scope': 'instantaneous algebra; no integration',
            'errors': errors, 'metadata': model.metadata}


if __name__ == '__main__':
    print(json.dumps(checks(), indent=2))
