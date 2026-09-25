"""Independent deterministic and saved-data checks for the long-time extension.

This checker performs no research training. Its reference contractions and
complex-step Jacobian are independent of the production implementations.
"""

import argparse
import hashlib
import json
from pathlib import Path
import warnings

import numpy as np


NAMES = ("f", "Theta", "C", "Q")


class Audit:
    def __init__(self):
        self.checks = []

    def check(self, name, passed, **details):
        self.checks.append({"name": name, "passed": bool(passed), **details})

    def close(self, name, actual, expected, atol=1e-10, rtol=1e-10):
        actual, expected = np.asarray(actual), np.asarray(expected)
        error = float(np.max(np.abs(actual - expected), initial=0))
        self.check(name, np.allclose(actual, expected, atol=atol, rtol=rtol),
                   maximum_absolute_error=error, atol=atol, rtol=rtol)

    def result(self):
        return {"status": "PASS" if all(c["passed"] for c in self.checks) else "FAIL",
                "checks": len(self.checks),
                "failures": [c for c in self.checks if not c["passed"]],
                "details": self.checks}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_npz(path):
    with np.load(path, allow_pickle=False) as data:
        return {key: data[key].copy() for key in data.files}


def split_state(state, m):
    """Independent documented ordering f,Theta,C,z,I,J."""
    result, offset = {}, 0
    for name, degree in (("f", 1), ("Theta", 2), ("C", 3),
                         ("z", 1), ("I", 2), ("J", 3)):
        size = m ** degree
        result[name] = np.asarray(state)[offset:offset + size].reshape((m,) * degree)
        offset += size
    if len(state) != offset:
        raise ValueError("unexpected long-time state size")
    return result


def independent_rhs(state, labels, q):
    """Polynomial reference preserving complex dtype for exact differentiation."""
    s = split_state(state, len(labels))
    velocity = -2 / len(labels) * (s["f"] - labels)
    values = (np.einsum("ab,b->a", s["Theta"], velocity),
              np.einsum("abc,c->ab", s["C"], velocity),
              np.einsum("abcd,d->abc", q, velocity),
              velocity, np.einsum("b,c->bc", velocity, s["z"]),
              np.einsum("b,cd->bcd", velocity, s["I"]))
    return np.concatenate([v.reshape(-1) for v in values])


def independent_recenter(coefficients, signature):
    """Ordered contractions from the protocol, always with old anchors."""
    f, k, c, q = (np.asarray(coefficients[n], dtype=np.longdouble) for n in NAMES)
    z, i, j = (np.asarray(signature[n], dtype=np.longdouble) for n in ("z", "I", "J"))
    return {"f": f + np.einsum("ab,b->a", k, z)
                    + np.einsum("abc,bc->a", c, i)
                    + np.einsum("abcd,bcd->a", q, j),
            "Theta": k + np.einsum("abc,c->ab", c, z)
                       + np.einsum("abcd,cd->ab", q, i),
            "C": c + np.einsum("abcd,d->abc", q, z), "Q": q.copy()}


def constant_signature(displacement):
    z = np.asarray(displacement)
    return {"z": z, "I": np.einsum("a,b->ab", z, z) / 2,
            "J": np.einsum("a,b,c->abc", z, z, z) / 6}


def concatenate_signatures(first, second):
    """Chen composition for the reversed chronological convention in this study."""
    return {"z": first["z"] + second["z"],
            "I": first["I"] + second["I"] + np.outer(second["z"], first["z"]),
            "J": first["J"] + second["J"]
                 + np.einsum("b,cd->bcd", second["z"], first["I"])
                 + np.einsum("bc,d->bcd", second["I"], first["z"])}


def frozen_reference(initial, passive, time):
    """Independent spectral training prediction and stable residual integral."""
    kernel = np.asarray(initial["Theta"])
    values, vectors = np.linalg.eigh((kernel + kernel.T) / 2)
    m = len(values)
    residual_modes = vectors.T @ (initial["f"] - initial["labels"])
    exponent = -(2 / m) * values * time
    decay = np.exp(exponent)
    integrated = np.empty_like(values)
    nonzero = values != 0
    integrated[nonzero] = np.expm1(exponent[nonzero]) / values[nonzero]
    integrated[~nonzero] = -(2 / m) * time
    z = vectors @ (integrated * residual_modes)
    prediction = initial["labels"] + vectors @ (decay * residual_modes)
    probe = np.asarray(passive["f"], dtype=np.longdouble)
    probe = probe + np.asarray(passive["Theta"], dtype=np.longdouble) @ z.astype(np.longdouble)
    return {"values": values, "vectors": vectors, "z": z,
            "train_f": prediction, "probe": probe,
            "loss": float(np.mean((prediction - initial["labels"]) ** 2))}


