"""Independent finite CPU/metric and CUDA checks; no retained arrays required."""
import os
from pathlib import Path
import tempfile
import unittest

import numpy as np
try:
    import torch
except ImportError:
    torch = None

from pde import observable_solver as cpu
if torch is not None:
    from pde import observable_torch_circle as gpu


@unittest.skipIf(torch is None,'optional Torch dependency unavailable')
class CircleTests(unittest.TestCase):
    def setUp(self):
        torch.set_num_threads(1)
        self.device = os.environ.get('CIRCLE_TEST_DEVICE','cpu')
        if self.device.startswith('cuda') and not torch.cuda.is_available():
            self.fail('requested CUDA validation has no CUDA device')
        angles = np.array([.1,.5,1.2,2.0])
        self.u = np.column_stack((np.cos(angles),np.sin(angles)))
        self.y = np.array([1.,-.3,.2,-.7])
        self.p = np.array([.1,.2,.3,.4])
        self.data = cpu.DataLaw(self.u,self.y,self.p).validate(cpu.Arithmetic())
        self.tdata = gpu.data_law(self.u,self.y,self.p,device=self.device)

    def fixture(self,order):
        state = cpu.initialize(order,initialization_nodes=64,population_nodes=32)
        rng = np.random.default_rng(7200+order)
        state.w += .05*rng.standard_normal(state.w.shape)
        state.c[:] = .2*rng.standard_normal(state.c.shape)
        state.M += .01*rng.standard_normal(state.M.shape)
        return state,gpu.from_cpu(state,device=self.device)

    def close(self,a,b,tol=2e-11):
        if isinstance(b,torch.Tensor): b=b.detach().cpu().numpy()
        np.testing.assert_allclose(a,b,rtol=tol,atol=tol)

    def test_all_orders_initialization_fields_rhs_heun(self):
        for order in (1,3,5):
            initial = gpu.initialize(order,initialization_nodes=64,population_nodes=32,device=self.device)
            ref = cpu.initialize(order,initialization_nodes=64,population_nodes=32)
            for key in gpu.KEYS: self.close(getattr(ref,key),getattr(initial,key),tol=0)
            self.assertEqual(initial.M.shape, {1:(3,5),3:(10,35),5:(21,128)}[order])
            state,tstate = self.fixture(order)
            old = tstate.copy()
            values = gpu.fields(tstate,self.u)
            for key,value in cpu._fields(state,self.u).items(): self.close(value,values[key])
            for a,b in zip(cpu.rhs(state,self.data,block_size=3),gpu.rhs(tstate,self.tdata,block_size=3)):
                self.close(a,b)
            expected = cpu.evolve(state,self.data,steps=4,step_size=.01,block_size=3)
            actual = gpu.evolve(tstate,self.tdata,steps=4,step_size=.01,block_size=3)
            for key in gpu.KEYS:
                self.close(getattr(expected,key),getattr(actual,key))
                self.assertTrue(torch.equal(getattr(old,key),getattr(tstate,key)))
            self.assertEqual(gpu.state_bytes(actual),sum(getattr(expected,k).nbytes for k in gpu.KEYS))

    def test_autograd_metric_and_energy(self):
        _,s = self.fixture(3)
        w,c,M = [getattr(s,k).clone().requires_grad_(True) for k in ('w','c','M')]
        h = torch.tanh(w @ self.tdata.inputs.T)
        a = s.b1.T @ (s.p1[:,None]*h)
        H = torch.tanh(s.b2 @ M @ a)
        f = (s.p2*c) @ H
        L = self.tdata.probabilities @ (f-self.tdata.labels)**2
        gradients = torch.autograd.grad(L,(w,c,M))
        v = gpu.rhs(s,self.tdata,block_size=2)
        for expected,actual in zip((-gradients[0]/s.p1[:,None],-gradients[1]/s.p2,-gradients[2]),v):
            self.close(expected.detach().cpu().numpy(),actual)
        directional = sum((a*b).sum() for a,b in zip(gradients,v))
        energy = -((s.p1[:,None]*v[0]**2).sum()+(s.p2*v[1]**2).sum()+(v[2]**2).sum())
        self.close(directional.detach().cpu().numpy(),energy)

    def test_observation_and_restart_every_order(self):
        scratch = os.environ.get('CIRCLE_TEST_SCRATCH')
        for order in (1,3,5):
            ref,s = self.fixture(order)
            value = gpu.observe(s,self.tdata,include_pairs=True)
            pairs = cpu.paired_observations(ref,self.data)
            blocked = gpu.paired_observations(s,self.tdata,block_size=2,include_pairs=True)
            self.close(pairs['first_pairs'],blocked['first_pairs'])
            self.close(pairs['second_pairs'],blocked['second_pairs'])
            self.close([pairs['rms1'],pairs['rms2']],blocked['rms'])
            self.close(pairs['first_pairs'],value['first_pairs'])
            self.close(pairs['second_pairs'],value['second_pairs'])
            self.close([pairs['rms1'],pairs['rms2']],value['rms'])
            fields = cpu._fields(ref,self.u)
            for i,(key,pop) in enumerate((('h1',ref.p1),('h2',ref.p2))):
                self.close(fields[key].T @ (pop[:,None]*fields[key]),value['grams'][i])
            self.close(cpu.loss(ref,self.data),value['loss'])
            self.close(np.zeros(4),gpu.predict(s,self.u)+gpu.predict(s,-self.u))
            first = gpu.evolve(s,self.tdata,steps=2,step_size=.01)
            with tempfile.TemporaryDirectory(dir=scratch) as directory:
                path = Path(directory)/'state.json'
                gpu.save_restart(path,first,self.tdata)
                restored,data = gpu.load_restart(path,device=self.device)
                for key in gpu.KEYS: self.assertTrue(torch.equal(getattr(first,key),getattr(restored,key)))
                self.assertEqual(first.metadata,restored.metadata)
                a = gpu.evolve(first,self.tdata,steps=2,step_size=.01)
                b = gpu.evolve(restored,data,steps=2,step_size=.01)
                for key in gpu.KEYS: self.assertTrue(torch.equal(getattr(a,key),getattr(b,key)))
                cpu_state,cpu_data = cpu.load_restart(path)
                self.close(cpu.predict(cpu_state,cpu_data.inputs),gpu.predict(restored,data.inputs))

    def test_boundaries_weights_blocking_ownership(self):
        ref,s = self.fixture(1)
        for order in (0,2,4,7,True,1.0):
            with self.assertRaises(ValueError): gpu.initialize(order)
        for value in (0,-1,True,1.5):
            with self.assertRaises(ValueError): gpu.predict(s,self.u,block_size=value)
        for h in (0,-1,float('nan'),float('inf'),True):
            with self.assertRaises(ValueError): gpu.evolve(s,self.tdata,steps=1,step_size=h)
        for u in (np.zeros((1,2)),np.ones((2,3)),np.empty((0,2)),[[float('nan'),0]]):
            with self.assertRaises(ValueError): gpu.predict(s,u)
        with self.assertRaises(ValueError): gpu.data_law(self.u,self.y,[1,1,1,1],device=self.device)
        for block in (1,2,20):
            self.close(gpu.predict(s,self.u).cpu().numpy(),gpu.predict(s,self.u,block_size=block))
        self.close(cpu.predict(ref,self.u[[0,0,2]]),gpu.predict(s,self.u[[0,0,2]]))
        # Unequal populations and zero-probability nodes are valid.
        ref.b2=ref.b2[:17]; ref.c=ref.c[:17]; ref.p2=np.ones(17)/17
        ref.p1[0]=0; ref.p1[1:]=1/31
        other=gpu.from_cpu(ref,device=self.device)
        for a,b in zip(cpu.rhs(ref,self.data),gpu.rhs(other,self.tdata)):
            self.close(a,b)
        copied=gpu.to_cpu(s); copied.w[:]=0
        self.assertFalse(torch.equal(s.w,torch.zeros_like(s.w)))
        broken=s.copy(); broken.w=broken.w.float()
        with self.assertRaises(ValueError): gpu.predict(broken,self.u)
        broken=s.copy(); broken.M[0,0]=float('nan')
        with self.assertRaises(ValueError): gpu.rhs(broken,self.tdata)

if __name__=='__main__': unittest.main()
