"""Tiny fixed-step algebra and CPU synthetic-flow checks; no benchmark training."""

import argparse
import contextlib
import hashlib
import io
import json
import math
from pathlib import Path
import tempfile
import time
from unittest.mock import patch

import diverse_benchmark as runner

np, torch = runner.np, runner.torch


class LinearProbe:
    """Synthetic c'=1 and monotone event loss used only for bookkeeping."""

    def __init__(self, fail=False):
        self.fail = fail

    def prepare_data(self, inputs, labels):
        return None

    def validate_state(self, state):
        if not all(bool(torch.isfinite(getattr(state, k)).all()) for k in ("w", "c", "M")):
            raise ValueError("nonfinite probe")
        return state

    def rhs(self, state, data):
        if self.fail:
            raise ValueError("deliberate probe failure")
        return runner.TensorState(torch.zeros_like(state.w), torch.ones_like(state.c),
                                  torch.zeros_like(state.M))

    def loss(self, state, data):
        return torch.exp(-8*state.c[0])

    def predict(self, state, inputs):
        return state.c[0].expand(len(inputs)).clone()

    def observations(self, state, inputs):
        return {"rms1": torch.tensor(0.), "rms2": torch.tensor(0.)}

    def retained_bytes(self, state):
        return sum(getattr(state, k).numel()*8 for k in ("w", "c", "M"))


def check_fixed_steps(device):
    engine = runner.NetworkEngine(2, 8, 20260920, device=device, dtype=torch.float64)
    initial = engine.initial_state()
    state = runner.TensorState(initial.w + .1, initial.c + .3, initial.M + .005)
    angles = torch.arange(8, dtype=torch.float64, device=device)*math.pi/4
    inputs = torch.stack((angles.cos(), angles.sin()), dim=1)
    labels = [1, 1, -1, 1, -1, -1, 1, -1]
    data = engine.prepare_data(inputs, labels)
    identity_basis = math.sqrt(8)*torch.eye(8, dtype=torch.float64, device=device)
    closure = runner.ClosureEngine(identity_basis, initial.w, identity_basis,
                                  initial.M, dtype=torch.float64, device=device)
    closure_data = closure.prepare_data(inputs, labels)
    maximum = 0.
    invariance = 0.
    errors = []
    for h in (.001, .05, .2):
        for current, current_data in ((engine, data), (closure, closure_data)):
            before = state.numpy()
            trial, ratio = runner.heun_trial(current, state, current_data, h,
                                             initial.M, 1e-3, 1e-5)
            reference = current.heun_step(state, current_data, h)
            for name in ("w", "c", "M"):
                difference = float((getattr(trial, name)-getattr(reference, name)).abs().max())
                maximum = max(maximum, difference)
                assert difference <= 1e-15
                assert np.array_equal(before[name], getattr(state, name).cpu().numpy())
            assert math.isfinite(ratio) and ratio >= 0
            errors.append(ratio)
        full, _ = runner.heun_trial(engine, state, data, h, initial.M, 1e-3, 1e-5)
        reduced, _ = runner.heun_trial(closure, state, closure_data, h,
                                     initial.M, 1e-3, 1e-5)
        for name in ("w", "c", "M"):
            invariance = max(invariance, float((getattr(full, name)-getattr(reduced, name)).abs().max()))
    assert invariance < 2e-14
    return dict(max_fixed_step_difference=maximum, max_full_basis_difference=invariance,
                embedded_error_ratios=errors)


