#!/usr/bin/env python3
"""Bounded routing acceptance. No numerical engines, compilers, or campaigns.

Executes selected, unchanged CLI function bodies with computational dependencies
replaced by explicit fixtures. All writes are intercepted or use a TemporaryDirectory
under this file's private directory. Wrapper child commands are replaced completely.
"""
from __future__ import annotations

import argparse
import ast
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import tempfile
from types import SimpleNamespace
from unittest.mock import patch

PRIVATE = Path(__file__).resolve().parent
REPO = Path('/home/amir/Codes/PDE')
LONG = REPO / 'studies/resnet_dense_long_horizon'
EARLY = REPO / 'studies/resnet_dense_early_audit'
OP = REPO / 'studies/resnet_operator_core'
QUAD = REPO / 'studies/mfp_quadratic_compiler'
STUDIES = (LONG, EARLY, OP, QUAD)


def emit(name, **data):
    print(json.dumps({'check': name, **data}, sort_keys=True))


def load(path, env=None):
    spec = importlib.util.spec_from_file_location('isolated_routing', path)
    module = importlib.util.module_from_spec(spec)
    with patch.dict(os.environ, env or {}, clear=True):
        spec.loader.exec_module(module)
    return module


def functions(path, names, namespace):
    tree = ast.parse(path.read_text())
    nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef)
             and node.name in names]
    assert len(nodes) == len(names)
    tree = ast.Module(body=[ast.ImportFrom(module='__future__',
                     names=[ast.alias(name='annotations')], level=0), *nodes],
                     type_ignores=[])
    ast.fix_missing_locations(tree)
    namespace.update(__file__=str(path), argparse=argparse, Path=Path,
                     json=json, sys=sys)
    exec(compile(tree, str(path), 'exec'), namespace)
    return namespace


def syntax():
    count = 0
    for base in STUDIES:
        for path in base.rglob('*.py'):
            ast.parse(path.read_text(), filename=str(path))
            count += 1
    for path in (LONG/'reproduce.sh', OP/'protocol/reproduce_full.sh',
                 OP/'protocol/verify_bundle.sh'):
        subprocess.run(['bash', '-n', str(path)], check=True)
    emit('syntax', python_files=count, shell_files=3, status='PASS')


