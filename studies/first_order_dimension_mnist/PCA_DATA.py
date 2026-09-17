"""Prepare and check train-only centered PCA retaining 98% of variance.

Preserve the projected coordinates, with no whitening or row normalization.
Run from any directory with ``python PCA_DATA.py``. A fresh output is required.
"""
import os

# Fix BLAS execution before importing NumPy. Eigenvector signs are fixed below.
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_name] = "1"

import argparse
import hashlib
import json
from pathlib import Path
import platform
import resource
import time

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "data/generated/first_order_dimension_mnist"
TARGET = 0.98


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_eigh(covariance):
    values, vectors = np.linalg.eigh(covariance)
    values = values[::-1].copy()
    components = vectors[:, ::-1].T.copy()
    # The largest-magnitude entry in each row is nonnegative.
    pivots = np.argmax(np.abs(components), axis=1)
    signs = np.sign(components[np.arange(len(components)), pivots])
    components *= signs[:, None]
    if values[-1] < -1e-12 * values[0]:
        raise ValueError("covariance has a significant negative eigenvalue")
    return np.maximum(values, 0.0), components, float(values[-1])


def norm_summary(rows):
    values = np.linalg.norm(rows.astype(np.float64), axis=1)
    return {"minimum": float(values.min()), "mean": float(values.mean()),
            "maximum": float(values.max()),
            "mean_squared": float(np.mean(values * values))}


