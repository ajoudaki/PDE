# Internal audit of the broader tanh classification results

2026-10-10. Verdict: the stated partial classification, replication tests,
conditional robustness, and moving escape construction pass the checks below.
The requested complete classification has not been established. This is
author-context internal checking, not an independent isolated promotion review.
No numerical experiment or external scientific theorem was used.

## 1. Source versions and actual coverage

The lead read all three proof contributions, reconstructed their substantive
arguments, read the complete cross-check reports, and checked the integrated
statement against them. The checked current versions are:

| File | SHA256 |
|---|---|
| `TANH_CLASSIFICATION_RESULT.md` | `7cd45778a45e35525e68199787fce4f31f5f6ad65ddac0582d4e7657f4d0ee80` |
| `TANH_REPLICATION_CLASS.md` | `3e0bcb142b985d5e79c8a56f6a66ee91e06fe22b3a41bb1a262c1f8eaf32e14b` |
| `TANH_NECESSARY_GEOMETRY.md` | `770527741d5a9acf76cb9c44e917be8eb9894edff6f02fc03c922f3ecb795b0f` |
| `GLOBAL_FAILURE_ALTERNATIVES.md` | `83efe858430bf60b5686c5790f0d71da0b2e87fe4a2002ea7628673716ba294f` |
| Existing `TANH_BAD_BASIN.md` | `f975c3bd44d9ad97ca22102908e69a181ac1bd4de491781497e9ce65d3d55a53` |
| Existing `TANH_GEOMETRY.md` | `3ac627b10bfe44001724359a0917b201577238a8312df907f79f7031e1e00cd0` |

The existing two notes were read completely in the preceding work in this
same research context; their hashes remain unchanged. They are used only
for the previously established strict seed, zero-readout entrance, and
contrasting geometry, not as evidence of a general classification.

The stationary-geometry and global-dynamics agents began their respective
routes from the self-contained model and bounded assignment, without the
old bad-basin proof. After freezing their results, they cross-checked each
other's work. Their reports are:

- `TANH_NECESSARY_GEOMETRY_CHECK.md`, by the global-dynamics agent: complete
  reconstruction of the frozen necessary-geometry contribution.
- `GLOBAL_ESCAPE_CHECK.md`, by the stationary-geometry agent: complete
  reading of the global contribution, with detailed reconstruction focused
  on global existence, finite-cluster stationarity, and the escape theorem.

These cross-checks are not blind or promotion reviews: both agents had
participated in the current author team before checking. The replication
agent also reused its previous author context, which is disclosed in its
note. The lead supplied the four-sample escape idea; the global agent and
stationary agent each reconstructed it. The lead generalized it to any even
sample count; the global agent independently verified its covariance proof.

The global agent subsequently read the full integrated result and verified
Sections 3--6 and the rank-one algebra in Section 2. It did not certify the
then-unavailable general replication source or the old seed's entrance
dependency. Those parts were reconstructed by the lead from their complete
sources. The stationary agent additionally checked the rank-one Hessian
identity and attraction at unequal nearby weight/readout allocations.

## 2. Corrections found and resolved

The initially written replication contribution contained a dropped plus
sign between the two splitting forms in its equation (9), a stray prose
`+`, and the name "right inverse" for the matrix satisfying
\(U^+U=I_m\). These were corrected before freezing. Its final formula has
the sum of the two splitting forms, and the inverse is correctly described
as a left inverse. The lead read the corrected passages.

The escape cross-check used the earlier global-source hash

```text
37ac6f2ec3316b42dc73f775b20d70467a0a04194338707de102f5cfff851a1f
```

After that check, the lead repaired only two prose occurrences of
`sigma_{\min}` to `\sigma_{\min}`. The theorem, formulas, and proofs were
unchanged. This accounts for the current hash in the table and preserves
the exact provenance of `GLOBAL_ESCAPE_CHECK.md`.

The integrated-result cross-check found one scope wording issue: Section 4
had cited a rank condition stated for local minima while classifying all
second-order stationary points. The corrected sentence explicitly derives
that rank condition from equations (4)--(5) when \(w\ne0\), then uses
full input rank. No new assumption or mathematical repair was needed.

## 3. Replication identity: lead reconstruction

The notation in this section follows `TANH_REPLICATION_CLASS.md`, where
each seed neuron at width \(k\) is repeated \(\ell\) times, the second
weights are divided by \(\ell\), and the new width is \(k\ell\).

