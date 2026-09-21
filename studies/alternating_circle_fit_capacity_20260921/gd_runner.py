#!/usr/bin/env python3
"""Execute the frozen GD-only conditional comparison, preserving all attempts."""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

STUDY=Path(__file__).resolve().parent
ROOT=STUDY.parents[1]
SEEDS=(20260921,20260922,20260923)
CAP=2500.0
RESERVATION=85.0


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    tmp=path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(value,indent=2,sort_keys=True,allow_nan=False)+'\n')
    tmp.replace(path)


def execute_job(job):
    out=Path(job['output'])
    config={k:job[k] for k in ('model','width','m','seed','gain','device','eta_max')}
    config['max_seconds']=75.0
    config_path=out.parent/(out.name+'_config.json')
    write_json(config_path,config)
    command=[sys.executable,'-B',str(STUDY/'gd_benchmark.py'),'attempt',
             '--config',str(config_path),'--output',str(out),
             '--freeze',str(STUDY/'GD_PROTOCOL.md')]
    env=os.environ.copy()
    env.update(PYTHONPATH=str(ROOT/'code'),PYTHONDONTWRITEBYTECODE='1',
               OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1')
    start=time.perf_counter()
    with (out.parent/(out.name+'.log')).open('w') as log:
        try:
            p=subprocess.run(command,cwd=ROOT,env=env,stdout=log,
                             stderr=subprocess.STDOUT,timeout=84)
            rc,failure=p.returncode,None
        except subprocess.TimeoutExpired:
            rc,failure=-9,'supervisor_timeout_84s'
    result=dict(job,command=command,cwd=str(ROOT),returncode=rc,
                process_wall_seconds=time.perf_counter()-start,supervisor_failure=failure)
    if (out/'record.json').exists():
        rec=json.loads((out/'record.json').read_text())
        result['summary']=rec
        if 'diagnostics' in rec and 'best' in rec['diagnostics']:
            result['metrics']=dict(rec['diagnostics']['best'],fit=rec['fit'])
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--resume',action='store_true')
    args=parser.parse_args()
    out=args.output.resolve()
    source_paths=(STUDY/'GD_PROTOCOL.md',STUDY/'gd_benchmark.py',STUDY/'fit_benchmark.py')
    if args.resume:
        rec=json.loads((out/'run_record.json').read_text())
        if rec['status']!='stopped_with_error':
            raise RuntimeError('Only a stopped campaign may be resumed')
        for p in source_paths:
            if digest(p)!=rec['source_hashes'][str(p.relative_to(ROOT))]:
                raise RuntimeError('Frozen scientific source changed')
        snap=out/f"interruption_{len(rec.get('resumes',[]))+1:02d}.json"
        write_json(snap,rec)
        rec.setdefault('resumes',[]).append(dict(command=sys.argv,interruption=str(snap),
                                                runner_sha256=digest(__file__)))
        rec['status']='running'
        rec.pop('error',None)
    else:
        out.mkdir(parents=True,exist_ok=False)
        rec=dict(status='running',worker_wall_cap=CAP,spent_worker_seconds=0.,
                 reservations=0.,jobs=[],ladder=[],selected_m=None,candidate_found=False,
                 source_hashes={str(p.relative_to(ROOT)):digest(p) for p in (*source_paths,Path(__file__))},
                 command=sys.argv,cwd=str(ROOT),started_unix_seconds=time.time())
    write_json(out/'run_record.json',rec)

    def valid(job):
        s=job.get('summary',{})
        return (job['returncode']==0 and s.get('numerical_valid') and s.get('budget_respected')
                and s.get('status') in ('fit_reached','step_limit','evaluation_limit',
                                        'physical_clock_limit','time_limit','gradient_floor'))

    def batch(jobs):
        existing={j['output']:j for j in rec['jobs']}
        pending=[]
        for job in jobs:
            if job['output'] in existing:
                old=existing[job['output']]
                if any(old[k]!=job[k] for k in ('model','width','m','seed','gain','eta_max','device','stage')):
                    raise RuntimeError('Resume settings mismatch')
                if not valid(old):
                    raise RuntimeError('Unresolved prior failed attempt; no gate inferred')
            else:
                pending.append(job)
        for begin in range(0,len(pending),2):
            group=pending[begin:begin+2]
            if rec['spent_worker_seconds']+RESERVATION*len(group)>CAP:
                raise BudgetStop('Insufficient remaining allowance for next reserved batch')
            rec['reservations']=RESERVATION*len(group)
            write_json(out/'run_record.json',rec)
            with ThreadPoolExecutor(max_workers=len(group)) as pool:
                results=list(pool.map(execute_job,group))
            rec['reservations']=0.
            for result in results:
                rec['jobs'].append(result)
                existing[result['output']]=result
                rec['spent_worker_seconds']+=result['process_wall_seconds']
                print(json.dumps(dict(attempt=Path(result['output']).name,
                    returncode=result['returncode'],status=result.get('summary',{}).get('status'),
                    **{k:result.get('metrics',{}).get(k) for k in ('fit','mse','sign_errors')})),flush=True)
            write_json(out/'run_record.json',rec)
            if not all(valid(r) for r in results):
                raise RuntimeError('Producer/numerical failure retained; no scientific gate inferred')
        return [existing[j['output']] for j in jobs]

    def group(model,width,m,gain,eta,stage):
        jobs=[]
        for index,seed in enumerate(SEEDS):
            name=f'{stage}_{model}_n{width}_m{m}_{gain}_eta{eta:g}_seed{seed}'
            jobs.append(dict(model=model,width=width,m=m,seed=seed,gain=gain,
                             eta_max=eta,device=f'cuda:{index%2}',stage=stage,output=str(out/name)))
        return batch(jobs)

    def fits(jobs):
        return sum(bool(j['metrics']['fit']) for j in jobs)

    try:
        selected=None
        primary={}
        for m in (30,62,126,254):
            dense=group('network',55,m,'rescue',1.,'ladder')
            closure=group('closure',1024,m,'rescue',1.,'ladder')
            primary[m]={('network',55):dense,('closure',1024):closure}
            gate=dict(m=m,dense55_fits=fits(dense),closure_fits=fits(closure))
            gate['candidate']=gate['dense55_fits']==0 and gate['closure_fits']>=2
            rec['ladder']=[g for g in rec['ladder'] if g['m']!=m]+[gate]
            print(json.dumps(dict(gate=gate)),flush=True)
            write_json(out/'run_record.json',rec)
            if gate['candidate']:
                selected=m
                rec['candidate_found']=True
                break
        selected=selected if selected is not None else 254
        rec['selected_m']=selected
        write_json(out/'run_record.json',rec)
        main=primary[selected]
        main[('network',105)]=group('network',105,selected,'rescue',1.,'size_control')
        fine={}
        for model,width in (('network',55),('closure',1024),('network',105)):
            fine[(model,width)]=group(model,width,selected,'rescue',.5,'step_sensitivity')
        rec['sensitivity']={str(width):dict(primary_fits=fits(main[(model,width)]),
            finer_cap_fits=fits(fine[(model,width)])) for model,width in main}
        rec['width55_separation_both_caps']=all(fits(g[('closure',1024)])>=2
            and fits(g[('network',55)])==0 for g in (main,fine))
        rec['width105_separation_both_caps']=all(fits(g[('closure',1024)])>=2
            and fits(g[('network',105)])==0 for g in (main,fine))
        write_json(out/'run_record.json',rec)
        for model,width in (('network',55),('closure',1024),('network',105)):
            group(model,width,selected,'primary',1.,'canonical_control')
        for groups in (main,fine):
            for model,width in (('network',55),('closure',1024),('network',105)):
                jobs=groups[(model,width)]
                succeeded=[j for j in jobs if j['metrics']['fit']]
                original=min(succeeded or jobs,key=lambda j:j['seed'])
                repeat={k:original[k] for k in ('model','width','m','seed','gain','eta_max','device')}
                repeat.update(stage='reproduction',original_output=original['output'],
                              output=str(out/('reproduction_'+Path(original['output']).name)))
                again=batch([repeat])[0]
                comp=dict(original_output=original['output'],reproduction_output=again['output'],
                          mse_difference=abs(original['summary']['diagnostics']['final']['mse']
                                             -again['summary']['diagnostics']['final']['mse']),
                          best_mse_difference=abs(original['metrics']['mse']-again['metrics']['mse']),
                          same_fit=original['metrics']['fit']==again['metrics']['fit'])
                comp['passed']=comp['same_fit'] and comp['mse_difference']<=1e-6
                counts=[j['summary']['accepted_steps'] for j in (original,again)]
                comp['accepted_steps']=counts
                comp['time_censored']=(counts[0]!=counts[1] and any(
                    j['summary']['status']=='time_limit' for j in (original,again)))
                if comp['time_censored']:
                    traces=[[json.loads(line) for line in
                             (Path(j['output'])/'trace.jsonl').read_text().splitlines()]
                            for j in (original,again)]
                    prefix=list(zip(*traces))
                    comp['shared_prefix']=dict(accepted_states=len(prefix),
                        maximum_mse_difference=max(abs(a['mse']-b['mse']) for a,b in prefix),
                        same_step_sequence=all(a.get('eta')==b.get('eta') for a,b in prefix))
                comp['classification']=('endpoint_pass' if comp['passed'] else
                    'time_censored' if comp['time_censored'] else 'unstable')
                rec['reproductions']=[r for r in rec.get('reproductions',[])
                    if r['original_output']!=comp['original_output']]+[comp]
                write_json(out/'run_record.json',rec)
        rec['status']='complete'
    except BudgetStop as exc:
        rec.update(status='budget_limited',error=str(exc))
    except Exception as exc:
        rec.update(status='stopped_with_error',error=repr(exc))
        raise
    finally:
        rec['reservations']=0.
        rec['finished_unix_seconds']=time.time()
        write_json(out/'run_record.json',rec)


class BudgetStop(Exception):
    pass


if __name__=='__main__':
    main()
