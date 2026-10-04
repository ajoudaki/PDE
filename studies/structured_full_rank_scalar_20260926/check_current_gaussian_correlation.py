"""Deterministic algebraic checks. No ODE integration or network training."""
from __future__ import annotations

import json
import math
import time
import numpy as np
from scipy.integrate import quad

from current_gaussian_correlation import (
    RadialTanhLink, CurrentGaussianCorrelationModel,
    initialize_with_queries, from_coefficients,
)


def reference_link(v):
    if v == 0:
        return 1.0, -2.0
    if v <= 1:
        def integrand(x):
            th = math.tanh(math.sqrt(v)*x)
            gate = 1-th*th
            density = math.sqrt(2/math.pi)*math.exp(-x*x/2)
            return gate*density, (4*gate-6*gate*gate)*density
        return tuple(quad(lambda x: integrand(x)[j], 0, 12,
                          epsabs=2e-13, epsrel=2e-13)[0] for j in range(2))
    def integrand(z):
        expneg = math.exp(-2*z)
        gate = 4*expneg/(1+expneg)**2
        base = math.sqrt(2/(math.pi*v))*gate*math.exp(-z*z/(2*v))
        return base, base*(z*z/v**2-1/v)
    return tuple(quad(lambda z: integrand(z)[j], 0, 30,
                      epsabs=2e-13, epsrel=2e-13)[0] for j in range(2))


