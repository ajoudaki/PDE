# Internal adversarial check of the two-layer persistence note

2026-10-10. Reviewer: `/root/residual_alignment_route`.

Current status after the follow-up check: the three initial findings are
repaired, and the new finite-time support and analytic-rank argument checks
out at source SHA-256
`a8138b6edfd1d62e1c0c235a4c2228605e0c55003366b7741c3d5823f29028a4`.
No unresolved correctness objection remains in Sections 1--6.1. Section 7's
neural-network literature claims remain outside this review's verified
scope. The initial findings below are retained against their original
source hash; the follow-up section at the end supersedes their pending status.

This is an internal proof check in a reused agent context, **not a fresh
isolated review and not a promotion review**. The reviewer previously worked
on a different route in this same study. The initial pass used the complete
assigned note as its only scientific input; prior findings were not used as
proof dependencies. A subsequent authorized pass also inspected the cited
MIT Brouwer theorem and its displayed proof, as recorded below. No
simulations, other studies, maintained scientific sources, or external
neural-network papers were read for this check. The assigned output path is
this report; the source was not edited.

## Source, coverage, and outcome

- Source: `TWO_LAYER_PERSISTENCE.md`, all 503 lines, including all seven
  sections, proof bodies, constants, qualifications, and the literature
  applicability paragraph.
- SHA-256 of the checked source:
  `c9688525520166211d712d952592a3e97d2b8553eb5a8fdc778959fac6c3f530`.
- Read commands: `cat studies/label_scale_obstruction_20261007/TWO_LAYER_PERSISTENCE.md`
  and a complete `nl -ba` reread. Neither read was truncated.
- Hash command: `sha256sum studies/label_scale_obstruction_20261007/TWO_LAYER_PERSISTENCE.md`.
- Required canonical-notation/neural, rigorous-mathematics, and research
  instructions were applied; current `RESEARCH_WORKFLOW.md` was read.
- Before this report was written, HEAD was
  `c17cb8c2e8d486ccc1d2b80e8cd173ba551145ae`, the shared index was empty,
  and unrelated working-tree changes were present and preserved. No Git
  staging or commit was performed.

**Initial-version outcome:** Sections 1--5 withstand the checks below. The numerical constants
in the Gaussian geometry theorem, the typical-invariant-level construction,
and the open attracting basin on the zero-readout/full-rank slice check out.
Section 6 has two local missing hypotheses that should be made explicit.
There is also one harmless coordinate-description error in Section 4.
Section 7's external literature assertions were read but not independently
verified because the assigned scientific input does not include that paper.
Consequently this is not an unconditional full-document PASS.

## Required local corrections

### F1. The Gaussian decomposition needs a width/rank hypothesis

Location: Section 6, original lines 440--459, especially
`Z(U^T U)^{-1}U^T`.

The section assumes `m=d` but does not assume `n>=d`. For `n<d`, the
`n by d` Gaussian matrix `U` has singular `U^T U`, so the displayed inverse
is undefined. The earlier `n>=d+1` assumption belongs to Section 2's theorem;
the contract expressly says such restrictions are local to their proposition.

Minimal repair: state `n>=d` and work on the almost-sure event
`rank(U)=d`; use `n>d` if the argument is meant to exhibit a nonzero unused
Gaussian component. The latter is the natural scope of the stated reserve
example. Alternatively a correctly specified pseudoinverse decomposition
would cover arbitrary rank, but no such extension is needed for the intended
sufficiently-large-width application.

Severity: local domain defect, not a counterexample to the geometry theorem
or the basin proposition. Equation (19) itself remains valid for every width.

### F2. The persistent projection must be orthogonal

Location: Section 6, original lines 466--469.

From `P h_a=0` one cannot infer `h_a^T P=0` for an arbitrary projection.
The update is

\[
\dot W P=-\frac2{mn}\sum_a r_a\delta_a h_a^\top P,
\]

so the asserted constancy requires `h_a^T P=0`. An orthogonal projection
provides this because `P=P^T`.

For a concrete algebraic check, take

