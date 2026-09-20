# Independent internal review of the SGD and noise routes

Reviewer: scoped agent `review_noise_routes`, 2026-09-19.

This is an internal mathematical review, not a promotion review. The neutral
assignment was to audit the sample-gradient/noise geometry, stationary-state
classification, step-size probability arguments, cubic examples, additive
diffusion, independent-population-mark obstruction, and persistent-noise scope.
The complete scientific inputs were `docs/observable_p1.md`,
`docs/NOTATION.md`, `sgd_geometry.md`, and `noise_escape.md`. The first two were
read completely as the supplied established model. No README, study history,
other study, other review, maintained implementation, or external source was
read. The rigorous-mathematics skill was used. No experiment was needed or run.
Only this report is written.

## Verdict

**PASS for the final reviewed versions, with no unresolved assigned-scope
mathematical defects identified.** The principal results pass the mathematical
audit, including the mixed-binary
realizability extension in `sgd_geometry.md` Section 9. The exact-gradient and
covariance identities, common-sample-stationarity characterization, fixed-step
escape/point-limit results, Robbins--Monro necessary condition, cubic absorbing
examples, additive-noise well-posedness and ball-exit estimates, and the
population-mark counterexample are sound under their stated hypotheses.

Two localized corrections were raised during review and are resolved in the
final hashed versions below. Neither changes the principal conclusion that the
proposed local arguments do not prove global zero-loss convergence from
`(g,0,D)`. The original issues and their resolutions are recorded here.

1. **Summable-step proof establishes positive loss, but does not yet establish
   failure of mean stationarity.** In `sgd_geometry.md` Section 6, the paragraph
   beginning “With summable steps even mean stationarity need not follow”
   confines the iterates to a ball where loss is positive. A positive-loss
   point can be mean stationary, so this does not prove the stronger opening
   claim. For that claim, choose a dataset for which the initial mean gradient
   is nonzero, and choose the ball so the gradient stays bounded away from zero
   as well as the loss staying positive. The same total-step bound confines all
   iterates there; bounded gradients and summability make the trajectory
   Cauchy, and its limit is nonstationary. Alternatively, narrow the paragraph's
   opening claim to failure of zero-loss convergence, which its existing proof
   already establishes. **Resolved:** the final Section 6 takes the latter
   option and explicitly disclaims a conclusion about the limiting mean
   gradient. Section 10 records the correction.
2. **Nonzero first label moment does not imply realizability.** In
   `noise_escape.md` Section 3, `m_y != 0` proves cubic descent from the origin,
   but the next sentence also says the obstruction is not caused by an
   unrepresentable target. That latter assertion should explicitly refer to
   the subsequent one-input example. Two copies of the same nonzero input
   with labels 1 and 2 already have `m_y != 0` and are unrepresentable. The
   explicit one-input construction correctly proves that the obstruction
   persists on a realizable problem; the mixed-binary construction in the
   other reviewed route proves a stronger existential example. **Resolved:**
   the final Section 3 explicitly separates the nonzero-moment/nonminimum
   conclusion from the subsequent single-input representability construction.

## Detailed coverage

### Gradients, covariance, and stationarity

I rederived the three components of `df_a` using the population L2 and matrix
Frobenius metrics. They give precisely `g_a = 2 r_a J_a`, including the
unhalved-loss factor 2 and the same matrix's transpose in the backward action.
There is no extra population probability in the physical row gradients.
Bounded frozen features, Lipschitz tanh/gates, and finite data give gradients
that are Lipschitz and bounded on every state ball. This holds in the stated
Hilbert state; it does not use compactness of Hilbert balls.

For independent draws with replacement, conditioning on the past gives

\[
E[\widehat g]=g,\qquad
\operatorname{Cov}(\widehat g)
=\frac1B\sum_a\mu_a(g_a-g)\otimes(g_a-g).
\]

The vanishing cross terms, directional quadratic form, range, and rank bound
`m-1` are correct. Positive sample weights are necessary for the claimed
equality between the covariance range and the span of all listed centered
gradients. At a mean stationary state, the trace identity proves that zero
covariance is equivalent to all sample gradients being zero. Away from mean
stationarity, coincident nonzero gradients give zero covariance with nonzero
drift, as the text correctly distinguishes. Batch size three scales covariance
by one third and creates no new directions.

The canonical feature Grams are strictly positive definite. For a lower
coordinate pair, conditioning on the original Gaussian first mark gives
strictly positive conditional variance for its reverse tanh feature. This
rules out a nontrivial linear relation involving that reverse feature; the
remaining first tanh feature has positive variance. Independence across
coordinate pairs and invertible ridge normalization preserve definiteness.
The upper features have positive diagonal covariance. Removing the constant
features in the odd representation preserves definiteness.

