"""Dense sphere3 run (Euler) that also tracks the Legendre moments of its own histories.

Records histories every 16 steps and full restart snapshots at t = 2, 4, 8 (Figs 15c, 16c, 17c).
Usage: python run_sphere3_moments.py OUT.npz T   (the figures use T = 112)
"""
import sys, time
import numpy as np
import torch

sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[2]))
from capture_trajectory import DeepDense, validation_data  # noqa: E402

OUT, T = sys.argv[1], float(sys.argv[2])
RESTARTS = (2., 4., 8.)
dev = torch.device('cuda:0')
n, d, m, step, every, Q = 1024, 3, 8, 0.0015625, 16, 8
x, y, xq, yq = validation_data(d, m, 30, 601, dev, task='toy')
model = DeepDense(n, d, 2, 'tanh', 601, dev)
state = [v.clone() for v in model.initial_state]
W0 = state[2].clone()
J = torch.arange(64, device=dev)
deg = torch.arange(Q, dtype=torch.float64, device=dev)
wts = 2*deg+1
hs, _ = model.fields(state, x)
bar_h = torch.zeros(Q, n, m, dtype=torch.float64, device=dev); bar_h[0] = hs[0]
bar_d = torch.zeros_like(bar_h)
tau = torch.tensor(1., dtype=torch.float64, device=dev)
def transport(mom, src, rho, tau):
    weighted = wts[:, None, None]*mom
    lower = torch.cat((torch.zeros_like(weighted[:1]), weighted[:-1].cumsum(0)), 0)
    return src[None]-(rho/tau)*(deg[:, None, None]*mom+lower)
rec = dict(t=[], tau=[], rho=[], h1=[], d2=[], r=[], W=[], fq=[])
snaps = {}
started = time.time()
steps = int(round(T/step))
for k in range(steps+1):
    hs, gates = model.fields(state, x)
    deltas = model.backward(state, hs, gates)
    r = state[1]@hs[-1]/n-y
    rho = r.norm()/np.sqrt(m)
    tnow = k*step
    if k % every == 0:
        rec['t'].append(tnow); rec['tau'].append(float(tau)); rec['rho'].append(float(rho))
        rec['h1'].append(hs[0][J].cpu().numpy()); rec['d2'].append(deltas[1][J].cpu().numpy())
        rec['r'].append(r.cpu().numpy()); rec['W'].append((state[2]-W0)[J][:, J].cpu().numpy())
        rec['fq'].append(model.predict(state, xq).cpu().numpy())
    for tr in RESTARTS:
        if abs(tnow-tr) < step/2:
            snaps[tr] = dict(A=state[0].cpu().numpy(), w=state[1].cpu().numpy(), tau=float(tau),
                             bar_h=bar_h.cpu().numpy(), bar_d=bar_d.cpu().numpy())
    if k == steps:
        break
    deficit = -r
    g = [(2/m)*(deltas[0]*deficit)@x, (2/m)*hs[1]@deficit, (2/(m*n))*(deltas[1]*deficit)@hs[0].T]
    dh = transport(bar_h, rho*hs[0], rho, tau)
    dd = transport(bar_d, deltas[1]*r, rho, tau)
    state = [v+step*gv for v, gv in zip(state, g)]
    bar_h, bar_d, tau = bar_h+step*dh, bar_d+step*dd, tau+step*rho
print('seconds', time.time()-started, 'final rho', float(rho), 'tau', float(tau))
np.savez_compressed(OUT, W0=W0.cpu().numpy(), x=x.cpu().numpy(), y=y.cpu().numpy(),
                    xq=xq.cpu().numpy(), **{k: np.array(v) for k, v in rec.items()},
                    **{f's{int(tr)}_{key}': val for tr, sn in snaps.items() for key, val in sn.items()})
print('saved', OUT)
