"""Deterministic Hessian/gradient/constructor checks; no training solves."""
import json
from pathlib import Path
import resource
import time

import numpy as np

import cubic_minimal_mode_repair as minimal
import cubic_quadratic_feature_repair as quadratic


def finite_features(w,W,points):
    return np.tanh(np.tanh(points @ w.T) @ W.T)


def check_case(extra_mode):
    rng = np.random.default_rng(20260930)
    n,m = 40,3
    angles = np.array([0.,.7,1.8])
    inputs = np.stack((np.cos(angles),np.sin(angles)),axis=1)
    labels = np.array([.5,-.3,.8])
    queries = np.vstack((inputs,[np.cos(.4),np.sin(.4)]))
    w,W = rng.normal(size=(n,2)),rng.normal(size=(n,n))/np.sqrt(n)
    model,query = quadratic.initialize_with_queries(w,W,inputs,labels,queries,
                                                     extra_mode=extra_mode)
    (inputs,_,first,H,basis,gamma,beta,S,U,
     _) = quadratic._workspace(w,W,inputs,labels,extra_mode)
    p,rank = model.p,model.d
    first_repeated = np.repeat(first,p,axis=0)
    inputs_repeated = np.repeat(inputs,p,axis=0)
    dw_basis = np.einsum('jl,jn,jk->lnk',U,beta,inputs_repeated)
    dW_basis = np.einsum('jl,jn,jk->lnk',U,gamma,first_repeated)/n
    physical_gram = (np.einsum('lnk,snk->ls',dw_basis,dw_basis)/n
                     +np.einsum('lnk,snk->ls',dW_basis,dW_basis))
    direction1,direction2 = rng.normal(size=(2,rank))
    direction1 /= np.linalg.norm(direction1)
    direction2 /= np.linalg.norm(direction2)
    Xw,XW = np.einsum('l,lnk->nk',direction1,dw_basis),np.einsum('l,lnk->nk',direction1,dW_basis)
    Yw,YW = np.einsum('l,lnk->nk',direction2,dw_basis),np.einsum('l,lnk->nk',direction2,dW_basis)
    hessian = np.einsum('qilk,l,k->qi',query.quadratic,direction1,direction2)
    hessian_errors = []
    for h in (.002,.001,.0005):
        mixed = np.zeros((len(queries),n))
        for sign1,sign2 in ((1,1),(1,-1),(-1,1),(-1,-1)):
            mixed += sign1*sign2*finite_features(
                w+h*(sign1*Xw+sign2*Yw),W+h*(sign1*XW+sign2*YW),queries)
        finite_difference = mixed @ basis.T/(4*h*h*n)
        hessian_errors.append(float(np.max(np.abs(finite_difference-hessian))))
    assert hessian_errors[-1] < 2e-6,hessian_errors
    assert hessian_errors[-1] < .15*hessian_errors[0],hessian_errors

    state = np.concatenate((rng.normal(size=p)*.2,rng.normal(size=rank)*.03))
    v,eta = model.unpack(state)
    rhs = model.rhs(0.,state)
    vdot,etadot = model.unpack(rhs)
    features = model._features(eta,model.coefficients)
    jacobian = model._hidden_jacobian(v,eta)
    residual = model.residual(state)
    direct_derivative = features @ vdot+jacobian @ etadot
    kernel = model.kernel(state)
    model_linear = quadratic.QuadraticFeatureModel(labels,model.readout_gram,
        model.coefficients,1,model.metadata)
    theta = (U @ eta).reshape(m,p)
    # Independent dense reconstruction of the linear-feature prediction.
    dw = np.einsum('l,lnk->nk',eta,dw_basis)
    dW = np.einsum('l,lnk->nk',eta,dW_basis)
    q,d = 1-first*first,1-H*H
    L = d*((q*(inputs @ dw.T)) @ W.T+first @ dW.T)
    linear_direct = (H+L) @ (v @ basis)/n
    lifted = quadratic.lifted_endpoint_diagnostic(w,W,inputs,labels,queries,state,
                                                   extra_mode=extra_mode)
    direct_lift = finite_features(w+dw,W+dW,queries) @ (v @ basis)/n
    loss_derivative = 2*np.dot(residual,direct_derivative)/m
    speed2 = vdot @ model.readout_gram @ vdot+etadot @ etadot
    delta = rng.normal(size=model.size)
    epsilon = 1e-6
    finite_loss_derivative = (np.mean(model.residual(state+epsilon*delta)**2)
                              -np.mean(model.residual(state-epsilon*delta)**2))/(2*epsilon)
    analytic_loss_derivative = -(vdot @ model.readout_gram @ delta[:p]+etadot @ delta[p:])
    results = dict(extra_mode=extra_mode,p=p,rank=rank,state_size=model.size,
        hessian_mixed_finite_difference_errors=hessian_errors,
        whitening_physical_error=float(np.max(np.abs(physical_gram-np.eye(rank)))),
        hessian_symmetry_error=float(np.max(np.abs(query.quadratic-query.quadratic.swapaxes(-1,-2)))),
        query_alias_error=float(np.max(np.abs(model.predict(state,query)[:m]-model.training_prediction(state)))),
        kernel_identity_error=float(np.max(np.abs(direct_derivative+model.alpha*kernel @ residual))),
        kernel_min_eigenvalue=float(np.linalg.eigvalsh(kernel)[0]),
        loss_identity_error=float(abs(loss_derivative+speed2)),
        loss_gradient_finite_difference_error=float(abs(finite_loss_derivative-analytic_loss_derivative)),
        readout_energy_identity_error=float(abs(2*v @ model.readout_gram @ vdot+2*model.alpha*residual @ (features @ v))),
        degree_one_direct_error=float(np.max(np.abs(linear_direct-model_linear.training_prediction(state)))),
        lifted_direct_error=float(np.max(np.abs(direct_lift-lifted['prediction']))),
        lifted_metric_error=float(abs(lifted['hidden_metric_norm']-np.linalg.norm(eta))),
        lifted_fingerprint_matches=lifted['basis_whitening_sha256']==model.metadata['basis_whitening_sha256'],
        linear_contraction_error=model.metadata['linear_contraction_error'])
    for name,value in results.items():
        if name.endswith('_error'):
            assert value < 1e-9,(name,value)
    assert results['kernel_min_eigenvalue'] > 0
    assert results['lifted_fingerprint_matches']
    return results