def check():
    start = time.perf_counter()
    report = {'scope': 'deterministic algebra and scalar quadrature; no fitting'}
    variances = np.r_[0., 1e-12, 1e-8, 1e-4, .01, .1, .5, 1., 2., 5., 10., 25., 100., 300., 1000.]
    link = RadialTanhLink(128)
    s, t = link.evaluate(variances)
    s2, t2 = RadialTanhLink(256).evaluate(variances)
    references = np.array([reference_link(v) for v in variances])
    report['scalar_quadrature_variance_max'] = 1000.
    report['scalar_quadrature_s_maxabs_error'] = float(np.max(abs(s-references[:, 0])))
    report['scalar_quadrature_t_maxabs_error'] = float(np.max(abs(t-references[:, 1])))
    report['scalar_quadrature_refinement_maxabs'] = float(max(np.max(abs(s-s2)), np.max(abs(t-t2))))
    assert report['scalar_quadrature_s_maxabs_error'] < 1e-9
    assert report['scalar_quadrature_t_maxabs_error'] < 1e-9

    rng = np.random.default_rng(290930)
    n, m, d = 23, 3, 2
    w = rng.normal(size=(n, d))
    W = rng.normal(size=(n, n))/math.sqrt(n)
    angles = np.array([.1, .7, 1.6])
    inputs = np.column_stack((np.cos(angles), np.sin(angles)))
    labels = np.array([1., -.4, .6])
    queries = np.vstack((inputs, -inputs, [[.2, .9], [-.8, .1]]))
    model = initialize_with_queries(w, W, inputs, labels, queries, input_scale=1.)
    assert model.size == model.training_size == m*m+m
    h1 = np.tanh(w @ inputs.T)
    d1 = 1-h1*h1
    K1 = h1.T @ h1/n
    G = inputs @ inputs.T
    trace_error = 0.
    for a in range(m):
        for b in range(m):
            exact = K1[a, b]*np.eye(n)+G[a, b]*(W*(d1[:, a]*d1[:, b])[None, :]) @ W.T
            trace_error = max(trace_error, abs(float(np.trace(exact)/n-model.A[a, b])))
    report['initial_hidden_operator_trace_error'] = trace_error
    assert trace_error < 1e-12

    maxima = {key: 0. for key in ['moment_derivative_error', 'query_moment_derivative_error',
                                  'energy_derivative_error', 'prediction_derivative_error',
                                  'training_alias_error', 'training_alias_derivative_error',
                                  'antipodal_error', 'bound_excess', 'link_gradient_fd_error']}
    min_kernel = math.inf
    for _ in range(12):
        R = np.eye(m)+.25*rng.normal(size=(m, m))
        beta = .5*rng.normal(size=m)
        state = np.r_[R.ravel(), beta]
        Rdot, betadot = model.unpack(model.rhs(0, state))
        q, u, V = model.moments(state)
        qdot, udot, Vdot = model.moment_derivatives(state)
        uq, vq, Vq = model.query_moments(state)
        s, t = model.link.evaluate(np.diag(V))
        r = u*s-labels
        # Independent literal indexed implementation of covariance eq. (7).
        udot_ref = np.zeros(m)
        Vdot_ref = np.zeros((m, m))
        for a in range(m):
            for b in range(m):
                udot_ref[a] -= model.alpha*r[b]*(V[a, b]*s[b]+model.A[a, b]*(q*s[b]+u[b]**2*t[b]))
                for e in range(m):
                    Vdot_ref[a, e] -= model.alpha*r[b]*(
                        model.A[a, b]*(u[e]*s[b]+u[b]*V[e, b]*t[b])
                        +model.A[e, b]*(u[a]*s[b]+u[b]*V[a, b]*t[b]))
        maxima['moment_derivative_error'] = max(maxima['moment_derivative_error'], float(np.max(abs(udot-udot_ref))), float(np.max(abs(Vdot-Vdot_ref))))
        # Direct derivative of the algebraic decoder, checked against eq. (13).
        disp = model.query_l @ (R-np.eye(m)).T
        dispdot = model.query_l @ Rdot.T
        pair = model.query_V0+disp @ model.V0
        pairdot = dispdot @ model.V0
        uqdot = pairdot @ beta+pair @ betadot
        vqdot = 2*np.sum(pair*dispdot, axis=1)
        Vqdot = pairdot @ R+pair @ Rdot
        sq, tq = model.link.evaluate(vq)
        qfdot = sq*uqdot+.5*uq*tq*vqdot
        fdot = s*udot+.5*u*t*np.diag(Vdot)
        for j in range(model.nquery):
            uqref = -model.alpha*sum(r[b]*(Vq[j, b]*s[b]+model.query_A[j, b]*(q*s[b]+u[b]**2*t[b])) for b in range(m))
            vqref = -2*model.alpha*sum(model.query_A[j, b]*r[b]*(uq[j]*s[b]+u[b]*Vq[j, b]*t[b]) for b in range(m))
            crossref = np.array([-model.alpha*sum(r[b]*(model.query_A[j, b]*(u[a]*s[b]+u[b]*V[a, b]*t[b])+model.A[a, b]*(uq[j]*s[b]+u[b]*Vq[j, b]*t[b])) for b in range(m)) for a in range(m)])
            maxima['query_moment_derivative_error'] = max(maxima['query_moment_derivative_error'], abs(float(uqdot[j]-uqref)), abs(float(vqdot[j]-vqref)), float(np.max(abs(Vqdot[j]-crossref))))
        theta = model.tangent_kernel(state)
        min_kernel = min(min_kernel, float(np.linalg.eigvalsh(theta)[0]))
        maxima['energy_derivative_error'] = max(maxima['energy_derivative_error'], abs(float(qdot+2*model.alpha*(r @ (u*s)))))
        maxima['prediction_derivative_error'] = max(maxima['prediction_derivative_error'], float(np.max(abs(fdot+model.alpha*(theta @ r)))))
        predictions = model.predict(state)
        maxima['training_alias_error'] = max(maxima['training_alias_error'], float(np.max(abs(predictions[:m]-u*s))))
        maxima['training_alias_derivative_error'] = max(maxima['training_alias_derivative_error'], float(np.max(abs(qfdot[:m]-fdot))))
        maxima['antipodal_error'] = max(maxima['antipodal_error'], float(np.max(abs(predictions[m:2*m]+u*s))))
        maxima['bound_excess'] = max(maxima['bound_excess'], float(np.max(predictions**2-q)), float(np.max((u*s)**2-q)))
        eps = 1e-6
        numerical = (model.training_prediction(state+eps*model.rhs(0, state))-model.training_prediction(state-eps*model.rhs(0, state)))/(2*eps)
        maxima['link_gradient_fd_error'] = max(maxima['link_gradient_fd_error'], float(np.max(abs(numerical-fdot))))

    report.update(maxima)
    report['kernel_min_eigenvalue_over_checks'] = min_kernel
    assert min_kernel > -1e-10
    for key, value in maxima.items():
        assert value < (1e-7 if key == 'link_gradient_fd_error' else 2e-9), (key, value)
    noquery = CurrentGaussianCorrelationModel(labels, model.A, model.V0,
                        np.empty((0, m)), np.empty((0, m)), np.empty(0))
    report['query_independence_exact'] = bool(np.array_equal(model.rhs(0, state), noquery.rhs(0, state)))
    assert report['query_independence_exact']
    reconstructed = from_coefficients(model.coefficient_dict())
    report['coefficient_roundtrip_rhs_exact'] = bool(np.array_equal(model.rhs(0, state), reconstructed.rhs(0, state)))
    report['coefficient_roundtrip_query_exact'] = bool(np.array_equal(model.predict(state), reconstructed.predict(state)))
    assert report['coefficient_roundtrip_rhs_exact'] and report['coefficient_roundtrip_query_exact']
    report['training_size'] = model.training_size
    report['query_dynamic_size'] = 0
    report['initial_state_diagnostics'] = model.diagnostics(model.initial_state())
    report['elapsed_seconds'] = time.perf_counter()-start
    report['status'] = 'PASS'
    return report


if __name__ == '__main__':
    print(json.dumps(check(), indent=2, sort_keys=True))
