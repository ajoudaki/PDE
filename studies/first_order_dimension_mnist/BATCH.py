"""Small declared waves, one experiment at a time on each GPU."""
from concurrent.futures import ThreadPoolExecutor
import argparse
import json
from pathlib import Path
import subprocess
import sys
import time
import numpy as np

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]/'data/generated/first_order_dimension_mnist'

def execute(jobs,gpu):
    outcomes=[]
    for opts in jobs:
        output=opts['output'];log=BASE/(output.replace('/','__')+'.log')
        cmd=[sys.executable,'-B',str(HERE/'RUN.py'),'--gpu',str(gpu),'--block','2048']
        for key,value in opts.items():
            cmd.append('--'+key.replace('_','-'))
            if value is not True: cmd.append(str(value))
        started=time.perf_counter()
        with log.open('x') as f:
            child=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,timeout=900)
        result={'output':output,'returncode':child.returncode,'seconds':time.perf_counter()-started,'log':str(log)}
        outcomes.append(result);print(json.dumps(result),flush=True)
        if child.returncode: raise RuntimeError('run failed: '+str(log))
    return outcomes

def pilot_report(refined=False):
    report={}
    for model in ('network','closure'):
        def get(dtype,h):
            path=BASE/f'pilot_wave/{model}_{dtype}_h{h}'
            return np.load(path/'observations.npz')['val_predictions'][-1]
        half=get('float64','0.125' if refined else '0.25');full=get('float64','0.25' if refined else '0.5');single=get('float32','0.25' if refined else '0.5')
        timestep=float(np.sqrt(np.mean((full-half)**2)));roundoff=float(np.sqrt(np.mean((single-full)**2)))
        base_step=.25 if refined else .5
        report[model]={'timestep_rms':timestep,'float32_rms':roundoff,'step':base_step if timestep<=.002 else base_step/2,
                       'precision_pass':roundoff<=1e-4,'float64_halfstep_reference':True}
    (BASE/('pilot_summary_refined.json' if refined else 'pilot_summary.json')).write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report),flush=True)
    if not all(r['precision_pass'] for r in report.values()):raise RuntimeError('float32 pilot gate failed')

