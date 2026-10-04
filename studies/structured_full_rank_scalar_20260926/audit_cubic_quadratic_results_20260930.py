"""Replay saved round-four endpoints and exact lifts; no integration."""
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT/'data/generated/structured_full_rank_scalar_20260926/cubic_feedback_repair_20260930/round4'
sys.path.insert(0,str(RUN/'sources'))
import cubic_quadratic_feature_repair as quadratic
import dense_compare as dense
from circle_tasks import directions


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


started = time.monotonic()
manifest = json.loads((RUN/'manifest.json').read_text())
for name,expected in manifest['source_sha256'].items():
    assert sha(RUN/'sources'/name) == expected,name
summary = json.loads((RUN/'summary.json').read_text())
initial = dense.initialize(1024,1,'gaussian')
rows = []
for row in summary['results']:
    stem = f"{row['task']}__{row['method']}"
    assert json.loads((RUN/f'{stem}.json').read_text()) == row
    assert sha(RUN/f'{stem}.npz') == row['data_sha256']
    assert sha(RUN/f'{stem}__coefficients.npz') == row['coefficient_sha256']
    with np.load(RUN/f'{stem}.npz') as stored:
        saved = {key:stored[key] for key in stored.files}
    with np.load(RUN/f'{stem}__coefficients.npz') as stored:
        coef = {key:stored[key] for key in stored.files}
    labels,G = coef['labels'],coef['readout_gram']
    m,p = len(labels),len(G)
    state = saved['state']
    v,eta = state[:p],state[p:]
    d = len(eta)
    assert len(saved['angles']) == 256+m
    inputs = directions(saved['angles'][256:])
    queries = directions(saved['angles'])
    def output(prefix):
        feature = (coef[f'{prefix}_constant']
                   +np.einsum('ail,l->ai',coef[f'{prefix}_linear'],eta)
                   +.5*np.einsum('ailk,l,k->ai',coef[f'{prefix}_quadratic'],eta,eta))
        return feature @ v
    train,prediction = output('train'),output('query')
    residual = train-labels
    lift = quadratic.lifted_endpoint_diagnostic(initial.w,initial.W,inputs,labels,
        queries,state,extra_mode=row['method']=='quadratic_mode')
    exact = lift['prediction']
    fingerprint = row['metadata']['basis_whitening_sha256']
    assert lift['basis_whitening_sha256'] == fingerprint
    assert row['lifted_diagnostic']['basis_whitening_sha256'] == fingerprint
    error = prediction[:256]-saved['dense']
    computed = dict(
        circle_rms=float(np.sqrt(np.mean(error*error))),
        old_circle_rms=float(np.sqrt(np.mean((saved['old']-saved['dense'])**2))),
        nested_rms_change=float(abs(np.sqrt(np.mean(error**2))-np.sqrt(np.mean(error[::2]**2)))),
        train_mse=float(np.mean(residual*residual)),
        lifted_tanh_train_mse=float(np.mean((exact[256:]-labels)**2)),
        lifted_tanh_circle_rms=float(np.sqrt(np.mean((exact[:256]-saved['dense'])**2))),
        surrogate_vs_lifted_circle_rms=float(np.sqrt(np.mean((prediction[:256]-exact[:256])**2))),
        alias_max_abs=float(np.max(np.abs(prediction[256:]-train))),
        readout_energy=float(v @ G @ v))
    report_error = max(abs(computed[key]-row[key]) for key in computed)
    prediction_error = float(np.max(np.abs(prediction-saved['prediction'])))
    exact_error = float(np.max(np.abs(exact-saved['lifted_tanh'])))
    assert report_error < 1e-10,report_error
    assert prediction_error < 1e-10,prediction_error
    assert exact_error < 1e-10,exact_error
    train_bytes = (labels.nbytes+2*G.nbytes
                   +sum(coef[f'train_{key}'].nbytes for key in ('constant','linear','quadratic')))
    query_bytes = sum(coef[f'query_{key}'].nbytes for key in ('constant','linear','quadratic'))
    assert train_bytes == row['metadata']['training_coefficient_bytes']
    assert query_bytes == row['metadata']['query_coefficient_bytes']
    assert p+d == row['training_states'] == row['total_states']
    assert row['passive_dynamic_states'] == 0
    assert d == row['metadata']['hidden_rank']
    assert row['metadata']['discarded_positive_eigenvalues'] == []
    assert row['metadata']['constructor_seconds'] < 30
    assert all(abs(lift[key]-value) < 1e-10 for key,value in row['lifted_diagnostic'].items()
               if key != 'basis_whitening_sha256')
    assert abs(lift['hidden_metric_norm']-np.linalg.norm(eta)) < 1e-9
    assert abs(lift['readout_rms']**2-computed['readout_energy']) < 1e-9
    rows.append(dict(task=row['task'],method=row['method'],m=m,p=p,d=d,
        state_count=p+d,train_static_bytes=train_bytes,query_static_bytes=query_bytes,
        train_static_scalars=train_bytes//8,query_static_scalars=query_bytes//8,
        training_hessian_scalars=m*p*d*d,prediction_replay_error=prediction_error,
        lifted_replay_error=exact_error,summary_recompute_error=report_error,
        basis_fingerprint_matches=True,**computed))
result = dict(rows=rows,source_hashes_verified=len(manifest['source_sha256']),
              seconds=time.monotonic()-started,training_runs=0,
              summary_sha256=sha(RUN/'summary.json'),manifest_sha256=sha(RUN/'manifest.json'))
out = RUN.parent/'round4_audit'/f'check_{time.time_ns()}'
out.mkdir(parents=True,exist_ok=False)
(out/'audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
print(out/'audit.json')
