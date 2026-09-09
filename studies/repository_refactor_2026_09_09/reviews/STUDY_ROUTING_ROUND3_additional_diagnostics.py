"""Additional isolated routing and publication checks; standard library only."""
import ast
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace as NS
from unittest import mock
ROOT=Path('/home/amir/Codes/PDE')
PRIVATE=Path(__file__).parent
records=[]
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def load(relative,names,env):
    path=ROOT/relative
    nodes=[n for n in ast.parse(path.read_text()).body if isinstance(n,ast.FunctionDef) and n.name in names]
    assert {n.name for n in nodes}==set(names)
    future=ast.ImportFrom(module='__future__',names=[ast.alias(name='annotations')],level=0)
    exec(compile(ast.fix_missing_locations(ast.Module(body=[future,*nodes],type_ignores=[])),str(path),'exec'),env)
    return env

with tempfile.TemporaryDirectory(dir=PRIVATE) as temp:
    work=Path(temp)
    summary=work/'generated/stieltjes_proxy_campaign/reference/runs/private/summary.json'
    summary.parent.mkdir(parents=True)
    summary.write_text(json.dumps(dict(config_name='validation_cpu.json',status='private_fixture',points=[])))
    before=digest(summary)
    env=load('studies/stieltjes_proxy_campaign/analysis/reference_data.py',['load_reference_run'],
             dict(Path=Path,json=json,ReferenceRun=NS))
    try: env['load_reference_run'](summary)
    except FileNotFoundError as exc:
        attempted=Path(exc.filename)
        assert attempted==work/'generated/stieltjes_proxy_campaign/reference/configs/validation_cpu.json'
    else: raise AssertionError('unexpected default config resolution')
    config=ROOT/'studies/stieltjes_proxy_campaign/reference/configs/validation_cpu.json'
    result=env['load_reference_run'](summary,config_path=config)
    assert result.config_path==config
    records.append(dict(name='proxy_optional_config_route',attempted=str(attempted.relative_to(work)),
                        correct_source_config=str(config.relative_to(ROOT)),explicit_config_succeeded=True,
                        before=before,after=digest(summary)))

with tempfile.TemporaryDirectory(dir=PRIVATE) as temp:
    repo=Path(temp)/'repo'
    source=repo/'studies/resnet_proof_audit'
    source.mkdir(parents=True)
    input_file=source/'summary.json'
    input_file.write_bytes(b'private protected source fixture\n')
    before=digest(input_file)
    output=repo/'data/generated/resnet_proof_audit/historical_review/processed'
    output.parent.mkdir(parents=True)
    output.symlink_to(source,target_is_directory=True)
    env=load('studies/resnet_proof_audit/source/analyze_results.py',['write_processed','_atomic_write'],
             dict(Path=Path,REPO_ROOT=repo,AnalysisError=RuntimeError,os=os,tempfile=tempfile,_sha256_file=digest))
    env['write_processed'](NS(processed_root=output),
                           {name:b'private processed output\n' for name in ('gates.csv','metrics.csv','archive_inventory.csv','summary.json')})
    after=digest(input_file)
    assert before!=after
    records.append(dict(name='proof_named_output_directory_alias',before=before,after=after,
                        target='private replica of protected studies tree',scientific_calls=0))

with tempfile.TemporaryDirectory(dir=PRIVATE) as temp:
    work=Path(temp)
    retained=work/'retained-input.json'
    retained.write_bytes(b'private historical input fixture\n')
    output=work/'generated/validation_analysis'
    output.mkdir(parents=True)
    os.link(retained,output/'VALIDATION_RESULT.json')
    before=digest(retained)
    env=load('studies/stieltjes_hybrid_campaign/breadth_panel/validation_analysis.py',
             ['write_outputs','_json_bytes'],dict(OUTPUT_ROOT=output,json=json,hashlib=hashlib,
                                                 render_report=lambda *a:'private report fixture'))
    env['write_outputs']({'private_fixture':True})
    after=digest(retained)
    assert after!=before
    records.append(dict(name='hybrid_named_validation_output_hardlink',before=before,after=after,scientific_calls=0))

for filename,var in [('gd_vs_rk4_n4096.py','OUTPUT_JSON'),('gd_vs_rk4_n8192_point.py','output_path')]:
    path=ROOT/'studies/stieltjes_proxy_campaign/reference/side_checks'/filename
    main=next(n for n in ast.parse(path.read_text()).body if isinstance(n,ast.FunctionDef) and n.name=='main')
    statements=[n for n in main.body if isinstance(n,ast.Expr) and isinstance(n.value,ast.Call)
                and ast.unparse(n.value.func) in (var+'.parent.mkdir',var+'.write_text')]
    assert len(statements)==2
    with tempfile.TemporaryDirectory(dir=PRIVATE) as temp:
        work=Path(temp)
        retained=work/'own-reference.npz'
        retained.write_bytes(b'private reference input fixture\n')
        output=work/'generated-result.json'
        os.link(retained,output)
        before=digest(retained)
        exec(compile(ast.Module(body=statements,type_ignores=[]),str(path),'exec'),
             {var:output,'payload':{'private_fixture':True},'json':json})
        after=digest(retained)
        assert before!=after
        records.append(dict(name='proxy_named_sidecheck_output_hardlink',file=filename,before=before,after=after,
                            limitation='actual publication statements; scientific body not executed'))

with tempfile.TemporaryDirectory(dir=PRIVATE) as temp:
    repo=Path(temp)/'repo'
    root=repo/'data/historical/studies/stieltjes_hybrid_campaign/breadth_panel/fp64_successor/runs/local_v1'
    output=root/'A'
    output.mkdir(parents=True)
    ledger=root/'ATTEMPTS.json'
    attempt=output/'ATTEMPT.json'
    provenance={'fixture_binding':'inert; no real authority'}
    record=dict(status='reserved',device='cuda:0',watchdog_timeout_seconds=1,**provenance)
    ledger.write_text(json.dumps(dict(provenance=provenance,attempts={'A':dict(record)},stage_gpu_seconds_ceiling=10)))
    attempt.write_text(json.dumps(record))
    guard=mock.Mock(side_effect=RuntimeError('archive-only FP64 runtime'))
    env=load('studies/stieltjes_hybrid_campaign/breadth_panel/fp64_successor/run_local_qualification.py',
             ['read_json','write_json','write_json_atomic','utc_now','format_seconds','claim_canonical_attempt','finish_canonical_attempt'],
             dict(Path=Path,os=os,json=json,fcntl=fcntl,datetime=datetime,timezone=timezone,
                  STAGE_RESULT_RELATIVE=Path('source/terminal-result'),require_current_authorization=guard))
    before=digest(ledger)
    with mock.patch.dict(os.environ,{'FP64_WATCHDOG_ACTIVE':'group:A:1'}):
        env['claim_canonical_attempt'](repo,{'run_root':str(root.relative_to(repo))},'A','cuda:0',provenance)
    claimed=digest(ledger)
    env['finish_canonical_attempt'](ledger,'A',{'status':'failed','gpu_seconds':7})
    finished=digest(ledger)
    assert before!=claimed!=finished and not guard.called
    records.append(dict(name='archive_only_callable_ledger_mutators',before=before,after_claim=claimed,after_finish=finished,
                        archive_guard_calls=guard.call_count,fixture_states=['reserved','running','failed'],
                        limitation='only private synthetic ledger; no actual historical state inspected or modified'))

(PRIVATE/'additional-results.json').write_text(json.dumps(records,indent=2)+'\n')
for record in records: print(json.dumps(record,sort_keys=True))
