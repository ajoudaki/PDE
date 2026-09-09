"""Independent inert boundary probes; no scientific imports, arrays or seals."""
import ast
import hashlib
import json
import os
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest import mock

from studies.resnet_generalization.generalization_paths import require_output as generalization_output
from studies.resnet_activation_controls.output_paths import require_output as activation_output

ROOT = Path('/home/amir/Codes/PDE')
PRIVATE = Path(__file__).resolve().parent
RECORDS = []

class StopBeforeInputs(Exception):
    pass

def functions(relative, names, guard):
    path = ROOT / relative
    nodes = [node for node in ast.parse(path.read_text()).body if isinstance(node, ast.FunctionDef) and node.name in names]
    assert {node.name for node in nodes} == set(names)
    future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
    env = {'Path': Path, 'os': os, 'json': json, 'require_output': guard, 'IntegrityError': RuntimeError}
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])), str(path), 'exec'), env)
    return env

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

class IndependentAcceptanceBoundaries(unittest.TestCase):
    def test_generalization_selected_report_can_target_its_seal_input(self):
        env = functions('studies/resnet_generalization/analyze_generalization.py',
                        {'run_analysis', '_atomic_bytes', '_atomic_text'}, generalization_output)
        for role in ('PDE_STAGE_SEAL.json', 'DENSE_STAGE_SEAL.json', 'pde_numerical_decision.json'):
            for linked in (False, True):
                with self.subTest(role=role, linked=linked):
                    base = PRIVATE / 'independent' / f'generalization-{role}-{linked}'
                    results = base / 'results/generalization'
                    results.mkdir(parents=True)
                    source = results / role
                    source.write_bytes(b'INERT INPUT BYTES: not a seal or authorization\n')
                    before = digest(source)
                    selected = source
                    if linked:
                        selected = base / 'report.md'
                        selected.symlink_to(source)
                    args = SimpleNamespace(root=base / 'source', results_dir=results,
                        output_dir=results / 'processed', figures_dir=results / 'figures', report=selected)
                    loader = mock.Mock(side_effect=StopBeforeInputs)
                    env['_json'] = loader
                    # The whole real entry callable is invoked, stopping at its
                    # first input read. No source/hash/frozen gate is bypassed.
                    with self.assertRaises(StopBeforeInputs) as stopped:
                        env['run_analysis'](args)
                    loader.assert_called_once_with(base / 'source/protocol/generalization_protocol.json')
                    self.assertEqual(digest(source), before)
                    # Separately exercise the real publication callable at the
                    # resolved path accepted by the entry boundary. This does
                    # not claim execution of the intervening frozen analysis.
                    env['_atomic_text'](selected.resolve(), 'INERT OUTPUT BYTES: private writer probe\n')
                    after = digest(source)
                    self.assertNotEqual(before, after)
                    RECORDS.append({'case': f'generalization/report/{role}/linked={linked}',
                        'entry_reached_first_input_loader': True,
                        'publication_probe': 'separate real writer, no intervening analysis',
                        'fixture': str(source), 'before': before, 'after': after})

    def test_activation_selected_protocol_can_be_summary_destination(self):
        env = functions('studies/resnet_activation_controls/analyze_activation.py',
                        {'run_analysis', '_atomic_text'}, activation_output)
        base = PRIVATE / 'independent/activation-protocol'
        output = base / 'processed'
        output.mkdir(parents=True)
        source = output / 'summary.json'
        source.write_bytes(b'INERT INPUT BYTES: not a protocol or authorization\n')
        before = digest(source)
        args = SimpleNamespace(root=base / 'source', protocol=source, cases=base / 'cases.json',
                               pde_dir=base / 'results/pde', dense_dir=base / 'results/dense', output_dir=output)
        loader = mock.Mock(side_effect=StopBeforeInputs)
        env['_json'] = loader
        with self.assertRaises(StopBeforeInputs):
            env['run_analysis'](args)
        loader.assert_called_once_with(source)
        self.assertEqual(digest(source), before)
        env['_atomic_text'](source, 'INERT OUTPUT BYTES: private writer probe\n')
        after = digest(source)
        self.assertNotEqual(before, after)
        RECORDS.append({'case': 'activation/protocol-equals-summary',
            'entry_reached_first_input_loader': True,
            'publication_probe': 'separate real writer, no intervening analysis',
            'fixture': str(source), 'before': before, 'after': after})

    def test_activation_matching_record_does_not_refuse_existing_partial(self):
        env = functions('studies/resnet_activation_controls/run_experiment.py',
                        {'_write_once', '_encoded'}, activation_output)
        base = PRIVATE / 'independent/activation-stale-partial'
        base.mkdir(parents=True)
        output = base / 'inert-record.json'
        payload = {'private': 'inert record, not a seal or authorization'}
        env['_write_once'](output, payload)
        partial = output.with_suffix('.json.partial')
        partial.write_bytes(b'INERT STALE PARTIAL\n')
        before = {str(p): digest(p) for p in (output, partial)}
        env['_write_once'](output, payload)
        after = {str(p): digest(p) for p in (output, partial)}
        self.assertEqual(before, after)
        RECORDS.append({'case': 'activation/write-once/matching-final-plus-stale-partial',
                        'returned_without_refusal': True, 'before': before, 'after': after})

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(IndependentAcceptanceBoundaries)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    (PRIVATE / 'independent-probes.json').write_text(json.dumps(RECORDS, indent=2) + '\n')
    print(json.dumps(RECORDS, indent=2))
    raise SystemExit(not result.wasSuccessful())
