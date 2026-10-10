"""Finite-carrier initialized dictionaries and maintained closure execution.

Study-owned extraction of the 2026-09-20 scaling dictionary, with CPU support
and the maintained p=2,p=4 word definitions added (no historical results for
those orders). Requires PYTHONPATH=code and Torch. No import from an old study.

Order p selects features; n is the supplied dense network's carrier width.
Both populations have n rows here. This is not independent population-law
quadrature, sparse carrier selection, Legendre memory, or a fitted-data basis.
Random numbers preserve the scaling campaign's fixed legacy/appended draw
shapes on the same device; CPU and CUDA streams need not coincide.
"""
from functools import lru_cache
import math
import operator

import torch

from dataclasses import dataclass

from pde.observable_initialization import build_dictionary
from pde.observable_torch_p1 import ClosureEngine, TensorState, initialize_p1

DICTIONARY_SEED = 7319


ORDERS = tuple(range(1, 10))
HISTORICAL_ORDERS = (1, 3, 5, 6, 7, 8, 9)
METHODS = ("ours", "gaussian", "orthogonal")
DIMENSIONS = {1: (5, 3), 2: (15, 6), 3: (35, 10), 4: (71, 15), 5: (128, 21), 6: (213, 28),
              7: (333, 36), 8: (499, 45), 9: (720, 55)}
LEGACY_DIMENSIONS = (128, 21)
MAX_DIMENSIONS = DIMENSIONS[9]
APPENDED_DIMENSIONS = tuple(b-a for a, b in zip(LEGACY_DIMENSIONS, MAX_DIMENSIONS))
APPENDED_SEED_OFFSET = 100000
GRAM_RANK_RTOL = 1e-10


def initialize_population_p1(d, population_nodes, seed, *, device="cpu",
                             block_size=256, population_rule="iid", folded=False,
                             **initialization_options):
    """Maintained general-d first-order population closure, with zero readout.

    This independently samples joint population marks; population_nodes is not
    a neural width. In the default unfolded representation K1=1+2d,K2=1+d.
    Scalar coefficient quadrature and optional antithetic/folding settings pass
    unchanged to the maintained initializer. It supplies no general-d trained
    network approximation guarantee. Returned engine methods match build().
    """
    return initialize_p1(d, population_nodes, seed, device=device,
                         dtype=torch.float64, block_size=block_size,
                         population_rule=population_rule, folded=folded,
                         **initialization_options)


def polynomial_values(coordinates, exponents, order):
    terms = [torch.ones_like(coordinates), coordinates]
    for _ in range(1, order):
        terms.append(2 * coordinates * terms[-1] - terms[-2])
    columns = []
    for powers in exponents:
        v = torch.ones(len(coordinates), dtype=coordinates.dtype, device=coordinates.device)
        for j, degree in enumerate(powers):
            v = v * terms[degree][:, j]
        columns.append(v)
    return torch.stack(columns, dim=1)


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


@lru_cache(maxsize=len(ORDERS))
def _compiled_definition(order):
    definition = build_dictionary(order)
    if (len(definition.first_words), len(definition.second_words)) != DIMENSIONS[order]:
        raise ValueError("maintained dictionary dimensions changed")
    return definition


def _definition(initial, order):
    if isinstance(order, bool) or not isinstance(order, int) or order not in ORDERS:
        raise ValueError("order must be an integer from 1 through 9")
    if not isinstance(initial, TensorState):
        raise ValueError("initial must be a TensorState")
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


@dataclass(frozen=True)
class Endpoint:
    """A bounded numerical endpoint, not an infinite-training limit."""

    state: TensorState
    time: float
    loss: float
    threshold: float
    steps: int
    status: str


@torch.no_grad()
def fit_endpoint(engine, state, data, *, step_size, max_steps, threshold=1e-3):
    """Stop at a detected MSE crossing or after an explicit Heun-step budget.

    Each accepted step is simultaneous Heun from the maintained engine. On
    the first bracketed crossing, bisect its parameter chord 40 times, retaining
    the below-threshold endpoint. This does not certify the earliest crossing
    of the continuous ODE or a nonmonotone within-step interpolant. A missed
    threshold is returned as 'step_cap', and is ineligible for endpoint_errors.
    This small fixed-step driver does not recreate the adaptive campaigns.
    """
    if isinstance(max_steps, bool) or not isinstance(max_steps, int) or max_steps < 0:
        raise ValueError("max_steps must be a nonnegative integer")
    if isinstance(step_size, bool) or not math.isfinite(float(step_size)) or step_size <= 0:
        raise ValueError("step_size must be finite and positive")
    if isinstance(threshold, bool) or not math.isfinite(float(threshold)) or threshold <= 0:
        raise ValueError("threshold must be finite and positive")
    engine.validate_state(state)
    current = state.clone()
    loss = float(engine.loss(current, data))
    if loss <= threshold:
        return Endpoint(current, 0.0, loss, float(threshold), 0, "fitted")
    h = float(step_size)
    for step in range(1, max_steps + 1):
        candidate = engine.heun_step(current, data, h)
        loss = float(engine.loss(candidate, data))
        if loss <= threshold:
            lo, hi = 0.0, 1.0
            for _ in range(40):
                fraction = (lo + hi) / 2
                middle = TensorState(*(getattr(current, k) + fraction *
                                     (getattr(candidate, k) - getattr(current, k))
                                     for k in ("w", "c", "M")))
                if float(engine.loss(middle, data)) <= threshold:
                    hi = fraction
                else:
                    lo = fraction
            current = TensorState(*(getattr(current, k) + hi *
                                  (getattr(candidate, k) - getattr(current, k))
                                  for k in ("w", "c", "M")))
            loss = float(engine.loss(current, data))
            return Endpoint(current, (step - 1 + hi) * h, loss, float(threshold),
                            step, "fitted")
        current = candidate
    return Endpoint(current, max_steps * h, loss, float(threshold), max_steps, "step_cap")


@torch.no_grad()
def endpoint_errors(engine, endpoint, reference_engine, reference_endpoint, inputs):
    """Uniform-panel errors between two independently stopped fitted predictors.

    Both endpoints must fit the same threshold. The supplied panel uses ordinary
    normalized input rows. The maximum is a sampled maximum, not a continuous
    supremum. Threshold metadata is checked, not taken as a convergence proof.
    """
    for end in (endpoint, reference_endpoint):
        if (not isinstance(end, Endpoint) or end.status != "fitted"
                or not math.isfinite(end.loss) or end.loss > end.threshold):
            raise ValueError("both predictors must have fitted endpoints")
    if endpoint.threshold != reference_endpoint.threshold:
        raise ValueError("compare endpoints at the same training-loss threshold")
    prediction = engine.predict(endpoint.state, inputs)
    reference = reference_engine.predict(reference_endpoint.state, inputs)
    difference = prediction - reference
    if not bool(torch.isfinite(difference).all()):
        raise ValueError("nonfinite endpoint difference")
    mse = float(difference.square().mean())
    if not math.isfinite(mse):
        raise ValueError("nonfinite endpoint mean square")
    return {"l1": float(difference.abs().mean()), "rms": math.sqrt(mse),
            "mse": mse, "sampled_max": float(difference.abs().max()),
            "panel_size": len(difference)}
