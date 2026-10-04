"""Fixed CPU check for the initialized, weak-second-layer orientation identity."""
import os
for name in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from scipy.special import roots_hermitenorm
from reuse_check import hadamard, quarter_circle


def moments(order):
    z, weight = roots_hermitenorm(order)
    t = np.tanh(z)**2
    weight = weight/np.sqrt(2*np.pi)
    return np.array([weight@t, weight@(1-t)**4, weight@((1-t)**4*t)])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    q256, q512 = moments(256), moments(512)
    quadrature_error = float(np.max(np.abs(q256-q512)))
    if quadrature_error > 1e-8:
        raise RuntimeError(('quadrature', quadrature_error))
    nu, b, c = map(float, q512)
    n, count = 256, 8192
    singular = quarter_circle(n)
    mu4 = float(np.mean(singular**4))
    rng = np.random.default_rng(20261002)
    h = np.tanh(rng.standard_normal((count,n)))
    derivative_squared = (1-h*h)**2
    forward = {'mix': lambda x: hadamard(hadamard(x)*singular),
               'unmix': lambda x: hadamard(x*singular)}
    transpose = {'mix': forward['mix'],
                 'unmix': lambda x: hadamard(x)*singular}
    matrices = {key: func(np.eye(n)).T for key,func in forward.items()}
    covariance_error = float(np.max(np.abs(
        matrices['mix']@matrices['mix'].T-matrices['unmix']@matrices['unmix'].T)))
    probe = rng.standard_normal((32,n))
    paired_z = [forward['mix'](hadamard(probe)), forward['unmix'](probe)]
    energy = [np.sum(transpose[key](np.tanh(z))**2,axis=1)
              for key,z in zip(('mix','unmix'),paired_z)]
    probe_error = float(np.max(np.abs(energy[0]-energy[1]))/np.max(energy[1]))
    if max(covariance_error,probe_error)>1e-12:
        raise RuntimeError(('matched covariance/probe oracle',covariance_error,probe_error))
    rows, arrays = [], {}
    for epsilon in (0.,.1,.3,1.):
        values = {}
        for key in ('mix','unmix'):
            z = forward[key](h)
            if epsilon:
                g = np.tanh(epsilon*z)
                response = g*(1-g*g)/epsilon
            else:
                response = z
            values[key] = np.mean((derivative_squared*transpose[key](response))**2,axis=1)
            arrays[f'{key}_{epsilon:g}'] = values[key]
        diff = values['unmix']-values['mix']
        rows.append(dict(epsilon=epsilon,
                         mean={key:float(val.mean()) for key,val in values.items()},
                         standard_error={key:float(val.std(ddof=1)/np.sqrt(count))
                                         for key,val in values.items()},
                         paired_gap=float(diff.mean()),
                         paired_standard_error=float(diff.std(ddof=1)/np.sqrt(count))))
    prediction = dict(mix=c+(mu4-1)*nu*b,unmix=mu4*c,gap=(mu4-1)*(c-nu*b))
    linear_agreement = all(abs(rows[0]['mean'][key]-prediction[key])
                           <=4*rows[0]['standard_error'][key] for key in ('mix','unmix'))
    source = Path(__file__)
    inputs = [source, source.with_name('INITIAL_ACCELERATION.md'), source.with_name('reuse_check.py')]
    result = dict(n=n,count=count,seed=20261002,nu=nu,b=b,c=c,mu4=mu4,
                  quadrature_error=quadrature_error,covariance_error=covariance_error,
                  matched_gaussian_probe_error=probe_error,linear_prediction=prediction,
                  linear_agreement=linear_agreement,rows=rows,seconds=time.monotonic()-started,
                  numpy=np.__version__,source_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest()
                                                    for p in inputs},
                  scope='Initialized acceleration; epsilon=1 descriptive; no fitted-performance claim')
    np.savez(args.out/'per_initialization.npz',**arrays)
    (args.out/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    if not linear_agreement:
        raise RuntimeError('analytic expectation outside fixed four-SE check')


if __name__ == '__main__':
    main()