For `r_a != 0`, the readout component of `g_a=0` forces `h_{2,a}=0` almost
surely and hence `M a_a=0`. Thus `f_a=0`, `y_a != 0`, and the backward
contraction reduces to `v_c=E[b_2 c]`. The remaining matrix and lower-field
components give `v_c a_a^T=0` and `M^T v_c=0`. The latter implication uses
both `u_a != 0` and strict positivity of the tanh gate at every finite field
value. An L2 field is finite almost surely. Positive definiteness of the
feature Grams then supplies the claimed coefficient conclusions. The reverse
implication is immediate by substitution. The stated unit-input and positive
Gram assumptions cover these requirements; this classification is not asserted
for arbitrary singular finite tables or zero input.

Both displayed absorbing families satisfy every individual gradient equation,
for any batch and step schedule. Their existence is an ambient-state result.
It does not prove accessibility from the initialized state.

### Step sizes and probability arguments

The fixed-step neighborhood argument is exact: continuity gives a uniform
lower bound for one sample gradient, and an all-identical batch then moves by
more than the ball diameter. The conditional probability is `mu_a^B`, so the
geometric tail and expected exit bound follow without any Hessian condition.
These are spatial-exit bounds, with a radius dependent on the step lower bound.

For deterministic steps with positive limsup, a deterministic subsequence has
steps bounded below. Independent all-identical batches occur infinitely often
on it for each of the finitely many samples. If the state has an H point
limit, its increments vanish; the corresponding individual gradients therefore
vanish along those subsequences and at the limit by continuity. This handles
a random limiting state without an uncountable union over candidate limits.
The limitation on steps chosen after viewing a batch is appropriate.

The Robbins--Monro proof is valid as a necessary condition conditional on state
convergence. Stopping before exit from each deterministic ball makes noise
increments uniformly bounded and preserves conditional centering. Their
weighted Hilbert-valued martingale has summable squared increments. The stated
maximal estimate and summable tail argument prove almost sure convergence of
that martingale. A convergent state path is contained in one integer-radius
ball. On that path, projecting the summed update onto its nonzero putative
limiting mean gradient would give a drift tending to minus infinity, a
contradiction. The random direction causes no problem after vector martingale
convergence is established. This proves mean stationarity only; it does not
establish convergence or common-sample stationarity.

The summable-step confinement bound itself is correct, including its validity
for every batch sequence. Its final interpretation incorporates correction 1
above and asserts positive-loss failure only.

The Section 7 one-step loss identity also passes. At `c=0` and mean
stationarity, an SGD step changes only the readout, the prediction is linear
in that change, and the mean linear cross term vanishes. The exact loss
increment is therefore the sum of squared new predictions. An all-identical
batch from a sample with nonzero `y_a h_{2,a}` makes that sample's new
prediction nonzero because its activation Gram diagonal is positive. This
establishes the stated lack of a universal one-step decrease, without making
a claim about later feature movement.

Dividing actual step covariance `eta^2 C_1/B` by the step's physical duration
`eta` gives the formal diffusion covariance `eta C_1/B`. The listed finite
noise columns have precisely this covariance and vanish, together with the
drift, at common-sample-stationary states. Their local Lipschitz property
supports uniqueness of the constant local solution at such a state. The
report correctly treats this as a formal moment-matched diffusion, without
claiming a discrete-to-diffusion or infinite-time transfer theorem.

### Cubic examples and the binary-label extension

Both origin constructions use admissible fields and the full p=1 matrix
architecture. The lower contraction is linear to first order, the selected
upper preactivation is of second order, and multiplication by the readout
produces the stated cubic. The lower tanh remainder produces order five in
prediction; the upper tanh remainder first produces order seven. Squaring
predictions produces order six and is therefore absorbed in the stated
order-five loss remainder. All required feature moments are finite and the
restricted perturbation features are bounded.

The full Hilbert-space Hessian claim at the origin also passes: the bounds
`a_a=O(||w||_2)`, `h_a=O(||M|| ||w||_2)`, and
`upsilon_a=O(||c||_2)` in the gradient imply
`||grad L(theta)||=O(||theta||^2)`. Thus the gradient has Frechet derivative
zero at the origin, without assuming a globally twice differentiable loss.
The nonzero odd cubic gives descent and ascent directions.

The original three-point example is exactly realizable by its defining state.
For Section 9, the scalar arguments `1`, `6/(5 sqrt(2))`, and
`4/(5 sqrt(2))` are distinct positive numbers. The derivative of `A(t)` is
strictly positive, so the three upper scales are distinct and positive. If
a linear combination of the three upper tanh functions has zero L2 norm,
positive support of the upper mark on every open subinterval and continuity
make that combination vanish on `(-1,1)`. Its coefficients of degrees 1, 3,
and 5 yield the displayed nonsingular Vandermonde system. The Gram is
therefore strictly positive definite.

The readout `sum_a (Q^{-1}y)_a psi_a` is bounded, odd, and an admissible L2
readout. The finite feature dictionary does not require the moving readout
to remain in the span of the frozen feature columns. The readout contracts to
exactly `(1,1,-1)` on the three inputs. The cubic coefficient for these labels
is `-2K/3`, and the origin has loss one and zero sample covariance. This is
an exactly realizable mixed-binary ambient counterexample. The text correctly
retains the missing canonical-reachability qualification.

