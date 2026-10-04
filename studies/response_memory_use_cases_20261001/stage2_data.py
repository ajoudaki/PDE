"""Reproduce the frozen stage2 datasets; no network outside explicit sources."""
import argparse
import concurrent.futures
import gzip
import hashlib
import io
import json
from pathlib import Path
import tarfile
import time
import urllib.request
import zipfile

import numpy as np

SEED = 20261002
FASHION = "https://raw.githubusercontent.com/zalandoresearch/fashion-mnist/master/data/fashion/"
SOURCES = {
    "train-images-idx3-ubyte.gz": (FASHION + "train-images-idx3-ubyte.gz", "8d4fb7e6c68d591d4c3dfef9ec88bf0d"),
    "train-labels-idx1-ubyte.gz": (FASHION + "train-labels-idx1-ubyte.gz", "25c81989df183df01b3e8a0aad5dffbe"),
    "t10k-images-idx3-ubyte.gz": (FASHION + "t10k-images-idx3-ubyte.gz", "bef4ecab320f06d8554ea6380940ec79"),
    "t10k-labels-idx1-ubyte.gz": (FASHION + "t10k-labels-idx1-ubyte.gz", "bb300cfdad3c16e7a12a480ee83cd310"),
    "cal_housing.tgz": ("https://ndownloader.figshare.com/files/5976036", "aaa5c9a6afe2225cc2aed2723682ae403280c4a3695a2ddda4ffb5d8215ea681"),
    "har.zip": ("https://archive.ics.uci.edu/static/public/240/human+activity+recognition+using+smartphones.zip", None),
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def download(item, raw):
    name, (url, expected) = item
    path = raw / name
    if not path.exists():
        request = urllib.request.Request(url, headers={"User-Agent": "response-memory-research/1.0"})
        with urllib.request.urlopen(request, timeout=90) as response:
            blob = response.read(200_000_000)
            if len(blob) == 200_000_000:
                raise RuntimeError("individual download exceeds declared small data limit")
        tmp = path.with_suffix(path.suffix + ".partial")
        tmp.write_bytes(blob)
        tmp.replace(path)
    blob = path.read_bytes()
    actual = hashlib.md5(blob).hexdigest() if expected and len(expected) == 32 else hashlib.sha256(blob).hexdigest()
    if expected and expected != actual:
        raise RuntimeError(f"Checksum failed: {name}: {actual}")
    print(json.dumps({"download": name, "bytes": len(blob), "sha256": digest(path)}), flush=True)
    return name, {"url": url, "bytes": len(blob), "sha256": digest(path), "expected_checksum": expected}


def idx(raw, name):
    blob = gzip.decompress((raw / name).read_bytes())
    dims = blob[3]
    shape = np.frombuffer(blob, dtype=">i4", offset=4, count=dims)
    return np.frombuffer(blob, dtype=np.uint8, offset=4 + 4 * dims).reshape(tuple(shape)).copy()


def preprocess(name, splits, output, regression=False):
    train_x = splits["train"][0].astype(np.float64)
    mean = train_x.mean(0)
    std = np.maximum(train_x.std(0), 1e-3)
    target_mean = float(splits["train"][1].mean()) if regression else 0.
    target_std = float(splits["train"][1].std()) if regression else 1.
    arrays = {"input_mean": mean, "input_std": std}
    metadata = {"target_mean": target_mean, "target_std": target_std, "target_tanh": regression, "splits": {}}
    for split, (x, y, indices, groups, subjects) in splits.items():
        standardized = np.clip((x - mean) / std, -5, 5)
        embedded = np.column_stack([standardized, np.ones(len(x))])
        embedded /= np.linalg.norm(embedded, axis=1, keepdims=True)
        transformed_y = np.tanh((y - target_mean) / target_std) if regression else y.astype(np.float64)
        assert np.all(np.isfinite(embedded)) and np.all(np.isfinite(transformed_y))
        assert np.max(np.abs(np.linalg.norm(embedded, axis=1) - 1)) < 1e-12
        arrays.update({f"X_{split}": embedded, f"y_{split}": transformed_y, f"index_{split}": indices,
                       f"group_{split}": groups, f"subject_{split}": subjects})
        metadata["splits"][split] = {"rows": len(x), "dimension": embedded.shape[1],
            "label_mean": float(transformed_y.mean()), "label_rms": float(np.sqrt(np.mean(transformed_y**2))),
            "groups": {str(int(k)): int(v) for k, v in zip(*np.unique(groups, return_counts=True))},
            "subjects": np.unique(subjects).tolist()}
    path = output / f"{name}.npz"
    np.savez_compressed(path, **arrays)
    metadata["sha256"] = digest(path)
    return metadata


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output
    output.mkdir(parents=True, exist_ok=True)
    if (output / "manifest.json").exists():
        raise RuntimeError("Completed dataset directory already exists")
    raw = output / "raw"
    raw.mkdir(exist_ok=True)
    start = time.monotonic()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        downloads = dict(pool.map(lambda item: download(item, raw), SOURCES.items()))
    manifest = {"seed": SEED, "sources": downloads, "source_sha256": digest(Path(__file__)),
                "protocol_sha256": digest(Path(__file__).with_name("STAGE2_DATA_PROTOCOL.md")), "datasets": {}}

    rng = np.random.default_rng(SEED)
    fashion_splits = {}
    for prefix, keys, counts in [("train", ["train", "val"], [1024, 256]), ("t10k", ["test"], [1024])]:
        x = idx(raw, f"{prefix}-images-idx3-ubyte.gz").reshape(-1, 784).astype(np.float64)
        groups = idx(raw, f"{prefix}-labels-idx1-ubyte.gz")
        selected = rng.permutation(np.flatnonzero((groups == 0) | (groups == 6)))
        pos = 0
        for key, count in zip(keys, counts):
            indices = selected[pos:pos + count]
            pos += count
            y = np.where(groups[indices] == 6, 1., -1.)
            fashion_splits[key] = (x[indices], y, indices, groups[indices], np.zeros(count, dtype=int))
    assert not set(fashion_splits["train"][2]) & set(fashion_splits["val"][2])
    manifest["datasets"]["fashion"] = preprocess("fashion", fashion_splits, output)

    with tarfile.open(raw / "cal_housing.tgz", "r:gz") as archive:
        table = np.loadtxt(archive.extractfile("CaliforniaHousing/cal_housing.data"), delimiter=",")
    table = table[:, [8, 7, 2, 3, 4, 5, 6, 1, 0]]
    y = table[:, 0] / 100000.
    x = table[:, 1:].copy()
    x[:, 2] /= x[:, 5]
    x[:, 3] /= x[:, 5]
    x[:, 5] = x[:, 4] / x[:, 5]
    indices = np.random.default_rng(SEED).permutation(len(x))
    housing_splits = {}
    pos = 0
    for key, count in [("train", 1024), ("val", 256), ("test", 1024)]:
        sel = indices[pos:pos + count]
        pos += count
        housing_splits[key] = (x[sel], y[sel], sel, np.zeros(count, dtype=int), np.zeros(count, dtype=int))
    manifest["datasets"]["housing"] = preprocess("housing", housing_splits, output, regression=True)

    har_splits = {}
    rng = np.random.default_rng(SEED)
    with zipfile.ZipFile(raw / "har.zip") as outer:
        archive = outer
        if not any(n.endswith("train/X_train.txt") for n in outer.namelist()):
            nested = [n for n in outer.namelist() if n.endswith(".zip")]
            assert len(nested) == 1, outer.namelist()
            archive = zipfile.ZipFile(io.BytesIO(outer.read(nested[0])))
        def har_read(suffix):
            names = [n for n in archive.namelist() if n.endswith(suffix)]
            assert len(names) == 1, names
            return np.loadtxt(io.BytesIO(archive.read(names[0])))
        for pool in ["train", "test"]:
            x = har_read(f"{pool}/X_{pool}.txt")
            groups = har_read(f"{pool}/y_{pool}.txt").astype(int)
            subjects = har_read(f"{pool}/subject_{pool}.txt").astype(int)
            if pool == "train":
                validation_subjects = np.sort(np.unique(subjects))[-4:]
                pools = [("train", np.flatnonzero(~np.isin(subjects, validation_subjects)), 1024),
                         ("val", np.flatnonzero(np.isin(subjects, validation_subjects)), 256)]
            else:
                pools = [("test", np.arange(len(x)), 1024)]
            for key, candidates, count in pools:
                sel = rng.permutation(candidates)[:count]
                assert len(sel) == count
                har_splits[key] = (x[sel], np.where(groups[sel] <= 3, 1., -1.), sel, groups[sel], subjects[sel])
        if archive is not outer:
            archive.close()
    subject_sets = [set(har_splits[k][4]) for k in ["train", "val", "test"]]
    assert not (subject_sets[0] & subject_sets[1] or subject_sets[0] & subject_sets[2] or subject_sets[1] & subject_sets[2])
    manifest["datasets"]["har"] = preprocess("har", har_splits, output)
    manifest["preparation_seconds"] = time.monotonic() - start
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"complete": str(output), "datasets": manifest["datasets"]}), flush=True)


if __name__ == "__main__":
    main()
