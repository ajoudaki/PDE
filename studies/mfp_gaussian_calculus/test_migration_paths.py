"""Small path-interface regressions; campaign/compilation work is mocked out."""
from __future__ import annotations

import ast
from contextlib import ExitStack
import hashlib
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest import mock

import numpy as np

from studies.mfp_gaussian_calculus import study_paths as paths
from studies.mfp_gaussian_calculus.order5.compiler import compare_independent as comparison
from studies.mfp_gaussian_calculus.depth_order5.primary import freeze_primary
from studies.mfp_gaussian_calculus.depth_order5_scalar.multi_observable.audit import (
    run_h3_sine_regression as sine,
    run_h3_curvature_extension as curvature,
    postprocess_h3_sine_regression as postprocess,
    postprocess_h3_curvature_extension as archival_postprocess,
)

HERE = Path(__file__).resolve().parent


class GaussianPathTests(unittest.TestCase):
    def test_h3_fresh_producers_and_consumers_agree(self):
        self.assertEqual(sine.OUTPUT, curvature.OUTPUT)
        self.assertEqual(sine.OUTPUT, postprocess.OUTPUT)
        self.assertEqual(curvature.OLD_RAW, postprocess.RAW)
        self.assertEqual(postprocess.RAW.parent, sine.OUTPUT)
        self.assertTrue(sine.OUTPUT.is_relative_to(paths.GENERATED_ROOT))

    def test_historical_selection_is_explicit(self):
        self.assertEqual(paths.input_directory(postprocess.PANEL), sine.OUTPUT)
        history = paths.input_directory(postprocess.PANEL, historical=True)
        self.assertTrue(history.is_relative_to(paths.HISTORICAL_ROOT))
        fresh_input, fresh_output = comparison.comparison_paths([])
        old_input, review_output = comparison.comparison_paths(['--historical'])
        self.assertTrue(fresh_input.is_relative_to(paths.GENERATED_ROOT))
        self.assertTrue(old_input.is_relative_to(paths.HISTORICAL_ROOT))
        self.assertEqual(review_output, fresh_output/'historical_review')

    def test_reject_unsafe_outputs_before_any_compiler_or_input_work(self):
        for output in (HERE/'forbidden', paths.HISTORICAL_ROOT/'forbidden'):
            with self.assertRaises(ValueError): sine.run(output)
            with self.assertRaises(ValueError): curvature.run(Path('/missing-input'), output)
            with self.assertRaises(ValueError): postprocess.run(Path('/missing-input'), output)
            with self.assertRaises(ValueError): comparison.comparison_paths(['--output-dir', str(output)])

    def test_existing_child_aliases_refuse_before_work_and_preserve_input(self):
        for kind in ('symlink', 'hardlink'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                retained = root / 'retained-result.json'
                retained.write_bytes(b'immutable fixture')
                output = root / 'fresh'
                output.mkdir()
                alias = output / 'H3_NORMALIZED_SINE_RESULT.json'
                if kind == 'symlink':
                    alias.symlink_to(retained)
                else:
                    alias.hardlink_to(retained)
                with ExitStack() as stack:
                    for operation in ('read_text', 'read_bytes', 'write_text', 'write_bytes', 'mkdir'):
                        stack.enter_context(mock.patch.object(
                            Path, operation, side_effect=AssertionError('input/output work reached')
                        ))
                    for target, name in ((sine, 'compile_numeric'), (curvature, 'compile_numeric'),
                                         (postprocess, 'compile_numeric'), (comparison, 'compile_factored')):
                        stack.enter_context(mock.patch.object(
                            target, name, side_effect=AssertionError('scientific work reached')
                        ))
                    with self.assertRaises(ValueError): paths.require_output(output)
                    with self.assertRaises(ValueError): sine.run(output)
                    with self.assertRaises(ValueError): curvature.run(root / 'missing-raw', output)
                    with self.assertRaises(ValueError): postprocess.run(root / 'missing-raw', output)
                    with self.assertRaises(ValueError):
                        comparison.comparison_paths(['--output-dir', str(output)])
                self.assertEqual(retained.read_bytes(), b'immutable fixture')
                self.assertEqual(list(output.iterdir()), [alias])

    def test_generated_defaults_and_unaliased_scratch_remain_accepted(self):
        self.assertEqual(paths.require_output(sine.OUTPUT), sine.OUTPUT)
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            (output / 'ordinary.json').write_text('{}')
            self.assertEqual(paths.require_output(output), output)
            self.assertEqual(paths.require_output(output / 'new'), output / 'new')

    def test_selected_sine_fixture_to_separate_fresh_result(self):
        # This tests I/O and the existing small fit, not simulated trajectories.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            raw = root/'selected-raw.npz'
            names = ('layer2_gamma04', 'layer2_q4', 'layer3_gamma04', 'layer3_q4')
            values = np.tile(np.array([-1., 0., 1.])[None, :, None], (3, 1, 4))
            np.savez(raw, widths=np.array([16, 32, 64]), names=names, values=values)
            digest = hashlib.sha256(raw.read_bytes()).hexdigest()
            prediction = {'layers': {2: {'Gamma04': 0., 'Q4': 0.}, 3: {'Gamma04': 0., 'Q4': 0.}}}
            with mock.patch.object(postprocess, 'EXPECTED_RAW_SHA256', digest), \
                 mock.patch.object(postprocess, 'compile_numeric', return_value=prediction), \
                 mock.patch.object(postprocess, 'normalized_sine_moment', return_value=None):
                result = postprocess.run(raw, root/'fresh')
            self.assertEqual(result['raw_sha256'], digest)
            self.assertEqual(result['raw_path'], raw.name)
            self.assertEqual(hashlib.sha256(raw.read_bytes()).hexdigest(), digest)
            self.assertTrue((root/'fresh/H3_NORMALIZED_SINE_RESULT.json').is_file())

    def test_comparison_uses_selected_inputs_and_fresh_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            inputs, output = root/'inputs', root/'fresh'
            inputs.mkdir()
            empty_maps = {name: [] for name in ('A', 'B', 'C')}
            payloads = [dict(unit_gram=empty_maps), empty_maps, dict(maps=empty_maps)]
            names = [comparison.INDEPENDENT.name, comparison.INDEPENDENT_TAGGED.name,
                     comparison.INDEPENDENT_SYMBOLIC_Q0.name]
            for name, payload in zip(names, payloads):
                (inputs/name).write_text(json.dumps(payload))
            fake_root = mock.Mock()
            fake_root.specialize_unit_gram.return_value = fake_root
            compiled = SimpleNamespace(A=fake_root, B3=fake_root, C=fake_root)
            with mock.patch.object(comparison, 'comparison_paths', return_value=(inputs, output)), \
                 mock.patch.object(comparison, 'compile_factored', return_value=compiled), \
                 mock.patch.object(comparison, 'expand_coefficient_map', return_value={}):
                comparison.main()
            self.assertEqual(len(list(output.glob('*.json'))), 4)
            result = json.loads((output/'INDEPENDENT_COMPARISON.json').read_text())
            for key, name in zip(('independent_frozen_sha256', 'independent_tagged_frozen_sha256',
                                  'independent_symbolic_q0_frozen_sha256'), names):
                self.assertEqual(result[key], hashlib.sha256((inputs/name).read_bytes()).hexdigest())

    def test_freeze_refuses_existing_seal_without_any_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source, history = root/'source', root/'history'
            source.mkdir()
            history.mkdir()
            seal = history/'PRIMARY_FREEZE_MANIFEST.json'
            seal.write_bytes(b'untouched historical fixture')
            with mock.patch.object(freeze_primary, 'HERE', source), \
                 mock.patch.object(freeze_primary, 'HISTORICAL', history):
                with self.assertRaisesRegex(RuntimeError, 'existing seal is immutable'):
                    freeze_primary.main()
            self.assertEqual(seal.read_bytes(), b'untouched historical fixture')
            self.assertEqual(list(source.iterdir()), [])

    def test_freeze_is_archive_only_even_when_seal_is_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with mock.patch.object(freeze_primary, 'HERE', root/'source'), \
                 mock.patch.object(freeze_primary, 'HISTORICAL', root/'history'):
                with self.assertRaisesRegex(RuntimeError, 'archive-only'):
                    freeze_primary.main()
            self.assertEqual(list(root.iterdir()), [])

    def test_archival_curvature_wrapper_refuses_before_global_patch_or_campaign(self):
        original = json.dumps
        with mock.patch.object(archival_postprocess.frozen, 'run') as campaign:
            with self.assertRaisesRegex(RuntimeError, 'archive-only'):
                archival_postprocess.run()
            campaign.assert_not_called()
        self.assertIs(json.dumps, original)

    def test_other_archive_guards_precede_function_work(self):
        entries = [
            ('order5/compiler/generate_artifacts.py', 'main'),
            ('order5/compiler/build_self_contained_report.py', 'main'),
            ('order5/independent/freeze_tagged.py', 'main'),
            ('order5/independent/interpolate_symbolic_q0.py', 'main'),
            ('order5/independent/independent_compiler.py', 'write_result'),
            ('depth_order5/primary/generate_frozen_artifacts.py', 'main'),
            ('depth_order5/primary/build_self_contained_report.py', 'main'),
            ('depth_order5/primary/compare_frozen_routes.py', 'main'),
        ]
        for relative, name in entries:
            with self.subTest(path=relative):
                tree = ast.parse((HERE/relative).read_text())
                function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
                self.assertIsInstance(function.body[0], ast.Raise)
                code = ast.Module(body=[function.body[0]], type_ignores=[])
                with self.assertRaisesRegex(RuntimeError, 'archive-only'):
                    exec(compile(code, str(HERE/relative), 'exec'), {})


if __name__ == '__main__':
    unittest.main()
