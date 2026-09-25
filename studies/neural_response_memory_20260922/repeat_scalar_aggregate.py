"""Frozen scalar campaign reproduction, own-state restart, and branch record."""
import argparse
import json
from pathlib import Path
import time

import numpy as np

from scalar_aggregate_engine import ScalarHierarchy, initialize_coefficients, initialize_network
from scalar_aggregate_run import integrate, scalar_observer, write_json, file_hash


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--primary",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    args.out.mkdir(parents=True,exist_ok=False)
    start=time.perf_counter()
    folder=args.primary/"equal_mixed_odd_n128_seed20260920"
    config=json.loads((folder/"configuration.json").read_text())
    saved=np.load(folder/"coefficients.npz")
    inputs,labels=saved["inputs"],saved["labels"]
    params=initialize_network(128,2,depth=3,seed=20260920)
    initialization_start=time.perf_counter()
    coeff=initialize_coefficients(params,inputs,order=4)
    init_seconds=time.perf_counter()-initialization_start
    initial_check={name:dict(bitwise_equal=bool(np.array_equal(coeff[name],saved[name])),
                            max_abs_difference=float(np.max(np.abs(coeff[name]-saved[name])))) for name in coeff}
    np.savez_compressed(args.out/"recomputed_coefficients.npz",**coeff)
    # Drop the one-time neural inputs before constructing and evolving the scalar model.
    del params
    model=ScalarHierarchy(coeff,labels,order=4)
    target=np.load(folder/"order4_resolution1"/"trajectory.npz")
    obs=scalar_observer(model,labels)
    repeated,repeated_record=integrate(model.rhs,model.initial_state(),obs,target["times"],1e-9,scalar=True)
    np.savez_compressed(args.out/"repeat.npz",**repeated)
    repeat_check={name:dict(bitwise_equal=bool(np.array_equal(repeated[name],target[name],equal_nan=True)),
                           max_abs_difference=float(np.nanmax(np.abs(repeated[name]-target[name]))))
                  for name in ("times","f","loss","kernel","states","final_state")}
    restart=model.pack(model.unpack(target["checkpoint_1_0"].copy()))
    resumed,resumed_record=integrate(model.rhs,restart,obs,target["times"],1e-9,scalar=True,start=1.)
    np.savez_compressed(args.out/"restart.npz",**resumed)
    ix=target["times"]>=1.
    restart_f_error=float(np.max(np.sqrt(np.mean((resumed["f"]-target["f"][ix])**2,axis=1))))
    restart_loss_error=float(np.max(np.abs(resumed["loss"]-target["loss"][ix])))
    restart_state_error=float(np.max(np.abs(resumed["states"]-target["states"][ix])))
    summaries=[json.loads(path.read_text()) for path in sorted(args.primary.glob("*/summary.json"))]
    nonlinear_qualified=[dict(case=s["configuration"]["case"],width=s["configuration"]["width"],seed=s["configuration"]["seed"])
                         for s in summaries if max(s["dense_motion_max"])>=.1 and s["orders"]["order2"]["prediction_error"]>=.05]
    refinement_count=sum(sum(level==2 for level in s["latest_resolution"].values()) for s in summaries)
    receipt=dict(status="pass" if all(x["bitwise_equal"] for x in initial_check.values()) and
                 all(x["bitwise_equal"] for x in repeat_check.values()) and restart_f_error<=.002 and restart_loss_error<=.002 else "fail",
                 source_hashes={name:file_hash(Path(__file__).with_name(name)) for name in (
                     "repeat_scalar_aggregate.py","scalar_aggregate_engine.py","scalar_aggregate_run.py","SCALAR_AGGREGATE_PROTOCOL.md")},
                 initialization_seconds=init_seconds, initialization=initial_check,
                 repeat=repeat_check,repeat_run=repeated_record,restart_run=resumed_record,
                 restart_prediction_rms_max=restart_f_error,restart_loss_max=restart_loss_error,
                 restart_state_abs_max=restart_state_error,conditional_refinement_runs=refinement_count,
                 nonlinear_qualified_configurations=nonlinear_qualified,
                 extension_triggered=not bool(nonlinear_qualified),
                 extension_decision="not triggered: dense nonlinear movement and frozen-kernel disagreement are present" if nonlinear_qualified else "requires protocol review",
                 primary_configurations=len(summaries),total_seconds=time.perf_counter()-start)
    write_json(args.out/"check.json",receipt)
    print(json.dumps(receipt,indent=2))


if __name__=="__main__":
    main()
