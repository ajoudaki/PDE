# Independent complete internal review R2 A

Reviewer: `cx2_partial_review_r2_a`. Review date: 2026-09-19.
Assignment: `REVIEW_R2_ASSIGNMENT_A.txt`. Frozen packet:
`data/generated/cx2_activation_class_20260919/review_r2_inputs/`.

**Verdict: PASS for the expressly local, bounded-subclass, and conditional
claims in this packet. This is not a proof of full C-X2.** I found no material
correctness objection requiring a correction to these claims. The missing
unbounded continuation and reached-tail estimates remain substantive open
obligations. Neither this verdict nor the deterministic checks promote the
result into established material.

## Scope and independence

I started from the neutral assignment in a fresh reviewer context. I am not
one of the listed authors/assemblers (`root`, `cx2_reference`, `cx2_source`,
`cx2_closure`). Scientific inputs were exclusively the thirteen manifest
files, read in full, and the manifest itself. I did not read the study README,
live scientific files, study history, earlier reports, another reviewer's
findings, chats, or other studies. I used no external scientific retrieval,
delegation, Git operation, or training experiment. Writes are confined to
this assigned report and `data/generated/cx2_activation_class_20260919/review_r2_a/`.

Required process inputs read were the supplied repository instructions,
`RESEARCH_WORKFLOW.md`, both `solve-math-rigorously` and
`investigate-conjectures` skills, and the latter's research-contract,
adversarial-audit, and decisive-experiments references. The task is an internal
scientific audit, not a relevance, promotion, or integration review.

## Exact conclusions supported

1. For each fixed nonaffine globally C1,1 activation with bounded derivative,
   the specified two-layer Gaussian model on the fixed nonparallel two-point
   dataset has a canonical strong flow on a positive initial interval. On
   that interval the stated raw row/HS/readout closure converges to it; actual
   finite GF and simultaneous raw GD for every vanishing step sequence have
   the stated observable limits. Predictions extend uniformly to the input
   circle. Paired hidden activation displacement is positive at sufficiently
   small positive times, and visited-law affine-fit errors stay positive on
   a sufficiently short interval.
2. For bounded activations in that class at the orthogonal reference, the
   canonical flow is global and has loss at most `exp(-4 q0 t)`, where `q0`
   is the strictly positive displayed initialization moment. Consequently
   the displayed `T_phi` gives loss at most `1/8`. B.1 provides finite GF
   capture and its sufficient `eta_n sqrt(n) -> 0` raw-GD condition. This
   does not itself supply the longer-horizon dense-closure tails.
3. For the full activation class, the same loss inequality holds on each
   existing strong canonical symmetric reference interval. The clock-Euler
   norm/readout-tail interface is a sufficient construction criterion;
   its hypotheses are not established through `T_phi` in general.
4. Given S and E on any fixed horizon, the dense hierarchy converges to that
   strong target, and the separate finite-network bridge is valid. Fixed
   hierarchy orders are globally well posed and have the stated separate
   cubature/time consistency. Arbitrary-precision execution requires the
   expressly added activation-evaluation interface.
5. The source route proves its mesh-uniform estimates under the response-row
   cap, an explicit sufficient cap inequality, and a short-time cap choice.
   Its first-raw-Euler curvature obstruction is valid with its restricted
   conclusion. The independent-row Gaussian driver lemma is also valid;
   neither result supplies the missing reinsertion/continuation theorem.

## Component and dependency audit

### Model, metrics, and foundational construction — PASS

The mean-loss factor, `sqrt(d)` input normalization, stored variances
`(1,1/n,1/n^2)`, and mobilities `(n,1,n)` agree throughout the operative
arguments and with the frozen finite implementation. The sample projection
Gram factor is retained. Only the learned middle increment is HS; no claim
makes the initialized Gaussian action HS. Normalized finite vector pairings
make population rank-one maps correspond to `uv^T/n`, and the finite HS
metric is the ordinary matrix Frobenius norm.

