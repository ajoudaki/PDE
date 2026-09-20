# Internal independent audit of stationary geometry

Date: 2026-09-18. Verdict: **PASS for the final source and its stated scope.**
The finite-state classification, prediction-differential singularity criteria,
saddle theorem, zero-loss representability construction, and necessary
stationary-loss list are valid. No claim of saddle avoidance, uniform
coercivity, or convergence of canonical training to zero loss follows.
This is an internal mathematical check, not a promotion review.

## Frozen inputs and review scope

Scientific inputs read were the complete `stationary_geometry.md`, the complete
`docs/observable_p1.md`, and the subsequently authorized existence dependencies
`docs/global_nonlinear.md` C.4.7.9.4 and the “Energy, existence and restart”
portion of C.4.7.10.D.3. No other study, study README, other review, prior
verdict, or study history was read. Required rigorous-mathematics and
conjecture-audit skills were applied. No numerical experiment was run; exact
rational enumeration was the only calculation executed.

SHA-256 hashes:

| Input | SHA-256 |
|---|---|
| `studies/p1_three_input_geometry_20260918/stationary_geometry.md` | `2fce30a3824d8bff4ecc9b04771f3986bc539735722f3434168103c464e7cfbc` |
| `docs/observable_p1.md` | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` |
| `docs/global_nonlinear.md` containing the authorized excerpts | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |
| C.4.7.9.4, lines 12310–12376 inclusive, original bytes including line endings | `4b5755116ee4cc59d0085f1a638fde8b0df636e7936145949f82a78ab68cf1ee` |
| C.4.7.10.D.3 existence paragraph, lines 15331–15371 inclusive, same convention | `0c38acc8f8179d21d87a63cd595e5a309881ce711d98001bd7430faa5e41072d` |

The whole-file hash for `global_nonlinear.md` identifies the container; it does
not assert a review of its unassigned contents. The final source incorporates
two scope corrections requested during this audit: binary labels delimit the
loss/saddle statements, and arbitrary nonodd active fields are explicitly an
auxiliary reduced extension. Both corrections are sufficient.

## Claim-specific checks

### 1. Canonical coefficients, mark support, state and energy — PASS

The active features are exactly the nonconstant d=2 features in
`observable_p1.md`, with the same positive normalization constants and ridge.
The full active matrix remains 2 by 4; no rank, diagonal, or rotational
symmetry assumption is introduced. The source's parity argument justifies
discarding the constant coordinates on the stated odd canonical class.
Outside that class the final report correctly limits its equations to a
reduced extension.

Each lower map `(G_i,Z_i) -> (h_i,k_i)` is a smooth bijection with a smooth
inverse and nonzero Jacobian on the open square. The Gaussian density is
strictly positive, so the transformed four-dimensional law has positive
density on the asserted open set. Recovering G from h makes g a smooth
function of b1 there. In particular, g is bounded on a sufficiently small
closed ball inside the support. The upper law has the stated positive open
square support for the same reason. These are population facts and do not
extend automatically to a finite sampled population.

Differentiation of each prediction yields the displayed readout, matrix and
lower-row gradients, including the actual transpose of the same M. The factor
2 is consistent with unhalved weighted squared loss. Pairing the negative
gradient with the velocity gives equation (3) in the stated physical metrics.

### 2. Upper ridge independence and ambient stationary equations — PASS

After collapsing sign repetitions and removing zero vectors, a generic line
avoids all finitely many forbidden linear conditions. On that line the first
k odd Taylor coefficients, k at most 3, produce a Vandermonde matrix in
distinct nonzero squared projections. Positive density and continuity justify
turning an almost-sure identity into an identity on that line. Thus unequal
nonzero magnitudes on the same line do not create extra ridge relations.

The resulting signed residual cancellation in each nonzero class is exactly
readout stationarity. Evenness of the upper gate gives `d_i=d_C` under both
signs. Adding the independent matrix and row stationarity equations is
necessary and sufficient, so equation (5) is complete for the declared ambient
active equations. The report does not incorrectly substitute readout
stationarity for stationarity of all blocks.

### 3. Lower submersion for arbitrary bounded displacement — PASS

This is the central nondegeneracy step. Pairwise nonparallel inputs have a
one-dimensional dependence with all three coefficients nonzero. If one
adjoint coefficient vanishes, independence of the other two input directions
and open support force every coefficient to vanish.

Otherwise, equation (7), on a small support ball where g and w are bounded,
gives two-sided constant comparisons between the absolute values of the
linear forms `b1·xi_i`. No regularity of w beyond measurable bounded
displacement is needed. The comparisons extend from almost every mark to
every point of the ball because the linear forms are continuous and every
open subset has positive probability. Inclusion of linear-form kernels on
this ball implies their global proportionality by scaling vectors into the
ball.

Cancelling the resulting common linear form is legitimate off a null
hyperplane. It forces each ratio of gates to be a constant. The bounded
remainder in the logarithmic gate identity then bounds
`||w·u_i|-|w·u_j||`; bounded displacement transfers that bound to g. Since
`1-|u_i·u_j|>0`, Gaussian support in neighborhoods of `t u_i` contradicts any
essential bound. The contradiction is valid despite those neighborhoods
having very small probabilities.

The adjoint maps finite-dimensional coefficients to bounded functions.
Injectivity therefore makes `JJ*` positive definite and gives the bounded
right inverse used in the report. At odd w the adjoint outputs are odd, so
surjectivity also holds with only parity-preserving variations. This proves
pointwise surjectivity, not a time-uniform lower singular-value bound. The
ambient counterexample w=0 correctly lies outside bounded displacement from
Gaussian g.

### 4. Rank-two, rank-one and zero-matrix classification — PASS

Applying lower submersion to row stationarity gives the individual equations
`R_i M^T d_i=0`. If M has rank two, injectivity of `M^T` makes these
`R_i d_i=0`; every term of the matrix gradient then vanishes individually.
If M has rank one, residual-active d-vectors lie in the single transverse
direction, and the remaining vector equation
`sum_i R_i delta_i a_i=0` is still necessary. The report retains it.

At M=0 every upper activation and prediction vanishes. Binary labels of
absolute value one and total mass one give loss one. The only potentially
nonzero gradient is the matrix gradient, and its vanishing is precisely
`d0 S^T=0`, equivalently `d0=0` or `S=0`. No cases are omitted.

### 5. Prediction-differential singularity — PASS

Pairing an arbitrary sample covector with the three independent block
variations gives equation (10). The same lower-submersion argument is
applicable without involving residuals. For rank two, allowed covectors are
supported only on samples whose d-vector vanishes. In a nonzero sign class
they must additionally satisfy one signed-sum constraint; a nonzero solution
exists exactly when that class has at least two elements. Zero-vector samples
have no readout constraint. This proves the exact rank-two criterion stated.

The rank-one matrix constraint remains necessary. At M=0 and d0 nonzero,
`N -> N^T d0` covers all four-dimensional covectors, so the prediction
differential has rank equal to the column rank of `[a1 a2 a3]`; at d0=0
every first prediction variation vanishes. Multiplication by positive data
weights preserves these ranks. These are qualitative singularity statements,
not coercivity bounds.

### 6. Confluent upper derivative outside the ridge span — PASS

The tanh differential equation gives the displayed positive recursion for
the magnitudes of all odd Taylor coefficients. For distinct squared line
projections X_j, the sequence operator `P(E)=product_j(E-X_j)` annihilates
every `X_j^n`, while

`P(E)[(2n+1)X_i^n] = 2 X_i^(n+1) P'(X_i)`.