def main():
    p=argparse.ArgumentParser();p.add_argument('wave',choices=['pilot','pilot_refine','toy','main','controls','reproduction','wider','speed4096','full4096','controls4096'])
    p.add_argument('--control-model',choices=['network','closure']);p.add_argument('--control-gpu',type=int,choices=[0,1]);args=p.parse_args()
    assert args.control_gpu is None or (args.wave=='controls4096' and args.control_model is not None)
    groups=[[],[]]
    if args.wave=='pilot':
        for gpu,model in enumerate(('network','closure')):
            for dtype,step in [('float64',.25),('float64',.5),('float32',.5)]:
                groups[gpu].append(dict(task='pilot',model=model,width=512,dtype=dtype,step=step,horizon=20,
                                        max_seconds=120,output=f'pilot_wave/{model}_{dtype}_h{step}'))
    elif args.wave=='pilot_refine':
        for gpu,model in enumerate(('network','closure')):
            for dtype,step in [('float64',.125),('float32',.25)]:
                groups[gpu].append(dict(task='pilot',model=model,width=512,dtype=dtype,step=step,horizon=20,
                                        max_seconds=120,output=f'pilot_wave/{model}_{dtype}_h{step}'))
    elif args.wave=='toy':
        for gpu,model in enumerate(('network','closure')):
            for seed in (1729,2718):
                groups[gpu].append(dict(task='toy',model=model,width=1024,dtype='float32',step=.25,horizon=100,
                                        seed=seed,max_seconds=120,output=f'toy/{model}_{seed}'))
            for dtype,step in [('float64',.25),('float32',.125)]:
                groups[gpu].append(dict(task='toy',model=model,width=1024,dtype=dtype,step=step,horizon=100,
                                        seed=1729,max_seconds=120,output=f'toy_controls/{model}_{dtype}_h{step}'))
    elif args.wave=='main':
        selected=json.loads((BASE/'pilot_gate_final.json').read_text())
        assert all(row['step_gate_pass'] and row['precision_pass'] for row in selected.values())
        for gpu,model in enumerate(('network','closure')):
            for seed in (1729,2718,3141):
                opts=dict(task='mnist',model=model,width=2048,dtype='float32',step=selected[model]['step'],horizon=200,
                          seed=seed,continue_validation=True,max_seconds=240,output=f'main/{model}_{seed}')
                if seed==1729: opts['precision_probe']=True
                groups[gpu].append(opts)
    elif args.wave=='controls':
        selected=json.loads((BASE/'pilot_gate_final.json').read_text())
        for gpu,model in enumerate(('network','closure')):
            prior=json.loads((BASE/f'main/{model}_1729/summary.json').read_text())
            groups[gpu].append(dict(task='mnist',model=model,width=2048,dtype='float32',step=selected[model]['step']/2,horizon=prior['final_time'],
                                    seed=1729,max_seconds=480,output=f'main_controls/{model}_halfstep'))
    elif args.wave=='reproduction':
        selected=json.loads((BASE/'pilot_gate_final.json').read_text())
        for gpu,model in enumerate(('network','closure')):
            groups[gpu].append(dict(task='mnist',model=model,width=2048,dtype='float32',step=selected[model]['step'],horizon=200,
                                    seed=1729,continue_validation=True,max_seconds=240,output=f'reproduction/{model}_1729'))
    elif args.wave=='full4096':
        selected=json.loads((BASE/'pilot_gate_final.json').read_text())
        assert all(row['step_gate_pass'] and row['precision_pass'] for row in selected.values())
        # The two-card speed check found GPU1 faster; assign it the denser network.
        for model,gpu in (('network',1),('closure',0)):
            for seed in (1729,2718,3141):
                opts=dict(task='mnist',model=model,width=4096,dtype='float32',step=selected[model]['step'],horizon=200,
                          seed=seed,continue_validation=True,max_seconds=600,output=f'main4096/{model}_{seed}')
                if seed==1729:opts['precision_probe']=True
                groups[gpu].append(opts)
    elif args.wave=='controls4096':
        selected=json.loads((BASE/'pilot_gate_final.json').read_text())
        for model,gpu in (('network',1),('closure',0)):
            if args.control_model is not None and args.control_model!=model:continue
            if args.control_gpu is not None:gpu=args.control_gpu
            prior=json.loads((BASE/f'main4096/{model}_1729/summary.json').read_text())
            groups[gpu].append(dict(task='mnist',model=model,width=4096,dtype='float32',step=selected[model]['step']/2,
                                   horizon=prior['final_time'],seed=1729,max_seconds=850,output=f'controls4096/{model}_halfstep'))
    elif args.wave=='speed4096':
        selected=json.loads((BASE/'pilot_gate_final.json').read_text())
        assert all(row['step_gate_pass'] and row['precision_pass'] for row in selected.values())
        for repetition in (1,2):
            widths=(2048,4096) if repetition==1 else (4096,2048)
            for model_index,model in enumerate(('network','closure')):
                gpu=model_index if repetition==1 else 1-model_index
                for width in widths:
                    groups[gpu].append(dict(task='mnist',model=model,width=width,dtype='float32',
                        step=selected[model]['step'],horizon=100,seed=1729,max_seconds=120,
                        output=f'speed4096/{model}_{width}_r{repetition}'))
    elif args.wave=='wider':
        selected=json.loads((BASE/'pilot_gate_final.json').read_text())
        for gpu,model in enumerate(('network','closure')):
            prior=json.loads((BASE/f'main/{model}_1729/summary.json').read_text())
            groups[gpu].append(dict(task='mnist',model=model,width=4096,dtype='float32',step=selected[model]['step'],horizon=prior['final_time'],
                                    seed=1729,max_seconds=480,output=f'width4096/{model}_1729'))
    with ThreadPoolExecutor(max_workers=2) as pool:
        futures=[pool.submit(execute,jobs,gpu) for gpu,jobs in enumerate(groups)]
        result=[future.result() for future in futures]
    record_name=args.wave+('_'+args.control_model if args.wave=='controls4096' and args.control_model else '')+'_execution.json'
    with (BASE/record_name).open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    if args.wave=='pilot':pilot_report()
    if args.wave=='pilot_refine':pilot_report(refined=True)

if __name__=='__main__':main()
