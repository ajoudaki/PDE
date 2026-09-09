"""Private stdlib/AST routing fixtures; no numerical work or repository writes."""
import argparse
import ast
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
from contextlib import redirect_stdout
from types import SimpleNamespace
from unittest.mock import MagicMock, Mock, patch

REPO = Path('/home/amir/Codes/PDE')
PRIVATE = Path('/tmp/pde-routing-acceptance-ntUaKfAN')

def interface(relative, names, **bindings):
    path = REPO / relative
    tree = ast.parse(path.read_text())
    nodes = [n for n in tree.body if
             (isinstance(n, ast.FunctionDef) and n.name in names) or
             (isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id in names for t in n.targets))]
    future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
    ns = dict(__file__=str(path), argparse=argparse, Path=Path, json=json,
              hashlib=hashlib, csv=csv, **bindings)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])), str(path), 'exec'), ns)
    return ns

def link(source, target, kind):
    target.parent.mkdir(parents=True, exist_ok=True)
    if kind == 'symlink':
        target.symlink_to(source)
    else:
        os.link(source, target)

def result(case, source, before, **extra):
    after = source.read_bytes()
    assert after != before, case + ': expected reproduction did not occur'
    print(json.dumps(dict(case=case, consumed_input_replaced=True,
                         before_sha256=hashlib.sha256(before).hexdigest(),
                         after_sha256=hashlib.sha256(after).hexdigest(), **extra)))

def manifest_cases():
    for name in ('manifest.json', 'SHA256SUMS'):
        for kind in ('symlink', 'hardlink'):
            with tempfile.TemporaryDirectory(dir=PRIVATE) as tmp:
                root = Path(tmp)
                source_root = root / 'source'
                source_root.mkdir()
                (source_root / 'program.py').write_text('# private source fixture\n')
                output = root / 'run'
                evidence = output / 'results/raw/consumed.npz'
                evidence.parent.mkdir(parents=True)
                evidence.write_bytes(b'private consumed trace sentinel\n')
                before = evidence.read_bytes()
                link(evidence, output / 'metadata' / name, kind)
                ns = interface('studies/resnet_dense_long_horizon/make_manifest.py',
                               {'main', 'validate_output_root', 'verify_manifest', 'EXCLUDED_PARTS', 'EXCLUDED_NAMES'},
                               ROOT=source_root, OUTPUT_ROOT=output)
                with patch.object(sys, 'argv', ['manifest', '--output-root', str(output)]), redirect_stdout(io.StringIO()):
                    ns['main']()
                result('manifest/' + name + '/' + kind, evidence, before)

def long_metadata_cases():
    for name in ('environment.json', 'run_manifest.json', 'source_sha256.txt'):
        for kind in ('symlink', 'hardlink'):
            with tempfile.TemporaryDirectory(dir=PRIVATE) as tmp:
                root = Path(tmp)
                output = root / 'run'
                evidence = output / 'results/raw/fixture.npz'
                evidence.parent.mkdir(parents=True)
                evidence.write_bytes(b'private reused trace sentinel\n')
                before = evidence.read_bytes()
                link(evidence, output / 'metadata' / name, kind)
                config = root / 'config.json'
                config.write_text('{}')
                consumed = []
                def load_trace(path):
                    consumed.append((path, path.read_bytes()))
                    return {'id': 'fixture', 'config_sha256': 'fixture-config'}, {}
                science = Mock(side_effect=AssertionError('training must never run'))
                validator = interface('studies/resnet_dense_long_horizon/make_manifest.py', {'validate_output_root'})
                ns = interface('studies/resnet_dense_long_horizon/run_all.py', {'main'},
                               ROOT=REPO / 'studies/resnet_dense_long_horizon', OUTPUT_ROOT=output,
                               source_hash=Mock(return_value='fixture-source'),
                               expand_config=Mock(return_value=[{'id':'fixture', 'group':'fixture'}]),
                               config_hash=Mock(return_value='fixture-config'), load_trace=load_trace,
                               run_trace=science, environment_record=Mock(return_value={'fixture':True}))
                with patch.dict(sys.modules, {'make_manifest': SimpleNamespace(validate_output_root=validator['validate_output_root'])}), \
                     patch.object(sys, 'argv', ['run_all', '--config', str(config), '--output-root', str(output), '--skip-analysis']), \
                     redirect_stdout(io.StringIO()):
                    ns['main']()
                assert consumed == [(evidence, before)]
                science.assert_not_called()
                result('long-run-metadata/' + name + '/' + kind, evidence, before)

