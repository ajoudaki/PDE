"""Bounded staged scaling runs; unchanged vector field and trajectory integrator."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

from benchmark import ROOT, NetworkEngine, setup, save_json, source_hashes, torch, np
from diverse_benchmark import trajectory, THRESHOLD, MAX_TIME, MAX_STEPS, SNAPSHOTS
from scaling_dictionary import build, dictionary_metadata
from scaling_cases import DISCOVERY, CONFIRMATION, SEEDS


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--group',choices=('discovery','confirm1','confirm2','width'),required=True)
    p.add_argument('--stage',choices=('A','B','C','D','extra'),required=True)
    p.add_argument('--orders',type=int,nargs='+',required=True)
    p.add_argument('--all-orders',type=int,nargs='+')
    p.add_argument('--include-full',action='store_true')
    p.add_argument('--cases',nargs='+')
    p.add_argument('--only-cells',nargs='+')
    p.add_argument('--worker',type=int,choices=(0,1),required=True)
    p.add_argument('--workers',type=int,choices=(1,2),default=2)
    p.add_argument('--device',required=True)
    p.add_argument('--level',type=int,choices=(0,1,2),default=0)
    p.add_argument('--budget',type=float,default=400.)
    args=p.parse_args()
    if not 0<args.budget<=600 or args.worker>=args.workers:
        raise ValueError('worker index or reserved budget invalid')
    if args.level==2 and args.stage!='extra':
        raise ValueError('third tolerance reserved for declared numerical branch')
    seed_index=int(args.group[-1]) if args.group.startswith('confirm') else 0
    cases=CONFIRMATION[seed_index] if seed_index else DISCOVERY
    if args.cases:
        if any(c not in cases for c in args.cases):
            raise ValueError('unknown predeclared case')
        cases={c:cases[c] for c in args.cases}
    width=4096 if args.group=='width' else 2048
    if args.group=='width' and len(cases)!=1:
        raise ValueError('width branch requires one selected original case')
    network_seed,dictionary_seed=SEEDS[seed_index]
    planned=args.all_orders or args.orders
    if len(set(planned))!=len(planned) or not set(args.orders)<=set(planned):
        raise ValueError('invalid planned/actual orders')
    rtol,atol=6.25e-5/4**args.level,6.25e-7/4**args.level
    device=setup(args.device)
    args.out.mkdir(parents=True,exist_ok=True)
    suffix=f'{args.stage}_worker{args.worker}'
    cp=args.out/f'config_{suffix}.json'
    if cp.exists():
        raise FileExistsError(cp)
    names=(['full'] if args.include_full else [])+[f'{method}_p{order}' for order in args.orders for method in ('ours','gaussian','orthogonal')]
    all_cells=[f'{c}_{m}' for i,c in enumerate(cases) if i%args.workers==args.worker for m in names]
    if args.only_cells:
        if not set(args.only_cells)<=set(all_cells):
            raise ValueError('extra branch selects a cell outside this worker/method scope')
        all_cells=[key for key in all_cells if key in args.only_cells]
    for key in all_cells:
        if (args.out/key).exists():
            raise FileExistsError(args.out/key)
    config=dict(group=args.group,stage=args.stage,cases=cases,orders=planned,
        orders_executed=args.orders,include_full=args.include_full,selected_cells=all_cells,
        width=width,network_seed=network_seed,dictionary_seed=dictionary_seed,
        threshold=THRESHOLD,dtype='float64',rtol=rtol,atol=atol,step=.05,max_step=2.,
        max_time=MAX_TIME,max_steps=MAX_STEPS,snapshot_times=SNAPSHOTS,
        circle_nodes=2048,endpoint_nodes=8192,worker=args.worker,workers=args.workers,
        worker_limit_seconds=args.budget,per_trajectory_limit_seconds=180,
        training_run=True,device=device,gpu=torch.cuda.get_device_name(device),
        torch=str(torch.__version__),numpy=np.__version__,python=sys.version,
        command=sys.argv,cwd=str(Path.cwd()),source_hashes=source_hashes(),
        protocol_sha256=hashlib.sha256(Path(__file__).with_name('SCALING_PROTOCOL.md').read_bytes()).hexdigest(),
        head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
        target_accuracies=[1.,.5,.3,.2,.1,.05,.02,.01])
    save_json(cp,config)
    start=time.monotonic()
    net=NetworkEngine(2,width,network_seed,device=device,dtype=torch.float64,block_size=256)
    initial=net.initial_state()
    engines={'full':(net,initial)}
    results={}
    def record_unrun(index):
        for pending in all_cells[index:]:
            directory=args.out/pending;directory.mkdir()
            results[pending]=dict(status='not_run_budget',loss=None,time=None,seconds=0,
                reason='Worker allocation exhausted before trajectory start',rtol=rtol,atol=atol)
            save_json(directory/'summary.json',results[pending])
        save_json(args.out/f'results_{suffix}.json',results)

    for index,key in enumerate(all_cells):
        if time.monotonic()-start>=args.budget:
            record_unrun(index)
            break
        case=next(c for c in cases if key.startswith(c+'_') and key[len(c)+1:] in names)
        name=key[len(case)+1:]
        if name not in engines:
            method,order=name.rsplit('_p',1)
            try:
                engine,state=build(initial,int(order),method,dictionary_seed=dictionary_seed)
                meta=dictionary_metadata(initial,int(order),method,dictionary_seed=dictionary_seed,bases=(engine.b1,engine.b2))
                save_json(args.out/f'dictionary_{suffix}_{name}.json',meta)
                populations=meta['populations']
                if any(v['ridge_condition'] is not None and v['ridge_condition']>1e10 for v in populations):
                    raise ValueError('regularized Gram condition exceeds1e10')
                if method=='orthogonal' and any(max(abs(e-1.) for e in v['normalized_gram_eigenvalues'])>1e-8 for v in populations):
                    raise ValueError('orthogonal Gram residual exceeds1e-8')
                if method=='ours' and any(v['triangular_solve_residual']>1e-8 for v in populations):
                    raise ValueError('triangular solve residual exceeds1e-8')
                engines[name]=(engine,state)
            except (ValueError,RuntimeError) as exc:
                directory=args.out/key;directory.mkdir()
                results[key]=dict(status='initialization_failure',loss=None,time=None,seconds=0,
                                  reason=f'{type(exc).__name__}: {exc}',rtol=rtol,atol=atol)
                save_json(directory/'summary.json',results[key])
                save_json(args.out/f'results_{suffix}.json',results)
                print(json.dumps(dict(completed=key,**results[key])),flush=True)
                continue
        if time.monotonic()-start>=args.budget:
            record_unrun(index)
            break
        engine,state=engines[name]
        results[key]=trajectory(engine,state,cases[case],args.out/key,rtol,atol,start,args.budget)
        save_json(args.out/f'results_{suffix}.json',results)
    torch.cuda.synchronize(device)
    completion=dict(exit_status=0,training_run=True,seconds=time.monotonic()-start,
        fitted=sum(v['status']=='fitted' for v in results.values()),total=len(results),
        planned_cells=all_cells,finished_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
    save_json(args.out/f'completion_{suffix}.json',completion)
    print(json.dumps(completion),flush=True)


if __name__=='__main__':
    main()
