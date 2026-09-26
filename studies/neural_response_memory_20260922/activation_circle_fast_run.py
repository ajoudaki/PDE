"""Optional fast execution of the same activation-circle runner and event rules.

Use --config JSON --out FRESH_DIRECTORY. Required config fields are inputs,
labels,model,activation; every effective control is frozen in config.json.
Observation predictions do not control the ODE or its endpoint.
"""

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import resource
import subprocess
import sys
import time
import traceback
import zipfile

import numpy as np
import torch

from activation_moment_engine import (ACTIVATIONS, ActivationDenseEngine, ActivationMomentEngine,
                                      combine, controlled_error)
from activation_fast_engine import FastActivationTrial, FastActivationMomentEngine


ERROR_CONTROL = ("max vector/moment block RMS ratio and hidden-link Frobenius/sqrt(n) ratios; "
                 "denominator atol+rtol*max(1,current block norm,candidate block norm); "
                 "hidden scales use W-W0, identically for dense and moment")


def scalar(value):
    return float(value.detach().cpu())


def synchronize(device):
    if torch.device(device).type == "cuda":
        torch.cuda.synchronize(device)


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda:stream.read(1<<20),b""):
            digest.update(chunk)
    return digest.hexdigest()


def array_hash(*values):
    digest = hashlib.sha256()
    for value in values:
        if isinstance(value,torch.Tensor):
            value = value.detach().cpu().numpy()
        value = np.asarray(value)
        digest.update(str(value.shape).encode())
        digest.update(str(value.dtype).encode())
        digest.update(value.tobytes(order="C"))
    return digest.hexdigest()


def save_archive(path, **payload):
    """Create once, then read every ZIP member to validate its stored CRC."""
    path = Path(path)
    if path.exists():
        raise FileExistsError("refusing to overwrite archive: "+str(path))
    np.savez(path, **payload)
    with zipfile.ZipFile(path) as archive:
        bad = archive.testzip()
    if bad is not None:
        raise IOError("CRC validation failed: "+str(path)+":"+bad)


def feature_diagnostics(engine,state,fields,initial_features):
    result = dict(w_motion_rms=scalar((state.w-engine.initial.w).square().mean().sqrt()),
                  c_motion_rms=scalar((state.c-engine.initial.c).square().mean().sqrt()))
    diagnostics = {}
    for layer in (1,2,3):
        z,h,derivative = (fields[name+str(layer)] for name in ("z","h","derivative"))
        result["feature_motion_h"+str(layer)+"_rms"] = scalar((h-initial_features[layer]).square().mean().sqrt())
        diagnostics["layer"+str(layer)] = dict(
            activation_mean=scalar(h.mean()),activation_rms=scalar(h.square().mean().sqrt()),
            activation_min=scalar(h.min()),activation_max=scalar(h.max()),
            preactivation_rms=scalar(z.square().mean().sqrt()),
            nonpositive_preactivation_fraction=scalar((z <= 0).to(z.dtype).mean()),
            derivative_mean=scalar(derivative.mean()),derivative_rms=scalar(derivative.square().mean().sqrt()),
            derivative_min=scalar(derivative.min()),derivative_max=scalar(derivative.max()),
            small_derivative_fraction=scalar((derivative.abs() <= 1e-3).to(z.dtype).mean()),
            zero_derivative_fraction=scalar((derivative == 0).to(z.dtype).mean()),
            negative_derivative_fraction=scalar((derivative < 0).to(z.dtype).mean()))
        if engine.activation == "sigmoid":
            diagnostics["layer"+str(layer)]["sigmoid_saturated_fraction"] = scalar(((h <= .01)|(h >= .99)).to(z.dtype).mean())
    result["activation_diagnostics"] = diagnostics
    return result