def check_bookkeeping(scratch_directory):
    initial = runner.TensorState(torch.zeros((1, 2), dtype=torch.float64),
                                 torch.zeros(1, dtype=torch.float64),
                                 torch.zeros((1, 1), dtype=torch.float64))
    case = next(iter(runner.CASES_V2.values()))
    results = {}
    scenarios = {
        "fitted": dict(max_time=2., max_steps=100, snapshots=[0, .1, .3, 2.]),
        "time_cap": dict(max_time=.35, max_steps=100, snapshots=[0, .1, .2, .35]),
        "step_cap": dict(max_time=2., max_steps=2, snapshots=[0, .1, .3, 2.]),
        "wall_cap": dict(max_time=2., max_steps=100, snapshots=[0, .1, .3, 2.]),
        "numerical_failure": dict(max_time=2., max_steps=100, snapshots=[0, .1, .3, 2.]),
        "initially_fitted": dict(max_time=2., max_steps=100, snapshots=[0, .1, .3, 2.]),
    }
    with tempfile.TemporaryDirectory(prefix="probe_", dir=scratch_directory) as temporary:
        for expected, config in scenarios.items():
            destination = Path(temporary)/expected
            offset = 1 if expected == "initially_fitted" else 0
            probe_initial = initial.clone()
            probe_initial.c.fill_(offset)
            worker_start = time.monotonic() - (2 if expected == "wall_cap" else 0)
            with patch.object(runner, "MAX_TIME", config["max_time"]), \
                    patch.object(runner, "MAX_STEPS", config["max_steps"]), \
                    patch.object(runner, "SNAPSHOTS", config["snapshots"]), \
                    patch.object(torch.cuda, "max_memory_allocated", return_value=0), \
                    contextlib.redirect_stdout(io.StringIO()):
                result = runner.trajectory(LinearProbe(fail=expected == "numerical_failure"),
                    probe_initial, case, destination, 1e-3, 1e-5, worker_start,
                    1 if expected == "wall_cap" else 30)
            expected_status = "fitted" if expected == "initially_fitted" else expected
            assert result["status"] == expected_status, result
            with np.load(destination/"arrays.npz", allow_pickle=False) as saved:
                times, snapshots = saved["times"], saved["snapshot_times"]
                assert times[0] == snapshots[0] == 0
                assert np.all(np.diff(times) > 0)
                assert np.all(np.diff(snapshots) > 0)
                assert times[-1] == snapshots[-1] == result["time"]
                assert np.allclose(np.diff(times), saved["accepted_steps"], atol=1e-15, rtol=0)
                assert len(times) == len(saved["losses"]) == result["steps"]+1
                assert len(saved["local_error_ratios"]) == result["steps"]
                assert np.allclose(saved["c"][:, 0], snapshots+offset, atol=1e-15, rtol=0)
                assert np.allclose(saved["circle_predictions"], snapshots[:, None]+offset, atol=1e-15, rtol=0)
                assert np.allclose(saved["losses"], np.exp(-8*(times+offset)), atol=1e-15, rtol=0)
                assert np.allclose(saved["endpoint_prediction"], times[-1]+offset, atol=1e-15, rtol=0)
                if expected == "fitted":
                    assert abs(times[-1]-math.log(1/runner.THRESHOLD)/8) < 1e-9
                    assert saved["losses"][-1] <= runner.THRESHOLD
                    assert saved["losses"][-2] > runner.THRESHOLD
                    assert np.allclose(snapshots[:-1], [0, .1, .3], atol=1e-15, rtol=0)
                if expected in ("wall_cap", "numerical_failure", "initially_fitted"):
                    assert len(times) == len(snapshots) == 1
            results[expected] = {k: result[k] for k in ("status", "steps", "time", "loss")}
    assert initial.c[0] == 0
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", choices=("cuda:0", "cuda:1"), default="cuda:0")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    runner.setup(args.device)
    torch.set_num_threads(1)
    checks = dict(device=args.device, fixed_steps=check_fixed_steps(args.device),
                  bookkeeping=check_bookkeeping(args.out.parent))
    sources = [Path(__file__), Path(runner.__file__),
               Path(runner.ROOT)/"code/pde/finite_torch.py",
               Path(runner.ROOT)/"code/pde/observable_torch_p1.py"]
    checks["sha256"] = {str(path.relative_to(runner.ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                        for path in sources}
    report = json.dumps(checks, indent=2, allow_nan=False)
    with args.out.open("x") as stream:
        stream.write(report+"\n")
    print(report)


if __name__ == "__main__":
    main()
