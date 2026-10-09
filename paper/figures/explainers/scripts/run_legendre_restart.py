"""Restart the Legendre moment model at time t_r from the dense moments; Euler to T (Fig 15c).

Usage: python run_legendre_restart.py SNAPSHOTS.npz t_r T OUT.npz   (figures: t_r = 2, 4, 8; T = 32)

Batched over orders q. State: A, w, bar_h, bar_delta, tau. Hidden mixer
W = W0 - 2/(m n tau) sum_j (2j+1) bar_delta_j bar_h_j^T is never formed.
"""
import sys, time
import numpy as np
import torch

SRC, TR, T, OUT = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
ORDERS = (1, 2, 4, 8)
dev = torch.device('cuda:0')
z = np.load(SRC)
tt = lambda a: torch.as_tensor(a, device=dev, dtype=torch.float64)
W0, x, y, xq = tt(z['W0']), tt(z['x']), tt(z['y']), tt(z['xq'])
n, m, Q, B = W0.shape[0], len(y), 8, len(ORDERS)
key = f's{int(TR)}_'
A = tt(z[key+'A'])[None].repeat(B, 1, 1)
w = tt(z[key+'w'])[None].repeat(B, 1)
bar_h = tt(z[key+'bar_h'])[None].repeat(B, 1, 1, 1)
bar_d = tt(z[key+'bar_d'])[None].repeat(B, 1, 1, 1)
tau = torch.full((B,), float(z[key+'tau']), dtype=torch.float64, device=dev)
deg = torch.arange(Q, dtype=torch.float64, device=dev)
wts = 2*deg+1
mask = torch.stack([(deg < q).double() for q in ORDERS])            # (B,Q)
J = torch.arange(64, device=dev)

def factors(bar_h, bar_d, tau):
    left = (-2/(m*n))*((mask*wts)[:, :, None, None]*bar_d).permute(0, 2, 1, 3).reshape(B, n, Q*m)
    right = (bar_h/tau[:, None, None, None]).permute(0, 2, 1, 3).reshape(B, n, Q*m)
    return left, right

def hidden(left, right, v, transpose=False):
    if transpose:
        return torch.einsum('ji,bjk->bik', W0, v)+right@(left.transpose(1, 2)@v)
    return torch.einsum('ij,bjk->bik', W0, v)+left@(right.transpose(1, 2)@v)

def transport(mom, src, rho, tau):
    weighted = wts[None, :, None, None]*mom
    lower = torch.cat((torch.zeros_like(weighted[:, :1]), weighted[:, :-1].cumsum(1)), 1)
    return src[:, None]-(rho/tau)[:, None, None, None]*(deg[None, :, None, None]*mom+lower)

step, every = 0.0015625, 16
rec = dict(t=[], tau=[], h1=[], d2=[], r=[], W=[], fq=[])
steps = int(round((T-TR)/step))
started = time.time()
for k in range(steps+1):
    left, right = factors(bar_h, bar_d, tau)
    h1 = torch.tanh(A@x.T)                                     # (B,n,m)
    h2 = torch.tanh(hidden(left, right, h1))
    r = torch.einsum('bn,bnm->bm', w, h2)/n-y
    rho = r.norm(dim=1)/np.sqrt(m)
    d2 = w[:, :, None]*(1-h2.square())
    if k % every == 0:
        rec['t'].append(TR+k*step); rec['tau'].append(tau.cpu().numpy())
        rec['h1'].append(h1[:, J].cpu().numpy()); rec['d2'].append(d2[:, J].cpu().numpy())
        rec['r'].append(r.cpu().numpy())
        rec['W'].append((left[:, J]@right[:, J].transpose(1, 2)).cpu().numpy())
        hq = torch.tanh(hidden(left, right, torch.tanh(A@xq.T)))
        rec['fq'].append((torch.einsum('bn,bnm->bm', w, hq)/n).cpu().numpy())
    if k == steps:
        break
    d1 = hidden(left, right, d2, transpose=True)*(1-h1.square())
    dA = (-2/m)*(d1*r[:, None, :])@x
    dw = (-2/m)*torch.einsum('bnm,bm->bn', h2, r)
    dh = transport(bar_h, rho[:, None, None]*h1, rho, tau)
    dd = transport(bar_d, d2*r[:, None, :], rho, tau)
    A, w = A+step*dA, w+step*dw
    bar_h, bar_d, tau = bar_h+step*dh, bar_d+step*dd, tau+step*rho
print('restart', TR, 'seconds', time.time()-started, 'final rho', rho.cpu().numpy())
np.savez_compressed(OUT, orders=np.array(ORDERS), **{k: np.array(v) for k, v in rec.items()})
