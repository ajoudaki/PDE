# Sampling and higher-accuracy representations of response memory

Started 2026-10-03. This new study investigates further compression of the canonical width-n, order-q response-memory closure. It is a different approximation axis from dense-to-population convergence.

**Latest integrated-comparison continuation (2026-10-04):**
[INTEGRATED_COMPARISON_CONTINUATION.md](INTEGRATED_COMPARISON_CONTINUATION.md)
records the current results and the still-open requested theorem. The
fully explicit sharp package covering compact versus dense, independent
dense versus dense, and Legendre versus dense with unbounded activations
has **not** been proved. In particular the general independent-dense
upper bound still has a subpolynomial width factor.

There are new actual nonlinear variability lower bounds. The
[trajectory and endpoint proof](INTEGRATED_DENSE_LOWER_ROUTE.md), with
[coordinator reconstruction](INTEGRATED_COMPARISON_CHECK.md), establishes
the scale \(Y\sqrt{m/n}\) during training on an orthogonal-data family
with arbitrary label signs, and \(|y|/\sqrt n\) at the fitted endpoint
for one input. The key is a conditionally centered, fluctuation-scale
bound on the complete nonlinear remainder. The
[fixed-confidence refinement](INTEGRATED_LOWER_CONFIDENCE.md), with
[complete check](INTEGRATED_LOWER_CONFIDENCE_CHECK.md), supplies an
explicit lower coefficient for any fixed confidence. It uses the new
[finite-depth initialized covariance CLT](INTEGRATED_INITIAL_VARIABILITY.md)
and its [complete check](INTEGRATED_INITIAL_VARIABILITY_CHECK.md), without
assuming that a zero-label derivative describes fixed-label training.
The [endpoint confidence refinement](INTEGRATED_ENDPOINT_CONFIDENCE.md),
with [coordinator reconstruction and compression corollary](INTEGRATED_ENDPOINT_COMPARISON_CHECK.md),
gives \(\delta|y|/(4\sqrt n)\) at the actual fitted endpoint with
probability at least \(1-\delta\), under its explicit fixed label cap.
Combining it with the existing compressor upper bound proves an actual
constant-factor comparison to fitted dense variability in this one-input,
two-tanh example; the retained compressor size is polylogarithmic in n.

The [dense upper extension](INTEGRATED_DENSE_VARIABILITY_ROUTE.md)
establishes the requested whole-sphere, all-time topology at the inherited
near-root rate, including endpoints. The prediction-directed adjoint and
[neuron-replacement attempt](INTEGRATED_NEURON_REPLACEMENT_ROUTE.md)
identify the unclosed mixed sensitivity products needed for a strict
root upper bound. They neither assume those estimates nor produce a
slower-rate neural counterexample.

The [general Legendre reuse](INTEGRATED_LEGENDRE_REUSE.md), with
[scope and arithmetic check](INTEGRATED_LEGENDRE_REUSE_CHECK.md), verifies
that \(q_n=\lceil n^{1/4}\exp([\log(e+n)]^{3/4})\rceil\) suffices
for strict root-width error under the inherited broad small-label theorem.
This retains the original RMS clock and a common event for all orders
at each width. The general result does not require a one-sixth-order
extension; its physical constants remain qualitative.

The [label-sensitive storage refinement](INTEGRATED_LABEL_STORAGE_ROUTE.md)
and [complete reconstruction](INTEGRATED_LABEL_STORAGE_CHECK.md) retain
the actual \(Y\) in the tanh compressor: the leading squared source
coefficient contains \((Ym/\gamma)^4\). This improves the fixed-activity
asymptotics but has a worse sufficient-width threshold for small labels.
The current dense metrics and sample solves still require quadratic
sample storage. No linear-in-m or sharp unbounded-activation extension
is claimed. No experiment, GPU job, manuscript edit, Git mutation,
promotion, or concurrent-work reset was performed in this continuation.

**Latest normalized-route continuation (2026-10-04):**
[NORMALIZED_ROUTE_CONTINUATION.md](NORMALIZED_ROUTE_CONTINUATION.md)
records the new proofs and the still-unresolved full theorem. The requested
polynomial-depth, fully explicit all-time compression label/error/storage
triple has **not** been established. No previous forecast is promoted to a
theorem by this continuation.

