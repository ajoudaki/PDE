"""Independent bounded CPU checks and saved-state replay for the deep circle run.

No training campaign is launched. The dense oracle is the maintained NumPy
finite_network module, loaded directly to keep the scientific input scope fixed.
Replay constructs both physical matrices independently and evaluates all saved
panels without calling the experiment engine's forward implementation.
"""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys
import time

import numpy as np
import torch

from deep_moment_engine import DeepDenseEngine, DeepMomentEngine, controlled_error
from deep_circle_run import heun_trial


STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parent.parent
spec = importlib.util.spec_from_file_location("deep_circle_numpy_oracle", ROOT / "code/pde/finite_network.py")
oracle = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = oracle
spec.loader.exec_module(oracle)


def digest(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for part in iter(lambda: stream.read(1 << 20), b""):
            value.update(part)
    return value.hexdigest()


def array_digest(*arrays):
    value = hashlib.sha256()
    for item in arrays:
        item = np.asarray(item)
        value.update(str(item.shape).encode())
        value.update(str(item.dtype).encode())
        value.update(item.tobytes(order="C"))
    return value.hexdigest()


def npv(value):
    return value.detach().cpu().numpy() if isinstance(value, torch.Tensor) else np.asarray(value)


def close(actual, expected, atol=1e-11, rtol=1e-10):
    actual, expected = npv(actual), npv(expected)
    np.testing.assert_allclose(actual, expected, atol=atol, rtol=rtol)
    return float(np.max(np.abs(actual - expected), initial=0))


def reconstruct(state, layer):
    """Literal indexwise formula, independent of factor flattening/order."""
    a, b = npv(getattr(state, "A" + str(layer))), npv(getattr(state, "B" + str(layer)))
    p, n, m = a.shape
    return -2 / (m * n * (1 + float(state.s))) * sum(
        (2 * k + 1) * np.outer(a[k, :, j], b[k, :, j])
        for k in range(p) for j in range(m))


def checks():
    result = {}
    gen = np.random.default_rng(837492)
    for n, d, m in ((1, 1, 1), (11, 3, 5), (17, 2, 3)):
        u, y = gen.normal(size=(m, d)), gen.normal(size=m)
        dense = DeepDenseEngine(d, n, u, y, seed=712)
        initial = oracle.initialize(n, 3, d, seed=712)
        for got, wanted in zip(dense.initial_state().tensors(), initial.weights + (initial.readout,)):
            close(got, wanted, 0, 0)
        state = dense.initial_state()
        for value in state.tensors():
            value.add_(torch.tensor(gen.normal(scale=.2, size=value.shape)))
        physical = oracle.Parameters(tuple(npv(getattr(state, k)) for k in ("w", "W2", "W3")), npv(state.c))
        raw_x = np.sqrt(d) * u.T
        vel = oracle.flow_velocity(physical, raw_x, y)
        errors = [close(got, wanted) for got, wanted in zip(dense.rhs(state).tensors(), vel.weights + (vel.readout,))]
        close(dense.predict(state, u), oracle.forward(physical, raw_x).output)
        for k, backward in enumerate(oracle.backward(physical, raw_x), 1):
            close(dense.fields(state)["delta" + str(k)], backward)
        # Repetition preserves mean loss and physical velocity, not just output.
        duplicate = DeepDenseEngine(d, n, np.tile(u, (3, 1)), np.tile(y, 3), seed=712)
        for got, wanted in zip(duplicate.rhs(state).tensors(), dense.rhs(state).tensors()):
            close(got, wanted)
        result[f"dense_n{n}_d{d}_m{m}"] = {"maximum_oracle_velocity_error": max(errors)}
        for p in (1, 2, 3):
            moment = DeepMomentEngine(d, n, p, u, y, seed=712)
            ms = moment.initial_state()
            ms.s.fill_(1.7)
            for key in ("w", "c", "A2", "B2", "A3", "B3"):
                value = getattr(ms, key)
                value.add_(torch.tensor(gen.normal(scale=.3, size=value.shape)))
            matrices = [npv(ms.w)] + [npv(getattr(moment, f"W{layer}0")) + reconstruct(ms, layer) for layer in (2, 3)]
            physical = oracle.Parameters(tuple(matrices), npv(ms.c))
            vel = oracle.flow_velocity(physical, raw_x, y)
            fields, mv = moment.fields(ms), moment.rhs(ms)
            close(mv.w, vel.weights[0]); close(mv.c, vel.readout)
            close(moment.predict(ms, u), oracle.forward(physical, raw_x).output)
            duplicate = DeepMomentEngine(d, n, p, np.tile(u, (3, 1)), np.tile(y, 3), seed=712)
            repeated = duplicate.initial_state()
            repeated.w, repeated.c, repeated.s = ms.w.clone(), ms.c.clone(), ms.s.clone()
            for key in ("A2", "B2", "A3", "B3"):
                setattr(repeated, key, getattr(ms, key).repeat(1, 1, 3))
            repeated_velocity = duplicate.rhs(repeated)
            close(repeated_velocity.w, mv.w); close(repeated_velocity.c, mv.c)
            close(repeated_velocity.s, mv.s)
            for key in ("A2", "B2", "A3", "B3"):
                close(getattr(repeated_velocity, key), getattr(mv, key).repeat(1, 1, 3))
            for k, backward in enumerate(oracle.backward(physical, raw_x), 1):
                close(fields["delta" + str(k)], backward)
            derivative_errors, defect_errors = [], []
            for layer in (2, 3):
                a, b = (npv(getattr(ms, prefix + str(layer))) for prefix in ("A", "B"))
                da, db = (npv(getattr(mv, prefix + str(layer))) for prefix in ("A", "B"))
                length, rho = 1 + float(ms.s), float(fields["rho"])
                weighted = np.arange(1, 2 * p, 2)
                physical_derivative = -2 / (m * n * length) * sum(
                    weighted[k] * (np.outer(da[k, :, j], b[k, :, j])
                                   + np.outer(a[k, :, j], db[k, :, j])
                                   - rho / length * np.outer(a[k, :, j], b[k, :, j]))
                    for k in range(p) for j in range(m))
                left, right = moment.derivative_factors(ms, layer, mv)
                derivative_errors.append(close(left @ right.T, physical_derivative))
                up = sum(weighted[k] * a[k] for k in range(p)) / length
                hp = sum(weighted[k] * b[k] for k in range(p)) / length
                defect = 2 / (m * n) * ((npv(fields["delta" + str(layer)]) * npv(fields["r"]) - rho * up)
                                         @ (npv(fields["h" + str(layer - 1)]) - hp).T)
                defect_errors.append(close(physical_derivative - vel.weights[layer - 1], defect))
                left, right = moment.defect_factors(ms, layer)
                close(left @ right.T, defect)
                close(moment.defect_frobenius(ms, layer), np.linalg.norm(defect))
                v, w = gen.normal(size=(n, 4)), gen.normal(size=(n, 4))
                forward = moment.apply_hidden(ms, layer, torch.tensor(v))
                backward = moment.apply_hidden(ms, layer, torch.tensor(w), transpose=True)
                close(forward, matrices[layer - 1] @ v)
                close(backward, matrices[layer - 1].T @ w)
                close((npv(forward) * w).sum(), (v * npv(backward)).sum())
            # Zero residual is absorbing at noninitial history as well.
            saved_labels = moment.labels.clone()
            moment.labels = moment.predict(ms, u).clone()
            for value in moment.rhs(ms).tensors():
                close(value, torch.zeros_like(value), 0, 0)
            moment.labels = saved_labels
            first, second, euler, candidate = heun_trial(moment, ms, .0007)
            rtol, atol = 1e-5, 1e-7
            ratios = [np.sqrt(np.mean((npv(c) - npv(b)) ** 2)) /
                      (atol + rtol * max(1, np.sqrt(np.mean(npv(a) ** 2)), np.sqrt(np.mean(npv(c) ** 2))))
                      for a, b, c in zip(ms.tensors(), euler.tensors(), candidate.tensors())]
            for layer in (2, 3):
                a, b, c = [reconstruct(value, layer) for value in (ms, euler, candidate)]
                ratios.append(np.linalg.norm(c - b) / np.sqrt(n) /
                              (atol + rtol * max(1, np.linalg.norm(a) / np.sqrt(n), np.linalg.norm(c) / np.sqrt(n))))
            controller_error = abs(controlled_error(moment, ms, euler, candidate, rtol, atol) - max(ratios))
            assert controller_error < 2e-8
            result[f"moment_n{n}_d{d}_m{m}_p{p}"] = dict(
                maximum_derivative_error=max(derivative_errors), maximum_defect_error=max(defect_errors),
                independent_controller_error=controller_error)
    # Test moving-interval moments against Gauss quadrature, not another transport implementation.
    from numpy.polynomial.legendre import leggauss, legval
    nodes, weights = leggauss(16)
    length, rate, eps = 2.3, .71, 1e-5
    def moments(ell):
        x = (nodes + 1) * ell / 2
        return np.asarray([ell / 2 * np.dot(weights, (1 + x + x ** 3) * legval(nodes, [0] * k + [1])) for k in range(3)])
    values = torch.tensor(moments(length)[:, None, None])
    e = DeepMomentEngine(1, 1, 3, [[1]], [1], seed=1)
    actual = e.transport_moments(values, torch.tensor([[rate * (1 + length + length ** 3)]], dtype=torch.float64),
                                 torch.tensor(rate, dtype=torch.float64), torch.tensor(length, dtype=torch.float64))
    finite = rate * (moments(length + eps) - moments(length - eps)) / (2 * eps)
    result["moving_interval_quadrature_error"] = close(actual[:, 0, 0], finite, 2e-7, 2e-8)
    # The four representative samples are the exact oddness quotient of eight.
    case = json.loads((STUDY / "deep_circle_cases.json").read_text())["equal_mixed_odd"]
    angles = np.deg2rad(case["angles_degrees"])
    u = np.column_stack((np.cos(angles), np.sin(angles)))
    y = np.asarray(case["labels"], dtype=float)
    full_u, full_y = np.concatenate((u, -u)), np.concatenate((y, -y))
    close(full_y, np.asarray(case["original_labels"]), 0, 0)
    all_angles = np.deg2rad(case["original_angles_degrees"])
    close(full_u, np.column_stack((np.cos(all_angles), np.sin(all_angles))), 1e-15, 0)
    antipodal_errors = []
    dense = DeepDenseEngine(2, 13, u, y, seed=916)
    full = DeepDenseEngine(2, 13, full_u, full_y, seed=916)
    state = dense.initial_state()
    for value in state.tensors():
        value.add_(torch.tensor(gen.normal(scale=.2, size=value.shape)))
    for got, expected in zip(full.rhs(state).tensors(), dense.rhs(state).tensors()):
        antipodal_errors.append(close(got, expected))
    for p in (1, 2, 3):
        half = DeepMomentEngine(2, 13, p, u, y, seed=916)
        full = DeepMomentEngine(2, 13, p, full_u, full_y, seed=916)
        for perturb in (False, True):
            hs, fs = half.initial_state(), full.initial_state()
            if perturb:
                hs.s.fill_(.8)
                for key in ("w", "c", "A2", "B2", "A3", "B3"):
                    value = getattr(hs, key)
                    value.add_(torch.tensor(gen.normal(scale=.2, size=value.shape)))
                fs.w, fs.c, fs.s = hs.w.clone(), hs.c.clone(), hs.s.clone()
                for key in ("A2", "B2", "A3", "B3"):
                    value = getattr(hs, key)
                    setattr(fs, key, torch.cat((value, -value), dim=2))
            hv, fv = half.rhs(hs), full.rhs(fs)
            hf, ff = half.fields(hs), full.fields(fs)
            for key in ("w", "c", "s"):
                antipodal_errors.append(close(getattr(hv, key), getattr(fv, key)))
            for key in ("A2", "B2", "A3", "B3"):
                value = getattr(hv, key)
                antipodal_errors.append(close(getattr(fv, key), torch.cat((value, -value), dim=2)))
            antipodal_errors.append(close(hf["loss"], ff["loss"]))
            for layer in (2, 3):
                antipodal_errors.append(close(reconstruct(hs, layer), reconstruct(fs, layer)))
                dl, dr = half.derivative_factors(hs, layer, hv)
                fl, fr = full.derivative_factors(fs, layer, fv)
                antipodal_errors.append(close(dl @ dr.T, fl @ fr.T))
            for layer in (1, 2, 3):
                antipodal_errors.append(close(ff["h" + str(layer)], torch.cat((hf["h" + str(layer)], -hf["h" + str(layer)]), dim=1)))
                antipodal_errors.append(close(ff["delta" + str(layer)], torch.cat((hf["delta" + str(layer)], hf["delta" + str(layer)]), dim=1)))
    result["antipodal_quotient_max_error"] = max(antipodal_errors)
    return result


@torch.no_grad()
def replay(path, device):
    """Replay complete saved final and threshold panels from physical matrices."""
    path = Path(path)
    summary = json.loads((path / "summary.json").read_text())
    config = json.loads((path / "config.json").read_text())
    manifest = json.loads((path / "manifest.json").read_text())
    for key, value in manifest.items():
        assert summary[key] == value, "manifest/summary mismatch: " + key
    for filename, expected in summary["source_sha256"].items():
        assert digest(STUDY / filename) == expected, "production source changed: " + filename
    if config.get("case"):
        case = json.loads((STUDY / "deep_circle_cases.json").read_text())[config["case"]]
        directions = np.deg2rad(case["angles_degrees"])
        close(config["inputs"], np.column_stack((np.cos(directions), np.sin(directions))), 2e-15, 0)
        close(config["labels"], case["labels"], 0, 0)
        assert config["width"] == 4096 and config["query_count"] == 8192
    assert digest(path / "arrays.npz") == summary["arrays_sha256"]
    assert digest(path / "config.json") == summary["effective_config_sha256"]
    for filename, expected in summary["checkpoint_sha256"].items():
        assert digest(path / filename) == expected
    n, d, m = config["width"], 2, len(config["labels"])
    initial = oracle.initialize(n, 3, d, seed=config["seed"])
    assert array_digest(*initial.weights, initial.readout) == summary["initialization_hash"]
    to_tensor = lambda value: torch.as_tensor(value, dtype=torch.float64, device=device)
    fixed = {"W2": to_tensor(initial.weights[1]), "W3": to_tensor(initial.weights[2])}
    with np.load(path / "arrays.npz", allow_pickle=False) as archive:
        assert array_digest(archive["train_inputs"], archive["train_labels"]) == summary["data_sha256"]
        assert array_digest(archive["circle_inputs"]) == summary["query_sha256"]
        assert np.isfinite(archive["local_error_ratios"]).all()
        assert (archive["local_error_ratios"] <= 1).all()
        assert len(archive["times"]) == summary["accepted"] + 1
        close(archive["accepted_steps"], np.diff(archive["times"]), 2e-11, 2e-12)
        close(archive["losses"][-1], summary["training_mse"], 0, 0)
        close(archive["physical_time"], summary["time"], 0, 0)
        assert list(archive["observation_labels"]) == [item["label"] for item in summary["observations"]]
        assert len(summary["checkpoints"]) == sum(item["label"].startswith("loss_") for item in summary["observations"])
        input_tensor = to_tensor(archive["circle_inputs"])
        train_tensor = to_tensor(archive["train_inputs"])
        labels = to_tensor(archive["train_labels"])
        entries = []
        initial_hidden = None
        for index, observation in enumerate(summary["observations"]):
            label = observation["label"]
            if label == "initial":
                state = {"w": to_tensor(initial.weights[0]), "W2": fixed["W2"],
                         "W3": fixed["W3"], "c": to_tensor(initial.readout)}
            else:
                if label == "final":
                    saved = archive
                else:
                    saved = np.load(path / ("checkpoint_" + label.replace(".", "p") + ".npz"), allow_pickle=False)
                state = {key: to_tensor(saved[key]) for key in ("w", "c")}
                for layer in (2, 3):
                    key = "W" + str(layer)
                    if config["model"] == "dense":
                        state[key] = to_tensor(saved[key])
                    else:
                        # Deliberately use a physical dense matrix for independent replay.
                        a, b = to_tensor(saved["A" + str(layer)]), to_tensor(saved["B" + str(layer)])
                        delta = torch.zeros_like(fixed[key])
                        for k in range(config["order"]):
                            delta.add_(a[k] @ b[k].T, alpha=2 * k + 1)
                        state[key] = fixed[key] - 2 / (m * n * (1 + float(saved["s"]))) * delta
                if label != "final":
                    close(saved["physical_time"], observation["time"], 0, 0)
                    close(saved["training_mse"], observation["training_mse"], 0, 0)
                    saved.close()
            def predict(inputs):
                panels = []
                for begin in range(0, len(inputs), 128):
                    h = torch.tanh(state["w"] @ inputs[begin:begin + 128].T)
                    h = torch.tanh(state["W2"] @ h)
                    h = torch.tanh(state["W3"] @ h)
                    panels.append(state["c"] @ h / n)
                return torch.cat(panels)
            predictions, train = predict(input_tensor), predict(train_tensor)
            mse = float(((train - labels) ** 2).mean())
            panel_error = close(predictions, archive["circle_predictions"][index], 2e-10, 2e-10)
            train_error = close(train, archive["train_predictions"][index], 2e-10, 2e-10)
            close(mse, observation["training_mse"], 2e-11, 2e-10)
            if label.startswith("loss_"):
                close(mse, float(label[5:]), 2e-9, 2e-9)
            h1 = torch.tanh(state["w"] @ train_tensor.T)
            h2 = torch.tanh(state["W2"] @ h1)
            h3 = torch.tanh(state["W3"] @ h2)
            if initial_hidden is None:
                assert label == "initial"
                initial_hidden = tuple(value.clone() for value in (h1, h2, h3))
            motion = {f"h{layer}_training_rms": float(((current - initial_h) ** 2).mean().sqrt())
                      for layer, (current, initial_h) in enumerate(zip((h1, h2, h3), initial_hidden), 1)}
            motion["w_rms"] = float(((state["w"] - to_tensor(initial.weights[0])) ** 2).mean().sqrt())
            motion["c_rms"] = float(((state["c"] - to_tensor(initial.readout)) ** 2).mean().sqrt())
            entries.append(dict(label=label, panel_max_error=panel_error, train_max_error=train_error,
                                replay_mse=mse, motion_from_initial=motion))
        return dict(path=str(path.resolve()), status=summary["status"], case=config.get("case"),
                    model=config["model"], P=config["order"] if config["model"] == "moment" else None,
                    rtol=config["rtol"], observation_count=len(entries), checkpoint_count=len(summary["checkpoints"]), observations=entries,
                    initialization_hash=summary["initialization_hash"], arrays_sha256=summary["arrays_sha256"])


def compare_reproduction(original, repetition):
    """Compare bytes of every scientific array, including every checkpoint field."""
    original, repetition = Path(original), Path(repetition)
    left_summary = json.loads((original / "summary.json").read_text())
    right_summary = json.loads((repetition / "summary.json").read_text())
    for key in ("source_sha256", "initialization_hash", "data_sha256", "query_sha256", "model", "P", "rtol", "atol"):
        assert left_summary[key] == right_summary[key], "repeat input differs: " + key
    assert left_summary["checkpoints"] == right_summary["checkpoints"]
    files = ["arrays.npz"] + left_summary["checkpoints"]
    results = []
    excluded = {"integration_wall_times"}
    for filename in files:
        with np.load(original / filename, allow_pickle=False) as left, np.load(repetition / filename, allow_pickle=False) as right:
            assert set(left.files) == set(right.files)
            fields = []
            for key in sorted(left.files):
                if key in excluded:
                    continue
                a, b = left[key], right[key]
                equal = a.shape == b.shape and a.dtype == b.dtype and a.tobytes(order="C") == b.tobytes(order="C")
                maximum = (float(np.max(np.abs(a - b), initial=0)) if a.dtype.kind in "fiu" and a.shape == b.shape else None)
                fields.append(dict(field=key, bitwise_equal=equal, maximum_absolute_difference=maximum))
            results.append(dict(file=filename, fields=fields, all_fields_bitwise_equal=all(item["bitwise_equal"] for item in fields)))
    return dict(original=str(original.resolve()), repetition=str(repetition.resolve()),
                original_device=left_summary["device"], repetition_device=right_summary["device"],
                excluded_fields=sorted(excluded), files=results,
                all_scientific_fields_bitwise_equal=all(item["all_fields_bitwise_equal"] for item in results))


def score_runs(paths):
    """Recompute every common matched-loss score and protocol refinement gate."""
    groups = {}
    for path in map(Path, paths):
        config = json.loads((path / "config.json").read_text())
        summary = json.loads((path / "summary.json").read_text())
        assert digest(path / "arrays.npz") == summary["arrays_sha256"]
        with np.load(path / "arrays.npz", allow_pickle=False) as archive:
            key = array_digest(archive["train_inputs"], archive["train_labels"])
            observations = {str(label): dict(prediction=archive["circle_predictions"][i].copy(),
                                            mse=float(archive["observation_training_mse"][i]),
                                            time=float(archive["observation_times"][i]))
                            for i, label in enumerate(archive["observation_labels"])}
            model = "dense" if config["model"] == "dense" else "P" + str(config["order"])
            groups.setdefault(key, {}).setdefault(model, []).append(
                dict(path=str(path.resolve()), rtol=config["rtol"], observations=observations,
                     query_hash=summary["query_sha256"], initialization_hash=summary["initialization_hash"]))
    result = []
    rms = lambda values: float(np.sqrt(np.mean(values ** 2)))
    for data_hash, models in groups.items():
        assert "dense" in models
        for model, runs in models.items():
            runs.sort(key=lambda item: item["rtol"])
            assert len({item["rtol"] for item in runs}) == len(runs), "score resolutions separately from duplicate reproducibility runs"
        dense = models["dense"][0]
        rows = []
        for name, runs in sorted(models.items()):
            if name == "dense":
                continue
            fine = runs[0]
            assert fine["query_hash"] == dense["query_hash"]
            assert fine["initialization_hash"] == dense["initialization_hash"]
            for label in fine["observations"]:
                if not label.startswith("loss_") or label not in dense["observations"]:
                    continue
                prediction = fine["observations"][label]["prediction"]
                reference = dense["observations"][label]["prediction"]
                error = rms(prediction - reference)
                nested_change = abs(error - rms(prediction[::2] - reference[::2]))
                previous = runs[1] if len(runs) >= 2 else None
                dense_previous = models["dense"][1] if len(models["dense"]) >= 2 else None
                model_change = (rms(prediction - previous["observations"][label]["prediction"])
                                if previous and label in previous["observations"] else None)
                dense_change = (rms(reference - dense_previous["observations"][label]["prediction"])
                                if dense_previous and label in dense_previous["observations"] else None)
                threshold = float(label[5:])
                crossing_valid = all(abs(item["observations"][label]["mse"] - threshold) <= .01 * threshold
                                     for item in (fine, dense))
                gate = (model_change is not None and dense_change is not None and
                        max(model_change, dense_change) <= min(.005, .1 * error) and
                        nested_change <= 1e-5 and crossing_valid)
                rows.append(dict(model=name, milestone=threshold, rms=error, nested_grid_change=nested_change,
                                 model_refinement_change=model_change, dense_refinement_change=dense_change,
                                 physical_crossing_valid=crossing_valid, numerical_gate=bool(gate),
                                 coarse_agreement=error <= .1, model_path=fine["path"], dense_path=dense["path"]))
        orderings = []
        for threshold in sorted({row["milestone"] for row in rows}, reverse=True):
            selected = {row["model"]: row for row in rows if row["milestone"] == threshold}
            if "P1" not in selected or "P3" not in selected:
                continue
            one, three = selected["P1"], selected["P3"]
            shifts = [row[key] for row in (one, three) for key in ("model_refinement_change", "dense_refinement_change")]
            uncertainty = sum(shifts) if all(value is not None for value in shifts) else None
            gap = one["rms"] - three["rms"]
            orderings.append(dict(milestone=threshold, p1_minus_p3_gap=gap, observed_uncertainty=uncertainty,
                                  ordering_resolved=bool(one["numerical_gate"] and three["numerical_gate"] and
                                                         uncertainty is not None and abs(gap) > uncertainty),
                                  p3_better=gap > 0))
        result.append(dict(data_hash=data_hash, rows=rows, p1_p3_ordering=orderings))
    return result


def compare_analysis(independent_path, analysis_path):
    """Compare independent scores to every analyzer comparison and order gate."""
    independent_path, analysis_path = Path(independent_path), Path(analysis_path)
    independent = json.loads(independent_path.read_text())
    analysis = json.loads(analysis_path.read_text())
    rows = {}
    for group in independent["scores"]:
        for row in group["rows"]:
            config = json.loads((Path(row["model_path"]) / "config.json").read_text())
            rows[(config["case"], int(row["model"][1:]), row["milestone"])] = row
    assert len(rows) == len(analysis["comparisons"])
    maximum = 0.
    for reported in analysis["comparisons"]:
        row = rows[(reported["case"], reported["P"], reported["milestone"])]
        assert row["model_path"] == reported["closure_run"]
        assert row["dense_path"] == reported["dense_run"]
        for a, b in (("rms", "rms_8192"), ("nested_grid_change", "nested_grid_change"),
                     ("model_refinement_change", "closure_refinement_rms"),
                     ("dense_refinement_change", "dense_refinement_rms")):
            maximum = max(maximum, close(row[a], reported[b], 3e-15, 3e-15))
        gates = dict(closure_refinement_available=row["model_refinement_change"] is not None,
                     dense_refinement_available=row["dense_refinement_change"] is not None,
                     closure_absolute=row["model_refinement_change"] <= .005,
                     dense_absolute=row["dense_refinement_change"] <= .005,
                     closure_relative=row["model_refinement_change"] <= .1 * row["rms"],
                     dense_relative=row["dense_refinement_change"] <= .1 * row["rms"],
                     grid=row["nested_grid_change"] <= 1e-5)
        valid_losses = []
        for key in ("closure_run", "dense_run", "closure_previous", "dense_previous"):
            summary = json.loads((Path(reported[key]) / "summary.json").read_text())
            label = "loss_" + format(reported["milestone"], ".12g")
            observation = next(item for item in summary["observations"] if item["label"] == label)
            valid_losses.append(abs(observation["training_mse"] - reported["milestone"]) <= .01 * reported["milestone"])
        gates["physical_loss"] = all(valid_losses)
        assert gates == reported["numerical_gates"]
        assert all(gates.values()) == reported["numerical_pass"] == row["numerical_gate"]
        assert row["coarse_agreement"] == reported["measured_coarse_agreement"]
    for reported in analysis["endpoint_comparisons"]:
        assert reported["milestone"] == .001
        row = rows[(reported["case"], reported["P"], reported["milestone"])]
        maximum = max(maximum, close(row["rms"], reported["rms_8192"], 3e-15, 3e-15))
        assert row["numerical_gate"] == reported["numerical_pass"]
    for reported in analysis["order_comparisons"]:
        low = rows[(reported["case"], reported["lower_P"], reported["milestone"])]
        high = rows[(reported["case"], reported["higher_P"], reported["milestone"])]
        gap = low["rms"] - high["rms"]
        sensitivity = sum(row[key] for row in (low, high)
                          for key in ("model_refinement_change", "dense_refinement_change"))
        maximum = max(maximum, close(gap, reported["lower_minus_higher_rms"], 3e-15, 3e-15))
        maximum = max(maximum, close(sensitivity, reported["summed_observed_sensitivity"], 3e-15, 3e-15))
        gates_pass = low["numerical_gate"] and high["numerical_gate"]
        assert gates_pass == reported["both_numerical_gates_pass"]
        assert bool(gates_pass and abs(gap) > sensitivity) == reported["resolved"]
    return dict(independent_scores=str(independent_path.resolve()), analysis=str(analysis_path.resolve()),
                independent_sha256=digest(independent_path), analysis_sha256=digest(analysis_path),
                matched_milestone_rows=len(rows), matched_endpoint_rows=len(analysis["endpoint_comparisons"]),
                matched_order_rows=len(analysis["order_comparisons"]), maximum_metric_difference=maximum,
                numerical_gates_passing=sum(row["numerical_gate"] for row in rows.values()), status="PASS")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True)
    parser.add_argument("--replay", action="append", default=[])
    parser.add_argument("--score-run", action="append", default=[])
    parser.add_argument("--repeat-pair", action="append", nargs=2, default=[], metavar=("ORIGINAL", "REPETITION"))
    parser.add_argument("--compare-analysis", nargs=2, metavar=("INDEPENDENT_SCORES", "ANALYSIS"))
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--threads", type=int, default=1)
    parser.add_argument("--skip-checks", action="store_true")
    args = parser.parse_args()
    output = Path(args.out)
    output.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(args.threads)
    torch.backends.cuda.matmul.allow_tf32 = False
    files = [STUDY / name for name in ("DEEP_CIRCLE_DERIVATION.md", "deep_moment_engine.py", "deep_circle_run.py",
                                     "test_deep_moment_engine.py", "moment_engine.py", "check_deep_circle.py", "deep_circle_cases.json")]
    files += [ROOT / "docs/NOTATION.md", ROOT / "code/pde/finite_network.py"]
    if (STUDY / "DEEP_CIRCLE_PROTOCOL.md").exists():
        files.append(STUDY / "DEEP_CIRCLE_PROTOCOL.md")
    report = dict(source_sha256={str(path.relative_to(ROOT)): digest(path) for path in files},
                  python=sys.version, numpy=np.__version__, torch=torch.__version__, platform=platform.platform(),
                  command=sys.argv, device=args.device, threads=args.threads)
    start = time.monotonic()
    try:
        report["checks"] = {} if args.skip_checks else checks()
        report["replay"] = []
        for path in args.replay:
            item = replay(path, args.device)
            report["replay"].append(item)
            print(json.dumps(dict(event="replayed", path=path, observations=len(item["observations"]))), flush=True)
        report["scores"] = score_runs(args.score_run) if args.score_run else []
        report["reproduction"] = [compare_reproduction(*pair) for pair in args.repeat_pair]
        report["analysis_comparison"] = compare_analysis(*args.compare_analysis) if args.compare_analysis else None
        report["replay_totals"] = dict(runs=len(report["replay"]),
            observations=sum(item["observation_count"] for item in report["replay"]),
            checkpoints=sum(item["checkpoint_count"] for item in report["replay"]),
            maximum_prediction_rebuild_difference=max((observation["panel_max_error"]
                for item in report["replay"] for observation in item["observations"]), default=0.))
        report["status"] = "PASS"
    except Exception as exc:
        report.update(status="FAIL", exception=type(exc).__name__, message=str(exc))
        raise
    finally:
        report["seconds"] = time.monotonic() - start
        (output / "check.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(dict(status=report["status"], seconds=report["seconds"], output=str(output))), flush=True)


if __name__ == "__main__":
    main()
