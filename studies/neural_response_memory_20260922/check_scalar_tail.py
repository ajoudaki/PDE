"""Bounded algebra checks only; no scientific training fits."""
import argparse
import hashlib
import json
from pathlib import Path
import pickle
import time

import numpy as np

from scalar_fourier_engine import canonical, field, node
from scalar_fourier_reference import PopulationReference, circle_inputs, initialize
from scalar_tail_engine import ScalarTailSystem, _InitialTreeJets


def generic_evaluator(pop, state, test):
    """Independent physical P1 velocities feed a contraction product rule."""
    values = pop.unpack(state)
    velocity = pop.unpack(pop.rhs(0., state))
    all_inputs = np.vstack((pop.inputs, test))
    responses = pop.query_fields(state, all_inputs)
    response_velocity = pop.query_field_velocity(state, all_inputs)
    fields = {}
    for layer in (1, 2, 3):
        for a in range(all_inputs.shape[0]):
            fields[field("h", layer, a)] = np.column_stack((responses["h" + str(layer)][:, a],
                                                             response_velocity["h" + str(layer)][:, a]))
    fields[field("c", 3)] = np.column_stack((values["c"], velocity["c"]))
    for layer in (2, 3):
        for kind in ("A", "B"):
            name = kind + str(layer)
            for a in range(pop.M):
                fields[field(kind, layer, a)] = np.column_stack((values[name][0, :, a], velocity[name][0, :, a]))
    return _InitialTreeJets(fields, pop.initialization.W20, pop.initialization.W30)


def contains(tree, sample):
    return (any(f[0] == "h" and f[2] == sample for f in tree[1])
            or any(contains(c, sample) for c in tree[2]))


def renamed(tree, source, target):
    def rooted(t):
        fs = [field(f[0], f[1], target if f[0] == "h" and f[2] == source else f[2])
              for f in t[1]]
        return node(t[0], fs, [rooted(c) for c in t[2]])
    return canonical(rooted(tree))


def run():
    started = time.process_time()
    U = circle_inputs([10., 125.], degrees=True).T
    test = circle_inputs([60.], degrees=True).T
    y = np.array([1., -1.])
    init = initialize(5)
    pop = PopulationReference(U.T, y, init, order=1)
    result = {}
    for mode in ("frozen", "tangent"):
        model = ScalarTailSystem(U, y, test, 3, mode=mode)
        z = model.initialize(init.w, init.W20, init.W30, init.c)
        actual = generic_evaluator(pop, pop.initial, test.T)
        live_jets = np.array([actual.tree(t) for t in model.training_patterns])
        rhs = model.rhs(0., z)
        checks = dict(initial_value_error=float(np.max(np.abs(z[:model.nscalar] - live_jets[:, 0]))),
                      initial_velocity_error=float(np.max(np.abs(rhs[:model.nscalar] - live_jets[:, 1]))),
                      output_error=float(np.max(np.abs(model.outputs(z) - pop.predict(pop.initial, np.vstack((U.T, test.T)))))))
        if mode == "tangent":
            r = model.training_output(z) - y
            drives = np.r_[r, np.linalg.norm(r) / np.sqrt(model.M)]
            boundary_jets = np.array([actual.tree(t) for t in model.boundary_patterns])
            checks["boundary_direction_error"] = float(np.max(np.abs(model.boundary_slopes @ drives - boundary_jets[:, 1])))
            epsilon = 1e-5
            velocity = pop.rhs(0., pop.initial)
            plus = generic_evaluator(pop, pop.initial + epsilon * velocity, test.T)
            minus = generic_evaluator(pop, pop.initial - epsilon * velocity, test.T)
            acceleration = np.array([(plus.tree(t)[1] - minus.tree(t)[1]) / (2 * epsilon)
                                     for t in model.training_patterns])
            scalar_acceleration = (model.rhs(0., z + epsilon * rhs) - model.rhs(0., z - epsilon * rhs)) / (2 * epsilon)
            checks["initial_acceleration_error"] = float(np.max(np.abs(scalar_acceleration[:model.nscalar] - acceleration)))
        train = np.array([not contains(t, model.M) for t in model.training_patterns])
        bound = np.array([contains(t, model.M) for t in model.boundary_patterns])
        flagged = np.r_[~train, bound, False]
        table = model.table
        forbidden = train[table["rows"]] & flagged[table["indices"]].any(axis=1)
        checks["training_reads_passive"] = bool(forbidden.any())
        altered = z.copy()
        altered[:model.nscalar][~train] += np.arange(np.sum(~train)) * .017 + .013
        checks["passive_feedback_error"] = float(np.max(np.abs(model.rhs(0., altered)[:model.nscalar][train] - rhs[:model.nscalar][train])))
        checks["clock_feedback_error"] = float(abs(model.rhs(0., altered)[model.length_index] - rhs[model.length_index]))
        stationary = z.copy()
        stationary[model.output_indices] = y
        checks["zero_residual_velocity"] = float(np.max(np.abs(model.rhs(0., stationary))))
        names = ("initialized", "mode", "M", "y", "output_indices", "all_output_indices", "length_index", "nscalar",
                 "dimension", "boundary_values", "boundary_slopes", "table")
        stripped = ScalarTailSystem.__new__(ScalarTailSystem)
        stripped.__dict__.update(pickle.loads(pickle.dumps({name: getattr(model, name) for name in names})))
        checks["scalar_only_restart_error"] = float(np.max(np.abs(stripped.rhs(17., z) - rhs)))
        checks["statistics"] = model.statistics()
        for key, value in checks.items():
            if key.endswith("error") or key == "zero_residual_velocity":
                gate = 2e-6 if key == "initial_acceleration_error" else 1e-10
                if value > gate:
                    raise AssertionError((mode, key, value, gate))
        if checks["training_reads_passive"]:
            raise AssertionError("Passive factor entered training row")
        result[mode] = checks
        if time.process_time() - started > 85.:
            raise TimeoutError("Algebra-check CPU budget reserve reached")
    # Duplicate input checks include arbitrarily perturbed consistent live states.
    duplicate = ScalarTailSystem(U, y, U[:, :1], 3, mode="tangent")
    z = duplicate.initialize(init.w, init.W20, init.W30, init.c)
    rng = np.random.default_rng(171)
    for i, tree in enumerate(duplicate.training_patterns):
        if not contains(tree, duplicate.M):
            z[i] += .001 * rng.normal()
    z[-duplicate.M:] = [.01, -.02]
    z[duplicate.length_index] = 1.03
    pairs = []
    for i, tree in enumerate(duplicate.training_patterns):
        if contains(tree, duplicate.M):
            target = duplicate.training_index[renamed(tree, duplicate.M, 0)]
            z[i] = z[target]
            pairs.append((i, target))
    rhs = duplicate.rhs(0., z)
    duplicate_error = max(abs(rhs[i] - rhs[j]) for i, j in pairs)
    if duplicate_error > 1e-10:
        raise AssertionError(("duplicate_input", duplicate_error))
    result["duplicate_input_error"] = float(duplicate_error)
    result["cpu_seconds"] = time.process_time() - started
    source = Path(__file__).resolve().parent
    result["source_sha256"] = {name: hashlib.sha256((source / name).read_bytes()).hexdigest()
                               for name in ("scalar_tail_engine.py", "check_scalar_tail.py",
                                            "scalar_fourier_engine.py", "scalar_fourier_reference.py")}
    result["passed"] = True
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    data = run()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps(data, indent=2))
