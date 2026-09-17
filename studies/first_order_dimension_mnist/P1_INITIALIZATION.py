"""Study-only first-order tanh observable initialization in any dimension.

Coefficient expectations factor into scalar/two-dimensional Gaussian integrals.
Population marks retain their complete within-population joint law. No training,
neural-width parameter, empirical covariance fit, or source tape is used here.
"""
from dataclasses import dataclass
from functools import lru_cache
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
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
        construction="study-general-dimensional-tanh-p1", hierarchy_order=1,
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


def dense_oracle(d, particles, seed, *, quadrature_order=128, refinement_order=256,
                 cutoff=10.0, population_rule="iid", folded=False):
    """Independent dense Cholesky normalization of the exact block moment target.

    This deliberately uses O(d^3) normalization and is for small checks only.
    Coefficients retain their declared numerical integration approximation.
    """
    c, _ = coefficients(quadrature_order, refinement_order, cutoff)
    g, h, k, upper = _marks(d, particles, seed, population_rule, folded, c)
    offset = 0 if folded else 1
    n1, n2 = 2*d+offset, d+offset
    raw1 = np.column_stack((h, k))
    raw2 = upper
    if not folded:
        raw1 = np.column_stack((np.ones(len(g)), raw1))
        raw2 = np.column_stack((np.ones(len(g)), raw2))
    gram1, gram2, C = np.zeros((n1,n1)), np.zeros((n2,n2)), np.zeros((n2,n1))
    if not folded:
        gram1[0,0] = gram2[0,0] = 1
    # Assemble from the full uncentered moment and source-contraction identities.
    for j in range(d):
        lower_h, lower_k, upper_j = j+offset, j+d+offset, j+offset
        gram1[lower_h,lower_h] = c["v"]
        gram1[lower_k,lower_k] = c["s"]
        gram1[lower_h,lower_k] = gram1[lower_k,lower_h] = c["beta"]
        gram2[upper_j,upper_j] = c["tau"]
        C[upper_j,lower_h] = c["alpha"]*c["v"]
        C[upper_j,lower_k] = c["alpha"]*c["beta"]+c["tau"]*c["gamma"]
    L1 = np.linalg.cholesky(gram1+RIDGE*np.eye(n1))
    L2 = np.linalg.cholesky(gram2+RIDGE*np.eye(n2))
    T1 = np.linalg.solve(L1, np.eye(n1))
    T2 = np.linalg.solve(L2, np.eye(n2))
    return dict(b1=raw1@T1.T, g=g, b2=raw2@T2.T, D=T2@C@T1.T,
                raw_gram1=gram1, raw_gram2=gram2, raw_contraction=C)


def _verification(output):
    """Run the bounded, predeclared initializer checks; no training occurs."""
    from pde.observable_arithmetic import Arithmetic, gaussian_points
    from pde.observable_initialization import initialize_features

    started = time.perf_counter()
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    c, diag = coefficients()
    checks = []
    for d in (1, 2, 7, 17):
        for rule, folded in (("iid",False), ("antithetic",False), ("antithetic",True)):
            actual = initialize(d, 40, 1907, population_rule=rule, folded=folded)
            reference = dense_oracle(d,40,1907,population_rule=rule,folded=folded)
            discrepancies = {key: float(np.max(np.abs(getattr(actual,key)-reference[key])))
                             for key in ("b1","b2","D","g")}
            checks.append(dict(d=d,population_rule=rule,folded=folded,
                               absolute_errors=discrepancies,
                               passed=max(discrepancies.values())<2e-12))
    paired = initialize(7,40,1907,population_rule="antithetic")
    folded = initialize(7,40,1907,population_rule="antithetic",folded=True)
    folding = dict(b1=float(np.max(abs(paired.b1[:20,1:]-folded.b1))),
                   b2=float(np.max(abs(paired.b2[:20,1:]-folded.b2))),
                   g=float(np.max(abs(paired.g[:20]-folded.g))),
                   D=float(np.max(abs(paired.D[1:,1:]-folded.D))),
                   lower_odd=float(np.max(abs(paired.b1[:20,1:]+paired.b1[20:,1:]))),
                   upper_odd=float(np.max(abs(paired.b2[:20,1:]+paired.b2[20:,1:]))))
    # A controlled d=2 comparison uses the maintained finite-Q coefficient rule
    # and EXACTLY its population replay nodes, with no random-population mismatch.
    ar = Arithmetic()
    population_nodes = 256
    z1 = gaussian_points(population_nodes,4,ar)
    z2 = gaussian_points(population_nodes,2,ar)
    h = np.tanh(z1[:,:2])
    k = np.tanh(math.sqrt(c["tau"])*z1[:,2:]+c["alpha"]*h)
    upper = np.tanh(math.sqrt(c["v"])*z2)
    b1,b2,D = _normalized(h,k,upper,c,False)
    maintained = []
    for Q in (2048,16384,131072):
        old = initialize_features(1,arithmetic=ar,initialization_nodes=Q,
                                  population_nodes=population_nodes,epsilon_cov=1e-8)
        errors = {key:float(np.max(np.abs(getattr(old,key)-target)))
                  for key,target in (("b1",b1),("b2",b2),("D",D))}
        maintained.append(dict(initialization_nodes=Q,absolute_errors=errors))
    passed = (all(item["passed"] for item in checks) and max(folding.values())<2e-12
              and diag["max_absolute_refinement_difference"]<1e-10
              and max(maintained[-1]["absolute_errors"].values())<5e-3)
    report = dict(passed=passed,claim="initializer algebra and numerical diagnostics only",
                  coefficients=c,quadrature_refinement=diag,dense_checks=checks,
                  initializer_folding=folding,maintained_d2_control=maintained,
                  maintained_control_pass_threshold=5e-3,
                  no_training_executed=True,elapsed_seconds=time.perf_counter()-started,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  python=platform.python_version(),numpy=np.__version__)
    (output/"initializer_check.json").write_text(json.dumps(report,indent=2)+"\n")
    if not passed:
        raise RuntimeError("initializer validity gate failed; inspect retained report")
    print(json.dumps(dict(passed=passed,output=str(output/"initializer_check.json"),
                         elapsed_seconds=report["elapsed_seconds"])))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path,
                        default=Path("data/generated/first_order_dimension_mnist/initializer_checks"))
    args = parser.parse_args()
    if not args.check:
        parser.error("use --check, or import initialize")
    _verification(args.output)
