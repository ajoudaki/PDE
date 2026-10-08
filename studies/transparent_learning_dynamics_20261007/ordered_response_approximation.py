"""Initialization-only cubic control response, including a passive input.

Imports the bounded Gaussian integrator (60 CPU seconds, 512 MiB).
No dense or completed population trajectory is read by this program.
"""
import hashlib
import json
import resource
import time
from pathlib import Path

from passive_clock_quadrature import gaussian_rule, lower_moments, upper_moments
import numpy as np
from scipy.integrate import solve_ivp


DEST=Path('data/generated/transparent_learning_dynamics_20261007/unequal_residuals_v1/approximation')


def coefficients(order,rotated=False):
    nodes,weights=gaussian_rule(order)
    h=np.tanh(nodes);g=1-h*h
    sigma2=weights@(h*h);qx=weights@(g*g);taux=weights@(h*h*g*g)
    hz=np.tanh(np.sqrt(sigma2)*nodes);gz=1-hz*hz
    nu=weights@(hz*hz);alpha=weights@gz;beta=weights@(gz*gz);tau=weights@(hz*hz*gz*gz)
    r0=3*beta-2*alpha
    c1,gg,gghh=lower_moments(nodes,weights,rotated)
    np.fill_diagonal(c1,sigma2);c1[0,1]=c1[1,0]=0.
    c2,g2g2,second_h,fourth,covariance=upper_moments(nodes,weights,c1,rotated,time.monotonic()+50)
    v=np.array([[1.,0.],[0.,1.],[2/np.sqrt(5),1/np.sqrt(5)]])
    s=v@v.T
    rd=np.zeros((2,2,3))
    for j in range(2):
        for b in range(2):rd[j,b,b]=r0 if j==b else alpha**2
    rpsi=np.zeros((3,3,3))
    for a in range(3):
        for q in range(3):
            rpsi[a,q,a]+=second_h[a,q]
            rpsi[a,q,q]+=g2g2[a,q]
    m1=np.zeros((3,3,2,2));m2=np.zeros_like(m1)
    for a in range(3):
        for q in range(3):
            for j in range(2):
                for b in range(2):
                    m1[a,q,j,b]=s[a,j]*np.dot(rd[j,b],gghh[a,j,q,:])
                    m2[a,q,j,b]=(c1[a,j]+s[a,j]*gg[a,j])*fourth[a,q,j,b]+s[a,j]*np.einsum('c,d,cd->',rd[j,b],rpsi[a,q],gghh[a,j])
    lam=(sigma2+qx)*tau+r0*r0*taux
    mu=(sigma2+qx)*nu*beta+sigma2*qx*alpha**4
    expected=np.zeros((2,2,2,2))
    expected[0,0,0,0]=expected[1,1,1,1]=lam
    expected[0,1,0,1]=expected[1,0,1,0]=mu
    return dict(c1=c1,c2=c2,m1=m1,m2=m2,
                constants=np.array([nu,lam,mu]),
                training_tensor_error=np.max(abs(expected-m2[:2,:2])),
                gaussian_covariance_error=np.max(abs(covariance-c1)))


def ordered(u,area):
    out=np.outer(u,u)/2
    out[0,1]+=area/2;out[1,0]-=area/2
    return out


def grams(coef,u,area):
    i=ordered(u,area)
    return [coef[key]+np.einsum('jb,aqjb->aq',i,coef[tensor]+coef[tensor].transpose(1,0,2,3))
            for key,tensor in (('c1','m1'),('c2','m2'))]


def potential(coef,u):
    m=coef['m2']
    return coef['c2'][:,:2]@u+np.einsum('q,j,b,aqjb->a',u,u,u,
                  .5*m[:,:2]+m[:2].transpose(1,0,2,3)/6)


def response_kernel(coef,u,area):
    m=coef['m2'];i=ordered(u,area)
    return coef['c2'][:,:2]+np.einsum('jb,aqjb->aq',i,
                 m[:,:2]+m[:2].transpose(1,0,2,3))+np.einsum('d,b,adqb->aq',u,u,m[:,:2])


def integrate(coef,model,labels=(.6,-.3),rtol=1e-10):
    y=np.array(labels)
    def rhs(t,state):
        u=state[:2]
        if model=='potential':return y-potential(coef,u)[:2]
        c=y-state[3:5]
        area_dot=c[0]*u[1]-c[1]*u[0]
        return np.concatenate([c,[area_dot],response_kernel(coef,u,state[2])@c])
    times=np.linspace(0,24,241)
    sol=solve_ivp(rhs,(0,24),np.zeros(2 if model=='potential' else 6),
                  t_eval=times,rtol=rtol,atol=rtol/100)
    assert sol.success
    state=sol.y.T
    if model=='potential':
        f=np.array([potential(coef,u) for u in state])
        # Radial reconstruction discards area even though its closed path can turn.
        area=np.zeros(len(times))
    else:f=state[:,3:];area=state[:,2]
    cg=np.array([grams(coef,u,a) for u,a in zip(state[:,:2],area)])
    return dict(time=times,u=state[:,:2],f=f,area=area,c1=cg[:,0],c2=cg[:,1])


def main():
    DEST.mkdir(parents=True,exist_ok=False)
    start=time.perf_counter()
    versions=[coefficients(order) for order in (40,64,96)]
    rotated=coefficients(96,True)
    final=versions[-1]
    errors={key:float(np.max(abs(versions[-1][key]-versions[-2][key])))
            for key in ('c1','c2','m1','m2','constants')}
    rotation={key:float(np.max(abs(final[key]-rotated[key]))) for key in errors}
    np.savez_compressed(DEST/'coefficients.npz',**final)
    comparisons={}
    for model in ('potential','ordered'):
        result=integrate(final,model)
        refined=integrate(final,model,rtol=1e-12)
        comparisons[model]=dict(final_f=result['f'][-1].tolist(),
                               final_area=float(result['area'][-1]),
                               solver_refinement=float(np.max(abs(result['f']-refined['f']))))
        np.savez_compressed(DEST/f'{model}.npz',**result)
    # Recover the independent phase-1 symmetric cubic coefficient and closure.
    u=np.array([.17,-.12]);nu,lam,mu=final['constants']
    expected=np.array([[nu+2*lam*u[0]**2+mu*u[1]**2,mu*u[0]*u[1]],
                       [mu*u[0]*u[1],nu+mu*u[0]**2+2*lam*u[1]**2]])
    kernel_error=float(np.max(abs(response_kernel(final,u,.07)[:2]-expected)))
    files=[Path(__file__),Path(__file__).with_name('passive_clock_quadrature.py')]
    summary=dict(quadrature_order=96,refinement_64_to_96=errors,rotation_96=rotation,
                 constants=dict(nu=float(nu),lambda_=float(lam),mu=float(mu)),
                 training_tensor_error=float(final['training_tensor_error']),
                 training_kernel_identity_error=kernel_error,models=comparisons,
                 wall_seconds=time.perf_counter()-start,
                 peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                 source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files})
    (DEST/'record.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
