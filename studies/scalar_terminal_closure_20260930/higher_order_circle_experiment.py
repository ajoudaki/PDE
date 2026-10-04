"""q=2/q=3 circle closures, then a separate frozen scalar evaluation stage.

Stage 1: --reference ORIGINAL_RUN --output FRESH_CLOSURE_RUN --budget SECONDS
Stage 2: --scalar --run CLOSURE_RUN --output FRESH_SCALAR_RUN --budget SECONDS
Tiny checks only: --check --output FRESH_CHECK_RUN

Moments have shape (q,n,m). Stage 2 preserves Stage 1 by copying its artifacts
to a fresh root. At most one 1/32 refinement per task/order is permitted.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import platform
import resource
import shutil
import signal
import sys
import time

import numpy as np
import scipy
from threadpoolctl import threadpool_info, threadpool_limits

import circle_terminal_experiment as base


HERE = Path(__file__).resolve().parent
BASE_HASH = "f5ea7959bbd440aa161b6cb0ee484e68d9e81d5e7cce5e4b9b1df590a170c6ba"
CASES = ("two_outliers_alternating", "quadrant_alternating")
FINAL_TIMES = {"two_outliers_alternating": 244.5, "quadrant_alternating": 346.375}
ORDERS = (2, 3)
THRESHOLDS = (0.1, 0.01, 0.001)
WIDTH, SEED = 1024, 20260920
MEMORY_LIMIT = 4 * 1024**3


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")
    temporary.replace(path)


def highwater_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else 1024 * value)


class Budget:
    def __init__(self, seconds):
        if not np.isfinite(seconds) or seconds <= 0 or seconds > 3600:
            raise ValueError("budget must be in (0,3600] seconds")
        self.seconds = float(seconds)
        self.started = time.perf_counter()
        self.deadline = self.started + self.seconds

    def guard(self, state=None):
        if time.perf_counter() >= self.deadline:
            raise TimeoutError("Numerical stage wall-time allowance exhausted")
        if highwater_bytes() > MEMORY_LIMIT:
            raise MemoryError("Process high-water RSS exceeds 4 GiB")
        if state is not None:
            if not all(np.isfinite(block).all() for block in state):
                raise FloatingPointError("Nonfinite closure state")
            if float(state[-1][0]) <= 0:
                raise FloatingPointError("Nonpositive activity clock")

    def __enter__(self):
        self.old_handler = signal.getsignal(signal.SIGALRM)
        signal.signal(signal.SIGALRM, self._alarm)
        signal.setitimer(signal.ITIMER_REAL, self.seconds)
        return self

    @staticmethod
    def _alarm(_signum, _frame):
        raise TimeoutError("Numerical stage wall-time allowance exhausted")

    def __exit__(self, *_error):
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, self.old_handler)


def weights(state):
    return 2 * np.arange(state[2].shape[0]) + 1


def initial_state(a, inputs, q):
    n, m = len(a), inputs.shape[1]
    keys = np.zeros((q, n, m))
    keys[0] = np.tanh(a @ inputs)
    return a.copy(), np.zeros(n), np.zeros_like(keys), keys, np.ones(1)


def fields(state, w0, inputs, backward=True):
    a, readout, values, keys, _clock = state
    n, m = a.shape[0], keys.shape[2]
    first_z = a @ inputs
    first = np.tanh(first_z)
    second_z = w0 @ first
    for j, weight in enumerate(weights(state)):
        second_z += weight / (m * n) * (values[j] @ (keys[j].T @ first))
    second = np.tanh(second_z)
    result = dict(h=first, g=second, f=readout @ second / n)
    if backward:
        delta = readout[:, None] * base.derivative(second_z)
        previous = w0.T @ delta
        for j, weight in enumerate(weights(state)):
            previous += weight / (m * n) * (keys[j] @ (values[j].T @ delta))
        result.update(d=delta, ell=base.derivative(first_z) * previous)
    return result


def velocity(state, w0, inputs, labels):
    f = fields(state, w0, inputs)
    residual = f["f"] - labels
    m = len(residual)
    rho = np.linalg.norm(residual) / np.sqrt(m)
    rate = rho / float(state[4][0])
    values, keys = state[2:4]
    value_dot, key_dot = np.empty_like(values), np.empty_like(keys)
    previous_values, previous_keys = np.zeros_like(values[0]), np.zeros_like(keys[0])
    forcing = -2 * f["d"] * residual
    for j, weight in enumerate(weights(state)):
        value_dot[j] = forcing - rate * (j * values[j] + previous_values)
        key_dot[j] = rate * (f["h"] - (j + 1) * keys[j] - previous_keys)
        previous_values += weight * values[j]
        previous_keys += weight * keys[j]
    adot = -2 / m * ((f["ell"] * residual) @ inputs.T)
    readout_dot = -2 / m * (f["g"] @ residual)
    return (adot, readout_dot, value_dot, key_dot, np.array([rho])), f


def endpoint_sums(state):
    scale = weights(state)[:, None, None]
    return np.sum(scale * state[2], axis=0), np.sum(scale * state[3], axis=0)


def response(state, w0, train_inputs, train_fields, query_inputs, budget=None, block=256):
    """Exact query coefficients from full fields and endpoint memory sums."""
    n, m = train_fields["h"].shape
    values_star, keys_star = endpoint_sums(state)
    outputs, matrices, drifts = [], [], []
    for start in range(0, query_inputs.shape[1], block):
        if budget is not None:
            budget.guard()
        query = query_inputs[:, start:start + block]
        qf = fields(state, w0, query)
        matrix = 2 / m * (
            qf["g"].T @ train_fields["g"] / n
            + (query.T @ train_inputs) * (qf["ell"].T @ train_fields["ell"] / n)
            + (qf["d"].T @ train_fields["d"] / n) * (qf["h"].T @ keys_star / n))
        drift = np.sum((qf["d"].T @ values_star / n)
                       * (qf["h"].T @ (train_fields["h"] - keys_star) / n), axis=1)
        drift /= m * np.sqrt(m) * float(state[4][0])
        outputs.append(qf["f"]); matrices.append(matrix); drifts.append(drift)
    return np.concatenate(outputs), np.concatenate(matrices), np.concatenate(drifts)


def predict(state, w0, inputs, budget=None, block=256):
    chunks = []
    for start in range(0, inputs.shape[1], block):
        if budget is not None:
            budget.guard()
        chunks.append(fields(state, w0, inputs[:, start:start + block], False)["f"])
    return np.concatenate(chunks)


def materialized_middle(state, w0):
    """Tiny checks and independent review only; production fields use actions."""
    n, m = state[3].shape[1:]
    middle = w0.copy()
    for j, weight in enumerate(weights(state)):
        middle += weight * state[2][j] @ state[3][j].T / (m * n)
    return middle


def task_arrays(task):
    inputs = np.asarray(task["normalized_inputs_u"], dtype=np.float64)
    if inputs.shape == (8, 2):
        inputs = inputs.T
    labels = np.asarray(task["labels"], dtype=np.float64)
    if inputs.shape != (2, 8) or labels.shape != (8,):
        raise ValueError("Unexpected fixed circle task shapes")
    return inputs, labels


def selected_tasks(path):
    by_name = {task["case"]: task for task in json.loads(Path(path).read_text())["tasks"]}
    return [by_name[case] for case in CASES]


def reference_files(reference):
    paths = [reference / "initialization.npz", reference / "results.json",
             reference / "circle_task_inputs.json"]
    for case in CASES:
        for resolution in ("coarse", "fine"):
            directory = reference / case / resolution
            paths.extend(directory / name for name in ("curves.npz", "summary.json", "endpoint_states.npz"))
    return {str(path.resolve()): digest(path) for path in paths}


def verified_initialization(reference, output):
    with np.load(reference / "initialization.npz", allow_pickle=False) as saved:
        a, w0, readout = (saved[name].copy() for name in ("a", "w0", "readout"))
    expected_a, expected_w0 = base.initialized(WIDTH, 8, SEED)
    if (a.shape != (WIDTH, 2) or w0.shape != (WIDTH, WIDTH)
            or not np.array_equal(a, expected_a) or not np.array_equal(w0, expected_w0)
            or readout.shape != (WIDTH,) or np.any(readout != 0)):
        raise ValueError("Saved initialization differs from the stipulated generator")
    np.savez_compressed(output / "initialization.npz", a=a, w0=w0, readout=readout)
    return a, w0, dict(a_initial_hash=base.array_digest(a), w0_initial_hash=base.array_digest(w0))


def load_reference(reference, case, resolution):
    actual = "coarse" if resolution == "coarse" else "fine"
    path = reference / case / actual / "curves.npz"
    with np.load(path, allow_pickle=False) as source:
        ref = {key: source[key].copy() for key in
               ("angles", "times", "dense_loss", "dense_output", "train_angles", "labels")}
    if float(ref["times"][-1]) != FINAL_TIMES[case]:
        raise ValueError("Dense reference has an unexpected physical endpoint")
    if not all(np.isfinite(value).all() for value in ref.values()):
        raise FloatingPointError("Nonfinite dense reference")
    return ref


def common_loss_error(times, losses, reference_times, reference_loss):
    common, first, second = np.intersect1d(times, reference_times, return_indices=True)
    if not len(common) or common[0] != times[0] or common[-1] != times[-1]:
        raise ValueError("Loss comparison lacks common endpoints")
    return float(np.max(np.abs(losses[first] - reference_loss[second])))


def dense_refinement(reference, case):
    first, second = (load_reference(reference, case, x) for x in ("coarse", "fine"))
    endpoint = base.rms(first["dense_output"] - second["dense_output"])
    loss = common_loss_error(first["times"], first["dense_loss"], second["times"], second["dense_loss"])
    return dict(dense_endpoint_rms=endpoint, dense_loss_max=loss,
                passed=endpoint <= 0.002 and loss <= 0.001,
                source="reused original coarse/fine dense references")


def capture(state, w0, inputs, labels, train, angles, threshold, t, output, budget):
    started = time.perf_counter()
    budget.guard(state)
    _, matrix, drift = response(state, w0, inputs, train, inputs, budget)
    uniform = 2 * np.pi * np.arange(2048) / 2048
    sample_f, sample_c, sample_b = response(state, w0, inputs, train, base.circle_inputs(uniform), budget)
    fourier = base.fourier_coefficients(np.column_stack((sample_f, sample_c, sample_b)))
    query_f, query_c, query_b = response(state, w0, inputs, train, base.circle_inputs(angles), budget)
    error = base.fourier_basis(angles) @ fourier - np.column_stack((query_f, query_c, query_b))
    residual = train["f"] - labels
    sym = (matrix + matrix.T) / 2
    info = dict(threshold=threshold, time=t, train_mse=float(np.mean(residual**2)),
                margin=float(np.linalg.eigvalsh(sym)[0] - np.linalg.norm(drift)),
                projected_margin=None,
                spatial_rms_by_field=np.sqrt(np.mean(error**2, axis=0)).tolist(),
                spatial_max_by_field=np.max(np.abs(error), axis=0).tolist(),
                capture_seconds=time.perf_counter()-started)
    path = output / f"handoff_{threshold:g}.npz"
    np.savez_compressed(path, a=state[0], readout=state[1], values=state[2],
                        keys=state[3], clock=state[4], matrix=matrix, drift=drift,
                        residual=residual, fourier=fourier, query_f=query_f,
                        query_c=query_c, query_b=query_b, time=t)
    info["handoff_sha256"] = digest(path)
    budget.guard()
    return info


def save_state(path, state, **extra):
    np.savez_compressed(path, closure_a=state[0], closure_readout=state[1],
                        values=state[2], keys=state[3], clock=state[4], **extra)


def run_closure(task, q, step, output, reference, a0, w0, initial_hashes, budget, schedule=None):
    output.mkdir(parents=True, exist_ok=False)
    started = time.perf_counter()
    inputs, labels = task_arrays(task)
    ref = load_reference(reference, task["case"], output.name)
    if not np.array_equal(labels, ref["labels"]):
        raise ValueError("Task labels differ from dense reference")
    reference_task = next(item for item in selected_tasks(reference / "circle_task_inputs.json")
                          if item["case"] == task["case"])
    reference_inputs, reference_labels = task_arrays(reference_task)
    train_angles = np.asarray(task["train_angles_radians"], dtype=np.float64)
    if (not np.array_equal(inputs, reference_inputs)
            or not np.array_equal(labels, reference_labels)
            or not np.array_equal(train_angles, ref["train_angles"])
            or not np.array_equal(train_angles, np.asarray(reference_task["train_angles_radians"]))):
        raise ValueError("Task geometry differs from the frozen dense reference")
    state = initial_state(a0, inputs, q)
    accepted = (state, 0.0)
    angles = ref["angles"]
    times, losses, residuals, captures = [], [], [], []
    used = set()
    t, last_print = 0.0, started
    final_time = FINAL_TIMES[task["case"]]
    max_steps = int(round(final_time / step))
    if max_steps * step != final_time:
        raise ValueError("Fixed endpoint does not lie on the integration grid")

    def rhs(candidate):
        budget.guard(candidate)
        return velocity(candidate, w0, inputs, labels)[0]

    try:
        for iteration in range(max_steps + 1):
            t = iteration * step
            budget.guard(state)
            vel, train = velocity(state, w0, inputs, labels)
            residual = train["f"] - labels
            loss = float(np.mean(residual**2))
            if not np.isfinite(loss) or loss > 1e6:
                raise FloatingPointError("Nonfinite or divergent closure loss")
            times.append(t); losses.append(loss); residuals.append(residual.copy())
            for threshold in THRESHOLDS:
                if threshold in used:
                    continue
                trigger = (loss <= threshold) if schedule is None else (
                    str(threshold) in schedule and t == schedule[str(threshold)])
                if trigger:
                    captures.append(capture(state, w0, inputs, labels, train, angles,
                                            threshold, t, output, budget))
                    used.add(threshold)
                    print(f"{task['case']} q={q} dt={step:g} handoff={threshold:g} t={t:g}", flush=True)
            if iteration == max_steps:
                break
            candidate = base.rk4(state, vel, rhs, step)
            budget.guard(candidate)
            accepted = (candidate, t + step)
            state = accepted[0]
            if time.perf_counter() - last_print > 25:
                print(f"{task['case']} q={q} dt={step:g} t={t:g} loss={loss:.6g}", flush=True)
                last_print = time.perf_counter()
        times, losses = np.asarray(times), np.asarray(losses)
        closure_output = predict(state, w0, base.circle_inputs(angles), budget)
        difference = closure_output - ref["dense_output"]
        away = np.abs(ref["dense_output"]) >= 0.05
        disagreements = np.sign(closure_output) != np.sign(ref["dense_output"])
        np.savez_compressed(output / "curves.npz", angles=angles, times=times,
            closure_loss=losses, closure_residual=np.asarray(residuals), closure_output=closure_output,
            dense_loss=np.interp(times, ref["times"], ref["dense_loss"]), dense_output=ref["dense_output"],
            dense_reference_times=ref["times"], dense_reference_loss=ref["dense_loss"],
            train_angles=np.asarray(task["train_angles_radians"]), labels=labels)
        save_state(output / "endpoint_states.npz", state)
        summary = dict(case=task["case"], q=q, order=q, width=WIDTH, seed=SEED, step=step,
            final_time=final_time, closure_final_loss=float(losses[-1]),
            dense_final_loss=float(ref["dense_loss"][-1]), closure_fitted=losses[-1] <= 1e-6,
            dense_fitted=bool(ref["dense_loss"][-1] <= 1e-6),
            fitted=bool(max(losses[-1], ref["dense_loss"][-1]) <= 1e-6),
            closure_vs_dense_rms=base.rms(difference), closure_vs_dense_max=float(np.max(np.abs(difference))),
            closure_dense_sign_disagreement=float(np.mean(disagreements)),
            closure_dense_sign_disagreement_away=float(np.mean(disagreements[away])) if away.any() else None,
            dense_away_fraction=float(np.mean(away)),
            closure_dense_fidelity_threshold_met=bool(base.rms(difference) <= .05 and np.mean(disagreements) <= .01),
            max_loss_error_vs_dense=common_loss_error(times, losses, ref["times"], ref["dense_loss"]),
            dense_loss_alignment="Interpolated only for plotting; metric uses exact common times",
            dense_refinement=dense_refinement(reference, task["case"]),
            handoffs=captures, missing_handoffs=[x for x in THRESHOLDS if x not in used],
            scalar_evaluated=False, moving_scalar_count=17, fixed_scalar_count=712,
            closure_moving_scalar_count=3*WIDTH+2*q*WIDTH*len(labels)+1,
            closure_fixed_mixer_count=WIDTH*WIDTH, dense_moving_scalar_count=WIDTH*WIDTH+3*WIDTH,
            wall_seconds=time.perf_counter()-started, highwater_rss_bytes=highwater_bytes(),
            **initial_hashes)
        # Python's JSON encoder does not accept NumPy booleans.
        summary["closure_fitted"] = bool(summary["closure_fitted"])
        write_json(output / "summary.json", summary)
        print(f"FINISHED closure {task['case']} q={q} dt={step:g} loss={losses[-1]:.6g}", flush=True)
        return summary
    except Exception as error:
        signal.setitimer(signal.ITIMER_REAL, 0)
        accepted_state, accepted_time = accepted
        save_state(output / "partial_state.npz", accepted_state, time=accepted_time)
        np.savez_compressed(output / "partial_curves.npz", times=np.asarray(times),
                            closure_loss=np.asarray(losses), closure_residual=np.asarray(residuals))
        write_json(output / "failure.json", dict(type=type(error).__name__, message=str(error),
                   accepted_time=accepted_time, wall_seconds=time.perf_counter()-started,
                   highwater_rss_bytes=highwater_bytes()))
        raise


def refinement(first, second, scalar=False):
    with np.load(first / "curves.npz", allow_pickle=False) as a, np.load(second / "curves.npz", allow_pickle=False) as b:
        endpoint = base.rms(a["closure_output"] - b["closure_output"])
        loss = common_loss_error(a["times"], a["closure_loss"], b["times"], b["closure_loss"])
        value = dict(closure_endpoint_rms=endpoint, closure_loss_max=loss,
                     closure_passed=endpoint <= .002 and loss <= .001,
                     compared_resolutions=[first.name, second.name], scalar_checked=scalar)
        if scalar:
            key = "scalar_output_0.01"
            available = key in a and key in b
            value["primary_scalar_endpoint_rms"] = base.rms(a[key]-b[key]) if available else None
            value["primary_scalar_available"] = available
            value["primary_scalar_passed"] = available and value["primary_scalar_endpoint_rms"] <= .002
            value["passed"] = value["closure_passed"] and value["primary_scalar_passed"]
        else:
            value["passed"] = value["closure_passed"]
        return value


def evaluate_scalar(directory, budget):
    budget.guard()
    summary = json.loads((directory / "summary.json").read_text())
    if summary.get("scalar_evaluated"):
        raise ValueError("Scalar stage was already applied to this resolution")
    with np.load(directory / "curves.npz", allow_pickle=False) as source:
        curves = {key: source[key].copy() for key in source.files}
    shutil.copy2(directory / "curves.npz", directory / "closure_curves.npz")
    shutil.copy2(directory / "summary.json", directory / "closure_summary.json")
    started = time.perf_counter()
    basis = base.fourier_basis(curves["angles"])
    train_basis = base.fourier_basis(curves["train_angles"])
    away = np.abs(curves["dense_output"]) >= .05
    captures = []
    for info in summary["handoffs"]:
        budget.guard()
        tag = f"{info['threshold']:g}"
        handoff_path = directory / f"handoff_{tag}.npz"
        if digest(handoff_path) != info["handoff_sha256"]:
            raise ValueError("Frozen handoff coefficients changed: " + str(handoff_path))
        with np.load(handoff_path, allow_pickle=False) as source:
            item = {key: source[key].copy() for key in
                    ("matrix", "drift", "residual", "fourier", "query_f", "query_c", "query_b")}
        mask = curves["times"] >= info["time"]
        times = curves["times"][mask]
        scalar, nfev = base.scalar_solution(item["matrix"], item["drift"], item["residual"], times)
        budget.guard()
        integral, norm_integral = scalar[-1, 8:16], scalar[-1, 16]
        coefficients = item["fourier"] @ np.concatenate(([1.], -integral, [norm_integral]))
        output = basis @ coefficients
        train_output = train_basis @ coefficients
        direct = item["query_f"] - item["query_c"] @ integral + item["query_b"] * norm_integral
        static_fourier = basis @ item["fourier"][:, 0]
        loss = np.mean(scalar[:, :8]**2, axis=1)
        residual_identity = curves["labels"] + item["residual"] - item["matrix"] @ integral + item["drift"] * norm_integral
        signs = np.sign(output) != np.sign(curves["dense_output"])
        summary_item = dict(info)
        summary_item.update(
            scalar_vs_dense_rms=base.rms(output-curves["dense_output"]),
            scalar_vs_dense_max=float(np.max(np.abs(output-curves["dense_output"]))),
            scalar_vs_closure_rms=base.rms(output-curves["closure_output"]),
            scalar_vs_closure_max=float(np.max(np.abs(output-curves["closure_output"]))),
            direct_scalar_vs_closure_rms=base.rms(direct-curves["closure_output"]),
            direct_scalar_vs_closure_max=float(np.max(np.abs(direct-curves["closure_output"]))),
            fourier_output_error_rms=base.rms(output-direct),
            fourier_output_error_max=float(np.max(np.abs(output-direct))),
            static_vs_closure_rms=base.rms(item["query_f"]-curves["closure_output"]),
            static_vs_closure_max=float(np.max(np.abs(item["query_f"]-curves["closure_output"]))),
            fourier_static_vs_closure_rms=base.rms(static_fourier-curves["closure_output"]),
            sign_disagreement=float(np.mean(signs)),
            sign_disagreement_away=float(np.mean(signs[away])) if away.any() else None,
            dense_away_fraction=float(np.mean(away)), scalar_final_loss=float(loss[-1]),
            scalar_ode_fitted=bool(loss[-1] <= 1e-6),
            fourier_predictor_train_mse=float(np.mean((train_output-curves["labels"])**2)),
            fourier_train_consistency_max=float(np.max(np.abs(train_output-curves["labels"]-scalar[-1,:8]))),
            exact_train_observer_consistency_max=float(np.max(np.abs(residual_identity-curves["labels"]-scalar[-1,:8]))),
            max_loss_error_vs_closure=float(np.max(np.abs(loss-curves["closure_loss"][mask]))),
            max_loss_error_vs_dense=common_loss_error(times, loss,
                curves["dense_reference_times"][curves["dense_reference_times"] >= times[0]],
                curves["dense_reference_loss"][curves["dense_reference_times"] >= times[0]]),
            scalar_final_residual=scalar[-1,:8].tolist(), scalar_nfev=nfev)
        summary_item["fourier_function_fitted"] = summary_item["fourier_predictor_train_mse"] <= 1e-6
        summary_item["dense_fidelity_threshold_met"] = summary_item["scalar_vs_dense_rms"] <= .05 and summary_item["sign_disagreement"] <= .01
        summary_item["closure_fidelity_threshold_met"] = summary_item["scalar_vs_closure_rms"] <= .01 and summary_item["scalar_vs_closure_max"] <= .05
        captures.append(summary_item)
        for key, value in (("scalar_output", output), ("scalar_direct_output", direct),
                           ("static_output", item["query_f"]), ("fourier_static_output", static_fourier),
                           ("scalar_times", times), ("scalar_loss", loss), ("scalar_state", scalar)):
            curves[f"{key}_{tag}"] = value
    np.savez_compressed(directory / "curves.npz", **curves)
    summary.update(handoffs=captures, scalar_evaluated=True,
                   scalar_wall_seconds=time.perf_counter()-started, highwater_rss_bytes=highwater_bytes())
    write_json(directory / "summary.json", summary)
    return summary


def checks(output):
    rng = np.random.default_rng(48791)
    n, m = 7, 3
    a, w0 = base.initialized(n, m, 123)
    inputs = base.circle_inputs(np.array([.2, .7, 1.3]))
    labels = np.array([1., -1., 1.])
    queries = np.concatenate((inputs, base.circle_inputs(np.array([2.1, 4.2]))), axis=1)
    records = []

    def check(name, error, tolerance):
        error = float(error)
        records.append(dict(name=name, maximum_absolute_error=error, tolerance=tolerance,
                            passed=np.isfinite(error) and error <= tolerance))

    for q in (1, 2, 3):
        state = (a.copy(), rng.normal(size=n), rng.normal(scale=.3, size=(q,n,m)),
                 rng.normal(scale=.2, size=(q,n,m)), np.array([2.3]))
        vel, train = velocity(state, w0, inputs, labels)
        residual, rho = train["f"]-labels, base.rms(train["f"]-labels)
        tau = float(state[4][0])
        scale = weights(state)
        # Independent matrix form of the raw triangular moment ODE.
        dilation = np.diag(np.arange(q)) + np.tril(np.broadcast_to(scale, (q,q)), -1)
        raw_h, raw_delta = tau*state[3], -state[2]/2
        raw_h_dot = rho*train["h"][None,:,:] - rho/tau*np.einsum('ji,ink->jnk', dilation, raw_h)
        raw_delta_dot = (train["d"]*residual)[None,:,:] - rho/tau*np.einsum('ji,ink->jnk', dilation, raw_delta)
        check(f"q{q}_raw_normalized_keys", np.max(np.abs((raw_h_dot-rho*state[3])/tau-vel[3])), 2e-12)
        check(f"q{q}_raw_normalized_values", np.max(np.abs(-2*raw_delta_dot-vel[2])), 2e-12)
        middle = materialized_middle(state, w0)
        direct_fields = base.fields((state[0], middle, state[1]), "dense", w0, queries)
        actual_fields = fields(state, w0, queries)
        for key in ("h", "g", "d", "ell", "f"):
            check(f"q{q}_materialized_{key}", np.max(np.abs(direct_fields[key]-actual_fields[key])), 2e-12)
        middle_dot = sum(weight*(vel[2][j]@state[3][j].T+state[2][j]@vel[3][j].T)
                         for j,weight in enumerate(scale))/(m*n)
        vstar, kstar = endpoint_sums(state)
        endpoint_dot = -2*(train["d"]*residual)@kstar.T/(m*n)+rho/(m*n*tau)*vstar@(train["h"]-kstar).T
        dense_dot = -2*(train["d"]*residual)@train["h"].T/(m*n)
        dense_plus_defect = dense_dot+(2*train["d"]*residual+rho/tau*vstar)@(train["h"]-kstar).T/(m*n)
        check(f"q{q}_middle_endpoint_derivative", np.max(np.abs(middle_dot-endpoint_dot)), 2e-12)
        check(f"q{q}_middle_dense_plus_defect", np.max(np.abs(middle_dot-dense_plus_defect)), 2e-12)
        _, matrix, drift = response(state, w0, inputs, train, queries)
        aggregate = -matrix@residual+np.linalg.norm(residual)*drift
        independent = (vel[1]@actual_fields["g"]+np.sum(actual_fields["d"]*(middle_dot@actual_fields["h"]),axis=0)
                       +np.sum(actual_fields["ell"]*(vel[0]@queries),axis=0))/n
        check(f"q{q}_scalar_aggregate_identity", np.max(np.abs(aggregate-independent)), 2e-12)
        finite_difference = []
        for epsilon in (1e-4,1e-5,1e-6):
            plus = tuple(x+epsilon*v for x,v in zip(state,vel))
            minus = tuple(x-epsilon*v for x,v in zip(state,vel))
            fd=(predict(plus,w0,queries)-predict(minus,w0,queries))/(2*epsilon)
            finite_difference.append(float(np.max(np.abs(fd-aggregate))))
        check(f"q{q}_noninitial_query_difference", min(finite_difference), 1e-8)
        records[-1]["step_errors"] = finite_difference
        stopped, _ = velocity(state, w0, inputs, train["f"].copy())
        check(f"q{q}_zero_residual_stop", max(np.max(np.abs(x)) for x in stopped), 0)
        initial = initial_state(a, inputs, q)
        initial_vel, initial_fields = velocity(initial, w0, inputs, labels)
        check(f"q{q}_initial_middle", np.max(np.abs(materialized_middle(initial,w0)-w0)), 0)
        check(f"q{q}_initial_output", np.max(np.abs(initial_fields["f"])), 0)
        check(f"q{q}_initial_keys", np.max(np.abs(initial[3][0]-np.tanh(a@inputs))), 0)
        check(f"q{q}_initial_stationary_modes", max(np.max(np.abs(initial_vel[i])) for i in (0,2,3)), 0)
        if q > 1:
            check(f"q{q}_initial_higher_keys", np.max(np.abs(initial[3][1:])), 0)
            check(f"q{q}_nonzero_higher_modes", float(np.max(np.abs(state[2][1:]))) == 0, 0)
        if q == 1:
            old_state=(state[0],state[1],state[2][0],state[3][0],state[4])
            old_vel, old_fields=base.velocity(old_state,"q1",w0,inputs,labels)
            old_vel=(old_vel[0],old_vel[1],old_vel[2][None,:,:],old_vel[3][None,:,:],old_vel[4])
            check("q1_velocity_parity",max(np.max(np.abs(x-y)) for x,y in zip(vel,old_vel)),2e-12)
            check("q1_output_parity",np.max(np.abs(train["f"]-old_fields["f"])),2e-12)
            old_response=base.response(old_state,w0,inputs,old_fields,queries)
            new_response=response(state,w0,inputs,train,queries)
            check("q1_response_parity",max(np.max(np.abs(x-y)) for x,y in zip(old_response,new_response)),2e-12)
    result=dict(passed=all(item["passed"] for item in records),checks=records,
                count=len(records), scope="tiny deterministic q=1,2,3 checks; no training")
    write_json(output/"checks.json",result)
    if not result["passed"]:
        raise AssertionError("Higher-order checks failed; see checks.json")
    return result


def frozen_sources(output):
    sources=[Path(__file__).resolve(),Path(base.__file__).resolve(),
             HERE/"HIGHER_ORDER_EXPERIMENT_PLAN.md",HERE/"circle_task_inputs.json"]
    hashes={str(path):digest(path) for path in sources}
    if digest(base.__file__) != BASE_HASH:
        raise ValueError("The frozen q1 helper source hash changed")
    for path in sources:
        shutil.copy2(path, output/path.name)
    return hashes


def campaign(reference, output, a0, w0, initial_hashes, budget, scalar=False, original_results=None):
    tasks=selected_tasks(output/"circle_task_inputs.json")
    results=[]
    for task in tasks:
        for q in ORDERS:
            directory=output/task["case"]/f"q{q}"
            if scalar:
                summaries={name:json.loads((directory/name/"summary.json").read_text())
                           for name in ("coarse","fine","refined") if (directory/name/"summary.json").exists()}
                for name in summaries:
                    summaries[name]=evaluate_scalar(directory/name,budget)
            else:
                summaries={}
                summaries["coarse"]=run_closure(task,q,1/8,directory/"coarse",reference,a0,w0,initial_hashes,budget)
                schedule={str(item["threshold"]):item["time"] for item in summaries["coarse"]["handoffs"]}
                summaries["fine"]=run_closure(task,q,1/16,directory/"fine",reference,a0,w0,initial_hashes,budget,schedule)
            schedule={str(item["threshold"]):item["time"] for item in summaries["coarse"]["handoffs"]}
            names=("fine","refined") if "refined" in summaries else ("coarse","fine")
            sensitivity=refinement(directory/names[0],directory/names[1],scalar)
            need_refinement=not sensitivity["closure_passed"] or (scalar and
                sensitivity["primary_scalar_available"] and not sensitivity["primary_scalar_passed"])
            if need_refinement and "refined" not in summaries:
                summaries["refined"]=run_closure(task,q,1/32,directory/"refined",reference,a0,w0,initial_hashes,budget,schedule)
                if scalar:
                    summaries["refined"]=evaluate_scalar(directory/"refined",budget)
                sensitivity=refinement(directory/"fine",directory/"refined",scalar)
            selected="refined" if "refined" in summaries else "fine"
            item=dict(case=task["case"],q=q,order=q,selected=selected,refinement=sensitivity,**summaries)
            results.append(item)
            write_json(output/"results.json",dict(stage="scalar" if scalar else "closure",
                complete=False,scalar_evaluated=scalar,results=results,
                wall_seconds=time.perf_counter()-budget.started))
    return results


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    mode=parser.add_mutually_exclusive_group()
    mode.add_argument("--check",action="store_true")
    mode.add_argument("--scalar",action="store_true")
    parser.add_argument("--reference",type=Path)
    parser.add_argument("--run",type=Path,help="Completed closure-stage input for --scalar")
    parser.add_argument("--budget",type=float,default=3600,
                        help="Remaining invocation allowance; caller reserves analysis/check costs")
    args=parser.parse_args()
    output=args.output.resolve()
    previous_seconds=0.0
    original=None
    if args.scalar:
        if args.run is None:
            parser.error("--scalar requires --run")
        source=args.run.resolve()
        if output==source or source in output.parents:
            parser.error("Scalar output must be a fresh root outside its source run")
        original=json.loads((source/"results.json").read_text())
        prior=json.loads((source/"provenance.json").read_text())
        if not original.get("complete") or original.get("stage")!="closure":
            raise ValueError("Scalar stage requires a complete closure-only run")
        if prior["producer_sha256"] != digest(__file__) or prior["base_sha256"] != digest(base.__file__):
            raise ValueError("Producer/helper changed since the closure stage")
        for path, expected in prior["source_hashes"].items():
            if digest(source / Path(path).name) != expected or digest(path) != expected:
                raise ValueError("A frozen scientific input changed: " + path)
        reference=Path(prior["dense_reference_root"])
        for path,expected in prior["dense_reference_hashes"].items():
            if digest(path)!=expected:
                raise ValueError("A frozen dense reference changed: "+path)
        previous_seconds=float(original["cumulative_producer_seconds"])
        shutil.copytree(source,output)
        shutil.copy2(output/"provenance.json",output/"closure_provenance.json")
        shutil.copy2(output/"results.json",output/"closure_results.json")
        write_json(output/"results.json",dict(stage="scalar",complete=False,
            scalar_evaluated=False,results=[],cumulative_producer_seconds=previous_seconds))
    else:
        if not args.check and args.reference is None:
            parser.error("Closure stage requires --reference")
        reference=args.reference.resolve() if args.reference else None
        output.mkdir(parents=True,exist_ok=False)
    allowance=min(args.budget,3600-previous_seconds)
    with threadpool_limits(limits=2):
        sources=frozen_sources(output)
        provenance=dict(command=sys.argv,python=sys.version,executable=sys.executable,
            numpy=np.__version__,scipy=scipy.__version__,platform=platform.platform(),
            threads=threadpool_info(),source_hashes=sources,producer_sha256=digest(__file__),
            base_sha256=digest(base.__file__),plan_sha256=digest(HERE/"HIGHER_ORDER_EXPERIMENT_PLAN.md"),
            stage="check" if args.check else ("scalar" if args.scalar else "closure"),
            budget_seconds=allowance,prior_producer_seconds=previous_seconds,
            cumulative_limit_seconds=3600,memory_limit_bytes=MEMORY_LIMIT)
        if reference is not None:
            provenance.update(dense_reference_root=str(reference),dense_reference_hashes=reference_files(reference))
        write_json(output/"provenance.json",provenance)
        started=time.perf_counter()
        try:
            with Budget(allowance) as budget:
                if args.check:
                    result=checks(output)
                    result["wall_seconds"]=time.perf_counter()-started
                    write_json(output/"checks.json",result)
                    print(json.dumps(result,indent=2));return
                if args.scalar:
                    with np.load(output/"initialization.npz",allow_pickle=False) as init:
                        a0,w0=init["a"].copy(),init["w0"].copy()
                    initial_hashes=dict(a_initial_hash=base.array_digest(a0),w0_initial_hash=base.array_digest(w0))
                else:
                    a0,w0,initial_hashes=verified_initialization(reference,output)
                results=campaign(reference,output,a0,w0,initial_hashes,budget,args.scalar,original)
                elapsed=time.perf_counter()-started
                write_json(output/"results.json",dict(stage="scalar" if args.scalar else "closure",
                    complete=True,scalar_evaluated=args.scalar,results=results,wall_seconds=elapsed,
                    cumulative_producer_seconds=previous_seconds+elapsed,highwater_rss_bytes=highwater_bytes()))
        except Exception as error:
            write_json(output/"failure.json",dict(type=type(error).__name__,message=str(error),
                       wall_seconds=time.perf_counter()-started,prior_producer_seconds=previous_seconds,
                       highwater_rss_bytes=highwater_bytes()))
            raise


if __name__=="__main__":
    main()
