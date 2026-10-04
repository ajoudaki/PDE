"""Derived physical-velocity certificate and explicitly modified gated flow."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys
import time

import numpy as np
import torch

from baseline_compact_flow import Flow
from input_field import InputFieldFlow
from stage2_index_experiment import TunedFactors, pca

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


class CertifiedField(InputFieldFlow):
    def __init__(self, *args, gated=False, **kwargs):
        super().__init__(*args, **kwargs)
        assert self.depth == 2
        self.gated = gated
        self.kappa = .001 * self.labels.square().mean()
        # The theorem requires kappa>0. Zero labels give an already-fitted
        # zero-readout initialization; use a positive fallback to avoid 0/0.
        self.kappa = torch.where(self.kappa > 0, self.kappa, torch.ones_like(self.kappa))

    @torch.no_grad()
    def fields_and_velocity(self):
        hidden, backward, residual, _ = self._loss_fields()
        loss = residual.square().mean()
        rho = loss.sqrt()
        outer = [(-2/self.M) * backward[0] @ self.inputs,
                 (-2/self.M) * hidden[-1] @ residual]
        R = backward[1] @ self.basis / self.M
        H = hidden[0] @ self.basis / self.M
        A, B = self.moments
        tau = 1 + self.s
        hstar = (self.weights * B).sum(0) / tau
        bstar = (self.weights * A).sum(0) / tau
        Vh = (-2/self.n) * (R @ (hstar.T @ hidden[0]) + rho * bstar @ ((H-hstar).T @ hidden[0]))
        S = (2/(self.n*self.M)) * (backward[1] * Vh).sum()
        D = sum(v.square().sum() for v in outer) / self.n
        gamma = (-S/self.kappa).clamp(0, 1) if self.gated else torch.ones_like(S)
        va = self._transport(A, R, rho)
        vb = self._transport(B, rho*H, rho)
        velocity = [*outer, gamma*va, gamma*vb, gamma*rho]
        projected_Vh = (-2/self.n) * R @ (H.T @ hidden[0])
        projected_S = (2/(self.n*self.M)) * (backward[1]*projected_Vh).sum()
        lag_Vh = (-2/self.n) * (R-rho*bstar) @ ((hstar-H).T @ hidden[0])
        lag_S = (2/(self.n*self.M)) * (backward[1]*lag_Vh).sum()
        Z=self.basis/(self.M**.5)
        AZ=hidden[0].T@(hidden[0]@Z)/self.M
        off_diagonal=AZ-Z@(Z.T@AZ)
        commutator_relative=torch.linalg.matrix_norm(off_diagonal,ord=2)/torch.linalg.matrix_norm(AZ,ord=2).clamp_min(1e-12)
        metrics = torch.stack([loss, D, S, gamma, -D+S, -D+gamma*S,
                               projected_S,lag_S,S-projected_S-lag_S,commutator_relative])
        V = (-2/self.n) * (R @ hstar.T + rho * bstar @ (H-hstar).T)
        return velocity, metrics, V

    @torch.no_grad()
    def rhs(self):
        # Do not construct a dense V inside the learner: only low-rank actions.
        hidden, backward, residual, _ = self._loss_fields()
        self.loss = residual.square().mean()
        rho = self.loss.sqrt()
        outer = [(-2/self.M)*backward[0]@self.inputs,
                 (-2/self.M)*hidden[-1]@residual]
        R = backward[1] @ self.basis / self.M
        H = hidden[0] @ self.basis / self.M
        A, B = self.moments
        hstar = (self.weights*B).sum(0)/(1+self.s)
        bstar = (self.weights*A).sum(0)/(1+self.s)
        Vh = (-2/self.n)*(R@(hstar.T@hidden[0]) + rho*bstar@((H-hstar).T@hidden[0]))
        S = (2/(self.n*self.M))*(backward[1]*Vh).sum()
        gamma = (-S/self.kappa).clamp(0,1) if self.gated else torch.ones_like(S)
        return [*outer, gamma*self._transport(A,R,rho),
                gamma*self._transport(B,rho*H,rho),gamma*rho]


def oracle():
    torch.set_num_threads(1)
    rng = np.random.default_rng(741)
    x = rng.normal(size=(11,5)); x /= np.linalg.norm(x,axis=1,keepdims=True)
    y = rng.normal(size=11)
    basis,_ = np.linalg.qr(rng.normal(size=(11,3)))
    basis *= np.sqrt(11)
    errors=[]
    for q in [1,2,4]:
        for gated in [False,True]:
            model = CertifiedField(x,y,basis,width=4,depth=2,activation='tanh',seed=741,
                device='cpu',dtype=torch.float64,hidden_gain=1.,readout_std=1.,order=q,gated=gated)
            with torch.no_grad():
                model.c.copy_(torch.tensor(rng.normal(size=4)))
                for val in model.moments:
                    val.add_(torch.tensor(rng.normal(size=tuple(val.shape)))*.2)
                model.s.fill_(1.2)
            velocity,metrics,V = model.fields_and_velocity()
            rhs = model.rhs()
            assert max(float((a-b).abs().max()) for a,b in zip(rhs,velocity)) < 1e-12
            w,c,A,B,s = [v.detach().clone().requires_grad_() for v in model.state]
            def reconstruct(A,B,s):
                return model.matrices[0]-2/(model.n*(1+s))*torch.einsum('jic,jkc,j->ik',A,B,model.weights[:,0,0])
            matrix = reconstruct(A,B,s)
            h = torch.tanh(w@model.inputs.T)
            g = torch.tanh(matrix@h)
            f = c@g/model.n
            loss = (f-model.labels).square().mean()
            grad = torch.autograd.grad(loss,[w,c,A,B,s])
            derivative = sum((g*v).sum() for g,v in zip(grad,velocity))
            errors.append(float(abs(derivative-metrics[5])))
            errors.append(float(abs(metrics[8])))
            _,matrix_velocity = torch.autograd.functional.jvp(reconstruct,(A,B,s),tuple(velocity[2:]))
            errors.append(float((matrix_velocity-metrics[3]*V).abs().max()))
            if gated:
                assert float(derivative) <= 1e-10
    assert max(errors)<1e-9,errors
    zero = CertifiedField(x,np.zeros_like(y),basis,width=4,depth=2,activation='tanh',seed=741,
        device='cpu',dtype=torch.float64,hidden_gain=1.,readout_std=1.,order=3,gated=True)
    assert all(bool(torch.isfinite(v).all()) and float(v.abs().max())==0 for v in zero.rhs())
    return {'checks':len(errors),'max_error':max(errors),'errors':errors,'zero_label_equilibrium':'pass'}


@torch.no_grad()
def make(data,seed,kind,domain,device,dtype=torch.float32,width=256):
    kw=dict(width=width,depth=2,activation='tanh',seed=seed,device=device,dtype=dtype,
            hidden_gain=1.,readout_std=1.)
    if kind=='factor':
        rates={'fashion':.25,'housing':4.,'har':4.}
        return TunedFactors(data['X_train'],data['y_train'],rank=24,factor_seed=seed+10000,
                            factor_rate=rates[domain],**kw)
    initial=Flow(data['X_train'],data['y_train'],order=None,**kw)
    initial.c.zero_()
    h=initial._forward(initial.inputs,None)[0][0]
    basis,vectors,values,_=pca(h,8)
    model=CertifiedField(data['X_train'],data['y_train'],basis,order=3,gated=kind=='gated',**kw)
    model.dictionary_first=model.w.clone()
    model.dictionary_vectors=vectors
    model.dictionary_values=values
    return model


@torch.no_grad()
def capture_check(device):
    rng=np.random.default_rng(741)
    x=rng.normal(size=(32,7));x/=np.linalg.norm(x,axis=1,keepdims=True)
    data={'X_train':x,'y_train':rng.normal(size=32)}
    result={}
    for kind in ['field','gated','factor']:
        a=make(data,741,kind,'fashion',device,width=32)
        b=make(data,741,kind,'fashion',device,width=32)
        saved=[v.clone() for v in a.state]
        stream=torch.cuda.Stream(device=device);stream.wait_stream(torch.cuda.current_stream(device))
        with torch.cuda.stream(stream):a.step(1/32)
        torch.cuda.current_stream(device).wait_stream(stream)
        for v,z in zip(a.state,saved):v.copy_(z)
        graph=torch.cuda.CUDAGraph()
        with torch.cuda.graph(graph,stream=stream):
            for _ in range(4):a.step(1/32)
        for v,z in zip(a.state,saved):v.copy_(z)
        graph.replay()
        for _ in range(4):b.step(1/32)
        error=max(float((v-z).abs().max()) for v,z in zip(a.state,b.state))
        assert error<2e-5,error
        result[kind]=error
    return result


@torch.no_grad()
def fit(path,seed,kind,device,out,dt):
    start=time.perf_counter()
    raw=dict(np.load(path))
    data={k:torch.tensor(raw[k],device=device,dtype=torch.float32)
          for k in ['X_train','y_train','X_val','y_val','X_test','y_test']}
    model=make(data,seed,kind,path.stem,device)
    state0=[v.clone() for v in model.state]
    stream=torch.cuda.Stream(device=device);stream.wait_stream(torch.cuda.current_stream(device))
    with torch.cuda.stream(stream):
        for _ in range(2):model.step(dt)
    torch.cuda.current_stream(device).wait_stream(stream)
    for v,z in zip(model.state,state0):v.copy_(z)
    block=round(1/dt)
    graph=torch.cuda.CUDAGraph()
    with torch.cuda.graph(graph,stream=stream):
        for _ in range(block):model.step(dt)
    for v,z in zip(model.state,state0):v.copy_(z)
    del state0
    metrics=[];checkpoints=[];predictions=[]
    for timepoint in range(1,129):
        graph.replay()
        if kind!='factor':
            _,measure,_=model.fields_and_velocity()
            metrics.append([timepoint,*measure.cpu().tolist()])
        if timepoint in [16,32,64,128]:
            cp={'time':timepoint}
            for split in ['train','val','test']:
                pred=model.predict(data['X_'+split])
                cp[split]=float((pred-data['y_'+split]).square().mean().sqrt())
                if split=='test':predictions.append(pred.cpu().numpy())
            checkpoints.append(cp)
    assert all(bool(torch.isfinite(v).all()) for v in model.state)
    best=min(range(4),key=lambda i:checkpoints[i]['val'])
    result={'domain':path.stem,'seed':seed,'kind':kind,'dt':dt,'width':256,'checkpoints':checkpoints,
        'selected_index':best,'selected':checkpoints[best],'seconds':time.perf_counter()-start,
        'data_sha256':sha(path),'moving_scalars':sum(v.numel() for v in model.state),
        'fixed_base_scalars':model.n**2,'dictionary_scalars':model.w.numel()+model.n*8+8 if kind!='factor' else 0,
        'cached_basis_scalars':model.M*8 if kind!='factor' else 0}
    if metrics:
        arr=np.asarray(metrics)
        result['diagnostics']={'sampled_hidden_ascent_fraction':float(np.mean(arr[:,3]>1e-10)),
            'sampled_ungated_loss_ascent_fraction':float(np.mean(arr[:,5]>1e-10)),
            'sampled_actual_loss_ascent_fraction':float(np.mean(arr[:,6]>1e-10)),
            'mean_gate':float(arr[:,4].mean()),'minimum_gate':float(arr[:,4].min()),
            'maximum_hidden_contribution':float(arr[:,3].max())}
    np.savez_compressed(out/'arrays.npz',predictions=np.stack(predictions),metrics=np.asarray(metrics),target=raw['y_test'])
    write(out/'result.json',result)
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--data',type=Path)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--device',default='cuda:0')
    parser.add_argument('--checks-only',action='store_true')
    parser.add_argument('--diagnostics-only',action='store_true')
    args=parser.parse_args()
    args.out.mkdir(parents=True,exist_ok=False)
    checks=oracle();write(args.out/'oracle.json',checks)
    if args.checks_only:
        print(json.dumps(checks));return
    torch.set_num_threads(1);torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
    torch.cuda.set_device(args.device)
    names=['stage2_root_gate.py','stage2_index_experiment.py','input_field.py','baseline_compact_flow.py',
           'STAGE2_ROOT_GATE_PROTOCOL.md','STAGE2_CHALLENGE_THEORY.md']
    for name in names:shutil.copy2(HERE/name,args.out/name)
    write(args.out/'manifest.json',{'command':sys.argv,'sources':{n:sha(HERE/n) for n in names},
        'torch':torch.__version__,'numpy':np.__version__,'device':torch.cuda.get_device_name(),
        'tf32':False,'threads':1})
    write(args.out/'capture_checks.json',capture_check(args.device))
    results=[]
    if args.diagnostics_only:
        for path in sorted(args.data.glob('*.npz')):
            folder=args.out/f'fit_{len(results):03d}';folder.mkdir()
            result=fit(path,4101,'field',args.device,folder,1/32);results.append(result)
            write(args.out/'results.json',results);print(json.dumps(result),flush=True)
        write(args.out/'completion.json',{'fits':len(results),'seconds':sum(r['seconds'] for r in results),'status':'complete'})
        return
    for seed in [4101,4102,4103]:
        for path in sorted(args.data.glob('*.npz')):
            for kind in ['field','gated','factor']:
                folder=args.out/f'fit_{len(results):03d}';folder.mkdir()
                result=fit(path,seed,kind,args.device,folder,1/32);results.append(result)
                write(args.out/'results.json',results);print(json.dumps(result),flush=True)
    for path in sorted(args.data.glob('*.npz')):
        for kind in ['field','gated']:
            folder=args.out/f'fit_{len(results):03d}';folder.mkdir()
            result=fit(path,4101,kind,args.device,folder,1/64);results.append(result)
            write(args.out/'results.json',results);print(json.dumps(result),flush=True)
    write(args.out/'completion.json',{'fits':len(results),'seconds':sum(r['seconds'] for r in results),'status':'complete'})


if __name__=='__main__':main()
