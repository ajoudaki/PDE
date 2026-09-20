"""Independent saved-state audit. Does not import any benchmark/analyzer logic.

Only NumPy file I/O uses the CPU; prediction, dictionary algebra and metric
reductions use CUDA float64. Run only after supervisor GPU coordination.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time

import numpy as np
import torch

from scaling_cases import DISCOVERY, CONFIRMATION

REPO = Path(__file__).resolve().parents[2]
STUDY = Path(__file__).resolve().parent
DATA = REPO / "data/generated/random_dictionary_learned_circle_20260920"
FORMULAS = {
    "full": "h=tanh(w@u.T); H=tanh(M@h); f=c@H/n",
    "closure": "h=tanh(w@u.T); a=b1.T@h/n; H=tanh(b2@M@a); f=c@H/n",
    "norms": "L1=mean(abs(delta)); MSE=mean(delta**2); RMS=sqrt(MSE); max=max(abs(delta))",
}


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for part in iter(lambda: stream.read(8 << 20), b""):
            h.update(part)
    return h.hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def relative(path):
    return str(Path(path).resolve().relative_to(REPO))


def parse_key(key):
    if key.endswith("_full"):
        return key[:-5], "full", 0
    for method in ("ours", "gaussian", "orthogonal"):
        token = "_" + method + "_p"
        if token in key:
            case, order = key.rsplit(token, 1)
            return case, method, int(order)
    raise ValueError("Unrecognized cell key: " + key)


class Audit:
    def __init__(self, args):
        self.args = args
        self.device = torch.device(args.device)
        self.checks = []
        self.hashes = {}
        self.source_records = []
        self.replays = {}
        self.dictionaries = {}
        self.metrics = []
        self.refinements = {}
        self.started = time.monotonic()

    def check(self, name, ok, **details):
        self.checks.append(dict(name=name, passed=bool(ok), **details))
        return bool(ok)

    def hashed(self, path):
        path = Path(path).resolve()
        if path not in self.hashes:
            self.hashes[path] = digest(path)
        return self.hashes[path]

    def tensor(self, x):
        return torch.as_tensor(x, device=self.device, dtype=torch.float64)

    def maximum(self, x):
        return float(x.abs().max().item())

    def norms(self, x):
        return {key: float(value.item()) for key, value in self.norm_tensors(x).items()}

    def norm_tensors(self, x):
        mse = x.square().mean()
        return dict(l1=x.abs().mean(), mse=mse, rms=mse.sqrt(), max_abs=x.abs().max())

    def source_hashes(self, config_path, config):
        for name, expected in config.get("source_hashes", {}).items():
            # Hash bytes only: this never decodes or imports analyzer/review code.
            path = (REPO / name).resolve()
            permitted = path.is_relative_to(STUDY) or path.is_relative_to(REPO / "code")
            record = dict(config=relative(config_path), source=name, expected=expected,
                          permitted=permitted)
            if permitted and path.is_file():
                record.update(actual=self.hashed(path), matches=self.hashed(path) == expected)
            else:
                record.update(actual=None, matches=False)
            producer_names = {"benchmark.py", "diverse_benchmark.py", "scaling_benchmark.py",
                "diverse_refine.py", "scaling_refine.py", "diverse_dictionary.py", "scaling_dictionary.py",
                "diverse_cases.py", "scaling_cases.py"}
            record["role"] = "producer_dependency" if name.startswith("code/") or path.name in producer_names else "incidental_manifest_entry"
            if record["role"] == "producer_dependency":
                self.check(relative(config_path) + ":producer_hash:" + name, record["matches"],
                           expected=expected, actual=record["actual"])
            self.source_records.append(record)
        if "protocol_sha256" in config:
            protocol_path = Path(config.get("protocol_path", STUDY / "SCALING_PROTOCOL.md")).resolve()
            if protocol_path.parent != STUDY:
                raise ValueError("Protocol path outside assigned study: " + str(protocol_path))
            self.check(relative(config_path) + ":protocol_hash",
                       self.hashed(protocol_path) == config["protocol_sha256"])

    def collect(self):
        attempts = defaultdict(list)
        all_cases = dict(DISCOVERY)
        for cases in CONFIRMATION.values():
            all_cases.update(cases)
        declared = []
        for root_arg in self.args.raw_roots:
            root = Path(root_arg).resolve()
            if root.parent != DATA or not root.name.startswith(("scaling_", "diverse_")):
                raise ValueError("Raw root outside assigned scope: " + str(root))
            for cp in sorted(root.glob("config*worker*.json")):
                config = read_json(cp)
                self.hashed(cp)
                self.source_hashes(cp, config)
                rp = cp.with_name(cp.name.replace("config", "results", 1))
                if not rp.exists():
                    self.check(relative(cp) + ":results_present", False)
                    continue
                results = read_json(rp)
                self.hashed(rp)
                expected = config.get("selected_cells")
                if expected is None and "own_selected" in config:
                    expected = [x["key"] for x in config["own_selected"]]
                if expected is not None:
                    self.check(relative(cp) + ":declared_executed", set(expected) == set(results),
                               missing=sorted(set(expected) - set(results)),
                               unexpected=sorted(set(results) - set(expected)))
                if "orders_executed" in config:
                    actual_orders = sorted({parse_key(k)[2] for k in results if parse_key(k)[1] != "full"})
                    self.check(relative(cp) + ":orders_executed",
                               actual_orders == sorted(config["orders_executed"]),
                               actual=actual_orders, declared=config["orders_executed"])
                declared.append(dict(config=relative(cp), expected=expected,
                                     executed=sorted(results), rtol=config["rtol"], atol=config["atol"]))
                for key, result in results.items():
                    case, method, order = parse_key(key)
                    if case not in self.args.cases:
                        continue
                    self.check(relative(cp) + ":case:" + case,
                               config["cases"][case] == all_cases[case])
                    cell = root / key
                    summary_path = cell / "summary.json"
                    arrays_path = cell / "arrays.npz"
                    if summary_path.exists():
                        summary = read_json(summary_path)
                        self.hashed(summary_path)
                        self.check(relative(summary_path) + ":results_agree", summary == result)
                    else:
                        summary = result
                    self.check(relative(cell) + ":tolerance",
                               summary.get("rtol", config["rtol"]) == config["rtol"] and
                               summary.get("atol", config["atol"]) == config["atol"])
                    attempts[key].append(dict(key=key, case=case, method=method, order=order,
                        cell=cell, arrays=arrays_path, config=config, config_path=cp,
                        summary=summary, rtol=config["rtol"], atol=config["atol"],
                        started=config.get("started_utc", "")))
        selections = {}
        for key, records in sorted(attempts.items()):
            # Finest two attempted tolerances, including unsuccessful attempts.
            records.sort(key=lambda r: (-r["rtol"], -r["atol"], r["started"], str(r["cell"])))
            tol_groups = defaultdict(list)
            for record in records:
                tol_groups[(record["rtol"], record["atol"])].append(record)
            unique = []
            for tolerance in sorted(tol_groups, reverse=True):
                same = tol_groups[tolerance]
                unique.append(same[-1])
                self.check(key + ":unique_tolerance:" + str(tolerance), len(same) == 1,
                           roots=[r["cell"].parent.name for r in same])
            self.check(key + ":two_attempts", len(unique) >= 2, attempts=len(unique))
            selections[key] = unique[-2:]
        return selections, declared

    def predict(self, z, snapshot, inputs):
        w = self.tensor(z["w"][snapshot])
        c = self.tensor(z["c"][snapshot])
        middle = self.tensor(z["M"][snapshot])
        n = len(c)
        b1 = self.tensor(z["b1"]) if "b1" in z else None
        b2 = self.tensor(z["b2"]) if "b2" in z else None
        outputs = []
        # Small chunks cap memory regardless of endpoint or carrier size.
        for u in inputs.split(512):
            h = torch.tanh(w @ u.T)
            if b1 is None:
                pre = middle @ h
            else:
                projected = (b1.T @ h) / n
                pre = b2 @ (middle @ projected)
            outputs.append(c @ torch.tanh(pre) / n)
        return torch.cat(outputs)

    def dictionary(self, record, z):
        if record["method"] == "full":
            return
        prefix = relative(record["cell"])
        root = record["cell"].parent
        matching = sorted(root.glob("dictionary_*_" + record["method"] + "_p" + str(record["order"]) + ".json"))
        metadata = None
        if matching:
            # Workers share the same initialized dictionaries; require agreement.
            metadata = read_json(matching[0])
            for path in matching:
                self.hashed(path)
                self.check(relative(path) + ":dictionary_metadata_equal", read_json(path) == metadata)
            self.check(prefix + ":dictionary_all_finite", metadata.get("all_finite") is True)
            self.check(prefix + ":dictionary_identity",
                       metadata["method"] == record["method"] and
                       metadata["order"] == record["order"] and
                       metadata["width"] == record["config"]["width"] and
                       metadata["dictionary_seed"] == record["config"]["dictionary_seed"])
        populations = []
        for layer in (1, 2):
            basis = self.tensor(z["b" + str(layer)])
            gram = basis.T @ basis / basis.shape[0]
            eigenvalues = torch.linalg.eigvalsh(gram)
            self.check(prefix + f":basis{layer}_finite", bool(torch.isfinite(basis).all()))
            reported = self.tensor(record["summary"]["gram_eigenvalues"][layer - 1])
            residual = self.maximum(eigenvalues - reported)
            self.check(prefix + f":basis{layer}_spectrum_replay", residual <= 1e-11, error=residual)
            rank = int((eigenvalues > eigenvalues[-1] * 1e-10).sum().item())
            entry = dict(layer=layer, count=basis.shape[1], numerical_rank=rank,
                         min_eigenvalue=float(eigenvalues[0].item()),
                         max_eigenvalue=float(eigenvalues[-1].item()),
                         spectrum_replay_error=residual)
            if record["method"] == "orthogonal":
                residual = self.maximum(gram - torch.eye(gram.shape[0], device=self.device))
                self.check(prefix + f":basis{layer}_orthogonal", residual <= 1e-8, error=residual)
                entry["orthogonal_residual"] = residual
            if record["method"] == "gaussian":
                residual = self.maximum(gram.diag() - 1)
                self.check(prefix + f":basis{layer}_unit_rms", residual <= 1e-11, error=residual)
                entry["unit_rms_squared_residual"] = residual
            if metadata:
                pop = metadata["populations"][layer - 1]
                self.check(prefix + f":basis{layer}_metadata_rank", rank == pop["numerical_rank"])
                self.check(prefix + f":basis{layer}_metadata_finite", all(pop["finite_checks"].values()))
                if record["method"] == "ours":
                    ridge = 1 / (1024 * (record["order"] + 1) ** 2)
                    condition = ((pop["raw_gram_max_eigenvalue"] + ridge) /
                                 (pop["raw_gram_min_eigenvalue"] + ridge))
                    self.check(prefix + f":basis{layer}_fixed_ridge", metadata["ridge"] == ridge)
                    self.check(prefix + f":basis{layer}_recorded_ridge_gate", condition <= 1e10,
                               condition=condition)
                    self.check(prefix + f":basis{layer}_recorded_triangular_gate",
                               pop["triangular_solve_residual"] <= 1e-8,
                               error=pop["triangular_solve_residual"])
                    entry.update(recorded_raw_gram_condition=condition,
                                 recorded_triangular_residual=pop["triangular_solve_residual"])
            populations.append(entry)
        self.dictionaries[prefix] = dict(populations=populations,
            raw_cholesky_reconstruction="Not possible from saved arrays: raw basis and Cholesky factor absent.")

    def replay(self, record):
        path = record["arrays"]
        prefix = relative(record["cell"])
        if prefix in self.replays:
            return self.replays[prefix]
        summary, config = record["summary"], record["config"]
        fitted = summary.get("status") == "fitted" and summary.get("loss", math.inf) <= config["threshold"] + 1e-10
        self.check(prefix + ":fit", fitted, status=summary.get("status"), loss=summary.get("loss"))
        if not path.exists():
            self.check(prefix + ":arrays_present", False)
            self.replays[prefix] = dict(fitted=fitted, replay_pass=False)
            return self.replays[prefix]
        self.hashed(path)
        initial_count = len(self.checks)
        with np.load(path, allow_pickle=False) as archive:
            z = {name: archive[name] for name in archive.files}
            n = config["width"]
            angles = self.tensor(z["endpoint_angles"])
            inputs = self.tensor(z["endpoint_inputs"])
            expected_angles = torch.arange(8192, device=self.device, dtype=torch.float64) * (2 * math.pi / 8192)
            self.check(prefix + ":endpoint_shape", z["endpoint_prediction"].shape == (8192,) and
                       z["endpoint_inputs"].shape == (8192, 2) and z["endpoint_angles"].shape == (8192,))
            self.check(prefix + ":endpoint_grid", self.maximum(angles - expected_angles) <= 2e-14)
            self.check(prefix + ":endpoint_directions", self.maximum(inputs - torch.stack((angles.cos(), angles.sin()), 1)) <= 2e-14)
            self.check(prefix + ":nested_snapshot_grid", self.maximum(inputs[::4] - self.tensor(z["circle_inputs"])) <= 2e-14)
            target = config["cases"][record["case"]]
            training_angles = self.tensor(target["angles_degrees"]) * (math.pi / 180)
            self.check(prefix + ":training_geometry", self.maximum(self.tensor(z["training_inputs"]) -
                       torch.stack((training_angles.cos(), training_angles.sin()), 1)) <= 2e-14)
            self.check(prefix + ":training_labels", bool(torch.equal(self.tensor(z["labels"]), self.tensor(target["labels"]))))
            count = z["snapshot_times"].shape[0]
            self.check(prefix + ":state_shapes", z["w"].shape == (count, n, 2) and
                       z["c"].shape == (count, n) and z["M"].shape[0] == count and
                       z["circle_predictions"].shape == (count, 2048))
            self.check(prefix + ":float64", all(z[k].dtype == np.float64 for k in
                       ("w", "c", "M", "endpoint_prediction", "endpoint_inputs")))
            for name in ("w", "c", "M", "endpoint_prediction", "losses", "times"):
                self.check(prefix + ":finite:" + name, bool(torch.isfinite(self.tensor(z[name])).all()))
            self.check(prefix + ":terminal_time", abs(float(z["snapshot_times"][-1]) - summary["time"]) <= 1e-10 and
                       abs(float(z["times"][-1]) - summary["time"]) <= 1e-10)
            losses = self.tensor(z["losses"])
            self.check(prefix + ":loss_summary", abs(float(losses[-1].item()) - summary["loss"]) <= 1e-10)
            self.check(prefix + ":first_crossing", bool((losses[:-1] > config["threshold"] - 1e-10).all()) if fitted else True)
            self.check(prefix + ":decreasing_loss", bool(((losses[1:] - losses[:-1]) <= 1e-10).all()))
            training = self.tensor(z["training_inputs"])
            labels = self.tensor(z["labels"])
            errors = {}
            for snapshot, label in ((0, "initial"), (-1, "terminal")):
                prediction = self.predict(z, snapshot, self.tensor(z["circle_inputs"]))
                errors[label + "_circle"] = self.maximum(prediction - self.tensor(z["circle_predictions"][snapshot]))
                train_prediction = self.predict(z, snapshot, training)
                loss = float((train_prediction - labels).square().mean().item())
                errors[label + "_loss"] = abs(loss - summary["initial_loss" if snapshot == 0 else "loss"])
            prediction = self.predict(z, -1, inputs)
            errors["terminal_endpoint"] = self.maximum(prediction - self.tensor(z["endpoint_prediction"]))
            for name, error in errors.items():
                self.check(prefix + ":replay:" + name, error <= 1e-10, error=error)
            if "p1" in z:
                self.check(prefix + ":uniform_carriers", self.maximum(self.tensor(z["p1"]) - 1 / n) == 0 and
                           self.maximum(self.tensor(z["p2"]) - 1 / n) == 0)
                self.check(prefix + ":initial_dictionary_state", self.maximum(self.tensor(z["M"][0]) - self.tensor(z["D"])) == 0 and
                           self.maximum(self.tensor(z["w"][0]) - self.tensor(z["g"])) == 0)
            self.dictionary(record, z)
        self.replays[prefix] = dict(fitted=fitted, errors=errors,
            replay_pass=all(c["passed"] for c in self.checks[initial_count:]))
        return self.replays[prefix]

    def difference(self, left, right):
        # Deliberately load only this endpoint pair; no eager GPU bank of models.
        with np.load(left["arrays"], allow_pickle=False) as a, np.load(right["arrays"], allow_pickle=False) as b:
            self.check(relative(left["cell"]) + ":pair_grid:" + relative(right["cell"]),
                       np.array_equal(a["endpoint_angles"], b["endpoint_angles"]) and
                       np.array_equal(a["endpoint_inputs"], b["endpoint_inputs"]))
            delta = self.tensor(a["endpoint_prediction"]) - self.tensor(b["endpoint_prediction"])
            fine_t = self.norm_tensors(delta)
            nested_t = self.norm_tensors(delta[::2])
            self.last_nested_sensitivity = {key: float((fine_t[key] - nested_t[key]).abs().item()) for key in fine_t}
            fine = {key: float(value.item()) for key, value in fine_t.items()}
            nested = {key: float(value.item()) for key, value in nested_t.items()}
        return fine, nested

    def run(self):
        torch.set_default_dtype(torch.float64)
        if self.device.type != "cuda" or not torch.cuda.is_available():
            raise ValueError("CUDA float64 is mandatory")
        torch.backends.cuda.matmul.allow_tf32 = False
        selected, declared = self.collect()
        historical_path = DATA / "diverse_analysis01/selected_levels.json"
        needs_historical = any(records[0]["case"] in DISCOVERY and records[0]["config"]["width"] == 2048 and records[0]["method"] != "full" and
                               records[0]["order"] in (1, 3, 5) for records in selected.values())
        if needs_historical and historical_path.exists():
            historical = read_json(historical_path)["cells"]
            self.hashed(historical_path)
            for key, records in selected.items():
                if records[0]["method"] != "full" and records[0]["order"] in (1, 3, 5) and key in historical:
                    row = historical[key]
                    expected = [Path(row[name]).resolve() for name in ("primary_directory", "refined_directory")]
                    self.check(key + ":historical_selection", [r["cell"] for r in records] == expected)
        for key, records in selected.items():
            if time.monotonic() - self.started > self.args.max_seconds:
                raise TimeoutError("Independent checker time allocation exhausted")
            for record in records:
                self.replay(record)
            if len(records) == 2 and all(r["arrays"].exists() for r in records):
                fine, nested = self.difference(*records)
                valid = all(self.replays[relative(r["cell"])]["fitted"] and
                            self.replays[relative(r["cell"])]["replay_pass"] for r in records)
                self.refinements[key] = dict(fine=fine, nested4096=nested,
                    both_fitted=all(self.replays[relative(r["cell"])]["fitted"] for r in records),
                    numerically_valid=valid and fine["max_abs"] <= 0.01,
                    discrepancy_gate=fine["max_abs"] <= 0.01,
                    roots=[r["cell"].parent.name for r in records])
        for key, records in selected.items():
            if records[0]["method"] == "full":
                continue
            references = selected.get(records[0]["case"] + "_full", [])
            self.check(key + ":reference_two_levels", len(references) == 2)
            for level, (model, reference) in enumerate(zip(records, references)):
                if not model["arrays"].exists() or not reference["arrays"].exists():
                    continue
                fine, nested = self.difference(model, reference)
                self.metrics.append(dict(case=model["case"], method=model["method"], order=model["order"],
                    level=level, model_root=model["cell"].parent.name, reference_root=reference["cell"].parent.name,
                    model_rtol=model["rtol"], reference_rtol=reference["rtol"], **fine,
                    nested4096=nested, nested_sensitivity=dict(self.last_nested_sensitivity)))
            print("checked", key, flush=True)
        comparisons = self.compare_analysis() if self.args.analysis else None
        torch.cuda.synchronize(self.device)
        result = dict(scope="Independent internal empirical audit; no promotion review or retraining.",
            formulas=FORMULAS, command=sys.argv, cwd=str(Path.cwd()),
            environment=dict(python=platform.python_version(), numpy=np.__version__, torch=torch.__version__,
                             device=str(self.device), gpu=torch.cuda.get_device_name(self.device), dtype="float64"),
            declared_executed=declared,
            selected={key: [dict(root=r["cell"].parent.name, rtol=r["rtol"], atol=r["atol"],
                                 status=r["summary"].get("status")) for r in values] for key, values in selected.items()},
            checks=self.checks, metrics=self.metrics, refinements=self.refinements,
            replays=self.replays, dictionaries=self.dictionaries, comparisons=comparisons,
            source_hash_checks=self.source_records,
            input_hashes={str(k): v for k, v in sorted(self.hashes.items())},
            checker_sha256=digest(__file__), wall_seconds=time.monotonic() - self.started,
            technical_checks_passed=all(c["passed"] for c in self.checks),
            all_selected_numerically_valid=all(v["numerically_valid"] for v in self.refinements.values()),
            limitations=["No independent integration or verification of every RHS step.",
                "Raw basis and Cholesky factors are absent; their condition/triangular gates use recorded metadata.",
                "Finite-level differences are empirical diagnostics, not certified ODE errors.",
                "Source manifest drift is listed explicitly; unused documentation/analysis sources may change."])
        self.args.out.mkdir(parents=True, exist_ok=False)
        (self.args.out / "checks.json").write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
        print(json.dumps({k: result[k] for k in ("technical_checks_passed", "all_selected_numerically_valid", "wall_seconds")}, indent=2))
        return result

    def compare_analysis(self):
        # Analyzer output is an object to check, never an implementation input.
        path = self.args.analysis / "metrics.json"
        author = read_json(path)
        self.hashed(path)
        if not isinstance(author, list):
            raise ValueError("Unexpected metrics schema; inspect raw schema and add explicit adapter")
        comparisons = []
        for ours in self.metrics:
            candidates = [row for row in author if row.get("case") == ours["case"] and
                          row.get("method") == ours["method"] and row.get("order") == ours["order"]]
            self.check(f"analysis_row:{ours['case']}:{ours['method']}:{ours['order']}:{ours['level']}", len(candidates) == 1)
            if len(candidates) != 1:
                continue
            row = candidates[0]
            prefix = "refined_" if ours["level"] else ""
            model_path = Path(row[prefix + "directory"])
            reference_path = Path(row["full_refined_directory" if ours["level"] else "full_directory"])
            self.check("analysis_selected_paths:" + str((ours["case"], ours["method"], ours["order"], ours["level"])),
                       model_path.parent.name == ours["model_root"] and reference_path.parent.name == ours["reference_root"])
            errors = {}
            for metric, name in {"l1": "l1", "mse": "mse", "rms": "l2", "max_abs": "max_abs"}.items():
                field = prefix + name
                if row.get(field) is None:
                    self.check("analysis_noneligible_null:" + metric, row.get(prefix + "eligible") is False)
                    field = prefix + "terminal_" + name
                self.check("analysis_field:" + metric, field in row and row[field] is not None)
                if field in row and row[field] is not None:
                    errors[metric] = abs(float(row[field]) - ours[metric])
                    self.check(f"analysis_metric:{ours['case']}:{ours['method']}:{ours['order']}:{ours['level']}:{metric}",
                               errors[metric] <= 1e-11, error=errors[metric])
            for metric, field in (("rms", "grid_l2_change"), ("max_abs", "grid_max_change")):
                error = abs(ours["nested_sensitivity"][metric] - row[prefix + field])
                self.check("analysis_nested_grid:" + str((ours["case"], ours["method"], ours["order"], ours["level"], metric)),
                           error <= 1e-11, error=error)
            key = f"{ours['case']}_{ours['method']}_p{ours['order']}"
            error = abs(self.refinements[key]["fine"]["max_abs"] - row["step_refinement_endpoint_max"])
            self.check("analysis_own_refinement:" + key, error <= 1e-11, error=error)
            reference_key = ours["case"] + "_full"
            error = abs(self.refinements[reference_key]["fine"]["max_abs"] - row["full_step_refinement_endpoint_max"])
            self.check("analysis_full_refinement:" + key, error <= 1e-11, error=error)
            independent_valid = self.refinements[key]["numerically_valid"] and self.refinements[reference_key]["numerically_valid"]
            self.check("analysis_validity:" + key, row["valid"] == independent_valid,
                       reported=row["valid"], independent=independent_valid)
            comparisons.append(dict(case=ours["case"], method=ours["method"], order=ours["order"],
                                    level=ours["level"], absolute_errors=errors))
        return comparisons


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw-roots", nargs="+", required=True)
    parser.add_argument("--cases", nargs="+", default=list(DISCOVERY))
    parser.add_argument("--analysis", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--max-seconds", type=float, default=180)
    args = parser.parse_args()
    args.out = args.out.resolve()
    if args.out.parent != DATA or not args.out.name.startswith("scaling_independent_check"):
        raise ValueError("Output must be the assigned independent-check namespace")
    with torch.inference_mode():
        Audit(args).run()


if __name__ == "__main__":
    main()