I inspected the complete Gaussian-program conditioning proof, singular-query
regularization, named-source derivative convention, common-space completion,
adjunction, rank-one estimates, multiplier continuity, and strong chain
rules. The adaptive conditioning is performed successively with inputs
measurable from the preceding transcript. Source covariances use uncentered
operand Grams; independent oriented *source groups* are not independent
answers to the two actions. The response correction preserves the transpose.
Singular covariance is treated through fixed Gaussian extensions and
square-root continuity, not continuity of pseudoinverses.

A.1 supplies the continuous at-most-linear value instructions required for
the C1,1 Euler programs and clock transform. A.2 supplies the separately
justified source derivatives for smooth fixed programs. The local C.2
argument actually retains weighted source pulses and chooses finite response
caps before shortening time. Its chronology avoids assuming the current
unconstructed backward row. Its Jensen estimate needs marginal Gaussian
tails, not maxima over mesh histories. C.1's localization adds one cutoff
factor at each backward substitution rather than multiplying such factors.
Its mollification constants involve only the stated C1,1 bounds.

The supplied finite-energy proof gives global finite-dimensional GF and raw
norm bounds. Extending its local Lipschitz argument from C2 to C1,1 is valid
for the finite products here. It does not imply ambient Hilbert local
Lipschitzness or population continuation. This distinction is preserved.

### Reference symmetry, radial inequality, and activity — PASS

Exchanging the orthogonal first-row anchor coordinates and negating the
readout sends predictions to `(-f2,-f1)` for every activation; oddness is
unnecessary. The loss and raw metric are invariant, and the initialized
array law has this symmetry. The deterministic canonical limit therefore
has `f1=-f2=b`. A hypothetical continued branch needs the stipulated
canonical symmetry/uniqueness; the proof explicitly does not assign it to
every arbitrary branch.

For `h=(H1-H2)/2`, the displayed J and J* have the correct raw row and HS
normalizations. Along feature ascent, `c'=h`, `h'=JJ*c`, and
`b'=||h||^2+||J*c||^2`. Once `c` leaves zero, monotonicity of `b` prevents
return. Differentiating `N=||c||` gives
`N''=(||h||^2+||J*c||^2)/N-<c,h>^2/N^3 >= 0`.
Since `N'(0+)=sqrt(q0)` and `N'<=||h||`, the lower bound on `||h||^2`
follows. This uses the strong curve chain rule, not a false global Frechet
derivative of a nonlinear L2-valued activation map.

The first-feature covariance `v I + mu^2 11^T` is positive definite because
`v>0`; the upper initial Gaussian pair has full support. Thus `q0>0` for
every nonconstant activation here, without a class-uniform lower bound.
The physical scalar equation `b_t=2(1-b)K` makes `1-b` positive on every
compact strong interval, justifies feature time there, and gives exactly
the factor four in the loss exponent. B.1's hypotheses cover the bounded
subclass, including flat/nonmonotone gates and the retained finite Gaussian
readout. The common anchor-length rescaling also carries the required
first-layer derivative factor. The equal-label and balanced-sign extensions
use the corresponding exchangeable orthogonal geometry and do not assert
arbitrary mixed-label symmetry.

The complete weighted C.3 correction was inspected. Its operative label
coefficient is `p_a=omega_a y_a`, not `y_a`. Ridge-function independence
gives positive first-feature Gram even when the input Gram is singular.
The reused forward/reverse/forward calculation leaves an independent upper
Gaussian component of positive variance. This both prevents cancellation
and survives multiplication by an upper gate that is nonzero with positive
Gaussian probability. The lower activation coefficient likewise retains
its nonzero squared-gate diagonal term. Consequently the stated paired
activation, not merely preactivation, displacement is positive. Continuity
of the variance/covariance formula preserves positive affine-fit error.
These are early-time conclusions, not fitting-endpoint assertions.

### Dense dictionary, initializer, and fixed-order dynamics — PASS