First variations split into means and zero-mean differences. For each
second-weight block, its row sums, column sums, and doubly centered
remainder are independently realizable through equation (21). This is
essential: a negative quadratic form in fictitiously independent
coordinates would not prove a genuine network saddle. The prescribed
row and column sums of (21) were checked directly.

For each top copy, the first preactivation variation is the coherent
seed variation plus its row-sum difference paired with the seed lower
features. Averaging over copies cancels the differences. Thus the first
prediction variation and its square are precisely the coherent seed
ones, with no missing splitting Gram term.

The second prediction derivative has exactly three additional types:

1. Readout differences paired with row-sum differences. Their residual
   contraction gives \(2\widehat c\,p_i^\top\widehat b\).
2. Second-activation curvature, giving
   \(w_i\widehat b^\top T_i\widehat b\).
3. First-activation curvature and mixed first/second-weight motion, giving
   \(\widehat a^\top B_j\widehat a\) and
   \(2\sum_i d_{ij\beta}v_{ij}^\top\widehat a\).

The mixed identity

\[
\sum_{\alpha,\beta}
\delta\widetilde W_{i\alpha,j\beta}a_{j\beta}
=\ell\bar B_{ij}\bar a_j
+\sum_\beta d_{ij\beta}\widehat a_{j\beta}
\]

was reconstructed by summing first over top copies and then using the
zero means. It verifies the coefficient and absence of additional terms.
Multiplying the second prediction variation by the exact loss factor
\(2/m\) yields the displayed \(2/(mk\ell)\) in the source equation (22).
The identity does not require criticality; criticality is needed to use
it as a stationary-point stability test.

The necessity of every mixed equality is valid. The readout difference
has no square term, so a nonzero \(p_i\) produces a negative quadratic
direction by choosing its signed coefficient large enough. Likewise the
column-sum difference has no square term, forcing each \(v_{ij}=0\).
The independent realization ensures these tests introduce no unintended
mean direction. Setting those mixed coefficients to zero leaves exactly
the seed Hessian and the two types of splitting curvature. This proves
both directions of the second-order equivalence, including zero seed
readouts and \(\ell=2\).

Specializing to \(k=1\) at a critical seed with \(qs\ne0\) makes the
two mixed moments vanish by the reduced critical equations. The remaining
conditions are exactly the three tests (1) in the integrated result. The
separate restriction \(n\geq2\) is needed for necessity of the splitting
tests; at width one there are no splitting directions.

## 4. Actual critical manifolds, attraction, and robustness

The strict conditions were checked against actual affine critical sets,
not merely against a candidate Hessian kernel. In the rank-one set,
all first rows remain fixed, second-weight row sums remain fixed, and
the mean readout remains fixed. The readout and second-weight gradients
vanish by their respective residual moments. The first-weight gradient
is a scalar weight-allocation factor times the zero vector supplied by
reduced first-weight stationarity. Thus unequal nearby readouts and
unequal column allocations remain exactly critical.

For the general replicated set, the row sum of each prototype block is
fixed, as is the mean readout in each top group. Strict
\(w_iT_i\succ0\) implies \(w_i\ne0\), so \(v_{ij}=0\) forces each
raw first-derivative residual moment to vanish separately. This validates
the first-layer gradient cancellation even when individual copy weights
and readouts differ. The seed Hessian and strict splitting forms make
the kernel exactly tangent to that affine set.

Positive curvature normal to a true local critical manifold gives
quadratic excess loss and a lower bound on gradient norm by its square
root. The energy identity then bounds remaining path length by a
constant times the square root of current excess. An inner-neighborhood
first-exit argument traps the path, and finite remaining length gives
parameter convergence to a point of the manifold. This direct argument
was checked without invoking an unverified global convergence theorem.
All metric eigenvalues are positive at each fixed width; constants may
depend on width.

For rank one, the reduced Hessian is invertible under strictness, so the
implicit-function theorem continues the seed under arbitrary small data
and label perturbations. All strict signs and positive residual norm
persist by continuity. The reduced parameter space, dynamics, and tests
are width independent. A known zero-readout seed trajectory enters a
strongly convex neighborhood at some finite time; finite-time continuous
dependence then gives entrance for perturbed data. Strong convexity and
loss monotonicity give convergence. This proves a width-independent data
neighborhood, but not a width-independent full-parameter basin radius or
Gaussian probability.

For multiple prototypes, continuing a strict seed minimum only preserves
the seed's summed critical equations, not the individual mixed equalities.
The source correctly does not assert automatic data robustness in this
case. It also does not assert existence of a strict multiple-prototype seed.

## 5. Universal geometry and the independent-input classification

