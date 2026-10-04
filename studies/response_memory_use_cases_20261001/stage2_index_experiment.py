"""Frozen multi-domain shared-index campaign. No persistent observation slots."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import shutil
import sys
import time
import numpy as np
import torch
from baseline_compact_flow import Flow, LowRankFlow
from input_field import InputFieldFlow, internal_matrix

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False))


@torch.no_grad()
def pca(h, count):
    """h has neuron x observation shape; return orthonormal input functions."""
    hd = h.double()
    values, vectors = torch.linalg.eigh(hd @ hd.T / h.shape[1])
    values = values[-count:].flip(0)
    vectors = vectors[:, -count:].flip(1)
    if not bool((values[-1] > values[0]*1e-8).item()):
        raise ValueError('declared PCA rank failed cutoff')
    basis = (hd.T @ vectors) / values.sqrt()
    error = float((basis.T @ basis / h.shape[1] - torch.eye(count, device=h.device)).abs().max())
    if error > 1e-10:
        raise ValueError(f'PCA orthonormality failed {error}')
    return basis.to(h.dtype), vectors.to(h.dtype), values.to(h.dtype), error


class TunedFactors(LowRankFlow):
    def __init__(self, *args, factor_rate=1., **kw):
        super().__init__(*args, **kw)
        self.c.zero_()
        self.factor_rate = factor_rate

    def rhs(self):
        values = super().rhs()
        return [*values[:2], *(v*self.factor_rate for v in values[2:])]


class Projected(Flow):
    def __init__(self, *args, rank=24, **kw):
        super().__init__(*args, order=None, **kw)
        self.c.zero_()
        h = self._forward(self.inputs, None)[0][0]
        _, self.V, _, self.ortho_error = pca(h, rank)
        self.A = self.w.new_zeros((self.n, rank))
        self.state = [self.w, self.c, self.A]

    def _factors(self):
        return [(self.A, self.V)]

    def rhs(self):
        hidden, backward, residual, _ = self._loss_fields()
        self.loss = residual.square().mean()
        return [(-2/self.M)*backward[0]@self.inputs,
                (-2/self.M)*hidden[-1]@residual,
                (-2/(self.M*self.n))*backward[1]@(self.V.T@hidden[0]).T]


@torch.no_grad()
def make(config, data, device, dtype=torch.float32):
    x, y = data['X_train'], data['y_train']
    kw = dict(width=128, depth=2, activation='tanh', seed=config['seed'],
              hidden_gain=1., readout_std=1., device=device, dtype=dtype)
    kind = config['kind']
    if kind == 'factor':
        return TunedFactors(x, y, rank=24, factor_seed=config['seed']+10000,
                            factor_rate=config['rate'], **kw)
    if kind == 'projected':
        return Projected(x, y, rank=24, **kw)
    initial = Flow(x, y, order=None, **kw)
    initial.c.zero_()
    if kind == 'dense':
        return initial
    h = initial._forward(initial.inputs, None)[0][0]
    basis, vectors, values, error = pca(h, config['C'])
    model = InputFieldFlow(x, y, basis, order=config['q'], **kw)
    model.dictionary_first = model.w.clone()
    model.dictionary_vectors = vectors
    model.dictionary_values = values
    model.ortho_error = error
    return model


@torch.no_grad()
def refresh_info(model, apply=None, observer=None):
    h = model._forward(model.inputs, model._factors())[0][0]
    new_basis, vectors, values, error = pca(h, model.C)
    overlap = model.basis.T @ new_basis / model.M
    u, singular, vh = torch.linalg.svd(overlap.double())
    # min ||new_basis R-old_basis||: R=V U^T for old^T new=U S V^T.
    rotation = (vh.T @ u.T).to(h.dtype)
    new_basis = new_basis @ rotation
    overlap = model.basis.T @ new_basis / model.M
    drift = float((1-singular.square()).clamp_min(0).mean().sqrt())
    result = dict(drift=drift, singular_values=singular.cpu().tolist(),
                  new_orthonormality_error=error)
    if observer is not None:
        old_errors = []
        projected = []
        exact = []
        for field, obs in zip(model.moments, observer):
            old = obs @ model.basis / model.M
            old_errors.append(float((old-field).abs().max()))
            projected.append(field @ overlap)
            exact.append(obs @ new_basis / model.M)
        result['observer_old_parity'] = max(old_errors)
        result['transport_relative_error'] = [float((a-b).norm()/b.norm().clamp_min(1e-12))
                                               for a,b in zip(projected,exact)]
        def reconstruction(moments):
            a,b = moments
            return (-2/(model.n*(1+model.s))) * torch.einsum('jic,jkc,j->ik',a,b,model.weights[:,0,0])
        e,p = reconstruction(exact), reconstruction(projected)
        result['transport_matrix_relative_error'] = float((e-p).norm()/e.norm().clamp_min(1e-12))
    if apply is not None:
        if apply == 'retro':
            for value in model.moments:
                value.copy_(value @ overlap)
        elif apply != 'write':
            raise ValueError(apply)
        model.basis.copy_(new_basis)
        model.dictionary_first.copy_(model.w)
        # The evaluable whitened feature map includes the alignment rotation.
        model.dictionary_vectors = vectors
        model.dictionary_values = values
        model.dictionary_rotation = rotation
    return result


@torch.no_grad()
def sanity(device):
    rng = np.random.default_rng(773)
    x = rng.normal(size=(16,5)); x /= np.linalg.norm(x,axis=1,keepdims=True)
    data = dict(X_train=x,y_train=rng.normal(size=16))
    result = {}
    for config in [dict(kind='dense'),dict(kind='factor',rate=4.),
                   dict(kind='projected'),dict(kind='field',C=8,q=3)]:
        # The projected rank24 requires at least24 observations.
        if config['kind']=='projected':
            dx = np.concatenate([x, rng.normal(size=(16,5))]);dx/=np.linalg.norm(dx,axis=1,keepdims=True)
            dat = dict(X_train=dx,y_train=np.tile(data['y_train'],2))
        else: dat=data
        config['seed']=773
        a=make(config,dat,device); b=make(config,dat,device)
        saved=[v.clone() for v in a.state]
        stream=torch.cuda.Stream(device=device);stream.wait_stream(torch.cuda.current_stream(device))
        with torch.cuda.stream(stream):a.step(1/32)
        torch.cuda.current_stream(device).wait_stream(stream)
        for v,s in zip(a.state,saved):v.copy_(s)
        graph=torch.cuda.CUDAGraph()
        with torch.cuda.graph(graph,stream=stream):
            for _ in range(4):a.step(1/32)
        for v,s in zip(a.state,saved):v.copy_(s)
        graph.replay()
        for _ in range(4):b.step(1/32)
        error=max(float((v-w).abs().max()) for v,w in zip(a.state,b.state))
        if error>2e-5:raise ValueError('capture parity failed')
        result[config['kind']]=error
    return result


@torch.no_grad()
def fit(config, dataset_path, folder, device):
    started=time.perf_counter()
    raw=dict(np.load(dataset_path))
    data={k:torch.tensor(raw[k],device=device,dtype=torch.float32)
          for k in ['X_train','y_train','X_val','y_val','X_test','y_test']}
    model=make(config,data,device)
    hidden0=[v.clone() for v in model._forward(data['X_test'],model._factors())[0]]
    # These optional full sample observers are measurement apparatus only.
    # Their arrays never feed the learner and are excluded from its state count.
    observer=None
    if config.get('observer') and config['kind']=='field':
        h=model._forward(model.inputs,model._factors())[0][0]
        oa=h.new_zeros((model.order,model.n,model.M));ob=torch.zeros_like(oa);ob[0]=h
        observer=[oa,ob]
    dt=config.get('dt',1/32);steps=round(128/dt);block=32
    def step():
        if observer is not None:
            hidden, backward, residual, _=model._loss_fields()
            rho=residual.square().mean().sqrt()
            va=model._transport(observer[0],backward[1],rho)
            vb=model._transport(observer[1],rho*hidden[0],rho)
            model.step(dt)
            observer[0].add_(va,alpha=dt);observer[1].add_(vb,alpha=dt)
        else:model.step(dt)
    states=[*model.state,*(observer or [])]
    backup=[v.clone() for v in states]
    stream=torch.cuda.Stream(device=device);stream.wait_stream(torch.cuda.current_stream(device))
    with torch.cuda.stream(stream):
        for _ in range(2):step()
    torch.cuda.current_stream(device).wait_stream(stream)
    for v,s in zip(states,backup):v.copy_(s)
    graph=torch.cuda.CUDAGraph()
    with torch.cuda.graph(graph,stream=stream):
        for _ in range(block):step()
    for v,s in zip(states,backup):v.copy_(s)
    del backup
    checkpoints=[];predictions=[];drift=None;status='complete'
    ticks={round(t/dt) for t in [16,32,64,128]}
    for actual in range(block,steps+1,block):
        graph.replay()
        if actual in ticks:
            train=model.predict(data['X_train']);val=model.predict(data['X_val']);test=model.predict(data['X_test'])
            vals={split:float((pred-data['y_'+split]).square().mean().sqrt())
                  for split,pred in [('train',train),('val',val),('test',test)]}
            checkpoints.append(dict(time=actual*dt,**vals));predictions.append(test.cpu().numpy())
            if not all(math.isfinite(v) for v in vals.values()):status='nonfinite';break
            if actual*dt==64 and config['kind']=='field':
                drift=refresh_info(model,config.get('refresh'),observer)
            if time.perf_counter()-started>90:status='wall_limit';break
    torch.cuda.synchronize(device)
    finite=all(bool(torch.isfinite(v).all()) for v in model.state)
    if not finite:status='nonfinite_state'
    best=min(range(len(checkpoints)),key=lambda k:checkpoints[k]['val'])
    hidden=model._forward(data['X_test'],model._factors())[0]
    moving=sum(v.numel() for v in model.state)
    fixed=0 if config['kind']=='dense' else model.n**2
    dictionary=0
    if config['kind']=='field':dictionary=model.w.numel()+model.n*model.C+model.C
    if config['kind']=='projected':dictionary=model.V.numel()
    if config.get('refresh'):dictionary+=model.C**2
    result=dict(config=config,data_path=str(dataset_path),data_sha256=sha(dataset_path),status=status,
                seconds=time.perf_counter()-started,steps=actual,finite=finite,checkpoints=checkpoints,
                selected=checkpoints[best],selected_index=best,drift=drift,
                moving_scalars=moving,fixed_base_scalars=fixed,dictionary_scalars=dictionary,
                cached_basis_scalars=model.M*model.C if config['kind']=='field' else 0,
                observer_scalars=sum(v.numel() for v in observer or []),
                feature_movement=[float((h-h0).square().mean().sqrt()) for h,h0 in zip(hidden,hidden0)],
                orthonormality_error=getattr(model,'ortho_error',None))
    if not finite:raise ValueError('nonfinite fit; artifacts require manual status handling')
    np.savez_compressed(folder/'predictions.npz',predictions=np.stack(predictions),
                        target=data['y_test'].cpu().numpy(),selected=np.asarray(best))
    write(folder/'result.json',result)
    return result


def main():
    p=argparse.ArgumentParser();p.add_argument('--data',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--stage',choices=['pilot','confirm','refine','adapt'],required=True)
    p.add_argument('--selection',type=Path);p.add_argument('--device',default='cuda:0')
    args=p.parse_args();args.out.mkdir(parents=True,exist_ok=False)
    torch.set_num_threads(1);torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
    torch.cuda.set_device(args.device)
    sources=['stage2_index_experiment.py','input_field.py','baseline_compact_flow.py','STAGE2_INDEX_PROTOCOL.md','STAGE2_INDEX_THEORY.md']
    hashes={}
    for name in sources:
        shutil.copy2(HERE/name,args.out/name);hashes[name]=sha(HERE/name)
    datasets=sorted(args.data.glob('*.npz'))
    if len(datasets)!=3:raise ValueError(f'Expected exactly3 data files, got{datasets}')
    write(args.out/'manifest.json',dict(command=sys.argv,sources=hashes,
          data={p.name:sha(p) for p in datasets},torch=torch.__version__,numpy=np.__version__,
          device=torch.cuda.get_device_name(),cpu_threads=1,tf32=False))
    write(args.out/'capture_checks.json',sanity(args.device))
    selections=json.loads(args.selection.read_text()) if args.selection else {}
    results=[]
    for path in datasets:
        domain=path.stem
        if args.stage=='pilot':
            configs=[dict(kind='field',C=8,q=3,observer=True),dict(kind='field',C=24,q=1,observer=True),
                     *[dict(kind='factor',rate=r) for r in [.25,1.,4.]],dict(kind='projected'),dict(kind='dense')]
            seeds=[101]
        else:
            chosen=selections[domain]
            field={k:v for k,v in chosen['field'].items() if k in ['kind','C','q']}
            factor={k:v for k,v in chosen['factor'].items() if k in ['kind','rate']}
            seeds=[201] if args.stage=='refine' else [201,202,203,204]
            if args.stage=='confirm':configs=[field,factor,dict(kind='projected'),dict(kind='dense')]
            elif args.stage=='refine':configs=[dict(field,dt=1/64),dict(factor,dt=1/64)]
            else:configs=[dict(field,refresh=mode) for mode in ['retro','write']]
        for seed in seeds:
            for config in configs:
                config=dict(config,seed=seed,domain=domain)
                folder=args.out/f'fit_{len(results):03d}';folder.mkdir()
                write(folder/'config.json',config)
                result=fit(config,path,folder,args.device);results.append(result)
                write(args.out/'results.json',results)
                print(json.dumps(dict(config=config,selected=result['selected'],seconds=result['seconds'])),flush=True)
    if args.stage=='pilot':
        selection={}
        for domain in [p.stem for p in datasets]:
            rr=[r for r in results if r['config']['domain']==domain]
            selection[domain]={kind:min((r for r in rr if r['config']['kind']==kind),key=lambda r:r['selected']['val'])['config']
                               for kind in ['field','factor']}
        write(args.out/'selection.json',selection)
    write(args.out/'completion.json',dict(status='complete',fits=len(results),fit_seconds=sum(r['seconds'] for r in results)))


if __name__=='__main__':main()
