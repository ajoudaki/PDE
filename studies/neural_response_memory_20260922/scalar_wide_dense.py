"""GPU dense reference for the scalar hierarchy's wide-circle comparison.

No initialization or model convention is changed: float64 parameters come
directly from scalar_aggregate_engine.initialize_network, inputs are already
normalized, f=c@h3/n, and MSE gradient flow has mobilities (n,1,1,n).
The existing adaptive Euler/Heun controller and quadratic event interpolant
are reused. This module does not authorize or launch a campaign on import.
"""

import argparse
import json
import math
import os
from pathlib import Path
import platform
import resource
import sys
import time
import traceback

import numpy as np
import torch

import scalar_aggregate_engine as aggregate
from deep_moment_engine import DeepDenseEngine, DeepDenseState, controlled_error
from deep_circle_run import (ERROR_CONTROL, array_hash, heun_trial,
                             locate_loss_crossing, panel_predict,
                             repository_metadata, sha256, synchronize,
                             training_loss)


PROTOCOL_CUDA_LIMIT_BYTES = 12 * 2**30
PROTOCOL_RSS_LIMIT_BYTES = 8 * 2**30


def memory_status(device, config):
    """Process/device peak measurements and any reached protocol ceilings."""
    device = torch.device(device)
    usage = dict(peak_process_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024,
                 peak_cuda_allocated_bytes=(torch.cuda.max_memory_allocated(device)
                                            if device.type == "cuda" else 0),
                 peak_cuda_reserved_bytes=(torch.cuda.max_memory_reserved(device)
                                           if device.type == "cuda" else 0))
    violations = {name: dict(observed_bytes=usage[name], limit_bytes=config[limit])
                  for name, limit in (("peak_process_rss_bytes", "max_process_rss_bytes"),
                                      ("peak_cuda_allocated_bytes", "max_cuda_allocated_bytes"))
                  if usage[name] >= config[limit]}
    return usage, violations


class CanonicalDenseEngine(DeepDenseEngine):
    """Existing dense equations, initialized from the supplied NumPy arrays.

    Conversion to float64 is exact for the canonical float64 initializer.
    No duplicate random draw, input normalization, or alternate readout is used.
    """

    def __init__(self, params, inputs, labels, *, device="cuda:0"):
        params, inputs = aggregate._validated_network(params, inputs)
        if len(params) != 4:
            raise ValueError("three hidden tanh layers are required")
        labels = np.asarray(labels, dtype=np.float64)
        if labels.shape != (len(inputs),) or not np.isfinite(labels).all():
            raise ValueError("labels must be a finite M-vector")
        self.device = torch.device(device)
        if self.device.type not in ("cpu", "cuda"):
            raise ValueError("device must be cpu or cuda")
        if self.device.type == "cuda":
            if not torch.cuda.is_available():
                raise RuntimeError("CUDA was requested but is unavailable; no CPU fallback")
            if self.device.index is None:
                self.device = torch.device("cuda", torch.cuda.current_device())
        self.dtype = torch.float64
        self.n, self.d = params[0].shape
        self.M = len(inputs)
        self.inputs, self.labels = self._tensor(inputs), self._tensor(labels)
        self.initial = DeepDenseState(*(self._tensor(value) for value in params))
        self.W20, self.W30 = self.initial.W2, self.initial.W3