\[
P=\begin{pmatrix}1&1\\0&0\end{pmatrix},\qquad
h=\begin{pmatrix}-1\\1\end{pmatrix}.
\]

Then `P^2=P` and `Ph=0`, but `h^T P=(-1,-1)` is nonzero. Thus the
implication as written is false under the general idempotent meaning of
projection. Minimal repair: write "fixed orthogonal projection".

Severity: local missing hypothesis. With that adjective, both the constancy
and the absence of a direct contribution to current preactivations follow.

### F3. The Taylor explanation uses `xi=0` inconsistently

Location: Section 4, original line 302.

The phrase saying that residuals "at `xi=0`" equal `(-a+2e,2a+e)` should
refer instead to `Z_:1=0, Z_:2=pi 1` with `e` free. The defined vector
`xi` includes `e`, so `xi=0` forces `e=0` and the residual is `(-a,2a)`.
The displayed expansion (12) and its Hessian constants are correct; this
is an explanatory wording correction only.

## Reconstruction of the Gaussian geometry theorem

The factors in (1) are consistent with mean squared loss and block
mobilities `(n,1,n)`. In the linear-first-layer case, the displayed matrix
`B` gives

\[
\dot A=W^\top B,\qquad \dot W=BA^\top/n.
\]

Both derivatives of `W^T W` and `AA^T/n` equal
`(AB^T W+W^T BA^T)/n`. Thus the matrix invariant is exact, without a label
or small-motion condition. A fixed negative spectral subspace of dimension
`d` gives a lower singular-value bound for the square matrix `A^T P/sqrt(n)`;
the passage from that bound to `A^T A/n >= I_d/512` is valid. It does not
require the moving column span of `A` to equal the initial negative space.

The Gaussian construction was checked term by term:

1. Conditional orthogonal rotation of the domain of `W(0)` preserves its
   independent variance-`1/n` Gaussian entries. The rotation may depend on
   `A(0)` because `W(0)` is independent of `A(0)`.
2. The Frobenius second moment of each normalized `d by d` Wishart Gram is
   `(d^2+d)/n`. Two Markov bounds at threshold `1/512` give
   `2*512^2=524288` times `(d^2+d)/n`.
3. For `k=n-d` and `M_0=E_0 E_0^T`, the three moments used in the source
   are correct. In particular, the conditional variance contribution of
   `S=B_0^T M_0 B_0` to `E||S-I||_F^2` is
   `(d^2+d) E tr(M_0^2)/n^2`; its conditional-mean contribution is
   `d[2k/n^3+d^2/n^2]`. This reproduces the displayed formula.
4. The loose bound by `4(d^2+d)/n` holds throughout `n>=d+1`.
   Indeed `k(n+k+1)<=2n^2`, `d^3/n^2<=d^2/n`, and
   `2dk/n^3<=2d/n^2`. Applying Markov at `1/2` gives the stated additional
   failure bound `16(d^2+d)/n`.
5. The two `1/4`-nets have total product cardinality at most
   `9^(2n-d)`. The bilinear approximation yields a factor two; exceeding
   operator norm eight therefore requires a net pairing exceeding four.
   Its Gaussian tail is at most `2 exp(-8n)`. The exponent in (3) follows.
6. The total algebraic failure coefficient is consequently
   `524288+16=524304`, as stated.

For the graph subspace
`v=(u,-E_0^T B_0u/64)`, the cross term is `-S/32`, and the final quadratic
term is `B_0^T(E_0 E_0^T)^2 B_0/4096`. Under the event (6), the latter is
at most `S/64`. Hence

\[
v^\top C v\le-\|u\|^2/256,\qquad
\|v\|^2\le(1+2/4096)\|u\|^2<2\|u\|^2.
\]

The negative Rayleigh bound `-1/512` follows, and the graph is injective
in `u`. The required min--max implication can be obtained just by
diagonalization: if fewer than `d` eigenvalues were at most that level,
the graph would intersect the complementary spectral space nontrivially,
contradicting its Rayleigh bound.

