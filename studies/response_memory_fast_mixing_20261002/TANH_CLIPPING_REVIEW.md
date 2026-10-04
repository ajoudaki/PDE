# Internal audit of the tanh clipping bridge

**Verdict: the conditional transfer can be proved without a higher-moment
assumption on the adaptive backward fields.** The frozen draft has the right
mechanism. Its two unfinished points need explicit repair: use a capped row
metric for every retained first-layer velocity and stage copy, and restrict
the observable class to bounded Lipschitz tests or stated continuous functions
of their empirical averages. The lemma below supplies those repairs.

This is an internal same-context mathematical audit, not an independent
promotion review. Premise (P) is an **unproved assumption throughout**. No
literature was fetched, no external AMP theorem was invoked, and no claim that
(P) has been proved is made. No GPU or experiment was used, and the original
draft was left unchanged.

Inputs read, with SHA-256 at review start:

| Input | SHA-256 |
|---|---|
| `TANH_TRANSFER_DRAFT.md` | `dcd7c460442bbf0cc644581fa1987ced9844aac406a8da1805c89f9b6d969f81` |
| `TRAINING_PROTOCOL.md` | `2a622aaff0c6a61eff84bc58df8439cab6707a450d1c7a64be924d3cee5dcd08` |

## Precise conditional statement

Fix training sample count (m), input dimension (d), a finite query list,
all inputs and labels, step size (\eta>0), and integer step count (J).
They do not depend on width (n). Use exact-arithmetic Heun integration of
the supplied q=1 tanh equations, with (A(0)) having independent standard
Gaussian rows, (w(0)=D(0)=0), (H_a(0)=h_a(0)), and (\tau(0)=1).
The initial Gaussian coordinate channels are independent of (W_0).

Assume the following corrected version of (P): for the two matrix ensembles
being compared, every fixed finite program built from (W_0,W_0^\top), the
allowed independent initial channels, globally Lipschitz coordinate maps with
finite history, and Lipschitz scalar feedback from bounded empirical averages
has identical deterministic limits in probability for its **bounded Lipschitz
empirical tests**. Continuous functions of a finite list of such convergent
averages are also allowed, by continuity. Zero/redundant channels are allowed.
Assume also that one fixed (C<\infty) satisfies

\[
\Pr(\|W_0\|_{\mathrm{op}}\le C)\longrightarrow1
\]

under each ensemble. This is an assumption about the full finite-program
class required below, not a consequence established here of a narrower AMP
or polynomial-iteration theorem.

Then the actual, unclipped q=1 Heun programs have common deterministic limits
in probability for predictions at the fixed times/queries, their sample
feature Grams, bounded Lipschitz empirical state tests as qualified below,
and continuous functions of finitely many such averages. In particular, RMS
feature displacements qualify. No higher-moment assumption on
(W_0^\top\delta_a) is needed. This is a fixed finite-step conclusion; it
does not exchange width with time, depth, sample count, step refinement, or
floating-point precision limits.

## 1. Uniform bounds for every clipping hybrid

Write (Y=\max_a|y_a|). At a full state with (|w_i|\le M), tanh boundedness
gives (|f_a|\le M), (|r_a|\le M+Y), and
(|\dot w_i|\le2(M+Y)). The predicted readout therefore satisfies

\[
|\widetilde w_i|\le M+2\eta(M+Y).
\]

Applying the same readout estimate to the second Heun stage gives

\[
M_{k+1}=(1+2\eta+2\eta^2)M_k+(2\eta+2\eta^2)Y,
\qquad M_0=0.
\]

Take (M=M_J). Because (\eta,Y\ge0), this bounds every full readout state
and every predicted readout state through step (J). The argument uses only
bounded activations, so it holds for every program obtained by clipping an
arbitrary subset of read-in velocity writes, at arbitrary thresholds.

Set (T=J\eta). At both stages, (\rho\le M+Y) and
(|\delta_{ai}|=|w_i(1-g_{ai}^2)|\le M). Consequently all full and predicted
states satisfy

\[
1\le\tau\le1+T(M+Y),\qquad
|H_{ai}|\le B_H:=1+T(M+Y),\qquad
|D_{ai}|\le B_D:=TM(M+Y).
\]

The Heun weights are positive: a full increment is the average of two stage
increments times (\eta), and a predictor uses one such increment times
(\eta). This proves the bounds for stage copies as well as accepted states.
Clock increments are nonnegative, so its lower bound is preserved. All bounds
are independent of (n), the Gaussian row magnitudes of (A(0)), and every
clipping threshold.

For each training example define the backward matrix response and its memory
correction by

\[
p_a=W_0^\top\delta_a,\qquad
b_a=\frac{2}{mn\tau}\sum_{b=1}^m H_b(D_b^\top\delta_a).
\]

The actual first-layer velocity has rows

\[
\dot A_i=-\frac{2}{m\sqrt d}\sum_{a=1}^m
r_a(1-h_{ai}^2)(p_{ai}-b_{ai})x_a^\top.
\]

The bounds above imply (|b_{ai}|\le2B_HB_DM). On
(\|W_0\|_{\mathrm{op}}\le C),

