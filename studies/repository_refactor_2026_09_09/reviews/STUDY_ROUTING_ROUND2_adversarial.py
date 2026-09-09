"""Independent tiny boundary probes. Never import or run a scientific campaign.

Actual functions are AST-compiled with postponed annotations. Numeric kernels
are substituted only in the jet writer fixture; it stops after its first small
NPZ write. All toy source/history/generated paths are beneath this directory.
"""
import argparse
import ast
import contextlib
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import resource
import runpy
import sys
import tempfile
from types import SimpleNamespace
from unittest import mock

import numpy as np
from read_inputs import BASE, OUT, read
from bounded_tests import guard

sys.dont_write_bytecode = True
sys.path.insert(0, str(BASE))

def functions(rel, names, env):
    tree = ast.parse(read(rel))
    nodes = [node for node in tree.body if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in names]
    assert {n.name for n in nodes} == set(names)
    future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
    env.setdefault('__file__', str(BASE / rel))
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])), str(BASE / rel), 'exec'), env)
    return env

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def jet_alias_fixture(parent, kind):
    from studies.stieltjes_finite_width import run_paths as paths
    repo = parent / ('jet-' + kind) / 'toy-repo'
    inputs = repo / 'data/historical/studies/stieltjes_direct_loewner/run'
    output = repo / 'data/generated/stieltjes_finite_width/run'
    inputs.mkdir(parents=True)
    output.mkdir(parents=True)
    raw = inputs / 'raw_width_64.npz'
    np.savez(raw, pair_g=np.ones((1, 3)), times=np.array([0., .1, .2]))
    destination = output / 'jets_and_cv_width_64.npz'
    if kind == 'symlink':
        destination.symlink_to(raw)
    else:
        os.link(raw, destination)
    before = digest(raw)
    class StopAfterFirstWrite(Exception):
        pass
    handles = []
    def load(path):
        handle = np.load(path)
        handles.append(handle)
        return handle
    def save(path, **arrays):
        np.savez_compressed(path, **arrays)
        raise StopAfterFirstWrite
    env = functions('studies/stieltjes_finite_width/jet_control_variate.py', ['main'],
        dict(OUT=output, RUN=inputs, HISTORICAL_RUN=inputs, WIDTHS=(64,),
             R0=0., R1=0., G0=0., G2=0., parse_paths=paths.parse_paths,
             np=SimpleNamespace(load=load, savez_compressed=save),
             regenerate_pair_jets=lambda width: np.zeros((1, 4))))
    with mock.patch.object(paths, 'REPO_ROOT', repo), mock.patch.object(paths, 'GENERATED_ROOT', repo/'data/generated/stieltjes_finite_width'), mock.patch.object(sys, 'argv', ['jet']), contextlib.redirect_stdout(io.StringIO()):
        # Verify that selecting history directly is rejected by this same helper.
        with contextlib.redirect_stderr(io.StringIO()):
            try:
                paths.parse_paths(output, ['--output-dir', str(inputs)])
            except SystemExit:
                pass
            else:
                raise AssertionError('direct history unexpectedly accepted')
        try:
            env['main']()
        except StopAfterFirstWrite:
            pass
        finally:
            for handle in handles:
                handle.close()
    after = digest(raw)
    with np.load(raw) as archive:
        keys = archive.files
    assert before != after and set(keys) == {'jets', 'corrected'}
    return dict(link=kind, retained_input=str(raw), output=str(destination),
                before_sha256=before, after_sha256=after, new_keys=keys,
                default_output_accepted=True, direct_historical_output_rejected=True,
                scientific_kernels_executed=False)

def generalization_partial_fixture(parent, kind):
    from studies.resnet_generalization import generalization_paths as paths
    root = parent / ('generalization-' + kind)
    history = root / 'toy-repo/data/historical/studies/resnet_generalization/input.bin'
    history.parent.mkdir(parents=True)
    history.write_bytes(b'private retained input')
    output_dir = root / 'toy-repo/data/generated/resnet_generalization/results/generalization/processed'
    output_dir.mkdir(parents=True)
    output = output_dir / 'summary.json'
    partial = output.with_name(output.name + '.partial')
    if kind == 'symlink':
        partial.symlink_to(history)
    else:
        os.link(history, partial)
    before = digest(history)
    env = functions('studies/resnet_generalization/analyze_generalization.py', ['_atomic_bytes'], dict(Path=Path, os=os))
    with mock.patch.object(paths, 'REPO_ROOT', root/'toy-repo'), mock.patch.object(paths, 'GENERATED_ROOT', root/'toy-repo/data/generated/resnet_generalization'):
        paths.require_output(output_dir)
        paths.require_output(output)
        try:
            paths.require_output(history)
        except ValueError:
            pass
        else:
            raise AssertionError('direct history unexpectedly accepted')
        env['_atomic_bytes'](output, b'{"tiny_diagnostic":true}\n')
    assert history.read_bytes() == b'{"tiny_diagnostic":true}\n'
    return dict(link=kind, retained_input=str(history), accepted_output=str(output),
                before_sha256=before, after_sha256=digest(history),
                compiled_function='_atomic_bytes only; caller require_output checks invoked separately',
                scientific_analysis_executed=False)

