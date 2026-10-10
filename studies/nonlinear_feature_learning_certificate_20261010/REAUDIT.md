# Rigorous re-audit of the shortened theorem and proof

Date: 2026-10-10. Requested scope: the newly added nonlinear feature-learning
theorem in the compact paper, its shortened proof, and the earlier fitting
lemma used by that proof. This is not a re-audit of the three compression
constructions or their storage proofs.

## Assessment

No mathematical error or missing hypothesis was found in the reviewed
argument. The theorem's four conclusions are supported at their stated
fixed-positive-time, probability-tending-to-one scope. No paper correction
was required or applied. This is a mathematical audit, not machine-checked
formal verification or book promotion.

The coordinator read the complete setup/entrypoint, theorem, new proof, and
fitting source, and reconstructed the calculations below. The previously
reported audit verdicts were not used as evidence. The coordinator is also
the proof's author and is not an independent reviewer. A fresh scoped
initialization audit is recorded in `REAUDIT_INITIALIZATION.md`. After that
reviewer reported its preliminary assessment, it received the coordinator's
completion status and cubic-coefficient check; the report records this timing
rather than claiming complete blind isolation. A separate
dynamics reviewer accidentally received earlier agents' verdict summaries
through an agent-status listing; that review was stopped and is **not counted
as an independent audit**. Its disclosure and partial calculation are in
`REAUDIT_DYNAMICS.md`. Attempts to open a replacement fresh reviewer were
blocked by the agent-thread limit; the coordinator completed the dynamics
audit directly.

## Exact inputs

All scientific lines of these four files were read:

| File | SHA-256 |
| --- | --- |
| `paper/compact.tex` | `5944806ea716f04baea2a8e56d79db913613c3a168dc2644cf5d81cd53daec21` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `paper/feature_learning_theorem.tex` | `f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f` |
| `paper/compact_feature_learning.tex` | `71f50a55613a3df12398d6226b8fe2380805f2f32082e134e7ab45846bfa4bd1` |

HEAD was `c17cb8c2e8d486ccc1d2b80e8cd173ba551145ae`; the shared worktree
was dirty and the index empty. No source, PDF, experiment, or Git-index
change was made for this audit. The rigorous-mathematics and canonical
neural-network notation instructions were applied. The maintained reading
guide and notation contract were read for author workflow, not used to
import an additional scientific theorem. No other study was consulted.

## 1. Nonaffinity and the four-input witness

The Hermite covariance expansion applies because bounded first derivative
implies at most linear activation growth and hence Gaussian square
integrability. Finite Hermite support would make the continuous activation
a polynomial everywhere; bounded derivative would make it affine. Thus each
nonaffine activation has unbounded positive covariance-coefficient support.
Composition preserves that support and summability; nonnegative coefficients
justify the rearrangement by Tonelli, including activations with nonzero mean.

For the normalized training inputs, the degree-k tensor Gram tends to the
identity because every off-diagonal inner product has absolute value less
than one. Its affine-projected kernel is positive semidefinite: it is the
Gram of the tensor feature with its constant and linear spherical components
removed. The removed coefficients tend to zero, so this projected training
Gram also tends to the identity. A nonzero label vector therefore cannot
cancel every nonlinear component of the limiting initial prediction
velocity. No invertibility of the raw input Gram is needed.

The great-circle argument is valid in every allowed dimension. If all great
circle restrictions were affine, the antipodal average would be a common
constant and the odd part's homogeneous extension would be linear on every
two-dimensional plane, hence additive and linear globally. On a nonaffine
circle, three distinct points determine the affine restriction and a fourth
witnesses its failure. The normalized affine-annihilating functional has
coefficient absolute sum one, so it bounds the uniform affine-approximation
error. The fitting proof's finite-query Gram convergence applies to these
fixed additional inputs without imposing a Gram gap on the augmented list.

## 2. Initialization and strictly positive layer energies

The reverse Gaussian formula retains the conditional mean determined by the
forward action of the same matrix; it does not substitute an independent
backward matrix. Conditional on all previous answers, the reverse query is
known and the unused residual of that matrix is still Gaussian. Each hidden
matrix is queried only once in each direction. Higher-layer reverse answers
do not reveal a lower matrix's residual beyond its already known forward
answer.

The finite-rank projected innovation has conditional normalized squared norm
equal to rank times the reverse-query Gram trace divided by n. The trace is
tight by the second-moment induction. Conditional Markov's inequality thus
makes the projection negligible in probability, without requiring an
unconditional expectation bound. Forward Gram inverses are used on their
full-rank events, whose probabilities tend to one; no input-Gram inverse is
used.

The empirical quadratic-Wasserstein induction is sufficient. Independent
Gaussian augmentation gives conditional laws of large numbers; continuous
maps of at most linear growth preserve convergence with second moments.
In particular, the derivative gate times a backward coordinate has this
growth, despite the activation values themselves being unbounded. Same-layer
quadratic products therefore converge. No trained population-flow theorem
or unproved fourth-moment bound is needed here.

At the top layer, a null backward-Gram direction would make the product of
the label-weighted activation sum and a derivative combination vanish on
the full-support Gaussian domain. Analyticity and varying coordinates force
the derivative coefficients to vanish. Lower layers inherit a positive
Gaussian innovation covariance; gating retains strict positivity because
each nonzero analytic derivative is nonzero almost everywhere under its
nondegenerate marginal. Finally, the Schur-product lower bound with a
positive-diagonal input/feature Gram proves positive acceleration energy
for every hidden block, even when the input Gram is singular.

