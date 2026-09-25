"""Independent bounded checks for ordered high-order scalar implementations.

Only tiny deterministic CPU fixtures are integrated. Research GPU and scalar
trajectories are producer-owned and must be audited from saved evidence.
"""

import argparse
import json
from pathlib import Path
import re
import time

import numpy as np
from scipy.integrate import BDF, solve_ivp

from check_scalar_long_time import Audit, digest, load_npz
from check_scalar_wide import array_hash


HERE = Path(__file__).resolve().parent
DATA = HERE.parents[1]/"data/generated/neural_response_memory_20260922"


def split(state, m, order, signatures=True):
    tensors, history, start = {}, {}, 0
    for j in range(1, order):
        size = m**j
        tensors[j] = state[start:start+size].reshape((m,)*j)
        start += size
    if signatures:
        for k in range(1, order):
            size = m**k
            history[k] = state[start:start+size].reshape((m,)*k)
            start += size
    assert start == len(state)
    return tensors, history


def reference_rhs(state, labels, terminal, order, signatures=True):
    m = len(labels)
    tensors, history = split(state, m, order, signatures)
    tensors[order] = terminal
    velocity = -2/m*(tensors[1]-labels)
    pieces = [(tensors[j+1].reshape(m**j, m) @ velocity).reshape(-1)
              for j in range(1, order)]
    if signatures:
        pieces += [(velocity[:, None]*np.asarray(history.get(k-1, 1)).reshape(1, -1)).reshape(-1)
                   for k in range(1, order)]
    return np.concatenate(pieces)


def reference_transport(coefficients, signatures):
    """Explicit scalar index sums, independent of production contractions."""
    order = len(coefficients)
    m = len(signatures["sigma1"])
    q = len(coefficients["T1"])
    result = {}
    for j in range(1, order+1):
        target = np.array(coefficients["T"+str(j)], dtype=np.longdouble, copy=True)
        for prefix in np.ndindex((q,)+(m,)*(j-1)):
            for k in range(1, order-j+1):
                for word in np.ndindex((m,)*k):
                    target[prefix] += (np.longdouble(coefficients["T"+str(j+k)][prefix+word])
                                       * np.longdouble(signatures["sigma"+str(k)][word]))
        result["T"+str(j)] = target
    return result


