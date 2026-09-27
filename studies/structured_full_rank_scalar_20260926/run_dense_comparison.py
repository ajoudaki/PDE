"""Reproducible, bounded dense-network initialization comparison."""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import time
import traceback
import numpy as np
import scipy
from circle_tasks import BY_NAME, METHODS, TASKS, directions, task_manifest
import dense_compare as dense

HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def prediction(state, inputs, block=512):
    return np.concatenate([dense.forward(state, inputs[j:j+block]).output
                           for j in range(0, len(inputs), block)])


def run_one(job):
    started = time.monotonic()
    task = BY_NAME[job["task"]]
    width, seed, method = job["width"], job["seed"], job["method"]
    key = f'{task.name}__n{width}__s{seed:02d}__{method}__dt{job["dt"]:g}'
    out = Path(job["output"])
    try:
        initial = dense.initialize(width, seed, method)
        state = initial.copy() if hasattr(initial, "copy") else dense.State(
            initial.w.copy(), initial.W.copy(), initial.c.copy())
        u, y = task.data()
        angles = 2*np.pi*np.arange(job["grid"])/job["grid"]
        queries = directions(angles)
        target = task.target(angles)
        target_rms = float(np.sqrt(np.mean(target**2)))
        records, arrays = {}, {"angles": angles, "target": target,
                               "train_angles": np.asarray(task.angles), "train_labels": y}
        history = []
        resumed_time = 0.0
        if job.get("resume_from"):
            prior_dir=Path(job["resume_from"])
            prior=json.loads((prior_dir/(key+".json")).read_text())
            if prior["status"]!="ok" or prior["fitted"]:
                raise ValueError("continuation requires a valid nonfitting base run")
            if digest(prior_dir/prior["data_file"])!=prior["data_sha256"]:
                raise ValueError("continuation source hash mismatch")
            with np.load(prior_dir/prior["data_file"]) as old:
                arrays={k:old[k].copy() for k in old.files}
            state=dense.State(arrays["final_w"].copy(),arrays["final_W"].copy(),
                              arrays["final_c"].copy())
            history=arrays["history"].tolist()
            records=prior["records"]
            resumed_time=records["final"]["time"]
            del records["final"]
        previous_loss = float(np.mean((dense.forward(state,u).output-y)**2))
        max_loss_rise = 0.0
        offset = resumed_time
        deadline = job["deadline"]

        def snapshot(label, absolute_time, current, mse):
            f = prediction(current,queries)
            error = f-target
            rms = float(np.sqrt(np.mean(error**2)))
            coarse = float(np.sqrt(np.mean(error[::2]**2)))
            grid_delta = abs(rms-coarse)
            refined_rms = None
            if grid_delta > 1e-4*target_rms:
                fine_angles=2*np.pi*np.arange(2*job["grid"])/(2*job["grid"])
                ff=prediction(current,directions(fine_angles))
                refined_rms=float(np.sqrt(np.mean((ff-task.target(fine_angles))**2)))
                arrays[label+"_circle_fine"] = ff
            fields=dense.forward(current,queries[::16])
            initial_fields=dense.forward(initial,queries[::16])
            arrays[label+"_circle"] = f
            arrays[label+"_train"] = dense.forward(current,u).output
            records[label] = {"time":float(absolute_time),"train_mse":float(mse),
                "test_rms":rms,"normalized_test_rms":rms/target_rms,
                "grid_refinement_delta":grid_delta,"refined_test_rms":refined_rms,
                "h1_motion":float(np.sqrt(np.mean((fields.h1-initial_fields.h1)**2))),
                "h2_motion":float(np.sqrt(np.mean((fields.h2-initial_fields.h2)**2))),
                "w_motion":float(np.linalg.norm(current.w-initial.w)/np.sqrt(width)),
                "middle_frobenius_motion":float(np.linalg.norm(current.W-initial.W)),
                "readout_rms":float(np.sqrt(np.mean(current.c**2)))}

        def callback(local_time,current,mse):
            nonlocal previous_loss,max_loss_rise
            absolute_time=offset+local_time
            max_loss_rise=max(max_loss_rise,float(mse)-previous_loss)
            previous_loss=float(mse)
            if mse<=1e-6 and "fit6" not in records:
                snapshot("fit6",absolute_time,current,mse)
            if mse<=1e-8 and "fit8" not in records:
                snapshot("fit8",absolute_time,current,mse)
            if len(history)==0 or absolute_time-history[-1][0]>=.99:
                history.append((absolute_time,float(mse)))
                if time.time()>deadline:
                    raise TimeoutError("campaign deadline reached")

        callback(0.,state,previous_loss)
        total_steps=0
        reached_time=resumed_time
        for endpoint in job["times"]:
            if endpoint>job["base_time"] and "fit6" in records:
                break
            offset=reached_time
            result=dense.integrate(state,u,y,time_cap=endpoint-offset,dt=job["dt"],
                target_train_mse=1e-6 if endpoint>job["base_time"] else None,
                check_interval=max(1,round(1/job["dt"])),callback=callback)
            if result.stop_reason not in ("time_cap","target"):
                raise RuntimeError("invalid integration stop: "+result.stop_reason)
            state=result.state
            total_steps+=result.steps
            local_end=float(result.history["time"][-1])
            reached_time=offset+local_end
            mse=float(np.mean((dense.forward(state,u).output-y)**2))
            # The extension can stop at a fitting threshold before its time cap.
            if abs(reached_time-endpoint)<1e-7:
                snapshot(f"time{endpoint:g}",reached_time,state,mse)
            if endpoint>job["base_time"] and "fit6" in records:
                break
        mse=float(np.mean((dense.forward(state,u).output-y)**2))
        snapshot("final",reached_time,state,mse)
        arrays["history"] = np.asarray(history)
        arrays["final_w"]=state.w
        arrays["final_c"]=state.c
        # Full final middle state permits independent continuation and readout checks.
        arrays["final_W"]=state.W
        np.savez_compressed(out/(key+".npz"),**arrays)
        rec={**job,"key":key,"status":"ok","records":records,"steps":total_steps,
             "target_rms":target_rms,"max_loss_rise":max_loss_rise,
             "fitted": "fit6" in records,"wall_seconds":time.monotonic()-started,
             "initial_middle_frobenius_sq_over_n":float(np.sum(initial.W**2)/width),
             "data_file":key+".npz","data_sha256":digest(out/(key+".npz"))}
    except Exception as exc:
        rec={**job,"key":key,"status":"failed","error":repr(exc),
             "traceback":traceback.format_exc(),"wall_seconds":time.monotonic()-started}
    (out/(key+".json")).write_text(json.dumps(rec,indent=2,allow_nan=False)+"\n")
    return {k:rec.get(k) for k in ("key","status","fitted","wall_seconds","error")}


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",required=True)
    p.add_argument("--widths",type=int,nargs="+",default=[128,256])
    p.add_argument("--seeds",type=int,nargs="+",default=list(range(12)))
    p.add_argument("--methods",nargs="+",default=list(METHODS),choices=METHODS)
    p.add_argument("--tasks",nargs="+",default=list(BY_NAME),choices=list(BY_NAME))
    p.add_argument("--dt",type=float,default=.05)
    p.add_argument("--times",type=float,nargs="+",default=[100,300,1500,3000])
    p.add_argument("--base-time",type=float,default=300)
    p.add_argument("--grid",type=int,default=4096)
    p.add_argument("--workers",type=int,default=8)
    p.add_argument("--wall-minutes",type=float,default=60)
    p.add_argument("--resume-from")
    args=p.parse_args()
    out=Path(args.output).resolve()
    out.mkdir(parents=True,exist_ok=False)
    start=time.time()
    config=vars(args)|{"output":str(out),"task_definitions":task_manifest(),
        "command":sys.argv,"cwd":os.getcwd(),"start_unix":start,
        "deadline":start+args.wall_minutes*60,"python":sys.version,
        "numpy":np.__version__,"scipy":scipy.__version__,"platform":platform.platform(),
        "cpu_count":os.cpu_count(),"git_head":subprocess.check_output(
            ["git","rev-parse","HEAD"],text=True).strip(),
        "sources":{str(q):digest(q) for q in HERE.glob("*.py")},
        "thread_env":{k:os.environ[k] for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")}}
    (out/"manifest.json").write_text(json.dumps(config,indent=2)+"\n")
    # Interleave tasks, seeds and candidates so a budget cutoff cannot retain
    # only easy tasks or one candidate. All jobs are fixed before results.
    jobs=[{"task":task,"width":width,"seed":seed,"method":method,
           "dt":args.dt,"times":args.times,"base_time":args.base_time,
           "grid":args.grid,"output":str(out),"deadline":config["deadline"],
           "resume_from":args.resume_from}
          for seed in args.seeds for task in args.tasks for width in args.widths
          for method in args.methods]
    if args.resume_from:
        source=Path(args.resume_from)
        def unfinished(job):
            key=f'{job["task"]}__n{job["width"]}__s{job["seed"]:02d}__{job["method"]}__dt{job["dt"]:g}'
            prior=json.loads((source/(key+".json")).read_text())
            return prior["status"]=="ok" and not prior["fitted"]
        jobs=[j for j in jobs if unfinished(j)]
    print(json.dumps({"jobs":len(jobs),"output":str(out)}),flush=True)
    completed=0
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures=[pool.submit(run_one,job) for job in jobs]
        with (out/"progress.jsonl").open("a") as log:
            for future in as_completed(futures):
                result=future.result()
                completed+=1
                log.write(json.dumps(result)+"\n");log.flush()
                if completed%12==0 or result["status"]!="ok":
                    print(json.dumps({"completed":completed,"total":len(jobs),
                          "elapsed":time.time()-start,"last":result}),flush=True)
    (out/"completion.json").write_text(json.dumps({"completed":completed,
            "total":len(jobs),"wall_seconds":time.time()-start})+"\n")
    (out/"artifact_hashes.json").write_text(json.dumps(
        {q.name:digest(q) for q in sorted(out.iterdir()) if q.is_file()},indent=2)+"\n")


if __name__=="__main__":
    main()