def prepare(source, output, check_output):
    started, cpu_started = time.perf_counter(), time.process_time()
    source, output, check_output = map(Path, (source, output, check_output))
    # Hard bound on this process's CPU use, including all numerical checks.
    old_soft, old_hard = resource.getrlimit(resource.RLIMIT_CPU)
    cpu_limit = 120 if old_hard == resource.RLIM_INFINITY else min(120, old_hard)
    resource.setrlimit(resource.RLIMIT_CPU, (cpu_limit, old_hard))
    if output.exists() or check_output.exists():
        raise FileExistsError("PCA output/check directories must both be fresh")
    source_archive = source / "dataset.npz"
    source_hash = sha256(source_archive)
    source_metadata = json.loads((source / "metadata.json").read_text())
    if source_hash != source_metadata["dataset_sha256"]:
        raise ValueError("source archive differs from its frozen metadata")
    source_arrays = np.load(source_archive, allow_pickle=False)
    original_train = source_arrays["train_u"]
    if original_train.ndim != 2 or not np.all(np.isfinite(original_train)):
        raise ValueError("training inputs must be finite matrix rows")
    centered = original_train.astype(np.float64)
    mean = centered.mean(axis=0)
    centered -= mean
    samples, dimension = centered.shape
    covariance = centered.T @ centered / (samples - 1)
    eigenvalues, all_components, minimum_raw_eigenvalue = canonical_eigh(covariance)
    ratios = eigenvalues / eigenvalues.sum()
    cumulative = np.cumsum(ratios)
    retained_dimension = int(np.searchsorted(cumulative, TARGET, side="left") + 1)
    components = all_components[:retained_dimension].copy()
    retained_fraction = float(cumulative[retained_dimension - 1])
    previous_fraction = float(cumulative[retained_dimension - 2]) if retained_dimension > 1 else 0.0
    train_projection = centered @ components.T
    fit_seconds = time.perf_counter() - started
    fit_cpu_seconds = time.process_time() - cpu_started
    fit_peak_rss_bytes = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024)

    # Everything influencing the transform has been fixed before these reads.
    arrays = {"train_u": train_projection.astype(np.float32)}
    input_norms, output_norms = {}, {}
    for split in ("train", "val", "test"):
        original = original_train if split == "train" else source_arrays[split + "_u"]
        if split != "train":
            arrays[split + "_u"] = ((original.astype(np.float64) - mean) @ components.T).astype(np.float32)
        arrays[split + "_y"] = source_arrays[split + "_y"].copy()
        arrays[split + "_ids"] = source_arrays[split + "_ids"].copy()
        input_norms[split] = norm_summary(original)
        output_norms[split] = norm_summary(arrays[split + "_u"])

    output.mkdir(parents=True, exist_ok=False)
    check_output.mkdir(parents=True, exist_ok=False)
    np.savez_compressed(output / "dataset.npz", **arrays)
    np.savez_compressed(output / "transform.npz", mean=mean, components=components,
                        eigenvalues=eigenvalues, explained_variance_ratios=ratios)
    prepared_hash = sha256(output / "dataset.npz")
    transform_hash = sha256(output / "transform.npz")
    preprocessing_seconds = time.perf_counter() - started
    preprocessing_cpu_seconds = time.process_time() - cpu_started
    preprocessing_peak_rss_bytes = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024)

    # Cross-check covariance PCA against singular values of the full centered
    # rectangular matrix, without requesting its large left singular vectors.
    singular_values = np.linalg.svd(centered, compute_uv=False)
    svd_eigenvalues = singular_values * singular_values / (samples - 1)
    repeated_values, repeated_components, _ = canonical_eigh(covariance)
    total_centered_energy = float(np.einsum("ij,ij->", centered, centered))
    projected_energy = float(np.einsum("ij,ij->", train_projection, train_projection))
    reconstruction_error = 0.0
    for first in range(0, samples, 512):
        stop = first + 512
        error = centered[first:stop] - train_projection[first:stop] @ components
        reconstruction_error += float(np.einsum("ij,ij->", error, error))
    covariance_norm = float(np.linalg.norm(covariance))
    numerical = {
        "orthonormality_max_abs": float(np.max(np.abs(components @ components.T - np.eye(retained_dimension)))),
        "covariance_eigen_relative_frobenius": float(np.linalg.norm(covariance @ components.T - components.T * eigenvalues[:retained_dimension]) / covariance_norm),
        "trace_relative_error": abs(float(eigenvalues.sum()) - total_centered_energy / (samples - 1)) / float(eigenvalues.sum()),
        "projected_energy_fraction": projected_energy / total_centered_energy,
        "reconstruction_error_fraction": reconstruction_error / total_centered_energy,
        "energy_fraction_error": abs(projected_energy / total_centered_energy - retained_fraction),
        "reconstruction_fraction_error": abs(reconstruction_error / total_centered_energy - (1 - retained_fraction)),
        "svd_eigenvalues_relative_l2": float(np.linalg.norm(svd_eigenvalues - eigenvalues) / np.linalg.norm(eigenvalues)),
        "training_centering_max_abs": float(np.max(np.abs(centered.mean(axis=0)))),
        "minimum_raw_covariance_eigenvalue": minimum_raw_eigenvalue,
        "retained_fraction": retained_fraction,
        "previous_dimension_fraction": previous_fraction,
        "same_environment_fit_exact": bool(np.array_equal(repeated_values, eigenvalues) and np.array_equal(repeated_components, all_components)),
    }
    saved_checks = {}
    with np.load(output / "dataset.npz", allow_pickle=False) as saved, np.load(output / "transform.npz", allow_pickle=False) as transform:
        for split in ("train", "val", "test"):
            original = source_arrays[split + "_u"]
            direct = ((original.astype(np.float64) - transform["mean"]) @ transform["components"].T).astype(np.float32)
            saved_checks[split] = {
                "projection_exact_after_float32_rounding": bool(np.array_equal(saved[split + "_u"], direct)),
                "labels_unchanged": bool(np.array_equal(saved[split + "_y"], source_arrays[split + "_y"])),
                "ids_unchanged": bool(np.array_equal(saved[split + "_ids"], source_arrays[split + "_ids"])),
                "input_dtype_float32": bool(saved[split + "_u"].dtype == np.float32),
            }
    source_arrays.close()
    passed = bool(
        numerical["orthonormality_max_abs"] < 1e-11
        and numerical["covariance_eigen_relative_frobenius"] < 1e-11
        and numerical["trace_relative_error"] < 1e-11
        and numerical["energy_fraction_error"] < 1e-11
        and numerical["reconstruction_fraction_error"] < 1e-11
        and numerical["svd_eigenvalues_relative_l2"] < 1e-10
        and numerical["training_centering_max_abs"] < 1e-12
        and previous_fraction < TARGET <= retained_fraction
        and numerical["same_environment_fit_exact"]
        and all(all(split.values()) for split in saved_checks.values()))
    generated_bytes = sum(path.stat().st_size for path in output.iterdir())
    if generated_bytes >= 200 * 1024 ** 2:
        raise RuntimeError("generated data budget exceeded")
    metadata = {
        "digits": source_metadata["digits"],
        "positive_digit": source_metadata["positive_digit"],
        "negative_digit": source_metadata["negative_digit"],
        "split_seed": source_metadata["split_seed"],
        "counts": source_metadata["counts"], "class_counts": source_metadata["class_counts"],
        "dimension": retained_dimension, "source_dimension": dimension,
        "preprocessing": "Centered train-only PCA of saved L2-normalized image rows; smallest dimension retaining >=98% centered training variance; no whitening or post-PCA row normalization",
        "variance_target": TARGET, "retained_variance_fraction": retained_fraction,
        "previous_dimension_variance_fraction": previous_fraction,
        "total_centered_sample_variance": float(eigenvalues.sum()),
        "discarded_sample_variance": float(eigenvalues[retained_dimension:].sum()),
        "discarded_variance_fraction": 1 - retained_fraction,
        "variance_denominator": samples - 1, "fit_split": "train",
        "fit_arithmetic": "float64", "stored_input_arithmetic": "float32",
        "fit_method": "symmetric covariance eigendecomposition; descending eigenvalues; largest-magnitude component entry nonnegative",
        "source_path": str(source), "source_archive_sha256": source_hash,
        "source_metadata_sha256": sha256(source / "metadata.json"),
        "prepared_archive_sha256": prepared_hash, "dataset_sha256": prepared_hash,
        "transform_sha256": transform_hash, "preparation_source_sha256": sha256(__file__),
        "source_input_row_norms": input_norms, "projected_input_row_norms": output_norms,
        "mean_squared_training_mean": float(mean @ mean),
        "train_projected_energy_fraction_of_original": projected_energy / float(np.einsum("ij,ij->", original_train.astype(np.float64), original_train.astype(np.float64))),
        "fit_seconds": fit_seconds, "fit_cpu_seconds": fit_cpu_seconds,
        "fit_peak_process_rss_bytes": fit_peak_rss_bytes,
        "preprocessing_seconds": preprocessing_seconds,
        "preprocessing_cpu_seconds": preprocessing_cpu_seconds,
        "preprocessing_peak_process_rss_bytes": preprocessing_peak_rss_bytes,
        "process_rss_note": "Linux ru_maxrss; includes Python, NumPy, source loading and preparation, excluding later validation/SVD checks",
        "python": platform.python_version(), "numpy": np.__version__,
        "blas_threads": 1, "gpu_used": False,
        "determinism_scope": "Repeated fit exactly agrees in this environment; arbitrary BLAS/LAPACK versions may differ in degenerate eigenspaces or final rounding",
        "validity_check_passed": passed,
    }
    (output / "metadata.json").write_text(json.dumps(metadata, indent=2, allow_nan=False) + "\n")
    check = {
        "passed": passed, "claim": "finite train-only PCA construction and numerical diagnostics only",
        "numerical": numerical, "saved_split_checks": saved_checks,
        "source_archive_sha256": source_hash, "prepared_archive_sha256": prepared_hash,
        "transform_sha256": transform_hash, "source_sha256": sha256(__file__),
        "elapsed_seconds": time.perf_counter() - started,
        "cpu_seconds": time.process_time() - cpu_started,
        "peak_process_rss_bytes": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024),
        "data_artifact_bytes": generated_bytes, "cpu_budget_seconds": 120,
        "generated_budget_bytes": 200 * 1024 ** 2,
        "test_inputs_fit_transform": False, "test_labels_used_to_choose_transform": False,
    }
    (check_output / "check.json").write_text(json.dumps(check, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"passed": passed, "dimension": retained_dimension,
                      "retained_fraction": retained_fraction, "previous_fraction": previous_fraction,
                      "elapsed_seconds": check["elapsed_seconds"], "cpu_seconds": check["cpu_seconds"],
                      "output": str(output), "check": str(check_output / "check.json")}))
    if not passed:
        raise RuntimeError("PCA data validity gate failed; inspect retained report")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=BASE / "data_3_5")
    parser.add_argument("--output", type=Path, default=BASE / "data_pca98")
    parser.add_argument("--check-output", type=Path, default=BASE / "pca_data_check")
    args = parser.parse_args()
    prepare(args.source, args.output, args.check_output)