def shared_hardlink_fixture(parent):
    from studies import _output_paths as shared
    root = parent / 'shared-hardlink/toy-repo'
    source = root / 'studies/stieltjes_direct_loewner/simulate_loewner.py'
    output = root / 'data/generated/stieltjes_direct_loewner/run'
    history = root / 'data/historical/studies/stieltjes_direct_loewner/retained.log'
    output.mkdir(parents=True)
    history.parent.mkdir(parents=True)
    history.write_bytes(b'private retained log')
    os.link(history, output/'run.log')
    with mock.patch.object(shared, 'REPO_ROOT', root):
        paths = shared.StudyPaths(source)
        assert paths.require_output(output) == output
    # Execute the real entry prefix only through the first log open. No model work.
    tree = ast.parse(read('studies/stieltjes_direct_loewner/simulate_loewner.py'))
    main = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
    prefix = main.body[:5]
    assert isinstance(prefix[-1], ast.Assign) and prefix[-1].targets[0].id == 'log_handle'
    env = dict(parse_args=lambda: SimpleNamespace(output=output), PATHS=paths)
    before = digest(history)
    with mock.patch.object(shared, 'REPO_ROOT', root):
        exec(compile(ast.Module(body=prefix, type_ignores=[]), str(source), 'exec'), env)
        env['log_handle'].close()
    assert history.read_bytes() == b''
    return dict(retained_input=str(history), before_sha256=before, after_sha256=digest(history),
                compiled_prefix='simulate_loewner.main lines 382-386 only',
                actual_shared_directory_guard_used=True, campaign_executed=False)

def generalization_raw_writer_fixture(parent):
    from studies.resnet_generalization import generalization_paths as paths
    repo = parent / 'generalization-raw/toy-repo'
    generated = repo / 'data/generated/resnet_generalization'
    retained = repo / 'data/historical/studies/resnet_generalization/retained.bin'
    retained.parent.mkdir(parents=True)
    retained.write_bytes(b'private retained input')
    # Compile the entire current parser and writer function; omit _one_seed,
    # the only numerical trajectory producer, and supply fixed tiny arrays.
    env = functions('studies/resnet_generalization/run_exact_reference.py', ['parse_args', 'run'],
        dict(argparse=argparse, Path=Path, np=np, hashlib=hashlib, json=json, os=os,
             GENERATED_ROOT=generated, require_output=paths.require_output,
             time=SimpleNamespace(perf_counter=lambda: 0.),
             _one_seed=lambda payload: dict(seed=payload['seed'], times=np.array([0.]),
                 f=np.zeros((1, 3)), grams=np.zeros((1, 2, 3, 3)), theta=np.zeros((1, 3, 3)))))
    with mock.patch.object(paths, 'REPO_ROOT', repo), mock.patch.object(paths, 'GENERATED_ROOT', generated), mock.patch.object(sys, 'argv', ['raw', '--n', '1', '--depth', '1', '--seeds', '2', '--workers', '1', '--duration', '0']), contextlib.redirect_stdout(io.StringIO()):
        args = env['parse_args']()
        assert args.output_dir is None and args.pde_seal is None
        first = env['run'](args)
        first.unlink()  # Tiny diagnostic product only; no retained input removed.
        partial = first.with_suffix(first.suffix + '.partial')
        partial.symlink_to(retained)
        before = digest(retained)
        final = env['run'](args)
    assert retained.read_bytes() == final.read_bytes() and digest(retained) != before
    return dict(default_output=str(final), retained_input=str(retained),
                before_sha256=before, after_sha256=digest(retained),
                run_function_executed_in_full=True, trajectory_function='fixed arrays substituted for _one_seed',
                source_seal_or_pde_authorization_generated=False)

