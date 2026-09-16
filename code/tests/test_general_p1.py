"""Deterministic finite-algebra tests; PDE_TEST_DEVICE selects cpu or cuda:1.

The same tests run on both. GPU policy must be set before engine construction.
No external dataset or archived state is read. Temporary archives use TMPDIR.
"""
import os
import tempfile
import unittest
from pathlib import Path
import numpy as np
try:
    import torch
except ModuleNotFoundError as error:
    if error.name != "torch":
        raise
    torch = None
from pde.observable_p1_initialization import initialize, coefficients, RIDGE
from pde.observable_initialization import build_dictionary
from pde.observable_words import constant, decode_word
if torch is not None:
    from pde.observable_torch_p1 import ClosureEngine, TensorState, initialize_p1
    from pde.finite_torch import NetworkEngine
from pde.finite_network import Parameters, forward, flow_velocity, initialize as initialize_network
from pde.closure_comparison import prediction_metrics, gram_metrics, all_seed_pairs, match_training_loss

DEVICE = os.environ.get("PDE_TEST_DEVICE","cpu")
if torch is not None:
    torch.set_num_threads(1)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    torch.use_deterministic_algorithms(True)
    if DEVICE.startswith("cuda"):
        torch.cuda.set_per_process_memory_fraction(0.15,device=DEVICE)


def array(x):
    return x.detach().cpu().numpy() if torch is not None and isinstance(x,torch.Tensor) else np.asarray(x)


def close(a,b,atol=2e-12,rtol=2e-11):
    np.testing.assert_allclose(array(a),array(b),atol=atol,rtol=rtol)


def case(d=3, dtype=None, block=4):
    if dtype is None:
        dtype = torch.float64
    rng = np.random.default_rng(123)
    P1,P2,K1,K2,m = 7,11,5,4,9
    g,b1,b2,D = (rng.normal(size=shape) for shape in ((P1,d),(P1,K1),(P2,K2),(K2,K1)))
    D *= 0.1
    p1,p2 = np.arange(1,P1+1,dtype=float),np.arange(1,P2+1,dtype=float)
    e = ClosureEngine(b1,g,b2,D,p1=p1/p1.sum(),p2=p2/p2.sum(),device=DEVICE,dtype=dtype,block_size=block)
    s = e.state(g+0.1*rng.normal(size=g.shape),0.2*rng.normal(size=P2),D+0.1*rng.normal(size=D.shape))
    U = rng.normal(size=(m,d)); U[0] = 0; U[2] = U[1]
    y = rng.normal(size=m); weights = np.arange(m,dtype=float); weights /= weights.sum()
    return e,s,e.prepare_data(U,y,weights)


def numpy_oracle(e,s,data):
    # Independent sample-by-sample contractions, no Torch or blocked kernel.
    b1,b2,p1,p2,w,c,M,U,y,mu = map(array,(e.b1,e.b2,e.p1,e.p2,s.w,s.c,s.M,data.inputs,data.labels,data.probabilities))
    vw,vc,vM = np.zeros_like(w),np.zeros_like(c),np.zeros_like(M)
    predictions = []
    for u,label,weight in zip(U,y,mu):
        h1 = np.tanh(w @ u)
        a = np.sum(p1[:,None]*b1*h1[:,None],axis=0)
        h2 = np.tanh(b2 @ M @ a)
        f = np.sum(p2*c*h2); predictions.append(f)
        backward = np.sum(p2[:,None]*b2*(c*(1-h2*h2))[:,None],axis=0)
        q = b1 @ M.T @ backward
        vw -= 2*weight*(f-label)*np.outer((1-h1*h1)*q,u)
        vc -= 2*weight*(f-label)*h2
        vM -= 2*weight*(f-label)*np.outer(backward,a)
    return np.array(predictions),(vw,vc,vM)


