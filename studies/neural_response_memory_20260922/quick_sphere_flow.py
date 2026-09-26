"""Bounded 3D extension of the compact dense/Legendre-closure comparison."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import sys
import time

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np
import torch
from compact_flow import Flow


def sphere_data(task, samples, queries=8192):
    """Nested iid training directions; separate equal-area Fibonacci test grid."""
    rng = np.random.default_rng(20260925)
    train = rng.standard_normal((samples, 3))
    train /= np.linalg.norm(train, axis=1, keepdims=True)
    i = np.arange(queries)
    z = 1 - 2*(i + .5)/queries
    angle = i*np.pi*(3-np.sqrt(5))
    radius = np.sqrt(1-z*z)
    test = np.column_stack([radius*np.cos(angle), radius*np.sin(angle), z])
    def target(x):
        if task == "xy": return np.sqrt(15)*x[:, 0]*x[:, 1]
        if task == "xyz": return np.sqrt(105)*np.prod(x, axis=1)
        raise ValueError(task)
    return train, target(train), test, target(test)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", choices=["xy", "xyz"], required=True)
    parser.add_argument("--samples", type=int, required=True)
    parser.add_argument("--device", required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--fit-seconds", type=float, default=12.)
    parser.add_argument("--step", type=float, default=1/128)
    parser.add_argument("--target-rms", type=float, default=.01)
    args = parser.parse_args()
    if args.samples < 1: raise ValueError("Positive sample count required")
    args.out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.cuda.set_device(args.device)
    x, y, test, truth = sphere_data(args.task, args.samples)
    np.savez(args.out / "data.npz", inputs=x, labels=y,
             test_inputs=test, test_labels=truth)
    here = Path(__file__).resolve().parent
    record = dict(task=args.task, samples=args.samples, dimension=3,
                  width=2048, depth=4, dtype="float32", step=args.step,
                  target_rms=args.target_rms, fit_seconds=args.fit_seconds,
                  max_steps=40000, block=32, network_seed=20260920,
                  data_seed=20260925, test_queries=len(test),
                  target="sqrt(15)*x*y" if args.task == "xy" else "sqrt(105)*x*y*z",
                  normalization="Unit directions supplied directly, as in the circle runs",
                  device=args.device, gpu=torch.cuda.get_device_name(args.device),
                  torch=torch.__version__, numpy=np.__version__,
                  command=shlex.join([sys.executable, *sys.argv]), cwd=os.getcwd(),
                  git_head=subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
                  source_sha256={name: hashlib.sha256((here/name).read_bytes()).hexdigest()
                                 for name in ["compact_flow.py", "quick_sphere_flow.py"]},
                  data_sha256=hashlib.sha256((args.out/"data.npz").read_bytes()).hexdigest(),
                  status="running", rows=[])
    def save():
        (args.out/"results.json").write_text(json.dumps(record, indent=2, allow_nan=False)+"\n")
    def rms(v):
        value = float(np.sqrt(np.mean(np.asarray(v, dtype=np.float64)**2)))
        return value if np.isfinite(value) else None
    save()
    started = time.perf_counter()
    for activation in ["relu", "gelu", "selu"]:
        for order in [None, 1, 2, 3]:
            begin = time.perf_counter()
            model = Flow(x, y, width=2048, depth=4, activation=activation,
                         order=order, seed=20260920, device=args.device)
            fit = model.fit(step=args.step, target_rms=args.target_rms,
                            max_seconds=args.fit_seconds, max_steps=40000, block=32)
            if not np.isfinite(fit["rms"]): fit["rms"] = None
            prediction = model.predict(x).cpu().numpy().astype(np.float64)
            test_prediction = np.concatenate([
                model.predict(test[i:i+512]).cpu().numpy()
                for i in range(0, len(test), 512)]).astype(np.float64)
            if order is None: dense_prediction = test_prediction.copy()
            name = "dense" if order is None else f"P{order}"
            row = dict(activation=activation, model=name, **fit,
                       train_rms=rms(prediction-y), test_rms_vs_dense=rms(test_prediction-dense_prediction),
                       test_rms_vs_target=rms(test_prediction-truth),
                       total_seconds=time.perf_counter()-begin)
            np.savez(args.out/f"{activation}_{name}.npz",
                     prediction=prediction, test_prediction=test_prediction)
            record["rows"].append(row)
            save()
            print(json.dumps(row, allow_nan=False), flush=True)
            del model
    record.update(status="complete", total_seconds=time.perf_counter()-started)
    save()
    print(json.dumps(dict(task=args.task, samples=args.samples,
                          total_seconds=record["total_seconds"])), flush=True)


if __name__ == "__main__":
    main()
