"""Generate the predeclared six-case ladder and worker configurations."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PYTHON = '/home/amir/miniconda3/bin/python'


def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()


def write_json(p,d):
    with Path(p).open('x') as f: json.dump(d,f,indent=2,allow_nan=False); f.write('\n')


def target(theta,stage):
    a=theta-np.deg2rad(17); b=theta+np.deg2rad(11); c=theta-np.deg2rad(23)
    fs=[np.cos(a),np.cos(3*a),.6*np.cos(3*a)+.4*np.sin(5*a),
        .4*np.cos(3*a)+.35*np.sin(5*a)+.25*np.cos(7*b),
        .2*np.cos(3*a)+.25*np.sin(5*a)+.3*np.cos(7*b)+.25*np.sin(11*c)]
    return fs[stage] if stage<5 else np.sign(fs[4])


def prepare(out):
    out=Path(out).resolve();out.mkdir(parents=True,exist_ok=False)
    for name in ('NETWORK.py','CLOSURE.py','ANALYZE.py','BATCH.py'):
        if not (HERE/name).exists(): raise RuntimeError('Finish source before freeze: '+name)
    train_theta=np.deg2rad((np.array([15,35,50,75,100,170])[:,None]+np.array([-4,-4/3,4/3,4])).ravel())
    circle_theta=np.arange(720)*(2*np.pi/720);dense_theta=np.arange(1440)*(2*np.pi/1440)
    u=lambda t:np.column_stack((np.cos(t),np.sin(t)))
    gap=lambda t:((np.rad2deg(t)>104)&(np.rad2deg(t)<166))|((np.rad2deg(t)>284)&(np.rad2deg(t)<346))
    assert not np.any(gap(train_theta)) and len(np.unique(train_theta))==24
    hashes={}
    for stage in range(6):
        folder=out/f'stage_{stage:02d}';folder.mkdir()
        path=folder/'inputs.npz'
        np.savez(path,train_u=u(train_theta),labels=target(train_theta,stage),probabilities=np.full(24,1/24),
                 train_theta=train_theta,circle_u=u(circle_theta),circle_theta=circle_theta,
                 dense_u=u(dense_theta),dense_theta=dense_theta,gap_mask=gap(circle_theta),
                 gap_dense_mask=gap(dense_theta),target_circle=target(circle_theta,stage),
                 target_dense=target(dense_theta,stage),stage=np.array(stage))
        hashes[str(path.relative_to(out))]=sha(path)
    sources=[HERE/n for n in ('README.md','CAMPAIGN_PLAN.md','PREPARE.py','BATCH.py','NETWORK.py','CLOSURE.py','ANALYZE.py')]
    sources+=list((ROOT/'code/pde').glob('*.py'))
    sources += [ROOT/'docs/NOTATION.md',ROOT/'docs/README.md',ROOT/'code/README.md',ROOT/'AGENTS.md',ROOT/'RESEARCH_WORKFLOW.md']
    manifest=dict(created_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),cwd=str(ROOT),python=PYTHON,
        head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        status=subprocess.check_output(['git','status','--short'],cwd=ROOT,text=True),
        inputs_sha256=hashes,sources_sha256={str(p.relative_to(ROOT)):sha(p) for p in sources},
        budget=dict(scientific_seconds=2700,worker_seconds=1200,output_bytes=6*1024**3,minimum_free_bytes=2*1024**3),
        command=[sys.executable,*sys.argv],numpy=np.__version__)
    write_json(out/'manifest.json',manifest)
    print(json.dumps(dict(campaign=str(out),stages=6,train_points=24)),flush=True)


def jobs(out,stage,profile,pair=None,common_time=None):
    out=Path(out).resolve();folder=out/f'stage_{stage:02d}'
    batch=folder/profile;batch.mkdir(exist_ok=False)
    result=[]
    def add(name,kind,**extra):
        config=dict(id=name,stage=stage,kind=kind,inputs_path=str(folder/'inputs.npz'),
                    h=.02,t_min=100,t_max=600,auto_stop=True,obs_dt=5,**extra)
        if common_time is not None:
            config.update(t_min=common_time,t_max=common_time,auto_stop=False)
        p=batch/(name+'.config.json');write_json(p,config)
        result.append(dict(name=name,kind=kind,config_path=str(p),out=str(batch/name),
                           device=config['device']))
    if profile=='screen':
        for n,device in ((1,'cpu'),(3,'cuda:0'),(5,'cuda:1')):
            add(f'cl_N{n}_screen','closure',order=n,Q=2048,P=1024,device=device)
    elif profile=='confirmation':
        for n in (1,3,5): add(f'cl_N{n}_main','closure',order=n,Q=8192,P=4096,device='cpu' if n==1 else 'cuda:auto')
        for n in pair:
            add(f'cl_N{n}_fine','closure',order=n,Q=16384,P=8192,device='cuda:auto')
            add(f'cl_N{n}_half','closure',order=n,Q=8192,P=4096,device='cuda:auto')
            p=Path(result[-1]['config_path']);c=json.loads(p.read_text());c['h']=.01;p.write_text(json.dumps(c,indent=2)+'\n')
        for seed in (11,29,47): add(f'net_n8192_s{seed}','network',width=8192,seed=seed,dtype='float32',device='cuda:auto')
        add('net_n4096_s11','network',width=4096,seed=11,dtype='float32',device='cuda:auto')
        add('net_n8192_s11_half','network',width=8192,seed=11,dtype='float32',device='cuda:auto')
        p=Path(result[-1]['config_path']);c=json.loads(p.read_text());c['h']=.01;p.write_text(json.dumps(c,indent=2)+'\n')
        add('net_n4096_s11_double','network',width=4096,seed=11,dtype='float64',device='cuda:auto')
    elif profile=='finest':
        for n in pair: add(f'cl_N{n}_finest','closure',order=n,Q=32768,P=16384,device='cuda:auto')
    else: raise ValueError('Unknown profile')
    write_json(batch/'jobs.json',dict(stage=stage,profile=profile,pair=pair,jobs=result))
    print(str(batch/'jobs.json'),flush=True)


def continuation(out,stage,profile,previous,common_time):
    out=Path(out).resolve();folder=out/f'stage_{stage:02d}';batch=folder/profile;batch.mkdir(exist_ok=False)
    previous=json.loads(Path(previous).read_text());result=[]
    for name,path in previous['jobs'].items():
        path=Path(path);r=json.loads((path/'record.json').read_text());config=dict(r['config'])
        if r.get('last_time',r.get('final_time',0))>=common_time: continue
        config.update(t_max=common_time,t_min=common_time,auto_stop=False,device='cuda:auto' if config['kind']=='network' or config['order']>1 else 'cpu')
        p=batch/(name+'.config.json');write_json(p,config)
        checkpoint=path/('state.pt' if config['kind']=='network' else 'final_restart.json')
        result.append(dict(name=name,kind=config['kind'],config_path=str(p),out=str(batch/name),
                           device=config['device'],resume=str(checkpoint)))
    write_json(batch/'jobs.json',dict(stage=stage,profile=profile,common_time=common_time,jobs=result))
    print(str(batch/'jobs.json'),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',required=True);p.add_argument('--stage',type=int)
    p.add_argument('--profile');p.add_argument('--pair',type=int,nargs=2);p.add_argument('--previous');p.add_argument('--time',type=float)
    a=p.parse_args()
    if a.profile and a.previous:continuation(a.out,a.stage,a.profile,a.previous,a.time)
    elif a.profile:jobs(a.out,a.stage,a.profile,a.pair,a.time)
    else:prepare(a.out)