def postprocessors():
    accepted = {1:111, 3:1685184, 5:77400633120, 7:7315868433079296}
    class Jet:
        def __init__(self, order): self.order = order
        def eval(self, point): return accepted[self.order]
        def degree(self): return 0
        def nth(self, q): return 0
    jets = {k:Jet(k) for k in accepted}
    runs = 0
    for campaign in ('campaign2', 'campaign3', 'campaign4'):
        for selected in (False, True):
            for explicit in (False, True):
                env = ({'PDE_QUADRATIC_INPUT_ROOT': str(PRIVATE/'selected-input'),
                        'PDE_QUADRATIC_OUTPUT_ROOT': str(PRIVATE/'selected-output')}
                       if selected else {})
                helper = load(QUAD/'campaign_paths.py', env)
                calls, writes = [], []
                def load_jets(path):
                    calls.append(('load', str(path)))
                    return jets
                def sha(path):
                    calls.append(('hash', str(path)))
                    return 'FIXTURE-ONLY-NOT-A-CERTIFICATE'
                def compute(path):
                    calls.append(('load', str(path)))
                    return {'shifted_H1':{'decision':{'status':'FIXTURE'},
                                          'numerator_term_count':0}}
                ns = functions(QUAD/campaign/'postprocess.py', {'main'}, {
                    'HERE':QUAD/campaign, 'INPUT_ROOT':helper.INPUT_ROOT,
                    'OUTPUT_ROOT':helper.OUTPUT_ROOT, 'load_jets':load_jets,
                    'divide_minus_endpoint':lambda j:j, 'sha256':sha,
                    'polynomial_json':lambda j:[], 'certificates':lambda j:{},
                    'stieltjes_expressions':lambda j:{}, 'compute':compute,
                    'sp':SimpleNamespace(Poly=lambda *a:jets[1]), 't':0,
                    'atomic_json':lambda p,v:writes.append(str(p)),
                })
                argv = ['postprocess.py']
                output_name = 'certificates_order9.json' if campaign=='campaign4' else 'certificates_order7.json'
                expected_output = helper.OUTPUT_ROOT/campaign/output_name
                if explicit:
                    expected_output = PRIVATE/'cli-output'/(campaign+'.json')
                    argv += ['--output', str(expected_output)]
                    if campaign=='campaign2':
                        argv += ['--plus',str(PRIVATE/'plus.json'),
                                 '--minus',str(PRIVATE/'minus.json')]
                        expected_inputs = [PRIVATE/'plus.json',PRIVATE/'minus.json']
                    else:
                        argv += ['--input',str(PRIVATE/'input.json')]
                        expected_inputs = [PRIVATE/'input.json']
                else:
                    rels = {'campaign2':['frozen/plus_order7_raw.json','frozen/minus_order7_raw.json'],
                            'campaign3':['frozen/results_order7.json'],
                            'campaign4':['results_order9.json']}[campaign]
                    expected_inputs = [helper.INPUT_ROOT/campaign/rel for rel in rels]
                def record_write(path, text, *args, **kwargs):
                    writes.append(str(path))
                    return len(text)
                with patch.object(sys,'argv',argv), patch.object(Path,'mkdir'), \
                     patch.object(Path,'write_text',record_write), contextlib.redirect_stdout(io.StringIO()):
                    ns['main']()
                assert [p for kind,p in calls if kind=='load']==list(map(str,expected_inputs))
                assert writes==[str(expected_output)], writes
                if campaign=='campaign2':
                    assert ('hash',str(helper.INPUT_ROOT/'campaign2/frozen/two_input_connected_vp')) in calls
                runs += 1
    emit('postprocessor_actual_main_routing', cases=runs, status='PASS',
         note='Computations, hashing and product writes mocked; parser and main wiring unchanged.')


def benchmark():
    for selected in (False, True):
        helper = load(QUAD/'campaign_paths.py',
                      {'PDE_QUADRATIC_OUTPUT_ROOT':str(PRIVATE/'selected-output')} if selected else {})
        calls, writes = [], []
        def child(command, **kwargs):
            calls.append((command, kwargs))
            return SimpleNamespace(returncode=0, stdout='FIXTURE', stderr='')
        import resource
        import time
        ns = functions(QUAD/'campaign6_f13_threshold/run_benchmark.py', {'main'}, {
            'OUTPUT_ROOT':helper.OUTPUT_ROOT, 'MEMORY_BYTES':4*1024**3,
            'CPU_SECONDS':900, 'WALL_SECONDS':900, 'resource':resource,'time':time,
            'subprocess':SimpleNamespace(run=child, TimeoutExpired=subprocess.TimeoutExpired),
            'hashlib':hashlib, 'sha256':lambda p:'FIXTURE-NO-EXECUTABLE-RUN',
        })
        argv = ['run_benchmark.py','routing-fixture',str(PRIVATE/'mock-executable'),'9','0','-1']
        with patch.object(sys,'argv',argv),patch.object(Path,'mkdir'), \
             patch.object(Path,'write_text',lambda p,s,**k:writes.append(str(p))), \
             contextlib.redirect_stdout(io.StringIO()):
            ns['main']()
        assert calls[0][0][-4:]==[str(PRIVATE/'mock-executable'),'9','0','-1']
        assert calls[0][1]['cwd']==helper.OUTPUT_ROOT/'campaign6_f13_threshold'
        assert writes==[str(helper.OUTPUT_ROOT/'campaign6_f13_threshold/routing-fixture.benchmark.json')]
    emit('campaign6_actual_main_routing',cases=2,status='PASS',child_invocations=0)


