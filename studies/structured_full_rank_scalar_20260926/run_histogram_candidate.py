"""Bounded genuine Eulerian-histogram test: one Gaussian-block circle datum.

Only fixed cell masses and L evolve in the tested model. Moving characteristic
quadrature is a separately identified reference, never a source for its RHS.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
import ctypes as ct
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time

import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.special import erf
import block_scalar_closure as population

GRIDS = {'coarse':(9,17,9,17,9), 'fine':(13,25,13,25,13)}
BOUNDS = (5.,6.,3.,4.,1.)  # g,x,a,c,b; a=-A, b=B/L.
ANGLES = 2*np.pi*np.arange(1024)/1024


def write(path,obj):
    Path(path).write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def rms(x,y):
    return float(np.sqrt(np.mean((x-y)**2)))


def gaussian_rule(order):
    nodes,weights=np.polynomial.hermite.hermgauss(order)
    return np.sqrt(2)*nodes,weights/np.sqrt(np.pi)


def folded_rule(order):
    nodes,weights=gaussian_rule(order)
    assert order%2==0
    return nodes[order//2:],2*weights[order//2:]


def fields(g,weights,state):
    n=len(g)
    x,a,c,b=state[:-1].reshape(4,n)
    h=np.tanh(x)
    S=np.dot(weights,b*h)
    z=g*h+2*a*S
    H=np.tanh(z)
    gate=1-H*H
    f=np.dot(weights,c*H)
    D=np.dot(weights,a*c*gate)
    return f,h,H,gate,S,D


def characteristic_rhs(g,weights,state,label=1.):
    n=len(g)
    x,a,c,b=state[:-1].reshape(4,n)
    L=state[-1]
    f,h,H,gate,S,D=fields(g,weights,state)
    r=f-label;rho=abs(r)
    result=np.empty_like(state)
    dx,da,dc,db=result[:-1].reshape(4,n)
    dx[:]=-2*r*(1-h*h)*(g*c*gate+2*b*D)
    da[:]=-r*c*gate
    dc[:]=-2*r*H
    db[:]=rho/L*(h-b)
    result[-1]=rho
    return result


def characteristic_predict(g,weights,state,angles,eta_order=64):
    eta,eta_w=gaussian_rule(eta_order)
    x,a,c,b=state[:-1].reshape(4,len(g))
    output=[]
    # The SAME eta enters both nonlinearities, preserving their dependence.
    for angle in angles:
        h=np.tanh(x[:,None]*np.cos(angle)+eta[None,:]*np.sin(angle))
        S=np.dot(weights*b,h@eta_w)
        H=np.tanh(g[:,None]*h+2*a[:,None]*S)
        output.append(np.dot(weights*c,H@eta_w))
    return np.asarray(output)


def run_reference(out,order):
    tick=time.monotonic()
    nodes,one_weights=folded_rule(order)
    gs,xs=np.meshgrid(nodes,nodes,indexing='ij')
    weights=np.outer(one_weights,one_weights).ravel()
    g=gs.ravel();n=len(g)
    initial=np.zeros(4*n+1)
    initial[:n]=xs.ravel()
    initial[3*n:4*n]=np.tanh(xs.ravel())
    initial[-1]=1.
    def function(t,state):
        if time.monotonic()-tick>50:
            raise TimeoutError('Reference exceeded fixed training budget')
        return characteristic_rhs(g,weights,state)
    def event(t,state):
        return (fields(g,weights,state)[0]-1)**2-.01
    event.terminal=True;event.direction=-1
    sol=solve_ivp(function,(0.,20.),initial,events=event,rtol=1e-9,atol=1e-11,
                  max_step=.1,first_step=.005)
    state=sol.y[:,-1]
    prediction=characteristic_predict(g,weights,state,ANGLES)
    pred32=characteristic_predict(g,weights,state,ANGLES,32)
    path=out/f'reference_GH{order}.npz'
    np.savez(path,g=g,weights=weights,initial=initial,state=state,angles=ANGLES,
             prediction=prediction,prediction_eta32=pred32,time=sol.t,
             train_prediction=np.asarray([fields(g,weights,v)[0] for v in sol.y.T]))
    row={'kind':'reference','gaussian_seed_order':order,'characteristics':n,
         'fitted':bool(len(sol.t_events[0])),'physical_time':float(sol.t[-1]),
         'train_mse':float((fields(g,weights,state)[0]-1)**2),
         'eta32_vs64_rms':rms(prediction,pred32),'nfev':sol.nfev,
         'total_seconds':time.monotonic()-tick,'data_file':path.name,'data_sha256':digest(path)}
    write(path.with_suffix('.json'),row)
    print(json.dumps(row),flush=True)
    return row,prediction


def coordinate_axes(shape):
    return [np.linspace(0,upper,count) for count,upper in zip(shape,BOUNDS)]


def initialize_histogram(shape):
    g,x,a,c,b=coordinate_axes(shape)
    gaussian=[]
    for axis in (g,x):
        edges=np.r_[0.,(axis[:-1]+axis[1:])/2,np.inf]
        gaussian.append(np.diff(erf(edges/np.sqrt(2))))
    p=np.zeros(shape,dtype=np.float64)
    for ix,xx in enumerate(x):
        position=np.tanh(xx)*(len(b)-1)
        lo=min(len(b)-2,int(position));fraction=position-lo
        p[:,ix,0,0,lo]+=gaussian[0]*gaussian[1][ix]*(1-fraction)
        p[:,ix,0,0,lo+1]+=gaussian[0]*gaussian[1][ix]*fraction
    assert abs(float(p.sum())-1)<1e-14
    return p.ravel()


PTR=ct.POINTER(ct.c_double)
def pointer(array):
    assert array.dtype==np.float64 and array.flags.c_contiguous
    return array.ctypes.data_as(PTR)


class Histogram:
    def __init__(self,library,shape,threads=8):
        self.lib=ct.CDLL(str(library));self.shape=tuple(shape)
        self.lib.hist_create.argtypes=[ct.c_int]*6;self.lib.hist_create.restype=ct.c_void_p
        self.lib.hist_free.argtypes=[ct.c_void_p]
        self.lib.hist_size.argtypes=[ct.c_void_p];self.lib.hist_size.restype=ct.c_size_t
        self.lib.hist_rhs.argtypes=[ct.c_void_p,PTR,ct.c_double,ct.c_double,PTR,PTR]
        self.lib.hist_integrate.argtypes=[ct.c_void_p,PTR,PTR,ct.c_double,ct.c_double,
                                         ct.c_double,ct.c_double,ct.c_double,PTR]
        self.lib.hist_predict.argtypes=[ct.c_void_p,PTR,ct.c_double,PTR,ct.c_int,
                                       PTR,PTR,ct.c_int,PTR]
        self.handle=self.lib.hist_create(*shape,threads)
        if not self.handle:raise RuntimeError('Histogram allocation failed')
        self.size=self.lib.hist_size(self.handle)
        assert self.size==int(np.prod(shape))

    def close(self):
        if self.handle:
            self.lib.hist_free(self.handle);self.handle=None

    def rhs(self,p,L=1.,label=1.):
        dp=np.empty_like(p);stats=np.empty(8)
        self.lib.hist_rhs(self.handle,pointer(p),L,label,pointer(dp),pointer(stats))
        return dp,stats

    def integrate(self,p,cfl=.7):
        L=np.array([1.]);stats=np.empty(12)
        self.lib.hist_integrate(self.handle,pointer(p),pointer(L),1.,.01,cfl,50.,20.,pointer(stats))
        return float(L[0]),stats

    def predict(self,p,L,angles=ANGLES,eta_order=64):
        eta,weights=gaussian_rule(eta_order)
        angles=np.ascontiguousarray(angles,dtype=np.float64)
        output=np.empty_like(angles)
        self.lib.hist_predict(self.handle,pointer(p),L,pointer(angles),len(angles),
                              pointer(eta),pointer(weights),len(eta),pointer(output))
        return output


def check_core(library,out):
    shape=(3,5,5,5,5)
    model=Histogram(library,shape,2)
    axes=coordinate_axes(shape)
    # One interior cell: the first moment of each transported coordinate must
    # equal the underlying canonical block velocity, with no taper active.
    p=np.zeros(model.size)
    index=(1,1,1,1,1);flat=np.ravel_multi_index(index,shape);p[flat]=1.
    g,x,a,c,b=[axis[i] for axis,i in zip(axes,index)]
    L=1.7
    state=np.array([x,a,c,b,L]);expected=characteristic_rhs(np.array([g]),np.ones(1),state)
    dp,stats=model.rhs(p,L)
    observed=[]
    for dimension in range(5):
        reshape=[1]*5;reshape[dimension]=shape[dimension]
        observed.append(float(np.sum(dp.reshape(shape)*axes[dimension].reshape(reshape))))
    desired=np.r_[0.,expected[0],expected[1],expected[2],expected[3]]
    error=float(np.max(np.abs(np.asarray(observed)-desired)))
    assert error<1e-11,(observed,desired)
    assert abs(float(dp.sum()))<1e-11
    assert (p+(.5/stats[4])*dp).min()>=-1e-14
    # Check the transformed velocity directly against the original H1 closure.
    layout=population.Layout(1,1,1,1)
    vector=np.zeros(layout.size)
    ww,cc,AA,BB,_=layout.unpack(vector)
    ww[:]=[[x,0.]];cc[:]=c;AA[:]=-a;BB[:]=L*b;vector[-1]=L
    velocity=population.rhs(layout,np.array([[[g]]]),vector,np.array([[1.,0.]]),np.array([1.]))
    dw,dc,dA,dB,_=layout.unpack(velocity)
    original=np.array([dw[0,0],-dA[0,0],dc[0],dB[0,0]/L-b*velocity[-1]/L,velocity[-1]])
    original_error=float(np.max(np.abs(original-expected)))
    assert original_error<1e-11
    angles=ANGLES[::64]
    predicted=model.predict(p,L,angles,32)
    reference=characteristic_predict(np.array([g]),np.ones(1),state,angles,32)
    query_error=float(np.max(np.abs(predicted-reference)))
    assert query_error<1e-11
    # A mixed law checks that reductions use the CURRENT masses.
    p=np.zeros(model.size)
    p[flat]=.4;p[np.ravel_multi_index((1,2,1,2,2),shape)]=.6
    dp,mixed=model.rhs(p,L)
    assert abs(float(dp.sum()))<1e-11
    assert (p+.5/mixed[4]*dp).min()>=-1e-14
    model.close()
    report={'mass_conservation':True,'positive_euler_step':True,
            'coordinate_velocity_max_error':error,'original_closure_velocity_error':original_error,
            'unseen_query_max_error':query_error}
    write(out/'checks.json',report);print(json.dumps(report),flush=True)


def run_histogram(library,out,name,shape,reference,cfl=.7):
    tick=time.monotonic()
    print(f'Start histogram {name}, {int(np.prod(shape))} masses, CFL={cfl}',flush=True)
    model=Histogram(library,shape)
    p=initialize_histogram(shape)
    L,stats=model.integrate(p,cfl)
    prediction=model.predict(p,L)
    prediction32=model.predict(p,L,eta_order=32)
    path=out/f'histogram_{name}.npz'
    np.savez(path,p=p,L=L,shape=shape,bounds=BOUNDS,angles=ANGLES,
             prediction=prediction,prediction_eta32=prediction32,stats=stats)
    model.close()
    row={'kind':'histogram','name':name,'shape':shape,'masses':len(p),'dynamic_scalars':len(p)+1,
         'cfl':cfl,'fitted':int(stats[0])==0,'stop_reason':int(stats[0]),
         'physical_time':float(stats[1]),'train_mse':float(stats[2]),'steps':int(stats[3]),
         'training_seconds':float(stats[4]),'mass':float(stats[5]),'minimum_mass':float(stats[6]),
         'maximum_taper_zone_mass':float(stats[7]),'maximum_loss_rise':float(stats[8]),
         'maximum_exit_rate':float(stats[9]),'last_step':float(stats[10]),'clock':L,
         'rms_vs_population_reference':rms(prediction,reference),
         'eta32_vs64_rms':rms(prediction,prediction32),
         'circle_quadrature_change':abs(rms(prediction,reference)-rms(prediction[::2],reference[::2])),
         'total_seconds':time.monotonic()-tick,'data_file':path.name,'data_sha256':digest(path)}
    write(path.with_suffix('.json'),row)
    print(json.dumps(row),flush=True)
    return row,prediction


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();out=args.output.resolve();out.mkdir(parents=True,exist_ok=False)
    source=Path(__file__).resolve().parent
    snapshot=out/'source_snapshot';snapshot.mkdir()
    names=('run_histogram_candidate.py','histogram_one_input.cpp','block_scalar_closure.py',
           'dense_compare.py','dense_wide_integrator.py')
    for name in names:shutil.copyfile(source/name,snapshot/name)
    command=['g++','-O3','-std=c++17','-fopenmp','-shared','-fPIC',str(source/'histogram_one_input.cpp'),
             '-o',str(out/'histogram_one_input.so')]
    subprocess.run(command,check=True,capture_output=True)
    manifest={'task':'single_cos1','training_angles':[0.],'labels':[1.],
        'k':1,'memory_order':1,'initial_readout':0.,'grid_shapes':GRIDS,'bounds':BOUNDS,
        'target_mse':.01,'cfl':.7,'training_deadline_seconds':50,'total_run_ceiling_seconds':60,
        'threads':8,'gaussian_seed_orders':[48,80,128],'test_angles':len(ANGLES),'eta_order':64,
        'sources':{n:digest(source/n) for n in names},'library_sha256':digest(out/'histogram_one_input.so'),
        'compile_command':command,'command':sys.argv,'python':platform.python_version(),
        'numpy':np.__version__,'scipy':scipy.__version__,'machine':platform.platform(),
        'head':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()}
    write(out/'manifest.json',manifest)
    check_core(out/'histogram_one_input.so',out)
    rows=[]
    low,p_low=run_reference(out,48);rows.append(low)
    high,p_ref=run_reference(out,80);rows.append(high)
    reference_error=rms(p_low,p_ref)
    if reference_error>.0005:
        higher,p_higher=run_reference(out,128);rows.append(higher)
        reference_error=rms(p_ref,p_higher);p_ref=p_higher;high=higher
    write(out/'reference_check.json',{'selected_order':high['gaussian_seed_order'],
          'circle_rms_difference':reference_error,'passed':reference_error<=.0005,
          'eta_quadrature_passed':high['eta32_vs64_rms']<=.0005})
    write(out/'results.json',rows)
    if not high['fitted'] or reference_error>.0005:
        write(out/'decision.json',{'passed':False,'reason':'reference unresolved; no histogram training'})
        return
    coarse,p_coarse=run_histogram(out/'histogram_one_input.so',out,'coarse',GRIDS['coarse'],p_ref)
    rows.append(coarse);write(out/'results.json',rows)
    fine,p_fine=run_histogram(out/'histogram_one_input.so',out,'fine',GRIDS['fine'],p_ref)
    rows.append(fine);write(out/'results.json',rows)
    refinement=None
    if fine['fitted'] and fine['rms_vs_population_reference']<=.025:
        refined,p_refined=run_histogram(out/'histogram_one_input.so',out,'fine_half_cfl',GRIDS['fine'],p_ref,.35)
        rows.append(refined);write(out/'results.json',rows)
        refinement={'rms_difference':rms(p_fine,p_refined),'both_fitted':fine['fitted'] and refined['fitted']}
        refinement['passed']=refinement['both_fitted'] and refinement['rms_difference']<=.002
        write(out/'refinement.json',refinement)
    hist=[r for r in rows if r['kind']=='histogram']
    gates={'both_resolutions_fitted':coarse['fitted'] and fine['fitted'],
        'fine_rms_at_most_001':fine['rms_vs_population_reference']<=.01,
        'no_resolved_worsening':fine['rms_vs_population_reference']<=coarse['rms_vs_population_reference']+.002,
        'mass_and_positivity':all(abs(r['mass']-1)<=1e-10 and r['minimum_mass']>=-1e-14 for r in hist),
        'taper_mass_below_001':all(r['maximum_taper_zone_mass']<=.001 for r in hist),
        'passive_quadrature':all(r['eta32_vs64_rms']<=.0005 for r in rows),
        'circle_quadrature':all(r['circle_quadrature_change']<=.0001 for r in hist),
        'run_budget':all(r['total_seconds']<=60 for r in rows),
        'temporal_refinement':refinement is not None and refinement['passed']}
    decision={'passed':all(gates.values()),'gates':gates,
              'next_action':'pair_cos1 feasibility/protocol' if all(gates.values()) else 'stop; no further tasks'}
    write(out/'decision.json',decision)
    print(json.dumps(decision),flush=True)


if __name__=='__main__':main()