The probe language is independent of the target activation and future path.
Its bounded sine/cosine cylinder tests are total by the included Fourier
argument. Tanh truncations recover unbounded words in L2. Actual action and
adjoint closure make the two observable spaces reducing. Thus the proof
does not quietly replace the Gaussian action by an independently generated
reverse map or by arbitrary supplied covariance.

At every fixed prefix the smooth probe programs have the bounded derivative
envelopes required by the finite source theorem. The target activation is
never source-differentiated to arbitrarily high order. Positive feature ridge
handles duplicate or dependent features. The displayed spectral estimate
for `(I-Q_N)S_N v` is correct (`eta^2 lambda/(lambda+eta)^2 <= eta/4`).
Density and contraction then give strong, not operator-norm, convergence.

Equations (8) are the actual gradient dynamics in row L2, readout L2, and
finite matrix Frobenius coordinates. Their filtered lifted increment is
`Q2 F_K Q1`, as required. For fixed order, bounded marks and `w=g+v`
permit a local contraction in bounded `v,c,M` spaces despite unbounded g.
Energy gives common L2/Frobenius displacement bounds. The pointwise speed
bounds use `||M|| <= ||D||+sqrt(T E0)`, and prevent finite-order blow-up.
The constants needed for this continuation may depend on order, as stated.
The saved joint laws retain the frozen marks and their current correlations;
own-state restart needs no omitted time history. These are two law fields,
not a finite list of scalar coordinates before quadrature.

### Target comparison, observations, and finite capture — PASS conditional

Under S/E the same one-reference estimate proves uniqueness and Euler
convergence to S by a stopped comparison. This justifies observable-space
invariance without assuming ambient Lipschitzness. Strong action convergence
is then used only on compact target node curves; the filtered HS velocity
converges by finite-rank approximation and a compact-curve net. This supplies
vanishing *production* error in addition to stability.

The two unbounded multipliers are reference c at the upper gate and
reference q at the lower gate. Their localization terms add: upper gate
error is propagated by bounded actions/gates before the lower cutoff is
introduced. The resulting growth is `C(1+R)`, not `C R^2`. Target-only
exponential tails therefore give the displayed logarithmic Osgood modulus.
Approximate-state tails are not assumed. The weaker Osgood interface has
the appropriate divergent reciprocal integral; uniform integrability alone
is not substituted for that condition.

The common-carrier L2 comparison controls predictions, actual adjoints,
fixed typed observation graphs, W2 joint laws, and quadratic contractions.
Gate products require a deterministic bounded envelope shared across
approximants. Initial/current pairs use the same carrier and saved roots;
independent coupling of their marginals would not suffice. The target
input-Lipschitz bound and finite circle nets give the claimed whole-circle
prediction upgrade. No cross-width operator distance or cross-population
neuron pairing is asserted. The reached complete-hierarchy statement is
restricted to matching realized states with action-intertwining observable
isometries, not arbitrary formal moment sequences.

The longer finite-network bridge uses fixed finite oracle transcripts with
deterministic scalar feedback, then within-width raw comparison; it does
not apply a fixed-program theorem to a growing transcript. At fixed mesh,
the recomputed proxy nodes converge by bounded actions and reference
localization. Euler convergence to S supplies proxy tail bounds up to a
vanishing node error. Cutoff removal on short subintervals is valid: first
establish the mesh-limit vanishing of each interval's endpoint discrepancy,
which is itself independent of the cutoff, and then use it at the next
interval with a newly fixed cutoff. No single cutoff is improperly held
through an arbitrarily long exponential amplification. The initial actual
readout is never reset; its vanishing RMS is an initial comparison error.

### Numerical consistency and implementation scope — PASS conditional

The Gaussian cubature, separate frozen-coefficient mark replay, covariance
regularization removal, and fixed positive feature ridge have distinct
roles. The bounded mark envelope persists through numerical approximations.
The mark stability estimate treats the unbounded first activation using
Cauchy--Schwarz; fixed-order upper readout/q bounds control remaining gate
products. Atomic dynamics are a finite locally Lipschitz ODE, so stopped
Euler/Heun consistency on a compact horizon is justified without a discrete
energy law. The nested limits put closure order last; an arbitrary diagonal
or effective accuracy-to-order rule is not claimed.