def wrappers():
    mocked = PRIVATE/'mock_python'
    for selected in (None, str(PRIVATE/'run with spaces'), '~/pde-round3-routing-fixture'):
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHON_BIN=str(mocked))
        for key in ('PDE_OPERATOR_OUTPUT_ROOT','PDE_OPERATOR_INPUT_ROOT'):
            env.pop(key,None)
        if selected: env['PDE_OPERATOR_OUTPUT_ROOT']=selected
        proc = subprocess.run(['bash',str(OP/'protocol/reproduce_full.sh')],cwd=PRIVATE,
                              env=env,text=True,capture_output=True,check=True)
        rows = [json.loads(line) for line in proc.stdout.splitlines() if line.startswith('{')]
        producer = next(row for row in rows if row['argv'][0]=='run_pde.py')
        restart = next(row for row in rows if '--restart-from' in row['argv'])
        root = load(OP/'runtime_paths.py', {'PDE_OPERATOR_OUTPUT_ROOT':producer['operator_output']}).OUTPUT_ROOT
        arg = restart['argv'][restart['argv'].index('--restart-from')+1]
        actual = Path(arg)
        if not actual.is_absolute(): actual = Path(restart['cwd'])/actual
        actual = actual.resolve()
        expected = root/'results/raw/pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz'
        merges = [r for r in rows if r['argv'][0]=='combine_references.py']
        merge_ok = True
        for row in merges:
            for arg in row['argv'][1:]:
                if arg=='--output': continue
                actual_merge=Path(arg)
                if not actual_merge.is_absolute(): actual_merge=Path(row['cwd'])/actual_merge
                merge_ok &= actual_merge.resolve().is_relative_to(root)
        assert all(r['operator_input']==r['operator_output'] for r in rows)
        if selected is None or not selected.startswith('~'):
            assert actual==expected and merge_ok
        else:
            assert actual!=expected and not merge_ok
        emit('operator_wrapper',selected=selected or 'default',mocked_commands=len(rows),
             restart_matches_producer=actual==expected,merges_match_producer=merge_ok,
             expected_restart=str(expected),actual_restart=str(actual))

    # Bash function intercepts every literal `python` call, including test and manifest commands.
    for selected in (None,str(PRIVATE/'long run with spaces')):
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PDE_MOCK_PYTHON=str(mocked))
        env.pop('PDE_LONG_HORIZON_OUTPUT_ROOT',None)
        if selected:env['PDE_LONG_HORIZON_OUTPUT_ROOT']=selected
        code='python() { "$PDE_MOCK_PYTHON" "$@"; }; export -f python; bash "$1"'
        proc=subprocess.run(['bash','-c',code,'routing',str(LONG/'reproduce.sh')],
                            cwd=PRIVATE,env=env,text=True,capture_output=True,check=True)
        rows=[json.loads(line) for line in proc.stdout.splitlines() if line.startswith('{')]
        producer,manifest=rows[1:]
        assert producer['argv'][-2]=='--output-root' and manifest['argv'][-2]=='--output-root'
        assert producer['argv'][-1]==manifest['argv'][-1]
        emit('long_wrapper',selected=selected or 'default',mocked_commands=len(rows),status='PASS')


