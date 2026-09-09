"""Independent preflight evidence on frozen code; all scientific calls trip."""
import ast
from contextlib import ExitStack, contextmanager
import hashlib
import importlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import types
import unittest
from unittest import mock

PRIVATE = Path(__file__).parent
SNAPSHOT = PRIVATE / 'snapshot'
sys.path.insert(0, str(SNAPSHOT))
os.chdir(SNAPSHOT)
sys.dont_write_bytecode = True
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
os.environ['TMPDIR'] = str(PRIVATE / 'adversarial-tmp')
Path(os.environ['TMPDIR']).mkdir(exist_ok=True)
tempfile.tempdir = os.environ['TMPDIR']

def boundary(event, args):
    if event == 'open' and isinstance(args[0], (str, bytes, os.PathLike)):
        p = Path(os.fsdecode(args[0])).absolute()
        mode, flags = args[1:3]
        write = isinstance(mode, str) and any(c in mode for c in 'wax+')
        write |= isinstance(flags, int) and bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC))
        if write and not p.is_relative_to(PRIVATE):
            raise AssertionError('nonprivate write: ' + str(p))
        if str(p).startswith('/home/amir/Codes/PDE/') or '/data/historical/' in str(p):
            raise AssertionError('live/historical input read: ' + str(p))
    if event == 'subprocess.Popen':
        raise AssertionError('subprocess forbidden in independent probes')
sys.addaudithook(boundary)

class StopBeforeScience(RuntimeError):
    pass

def stop(*args, **kwargs):
    raise StopBeforeScience('science tripwire')

sympy = types.ModuleType('sympy')
sympy.Matrix = sympy.Rational = stop
sys.modules['sympy'] = sympy

PREFIX = 'studies.mfp_gaussian_calculus.'
NAMES = [
 PREFIX + 'order5.compiler.compare_independent',
 PREFIX + 'depth_order5.independent.compare_symbolic_q0',
 PREFIX + 'depth_order5.audit.compare_frozen',
 PREFIX + 'depth_order5.audit.audit_symbolic_q0',
 PREFIX + 'depth_order5.audit.run_normalized_sine_experiment',
 PREFIX + 'depth_order5_observables.independent.run_sine_experiment',
 'studies.mfp_identity_compiler.linear_gaussian_program.depth2_all_order_search.spectral_closure',
 'studies.mfp_identity_compiler.linear_gaussian_program.depth2_all_order_search.audit_hankel40',
]
MODULES = [importlib.import_module(name) for name in NAMES]
G = SNAPSHOT / 'studies/mfp_gaussian_calculus'
MANIFESTS = [json.loads((G / name).read_text()) for name in (
 'depth_order5/primary/PRIMARY_FREEZE_MANIFEST.json',
 'depth_order5/independent/FROZEN_MANIFEST.json')]
WORK = ('compile_factored', 'expand_coefficient_map', 'compile_depth_factored', 'expand_expression',
        'compare_depth_point', '_verify_manifest', '_primary_map', '_independent_map',
        'primary_graded', 'independent_map', 'collect_cell', 'one_jet', 'cell_summary', 'fit_depth',
        'collect', 'one_observation', 'summarize', 'fit', 'spectral_fixed_point', 'audit_family')
FIXTURE_HASHES = []
MATRIX = []

def fingerprint(paths):
    return {str(p): hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None for p in paths}

