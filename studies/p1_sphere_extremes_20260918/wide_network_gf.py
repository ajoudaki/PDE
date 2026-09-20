"""Frozen quick diagnostic; see wide_network_gf_plan.md for scope and limits."""
import argparse
import contextlib
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import platform
import resource
import subprocess
import sys
import time

import numpy as np
import scipy

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "code"))
from pde import finite_network as ref

ANGLES = np.array([0, 2*np.pi/3, 4*np.pi/3,
                   np.pi/4, 3*np.pi/4, 5*np.pi/4, 7*np.pi/4])
U = np.vstack([np.ones(7), np.cos(ANGLES), np.sin(ANGLES)]) / np.sqrt(2)
X = np.sqrt(3) * U
LABELS = np.array([1., 1., 1., -1., -1., -1., -1.])
CHECKPOINTS = [.1, .2, .5, 1., 2., 5., 10., 20., 50., 100.,
               200., 500., 1000., 2000.]


def parameter(state):
    return ref.Parameters((state[0], state[1]), state[2])


def initial(width, seed):
    p = ref.initialize(width, 2, 3, seed=seed)
    return tuple(a.copy() for a in (p.weights[0], p.weights[1], p.readout))


def rhs(state):
    w, matrix, c = state
    n = len(c)
    z1 = w @ U
    h1 = np.tanh(z1)
    z2 = matrix @ h1
    h2 = np.tanh(z2)
    f = c @ h2 / n
    q = (f - LABELS) / 7
    weighted_back2 = (c[:, None] * ref.TANH.derivative(z2)) * q
    dw = -2 * ((matrix.T @ weighted_back2) * ref.TANH.derivative(z1)) @ U.T
    dm = (-2/n) * (weighted_back2 @ h1.T)
    dc = -2 * (h2 @ q)
    return (dw, dm, dc), (float(np.mean((f-LABELS)**2)), f, h1, h2)


def combine(state, step, terms):
    out = []
    for j, block in enumerate(state):
        v = block.copy()
        for coefficient, velocity in terms:
            v += (step*coefficient) * velocity[j]
        out.append(v)
    return tuple(out)


def physical_norms(state):
    n = len(state[2])
    return np.array([np.linalg.norm(state[0])/np.sqrt(n),
                     np.linalg.norm(state[1]),
                     np.linalg.norm(state[2])/np.sqrt(n)])


def compare_reference(state):
    fast, obs = rhs(state)
    p = parameter(state)
    reference = ref.flow_velocity(p, X, LABELS)
    blocks = (reference.weights[0], reference.weights[1], reference.readout)
    errors = []
    for a, b in zip(fast, blocks):
        np.testing.assert_allclose(a, b, rtol=5e-12, atol=1e-13)
        errors.append(float(np.max(np.abs(a-b))))
    np.testing.assert_allclose(obs[1], ref.forward(p, X).output,
                               rtol=5e-12, atol=1e-13)
    return errors


def unit_checks():
    state = initial(13, 918)
    init_errors = compare_reference(state)
    rng = np.random.default_rng(919)
    perturbed = (state[0]+.1*rng.standard_normal(state[0].shape),
                 state[1]+.03*rng.standard_normal(state[1].shape)/np.sqrt(13),
                 state[2]+.4*rng.standard_normal(state[2].shape))
    nonzero_errors = compare_reference(perturbed)
    velocity, obs = rhs(perturbed)
    speed = float(physical_norms(velocity) @ physical_norms(velocity))
    derivative_errors = []
    for eps in (1e-5, 1e-6):
        lp = ref.loss(parameter(combine(perturbed, eps, [(1., velocity)])), X, LABELS)
        lm = ref.loss(parameter(combine(perturbed, -eps, [(1., velocity)])), X, LABELS)
        error = abs((lp-lm)/(2*eps)+speed)/max(speed, 1e-12)
        assert error <= 1e-5, error
        derivative_errors.append(error)
    kernel_rate = 4/49 * ((obs[1]-LABELS) @ ref.kernel(parameter(perturbed), X)
                          @ (obs[1]-LABELS))
    np.testing.assert_allclose(speed, kernel_rate, rtol=1e-11, atol=1e-13)
    gram = U.T @ U
    assert np.max(np.abs(gram-np.eye(7))) < 1 - 1e-8
    return {"initial_rhs_max_errors": init_errors,
            "nontrivial_rhs_max_errors": nonzero_errors,
            "directional_relative_errors": derivative_errors,
            "metric_speed_squared": speed, "kernel_rate": float(kernel_rate)}


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False)+"\n")


