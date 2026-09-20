"""Finite-carrier p=1,3,5 dictionaries for the extended CUDA benchmark.

All retained initialized words are evaluated, including the redundant p=5
constant tails. Random controls share a maximal GPU draw in each population,
then take prefixes. This expands the random-draw protocol from benchmark.py;
the original p=1,3 experiment and its source remain unchanged.
"""
import math

import torch

from benchmark import ClosureEngine, DICTIONARY_SEED, build_dictionary, polynomial_values


ORDERS = (1, 3, 5)
METHODS = ("ours", "gaussian", "orthogonal")
DIMENSIONS = {1: (5, 3), 3: (35, 10), 5: (128, 21)}
MAX_DIMENSIONS = DIMENSIONS[5]


def _definition(initial, order):
    if isinstance(order, bool) or not isinstance(order, int) or order not in ORDERS:
        raise ValueError("the bounded benchmark supports integer orders 1, 3, 5")
    n = len(initial.w)
    arrays = (initial.w, initial.c, initial.M)
    if (initial.w.shape != (n, 2) or initial.c.shape != (n,)
            or initial.M.shape != (n, n)):
        raise ValueError("expected an equal-width two-input finite network state")
    if any(x.device != initial.w.device or x.dtype != torch.float64 for x in arrays):
        raise ValueError("the common network state must have one device and float64 dtype")
    if initial.w.device.type != "cuda":
        raise ValueError("the benchmark requires CUDA dictionary computation")
    if not all(bool(torch.isfinite(x).all()) for x in arrays):
        raise ValueError("the common network state must be finite")
    definition = build_dictionary(order)
    if (len(definition.first_words), len(definition.second_words)) != DIMENSIONS[order]:
        raise ValueError("maintained dictionary dimensions changed")
    return definition


@torch.no_grad()
def word_values(initial, words):
    """Interpret exact initialized-word syntax on this actual finite network."""
    cache = {}

    def evaluate(word):
        if word in cache:
            return cache[word]
        op = word.op
        if op == "one":
            value = torch.ones(len(initial.w), device=initial.w.device, dtype=initial.w.dtype)
        elif op in ("g1", "g2"):
            value = initial.w[:, int(op[-1]) - 1]
        elif op == "action":
            matrix = initial.M if word.population == 2 else initial.M.T
            value = matrix @ evaluate(word.args[0])
        elif op in ("sin", "cos", "tanh"):
            value = getattr(torch, op)(evaluate(word.args[0]))
        elif op == "scale":
            value = float(word.scalar) * evaluate(word.args[0])
        elif op == "add":
            value = evaluate(word.args[0]) + evaluate(word.args[1])
        elif op == "multiply":
            value = evaluate(word.args[0]) * evaluate(word.args[1])
        else:
            raise ValueError("unsupported initialized word: " + op)
        cache[word] = value
        return value

    if not words:
        return torch.empty((len(initial.w), 0), device=initial.w.device, dtype=initial.w.dtype)
    return torch.stack([evaluate(word) for word in words], dim=1)


@torch.no_grad()
def raw_observable_values(initial, order):
    """Exact retained polynomial words followed by every declared tail word."""
    definition = _definition(initial, order)
    lower = initial.w.tanh()
    upper = (initial.M @ lower).tanh()
    reverse = (initial.M.T @ upper).tanh()
    coordinates = (torch.cat((lower, reverse), dim=1), upper)
    result = []
    for x, exponents, tail in zip(coordinates,
            (definition.first_exponents, definition.second_exponents),
            (definition.first_tail, definition.second_tail)):
        core = polynomial_values(x, exponents, order)
        result.append(torch.cat((core, word_values(initial, tail)), dim=1).contiguous())
    return result


@torch.no_grad()
def dictionaries(initial, order, method):
    """Return frozen b1,b2, retaining nominal dimensions even with redundancy."""
    _definition(initial, order)
    if method not in METHODS:
        raise ValueError("unknown dictionary method: " + str(method))
    n, device = len(initial.w), initial.w.device
    if method == "ours":
        ridge = 1 / (1024 * (order + 1) ** 2)
        bases = []
        for raw in raw_observable_values(initial, order):
            gram = raw.T @ raw / n
            eye = torch.eye(raw.shape[1], device=device, dtype=raw.dtype)
            lower = torch.linalg.cholesky(gram + ridge * eye)
            # B=raw L^{-T}; solve avoids explicitly forming the inverse.
            bases.append(torch.linalg.solve_triangular(lower, raw.T, upper=False).T.contiguous())
        return bases
    ranks = DIMENSIONS[order]
    if method == "orthogonal" and n < max(ranks):
        raise ValueError("orthogonal controls need at least as many neurons as retained columns")
    bases = []
    for layer, (rank, maximal_rank) in enumerate(zip(ranks, MAX_DIMENSIONS)):
        generator = torch.Generator(device=device).manual_seed(DICTIONARY_SEED + layer)
        raw = torch.randn((n, maximal_rank), generator=generator,
                          device=device, dtype=torch.float64)[:, :rank]
        if method == "gaussian":
            basis = raw / raw.square().mean(dim=0).sqrt()
        else:
            basis = math.sqrt(n) * torch.linalg.qr(raw, mode="reduced")[0]
        bases.append(basis.contiguous())
    return bases


@torch.no_grad()
def build(initial, order, method):
    """Return the maintained engine and a state with the actual finite readout."""
    b1, b2 = dictionaries(initial, order, method)
    D = b2.T @ (initial.M @ b1) / len(initial.w)
    engine = ClosureEngine(b1, initial.w, b2, D, device=initial.w.device,
                           dtype=torch.float64, block_size=256)
    return engine, engine.state(initial.w, initial.c, D)
