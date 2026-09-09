#!/usr/bin/env python3
"""Release-level integrity and anti-oracle checks for the PDE evidence."""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "results" / "raw"
PROCESSED = ROOT / "results" / "processed"
AGENT_OUTPUTS = ROOT.parent / "agent_outputs"


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_complete(path: Path) -> dict[str, np.ndarray]:
    with np.load(path, allow_pickle=False) as archive:
        return {key: archive[key].copy() for key in archive.files}


def verify_all_npz() -> int:
    paths = sorted(
        [
            *ROOT.rglob("*.npz"),
            *AGENT_OUTPUTS.rglob("*.npz"),
        ]
    )
    for path in paths:
        arrays = load_complete(path)
        check(bool(arrays), f"empty archive: {path}")
        for key, array in arrays.items():
            if np.issubdtype(array.dtype, np.number):
                check(np.all(np.isfinite(array)), f"nonfinite {path}:{key}")
    return len(paths)


def sha256(path: Path) -> str:
    result = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(2**20), b""):
            result.update(chunk)
    return result.hexdigest()


def interpolate_grams(grams: np.ndarray, target_nodes: int) -> np.ndarray:
    source_s = np.linspace(0.0, 1.0, grams.shape[1])
    target_s = np.linspace(0.0, 1.0, target_nodes)
    result = np.empty((grams.shape[0], target_nodes, 3, 3))
    for time in range(grams.shape[0]):
        for row in range(3):
            for column in range(3):
                result[time, :, row, column] = np.interp(
                    target_s,
                    source_s,
                    grams[time, :, row, column],
                )
    return result


def gram_increment_gap(left: np.ndarray, right: np.ndarray) -> float:
    left_increment = left - left[0:1]
    right_increment = right - right[0:1]
    return float(
        np.max(
            np.linalg.norm(
                left_increment - right_increment,
                axis=(-2, -1),
            )
        )
    )


def combine_arrays(paths: list[Path]) -> dict[str, np.ndarray]:
    archives = [load_complete(path) for path in paths]
    times = archives[0]["times"]
    check(
        all(np.array_equal(item["times"], times) for item in archives),
        "pooled reference time grids differ",
    )
    f = np.concatenate([item["f"] for item in archives], axis=0)
    grams = np.concatenate([item["grams"] for item in archives], axis=0)
    theta = np.concatenate([item["theta"] for item in archives], axis=0)
    seeds = np.concatenate([item["seeds"] for item in archives])
    increments = grams - grams[:, 0:1]
    sem = lambda x: np.std(x, axis=0, ddof=1) / np.sqrt(x.shape[0])
    return {
        "times": times,
        "seeds": seeds,
        "f_mean": np.mean(f, axis=0),
        "f_sem": sem(f),
        "grams_mean": np.mean(grams, axis=0),
        "grams_sem": sem(grams),
        "gram_increments_mean": np.mean(increments, axis=0),
        "gram_increments_sem": sem(increments),
        "theta_mean": np.mean(theta, axis=0),
        "theta_sem": sem(theta),
    }


def verify_pooled_reference(name: str, sources: list[str]) -> None:
    expected = combine_arrays([RAW / source for source in sources])
    actual = load_complete(PROCESSED / name)
    for key, value in expected.items():
        check(key in actual, f"{name} lacks {key}")
        check(np.array_equal(value, actual[key]), f"{name}:{key} mismatch")


def verify_no_reference_oracle() -> None:
    source = ROOT / "src" / "dense_pde" / "operator_galerkin.py"
    text = source.read_text(encoding="utf-8")
    tree = ast.parse(text, filename=str(source))
    imports: list[str] = []
    string_literals: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            string_literals.append(node.value)
    check(
        not any("dense_reference" in name for name in imports),
        "PDE source imports the dense reference",
    )
    forbidden = ("results/raw", "exact_ensemble", "reference_comparisons")
    check(
        not any(token in literal for token in forbidden for literal in string_literals),
        "PDE source contains a dense-reference path or result literal",
    )
    check("np.load" not in text, "PDE vector-field module performs file loading")


