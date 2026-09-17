"""Frozen inputs, stage conventions and resource guards for long continuation."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time
import numpy as np

STUDY=Path(__file__).resolve().parent
ROOT=STUDY.parents[1]
GENERATED=ROOT/"data/generated/wide_network_closure_comparison"
SOURCE=GENERATED/"ARC30_20260914_v1"
PLAN=STUDY/"LONG_20260914_PLAN.md"
STAGES=tuple(40*2**k for k in range(9))
GLOBAL_WALL=7200
WORKER_WALL=2400
FAMILY_WORKER_WALL=14000
OUTPUT_CAP=14*1024**3
FREE_FLOOR=3*1024**3


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(1024**2),b""):h.update(block)
    return h.hexdigest()


def write(path,value):
    path=Path(path)
    tmp=path.with_suffix(path.suffix+".tmp")
    tmp.write_text(json.dumps(value,indent=2,allow_nan=False)+"\n")
    tmp.replace(path)


def size(path):
    total=0
    for p in Path(path).rglob("*"):
        try:
            if p.is_file():total+=p.stat().st_size
        except FileNotFoundError:pass
    return total


def load_manifest(output,require_started=True):
    output=Path(output).resolve()
    if output.parent!=GENERATED or not output.name.startswith("LONG_"):
        raise ValueError("Expected this study's separate LONG_ generated namespace")
    m=json.loads((output/"long_campaign.json").read_text())
    if sha(PLAN)!=m["plan_sha256"] or sha(output/"inputs.npz")!=m["inputs_sha256"]:
        raise ValueError("Frozen plan/input hash mismatch")
    for name,value in m.get("producer_hashes",{}).items():
        if sha(ROOT/name)!=value:raise ValueError("Frozen producer changed: "+name)
    if require_started and m["experiment_started_epoch"] is None:
        raise ValueError("Campaign scientific clock has not started")
    return m


def stage_times(target):
    if target not in STAGES:raise ValueError("Unplanned target")
    if target==40:
        return [Fraction(v) for v in json.loads((SOURCE/"inputs.json").read_text())["time_fractions"]]
    return [Fraction(target,2)+Fraction(target*j,40) for j in range(21)]


def stage_directory(output,family,name,target):
    if family not in ("network","closure") or target not in STAGES:
        raise ValueError("Invalid stage")
    if Path(name).name!=name:raise ValueError("Invalid run name")
    return Path(output).resolve()/family/name/f"stage_{target:06d}"


def guard_budget(output,worker_started_monotonic):
    m=json.loads((Path(output)/"long_campaign.json").read_text())
    if time.monotonic()-worker_started_monotonic>WORKER_WALL:
        raise TimeoutError("Per-stage worker wall cap")
    if m["experiment_started_epoch"] is None or time.time()-m["experiment_started_epoch"]>GLOBAL_WALL:
        raise TimeoutError("Global scientific wall cap")
    if size(output)>OUTPUT_CAP:raise RuntimeError("Generated-output cap")
    if shutil.disk_usage(output).free<FREE_FLOOR:raise RuntimeError("Filesystem free-space floor")


def prepare(output):
    output=Path(output).resolve()
    if output.parent!=GENERATED or not output.name.startswith("LONG_") or output.exists():
        raise ValueError("Preparation requires a fresh study-owned LONG_ output")
    old=json.loads((SOURCE/"arc30_campaign.json").read_text())
    verified=json.loads((SOURCE/"final_verification.json").read_text())
    assert old["status"]=="complete" and verified["status"]=="passed"
    assert sha(SOURCE/"arc30_comparison.json")==verified["analysis_sha256"]
    assert len(old["network_configs"])==len(old["closure_configs"])==8
    with np.load(SOURCE/"inputs.npz",allow_pickle=False) as a:
        assert a["arcs30_inputs"].shape==(16,2) and a["circle"].shape==(128,2)
        assert len(a["times"])==206 and a["times"][-1]==40
    # All already existing evidence belongs to this study; do not read other studies.
    existing={str(p.relative_to(ROOT)):sha(p) for p in GENERATED.rglob("*") if p.is_file()}
    existing.update({str(p.relative_to(ROOT)):sha(p) for p in STUDY.iterdir()
                     if p.is_file() and p.name!="README.md" and not p.name.startswith("LONG_")})
    output.mkdir()
    for name in ("inputs.npz","inputs.json"):shutil.copyfile(SOURCE/name,output/name)
    result=dict(status="prepared",created_utc=datetime.now(timezone.utc).isoformat(),source_run=str(SOURCE),
        source_campaign_sha256=sha(SOURCE/"arc30_campaign.json"),source_verification_sha256=sha(SOURCE/"final_verification.json"),
        plan_sha256=sha(PLAN),inputs_sha256=sha(output/"inputs.npz"),inputs_json_sha256=sha(output/"inputs.json"),
        network_configs=old["network_configs"],closure_configs=old["closure_configs"],stages=list(STAGES),
        panel_order="16 training inputs then128 passive-circle inputs",experiment_started_epoch=None,
        old_preservation=existing,producer_hashes={},prepare_source_sha256=sha(__file__),prepare_command=sys.argv,
        git_head=subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip(),
        git_status=subprocess.check_output(["git","status","--short","--untracked-files=no"],cwd=ROOT,text=True))
    write(output/"long_campaign.json",result)
    return dict(status="prepared",preserved_file_count=len(existing),output=str(output))


def start(output):
    m=load_manifest(output,False)
    if m["experiment_started_epoch"] is not None:raise ValueError("Clock already started")
    names=("LONG_20260914_COMMON.py","LONG_20260914_NETWORK.py","LONG_20260914_CLOSURE.py",
           "LONG_20260914_SUPERVISE.py","WIDE_GPU_20260914_NETWORK.py","GRAM_20260914_NETWORK.py",
           "ARC30_20260914_NETWORK.py","WIDE_GPU_20260914_CLOSURE.py","GRAM_20260914_CLOSURE.py",
           "ARC30_20260914_CLOSURE.py","ARC30_20260914_PREPARE.py")
    paths=[STUDY/name for name in names]+[PLAN]+list((ROOT/"code/pde").glob("observable_*.py"))
    m.update(status="running",experiment_started_epoch=time.time(),
             producer_hashes={str(p.relative_to(ROOT)):sha(p) for p in paths})
    write(Path(output)/"long_campaign.json",m)
    return dict(status="running",producer_count=len(paths))


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--start",action="store_true")
    args=parser.parse_args()
    print(json.dumps(start(args.output) if args.start else prepare(args.output),indent=2))
