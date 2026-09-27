"""Independent, bounded algebra checks for the genuine tree aggregate ODE.

The oracle differentiates the original physical block variables w,c,A,B,L.
It does not use a population in the scalar RHS or train a population model.
Tiny finite blocks are used only to evaluate identities at one frozen state.
"""
from __future__ import annotations

import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_key, "1")

import argparse
import json
from pathlib import Path
import time

import numpy as np


def physical_oracle(u, queries, labels, G, physical, mark_bound=3.0,
                    local_overlaps=False):
    """Original block equations and their analytic chain rule, no compiler code."""
    w, c, A, B, L = physical
    q, k, _ = G.shape
    m, order = len(u), A.shape[1] // len(u)
    n = q * k
    nu = np.repeat(2 * np.arange(order) + 1, m)
    x = np.tanh(w @ queries.T)

    def action(field, transpose=False):
        mat = G.transpose(0, 2, 1) if transpose else G
        return (mat @ field.reshape(q, k, -1)).reshape(n, -1)

    def overlap(left, right):
        if local_overlaps:
            return np.einsum("qia,qib->qab", left.reshape(q, k, -1),
                             right.reshape(q, k, -1)) / k
        return left.T @ right / n

    def memory(left, overlaps):
        if local_overlaps:
            return np.einsum("qia,qab->qib", left.reshape(q, k, -1),
                             nu[None, :, None] * overlaps).reshape(n, -1)
        return left @ (nu[:, None] * overlaps)

    kappa = 2.0 / (m * L)
    S = overlap(B, x)
    h = np.tanh(action(x) - kappa * memory(A, S))
    f = c @ h / n
    residual = f[:m] - labels
    rho = np.linalg.norm(residual) / np.sqrt(m)
    delta = c[:, None] * (1.0 - h[:, :m] ** 2)
    J = action(delta, True) - kappa * memory(B, overlap(A, delta))
    dw = -2.0 / m * (((1.0 - x[:, :m] ** 2) * J * residual) @ u)
    dc = -2.0 / m * (h[:, :m] @ residual)

    def moment_velocity(moment, source):
        shaped = moment.reshape(n, order, m)
        j = np.arange(order)[None, :, None]
        weighted = (2 * j + 1) * shaped
        prefix = np.cumsum(weighted, axis=1) - weighted
        return (source[:, None, :] - rho / L *
                (j * shaped + prefix)).reshape(n, order * m)

    dA = moment_velocity(A, delta * residual)
    dB = moment_velocity(B, rho * x[:, :m])
    dx = (1.0 - x*x) * (dw @ queries.T)
    dS = overlap(dB, x) + overlap(B, dx)
    dh = (1.0 - h*h) * (action(dx) + kappa * rho / L * memory(A, S)
                        - kappa * (memory(dA, S) + memory(A, dS)))
    g, dg = 1.0 / L, -rho / (L*L)
    coords, velocities = {}, {}

    def add(name, value, velocity):
        coords[name] = np.asarray(value).reshape(q, k)
        velocities[name] = np.asarray(velocity).reshape(q, k)

    for a in range(len(queries)):
        add(("x", a), x[:, a], dx[:, a])
        add(("h", a), h[:, a], dh[:, a])
    add(("zeta",), c*g/2, (dc*g+c*dg)/2)
    for j in range(order):
        for b in range(m):
            col = j*m+b
            add(("alpha", j, b), A[:, col]*g*g/np.sqrt(m),
                (dA[:, col]*g*g+2*A[:, col]*g*dg)/np.sqrt(m))
            add(("beta", j, b), B[:, col]*g,
                dB[:, col]*g+B[:, col]*dg)
    return {"coordinates": coords, "velocity": velocities,
            "physical_velocity": (dw, dc, dA, dB, rho),
            "G_normalized": G/max(1.0, mark_bound), "g": g, "dg": dg,
            "prediction": f, "residual": residual, "rho": rho,
            "S": S, "dS": dS}


def tree_value_and_derivative(tree, colors, oracle):
    """Rooted message passing with an independent product-rule derivative."""
    matrix = oracle["G_normalized"]
    q, k, _ = matrix.shape

    def recurse(node):
        kind, decorations, children = node
        factors = [(oracle["coordinates"][colors[c]],
                    oracle["velocity"][colors[c]]) for c in decorations]
        mat = matrix if kind == 1 else matrix.transpose(0, 2, 1)
        for child in children:
            value, derivative = recurse(child)
            factors.append((np.einsum("qij,qj->qi", mat, value)/k,
                            np.einsum("qij,qj->qi", mat, derivative)/k))
        value, derivative = np.ones((q, k)), np.zeros((q, k))
        for factor, dfactor in factors:
            derivative = derivative*factor + value*dfactor
            value = value*factor
        return value, derivative

    value, derivative = recurse(tree)
    return float(value.mean()), float(derivative.mean())


