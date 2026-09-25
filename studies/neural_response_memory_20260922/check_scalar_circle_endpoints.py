"""Independent deterministic checks and saved endpoint rescoring; no research runs."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
TENSOR_NAMES = ("f", "Theta", "C", "Q")


def rms(value):
    return float(np.sqrt(np.mean(np.abs(value) ** 2)))


class Audit:
    def __init__(self):
        self.checks = 0
        self.failures = []
        self.maximum_discrepancy = 0.
        self.maximum_roundoff_fraction = 0.

    def check(self, condition, description):
        self.checks += 1
        if not condition:
            self.failures.append(description)

    def close(self, actual, expected, description, atol=2e-10, rtol=2e-9):
        actual, expected = np.asarray(actual), np.asarray(expected)
        same_shape = actual.shape == expected.shape
        if same_shape and actual.size:
            difference = float(np.max(np.abs(actual - expected)))
            if np.isfinite(difference):
                self.maximum_discrepancy = max(self.maximum_discrepancy, difference)
        self.check(same_shape and np.allclose(actual, expected, atol=atol, rtol=rtol), description)

    def bounded(self, actual, expected, bound, description):
        difference = np.abs(np.asarray(actual) - np.asarray(expected))
        self.maximum_discrepancy = max(self.maximum_discrepancy, float(np.max(difference)))
        self.maximum_roundoff_fraction = max(self.maximum_roundoff_fraction,
                                             float(np.max(difference / bound)))
        self.check(np.all(difference <= bound), description)

    def result(self):
        return dict(checks=self.checks, failures=self.failures,
                    maximum_discrepancy=self.maximum_discrepancy,
                    maximum_roundoff_fraction=self.maximum_roundoff_fraction,
                    passed=not self.failures)


def scalar_readout(coefficients, state, m, order, high_precision=False):
    """Literal independent contractions, without importing the probe engine."""
    if high_precision:
        coefficients = {key: np.asarray(coefficients[key], dtype=(np.clongdouble
                        if np.iscomplexobj(coefficients[key]) else np.longdouble))
                        for key in TENSOR_NAMES[:order]}
        state = np.asarray(state, dtype=np.longdouble)
    start = m if order == 2 else m + m*m + m*m*m
    z = state[start:start+m]
    result = coefficients["f"] + np.einsum("qb,b->q", coefficients["Theta"], z)
    if order == 4:
        start += m
        integral = state[start:start+m*m].reshape(m, m)
        start += m*m
        triple = state[start:start+m*m*m].reshape(m, m, m)
        result = result + np.einsum("qbc,bc->q", coefficients["C"], integral)
        result = result + np.einsum("qbcd,bcd->q", coefficients["Q"], triple)
    return result


def readout_roundoff_bound(coefficients, state, m, order):
    """Conservative gamma_n absolute-sum bound for each saved float64 contraction.

    Bounds summation/multiplication roundoff on the saved inputs, not ODE,
    coefficient, model, or continuum error. Complex products receive a further
    factor four. Long-double evaluation supplies the independent reference.
    """
    magnitude = scalar_readout({key: np.abs(coefficients[key]) for key in TENSOR_NAMES[:order]},
                               np.abs(state), m, order, high_precision=True)
    terms = sum(m**degree for degree in range(order))
    operations = 8*terms+32
    eps = np.finfo(float).eps
    gamma = operations*eps/(1-operations*eps)
    return gamma*np.maximum(1., magnitude)


def dense_readout(state, inputs, width):
    """Independent dense forward calculation for the fixed three-hidden model."""
    start, value = 0, inputs.T
    for columns in (2, width, width):
        stop = start + width*columns
        value = np.tanh(state[start:stop].reshape(width, columns) @ value)
        start = stop
    return state[start:start+width] @ value / width


def fourier_value(modes, angles):
    """Independent real cosine/sine evaluation of normalized positive modes."""
    phase = np.outer(angles, np.arange(1, len(modes)))
    return modes[0].real + 2*(np.cos(phase) @ modes[1:].real
                              - np.sin(phase) @ modes[1:].imag)


def deterministic_checks(audit):
    import scalar_aggregate_engine as original
    import scalar_circle_probe_engine as probe
    import run_scalar_circle_endpoints as runner

    rng = np.random.default_rng(71021)
    train, points = rng.normal(size=(2, 2)), rng.normal(size=(3, 2))
    # Non-small readout makes ordered moving-direction contributions observable.
    params = tuple(rng.normal(size=shape)*.3 for shape in ((3, 2), (3, 3), (3, 3), (3,)))
    joint = np.vstack((train, points))
    full = original.initialize_coefficients(params, joint, order=4)
    cross = probe.initialize_probe_coefficients(params, train, points, order=4)
    slices = {"f": (slice(2, None),), "Theta": (slice(2, None), slice(2)),
              "C": (slice(2, None), slice(2), slice(2)),
              "Q": (slice(2, None), slice(2), slice(2), slice(2))}
    for key in TENSOR_NAMES:
        audit.close(cross[key], full[key][slices[key]], "tiny cross tensor " + key)
    training = original.initialize_coefficients(params, train, order=4)
    labels = np.array([.2, -.4])
    for order in (2, 4):
        model = probe.SignatureHierarchy(training, labels, order=order)
        state = model.initial_state() + rng.normal(size=model.size)*.015
        before = model.rhs(0., state)
        audit.close(before[:model.training_size], model.training.rhs(0., state[:model.training_size]),
                    "training RHS unchanged order " + str(order))
        audit.close(model.readout(cross, state), scalar_readout(cross, state, 2, order),
                    "literal ordered signature readout order " + str(order))
        disabled = lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("neural runtime access"))
        old_fields, old_forward = probe._fields, probe.forward_only
        probe._fields, probe.forward_only = disabled, disabled
        try:
            audit.close(model.rhs(0., state), before, "runtime neural independence order " + str(order))
            audit.close(model.readout(cross, state), scalar_readout(cross, state, 2, order),
                        "readout neural independence order " + str(order))
        finally:
            probe._fields, probe.forward_only = old_fields, old_forward
    angles = 2*np.pi*np.arange(64)/64
    query = rng.uniform(-8., 8., 23)
    samples = .31 + .42*np.cos(3*angles) - .27*np.sin(7*angles)
    expected = .31 + .42*np.cos(3*query) - .27*np.sin(7*query)
    modes = probe.fit_fourier(samples, 7)
    audit.close(probe.evaluate_fourier(modes, query), expected, "analytic Fourier fixture")
    audit.close(fourier_value(modes, query), expected, "independent Fourier fixture")
    # A deterministic one-dimensional ODE, not a neural research trajectory.
    arrays, receipt = runner.integrate_endpoint(lambda t, y: -y, np.array([1.]),
        lambda y: y, np.array([0.]), 1e-9, 3.)
    audit.check(receipt["status"] == "fitted", "analytic decay endpoint status")
    audit.close(arrays["time"], np.log(1000.), "analytic decay event time", atol=1e-7)
    audit.close(receipt["loss"], 1e-6, "analytic decay event loss", atol=1e-12)
    arrays, receipt = runner.integrate_endpoint(lambda t, y: -y, np.array([0.]),
        lambda y: y, np.array([0.]), 1e-9, 3.)
    audit.check(receipt["status"] == "fitted" and receipt["time"] == 0.,
                "initially fitted endpoint stops at zero")


def load_npz(path):
    with np.load(path, allow_pickle=False) as data:
        return {key: data[key] for key in data.files}


def audit_configuration(directory, audit):
    summary = json.loads((directory / "summary.json").read_text())
    meta, latest = summary["configuration"], summary["latest"]
    m, width = meta["M"], meta["width"]
    initial = load_npz(directory / "initial_coefficients.npz")
    refined = (directory / "probe_coefficients_refined.npz").exists()
    probes = load_npz(directory / ("probe_coefficients_refined.npz" if refined else "probe_coefficients.npz"))
    count, angles, off_angles = len(probes["angles"]), probes["angles"], probes["off_angles"]
    inputs, labels = initial["inputs"], initial["labels"]
    audit.close(probes["probe_inputs"][:count], np.column_stack((np.cos(angles), np.sin(angles))),
                directory.name + " probe input normalization")
    audit.close(angles, 2*np.pi*np.arange(count)/count, directory.name + " uniform angles")
    for key in TENSOR_NAMES:
        audit.close(probes[key][-m:], initial[key], directory.name + " training probe coefficient " + key)
    runs, records = {}, {}
    for name in ("dense", "order2", "order4"):
        for level in range(latest[name]+1):
            stem = name + ("_spatial_refined_resolution" if refined else "_resolution") + str(level)
            run = load_npz(directory / (stem + ".npz"))
            record = json.loads((directory / (name + "_resolution" + str(level) + ".json")).read_text())
            runs[name, level], records[name, level] = run, record
            identity = directory.name + "/" + name + "/" + str(level)
            values = (dense_readout(run["state"], probes["probe_inputs"], width) if name == "dense"
                      else scalar_readout(probes, run["state"], m, int(name[-1]), high_precision=True))
            bounds = None if name == "dense" else readout_roundoff_bound(probes, run["state"], m, int(name[-1]))
            for key, expected in (("grid", values[:count]), ("off_grid", values[count:count+32]),
                                  ("train_probe", values[-m:])):
                if bounds is None:
                    audit.close(run[key], expected, identity + " reconstructed " + key)
                else:
                    bound = bounds[:count] if key == "grid" else bounds[count:count+32] if key == "off_grid" else bounds[-m:]
                    audit.bounded(run[key], expected, bound, identity + " reconstructed " + key)
            train_f = dense_readout(run["state"], inputs, width) if name == "dense" else run["state"][:m]
            audit.close(run["train_f"], train_f, identity + " training predictions")
            loss = np.mean((train_f-labels)**2)
            audit.close(record["loss"], loss, identity + " loss receipt", atol=2e-12)
            audit.close(record["time"], run["time"], identity + " endpoint time")
            audit.close(run["times"][-1], run["time"], identity + " history ends at endpoint")
            audit.close(run["losses"][-1], loss, identity + " history endpoint loss", atol=2e-12)
            audit.check(np.all(np.diff(run["times"]) > 0), identity + " chronological history")
            audit.check(all(np.isfinite(run[key]).all() for key in run), identity + " finite arrays")
            audit.check(record["rtol"] == (1e-7, 1e-9, 1e-11)[level] and record["max_step"] == 2.,
                        identity + " frozen solver settings")
            if record["status"] == "fitted":
                audit.close(loss, 1e-6, identity + " fitted threshold", atol=5e-11)
                audit.check(np.all(run["losses"][:-1] > 1e-6), identity + " no earlier saved threshold crossing")
            audit.close(record["training_readout_gap"], rms(run["train_probe"]-train_f),
                        identity + " training readout gap receipt", atol=2e-12)
    dense = runs["dense", latest["dense"]]
    rescored = {}
    for name in ("order2", "order4"):
        level, dl = latest[name], latest["dense"]
        scalar, recorded = runs[name, level], summary["models"][name]
        error = rms(scalar["grid"]-dense["grid"])
        dense_rms = rms(dense["grid"])
        numerical = []
        for key, last, field in ((name, level, "scalar_gate"), ("dense", dl, "dense_gate")):
            change = rms(runs[key, last-1]["grid"]-runs[key, last]["grid"])
            passed = change <= .002 and change <= .1*max(error, 1e-6)
            audit.close(recorded[field]["change"], change, directory.name + " " + name + " " + field)
            audit.check(recorded[field]["passed"] == passed, directory.name + " " + name + " " + field + " decision")
            numerical.append(passed)
        spatial_change = abs(error-rms((scalar["grid"]-dense["grid"])[::2]))
        spatial_ok = spatial_change <= .001 and spatial_change <= .01*max(error, 1e-6)
        audit.close(recorded["quadrature"]["change"], spatial_change, directory.name + " " + name + " quadrature")
        audit.check(recorded["quadrature"]["passed"] == spatial_ok, directory.name + " " + name + " quadrature decision")
        fc = load_npz(directory / (name + "_fourier.npz"))
        endpoint = scalar_readout(fc, scalar["state"], m, int(name[-1]), high_precision=True)
        audit.bounded(fc["endpoint"], endpoint, readout_roundoff_bound(fc, scalar["state"], m, int(name[-1])),
                      directory.name + " " + name + " Fourier contraction")
        fg, fo = fourier_value(fc["endpoint"], angles), fourier_value(fc["endpoint"], off_angles)
        audit.close(fc["endpoint_grid"], fg, directory.name + " " + name + " Fourier grid")
        audit.close(fc["endpoint_off_grid"], fo, directory.name + " " + name + " Fourier off-grid")
        grid_error, off_error = fg-scalar["grid"], fo-scalar["off_grid"]
        fourier_ok = (rms(grid_error) <= 1e-5 and rms(off_error) <= 1e-5
                      and np.max(np.abs(grid_error)) <= 1e-4 and np.max(np.abs(off_error)) <= 1e-4)
        audit.check(recorded["fourier"]["passed"] == fourier_ok,
                    directory.name + " " + name + " separate Fourier grid/off-grid gates")
        for key, value in (("circle_rms", error), ("dense_function_rms", dense_rms),
                           ("relative_rms", error/dense_rms),
                           ("maximum_grid_error", np.max(np.abs(scalar["grid"]-dense["grid"])))):
            audit.close(recorded[key], value, directory.name + " " + name + " metric " + key)
        fitted = records[name, level]["status"] == records["dense", dl]["status"] == "fitted"
        statuses_match = (records[name, level-1]["status"] == records[name, level]["status"]
                          and records["dense", dl-1]["status"] == records["dense", dl]["status"])
        valid = all(numerical) and spatial_ok and fourier_ok and statuses_match
        verdict = ("no_matched_endpoint" if not fitted else "numerically_inconclusive" if not valid
                   else "agreement" if error <= .1 else "adverse" if error > .2 else "inconclusive")
        audit.check(recorded["fitted_pair"] == fitted, directory.name + " " + name + " fitted pair")
        audit.check(recorded["valid"] == valid, directory.name + " " + name + " validity")
        audit.check(recorded["verdict"] == verdict, directory.name + " " + name + " verdict")
        rescored[name] = dict(circle_rms=error, verdict=verdict, fourier_grid_rms=rms(grid_error),
                              fourier_off_grid_rms=rms(off_error))
    return rescored


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--deterministic", action="store_true")
    parser.add_argument("--runs", type=Path)
    parser.add_argument("--reproduction", type=Path)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    if not args.deterministic and args.runs is None:
        parser.error("select --deterministic and/or --runs")
    if args.reproduction is not None and args.runs is None:
        parser.error("--reproduction requires --runs")
    audit, configurations = Audit(), {}
    if args.deterministic:
        deterministic_checks(audit)
    if args.runs is not None:
        manifest = json.loads((args.runs / "manifest.json").read_text())
        for name, expected in manifest["source_hashes"].items():
            path = args.runs / "sources" / name
            audit.check(hashlib.sha256(path.read_bytes()).hexdigest() == expected, "frozen source hash " + name)
        for directory in sorted(args.runs.iterdir()):
            if directory.is_dir() and (directory / "summary.json").exists():
                configurations[directory.name] = audit_configuration(directory, audit)
    reproduction = {}
    if args.reproduction is not None:
        primary_manifest = json.loads((args.runs / "manifest.json").read_text())
        repeat_manifest = json.loads((args.reproduction / "manifest.json").read_text())
        audit.check(primary_manifest["source_hashes"] == repeat_manifest["source_hashes"],
                    "reproduction uses identical frozen producer sources")
        for directory in sorted(args.reproduction.iterdir()):
            if directory.is_dir() and (directory / "summary.json").exists():
                reproduction[directory.name] = audit_configuration(directory, audit)
                original = args.runs / directory.name
                for path in sorted(directory.glob("*.npz")):
                    first, second = load_npz(original/path.name), load_npz(path)
                    audit.check(set(first) == set(second), "reproduction array keys " + path.name)
                    for key in first:
                        audit.check(np.array_equal(first[key], second[key]),
                                    "bit-identical reproduction " + path.name + "/" + key)
    result = dict(**audit.result(), configurations=configurations, reproduction=reproduction,
                  checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(rendered)
    print(rendered, end="")
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
