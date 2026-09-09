"""Independent bounded routing checks. No scientific runner is dispatched."""
import argparse
import ast
import contextlib
import copy
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

REPO = Path('/home/amir/Codes/PDE')
WORK = Path(__file__).parent
LONG = REPO / 'studies/resnet_dense_long_horizon'
EARLY = REPO / 'studies/resnet_dense_early_audit'
OP = REPO / 'studies/resnet_operator_core'
QUAD = REPO / 'studies/mfp_quadratic_compiler'


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parser_only(path, namespace, argv=()):
    tree = ast.parse(path.read_text())
    function = next(n for n in tree.body if isinstance(n, ast.FunctionDef)
                    and n.name in ('main', 'parse_args'))
    body = []
    for statement in function.body:
        body.append(statement)
        if isinstance(statement, ast.Assign) and isinstance(statement.value, ast.Call):
            call = statement.value
            if isinstance(call.func, ast.Attribute) and call.func.attr == 'parse_args':
                body.append(ast.Return(value=ast.Name(id=statement.targets[0].id, ctx=ast.Load())))
                break
        if isinstance(statement, ast.Return):
            break
    else:
        raise AssertionError('No parser boundary')
    function.body = body
    isolated = ast.fix_missing_locations(ast.Module(body=[function], type_ignores=[]))
    namespace = dict(namespace, argparse=argparse, Path=Path, __file__=str(path))
    exec(compile(isolated, str(path), 'exec'), namespace)
    with patch.object(sys, 'argv', [str(path), *argv]):
        return namespace[function.name]()


def snapshot(base):
    return {str(p.relative_to(base)): p.read_bytes() for p in base.rglob('*') if p.is_file()}


