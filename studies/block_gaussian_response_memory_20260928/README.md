# Block Gaussian initialization and response-memory approximation

28 September 2026. New study for the modified block-diagonal initialization.
The user asks whether block size k can approximate canonical dense Gaussian
initialization efficiently enough to support a width- and time-uniform
response-memory theorem. The primary target remains the trained dense
population predictor, rather than entrywise approximation of its matrices.

## Scope and model

Fixed data and depth, n=Bk neurons per hidden layer, aligned independent
k-by-k Gaussian initialized blocks with entry variance 1/k. First-layer
initialization is iid Gaussian and readout is zero. Only initialization is
block diagonal: canonical gradient updates and learned memory corrections
remain globally connected. Compare the B-to-infinity block population at
fixed k with the canonical fully iid dense population as k increases.

Scientific inputs are the problem definition, this study's derivations,
and relevant maintained docs/ material. Prior unpromoted studies are not
proof dependencies. No training experiments, manuscript edits or Git writes
are planned. Deterministic algebra verification is permitted if useful.

## Completed results

- INITIALIZATION_UPPER.md proves, for bounded C_b^4 activations and any
  fixed depth, population kernel bias at most D_L/k uniformly over every
  input pair. The finite n=Bk empirical kernel has pointwise mean-square
  error at most D_L^2/k^2+V_L/n. D_L,V_L have explicit depth recursions.
  A weaker-regularity variant requires stated covariance nondegeneracy.
- BLOCK_BIAS_LOWER.md proves the 1/k bias is sharp for tanh already with
  two hidden layers and one normalized input. It gives all-k positive
  bounds and a positive leading coefficient with O(k^-2) remainder.
  A sine example gives a further closed-form check. Canonical residual
  signs were corrected during the parent's complete proof read-through.
- TRAINING_METRIC_AND_LINEAR_RESPONSE.md proves an all-time, all-input
  population predictor estimate C/k for the exact first derivative in
  label amplitude at zero labels, assuming a positive dense initial
  training-Gram gap. Its finite-width version has error
  C_p(1/k+1/sqrt(n)) in L2(test law; sup over time), with probability
  1-p. Differentiation precedes the width limit; no limit interchange or
  fixed-nonzero-label approximation is asserted.
- That note also derives an exact trained two-time feature-covariance
  identity and a sufficient all-time comparison bound. The required
  trained covariance comparison is explicitly unproved.
- SMALL_LABEL_BLOCK_FITTING.md now proves a fully nonlinear a priori
  result for the actual canonical block-initialized network, with all
  learned entries trainable. At every fixed finite depth, bounded
  C^{1,1}_loc activations with bounded first derivative, zero readout,
  an initial normalized feature-Gram gap gamma, and an empirical block
  operator-norm moment bound imply a size-independent small-label
  threshold. Below it, rho(t)<=Y exp(-gamma t) and the remaining
  L2(test-law) prediction change is at most C_mu Y exp(-gamma t)/gamma.
  Gaussian blocks meet the moment condition with explicit probability
  uniform in B,k; the initial Gram estimate supplies the other event
  under its C_b^4 assumptions. This is an all-time fitting and test-tail
  theorem, not a block-to-dense or moment-closure discrepancy theorem.
- SMALL_LABEL_TRAINED_BRIDGE_ROUTE.md proves an exact Gaussian A/A^T
  response identity and an O(1/k) weak-bias estimate for it. For two
  hidden tanh layers the identity also controls the complete cubic
  label-response coefficient equations, uniformly in time. Identification
  with a population derivative is separately qualified. A finite label
  expansion does not give the fixed-nonzero-label trained comparison.
- SMALL_LABEL_COMPLEXITY_THRESHOLD.md optimizes two explicitly
  hypothetical joint predictor-error certificates. With O(1/k) trained
  bias and near-quadratic order decay, a uniform B^{-1/2} sampling term
  would give learned exponent 7/2; a stronger (Bk)^{-1/2} term would give
  exponent 5/2. Neither joint error bound is established. The note also
  quantifies how growing constants change or destroy that comparison.