\[
\frac{\|p_a\|_2^2}{n}\le C^2M^2,
\qquad
\frac1n\#\{i:|p_{ai}|>R\}\le\frac{C^2M^2}{R^2}.
\]

This is deterministic, including when (\delta_a) depends adaptively on
(W_0). It uses a normalized second-moment bound, not uniform integrability
of (p_a^2), a higher moment, or independence of the backward response.

## 2. The augmented state that makes Heun reuse legitimate

Unroll the computation into a finite straight-line program that retains every
quantity used later. In each Heun step, retain the accepted state, the first
RHS, the predictor, the second RHS, and the accepted output. In particular,
retain both (\dot A^{(1)}) and (\dot A^{(2)}) until the final update

\[
\widetilde A=A+\eta\dot A^{(1)},\qquad
A^+=A+\frac\eta2(\dot A^{(1)}+\dot A^{(2)}).
\]

Distinct copies remain distinct channels even if their values initially
coincide. Retaining the entire finite history is harmless because (J,m,d)
and the query list are fixed. This is a mathematical bookkeeping expansion of
the actual Heun scheme, not an altered update.

For each unbounded row channel (U\in\mathbb R^{n\times d}), including every
(A) copy and every stored (A)-velocity, use

\[
d_c(U,V)=\left[\frac1n\sum_{i=1}^n
\min\{\|U_i-V_i\|_2,1\}^2\right]^{1/2}.
\]

Use normalized Euclidean norms for bounded neuron channels and for unbounded
matrix-action temporaries such as (W_0h_a,p_a). Use ordinary finite-dimensional
norms for scalar feedback. Sum these finitely many component distances to
obtain an augmented-state metric. The number of channels is independent of
(n).

The metric assignment is important: placing a stored unbounded (A)-velocity
in ordinary normalized Euclidean distance would reopen the tail problem.
Its rare, large clipping error need not tend to zero in that stronger norm.

For fixed scalars (c_j), the capped triangle inequality and Minkowski give

\[
d_c\left(\sum_jc_jU_j,\sum_jc_jV_j\right)
\le\sum_j\max\{1,|c_j|\}\,d_c(U_j,V_j).
\]

Indeed, pointwise,
(\min\{\|\sum_jc_j\Delta U_j\|,1\}
\le\sum_j\min\{|c_j|\|\Delta U_j\|,1\}).
Thus predictor formation, final averaging, buffer copies, and reuse of a
previously unclipped velocity are all Lipschitz in this augmented metric.
No bound on the magnitude of a stored velocity row is required for these
linear operations.

## 3. Clipped suffix stability and its relation to (P)

At a write of the (A)-velocity buffer, replace each (p_{ai}) in that write
only by (\operatorname{clip}(p_{ai},[-R,R])). Leave the stored (p_a), all
other RHS components, and the original equations elsewhere unchanged. There
are exactly (N=2J) such writes; the case (J=0) needs no clipping.

For a fixed query (x), with (h_i(A)=\tanh(A_ix/\sqrt d)),

\[
|h_i(A)-h_i(A')|
\le\max\{\|x\|_2/\sqrt d,2\}
\min\{\|A_i-A'_i\|_2,1\}.
\]

It follows that (A\mapsto h), and also (A\mapsto1-h^2), are Lipschitz
from the capped row metric to normalized Euclidean distance. Matrix actions
cost at most (C) in the latter norm. Empirical products of uniformly bounded
channels are Lipschitz by Cauchy–Schwarz; their normalizations are (1/n), so
the constants do not grow with width. The reconstructed forward and transpose
memory terms involve only such products, bounded channel factors, and
(1/\tau\) with (\tau\ge1).

The problematic product in an unclipped read-in write becomes harmless after
clipping. Its difference splits into a bounded-response term times the
activation-derivative difference and a 1-Lipschitz clipped-response difference:

\[
u\operatorname{clip}(p,R)-u'\operatorname{clip}(p',R)
=(u-u')\operatorname{clip}(p,R)
+u'[\operatorname{clip}(p,R)-\operatorname{clip}(p',R)],
\]

where (u=1-h^2\) satisfies (0\le u\le1). The resulting constant may depend
on (R) and the fixed bounds, but not on (n) or the incoming row magnitudes
of (A). Bounded residual factors and fixed inputs preserve this property.
The memory-correction product is bounded without clipping (p).

The scalar feedback (\rho=\|r\|_2/\sqrt m) is globally Lipschitz as a
function of the finite residual vector. One must use this norm formulation,
not assert that the scalar map (s\mapsto\sqrt s) is Lipschitz at zero.
This also avoids any special nonzero-residual assumption.

For the global coordinate-map hypotheses of (P), insert coordinate projections
to the proved bounds before reading (w,H,D), and project clock reads to
([1,1+T(M+Y)]). The projections leave every valid original, clipped, and
hybrid path unchanged. Products then have bounded factors and are globally
Lipschitz; additive updates of unbounded (A) or velocity channels remain
ordinary globally Lipschitz linear maps. Bounded empirical products supply
the scalar feedback. Consequently the fully clipped finite program lies in
the class **assumed** in corrected (P).

