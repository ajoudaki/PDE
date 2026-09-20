"""Deterministic CUDA implementation checks; no training or accuracy campaign.

Predeclared contract: cuda:1, float64, widths 256/2048, network seeds 105/117,
dictionary seed 7319 plus one independence check at 7320. Old p=1,3,5 must
reproduce the frozen old builder; p=6,7,9 raw outputs must match a separate
interpreter of every maintained word. All new orders must have exact counts,
finite diagnostics, unit-RMS Gaussian columns, orthonormal QR columns, nested
random spans/prefixes, correct initial forward/reverse contractions, and the
maintained state contract. Triangular-solve metadata must be finite and at most
1e-8 for ours, and None for controls. Tolerance 2e-11 (ridge identity 2e-9); exact legacy
comparisons use zero tolerance. A full-basis width-64 oracle checks the engine.
One execution, at most 60 seconds after CUDA setup, 1 GiB allocated tensor
memory. A failed gate is an implementation failure, not scientific evidence
about trained accuracy or order convergence. No adaptive experiment branch.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time
import traceback

from benchmark import ClosureEngine, NetworkEngine, ROOT, TensorState, setup
from diverse_dictionary import dictionaries as old_dictionaries
from scaling_dictionary import (APPENDED_DIMENSIONS, APPENDED_SEED_OFFSET, DICTIONARY_SEED,
                                DIMENSIONS, LEGACY_DIMENSIONS, METHODS, ORDERS, build,
                                build_dictionary, dictionaries, dictionary_metadata,
                                raw_observable_values)
import torch


def interpreted_values(initial, words):
    """Independent whole-DAG interpreter; no polynomial-core fast path."""
    cache = {}
    for target in words:
        pending = [target]
        while pending:
            word = pending[-1]
            if word in cache:
                pending.pop()
                continue
            missing = next((child for child in word.args if child not in cache), None)
            if missing is not None:
                pending.append(missing)
                continue
            arguments = [cache[child] for child in word.args]
            if word.op == "one":
                value = torch.ones_like(initial.c)
            elif word.op in ("g1", "g2"):
                value = initial.w[:, int(word.op[-1]) - 1]
            elif word.op == "action":
                value = (initial.M if word.population == 2 else initial.M.T) @ arguments[0]
            elif word.op in ("sin", "cos", "tanh"):
                value = getattr(torch, word.op)(arguments[0])
            elif word.op == "scale":
                value = float(word.scalar) * arguments[0]
            elif word.op == "add":
                value = arguments[0] + arguments[1]
            elif word.op == "multiply":
                value = arguments[0] * arguments[1]
            else:
                raise ValueError(word.op)
            cache[word] = value
            pending.pop()
    return torch.stack([cache[word] for word in words], dim=1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True, type=Path, help="fresh run directory")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    sources = [Path(__file__), Path(__file__).with_name("scaling_dictionary.py"),
               Path(__file__).with_name("diverse_dictionary.py"),
               Path(__file__).with_name("benchmark.py"),
               *(ROOT / "code" / "pde" / name for name in (
                   "finite_torch.py", "finite_network.py", "observable_initialization.py",
                   "observable_words.py", "observable_torch_p1.py"))]
    report = {
        "passed": False, "scope": "finite initialized dictionary implementation; no training",
        "command": [sys.executable, "-B", *sys.argv], "cwd": str(Path.cwd()),
        "orders": list(ORDERS), "nominal_dimensions": DIMENSIONS,
        "network_seeds_by_width": {"256": 105, "2048": 117},
        "dictionary_seed": DICTIONARY_SEED, "budget_seconds": 60,
        "source_hashes": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in sources},
        "environment": {key: os.environ.get(key) for key in (
            "PYTHONDONTWRITEBYTECODE", "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS",
            "MKL_NUM_THREADS", "CUBLAS_WORKSPACE_CONFIG")},
        "checks": {}, "metadata": {},
    }
    device, start = None, None
    try:
        device = setup("cuda:1")
        torch.cuda.set_per_process_memory_fraction(0.04, device)
        torch.cuda.reset_peak_memory_stats(device)
        torch.cuda.synchronize(device)
        start = time.monotonic()

        def budget():
            torch.cuda.synchronize(device)
            if time.monotonic() - start > 60:
                raise RuntimeError("60-second validation budget exhausted")
            if torch.cuda.max_memory_allocated(device) > 1024**3:
                raise RuntimeError("1-GiB validation allocation budget exhausted")

        def compare(name, actual, expected, tolerance=2e-11):
            if actual.shape != expected.shape:
                raise AssertionError((name, tuple(actual.shape), tuple(expected.shape)))
            error = float((actual - expected).abs().max())
            report["checks"][name] = {"max_absolute_error": error, "tolerance": tolerance}
            if not math.isfinite(error) or error > tolerance:
                raise AssertionError((name, error, tolerance))

        def reject(name, operation):
            try:
                operation()
            except ValueError:
                report["checks"][name] = {"rejected": True}
            else:
                raise AssertionError(name + " accepted invalid input")

        # Independent full-basis finite-network oracle, including one solver step.
        net = NetworkEngine(2, 64, 105, device=device, dtype=torch.float64)
        initial = net.initial_state()
        identity = 8 * torch.eye(64, device=device, dtype=torch.float64)
        exact = ClosureEngine(identity, initial.w, identity, initial.M,
                              device=device, dtype=torch.float64)
        inputs = torch.tensor([[1., 0.], [.6, .8]], device=device, dtype=torch.float64)
        data = net.prepare_data(inputs, [1., -.4])
        compare("full_basis_prediction", net.predict(initial, inputs), exact.predict(initial, inputs))
        for label, left, right in (
                ("rhs", net.rhs(initial, data), exact.rhs(initial, data)),
                ("step", net.heun_step(initial, data, .01), exact.heun_step(initial, data, .01))):
            for key in ("w", "c", "M"):
                compare(f"full_basis_{label}_{key}", getattr(left, key), getattr(right, key))

        for width, network_seed in ((256, 105), (2048, 117)):
            budget()
            net = NetworkEngine(2, width, network_seed, device=device, dtype=torch.float64)
            initial = net.initial_state()
            original = initial.clone()
            for order in (1, 3, 5):
                for method in METHODS:
                    current = dictionaries(initial, order, method)
                    legacy = old_dictionaries(initial, order, method)
                    for layer, (actual, expected) in enumerate(zip(current, legacy)):
                        compare(f"legacy_n{width}_{method}_p{order}_{layer}", actual, expected, 0)
            reject(f"bad_order_n{width}", lambda: dictionaries(initial, 2, "ours"))
            reject(f"bool_seed_n{width}", lambda: dictionaries(initial, 1, "gaussian", True))
            if width == 256:
                reject("insufficient_width_qr", lambda: dictionaries(initial, 9, "orthogonal"))
            else:
                cached = {}
                for order in ORDERS:
                    budget()
                    definition = build_dictionary(order)
                    actual_counts = (len(definition.first_words), len(definition.second_words))
                    if actual_counts != DIMENSIONS[order]:
                        raise AssertionError((order, actual_counts))
                    report["checks"][f"counts_p{order}"] = {"actual": actual_counts}
                    if order in (6, 7, 9):
                        raw = raw_observable_values(initial, order)
                        for layer, (values, words) in enumerate(zip(raw,
                                (definition.first_words, definition.second_words))):
                            compare(f"maintained_words_p{order}_{layer}", values,
                                    interpreted_values(initial, words))
                    for method in METHODS:
                        engine, state = build(initial, order, method)
                        bases = (engine.b1, engine.b2)
                        cached[method, order] = bases
                        compare(f"readout_{method}_p{order}", state.c, initial.c, 0)
                        compare(f"weights_{method}_p{order}", state.w, initial.w, 0)
                        if state.w.data_ptr() == initial.w.data_ptr() or state.c.data_ptr() == initial.c.data_ptr():
                            raise AssertionError("builder must own its moving state")
                        compare(f"projection_{method}_p{order}", state.M,
                                engine.b2.T @ (initial.M @ engine.b1) / width)
                        first = torch.tanh(state.w @ inputs.T)
                        projected_first = engine.b1 @ (engine.b1.T @ first / width)
                        forward = engine.b2 @ (state.M @ (engine.b1.T @ first / width))
                        compare(f"forward_{method}_p{order}", forward,
                                engine.b2 @ (engine.b2.T @ (initial.M @ projected_first) / width))
                        delta = torch.cos(initial.w @ inputs.T)
                        projected_delta = engine.b2 @ (engine.b2.T @ delta / width)
                        reverse = engine.b1 @ (state.M.T @ (engine.b2.T @ delta / width))
                        compare(f"reverse_{method}_p{order}", reverse,
                                engine.b1 @ (engine.b1.T @ (initial.M.T @ projected_delta) / width))
                        compare(f"prediction_{method}_p{order}", engine.predict(state, inputs),
                                state.c @ forward.tanh() / width)
                        data = engine.prepare_data(inputs, [1., -.4])
                        # Perturb c to ensure reverse derivatives are not hidden by 1/n readout.
                        perturbed = TensorState(state.w + .07, state.c + .3, state.M + .02)
                        optimized = engine.rhs(perturbed, data)
                        reference = engine.rhs(perturbed, data, implementation="reference")
                        for key in ("w", "c", "M"):
                            compare(f"rhs_{method}_p{order}_{key}",
                                    getattr(optimized, key), getattr(reference, key))
                        metadata = dictionary_metadata(initial, order, method, bases=bases)
                        report["metadata"][f"{method}_p{order}"] = metadata
                        for layer, population in enumerate(metadata["populations"]):
                            residual = population["triangular_solve_residual"]
                            name = f"triangular_solve_metadata_{method}_p{order}_{layer}"
                            if method == "ours":
                                report["checks"][name] = {
                                    "max_absolute_error": residual, "tolerance": 1e-8}
                                if not math.isfinite(residual) or residual > 1e-8:
                                    raise AssertionError((name, residual, 1e-8))
                            else:
                                if residual is not None:
                                    raise AssertionError((name, residual))
                                report["checks"][name] = {"not_applicable": True}
                        for layer, basis in enumerate(bases):
                            if method == "gaussian":
                                compare(f"gaussian_rms_p{order}_{layer}", basis.square().mean(0),
                                        torch.ones(basis.shape[1], device=device, dtype=torch.float64))
                            elif method == "orthogonal":
                                compare(f"orthogonal_gram_p{order}_{layer}", basis.T @ basis / width,
                                        torch.eye(basis.shape[1], device=device, dtype=torch.float64))
                    if order in (6, 7, 9):
                        for layer, (values, basis) in enumerate(zip(raw, cached["ours", order])):
                            ridge = 1 / (1024 * (order + 1)**2)
                            eye = torch.eye(values.shape[1], device=device, dtype=torch.float64)
                            lower = torch.linalg.cholesky(values.T @ values / width + ridge * eye)
                            inverse = torch.linalg.solve_triangular(lower, eye, upper=False)
                            compare(f"transpose_solve_p{order}_{layer}", basis, values @ inverse.T)
                            compare(f"ridge_identity_p{order}_{layer}",
                                    basis.T @ basis / width + ridge * (inverse @ inverse.T), eye, 2e-9)
                for order in ORDERS:
                    budget()
                    for layer, (gaussian, orthogonal) in enumerate(zip(cached["gaussian", order],
                                                                      cached["orthogonal", order])):
                        compare(f"random_same_span_p{order}_{layer}",
                                orthogonal @ (orthogonal.T @ gaussian / width), gaussian)
                        for method in ("gaussian", "orthogonal"):
                            basis = cached[method, order][layer]
                            maximal = cached[method, 9][layer][:, :basis.shape[1]]
                            if method == "orthogonal":
                                maximal = maximal * (maximal * basis).sum(0).sign()
                            compare(f"nested_{method}_p{order}_{layer}", basis, maximal)
                for layer, basis in enumerate(cached["gaussian", 9]):
                    generator = torch.Generator(device=device).manual_seed(DICTIONARY_SEED + layer)
                    first = torch.randn((width, LEGACY_DIMENSIONS[layer]), generator=generator,
                                        device=device, dtype=torch.float64)
                    generator.manual_seed(DICTIONARY_SEED + APPENDED_SEED_OFFSET + layer)
                    extra = torch.randn((width, APPENDED_DIMENSIONS[layer]), generator=generator,
                                        device=device, dtype=torch.float64)
                    raw_random = torch.cat((first, extra), 1)
                    compare(f"fixed_append_protocol_{layer}", basis,
                            raw_random / raw_random.square().mean(0).sqrt(), 0)
                alternative = dictionaries(initial, 1, "gaussian", DICTIONARY_SEED + 1)
                differences = [float((a-b).abs().max()) for a, b in
                               zip(alternative, cached["gaussian", 1])]
                if min(differences) <= 1:
                    raise AssertionError("dictionary_seed did not change both independent blocks")
                report["checks"]["dictionary_seed_changes_random_basis"] = {"max_differences": differences}
                for layer, basis in enumerate(dictionaries(initial, 1, "ours", DICTIONARY_SEED + 1)):
                    compare(f"ours_ignores_dictionary_seed_{layer}", basis, cached["ours", 1][layer], 0)
            for key in ("w", "c", "M"):
                compare(f"initial_preserved_n{width}_{key}", getattr(initial, key), getattr(original, key), 0)
        budget()
        report["passed"] = True
    except Exception:
        report["failure"] = traceback.format_exc()
        raise
    finally:
        if device is not None:
            torch.cuda.synchronize(device)
            report.update(device=device, gpu=torch.cuda.get_device_name(device),
                          torch_version=str(torch.__version__),
                          cuda_peak_allocated_bytes=torch.cuda.max_memory_allocated(device))
        if start is not None:
            report["work_seconds"] = time.monotonic() - start
        (args.out / "validation.json").write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    errors = [v["max_absolute_error"] for v in report["checks"].values() if "max_absolute_error" in v]
    print(json.dumps({"passed": True, "checks": len(report["checks"]),
                      "max_error": max(errors), "work_seconds": report["work_seconds"],
                      "out": str(args.out / "validation.json")}))


if __name__ == "__main__":
    main()
