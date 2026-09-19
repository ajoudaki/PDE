"""Fixed supplied-state checks; no training trajectory or resolution sweep."""
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import sys
import time
import unittest

import numpy as np

import activation_closure as ac
from pde import finite_network as net
from pde.observable_compiler import GaussianCompiler, compile_raw_dictionary
from pde.observable_words import seed, unary, action, decode_word
from pde.observable_laws import OrthogonalArcLaw, RationalRadius


ARRAYS=("b1","g","w","p1","b2","c","p2","M","D")


def example(activation=ac.LINEAR_SINE,ar=None):
    return ac.supplied_state(
        b1=[[1,"1/4"],["1/2","-2/5"],["-1/3","3/5"]],
        g=[["-1/5","2/5"],["3/5","-2/5"],["4/5","1/10"]],
        w=[["1/5","3/10"],["-3/5","4/5"],["6/5","-1/10"]],
        p1=[Fraction(1,4),Fraction(1,4),Fraction(1,2)],
        b2=[[1,"1/5"],["-3/10","4/5"]],c=["2/5","-1/4"],
        p2=[Fraction(1,3),Fraction(2,3)],M=[["4/5","-3/10"],["1/5","1/2"]],
        D=[["3/5","1/10"],["-1/5","2/5"]],activation=activation,arithmetic=ar)


def data(ar,unequal=True):
    return ac.DataLaw(ar.array([[1,0],[Fraction(3,5),Fraction(4,5)]]),
                      ar.array([1,-1]),ar.array([Fraction(1,3),Fraction(2,3)] if unequal else [Fraction(1,2)]*2)).validate(ar)