def fourier_reference(values, angles, mode):
    coefficient = np.fft.rfft(np.asarray(values))[:mode + 1] / len(values)
    phase = np.exp(1j * np.multiply.outer(angles, np.arange(1, mode + 1)))
    return coefficient[0].real + 2 * np.real(phase @ coefficient[1:])


def deterministic(audit):
    from scipy.integrate import BDF
    from scipy.linalg import expm
    from scalar_long_time_engine import (StiffSignatureHierarchy,
                                         frozen_kernel_endpoint, recenter_coefficients)

    rng = np.random.default_rng(194718)
    for m in (2, 3, 4):
        coefficients = {name: rng.normal(size=(m,) * degree)
                        for degree, name in enumerate(NAMES, 1)}
        labels = rng.normal(size=m)
        system = StiffSignatureHierarchy(coefficients, labels)
        state = rng.normal(size=system.size)
        audit.close(f"m{m}: independent RHS", system.rhs(0, state),
                    independent_rhs(state, labels, coefficients["Q"]))
        reference = np.empty((system.size, system.size))
        for column in range(system.size):
            perturb = state.astype(complex)
            perturb[column] += 1e-25j
            reference[:, column] = independent_rhs(perturb, labels, coefficients["Q"]).imag / 1e-25
        jacobian = system.jac(0, state)
        audit.check(f"m{m}: sparse Jacobian", jacobian.format == "csc")
        audit.close(f"m{m}: full complex-step Jacobian", jacobian.toarray(), reference,
                    atol=2e-13, rtol=2e-13)
        audit.close(f"m{m}: passive signature no feedback",
                    jacobian.toarray()[:system.training_size, system.training_size:], 0, atol=0, rtol=0)
        first = constant_signature(rng.normal(size=m))
        second = constant_signature(rng.normal(size=m))
        third = constant_signature(rng.normal(size=m))
        passive = {name: rng.normal(size=(5,) + (m,) * degree)
                   for degree, name in enumerate(NAMES)}
        old = {name: value.copy() for name, value in passive.items()}
        centered = recenter_coefficients(passive, first)
        expected = independent_recenter(passive, first)
        for name in NAMES:
            audit.close(f"m{m}: old-anchor contraction {name}", centered[name], expected[name],
                        atol=2e-14, rtol=2e-14)
            audit.close(f"m{m}: recenter leaves input {name}", passive[name], old[name], atol=0, rtol=0)
        audit.check(f"m{m}: unchanged terminal identity", centered["Q"] is passive["Q"])
        sequential = recenter_coefficients(recenter_coefficients(centered, second), third)
        complete = concatenate_signatures(concatenate_signatures(first, second), third)
        monolithic = independent_recenter(passive, complete)
        for name in NAMES:
            audit.close(f"m{m}: noncommuting three-segment transport {name}",
                        sequential[name], monolithic[name], atol=5e-13, rtol=5e-13)
        audit.check(f"m{m}: ordered derivative stress is nondegenerate",
                    np.max(np.abs(passive["Q"] - passive["Q"].swapaxes(-1, -2))) > .1)
        system.readout(passive, state)
        audit.close(f"m{m}: readout leaves training derivative unchanged", system.rhs(0, state),
                    independent_rhs(state, labels, coefficients["Q"]), atol=0, rtol=1e-14)

    spectral_cases = (
        (np.diag([.1, 2., 5.]), np.array([1., -.5, .3]), 1e-6, 200.),
        (np.diag([0., .2, 2.]), np.array([0., 1., -.5]), 1e-6, 200.),
        (np.diag([0., .2, 2.]), np.array([1., 1., -.5]), 1e-6, 10.),
        (np.diag([-.2, 2.]), np.array([.001, 1.]), .01, 20.),
    )
    for index, (kernel, residual, target, cap) in enumerate(spectral_cases):
        m = len(residual)
        labels = rng.normal(size=m)
        initial = {"f": labels + residual, "Theta": kernel, "labels": labels}
        result = frozen_kernel_endpoint(initial, labels, target=target, time_cap=cap)
        expected = labels + expm(-(2 / m) * kernel * result["time"]) @ residual
        audit.close(f"spectral{index}: independent matrix exponential", result["train_f"], expected)
        audit.close(f"spectral{index}: integral identity",
                    initial["f"] + kernel @ result["z"], expected)
        if result["status"] == "fitted":
            audit.close(f"spectral{index}: target event", result["loss"], target, atol=1e-12, rtol=1e-10)
            earlier = expm(-(2 / m) * kernel * result["time"] * (1 - 1e-6)) @ residual
            audit.check(f"spectral{index}: downward first-crossing side", np.mean(earlier ** 2) > target)
        else:
            audit.check(f"spectral{index}: cap preserves nonfitting", result["time"] == cap and result["loss"] > target)

    # SciPy 1.11.4 leaves unused high difference rows uninitialized. Its first
    # accepted step reads one only to construct a row overwritten before use.
    # Deliberately poison those rows with signaling NaNs and compare the whole
    # accepted trajectory with zero-filled unused rows on a deterministic ODE.
    linear = np.diag([-1., -100.])
    rhs = lambda t, state: linear @ state
    reference = BDF(rhs, 0., np.array([1., -.5]), .2, rtol=1e-9, atol=1e-11, jac=linear)
    poisoned = BDF(rhs, 0., np.array([1., -.5]), .2, rtol=1e-9, atol=1e-11, jac=linear)
    reference.D[2:] = 0.
    poisoned.D[2:] = np.array([0x7ff0000000000001], dtype=np.uint64).view(np.float64)[0]
    same, count = True, 0
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always", RuntimeWarning)
        while reference.status == "running":
            reference.step()
            poisoned.step()
            count += 1
            same = same and reference.status == poisoned.status and reference.t == poisoned.t
            same = same and reference.order == poisoned.order and np.array_equal(reference.y, poisoned.y)
            same = same and np.array_equal(reference.D[:reference.order + 1], poisoned.D[:poisoned.order + 1])
    audit.check("BDF unused-workspace signaling-NaN stress", same, accepted_steps=count)
    audit.check("BDF first-step warning reproduced", any("invalid value" in str(w.message) for w in caught),
                warnings=[str(w.message) for w in caught])


