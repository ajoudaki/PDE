"""Deterministic check of the finite-q binary-label ascent coefficient."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import sys
import time

resource.setrlimit(resource.RLIMIT_CPU, (180, 180))
import numpy as np
import scipy
from scipy.integrate import solve_ivp

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--out', type=Path, required=True, help='Fresh generated-output directory')
run = parser.parse_args().out
run.mkdir(parents=True, exist_ok=False)
started = time.process_time()
labels = np.array([-1.0, 1.0, 1.0])
initial_h = np.array([0.75, 0.25, 0.25])
endpoint = 3 * np.pi * np.sqrt(3 / 5)
rows = []

for q in (1, 2, 4):
    modes = np.arange(q, dtype=float)
    weights = 2 * modes + 1
    triangular = np.diag(modes)
    for j in range(q):
        triangular[j, :j] = weights[:j]
    for epsilon in (0.02, 0.01):
        initial = np.zeros(5 + 2 * q)
        initial[:3] = np.arctanh(initial_h)
        initial[4] = 1
        initial[5] = initial_h.mean()
        for rtol, atol in ((1e-10, 1e-12), (1e-12, 1e-14)):
            errors = {"velocity": 0.0, "loss": 0.0}

            def quantities(state):
                u, w, tau = state[:3], state[3], state[4]
                forward = state[5:5+q]
                backward = state[5+q:]
                pairing = np.dot(weights * forward, backward)
                v = epsilon - 2 * pairing / tau
                h = np.tanh(u)
                h2 = np.tanh(v * h)
                gate = 1 - h2**2
                residual = w * h2 - labels
                rho = np.sqrt(np.mean(residual**2))
                hmean = h.mean()
                source = np.mean(residual * w * gate)
                du = -(2/3) * residual * v * w * gate * (1-h**2)
                dw = -2 * np.mean(residual * h2)
                dforward = rho * hmean - rho/tau * (triangular @ forward)
                dbackward = source - rho/tau * (triangular @ backward)
                vdot = (-2/tau * np.dot(
                    weights, dforward*backward + forward*dbackward
                ) + 2*rho/tau**2 * pairing)
                hstar = np.dot(weights, forward)/tau
                bstar = np.dot(weights, backward)/tau
                vdot_lowrank = -2 * (
                    source*hstar + rho*bstar*(hmean-hstar)
                )
                fvelocity = dw*h2 + w*gate*(
                    vdot*h + v*(1-h**2)*du
                )
                lossdot = 2*np.mean(residual*fvelocity)
                gradient_v = 2*np.mean(residual*w*gate*h)
                lossdot_blocks = -np.dot(du,du)-dw**2+gradient_v*vdot
                errors["velocity"] = max(
                    errors["velocity"], abs(vdot-vdot_lowrank)
                )
                errors["loss"] = max(
                    errors["loss"], abs(lossdot-lossdot_blocks)
                )
                velocity = np.concatenate((
                    du, [dw, rho], dforward, dbackward
                ))
                return velocity, lossdot, v, w, tau

            def rhs(t, state):
                return quantities(state)[0]

            solution = solve_ivp(
                rhs, (0, endpoint), initial, method="DOP853",
                rtol=rtol, atol=atol,
            )
            _, lossdot, v, w, tau = quantities(solution.y[:, -1])
            rows.append({
                "q": q, "epsilon": epsilon, "rtol": rtol, "atol": atol,
                "success": bool(solution.success), "message": solution.message,
                "nfev": int(solution.nfev), "loss_derivative": float(lossdot),
                "normalized": float(lossdot/(epsilon**2/36)),
                "v": float(v), "w": float(w), "tau": float(tau),
                "max_velocity_identity_error": errors["velocity"],
                "max_loss_identity_error": errors["loss"],
            })

fine = {(r["q"],r["epsilon"]):r for r in rows if r["rtol"] == 1e-12}
coarse = {(r["q"],r["epsilon"]):r for r in rows if r["rtol"] == 1e-10}
tolerance_change = max(
    abs(fine[k]["normalized"]-coarse[k]["normalized"]) for k in fine
)
valid = (
    all(r["success"] for r in rows)
    and tolerance_change < 1e-7
    and max(r["max_velocity_identity_error"] for r in rows) < 1e-10
    and max(r["max_loss_identity_error"] for r in rows) < 1e-10
)
contraction = {
    str(q): abs(fine[q,.01]["normalized"]-1)
        / max(abs(fine[q,.02]["normalized"]-1), np.finfo(float).tiny)
    for q in (1,2,4)
}
passed = valid and all(
    r["loss_derivative"] > 0 and abs(r["normalized"]-1) < .01
    for r in rows
) and all(
    abs(fine[q,.01]["normalized"]-1)
    <= .35*abs(fine[q,.02]["normalized"]-1)+1e-7
    for q in (1,2,4)
)
report = {
    "python": sys.version, "numpy": np.__version__,
    "scipy": scipy.__version__, "platform": platform.platform(),
    "cpu_threads": {
        k: os.environ.get(k) for k in (
            "OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS"
        )
    },
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "endpoint": float(endpoint), "rows": rows, "valid": bool(valid),
    "pass": bool(passed), "max_normalized_tolerance_change": float(tolerance_change),
    "deviation_contraction": contraction,
    "cpu_seconds": time.process_time()-started,
}
(run/"results.json").write_text(json.dumps(report, indent=2)+"\n")
print(json.dumps(report, indent=2))
if not passed:
    raise SystemExit(1)
