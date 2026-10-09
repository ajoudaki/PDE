"""Width-1024, two tanh layers, Euler; 128 points on S^2, odd degree-3/5 target (Fig 21c).

Usage: python train_rich_target.py OUT.npz T   (the figure uses T = 64)
"""
import sys, time, math
import numpy as np, torch
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[2]))
from capture_trajectory import DeepDense  # noqa: E402
dev = torch.device('cuda:0'); n, d, m, step, T = 1024, 3, 128, 0.0015625, float(sys.argv[2])
rng = np.random.default_rng(7)
X = rng.normal(size=(m, 3)); X /= np.linalg.norm(X, axis=1, keepdims=True)
def target(v): return 15*v[:, 0]*v[:, 1]*v[:, 2]+2.5*(5*v[:, 2]**3-3*v[:, 2])+0.7*v[:, 0]+3*(v[:, 1]**5-10*v[:, 1]**3*v[:, 0]**2+5*v[:, 1]*v[:, 0]**4)
Y = target(X); Y /= np.sqrt(np.mean(Y**2))
x, y = torch.as_tensor(X, device=dev), torch.as_tensor(Y, device=dev)
model = DeepDense(n, d, 2, 'tanh', 11, dev)
state = [v.clone() for v in model.initial_state]
t0 = time.time()
for k in range(int(round(T/step))):
    hs, gates = model.fields(state, x); deltas = model.backward(state, hs, gates)
    deficit = y-state[1]@hs[-1]/n
    g = [(2/m)*(deltas[0]*deficit)@x, (2/m)*hs[1]@deficit, (2/(m*n))*(deltas[1]*deficit)@hs[0].T]
    state = [v+step*gv for v, gv in zip(state, g)]
print('seconds', time.time()-t0, 'train rms', float((y-state[1]@model.fields(state, x)[0][-1]/n).square().mean().sqrt()))
NT, NP = 64, 128
ct, wt = np.polynomial.legendre.leggauss(NT); ph = 2*np.pi*np.arange(NP)/NP
CT, PH = np.meshgrid(ct, ph, indexing='ij'); ST = np.sqrt(1-CT**2)
V = np.stack([ST*np.cos(PH), ST*np.sin(PH), CT], -1).reshape(-1, 3)
with torch.no_grad():
    hs, _ = model.fields(state, torch.as_tensor(V, device=dev))
    f = (state[1]@hs[-1]/n).cpu().numpy(); h2 = hs[1].cpu().numpy(); h1 = hs[0].cpu().numpy()
np.savez_compressed(sys.argv[1], ct=ct, wt=wt, ph=ph, f=f, h2=h2, h1=h1[:64], fstar=target(V)/np.sqrt(np.mean(target(X)**2)))