def integrate(name, seed, rtol, atol, horizon, cap, output, global_start,
              stop_at_fit=True):
    begin = time.monotonic()
    deadline = min(begin+cap, global_start+230.)
    state = initial(1024, seed)
    start_state = tuple(x.copy() for x in state)
    k1, obs = rhs(state)
    start_h1, start_h2 = obs[2].copy(), obs[3].copy()
    h, t = .02, 0.
    accepted = rejected = error_rejected = increase_rejected = 0
    rows = []
    checkpoints = {}
    checkpoint_times = sorted(set([v for v in CHECKPOINTS if v <= horizon]+[horizon]))
    next_checkpoint = 0
    last_log = begin
    max_increase = 0.
    accepted_error_max = 0.
    start_loss = obs[0]

    def record():
        norms = physical_norms(k1)
        rows.append([t, obs[0], -float(norms @ norms), *obs[1].tolist()])

    record()
    checkpoints["0"] = obs[1].tolist()
    reason = "horizon"
    while t < horizon-1e-12:
        if time.monotonic() >= deadline:
            reason = "wall_time_cap"
            break
        if stop_at_fit and obs[0] <= 1e-6:
            reason = "loss_threshold"
            break
        while next_checkpoint < len(checkpoint_times) and checkpoint_times[next_checkpoint] <= t+1e-12:
            checkpoints[format(checkpoint_times[next_checkpoint], '.16g')] = obs[1].tolist()
            next_checkpoint += 1
        target = checkpoint_times[next_checkpoint] if next_checkpoint < len(checkpoint_times) else horizon
        step = min(h, target-t, horizon-t)
        if step <= 1e-12:
            reason = "step_underflow"
            break
        k2, _ = rhs(combine(state, step, [(.5, k1)]))
        k3, _ = rhs(combine(state, step, [(.75, k2)]))
        proposal = combine(state, step, [(2/9, k1), (1/3, k2), (4/9, k3)])
        k4, proposal_obs = rhs(proposal)
        error = tuple(step*(-5/72*a+1/12*b+1/9*c-1/8*d)
                      for a, b, c, d in zip(k1, k2, k3, k4))
        change = tuple(a-b for a, b in zip(proposal, start_state))
        scales = atol + rtol*np.maximum(1., physical_norms(change))
        err = float(np.max(physical_norms(error)/scales))
        increase = proposal_obs[0]-obs[0]
        finite = np.isfinite(err) and np.isfinite(proposal_obs[0])
        descent_ok = increase <= 1e-11*max(1., obs[0])
        if finite and err <= 1 and descent_ok:
            state, k1, obs = proposal, k4, proposal_obs
            t += step
            accepted += 1
            max_increase = max(max_increase, increase)
            accepted_error_max = max(accepted_error_max, err)
            record()
            if abs(t-target) <= 1e-10:
                checkpoints[format(target, '.16g')] = obs[1].tolist()
                next_checkpoint += 1
            h = min(1., step*min(5., max(.2, .9*max(err, 1e-16)**(-1/3))))
        else:
            rejected += 1
            error_rejected += int(not finite or err > 1)
            increase_rejected += int(not descent_ok)
            h = step*(.5 if not finite or not descent_ok else max(.1, min(.5, .9*err**(-1/3))))
        if time.monotonic()-last_log >= 10:
            print(json.dumps({"run": name, "time": t, "loss": obs[0],
                              "accepted": accepted, "rejected": rejected}), flush=True)
            last_log = time.monotonic()
    checkpoints[format(t, '.16g')] = obs[1].tolist()
    endpoint_rhs_errors = compare_reference(state)
    feature_motion = [float(np.sqrt(np.mean((obs[2]-start_h1)**2))),
                      float(np.sqrt(np.mean((obs[3]-start_h2)**2)))]
    displacement = physical_norms(tuple(a-b for a, b in zip(state, start_state))).tolist()
    threshold_times = {}
    for threshold in (48/49, 48/49-.01, .5, .1, .01, 1e-4, 1e-6):
        hits = [row[0] for row in rows if row[1] <= threshold]
        threshold_times[format(threshold, '.12g')] = hits[0] if hits else None
    with (output/(name+"_trajectory.csv")).open('w', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['time', 'loss', 'loss_derivative']+[f'prediction_{i}' for i in range(7)])
        writer.writerows(rows)
    np.savez(output/(name+"_final.npz"), w=state[0], matrix=state[1], c=state[2],
             X=X, y=LABELS, probabilities=np.full(7, 1/7))
    result = {"name": name, "width": 1024, "seed": seed,
              "rtol": rtol, "atol": atol, "physical_time": t,
              "wall_seconds": time.monotonic()-begin, "stop_reason": reason,
              "initial_loss": start_loss, "final_loss": obs[0],
              "final_loss_derivative": rows[-1][2], "predictions": obs[1].tolist(),
              "min_signed_margin": float(np.min(LABELS*obs[1])),
              "hidden_feature_rms_displacements": feature_motion,
              "physical_parameter_displacements": displacement,
              "accepted_steps": accepted, "rejected_steps": rejected,
              "error_rejections": error_rejected, "loss_increase_rejections": increase_rejected,
              "max_accepted_loss_increase": max_increase,
              "max_accepted_error_ratio": accepted_error_max,
              "endpoint_rhs_max_errors": endpoint_rhs_errors,
              "first_accepted_threshold_times": threshold_times,
              "checkpoints": checkpoints}
    write_json(output/(name+"_summary.json"), result)
    print(json.dumps({k: result[k] for k in ('name','physical_time','final_loss','stop_reason','wall_seconds')}), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=False)
    begin = time.monotonic()
    sources = [Path(__file__).resolve(), Path(__file__).with_name('wide_network_gf_plan.md'),
               ROOT/'code/pde/finite_network.py', ROOT/'docs/NOTATION.md']
    config = io.StringIO()
    with contextlib.redirect_stdout(config):
        np.show_config()
    manifest = {"source_sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                                   for p in sources},
                "HEAD": subprocess.check_output(['git','rev-parse','HEAD'], cwd=ROOT,text=True).strip(),
                "python": sys.version, "platform": platform.platform(),
                "numpy": np.__version__, "scipy": scipy.__version__, "dtype": "float64",
                "blas": config.getvalue(),
                "thread_environment": {k:os.environ.get(k) for k in
                                        ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
                "X": X.tolist(), "labels": LABELS.tolist(), "mass_per_input": 1/7,
                "constant_prediction_loss": 48/49, "total_cap_seconds": 240}
    write_json(output/'manifest.json', manifest)
    checks = unit_checks()
    write_json(output/'unit_checks.json', checks)
    print(json.dumps({"reference_checks": "passed", "output": str(output)}), flush=True)
    results = []
    results.append(integrate('main', 20260918, 2e-5, 2e-8, 2000., 85., output, begin))
    results.append(integrate('refinement', 20260918, 2e-6, 2e-9,
                             results[0]['physical_time'], 105., output, begin, stop_at_fit=False))
    a, b = results
    common = sorted(set(a['checkpoints']) & set(b['checkpoints']), key=float)
    differences = [float(np.max(np.abs(np.array(a['checkpoints'][k])-b['checkpoints'][k])))
                   for k in common]
    complete = abs(a['physical_time']-b['physical_time']) <= 1e-9
    loss_difference = abs(a['final_loss']-b['final_loss']) if complete else None
    validation = {"complete_matching_horizon": complete, "common_times": [float(k) for k in common],
                  "max_prediction_difference": max(differences, default=0.),
                  "final_loss_difference": loss_difference,
                  "passed": bool(complete and max(differences, default=np.inf)<=1e-3
                                 and loss_difference<=2e-5)}
    write_json(output/'refinement_check.json', validation)
    print(json.dumps({"refinement": validation}), flush=True)
    remaining = 230-(time.monotonic()-begin)
    if validation['passed'] and remaining >= 20:
        results.append(integrate('second_seed', 20260919, 2e-5, 2e-8, 2000.,
                                 min(45., remaining-5), output, begin))
    summary = {"runs": results, "refinement_validation": validation,
               "wall_seconds": time.monotonic()-begin,
               "peak_rss_mib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,
               "scope": "Finite wide networks only; no p=1 closure or infinite-time theorem."}
    write_json(output/'results.json', summary)
    print(json.dumps({"total_wall_seconds": summary['wall_seconds'],
                      "peak_rss_mib": summary['peak_rss_mib']}), flush=True)


if __name__ == '__main__':
    main()