Likewise, after the incoming write location, any suffix whose remaining
read-in writes are clipped has a finite Lipschitz constant in the augmented
metric on the operator-norm event. Previously computed unbounded velocities
can be reused because they enter only the linear row operations above before
bounded activations are evaluated. Previously computed (p_a) channels are
read through clipping in subsequent read-in writes. This is the required
suffix statement; global Lipschitzness of the original, unclipped program is
neither asserted nor needed.

## 4. Sparse local error and reverse threshold choice

Compare original and clipped versions of one velocity write at the same
incoming augmented state. Only the newly written (A)-velocity can change.
It changes only on

\[
B_R=\bigcup_{a=1}^m\{i:|p_{ai}|>R\},
\qquad
|B_R|/n\le mC^2M^2/R^2.
\]

Therefore its local augmented-metric error is at most

\[
d_c(\dot A,\dot A^{[R]})\le\sqrt m\,CM/R.
\]

This bound does not contain the magnitude of the changed rows, the read-in
velocity, or a tail second moment. Fixed Heun coefficients enter only through
the later Lipschitz constants. If (M=0), every (p_a=0) and this error is
already zero.

Enumerate the velocity writes chronologically as (1,\ldots,N). Compare
hybrids by replacing write (N) first, then (N-1), down to 1. At the
comparison for write (j), the prefix through its input is identical in the
two programs and may contain unclipped writes. The suffix contains only
already-clipped future writes, with fixed thresholds (R_{j+1},\ldots,R_N).
Let (S_j<\infty) be a Lipschitz constant from the output of write (j) to
the requested final observable vector, including all buffer reuse, saved-time
observables, and non-write instructions. Its dependence on later thresholds
is permitted; it does not depend on (R_j) or (n).

For any (\varepsilon>0), choose thresholds backwards so that

\[
S_j\sqrt m\,CM/R_j\le\varepsilon/N.
\]

All thresholds are finite constants independent of width. The coordinate
bounds proved in part 1 apply to every hybrid, so the local error estimate
remains valid throughout this replacement sequence. Summing the (N)
comparisons gives a deterministic observable error at most (\varepsilon)
on (\|W_0\|_{\mathrm{op}}\le C), for either ensemble. This proves the
essential uniform approximation. A single shared threshold with an increasing
suffix constant would not provide this argument.

## 5. Common limits and the exact observable boundary

For each tolerance (\varepsilon_k\downarrow0), construct one such fully
clipped program. By assumed (P), its bounded Lipschitz observable vector
converges in probability to a deterministic value (a_k), common to both
matrix ensembles. Couple any two clipped programs to the same original
program within one ensemble. Their difference is at most
(\varepsilon_k+\varepsilon_l) on the common operator-norm event. Since that
event has probability tending to one, taking their deterministic limits gives

\[
\|a_k-a_l\|\le\varepsilon_k+\varepsilon_l.
\]

Thus (a_k\) is Cauchy and has a common limit (a). For fixed (k), compare
the original observable to its clipped counterpart, then take (n\to\infty);
finally let (k\to\infty). The deterministic approximation and the vanishing
probability of the exceptional norm event yield convergence in probability of
the original observable to (a), under both ensembles. There is no hidden
exchange of (k\) with (n), no almost-sure conclusion, and no new moment
hypothesis in this step.

Predictions and feature Grams are bounded Lipschitz empirical averages after
the indicated bounded extensions. A bounded globally Euclidean-Lipschitz row
test also works in the capped row metric: if its bound is (B) and Lipschitz
constant is (L), its pointwise change is at most
(\max\{L,2B\}\min\{\|\Delta A_i\|,1\}), followed by Cauchy–Schwarz when
averaging. Finite histories can be included as additional row channels.

For RMS feature motion, first transfer the bounded empirical squared
displacement, then apply continuity of the square root. This uses no
Lipschitz assertion for scalar square root at zero. Equivalently, RMS motion
itself obeys the reverse triangle inequality in the normalized feature norm.

Arbitrary bounded test functions do **not** follow from this argument.
Indicators with a discontinuity at the limiting value can fail under vanishing
perturbations. Classification errors, for example, require an appropriate
nonzero limiting margin or a separate continuity argument. Bounded continuous
tests that are not uniformly continuous require an additional justified
tightness/approximation step; they should not be silently included either.
Unbounded weight moments, strong Euclidean convergence of (A), or equality
of full parameter trajectories are not controlled by the capped metric.

## What this audit resolves

The adaptive backward response needs only the deterministic normalized
second-moment estimate supplied by the operator norm and bounded readout.
Sparse-coordinate clipping, complete Heun-buffer bookkeeping, and backwards
threshold selection then establish the finite-step conditional transfer.
The missing work is the actual proof or verified import of corrected premise
(P). This audit removes a proposed tanh/product obstruction conditional on that
premise; it does not establish the premise, confer exclusive universality on
response-memory learning, or strengthen the finite-step result into an ODE or
all-time theorem.
