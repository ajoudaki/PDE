"""Exact post-freeze symbolic-Q0 comparison by rational specialization.

The preregistration is ``SYMBOLIC_Q0_AUDIT_CONTRACT.md``.  This script does
not write or mutate any frozen independent or primary coefficient artifact.
It retains at most one fully expanded root from each route at a time.
"""

from __future__ import annotations

import gc
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from time import monotonic

from .depth_factored import compile_depth_factored, expand_expression


HERE = Path(__file__).resolve().parent
DEPTH_ROOT = HERE.parent
PRIMARY = DEPTH_ROOT / "primary"

RECONSTRUCTION_POINTS = (
    Fraction(1, 2),
    Fraction(2, 3),
    Fraction(1),
    Fraction(3, 2),
    Fraction(2),
    Fraction(3),
)
HOLDOUT = Fraction(5, 2)
ROOT_DEGREE_BOUNDS = {"A": 1, "B": 3, "C": 5}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def primary_specialization(records: list, q0: Fraction):
    """Strip explicit Q0 atoms and specialize their coefficient exactly."""

    out: dict[str, Fraction] = {}
    maximum_degree = 0
    separator = "\x1f"
    for atoms, coefficient_text in records:
        degree = atoms.count("Q0")
        maximum_degree = max(maximum_degree, degree)
        key = separator.join(atom for atom in atoms if atom != "Q0")
        coefficient = Fraction(coefficient_text) * q0**degree
        out[key] = out.get(key, Fraction(0)) + coefficient
    return {key: value for key, value in out.items() if value}, maximum_degree


def compare_root(independent_root, primary_map: dict[str, Fraction]):
    independent_map = expand_expression(independent_root)
    discrepancy_examples = []
    mismatch_count = 0
    for monomial, coefficient in independent_map.items():
        key = "\x1f".join(monomial)
        expected = primary_map.pop(key, Fraction(0))
        if coefficient != expected:
            mismatch_count += 1
            if len(discrepancy_examples) < 5:
                discrepancy_examples.append(
                    {
                        "atoms": list(monomial),
                        "independent": str(coefficient),
                        "primary": str(expected),
                    }
                )
    for key, expected in primary_map.items():
        mismatch_count += 1
        if len(discrepancy_examples) < 5:
            discrepancy_examples.append(
                {
                    "atoms": key.split("\x1f") if key else [],
                    "independent": "0",
                    "primary": str(expected),
                }
            )
    return len(independent_map), mismatch_count, discrepancy_examples


def compare_depth_point(depth: int, q0: Fraction) -> dict[str, object]:
    started = monotonic()
    independent = compile_depth_factored(depth, q0=q0, unit_gram=False)
    compiled = monotonic()

    primary_path = PRIMARY / f"H{depth}_LAYER_TAGGED_COEFFICIENTS.json"
    payload = json.loads(primary_path.read_text())
    if payload.get("depth") != depth or payload.get("quotient") != "layer-tagged-arbitrary-Q0":
        raise RuntimeError(f"unexpected primary schema in {primary_path}")

    roots = {}
    for name in "ABC":
        primary_map, observed_degree = primary_specialization(payload["roots"][name], q0)
        payload["roots"][name] = None
        gc.collect()
        term_count, mismatch_count, examples = compare_root(
            getattr(independent, name), primary_map
        )
        roots[name] = {
            "independent_term_count": term_count,
            "observed_primary_explicit_Q0_degree": observed_degree,
            "proved_degree_bound": ROOT_DEGREE_BOUNDS[name],
            "mismatch_count": mismatch_count,
            "discrepancy_examples": examples,
        }
        del primary_map
        gc.collect()
        print(
            f"H={depth} Q0={q0} {name}: terms={term_count} "
            f"mismatches={mismatch_count}",
            flush=True,
        )
    finished = monotonic()
    return {
        "Q0": str(q0),
        "compile_seconds": compiled - started,
        "total_seconds": finished - started,
        "roots": roots,
        "pass": all(item["mismatch_count"] == 0 for item in roots.values()),
    }


def main() -> None:
    started = monotonic()
    independent_manifest = HERE / "FROZEN_MANIFEST.json"
    primary_manifest = PRIMARY / "PRIMARY_FREEZE_MANIFEST.json"
    report: dict[str, object] = {
        "format": "independent-symbolic-Q0-rational-certificate-v1",
        "contract": "SYMBOLIC_Q0_AUDIT_CONTRACT.md",
        "independent_frozen_manifest_sha256": sha256(independent_manifest),
        "primary_frozen_manifest_sha256": sha256(primary_manifest),
        "degree_argument": (
            "only zdot1=Q0*b1 contains explicit Q0; k feature-vector-field "
            "applications introduce at most k factors"
        ),
        "degree_bounds": ROOT_DEGREE_BOUNDS,
        "reconstruction_points": [str(value) for value in RECONSTRUCTION_POINTS],
        "holdout": str(HOLDOUT),
        "depths": {},
    }
    for depth in (3, 4):
        point_reports = []
        for q0 in RECONSTRUCTION_POINTS + (HOLDOUT,):
            point_reports.append(compare_depth_point(depth, q0))
        report["depths"][str(depth)] = {
            "points": point_reports,
            "reconstruction_pass": all(item["pass"] for item in point_reports[:-1]),
            "holdout_pass": point_reports[-1]["pass"],
        }
    report["elapsed_seconds"] = monotonic() - started
    report["pass"] = all(
        item["reconstruction_pass"] and item["holdout_pass"]
        for item in report["depths"].values()
    )
    output = HERE / "SYMBOLIC_Q0_COMPARISON.json"
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"wrote {output}; pass={report['pass']}", flush=True)
    if not report["pass"]:
        raise SystemExit("symbolic-Q0 comparison failed")


if __name__ == "__main__":
    main()