def verify_primary_and_restart() -> dict[str, float]:
    primary = load_complete(
        RAW / "pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz"
    )
    tail = load_complete(
        RAW
        / "pde_QMC_P5_N16_M256_R128_s20260723_dt0p1_T24_from8_to32.npz"
    )
    primary_meta = json.loads(str(primary["metadata_json"]))
    tail_meta = json.loads(str(tail["metadata_json"]))
    check(primary_meta["actual_width_independent_pde_run"] is True, "bad PDE label")
    check(
        primary_meta["contains_dense_network_weight_matrix"] is False,
        "PDE metadata claims a dense matrix",
    )
    check(
        primary_meta["static_compiler_sha256"]
        == tail_meta["static_compiler_sha256"],
        "restart compiler hash mismatch",
    )
    for key in ("f", "loss", "grams", "theta"):
        check(
            np.array_equal(primary[key][-1], tail[key][0]),
            f"restart observable mismatch: {key}",
        )
    check(float(np.min(primary["theta_min"])) >= -1e-12, "non-PSD tangent kernel")
    output_drift = float(
        np.max(np.linalg.norm(tail["f"] - tail["f"][0], axis=-1))
    )
    gram_drift = float(
        np.max(
            np.linalg.norm(
                tail["grams"] - tail["grams"][0:1],
                axis=(-2, -1),
            )
        )
    )
    check(output_drift < 1e-10, "PDE output tail has not plateaued")
    check(gram_drift < 1e-10, "PDE Gram tail has not plateaued")
    return {"output_tail_drift": output_drift, "gram_tail_drift": gram_drift}


