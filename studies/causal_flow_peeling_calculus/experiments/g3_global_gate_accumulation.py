#!/usr/bin/env python3
"""Preregistered G3 compact-time accumulation probe."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import torch

from g2_reachable_gate_defect import (
    compare,
    frozen_gate_block,
    integrate,
    seeded_state,
)


HORIZONS = (0.25, 0.5)
MESHES = (0.02, 0.01, 0.005)


def clone_state(state):
    return tuple(x.clone() for x in state)


def run_one(width, trial, alpha, device, dtype, ref_dt):
    initial = seeded_state(width, trial, alpha, device, dtype)

    references = {}
    reference = clone_state(initial)
    old_time = 0.0
    for horizon in HORIZONS:
        reference = integrate(reference, horizon - old_time, ref_dt, alpha)
        references[horizon] = clone_state(reference)
        old_time = horizon

    rows = []
    for mesh in MESHES:
        approximate = clone_state(initial)
        current = 0.0
        max_constraint = 0.0
        for horizon in HORIZONS:
            while current < horizon - 1e-12:
                step = min(mesh, horizon - current)
                approximate, check = frozen_gate_block(
                    approximate, step, alpha, ref_dt
                )
                max_constraint = max(max_constraint, check)
                current += step
            row = compare(
                references[horizon], approximate, alpha, width, trial,
                horizon, mesh, max_constraint
            )
            row["horizon"] = horizon
            row["mesh"] = mesh
            rows.append(row)
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--widths", default="128,256,512,1024")
    parser.add_argument("--trials", type=int, default=4)
    parser.add_argument("--alphas", default="0,0.2")
    parser.add_argument("--ref-dt", type=float, default=1.0 / 2048.0)
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--dtype", choices=("float32", "float64"), default="float32")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    widths = [int(x) for x in args.widths.split(",") if x]
    alphas = [float(x) for x in args.alphas.split(",") if x]
    device = torch.device(args.device)
    dtype = torch.float32 if args.dtype == "float32" else torch.float64
    if device.type == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested but unavailable")

    rows = []
    with torch.no_grad():
        for alpha in alphas:
            for width in widths:
                for trial in range(args.trials):
                    rows.extend(run_one(width, trial, alpha, device, dtype, args.ref_dt))

    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    with (output / "raw.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    metadata = {
        "widths": widths,
        "trials": args.trials,
        "alphas": alphas,
        "horizons": HORIZONS,
        "meshes": MESHES,
        "ref_dt": args.ref_dt,
        "device": str(device),
        "dtype": args.dtype,
        "checkpoint_rule": "partial final block to hit each checkpoint exactly",
        "torch": torch.__version__,
    }
    (output / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps({"rows": len(rows), **metadata}, indent=2))


if __name__ == "__main__":
    main()