The latter is nonzero because the roots are distinct and X_i is positive.
This proves the required confluent ridge derivative cannot lie in the
current ridge span, including when other vectors are collinear with it but
have different magnitudes. The separate Vandermonde argument for a nonzero
linear function works by choosing the generic line with nonzero projection
on that function's vector. Empty ridge spans also cause no exception.

### 7. Negative second variation at nonzero M — PASS

At a positive-loss stationary point some R_i is nonzero and
`M^T d_i=0`. The selected nonzero v lies in the image of M. Lower
surjectivity permits changing only the selected sample's first upper vector
by v. The projected readout perturbation is nonzero by the previous claim,
bounded, odd, and orthogonal to every current ridge.

Every first prediction variation along the combined direction is zero.
The mixed second prediction derivative for the selected sample is
`2 lambda E[delta_c p] = 2 lambda ||delta_c||_2^2`.
Consequently the loss second derivative is exactly
`Q(0)+4 lambda R_i ||delta_c||_2^2`. The factor is correct, there is no
quadratic lambda term, and all pure lower variations remain in Q(0). A finite
lambda with appropriate sign gives a negative value. Scaling the resulting
fixed direction gives arbitrarily small admissible perturbations. In fact
both signs of second variation occur. The argument covers rank one as well
as rank two and includes the case z_i=0.

### 8. Zero-matrix Hessian and cubic descent — PASS