def repository_metadata(source_names):
    folder = Path(__file__).resolve().parent
    root = folder.parents[1]
    result = dict(cwd=str(Path.cwd().resolve()),repository_root=str(root))
    try:
        result["git_head"] = subprocess.check_output(
            ["git","-C",str(root),"rev-parse","HEAD"],text=True).strip()
        paths = [str((folder/name).relative_to(root)) for name in source_names]
        result["scoped_git_status"] = subprocess.check_output(
            ["git","-C",str(root),"status","--porcelain=v1","--",*paths],text=True)
    except (OSError,subprocess.CalledProcessError) as exc:
        result["git_metadata_error"] = str(exc)
    result["working_source_sha256"] = {name:sha256(folder/name) for name in source_names}
    return result


def training_loss(engine,state):
    return scalar((engine.predict(state,engine.inputs)-engine.labels).square().mean())


def heun_trial(engine,state,step,first=None):
    first = engine.rhs(state) if first is None else first
    euler = combine((1.,step),(state,first))
    second = engine.rhs(euler)
    candidate = combine((1.,step/2,step/2),(state,first,second))
    return first,second,euler,candidate


def heun_interpolant(state,first,second,step,fraction):
    if not 0 <= fraction <= 1:
        raise ValueError("interpolation fraction must lie in [0,1]")
    return combine((1.,step*(fraction-fraction*fraction/2),step*fraction*fraction/2),
                   (state,first,second))


def locate_loss_crossing(engine,state,first,second,step,threshold,iterations=32):
    initial_loss = training_loss(engine,state)
    endpoint_loss = training_loss(engine,heun_interpolant(state,first,second,step,1.))
    if not endpoint_loss <= threshold < initial_loss:
        raise ValueError("accepted step must bracket the loss threshold")
    low,high = 0.,1.
    for _ in range(iterations):
        middle = (low+high)/2
        value = heun_interpolant(state,first,second,step,middle)
        if training_loss(engine,value) > threshold:
            low = middle
        else:
            high = middle
    # Keep the side actually at or below the threshold, up to roundoff.
    value = heun_interpolant(state,first,second,step,high)
    return high,value,training_loss(engine,value)


def panel_predict(engine,state,inputs,block=128):
    return np.concatenate([engine.predict(state,inputs[start:start+block]).cpu().numpy()
                           for start in range(0,len(inputs),block)])


def normalized_config(raw):
    config = dict(raw)
    aliases = {"n":"width","P":"order","wall_seconds":"max_wall_seconds",
               "loss_crossings":"milestones","validation_block":"query_batch_size"}
    for old,new in aliases.items():
        if old in config:
            if new in config and config[new] != config[old]:
                raise ValueError("conflicting config aliases: "+old+" and "+new)
            config[new] = config.pop(old)
    defaults = dict(width=4096,order=1,seed=20260920,device="cpu",threads=1,
                    rtol=1.25e-5,initial_step=.05,max_step=2.,max_time=10000.,
                    max_steps=30000,max_wall_seconds=300.,target_loss=.001,
                    milestones=[.9,.5,.1,.03,.01,.003,.001],observation_times=[10.,100.,1000.],query_count=8192,
                    query_batch_size=128,progress_seconds=30.,bisection_iterations=32)
    for name,value in defaults.items():
        config.setdefault(name,value)
    config.setdefault("atol",config["rtol"]*.01)
    if config.get("activation") not in ACTIVATIONS:
        raise ValueError("activation must be explicitly selected")
    if config.get("model") not in ("dense","moment"):
        raise ValueError("model must be dense or moment")
    integer_names = ("width","order","seed","threads","max_steps","query_count",
                     "query_batch_size","bisection_iterations")
    for name in integer_names:
        value = config[name]
        if isinstance(value,bool) or not isinstance(value,int) or value < (0 if name == "seed" else 1):
            raise ValueError("invalid integer config "+name)
    if config["order"] not in (1,2,3):
        raise ValueError("this experiment predeclares only P=1,2,3")
    for name in ("rtol","atol","initial_step","max_step","max_time","max_wall_seconds",
                 "target_loss","progress_seconds"):
        if not math.isfinite(config[name]) or config[name] <= 0:
            raise ValueError("invalid positive control "+name)
    for threshold in config["milestones"]+config["observation_times"]:
        if not math.isfinite(threshold) or threshold <= 0:
            raise ValueError("invalid milestone")
    u,y = np.asarray(config["inputs"],dtype=np.float64),np.asarray(config["labels"],dtype=np.float64)
    if u.ndim != 2 or u.shape[1] != 2 or len(u) < 1 or y.shape != (len(u),):
        raise ValueError("circle inputs must have shape (M,2), labels shape (M,)")
    if not np.isfinite(u).all() or not np.isfinite(y).all():
        raise ValueError("nonfinite training data")
    if not np.allclose(np.linalg.norm(u,axis=1),1.,rtol=0,atol=1e-12):
        raise ValueError("circle inputs must be unit vectors, without sqrt(2) scaling")
    config["inputs"],config["labels"] = u.tolist(),y.tolist()
    return config