def scalar_rms(value):
    return float(np.sqrt(np.mean(np.asarray(value, dtype=np.longdouble) ** 2)))


def pair_reference(first, second, first_record, second_record, dense):
    error = scalar_rms(second["grid"] - dense["grid"])
    change = scalar_rms(first["grid"] - second["grid"])
    time_change = abs(float(first["time"] - second["time"])) / max(1., float(second["time"]))
    passed = (first_record["status"] == second_record["status"] == "fitted"
              and change <= .002 and change <= .1 * max(error, 1e-6)
              and time_change <= .001
              and max(first_record["training_probe_gap"], second_record["training_probe_gap"]) <= 1e-4)
    return {"circle_rms": error, "numerical_change": change,
            "time_relative_change": time_change, "passed": passed}


def check_spatial(audit, prefix, prediction, probe, dense, saved, fourier_path):
    difference = prediction["grid"] - dense["grid"]
    error = scalar_rms(difference)
    quadrature = abs(error - scalar_rms(difference[::2]))
    audit.close(prefix + ": circle RMS", saved["circle_rms"], error, atol=1e-11)
    audit.close(prefix + ": relative circle RMS", saved["relative_rms"], error / scalar_rms(dense["grid"]))
    audit.close(prefix + ": quadrature sensitivity", saved["quadrature_change"], quadrature, atol=1e-11)
    gate = quadrature <= .001 and quadrature <= .01 * max(error, 1e-6)
    audit.check(prefix + ": quadrature gate scoring", saved["quadrature_pass"] == gate)
    for index, entry in enumerate(saved["fourier"]):
        mode = entry["mode"]
        audit.check(prefix + f": Fourier mode {index} progression", mode == (64, 128, 256)[index])
        grid_difference = fourier_reference(prediction["grid"], probe["angles"], mode) - prediction["grid"]
        off_difference = fourier_reference(prediction["grid"], probe["off_angles"], mode) - prediction["off_grid"]
        maximum = float(max(np.max(abs(grid_difference)), np.max(abs(off_difference))))
        gate = max(scalar_rms(grid_difference), scalar_rms(off_difference)) <= 1e-5 and maximum <= 1e-4
        audit.close(prefix + f": mode{mode} grid error", entry["grid_rms"], scalar_rms(grid_difference), atol=2e-10)
        audit.close(prefix + f": mode{mode} off-grid error", entry["off_grid_rms"], scalar_rms(off_difference), atol=2e-10)
        audit.close(prefix + f": mode{mode} maximum", entry["maximum"], maximum, atol=2e-9)
        audit.check(prefix + f": mode{mode} gate scoring", entry["passed"] == gate)
        if index:
            audit.check(prefix + f": mode{mode} conditional trigger", not saved["fourier"][index - 1]["passed"])
    stored = load_npz(fourier_path)
    expected = np.fft.rfft(prediction["grid"])[:saved["fourier"][-1]["mode"] + 1] / len(prediction["grid"])
    audit.close(prefix + ": saved endpoint Fourier coefficients", stored["endpoint"], expected)


