"""Recompute the sphere comparison table from saved predictions; no training."""
import argparse
import csv
import json
from pathlib import Path

import numpy as np


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    scores, rows, durations = [], [], {}
    rms = lambda x: float(np.sqrt(np.mean(np.asarray(x, dtype=np.float64)**2)))
    for task in ["xy", "xyz"]:
        for samples in [32, 64]:
            folder = args.root/f"{task}_m{samples}"
            record = json.loads((folder/"results.json").read_text())
            assert record["status"] == "complete" and len(record["rows"]) == 12
            durations[folder.name] = record["total_seconds"]
            with np.load(folder/"data.npz") as data:
                labels, truth = data["labels"].copy(), data["test_labels"].copy()
                assert data["inputs"].shape == (samples, 3)
                assert data["test_inputs"].shape == (8192, 3)
            for row in record["rows"]:
                act, model = row["activation"], row["model"]
                with np.load(folder/f"{act}_dense.npz") as data:
                    dense = data["test_prediction"].copy()
                with np.load(folder/f"{act}_{model}.npz") as data:
                    values = dict(train_rms=rms(data["prediction"]-labels),
                                  test_rms_vs_target=rms(data["test_prediction"]-truth),
                                  test_rms_vs_dense=rms(data["test_prediction"]-dense))
                for key, value in values.items():
                    assert np.isfinite(value) and abs(value-row[key]) < 1e-12
                scores.append(dict(task=task, samples=samples, activation=act, model=model,
                                   **values, status=row["status"], steps=row["steps"],
                                   physical_time=row["physical_time"], seconds=row["total_seconds"]))
            for act in ["relu", "gelu", "selu"]:
                group = {r["model"]: r for r in scores
                         if (r["task"], r["samples"], r["activation"]) == (task, samples, act)}
                values = [group[f"P{p}"]["test_rms_vs_dense"] for p in [1, 2, 3]]
                values.extend([group["dense"]["test_rms_vs_target"], group["P3"]["test_rms_vs_target"]])
                rows.append(f"| {task} | {samples} | {act.upper()} | "+" | ".join(f"{v:.5f}" for v in values)+" |")
    with (args.root/"sphere_rms.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(scores[0]))
        writer.writeheader(); writer.writerows(scores)
    summary = dict(fits=len(scores), target_reached=sum(r["status"] == "target_rms" for r in scores),
                   maximum_train_rms=max(r["train_rms"] for r in scores), worker_seconds=durations,
                   fit_seconds_range=[min(r["seconds"] for r in scores), max(r["seconds"] for r in scores)])
    (args.root/"summary.json").write_text(json.dumps(summary, indent=2)+"\n")
    table = ("| Target | Samples | Activation | P1 vs dense | P2 vs dense | P3 vs dense | Dense vs target | P3 vs target |\n"
             "|---|---:|---|---:|---:|---:|---:|---:|\n"+"\n".join(rows)+"\n")
    (args.root/"table.md").write_text(table)
    print(table)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
