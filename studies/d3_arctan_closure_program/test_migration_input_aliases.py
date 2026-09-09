"""No-science analyzer preflights, including every selected NPZ audit panel."""
import importlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


def module(name):
    return importlib.import_module('studies.d3_arctan_closure_program.analyze_' + name)


def panel_cases():
    return (
        ('gpu_forward_query_budget', ('--output',),
         [f'forward_query_main_n{n}.npz' for n in (256, 512, 1024, 2048, 4096)]
         + [f'forward_query_audit_{tag}_n{n}.npz' for n in (256, 512) for tag in ('h001', 'h0005')]
         + [f'forward_query_audit_{tag}_n{n}.npz' for n in (128, 256) for tag in ('fp32draw64', 'fp64')]),
        ('gpu_middle_saturation', ('--output-json', '--output-md'),
         [f'middle_saturation_main_n{n}.npz' for n in (512, 1024, 2048, 4096)]
         + ['middle_saturation_audit_h0005_n512.npz', 'middle_saturation_audit_fp32draw64_n256.npz', 'middle_saturation_audit_fp64_n256.npz']),
        ('gpu_paired_cavity_product', ('--output',),
         [f'paired_product_main_h001_fp32_n{n}.npz' for n in (128, 256, 512, 1024, 2048)]
         + [f'paired_product_audit_{tag}_fp32_n{n}.npz' for n in (256, 512) for tag in ('h001', 'h0005')]
         + [f'paired_product_audit_h001_{tag}_n{n}.npz' for n in (128, 256) for tag in ('fp32draw64', 'fp64')]),
        ('gpu_susceptibility_trace', ('--json-output', '--md-output'),
         [f'susceptibility_main_n{n}_h0.02_T{t}.npz' for t in (1, 2, 4) for n in (128, 256, 512)]
         + [f'susceptibility_main_extra_n{n}_h0.02_T4.npz' for n in (128, 256, 512)]
         + ['susceptibility_refine_n128_h0.01_T4.npz', 'susceptibility_fine_n128_h0.005_T4.npz',
            'susceptibility_refine_n256_h0.01_T4.npz', 'susceptibility_arithmetic32_n128_h0.02_T4.npz',
            'susceptibility_arithmetic64_n128_h0.02_T4.npz']),
    )


