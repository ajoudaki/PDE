"""Exercise real routing/writer/CLI code without optional analysis imports."""
import ast
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest import mock

HERE = Path(__file__).resolve().parents[1]
PACKAGE = '_routing_proxy_analysis'
path_spec = importlib.util.spec_from_file_location('_routing_proxy_paths', HERE/'output_paths.py')
paths = importlib.util.module_from_spec(path_spec)
path_spec.loader.exec_module(paths)


def load_writer():
    # Only this actual function is compiled; no bootstrap, plotting, symbolic
    # inventory or frozen analysis is imported or executed.
    source = HERE/'pilot_runner.py'
    node = next(n for n in ast.parse(source.read_text()).body
                if isinstance(n, ast.FunctionDef) and n.name == 'write_json_atomic')
    future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
    env = dict(Path=Path, json=json, require_new_output=paths.require_new_output, require_output=paths.require_output)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future, node], type_ignores=[])), str(source), 'exec'), env)
    return env['write_json_atomic']


class SyntheticAnalysisInvalid(RuntimeError):
    pass


@contextlib.contextmanager
def load_cli(direct=False):
    package_name = 'analysis' if direct else PACKAGE
    # The real package initializer eagerly imports optional symbolic analysis.
    # Substitute only that package/dependency; load the CLI and helper source.
    package = types.ModuleType(package_name)
    package.__path__ = [str(HERE)]
    dependency_name = package_name+'.pilot_runner'
    scientific = types.ModuleType(dependency_name)
    scientific.PilotAnalysisInvalid = SyntheticAnalysisInvalid
    scientific.analyze_pilot = mock.Mock(return_value={'status': 'synthetic_success'})
    scientific.write_json_atomic = load_writer()
    name = '_routing_direct_cli' if direct else PACKAGE+'._routing_module_cli'
    spec = importlib.util.spec_from_file_location(name, HERE/'run_frozen_pilot.py')
    cli = importlib.util.module_from_spec(spec)
    with mock.patch.dict(sys.modules, {package_name: package, dependency_name: scientific}), \
         mock.patch.object(sys, 'path', [str(HERE), *sys.path]):
        spec.loader.exec_module(cli)
        yield cli, scientific.analyze_pilot


