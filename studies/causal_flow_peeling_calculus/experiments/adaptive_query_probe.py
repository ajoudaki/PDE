#!/usr/bin/env python3
"""Preregistered Q1 probe: first adaptive transpose query and response scaling."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import numpy as np


sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from studies._output_paths import StudyPaths

PATHS = StudyPaths(__file__)
WIDTHS = (64, 128, 256, 512, 1024, 2048)
REPLICATES = {64: 40, 128: 40, 256: 30, 512: 20, 1024: 12, 2048: 6}
HUTCHINSON_PROBES = 8
BASE_SEED = 20260824


def one_trial(n: int, rng: np.random.Generator) -> dict[str, float]:
    u = rng.standard_normal(n)
    a = rng.standard_normal(n)
    g = rng.standard_normal((n, n))
    x = np.arctan(u)
    z = (g @ x) / np.sqrt(n)
    d = 1.0 / (1.0 + z * z)
    d_prime = -2.0 * z / (1.0 + z * z) ** 2
    c = a * d
    e = a * d_prime
    q = (g.T @ c) / np.sqrt(n)

    row_g2 = np.sum(g * g, axis=1)
    term_creation = np.mean(c * c)
    term_response = np.sum(x * x) * np.sum(e * e * row_g2) / (n**3)
    term_cross = 2.0 * np.sum(c * e * z) / (n**2)
    exact_hs2 = term_creation + term_response + term_cross

    hutchinson = []
    for _ in range(HUTCHINSON_PROBES):
        xi = rng.integers(0, 2, size=(n, n), dtype=np.int8).astype(np.float64)
        xi *= 2.0
        xi -= 1.0
        # J[xi], evaluated from the exact derivative formula without forming J.
        creation = (xi.T @ c) / np.sqrt(n)
        row_direction = (xi @ x) / n
        response = g.T @ (e * row_direction)
        jxi = creation + response
        hutchinson.append(float(np.mean(jxi * jxi)))

    record = {
        "n": float(n),
        "q_l2": float(np.mean(q * q) ** 0.5),
        "q_l4": float(np.mean(np.abs(q) ** 4) ** 0.25),
        "q_l6": float(np.mean(np.abs(q) ** 6) ** (1.0 / 6.0)),
        "q_l8": float(np.mean(np.abs(q) ** 8) ** 0.125),
        "response_hs2_exact": float(exact_hs2),
        "response_creation": float(term_creation),
        "response_adaptive": float(term_response),
        "response_cross": float(term_cross),
        "response_hs2_hutchinson": float(np.mean(hutchinson)),
        "response_hutchinson_sd": float(np.std(hutchinson, ddof=1)),
    }
    return record


def summarize(records: list[dict[str, float]]) -> dict[str, object]:
    metrics = [key for key in records[0] if key != "n"]
    result: dict[str, object] = {}
    for n in WIDTHS:
        group = [r for r in records if int(r["n"]) == n]
        result[str(n)] = {
            "replicates": len(group),
            **{
                metric: {
                    "mean": float(np.mean([r[metric] for r in group])),
                    "sd": float(np.std([r[metric] for r in group], ddof=1)),
                    "q10": float(np.quantile([r[metric] for r in group], 0.1)),
                    "q90": float(np.quantile([r[metric] for r in group], 0.9)),
                }
                for metric in metrics
            },
        }
    return result


def main() -> None:
    OUT = PATHS.parse(output_relative="experiments/outputs/adaptive_query").output_dir
    OUT.mkdir(parents=True, exist_ok=True)
    seed_sequence = np.random.SeedSequence(BASE_SEED)
    child_seeds = seed_sequence.spawn(sum(REPLICATES.values()))
    records: list[dict[str, float]] = []
    seed_index = 0
    for n in WIDTHS:
        for replicate in range(REPLICATES[n]):
            rng = np.random.default_rng(child_seeds[seed_index])
            seed_index += 1
            record = one_trial(n, rng)
            record["replicate"] = float(replicate)
            records.append(record)
        print(f"completed n={n} replicates={REPLICATES[n]}", flush=True)

    columns = list(records[0].keys())
    with (OUT / "raw.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(records)

    # Remove the bookkeeping column before aggregation.
    clean_records = [
        {key: value for key, value in record.items() if key != "replicate"}
        for record in records
    ]
    report = {
        "base_seed": BASE_SEED,
        "widths": list(WIDTHS),
        "replicates": REPLICATES,
        "hutchinson_probes": HUTCHINSON_PROBES,
        "summary": summarize(clean_records),
    }
    (OUT / "summary.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
