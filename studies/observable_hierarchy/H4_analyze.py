"""Read-only analysis of a declared time-40 observable validation.

No initializer, solver step, fitted reference or target trajectory is used.
All differences are between numerical runs at fixed saved times and a finite
input panel. They are not convergence rates or population-error bounds.
"""
import argparse
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import re
import time

import numpy as np


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def basename(value):
    if not isinstance(value, str) or Path(value).name != value or value in ("", ".", ".."):
        raise ValueError("artifact must be a basename")
    return value


def read_observation(folder, item, dimensions, circle_count):
    path = folder / basename(item["npz"])
    with np.load(path, allow_pickle=False) as archive:
        data = {k: np.asarray(archive[k], dtype=float) for k in archive.files}
    p1, p2, a = (dimensions[k] for k in ("first_nodes", "second_nodes", "input_nodes"))
    shapes = dict(circle=(circle_count, 2), prediction=(circle_count,),
                  training_prediction=(a,), labels=(a,), loss=(),
                  first_pairs=(p1, a, 2), second_pairs=(p2, a, 2),
                  first_weights=(p1,), second_weights=(p2,), input_weights=(a,),
                  inputs=(a, 2), rms1=(), rms2=())
    if set(data) != set(shapes):
        raise ValueError("unexpected observation fields: " + str(set(data) ^ set(shapes)))
    for key, shape in shapes.items():
        if data[key].shape != shape or not np.isfinite(data[key]).all():
            raise ValueError("invalid observation shape/value: " + key)
    for key in ("first_weights", "second_weights", "input_weights"):
        if np.any(data[key] < 0) or abs(float(data[key].sum()) - 1) > 1e-10:
            raise ValueError("invalid observation probability approximation")
    recomputed = dict(loss=float(data["input_weights"] @ (data["training_prediction"] - data["labels"]) ** 2))
    moments = {}
    for layer, name in ((1, "first"), (2, "second")):
        pair = data[name + "_pairs"]
        if np.max(np.abs(pair)) > 1 + 1e-12:
            raise ValueError("tanh activation outside its range")
        weights = data[name + "_weights"][:, None] * data["input_weights"][None, :]
        motion = float(np.sum(weights * (pair[:, :, 1] - pair[:, :, 0]) ** 2))
        recomputed["rms" + str(layer)] = float(np.sqrt(max(0, motion)))
        mass = float(weights.sum())
        moments[name] = dict(mass=mass,
                            initial_mean=float(np.sum(weights * pair[:, :, 0]) / mass),
                            current_mean=float(np.sum(weights * pair[:, :, 1]) / mass),
                            initial_current_product=float(np.sum(weights * pair[:, :, 0] * pair[:, :, 1]) / mass),
                            squared_displacement=motion)
    discrepancies = {}
    for key, value in recomputed.items():
        discrepancies[key] = max(abs(value - float(data[key])), abs(value - item[key]))
        if discrepancies[key] > 2e-11 * max(1, abs(value)):
            raise ValueError("saved-observation algebra mismatch: " + key)
    if Fraction(item["time"]) == 0 and any(recomputed[k] != 0 for k in ("rms1", "rms2")):
        raise ValueError("initial/current pair differs at time zero")
    exact = folder / basename(item["exact_json"])
    if not exact.is_file():
        raise ValueError("missing exact working observation archive")
    return data, dict(time=item["time"], recomputed=recomputed,
                      algebra_absolute_discrepancies=discrepancies, paired_moments=moments,
                      npz_sha256=digest(path), exact_json_sha256=digest(exact),
                      npz_bytes=path.stat().st_size, exact_json_bytes=exact.stat().st_size,
                      float_payload_bytes=sum(v.nbytes for v in data.values()))