@contextmanager
def layout(index, *, together=False, declared_source=False):
    m = MODULES[index]
    with tempfile.TemporaryDirectory() as tmp, ExitStack() as stack:
        root = Path(tmp)
        inp, out, src = root / 'input', root / ('input' if together else 'output'), root / 'source'
        for p in (inp, out, src / 'primary', src / 'independent'):
            p.mkdir(parents=True, exist_ok=True)
        selected = []
        if index == 0:
            selected = [inp / name for name in ('independent_coefficient_map.json',
                         'independent_layer_tagged_coefficient_map.json', 'independent_symbolic_q0_coefficient_map.json')]
            outputs = [out / name for name in ('PRIMARY_UNIT_COEFFICIENT_MAP.json',
                       'PRIMARY_LAYER_TAGGED_COEFFICIENT_MAP.json', 'PRIMARY_SYMBOLIC_Q0_COEFFICIENT_MAP.json',
                       'INDEPENDENT_COMPARISON.json')]
        elif index == 1:
            stack.enter_context(mock.patch.multiple(m, HERE=src / 'independent', PRIMARY=src / 'primary'))
            selected = [inp / f'H{d}_LAYER_TAGGED_COEFFICIENTS.json' for d in (3, 4)]
            selected += [src / 'independent/FROZEN_MANIFEST.json', src / 'primary/PRIMARY_FREEZE_MANIFEST.json']
            outputs = [out / 'SYMBOLIC_Q0_COMPARISON.json']
        elif index == 2:
            stack.enter_context(mock.patch.multiple(m, PRIMARY=src / 'primary', INDEPENDENT=src / 'independent',
                PRIMARY_MANIFEST=src / 'primary/PRIMARY_FREEZE_MANIFEST.json',
                INDEPENDENT_MANIFEST=src / 'independent/FROZEN_MANIFEST.json'))
            selected = [m.PRIMARY_MANIFEST, m.INDEPENDENT_MANIFEST,
                        src / 'primary/PRIMARY_FREEZE_SHA256.txt', src / 'independent/FROZEN_MANIFEST_SHA256.txt']
            for role, manifest in zip(('primary', 'independent'), MANIFESTS):
                names = (list(manifest['artifacts']) if role == 'primary' else
                         [record[k]['file'] for record in manifest['artifacts'].values() for k in ('dag', 'expanded', 'text')])
                for name in names:
                    is_map = name.endswith(('_COEFFICIENTS.json', '_COEFFICIENT_MAP.json'))
                    selected.append((src if declared_source and not is_map else inp) / role / name)
            outputs = [out / 'FROZEN_MAP_COMPARISON.json']
        elif index == 3:
            selected = [inp / 'primary' / f'H{d}_LAYER_TAGGED_COEFFICIENTS.json' for d in (3, 4)]
            selected += [inp / 'independent' / f'H{d}_TAGGED_COEFFICIENT_MAP.json' for d in (3, 4)]
            outputs = [out / 'SYMBOLIC_Q0_AUDIT.json']
        elif index == 4:
            stack.enter_context(mock.patch.object(m, 'HERE', src))
            selected = [inp / 'audit/TWO_ORACLE_GATE.json', inp / 'common/NORMALIZED_SINE_FROZEN_PREDICTION.json']
            outputs = [out / 'NORMALIZED_SINE_EXPERIMENT.json'] + [out / f'normalized_sine_H{d}_n{w}.npy'
                      for d in (3, 4) for w in (32, 64, 128, 256)]
        elif index == 5:
            stack.enter_context(mock.patch.object(m, 'HERE', src))
            selected = [inp / 'POST_FREEZE_EXACT_AUDIT.json', inp / 'NORMALIZED_SINE_PREDICTION.json']
            outputs = [out / 'NORMALIZED_SINE_EXPERIMENT.json'] + [out / 'sine_raw' / f'gamma04_H2_n{w}.npy'
                      for w in (16, 32, 64, 128)]
        else:
            stem = 'SPECTRAL_CLOSURE' if index == 6 else 'HANKEL40'
            stack.enter_context(mock.patch.multiple(m, HERE=src, __file__=str(src / Path(m.__file__).name)))
            selected = [inp / 'RESULTS.json', src / (stem + '_PROTOCOL.md'), Path(m.__file__)]
            outputs = [out / (stem + '_RESULTS.json')]
        for p in selected:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(b'inert transport bytes, never scientific input')
        if index == 2:
            for p, payload in zip((m.PRIMARY_MANIFEST, m.INDEPENDENT_MANIFEST), MANIFESTS):
                p.write_text(json.dumps(payload))
        argv = ['private-probe', '--independent-dir' if index == 0 else '--input-dir', str(inp), '--output-dir', str(out)]
        for name in WORK:
            if hasattr(m, name):
                stack.enter_context(mock.patch.object(m, name, side_effect=stop))
        stack.enter_context(mock.patch.object(sys, 'argv', argv))
        yield m, root, inp, out, src, selected, outputs

