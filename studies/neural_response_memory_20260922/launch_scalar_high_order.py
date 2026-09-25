"""Sequential scalar integration lane; fixed seeds/orders and per-run limits."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
DATA=HERE.parents[1]/"data/generated/neural_response_memory_20260922"


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed",type=int,choices=(20260920,20260927),required=True)
    parser.add_argument("--reproduction",action="store_true")
    args=parser.parse_args()
    suffix="_reproduction01" if args.reproduction else "01"
    source=DATA/("scalar_high_order_training"+suffix)/("seed"+str(args.seed))
    root=DATA/("scalar_high_order_reproduction01" if args.reproduction else "scalar_high_order_primary01")/("seed"+str(args.seed))
    root.mkdir(parents=True,exist_ok=True)
    records=[]; env=os.environ.copy()
    env.update(OPENBLAS_NUM_THREADS="1",OMP_NUM_THREADS="1",MKL_NUM_THREADS="1",PYTHONDONTWRITEBYTECODE="1")
    for order in (5,6):
        for level,rtol in ((1,1e-9),) if args.reproduction else ((0,1e-7),(1,1e-9)):
            name="order"+str(order)+( "" if args.reproduction else "_resolution"+str(level))
            target=root/name
            command=[sys.executable,"-B",str(HERE/"run_scalar_high_order.py"),"integrate",
                "--source",str(source),"--output",str(target),"--order",str(order),
                "--rtol",str(rtol),"--seconds","600"]
            started=time.perf_counter()
            with (root/(name+".log")).open("x") as stream:
                process=subprocess.run(command,env=env,stdout=stream,stderr=subprocess.STDOUT)
            record=dict(command=command,seconds=time.perf_counter()-started,exit_code=process.returncode)
            records.append(record)
            (root/"launch.json").write_text(json.dumps(dict(records=records,active_seconds=sum(r["seconds"] for r in records)),indent=2)+"\n")
            print(json.dumps(record),flush=True)
            if process.returncode:
                raise SystemExit(process.returncode)


if __name__=="__main__":
    main()
