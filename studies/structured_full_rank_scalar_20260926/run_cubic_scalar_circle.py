"""Frozen nine-task direct scalar-vs-dense comparison; no training on import."""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
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
from cubic_scalar_ode import initialize, query_coefficients, integrate, frozen_kernel

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = ROOT/'data/generated/structured_full_rank_scalar_20260926/cubic_scalar_20260930'
REF = ROOT/'data/generated/structured_full_rank_scalar_20260926/all_tasks_j2_20260927/references'
TASKS = ('pair_cos3','pair_orthogonal_cos1','near_pair_sin9','cluster_triple_cos9',
         'cluster_triple_cos1','triple_wide_mixed','quartet_mixed','broad_ridge6','alternating3')


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path,value):
    path.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')


def rms(values):
    return float(np.sqrt(np.mean(np.asarray(values)**2)))


def antipodal_reduce(inputs,labels):
    retained, groups = [], []
    for i in range(len(labels)):
        found = False
        for j, group in zip(retained,groups):
            if np.linalg.norm(inputs[i]+inputs[j]) < 1e-12 and abs(labels[i]+labels[j]) < 1e-12:
                group.append(i)
                found = True
                break
        if not found:
            retained.append(i)
            groups.append([i])
    if len(set(map(len,groups))) != 1:
        raise ValueError('Unequal multiplicities require weighted equations, not uniform reduction')
    return np.array(retained), groups


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    if (OUT/'summary.json').exists():
        raise FileExistsError('Preserve existing experiment; no overwrite')
    started = time.monotonic()
    sources = ('cubic_scalar_ode.py','run_cubic_scalar_circle.py','check_cubic_scalar_ode.py',
               'dense_compare.py','circle_tasks.py','CUBIC_SCALAR_EXPERIMENT_PROTOCOL_20260930.md')
    manifest = dict(command=sys.argv,python=platform.python_version(),numpy=np.__version__,
                    scipy=scipy.__version__,platform=platform.platform(),width=1024,seed=1,
                    target_mse=.001,source_sha256={p:digest(HERE/p) for p in sources},
                    primary='raw circle RMS(scalar-dense) at own first MSE=.001 crossing',
                    query_count=256,task_panel=TASKS,blas_threads=1)
    write_json(OUT/'manifest.json',manifest)
    initial = dense.initialize(1024,1,'gaussian')
    results = []
    for number,name in enumerate(TASKS):
        if time.monotonic()-started > 240:
            results.append(dict(task=name,status='campaign_wall_limit'))
            continue
        task_started = time.monotonic()
        with np.load(REF/f'{name}__gaussian.npz') as saved:
            angles = saved['angles'].copy()
            train_angles = saved['train_angles'].copy()
            labels = saved['train_labels'].copy()
            reference = saved['prediction'].copy()
            dense_train = saved['train_prediction'].copy()
        refinfo = json.loads((REF/f'{name}__gaussian.json').read_text())
        inputs = directions(train_angles)
        selected, groups = antipodal_reduce(inputs,labels)
        train = inputs[selected]
        row = dict(task=name,original_samples=len(labels),effective_samples=len(selected),
                   representatives=selected.tolist(),antipodal_groups=groups,
                   dense_checkpoint_sha256=digest(REF/f'{name}__gaussian.npz'),
                   dense_train_mse=float(np.mean((dense_train-labels)**2)),
                   dense_physical_time=refinfo['physical_time'])
        try:
            model = initialize(initial.w,initial.W,train,labels[selected])
            coefficients = query_coefficients(initial.w,initial.W,train,
                directions(np.concatenate((angles,train_angles))))
            coefficient_seconds = time.monotonic()-task_started
            if coefficient_seconds > 30:
                raise TimeoutError('coefficient construction exceeded fixed 30s budget')
            state, info = integrate(model)
            history = info.pop('history')
            prediction = model.predict(state,coefficients)
            frozen, frozen_info = frozen_kernel(model,coefficients)
            q = len(angles)
            scalar_circle, scalar_train = prediction[:q],prediction[q:]
            difference = scalar_circle-reference
            row.update(status=info['stop_reason'],scalar=info,frozen=frozen_info,
                scalar_dense_rms=rms(difference),frozen_dense_rms=rms(frozen[:q]-reference),
                scalar_dense_max_abs=float(np.max(np.abs(difference))),
                rms_128=rms(difference[::2]),quadrature_rms_change=abs(rms(difference)-rms(difference[::2])),
                scalar_decoded_train_mse=float(np.mean((scalar_train-labels)**2)),
                training_alias_max_abs=float(np.max(np.abs(prediction[selected+q]-(model.labels+state[:model.m])))),
                initial_circle_output_rms=rms(dense._forward(initial,directions(angles)).output),
                training_state_count=model.training_size,total_state_count=model.size,
                scalar_coefficients_bytes=model.coefficient_nbytes,
                query_coefficients_bytes=coefficients.nbytes,
                gram_min_eigenvalue=float(model.eigenvalues[0]),gram_condition=model.condition,
                coefficient_seconds=coefficient_seconds)
            arrays = dict(angles=angles,train_angles=train_angles,labels=labels,
                          scalar=scalar_circle,dense=reference,frozen=frozen[:q],
                          scalar_train=scalar_train,dense_train=dense_train,
                          state=state,history=history,initial_gram=model.initial_gram,
                          response_gram=model.response_gram,model_labels=model.labels,
                          query_gram=coefficients.cross_gram,query_cubic=coefficients.cubic)
            if number < 2:
                tighter, tighter_info = integrate(model,rtol=1e-9,atol=1e-11)
                tighter_info.pop('history')
                tight_prediction = model.predict(tighter,coefficients)
                row['tolerance_check'] = dict(**tighter_info,
                    circle_rms_difference=rms(tight_prediction[:q]-scalar_circle),
                    passes=rms(tight_prediction[:q]-scalar_circle)<1e-4)
                arrays['tighter_scalar'] = tight_prediction[:q]
            if row['quadrature_rms_change'] > .001:
                from true_aggregate_references import load_checkpoint
                finer_angles = np.arange(512)*2*np.pi/512
                finer_coefficients = query_coefficients(initial.w,initial.W,train,directions(finer_angles))
                finer_scalar = model.predict(state,finer_coefficients)
                finer_dense = load_checkpoint(REF/f'{name}__gaussian.npz').predict(finer_angles)
                row['rms_512'] = rms(finer_scalar-finer_dense)
                arrays.update(angles_512=finer_angles,scalar_512=finer_scalar,dense_512=finer_dense)
            np.savez_compressed(OUT/f'{name}.npz',**arrays)
            row['data_sha256'] = digest(OUT/f'{name}.npz')
        except (ValueError,TimeoutError,np.linalg.LinAlgError) as error:
            row.update(status='failed',error=f'{type(error).__name__}: {error}')
        row['task_seconds'] = time.monotonic()-task_started
        write_json(OUT/f'{name}.json',row)
        results.append(row)
        write_json(OUT/'summary.partial.json',results)
        print(json.dumps({key:row.get(key) for key in ('task','status','scalar_dense_rms','frozen_dense_rms',
             'total_state_count','task_seconds','error')}),flush=True)
    write_json(OUT/'summary.json',dict(results=results,total_seconds=time.monotonic()-started))
    print(f'COMPLETE {time.monotonic()-started:.3f}s: {OUT}',flush=True)


if __name__ == '__main__':
    main()
