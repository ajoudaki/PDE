"""Private path/metadata fixtures only; no compilation, fits or simulations."""
from contextlib import ExitStack, contextmanager
import hashlib
import importlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock


CASES = (
    ('depth_order5.independent.compare_symbolic_q0', 'SYMBOLIC_Q0_COMPARISON.json'),
    ('depth_order5.audit.compare_frozen', 'FROZEN_MAP_COMPARISON.json'),
    ('depth_order5.audit.audit_symbolic_q0', 'SYMBOLIC_Q0_AUDIT.json'),
    ('depth_order5.audit.run_normalized_sine_experiment', 'NORMALIZED_SINE_EXPERIMENT.json'),
    ('depth_order5_observables.independent.run_sine_experiment', 'NORMALIZED_SINE_EXPERIMENT.json'),
)
WORK = ('compile_depth_factored', 'expand_expression', '_verify_manifest',
        '_primary_map', '_independent_map', 'primary_graded', 'collect_cell',
        'one_jet', 'fit_depth', 'collect', 'one_observation', 'fit')


def hashes(paths):
    return {str(path): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}


@contextmanager
def layout(index, *, same_directory=False):
    suffix, output_name = CASES[index]
    module = importlib.import_module('studies.mfp_gaussian_calculus.' + suffix)
    with tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
        root = Path(temporary)
        inputs = root / 'inputs'
        output = inputs if same_directory else root / 'output'
        primary, independent = root / 'source/primary', root / 'source/independent'
        for path in (inputs, output, primary, independent):
            path.mkdir(parents=True, exist_ok=True)
        selected = []
        if index == 0:
            stack.enter_context(mock.patch.multiple(module, HERE=independent, PRIMARY=primary))
            selected = [inputs / f'H{depth}_LAYER_TAGGED_COEFFICIENTS.json' for depth in (3, 4)]
            selected += [independent / 'FROZEN_MANIFEST.json', primary / 'PRIMARY_FREEZE_MANIFEST.json']
        elif index == 1:
            stack.enter_context(mock.patch.multiple(
                module, PRIMARY=primary, INDEPENDENT=independent,
                PRIMARY_MANIFEST=primary / 'PRIMARY_FREEZE_MANIFEST.json',
                INDEPENDENT_MANIFEST=independent / 'FROZEN_MANIFEST.json'))
            selected = [inputs / 'primary' / f'H{depth}_{scope}_COEFFICIENTS.json'
                        for depth in (3, 4) for scope in ('UNIT', 'LAYER_TAGGED')]
            selected += [inputs / 'independent' / f'H{depth}_{scope}_COEFFICIENT_MAP.json'
                         for depth in (3, 4) for scope in ('UNIT', 'TAGGED')]
            selected += [module.PRIMARY_MANIFEST, module.INDEPENDENT_MANIFEST,
                         primary / 'PRIMARY_FREEZE_SHA256.txt', independent / 'FROZEN_MANIFEST_SHA256.txt']
        elif index == 2:
            selected = [inputs / 'primary' / f'H{depth}_LAYER_TAGGED_COEFFICIENTS.json' for depth in (3, 4)]
            selected += [inputs / 'independent' / f'H{depth}_TAGGED_COEFFICIENT_MAP.json' for depth in (3, 4)]
        else:
            stack.enter_context(mock.patch.object(module, 'HERE', primary))
            selected = ([inputs / 'audit/TWO_ORACLE_GATE.json', inputs / 'common/NORMALIZED_SINE_FROZEN_PREDICTION.json']
                        if index == 3 else [inputs / 'POST_FREEZE_EXACT_AUDIT.json', inputs / 'NORMALIZED_SINE_PREDICTION.json'])
        outputs = [output / output_name]
        if index == 3:
            outputs += [output / f'normalized_sine_H{depth}_n{width}.npy'
                        for depth in module.DEPTHS for width in module.ALLOCATIONS]
        if index == 4:
            outputs += [output / 'sine_raw' / f'gamma04_H2_n{width}.npy' for width in module.ALLOCATIONS]
        for path in selected:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('{"artifacts": {}}\n')
        argv = [module.__file__, '--input-dir', str(inputs), '--output-dir', str(output)]
        yield module, root, selected, outputs, argv