class InitializationTests(unittest.TestCase):
    def test_dense_cholesky_and_response(self):
        dictionary = build_dictionary(1)
        self.assertEqual(dictionary.first_exponents,((0,0,0,0),(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)))
        self.assertEqual(dictionary.second_exponents,((0,0),(1,0),(0,1)))
        self.assertEqual(dictionary.tail_codes,())
        self.assertTrue(dictionary.fast_core)
        self.assertEqual(decode_word(0),constant(1))
        self.assertEqual(decode_word(1),constant(2))
        coeff,diagnostic = coefficients()
        self.assertLess(diagnostic['max_absolute_refinement_difference'],1e-10)
        for d in (1,2,7,17):
            for rule,folded in (("iid",False),("antithetic",False),("antithetic",True)):
                z = initialize(d,40,1907,population_rule=rule,folded=folded)
                offset = 0 if folded else 1
                # Recover RAW fields from common Gaussian draws independently.
                streams = [np.random.Generator(np.random.PCG64(x)) for x in np.random.SeedSequence(1907).spawn(3)]
                count = 20 if rule=="antithetic" else 40
                g = streams[0].standard_normal((count,d)); h=np.tanh(g)
                k=np.tanh(np.sqrt(coeff['tau'])*streams[1].standard_normal((count,d))+coeff['alpha']*h)
                upper=np.tanh(np.sqrt(coeff['v'])*streams[2].standard_normal((count,d)))
                if rule=="antithetic" and not folded:
                    g,h,k,upper = [np.concatenate((a,-a)) for a in (g,h,k,upper)]
                r1,r2 = np.column_stack((h,k)),upper
                if offset:
                    r1=np.column_stack((np.ones(len(g)),r1));r2=np.column_stack((np.ones(len(g)),r2))
                G1,G2,C = np.zeros((2*d+offset,2*d+offset)),np.zeros((d+offset,d+offset)),np.zeros((d+offset,2*d+offset))
                if offset: G1[0,0]=G2[0,0]=1
                for j in range(d):
                    hcol,kcol,row=j+offset,j+d+offset,j+offset
                    G1[hcol,hcol]=coeff['v'];G1[kcol,kcol]=coeff['s']
                    G1[hcol,kcol]=G1[kcol,hcol]=coeff['beta'];G2[row,row]=coeff['tau']
                    C[row,hcol]=coeff['alpha']*coeff['v']
                    C[row,kcol]=coeff['alpha']*coeff['beta']+coeff['tau']*coeff['gamma']
                L1=np.linalg.cholesky(G1+RIDGE*np.eye(len(G1)));L2=np.linalg.cholesky(G2+RIDGE*np.eye(len(G2)))
                T1=np.linalg.solve(L1,np.eye(len(G1)));T2=np.linalg.solve(L2,np.eye(len(G2)))
                close(z.g,g);close(z.b1,r1@T1.T);close(z.b2,r2@T2.T);close(z.D,T2@C@T1.T)
                self.assertFalse(z.metadata['exact_population_coefficients'])

    def test_validation_and_seed_ownership(self):
        np.random.seed(19); saved=np.random.get_state()
        initialize(1,2,3)
        current=np.random.get_state()
        np.testing.assert_array_equal(saved[1],current[1]);self.assertEqual(saved[2:],current[2:])
        for args,kw in (((0,2,1),{}),((1,0,1),{}),((1,2,True),{}),((1,3,1),dict(population_rule='antithetic')),
                        ((1,2,1),dict(folded=True)),((1,2,1),dict(cutoff=True))):
            with self.assertRaises(ValueError): initialize(*args,**kw)