def manifest():
    module=load(LONG/'make_manifest.py')
    with tempfile.TemporaryDirectory(dir=PRIVATE,prefix='manifest-fixture-') as temp:
        base=Path(temp); source=base/'source'; output=base/'run'
        source.mkdir();output.mkdir()
        (source/'fixture.txt').write_text('FIXTURE SOURCE')
        (output/'fixture.txt').write_text('FIXTURE RUN')
        module.ROOT=source
        with patch.object(sys,'argv',['make_manifest.py','--output-root',str(output)]), \
             contextlib.redirect_stdout(io.StringIO()):
            module.main()
        path=output/'metadata/manifest.json'
        original=json.loads(path.read_text())
        tests={}
        cases={'valid':original}
        wrong_run=copy.deepcopy(original);wrong_run['roots']['run']=str(base/'other')
        cases['wrong_run_root']=wrong_run
        duplicate=copy.deepcopy(original);duplicate['files'].append(duplicate['files'][0])
        cases['duplicate']=duplicate
        for name,label in [('traversal','../escape'),('absolute','/tmp/escape')]:
            altered=copy.deepcopy(original);altered['files'][0]['path']=label;cases[name]=altered
        bad_hash=copy.deepcopy(original);bad_hash['files'][0]['sha256']='0'*64
        cases['changed_hash']=bad_hash
        for name,value in cases.items():
            path.write_text(json.dumps(value))
            before={str(p):p.read_bytes() for p in base.rglob('*') if p.is_file()}
            try:
                with contextlib.redirect_stdout(io.StringIO()): module.verify_manifest(path)
                result='accepted'
            except ValueError: result='rejected'
            after={str(p):p.read_bytes() for p in base.rglob('*') if p.is_file()}
            assert before==after
            assert result==('accepted' if name=='valid' else 'rejected')
            tests[name]=result
        assert original['schema']==2 and {r['root'] for r in original['files']}=={'source','run'}
        emit('schema2_manifest',cases=tests,verification_read_only=True,status='PASS')


def resnet_callers():
    for explicit in (False,True):
        outputs=[]
        ns=functions(EARLY/'run_dense_resnet_audit.py', {'main'}, {
            'finite_difference_scaling_audit':lambda p:outputs.append(str(p)),
            'iid_depth_self_averaging':lambda p:outputs.append(str(p)),
            'summarize':lambda p,v:outputs.append(str(p)),
        })
        expected=PRIVATE/'early selected' if explicit else REPO/'data/generated/resnet_dense_early_audit/results'
        argv=['run_dense_resnet_audit.py','--quick']+(['--out',str(expected)] if explicit else [])
        with patch.object(sys,'argv',argv),patch.object(Path,'mkdir'),contextlib.redirect_stdout(io.StringIO()):
            ns['main']()
        assert outputs==[str(expected)]*3

        writes=[]
        class Plot:
            def __getattr__(self,key):
                return lambda *a,**k:None
            def savefig(self,path,**kwargs):writes.append(str(path))
        ns=functions(EARLY/'run_response_galerkin_projection.py', {'main'}, {
            'os':os,'make_data':lambda *a,**k:(None,None),
            'initialize':lambda *a,**k:None,'train':lambda *a,**k:(None,None),
            'response_contraction':lambda *a:None,
            'triangular_legendre_projection':lambda *a:(None,0,0),
            'write_rows':lambda p,r:writes.append(str(p)),
            'plt':SimpleNamespace(subplots=lambda *a,**k:(Plot(),[Plot(),Plot()]),close=lambda f:None),
        })
        env={'GALERKIN_OUT':str(expected)} if explicit else {}
        with patch.dict(os.environ,env,clear=True),patch.object(Path,'mkdir'),contextlib.redirect_stdout(io.StringIO()):
            ns['main']()
        assert writes==[str(expected/'triangular_galerkin_projection.csv'),
                        str(expected/'triangular_galerkin_projection.png')]

        writes=[];calls=[];reads=[]
        helper=load(LONG/'make_manifest.py')
        selected=PRIVATE/'long selected' if explicit else REPO/'data/generated/resnet_dense_long_horizon'
        config_path=PRIVATE/'fixture-config.json' if explicit else LONG/'config/protocol.json'
        config={'representative':{'group':'fixture','seed':0},'plateau_protocol':{}}
        def read_config(path,**kwargs):
            reads.append(str(path));return json.dumps(config)
        def trace(run,path,**kwargs):
            calls.append(('trace',str(path)));return {'id':'fixture'}
        def analysis(**kwargs):
            calls.append(('analysis',kwargs));return {'FIXTURE':True}
        ns=functions(LONG/'run_all.py', {'main'}, {
            'ROOT':LONG,'OUTPUT_ROOT':REPO/'data/generated/resnet_dense_long_horizon',
            'source_hash':lambda p:'FIXTURE',
            'expand_config':lambda c,s:[{'id':'fixture','group':'fixture','seed':0}],
            'config_hash':lambda c:'FIXTURE','run_trace':trace,
            'environment_record':lambda:{'FIXTURE':True},'analyze_directory':analysis,
        })
        argv=['run_all.py']+(['--config',str(config_path),'--output-root',str(selected)] if explicit else [])
        with patch.object(sys,'argv',argv),patch.object(Path,'mkdir'), \
             patch.object(Path,'exists',return_value=False),patch.object(Path,'read_text',read_config), \
             patch.object(Path,'write_text',lambda p,s,**k:writes.append(str(p))), \
             patch.dict(sys.modules,{'make_manifest':helper}),contextlib.redirect_stdout(io.StringIO()):
            ns['main']()
        assert reads==[str(config_path)]
        assert calls[0]==('trace',str(selected/'results/raw/fixture.npz'))
        consumer=calls[1][1]
        assert consumer['raw_dir']==selected/'results/raw'
        assert consumer['processed_dir']==selected/'results/processed'
        assert consumer['figures_dir']==selected/'figures'
        assert consumer['report_path']==selected/'REPORT.md'
        assert writes==[str(selected/'metadata'/name) for name in
                         ('environment.json','run_manifest.json','source_sha256.txt')]
    emit('resnet_actual_main_callers',cases=6,status='PASS',
         note='Numerical and plotting functions replaced; selected CLI paths reach consumers.')


