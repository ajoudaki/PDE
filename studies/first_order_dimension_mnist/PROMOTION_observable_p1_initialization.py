"""First-order tanh observable initialization in any dimension.

Coefficient expectations factor into scalar/two-dimensional Gaussian integrals.
Population marks retain their complete within-population joint law. No training,
neural-width parameter, empirical covariance fit, or source tape is used here.
"""
from dataclasses import dataclass
from functools import lru_cache
import math
import time

import numpy as np

RIDGE = 1.0 / 4096.0


@dataclass
class InitializedFeatures:
    b1: np.ndarray
    g: np.ndarray
    p1: np.ndarray
    b2: np.ndarray
    p2: np.ndarray
    D: np.ndarray
    metadata: dict


def _positive_integer(value, name, minimum=1):
    if isinstance(value, bool) or not isinstance(value, (int, np.integer)):
        raise ValueError(f"{name} must be an integer")
    if value < minimum:
        raise ValueError(f"{name} must be at least {minimum}")
    return int(value)


@lru_cache(maxsize=8)
def _coefficients(order, cutoff):
    """Positive Gauss-Legendre integration of a truncated normal law.

    The weights are normalized to sum to one; the omitted Gaussian probability
    is erfc(cutoff/sqrt(2)). A quadrature refinement is a diagnostic, not a bound.
    This internal cache contains scalar constants only.
    """
    x, w = np.polynomial.legendre.leggauss(order)
    x = cutoff*x
    w = cutoff*w*np.exp(-x*x/2)/math.sqrt(2*math.pi)
    w /= w.sum()
    h = np.tanh(x)
    v = float(w @ (h*h))
    upper = np.tanh(math.sqrt(v)*x)
    tau = float(w @ (upper*upper))
    alpha = 1-tau
    reverse = math.sqrt(tau)*x[None, :]+alpha*h[:, None]
    k = np.tanh(reverse)
    s = float(w @ ((k*k) @ w))
    beta = float((w*h) @ (k @ w))
    gamma = 1-s
    a = math.sqrt(v+RIDGE)
    b = math.sqrt(s+RIDGE-beta*beta/(v+RIDGE))
    c = math.sqrt(tau+RIDGE)
    d_h = alpha*v/(a*c)
    d_k = (alpha*beta*RIDGE/(v+RIDGE)+tau*gamma)/(b*c)
    values = dict(v=v, tau=tau, alpha=alpha, s=s, beta=beta, gamma=gamma,
                  a=a, b=b, c=c, d_h=d_h, d_k=d_k)
    if not all(math.isfinite(v) for v in values.values()):
        raise ValueError("nonfinite initializer coefficients")
    if min(v, tau, alpha, s, gamma, a, b, c) <= 0:
        raise ValueError("positive initializer coefficient unresolved")
    return tuple(values.items())


def coefficients(quadrature_order=128, refinement_order=256, cutoff=10.0):
    """Return refined constants and the coarse-versus-refined diagnostic.

    The larger rule supplies the working coefficients. Orders are numbers of
    scalar nodes, not the number of nodes in a d-dimensional tensor product.
    """
    q = _positive_integer(quadrature_order, "quadrature_order", 8)
    r = _positive_integer(refinement_order, "refinement_order", q+1)
    if isinstance(cutoff, (bool, np.bool_)):
        raise ValueError("cutoff must be a finite positive real")
    cutoff = float(cutoff)
    if not math.isfinite(cutoff) or cutoff <= 0:
        raise ValueError("cutoff must be finite and positive")
    coarse, fine = dict(_coefficients(q, cutoff)), dict(_coefficients(r, cutoff))
    errors = {key: abs(fine[key]-coarse[key]) for key in fine}
    metadata = dict(rule="normalized-truncated-Gaussian-Gauss-Legendre",
                    coarse_order=q, working_order=r, cutoff=cutoff,
                    omitted_scalar_Gaussian_mass=math.erfc(cutoff/math.sqrt(2)),
                    absolute_refinement_differences=errors,
                    max_absolute_refinement_difference=max(errors.values()),
                    error_certificate=False)
    return fine, metadata