@unittest.skipIf(torch is None,"optional Torch dependency unavailable")
class EngineTests(unittest.TestCase):
    def test_numpy_supplied_state_and_heun(self):
        for d in (1,2,7):
            e,s,data=case(d)
            f,v=numpy_oracle(e,s,data);close(e.predict(s,data.inputs),f)
            for implementation in ('reference','optimized'):
                actual=e.rhs(s,data,implementation=implementation)
                for name,expected in zip(('w','c','M'),v):close(getattr(actual,name),expected)
            dt=.01
            stage=e.state(*(array(getattr(s,k))+dt*x for k,x in zip(('w','c','M'),v)))
            _,ell=numpy_oracle(e,stage,data)
            end=e.heun_step(s,data,dt)
            for k,a,b in zip(('w','c','M'),v,ell):close(getattr(end,k),array(getattr(s,k))+dt/2*(a+b))

    def test_autograd_and_energy(self):
        for d in (1,2,7):
            e,s,data=case(d)
            w,c,M=[v.clone().requires_grad_(True) for v in (s.w,s.c,s.M)]
            h1=torch.tanh(w@data.inputs.T);a=e.b1.T@(e.p1[:,None]*h1)
            h2=torch.tanh(e.b2@M@a);f=(e.p2*c)@h2
            L=(data.probabilities*(f-data.labels)**2).sum()
            gw,gc,gM=torch.autograd.grad(L,(w,c,M));v=e.rhs(s,data)
            close(v.w,-gw/e.p1[:,None]);close(v.c,-gc/e.p2);close(v.M,-gM)
            derivative=(gw*v.w).sum()+(gc*v.c).sum()+(gM*v.M).sum()
            energy=-(e.p1[:,None]*v.w**2).sum()-(e.p2*v.c**2).sum()-(v.M**2).sum()
            close(derivative,energy)
            initial=e.rhs(e.initial_state(),data)
            self.assertEqual(torch.count_nonzero(initial.w).item(),0)
            self.assertEqual(torch.count_nonzero(initial.M).item(),0)

    def test_associations_restart_and_observations(self):
        e,s,data=case(); baseline=e.rhs(s,data)
        for block in (1,4,32):
            for mode in ('direct','folded','auto'):
                e.block_size,e.forward_mode=block,mode
                v=e.rhs(s,data)
                for k in ('w','c','M'): close(getattr(v,k),getattr(baseline,k))
        e.block_size=4
        half=e.evolve(s,data,steps=3,step_size=.01)
        with tempfile.TemporaryDirectory() as directory:
            checkpoint=Path(directory)/'state.npz'
            e.save_restart(checkpoint,half,data,metadata={'time':.03})
            restored,current,law,metadata=ClosureEngine.load_restart(checkpoint,device=DEVICE)
            self.assertEqual(metadata,{'time':.03})
            continued=restored.evolve(current,law,steps=3,step_size=.01)
        direct=e.evolve(s,data,steps=6,step_size=.01)
        for k in ('w','c','M'):self.assertTrue(torch.equal(getattr(continued,k),getattr(direct,k)))
        obs=e.observations(direct,data,include_pairs=True)
        for number in (1,2):
            pairs,p=obs[f'pairs{number}'],obs[f'population_weights{number}']
            h0,h=pairs[:,:,0],pairs[:,:,1]
            close(obs[f'rms{number}'],torch.sqrt(p@((h-h0)**2)@data.probabilities))
            for label,left,right in (('initial',h0,h0),('current',h,h),('cross',h0,h)):
                close(obs[f'gram{number}_{label}'],left.T@(p[:,None]*right))

    def test_nontrivial_folding_and_signed_law(self):
        ef,sf=initialize_p1(4,24,7,population_rule='antithetic',folded=True,device=DEVICE)
        eu,su=initialize_p1(4,24,7,population_rule='antithetic',device=DEVICE)
        rng=np.random.default_rng(15)
        sf=ef.state(array(sf.w)+.1*rng.normal(size=sf.w.shape),rng.normal(size=sf.c.shape),
                    array(sf.M)+.2*rng.normal(size=sf.M.shape))
        fullM=array(su.M);fullM[1:,1:]=array(sf.M)
        su=eu.state(np.concatenate((array(sf.w),-array(sf.w))),np.concatenate((array(sf.c),-array(sf.c))),fullM)
        U=rng.normal(size=(7,4));y=rng.normal(size=7)
        df,du=ef.prepare_data(U,y),eu.prepare_data(U,y)
        for _ in range(4):
            close(ef.predict(sf,U),eu.predict(su,U))
            sf,su=ef.heun_step(sf,df,.01),eu.heun_step(su,du,.01)
            close(sf.w,su.w[:12]);close(sf.c,su.c[:12]);close(sf.M,su.M[1:,1:])
            close(su.M[0],np.zeros(9));close(su.M[:,0],np.zeros(5))
        of,ou=ef.observations(sf,df,include_pairs=True),eu.observations(su,du,include_pairs=True)
        for k in of:close(of[k],ou[k])
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'fold.npz';ef.save_restart(path,sf,df)
            loaded,_,_,_=ClosureEngine.load_restart(path,device=DEVICE)
            self.assertEqual(loaded.representation,ef.representation)
            self.assertEqual(loaded.representation['nominal_population_nodes'],24)

    def test_float32_and_saturation(self):
        e64,s64,d64=case(dtype=torch.float64);e32,s32,d32=case(dtype=torch.float32)
        for _ in range(12):
            s64=e64.heun_step(s64,d64,.01);s32=e32.heun_step(s32,d32,.01)
        close(e32.predict(s32,d32.inputs),e64.predict(s64,d64.inputs),atol=3e-6,rtol=3e-4)
        s64.w.fill_(1e3);self.assertTrue(torch.isfinite(e64.rhs(s64,d64).w).all())

    def test_boundaries_and_mutation(self):
        e,s,data=case()
        for h in (0,-1,np.nan,True):
            with self.assertRaises(ValueError):e.heun_step(s,data,h)
            with self.assertRaises(ValueError):e.evolve(s,data,steps=0,step_size=h)
        with self.assertRaises(ValueError):e.prepare_inputs(np.zeros((2,4)))
        with self.assertRaises(ValueError):e.prepare_inputs([[np.nan]*3])
        with self.assertRaises(ValueError):e.prepare_data(np.zeros((2,3)),[1,2],[.5,.6])
        U=np.ones((2,3));law=e.prepare_data(U,[1,2]);U[:]=3;close(law.inputs,np.ones((2,3)))
        law.inputs.add_(1)
        with self.assertRaises(ValueError):e.rhs(s,law)
        s.c[0]=float('nan')
        with self.assertRaises(ValueError):e.predict(s,data.inputs)
        e,s,data=case();e.b1.add_(1)
        with self.assertRaises(ValueError):e.rhs(s,data)
        e,s,data=case();zero=e.prepare_data(data.inputs,data.labels,[1]+[0]*8)
        self.assertTrue(torch.isfinite(e.rhs(s,zero).M).all())


