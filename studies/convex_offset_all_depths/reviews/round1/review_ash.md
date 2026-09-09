# Independent review: convex-offset conditioning obstruction

**Verdict: UNVERIFIED as a complete report.** Equations (1)–(10), the initialized feature-Gram contraction, and the stated distinction from a qualitative fixed-depth global-training theorem pass my mathematical checks. One asserted identification is not defined or proved by the supplied report: the identification of the total raw training kernel with the feature Gram in lines 201–207. Under the ordinary Euclidean parameter metric, the claimed readout identification is false for the finite-width readout formula that the report states. A specified population/raw metric could make it correct, but that specification is absent. I cannot issue PASS for all asserted results without resolving this point.

## Scope and provenance

I read the entire supplied manuscript, lines 1–236, at:

`/tmp/convex_offset_review_20260908/manuscript.md`

Verified SHA256:

`058ca16241af739ae68845a260cbf39c09a9cb84524e62703ad7e4e19d34da19`

The manuscript was the only mathematical context read. I did not read project files, prior chat context, skill files, other manuscripts, or other reviews. I did not use agents or communicate with reviewers. No specialized external theorem was needed: the covariance identity is proved directly in the report and checked below. This review certifies only assertions actually made in this manuscript and cannot certify any additional global-training theorem.

## 1. Initialized Gaussian law and compact interval: PASS

For an independent higher-layer Gaussian row with entries of variance 1/n, conditioning on the preceding features gives covariance

`(1/n) sum_a h_{i,a} h_{j,a}`.

This is the full uncentered Gram, including the contribution of the nonzero feature mean. Replacing it by the centered feature covariance would be wrong; the report does not make that mistake. The first layer has covariance Gamma because its entries have variance 1/d and the inputs have the specified inner products.

For each separately fixed finite depth, conditional independence across rows and induction give the deterministic Gaussian covariance recursion (2). Linear growth of the activation gives all necessary fixed-depth Gaussian moments; continuity of Gaussian expectations in a positive semidefinite covariance follows by a square-root coupling and uniform moment bounds. Thus the law-of-large-numbers argument can be completed routinely, including singular covariance. Equation (2) is correctly presented as the population recursion, rather than as an unconditional finite-width Gaussian identity.

Equal diagonal variances are preserved because all inputs have the same norm and all coordinates use the same activation. Equation (3) is therefore correct.

Write alpha = 1 − epsilon and m = 1 − 2 epsilon. The mean is at least alpha − epsilon = m > 0. The L2 norm is at least this mean. The upper estimate is

`||alpha sigma G + alpha + epsilon psi(sigma G)||_2 <= alpha sigma + 1`.

At sigma = 1/epsilon its right-hand side equals 1/epsilon, and the affine bound is increasing. The initial value 1 belongs to the claimed interval. This verifies (4), including the lower endpoint for every layer. Strict positivity of m is used essentially later; the result is stated only for epsilon < 1/2.

## 2. Strict Gaussian contraction: PASS

