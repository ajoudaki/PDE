"""Frozen finite-carrier dictionaries for the bounded width/order extension.

Only initialized arrays enter this adapter. The maintained polynomial words,
all declared tails, ridge 1/[1024(p+1)^2], inverse-Cholesky transpose, and
ClosureEngine dynamics are unchanged. Width and network seed belong to the
supplied initial state. This does not assert a population or order limit.

At the default dictionary seed, the first random blocks reproduce
diverse_dictionary.py exactly. Higher orders append independent blocks with
fixed p=9 shapes; neither draw shape depends on the requested order.
"""
from functools import lru_cache
import math
import operator

import torch

from benchmark import ClosureEngine, DICTIONARY_SEED, build_dictionary, polynomial_values
from diverse_dictionary import word_values


ORDERS = (1, 3, 5, 6, 7, 8, 9)
METHODS = ("ours", "gaussian", "orthogonal")
DIMENSIONS = {1: (5, 3), 3: (35, 10), 5: (128, 21), 6: (213, 28),
              7: (333, 36), 8: (499, 45), 9: (720, 55)}
LEGACY_DIMENSIONS = (128, 21)
MAX_DIMENSIONS = DIMENSIONS[9]
APPENDED_DIMENSIONS = tuple(b-a for a, b in zip(LEGACY_DIMENSIONS, MAX_DIMENSIONS))
APPENDED_SEED_OFFSET = 100000
GRAM_RANK_RTOL = 1e-10


@lru_cache(maxsize=len(ORDERS))
def _compiled_definition(order):
    definition = build_dictionary(order)
    if (len(definition.first_words), len(definition.second_words)) != DIMENSIONS[order]:
        raise ValueError("maintained dictionary dimensions changed")
    return definition


def _definition(initial, order):
    if isinstance(order, bool) or not isinstance(order, int) or order not in ORDERS:
        raise ValueError("supported integer orders are 1, 3, 5, 6, 7, 8, 9")
    arrays = (initial.w, initial.c, initial.M)
    if any(not isinstance(x, torch.Tensor) for x in arrays):
        raise ValueError("initial arrays must be Torch tensors")
    if initial.w.ndim != 2:
        raise ValueError("expected an equal-width two-input finite network state")
    n = len(initial.w)
    if (n < 1 or initial.w.shape != (n, 2) or initial.c.shape != (n,)
            or initial.M.shape != (n, n)):
        raise ValueError("expected an equal-width two-input finite network state")
    if any(x.device != initial.w.device or x.dtype != torch.float64 for x in arrays):
        raise ValueError("the common network state must have one device and float64 dtype")
    if initial.w.device.type != "cuda":
        raise ValueError("the benchmark requires CUDA dictionary computation")
    if not all(bool(torch.isfinite(x).all()) for x in arrays):
        raise ValueError("the common network state must be finite")
    return _compiled_definition(order)


def _seed(value):
    if isinstance(value, bool):
        raise ValueError("dictionary_seed must be a nonnegative integer")
    try:
        result = operator.index(value)
    except TypeError as exc:
        raise ValueError("dictionary_seed must be a nonnegative integer") from exc
    if not 0 <= result <= 2**64 - 2 - APPENDED_SEED_OFFSET:
        raise ValueError("dictionary_seed and both appended seeds must fit uint64")
    return result


@torch.no_grad()
def raw_observable_values(initial, order):
    """Polynomial core followed by every maintained retained tail word."""
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
    if not all(bool(torch.isfinite(x).all()) for x in result):
        raise ValueError("nonfinite initialized observable dictionary")
    return result


def _random_columns(initial, rank, layer, dictionary_seed):
    n, device = len(initial.w), initial.w.device
    generator = torch.Generator(device=device).manual_seed(dictionary_seed + layer)
    legacy = torch.randn((n, LEGACY_DIMENSIONS[layer]), generator=generator,
                         device=device, dtype=torch.float64)
    if rank <= LEGACY_DIMENSIONS[layer]:
        return legacy[:, :rank]
    generator.manual_seed(dictionary_seed + APPENDED_SEED_OFFSET + layer)
    appended = torch.randn((n, APPENDED_DIMENSIONS[layer]), generator=generator,
                           device=device, dtype=torch.float64)
    return torch.cat((legacy, appended), dim=1)[:, :rank]


@torch.no_grad()
def dictionaries(initial, order, method, dictionary_seed=DICTIONARY_SEED):
    """Return frozen b1,b2 with declared dimensions, retaining redundancy."""
    _definition(initial, order)
    dictionary_seed = _seed(dictionary_seed)
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
            # B=raw L^{-T}; preserve the original triangular solve exactly.
            bases.append(torch.linalg.solve_triangular(lower, raw.T, upper=False).T.contiguous())
    else:
        ranks = DIMENSIONS[order]
        if method == "orthogonal" and n < max(ranks):
            raise ValueError("orthogonal controls need at least as many neurons as retained columns")
        bases = []
        for layer, rank in enumerate(ranks):
            raw = _random_columns(initial, rank, layer, dictionary_seed)
            if method == "gaussian":
                basis = raw / raw.square().mean(dim=0).sqrt()
            else:
                basis = math.sqrt(n) * torch.linalg.qr(raw, mode="reduced")[0]
            bases.append(basis.contiguous())
    if not all(bool(torch.isfinite(x).all()) for x in bases):
        raise ValueError("nonfinite normalized dictionary")
    return bases