class Checks(unittest.TestCase):
    def close(self,left,right,tolerance=2e-11):
        np.testing.assert_allclose(np.asarray(left,dtype=float),np.asarray(right,dtype=float),
                                   rtol=tolerance,atol=tolerance)

    def test_dictionary_cofinal_prefix_duplicates_and_budget(self):
        previous=[(),()]
        for N in (1,2,4,8):
            d=ac.build_dictionary(N)
            for layer,words,codes in ((1,d.first_words,d.first_codes),(2,d.second_words,d.second_codes)):
                expected=tuple(code for code in range(16*N+1)
                               if (w:=decode_word(code)) is not None and w.bounded and w.population==layer)
                self.assertEqual(codes,expected)
                self.assertEqual(words[:len(previous[layer-1])],previous[layer-1])
                previous[layer-1]=words
        self.assertIn(62,d.second_codes)  # tanh(A0 1)
        self.assertIn(126,d.first_codes)  # tanh(A0* 1)
        self.assertGreater(len(d.first_words),len(set(d.first_words)))
        with self.assertRaises(ac.InitializationResourceLimit):
            ac.build_dictionary(8,limits=ac.InitializationLimits(max_codes=128))

    def test_complete_nested_response_and_frozen_derivatives(self):
        ar=ac.Arithmetic()
        h=unary("sin",seed("g1")); xi=action(h); v=unary("sin",xi)
        q=action(v); b=unary("sin",q); y=action(b)
        program=GaussianCompiler(ar,ac.gaussian_points,32,"0.001").compile((y,))
        xi_value=program.evaluate(xi); h_value=program.evaluate(h)
        q_value,partial=program.evaluate(q,derivative=True)
        alpha=np.mean(np.cos(xi_value))
        reverse=program.sources[program._word(q,False)]
        self.close([coef for _,coef in reverse.response],[alpha])
        self.close(partial[:,reverse.index],np.ones(32))
        base=program._normals[1][:,2:] @ program.factors[1].T
        self.close(q_value,base[:,reverse.index]+alpha*h_value)
        forward=program.sources[program._word(y,False)]
        beta=np.mean(np.cos(q_value))
        self.close([coef for _,coef in forward.response],[beta])
        self.assertGreater(abs(alpha),0.1)
        self.assertGreater(abs(beta),0.1)
        coefficients=tuple((s.node,s.response) for s in program.sources.values())
        replay=program.evaluate(b,16)
        self.assertEqual(replay.shape,(16,))
        self.assertEqual(coefficients,tuple((s.node,s.response) for s in program.sources.values()))

    def test_generic_initialization_and_activation_independence(self):
        s=ac.initialize(ac.LINEAR_SINE,8,initialization_nodes=32,population_nodes=16)
        never=ac.Activation("unevaluated","caller formula",lambda *x: self.fail("initializer called phi"),
                            lambda *x: self.fail("initializer called phi prime"))
        other=ac.initialize(never,8,initialization_nodes=32,population_nodes=16)
        for key in ARRAYS:
            np.testing.assert_array_equal(getattr(s,key),getattr(other,key))
        d=ac.build_dictionary(8); ar=s.arithmetic
        raw=compile_raw_dictionary(d.first_words,d.second_words,arithmetic=ar,
             gaussian_points=ac.gaussian_points,initialization_nodes=32,population_nodes=16,epsilon_cov="0.001")
        eta=2.**-8
        L1=np.linalg.cholesky(raw.gram1+eta*np.eye(len(d.first_words)))
        L2=np.linalg.cholesky(raw.gram2+eta*np.eye(len(d.second_words)))
        self.close(s.b1,np.linalg.solve(L1,raw.psi1.T).T)
        self.close(s.b2,np.linalg.solve(L2,raw.psi2.T).T)
        expected=np.linalg.solve(L2,np.linalg.solve(L1,raw.C.T).T)
        self.close(s.D,expected)
        self.assertEqual(s.metadata["initialization_strategy"],"complete-gaussian-program")
        self.assertGreater(s.metadata["compiler"]["sources"],4)
        self.assertEqual(s.b1.shape[1],len(d.first_words))
        self.assertEqual(s.b2.shape[1],len(d.second_words))
        self.assertEqual(s.M.shape,(len(d.second_words),len(d.first_words)))
        self.assertEqual(s.metadata["ridge_denominator"],256)
        np.testing.assert_array_equal(s.w,s.g)
        np.testing.assert_array_equal(s.M,s.D)
        self.assertTrue(np.all(s.c==0))

    def test_all_gradients_energy_and_actual_adjunction(self):
        delta=1e-6
        for activation in (ac.LINEAR_SINE,ac.FLAT_RAMP):
            s=example(activation); law=data(s.arithmetic)
            velocity=ac.rhs(s,law,activation)
            for name,drift in zip(("w","c","M"),velocity):
                for index in np.ndindex(drift.shape):
                    plus,minus=s.copy(),s.copy()
                    getattr(plus,name)[index]+=delta
                    getattr(minus,name)[index]-=delta
                    difference=(ac.loss(plus,law,activation)-ac.loss(minus,law,activation))/(2*delta)
                    weight=s.p1[index[0]] if name=="w" else s.p2[index[0]] if name=="c" else 1
                    self.close(difference,-weight*drift[index],3e-6)
            plus=s.dynamic_copy(*(getattr(s,k)+delta*v for k,v in zip(("w","c","M"),velocity)))
            minus=s.dynamic_copy(*(getattr(s,k)-delta*v for k,v in zip(("w","c","M"),velocity)))
            derivative=(ac.loss(plus,law,activation)-ac.loss(minus,law,activation))/(2*delta)
            norm=np.sum(s.p1[:,None]*velocity[0]**2)+np.sum(s.p2*velocity[1]**2)+np.sum(velocity[2]**2)
            self.close(derivative,-norm,3e-6)
            v=np.array([.7,-.3,.2]); z=np.array([-.4,.8])
            self.close(z @ (s.p2*ac.apply_action(s,1,v)),v @ (s.p1*ac.apply_action(s,2,z)))
            split=ac.rhs(s,law,activation,block_size=1)
            for got,expected in zip(split,velocity):
                self.close(got,expected)

    def test_dense_network_normalization_at_supplied_state(self):
        activation=ac.Activation("shifted-linear-sine","phi(z)=1/5+z+sin(z)/4",
            lambda z,ar: ar.real(Fraction(1,5))+z+ar.trig(z)/ar.real(4),ac.LINEAR_SINE.derivative)
        b=np.sqrt(2)*np.eye(2); w=np.array([[.2,.3],[-.5,.4]])
        M=np.array([[.7,-.2],[.3,.8]]); c=np.array([.4,-.6])
        s=ac.supplied_state(b1=b,g=w,w=w,p1=[.5,.5],b2=b,c=c,p2=[.5,.5],M=M,D=M,activation=activation)
        law=data(s.arithmetic,False)
        theta=net.Parameters((w,M),c)
        a=net.Activation(activation.name,lambda z: activation.evaluate(z,s.arithmetic),
                         lambda z: activation.evaluate(z,s.arithmetic,True))
        physical=np.sqrt(2)*law.inputs.T
        self.close(ac.predict(s,law.inputs,activation),net.forward(theta,physical,a).output)
        ours=ac.rhs(s,law,activation); theirs=net.flow_velocity(theta,physical,law.labels,a)
        self.close(ours[0],theirs.weights[0]); self.close(ours[1],theirs.readout)
        self.close(ours[2],theirs.weights[1])

    def test_pairs_heun_map_and_restart(self):
        scratch=Path(os.environ["ACTIVATION_NUMERICS_SCRATCH"])
        for ar in (ac.Arithmetic(),ac.Arithmetic(24,"rational")):
            activation=ac.LINEAR_SINE;s=example(activation,ar);law=data(ar)
            with ar.context():
                pairs=ac.paired_observations(s,law,activation,block_size=1)
                h0=activation.evaluate(s.g @ law.inputs.T,ar)
                H0=activation.evaluate(ac.apply_action(s,1,h0,frozen=True),ar)
                self.close(pairs["first_pairs"][:,:,0],h0)
                self.close(pairs["second_pairs"][:,:,0],H0)
                for name,p,key in (("first_pairs",s.p1,"rms1"),("second_pairs",s.p2,"rms2")):
                    values=pairs[name]; direct=ar.sqrt(p @ ((values[:,:,1]-values[:,:,0])**2) @ law.probabilities).item()
                    self.close(direct,pairs[key])
                h=ar.real(Fraction(1,1000));k=ac.rhs(s,law,activation)
                stage=s.dynamic_copy(s.w+h*k[0],s.c+h*k[1],s.M+h*k[2]);l=ac.rhs(stage,law,activation)
                expected=s.dynamic_copy(*(getattr(s,key)+(h/2)*(a+b)
                      for key,a,b in zip(("w","c","M"),k,l)))
                got=ac.evolve(s,law,activation,steps=1,step_size=Fraction(1,1000))
                for key in ARRAYS:
                    np.testing.assert_array_equal(getattr(got,key),getattr(expected,key))
                path=scratch/("restart_"+str(ar.digits)+".json")
                ac.save_restart(path,s,law,activation)
                restored,restored_law=ac.load_restart(path,activation)
                repeated=ac.evolve(restored,restored_law,activation,steps=1,step_size=Fraction(1,1000))
                for key in ARRAYS:
                    np.testing.assert_array_equal(getattr(repeated,key),getattr(got,key))
                self.assertEqual(restored.metadata,s.metadata)
                with self.assertRaises(ValueError):
                    ac.load_restart(path,ac.TANH)
                self.assertEqual(sum(getattr(got,k).size for k in ARRAYS),
                                 sum(getattr(s,k).size for k in ARRAYS))

    def test_precision_and_law_scope(self):
        states=[ac.initialize(ac.FLAT_RAMP,1,initialization_nodes=8,population_nodes=4,
                  digits=p,backend="rational") for p in (24,36)]
        for key in ARRAYS:
            errors=[abs(a.fraction()-b.fraction()) for a,b in
                    zip(getattr(states[0],key).flat,getattr(states[1],key).flat)]
            self.assertLess(max(errors),Fraction(1,10**18))
        field_values=[]
        for s in states:
            supplied=example(ac.FLAT_RAMP,s.arithmetic)
            field_values.append(ac.fields(supplied,data(s.arithmetic).inputs,ac.FLAT_RAMP))
        for key in field_values[0]:
            errors=[abs(a.fraction()-b.fraction()) for a,b in zip(field_values[0][key].flat,field_values[1][key].flat)]
            self.assertLess(max(errors),Fraction(1,10**18))
        ar=ac.Arithmetic()
        law=ac.ArcLaw("2/5","-1/25","1/30","-1/40","1/20")
        q=ac.law_quadrature(law,3,ar)
        self.assertEqual(len(q.inputs),6)
        self.assertIn("target theorem required",q.metadata["scope"])
        near=OrthogonalArcLaw(RationalRadius("1/20"),a="-1/2",b=1,c=0,d=0)
        other=ac.law_quadrature(near,3,ar,allow_collapse=False)
        self.assertEqual(len(other.inputs),4)
        self.assertFalse(other.metadata["collapsed_to_reference"])
        self.assertIn("target theorem required",other.metadata["scope"])

    def test_callback_shape_finiteness_ownership_and_binding(self):
        ar=ac.Arithmetic();z=np.array([0.,1.,2.]);before=z.copy()
        def mutate(x,ar):
            x[:]=4
            return x
        callback=ac.Activation("mutation","constant 4",mutate,lambda z,ar: z*0)
        self.close(callback.evaluate(z,ar),[4]*3)
        np.testing.assert_array_equal(z,before)
        for fn in (lambda z,ar: z[:1],lambda z,ar: np.full(z.shape,np.nan)):
            bad=ac.Activation("bad","bad callback",fn,fn)
            with self.assertRaises(ValueError):bad.evaluate(z,ar)
        with self.assertRaises(ValueError):ac.predict(example(),[[1,0]],ac.TANH)
        # The nonsmooth-second-derivative example really includes the junctions.
        self.close(ac.FLAT_RAMP.evaluate(np.array([-.5,0.,.5,1.,1.5]),ar),[0,0,.125,.5,1])
        self.close(ac.FLAT_RAMP.evaluate(np.array([-.5,0.,.5,1.,1.5]),ar,True),[0,0,.5,1,1])


