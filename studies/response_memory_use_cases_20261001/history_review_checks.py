"""Small independent oracles and saved-evidence audit; no research sweep.

Run with /home/amir/miniconda3/bin/python -B from the repository root.
The full seed201 reproduction is a separate, already specified producer run.
"""
import copy
import hashlib
import json
from pathlib import Path
import platform
import sys
import time

import numpy as np
import torch

from history_probe import (edit_score, interval_coefficients, make_data, new_flow,
                           train_record)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DATA = ROOT / 'data/generated/response_memory_use_cases_20261001'
OUT = DATA / 'history_independent_review01'
SOURCE_NAMES = ['baseline_compact_flow.py', 'history_probe.py',
                'history_probe_initial.py', 'history_controls.py',
                'HISTORY_PROTOCOL.md', 'HISTORY_CONTROL_PROTOCOL.md',
                'MODEL_RECONCILIATION.md']
RUN_NAMES = ['history_pilot01', 'history_pilot02', 'history_confirm01',
             'history_refine01', 'history_controls01']


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def quadrature_coefficients(masses, q):
    """Independent Gauss quadrature of each polynomial on each interval."""
    nodes, weights = np.polynomial.legendre.leggauss(40)
    total = sum(masses)
    answer = np.zeros((q, len(masses)))
    left = 0.
    for a, width in enumerate(masses):
        locations = left + (nodes + 1) * width / 2
        for k in range(q):
            basis = np.polynomial.Legendre.basis(k)
            answer[k, a] = (width / 2 * np.dot(weights, basis(2 * locations / total - 1))
                            * np.sqrt((2 * k + 1) / total))
        left += width
    return answer


