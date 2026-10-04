"""Deterministic covariance and archived source-rank diagnostics; no training."""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import math
import os
import resource
import signal
import sys
import time
import numpy as np
from scipy.special import roots_hermitenorm

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def covariance(q, order):
    x, weights = roots_hermitenorm(order)
    weights = weights/math.sqrt(2*math.pi)
    diagonal = np.diag(q)
    assert np.max(np.abs(diagonal-diagonal[0])) < 1e-10
    variance = float(diagonal[0])
    xx, yy = x[:, None], x[None, :]
    ww = weights[:, None]*weights[None, :]
    result = np.empty_like(q)
    for a in range(len(q)):
        for b in range(a+1):
            corr = float(np.clip(q[a, b]/variance, -1., 1.))
            common = math.sqrt(variance*(1+corr)/2)*xx
            contrast = math.sqrt(variance*(1-corr)/2)*yy
            value = np.sum(ww*np.tanh(common+contrast)*np.tanh(common-contrast))
            result[a, b] = result[b, a] = value
    assert np.min(np.linalg.eigvalsh(result)) > -1e-8
    return result


def rank_needed(singular, priority, n, norm_weight, target):
    squared = np.asarray(singular, dtype=float)**2
    tails = np.r_[np.cumsum(squared[::-1])[::-1], 0.]
    found = np.flatnonzero(tails <= target*target*n*norm_weight)
    return priority+int(found[0])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--analysis', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError()))
    signal.alarm(120)
    resource.setrlimit(resource.RLIMIT_CPU, (118, 120))
    started = time.monotonic()
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=False)
    paths = [HERE/'gpu_multidata_baseline_0.json', HERE/'gpu_multidata_baseline_1.json']
    datasets = {}
    for path in paths:
        datasets.update(json.loads(path.read_text())['datasets'])
    gap_rows = []
    for name, data in sorted(datasets.items()):
        u, y = np.array(data['U']), np.array(data['labels'])
        values = []
        for order in (64, 128, 256):
            q0 = u@u.T
            q1 = covariance(q0, order)
            q2 = covariance(q1, order)
            eigenvalues = np.linalg.eigvalsh(q2)
            values.append(dict(order=order, q2=q2.tolist(),
                               gamma=float(eigenvalues[0]), eigenvalues=eigenvalues.tolist()))
        gamma = values[-1]['gamma']
        q = np.array(values[-1]['q2'])
        entry_change = float(np.max(np.abs(q-np.array(values[-2]['q2']))))
        gap_relative = abs(gamma-values[-2]['gamma'])/gamma
        label_rms = float(np.sqrt(np.mean(y*y)))
        gap_rows.append(dict(dataset_id=name, m=len(u), d=u.shape[1],
            Y=label_rms, gamma=gamma, normalized_gap=gamma/len(u),
            label_gap_ratio=label_rms/(gamma/len(u)),
            frozen_feature_readout_norm=float(np.sqrt(y@np.linalg.solve(q,y))),
            last_entry_change=entry_change, last_gap_relative_change=gap_relative,
            convergence_pass=entry_change<1e-7 and gap_relative<1e-4, quadrature=values))

    rows = list(csv.DictReader((Path(args.analysis)/'all_comparisons.csv').open()))
    base_rows = [r for r in rows if r['stage']=='baseline']
    assert len(base_rows) == 70
    rank_rows, hashes = [], {}
    weight_maps = [dict(A0=.25, h0=1., reverse_delta1=.5, h2=.3),
                   dict(z0=1., g0=1., delta1=.5, g2=.3, W_h2=.3)]
    for r in base_rows:
        path = Path(r['case_path'])/'record.json'
        if not path.is_absolute(): path = ROOT/path
        record = json.loads(path.read_text())
        hashes[str(path.relative_to(ROOT))] = sha(path)
        diag = record['sampler_diagnostics'][0]
        n, m, d = record['n'], record['m'], record['d']
        for layer, weights in enumerate(weight_maps, 1):
            basis = diag[f'basis{layer}']
            assert basis['discarded_priority_directions'] == 0
            sizes = dict(A0=d, h0=m+32, reverse_delta1=m, h2=m+32,
                         z0=m+32, g0=m+32, delta1=m, g2=m+32, W_h2=m+32)
            skips = {x['source']:x['zero_or_tiny_columns'] for x in basis['tiny_source_columns']}
            norm_weight = sum(weight**2 for name,weight in weights.items() if sizes[name]>skips[name])
            singular = basis['remainder_singular_values']
            priority = basis['priority_rank']
            row = dict(dataset_id=record['dataset_id'], n=n, seed=record['seed'], layer=layer,
                       priority_rank=priority, source_norm_squared=n*norm_weight,
                       rank_at_10percent=rank_needed(singular,priority,n,norm_weight,.1),
                       rank_at_3percent=rank_needed(singular,priority,n,norm_weight,.03),
                       rank_at_1percent=rank_needed(singular,priority,n,norm_weight,.01),
                       rank_at_root_tolerance=rank_needed(singular,priority,n,norm_weight,1/math.sqrt(n)))
            rank_rows.append(row)

    # Tiny exact checks of the tail selector, with known errors and ranks.
    assert rank_needed([3., 2., 1.],2,1,14.,0.) == 5
    assert rank_needed([3., 2., 1.],2,1,14.,1.) == 2
    assert rank_needed([3., 2., 1.],2,1,14.,.3) == 4
    result = dict(covariances=gap_rows, source_ranks=rank_rows,
        input_hashes={**hashes, **{str(p.relative_to(ROOT)):sha(p) for p in paths}},
        analysis_summary_sha256=sha(Path(args.analysis)/'summary.json'),
        source_sha256=sha(__file__), protocol_sha256=sha(HERE/'PRACTICAL_EXPONENT_PROTOCOL.md'),
        argv=sys.argv, cwd=os.getcwd(), numpy=np.__version__,
        seconds=time.monotonic()-started, training_performed=False,
        meaning='Initial finite-source relative Frobenius tails; not trajectory error guarantees.')
    (out/'assessment.json').write_text(json.dumps(result,indent=2)+'\n')
    (out/'analysis_source.py').write_bytes(Path(__file__).read_bytes())
    for name,data in [('conditioning',gap_rows),('source_ranks',rank_rows)]:
        trimmed=[{k:v for k,v in row.items() if k!='quadrature'} for row in data]
        with (out/f'{name}.csv').open('w',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=list(trimmed[0]));writer.writeheader();writer.writerows(trimmed)
    print(json.dumps(dict(datasets=len(gap_rows),rank_rows=len(rank_rows),seconds=result['seconds'],
                          all_covariances_converged=all(r['convergence_pass'] for r in gap_rows))))


if __name__=='__main__': main()
