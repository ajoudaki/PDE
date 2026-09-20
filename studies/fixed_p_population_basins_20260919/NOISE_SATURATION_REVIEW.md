# Independent audit of the saturation obstruction and conditional progress theorem

2026-09-19. Independent isolated mathematical review; no promotion decision.

## Verdict and frozen scope

**PASS for the stated obstruction and the conditional Gram theorem.** I found no substantive normalization, gradient, probability-quantifier, or data-class error. The report correctly leaves convergence of the accepted process from canonical initialization unresolved. A sequence of valid states is not a stochastic escape or trapping trajectory.

Complete scientific inputs read:

- `NOISE_CLOSURE_ROUTE.md`, SHA-256 `3c4537c2c9574304c751d04b3e0953962ee265107124e3db08790208d18a1129`.
- `ESCAPE_AND_LIMITS.md`, SHA-256 `544a5fde3b224cfa30539754c5d27123b900c12ed3fe5df98df00d5a8dd20ac2`.
- Established `docs/global_nonlinear.md`, lines 13161–13786 and 15146–15528: C.4.7.10.B/C.1 and D.3.

Both supplied hashes were verified before the audit. I read the required `solve-math-rigorously` skill. I did not read the study README, history, other studies, or other reviewers' findings. This report is the only written artifact. The verification below is exact; no numerical experiment is needed or used.

## 1. Canonical normalization, data, and state validity

The constant is first in the prescribed raw dictionary. The first row of the inverse of the lower Cholesky factor therefore gives

\[
b_{\ell,0}=(1+\eta_p)^{-1/2}=\beta_\ell>0.
\]

Thus `v_0=E_1[b_1]` is nonzero, and the matrix in equation (3) is well-defined. Direct substitution gives

\[
b_2^TM_*v_0
=\frac{\kappa}{\beta_2|v_0|^2}
 (b_2^Te_0)|v_0|^2=\kappa.
\]

This verifies the constant upper preactivation coefficient without assuming that the entire normalized feature column has mean zero. The construction works separately with each canonical order's actual ridge and complete frozen joint law. It neither whitens again nor substitutes a different transpose or population metric.

The table uses normalized inputs `u_i`; the corresponding physical data are `x_i=sqrt(2)u_i`. Their label masses are exactly one half each. Moreover

\[
|u_2-e_1|=2\sin(\theta/2)<\theta<\rho<2\rho,
\]

and the other two inputs equal their required centers. These data belong to the exact `V_rho` of D.3, despite its extremely small positive radius. All three directions are distinct and non-antipodal; there is no duplicate-label or oddness incompatibility.

The constant field `w_R=Rv` is in the assigned full lower `L2` space for every finite `R`, with norm `R`. The frozen `(b_1,g)` law is unchanged. Its difference from `g` need not be bounded, but it is in `L2`; the full-Hilbert-space extension proved in `ESCAPE_AND_LIMITS.md`, Section 1, is sufficient. No reachability from initialization is needed for a counterexample to a state-uniform bound.

## 2. Exact loss and all gradient blocks

The three projections are `(alpha,-alpha,-beta)` with `0<alpha<beta`. Therefore the actual upper features are constant fields with values `(a_R,-a_R,-b_R)`, where `0<a_R<b_R<tau`. Expanding the unhalved probability-weighted loss gives

\[
\frac14(ca_R-1)^2+\frac14(-ca_R-1)^2
 +\frac12(-cb_R+1)^2
=1-b_Rc+\frac{a_R^2+b_R^2}{2}c^2.
\]

This confirms equations (5)–(6), including `ell_R<3/4`. Completing the square then proves exactly

\[
L(S_R)=3/4+1/R<1\quad(R>4),\qquad
c_R\longrightarrow (2\tau)^{-1}.
\]

Consequently every fixed sublevel `L<=a` with `3/4<a<1` contains an unbounded tail of this sequence. This is the precise sublevel range directly demonstrated by the descending sequence; it is enough to refute the proposed coercivity argument.

