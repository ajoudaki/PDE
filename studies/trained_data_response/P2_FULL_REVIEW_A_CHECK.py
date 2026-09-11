"""Reviewer A: fixed source-expression algebra, not trained trajectories."""
from pathlib import Path
import hashlib
import json
import platform
import numpy as np


def a(x):
    return 1/np.cosh(x)**2


def b(x):
    return -2*np.tanh(x)*a(x)


def main():
    # Three formal times, repeated directions, unequal masses, and an unused
    # zero-mass slot. Residuals and coefficient arrays stay frozen throughout.
    u = np.array([[1., 0.], [.6, .8], [.6, .8], [0., 1.]])
    mass = np.array([.4, .599999, .000001, 0.])
    step = np.array([.03, .017, .011])
    residual = np.array([[-.7, .2, .2, .1], [-.4, .3, .3, -.2],
                         [-.2, .1, .1, -.3]])
    gamma = -2*step[:, None]*mass*residual
    D = np.zeros((3, 4, 3, 4))
    F = np.zeros_like(D)
    for k in range(3):
        for j in range(4):
            D[k, j, k, j] = .1*(j+1)
            for s in range(k):
                D[k, j, s] = (.2-.03*j+.01*s)*step[s]*mass
                F[k, j, s] = (-.1+.04*j+.02*s)*step[s]*mass
    roots = np.array([[.2, -.3, -.3, 0.], [.4, .1, .1, 0.],
                      [-.2, .5, .5, 0.]])
    # Named slots remain distinct, even at equal numerical values.
    def lower(zeta, pulse=None):
        ws = [np.array([.3, -.8], dtype=zeta.dtype)]
        vs = [np.zeros(2, dtype=zeta.dtype)]
        hs = []
        for k in range(3):
            hs.append(np.tanh(u@ws[k]))
            Q = zeta[k].copy()
            dQ = np.zeros(4, dtype=zeta.dtype)
            for s in range(k+1):
                Q += D[k, :, s]@hs[s]
                dQ += D[k, :, s]@(a(u@ws[s])*(u@vs[s]))
            if pulse is not None and pulse[0] == k:
                dQ[pulse[1]] += 1
            ws.append(ws[k]+(gamma[k]*a(u@ws[k])*Q)@u)
            vs.append(vs[k]+(gamma[k]*(b(u@ws[k])*Q*(u@vs[k])
                                          +a(u@ws[k])*dQ))@u)
        return np.array(ws), np.array(vs)
    def upper(xi, pulse=None):
        c, cp = 0., 0.
        ds, dp = [], []
        for k in range(3):
            Z = xi[k].copy()
            Zp = np.zeros(4, dtype=xi.dtype)
            if pulse is not None and pulse[0] == k:
                Zp[pulse[1]] = 1
            for s in range(k):
                Z += F[k, :, s]@ds[s]
                Zp += F[k, :, s]@dp[s]
            ds.append(c*a(Z))
            dp.append(cp*a(Z)+c*b(Z)*Zp)
            c, cp = c+gamma[k]@np.tanh(Z), cp+gamma[k]@(a(Z)*Zp)
        return np.array(ds), np.array(dp)
    lower_errors, upper_errors, zero_mass_errors = [], [], []
    tiny = 1e-28
    for k in range(3):
        for j in range(4):
            pert = roots.astype(complex)
            pert[k, j] += 1j*tiny
            expected_lower = lower(roots, (k,j))[1]
            expected_upper = upper(roots, (k,j))[1]
            lower_errors.append(float(np.max(abs(lower(pert)[0].imag/tiny-expected_lower))))
            upper_errors.append(float(np.max(abs(upper(pert)[0].imag/tiny-expected_upper))))
            if mass[j] == 0:
                zero_mass_errors.append(float(np.max(abs(expected_lower))))
                zero_mass_errors.append(float(np.max(abs(expected_upper[k+1:]), initial=0)))
    assert max(lower_errors+upper_errors) < 1e-14
    assert max(zero_mass_errors) == 0
    # Direct raw-to-clock derivative, independently differentiated by complex step.
    w, h, velocity = .7, .02, -.4
    primitive = lambda z: z/2+np.sinh(2*z)/4
    defect = lambda z,v: primitive(z+h*v*a(z))-primitive(z)-h*v
    after = w+h*velocity*a(w)
    dw = (1+h*velocity*b(w))/a(after)-1/a(w)
    dv = h*a(w)/a(after)-h
    defects = [float(abs(defect(w+1j*tiny,velocity).imag/tiny-dw)),
               float(abs(defect(w,velocity+1j*tiny).imag/tiny-dv))]
    assert max(defects) < 1e-14
    result = dict(result='PASS', python=platform.python_version(), numpy=np.__version__,
                  lower_chain_max_error=max(lower_errors), upper_chain_max_error=max(upper_errors),
                  zero_mass_past_source_error=max(zero_mass_errors), clock_defect_errors=defects,
                  scope='Fixed formal source algebra; no source expectations, tail proof, or training certification',
                  sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
