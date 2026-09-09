"""Bounded routing probes: no scientific jobs, data writes, or real seals."""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys
from types import SimpleNamespace
from unittest import mock

import numpy as np

REPO = Path('/home/amir/Codes/PDE')
sys.path.insert(0, str(REPO))


def functions(relative, names, **env):
    path = REPO / relative
    tree = ast.parse(path.read_text())
    nodes = [n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name in names]
    assert {n.name for n in nodes} == set(names)
    future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
    env.update(Path=Path, json=json, argparse=argparse, sys=sys, np=np, hashlib=hashlib)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])), str(path), 'exec'), env)
    return env


class StopBeforeWrite(BaseException):
    pass


def catch_write(call):
    reached = []
    def stop(path, *args, **kwargs):
        reached.append(str(path))
        raise StopBeforeWrite
    with mock.patch.object(Path, 'mkdir', stop):
        try:
            call()
        except StopBeforeWrite:
            pass
    assert len(reached) == 1, reached
    return reached[0]


from studies._output_paths import StudyPaths
from studies.resnet_generalization.generalization_paths import require_output
from studies.stieltjes_finite_width.run_paths import parse_paths, GENERATED_ROOT
from studies.stieltjes_hybrid_campaign.breadth_panel.successive_paths import parse_analysis_paths

foreign = REPO / 'data/generated/resnet_activation_controls/routing-probe'
assert require_output(foreign) == foreign
assert parse_paths(GENERATED_ROOT/'probe', ['--output-dir', str(foreign)]).output_dir == foreign
assert parse_analysis_paths('successive_n4096', ['--output-dir', str(foreign)]).output_dir == foreign
shared = StudyPaths(REPO/'studies/resnet_generalization/run_pde.py')
try:
    shared.require_output(foreign)
except ValueError:
    print('PASS shared helper rejects another study; FAIL generalization/finite-width/successive helpers accept it')
else:
    raise AssertionError('shared helper unexpectedly accepts foreign output')

writer = functions('studies/stieltjes_proxy_campaign/analysis/pilot_runner.py', ['write_json_atomic'])
def unavailable(*args):
    raise FileNotFoundError('synthetic missing input; no file was opened')
pilot = functions('studies/stieltjes_proxy_campaign/analysis/run_frozen_pilot.py', ['parse_args', 'main'],
                  analyze_pilot=unavailable, write_json_atomic=writer['write_json_atomic'], PilotAnalysisInvalid=ValueError)
for directory in ('studies/stieltjes_proxy_campaign/analysis', 'data/historical/studies/stieltjes_proxy_campaign'):
    target = REPO/directory/'adversarial-probe-not-created.json'
    with mock.patch.object(sys, 'argv', ['pilot', '--summary', 'missing', '--config', 'missing',
                                      '--analysis-config', 'missing', '--output', str(target)]):
        print('FAIL proxy failure handler reaches protected mkdir:', catch_write(pilot['main']))

metadata = dict.fromkeys(('case_id case_sha256 registry_sha256 n depth duration dt sample_dt sigma_w A gamma '
                          'activation X y m d pde_seal_sha256 dynamics_sha256').split(), 1)
fixture = dict(times=np.array([0., 1.]), seeds=np.array([1, 2]), f=np.zeros((2, 2, 1)),
               grams=np.zeros((2, 2, 1, 1)), theta=np.zeros((2, 2, 1, 1)), metadata_json=json.dumps(metadata))
combine = functions('studies/resnet_generalization/combine_references.py', ['main'],
                    load_raw=lambda p: fixture, file_sha256=lambda p: 'fixture')
for directory in ('studies/resnet_generalization', 'data/historical/studies/resnet_generalization'):
    target = REPO/directory/'adversarial-probe-not-created.npz'
    with mock.patch.object(sys, 'argv', ['combine', 'memory-only', '--output', str(target)]):
        print('FAIL reference combiner reaches protected mkdir:', catch_write(combine['main']))

genroot = REPO/'studies/resnet_generalization'
verify = functions('studies/resnet_generalization/verify_study.py', ['sha256', 'verify_source'], ROOT=genroot)
try:
    verify['verify_source'](False)
except RuntimeError as exc:
    print('EXPECTED generalization source gate:', exc)
else:
    raise AssertionError('expected migrated source hash mismatch')

