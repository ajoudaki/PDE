"""Independent supplied-state finite-difference and API checks; no training."""
import sys, resource
from pathlib import Path
import numpy as np
from pde import ARCTAN, forward, gd_step, initialize, kernel, loss
from pde.finite_network import Activation, Parameters, flow_velocity, loss_gradients, kernel_blocks
resource.setrlimit(resource.RLIMIT_CPU,(120,120))
rng=np.random.default_rng(73109)
acts=(Activation("softplus",lambda z:np.logaddexp(0,z),lambda z:1/(1+np.exp(-z))),Activation("oscillatory",lambda z:z+.4*np.sin(z),lambda z:1+.4*np.cos(z)),Activation("nonodd",lambda z:.3+np.sin(z),np.cos),Activation("flat_c11",lambda z:np.where(z<=0,0,np.where(z<1,z*z/2,z-.5)),lambda z:np.clip(z,0,1)))
geometries=(np.eye(2),np.array([[1,.6],[0,.8]]),np.array([[1,-1],[0,0]]))
n=5
state=Parameters((rng.normal(size=(n,2)),rng.normal(size=(n,n))/np.sqrt(n)),rng.normal(size=n)/n)
kappas=np.array([.7,1.3,1.9]); labels=np.array([1.,-.7]); eps=1e-6
max_gradient_error=max_flow_error=max_kernel_error=0.
for phi in acts:
 for geo in geometries:
  X=np.sqrt(2)*geo
  grad=loss_gradients(state,X,labels,phi)
  vel=flow_velocity(state,X,labels,phi,kappas=kappas)
  blocks=(*state.weights,state.readout); grads=(*grad.weights,grad.readout); velocities=(*vel.weights,vel.readout)
  D=(n*kappas[0],kappas[1],n*kappas[2])
  expected=[]
  for b,block in enumerate(blocks):
   J=np.empty((labels.size,block.size)); numeric=np.empty_like(block)
   for j in range(block.size):
    pos=[v.copy() for v in blocks]; neg=[v.copy() for v in blocks]
    pos[b].flat[j]+=eps; neg[b].flat[j]-=eps
    pp=Parameters(tuple(pos[:-1]),pos[-1]); pn=Parameters(tuple(neg[:-1]),neg[-1])
    J[:,j]=(forward(pp,X,phi).output-forward(pn,X,phi).output)/(2*eps)
    numeric.flat[j]=(loss(pp,X,labels,phi)-loss(pn,X,labels,phi))/(2*eps)
   max_gradient_error=max(max_gradient_error,float(np.max(np.abs(numeric-grads[b]))))
   np.testing.assert_allclose(numeric,grads[b],atol=3e-8,rtol=3e-6)
   max_flow_error=max(max_flow_error,float(np.max(np.abs(velocities[b]+D[b]*numeric))))
   np.testing.assert_allclose(velocities[b],-D[b]*numeric,atol=2e-7,rtol=3e-6)
   expected.append(D[b]*(J@J.T))
  actual=kernel_blocks(state,X,phi,kappas=kappas)
  max_kernel_error=max(max_kernel_error,float(np.max(np.abs(actual-np.array(expected)))))
  np.testing.assert_allclose(actual,expected,atol=2e-8,rtol=3e-6)
print("12 supplied-state activation/geometry combinations passed; all raw blocks checked.")
print("max_gradient_abs_error",max_gradient_error)
print("max_flow_abs_error",max_flow_error)
print("max_kernel_abs_error",max_kernel_error)
X=np.sqrt(2.)*np.array([[1.,.6,-1.],[0.,.8,0.]])
y=np.array([1.,-.5,-1.]); theta=initialize(width=8,depth=3,input_dimension=2,seed=42)
print("guide_output",forward(theta,X,ARCTAN).output)
print("guide_kernel",kernel(theta,X,ARCTAN))
next_theta=gd_step(theta,X,y,eta=.01,activation=ARCTAN)
print("guide_losses",loss(theta,X,y,ARCTAN),loss(next_theta,X,y,ARCTAN))
print("cpu_seconds",resource.getrusage(resource.RUSAGE_SELF).ru_utime+resource.getrusage(resource.RUSAGE_SELF).ru_stime)