At M=0 the first prediction variation is `d0^T N A_i`; the second one is
`2 m^T N A_i + 2 d0^T N delta_A_i`. Substitution into the unhalved loss
second derivative gives equation (13) exactly. The covariance of b2 is
positive definite, so every m is realized by the displayed bounded odd
readout perturbation. Lower submersion and the nonzero binary labels make
every delta_S available.

The two nonexceptional stationary cases therefore admit a negative second
variation as stated. If d0 and S both vanish, all second variations vanish.
Expanding the line in the report gives

`f_i(t) = t^2 m^T N A_i + t^3[m^T N delta_A_i - E(c (b2^T N A_i)^3)/3] + O(t^4)`.

Terms involving higher lower-feature derivatives multiplied by d0 vanish.
The weighted label sum loses its quadratic term because S=0. The cubic
coefficient can be made positive by choosing delta_S, while the squared
predictions start at order four. Thus the claimed cubic loss descent is
valid. Bounded perturbations and bounded tanh derivatives justify uniform
integrable Taylor remainders; the unbounded base g introduces no remainder
problem. “Hessian” here is the second variation on the declared bounded
perturbation domain, which is sufficient for the local-minimum conclusion.

### 9. Zero-loss representability — PASS

At w=g, lower surjectivity provides any chosen 4-by-3 first feature
variation using a bounded odd perturbation. In singular-vector coordinates,
putting first-order diagonal entries in exactly the missing singular
directions makes a three-row minor have nonzero leading determinant of order
`t^(3-r)`. Off-diagonal Taylor remainders cannot change this leading term.
This also handles r=0 and r=3. Hence a nearby admissible state has three
independent lower-feature columns.

A finite linear map M can prescribe the images of those independent columns
as `e1,e2,e1+e2`. Their upper ridges are independent by Lemma 1, and their
positive definite Gram permits an exact interpolating readout in their span.
That readout is bounded and odd. This establishes a zero-loss state in the
same class, independently of any claim that training reaches it.

### 10. Stationary-loss values and positive gap — PASS

The class loss is the weighted variance of its signed binary targets,
namely `4 P_C N_C/(P_C+N_C)`. Zero-vector samples contribute their masses.
Every positive mixed-class contribution is at least
`2 min(P_C,N_C)`, and a nonempty zero subset contributes at least the
smallest sample mass. The general stated lower bound therefore holds.

For q=3/4, exact rational enumeration yields precisely the report's necessary
list:

`0, 1/8, 3/8, 2/5, 7/16, 1/2, 5/8, 31/40, 6/7, 7/8, 15/16, 55/56, 1`.

For additional arithmetic checks, the three conflicting-pair contributions
are `3/8, 6/7, 2/5`; adding the complementary zero singleton gives
`7/8, 55/56, 31/40`. The three all-sample split values are
`15/16, 7/16, 1`. The source correctly calls this a necessary list and does
not assert every combinatorial configuration is realizable by a full
stationary state. Equilateral rotations preserve the hypotheses used here;
this says nothing about rotation invariance of the initialization or flow.

### 11. Finite-time reachability and long-time limitations — PASS

The authorized canonical existence excerpts establish local Lipschitz
evolution in bounded displacement, bounded readout and finite matrix norms,
followed by finite-time continuation from energy and speed bounds. Their
conditions hold for the bounded p=1 features and the given unit inputs.
Parity invariance keeps the canonical solution inside the class required by
the finite-state results. Thus applying those results at every reached
finite state is justified.

Local uniqueness also holds with reversed time on a sufficiently short
interval. A nonstationary trajectory therefore cannot hit a stationary
point at finite time. The source correctly leaves initial nonstationarity
as a separate condition. Since initial loss is one, strict descent together
with monotonicity excludes later states where all upper vectors vanish,
including M=0. It does not exclude rank-one M or isolated collisions.

The report explicitly retains the necessary missing bridges: a deterministic
trajectory may approach a saddle through its stable set; finite-time bounds
need not be uniform as time grows; an L2 limit need not have bounded
displacement; and pointwise submersion permits asymptotic degeneration.
Positive limiting loss with parameter escape is not excluded by the finite
stationary-loss list. No passage from finite-state geometry to an all-time
zero-loss theorem is justified or asserted.

## Final disposition

No unresolved mathematical defect was found in the final hashed source.
The conclusion is an internally checked exact population landscape result
for the specified three-input problem and canonical parity class. It does
not establish a training-convergence theorem, a finite-population theorem,
or a neural-network limit, and it is not promotion approval.
