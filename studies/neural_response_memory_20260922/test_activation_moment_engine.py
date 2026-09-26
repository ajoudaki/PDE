"""Small CPU algebra, physical-flow, controller and runner endpoint checks."""

import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import torch

from activation_moment_engine import (ActivationDenseEngine,DeepDenseState,ActivationMomentEngine,
                                DeepMomentState,combine,controlled_error,tensor_rms)
from activation_circle_run import (heun_trial,heun_interpolant,locate_loss_crossing,
                             normalized_config,run,training_loss,sha256)


from activation_moment_engine import activation_value, activation_derivative, SELU_ALPHA, SELU_SCALE
from activation_circle_run import save_archive
from run_activation_circle_campaign import build_jobs, TOLERANCES
import torch.nn.functional as F

SCRATCH = Path(__file__).resolve().parents[2]/"data/generated/neural_response_memory_20260922/activation_circle_engine_check01"
SCRATCH.mkdir(parents=True,exist_ok=True)
REFERENCES = {"relu": F.relu, "gelu": lambda z:F.gelu(z,approximate="none"),
              "selu": F.selu, "sigmoid": torch.sigmoid}


class ActivationChecks:
    activation = "relu"
    def setUp(self):
        torch.set_num_threads(1)
        self.n,self.M,self.seed = 9,4,20260920
        angles = np.asarray([.1,.8,1.4,2.6])
        self.inputs = np.column_stack((np.cos(angles),np.sin(angles)))
        self.labels = np.asarray([1.,-1.,.5,-.4])

    def dense(self):
        return ActivationDenseEngine(2,self.n,self.inputs,self.labels,seed=self.seed,activation=self.activation)

    def moment(self,order=3,labels=None):
        return ActivationMomentEngine(2,self.n,order,self.inputs,
                                self.labels if labels is None else labels,seed=self.seed,activation=self.activation)

    def close(self,actual,expected,atol=3e-13,rtol=3e-12):
        torch.testing.assert_close(actual,expected,atol=atol,rtol=rtol)

    def noninitial(self,engine):
        state = engine.initial_state()
        gen = torch.Generator().manual_seed(817)
        state.s.fill_(.8)
        for name in ("A2","B2","A3","B3","w","c"):
            value = getattr(state,name)
            value.add_(.15*torch.randn(value.shape,generator=gen,dtype=torch.float64))
        return state

    def reconstructed(self,engine,state):
        return DeepDenseState(state.w,engine.W20+engine.reconstruct_delta_for_diagnostics(state,2),
                              engine.W30+engine.reconstruct_delta_for_diagnostics(state,3),state.c)

    def test_numpy_initialization_and_all_initial_tangents(self):
        dense = self.dense()
        state,velocity = dense.initial_state(),dense.rhs(dense.initial_state())
        rng = np.random.default_rng(self.seed)
        expected = (rng.standard_normal((self.n,2)),rng.standard_normal((self.n,self.n))/np.sqrt(self.n),
                    rng.standard_normal((self.n,self.n))/np.sqrt(self.n),rng.standard_normal(self.n)/self.n)
        for actual,wanted in zip(state.tensors(),expected):
            np.testing.assert_array_equal(actual.numpy(),wanted)
        for order in (1,2,3):
            engine = self.moment(order)
            ms = engine.initial_state()
            self.close(ms.w,state.w,atol=0,rtol=0)
            self.close(ms.c,state.c,atol=0,rtol=0)
            self.close(engine.W20,state.W2,atol=0,rtol=0)
            self.close(engine.W30,state.W3,atol=0,rtol=0)
            with patch.object(engine,"reconstruct_delta_for_diagnostics",side_effect=AssertionError("dense reconstruction")):
                mv = engine.rhs(ms)
                self.close(engine.predict(ms,self.inputs),dense.predict(state,self.inputs),atol=0,rtol=0)
            self.close(mv.w,velocity.w,atol=0,rtol=0)
            self.close(mv.c,velocity.c,atol=0,rtol=0)
            for layer in (2,3):
                left,right = engine.derivative_factors(ms,layer,mv)
                self.close(left @ right.T,getattr(velocity,"W"+str(layer)))
                self.assertEqual(float(engine.defect_frobenius(ms,layer)),0.)
                self.close(getattr(ms,"A"+str(layer)),torch.zeros_like(getattr(ms,"A"+str(layer))),atol=0,rtol=0)
                self.close(getattr(ms,"B"+str(layer))[1:],torch.zeros_like(getattr(ms,"B"+str(layer))[1:]),atol=0,rtol=0)

    def test_dense_velocity_against_independent_autograd(self):
        engine = self.dense()
        state = engine.initial_state()
        state.c.add_(torch.linspace(-.5,.6,self.n,dtype=torch.float64))
        w,W2,W3,c = (value.clone().requires_grad_() for value in state.tensors())
        activation = REFERENCES[self.activation]
        h1 = activation(w @ torch.tensor(self.inputs).T)
        h2 = activation(W2 @ h1)
        h3 = activation(W3 @ h2)
        loss = (c @ h3/self.n-torch.tensor(self.labels)).square().mean()
        gradients = torch.autograd.grad(loss,(w,W2,W3,c))
        for actual,gradient,mobility in zip(engine.rhs(state).tensors(),gradients,(self.n,1,1,self.n)):
            self.close(actual,-mobility*gradient)

    def test_both_defects_derivatives_and_adjoint_actions(self):
        engine = self.moment()
        state = self.noninitial(engine)
        velocity,fields = engine.rhs(state),engine.fields(state)
        dense_state = self.reconstructed(engine,state)
        reference = self.dense().rhs(dense_state)
        self.close(velocity.w,reference.w)
        self.close(velocity.c,reference.c)
        gen = torch.Generator().manual_seed(132)
        left_values = torch.randn((self.n,5),generator=gen,dtype=torch.float64)
        right_values = torch.randn((self.n,5),generator=gen,dtype=torch.float64)
        eps = 2e-6
        for layer in (2,3):
            matrix = getattr(dense_state,"W"+str(layer))
            self.close(engine.apply_hidden(state,layer,left_values),matrix @ left_values)
            self.close(engine.apply_hidden(state,layer,right_values,transpose=True),matrix.T @ right_values)
            self.close((engine.apply_hidden(state,layer,left_values)*right_values).sum(),
                       (left_values*engine.apply_hidden(state,layer,right_values,transpose=True)).sum())
            dl,dr = engine.derivative_factors(state,layer,velocity)
            el,er = engine.defect_factors(state,layer,fields)
            self.close(dl @ dr.T-getattr(reference,"W"+str(layer)),el @ er.T)
            self.close(engine.defect_frobenius(state,layer),torch.linalg.vector_norm(el @ er.T))
            finite_difference = (engine.reconstruct_delta_for_diagnostics(state.add_scaled(velocity,eps),layer)
                                 -engine.reconstruct_delta_for_diagnostics(state.add_scaled(velocity,-eps),layer))/(2*eps)
            self.close(finite_difference,dl @ dr.T,atol=2e-11,rtol=2e-8)

    def test_reconstructed_prediction_and_backprop_match_dense(self):
        engine = self.moment()
        state = self.noninitial(engine)
        dense = self.dense()
        ds = self.reconstructed(engine,state)
        for name,value in engine.fields(state).items():
            self.close(value,dense.fields(ds)[name])
        grid = np.column_stack((np.cos(np.arange(21)),np.sin(np.arange(21))))
        self.close(engine.predict(state,grid),dense.predict(ds,grid))

    def test_zero_residual_is_absorbing(self):
        probe = self.moment()
        labels = probe.predict(probe.initial_state(),self.inputs)
        for order in (1,2,3):
            engine = self.moment(order,labels)
            state = engine.initial_state()
            for value in engine.rhs(state).tensors():
                self.close(value,torch.zeros_like(value),atol=0,rtol=0)

    def test_stable_matrix_difference_and_fair_physical_controller(self):
        engine = self.moment()
        current = self.noninitial(engine)
        first,second,euler,candidate = heun_trial(engine,current,.003)
        ratios = []
        for a,b,c in zip(current.tensors(),euler.tensors(),candidate.tensors()):
            ratios.append(tensor_rms(c-b)/(.00001+.001*torch.maximum(tensor_rms(a),tensor_rms(c)).clamp_min(1)))
        for layer in (2,3):
            a,b,c = (engine.reconstruct_delta_for_diagnostics(state,layer) for state in (current,euler,candidate))
            expected = torch.linalg.vector_norm(c-b)
            self.close(engine.hidden_difference_norm(candidate,euler,layer),expected,atol=2e-15,rtol=2e-10)
            scale = (torch.maximum(torch.linalg.vector_norm(a),torch.linalg.vector_norm(c))/np.sqrt(self.n)).clamp_min(1)
            ratios.append(expected/np.sqrt(self.n)/(.00001+.001*scale))
        expected = float(torch.stack(ratios).max())
        with patch.object(engine,"reconstruct_delta_for_diagnostics",side_effect=AssertionError("controller constructed dense matrix")):
            actual = controlled_error(engine,current,euler,candidate,.001,.00001)
        self.assertAlmostEqual(actual,expected,places=11)

    def test_heun_extension_and_real_physical_loss_crossing(self):
        for engine in (self.dense(),self.moment()):
            state = engine.initial_state()
            first,second,euler,candidate = heun_trial(engine,state,.01)
            self.assertLess(training_loss(engine,candidate),training_loss(engine,state))
            threshold = (training_loss(engine,candidate)+training_loss(engine,state))/2
            fraction,event,loss = locate_loss_crossing(engine,state,first,second,.01,threshold)
            self.assertTrue(0 < fraction < 1)
            self.assertAlmostEqual(loss,threshold,places=10)
            for wanted,actual in zip(candidate.tensors(),heun_interpolant(state,first,second,.01,1).tensors()):
                self.close(actual,wanted,atol=0,rtol=0)

    def test_runner_endpoint_checkpoint_and_query_isolation(self):
        common = dict(inputs=[[1.,0.]],labels=[.2],width=7,seed=self.seed,rtol=.0002,
                      max_time=20.,max_steps=3000,max_wall_seconds=30.,target_loss=.025,
                      milestones=[.03,.025],query_count=32,query_batch_size=8)
        with tempfile.TemporaryDirectory(dir=SCRATCH) as directory:
            root = Path(directory)
            for model in ("dense","moment"):
                config = dict(common,model=model,order=3,activation=self.activation,observation_times=[])
                with contextlib.redirect_stdout(io.StringIO()):
                    summary = run(config,root/model)
                self.assertEqual(summary["status"],"target_loss")
                self.assertAlmostEqual(summary["training_mse"],.025,places=10)
                self.assertEqual(summary["arrays_sha256"],sha256(root/model/"arrays.npz"))
                engine = (ActivationDenseEngine(2,7,[[1.,0.]],[.2],seed=self.seed,activation=self.activation) if model == "dense"
                          else ActivationMomentEngine(2,7,3,[[1.,0.]],[.2],seed=self.seed,activation=self.activation))
                with np.load(root/model/"checkpoint_loss_0p025.npz",allow_pickle=False) as archive:
                    fields = {name:torch.tensor(archive[name]) for name in engine.initial_state().names()}
                    state = (DeepDenseState if model == "dense" else DeepMomentState)(**fields)
                    self.assertAlmostEqual(training_loss(engine,state),.025,places=10)
                with np.load(root/model/"arrays.npz",allow_pickle=False) as archive:
                    self.assertEqual(archive["circle_predictions"].shape[1],32)
                    self.assertTrue(np.all(archive["local_error_ratios"] <= 1))
                    final_a = {name:archive[name].copy() for name in engine.initial_state().names()}
                    times_a = archive["times"].copy()
                with contextlib.redirect_stdout(io.StringIO()):
                    run(dict(config,query_count=19),root/(model+"_different_query"))
                with np.load(root/(model+"_different_query")/"arrays.npz",allow_pickle=False) as archive:
                    for name,value in final_a.items():
                        np.testing.assert_array_equal(value,archive[name])
                    np.testing.assert_array_equal(times_a,archive["times"])

    def test_invalid_circle_scaling_and_capped_exact_time(self):
        config = dict(model="moment",activation=self.activation,width=7,order=2,inputs=[[1.,0.]],labels=[1.],
                      query_count=8,max_time=.025,initial_step=.02,target_loss=.000001)
        with self.assertRaises(ValueError):
            normalized_config(dict(config,inputs=[[.7071067811865475,0.]]))
        with tempfile.TemporaryDirectory(dir=SCRATCH) as directory:
            with contextlib.redirect_stdout(io.StringIO()):
                summary = run(config,Path(directory)/"capped")
            self.assertEqual(summary["status"],"max_time")
            self.assertEqual(summary["time"],.025)
            self.assertGreaterEqual(summary["integration_seconds_excluding_observations"],0.)

    def test_activation_and_derivative_independent_reference(self):
        z = torch.tensor([-100.,-12.,-2.,-.2,-1e-10,0.,1e-10,.3,2.,12.,100.],dtype=torch.float64,requires_grad=True)
        reference = REFERENCES[self.activation](z)
        derivative, = torch.autograd.grad(reference.sum(),z)
        self.close(activation_value(self.activation,z),reference,atol=3e-15)
        self.close(activation_derivative(self.activation,z),derivative,atol=3e-15)
        selected_zero = dict(relu=0.,gelu=.5,selu=SELU_SCALE*SELU_ALPHA,sigmoid=.25)[self.activation]
        self.assertEqual(float(activation_derivative(self.activation,z)[5]),selected_zero)
        extreme = torch.tensor([-1e300,-1000.,1000.,1e300],dtype=torch.float64)
        self.assertTrue(bool(torch.isfinite(activation_value(self.activation,extreme)).all()))
        self.assertTrue(bool(torch.isfinite(activation_derivative(self.activation,extreme)).all()))

    def test_initial_feature_moments_and_transport_direct_formula(self):
        engine = self.moment(3)
        state = engine.initial_state()
        h1 = REFERENCES[self.activation](state.w @ torch.tensor(self.inputs).T)
        h2 = REFERENCES[self.activation](engine.W20 @ h1)
        self.close(state.B2[0],h1)
        self.close(state.B3[0],h2)
        moments = torch.arange(3*9*4,dtype=torch.float64).reshape(3,9,4)/100
        source = torch.full((9,4),.4,dtype=torch.float64)
        expected = torch.stack((source,source-.3*(moments[1]+moments[0]),
                                source-.3*(2*moments[2]+moments[0]+3*moments[1])))
        self.close(engine.transport_moments(moments,source,.6,2.),expected)


