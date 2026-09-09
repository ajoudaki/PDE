"""Path and fail-closed checks only; no FP64 engine, GPU, bootstrap or plots."""
from __future__ import annotations

import ast
import hashlib
import importlib.util
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest import mock

from studies.stieltjes_hybrid_campaign.breadth_panel import successive_paths as paths
from studies.stieltjes_hybrid_campaign.breadth_panel.fp64_successor.legacy_runtime import require_current_authorization

HERE = Path(__file__).resolve().parent


def load_source(relative, name):
    spec = importlib.util.spec_from_file_location(name, HERE/relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class SuccessivePathTests(unittest.TestCase):
    def test_fresh_and_historical_roots_are_explicit(self):
        for study in ('successive_n4096', 'successive_n8192'):
            fresh = paths.parse_analysis_paths(study, [])
            history = paths.parse_analysis_paths(study, ['--historical'])
            self.assertEqual(fresh.input_dir, paths.GENERATED_PANEL/study)
            self.assertEqual(fresh.manifest_dir, fresh.input_dir)
            self.assertEqual(history.input_dir, paths.HISTORICAL_PANEL/study)
            self.assertEqual(history.manifest_dir, HERE/study)
            self.assertEqual(history.output_dir, fresh.output_dir/'historical_review')

    def test_explicit_inputs_and_outputs_are_not_inferred_from_cwd(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            args = paths.parse_analysis_paths('successive_n4096', [
                '--input-dir', str(root/'arrays'), '--manifest-dir', str(root/'manifests'),
                '--output-dir', str(root/'fresh')])
            self.assertEqual(args.input_dir, root/'arrays')
            self.assertEqual(args.manifest_dir, root/'manifests')
            self.assertEqual(args.output_dir, root/'fresh')
            self.assertEqual(list(root.iterdir()), [])

    def test_source_and_history_outputs_are_rejected(self):
        for target in (HERE/'forbidden', paths.HISTORICAL_PANEL/'forbidden'):
            with self.assertRaises(ValueError):
                paths.parse_analysis_paths('successive_n4096', ['--output-dir', str(target)])

    def test_selected_block_manifest_and_array_roots(self):
        relative = 'successive_n4096/analyze.py'
        tree = ast.parse((HERE/relative).read_text())
        function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'load_block')
        future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
        code = ast.fix_missing_locations(ast.Module(body=[future, function], type_ignores=[]))
        class StopBeforeArrays(Exception): pass
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def selected(*args, **kwargs):
                self.assertEqual(args[4], root/'manifests/runs/fixture')
                self.assertEqual(kwargs['arrays_dir'], root/'arrays/runs/fixture')
                raise StopBeforeArrays
            env = dict(OUTPUT_ROOT=paths.GENERATED_PANEL/'successive_n4096',
                       expected_point=lambda *a: {'key': 'fixture'}, validate_block_manifest=selected)
            exec(compile(code, relative, 'exec'), env)
            with self.assertRaises(StopBeforeArrays):
                env['load_block']({}, 'C', 0, 8, input_dir=root/'arrays', manifest_dir=root/'manifests')
            self.assertEqual(list(root.iterdir()), [])

    def test_comparison_forwards_selected_roots_to_both_widths(self):
        comparison = load_source('successive_n8192/compare_with_n4096.py', 'path_test_width_comparison')
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for width in (4096, 8192):
                calls = []
                config = {'width': width, 'nodes': [0.5], 'lineage_blocks': [[0, 8]]}
                def block(*args, **kwargs):
                    calls.append(kwargs)
                    return object()
                analyzer = SimpleNamespace(CONFIG_PATH=root/'config', read_json=lambda p: config,
                    validate_campaign_config=lambda c: None, load_block=block,
                    merge_blocks=lambda blocks, key: object(), central_common_clock=lambda *a: (None, {}))
                with mock.patch.object(comparison, 'CONFIGURATION_ORDER', ('C',)), \
                     mock.patch.object(comparison, 'validate_retained_result', return_value={}) as checked:
                    campaign = comparison.load_campaign(width, HERE/f'successive_n{width}', analyzer,
                        input_dir=root/'arrays', manifest_dir=root/'manifests')
                self.assertEqual(calls, [dict(input_dir=root/'arrays', manifest_dir=root/'manifests')])
                self.assertEqual(checked.call_args.kwargs['input_dir'], root/'arrays')
                self.assertEqual(campaign.manifest_directory, root/'manifests')
                self.assertEqual(campaign.input_directory, root/'arrays')

    def test_n8192_frozen_transform_still_refuses_before_work(self):
        wrapper = load_source('successive_n8192/analyze.py', 'path_test_n8192_wrapper')
        self.assertNotEqual(hashlib.sha256(wrapper.BASE_ANALYZER.read_bytes()).hexdigest(), wrapper.EXPECTED_BASE_SHA256)
        with self.assertRaisesRegex(RuntimeError, 'refusing an unreviewed'):
            wrapper.load_analyzer()

    def test_comparison_transform_refusal_creates_no_output(self):
        comparison = load_source('successive_n8192/compare_with_n4096.py', 'path_test_comparison_refusal')
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)/'not-created'
            with mock.patch.object(sys, 'argv', ['compare', '--historical', '--output-dir', str(output)]):
                with self.assertRaisesRegex(RuntimeError, 'refusing an unreviewed'):
                    comparison.main()
            self.assertFalse(output.exists())

    def test_all_six_legacy_main_guards_precede_work(self):
        entries = ['fp64_successor/'+name for name in (
            'watchdog_launcher.py', 'gpu_preflight.py', 'run_local_qualification.py',
            'adjudicate_local_qualification.py')]
        entries += [f'successive_n{width}/run_block.py' for width in (4096, 8192)]
        for relative in entries:
            with self.subTest(path=relative):
                tree = ast.parse((HERE/relative).read_text())
                function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
                self.assertEqual(function.body[0].value.func.id, 'require_current_authorization')
                env = dict(require_current_authorization=require_current_authorization)
                exec(compile(ast.Module(body=[function], type_ignores=[]), relative, 'exec'), env)
                with self.assertRaisesRegex(RuntimeError, 'archive-only FP64 runtime'):
                    env['main']()

    def test_attempt_reservation_and_failure_finalization_refuse_before_writes(self):
        for relative, name, args in [
            ('fp64_successor/run_local_qualification.py', 'reserve_canonical_attempt', (None, {}, 'A', 'cuda:0', {})),
            ('fp64_successor/watchdog_launcher.py', 'finalize_external_group_failure', (None, None, 'A', 0, '', ''))]:
            tree = ast.parse((HERE/relative).read_text())
            function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
            future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
            code = ast.fix_missing_locations(ast.Module(body=[future, function], type_ignores=[]))
            env = dict(require_current_authorization=require_current_authorization)
            exec(compile(code, relative, 'exec'), env)
            with self.assertRaisesRegex(RuntimeError, 'archive-only FP64 runtime'):
                env[name](*args)


if __name__ == '__main__':
    unittest.main()
