"""Independent saved-state audit of the two-case width-4096 comparison.

No trajectory producer or maintained prediction engine is imported. Scientific
arithmetic uses CUDA float64. Large uncompressed NPZ state stacks are mapped
read-only, and only the requested snapshot is copied into memory.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import struct
import sys
import zipfile

os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]
STUDY = Path(__file__).resolve().parent
DATA = ROOT / "data/generated/gradient_flow_probe_dictionary_20260921"
ARCHIVE = ROOT / "data/generated/random_dictionary_learned_circle_20260920"
WIDTH, THRESHOLD, REPLAY, GATE = 4096, 1e-3, 1e-10, .01
MAX_EXTRA_PER_CELL = 1
CASES = {
    "quadrant_pairs": ([10, 20, 30, 40, 50, 60, 70, 80], [1, 1, -1, -1, 1, 1, -1, -1]),
    "two_outliers_alternating": ([15, 27, 39, 51, 63, 75, 165, 285], [1, -1, 1, -1, 1, -1, 1, -1]),
}
COUNTS = {"new": {1: (2, 4), 2: (2, 4), 3: (6, 12)},
          "old": {1: (5, 3), 2: (15, 6), 3: (35, 10)}}
METHODS = tuple(f"{family}_p{p}" for family in COUNTS for p in (1, 2, 3))
HASHES = {}


def digest(path):
    path = Path(path).resolve()
    if str(path) not in HASHES:
        h = hashlib.sha256()
        with path.open("rb") as stream:
            for block in iter(lambda: stream.read(8 * 1024 * 1024), b""):
                h.update(block)
        HASHES[str(path)] = h.hexdigest()
    return HASHES[str(path)]


def read_json(path):
    digest(path)
    return json.loads(Path(path).read_text())


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def owned(path):
    path = Path(path).resolve()
    if not path.is_relative_to(DATA.resolve()) or path == DATA.resolve():
        raise ValueError("current input/output roots must be below this study's generated namespace")
    return path


class Arrays:
    """Safe numeric NPZ reader with bounded-memory snapshot extraction."""

    def __init__(self, path):
        self.path = Path(path)
        self.zipped = zipfile.ZipFile(self.path)
        self.arrays = np.load(self.path, allow_pickle=False)

    def close(self):
        self.arrays.close()
        self.zipped.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def __contains__(self, key):
        return key in self.arrays.files

    def __getitem__(self, key):
        value = self.arrays[key]
        if value.dtype.hasobject:
            raise ValueError("object arrays are forbidden")
        return value

    @staticmethod
    def header(stream):
        version = np.lib.format.read_magic(stream)
        if version == (1, 0):
            return np.lib.format.read_array_header_1_0(stream)
        if version == (2, 0):
            return np.lib.format.read_array_header_2_0(stream)
        raise ValueError(f"unsupported NPY version {version}")

    def shape(self, key):
        with self.zipped.open(key + ".npy") as stream:
            shape, _, dtype = self.header(stream)
        if dtype.hasobject:
            raise ValueError("object arrays are forbidden")
        return shape

    def snapshot(self, key, index):
        info = self.zipped.getinfo(key + ".npy")
        if info.compress_type == zipfile.ZIP_STORED:
            with self.path.open("rb") as stream:
                stream.seek(info.header_offset)
                header = stream.read(30)
                if header[:4] != b"PK\x03\x04":
                    raise ValueError("invalid local ZIP header")
                name_length, extra_length = struct.unpack_from("<HH", header, 26)
                stream.seek(name_length + extra_length, 1)
                shape, fortran, dtype = self.header(stream)
                offset = stream.tell()
            if dtype.hasobject or not shape:
                raise ValueError("snapshot requires a numeric non-scalar array")
            mapped = np.memmap(self.path, dtype=dtype, mode="r", offset=offset,
                               shape=shape, order="F" if fortran else "C")
            result = np.array(mapped[index], copy=True)
            del mapped
            return result
        with self.zipped.open(key + ".npy") as stream:
            shape, fortran, dtype = self.header(stream)
            if fortran or dtype.hasobject or not shape:
                raise ValueError("compressed snapshots must be numeric and C-contiguous")
            index = index if index >= 0 else shape[0] + index
            if not 0 <= index < shape[0]:
                raise IndexError(index)
            count = math.prod(shape[1:])
            stream.seek(index * count * dtype.itemsize, 1)
            data = stream.read(count * dtype.itemsize)
            if len(data) != count * dtype.itemsize:
                raise ValueError("truncated snapshot")
            return np.frombuffer(data, dtype=dtype).reshape(shape[1:]).copy()


def tensor(value, device):
    if isinstance(value, torch.Tensor):
        return value.to(device=device, dtype=torch.float64)
    return torch.as_tensor(np.asarray(value), device=device, dtype=torch.float64)


def finite_number(value):
    value = float(value)
    return value if math.isfinite(value) else None


@torch.no_grad()
def predict(state, inputs, device):
    """Independent normalized forward calculation, input blocks of 256."""
    w, c, middle = (state[k] for k in ("w", "c", "M"))
    result = []
    for batch in tensor(inputs, device).split(256):
        lower = torch.tanh(w @ batch.T)
        upper = (state["b2"] @ (middle @ (state["b1"].T @ lower / len(w)))
                 if "b1" in state else middle @ lower)
        result.append(c @ torch.tanh(upper) / len(c))
    return torch.cat(result)


def config_for(directory, case):
    worker = list(CASES).index(case)
    root = directory.parent
    paths = [root / f"config_worker{worker}.json",
             root / f"config_user_width4096_worker{worker}.json"]
    for path in paths:
        if path.exists():
            return path, read_json(path)
    raise FileNotFoundError(f"no case-worker configuration beside {directory}")


def cell_paths(case, method, roots):
    frozen = method == "full" or method in ("old_p1", "old_p3")
    archive_method = "full" if method == "full" else method.replace("old_", "ours_")
    if frozen:
        return [ARCHIVE / f"scaling_width4096_{level}01" / f"{case}_{archive_method}"
                for level in ("primary", "refined")]
    paths = [root / f"{case}_{method}" for root in roots[:2]]
    paths.extend(root / f"{case}_{method}" for root in roots[2:]
                 if (root / f"{case}_{method}").exists())
    return paths


@torch.no_grad()
def audit(directory, case, method, device, origin=None):
    record = dict(path=str(directory), valid=False, fitted=False, replay_valid=False,
                  reasons=[], checks={}, status="missing")
    checks, reasons = record["checks"], record["reasons"]
    bundle = None

    def require(condition, description):
        if not bool(condition):
            reasons.append(description)

    def difference(name, actual, expected, tolerance=REPLAY):
        actual, expected = tensor(actual, device), tensor(expected, device)
        if actual.shape != expected.shape:
            checks[name] = None
            reasons.append(name + ": shape mismatch")
            return
        error = finite_number((actual - expected).abs().max()) if actual.numel() else 0.
        checks[name] = error
        require(error is not None and error <= tolerance, name + " exceeds tolerance")

    try:
        summary = read_json(directory / "summary.json")
        cp, config = config_for(directory, case)
        record.update(config_path=str(cp), config_sha256=digest(cp),
                      rtol=config.get("rtol"), atol=config.get("atol"),
                      status=summary.get("status"), summary=summary)
        for key, expected in (("width", WIDTH), ("network_seed", 20260920),
                              ("threshold", THRESHOLD), ("dtype", "float64")):
            require(config.get(key) == expected, "configuration mismatch: " + key)
        if case in config.get("cases", {}):
            declared = config["cases"][case]
            require(declared.get("angles_degrees") == CASES[case][0] and
                    declared.get("labels") == CASES[case][1], "configuration geometry mismatch")
        for name in ("rtol", "atol"):
            require(isinstance(config.get(name), (int, float)) and config[name] > 0,
                    "missing/invalid " + name)
            require(summary.get(name) == config.get(name), "summary/config mismatch: " + name)
        current = directory.is_relative_to(DATA)
        if current:
            initial_archive = (ROOT / config["initial_archive"]).resolve()
            require(initial_archive.is_relative_to(ARCHIVE), "initialization archive outside authorized boundary")
            if initial_archive.is_relative_to(ARCHIVE):
                require(digest(initial_archive) == config["initial_archive_sha256"], "initial archive hash mismatch")
        critical = ("code/pde/finite_torch.py", "code/pde/observable_torch_p1.py",
                    "studies/random_dictionary_learned_circle_20260920/diverse_benchmark.py")
        source_hashes = config.get("source_hashes", {})
        require(all(name in source_hashes for name in critical), "missing critical producer source hashes")
        source_checks = {}
        for name, expected in source_hashes.items():
            if not current and name not in critical:
                continue
            source = (ROOT / name).resolve()
            allowed = (source.is_relative_to(ROOT / "code") or source.is_relative_to(STUDY)
                       or source.is_relative_to(ROOT / "studies/random_dictionary_learned_circle_20260920"))
            require(allowed, "source outside authorized input boundary")
            if not allowed:
                continue
            source_checks[name] = digest(source) == expected
            require(source_checks[name], "producer source hash mismatch: " + name)
        record["producer_source_checks"] = source_checks
        if method != "full":
            if current:
                metadata_path = directory.parent / (directory.name + "_dictionary.json")
            else:
                worker = list(CASES).index(case)
                metadata_path = directory.parent / f"dictionary_user_width4096_worker{worker}_{method.replace('old_', 'ours_')}.json"
            metadata = read_json(metadata_path)
            record["dictionary_metadata_path"] = str(metadata_path)
            if method.startswith("new"):
                populations = [metadata["lower"], metadata["upper"]]
                names = ("ridge_condition", "triangular_relative_residual")
            elif current:
                populations, names = metadata["populations"], ("regularized_condition", "triangular_residual")
            else:
                populations, names = metadata["populations"], ("ridge_condition", "triangular_solve_residual")
            require(len(populations) == 2, "dictionary diagnostics must cover both populations")
            for population in populations:
                condition, residual = population[names[0]], population[names[1]]
                require(math.isfinite(condition) and 1 <= condition <= 1e10, "dictionary ridge-condition gate failed")
                require(math.isfinite(residual) and 0 <= residual <= 1e-8, "dictionary triangular-residual gate failed")
        record["arrays_sha256"] = digest(directory / "arrays.npz")
        with Arrays(directory / "arrays.npz") as saved:
            snapshots = saved["snapshot_times"]
            require(snapshots.ndim == 1 and len(snapshots) >= 1, "invalid snapshot times")
            require(saved.shape("w") == (len(snapshots), WIDTH, 2), "wrong saved readin shape")
            require(saved.shape("c") == (len(snapshots), WIDTH), "wrong saved readout shape")
            if method == "full":
                expected_middle = (WIDTH, WIDTH)
                require("b1" not in saved and "b2" not in saved, "full reference contains closure bases")
            else:
                family, p = method.split("_p")
                k1, k2 = COUNTS[family][int(p)]
                expected_middle = (k2, k1)
                require(saved.shape("b1") == (WIDTH, k1) and saved.shape("b2") == (WIDTH, k2),
                        "dictionary dimensions mismatch")
            require(saved.shape("M") == (len(snapshots), *expected_middle), "wrong saved middle shape")
            require(saved.shape("circle_predictions") == (len(snapshots), 2048), "wrong snapshot prediction shape")
            for prefix, count in (("endpoint", 8192), ("circle", 2048)):
                angles = torch.arange(count, device=device, dtype=torch.float64) * (2 * math.pi / count)
                difference(prefix + "_angles", saved[prefix + "_angles"], angles)
                difference(prefix + "_inputs", saved[prefix + "_inputs"], torch.stack((angles.cos(), angles.sin()), 1))
            angles = torch.tensor(CASES[case][0], device=device, dtype=torch.float64) * (math.pi / 180)
            difference("training_inputs", saved["training_inputs"], torch.stack((angles.cos(), angles.sin()), 1))
            difference("training_labels", saved["labels"], CASES[case][1])
            endpoint = tensor(saved["endpoint_prediction"], device)
            require(endpoint.shape == (8192,) and torch.isfinite(endpoint).all(), "invalid endpoint prediction")
            times, losses = tensor(saved["times"], device), tensor(saved["losses"], device)
            require(times.ndim == 1 and times.shape == losses.shape and len(times) > 0,
                    "invalid loss/time dimensions")
            require(torch.isfinite(times).all() and torch.isfinite(losses).all(), "nonfinite loss/time trace")
            require(times[0] == 0 and (times[1:] > times[:-1]).all(), "time trace is not strictly increasing from zero")
            require((losses[1:] <= losses[:-1] * (1 + 1e-8) + 1e-12).all(), "accepted loss increases")
            difference("summary_time", times[-1], summary["time"])
            difference("summary_initial_loss", losses[0], summary["initial_loss"])
            difference("summary_final_loss", losses[-1], summary["loss"])
            difference("snapshot_initial_time", snapshots[0], 0.)
            difference("snapshot_final_time", snapshots[-1], times[-1])
            require(np.isfinite(snapshots).all() and np.all(np.diff(snapshots) > 0), "invalid snapshot ordering")
            accepted, errors = tensor(saved["accepted_steps"], device), tensor(saved["local_error_ratios"], device)
            difference("accepted_step_times", accepted, times.diff())
            require(len(accepted) == summary["steps"] <= 30000 and errors.shape == accepted.shape,
                    "accepted-step count mismatch")
            require(torch.isfinite(errors).all() and (errors >= 0).all() and (errors <= 1).all(), "invalid local error ratios")
            require((accepted > 0).all() and (accepted <= 2 + REPLAY).all(), "accepted steps outside bounds")
            bases = {} if method == "full" else {key: tensor(saved[key], device) for key in ("b1", "b2")}
            if method != "full":
                for key in ("p1", "p2"):
                    difference("uniform_" + key, saved[key], torch.full((WIDTH,), 1 / WIDTH, device=device, dtype=torch.float64))
                require(all(saved[key].dtype == np.float64 for key in ("b1", "b2")), "dictionary storage is not float64")
            initial_copy = None
            for index, label in ((0, "initial"), (-1, "final")):
                state = {}
                for key in ("w", "c", "M"):
                    raw_state = saved.snapshot(key, index)
                    require(raw_state.dtype == np.float64, label + " " + key + " storage is not float64")
                    state[key] = tensor(raw_state, device)
                del raw_state
                state.update(bases)
                require(all(torch.isfinite(value).all() for value in state.values()), label + " state is nonfinite")
                difference(label + "_circle_replay", predict(state, saved["circle_inputs"], device),
                           saved.snapshot("circle_predictions", index))
                prediction = predict(state, saved["training_inputs"], device)
                loss = (prediction - tensor(saved["labels"], device)).square().mean()
                difference(label + "_loss_replay", loss, losses[0 if index == 0 else -1])
                if index == 0:
                    initial_copy = {key: state[key].clone() for key in ("w", "c")}
                    if method == "full":
                        initial_copy["M"] = state["M"].clone()
                    if origin is not None:
                        for key in ("w", "c"):
                            difference("common_initial_" + key, state[key], origin[key])
                    if method != "full":
                        difference("initial_middle_D", state["M"], saved["D"])
                        difference("initial_readin_g", state["w"], saved["g"])
                        if origin is not None:
                            expected_middle = state["b2"].T @ (origin["M"] @ state["b1"]) / WIDTH
                            difference("projected_common_initial_middle", state["M"], expected_middle)
                        else:
                            reasons.append("common full initial state is unavailable")
                else:
                    difference("endpoint_replay", predict(state, saved["endpoint_inputs"], device), endpoint)
                    record["recomputed_loss"] = finite_number(loss)
                del state
            record.update(loss=summary["loss"], time=summary["time"],
                          first_crossing=bool((losses[:-1] > THRESHOLD).all()),
                          fitted=summary.get("status") == "fitted" and float(losses[-1]) <= THRESHOLD + REPLAY)
            require(record["fitted"], "endpoint did not fit the declared threshold")
            require(record["first_crossing"], "endpoint is not the first detected threshold crossing")
            bundle = dict(prediction=endpoint, angles=saved["endpoint_angles"],
                          inputs=saved["endpoint_inputs"], training_inputs=saved["training_inputs"],
                          labels=saved["labels"], initial=initial_copy)
        record["replay_valid"] = not reasons
        record["valid"] = not reasons
    except (OSError, ValueError, KeyError, TypeError, IndexError, RuntimeError, zipfile.BadZipFile) as exc:
        reasons.append(f"audit failed: {type(exc).__name__}: {exc}")
    return record, bundle


def aligned(left, right):
    return (left is not None and right is not None and all(
        np.array_equal(left[key], right[key]) for key in ("angles", "inputs", "training_inputs", "labels")))


def discrepancy(left, right):
    return finite_number((left["prediction"] - right["prediction"]).abs().max()) if aligned(left, right) else None


def metrics(prediction, reference):
    error = prediction - reference
    return {"rms": finite_number(error.square().mean().sqrt()),
            "l1": finite_number(error.abs().mean()),
            "mse": finite_number(error.square().mean()),
            "max_abs": finite_number(error.abs().max())}


@torch.no_grad()
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primary", type=Path, default=DATA / "comparison_primary01")
    parser.add_argument("--refined", type=Path, default=DATA / "comparison_refined01")
    parser.add_argument("--extra", type=Path, action="append", default=[])
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--device", default="cuda:0")
    args = parser.parse_args()
    roots = [owned(path) for path in (args.primary, args.refined, *args.extra)]
    out = owned(args.out)
    if len(set(roots)) != len(roots) or out in roots or out.exists():
        raise ValueError("distinct input roots and a fresh output root are required")
    if not torch.cuda.is_available() or torch.device(args.device).type != "cuda":
        raise RuntimeError("CUDA is required for scientific replay and metrics")
    torch.set_num_threads(1)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.cuda.set_device(args.device)
    device = args.device
    out.mkdir(parents=True)
    rows, validation, selection, gates, pointwise = [], {}, {}, [], {}
    extra_count = 0
    for case in CASES:
        audited = {}
        full_paths = cell_paths(case, "full", roots)
        full_attempts = [audit(path, case, "full", device) for path in full_paths]
        origins = [attempt[1]["initial"] if attempt[1] else None for attempt in full_attempts]
        if all(origin is not None for origin in origins):
            for name in ("w", "c", "M"):
                delta = finite_number((origins[0][name] - origins[1][name]).abs().max())
                for record, _ in full_attempts:
                    record["checks"]["full_cross_level_initial_" + name] = delta
                    if delta is None or delta > REPLAY:
                        record["reasons"].append("full references have different initial " + name)
                        record["valid"] = record["replay_valid"] = False
        for method in ("full", *METHODS):
            key = case + "_" + method
            paths = cell_paths(case, method, roots)
            attempts = full_attempts if method == "full" else [
                audit(path, case, method, device, origins[min(i, 1)]) for i, path in enumerate(paths)]
            reasons = []
            branch_checks = []
            frozen = method in ("full", "old_p1", "old_p3")
            extras = max(0, len(attempts) - 2)
            extra_count += extras
            if extras > MAX_EXTRA_PER_CELL:
                reasons.append("extra trajectory count exceeds the fixed per-cell bound")
            for i in range(2, len(attempts)):
                left, right = attempts[i - 2:i]
                change = discrepancy(left[1], right[1])
                eligible = left[0]["valid"] and right[0]["valid"] and change is not None and change > GATE
                checks = dict(extra_path=str(paths[i]), eligible=eligible, preceding_refinement_max=change)
                branch_checks.append(checks)
                if not eligible:
                    reasons.append("extra trajectory lacked the numerical-refinement trigger")
                for tolerance in ("rtol", "atol"):
                    previous, current = attempts[i-1][0].get(tolerance), attempts[i][0].get(tolerance)
                    if previous is None or current is None or not math.isclose(current * 4, previous, rel_tol=1e-12):
                        reasons.append("extra tolerance is not fourfold tighter: " + tolerance)
            primary, refined = attempts[-2:]
            change = discrepancy(primary[1], refined[1])
            reasons.extend("primary: " + reason for reason in primary[0]["reasons"])
            reasons.extend("refined: " + reason for reason in refined[0]["reasons"])
            if change is None or change > GATE:
                reasons.append("selected endpoint refinement maximum exceeds 0.01 or is unavailable")
            for tolerance in ("rtol", "atol"):
                left, right = primary[0].get(tolerance), refined[0].get(tolerance)
                if left is None or right is None or right >= left:
                    reasons.append("selected tolerances are not successively tighter: " + tolerance)
            validation[key] = dict(case=case, method=method, valid=not reasons, reasons=reasons,
                                   refinement_max=change, attempts=[a[0] for a in attempts], branch_checks=branch_checks)
            selection[key] = dict(primary=primary[0], refined=refined[0], valid=not reasons,
                                  refinement_max=change, reasons=reasons)
            audited[method] = (primary, refined)
            if not frozen:
                eligible = (extras < MAX_EXTRA_PER_CELL and primary[0]["valid"] and refined[0]["valid"]
                            and change is not None and change > GATE and not branch_checks)
                gates.append(dict(cell=key, eligible=bool(eligible), extras_attempted=extras,
                                  refinement_max=change, status="eligible" if eligible else "closed",
                                  next_rtol=refined[0].get("rtol", 0) / 4 if eligible else None,
                                  next_atol=refined[0].get("atol", 0) / 4 if eligible else None))
            for level, attempt in (("primary", primary), ("refined", refined)):
                if attempt[1] is not None:
                    pointwise[key + "_" + level + "_prediction"] = attempt[1]["prediction"].cpu().numpy()
                    pointwise[case + "_angles"] = attempt[1]["angles"]
        full_check = validation[case + "_full"]
        for method in METHODS:
            family, order = method.split("_p")
            p = int(order)
            k1, k2 = COUNTS[family][p]
            check = validation[case + "_" + method]
            row = dict(case=case, method=method, p=p, family=family, K1=k1, K2=k2, vectors=k1+k2,
                       valid=check["valid"] and full_check["valid"],
                       reasons=check["reasons"] + ["full: " + r for r in full_check["reasons"]],
                       refinement_max=check["refinement_max"], full_refinement_max=full_check["refinement_max"])
            for index, level in enumerate(("primary", "refined")):
                record, bundle = audited[method][index]
                full_record, reference = audited["full"][index]
                row.update({level + "_" + key: record.get(key) for key in ("path", "rtol", "atol", "loss", "time", "status")})
                row[level + "_full_path"] = full_record["path"]
                row[level + "_eligible"] = record["valid"] and full_record["valid"]
                for metric in ("rms", "l1", "mse", "max_abs"):
                    for suffix in ("", "_grid4096", "_grid_change"):
                        row[level + "_" + metric + suffix] = None
                if aligned(bundle, reference):
                    measured = metrics(bundle["prediction"], reference["prediction"])
                    nested = metrics(bundle["prediction"][::2], reference["prediction"][::2])
                    for metric, value in measured.items():
                        row[level + "_" + metric] = value
                        row[level + "_" + metric + "_grid4096"] = nested[metric]
                        row[level + "_" + metric + "_grid_change"] = finite_number(
                            (tensor(value, device) - tensor(nested[metric], device)).abs()) if value is not None and nested[metric] is not None else None
                        if value is None:
                            row["valid"] = False
                            row["reasons"].append("nonfinite " + level + " " + metric)
                else:
                    row["valid"] = False
                    row["reasons"].append(level + " predictor/reference grids or training data disagree")
            row["max_abs"] = row["refined_max_abs"]
            rows.append(row)
        print(json.dumps(dict(case=case, valid_rows=sum(r["valid"] for r in rows if r["case"] == case))), flush=True)
        del audited, full_attempts, origins
        torch.cuda.empty_cache()
    comparisons = []
    lookup = {(row["case"], row["family"], row["p"]): row for row in rows}
    for case in CASES:
        for p in (1, 2, 3):
            new, old = lookup[case, "new", p], lookup[case, "old", p]
            winners = []
            item = dict(case=case, p=p, valid=new["valid"] and old["valid"])
            for level in ("primary", "refined"):
                a, b = new[level + "_rms"], old[level + "_rms"]
                winner = ("new" if a < b else "old" if b < a else "tie") if a is not None and b is not None else "unavailable"
                item.update({level + "_new_rms": a, level + "_old_rms": b, level + "_winner": winner,
                             level + "_old_over_new_rms": finite_number(tensor(b, device) / tensor(a, device)) if a is not None and b is not None and a > 0 else None})
                winners.append(winner)
            item["ordering_agrees"] = winners[0] == winners[1] and winners[0] != "unavailable"
            item["verdict"] = winners[0] if item["valid"] and item["ordering_agrees"] else "inconclusive"
            comparisons.append(item)
    write_json(out / "metrics.json", rows)
    write_json(out / "validation.json", validation)
    write_json(out / "selected_levels.json", dict(cells=selection))
    write_json(out / "comparisons.json", comparisons)
    write_json(out / "gates.json", dict(rule="Only fitted replay-valid predictors with own endpoint cross-level maximum >0.01; no performance trigger.",
               max_extra_per_cell=MAX_EXTRA_PER_CELL, max_extra_total=8, extras_attempted=extra_count,
               cells=gates, eligible_cells=[g["cell"] for g in gates if g["eligible"]]))
    np.savez(out / "endpoint_predictions.npz", **pointwise)
    write_json(out / "provenance.json", dict(command=sys.argv, device=device, gpu=torch.cuda.get_device_name(device),
               python=sys.version, torch=str(torch.__version__), numpy=np.__version__, dtype="float64",
               width=WIDTH, network_seed=20260920, cases=CASES, counts=COUNTS, threshold=THRESHOLD,
               replay_tolerance=REPLAY, refinement_gate=GATE, roots=[str(root) for root in roots],
               selection_policy="latest two attempted levels for new/old-p2; frozen archive levels for old-p1/p3/full",
               endpoint_definition="Each predictor's own first detected unhalved training-MSE 0.001 crossing",
               error_definition="RMS/L1/MSE/sampled maximum versus corresponding selected full reference on 8192 uniform angles; nested 4096 diagnostics",
               analyzer_sha256=digest(__file__), input_hashes=HASHES.copy(),
               output_hashes={str(path): digest(path) for path in sorted(out.iterdir()) if path.is_file()}))
    print(json.dumps(dict(out=str(out), valid_rows=sum(row["valid"] for row in rows),
                          eligible_extra_cells=sum(g["eligible"] for g in gates))), flush=True)


if __name__ == "__main__":
    main()