def timeout_escape_fixture(parent, kind):
    rel = 'studies/stieltjes_hybrid_campaign/width_ladder/euler_fp32/run_stage_v_point.py'
    root = parent / ('timeout-' + kind) / 'toy-repo'
    run_root = root / 'data/generated/stieltjes_hybrid_campaign/width_ladder/euler_fp32/runs/stage_v'
    run_root.mkdir(parents=True)
    retained = root / 'data/historical/studies/stieltjes_hybrid_campaign/retained-point'
    retained.mkdir(parents=True)
    manifest = retained / 'manifest.json'
    manifest.write_text(json.dumps({'status': 'running', 'fixture': 'private retained input'}) + '\n')
    before = digest(manifest)
    point = str(retained) if kind == 'absolute' else os.path.relpath(retained, run_root)
    # Neither lock validation nor device/engine functions are present. The real
    # main reaches the failure writer without needing any of them.
    env = functions(rel, ['load_json', 'utc_now', 'atomic_json', 'finalize_timeout', 'main'],
        dict(Path=Path, json=json, os=os, argparse=argparse, resource=resource,
             datetime=datetime, timezone=timezone, RUN_ROOT=run_root))
    with mock.patch.object(sys, 'argv', ['stage-v', '--point', point, '--finalize-timeout']):
        rc = env['main']()
    result = json.loads(manifest.read_text())
    assert rc == 0 and result['status'] == 'failed_inconclusive_external_timeout'
    assert not list(run_root.iterdir())
    return dict(point_argument=point, retained_manifest=str(manifest), rc=rc,
                before_sha256=before, after_sha256=digest(manifest), new_status=result['status'],
                source_or_unlock_checks_called=False, torch_imported=False)

def negative_gate_checks():
    from studies.resnet_generalization import verify_study
    try:
        verify_study.verify_source(False)
    except RuntimeError as exc:
        source_refusal = str(exc)
    else:
        raise AssertionError('expected current freeze mismatch')
    results = {'generalization_source': source_refusal}
    for rel, names, env, name in [
        ('studies/resnet_generalization/protocol/seal_dense_postfreeze_amendment.py', ['sha256', 'main'],
         dict(ROOT=BASE/'studies/resnet_generalization', RUNNER=BASE/'studies/resnet_generalization/protocol/run_grid.py',
              MANIFEST=BASE/'studies/resnet_generalization/protocol/FROZEN_DYNAMICS_MANIFEST.json', Path=Path, hashlib=hashlib, json=json), 'dense_wrapper'),
        ('studies/resnet_generalization/protocol/analyze_postfreeze_amendment.py', ['sha256', 'main'],
         dict(ANALYZER=BASE/'studies/resnet_generalization/analyze_generalization.py',
              MANIFEST=BASE/'studies/resnet_generalization/protocol/FROZEN_DYNAMICS_MANIFEST.json', Path=Path, hashlib=hashlib, json=json), 'analysis_wrapper')]:
        scope = functions(rel, names, env)
        try:
            scope['main']()
        except RuntimeError as exc:
            results[name] = str(exc)
        else:
            raise AssertionError('wrapper did not refuse')
    return results

def real_archive_entry_refusals():
    relatives = ['studies/stieltjes_hybrid_campaign/breadth_panel/fp64_successor/' + name
                 for name in ('watchdog_launcher.py', 'gpu_preflight.py', 'run_local_qualification.py', 'adjudicate_local_qualification.py')]
    relatives += [f'studies/stieltjes_hybrid_campaign/breadth_panel/successive_n{width}/run_block.py' for width in (4096, 8192)]
    results = {}
    for rel in relatives:
        read(rel)
        with mock.patch.object(sys, 'argv', [str(BASE/rel)]), mock.patch.object(sys, 'path', list(sys.path)):
            try:
                runpy.run_path(str(BASE/rel), run_name='__main__')
            except RuntimeError as exc:
                assert 'archive-only FP64 runtime' in str(exc)
                results[rel] = str(exc)
            else:
                raise AssertionError('archive entry did not refuse')
    assert 'torch' not in sys.modules
    return results

def main():
    os.chdir(OUT)
    tempfile.tempdir = str(OUT)
    sys.addaudithook(guard)
    with tempfile.TemporaryDirectory(prefix='adversarial-') as temp:
        root = Path(temp)
        result = {
            'finite_width_retained_input_overwrite': [jet_alias_fixture(root, kind) for kind in ('symlink', 'hardlink')],
            'generalization_partial_redirection': [generalization_partial_fixture(root, kind) for kind in ('symlink', 'hardlink')],
            'generalization_raw_default_writer_redirection': generalization_raw_writer_fixture(root),
            'shared_helper_hardlink_redirection': shared_hardlink_fixture(root),
            'stage_v_timeout_path_escape': [timeout_escape_fixture(root, kind) for kind in ('absolute', 'relative')],
            'current_hash_gate_refusals': negative_gate_checks(),
            'real_archive_entry_refusals': real_archive_entry_refusals(),
            'runtime': {'python': sys.version, 'numpy': np.__version__},
        }
        (OUT/'adversarial-results.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
        print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