The derivative satisfies m <= phi' <= 1. For every positive sigma, equality `E phi'(sigma G)^2 = 1` would force phi' = 1 Gaussian-almost everywhere. Positivity of phi', full Gaussian support, and continuity then give phi' = 1 everywhere. This forces psi' = 1 everywhere, which contradicts boundedness of psi.

The expectation is continuous in sigma by bounded convergence. The interval [m, 1/epsilon] is compact and excludes zero. Hence the maximum in (5) is attained and is strictly smaller than one. Its square root is positive, indeed at least m. The compactness step is valid and does not confuse pointwise strictness with uniform strictness over a noncompact set.

This kappa is for a fixed epsilon and a fixed shape psi. The report does not prove or need a common contraction constant for all shapes, nor for depth-dependent choices of epsilon.

### Direct density calculation

With D = sigma^4 − c^2, differentiating the logarithm of the Gaussian density in c gives

`c/D + [(sigma^4 + c^2)xy − sigma^2 c(x^2 + y^2)]/D^2`.

Computing `(partial_x partial_y p_c)/p_c` gives exactly the same expression. There is no missing factor of two from the off-diagonal covariance: c changes both symmetric entries, and the displayed mixed derivative is the correct result.

On compact interior covariance intervals the covariance eigenvalues stay bounded away from zero, so density derivatives have a Gaussian envelope times a polynomial. The activation has at most linear growth and bounded derivatives. Differentiation under the integral and the two integrations by parts are justified, with vanishing boundary terms. This yields the claimed derivative of the product expectation.

Cauchy–Schwarz uses the two equal marginal laws and gives the derivative upper bound `E phi'(sigma G)^2`. Integrating to the upper covariance endpoint is legitimate. The stated coupling has exactly the desired covariance, and converges in L2 at both endpoints. Lipschitzness gives L2 convergence of the activations, and Cauchy–Schwarz gives convergence of their product expectation. Consequently the argument also covers c = −sigma^2, not just nonnegative correlations. Multiplication by two gives (6) with the correct coefficient.

### Analytic stress test with an admissible shape

As an independent check, take psi(z) = sin z. For q = sigma^2 and covariance c, the product expectation is exactly

`F(c) = alpha^2(1+c) + 2 alpha epsilon c exp(−q/2) + epsilon^2 exp(−q) sinh(c)`.

Its derivative is

`F'(c) = alpha^2 + 2 alpha epsilon exp(−q/2) + epsilon^2 exp(−q) cosh(c)`.

For |c| <= q, this is at most

`alpha^2 + 2 alpha epsilon exp(−q/2) + (epsilon^2/2)(1 + exp(−2q)) = E phi'(sigma G)^2`.

This confirms the comparison for negative correlations as well as positive ones in a concrete allowed nonlinear case. It reveals no counterexample to (6).

## 3. Distance and spectral bounds: PASS

At layer one the Gaussian squared distance is 2(1 − Gamma_ij). At every subsequent layer the Gaussian squared distance is the preceding feature squared distance, because its covariance is the full preceding Gram and the two marginal second moments are equal. Thus applying (6) at each layer gives exactly the power kappa^(2L) in (7).

For distinct coefficient indices i and j, `(e_i − e_j)/sqrt(2)` is a unit vector and its Gram Rayleigh quotient is Delta_L,ij/2. The minimum-eigenvalue upper bound (8) follows. Singular input Grams, negative pair correlations, or singular later Grams do not invalidate this argument. Pairwise angular separation is unnecessary for the upper bound.

Each feature mean is at least m. Therefore the Rayleigh quotient in the all-ones direction is at least 3m^2 by Jensen's inequality, giving the stated positive lower bound on lambda_max. Combining it with (8) correctly proves collapse of lambda_min/lambda_max. This is stronger than merely saying that an overall feature amplitude goes to zero.

The result concerns the population initialization for each fixed depth, followed by L tending to infinity. It does not supply a finite-width estimate uniform over increasing depths. The manuscript does not claim such an estimate.

## 4. Concrete activation: PASS

For psi(z) = arctan(z)/4,

- its supremum norm is pi/8;
- psi'(z) = 1/[4(1+z^2)], whose supremum is 1/4;
- psi''(z) = −z/[2(1+z^2)^2], whose maximum absolute value occurs at |z| = 1/sqrt(3) and equals 3 sqrt(3)/32.

The shape is bounded, smooth, and nonconstant, and satisfies every stipulated bound. At epsilon = 1/4 the resulting activation is exactly (9). Its derivative is

`3/4 + 1/[16(1+z^2)]`,

so 13/16 is its global Lipschitz constant. Pointwise Lipschitz contraction, followed by the same covariance recursion and Rayleigh quotient, proves (10) without the covariance-differentiation argument.

