"""Hash-checked paired analysis of the frozen dense-initialization campaign.

No training is performed. The primary unit of replication is a seed, with
20,000 deterministic bootstrap resamples (seed 0). Per-cell intervals are
descriptive, not simultaneous across the suite. Aggregate intervals resample
entire seed blocks across tasks and widths, preserving their dependence.

Example:
  python analyze_dense_comparison.py --base BASE --continuation CONT \
      --refinement HALF_DT --output ANALYSIS

Successful continuation artifacts replace the same key, retaining earlier
snapshots. Failed continuation attempts are retained in status columns while
earlier valid snapshots remain available. Default operation requires completed,
hashed directories. --allow-incomplete is explicitly provisional and disables
all 'close' classifications. Runtime inputs are JSON/NPZ artifacts only.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass, field
import hashlib
import json
from pathlib import Path
import sys

import numpy as np

from circle_tasks import BY_NAME


BOOTSTRAP_RESAMPLES = 20_000
BOOTSTRAP_SEED = 0
STAGES = ("fit6", "time300", "fit8")
MAIN_STAGES = ("fit6", "time300")
_BOOTSTRAP_CACHE: dict[int, np.ndarray] = {}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def _finite(value, name: str) -> float:
    result = float(value)
    if not np.isfinite(result):
        raise ValueError(f"nonfinite {name}")
    return result


def _same(actual: float, recorded: float, name: str) -> None:
    if not np.isclose(actual, recorded, rtol=2e-10, atol=2e-12):
        raise ValueError(f"recomputed {name} differs: {actual} versus {recorded}")


def _rms(values: np.ndarray) -> float:
    return float(np.sqrt(np.mean(np.square(values))))


def _stats(values) -> dict:
    values = np.asarray(values, dtype=float)
    if not len(values):
        return {"mean": None, "median": None, "std": None}
    return {"mean": float(np.mean(values)), "median": float(np.median(values)),
            "std": float(np.std(values, ddof=1)) if len(values) > 1 else None}


def _ci(values) -> tuple[float, float]:
    low, high = np.quantile(values, [.025, .975])
    return float(low), float(high)


def bootstrap_indices(n: int) -> np.ndarray:
    if n not in _BOOTSTRAP_CACHE:
        _BOOTSTRAP_CACHE[n] = np.random.default_rng(BOOTSTRAP_SEED).integers(
            n, size=(BOOTSTRAP_RESAMPLES, n))
    return _BOOTSTRAP_CACHE[n]


@dataclass
class Snapshot:
    time: float
    train_mse: float
    risk: float
    base_risk: float
    target_rms: float
    prediction: np.ndarray
    grid_points: int
    refined_prediction: np.ndarray | None
    grid_delta: float
    grid_pass: bool
    details: dict


@dataclass
class Run:
    task: str
    width: int
    seed: int
    method: str
    dt: float
    key: str
    status: str
    source: str
    record: dict = field(default_factory=dict)
    snapshots: dict[str, Snapshot] = field(default_factory=dict)
    attempts: list[dict] = field(default_factory=list)
    json_hash: str = ""
    data_hash: str = ""

    @property
    def identity(self):
        return self.task, self.width, self.seed, self.method


class Provenance:
    def __init__(self):
        self.hashes: dict[str, str] = {}
        self.checked_against_index: set[str] = set()

    def check(self, path: Path, expected: str | None = None, *, from_index: bool = False) -> str:
        path = path.resolve()
        actual = digest(path)
        if expected is not None:
            if actual != expected:
                raise ValueError(f"SHA256 mismatch: {path}")
            if from_index:
                self.checked_against_index.add(str(path))
        previous = self.hashes.get(str(path))
        if previous is not None and previous != actual:
            raise ValueError(f"input changed while analyzing: {path}")
        self.hashes[str(path)] = actual
        return actual

    def recheck(self) -> None:
        for name, expected in self.hashes.items():
            if digest(Path(name)) != expected:
                raise ValueError(f"input changed while analyzing: {name}")


def _read_json(path: Path, hashes: dict, provenance: Provenance,
               require_index: bool) -> tuple[dict, str]:
    expected = hashes.get(path.name)
    if require_index and expected is None:
        raise ValueError(f"artifact index has no JSON hash: {path}")
    actual = provenance.check(path, expected, from_index=expected is not None)
    return json.loads(path.read_text()), actual


def load_directory(folder: Path, provenance: Provenance,
                   allow_incomplete: bool = False) -> tuple[dict, dict[str, Run], dict]:
    folder = folder.resolve()
    index_path = folder / "artifact_hashes.json"
    hashes = {}
    if index_path.exists():
        provenance.check(index_path)
        hashes = json.loads(index_path.read_text())
        if not isinstance(hashes, dict):
            raise ValueError(f"invalid artifact hash index in {folder}")
        for name in hashes:
            if Path(name).name != name:
                raise ValueError(f"nonlocal artifact-index path: {name}")
            if not (folder/name).is_file() and not allow_incomplete:
                raise ValueError(f"indexed artifact is missing: {folder/name}")
    elif not allow_incomplete:
        raise ValueError(f"completed artifact hash index is absent: {folder}")
    require_index = bool(hashes) and not allow_incomplete
    manifest, _ = _read_json(folder / "manifest.json", hashes, provenance, require_index)
    completion = None
    if (folder / "completion.json").exists():
        completion, _ = _read_json(folder / "completion.json", hashes, provenance, require_index)
    complete = (completion is not None
                and completion.get("completed") == completion.get("total"))
    if not complete and not allow_incomplete:
        raise ValueError(f"campaign has not completed: {folder}")
    runs = {}
    for path in sorted(folder.glob("*__dt*.json")):
        record, json_hash = _read_json(path, hashes, provenance, require_index)
        task, width, seed, method, dt = (
            record["task"], int(record["width"]), int(record["seed"]),
            record["method"], float(record["dt"]))
        key = f"{task}__n{width}__s{seed:02d}__{method}__dt{dt:g}"
        if record.get("key") != key or path.stem != key:
            raise ValueError(f"run identity mismatch: {path}")
        run = Run(task, width, seed, method, dt, key, record["status"], str(folder),
                  record=record, json_hash=json_hash)
        if run.status not in ("ok", "failed"):
            raise ValueError(f"unknown run status in {path}: {run.status}")
        run.attempts.append({"source": str(folder), "status": run.status,
                             "error": record.get("error", ""), "json_sha256": json_hash})
        if run.status == "ok":
            if task not in BY_NAME:
                raise ValueError(f"unknown task {task}; use the frozen task source")
            data_path = (folder / record["data_file"]).resolve()
            if data_path.parent != folder or data_path.name != key + ".npz":
                raise ValueError(f"invalid run data path: {data_path}")
            run.data_hash = provenance.check(data_path, record["data_sha256"])
            if require_index and data_path.name not in hashes:
                raise ValueError(f"artifact index has no NPZ hash: {data_path}")
            if data_path.name in hashes:
                provenance.check(data_path, hashes[data_path.name], from_index=True)
            with np.load(data_path, allow_pickle=False) as data:
                angles, target = data["angles"].copy(), data["target"].copy()
                labels = data["train_labels"].copy()
                train_angles = data["train_angles"].copy()
                count = len(angles)
                if (angles.shape != (count,) or target.shape != (count,) or count < 8
                        or count % 2 or not np.all(np.isfinite(target))):
                    raise ValueError(f"invalid query grid: {data_path}")
                if not np.allclose(angles, 2*np.pi*np.arange(count)/count,
                                   rtol=0, atol=1e-12):
                    raise ValueError(f"query grid changed: {data_path}")
                if not np.allclose(target, BY_NAME[task].target(angles),
                                   rtol=1e-12, atol=1e-12):
                    raise ValueError(f"teacher data differs from frozen task: {data_path}")
                _, expected_labels = BY_NAME[task].data()
                if (train_angles.shape != np.asarray(BY_NAME[task].angles).shape
                        or not np.allclose(train_angles, BY_NAME[task].angles,
                                           rtol=1e-12, atol=1e-12)):
                    raise ValueError(f"training angles changed: {data_path}")
                if not np.allclose(labels, expected_labels, rtol=1e-12, atol=1e-12):
                    raise ValueError(f"training labels changed: {data_path}")
                target_rms = _rms(target)
                if target_rms <= 0:
                    raise ValueError("target RMS must be positive")
                _same(target_rms, record["target_rms"], "target RMS")
                for stage, details in record["records"].items():
                    pred, train = data[stage + "_circle"].copy(), data[stage + "_train"].copy()
                    if (pred.shape != target.shape or train.shape != labels.shape
                            or not np.all(np.isfinite(pred)) or not np.all(np.isfinite(train))):
                        raise ValueError(f"invalid {stage} predictions in {data_path}")
                    risk = _rms(pred-target)
                    train_mse = float(np.mean((train-labels)**2))
                    _same(risk, details["test_rms"], "base-grid test RMS")
                    _same(risk/target_rms, details["normalized_test_rms"], "normalized risk")
                    _same(train_mse, details["train_mse"], "training MSE")
                    snapshot_time = _finite(details["time"], "snapshot time")
                    if snapshot_time < 0:
                        raise ValueError(f"negative snapshot time in {data_path}")
                    if stage.startswith("time") and abs(snapshot_time-float(stage[4:])) > 1e-7:
                        raise ValueError(f"incorrect common-time label {stage}: {data_path}")
                    if stage in ("fit6", "fit8"):
                        threshold = 1e-6 if stage == "fit6" else 1e-8
                        if train_mse > threshold*(1+1e-9):
                            raise ValueError(f"unfitted threshold snapshot {stage}: {data_path}")
                    delta = abs(risk-_rms((pred-target)[::2]))
                    _same(delta, details["grid_refinement_delta"], "coarse-grid discrepancy")
                    fine, final_risk, grid_points = None, risk, count
                    if details.get("refined_test_rms") is not None:
                        if stage + "_circle_fine" not in data.files:
                            raise ValueError(f"missing refined array in {data_path}")
                        fine = data[stage + "_circle_fine"].copy()
                        if fine.shape != (2*count,) or not np.all(np.isfinite(fine)):
                            raise ValueError(f"invalid refined grid in {data_path}")
                        fine_target = BY_NAME[task].target(2*np.pi*np.arange(2*count)/(2*count))
                        final_risk = _rms(fine-fine_target)
                        _same(final_risk, details["refined_test_rms"], "refined risk")
                        if not np.allclose(fine[::2], pred, rtol=2e-10, atol=2e-12):
                            raise ValueError(f"refined predictions disagree on common grid: {data_path}")
                        delta, grid_points = abs(final_risk-risk), 2*count
                    # Resumed archives can retain an old fine array under a
                    # replaced final-stage key. Only the current JSON record
                    # declares whether that refined array belongs to this stage.
                    run.snapshots[stage] = Snapshot(
                        snapshot_time, train_mse, final_risk,
                        risk, target_rms, pred, grid_points, fine, delta,
                        delta <= 1e-4*target_rms, details)
        runs[key] = run
    info = {"directory": str(folder), "complete": complete, "hash_index_present": bool(hashes),
            "reported_completion": completion, "run_json_count": len(runs)}
    return manifest, runs, info


def merge_continuation(base: dict[str, Run], later: dict[str, Run]) -> None:
    for key, new in later.items():
        if key not in base:
            raise ValueError(f"continuation has no matching base key: {key}")
        old = base[key]
        if new.identity != old.identity or new.dt != old.dt:
            raise ValueError(f"continuation identity changed: {key}")
        attempts = old.attempts + new.attempts
        if new.status != "ok":
            old.attempts = attempts
            continue
        for stage in old.snapshots.keys() & new.snapshots.keys():
            if stage == "final":
                continue
            a, b = old.snapshots[stage], new.snapshots[stage]
            if a.time != b.time or not np.array_equal(a.prediction, b.prediction):
                raise ValueError(f"continuation changed earlier {stage}: {key}")
        if old.snapshots and new.snapshots["final"].time < old.snapshots["final"].time:
            raise ValueError(f"continuation moves backwards: {key}")
        new.snapshots = old.snapshots | new.snapshots
        new.attempts = attempts
        # A continuation's scalar max only covers that leg; retain the maximum.
        new.record["max_loss_rise"] = max(float(old.record.get("max_loss_rise", 0)),
                                           float(new.record.get("max_loss_rise", 0)))
        base[key] = new


def paired_predictions(a: Snapshot, b: Snapshot) -> tuple[np.ndarray, np.ndarray]:
    if a.refined_prediction is not None and b.refined_prediction is not None:
        if a.refined_prediction.shape == b.refined_prediction.shape:
            return a.refined_prediction,b.refined_prediction
    if a.prediction.shape != b.prediction.shape:
        raise ValueError("paired prediction grids differ")
    return a.prediction,b.prediction


def distance(a: Snapshot, b: Snapshot) -> tuple[float, int]:
    aa,bb=paired_predictions(a,b)
    return _rms(aa-bb),len(aa)


def complete_plan(manifest: dict, observed: dict[str, Run]) -> list[Run]:
    result = []
    for task in manifest["tasks"]:
        for width in manifest["widths"]:
            for seed in manifest["seeds"]:
                for method in manifest["methods"]:
                    dt = manifest["dt"]
                    key = f"{task}__n{width}__s{seed:02d}__{method}__dt{dt:g}"
                    result.append(observed.get(key, Run(task, width, seed, method, dt, key,
                                                        "missing", manifest["output"])))
    expected = {run.key for run in result}
    if set(observed)-expected:
        raise ValueError("base artifacts contain runs outside the manifest plan")
    return result


def per_run_rows(runs: list[Run]) -> list[dict]:
    lookup = {run.identity: run for run in runs}
    rows = []
    for run in runs:
        latest = run.attempts[-1] if run.attempts else {}
        row = {"task": run.task, "width": run.width, "seed": run.seed,
               "method": run.method, "dt": run.dt, "key": run.key,
               "status": run.status, "latest_attempt_status": latest.get("status", "missing"),
               "latest_error": latest.get("error", ""), "attempt_count": len(run.attempts),
               "source": run.source, "json_sha256": run.json_hash, "npz_sha256": run.data_hash,
               "has_fit6": "fit6" in run.snapshots, "has_fit8": "fit8" in run.snapshots,
               "has_time300": "time300" in run.snapshots,
               "max_loss_rise": run.record.get("max_loss_rise"),
               "loss_rise_exceeds_1e_7": float(run.record.get("max_loss_rise", 0)) > 1e-7,
               "initial_middle_frobenius_sq_over_n": run.record.get("initial_middle_frobenius_sq_over_n")}
        for stage in ("fit6", "time100", "time300", "fit8", "final"):
            snap = run.snapshots.get(stage)
            if snap is None:
                continue
            row.update({stage+"_time": snap.time, stage+"_train_mse": snap.train_mse,
                        stage+"_test_rms": snap.risk,
                        stage+"_normalized_test_rms": snap.risk/snap.target_rms,
                        stage+"_target_rms": snap.target_rms,
                        stage+"_risk_grid_points": snap.grid_points,
                        stage+"_base_grid_test_rms": snap.base_risk,
                        stage+"_grid_delta": snap.grid_delta,
                        stage+"_grid_pass": snap.grid_pass})
            for metric in ("h1_motion", "h2_motion", "w_motion", "middle_frobenius_motion", "readout_rms"):
                row[stage+"_"+metric] = snap.details.get(metric)
            reference = lookup.get((run.task, run.width, run.seed, "gaussian"))
            control = lookup.get((run.task, run.width, run.seed, "gaussian_control"))
            if reference is not None and stage in reference.snapshots:
                g = reference.snapshots[stage]
                d, count = distance(snap, g)
                candidate_prediction,gaussian_prediction=paired_predictions(snap,g)
                gaussian_rms=_rms(gaussian_prediction)
                row[stage+"_paired_gaussian_function_distance"] = d
                row[stage+"_canonical_gaussian_function_rms"] = gaussian_rms
                row[stage+"_relative_function_distance"] = d/gaussian_rms if gaussian_rms>0 else None
                row[stage+"_grid_sup_abs_function_error"] = float(np.max(np.abs(candidate_prediction-gaussian_prediction)))
                row[stage+"_function_distance_grid_points"] = count
                row[stage+"_paired_risk_difference"] = snap.risk-g.risk
                if control is not None and stage in control.snapshots:
                    dc, _ = distance(control.snapshots[stage], g)
                    row[stage+"_gaussian_control_function_distance"] = dc
                    row[stage+"_function_distance_ratio"] = d/dc if dc > 0 else None
        for later in ("fit8", "time300"):
            if "fit6" in run.snapshots and later in run.snapshots:
                a, b = run.snapshots["fit6"], run.snapshots[later]
                d, count = distance(a, b)
                row["fit6_to_"+later+"_function_drift_rms"] = d
                row["fit6_to_"+later+"_normalized_drift"] = d/a.target_rms
                row["fit6_to_"+later+"_risk_change"] = b.risk-a.risk
                row["fit6_to_"+later+"_time_difference"] = b.time-a.time
                row["fit6_to_"+later+"_grid_points"] = count
        rows.append(row)
    return rows


def paired_summary(runs: list[Run], manifest: dict, provisional: bool,
                   numerical_issues: dict[tuple, list[str]] | None = None) -> list[dict]:
    lookup = {run.identity: run for run in runs}
    numerical_issues = numerical_issues or {}
    seeds = sorted(manifest["seeds"])
    rows = []
    for task in manifest["tasks"]:
        for width in manifest["widths"]:
            for method in manifest["methods"]:
                for stage in STAGES:
                    threshold = 1e-8 if stage == "fit8" else 1e-6
                    methods = [lookup[(task,width,s,method)] for s in seeds]
                    refs = [lookup.get((task,width,s,"gaussian")) for s in seeds]
                    pairs = [(s,a.snapshots[stage],g.snapshots[stage])
                             for s,a,g in zip(seeds,methods,refs)
                             if stage in a.snapshots and g is not None and stage in g.snapshots]
                    row = {"task": task, "width": width, "method": method, "stage": stage,
                           "n_expected": len(seeds), "n_run_ok": sum(r.status=="ok" for r in methods),
                           "n_run_failed": sum(r.status=="failed" for r in methods),
                           "n_run_missing": sum(r.status=="missing" for r in methods),
                           "n_failed_latest_attempt": sum(bool(r.attempts) and r.attempts[-1]["status"]!="ok" for r in methods),
                           "n_fit6": sum("fit6" in r.snapshots for r in methods),
                           "n_not_fit6_including_missing_failed": sum("fit6" not in r.snapshots for r in methods),
                           "n_fit8": sum("fit8" in r.snapshots for r in methods),
                           "n_stage_available": sum(stage in r.snapshots for r in methods),
                           "n_pairs": len(pairs), "paired_seeds": ",".join(str(p[0]) for p in pairs),
                           "category": "reference" if method=="gaussian" else "inconclusive",
                           "provisional": provisional}
                    if not pairs:
                        row["classification_reason"] = "no paired snapshots"
                        rows.append(row)
                        continue
                    target = pairs[0][1].target_rms
                    if any(not np.isclose(a.target_rms,target,rtol=1e-12,atol=1e-12)
                           or not np.isclose(g.target_rms,target,rtol=1e-12,atol=1e-12)
                           for _,a,g in pairs):
                        raise ValueError("paired target normalizations differ")
                    x = np.asarray([a.risk for _,a,_ in pairs])
                    g = np.asarray([b.risk for _,_,b in pairs])
                    difference = x-g
                    both_fit = sum(a.train_mse<=threshold*(1+1e-9) and b.train_mse<=threshold*(1+1e-9)
                                   for _,a,b in pairs)
                    valid_grids = all(a.grid_pass and b.grid_pass for _,a,b in pairs)
                    issues = []
                    loss_warning_seeds = set()
                    refinement_warning_seeds = set()
                    for seed,_,_ in pairs:
                        for compared_method in (method,"gaussian"):
                            compared = lookup[(task,width,seed,compared_method)]
                            if float(compared.record.get("max_loss_rise",0)) > 1e-7:
                                loss_warning_seeds.add(seed)
                            errors = numerical_issues.get((task,width,seed,compared_method,stage),[])
                            if errors:
                                refinement_warning_seeds.add(seed)
                                issues.extend(errors)
                    numerical_valid = valid_grids and not loss_warning_seeds and not refinement_warning_seeds
                    all_twelve_fit = (not provisional and seeds==list(range(12))
                                      and len(pairs)==12 and both_fit==12)
                    row.update(target_rms=target, n_both_fit=both_fit,
                               n_not_both_fit_including_missing=len(seeds)-both_fit,
                               all_12_both_fit=all_twelve_fit, all_paired_grids_pass=valid_grids,
                               paired_loss_rise_warning_count=len(loss_warning_seeds),
                               paired_refinement_warning_count=len(refinement_warning_seeds),
                               refinement_issues="; ".join(sorted(set(issues))),
                               numerically_valid=numerical_valid)
                    for prefix, values in (("method_risk",x),("gaussian_risk",g),("risk_difference",difference)):
                        row.update({prefix+"_"+k:v for k,v in _stats(values).items()})
                    row["normalized_risk_difference_mean"] = float(np.mean(difference))/target
                    row["normalized_method_risk_mean"] = float(np.mean(x))/target
                    row["normalized_gaussian_risk_mean"] = float(np.mean(g))/target
                    ix = bootstrap_indices(len(pairs))
                    xb, gb = np.mean(x[ix],axis=1), np.mean(g[ix],axis=1)
                    db = xb-gb
                    margin = .02*target+.05*gb  # recomputed on EVERY bootstrap sample
                    row["risk_difference_ci_low"],row["risk_difference_ci_high"] = _ci(db)
                    row["method_risk_ci_low"],row["method_risk_ci_high"] = _ci(xb)
                    row["gaussian_risk_ci_low"],row["gaussian_risk_ci_high"] = _ci(gb)
                    row["diff_plus_margin_ci_low"],row["diff_plus_margin_ci_high"] = _ci(db+margin)
                    row["diff_minus_margin_ci_low"],row["diff_minus_margin_ci_high"] = _ci(db-margin)
                    row["equivalence_margin_at_means"] = .02*target+.05*float(np.mean(g))
                    inside = row["diff_plus_margin_ci_low"]>0 and row["diff_minus_margin_ci_high"]<0
                    row["interval_inside_equivalence_band"] = inside
                    row["noninferiority_margin"] = .10*target
                    row["noninferiority_interval_pass"] = row["risk_difference_ci_high"]<.10*target
                    row["noninferiority_with_fit_gate"] = (row["noninferiority_interval_pass"]
                                                           and all_twelve_fit and numerical_valid)
                    if method != "gaussian" and len(pairs)>=2 and numerical_valid:
                        if inside and all_twelve_fit:
                            row["category"] = "close"
                        elif row["diff_minus_margin_ci_low"]>0:
                            row["category"] = "worse"
                        elif row["diff_plus_margin_ci_high"]<0:
                            row["category"] = "better"
                    row["classification_reason"] = (
                        "descriptive paired-seed interval; all fit" if all_twelve_fit
                        else "available-pair interval only; complete 12-seed fit gate fails")
                    if not valid_grids:
                        row["classification_reason"] += "; unresolved circle-grid check"
                    if loss_warning_seeds:
                        row["classification_reason"] += "; step-loss rise exceeds 1e-7"
                    if refinement_warning_seeds:
                        row["classification_reason"] += "; failed or unmatched time-refinement check"
                    distances, controls = [], []
                    for seed,a,b in pairs:
                        control = lookup.get((task,width,seed,"gaussian_control"))
                        if control is not None and stage in control.snapshots:
                            # Use the common base grid for the ratio numerator/denominator.
                            cp = control.snapshots[stage].prediction
                            if a.prediction.shape != cp.shape or b.prediction.shape != cp.shape:
                                raise ValueError("triple paired grids differ")
                            distances.append(_rms(a.prediction-b.prediction))
                            controls.append(_rms(cp-b.prediction))
                    row["n_function_distance_triples"] = len(distances)
                    if distances:
                        distances,controls=np.asarray(distances),np.asarray(controls)
                        for prefix,values in (("function_distance",distances),("control_function_distance",controls)):
                            row.update({prefix+"_"+k:v for k,v in _stats(values).items()})
                        jx=bootstrap_indices(len(distances))
                        bd,bc=np.mean(distances[jx],axis=1),np.mean(controls[jx],axis=1)
                        row["function_distance_ci_low"],row["function_distance_ci_high"]=_ci(bd)
                        row["control_function_distance_ci_low"],row["control_function_distance_ci_high"]=_ci(bc)
                        row["function_distance_ratio_aggregate"]=(float(np.mean(distances)/np.mean(controls))
                                                                  if np.mean(controls)>0 else None)
                        row["function_ratio_finite_bootstrap_fraction"]=float(np.mean(bc>0))
                        if np.all(bc>0):
                            row["function_ratio_ci_low"],row["function_ratio_ci_high"]=_ci(bd/bc)
                    rows.append(row)
    return rows


def aggregate_rankings(runs: list[Run], cells: list[dict], manifest: dict) -> list[dict]:
    lookup={r.identity:r for r in runs}
    seeds=sorted(manifest["seeds"])
    result=[]
    for stage in STAGES:
        stage_rows=[]
        for method in manifest["methods"]:
            if method=="gaussian":
                continue
            chosen=[c for c in cells if c["method"]==method and c["stage"]==stage]
            row={"stage":stage,"method":method,"baseline_control":method=="gaussian_control",
                 "cells_expected":len(manifest["tasks"])*len(manifest["widths"]),
                 "cells_with_all_pairs":sum(c["n_pairs"]==len(seeds) for c in chosen),
                 "cells_all_12_both_fit":sum(c.get("all_12_both_fit",False) for c in chosen),
                 "numerically_valid_cells":sum(c.get("numerically_valid",False) for c in chosen)}
            for category in ("close","better","worse","inconclusive"):
                row[category+"_cells"]=sum(c["category"]==category for c in chosen)
            matrix=[]
            complete=True
            for seed in seeds:
                values=[]
                for task in manifest["tasks"]:
                    for width in manifest["widths"]:
                        a,b=lookup[(task,width,seed,method)],lookup.get((task,width,seed,"gaussian"))
                        if stage not in a.snapshots or b is None or stage not in b.snapshots:
                            complete=False
                            continue
                        aa,bb=a.snapshots[stage],b.snapshots[stage]
                        values.append((aa.risk-bb.risk)/aa.target_rms)
                matrix.append(values)
            row["complete_balanced_risk_comparison"]=complete
            available=[c["normalized_risk_difference_mean"] for c in chosen
                       if "normalized_risk_difference_mean" in c]
            row["available_cell_mean_normalized_difference"]=(float(np.mean(available)) if available else None)
            row["available_cell_denominator"]=len(available)
            if complete and seeds:
                seed_means=np.mean(np.asarray(matrix),axis=1)
                row["balanced_mean_normalized_risk_difference"]=float(np.mean(seed_means))
                ix=bootstrap_indices(len(seeds))
                row["seed_block_ci_low"],row["seed_block_ci_high"]=_ci(np.mean(seed_means[ix],axis=1))
            stage_rows.append(row)
        eligible=sorted((r for r in stage_rows if r["complete_balanced_risk_comparison"]
                         and r["numerically_valid_cells"]==r["cells_expected"]
                         and not r["baseline_control"]),
                        key=lambda r:r["balanced_mean_normalized_risk_difference"])
        for rank,row in enumerate(eligible,1):
            row["balanced_risk_rank"]=rank
        result.extend(stage_rows)
    return result


def refinement_rows(base: list[Run], refinements: list[Run]) -> list[dict]:
    lookup={r.identity:r for r in base}
    result=[]
    for fine in refinements:
        coarse=lookup.get(fine.identity)
        if coarse is None:
            raise ValueError(f"refinement has no main counterpart: {fine.key}")
        if fine.dt>=coarse.dt:
            raise ValueError("refinement dt must be smaller than base dt")
        for stage in STAGES+("final",):
            row={"task":fine.task,"width":fine.width,"seed":fine.seed,"method":fine.method,
                 "stage":stage,"coarse_dt":coarse.dt,"fine_dt":fine.dt,
                 "fine_status":fine.status,"paired_snapshot_available":False,
                 "coarse_stage_available":stage in coarse.snapshots,
                 "fine_stage_available":stage in fine.snapshots,
                 "numerically_comparable":False,
                 "fitting_status_mismatch":("fit6" in coarse.snapshots)!=("fit6" in fine.snapshots)}
            if stage in coarse.snapshots and stage in fine.snapshots:
                a,b=coarse.snapshots[stage],fine.snapshots[stage]
                d,n=distance(a,b)
                if stage in ("fit6","fit8"):
                    alignment="matched_threshold_"+stage
                elif abs(a.time-b.time)<=1e-7:
                    alignment="same_time"
                elif ("fit6" in coarse.snapshots and "fit6" in fine.snapshots
                      and abs(a.time-coarse.snapshots["fit6"].time)<=1e-7
                      and abs(b.time-fine.snapshots["fit6"].time)<=1e-7):
                    alignment="matched_threshold_fit6"
                else:
                    alignment="different_endpoints"
                comparable=alignment!="different_endpoints"
                row.update(paired_snapshot_available=True,query_grid_points=n,
                           normalized_function_difference=d/a.target_rms,
                           normalized_risk_difference=(b.risk-a.risk)/a.target_rms,
                           function_difference_pass=(d<=.002*a.target_rms if comparable else None),
                           coarse_time=a.time,fine_time=b.time,endpoint_alignment=alignment,
                           numerically_comparable=comparable,
                           coarse_train_mse=a.train_mse,fine_train_mse=b.train_mse)
                if stage=="final":
                    row["fitting_status_mismatch"]=(a.train_mse<=1e-6)!=(b.train_mse<=1e-6)
            else:
                row["endpoint_alignment"]="missing_snapshot"
            result.append(row)
    return result


def refinement_issues(rows: list[dict]) -> dict[tuple, list[str]]:
    """Translate refinement failures into cell/stage numerical gates."""
    result: dict[tuple,list[str]] = {}
    for row in rows:
        issue=None
        if row["fine_status"]!="ok":
            issue="refinement run failed"
        elif row.get("function_difference_pass") is False:
            issue="refinement circle-function RMS exceeds 0.002*target_RMS"
        elif row["paired_snapshot_available"] and not row["numerically_comparable"]:
            issue="refinement endpoints differ without matched fitting thresholds"
        elif row["coarse_stage_available"] != row["fine_stage_available"]:
            issue="refinement fitting/snapshot availability differs"
        if issue is not None:
            key=tuple(row[k] for k in ("task","width","seed","method","stage"))
            result.setdefault(key,[]).append(issue)
    return result


def function_summary(runs: list[Run], risk_cells: list[dict], manifest: dict) -> list[dict]:
    """Primary canonical-Gaussian function agreement; teacher risk is unused."""
    lookup={r.identity:r for r in runs}
    result=[]
    for cell in risk_cells:
        task,width,method,stage=(cell[k] for k in ("task","width","method","stage"))
        observations=[]
        for seed in sorted(manifest["seeds"]):
            candidate=lookup[(task,width,seed,method)]
            reference=lookup.get((task,width,seed,"gaussian"))
            if stage not in candidate.snapshots or reference is None or stage not in reference.snapshots:
                continue
            aa,bb=paired_predictions(candidate.snapshots[stage],reference.snapshots[stage])
            d,gaussian_rms=_rms(aa-bb),_rms(bb)
            d_grid_delta=abs(d-_rms((aa-bb)[::2]))
            g_grid_delta=abs(gaussian_rms-_rms(bb[::2]))
            relative=d/gaussian_rms if gaussian_rms>0 else None
            if relative is not None and not np.isfinite(relative):
                relative=None
            item={"seed":seed,"function_rms_distance":d,
                  "relative_function_rms":relative,"canonical_gaussian_rms":gaussian_rms,
                  "grid_sup_abs_error":float(np.max(np.abs(aa-bb))),
                  "query_grid_points":len(aa),
                  "function_rms_grid_coarsening_delta":d_grid_delta,
                  "canonical_rms_grid_coarsening_delta":g_grid_delta,
                  "function_rms_grid_normalized_delta":d_grid_delta/gaussian_rms if gaussian_rms>0 else None,
                  "canonical_rms_grid_normalized_delta":g_grid_delta/gaussian_rms if gaussian_rms>0 else None,
                  "function_grid_pass":(gaussian_rms>0 and d_grid_delta<=1e-4*gaussian_rms
                                         and g_grid_delta<=1e-4*gaussian_rms)}
            control=lookup.get((task,width,seed,"gaussian_control"))
            if control is not None and stage in control.snapshots:
                # Context always uses one common base grid; it is never a
                # normalization or success criterion for function agreement.
                cp=control.snapshots[stage].prediction
                gp=reference.snapshots[stage].prediction
                item["independent_gaussian_control_rms_distance"]=_rms(cp-gp)
            observations.append(item)
        keep=("task","width","method","stage","n_expected","n_pairs","n_both_fit",
              "n_run_failed","n_run_missing","n_failed_latest_attempt","n_fit6",
              "n_not_fit6_including_missing_failed","n_fit8","all_12_both_fit",
              "numerically_valid","paired_loss_rise_warning_count",
              "paired_refinement_warning_count","refinement_issues","provisional")
        row={key:cell.get(key) for key in keep}
        row.update(primary_metric="D=RMS_circle(f_method-f_Gaussian)",
                   relative_metric="D/RMS_circle(f_Gaussian)",relative_agreement_threshold=.05,
                   independent_middle_draws=True,control_is_context_only=True,
                   screen_evaluable=False,passes_5pct_screen=False,agreement_status="inconclusive",
                   per_seed_json=json.dumps(observations,separators=(",",":")))
        for metric in ("function_rms_distance","relative_function_rms","grid_sup_abs_error",
                       "canonical_gaussian_rms","independent_gaussian_control_rms_distance"):
            values=np.asarray([o[metric] for o in observations if o.get(metric) is not None],dtype=float)
            row[metric+"_count"]=len(values)
            if not len(values):
                continue
            row.update({metric+"_"+key:value for key,value in _stats(values).items()})
            row[metric+"_p90"]=float(np.quantile(values,.9))
            row[metric+"_max"]=float(np.max(values))
            row[metric+"_min"]=float(np.min(values))
            ix=bootstrap_indices(len(values))
            row[metric+"_ci_low"],row[metric+"_ci_high"]=_ci(np.mean(values[ix],axis=1))
        row["canonical_zero_norm_count"]=sum(o["canonical_gaussian_rms"]==0 for o in observations)
        row["function_rms_grid_coarsening_delta_max"]=max(
            (o["function_rms_grid_coarsening_delta"] for o in observations),default=None)
        for metric in ("function_rms_grid_normalized_delta","canonical_rms_grid_normalized_delta"):
            row[metric+"_max"]=max((o[metric] for o in observations if o[metric] is not None),default=None)
        row["paired_function_grid_pass"]=bool(observations) and all(o["function_grid_pass"] for o in observations)
        # Teacher-risk quadrature and risk classification are not function-
        # agreement criteria. Use the paired function's own nested-grid test.
        nonquadrature_valid=(bool(observations) and not cell.get("paired_loss_rise_warning_count")
                             and not cell.get("paired_refinement_warning_count"))
        row["numerically_valid"]=nonquadrature_valid and row["paired_function_grid_pass"]
        row["query_grid_points_min"]=min((o["query_grid_points"] for o in observations),default=None)
        row["query_grid_points_max"]=max((o["query_grid_points"] for o in observations),default=None)
        all_relative=(len(observations)==12 and row["relative_function_rms_count"]==12)
        evaluable=bool(cell.get("all_12_both_fit") and row["numerically_valid"] and all_relative)
        row["screen_evaluable"]=evaluable
        if method=="gaussian":
            row["agreement_status"]="reference"
        elif method=="gaussian_control":
            row["agreement_status"]="context_only"
        elif evaluable:
            row["passes_5pct_screen"]=row["relative_function_rms_ci_high"]<=.05
            if row["passes_5pct_screen"]:
                row["agreement_status"]="within_5pct"
            elif row["relative_function_rms_ci_low"]>.05:
                row["agreement_status"]="exceeds_5pct"
        if row["relative_function_rms_count"]:
            row["worst_seed_relative_D"]=row["relative_function_rms_max"]
            row["all_observed_seeds_relative_D_le_5pct"]=row["relative_function_rms_max"]<=.05
        row["screen_reason"]=("complete paired fit and numerical screen" if evaluable
                              else "requires all12 bothfit, defined canonical-relative errors and numerical validity")
        result.append(row)
    return result


def function_rankings(function_cells: list[dict], manifest: dict) -> list[dict]:
    """Balanced function-distance ordering with whole-seed bootstrap blocks."""
    results=[]
    expected=len(manifest["tasks"])*len(manifest["widths"])
    seeds=sorted(manifest["seeds"])
    for stage in STAGES:
        stage_rows=[]
        for method in manifest["methods"]:
            if method=="gaussian":
                continue
            cells=[c for c in function_cells if c["stage"]==stage and c["method"]==method]
            row={"stage":stage,"method":method,"context_control":method=="gaussian_control",
                 "cells_expected":expected,
                 "cells_all12_bothfit":sum(bool(c.get("all_12_both_fit")) for c in cells),
                 "cells_numerically_valid":sum(bool(c.get("numerically_valid")) for c in cells),
                 "cells_pass_5pct_screen":sum(c["passes_5pct_screen"] for c in cells),
                 "cells_exceed_5pct":sum(c["agreement_status"]=="exceeds_5pct" for c in cells),
                 "cells_inconclusive":sum(c["agreement_status"]=="inconclusive" for c in cells)}
            observations=[{o["seed"]:o for o in json.loads(c["per_seed_json"])} for c in cells]
            complete=(len(cells)==expected and all(
                seed in group and group[seed]["relative_function_rms"] is not None
                for group in observations for seed in seeds))
            row["complete_balanced_function_comparison"]=complete
            finite_means=[c["relative_function_rms_mean"] for c in cells if "relative_function_rms_mean" in c]
            row["available_cell_mean_relative_D"]=float(np.mean(finite_means)) if finite_means else None
            row["available_cell_denominator"]=len(finite_means)
            row["worst_seed_relative_D_across_suite"]=max(
                (c["relative_function_rms_max"] for c in cells if "relative_function_rms_max" in c),default=None)
            if complete and seeds:
                relative=np.asarray([[group[seed]["relative_function_rms"] for group in observations]
                                     for seed in seeds])
                absolute=np.asarray([[group[seed]["function_rms_distance"] for group in observations]
                                     for seed in seeds])
                ix=bootstrap_indices(len(seeds))
                for name,matrix in (("relative_D",relative),("absolute_D",absolute)):
                    seed_mean=np.mean(matrix,axis=1)
                    row["balanced_mean_"+name]=float(np.mean(seed_mean))
                    low,high=_ci(np.mean(seed_mean[ix],axis=1))
                    row["seed_block_"+name+"_ci_low"],row["seed_block_"+name+"_ci_high"]=low,high
            row["every_planned_cell_passes_5pct_screen"]=(row["cells_pass_5pct_screen"]==expected
                                                         and not row["context_control"])
            stage_rows.append(row)
        eligible=sorted((r for r in stage_rows if r["complete_balanced_function_comparison"]
                         and r["cells_numerically_valid"]==expected and not r["context_control"]),
                        key=lambda r:r["balanced_mean_relative_D"])
        for rank,row in enumerate(eligible,1):
            row["balanced_function_distance_rank"]=rank
        results.extend(stage_rows)
    return results


def write_csv(path: Path, rows: list[dict]) -> None:
    columns=list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w",newline="") as stream:
        writer=csv.DictWriter(stream,fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def _number(value) -> str:
    if value is None:
        return "—"
    return f"{value:.4g}"


def markdown_risk_appendix(summary: dict) -> str:
    lines=["# Secondary teacher-risk appendix", "",
           "These teacher-risk equivalence categories and rankings do not establish function agreement and are not recommendation criteria. They are retained for traceability only.", "",
           "PROVISIONAL: incomplete-artifact mode; no close classification is permitted."
           if summary["provisional"] else "All loaded campaign directories passed completion and artifact-hash checks.",
           "", "This is empirical evidence for the frozen finite-width circle suite, not a Gaussian-universality or scalar-compression theorem. All middle matrices and both outer blocks were trained densely.",
           "", "Intervals use 20,000 paired-seed bootstrap resamples with seed 0. They are descriptive per-comparison 95% intervals, not simultaneous guarantees. The Gaussian-dependent equivalence margin is recomputed in each resample. `close` requires all twelve planned seeds to fit in both methods, as well as the two-sided interval screen and passing circle-grid checks. Partial-fit risk intervals describe available pairs only.",
           "", "Refined circle risk is used when an 8192-grid snapshot is saved. Function-distance ratios use a shared base grid and are ratios of aggregate distances, not means of per-seed ratios. Positive risk difference means the candidate has higher error. A fixed-time snapshot can precede its run's matched-fit snapshot; drift time differences are retained in per_run.csv.",
           "", "## Coverage and numerical checks", "", "```json",
           json.dumps(summary["coverage"],indent=2), "```", "",
           "The complete per-run denominators, failed/missing attempts, feature motions, first-fit times, threshold drift, grid discrepancies and artifact hashes are retained in the CSV/JSON files."]
    manifest=summary["plan"]
    methods=[m for m in manifest["methods"] if m!="gaussian"]
    lookup={(c["task"],c["width"],c["method"],c["stage"]):c for c in summary["cells"]}
    for stage in STAGES:
        lines.extend(["",f"## {stage}"+(" sensitivity" if stage=="fit8" else ""), "",
                      "Each entry: normalized paired risk difference [95% interval]; category; paired/both-fit count.","",
                      "| Task / width | "+" | ".join(methods)+" |",
                      "|---|"+"---|"*len(methods)])
        for task in manifest["tasks"]:
            for width in manifest["widths"]:
                entries=[]
                for method in methods:
                    c=lookup[(task,width,method,stage)]
                    if c["n_pairs"]:
                        scale=c["target_rms"]
                        entries.append(f'{_number(c["normalized_risk_difference_mean"])} '
                                       f'[{_number(c["risk_difference_ci_low"]/scale)}, '
                                       f'{_number(c["risk_difference_ci_high"]/scale)}]; '
                                       f'{c["category"]}; {c["n_pairs"]}/{c["n_both_fit"]}')
                    else:
                        entries.append("unavailable; 0/0")
                lines.append(f"| {task} / {width} | "+" | ".join(entries)+" |")
    lines.extend(["", "## Balanced candidate ranking", "",
                  "Ranking uses the mean normalized risk difference over every planned task/width cell. A rank is assigned only when every seed/cell has a paired snapshot; fitting completeness is reported separately. Aggregate intervals resample entire seed blocks jointly across tasks and widths. The independent Gaussian control is shown but not ranked.", "",
                  "| Stage | Method | Rank | Mean normalized difference [95% interval] | All-pair cells | All-fit cells | Close / better / worse / inconclusive |",
                  "|---|---|---|---|---|---|---|"])
    for r in summary["rankings"]:
        mean=r.get("balanced_mean_normalized_risk_difference")
        estimate=(f'{_number(mean)} [{_number(r.get("seed_block_ci_low"))}, '
                  f'{_number(r.get("seed_block_ci_high"))}]') if mean is not None else "unavailable"
        counts=" / ".join(str(r[c+"_cells"]) for c in ("close","better","worse","inconclusive"))
        lines.append(f'| {r["stage"]} | {r["method"]} | {r.get("balanced_risk_rank","—")} | {estimate} | '
                     f'{r["cells_with_all_pairs"]}/{r["cells_expected"]} | '
                     f'{r["cells_all_12_both_fit"]}/{r["cells_expected"]} | {counts} |')
    lines.extend(["", "Risk similarity does not imply predictor similarity. Paired function distances and their independent-Gaussian control ratios, with uncertainty, are in paired_summary.csv and summary.json. No candidate or task is omitted from these tables.", ""])
    return "\n".join(lines)


def markdown_report(summary: dict) -> str:
    lines=["# Circle-function agreement with the canonical Gaussian network", "",
           "PROVISIONAL: incomplete-artifact mode; no agreement pass is permitted."
           if summary["provisional"] else "All analyzed input directories passed completion and saved-artifact hash checks.", "",
           "The primary question is whether each structured initialization reproduces the Gaussian network's predicted circle function under dense training. Teacher risk is secondary and is not used as a success criterion.", "",
           "The user corrected the primary metric while 1323 of 2016 principal trajectories had completed. The experiment candidates, tasks, seeds, initializations and training trajectories were unchanged; this analysis change occurred before the completed-data comparisons. The original risk analysis is retained only as an appendix.", "",
           "For each seed, D is the circle RMS of f_method − f_Gaussian. Relative error is D/RMS(f_Gaussian). The maximum absolute error is a maximum on the saved circle grid, not a certified continuous-circle supremum. The two networks share outer initialization and use independent middle draws: this is a comparison of the prescribed paired realizations, not an optimized coupling or a fit of a structured matrix to a given Gaussian matrix.", "",
           "The explicit agreement screen requires all twelve seeds to fit in both methods, passing numerical checks, and the 95% upper confidence limit of the mean seed-relative RMS error to be at most 5%. The worst seed is also reported. A Gaussian-control distance is context only: matching it does not constitute success. Intervals use 20,000 paired-seed resamples with seed 0 and are descriptive per comparison, not simultaneous suite-wide guarantees.", "",
           "The function quadrature check compares the finest shared saved grid with its alternating-point half grid. Both the D discrepancy and canonical Gaussian-RMS discrepancy must be at most 1e-4 times canonical Gaussian RMS. Step-loss rises above 1e-7 and failed/unmatched paired time refinements prevent an agreement conclusion. No teacher-risk comparison enters this function screen.", "",
           "## Coverage and numerical checks", "", "```json",json.dumps(summary["coverage"],indent=2),"```"]
    plan=summary["plan"]
    methods=[m for m in plan["methods"] if m!="gaussian"]
    lookup={(c["task"],c["width"],c["method"],c["stage"]):c for c in summary["function_cells"]}
    for stage in STAGES:
        lines.extend(["",f"## {stage}"+(" sensitivity" if stage=="fit8" else ""),"",
                      "Entries: mean relative function RMS error in percent [95% interval]; worst seed percent; agreement status; paired/both-fit count. The Gaussian control is contextual only.","",
                      "| Task / width | "+" | ".join(methods)+" |",
                      "|---|"+"---|"*len(methods)])
        for task in plan["tasks"]:
            for width in plan["widths"]:
                entries=[]
                for method in methods:
                    c=lookup[(task,width,method,stage)]
                    if c.get("relative_function_rms_count",0):
                        entries.append(f'{_number(100*c["relative_function_rms_mean"])} '
                                       f'[{_number(100*c["relative_function_rms_ci_low"])}, '
                                       f'{_number(100*c["relative_function_rms_ci_high"])}]; '
                                       f'max {_number(100*c["relative_function_rms_max"])}; '
                                       f'{c["agreement_status"]}; {c["n_pairs"]}/{c.get("n_both_fit",0)}')
                    else:
                        entries.append("unavailable or undefined relative error")
                lines.append(f"| {task} / {width} | "+" | ".join(entries)+" |")
    lines.extend(["", "## Balanced function-distance ordering", "",
                  "Ordering uses equal weight for every planned task/width cell, then averages over paired seeds. Ranks require complete paired function data and passing numerical checks; they do not imply agreement. A method passes across the suite only if every planned cell passes its 5% screen. Aggregate intervals resample each seed jointly across tasks and widths.", "",
                  "| Stage | Method | Rank | Mean relative RMS percent [95% interval] | Worst seed percent | Passing cells | All-fit cells |",
                  "|---|---|---|---|---|---|---|"])
    for r in summary["function_rankings"]:
        value=r.get("balanced_mean_relative_D")
        estimate=(f'{_number(100*value)} [{_number(100*r["seed_block_relative_D_ci_low"])}, '
                  f'{_number(100*r["seed_block_relative_D_ci_high"])}]') if value is not None else "unavailable"
        worst=r.get("worst_seed_relative_D_across_suite")
        lines.append(f'| {r["stage"]} | {r["method"]} | {r.get("balanced_function_distance_rank","—")} | '
                     f'{estimate} | {_number(100*worst) if worst is not None else "—"} | '
                     f'{r["cells_pass_5pct_screen"]}/{r["cells_expected"]} | '
                     f'{r["cells_all12_bothfit"]}/{r["cells_expected"]} |')
    lines.extend(["", "Absolute RMS errors, canonical Gaussian norms, grid maxima, individual-seed median/p90/max, contextual Gaussian-control distances, confidence intervals, and numerical gates are in function_summary.csv and summary.json. Complete run statuses and first-fit timing remain in per_run.csv. These are empirical finite-width paired-realization results; they do not establish a universal operator approximation or a scalar-closure theorem.", "",
                  markdown_risk_appendix(summary)])
    return "\n".join(lines)


def analyze(base: Path, output: Path, continuations=(), refinements=(),
            allow_incomplete: bool = False) -> dict:
    provenance=Provenance()
    manifest,observed,base_info=load_directory(base,provenance,allow_incomplete)
    infos=[base_info]
    for folder in continuations:
        _,later,info=load_directory(folder,provenance,allow_incomplete)
        merge_continuation(observed,later)
        infos.append(info)
    runs=complete_plan(manifest,observed)
    refined=[]
    for folder in refinements:
        _,loaded,info=load_directory(folder,provenance,allow_incomplete)
        refined.extend(loaded.values())
        infos.append(info)
    refinement=refinement_rows(runs,refined)
    issues=refinement_issues(refinement)
    per_run=per_run_rows(runs)
    cells=paired_summary(runs,manifest,allow_incomplete,issues)
    rankings=aggregate_rankings(runs,cells,manifest)
    functions=function_summary(runs,cells,manifest)
    function_order=function_rankings(functions,manifest)
    grids=[s for r in runs for s in r.snapshots.values()]
    max_rise=max((float(r.record.get("max_loss_rise",0)) for r in runs),default=0.)
    available_ref=[r for r in refinement if r["paired_snapshot_available"]]
    coverage={"planned_runs":len(runs),"valid_runs":sum(r.status=="ok" for r in runs),
              "failed_runs":sum(r.status=="failed" for r in runs),
              "missing_runs":sum(r.status=="missing" for r in runs),
              "failed_latest_attempts":sum(bool(r.attempts) and r.attempts[-1]["status"]!="ok" for r in runs),
              "not_fit6_including_missing_failed":sum("fit6" not in r.snapshots for r in runs),
              "not_fit8_including_missing_failed":sum("fit8" not in r.snapshots for r in runs),
              "missing_time300":sum("time300" not in r.snapshots for r in runs),
              "max_step_loss_rise":max_rise,
              "runs_loss_rise_above_1e_7":sum(float(r.record.get("max_loss_rise",0))>1e-7 for r in runs),
              "snapshots_with_unresolved_grid_check":sum(not s.grid_pass for s in grids),
              "max_final_grid_delta_normalized":max((s.grid_delta/s.target_rms for s in grids),default=None),
              "refinement_snapshot_pairs":len(available_ref),
              "refinement_pairs_failing_function_check":sum(r.get("function_difference_pass") is False for r in available_ref),
              "refinement_pairs_with_unmatched_endpoints":sum(not r["numerically_comparable"] for r in available_ref),
              "refinement_fitting_status_mismatches":sum(r["fitting_status_mismatch"] for r in refinement),
              "function_cells_failing_own_grid_check":sum(c["n_pairs"]>0 and not c["paired_function_grid_pass"] for c in functions),
              "max_refinement_normalized_function_difference":max((r["normalized_function_difference"] for r in available_ref),default=None)}
    summary={"provisional":allow_incomplete,"bootstrap_resamples":BOOTSTRAP_RESAMPLES,
             "bootstrap_seed":BOOTSTRAP_SEED,"interval_scope":"descriptive per comparison; not simultaneous",
             "aggregate_resampling":"whole seed blocks jointly over all tasks and widths",
             "equivalence_margin":"0.02*target_RMS + 0.05*bootstrap_mean_Gaussian_RMS",
             "primary_metric":"circle predicted-function agreement with the paired canonical Gaussian network",
             "primary_relative_error":"RMS(f_method-f_Gaussian)/RMS(f_Gaussian), computed per seed",
             "function_agreement_screen":"all12 bothfit and numerical gates; 95% upper mean relative error <= 0.05",
             "metric_revision":{"user_correction_after_completed_principal_runs":1323,
                                "planned_principal_runs":2016,
                                "trajectory_candidate_task_seed_changes":False,
                                "teacher_risk_is_success_criterion":False},
             "coupling":"shared outer initialization, independent middle draws; no optimized Gaussian-to-structured fit",
             "plan":{k:manifest[k] for k in ("tasks","widths","seeds","methods","dt")},
             "directories":infos,"coverage":coverage,"cells":cells,"rankings":rankings,
             "function_cells":functions,"function_rankings":function_order,
             "refinement_comparisons":refinement,
             "empirical_scope":"Frozen finite-width dense-training circle suite only; no universality or scalar-closure conclusion."}
    provenance.recheck()
    output=output.resolve()
    input_dirs={Path(i["directory"]).resolve() for i in infos}
    if output in input_dirs:
        raise ValueError("analysis output must be separate from input artifact directories")
    output.mkdir(parents=True,exist_ok=False)
    write_csv(output/"per_run.csv",per_run)
    write_csv(output/"paired_summary.csv",cells)
    write_csv(output/"rankings.csv",rankings)
    write_csv(output/"function_summary.csv",functions)
    write_csv(output/"function_rankings.csv",function_order)
    write_csv(output/"refinement_comparisons.csv",refinement)
    (output/"summary.json").write_text(json.dumps(summary,indent=2,allow_nan=False)+"\n")
    (output/"input_hashes.json").write_text(json.dumps({"sha256":provenance.hashes,
        "verified_against_artifact_index":sorted(provenance.checked_against_index),
        "rechecked_unchanged_before_output":True},indent=2)+"\n")
    (output/"report.md").write_text(markdown_report(summary))
    (output/"analysis_provenance.json").write_text(json.dumps({
        "script":str(Path(__file__).resolve()),"script_sha256":digest(Path(__file__)),
        "numpy":np.__version__,"python":sys.version,"command":sys.argv},indent=2)+"\n")
    return summary


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--base",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--continuation",type=Path,nargs="*",default=[])
    p.add_argument("--refinement",type=Path,nargs="*",default=[])
    p.add_argument("--allow-incomplete",action="store_true")
    args=p.parse_args()
    result=analyze(args.base,args.output,args.continuation,args.refinement,args.allow_incomplete)
    print(json.dumps({"output":str(args.output.resolve()),"provisional":result["provisional"],
                      "coverage":result["coverage"]},indent=2))


if __name__=="__main__":
    main()
