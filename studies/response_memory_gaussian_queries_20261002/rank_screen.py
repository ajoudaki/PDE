#!/usr/bin/env python3
"""Fresh canonical raw-Legendre producer; see RANK_PROTOCOL.md before use."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import sys
import time

import numpy as np
import torch


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/generated/response_memory_gaussian_queries_20261002/rank_screen01"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def data(name):
    if name == "circle":
        a = np.array([.07, .38, .84, 1.31, 1.89, 2.42, 2.93, 3.57])
        x = math.sqrt(2) * np.stack([np.cos(a), np.sin(a)], axis=1)
        y = (-1.) ** np.arange(8)
    else:
        x = np.random.default_rng(8841).standard_normal((16, 8))
        x *= math.sqrt(8) / np.linalg.norm(x, axis=1)[:, None]
        y = np.sign(x[:, 0] * x[:, 1] * x[:, 2])
    return x, y


class Closure:
    def __init__(self, x, y, n, q, device, dtype=torch.float32, seed=1771):
        self.n, self.q = n, q
        self.x = torch.as_tensor(x, device=device, dtype=dtype)
        self.y = torch.as_tensor(y, device=device, dtype=dtype)
        self.m, self.d = self.x.shape
        self.xs = self.x / math.sqrt(self.d)
        # CPU generator gives paired initialization independently of GPU index.
        gen = torch.Generator(device="cpu").manual_seed(seed)
        W1 = torch.randn((n, self.d), generator=gen, dtype=dtype).to(device)
        self.W0 = (torch.randn((n, n), generator=gen, dtype=dtype)
                   / math.sqrt(n)).to(device)
        w = torch.zeros(n, dtype=dtype, device=device)
        H = torch.zeros((q, self.m, n), dtype=dtype, device=device)
        H[0] = torch.tanh(self.xs @ W1.T)
        D = torch.zeros_like(H)
        tau = torch.ones((), dtype=dtype, device=device)
        self.initial = [W1, w, H, D, tau]
        self.mode_weights = (2 * torch.arange(q, device=device, dtype=dtype) + 1)
        self.flat_weights = self.mode_weights.repeat_interleave(self.m)
        self.dilation = torch.zeros((q, q), device=device, dtype=dtype)
        for k in range(q):
            self.dilation[k, k] = k
            for j in range(k):
                self.dilation[k, j] = 2 * j + 1

    def reconstruct(self, state):
        _, _, H, D, tau = state
        hf, df = H.flatten(0, 1), D.flatten(0, 1)
        return self.W0 - (2 / (self.n * self.m * tau)) * (df.T * self.flat_weights) @ hf

    def evaluate(self, state):
        W1, w, H, D, tau = state
        hf, df = H.flatten(0, 1), D.flatten(0, 1)
        c = 2 / (self.n * self.m * tau)
        h1 = torch.tanh(self.xs @ W1.T)
        z2 = h1 @ self.W0.T - c * ((h1 @ hf.T) * self.flat_weights) @ df
        h2 = torch.tanh(z2)
        f = h2 @ w / self.n
        r = f - self.y
        rho = r.square().mean().sqrt()
        delta2 = (1 - h2.square()) * w
        delta1 = (1 - h1.square()) * (
            delta2 @ self.W0 - c * ((delta2 @ df.T) * self.flat_weights) @ hf)
        return dict(h1=h1, h2=h2, f=f, r=r, rho=rho, delta1=delta1, delta2=delta2)

    def rhs(self, state, ev=None):
        if ev is None:
            ev = self.evaluate(state)
        _, _, H, D, tau = state
        r, rho = ev["r"], ev["rho"]
        dW1 = -2 / self.m * (ev["delta1"].T * r) @ self.xs
        dw = -2 / self.m * (r @ ev["h2"])
        dH = rho * ev["h1"][None] - (rho / tau) * torch.einsum("kj,jmn->kmn", self.dilation, H)
        dD = (r[:, None] * ev["delta2"])[None] - (rho / tau) * torch.einsum("kj,jmn->kmn", self.dilation, D)
        return [dW1, dw, dH, dD, rho]


class OnlineSpan:
    def __init__(self, n, m, tol, device):
        self.n, self.m, self.tol = n, m, tol
        self.Q = torch.empty((n, n), device=device)
        self.rank = 0
        self.variation = np.zeros(m)
        self.prev = None
        self.records = []
        self.max_action = 0.
        self.max_residual = 0.
        self.max_query = 0.
        self.work_rank_sum = 0
        self.acceptance = []

    def observe(self, x, W0, transpose, t):
        if self.prev is not None:
            self.variation += ((x - self.prev).square().mean(1).sqrt()).cpu().numpy()
        self.prev = x.clone()
        R = x.clone()
        if self.rank:
            B = self.Q[:, :self.rank]
            R -= (R @ B) @ B.T
            R -= (R @ B) @ B.T
        post = torch.empty_like(R)
        innovations = []
        for a in range(self.m):
            norm = torch.linalg.vector_norm(R[a])
            rms = float(norm) / math.sqrt(self.n)
            innovations.append(rms)
            self.work_rank_sum += self.rank
            if rms > self.tol and self.rank < self.n:
                v = R[a] / norm
                # Reorthogonalize the appended direction to suppress drift.
                if self.rank:
                    B = self.Q[:, :self.rank]
                    v -= B @ (B.T @ v)
                    v -= B @ (B.T @ v)
                    v /= torch.linalg.vector_norm(v)
                self.Q[:, self.rank] = v
                self.rank += 1
                self.acceptance.append([t, a, rms])
                post[a].zero_()
                if a + 1 < self.m:
                    tail = R[a + 1:]
                    tail -= (tail @ v)[:, None] * v
                    tail -= (tail @ v)[:, None] * v
            else:
                post[a] = R[a]
        residuals = post.square().mean(1).sqrt()
        action = post @ (W0 if transpose else W0.T)
        errors = action.square().mean(1).sqrt()
        query_rms = x.square().mean(1).sqrt()
        mxr, mxe, mxq = float(residuals.max()), float(errors.max()), float(query_rms.max())
        self.max_action = max(self.max_action, mxe)
        self.max_residual = max(self.max_residual, mxr)
        self.max_query = max(self.max_query, mxq)
        self.records.append(dict(t=t, rank=self.rank, innovation_rms=innovations,
                                 retained_residual_rms=residuals.cpu().tolist(),
                                 action_error_rms=errors.cpu().tolist(),
                                 query_rms=query_rms.cpu().tolist(),
                                 variation_sum=float(self.variation.sum())))

    def finish(self, path):
        B = self.Q[:, :self.rank]
        if self.rank:
            gram = B.T @ B
            gram -= torch.eye(self.rank, device=B.device)
            orth = float(gram.abs().max())
        else:
            orth = 0.
        np.save(path.with_suffix(".basis.npy"), B.cpu().numpy())
        path.with_suffix(".json").write_text(json.dumps(self.records))
        return dict(rank=self.rank, max_action_error_rms=self.max_action,
                    max_retained_residual_rms=self.max_residual, max_query_rms=self.max_query,
                    normalized_variation_by_sample=self.variation.tolist(),
                    sampled_rank_bound=min(self.n, self.m + float(self.variation.sum()) / self.tol),
                    orthogonality_max=orth, rank_sum_before_query=self.work_rank_sum,
                    accepted=self.acceptance)


def validate():
    dtype = torch.float64
    x, y = data("sphere")
    model = Closure(x[:5], y[:5], 23, 3, "cpu", dtype)
    s = [v.clone() for v in model.initial]
    gen = torch.Generator().manual_seed(901)
    s[1] = torch.randn(s[1].shape, generator=gen, dtype=dtype)
    s[2] += .2 * torch.randn(s[2].shape, generator=gen, dtype=dtype)
    s[3] += .1 * torch.randn(s[3].shape, generator=gen, dtype=dtype)
    s[4].fill_(2.3)
    ev = model.evaluate(s)
    W = model.reconstruct(s).detach()
    W1, w = s[0].clone().requires_grad_(), s[1].clone().requires_grad_()
    hd1 = torch.tanh(model.xs @ W1.T)
    hd2 = torch.tanh(hd1 @ W.T)
    fd = hd2 @ w / model.n
    loss = ((fd - model.y) ** 2).mean()
    grad1, gradw = torch.autograd.grad(loss, [W1, w])
    rhs = model.rhs(s, ev)
    errors = dict(dense_prediction=float((fd-ev["f"]).abs().max()),
                  dense_h2=float((hd2-ev["h2"]).abs().max()),
                  first_velocity=float((rhs[0]+model.n*grad1).abs().max()),
                  readout_velocity=float((rhs[1]+model.n*gradw).abs().max()))
    # Differentiate reconstruction with respect to all raw moment coordinates.
    initial = [v.clone() for v in model.initial]
    vel = model.rhs(initial)
    _, dW = torch.autograd.functional.jvp(lambda *args: model.reconstruct(args), tuple(initial), tuple(vel))
    ei = model.evaluate(initial)
    densevel = -2 / (model.n*model.m) * (ei["delta2"].T * ei["r"]) @ ei["h1"]
    errors["initial_reconstruction_velocity"] = float((dW-densevel).abs().max())
    # Same initial prefix with nonzero readout makes this identity non-vacuous.
    initial[1] = torch.randn(initial[1].shape, generator=gen, dtype=dtype)
    vel = model.rhs(initial)
    _, dW = torch.autograd.functional.jvp(lambda *args: model.reconstruct(args), tuple(initial), tuple(vel))
    ei = model.evaluate(initial)
    densevel = -2 / (model.n*model.m) * (ei["delta2"].T * ei["r"]) @ ei["h1"]
    errors["nonzero_readout_prefix_velocity"] = float((dW-densevel).abs().max())
    # Raw integral with constant prefix, independently quadrature-evaluated.
    nodes, weights = np.polynomial.legendre.leggauss(16)
    nodes = torch.tensor((nodes+1)/2, dtype=dtype)
    weights = torch.tensor(weights/2, dtype=dtype)
    tau = torch.tensor(2.7, dtype=dtype, requires_grad=True)
    def pol(v):
        return torch.stack([torch.ones_like(v), 2*v-1, 6*v*v-6*v+1])
    prefix = 2*(pol(nodes/tau) @ weights)
    xi = 1+(tau-1)*nodes
    hsig = 2+(xi-1)+(xi-1)**2
    bsig = xi-1
    H = prefix+(tau-1)*(pol(xi/tau) @ (weights*hsig))
    D = (tau-1)*(pol(xi/tau) @ (weights*bsig))
    Hdot = torch.stack([torch.autograd.grad(H[k], tau, retain_graph=True)[0] for k in range(3)])
    Ddot = torch.stack([torch.autograd.grad(D[k], tau, retain_graph=True)[0] for k in range(3)])
    errors["synthetic_forward_moment"] = float((Hdot-(2+(tau-1)+(tau-1)**2-model.dilation@H/tau)).abs().max().detach())
    errors["synthetic_backward_moment"] = float((Ddot-((tau-1)-model.dilation@D/tau)).abs().max().detach())
    errors["passed"] = all(v < 1e-10 for v in errors.values())
    return errors


def run_case(args, q, started):
    device = torch.device(args.device)
    x, y = data(args.dataset)
    model = Closure(x, y, args.n, q, device)
    state = [v.clone() for v in model.initial]
    ev = model.evaluate(state)
    initial_h1, initial_h2 = ev["h1"].clone(), ev["h2"].clone()
    base = OUT / f"{args.dataset}_q{q}{'_predictors' if args.predictors else ''}"
    spans = {(tol, direction): OnlineSpan(args.n, len(y), tol, device)
             for tol in args.tolerances for direction in ["forward", "backward"]}
    metrics, max_motion = [], [0., 0.]
    steps = round(args.T/args.dt)
    finite = True
    case_start = time.monotonic()
    def observe(t, ev, complete=True):
        for (tol, direction), span in spans.items():
            span.observe(ev["h1" if direction == "forward" else "delta2"],
                         model.W0, direction == "backward", t)
        if complete:
            motion = [float((ev["h1"]-initial_h1).square().mean().sqrt()),
                      float((ev["h2"]-initial_h2).square().mean().sqrt())]
            for j in range(2):
                max_motion[j] = max(max_motion[j], motion[j])
            metrics.append(dict(t=t, loss=float(ev["rho"]**2), motion_h1=motion[0],
                                motion_h2=motion[1], tau=float(state[4])))
    observe(0., ev)
    with torch.no_grad():
        for step in range(steps):
            if time.monotonic() - started > args.max_seconds:
                raise TimeoutError("Dataset-process hard cumulative execution cap reached")
            v1 = model.rhs(state, ev)
            predictor = [s+args.dt*v for s, v in zip(state, v1)]
            ep = model.evaluate(predictor)
            if args.predictors:
                observe((step+1)*args.dt, ep, False)
            v2 = model.rhs(predictor, ep)
            state = [s+.5*args.dt*(u+v) for s, u, v in zip(state, v1, v2)]
            ev = model.evaluate(state)
            observe((step+1)*args.dt, ev)
            if step % 100 == 99:
                finite = all(bool(torch.isfinite(s).all()) for s in state)
                print(json.dumps(dict(dataset=args.dataset, q=q, step=step+1,
                     loss=metrics[-1]["loss"], ranks={f"{t}:{d}": z.rank for (t,d),z in spans.items()},
                     elapsed=time.monotonic()-started)), flush=True)
                if not finite:
                    raise FloatingPointError("Nonfinite raw state")
    summaries = {}
    for (tol, direction), span in spans.items():
        summaries[f"{tol}:{direction}"] = span.finish(Path(str(base)+f"_{tol}_{direction}"))
    primary = [summaries[f"0.001:{d}"] for d in ["forward", "backward"]]
    combined = sum(a["rank"] for a in primary)
    valid = finite and all(s["orthogonality_max"] < 1e-4 for s in summaries.values())
    motion_ok = min(max_motion) > .05
    target_ok = combined < args.n/8 and max(s["max_action_error_rms"] for s in primary) <= .005
    result = dict(dataset=args.dataset, q=q, n=args.n, m=len(y), d=x.shape[1],
                  dt=args.dt, T=args.T, seed=1771, data_seed=8841 if args.dataset=="sphere" else None,
                  predictor_observation=args.predictors, metrics=metrics, spans=summaries,
                  max_feature_motion=max_motion, combined_primary_rank=combined,
                  finite=finite, numerical_validity=valid, nontrivial_motion=motion_ok,
                  resource_target=target_ok, classification=("PASS" if target_ok else "FAIL") if valid and motion_ok else "INCONCLUSIVE",
                  case_elapsed_seconds=time.monotonic()-case_start,
                  source_sha256=digest(__file__), protocol_sha256=digest(Path(__file__).with_name("RANK_PROTOCOL.md")))
    Path(str(base)+"_summary.json").write_text(json.dumps(result, indent=2))
    np.savez(Path(str(base)+"_inputs.npz"), x=x, y=y, W1_initial=model.initial[0].cpu().numpy())
    print(json.dumps({k:v for k,v in result.items() if k not in ["metrics", "spans"]}), flush=True)
    return result


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--dataset", choices=["circle","sphere"], default="circle")
    ap.add_argument("--device", default="cuda:0")
    ap.add_argument("--n", type=int, default=2048)
    ap.add_argument("--T", type=float, default=80.)
    ap.add_argument("--dt", type=float, default=.05)
    ap.add_argument("--q", nargs="+", type=int, default=[1,3])
    ap.add_argument("--tolerances", nargs="+", type=float, default=[.001,.0001])
    ap.add_argument("--max-seconds", type=float, default=270.)
    ap.add_argument("--validate-only", action="store_true")
    ap.add_argument("--predictors", action="store_true")
    args=ap.parse_args()
    torch.set_num_threads(4)
    torch.backends.cuda.matmul.allow_tf32=False
    torch.backends.cudnn.allow_tf32=False
    OUT.mkdir(parents=True, exist_ok=True)
    errors=validate()
    print(json.dumps(errors), flush=True)
    if not errors["passed"]:
        raise AssertionError(errors)
    if args.validate_only:
        (OUT/"validation.json").write_text(json.dumps(errors,indent=2))
        return
    info=dict(command=sys.argv, python=sys.version, executable=sys.executable,
              torch=torch.__version__, numpy=np.__version__, cuda=torch.version.cuda,
              device=torch.cuda.get_device_name(args.device), platform=platform.platform(),
              source_sha256=digest(__file__), protocol_sha256=digest(Path(__file__).with_name("RANK_PROTOCOL.md")),
              pid=os.getpid(), validation=errors, started_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()))
    suffix="_predictors" if args.predictors else ""
    (OUT/f"{args.dataset}{suffix}_environment.json").write_text(json.dumps(info,indent=2))
    started=time.monotonic()
    for q in args.q:
        run_case(args,q,started)
    torch.cuda.synchronize()
    (OUT/f"{args.dataset}{suffix}_elapsed.json").write_text(json.dumps(dict(elapsed_seconds=time.monotonic()-started)))


if __name__=="__main__":
    main()