def engine_checks(audit):
    from scalar_high_order_engine import ScalarHierarchy, StructuredBDF, recenter_coefficients
    from scalar_long_time_engine import StiffSignatureHierarchy

    rng = np.random.default_rng(30971)
    audit.check("structured BDF inherits original step implementation", StructuredBDF._step_impl is BDF._step_impl)
    for order in range(2, 7):
        m = 2
        coeff = {"T"+str(j): rng.normal(size=(m,)*j)*.15 for j in range(1, order+1)}
        labels = rng.normal(size=m)*.2
        for signatures in (False, True):
            model = ScalarHierarchy(coeff, labels, order, with_signatures=signatures)
            state = model.initial_state()+rng.normal(size=model.size)*.03
            prefix = f"P{order} signatures{signatures}"
            reference = lambda value:reference_rhs(value, labels, coeff["T"+str(order)], order, signatures)
            audit.close(prefix+" independent ordered RHS", model.rhs(0, state), reference(state), 2e-15, 2e-14)
            jacobian = np.column_stack([reference(state.astype(complex)+1e-30j*np.eye(model.size)[i]).imag/1e-30
                                       for i in range(model.size)])
            audit.close(prefix+" complex-step full Jacobian", model.jac(0, state).toarray(), jacobian, 2e-14, 2e-13)
            snapshot = model.linearize(state)
            original_state = state.copy()
            state += rng.normal(size=model.size)
            model.linearize(state)
            for gamma in (.001, .17, 1.4):
                factor = snapshot.factor(gamma)
                rhs = rng.normal(size=(model.size, 3))
                actual = factor.solve(rhs)
                expected = np.linalg.solve(np.eye(model.size)-gamma*jacobian, rhs)
                audit.close(prefix+f" stale-snapshot full solve gamma{gamma}", actual, expected, 2e-12, 2e-12)
                audit.close(prefix+f" backward linear residual gamma{gamma}",
                            (np.eye(model.size)-gamma*jacobian)@actual, rhs, 2e-12, 2e-12)
                complex_rhs = rhs[:, 0]+1j*rhs[:, 1]
                audit.close(prefix+f" complex forcing gamma{gamma}", factor.solve(complex_rhs),
                            np.linalg.solve(np.eye(model.size)-gamma*jacobian, complex_rhs), 2e-12, 2e-12)
            audit.close(prefix+" snapshot velocity immutable", snapshot.velocity,
                        -2/m*(original_state[:m]-labels), 0, 0)
            audit.check(prefix+" snapshot arrays readonly", not snapshot.velocity.flags.writeable
                        and all(not x.flags.writeable for x in snapshot.tensors.values())
                        and all(not x.flags.writeable for x in snapshot.signatures.values()))
            if signatures:
                reset = model.reset_signatures(state)
                audit.close(prefix+" reset preserves training exactly", reset[:model.training_size],
                            state[:model.training_size], 0, 0)
                audit.close(prefix+" reset zeros signatures", reset[model.training_size:], 0, 0, 0)
                perturb = state.copy()
                perturb[model.training_size:] += 100*rng.normal(size=model.size-model.training_size)
                audit.close(prefix+" no passive feedback", model.rhs(0, state)[:model.training_size],
                            model.rhs(0, perturb)[:model.training_size], 0, 0)
            if order == 4 and signatures:
                old = StiffSignatureHierarchy(dict(zip(("f", "Theta", "C", "Q"),
                                                      (coeff["T"+str(j)] for j in range(1, 5)))), labels)
                audit.close("generic P4 equals old RHS", model.rhs(0, state), old.rhs(0, state), 2e-15, 2e-14)
                audit.close("generic P4 equals old Jacobian", model.jac(0, state).toarray(),
                            old.jac(0, state).toarray(), 2e-15, 2e-14)

        # Exercise actual inherited BDF step/cache lifecycle on a tiny fixture.
        model = ScalarHierarchy(coeff, labels, order)
        custom = StructuredBDF(model, 0, model.initial_state(), .4, rtol=2e-9, atol=2e-11)
        while custom.status == "running":
            custom.step()
        conventional = solve_ivp(model.rhs, (0, .4), model.initial_state(), method="BDF",
                                 jac=model.jac, rtol=2e-9, atol=2e-11)
        independent = solve_ivp(lambda t, s:reference_rhs(s, labels, coeff["T"+str(order)], order),
                                (0, .4), model.initial_state(), method="DOP853", rtol=2e-12, atol=2e-14)
        audit.check(f"P{order} structured BDF finishes", custom.status == "finished")
        audit.close(f"P{order} structured vs ordinary BDF", custom.y, conventional.y[:, -1], 2e-11, 2e-10)
        audit.close(f"P{order} structured vs independent explicit fixture", custom.y,
                    independent.y[:, -1], 2e-8, 2e-8)

        passive = {"T"+str(j):rng.normal(size=(3,)+(m,)*(j-1)) for j in range(1, order+1)}
        sig = {"sigma"+str(k):rng.normal(size=(m,)*k)*.1 for k in range(1, order)}
        old = {name:value.copy() for name, value in passive.items()}
        moved = recenter_coefficients(passive, sig)
        expected = reference_transport(passive, sig)
        blocked = vectorized_transport(passive, {k:sig["sigma"+str(k)] for k in range(1, order)}, query_chunk=2)
        for name in passive:
            audit.close(f"P{order} explicit-index old-anchor transport {name}", moved[name], expected[name], 2e-16, 2e-16)
            audit.close(f"P{order} bounded audit replay vs explicit sums {name}", blocked[name], expected[name], 2e-16, 2e-16)
            audit.close(f"P{order} immutable old passive {name}", passive[name], old[name], 0, 0)
        audit.check(f"P{order} terminal object preserved", moved["T"+str(order)] is passive["T"+str(order)])

        # Driven noncommuting path: independently integrate the full passive
        # chain and local signatures, then compare two transported segments.
        initial = np.concatenate([passive["T"+str(j)].reshape(-1) for j in range(1, order)])
        sizes = [3*m**(j-1) for j in range(1, order)]
        breaks = np.cumsum([0]+sizes)
        signature_size = sum(m**k for k in range(1, order))
        anchor = passive
        direct = initial
        for begin, end in ((0., .19), (.19, .57)):
            def driven(time_value, state):
                velocity = np.array([.7+time_value, -.2+time_value*time_value])
                blocks = [state[breaks[j-1]:breaks[j]].reshape((3,)+(m,)*(j-1))
                          for j in range(1, order)]
                blocks.append(passive["T"+str(order)])
                output = [(blocks[j].reshape(-1, m)@velocity).reshape(-1) for j in range(1, order)]
                start, previous = len(initial), np.array(1.)
                for k in range(1, order):
                    output.append(np.outer(velocity, previous).reshape(-1))
                    previous = state[start:start+m**k]
                    start += m**k
                return np.concatenate(output)
            sol = solve_ivp(driven, (begin, end), np.r_[direct, np.zeros(signature_size)],
                            method="DOP853", rtol=2e-12, atol=2e-14)
            direct = sol.y[:len(initial), -1]
            start, local = len(initial), {}
            for k in range(1, order):
                local["sigma"+str(k)] = sol.y[start:start+m**k, -1].reshape((m,)*k)
                start += m**k
            anchor = recenter_coefficients(anchor, local)
            transported = np.concatenate([anchor["T"+str(j)].reshape(-1) for j in range(1, order)])
            audit.close(f"P{order} multisegment forced passive endpoint {end}", transported,
                        direct, 2e-11, 2e-11)

    # The actual M=8 P6 state has 74,896 entries; sample directions avoid a
    # quadratic dense Jacobian allocation while checking its exact sparse map.
    m, order = 8, 6
    coeff = {"T"+str(j):rng.normal(size=(m,)*j)*.01 for j in range(1, order+1)}
    labels = rng.normal(size=m)
    model = ScalarHierarchy(coeff, labels, order)
    state = model.initial_state()+rng.normal(size=model.size)*.01
    direction = rng.normal(size=model.size)
    derivative = reference_rhs(state.astype(complex)+1e-30j*direction, labels, coeff["T6"], 6).imag/1e-30
    audit.close("M8 P6 sparse directional Jacobian", model.jac(0, state)@direction, derivative, 2e-13, 2e-12)
    rhs = rng.normal(size=model.size)
    delta = model.linearize(state).factor(.13).solve(rhs)
    audit.close("M8 P6 structured backward residual", delta-.13*(model.jac(0, state)@delta), rhs, 2e-12, 2e-12)


