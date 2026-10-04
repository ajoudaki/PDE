"""Bounded own-state dense / Legendre equilibrium pilot; see frozen candidate."""
import argparse
import hashlib
import json
import math
import os
import time
from pathlib import Path

import torch

torch.set_num_threads(1)
torch.set_grad_enabled(False)
torch.set_default_dtype(torch.float64)


def grid_matrix(side, heterogeneous, device):
    n = side * side
    xy = torch.cartesian_prod(torch.linspace(0, 1, side),
                              torch.linspace(0, 1, side)).to(device)
    conductivity = (1 + 0.65 * torch.sin(2 * math.pi * xy[:, 0])
                    * torch.cos(2 * math.pi * xy[:, 1])) if heterogeneous else torch.ones(n, device=device)
    p = torch.zeros(n, n, device=device)
    for i in range(side):
        for j in range(side):
            k = i * side + j
            for ii, jj in ((i+1, j), (i, j+1)):
                if ii < side and jj < side:
                    l = ii * side + jj
                    p[k, l] = p[l, k] = 0.5 * (conductivity[k] + conductivity[l])
    return p / torch.linalg.eigvalsh(p)[-1], xy


def forcings(xy, count, seed):
    gen = torch.Generator(device="cpu").manual_seed(seed)
    coeff = torch.randn(count, 6, generator=gen).to(xy.device)
    modes = [(1,1), (1,2), (2,1), (2,2), (3,1), (1,3)]
    basis = torch.stack([torch.sin(i*math.pi*xy[:,0]) * torch.sin(j*math.pi*xy[:,1])
                         for i,j in modes])
    broad = coeff @ basis / math.sqrt(6)
    centers = torch.rand(count, 2, generator=gen).to(xy.device)
    amps = torch.randn(count, generator=gen).to(xy.device)
    bump = torch.exp(-((xy[None]-centers[:,None])**2).sum(-1)/(2*0.13**2))
    return 0.12 * (broad + amps[:,None]*bump)