The computability qualification is necessary and correctly included:
regularity alone cannot evaluate an arbitrary activation containing a
noncomputable constant. No general-activation executable closure solver is
delivered by this packet. The storage count retains mark weights, frozen g,
current fields, M and D and is correct as stated; finite precision bit cost
is explicitly additional.

### Source cap, rare-event obstruction, and auxiliary partials — PASS

In SOURCE_PROOF the clock program is clearly distinguished from raw Euler.
The lower pulse carries its mesh/sample weight and obeys deterministic
Gronwall under the beta-row cap. The upper source row includes the current
`E[c phi''(Z)]` term. Under the cap, the lower/upper moment majorants are
finite on any fixed horizon. The upper row's random integrating factor is
controlled using marginal subGaussian moments and time-weighted Jensen;
the cap test `Psi_T(B)<B` is a genuine chronological sufficient condition.
For fixed B it closes locally. The text does not claim that its rapidly
growing bound can be closed globally or restarted with fresh independence.
The C1,1 passage is conditional on cap constants uniform in mollification.

For `phi(z)=z+epsilon sin(z)`, the first population raw Euler state has
unchanged hidden weights and `c=h(phi(Z1)-phi(Z2))`. On the displayed rare
events, the unit-HS concentrated rank direction affects only sample one;
its first prediction derivative tends to zero while its second derivative
grows positively. The negative residual therefore makes loss curvature
unbounded below. Every fixed direction has justified scalar derivatives.
This contradicts local Lipschitzness of the raw gradient (and the clock
field's identical K component) at that state. The directions are adapted
rare-event directions; this is not a no-go theorem for independent probes,
actual GF existence, source tails, fitting, or closure.

The feature-energy example correctly disproves the inference of a uniform
spatial exponential moment from Hilbert-speed energy alone; it is not
claimed to be a neural trajectory. The bounded-activation truncation
discussion correctly retains reached weighted gate-tail defects. In the
row-removal partial, deleted dynamics are independent of the removed
initialized row, and finite energy bounds the trace of the conditional
Gaussian path covariance. The exponential Hilbert-Gaussian estimate and
the absolute-continuity supremum estimate are valid. The adaptive
reinsertion term remains uncontrolled and is expressly not dropped.

## Deterministic reproduction

Working directory was `/home/amir/Codes/PDE`. Imports were restricted to
the frozen `review_r2_inputs/code` by `PYTHONPATH`. Python bytecode writing
was disabled. `OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS`, and `MKL_NUM_THREADS`
were all 1. Environment: Python 3.10.12, NumPy 1.26.4. An RLIMIT_CPU of
120 seconds was set for validation processes; total validation CPU was
under one second. No trajectory fitting/training experiment was run.

Reproduction commands (with the above environment):

```sh
python -B data/generated/cx2_activation_class_20260919/review_r2_inputs/check_identities.py
python -B data/generated/cx2_activation_class_20260919/review_r2_a/audit_checks.py
```

The supplied test file passed both test methods and all four activation
subcases: nonodd flow/raw-step symmetry and the feature-ascent chain rule
with the correct raw metric. Result: 2 tests, 0.060 seconds, exit 0.

The independent check used a fixed supplied state and every raw block,
four activations (softplus, oscillating linear, nonodd bounded, flat-gate
C1,1), three geometries (orthogonal, correlated, antiparallel), nonunit
mobilities, and independent forward/loss finite differences. All twelve
combinations passed. Maximum absolute errors were:

| Quantity | Maximum absolute error |
|---|---:|
| Ordinary loss gradient | 1.6765015417585794e-10 |
| Mobility-weighted flow | 1.1185394832580187e-09 |
| Individual kernel blocks | 2.375077912120105e-10 |

The frozen guide example also ran successfully; its two reported losses
were 0.7410221085761991 and 0.7398799811970899. This single update is an API
reproduction, not evidence for training convergence. The complete frozen
finite implementation and both package-import dependencies were inspected.
The guide's broader repository-wide test suite is not included in the
packet and was not fetched or claimed to have been run. It is unnecessary
for reproducing the supplied candidate checks. No missing scientific input
is needed for the operative proofs audited above.

Evidence is retained in `review_r2_a/identity_checks.txt`,
`review_r2_a/audit_checks.py`, `review_r2_a/audit_checks.txt`, and
`review_r2_a/environment.json` under the assigned generated namespace.

## Complete read coverage and integrity

Every line of each file below was read, including all proof bodies, supplied
foundation sections, API guide, validation source, and transitive local
imports. The first combined PARTIAL/REFERENCE display was truncated inside
REFERENCE; I repaired it by explicitly reading REFERENCE lines 60–161.
All remaining reads used bounded, contiguous chunks. Total file coverage is
5,643 lines; no scientific component was skipped.

All thirteen SHA256 values and manifest line counts matched before review,
and all matched again after scientific inspection and checks. The final
verification record is `review_r2_a/verified_hashes_after.json`. The manifest
itself has SHA256 `e157377112c43577948b3a90c8966ff929ebc5c8154d29fc98416898a5e7bf37`.

The exact original before-review command and output, recovered from the
reviewer's still-visible tool transcript and persisted afterward, are in
`review_r2_a/verified_hashes_before_original_transcript.txt`. This is the
original check's transcript, not a newly computed before-check record.

| File | Complete lines read | Verified SHA256, before and after |
|---|---:|---|
| PARTIAL_RESULT.md | 1–230 | a47d85ca451bfe1d70e44fad4cb695d5011445a19b0ab9f182e8b5bf4293cd1b |
| REFERENCE_PROOF.md | 1–430 | 535d4576ac2de2711bcacbed64d5864d2207a54eb1b7bc84bc668e8402395be7 |
| CLOSURE_PROOF.md | 1–741 | 15270cb49004fe359c49722508ad0c96695d8ddb2f939a66b84939a3be0f0d6c |
| SOURCE_PROOF.md | 1–651 | 4b944a9c4bfe290a4b294a3586d1c67607ac776926482beeb8fa832c2613ceff |
| check_identities.py | 1–90 | 22e441ce52e0e3efab6aa91708c5ff5a0460fa876660c0e812c450eca0982f44 |
| NOTATION.md | 1–98 | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| global_A_B_C.md | 1–1996 | 58e7dc1d8cf7abd991fcba7e305d084bfb522795cc5b9aee443c183fe4fa1c03 |
| gaussian_foundation.md | 1–542 | 8a8dbe6a31a51d3f73c999b75c75dcade76b3d533c8901a062c66587776cdd0a |
| finite_energy.md | 1–227 | bd10bbff9d16f60c63d26b06e793510fa19958e1ec91dbdd85709caff7d96980 |
| finite_code_guide.md | 1–135 | 3737d8f30a80aa3b14cfcb67cdffed160c5a98507ee95a151adac385e33ed9d2 |
| code/pde/finite_network.py | 1–363 | efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551 |
| code/pde/__init__.py | 1–26 | 65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3 |
| code/pde/gaussian_moments.py | 1–114 | 6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae |

## Unresolved obligations and completion

There are no unresolved correctness objections within the scoped positive
and conditional statements. Full C-X2 still needs strong canonical
continuation for every unbounded activation through the activation-dependent
fitting horizon, adequate reached-source/tail control for that construction,
and continuation/tail control on a positive correlated-input neighborhood
through the same horizon. The general-activation executable closure solver
and its validation are also absent. Energy bounds, endpoint completeness,
global bounded approximants, and the independent-row Gaussian driver do not
by themselves provide the missing bridges.

Complete review of every frozen component and operative dependency is
finished. The verdict applies only to the identical hashed packet and its
expressly limited claims.
