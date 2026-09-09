"""Routing-only adversarial checks. No experiment, compiler, or real seal is run."""
import argparse
import ast
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

REPO = Path('/home/amir/Codes/PDE')
BASE = Path(__file__).resolve().parent
OP = REPO / 'studies/resnet_operator_core'
LONG = REPO / 'studies/resnet_dense_long_horizon'
EARLY = REPO / 'studies/resnet_dense_early_audit'
QUAD = REPO / 'studies/mfp_quadratic_compiler'


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def tree(path):
    return ast.parse(path.read_text(), filename=str(path))


def isolated_function(path, name, namespace):
    node = next(n for n in tree(path).body if isinstance(n, ast.FunctionDef) and n.name == name)
    future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
    unit = ast.fix_missing_locations(ast.Module(body=[future, node], type_ignores=[]))
    exec(compile(unit, str(path), 'exec'), namespace)
    return namespace[name]


def parse_main(path, argv, namespace):
    class Parsed(BaseException):
        pass
    class Parser(argparse.ArgumentParser):
        def parse_args(self, *args, **kwargs):
            result = super().parse_args(argv)
            raise Parsed(result)
    ns = {'__file__': str(path), 'Path': Path, 'argparse': types.SimpleNamespace(ArgumentParser=Parser), **namespace}
    try:
        isolated_function(path, 'main', ns)()
    except Parsed as result:
        return result.args[0]
    raise AssertionError('main did not parse arguments')


