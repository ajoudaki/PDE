#!/usr/bin/env python3
"""No-training CUDA parity checks for the study's actual autograd models."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import torch

from fit_benchmark import (FitModel, build_finite_closure, circle_dataset,
                           configure_torch, initialize)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    configure_torch()
    state = initialize(7, 2, 2, seed=53)
    W, A, c = state.weights[0], state.weights[1], state.readout
    closure, _ = build_finite_closure(W, A)
    data = circle_dataset(6, 16)
    records = []
    for kind in ("network", "closure"):
        models = [FitModel(kind, W, c, A if kind == "network" else closure["D"],
                           closure["B1"], closure["B2"]).to(device)
                  for device in ("cpu", "cuda:0", "cuda:1")]
        outputs, gradients = [], []
        for model in models:
            device = model.W.device
            pred = model(torch.tensor(data["u"], device=device))
            torch.mean((pred-torch.tensor(data["y"], device=device))**2).backward()
            outputs.append(pred.detach().cpu().numpy())
            gradients.append([p.grad.detach().cpu().numpy() for p in model.parameters()])
        for gpu in range(2):
            err = max(float(np.max(np.abs(a-b))) for a, b in
                      zip(gradients[0], gradients[gpu+1]))
            pred_err = float(np.max(np.abs(outputs[0]-outputs[gpu+1])))
            assert max(err, pred_err) <= 1e-12
            records.append(dict(model=kind, device=f"cuda:{gpu}", gradient_error=err,
                                prediction_error=pred_err, passed=True,
                                device_name=torch.cuda.get_device_name(gpu)))
    source = Path(__file__).with_name("fit_benchmark.py")
    report = dict(training_performed=False, torch=str(torch.__version__), checks=records,
                  producer_sha256=hashlib.sha256(source.read_bytes()).hexdigest())
    (args.output/"checks.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report))


if __name__ == "__main__":
    main()
