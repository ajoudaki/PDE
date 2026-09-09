"""Private interface checks. All science is stopped or replaced by inert mocks."""
import ast
from contextlib import ExitStack, redirect_stdout
import hashlib
import importlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest import mock

ROOT = Path('/home/amir/Codes/PDE')
PRIVATE = Path(__file__).parent
sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True
os.chdir(PRIVATE)
tempfile.tempdir = str(PRIVATE)
os.environ.update(TMPDIR=str(PRIVATE), PYTHONDONTWRITEBYTECODE='1')
ALLOWED = {str(ROOT / p) for p in json.loads((PRIVATE/'before.json').read_text())}
def boundary(event, args):
    if event == 'open' and isinstance(args[0], (str, bytes, os.PathLike)):
        path = os.path.abspath(os.fsdecode(args[0]))
        writing = args[2] & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND)
        if writing and not path.startswith(str(PRIVATE)+'/'):
            raise PermissionError('private writes only: '+path)
        if not writing and path.startswith(str(ROOT)+'/') and path not in ALLOWED:
            raise PermissionError('permitted source only: '+path)
sys.addaudithook(boundary)
from studies._output_paths import StudyPaths

EVIDENCE = []
COVERAGE = []

def fresh(label):
    return Path(tempfile.mkdtemp(prefix=label + '-', dir=PRIVATE))

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def remember(label, paths, before):
    record = {'case': label, 'inputs': [dict(path=str(p), before=before[str(p)], after=digest(p)) for p in paths]}
    EVIDENCE.append(record)
    return all(item['before'] == item['after'] for item in record['inputs'])

def inert(path, text='private selected input\n'):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    return path

def analyzer_cases(root):
    causal = 'studies.causal_flow_peeling_calculus.experiments.'
    d3 = 'studies.d3_arctan_closure_program.'
    yield causal+'analyze_g2_gate_defect', ['--input', root/'raw.csv'], [root/'raw.csv'], ['--output'], [root/'result.json'], 'Path.open'
    p = [root/'p1.csv', root/'p2.csv']; s = [root/'s1/raw.csv', root/'s2/raw.csv']
    yield causal+'analyze_d3_reachable_tail', ['--primary', *p, '--step', *s], p+s+[x.with_name('metadata.json') for x in s], ['--output'], [root/'result.json'], 'read_rows'
    groups = ('primary', 'refined', 'float64-coarse', 'float64-fine')
    argv = [v for g in groups for v in ('--'+g, root/g)]
    inputs = [root/g/'raw_replacement.csv' for g in groups]+[root/'primary/raw_jvp.csv']
    yield causal+'analyze_marked_column_cavity', argv, inputs, ['--output'], [root/'fresh/summary.json', root/'fresh/width_scaling.csv'], 'read_rows'
    for name, flags in [('middle_response', ('main','cavity','main-fine','cavity-fine')), ('response_leverage', ('coarse','fine'))]:
        selected=[root/(f+'.jsonl') for f in flags]
        yield d3+'analyze_'+name, [v for flag,p in zip(flags,selected) for v in ('--'+flag,p)], selected, ['--output'], [root/'result.json'], 'load'
    for name, leaves, flags in [
        ('gpu_forward_query_budget', [f'forward_query_main_n{n}.npz' for n in (256,512,1024,2048,4096)]+[f'forward_query_audit_{tag}_n{n}.npz' for n in (256,512) for tag in ('h001','h0005')]+[f'forward_query_audit_{tag}_n{n}.npz' for n in (128,256) for tag in ('fp32draw64','fp64')], ['--output']),
        ('gpu_middle_saturation', [f'middle_saturation_main_n{n}.npz' for n in (512,1024,2048,4096)]+['middle_saturation_audit_h0005_n512.npz','middle_saturation_audit_fp32draw64_n256.npz','middle_saturation_audit_fp64_n256.npz'], ['--output-json','--output-md']),
        ('gpu_paired_cavity_product', [f'paired_product_main_h001_fp32_n{n}.npz' for n in (128,256,512,1024,2048)]+[f'paired_product_audit_{tag}_fp32_n{n}.npz' for n in (256,512) for tag in ('h001','h0005')]+[f'paired_product_audit_h001_{tag}_n{n}.npz' for n in (128,256) for tag in ('fp32draw64','fp64')], ['--output']),
        ('gpu_susceptibility_trace', [f'susceptibility_main_n{n}_h0.02_T{t}.npz' for t in (1,2,4) for n in (128,256,512)]+[f'susceptibility_main_extra_n{n}_h0.02_T4.npz' for n in (128,256,512)]+['susceptibility_refine_n128_h0.01_T4.npz','susceptibility_fine_n128_h0.005_T4.npz','susceptibility_refine_n256_h0.01_T4.npz','susceptibility_arithmetic32_n128_h0.02_T4.npz','susceptibility_arithmetic64_n128_h0.02_T4.npz'], ['--json-output','--md-output']),
        ('first_passage_cooperative', ['first_passage_any.npz','first_passage_other.npz'], ['--output']),
    ]:
        yield d3+'analyze_'+name, ['--input-dir',root], [root/x for x in leaves], flags, [root/('fresh'+str(i)+'.json') for i in range(len(flags))], 'summarize' if name.startswith('first') else 'load'