def _marks(d, particles, seed, population_rule, folded, constants):
    d = _positive_integer(d, "d")
    particles = _positive_integer(particles, "particles")
    seed = _positive_integer(seed, "seed", 0)
    if population_rule not in ("iid", "antithetic"):
        raise ValueError("population_rule must be iid or antithetic")
    if not isinstance(folded, bool):
        raise ValueError("folded must be boolean")
    if folded and population_rule != "antithetic":
        raise ValueError("folding requires the antithetic population rule")
    if population_rule == "antithetic" and particles % 2:
        raise ValueError("antithetic nominal particles must be even")
    count = particles//2 if population_rule == "antithetic" else particles
    children = np.random.SeedSequence(seed).spawn(3)
    rng_g, rng_reverse, rng_upper = [np.random.Generator(np.random.PCG64(s)) for s in children]
    g = rng_g.standard_normal((count, d))
    h = np.tanh(g)
    k = rng_reverse.standard_normal((count, d))
    k *= math.sqrt(constants["tau"])
    k += constants["alpha"]*h
    np.tanh(k, out=k)
    upper = rng_upper.standard_normal((count, d))
    upper *= math.sqrt(constants["v"])
    np.tanh(upper, out=upper)
    if population_rule == "antithetic" and not folded:
        g, h, k, upper = [np.concatenate((x, -x), axis=0) for x in (g, h, k, upper)]
    return g, h, k, upper


def _normalized(h, k, upper, constants, folded):
    n, d = h.shape
    start = 0 if folded else 1
    b1 = np.empty((n, 2*d+start))
    b2 = np.empty((n, d+start))
    if not folded:
        b1[:, 0] = b2[:, 0] = 1/math.sqrt(1+RIDGE)
    b1[:, start:start+d] = h/constants["a"]
    b1[:, start+d:] = (k-constants["beta"]*h/(constants["v"]+RIDGE))/constants["b"]
    b2[:, start:] = upper/constants["c"]
    D = np.zeros((d+start, 2*d+start))
    j = np.arange(d)+start
    D[j, j] = constants["d_h"]
    D[j, j+d] = constants["d_k"]
    return b1, b2, D


def initialize(d, particles, seed, *, quadrature_order=128, refinement_order=256,
               cutoff=10.0, population_rule="iid", folded=False):
    """Initialize full joint marks and a dense stored initial action matrix.

    Unfolded shapes: b1=(P,1+2d), g=(P,d), b2=(P,1+d), D=(1+d,1+2d).
    Antithetic folded shapes: b1=(P/2,2d), g=(P/2,d), b2=(P/2,d), D=(d,2d).
    The full evolving M may acquire arbitrary entries; D's initial structure
    imposes no later block or rank constraint. Probability arrays sum to one.
    """
    started = time.perf_counter()
    constants, diagnostic = coefficients(quadrature_order, refinement_order, cutoff)
    g, h, k, upper = _marks(d, particles, seed, population_rule, folded, constants)
    b1, b2, D = _normalized(h, k, upper, constants, folded)
    p1 = np.full(len(g), 1/len(g))
    p2 = p1.copy()
    metadata = dict(
        construction="general-dimensional-tanh-p1", hierarchy_order=1,
        input_dimension=int(d), nominal_population_nodes=int(particles),
        stored_population_nodes=len(g), population_rule=population_rule,
        sign_folded=folded, omitted_inactive_constant_features=folded,
        full_feature_dimensions=[1+2*int(d), 1+int(d)],
        feature_dimensions=[b1.shape[1], b2.shape[1]],
        first_feature_order="h_1..h_d,k_1..k_d" if folded else "1,h_1..h_d,k_1..k_d",
        second_feature_order="upper_1..upper_d" if folded else "1,upper_1..upper_d",
        ridge=RIDGE, ridge_numerator=1, ridge_denominator=4096,
        normalization="inverse-lower-Cholesky-of-population-Gram",
        core_constants=constants, coefficient_quadrature=diagnostic,
        population_seed=int(seed), random_generator="NumPy-PCG64",
        seed_streams=["SeedSequence(seed).spawn(3)[0]: G",
                      "SeedSequence(seed).spawn(3)[1]: reverse independent Z",
                      "SeedSequence(seed).spawn(3)[2]: upper independent Z"],
        exact_population_coefficients=False, coefficient_target="population expectation",
        empirical_population_Gram_used=False, source_regularizer_used=False,
        arbitrary_dimension_network_convergence_proved=False,
        full_evolving_matrix_required=True, arithmetic="float64",
        initialized_output_bytes=sum(x.nbytes for x in (b1,g,p1,b2,p2,D)),
        initialization_seconds=time.perf_counter()-started)
    return InitializedFeatures(b1, g, p1, b2, p2, D, metadata)