For the gradients, let `s=(1,-1,-1)` and `m=sum_i mu_i y_i s_i=1/2`. The residual limit is `r_i^*=m s_i-y_i`, and

\[
\sum_i\mu_i r_i^*s_i
=m\sum_i\mu_i s_i^2-\sum_i\mu_i y_i s_i=0.
\]

The canonical population readout gradient tends to `2 tau` times this scalar. The middle gradient tends to

\[
2(2\tau)^{-1}(1-\tau^2)v_2v_0^T
 \sum_i\mu_i r_i^*s_i=0.
\]

For the row block the actual adjoint coefficient satisfies, uniformly for large `R`,

\[
\|q_i\|_\infty
\le B_1\|M_*\|_F B_2|c_R|.
\]

The residuals and `c_R` are bounded, so the row gradient norm is at most a fixed constant times `max_i sech^2(R v dot u_i)`, which tends to zero. Hence the **entire** gradient tends to zero in the required `L2/L2/Frobenius` metric. All factors of two and probability weights agree with (H3.N2) and (H40.C6); no extra neuron weights belong in these gradient fields.

## 3. Fixed and uniformly bounded proposals

For each fixed Hilbert increment `h`, its lower field is finite almost everywhere. Since every `v dot u_i` is nonzero, dominated convergence gives `a_i(w_R+h_w)->s_i v_0`. Bounded upper marks then give uniform essential convergence of the upper features to `s_i H_h`. Pairing with `c_R+h_c`, which converges in `L2`, proves

\[
L(S_R+h)\longrightarrow
1-t_h+t_h^2=3/4+(t_h-1/2)^2.
\]

This is a statement for each fixed increment, not a uniform assertion over an unbounded increment set. It nonetheless proves the claimed probability statements for **each fixed law** on Hilbert-valued increments. For any fixed `delta>0`, the fixed-gain indicator tends pointwise to zero. The accepted gain tends pointwise to zero and is bounded by `L(S_R)<1`. Bounded convergence therefore proves both (12) and (13), including for the Gaussian law conditioned on a fixed positive-radius ball. No covariance-basis assumption, uniform lower Gaussian density, or exchange of a supremum with this limit is used.

The separate bounded-ball argument is also correct. If `||h||<=epsilon`, the exceptional lower-carrier set `|h_w|>R alpha/2` has probability at most `4 epsilon^2/(R^2 alpha^2)`. On its complement the projection retains its sign and has magnitude at least `R alpha/2`, giving a tanh error at most `2 exp(-R alpha)`. Multiplying by bounded marks and bounding the exceptional error by two proves exactly (14).

For completeness, the uniform loss comparison can use the **current** comparison scalar

\[
t_{R,h}=E_2[(c_R+h_c)
 \tanh(b_2^T(M_*+h_M)v_0)].
\]

Writing the lower-coefficient error bound in (14) as `e_R`, each prediction differs from `s_i t_{R,h}` by at most

\[
(|c_R|+\epsilon)B_2(\|M_*\|_F+\epsilon)e_R.
\]

The comparison scalar and all actual predictions are uniformly bounded for large `R`. Squared-loss subtraction therefore gives `L(S_R+h)>=3/4-C_epsilon e_R`, because the comparison loss is at least `3/4` for every scalar. This establishes (15) without inserting the slower convergence rate of `c_R` into the error term.

These conclusions exclude a state-uniform positive fixed gain or fixed-gain probability. They do not exclude accumulation of infinitely many shrinking gains along a realized process.

## 4. Finite-observation boundary

For every finite `L2` field, `|tanh(w dot u_i)|<1` almost surely. Its nonnegative deficit from one is strictly positive almost surely, so

\[
|E_1\tanh(w\cdot u_i)|
\le E_1|\tanh(w\cdot u_i)|<1.
\]