No union over labels is needed: the single initial matrix event implies
the subsequent deterministic conclusion for every finite label vector.
For fixed `d`, the probability bound tends to one. For `n` near `d`, the
stated lower bound may be negative and the sufficient event may even be
empty; the source expressly limits its informativeness to positive lower
bounds. This is not a contradiction. Finally, a lower input-space singular
value does not provide a sample-space gap when the columns of `X` are
dependent, exactly as the note states.

## Reconstruction of the invariant-level bad state

The initialized population covariance in (9) is correct: the scalar
variance is

\[
\frac14\left[\frac{1+e^{-2}}2-e^{-1}\right]
=\frac{(1-e^{-1})^2}{8}.
\]

For `d=2`, the Gaussian event supplies at least two negative eigenvalues.
Rank-two subtraction from `W(0)^T W(0)` supplies at most two. The source's
nonzero determinant-polynomial argument excludes zero eigenvalues almost
surely; thus its remaining eigenvalues are positive.

The proposed root `s` satisfies `s>b` and `s(s-b)=pi^2`. The resulting
matrix `C+A_*A_*^T/n` has the claimed eigenvalues. A factor `W_*` exists:
send `v_2` to the prescribed multiple of `1/sqrt(n)`, send `v_1` to zero,
and send the remaining `n-2` eigenvectors to mutually orthogonal output
directions perpendicular to `1` with their required singular values.
There is adequate output dimension. This gives both `W_*A_*=[0,pi 1]`
and the exact original value of `C`.

At this state the residual is `(-a,2a)`, the top derivatives vanish, and
`H^(2)r=0`. The local-minimum proof using positive readouts is valid:
all nearby predictions lie in `f_1-2f_2<=0`, and `(2a,a)` is the Euclidean
projection of `(3a,-a)` onto that halfspace. The mean loss is `5a^2/2`.
The corrective-group construction in Section 5 also shows interpolation is
available in the same model class. None of this supplies a trajectory from
the sampled initial point to the constructed minimum, and the note does
not make that inference.

## Reconstruction of the open attracting basin

At `A_0=[0,1]`, `W_0=pi I`, the hidden gradients vanish for all readout
values because both top preactivations are activation extrema. If all
readouts equal a scalar `b(t)`, equation (1) gives `b'=5(a-b)`. This
verifies the exact trajectory (11).

Near its limiting state, `W` remains invertible, so `(Z=WA,W,w)` are
legitimate smooth local coordinates. The transverse coordinates together
with `W` and the mean-zero part of `w` have exactly the original dimension.
For fixed complementary coordinates with `a+v_i>0`, direct expansion gives

\[
\mathcal L-\mathcal L_*
=\frac52e^2+\frac a{4n}\sum_i(a+v_i)Z_{i1}^2
+\frac a{2n}\sum_i(a+v_i)(Z_{i2}-\pi)^2+O(\|\xi\|^3).
\]

The three Hessian blocks in the source are therefore correct. Taking a
compact neighborhood with `a+v_i` bounded below and `W` uniformly
invertible makes the Hessian coercivity and coordinate norm-equivalence
constants uniform within this fixed-width neighborhood. Taylor's integral
formula gives a positive-definite averaged transverse Hessian, so its
action on `xi` has a lower norm bound. This proves both inequalities in
(13); tangential directions do not invalidate the gradient lower bound.

The path argument also has the correct direction. With speed
`v_theta=||dot(theta)||_(M^-1)` and `E=L-L_*`, one has
`-E'=v_theta^2` and `v_theta>=c_3 sqrt(E)`. Thus, where `E>0`,

