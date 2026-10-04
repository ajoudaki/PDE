# Scoped numerical verification of the two large scalar discrepancies

2026-09-30. Frozen before these two verification solves. The primary
protocol authorized tighter scalar solves only on its first two tasks.
After the fixed nine-task panel completed, the supervisor explicitly
authorized this limited extension because `near_pair_sin9` and
`cluster_triple_cos9` had large circle discrepancies, while neither had
a retained scalar tolerance replicate. This is a post-result numerical
check of unchanged models and endpoints; it is not predeclared evidence
for model selection, a new task, a new response order, or a parameter fit.

Run exactly one additional integration for each of those two tasks from
its saved `initial_gram`, `response_gram`, and `model_labels`. Use the
saved query tensors without rebuilding initialization. Set `rtol=1e-9`,
`atol=1e-11`, target MSE `0.001`, physical-time cap `3000`, maximum step
`10`, and per-solve wall limit `10` seconds. Float64 and one BLAS thread
are retained. No new dense reference is trained and no existing product
is overwritten.

The primary verification metric is the circle RMS difference between
the existing scalar prediction and this tighter solve. Success requires
the tighter solve to reach the target and this difference to be less
than `1e-4`, the original protocol's numerical threshold. Otherwise
report numerical uncertainty and retain the actual outcome. Also retain
the new scalar-vs-dense RMS, returned residual MSE, decoded training MSE,
training alias error, endpoint state and history. All inputs, module
source, and this protocol receive SHA256 records.

Outputs are separate files inside the existing generated run directory:
`hard_task_tolerance_checks.json` and
`hard_task_tolerance_endpoints.npz`. The following exact Python body is
the complete reproduction source; execute it from the repository root.

```python
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import hashlib
import json
from pathlib import Path
import platform
import sys
import time
import numpy as np
import scipy

study = Path('studies/structured_full_rank_scalar_20260926')
base = Path('data/generated/structured_full_rank_scalar_20260926/cubic_scalar_20260930')
protocol = study/'CUBIC_NUMERICAL_CHECK_ADDENDUM_20260930.md'
sys.path.insert(0, str(study))
from cubic_scalar_ode import ScalarModel, QueryCoefficients, integrate

json_path = base/'hard_task_tolerance_checks.json'
array_path = base/'hard_task_tolerance_endpoints.npz'
if json_path.exists() or array_path.exists():
    raise FileExistsError('Verification outputs already exist; preserve them')
digest = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
rms = lambda values: float(np.sqrt(np.mean(np.asarray(values)**2)))
records, endpoints = [], {}
started = time.monotonic()
for task in ('near_pair_sin9', 'cluster_triple_cos9'):
    source = base/f'{task}.npz'
    with np.load(source) as saved:
        labels = saved['model_labels'].copy()
        gram = saved['initial_gram'].copy()
        response = saved['response_gram'].copy()
        query_gram = saved['query_gram'].copy()
        query_cubic = saved['query_cubic'].copy()
        original = saved['scalar'].copy()
        dense = saved['dense'].copy()
        original_labels = saved['labels'].copy()
        q = len(saved['angles'])
    row = json.loads((base/f'{task}.json').read_text())
    model = ScalarModel(labels, gram, response)
    coefficients = QueryCoefficients(query_gram, query_cubic)
    state, info = integrate(model, target=.001, rtol=1e-9, atol=1e-11,
                            time_cap=3000., deadline_seconds=10., max_step=10.)
    history = info.pop('history')
    prediction = model.predict(state, coefficients)
    circle, train = prediction[:q], prediction[q:]
    representatives = np.asarray(row['representatives'])
    residual = state[:model.m]
    difference = rms(circle-original)
    records.append(dict(task=task, source_sha256=digest(source),
        result=info, original_circle_rms=row['scalar_dense_rms'],
        tighter_circle_rms=rms(circle-dense),
        scalar_circle_rms_change=difference,
        scalar_circle_max_abs_change=float(np.max(abs(circle-original))),
        residual_mse=float(np.mean(residual**2)),
        decoded_train_mse=float(np.mean((train-original_labels)**2)),
        training_alias_max_abs=float(np.max(abs(
            train[representatives]-(labels+residual)))),
        passes=bool(info['fitted'] and difference < 1e-4)))
    endpoints[f'{task}__state'] = state
    endpoints[f'{task}__circle'] = circle
    endpoints[f'{task}__train'] = train
    endpoints[f'{task}__history'] = history

np.savez_compressed(array_path, **endpoints)
result = dict(kind='post-result fixed-coefficient numerical verification',
    command='Execute the Python body in CUBIC_NUMERICAL_CHECK_ADDENDUM_20260930.md',
    cwd=str(Path.cwd()), python=platform.python_version(),
    numpy=np.__version__, scipy=scipy.__version__, blas_threads=1,
    source_sha256=digest(study/'cubic_scalar_ode.py'),
    addendum_sha256=digest(protocol), original_summary_sha256=digest(base/'summary.json'),
    endpoints_file=array_path.name, endpoints_sha256=digest(array_path),
    total_seconds=time.monotonic()-started, results=records)
with json_path.open('x') as output:
    json.dump(result, output, indent=2, allow_nan=False)
    output.write('\n')
print(json.dumps(result, indent=2, allow_nan=False))
```
