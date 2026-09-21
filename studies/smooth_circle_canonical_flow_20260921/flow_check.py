"""Independent no-training numerical checks for the frozen smooth-circle study.

The closure oracle forms its implied dense matrix before differentiating, then
maps the ordinary dense matrix gradient back to M. It does not call producer
fields, derivatives, or RHS routines to construct expected numerical values.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys
import time

import numpy as np


STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
SEEDS = (20260921, 20260922, 20260923)
SPECS = (("width55", 55), ("closure1024", 1024), ("width105", 105))
TIMES = np.array([0, .01, .03, .1, .3, 1, 3, 5, 10, 20, 40, 60,
                  100, 160, 250, 400, 630, 800, 1000.], dtype=np.float64)
sys.path.insert(0, str(ROOT / "code"))
from pde import finite_network as maintained  # noqa: E402


def load_producer():
    path = STUDY / "flow_benchmark.py"
    spec = importlib.util.spec_from_file_location("smooth_flow_producer_checked", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def source_hashes():
    paths = [STUDY / "PROTOCOL.md", STUDY / "flow_benchmark.py", Path(__file__),
             ROOT / "docs/NOTATION.md", ROOT / "code/pde/finite_network.py"]
    return {str(path.relative_to(ROOT)): digest(path) for path in paths}


def independent_data(count, offset=0.0):
    theta = (2 * np.pi / count) * (np.arange(count, dtype=np.float64) + offset)
    x = np.stack((np.cos(theta), np.sin(theta)), axis=1)
    labels = np.sqrt(32 / 21) * (np.cos(theta) + np.sin(3 * theta) / 2
                                + np.cos(5 * theta) / 4)
    return dict(theta=theta, x=x, u=x / np.sqrt(2), y=labels)


def canonical_arrays(n, seed):
    generator = np.random.default_rng(seed)
    return (generator.standard_normal((n, 2)),
            generator.standard_normal((n, n)) / np.sqrt(n),
            generator.standard_normal(n) / n)


def derivative(z):
    v = np.exp(-np.abs(z))
    return (2 * v / (1 + v * v)) ** 2


def independent_bases(W, A):
    n = len(W)
    h = np.tanh(W)
    upper = np.tanh(A @ h)
    returning = np.tanh(A.T @ upper)
    raw1 = np.column_stack((np.ones(n), h, returning))
    raw2 = np.column_stack((np.ones(n), upper))
    result = {}
    for i, raw in ((1, raw1), (2, raw2)):
        gram = raw.T @ raw / n
        chol = np.linalg.cholesky(gram + np.eye(raw.shape[1]) / 4096)
        # Solving L B.T = raw.T is independent of a right inverse association.
        basis = np.linalg.solve(chol, raw.T).T
        result.update({f"rawB{i}": raw, f"chol{i}": chol, f"B{i}": basis})
    result["M0"] = result["B2"].T @ A @ result["B1"] / n
    return result


def oracle(W, middle, c, inputs, labels, B1=None, B2=None):
    """Dense-equivalent prediction and physical RHS, ordinary mean loss."""
    n, samples = len(W), len(inputs)
    effective = middle if B1 is None else B2 @ middle @ B1.T / n
    z1 = W @ inputs.T
    h1 = np.tanh(z1)
    z2 = effective @ h1
    h2 = np.tanh(z2)
    prediction = c @ h2 / n
    residual = prediction - labels
    delta2 = c[:, None] * derivative(z2)
    delta1 = derivative(z1) * (effective.T @ delta2)
    gradW = (2 / (samples * n)) * (delta1 * residual) @ inputs
    gradA = (2 / (samples * n)) * (delta2 * residual) @ h1.T
    gradc = (2 / (samples * n)) * h2 @ residual
    grad_middle = gradA if B1 is None else B2.T @ gradA @ B1 / n
    velocity = (-n * gradW, -grad_middle, -n * gradc)
    return dict(h1=h1, h2=h2, prediction=prediction,
                loss=float(np.mean(residual * residual)),
                gradients=(gradW, grad_middle, gradc), velocity=velocity,
                dissipation=float(n * np.sum(gradW * gradW)
                                  + np.sum(grad_middle * grad_middle)
                                  + n * np.sum(gradc * gradc)))


def objective(W, middle, c, inputs, labels, B1=None, B2=None):
    """Forward-only independent scalar objective for numerical differences."""
    n = len(W)
    first = np.tanh(W @ inputs.T)
    if B1 is None:
        second = np.tanh(middle @ first)
    else:
        # A different association from the dense-equivalent oracle.
        second = np.tanh(B2 @ (middle @ (B1.T @ first / n)))
    residual = c @ second / n - labels
    return float(np.dot(residual, residual) / len(labels))


def compact_oracle(W, middle, c, inputs, labels, B1=None, B2=None):
    """All-checkpoint replay; checked against dense-equivalent oracle first.

    Normalizers remain explicit at the final gradient contractions. No
    producer forward/RHS/derivative function or cache is used.
    """
    if B1 is None:
        return oracle(W, middle, c, inputs, labels)
    n, samples = len(W), len(inputs)
    z1 = W @ inputs.T
    h1 = np.tanh(z1)
    feature_sums = B1.T @ h1
    z2 = (B2 @ middle) @ feature_sums / n
    h2 = np.tanh(z2)
    prediction = h2.T @ c / n
    residual = prediction - labels
    error_at_second = c[:, None] * derivative(z2) * residual
    summed_backward = B2.T @ error_at_second
    first_error = derivative(z1) * (B1 @ (middle.T @ summed_backward))
    gradW = 2 * (first_error @ inputs) / (samples * n * n)
    grad_middle = 2 * (summed_backward @ feature_sums.T) / (samples * n * n)
    gradc = 2 * (h2 @ residual) / (samples * n)
    return dict(h1=h1, h2=h2, prediction=prediction,
                loss=float(np.mean(residual * residual)),
                gradients=(gradW, grad_middle, gradc),
                velocity=(-n * gradW, -grad_middle, -n * gradc),
                dissipation=float(n * np.sum(gradW * gradW)
                                  + np.sum(grad_middle * grad_middle)
                                  + n * np.sum(gradc * gradc)))


class Checks:
    def __init__(self):
        self.items = []

    def gate(self, name, passed, **detail):
        self.items.append(dict(name=name, passed=bool(passed), **detail))

    def close(self, name, actual, expected, atol=2e-12, rtol=2e-10):
        a, b = np.asarray(actual), np.asarray(expected)
        if a.shape != b.shape:
            self.gate(name, False, actual_shape=list(a.shape), expected_shape=list(b.shape))
            return
        error = np.abs(a - b)
        finite = np.isfinite(a).all() and np.isfinite(b).all()
        self.gate(name, finite and np.all(error <= atol + rtol * np.abs(b)),
                  maximum_absolute_error=float(np.max(error, initial=0.0)),
                  atol=atol, rtol=rtol)

    @property
    def passed(self):
        return all(item["passed"] for item in self.items)


def compare_state(checks, prefix, model, packed, data):
    W, middle, c = model.unpack(packed)
    expected = oracle(W, middle, c, data["u"], data["y"], model.B1, model.B2)
    compact = compact_oracle(W, middle, c, data["u"], data["y"], model.B1, model.B2)
    for key in ("h1", "h2", "prediction", "loss", "dissipation"):
        checks.close(prefix + "/compact_oracle_" + key, compact[key], expected[key])
    for key, left, right in zip(("W", "middle", "c"), compact["velocity"], expected["velocity"]):
        checks.close(prefix + "/compact_oracle_rhs_" + key, left, right)
    actual_fields = model.fields(packed, data["u"])
    for field, actual in zip(("h1", "h2", "prediction"), actual_fields):
        checks.close(prefix + "/" + field, actual, expected[field])
    rhs = model.unpack(model.rhs(0.0, packed, data["u"], data["y"]))
    for block, actual, reference in zip(("W", "middle", "c"), rhs, expected["velocity"]):
        checks.close(prefix + "/rhs_" + block, actual, reference)
    identity = -(sum(float(np.sum(g * v)) for g, v in zip(expected["gradients"], rhs)))
    checks.close(prefix + "/dissipation", identity, expected["dissipation"])
    checks.close(prefix + "/prediction_oddness", model.predict(packed, -data["u"]),
                 -expected["prediction"], atol=5e-13, rtol=0)
    if model.B1 is None:
        params = maintained.Parameters((W, middle), c)
        reference = maintained.flow_velocity(params, (data["u"] * np.sqrt(2)).T, data["y"])
        for name, actual, ref in zip(("W", "middle", "c"), rhs,
                                     (*reference.weights, reference.readout)):
            checks.close(prefix + "/maintained_rhs_" + name, actual, ref)
    return expected


def check_differences(checks, prefix, model, packed, data, expected):
    blocks = tuple(v.copy() for v in model.unpack(packed))
    random = np.random.default_rng(701)
    for index, name in enumerate(("W", "middle", "c")):
        gradient = expected["gradients"][index]
        for kind in ("aligned", "random"):
            direction = gradient.copy() if kind == "aligned" else random.standard_normal(gradient.shape)
            direction /= np.linalg.norm(direction)
            analytic = float(np.sum(gradient * direction))
            attempts = []
            for epsilon in (1e-4, 3e-5, 1e-5):
                plus, minus = [v.copy() for v in blocks], [v.copy() for v in blocks]
                plus[index] += epsilon * direction
                minus[index] -= epsilon * direction
                numerical = (objective(*plus, data["u"], data["y"], model.B1, model.B2)
                             - objective(*minus, data["u"], data["y"], model.B1, model.B2)) / (2 * epsilon)
                attempts.append(dict(epsilon=epsilon, numerical=numerical,
                                     absolute_error=abs(numerical - analytic)))
            allowed = max(1e-9, 1e-6 * abs(analytic))
            checks.gate(prefix + "/finite_difference_" + name + "_" + kind,
                        min(a["absolute_error"] for a in attempts) <= allowed,
                        analytic=analytic, allowed_absolute_error=allowed, attempts=attempts)
    velocity = expected["velocity"]
    norm = np.sqrt(sum(np.sum(v * v) for v in velocity))
    epsilon = 1e-5 / max(norm, 1.0)
    plus = [v + epsilon * dv for v, dv in zip(blocks, velocity)]
    minus = [v - epsilon * dv for v, dv in zip(blocks, velocity)]
    numerical = (objective(*plus, data["u"], data["y"], model.B1, model.B2)
                 - objective(*minus, data["u"], data["y"], model.B1, model.B2)) / (2 * epsilon)
    analytic = -expected["dissipation"]
    checks.gate(prefix + "/finite_difference_dissipation",
                abs(numerical - analytic) <= max(1e-9, 1e-6 * abs(analytic)),
                numerical=numerical, analytic=analytic, epsilon=float(epsilon),
                absolute_error=abs(numerical - analytic))


def preflight(output_dir):
    started = time.monotonic()
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=False)
    producer = load_producer()
    checks = Checks()
    checks.close("protocol/checkpoints", producer.CHECKPOINTS, TIMES, atol=0, rtol=0)
    checks.gate("protocol/levels", producer.LEVELS == {
        "primary": {"rtol": 1e-6, "atol": 1e-9, "max_step": 2.0},
        "fine": {"rtol": 1e-8, "atol": 1e-11, "max_step": 1.0},
        "finer": {"rtol": 1e-10, "atol": 1e-13, "max_step": .5}})
    checks.gate("protocol/ridge", producer.RIDGE == 1 / 4096)
    train = independent_data(126)
    actual_data = producer.circle_data(126)
    for field in ("theta", "x", "u", "y"):
        checks.close("data/" + field, actual_data[field], train[field], atol=5e-13, rtol=0)
    for name, value, expected in (
        ("target_mean_square", np.mean(train["y"] ** 2), 1.0),
        ("input_norm_squared", np.sum(train["u"] ** 2, axis=1), np.full(126, .5)),
        ("target_oddness", train["y"][:63] + train["y"][63:], np.zeros(63)),
        ("input_oddness", train["u"][:63] + train["u"][63:], np.zeros((63, 2))),
    ):
        checks.close("data/" + name, value, expected, atol=5e-13, rtol=0)
    for name, n in SPECS:
        for seed in SEEDS:
            prefix = f"{name}/{seed}"
            model = producer.build_model(name, seed)
            passive = independent_data(1024, .5)
            for field in ("theta", "x", "u", "y"):
                checks.close(prefix + "/passive_" + field, model.passive[field], passive[field],
                             atol=5e-13, rtol=0)
            W, A, c = canonical_arrays(n, seed)
            reference = maintained.initialize(n, 2, 2, seed=seed)
            for key, actual, expected, established in (
                ("W0", model.W0, W, reference.weights[0]),
                ("A0", model.A0, A, reference.weights[1]),
                ("c0", model.c0, c, reference.readout),
            ):
                checks.gate(prefix + "/canonical_" + key,
                            np.array_equal(actual, expected) and np.array_equal(actual, established))
            packed = model.initial
            initial = model.unpack(packed)
            checks.close(prefix + "/initial_W", initial[0], W, atol=0, rtol=0)
            checks.close(prefix + "/initial_c", initial[2], c, atol=0, rtol=0)
            expected_trainable = n * n + 3 * n if model.B1 is None else 3 * n + 15
            checks.gate(prefix + "/trainable_count", packed.size == expected_trainable,
                        actual=int(packed.size), expected=expected_trainable)
            if model.B1 is not None:
                bases = independent_bases(W, A)
                for key, expected in bases.items():
                    checks.close(prefix + "/basis_" + key, getattr(model, key), expected,
                                 atol=2e-13, rtol=2e-12)
                checks.close(prefix + "/initial_M", initial[1], bases["M0"], atol=2e-13, rtol=2e-12)
                checks.gate(prefix + "/retained_count", packed.size + model.B1.size + model.B2.size == 11279)
                for i in (1, 2):
                    basis, chol = bases[f"B{i}"], bases[f"chol{i}"]
                    inverse = np.linalg.solve(chol, np.eye(len(chol)))
                    checks.close(prefix + f"/ridge_whitening_{i}", basis.T @ basis / n,
                                 np.eye(len(chol)) - inverse @ inverse.T / 4096,
                                 atol=2e-13, rtol=2e-12)
            else:
                checks.close(prefix + "/initial_A", initial[1], A, atol=0, rtol=0)
            compare_state(checks, prefix + "/initial", model, packed, train)
            if seed == SEEDS[0]:
                generator = np.random.default_rng(314159)
                W_test = W + .07 * generator.standard_normal(W.shape)
                middle_test = initial[1] + .04 * generator.standard_normal(initial[1].shape)
                c_test = .3 * generator.standard_normal(c.shape)
                synthetic = model.pack(W_test, middle_test, c_test)
                expected = compare_state(checks, prefix + "/synthetic", model, synthetic, train)
                check_differences(checks, prefix + "/synthetic", model, synthetic, train, expected)
                # A zero residual must give exactly zero velocity for every block.
                labels = model.predict(synthetic, train["u"])
                checks.close(prefix + "/zero_residual_rhs",
                             model.rhs(0, synthetic, train["u"], labels),
                             np.zeros_like(synthetic), atol=0, rtol=0)
                if model.B1 is None:
                    # These large readouts amplify an otherwise tiny saturated
                    # derivative enough to catch 1-tanh(z)^2 cancellation.
                    one = dict(u=np.array([[1 / np.sqrt(2), 0.0]]), y=np.zeros(1))
                    saturated_W = np.zeros_like(W)
                    saturated_W[:, 0] = 20 * np.sqrt(2)
                    for location in ("first", "second"):
                        test_W = saturated_W if location == "first" else saturated_W / 40
                        test_A = np.eye(n) if location == "first" else np.eye(n) * (20 / np.tanh(.5))
                        test_c = np.full(n, 1e8)
                        saturation = model.pack(test_W, test_A, test_c)
                        compare_state(checks, prefix + "/saturation_" + location,
                                      model, saturation, one)
    result = dict(status="PASS" if checks.passed else "FAIL", passed=checks.passed,
                  producer_sha256=digest(STUDY / "flow_benchmark.py"),
                  protocol_sha256=digest(STUDY / "PROTOCOL.md"),
                  checker_sha256=digest(Path(__file__)), checks=checks.items,
                  source_hashes=source_hashes(), wall_seconds=time.monotonic() - started,
                  environment=dict(python=platform.python_version(), numpy=np.__version__,
                                   executable=sys.executable,
                                   threads={key: os.environ.get(key) for key in
                                            ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")}),
                  scope="deterministic preflight only; no integration or trajectory claim")
    (output_dir / "preflight.json").write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    return result


def unpack_saved(state, n, closure):
    count = 15 if closure else n * n
    expected = 3 * n + count
    if state.shape != (expected,):
        raise ValueError("wrong saved state shape")
    shape = (3, 5) if closure else (n, n)
    return state[:2*n].reshape(n, 2), state[2*n:2*n+count].reshape(shape), state[2*n+count:]


def audit_run(run_dir, output_dir=None):
    """Replay every retained checkpoint and the final state; never integrate."""
    started = time.monotonic()
    run_dir = Path(run_dir).resolve()
    run_dir.relative_to(ROOT / "data/generated" / STUDY.name)
    checks = Checks()
    result = dict(run_id=run_dir.name, directory=str(run_dir), passed=False,
                  completed=False, checkpoint_count=0, output_hashes_verified=False)
    try:
        record = json.loads((run_dir / "result.json").read_text())
        config = json.loads((run_dir / "config.json").read_text())
        result["result_sha256"] = digest(run_dir / "result.json")
        result["completed"] = record["status"] == "completed"
        n = dict(SPECS)[config["model"]]
        closure = config["model"] == "closure1024"
        checks.gate("config/seed", config["seed"] in SEEDS)
        checks.gate("config/mobilities", config["mobilities"] == [n, 1, n])
        checks.close("config/checkpoints", config["checkpoints"], TIMES, atol=0, rtol=0)
        result["source_hashes"] = record["source_sha256"]
        for path in (STUDY / "flow_benchmark.py", STUDY / "PROTOCOL.md", ROOT / "code/pde/finite_network.py"):
            checks.gate("source_hash/" + path.name,
                        record["source_sha256"].get(str(path)) == digest(path))
        hash_passes = []
        for filename, expected_hash in record["output_sha256"].items():
            path = run_dir / filename
            path.resolve().relative_to(run_dir)
            good = path.is_file() and digest(path) == expected_hash
            checks.gate("output_hash/" + filename, good)
            hash_passes.append(good)
        result["output_hashes_verified"] = bool(hash_passes and all(hash_passes))
        with np.load(run_dir / "source.npz", allow_pickle=False) as archive:
            source = {key: archive[key].copy() for key in archive.files}
        W0, A0, c0 = canonical_arrays(n, config["seed"])
        for key, expected in (("W0", W0), ("A0", A0), ("c0", c0)):
            checks.gate("canonical/" + key, np.array_equal(source[key], expected))
        train, passive = independent_data(126), independent_data(1024, .5)
        for name, data in (("train", train), ("passive", passive)):
            for key, expected in data.items():
                checks.close("data/" + name + "_" + key, source[name + "_" + key], expected,
                             atol=5e-13, rtol=0)
        bases = independent_bases(W0, A0) if closure else {}
        for key, expected in bases.items():
            checks.close("basis/" + key, source[key], expected, atol=2e-13, rtol=2e-12)
        B1, B2 = bases.get("B1"), bases.get("B2")
        middle0 = bases["M0"] if closure else A0
        initial = np.concatenate((W0.ravel(), middle0.ravel(), c0))
        checks.close("initial_state", source["initial_state"], initial, atol=2e-13, rtol=2e-12)
        baseline = compact_oracle(W0, middle0, c0, train["u"], train["y"], B1, B2)

        def replay_snapshot(prefix, snapshot):
            W, middle, c = unpack_saved(snapshot["state"], n, closure)
            expected = compact_oracle(W, middle, c, train["u"], train["y"], B1, B2)
            passive_expected = compact_oracle(W, middle, c, passive["u"], passive["y"], B1, B2)
            checks.close(prefix + "/train_prediction", snapshot["train_prediction"], expected["prediction"],
                         atol=1e-9, rtol=0)
            checks.close(prefix + "/passive_prediction", snapshot["passive_prediction"], passive_expected["prediction"],
                         atol=1e-9, rtol=0)
            checks.close(prefix + "/train_loss", snapshot["train_loss"], expected["loss"], atol=1e-10, rtol=0)
            checks.close(prefix + "/passive_loss", snapshot["passive_loss"], passive_expected["loss"], atol=1e-10, rtol=0)
            rhs = np.concatenate(tuple(value.ravel() for value in expected["velocity"]))
            checks.close(prefix + "/rhs", snapshot["rhs"], rhs)
            checks.close(prefix + "/dissipation", snapshot["dissipation"], expected["dissipation"])
            motion = np.array([np.sqrt(np.mean((expected[key] - baseline[key]) ** 2)) for key in ("h1", "h2")])
            checks.close(prefix + "/hidden_rms_displacement", snapshot["hidden_rms_displacement"], motion,
                         atol=1e-9, rtol=0)
            return expected

        with np.load(run_dir / "checkpoints.npz", allow_pickle=False) as archive:
            saved = {key: archive[key] for key in archive.files}
        count = len(saved["times"])
        result["checkpoint_count"] = count
        checks.close("checkpoint_times", saved["times"], TIMES[:count], atol=0, rtol=0)
        if result["completed"]:
            checks.gate("completed_checkpoint_count", count == len(TIMES))
        checks.gate("checkpoint_initial_state", count > 0
                    and np.array_equal(saved["states"][0], source["initial_state"]))
        for index in range(count):
            snapshot = {key: value[index] for key, value in saved.items() if key not in ("times", "states")}
            snapshot["state"] = saved["states"][index]
            replay_snapshot(f"checkpoint{index}", snapshot)
        with np.load(run_dir / "final.npz", allow_pickle=False) as archive:
            final = {key: archive[key] for key in archive.files}
        final_expected = replay_snapshot("final", final)
        checks.close("final/time", final["time"], record["physical_time"], atol=0, rtol=0)
        checks.close("final/result_loss", record["final_loss"], final_expected["loss"], atol=1e-10, rtol=0)
        with (run_dir / "accepted_steps.csv").open() as stream:
            rows = list(csv.DictReader(stream))
        step_times = np.array([float(row["time"]) for row in rows])
        losses = np.array([float(row["loss"]) for row in rows])
        checks.gate("accepted_trace_finite", np.isfinite(step_times).all() and np.isfinite(losses).all())
        checks.gate("accepted_trace_times", len(step_times) > 0 and step_times[0] == 0
                    and np.all(np.diff(step_times) > 0))
        checks.close("accepted_trace_final_time", step_times[-1], final["time"], atol=0, rtol=0)
        checks.close("accepted_trace_final_loss", losses[-1], final_expected["loss"], atol=1e-10, rtol=0)
        result["max_relative_loss_increase"] = (float(np.max(np.maximum(np.diff(losses), 0)
                                                   / np.maximum(1, losses[:-1]))) if len(losses) > 1 else 0.)
        result["passed"] = checks.passed
    except (OSError, KeyError, ValueError, IndexError, FloatingPointError) as error:
        result["error"] = type(error).__name__ + ": " + str(error)
    result.update(checks=checks.items, wall_seconds=time.monotonic() - started)
    if output_dir is not None:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=False)
        (output_dir / "audit.json").write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    return result


def replay(campaign, output_dir):
    started = time.monotonic()
    campaign, output_dir = Path(campaign).resolve(), Path(output_dir)
    campaign.relative_to(ROOT / "data/generated" / STUDY.name)
    output_dir.mkdir(parents=True, exist_ok=False)
    manifest = json.loads((campaign / "run_record.json").read_text())
    runs = [audit_run(item["directory"]) for item in manifest["attempts"]]
    result = dict(passed=bool(runs) and all(run["passed"] for run in runs),
                  campaign=str(campaign), runs=runs,
                  producer_sha256=digest(STUDY / "flow_benchmark.py"),
                  protocol_sha256=digest(STUDY / "PROTOCOL.md"),
                  checker_sha256=digest(Path(__file__)), wall_seconds=time.monotonic() - started,
                  scope="all retained predictions, losses and RHS replayed; completeness/refinement separate")
    (output_dir / "replay.json").write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("preflight", "replay", "audit"))
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--campaign", type=Path)
    parser.add_argument("--run", type=Path)
    args = parser.parse_args()
    if args.action == "preflight":
        result = preflight(args.output)
    elif args.action == "replay":
        result = replay(args.campaign, args.output)
    else:
        result = audit_run(args.run, args.output)
    print(json.dumps({key: result[key] for key in ("passed", "wall_seconds")}, allow_nan=False))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