### Additive perturbations and spatial escape

The drift bounds in `noise_escape.md` Section 1 are correct. On a finite
interval with continuous additive H-valued forcing, first the linear
readout bound and Gronwall control `c`; the matrix bound then controls `M`;
the lower-field bound then controls `w`. The drift is bounded and Lipschitz
on these state balls, so the local integral-equation solution extends globally
in time. This gives pathwise well-posedness for continuous trace-class
Hilbert Brownian forcing as asserted.

For a nonzero homogeneous cubic on a finite-dimensional perturbation space,
its zero set has Lebesgue measure zero. A nondegenerate centered Gaussian
therefore has a nonzero cubic almost surely, and symmetry divides its sign
probabilities equally. Pointwise convergence followed by dominated convergence
of indicators proves the limiting one-half descent probability. This requires
noise with support on such a cubic, rather than merely a nonzero variance
somewhere in the state space.

The repeated-kick lower-loss event follows from continuity and a positive
support-ball probability. The geometric estimate concerns histories staying
in the specified pre-kick neighborhood while never reaching the lower-loss
level. Leaving that neighborhood alone certifies no loss improvement. The
trace-class full-support Gaussian construction is valid; finite-rank support
also suffices when it includes the specified descent perturbation.

For ball exit under additive Brownian forcing, choose a scalar projection
with positive noise variance. On a path remaining in the ball during a block,
the scalar displacement is at most its diameter and the integrated drift is
bounded by `B Delta`. An independent Brownian increment exceeding their sum
forces exit. This proves the stated geometric tail and finite mean exit time,
including in the infinite-dimensional state. Uniform ellipticity and negative
Hessian eigenvalues are unnecessary. The conclusion is spatial exit, and the
bound is not uniform as the noise amplitude tends to zero.

### Independent population marks and persistent noise

Identity-covariance Gaussian noise cannot be H-valued in the infinite-dimensional
population space. The coordinate argument in the report correctly demonstrates
this. Enlarging the population probability space and integrating fresh marks
inside each population expectation is a distinct, explicitly described
distributional interpretation, rather than an identity-covariance H-valued
random perturbation on the original frozen-mark space.

Under that interpretation, the induction is exact. The lower perturbation
remains symmetric and independent of its frozen feature vector, giving
`a_a=0`. The upper readout remains centered and independent of its features,
giving `upsilon_a=0`. Consequently every sample gradient vanishes even with
an arbitrary common middle matrix conditioned upon in the expectations. Every
finite step is square integrable. This works before or after gradient steps,
between exact gradient-flow intervals, and with any minibatch size. Extending
the simultaneous sign negation to the fresh marks preserves the odd state
class. The qualification that empirical finite-population averages generally
break these exact cancellations is essential and is present.

The one-input realizability construction is valid. Its positive lower
contraction and positive readout/upper-activation pairing permit exact fitting
by a finite scalar multiple of the selected upper feature. The final wording
incorporates correction 2 above.

The interpolator readout-kick identity is exact. The persistent-noise argument
also passes under its explicit eventual positive-variance hypothesis: a normal
variable with arbitrary mean and variance bounded below has a uniformly
positive probability of leaving a fixed interval about zero. Conditional
iteration gives infinitely many positive-loss post-kick states. Strictly
positive covariance supplies this lower bound locally near a finite
interpolator with a positively weighted nonzero label. It supplies neither a
global variance lower bound nor a conclusion along unbounded representations
whose noise sensitivity can vanish. The report correctly keeps both limits
of scope. The annealing discussion and the distinction from negative-Hessian
escape theorems are also accurate.

## Coverage limits and version record

No assigned mathematical input is missing. This review does not validate
maintained code, numerical behavior, upstream Gaussian-source derivations
outside the supplied established file, finite-width identification, or global
canonical-initialization fitting. The latter remains unproved in both routes.
The necessary data compatibility statements follow from exact oddness of
prediction in the input; they do not alone prove representability or fitting.

All four complete files, including Section 9 of `sgd_geometry.md`, were read.
The subsequent changed paragraphs and added correction provenance were read
and checked before finalizing this review. The final reviewed SHA-256 values
are:

```text
0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba  docs/observable_p1.md
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
619f6c0f3148b72f764a8bacaf92aa434801e94323af0b343a3e1904e01cdf0e  studies/p1_stochastic_escape_20260918/sgd_geometry.md
9fa48de193e103925eb86e4be38a64959c4881b0d217ca669033510b01f4a12b  studies/p1_stochastic_escape_20260918/noise_escape.md
```

The first route's appendix was present when read, after the initial prefix
audit. Its own provenance identifies it as an informed post-freeze extension;
that is not treated as independent discovery. This review's scientific verdict
was derived independently from the supplied equations and complete arguments.
