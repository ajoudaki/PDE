"""Deterministic GPU oracles, without a training campaign."""
import argparse
from pathlib import Path
import json
import numpy as np
import torch
from benchmark import setup, NetworkEngine, ClosureEngine, TensorState, closure, dictionaries, polynomial_values, build_dictionary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    device = setup()
    checks = {}
    net = NetworkEngine(2, 64, 105, device=device, dtype=torch.float64)
    initial = net.initial_state()
    identity = 8 * torch.eye(64, device=device, dtype=torch.float64)
    exact = ClosureEngine(identity, initial.w, identity, initial.M, device=device, dtype=torch.float64)
    inputs = torch.tensor([[1., 0.], [.6, .8], [-.8, .6]], device=device, dtype=torch.float64)
    data = net.prepare_data(inputs, [1, -.4, -.7])

    def compare(name, a, b, tolerance=2e-11):
        err = float((a - b).abs().max())
        assert err <= tolerance, (name, err)
        checks[name] = err

    compare("full_basis_prediction", net.predict(initial, inputs), exact.predict(initial, inputs))
    a, b = net.rhs(initial, data), exact.rhs(initial, data)
    aa, bb = net.heun_step(initial, data, .01), exact.heun_step(initial, data, .01)
    for k in ("w", "c", "M"):
        compare("full_basis_rhs_" + k, getattr(a, k), getattr(b, k))
        compare("full_basis_step_" + k, getattr(aa, k), getattr(bb, k))
    for p in (1, 3):
        definition = build_dictionary(p)
        cache = {}
        def evaluate(word):
            if word in cache:
                return cache[word]
            op = word.op
            if op == "one":
                value = torch.ones(64, device=device, dtype=torch.float64)
            elif op in ("g1", "g2"):
                value = initial.w[:, int(op[-1])-1]
            elif op == "action":
                value = (initial.M if word.population == 2 else initial.M.T) @ evaluate(word.args[0])
            elif op == "tanh":
                value = evaluate(word.args[0]).tanh()
            elif op == "scale":
                value = float(word.scalar) * evaluate(word.args[0])
            elif op == "add":
                value = evaluate(word.args[0]) + evaluate(word.args[1])
            elif op == "multiply":
                value = evaluate(word.args[0]) * evaluate(word.args[1])
            else:
                raise ValueError(op)
            cache[word] = value
            return value
        lower = initial.w.tanh()
        upper = (initial.M @ lower).tanh()
        coords = (torch.cat((lower, (initial.M.T @ upper).tanh()), 1), upper)
        for layer, (x, exponents, words) in enumerate(zip(coords,
                (definition.first_exponents, definition.second_exponents),
                (definition.first_words, definition.second_words))):
            compare(f"maintained_word_values_{p}_{layer}", polynomial_values(x, exponents, p),
                    torch.stack([evaluate(word) for word in words], 1))
        for method in ("ours", "gaussian", "orthogonal"):
            engine, state = closure(initial, p, method)
            lifted = engine.b2 @ state.M @ engine.b1.T / 64
            independent = state.c @ torch.tanh(lifted @ torch.tanh(state.w @ inputs.T)) / 64
            compare(f"{method}_{p}_lifted_prediction", engine.predict(state, inputs), independent)
            a = engine.rhs(state, data, implementation="optimized")
            b = engine.rhs(state, data, implementation="reference")
            for k in ("w", "c", "M"):
                compare(f"{method}_{p}_rhs_{k}", getattr(a, k), getattr(b, k))
            # Non-initial state avoids a vacuous tiny-readout gradient check.
            c = (state.c + .3).requires_grad_()
            w = (state.w + .07).requires_grad_()
            M = (state.M + .02).requires_grad_()
            f = (c @ torch.tanh(engine.b2 @ M @ (engine.b1.T @ torch.tanh(w @ inputs.T) / 64))) / 64
            loss = ((f - data.labels)**2).mean()
            grads = torch.autograd.grad(loss, (w, c, M))
            velocity = engine.rhs(TensorState(w.detach(), c.detach(), M.detach()), data)
            for k, g, mobility in zip(("w", "c", "M"), grads, (64, 64, 1)):
                compare(f"{method}_{p}_autograd_{k}", getattr(velocity, k), -mobility*g)
            if method == "gaussian":
                for layer, B in enumerate((engine.b1, engine.b2)):
                    compare(f"gaussian_{p}_column_norm_{layer}", B.square().mean(0), torch.ones(B.shape[1], device=device))
            if method == "orthogonal":
                for layer, B in enumerate((engine.b1, engine.b2)):
                    compare(f"orthogonal_{p}_gram_{layer}", B.T @ B / 64, torch.eye(B.shape[1], device=device))
        G = dictionaries(initial, p, "gaussian")
        Q = dictionaries(initial, p, "orthogonal")
        for layer, (g, q) in enumerate(zip(G, Q)):
            compare(f"random_same_span_{p}_{layer}", q @ (q.T @ g) / 64, g)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    if args.out.exists():
        raise FileExistsError(args.out)
    args.out.write_text(json.dumps({"passed": True, "checks": checks}, indent=2) + "\n")
    print(json.dumps({"passed": True, "checks": len(checks), "max_error": max(checks.values())}))


if __name__ == "__main__":
    main()
