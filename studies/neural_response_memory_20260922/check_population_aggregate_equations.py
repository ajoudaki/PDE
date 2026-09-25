"""Bounded algebra check of chronological population aggregate equations.

Frozen design: n=7, d=2, M=3, two passive queries, P=1,2,3; initialization
and one deterministic nonzero-history state per order. No ODE is integrated.
The nonzero states are admissible algebraic states, not claimed reachable.

The tested claim is algebraic equality of report equations and the implemented
order-P population-field RHS. The independent reference is autograd JVP of
an explicit tiny reconstructed-network map. Pass requires every normalized
max error <= 2e-11, with finite values. No adaptive configurations or reruns.
An algebra pass supports these identities only, not scalar finite closure,
accuracy of a population approximation, or any training-convergence claim.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys

import numpy as np
import torch

from deep_moment_engine import DeepMomentEngine


TOLERANCE = 2e-11


def columns(value):
    return value.permute(1, 0, 2).reshape(value.shape[1], -1)


def pairing(left, right):
    return left.T @ right / left.shape[0]


def explicit_fields(engine, queries, *values):
    """Differentiable diagnostic map; no engine factor or field helpers."""
    w, c, a2, b2, a3, b3, activity = values
    length = 1 + activity
    matrices = []
    for initial, a, b in ((engine.W20, a2, b2), (engine.W30, a3, b3)):
        learned = torch.zeros_like(initial)
        for k in range(engine.P):
            learned = learned - (2 * (2*k+1) / (engine.M*engine.n*length)) * (a[k] @ b[k].T)
        matrices.append(initial + learned)
    w2, w3 = matrices
    h1 = torch.tanh(w @ queries.T)
    h2 = torch.tanh(w2 @ h1)
    h3 = torch.tanh(w3 @ h2)
    delta3 = c[:, None] * (1-h3.square())
    delta2 = (1-h2.square()) * (w3.T @ delta3)
    delta1 = (1-h1.square()) * (w2.T @ delta2)
    output = c @ h3 / engine.n
    return h1, h2, h3, delta1, delta2, delta3, output, w2, w3


def scalar_fdot(aggregates):
    """Report equation (14), using scalar aggregate arrays exclusively."""
    q = aggregates
    result = (-2/q["M"]) * ((q["C3"] + q["G"]*q["R1"]) @ q["r"])
    for ell in (2, 3):
        result = result - (2/q["M"]) * (
            q[f"R{ell}"]*q[f"S{ell}"].T*q["r"][None, :]
            + q["rho"]*q[f"T{ell}"]*(q[f"C{ell-1}"]-q[f"S{ell}"].T)
        ).sum(dim=1)
    return result


def normalized_error(actual, expected):
    if not bool(torch.isfinite(actual).all() and torch.isfinite(expected).all()):
        return float("inf")
    return float((actual-expected).abs().max() / max(1., float(expected.abs().max())))


def one_case(order, nonzero):
    inputs = np.array([[1., 0.], [0.3, 0.9], [-0.7, 0.4]])
    labels = np.array([0.4, -0.8, 0.6])
    passive = np.array([[0.2, -0.6], [-0.9, -0.1]])
    engine = DeepMomentEngine(2, 7, order, inputs, labels, seed=20260925)
    queries = torch.as_tensor(np.concatenate((inputs, passive)), dtype=torch.float64)
    state = engine.initial_state()
    if nonzero:
        rng = np.random.default_rng(3100+order)
        for name in ("w", "c", "A2", "B2", "A3", "B3"):
            value = getattr(state, name)
            value.add_(torch.as_tensor(rng.normal(0., 0.17, size=value.shape), dtype=value.dtype))
        state.s.fill_(0.37)
    velocity = engine.rhs(state)
    fields, derivatives = torch.autograd.functional.jvp(
        lambda *values: explicit_fields(engine, queries, *values),
        state.tensors(), velocity.tensors(), create_graph=False, strict=False,
    )
    h = {ell: fields[ell-1] for ell in (1, 2, 3)}
    delta = {ell: fields[ell+2] for ell in (1, 2, 3)}
    dh = {ell: derivatives[ell-1] for ell in (1, 2, 3)}
    ddelta = {ell: derivatives[ell+2] for ell in (1, 2, 3)}
    output, fdot_jvp = fields[6], derivatives[6]
    training = engine.fields(state)
    residual, rho, length = output[:engine.M]-engine.labels, training["rho"], 1+state.s
    report = {}

    def check(name, actual, expected):
        report[name] = normalized_error(actual, expected)

    check("current_predictions", output, engine.predict(state, queries))
    for ell in (1, 2, 3):
        check(f"current_H{ell}", h[ell][:, :engine.M], training[f"h{ell}"])
        check(f"current_Delta{ell}", delta[ell][:, :engine.M], training[f"delta{ell}"])

    # Direct chain rule uses the engine's derivative factorization, providing
    # a separate check of that route against explicit-network autograd.
    dh_chain = {1: (1-h[1].square())*(velocity.w @ queries.T)}
    dmatrices = {}
    for ell in (2, 3):
        left, right = engine.derivative_factors(state, ell, velocity)
        dmatrices[ell] = left @ right.T
        dh_chain[ell] = (1-h[ell].square()) * (
            left @ (right.T @ h[ell-1]) + engine.apply_hidden(state, ell, dh_chain[ell-1])
        )
        check(f"W{ell}_derivative_JVP", dmatrices[ell], derivatives[ell+5])
        check(f"H{ell}_derivative_JVP", dh_chain[ell], dh[ell])
    fdot_chain = (velocity.c @ h[3] + state.c @ dh_chain[3])/engine.n
    check("fdot_direct_chain_JVP", fdot_chain, fdot_jvp)

    q = {"M": engine.M, "rho": rho, "r": residual,
         "G": queries @ engine.inputs.T}
    for ell in (1, 2, 3):
        q[f"C{ell}"] = pairing(h[ell], h[ell][:, :engine.M])
        q[f"R{ell}"] = pairing(delta[ell], delta[ell][:, :engine.M])

    idx = torch.arange(engine.M).repeat(order)
    rcols = residual[idx]
    legendre_transport = torch.zeros((order, order), dtype=torch.float64)
    for k in range(order):
        legendre_transport[k, k] = k
        for j in range(k):
            legendre_transport[k, j] = 2*j+1
    transport = torch.kron(legendre_transport, torch.eye(engine.M, dtype=torch.float64))
    a, b, da, db = {}, {}, {}, {}
    for ell in (2, 3):
        a[ell], b[ell] = (columns(getattr(state, prefix+str(ell))) for prefix in ("A", "B"))
        da[ell], db[ell] = (columns(getattr(velocity, prefix+str(ell))) for prefix in ("A", "B"))
        abar, bbar = engine.endpoint_projections(state, ell)
        q[f"T{ell}"] = pairing(delta[ell], abar)
        q[f"S{ell}"] = pairing(bbar, h[ell-1])
        endpoint_dot = (-2/(engine.M*engine.n)) * (
            (delta[ell][:, :engine.M]*residual) @ bbar.T
            + rho*abar @ (h[ell-1][:, :engine.M]-bbar).T
        )
        check(f"W{ell}_endpoint_velocity", endpoint_dot, dmatrices[ell])

        x, y = pairing(a[ell], a[ell]), pairing(b[ell], b[ell])
        d = pairing(delta[ell], a[ell])
        v = pairing(b[ell], h[ell-1])
        xsource = rcols[:, None]*d[idx]
        ysource = rho*v[:, idx].T
        xdot_scalar = xsource+xsource.T-(rho/length)*(transport @ x+x @ transport.T)
        ydot_scalar = ysource+ysource.T-(rho/length)*(transport @ y+y @ transport.T)
        check(f"A{ell}_Gram_velocity", xdot_scalar, pairing(da[ell], a[ell])+pairing(a[ell], da[ell]))
        check(f"B{ell}_Gram_velocity", ydot_scalar, pairing(db[ell], b[ell])+pairing(b[ell], db[ell]))
        ddot_scalar = pairing(ddelta[ell], a[ell]) + q[f"R{ell}"][:, idx]*rcols - (rho/length)*(d @ transport.T)
        vdot_scalar = rho*q[f"C{ell-1}"][:, idx].T - (rho/length)*(transport @ v) + pairing(b[ell], dh[ell-1])
        check(f"D{ell}_mixed_velocity", ddot_scalar, pairing(ddelta[ell], a[ell])+pairing(delta[ell], da[ell]))
        check(f"V{ell}_mixed_velocity", vdot_scalar, pairing(db[ell], h[ell-1])+pairing(b[ell], dh[ell-1]))

        weights = engine.weights.repeat_interleave(engine.M)
        gram_norm_sq = (4/(engine.M**2*length**2))*(x*y*weights[:, None]*weights[None, :]).sum()
        learned = engine.reconstruct_delta_for_diagnostics(state, ell)
        check(f"W{ell}_learned_Gram_norm", gram_norm_sq, learned.square().sum())

    fdot_scalar = scalar_fdot(q)
    check("fdot_train_scalar_JVP", fdot_scalar[:engine.M], fdot_jvp[:engine.M])
    check("fdot_query_scalar_JVP", fdot_scalar[engine.M:], fdot_jvp[engine.M:])
    check("fdot_scalar_direct_chain", fdot_scalar, fdot_chain)

    cross = pairing(a[2], b[3])
    cross_scalar = (rcols[:, None]*pairing(delta[2][:, :engine.M], b[3])[idx]
                    + rho*pairing(a[2], h[2][:, :engine.M])[:, idx]
                    - (rho/length)*(transport @ cross+cross @ transport.T))
    check("A2_B3_cross_Gram_velocity", cross_scalar, pairing(da[2], b[3])+pairing(a[2], db[3]))

    # Equation (16): gate-weighted fourth moment in the lower mixed velocity.
    gated_lower = torch.empty((order*engine.M, len(queries)), dtype=torch.float64)
    for query in range(len(queries)):
        gated = pairing(b[2], (1-h[1][:, query, None].square())*delta[1][:, :engine.M])
        gated_lower[:, query] = (-2/engine.M)*(gated*(residual*q["G"][query])[None, :]).sum(dim=1)
    check("B2_H1dot_gated_statistic", gated_lower, pairing(b[2], dh[1]))

    # Equations (17)--(19): keep the same initialized W20 in the gated term.
    z2dot = engine.W20 @ dh[1]
    weighted_a2 = columns(engine.weights[:, None, None]*state.A2)
    z2dot = z2dot - (2/(engine.M*length))*weighted_a2 @ gated_lower
    abar2, _ = engine.endpoint_projections(state, 2)
    z2dot = z2dot - (2/engine.M)*(
        (delta[2][:, :engine.M]*residual) @ q["S2"]
        + rho*abar2 @ (q["C1"].T-q["S2"])
    )
    check("B3_H2dot_operator_gated_statistic", pairing(b[3], (1-h[2].square())*z2dot), pairing(b[3], dh[2]))

    # Full backward derivative recurrence (20)--(21), including actual adjoints.
    backward = {3: velocity.c[:, None]*(1-h[3].square()) - 2*state.c[:, None]*h[3]*dh[3]}
    for ell in (2, 1):
        backward[ell] = (
            -2*h[ell]*dh[ell]*engine.apply_hidden(state, ell+1, delta[ell+1], transpose=True)
            + (1-h[ell].square())*(dmatrices[ell+1].T @ delta[ell+1]
                                    + engine.apply_hidden(state, ell+1, backward[ell+1], transpose=True))
        )
    for ell in (1, 2, 3):
        check(f"Delta{ell}_derivative_JVP", backward[ell], ddelta[ell])

    return {"order": order, "state": "nonzero_history" if nonzero else "initial",
            "rho": float(rho), "history_length": float(length),
            "max_normalized_error": max(report.values()),
            "passed": all(value <= TOLERANCE for value in report.values()),
            "errors": report}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    default_output = Path(__file__).resolve().parents[2] / "data/generated/neural_response_memory_20260922/population_aggregate_algebra01"
    parser.add_argument("--output", type=Path, default=default_output)
    args = parser.parse_args()
    torch.set_num_threads(1)
    cases = [one_case(order, nonzero) for order in (1, 2, 3) for nonzero in (False, True)]
    source_dir = Path(__file__).resolve().parent
    hashes = {name: hashlib.sha256((source_dir/name).read_bytes()).hexdigest() for name in
              (Path(__file__).name, "deep_moment_engine.py", "moment_engine.py", "POPULATION_AGGREGATE_EQUATIONS_CHECK.md")}
    result = {"scope": "deterministic algebra check, no training integration or population experiment",
              "width": 7, "input_dimension": 2, "training_samples": 3, "passive_queries": 2,
              "orders": [1, 2, 3], "tolerance": TOLERANCE, "cases": cases,
              "passed": all(case["passed"] for case in cases),
              "max_normalized_error": max(case["max_normalized_error"] for case in cases),
              "source_sha256": hashes, "python": platform.python_version(),
              "numpy": np.__version__, "torch": torch.__version__,
              "command": [sys.executable, *sys.argv]}
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output/"results.json").write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    print(json.dumps({key: result[key] for key in ("passed", "max_normalized_error", "tolerance")}, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
