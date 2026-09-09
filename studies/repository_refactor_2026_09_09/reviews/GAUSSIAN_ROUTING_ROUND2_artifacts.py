"""Artifact binding and digest gates only; no recurrence evaluation."""
import ast
import hashlib
import json
from pathlib import Path
from unittest import mock
from bounded import BASE, OUT
from acceptance import module, note, rows

inventory = json.loads((OUT / 'hashes-start.json').read_text())
hashes = {BASE / row['path']: row['sha256'] for group in inventory.values() for row in group if 'sha256' in row}

def constants(relative, names):
    path = BASE / 'studies' / relative
    tree = ast.parse(path.read_text())
    env = {'Path': Path, '__file__': str(path)}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) and node.targets[0].id in names:
            exec(compile(ast.Module(body=[node], type_ignores=[]), str(path), 'exec'), env)
    return env

for relative in ('mfp_sine_compiler/depth2_gaussian_program/raw_sine_order5.py',
                 'mfp_sine_compiler/depth2_gaussian_program/normalized_sine_order5.py',
                 'mfp_sine_compiler/depth2_gaussian_program/sine_order9_stieltjes_audit.py'):
    data = constants(relative, {'HERE', 'REPO', 'PROTOCOL', 'PRIMARY', 'INDEPENDENT', 'INPUT', 'ENGINE', 'EXPECTED_SHA256'})
    bindings = {key.lower(): value for key, value in data.items() if key in ('PROTOCOL', 'PRIMARY', 'INDEPENDENT', 'INPUT', 'ENGINE')}
    for key, expected in data['EXPECTED_SHA256'].items():
        if key not in bindings:
            note('Sine unchecked binding', source=relative, key=key, expected=expected)
            continue
        path = bindings[key]
        actual = hashes.get(path)
        note('Sine artifact path/hash', source=relative, role=key, path=path,
             expected=expected, actual=actual, match=actual == expected,
             limit='Only named literal/path assignments evaluated; no dependency import or mathematical evaluation')

cubic = module('mfp_cubic_compiler/two_input_plus_gaussian_program/audit_symbolic_order5.py')
for key, path in cubic.FILES.items():
    expected = cubic.EXPECTED_SHA256[key]
    actual = hashes.get(path)
    note('Cubic artifact path/hash', role=key, path=path, expected=expected, actual=actual,
         match=actual == expected if actual is not None else 'outside allowed scope; not read')

fixed = module('mfp_cubic_compiler/two_input_plus_gaussian_program/two_input_cubic_plus_fixed_rho_jet.py')
try:
    fixed.assert_source_hashes()
except AssertionError as exc:
    note('Actual cubic frozen hash gate refuses', error=str(exc), limit='source_hashes/assert_source_hashes only; no jets')
else:
    note('Actual cubic fixed-rho input gate', passed=True, limit='Only source_hashes/assert_source_hashes; no coefficient work')

for relative in ('stieltjes_resolution/canonical_hidden_high_order/hidden_moment_hankel_audit.py',
                 'stieltjes_resolution/canonical_hidden_high_order/independent_hidden_scalar_audit.py'):
    m = module(relative)
    paths = ((m.PRODUCTION_RESULT, m.INDEPENDENT_RESULT) if hasattr(m, 'PRODUCTION_RESULT') else (m.PRODUCTION_DEFAULT, m.INDEPENDENT_DEFAULT))
    for path in paths:
        doc = json.loads(path.read_text())
        note('Stieltjes selected retained result', consumer=relative, path=path, sha256=hashes[path], source_record=doc['source'])
        if hasattr(m, 'validate_source'):
            try:
                result = m.validate_source(doc, path)
                note('Stieltjes actual source validator', retained=path, result=result)
            except (AssertionError, FileNotFoundError, PermissionError) as exc:
                note('Stieltjes actual source validator refuses', retained=path, error=repr(exc), missing=getattr(exc, 'filename', None),
                     limit='validate_source only; out-of-scope former-layout read denied before access; no determinant or result audit')
        else:
            source_path = m.HERE / ('production_hidden_recurrence.py' if path == paths[0] else 'independent_hidden_recurrence.py')
            note('Stieltjes fixed-source boolean gate', source=source_path,
                 expected=doc['source']['sha256'], actual=hashes[source_path],
                 result=m._source_hash_gate(doc, source_path))

production = module('stieltjes_resolution/canonical_high_order/production_canonical_recurrence.py')
try:
    production.verify_frozen_inputs()
except AssertionError as exc:
    note('Actual Stieltjes frozen hash gate refuses', expected_source=production.FROZEN_SOURCE_SHA256,
         actual=production.frozen_hashes(), error=str(exc), limit='hash guard stops before certificate arithmetic or recurrence')

# Source/result records for canonical recurrences: inspect only binding metadata.
for subdir, name, source in (
    ('canonical_high_order', 'PRODUCTION_RESULT.json', 'production_canonical_recurrence.py'),
    ('canonical_high_order', 'INDEPENDENT_RESULT.json', 'independent_canonical_recurrence.py'),
):
    data_path = BASE / 'data/historical/studies/stieltjes_resolution' / subdir / name
    source_path = BASE / 'studies/stieltjes_resolution' / subdir / source
    record = json.loads(data_path.read_text())['source']
    note('Canonical retained source hash', retained=data_path, source=source_path,
         expected=record['sha256'], actual=hashes[source_path], match=record['sha256'] == hashes[source_path])

(OUT / 'artifacts.json').write_text(json.dumps(rows, indent=2, default=str) + '\n')