def frozen_case(order=2):
    """Asymmetric q=k=m=2 state; none of the memory terms is forced to zero."""
    rng = np.random.default_rng(49071)
    u = np.array([[1.0, 0.0], [np.cos(.91), np.sin(.91)]])
    queries = np.vstack((u, [np.cos(1.73), np.sin(1.73)]))
    labels = np.array([.67, -.38])
    G = np.array([[[2.1, -.4], [.25, -.85]],
                  [[-.3, .73], [1.2, .17]]])
    w = rng.normal(scale=.7, size=(4, 2))
    c = np.array([.21, -.34, .47, .13])
    A = rng.normal(scale=.025, size=(4, order*2))
    B = rng.normal(scale=.22, size=(4, order*2))
    return u, queries, labels, G, (w, c, A, B, 1.3)


def displace(physical, tangent, epsilon):
    return tuple(x+epsilon*dx for x, dx in zip(physical, tangent))


def check_oracle():
    """Finite differences independently validate the analytic oracle itself."""
    u, queries, labels, G, physical = frozen_case()
    oracle = physical_oracle(u, queries, labels, G, physical)
    epsilon = 2e-6
    plus = physical_oracle(u, queries, labels, G,
                          displace(physical, oracle["physical_velocity"], epsilon))
    minus = physical_oracle(u, queries, labels, G,
                           displace(physical, oracle["physical_velocity"], -epsilon))
    errors = {str(key): float(np.max(np.abs(
        (plus["coordinates"][key]-minus["coordinates"][key])/(2*epsilon)
        - oracle["velocity"][key]))) for key in oracle["coordinates"]}
    crossblock = physical_oracle(u, queries, labels, G, physical,
                                local_overlaps=True)
    overlap_gap = max(float(np.max(np.abs(oracle["velocity"][key]
                        -crossblock["velocity"][key])))
                      for key in oracle["coordinates"])
    if max(errors.values()) > 2e-8:
        raise AssertionError(f"Independent physical chain rule: {errors}")
    if overlap_gap < 1e-5:
        raise AssertionError("Global-overlap test is degenerate")
    return {"chain_rule_max_error": max(errors.values()),
            "wrong_block_local_overlap_velocity_gap": overlap_gap,
            "per_color_error": errors}


def exact_fields(model, oracle):
    """Coefficient fields evaluated from independent physical derivatives."""
    coords, velocity = oracle["coordinates"], oracle["velocity"]
    fields = np.zeros(len(model.field_names))
    for i, name in enumerate(model.field_names):
        if name[0] == "R":
            fields[i] = oracle["g"]*oracle["residual"][name[1]]
        elif name[0] == "sigma":
            fields[i] = oracle["g"]*oracle["rho"]
        elif name[0] == "s":
            _, j, b, a = name
            fields[i] = np.mean(coords["beta", j, b]*coords["x", a])
        elif name[0] == "t":
            _, j, l, b = name
            fields[i] = np.mean(coords["alpha", j, l]*coords["zeta",]
                                *(1-coords["h", b]**2))
        elif name[0] == "D":
            _, j, b, a = name
            fields[i] = np.mean(velocity["beta", j, b]*coords["x", a]
                                +coords["beta", j, b]*velocity["x", a])
        elif name[0] == "C":
            fields[i] = float(model.queries[name[1]] @ model.u[name[2]])
        else:
            raise AssertionError(f"Unknown field {name}")
    return fields


