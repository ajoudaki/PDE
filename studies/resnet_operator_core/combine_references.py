#!/usr/bin/env python3
"""Combine disjoint exact-network ensembles without losing uncertainty data."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import numpy as np


def require_new_output(output: Path, inputs: list[Path]) -> tuple[Path, Path]:
    """Refuse occupied output/partial paths and all aliases of consumed inputs."""
    output = output.expanduser().absolute()
    partial = output.with_suffix(output.suffix + ".partial")
    for destination in (output, partial):
        for source in inputs:
            if destination.resolve() == source.resolve() or (
                destination.exists() and source.exists() and destination.samefile(source)
            ):
                raise ValueError(f"output aliases an input archive: {source}")
        if destination.exists() or destination.is_symlink():
            raise FileExistsError(f"refusing to overwrite output or partial: {destination}")
    return output, partial


def load_raw(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as archive:
        required = {"times", "seeds", "f", "grams", "theta", "metadata_json"}
        missing = required.difference(archive.files)
        if missing:
            raise ValueError(f"{path} is missing {sorted(missing)}")
        return {key: archive[key].copy() for key in required}


def sem(array: np.ndarray) -> np.ndarray:
    if array.shape[0] < 2:
        raise ValueError("at least two ensemble members are required")
    return np.std(array, axis=0, ddof=1) / np.sqrt(array.shape[0])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", type=Path, nargs="+")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output, _ = require_new_output(args.output, args.inputs)

    archives = [load_raw(path) for path in args.inputs]
    times = archives[0]["times"]
    metadata = [json.loads(str(item["metadata_json"])) for item in archives]
    for path, item, meta in zip(args.inputs[1:], archives[1:], metadata[1:]):
        if not np.array_equal(item["times"], times):
            raise ValueError(f"time grid mismatch in {path}")
        for key in ("n", "depth", "duration", "dt", "sample_dt", "sigma_w"):
            if meta.get(key) != metadata[0].get(key):
                raise ValueError(f"metadata mismatch for {key} in {path}")

    seeds = np.concatenate([item["seeds"] for item in archives])
    if np.unique(seeds).size != seeds.size:
        raise ValueError("input ensembles contain duplicate seeds")
    f = np.concatenate([item["f"] for item in archives], axis=0)
    grams = np.concatenate([item["grams"] for item in archives], axis=0)
    theta = np.concatenate([item["theta"] for item in archives], axis=0)
    gram_increments = grams - grams[:, 0:1]
    combined_metadata = {
        "role": "pooled exact-network ensemble reference",
        "sources": [str(path) for path in args.inputs],
        "source_metadata": metadata,
        "seeds": int(seeds.size),
    }

    args.output, partial = require_new_output(args.output, args.inputs)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with partial.open("xb") as handle:
        np.savez_compressed(
            handle,
            times=times,
            seeds=seeds,
            f_mean=np.mean(f, axis=0),
            f_sem=sem(f),
            grams_mean=np.mean(grams, axis=0),
            grams_sem=sem(grams),
            gram_increments_mean=np.mean(gram_increments, axis=0),
            gram_increments_sem=sem(gram_increments),
            theta_mean=np.mean(theta, axis=0),
            theta_sem=sem(theta),
            metadata_json=np.array(
                json.dumps(combined_metadata, sort_keys=True)
            ),
        )
        handle.flush()
        os.fsync(handle.fileno())
    if args.output.exists() or args.output.is_symlink():
        raise FileExistsError(f"output appeared during pooling: {args.output}")
    os.replace(partial, args.output)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "ensemble_members": int(seeds.size),
                "seed_min": int(np.min(seeds)),
                "seed_max": int(np.max(seeds)),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
