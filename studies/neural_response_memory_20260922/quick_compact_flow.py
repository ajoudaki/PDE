"""One bounded fitting check: three activations, dense and P=1,2,3.

Run once per task/GPU; the two task workers may run concurrently.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import time

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np
import torch
from compact_flow import Flow


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", required=True)
    parser.add_argument("--cases", type=Path, default=Path(__file__).resolve().parent / "activation_circle_cases.json")
    parser.add_argument("--device", required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--step", type=float, default=0.0625)
    parser.add_argument("--seconds", type=float, default=115)
    parser.add_argument("--circle", type=int, default=0, help="Number of uniform circle queries; zero skips them")
    parser.add_argument("--target-rms", type=float, default=.05)
    parser.add_argument("--fit-seconds", type=float, default=8.)
    parser.add_argument("--max-steps", type=int, default=12000)
    parser.add_argument("--depth", type=int, default=3)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    torch.set_num_threads(1)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.cuda.set_device(args.device)
    here = Path(__file__).resolve().parent
    cases = json.loads(args.cases.read_text())
    record = dict(task=args.task, device=args.device, width=2048, depth=args.depth,
                  step=args.step, target_rms=args.target_rms, dtype="float32", seed=20260920,
                  max_steps=args.max_steps, fit_seconds=args.fit_seconds,
                  scope="Training RMS check; no gradient-flow or circle-accuracy certificate",
                  torch=torch.__version__, gpu=torch.cuda.get_device_name(args.device),
                  circle_queries=args.circle,
                  cases_path=str(args.cases.resolve()), cases_sha256=hashlib.sha256(args.cases.read_bytes()).hexdigest(),
                  source_sha256={n: hashlib.sha256((here/n).read_bytes()).hexdigest()
                                 for n in ["compact_flow.py", "quick_compact_flow.py"]},
                  rows=[])
    def save():
        (args.out / "results.json").write_text(json.dumps(record, indent=2, allow_nan=False) + "\n")
    save()
    started = time.perf_counter()
    angles = 2*np.pi*np.arange(args.circle)/max(1, args.circle)
    circle_inputs = np.column_stack([np.cos(angles), np.sin(angles)])
    for activation in ["relu", "gelu", "selu"]:
        literal = cases.get(activation + "__" + args.task, cases.get(args.task))
        if literal is None: raise ValueError("Unknown task: " + args.task)
        angle = np.deg2rad(literal["angles_degrees"])
        x = np.column_stack([np.cos(angle), np.sin(angle)])
        y = np.array(literal["labels"])
        for order in [None, 1, 2, 3]:
            remaining = args.seconds - (time.perf_counter() - started)
            if remaining <= 0:
                record["status"] = "time_limit"
                save()
                return
            start = time.perf_counter()
            model = Flow(x, y, width=2048, depth=args.depth, activation=activation,
                         order=order, device=args.device, dtype=torch.float32)
            result = model.fit(step=args.step, target_rms=args.target_rms,
                               max_seconds=min(args.fit_seconds, remaining), max_steps=args.max_steps, block=32)
            if not np.isfinite(result["rms"]): result["rms"] = None
            prediction = model.predict(x).detach().cpu().numpy()
            rms = float(np.sqrt(np.mean((prediction-y)**2)))
            row = dict(activation=activation, model="dense" if order is None else f"P{order}",
                       **result, measured_rms=rms if np.isfinite(rms) else None,
                       total_seconds=time.perf_counter()-start)
            arrays = dict(inputs=x, labels=y, prediction=prediction)
            if args.circle:
                circle = np.concatenate([model.predict(circle_inputs[i:i+512]).cpu().numpy()
                                         for i in range(0, args.circle, 512)]).astype(np.float64)
                if order is None: dense_circle = circle
                difference = circle-dense_circle
                row["circle_rms_vs_dense"] = float(np.sqrt(np.mean(difference**2))) if np.isfinite(difference).all() else None
                arrays.update(circle_angles=angles, circle_prediction=circle)
                row["total_seconds"] = time.perf_counter()-start
            record["rows"].append(row)
            np.savez(args.out / f"{activation}_{row['model']}.npz", **arrays)
            print(json.dumps(row, allow_nan=False), flush=True)
            save()
            del model
    record.update(status="complete", total_seconds=time.perf_counter()-started)
    save()
    print(json.dumps(dict(task=args.task, total_seconds=record["total_seconds"])), flush=True)


if __name__ == "__main__":
    main()
