# Frozen query-span screen, 2026-10-02

This protocol was written before simulation outcomes. Scope is an empirical
screen of the actual fixed-Gaussian queries along the paper's order-q,
learning-speed, raw-Legendre closure. It does not validate the closure against
dense training, simulate a deferred Gaussian oracle, or prove a population
complexity bound. Sources are `paper/main.tex` (Setting and learning-speed
construction/proof), its relevant result statements, and `docs/notation.qmd`.

## Decision and hypotheses

H1: the observed forward and adjoint query directions occupy a small online
span at absolute per-neuron RMS tolerance 0.001 despite substantial feature
learning. H0: preserving these actions requires a combined span comparable
with width. A shared fixed Gaussian matrix is used in both directions throughout;
no fresh-independent-noise, frozen-feature, linearized, or fitted-history
substitution is allowed. A second correlated, higher-dimensional dataset is a
stress against circle-specific redundancy. This is one seed, not replication.

## Canonical construction

Two tanh hidden layers have width n=2048. There are m inputs x_a in R^d of norm
sqrt(d), labels y_a, and stored readout w in R^n. First weights W^(1) are n by d;
the initialized hidden matrix W_0 is n by n. Independently initialize first
weights N(0,1), W_0 entries N(0,1/n), and w=0. The forward pass is

    z1_a = W1 x_a / sqrt(d), h1_a = tanh(z1_a),
    z2_a = W_hat h1_a,       h2_a = tanh(z2_a),
    f_a = w^T h2_a / n, r_a=f_a-y_a, rho=sqrt(mean_a r_a^2).

Backward responses exclude residuals:
delta2_a=w*(1-h2_a^2), delta1_a=(1-h1_a^2)*(W_hat^T delta2_a).
The stored state is W1,w,tau and moments bar_h[a,k,:], bar_delta[a,k,:],
0<=k<q. Here q is separately 1 and 3, paired to identical initialization.
The moments reconstruct

    W_hat = W_0 - 2/(n*m*tau) sum_(a,k) (2k+1) bar_delta[a,k] bar_h[a,k]^T.

Physical time follows canonical mobilities (n,1,n):

    dot W1 = -2/m sum_a r_a delta1_a x_a^T/sqrt(d),
    dot w  = -2/m sum_a r_a h2_a, dot tau=rho,
    dot bar_h[a,k] = rho*h1_a - rho/tau*(k*bar_h[a,k]
                                      +sum_(j<k)(2j+1)bar_h[a,j]),
    dot bar_delta[a,k] = r_a*delta2_a - rho/tau*(k*bar_delta[a,k]
                                      +sum_(j<k)(2j+1)bar_delta[a,j]).

Initialize tau=1, bar_h[a,0]=h1_a(0), other bar_h modes zero, and all bar_delta
zero. This is the constant-forward/zero-backward unit prefix. The code evaluates
W_hat and its transpose by low-rank actions, with the same dense W_0 for both.
No division by rho occurs.

## Fixed datasets and runs

* Circle: m=8,d=2, angles (0.07,0.38,0.84,1.31,1.89,2.42,2.93,3.57)
  radians, x_a=sqrt(2)*(cos(angle_a),sin(angle_a)), y_a=(-1)^a for a=0,...,7.
  No antipodal pair is imposed. These labels admit an odd extension on the
  observed circle points, as required by the bias-free tanh network.
* Sphere: m=16,d=8, independent Gaussian rows from data seed 8841, normalized
  to norm sqrt(8), labels sign(x_a1*x_a2*x_a3). No whitening or orthogonalization.
* Network seed 1771. Data and parameter RNG provenance is saved. Run q=1 then
  q=3 separately on each dataset. One process per dataset/GPU; inspect GPU
  occupancy first. T=80, Heun physical timestep 0.05 (1600 steps).

## Online monitor and metrics

