"""Freeze a stratified 100-image subset of the prior MNIST training panel.

The complete official validation panel and all preprocessing are inherited
unchanged. Selection depends only on the parent training digits and fixed seed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import numpy as np


PARENT_SHA256 = "001d62792dccc16176d8e5cf832687e540c78f8a0f4dded5e42cd04adb74269c"
SEED = 20260924


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def array_record(values):
    return dict(shape=list(values.shape), dtype=str(values.dtype),
                sha256_c_order_bytes=hashlib.sha256(values.tobytes(order="C")).hexdigest())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--parent", type=Path, required=True,
                        help="Original mnist_data01/prepared.npz")
    parser.add_argument("--output", type=Path, required=True,
                        help="Fresh data directory")
    args = parser.parse_args()
    parent_hash = sha256(args.parent)
    parent_provenance_path = args.parent.parent / "provenance.json"
    parent_provenance = json.loads(parent_provenance_path.read_text())
    if parent_hash != PARENT_SHA256 or parent_provenance["prepared_sha256"] != parent_hash:
        raise ValueError("parent data do not match the frozen 1000-image experiment")
    with np.load(args.parent, allow_pickle=False) as archive:
        parent = {name: archive[name].copy() for name in archive.files}
    if parent["train_inputs"].shape != (1000, 784):
        raise ValueError("invalid parent training dimensions")
    if parent["validation_inputs"].shape != (1984, 784):
        raise ValueError("invalid parent validation dimensions")
    for split, expected in (("train", {3: 500, 8: 500}),
                            ("validation", {3: 1010, 8: 974})):
        digits, labels, ids = (parent[f"{split}_{name}"] for name in ("digits", "labels", "ids"))
        if {int(d): int(np.sum(digits == d)) for d in np.unique(digits)} != expected:
            raise ValueError(f"invalid parent {split} class counts")
        if not np.array_equal(labels, np.where(digits == 3, -1., 1.)):
            raise ValueError(f"invalid parent {split} labels")
        if len(np.unique(ids)) != len(ids):
            raise ValueError(f"duplicate parent {split} original IDs")
    checked_raw = {}
    for relative, expected_hash in parent_provenance["raw_sha256"].items():
        actual = sha256(args.parent.parent / relative)
        if actual != expected_hash:
            raise ValueError(f"parent raw checksum mismatch: {relative}")
        checked_raw[relative] = actual

    rng = np.random.default_rng(SEED)
    positions = np.concatenate([
        rng.choice(np.flatnonzero(parent["train_digits"] == digit), size=50, replace=False)
        for digit in (3, 8)])
    rng.shuffle(positions)
    prepared_arrays = {
        name: values[positions].copy() if name.startswith("train_") else values.copy()
        for name, values in parent.items()}
    prepared_arrays["train_parent_positions"] = positions
    for name, values in parent.items():
        if name.startswith("validation_") and not np.array_equal(prepared_arrays[name], values):
            raise AssertionError(f"validation changed: {name}")

    args.output.mkdir(parents=True, exist_ok=False)
    prepared_path = args.output / "prepared.npz"
    np.savez_compressed(prepared_path, **prepared_arrays)
    metadata = dict(
        seed=SEED, digits=[3, 8], samples_per_class=50, training_count=100,
        validation_count=1984, training_counts={"3": 50, "8": 50},
        validation_counts={"3": 1010, "8": 974},
        subset_method="NumPy default_rng(seed); for digits (3,8), choice of 50 parent row positions without replacement; concatenate; rng.shuffle",
        preprocessing=parent_provenance["preprocessing"],
        splits=parent_provenance["splits"],
        validation_policy="All parent validation arrays copied exactly; no selection or reprocessing",
        parent_dataset=str(args.parent.resolve()), parent_prepared_sha256=parent_hash,
        parent_provenance_sha256=sha256(parent_provenance_path),
        parent_source_sha256=parent_provenance["source_sha256"],
        source_mirrors=parent_provenance["source_mirrors"],
        resources=parent_provenance["resources"], parent_raw_sha256_verified=checked_raw,
        selected_parent_training_positions=positions.tolist(),
        original_train_ids=prepared_arrays["train_ids"].tolist(),
        original_validation_ids=prepared_arrays["validation_ids"].tolist(),
        prepared_sha256=sha256(prepared_path), source_sha256=sha256(__file__),
        arrays={name: array_record(values) for name, values in prepared_arrays.items()},
        python=sys.version, numpy=np.__version__, command=sys.argv)
    (args.output / "provenance.json").write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps({name: metadata[name] for name in
        ("training_count", "training_counts", "validation_count", "validation_counts",
         "parent_prepared_sha256", "prepared_sha256", "source_sha256")}, indent=2))


if __name__ == "__main__":
    main()
