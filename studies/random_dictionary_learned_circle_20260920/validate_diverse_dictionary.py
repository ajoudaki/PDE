"""Deterministic CUDA checks for the p=1,3,5 adapter; no training campaign.

One width-256 seed, at most 120 seconds of validation work, GPU 1, float64.
Oracles use 2e-11 absolute tolerance; ridge Gram identities allow 2e-10.
Rank means singular values above 1e-10 times the largest singular value.
Only implementation correctness is tested, not comparative learned accuracy.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

from benchmark import (ClosureEngine, NetworkEngine, ROOT, TensorState,
                       dictionaries as original_dictionaries, setup)
import torch

from diverse_dictionary import (DICTIONARY_SEED, DIMENSIONS, MAX_DIMENSIONS,
                                METHODS, ORDERS, build, build_dictionary,
                                dictionaries, raw_observable_values)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    device = setup("cuda:1")
    torch.cuda.set_per_process_memory_fraction(0.04, device)
    start = time.monotonic()
    n = 256
    network_seed = 105
    net = NetworkEngine(2, n, network_seed, device=device, dtype=torch.float64)
    initial = net.initial_state()
    original = initial.clone()
    inputs = torch.tensor([[1., 0.], [.6, .8], [-.8, .6]], device=device, dtype=torch.float64)
    data = net.prepare_data(inputs, [1, -.4, -.7])
    checks, ranks, tail_records = {}, {}, {}

    def compare(name, a, b, tolerance=2e-11):
        if a.shape != b.shape:
            raise AssertionError((name, a.shape, b.shape))
        err = float((a - b).abs().max())
        if not math.isfinite(err) or err > tolerance:
            raise AssertionError((name, err, tolerance))
        checks[name] = {"max_absolute_error": err, "tolerance": tolerance}

    def rank_check(name, values, expected):
        singular = torch.linalg.svdvals(values)
        threshold = float(singular[0]) * 1e-10
        rank = int((singular > threshold).sum())
        if rank != expected:
            raise AssertionError((name, rank, expected))
        ranks[name] = {"rank": rank, "expected": expected,
                       "threshold": threshold, "singular_values": singular.cpu().tolist()}

    # Complete syntax interpreter is independent of the adapter's core/tail split.
    cache = {}

    def interpret(word):
        if word in cache:
            return cache[word]
        op = word.op
        if op == "one":
            value = torch.ones(n, device=device, dtype=torch.float64)
        elif op in ("g1", "g2"):
            value = initial.w[:, int(op[-1]) - 1]
        elif op == "action":
            value = (initial.M if word.population == 2 else initial.M.T) @ interpret(word.args[0])
        elif op == "sin":
            value = interpret(word.args[0]).sin()
        elif op == "cos":
            value = interpret(word.args[0]).cos()
        elif op == "tanh":
            value = interpret(word.args[0]).tanh()
        elif op == "scale":
            value = float(word.scalar) * interpret(word.args[0])
        elif op == "add":
            value = interpret(word.args[0]) + interpret(word.args[1])
        elif op == "multiply":
            value = interpret(word.args[0]) * interpret(word.args[1])
        else:
            raise ValueError(op)
        cache[word] = value
        return value

    full_basis = math.sqrt(n) * torch.eye(n, device=device, dtype=torch.float64)
    exact = ClosureEngine(full_basis, initial.w, full_basis, initial.M,
                          device=device, dtype=torch.float64)
    compare("full_basis_prediction", net.predict(initial, inputs), exact.predict(initial, inputs))
    full_rhs, exact_rhs = net.rhs(initial, data), exact.rhs(initial, data)
    full_step, exact_step = net.heun_step(initial, data, .01), exact.heun_step(initial, data, .01)
    for key in ("w", "c", "M"):
        compare("full_basis_rhs_" + key, getattr(full_rhs, key), getattr(exact_rhs, key))
        compare("full_basis_step_" + key, getattr(full_step, key), getattr(exact_step, key))

    random_bases = {}
    for order in ORDERS:
        if time.monotonic() - start > 120:
            raise RuntimeError("validation work budget exhausted")
        definition = build_dictionary(order)
        raw_values = raw_observable_values(initial, order)
        ours = dictionaries(initial, order, "ours")
        for layer, (raw, basis, words) in enumerate(zip(raw_values, ours,
                (definition.first_words, definition.second_words))):
            compare(f"maintained_word_values_{order}_{layer}", raw,
                    torch.stack([interpret(word) for word in words], dim=1))
            if raw.shape != (n, DIMENSIONS[order][layer]):
                raise AssertionError("nominal dimensions changed")
            expected_rank = len((definition.first_exponents, definition.second_exponents)[layer])
            rank_check(f"ours_raw_{order}_{layer}", raw, expected_rank)
            rank_check(f"ours_normalized_{order}_{layer}", basis, expected_rank)
            eye = torch.eye(raw.shape[1], device=device, dtype=torch.float64)
            ridge = 1 / (1024 * (order + 1) ** 2)
            lower = torch.linalg.cholesky(raw.T @ raw / n + ridge * eye)
            inverse = torch.linalg.solve_triangular(lower, eye, upper=False)
            compare(f"inverse_cholesky_transpose_{order}_{layer}", basis, raw @ inverse.T)
            compare(f"ridge_gram_identity_{order}_{layer}",
                    basis.T @ basis / n + ridge * (inverse @ inverse.T), eye, 2e-10)
        if order in (1, 3):
            for layer, old in enumerate(original_dictionaries(initial, order, "ours")):
                compare(f"original_observable_semantics_{order}_{layer}", ours[layer], old)
        if order == 5:
            if (definition.tail_codes != (4, 5) or len(definition.first_tail) != 2
                    or definition.second_tail):
                raise AssertionError("p=5 retained tail syntax changed")
            for index, expected in enumerate((math.sin(1), math.cos(1))):
                actual = raw_values[0][:, 126 + index]
                compare(f"p5_constant_tail_{index}", actual, torch.full_like(actual, expected))
                tail_records[str(index)] = {"code": definition.tail_codes[index],
                                            "value": float(actual[0]), "column": 126 + index}
        for method in METHODS:
            engine, state = build(initial, order, method)
            compare(f"{method}_{order}_actual_readout", state.c, initial.c, 0)
            compare(f"{method}_{order}_actual_first_weights", state.w, initial.w, 0)
            if state.c.data_ptr() == initial.c.data_ptr() or state.w.data_ptr() == initial.w.data_ptr():
                raise AssertionError("builder must copy the moving initial arrays")
            compare(f"{method}_{order}_projected_initialization", state.M,
                    engine.b2.T @ (initial.M @ engine.b1) / n)
            lifted = engine.b2 @ state.M @ engine.b1.T / n
            independent = state.c @ torch.tanh(lifted @ torch.tanh(state.w @ inputs.T)) / n
            compare(f"{method}_{order}_lifted_prediction", engine.predict(state, inputs), independent)
            # Nonzero perturbations prevent a tiny initial readout from hiding gradient bugs.
            w = (state.w + .07).requires_grad_()
            c = (state.c + .3).requires_grad_()
            M = (state.M + .02).requires_grad_()
            perturbed = TensorState(w.detach(), c.detach(), M.detach())
            optimized = engine.rhs(perturbed, data, implementation="optimized")
            reference = engine.rhs(perturbed, data, implementation="reference")
            f = c @ torch.tanh(engine.b2 @ M @ (engine.b1.T @ torch.tanh(w @ inputs.T) / n)) / n
            loss = ((f - data.labels) ** 2).mean()
            gradients = torch.autograd.grad(loss, (w, c, M))
            for key, gradient, mobility in zip(("w", "c", "M"), gradients, (n, n, 1)):
                compare(f"{method}_{order}_rhs_{key}", getattr(optimized, key), getattr(reference, key))
                compare(f"{method}_{order}_autograd_{key}", getattr(optimized, key), -mobility * gradient)
            if method != "ours":
                random_bases[method, order] = (engine.b1, engine.b2)
                for layer, basis in enumerate((engine.b1, engine.b2)):
                    rank_check(f"{method}_{order}_{layer}", basis, DIMENSIONS[order][layer])
                    if method == "gaussian":
                        compare(f"gaussian_{order}_column_norm_{layer}", basis.square().mean(0),
                                torch.ones(basis.shape[1], device=device, dtype=torch.float64))
                    else:
                        compare(f"orthogonal_{order}_gram_{layer}", basis.T @ basis / n,
                                torch.eye(basis.shape[1], device=device, dtype=torch.float64))
        for layer, (gaussian, orthogonal) in enumerate(zip(random_bases["gaussian", order],
                                                         random_bases["orthogonal", order])):
            compare(f"random_same_span_{order}_{layer}", orthogonal @ (orthogonal.T @ gaussian) / n, gaussian)
            generator = torch.Generator(device=device).manual_seed(DICTIONARY_SEED + layer)
            raw = torch.randn((n, MAX_DIMENSIONS[layer]), generator=generator,
                              device=device, dtype=torch.float64)[:, :DIMENSIONS[order][layer]]
            compare(f"random_draw_protocol_{order}_{layer}", gaussian,
                    raw / raw.square().mean(0).sqrt())
    for method in ("gaussian", "orthogonal"):
        for order in (1, 3):
            for layer, basis in enumerate(random_bases[method, order]):
                maximal = random_bases[method, 5][layer][:, :basis.shape[1]]
                if method == "orthogonal":
                    # QR column signs are implementation conventions; compare matched signs.
                    signs = (maximal * basis).sum(0).sign()
                    maximal = maximal * signs
                compare(f"{method}_nested_{order}_{layer}", basis, maximal)
    for key in ("w", "c", "M"):
        compare("common_initial_state_preserved_" + key, getattr(initial, key), getattr(original, key), 0)
    torch.cuda.synchronize(device)
    elapsed = time.monotonic() - start
    if elapsed > 120:
        raise RuntimeError("validation work budget exhausted")
    sources = [Path(__file__), Path(__file__).with_name("diverse_dictionary.py"),
               Path(__file__).with_name("benchmark.py"),
               *(ROOT / "code" / "pde" / name for name in (
                   "finite_torch.py", "finite_network.py", "observable_initialization.py",
                   "observable_words.py", "observable_torch_p1.py"))]
    report = {"passed": True, "scope": "finite dictionary/RHS implementation only; no training",
              "device": device, "gpu": torch.cuda.get_device_name(device),
              "torch_version": str(torch.__version__), "width": n, "network_seed": network_seed,
              "dictionary_seed": DICTIONARY_SEED, "orders": ORDERS,
              "nominal_dimensions": DIMENSIONS, "checks": checks, "ranks": ranks,
              "p5_tail": tail_records, "work_seconds": elapsed,
              "cuda_peak_allocated_bytes": torch.cuda.max_memory_allocated(device),
              "command": sys.argv, "environment": {key: os.environ.get(key) for key in
                  ("PYTHONDONTWRITEBYTECODE", "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS",
                   "MKL_NUM_THREADS", "CUBLAS_WORKSPACE_CONFIG")},
              "source_hashes": {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                                for path in sources}}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("x") as handle:
        json.dump(report, handle, indent=2, allow_nan=False)
        handle.write("\n")
    print(json.dumps({"passed": True, "checks": len(checks), "rank_checks": len(ranks),
                      "max_error": max(value["max_absolute_error"] for value in checks.values()),
                      "work_seconds": elapsed, "out": str(args.out)}))


if __name__ == "__main__":
    main()
