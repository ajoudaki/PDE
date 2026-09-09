"""Additional AST and mocked-consumer evidence; no research computation."""
import ast
import contextlib
import importlib
import io
import json
from pathlib import Path
import sys
from unittest import mock

ROOT = Path('/home/amir/Codes/PDE')
PRIVATE = Path('/tmp/pde-gaussian-routing-final.bJLzzv91')
manifest = json.loads((PRIVATE/'input_manifest.json').read_text())
by_path = {str(ROOT/row['path']): row for row in manifest['files']}
def tree(relative):
    path = ROOT/relative
    assert str(path) in by_path
    return ast.parse(path.read_text()), path
def extract(relative, names, env):
    parsed, path = tree(relative)
    nodes = [n for n in parsed.body if isinstance(n, ast.FunctionDef) and n.name in names]
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), 'exec'), env)
    return env
results = {}

# Execute the actual two run() bodies with every scientific test replaced.
hostile_rel = 'studies/mfp_gaussian_calculus/order5/audit_hostile.py'
parsed, path = tree(hostile_rel)
def no_work(): pass
env = {n.name: no_work for n in parsed.body if isinstance(n, ast.FunctionDef) and n.name.startswith('test_')}
env.update({'Path': Path, 'json': json, 'HERE': path.parent})
extract(hostile_rel, {'run', 'test_bounded_q0_spot_report'}, env)
outer = {'run_hostile': env['run'], 'run_compiler': no_work, 'run_finite_width': no_work}
extract('studies/mfp_gaussian_calculus/order5/run_checks.py', {'run'}, outer)
with contextlib.redirect_stdout(io.StringIO()) as log:
    try:
        outer['run']()
    except FileNotFoundError as error:
        results['root_runner_archive_bypass'] = {'type': type(error).__name__, 'filename': error.filename,
                                                'outer_calls': log.getvalue().splitlines()[:3],
                                                'science': 'all scientific checks mocked; original result reader retained'}

# Resolve only harmless top-level path declarations. No import, function or
# provenance gate is executed; compare retained hashes against the manifest.
def declarations(relative):
    parsed, path = tree(relative)
    ns = {'Path': Path, '__file__': str(path)}
    for n in parsed.body:
        if not isinstance(n, ast.Assign): continue
        calls = [c for c in ast.walk(n.value) if isinstance(c, ast.Call)]
        if any(not (isinstance(c.func, ast.Name) and c.func.id == 'Path'
                    or isinstance(c.func, ast.Attribute) and c.func.attr in ('resolve', 'with_name', 'with_suffix'))
               for c in calls): continue
        try:
            exec(compile(ast.Module(body=[n], type_ignores=[]), str(path), 'exec'), ns)
        except (NameError, AttributeError, TypeError): pass
    return ns
paths = [
    ('studies/mfp_cubic_compiler/two_input_plus_gaussian_program/audit_symbolic_order5.py', 'FILES'),
    ('studies/mfp_sine_compiler/depth2_gaussian_program/raw_sine_order5.py', ('PRIMARY','INDEPENDENT')),
    ('studies/mfp_sine_compiler/depth2_gaussian_program/normalized_sine_order5.py', ('PRIMARY','INDEPENDENT')),
    ('studies/mfp_sine_compiler/depth2_gaussian_program/sine_order9_stieltjes_audit.py', ('INPUT',)),
    ('studies/stieltjes_resolution/canonical_hidden_high_order/independent_hidden_scalar_audit.py', ('PRODUCTION_DEFAULT','INDEPENDENT_DEFAULT')),
    ('studies/stieltjes_resolution/independent_qalpha_recurrence_audit.py', ('JET_CERTIFICATE','INTERVAL_CERTIFICATE')),
]
results['retained_inputs'] = []
for relative, names in paths:
    ns = declarations(relative)
    values = ns[names] if isinstance(names, str) else {name: ns[name] for name in names}
    records = []
    for name, path in values.items():
        # Respect the other-study read exclusion even for existence checks.
        in_scope = any(path.is_relative_to(ROOT/'studies'/study) or path.is_relative_to(ROOT/'data/historical/studies'/study)
                       for study in manifest['scope'])
        row = {'name': name, 'path': str(path), 'exists': path.exists() if in_scope else 'out of scope; unchecked'}
        actual = by_path.get(str(path), {}).get('sha256_start')
        expected = ns.get('EXPECTED_SHA256', {}).get(name.lower()) or ns.get('EXPECTED_SHA256', {}).get(name)
        if actual and expected:
            row.update({'current_sha256': actual, 'expected_sha256': expected, 'matches_retained_seal': actual == expected})
        records.append(row)
    results['retained_inputs'].append({'source': relative, 'paths': records})

ns = declarations('studies/mfp_program_history/report/build_report.py')
results['report_build_destinations'] = {name: str(ns[name]) for name in ('REPORT_DIR','OUTPUT_DIR','BUILD_DIR','MARKDOWN_DIR','REPORT_TEX','REPORT_PDF')}

# The Gaussian scalar companion result readers receive the selected root.
relative = 'studies/mfp_gaussian_calculus/depth_order5_scalar/primary/audit_full_scalar_recurrence.py'
class ReadStop(Exception): pass
seen = []
def read_stop(path, *args, **kwargs):
    seen.append(str(path)); raise ReadStop()
ns = declarations(relative)
ns.update({'json': json})
extract(relative, {'nonpolynomial_regression'}, ns)
for root in (ROOT/'data/generated/mfp_gaussian_calculus', ROOT/'data/historical/studies/mfp_gaussian_calculus', PRIVATE/'selected'):
    with mock.patch.object(Path, 'read_text', read_stop):
        try: ns['nonpolynomial_regression'](root)
        except ReadStop: pass
results['scalar_result_first_reads'] = seen

print(json.dumps(results, indent=2))