def centered_roles():
    class StopRead(Exception):pass
    for selected in (False,True):
        env=({'PDE_QUADRATIC_INPUT_ROOT':str(PRIVATE/'centered-input'),
              'PDE_QUADRATIC_OUTPUT_ROOT':str(PRIVATE/'centered-output')} if selected else {})
        helper=load(QUAD/'campaign_paths.py',env)
        tree=ast.parse((QUAD/'centered_depth1_order13/centered_h2_exact.py').read_text())
        main=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main')
        assignment=next(n for n in main.body if isinstance(n,ast.Assign)
                        and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='output')
        output=eval(compile(ast.Expression(assignment.value),'<output-expression>','eval'),
                    {'OUTPUT_ROOT':helper.OUTPUT_ROOT})
        assert output==helper.OUTPUT_ROOT/'centered_depth1_order13/RESULTS.json'
        path=QUAD/'centered_depth1_order13/test_centered_h2_exact.py'
        tree=ast.parse(path.read_text())
        cls=next(n for n in tree.body if isinstance(n,ast.ClassDef))
        method=next(n for n in cls.body if isinstance(n,ast.FunctionDef)
                    and n.name=='test_exact_violation_artifact')
        ns={'INPUT_ROOT':helper.INPUT_ROOT,'json':json}
        module=ast.Module(body=[method],type_ignores=[])
        exec(compile(module,str(path),'exec'),ns)
        reads=[]
        def stop_read(path,**kwargs):reads.append(str(path));raise StopRead
        with patch.object(Path,'read_text',stop_read):
            try:ns[method.name](None)
            except StopRead:pass
        assert reads==[str(helper.INPUT_ROOT/'centered_depth1_order13/RESULTS.json')]
    emit('centered_roles',cases=2,status='PASS',
         note='Producer output expression and actual artifact-consumer method checked; external imports not executed.')


