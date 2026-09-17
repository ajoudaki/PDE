"""Bounded common-horizon supervisor; two GPUs and two closure workers."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
from LONG_20260914_COMMON import (
    ROOT,STUDY,STAGES,WORKER_WALL,FAMILY_WORKER_WALL,
    load_manifest,guard_budget,write,sha)

GPU_PYTHON="/home/amir/miniconda3/bin/python"
CPU_PYTHON="/usr/bin/python"


def supervise(output):
    output=output.resolve()
    manifest=load_manifest(output)
    if (output/"supervisor.json").exists():raise FileExistsError("Prior supervisor result exists")
    active={}
    finished=[]
    family_spent={"network":0.,"closure":0.}
    completed_stages=[]
    termination=None
    source_hash=sha(__file__)

    def progress(target,pending):
        write(output/"supervisor_progress.json",dict(target=target,
            active=[dict(family=v["family"],name=v["name"],lane=lane,elapsed_seconds=time.monotonic()-v["launch"])
                    for lane,v in active.items()],
            pending=[dict(family=f,name=c.get("name",c.get("id"))) for f,c in pending],
            completed_stages=completed_stages,family_worker_seconds=family_spent,
            scientific_elapsed_seconds=time.time()-manifest["experiment_started_epoch"],
            finished_worker_count=len(finished)))

    def finish_active(killed=False):
        for lane,v in list(active.items()):
            proc=v["proc"]
            if killed and proc.poll() is None:
                proc.terminate()
                try:proc.wait(timeout=5)
                except subprocess.TimeoutExpired:proc.kill();proc.wait()
            if proc.poll() is None:continue
            elapsed=time.monotonic()-v["launch"]
            family_spent[v["family"]]+=elapsed
            v["log"].close()
            row=dict(family=v["family"],name=v["name"],target=v["target"],lane=lane,
                exit_code=proc.returncode,wall_seconds=elapsed,command=v["command"],budget_killed=killed)
            finished.append(row)
            print(json.dumps(row),flush=True)
            del active[lane]

    try:
        for target in STAGES:
            pending=[("network",c) for c in sorted(manifest["network_configs"],
                key=lambda c:-(c["width"]**2/c["step"]*(3 if c["dtype"]=="float64" else 1)))]
            pending += [("closure",c) for c in sorted(manifest["closure_configs"],
                key=lambda c:-(c["population_nodes"]*c["order"]**2*(2 if "halfstep" in c["id"] else 1)))]
            stage_start=time.monotonic()
            stage_finished_offset=len(finished)
            print(json.dumps(dict(event="stage_start",target=target)),flush=True)
            last_progress=0.
            while pending or active:
                finish_active()
                stage_rows=finished[stage_finished_offset:]
                if any(r["exit_code"]!=0 for r in stage_rows):
                    termination="worker_failure";break
                if any(time.monotonic()-v["launch"]>WORKER_WALL for v in active.values()):
                    termination="worker_wall_limit";break
                try:
                    guard_budget(output,time.monotonic())
                except (TimeoutError,RuntimeError) as exc:
                    termination="resource_limit: "+str(exc);break
                if any(family_spent[f]+sum(time.monotonic()-v["launch"] for v in active.values() if v["family"]==f)
                       >FAMILY_WORKER_WALL for f in family_spent):
                    termination="family_worker_limit";break
                for lane,family,gpu in (("gpu1","network",1),("gpu0","network",0),
                                        ("cpu0","closure",None),("cpu1","closure",None)):
                    if lane in active:continue
                    index=next((i for i,(f,c) in enumerate(pending) if f==family),None)
                    if index is None:continue
                    _,config=pending.pop(index)
                    name=config.get("name",config.get("id"))
                    parent=output/family/name;parent.mkdir(parents=True,exist_ok=True)
                    log= (parent/f"stage_{target:06d}.worker.log").open("x")
                    env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1",OPENBLAS_NUM_THREADS="1",
                             OMP_NUM_THREADS="4" if family=="network" else "1",
                             MKL_NUM_THREADS="4" if family=="network" else "1")
                    if gpu is not None:env["CUDA_VISIBLE_DEVICES"]=str(gpu)
                    command=[GPU_PYTHON if family=="network" else CPU_PYTHON,"-B",
                             str(STUDY/f"LONG_20260914_{family.upper()}.py"),
                             "--output",str(output),"--run-id",name,"--target",str(target)]
                    proc=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,cwd=ROOT,env=env)
                    active[lane]=dict(proc=proc,family=family,name=name,target=target,launch=time.monotonic(),
                                      log=log,command=command)
                if time.monotonic()-last_progress>5:
                    progress(target,pending);last_progress=time.monotonic()
                time.sleep(.5)
            if termination:
                finish_active(True);progress(target,pending);break
            finish_active()
            from LONG_20260914_ANALYSIS import analyse_stage
            analysis=analyse_stage(output,target)
            path=output/f"stage_analysis_{target:06d}.json"
            if path.exists():raise FileExistsError("Stage analysis already exists")
            write(path,analysis)
            stage_row=dict(target=target,worker_count=len(finished)-stage_finished_offset,
                wall_seconds=time.monotonic()-stage_start,analysis_sha256=sha(path),
                stop_recommended=analysis.get("stop_recommended"))
            completed_stages.append(stage_row)
            progress(target,[])
            print(json.dumps(dict(event="stage_complete",**stage_row)),flush=True)
            if analysis.get("stop_recommended"):
                termination=analysis["stop_recommended"];break
        if termination is None:termination="horizon_limit"
    except BaseException as exc:
        termination=f"exception: {type(exc).__name__}: {exc}"
        finish_active(True)
        raise
    finally:
        result=dict(status="settled" if termination=="settled" else "stopped",reason=termination,
            completed_stages=completed_stages,last_complete_target=completed_stages[-1]["target"] if completed_stages else None,
            family_worker_seconds=family_spent,workers=finished,source_sha256=source_hash,command=sys.argv,
            scientific_elapsed_seconds=time.time()-manifest["experiment_started_epoch"],completed_epoch=time.time())
        write(output/"supervisor.json",result)
        current=json.loads((output/"long_campaign.json").read_text())
        current.update(status=result["status"],stop_reason=termination,last_complete_target=result["last_complete_target"],
                       scientific_completion_recorded_epoch=time.time(),supervisor_sha256=sha(output/"supervisor.json"))
        write(output/"long_campaign.json",current)
        print(json.dumps(dict(event="campaign_stop",status=result["status"],reason=termination,
                             target=result["last_complete_target"])),flush=True)
    return 0 if termination in ("settled","horizon_limit") else 1


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",required=True,type=Path)
    args=parser.parse_args()
    signal.signal(signal.SIGTERM,lambda signum,frame: (_ for _ in ()).throw(KeyboardInterrupt()))
    raise SystemExit(supervise(args.output))