@contextmanager
def work_tripwires(module, message='work reached'):
    with ExitStack() as stack:
        for name in WORK:
            if hasattr(module, name):
                stack.enter_context(mock.patch.object(module, name, side_effect=RuntimeError(message)))
        yield


class SiblingConsumerTests(unittest.TestCase):
    def test_every_selected_input_against_every_named_output_before_reads(self):
        for index in range(len(CASES)):
            with layout(index) as (_module, _root, selected, outputs, _argv):
                dimensions = len(selected), len(outputs)
            for input_index in range(dimensions[0]):
                for output_index in range(dimensions[1]):
                    for kind in ('input-symlink', 'output-symlink', 'hardlink'):
                        with self.subTest(module=index, input=input_index, output=output_index, alias=kind), layout(index) as (module, _root, selected, outputs, argv):
                            source, destination = selected[input_index], outputs[output_index]
                            destination.parent.mkdir(parents=True, exist_ok=True)
                            if kind == 'input-symlink':
                                destination.write_bytes(source.read_bytes())
                                source.unlink()
                                source.symlink_to(destination)
                            elif kind == 'output-symlink':
                                destination.symlink_to(source)
                            else:
                                destination.hardlink_to(source)
                            before = hashes(selected)
                            with mock.patch.object(sys, 'argv', argv), work_tripwires(module), \
                                 mock.patch.object(Path, 'read_text', side_effect=AssertionError('read reached')), \
                                 mock.patch.object(Path, 'read_bytes', side_effect=AssertionError('hash reached')):
                                with self.assertRaises(ValueError):
                                    module.main()
                            self.assertEqual(before, hashes(selected))

    def test_existing_distinct_outputs_in_same_directory_still_dispatch(self):
        for index in range(len(CASES)):
            with self.subTest(module=index), layout(index, same_directory=True) as (module, _root, selected, outputs, argv):
                for path in outputs:
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(b'ordinary private output/checkpoint')
                before = hashes(selected + outputs)
                with mock.patch.object(sys, 'argv', argv), work_tripwires(module), \
                     mock.patch.object(Path, 'read_text', side_effect=RuntimeError('work reached')), \
                     mock.patch.object(Path, 'read_bytes', side_effect=RuntimeError('work reached')):
                    with self.assertRaisesRegex(RuntimeError, 'work reached'):
                        module.main()
                self.assertEqual(before, hashes(selected + outputs))

    def test_unselected_input_alias_is_not_treated_as_consumed(self):
        for index in range(len(CASES)):
            with self.subTest(module=index), layout(index) as (module, root, _selected, outputs, argv):
                outputs[0].write_bytes(b'ordinary private output')
                (root / 'inputs/not-selected.json').symlink_to(outputs[0])
                with mock.patch.object(sys, 'argv', argv), work_tripwires(module), \
                     mock.patch.object(Path, 'read_text', side_effect=RuntimeError('work reached')), \
                     mock.patch.object(Path, 'read_bytes', side_effect=RuntimeError('work reached')):
                    with self.assertRaisesRegex(RuntimeError, 'work reached'):
                        module.main()

    def test_manifest_declared_artifact_aliases_precede_verification(self):
        for role in ('primary', 'independent'):
            for selected_copy in (False, True):
                for explicit_file in (False, True):
                    with self.subTest(role=role, selected_copy=selected_copy, explicit_file=explicit_file), layout(1) as (module, root, selected, outputs, argv):
                        source_dir = getattr(module, role.upper())
                        manifest_path = getattr(module, role.upper() + '_MANIFEST')
                        directory = root / 'inputs' / role if selected_copy else source_dir
                        directory.mkdir(parents=True, exist_ok=True)
                        alias = directory / 'private-formula.txt'
                        outputs[0].write_bytes(b'private declared artifact')
                        alias.symlink_to(outputs[0])
                        artifact = {'sha256': 'unused-private-digest'}
                        if role == 'primary':
                            if explicit_file:
                                artifact['file'] = alias.name
                            artifacts = {alias.name: artifact}
                        else:
                            artifact['file'] = alias.name
                            artifacts = {'fixture': artifact if explicit_file else {'text': artifact}}
                        manifest_path.write_text(json.dumps({'artifacts': artifacts}))
                        before = hashes([*selected, alias])
                        with mock.patch.object(sys, 'argv', argv), work_tripwires(module), \
                             mock.patch.object(Path, 'read_bytes', side_effect=AssertionError('artifact hashing reached')):
                            with self.assertRaises(ValueError):
                                module.main()
                        self.assertEqual(before, hashes([*selected, alias]))

    def test_historical_fallback_gate_is_selected_before_preflight(self):
        for index, leaf in ((3, 'TWO_ORACLE_GATE.json'), (4, 'POST_FREEZE_EXACT_AUDIT.json')):
            with self.subTest(module=index), layout(index) as (module, root, _selected, outputs, argv):
                outputs[-1].parent.mkdir(parents=True, exist_ok=True)
                outputs[-1].write_bytes(b'private fallback gate')
                fallback = module.HERE / leaf
                fallback.symlink_to(outputs[-1])
                before = hashes([fallback])
                with mock.patch.object(module.PATHS, 'input_dir', return_value=root / 'missing-historical'), \
                     mock.patch.object(sys, 'argv', [argv[0], '--historical-inputs', '--output-dir', argv[-1]]), \
                     mock.patch.object(Path, 'read_text', side_effect=AssertionError('gate read reached')), work_tripwires(module):
                    with self.assertRaises(ValueError):
                        module.main()
                self.assertEqual(before, hashes([fallback]))

    def test_original_manifest_and_prediction_digest_failures_remain(self):
        with layout(1) as (module, _root, _selected, _outputs, _argv):
            with mock.patch.object(Path, 'read_bytes', return_value=b'private metadata'), \
                 mock.patch.object(Path, 'read_text', return_value='wrong-private-digest'):
                with self.assertRaises(AssertionError):
                    module._verify_manifest(module.PRIMARY, module.PRIMARY_MANIFEST,
                                            module.PRIMARY / 'unused.txt', data_directory=module.PRIMARY)
        with layout(4) as (module, _root, selected, outputs, argv):
            selected[0].write_text('{"decision":"pass"}')
            before = hashes(selected)
            with mock.patch.object(sys, 'argv', argv), work_tripwires(module):
                with self.assertRaisesRegex(RuntimeError, 'prediction changed:'):
                    module.main()
            self.assertEqual(before, hashes(selected))
            self.assertTrue(all(not output.exists() for output in outputs))

    def test_ordinary_checkpoint_resume_keeps_existing_read_dispatch(self):
        for index in (3, 4):
            with self.subTest(module=index), layout(index) as (module, _root, _selected, outputs, _argv):
                checkpoint = outputs[1]
                checkpoint.parent.mkdir(parents=True, exist_ok=True)
                checkpoint.write_bytes(b'private checkpoint; decoding prohibited')
                before = hashes([checkpoint])
                with mock.patch.object(module.np, 'load', side_effect=RuntimeError('checkpoint read reached')):
                    with self.assertRaisesRegex(RuntimeError, 'checkpoint read reached'):
                        if index == 3:
                            module.collect_cell(3, 32, 1800, 0, output_dir=checkpoint.parent)
                        else:
                            module.collect(16, 1200, 0, output_dir=checkpoint.parent)
                self.assertEqual(before, hashes([checkpoint]))


if __name__ == '__main__':
    unittest.main()
