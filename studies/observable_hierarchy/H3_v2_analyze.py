"""Read-only postprocessing of a declared observable-solver validation plan.

Reads existing records, exact restarts and float64 observation archives. No
initialization, trajectory evolution or source fitting is invoked. Comparisons
are final-time differences on the saved circle panel, not error certificates.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import re
import sys
import time

import numpy as np


def digest(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as source:
        for block in iter(lambda: source.read(1024*1024), b""):
            value.update(block)
    return value.hexdigest()


def _observations(path, dimensions, circle_count):
    required = {"circle", "prediction", "first_pairs", "second_pairs", "first_weights",
                "second_weights", "input_weights", "inputs", "rms1", "rms2"}
    with np.load(path, allow_pickle=False) as archive:
        if set(archive.files) != required:
            raise ValueError("unexpected observation archive schema")
        data = {key: np.asarray(archive[key], dtype=float) for key in required}
    p1, p2, m = (dimensions[key] for key in ("first_nodes", "second_nodes", "input_nodes"))
    shapes = dict(circle=(circle_count, 2), prediction=(circle_count,),
                  first_pairs=(p1, m, 2), second_pairs=(p2, m, 2),
                  first_weights=(p1,), second_weights=(p2,),
                  input_weights=(m,), inputs=(m, 2), rms1=(), rms2=())
    for name, expected in shapes.items():
        if data[name].shape != expected or not np.all(np.isfinite(data[name])):
            raise ValueError("invalid finite observation shape: "+name)
    for key in ("first_weights", "second_weights", "input_weights"):
        if np.any(data[key] < 0) or abs(float(data[key].sum())-1) > 1e-10:
            raise ValueError("invalid saved observation probabilities")
    motion = {}
    for layer, key in ((1, "first"), (2, "second")):
        delta = data[key+"_pairs"][:, :, 1]-data[key+"_pairs"][:, :, 0]
        squared = float(data[key+"_weights"] @ (delta*delta) @ data["input_weights"])
        motion["rms"+str(layer)+"_from_saved_pairs"] = float(np.sqrt(max(squared, 0)))
    return data, motion


def _recount(path, old_bytes):
    # Import only for explicitly requested exact-state memory postprocessing.
    # load_restart validates/reconstructs saved values; no evolution is called.
    from pde import observable_solver
    from pde.observable_fixed import Fixed
    import sys as runtime_sys

    state, data = observable_solver.load_restart(path)
    corrected = observable_solver.state_bytes(state)
    arrays = [getattr(state, key) for key in ("b1", "g", "w", "p1", "b2", "c", "p2", "M", "D")]
    pointer_or_payload = sum(a.nbytes for a in arrays)
    scalar_objects = sum(runtime_sys.getsizeof(x) for a in arrays if a.dtype == object for x in a.flat)
    units = sum(runtime_sys.getsizeof(x.units) for a in arrays if a.dtype == object for x in a.flat if isinstance(x, Fixed))
    scales = sum(runtime_sys.getsizeof(x.scale) for a in arrays if a.dtype == object for x in a.flat if isinstance(x, Fixed))
    if pointer_or_payload+scalar_objects+units+scales != corrected["arrays"]:
        raise ValueError("state_bytes disagrees with explicit current accounting")
    mark_diagnostics = {}
    for suffix in ("1", "2"):
        b = np.asarray(getattr(state, "b"+suffix), dtype=float)
        weights = np.asarray(getattr(state, "p"+suffix), dtype=float)
        gram = b.T@(weights[:, None]*b)
        singular_values = np.linalg.svd(gram, compute_uv=False)
        condition = singular_values[0]/singular_values[-1] if singular_values[-1] > 0 else float("inf")
        mark_diagnostics["population_"+suffix] = dict(
            gram_condition_2=float(condition) if np.isfinite(condition) else None,
            gram_condition_status="finite" if np.isfinite(condition) else "singular_or_unresolved_float64_diagnostic",
            gram_largest_singular_value=float(singular_values[0]),
            gram_smallest_singular_value=float(singular_values[-1]),
            maximum_absolute_feature=float(np.max(np.abs(b))))
    mark_diagnostics["D_operator_norm_2"] = float(np.linalg.norm(np.asarray(state.D, dtype=float), ord=2))
    mark_diagnostics["meaning"] = "P-rule frozen normalized-mark diagnostics recalculated in float64 from exact restarts; not original Q raw-Gram conditioning or a certificate."
    # The dimensions and data point count are measured from the decoded values.
    return dict(recorded=old_bytes, recounted=corrected,
                array_byte_correction=corrected["arrays"]-old_bytes["arrays"],
                array_storage_breakdown=dict(ndarray_payload_or_pointers=pointer_or_payload,
                                             scalar_objects=scalar_objects,
                                             rational_units_integers=units,
                                             rational_scale_integers=scales),
                decoded_state_scalars=sum(a.size for a in arrays),
                decoded_data_scalars=sum(getattr(data, k).size for k in ("inputs", "labels", "probabilities")),
                frozen_mark_diagnostics=mark_diagnostics,
                counter_source_sha256=digest(observable_solver.__file__),
                meaning="Retained per-entry accounting; excludes array headers and Python metadata heap; integer sharing is not deduplicated.")


def _comparison(left, right, left_data, right_data):
    a, b = left["configuration"], right["configuration"]
    if a["law"] != b["law"]:
        return None
    changed = sorted(key for key in set(a)|set(b) if key != "id" and a.get(key) != b.get(key))
    if changed == ["order"]:
        kind = "dictionary_order"
    elif changed and set(changed) <= {"digits", "backend"}:
        kind = "arithmetic_precision"
    elif changed and set(changed) <= {"initialization_nodes", "population_nodes", "nodes_per_arc", "steps"}:
        kind = "single_numerical_axis" if len(changed) == 1 else "joint_numerical_refinement"
    else:
        return None
    if left_data["circle"].shape != right_data["circle"].shape:
        raise ValueError("comparison requires corresponding saved circle panels")
    circle_difference = float(np.max(np.abs(left_data["circle"]-right_data["circle"])))
    if circle_difference > 1e-12:
        raise ValueError("saved circle indices do not represent the same panel")
    difference = right_data["prediction"]-left_data["prediction"]
    return dict(left=left["id"], right=right["id"], kind=kind, changed_parameters=changed,
                final_panel_max_abs_prediction_difference=float(np.max(np.abs(difference))),
                final_panel_rms_prediction_difference=float(np.sqrt(np.mean(difference*difference))),
                panel_coordinate_max_abs_difference=circle_difference,
                right_minus_left_loss=right["loss_final"]-left["loss_final"],
                right_minus_left_paired_rms1=right["rms1"]-left["rms1"],
                right_minus_left_paired_rms2=right["rms2"]-left["rms2"])


def analyze(plan_path, runs_path, *, recount_state=False, source_revision=None):
    plan_path, runs_path = Path(plan_path), Path(runs_path)
    plan = json.loads(plan_path.read_text())
    plan_hash = digest(plan_path)
    configured = plan["configurations"]
    if len({c["id"] for c in configured}) != len(configured):
        raise ValueError("configuration IDs must be unique")
    summary = dict(format="observable-validation-summary-v1", plan_sha256=plan_hash,
                   plan_version=plan["version"], source_revision_label=source_revision,
                   inputs=dict(plan=str(plan_path.resolve()), runs=str(runs_path.resolve())),
                   postprocessor_sha256=digest(__file__),
                   prediction_domain="Final t="+str(plan["horizon"])+" at "+str(plan["common"]["circle_directions"])+" saved circle indices.",
                   interpretation="Differences between numerical witnesses, not canonical-error bounds, full-circle suprema, time-uniform bounds or a monotone-convergence claim.",
                   memory_recount_requested=recount_state, runs=[], comparisons=[], problems=[])
    retained, panels = {}, {}
    for config in configured:
        name = config["id"]
        if not re.fullmatch(r"[A-Za-z0-9_-]+", name):
            raise ValueError("configuration ID is not a safe directory name")
        folder = runs_path/name
        record_path = folder/"record.json"
        if not record_path.is_file():
            summary["problems"].append(dict(id=name, problem="missing_record"))
            continue
        record = json.loads(record_path.read_text())
        if record.get("id") != name or record.get("configuration") != config or record.get("plan_sha256") != plan_hash:
            raise ValueError("record does not match the declared plan: "+name)
        row = dict(id=name, configuration=config, status=record.get("status"),
                   record_sha256=digest(record_path), recorded_source_hashes=record.get("source_hashes", {}),
                   producer_sha256=record.get("producer_sha256"), output_hashes_verified={})
        for filename, expected in record.get("outputs", {}).items():
            if Path(filename).name != filename:
                raise ValueError("record output name must be a basename")
            file = folder/filename
            if not file.is_file() or digest(file) != expected:
                raise ValueError("recorded output hash mismatch: "+str(file))
            row["output_hashes_verified"][filename] = expected
        if record.get("status") != "operational_pass":
            row["error"] = record.get("error")
            summary["runs"].append(row)
            summary["problems"].append(dict(id=name, problem="recorded_nonpass"))
            continue
        dimensions = record["dimensions"]
        d1, d2, p1, p2, m = [dimensions[k] for k in
                            ("first_features", "second_features", "first_nodes", "second_nodes", "input_nodes")]
        if dimensions["action_matrix"] != [d2, d1]:
            raise ValueError("recorded action matrix dimensions disagree")
        archive = folder/"observations.npz"
        data, motion = _observations(archive, dimensions, plan["common"]["circle_directions"])
        for phase in ("initialization", "evolution", "restart", "observation", "total"):
            row[phase+"_seconds"] = record[phase+"_seconds"]
        row.update(dimensions=dimensions, dictionary_nodes=record["initialization_metadata"]["dictionary_nodes"],
                   initialization_metadata=record["initialization_metadata"],
                   state_scalars=p1*(d1+5)+p2*(d2+2)+2*d1*d2, data_scalars=4*m,
                   dynamic_scalars=2*p1+p2+d1*d2,
                   recorded_state_bytes_initial=record["state_bytes_initial"],
                   recorded_state_bytes_final=record["state_bytes_final"],
                   peak_rss_bytes=record["peak_rss_bytes"],
                   checkpoint_bytes=record["checkpoint_bytes"],
                   observations_file_bytes=archive.stat().st_size,
                   observation_payload_bytes=sum(a.nbytes for a in data.values()),
                   loss_initial=record["loss_initial"], loss_final=record["loss_final"],
                   rms1=record["rms1"], rms2=record["rms2"],
                   prediction_max_abs=float(np.max(np.abs(data["prediction"]))),
                   dynamic_changes=record["dynamic_changes"], restart_exact=record["restart_exact"], **motion)
        row["rms1_recomputation_abs_difference"] = abs(row["rms1"]-motion["rms1_from_saved_pairs"])
        row["rms2_recomputation_abs_difference"] = abs(row["rms2"]-motion["rms2_from_saved_pairs"])
        if recount_state:
            row["state_memory_postprocess"] = _recount(folder/"final_restart.json", record["state_bytes_final"])
            if row["state_memory_postprocess"]["decoded_state_scalars"] != row["state_scalars"]:
                raise ValueError("exact restart scalar count disagrees with recorded dimensions")
        if not row["restart_exact"]:
            summary["problems"].append(dict(id=name, problem="restart_mismatch"))
        retained[name], panels[name] = record, data
        summary["runs"].append(row)
    for left, right in itertools.combinations(retained, 2):
        comparison = _comparison(retained[left], retained[right], panels[left], panels[right])
        if comparison is not None:
            summary["comparisons"].append(comparison)
    supervisor_path = runs_path/"supervisor.json"
    if supervisor_path.is_file():
        supervisor = json.loads(supervisor_path.read_text())
        if supervisor.get("plan_sha256") != plan_hash:
            raise ValueError("supervisor plan hash differs")
        summary["supervisor"] = dict(sha256=digest(supervisor_path),
                                     charged_total_cpu_seconds=supervisor["total_cpu_seconds"],
                                     all_records=supervisor["configurations"])
    successful = [r for r in summary["runs"] if r["status"] == "operational_pass"]
    summary["aggregate"] = dict(declared_configurations=len(configured), read_records=len(summary["runs"]),
                                 recorded_operational_passes=len(successful),
                                 sum_worker_total_cpu_seconds=sum(r["total_seconds"]["cpu"] for r in successful),
                                 sum_worker_total_wall_seconds=sum(r["total_seconds"]["wall"] for r in successful),
                                 maximum_worker_peak_rss_bytes=max((r["peak_rss_bytes"] for r in successful), default=0))
    return summary


def _number(value):
    return f"{value:.6g}"


def markdown(summary):
    lines = ["# Recorded observable-solver validation", "", summary["prediction_domain"], "",
             summary["interpretation"], "",
             "| Run | Features | Q / P | Data / steps | Init CPU s | Evolve CPU s | Total CPU s | Peak MiB | State KiB | Layer 1 RMS | Layer 2 RMS |",
             "| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for row in summary["runs"]:
        if row["status"] != "operational_pass":
            lines.append("| "+row["id"]+" | "+str(row["status"])+" | | | | | | | | | |")
            continue
        c, d = row["configuration"], row["dimensions"]
        state_bytes = row.get("state_memory_postprocess", {}).get("recounted", row["recorded_state_bytes_final"])["arrays"]
        fields = [row["id"], f"{d['first_features']} / {d['second_features']}",
                  f"{c['initialization_nodes']} / {c['population_nodes']}", f"{d['input_nodes']} / {c['steps']}",
                  _number(row["initialization_seconds"]["cpu"]), _number(row["evolution_seconds"]["cpu"]),
                  _number(row["total_seconds"]["cpu"]), _number(row["peak_rss_bytes"]/2**20),
                  _number(state_bytes/1024), _number(row["rms1"]), _number(row["rms2"])]
        lines.append("| "+" | ".join(fields)+" |")
    lines.extend(["", "State KiB uses corrected retained-array accounting when requested; it is separate from process peak RSS.",
                  "Recorded timings belong to the source hashes in each original record. Totals include restart checks and observations.", "",
                  "| Run | P-mark Gram condition 1 | P-mark Gram condition 2 | D operator norm | Max absolute b1 | Max absolute b2 |",
                  "| --- | ---: | ---: | ---: | ---: | ---: |"])
    for row in summary["runs"]:
        diagnostics = row.get("state_memory_postprocess", {}).get("frozen_mark_diagnostics")
        if diagnostics is not None:
            fields = [row["id"]]
            fields.extend(_number(diagnostics["population_"+suffix]["gram_condition_2"])
                          if diagnostics["population_"+suffix]["gram_condition_2"] is not None else "unresolved"
                          for suffix in ("1", "2"))
            fields.append(_number(diagnostics["D_operator_norm_2"]))
            fields.extend(_number(diagnostics["population_"+suffix]["maximum_absolute_feature"])
                          for suffix in ("1", "2"))
            lines.append("| "+" | ".join(fields)+" |")
    lines.extend(["", "These are postprocessed P-rule normalized-mark diagnostics, not the omitted original Q raw-Gram condition numbers.", "",
                  "| Left → right | Changed parameters | Final panel max prediction difference | Final panel RMS prediction difference |",
                  "| --- | --- | ---: | ---: |"])
    for comparison in summary["comparisons"]:
        lines.append("| "+comparison["left"]+" → "+comparison["right"]+" | "+", ".join(comparison["changed_parameters"])+
                     " | "+_number(comparison["final_panel_max_abs_prediction_difference"])+" | "+
                     _number(comparison["final_panel_rms_prediction_difference"])+" |")
    lines.extend(["", "All comparable declared pairs are listed; no reference solution or favorable subset is selected.", ""])
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--runs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True, help="fresh output directory")
    parser.add_argument("--recount-state", action="store_true", help="load exact restarts and apply current retained-state byte counter")
    parser.add_argument("--source-revision", help="provenance label; source hashes remain authoritative")
    args = parser.parse_args(argv)
    if args.output.exists():
        raise FileExistsError("postprocessing output must be fresh")
    start = time.process_time()
    summary = analyze(args.plan, args.runs, recount_state=args.recount_state, source_revision=args.source_revision)
    summary["postprocessing_cpu_seconds"] = time.process_time()-start
    summary["postprocessing_python"] = sys.version
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output/"summary.json").write_text(json.dumps(summary, indent=2, allow_nan=False)+"\n")
    (args.output/"summary.md").write_text(markdown(summary))
    print(json.dumps(dict(aggregate=summary["aggregate"], comparisons=len(summary["comparisons"]),
                         problems=summary["problems"], output=str(args.output.resolve()),
                         postprocessing_cpu_seconds=summary["postprocessing_cpu_seconds"]), indent=2))
    return int(bool(summary["problems"]))


if __name__ == "__main__":
    raise SystemExit(main())