- SMALL_LABEL_GAUSSIAN_PROGRAM_ROUTE.md records the exact scope of the
  maintained Gaussian-program results. Its Section 4.6 combines their
  qualitative fixed-program limit with the new fitting theorem and a
  one-reference comparison to prove the actual full nonlinear bridge
  qualitatively: for every epsilon>0,
  sup_B P(E_mu(f_{Bk,k},f_dense)>epsilon) tends to zero as k tends to
  infinity. E_mu is the L2(test law) norm of the pointwise all-time
  prediction difference. This is for full canonical learned updates,
  sufficiently small fixed labels, a positive initial training gap,
  and the assumed regular canonical dense population flow. It covers
  any fixed test probability law and the final predictors on the
  high-probability fitting event. It does not require existence of a
  fixed-k B-to-infinity population. No rate in k is supplied, and no
  finite-q closure is included in this convergence statement.
  Fixed-transcript quantitative estimates cannot simply be made
  mesh-uniform: their history Gram gaps and moment constants matter.

The initialization results imply that k of order sqrt(n) matches the
dense model's n^-1/2 kernel-error scale while using O(L n^(3/2)) rather
than O(L n^2) fixed initialized hidden weights. The tanh lower bound makes
this block-size scaling necessary in that kernel metric in general.
Equivalently, n=O(epsilon^-2), k=O(epsilon^-1) suffice for initialization
kernel RMS error epsilon, with O(L epsilon^-3) fixed-matrix storage.
These are initialization (and, under the stated gap, first-label-response)
claims, not an epsilon-cost theorem for nonlinear fitted predictors.

The eventual observable is the whole-input prediction discrepancy, with
the time supremum inside L2 of the test-input law. Initialization feature
kernels on training and passive test inputs are preliminary observables,
because initial predictions themselves vanish exactly with zero readout.

## Ownership and checks

Parent: model/metric choice, trained-flow implications, synthesis and README;
TRAINING_METRIC_AND_LINEAR_RESPONSE.md.
Fresh scoped author `block_initialization_kernel`: INITIALIZATION_UPPER.md.
Fresh scoped author `block_bias_obstruction`: BLOCK_BIAS_LOWER.md.
Each agent received only its neutral mathematical assignment, required
skills and optional current notation. They were independent author routes,
not promotion reviews. The parent read both complete derivations, checked
the Gaussian interpolation coefficients, variance and bias recursions,
and tanh curvature proof, and reconciled residual signs with docs/notation.
No numerical experiments or external scientific sources were needed.

For the resumed trained-bridge investigation, independent scoped routes
were assigned to `small_label_block_bridge`, `gaussian_bridge_program`,
and `block_compression_cost`. The parent independently derived the
all-depth fitting/test-tail theorem; `block_compression_cost` checked
its entire deterministic proof and probability algebra. The parent
checked the imported initialization proof, added its C_b^4 hypothesis
explicitly to the Gaussian probability corollary, and fixed the stated
limit topology and L>=2 scope. The parent also read the complete cubic
route and complexity derivations. These are author checks, not promotion
reviews. The cost agent checked its exponent optimization on 100 random
parameter choices against a linear-program solver (maximum discrepancy
3.6e-15); no neural training experiments were run.

The cost agent also checked the completed qualitative bridge's uniform-B
limit argument and whole-test dominated-convergence passage. The parent
checked the maintained C.1 one-reference inequality and C.2 hypotheses,
made the allowed dense-existence assumption explicit, and explained why
the dense fitting bounds follow from the same deterministic bootstrap.
The proxy's products with random global contractions are localized on
their uniformly tight moment event. None of these checks supplies a
quantitative block-size rate or a finite-memory complexity theorem.

Two external primary full texts were retrieved for a narrowly scoped
applicability check: Agazzi--Mosig Garcia--Trevisan, arXiv:2607.06290v1,
and Chen--Yang--Zhao--Gu, arXiv:2503.09565v2. Neither is used as a proof
dependency. The former's stated execution rules and Theorem 1.2 concern
fixed Netsor Gaussian-process programs, with Section 1 distinguishing
their setting from feature learning; they do not provide our trained
transpose-reuse, mesh-uniform weak error. The latter's Theorem 4.5 and
Corollary 4.6 concern feature nondegeneracy and vanishing residual when
training stops under their stated hypotheses, not a quantitative
block-size approximation rate. Full texts:
https://arxiv.org/pdf/2607.06290v1 and
https://arxiv.org/pdf/2503.09565v2.

## Remaining obligation and claim level

The reported derivations are internally checked study results, not
promoted book theorems. No manuscript was changed and no Git commit was
made. The fully nonlinear block-population predictor has not been proved
O(1/k)-close to canonical dense population flow uniformly in time for fixed
nonzero labels. That requires comparison of the trained two-time feature
kernels, including their accumulated variation, with constants controlled
in k and closure order q. Initialization covariance alone does not provide
it. Consequently no combined all-time q^-2+k^-1+n^-1/2 theorem is claimed.