At t=0 and after every complete Heun timestep, process each datum in fixed
index order, separately for h1_a and delta2_a. Heun predictor queries are not
observed in this initial screen. Each direction has its own never-forget
orthonormal basis. Orthogonalize twice; if the residual Euclidean norm divided
by sqrt(n) exceeds tolerance, append its normalized direction. No SVD of future
queries is used. The primary tolerance is 0.001; repeat the monitor at 0.0001
on the same trajectory as a diagnostic if it fits the resource cap.

Record ranks against time, every query's pre-acceptance innovation RMS, maximum
post-decision residual RMS, and actual fixed-matrix action error:
||W_0(h1_a-P h1_a)||/sqrt(n) or
||W_0^T(delta2_a-P delta2_a)||/sqrt(n), with the basis at that query. Accepted
directions have zero residual in exact arithmetic. The matrix is available
only in this diagnostic, so these errors do not claim an operational stopping
rule for a matrix-free implementation.

For each sample and direction, sum successive query differences in normalized
RMS. Their sum V over samples gives the rigorous *sampled-path* counting bound
rank <= m+V/tolerance, capped at n. This follows by charging each acceptance
after a sample's first acceptance to at least tolerance of path variation since
its previous accepted query, which remains in the basis. This normalized bound
does not bound unobserved excursions between sample times. Save layer-1 and
layer-2 feature RMS displacements, loss, maximal query magnitude, basis
orthogonality, finite-state diagnostics, and algebra-check errors.

Report operation/storage ceilings, distinguishing the actually measured dense
W_0 screen from a proposed oracle. Dense fixed-source storage is n^2 scalars;
an oracle retaining input bases and their output images needs about
2*n*(rank_forward+rank_backward) plus cross coefficients. If K forward-plus-
backward vector queries are evaluated, dense actions cost O(n^2*K); an optimistic
basis-action calculation costs O(n*sum_query retained_rank), with initialization,
Gaussian draws, reorthogonalization and low-rank closure work still charged
separately. These are arithmetic proxies, not measured speedups.

## Validity, branches and terminal stop

Before the main runs, check float64 low-rank evaluation against dense
reconstruction; first-layer/readout velocities against autograd with the
reconstructed hidden matrix held fixed; and the moment reconstruction derivative
at initialization against the dense hidden velocity (both vanish for w=0).
Also check moment integral/dilation formulas on an independently integrated
synthetic signal, so the zero-readout test alone cannot pass vacuously.
Autograd/reconstruction tolerance is 1e-10 absolute. GPU trajectories use
float32 with TF32 disabled; all states must remain finite and final basis
orthogonality maximum entry error must be below 1e-4. A failed validity gate is
inconclusive, not evidence against the span hypothesis.

A dataset/order provisionally passes only if rank_forward+rank_backward<n/8
at tolerance 0.001, both hidden layers move more than 0.05 RMS by some observed
time, and maximum retained-space action error in each direction is <=0.005.
Failure of the rank/action criterion with valid nontrivial motion rejects this
particular resource target on the tested path. Insufficient motion or invalid
numerics is inconclusive. Overall encouragement requires all four cases.
Full network/closure accuracy remains untested even after a screen pass.

If ranks plateau and all four cases pass, permit one stronger observation audit
of the same numerical paths by including Heun predictor queries; no scientific
parameter change or extra seed. This audit runs only if remaining budget permits
and is reported separately. If any case fails the resource target, stop before
building a larger simulator. No timestep-convergence conclusion is claimed;
the initial result is explicitly about the chosen discretized paths.

Hard cumulative cap: 10 additive GPU-minutes and 20 wall minutes for experiment
execution, including validation/audit. Maximum four primary runs plus their
precommitted observation audit; terminate before exceeding the cap. Save source
hashes, exact commands, versions, inputs, seeds, per-time logs and basis arrays
in data/generated/response_memory_gaussian_queries_20261002/rank_screen01.
Raw full histories may be omitted when large; logs and accepted bases suffice
for the preregistered screen. No manuscript or maintained-code edits.