def run(raw_config,out,*,config_path=None):
    process_start = time.monotonic()
    config = normalized_config(raw_config)
    config.setdefault("execution_backend","batched_graphs")
    if config["execution_backend"] not in ("graphs","batched_graphs"):
        raise ValueError("unknown fast execution backend")
    out = Path(out)
    out.mkdir(parents=True,exist_ok=False)
    (out/"config.json").write_text(json.dumps(config,indent=2)+"\n")
    os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG",":4096:8")
    torch.set_num_threads(config["threads"])
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    device = torch.device(config["device"])
    if device.type == "cuda":
        torch.cuda.set_device(device)
        torch.cuda.reset_peak_memory_stats(device)
    inputs,labels = np.asarray(config["inputs"]),np.asarray(config["labels"])
    angles = 2*np.pi*np.arange(config["query_count"])/config["query_count"]
    circle_inputs = np.column_stack((np.cos(angles),np.sin(angles)))
    common = dict(seed=config["seed"],device=device,dtype=torch.float64,activation=config["activation"])
    setup_start = time.monotonic()
    if config["model"] == "dense":
        engine = ActivationDenseEngine(2,config["width"],inputs,labels,**common)
    else:
        engine_type = FastActivationMomentEngine if config["execution_backend"] == "batched_graphs" else ActivationMomentEngine
        engine = engine_type(2,config["width"],config["order"],inputs,labels,**common)
    state = engine.initial_state()
    capture_start = time.monotonic()
    fast_trial = FastActivationTrial(engine,cuda_graph=True,rtol=config["rtol"],atol=config["atol"])
    synchronize(device)
    capture_seconds = time.monotonic()-capture_start
    initialization_hash = array_hash(state.w,engine.W20,engine.W30,state.c)
    synchronize(device)
    setup_seconds = time.monotonic()-setup_start
    folder = Path(__file__).parent
    sources = {name:sha256(folder/name) for name in
               ("activation_circle_fast_run.py","activation_fast_engine.py","activation_circle_run.py",
                "activation_moment_engine.py","deep_moment_engine.py","moment_engine.py")}
    manifest = dict(effective_config_sha256=sha256(out/"config.json"),
                    source_sha256=sources,initialization_hash=initialization_hash,
                    data_sha256=array_hash(inputs,labels),query_sha256=array_hash(circle_inputs),
                    input_config_sha256=sha256(config_path) if config_path else None,
                    input_config_path=str(Path(config_path).resolve()) if config_path else None,
                    execution_backend=config["execution_backend"],capture_seconds=capture_seconds,
                    dtype="float64",device=str(device),device_name=
                    torch.cuda.get_device_name(device) if device.type == "cuda" else platform.processor(),
                    software=dict(python=sys.version,numpy=np.__version__,torch=torch.__version__,
                                  cuda=torch.version.cuda,platform=platform.platform(),threads=config["threads"]),
                    deterministic_algorithms=True,tf32=False,
                    cublas_workspace_config=os.environ.get("CUBLAS_WORKSPACE_CONFIG"),
                    command=sys.argv,initialization_seconds=setup_seconds,
                    closure_mode="direct_"+config["activation"] if engine.moment else None,
                    error_control=ERROR_CONTROL,
                    endpoint_method=str(config["bisection_iterations"])+" bisections of quadratic Heun continuous extension",
                    initialization="NumPy default_rng; w std1, W20 then W30 std1/sqrt(n), stored c std1/n",
                    case=config.get("case",config.get("case_id")),
                    activation=config["activation"],task=config.get("task"),
                    phase=config.get("phase"),run_id=config.get("run_id"),
                    repository=repository_metadata(tuple(sources)),
                    numerical_thread_environment={key:os.environ.get(key) for key in
                    ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS",
                     "VECLIB_MAXIMUM_THREADS","BLIS_NUM_THREADS")})
    (out/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    initial_fields = engine.fields(state)
    initial_features = {layer:initial_fields["h"+str(layer)].clone() for layer in (1,2,3)}
    del initial_fields
    observation_seconds = 0.
    observations,checkpoints = [],[]
    predictions,train_predictions = [],[]
    checkpoint_hashes = {}

    def observe(value,t,loss,label,*,save_state=False,kind=None,requested_time=None,requested_loss=None):
        nonlocal observation_seconds
        start = time.monotonic()
        predictions.append(panel_predict(engine,value,circle_inputs,config["query_batch_size"]))
        train_predictions.append(panel_predict(engine,value,inputs,config["query_batch_size"]))
        record = dict(label=label,time=t,training_mse=loss,kind=kind or label,
                      requested_time=requested_time,requested_loss=requested_loss)
        fields = engine.fields(value)
        record.update(feature_diagnostics(engine,value,fields,initial_features))
        if engine.moment:
            record.update(activity=scalar(value.s),
                          defect_W2_frobenius=scalar(engine.defect_frobenius(value,2,fields)),
                          defect_W3_frobenius=scalar(engine.defect_frobenius(value,3,fields)))
        observations.append(record)
        if save_state:
            filename = "checkpoint_"+label.replace(".","p")+".npz"
            payload = {key:tensor.detach().cpu().numpy() for key,tensor in zip(value.names(),value.tensors())}
            # Fixed Gaussian matrices regenerate exactly from saved config and seed.
            save_archive(out/filename,**payload,physical_time=np.asarray(t),training_mse=np.asarray(loss))
            checkpoints.append(filename)
            checkpoint_hashes[filename] = sha256(out/filename)
        synchronize(device)
        observation_seconds += time.monotonic()-start

    t,step = 0.,config["initial_step"]
    current_loss = training_loss(engine,state)
    times,losses,steps,errors,wall_times = [t],[current_loss],[],[],[0.]
    rejected,loss_increases = 0,0
    thresholds = sorted(set(config["milestones"]+[config["target_loss"]]),reverse=True)
    crossed = set()
    observed_times = set()
    initial_below = [value for value in thresholds if current_loss <= value]
    observe(state,t,current_loss,"initial")
    initial_observation_seconds = observation_seconds
    start = last_report = time.monotonic()
    lifecycle = dict(status="integrating",pid=os.getpid(),integration_start_monotonic=start,
                     integration_start_unix=time.time())
    (out/"lifecycle.json").write_text(json.dumps(lifecycle,indent=2)+"\n")
    last_rejected_error = None
    failure_detail = None
    while True:
        elapsed = time.monotonic()-start
        if current_loss <= config["target_loss"]*(1+1e-12):
            status = "target_loss"; break
        if elapsed >= config["max_wall_seconds"]:
            status = "wall_limit"; break
        if t >= config["max_time"]:
            status = "max_time"; break
        if len(steps) >= config["max_steps"]:
            status = "max_steps"; break
        proposed = min(step,config["max_step"],config["max_time"]-t)
        if proposed < 1e-12*max(1.,t):
            status = "step_underflow"; break
        try:
            first,second,euler,candidate,error,candidate_loss,valid = fast_trial.trial(
                state,proposed,config["rtol"],config["atol"])
            if not valid:
                raise ValueError("nonfinite or invalid fast trial")
        except (ValueError,FloatingPointError) as exc:
            error,valid = float("inf"),False
            last_rejected_error = str(exc)
        except RuntimeError as exc:
            status = "failed"
            failure_detail = dict(exception=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
            break
        if not valid or error > 1:
            rejected += 1
            step = proposed*(max(.1,min(.5,.9/math.sqrt(error))) if math.isfinite(error) else .1)
        else:
            actual_step = proposed
            event_specs = []
            target_fraction = None
            for threshold in thresholds:
                if threshold in crossed or not candidate_loss <= threshold < current_loss:
                    continue
                fraction,event_state,event_loss = locate_loss_crossing(
                    engine,state,first,second,proposed,threshold,config["bisection_iterations"])
                event_specs.append((fraction,"loss",threshold))
                if threshold == config["target_loss"]:
                    target_fraction = fraction
                    candidate,candidate_loss,actual_step = event_state,event_loss,fraction*proposed
            # Endpoint-bracketed roots need not be first roots under nonmonotone
            # loss. Retain only events before the selected numerical target root.
            endpoint_fraction = target_fraction if target_fraction is not None else 1.
            event_specs = [event for event in event_specs if event[0] <= endpoint_fraction]
            endpoint_time = t+actual_step
            for requested in sorted(set(config["observation_times"])):
                before_endpoint = requested < endpoint_time if target_fraction is not None else requested <= endpoint_time
                if requested not in observed_times and t < requested and before_endpoint:
                    event_specs.append(((requested-t)/proposed,"time",requested))
            for fraction,kind,requested in sorted(event_specs,key=lambda item:(item[0],item[1])):
                event_state = heun_interpolant(state,first,second,proposed,fraction)
                event_time = requested if kind == "time" else t+fraction*proposed
                event_loss = training_loss(engine,event_state)
                observe(event_state,event_time,event_loss,kind+"_"+format(requested,".12g"),save_state=True,
                        kind=kind,requested_time=requested if kind == "time" else None,
                        requested_loss=requested if kind == "loss" else None)
                (crossed if kind == "loss" else observed_times).add(requested)
            loss_increases += int(candidate_loss > current_loss+1e-12)
            state,current_loss = candidate,candidate_loss
            t += actual_step
            times.append(t); losses.append(current_loss); steps.append(actual_step); errors.append(error)
            wall_times.append(time.monotonic()-start)
            step = proposed*max(.5,min(2.,.9/math.sqrt(max(error,1e-16))))
        if time.monotonic()-last_report >= config["progress_seconds"]:
            print(json.dumps(dict(event="progress",model=config["model"],P=config["order"],
                                  time=t,training_mse=current_loss,accepted=len(steps),rejected=rejected,
                                  wall_seconds=time.monotonic()-start)),flush=True)
            last_report = time.monotonic()
    synchronize(device)
    integration_wall = time.monotonic()-start
    lifecycle.update(status="integration_complete",integration_end_monotonic=time.monotonic(),
                     integration_end_unix=time.time(),integration_with_observations_seconds=integration_wall)
    (out/"lifecycle.json").write_text(json.dumps(lifecycle,indent=2)+"\n")
    observation_before_final = observation_seconds
    observe(state,t,current_loss,"final")
    save_start = time.monotonic()
    payload = {key:tensor.detach().cpu().numpy() for key,tensor in zip(state.names(),state.tensors())}
    payload.update(times=np.asarray(times),losses=np.asarray(losses),accepted_steps=np.asarray(steps),
                   local_error_ratios=np.asarray(errors),integration_wall_times=np.asarray(wall_times),
                   observation_times=np.asarray([value["time"] for value in observations]),
                   observation_training_mse=np.asarray([value["training_mse"] for value in observations]),
                   observation_labels=np.asarray([value["label"] for value in observations]),
                   circle_angles=angles,circle_inputs=circle_inputs,circle_predictions=np.asarray(predictions),
                   train_inputs=inputs,train_labels=labels,train_predictions=np.asarray(train_predictions),
                   physical_time=np.asarray(t))
    save_archive(out/"arrays.npz",**payload)
    arrays_hash = sha256(out/"arrays.npz")
    saving_seconds = time.monotonic()-save_start
    summary = dict(manifest,model=config["model"],P=config["order"] if engine.moment else None,
                   width=engine.n,hidden_layers=3,d=engine.d,sample_count=engine.M,
                   query_count=config["query_count"],seed=config["seed"],status=status,time=t,
                   training_mse=current_loss,target_loss=config["target_loss"],
                   crossed_losses=sorted(crossed,reverse=True),initially_below_losses=initial_below,
                   observed_physical_times=sorted(observed_times),archive_crc_validated=True,
                   accepted=len(steps),rejected=rejected,loss_increases=loss_increases,
                   rtol=config["rtol"],atol=config["atol"],maximum_step=config["max_step"],
                   initial_step=config["initial_step"],max_time=config["max_time"],max_steps=config["max_steps"],
                   wall_limit_seconds=config["max_wall_seconds"],
                   integration_with_observations_seconds=integration_wall,
                   integration_seconds_excluding_observations=integration_wall-observation_before_final+initial_observation_seconds,
                   wall_limit_overshoot_seconds=max(0.,integration_wall-config["max_wall_seconds"]),
                   observation_seconds=observation_seconds,final_saving_seconds=saving_seconds,
                   checkpoints=checkpoints,checkpoint_sha256=checkpoint_hashes,observations=observations,
                   arrays_sha256=arrays_hash,last_rejected_stage_error=last_rejected_error,
                   failure_detail=failure_detail,
                   peak_process_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024,
                   peak_cuda_allocated_bytes=torch.cuda.max_memory_allocated(device) if device.type == "cuda" else 0,
                   peak_cuda_reserved_bytes=torch.cuda.max_memory_reserved(device) if device.type == "cuda" else 0,
                   saved_state_fixed_matrix_policy="regenerate W20,W30 from exact NumPy seed/draw order; verify initialization_hash",
                   **engine.storage(state))
    if engine.moment:
        summary["activity"] = scalar(state.s)
    summary["total_work_seconds"] = time.monotonic()-process_start
    (out/"summary.json").write_text(json.dumps(summary,indent=2)+"\n")
    lifecycle.update(status="complete",completion_unix=time.time())
    (out/"lifecycle.json").write_text(json.dumps(lifecycle,indent=2)+"\n")
    print(json.dumps(dict(event="complete",status=status,model=config["model"],P=summary["P"],
                          time=t,training_mse=current_loss,accepted=len(steps),rejected=rejected,
                          total_work_seconds=summary["total_work_seconds"])),flush=True)
    return summary


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--config",required=True)
    result.add_argument("--out",required=True)
    return result


def main():
    args = parser().parse_args()
    try:
        summary = run(json.loads(Path(args.config).read_text()),args.out,config_path=args.config)
        if summary["status"] == "failed":
            raise SystemExit(1)
    except Exception as exc:
        failure = dict(status="failed",exception=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        output = Path(args.out)
        if output.exists() and not (output/"summary.json").exists() and not (output/"failure.json").exists():
            lifecycle_path = output/"lifecycle.json"
            if lifecycle_path.exists():
                lifecycle = json.loads(lifecycle_path.read_text())
                if lifecycle.get("status") == "integrating":
                    lifecycle.update(status="failed",integration_end_monotonic=time.monotonic(),
                                     integration_with_observations_seconds=time.monotonic()-lifecycle["integration_start_monotonic"])
                    lifecycle_path.write_text(json.dumps(lifecycle,indent=2)+"\n")
                failure["lifecycle"] = lifecycle
            (output/"failure.json").write_text(json.dumps(failure,indent=2)+"\n")
        raise


if __name__ == "__main__":
    main()