Thus the limiting first lower-feature coordinate `s_i beta_1` cannot be realized by any such field. The convergence of the finite coefficient vectors, predictions, matrix, and constant readout does not produce a genuine state with these limiting observations. This verifies the claimed failure of that particular observation-compactness argument and the inapplicability of the local escape theorem at the added boundary. It does not rule out a different argument formulated directly on a compactified space and equipped with appropriate boundary dynamics.

## 5. Conditional Gram theorem and stochastic quantifiers

Set `v_i=sqrt(mu_i) r_i`. Then `L=|v|^2`, and direct expansion gives

\[
\|g_c\|_2^2=4v^T\widetilde K v
\ge4\kappa_0L,\qquad \|g_c\|_2\le2\sqrt{L_0}.
\]

With `w,M` fixed, the prediction is linear in `c`. The exact quadratic loss identity has linear term `-t||g_c||_2^2`, while its quadratic term is at most `t^2||g_c||_2^2`. For `t<=1/2` this proves (19), including its stated decrease `2t kappa_0 ell`.

The uniform-neighborhood argument hides no bound on `w`: tanh is globally Lipschitz, the lower coefficients are uniformly bounded, and the upper preactivations depend on their finite vectors through bounded marks. Target readout norms are bounded by `C+sqrt(L_0)`. The displayed difference estimates consequently give a common loss Lipschitz constant around all target states. A sufficiently small common `r_0` leaves a loss decrease of at least `delta=t kappa_0 ell`.

The compactness step applies to the **increments**, which have only a readout component. Each feature is `tanh(b_2^T z_i)` with `|z_i|<=M_0B_1`; the residual coefficients range over a bounded finite-dimensional box. The continuous image of the compact product parameter set contains all target gradients. Their closure is therefore compact in the upper `L2` space. A finite covering and full support give the claimed common `q>0`. For the conditioned law, `||-t g_c||<=epsilon/2` and `r_0<epsilon/4` keep all smaller witness balls inside the conditioning ball. Dependence of `q` on the particular fixed proposal law is permitted and necessary.

The almost-sure consequence has the correct quantifiers. At proposal time `k`, let `A_k` be the past-measurable event that the fixed bounds (17) hold, and `B_k` the event of a decrease at least `delta`. Fresh noise gives

\[
P(B_k\mid\mathcal F_k)\ge q\quad\hbox{on }A_k.
\]

Loss monotonicity and nonnegativity bound the total number of such successes by the initial loss divided by `delta`. Consequently, by conditional expectation and monotone summation,

\[
q\,E\sum_k1_{A_k}
\le E\sum_k1_{A_k}1_{B_k}
\le L(S_0)/\delta<\infty.
\]

There are therefore only finitely many visits to each fixed region (17), almost surely. Countably many integer norm bounds and reciprocal-integer positive bounds for the Gram and limiting loss yield the stated conditional consequence. More precisely, the event that `c,M` stay bounded, the weighted Gram has a positive uniform lower bound, and `L_infinity>0` has probability zero. Exact intervening gradient flow preserves the needed monotonicity. No independence of the proposal-time states themselves is assumed.

The duplicate/antipodal reduction must refer to fixed exact output constraints with compatible labels, as the text specifies. It does not authorize discarding state-dependent small eigenvalues. In the explicit obstruction the Gram has rank one at every `R`, so the positive-Gram hypothesis really fails even though all matrix/readout bounds hold.

## Required changes and remaining scope

No mathematical correction is required for the audited claims. When quoting the noncoercivity conclusion, retain the demonstrated range of fixed sublevels above `3/4`; when quoting the stochastic conclusion, retain the matrix/readout and uniform-Gram hypotheses. The original almost-sure zero-loss convergence claim remains open on the supplied evidence because no argument establishes these hypotheses, excludes saturation along reached states, or constructs a positive-probability trajectory following the obstruction.
