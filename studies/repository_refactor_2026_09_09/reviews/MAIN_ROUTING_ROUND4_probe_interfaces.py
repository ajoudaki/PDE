"""Private stdlib interface probes. Scientific operations are mocks only."""
from __future__ import annotations
import argparse
import ast
import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
from unittest.mock import patch

BASE = Path('/tmp/pde-main-routing-round4.MZx4oZmk')
REPO = Path('/home/amir/Codes/PDE')
QUAD = REPO / 'studies/mfp_quadratic_compiler'
LONG = REPO / 'studies/resnet_dense_long_horizon'
OP = REPO / 'studies/resnet_operator_core'
tempfile.tempdir = str(BASE)
sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
os.environ['TMPDIR'] = str(BASE)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load(path):
    spec = importlib.util.spec_from_file_location('private_routing_module', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def functions(path, names, namespace):
    tree = ast.parse(path.read_text())
    selected = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
    assert len(selected) == len(names)
    code = ast.Module(body=[ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0), *selected], type_ignores=[])
    ast.fix_missing_locations(code)
    namespace['__file__'] = str(path)
    exec(compile(code, str(path), 'exec'), namespace)
    return namespace

def call_main(ns, args):
    stdout, stderr = io.StringIO(), io.StringIO()
    with patch.object(sys, 'argv', ['probe', *map(str, args)]), contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        try:
            ns['main']()
            status = 'completed'
        except BaseException as exc:
            status = f'{type(exc).__name__}: {exc}'
    return dict(status=status, stdout=stdout.getvalue(), stderr=stderr.getvalue())

results = {}
# Parse every permitted Python source, without importing its dependencies.
sources = []
for name in ('resnet_dense_long_horizon', 'resnet_dense_early_audit', 'resnet_operator_core', 'mfp_quadratic_compiler'):
    for path in sorted((REPO / 'studies' / name).rglob('*.py')):
        ast.parse(path.read_text(), filename=str(path))
        sources.append(str(path.relative_to(REPO)))
results['syntax'] = {'python_count': len(sources), 'all_pass': True}

