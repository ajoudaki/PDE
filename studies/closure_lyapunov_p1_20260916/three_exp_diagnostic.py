"""Bounded diagnostic specified in three_exp_contract.md; not a proof."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import time

import numpy as np
import scipy
from scipy.integrate import solve_ivp

from pde.observable_solver import DataLaw, initialize, rhs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=False)
    started = time.process_time()
    records = []
    traces = {}
    states = {}
    angles = [(0.1, 1.4, 0.75), (0.15, 2.5, 4.3),
              (0.0, np.pi - 0.2, np.pi + 0.4)]
    labels = np.array([1.0, 1.0, -1.0])
    source_paths = [Path(__file__), Path(__file__).with_name("three_exp_contract.md")]
    source_paths += sorted(Path("code/pde").glob("observable_*.py"))
    metadata = {
        "scope": "finite deterministic quadrature diagnostic, not population proof",
        "python": platform.python_version(), "numpy": np.__version__,
        "scipy": scipy.__version__, "angles": angles, "labels": labels.tolist(),
        "source_hashes": {str(p): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in source_paths},
        "threads": {k: os.environ.get(k) for k in
                    ["OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"]},
    }

    def check_budget():
        if time.process_time() - started > 180:
            raise RuntimeError("predeclared cumulative CPU budget exceeded")
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 1024 ** 2:
            raise RuntimeError("predeclared 1 GiB RSS safety cap exceeded")

    def run(case, refinement, tight=False):
        check_budget()
        if refinement not in states:
            q, p = [(2048, 512), (4096, 1024)][refinement]
            states[refinement] = initialize(1, initialization_nodes=q, population_nodes=p)
            s = states[refinement]
            np.savez(output / f"initial_{refinement}.npz",
                     **{k: getattr(s, k) for k in
                        ["b1", "b2", "p1", "p2", "g", "w", "c", "M", "D"]})
        state = states[refinement]
        u = np.column_stack([np.cos(angles[case]), np.sin(angles[case])])
        law = DataLaw(u, labels, np.ones(3)/3).validate(state.arithmetic)
        n1, n2 = len(state.w), len(state.c)
        split = 2*n1 + n2
        x0 = np.concatenate([state.w.ravel(), state.c, state.M.ravel()])
        b1p = state.b1.T * state.p1
        b2p = state.b2.T * state.p2
        evaluations = 0

        def unpack(x):
            return x[:2*n1].reshape(n1, 2), x[2*n1:split], x[split:].reshape(state.M.shape)

        def fields(x):
            w, c, mat = unpack(x)
            h = np.tanh(w @ u.T)
            a = b1p @ h
            upper = np.tanh(state.b2 @ (mat @ a))
            f = (state.p2*c) @ upper
            d = b2p @ (c[:, None]*(1-upper*upper))
            reverse = state.b1 @ (mat.T @ d)
            return h, a, upper, f, d, reverse

        def velocity(t, x):
            nonlocal evaluations
            evaluations += 1
            if evaluations > 250000:
                raise RuntimeError("predeclared per-integration RHS limit exceeded")
            check_budget()
            h, a, upper, f, d, reverse = fields(x)
            r = (f-labels)/3
            vw = -2*((1-h*h)*reverse*r) @ u
            vc = -2*upper @ r
            vm = -2*(d*r) @ a.T
            return np.concatenate([vw.ravel(), vc, vm.ravel()])

        # Independent maintained producer comparison at init and an explicit
        # deterministic nonzero-readout perturbation; no trajectory tuning.
        oracle_errors = []
        for probe in (x0, x0+0.001*np.sin(np.arange(len(x0)))):
            w, c, mat = unpack(probe)
            expected = np.concatenate([v.ravel() for v in
                                       rhs(state.dynamic_copy(w, c, mat), law)])
            got = velocity(0.0, probe)
            error = float(np.max(np.abs(expected-got)))
            oracle_errors.append(error)
            assert error < 1e-12

        initial_upper = fields(x0)[2]
        initial_contrast = initial_upper @ labels/3
        c0 = float(np.sum(state.p2*initial_contrast**2))

        def event(t, x):
            f = fields(x)[3]
            return np.mean((f-labels)**2)-1e-8
        event.terminal = True
        event.direction = -1
        before = time.process_time()
        sol = solve_ivp(velocity, (0.0, 400.0), x0, method="DOP853",
                        rtol=1e-10 if tight else 1e-8,
                        atol=1e-12 if tight else 1e-10,
                        events=event, dense_output=True)
        if not sol.success:
            raise RuntimeError(sol.message)
        times = np.unique(np.r_[np.arange(401)[np.arange(401) <= sol.t[-1]], sol.t[-1]])
        rows = []
        for t in times:
            check_budget()
            x = sol.sol(t)
            w, c, mat = unpack(x)
            h, a, upper, f, d, reverse = fields(x)
            r = f-labels
            gram = upper.T @ (state.p2[:, None]*upper)
            lower = (1-h*h)*reverse
            kernel = gram + (lower.T @ (state.p1[:, None]*lower))*(u @ u.T)
            kernel += (d.T @ d)*(a.T @ a)
            fdot = -2*kernel @ r/3
            loss = float(np.mean(r*r))
            cnorm2 = float(np.sum(state.p2*c*c))
            fmargin = float(labels @ f/3)
            fdotmargin = float(labels @ fdot/3)
            qdot = float(-4*r @ f/3)
            den = c0+fmargin*fmargin
            phi = (1+cnorm2)/den
            phidot = (qdot*den-(1+cnorm2)*2*fmargin*fdotmargin)/(den*den)
            curvature = float(r @ kernel @ r/(9*loss)) if loss > 0 else np.nan
            vw, vc, vm = unpack(velocity(t, x))
            speed2 = np.sum(state.p1[:, None]*vw*vw)+np.sum(state.p2*vc*vc)+np.sum(vm*vm)
            energy_error = float(abs(speed2-4*r @ kernel @ r/9))
            rows.append([t, loss, cnorm2, phi, phidot, curvature,
                         np.linalg.eigvalsh(gram/3)[0], energy_error, *f])
        panel = np.asarray(rows)
        tag = f"case{case}_q{refinement}"+("_tight" if tight else "")
        np.savez(output / (tag+".npz"), panel=panel, final_state=sol.y[:, -1])
        result = {"tag": tag, "case": case, "refinement": refinement, "tight": tight,
                  "columns": ["time", "loss", "c_norm_squared", "phi", "phi_dot",
                              "residual_curvature", "readout_gram_min", "energy_error",
                              "prediction_1", "prediction_2", "prediction_3"],
                  "endpoint": float(sol.t[-1]), "final_loss": float(panel[-1, 1]),
                  "initial_contrast": c0, "initial_phi": float(panel[0, 3]),
                  "max_phi_dot": float(np.max(panel[:, 4])),
                  "max_phi_dot_time": float(panel[np.argmax(panel[:, 4]), 0]),
                  "min_curvature": float(np.min(panel[:, 5])),
                  "initial_curvature": float(panel[0, 5]),
                  "max_readout_norm": float(np.sqrt(np.max(panel[:, 2]))),
                  "oracle_rhs_errors": oracle_errors,
                  "max_energy_error": float(np.max(panel[:, 7])),
                  "rhs_evaluations": evaluations,
                  "cpu_seconds": time.process_time()-before,
                  "state_metadata": state.metadata}
        records.append(result)
        traces[tag] = panel
        (output / "records.json").write_text(json.dumps({**metadata, "runs": records}, indent=2))
        print(json.dumps({k: result[k] for k in
                          ["tag", "endpoint", "final_loss", "max_phi_dot",
                           "max_phi_dot_time", "max_readout_norm", "cpu_seconds"]}), flush=True)
        return result

    try:
        for case in range(3):
            for refinement in range(2):
                run(case, refinement)
        candidate = 0
        for case in range(3):
            left, right = traces[f"case{case}_q0"], traces[f"case{case}_q1"]
            count = min(len(left)-1, len(right)-1)
            threshold = 1e-4*max(1.0, left[0, 3])
            if np.any((left[:count, 4] > threshold) & (right[:count, 4] > threshold)):
                candidate = case
                break
        run(candidate, 0, tight=True)
        baseline = traces[f"case{candidate}_q0"]
        refined = traces[f"case{candidate}_q1"]
        tight = traces[f"case{candidate}_q0_tight"]
        count = min(len(baseline)-1, len(refined)-1, len(tight)-1)
        assert np.array_equal(baseline[:count, 0], refined[:count, 0])
        assert np.array_equal(baseline[:count, 0], tight[:count, 0])
        pred_error = float(np.max(np.abs(baseline[:count, 8:]-refined[:count, 8:])))
        time_error = np.abs(baseline[:count, 4]-tight[:count, 4])
        threshold = 1e-4*max(1.0, baseline[0, 3])
        valid = (baseline[:count, 4] > threshold) & (refined[:count, 4] > threshold)
        valid &= baseline[:count, 4] > 100*time_error
        conclusion = "violation" if np.any(valid) and pred_error <= 0.02 else (
            "no_resolved_violation" if pred_error <= 0.02 else "inconclusive_population_refinement")
        metadata["comparison"] = {"case": candidate, "prediction_refinement_error": pred_error,
                                  "max_phi_dot_time_error": float(np.max(time_error)),
                                  "conclusion": conclusion,
                                  "witness_times": baseline[:count, 0][valid].tolist()}
        metadata["status"] = "complete"
    except Exception as exc:
        metadata["status"] = "stopped"
        metadata["error"] = repr(exc)
    metadata["cpu_seconds"] = time.process_time()-started
    metadata["peak_rss_kib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    metadata["output_hashes"] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                 for p in output.glob("*.npz")}
    (output / "records.json").write_text(json.dumps({**metadata, "runs": records}, indent=2))
    print(json.dumps({k: metadata[k] for k in ["status", "cpu_seconds", "peak_rss_kib"]}), flush=True)


if __name__ == "__main__":
    main()
