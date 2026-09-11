"""Independent finite scalar-expression checks; no Gaussian law or training simulation.

All arrays below are supplied deterministic source coordinates. Their synthetic
means test identities, not probability limits or the theorem's tail constants.
Precommitted gates: source complex-step error <1e-10; atom split value/row
errors <1e-10; clock defect and derivative halve quadratically within 10%.
One fixed 4-node graph, plus a duplicate-name rewrite; no fitted parameters.
"""
from pathlib import Path
import json, hashlib, platform
import numpy as np

OUT=Path(__file__).resolve().parent
N=7; M=9; steps=np.array([.02,.013,.017,.011]); nt=len(steps)
u=np.array([[1.,0.],[.6,.8],[-.8,.6]])
p=np.array([.47,.53-1e-11,1e-11]); y=np.array([1.,-.7,.4])
g=np.array([[.2,-.4],[1.,.3],[-.8,.6],[2.,-1.],[.1,.7],[-1.1,.2],[.4,.9]])
xi=np.sin(np.arange(nt*3*M).reshape(nt,3,M)*.17)*.4
ze=np.cos(np.arange(nt*3*N).reshape(nt,3,N)*.13)*.3

def gate(x): return 1/np.cosh(x)**2
def curv(x): return -2*np.tanh(x)*gate(x)

def build(u,p,y,xi,ze):
    na=len(p); S=nt*na
    w=g.copy(); v=np.zeros((S,N,2)); c=np.zeros(M); C=np.zeros((S,M))
    H=[]; De=[]; Q=[]; V=[]; Va=[]; F=[]; D=[]; Ga=[]; Ws=[]; Cs=[]; Al=[]; Be=[]
    for k in range(nt):
        Ws.append(w.copy()); Cs.append(c.copy()); Va.append(v.copy())
        hk=np.tanh(w@u.T).T
        alpha=np.einsum('an,pnd,ad->ap',gate(w@u.T).T,v,u)/N
        fk=np.zeros((na,S));
        if k:
            oldh=np.array(H).reshape(k*na,N)
            fk[:,:k*na]=alpha[:,:k*na]+np.array(Ga).ravel()[None,:]*(hk@oldh.T/N)
        zk=xi[k].copy()
        if k: zk+=fk[:,:k*na]@np.array(De).reshape(k*na,M)
        uk=np.zeros((na,S,M))
        for a in range(na): uk[a,k*na+a,:]=1
        if k: uk+=np.einsum('aq,qpm->apm',fk[:,:k*na],np.array(V).reshape(k*na,S,M))
        de=c[None,:]*gate(zk)
        vk=gate(zk)[:,None,:]*C[None,:,:]+c[None,None,:]*curv(zk)[:,None,:]*uk
        beta=vk.mean(axis=2)
        dk=beta.copy()
        if k: dk[:,:k*na]+=np.array(Ga).ravel()[None,:]*(de@np.array(De).reshape(k*na,M).T/M)
        allh=np.concatenate([np.array(H).reshape(k*na,N),hk])
        qk=ze[k]+dk[:,:((k+1)*na)]@allh
        gam=-2*steps[k]*p*(np.mean(c[None,:]*np.tanh(zk),axis=1)-y)
        olddh=[]
        for j in range(k+1):
            wj=Ws[j]; vj=Va[j]
            olddh.append(gate(wj@u.T).T[:,None,:]*np.einsum('ad,pnd->apn',u,vj))
        dq=np.einsum('aq,qpn->apn',dk[:,:((k+1)*na)],np.array(olddh).reshape((k+1)*na,S,N))
        for a in range(na): dq[a,k*na+a,:]+=1
        local=np.einsum('ad,pnd->apn',u,v)
        v=v+np.einsum('a,ad,apn->pnd',gam,u,curv(w@u.T).T[:,None,:]*qk[:,None,:]*local+gate(w@u.T).T[:,None,:]*dq)
        w=w+np.einsum('a,an,ad->nd',gam,gate(w@u.T).T*qk,u)
        C=C+np.einsum('a,am,apm->pm',gam,gate(zk),uk)
        c=c+gam@np.tanh(zk)
        H.append(hk); De.append(de); Q.append(qk); V.append(vk); F.append(fk); D.append(dk); Ga.append(gam); Al.append(alpha); Be.append(beta)
    return dict(w=w,c=c,H=np.array(H),de=np.array(De),Q=np.array(Q),v=v,V=np.array(V),F=np.array(F),D=np.array(D),gamma=np.array(Ga),alpha=np.array(Al),beta=np.array(Be))