def normalized_config(raw):
    """Freeze all solver controls; small widths/CPU are for deterministic checks."""
    config = dict(raw)
    defaults = dict(width=2048, seed=20260920, device="cuda:0", threads=1,
                    rtol=1.25e-5, initial_step=.05, max_step=2., max_time=2048.,
                    max_steps=100000, max_wall_seconds=900., target_loss=1e-6,
                    query_batch_size=128, progress_seconds=30.,
                    bisection_iterations=32,
                    max_cuda_allocated_bytes=PROTOCOL_CUDA_LIMIT_BYTES,
                    max_process_rss_bytes=PROTOCOL_RSS_LIMIT_BYTES)
    for key, value in defaults.items():
        config.setdefault(key, value)
    config.setdefault("atol", config["rtol"] / 100)
    for key in ("width", "seed", "threads", "max_steps", "query_batch_size",
                "bisection_iterations", "max_cuda_allocated_bytes", "max_process_rss_bytes"):
        value = config[key]
        if (isinstance(value, bool) or not isinstance(value, int)
                or value < (0 if key == "seed" else 1)):
            raise ValueError("invalid integer control " + key)
    for key, ceiling in (("max_cuda_allocated_bytes", PROTOCOL_CUDA_LIMIT_BYTES),
                         ("max_process_rss_bytes", PROTOCOL_RSS_LIMIT_BYTES)):
        if config[key] > ceiling:
            raise ValueError(key + " exceeds the frozen protocol ceiling")
    for key in ("rtol", "atol", "initial_step", "max_step", "max_time",
                "max_wall_seconds", "target_loss", "progress_seconds"):
        if (isinstance(config[key], bool) or not math.isfinite(config[key])
                or config[key] <= 0):
            raise ValueError("invalid positive control " + key)
    inputs = np.asarray(config["inputs"], dtype=np.float64)
    labels = np.asarray(config["labels"], dtype=np.float64)
    if (inputs.ndim != 2 or inputs.shape[1] != 2 or len(inputs) < 1
            or labels.shape != (len(inputs),)):
        raise ValueError("inputs must have shape (M,2), labels (M,)")
    if not np.isfinite(inputs).all() or not np.isfinite(labels).all():
        raise ValueError("training data must be finite")
    if not np.allclose(np.linalg.norm(inputs, axis=1), 1., rtol=0, atol=1e-12):
        raise ValueError("circle rows must already be (cos(theta),sin(theta))")
    config["inputs"], config["labels"] = inputs.tolist(), labels.tolist()
    panels = {"grid_angles": 2*np.pi*np.arange(1024)/1024,
              "off_grid_angles": 2*np.pi*(np.arange(32)+.371)/32}
    for key, default in panels.items():
        angles = np.asarray(config.get(key, default), dtype=np.float64)
        if angles.ndim != 1 or len(angles) < 1 or not np.isfinite(angles).all():
            raise ValueError(key + " must be a nonempty finite vector in radians")
        config[key] = angles.tolist()
    device = torch.device(config["device"])
    if device.type not in ("cpu", "cuda"):
        raise ValueError("device must be cpu or cuda")
    config["device"] = str(device)
    return config


@torch.no_grad()
def integrate(engine, config):
    """Return endpoint state, accepted-step traces and timing/status metadata.

    The stopping event is the first accepted step bracketing a downward MSE
    crossing. Bisection keeps its endpoint on the <=target side. Initial data
    already below target are explicitly distinguished from a fitted crossing.
    Event interpolation and probes never affect the physical vector field.
    """
    device = engine.device
    state = engine.initial_state()
    current_loss = training_loss(engine, state)
    t, step = 0., config["initial_step"]
    times, losses, steps, errors, walls = [t], [current_loss], [], [], [0.]
    rejected, loss_increases, attempts = 0, 0, 0
    last_rejected_error = None
    crossing_bracket = None
    synchronize(device)
    start, cpu_start = time.monotonic(), time.process_time()
    cuda_start = cuda_end = None
    if device.type == "cuda":
        cuda_start, cuda_end = torch.cuda.Event(enable_timing=True), torch.cuda.Event(enable_timing=True)
        cuda_start.record(torch.cuda.current_stream(device))
    last_report = start
    status = "initially_below_target" if current_loss <= config["target_loss"] else None
    while status is None:
        _, violations = memory_status(device, config)
        if violations:
            status = "memory_limit"
            break
        elapsed = time.monotonic() - start
        if elapsed >= config["max_wall_seconds"]:
            status = "wall_limit"
            break
        if t >= config["max_time"]:
            status = "max_time"
            break
        if len(steps) >= config["max_steps"]:
            status = "max_steps"
            break
        proposed = min(step, config["max_step"], config["max_time"]-t)
        if proposed < 1e-12*max(1., t):
            status = "step_underflow"
            break
        attempts += 1
        first = second = euler = candidate = None
        try:
            first, second, euler, candidate = heun_trial(engine, state, proposed)
            engine.validate_state(candidate)
            error = controlled_error(engine, state, euler, candidate,
                                     config["rtol"], config["atol"])
            candidate_loss = training_loss(engine, candidate)
            valid = math.isfinite(error) and math.isfinite(candidate_loss)
        except (ValueError, FloatingPointError) as exc:
            error, valid = float("inf"), False
            last_rejected_error = str(exc)
        _, violations = memory_status(device, config)
        if violations:
            status = "memory_limit"
            del first, second, euler, candidate
            break
        if not valid or error > 1:
            rejected += 1
            step = proposed * (max(.1, min(.5, .9/math.sqrt(error)))
                               if math.isfinite(error) else .1)
        else:
            actual_step = proposed
            if candidate_loss <= config["target_loss"] < current_loss:
                crossing_bracket = dict(left_time=t, right_time=t+proposed,
                                        left_loss=current_loss, right_loss=candidate_loss)
                fraction, candidate, candidate_loss = locate_loss_crossing(
                    engine, state, first, second, proposed, config["target_loss"],
                    config["bisection_iterations"])
                actual_step = fraction*proposed
                status = "fitted"
            loss_increases += int(candidate_loss > current_loss + 1e-12)
            state, current_loss = candidate, candidate_loss
            t += actual_step
            times.append(t)
            losses.append(current_loss)
            steps.append(actual_step)
            errors.append(error)
            walls.append(time.monotonic()-start)
            step = proposed*max(.5, min(2., .9/math.sqrt(max(error, 1e-16))))
        # Do not retain obsolete O(n^2) trial arrays between steps or at readout.
        del first, second, euler, candidate
        if time.monotonic()-last_report >= config["progress_seconds"]:
            print(json.dumps(dict(event="dense_progress", time=t, training_mse=current_loss,
                                  accepted=len(steps), rejected=rejected,
                                  wall_seconds=time.monotonic()-start)), flush=True)
            last_report = time.monotonic()
    if cuda_end is not None:
        cuda_end.record(torch.cuda.current_stream(device))
    synchronize(device)
    wall_seconds = time.monotonic()-start
    peak_memory, violations = memory_status(device, config)
    if violations:
        status = "memory_limit"
    metadata = dict(status=status, time=t, training_mse=current_loss,
                    accepted=len(steps), rejected=rejected, attempts=attempts,
                    loss_increases=loss_increases, crossing_bracket=crossing_bracket,
                    integration_seconds=wall_seconds,
                    integration_cpu_process_seconds=time.process_time()-cpu_start,
                    integration_cuda_event_interval_seconds=(
                        cuda_start.elapsed_time(cuda_end)/1000 if cuda_end is not None else None),
                    cuda_event_timing_note="device timeline interval including host submission gaps; not kernel-only time",
                    wall_limit_overshoot_seconds=max(0., wall_seconds-config["max_wall_seconds"]),
                    last_rejected_stage_error=last_rejected_error,
                    resource_limits_satisfied=not bool(violations),
                    memory_limit_violations=violations, **peak_memory)
    traces = dict(times=np.asarray(times), losses=np.asarray(losses),
                  accepted_steps=np.asarray(steps), local_error_ratios=np.asarray(errors),
                  integration_wall_times=np.asarray(walls))
    return state, traces, metadata


