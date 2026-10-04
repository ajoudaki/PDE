"""Frozen q=1 initialized-mixer training gate; no maintained API dependency."""
import os
for _name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np
import torch
import triton
import triton.language as tl
from sklearn.datasets import load_digits
import sklearn
from reuse_check import FastMixer, quarter_circle


@triton.jit
def _hadamard(X, Y, N: tl.constexpr, LOG: tl.constexpr):
    row = tl.program_id(0)
    i = tl.arange(0, N)
    v = tl.load(X + row * N + i)
    for level in tl.static_range(0, LOG):
        step = 1 << level
        partner = tl.gather(v, i ^ step, axis=0)
        v = tl.where((i & step) == 0, v + partner, partner - v)
    tl.store(Y + row * N + i, v * (N ** -0.5))


def hadamard(x):
    x = x.contiguous()
    y = torch.empty_like(x)
    n = x.shape[-1]
    _hadamard[(x.numel() // n,)](x, y, n, n.bit_length()-1, num_warps=4 if n <= 1024 else 8)
    return y


class Mixer:
    def __init__(self, n, kind, seed, device):
        rng = np.random.default_rng(seed + 19000)
        self.n, self.kind = n, kind
        to = lambda a: torch.as_tensor(a, dtype=torch.float32, device=device)
        if kind == 'gaussian':
            self.matrix = to(rng.standard_normal((n, n)) / np.sqrt(n))
            self.fixed_count = n*n
            return
        singular = (np.ones(n) if kind == 'flat' else quarter_circle(n)
                    if kind == 'quarter_circle' else np.abs(rng.standard_normal(n)))
        singular /= np.sqrt(np.mean(singular**2))
        base = FastMixer(singular, seed + 20000)
        self.left, self.right, self.middle = map(to, (base.left, base.right, base.middle))
        index = lambda a: torch.as_tensor(a, dtype=torch.long, device=device)
        self.perm, self.inverse = map(index, (base.permutation, base.inverse))
        outer = np.random.default_rng(seed + 21000)
        lp, rp = outer.permutation(n), outer.permutation(n)
        self.lp, self.rp, self.li, self.ri = map(index, (lp, rp, np.argsort(lp), np.argsort(rp)))
        self.fixed_count = 9*n  # 3 float arrays, 6 integer index arrays

    def forward(self, x):
        if self.kind == 'gaussian':
            return x @ self.matrix.T
        z = hadamard(x[..., self.rp] * self.right)
        return (hadamard(z[..., self.perm] * self.middle) * self.left)[..., self.lp]

    def transpose(self, x):
        if self.kind == 'gaussian':
            return x @ self.matrix
        z = hadamard(x[..., self.li] * self.left) * self.middle
        return (hadamard(z[..., self.inverse]) * self.right)[..., self.ri]


def evaluate(state, mixer, x):
    A, w, H, D, tau = state
    m, n = H.shape
    h = torch.tanh(x @ A.T / np.sqrt(x.shape[1]))
    z = mixer.forward(h) - (h @ H.T) @ D * (2/(m*n))/tau
    g = torch.tanh(z)
    return g @ w / n, h, g


def rhs(state, mixer, x, y):
    A, w, H, D, tau = state
    m, n = H.shape
    f, h, g = evaluate(state, mixer, x)
    r = f-y
    rho = torch.sqrt(torch.mean(r*r))
    delta = (1-g*g)*w
    ell = (1-h*h)*(mixer.transpose(delta)-(delta @ D.T) @ H*(2/(m*n))/tau)
    return [(-2/m/np.sqrt(x.shape[1]))*(r[:, None]*ell).T @ x,
            (-2/m)*(r @ g), rho*h, r[:, None]*delta, rho]


def step(state, mixer, x, y, dt):
    first = rhs(state, mixer, x, y)
    trial = [v+dt*a for v, a in zip(state, first)]
    second = rhs(trial, mixer, x, y)
    for v, a, b in zip(state, first, second):
        v.add_((dt/2)*(a+b))


def checks(device):
    torch.manual_seed(7201)
    mixer = Mixer(128, 'quarter_circle', 7401, device)
    x = torch.randn(5, 128, device=device)
    matrix = mixer.forward(torch.eye(128, device=device)).T
    ferr = ((mixer.forward(x)-x @ matrix.T).norm()/(x @ matrix.T).norm()).item()
    terr = ((mixer.transpose(x)-x @ matrix).norm()/(x @ matrix).norm()).item()
    if max(ferr, terr) >= 3e-6:
        raise RuntimeError(('fast action mismatch', ferr, terr))
    # Independent autograd physical-gradient oracle, CPU float64.
    g = torch.Generator().manual_seed(7202)
    rand = lambda *s: torch.randn(*s, generator=g, dtype=torch.float64)
    m, n, d = 3, 7, 4
    A, w, H, D = rand(n,d), rand(n), rand(m,n), rand(m,n)
    tau, W0, X, y = torch.tensor(2.3, dtype=torch.float64), rand(n,n)/np.sqrt(n), rand(m,d), rand(m)
    class Dense:
        def forward(self, v): return v @ W0.T
        def transpose(self, v): return v @ W0
    state = [A,w,H,D,tau]
    velocity = rhs(state, Dense(), X, y)
    B = (W0-2*D.T@H/(m*n*tau)).detach().requires_grad_()
    Ag, wg = A.clone().requires_grad_(), w.clone().requires_grad_()
    h = torch.tanh(X@Ag.T/np.sqrt(d)); z = h@B.T; gg = torch.tanh(z)
    f = gg@wg/n; loss = torch.mean((f-y)**2)
    da,dw,dB = torch.autograd.grad(loss, (Ag,wg,B))
    grad_error = max((velocity[0]+n*da).abs().max().item(), (velocity[1]+n*dw).abs().max().item())
    r, rho = f.detach()-y, torch.mean((f.detach()-y)**2).sqrt()
    backward = r[:,None]*(1-gg.detach()**2)*w
    d_recon = -2*(velocity[3].T@H+D.T@velocity[2]-rho/tau*D.T@H)/(m*n*tau)
    defect = 2*rho*(backward/rho-D/tau).T@(h.detach()-H/tau)/(m*n)
    defect_error = (d_recon+dB-defect).abs().max().item()
    if max(grad_error, defect_error)>1e-11:
        raise RuntimeError(('gradient/moment mismatch', grad_error, defect_error))
    return dict(forward_error=ferr, transpose_error=terr, autograd_error=grad_error, defect_error=defect_error)


def data(out):
    raw = load_digits()
    rng = np.random.default_rng(7301)
    training, test = [], []
    for digit in (3,8):
        ix = rng.permutation(np.flatnonzero(raw.target==digit))
        training.extend(ix[:32]); test.extend(ix[32:])
    ix = np.array(training+test)
    X = raw.data[ix].copy(); X-=np.mean(X[:64],axis=0)
    X *= 8/np.linalg.norm(X,axis=1,keepdims=True)
    y = np.where(raw.target[ix]==8,1.,-1.)
    np.savez(out/'data.npz', X=X,y=y,indices=ix)
    return X,y


def run_one(n, kind, seed, dt, X, y, device, out):
    started = time.monotonic()
    mixer = Mixer(n,kind,seed,device)
    rng = np.random.default_rng(seed)
    A = torch.as_tensor(rng.standard_normal((n,X.shape[1])),device=device,dtype=torch.float32)
    m=64
    H = torch.tanh(X[:m]@A.T/np.sqrt(X.shape[1]))
    initial = [A,torch.zeros(n,device=device),H,torch.zeros_like(H),torch.ones((),device=device)]
    state = [v.clone() for v in initial]
    _,h0,g0 = evaluate(initial,mixer,X)
    K = (g0[:m]@g0[:m].T/n).double()
    cross = (g0@g0[:m].T/n).double()
    ev,Q = torch.linalg.eigh(K)
    evals=ev.clamp_min(1e-12); coef=Q.T@y[:m].double()
    # Warm kernels and capture one Heun step. State reset makes warmup invisible.
    for _ in range(3): step(state,mixer,X[:m],y[:m],dt)
    torch.cuda.synchronize()
    for a,b in zip(state,initial): a.copy_(b)
    eager = [v.clone() for v in state]
    step(eager,mixer,X[:m],y[:m],dt)
    graph = torch.cuda.CUDAGraph()
    with torch.cuda.graph(graph): step(state,mixer,X[:m],y[:m],dt)
    # Capture executes once; replay from reset must equal eager.
    for a,b in zip(state,initial): a.copy_(b)
    graph.replay(); torch.cuda.synchronize()
    graph_error=max((a-b).abs().max().item() for a,b in zip(state,eager))
    if graph_error>1e-6: raise RuntimeError(('graph mismatch',graph_error))
    for a,b in zip(state,initial): a.copy_(b)
    compiled = time.monotonic()-started
    torch.cuda.reset_peak_memory_stats()
    times, preds, frozen, metrics = [], [], [], []
    first_history, second_history = [], []
    train_start=time.monotonic()
    steps=int(round(40/dt)); chunk=int(round(2/dt))
    for it in range(steps+1):
        if it%chunk==0:
            t=it*dt
            pred,h,g=evaluate(state,mixer,X)
            fixed=cross@Q@((1-torch.exp(-2*evals*t/m))*coef/evals)
            if not torch.isfinite(pred).all(): raise RuntimeError('nonfinite trajectory')
            times.append(t); preds.append(pred.cpu().numpy()); frozen.append(fixed.cpu().numpy())
            first_history.append(h[:m].cpu().numpy())
            second_history.append(g[:m].cpu().numpy())
            metrics.append(dict(time=t,train_mse=torch.mean((pred[:m]-y[:m])**2).item(),
                test_mse=torch.mean((pred[m:]-y[m:])**2).item(),
                test_error=torch.mean(((pred[m:]>0)!=(y[m:]>0)).float()).item(),
                first_motion=torch.mean((h-h0)**2).sqrt().item(),
                second_motion=torch.mean((g-g0)**2).sqrt().item(),
                frozen_test_mse=torch.mean((fixed[m:]-y[m:])**2).item(),
                gram_trace=torch.mean(g[:m]**2).item(),
                gram_square=torch.mean((g[:m]@g[:m].T/n)**2).item()))
        if it<steps: graph.replay()
    torch.cuda.synchronize()
    elapsed=time.monotonic()-train_start
    tag=f'{kind}_n{n}_s{seed}_dt{dt:g}'
    np.savez(out/f'{tag}.npz',times=times,predictions=preds,frozen=frozen,initial_gram=K.cpu().numpy(),
             train_first=first_history, train_second=second_history)
    record=dict(n=n,kind=kind,seed=seed,dt=dt,graph_error=graph_error,compilation_seconds=compiled,
        training_seconds=elapsed,peak_allocated_bytes=torch.cuda.max_memory_allocated(),
        moving_scalars=sum(v.numel() for v in state),fixed_entries=mixer.fixed_count,metrics=metrics)
    (out/f'{tag}.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:v for k,v in record.items() if k!='metrics'}|{'terminal':metrics[-1]}),flush=True)
    return record


def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True)
    p.add_argument('--widths',type=int,nargs='+',default=[512,2048]);p.add_argument('--seeds',type=int,nargs='+',default=[7401,7402,7403])
    p.add_argument('--kinds',nargs='+',default=['gaussian','flat','quarter_circle','gaussian_diagonal'])
    p.add_argument('--dt',type=float,default=.02);p.add_argument('--device',default='cuda:0')
    args=p.parse_args();args.out.mkdir(parents=True,exist_ok=False)
    torch.set_num_threads(1);torch.backends.cuda.matmul.allow_tf32=False
    torch.backends.cudnn.allow_tf32=False;torch.set_grad_enabled(False)
    started=time.monotonic()
    # Autograd oracle explicitly restores differentiation inside check.
    with torch.enable_grad(): check=checks(args.device)
    X,y=data(args.out)
    sources=[Path(__file__),Path(__file__).with_name('reuse_check.py'),Path(__file__).with_name('TRAINING_PROTOCOL.md')]
    config=dict(arguments=vars(args)|{'out':str(args.out)},checks=check,
        versions=dict(torch=torch.__version__,numpy=np.__version__,sklearn=sklearn.__version__,triton=triton.__version__),
        gpu=torch.cuda.get_device_name(),sources={str(s):hashlib.sha256(s.read_bytes()).hexdigest() for s in sources})
    (args.out/'config.json').write_text(json.dumps(config,indent=2)+'\n')
    X=torch.as_tensor(X,device=args.device,dtype=torch.float32);y=torch.as_tensor(y,device=args.device,dtype=torch.float32)
    rows=[]
    for n in args.widths:
        for seed in args.seeds:
            for kind in args.kinds:
                if time.monotonic()-started>1800: raise RuntimeError('GPU time budget exhausted')
                rows.append(run_one(n,kind,seed,args.dt,X,y,args.device,args.out))
        at_width=[r['metrics'][-1] for r in rows if r['n']==n]
        if all(r['first_motion']<.03 or r['test_mse']>.95*r['frozen_test_mse'] for r in at_width):
            print('STOP: useful feature-learning gate inconclusive',flush=True);break
    (args.out/'summary.json').write_text(json.dumps(dict(rows=rows,elapsed_seconds=time.monotonic()-started),indent=2)+'\n')


if __name__=='__main__': main()
