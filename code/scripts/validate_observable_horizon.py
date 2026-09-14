"""One predeclared physical-horizon observable validation configuration.

The H3 initializer, dynamics, Heun step and checkpoint encoding are unchanged.
Use the bounded supervisor with --worker validate_observable_horizon.py.
Observations at a fixed finite list of times are output only, never feedback.
"""
import argparse
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import resource
import sys
import time
import traceback

import numpy as np

from pde import (observable_fixed, observable_arithmetic, observable_words,
                 observable_compiler, observable_initialization, observable_solver,
                 observable_laws)
from pde.observable_fixed import Fixed
from pde.observable_laws import (OrthogonalArcLaw, RationalRadius, LawLimits,
                                 radius_from_record, supported_radius, supported_law)


STATE_KEYS = ("b1", "g", "w", "p1", "b2", "c", "p2", "M", "D")
FROZEN_KEYS = ("b1", "g", "p1", "b2", "p2", "D")
DATA_KEYS = ("inputs", "labels", "probabilities")
OBSERVATION_FORMAT = "observable-horizon-observations-v1"


def digest(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as source:
        for block in iter(lambda: source.read(1024*1024), b""):
            value.update(block)
    return value.hexdigest()


def encode_array(value, arithmetic):
    """Exact working scalar representation, including signed floating zero."""
    array = np.asarray(value)
    if not arithmetic.finite(array):
        raise ValueError("cannot encode a nonfinite working observation")
    if arithmetic.digits is None:
        values = [float(x).hex() for x in array.flat]
    elif arithmetic.backend == "rational":
        values = [hex(x.units) for x in array.flat]
    else:
        values = [str(x) for x in array.flat]
    return dict(shape=list(array.shape), values=values)


def _json_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def frozen_signature(state, data):
    ar = state.arithmetic
    return dict(state={key: _json_hash(encode_array(getattr(state, key), ar)) for key in FROZEN_KEYS},
                data={key: _json_hash(encode_array(getattr(data, key), ar)) for key in DATA_KEYS},
                state_metadata=_json_hash(state.metadata), data_metadata=_json_hash(data.metadata),
                arithmetic=dict(digits=ar.digits, backend=ar.backend))


def exact_restart_comparison(first, first_data, second, second_data):
    """Compare every array, both metadata mappings and arithmetic settings."""
    a, b = first.arithmetic, second.arithmetic
    result = dict(arithmetic=(a.digits, a.backend) == (b.digits, b.backend),
                  state_metadata=first.metadata == second.metadata,
                  data_metadata=first_data.metadata == second_data.metadata)
    for key in STATE_KEYS:
        result["state_"+key] = encode_array(getattr(first, key), a) == encode_array(getattr(second, key), b)
    for key in DATA_KEYS:
        result["data_"+key] = encode_array(getattr(first_data, key), a) == encode_array(getattr(second_data, key), b)
    result["all_exact"] = all(result.values())
    return result


def build_law(plan, config):
    parameters = dict(plan["law_parameters"][config["law"]])
    description = parameters.pop("radius")
    limits = LawLimits(**plan["common"]["law_limits"])
    if description == "supported_radius":
        if plan["supported_radius"] != supported_radius().to_record(limits=limits):
            raise ValueError("plan radius differs from the fixed supported-family radius")
        tag = parameters.pop("scope_tag", None)
        if tag not in (None, "H4_explicit_supported_T40"):
            raise ValueError("supported law has a conflicting scientific scope tag")
        return supported_law(**parameters), limits
    elif isinstance(description, dict) and description.get("kind") == "rational" and isinstance(description.get("value"), str):
        radius = RationalRadius(description["value"])
    else:
        radius = radius_from_record(description, limits=limits)
    if parameters.get("scope_tag") == "H4_explicit_supported_T40":
        raise ValueError("the supported scope tag requires the canonical supported law constructor")
    return OrthogonalArcLaw(radius, **parameters), limits


def _add_timing(timing, wall, cpu):
    timing["wall"] += time.perf_counter()-wall
    timing["cpu"] += time.process_time()-cpu


def observe_path(state, data, *, steps, step_size, observation_times,
                 restart_time, block_size, observer, checkpoint, timing):
    """Advance unchanged Heun to a fixed event list; never evolve interpolants.

    At an off-mesh time retain the adjacent actual nodes, observe their affine
    interpolant, then continue from the right node. Checkpoint time must be a
    node. Only a constant number of states is live, independently of steps.
    Callbacks are internal output operations and must not mutate supplied data.
    """
    if type(steps) is not int or steps < 1:
        raise ValueError("steps must be a positive integer")
    h = Fraction(step_size)
    horizon = h*steps
    times = [Fraction(t) for t in observation_times]
    restart = Fraction(restart_time)
    if h <= 0 or times != sorted(set(times)) or not times or times[0] < 0 or times[-1] > horizon:
        raise ValueError("invalid fixed observation schedule")
    restart_index = restart/h
    if restart <= 0 or restart >= horizon or restart_index.denominator != 1:
        raise ValueError("restart must be a strict interior mesh node")
    events = sorted(set(times+[restart, horizon]))
    current, current_index = state, 0
    last_left, last_right, last_right_index = None, None, None

    def advance(count):
        nonlocal current, current_index
        if count:
            wall, cpu = time.perf_counter(), time.process_time()
            current = observable_solver.evolve(current, data, steps=count, step_size=h, block_size=block_size)
            _add_timing(timing, wall, cpu)
            current_index += count

    for instant in events:
        coordinate = instant/h
        left_index = coordinate.numerator//coordinate.denominator
        if coordinate.denominator == 1:
            if left_index < current_index:
                raise ValueError("node event precedes current integration node")
            last_left = last_right = last_right_index = None
            advance(left_index-current_index)
            observation_state = current
        else:
            right_index = left_index+1
            if last_right_index != right_index:
                if left_index < current_index:
                    raise ValueError("unavailable adjacent nodes for off-mesh event")
                advance(left_index-current_index)
                last_left = current
                advance(1)
                last_right, last_right_index = current, right_index
            observation_state = observable_solver.interpolate_state(last_left, last_right, coordinate-left_index)
        if instant in times:
            observer(instant, observation_state)
        if instant == restart:
            checkpoint(instant, current)
    return current


def collect_observation(state, data, circle, *, block_size):
    ar = state.arithmetic
    with ar.context():
        pairs = observable_solver.paired_observations(state, data, block_size=block_size)
        prediction = observable_solver.predict(state, circle, block_size=block_size)
        training_prediction = observable_solver.predict(state, data.inputs, block_size=block_size)
        residual = training_prediction-data.labels
        value = data.probabilities @ (residual*residual)
    return dict(**pairs, circle=circle.copy(), prediction=prediction,
                training_prediction=training_prediction, labels=data.labels.copy(), loss=np.asarray(value))


def save_observation(output, index, instant, state, data, circle, *, block_size):
    arrays = collect_observation(state, data, circle, block_size=block_size)
    ar = state.arithmetic
    base = "observation_"+str(index).zfill(2)
    exact_name, npz_name = base+".json", base+".npz"
    exact = dict(format=OBSERVATION_FORMAT, time=str(instant), digits=ar.digits,
                 backend=ar.backend, arrays={key: encode_array(value, ar) for key, value in arrays.items()})
    with (output/exact_name).open("x", encoding="utf-8") as stream:
        json.dump(exact, stream, separators=(",", ":"), allow_nan=False)
    del exact
    floating = {key: np.asarray(value, dtype=float) for key, value in arrays.items()}
    if not all(np.isfinite(value).all() for value in floating.values()):
        raise ValueError("requested float64 observation view is nonfinite")
    with (output/npz_name).open("xb") as stream:
        np.savez_compressed(stream, **floating)
    return dict(time=str(instant), npz=npz_name, exact_json=exact_name,
                loss=float(floating["loss"]), rms1=float(floating["rms1"]), rms2=float(floating["rms2"]),
                exact_bytes=(output/exact_name).stat().st_size, npz_bytes=(output/npz_name).stat().st_size,
                float_view_payload_bytes=sum(value.nbytes for value in floating.values()))


def conditioning_diagnostics(state):
    result = dict(scope="float64 diagnostics of frozen normalized P-node Grams; not Q raw-Gram conditioning or error certificates")
    for suffix in ("1", "2"):
        try:
            b = np.asarray(getattr(state, "b"+suffix), dtype=float)
            p = np.asarray(getattr(state, "p"+suffix), dtype=float)
            gram = b.T @ (p[:, None]*b)
            if not np.isfinite(gram).all():
                raise ValueError("nonfinite converted Gram")
            singular = np.linalg.svd(gram, compute_uv=False)
            ratio = singular[0]/singular[-1] if singular[-1] > 0 else float("inf")
            result["population_"+suffix] = dict(
                singular_values=singular.tolist(), condition_2=float(ratio) if np.isfinite(ratio) else None,
                condition_status="finite" if np.isfinite(ratio) else "singular_or_unresolved",
                maximum_absolute_feature=float(np.max(np.abs(b))))
        except (ValueError, OverflowError, np.linalg.LinAlgError) as exc:
            result["population_"+suffix] = dict(condition_2=None, condition_status="unresolved_float64_diagnostic", error=str(exc))
    try:
        value = float(np.linalg.norm(np.asarray(state.D, float), ord=2))
        result["initialized_matrix_norm"] = value if np.isfinite(value) else None
        result["initialized_matrix_norm_status"] = "finite" if np.isfinite(value) else "unresolved_float64_diagnostic"
    except (ValueError, OverflowError, np.linalg.LinAlgError) as exc:
        result.update(initialized_matrix_norm=None, initialized_matrix_norm_status="unresolved_float64_diagnostic", error=str(exc))
    return result


def array_bytes(array):
    result = array.nbytes
    if array.dtype == object:
        result += sum(sys.getsizeof(x) for x in array.flat)
        result += sum(sys.getsizeof(x.units)+sys.getsizeof(x.scale) for x in array.flat if isinstance(x, Fixed))
    return result


def workspace_accounting(state, data, block_size):
    """Conservative structural scalar slots; process RSS is measured separately.

    Six full state payloads and eight extra dynamic payloads cover source,
    copied current, adjacent/interpolated observation, final/restored comparison,
    and Heun stages/velocities/expression temporaries. They are a deliberately
    loose allowance, not an instrumented peak allocator measurement. The fixed
    pair outputs and serialized strings are outside the evolution workspace.
    """
    p1, p2, a = len(state.b1), len(state.b2), len(data.inputs)
    d1, d2 = state.b1.shape[1], state.b2.shape[1]
    total = sum(getattr(state, key).size for key in STATE_KEYS)
    moving = state.w.size+state.c.size+state.M.size
    block = min(block_size, a)
    block_slots = 32*(p1+p2)*block+12*(d1+d2)*block+8*d1*d2
    slots = 6*total+8*moving+12*a+block_slots
    arrays = [getattr(state, key) for key in STATE_KEYS]+[getattr(data, key) for key in DATA_KEYS]
    scalar_bytes = 8
    max_units_bits = max_scale_bits = 0
    for array in arrays:
        if array.dtype == object:
            for value in array.flat:
                size = array.itemsize+sys.getsizeof(value)
                if isinstance(value, Fixed):
                    size += sys.getsizeof(value.units)+sys.getsizeof(value.scale)
                    max_units_bits = max(max_units_bits, abs(value.units).bit_length())
                    max_scale_bits = max(max_scale_bits, value.scale.bit_length())
                scalar_bytes = max(scalar_bytes, size)
    return dict(state_scalars=total, dynamic_scalars=moving, data_scalars=4*a,
                fixed_state_payload_allowance=6, extra_dynamic_payload_allowance=8,
                block_workspace_scalar_allowance=block_slots,
                evolution_scalar_slot_allowance=slots, independent_of_elapsed_step_count=True,
                current_max_scalar_storage_bytes=scalar_bytes,
                evolution_bytes_at_current_scalar_size=slots*scalar_bytes,
                final_pair_scalars=2*(p1+p2)*a,
                maximum_fixed_units_bits=max_units_bits, maximum_fixed_scale_bits=max_scale_bits,
                excludes="Python headers, metadata heap, serialized observation/checkpoint strings and elementary temporary Fractions; current scalar byte size is not a future magnitude bound")


def _write_record(path, record):
    temporary = path.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(record, indent=2, allow_nan=False)+"\n")
    temporary.replace(path)