class Checks(unittest.TestCase):
    def test_parser_roots_without_scientific_imports(self):
        args = parser_only(EARLY / 'run_dense_resnet_audit.py', {})
        self.assertEqual(Path(args.out), REPO / 'data/generated/resnet_dense_early_audit/results')
        tree = ast.parse((EARLY / 'run_response_galerkin_projection.py').read_text())
        main = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
        self.assertEqual([type(n).__name__ for n in main.body[:2]], ['Assign', 'Assign'])
        isolated = ast.fix_missing_locations(ast.Module(body=main.body[:2], type_ignores=[]))
        ns = {'Path': Path, 'os': os, '__file__': str(EARLY / 'run_response_galerkin_projection.py')}
        with patch.dict(os.environ, {}, clear=True):
            exec(compile(isolated, '<galerkin-routing>', 'exec'), ns)
        self.assertEqual(ns['out'], Path(args.out))
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            with patch.dict(os.environ, {'PDE_QUADRATIC_INPUT_ROOT': str(base/'in'),
                                         'PDE_QUADRATIC_OUTPUT_ROOT': str(base/'out')}, clear=True):
                helper = load(QUAD / 'campaign_paths.py', 'quad_parser_paths')
                for campaign in ('campaign2', 'campaign3', 'campaign4'):
                    args = parser_only(QUAD / campaign / 'postprocess.py',
                                       {'INPUT_ROOT': helper.INPUT_ROOT, 'OUTPUT_ROOT': helper.OUTPUT_ROOT})
                    self.assertTrue(args.output.is_relative_to(base/'out'/campaign))
                    inputs = [args.plus, args.minus] if campaign == 'campaign2' else [args.input]
                    self.assertTrue(all(p.is_relative_to(base/'in'/campaign) for p in inputs))
                self.assertEqual(helper.certificate_path('campaign4/certificates_order9.json'),
                                 base/'in/campaign4/certificates_order9.json')
                for label in ('studies/mfp_quadratic_compiler/campaign4/sectors/k1_w0_a0.json',
                              'studies/mean_field_peeling/quadratic_compiler/campaign4/sectors/k1_w0_a0.json'):
                    self.assertEqual(helper.recorded_sector_path(label), base/'in/campaign4/sectors/k1_w0_a0.json')
            self.assertEqual(list(base.iterdir()), [])

    def test_manifest_valid_and_negative_read_only_cases(self):
        module = load(LONG / 'make_manifest.py', 'manifest_checks')
        cases = ('valid', 'source_tamper', 'run_tamper', 'size_tamper', 'sums_tamper',
                 'duplicate', 'unknown_root', 'absolute', 'parent_escape', 'symlink_escape',
                 'wrong_run_root', 'old_schema')
        for case in cases:
            with self.subTest(case=case), tempfile.TemporaryDirectory() as tmp:
                base = Path(tmp)
                source, output = base/'source', base/'run'
                source.mkdir()
                output.mkdir()
                (source/'program.txt').write_text('fixture source')
                (source/'metadata').mkdir()
                (source/'metadata/manifest.json').write_text('unchanged historical seal')
                (source/'metadata/SHA256SUMS').write_text('unchanged historical sums')
                (output/'result.txt').write_text('fixture result')
                module.ROOT = source
                with patch.object(sys, 'argv', ['manifest', '--output-root', str(output)]), contextlib.redirect_stdout(io.StringIO()):
                    module.main()
                manifest_path = output/'metadata/manifest.json'
                manifest = json.loads(manifest_path.read_text())
                self.assertEqual(len(manifest['files']), 2)
                row = manifest['files'][1]
                if case == 'source_tamper':
                    (source/'program.txt').write_text('changed source')
                elif case == 'run_tamper':
                    (output/'result.txt').write_text('changed result')
                elif case == 'size_tamper':
                    row['size_bytes'] += 1
                elif case == 'sums_tamper':
                    (output/'metadata/SHA256SUMS').write_text('changed sums')
                elif case == 'duplicate':
                    manifest['files'].append(copy.deepcopy(row))
                elif case == 'unknown_root':
                    row['root'] = 'other'
                elif case == 'absolute':
                    row['path'] = str(output/'result.txt')
                elif case == 'parent_escape':
                    row['path'] = '../source/program.txt'
                elif case == 'symlink_escape':
                    (output/'escape.txt').symlink_to(source/'program.txt')
                    row['path'] = 'escape.txt'
                elif case == 'wrong_run_root':
                    manifest['roots']['run'] = str(base/'elsewhere')
                elif case == 'old_schema':
                    manifest = {'schema': 1, 'files': []}
                manifest_path.write_text(json.dumps(manifest))
                before = snapshot(base)
                with patch.object(sys, 'argv', ['manifest', '--output-root', str(output), '--verify']), contextlib.redirect_stdout(io.StringIO()):
                    if case == 'valid':
                        module.main()
                    else:
                        with self.assertRaises(ValueError):
                            module.main()
                self.assertEqual(snapshot(base), before)
                self.assertEqual((source/'metadata/manifest.json').read_text(), 'unchanged historical seal')

    def test_operator_wrapper_with_record_only_interpreter(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = str(Path(tmp)/'fresh')
            env = dict(os.environ, PYTHON_BIN=str(WORK/'python'), PDE_OPERATOR_OUTPUT_ROOT=output,
                       PDE_OPERATOR_INPUT_ROOT=str(Path(tmp)/'other'), PYTHONDONTWRITEBYTECODE='1')
            result = subprocess.run(['bash', str(OP/'protocol/reproduce_full.sh')], cwd=tmp,
                                    env=env, check=True, capture_output=True, text=True, timeout=10)
            calls = [json.loads(line) for line in result.stdout.splitlines() if line.startswith('{')]
            self.assertEqual(len(calls), 42)
            self.assertTrue(all(c['cwd'] == str(OP) and c['input'] == c['output'] == output for c in calls))
            restarts = [c for c in calls if '--restart-from' in c['args']]
            self.assertEqual(len(restarts), 1)
            restart = restarts[0]['args'][restarts[0]['args'].index('--restart-from')+1]
            self.assertEqual(restart, output+'/results/raw/pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz')
            merges = [c for c in calls if c['args'][0] == 'combine_references.py']
            self.assertEqual(len(merges), 4)
            produced = set()
            for c in calls:
                name = c['args'][0]
                if name not in ('run_pde.py', 'run_exact_reference.py'):
                    continue
                args = parser_only(OP/name, {}, c['args'][1:])
                body = next(n for n in ast.parse((OP/name).read_text()).body
                            if isinstance(n, ast.FunctionDef) and n.name == 'run').body
                if name == 'run_pde.py':
                    base_points = args.base_order**4 if args.quadrature in ('gauss-hermite', 'hybrid') else args.M
                    fast_points = args.fast_order**args.P if args.quadrature == 'gauss-hermite' else args.R
                    ns = {'args': args, 'spec': SimpleNamespace(base_points=base_points, fast_points=fast_points),
                          'start_time': 8.0 if args.restart_from else 0.0,
                          '_tag': lambda value: f'{value:g}'.replace('.', 'p').replace('-', 'm')}
                    index = next(i for i,n in enumerate(body) if isinstance(n, ast.Assign)
                                 and any(isinstance(t,ast.Name) and t.id=='name' for t in n.targets))
                    filename_statements = body[index:index+3]
                    self.assertEqual([type(n).__name__ for n in filename_statements], ['Assign','If','If'])
                    exec(compile(ast.Module(body=filename_statements, type_ignores=[]), '<PDE-filename>', 'exec'), ns)
                    produced.add(output+'/results/raw/'+ns['name'])
                else:
                    statement = next(n for n in body if isinstance(n, ast.Assign)
                                     and any(isinstance(t,ast.Name) and t.id=='path' for t in n.targets))
                    ns = {'args': args, 'output_dir': Path(output)/'results/raw'}
                    exec(compile(ast.Module(body=[statement], type_ignores=[]), '<reference-filename>', 'exec'), ns)
                    produced.add(str(ns['path']))
            self.assertEqual(len(produced), 32)
            self.assertIn(restart, produced)
            for c in merges:
                inputs = c['args'][1:c['args'].index('--output')]
                self.assertTrue(set(inputs).issubset(produced))
                for value in c['args'][1:]:
                    if value != '--output':
                        self.assertTrue(value.startswith(output+'/results/'))
            self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_long_wrapper_with_record_only_interpreter(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(os.environ, PATH=str(WORK)+os.pathsep+os.environ['PATH'],
                       PDE_LONG_HORIZON_OUTPUT_ROOT=str(Path(tmp)/'fresh'), PYTHONDONTWRITEBYTECODE='1')
            result = subprocess.run(['bash', str(LONG/'reproduce.sh')], cwd=tmp, env=env,
                                    capture_output=True, text=True, check=True, timeout=10)
            calls = [json.loads(line) for line in result.stdout.splitlines()]
            self.assertEqual(len(calls), 3)
            self.assertEqual([c['args'][0] for c in calls], ['-m', 'run_all.py', 'make_manifest.py'])
            for c in calls[1:]:
                self.assertEqual(c['args'][-2:], ['--output-root', str(Path(tmp)/'fresh')])
            self.assertEqual(list(Path(tmp).iterdir()), [])

    def test_benchmark_routing_with_mock_child(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            executable = base/'fixture_executable'
            executable.write_bytes(b'fixture; never executed')
            env = {'PDE_QUADRATIC_INPUT_ROOT': str(base/'evidence'), 'PDE_QUADRATIC_OUTPUT_ROOT': str(base/'out')}
            with patch.dict(os.environ, env, clear=True):
                helper = load(QUAD/'campaign_paths.py', 'quad_benchmark_paths')
                with patch.dict(sys.modules, {'campaign_paths': helper}):
                    module = load(QUAD/'campaign6_f13_threshold/run_benchmark.py', 'benchmark_checks')
            completed = subprocess.CompletedProcess([], 0, stdout='fixture stdout', stderr='')
            with patch.object(module.subprocess, 'run', return_value=completed) as child, patch.object(sys, 'argv', ['benchmark', 'synthetic', str(executable), '3']), contextlib.redirect_stdout(io.StringIO()):
                module.main()
            self.assertEqual(child.call_args.kwargs['cwd'], base/'out/campaign6_f13_threshold')
            self.assertEqual(child.call_args.args[0][-2:], [str(executable), '3'])
            result = json.loads((base/'out/campaign6_f13_threshold/synthetic.benchmark.json').read_text())
            self.assertEqual(result['limits'], {'address_space_bytes': 4294967296, 'cpu_seconds': 900, 'wall_seconds': 900})
            self.assertEqual(executable.read_bytes(), b'fixture; never executed')
            self.assertFalse((base/'evidence').exists())

    def test_campaign6_advertised_build_destinations(self):
        # Confirm the concrete defect without invoking either compiler.
        import re
        import shlex
        text = (QUAD/'campaign6_f13_threshold/CAMPAIGN_REPORT.md').read_text()
        block = text.split('Compile the lower and hybrid interval evaluators:', 1)[1].split('```bash', 1)[1].split('```', 1)[0]
        commands = block.replace('\\\n', ' ').strip().split('\n\n')
        destinations = []
        for command in commands:
            args = shlex.split(command)
            self.assertEqual(args[0], 'g++')
            destinations.append((QUAD/'campaign6_f13_threshold'/args[args.index('-o')+1]).resolve())
        self.assertEqual([p.name for p in destinations], ['peeling_lower_bound_checked', 'hybrid_component_interval_checked'])
        self.assertTrue(all(p.is_relative_to(QUAD) for p in destinations))
        self.assertTrue(all(not p.is_relative_to(REPO/'data/generated') for p in destinations))


if __name__ == '__main__':
    unittest.main(verbosity=2)
