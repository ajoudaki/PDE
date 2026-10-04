"""Frozen round-four curvature test; never fits coefficients to dense outputs."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys
import time
import numpy as np
import scipy
import dense_compare as dense
from circle_tasks import directions
from cubic_quadratic_feature_repair import initialize_with_queries, lifted_endpoint_diagnostic
from small_scalar_integrator import integrate

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[1]/'data/generated/structured_full_rank_scalar_20260926'
OLD = DATA/'cubic_scalar_20260930'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tasks',nargs='+',default=[
        'near_pair_sin9','cluster_triple_cos9','cluster_triple_cos1'])
    parser.add_argument('--methods',nargs='+',choices=['quadratic','quadratic_mode'],
                        default=['quadratic','quadratic_mode'])
    parser.add_argument('--output',default='round4')
    parser.add_argument('--rtol',type=float,default=1e-8)
    parser.add_argument('--atol',type=float,default=1e-10)
    args = parser.parse_args()
    out = DATA/'cubic_feedback_repair_20260930'/args.output
    out.mkdir(parents=True,exist_ok=False)
    sources = out/'sources'
    sources.mkdir()
    names = ('run_cubic_quadratic_repair.py','cubic_quadratic_feature_repair.py',
             'cubic_minimal_mode_repair.py','small_scalar_integrator.py','cubic_scalar_ode.py',
             'CUBIC_REPAIR_ROUND4_20260930.md','CUBIC_QUADRATIC_FEATURE_ROUTE_20260930.md',
             'dense_compare.py','circle_tasks.py')
    for name in names:
        (sources/name).write_bytes((HERE/name).read_bytes())
    manifest = dict(command=sys.argv,settings=vars(args),python=platform.python_version(),
                    numpy=np.__version__,scipy=scipy.__version__,
                    source_sha256={name:sha(HERE/name) for name in names})
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    initial = dense.initialize(1024,1,'gaussian')
    results = []
    for task in args.tasks:
        with np.load(OLD/f'{task}.npz') as saved:
            y = saved['model_labels']
            angles = np.r_[saved['angles'],saved['train_angles']]
            ref,old = saved['dense'],saved['scalar']
        previous = json.loads((OLD/f'{task}.json').read_text())
        representatives = np.asarray(previous['representatives'])
        inputs = directions(angles[256:])[representatives]
        queries = directions(angles)
        for method in args.methods:
            extra = method == 'quadratic_mode'
            model,coeff = initialize_with_queries(initial.w,initial.W,inputs,y,queries,
                                                  extra_mode=extra,degree=2)
            if model.metadata['constructor_seconds'] > 30:
                raise TimeoutError('Coefficient construction exceeded 30 seconds')
            coefficient_path = out/f'{task}__{method}__coefficients.npz'
            np.savez_compressed(coefficient_path,labels=y,readout_gram=model.readout_gram,
                train_constant=model.coefficients.constant,train_linear=model.coefficients.linear,
                train_quadratic=model.coefficients.quadratic,query_constant=coeff.constant,
                query_linear=coeff.linear,query_quadratic=coeff.quadratic)
            state,info,history = integrate(model.rhs,model.initial_state(),model.residual,
                                           model.blocks,rtol=args.rtol,atol=args.atol)
            pred = model.predict(state,coeff)
            error = pred[:256]-ref
            # This diagnostic evaluates real tanh at the *same lifted state*.
            # It is never used in the scalar RHS, prediction or selection.
            diagnostic_started = time.monotonic()
            lifted = lifted_endpoint_diagnostic(initial.w,initial.W,inputs,y,queries,state,
                                                  extra_mode=extra)
            exact = np.asarray(lifted.pop('prediction'))
            if lifted['basis_whitening_sha256'] != model.metadata['basis_whitening_sha256']:
                raise ValueError('Posthoc lift regenerated a different basis')
            row = dict(task=task,method=method,**info,metadata=model.metadata,
                training_states=model.training_size,total_states=model.size,
                passive_dynamic_states=0,circle_rms=float(np.sqrt(np.mean(error**2))),
                old_circle_rms=previous['scalar_dense_rms'],
                nested_rms_change=float(abs(np.sqrt(np.mean(error**2))-
                                           np.sqrt(np.mean(error[::2]**2)))),
                alias_max_abs=float(np.max(np.abs(pred[256+representatives]-
                                                 model.training_prediction(state)))),
                readout_energy=model.readout_energy(state),
                kernel_min_eigenvalue=float(np.linalg.eigvalsh(model.kernel(state))[0]),
                lifted_diagnostic=lifted,
                lifted_tanh_circle_rms=float(np.sqrt(np.mean((exact[:256]-ref)**2))),
                surrogate_vs_lifted_circle_rms=float(np.sqrt(np.mean((pred[:256]-exact[:256])**2))),
                lifted_tanh_train_mse=float(np.mean((exact[256+representatives]-y)**2)),
                diagnostic_seconds=time.monotonic()-diagnostic_started,
                coefficient_sha256=sha(coefficient_path),input_sha256=sha(OLD/f'{task}.npz'))
            path = out/f'{task}__{method}.npz'
            np.savez_compressed(path,state=state,history=history,prediction=pred,dense=ref,
                                old=old,angles=angles,lifted_tanh=exact)
            row['data_sha256'] = sha(path)
            (out/f'{task}__{method}.json').write_text(json.dumps(row,indent=2,allow_nan=False)+'\n')
            results.append(row)
            print(json.dumps({key:row[key] for key in ('task','method','fitted','circle_rms',
                'train_mse','training_states','training_seconds','lifted_tanh_train_mse',
                'surrogate_vs_lifted_circle_rms','lifted_tanh_circle_rms')}),flush=True)
    (out/'summary.json').write_text(json.dumps(dict(results=results),indent=2,allow_nan=False)+'\n')


if __name__ == '__main__':
    main()
