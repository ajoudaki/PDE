"""Deterministic algebra/initializer/restart checks; no training experiment.

Declared scope: dimensions 1,2,3,7; orders 1 and 3; finite supplied
states and at most two Heun steps. One process/thread, <120 s, no refinement
search. Pass thresholds: exact shape/restart; 2e-12 source/adapter identities;
3e-6 relative finite-difference gradients; 2e-12 rational/float agreement.
Results validate implementation identities, not order convergence or fitting.
Enumeration regressions use small degrees
and construction of the d=600/order=1 dictionary without initialization.
"""
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import time
import unittest

import numpy as np
import cx1_closure as c
from pde.observable_compiler import GaussianCompiler
from pde.observable_arithmetic import Arithmetic, gaussian_points
from pde.observable_initialization import _all_exponents as reference_exponents

OUTPUT = Path(os.environ.get("CX1_CLOSURE_CHECK_OUTPUT",
    "data/generated/cx1_many_point_closure_20260919/closure/deterministic_v1"))


class ClosureChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = c.initialize(3, 3, initialization_nodes=64, population_nodes=32)
        ar = cls.base.arithmetic
        cls.data = c.DataLaw(ar.array([[1,0,0], [Fraction(40,401),Fraction(399,401),0],
            [0,Fraction(40,401),Fraction(399,401)]]), ar.array([1,-1,1]),
            ar.array([Fraction(1,3)]*3)).validate(ar)

    def test_genuine_enrichment_and_dimension(self):
        for d in (1,2,3,7):
            low, high = c.build_dictionary(d,1), c.build_dictionary(d,3)
            self.assertEqual(low.core_dimensions, (1+2*d,1+d))
            self.assertEqual(high.core_dimensions, (c.math.comb(3+2*d,2*d),c.math.comb(3+d,d)))
            self.assertGreater(high.core_dimensions[0], low.core_dimensions[0])
            self.assertGreater(high.core_dimensions[1], low.core_dimensions[1])
        self.assertEqual(self.base.w.shape, (32,3))
        self.assertEqual(self.base.M.shape, (21,85))
        self.assertGreater(self.base.metadata['source_counts'][0], 3)
        self.assertGreater(self.base.metadata['source_counts'][1], 3)

    def test_iterative_exponents_have_no_recursion_dimension_ceiling(self):
        for dimension in (1,2,3,4):
            for order in range(5):
                self.assertEqual(tuple(c._all_exponents(order,dimension)),
                                 reference_exponents(order,dimension))
        high = c.build_dictionary(600,1)
        self.assertEqual(high.core_dimensions,(1201,601))
        self.assertEqual((len(high.first_words),len(high.second_words)),(1202,602))

    def test_dimension_adapter_matches_maintained_compiler(self):
        dictionary = c.build_dictionary(2,3)
        words = dictionary.first_words+dictionary.second_words
        union = words+tuple(c.node('action', w) for w in words)
        ar = Arithmetic()
        old = GaussianCompiler(ar,gaussian_points,32,Fraction(1,1000)).compile(union,population_nodes=17)
        new = c.DimensionCompiler(2,ar,gaussian_points,32,Fraction(1,1000)).compile(union,population_nodes=17)
        for group in (dictionary.first_words,dictionary.second_words):
            np.testing.assert_allclose(new.table(group,17),old.table(group,17),rtol=0,atol=2e-12)
        for pop in (1,2):
            np.testing.assert_allclose(new.factors[pop],old.factors[pop],rtol=0,atol=2e-12)

    def test_forward_reverse_response_and_high_seed(self):
        g = c.node('g7')
        h = c.node('sin',g)
        xi = c.node('action',h)
        H = c.node('sin',xi)
        reverse = c.node('action',H)
        forward_again = c.node('action',c.node('tanh',reverse))
        ar = Arithmetic()
        program = c.DimensionCompiler(7,ar,gaussian_points,128,Fraction(1,1000)).compile((reverse,forward_again))
        source = program.sources[program._word(reverse,allow_new=False)]
        alpha = np.mean(np.cos(program.evaluate(xi)))
        self.assertEqual(len(source.response),1)
        self.assertAlmostEqual(source.response[0][1],alpha,places=13)
        noise = program._normals[1][:,7]*program.factors[1][0,0]
        np.testing.assert_allclose(program.evaluate(reverse),noise+alpha*program.evaluate(h),atol=2e-12,rtol=0)
        _, derivative = program.evaluate(reverse,derivative=True)
        np.testing.assert_allclose(derivative,np.ones((128,1)),atol=0,rtol=0)
        again_source = program.sources[program._word(forward_again,allow_new=False)]
        self.assertGreater(abs(again_source.response[0][1]),0)
        replay = program.evaluate(reverse,37)
        self.assertEqual(replay.shape,(37,))

    def supplied_state(self):
        state = self.base.copy()
        state.w += .02*np.sin(np.arange(state.w.size).reshape(state.w.shape))
        state.c[:] = .2*np.sin(np.arange(len(state.c))+.3)
        state.M += .003*np.cos(np.arange(state.M.size).reshape(state.M.shape))
        return state

    def test_actual_adjoint_and_complete_gradients(self):
        state = self.supplied_state()
        a = np.sin(np.arange(len(state.b1))+.2)
        b = np.cos(np.arange(len(state.b2))+.1)
        left = state.p2 @ (b*c.apply_action(state,a))
        right = state.p1 @ (a*c.apply_action(state,b,reverse=True))
        self.assertAlmostEqual(left,right,places=12)
        velocity = c.rhs(state,self.data)
        h = 2e-6
        checks = [("w",(0,0),0,state.p1[0]),("w",(3,2),0,state.p1[3]),
                  ("c",(4,),1,state.p2[4]),("M",(2,7),2,1), ("M",(20,84),2,1)]
        for name,index,block,weight in checks:
            plus,minus=state.copy(),state.copy()
            getattr(plus,name)[index]+=h
            getattr(minus,name)[index]-=h
            derivative=(c.loss(plus,self.data)-c.loss(minus,self.data))/(2*h)
            expected=-weight*velocity[block][index]
            self.assertLess(abs(derivative-expected),3e-6*max(1,abs(expected)))
        plus=state.dynamic_copy(*(getattr(state,k)+h*v for k,v in zip(('w','c','M'),velocity)))
        minus=state.dynamic_copy(*(getattr(state,k)-h*v for k,v in zip(('w','c','M'),velocity)))
        derivative=(c.loss(plus,self.data)-c.loss(minus,self.data))/(2*h)
        energy=state.p1 @ np.sum(velocity[0]**2,axis=1)+state.p2 @ (velocity[1]**2)+np.sum(velocity[2]**2)
        self.assertLess(abs(derivative+energy),3e-6*max(1,energy))

    def test_joint_observations_and_restart(self):
        state=self.supplied_state()
        h=c.node('tanh',c.Word('w1',1))
        upper=c.node('action',h)
        reverse=c.node('action',c.node('sin',upper))
        observed,p=c.observe(state,(c.Word('g1',1),c.Word('w1',1),reverse))
        np.testing.assert_array_equal(observed[:,0],state.g[:,0])
        np.testing.assert_array_equal(observed[:,1],state.w[:,0])
        np.testing.assert_allclose(observed[:,2],c.apply_action(state,np.sin(c.apply_action(state,np.tanh(state.w[:,0]))),reverse=True))
        np.testing.assert_array_equal(p,state.p1)
        pairs=c.paired_observations(state,self.data)
        self.assertEqual(pairs['first_pairs'].shape,(32,3,2))
        checkpoint=OUTPUT/'restart.json'
        c.save_restart(checkpoint,state,self.data)
        restored,data=c.load_restart(checkpoint)
        for name in c._ARRAYS:
            np.testing.assert_array_equal(getattr(restored,name),getattr(state,name))
        direct=c.evolve(state,self.data,steps=2,step_size=Fraction(1,100000))
        split=c.evolve(restored,data,steps=1,step_size=Fraction(1,100000))
        split=c.evolve(split,data,steps=1,step_size=Fraction(1,100000))
        for name in ('w','c','M'):
            np.testing.assert_array_equal(getattr(direct,name),getattr(split,name))
        self.assertEqual(direct.b1.shape,state.b1.shape)

    def test_rational_backend_and_fail_closed(self):
        small=c.initialize(1,1,initialization_nodes=2,population_nodes=3,digits=20,backend='rational')
        floating=c.initialize(1,1,initialization_nodes=2,population_nodes=3)
        for name in ('b1','b2','D','g'):
            np.testing.assert_allclose(np.asarray(getattr(small,name),float),getattr(floating,name),atol=2e-12,rtol=2e-12)
        ar=small.arithmetic
        data=c.DataLaw(ar.array([[1],[-1]]),ar.array([1,-1]),ar.array([Fraction(1,2)]*2)).validate(ar)
        updated=c.evolve(small,data,steps=1,step_size=Fraction(1,100000))
        c.save_restart(OUTPUT/'rational_restart.json',updated,data)
        restored,_=c.load_restart(OUTPUT/'rational_restart.json')
        for name in c._ARRAYS:
            np.testing.assert_array_equal(getattr(restored,name),getattr(updated,name))
        with self.assertRaises(c.CompilerResourceLimit):
            c.build_dictionary(7,3,max_features=4)
        with self.assertRaises(ValueError):
            c.fields(floating,[[2]])


if __name__ == '__main__':
    OUTPUT.mkdir(parents=True,exist_ok=False)
    start=time.monotonic()
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ClosureChecks))
    record=dict(success=result.wasSuccessful(),tests=result.testsRun,failures=len(result.failures),errors=len(result.errors),
                seconds=time.monotonic()-start,scope='deterministic identities; no training accuracy conclusion',
                hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),Path(c.__file__))})
    (OUTPUT/'results.json').write_text(json.dumps(record,indent=2)+'\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