The [near-critical geometry](NEARCRITICAL_GEOMETRY_ROUTE.md) computes the
exact initialized gain \(\chi^L\), where
\(\chi=\mathbb E\phi'(Z)^2\), and supplies an explicit unbounded,
nonlinear, variance-stable linear-plus-erf family with
\(\mathbb E\phi(Z)^2=1\) and tunable \(\chi\) on both sides of one.
The [all-order majorant](NEARCRITICAL_ALL_ORDER_ROUTE.md), with
[reconstruction](NEARCRITICAL_ALL_ORDER_CHECK.md), controls every
initialized population derivative order with one analytic radius. At
criticality its angular radius is of order \(L^{-1/2}\). A fixed
\(\chi>1\) does not give polynomial depth costs; a depth-scaled tolerance
is quantified explicitly.

There is new actual trained progress. The [two-layer first-gate proof](TRAINED_NORMALIZED_RESPONSE_ROUTE.md)
and [check](TRAINED_NORMALIZED_RESPONSE_CHECK.md) bound an all-time,
whole-sphere mixed response for one training input, with no width factor.
The subsequent [integrated tangent proof](TRAINED_TWO_LAYER_TANGENT_STABILITY.md)
and [check](TRAINED_TWO_LAYER_TANGENT_CHECK.md) close both gates at the
observed input after integrating over learning activity. The top hidden
feature's transverse input derivative changes by at most an explicit
constant times \(Y^2\) throughout training and at its endpoint. This uses
the exact independence of frozen transverse Gaussian input columns, not
a Gaussian assumption about trained weights. General queries, higher
orders, arbitrary data and polynomial depth remain outside this trained
result.

The [explicit unbounded fitting proof](EXPLICIT_UNBOUNDED_NORMALIZATION_ROUTE.md)
removes the activation-value bound for real dense fitting at general fixed
depth and finite data, with an explicit label cap and sphere-uniform tail.
Its constants still use real slope supremums and grow exponentially with
depth. It is a fitting theorem, not a new compressor guarantee. The
[coordinator reconstruction](NORMALIZED_ROUTE_CONTINUATION_CHECK.md)
checks this proof and the independent near-critical geometry completely.

A [finite-width complex-moment obstruction](NORMALIZED_COMPLEX_FINITE_WIDTH_AUDIT.md),
with [complete check](NORMALIZED_COMPLEX_FINITE_WIDTH_CHECK.md), shows why
population complex moments cannot simply be substituted into the finite
network: at two layers their unconditional finite-width second moments
are infinite at every fixed nonreal query for erf-type activations.
This does not rule out the desired stopped high-probability estimates,
does not concern real-axis moment divergence, and is not an output-error
or compression lower bound.

All contributions remain internally checked study material. Contributors:
root (all-order majorant, finite-width obstruction, integrated trained
tangent, assembly and synthesis), `nearcritical_geometry`,
`trained_moment_closure`, and `explicit_unbounded_theorem`, with the
nonauthor reconstructions linked above. No experiment, GPU job, manuscript
edit, Git mutation, promotion or concurrent-work reset was performed.

**Previous normalized-activation investigation (2026-10-04):**
[NORMALIZED_ACTIVATION_DEPTH_SYNTHESIS.md](NORMALIZED_ACTIVATION_DEPTH_SYNTHESIS.md)
uses the user's clarified conditions
\(\mathbb E[\phi(Z)^2]=\mathbb E[(\phi'(Z))^2]=1\),
\(Z\sim N(0,1)\), without centering the activation. It does **not**
change the existing all-time compression bounds to beta=1.

The [constant audit](BETA_ENVELOPE_AUDIT.md) distinguishes numerical
floors, analytic radii, deterministic operator gains and Gaussian mean-square
gains. For any normalized nonlinear activation, the derivative supremum is
strictly above one, so the existing supremum-based beta cannot be one even
after removing the numerical floors. A new proof using actual response
moments would be required. The [explicit activation constructions](NORMALIZED_ACTIVATION_EXAMPLES_ROUTE.md)
normalize tanh, erf, exact GELU and unbounded near-identity functions by
output rescaling and offsets; GELU satisfies the unbounded-value extension's
bounded-strip-derivative hypothesis.

The [critical covariance proof](CRITICAL_NORMALIZATION_GEOMETRY_ROUTE.md)
gives unit first sphere-tangent norm, second norm
\(\sqrt{1+3L\mathbb E\phi''(Z)^2}\), and an explicit polynomial
initial Gram-gap bound under its separately stated input-gap premise.
The root's [normalized erf theorem](NORMALIZED_ERF_COMPLEX_GAIN_ROUTE.md),
with [complete reconstruction](NORMALIZED_ERF_COMPLEX_GAIN_CHECK.md), gives
an ordinary-sized monotone activation with unit forward/derivative moments,
variance-map derivative \(1/2\), second derivative energy \(1/3\),
and complex Gaussian moment radius of order \(L^{-1/2}\). At fixed
distinct finite data its limiting initialized gap is asymptotic to \(6/L\).
These are initialization results, not trained response bounds.

The [finite-network fluctuation proof](NORMALIZED_VARIANCE_FLUCTUATIONS_ROUTE.md)
proves an exact Markov recursion and fixed-depth central limit/variance law
for empirical feature norms. A normalized GELU branch satisfying both unit
moments nevertheless has exponentially growing depth coefficients; another
branch, and the normalized erf, have bounded ones. This identifies variance
stability as a substantive extra diagnostic, without claiming an output or
compression lower bound. The coordinator's complete reconstruction and
source hashes are in [NORMALIZED_ACTIVATION_ASSEMBLY_CHECK.md](NORMALIZED_ACTIVATION_ASSEMBLY_CHECK.md).
The scalar examples have an additional
[cross-route reconstruction](NORMALIZED_ACTIVATION_COMPONENT_CHECK.md).
The remaining all-time issue is the actual adaptive mixed product
\(\phi''(z)R_aJ\) and its repeated responses. No such estimate is
silently assumed. No trained-network experiment, manuscript edit or Git
mutation was performed. Contributors: root (erf theorem, assembly and
synthesis), `critical_activation_geometry`, `normalized_activations`, and
`beta_gain_audit`; cross-route checks began after independent candidates
were frozen. All results retain internal study status.

**Previous activation/depth refinement (2026-10-04):**
[ACTIVITY_SENSITIVE_DEPTH_REFINEMENT.md](ACTIVITY_SENSITIVE_DEPTH_REFINEMENT.md)
substantially reduces the structural depth--dimension coefficient for
ordinary tanh and full-rank data. The old \(16^{82Ld}\) envelope is
replaced by an explicit coefficient whose depth growth is
\((64/15)^{2(L-2)(d-1)}\), with the remaining numerical and dimension
factors fully displayed. This does not rely on replacing \(d\) by input
rank. At two hidden layers the depth factor in the query radius disappears;
at larger depth complete removal remains open. The old sufficient label
condition remains valid, and a weaker finite recurrence is provided.

The [tanh proof](ACTIVATION_CONSTANTS_REFINEMENT_ROUTE.md) keeps the
\(S^2\) in learned query corrections and \(YS\) in complex-time motion,
uses actual tanh slope/curvature bounds, proves smaller Gaussian operator
caps, and separates approximation error from the carrier maximum.
Its [complete reconstruction](ACTIVATION_CONSTANTS_REFINEMENT_CHECK.md)
checks the enlarged pole domain and reproduces both deterministic tables.
The leading depth-two storage coefficient at \(d=100\), for example,
falls from about \(10^{19633}\) to \(10^{665}\); the latter remains
impractical. No small practical constant or optimality claim is made.

The subsequent [runtime refinement](RUNTIME_SMALL_ACTIVITY_CONSTANT_ROUTE.md)
and [complete reconstruction](RUNTIME_SMALL_ACTIVITY_CONSTANT_CHECK.md)
retain small label factors in hidden feedback and keep source defects
out of the amplification exponent. For two hidden tanh layers they certify
\[
Y\le2.8\,10^{-7}\gamma/m,\qquad
\sup_{t\in[0,\infty],\,\|x\|=\sqrt d}|f_C-f_n|
\le2.8\,10^5Y(m/\gamma)^{3/2}/\sqrt n.
\]
These supersede the first refinement's weaker numerical cap/error pair,
while retaining its sharpened storage. The same explicit recurrences apply
at every fixed depth. Exact rational checks of the simple depth-two pair
and deterministic evaluations are reproducible by running
`python studies/closure_sampling_20261003/check_small_activity_constants.py`.
The label threshold is still small and the storage constants remain large.

A [contractive nonlinear subclass](CONTRACTIVE_DEPTH_CONSTANT_ROUTE.md),
\(\phi_\ell=c\tanh\), \(0<c\le1/40\), removes the additional
\(C^{Ld}\) factor entirely. Cite it **with the correction** in
[CONTRACTIVE_DEPTH_CONSTANT_CHECK.md](CONTRACTIVE_DEPTH_CONSTANT_CHECK.md):
its external-trace coefficient must maximize over the injection layer.
The corrected bound is still \(0.4\), preserving every final numerical
conclusion. The actual gap obeys \(\gamma\le c^{2L}\), so this does
not give overall polynomial depth dependence at fixed absolute labels.

The [activation-class extension](ACTIVATION_CLASS_EXTENSION_ROUTE.md),
with [complete check](ACTIVATION_CLASS_EXTENSION_CHECK.md), replaces
bounded activation values by a finite value at zero and a bounded
holomorphic derivative on a strip. This includes identity and nonlinear
unbounded examples \(z+\varepsilon\tanh z\). It preserves all-time
whole-sphere \(C/\sqrt n\) error under the positive-gap/small-label
conditions, but currently uses the older, larger storage exponent
\(2[d(L+5)+1]\), with qualitative numerical constants. The sharp tanh
constants are not claimed for this enlarged class. A separate affine
projection argument gives \(C/n\) error and \(O(\log^4 n)\) storage;
identity's positive gap requires independent inputs and \(m\le d\).

The root [initialization lemma](NONEXPANSIVE_INITIAL_QUERY_ROUTE.md)
shows no exponential-depth factor in uniform real query tangent bounds
at Gaussian initialization for nonexpansive slopes. Its attempted training
extension records the unclosed mixed product \(R_aJ\); it is not used
as an all-time theorem premise. The combined evidence/normalization audit
is [ACTIVATION_REFINEMENT_ASSEMBLY_CHECK.md](ACTIVATION_REFINEMENT_ASSEMBLY_CHECK.md).

These remain internally checked study results relative to their explicit
prior mathematical inputs, not book promotion. The canonical dense target,
physical-time comparison, full-sphere norm, endpoint, and existing autonomous
corrected-readout compressor are preserved. All retained coordinates count;
the width threshold, setup work and precision remain unquantified. The
only new numerical calculations evaluated finite proof constants. No
training experiment, manuscript edit, Git mutation or concurrent-work reset
was performed. Contributors are root (synthesis, activity observation,
initialization lemma, runtime reconstruction and assembly), `activation_constants` (tanh route and
separate unbounded reconstruction), `contractive_depth` (contractive route),
`activation_extension` (unbounded/affine route), and
`contractive_independent_check` (both scalar-constant reconstructions,
including the required contractive correction, and the later collaborative
runtime derivation with scoped child `small_activity_error`). The affine subcheck is
incorporated with its provenance into the unbounded reconstruction.

**Previous input-dimension refinement (2026-10-04):**
[INPUT_DIMENSION_REFINEMENT.md](INPUT_DIMENSION_REFINEMENT.md) combines
two improvements. Intrinsic spherical approximation removes the growing
dimension-only prefactor. A new strict root-width query-folding theorem
also replaces ambient dimension in the expensive storage factors by
\(D=\min(d,r+1)\le m+1\), where \(r\) is the rank of the training
input span. Rank is measured from the given data, not a new restriction.
Use the activation-only \(\beta\) below (\(16\) suffices for tanh),
\(\gamma=\lambda_{\min}(Q^{(L)})>0\), and label RMS \(Y\).
The unchanged sufficient label condition and improved total retained size are
\[
Y\le(\gamma/m)\beta^{-62L},
\]
\[
\begin{split}
\operatorname{size}(C)\le{}&
\beta^{82LD}\frac{(D+3)^D}{(D!)^2}(m/\gamma)^2\log^{3D+2}(en)\\
&+2040(L+1)(2m+D+1)^2+10m(d+1)+10d(r+1).
\end{split}
\]
The factorial ratio is at most \(25/4\). At confidence \(1-\delta\),
write \(J_\delta=d+1+\log(1/\delta)\). The full error is
\[
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|f_C-f_n|
\le[\beta^{124L}+\beta^{44L}J_\delta]
             Y(m/\gamma)^{3/2}/\sqrt n.
\]
Thus the remaining displayed ambient-d cost is polynomial in storage
and linear in the added error coefficient. For full-span data, use
\(D=d\), omit the projection term, and retain the smaller error
coefficient \(\beta^{124L}\). Exponential intrinsic-rank/depth costs
remain; this is not a polynomial-rank or practical large-dimension theorem.

The fixed query map keeps the projection onto the training span and the
length of its orthogonal component. Training never changes the first
weights in that orthogonal component. The new
[passive-query insertion and moment proof](INTRINSIC_STRICT_ROOT_ROUTE.md)
uses an asymmetric Schatten estimate; fourth carrier moments then give
half-Hölder Gaussian increments. A fixed-moment net argument removes the
old \(\sqrt{\log n}\) loss. The finite-network moment implication and
its downstream use have separate checks:
[insertion](INTRINSIC_STRICT_ROOT_INSERTION_CHECK.md) and
[chaining/restriction](INTRINSIC_STRICT_ROOT_CHAINING_CHECK.md).
The [constant refinement](INTRINSIC_FOLDING_CONSTANT_ROUTE.md) makes
the ambient-d error dependence explicit, with a
[quantitative check](INTRINSIC_FOLDING_CONSTANT_CHECK.md).

The [spherical source proof](SPHERICAL_SOURCE_DIMENSION_ROUTE.md),
[reconstruction](SPHERICAL_SOURCE_DIMENSION_CHECK.md), and
[additional construction check](SPHERICAL_SOURCE_ADDITIONAL_CHECK.md)
remove the superexponential dimension prefactor without folding as well.
An independent, simpler
[angular proof optimization](EUCLIDEAN_ANGLE_DIMENSION_ROUTE.md), with
[check](EUCLIDEAN_ANGLE_DIMENSION_CHECK.md), removes the former coarse
\((d+3)^d\) factor. The combined model, counting, quantitative and
endpoint audit is in
[INPUT_DIMENSION_ASSEMBLY_CHECK.md](INPUT_DIMENSION_ASSEMBLY_CHECK.md).

These are internally checked study results. They compare the same realized
canonical dense network at equal physical times over the entire sphere,
including fitting, with the existing corrected-readout autonomous optimizer.
The only new runtime operation is the fixed projection/norm query map;
all retained arrays and work vectors are counted. Original full training
inputs may be discarded after setup; keeping them adds \(m(d+1)\).
No clipping, population substitution, new label restriction or trained-path
oracle is used. The width threshold, setup work and precision remain
unquantified; architecture, data and confidence are fixed before large
width. No numerical experiment or manuscript/book edit was made.
Contributors: root (angular proof, spherical/assembly reconstruction),
`intrinsic_root_width` (folding and constants), `sphere_source_dimension`
(spherical proof and downstream checks), and `dimension_alternative`
(separate source-class audit and insertion/angle checks). The generic
analytic obstructions in
[DIMENSION_ALTERNATIVE_ROUTE.md](DIMENSION_ALTERNATIVE_ROUTE.md) are not
neural impossibility results or dependencies of these positive theorems.

**Previous architecture dependence (2026-10-04):**
[ARCHITECTURE_CONSTANT_REFINEMENT.md](ARCHITECTURE_CONSTANT_REFINEMENT.md)
supersedes the conservative coefficients immediately below. Let
\(B=\max(1,B_\phi)\) and
\(\beta=\max(10,B,4B/a,32B/a^2,16/a)\), for the common activation
strip bounds. Certified inner-strip derivative bounds may replace the
Cauchy estimates; for tanh, \(\beta=16\) is valid. For fixed
\(L\ge2,d\ge1\), \(\gamma=\lambda_{\min}(Q^{(L)})>0\), and
label RMS \(Y\), the revised complete sufficient bounds are
\[
Y\le(\gamma/m)\beta^{-62L},\qquad
\operatorname{size}(C)\le
\beta^{84Ld}(d+3)^d(m/\gamma)^2\log^{3d+2}(en)+10m(d+1),
\]
\[
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|f_C-f_n|
\le\beta^{124L}Y(m/\gamma)^{3/2}/\sqrt n.
\]
The sharper storage coefficient is
\(\beta^{82Ld}(d+3)^{3d-2}/(d!)^2\). Thus the double-exponential
label loss becomes exponential in depth, the error exponent changes from
\(L^2\) to \(L\), and the dimension-only storage factor falls from
roughly \(d^{3d}\) to \(d^d\). The logarithmic exponent remains
\(3d+2\); the numeric powers are conservative sufficient estimates.

The [rescaled carrier budget](LABEL_DEPTH_RESCALING_ROUTE.md) retains
the fourth activity power in endpoint feedback and uses the correct
\(\log(1/\eta)\) cutoff term. The
[runtime calculation](DEPTH_CONSTANT_SEPARATION.md) separates the actual
fixed mixer norm from the larger source coefficient. The
[source representation](DIMENSION_PREFACTOR_OPTIMIZATION.md) separates
time and angle radii and retains a weighted-degree index set, giving the
factorial saving. Complete independent reconstruction is recorded in
[ARCHITECTURE_OPTIMIZATION_CHECK.md](ARCHITECTURE_OPTIMIZATION_CHECK.md),
with an additional
[label/runtime coupling check](LABEL_RUNTIME_ASSEMBLY_CHECK.md).

The dense reference, whole-sphere norm, physical time and corrected-readout
autonomous optimizer are unchanged. The bound includes the fitted endpoint
and counts all fixed and moving retained real coordinates. Probability
remains at fixed confidence for each sufficiently large width, with fixed
architecture and data; the width threshold and preprocessing/precision
cost remain unquantified. No numerical experiment or manuscript edit was
made. These are internally checked study refinements, not promotion reviews
or a proof that the remaining exponential costs are necessary.

**Explicit architecture coefficients (2026-10-04):**
[EXPLICIT_ARCHITECTURE_CONSTANTS.md](EXPLICIT_ARCHITECTURE_CONSTANTS.md)
gives a conservative fully explicit specialization of the current three
bounds. For common activation strip width \(a\) and bound \(B_\phi\), set
\(B=\max(1,B_\phi)\),
\(\beta=\max(10,B,4B/a,32B/a^2,16/a)\), and
\(A_\phi=\beta^{1024}\). For fixed \(L\ge2,d\ge1\),
\(\gamma=\lambda_{\min}(Q^{(L)})>0\), and label RMS \(Y\), a sufficient
condition and the resulting bounds are
\[
Y\le(\gamma/m)e^{-A_\phi^L},\qquad
\operatorname{size}(C)\le
A_\phi^{Ld}(d+3)^{3d}(m/\gamma)^2\log^{3d+2}(en)
 +A_\phi m(d+1),
\]
\[
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|f_C-f_n|
\le A_\phi^{L^2}Y(m/\gamma)^{3/2}/\sqrt n.
\]
All depth, dimension and geometry dependence in these coefficients is now
displayed. The depth factors, especially the admissible label coefficient,
are conservative rather than sharp; finite layer recurrences in the
component notes give better evaluable constants. This does not enlarge
the previous label range or change the optimizer, source tolerance or
resource contract. High probability remains for each sufficiently large
width with fixed data and confidence; the width threshold is unquantified
and can depend on architecture and data. Both fixed and moving real
coordinates are counted, and exact-real setup remains unbounded.

The component derivations are
[explicit label constants](EXPLICIT_LABEL_CONSTANTS_ROUTE.md),
[source constants and normalization](EXPLICIT_SOURCE_CONSTANTS_ROUTE.md),
and [runtime constants](EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md), with a
[separate reconstruction and assembly check](EXPLICIT_LABEL_SOURCE_CHECK.md).
The assembly corrects one interface normalization: the carrier bound uses
the proved activity allowance \(16Y/\lambda\), not an unsupported lower
comparison with the actual activity integral. The all-time comparison
uses precisely the available bound. These are internal study results,
not promotion reviews or manuscript claims.

**Latest prediction-prefactor refinement (2026-10-04):**
[ERROR_PREFACTOR_REFINEMENT.md](ERROR_PREFACTOR_REFINEMENT.md) removes the
exponential sample/gap dependence from the all-time, whole-sphere error
constant while retaining the current source accuracy, autonomous optimizer,
label condition, and storage count. With
\(Y=\|y\|_2/\sqrt m\), \(\gamma=\lambda_{\min}(Q^{(L)})>0\),
\(\lambda=\min(1,\gamma/m)\), and \(Y\le c\lambda\), the improved bound is
\[
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|f_C(t,x)-f_n(t,x)|
\le \frac{CY}{\lambda^{3/2}\sqrt n}
\le \frac{C}{\sqrt{\lambda n}}.
\]
For tanh, this gives
\(C_{\rm data}\le CY(m/\gamma)^{3/2}\le C\sqrt{m/\gamma}\).
The explicit sample-count dependence is polynomial; poor conditioning
still enters through the displayed gap. Structural constants depend on
fixed dimension, depth and activation bounds. The inherited fixed-data,
fixed-confidence, sufficiently-large-width quantifiers are unchanged.
The stochastic source width threshold is not proved polynomial, but no
new exponential threshold or finer source tolerance is used to remove the
exponential error prefactor.

The proof pairs the residual discrepancy with its least-norm readout lift.
Adding that lift to the raw readout discrepancy cancels their leading
coupling exactly. Keeping the factorized feature-Gram difference then
uses the actual readout path length, instead of a weaker residual-only
bound. The exponent depends only on the bounded ratio \(Y/\lambda\)
and the existing carrier maximum. Complete details are in
[ERROR_PREFACTOR_GEOMETRIC_ROUTE.md](ERROR_PREFACTOR_GEOMETRIC_ROUTE.md),
with a separate
[mathematical reconstruction](ERROR_PREFACTOR_GEOMETRIC_CHECK.md) and
[assembly audit](ERROR_PREFACTOR_ASSEMBLY_CHECK.md). These passed as
internal study checks, including the sharper label-dependent prefactor.
The runtime remains the previously specified corrected-readout optimizer;
no ordinary-gradient-flow or promotion claim is added.

**Latest input/depth refinement (2026-10-04):**
[INPUT_DEPTH_REFINEMENT.md](INPUT_DEPTH_REFINEMENT.md) keeps the user's
chosen label condition \(Y\le c\gamma/m\) and improves total retained size to
\[
C\frac{m^2}{\gamma^2}[\log(en)]^{3d+2}+Cm(d+1)
\]
when the normalized gap cap is inactive, as it is for tanh. Depth has
disappeared from the logarithmic exponent; it remains in structural
constants and the sufficiently-large-width threshold. The earlier power
was \(2[d(L+5)+1]\). For two layers on the circle this changes
\(\log^{30}n\) to \(\log^8n\). The strict \(C_{\rm data}/\sqrt n\)
error remains uniform over the whole sphere and all physical time,
including the fitted endpoint, against the same realized canonical dense
run. All retained fixed and moving coefficients are counted. The same
previously specified autonomous corrected-readout optimizer is used;
its exact-real setup work and precision remain unbounded.

The improvement uses average squared endpoint responses in the trace
estimate, avoiding a coordinate-maximum loss at each layer. A deterministic
carrier-moment interpolation then proves a joint complex radius
\(c/\sqrt{\log(en)}\) at every fixed depth. The complete proof is
[DEPTH_INDEPENDENT_EXPONENT.md](DEPTH_INDEPENDENT_EXPONENT.md), with the
[separate reconstruction](DEPTH_INDEPENDENT_EXPONENT_CHECK.md) and
[runtime assembly check](INPUT_DEPTH_ASSEMBLY_CHECK.md). These are internal
study results, not promotion reviews or manuscript claims. The broader
activation class still requires bounded holomorphy on a fixed strip.

At that stage, input dimension had not been removed from the strict
theorem. A checked
[source-space lower bound](DIMENSION_FREE_REPRESENTATION_ROUTE.md), with
[reconstruction](INPUT_DIMENSION_SOURCE_CHECK.md), shows that the current
whole-feature linear approximation interface needs a dimension-dependent
logarithmic exponent for the allowed activation class. This does not prove
a lower bound for arbitrary autonomous predictors. For tanh, the
[initialized complex poles](ANGULAR_RADIUS_CHECK.md) also show that the
new common angular radius has the correct order for those source coordinates.

The earlier weaker-accuracy dimension reduction was: if the training
span has rank r, fixed radial query preprocessing replaces d in the storage
exponent by \(D=\min(d,r+1)\le m+1\), but the proved uniform error is
\(C_{\rm data}\sqrt{\log(en)/n}\). The
[intrinsic-dimension route](INTRINSIC_INPUT_DIMENSION_ROUTE.md) proves
that corollary and records the then-open mixed-response route. The new
strict result at the top of this README supersedes that accuracy gap:
ordinary passive-carrier moments and half-Hölder increments avoid the
unproved higher-derivative estimate. The fixed radial preprocessing
remains explicit. The source-space obstruction still applies to its
original stronger whole-feature interface, not to this scalar-output
folding. The gap-only label corollary below is historical and is not used
in this continuation.

**Previous sample-count refinement (2026-10-04):**
[SAMPLE_COUNT_REFINEMENT.md](SAMPLE_COUNT_REFINEMENT.md) reduces total
retained state to
\[
C\frac{m^2}{\gamma^2}
[\log(en)]^{2[d(L+5)+1]}+Cm(d+1)
\]
when \(\lambda=\gamma/m\), where
\(\gamma=\lambda_{\min}(Q^{(L)})\) is the unnormalized initialized
feature-Gram gap. Both fixed and moving state, including solve caches,
are counted. There is no remaining \(m^4\) training-source term.
The reference is the same canonical dense run, and the error remains
\(C_{\rm data}/\sqrt n\), uniformly over the whole sphere and all
physical time including fitting. The smaller representation uses a
**different autonomous optimizer**, with an internal residual and an
algebraically corrected readout; ordinary reduced-network gradient flow
is not claimed at this improved count. Exact-real setup work and precision
remain unbounded, and the error prefactor has worse explicit gap dependence
than in the older representation.

The complete source label condition is now \(Y\le c\lambda\).
The separate-sample budget proof removes the former
\(\exp[-C\sqrt{\log(em)}]\) penalty. In addition, fixed-dimensional
analytic initialization implies
\[
m\le C[\log(e+1/\bar\gamma)]^{3(d-1)/2},
\qquad \bar\gamma=\min(1,\gamma).
\]
Consequently
\[
Y\le c\,\bar\gamma
[\log(e+1/\bar\gamma)]^{-3(d-1)/2}
\]
is a sufficient condition with no explicit sample count. This last step
uses the relation between sample count and the gap; it does not enlarge
the numerical \(c\lambda\) threshold for a given dataset. None of these
label bounds is claimed optimal or necessary.

The complete component proofs are
[LABEL_SEPARATE_BUDGETS.md](LABEL_SEPARATE_BUDGETS.md),
[GEOMETRY_GAMMA_ONLY_LABELS.md](GEOMETRY_GAMMA_ONLY_LABELS.md),
[WHOLE_QUERY_RESPONSE_SOURCE.md](WHOLE_QUERY_RESPONSE_SOURCE.md), and
[STORAGE_QUADRATIC_IMPROVEMENT.md](STORAGE_QUADRATIC_IMPROVEMENT.md).
Their separate reconstructions and the assembly are recorded in
[SAMPLE_COUNT_REFINEMENT_CHECK.md](SAMPLE_COUNT_REFINEMENT_CHECK.md).
These remain internal study results, not promoted manuscript claims.
Dataset size, dimension, depth, labels and confidence are fixed before
the sufficiently-large-width limit; the eventual width threshold retains
their dependence.

**General theorem baseline:** [GENERAL_COMPRESSION_RESULT.md](GENERAL_COMPRESSION_RESULT.md)
and the [complete theorem](GENERAL_ANALYTIC_COMPRESSION.md) give an internally
checked positive answer for **fixed finite sample count, arbitrary fixed
hidden depth, general data with the existing initialized Gram gap, and
bounded strip-holomorphic activations**. The original model is the actual
canonical Gaussian dense run with every hidden width $n$. An autonomous
weighted network with its own residuals uses total moving and post-setup
fixed state $C\log^{4[d(L+5)+1]}(en)=o(n)$ and achieves strict
$C/\sqrt n$ prediction error on the whole input sphere, uniformly over
all physical time including the fitted endpoint, with any fixed confidence
for all sufficiently large widths. Labels are fixed and sufficiently small,
with arbitrary signs and ratios. No orthogonality or clipping is required.
For nonconstant activations, distinct sphere points without antipodal pairs
satisfy the Gram condition for any fixed $m$, including $m>d$.

This is an exact-real representation theorem: setup work, temporary memory
and precision can be enormous and are not bounded. The activation assumption
is stronger than merely $C^3$; efficient preprocessing and neuron reduction
of the unchanged order-$q$ equations remain open. The earlier
[two-input theorem](TWO_INPUT_COMPRESSION_RESULT.md) retains its sharper
$\log^{16}n$ circle count and width-independent two-layer feature-motion
bound. The new general theorem has an exact nonzero every-layer motion
certificate in its linearly independent-data subcase, without a general
width-independent motion lower bound. Earlier open-status statements below
record their historical stages and are superseded in this analytic dense
scope; the ordinary-Gaussian sampling obstruction never applied to the
coordinated sampler used here.

**Earlier dataset-dependence bounds (2026-10-04; sharpened above):**
[DATASET_DEPENDENCE.md](DATASET_DEPENDENCE.md) tracks the sample count
and the normalized initial feature-Gram gap
$\lambda=\min\{1,\lambda_{\min}(Q^{(L)}/m)\}$. A conservative
sufficient condition for the complete analytic source and compression
argument is $Y\le c\lambda/\sqrt m$, using the new real energy
estimate in the source proof. The subsequent
[Gaussian-maximum refinement](DATASET_MAXIMUM_REFINEMENT.md), checked in
[DATASET_MAXIMUM_CHECK.md](DATASET_MAXIMUM_CHECK.md), improves the label
condition to $Y\le c\lambda\exp[-C\sqrt{\log(em)}]$. The extra
$m^{-1/2}$ penalty was therefore not sharp: it came from bounding a
maximum's exponential moment by a sum of $m$ moments. The sharp gap,
sample-count and label-direction dependence remains open.
The [normalization assessment](DATASET_NORMALIZATION_ASSESSMENT.md)
explains why the correct mean-loss factor $1/m$ is not a proved necessary
label restriction. It also retains the sharper two-term storage bound:
writing $\gamma=\lambda_{\min}(Q^{(L)})$, $a=d(L+5)+1$ and
$b=L+6$, it is
$C\gamma^{-4}[m^4\log^{4a}(en)+m^8\log^{4b}(en)]+O(md+m)$
when the cap is inactive. The first term dominates once
$\log^{(d-1)(L+5)}(en)\ge m$. No necessity of either sample-count
power or improved general label threshold is claimed.
The retained-state bound is
$C(1+m)^4\lambda^{-4}\log^{4[d(L+5)+1]}(en)+O(md+m)$, and the
all-time prediction constant can be bounded by
$C\exp(CY/\lambda^2)$. Structural constants depend only on dimension,
depth and the activation strip bounds. The sufficiently-large-width
threshold still depends on the fixed dataset parameters, positive label
RMS and confidence; no growing-$m$ result is asserted. The
[source-constant audit](DATASET_SOURCE_CONSTANTS.md),
[real energy fitting proof](DATASET_LABEL_DEPENDENCE.md), and
[two-nearby-input example](DATASET_GEOMETRY_EXAMPLE.md) separate the
full compression condition, the stronger real-fitting-only condition,
and the effect of label direction. These powers are sufficient, not
optimality or impossibility statements. The
[complete quantitative reconstruction](DATASET_DEPENDENCE_CHECK.md)
checks the final synthesis and its source interfaces; these are internal
collaborative checks, not promotion reviews. The separate real fitting
certificate also has a [complete check](DATASET_LABEL_CHECK.md).

## Contract

Start with two tanh hidden layers, canonical Gaussian initialization, zero readout, fixed finite compatible sphere data with a positive initial feature-Gram gap, and fixed sufficiently small labels. The reference is the actual residual-RMS order-q closure in paper/main.tex, including its own coupled forward/backward memories and unchanged initialized mixer.

Seek an autonomous, restartable smaller moving-state representation with high-probability error at most n^{-1/2+o(1)} in the manuscript's query-integrated full-time supremum norm, including the fitted limit. The user has clarified that the saving must come from fewer neurons, through structured or more accurate population sampling. Reducing memory order alone does not satisfy this objective. The strongest requested target is sublinear-in-n total learned state at matched root-width error, by combining neuron reduction with the separately proved memory-order reduction. Count fixed initialization storage separately. All approximation bias must be bounded against the original realized closure. Replacing it by an independent population, a fixed kernel, or a prescribed trajectory is not a resolution.

The user suggests low-discrepancy or other more accurate sampling. Neuron quadrature and structured temporal-history approximation are separate proposed routes. No numerical training is planned; earlier GPU restriction remains in effect.

## Inputs and coordination

Allowed current inputs: repository instructions, required skills, maintained docs/ and code/ if needed, and user-authorized complete current manuscript and included proof files. The manuscript and book hashes remain unchanged from the preceding complete reads. The user explicitly answered "Yes, use the relevant prior proofs" to importing the prior compression theorem and its proof/check files from studies/dense_cutoff_population_rate_20261001. That specific study is therefore an authorized dependency source; unrelated studies remain excluded.

The coordinator read Q_ORDER_RESULT.md, the complete Q_ORDER_POSITIVE_ROUTE.md, its complete local and probability checks, NONORTHOGONAL_DIRECT_ROUTE.md and its check, the complete FINITE_MIXED_MOMENT_ROUTE.md and its check, and the complete quotient/Gram arguments in Sections 1–2 of DATA_QUOTIENT_CLOCK.md and DATA_QUOTIENT_CHECK.md. The new result needs the prior finite dense-carrier maximum, not a dense-to-population rate. The manuscript's complete projection/fitting and tracking arguments were reread. Unchanged complete manuscript/book startup reads remain current.

HEAD is 4dfa5c1ef2c5b920eda2bbc84316b189b97da92e. The Git index was empty. Existing changes to paper/main.pdf and studies/structured_full_rank_scalar_20260926/README.md are preserved.

The coordinator owns this README and the synthesis. Scoped agents will own separate route notes. Internal reconstructions are not promotion reviews. No manuscript, maintained code, Git index or remote changes are authorized by this work.

## Initial proof routes

| Route | Concrete question | Status |
|---|---|---|
| Neuron sampling | Can structured sampling control the actual coupled random mixer and population-selection bias? | Exact restricted forward/adjoint and query-coefficient calculations checked; no universal impossibility claim or neuron-sampling theorem |
| Temporal approximation | Can the stored one-dimensional response histories be represented with higher-order accuracy and fewer vectors? | Complete weighted second-order forward projection bound for the unchanged closure; mathematical reconstruction passed |
| Direct closure reduction | Can a smaller autonomous reconstruction approximate the original finite-q closure without a population comparison? | Same-initialization dense comparison closes order n^(1/6+o(1)), direct original-closure error C_mu/sqrt(n), all physical time and endpoint |

## Current result and evidence

The [result](RESULT.md) is a strict root-width, all-time comparison to the actual original closure with a moving-state count n^(7/6+o(1)). Run the same width-n closure with p=min(q,p_n), where p_n=ceil(n^(1/6) exp(a sqrt(log(e+n)))) and a is sufficiently large and fixed. On common initialization events of probability tending to one, the full query-integrated time-supremum error is at most C_mu/sqrt(n), simultaneously over original orders q. The construction retains all neurons, the exact fixed mixer and transpose, the original residual clock, and each model's own coupled memories. The target includes deterministic truncation bias; no population comparison is used.

This proves a power saving below n^(5/4) for the user's original near-quarter-order reference: every fixed exponent saving smaller than 1/12 is available. The scope remains two tanh hidden layers, fixed compatible sphere data, small fixed labels, zero readout and canonical Gaussian initialization. The fixed n-by-n mixer storage and matrix-vector cost remain. No arbitrary-depth extension, optimality, practical numerical threshold, or low-discrepancy neuron-sampling theorem is claimed.

The temporal author and coordinator independently derived the weighted second-order forward-history mechanism, then exchanged their concrete calculations. Zero initial readout removes a derivative jump at the unit-prefix join. The closure carrier maximum is bounded by the previously proved dense maximum plus sqrt(n) times the unknown normalized tracking discrepancy. The resulting feedback term is absorbed at the new order. The ordinary backward bound supplies the other history factor, producing a third rather than second power of inverse order.

| Artifact | Contents | Validation |
|---|---|---|
| [RESULT.md](RESULT.md) | Self-contained theorem, construction, state count, error accounting and scope | Coordinator synthesis of the checked proof |
| [HISTORY_APPROXIMATION_ROUTE.md](HISTORY_APPROXIMATION_ROUTE.md) | Complete weighted-history and absorption proof, direct original-order comparison | Complete reconstruction in [HISTORY_APPROXIMATION_CHECK.md](HISTORY_APPROXIMATION_CHECK.md) and [COORDINATOR_CHECK.md](COORDINATOR_CHECK.md) |
| [NEURON_SAMPLING_ROUTE.md](NEURON_SAMPLING_ROUTE.md) | Exact Gaussian sampling obstructions and a conditional stratification estimate | Complete coordinator reconstruction in COORDINATOR_CHECK; the adaptive sampling construction remains open |

Both mathematical reconstructions passed the original frozen history proof and then reread the complete notation-corrected version, SHA-256 46fc0584660bc45bda7cfeb6e4b6a63151559f79c96005ad3794799048d2477f. The correction makes finite normalization factors explicit and removes the activation-derivative alias; it changes no mathematics. Check reports retain both versions. The proof file preserves its candidate-stage header as the frozen submission; the completed reports and RESULT give its current internally checked status. These are collaborative internal checks, not isolated promotion reviews. The user-authorized prior theorem is likewise an internal research dependency, not silently promoted manuscript material.

Write assignments: sampling_neurons owns NEURON_SAMPLING_ROUTE.md; sampling_history owns HISTORY_APPROXIMATION_ROUTE.md; the coordinator owns this README and the synthesis/check record. A third-agent launch was unavailable because of the active thread limit; no extra route or output was created by that failed request.

After freezing its initial independent route, sampling_neurons reconstructed the complete history proof and the full relevant prior finite-carrier dependency chain, writing HISTORY_APPROXIMATION_CHECK.md. The coordinator separately reconstructed the full new proof, read and checked the prior chain, and checked the neuron-sampling calculations. No experiments or external theorem were used. Validation consists of complete mathematical reconstruction, frozen source hashes, normalization checks and local artifact checks. No manuscript, maintained code, prior-study source, Git index, commit or remote was changed.

The memory-order target is resolved in the two-tanh scope by the existing closure family. The user's clarified neuron-reduction target remains open; the previous claim that the requested target was resolved was too broad. The n^(7/6+o(1)) theorem is unchanged and is now a baseline to combine with a separate neuron-sampling theorem. This clarification continues the original neuron-sampling route in this study.

## Neuron-reduction continuation

The active contract is an original realized width-n closure versus an autonomous N-neuron weighted or otherwise structured representation. Its initialization may use the original Gaussian arrays, the dataset and the query law; it may not use a trained reference trajectory. Both forward and reverse use of the same mixer, coupled forward/backward memory, the sampler's own residual and clock, sampling bias, and the full physical-time supremum must be controlled. Constants must be explicit about N, n, q and any sampling parameter. No experiment was run.

The [initial neuron-reduction synthesis](NEURON_REDUCTION_RESULT.md) records a proved initialization-only construction and the still-open trained comparison. The [latest continuation](NEURON_GLOBAL_RESULT.md) adds a fitted-function lower bound for canonical smaller-width initialization laws and an exact finite-response cubature construction; its scope and remaining gap are recorded below. For fixed d,m and confidence, the earlier construction selects both initialized neuron populations down to O((log n)^(3d)) weighted original indices. It preserves the initial training kernel exactly and the full sphere-query kernel to C/sqrt(n), using a bounded projected mixer and its exact weighted adjoint. The initial training velocity is therefore exact and the initial query velocity root-width accurate. Its coefficients use only initialization. After setup its evaluation and defined weighted dynamics use only retained neurons. No trained trajectory or population bias has been substituted into the proof.

This does not establish accuracy after learning begins. Exact Gaussian calculations show new response directions appearing already in the second derivative; they are restricted source obstructions, not prediction lower bounds. A second, block-based weighted algorithm has a fully derived all-time source certificate, with the unbounded sampling source left explicit. Observable first-order cancellation does not eliminate the corresponding retained backward response. The original q=n^(1/6+o(1)) theorem has not been silently transferred to either modified model.

| New artifact | Result and check status |
|---|---|
| [NEURON_REDUCTION_RESULT.md](NEURON_REDUCTION_RESULT.md) | Current clarified target, initialization-only joint sampler, proof mechanism and exact global gap |
| [JOINT_SOURCE_SAMPLING.md](JOINT_SOURCE_SAMPLING.md) | Gaussian source identities, infinite exact query rank, top and joint empirical cubature, weighted candidate; complete internal check passed |
| [NEURON_CUBATURE_CONSTRUCTION.md](NEURON_CUBATURE_CONSTRUCTION.md) | Exact block-weighted q closure, fitting scope, all-time conditional source certificate, query cancellation and backward obstruction; complete internal reconstruction passed for that scope |
| [EMPIRICAL_PATH_QUADRATURE.md](EMPIRICAL_PATH_QUADRATURE.md) | Exact full-time sampling bound on the unchanged finite reference path and resource arithmetic |
| [EMPIRICAL_PATH_QUADRATURE_CHECK.md](EMPIRICAL_PATH_QUADRATURE_CHECK.md) | Complete PASS after exponent-boundary wording repair; also proves actual-reference C_mu Y/sqrt(N) MC bound, uniform constants for each chosen q |
| [NEURON_REDUCTION_CHECK.md](NEURON_REDUCTION_CHECK.md) | Coordinator's complete reconstruction of the new source and construction files, with hashes and limitations |

Write assignments: `neuron_joint_sources` authored JOINT_SOURCE_SAMPLING.md and checked the coordinator's joint-population strengthening; `sampling_history` authored NEURON_CUBATURE_CONSTRUCTION.md and EMPIRICAL_PATH_QUADRATURE_CHECK.md; the coordinator authored the path lemma, synthesis and overall reconstruction. These are collaborative internal checks, not isolated promotion reviews. A failed third-agent launch/follow-up produced no additional research output.

Final checked source hashes: JOINT_SOURCE_SAMPLING.md `6e8c856fb9c79e106cf3e75580019cdb0d07b0873ef745ea7700b82d23a65f87`; NEURON_CUBATURE_CONSTRUCTION.md `d02322be2e58dd8462323c7dfbe85c51451eb4186ff030274a4cd28b47bb81cf`; EMPIRICAL_PATH_QUADRATURE.md `9b92ba8cf4405d805a77661877118f13cdfe492d804d9f76b2747bb3ea1a80b9`. The sampler now has a concrete non-oracle initial construction; its full training fidelity remains the substantive unresolved question. The next research target is control of response-aware empirical cubature through the actual coupled evolution. No experiment, promotion, paper edit, prior-study edit, or Git write occurred.

## Continuation: fitted-function obstruction and response-aware selection

The user's next request retained this scope and asked for either a genuine all-time neuron reduction or an incompressibility construction. The [new synthesis](NEURON_GLOBAL_RESULT.md) records two checked results and their exact limits. **The general optimized-sampling question is still open.** The negative result below must not be presented as an impossibility theorem for the weighted sampler the user proposed.

- **Fitted-function lower bound for canonical smaller laws.** Train on one sphere input with one sufficiently small fixed nonzero label. For any coupling of canonical width-N and width-n initializations, any deterministic positive memory orders, and N=o(n), the two actual fitted query functions differ by at least c_y/sqrt(N) with fixed positive probability. Both networks interpolate on that event. This holds on one orthogonal query and in L2 for any fixed query law on the orthogonal sphere, including a continuous circle in dimension three. It also holds at a fixed positive physical time and therefore contradicts the full-time root-n target for this class. It covers ordinary variance-preserving neuron subsampling, but excludes noncanonical source-dependent cubature. The complete nonlinear endpoint remainder is O(y^3/sqrt(N)); it is not a discarded width-independent bias.
- **Exact finite initial-response sampler.** For every fixed original initialization, q, and p, positive cubature selects O(p^2) neurons in each layer that exactly match prediction and retained-state derivatives through order p. It preserves both directions of its fixed projected mixer, the coupled memories, and physical clock, with moving count O(p^2 q) at fixed data dimension and sample count. Any fixed finite set of query probes can be included. Setup differentiates the original initialized equations; it does not query a trained path. There is no uniform global remainder bound that converts this into the requested all-time approximation. Fitting itself requires the explicitly stated original Gram-gap, initialized-bound and small-label hypotheses.
- **Bounded temporal-source follow-up.** The checked second-order history estimate gives actual coefficient amplitudes in l^p for every p>2/5 and spatial singular-value decay, with the history-bound constant retained. It does not make the endogenous history coefficients independent Gaussian innovations. An exact early-response calculation exhibits the necessary reverse-mixer conditioning. This distinguishes a proved temporal regularity estimate from the missing source-sensitivity argument.

| Artifact | Contents and check status |
|---|---|
| [NEURON_GLOBAL_RESULT.md](NEURON_GLOBAL_RESULT.md) | Current conclusion, theorem intuition, sampler, and unresolved broad target |
| [NEURON_GLOBAL_NEGATIVE.md](NEURON_GLOBAL_NEGATIVE.md) | Full canonical-marginal fixed-time and endpoint lower bounds, including orthogonal-continuum query laws |
| [NEURON_GLOBAL_NEGATIVE_CHECK.md](NEURON_GLOBAL_NEGATIVE_CHECK.md) | Complete internal PASS for the fixed-time and endpoint point-query source before its continuum extension |
| [NEURON_GLOBAL_POSITIVE.md](NEURON_GLOBAL_POSITIVE.md) | Exact initial-derivative cubature, global approximation obstruction, and bounded temporal-source calculation |
| [NEURON_GLOBAL_POSITIVE_CHECK.md](NEURON_GLOBAL_POSITIVE_CHECK.md) | Complete finite-jet reconstruction; fitting wording corrected and latest version checked |
| [NEURON_GLOBAL_COORDINATOR_CHECK.md](NEURON_GLOBAL_COORDINATOR_CHECK.md) | Coordinator reconstruction of both routes, continuum extension, source hashes, and scope audit |

The independent route attempts began fresh with explicitly scoped inputs. The negative author derived the fixed-time bound; the coordinator proposed the endpoint expansion, independently checked the full argument, and proposed the continuum extension; the author completed both proofs. The positive author developed the response cubature and bounded history follow-up. After their route candidates were frozen, the two authors cross-checked each other's complete notes. The coordinator read both full notes and full checks. These are collaborative internal reconstructions, not promotion reviews. The positive proof's fitting sentence was corrected to distinguish its hypotheses from the unconditional finite-jet identity; no algebraic defect remains within either stated result.

Final checked route hashes: NEURON_GLOBAL_NEGATIVE.md `ddfca55aaaddd6bb80d74d0664038539ed8d7d1ee5ea52240eeee3d97de47e1c`; NEURON_GLOBAL_POSITIVE.md `00aefc9cbccee65a8d4ddaa603709395d1eace1a2e91d54aa4da7c85389e8819`. The complete proof and check notes supply the mathematical reproduction; no numerical experiment was run. The initialized projection/fitting part of the unchanged manuscript was reread for the endpoint dependency. The positive author also inspected the user-authorized prior study's FINITE_TAIL_ROUTE.md, CONTROLLED_FEEDBACK_STABILITY.md and GENERAL_DATA_STABILITY_ROUTE.md diagnostically; no unproved or additional hypotheses from them enter the finite-jet theorem. No unrelated studies were used.

Current write ownership: `neuron_global_negative` owns the negative route and positive check; `neuron_global_positive` owns the positive route and negative check; the coordinator owns this README, current synthesis and coordinator check. No paper, maintained code, prior-study source, Git index, commit, remote or existing concurrent work was changed. The remaining authorized research is a full-trajectory construction or prediction lower bound for source-dependent weighted neuron selection; the canonical-marginal obstruction does not close that question.

## Continuation: coordinated compression succeeds for one canonical input

The user rejected ordinary-Gaussian sampling lower bounds as an answer to
the coordinated-sampling question and explicitly permitted a direct dense
construction for one nontrivial configuration. In the subsequent scope
clarification, the user emphasized the actual realized width-$n$ reference
and constants independent of width and time. The new main result retains
two hidden layers of original width $n$, ordinary independent Gaussian
initialization, zero readout, and the manuscript's exact dense gradient
mobilities. It does not use the fixed-second-width benchmark as a substitute.

For the one training input $\sqrt2e_1$ and every sufficiently small fixed
positive label, initialization-only positive empirical cubature selects
$n^{o(1)}$ weighted neurons in each layer. Its total moving state, including
the entire small learned hidden matrix, is at most
$C\exp(C\sqrt{\log(en/\eta)})[\log(en/\eta)]^{10}$.
At any fixed failure probability $\eta$, this is $n^{o(1)}=o(n)$.
With probability at least $1-\eta$, the error against the **same realized
canonical dense network** is $C/\sqrt n$ uniformly over the whole input
circle and every physical training time, including both fitted endpoints.
All sampling and projected-mixer errors are bounded. There is no population
bias term, clipping modification, trained-path input, or assumed source
regularity. Post-setup fixed storage has the same sublinear order. Setup
work and numerical bit complexity are not controlled.

The exact coordinate change $u=a/2+\sinh(2a)/4$ removes the first-layer
carrier from the activity stability constant. This permits a complete
finite Gaussian complex-strip proof using autonomous singleton cavities
in both mixer directions. Conformal continuation of initial derivatives
and finite angular trigonometric interpolation produce a sufficiently small
response space. Positive cubature matches its pairings, preserving forward
and reverse consistency. Weighted stability closes the smaller model's
own dynamics; contraction of the two distinct scalar physical clocks gives
the same-time bound. Both hidden training-feature displacements are at least
$cy^2$ at fitting for fixed $y>0$, uniformly in width. The result retains
nonlinear feature movement and proves approximation of the full query
function; it does not assert beneficial classification under an unspecified
test-label rule.

| Artifact | Contribution and check |
|---|---|
| [CANONICAL_COMPRESSION_RESULT.md](CANONICAL_COMPRESSION_RESULT.md) | Readable theorem, construction, intuition, resource accounting and scope |
| [CANONICAL_NEURON_COMPRESSION.md](CANONICAL_NEURON_COMPRESSION.md) | Full direct canonical dense-to-small-weighted-dense proof; complete reconstruction in [CANONICAL_NEURON_COMPRESSION_CHECK.md](CANONICAL_NEURON_COMPRESSION_CHECK.md) |
| [COMPLEX_ACTIVITY_ROUTE.md](COMPLEX_ACTIVITY_ROUTE.md) | Actual finite Gaussian activity and query holomorphy, including both mixer directions; full check in [COMPLEX_ACTIVITY_CHECK.md](COMPLEX_ACTIVITY_CHECK.md) |
| [CANONICAL_SCALAR_AUTONOMY_ROUTE.md](CANONICAL_SCALAR_AUTONOMY_ROUTE.md) | Explicit initial-derivative analytic continuation and same-physical-time clock contraction; historical open-route portion superseded by its dated note |
| [WEIGHTED_ACTIVITY_STABILITY.md](WEIGHTED_ACTIVITY_STABILITY.md) | Complete deterministic forward/reverse source-to-trajectory lemma, without minimum-weight or maximum-carrier constants |
| [CANONICAL_FEATURE_LEARNING.md](CANONICAL_FEATURE_LEARNING.md) | Width-independent motion of both hidden feature vectors; full dense check and transfer implication in [CANONICAL_FEATURE_LEARNING_CHECK.md](CANONICAL_FEATURE_LEARNING_CHECK.md) |
| [CANONICAL_COMPRESSION_COORDINATOR_CHECK.md](CANONICAL_COMPRESSION_COORDINATOR_CHECK.md) | Full-chain reconciliation, normalization, hashes, information/state accounting and scope audit |
| [TWO_INPUT_EXTENSION_ASSESSMENT.md](TWO_INPUT_EXTENSION_ASSESSMENT.md) | Exact two-input equations and noncommutation; bounded extension attempt, with the actual canonical two-input theorem left open |

The one-input positive result is internally checked, not promoted. The
coordinator read every source and complete check in this chain.
`compact_complex_activity` authored the complex proof and checked the
coordinator's feature-motion proof. `compact_canonical_one_input` authored
the conformal/clock route and reconstructed the complete complex and
compression proofs, including the finite-interpolation revision.
`compact_bottleneck_geometry` supplied the separate weighted stability
lemma, fully reconstructed by the coordinator. Initial creative routes
started fresh with explicitly scoped inputs; subsequent exchanged checks
are collaborative internal checks, not promotion reviews.

Final main source hash:
`1a3ec599335af598ac834ce1f3892817d671cce7b42331808b6e84fd531b3a61`.
Complete complex source hash:
`3190cbcef13c3089b2a475c297e9333e98ce3c01f69a686bde217cf87f193fe4`.
The source-hash records and full reconstructions supply the mathematical
reproduction. No numerical experiment was run. The root owns the synthesis,
main theorem, feature certificate, coordinator check and README; the scoped
agents own their named route/check files.

The bounded two-input attempt preserves the useful coordinate change for
orthogonal inputs, but proves that their activity vector fields do not
commute even at canonical initialization. For nonorthogonal noncollinear
inputs the first-layer gate directions also fail to admit simultaneous
constant-coordinate straightening. These exclude simple extensions of the
present proof; they are not neuron-compression lower bounds. The remaining
canonical two-input obligation is a full fitting-interval comparison of
the differing residual-direction histories with independent cavity sources.

A separate [structured benchmark](BOTTLENECK_POPULATION_ROUTE.md), checked
in [BOTTLENECK_POPULATION_CHECK.md](BOTTLENECK_POPULATION_CHECK.md), proves
$O((\log n)^4)$ moving state for two correlated inputs and two learning
tanh layers with compact particle initialization. Its exact equal-width
lift has cloned upper rows and a rank-two initial matrix. This explicit
initialization restriction is material. It is retained as a useful separate
positive example, and is not used to prove the canonical theorem above.

This completes the user's requested positive existence result for at least
one canonical deep feature-learning configuration. It does not resolve
general finite datasets, a polylogarithmic canonical bound, arbitrary depth,
large labels, practical setup, or the unchanged order-$q$ closure's neuron
compression. Those are further research questions. No manuscript, maintained
code, other study source, Git index, commit, push, or concurrent work was changed.

## Continuation: two inputs, all small label signs, and polylogarithmic state

The current user request asks for at least two inputs, arbitrary fixed
sufficiently small labels, both same-sign and opposite-sign cases, and
sublinear autonomous state at full-time $C/\sqrt n$ functional error.
The direct dense route remains authorized. The completed result uses
$x_1=\sqrt2e_1,x_2=\sqrt2e_2$, with no restriction on the signs or ratio
of the two labels. Orthogonality is a material geometry restriction; no
claim for every pair of input positions is made.

[TWO_INPUT_COMPRESSION_RESULT.md](TWO_INPUT_COMPRESSION_RESULT.md)
states the theorem and qualifications. For each fixed label vector with
$\|y\|_2\le Y_*$ and confidence $1-\eta$, an initialization-only
construction selects $O(\log^8(en/\eta))$ positively weighted neurons in
each layer. Counting the entire small learned hidden matrix gives
$O(\log^{16}(en/\eta))$ moving and fixed real coordinates after setup.
The exact canonical reference retains its two original width-$n$ tanh
layers, Gaussian read-in and mixer, zero readout, and manuscript gradient
mobilities $(n,1,n)$. With probability at least $1-\eta$, the error is
$C/\sqrt n$ at every circle query and every physical time, including both
fitted limits. The constant is independent of width and time. The width
threshold may depend on fixed labels and confidence. The compressed
initialization is task-dependent; no single sampler for all labels is claimed.

The central new estimate compares the two models' signed integrated
residual differences. The initial feature Gram gap supplies a stable
linear part, and bounded total residual activity absorbs the nonlinear
feedback. The two training vector fields need not commute. This proves
actual all-time comparisons with autonomous neuron-deleted networks and
with the selected model, including its own residuals. It supersedes the
open feedback-history obligation in `TWO_INPUT_EXTENSION_ASSESSMENT.md`.

Those independent neuron-deleted networks support the finite Gaussian
complex physical-time estimates for both mixer directions. The proved
time/angle neighborhood has width $c/\sqrt{\log n}$ through time
$C\log n$. An explicit finite initial-derivative continuation constructs
a small polynomial response space. Its temporary derivative order may
be enormous, but only $O(\log^4 n)$ coefficient vectors are retained for
cubature. This distinction improves the previous one-input storage
argument to a polylogarithmic count here. No trained snapshots, full-width
runtime arrays, external residual control, population approximation or
clipped algorithm enter the constructed model.

The separate feature theorem gives fixed $t_*,c,C>0$ and a label-independent
initialization event of probability tending to one such that both original
hidden training-feature tuple displacements at $t_*$ lie between
$c\|y\|_2^2$ and $C\|y\|_2^2$, simultaneously over nonzero small label
directions. The same lower bounds transfer to the weighted model for each
fixed nonzero label vector at sufficiently large width. This proves
nonvanishing feature motion as width grows, with no endpoint displacement
lower bound or test-label generalization claim.

| Artifact | Contribution and status |
|---|---|
| [TWO_INPUT_COMPRESSION_RESULT.md](TWO_INPUT_COMPRESSION_RESULT.md) | Readable complete theorem, smaller model, mechanism, and resource limits |
| [TWO_INPUT_CANONICAL_COMPRESSION.md](TWO_INPUT_CANONICAL_COMPRESSION.md) | Complete positive cubature, paired-mixer defects, own dynamics, state count, same-time and endpoint theorem |
| [TWO_INPUT_STABLE_GEOMETRY.md](TWO_INPUT_STABLE_GEOMETRY.md) | Signed-integral stability, weighted fitting, autonomous cavities, and initial jets to small polynomial spaces |
| [TWO_INPUT_COMPLEX_SOURCE.md](TWO_INPUT_COMPLEX_SOURCE.md) | Actual finite-network complex time/query bounds; both mixer orientations and independently stopped cavity Gaussian estimates |
| [TWO_INPUT_CANONICAL_COMPRESSION_CHECK.md](TWO_INPUT_CANONICAL_COMPRESSION_CHECK.md) | Complete reconstruction of the three-file theorem chain, including revised source hashes |
| [TWO_INPUT_COMPLEX_SOURCE_CHECK.md](TWO_INPUT_COMPLEX_SOURCE_CHECK.md) | Separate full source/approximation reconstruction; final clarifications checked |
| [TWO_INPUT_FEATURE_LEARNING.md](TWO_INPUT_FEATURE_LEARNING.md) | Width-independent feature motion in both layers for all small label directions |
| [TWO_INPUT_FEATURE_LEARNING_CHECK.md](TWO_INPUT_FEATURE_LEARNING_CHECK.md) | Full reconstruction of both lower bounds and their compressed-model transfer |
| [TWO_INPUT_COMPRESSION_COORDINATOR_CHECK.md](TWO_INPUT_COMPRESSION_COORDINATOR_CHECK.md) | Final source hashes, normalization and quantifier reconciliation, proof and information-flow audit |
| [TWO_INPUT_FEEDBACK_STABILITY.md](TWO_INPUT_FEEDBACK_STABILITY.md) | Separately attempted primitive-of-residual proof, then cross-check and rectangular deletion calculations |
| [TWO_INPUT_LABEL_SERIES.md](TWO_INPUT_LABEL_SERIES.md) | Unused independent route: initial label jets span $O(p^3)$ time modes and a local complex-label disk; the desired larger label disk remains unproved and is unnecessary for the completed physical-time route |

The three initial attempts began fresh with explicitly scoped permitted
sources and wrote separate files before exchange. `two_input_stable_geometry`
authored the deterministic stability/approximation route, main construction
and feature note. `two_input_feedback_stability` derived a separate stability
route, then reconstructed the complete three-file theorem and feature note.
`two_input_label_series` derived the independent label-series route, then
reconstructed the complete complex source and approximation argument.
The coordinator authored the complex physical-time source proof, contributed
the second-layer feature-energy proof, reconciled and read the complete
chain, and owns the synthesis, coordinator check and this README. Internal
checks are collaborative research checks, not isolated promotion reviews.

The actual minor corrections were a positive-error range in the general
approximation lemma, two missing TeX backslashes, and explicit retained-data
conditioning in the query Gaussian argument. Final reports retain their
initial source hashes and verify the corrected versions. The current paper,
its included mathematical proofs, book entry and notation contract are
unchanged from their complete prior reads. Their hashes and final research
source hashes are in the coordinator check.

The proof files and full reconstructions provide mathematical reproduction.
No numerical experiment was run. This is an exact-real representation result;
efficient preprocessing, bounded setup workspace and bit complexity are
unresolved. General nonorthogonal pairs, arbitrary finite datasets, larger
labels, other activations/depths and unchanged order-$q$ neuron compression
remain outside the theorem. The requested positive existence case with two
inputs and both label signs is complete within its stated geometry and
resource contract. No manuscript, maintained code, other study, Git index,
commit, push, or concurrent work was changed.

## Continuation: sample count, depth and activation extensions

The user now requests separate extensions in fixed sample count, fixed
depth, and activation class, followed if possible by a joined
polylogarithmic-state theorem. The reference remains the realized canonical
width-$n$ dense network, with initialization-only setup, its own physical
gradient flow, and full-time $C/\sqrt n$ functional error. The smaller
model must remain autonomous with its own residuals; learned and fixed
post-setup coordinates both count. Exact-real setup cost remains outside
the inherited resource contract. No trained-trajectory playback or unknown
response-regularity assumption resolves this target.

The coordinator owns the merged assessment and this README. Fresh scoped
routes own `M_INPUT_COMPRESSION_ROUTE.md` (fixed sample count and sphere
dimension), `DEPTH_COMPRESSION_ROUTE.md` (interior-layer feedback), and
`ACTIVATION_COMPRESSION_ROUTE.md` (a concrete wider activation class).
Each initially sees only the specified completed two-input proofs and
canonical manuscript context. They will freeze separate mathematical
outputs before exchange. The coordinator examines general coupling and
the user-authorized prior finite-depth carrier proofs. Analytic activation
requirements and arbitrary-data geometry will remain explicit rather than
being conflated with the broader $C^3$ closure theorem. The joined theorem
was the initial research target. The completed result and its scope follow.
No experiments were run.

The joint theorem is now internally checked. Its main new source estimate
controls residual-free forward responses and angular derivatives by upward
layer induction: the incoming-row trace at the next layer contains only
lower-layer response maxima. The proof removes independently defined
complex cavity stops using actual finite-network mixed-response estimates,
retains both Gaussian mixer directions and residual adaptation, and gives
an inverse-power-of-logarithm analytic neighborhood. Separately, the
own-residual comparison allows $e^{C\sqrt{\log n}}$ amplification;
slightly more accurate source approximation absorbs it without changing
polylogarithmic dimension. Positive cubature then yields a smaller trained
weighted network with all fixed and moving coordinates counted. This is
strict root-width error, including selection bias and the endpoint.

| Artifact | Result and actual check |
|---|---|
| [GENERAL_COMPRESSION_RESULT.md](GENERAL_COMPRESSION_RESULT.md) | Readable joint result, mechanism and resource/activation qualifications |
| [GENERAL_ANALYTIC_COMPRESSION.md](GENERAL_ANALYTIC_COMPRESSION.md) | Complete statement, initial-jet tensor construction, paired selection, total state count, all-time transfer, data criterion and feature certificate |
| [GENERAL_WEIGHTED_COMPARISON.md](GENERAL_WEIGHTED_COMPARISON.md) | Arbitrary-data/depth deterministic source comparison; actual residual damping and selection bias |
| [GENERAL_WEIGHTED_COMPARISON_CHECK.md](GENERAL_WEIGHTED_COMPARISON_CHECK.md) | Complete reconstruction of that deterministic implication, including corrected final source |
| [DEEP_COMPLEX_SOURCE.md](DEEP_COMPLEX_SOURCE.md) | Actual finite-network complex source theorem through fixed depth; triangular response traces and independent cavity budget |
| [DEEP_ACTIVATION_EXTENSION.md](DEEP_ACTIVATION_EXTENSION.md) | All-layer analytic activation class, full augmented response remainder calculation, exact every-layer feature-motion certificate |
| [DEEP_COMPLEX_SOURCE_CHECK.md](DEEP_COMPLEX_SOURCE_CHECK.md) | Complete reconstruction of both deep source files and all three authorized prior cavity inputs |
| [GENERAL_ANALYTIC_COMPRESSION_CHECK.md](GENERAL_ANALYTIC_COMPRESSION_CHECK.md) | Complete assembly reconstruction; no extra approximation, feedback or endpoint hypothesis |
| [GENERAL_COMPRESSION_COORDINATOR_CHECK.md](GENERAL_COMPRESSION_COORDINATOR_CHECK.md) | Whole-chain reconstruction, source versions, normalization and information/resource audit |
| [ACTIVATION_COMPRESSION_ROUTE.md](ACTIVATION_COMPRESSION_ROUTE.md) | Separately frozen two-layer activation-axis proof, including the sharper two-layer state exponent and RMS feature motion |
| [M_INPUT_COMPRESSION_ROUTE.md](M_INPUT_COMPRESSION_ROUTE.md) | Separately frozen fixed-$m$ orthogonal proof and full sphere tensor approximation; sharper two-layer exponent $6d+4$ |
| [DEPTH_COMPRESSION_ROUTE.md](DEPTH_COMPRESSION_ROUTE.md) | Separately frozen first depth attempt: all-depth fitting/initial jets and the failure of a stronger dimension-free field bound; its later source gap is resolved by the new files above |

The coordinator authored the deterministic bridge, assembled and
reconstructed the joint theorem, read all complete sources and reports,
and owns this README and the synthesis/audit. `sampling_depth` authored
the deep source and activation supplement, then reconstructed the complete
assembly as an implication from the named source theorem.
`sampling_activations` reconstructed the bridge and, separately, the entire
deep source and activation proof; its source check supplies that named
input rather than assuming it. The initial axis proofs were frozen before
exchange; later work and checks are explicitly collaborative internal
research. They are not isolated promotion reviews.

`sampling_m_inputs` authored the fixed-$m$ route, which the coordinator
read and checked completely, and read the complete separately frozen
two-layer activation route for a bounded compatibility assessment. No
separate merged special-case check report was created. These sharper routes are not
dependencies needed to fill the joint theorem's general-data source proof.

The exact manuscript normalization and initial nonproportional-data Gram
criterion are preserved. The runtime trains all selected layers using only
small arrays and positive masses; no source coefficients, initial jets or
original-width mixer survives setup. State constants are independent of
width and physical time, while fixed data, dimension, depth, activation
bounds and Gram margin may enter them. Fixed-confidence sufficiently large
width is distinguished from a simultaneous event over all widths. The
full sphere function is approximated; no claim about unknown test labels
or a population limit follows.

Reproduction is the persisted complete proofs and mathematical
reconstructions. The next unresolved extensions are merely smooth
activations and efficient bounded-precision setup, not the proved analytic
fixed-depth result. No manuscript, maintained code, other study, index,
commit, push, or preexisting concurrent work was changed.

## Completed bounded GPU continuation: practical log-state samplers

Separately from the theoretical extension routes above, the user explicitly
authorized a quick two-GPU numerical test at widths 512, 1024 and 2048,
including nonorthogonal inputs, both label signs and dense-versus-dense
controls. The fixed protocol and completed findings are in
[GPU_SAMPLING_PROTOCOL.md](GPU_SAMPLING_PROTOCOL.md) and
[GPU_SAMPLING_RESULTS.md](GPU_SAMPLING_RESULTS.md).

The 36 paired cases used 90-degree and 60-degree inputs, labels (0.2,0.1)
and (0.2,-0.1), and three seed pairs. There were 72 dense trajectories and
180 distinct smaller trajectories. The main workers completed in about
72 seconds on the two RTX 3090s, using float64 and about 409 MiB peak
allocated GPU memory each. All models numerically fitted. Step-size and
query/time-grid checks passed; the code was checked against the maintained
dense RHS/Heun and independent weighted autograd/restart oracles.

This tested a **practical truncated initialization-only sampler**, not the
theorem's full initial-derivative construction: source rank at most eight,
initial forward derivative order two, reverse order one, and approximate
positive cubature. Its weighted mixer uses consistent forward and reverse
actions and its later dynamics use only its own state and residuals. All
source truncations, positive-mass constraints and setup defects are explicit.

Budgets were fixed before the sweep as S[log(n)/log(512)]^p, for p=1,2
and S=128,256,512. Total model state includes the complete learned small
matrix, read-in, readout, masses and training data. At S=512,p=2, actual
counts were 506,600,756; median paired error/dense-copy ratios were
0.56,1.50,2.75 as width increased. None of the six schedules met the
predeclared competitive criterion in every geometry/sign/width cell.
Errors were largely persistent unseen-input discrepancies at fitting,
despite nonzero motion of both hidden representations.

The empirical result disfavors these particular practical low-order
witnesses at the tested constants. It does not establish an optimal
logarithmic exponent, a lower bound, failure of coordinated sampling in
general, or a refutation of the exact-real theorem. The observed quantity
is a maximum on saved physical times and a finite circle panel, with
numerically settled endpoint diagnostics; no numerical continuum or
infinite-time certificate is claimed.

Sources are [neuron_sampling_setup.py](neuron_sampling_setup.py),
[gpu_sampling_experiment.py](gpu_sampling_experiment.py) and
[analyze_gpu_sampling.py](analyze_gpu_sampling.py). The sampler author is
`gpu_sampler_design`; the numerical coordinator owns the runner, analysis,
protocol and report; `gpu_code_scope_audit` checked equations and independently
recomputed raw metrics and restart outputs in
[GPU_NUMERICAL_CODE_CHECK.md](GPU_NUMERICAL_CODE_CHECK.md). These are internal
implementation/evidence checks, not promotion reviews. Generated data,
source snapshots, provenance, CSV tables and PNG/PDF figure are under
`data/generated/closure_sampling_20261003/gpu_sampling_20261003_*`.
The report supplies commands and exact interpretation. No additional
sampler tuning or training sweep followed the fixed campaign, and no
manuscript, maintained code, other study, Git index or remote was changed.


## Completed GPU continuation: circle-RMS state growth

The user authorized continuing the numerical investigation to identify an
empirically sufficient retained-state growth rule at root-width error.
[GPU_RMS_GROWTH_PROTOCOL.md](GPU_RMS_GROWTH_PROTOCOL.md) freezes the new
calibration/holdout design, fixed error ceiling, rank/node-count separation,
optional branches and 25-minute execution cap before new training.
The primary metric is the circle RMS of the pointwise time supremum;
ordinary maximum-over-time circle RMS and endpoint RMS are also retained.
The previous maximum-error campaign remains unchanged.

The coordinator owns the protocol, configs, selection record, final results
and this README. `growth_runner` owns the new flexible runner;
`rms_growth_design` owns independent old-data RMS reanalysis and the new
analysis script; `sampler_rank_audit` owns the parameter/conditioning and
runner audit. Their permitted scientific inputs are this study's numerical
artifacts and directly used maintained code, without importing other studies.
The new outputs use `data/generated/closure_sampling_20261003/gpu_rms_growth_*`.
The completed empirical result is recorded in
[GPU_RMS_GROWTH_RESULTS.md](GPU_RMS_GROWTH_RESULTS.md). A fixed initialization-only
sampler with response rank 16 and budget
`2550[log(n)/log(512)]^4` passed all 80 held-out cases at widths 512 through
4096, plus four separately seeded cases at 8192. Actual total scalar counts
were 2550, 3782, 5550, 8010, 10920. Every successful p4 trajectory satisfied
`sqrt(n) * RMS_angle(max_saved_time |prediction error|) <= 0.056597`, below
the predeclared 0.15 ceiling, and reached a numerically settled fit. The four
geometry/sign median scaled errors stayed stable as width grew. The two
required step-size and nested query/time-grid checks passed.

This is a sufficient tested rule, not an asymptotic theorem or an optimal
exponent. The smaller p=0,1,2 schedules had preserved numerical setup failures;
in particular, tiny equality-constraint drift and unsuccessful SLSQP status
do not prove that p=1 or p=2 needs more state. A fixed response basis could
eventually produce an approximation floor. The practical count remains above
n at these widths, so this experiment does not yet demonstrate fewer than
n retained scalars, despite large savings against the dense n-squared matrix.
The measured metric uses finite saved times and 257 circle directions, with
numerical endpoint checks rather than a continuum or infinite-time certificate.

[GPU_RMS_GROWTH_SELECTION.md](GPU_RMS_GROWTH_SELECTION.md) freezes the choice
before holdout. [GPU_RMS_GROWTH_DESIGN_CHECK.md](GPU_RMS_GROWTH_DESIGN_CHECK.md)
contains independent raw-data calibration reconstruction;
[GPU_RMS_SAMPLER_AUDIT.md](GPU_RMS_SAMPLER_AUDIT.md) checks equations, storage,
all held-out metrics and both refinements, failed-case recovery, and complete
extrapolation prefixes. The optimizer failures are reconstructed in
[GPU_RMS_SOLVER_DIAGNOSTIC.md](GPU_RMS_SOLVER_DIAGNOSTIC.md). These are internal
implementation/evidence checks, not promotion reviews.

The exact frozen sampler/flow sources were unchanged throughout the campaign.
Failed constructors were retained and disqualified, and remaining original
cases were completed for the unchanged surviving schedules. Two interrupted
8192 stress runs were completed from the same initializations within the
remaining global budget; their saved prefixes match exactly. Total active
parallel execution was 22.17 minutes on two RTX3090s, with peak 6.02 GiB.
All interrupted artifacts remain available. No further training was run.

The runner is [gpu_rms_growth_experiment.py](gpu_rms_growth_experiment.py);
analysis is [analyze_gpu_rms_growth.py](analyze_gpu_rms_growth.py), with final
focused figures from [plot_gpu_rms_growth_summary.py](plot_gpu_rms_growth_summary.py).
The report lists exact configurations and generated analysis roots, whose
provenance records supply full commands, inputs and source snapshots.
No manuscript, maintained code, other study, index, commit or remote changed.

## Completed GPU continuation: multiple samples and sphere queries

The user explicitly requested testing the successful practical budget on
four/eight circle inputs, close same/opposite-label pairs and sphere inputs.
[GPU_MULTIDATA_PROTOCOL.md](GPU_MULTIDATA_PROTOCOL.md) freezes twelve tasks,
widths 512/1024/2048, two new seed clusters, dense-copy controls, the unchanged
rank-16 baseline budget and bounded increased-budget branches. Evaluation uses
circle RMS or full-sphere panel RMS through saved training times and numerical
settlement; all-time/continuum claims remain outside numerical evidence.
The generic total state count is N²+(d+3)N+m(d+1), including fixed masses and
training data. The physical mean-loss factor 2/m is explicitly preserved.

Root owns configs/protocol/results/README; `multidata_runner` owns the new
dimension/sample adapter and runner; `multidata_design` owns analysis;
`multidata_audit` owns implementation/evidence checking. Earlier experiment
code and outputs remain unchanged. New products use
`data/generated/closure_sampling_20261003/gpu_multidata_20261004_*`.
The hard GPU execution-union budget is 25 minutes with at most two workers.

The completed findings are in [GPU_MULTIDATA_RESULTS.md](GPU_MULTIDATA_RESULTS.md).
All 72 baseline dense cases completed, with 70 valid constructed reduced models
and two preserved constructor failures. The old budget passed both 15-degree
two-input label configurations. Eight smooth circle inputs had small recorded
errors, but had not numerically fitted at the T1200 cap. Four/eight harmonic
circle tasks failed the prescribed width-trend check. Full-sphere evaluation
of the same eight-point circle embedded in R^3/R^5 produced substantially larger
errors, with maximum sqrt(n)-scaled discrepancies .33873/.46249 and unfinished
fitting. General-position sphere tasks were more favorable, but no single
unchanged budget/rank rule passed all these configurations. These are finite
width/time/panel observations, not a new exponent or impossibility theorem.

The most informative paired diagnostic holds total retained state fixed:
on the embedded R^3 case at n=2048, seed 9411, twice-budget/rank-16 gave scaled error
.30752, while twice-budget/rank-24 gave .07242; both retain 11259 scalars.
Merely doubling state at rank 16 barely improved the original .3137 error.
At eight samples, the rank-16 priority space was completely occupied by initial
training activations/preactivations, leaving no additional basis directions
for other source responses. Independently reconstructed source projection
defects were small on the circle and large on full-sphere setup directions.
This identifies a limitation of the particular sampled representation and
supports basis enrichment; it does not prove a nonlinear error bound.

Twice-budget/rank-16 passed the smooth four-point confirmation at widths 512
and 2048 on seed 9412, with scaled errors .009776/.007361. The harmonic
four-point confirmation still failed the width trend: raw error stayed near
.002 while width quadrupled. The eight-point harmonic width 2048 confirmation
and one R^5 diagnostic were interrupted at the campaign limit; their partial
records remain archived. No sphere candidate cleared all selection gates.
Two R^5 rank-enriched constructor failures were independently replayed:
positive weights missed the fixed unit-mass tolerance after the optimizer
iteration limit. They are numerical failures, not lower bounds on sampling.
See [GPU_MULTIDATA_SOLVER_DIAGNOSTIC.md](GPU_MULTIDATA_SOLVER_DIAGNOSTIC.md).

[GPU_MULTIDATA_AUDIT.md](GPU_MULTIDATA_AUDIT.md) checks equations, initialization
derivatives, scalar counts, restart autonomy, all 83 complete records and exact
interrupted-prefix reproduction. Both worst-case circle/sphere time-step and
nested-query refinements passed. [GPU_MULTIDATA_DESIGN_CHECK.md](GPU_MULTIDATA_DESIGN_CHECK.md)
records the independent analysis checks. Final tables and PNG/PDF are in
`data/generated/closure_sampling_20261003/gpu_multidata_20261004_final_analysis_checked/`;
separate final audit/budget evidence is in `gpu_multidata_audit_final_20261004/`
within this study's generated namespace. The measured execution-timer union
was 1496.854 seconds, excluding environment startup/source archival, with peak
allocated GPU memory 421450752 bytes. Both RTX3090s were used. All scientific
sampler/flow sources stayed frozen during execution; the final analysis-only
correction repaired pass-status wording without changing any numerical decision.

The direct reduced model still trains a small weighted dense mixer; this
campaign does not test an unchanged q-closure implementation. Total retained
counts remain above n in the tested range. General all-time accuracy, complete
endpoint comparison for unfinished fits, robust higher-rank construction in
R^5 and a common sufficient growth schedule remain open. The bounded campaign
is closed, with no further training or tuning launched. Next useful research,
if requested, is a representation that reserves capacity for off-training
directions and remains numerically robust as sample count grows. No manuscript,
maintained code, other study, Git index or remote was changed.

## Practical-exponent assessment using the refined theorem

The user asked whether the new theorem determines a better practical scaling
rule and optimal powers. [PRACTICAL_EXPONENT_ASSESSMENT.md](PRACTICAL_EXPONENT_ASSESSMENT.md)
separates the theorem's source-space count from the previous practical sampler.
The theorem supplies sufficient total-state powers 8,11,17 for input dimensions
2,3,5, using its corrected-readout optimizer; it does not prove optimality or
supply those powers as numerical minima for ordinary weighted-network training.

Two new deterministic calculations are complete, with no new training. First,
converged two-layer Gaussian covariance quadrature gives label/gap ratios
Y/(gamma/m) between about 20 and 5689 for the earlier tasks. Those labels are
not in the theorem's sufficiently small ratio regime. The eight-point circle
has gamma/m about 1.96537e-5, unchanged by embedding into R^3/R^5. This separates
training conditioning from the added full-sphere query difficulty.

Second, archived source singular values determine the minimum rank for a
specified finite initial-source Frobenius tolerance, with training priorities
retained. At diagnostic tolerance 1/sqrt(n), median second-layer ranks at
n=2048 are 25.5 for the eight-point circle, 56.5 for its R^3 embedding, and 107
for its R^5 embedding. These are source ranks, not neuron lower bounds or
certificates of all-time prediction. Short-range squared-rank proxy powers
are roughly 2--5 across the tested tasks, contingent on neuron count being
proportional to rank. No new practical prediction exponent is established.

[PRACTICAL_EXPONENT_PROTOCOL.md](PRACTICAL_EXPONENT_PROTOCOL.md) records the
bounded analysis contract. Sources are [assess_practical_exponents.py](assess_practical_exponents.py)
and [check_practical_exponents.py](check_practical_exponents.py); generated
quadrature matrices, all 140 rank rows, hashes and checks are under
`data/generated/closure_sampling_20261003/practical_exponent_assessment_20261004/`
and the corresponding `_check/` root. The independent Gaussian parameterization
agreed to 8.33e-16; degenerate correlations and tail-selector tests passed.
Root owns these new artifacts and this update; there was no delegated research
or new scientific training in this assessment. The stronger practical optimum
remains open. The useful next decision is the requested error norm and an
adaptive-rank/selection construction, rather than fitting an exponent to
state budgets that were imposed in advance. Earlier scientific artifacts and
concurrent theorem updates are preserved.
