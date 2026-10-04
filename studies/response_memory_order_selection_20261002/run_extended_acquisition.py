"""Explicit exploratory extension; original prefix failure is retained."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
import torch

import run_order_gate as base

HERE = Path(__file__).resolve().parent
START = time.monotonic()
CAP = 600
TOTAL_EPOCHS = 2560
CONT_EPOCHS = 2368


def budget():
    if time.monotonic()-START > CAP:
        raise TimeoutError("Exploratory extension process exceeded 600 seconds")


def arrays(seed, device):
    original=base.OUT/f"seed_{seed}"
    data={k:v.to(device) for k,v in torch.load(original/"data.pt",weights_only=True).items()}
    data["vy"]=data["yt"].square().mean().item()
    sq={k:v.to(device) for k,v in torch.load(original/"schedules.pt",weights_only=True).items()}
    rng=np.random.default_rng(seed+300000)
    extra=[]
    for _ in range(CONT_EPOCHS-base.CONTINUATION):
        aa=rng.permutation(1152).reshape(-1,64)
        bb=(1152+rng.permutation(128)).reshape(-1,64)
        extra.extend([*aa[:9],bb[0],*aa[9:],bb[1]])
    extra=torch.from_numpy(np.asarray(extra)).to(device)
    sq["continuation"]=torch.cat((sq["continuation"],extra))
    assert len(sq["prefix"])+len(sq["ab"])+len(sq["continuation"])==51200
    sq["nospur"]=torch.cat((sq["prefix"],sq["reference"],sq["continuation"]))
    assert len(sq["nospur"])==51200
    return data,sq


def diagnostic(p,data,nospur=False):
    if not nospur:
        return base.metrics(p,data)
    train=base.forward(p,data["x"])[0]
    test=base.forward(p,data["xt"])[0]
    ans=dict(train=(train-data["y"]).square().mean().item(),
             ood=(test-data["yt"]).square().mean().item(),
             zero=(test-data["yt"]).square().mean().item(),shortcut=0.,
             param_rms=[z.square().mean().sqrt().item() for z in p])
    if not all(np.isfinite([ans["train"],ans["ood"],*ans["param_rms"]])) or max(ans["param_rms"])>100:
        raise FloatingPointError("No-shortcut control violated finite/RMS validity gate")
    return ans


def train(p,seq,data,label,dest,offset=0,nospur=False,prior_crossing=None):
    history=[]
    first=prior_crossing
    pred=np.lib.format.open_memmap(dest/f"{label}_predictions.npy",mode="w+",dtype="float32",shape=(len(seq)//20+1,len(data["yt"])))
    row=diagnostic(p,data,nospur)
    row.update(phase_epoch=0,total_epoch=offset,total_step=20*offset,physical_time=.2*offset)
    history.append(row)
    journal=(dest/f"{label}_metrics.jsonl").open("w")
    journal.write(json.dumps(row)+"\n")
    journal.flush()
    pred[0]=base.forward(p,data["xt"])[0].cpu().numpy()
    if first is None and row["train"]<=.001:
        first=row.copy()
        torch.save([v.cpu() for v in p],dest/f"{label}_first_fit_state.pt")
    max_update=[0.,0.,0.]
    for k,idx in enumerate(seq):
        F,_=base.field(p,data["x"][idx],data["y"][idx])
        for pi,fi in zip(p,F):
            pi.add_(fi,alpha=base.ETA)
        if (k+1)%20==0:
            budget()
            epoch=(k+1)//20
            row=diagnostic(p,data,nospur)
            max_update=[max(v,.01*f.square().mean().sqrt().item()) for v,f in zip(max_update,F)]
            row.update(phase_epoch=epoch,total_epoch=offset+epoch,total_step=20*(offset+epoch),
                       physical_time=.2*(offset+epoch),sampled_max_update_rms=max_update.copy())
            history.append(row)
            journal.write(json.dumps(row)+"\n")
            if epoch%8==0:
                journal.flush()
            pred[epoch]=base.forward(p,data["xt"])[0].cpu().numpy()
            if first is None and row["train"]<=.001:
                first=row.copy()
                torch.save([v.cpu() for v in p],dest/f"{label}_first_fit_state.pt")
                base.dump(dest/f"{label}_first_fit.json",first)
                print(json.dumps(dict(stage=label,event="first_fit",total_epoch=offset+epoch,ood=row["ood"],seconds=time.monotonic()-START)),flush=True)
            if epoch%128==0 or k+1==len(seq):
                print(json.dumps(dict(stage=label,total_epoch=offset+epoch,train=row["train"],ood=row["ood"],zero=row["zero"],seconds=time.monotonic()-START)),flush=True)
    pred.flush()
    journal.close()
    base.dump(dest/f"{label}_metrics.json",history)
    torch.save([v.cpu() for v in p],dest/f"{label}_state.pt")
    return history,first


def combined_crossing(h,level):
    # Epoch grid and interpolation are both retained; no continuous hitting claim.
    previous=None
    for row in h:
        if row["train"]<=level:
            ans=row.copy()
            if previous is not None and previous["train"]>level:
                w=(np.log(previous["train"])-np.log(level))/(np.log(previous["train"])-np.log(row["train"]))
                ans["ood_logloss_interpolation"]=(1-w)*previous["ood"]+w*row["ood"]
                ans["time_bracket"]=[previous["physical_time"],row["physical_time"]]
            return ans
        previous=row
    return None


def provenance(dest,seed,mode,data):
    base.dump(dest/"environment.json",dict(seed=seed,mode=mode,device=os.environ["CUDA_VISIBLE_DEVICES"],
        gpu=torch.cuda.get_device_name(0),torch=torch.__version__,vy=data["vy"],total_time=512,
        producer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        base_sha256=hashlib.sha256((HERE/"run_order_gate.py").read_bytes()).hexdigest(),
        amendment_sha256=hashlib.sha256((HERE/"AMENDMENT_EXTENDED_ACQUISITION.md").read_bytes()).hexdigest()))


@torch.no_grad()
def run(seed,mode):
    dest=base.OUT/f"extended_seed_{seed}_{mode}"
    dest.mkdir(parents=True,exist_ok=False)
    data,sq=arrays(seed,"cuda:0")
    provenance(dest,seed,mode,data)
    torch.save({k:v.cpu() for k,v in sq.items()},dest/"extended_schedules.pt")
    if mode=="nospur":
        for key in ["x","xt","xr","x0","xc"]:
            data[key][:,3]=0
        p=base.init(512,seed,"cuda:0")
        h,first=train(p,sq["nospur"],data,"nospur",dest,nospur=True)
        joint=next((r for r in h if r["train"]<=.001 and r["ood"]<.5*data["vy"]),None)
        useful=joint is not None
        result=dict(mode=mode,first_fit=first,final=h[-1],min_heldout=min(r["ood"] for r in h),
                    joint_learnability_checkpoint=joint,useful_nonlinear_task_learned=useful,vy=data["vy"],seconds=time.monotonic()-START)
        base.dump(dest/"summary.json",result)
        print(json.dumps(result),flush=True)
        return
    narrow=base.init(64,seed,"cuda:0")
    ph,pc=train(narrow,sq["prefix"],data,"narrow_prefix",dest)
    narrow_result={}
    for order in ["ab","ba"]:
        p=base.clone(narrow)
        ih,ic=train(p,sq[order],data,f"narrow_{order}_intervention",dest,offset=128,prior_crossing=pc)
        ch,cc=train(p,sq["continuation"],data,f"narrow_{order}_continuation",dest,offset=192,prior_crossing=ic)
        narrow_result[order]=dict(final=ch[-1],first_fit=cc)
    nc=narrow_result["ba"]["final"]["ood"]-narrow_result["ab"]["final"]["ood"]
    narrow_result.update(contrast=nc,normalized_contrast=nc/data["vy"],forecast_completed_before_wide_branches=True,
                         forecast_finished_elapsed=time.monotonic()-START)
    base.dump(dest/"narrow_forecast.json",narrow_result)
    print(json.dumps(dict(event="narrow_forecast_saved",normalized_contrast=nc/data["vy"],seconds=time.monotonic()-START)),flush=True)
    wide=[v.to("cuda:0") for v in torch.load(base.OUT/f"seed_{seed}"/"wide_prefix_state.pt",weights_only=True)]
    prefix_rows=json.loads((base.OUT/f"seed_{seed}"/"wide_prefix_metrics.json").read_text())
    prefix_rows=[dict(r,total_epoch=r["epoch"],total_step=r["step"],physical_time=.2*r["epoch"]) for r in prefix_rows]
    prefix_first=next((r for r in prefix_rows if r["train"]<=.001),None)
    branches={}; histories={}; fits={}
    for order in ["ab","ba"]:
        p=base.clone(wide)
        ih,ic=train(p,sq[order],data,f"wide_{order}_intervention",dest,offset=128,prior_crossing=prefix_first)
        ch,cc=train(p,sq["continuation"],data,f"wide_{order}_continuation",dest,offset=192,prior_crossing=ic)
        branches[order]=p
        histories[order]=prefix_rows+ih[1:]+ch[1:]
        fits[order]=cc
    final={o:h[-1] for o,h in histories.items()}
    contrast=final["ba"]["ood"]-final["ab"]["ood"]
    meaningful=abs(contrast)>=.05*data["vy"]
    narrow_captures=contrast*nc>0 and abs(contrast-nc)<=max(.25*abs(contrast),.02*data["vy"])
    common_level=max(min(r["train"] for r in histories["ab"]),min(r["train"] for r in histories["ba"]))
    matched={o:combined_crossing(h,common_level) for o,h in histories.items()}
    same_times={}
    for order,fit in fits.items():
        if fit is not None:
            other="ba" if order=="ab" else "ab"
            same_times[order]=dict(fitting_branch=fit,other_at_same_time=next((r for r in histories[other] if r["total_epoch"]==fit["total_epoch"]),None))
    fa=base.forward(branches["ab"],data["xt"])[0]
    fb=base.forward(branches["ba"],data["xt"])[0]
    result=dict(mode=mode,vy=data["vy"],final=final,first_fit=fits,contrast=contrast,normalized_contrast=contrast/data["vy"],
                endpoint_function_rms=(fa-fb).square().mean().sqrt().item(),meaningful_endpoint=meaningful,narrow_forecast=nc,
                narrow_captures=narrow_captures,common_loss=common_level,common_loss_crossings=matched,
                first_fit_same_time_pairs=same_times,seconds=time.monotonic()-START)
    if all(fits.values()):
        mc=fits["ba"]["ood"]-fits["ab"]["ood"]
        paired_contrasts={o:(pair["other_at_same_time"]["ood"]-pair["fitting_branch"]["ood"] if o=="ab" else
                             pair["fitting_branch"]["ood"]-pair["other_at_same_time"]["ood"])
                          for o,pair in same_times.items() if pair["other_at_same_time"] is not None}
        result.update(first_fit_contrast=mc,first_fit_normalized_contrast=mc/data["vy"],
                      paired_same_time_fit_contrasts=paired_contrasts,
                      matched_fit_meaningful_same_sign=contrast*mc>0 and abs(mc)>=.05*data["vy"] and
                      len(paired_contrasts)==2 and all(contrast*c>0 for c in paired_contrasts.values()))
    else:
        result["matched_fit_meaningful_same_sign"]=False
    result["decision"]=("STOP_SMALL_PERSISTENT_EFFECT" if not meaningful else
                        "STOP_ORDINARY_NARROW_CAPTURE" if narrow_captures else
                        "INCONCLUSIVE_MATCHED_FITTING" if not result["matched_fit_meaningful_same_sign"] else
                        "REPORT_PERSISTENT_UNEXPLAINED_ACQUISITION")
    if meaningful:
        refits={o:base.ridge_refit(p,data) for o,p in branches.items()}
        result.update(refit_risks=refits,refit_normalized_contrast=(refits["ba"]-refits["ab"])/data["vy"],
                      refit_gap_removed=abs(refits["ba"]-refits["ab"])<.02*data["vy"])
    base.dump(dest/"summary.json",result)
    print(json.dumps(result),flush=True)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--seed",type=int,default=101)
    parser.add_argument("--mode",choices=["nospur","target"],required=True)
    args=parser.parse_args()
    expected="1" if args.mode=="nospur" else "0"
    assert os.environ.get("CUDA_VISIBLE_DEVICES")==expected
    try:
        run(args.seed,args.mode)
    except Exception as exc:
        dest=base.OUT/f"extended_seed_{args.seed}_{args.mode}"
        dest.mkdir(parents=True,exist_ok=True)
        base.dump(dest/"failure.json",dict(type=type(exc).__name__,message=str(exc),seconds=time.monotonic()-START))
        raise


if __name__=="__main__":
    main()
