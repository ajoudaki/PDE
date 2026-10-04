"""Diagnostic Gaussian quadrature of exact q1 initialization derivatives.

No neuron system or trajectory is simulated. See STRUCTURED_POPULATION_CONTRACT.md.
"""
import argparse
import hashlib
import itertools
import json
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.special import roots_hermitenorm


def chunks(dim, order, chunk=32768):
    nodes, weights = roots_hermitenorm(order)
    weights = weights / np.sqrt(2 * np.pi)
    for start in range(0, order**dim, chunk):
        ix = np.array(np.unravel_index(np.arange(start, min(start+chunk, order**dim)), (order,)*dim)).T
        yield nodes[ix], np.prod(weights[ix], axis=1)


def calculate(points, chars, nroot, nsecond):
    m, dim = points.shape
    nc = chars.shape[0]
    gram = points @ points.T
    C = np.zeros((m, m))
    root_records = []
    for a, wt in chunks(dim, nroot):
        h = np.tanh(a @ points.T)
        gate = 1-h*h
        C += h.T @ (wt[:, None]*h)
        root_records.append((h, gate, wt))
    eig, vec = np.linalg.eigh(C)
    if eig.min() <= 0:
        raise ValueError('Degenerate initialized forward covariance')
    sq = vec*np.sqrt(eig)[None, :]
    Ms = np.zeros((nc, m, m))
    cross = np.zeros((nc, m, m))
    energy2 = np.zeros(nc)
    for zstandard, wt in chunks(m, nsecond):
        z = zstandard @ sq.T
        g = np.tanh(z)
        gate = 1-g*g
        gchars = g @ chars.T/m
        U = gchars[:, 0, None]*gate
        energy2 += np.sum(wt[:, None]*gchars*gchars, axis=0)
        gategram = gate.T @ (wt[:, None]*gate)/m
        for k, char in enumerate(chars):
            Y = char[None, :]*gchars[:, k, None]*gate
            Ms[k] += char[:, None]*char[None, :]*gategram
            Ms[k] -= np.diag(2*np.sum(wt[:, None]*Y*g, axis=0))
            cross[k] += U.T @ (wt[:, None]*Y)
    e1 = np.zeros(nc)
    dd1 = np.zeros(nc)
    dd2_A = np.zeros(nc)
    M0 = Ms[0]
    for h, gate, wt in root_records:
        means = [h @ M.T for M in Ms]
        accpre = (gate*means[0]) @ gram/m
        acch = gate*accpre
        hc = h @ chars.T/m
        hcc = acch @ chars.T/m
        e1 += np.sum(wt[:, None]*hc*hc, axis=0)
        dd1 += 2*np.sum(wt[:, None]*hc*hcc, axis=0)
        AU = (gate*means[0]) @ points/m
        gates_gram = gate.T @ (wt[:, None]*gate)
        for k in range(nc):
            AY = (gate*means[k]) @ points/m
            dd2_A[k] += 2*np.sum(wt*np.sum(AU*AY, axis=1))
            dd2_A[k] += 2*np.sum(gram*gates_gram*cross[k])/m**2
    dd2_memory = np.array([2*np.sum(C*cross[k])/m**2 for k in range(nc)])
    return dict(input_gram=gram.tolist(), covariance=C.tolist(),
                response_eigenvalues=np.linalg.eigvalsh(M0).tolist(),
                first_energies=e1.tolist(), first_accelerations=dd1.tolist(),
                second_energies=energy2.tolist(), second_accelerations=(dd2_A+dd2_memory).tolist(),
                second_readin=dd2_A.tolist(), second_memory=dd2_memory.tolist())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.exists():
        raise FileExistsError(args.output)
    sig = np.array(list(itertools.product([-1., 1.], repeat=2)))
    tetra = np.column_stack((sig[:, 0], sig[:, 1], sig[:, 0]*sig[:, 1]))
    chars4 = np.column_stack((np.ones(4), tetra)).T
    angles = 2*np.pi*np.arange(3)/3
    triangle = np.column_stack((np.cos(angles), np.sin(angles)))
    # The two contrast rows have mean square one and span the standard mode.
    chars3 = np.vstack((np.ones(3), np.sqrt(2)*np.cos(angles), np.sqrt(2)*np.sin(angles)))
    configs = [('triangle', triangle, chars3)]
    for name, scale in [('tetra', [1/3]*3), ('anisotropic', [.8,.1,.1]), ('small_factors', [.98,.01,.01])]:
        configs.append((name, tetra*np.sqrt(scale), chars4))
    result = dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), runs=[])
    for order1, order2 in [(31,21),(45,31)]:
        for name, points, chars in configs:
            run=dict(name=name, root_order=order1, second_order=order2, points=points.tolist(), chars=chars.tolist(),
                     result=calculate(points,chars,order1,order2))
            result['runs'].append(run)
            print(json.dumps(run), flush=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')


if __name__ == '__main__':
    main()
