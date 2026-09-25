"""Sequential GPU or CPU lane for the frozen width-2048 primary campaign."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[1]/"data/generated/neural_response_memory_20260922"
CONFIGS = tuple((case, seed) for case in ("quadrant_alternating", "equal_mixed_odd")
                for seed in (20260920,20260927))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("lane", choices=("dense", "scalar"))
    parser.add_argument("--budget", type=float, required=True)
    args=parser.parse_args()
    primary=DATA/"scalar_wide_primary01"
    primary.mkdir(exist_ok=True)
    receipt=primary/(args.lane+"_launch.json")
    if receipt.exists():
        raise FileExistsError(receipt)
    records=[]
    active=0.

    def run(command, log, threads, maximum):
        nonlocal active
        if active+maximum > args.budget:
            raise RuntimeError("insufficient reserved lane budget for next bounded job")
        env=dict(os.environ, OPENBLAS_NUM_THREADS=str(threads), OMP_NUM_THREADS=str(threads),
                 MKL_NUM_THREADS=str(threads), PYTHONDONTWRITEBYTECODE="1",
                 CUBLAS_WORKSPACE_CONFIG=":4096:8")
        started=time.perf_counter()
        with log.open("x") as stream:
            job=subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT, env=env)
        elapsed=time.perf_counter()-started
        active+=elapsed
        records.append(dict(command=command, log=str(log), seconds=elapsed, exit_code=job.returncode))
        receipt.write_text(json.dumps(dict(lane=args.lane, active_seconds=active, records=records),indent=2)+"\n")
        print(json.dumps(dict(event="job", lane=args.lane, command=command, seconds=elapsed,
                              exit_code=job.returncode)), flush=True)
        if job.returncode:
            raise RuntimeError("child job failed; retained output in " + str(log))

    for case,seed in CONFIGS:
        name=f"{case}_n2048_seed{seed}"
        target=primary/name
        target.mkdir(exist_ok=True)
        source=DATA/"scalar_wide_source01"/name
        if args.lane=="scalar" and not (source/"initialization.json").exists():
            run([sys.executable,"-B",str(HERE/"run_scalar_wide.py"),"prepare","--case",case,
                 "--seed",str(seed),"--output",str(source),"--seconds","600"],
                target/"initialization.log",4,600.)
        for level in (0,1):
            if args.lane=="dense":
                config=DATA/"scalar_wide_configs01"/(name+f"_resolution{level}.json")
                command=[sys.executable,"-B",str(HERE/"scalar_wide_dense.py"),"--config",str(config),
                         "--output",str(target/f"dense_resolution{level}")]
                maximum=900.
            else:
                command=[sys.executable,"-B",str(HERE/"run_scalar_wide.py"),"scalar","--source",str(source),
                         "--output",str(target/f"order4_resolution{level}"),"--rtol",str((1e-7,1e-9)[level]),
                         "--seconds","240"]
                maximum=240.
            run(command,target/(args.lane+f"_resolution{level}.log"),1,maximum)
    print(json.dumps(dict(event="lane_complete", lane=args.lane, active_seconds=active)),flush=True)


if __name__=="__main__":
    main()
