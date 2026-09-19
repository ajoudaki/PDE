"""Reproduce R1-B's deterministic algebra; no initialization/training run.

The review executed this calculation via standard input. This retained source
has the same numerical inputs, formulas, thresholds and resource caps. It
accepts a result path so a reproduction need not overwrite the review record.
Run from the checkout root with one numerical thread and the PYTHONPATH in
SCIENTIFIC_REVIEW_R1_B.md.
"""
import argparse
import contextlib
import hashlib
import io
import json
from pathlib import Path
import resource
import runpy
import signal
import time

resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
signal.alarm(60)
start = time.monotonic()

import numpy as np
import cx1_closure as c

parser = argparse.ArgumentParser()
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
if args.output.exists():
    raise ValueError('Choose a fresh result path')
base = Path('studies/cx1_many_point_closure_20260919')
for name in ('REVIEW_INPUTS_R1.json', 'REVIEW_DEPENDENCY_SUPPLEMENT_R1.json'):
    manifest = json.loads((base / name).read_text())
    assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest() == v
               for p, v in manifest.items())

certificate = io.StringIO()
with contextlib.redirect_stdout(certificate):
    runpy.run_path(str(base / 'check_reference_constants.py'), run_name='__main__')

ar = c.Arithmetic()
p1 = np.array([.0, .1, .2, .3, .4])
p2 = np.array([.2, .0, .15, .25, .1, .3])
b1 = np.sin(np.arange(20).reshape(5, 4) + .3)
b2 = np.cos(np.arange(18).reshape(6, 3) + .1)
g = .2 * np.sin(np.arange(25).reshape(5, 5) + .2)
w = g + .1 * np.cos(np.arange(25).reshape(5, 5))
read = .3 * np.sin(np.arange(6) + .4)
M = .2 * np.sin(np.arange(12).reshape(3, 4) + .3)
s = c.State(b1, g, w, p1, b2, read, p2, M, M.copy(), ar,
            {'scheme': 'cx1-general-d-dense-v1'}).validate()
u = np.eye(5)[:4]
u[0] = [3/5, 4/5, 0, 0, 0]
law = c.DataLaw(u, np.array([1., -1., 1., -1.]),
                np.array([.1, .2, .3, .4])).validate(ar)
v = c.rhs(s, law)
h = 1e-6
errs = []
for name, k, weights in [('w', 0, p1), ('c', 1, p2), ('M', 2, None)]:
    for index in np.ndindex(getattr(s, name).shape):
        a, b = s.copy(), s.copy()
        getattr(a, name)[index] += h
        getattr(b, name)[index] -= h
        numeric = (c.loss(a, law) - c.loss(b, law)) / (2*h)
        metric = 1 if weights is None else weights[index[0]]
        expected = -metric * v[k][index]
        errs.append(abs(numeric - expected))
assert max(errs) < 2e-9
left = s.dynamic_copy(*(getattr(s, n) + h*x
                        for n, x in zip(('w', 'c', 'M'), v)))
right = s.dynamic_copy(*(getattr(s, n) - h*x
                         for n, x in zip(('w', 'c', 'M'), v)))
energy = p1 @ np.sum(v[0]**2, axis=1) + p2 @ (v[1]**2) + np.sum(v[2]**2)
energy_error = abs((c.loss(left, law) - c.loss(right, law)) / (2*h) + energy)
assert energy_error < 2e-9
x = np.sin(np.arange(5))
y = np.cos(np.arange(6))
adjoint_error = abs(p2 @ (y*c.apply_action(s, x))
                    - p1 @ (x*c.apply_action(s, y, reverse=True)))
assert adjoint_error < 2e-14

ops = Path('data/generated/cx1_many_point_closure_20260919/operational_02')
record = json.loads((ops / 'record.json').read_text())
assert all(hashlib.sha256((ops / name).read_bytes()).hexdigest() == value
           for name, value in record['outputs'].items())
assert all(hashlib.sha256(Path(name).read_bytes()).hexdigest() == value
           for name, value in record['sources'].items())
results = {
    'status': 'passed',
    'scope': 'deterministic certificate and supplied-state algebra only; no training',
    'certificate_stdout': certificate.getvalue(),
    'gradient_coordinates': len(errs),
    'max_gradient_absolute_error': max(errs),
    'energy_absolute_error': energy_error,
    'adjoint_absolute_error': adjoint_error,
    'operational_02_output_hashes_verified': len(record['outputs']),
    'operational_02_source_hashes_verified': len(record['sources']),
    'seconds': time.monotonic() - start,
    'address_space_limit_bytes': 512 * 1024**2,
    'alarm_seconds': 60,
}
args.output.write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
