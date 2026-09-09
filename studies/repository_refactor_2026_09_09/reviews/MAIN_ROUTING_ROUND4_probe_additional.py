"""Additional path/metadata checks, with every scientific operation mocked."""
from __future__ import annotations
import argparse
import ast
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from types import SimpleNamespace
from unittest.mock import patch

BASE = Path('/tmp/pde-main-routing-round4.MZx4oZmk')
REPO = Path('/home/amir/Codes/PDE')
Q = REPO / 'studies/mfp_quadratic_compiler'
H = REPO / 'data/historical/studies/mfp_quadratic_compiler'
tempfile.tempdir = str(BASE)
sys.dont_write_bytecode = True

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main_only(path, ns):
    tree = ast.parse(path.read_text())
    main = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'main')
    node = ast.Module(body=[main], type_ignores=[])
    exec(compile(node, str(path), 'exec'), ns)
    return ns

results = {}
with tempfile.TemporaryDirectory(prefix='additional-', dir=BASE) as tmp:
    scratch = Path(tmp)
    # Exercise the entire merge main with scalar/array operations stubbed.
    class FakeArray:
        size = 2
        def __getitem__(self, key):
            return self
        def __sub__(self, other):
            return self
    array = FakeArray()
    calls = []
    def load_raw(path):
        calls.append(str(path))
        return dict(times=array, seeds=array, f=array, grams=array, theta=array, metadata_json='{}')
    def save(handle, **kwargs):
        handle.write(b'mocked pooled archive; no scientific arrays')
    np = SimpleNamespace(array_equal=lambda *_: True, concatenate=lambda *_, **__: array,
        unique=lambda x: x, mean=lambda *_, **__: 0, array=lambda x: x,
        savez_compressed=save, min=lambda x: 1, max=lambda x: 2)
    ns = main_only(REPO / 'studies/resnet_operator_core/combine_references.py',
        dict(argparse=argparse, Path=Path, json=json, os=os, np=np, load_raw=load_raw, sem=lambda x: 0))
    items = []
    for mode in ('direct', 'partial'):
        output = scratch / (mode + '.npz')
        source = output if mode == 'direct' else output.with_suffix('.npz.partial')
        source.write_bytes(b'tiny raw fixture')
        before = sha(source)
        calls.clear()
        with patch.object(sys, 'argv', ['merge', str(source), '--output', str(output)]), contextlib.redirect_stdout(io.StringIO()):
            ns['main']()
        items.append({'mode': mode, 'input': str(source), 'output': str(output),
            'mock_load_calls': list(calls), 'input_before_sha256': before,
            'input_exists_after': source.exists(),
            'input_after_sha256': sha(source) if source.exists() else None,
            'output_after_sha256': sha(output)})
    results['merge_aliases'] = items

    # Read the long wrapper itself; override all its python commands by a shell
    # recorder. No unittest, producer, or manifest process is dispatched.
    wrapper = REPO / 'studies/resnet_dense_long_horizon/reproduce.sh'
    shell = '''python() { printf 'CALL'; printf '\\t%s' "$PWD" "$@"; printf '\\n'; }
export -f python
bash "$1"
'''
    cases = []
    for selection in ('relative run', '~/routing-never-created', str(scratch / 'with spaces')):
        env = dict(os.environ, PDE_LONG_HORIZON_OUTPUT_ROOT=selection, TMPDIR=str(BASE))
        p = subprocess.run(['bash', '-c', shell, 'probe', str(wrapper)], cwd=scratch,
                           env=env, capture_output=True, text=True)
        rows = [line.split('\t')[1:] for line in p.stdout.splitlines() if line.startswith('CALL\t')]
        cases.append({'selected': selection, 'returncode': p.returncode, 'calls': rows})
    results['long_wrapper_all_mocked'] = cases

    # Extract only shell code fences from the two current quadratic build guides.
    # g++, mkdir and every sector executable call are captured as shell text;
    # only bash syntax validation runs.
    guide_rows = []
    for path in (Q / 'SECTOR_ENGINE.md', Q / 'campaign6_f13_threshold/CAMPAIGN_REPORT.md'):
        content = path.read_text()
        blocks = re.findall(r'```(?:sh|bash)\n(.*?)```', content, re.S)
        for block in blocks:
            if 'g++' not in block:
                continue
            p = subprocess.run(['bash', '-n'], input=block, capture_output=True, text=True)
            srcs = re.findall(r'(?m)^\s+(studies/[^\s]+\.cpp)', block)
            guide_rows.append({'guide': str(path.relative_to(REPO)), 'syntax_exit': p.returncode,
                'sources': {s: (REPO / s).is_file() for s in srcs},
                'commands_executed': 'bash -n only; no build or sector invocation'})
    results['build_guides'] = guide_rows

