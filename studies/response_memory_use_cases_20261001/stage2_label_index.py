"""Final predeclared label-population address candidate; no query labels used."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys
import time
import numpy as np
import torch
from input_field import InputFieldFlow
from stage2_index_experiment import TunedFactors

HERE=Path(__file__).resolve().parent


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def write(path,value):Path(path).write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')


@torch.no_grad()
def make(data,domain,seed,kind,device,width=256):
    x,y=data['X_train'],data['y_train']
    kw=dict(width=width,depth=2,activation='tanh',seed=seed,device=device,
            dtype=torch.float32,hidden_gain=1.,readout_std=1.)
    if kind=='factor':
        model=TunedFactors(x,y,rank=24,factor_seed=seed+10000,
            factor_rate={'fashion':.25,'har':4.,'housing':4.}[domain],**kw)
        model.address_metadata=None
        return model
    labels=np.asarray(y.detach().cpu() if isinstance(y,torch.Tensor) else y)
    if domain=='housing':
        edges=np.quantile(labels,[.25,.5,.75]);group=np.digitize(labels,edges,right=False);count=4
    else:
        assert set(np.unique(labels))=={-1.,1.}
        edges=np.array([0.]);group=(labels>0).astype(int);count=2
    prob=np.bincount(group,minlength=count)/len(labels)
    assert min(prob)>0
    basis=np.eye(count)[group]/np.sqrt(prob)[None,:]
    order=1 if kind=='population_q1' else 24//count
    model=InputFieldFlow(x,y,basis,order=order,**kw)
    error=float((model.basis.T@model.basis/model.M-torch.eye(count,device=device)).abs().max())
    assert error<1e-5,error
    model.address_metadata={'C':count,'q':order,'probabilities':prob.tolist(),'edges':edges.tolist(),
                            'gram_error':error,'group_counts':np.bincount(group,minlength=count).tolist()}
    return model


@torch.no_grad()
def capture_checks(device):
    rng=np.random.default_rng(751)
    x=rng.normal(size=(32,7));x/=np.linalg.norm(x,axis=1,keepdims=True)
    data={'X_train':x,'y_train':np.where(np.arange(32)%2,1.,-1.)}
    errors={}
    for kind in ['population_q1','population_matched','factor']:
        a=make(data,'fashion',751,kind,device,width=32);b=make(data,'fashion',751,kind,device,width=32)
        saved=[v.clone() for v in a.state]
        stream=torch.cuda.Stream(device=device);stream.wait_stream(torch.cuda.current_stream(device))
        with torch.cuda.stream(stream):a.step(1/64)
        torch.cuda.current_stream(device).wait_stream(stream)
        for v,z in zip(a.state,saved):v.copy_(z)
        graph=torch.cuda.CUDAGraph()
        with torch.cuda.graph(graph,stream=stream):
            for _ in range(4):a.step(1/64)
        for v,z in zip(a.state,saved):v.copy_(z)
        graph.replay()
        for _ in range(4):b.step(1/64)
        error=max(float((v-z).abs().max()) for v,z in zip(a.state,b.state))
        assert error<2e-5,error
        errors[kind]=error
    return errors


@torch.no_grad()
def fit(path,seed,kind,dt,device,out):
    started=time.perf_counter();raw=dict(np.load(path))
    data={k:torch.tensor(raw[k],device=device,dtype=torch.float32)
          for k in ['X_train','y_train','X_val','y_val','X_test','y_test']}
    model=make(data,path.stem,seed,kind,device)
    saved=[v.clone() for v in model.state]
    stream=torch.cuda.Stream(device=device);stream.wait_stream(torch.cuda.current_stream(device))
    with torch.cuda.stream(stream):
        for _ in range(2):model.step(dt)
    torch.cuda.current_stream(device).wait_stream(stream)
    for v,z in zip(model.state,saved):v.copy_(z)
    graph=torch.cuda.CUDAGraph();block=32
    with torch.cuda.graph(graph,stream=stream):
        for _ in range(block):model.step(dt)
    for v,z in zip(model.state,saved):v.copy_(z)
    del saved
    checkpoints=[];predictions=[];ticks={round(t/dt) for t in [16,32,64,128]}
    for step in range(block,round(128/dt)+1,block):
        graph.replay()
        if step in ticks:
            cp={'time':step*dt}
            for split in ['train','val','test']:
                pred=model.predict(data['X_'+split])
                cp[split]=float((pred-data['y_'+split]).square().mean().sqrt())
                if split=='test':predictions.append(pred.cpu().numpy())
            checkpoints.append(cp)
    assert all(bool(torch.isfinite(v).all()) for v in model.state)
    selected=min(range(4),key=lambda i:checkpoints[i]['val'])
    result={'domain':path.stem,'seed':seed,'kind':kind,'dt':dt,'width':256,'checkpoints':checkpoints,
        'selected':checkpoints[selected],'selected_index':selected,'seconds':time.perf_counter()-started,
        'data_sha256':sha(path),'addresses':model.address_metadata,'moving_scalars':sum(v.numel() for v in model.state),
        'base_scalars':model.n**2,'cached_basis_scalars':model.basis.numel() if isinstance(model,InputFieldFlow) else 0}
    np.savez_compressed(out/'predictions.npz',predictions=np.stack(predictions),target=raw['y_test'])
    write(out/'result.json',result)
    return result


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--data',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True);parser.add_argument('--device',default='cuda:0')
    args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=False)
    torch.set_num_threads(1);torch.cuda.set_device(args.device)
    torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
    names=['stage2_label_index.py','STAGE2_LABEL_INDEX_PROTOCOL.md','input_field.py',
           'stage2_index_experiment.py','baseline_compact_flow.py']
    for name in names:shutil.copy2(HERE/name,args.out/name)
    write(args.out/'manifest.json',{'sources':{n:sha(HERE/n) for n in names},'command':sys.argv,
        'torch':torch.__version__,'numpy':np.__version__,'device':torch.cuda.get_device_name(),
        'tf32':False,'cpu_threads':1})
    write(args.out/'capture_checks.json',capture_checks(args.device))
    results=[]
    configurations=[(seed,kind,1/64) for seed in [4501,4502,4503,4504]
        for kind in ['population_q1','population_matched','factor']]
    configurations += [(4501,kind,1/128) for kind in ['population_matched','factor']]
    for path in sorted(args.data.glob('*.npz')):
        for seed,kind,dt in configurations:
            folder=args.out/f'fit_{len(results):03d}';folder.mkdir()
            result=fit(path,seed,kind,dt,args.device,folder);results.append(result)
            write(args.out/'results.json',results)
            print(json.dumps({k:result[k] for k in ['domain','seed','kind','dt','selected','seconds']}),flush=True)
    write(args.out/'completion.json',{'fits':len(results),'seconds':sum(r['seconds'] for r in results),'status':'complete'})


if __name__=='__main__':main()