def main():
    start = time.perf_counter()
    result = {'command': sys.argv, 'python': sys.executable,
              'platform': platform.platform(), 'torch': torch.__version__,
              'numpy': np.__version__, 'threads': torch.get_num_threads(),
              'source_hashes': {n: sha(HERE / n) for n in SOURCE_NAMES},
              'check_source_sha256': sha(Path(__file__))}
    torch.set_num_threads(1)
    # Autograd differentiates a direct dense forward pass at a nonzero readout.
    x, y, query, truth = make_data()
    model = new_flow(x, y, 7, 992, 'cpu')
    model.c.copy_(torch.linspace(-.4, .8, 7, dtype=torch.float64))
    parameters = [v.clone().requires_grad_(True) for v in model.state]
    first, hidden, readout = parameters
    prediction = readout @ torch.tanh(hidden @ torch.tanh(first @ model.inputs.T)) / 7
    loss = ((prediction - model.labels) ** 2).mean()
    gradients = torch.autograd.grad(loss, parameters)
    velocity = model.rhs()
    errors = [float((v + mobility * g).abs().max())
              for v, g, mobility in zip(velocity, gradients, (7, 1, 7))]
    assert max(errors) < 1e-13
    result['autograd_velocity_max_abs_by_layer'] = errors
    # Integral oracle includes zero-mass intervals and unequal activity lengths.
    masses = np.array([0., .13, 1.7, 0., .007, 2.5])
    exact = quadrature_coefficients(masses, 32)
    computed = interval_coefficients(masses, 32)
    error = float(np.max(np.abs(exact - computed)))
    assert error < 2e-13
    result['legendre_integral_max_abs_q32'] = error
    # Tiny state-based observer check, independent quadrature, and accumulated
    # sample writes checked against direct per-example autograd differentiation.
    before = [v.clone() for v in model.state]
    expected_per_sample = []
    for a in range(model.M):
        w = before[1].clone().requires_grad_(True)
        h = torch.tanh(before[0] @ model.inputs[a])
        f = before[2] @ torch.tanh(w @ h) / model.n
        gradient = torch.autograd.grad((f - model.labels[a]) ** 2 / model.M, w)[0]
        expected_per_sample.append(-.001 * gradient)
    one = copy.deepcopy(model)
    history_one = train_record(one, .001, .001)
    sample_error = float((history_one['per_sample'] - torch.stack(expected_per_sample)).abs().max())
    assert sample_error < 1e-16
    result['per_sample_autograd_write_max_abs'] = sample_error
    hist = train_record(model, .016, .001)
    quad = torch.from_numpy(quadrature_coefficients(hist['mass'], 8))
    observer_errors = {}
    for key in ('h', 'b'):
        oracle = torch.einsum('jt,tia->jia', quad, hist[key])
        err = float((hist['online_' + key] - oracle).norm() / oracle.norm())
        assert err < 1e-8
        observer_errors[key] = err
    result['online_vs_quadrature_relative_q8'] = observer_errors
    # The edit is isolated to a copy and adds the supplied matrix with its sign.
    saved = [v.clone() for v in model.state]
    delta = -hist['per_sample'][[1, 7]].sum(0)
    score = edit_score(model, delta, query, truth, y, 0.)
    direct = copy.deepcopy(model)
    direct.matrices[0].add_(delta)
    oracle_test_mse = float(((direct.predict(query) - torch.from_numpy(truth)) ** 2).mean())
    assert score['immediate']['test_mse'] == oracle_test_mse
    assert all(torch.equal(a, b) for a, b in zip(saved, model.state))
    result['edit_isolation_and_addition'] = True
    # This edge is outside the positive-activity experiment, but document the
    # helper's current behavior rather than silently treating it as supported.
    zero = new_flow(x, np.zeros_like(y), 7, 992, 'cpu')
    stationary = train_record(zero, .001, .001)
    result['zero_activity_helper_returns_finite_moments'] = bool(
        torch.isfinite(stationary['online_h']).all()
        and torch.isfinite(stationary['online_b']).all())
    assert all(torch.equal(a, b) for a, b in zip(zero.state,
        new_flow(x, np.zeros_like(y), 7, 992, 'cpu').state))
    # Inspect every supplied generated file and verify producer archive hashes.
    evidence_hashes, hashes_ok, duplicate_json_ok = {}, True, True
    for name in RUN_NAMES:
        folder = DATA / name
        evidence_hashes[name] = {p.name: sha(p) for p in sorted(folder.iterdir()) if p.is_file()}
        completion = json.loads((folder / 'completion.json').read_text())
        for filename, digest in completion.get('hashes', {}).items():
            hashes_ok &= evidence_hashes[name][filename] == digest
        rows = json.loads((folder / 'results.json').read_text())
        for row in rows:
            if 'corrupt' in row:
                filename = f"seed{row['seed']}_" + ('repair' if row['corrupt'] else 'coordination') + '.json'
                duplicate_json_ok &= row == json.loads((folder / filename).read_text())
    assert hashes_ok and duplicate_json_ok
    result['evidence_file_hashes'] = evidence_hashes
    result['saved_archive_hashes_and_duplicate_json_pass'] = True
    # Scientific numbers and saved arrays must match the independently executed
    # specified producer run. Wall time is the sole deliberately excluded field.
    original = json.loads((DATA / 'history_confirm01/seed201_repair.json').read_text())
    reproduction = json.loads((OUT / 'seed201_repair.json').read_text())
    original.pop('training_seconds')
    reproduction.pop('training_seconds')
    assert original == reproduction
    result['reproduction_scientific_json_bitwise_equal'] = True
    array_differences = {}
    with np.load(DATA / 'history_confirm01/seed201_repair.npz') as a, np.load(OUT / 'seed201_repair.npz') as b:
        assert a.files == b.files
        for key in a.files:
            array_differences[key] = float(np.max(np.abs(a[key] - b[key])))
            assert np.array_equal(a[key], b[key])
    result['reproduction_array_max_abs_differences'] = array_differences
    controls = json.loads((DATA / 'history_controls01/results.json').read_text())
    for row in controls:
        for name in ('history', 'current_gradient'):
            candidates = row[name]['candidates']
            assert [r['alpha'] for r in candidates] == [0., .25, .5, 1., 2., 4.]
            assert min(candidates, key=lambda r:r['immediate']['train_mse']) == row[name]['selected']
        assert abs(row['history']['candidates'][3]['edit_norm'] -
                   row['current_gradient']['candidates'][3]['edit_norm']) < 1e-12
    result['saved_control_train_only_selection_and_base_norm_match'] = True
    result['seconds'] = time.perf_counter() - start
    (OUT / 'review_checks.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'evidence_file_hashes'}, indent=2))


if __name__ == '__main__':
    main()
