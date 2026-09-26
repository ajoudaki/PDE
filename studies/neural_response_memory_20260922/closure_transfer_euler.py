"""Simultaneous fixed Euler for the existing activation moment closure."""
import argparse
import copy
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import sys
import time
import traceback
import zipfile

os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
for _name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_name, "1")
import numpy as np
import torch

from activation_fast_engine import FastActivationMomentEngine

HERE = Path(__file__).resolve().parent
SEED = 20260920
SOURCE_NAMES = ("closure_transfer_euler.py", "activation_fast_engine.py", "activation_moment_engine.py",
                "deep_moment_engine.py", "moment_engine.py")


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""): digest.update(block)
    return digest.hexdigest()


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False)+"\n")


def save_npz(path, **arrays):
    path = Path(path)
    if path.exists(): raise FileExistsError(path)
    np.savez_compressed(path, **arrays)
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None: raise ValueError("Saved archive CRC failure")


def task_data(path, activation, task):
    source = json.loads(Path(path).read_text())
    literal = source.get(activation+"__"+task, source.get(task))
    if literal is None: raise ValueError("Unknown activation/task")
    angles = [value*math.pi/180 for value in literal["angles_degrees"]]
    inputs = np.asarray([[math.cos(value), math.sin(value)] for value in angles], dtype=np.float64)
    labels = np.asarray(literal["labels"], dtype=np.float64)
    if inputs.shape != (8, 2) or labels.shape != (8,) or not np.isfinite(inputs).all() or not np.isfinite(labels).all():
        raise ValueError("Eight finite circle inputs and labels required")
    return inputs, labels, {key: literal[key] for key in ("angles_degrees", "labels")}


class CachedEulerEngine(FastActivationMomentEngine):
    """Retain fields from the inherited RHS without changing its arithmetic."""
    def _fields(self, state):
        self.last_fields = super()._fields(state)
        return self.last_fields


class EulerStage:
    """A pure RHS, optionally captured; returned velocities are borrowed buffers.

    State storage is fixed. Capture warmups never advance state. Full validation
    occurs before capture; metadata and packed finite/activity checks remain.
    """
    @torch.no_grad()
    def __init__(self, engine, state, backend="eager"):
        if backend not in ("eager", "graphs"): raise ValueError("Unknown backend")
        if backend == "graphs" and engine.device.type != "cuda": raise ValueError("Graphs require CUDA")
        engine.validate_state(state)
        self.engine, self.state, self.backend = engine, state, backend
        self.metadata = self._metadata()
        self.view = copy.copy(engine)
        self.view.validate_state = lambda state, finite=True: state
        self.graph = None
        if backend == "graphs":
            with torch.cuda.device(engine.device):
                stream = torch.cuda.Stream(device=engine.device)
                stream.wait_stream(torch.cuda.current_stream(engine.device))
                with torch.cuda.stream(stream):
                    for _ in range(3): self._operation()
                torch.cuda.current_stream(engine.device).wait_stream(stream)
                torch.cuda.synchronize(engine.device)
                self.graph = torch.cuda.CUDAGraph()
                with torch.cuda.graph(self.graph, stream=stream): self.output = self._operation()
                torch.cuda.synchronize(engine.device)

    def _metadata(self):
        return tuple((id(value), value.data_ptr(), value.shape, value.stride(), value.dtype, value.device)
                     for value in self.state.tensors())

    def _operation(self):
        velocity = self.view.rhs(self.state)
        fields = self.view.last_fields
        tensors = (*self.state.tensors(), *velocity.tensors(), *fields.values())
        finite = torch.stack([torch.isfinite(value).all() for value in tensors]).all()
        valid = finite & (self.state.s >= 0)
        return velocity, torch.stack((fields["loss"], valid.to(dtype=self.engine.dtype)))

    @torch.no_grad()
    def evaluate(self):
        if self._metadata() != self.metadata: raise ValueError("Euler state storage/metadata changed")
        if self.graph is None: velocity, packed = self._operation()
        else:
            self.graph.replay()
            velocity, packed = self.output
        loss, valid = packed.detach().cpu().tolist()
        return velocity, loss, bool(valid) and math.isfinite(loss)


@torch.no_grad()
def euler_update(state, velocity, step):
    """The caller must compute the complete velocity before any in-place add."""
    if not math.isfinite(step) or step <= 0: raise ValueError("Step must be positive and finite")
    for value, rate in zip(state.tensors(), velocity.tensors()): value.add_(rate, alpha=step)


def finite_number(value):
    return float(value) if math.isfinite(value) else None