proofroot = REPO/'studies/resnet_proof_audit'
freeze = functions('studies/resnet_proof_audit/protocol/freeze_study.py', ['main'],
                   HISTORICAL_SEAL=REPO/'data/historical/studies/resnet_proof_audit/results/seals/FROZEN_INPUTS.json')
try:
    freeze['main']()
except RuntimeError as exc:
    print('EXPECTED proof freeze refusal:', exc)
else:
    raise AssertionError('freeze was not refused at first guard')

activation = functions('studies/resnet_activation_controls/run_experiment.py', ['_create_input_manifest'],
    HISTORICAL_INPUT_MANIFEST_PATH=REPO/'data/historical/studies/resnet_activation_controls/evidence/seals/FROZEN_INPUTS.json',
    INPUT_MANIFEST_PATH=Path('/tmp/pde-study-routing-final.IVwibJSr/nonexistent-live-freeze.json'), IntegrityError=RuntimeError)
try:
    activation['_create_input_manifest']()
except RuntimeError as exc:
    print('EXPECTED activation freeze refusal:', exc)
else:
    raise AssertionError('freeze was not refused at first guard')

refroot = REPO/'studies/stieltjes_proxy_campaign/reference'
gate = functions('studies/stieltjes_proxy_campaign/reference/run_reference.py',
                 ['sha256', 'source_hashes', 'source_bundle_sha256', '_production_gate', '_analysis_lock_fields'],
                 HERE=refroot, SOURCE_FILES=tuple(refroot/n for n in ('canonical_model.py', 'reference_engine.py',
                 'run_reference.py', 'run_capped_reference.sh')))
configpath = refroot/'configs/FROZEN_SUCCESSOR_02.json'
try:
    gate['_production_gate'](json.loads(configpath.read_text()), configpath, gate['source_hashes']())
except PermissionError as exc:
    assert 'source_bundle_sha256' in str(exc)
    print('EXPECTED proxy production refusal:', exc)
else:
    raise AssertionError('production unexpectedly authorized')

figure = functions('studies/resnet_activation_controls/make_figures.py', ['main'],
                   PATHS=StudyPaths(REPO/'studies/resnet_activation_controls/make_figures.py'))
for options, suffix in (([], 'data/generated/resnet_activation_controls/results/processed/summary.json'),
                         (['--historical-inputs'], 'data/historical/studies/resnet_activation_controls/evidence/processed/summary.json')):
    selected = []
    def stop_read(path, *a, **k):
        selected.append(path)
        raise StopBeforeWrite
    with mock.patch.object(sys, 'argv', ['figures', *options]), mock.patch.object(Path, 'mkdir'), \
         mock.patch.object(Path, 'read_text', stop_read):
        try:
            figure['main']()
        except StopBeforeWrite:
            pass
    assert selected == [REPO/suffix], selected
    print('PASS activation figure input selection:', selected[0])

from studies.resnet_generalization.generalization_paths import evidence_path, evidence_label
results = Path('/tmp/pde-study-routing-final.IVwibJSr/memory-only/results/generalization')
archive = results/'pde_primary/never-created.npz'
record = dict(dynamics_sha256='synthetic', run_grid_sha256='runner', files={evidence_label(archive, results): 'archive'}, file_count=1)
sealpath = results/'PDE_STAGE_SEAL.json'
gridpath = genroot/'protocol/run_grid.py'
digests = {gridpath: 'runner', archive: 'archive'}
grid = functions('studies/resnet_generalization/protocol/run_grid.py', ['_require_pde_seal'],
                 RESULTS=results, __file__=str(gridpath), evidence_path=evidence_path,
                 verify_frozen=lambda: 'synthetic', _sha256=lambda p: digests[p])
sealed = functions('studies/resnet_generalization/verify_study.py', ['verify_seal'],
                   RESULTS=results, evidence_path=evidence_path, sha256=lambda p: digests[p])
with mock.patch.object(Path, 'exists', lambda p: p in {sealpath, archive}), \
     mock.patch.object(Path, 'read_text', lambda p: json.dumps(record)):
    grid['_require_pde_seal']()
    assert sealed['verify_seal'](sealpath, results) == record
    digests[archive] = 'changed'
    for fn in (grid['_require_pde_seal'], lambda: sealed['verify_seal'](sealpath, results)):
        try:
            fn()
        except RuntimeError:
            pass
        else:
            raise AssertionError('changed synthetic evidence was accepted')
print('PASS grid and verifier agree on in-memory evidence labels and reject tampering; no seal file generated')
print('All probes completed without reaching a file write or scientific engine.')
