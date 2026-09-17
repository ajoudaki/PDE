"""Bounded checks of the study's tensor closure; no scientific training data.

Run CPU reference checks first. A GPU run repeats exactly these checks on the
selected device. --benchmark adds a small synthetic timing comparison only.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "code"))
from pde.observable_arithmetic import Arithmetic
from pde import observable_solver as cpu
from P1_ENGINE import ClosureEngine, TensorState


def as_np(x):
    return x.detach().cpu().numpy() if isinstance(x, torch.Tensor) else np.asarray(x)


def difference(actual, expected):
    a, b = as_np(actual), as_np(expected)
    return {"max_absolute": float(np.max(np.abs(a-b))),
            "relative_l2": float(np.linalg.norm(a-b)/max(np.linalg.norm(b), 1e-30))}


def close(actual, expected, *, atol=2e-12, rtol=2e-11):
    np.testing.assert_allclose(as_np(actual), as_np(expected), atol=atol, rtol=rtol)
    return difference(actual, expected)


def make_case(d, *, P1=17, P2=19, m=23, seed=912, device="cpu", dtype=torch.float64,
              block_size=7, unequal=True):
    rng = np.random.default_rng(seed)
    K1, K2 = 2*d+1, d+1
    b1, b2 = rng.normal(size=(P1, K1)), rng.normal(size=(P2, K2))
    g = rng.normal(size=(P1, d))
    D = rng.normal(scale=0.2/np.sqrt(d), size=(K2, K1))
    p1, p2 = (rng.uniform(0.5, 1.5, size=P1), rng.uniform(0.5, 1.5, size=P2))
    p1, p2 = (p1/p1.sum(), p2/p2.sum()) if unequal else (None, None)
    e = ClosureEngine(b1, g, b2, D, p1=p1, p2=p2, device=device, dtype=dtype, block_size=block_size)
    s = e.state(g+rng.normal(scale=0.2, size=g.shape), rng.normal(scale=0.3, size=P2),
                D+rng.normal(scale=0.1, size=D.shape))
    U = rng.normal(size=(m, d))
    U /= np.linalg.norm(U, axis=1, keepdims=True)
    y = rng.uniform(-1, 1, size=m)
    weights = rng.uniform(0.5, 1.5, size=m)
    data = e.prepare_data(U, y, weights/weights.sum() if unequal else None)
    return e, s, data


def cpu_oracle(device):
    e, s, data = make_case(2, device=device)
    ar = Arithmetic()
    old = cpu.State(*(as_np(x).copy() for x in (e.b1, e.g, s.w, e.p1, e.b2, s.c, e.p2, s.M, e.D)), ar).validate()
    law = cpu.DataLaw(as_np(data.inputs).copy(), as_np(data.labels).copy(),
                      as_np(data.probabilities).copy()).validate(ar)
    results = {"prediction": close(e.predict(s, data.inputs), cpu.predict(old, law.inputs, block_size=7))}
    for implementation in ("reference", "optimized"):
        velocity = e.rhs(s, data, implementation=implementation)
        reference = cpu.rhs(old, law, block_size=7)
        results[implementation] = {name: close(getattr(velocity, name), value)
                                   for name, value in zip(("w", "c", "M"), reference)}
    end = e.evolve(s, data, steps=5, step_size=0.015)
    oldend = cpu.evolve(old, law, steps=5, step_size=0.015, block_size=7)
    results["heun_5_steps"] = {k: close(getattr(end, k), getattr(oldend, k)) for k in ("w", "c", "M")}
    observations = e.observations(end, data, include_pairs=True)
    oldobs = cpu.paired_observations(oldend, law, block_size=7)
    results["observations"] = {"rms1": close(observations["rms1"], oldobs["rms1"]),
                               "rms2": close(observations["rms2"], oldobs["rms2"]),
                               "pairs1": close(observations["pairs1"], oldobs["first_pairs"]),
                               "pairs2": close(observations["pairs2"], oldobs["second_pairs"])}
    for number, name, p in ((1, "first_pairs", old.p1), (2, "second_pairs", old.p2)):
        h0, ht = oldobs[name][:, :, 0], oldobs[name][:, :, 1]
        for label, left, right in (("initial", h0, h0), ("current", ht, ht), ("cross", h0, ht)):
            results["observations"][f"gram{number}_{label}"] = close(
                observations[f"gram{number}_{label}"], left.T @ (p[:, None]*right))
    return results


def autograd_check(device):
    results = {}
    for d, P1, P2 in ((1,17,19), (2,17,19), (7,17,19), (11,9,7)):
        e, s, data = make_case(d, P1=P1, P2=P2, device=device, unequal=True)
        w, c, M = [x.clone().requires_grad_(True) for x in (s.w, s.c, s.M)]
        # Independent ordinary Euclidean differentiation, then the exact
        # population L2 metric: divide each population gradient by its weight.
        h1 = torch.tanh(w @ data.inputs.T)
        a = e.b1.T @ (e.p1[:, None]*h1)
        h2 = torch.tanh(e.b2 @ (M @ a))
        f = torch.sum(e.p2[:, None]*c[:, None]*h2, dim=0)
        objective = torch.sum(data.probabilities*(f-data.labels)**2)
        gw, gc, gM = torch.autograd.grad(objective, (w, c, M))
        velocity = e.rhs(s, data)
        results[str(d)] = {"w": close(velocity.w, -gw/e.p1[:, None]),
                           "c": close(velocity.c, -gc/e.p2),
                           "M": close(velocity.M, -gM)}
        derivative = (gw*velocity.w).sum()+(gc*velocity.c).sum()+(gM*velocity.M).sum()
        energy = -(e.p1[:, None]*velocity.w.square()).sum()-(e.p2*velocity.c.square()).sum()-velocity.M.square().sum()
        results[str(d)]["energy_identity"] = close(derivative, energy)
        initial_velocity = e.rhs(e.initial_state(), data)
        assert torch.count_nonzero(initial_velocity.w) == 0
        assert torch.count_nonzero(initial_velocity.M) == 0
    return results


def blocking_restart(device, output):
    e, s, data = make_case(5, device=device, unequal=False, block_size=23)
    full = e.rhs(s, data)
    full_prediction = e.predict(s, data.inputs)
    result = {}
    for block in (1, 7, 23, 64):
        e.block_size = block
        blocked = e.rhs(s, data)
        result[str(block)] = {k: close(getattr(blocked, k), getattr(full, k)) for k in ("w", "c", "M")}
        result[str(block)]["prediction"] = close(e.predict(s, data.inputs), full_prediction)
    e.block_size = 7
    for mode in ("direct", "folded", "auto"):
        e.forward_mode = mode
        velocity = e.rhs(s, data)
        result["forward_"+mode] = {k: close(getattr(velocity, k), getattr(full, k)) for k in ("w", "c", "M")}
    half = e.evolve(s, data, steps=4, step_size=0.02)
    checkpoint = output / "restart.npz"
    e.save_restart(checkpoint, half, data, metadata={"test": "own_state"})
    restored, state, data2, metadata = ClosureEngine.load_restart(checkpoint, device=device)
    assert metadata == {"test": "own_state"}
    for k in ("w", "c", "M"):
        assert torch.equal(getattr(half, k), getattr(state, k))
    continuation = restored.evolve(state, data2, steps=5, step_size=0.02)
    direct = e.evolve(s, data, steps=9, step_size=0.02)
    result["restart_bitwise"] = {k: bool(torch.equal(getattr(continuation, k), getattr(direct, k))) for k in ("w", "c", "M")}
    assert all(result["restart_bitwise"].values())
    return result


def signfold_check(device, use_initializer=False):
    # Synthetic exact sign-paired joint marks exercise folding independently
    # of initialization. The moving odd-to-odd matrix is fully dense.
    rng = np.random.default_rng(527)
    d, P = 4, 18
    g = rng.normal(size=(P, d))
    b1 = rng.normal(size=(P, 2*d))
    b2 = rng.normal(size=(P, d))
    D = rng.normal(scale=0.2, size=(d, 2*d))
    if use_initializer:
        from P1_INITIALIZATION import initialize
        initial = initialize(d, 2*P, 527, population_rule="antithetic", folded=True)
        whole = initialize(d, 2*P, 527, population_rule="antithetic", folded=False)
        b1, g, b2, D = initial.b1, initial.g, initial.b2, initial.D
    folded = ClosureEngine(b1, g, b2, D, device=device, block_size=5)
    fullb1 = np.column_stack((np.ones(2*P), np.concatenate((b1, -b1))))
    fullb2 = np.column_stack((np.ones(2*P), np.concatenate((b2, -b2))))
    fullD = np.zeros((d+1, 2*d+1)); fullD[1:, 1:] = D
    if use_initializer:
        fullb1, fullb2, fullD = whole.b1, whole.b2, whole.D
    unfolded = ClosureEngine(fullb1, np.concatenate((g, -g)), fullb2, fullD,
                             device=device, block_size=5)
    w = g+rng.normal(scale=0.2, size=g.shape)
    c = rng.normal(scale=0.3, size=P)
    M = D+rng.normal(scale=0.2, size=D.shape)
    fs = folded.state(w, c, M)
    wholeM = fullD.copy(); wholeM[1:, 1:] = M
    us = unfolded.state(np.concatenate((w, -w)), np.concatenate((c, -c)), wholeM)
    U = rng.normal(size=(17, d)); U /= np.linalg.norm(U, axis=1, keepdims=True)
    y = rng.uniform(-1, 1, size=len(U))
    fd, ud = folded.prepare_data(U, y), unfolded.prepare_data(U, y)
    result = {}
    for step in range(4):
        fv, uv = folded.rhs(fs, fd), unfolded.rhs(us, ud)
        result[str(step)] = {"prediction": close(folded.predict(fs, fd.inputs), unfolded.predict(us, ud.inputs)),
                             "w_rhs": close(fv.w, uv.w[:P]), "c_rhs": close(fv.c, uv.c[:P]),
                             "M_rhs": close(fv.M, uv.M[1:, 1:]),
                             "constant_row_rhs": close(uv.M[0], torch.zeros_like(uv.M[0])),
                             "constant_column_rhs": close(uv.M[:, 0], torch.zeros_like(uv.M[:, 0]))}
        fs, us = folded.heun_step(fs, fd, 0.03), unfolded.heun_step(us, ud, 0.03)
        for k in ("w", "c"):
            close(getattr(fs, k), getattr(us, k)[:P])
            close(getattr(us, k)[P:], -getattr(us, k)[:P])
        close(fs.M, us.M[1:, 1:])
    fobs, uobs = folded.observations(fs, fd), unfolded.observations(us, ud)
    result["observations"] = {k: close(fobs[k], uobs[k]) for k in fobs}
    return result


def representative_benchmark(device):
    """One bounded d784/Pnom2048/m2048 case, synthetic inputs and labels."""
    from P1_INITIALIZATION import initialize
    init = initialize(784, 2048, 617, population_rule="antithetic", folded=True)
    rng = np.random.default_rng(618)
    w = init.g+rng.normal(scale=0.02, size=init.g.shape)
    c = rng.normal(scale=0.1, size=len(init.b2))
    M = init.D+rng.normal(scale=0.001, size=init.D.shape)
    U = rng.normal(size=(2048, 784)); U /= np.linalg.norm(U, axis=1, keepdims=True)
    y = rng.choice([-1.0,1.0], size=len(U))
    result = {"shape": {"d": 784, "nominal_P": 2048, "stored_P": 1024,
                        "m": 2048, "K1": 1568, "K2": 784},
              "synthetic_only": True, "tf32": False}
    e64 = ClosureEngine(init.b1,init.g,init.b2,init.D,device=device,block_size=512)
    s64, data64 = e64.state(w,c,M), e64.prepare_data(U,y)
    v64 = e64.rhs(s64,data64)
    e = ClosureEngine(init.b1,init.g,init.b2,init.D,device=device,block_size=512,dtype=torch.float32)
    state, data = e.state(w,c,M), e.prepare_data(U,y)
    v = e.rhs(state,data)
    result["rhs_float32_vs_float64"] = {k: close(getattr(v,k),getattr(v64,k),atol=3e-6,rtol=1e-2)
                                        for k in ("w","c","M")}
    def sync():
        if e.device.type == "cuda":
            torch.cuda.synchronize(e.device)
    timings = []
    for block in (256,512,1024,2048):
        e.block_size = block
        for mode in ("direct","folded"):
            e.forward_mode = mode
            computed = e.rhs(state,data)
            errors = {k: close(getattr(computed,k),getattr(v,k),atol=3e-6,rtol=1e-2)
                      for k in ("w","c","M")}
            e.rhs(state,data)
            sync()
            samples = []
            if e.device.type == "cuda":
                torch.cuda.reset_peak_memory_stats(e.device)
            for _ in range(3):
                start = time.perf_counter()
                e.rhs(state,data)
                sync()
                samples.append(time.perf_counter()-start)
            row = {"block_size":block,"forward_mode":mode,"seconds":samples,
                   "median_seconds":float(np.median(samples)),"equivalence":errors}
            if e.device.type == "cuda":
                row["peak_allocated_bytes"] = torch.cuda.max_memory_allocated(e.device)
            timings.append(row)
    result["timings"] = timings
    result["fastest_observed"] = min(timings,key=lambda x:x["median_seconds"])
    # Direct displayed implementation provides the pre-refactor comparator.
    e.block_size = result["fastest_observed"]["block_size"]
    e.forward_mode = "auto"
    samples = []
    e.rhs(state,data,implementation="reference")
    sync()
    for _ in range(3):
        start = time.perf_counter()
        e.rhs(state,data,implementation="reference")
        sync()
        samples.append(time.perf_counter()-start)
    result["reference_at_selected_block"] = {"seconds":samples,"median_seconds":float(np.median(samples))}
    return result


def precision_check(device):
    results = {}
    for d, P, m in ((7, 23, 31), (64, 128, 96)):
        e64, s64, data64 = make_case(d, P1=P, P2=P, m=m, device=device, seed=457,
                                    block_size=32, unequal=False)
        e32, s32, data32 = make_case(d, P1=P, P2=P, m=m, device=device, seed=457,
                                    block_size=32, unequal=False, dtype=torch.float32)
        v64, v32 = e64.rhs(s64, data64), e32.rhs(s32, data32)
        row = {"rhs": {k: close(getattr(v32, k), getattr(v64, k), atol=2e-6, rtol=2e-4)
                       for k in ("w", "c", "M")}}
        for _ in range(24):
            s64, s32 = e64.heun_step(s64, data64, 0.01), e32.heun_step(s32, data32, 0.01)
        row["24_heun_steps"] = {k: close(getattr(s32, k), getattr(s64, k), atol=3e-6, rtol=3e-4)
                                for k in ("w", "c", "M")}
        row["prediction"] = close(e32.predict(s32, data32.inputs), e64.predict(s64, data64.inputs),
                                   atol=2e-6, rtol=2e-4)
        row["loss"] = difference(e32.loss(s32, data32), e64.loss(s64, data64))
        results[str(d)] = row
    return results


def benchmark(device):
    e, state, data = make_case(64, P1=256, P2=256, m=1024, device=device,
                               unequal=False, block_size=128, dtype=torch.float64)
    def sync():
        if e.device.type == "cuda":
            torch.cuda.synchronize(e.device)
    out = {"shape": {"d": 64, "P1": 256, "P2": 256, "m": 1024, "block": 128},
           "dtype": "float64", "repetitions": 5}
    # Algebra comparisons precede timing, even when called independently.
    ref, opt = e.rhs(state, data, implementation="reference"), e.rhs(state, data)
    out["equivalence"] = {k: close(getattr(opt, k), getattr(ref, k)) for k in ("w", "c", "M")}
    for implementation in ("reference", "optimized"):
        for _ in range(2):
            e.rhs(state, data, implementation=implementation)
        sync()
        samples = []
        for _ in range(5):
            start = time.perf_counter()
            e.rhs(state, data, implementation=implementation)
            sync()
            samples.append(time.perf_counter()-start)
        out[implementation] = {"seconds": samples, "median_seconds": float(np.median(samples))}
    out["speedup_median"] = out["reference"]["median_seconds"]/out["optimized"]["median_seconds"]
    out["engine_and_state_retained_bytes"] = e.retained_bytes(state)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--output", type=Path,
                        default=ROOT/"data/generated/first_order_dimension_mnist/engine_checks/cpu")
    parser.add_argument("--benchmark", action="store_true")
    parser.add_argument("--representative-benchmark", action="store_true")
    parser.add_argument("--threads", type=int, default=1)
    args = parser.parse_args()
    torch.set_num_threads(args.threads)
    if args.device.startswith("cuda"):
        torch.backends.cuda.matmul.allow_tf32 = False
        torch.backends.cudnn.allow_tf32 = False
    args.output.mkdir(parents=True, exist_ok=True)
    result = {"device": args.device, "torch": torch.__version__, "numpy": np.__version__,
              "threads": torch.get_num_threads(), "tf32": False,
              "source_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                                 for p in (Path(__file__), Path(__file__).with_name("P1_ENGINE.py"),
                                           Path(__file__).with_name("P1_INITIALIZATION.py"))},
              "claim_scope": "finite synthetic implementation checks; no population or training accuracy bound"}
    if args.device.startswith("cuda"):
        result["gpu_name"] = torch.cuda.get_device_name(torch.device(args.device))
        result["cuda_runtime"] = torch.version.cuda
    start = time.perf_counter()
    for name, function in (("maintained_cpu_oracle", lambda: cpu_oracle(args.device)),
                            ("autograd_population_metric", lambda: autograd_check(args.device)),
                            ("blocking_restart", lambda: blocking_restart(args.device, args.output)),
                            ("signfold_exact_quadrature", lambda: signfold_check(args.device)),
                            ("initializer_signfold_exact_quadrature", lambda: signfold_check(args.device, True)),
                            ("float32_vs_float64", lambda: precision_check(args.device))):
        result[name] = function()
        print(name + ": PASS", flush=True)
    if args.benchmark:
        result["benchmark"] = benchmark(args.device)
    if args.representative_benchmark:
        result["representative_benchmark"] = representative_benchmark(args.device)
    result["elapsed_seconds"] = time.perf_counter()-start
    result["status"] = "PASS"
    path = args.output / "checks.json"
    path.write_text(json.dumps(result, indent=2, allow_nan=False)+"\n")
    print(json.dumps({"status": result["status"], "elapsed_seconds": result["elapsed_seconds"],
                      "report": str(path), "benchmark": result.get("benchmark", {})}))


if __name__ == "__main__":
    main()