def argv_for(name, argv, flags, outputs):
    if name.endswith('marked_column_cavity'):
        return [name, *map(str,argv), '--output', str(outputs[0].parent)]
    return [name, *map(str,argv), *[v for flag,p in zip(flags,outputs) for v in (flag,str(p))]]

class PrivateAcceptance(unittest.TestCase):
    def test_roots_all_ten_and_ordinary_refresh(self):
        names='causal_flow_peeling_calculus d3_arctan_closure_program mfp_gaussian_calculus mfp_cubic_compiler mfp_identity_compiler mfp_linear_growth_uniform_counterexample mfp_sine_compiler mfp_quadratic_l2_order5 stieltjes_resolution mfp_program_history'.split()
        for name in names:
            with self.subTest(tree=name):
                paths=StudyPaths(ROOT/'studies'/name/'entry.py')
                self.assertEqual(paths.generated,ROOT/'data/generated'/name)
                self.assertEqual(paths.input_dir(historical=True),ROOT/'data/historical/studies'/name)
                for bad in (ROOT/'studies'/name/'forbidden', paths.historical/'forbidden', ROOT/'data/generated/other/forbidden'):
                    with self.assertRaises(ValueError): paths.require_output(bad)
                output=inert(fresh(name)/'existing.json')
                self.assertEqual(paths.require_output(output),output)

    def test_ten_complete_selected_sets_and_declared_outputs(self):
        root=fresh('analyzer-selections')
        for name,argv,inputs,flags,outputs,work in analyzer_cases(root):
            with self.subTest(module=name):
                target=importlib.import_module(name)
                for p in inputs: inert(p)
                before={str(p):digest(p) for p in inputs}
                observed={}
                def capture(out, ins):
                    observed.update(outputs={Path(p).resolve() for p in out if p is not None}, inputs={Path(p).resolve() for p in ins if p is not None})
                    raise RuntimeError('stop at preflight')
                with mock.patch.object(sys,'argv',argv_for(name,argv,flags,outputs)), mock.patch.object(target,'guard_outputs',side_effect=capture):
                    with self.assertRaisesRegex(RuntimeError,'stop at preflight'): target.main()
                expected=set(inputs)
                if name.endswith('marked_column_cavity'): expected.add(Path(target.__file__))
                self.assertEqual(observed['inputs'],expected)
                self.assertEqual(observed['outputs'],set(outputs))
                self.assertTrue(remember(name,inputs,before))
                COVERAGE.append(dict(module=name, selected_inputs=[str(p) for p in inputs], outputs=[str(p) for p in outputs]))

    def test_ten_existing_distinct_outputs_dispatch_without_changing_inputs(self):
        root=fresh('analyzer-refresh')
        for name,argv,inputs,flags,outputs,work in analyzer_cases(root):
            with self.subTest(module=name):
                target=importlib.import_module(name)
                for p in inputs+outputs: inert(p)
                before={str(p):digest(p) for p in inputs}
                with ExitStack() as stack:
                    stack.enter_context(mock.patch.object(sys,'argv',argv_for(name,argv,flags,outputs)))
                    if work=='Path.open': stack.enter_context(mock.patch.object(Path,'open',side_effect=RuntimeError('stop before decoding')))
                    else: stack.enter_context(mock.patch.object(target,work,side_effect=RuntimeError('stop before decoding')))
                    with self.assertRaisesRegex(RuntimeError,'stop before decoding'): target.main()
                self.assertTrue(remember('refresh '+name,inputs,before))

    def test_report_input_side_symlink_cannot_be_published_over(self):
        from studies.mfp_program_history.report import build_report as report
        root=fresh('report-input-link')
        output=root/'fresh'; output.mkdir()
        pdf=inert(output/'report.pdf')
        selected=root/'selected.md'; selected.symlink_to(pdf)
        wrapper=inert(root/'wrapper.tex')
        before={str(p):digest(p) for p in (selected,wrapper)}
        with mock.patch.multiple(report,SOURCES=(selected,),REPORT_TEX=wrapper,OUTPUT_DIR=output,BUILD_DIR=output/'build',MARKDOWN_DIR=output/'build/markdown',REPORT_PDF=pdf), mock.patch.object(report,'run',side_effect=AssertionError('compiler reached')):
            with self.assertRaises(ValueError): report.main()
        self.assertTrue(remember('report input-side alias',[selected,wrapper],before))

    def test_gaussian_comparison_preserves_selected_input(self):
        from studies.mfp_gaussian_calculus.order5.compiler import compare_independent as target
        root=fresh('gaussian-comparison-repro')
        selected=root/'selected'; selected.mkdir()
        output=root/'fresh'; output.mkdir()
        empty={name:[] for name in 'ABC'}
        destination=inert(output/'PRIMARY_UNIT_COEFFICIENT_MAP.json',json.dumps({'unit_gram':empty,'private_input_marker':'must survive'})+'\n')
        source=selected/target.INDEPENDENT.name; source.symlink_to(destination)
        tagged=inert(selected/target.INDEPENDENT_TAGGED.name,json.dumps(empty))
        symbolic=inert(selected/target.INDEPENDENT_SYMBOLIC_Q0.name,json.dumps({'maps':empty}))
        inputs=[source,tagged,symbolic]
        before={str(p):digest(p) for p in inputs}
        fake=mock.Mock(); fake.specialize_unit_gram.return_value=fake
        with mock.patch.object(sys,'argv',[target.__file__,'--independent-dir',str(selected),'--output-dir',str(output)]), mock.patch.object(target,'compile_factored',return_value=SimpleNamespace(A=fake,B3=fake,C=fake)), mock.patch.object(target,'expand_coefficient_map',return_value={}), mock.patch.object(target,'serializable_map',return_value=[]):
            target.main()
        self.assertTrue(remember('Gaussian real main with inert compiler mocks',inputs,before), 'selected input was overwritten via input-side symlink')

    def test_identity_consumers_reject_selected_input_alias_before_read(self):
        for leaf,output_name in [('spectral_closure','SPECTRAL_CLOSURE_RESULTS.json'),('audit_hankel40','HANKEL40_RESULTS.json')]:
            with self.subTest(module=leaf):
                source_path=ROOT/'studies/mfp_identity_compiler/linear_gaussian_program/depth2_all_order_search'/(leaf+'.py')
                tree=ast.parse(source_path.read_text())
                main=next(node for node in tree.body if isinstance(node,ast.FunctionDef) and node.name=='main')
                namespace={'PATHS':StudyPaths(source_path),'Path':Path,'json':json,'__file__':str(source_path)}
                exec(compile(ast.Module(body=[main],type_ignores=[]),str(source_path),'exec'),namespace)
                target=SimpleNamespace(main=namespace['main'],__file__=str(source_path))
                root=fresh('identity-'+leaf); selected=root/'selected'; selected.mkdir(); output=root/'fresh'; output.mkdir()
                destination=inert(output/output_name)
                source=selected/'RESULTS.json'; source.symlink_to(destination)
                before={str(source):digest(source)}
                refused=False
                with mock.patch.object(sys,'argv',[target.__file__,'--input-dir',str(selected),'--output-dir',str(output)]), mock.patch.object(Path,'read_text',side_effect=RuntimeError('input read reached')):
                    try: target.main()
                    except ValueError: refused=True
                    except RuntimeError as error: self.assertEqual(str(error),'input read reached')
                self.assertTrue(remember('identity preflight '+leaf,[source],before))
                self.assertTrue(refused,'input/output alias passed directory preflight and reached input read')

    def test_retired_sibling_pure_helpers_remain_importable(self):
        for suffix,helper in [
            ('depth_order5_scalar.multi_observable.audit.run_hostile_checks','parse_expression'),
            ('depth_order5.primary.run_lightweight_checks','sha256'),
            ('depth_order5.audit.run_checks','digest'),
        ]:
            with self.subTest(module=suffix,helper=helper):
                try:
                    module=importlib.import_module('studies.mfp_gaussian_calculus.'+suffix)
                except RuntimeError as error:
                    self.fail('pure helper unavailable because import raises: '+str(error))
                self.assertTrue(callable(getattr(module,helper)))