@torch.no_grad()
def run(args, *, width=2048):
    if args.activation not in ("relu", "gelu", "selu") or args.P not in (1, 2, 3): raise ValueError("Unsupported activation/order")
    if any(not math.isfinite(value) or value <= 0 for value in
           (args.step, args.max_seconds, args.max_time, args.target_mse)) or args.max_steps < 1:
        raise ValueError("Step and caps must be positive and finite")
    if args.backend not in ("eager", "graphs"): raise ValueError("Unknown backend")
    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=False)
    config = dict(vars(args), out=str(out), width=width, seed=SEED, dtype="float64", mobilities=[width, 1, 1, width],
                  query_count=8192, query_batch_size=128, hidden_layers=3, model="moment", method="simultaneous fixed Euler",
                  loss="mean squared error without one-half", physical_time_rule="updates*step", activity_rule="s'=sqrt(MSE)",
                  effective_max_seconds=args.max_seconds, effective_max_steps=args.max_steps, effective_max_time=args.max_time)
    write_json(out/"config.json", config)
    lifecycle = None; manifest = None
    try:
        inputs, labels, literal = task_data(args.cases_json, args.activation, args.task)
        config.update(inputs=inputs.tolist(), labels=labels.tolist(), literal_task=literal,
                      case=args.activation+"__"+args.task, cases_json=str(Path(args.cases_json).resolve()))
        write_json(out/"config.json", config)
        torch.set_num_threads(1); torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32 = False; torch.backends.cudnn.allow_tf32 = False
        device = torch.device(args.device)
        if device.type == "cuda":
            torch.cuda.set_device(device); torch.cuda.reset_peak_memory_stats(device)
        setup = time.monotonic()
        engine = CachedEulerEngine(2, width, args.P, inputs, labels, activation=args.activation,
                                   seed=SEED, device=device, dtype=torch.float64)
        state = engine.initial_state()
        initial = hashlib.sha256()
        for value in (state.w, engine.W20, engine.W30, state.c): initial.update(value.cpu().numpy().tobytes())
        capture = time.monotonic()
        stage = EulerStage(engine, state, args.backend)
        capture_seconds = time.monotonic()-capture
        manifest = dict(source_sha256={name: sha256(HERE/name) for name in SOURCE_NAMES},
            config_sha256=sha256(out/"config.json"), cases_sha256=sha256(args.cases_json),
            protocol_sha256=sha256(HERE/"CLOSURE_TRANSFER_2048_PROTOCOL.md"), initialization_sha256=initial.hexdigest(),
            initialization_hash_encoding="SHA256 concatenated C-order float64 bytes: w,W20,W30,c",
            numpy=np.__version__, torch=torch.__version__, python=sys.version, cuda=torch.version.cuda,
            platform=platform.platform(), device_name=torch.cuda.get_device_name(device) if device.type == "cuda" else platform.processor(),
            deterministic_algorithms=True, tf32=False, threads=1, cublas_workspace_config=os.environ.get("CUBLAS_WORKSPACE_CONFIG"),
            command=sys.argv, setup_seconds=time.monotonic()-setup, capture_seconds=capture_seconds)
        write_json(out/"manifest.json", manifest)
        started = reported = time.monotonic()
        lifecycle = dict(status="integrating", pid=os.getpid(), integration_start_unix=time.time(),
                         integration_start_monotonic=started)
        write_json(out/"lifecycle.json", lifecycle)
        updates = 0; losses = []; walls = []
        while True:
            velocity, loss, valid = stage.evaluate()
            elapsed = time.monotonic()-started
            losses.append(loss); walls.append(elapsed)
            physical_time = updates*args.step
            if not valid: status="diverged"; reason="nonfinite_fields_or_state"; break
            if loss > 1e6: status="diverged"; reason="loss_exceeds_1e6"; break
            if loss <= args.target_mse: status="target_loss"; reason="first_discrete_fitted_endpoint"; break
            if physical_time >= args.max_time: status="max_time"; reason="physical_time_cap"; break
            if updates >= args.max_steps: status="max_steps"; reason="update_cap"; break
            if elapsed >= args.max_seconds: status="wall_limit"; reason="integration_wall_cap"; break
            if time.monotonic()-reported >= 30:
                print(json.dumps(dict(event="progress",updates=updates, physical_time=physical_time,
                    training_mse=loss, integration_seconds=elapsed)), flush=True)
                reported = time.monotonic()
            euler_update(state, velocity, args.step)
            updates += 1
        integration_seconds = time.monotonic()-started
        lifecycle.update(status="integration_complete", integration_end_unix=time.time(), integration_seconds=integration_seconds)
        write_json(out/"lifecycle.json", lifecycle)
        saving = time.monotonic()
        # The stage view can preserve raw nonfinite endpoints without the host s>=0 guard.
        training = stage.view.predict(state, engine.inputs).cpu().numpy()
        mse = float(np.mean((training-labels)**2)); residual = float(np.max(np.abs(training-labels)))
        state_finite = all(bool(torch.isfinite(value).all()) for value in state.tensors())
        angles = 2*np.pi*np.arange(8192)/8192
        circle_inputs = np.column_stack((np.cos(angles), np.sin(angles)))
        circle = np.concatenate([stage.view.predict(state, circle_inputs[i:i+128]).cpu().numpy() for i in range(0,8192,128)])
        predictions_finite = bool(np.isfinite(training).all() and np.isfinite(circle).all())
        if not state_finite or not predictions_finite or not math.isfinite(mse):
            status, reason = "diverged", "nonfinite_final_state_or_predictions"
        fitted = status == "target_loss" and mse <= args.target_mse*(1+1e-12)
        if status == "target_loss" and not fitted: status, reason = "failed", "final_recomputed_loss_mismatch"
        save_npz(out/"state.npz", **{name: value.cpu().numpy() for name,value in zip(state.names(),state.tensors())},
                 physical_time=np.asarray(physical_time), steps=np.asarray(updates), training_mse=np.asarray(mse))
        save_npz(out/"predictions.npz", circle_angles=angles, circle_inputs=circle_inputs, circle_predictions=circle,
                 train_inputs=inputs, train_labels=labels, train_predictions=training, training_mse=np.asarray(mse),
                 steps=np.asarray(updates), physical_time=np.asarray(physical_time))
        save_npz(out/"loss_trace.npz", steps=np.arange(updates+1), physical_times=args.step*np.arange(updates+1),
                 losses=np.asarray(losses), wall_seconds=np.asarray(walls))
        summary = dict(config, **manifest, status=status, stop_reason=reason, fitted=fitted, updates=updates, steps=updates,
            physical_time=physical_time, activity=finite_number(float(state.s.cpu())), training_mse=finite_number(mse),
            max_train_residual=finite_number(residual), initial_loss=finite_number(losses[0]), state_finite=state_finite,
            predictions_finite=predictions_finite, integration_seconds=integration_seconds,
            wall_limit_overshoot_seconds=max(0.,integration_seconds-args.max_seconds), final_saving_seconds=time.monotonic()-saving,
            peak_cuda_bytes=torch.cuda.max_memory_allocated(device) if device.type == "cuda" else 0,
            storage=engine.storage(state), artifact_sha256={name:sha256(out/name) for name in
                ("state.npz", "predictions.npz", "loss_trace.npz")}, archive_crc_validated=True)
        write_json(out/"summary.json", summary)
        lifecycle.update(status="complete", completion_unix=time.time()); write_json(out/"lifecycle.json", lifecycle)
        print(json.dumps(dict(event="complete", status=status, fitted=fitted, updates=updates, physical_time=physical_time,
            training_mse=summary["training_mse"], integration_seconds=integration_seconds, out=str(out))), flush=True)
        return summary
    except BaseException as error:
        if lifecycle is not None and lifecycle.get("status") == "integrating":
            lifecycle.update(status="failed", integration_seconds=time.monotonic()-lifecycle["integration_start_monotonic"])
            write_json(out/"lifecycle.json", lifecycle)
        write_json(out/"failure.json", dict(status="failed", exception=type(error).__name__, message=str(error),
            traceback=traceback.format_exc(), config_sha256=sha256(out/"config.json"), lifecycle=lifecycle,
            initialization_sha256=manifest["initialization_sha256"] if manifest else None,
            integration_seconds=lifecycle.get("integration_seconds", 0.) if lifecycle else 0.,
            source_sha256={name:sha256(HERE/name) for name in SOURCE_NAMES}))
        raise


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--activation", choices=("relu", "gelu", "selu"), required=True)
    result.add_argument("--task", choices=("two_outliers_alternating", "quadrant_alternating"), required=True)
    result.add_argument("--P", type=int, choices=(1,2,3), required=True)
    result.add_argument("--step", type=float, required=True)
    result.add_argument("--device", required=True)
    result.add_argument("--out", required=True)
    result.add_argument("--max-seconds", type=float, default=1800.)
    result.add_argument("--max-time", type=float, default=260.)
    result.add_argument("--max-steps", type=int, default=2200000)
    result.add_argument("--target-mse", type=float, default=1e-8)
    result.add_argument("--backend", choices=("eager", "graphs"), default="eager")
    result.add_argument("--cases-json", default=str(HERE/"activation_circle_cases.json"))
    return result


if __name__ == "__main__": run(parser().parse_args())