def check_symbolic():
    """Check exact Lie derivatives and separately account for every omitted child."""
    from true_aggregate_ode import Closure, canonical, degree, node
    u, queries, labels, G, physical = frozen_case()
    model = Closure(u, labels, k=2, order=2, degree=9, mark_bound=3.,
                    queries=queries)
    oracle = physical_oracle(u, queries, labels, G, physical)
    fields = exact_fields(model, oracle)
    color_map = {i: oracle["coordinates"][name]
                 for i, name in enumerate(model.colors)}
    trees = [node(0 if name[0] in ("x", "beta") else 1, [i])
             for i, name in enumerate(model.colors)]
    trees += model.Ftrees + list(model.strees.values())
    trees += [tr for pair in model.ttrees.values() for tr in pair]
    # A repeated-branch tree and a two-edge tree check unrestricted index sums.
    trees += [node(0, [model.x[0]],
                   [node(1, [model.h[0], model.zeta])]*2),
              node(1, [model.zeta, model.h[2]],
                   [node(0, [model.x[1]], [node(1, [model.alpha[1, 0]])])])]
    trees = list(dict.fromkeys(canonical(tr) for tr in trees))
    derivatives = [model.derivative(tr) for tr in trees]
    children = list(dict.fromkeys(tr for terms in derivatives for _, _, tr in terms))
    child_values = dict(zip(children,
                            model.tree_values(children, color_map, G).mean(axis=1)))
    errors, contraction_errors, omitted_effects, ablation_effects = [], [], [], []
    zero_oracle = physical_oracle(u, queries, oracle["prediction"][:len(u)],
                                  G, physical)
    zero_fields = exact_fields(model, zero_oracle)
    zero_max = 0.0
    for tr, terms in zip(trees, derivatives):
        val, direct = tree_value_and_derivative(tr, model.colors, oracle)
        compiler_val = model.tree_values([tr], color_map, G).mean()
        contraction_errors.append(abs(val-compiler_val))
        symbolic = sum(c*model.coefficient(key, fields, physical[-1])
                       *child_values[child] for c, key, child in terms)
        retained = sum(c*model.coefficient(key, fields, physical[-1])
                       *child_values[child] for c, key, child in terms
                       if degree(child) <= model.cutoff)
        omitted = sum(c*model.coefficient(key, fields, physical[-1])
                      *child_values[child] for c, key, child in terms
                      if degree(child) > model.cutoff)
        errors.append(abs(symbolic-direct))
        errors.append(abs((direct-retained)-omitted))
        omitted_effects.append(abs(omitted))
        no_D = fields.copy()
        no_D[list(model.D.values())] = 0.
        ablated = sum(c*model.coefficient(key, no_D, physical[-1])
                      *child_values[child] for c, key, child in terms)
        ablation_effects.append(abs(symbolic-ablated))
        zero_max = max(zero_max, abs(sum(
            c*model.coefficient(key, zero_fields, physical[-1])*child_values[child]
            for c, key, child in terms)))
    D_error = 0.
    for key, terms in model.Dterms.items():
        derivative = sum(c*model.coefficient(coeff, fields, physical[-1])
                         *child_values[child] for c, coeff, child in terms)
        D_error = max(D_error, abs(derivative-fields[model.D[key]]))
    output_error = max(abs(2/ oracle["g"] * tree_value_and_derivative(
        tr, model.colors, oracle)[0] - oracle["prediction"][a])
        for a, tr in enumerate(model.Ftrees))
    if max(errors + contraction_errors + [D_error, output_error, zero_max]) > 2e-11:
        raise AssertionError({"symbolic": max(errors), "tree": max(contraction_errors),
                              "D": D_error, "output": output_error, "zero": zero_max})
    if max(ablation_effects) < 1e-6:
        raise AssertionError("dot-s omission test is degenerate")
    return {"tested_observables": len(trees), "distinct_derivative_children": len(children),
            "max_symbolic_chain_rule_error": max(errors),
            "max_tree_evaluation_error": max(contraction_errors),
            "global_overlap_derivative_field_error": D_error,
            "trained_readout_normalization_error": output_error,
            "zero_residual_max_derivative": zero_max,
            "degree9_omitted_child_max_effect": max(omitted_effects),
            "omitting_dot_s_max_effect": max(ablation_effects),
            "normalization": {"G_scale": model.Gscale, "k": model.k,
                              "L": physical[-1], "population_blocks": len(G)},
            "claim": "Pointwise exact symbolic identities; no hierarchy convergence claim"}


