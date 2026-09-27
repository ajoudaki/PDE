#!/usr/bin/env python3
"""One matched-initialization frozen-NTK control for the paper radial preview.

Compute the full empirical tangent kernel with canonical mobilities (n,1,n),
then solve its constant-kernel flow by eigendecomposition. No neural training,
ridge penalty, rescaling, kernel tuning or omitted parameter blocks.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import time

os.environ.setdefault('OPENBLAS_NUM_THREADS', '2')
os.environ.setdefault('OMP_NUM_THREADS', '2')
import numpy as np

HERE = Path(__file__).resolve().parent
INITIAL_HASHES = {
    'w': 'da24d2b86aed45dfa6e7442e24bfcb968ec28fcfbcfb2f5f07ac066601fffd63',
    'c': '460ee22d13695cbe3226805bf5b24b124100e32be5717737508c79d8679b0db6',
    'W0': '559c9ad62fd9feab4fb4671e854b86ec975240a12aa8792873824ebe2344b3f9',
}


def array_hash(a):
    return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()


def initial(width, seed):
    rng = np.random.default_rng(seed)
    return (rng.standard_normal((width, 2)),
            rng.standard_normal((width, width))/np.sqrt(width),
            rng.standard_normal(width)/width)


def fields(weights, inputs):
    w, matrix, c = weights
    h1 = np.tanh(w @ inputs.T)
    h2 = np.tanh(matrix @ h1)
    delta2 = c[:, None]*(1-h2*h2)
    delta1 = (matrix.T @ delta2)*(1-h1*h1)
    return h1, h2, delta1, delta2, c @ h2 / len(c)


def blocks(left, right, inputs_left, inputs_right, n):
    h1, h2, d1, d2, _ = left
    g1, g2, e1, e2, _ = right
    return np.stack(((d1.T @ e1)*(inputs_left @ inputs_right.T)/n,
                     (d2.T @ e2)*(h1.T @ g1)/(n*n),
                     h2.T @ g2/n))


def formula_check():
    """Compare each block to full autograd Jacobians on a separate tiny net."""
    import torch
    torch.set_num_threads(1)
    rng = np.random.default_rng(827)
    X, Q = rng.normal(size=(4,2)), rng.normal(size=(3,2))
    weights = initial(9, 612)
    weights = (weights[0], weights[1], weights[2]*9)
    w, matrix, c = [torch.tensor(v, dtype=torch.float64, requires_grad=True) for v in weights]
    def jac(x):
        h1 = (w @ torch.tensor(x.T, dtype=torch.float64)).tanh()
        h2 = (matrix @ h1).tanh()
        f = c @ h2/9
        result = [[], [], []]
        for j in range(len(x)):
            for rows, gradient in zip(result, torch.autograd.grad(f[j], (w,matrix,c), retain_graph=True)):
                rows.append(gradient.detach().numpy().reshape(-1))
        return [np.stack(rows) for rows in result]
    J, Jq = jac(X), jac(Q)
    expected = np.stack([mob*(a @ b.T) for mob,a,b in zip((9,1,9),Jq,J)])
    actual = blocks(fields(weights,Q), fields(weights,X), Q,X,9)
    error = float(np.max(np.abs(actual-expected)))
    assert error < 1e-12, error
    return error


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--bundle',type=Path,default=HERE/'response_memory_source.npz')
    p.add_argument('--out',type=Path,required=True)
    args = p.parse_args()
    args.out.mkdir(parents=True,exist_ok=False)
    started = time.monotonic()
    report = dict(task='quadrant_pairs',width=2048,hidden_layers=2,activation='tanh',
                  seed=20260920,loss='unhalved mean squared error',threshold=.001,
                  parameter_mobilities=[2048,1,2048],control='full initialization-frozen empirical NTK',
                  protocol='One preselected task/seed, all three parameter blocks, same initialization and fit threshold; no tuning or ridge',
                  success='Positive resolved training spectrum, target MSE reached, finite full-circle predictions and independent formula check',
                  budget='One kernel construction and analytic flow; 8192 queries in blocks of 256; 180 wall seconds for kernel construction',
                  python=platform.python_version(),numpy=np.__version__,command=sys.argv,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  bundle_sha256=hashlib.sha256(args.bundle.read_bytes()).hexdigest())
    (args.out/'protocol.json').write_text(json.dumps(report,indent=2)+'\n')
    report['autograd_block_max_abs_error'] = formula_check()
    with np.load(args.bundle,allow_pickle=False) as z:
        X,y,angles = z['train_inputs'],z['train_labels'],z['factor_angles']
        dense,memory = z['factor_dense'],z['memory_endpoint_3']
        common_angles,initial_prediction = z['history_angles'],z['common_dense'][0]
        meta=json.loads(str(z['metadata_json']))
    weights=initial(2048,20260920)
    for name,value in zip(('w','W0','c'),weights):
        assert array_hash(value)==INITIAL_HASHES[name],name
    train=fields(weights,X)
    block=blocks(train,train,X,X,2048)
    K=block.sum(axis=0); K=(K+K.T)/2
    eig,V=np.linalg.eigh(K)
    screen=64*2048*np.finfo(float).eps*eig[-1]
    if eig[0] <= screen:
        raise RuntimeError(f'Training kernel is not resolved in float64: minimum={eig[0]}, screen={screen}')
    direction=V.T @ (y-train[-1])
    rates=2*eig/len(y)
    def prediction(t):
        return y - V @ (np.exp(-rates*t)*direction)
    def mse(t):
        return float(np.mean((prediction(t)-y)**2))
    lo,hi=0.,1.
    for _ in range(100):
        if mse(hi) <= .001: break
        hi*=2
    else: raise RuntimeError('Failed to bracket fitting time')
    for _ in range(100):
        mid=(lo+hi)/2
        if mse(mid) > .001: lo=mid
        else: hi=mid
    fit_time=hi
    alpha=V @ ((-np.expm1(-rates*fit_time))*direction/eig)
    alpha_infinity=V @ (direction/eig)
    spectral_train=prediction(fit_time)
    cross_train=train[-1]+K @ alpha
    train_check=float(np.max(np.abs(spectral_train-cross_train)))
    assert train_check < 1e-8, train_check

    # Independent expm check at a nontrivial fraction of the fitted time.
    from scipy.linalg import expm
    check_time=fit_time/7
    train_expm=y + expm(-2*K*check_time/len(y)) @ (train[-1]-y)
    expm_check=float(np.max(np.abs(train_expm-prediction(check_time))))
    assert expm_check < 1e-8,expm_check

    Q=np.column_stack((np.cos(angles),np.sin(angles)))
    cross,initial_query=[],[]
    last=time.monotonic()
    for start in range(0,len(Q),256):
        if time.monotonic()-started > 180: raise RuntimeError('Kernel capture exceeded time budget')
        q=Q[start:start+256]
        qfields=fields(weights,q)
        cross.append(blocks(qfields,train,q,X,2048).sum(axis=0))
        initial_query.append(qfields[-1])
        if time.monotonic()-last>20:
            print(json.dumps(dict(event='queries',complete=start+len(q))),flush=True)
            last=time.monotonic()
    cross=np.concatenate(cross); initial_query=np.concatenate(initial_query)
    assert np.array_equal(angles[::4],common_angles)
    initial_check=float(np.max(np.abs(initial_query[::4]-initial_prediction)))
    assert initial_check < 1e-14,initial_check
    frozen=initial_query+cross @ alpha
    frozen_infinity=initial_query+cross @ alpha_infinity
    assert np.isfinite(frozen).all()
    errors={name:float(np.sqrt(np.mean((f-dense)**2))) for name,f in
            [('frozen_ntk',frozen),('frozen_ntk_infinity',frozen_infinity),('memory_P3',memory)]}
    report.update(fit_time=fit_time,training_mse=mse(fit_time),
                  train_kernel_eigenvalues=eig.tolist(),condition=float(eig[-1]/eig[0]),
                  eigenvalue_screen=float(screen),kernel_trace_by_block=np.trace(block,axis1=1,axis2=2).tolist(),
                  training_prediction_check=train_check,expm_check=expm_check,initial_prediction_check=initial_check,
                  full_circle_rms_vs_dense=errors,
                  frozen_range=[float(frozen.min()),float(frozen.max())],
                  frozen_infinity_range=[float(frozen_infinity.min()),float(frozen_infinity.max())],
                  frozen_training_mse_at_t80=mse(80),elapsed_seconds=time.monotonic()-started,
                  initialization_hashes=INITIAL_HASHES,train_inputs_sha256=array_hash(X),labels_sha256=array_hash(y),
                  angles_sha256=array_hash(angles),frozen_prediction_sha256=array_hash(frozen),
                  interpretation='Fidelity to this trained dense network, not error against unknown test labels; same finite-width feature-learning parameterization, not an infinite-width lazy-limit theorem')
    np.savez_compressed(args.out/'frozen_ntk_source.npz',angles=angles,train_inputs=X,train_labels=y,
                        dense=dense,memory=memory,frozen_ntk=frozen,frozen_ntk_infinity=frozen_infinity,
                        initial_prediction=initial_query,train_initial_prediction=train[-1],train_prediction=spectral_train,
                        train_kernel=K,train_kernel_blocks=block,cross_kernel=cross,alpha=alpha,
                        metadata_json=np.array(json.dumps(report,allow_nan=False)))
    (args.out/'report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(report,indent=2,allow_nan=False),flush=True)


if __name__=='__main__': main()