def operator_verifier():
    import numpy as np
    class StopArrays(Exception):pass
    with tempfile.TemporaryDirectory(dir=PRIVATE,prefix='operator-fixture-') as temp:
        base=Path(temp);input_root=base/'input';output_root=base/'unused-output'
        raw=input_root/'results/raw';raw.mkdir(parents=True)
        archive=raw/'fixture.npz'
        np.savez(archive,fixture=np.array([1.0]))
        helper=load(OP/'runtime_paths.py',{'PDE_OPERATOR_INPUT_ROOT':str(input_root),
                    'PDE_OPERATOR_OUTPUT_ROOT':str(output_root)})
        with patch.dict(sys.modules,{'runtime_paths':helper}):
            verifier=load(OP/'verify_evidence.py')
        assert verifier.verify_all_npz()==1
        calls=[]
        def combine(paths):
            calls.append(('raw',list(map(str,paths))));return {'fixture':np.array([1.0])}
        def complete(path):
            calls.append(('processed',str(path)));return {'fixture':np.array([1.0])}
        with patch.object(verifier,'combine_arrays',combine),patch.object(verifier,'load_complete',complete):
            verifier.verify_pooled_reference('pooled.npz',['one.npz','two.npz'])
        assert calls==[('raw',[str(raw/'one.npz'),str(raw/'two.npz')]),
                       ('processed',str(input_root/'results/processed/pooled.npz'))]
        audit=input_root/'audits/statistical_audit';audit.mkdir(parents=True)
        record={'filename':'fixture.npz','sha256':hashlib.sha256(archive.read_bytes()).hexdigest()}
        summary=audit/'ordered_limit_summary.json'
        summary.write_text(json.dumps({'exact_files':{'fixture':record},'pde_files':{'P5':record}}))
        reads=[]
        def stop_arrays(path):reads.append(str(path));raise StopArrays
        with patch.object(verifier,'load_complete',stop_arrays):
            try:verifier.verify_ordered_limit_results()
            except StopArrays:pass
        assert reads==[str(archive)]
        verifier.verify_no_reference_oracle()
        # Run the unchanged shell dispatch with a sentinel primary file and all
        # unittest/verifier child invocations mocked. No real evidence run occurs.
        primary=raw/'pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz'
        primary.write_bytes(b'FIXTURE SENTINEL; NEVER LOADED')
        before={str(p):p.read_bytes() for p in input_root.rglob('*') if p.is_file()}
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',PYTHON_BIN=str(PRIVATE/'mock_python'),
                 PDE_OPERATOR_INPUT_ROOT=str(input_root),PDE_OPERATOR_OUTPUT_ROOT=str(output_root))
        proc=subprocess.run(['bash',str(OP/'protocol/verify_bundle.sh'),'evidence'],
                            cwd=PRIVATE,env=env,text=True,capture_output=True,check=True)
        rows=[json.loads(line) for line in proc.stdout.splitlines() if line.startswith('{')]
        assert len(rows)==2 and rows[-1]['argv']==['verify_evidence.py']
        after={str(p):p.read_bytes() for p in input_root.rglob('*') if p.is_file()}
        assert before==after and not output_root.exists()
        emit('operator_selected_evidence_verifier',status='PASS',
             checked=['NPZ inventory','raw/pooled paths','ordered summary and hashes',
                      'source anti-oracle AST','shell evidence dispatch'],
             evidence_read_only=True,output_directory_created=False)


def refused_output():
    calls=[]
    def solve_one(width,seed,**kwargs):
        calls.append((width,seed))
        return SimpleNamespace(event_time=0)
    ns=functions(QUAD/'operator_ide_closure/finite_width_boundary_layer.py', {'main'},
                 {'solve_one':solve_one,'asdict':lambda value:{'FIXTURE':True}})
    selected=PRIVATE/'never-created.json'
    with patch.object(sys,'argv',['finite_width_boundary_layer.py','--widths','32',
                                  '--seeds','1','--output',str(selected)]):
        try: ns['main']()
        except RuntimeError as error: message=str(error)
        else: raise AssertionError('Expected current CLI refusal')
    assert len(calls)==3 and not selected.exists()
    emit('finite_width_explicit_output',mocked_solve_calls=len(calls),
         exception=message,output_created=False,status='DEFECT')


