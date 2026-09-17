"""Actual dense two-hidden tanh network in the canonical physical metric."""
from dataclasses import dataclass
import numpy as np
import torch

@dataclass
class NetworkState:
    w: torch.Tensor
    c: torch.Tensor
    M: torch.Tensor

class NetworkEngine:
    def __init__(self,d,width,seed,*,device='cpu',dtype=torch.float64,block_size=512):
        self.d=d;self.n=width;self.device=torch.device(device);self.dtype=dtype;self.block_size=block_size
        rng=np.random.default_rng(seed)
        w=rng.standard_normal((width,d));M=rng.standard_normal((width,width))/np.sqrt(width)
        c=rng.standard_normal(width)/width
        self.initial=NetworkState(*(torch.as_tensor(a,device=device,dtype=dtype) for a in (w,c,M)))
    def initial_state(self):
        return NetworkState(*(v.clone() for v in (self.initial.w,self.initial.c,self.initial.M)))
    def prepare_data(self,U,y):
        return (torch.as_tensor(U,device=self.device,dtype=self.dtype),torch.as_tensor(y,device=self.device,dtype=self.dtype))
    def fields(self,state,U):
        h1=torch.tanh(state.w@U.T);h2=torch.tanh(state.M@h1)
        return h1,h2,state.c@h2/self.n
    @torch.no_grad()
    def predict(self,state,U):
        U=torch.as_tensor(U,device=self.device,dtype=self.dtype)
        return torch.cat([self.fields(state,U[s:s+self.block_size])[2] for s in range(0,len(U),self.block_size)])
    @torch.no_grad()
    def rhs(self,state,data):
        U,y=data;m=len(U)
        vw=torch.zeros_like(state.w);vc=torch.zeros_like(state.c);vM=torch.zeros_like(state.M)
        for s in range(0,m,self.block_size):
            u=U[s:s+self.block_size];h1,h2,f=self.fields(state,u);r=(f-y[s:s+self.block_size])/m
            delta2=state.c[:,None]*(1-h2*h2)
            delta1=(state.M.T@delta2)*(1-h1*h1)
            vw.addmm_(delta1*r,u,alpha=-2.)
            vc.addmv_(h2,r,alpha=-2.)
            vM.addmm_(delta2*r,h1.T,alpha=-2./self.n)
        return NetworkState(vw,vc,vM)
    @torch.no_grad()
    def heun_step(self,state,data,dt):
        k=self.rhs(state,data)
        stage=NetworkState(*(a+dt*b for a,b in zip((state.w,state.c,state.M),(k.w,k.c,k.M))))
        ell=self.rhs(stage,data)
        return NetworkState(*(a+(dt/2)*(b+c) for a,b,c in zip((state.w,state.c,state.M),(k.w,k.c,k.M),(ell.w,ell.c,ell.M))))
    @torch.no_grad()
    def observations(self,state,panel):
        panel=torch.as_tensor(panel,device=self.device,dtype=self.dtype)
        h1,h2,f=self.fields(state,panel);h10,h20,_=self.fields(self.initial,panel)
        return {'gram1':h1.T@h1/self.n,'gram2':h2.T@h2/self.n,
                'rms_motion1':torch.sqrt(torch.mean((h1-h10)**2)),
                'rms_motion2':torch.sqrt(torch.mean((h2-h20)**2))}
    def state_bytes(self,state):
        return sum(a.numel()*a.element_size() for a in (state.w,state.c,state.M))

def verify(device='cpu'):
    import sys
    from pathlib import Path
    sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'code'))
    from pde.finite_network import Parameters,forward,flow_velocity
    rng=np.random.default_rng(62);d=5;n=12;m=9
    U=rng.normal(size=(m,d));U/=np.linalg.norm(U,axis=1,keepdims=True);y=rng.normal(size=m)
    engine=NetworkEngine(d,n,31,device=device,block_size=4)
    state=engine.initial_state();state.c.add_(torch.as_tensor(rng.normal(size=n),device=device))
    state.M.add_(.1*torch.as_tensor(rng.normal(size=(n,n)),device=device))
    def params(s):
        return Parameters((s.w.cpu().numpy(),s.M.cpu().numpy()),s.c.cpu().numpy())
    data=engine.prepare_data(U,y);X=U.T*np.sqrt(d)
    ref=forward(params(state),X).output;vel=flow_velocity(params(state),X,y)
    actual=engine.rhs(state,data)
    errors={'prediction':float(np.max(np.abs(ref-engine.predict(state,U).cpu().numpy())))}
    for name,a,b in [('w',actual.w,vel.weights[0]),('M',actual.M,vel.weights[1]),('c',actual.c,vel.readout)]:
        errors[name]=float(np.max(np.abs(a.cpu().numpy()-b)))
    h=.02;stage=Parameters(tuple(w+h*v for w,v in zip(params(state).weights,vel.weights)),params(state).readout+h*vel.readout)
    ell=flow_velocity(stage,X,y)
    expected=[params(state).weights[0]+h/2*(vel.weights[0]+ell.weights[0]),params(state).readout+h/2*(vel.readout+ell.readout),params(state).weights[1]+h/2*(vel.weights[1]+ell.weights[1])]
    out=engine.heun_step(state,data,h)
    errors['heun']=max(float(np.max(np.abs(a.cpu().numpy()-b))) for a,b in zip((out.w,out.c,out.M),expected))
    assert max(errors.values())<2e-12,errors
    return errors

if __name__=='__main__':
    import argparse,json
    parser=argparse.ArgumentParser();parser.add_argument('--device',default='cpu');args=parser.parse_args()
    print(json.dumps(verify(args.device),indent=2))
