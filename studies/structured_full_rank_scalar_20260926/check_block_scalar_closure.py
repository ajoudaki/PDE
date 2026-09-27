"""Deterministic independent oracles for the representative-block closure."""
import block_scalar_closure as scalar
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import eval_legendre
import dense_compare as dense
import quick_block_compare as quick
from circle_tasks import directions


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    checks={}
    rng=np.random.default_rng(9241)
    pool=scalar.initial_pool(64,8,1)
    original=quick.initialize(64,1,'block8')
    Gfull=np.zeros((64,64))
    for b in range(8):Gfull[b*8:(b+1)*8,b*8:(b+1)*8]=pool['G'][b]
    for name,a,b in (('initial_w',pool['w'],original.w),('initial_c',pool['c'],original.c),
                     ('initial_G',Gfull,original.W)):
        assert np.array_equal(a,b);checks[name]=0.
    u=directions([-.3,.2,.9]);labels=np.array([-.4,.6,.3])
    layout,G,state=scalar.initialize(pool,[0,2,5],u,4)
    w,c,A,B,_=layout.unpack(state)
    c[:]=rng.normal(scale=.2,size=c.shape)
    A[:]=rng.normal(scale=.1,size=A.shape)
    B[:]+=rng.normal(scale=.1,size=B.shape)
    state[-1]=1.7
    W=np.zeros((layout.n,layout.n))
    for b in range(layout.q):W[b*8:(b+1)*8,b*8:(b+1)*8]=G[b]
    W-=2/(layout.m*layout.n*state[-1])*(A*layout.coefficients)@B.T
    oracle=dense.State(w.copy(),W,c.copy())
    field=rng.normal(size=(layout.n,7))
    for transpose in (False,True):
        actual=scalar.middle_action(layout,G,state,field,transpose)
        expected=(W.T if transpose else W)@field
        err=float(np.max(np.abs(actual-expected)));assert err<2e-12
        checks['transpose' if transpose else 'forward_action']=err
    left=rng.normal(size=field.shape)
    adj=abs(float(np.sum(left*scalar.middle_action(layout,G,state,field))-
                  np.sum(scalar.middle_action(layout,G,state,left,True)*field)))
    assert adj<2e-11;checks['adjoint_identity']=adj
    predictions=scalar.forward(layout,G,state,u)[0]
    checks['materialized_prediction']=float(np.max(np.abs(predictions-dense.forward(oracle,u).output)))
    assert checks['materialized_prediction']<2e-12
    velocity=scalar.rhs(layout,G,state,u,labels)
    dw,dc,dA,dB,dL=layout.unpack(velocity)
    expected=dense.rhs(oracle,u,labels)
    for name,a,b in (('canonical_wdot',dw,expected.w),('canonical_cdot',dc,expected.c)):
        checks[name]=float(np.max(np.abs(a-b)));assert checks[name]<2e-12
    assert np.linalg.norm(W[:8,8:16])>1e-6
    checks['nonzero_learned_off_block']=float(np.linalg.norm(W[:8,8:16]))
    # Independent defining Legendre integrals, including artificial prefix.
    L=scalar.Layout(1,1,1,6)
    initial=np.zeros(12);initial[6]=.3
    def memory_rhs(t,y):
        return np.concatenate((scalar.moment_rhs(L,y[:6].reshape(1,6),np.array([[np.cos(.7*t)]]),1.,1+t).ravel(),
                               scalar.moment_rhs(L,y[6:].reshape(1,6),np.array([[np.sin(t)+.3]]),1.,1+t).ravel()))
    result=solve_ivp(memory_rhs,(0.,2.3),initial,rtol=1e-11,atol=1e-13)
    nodes,weights=np.polynomial.legendre.leggauss(120)
    t=2.3;s=(nodes+1)*t/2;ts=weights*t/2
    prefix=(nodes+1)/2;pw=weights/2
    exact=[]
    for mode in range(6):
        exact.append(np.sum(ts*np.cos(.7*s)*eval_legendre(mode,2*(1+s)/(1+t)-1)))
    for mode in range(6):
        exact.append(.3*np.sum(pw*eval_legendre(mode,2*prefix/(1+t)-1))+
                     np.sum(ts*(np.sin(s)+.3)*eval_legendre(mode,2*(1+s)/(1+t)-1)))
    err=float(np.max(np.abs(result.y[:,-1]-exact)))
    assert err<1e-9;checks['defining_history_integrals']=err
    # Small deterministic endpoint refinement; passive circle queries use no test moments.
    u=directions([0.,np.pi/3]);labels=np.array([1.,-1.])
    pool=scalar.initial_pool(16,4,3)
    layout,G,state=scalar.initialize(pool,np.arange(4),u,4)
    x1,r1=scalar.integrate(layout,G,state,u,labels,rtol=1e-6,atol=1e-9,deadline_seconds=10,interrupt_seconds=12)
    x2,r2=scalar.integrate(layout,G,state,u,labels,rtol=1e-7,atol=1e-10,deadline_seconds=10,interrupt_seconds=12)
    assert r1['fitted'] and r2['fitted']
    a=2*np.pi*np.arange(128)/128
    pred1=scalar.predict(layout,G,x1,a);pred2=scalar.predict(layout,G,x2,a)
    err=float(np.sqrt(np.mean((pred1-pred2)**2)))
    assert err<1e-4;checks['small_endpoint_refinement_rms']=err
    checks['passive_oddness']=float(np.max(np.abs(pred1[:64]+pred1[64:])))
    assert checks['passive_oddness']<1e-12
    checks['dynamic_scalars']=layout.size
    assert layout.size==1+layout.n*(3+2*layout.m*layout.order)
    source=Path(__file__).resolve().parent
    report={'checks':checks,'passed':True,'sources':{name:hashlib.sha256((source/name).read_bytes()).hexdigest()
        for name in ('block_scalar_closure.py','check_block_scalar_closure.py','dense_compare.py','dense_wide_integrator.py')},
        'small_training_checks':2,'small_training_seconds':r1['training_seconds']+r2['training_seconds']}
    (args.output/'check.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