@unittest.skipIf(torch is None,"optional Torch dependency unavailable")
class NetworkTests(unittest.TestCase):
    def test_initialization_numpy_rhs_heun_autograd(self):
        e=NetworkEngine(3,9,17,device=DEVICE,block_size=4);s=e.initial_state()
        initial=initialize_network(9,2,3,seed=17)
        close(s.w,initial.weights[0],atol=0,rtol=0);close(s.M,initial.weights[1],atol=0,rtol=0);close(s.c,initial.readout,atol=0,rtol=0)
        self.assertGreater(torch.count_nonzero(s.c).item(),0)
        rng=np.random.default_rng(8);s.c.add_(torch.as_tensor(rng.normal(size=9),device=DEVICE))
        U=rng.normal(size=(7,3));U[0]=0;U[2]=U[1];y=rng.normal(size=7);data=e.prepare_data(U,y)
        def params(state):return Parameters((array(state.w),array(state.M)),array(state.c))
        reference=flow_velocity(params(s),U.T*np.sqrt(3),y);v=e.rhs(s,data)
        close(e.predict(s,U),forward(params(s),U.T*np.sqrt(3)).output)
        for a,b in zip((v.w,v.c,v.M),(reference.weights[0],reference.readout,reference.weights[1])):close(a,b)
        h=.01;stage=e.state(*(array(a)+h*array(b) for a,b in zip((s.w,s.c,s.M),(v.w,v.c,v.M))))
        ell=flow_velocity(params(stage),U.T*np.sqrt(3),y);end=e.heun_step(s,data,h)
        for a,old,b,c in zip((end.w,end.c,end.M),(s.w,s.c,s.M),(v.w,v.c,v.M),(ell.weights[0],ell.readout,ell.weights[1])):
            close(a,array(old)+h/2*(array(b)+c))
        weights=np.arange(1,8,dtype=float);weights/=weights.sum();law=e.prepare_data(U,y,weights)
        w,c,M=[x.clone().requires_grad_(True) for x in (s.w,s.c,s.M)]
        f=c@torch.tanh(M@torch.tanh(w@law.inputs.T))/e.n
        gw,gc,gM=torch.autograd.grad((law.probabilities*(f-law.labels)**2).sum(),(w,c,M));v=e.rhs(s,law)
        close(v.w,-e.n*gw);close(v.c,-e.n*gc);close(v.M,-gM)
        obs=e.observations(end,U)
        for number in (1,2):
            pairs=obs[f'pairs{number}'];close(obs[f'gram{number}_current'],pairs[:,:,1].T@pairs[:,:,1]/e.n)

    def test_invalid_and_zero_steps(self):
        for args in ((0,3,1),(2,0,1),(2,3,True)):
            with self.assertRaises(ValueError):NetworkEngine(*args,device=DEVICE)
        e=NetworkEngine(2,3,1,device=DEVICE);s=e.initial_state();data=e.prepare_data([[0.,0.]],[1.])
        self.assertTrue(torch.equal(e.evolve(s,data,steps=0,step_size=.01).M,s.M))
        for dt in (0,-1,True,np.nan):
            with self.assertRaises(ValueError):e.heun_step(s,data,dt)
        with self.assertRaises(ValueError):e.prepare_data([[0.,0.]],[1.],[-1.])