def operator_inventory_cases():
    for kind in ('symlink', 'hardlink'):
        with tempfile.TemporaryDirectory(dir=PRIVATE) as tmp:
            root = Path(tmp)
            inputs, outputs = root / 'selected-evidence', root / 'generated'
            evidence = inputs / 'results/raw/fixture.npz'
            evidence.parent.mkdir(parents=True)
            evidence.write_bytes(b'private selected operator archive sentinel\n')
            before = evidence.read_bytes()
            link(evidence, outputs / 'audits/statistical_audit/inventory.csv', kind)
            consumed = []
            def load_archive(path):
                consumed.append((path, path.read_bytes()))
                return SimpleNamespace(path=path, arrays={'fixture':True})
            stop = Mock(side_effect=RuntimeError('private stop after first output'))
            ns = interface('studies/resnet_operator_core/audits/statistical_audit/analyze.py',
                           {'main', 'write_csv', 'RAW', 'NUM', 'OUT'},
                           INPUT_ROOT=inputs, OUTPUT_ROOT=outputs, load_archive=load_archive,
                           inventory_row=Mock(return_value={'name':'fixture.npz'}), integrity_row=stop)
            try:
                ns['main']()
            except RuntimeError as error:
                assert str(error) == 'private stop after first output'
            else:
                raise AssertionError('diagnostic did not stop')
            stop.assert_called_once()
            assert consumed == [(evidence, before)]
            result('operator-inventory/' + kind, evidence, before)

def early_intermediate_cases():
    for kind in ('symlink', 'hardlink'):
        with tempfile.TemporaryDirectory(dir=PRIVATE) as tmp:
            root = Path(tmp)
            evidence = root / 'response_singular_values_smooth_generic.npy'
            before = b'private regenerated singular-values sentinel\n'
            evidence.write_bytes(before)
            link(evidence, root / 'response_singular_value_decay.png', kind)
            class Vector:
                def __len__(self): return 2
                def __getitem__(self, key): return self if isinstance(key, slice) else 1
                def __truediv__(self, other): return self
            history = MagicMock()
            consumed = []
            def load(path):
                data = path.read_bytes()
                assert data == before
                consumed.append(path)
                return Vector()
            def snapshot(*args, out_dir, tag, **kwargs):
                (out_dir / f'response_singular_values_{tag}.npy').write_bytes(before)
            def savefig(path, **kwargs):
                path.write_bytes(b'private rendered plot sentinel\n')
            figure = SimpleNamespace(tight_layout=Mock(), savefig=savefig)
            axes = [Mock(), Mock()]
            plot = SimpleNamespace(subplots=Mock(side_effect=[(figure, axes), (figure, Mock())]), close=Mock())
            arrays = SimpleNamespace(linalg=SimpleNamespace(norm=Mock(return_value=1)),
                                     max=Mock(return_value=1), trapezoid=Mock(return_value=1),
                                     arange=Mock(return_value=()), maximum=Mock(return_value=()), load=load)
            ns = interface('studies/resnet_dense_early_audit/run_dense_resnet_audit.py',
                           {'truncated_training_experiment', 'write_csv'}, np=arrays, plt=plot,
                           make_data=Mock(return_value=(history, history)), initialize=Mock(return_value=history),
                           train=Mock(return_value=(history, history)),
                           compare_histories=Mock(side_effect=lambda *args: {'sup_output_l2_error':1, 'sup_all_depth_gram_fro_error':1}),
                           response_snapshot_audit=snapshot)
            ns['truncated_training_experiment'](root)
            assert evidence in consumed and len(consumed) == 4
            result('early-intermediate/final-plot/' + kind, evidence, before)

if __name__ == '__main__':
    manifest_cases()
    long_metadata_cases()
    operator_inventory_cases()
    early_intermediate_cases()