# Parse only source metadata from the retained provenance JSON. No mathematics.
rows = []
for campaign, record, fields in (
    ('campaign2', 'provenance_order7.json', {
        'source_sha256': 'two_input_connected.cpp', 'reference_source_sha256': 'two_input_reference.py',
        'postprocess_source_sha256': 'postprocess.py', 'certificates_sha256': 'certificates_order7.json'}),
    ('campaign3', 'provenance_order7.json', {
        'source_sha256': 'centered_connected.cpp', 'reference_source_sha256': 'centered_reference.py',
        'postprocess_source_sha256': 'postprocess.py', 'certificates_sha256': 'certificates_order7.json'}),
    ('campaign4', 'provenance_order9.json', {
        'protocol_sha256': 'PROTOCOL.md', 'wrapper_source_sha256': 'sector_wrapper.cpp',
        'runner_sha256': 'run_sectors.py', 'reference_source_sha256': 'bivariate_reference.py',
        'postprocessor_sha256': 'postprocess.py', 'provenance_builder_sha256': 'make_provenance.py',
        'certificate_sha256': 'certificates_order9.json'}),
):
    record_path = H / campaign / record
    data = json.loads(record_path.read_text())
    fields_source = data.get('hashes', data)
    for key, filename in fields.items():
        source = Q / campaign / filename
        rows.append({'source': str(source.relative_to(REPO)), 'record': str(record_path.relative_to(REPO)),
                     'field': key, 'expected': fields_source[key], 'actual': sha(source),
                     'matches': fields_source[key] == sha(source)})
results['historical_source_seals_read_only'] = rows
ledger = json.loads((H / 'campaign4/production_budget.json').read_text())
results['campaign4_budget_metadata'] = ledger

# Resolve depth-3 INPUT constants without importing external study dependencies.
rows = []
for name in ('depth3_stieltjes_audit.py', 'depth3_order13_stieltjes_audit.py'):
    path = Q / 'depth3_gaussian_program' / name
    tree = ast.parse(path.read_text())
    nodes = [n for n in tree.body if isinstance(n, ast.Assign)
             and any(isinstance(t, ast.Name) and t.id in ('HERE', 'INPUT') for t in n.targets)]
    with patch.dict(os.environ, {'PDE_QUADRATIC_INPUT_ROOT': str(BASE / 'selected-depth3')}, clear=True):
        ns = dict(Path=Path, __file__=str(path))
        exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), 'exec'), ns)
    rows.append({'source': str(path.relative_to(REPO)), 'selected_env': str(BASE / 'selected-depth3'),
                 'resolved_input': str(ns['INPUT'])})
results['depth3_fixed_inputs'] = rows
rows = []
for relative, names in (
    ('campaign5_b3/postprocess_lower_moments.py', {'HERE', 'DATA', 'STAGE_A', 'STAGE_B'}),
    ('campaign1/test_order9_q2_order8.py', {'HERE', 'RAW', 'COMPACT', 'PROVENANCE'}),
):
    path = Q / relative
    tree = ast.parse(path.read_text())
    nodes = [n for n in tree.body if isinstance(n, ast.Assign)
             and any(isinstance(t, ast.Name) and t.id in names for t in n.targets)]
    with patch.dict(os.environ, {'PDE_QUADRATIC_INPUT_ROOT': str(BASE / 'selected-campaign')}, clear=True):
        ns = dict(Path=Path, __file__=str(path))
        exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), 'exec'), ns)
    rows.append({'source': str(path.relative_to(REPO)), 'selected_env': str(BASE / 'selected-campaign'),
                 'resolved_paths': {key: str(ns[key]) for key in sorted(names - {'HERE'})}})
results['other_fixed_inputs'] = rows
print(json.dumps(results, indent=2))