class InputAliasTests(unittest.TestCase):
    def assert_preflight(self, target, argv, *, refused=True):
        first_work = 'summarize' if 'first_passage' in target.__name__ else 'load'
        with mock.patch.object(sys, 'argv', [target.__file__, *map(str, argv)]), \
             mock.patch.object(target, first_work, side_effect=RuntimeError('stop before analysis')) as work:
            if refused:
                with self.assertRaises(ValueError):
                    target.main()
                work.assert_not_called()
            else:
                with self.assertRaisesRegex(RuntimeError, 'stop before analysis'):
                    target.main()
                work.assert_called_once()

    def test_jsonl_every_selected_input_alias(self):
        for name, flags in (('middle_response', ('--main', '--cavity', '--main-fine', '--cavity-fine')),
                            ('response_leverage', ('--coarse', '--fine'))):
            target = module(name)
            for selected_flag in flags:
                for kind in ('same', 'symlink', 'hardlink', 'input-symlink'):
                    with self.subTest(module=name, flag=selected_flag, kind=kind), tempfile.TemporaryDirectory() as tmp:
                        root = Path(tmp)
                        paths = {flag: root / (flag[2:] + '.jsonl') for flag in flags}
                        for path in paths.values():
                            path.write_bytes(b'untouched JSONL fixture\n')
                        selected = paths[selected_flag]
                        output = root / 'result.json'
                        if kind == 'same':
                            output = selected
                        elif kind == 'symlink':
                            output.symlink_to(selected)
                        elif kind == 'hardlink':
                            output.hardlink_to(selected)
                        else:
                            output.write_bytes(selected.read_bytes())
                            paths[selected_flag] = root / 'selected-link.jsonl'
                            paths[selected_flag].symlink_to(output)
                        argv = [part for flag, path in paths.items() for part in (flag, path)]
                        before = {path: path.read_bytes() for path in paths.values()}
                        self.assert_preflight(target, [*argv, '--output', output])
                        self.assertEqual(before, {path: path.read_bytes() for path in paths.values()})

    def test_all_npz_inputs_and_all_output_fields_precede_analysis(self):
        for name, fields, leaves in panel_cases():
            target = module(name)
            with tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                for leaf in leaves:
                    (root / leaf).write_bytes(b'untouched panel placeholder\n')
                for field in fields:
                    for leaf in leaves:
                        with self.subTest(module=name, field=field, input=leaf):
                            argv = ['--input-dir', root]
                            for other in fields:
                                argv += [other, root / leaf if other == field else root / (other[2:] + '.json')]
                            self.assert_preflight(target, argv)
                self.assertTrue(all((root / leaf).read_bytes() == b'untouched panel placeholder\n' for leaf in leaves))

    def test_npz_symlink_hardlink_and_output_output_aliases(self):
        for name, fields, leaves in panel_cases():
            target = module(name)
            for kind in ('symlink', 'hardlink', 'input-symlink'):
                with self.subTest(module=name, kind=kind), tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    source, output = root / leaves[-1], root / 'report.json'
                    if kind == 'input-symlink':
                        output.write_bytes(b'untouched input\n')
                        source.symlink_to(output)
                    else:
                        source.write_bytes(b'untouched input\n')
                        if kind == 'symlink':
                            output.symlink_to(source)
                        else:
                            output.hardlink_to(source)
                    argv = ['--input-dir', root]
                    for index, field in enumerate(fields):
                        argv += [field, output if index == 0 else root / 'other.md']
                    self.assert_preflight(target, argv)
                    self.assertEqual(source.read_bytes(), b'untouched input\n')
            if len(fields) == 2:
                with tempfile.TemporaryDirectory() as tmp:
                    root = Path(tmp)
                    self.assert_preflight(target, ['--input-dir', root, fields[0], root / 'same', fields[1], root / 'same'])

    def test_first_passage_selection_and_aliases(self):
        target = module('first_passage_cooperative')
        for kind in ('same', 'symlink', 'hardlink', 'input-symlink'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                source, output = root / 'first_passage_selected.npz', root / 'result.json'
                if kind == 'input-symlink':
                    output.write_bytes(b'untouched fixture')
                    source.symlink_to(output)
                else:
                    source.write_bytes(b'untouched fixture')
                    if kind == 'same':
                        output = source
                    elif kind == 'symlink':
                        output.symlink_to(source)
                    else:
                        output.hardlink_to(source)
                self.assert_preflight(target, ['--input-dir', root, '--output', output])
                self.assertEqual(source.read_bytes(), b'untouched fixture')

    def test_disjoint_and_stdout_routes_remain_available(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, fields, _leaves in panel_cases():
                argv = ['--input-dir', root]
                for field in fields:
                    argv += [field, root / (field[2:] + '.json')]
                self.assert_preflight(module(name), argv, refused=False)
            for name, flag in (('middle_response', '--main'), ('response_leverage', '--coarse')):
                self.assert_preflight(module(name), [flag, root / 'selected.jsonl'], refused=False)
            (root / 'first_passage_selected.npz').write_bytes(b'private input')
            self.assert_preflight(module('first_passage_cooperative'), ['--input-dir', root, '--output', root / 'fresh.json'], refused=False)

    def test_direct_script_help_from_external_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            for name in ('middle_response', 'response_leverage', 'first_passage_cooperative', *(case[0] for case in panel_cases())):
                result = subprocess.run([sys.executable, '-B', module(name).__file__, '--help'], cwd=tmp,
                                        capture_output=True, text=True, timeout=10)
                self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(list(Path(tmp).iterdir()), [])


if __name__ == '__main__':
    unittest.main()