class OutputBoundaryTests(unittest.TestCase):
    def run_cli(self, cli, output):
        with mock.patch.object(sys, 'argv', ['pilot', '--summary', 'unread-summary.json',
                              '--config', 'unread-config.json', '--analysis-config', 'unread-analysis.json',
                              '--output', str(output)]), contextlib.redirect_stderr(io.StringIO()):
            return cli.main()

    def protected_outputs(self):
        return [root/'unwritten.json' for root in (
            paths.REPO_ROOT/'studies/stieltjes_proxy_campaign/analysis',
            paths.REPO_ROOT/'data/historical/studies/stieltjes_proxy_campaign',
            paths.REPO_ROOT/'data/generated/resnet_activation_controls',
            paths.REPO_ROOT/'data/generated/stieltjes_proxy_campaign_other',
        )]

    def test_cli_rejects_protected_outputs_before_analysis_in_both_import_modes(self):
        for direct in (False, True):
            with self.subTest(direct=direct), load_cli(direct) as (cli, analyze):
                for output in self.protected_outputs():
                    with self.subTest(output=output), mock.patch.object(Path, 'mkdir') as mkdir:
                        with self.assertRaises(ValueError):
                            self.run_cli(cli, output)
                        analyze.assert_not_called()
                        mkdir.assert_not_called()

    def test_callable_writer_rejects_protected_outputs_without_writes(self):
        writer = load_writer()
        for output in self.protected_outputs():
            with self.subTest(output=output), mock.patch.object(Path, 'mkdir') as mkdir:
                with self.assertRaises(ValueError):
                    writer(output, {'status': 'synthetic'})
                mkdir.assert_not_called()

    def test_own_generated_and_external_scratch_are_valid_without_writes(self):
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(Path, 'mkdir') as mkdir:
            for output in (paths.GENERATED_ROOT/'boundary-test-unwritten.json', Path(tmp)/'fresh.json'):
                self.assertEqual(paths.require_new_output(output), (output.resolve(), output.with_suffix('.json.tmp').resolve()))
            mkdir.assert_not_called()

    def test_final_and_temp_conflicts_stop_cli_before_analysis_and_preserve_bytes(self):
        writer = load_writer()
        with tempfile.TemporaryDirectory() as tmp, load_cli() as (cli, analyze):
            root = Path(tmp)
            for name, suffix in (('final', ''), ('temporary', '.tmp')):
                output = root/f'{name}.json'
                occupied = Path(str(output)+suffix)
                occupied.write_bytes(b'preserve fixture')
                with self.assertRaises(FileExistsError):
                    self.run_cli(cli, output)
                with self.assertRaises(FileExistsError):
                    writer(output, {'status': 'synthetic'})
                analyze.assert_not_called()
                self.assertEqual(occupied.read_bytes(), b'preserve fixture')

    def test_dangling_final_and_temp_links_are_not_replaced(self):
        writer = load_writer()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, suffix in (('final', ''), ('temporary', '.tmp')):
                output = root/f'{name}.json'
                occupied = Path(str(output)+suffix)
                occupied.symlink_to(root/'absent-target')
                with self.assertRaises(FileExistsError):
                    writer(output, {'status': 'synthetic'})
                self.assertTrue(occupied.is_symlink())
                self.assertFalse((root/'absent-target').exists())

    def test_scratch_success_and_failure_records_keep_existing_formats(self):
        for direct in (False, True):
            with self.subTest(direct=direct), tempfile.TemporaryDirectory() as tmp, load_cli(direct) as (cli, analyze):
                root = Path(tmp)
                success = root/'fresh/success.json'
                self.assertEqual(self.run_cli(cli, success), 0)
                self.assertEqual(success.read_text(), json.dumps({'status': 'synthetic_success'}, indent=2, sort_keys=True)+'\n')
                for number, (error, expected_code) in enumerate((
                    (SyntheticAnalysisInvalid('synthetic refusal'), 2),
                    (FileNotFoundError('synthetic missing input'), 1),
                )):
                    output = root/f'fresh/failure{number}.json'
                    analyze.side_effect = error
                    self.assertEqual(self.run_cli(cli, output), expected_code)
                    record = json.loads(output.read_text())
                    self.assertEqual(record['status'], 'inconclusive_analysis_failure')
                    self.assertEqual(record['protocol_result'], 'inconclusive')
                    self.assertEqual(record['failure_type'], type(error).__name__)
                    self.assertEqual(record['reason'], str(error))
                self.assertEqual(list(root.rglob('*.tmp')), [])

    def test_late_temp_file_is_not_truncated(self):
        writer = load_writer()
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)/'output.json'
            temporary = output.with_suffix('.json.tmp')
            original_mkdir = Path.mkdir
            def mkdir_and_introduce_temp(path, *args, **kwargs):
                original_mkdir(path, *args, **kwargs)
                temporary.write_bytes(b'preserve late temporary')
            with mock.patch.object(Path, 'mkdir', mkdir_and_introduce_temp):
                with self.assertRaises(FileExistsError):
                    writer(output, {'status': 'synthetic'})
            self.assertEqual(temporary.read_bytes(), b'preserve late temporary')
            self.assertFalse(output.exists())

    def test_late_final_is_not_replaced(self):
        writer = load_writer()
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)/'output.json'
            original_dumps = json.dumps
            def encode_and_introduce_final(value, **kwargs):
                output.write_bytes(b'preserve late final')
                return original_dumps(value, **kwargs)
            with mock.patch.object(json, 'dumps', side_effect=encode_and_introduce_final):
                with self.assertRaises(FileExistsError):
                    writer(output, {'status': 'synthetic'})
            self.assertEqual(output.read_bytes(), b'preserve late final')
            self.assertTrue(output.with_suffix('.json.tmp').is_file())


if __name__ == '__main__':
    unittest.main()