def run(plan_path, run_id, output):
    plan_path, output = Path(plan_path).resolve(), Path(output)
    plan = json.loads(plan_path.read_text())
    config = next(c for c in plan["configurations"] if c["id"] == run_id)
    output.mkdir(parents=True, exist_ok=False)
    resource.setrlimit(resource.RLIMIT_CPU, (plan["budget"]["cpu_seconds_per_configuration"],)*2)
    modules = (observable_fixed, observable_arithmetic, observable_words, observable_compiler,
               observable_initialization, observable_solver, observable_laws)
    record = dict(id=run_id, configuration=config, plan_sha256=digest(plan_path), plan_version=plan["version"],
                  status="running", command=sys.argv, cwd=str(Path.cwd()),
                  source_hashes={Path(m.__file__).name: digest(m.__file__) for m in modules},
                  producer_sha256=digest(__file__), python=sys.version, numpy=np.__version__,
                  platform=platform.platform(), processor=platform.processor(),
                  thread_environment={k: os.environ.get(k) for k in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
                  observations=[], evolution_seconds=dict(wall=0., cpu=0.), observation_seconds=dict(wall=0., cpu=0.),
                  checkpoint_write_seconds=dict(wall=0., cpu=0.))
    record_path = output/"record.json"
    wall_start, cpu_start = time.perf_counter(), time.process_time()
    _write_record(record_path, record)
    try:
        common = plan["common"]
        wall, cpu = time.perf_counter(), time.process_time()
        state = observable_solver.initialize(config["order"], initialization_nodes=config["initialization_nodes"],
                    population_nodes=config["population_nodes"], digits=config["digits"], backend=config["backend"],
                    epsilon_cov=common["epsilon_cov"])
        ar = state.arithmetic
        law, limits = build_law(plan, config)
        data = law.quadrature(config["nodes_per_arc"], ar, limits=limits,
                              allow_collapse=common["allow_radius_collapse"])
        record["initialization_seconds"] = dict(wall=time.perf_counter()-wall, cpu=time.process_time()-cpu)
        record["initialization_metadata"] = state.metadata
        record["law_metadata"] = data.metadata
        record["state_bytes_initial"] = observable_solver.state_bytes(state)
        record["data_bytes"] = dict(arrays=sum(array_bytes(getattr(data, k)) for k in DATA_KEYS),
                                    metadata_utf8=len(json.dumps(data.metadata).encode()),
                                    exact_description_utf8=data.metadata["exact_description_utf8_bytes"])
        record["dimensions"] = dict(first_features=state.b1.shape[1], second_features=state.b2.shape[1],
                                    first_nodes=len(state.b1), second_nodes=len(state.b2), input_nodes=len(data.inputs),
                                    action_matrix=list(state.M.shape))
        record["conditioning_diagnostics"] = conditioning_diagnostics(state)
        record["workspace_initial"] = workspace_accounting(state, data, common["block_size"])
        frozen = frozen_signature(state, data)
        record["frozen_signature_initial"] = frozen
        circle = observable_solver.circle_inputs(common["circle_directions"], ar)
        steps, h = config["steps"], Fraction(plan["horizon"])/config["steps"]
        restart_index = Fraction(common["restart_time"])/h
        if restart_index.denominator != 1:
            raise ValueError("declared restart is not on the declared mesh")
        record["restart_contract"] = dict(time=common["restart_time"], step_size=str(h), steps_before=int(restart_index),
                    steps_after=steps-int(restart_index), block_size=common["block_size"],
                    method=plan["method"], arithmetic=dict(digits=ar.digits, backend=ar.backend))

        def observer(instant, observed):
            wall, cpu = time.perf_counter(), time.process_time()
            record["observations"].append(save_observation(output, len(record["observations"]), instant,
                                                         observed, data, circle, block_size=common["block_size"]))
            _add_timing(record["observation_seconds"], wall, cpu)
            _write_record(record_path, record)

        def checkpoint(instant, current):
            wall, cpu = time.perf_counter(), time.process_time()
            observable_solver.save_restart(output/"midpoint_restart.json", current, data)
            _add_timing(record["checkpoint_write_seconds"], wall, cpu)

        final = observe_path(state, data, steps=steps, step_size=h, observation_times=common["observation_times"],
                     restart_time=common["restart_time"], block_size=common["block_size"], observer=observer,
                     checkpoint=checkpoint, timing=record["evolution_seconds"])
        del state
        record["frozen_signature_final"] = frozen_signature(final, data)
        if frozen != record["frozen_signature_final"]:
            raise AssertionError("frozen marks, data or metadata changed during evolution")
        wall, cpu = time.perf_counter(), time.process_time()
        restored, restored_data = observable_solver.load_restart(output/"midpoint_restart.json")
        resumed = observable_solver.evolve(restored, restored_data, steps=steps-int(restart_index),
                                           step_size=h, block_size=common["block_size"])
        record["restart_comparison"] = exact_restart_comparison(final, data, resumed, restored_data)
        record["restart_prediction_exact"] = (
            encode_array(observable_solver.predict(final, circle, block_size=common["block_size"]), ar) ==
            encode_array(observable_solver.predict(resumed, circle, block_size=common["block_size"]), ar))
        record["restart_exact"] = record["restart_comparison"]["all_exact"] and record["restart_prediction_exact"]
        record["restart_seconds"] = dict(wall=time.perf_counter()-wall, cpu=time.process_time()-cpu)
        if not record["restart_exact"]:
            raise AssertionError("own-state disk continuation differs in retained values, data or metadata")
        del restored, resumed, restored_data
        expected_times = [str(Fraction(t)) for t in common["observation_times"]]
        if [row["time"] for row in record["observations"]] != expected_times:
            raise AssertionError("saved observations differ from the fixed plan")
        record["loss_initial"], record["loss_final"] = record["observations"][0]["loss"], record["observations"][-1]["loss"]
        record["rms1"], record["rms2"] = record["observations"][-1]["rms1"], record["observations"][-1]["rms2"]
        with ar.context():
            changes = dict(row_max_abs=float(np.max(np.abs(np.asarray(final.w-final.g, float)))),
                readout_max_abs=float(np.max(np.abs(np.asarray(final.c, float)))),
                matrix_frobenius=float(np.linalg.norm(np.asarray(final.M-final.D, float))))
        if not all(math.isfinite(value) for value in changes.values()):
            raise ValueError("nonfinite requested dynamic-change diagnostic")
        record["dynamic_changes"] = changes
        record["state_bytes_final"] = observable_solver.state_bytes(final)
        record["workspace_final"] = workspace_accounting(final, data, common["block_size"])
        wall, cpu = time.perf_counter(), time.process_time()
        observable_solver.save_restart(output/"final_restart.json", final, data)
        _add_timing(record["checkpoint_write_seconds"], wall, cpu)
        record["checkpoint_bytes"] = (output/"midpoint_restart.json").stat().st_size
        record["final_checkpoint_bytes"] = (output/"final_restart.json").stat().st_size
        record["observation_storage"] = "Exact working scalar JSON and separate float64 NPZ at six fixed times; none is a runtime input"
        record["status"] = "operational_pass"
    except Exception as exc:
        record.update(status="failure", error=repr(exc), traceback=traceback.format_exc())
    finally:
        record["total_seconds"] = dict(wall=time.perf_counter()-wall_start, cpu=time.process_time()-cpu_start)
        record["peak_rss_bytes"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024
        record["outputs"] = {path.name: digest(path) for path in output.iterdir()
                             if path.is_file() and path.name not in ("record.json", "record.json.tmp")}
        _write_record(record_path, record)
    print(json.dumps({key: record.get(key) for key in ("id", "status", "total_seconds", "peak_rss_bytes", "error")}))
    return 0 if record["status"] == "operational_pass" else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True)
    parser.add_argument("--id", required=True)
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()
    raise SystemExit(run(arguments.plan, arguments.id, arguments.output))
