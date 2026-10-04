"""Matched dense/q1 circle runs and finite frozen-response scalar observers.

All outputs go to an explicitly supplied fresh study-generated directory.
Run with --check for deterministic upstream and observer validation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import sys
import time

import numpy as np
import scipy
from scipy.integrate import solve_ivp
from threadpoolctl import threadpool_info, threadpool_limits
import psutil

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
THRESHOLDS = (0.1, 0.01, 0.001)
FREQUENCIES = np.arange(1, 64, 2)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def array_digest(a):
    return hashlib.sha256(np.ascontiguousarray(a).tobytes()).hexdigest()


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def derivative(z):
    q = np.exp(-2 * np.abs(z))
    return 4 * q / (1 + q) ** 2


def initialized(n, m, seed):
    rng = np.random.default_rng(seed)
    a = rng.standard_normal((n, 2))
    w0 = rng.standard_normal((n, n)) / np.sqrt(n)
    return a, w0


def fields(state, kind, w0, inputs, backward=True):
    if kind == "dense":
        a, middle, readout = state
    else:
        a, readout, values, keys, clock = state
    n = a.shape[0]
    first_z = a @ inputs
    first = np.tanh(first_z)
    if kind == "dense":
        second_z = middle @ first
    else:
        m = keys.shape[1]
        second_z = w0 @ first + values @ (keys.T @ first) / (m * n)
    second = np.tanh(second_z)
    result = {"h": first, "g": second, "f": readout @ second / n}
    if backward:
        delta = readout[:, None] * derivative(second_z)
        if kind == "dense":
            previous = middle.T @ delta
        else:
            previous = w0.T @ delta + keys @ (values.T @ delta) / (m * n)
        result.update(d=delta, ell=derivative(first_z) * previous)
    return result


def velocity(state, kind, w0, inputs, labels):
    f = fields(state, kind, w0, inputs)
    r = f["f"] - labels
    n, m = f["h"].shape
    adot = -2 / m * ((f["ell"] * r) @ inputs.T)
    wdot = -2 / m * (f["g"] @ r)
    if kind == "dense":
        middle_dot = -2 / (m * n) * ((f["d"] * r) @ f["h"].T)
        result = (adot, middle_dot, wdot)
    else:
        rho = np.linalg.norm(r) / np.sqrt(m)
        result = (adot, wdot, -2 * f["d"] * r,
                  rho / float(state[4][0]) * (f["h"] - state[3]),
                  np.array([rho]))
    return result, f


def rk4(state, first_velocity, rhs, step):
    second = rhs(tuple(s + step / 2 * v for s, v in zip(state, first_velocity)))
    third = rhs(tuple(s + step / 2 * v for s, v in zip(state, second)))
    fourth = rhs(tuple(s + step * v for s, v in zip(state, third)))
    return tuple(s + step / 6 * (v1 + 2 * v2 + 2 * v3 + v4)
                 for s, v1, v2, v3, v4 in zip(state, first_velocity, second, third, fourth))


def response(state, w0, train_inputs, train_fields, query_inputs, block=256):
    n, m = train_fields["h"].shape
    _, _, values, keys, clock = state
    outputs, matrices, drifts = [], [], []
    for start in range(0, query_inputs.shape[1], block):
        query = query_inputs[:, start:start + block]
        q = fields(state, "q1", w0, query)
        matrix = (2 / m) * (
            q["g"].T @ train_fields["g"] / n
            + (query.T @ train_inputs) * (q["ell"].T @ train_fields["ell"] / n)
            + (q["d"].T @ train_fields["d"] / n) * (q["h"].T @ keys / n))
        drift = np.sum((q["d"].T @ values / n)
                       * (q["h"].T @ (train_fields["h"] - keys) / n), axis=1)
        drift /= m * np.sqrt(m) * float(clock[0])
        outputs.append(q["f"])
        matrices.append(matrix)
        drifts.append(drift)
    return np.concatenate(outputs), np.concatenate(matrices), np.concatenate(drifts)


def circle_inputs(angles):
    return np.stack((np.cos(angles), np.sin(angles)))


def fourier_coefficients(samples):
    spectrum = np.fft.rfft(samples, axis=0) / len(samples)
    return np.concatenate((2 * spectrum[FREQUENCIES].real,
                           -2 * spectrum[FREQUENCIES].imag), axis=0)


def fourier_basis(angles):
    phase = np.asarray(angles)[:, None] * FREQUENCIES[None, :]
    return np.concatenate((np.cos(phase), np.sin(phase)), axis=1)


def predict(state, kind, w0, inputs, block=256):
    return np.concatenate([fields(state, kind, w0, inputs[:, i:i + block], False)["f"]
                           for i in range(0, inputs.shape[1], block)])


def scalar_solution(matrix, drift, residual, times):
    m = len(residual)
    initial = np.concatenate((residual, np.zeros(m + 1)))
    def rhs(t, state):
        r = state[:m]
        norm = np.linalg.norm(r)
        return np.concatenate((-matrix @ r + norm * drift, r, [norm]))
    if times[-1] == times[0]:
        return initial[None, :], 0
    solved = solve_ivp(rhs, (times[0], times[-1]), initial, method="DOP853",
                       t_eval=times, rtol=1e-10, atol=1e-12)
    if not solved.success or not np.isfinite(solved.y).all():
        raise RuntimeError("Scalar integrator failed: " + solved.message)
    return solved.y.T, solved.nfev


def rms(a):
    return float(np.sqrt(np.mean(np.asarray(a) ** 2)))


def capture(state, w0, inputs, labels, train_fields, angles, threshold, t, output):
    start = time.perf_counter()
    _, matrix, drift = response(state, w0, inputs, train_fields, inputs)
    sample_angles = 2 * np.pi * np.arange(2048) / 2048
    sample_f, sample_c, sample_b = response(state, w0, inputs, train_fields,
                                          circle_inputs(sample_angles))
    coeff = fourier_coefficients(np.column_stack((sample_f, sample_c, sample_b)))
    query_f, query_c, query_b = response(state, w0, inputs, train_fields,
                                       circle_inputs(angles))
    direct = np.column_stack((query_f, query_c, query_b))
    spatial_error = fourier_basis(angles) @ coeff - direct
    sym = (matrix + matrix.T) / 2
    margin = float(np.linalg.eigvalsh(sym)[0] - np.linalg.norm(drift))
    # Physical residual subspace for the one dataset consisting of antipodal pairs.
    projected_margin = None
    if np.max(np.abs(inputs[:, :4] + inputs[:, 4:])) < 1e-12 and np.array_equal(labels[:4], -labels[4:]):
        basis = np.vstack((np.eye(4), -np.eye(4))) / np.sqrt(2)
        projected_margin = float(np.linalg.eigvalsh(basis.T @ sym @ basis)[0]
                                 - np.linalg.norm(basis.T @ drift))
    item = dict(threshold=threshold, time=t, train_mse=rms(train_fields["f"] - labels)**2,
                matrix=matrix, drift=drift, residual=train_fields["f"] - labels,
                fourier=coeff, query_f=query_f, query_c=query_c, query_b=query_b,
                margin=margin, projected_margin=projected_margin,
                spatial_rms_by_field=np.sqrt(np.mean(spatial_error**2, axis=0)).tolist(),
                spatial_max_by_field=np.max(np.abs(spatial_error), axis=0).tolist(),
                capture_seconds=time.perf_counter() - start)
    np.savez_compressed(output / f"handoff_{threshold:g}.npz", **dict(
        a=state[0], readout=state[1], values=state[2], keys=state[3], clock=state[4],
        matrix=matrix, drift=drift, residual=item["residual"], fourier=coeff,
        query_f=query_f, query_c=query_c, query_b=query_b, time=t))
    return item


def run_case(task, n, seed, step, output, deadline, final_time=None, schedule=None):
    output.mkdir()
    begin = time.perf_counter()
    inputs = np.array(task["normalized_inputs_u"], dtype=float)
    if inputs.shape == (8, 2):
        inputs = inputs.T
    labels = np.array(task["labels"], dtype=float)
    if inputs.shape != (2, 8):
        raise ValueError(f"Unexpected task orientation {inputs.shape}")
    m = len(labels)
    a, w0 = initialized(n, m, seed)
    dense = (a.copy(), w0.copy(), np.zeros(n))
    q1 = (a.copy(), np.zeros(n), np.zeros((n, m)), np.tanh(a @ inputs), np.ones(1))
    angles = 2 * np.pi * (np.arange(8192) + 0.5) / 8192
    queries = circle_inputs(angles)
    times, dense_losses, q1_losses, q1_residuals = [], [], [], []
    captures = []
    used = set()
    peak_rss = psutil.Process().memory_info().rss
    maximum = final_time if final_time is not None else 512.
    max_steps = int(round(maximum / step))
    last_print = begin
    for iteration in range(max_steps + 1):
        t = iteration * step
        if time.perf_counter() > deadline:
            raise TimeoutError("Precommitted cumulative wall budget exhausted")
        dv, df = velocity(dense, "dense", w0, inputs, labels)
        qv, qf = velocity(q1, "q1", w0, inputs, labels)
        dense_loss = rms(df["f"] - labels) ** 2
        q1_loss = rms(qf["f"] - labels) ** 2
        if not np.isfinite(dense_loss + q1_loss) or max(dense_loss, q1_loss) > 1e6:
            raise FloatingPointError("Nonfinite or divergent full dynamics")
        times.append(t); dense_losses.append(dense_loss); q1_losses.append(q1_loss)
        q1_residuals.append(qf["f"] - labels)
        for threshold in THRESHOLDS:
            if threshold in used:
                continue
            triggered = (q1_loss <= threshold) if schedule is None else (
                str(threshold) in schedule and abs(t - schedule[str(threshold)]) < step / 4)
            if triggered:
                captures.append(capture(q1, w0, inputs, labels, qf, angles, threshold, t, output))
                used.add(threshold)
                print(f"{task['case']} dt={step:g} handoff {threshold:g} at t={t:g}", flush=True)
        peak_rss = max(peak_rss, psutil.Process().memory_info().rss)
        if iteration == max_steps or (final_time is None and max(dense_loss, q1_loss) <= 1e-7):
            break
        dense = rk4(dense, dv, lambda s: velocity(s, "dense", w0, inputs, labels)[0], step)
        q1 = rk4(q1, qv, lambda s: velocity(s, "q1", w0, inputs, labels)[0], step)
        if time.perf_counter() - last_print > 25:
            print(f"{task['case']} dt={step:g} t={t:g} dense={dense_loss:.3g} q1={q1_loss:.3g}", flush=True)
            last_print = time.perf_counter()
    times = np.asarray(times)
    dense_output = predict(dense, "dense", w0, queries)
    q1_output = predict(q1, "q1", w0, queries)
    curve_data = dict(angles=angles, times=times, dense_loss=np.array(dense_losses),
                      q1_loss=np.array(q1_losses), q1_residual=np.array(q1_residuals),
                      dense_output=dense_output, q1_output=q1_output,
                      train_angles=np.array(task["train_angles_radians"]), labels=labels)
    summaries = []
    basis = fourier_basis(angles)
    for item in captures:
        mask = times >= item["time"]
        scalar, evaluations = scalar_solution(item["matrix"], item["drift"], item["residual"], times[mask])
        integrated = scalar[-1, m:2*m]
        integrated_norm = scalar[-1, -1]
        weights = np.concatenate(([1.], -integrated, [integrated_norm]))
        scalar_output = basis @ (item["fourier"] @ weights)
        fourier_train_output = fourier_basis(np.array(task["train_angles_radians"])) @ (item["fourier"] @ weights)
        direct_output = item["query_f"] - item["query_c"] @ integrated + item["query_b"] * integrated_norm
        exact_train_observer = labels + item["residual"] - item["matrix"] @ integrated + item["drift"] * integrated_norm
        scalar_loss = np.mean(scalar[:, :m] ** 2, axis=1)
        tag = f"{item['threshold']:g}"
        curve_data[f"scalar_output_{tag}"] = scalar_output
        curve_data[f"scalar_direct_output_{tag}"] = direct_output
        curve_data[f"static_output_{tag}"] = item["query_f"]
        curve_data[f"scalar_times_{tag}"] = times[mask]
        curve_data[f"scalar_loss_{tag}"] = scalar_loss
        curve_data[f"scalar_state_{tag}"] = scalar
        off_boundary = np.abs(dense_output) >= 0.05
        sign_error = (np.sign(scalar_output) != np.sign(dense_output))
        summary = {k: v for k, v in item.items() if not isinstance(v, np.ndarray)}
        summary.update(scalar_vs_dense_rms=rms(scalar_output - dense_output),
                       scalar_vs_dense_max=float(np.max(np.abs(scalar_output-dense_output))),
                       scalar_vs_q1_rms=rms(scalar_output - q1_output),
                       scalar_vs_q1_max=float(np.max(np.abs(scalar_output-q1_output))),
                       direct_scalar_vs_q1_rms=rms(direct_output-q1_output),
                       fourier_output_error_rms=rms(scalar_output-direct_output),
                       static_vs_q1_rms=rms(item["query_f"]-q1_output),
                       sign_disagreement=float(np.mean(sign_error)),
                       sign_disagreement_away=float(np.mean(sign_error[off_boundary])),
                       dense_away_fraction=float(np.mean(off_boundary)),
                       scalar_final_loss=float(scalar_loss[-1]),
                       fourier_predictor_train_mse=rms(fourier_train_output-labels)**2,
                       fourier_train_consistency_max=float(np.max(np.abs(fourier_train_output-labels-scalar[-1,:m]))),
                       exact_train_observer_consistency_max=float(np.max(np.abs(exact_train_observer-labels-scalar[-1,:m]))),
                       max_loss_error_vs_q1=float(np.max(np.abs(scalar_loss-np.array(q1_losses)[mask]))),
                       scalar_final_residual=scalar[-1,:m].tolist(),
                       scalar_nfev=evaluations)
        summaries.append(summary)
    np.savez_compressed(output / "curves.npz", **curve_data)
    np.savez_compressed(output / "endpoint_states.npz", dense_a=dense[0], dense_w=dense[1],
                        dense_readout=dense[2], q1_a=q1[0], q1_readout=q1[1], values=q1[2],
                        keys=q1[3], clock=q1[4])
    summary = dict(case=task["case"], width=n, seed=seed, step=step, final_time=float(times[-1]),
                   dense_final_loss=dense_losses[-1], q1_final_loss=q1_losses[-1],
                   fitted=max(dense_losses[-1],q1_losses[-1]) <= 1e-6,
                   q1_vs_dense_rms=rms(q1_output-dense_output),
                   q1_vs_dense_max=float(np.max(np.abs(q1_output-dense_output))),
                   q1_dense_sign_disagreement=float(np.mean(np.sign(q1_output)!=np.sign(dense_output))),
                   handoffs=summaries, wall_seconds=time.perf_counter()-begin,
                   peak_rss_bytes=peak_rss, a_initial_hash=array_digest(a), w0_initial_hash=array_digest(w0),
                   moving_scalar_count=2*m+1, fixed_scalar_count=m*m+m+(m+2)*64,
                   dense_moving_scalar_count=n*n+3*n, q1_moving_scalar_count=3*n+2*n*m+1,
                   q1_fixed_mixer_count=n*n)
    write_json(output / "summary.json", summary)
    print(f"FINISHED {task['case']} dt={step:g} t={times[-1]:g} wall={summary['wall_seconds']:.1f}s", flush=True)
    return summary


def refinement(first, second):
    with np.load(first / "curves.npz") as a, np.load(second / "curves.npz") as b:
        values = {f"{model}_endpoint_rms": rms(a[f"{model}_output"] - b[f"{model}_output"])
                  for model in ("dense", "q1")}
        for model in ("dense", "q1"):
            values[f"{model}_loss_max"] = float(np.max(np.abs(
                a[f"{model}_loss"] - np.interp(a["times"],b["times"],b[f"{model}_loss"]))))
        key = "scalar_output_0.01"
        values["primary_scalar_endpoint_rms"] = rms(a[key]-b[key]) if key in a and key in b else None
        values["passed"] = all(values[f"{x}_endpoint_rms"] <= 0.002 for x in ("dense","q1")) and all(
            values[f"{x}_loss_max"] <= 0.001 for x in ("dense","q1")) and (
                values["primary_scalar_endpoint_rms"] is not None and values["primary_scalar_endpoint_rms"] <= 0.002)
        return values


def checks(output):
    sys.path.insert(0, str(ROOT / "code"))
    from pde.finite_network import Parameters, flow_velocity, TANH
    rng = np.random.default_rng(879)
    n, m = 7, 3
    a, w0 = initialized(n,m,123)
    inputs = circle_inputs(np.array([0.2,0.7,1.3]))
    labels = np.array([1.,-1.,1.])
    dense = (a,w0,rng.normal(size=n))
    our,_ = velocity(dense,"dense",w0,inputs,labels)
    reference = flow_velocity(Parameters((a,w0),dense[2]),np.sqrt(2)*inputs,labels,TANH)
    errors = [float(np.max(np.abs(x-y))) for x,y in zip(our,reference.weights+(reference.readout,))]
    assert max(errors) < 2e-12, errors
    state = (a.copy(),rng.normal(size=n),rng.normal(size=(n,m)),
             rng.uniform(-0.8,0.8,size=(n,m)),np.array([2.3]))
    vel,train = velocity(state,"q1",w0,inputs,labels)
    query = np.concatenate((inputs,circle_inputs(np.array([2.1,4.2]))),axis=1)
    _,c,b = response(state,w0,inputs,train,query)
    residual=train['f']-labels
    exact=-c@residual+np.linalg.norm(residual)*b
    fd_errors=[]
    for eps in (1e-4,1e-5,1e-6):
        plus=tuple(s+eps*v for s,v in zip(state,vel));minus=tuple(s-eps*v for s,v in zip(state,vel))
        numerical=(predict(plus,"q1",w0,query)-predict(minus,"q1",w0,query))/(2*eps)
        fd_errors.append(float(np.max(np.abs(numerical-exact))))
    assert min(fd_errors) < 1e-8, fd_errors
    angles=2*np.pi*np.arange(2048)/2048
    values=(1.3*np.cos(3*angles)-0.4*np.sin(7*angles))[:,None]
    test_angles=2*np.pi*(np.arange(8192)+0.5)/8192
    reconstruction=fourier_basis(test_angles)@fourier_coefficients(values)
    fourier_error=float(np.max(np.abs(reconstruction[:,0]-(1.3*np.cos(3*test_angles)-.4*np.sin(7*test_angles)))))
    assert fourier_error < 1e-13
    times=np.linspace(0,3,31)
    solved,_=scalar_solution(np.array([[1.]]),np.array([.2]),np.array([-1.]),times)
    exponential=np.exp(-1.2*times)
    analytic=np.column_stack((-exponential,-(1-exponential)/1.2,(1-exponential)/1.2))
    scalar_error=float(np.max(np.abs(solved-analytic)))
    assert scalar_error < 1e-9
    write_json(output/'checks.json',dict(dense_rhs_max_errors=errors,q1_directional_errors=fd_errors,
                 fourier_error=fourier_error,scalar_analytic_error=scalar_error,passed=True))
    print((output/'checks.json').read_text(),flush=True)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--check',action='store_true')
    parser.add_argument('--budget',type=float,default=3600)
    args=parser.parse_args()
    args.output.mkdir(parents=True,exist_ok=False)
    start=time.perf_counter()
    with threadpool_limits(limits=2):
        sources=[Path(__file__),HERE/'CIRCLE_EXPERIMENT_PLAN.md',HERE/'circle_task_inputs.json']
        for source in sources: shutil.copy2(source,args.output/source.name)
        write_json(args.output/'provenance.json',dict(command=sys.argv,python=sys.version,
                   executable=sys.executable,numpy=np.__version__,scipy=scipy.__version__,
                   platform=platform.platform(),threads=threadpool_info(),
                   source_hashes={str(p.relative_to(ROOT)):digest(p) for p in sources},
                   budget_seconds=args.budget))
        if args.check:
            checks(args.output);return
        initial_a, initial_w0 = initialized(1024,8,20260920)
        np.savez_compressed(args.output/'initialization.npz',a=initial_a,w0=initial_w0,readout=np.zeros(1024))
        tasks=json.loads((HERE/'circle_task_inputs.json').read_text())['tasks']
        results=[]
        try:
            for task in tasks:
                directory=args.output/task['case'];directory.mkdir()
                coarse=run_case(task,1024,20260920,1/8,directory/'coarse',start+args.budget)
                schedule={str(h['threshold']):h['time'] for h in coarse['handoffs']}
                fine=run_case(task,1024,20260920,1/16,directory/'fine',start+args.budget,
                              coarse['final_time'],schedule)
                sensitivity=refinement(directory/'coarse',directory/'fine')
                selected='fine'
                extra=None
                if not sensitivity['passed'] and time.perf_counter() < start+args.budget:
                    extra=run_case(task,1024,20260920,1/32,directory/'refined',start+args.budget,
                                   coarse['final_time'],schedule)
                    sensitivity=refinement(directory/'fine',directory/'refined');selected='refined'
                result=dict(case=task['case'],selected=selected,refinement=sensitivity,
                            coarse=coarse,fine=fine,refined=extra)
                results.append(result)
                write_json(args.output/'results.json',dict(results=results,complete=False))
            write_json(args.output/'results.json',dict(results=results,complete=True,
                        wall_seconds=time.perf_counter()-start))
        except Exception as error:
            write_json(args.output/'failure.json',dict(type=type(error).__name__,message=str(error),
                         wall_seconds=time.perf_counter()-start,completed_cases=len(results)))
            raise


if __name__=='__main__':
    main()
