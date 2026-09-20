"""Targeted numerical-quality correction using the unchanged frozen integrator.

Select solely by discrepancy between two generated levels, never by dictionary
ranking. Each selected trajectory is regenerated from its original initialization.
"""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import time

from benchmark import setup, save_json, source_hashes, np, torch, NetworkEngine, ROOT
from diverse_cases import CASES_V2
from diverse_dictionary import build
from diverse_benchmark import (trajectory, WIDTH, NETWORK_SEED, DICTIONARY_SEED,
                               THRESHOLD, METHODS, MAX_TIME, MAX_STEPS, SNAPSHOTS)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--older", type=Path, required=True)
    parser.add_argument("--newer", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--worker", type=int, choices=(0, 1), required=True)
    parser.add_argument("--workers", type=int, choices=(1, 2), default=2)
    parser.add_argument("--exclude", type=Path, action="append", default=[], help="Already attempted cells at this tolerance level")
    parser.add_argument("--device", required=True)
    parser.add_argument("--level", type=int, choices=(1, 2), required=True)
    parser.add_argument("--budget", type=float, default=300., help="Integration seconds; at most 300 per worker/level")
    args = parser.parse_args()
    if not 0 < args.budget <= 300:
        raise ValueError("At most 300 seconds per worker and level")
    if args.worker >= args.workers:
        raise ValueError("Worker index must be smaller than the worker count")
    device = setup(args.device)
    selected = []
    for path in sorted(args.newer.glob("*/summary.json")):
        key = path.parent.name
        if any((root / key / "summary.json").exists() for root in args.exclude):
            continue
        older = args.older / key
        if not (older / "summary.json").exists():
            continue
        a, b = json.loads((older / "summary.json").read_text()), json.loads(path.read_text())
        if a["status"] != "fitted" or b["status"] != "fitted":
            continue
        with np.load(older / "arrays.npz", allow_pickle=False) as s:
            x = torch.as_tensor(s["endpoint_prediction"], dtype=torch.float64, device=device)
        with np.load(path.parent / "arrays.npz", allow_pickle=False) as s:
            y = torch.as_tensor(s["endpoint_prediction"], dtype=torch.float64, device=device)
        error = float((x-y).abs().max())
        if error > .01:
            selected.append(dict(key=key, discrepancy=error))
    rtol, atol = 2.5e-4 / 4**args.level, 2.5e-6 / 4**args.level
    args.out.mkdir(parents=True, exist_ok=True)
    config_path = args.out / f"config_worker{args.worker}.json"
    if config_path.exists():
        raise FileExistsError(config_path)
    own = selected[args.worker::args.workers]
    config = dict(cases=CASES_V2, width=WIDTH, network_seed=NETWORK_SEED, dictionary_seed=DICTIONARY_SEED,
                  threshold=THRESHOLD, orders=[1,3,5], dtype="float64", step=.05, max_step=2.,
                  rtol=rtol, atol=atol, max_time=MAX_TIME, max_steps=MAX_STEPS,
                  worker_limit_seconds=args.budget, per_trajectory_limit_seconds=180,
                  snapshot_times=SNAPSHOTS, endpoint_nodes=8192, circle_nodes=2048,
                  worker=args.worker, device=device, gpu=torch.cuda.get_device_name(device),
                  torch=str(torch.__version__), numpy=np.__version__, python=sys.version,
                  source_hashes=source_hashes(), command=sys.argv, cwd=str(Path.cwd()),
                  head=subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
                  started_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                  selection_rule="Both fitted and maximum endpoint refinement discrepancy > 0.01",
                  selected=selected, own_selected=own, older=str(args.older), newer=str(args.newer), level=args.level)
    config["workers"] = args.workers
    config["exclude_roots"] = list(map(str, args.exclude))
    save_json(config_path, config)
    print(json.dumps(dict(worker=args.worker, selected=own, rtol=rtol, atol=atol)), flush=True)
    start = time.monotonic()
    net = NetworkEngine(2, WIDTH, NETWORK_SEED, device=device, dtype=torch.float64, block_size=256)
    initial = net.initial_state()
    engines = {"full": (net, initial)}
    results = {}
    for record in own:
        key = record["key"]
        case = next(c for c in CASES_V2 if any(key == c + "_" + method for method in METHODS))
        method = key[len(case)+1:]
        if method not in engines:
            name, order = method.rsplit("_p", 1)
            engines[method] = build(initial, int(order), name)
        engine, state = engines[method]
        results[key] = trajectory(engine, state, CASES_V2[case], args.out/key, rtol, atol, start, args.budget)
        save_json(args.out / f"results_worker{args.worker}.json", results)
    save_json(args.out / f"completion_worker{args.worker}.json", dict(exit_status=0,
              seconds=time.monotonic()-start, fitted=sum(v["status"] == "fitted" for v in results.values()),
              total=len(results), finished_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())))


if __name__ == "__main__":
    main()
