"""Dense sphere3 network to t=32 (Euler): forward and backward fields of every layer-2 neuron, for Fig 19c.

Same network and data as train_sphere3_t32.py. Records, every 32 Euler steps, the
layer-2 activations h (n, m) and backward responses delta = w * tanh'(z) (n, m)
at all m training inputs, and the residual r (m).

Usage: python record_neuron_clouds.py OUT.npz
"""
import sys, time
import numpy as np
import torch

sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parents[2]))
from capture_trajectory import DeepDense, validation_data  # noqa: E402

OUT = sys.argv[1]
dev = torch.device('cuda:0')
n, d, m, step, T, every = 1024, 3, 8, 0.0015625, 32., 32
x, y, xq, yq = validation_data(d, m, 30, 601, dev, task='toy')
model = DeepDense(n, d, 2, 'tanh', 601, dev)
state = [v.clone() for v in model.initial_state]
rec = dict(t=[], h2=[], d2=[], r=[])
started = time.time()
steps = int(round(T/step))
for k in range(steps+1):
    if k % every == 0:
        hs, gates = model.fields(state, x)
        deltas = model.backward(state, hs, gates)
        rec['t'].append(k*step)
        rec['h2'].append(hs[1].float().cpu().numpy())       # (n, m) forward, layer 2
        rec['d2'].append(deltas[1].float().cpu().numpy())   # (n, m) backward, layer 2
        rec['r'].append((state[1]@hs[-1]/n-y).cpu().numpy())
    if k == steps:
        break
    g = model.rhs(state, x, y)
    state = [v+step*gv for v, gv in zip(state, g)]
print('train seconds', time.time()-started, 'final loss', float(np.square(rec['r'][-1]).mean()))
np.savez_compressed(OUT, n=n, step=step, every=every, x=x.cpu().numpy(), y=y.cpu().numpy(),
                    **{k: np.array(v) for k, v in rec.items()})
print('saved', OUT, 'total seconds', time.time()-started)
