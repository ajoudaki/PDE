import argparse
import ast
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace as NS
from unittest import mock

ROOT=Path('/home/amir/Codes/PDE')
PRIVATE=Path(__file__).parent
sys.path.insert(0,str(ROOT))
from studies._output_paths import StudyPaths
from studies.resnet_generalization.generalization_paths import require_output
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def array(value=None):
    result=mock.MagicMock()
    result.tolist.return_value=[] if value is None else value
    result.__getitem__.return_value.tolist.return_value=[]
    result.shape=(3,3)
    result.size=3
    return result
def compile_functions(source, names, env):
    nodes=[n for n in ast.parse(source.read_text()).body if isinstance(n,ast.FunctionDef) and n.name in names]
    future=ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future,*nodes],type_ignores=[])),str(source),'exec'),env)

records=[]
for relative in ('studies/resnet_generalization/run_exact_reference.py',
                 'studies/resnet_activation_controls/source/run_exact_reference.py'):
    for overlap in ('final','partial'):
        with tempfile.TemporaryDirectory(dir=PRIVATE) as temp:
            work=Path(temp)
            source=ROOT/relative
            seed_input=work/'input-record.json'
            seed_input.write_text('{"dynamics_sha256":"inert private input; no seal authorization"}\n')
            before=digest(seed_input)
            np=NS(eye=lambda _:array(),array=array,stack=lambda _:array(),
                  mean=lambda *a,**kw:array(),std=lambda *a,**kw:array(),
                  sqrt=lambda _:1,max=lambda *a,**kw:0,linalg=NS(norm=lambda *a,**kw:array()),
                  savez_compressed=lambda handle,**kw:handle.write(b'private raw output; no arrays\n'))
            seed=mock.Mock(side_effect=lambda p:dict(seed=p['seed'],times=[],f=[],grams=[],theta=[]))
            env=dict(Path=Path,hashlib=hashlib,json=json,os=os,np=np,time=NS(perf_counter=lambda:0),
                     require_output=require_output,GENERATED_ROOT=work/'generated',
                     PATHS=StudyPaths(source),_one_seed=seed)
            compile_functions(source,['run','_file_sha256'],env)
            args=NS(output_dir=work/'output',pde_seal=seed_input,case_id=None,activation=None,
                    sigma_w=None,A=None,gamma=None,n=1,depth=1,seeds=2,seed_start=1,
                    workers=1,duration=0.0,dt=1.0,sample_dt=1.0)
            with contextlib.redirect_stdout(io.StringIO()): output=env['run'](args)
            output.rename(work/'previous-private-output')
            target=output if overlap=='final' else output.with_suffix('.npz.partial')
            seed_input.rename(target)
            args.pde_seal=target
            outcome='returned'
            with contextlib.redirect_stdout(io.StringIO()):
                try: env['run'](args)
                except FileExistsError: outcome='FileExistsError'
            observed=target if target.exists() else output
            after=digest(observed)
            expected_safe=relative.startswith('studies/resnet_generalization/') and overlap=='partial'
            assert (after==before)==expected_safe
            records.append(dict(file=relative,overlap=overlap,outcome=outcome,before=before,after=after,
                                original_input_exists=target.exists(),scientific_calls=0,
                                diagnostic='full actual run function; mocked numeric operations and seed worker'))
(PRIVATE/'exact-input-results.json').write_text(json.dumps(records,indent=2)+'\n')
for record in records: print(json.dumps(record,sort_keys=True))