def verify_ordered_limit_results() -> dict[str, float]:
    audit_root = AGENT_OUTPUTS / "statistical_audit"
    summary_path = audit_root / "ordered_limit_summary.json"
    check(summary_path.is_file(), "ordered-limit summary is missing")
    summary = json.loads(summary_path.read_text(encoding="utf-8"))

    for metadata in [
        *summary["exact_files"].values(),
        *summary["pde_files"].values(),
    ]:
        path = RAW / metadata["filename"]
        check(path.is_file(), f"ordered-limit source is missing: {path.name}")
        check(
            sha256(path) == metadata["sha256"],
            f"ordered-limit source hash mismatch: {path.name}",
        )

    p5 = load_complete(
        RAW / summary["pde_files"]["P5"]["filename"]
    )["grams"]
    p15 = load_complete(
        RAW / summary["pde_files"]["P15"]["filename"]
    )["grams"]
    ref_256_32 = load_complete(
        PROCESSED / "exact_combined_n256_L32_S128.npz"
    )["grams_mean"]
    ref_256_64 = load_complete(
        PROCESSED / "exact_combined_n256_L64_S64.npz"
    )["grams_mean"]
    ref_512_32 = load_complete(
        RAW / "exact_ensemble_n512_L32_S16_seed14000_dt0p02_T8p0.npz"
    )["grams_mean"]

    width_gap = gram_increment_gap(ref_512_32, ref_256_32)
    depth_gap = gram_increment_gap(
        ref_256_64,
        interpolate_grams(ref_256_32, ref_256_64.shape[1]),
    )
    p5_l64_gap = gram_increment_gap(
        interpolate_grams(p5, ref_256_64.shape[1]),
        ref_256_64,
    )
    p5_n512_gap = gram_increment_gap(
        interpolate_grams(p5, ref_512_32.shape[1]),
        ref_512_32,
    )

    cauchy = {
        item["comparison"]: item for item in summary["cauchy_decisions"]
    }
    pde_decisions = {
        (item["pde"], item["reference"]): item
        for item in summary["pde_decisions"]
    }
    expected = (
        (
            width_gap,
            cauchy["width_n256_to_n512_at_L32"][
                "observed_gram_increment_sup"
            ],
        ),
        (
            depth_gap,
            cauchy["depth_L32_to_L64_at_n256"][
                "observed_gram_increment_sup"
            ],
        ),
        (
            p5_l64_gap,
            pde_decisions[("P5", "E256_L64_S64")][
                "observed_gram_increment_sup"
            ],
        ),
        (
            p5_n512_gap,
            pde_decisions[("P5", "E512_L32_S16")][
                "observed_gram_increment_sup"
            ],
        ),
    )
    for recomputed, recorded in expected:
        check(
            abs(recomputed - recorded) < 1e-14,
            "ordered-limit curve metric does not reproduce",
        )

    check(
        all(
            item["decision"]
            == "not_statistically_resolved_at_curvewise_5pct"
            for item in summary["cauchy_decisions"]
        ),
        "ordered-limit Cauchy decision changed",
    )
    check(
        pde_decisions[("P5", "E256_L64_S64")]["decision"]
        == "not_statistically_resolved_at_curvewise_5pct",
        "P5/L64 decision changed",
    )
    check(
        pde_decisions[("P5", "E512_L32_S16")]["decision"]
        == "statistically_resolved_at_curvewise_5pct",
        "P5/n512 decision changed",
    )

    references = {
        "E256_L32_S128": ref_256_32,
        "E256_L64_S64": ref_256_64,
        "E512_L32_S16": ref_512_32,
    }
    for item in summary["p15_decisions"]:
        reference = references[item["reference"]]
        p5_gap = gram_increment_gap(
            interpolate_grams(p5, reference.shape[1]), reference
        )
        p15_gap = gram_increment_gap(
            interpolate_grams(p15, reference.shape[1]), reference
        )
        check(
            abs(p5_gap - item["observed_P5_gap"]) < 1e-14
            and abs(p15_gap - item["observed_P15_gap"]) < 1e-14,
            f"P-order metric changed for {item['reference']}",
        )
        check(
            item["decision"] == "P15_farther" and p15_gap > p5_gap,
            f"P15 direction changed for {item['reference']}",
        )

    return {
        "width_cauchy_gap": width_gap,
        "depth_cauchy_gap": depth_gap,
        "p5_l64_gap": p5_l64_gap,
        "p5_n512_gap": p5_n512_gap,
    }


def main() -> None:
    archive_count = verify_all_npz()
    verify_pooled_reference(
        "exact_combined_n128_L32_S96.npz",
        [
            "exact_ensemble_n128_L32_S32_seed3000_dt0p02_T8p0.npz",
            "exact_ensemble_n128_L32_S64_seed5000_dt0p02_T8p0.npz",
        ],
    )
    verify_pooled_reference(
        "exact_combined_n256_L32_S64.npz",
        [
            "exact_ensemble_n256_L32_S32_seed6000_dt0p02_T8p0.npz",
            "exact_ensemble_n256_L32_S32_seed8000_dt0p02_T8p0.npz",
        ],
    )
    verify_pooled_reference(
        "exact_combined_n256_L32_S128.npz",
        [
            "exact_ensemble_n256_L32_S32_seed6000_dt0p02_T8p0.npz",
            "exact_ensemble_n256_L32_S32_seed8000_dt0p02_T8p0.npz",
            "exact_ensemble_n256_L32_S64_seed10000_dt0p02_T8p0.npz",
        ],
    )
    verify_pooled_reference(
        "exact_combined_n256_L64_S64.npz",
        [
            "exact_ensemble_n256_L64_S16_seed7000_dt0p02_T8p0.npz",
            "exact_ensemble_n256_L64_S48_seed12000_dt0p02_T8p0.npz",
        ],
    )
    verify_no_reference_oracle()
    tail = verify_primary_and_restart()
    ordered = verify_ordered_limit_results()
    print(
        json.dumps(
            {
                "status": "passed",
                "complete_npz_archives": archive_count,
                **tail,
                **ordered,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