if __name__=="__main__":
    resource.setrlimit(resource.RLIMIT_CPU,(120,120))
    resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
    scratch=Path(os.environ["ACTIVATION_NUMERICS_SCRATCH"])
    scratch.mkdir(parents=True,exist_ok=True)
    start=time.monotonic()
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    root=Path(__file__).resolve().parents[2]
    paths=[Path(__file__),Path(ac.__file__),Path(__file__).with_name("NUMERICAL_VALIDATION_PLAN.md")]
    paths.extend(root/"code"/"pde"/(name+".py") for name in
        ("observable_arithmetic","observable_fixed","observable_compiler","observable_words",
         "observable_solver","observable_initialization","observable_laws","finite_network"))
    record=dict(tests=result.testsRun,failures=len(result.failures),errors=len(result.errors),
        successful=result.wasSuccessful(),elapsed_wall_seconds=time.monotonic()-start,
        process_usage=dict(cpu_seconds=resource.getrusage(resource.RUSAGE_SELF).ru_utime+
          resource.getrusage(resource.RUSAGE_SELF).ru_stime,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        python=sys.version,numpy=np.__version__,platform=platform.platform(),
        command="python -B studies/cx2_activation_class_20260919/test_activation_closure.py",
        thread_environment={key:os.environ.get(key) for key in
          ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")},
        source_sha256={str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
    (scratch/"validation_record.json").write_text(json.dumps(record,indent=2)+"\n")
    sys.exit(not result.wasSuccessful())