def initializer_checks(audit):
    import torch
    import scalar_aggregate_engine as legacy
    import scalar_circle_probe_engine as old_probe
    import scalar_high_order_initialization as production
    import scalar_high_order_oracle as oracle

    torch.set_num_threads(1)
    rng = np.random.default_rng(41627)
    inputs, probes = rng.normal(size=(2, 2))*.7, rng.normal(size=(3, 2))*.8
    for readout in (0., .8):
        params = legacy.initialize_network(3, 2, depth=3, seed=719)
        params = (*params[:-1], np.array([-.4, .7, .2])*readout)
        copies = [value.copy() for value in params]
        expected = oracle.initialize_probe_coefficients(params, inputs, probes, order=6)
        actual = production.initialize_probe_coefficients(params, inputs, probes, order=6,
                    device="cpu", batch_size=2, word_chunk_size=3)
        alternative = production.initialize_probe_coefficients(params, inputs, probes, order=6,
                    device="cpu", batch_size=3, word_chunk_size=7)
        old = old_probe.initialize_probe_coefficients(params, inputs, probes)
        for j, old_name in enumerate(("f", "Theta", "C", "Q"), 1):
            audit.close(f"readout{readout} P4 legacy {old_name}", actual["T"+str(j)], old[old_name], 2e-11, 2e-10)
        for name in actual:
            audit.close(f"readout{readout} full square-zero oracle {name}", actual[name], expected[name], 2e-11, 2e-10)
            audit.close(f"readout{readout} batch and word partition {name}", actual[name], alternative[name], 2e-12, 2e-11)
        for i, (before, after) in enumerate(zip(copies, params)):
            audit.close(f"readout{readout} input parameter immutable {i}", after, before, 0, 0)
        if readout:
            audit.check("T6 ordered derivative axes not silently symmetrized",
                        np.max(np.abs(actual["T6"]-actual["T6"].swapaxes(-1, -2))) > 1e-7)
            # Independent outer directional finite difference checks the
            # oracle's reverse flow-composition convention, including Dg.
            sample, word, epsilon = 1, (0, 1, 0), 2e-5
            fields = legacy.network_fields(params, inputs)
            h, delta = fields["h"], fields["delta"]
            directions = (np.outer(delta[0][:, sample], inputs[sample]),
                          np.outer(delta[1][:, sample], h[0][:, sample])/3,
                          np.outer(delta[2][:, sample], h[1][:, sample])/3,
                          h[2][:, sample])
            plus = tuple(p+epsilon*d for p, d in zip(params, directions))
            minus = tuple(p-epsilon*d for p, d in zip(params, directions))
            numerical = (oracle.selected_word_kernel(plus, inputs, probes, word)
                         -oracle.selected_word_kernel(minus, inputs, probes, word))/(2*epsilon)
            audit.close("oracle outer moving-direction convention through T6", numerical,
                        expected["T6"][(slice(None), slice(None), *word, sample)], 2e-7, 2e-6)
        antipodes = production.initialize_antipodal_probe_coefficients(params, inputs, probes[:2],
                       order=6, device="cpu", batch_size=2, word_chunk_size=5)
        explicit = production.initialize_probe_coefficients(params, inputs, np.r_[probes[:2], -probes[:2]],
                       order=6, device="cpu", batch_size=3, word_chunk_size=4)
        for name in explicit:
            audit.close(f"readout{readout} explicit antipodal {name}", antipodes[name], explicit[name], 2e-12, 2e-11)


def json_read(path):
    return json.loads(Path(path).read_text())


