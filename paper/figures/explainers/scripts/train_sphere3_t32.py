"""Dense sphere3 network to t=32 (Euler): histories and sphere fields for Figs 15b, 16b, 21b.

Usage: python train_sphere3_t32.py OUT.npz
"""
import sys, time
import numpy as np
import torch

sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[2]))
from capture_trajectory import DeepDense, validation_data  # noqa: E402

OUT = sys.argv[1]
dev = torch.device('cuda:0')
n, d, m, step, T, every = 1024, 3, 8, 0.0015625, 32., 16
x, y, xq, yq = validation_data(d, m, 30, 601, dev, task='toy')
model = DeepDense(n, d, 2, 'tanh', 601, dev)
state = [v.clone() for v in model.initial_state]
W0 = state[2].clone()
J = torch.arange(64, device=dev)  # recorded neuron indices (first 64 of each layer)
rec = dict(t=[], h1=[], d2=[], r=[], W=[])
started = time.time()
steps = int(round(T/step))
for k in range(steps+1):
    if k % every == 0:
        hs, gates = model.fields(state, x)
        deltas = model.backward(state, hs, gates)
        r = state[1]@hs[-1]/n-y
        rec['t'].append(k*step)
        rec['h1'].append(hs[0][J].cpu().numpy())        # (64, m) forward features, layer 1
        rec['d2'].append(deltas[1][J].cpu().numpy())    # (64, m) backward responses, layer 2
        rec['r'].append(r.cpu().numpy())
        rec['W'].append((state[2]-W0)[J][:, J].cpu().numpy())
    if k == steps:
        break
    g = model.rhs(state, x, y)
    state = [v+step*gv for v, gv in zip(state, g)]
print('train seconds', time.time()-started, 'final loss', float(rec['r'][-1].__pow__(2).mean()))

# sphere grid: Gauss-Legendre in cos(theta) x uniform phi
NT, NP = 64, 128
ct, wt = np.polynomial.legendre.leggauss(NT)
ph = 2*np.pi*np.arange(NP)/NP
CT, PH = np.meshgrid(ct, ph, indexing='ij')
ST = np.sqrt(1-CT**2)
V = np.stack([ST*np.cos(PH), ST*np.sin(PH), CT], -1).reshape(-1, 3)
Vt = torch.as_tensor(V, device=dev)
with torch.no_grad():
    hs, _ = model.fields(state, Vt)
    f = (state[1]@hs[-1]/n).cpu().numpy()
    h2 = hs[1].cpu().numpy()          # (n, points) layer-2 neurons, trained
    hs0, _ = model.fields(model.initial_state, Vt)
    h2_0 = hs0[1].cpu().numpy()        # at initialization
np.savez_compressed(OUT, n=n, step=step, x=x.cpu().numpy(), y=y.cpu().numpy(),
                    **{k: np.array(v) for k, v in rec.items()},
                    ct=ct, wt=wt, ph=ph, f=f, h2=h2, h2_0=h2_0)
print('saved', OUT, 'total seconds', time.time()-started)
