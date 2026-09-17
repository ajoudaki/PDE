#!/usr/bin/env python3
"""Study-owned float64 runner for the maintained nonlinear observable closure.

The initializer and portable state format are maintained APIs.  Torch executes
the same fields, vector field and simultaneous Heun update on CPU or CUDA.
Only explicit training arrays enter the vector field; circle panels are passive.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
import traceback

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "code"))
from pde.observable_arithmetic import Arithmetic
from pde.observable_initialization import InitializationLimits
from pde import observable_solver as maintained

STATE_KEYS = ("b1", "g", "w", "p1", "b2", "c", "p2", "M", "D")
HISTORY_KEYS = ("times", "predictions", "loss", "grams", "rms", "movement")


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1048576), b""):
            digest.update(chunk)
    return digest.hexdigest()


def atomic_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)


def array(value):
    return value.detach().cpu().numpy() if torch.is_tensor(value) else np.asarray(value)


def tensor_state(state, device):
    return {name: torch.tensor(getattr(state, name), dtype=torch.float64, device=device)
            for name in STATE_KEYS}


def numpy_state(state, metadata):
    return maintained.State(*(array(state[name]).copy() for name in STATE_KEYS),
                            Arithmetic(), metadata).validate()


def fields(state, inputs, backward=True):
    h1 = torch.tanh(state["w"] @ inputs.T)
    a = state["b1"].T @ (state["p1"][:, None] * h1)
    h2 = torch.tanh(state["b2"] @ (state["M"] @ a))
    f = state["p2"] @ (state["c"][:, None] * h2)
    result = dict(h1=h1, a=a, h2=h2, f=f)
    if backward:
        d = state["b2"].T @ (state["p2"][:, None] * state["c"][:, None] * (1-h2*h2))
        result.update(d=d, q=state["b1"] @ (state["M"].T @ d))
    return result


def rhs(state, inputs, labels, probabilities):
    value = fields(state, inputs)
    residual = probabilities * (value["f"] - labels)
    vw = -2 * (((1-value["h1"]*value["h1"]) * value["q"] * residual) @ inputs)
    vc = -2 * (value["h2"] @ residual)
    vM = -2 * ((value["d"] * residual) @ value["a"].T)
    return vw, vc, vM


def heun(state, inputs, labels, probabilities, h):
    first = rhs(state, inputs, labels, probabilities)
    stage = dict(state)
    for name, velocity in zip(("w", "c", "M"), first):
        stage[name] = state[name] + h*velocity
    second = rhs(stage, inputs, labels, probabilities)
    for name, left, right in zip(("w", "c", "M"), first, second):
        state[name] = state[name] + (h/2)*(left+right)


def predict(state, inputs, block_size=128):
    return torch.cat([fields(state, inputs[start:start+block_size], False)["f"]
                      for start in range(0, len(inputs), block_size)])


def training_observation(state, inputs, labels, probabilities, initial_h):
    value = fields(state, inputs, False)
    grams, rms, movement = [], [], []
    for layer, name in enumerate(("h1", "h2")):
        actual = value[name]
        population = state["p1" if layer == 0 else "p2"]
        grams.append(actual.T @ (population[:, None]*actual))
        rms.append(torch.sqrt(population @ (actual*actual) @ probabilities))
        difference = actual-initial_h[layer]
        movement.append(torch.sqrt(population @ (difference*difference) @ probabilities))
    residual = value["f"]-labels
    return dict(prediction=value["f"], loss=probabilities @ (residual*residual),
                grams=torch.stack(grams), rms=torch.stack(rms), movement=torch.stack(movement))


def plateau(history, t_min):
    """Two complete 25-unit windows, checked only at a multiple of 25."""
    now = float(history["times"][-1])
    if now < t_min-1e-9 or abs(now/25-round(now/25)) > 1e-9:
        return False, None
    times = np.asarray(history["times"])
    indexes = []
    for wanted in (now-50, now-25, now):
        found = np.flatnonzero(np.isclose(times, wanted, atol=1e-8, rtol=0))
        if not len(found):
            return False, None
        indexes.append(int(found[-1]))
    # The complete saved circle follows the training part of each row.
    m = int(history["train_count"])
    changes = [float(np.max(np.abs(history["predictions"][b][m:]
                                 - history["predictions"][a][m:])))
               for a, b in zip(indexes, indexes[1:])]
    losses = [float(abs(history["loss"][b]-history["loss"][a]))
              for a, b in zip(indexes, indexes[1:])]
    return all(x < .005 for x in changes) and all(x < .0005 for x in losses), {
        "window_output_sup": changes, "window_loss_change": losses}


def wrapper_path(restart_path):
    restart_path = Path(restart_path)
    return restart_path.with_name(restart_path.name.replace("_restart.json", "_wrapper.npz"))


def save_checkpoint(path, state, metadata, data, initial_h, history, config, input_hash):
    path = Path(path)
    current = numpy_state(state, metadata)
    temporary = path.with_name(path.name + ".tmp")
    maintained.save_restart(temporary, current, data)
    temporary.replace(path)
    supplement = wrapper_path(path)
    with supplement.with_name(supplement.name + ".tmp").open("wb") as handle:
        np.savez_compressed(handle, **{key: np.asarray(history[key]) for key in HISTORY_KEYS},
                            initial_h1=array(initial_h[0]), initial_h2=array(initial_h[1]),
                            config_json=np.array(json.dumps(config, sort_keys=True)),
                            inputs_sha256=np.array(input_hash), train_count=np.array(len(data.inputs)))
    supplement.with_name(supplement.name + ".tmp").replace(supplement)
    return current


def equation_check(device="cpu"):
    """Small deterministic implementation fixture; not a scientific trajectory."""
    rng = np.random.default_rng(84017)
    original = maintained.initialize(order=3, initialization_nodes=128, population_nodes=64)
    original.w += .07*rng.standard_normal(original.w.shape)
    original.c[:] = .13*rng.standard_normal(original.c.shape)
    original.M += .025*rng.standard_normal(original.M.shape)
    original.validate()
    angles = np.array([.13, .47, 1.01, 1.77, 2.38])
    inputs = np.column_stack((np.cos(angles), np.sin(angles)))
    labels = np.array([.6, -.8, .2, .9, -.3])
    probabilities = np.array([.1, .15, .25, .2, .3])
    data = maintained.DataLaw(inputs, labels, probabilities).validate(original.arithmetic)
    state = tensor_state(original, device)
    u, y, p = (torch.tensor(v, dtype=torch.float64, device=device)
               for v in (inputs, labels, probabilities))
    checks = {}
    expected = maintained._fields(original, inputs)
    actual = fields(state, u)
    for name in expected:
        checks["fields_"+name] = float(np.max(np.abs(expected[name]-array(actual[name]))))
    expected_rhs = maintained.rhs(original, data, block_size=len(inputs))
    actual_rhs = rhs(state, u, y, p)
    for name, left, right in zip(("w", "c", "M"), expected_rhs, actual_rhs):
        checks["rhs_"+name] = float(np.max(np.abs(left-array(right))))
    # Autograd gradients use the population metric of the maintained dynamics.
    differentiable = dict(state)
    for name in ("w", "c", "M"):
        differentiable[name] = state[name].clone().requires_grad_(True)
    residual = fields(differentiable, u, False)["f"]-y
    objective = p @ (residual*residual)
    gradients = torch.autograd.grad(objective, [differentiable[k] for k in ("w", "c", "M")])
    metric_gradients = (-gradients[0]/state["p1"][:, None],
                        -gradients[1]/state["p2"], -gradients[2])
    for name, left, right in zip(("w", "c", "M"), actual_rhs, metric_gradients):
        checks["autograd_"+name] = float(torch.max(torch.abs(left-right)).detach().cpu())
    h = .013
    maintained_next = maintained.evolve(original, data, steps=1, step_size=h, block_size=len(inputs))
    heun(state, u, y, p, h)
    for name in ("w", "c", "M"):
        checks["heun_"+name] = float(np.max(np.abs(getattr(maintained_next, name)-array(state[name]))))
    checks["passed"] = max(checks.values()) <= 1e-10
    checks["device"] = str(device)
    if not checks["passed"]:
        raise AssertionError(json.dumps(checks))
    return checks


def execute(config_path, out_path, resume=None):
    began = time.monotonic()
    config_path, out = Path(config_path).resolve(), Path(out_path).resolve()
    config = json.loads(config_path.read_text())
    device = str(config.get("device", "cpu"))
    if device.startswith("cuda"):
        torch.cuda.set_device(torch.device(device))
    torch.set_num_threads(1)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    out.mkdir(parents=True, exist_ok=True)
    if (out/"record.json").exists() or (out/"trajectories.npz").exists():
        raise ValueError("output already contains a run; use a fresh output directory")
    record = dict(status="running", settled=False, config=config, last_time=None,
                  config_path=str(config_path), device=device, dtype="float64",
                  python=sys.version, numpy=np.__version__, torch=torch.__version__,
                  checks={}, hashes={"config": sha256(config_path), "runner": sha256(__file__),
                                     "plan": sha256(Path(__file__).with_name("CAMPAIGN_PLAN.md")),
                                     "solver": sha256(ROOT/"code/pde/observable_solver.py"),
                                     "initializer": sha256(ROOT/"code/pde/observable_initialization.py"),
                                     "words": sha256(ROOT/"code/pde/observable_words.py")})
    atomic_json(out/"record.json", record)
    try:
        input_path = Path(config["inputs_path"])
        if not input_path.is_absolute():
            input_path = (config_path.parent/input_path).resolve()
        input_hash = sha256(input_path)
        record["hashes"]["inputs"] = input_hash
        with np.load(input_path, allow_pickle=False) as inputs_file:
            panels = {name: inputs_file[name].copy() for name in inputs_file.files}
        required = ("train_u", "labels", "probabilities", "circle_u", "circle_theta", "dense_u", "dense_theta")
        if not all(name in panels for name in required):
            raise ValueError("input archive lacks a required array")
        data = maintained.DataLaw(panels["train_u"], panels["labels"], panels["probabilities"],
                                  {"scope": "exploratory endpoint-discrimination campaign",
                                   "inputs_sha256": input_hash}).validate(Arithmetic())
        for name in ("circle_u", "dense_u"):
            maintained._unit_inputs(panels[name], Arithmetic())
        h = float(config.get("h", .02))
        obs_dt = float(config.get("obs_dt", 5))
        t_min, t_max = float(config.get("t_min", 100)), float(config.get("t_max", 600))
        if h <= 0 or obs_dt <= 0 or t_max < 0:
            raise ValueError("invalid step or horizon")
        for duration in (obs_dt, t_max):
            if abs(duration/h-round(duration/h)) > 1e-7:
                raise ValueError("observation interval and endpoint must be multiples of h")
        record["checks"]["equations"] = equation_check(device)
        if resume:
            resume = Path(resume).resolve()
            original, restored_data = maintained.load_restart(resume)
            for name, expected in (("inputs", data.inputs), ("labels", data.labels),
                                   ("probabilities", data.probabilities)):
                if not np.array_equal(getattr(restored_data, name), expected):
                    raise ValueError("resume data differ from configured data")
            with np.load(wrapper_path(resume), allow_pickle=False) as previous:
                old_config = json.loads(str(previous["config_json"]))
                for key in ("order", "Q", "P", "h"):
                    if old_config[key] != config[key]:
                        raise ValueError("resume changed fixed configuration " + key)
                if str(previous["inputs_sha256"]) != input_hash:
                    raise ValueError("resume input archive hash differs")
                history = {key: list(previous[key]) for key in HISTORY_KEYS}
                history["train_count"] = len(data.inputs)
                h0_arrays = [previous["initial_h1"].copy(), previous["initial_h2"].copy()]
            start_time = float(history["times"][-1])
            state = tensor_state(original, device)
            initial_h = [torch.tensor(v, dtype=torch.float64, device=device) for v in h0_arrays]
            record["resume_from"] = str(resume)
            record["hashes"]["resume_state"] = sha256(resume)
            record["hashes"]["resume_wrapper"] = sha256(wrapper_path(resume))
        else:
            limits = None
            if int(config["Q"]) > 16384 or int(config["P"]) > 8192:
                limits = InitializationLimits(max_working_bytes=2*1024**3, max_work_units=8000000000)
            original = maintained.initialize(order=int(config["order"]),
                                             initialization_nodes=int(config["Q"]),
                                             population_nodes=int(config["P"]), limits=limits)
            state = tensor_state(original, device)
            initial_h = None
            start_time = 0.
            history = {key: [] for key in HISTORY_KEYS}
            history["train_count"] = len(data.inputs)
        if start_time > t_max+1e-9:
            raise ValueError("resume time exceeds endpoint")
        metadata = original.metadata
        record["initialization_metadata"] = metadata
        u, labels, probabilities, circle_u, dense_u = [
            torch.tensor(v, dtype=torch.float64, device=device) for v in
            (data.inputs, data.labels, data.probabilities, panels["circle_u"], panels["dense_u"])]
        if initial_h is None:
            initial = fields(state, u, False)
            initial_h = [initial["h1"].clone(), initial["h2"].clone()]
        record["initialization_elapsed_seconds"] = time.monotonic()-began
        atomic_json(out/"record.json", record)
        settled, plateau_values = False, None
        total_steps, current_step = int(round(t_max/h)), int(round(start_time/h))
        observation_steps = int(round(obs_dt/h))

        def observe(now):
            nonlocal settled, plateau_values
            observed = training_observation(state, u, labels, probabilities, initial_h)
            predictions = torch.cat((observed["prediction"], predict(state, circle_u)))
            values = dict(times=float(now), predictions=array(predictions).copy(),
                          loss=float(observed["loss"].cpu()), grams=array(observed["grams"]).copy(),
                          rms=array(observed["rms"]).copy(), movement=array(observed["movement"]).copy())
            if not all(np.all(np.isfinite(value)) for value in values.values()):
                raise ValueError("nonfinite saved observation")
            for key in HISTORY_KEYS:
                history[key].append(values[key])
            if len(history["loss"]) > 1 and values["loss"]-history["loss"][-2] > 1e-5:
                raise ValueError("loss increased by more than 1e-5 per saved interval")
            settled, plateau_values = plateau(history, t_min)
            record.update(last_time=float(now), settled=settled, plateau=plateau_values,
                          last_loss=values["loss"], elapsed_seconds=time.monotonic()-began)
            atomic_json(out/"record.json", record)
            print(json.dumps({"id": config.get("id"), "time": float(now), "loss": values["loss"],
                              "settled": settled}), flush=True)

        with torch.no_grad():
            if not history["times"]:
                observe(0.)
            else:
                replay = torch.cat((predict(state, u), predict(state, circle_u)))
                resume_error = float(np.max(np.abs(array(replay)-history["predictions"][-1])))
                record["checks"]["resume_prediction_max_error"] = resume_error
                if resume_error > 1e-10:
                    raise ValueError("resume endpoint replay differs")
            while current_step < total_steps:
                if time.monotonic()-began > 1180:
                    raise TimeoutError("worker approaching declared 1200-second cap")
                stop_step = min(current_step+observation_steps, total_steps)
                for _ in range(current_step, stop_step):
                    heun(state, u, labels, probabilities, h)
                current_step = stop_step
                now = current_step*h
                observe(now)
                if abs(now/100-round(now/100)) < 1e-8:
                    save_checkpoint(out/f"t{int(round(now)):04d}_restart.json", state, metadata,
                                    data, initial_h, history, config, input_hash)
                if settled and bool(config.get("auto_stop", True)):
                    break
            # A forced endpoint may lie between the 25-unit plateau checks.
            settled, plateau_values = plateau(history, t_min)
            final_dense = array(predict(state, dense_u)).copy()
            passive_angles = 2*np.pi*np.arange(128)/128
            passive_u = torch.tensor(np.column_stack((np.cos(passive_angles), np.sin(passive_angles))),
                                     dtype=torch.float64, device=device)
            passive = fields(state, passive_u, False)
            passive_grams = np.stack([array(passive[k].T @ (state[p][:, None]*passive[k]))
                                     for k, p in (("h1", "p1"), ("h2", "p2"))])
            odd_error = float(torch.max(torch.abs(predict(state, circle_u)+predict(state, -circle_u))).cpu())
        final_state = save_checkpoint(out/"final_restart.json", state, metadata, data, initial_h,
                                      history, config, input_hash)
        restored_state, restored_data = maintained.load_restart(out/"final_restart.json")
        restart_exact = all(np.array_equal(getattr(final_state, key), getattr(restored_state, key))
                            for key in STATE_KEYS)
        # Replay in maintained NumPy, including all dense final plotted points.
        replay_dense = maintained.predict(restored_state, panels["dense_u"], block_size=128)
        replay_error = float(np.max(np.abs(replay_dense-final_dense)))
        maintained_pairs = maintained.paired_observations(restored_state, restored_data, include_pairs=False)
        movement_error = float(np.max(np.abs(np.array([maintained_pairs["rms1"], maintained_pairs["rms2"]])
                                                - np.asarray(history["movement"][-1]))))
        gram_array = np.asarray(history["grams"])
        gram_symmetry = float(np.max(np.abs(gram_array-np.swapaxes(gram_array, -1, -2))))
        gram_min_eigenvalue = float(np.min(np.linalg.eigvalsh(gram_array)))
        rms_identity = float(np.max(np.abs(np.asarray(history["rms"])**2
                              - np.einsum("tlm,m->tl", np.diagonal(gram_array, axis1=-2, axis2=-1), data.probabilities))))
        mse_identity = float(np.max(np.abs(np.asarray(history["loss"])
                         - np.sum((np.asarray(history["predictions"])[:, :len(data.inputs)]-data.labels)**2
                                  *data.probabilities, axis=1))))
        record["checks"].update(restart_arrays_exact=restart_exact, dense_replay_max_error=replay_error,
                                oddness_max_error=odd_error, paired_movement_max_error=movement_error,
                                gram_symmetry_max_error=gram_symmetry, gram_min_eigenvalue=gram_min_eigenvalue,
                                rms_identity_max_error=rms_identity, mse_identity_max_error=mse_identity)
        with (out/"trajectories.npz").open("wb") as handle:
            np.savez_compressed(handle, **{key: np.asarray(history[key]) for key in HISTORY_KEYS},
                                dense_predictions=final_dense, passive_grams_final=passive_grams,
                                passive_theta=passive_angles, **panels)
        if (not restart_exact or max(replay_error, odd_error, movement_error, gram_symmetry,
                                     rms_identity, mse_identity) > 1e-10 or gram_min_eigenvalue < -1e-5):
            raise AssertionError("final numerical identity gate failed: " + json.dumps(record["checks"]))
        record.update(status="complete", settled=settled, plateau=plateau_values,
                      last_time=float(history["times"][-1]), elapsed_seconds=time.monotonic()-began,
                      checkpoint=str(out/"final_restart.json"), wrapper=str(out/"final_wrapper.npz"))
        for name in ("trajectories.npz", "final_restart.json", "final_wrapper.npz"):
            record["hashes"][name] = sha256(out/name)
        atomic_json(out/"record.json", record)
        return record
    except BaseException as error:
        record.update(status="failed", error=str(error), traceback=traceback.format_exc(),
                      elapsed_seconds=time.monotonic()-began)
        # Preserve the last available state/history without concealing failure.
        available = locals()
        if all(name in available for name in ("state", "metadata", "data", "initial_h", "history", "input_hash")):
            try:
                save_checkpoint(out/"failed_restart.json", state, metadata, data, initial_h,
                                history, config, input_hash)
                np.savez_compressed(out/"partial_trajectories.npz",
                                    **{key: np.asarray(history[key]) for key in HISTORY_KEYS})
            except BaseException:
                record["checkpoint_error"] = traceback.format_exc()
        atomic_json(out/"record.json", record)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config")
    parser.add_argument("--out", "--outDIR", dest="out")
    parser.add_argument("--resume")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--device", default="cpu", help="device for --check only")
    args = parser.parse_args()
    torch.set_num_threads(1)
    if args.check:
        print(json.dumps(equation_check(args.device), indent=2))
        return
    if not args.config or not args.out:
        parser.error("--config and --out are required for a run")
    execute(args.config, args.out, args.resume)


if __name__ == "__main__":
    main()
