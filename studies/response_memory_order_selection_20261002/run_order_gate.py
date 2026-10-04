"""Bounded raw-SGD order-selection gate; see PROTOCOL.md before running."""
import argparse
import copy
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import time

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/response_memory_order_selection_20261002"
STUDY = Path(__file__).resolve().parent
D, M, B, ETA = 16, 1280, 64, 0.01
PREFIX, INTERVENTION, CONTINUATION = 128, 64, 256
START = time.monotonic()
DEADLINE = 600
torch.set_num_threads(2)
torch.backends.cuda.matmul.allow_tf32 = False
torch.backends.cudnn.allow_tf32 = False


def dump(path, obj):
    path.write_text(json.dumps(obj, indent=2, allow_nan=False) + "\n")


def check_budget():
    if time.monotonic() - START > DEADLINE:
        raise TimeoutError("Frozen 600-second per-seed process cap reached")


def init(n, seed, device, dtype=torch.float32):
    g = torch.Generator(device="cpu").manual_seed(seed)
    return [torch.randn(n, D, generator=g, dtype=dtype).to(device),
            (torch.randn(n, n, generator=g, dtype=dtype) / math.sqrt(n)).to(device),
            torch.zeros(n, device=device, dtype=dtype)]


def clone(p):
    return [v.clone() for v in p]


def forward(p, x):
    w1, w2, w = p
    h1 = torch.tanh(x @ w1.T / math.sqrt(D))
    h2 = torch.tanh(h1 @ w2.T)
    return h2 @ w / len(w), h1, h2


def field(p, x, y, tangents=()):
    w1, w2, w = p
    n = len(w)
    f, h1, h2 = forward(p, x)
    r = f - y
    g1, g2 = 1 - h1.square(), 1 - h2.square()
    delta2 = g2 * w
    carrier1 = delta2 @ w2
    delta1 = g1 * carrier1
    rr = r[:, None]
    a2 = rr * delta2
    F = [-2 * (rr * delta1).T @ x / (len(x) * math.sqrt(D)),
         -2 * a2.T @ h1 / (n * len(x)),
         -2 * (rr * h2).mean(0)]
    jvps = []
    for v1, v2, vw in tangents:
        dh1 = g1 * (x @ v1.T / math.sqrt(D))
        dh2 = g2 * (dh1 @ w2.T + h1 @ v2.T)
        dr = (dh2 @ w + h2 @ vw) / n
        dd2 = g2 * vw - 2 * h2 * dh2 * w
        dd1 = g1 * (dd2 @ w2 + delta2 @ v2) - 2 * h1 * dh1 * carrier1
        da2 = dr[:, None] * delta2 + rr * dd2
        jvps.append([
            -2 * (dr[:, None] * delta1 + rr * dd1).T @ x / (len(x) * math.sqrt(D)),
            -2 * (da2.T @ h1 + a2.T @ dh1) / (n * len(x)),
            -2 * (dr[:, None] * h2 + rr * dh2).mean(0),
        ])
    return F, jvps


def predict_tangent(p, v, x):
    w1, w2, w = p
    v1, v2, vw = v
    f, h1, h2 = forward(p, x)
    dh1 = (1-h1.square()) * (x @ v1.T / math.sqrt(D))
    dh2 = (1-h2.square()) * (dh1 @ w2.T + h1 @ v2.T)
    return f + (dh2 @ w + h2 @ vw) / len(w)


