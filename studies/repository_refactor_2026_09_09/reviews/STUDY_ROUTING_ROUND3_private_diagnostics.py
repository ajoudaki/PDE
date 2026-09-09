"""Private stdlib/AST/mock migration diagnostics. No scientific imports/work."""
import argparse
import ast
import contextlib
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace as NS
from unittest import mock

ROOT = Path('/home/amir/Codes/PDE')
PRIVATE = Path(__file__).parent
sys.path.insert(0, str(ROOT))
from studies._output_paths import StudyPaths
from studies.stieltjes_finite_width.run_paths import parse_paths
records = []
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def emit(name, **evidence):
    records.append(dict(name=name, **evidence))
def load_functions(relative, names, env):
    source = ROOT/relative
    tree = ast.parse(source.read_text())
    nodes = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
    assert {n.name for n in nodes} == set(names)
    future = ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future, *nodes], type_ignores=[])), str(source), 'exec'), env)
    return env
class StopBeforeScience(Exception):
    pass

# Complete entry functions, with only scientific/dependency operations mocked.
for filename, target in [('run_fresh_order13_median.py', 'exact_targets'),
                         ('run_fresh_calibrated_ratio.py', 'exact_values')]:
    with tempfile.TemporaryDirectory(dir=PRIVATE) as temp:
        work = Path(temp)
        resource = mock.Mock()
        env = dict(OUT=work/'output', parse_paths=parse_paths, resource=resource,
                   ADDRESS_CAP=8*1024**3, WIDTHS=(128,256), COUNT=512,
                   SEED_BASE=1, BOOTSTRAPS=20000, BOOTSTRAP_BASE=2,
                   os=os, PROTOCOL=work/'not-read', Path=Path, __file__=str(ROOT/'studies/stieltjes_finite_width'/filename),
                   sha256=lambda _: 'not-read', MFP_COMPILER=ROOT/'studies/mfp_quadratic_compiler',
                   CERTIFICATE=work/'not-read', **{target:lambda: ([], 0)})
        load_functions('studies/stieltjes_finite_width/'+filename, ['main'], env)
        with mock.patch.object(sys, 'argv', [filename]):
            try: env['main']()
            except NameError as exc:
                assert exc.name == 'PEELING'
                emit('undefined_migrated_path', file=filename, exception=str(exc),
                     output_directory_created=(work/'output').is_dir(),
                     memory_limit_attempted=resource.setrlimit.called,
                     scientific_calls=0)

for kind in ('hardlink', 'symlink', 'directory'):
    with tempfile.TemporaryDirectory(dir=PRIVATE) as temp:
        work = Path(temp)
        retained = work/'retained.log'
        retained.write_bytes(b'private retained input\n')
        output = work/'generated'
        output.mkdir()
        if kind == 'directory':
            target = work/'target'
            target.mkdir()
            retained = target/'run.log'
            retained.write_bytes(b'private retained input\n')
            output = work/'generated-link'
            output.symlink_to(target, target_is_directory=True)
        elif kind == 'hardlink': os.link(retained, output/'run.log')
        else: (output/'run.log').symlink_to(retained)
        before = digest(retained)
        env = dict(OUTPUT=output, sys=sys, np=NS(__version__='mock'),
                   platform=NS(platform=mock.Mock(side_effect=StopBeforeScience)))
        load_functions('studies/stieltjes_direct_loewner/run_corrected_clock_test.py', ['main','log_factory'], env)
        factory = env['log_factory']
        handles = []
        def tracked_factory(path):
            log, handle = factory(path)
            handles.append(handle)
            return log, handle
        env['log_factory'] = tracked_factory
        with mock.patch.object(sys, 'argv', ['private-output-boundary']), contextlib.redirect_stdout(io.StringIO()):
            try: env['main']()
            except StopBeforeScience: pass
        for handle in handles: handle.close()
        after = digest(retained)
        assert after != before
        emit('corrected_clock_log_alias', kind=kind, before=before, after=after,
             resulting_text=retained.read_text(), scientific_calls=0)