def comparison(left, right, left_panels, right_panels):
    a, b = left["configuration"], right["configuration"]
    if a["law"] != b["law"]:
        return None
    changed = sorted(k for k in set(a) | set(b) if k != "id" and a.get(k) != b.get(k))
    if changed == ["order"]:
        kind = "closure_order"
    elif changed and set(changed) <= {"digits", "backend"}:
        kind = "arithmetic"
    elif len(changed) == 1 and changed[0] in {"initialization_nodes", "population_nodes", "nodes_per_arc", "steps"}:
        kind = "single_numerical_axis"
    else:
        return None
    observations = []
    for time_key in left_panels:
        x, y = left_panels[time_key], right_panels[time_key]
        if x["circle"].shape != y["circle"].shape or np.max(np.abs(x["circle"] - y["circle"])) > 1e-12:
            raise ValueError("comparison panels do not correspond")
        difference = y["prediction"] - x["prediction"]
        observations.append(dict(time=time_key,
                                 panel_max_abs_prediction_difference=float(np.max(np.abs(difference))),
                                 panel_rms_prediction_difference=float(np.sqrt(np.mean(difference ** 2))),
                                 right_minus_left_loss=float(y["loss"] - x["loss"]),
                                 right_minus_left_rms1=float(y["rms1"] - x["rms1"]),
                                 right_minus_left_rms2=float(y["rms2"] - x["rms2"])))
    return dict(left=a["id"], right=b["id"], kind=kind, changed=changed,
                observations=observations,
                maximum_over_saved_times_and_panel=max(r["panel_max_abs_prediction_difference"] for r in observations))


def analyze(plan_path, runs):
    plan_path, runs = Path(plan_path), Path(runs)
    plan = json.loads(plan_path.read_text())
    plan_hash = digest(plan_path)
    result = dict(format="observable-horizon-analysis-v1", plan_sha256=plan_hash,
                  postprocessor_sha256=digest(__file__), horizon=plan["horizon"],
                  scope="Fixed saved times and finite circle panel; numerical comparisons and algebra checks only, no target error or finite-run accuracy certificate.",
                  probability_note="Paired-law probability interpretation normalizes nonnegative product weights; operational RMS/loss use literal weights.",
                  runs=[], comparisons=[], problems=[])
    panels, records = {}, {}
    expected_times = list(map(Fraction, plan["common"]["observation_times"]))
    for config in plan["configurations"]:
        name = config["id"]
        if not re.fullmatch(r"[A-Za-z0-9_-]{1,80}", name):
            raise ValueError("unsafe configuration identifier")
        folder = runs / name
        path = folder / "record.json"
        if not path.is_file():
            result["problems"].append(dict(id=name, problem="missing_record"))
            continue
        record = json.loads(path.read_text())
        if record.get("configuration") != config or record.get("id") != name or record.get("plan_sha256") != plan_hash:
            raise ValueError("configuration/plan provenance mismatch: " + name)
        row = dict(id=name, configuration=config, status=record.get("status"), record_sha256=digest(path))
        for file, expected in record.get("outputs", {}).items():
            artifact = folder / basename(file)
            if not artifact.is_file() or digest(artifact) != expected:
                raise ValueError("artifact hash mismatch: " + str(artifact))
        if record.get("status") != "operational_pass":
            row["error"] = record.get("error")
            result["runs"].append(row)
            result["problems"].append(dict(id=name, problem="recorded_failure"))
            continue
        if not record.get("restart_exact"):
            raise ValueError("operational pass without exact restart")
        dimensions = record["dimensions"]
        if dimensions["action_matrix"] != [dimensions["second_features"], dimensions["first_features"]]:
            raise ValueError("action dimensions mismatch")
        if list(map(lambda x: Fraction(x["time"]), record["observations"])) != expected_times:
            raise ValueError("saved time list differs from plan")
        panel, checks = {}, []
        for item in record["observations"]:
            data, check = read_observation(folder, item, dimensions, plan["common"]["circle_directions"])
            panel[item["time"]] = data
            checks.append(check)
        p1, p2, d1, d2, a = (dimensions[k] for k in
                              ("first_nodes", "second_nodes", "first_features", "second_features", "input_nodes"))
        row.update(dimensions=dimensions, observations=checks,
                   state_scalars=p1*(d1+5)+p2*(d2+2)+2*d1*d2,
                   dynamic_scalars=2*p1+p2+d1*d2, data_scalars=4*a)
        for key in ("initialization_seconds", "evolution_seconds", "restart_seconds", "observation_seconds", "total_seconds",
                    "peak_rss_bytes", "initialization_metadata", "conditioning_diagnostics", "state_bytes_initial", "state_bytes_final",
                    "loss_initial", "loss_final", "rms1", "rms2", "restart_exact", "law_metadata", "workspace_initial", "workspace_final",
                    "data_bytes", "checkpoint_bytes", "final_checkpoint_bytes", "restart_contract", "restart_comparison",
                    "source_hashes", "producer_sha256"):
            if key in record:
                row[key] = record[key]
        result["runs"].append(row)
        panels[name], records[name] = panel, record
    for left, right in itertools.combinations(records, 2):
        item = comparison(records[left], records[right], panels[left], panels[right])
        if item is not None:
            result["comparisons"].append(item)
    supervisor_path = runs / "supervisor.json"
    if supervisor_path.is_file():
        supervisor = json.loads(supervisor_path.read_text())
        if supervisor["plan_sha256"] != plan_hash:
            raise ValueError("supervisor plan hash mismatch")
        result["supervisor"] = dict(sha256=digest(supervisor_path), status=supervisor["status"],
                                    total_cpu_seconds=supervisor["total_cpu_seconds"],
                                    configurations=supervisor["configurations"])
    successful = [r for r in result["runs"] if r["status"] == "operational_pass"]
    result["aggregate"] = dict(declared=len(plan["configurations"]), successful=len(successful),
                               sum_worker_cpu_seconds=sum(r["total_seconds"]["cpu"] for r in successful),
                               maximum_peak_rss_bytes=max((r["peak_rss_bytes"] for r in successful), default=0))
    return result