def make_data(seed, device):
    rng = np.random.default_rng(seed + 100000)
    def examples(count, mode):
        x = rng.normal(size=(count, D)).astype("float32")
        y = np.tanh(x[:, 0] * x[:, 1] * x[:, 2])
        if mode == "train":
            e = np.r_[np.ones(1152), -np.ones(128)]
            x[:, 3] = e * y + .1 * rng.normal(size=count)
        elif mode == "balanced":
            e = np.r_[np.ones(count//2), -np.ones(count//2)]
            x[:, 3] = e * y + .1 * rng.normal(size=count)
        else:
            zprime = rng.normal(size=(count, 3))
            x[:, 3] = np.tanh(np.prod(zprime, axis=1)) + .1 * rng.normal(size=count)
        return torch.from_numpy(x).to(device), torch.from_numpy(y).to(device)
    x, y = examples(M, "train")
    xt, yt = examples(8192, "ood")
    xr = xt.clone()
    zp = rng.normal(size=(len(xt), 3))
    xr[:, 3] = torch.tensor(np.tanh(np.prod(zp, axis=1)) + .1 * rng.normal(size=len(xt)), device=device, dtype=xt.dtype)
    x0 = xt.clone()
    x0[:, 3] = 0
    xc, yc = examples(1024, "balanced")
    return dict(x=x, y=y, xt=xt, yt=yt, xr=xr, x0=x0, xc=xc, yc=yc,
                vy=yt.square().mean().item())


def schedules(seed, device):
    rng = np.random.default_rng(seed + 200000)
    def groups():
        return rng.permutation(1152).reshape(-1, B), (1152+rng.permutation(128)).reshape(-1, B)
    def mixed(epochs):
        seq = []
        for _ in range(epochs):
            a, b = groups()
            seq.extend([*a[:9], b[0], *a[9:], b[1]])
        return np.asarray(seq)
    prefix = mixed(PREFIX)
    aa, bb = [], []
    for _ in range(INTERVENTION):
        a, b = groups()
        aa.extend(a)
        bb.extend(b)
    ab, ba = np.asarray(aa+bb), np.asarray(bb+aa)
    reference = mixed(INTERVENTION)
    continuation = mixed(CONTINUATION)
    ans = {k: torch.from_numpy(v).to(device) for k,v in
           dict(prefix=prefix, ab=ab, ba=ba, reference=reference, continuation=continuation).items()}
    assert np.array_equal(np.bincount(ab.ravel(), minlength=M), np.full(M, INTERVENTION))
    assert np.array_equal(np.bincount(ba.ravel(), minlength=M), np.full(M, INTERVENTION))
    return ans


def metrics(p, data, initial=None):
    f, h1, h2 = forward(p, data["x"])
    ft, _, _ = forward(p, data["xt"])
    fr, _, _ = forward(p, data["xr"])
    f0, _, _ = forward(p, data["x0"])
    r = dict(train=((f-data["y"])**2).mean().item(),
             ood=((ft-data["yt"])**2).mean().item(),
             zero=((f0-data["yt"])**2).mean().item(),
             shortcut=((ft-fr)**2).mean().item(),
             param_rms=[v.square().mean().sqrt().item() for v in p])
    if initial is not None:
        _, hi1, hi2 = forward(initial, data["x"])
        r["feature_motion"] = [(h1-hi1).square().mean().sqrt().item(), (h2-hi2).square().mean().sqrt().item()]
    if not all(math.isfinite(z) for z in [r["train"],r["ood"],r["zero"],r["shortcut"],*r["param_rms"]]):
        raise FloatingPointError("Nonfinite state or metric")
    if max(r["param_rms"]) > 100:
        raise FloatingPointError("Parameter RMS exceeded frozen validity cap")
    return r


def train(p, seq, data, label, dest, initial=None):
    history = []
    max_update = [0.,0.,0.]
    for k, idx in enumerate(seq):
        F, _ = field(p, data["x"][idx], data["y"][idx])
        for j,(param, f) in enumerate(zip(p,F)):
            param.add_(f, alpha=ETA)
        if (k+1) % 20 == 0:
            check_budget()
            for j,f in enumerate(F):
                max_update[j] = max(max_update[j], ETA*f.square().mean().sqrt().item())
            row = metrics(p, data, initial)
            row.update(epoch=(k+1)//20, step=k+1, physical_time=ETA*(k+1), max_update_rms=max_update.copy())
            history.append(row)
            if (k+1) % 640 == 0 or k+1 == len(seq):
                print(json.dumps(dict(stage=label, epoch=row["epoch"], train=row["train"], ood=row["ood"], seconds=time.monotonic()-START)), flush=True)
    dump(dest/f"{label}_metrics.json",history)
    torch.save([v.cpu() for v in p], dest/f"{label}_state.pt")
    return history


def first_order_forecast(p, seqs, data, dest):
    p=clone(p)
    vs=[[torch.zeros_like(z) for z in p] for _ in range(2)]
    ref=torch.cat((seqs["reference"],seqs["continuation"]))
    targets=[seqs["ab"],seqs["ba"]]
    for k,idx in enumerate(ref):
        F, Js = field(p,data["x"][idx],data["y"][idx],vs)
        Fs = [field(p,data["x"][sq[k]],data["y"][sq[k]])[0] for sq in targets] if k<len(targets[0]) else [F,F]
        for v,J,Ftarget in zip(vs,Js,Fs):
            for vi,ji,ft,ff in zip(v,J,Ftarget,F):
                vi.add_(ji,alpha=ETA)
                if k<len(targets[0]):
                    vi.add_(ft-ff,alpha=ETA)
        for pi,fi in zip(p,F):
            pi.add_(fi,alpha=ETA)
        if (k+1)%640==0:
            check_budget()
            print(json.dumps(dict(stage="first_order_reference",epoch=(k+1)//20,seconds=time.monotonic()-START)),flush=True)
    preds=[predict_tangent(p,v,data["xt"]) for v in vs]
    risks=[(f-data["yt"]).square().mean().item() for f in preds]
    ans=dict(risks=risks,contrast=risks[1]-risks[0],normalized_contrast=(risks[1]-risks[0])/data["vy"],
             tangent_rms=[[t.square().mean().sqrt().item() for t in v] for v in vs],
             reference=metrics(p,data),forecast_completed_before_wide_branches=True)
    dump(dest/"first_order_forecast.json",ans)
    torch.save(dict(predictions=[f.cpu() for f in preds],reference=[z.cpu() for z in p],tangents=[[z.cpu() for z in v] for v in vs]),dest/"first_order_forecast.pt")
    return ans


def derivative_check():
    torch.manual_seed(42)
    p=init(8,43,"cpu",torch.float64)
    p[2]=torch.randn(8,dtype=torch.float64)
    x=torch.randn(7,D,dtype=torch.float64)
    y=torch.randn(7,dtype=torch.float64)
    v=[torch.randn_like(z) for z in p]
    F,J=field(p,x,y,[v])
    pp=[z.clone().requires_grad_() for z in p]
    loss=(forward(pp,x)[0]-y).square().mean()
    grad=torch.autograd.grad(loss,pp)
    expected=[-8*grad[0],-grad[1],-8*grad[2]]
    gradient_error=max((a-b).norm().item()/max(1.,b.norm().item()) for a,b in zip(F,expected))
    e=1e-6
    fp=field([z+e*t for z,t in zip(p,v)],x,y)[0]
    fm=field([z-e*t for z,t in zip(p,v)],x,y)[0]
    jvp_error=max((a-(b-c)/(2*e)).norm().item()/max(1.,a.norm().item()) for a,b,c in zip(J[0],fp,fm))
    assert gradient_error<1e-5 and jvp_error<1e-4,(gradient_error,jvp_error)
    return dict(gradient_relative_error=gradient_error,jvp_relative_error=jvp_error)


def ridge_refit(p,data):
    _,_,hc=forward(p,data["xc"])
    _,_,ht=forward(p,data["xt"])
    hc,ht=hc.double()/math.sqrt(len(p[2])),ht.double()/math.sqrt(len(p[2]))
    n=len(p[2]); count=len(hc)
    gram=hc.T@hc/count+0.001*torch.eye(n,device=hc.device,dtype=hc.dtype)
    beta=torch.linalg.solve(gram,hc.T@data["yc"].double()/count)
    return ((ht@beta-data["yt"].double())**2).mean().item()


def crossing(history,level):
    previous=None
    for row in history:
        if row["train"]<=level:
            ans=dict(epoch=row["epoch"],train=row["train"],ood=row["ood"])
            if previous is not None and previous["train"]>level:
                weight=(math.log(previous["train"])-math.log(level))/(math.log(previous["train"])-math.log(row["train"]))
                ans["ood_logloss_interpolation"]=(1-weight)*previous["ood"]+weight*row["ood"]
                ans["epoch_bracket"]=[previous["epoch"],row["epoch"]]
            return ans
        previous=row
    return None


@torch.no_grad()
def run(seed,device):
    dest=OUT/f"seed_{seed}"
    dest.mkdir(parents=True,exist_ok=False)
    data=make_data(seed,device)
    seqs=schedules(seed,device)
    env=dict(seed=seed,torch=torch.__version__,numpy=np.__version__,python=platform.python_version(),device=device,
             gpu=torch.cuda.get_device_name(0),eta=ETA,batch=B,widths=[512,64],prefix_epochs=PREFIX,
             intervention_epochs=INTERVENTION,continuation_epochs=CONTINUATION,label_variance=data["vy"],
             source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             protocol_sha256=hashlib.sha256((STUDY/"PROTOCOL.md").read_bytes()).hexdigest())
    dump(dest/"environment.json",env)
    torch.save({k:v.cpu() for k,v in data.items() if isinstance(v,torch.Tensor)},dest/"data.pt")
    torch.save({k:v.cpu() for k,v in seqs.items()},dest/"schedules.pt")
    wide=init(512,seed,device); initial=clone(wide)
    prefix=train(wide,seqs["prefix"],data,"wide_prefix",dest,initial)
    gate=prefix[-1]
    gate_pass=gate["shortcut"]/data["vy"]>=0.1 and gate["zero"]/data["vy"]<0.95 and max(gate["feature_motion"])>=0.05
    result=dict(seed=seed,gate=gate,gate_pass=gate_pass,vy=data["vy"])
    if not gate_pass:
        result.update(decision="INCONCLUSIVE_FEATURE_COMPETITION_GATE",seconds=time.monotonic()-START)
        dump(dest/"summary.json",result)
        print(json.dumps(result),flush=True)
        return result
    narrow=init(64,seed,device)
    train(narrow,seqs["prefix"],data,"narrow_prefix",dest)
    narrow_risks=[]
    for name in ["ab","ba"]:
        branch=clone(narrow)
        train(branch,seqs[name],data,f"narrow_{name}_intervention",dest)
        h=train(branch,seqs["continuation"],data,f"narrow_{name}_continuation",dest)
        narrow_risks.append(h[-1]["ood"])
    narrow_forecast=dict(risks=narrow_risks,contrast=narrow_risks[1]-narrow_risks[0],forecast_completed_before_wide_branches=True)
    dump(dest/"narrow_forecast.json",narrow_forecast)
    linear=first_order_forecast(wide,seqs,data,dest)
    branches=[]; histories=[]
    for name in ["ab","ba"]:
        branch=clone(wide)
        train(branch,seqs[name],data,f"wide_{name}_intervention",dest,wide)
        h=train(branch,seqs["continuation"],data,f"wide_{name}_continuation",dest,wide)
        branches.append(branch); histories.append(h)
        torch.save(forward(branch,data["xt"])[0].cpu(),dest/f"wide_{name}_test_predictions.pt")
    contrast=histories[1][-1]["ood"]-histories[0][-1]["ood"]
    threshold=max(.25*abs(contrast),.02*data["vy"])
    rivals={"narrow":narrow_forecast["contrast"],"first_order":linear["contrast"]}
    captured={k: bool(v*contrast>0 and abs(v-contrast)<=threshold) for k,v in rivals.items()}
    meaningful=abs(contrast)/data["vy"]>=.05
    level=max(min(h["train"] for h in histories[0]),min(h["train"] for h in histories[1]))
    result.update(contrast=contrast,normalized_contrast=contrast/data["vy"],meaningful=meaningful,rival_forecasts=rivals,
                  rival_captures=captured,final_metrics=[h[-1] for h in histories],
                  matched_001=[crossing(h,.001) for h in histories],
                  common_loss_level=level,common_loss_crossings=[crossing(h,level) for h in histories])
    if meaningful:
        rr=[ridge_refit(p,data) for p in branches]
        result.update(refit_risks=rr,refit_normalized_contrast=(rr[1]-rr[0])/data["vy"],
                      refit_gap_removed=abs(rr[1]-rr[0])/data["vy"]<.02)
    decision="STOP_SMALL_PERSISTENT_EFFECT" if not meaningful else (
        "STOP_ORDINARY_RIVAL_CAPTURES" if any(captured.values()) else "REPORT_PERSISTENT_UNEXPLAINED_CONTRAST")
    result.update(decision=decision,seconds=time.monotonic()-START)
    dump(dest/"summary.json",result)
    print(json.dumps(result),flush=True)
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--seed",type=int,default=101)
    parser.add_argument("--check-only",action="store_true")
    args=parser.parse_args()
    OUT.mkdir(parents=True,exist_ok=True)
    checks=derivative_check()
    dump(OUT/"derivative_checks.json",checks)
    print(json.dumps(checks),flush=True)
    if args.check_only:
        return
    assert os.environ.get("CUDA_VISIBLE_DEVICES")=="0","GPU0 allocation must be explicit"
    try:
        run(args.seed,"cuda:0")
    except Exception as exc:
        dest=OUT/f"seed_{args.seed}"
        dest.mkdir(parents=True,exist_ok=True)
        dump(dest/"failure.json",dict(type=type(exc).__name__,message=str(exc),seconds=time.monotonic()-START))
        raise


if __name__=="__main__":
    main()