The lead's reconstruction agrees with the full companion cross-check.
At a zero pure Hessian direction, positive semidefiniteness forces every
mixed pairing to vanish. Applying this first to an inactive readout's
second-weight row yields \(U(d_i\odot r)=0\) for all top rows. Applying
it to a row perturbation in \(\ker U^\top\) yields the first-layer
derivative annihilation for every redundant lower row and active top row.

Strict positivity of all finite tanh derivative values is used exactly
where multiplication of a nonzero residual must remain nonzero. The
critical-zero interpretation freezes those derivative values and the
residual while varying the ridge parameter; differentiating them as
network-dependent functions would have been a different and incorrect
calculation. Nonredundant feature rows are linearly independent, giving
the count of at least \(n-\operatorname{rank}U\) critical-zero neurons.

The exclusion of zero-readout local minima is higher-order, not a Hessian
test: nearby hidden changes leave their loss fixed, hence yield nearby
local minima and zero readout gradients. Real-analytic continuation and
the elementary distinct-rate tanh separation argument then force the
labels to vanish. The same flat-coordinate reasoning excludes unused
first-layer neurons. The source handles sign collisions and zero feature
columns separately in its inactive-readout statement.

When \(X\) is injective on sample vectors, the derivative condition
rules out an active readout at positive-loss second-order stationarity.
Mixed hidden/readout Hessian blocks then force \(W=0\) and \(Uy=0\).
All Hessian blocks vanish at those remaining points. The explicit
first-layer perturbation realizes feature derivative \(y\), and the
one-entry second-weight/readout perturbation gives cubic loss change
\(-2\|y\|^2t^3/(mn)+O(t^4)\). The factor and sign were checked. Hence
the theorem classifies all second-order stationary points in this data
class and proves that all its local minima fit, without asserting
trajectory avoidance of the remaining saddles.

## 6. Escape extension and global alternatives

The four-sample escape proof and its global-flow dependencies are
reconstructed in `GLOBAL_ESCAPE_CHECK.md`. For the extension in the
integrated result, the lead and global agent separately checked:

- With \(m=2k\), averaging the two signs of each pair gives
  \(\mathcal L=k^{-1}\sum_jr_j^2\) and reduced-flow factor \(2/k\).
- The induced mobility metric is exactly Euclidean in \((p,q,v)\).
- Strict positivity follows from the nonnegative coordinate-face
  velocities and a finite-box Lipschitz comparison; finite-time energy
  bounds supply that box. No global Lipschitz bound is assumed.
- Predictions increase strictly while positive labels decrease weakly.
  Their covariance is nonpositive, so the loss is at least the positive
  variance of the nonconstant pair labels.
- At hypothetical readout stationarity, the residual-to-feature ratio
  has zero mean under weights proportional to \(h_j^2\) and is strictly
  increasing. The ratio \(\partial_qh_j/h_j\) is strictly decreasing.
  Their weighted covariance is strictly negative, giving \(\dot q>0\)
  and excluding a finite interior stationary point.
- Every finite boundary point has zero prediction and initial loss;
  initial strict descent excludes it as an accumulation point. Every
  finite accumulation point is stationary by the local dissipation
  argument, so no finite accumulation point exists. This proves norm
  tends to infinity, not just unboundedness along a subsequence.

The escape result needs no conjecture about which coordinate diverges
or what the exact limiting loss is. It does not show stability under
symmetry-breaking perturbations, an open full-parameter escape basin, or
failure with positive Gaussian probability. The initialization's rank-one
feature condition is explicitly retained.

The fitting criterion (15) in the integrated note retains bounded
parameters, strict initial learning, and recurrent positive first-feature
gap. It is not an initial-data criterion. The tangent-Rayleigh identity
(16) has factor \(4/m\), checked from the loss \(\|r\|^2/m\), and is
retrospective. It is not presented as a solution of the classification
problem.

## 7. Open obligations and disposition

The original unrestricted target is not achieved. Specifically absent are
a necessary-and-sufficient geometric classification of dependent-input
local minima, higher-order flat stability, a full basin description from
the zero-readout slice, and a classification of positive-loss escape.
The new escape class proves that finite local-minimum classification
would not alone settle the last issue.

No statement that all bad minima are duplicated profiles, that all other
initializations fit, that strict saddles are avoided by the zero-readout
Gaussian law, or that bad dynamics are incompressible is supported here.
The integrated compression theorem and maintained book are unchanged.
Theoretical notes and the study README are the only task-owned changes;
there was no experiment, staging, promotion, or Git commit.