def builds():
    sector=QUAD/'SECTOR_ENGINE.md'
    text=sector.read_text()
    block=next(b for b in re.findall(r'```sh\n(.*?)```',text,re.S) if 'g++' in b)
    commands=[shlex.split(line) for line in block.replace('\\\n',' ').splitlines()
              if line.startswith('g++ ')]
    sources=[arg for cmd in commands for arg in cmd if arg.endswith('.cpp')]
    # Do not inspect retired paths outside the permitted study.
    assert sources==['studies/mean_field_peeling/quadratic_compiler/sector_parallel.cpp',
                     'studies/mean_field_peeling/quadratic_compiler/sector_parallel_reuse.cpp']
    assert all((QUAD/Path(p).name).is_file() for p in sources)
    emit('sector_engine_build_guide',advertised_sources=sources,
         live_sources=[str(QUAD/Path(p).name) for p in sources],status='DEFECT')


def provenance():
    historical=REPO/'data/historical/studies/mfp_quadratic_compiler'
    mappings={
      'campaign2':('provenance_order7.json',None,{
        'source_sha256':QUAD/'campaign2/two_input_connected.cpp',
        'reference_source_sha256':QUAD/'campaign2/two_input_reference.py',
        'postprocess_source_sha256':QUAD/'campaign2/postprocess.py',
        'certificates_sha256':QUAD/'campaign2/certificates_order7.json'}),
      'campaign3':('provenance_order7.json',None,{
        'source_sha256':QUAD/'campaign3/centered_connected.cpp',
        'reference_source_sha256':QUAD/'campaign3/centered_reference.py',
        'postprocess_source_sha256':QUAD/'campaign3/postprocess.py',
        'raw_results_sha256':historical/'campaign3/frozen/results_order7.json',
        'certificates_sha256':QUAD/'campaign3/certificates_order7.json'}),
      'campaign4':('provenance_order9.json','hashes',{
        'protocol_sha256':QUAD/'campaign4/PROTOCOL.md',
        'results_report_sha256':QUAD/'campaign4/RESULTS.md',
        'wrapper_source_sha256':QUAD/'campaign4/sector_wrapper.cpp',
        'campaign1_graded_source_sha256':QUAD/'campaign1/graded_sector.cpp',
        'runner_sha256':QUAD/'campaign4/run_sectors.py',
        'reference_source_sha256':QUAD/'campaign4/bivariate_reference.py',
        'postprocessor_sha256':QUAD/'campaign4/postprocess.py',
        'provenance_builder_sha256':QUAD/'campaign4/make_provenance.py',
        'frozen_campaign1_result_sha256':historical/'campaign1/results_order9_q2_order8.json',
        'result_sha256':historical/'campaign4/results_order9.json',
        'certificate_sha256':QUAD/'campaign4/certificates_order9.json',
        'budget_ledger_sha256':historical/'campaign4/production_budget.json'})}
    for campaign,(filename,key,mapping) in mappings.items():
        data=json.loads((historical/campaign/filename).read_text())
        if key:data=data[key]
        rows=[]
        for field,path in mapping.items():
            current=hashlib.sha256(path.read_bytes()).hexdigest()
            rows.append({'field':field,'matches':current==data[field],
                         'current':current,'frozen':data[field]})
        emit('frozen_provenance',campaign=campaign,rows=rows)
    expected='1cdc9f40f8180e744275806f667a66e5c4194afe2884c4a57262c2fb7ec7ed43'
    actual=hashlib.sha256((QUAD/'campaign6_f13_threshold/PROTOCOL.md').read_bytes()).hexdigest()
    emit('campaign6_frozen_protocol',matches=actual==expected,current=actual,frozen=expected)


def main():
    syntax();postprocessors();benchmark();wrappers();manifest()
    resnet_callers();centered_roles();operator_verifier();refused_output();builds();provenance()


if __name__=='__main__':main()