class Pilot:
    def __init__(self, args):
        self.args = args
        self.start = time.monotonic()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        if self.device.type != "cuda":
            raise RuntimeError("This authorized pilot requires the selected GPU.")
        self.p0, self.xy = grid_matrix(args.side, False, self.device)
        self.pstar, _ = grid_matrix(args.side, True, self.device)
        self.w0 = 0.6*self.p0
        self.n = self.w0.shape[0]
        self.u = forcings(self.xy, args.samples+args.test_samples, args.seed)
        self.y, _, _ = self.forward(0.985*self.pstar, self.u)
        self.h0, _, _ = self.forward(self.w0, self.u)
        self.eye = torch.eye(self.n, device=self.device)
        self.out = Path(args.output)
        self.out.mkdir(parents=True, exist_ok=True)
        self.records = {}

    def budget(self):
        if time.monotonic()-self.start > self.args.max_seconds:
            raise TimeoutError("Preregistered process-time cap reached")

    def forward(self, w, u, start=None):
        self.budget()
        h = torch.zeros_like(u) if start is None else start.clone()
        for k in range(1200):
            next_h = torch.tanh(h @ w.T + u)
            err = torch.linalg.vector_norm(next_h-h, dim=1)
            scale = torch.linalg.vector_norm(next_h, dim=1).clamp_min(1e-12)
            h = next_h
            if float((err/scale).max()) < 1e-11:
                residual = torch.tanh(h @ w.T+u)-h
                rel = float((torch.linalg.vector_norm(residual,dim=1) /
                             torch.linalg.vector_norm(h,dim=1).clamp_min(1e-12)).max())
                if rel > 1e-9:
                    raise RuntimeError("Equilibrium residual gate failed")
                return h, rel, k+1
            if not torch.isfinite(h).all():
                raise RuntimeError("Nonfinite equilibrium iterate")
            if k % 100 == 0:
                self.budget()
        raise RuntimeError("Equilibrium iteration cap reached")

    def credit(self, w, h, y):
        d = 1-h*h
        kt = self.eye[None] - w.T[None] * d[:,None,:]
        e = h-y
        lam = torch.linalg.solve(kt, e[:,:,None]).squeeze(-1)
        res = (kt @ lam[:,:,None]).squeeze(-1)-e
        rel = float((torch.linalg.vector_norm(res,dim=1) /
                     torch.linalg.vector_norm(e,dim=1).clamp_min(1e-12)).max())
        if rel > 1e-9 or not torch.isfinite(lam).all():
            raise RuntimeError("Adjoint residual gate failed")
        return d*lam, lam, rel

    def physical(self, state, method):
        if method == "dense":
            return state[0]
        if method.startswith("svd"):
            return self.w0+state[0]@state[1].T
        hbar,bbar,tau = state
        q = hbar.shape[1]
        weights = torch.arange(q, device=self.device,dtype=torch.float64)*2+1
        return self.w0 - 2/(self.n*self.args.samples*tau) * torch.einsum(
            "aqi,q,aqj->ij", bbar, weights, hbar)

    def rhs(self, state, method, warm=None):
        w = self.physical(state, method)
        h, _, _ = self.forward(w, self.u[:self.args.samples], warm)
        delta, _, _ = self.credit(w,h,self.y[:self.args.samples])
        if method == "dense":
            return [-2/(self.n*self.args.samples)*delta.T@h], h
        hbar,bbar,tau = state
        q = hbar.shape[1]
        rho = ((h-self.y[:self.args.samples])**2).mean().sqrt()
        j = torch.arange(q, device=self.device,dtype=torch.float64)
        tmat = (2*j[None,:]+1).expand(q,q).clone()
        tmat = torch.tril(tmat, diagonal=-1)+torch.diag(j)
        dh = rho*h[:,None,:] - rho/tau*torch.einsum("jk,akn->ajn",tmat,hbar)
        db = delta[:,None,:] - rho/tau*torch.einsum("jk,akn->ajn",tmat,bbar)
        return [dh,db,rho], h

    def measure(self, state, method, t):
        w = self.physical(state, method)
        h, f_res, iterations = self.forward(w,self.u)
        delta,lam,b_res = self.credit(w,h[:self.args.samples],self.y[:self.args.samples])
        d = 1-h[:self.args.samples]**2
        k = self.eye[None]-d[:,:,None]*w[None]
        a = self.eye[None]-d[:,:,None]*self.w0[None]
        sv = torch.linalg.svdvals(w-self.w0)
        energy = sv.square()
        erank = int(torch.searchsorted(energy.cumsum(0),0.99*energy.sum()))+1 if float(energy.sum()) else 0
        kinv = 1/torch.linalg.svdvals(k)[:,-1]
        ainv = 1/torch.linalg.svdvals(a)[:,-1]
        e = h[:self.args.samples]-self.y[:self.args.samples]
        amp = torch.linalg.vector_norm(lam,dim=1)/torch.linalg.vector_norm(e,dim=1).clamp_min(1e-12)
        record = {
            "time":t, "train_mse":float(e.square().mean()),
            "test_mse":float((h[self.args.samples:]-self.y[self.args.samples:]).square().mean()),
            "feature_change_rms":float((h-self.h0).square().mean().sqrt()),
            "gate_fraction_above_0p05":float(((1-d)>0.05).double().mean()),
            "increment_frobenius":float(torch.linalg.vector_norm(w-self.w0)),
            "increment_effective_rank_99":erank, "increment_singular_values":sv.cpu().tolist(),
            "full_inverse_norm":kinv.cpu().tolist(),"base_inverse_norm":ainv.cpu().tolist(),
            "loss_directed_gain":amp.cpu().tolist(),
            "forward_residual":f_res,"adjoint_residual":b_res,"forward_iterations":iterations,
        }
        torch.save({"w":w.cpu(),"h":h.cpu(),"lambda":lam.cpu(),"delta":delta.cpu(),
                    "state":[s.cpu() for s in state],"record":record},
                   self.out/f"{method}_t{t:g}.pt")
        self.records.setdefault(method,[]).append(record)
        print(json.dumps({k:v for k,v in record.items() if k not in
             ("increment_singular_values","full_inverse_norm","base_inverse_norm","loss_directed_gain")}
             | {"method":method,"inverse_norm_max":float(kinv.max()),
                "elapsed":time.monotonic()-self.start}),flush=True)

    def gradient_check(self):
        p,xy=grid_matrix(4,False,self.device)
        w=0.4*p
        u=forcings(xy,3,919)
        h,_,_=self.forward(w,u)
        y=0.7*h+0.02
        d=1-h*h
        kt=torch.eye(16,device=self.device)[None]-w.T[None]*d[:,None,:]
        lam=torch.linalg.solve(kt,(h-y)[:,:,None]).squeeze(-1)
        grad=2/(16*3)*(d*lam).T@h
        g=torch.Generator(device="cpu").manual_seed(920)
        v=torch.randn(16,16,generator=g).to(self.device)
        v/=torch.linalg.vector_norm(v)
        eps=1e-4
        hp,_,_=self.forward(w+eps*v,u)
        hm,_,_=self.forward(w-eps*v,u)
        finite=float(((hp-y).square().mean()-(hm-y).square().mean())/(2*eps))
        analytic=float((grad*v).sum())
        rel=abs(finite-analytic)/max(abs(finite),abs(analytic),1e-12)
        with torch.enable_grad():
            aw=w.clone().requires_grad_(True)
            ah=torch.zeros_like(u)
            for _ in range(100):
                ah=torch.tanh(ah@aw.T+u)
            oracle=torch.autograd.grad((ah-y).square().mean(),aw)[0]
        oracle_error=float(torch.linalg.vector_norm(grad-oracle)/torch.linalg.vector_norm(oracle))
        check={"finite":finite,"analytic":analytic,"relative_error":rel,
               "unrolled_autograd_gradient_error":oracle_error}
        (self.out/"gradient_check.json").write_text(json.dumps(check,indent=2))
        if rel>1e-6 or oracle_error>1e-8:
            raise RuntimeError(f"Directional gradient check failed {check}")

    def moment_check(self):
        q=3
        hb=torch.zeros(self.args.samples,q,self.n,device=self.device)
        hb[:,0]=self.h0[:self.args.samples]
        bb=torch.zeros_like(hb)
        zero_error=float(torch.linalg.vector_norm(self.physical([hb,bb,torch.ones((),device=self.device)],"memory3")-self.w0))
        gen=torch.Generator(device="cpu").manual_seed(922)
        hb=hb+0.01*torch.randn(hb.shape,generator=gen).to(self.device)
        bb=0.01*torch.randn(bb.shape,generator=gen).to(self.device)
        tau=torch.tensor(1.4,device=self.device)
        state=[hb,bb,tau]
        tangent,h=self.rhs(state,"memory3")
        w=self.physical(state,"memory3")
        delta,_,_=self.credit(w,h,self.y[:self.args.samples])
        rho=(h-self.y[:self.args.samples]).square().mean().sqrt()
        weights=2*torch.arange(q,device=self.device,dtype=torch.float64)+1
        hs=torch.einsum("aqn,q->an",hb,weights)/tau
        bs=torch.einsum("aqn,q->an",bb,weights)/tau
        expected=-2/(self.n*self.args.samples)*delta.T@h + 2*rho/(self.n*self.args.samples)*(delta/rho-bs).T@(h-hs)
        with torch.enable_grad():
            _,velocity=torch.autograd.functional.jvp(
                lambda hh,dd,tt:self.physical([hh,dd,tt],"memory3"),
                tuple(state),tuple(tangent),strict=True)
        rel=float(torch.linalg.vector_norm(velocity-expected)/torch.linalg.vector_norm(expected))
        check={"zero_reconstruction_error":zero_error,"velocity_defect_autograd_error":rel}
        (self.out/"moment_check.json").write_text(json.dumps(check,indent=2))
        if zero_error>1e-12 or rel>1e-8:
            raise RuntimeError(f"Moment identity failed {check}")

    def truncate(self,u,v,rank):
        qu,ru=torch.linalg.qr(u,mode="reduced")
        qv,rv=torch.linalg.qr(v,mode="reduced")
        left,s,right=torch.linalg.svd(ru@rv.T,full_matrices=False)
        r=min(rank,len(s))
        return [(qu@left[:,:r])*s[:r],qv@right[:r].T]

    def run(self, method):
        run_start=time.monotonic()
        if method=="dense":
            state=[self.w0.clone()]
        elif method.startswith("svd"):
            state=[torch.empty(self.n,0,device=self.device),torch.empty(self.n,0,device=self.device)]
        else:
            q=int(method.removeprefix("memory"))
            hbar=torch.zeros(self.args.samples,q,self.n,device=self.device)
            hbar[:,0]=self.h0[:self.args.samples]
            state=[hbar,torch.zeros_like(hbar),torch.ones((),device=self.device)]
        self.measure(state,method,0)
        warm=self.h0[:self.args.samples]
        steps=round(self.args.horizon/self.args.step)
        checkpoints={round(t/self.args.step):t for t in (5,10,20,40)
                     if t<=self.args.horizon}
        for k in range(1,steps+1):
            self.budget()
            if method.startswith("svd"):
                rank=int(method.removeprefix("svd"))
                w=self.physical(state,method)
                h1,_,_=self.forward(w,self.u[:self.args.samples],warm)
                d1,_,_=self.credit(w,h1,self.y[:self.args.samples])
                scale=-2/(self.n*self.args.samples)
                wp=w+self.args.step*scale*d1.T@h1
                h2,_,_=self.forward(wp,self.u[:self.args.samples],h1)
                d2,_,_=self.credit(wp,h2,self.y[:self.args.samples])
                unew=torch.cat((state[0],self.args.step*0.5*scale*d1.T,self.args.step*0.5*scale*d2.T),dim=1)
                vnew=torch.cat((state[1],h1.T,h2.T),dim=1)
                state=self.truncate(unew,vnew,rank)
                warm=h2
                if k in checkpoints:
                    self.measure(state,method,checkpoints[k])
                continue
            f1,h1=self.rhs(state,method,warm)
            trial=[s+self.args.step*f for s,f in zip(state,f1)]
            f2,h2=self.rhs(trial,method,h1)
            state=[s+self.args.step*0.5*(a+b) for s,a,b in zip(state,f1,f2)]
            warm=h2
            if k in checkpoints:
                self.measure(state,method,checkpoints[k])
        torch.cuda.synchronize()
        return time.monotonic()-run_start

    def compare(self):
        summary=[]
        target_rms=float(self.y[self.args.samples:].square().mean().sqrt())
        for method,records in self.records.items():
            if method=="dense":
                continue
            for record in records:
                t=record["time"]
                dense_file=self.out/f"dense_t{t:g}.pt"
                if not dense_file.exists():
                    continue
                dense=torch.load(dense_file,weights_only=False)
                mem=torch.load(self.out/f"{method}_t{t:g}.pt",weights_only=False)
                test=(mem["h"][self.args.samples:]-dense["h"][self.args.samples:])
                summary.append({
                    "method":method,"time":t,
                    "test_prediction_relative_rms":float(test.square().mean().sqrt())/target_rms,
                    "train_prediction_relative_rms":float((mem["h"][:self.args.samples]-dense["h"][:self.args.samples]).square().mean().sqrt())/
                        float(self.y[:self.args.samples].square().mean().sqrt()),
                    "adjoint_relative_error":float(torch.linalg.vector_norm(mem["lambda"]-dense["lambda"]))/
                        max(float(torch.linalg.vector_norm(dense["lambda"])),1e-12),
                    "weight_increment_relative_error":float(torch.linalg.vector_norm(mem["w"]-dense["w"]))/
                        max(float(torch.linalg.vector_norm(dense["w"]-self.w0.cpu())),1e-12),
                })
        return summary


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--side",type=int,default=16)
    parser.add_argument("--samples",type=int,default=8)
    parser.add_argument("--test-samples",type=int,default=32)
    parser.add_argument("--seed",type=int,default=4101)
    parser.add_argument("--step",type=float,default=0.25)
    parser.add_argument("--horizon",type=float,default=40)
    parser.add_argument("--methods",default="dense,memory4")
    parser.add_argument("--max-seconds",type=float,default=480)
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    runner=Pilot(args)
    metadata={"args":vars(args),"torch":torch.__version__,"cuda":torch.version.cuda,
              "device":torch.cuda.get_device_name(),"cuda_visible_devices":os.environ.get("CUDA_VISIBLE_DEVICES"),
              "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "timings":{},"failures":[]}
    runner.gradient_check()
    runner.moment_check()
    torch.save({"u":runner.u.cpu(),"y":runner.y.cpu(),"w0":runner.w0.cpu(),
                "teacher":(0.985*runner.pstar).cpu(),"h0":runner.h0.cpu()},runner.out/"data.pt")
    for method in args.methods.split(","):
        try:
            metadata["timings"][method]=runner.run(method)
        except Exception as exc:
            metadata["failures"].append({"method":method,"error":repr(exc)})
            print(json.dumps(metadata["failures"][-1]),flush=True)
            break
    torch.cuda.synchronize()
    metadata["total_process_seconds"]=time.monotonic()-runner.start
    metadata["peak_cuda_bytes"]=torch.cuda.max_memory_allocated()
    tag=args.methods.replace(",","_")
    (runner.out/f"metadata_{tag}.json").write_text(json.dumps(metadata,indent=2))
    (runner.out/f"metrics_{tag}.json").write_text(json.dumps(runner.records,indent=2))
    comparison=runner.compare()
    (runner.out/f"comparison_{tag}.json").write_text(json.dumps(comparison,indent=2))
    print(json.dumps({"comparison":comparison,"metadata":metadata}),flush=True)


if __name__=="__main__":
    main()