if __name__=='__main__':
    selected_method={'identity-ast-retry':'test_identity_consumers_reject_selected_input_alias_before_read',
                     'retired-siblings':'test_retired_sibling_pure_helpers_remain_importable'}
    suite=(unittest.TestSuite([PrivateAcceptance(selected_method[sys.argv[1]])])
           if len(sys.argv)>1 else unittest.defaultTestLoader.loadTestsFromTestCase(PrivateAcceptance))
    class Result(unittest.TextTestResult):
        subtests=0
        def addSubTest(self,test,subtest,err):
            self.subtests+=1
            super().addSubTest(test,subtest,err)
    label='adversarial-tests' if len(sys.argv)==1 else sys.argv[1]
    with (PRIVATE/(label+'.log')).open('w') as log:
        result=unittest.TextTestRunner(stream=log,verbosity=2,resultclass=Result).run(suite)
    if EVIDENCE: (PRIVATE/('fixture-hashes.json' if len(sys.argv)==1 else label+'-hashes.json')).write_text(json.dumps(EVIDENCE,indent=2)+'\n')
    if COVERAGE: (PRIVATE/'analyzer-coverage.json').write_text(json.dumps(COVERAGE,indent=2)+'\n')
    summary=dict(tests=result.testsRun,subtests=result.subtests,failures=len(result.failures),errors=len(result.errors),skipped=len(result.skipped))
    (PRIVATE/(label+'.json')).write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary))
    for test,message in result.failures+result.errors: print(test.id(),message)
    sys.exit(not result.wasSuccessful())