def run(raw_config, output, *, config_path=None):
    """Write a fresh dense run; GPU is the default and never silently falls back."""
    start, cpu_start = time.monotonic(), time.process_time()
    config = normalized_config(raw_config)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    (output/"config.json").write_text(json.dumps(config, indent=2)+"\n")
    try:
        os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
        torch.set_num_threads(config["threads"])
        torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32 = False
        torch.backends.cudnn.allow_tf32 = False
        device = torch.device(config["device"])
        if device.type == "cuda":
            if not torch.cuda.is_available():
                raise RuntimeError("CUDA was requested but is unavailable; no CPU fallback")
            torch.cuda.set_device(device)
            device = torch.device("cuda", torch.cuda.current_device())
            torch.cuda.reset_peak_memory_stats(device)
        inputs, labels = np.asarray(config["inputs"]), np.asarray(config["labels"])
        setup_start = time.monotonic()
        params = aggregate.initialize_network(config["width"], 2, depth=3, seed=config["seed"])
        initialization_hash = array_hash(*params)
        engine = CanonicalDenseEngine(params, inputs, labels, device=device)
        if array_hash(*engine.initial.tensors()) != initialization_hash:
            raise RuntimeError("NumPy-to-device initialization hash mismatch")
        del params
        synchronize(device)
        setup_seconds = time.monotonic()-setup_start
        sources = ("scalar_wide_dense.py", "scalar_aggregate_engine.py",
                   "deep_circle_run.py", "deep_moment_engine.py", "moment_engine.py")
        manifest = dict(initialization_hash=initialization_hash,
                        effective_config_sha256=sha256(output/"config.json"),
                        input_config_sha256=sha256(config_path) if config_path else None,
                        repository=repository_metadata(sources),
                        data_sha256=array_hash(inputs, labels), device=str(device),
                        device_name=(torch.cuda.get_device_name(device) if device.type == "cuda"
                                     else platform.processor()),
                        software=dict(python=sys.version, numpy=np.__version__, torch=torch.__version__,
                                      cuda=torch.version.cuda, platform=platform.platform()),
                        dtype="float64", deterministic_algorithms=True, tf32=False,
                        cublas_workspace_config=os.environ.get("CUBLAS_WORKSPACE_CONFIG"),
                        command=sys.argv, threads=config["threads"],
                        numerical_thread_environment={key: os.environ.get(key) for key in
                            ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
                        initialization_seconds=setup_seconds, error_control=ERROR_CONTROL,
                        max_cuda_allocated_bytes=config["max_cuda_allocated_bytes"],
                        max_process_rss_bytes=config["max_process_rss_bytes"],
                        endpoint_method="first detected downward crossing; quadratic Heun extension and bisection",
                        bisection_iterations=config["bisection_iterations"])
        (output/"manifest.json").write_text(json.dumps(manifest, indent=2)+"\n")

        def memory_failure(phase, usage, violations, integration=None):
            # Avoid allocating/saving large endpoint panels after a cap failure.
            result = dict(manifest)
            result.update(integration or dict(time=0., training_mse=None, accepted=0, rejected=0))
            result.update(status="memory_limit", scientific_validity=False,
                          resource_limits_satisfied=False, memory_limit_phase=phase,
                          memory_limit_violations=violations, model="dense", width=engine.n,
                          seed=config["seed"], target_loss=config["target_loss"],
                          rtol=config["rtol"], atol=config["atol"], **usage)
            result["total_work_seconds"] = time.monotonic()-start
            result["total_cpu_process_seconds"] = time.process_time()-cpu_start
            (output/"result.json").write_text(json.dumps(result, indent=2)+"\n")
            print(json.dumps(dict(event="dense_complete", status="memory_limit",
                                  memory_limit_phase=phase, scientific_validity=False)), flush=True)
            return result

        usage, violations = memory_status(device, config)
        if violations:
            return memory_failure("initialization", usage, violations)
        state, traces, integration = integrate(engine, config)
        usage, violations = memory_status(device, config)
        if violations or integration["status"] == "memory_limit":
            return memory_failure("integration", usage,
                                  violations or integration["memory_limit_violations"], integration)
        readout_start = time.monotonic()
        panels = {name: np.asarray(config[key]) for name, key in
                  (("grid", "grid_angles"), ("off_grid", "off_grid_angles"))}
        arrays = dict(traces, time=np.asarray(integration["time"]),
                      train_inputs=inputs, train_labels=labels,
                      train_f=panel_predict(engine, state, inputs, config["query_batch_size"]))
        for name, angles in panels.items():
            queries = np.column_stack((np.cos(angles), np.sin(angles)))
            arrays[name] = panel_predict(engine, state, queries, config["query_batch_size"])
            arrays[name+"_angles"] = angles
        for name, value in zip(state.names(), state.tensors()):
            arrays[name] = value.cpu().numpy().copy()
        arrays["flatstate"] = np.concatenate([arrays[name].reshape(-1) for name in state.names()])
        synchronize(device)
        readout_seconds = time.monotonic()-readout_start
        usage, violations = memory_status(device, config)
        if violations:
            return memory_failure("readout", usage, violations, integration)
        save_start = time.monotonic()
        np.savez(output/"trajectory.npz", **arrays)
        usage, violations = memory_status(device, config)
        if violations:
            return memory_failure("saving", usage, violations, integration)
        # Integration already reports its peaks; final peaks also cover readout.
        integration.update(usage)
        result = dict(manifest, **integration, model="dense", hidden_layers=3,
                      width=engine.n, seed=config["seed"], sample_count=engine.M,
                      case=config.get("case"), phase=config.get("phase"),
                      target_loss=config["target_loss"], rtol=config["rtol"], atol=config["atol"],
                      max_time=config["max_time"], max_step=config["max_step"],
                      max_steps=config["max_steps"], max_wall_seconds=config["max_wall_seconds"],
                      output_panel_sha256={name: array_hash(angles) for name, angles in panels.items()},
                      readout_seconds=readout_seconds, saving_seconds=time.monotonic()-save_start,
                      trajectory_sha256=sha256(output/"trajectory.npz"),
                      rss_note="process lifetime high-water mark; use a fresh process for per-run attribution",
                      scientific_validity=(integration["status"] == "fitted"),
                      **engine.storage(state))
        result["total_work_seconds"] = time.monotonic()-start
        result["total_cpu_process_seconds"] = time.process_time()-cpu_start
        (output/"result.json").write_text(json.dumps(result, indent=2)+"\n")
        print(json.dumps(dict(event="dense_complete", status=result["status"],
                              time=result["time"], training_mse=result["training_mse"],
                              accepted=result["accepted"], rejected=result["rejected"],
                              total_work_seconds=result["total_work_seconds"])), flush=True)
        return result
    except Exception as exc:
        failure = dict(status="failed", exception=type(exc).__name__, message=str(exc),
                       traceback=traceback.format_exc())
        (output/"failure.json").write_text(json.dumps(failure, indent=2)+"\n")
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--output", "--out", dest="output", required=True)
    args = parser.parse_args()
    run(json.loads(Path(args.config).read_text()), args.output, config_path=args.config)


if __name__ == "__main__":
    main()