class AdversarialTests(unittest.TestCase):
    def test_independent_all_selected_inputs_cross_all_actual_output_names(self):
        for index in range(len(MODULES)):
            for fallback in ((False, True) if index == 2 else (False,)):
                with layout(index, declared_source=fallback) as (_, _, _, _, _, inputs, outputs):
                    dims = len(inputs), len(outputs)
                MATRIX.append({'module': NAMES[index], 'source_fallback': fallback, 'inputs': dims[0], 'outputs': dims[1]})
                for i in range(dims[0]):
                    for o in range(dims[1]):
                        kinds = ['input-symlink', 'output-symlink', 'hardlink']
                        if index != 2 or i >= 4:
                            kinds += ['dangling-input-symlink']
                        for kind in kinds:
                            with self.subTest(module=index, fallback=fallback, input=i, output=o, kind=kind), \
                                 layout(index, declared_source=fallback) as (m, root, inp, out, src, inputs, outputs):
                                source, output = inputs[i], outputs[o]
                                output.parent.mkdir(parents=True, exist_ok=True)
                                if kind in ('input-symlink', 'dangling-input-symlink'):
                                    raw = source.read_bytes()
                                    source.unlink()
                                    if kind == 'input-symlink':
                                        output.write_bytes(raw)
                                    source.symlink_to(output.parent / 'lexical-parent' / '..' / output.name)
                                    (output.parent / 'lexical-parent').mkdir(exist_ok=True)
                                elif kind == 'output-symlink':
                                    output.symlink_to(source)
                                else:
                                    output.hardlink_to(source)
                                before = fingerprint(inputs + outputs)
                                # Declared fallback selection uses is_file: a dangling selected
                                # override is intentionally not consumed when source fallback exists.
                                should_refuse = not (index == 2 and not fallback and kind == 'dangling-input-symlink'
                                                     and i >= 4 and not source.name.endswith(('_COEFFICIENTS.json', '_COEFFICIENT_MAP.json')))
                                with ExitStack() as io_stack:
                                    for op in ('write_text', 'write_bytes', 'mkdir'):
                                        io_stack.enter_context(mock.patch.object(Path, op, side_effect=AssertionError('write before refusal')))
                                    # Metadata decoding is necessary for manifest selection only.
                                    if index != 2:
                                        for op in ('read_text', 'read_bytes'):
                                            io_stack.enter_context(mock.patch.object(Path, op, side_effect=AssertionError('input read before refusal')))
                                    with self.assertRaises(ValueError if should_refuse else StopBeforeScience):
                                        m.main()
                                after = fingerprint(inputs + outputs)
                                self.assertEqual(before, after)
                                FIXTURE_HASHES.append({'case': str(self._subtest), 'before': before, 'after': after})

    def test_selection_and_verification_use_identical_actual_declared_paths(self):
        m = MODULES[2]
        # Deliberately override verification's hash function and Path reads in memory.
        for fallback in (False, True):
            with layout(2, declared_source=fallback) as (_, root, inp, out, src, inputs, outputs):
                for role, manifest in zip(('primary', 'independent'), MANIFESTS):
                    directory = src / role
                    mp = directory / ('PRIMARY_FREEZE_MANIFEST.json' if role == 'primary' else 'FROZEN_MANIFEST.json')
                    declared = m._manifest_inputs(directory, mp, inp / role)
                    expected = [p for p in inputs[4:] if p.parent.name == role]
                    self.assertEqual(declared, expected)
                    # The AST proves the verifier calls the very same selector for
                    # both explicit filenames and primary dictionary keys.
                    tree = ast.parse(Path(m.__file__).read_text())
                    funcs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
                    for name in ('_manifest_inputs', '_verify_manifest'):
                        calls = [n for n in ast.walk(funcs[name]) if isinstance(n, ast.Call)
                                 and isinstance(n.func, ast.Name) and n.func.id == '_artifact_path']
                        self.assertEqual(len(calls), 2)

    def test_distinct_same_directory_refresh_reaches_input_or_work_boundary(self):
        for index in range(8):
            with self.subTest(module=index), layout(index, together=True) as (m, root, inp, out, src, inputs, outputs):
                for p in outputs:
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_bytes(b'ordinary reusable output')
                before = fingerprint(inputs + outputs)
                with mock.patch.object(Path, 'read_text', side_effect=stop), mock.patch.object(Path, 'read_bytes', side_effect=stop):
                    with self.assertRaises(StopBeforeScience):
                        m.main()
                self.assertEqual(before, fingerprint(inputs + outputs))

    def test_unselected_source_fallback_alias_does_not_block_selected_copy(self):
        with layout(2) as (m, root, inp, out, src, inputs, outputs):
            target = outputs[0]
            target.write_bytes(b'unselected source alias target')
            (src / 'primary/H3_ARTIFACT_STATS.json').symlink_to(target)
            with self.assertRaises(StopBeforeScience):
                m.main()

    def test_explicit_gate_takes_precedence_over_aliasing_archival_fallback(self):
        for index, leaf in ((4, 'TWO_ORACLE_GATE.json'), (5, 'POST_FREEZE_EXACT_AUDIT.json')):
            with self.subTest(module=index), layout(index) as (m, root, inp, out, src, inputs, outputs):
                outputs[0].write_bytes(b'unselected fallback target')
                (src / leaf).symlink_to(outputs[0])
                with mock.patch.object(m.PATHS, 'input_dir', return_value=inp), \
                     mock.patch.object(sys, 'argv', ['probe', '--historical-inputs', '--output-dir', str(out)]), \
                     mock.patch.object(Path, 'read_text', side_effect=stop):
                    with self.assertRaises(StopBeforeScience):
                        m.main()

    def test_all_checkpoint_fallback_gate_aliases_refuse(self):
        for index, leaf, count in ((4, 'TWO_ORACLE_GATE.json', 9), (5, 'POST_FREEZE_EXACT_AUDIT.json', 5)):
            for o in range(count):
                with self.subTest(module=index, output=o), layout(index) as (m, root, inp, out, src, inputs, outputs):
                    outputs[o].parent.mkdir(parents=True, exist_ok=True)
                    outputs[o].write_bytes(b'fallback metadata alias')
                    (src / leaf).symlink_to(outputs[o])
                    with mock.patch.object(m.PATHS, 'input_dir', return_value=root / 'missing-history'), \
                         mock.patch.object(sys, 'argv', ['probe', '--historical-inputs', '--output-dir', str(out)]), \
                         mock.patch.object(Path, 'read_text', side_effect=AssertionError('gate read')):
                        with self.assertRaises(ValueError):
                            m.main()

    def test_intact_schema_and_budget_refusals_without_calculation(self):
        # Identity length gate: inert identity Q conversion, no determinants.
        m = MODULES[7]
        for count in (0, 39, 41):
            with self.subTest(moment_count=count), layout(7) as (_, root, inp, out, src, inputs, outputs):
                inputs[0].write_text(json.dumps({'moments': ['inert'] * count}))
                with mock.patch.object(m, 'Q', side_effect=lambda v: v):
                    with self.assertRaisesRegex(AssertionError, 'exactly forty'):
                        m.main()
        # Primary schema gate: compiler is replaced with an inert object.
        m = MODULES[1]
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'H3_LAYER_TAGGED_COEFFICIENTS.json'
            p.write_text('{"depth":4,"quotient":"wrong"}')
            with mock.patch.object(m, 'compile_depth_factored', return_value=object()), \
                 mock.patch.object(m, 'primary_specialization', side_effect=stop):
                with self.assertRaisesRegex(RuntimeError, 'unexpected primary schema'):
                    m.compare_depth_point(3, None, input_dir=p.parent)
        self.assertEqual(MODULES[4].ALLOCATIONS, {32:1800,64:1200,128:600,256:250})
        self.assertEqual(MODULES[5].ALLOCATIONS, {16:1200,32:800,64:400,128:150})
        self.assertEqual(MODULES[6].MAX_FEATURE_ORDER, 81)
        self.assertEqual(MODULES[6].MAX_R_ORDER, 82)

    def test_completed_checkpoint_resume_and_bad_shape_without_new_samples(self):
        for index, function, shape in ((4, 'collect_cell', (1800, 3)), (5, 'collect', (1200,))):
            m = MODULES[index]
            with tempfile.TemporaryDirectory() as tmp:
                directory = Path(tmp)
                name = 'normalized_sine_H3_n32.npy' if index == 4 else 'gamma04_H2_n16.npy'
                p = directory / name
                p.write_bytes(b'inert checkpoint - no raw decoding')
                # In-memory shape-only values; no sampling, summaries, or fits.
                values = m.np.zeros(shape)
                with mock.patch.object(m.np, 'load', return_value=values), \
                     mock.patch.object(m.np, 'save', side_effect=AssertionError('completed checkpoint rewritten')), \
                     mock.patch.object(m, 'one_jet' if index == 4 else 'one_observation', side_effect=stop):
                    if index == 4:
                        result = m.collect_cell(3, 32, 1800, 0, output_dir=directory)
                    else:
                        result = m.collect(16, 1200, 0, output_dir=directory)
                    self.assertEqual(result.shape, shape)
                bad = m.np.zeros((1, 4)) if index == 4 else m.np.zeros(1201)
                with mock.patch.object(m.np, 'load', return_value=bad):
                    with self.assertRaisesRegex(RuntimeError, 'invalid checkpoint|checkpoint too long'):
                        if index == 4:
                            m.collect_cell(3, 32, 1800, 0, output_dir=directory)
                        else:
                            m.collect(16, 1200, 0, output_dir=directory)

    def test_manifest_hash_and_size_checks_remain_strict(self):
        m = MODULES[2]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            artifact = root / 'inert.txt'
            artifact.write_bytes(b'inert artifact')
            good = hashlib.sha256(artifact.read_bytes()).hexdigest()
            for wrong_field in ('sha256', 'bytes'):
                record = {'sha256': good, 'bytes': artifact.stat().st_size}
                record[wrong_field] = 'bad' if wrong_field == 'sha256' else 999
                manifest = json.dumps({'artifacts': {artifact.name: record}}).encode()
                with mock.patch.object(m, 'PRIMARY', root), \
                     mock.patch.object(Path, 'read_text', return_value=hashlib.sha256(manifest).hexdigest()), \
                     mock.patch.object(Path, 'read_bytes', autospec=True, side_effect=lambda p: manifest if p.name == 'manifest' else b'inert artifact'):
                    with self.assertRaises(AssertionError):
                        m._verify_manifest(root, root / 'manifest', root / 'hash', data_directory=root)

    def test_replay_imports_and_every_helper_preserve_import_purity(self):
        relatives = ['depth_order5/audit/run_checks.py', 'depth_order5/primary/run_lightweight_checks.py',
                     'depth_order5_scalar/multi_observable/audit/run_hostile_checks.py']
        paths = [G / relative for relative in relatives] + [Path(m.__file__) for m in MODULES]
        for path in paths:
            code = compile(path.read_text(), str(path), 'exec')
            tree = ast.parse(path.read_text())
            names = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]
            namespace = {'__name__':'private_import', '__file__':str(path)}
            with self.subTest(relative=str(path.relative_to(SNAPSHOT))), ExitStack() as stack:
                for name in ('open','read_text','read_bytes','write_text','write_bytes','mkdir','unlink','rename','replace'):
                    stack.enter_context(mock.patch.object(Path, name, side_effect=AssertionError('import I/O')))
                stack.enter_context(mock.patch('builtins.open', side_effect=AssertionError('import builtins I/O')))
                for name in ('Popen','run','check_call','check_output','call'):
                    stack.enter_context(mock.patch.object(subprocess, name, side_effect=AssertionError('import subprocess')))
                namespace['__package__'] = '.'.join(path.relative_to(SNAPSHOT).parts[:-1])
                exec(code, namespace)
                self.assertTrue(all(callable(namespace[n]) for n in names))

    def test_hostile_entire_executable_body_remains_below_unconditional_raise(self):
        path = G / 'depth_order5_scalar/multi_observable/audit/run_hostile_checks.py'
        tree = ast.parse(path.read_text())
        main = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
        self.assertIsInstance(main.body[0], ast.Raise)
        self.assertEqual(main.end_lineno, 417)
        self.assertEqual(len(main.body), 73)
        text = ast.unparse(main)
        for token in ('AUDIT_CONTRACT_FREEZE.json','HOSTILE_CANDIDATE_V2_FREEZE.json',
                      'FINAL_ROUTE_A_FREEZE.json','FINAL_PRODUCER_FREEZE.json','promotion_gates',
                      'count_free_trees.py','print(json.dumps(result', 'raise SystemExit(1)'):
            self.assertIn(token, text)
        # No executable audit assignments escaped to module scope.
        assigned = {n.id for node in tree.body if not isinstance(node, ast.FunctionDef)
                    for n in ast.walk(node) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store)}
        self.assertFalse(assigned & {'checks','promotion_gates','result'})

class Recorded(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subtests = 0
    def addSubTest(self, test, subtest, outcome):
        self.subtests += 1
        super().addSubTest(test, subtest, outcome)

with (PRIVATE / 'adversarial.log').open('w') as log:
    result = unittest.TextTestRunner(stream=log, verbosity=2, resultclass=Recorded).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(AdversarialTests))
payload = {'tests':result.testsRun, 'subtests':result.subtests,
           'failures':[(t.id(),text) for t,text in result.failures],
           'errors':[(t.id(),text) for t,text in result.errors],
           'matrix':MATRIX, 'fixture_hash_cases':len(FIXTURE_HASHES),
           'optional_stub':'sympy import only; Matrix/Rational raise'}
(PRIVATE / 'adversarial.json').write_text(json.dumps(payload, indent=2) + '\n')
(PRIVATE / 'fixture-hashes.json').write_text(json.dumps(FIXTURE_HASHES, indent=2) + '\n')
print(json.dumps(payload, indent=2))
sys.exit(not result.wasSuccessful())