def saved_data(audit, directory, original_directory):
    if original_directory is None:
        raise ValueError("--original is required for the saved-data audit")
    directory = Path(directory).resolve()
    original_directory = Path(original_directory).resolve()
    manifest = json.loads((directory / "manifest.json").read_text())
    for name, expected_hash in manifest["sources"].items():
        audit.check("source hash: " + name, digest(directory / "sources" / name) == expected_hash)
    for path, expected_hash in manifest["inputs"].items():
        input_path = Path(path)
        audit.check("input provenance: " + str(input_path.relative_to(original_directory)),
                    input_path.is_relative_to(original_directory) and digest(input_path) == expected_hash)
    campaign = json.loads((directory / "campaign.json").read_text())
    audit.check("all four configurations accounted for", len(campaign["configurations"]) == 4)
    audit.check("cumulative research budget", campaign["seconds"] <= 1800.5)
    for number, config in enumerate(campaign["configurations"]):
        name = config["configuration"]
        source, target = original_directory / name, directory / name
        initial, probe = load_npz(source / "initial_coefficients.npz"), load_npz(source / "probe_coefficients.npz")
        dense = load_npz(source / "dense_resolution1.npz")
        m, labels, size = len(initial["labels"]), initial["labels"], sum(len(initial["labels"]) ** k for k in (1, 2, 3))
        audit.close(name + ": dense reference fitted", np.mean((dense["train_f"] - labels) ** 2), 1e-6, atol=1e-12)
        width = int(name.split("_n")[1].split("_")[0])
        state, cursor, matrices = dense["state"], 0, []
        for shape in ((width, 2), (width, width), (width, width)):
            count = int(np.prod(shape))
            matrices.append(state[cursor:cursor + count].reshape(shape))
            cursor += count
        readout = state[cursor:]
        value = probe["probe_inputs"].T
        for matrix in matrices:
            value = np.tanh(matrix @ value)
        predictions = readout @ value / width
        audit.close(name + ": independent dense grid evaluation", dense["grid"], predictions[:1024], atol=1e-12)
        audit.close(name + ": independent dense off-grid evaluation", dense["off_grid"], predictions[1024:1056], atol=1e-12)
        audit.close(name + ": dense endpoint time provenance", config["dense_time"], dense["time"], atol=0, rtol=0)
        for key in NAMES:
            audit.close(name + ": initial training-probe identity " + key,
                        probe[key][-m:], initial[key], atol=0, rtol=0)
        runs, records = {}, {}
        for run in sorted(target.iterdir()):
            if not run.is_dir() or not (run / "trajectory.npz").exists():
                continue
            prefix = name + "/" + run.name
            result = json.loads((run / "result.json").read_text())
            arrays = load_npz(run / "trajectory.npz")
            audit.check(prefix + ": all archived numeric arrays finite",
                        all(np.isfinite(value).all() for value in arrays.values()))
            runs[run.name], records[run.name] = arrays, result
            anchors = {key: probe[key] for key in NAMES}
            if result["from_zero"]:
                start = np.concatenate([initial[key].reshape(-1) for key in NAMES[:3]])
                start_time = 0.
            else:
                archived = load_npz(source / ("order4_resolution" + str(result["start_level"]) + ".npz"))
                start, start_time = archived["state"][:size], float(archived["time"])
                anchors = independent_recenter(anchors, split_state(archived["state"], m))
            audit.close(prefix + ": original restart time", arrays["times"][0], start_time, atol=0, rtol=0)
            audit.close(prefix + ": starting training state", arrays["segment_training"][0], start, atol=0, rtol=0)
            audit.check(prefix + ": time monotonicity", np.all(np.diff(arrays["times"]) > 0))
            audit.check(prefix + ": physical cap", float(arrays["time"]) <= 1e9)
            audit.check(prefix + ": per-trajectory resource bounds", result["seconds"] <= 182 and result["peak_rss_bytes"] < 2 * 1024 ** 3)
            milestones = json.loads((run / "milestones.json").read_text())
            audit.check(prefix + ": milestone archive cardinality", len(milestones) == len(arrays["milestone_states"])
                        == len(arrays["milestone_grids"]) == len(arrays["milestone_segments"]))
            maximum_gap = scalar_rms(anchors["f"][-m:] - start[:m])
            for segment, local_state in enumerate(arrays["segment_states"]):
                prefix_segment = prefix + f": segment{segment}"
                audit.close(prefix_segment + " unchanged training anchor", arrays["segment_training"][segment], start, atol=0, rtol=0)
                for milestone_index in np.flatnonzero(arrays["milestone_segments"] == segment):
                    milestone = milestones[milestone_index]
                    checkpoint = split_state(arrays["milestone_states"][milestone_index], m)
                    checkpoint_probe = independent_recenter(anchors, checkpoint)["f"]
                    checkpoint_residual = checkpoint["f"] - labels
                    eigenvalues = np.linalg.eigvalsh((checkpoint["Theta"] + checkpoint["Theta"].T) / 2)
                    rate = checkpoint_residual @ checkpoint["Theta"] @ checkpoint_residual / (checkpoint_residual @ checkpoint_residual)
                    tag = prefix + f": milestone{milestone_index}"
                    audit.close(tag + " loss", milestone["loss"], np.mean(checkpoint_residual ** 2), atol=1e-13)
                    audit.close(tag + " eigenmin", milestone["eigenmin"], eigenvalues[0], atol=2e-12)
                    audit.close(tag + " effective kernel rate", milestone["effective_rate"], rate, atol=2e-12)
                    audit.close(tag + " training-probe gap", milestone["training_probe_gap"],
                                scalar_rms(checkpoint_probe[-m:] - checkpoint["f"]), atol=2e-7)
                    audit.close(tag + " circle readout", arrays["milestone_grids"][milestone_index], checkpoint_probe[:1024],
                                atol=2e-7, rtol=2e-12)
                    audit.check(tag + " training-probe numerical gate", milestone["training_probe_gap"] <= 1e-4)
                parts = split_state(local_state, m)
                anchors = independent_recenter(anchors, parts)
                maximum_gap = max(maximum_gap, scalar_rms(anchors["f"][-m:] - parts["f"]))
                start = local_state[:size]
                if segment < len(arrays["segment_states"]) - 1:
                    crossing = max(np.max(abs(parts["z"])) / 64,
                                   np.max(abs(parts["I"])) / 64 ** 2,
                                   np.max(abs(parts["J"])) / 64 ** 3)
                    audit.close(prefix_segment + " recenter threshold", crossing, 1., atol=2e-9, rtol=0)
            audit.close(prefix + ": final training state preserved", arrays["state"][:size], start, atol=0, rtol=0)
            audit.close(prefix + ": final local signatures zero", arrays["state"][size:], 0, atol=0, rtol=0)
            final_anchors = load_npz(run / "passive_endpoint.npz")
            audit.check(prefix + ": finite passive coefficients", all(np.isfinite(value).all() for value in final_anchors.values()))
            for key in NAMES:
                audit.close(prefix + ": independent passive replay " + key, final_anchors[key], anchors[key], atol=2e-7, rtol=2e-12)
            audit.close(prefix + ": original frozen passive Q", final_anchors["Q"], probe["Q"], atol=0, rtol=0)
            audit.close(prefix + ": independent grid replay", arrays["grid"], anchors["f"][:1024], atol=2e-7, rtol=2e-12)
            audit.close(prefix + ": independent off-grid replay", arrays["off_grid"], anchors["f"][1024:1056], atol=2e-7, rtol=2e-12)
            audit.close(prefix + ": peak training-probe gap", result["training_probe_gap"], maximum_gap, atol=2e-7, rtol=2e-8)
            measured_loss = np.mean((arrays["train_f"] - labels) ** 2)
            audit.close(prefix + ": final loss", result["loss"], measured_loss, atol=1e-14)
            audit.close(prefix + ": loss trace end", arrays["losses"][-1], measured_loss, atol=1e-14)
            audit.close(prefix + ": final time", result["time"], arrays["time"], atol=0, rtol=0)
            if result["status"] == "fitted":
                audit.close(prefix + ": fitting event", measured_loss, 1e-6, atol=1e-12, rtol=0)
                audit.check(prefix + ": first saved fitting crossing", np.all(arrays["losses"][:-1] > 1e-6))
            else:
                audit.check(prefix + ": nonfitting status retained", measured_loss > 1e-6)
        latest = "order4_resolution" + str(config["latest"])
        previous = "order4_resolution" + str(config["latest"] - 1)
        expected_gate = pair_reference(runs[previous], runs[latest], records[previous], records[latest], dense)
        for key in ("circle_rms", "numerical_change", "time_relative_change"):
            audit.close(name + ": primary gate " + key, config["gate"][key], expected_gate[key], atol=1e-11)
        audit.check(name + ": primary gate decision", config["gate"]["passed"] == expected_gate["passed"])
        check_spatial(audit, name + "/order4", runs[latest], probe, dense, config["spatial"], target / "order4_fourier.npz")
        extra_pass = True
        if number == 0:
            for extra in ("radau_crosscheck", "fresh_reproduction"):
                audit.check(name + ": required " + extra, extra in runs and extra in config["checks"])
                if extra not in runs or extra not in config["checks"]:
                    extra_pass = False
                    continue
                expected = pair_reference(runs[latest], runs[extra], records[latest], records[extra], dense)
                extra_pass = extra_pass and expected["passed"]
                for key in ("circle_rms", "numerical_change", "time_relative_change"):
                    audit.close(name + ": " + extra + " " + key,
                                config["checks"][extra]["comparison"][key], expected[key], atol=1e-11)
                audit.check(name + ": " + extra + " gate decision", config["checks"][extra]["comparison"]["passed"] == expected["passed"])
        valid = expected_gate["passed"] and config["spatial"]["quadrature_pass"] and config["spatial"]["fourier_pass"] and extra_pass
        fitted = records[latest]["status"] == "fitted"
        error = config["spatial"]["circle_rms"]
        verdict = ("no_matched_endpoint" if not fitted else "numerically_inconclusive" if not valid
                   else "agreement" if error <= .1 else "adverse" if error > .2 else "inconclusive")
        audit.check(name + ": independent final verdict", config["verdict"] == verdict)
        baseline = load_npz(target / "order2_spectral.npz")
        expected = frozen_reference(initial, probe, float(baseline["time"]))
        audit.close(name + ": spectral eigen residual", initial["Theta"] @ expected["vectors"],
                    expected["vectors"] * expected["values"], atol=1e-12)
        audit.close(name + ": spectral eigen orthogonality", expected["vectors"].T @ expected["vectors"], np.eye(m), atol=1e-12)
        audit.check(name + ": positive frozen spectrum", np.min(expected["values"]) > 0)
        audit.close(name + ": spectral training outputs", baseline["train_f"], expected["train_f"], atol=2e-12)
        audit.close(name + ": spectral residual integral", baseline["z"], expected["z"], atol=2e-7)
        audit.close(name + ": spectral training integral identity", initial["f"] + initial["Theta"] @ baseline["z"], baseline["train_f"], atol=2e-8)
        audit.close(name + ": spectral passive grid", baseline["grid"], expected["probe"][:1024], atol=2e-8)
        audit.close(name + ": spectral passive off-grid", baseline["off_grid"], expected["probe"][1024:1056], atol=2e-8)
        audit.close(name + ": spectral target", expected["loss"], 1e-6, atol=1e-12)
        before = frozen_reference(initial, probe, float(baseline["time"]) * (1 - 1e-6))
        audit.check(name + ": spectral first crossing side", before["loss"] > 1e-6 and str(baseline["status"]) == "fitted")
        check_spatial(audit, name + "/order2", baseline, probe, dense, config["order2"]["spatial"], target / "order2_fourier.npz")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path)
    parser.add_argument("--original", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    audit = Audit()
    deterministic(audit)
    if args.input:
        saved_data(audit, args.input, args.original)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    result = audit.result()
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("status", "checks", "failures")}, indent=2))
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