with tempfile.TemporaryDirectory(prefix='private-', dir=BASE) as tmp:
    scratch = Path(tmp)
    # The full Campaign-4 entrypoint, with compute replaced by an inert stub.
    # Its actual atomic writer can only affect these tiny fixture files.
    input_path = scratch / 'campaign4-results.json'
    input_path.write_text('{"fixture":"raw input"}\n')
    consumed = []
    def fake_compute(path):
        consumed.append(str(path))
        return {'fixture': 'certificate replacement', 'shifted_H1': {
            'decision': {'status': 'mocked'}, 'numerator_term_count': 0}}
    ns = functions(QUAD / 'campaign4/postprocess.py', {'main', 'atomic_json'}, dict(
        argparse=argparse, Path=Path, json=json, os=os, tempfile=tempfile,
        INPUT_ROOT=scratch, OUTPUT_ROOT=scratch / 'output', compute=fake_compute, sha256=sha))
    before = sha(input_path)
    event = call_main(ns, ['--input', input_path, '--output', input_path])
    event.update(input=str(input_path), read_by_mock=consumed, before_sha256=before,
                 after_sha256=sha(input_path), input_replaced=before != sha(input_path))
    results['campaign4_input_alias'] = event

    # Full early projection main, stopping at the first scientific boundary.
    # mkdir is mocked too, so even its chosen output directory is never created.
    scientific = []
    class StopScientific(Exception):
        pass
    def fake_make_data(*args, **kwargs):
        scientific.append({'args': args, 'kwargs': kwargs})
        raise StopScientific('first scientific call intercepted')
    ns = functions(REPO / 'studies/resnet_dense_early_audit/run_response_galerkin_projection.py',
                   {'main'}, dict(Path=Path, os=os, make_data=fake_make_data))
    events = []
    for args in (['--help'], ['--out', str(scratch / 'selected')], ['--not-a-supported-flag']):
        scientific.clear()
        with patch.dict(os.environ, {'GALERKIN_OUT': str(scratch / 'early-output')}), patch.object(Path, 'mkdir') as mkdir:
            event = call_main(ns, args)
            event.update(argv=args, mkdir_calls=mkdir.call_count,
                         scientific_calls=list(scientific), output_exists=(scratch / 'early-output').exists())
            events.append(event)
    results['early_projection_flags'] = events

    # Protected-root normalization includes symlink and dot-dot aliases.
    (scratch / 'source-link').symlink_to(OP, target_is_directory=True)
    checks = []
    for file, var in ((OP / 'runtime_paths.py', 'PDE_OPERATOR_OUTPUT_ROOT'),
                      (QUAD / 'campaign_paths.py', 'PDE_QUADRATIC_OUTPUT_ROOT')):
        for selected in (scratch / 'source-link', REPO / 'data/generated/../../studies', REPO, REPO / 'data'):
            with patch.dict(os.environ, {var: str(selected)}, clear=True):
                try:
                    load(file)
                    outcome = 'accepted'
                except ValueError:
                    outcome = 'rejected'
            checks.append({'helper': file.name, 'selected': str(selected), 'outcome': outcome})
    results['protected_aliases'] = checks

    # Default/explicit certificate roles, with imports only (no fixtures loaded).
    checks = []
    for env in ({}, {'PDE_QUADRATIC_INPUT_ROOT': str(scratch / 'chosen-evidence'),
                      'PDE_QUADRATIC_OUTPUT_ROOT': str(scratch / 'chosen-output')}):
        with patch.dict(os.environ, env, clear=True):
            helper = load(QUAD / 'campaign_paths.py')
            checks.append({'input': str(helper.INPUT_ROOT), 'output': str(helper.OUTPUT_ROOT),
                'certificate': str(helper.certificate_path('campaign4/certificates_order9.json')),
                'centered_data': str(helper.INPUT_ROOT / 'centered_depth1_order13/RESULTS.json')})
    results['quadratic_roles'] = checks

    # Schema-2 checks: source/run roots and checksum-file agreement.
    helper = load(LONG / 'make_manifest.py')
    source, run = scratch / 'source', scratch / 'run'
    source.mkdir()
    run.mkdir()
    (source / 'source.txt').write_text('tiny source')
    (run / 'result.txt').write_text('tiny result')
    helper.ROOT = source
    with patch.object(sys, 'argv', ['manifest', '--output-root', str(run)]), contextlib.redirect_stdout(io.StringIO()):
        helper.main()
    manifest_file = run / 'metadata/manifest.json'
    sums_file = run / 'metadata/SHA256SUMS'
    baseline = manifest_file.read_text()
    baseline_sums = sums_file.read_text()
    variants = {}
    variants['valid'] = json.loads(baseline)
    bad = json.loads(baseline); bad['schema'] = 1; variants['schema1'] = bad
    bad = json.loads(baseline); bad['files'].append(bad['files'][0]); variants['duplicate'] = bad
    bad = json.loads(baseline); bad['files'][0]['root'] = 'other'; variants['unknown_root'] = bad
    bad = json.loads(baseline); bad['files'][0]['path'] = '../result.txt'; variants['traversal'] = bad
    bad = json.loads(baseline); bad['files'][0]['path'] = str(run / 'result.txt'); variants['absolute_entry'] = bad
    bad = json.loads(baseline); bad['roots']['run'] = str(source); variants['wrong_run_root'] = bad
    (source / 'escape').symlink_to(run / 'result.txt')
    bad = json.loads(baseline); bad['files'][0]['path'] = 'escape'; variants['symlink_escape'] = bad
    variants['companion_mismatch'] = json.loads(baseline)
    variants['tampered_result'] = json.loads(baseline)
    checks = {}
    for name, variant in variants.items():
        manifest_file.write_text(json.dumps(variant))
        sums_file.write_text(baseline_sums if name != 'companion_mismatch' else 'wrong\n')
        (run / 'result.txt').write_text('changed result' if name == 'tampered_result' else 'tiny result')
        frozen_manifest, frozen_sums = sha(manifest_file), sha(sums_file)
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                helper.verify_manifest(manifest_file)
            outcome = 'accepted'
        except Exception as exc:
            outcome = f'{type(exc).__name__}: {exc}'
        checks[name] = {'outcome': outcome, 'verifier_read_only':
                       sha(manifest_file) == frozen_manifest and sha(sums_file) == frozen_sums}
    results['schema2'] = checks

    # Benchmark: full wrapper entrypoint with subprocess replaced; no executable
    # is ever dispatched. Fake executable content is a plain text sentinel.
    binary = scratch / 'mock-executable'
    binary.write_text('mock binary bytes, never executable')
    output = scratch / 'benchmark-output'
    calls = []
    def fake_run(command, **kwargs):
        calls.append({'command': command, 'cwd': str(kwargs.get('cwd')), 'timeout': kwargs.get('timeout')})
        return SimpleNamespace(returncode=0, stdout='mock stdout', stderr='')
    with patch.dict(os.environ, {'PDE_QUADRATIC_OUTPUT_ROOT': str(output)}, clear=True):
        helper = load(QUAD / 'campaign_paths.py')
        with patch.dict(sys.modules, {'campaign_paths': helper}):
            bench = load(QUAD / 'campaign6_f13_threshold/run_benchmark.py')
    with patch.object(bench.subprocess, 'run', fake_run):
        event = call_main(vars(bench), ['tiny', binary, '9', '1'])
        rejected = call_main(vars(bench), ['../bad', binary])
    event.update(calls=calls, output_file=str(output / 'campaign6_f13_threshold/tiny.benchmark.json'),
                 rejected_name=rejected['status'], binary_unchanged=sha(binary) == hashlib.sha256(b'mock binary bytes, never executable').hexdigest())
    results['campaign6_mocked'] = event

print(json.dumps(results, indent=2))
