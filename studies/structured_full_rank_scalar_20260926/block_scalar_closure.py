"""Moving representative Gaussian blocks on top of the Legendre memory closure.

All runtime arrays depend on q,k,m,P, never on an omitted source width.
Every learned interaction is evaluated through current moment contractions.
No neuron dictionary or dense learned matrix is used in the RHS.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'

from dataclasses import dataclass
import signal
import time

import numpy as np
from scipy.optimize import brentq

from dense_compare import _sech_squared
from dense_wide_integrator import _BlockRK45


@dataclass
class Layout:
    q: int
    k: int
    m: int
    order: int
    d: int = 2

    def __post_init__(self):
        if min(self.q, self.k, self.m, self.order, self.d) < 1:
            raise ValueError('Positive dimensions required')
        self.n = self.q*self.k
        sizes = (self.n*self.d, self.n, self.n*self.order*self.m,
                 self.n*self.order*self.m, 1)
        edges = np.cumsum((0,)+sizes)
        self.slices = tuple(slice(int(a), int(b)) for a,b in zip(edges[:-1],edges[1:]))
        self.size = int(edges[-1])
        self.coefficients = np.repeat(2*np.arange(self.order)+1, self.m)

    def unpack(self, vector):
        w,c,A,B,L = (vector[s] for s in self.slices)
        return (w.reshape(self.n,self.d), c,
                A.reshape(self.n,self.order*self.m),
                B.reshape(self.n,self.order*self.m), float(L[0]))


def initial_pool(width=2048, k=16, seed=1):
    """Same streams/values as quick_block_compare.initialize, without dense W."""
    if width % k:
        raise ValueError('Width must be divisible by block size')
    rng = lambda stream: np.random.default_rng(np.random.SeedSequence([seed,stream]))
    return {'w': rng(1).standard_normal((width,2)),
            'c': rng(2).standard_normal(width)/width,
            'G': rng(300+k).standard_normal((width//k,k,k))/np.sqrt(k)}


def initialize(pool, indices, u, order):
    indices = np.asarray(indices,dtype=int)
    k = pool['G'].shape[1]
    if len(np.unique(indices)) != len(indices):
        raise ValueError('This driver uses subsets without replacement')
    layout = Layout(len(indices),k,len(u),order,u.shape[1])
    vector = np.zeros(layout.size)
    w,c,A,B,_ = layout.unpack(vector)
    w[:] = pool['w'].reshape(-1,k,u.shape[1])[indices].reshape(w.shape)
    c[:] = pool['c'].reshape(-1,k)[indices].reshape(c.shape)
    B[:,:len(u)] = np.tanh(w@u.T)
    vector[-1] = 1.
    G = np.ascontiguousarray(pool['G'][indices])
    return layout, G, vector


def initial_action(G, field, transpose=False):
    q,k,_ = G.shape
    blocks = field.reshape(q,k,-1)
    matrix = G.transpose(0,2,1) if transpose else G
    return (matrix@blocks).reshape(q*k,-1)


def middle_action(layout, G, vector, field, transpose=False):
    _,_,A,B,L = layout.unpack(vector)
    left,right = (B,A) if transpose else (A,B)
    overlaps = (right.T@field)/layout.n
    overlaps *= layout.coefficients[:,None]
    return initial_action(G,field,transpose)-2/(layout.m*L)*(left@overlaps)


def forward(layout, G, vector, u):
    w,c,_,_,_ = layout.unpack(vector)
    z1 = w@u.T
    h1 = np.tanh(z1)
    z2 = middle_action(layout,G,vector,h1)
    h2 = np.tanh(z2)
    prediction = (c@h2)/layout.n
    return prediction,z1,h1,z2,h2


def moment_rhs(layout,moments,source,rho,L):
    p=np.arange(layout.order)[None,:,None]
    shaped=moments.reshape(layout.n,layout.order,layout.m)
    weighted=(2*p+1)*shaped
    prefix=np.cumsum(weighted,axis=1)-weighted
    return (source[:,None,:]-rho/L*(p*shaped+prefix)).reshape(moments.shape)


def rhs(layout, G, vector, u, labels):
    _,c,A,B,L = layout.unpack(vector)
    pred,z1,h1,z2,h2 = forward(layout,G,vector,u)
    r = pred-labels
    rho = float(np.sqrt(np.mean(r*r)))
    delta2 = c[:,None]*_sech_squared(z2)
    delta1 = _sech_squared(z1)*middle_action(layout,G,vector,delta2,True)
    result = np.empty_like(vector)
    dw,dc,dA,dB,_ = layout.unpack(result)
    dw[:] = -2/layout.m*((delta1*r)@u)
    dc[:] = -2/layout.m*(h2@r)
    for moments,derivative,source in ((A,dA,delta2*r),(B,dB,rho*h1)):
        derivative[:] = moment_rhs(layout,moments,source,rho,L)
    result[-1] = rho
    return result


def predict(layout,G,vector,angles,batch=128):
    angles=np.asarray(angles)
    u=np.column_stack((np.cos(angles),np.sin(angles)))
    return np.concatenate([forward(layout,G,vector,u[j:j+batch])[0]
                           for j in range(0,len(u),batch)])


class _BudgetReached(Exception):
    pass


def integrate(layout,G,initial,u,labels,target=.01,rtol=1e-5,atol=1e-8,
              deadline_seconds=50.,interrupt_seconds=55.,time_cap=3000.):
    """Full autonomous state, blockwise RK norm, accepted-state checkpoint."""
    started=time.monotonic()
    values=initial.copy()
    mse_at=lambda y: float(np.mean((forward(layout,G,y,u)[0]-labels)**2))
    mse=mse_at(values)
    t=0.; reason='time_cap'; steps=0; max_rise=0.; min_clock=values[-1]
    history=[(t,mse,values[-1])]
    nfev=0; solver=None; bracket=None; last_progress=started
    def function(at,y):
        if time.monotonic()-started>=deadline_seconds:
            raise _BudgetReached()
        return rhs(layout,G,y,u,labels)
    def alarm(signum,frame):
        raise _BudgetReached()
    old=signal.signal(signal.SIGALRM,alarm)
    signal.setitimer(signal.ITIMER_REAL,interrupt_seconds)
    try:
        if mse<=target:
            reason='target'
        else:
            solver=_BlockRK45(function,0.,values,time_cap,rtol=rtol,atol=atol,
                first_step=.01,max_step=10.,block_slices=layout.slices)
            while solver.status=='running':
                old_t,old_mse=t,mse
                solver.step()
                if solver.status=='failed':
                    reason='solver_failed';break
                trial=mse_at(solver.y)
                if not np.isfinite(trial) or not np.all(np.isfinite(solver.y)):
                    reason='nonfinite';break
                min_clock=min(min_clock,float(solver.y[-1]))
                max_rise=max(max_rise,trial-old_mse)
                if trial<=target:
                    interp=solver.dense_output()
                    bracket=(old_t,float(solver.t))
                    tol=max(1e-12,8*np.finfo(float).eps*max(1.,solver.t))
                    root=brentq(lambda at:mse_at(interp(at))-target,*bracket,
                                xtol=tol,rtol=8*np.finfo(float).eps)
                    candidate=interp(root); trial=mse_at(candidate)
                    for _ in range(4):
                        if trial<=target:break
                        root=min(solver.t,root+max(tol,1e-9*(solver.t-old_t)))
                        candidate=interp(root);trial=mse_at(candidate)
                    if trial>target or abs(trial-target)>max(1e-12,1e-6*target):
                        reason='event_refinement_failed';break
                    values,t,mse=candidate,float(root),trial
                    reason='target'
                else:
                    values,t,mse=solver.y,float(solver.t),trial
                steps+=1
                history.append((t,mse,float(values[-1])))
                now=time.monotonic()
                if now-last_progress>=10:
                    print(f'progress q={layout.q} P={layout.order} MSE={mse:.6g} seconds={now-started:.1f}',flush=True)
                    last_progress=now
                if reason=='target':break
    except _BudgetReached:
        reason='deadline'
    finally:
        signal.setitimer(signal.ITIMER_REAL,0.)
        signal.signal(signal.SIGALRM,old)
        if solver is not None:nfev=solver.nfev
    return values,{'stop_reason':reason,'fitted':reason=='target' and mse<=target*(1+1e-7),
        'train_mse':mse,'physical_time':t,'nsteps':steps,'nfev':nfev,
        'max_loss_rise':max_rise,'min_clock':min_clock,'history':np.asarray(history),
        'training_seconds':time.monotonic()-started,'target_bracket':bracket,
        'rtol':rtol,'atol':atol,'first_step':.01,'max_step':10.}