\[
v_\theta=\frac{-E'}{v_\theta}
\le\frac{-E'}{c_3\sqrt E}.
\]

Integration gives (14). Shrinking the initial neighborhood until this
length is less than its distance to the outer boundary makes the
first-exit argument valid. The trajectory remains in the coordinate
neighborhood, has finite total length, and converges to `xi=0`; its
predictions are `(2a,a)`. At `E=0`, local coercivity gives `xi=0`, hence an
equilibrium, so the division poses no missing case.

Continuous dependence at a fixed sufficiently large time pulls this open
basin back to an open set on the hidden-parameter slice `w(0)=0`. The
specified perturbation has feature Gram determinant
`delta^2(n-1)/n^2`, strictly positive for `n>=2` and sufficiently small
nonzero `epsilon`. Its intersection with the pulled-back basin is nonempty
and open. The Gaussian law has positive density on that hidden-parameter
space, which proves strictly positive failure probability at each fixed
width, without any false appeal to positive mass of the zero-readout
hyperplane under a random-readout distribution.

The upper bound for a selected certificate restricted to `W_ii>pi/2`
also checks: each tail is at most `exp(-pi^2 n/8)` and there are `n`
independent diagonal entries. It bounds only that selected subset by
`exp(-pi^2 n^2/8)`, not the entire failure probability. The note correctly
keeps finite-width positive probability separate from a nonvanishing
probability as width increases.

## Corrective group, feedback, and limit audit

For the two fixed feature types, their fractions give the matrix in (15),
whose trace is five and determinant is `9p(1-p)`. Since `m=2`, the residual
equation is `dot(r)=-Gr`, without an omitted factor two. Its positive
eigenvalues ensure fitting. Solving for the two weighted readouts gives
`(1-p)u=7a/3`, `pv=-5a/3`; the stated endpoint, initial signs, and
small-`p` rate `9p/5` follow. At finite width the fractions must satisfy
`pn` integral, as stipulated; the asymptotic `p->0` can be taken along
admissible increasing-width fractions. It is not an additional conclusion
about Gaussian trajectories.

The time rescaling `tau=a t` is correct: the actual flow becomes metric
gradient ascent of `3f_1-f_2-(f_1^2+f_2^2)/(2a)`. The limiting readout
velocity lies between one and five because `1<=phi_2<=2`. The source calls
this limit formal and does not exchange fixed-label large-width and
infinite-time limits with an amplitude limit. A nonzero rare fraction at
each fixed amplitude cannot be discarded in the stated target.

Equations (17) and (18) were reconstructed directly from (1). In (17),
differentiating `AA^T/n` produces the preactivation `z^(1)=Ax/sqrt(d)`,
not the first activation `h^(1)`, so the displayed lack of cancellation
for a general nonlinear first activation is real. The row-balance formula
has the correct factor `-4/m` and the difference `z phi_2'(z)-phi_2(z)`.

At zero readout, `dot(w)=2Hy/m`, while both hidden velocities vanish.
Differentiating the hidden equations once gives the two accelerations
in (19), and differentiating `Z=WA` gives
`ddot(Z)=4[RQ+WW^T R]/m^2`. The conditionally unused Gaussian component
therefore enters through `V Pi V^T R` once F1's width/rank hypothesis is
supplied. The observation is a possible shared-layer feedback mechanism;
it does not assert nonzero feedback for every label or state (zero labels
give no movement, for example). A zero row of `R` need not be a zero row
of `WW^T R`, so suppressing one neuron's immediate readout response does
not isolate its hidden input from the other neurons' training.

With F2's orthogonality repair, the final persistent-projection argument
is correct. It supplies no independent lower bound on the size of a useful
reserve: the preserved component annihilates the current lower features.

## Unverified material and actual limits of this check

The external Pham--Nguyen paper was not an allowed input. Its initialization,
scaling, assumptions, and clause-specific applicability in Section 7 have
therefore **not** been independently checked here. No proof above imports
a result from that paper, so this limitation does not undermine the
self-contained results in Sections 1--6; it does prevent this report from
certifying the literature paragraph.

This check establishes neither a high-width Gaussian non-fitting theorem
nor an arbitrary-label high-probability fitting theorem. It gives no
compression guarantee or lower bound. The verified finite-width basin
can have very small Gaussian probability and a small empirical initial
gap. The verified all-time invariant protects only the linear first
activation's input-space geometry. The invariant-level equilibrium is
not shown reachable from the Gaussian point that supplied its invariant.

No numerical computation, formal verification, or fresh independent review
was performed. The proof check consisted of full source reading, direct
algebraic reconstruction, the explicit oblique-projection counterexample,
dimension and zero-denominator checks, and probability/limit-order audits.
The verdict and findings above attach only to the source hash recorded
at the start; a repaired source needs a recorded follow-up check.

## Follow-up check of the corrected and extended source

The supervisor supplied a corrected and extended candidate and requested a
substantive audit of its new Section 6.1. I reread the **complete** new file
using `cat`, without truncation, and independently recomputed its SHA-256:

`d005936028bbe05dab1279f8b431d5b632b9da22a1194f2ce6585f27a0ce3f89`.

The following resolutions were checked in that text:

- F1: Section 6 now assumes `n>d=m` and explicitly states the almost-sure
  full column rank of `U` before using the inverse.
- F2: The persistent projection is now explicitly orthogonal.
- F3: The expansion explanation now fixes the two preactivation columns
  while allowing `e` to vary.

The initial objections are therefore resolved for this version. The
additional neural-network literature paragraph was read but not verified
against its external source, consistently with the assignment. Neither
external neural-network theorem is a dependency of the mathematical proofs.

### Hidden-state surjectivity and full support

Write `v=(A/sqrt(n),W)` as in the new subsection. For any hidden initial
state and exact zero readout, the initial prediction is exactly zero, so
the initial loss is the same number `Y^2`. The full metric path bound in
(2) bounds its hidden-coordinate component and gives

\[
\|F_T(v_0)-v_0\|\le Y\sqrt T
\]

uniformly over the whole hidden initial space. This uniformity would not
follow in the same way from an arbitrary nonzero initial readout, but the
source keeps the zero-readout condition throughout.

For a target `z`, the map
`v -> z-(F_T(v)-v)` sends the closed Euclidean ball of radius
`Y sqrt(T)` about `z` into itself. Continuity follows from finite-time
continuous dependence of the smooth flow. The Brouwer theorem therefore
gives a fixed point and hence a preimage of `z`. The degenerate-radius
case is separately and correctly handled: zero labels or zero elapsed
time make `F_T` the identity.

I checked the cited classical theorem in the
[MIT text, Theorem 3.6.13, printed page 88](https://math.mit.edu/classes/18.952/2018SP/files/18.952_book.pdf),
including its displayed proof and adjacent approximation lemma. Its
continuous closed-unit-ball statement applies to the ball above by
translation and positive scaling. This source check confirms the invoked
statement and its hypotheses; it is not a new reconstruction of all
earlier degree-theory dependencies in that textbook.

Surjectivity plus continuity makes the preimage of every nonempty open
target set nonempty and open. The prescribed Gaussian hidden law has a
strictly positive density in these coordinates, so every such preimage
has positive probability. This proves full support. It does not require
`F_T` to be injective, preserve a density, or be a projection of an onto
full-parameter flow.

### Real analyticity and the null-set argument

The finite-dimensional vector field is real analytic when the activations
are real analytic. Its real squared-loss expressions extend holomorphically
locally by the same algebraic formulas; no complex conjugation is required
for this extension. A given finite real trajectory has compact image, and
the vector field admits local complex extensions along it. Taking short
time intervals with a contraction domain, performing Picard iteration
uniformly in a smaller complex neighborhood of the initial point, and
composing finitely many resulting local maps proves real-analytic
dependence at each initial state. Restriction to the linear zero-readout
slice and projection onto hidden coordinates preserve analyticity.
No width-uniform complex neighborhood or infinite-time analytic bound is
needed or asserted.

For a scalar real-analytic `P` that is nonzero somewhere, surjectivity
makes `P o F_T` nonzero somewhere on connected Euclidean initial space.
The source's zero-set proof is sound. At a zero, let `alpha` be a
multi-index of minimum positive order with a nonzero derivative. Removing
one differentiation gives a derivative `D^beta P` that vanishes there but
has a nonzero gradient component. The point lies on a regular hypersurface
of `D^beta P`. Countably many multi-indices and coordinate charts cover
the zero set by null hypersurfaces. A point with all derivatives zero
would force local, then connected-domain, identically zero behavior and
is excluded. Applying absolute continuity of the initial Gaussian law
proves (21) without assuming a density for the trained state.

### Rank realization for every width `n>=m`

Let `S` be the span of all possible first-layer feature rows `v(g)`.
The range identification `S=range(Q^(1))` is valid: a continuous function
`c^T v(g)` that vanishes Gaussian-almost-everywhere must vanish everywhere,
because a nonzero value would persist on an open set of positive Gaussian
measure. Thus the kernel of `Q^(1)` is `S`'s orthogonal complement.

There is no hidden need for `Q^(1)` to be positive definite. Even when it
is singular, `S` has dimension at most `m`, so at most `m` vectors from
the set of available first-layer rows span it. Positive definiteness of
`Q^(2)` implies that the available top feature rows `phi_2(z)`, `z in S`,
span all of `R^m`; otherwise a nonzero common orthogonal vector would have
zero quadratic form under `Q^(2)`.

For any `n>=m`, place a basis of the first-row span among the rows of `A`
and pad the remaining rows with any valid first-layer rows. Choose `m`
vectors in `S` whose transformed top rows are independent. Each chosen
preactivation vector is a linear combination of the first-layer rows,
and an unrestricted row of `W` realizes exactly those coefficients.
Thus the first `m` top rows form a rank-`m` matrix. The normalization of
the random initialization constrains its density, not the finite real
values allowed in this deterministic rank witness.

The Gram determinant is therefore a nonzero real-analytic function on the
whole hidden parameter space. Bounded first derivatives give at most
linear growth of activation values, ensuring that the two population
moments used in the hypothesis are finite. The argument needs only the
stated positive population top gap; it does not silently add independent
inputs, `m<=d`, or a first-layer population gap.

### Time and probability quantifiers

For each fixed width `n>=m`, fixed label vector, and prescribed finite
time `T`, the determinant vanishes with probability zero. A prescribed
countable collection of times follows by a countable union of null
events. These events need not be uniform over an uncountable family of
labels or times, and the source does not say they are.

Almost surely the determinant at time zero is nonzero. The trajectory
and determinant are analytic locally around every finite time. A
nonzero one-variable analytic function has isolated zeros; on any compact
time interval an infinite collection would have an accumulation point,
contradicting analyticity there. Hence possible rank-loss times are
locally finite along almost every path. This is consistent with a random
isolated rank-loss time having probability zero at each prescribed time.
It also permits a determinant that remains positive at every finite time
but tends to zero as time tends to infinity. The source's distinction
between these statements and a positive all-time gap is correct.

**Follow-up verdict:** the added Section 6.1 is internally checked for its
stated finite-width, fixed-time, zero-readout, analytic-activation scope.
Together with the resolved F1--F3 findings, there is no remaining local
correctness objection to Sections 1--6.1 at the new recorded hash. The
Gaussian fitting/compression question, quantitative persistence bounds,
and both external neural-network literature applicability assessments
remain outside what this report proves or independently verifies.

### Final notation-only version

The supervisor subsequently renamed the population first-feature vector
from `v(g)` to `h(g)` in Section 6.1 to distinguish it from the hidden
parameter coordinate `v`. I checked the changed passage, then reread the
complete 618-line source and recomputed SHA-256:

`9c08c9905aca1f7f4feee89d317278cd8d1de6ebf9338725000c5f30d9c09d5b`.

The definition of `Q^(1)` and every use in the span/range argument now
consistently use `h(g)`. The substantive arguments audited above are
unchanged. The follow-up verdict therefore applies to this final hash.
Any later supplementary observation requires its own recorded check.

## Final supplementary check: the typical-invariant-level basin

The supervisor supplied a final addition, Section 4.1, and an expanded
introductory description. I read both changed passages completely and
recomputed the final source SHA-256:

`a8138b6edfd1d62e1c0c235a4c2228605e0c55003366b7741c3d5823f29028a4`.

The prior complete-file checks cover the unchanged proof. The added
Section 4.1 passes the following direct checks.

### Coordinates at singular `W_*`

The earlier invertible-`W` chart cannot be used directly at the Section 3
base, but the new chart fixes that issue. Full column rank of `A_*` supplies
a nonsingular two-row minor `A_I`. Here `W_I` denotes the corresponding
two columns of `W`, so the matrix dimensions in

\[
Z=W_I A_I+W_{I^c}A_{I^c},\qquad
W_I=(Z-W_{I^c}A_{I^c})A_I^{-1}
\]

match exactly. Keeping the same minor nonsingular gives an open chart.
The coordinates `(Z,A,W_{I^c},w)` have dimension
`2n+2n+n(n-2)+n=n^2+3n`, equal to the original parameter dimension.
Their displayed inverse is smooth. Singularity of the full `W_*` poses
no remaining problem.

The loss still depends only on `Z,w`, and the same transverse coordinates
give exactly the earlier expansion and positive transverse Hessian.
Coordinate norm equivalence is local and fixed-width, which suffices for
the unchanged energy, finite-length, and trapping argument. At the hidden
base, both top derivatives vanish and the zero-readout trajectory is
again `w(t)=a(1-exp(-5t))1`. Pulling back the attracting neighborhood
therefore gives an ambient open basin on the zero-readout slice near
each constructed base.

### Exact invariant preservation and full-rank features

Left multiplication by an orthogonal output rotation preserves `W^T W`.
Since `A` is held fixed, both the exact invariant `C` and the first-layer
Gram are preserved. The two preactivation columns become `0` and
`pi R_epsilon 1`. With the stated planar rotation convention, their first
two entries are `pi(cos(epsilon)-sin(epsilon))` and
`pi(cos(epsilon)+sin(epsilon))`. The identity

\[
\cos(\pi(\cos\epsilon-\sin\epsilon))
-\cos(\pi(\cos\epsilon+\sin\epsilon))
=2\sin(\pi\cos\epsilon)\sin(\pi\sin\epsilon)
\]

is correct and strictly positive for sufficiently small positive
`epsilon`. Thus the second feature column is nonconstant whereas the
first is the nonzero constant `2 1`. The two columns are independent,
including in the two-coordinate edge case. The perturbed start remains
inside the open basin for a sufficiently small rotation.

For an ambient neighborhood, take the intersection of that basin with
the open full-feature-rank set and a sufficiently small spectral-continuity
neighborhood. If its invariant differs in operator norm from the base
invariant by less than `min(alpha,b)/2`, it retains two eigenvalues at
most `-min(alpha,b)/2`. The invariant argument of Section 2 then gives
the stated all-time first-Gram floor `min(alpha,b) I_2/2`. This ambient
open set has positive Gaussian probability at each fixed width.

These are appropriately distinct conclusions: a deterministic bad start
with full-rank top features exists on the exact prescribed invariant
level, while an ambient neighborhood gives positive finite-width
Gaussian probability with a protected first Gram. The argument does not
claim that a Gaussian initialization conditional on that exact invariant
has a quantified probability of reaching the displayed equilibrium.
It also does not give a width-uniform probability bound.

### Residual-direction integral

The normalization in (14a) is correct. For the note's mean loss and
`m=2`, the residual satisfies `dot(r)=-Kr`, and hence

\[
\frac d{dt}\log\mathcal L
=-2\frac{r^\top Kr}{\|r\|^2}.
\]

Every zero-readout start has loss `5a^2`, while every trajectory in this
basin tends to loss `5a^2/2`. In particular its residual never vanishes,
so the quotient and logarithm are defined throughout. Integrating to a
finite time and passing to the positive limiting loss yields precisely
`(log 2)/2`. The integrand is the unnormalized residual Rayleigh rate;
the rate divided by `m` would instead integrate to `(log 2)/4`.

At the endpoint, vanishing top derivatives eliminate hidden tangent
contributions. The residual `(-a,2a)` is annihilated by each top feature
row `(2,1)`, so it is in the nullspace of both the feature Gram and the
full tangent Gram. The result disproves a deterministic all-time
residual-coercivity principle even when the first Gram is protected and
the initial top Gram is positive definite. It does not disprove the
fixed-label, sufficiently-large-width high-probability target.

**Final supplementary verdict:** no new correctness objection was found.
The internal-check verdict for Sections 1--6.1, now including Section 4.1,
applies to the final hash above. The expanded introduction accurately
describes these scoped results. The reused-context and external-literature
limitations recorded earlier remain in force.
