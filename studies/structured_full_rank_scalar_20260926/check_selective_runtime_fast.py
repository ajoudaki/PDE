"""Deterministic exact-RHS comparisons on existing J2 scalar checkpoints."""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import json
import pickle
from pathlib import Path
import time
import numpy as np
from selective_runtime_fast import FastSharedQueryClosure
from true_aggregate_references import digest


def main():
    root = Path(__file__).resolve().parents[2]
    data = root/'data/generated/structured_full_rank_scalar_20260926'
    rows = []
    for task in ('pair_orthogonal_cos1', 'cluster_triple_cos1'):
        source = data/'selective_order_20260927/scalar'/f'{task}__selective_zero_out2.json'
        record = json.loads(source.read_text())
        template_path = Path(record['template_cache']['pickle_file'])
        if digest(template_path) != record['template_cache']['pickle_sha256']:
            raise ValueError('Template hash changed')
        with template_path.open('rb') as handle:
            template = pickle.load(handle)
        with np.load(source.parent/record['data_file'], allow_pickle=False) as saved:
            model = FastSharedQueryClosure(template, saved['all_query_angles'])
            initial, final = saved['initial_state'].copy(), saved['state'].copy()
        rng = np.random.default_rng(4107)
        stress = rng.uniform(-1.3, 1.3, model.size)
        stress[-1] = 1.2
        started = time.monotonic()
        checks = model.check_exact_rhs([initial, final, stress])
        rows.append({'task': task, 'states': model.size,
            'checks_initial_final_active_clipping': checks,
            'seconds': time.monotonic()-started,
            'core_terms': len(model._core_terms),
            'passive_terms': len(model._passive_terms)})
    output = data/'all_tasks_j2_20260927/checks/runtime_equivalence.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    result = {'passed': True, 'model_source_sha256': digest(Path(__file__).with_name('selective_runtime_fast.py')),
        'checker_source_sha256': digest(Path(__file__)), 'results': rows,
        'no_training_or_compilation': True}
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
