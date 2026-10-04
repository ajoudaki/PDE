"""Authorized posthoc algebra on preserved same-state matrices only."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import time

for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import numpy as np


def main():
    start = time.monotonic()
    study = Path(__file__).resolve().parent
    root = study.parents[1]
    relative = Path('data/generated/structured_full_rank_scalar_20260926/current_correlation_20260930')
    folder = root/relative/'same_state'
    destination = folder/'decomposition.json'
    if destination.exists():
        raise FileExistsError(destination)
    diag_path = folder/'input_snapshot'/relative/'diagnostic/diagnostic.json'
    raw = diag_path.read_bytes()
    rows = json.loads(raw)['tasks']
    script = Path(__file__).read_bytes()
    (folder/'sources'/Path(__file__).name).write_bytes(script)
    out = {'scope': 'posthoc saved-matrix algebra; no dense evaluation or fit',
           'source_sha256': hashlib.sha256(script).hexdigest(),
           'input_sha256': {str(diag_path.relative_to(root)): hashlib.sha256(raw).hexdigest()},
           'tasks': []}
    for row in rows:
        task = row['task']
        path = folder/f'{task}__same_state.npz'
        out['input_sha256'][str(path.relative_to(root))] = hashlib.sha256(path.read_bytes()).hexdigest()
        with np.load(path, allow_pickle=False) as saved:
            beta, GA, D, NA, N = [saved[k] for k in ('beta','A_gate','exact_gate','A_lower','exact_lower')]
        optimistic = beta*D
        gate = beta*(GA-D)
        hidden = optimistic-N
        defect = float(np.max(abs(gate+hidden-(NA-N))))
        assert defect < 1e-12
        directions = {}
        for name in ('residual_unit', 'weak_initial_unit'):
            v = np.asarray(row['contractions'][name]['direction'])
            exact = float(v@N@v)
            g = float(v@gate@v)
            h = float(v@hidden@v)
            directions[name] = {'exact_lower':exact, 'A_lower':float(v@NA@v),
                                'optimistic_lower':float(v@optimistic@v),
                                'gate_signed_error':g, 'hidden_signed_error':h,
                                'gate_signed_relative_error':g/abs(exact) if exact else None,
                                'hidden_signed_relative_error':h/abs(exact) if exact else None}
        norm = float(np.linalg.norm(N))
        out['tasks'].append({'task':task, 'sum_identity_max_abs_error':defect,
                            'exact_lower_frobenius':norm,
                            'gate_error_frobenius':float(np.linalg.norm(gate)),
                            'hidden_error_frobenius':float(np.linalg.norm(hidden)),
                            'gate_relative_frobenius':float(np.linalg.norm(gate))/norm,
                            'hidden_relative_frobenius':float(np.linalg.norm(hidden))/norm,
                            'total_relative_frobenius':float(np.linalg.norm(NA-N))/norm,
                            'optimistic_lower':optimistic.tolist(),
                            'gate_signed_matrix':gate.tolist(),
                            'hidden_signed_matrix':hidden.tolist(), 'directions':directions})
    out['wall_seconds'] = time.monotonic()-start
    assert out['wall_seconds'] < 1., 'Unexpected saved-matrix analysis cost'
    destination.write_text(json.dumps(out, indent=2, allow_nan=False)+'\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