checks = [check_case(False),check_case(True)]
n,m = 1024,6
angles = np.linspace(0,2.4,m)
inputs = np.stack((np.cos(angles),np.sin(angles)),axis=1)
labels = np.sin(3*angles)+.3*np.cos(angles)
query_angles = np.linspace(0,2*np.pi,256,endpoint=False)
queries = np.vstack((np.stack((np.cos(query_angles),np.sin(query_angles)),axis=1),inputs))
w = np.random.default_rng(np.random.SeedSequence([1,1])).normal(size=(n,2))
W = np.random.default_rng(np.random.SeedSequence([1,101])).normal(size=(n,n))/np.sqrt(n)
started = time.monotonic()
model,query = quadratic.initialize_with_queries(w,W,inputs,labels,queries,extra_mode=True)
timing = dict(seconds=time.monotonic()-started,model_metadata=model.metadata,
              state_size=model.size,query_count=len(queries),
              maximum_resident_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024)
assert timing['seconds'] < 30,timing
assert timing['maximum_resident_bytes'] < 2*1024**3,timing
result = dict(checks=checks,constructor_width_1024_m6=timing)
root = Path(__file__).resolve().parents[2]
output = root/'data/generated/structured_full_rank_scalar_20260926/cubic_quadratic_feature_20260930'/f'check_{time.time_ns()}'
output.mkdir(parents=True,exist_ok=False)
(output/'check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
print(str(output/'check.json'))