@torch.no_grad()
def build(initial, order, method, dictionary_seed=DICTIONARY_SEED):
    """Return maintained engine/state, retaining the actual finite readout."""
    b1, b2 = dictionaries(initial, order, method, dictionary_seed)
    D = b2.T @ (initial.M @ b1) / len(initial.w)
    engine = ClosureEngine(b1, initial.w, b2, D, device=initial.w.device,
                           dtype=torch.float64, block_size=256)
    return engine, engine.state(initial.w, initial.c, D)


@torch.no_grad()
def dictionary_metadata(initial, order, method, dictionary_seed=DICTIONARY_SEED, *, bases=None):
    """JSON-safe initialized diagnostics; no trajectory or fitting information.

    Optionally pass the matching engine's (b1,b2) to avoid rebuilding them.
    Eigenvalues are those of B.T@B/n. Numerical nonzero means greater than
    GRAM_RANK_RTOL times the largest eigenvalue; effective ranks use only these
    eigenvalues. This cutoff is a diagnostic, not a change to retained columns.
    Ridge condition refers to raw.T@raw/n + ridge*I for the observable method.
    Its triangular_solve_residual is max(abs(L@B.T-raw.T)) for that Gram's
    Cholesky factor L; random controls report None for this diagnostic.
    """
    definition = _definition(initial, order)
    dictionary_seed = _seed(dictionary_seed)
    if method not in METHODS:
        raise ValueError("unknown dictionary method: " + str(method))
    if bases is None:
        bases = dictionaries(initial, order, method, dictionary_seed)
    if len(bases) != 2:
        raise ValueError("expected exactly two dictionary bases")
    n = len(initial.w)
    raw_values = raw_observable_values(initial, order) if method == "ours" else (None, None)
    ridge = 1 / (1024 * (order + 1) ** 2) if method == "ours" else None
    populations = []
    for layer, (basis, raw, count, core, tails) in enumerate(zip(bases, raw_values,
            DIMENSIONS[order], (definition.first_exponents, definition.second_exponents),
            (definition.first_tail, definition.second_tail)), start=1):
        if (not isinstance(basis, torch.Tensor) or basis.shape != (n, count)
                or basis.dtype != initial.w.dtype or basis.device != initial.w.device):
            raise ValueError("supplied bases do not match the dictionary contract")
        gram = basis.T @ basis / n
        finite = bool(torch.isfinite(basis).all()) and bool(torch.isfinite(gram).all())
        if not finite:
            raise ValueError("nonfinite normalized dictionary or Gram")
        eigenvalues = torch.linalg.eigvalsh((gram + gram.T) / 2)
        cutoff = GRAM_RANK_RTOL * float(eigenvalues[-1])
        nonzero = eigenvalues[eigenvalues > cutoff]
        if not bool(torch.isfinite(eigenvalues).all()) or not len(nonzero):
            raise ValueError("nonfinite or zero normalized dictionary spectrum")
        fractions = nonzero / nonzero.sum()
        record = {
            "population": layer, "nominal_count": count, "core_count": len(core),
            "tail_count": len(tails), "normalized_gram_eigenvalues": eigenvalues.cpu().tolist(),
            "normalized_gram_nonzero_eigenvalues": nonzero.cpu().tolist(),
            "nonzero_eigenvalue_fractions": fractions.cpu().tolist(),
            "numerical_rank": len(nonzero), "eigenvalue_cutoff": cutoff,
            "nonzero_gram_condition": float(nonzero[-1] / nonzero[0]),
            "stable_rank": float(nonzero.sum() / nonzero[-1]),
            "participation_rank": float(1 / fractions.square().sum()),
            "entropy_effective_rank": float(torch.exp(-(fractions * fractions.log()).sum())),
            "ridge_condition": None,
            "triangular_solve_residual": None,
            "finite_checks": {"basis": True, "normalized_gram": True, "spectrum": True},
        }
        if raw is not None:
            raw_gram = raw.T @ raw / n
            lower = torch.linalg.cholesky(raw_gram + ridge * torch.eye(
                count, device=raw.device, dtype=raw.dtype))
            solve_residual = float((lower @ basis.T - raw.T).abs().max())
            if not math.isfinite(solve_residual):
                raise ValueError("nonfinite triangular solve residual")
            raw_eigenvalues = torch.linalg.eigvalsh((raw_gram + raw_gram.T) / 2)
            condition = float((raw_eigenvalues[-1] + ridge) / (raw_eigenvalues[0] + ridge))
            if (not bool(torch.isfinite(raw_eigenvalues).all())
                    or not math.isfinite(condition) or condition < 1):
                raise ValueError("invalid regularized raw Gram condition")
            record.update(ridge_condition=condition,
                          triangular_solve_residual=solve_residual,
                          raw_gram_min_eigenvalue=float(raw_eigenvalues[0]),
                          raw_gram_max_eigenvalue=float(raw_eigenvalues[-1]))
            record["finite_checks"].update(raw=True, raw_gram=True, ridge_condition=True,
                                          triangular_solve_residual=True)
        populations.append(record)
    return {"order": order, "method": method, "width": n,
            "dictionary_seed": dictionary_seed, "nominal_dimensions": list(DIMENSIONS[order]),
            "ridge": ridge, "gram_rank_rtol": GRAM_RANK_RTOL,
            "random_legacy_dimensions": list(LEGACY_DIMENSIONS),
            "random_appended_dimensions": list(APPENDED_DIMENSIONS),
            "random_appended_seed_offset": APPENDED_SEED_OFFSET,
            "tail_codes": list(definition.tail_codes), "populations": populations,
            "all_finite": True}