class IndependentChecks(unittest.TestCase):
    def test_default_parsers_stop_before_work(self):
        env = {k: v for k, v in os.environ.items() if not k.startswith('PDE_')}
        with patch.dict(os.environ, env, clear=True):
            q = load(QUAD / 'campaign_paths.py', 'campaign_paths')
            l = load(LONG / 'make_manifest.py', 'long_paths_check')
            a = parse_main(EARLY / 'run_dense_resnet_audit.py', [], {})
            self.assertEqual(Path(a.out), REPO / 'data/generated/resnet_dense_early_audit/results')
            a = parse_main(LONG / 'run_all.py', [], {'ROOT': LONG, 'OUTPUT_ROOT': l.OUTPUT_ROOT})
            self.assertEqual(a.output_root, REPO / 'data/generated/resnet_dense_long_horizon')
            self.assertEqual(a.config, LONG / 'config/protocol.json')
            for campaign in ('campaign2', 'campaign3', 'campaign4'):
                a = parse_main(QUAD / campaign / 'postprocess.py', [], vars(q))
                self.assertTrue(a.output.is_relative_to(q.OUTPUT_ROOT))
                for key in ('input', 'plus', 'minus'):
                    if hasattr(a, key):
                        self.assertTrue(getattr(a, key).is_relative_to(q.INPUT_ROOT))

    def test_galerkin_default_stops_at_first_mkdir(self):
        class AtMkdir(BaseException):
            pass
        def stop(path, *args, **kwargs):
            raise AtMkdir(path)
        path = EARLY / 'run_response_galerkin_projection.py'
        ns = {'__file__': str(path), 'Path': Path, 'os': os}
        env = {k: v for k, v in os.environ.items() if k != 'GALERKIN_OUT'}
        with patch.dict(os.environ, env, clear=True), patch.object(Path, 'mkdir', stop):
            with self.assertRaises(AtMkdir) as result:
                isolated_function(path, 'main', ns)()
        self.assertEqual(result.exception.args[0], REPO / 'data/generated/resnet_dense_early_audit/results')

    def test_operator_real_imports_create_no_output(self):
        with tempfile.TemporaryDirectory(dir=BASE) as temp:
            root = Path(temp)
            with patch.dict(os.environ, {'PDE_OPERATOR_OUTPUT_ROOT': str(root / 'out'), 'PDE_OPERATOR_INPUT_ROOT': str(root / 'in')}):
                load(OP / 'runtime_paths.py', 'runtime_paths')
                sys.path.insert(0, str(OP))
                for index, path in enumerate((OP / 'run_pde.py', OP / 'run_exact_reference.py', OP / 'audits/numerics/paired_w_variance.py', *sorted((OP / 'audits/statistical_audit').glob('*.py')))):
                    module = load(path, 'operator_import_' + str(index))
                    if hasattr(module, 'RAW'):
                        self.assertEqual(module.RAW, root / 'in/results/raw')
                    if hasattr(module, 'OUT'):
                        self.assertEqual(module.OUT, root / 'out/audits/statistical_audit')
                self.assertEqual(list(root.iterdir()), [])

    def test_operator_verifier_mismatch_reproduced(self):
        with patch.dict(os.environ, {'PDE_OPERATOR_INPUT_ROOT': str(BASE / 'selected-run'), 'PDE_OPERATOR_OUTPUT_ROOT': str(BASE / 'selected-run')}):
            module = load(OP / 'verify_evidence.py', 'operator_verifier')
        self.assertEqual(module.RAW, OP / 'results/raw')
        self.assertNotEqual(module.RAW, BASE / 'selected-run/results/raw')
        self.assertEqual(module.PROCESSED, OP / 'results/processed')
        self.assertEqual(module.AGENT_OUTPUTS, OP / 'audits')
        expected = OP / 'results/raw/pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz'
        self.assertFalse(expected.exists())
        result = subprocess.run(['bash', str(OP / 'protocol/verify_bundle.sh'), 'evidence'], cwd=BASE, env={**os.environ, 'PYTHON_BIN': '/bin/false'}, capture_output=True, text=True, timeout=5)
        self.assertEqual(result.returncode, 2)
        self.assertIn('Run protocol/reproduce_full.sh first', result.stderr)
        print('CONFIRMED operator verifier/wrapper still select source results, regardless of selected run.')

    def test_early_documented_override_selects_source(self):
        path = EARLY / 'run_dense_resnet_audit.py'
        self.assertIn('python run_dense_resnet_audit.py --out results/reproduced', (EARLY / 'REPRODUCE.md').read_text())
        parsed = parse_main(path, ['--out', 'results/reproduced'], {})
        self.assertEqual((EARLY / parsed.out).resolve(), EARLY / 'results/reproduced')
        self.assertIn('GALERKIN_OUT=results/reproduced', (EARLY / 'REPRODUCE.md').read_text())
        print('CONFIRMED early-audit documented reproduction overrides both new defaults into the source tree.')

    def test_long_analysis_keeps_source_hash_gate(self):
        expected = {'id': 'fixture', 'config_sha256': 'config', 'code_sha256': 'new-code'}
        stale = {**expected, 'code_sha256': 'old-code'}
        ns = {'Path': Path, 'load_trace': lambda p: (stale, {}), 'hashlib': hashlib, 'json': json}
        function = isolated_function(LONG / 'src/dense_mup/analysis.py', 'analyze_directory', ns)
        with patch.object(Path, 'exists', return_value=True), patch.object(Path, 'mkdir', side_effect=AssertionError('unexpected write')):
            with self.assertRaisesRegex(ValueError, 'stale code hash'):
                function(BASE / 'raw', BASE / 'processed', BASE / 'figures', {}, 'fixture', [expected])

    def test_quadratic_frozen_tests_still_fail_on_source_hash(self):
        env = {k: v for k, v in os.environ.items() if not k.startswith('PDE_QUADRATIC_')}
        with patch.dict(os.environ, env, clear=True):
            load(QUAD / 'campaign_paths.py', 'campaign_paths')
            c2 = load(QUAD / 'campaign2/test_provenance.py', 'provenance2')
            c2.ProvenanceTests.setUpClass()
            with self.assertRaises(AssertionError):
                c2.ProvenanceTests('test_durable_hashes').test_durable_hashes()
            for campaign, filename in (('campaign3', 'test_campaign3_provenance.py'), ('campaign4', 'test_campaign4_provenance.py')):
                module = load(QUAD / campaign / filename, 'provenance_' + campaign)
                with self.assertRaises(AssertionError):
                    module.test_frozen_hashes_match_provenance()
        print('CONFIRMED Campaign 2/3/4 frozen source-hash checks fail; no silent waiver.')

    def test_quadratic_certificates_and_budget_match_old_seals(self):
        history = REPO / 'data/historical/studies/mfp_quadratic_compiler'
        for campaign, provenance, certificate, field in (
            ('campaign2', 'provenance_order7.json', 'certificates_order7.json', 'certificates_sha256'),
            ('campaign3', 'provenance_order7.json', 'certificates_order7.json', 'certificates_sha256'),
            ('campaign4', 'provenance_order9.json', 'certificates_order9.json', 'certificate_sha256'),
        ):
            record = json.loads((history / campaign / provenance).read_text())
            hashes = record.get('hashes', record)
            self.assertEqual(hashlib.sha256((QUAD / campaign / certificate).read_bytes()).hexdigest(), hashes[field])
            if campaign == 'campaign4':
                ledger = history / campaign / 'production_budget.json'
                self.assertEqual(hashlib.sha256(ledger.read_bytes()).hexdigest(), hashes['budget_ledger_sha256'])
                self.assertGreater(record['production_measurement']['cumulative_wall_seconds'], 0)
                print('Campaign 4 retained cumulative wall seconds:', record['production_measurement']['cumulative_wall_seconds'])

    def test_campaign6_working_directory_without_running_binary(self):
        with patch.dict(os.environ, {'PDE_QUADRATIC_OUTPUT_ROOT': str(BASE / 'fake-generated')}):
            load(QUAD / 'campaign_paths.py', 'campaign_paths')
            module = load(QUAD / 'campaign6_f13_threshold/run_benchmark.py', 'benchmark_check')
        writes, directories = [], []
        with patch.object(sys, 'argv', ['benchmark', 'probe', '/bin/true']), patch.object(Path, 'mkdir', lambda p, **kw: directories.append(p)), patch.object(Path, 'write_text', lambda p, body: writes.append((p, json.loads(body)))), patch.object(module, 'sha256', return_value='fixture'), patch.object(module.subprocess, 'run', return_value=types.SimpleNamespace(returncode=0, stdout='', stderr='')) as run:
            module.main()
        expected = BASE / 'fake-generated/campaign6_f13_threshold'
        self.assertEqual(run.call_args.kwargs['cwd'], expected)
        self.assertEqual(writes[0][0], expected / 'probe.benchmark.json')
        self.assertEqual(directories, [expected])
        with patch.object(sys, 'argv', ['benchmark', '../escape', '/bin/true']), patch.object(Path, 'mkdir', side_effect=AssertionError('unexpected write')):
            with self.assertRaises(ValueError):
                module.main()


if __name__ == '__main__':
    unittest.main(verbosity=2)