def markdown(result):
    lines = ["# Time-40 observable computation: recorded validation", "", result["scope"], "",
             "Supported-law perturbations that collapse to the reference at working precision are explicitly recorded. Such runs do not resolve the positive perturbation. Exploratory rational-radius runs carry no population theorem.", "",
             "| Run | Order / features | Q / P / input nodes | Steps / digits | Loss at 40 | RMS1 / RMS2 at 40 | CPU s | Peak MiB |",
             "| --- | --- | --- | --- | ---: | --- | ---: | ---: |"]
    for row in result["runs"]:
        if row["status"] != "operational_pass":
            lines.append("| " + row["id"] + " | " + str(row["status"]) + " | | | | | | |")
            continue
        c, d = row["configuration"], row["dimensions"]
        fields = [row["id"], f"{c['order']} / {d['first_features']},{d['second_features']}",
                  f"{c['initialization_nodes']} / {c['population_nodes']} / {d['input_nodes']}",
                  f"{c['steps']} / {c['digits'] or 'float64'}", f"{row['loss_final']:.8g}",
                  f"{row['rms1']:.7g} / {row['rms2']:.7g}", f"{row['total_seconds']['cpu']:.3f}",
                  f"{row['peak_rss_bytes']/2**20:.3f}"]
        lines.append("| " + " | ".join(fields) + " |")
    lines.extend(["", "| Comparison | Changed parameter | Largest difference over saved times/panel |", "| --- | --- | ---: |"])
    for item in result["comparisons"]:
        lines.append(f"| {item['left']} → {item['right']} | {', '.join(item['changed'])} | {item['maximum_over_saved_times_and_panel']:.9g} |")
    lines.extend(["", "All declared comparable pairs are included. The finite panel and saved times do not establish a supremum error over the circle or time interval. Exact restarts and exact working observations remain in the run artifacts; full configuration, timing, memory, law and conditioning records are in the JSON summary.", ""])
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--runs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.output.exists():
        raise FileExistsError("analysis output must be fresh")
    started = time.process_time()
    result = analyze(args.plan, args.runs)
    result["analysis_cpu_seconds"] = time.process_time()-started
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "summary.json").write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    (args.output / "summary.md").write_text(markdown(result))
    print(json.dumps(dict(aggregate=result["aggregate"], problems=result["problems"], comparisons=len(result["comparisons"]))))
    return int(bool(result["problems"]))


if __name__ == "__main__":
    raise SystemExit(main())