class ReluTests(ActivationChecks,unittest.TestCase):
    activation = "relu"


class GeluTests(ActivationChecks,unittest.TestCase):
    activation = "gelu"


class SeluTests(ActivationChecks,unittest.TestCase):
    activation = "selu"


class SigmoidTests(ActivationChecks,unittest.TestCase):
    activation = "sigmoid"


class RunnerTests(unittest.TestCase):
    def test_time_interpolation_no_trajectory_feedback(self):
        config = dict(activation="gelu",model="moment",order=3,width=7,inputs=[[1.,0.]],labels=[1.],
                      query_count=8,max_time=.04,initial_step=.02,max_step=.02,
                      rtol=.1,max_steps=3,target_loss=1e-8,milestones=[],observation_times=[.005,.02,.03,.04])
        with tempfile.TemporaryDirectory(dir=SCRATCH) as directory:
            root = Path(directory)
            with contextlib.redirect_stdout(io.StringIO()):
                a = run(config,root/"observations")
                b = run(dict(config,observation_times=[],query_count=13),root/"no_observations")
            self.assertEqual(a["status"],"max_time")
            self.assertEqual(a["observed_physical_times"],[.005,.02,.03,.04])
            self.assertEqual([r["time"] for r in a["observations"]],sorted(r["time"] for r in a["observations"]))
            engine = ActivationMomentEngine(2,7,3,[[1.,0.]],[1.],activation="gelu")
            with np.load(root/"observations/arrays.npz") as aa,np.load(root/"no_observations/arrays.npz") as bb:
                for name in (*engine.initial_state().names(),"times","losses","accepted_steps","local_error_ratios"):
                    np.testing.assert_array_equal(aa[name],bb[name])
            state = engine.initial_state()
            first,second,_,_ = heun_trial(engine,state,.02)
            expected = heun_interpolant(state,first,second,.02,.25)
            with np.load(root/"observations/checkpoint_time_0p005.npz") as checkpoint:
                for name,value in zip(expected.names(),expected.tensors()):
                    np.testing.assert_array_equal(value.numpy(),checkpoint[name])
                self.assertEqual(float(checkpoint["physical_time"]),.005)

    def test_events_sorted_and_fixed_times_strictly_before_target(self):
        engine = ActivationDenseEngine(2,7,[[1.,0.]],[.2],activation="selu")
        state = engine.initial_state()
        first,second,_,candidate = heun_trial(engine,state,.02)
        initial,final = training_loss(engine,state),training_loss(engine,candidate)
        target = (initial+final)/2
        fraction,_,_ = locate_loss_crossing(engine,state,first,second,.02,target)
        target_time = .02*fraction
        config = dict(activation="selu",model="dense",width=7,inputs=[[1.,0.]],labels=[.2],
                      query_count=8,initial_step=.02,max_step=.02,rtol=1.,target_loss=target,
                      milestones=[initial-.1*(initial-final),target],
                      observation_times=[target_time/2,target_time,target_time*1.5])
        with tempfile.TemporaryDirectory(dir=SCRATCH) as directory:
            with contextlib.redirect_stdout(io.StringIO()):
                summary = run(config,Path(directory)/"run")
            self.assertEqual(summary["status"],"target_loss")
            self.assertEqual(summary["observed_physical_times"],[target_time/2])
            times = [row["time"] for row in summary["observations"]]
            self.assertEqual(times,sorted(times))
            self.assertAlmostEqual(summary["training_mse"],target,places=11)
            for row in summary["observations"]:
                self.assertIn("activation_diagnostics",row)
                self.assertIn("feature_motion_h3_rms",row)

    def test_step_and_wall_caps_and_archive_integrity(self):
        config = dict(activation="sigmoid",model="dense",width=4,inputs=[[1.,0.]],labels=[1.],
                      query_count=4,milestones=[],observation_times=[],max_steps=1,target_loss=1e-8)
        with tempfile.TemporaryDirectory(dir=SCRATCH) as directory:
            root = Path(directory)
            with contextlib.redirect_stdout(io.StringIO()):
                step = run(config,root/"steps")
                wall = run(dict(config,max_wall_seconds=1e-12),root/"wall")
            self.assertEqual(step["status"],"max_steps")
            self.assertEqual(step["accepted"],1)
            self.assertEqual(wall["status"],"wall_limit")
            self.assertEqual(wall["accepted"],0)
            self.assertTrue(step["archive_crc_validated"])
            path = root/"integrity.npz"
            save_archive(path,x=np.arange(5))
            with self.assertRaises(FileExistsError):
                save_archive(path,x=np.arange(6))
            with patch("activation_circle_run.zipfile.ZipFile.testzip",return_value="x.npy"):
                with self.assertRaises(IOError):
                    save_archive(root/"bad_crc.npz",x=np.arange(5))
            self.assertTrue((root/"bad_crc.npz").exists())

    def test_frozen_campaign_sizes_and_repetitions(self):
        cases = json.loads((Path(__file__).parent/"activation_circle_cases.json").read_text())
        pilot,primary = build_jobs("pilot",cases),build_jobs("primary",cases)
        self.assertEqual(len(pilot),8)
        self.assertEqual(len(primary),64)
        self.assertTrue(all(job["config"]["query_count"] == 128 and not job["config"]["observation_times"] for job in pilot))
        self.assertTrue(all(job["config"]["max_wall_seconds"] == 300. and len(job["config"]["milestones"]) == 7 for job in primary))
        selected = [dict(case=job["config"]["case"],model=job["config"]["model"],order=job["config"]["order"],rtol=TOLERANCES[1])
                    for job in primary if job["config"]["task"] == "two_outliers_alternating"
                    and job["config"]["rtol"] == TOLERANCES[1]
                    and (job["config"]["model"] == "dense" or job["config"]["order"] == 3)]
        repeated = build_jobs("repeat",cases,selected,primary)
        self.assertEqual(len(repeated),8)
        for row in repeated:
            original = next(job for job in primary if all(job["config"][key] == row["config"][key] for key in ("case","model","order","rtol")))
            self.assertNotEqual(original["config"]["device"],row["config"]["device"])

    def test_runtime_failure_preserves_last_valid_state(self):
        config = dict(activation="relu",model="dense",width=4,inputs=[[1.,0.]],labels=[1.],
                      query_count=4,milestones=[],observation_times=[])
        with tempfile.TemporaryDirectory(dir=SCRATCH) as directory:
            out = Path(directory)/"failed"
            with contextlib.redirect_stdout(io.StringIO()),patch.object(ActivationDenseEngine,"rhs",side_effect=RuntimeError("controlled test failure")):
                result = run(config,out)
            self.assertEqual(result["status"],"failed")
            self.assertEqual(result["accepted"],0)
            self.assertEqual(result["failure_detail"]["message"],"controlled test failure")
            self.assertTrue((out/"arrays.npz").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)

