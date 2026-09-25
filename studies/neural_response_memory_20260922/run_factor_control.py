"""Bounded direct-factor controls; archive predictions are used only for metrics."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
import numpy as np
import torch
from factor_control_engine import FactorEngine, blend, heun_trial, factor_frobenius
from run_moment_experiment import REFERENCES, ROOT

THRESHOLD, WIDTH = .001, 2048


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(8*1024*1024), b""):
            digest.update(block)
    return digest.hexdigest()


def array_hash(value):
    return hashlib.sha256(np.ascontiguousarray(value).tobytes()).hexdigest()


def save_json(path, value):
    with Path(path).open("x") as stream:
        stream.write(json.dumps(value, indent=2, allow_nan=False)+"\n")


def panel_predict(engine, state, panel):
    return np.concatenate([engine.predict(state, panel[k:k+512]).cpu().numpy()
                           for k in range(0, len(panel), 512)])


@torch.no_grad()
def integrate(engine, initial, snapshot_panel, requested_times, rtol, atol, *,
              run_seconds=240., max_steps=30000, max_time=10000.):
    """Uses only own state/data and requested query times, never reference values."""
    state, t, step, rejected = initial.clone(), 0., .05, 0
    current_loss = float(engine.loss(state))
    times, losses, steps, errors = [t], [current_loss], [], []
    snapshot_times, snapshots = [0.], [panel_predict(engine, state, snapshot_panel)]
    schedule = sorted(set(float(x) for x in requested_times if 0 < x <= max_time))
    next_snapshot, exception = 0, None
    start = last_report = time.monotonic()
    status = "time_cap"
    try:
        while current_loss > THRESHOLD:
            if time.monotonic()-start >= run_seconds:
                status = "wall_cap"; break
            if len(steps) >= max_steps:
                status = "step_cap"; break
            if t >= max_time-1e-9:
                status = "time_cap"; break
            proposed = min(step, 2., max_time-t)
            if next_snapshot < len(schedule):
                proposed = min(proposed, schedule[next_snapshot]-t)
            if proposed <= 0:
                raise RuntimeError("nonpositive proposed step")
            try:
                candidate, error = heun_trial(engine, state, proposed, rtol, atol)
                candidate_loss = float(engine.loss(candidate))
                if not math.isfinite(error) or not math.isfinite(candidate_loss):
                    raise ValueError("nonfinite trial error or loss")
            except (ValueError, RuntimeError) as exc:
                rejected += 1
                step = proposed*.25
                if step < 1e-7:
                    raise RuntimeError("adaptive step below 1e-7 after invalid trial") from exc
                continue
            decreasing = candidate_loss <= current_loss*(1+1e-8)+1e-12
            if error > 1 or not decreasing:
                rejected += 1
                step = proposed*max(.1, min(.5, .9/math.sqrt(max(error, 1e-16))))
                if step < 1e-7:
                    raise RuntimeError("adaptive step below 1e-7")
                continue
            used_step = proposed
            if candidate_loss <= THRESHOLD:
                low, high = 0., 1.
                for _ in range(32):
                    middle = .5*(low+high)
                    if float(engine.loss(blend(state, candidate, middle))) <= THRESHOLD:
                        high = middle
                    else:
                        low = middle
                candidate, used_step = blend(state, candidate, high), proposed*high
                candidate_loss = float(engine.loss(candidate))
            state, current_loss, t = candidate, candidate_loss, t+used_step
            times.append(t); losses.append(current_loss); steps.append(used_step); errors.append(error)
            if next_snapshot < len(schedule) and t >= schedule[next_snapshot]-1e-9:
                snapshot_times.append(t); snapshots.append(panel_predict(engine, state, snapshot_panel))
                next_snapshot += 1
            step = proposed*max(.5, min(2., .9/math.sqrt(max(error, 1e-16))))
            if time.monotonic()-last_report >= 20:
                print(json.dumps(dict(event="progress", time=t, loss=current_loss,
                                      steps=len(steps), wall_seconds=time.monotonic()-start)), flush=True)
                last_report = time.monotonic()
        if current_loss <= THRESHOLD:
            status = "fitted"
    except Exception as exc:
        status, exception = "numerical_failure", dict(type=type(exc).__name__, message=str(exc))
    try:
        if abs(snapshot_times[-1]-t) > 1e-12:
            final_prediction = panel_predict(engine, state, snapshot_panel)
            snapshot_times.append(t); snapshots.append(final_prediction)
    except Exception as exc:
        status, exception = "numerical_failure", dict(type=type(exc).__name__, message=str(exc))
    elapsed = time.monotonic()-start
    arrays = dict(times=np.asarray(times), losses=np.asarray(losses), accepted_steps=np.asarray(steps),
                  local_error_ratios=np.asarray(errors), snapshot_times=np.asarray(snapshot_times),
                  circle_predictions=np.asarray(snapshots))
    summary = dict(status=status, time=t, training_mse=current_loss, initial_loss=losses[0],
                   accepted=len(steps), rejected=rejected, integration_seconds=elapsed, exception=exception,
                   loss_increases=int(np.count_nonzero(np.diff(losses)>1e-10)))
    return state, arrays, summary


@torch.no_grad()
def run_cell(args, case, order, factor_seed):
    directory = Path(args.out)/f"{case}_factor_P{order}_seed{factor_seed}_level{args.level}"
    directory.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    rtol = 6.25e-5/4**args.level
    sources = ("factor_control_engine.py", "run_factor_control.py", "test_factor_control.py",
               "run_moment_experiment.py", "moment_engine.py", "FACTOR_CONTROL_PROTOCOL.md")
    config = dict(case=case, variant="factor", P=order, factor_seed=factor_seed, level=args.level,
                  width=WIDTH, input_dimension=2, network_seed=20260920, dtype="float64",
                  device=args.device, gpu=torch.cuda.get_device_name(args.device), rtol=rtol, atol=rtol/100,
                  threshold=THRESHOLD, initial_step=.05, max_step=2., min_step=1e-7,
                  max_time=10000., max_steps=30000, run_seconds=args.run_seconds, crossing_bisections=32,
                  mobilities=dict(w=WIDTH, c=WIDTH, A=1, B=1), loss="unhalved probability MSE",
                  factor_convention="A'=-grad_A L, B'=-grad_B L; W2=W0+A@B; W0 fixed",
                  factor_initialization="A=0; B=default_rng(factor_seed).standard_normal((rank,n))/sqrt(rank)",
                  error_scales="raw w,c,A,B RMS clamped at 1; deltaW Frobenius clamped at 1",
                  source_sha256={name:sha256(Path(__file__).parent/name) for name in sources},
                  command=sys.argv, cwd=str(Path.cwd()), python=sys.version, numpy=np.__version__,
                  torch=str(torch.__version__), started_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    arrays, summary, state = {}, dict(status="setup_failure"), None
    try:
        archive_path = ROOT/"data/generated/random_dictionary_learned_circle_20260920"/REFERENCES[case]/"arrays.npz"
        config.update(reference=str(archive_path.relative_to(ROOT)), reference_sha256=sha256(archive_path))
        with np.load(archive_path, allow_pickle=False) as archive:
            arrays = {name:archive[name].copy() for name in
                      ("training_inputs", "labels", "endpoint_angles", "endpoint_inputs", "circle_angles", "circle_inputs")}
            arrays.update(reference_snapshot_times=archive["snapshot_times"].copy(),
                          reference_circle_predictions=archive["circle_predictions"].copy(),
                          reference_endpoint_prediction=archive["endpoint_prediction"].copy())
            inputs, labels = arrays["training_inputs"], arrays["labels"]
            if inputs.shape != (8, 2) or labels.shape != (8,) or arrays["endpoint_inputs"].shape != (8192, 2):
                raise ValueError("unexpected archived training or endpoint shape")
            quotient = case == "equal_mixed_odd"
            if quotient:
                if not (np.allclose(inputs[4:], -inputs[:4], rtol=0, atol=1e-14) and np.array_equal(labels[4:], -labels[:4])):
                    raise ValueError("antipodal quotient conditions failed")
                inputs, labels = inputs[:4], labels[:4]
            engine = FactorEngine(2, WIDTH, order*len(labels), inputs, labels, factor_seed=factor_seed, device=args.device)
            state = engine.initial_state()
            initial_match = {name:np.array_equal(value.cpu().numpy(), archive[key][0])
                             for name, key, value in (("w", "w", state.w), ("c", "c", state.c), ("W0", "M", engine.W0))}
        config.update(rank=engine.rank, sample_count=len(labels), original_sample_count=8,
                      antipodal_quotient=quotient, initial_match=initial_match,
                      moving_scalars=sum(x.numel() for x in state.tensors()), fixed_W0_scalars=engine.W0.numel(),
                      initial_array_sha256={name:array_hash(value.cpu().numpy()) for name, value in
                          zip(("w", "c", "A", "B", "W0"), (*state.tensors(), engine.W0))},
                      final_state_layout={name:list(value.shape) for name, value in zip(state.names(), state.tensors())},
                      state_arrays_have_snapshot_axis=False)
        velocity = engine.rhs(state)
        h1, _, _, q = engine.fields(state)
        dense_left = (-2/(engine.S*engine.n))*q
        config["initial_checks"] = dict(A_is_zero=bool((state.A==0).all()), B_is_nonzero=bool((state.B!=0).any()),
            correction_frobenius=float(factor_frobenius(state.A, state.B.T)),
            B_mean=float(state.B.mean()), B_second_moment=float(state.B.square().mean()), B_variance_target=1/engine.rank,
            A_velocity_frobenius=float(velocity.A.norm()), B_velocity_frobenius=float(velocity.B.norm()),
            induced_velocity_frobenius=float(factor_frobenius(velocity.A, state.B.T)),
            dense_velocity_frobenius=float(factor_frobenius(dense_left, h1)),
            induced_minus_dense_frobenius=float(factor_frobenius(torch.cat((velocity.A, -dense_left), 1),
                                                                 torch.cat((state.B.T, h1), 1))))
        if not all(initial_match.values()) or config["initial_checks"]["correction_frobenius"] != 0:
            raise ValueError("canonical initialization mismatch or nonzero initial correction")
        arrays.update(represented_training_inputs=inputs, represented_labels=labels)
        save_json(directory/"config.json", config)
        state, trace, summary = integrate(engine, state, arrays["circle_inputs"], arrays["reference_snapshot_times"],
                                          rtol, rtol/100, run_seconds=args.run_seconds)
        arrays.update(trace)
        engine.validate_state(state)
        prediction = panel_predict(engine, state, arrays["endpoint_inputs"])
        training_prediction = engine.predict(state, arrays["training_inputs"]).cpu().numpy()
        arrays.update(endpoint_prediction=prediction, endpoint_prediction_4096=prediction[::2],
                      training_prediction=training_prediction)
        difference = prediction-arrays["reference_endpoint_prediction"]
        summary.update(circle_rms=float(np.sqrt(np.mean(difference**2))),
                       circle_rms_4096=float(np.sqrt(np.mean(difference[::2]**2))), circle_max=float(np.max(np.abs(difference))),
                       endpoint_loss_recomputed=float(np.mean((training_prediction-arrays["labels"])**2)),
                       represented_endpoint_loss_recomputed=float(engine.loss(state)), finite_state=True)
        indices = [next((i for i, ref in enumerate(arrays["reference_snapshot_times"]) if abs(ref-t)<1e-9), -1)
                   for t in arrays["snapshot_times"]]
        arrays["snapshot_reference_indices"] = np.asarray(indices)
        arrays["matched_time_rms"] = np.asarray([np.sqrt(np.mean((p-arrays["reference_circle_predictions"][i])**2))
                                                  for p, i in zip(arrays["circle_predictions"], indices) if i>=0])
    except Exception as exc:
        summary.update(prior_status=summary["status"], status="failure",
                       exception=dict(type=type(exc).__name__, message=str(exc)))
    if state is not None:
        arrays.update({name:value.cpu().numpy() for name, value in zip(state.names(), state.tensors())})
    if not (directory/"config.json").exists():
        save_json(directory/"config.json", config)
    with (directory/"arrays.npz").open("xb") as stream:
        np.savez(stream, **arrays)
    summary.update(case=case, variant="factor", P=order, factor_seed=factor_seed, level=args.level,
                   width=WIDTH, rank=config.get("rank"), rtol=rtol, atol=rtol/100, initial_match=config.get("initial_match"),
                   initial_checks=config.get("initial_checks"), source_sha256=config["source_sha256"],
                   zero_initial_correction=config.get("initial_checks", {}).get("correction_frobenius") == 0,
                   arrays_sha256=sha256(directory/"arrays.npz"), wall_seconds=time.monotonic()-started)
    save_json(directory/"summary.json", summary)
    print(json.dumps(dict(event="completed", directory=str(directory), **summary)), flush=True)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", nargs="+", choices=tuple(REFERENCES), required=True)
    parser.add_argument("--orders", nargs="+", type=int, default=[1, 3, 7])
    parser.add_argument("--level", type=int, choices=(0, 1, 2), default=0)
    parser.add_argument("--factor-seeds", nargs="+", type=int, choices=(20260924, 20260925), default=[20260924, 20260925])
    parser.add_argument("--device", required=True)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--run-seconds", type=float, default=240.)
    parser.add_argument("--batch-seconds", type=float, default=900., help="cumulative integration-seconds cap")
    args = parser.parse_args()
    if any(len(values)!=len(set(values)) for values in (args.cases, args.orders, args.factor_seeds)) or min(args.orders)<1:
        parser.error("orders must be positive; duplicate cells are forbidden")
    if not math.isfinite(args.run_seconds) or not 0 < args.run_seconds <= 240:
        parser.error("run-seconds must be in (0,240]")
    if not math.isfinite(args.batch_seconds) or args.batch_seconds <= 0:
        parser.error("batch-seconds must be positive and finite")
    if not args.device.startswith("cuda:") or not torch.cuda.is_available():
        parser.error("CUDA required for benchmark runs; CPU is reserved for tests")
    targets = [(case, order, seed) for case in args.cases for order in args.orders for seed in args.factor_seeds]
    if any((args.out/f"{case}_factor_P{order}_seed{seed}_level{args.level}").exists() for case, order, seed in targets):
        parser.error("output cell exists; use a fresh path")
    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    torch.cuda.set_device(args.device)
    results, used, requested_seconds = [], 0., args.run_seconds
    for cell in targets:
        if used >= args.batch_seconds:
            break
        args.run_seconds = min(requested_seconds, args.batch_seconds-used)
        result = run_cell(args, *cell)
        results.append(result)
        used += result.get("integration_seconds", 0.)
    batch = dict(integration_seconds=used, batch_seconds=args.batch_seconds,
                 completed_cells=len(results), requested_cells=len(targets),
                 skipped_cells=targets[len(results):], command=sys.argv,
                 status="batch_cap" if len(results)<len(targets) else "completed")
    save_json(args.out/f"batch_summary_{time.time_ns()}.json", batch)
    print(json.dumps(dict(event="batch_complete", **batch)), flush=True)
    return 0 if len(results)==len(targets) and all(result["status"]=="fitted" for result in results) else 2


if __name__ == "__main__":
    raise SystemExit(main())
