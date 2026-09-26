"""Bounded, archived-initialization comparison; see COMPARISON_PROTOCOL.md."""
import os
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
import zipfile

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OLD = ROOT / "studies/random_dictionary_learned_circle_20260920"
ARCHIVE = ROOT / "data/generated/random_dictionary_learned_circle_20260920"
sys.path.insert(0, str(ROOT / "code"))
sys.path.insert(0, str(OLD))
from benchmark import setup, polynomial_values, save_json
from diverse_benchmark import trajectory
from diverse_cases import CASES_V2
from pde.observable_initialization import build_dictionary
from pde.observable_torch_p1 import ClosureEngine, TensorState
from new_dictionary import build as build_new

CASES = {k: CASES_V2[k] for k in ("quadrant_pairs", "two_outliers_alternating")}
METHODS = ("new_p1", "new_p2", "new_p3", "old_p2")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for block in iter(lambda: handle.read(8*1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read_initial(path, device):
    """Read first snapshots only, without materializing the dense history."""
    values = []
    with zipfile.ZipFile(path) as archive:
        for name in ("w", "c", "M"):
            with archive.open(name + ".npy") as handle:
                version = np.lib.format.read_magic(handle)
                reader = (np.lib.format.read_array_header_1_0 if version == (1, 0)
                          else np.lib.format.read_array_header_2_0)
                shape, fortran, dtype = reader(handle)
                if fortran or dtype != np.dtype("float64") or len(shape) < 2:
                    raise ValueError("unexpected archived snapshot representation")
                count = int(np.prod(shape[1:]))
                raw = handle.read(count * dtype.itemsize)
                array = np.frombuffer(raw, dtype=dtype).reshape(shape[1:]).copy()
                values.append(torch.tensor(array, device=device, dtype=torch.float64))
    return TensorState(*values)


@torch.no_grad()
def old_build(initial, p):
    definition = build_dictionary(p)
    if p not in (1, 2, 3) or definition.first_tail or definition.second_tail:
        raise ValueError("expected the unmodified old low-order cores")
    n = len(initial.w)
    h = initial.w.tanh()
    H = (initial.M @ h).tanh()
    coordinates = (torch.cat((h, (initial.M.T @ H).tanh()), 1), H)
    bases, diagnostics = [], []
    eta = 1 / (1024*(p+1)**2)
    for x, powers in zip(coordinates, (definition.first_exponents, definition.second_exponents)):
        raw = polynomial_values(x, powers, p)
        gram = raw.T @ raw/n
        regularized = gram + eta*torch.eye(raw.shape[1], device=x.device, dtype=x.dtype)
        lower = torch.linalg.cholesky(regularized)
        b = torch.linalg.solve_triangular(lower, raw.T, upper=False).T.contiguous()
        spectrum = torch.linalg.eigvalsh(gram)
        residual = float((b @ lower.T-raw).norm()/raw.norm())
        condition = float(torch.linalg.cond(regularized))
        if condition > 1e10 or residual > 1e-8:
            raise ValueError("old dictionary numerical gate failed")
        diagnostics.append(dict(raw_eigenvalues=spectrum.cpu().tolist(),
            normalized_eigenvalues=torch.linalg.eigvalsh(b.T @ b/n).cpu().tolist(),
            numerical_rank=int((spectrum > spectrum[-1]*1e-10).sum()),
            regularized_condition=condition, triangular_residual=residual))
        bases.append(b)
    b1, b2 = bases
    M = b2.T @ (initial.M @ b1)/n
    engine = ClosureEngine(b1, initial.w, b2, M, device=initial.w.device,
                           dtype=torch.float64, block_size=256)
    return engine, engine.state(initial.w, initial.c, M), dict(
        family="old", p=p, K1=b1.shape[1], K2=b2.shape[1], ridge=eta,
        populations=diagnostics)


def hashes():
    paths = {Path(__file__).resolve(), HERE / "new_dictionary.py", HERE / "COMPARISON_PROTOCOL.md"}
    for module in list(sys.modules.values()):
        value = getattr(module, "__file__", None)
        if value:
            path = Path(value).resolve()
            if path.suffix == ".py" and (ROOT / "code" in path.parents or OLD in path.parents):
                paths.add(path)
    return {str(p.relative_to(ROOT)): sha(p) for p in sorted(paths)}


@torch.no_grad()
def preflight(initial, directory, device):
    checks = {}
    for p in (1, 3):
        engine, state, metadata = old_build(initial, p)
        path = ARCHIVE / "scaling_width4096_refined01" / f"quadrant_pairs_ours_p{p}" / "arrays.npz"
        with np.load(path, allow_pickle=False) as archived:
            for key in ("b1", "b2", "D"):
                delta = float((getattr(engine, key)-torch.tensor(archived[key], device=device)).abs().max())
                checks[f"old_p{p}_{key}"] = delta
                assert delta <= 1e-10
            for key in ("w", "c", "M"):
                delta = float((getattr(state, key)-torch.tensor(archived[key][0], device=device)).abs().max())
                checks[f"old_p{p}_{key}0"] = delta
                assert delta <= 1e-10
            grid = torch.tensor(archived["circle_inputs"], device=device)
            delta = float((engine.predict(state, grid)-torch.tensor(archived["circle_predictions"][0], device=device)).abs().max())
            checks[f"old_p{p}_initial_prediction"] = delta
            assert delta <= 1e-10
    other_path = ARCHIVE / "scaling_width4096_refined01/two_outliers_alternating_full/arrays.npz"
    other = read_initial(other_path, device)
    for key in ("w", "c", "M"):
        checks["shared_initial_"+key] = float((getattr(initial, key)-getattr(other, key)).abs().max())
        assert checks["shared_initial_"+key] == 0
    for method in METHODS:
        p = int(method[-1])
        engine, state, metadata = build_new(initial, p, block_size=256) if method.startswith("new") else old_build(initial, p)
        checks[method] = metadata
        assert torch.equal(state.w, initial.w) and torch.equal(state.c, initial.c)
        assert (engine.K1, engine.K2) == ({1:(2,4),2:(2,4),3:(6,12)}[p] if method.startswith("new") else (15,6))
    save_json(directory / "validation.json", dict(passed=True, checks=checks, source_hashes=hashes()))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--device", required=True)
    parser.add_argument("--worker", type=int, choices=(0,1), default=0)
    parser.add_argument("--level", type=int, choices=(0,1,2), default=0)
    parser.add_argument("--budget", type=float, default=400)
    parser.add_argument("--only", nargs="+", choices=METHODS)
    parser.add_argument("--preflight", action="store_true")
    args = parser.parse_args()
    if not 0 < args.budget <= 400:
        parser.error("budget must be in (0,400]")
    setup(args.device)
    start = time.monotonic()
    args.out.mkdir(parents=True, exist_ok=not args.preflight)
    config_path = args.out / f"config_worker{args.worker}.json"
    if config_path.exists():
        raise FileExistsError(config_path)
    initial_path = ARCHIVE / "scaling_width4096_refined01/quadrant_pairs_full/arrays.npz"
    initial = read_initial(initial_path, args.device)
    rtol, atol = 6.25e-5/4**args.level, 6.25e-7/4**args.level
    config = dict(cases=CASES, width=4096, network_seed=20260920, threshold=1e-3,
        methods=args.only or METHODS, orders=[1,2,3], device=args.device,
        gpu=torch.cuda.get_device_name(args.device), dtype="float64", rtol=rtol, atol=atol,
        level=args.level, worker=args.worker, worker_limit_seconds=args.budget,
        per_trajectory_limit_seconds=180, max_time=10000, max_steps=30000,
        initial_step=.05, max_step=2, min_step=1e-7, block_size=256,
        initial_archive=str(initial_path.relative_to(ROOT)), initial_archive_sha256=sha(initial_path),
        initial_array_sha256={k:hashlib.sha256(getattr(initial,k).cpu().numpy().tobytes()).hexdigest() for k in ("w","c","M")},
        torch=str(torch.__version__), numpy=np.__version__, python=sys.version,
        source_hashes=hashes(), command=sys.argv, cwd=str(Path.cwd()),
        head=subprocess.check_output(["git","rev-parse","HEAD"], cwd=ROOT, text=True).strip(),
        started_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()))
    save_json(config_path, config)
    if args.preflight:
        preflight(initial, args.out, args.device)
        seconds = time.monotonic()-start
        save_json(args.out / "completion.json", dict(seconds=seconds, passed=True))
        print(json.dumps(dict(preflight="PASS", seconds=seconds)), flush=True)
        return
    name, case = list(CASES.items())[args.worker]
    results = {}
    for method in args.only or METHODS:
        if time.monotonic()-start >= args.budget:
            break
        p = int(method[-1])
        engine, state, metadata = build_new(initial, p, block_size=256) if method.startswith("new") else old_build(initial, p)
        key = name+"_"+method
        save_json(args.out / (key+"_dictionary.json"), metadata)
        results[key] = trajectory(engine, state, case, args.out/key, rtol, atol, start, args.budget)
        results[key]["declared_executed"] = True
        save_json(args.out / f"results_worker{args.worker}.json", results)
    torch.cuda.synchronize(args.device)
    completion = dict(seconds=time.monotonic()-start, fitted=sum(r["status"]=="fitted" for r in results.values()),
        total=len(results), expected=len(args.only or METHODS), exit_status=0,
        finished_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()))
    save_json(args.out / f"completion_worker{args.worker}.json", completion)
    print(json.dumps(completion), flush=True)


if __name__ == "__main__":
    main()