def check_packed(output=None):
    """Completed finite closure: coefficient fields, face direction, restart."""
    from true_aggregate_ode import Closure, degree
    u, _, labels, G, physical = frozen_case(order=1)
    u, labels = u[:1], labels[:1]
    w, c, A, B, L = physical
    physical = (w, c, A[:, :1], B[:, :1], L)
    oracle = physical_oracle(u, u, labels, G, physical)
    model = Closure(u, labels, k=2, order=1, degree=9, mark_bound=3.)
    model.compile(max_states=30000, max_terms=400000, seconds=8.)
    if not model.compiled:
        raise AssertionError(f"Bounded restart model did not compile: {model.report}")
    color_map = {i: oracle["coordinates"][name]
                 for i, name in enumerate(model.colors)}
    q = model.tree_values(model.trees, color_map, G).mean(axis=1)
    state = np.r_[q, L]
    fields = exact_fields(model, oracle)
    field_error = float(np.max(np.abs(model.fields(q, L)-fields)))
    packed = model.rhs(0., state)
    selected = np.unique(np.r_[np.arange(min(12, len(q))),
                              np.linspace(0, len(q)-1, 24, dtype=int)])
    errors, complete_rows = [], 0
    for index in selected:
        tr = model.trees[index]
        terms = model.derivative(tr)
        missing = [term for term in terms if degree(term[2]) > model.cutoff]
        values = (model.tree_values([t[2] for t in missing], color_map, G).mean(axis=1)
                  if missing else [])
        omission = sum(c*model.coefficient(key, fields, L)*v
                       for (c, key, _), v in zip(missing, values))
        direct = tree_value_and_derivative(tr, model.colors, oracle)[1]
        errors.append(abs(packed[index]-(direct-omission)))
        complete_rows += not bool(missing)
    output_error = float(np.max(np.abs(model.prediction(state)-oracle["prediction"])))
    clock_error = abs(packed[-1]-oracle["rho"])
    old_labels = model.labels.copy()
    model.labels[:] = model.prediction(state)
    zero_error = float(np.max(np.abs(model.rhs(0., state))))
    model.labels[:] = old_labels
    face_violations = {}
    for mode in ("row_envelope", "global"):
        model.penalty_mode = mode
        worst = -np.inf
        for signs in (np.ones(len(q)), -np.ones(len(q)),
                      np.where(np.arange(len(q)) % 2, 1., -1.)):
            face = np.r_[2*signs, 1.25]
            velocity = model.rhs(0., face)
            worst = max(worst, float(np.max(signs*velocity[:-1])))
        face_violations[mode] = max(0., worst)
    model.penalty_mode = "row_envelope"
    if max(errors+[field_error, output_error, clock_error, zero_error,
                   *face_violations.values()]) > 2e-10:
        raise AssertionError({"packed": max(errors), "fields": field_error,
                              "zero": zero_error, "faces": face_violations})

    # From this point, no population arrays are needed. Fixed RK4 makes the
    # restart comparison independent of adaptive solver step selection.
    del oracle, color_map, G, physical, w, c, A, B
    bad_arrays = {name: value.shape for name, value in vars(model).items()
                  if isinstance(value, np.ndarray) and value.ndim > 1
                  and name not in ("u", "queries")}
    if bad_arrays:
        raise AssertionError(f"Unexpected runtime population arrays: {bad_arrays}")

    def rk4(value, steps):
        value = value.copy()
        dt = 1e-4
        for _ in range(steps):
            k1 = model.rhs(0., value)
            k2 = model.rhs(0., value+dt*k1/2)
            k3 = model.rhs(0., value+dt*k2/2)
            k4 = model.rhs(0., value+dt*k3)
            value += dt*(k1+2*k2+2*k3+k4)/6
        return value

    original_rng = np.random.default_rng
    def forbidden_rng(*args, **kwargs):
        raise AssertionError("Scalar runtime attempted to construct samples")
    np.random.default_rng = forbidden_rng
    try:
        continuous = rk4(state, 6)
        checkpoint = rk4(state, 3)
        if output:
            output.mkdir(parents=True, exist_ok=True)
            np.save(output/"scalar_restart_state.npy", checkpoint)
            checkpoint = np.load(output/"scalar_restart_state.npy")
        else:
            checkpoint = np.asarray(json.loads(json.dumps(checkpoint.tolist())))
        restarted = rk4(checkpoint, 3)
    finally:
        np.random.default_rng = original_rng
    restart_error = float(np.max(np.abs(continuous-restarted)))
    if restart_error != 0. or not np.all(np.isfinite(restarted)):
        raise AssertionError(f"Finite scalar restart failure: {restart_error}")
    return {"compile": model.report, "tested_rhs_rows": len(selected),
            "tested_rows_with_no_boundary_children": complete_rows,
            "max_packed_rhs_error_after_exact_omission": max(errors),
            "coefficient_field_error": field_error,
            "prediction_normalization_error": output_error,
            "L_clock_error": clock_error, "zero_residual_rhs_error": zero_error,
            "box_face_outward_violation": face_violations,
            "restart_max_error": restart_error,
            "restart_state_shape": list(restarted.shape),
            "runtime_population_arrays": bad_arrays,
            "runtime_rng_construction_forbidden": True,
            "claim": "Finite scalar algebra/restart verification, not training accuracy"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    started = time.monotonic()
    results = {"oracle": check_oracle(), "symbolic": check_symbolic(),
               "packed": check_packed(args.output)}
    results["seconds"] = time.monotonic()-started
    if args.output:
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output/"validation.json").write_text(json.dumps(results, indent=2)+"\n")
    print(json.dumps(results, indent=2))