Here “convex activation” means the convex mixture in (1). The arctangent example is not a globally convex function of its scalar argument; the explicit reference to the convex-mixture question makes the intended meaning recoverable. This terminological issue does not affect the mathematics.

## 5. Outstanding objection: the raw kernel metric is unspecified

The issue is at lines 28–34 and 201–207. The report specifies the finite-width output

`f_i = (1/n) C^T h_i^L`,

but it gives no definition of the “original raw metric,” no block learning-rate normalization, and no formula defining the corresponding population training kernel.

Under the usual Euclidean inner product on the stated C coordinates,

`partial f_i / partial C_a = h_{i,a}^L/n`,

and hence the readout block is

`K_read,ij^(n) = (1/n^2) sum_a h_{i,a}^L h_{j,a}^L = Q_emp,ij^(n)/n`.

It therefore tends to zero, rather than to Q_L. This discrepancy is independent of the random initialization of C; the readout derivative itself does not depend on C. In particular, the assertion “The readout block is exactly Q_L” does not follow from the explicitly specified network and ordinary Euclidean metric.

One can obtain Q_L by specifying the readout metric to be `g_C(u,v) = (1/n) u^T v`, equivalently using inverse metric n times the Euclidean identity in that block, and then taking the population limit. Alternatively one can define the continuum readout metric as an L2 metric on the neuron index, derive `D_C f_i[delta C] = E[h_i^L delta C]`, and identify its gradient Gram as Q_L. Either convention could be intended. Neither is defined in the manuscript.

Likewise, the population assertion that all hidden gradient blocks vanish at C = 0 is algebraically correct for an appropriately defined population differential whose backward fields are linear in C. At finite width the initialized C is random and not identically zero. Inferring the limit of metric-weighted hidden kernels from the bare limiting value C = 0 requires specifying the hidden metric and its scaling, or specifying and deriving the population kernel directly. Divergent metric factors can in general compensate a shrinking readout, so the metric cannot be omitted from this identification.

This objection does not undermine the feature-Gram theorem. It prevents unconditional certification of the asserted total-raw-kernel theorem from the supplied standalone report. To repair it, explicitly state the raw metric or population kernel definition, show the readout block equals Q_L under that definition, and show each hidden block is zero at the stated population initialization. If these are established properties of an earlier model, reproduce the necessary definitions and derivation here; I was instructed not to consult other mathematical context.

## 6. Scope concerning global training: PASS

The report explicitly distinguishes

`for each fixed allowed activation, lambda_min(Q_L) -> 0 as L -> infinity`

from a statement that a fixed activation fails a qualitative global-training theorem at some finite depth. That distinction is correct.

For example, the abstract matrices `J_3 + rho^L I_3`, with 0 < rho < 1 and J_3 the all-ones matrix, have a strictly positive smallest eigenvalue at every finite L, but that eigenvalue tends to zero and their eigenvalue ratio also tends to zero. This is a logical counterexample to an inference from loss of a depth-uniform floor to loss of positivity at an individual finite depth; it is not asserted to be this network's exact kernel.

The report makes no claim of proving fixed-depth positive definiteness, all-time feature separation, a tail estimate along training, or global training convergence. It explicitly lists these as further obligations. I found no illicit inference of impossibility of qualitative fixed-depth global training.

Subject to the unresolved metric identification, the obstruction correctly applies to arguments requiring a single positive initialized raw-kernel floor for every depth in the fixed activation class. It cannot certify or refute an additional global-training theorem whose constants may depend on depth.

## Final assessment

The self-contained initialized feature-Gram results are valid, including the strict contraction for every fixed allowed shape and the normalized-conditioning collapse. The covariance proof is complete and does not rely on an unchecked specialized external theorem. The sole substantive unresolved point is the undefined raw metric and resulting unproved identification of the total initialized training kernel with Q_L. **Overall status: UNVERIFIED; not PASS.**