class ComparisonTests(unittest.TestCase):
    def test_scaled_tiny_and_large_metrics(self):
        kw=dict(ids=[1,2],reference_ids=[1,2])
        for scale in (1e-200,1e200):
            reference=scale*np.array([1.,2.])
            result=prediction_metrics(2*reference,reference,**kw)['overall']
            self.assertAlmostEqual(result['rms']/scale,np.sqrt(2.5),places=14)
            self.assertAlmostEqual(result['relative_rms'],1.,places=14)
            self.assertAlmostEqual(result['correlation'],1.,places=14)
            zero=prediction_metrics([scale,0.],[0.,0.],**kw)['overall']
            self.assertAlmostEqual(zero['rms']/scale,1/np.sqrt(2),places=14)
            self.assertIsNone(zero['relative_rms'])
            self.assertEqual(zero['max_absolute'],scale)
            gram=gram_metrics([[scale,0.],[0.,0.]],np.zeros((2,2)),**kw)
            self.assertEqual(gram['frobenius'],scale)
            self.assertEqual(gram['rms_entry'],scale/2)
            self.assertIsNone(gram['relative_frobenius'])
            proportional=gram_metrics(np.diag([2*scale,4*scale]),np.diag([scale,2*scale]),**kw)
            self.assertAlmostEqual(proportional['relative_frobenius'],1.,places=14)
        # L2 magnitude may overflow although the requested RMS is representable.
        largest=prediction_metrics([1e308,-1e308],[0.,0.],**kw)['overall']
        self.assertEqual(largest['rms'],1e308)
        self.assertIsNone(largest['relative_rms'])
        # Nearby large entries retain their centered spread after an exact
        # power-of-two scale and anchor subtraction.
        x=1e200+np.arange(4)*np.spacing(1e200)
        result=prediction_metrics(x,x,ids=np.arange(4),reference_ids=np.arange(4))['overall']
        self.assertAlmostEqual(result['correlation'],1.,places=14)
        self.assertEqual(result['relative_rms'],0.)

    def test_scaled_class_and_seed_wrappers(self):
        reference=1e-200*np.array([1.,2.,3.,4.]);ids=np.arange(4);labels=[0,0,1,1]
        result=prediction_metrics(2*reference,reference,ids=ids,reference_ids=ids,labels=labels)
        for row in [result['overall'],*result['within_class']]:
            self.assertGreater(row['rms'],0)
            self.assertAlmostEqual(row['relative_rms'],1.,places=14)
            self.assertAlmostEqual(row['correlation'],1.,places=14)
        result=all_seed_pairs([2*reference],[reference,reference],ids=ids,reference_ids=ids,labels=labels)
        for item in result['individual_pairs']+result['reference_mean']:
            for row in [item['metrics']['overall'],*item['metrics']['within_class']]:
                self.assertGreater(row['rms'],0)
                self.assertAlmostEqual(row['relative_rms'],1.,places=14)
                self.assertAlmostEqual(row['correlation'],1.,places=14)
        result=all_seed_pairs([reference],[np.zeros(4),np.zeros(4)],ids=ids,reference_ids=ids,labels=labels)
        for item in result['individual_pairs']+result['reference_mean']:
            self.assertIsNone(item['metrics']['overall']['relative_rms'])
            self.assertTrue(all(row['relative_rms'] is None for row in item['metrics']['within_class']))
        # Reference averaging must neither overflow a large constant nor erase
        # a minimum-subnormal constant before the comparison path sees it.
        tiny=np.nextafter(0.,1.)
        for value in (tiny,1e308):
            result=all_seed_pairs([[value]],[ [value], [value] ],ids=[1],reference_ids=[1])
            self.assertEqual(result['reference_mean'][0]['metrics']['overall']['relative_rms'],0.)
            self.assertIsNone(result['reference_mean'][0]['metrics']['overall']['correlation'])
        large=np.array([1e308,5e307])
        result=all_seed_pairs([large],[large,.5*large],ids=[1,2],reference_ids=[1,2])
        self.assertAlmostEqual(result['reference_mean'][0]['metrics']['overall']['relative_rms'],1/3,places=14)

    def test_subnormal_and_unrepresentable_diagnostics(self):
        tiny=np.nextafter(0.,1.)
        prediction=prediction_metrics([tiny],[0.],ids=[1],reference_ids=[1])['overall']
        self.assertEqual(prediction['rms'],tiny)
        self.assertIsNone(prediction['relative_rms'])
        self.assertEqual(prediction_metrics([2*tiny],[tiny],ids=[1],reference_ids=[1])['overall']['relative_rms'],1.)
        gram=gram_metrics([[4*tiny,0.],[0.,0.]],np.zeros((2,2)),ids=[1,2],reference_ids=[1,2])
        self.assertEqual(gram['frobenius'],4*tiny);self.assertEqual(gram['rms_entry'],2*tiny)
        self.assertIsNone(gram['relative_frobenius'])
        # A nonzero requested diagnostic below float64 range rejects, rather
        # than acquiring the exact-zero sentinel. Overflow rejects too.
        with self.assertRaises(ValueError):
            prediction_metrics([tiny]+[0.]*15,np.zeros(16),ids=np.arange(16),reference_ids=np.arange(16))
        with self.assertRaises(ValueError):
            gram_metrics([[tiny,0.],[0.,0.]],np.zeros((2,2)),ids=[1,2],reference_ids=[1,2])
        with self.assertRaises(ValueError):
            prediction_metrics([1.],[tiny],ids=[1],reference_ids=[1])
        with self.assertRaises(ValueError):
            prediction_metrics([1e308,tiny],[1e308,0.],ids=[1,2],reference_ids=[1,2])
        with self.assertRaises(ValueError):
            prediction_metrics([1e308],[-1e308],ids=[1],reference_ids=[1])
        with self.assertRaises(ValueError):
            gram_metrics(np.full((2,2),1e308),np.zeros((2,2)),ids=[1,2],reference_ids=[1,2])
        with self.assertRaises(ValueError):
            all_seed_pairs([[tiny]],[[tiny],[0.]],ids=[1],reference_ids=[1])

    def test_decimal_constant_correlations(self):
        for count in (3,7):
            ids=np.arange(count)
            fixed=np.full(count,.1); varying=np.arange(count,dtype=float)
            for candidate,reference in ((fixed,fixed),(fixed,varying),(varying,fixed)):
                result=prediction_metrics(candidate,reference,ids=ids,reference_ids=ids)
                self.assertIsNone(result['overall']['correlation'])
        # The overall arrays vary, while each class is exactly constant.
        ids=np.arange(6); labels=np.repeat([0,1],3)
        candidate=np.repeat([.1,.2],3); reference=np.repeat([.3,.4],3)
        result=prediction_metrics(candidate,reference,ids=ids,reference_ids=ids,labels=labels)
        self.assertIsNotNone(result['overall']['correlation'])
        self.assertTrue(all(row['correlation'] is None for row in result['within_class']))
        pairs=all_seed_pairs([np.full(3,.1)],[np.full(3,.2)],ids=np.arange(3),reference_ids=np.arange(3))
        self.assertIsNone(pairs['individual_pairs'][0]['metrics']['overall']['correlation'])
        self.assertIsNone(pairs['reference_mean'][0]['metrics']['overall']['correlation'])

    def test_zero_constant_absent_and_ids(self):
        kw=dict(ids=[4,8],reference_ids=[4,8])
        report=prediction_metrics([1,1],[0,0],labels=[1,1],classes=[1,2],**kw)
        self.assertIsNone(report['overall']['relative_rms']);self.assertIsNone(report['overall']['correlation'])
        self.assertEqual(report['within_class'][1]['count'],0)
        self.assertEqual(prediction_metrics([0,0],[0,0],**kw)['overall']['relative_rms'],0)
        self.assertIsNone(prediction_metrics([1,2],[1,1],**kw)['overall']['correlation'])
        self.assertIsNone(gram_metrics(np.ones((2,2)),np.zeros((2,2)),**kw)['relative_frobenius'])
        with self.assertRaises(ValueError):prediction_metrics([1,2],[1,2],ids=[4,8],reference_ids=[8,4])
        with self.assertRaises(ValueError):prediction_metrics([1,np.nan],[1,2],**kw)
        pairs=all_seed_pairs([[0,1],[1,0]],[[1,2],[2,1],[3,4]],**kw)
        self.assertEqual(len(pairs['individual_pairs']),6)

    def test_loss_matching_is_training_only(self):
        match=match_training_loss([0,1,2,3],[3,1,2,1],1.5)
        self.assertEqual(match['index'],1);self.assertEqual(match['lower_index'],1);self.assertEqual(match['upper_index'],2)
        self.assertEqual(match['absolute_mismatch'],.5)
        for target in (0,4,np.nan):
            with self.assertRaises(ValueError):match_training_loss([0,1],[3,1],target)
        with self.assertRaises(ValueError):match_training_loss([0,0],[3,1],2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
