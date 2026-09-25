"""Small CPU implementation checks; no scientific training or CUDA execution."""
import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
import tempfile

import numpy as np
import torch

import closure_transfer_euler as runner
from activation_moment_engine import ActivationMomentEngine, activation_value
from deep_moment_engine import DeepMomentState, combine


def check(output):
    output = Path(output).resolve(); output.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    checks, worst = 0, 0.
    def near(actual, expected):
        nonlocal checks, worst
        torch.testing.assert_close(actual, expected, rtol=2e-12, atol=2e-13)
        worst = max(worst, float((actual-expected).abs().max()))
        checks += 1
    inputs, labels, _ = runner.task_data(runner.HERE/"activation_circle_cases.json", "selu", "quadrant_alternating")
    for activation in ("relu", "gelu", "selu"):
        for order in (1,2,3):
            engine = runner.CachedEulerEngine(2,7,order,inputs,labels,activation=activation)
            original = ActivationMomentEngine(2,7,order,inputs,labels,activation=activation)
            state, reference = engine.initial_state(), original.initial_state()
            initial_copy = engine.initial.clone()
            rng = np.random.default_rng(20260920)
            for actual, expected in zip((state.w, engine.W20, engine.W30, state.c),
                    (rng.standard_normal((7,2)),rng.standard_normal((7,7))/math.sqrt(7),
                     rng.standard_normal((7,7))/math.sqrt(7),rng.standard_normal(7)/7)):
                near(actual, torch.tensor(expected))
            h1 = activation_value(activation, state.w@engine.inputs.T)
            h2 = activation_value(activation, engine.W20@h1)
            near(state.B2[0],h1); near(state.B3[0],h2)
            assert not torch.count_nonzero(state.A2) and not torch.count_nonzero(state.A3)
            assert not torch.count_nonzero(state.B2[1:]) and not torch.count_nonzero(state.B3[1:])
            stage = runner.EulerStage(engine,state)
            for _ in range(12):
                velocity, loss, valid = stage.evaluate()
                assert valid
                expected_velocity = original.rhs(reference)
                for actual, expected in zip(velocity.tensors(),expected_velocity.tensors()): near(actual,expected)
                near(torch.tensor(loss), original.fields(reference)["loss"].float())
                expected = combine((1.,.003),(reference,expected_velocity))
                runner.euler_update(state,velocity,.003)
                reference = expected
                for actual, expected in zip(state.tensors(),reference.tensors()): near(actual,expected)
            for actual, expected in zip(engine.initial.tensors(),initial_copy.tensors()): near(actual,expected)
            # Independent nested-sum transport, without the implementation cumsum.
            fields = engine.fields(state)
            for layer in (2,3):
                for name, source in (("A",fields["delta"+str(layer)]*fields["r"]),
                                     ("B",fields["rho"]*fields["h"+str(layer-1)])):
                    moment = getattr(state,name+str(layer))
                    explicit = torch.stack([source-fields["rho"]/(1+state.s)*(j*moment[j]+
                        sum(((2*k+1)*moment[k] for k in range(j)),torch.zeros_like(source))) for j in range(order)])
                    near(engine.transport_moments(moment,source,fields["rho"],1+state.s),explicit)
            # Check forward and transpose against explicitly reconstructed matrices.
            values = torch.tensor(np.random.default_rng(44).standard_normal((7,11)))
            for layer in (2,3):
                left,right = engine.delta_factors(state,layer)
                matrix = getattr(engine,"W"+str(layer)+"0")+left@right.T
                near(engine.apply_hidden(state,layer,values),matrix@values)
                near(engine.apply_hidden(state,layer,values,transpose=True),matrix.T@values)
            query = torch.tensor(inputs[:3])
            near(engine.predict(state,query),original.predict(reference,query))
            # Exact zero residual at a noninitial state freezes every block.
            engine.labels.copy_(engine.fields(state)["f"])
            velocity, loss, valid = stage.evaluate()
            assert valid and loss == 0 and all(torch.count_nonzero(value)==0 for value in velocity.tensors())
            checks += 1
            state.w = state.w.clone()
            try: stage.evaluate()
            except ValueError: checks += 1
            else: raise AssertionError("Replaced graph-bound state storage was accepted")
    # Actual tiny runner output: endpoint and every archive use the same update count.
    def args(name, **changes):
        values = dict(activation="selu",task="quadrant_alternating",P=3,step=.001,device="cpu",
                      out=str(output/name),max_seconds=20.,max_time=260.,max_steps=3,target_mse=1e-8,
                      backend="eager",cases_json=str(runner.HERE/"activation_circle_cases.json"))
        values.update(changes)
        return argparse.Namespace(**values)
    for name, changes, status, count in (("steps",{},"max_steps",3),
            ("time",dict(max_time=.002),"max_time",2),
            ("wall",dict(max_seconds=1e-12),"wall_limit",0),
            ("target",dict(target_mse=2.),"target_loss",0)):
        summary = runner.run(args(name,**changes),width=7)
        assert summary["status"] == status and summary["updates"] == count
        directory = output/name
        with np.load(directory/"state.npz") as archive:
            saved = DeepMomentState(*(torch.tensor(archive[key]) for key in ("w","c","A2","B2","A3","B3","s")))
            assert float(archive["physical_time"]) == count*.001 and int(archive["steps"]) == count
        engine = runner.CachedEulerEngine(2,7,3,inputs,labels,activation="selu")
        with np.load(directory/"predictions.npz") as archive:
            predicted = engine.predict(saved,inputs)
            near(predicted,torch.tensor(archive["train_predictions"]))
            near(engine.predict(saved,archive["circle_inputs"]),torch.tensor(archive["circle_predictions"]))
            mse = float(((predicted-engine.labels)**2).mean())
            assert abs(mse-summary["training_mse"]) < 1e-14
        with np.load(directory/"loss_trace.npz") as archive:
            assert len(archive["losses"]) == count+1
            assert np.array_equal(archive["physical_times"],.001*np.arange(count+1))
            assert abs(archive["losses"][-1]-mse) < 1e-14
        assert summary["config_sha256"] == runner.sha256(directory/"config.json")
        assert all(runner.sha256(directory/key)==value for key,value in summary["artifact_sha256"].items())
        try: runner.run(args(name,**changes),width=7)
        except FileExistsError: checks += 1
        else: raise AssertionError("Existing output was overwritten")
        checks += 1
    receipt = dict(passed=True,device="cpu",checks=checks,max_absolute_difference=worst,
                   runner_sha256=runner.sha256(runner.__file__),test_sha256=runner.sha256(__file__))
    runner.write_json(output/"receipt.json",receipt)
    return receipt


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out",required=True)
    print(json.dumps(check(parser.parse_args().out),indent=2))