def replay(a,u,xi,ze):
    na=len(u); w=g.astype(complex); c=np.zeros(M,dtype=complex); H=[]; De=[]
    for k in range(nt):
        hk=np.tanh(w@u.T).T
        zk=xi[k].astype(complex).copy()
        if k: zk+=a['F'][k,:,:k*na]@np.array(De).reshape(k*na,M)
        de=c[None,:]*gate(zk)
        qk=ze[k]+a['D'][k,:,:((k+1)*na)]@np.concatenate([np.array(H).reshape(k*na,N),hk])
        w=w+np.einsum('a,an,ad->nd',a['gamma'][k],gate(w@u.T).T*qk,u)
        c=c+a['gamma'][k]@np.tanh(zk)
        H.append(hk); De.append(de)
    return w,np.array(De)

a=build(u,p,y,xi,ze)
h=1e-25; low=up=0.
for pulse in range(nt*3):
    zs=ze.astype(complex); zs.reshape(nt*3,N)[pulse]+=1j*h
    w,_=replay(a,u,xi,zs); low=max(low,float(np.max(np.abs(w.imag/h-a['v'][pulse]))))
    xs=xi.astype(complex); xs.reshape(nt*3,M)[pulse]+=1j*h
    _,ds=replay(a,u,xs,ze); up=max(up,float(np.max(np.abs(ds.imag/h-a['V'][:,:,pulse,:]))))
assert max(low,up)<1e-10
# The same atom/source is rewritten as two names carrying .2/.8 of its mass.
idx=np.array([0,0,1,2]); pp=np.array([.2*p[0],.8*p[0],p[1],p[2]])
b=build(u[idx],pp,y[idx],xi[:,idx],ze[:,idx])
value=max(float(np.max(abs(a['w']-b['w']))),float(np.max(abs(a['c']-b['c']))),float(np.max(abs(a['Q'][:,idx]-b['Q']))))
rows=0.
for k in range(nt):
    for ab,aa in enumerate(idx):
        for s in range(k):
            for old in range(3):
                cols=np.where(idx==old)[0]+4*s
                rows=max(rows,abs(float(b['beta'][k,ab,cols].sum()-a['beta'][k,aa,3*s+old])))
        rows=max(rows,abs(float(b['beta'][k,ab,k*4+ab]-a['beta'][k,aa,k*3+aa])))
assert max(value,rows)<1e-10
# Raw-to-clock defect and its held-b derivatives, independently differentiated.
def primitive(w): return w/2+np.sinh(2*w)/4
w=np.array([-2.,0.,1.]); bb=np.array([.3,-.7,1.2]); hs=[.02,.01,.005]
errs=[]; dwerrs=[]; dberrs=[]
for dt in hs:
    z=w+dt*bb*gate(w)
    errs.append(float(np.max(abs(primitive(z)-primitive(w)-dt*bb))))
    dwerrs.append(float(np.max(abs(np.cosh(z)**2*(1+dt*bb*curv(w))-np.cosh(w)**2))))
    dberrs.append(float(np.max(abs(dt*gate(w)*np.cosh(z)**2-dt))))
ratios=[[x[i]/x[i+1] for i in range(2)] for x in [errs,dwerrs,dberrs]]
assert all(3.6<v<4.4 for r in ratios for v in r)
result=dict(scope='deterministic scalar expression algebra; not probability or training',result='PASS',lower_source_complex_step_error=low,upper_source_complex_step_error=up,duplicate_atom_value_error=value,duplicate_atom_beta_aggregation_error=rows,tiny_atom_mass=float(p[-1]),clock_defects=errs,clock_w_derivative=dwerrs,clock_b_derivative=dberrs,quadratic_ratios=ratios,python=platform.python_version(),numpy=np.__version__,sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(OUT/'source_algebra_results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