def manifest_checks(audit, directory):
    directory = directory.resolve()
    audit.check(str(directory)+" stays in assigned generated namespace", directory.is_relative_to(DATA))
    record = json_read(directory/"manifest.json")
    for name, expected in record["sources"].items():
        path = directory/"sources"/name
        audit.check(str(directory)+" frozen source "+name, path.is_file() and digest(path) == expected)
    for name, expected in record["inputs"].items():
        path = Path(name)
        permitted = path.is_relative_to(DATA)
        audit.check(str(directory)+" input integrity "+path.name,
                    permitted and path.is_file() and digest(path) == expected)
    for name, expected in record.get("outputs", {}).items():
        path = directory/name
        audit.check(str(directory)+" output integrity "+name, path.is_file() and digest(path) == expected)
    audit.check(str(directory)+" one numerical thread", all(record["threads"].get(name) == "1"
        for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")))
    return record


def saved_initialization(audit, directory):
    manifest_checks(audit, directory)
    record = json_read(directory/"result.json")
    config = record.get("configuration", json_read(directory/"configuration.json"))
    prefix = str(directory)
    audit.check(prefix+" declared task and width", config["case"] == "quadrant_alternating"
                and config["width"] == 2048 and config["seed"] in (20260920, 20260927))
    audit.check(prefix+" GPU device requested", config["device"].startswith("cuda:"))
    if record["status"] != "complete":
        audit.check(prefix+" resource stop explicitly recorded", record["status"] == "resource_limit")
        return dict(directory=str(directory), status=record["status"], configuration=config)
    audit.check(prefix+" declared precision", record["dtype"] == "float64"
                and record["deterministic_algorithms"] and record["tf32"] is False)
    audit.check(prefix+" GPU memory below cap", record["peak_cuda_allocated_bytes"] < 12*2**30)
    audit.check(prefix+" process RSS below cap", max(record["peak_rss_bytes"], record["peak_process_rss_bytes"]) < 8*2**30)
    audit.check(prefix+" whole-action wall cap", record["whole_action_limits_satisfied"]
                and record["total_seconds"] < config["seconds"])
    olddir = DATA/"scalar_wide_source01"/("quadrant_alternating_n2048_seed"+str(config["seed"]))
    old = load_npz(olddir/"initial_coefficients.npz")
    provenance = json_read(olddir/"initialization.json")
    audit.check(prefix+" same original network", record["initialization_hash"] == provenance["initialization_hash"])
    audit.check(prefix+" same literal eight inputs", record["training_input_hash"] == array_hash(old["inputs"]))
    data = load_npz(directory/"coefficients.npz")
    for j in range(1, config["order"]+1):
        value = data["T"+str(j)]
        count = record.get("queries", record["query_count"])
        audit.check(prefix+f" finite full T{j} shape", value.shape == (count,)+(8,)*(j-1)
                    and np.isfinite(value).all() and value.dtype == np.float64)
    if config["panel"] == "training":
        audit.close(prefix+" original input rows", data["inputs"], old["inputs"], 0, 0)
        audit.close(prefix+" original labels", data["labels"], old["labels"], 0, 0)
        for j, name in enumerate(("f", "Theta", "C", "Q"), 1):
            error = float(np.max(abs(data["T"+str(j)]-old[name])))
            bound = 1e-11+1e-9*float(np.max(abs(old[name])))
            audit.check(prefix+" independent legacy comparison "+name, error <= bound)
            audit.close(prefix+" recorded legacy error "+name, record["legacy_checks"][name]["maximum_difference"], error, 0, 0)
        for j in range(2, config["order"]+1):
            value = data["T"+str(j)]
            audit.close(prefix+f" symmetric first kernel pair T{j}", value, value.swapaxes(0, 1), 2e-11, 2e-10)
    elif config["panel"] == "probes":
        grid = config["grid"]
        angles = 2*np.pi*np.arange(grid)/grid
        off = 2*np.pi*(np.arange(32)+np.sqrt(2)/10)/32
        circle = lambda x:np.column_stack((np.cos(x), np.sin(x)))
        half, offhalf = circle(angles[:grid//2]), circle(off[:16])
        expected = np.vstack((half, -half, offhalf, -offhalf, old["inputs"]))
        audit.close(prefix+" passive antipodal point ordering", data["probe_inputs"], expected, 0, 0)
        audit.close(prefix+" grid angles", data["angles"], angles, 0, 0)
        audit.close(prefix+" off-grid angles", data["off_angles"], off, 0, 0)
        for j in range(1, config["order"]+1):
            value = data["T"+str(j)]
            audit.close(prefix+f" exact grid antipodes T{j}", value[grid//2:grid], -value[:grid//2], 0, 0)
            audit.close(prefix+f" exact off-grid antipodes T{j}", value[grid+16:grid+32], -value[grid:grid+16], 0, 0)
    return dict(directory=str(directory), status=record["status"], configuration=config,
                total_seconds=record["total_seconds"], peak_cuda_bytes=record["peak_cuda_allocated_bytes"],
                peak_rss_bytes=max(record["peak_rss_bytes"], record["peak_process_rss_bytes"]))


def vectorized_transport(coefficients, signatures, query_chunk=16):
    """Block matrix contraction, bounded-memory independent replay."""
    order, count = len(coefficients), len(coefficients["T1"])
    m = len(signatures[1])
    result = {"T"+str(j):np.array(coefficients["T"+str(j)], dtype=np.longdouble, copy=True)
              for j in range(1, order)}
    for start in range(0, count, query_chunk):
        stop = min(start+query_chunk, count)
        for j in range(1, order):
            target = result["T"+str(j)][start:stop].reshape(-1)
            for k in range(1, order-j+1):
                matrix = np.asarray(coefficients["T"+str(j+k)][start:stop], dtype=np.longdouble).reshape(-1, m**k)
                target += matrix @ np.asarray(signatures[k], dtype=np.longdouble).reshape(-1)
    result["T"+str(order)] = coefficients["T"+str(order)]
    return result


def saved_run(audit, directory):
    manifest_checks(audit, directory)
    record = json_read(directory/"result.json")
    source = Path(record["initialization"])
    initial = load_npz(source/"coefficients.npz")
    trajectory = load_npz(directory/"trajectory.npz")
    prefix, order, m = str(directory), record["order"], len(initial["labels"])
    training_size = sum(m**j for j in range(1, order))
    audit.check(prefix+" starts at zero", trajectory["times"][0] == 0)
    audit.check(prefix+" saved arrays finite", all(np.isfinite(value).all() for value in trajectory.values()))
    audit.check(prefix+" increasing accepted times", np.all(np.diff(trajectory["times"]) > 0))
    audit.check(prefix+" physical cap", 0 <= float(trajectory["time"]) <= 1e9)
    audit.check(prefix+" declared tolerance", record["rtol"] in (1e-7, 1e-9, 1e-11)
                and record["atol"] == record["rtol"]/100)
    audit.check(prefix+" RSS cap", record["peak_rss_bytes"] < 8*2**30 or record["status"] == "memory_cap")
    audit.close(prefix+" recorded final time", record["time"], trajectory["time"], 0, 0)
    audit.close(prefix+" recorded endpoint loss", record["loss"], np.mean((trajectory["train_f"]-initial["labels"])**2), 2e-14, 2e-14)
    audit.close(prefix+" final train state", trajectory["state"][:m], trajectory["train_f"], 0, 0)
    audit.close(prefix+" final local signatures reset", trajectory["state"][training_size:], 0, 0, 0)
    expected = np.concatenate([initial["T"+str(j)].reshape(-1) for j in range(1, order)])
    passive = {"T"+str(j):initial["T"+str(j)] for j in range(1, order+1)}
    peak_gap = 0.
    for index, state in enumerate(trajectory["segment_states"]):
        audit.close(prefix+f" preserved segment anchor {index}", trajectory["segment_training"][index], expected, 0, 0)
        expected = state[:training_size]
        _, signature = split(state, m, order)
        amplitude = max(float(np.max(abs(value)))/64**k for k, value in signature.items())
        audit.check(prefix+f" signature boundary {index}", amplitude <= 1+1e-8)
        if index+1 < len(trajectory["segment_states"]):
            audit.close(prefix+f" intermediate boundary reached {index}", amplitude, 1., 1e-8, 0)
        passive = vectorized_transport(passive, signature)
        peak_gap = max(peak_gap, float(np.sqrt(np.mean((passive["T1"]-state[:m])**2))))
    audit.close(prefix+" endpoint training preserved after final reset", trajectory["state"][:training_size], expected, 0, 0)
    tensors, _ = split(trajectory["state"], m, order)
    residual, kernel = tensors[1]-initial["labels"], tensors[2]
    quadratic = float(residual@kernel@residual)
    rho = quadratic/float(residual@residual)
    minimum_eigenvalue = float(np.linalg.eigvalsh((kernel+kernel.T)/2)[0])
    loss_derivative = -4/m**2*quadratic
    audit.close(prefix+" endpoint residual effective rate", record["endpoint_effective_rate"], rho, 1e-10, 1e-13)
    audit.close(prefix+" endpoint symmetric kernel minimum", record["endpoint_kernel_minimum_eigenvalue"],
                minimum_eigenvalue, 1e-10, 1e-13)
    audit.close(prefix+" maximum saved loss", record["maximum_saved_loss"], np.max(trajectory["losses"]), 0, 0)
    audit.close(prefix+" minimum saved loss", record["minimum_saved_loss"], np.min(trajectory["losses"]), 0, 0)
    audit.check(prefix+" segment count", record["segments"] == len(trajectory["segment_states"]))
    audit.check(prefix+" step count", record["accepted_steps"] == len(trajectory["times"])-1
                or (record["status"] == "solver_failure" and record["accepted_steps"] == len(trajectory["times"])))
    if record["status"] == "fitted":
        bracket = record["crossing_bracket"]
        audit.check(prefix+" first detected downward crossing", np.all(trajectory["losses"][:-1] > 1e-6)
                    and bracket["left_loss"] > 1e-6 >= bracket["right_loss"]
                    and bracket["left_time"] < record["time"] <= bracket["right_time"])
        audit.close(prefix+" target loss", record["loss"], 1e-6, 2e-12, 0)
    else:
        audit.check(prefix+" explicit nonfit status", record["status"] in
                    ("time_cap", "wall_cap", "step_cap", "memory_cap", "solver_failure", "nonfinite"))
        audit.check(prefix+" no earlier detected fitting", np.all(trajectory["losses"] > 1e-6))
    return dict(directory=str(directory), status=record["status"], order=order,
                time=record["time"], loss=record["loss"], seconds=record["seconds"],
                peak_training_replay_gap=peak_gap, training_replay_gate=peak_gap <= 1e-4,
                accepted_steps=record["accepted_steps"], segments=record["segments"],
                endpoint_effective_rate=rho, endpoint_symmetric_kernel_minimum=minimum_eigenvalue,
                endpoint_loss_derivative=loss_derivative,
                minimum_saved_loss=float(np.min(trajectory["losses"])),
                minimum_loss_time=float(trajectory["times"][np.argmin(trajectory["losses"])]),
                last_100_saved_loss_increments_positive_fraction=float(np.mean(np.diff(trajectory["losses"][-101:]) > 0)))


def saved_replay(audit, directory):
    manifest = manifest_checks(audit, directory)
    record = json_read(directory/"result.json")
    source_path, = [Path(name) for name in manifest["inputs"] if Path(name).name == "coefficients.npz"]
    probe = load_npz(source_path)
    trajectory = load_npz(Path(record["run"])/"trajectory.npz")
    endpoint = load_npz(directory/"endpoint.npz")
    order, prefix = record["order"], str(directory)
    passive = {"T"+str(j):probe["T"+str(j)] for j in range(1, order+1)}
    gaps = []
    for state in trajectory["segment_states"]:
        _, signatures = split(state, 8, order)
        passive = vectorized_transport(passive, signatures)
        gaps.append(float(np.sqrt(np.mean((passive["T1"][-8:]-state[:8])**2))))
    grid = len(probe["angles"])
    prediction = np.asarray(passive["T1"], dtype=float)
    for name, expected in (("grid", prediction[:grid]), ("off_grid", prediction[grid:grid+32]),
                           ("train_probe", prediction[-8:]), ("train_f", trajectory["train_f"]),
                           ("time", trajectory["time"]), ("segment_training_gaps", np.array(gaps))):
        audit.close(prefix+" independent passive replay "+name, endpoint[name], expected, 2e-9, 2e-12)
    audit.close(prefix+" recorded maximum passive training gap", record["training_probe_gap"], max(gaps, default=0.), 2e-9, 2e-12)
    audit.check(prefix+" segments retained", record["segments"] == len(gaps))
    audit.check(prefix+" no research training during replay", record["status"] == json_read(Path(record["run"])/"result.json")["status"])
    return dict(directory=str(directory), source=str(source_path.parent), run=record["run"], order=order,
                status=record["status"], peak_training_replay_gap=max(gaps, default=0.),
                training_replay_gate=max(gaps, default=0.) <= 1e-4, replay_seconds=record["replay_seconds"])


def columns(path, *names):
    with np.load(path, allow_pickle=False) as arrays:
        return {name:arrays[name].copy() for name in names}


def rms(value):
    value = np.asarray(value, dtype=np.longdouble)
    return float(np.sqrt(np.mean(value*value)))


def analysis_checks(audit, directory):
    summary = json_read(directory/"analysis.json")
    manifest = json_read(directory/"manifest.json")
    for name, checksum in manifest["inputs"].items():
        path = Path(name)
        allowed = path.is_relative_to(DATA) or path.is_relative_to(HERE)
        audit.check("analysis input integrity "+name, allowed and digest(path) == checksum)
    for name, checksum in manifest["outputs"].items():
        audit.check("analysis output integrity "+name, digest(directory/name) == checksum)
    audit.check("analysis has fixed width, task and both seeds", summary["width"] == 2048
        and summary["samples"] == 8 and summary["target"] == 1e-6
        and [entry["seed"] for entry in summary["configurations"]] == [20260920, 20260927])
    diagnostics = []
    for entry in summary["configurations"]:
        seed = entry["seed"]
        old = DATA/"scalar_wide_primary01"/("quadrant_alternating_n2048_seed"+str(seed))
        dense = columns(old/"dense_resolution1"/"trajectory.npz", "grid", "time")
        dense_coarse = columns(old/"dense_resolution0"/"trajectory.npz", "grid")
        dense_change = rms(dense_coarse["grid"]-dense["grid"])
        audit.close(f"seed{seed} dense refinement", entry["dense_refinement"]["numerical_change"], dense_change, 2e-13, 2e-12)
        for order in (5, 6):
            item = entry["order"+str(order)]
            parent = DATA/"scalar_high_order_primary01"/("seed"+str(seed))
            folders = sorted((path for path in parent.iterdir() if path.is_dir()
                             and re.fullmatch("order"+str(order)+r"_resolution\d+", path.name)),
                             key=lambda path:int(path.name.split("resolution")[1]))
            latest = folders[-1]
            records = [json_read(folder/"result.json") for folder in folders]
            record = records[-1]
            prefix = f"seed{seed} P{order} analysis"
            audit.check(prefix+" latest resolution selected", item["rtol"] == record["rtol"]
                        and item["status"] == record["status"])
            for name in ("time", "loss", "accepted_steps", "nfev", "njev", "nlu", "segments"):
                audit.close(prefix+" "+name, item[name], record[name], 1e-9, 1e-12)
            audit.check(prefix+" exact scalar counts", item["moving_state_scalars"] == 2*sum(8**j for j in range(1, order))
                        and item["initialized_training_scalars"] == sum(8**j for j in range(1, order+1)))
            dt = abs(records[-2]["time"]-record["time"])/max(1., record["time"])
            audit.close(prefix+" fitting-time refinement", item["refinement"]["time_relative_change"], dt, 1e-14, 1e-12)
            if record["status"] != "fitted":
                audit.check(prefix+" no matched endpoint manufactured", "spatial" not in item
                    and not item["direct_grid_qualified"] and not item["encoded_qualified"]
                    and item["verdict"] == "no_matched_endpoint")
                continue
            endpoints = [load_npz(folder.with_name(folder.name+"_readout")/"endpoint.npz") for folder in folders[-2:]]
            end = endpoints[-1]
            delta = end["grid"]-dense["grid"]
            error, change = rms(delta), rms(endpoints[-2]["grid"]-end["grid"])
            quadrature = abs(error-rms(delta[::2]))
            spatial = item["spatial"]
            for key, expected in (("circle_rms", error), ("relative_rms", error/rms(dense["grid"])),
                                  ("maximum_error", np.max(abs(delta))), ("dense_function_rms", rms(dense["grid"])),
                                  ("quadrature_change", quadrature)):
                audit.close(prefix+" spatial "+key, spatial[key], expected, 2e-12, 2e-12)
            audit.close(prefix+" scalar refinement", item["refinement"]["numerical_change"], change, 2e-12, 2e-12)
            gap = max(float(np.max(endpoint["segment_training_gaps"])) for endpoint in endpoints)
            passed = all(r["status"] == "fitted" for r in records[-2:]) and gap <= 1e-4
            passed = passed and change <= .002 and change <= .1*max(error, 1e-6) and dt <= .001
            audit.check(prefix+" independent refinement gate", item["refinement"]["passed"] == passed)
            quadrature_pass = quadrature <= .001 and quadrature <= .01*max(error, 1e-6)
            audit.check(prefix+" independent quadrature gate", spatial["quadrature_pass"] == quadrature_pass)
            count = len(end["grid"])
            angles = 2*np.pi*np.arange(count)/count
            off = 2*np.pi*(np.arange(32)+np.sqrt(2)/10)/32
            fourier_pass = False
            for index, degree in enumerate((64, 128, 256)):
                modes = np.fft.rfft(end["grid"])/count
                frequency = np.arange(1, degree+1)
                evaluate = lambda x:modes[0].real+2*(np.cos(np.outer(x, frequency))@modes[1:degree+1].real
                                                    -np.sin(np.outer(x, frequency))@modes[1:degree+1].imag)
                grid_error, off_error = evaluate(angles)-end["grid"], evaluate(off)-end["off_grid"]
                measured = dict(mode=degree, grid_rms=rms(grid_error), off_grid_rms=rms(off_error),
                                maximum=float(max(np.max(abs(grid_error)), np.max(abs(off_error)))))
                fourier_pass = max(measured["grid_rms"], measured["off_grid_rms"]) <= 1e-5 and measured["maximum"] <= 1e-4
                for key, value in measured.items():
                    audit.close(prefix+f" mode{degree} "+key, spatial["fourier"][index][key], value, 3e-11, 2e-8)
                if fourier_pass:
                    break
            audit.check(prefix+" Fourier gate", spatial["fourier_pass"] == fourier_pass)
            reproduction_pass = True
            if seed == 20260920:
                fresh = DATA/"scalar_high_order_reproduction01"/"seed20260920"/("order"+str(order))
                freshrecord = json_read(fresh/"result.json")
                freshend = load_npz(fresh.with_name(fresh.name+"_readout")/"endpoint.npz")
                reproducibility_change = rms(freshend["grid"]-end["grid"])
                reproducibility_dt = abs(float(freshend["time"])-float(end["time"]))/max(1., float(freshend["time"]))
                freshgap = float(np.max(freshend["segment_training_gaps"]))
                reproduction_pass = freshrecord["status"] == "fitted" and max(gap, freshgap) <= 1e-4
                reproduction_pass = reproduction_pass and reproducibility_change <= .002 and reproducibility_change <= .1*max(error, 1e-6) and reproducibility_dt <= .001
                audit.close(prefix+" reproduction function difference", item["reproduction"]["comparison"]["numerical_change"], reproducibility_change, 2e-12, 2e-12)
                audit.close(prefix+" reproduction time difference", item["reproduction"]["comparison"]["time_relative_change"], reproducibility_dt, 1e-14, 1e-12)
                audit.check(prefix+" reproduction gate", item["reproduction"]["passed"] == reproduction_pass)
            qualified = bool(passed and quadrature_pass and reproduction_pass)
            audit.check(prefix+" direct-grid qualification", item["direct_grid_qualified"] == qualified)
            audit.check(prefix+" encoded qualification", item["encoded_qualified"] == (qualified and fourier_pass))
            expected_verdict = "numerically_inconclusive" if not qualified else "agreement" if error <= .1 else "adverse" if error > .2 else "inconclusive"
            audit.check(prefix+" direct verdict", item["direct_grid_verdict"] == expected_verdict)
            diagnostics.append(dict(seed=seed, order=order, error=error, refinement_change=change,
                                    peak_pair_gap=gap, direct_grid_qualified=qualified, fourier_pass=fourier_pass))
        comparison = entry["comparisons"]["order5_over_order4"]
        low, high = entry["order4"], entry["order5"]
        if "spatial" in high:
            low_error, high_error = low["spatial"]["circle_rms"], high["spatial"]["circle_rms"]
            numerical = 10*(low["refinement"]["numerical_change"]+high["refinement"]["numerical_change"]+dense_change)
            audit.close(f"seed{seed} E5/E4", comparison["ratio"], high_error/low_error, 2e-13, 2e-12)
            audit.close(f"seed{seed} resolved-improvement numerical margin", comparison["numerical_threshold"], numerical, 2e-13, 2e-12)
            resolved = bool(low["direct_grid_qualified"] and high["direct_grid_qualified"]
                            and low_error-high_error > .01*low_error and low_error-high_error > numerical)
            audit.check(f"seed{seed} resolved improvement gate", comparison["resolved_improvement"] == resolved)
    return diagnostics


def reproduction_checks(audit):
    diagnostics = {}
    for kind in ("training", "probes"):
        first = DATA/("scalar_high_order_"+kind+"01")/"seed20260920"/"coefficients.npz"
        fresh = DATA/("scalar_high_order_"+kind+"_reproduction01")/"seed20260920"/"coefficients.npz"
        differences = {}
        with np.load(first, allow_pickle=False) as a, np.load(fresh, allow_pickle=False) as b:
            audit.check(kind+" reproduction fields", set(a.files) == set(b.files))
            for name in a.files:
                x, y = a[name], b[name]
                difference = float(np.max(abs(x-y), initial=0))
                bitwise = bool(np.array_equal(x, y))
                bound = 1e-11+1e-9*float(np.max(abs(x), initial=0))
                audit.check(kind+" fresh coefficient tolerance "+name, difference <= bound)
                differences[name] = dict(maximum_difference=difference, bitwise_equal=bitwise)
        diagnostics[kind] = differences
    for order in (5, 6):
        parent = DATA/"scalar_high_order_primary01"/"seed20260920"
        primary = sorted((path for path in parent.iterdir() if path.is_dir()
                         and re.fullmatch("order"+str(order)+r"_resolution\d+", path.name)),
                         key=lambda path:int(path.name.split("resolution")[1]))[-1]
        fresh = DATA/"scalar_high_order_reproduction01"/"seed20260920"/("order"+str(order))
        a, b = json_read(primary/"result.json"), json_read(fresh/"result.json")
        audit.check(f"P{order} reproduced status and settings", a["status"] == b["status"]
                    and a["message"] == b["message"] and a["rtol"] == b["rtol"] and a["atol"] == b["atol"])
        one, two = load_npz(primary/"trajectory.npz"), load_npz(fresh/"trajectory.npz")
        equal = {name:bool(np.array_equal(one[name], two[name])) for name in one}
        diagnostics["order"+str(order)] = dict(status=a["status"], all_saved_arrays_equal=all(equal.values()),
                                               arrays=equal, time_difference=abs(a["time"]-b["time"]))
    return diagnostics


def budget_checks(audit):
    initialization_paths = [DATA/"scalar_high_order_pilot01"]
    for namespace in ("scalar_high_order_training01", "scalar_high_order_training_reproduction01",
                      "scalar_high_order_probes01", "scalar_high_order_probes_reproduction01"):
        initialization_paths += sorted(path.parent for path in (DATA/namespace).glob("*/result.json"))
    initialization_records = [(path, json_read(path/"result.json")) for path in initialization_paths]
    run_paths, readout_paths, launches = [], [], []
    for namespace in ("scalar_high_order_primary01", "scalar_high_order_reproduction01"):
        for path in (DATA/namespace).glob("*/*/result.json"):
            if path.parent.name.endswith("_readout"):
                readout_paths.append(path.parent)
            elif re.fullmatch(r"order[56](?:_resolution\d+)?", path.parent.name):
                run_paths.append(path.parent)
        launches += sorted((DATA/namespace).glob("*/launch.json"))
    audit.check("budget exact initialization phases", len(initialization_records) == 7)
    audit.check("budget exact integration phases", len(run_paths) == 12)
    audit.check("budget exact readout phases", len(readout_paths) == 7)
    covered, launch_seconds, receipt_records = set(), 0., []
    for path in launches:
        record = json_read(path)
        audit.close(str(path)+" active seconds sum", record["active_seconds"], sum(item["seconds"] for item in record["records"]), 1e-10, 1e-14)
        for item in record["records"]:
            command = item["command"]
            destination = Path(command[command.index("--output")+1]).resolve()
            audit.check(str(destination)+" successful launcher completion", item["exit_code"] == 0)
            audit.check(str(destination)+" not counted twice in launch receipts", destination not in covered)
            covered.add(destination)
            launch_seconds += item["seconds"]
            receipt_records.append(dict(path=str(path), output=str(destination), seconds=item["seconds"]))
    init_seconds = sum(record["total_seconds"] for _, record in initialization_records)
    other_seconds = sum(json_read(path/"result.json")["seconds"] for path in run_paths if path.resolve() not in covered)
    replay_seconds = sum(json_read(path/"result.json")["replay_seconds"] for path in readout_paths)
    total = init_seconds+launch_seconds+other_seconds+replay_seconds
    audit.check("reported active-work subtotal below campaign limit", total < 10800)
    allrecords = [record for _, record in initialization_records]+[json_read(path/"result.json") for path in run_paths+readout_paths]
    peak_cuda = max(record.get("peak_cuda_allocated_bytes", 0) for record in allrecords)
    peak_rss = max(max(record.get("peak_rss_bytes", 0), record.get("peak_process_rss_bytes", 0)) for record in allrecords)
    audit.check("global observed CUDA cap", peak_cuda < 12*2**30)
    audit.check("global observed process RSS cap", peak_rss < 8*2**30)
    return dict(initializations=[dict(directory=str(path), seconds=record["total_seconds"],
                                     panel=record["configuration"]["panel"]) for path,record in initialization_records],
                launch_receipts=receipt_records, initialization_seconds=init_seconds,
                wrapped_integration_seconds=launch_seconds, unwrapped_integration_seconds=other_seconds,
                replay_seconds=replay_seconds, reported_active_work_subtotal=total,
                peak_cuda_allocated_bytes=peak_cuda, peak_rss_bytes=peak_rss,
                note="Launch receipts include subprocess overhead. Standalone reported work omits unrecorded process startup/source-copy/scoring overhead. Concurrent CPU/GPU work is summed; this is not a campaign elapsed stopwatch.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--skip-deterministic", action="store_true")
    parser.add_argument("--initialization", type=Path, action="append", default=[])
    parser.add_argument("--run", type=Path, action="append", default=[])
    parser.add_argument("--replay", type=Path, action="append", default=[])
    parser.add_argument("--analysis", type=Path)
    parser.add_argument("--reproduction", action="store_true")
    parser.add_argument("--budget", action="store_true")
    args = parser.parse_args()
    started = time.monotonic()
    audit = Audit()
    if not args.skip_deterministic:
        engine_checks(audit)
        initializer_checks(audit)
    initializations = [saved_initialization(audit, path.resolve()) for path in args.initialization]
    runs = [saved_run(audit, path.resolve()) for path in args.run]
    replays = [saved_replay(audit, path.resolve()) for path in args.replay]
    analysis = analysis_checks(audit, args.analysis.resolve()) if args.analysis else None
    reproduction = reproduction_checks(audit) if args.reproduction else None
    budget = budget_checks(audit) if args.budget else None
    result = audit.result()
    result.update(wall_seconds=time.monotonic()-started,
                  scope="deterministic implementation and requested saved-data checks; no research training or GPU use",
                  initializations=initializations, runs=runs, replays=replays, analysis=analysis,
                  reproduction=reproduction, budget=budget,
                  source_hashes={name:digest(Path(__file__).with_name(name)) for name in
                    ("check_scalar_high_order.py", "scalar_high_order_engine.py",
                     "scalar_high_order_initialization.py", "scalar_high_order_oracle.py",
                     "SCALAR_HIGH_ORDER_PROTOCOL.md", "SCALAR_HIGH_ORDER_INITIALIZATION.md",
                     "SCALAR_HIGH_ORDER_ENGINE.md", "run_scalar_high_order.py",
                     "test_scalar_high_order_initialization.py", "test_scalar_high_order_engine.py")})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key:result[key] for key in ("status", "checks", "failures", "wall_seconds")}))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