## 3. The real estimates really are width-uniform

The earlier fitting lemma was checked rather than merely cited. Its
initialization event has probability tending to one; its constants bound
operator norms, sphere-uniform feature RMS and residuals independently of
width. The gradient-flow dissipation and readout Gram gap give finite
parameter length. The stated small-label condition strictly closes its
feature and Gram bootstrap. The estimates used by the new proof are actual
conclusions of that lemma, not confidence-dependent substitutes.

Zero initial readout then gives readout/backward fields of order t and
hidden weight/feature increments of order t squared. To control derivative
gates, fix a deterministic tail cutoff in an initial backward field before
choosing time. Empirical convergence with second moments makes the squared
tail smaller than any prescribed tolerance with probability tending to one.
On the bounded part, the bounded second derivative and real increment bound
control the gate difference uniformly over the entire chosen interval.

This proves the displayed strong remainder convention: for every tolerance,
there is a deterministic positive interval on which the probability of any
normalized-remainder violation tends to zero. It is stronger than a merely
pointwise-in-time expansion or a confidence-dependent small interval. Finite
sums, bounded operators and time integration preserve this convention.

## 4. Adjoint telescoping and an independent cubic-coefficient check

Pairing each feature increment with its initial pre-gated adjoint turns
the direct weight increment into an inverse-mobility inner product with
the initial weight acceleration. The propagated feature increment pairs
with the preceding layer's adjoint, while the product of the two increments
is of order t to the fourth. Telescoping produces a positive partial sum of
hidden-block acceleration energies. Cauchy--Schwarz against the bounded
initial adjoints proves actual feature movement in every layer; weight
movement alone is not being substituted for feature movement.

There is also a separate finite-width derivative check on the cubic
coefficient. In this paragraph only, put k = 2/m and let E be the sum of
the squared hidden accelerations in inverse-mobility norm. At zero,
hidden velocities vanish, the tangent-kernel derivative vanishes, and
the readout and hidden-block parts each contribute \(2E/k^2\) to the
label-contracted second kernel derivative. Thus

\[
y^\top K''(0)y=\frac{4E}{k^2}.
\]

Both the dense and frozen-kernel predictions start at zero and have the
same first and second derivatives. Differentiating their exact prediction
equations at zero therefore gives

\[
y^\top(f_n-f_{\mathrm{NTK},n})'''(0)
 =k\,y^\top K''(0)y=\frac{4E}{k}.
\]

Division by 3! gives 2E/(3k) = mE/3, agreeing with the paper. This finite-width
calculation alone would not justify a width-uniform positive-time gap.
That additional step is supplied by the audited multiplier and adjoint
remainder argument. In the exact variation-of-constants formula, the
operator kernel increment is of order t squared, so replacing the frozen
exponential by the identity and the residual direction by its initial
value costs only order t to the fourth. No full matrix-valued limiting
second kernel coefficient is required.

## 5. Nonlinear feature increment and final transfer

The training span has dimension at least two. For nonzero vectors g and r
in that span, an affine representation of the function
phi'(g dot v) times (r dot v) on its unit sphere would vanish on the equator
orthogonal to r. Antipodes then force the affine representation to be a
multiple of r dot v. Division off that equator and continuity would make
phi' constant on a nontrivial interval, contradicting analyticity and
nonaffineness. This works also in a two-dimensional span and for even
activations.

The initial projected weight is nonzero almost surely, and the acceleration
has positive mean-square norm. Their dependence causes no problem: the
first property holds almost surely and the second gives positive probability
of a nonzero acceleration. The squared distance from affine functions is
continuous and bounded by a constant times the acceleration's squared norm.
The joint empirical second-moment limit thus gives a strictly positive
limiting projected energy. A bounded-row Taylor estimate followed by the
same deterministic tail cutoff transfers it to the actual feature increment.

The final transfer requires only that each supplied compression error tends
to zero in probability. At any fixed positive time, subtract that error
from the positive dense affine and frozen-kernel gaps. The four Taylor
witness inputs are chosen before initialization from the fixed training
problem; no passive labels are supplied. Adding at most four inputs changes
the panel-dependent constant factors, not the storage exponents.

## Qualifications that remain essential

- Every activation is nonaffine, and distinct training inputs are neither
  parallel nor antiparallel. These are additional activity-theorem
  hypotheses, not new restrictions on the compression theorem.
- The activation values may be unbounded; bounded derivative and analyticity
  are used exactly as stated. No centering or label-sign condition is added.
- Constants may depend on the entire fixed problem. This is not uniform in
  growing data size, shrinking label scale, or nearly coincident inputs.
- Prediction gaps hold at each fixed sufficiently small positive time with
  probability tending to one. They are not endpoint lower bounds or bounds
  valid for arbitrary width-dependent times tending to zero.
- The kernel comparator is the same dense initialization's frozen initial
  tangent kernel, not an arbitrary data-dependent kernel method.
- The hidden-feature statements concern the dense reference. The proof does
  not identify compressed coordinates with individual dense neurons.
- The three existing compression accuracy conclusions are supplied inputs
  in this scoped audit; their full proofs were not re-audited here.

No numerical experiment was used as proof evidence. The paper was not edited
or recompiled, because the audit found no required source correction.
