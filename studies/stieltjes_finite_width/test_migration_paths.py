"""Path-only checks; do not import six-thread campaign modules or run jets."""
from __future__ import annotations

import ast
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest

from studies.stieltjes_finite_width.run_paths import GENERATED_ROOT, HISTORICAL_ROOT, parse_paths

HERE = Path(__file__).resolve().parent


def paths(path):
    env = dict(__file__=str(path), GENERATED_ROOT=GENERATED_ROOT, HISTORICAL_ROOT=HISTORICAL_ROOT)
    def value(node):
        if isinstance(node, ast.Constant): return node.value
        if isinstance(node, ast.Name): return env[node.id]
        if isinstance(node, ast.Attribute) and node.attr in ('parent', 'parents'): return getattr(value(node.value), node.attr)
        if isinstance(node, ast.Subscript): return value(node.value)[value(node.slice)]
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div): return value(node.left)/value(node.right)
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == 'Path': return Path(value(node.args[0]))
            if isinstance(node.func, ast.Attribute) and node.func.attr == 'resolve': return value(node.func.value).resolve()
        raise ValueError('not a static path')
    for node in ast.parse(path.read_text()).body:
        if isinstance(node, ast.Assign):
            try: result = value(node.value)
            except (ValueError, KeyError, TypeError, AttributeError, IndexError): continue
            for target in node.targets:
                if isinstance(target, ast.Name): env[target.id] = result
    return env


class FiniteWidthPathTests(unittest.TestCase):
    def test_all_five_campaign_outputs_are_generated(self):
        for name, key in [('run_fresh_calibrated_ratio.py', 'OUT'), ('run_fresh_order13_median.py', 'OUT'),
                          ('jet_control_variate.py', 'OUT'), ('run_fresh_pair_median.py', 'OUTPUT'),
                          ('run_positive_time_pair_median.py', 'OUTPUT')]:
            self.assertTrue(paths(HERE/name)[key].is_relative_to(GENERATED_ROOT), name)

    def test_both_fresh_producer_consumer_roots_agree(self):
        pair = paths(HERE/'run_fresh_pair_median.py')
        positive = paths(HERE/'run_positive_time_pair_median.py')
        corrected = paths(HERE.parent/'stieltjes_direct_loewner/run_corrected_clock_test.py')
        jet = paths(HERE/'jet_control_variate.py')
        self.assertEqual(pair['OUTPUT'], positive['LOCAL_ARCHIVE'])
        self.assertEqual(corrected['OUTPUT'], jet['RUN'])

    def test_historical_input_selection_is_explicit(self):
        for filename, output_key, input_key, history_key in [
            ('jet_control_variate.py', 'OUT', 'RUN', 'HISTORICAL_RUN'),
            ('run_positive_time_pair_median.py', 'OUTPUT', 'LOCAL_ARCHIVE', 'HISTORICAL_ARCHIVE')]:
            env = paths(HERE/filename)
            fresh = parse_paths(env[output_key], [], input_dir=env[input_key], historical_input=env[history_key])
            replay = parse_paths(env[output_key], ['--historical'], input_dir=env[input_key], historical_input=env[history_key])
            self.assertEqual(fresh.input_dir, env[input_key])
            self.assertEqual(replay.input_dir, env[history_key])
            self.assertNotEqual(fresh.output_dir, replay.output_dir)
            self.assertTrue(replay.output_dir.is_relative_to(GENERATED_ROOT/'historical_review'))

    def test_source_and_historical_outputs_are_rejected(self):
        for output in (HERE/'forbidden', HISTORICAL_ROOT/'forbidden'):
            with self.assertRaises(SystemExit):
                parse_paths(GENERATED_ROOT/'test', ['--output-dir', str(output)])

    def test_jet_reader_uses_selected_fixture_before_any_jet_work(self):
        path = HERE/'jet_control_variate.py'
        function = next(n for n in ast.parse(path.read_text()).body if isinstance(n, ast.FunctionDef) and n.name == 'main')
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_dir = root/'inputs'
            input_dir.mkdir()
            raw = input_dir/'raw_width_64.npz'
            raw.write_bytes(b'path fixture only')
            output = root/'fresh'
            selected = []
            class StopBeforeJet(Exception): pass
            def load(path):
                selected.append(path)
                raise StopBeforeJet
            env = dict(OUT=output, RUN=input_dir, HISTORICAL_RUN=root/'history', WIDTHS=(64,),
                       R0=0, R1=0, G0=0, G2=0,
                       np=SimpleNamespace(load=load),
                       parse_paths=lambda *a, **k: SimpleNamespace(input_dir=input_dir, output_dir=output, historical=False))
            exec(compile(ast.Module(body=[function], type_ignores=[]), str(path), 'exec'), env)
            with self.assertRaises(StopBeforeJet): env['main']()
            self.assertEqual(selected, [raw])
            self.assertEqual(list(output.iterdir()), [])


if __name__ == '__main__':
    unittest.main()
