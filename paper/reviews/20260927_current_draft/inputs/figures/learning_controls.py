#!/usr/bin/env python3
"""Capture five four-method circle comparisons; no neural training is run.

Use the paper's dense/P3 endpoint bundle and both archived factor seeds.
Compute the complete canonical frozen empirical NTK at the same initialization.
Output is a fresh directory; rendering is separate in scripts/tikz_figures.py.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import time

os.environ.setdefault('OPENBLAS_NUM_THREADS', '2')
os.environ.setdefault('OMP_NUM_THREADS', '2')
import numpy as np
from scipy.linalg import expm
from frozen_ntk import initial, fields, blocks, formula_check, array_hash, INITIAL_HASHES

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ARCHIVE = ROOT / 'data/generated/neural_response_memory_20260922'
SEEDS = (20260924, 20260925)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rms(a):
    return float(np.sqrt(np.mean(np.asarray(a)**2)))


def frozen_flow(K, initial_train, y):
    K = (K+K.T)/2
    eig, V = np.linalg.eigh(K)
    screen = 64*2048*np.finfo(float).eps*eig[-1]
    if eig[0] <= screen:
        raise RuntimeError(f'Unresolved training spectrum: {eig[0]} <= {screen}')
    direction = V.T @ (y-initial_train)
    rates = 2*eig/len(y)
    def prediction(t):
        return y - V @ (np.exp(-rates*t)*direction)
    lo, hi = 0., 1.
    for _ in range(100):
        if rms(prediction(hi)-y)**2 <= .001:
            break
        hi *= 2
    else:
        raise RuntimeError('Could not bracket the fitted time')
    for _ in range(100):
        mid = (lo+hi)/2
        if rms(prediction(mid)-y)**2 > .001:
            lo = mid
        else:
            hi = mid
    alpha = V @ (-np.expm1(-rates*hi)*direction/eig)
    alpha_inf = V @ (direction/eig)
    check = float(np.max(np.abs(initial_train+K @ alpha-prediction(hi))))
    expm_check = float(np.max(np.abs(y+expm(-2*K*(hi/7)/len(y)) @
                                   (initial_train-y)-prediction(hi/7))))
    assert max(check, expm_check) < 1e-7, (check, expm_check)
    return alpha, alpha_inf, dict(fit_time=hi, training_mse=rms(prediction(hi)-y)**2,
        eigenvalues=eig.tolist(), condition=float(eig[-1]/eig[0]),
        cross_formula_check=check, expm_check=expm_check)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    start = time.monotonic()
    report = dict(protocol='All five archived tasks, P3, both recorded factor seeds, no selection or tuning',
        purpose='Four-panel fitted-function previews: dense, frozen NTK, factors, response memory',
        controls='Identical width 2048, two tanh hidden layers, physical initialization seed 20260920; MSE 0.001 endpoints',
        metric='RMS discrepancy from dense on 8192 uniform circle queries; each method at its own fitting time',
        success='Resolved kernel spectrum, same physical data, endpoint metrics match archives, finite predictions',
        budget='One initialization; one analytic kernel fit per task; 180 seconds total; no neural training',
        parameter_mobilities=[2048, 1, 2048], factor_seeds=list(SEEDS), command=sys.argv,
        producer_sha256=digest(Path(__file__)), kernel_source_sha256=digest(HERE/'frozen_ntk.py'),
        numpy=np.__version__, sources={}, tasks=[])
    (args.out/'protocol.json').write_text(json.dumps(report, indent=2)+'\n')
    def record(path):
        report['sources'][str(path.relative_to(ROOT))] = digest(path)
    radial_path = HERE/'radial_source_data.npz'
    metrics_path = ARCHIVE/'factor_analysis01/metrics.json'
    record(radial_path); record(metrics_path)
    with np.load(radial_path, allow_pickle=False) as z:
        radial = {k:z[k] for k in z.files}
    descriptions = json.loads(str(radial['description_json']))['shallow']
    metrics = json.loads(metrics_path.read_text())
    weights = initial(2048, 20260920)
    for name, value in zip(('w', 'W0', 'c'), weights):
        assert array_hash(value) == INITIAL_HASHES[name], name
    report['autograd_block_max_abs_error'] = formula_check()
    result, cases = {}, []
    for i, desc in enumerate(descriptions):
        case = desc['case']
        prefix = f'case_{i}_'
        angles, dense, memory = [radial[f'shallow_{i}_{k}'] for k in ['angles','P0','P3']]
        memory_row = next(r for r in metrics['closure_selected'] if r['case']==case and r['P']==3)
        assert memory_row['valid'] and np.isclose(rms(memory-dense), memory_row['circle_rms'], rtol=1e-12)
        factors, factors_meta = [], []
        for seed in SEEDS:
            row = next(r for r in metrics['factor_selected'] if
                       r['case']==case and r['P']==3 and r['factor_seed']==seed)
            assert row['valid'] and all(row['initial_match'].values())
            path = ROOT / row['arrays_source']
            assert path.is_relative_to(ARCHIVE)
            record(path)
            assert digest(path)==row['arrays_sha256']
            with np.load(path, allow_pickle=False) as z:
                X, y = z['training_inputs'], z['labels']
                Xr, yr = z['represented_training_inputs'], z['represented_labels']
                f = z['endpoint_prediction']
                assert np.array_equal(angles, z['endpoint_angles'])
                assert abs(rms(z['training_prediction']-y)**2-.001) < 1e-8
            assert np.allclose(X, np.column_stack((np.cos(radial[f'shallow_{i}_train_angles']),
                                                  np.sin(radial[f'shallow_{i}_train_angles']))), atol=1e-14)
            assert np.array_equal(y, radial[f'shallow_{i}_labels'])
            assert np.isclose(rms(f-dense), row['circle_rms'], rtol=1e-12)
            factors.append(f)
            factors_meta.append({k:row[k] for k in ['factor_seed','rank','circle_rms','time','physical_training_mse','endpoint_refinement_rms']})
        if len(Xr)!=len(X):
            # Exact odd-network antipodal quotient: equal duplicated loss terms.
            assert len(X)==2*len(Xr)
            assert np.allclose(X[:len(Xr)], Xr, atol=1e-14)
            assert np.allclose(X[len(Xr):], -Xr, atol=1e-14)
            assert np.array_equal(y[:len(yr)], yr) and np.array_equal(y[len(yr):], -yr)
        train = fields(weights, Xr)
        Kblocks = blocks(train, train, Xr, Xr, 2048)
        alpha, alpha_inf, frozen_meta = frozen_flow(Kblocks.sum(axis=0), train[-1], yr)
        # Confirm the original physical eight-input loss, including quotient case.
        physical = fields(weights, X)
        fy = physical[-1]+blocks(physical,train,X,Xr,2048).sum(axis=0) @ alpha
        assert abs(rms(fy-y)**2-.001)<1e-8
        for key,value in dict(angles=angles,dense=dense,memory=memory,factors=np.stack(factors),
                train_inputs=X,train_labels=y,represented_inputs=Xr,represented_labels=yr,
                train_kernel=Kblocks.sum(axis=0),kernel_blocks=Kblocks,alpha=alpha).items():
            result[prefix+key]=value
        record_entry=dict(case=case,title=desc['title'],P=3,rank=memory_row['rank'],
            represented_samples=len(Xr),factors=factors_meta,memory_mse=memory_row['physical_training_mse'],
            memory_fit_time=memory_row['time'],frozen=frozen_meta)
        cases.append((prefix,train,Xr,alpha,alpha_inf,dense,memory,record_entry))
    angles = result['case_0_angles']
    assert all(np.array_equal(result[f'case_{i}_angles'],angles) for i in range(5))
    query=np.column_stack((np.cos(angles),np.sin(angles)))
    cross=[[] for _ in cases]; initial_query=[]
    for k in range(0,len(query),256):
        if time.monotonic()-start>180:
            raise RuntimeError('Capture exceeded the declared budget')
        q=query[k:k+256]; qfields=fields(weights,q)
        initial_query.append(qfields[-1])
        for j,(_,train,Xr,*_) in enumerate(cases):
            cross[j].append(blocks(qfields,train,q,Xr,2048).sum(axis=0))
    initial_query=np.concatenate(initial_query)
    for j,(prefix,train,Xr,alpha,alpha_inf,dense,memory,entry) in enumerate(cases):
        C=np.concatenate(cross[j]); frozen=initial_query+C @ alpha; limit=initial_query+C @ alpha_inf
        assert np.isfinite(frozen).all() and np.isfinite(limit).all()
        result[prefix+'frozen_ntk']=frozen; result[prefix+'frozen_ntk_infinity']=limit
        result[prefix+'cross_kernel']=C
        entry['rms_vs_dense']=dict(frozen_ntk=rms(frozen-dense),memory=rms(memory-dense),
                                  factors=[rms(v-dense) for v in result[prefix+'factors']],
                                  frozen_ntk_infinity=rms(limit-dense))
        entry['output_ranges']={k:[float(result[prefix+k].min()),float(result[prefix+k].max())]
                                for k in ['dense','memory','frozen_ntk','factors']}
        report['tasks'].append(entry)
        print(json.dumps(dict(task=entry['case'],rms=entry['rms_vs_dense'])),flush=True)
    # The existing paired-label control provides a cross-run regression oracle.
    with np.load(HERE/'frozen_ntk_source.npz',allow_pickle=False) as z:
        check=float(np.max(np.abs(z['frozen_ntk']-result['case_2_frozen_ntk'])))
        assert check<1e-7,check
    record(HERE/'frozen_ntk_source.npz')
    report.update(paired_control_max_difference=check,elapsed_seconds=time.monotonic()-start,
                  initialization_hashes=INITIAL_HASHES)
    result['initial_prediction']=initial_query
    result['metadata_json']=np.array(json.dumps(report,allow_nan=False))
    np.savez_compressed(args.out/'learning_controls_source.npz',**result)
    (args.out/'learning_controls_manifest.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')


if __name__=='__main__':
    main()