# Actual activation text writer with an aliased intermediate, no analyzer import.
for kind in ('ordinary', 'hardlink', 'symlink'):
    with tempfile.TemporaryDirectory(dir=PRIVATE) as temp:
        work=Path(temp)
        output=work/'processed/summary.json'
        output.parent.mkdir()
        retained=work/'input.json'
        retained.write_bytes(b'private input record\n')
        partial=output.with_name(output.name+'.partial')
        if kind == 'ordinary':
            retained=partial
            retained.write_bytes(b'private input record\n')
        elif kind == 'hardlink': os.link(retained, partial)
        else: partial.symlink_to(retained)
        before=digest(retained)
        env=load_functions('studies/resnet_activation_controls/analyze_activation.py',
                           ['_atomic_text'], dict(Path=Path, os=os))
        env['_atomic_text'](output, 'private output record\n')
        observed=output if kind=='ordinary' else retained
        after=digest(observed)
        assert after != before
        emit('activation_analysis_intermediate', kind=kind, before=before, after=after)

# Raw activation publication statements from the fully inspected run function.
relative='studies/resnet_activation_controls/source/run_pde.py'
run=next(n for n in ast.parse((ROOT/relative).read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='run')
start=next(i for i,n in enumerate(run.body) if isinstance(n,ast.Expr) and
           isinstance(n.value,ast.Call) and ast.unparse(n.value.func)=='output_dir.mkdir')
end=next(i for i,n in enumerate(run.body) if isinstance(n,ast.Expr) and
         isinstance(n.value,ast.Call) and ast.unparse(n.value.func)=='os.replace')
publication=compile(ast.Module(body=run.body[start:end+1], type_ignores=[]),str(ROOT/relative),'exec')
for overlap in ('final_restart', 'partial_restart'):
    with tempfile.TemporaryDirectory(dir=PRIVATE) as temp:
        work=Path(temp)
        name='pde_fixture_legacy_QMC_P1_N1_M1_R1_s1_dt1_T1_cfg'+'a'*12+'.npz'
        retained=work/(name+('.partial' if overlap=='partial_restart' else ''))
        retained.write_bytes(b'private restart bytes; no scientific archive\n')
        before=digest(retained)
        guard=StudyPaths(ROOT/relative)
        assert guard.require_output(work)==work
        def save(handle, **_):
            handle.write(b'private publication bytes\n')
        env=dict(output_dir=work, case_info={'case_id':'fixture','case_sha256':'legacy'},
                 args=NS(quadrature='sobol',P=1,N=1,seed=1,dt=1,duration=1,integrator='rk4',restart_from=retained),
                 spec=NS(base_points=1,fast_points=1), scientific_config_sha256='a'*64,
                 _tag=lambda x:str(x), start_time=0, np=NS(savez_compressed=save,array=lambda x:x),
                 os=os,json=json,config={},state=NS(B=[],a=[],c=[]),
                 **{key:[] for key in ('times','f','loss','grams','theta','theta_min','residual','loss_dot','projected_energy')})
        exec(publication,env)
        output=work/name
        after=digest(output)
        assert after != before
        emit('activation_raw_restart_overlap', overlap=overlap, before=before, after=after,
             input_still_exists=retained.exists(), output=output.name, scientific_calls=0)

# Producer label versus consumer root: inert in-memory metadata, no seal creation.
with tempfile.TemporaryDirectory(dir=PRIVATE) as temp:
    work=Path(temp)
    source=work/'source'
    source.mkdir()
    results=work/'generated/results'
    archive=results/'pde/input.npz'
    archive.parent.mkdir(parents=True)
    archive.write_bytes(b'private routing fixture\n')
    token_file=work/'unsealed-token'
    token_file.write_bytes(b'not an authorization')
    fields=('dynamics_sha256','source_sha256','source_files','protocol_sha256','protocol_files',
            'execution_sha256','execution_files','parent_source_lineage','inference_roles')
    inputs={key:'in-memory-fixture' for key in fields}
    env=dict(ROOT=source,RESULTS=results,os=os,Path=Path,INPUT_MANIFEST_PATH=token_file,__file__=str(token_file),
             _require_input_manifest=lambda:inputs,_sha256=digest,IntegrityError=RuntimeError)
    load_functions('studies/resnet_activation_controls/run_experiment.py',
                   ['_evidence_relative','_require_seal_common'],env)
    label=env['_evidence_relative'](archive)
    record=dict(inputs,schema_version=1,stage='fixture',input_manifest_sha256=digest(token_file),
                orchestrator_sha256=digest(token_file),files={label:digest(archive)})
    try: env['_require_seal_common'](record,'fixture')
    except RuntimeError as exc:
        emit('activation_seal_routing', label=label, producer=str(archive.relative_to(work)),
             consumer=str((source/label).relative_to(work)), exception=str(exc),
             before=digest(archive),after=digest(archive),authorization='not tested or renewed')

# Full width-analysis entry point; all scientific calls are mocked.
for alias in ('same','lexical','symlink','hardlink'):
    with tempfile.TemporaryDirectory(dir=PRIVATE) as temp:
        work=Path(temp)
        names=['n2048','n4096','n8192-shard0','n8192-shard1','n4096-halfstep']
        inputs=[work/(name+'.npz') for name in names]
        for path in inputs: path.write_bytes(b'private width input\n')
        selected=inputs[0]
        output=selected
        if alias=='lexical':
            (work/'sub').mkdir()
            output=work/'sub/../n2048.npz'
        if alias=='symlink':
            output=work/'output.json'
            output.symlink_to(selected)
        if alias=='hardlink':
            output=work/'output.json'
            os.link(selected,output)
        before=digest(selected)
        loaded=[]
        def load_npz(path):
            loaded.append(str(path))
            path.read_bytes()
            return {}
        env=dict(argparse=argparse,Path=Path,json=json,load_npz=load_npz,
                 merge_shards=lambda _: {},
                 bootstrap_campaign=lambda *a,**k:{'width_models':{n:{'mandatory_union':{'full_width':[]}}
                                                               for n in ('effective','progress')}},
                 initialization_calibration=lambda *a:{}, np=NS(asarray=lambda v,**kw:v,float64='mock'),
                 jackknife_clock_bias=lambda *a:{},step_halving_gate=lambda *a:{},
                 authorization_diagnostics=lambda *a:{})
        load_functions('studies/stieltjes_hybrid_campaign/width_ladder/width_analysis.py',['main','_json_ready'],env)
        argv=['private-width']
        for name,path in zip(names,inputs): argv += ['--'+name,str(path)]
        argv += ['--output',str(output)]
        with mock.patch.object(sys,'argv',argv):
            code=env['main']()
        after=digest(selected)
        assert code==0 and len(loaded)==5 and before!=after
        emit('width_analysis_own_input_alias',kind=alias,before=before,after=after,
             exit_code=code,inputs_read=len(loaded),scientific_calls=0)

# Missing-reference preflight: stop at the first engine call; no GPU import.
with tempfile.TemporaryDirectory(dir=PRIVATE) as temp:
    reference=Path(temp)/'missing-reference.npz'
    engine=mock.Mock()
    engine.run_point.side_effect=StopBeforeScience
    torch=mock.Mock()
    env=dict(parse_args=lambda:NS(step=5e-6,device='cuda:0'),torch=torch,reference_engine=engine,
             float64_draw_then_cast=mock.Mock(),euler_step=mock.Mock(),MAX_TIME=.024,
             PAIR_COUNT=8,PAIR_BATCH_SIZE=2,WIDTH=8192,SEED_BASE=1,
             OUTPUT_NODES=NS(tolist=lambda:[]),math=__import__('math'),datetime=datetime,timezone=timezone,
             time=NS(monotonic=lambda:0),REFERENCE_NPZ=reference,np=mock.Mock())
    load_functions('studies/stieltjes_proxy_campaign/reference/side_checks/gd_vs_rk4_n8192_point.py',['main'],env)
    try: env['main']()
    except StopBeforeScience: pass
    assert engine.run_point.called and not reference.exists() and not env['np'].load.called
    emit('proxy_missing_reference_late_check',engine_reached=True,reference_exists=False,
         reference_loaded=False,scientific_calls=0)

(PRIVATE/'diagnostic-results.json').write_text(json.dumps(records,indent=2)+'\n')
for record in records: print(json.dumps(record,sort_keys=True))
