# Independent review of the nonlinear rank-one obstruction

Review date: 2026-09-18. Verdict: **PASS for the static counterexample and
both variants.** No mathematical gap was found in the construction. This is
an internal mathematical check, not promotion or a claim about initialized
trajectory reachability.

The frozen candidate reviewed was `rank_one_nonlinear_obstruction.md`, SHA-256
`07b481e396584ebbcfb30b155b157778179a6c11c929a85376e94e31d072784c`.
The permitted scientific inputs read were all of `docs/observable_p1.md`,
the state/equation/existence sections C.4.7.9.3–4 and C.4.7.10.D.3 of
`docs/global_nonlinear.md`, and this study's complete
`architectural_loss_floor.md` and `plateau_finite_critical.md`. Following
explicit supplemental input authorization, the complete own-study
`initialization_positivity.md` was also read. Required
research and rigorous-math skills and the research-contract/adversarial-audit
references were read. No study history, other route report, prior review,
or numerical result was used. No numerical experiment was run.

## 1. Exact marks and admissible state

The canonical upper coordinates are independent copies of
`tanh(sqrt(v) Z)/sqrt(tau+eta)`. They are centered, bounded, and have strictly
positive densities throughout their common open support interval. In
particular, each has positive variance. They have not been replaced by
arbitrary symmetric features.

For each lower coordinate pair, the map from `(G,Z)` to
`(tanh G,tanh(sqrt(tau) Z+alpha tanh G))` is a smooth bijection onto
`(-1,1)^2`, with nonzero Jacobian everywhere. Independent coordinate pairs
therefore give a positive density on `(-1,1)^6`. The invertible prescribed
Cholesky normalization preserves absolute continuity and yields positive
density on a full-dimensional open set. Consequently the lower uncentered
Gram is positive definite. This reasoning preserves the full joint law
with `g`; it does not assume `g` and `b_1` are independent.

The candidate's fields satisfy the exact finite-state requirements:
`w-g` and `c` are bounded measurable fields, `M` is finite, and `w,c` are
odd under their respective simultaneous mark negations. Restoring the
inactive constant feature gives zero lower constant contraction and zero
upper constant backward contraction. Hence the omitted row and column of
the full matrix gradient also vanish. The construction is stationary in
the full equations, not merely after projecting their gradient onto the
odd coordinates.

## 2. Simultaneous moment realizability

Positive definiteness of the lower Gram implies
`E|b_1 dot v|>0` for every nonzero `v`. Boundedness of `b_1` makes this
expectation continuous on the unit sphere, so the candidate's `m_0` is
strictly positive.

Both derivatives of `F_i` are justified by uniform bounds on `b_1`, tanh,
and its derivative. For every nonzero `z` and finite `theta`,

\[
 z^T\nabla^2F_i(\theta)z
 =E[(z\cdot b_1)^2\operatorname{sech}^2(g\cdot u_i+b_1\cdot\theta)]>0.
\]

The gate is strictly positive almost surely; the Gram supplies a
positive-probability set on which the square is positive. The lower bound
in candidate equation (6) follows from
`log cosh(t)>=|t|-log 2` and the triangle inequality. It proves coercivity
for every target strictly inside the stated common ball. Continuity gives
existence of a minimizer, strict convexity gives uniqueness, and its
first-order equation gives the required moment exactly.

For independent inputs the dual vectors in equation (7) exist. Taking the
dot product with each input isolates its own minimizer, so all three
moments are realized simultaneously. Explicitly,

\[
 \|w-g\|_\infty
 \le \|b_1\|_\infty\sum_i |t_i|\,|\theta_i(A_i)|<\infty.
\]

No uniform bound as the inputs approach linear dependence is claimed or
needed. Global negation sends both terms defining `w` to their negatives.
This part of the proof closes the potential objection that the forward
vectors were assigned freely without a realizable lower field.

## 3. Upper construction, all gradients, and loss

The functions `H=tanh(B_1)` and `J=B_1 sech^2(B_1)` are not proportional:
their ratio off zero is `sinh(2z)/(2z)`, which is not constant on the
support interval. Positive density and continuity upgrade an almost-sure
proportionality to an interval identity, a contradiction. Thus the
orthogonal residual `U` has positive squared norm, and
`E[UH]=E[U^2]=s^2>0` while `E[UJ]=0`.

For `c=mU/s^2+B_2`, independence gives `E[cH]=m`. Directly computing all
three backward coordinates gives

\[
 d_1=0,\qquad d_2=E[B_2^2]E[\operatorname{sech}^2(B_1)]>0,
 \qquad d_3=0.
\]

Evenness of the upper gate makes this same vector apply to all three
inputs. Since `M` has only its first row nonzero, `M^T d=0` despite
`d!=0`.

At least one positive probability weight is less than `1/2`. The chosen
index gives `0<m=1-2p_k<1` for every binary labeling. With
`rho_i=p_i r_i`, the three nonzero coefficients are exactly

\[
 \rho_i\sigma_i=-2p_ip_k\quad(i\ne k),\qquad
 \rho_k\sigma_k=2p_k(1-p_k).
\]

Their sum is zero. Thus every individual weighted middle matrix is the
nonzero rank-one matrix `(rho_i sigma_i) d a^T`, and their sum is zero.
The same scalar identity annihilates the complete readout velocity.
The lower velocity vanishes pointwise because `M^T d=0`. The full physical
metric and the factor two from the unhalved loss agree with the canonical
equations.

All residuals are nonzero, and direct expansion gives
`L=1-m^2=4p_k(1-p_k)` strictly between zero and one. The candidate's
balanced numerical example and its three matrix coefficients are also
algebraically correct; evaluating them does not require numerical
integration.

## 4. Architectural compatibility and negative curvature

The zero architectural minimum can be checked without any initialization
separation theorem. Choose `0<kappa<m_0`, realize
`A_i=kappa e_i` in the lower six-dimensional space using the proved moment
lemma, and take `M=kappa^{-1}[I_3 0]`. Then the three upper features are
`tanh(B_i)`. They are independent, centered, and have positive variance,
so the bounded odd readout

\[
 c=\sum_{i=1}^3
 \frac{y_i\tanh(B_i)}{E[\tanh^2(B_i)]}
\]

fits all three labels exactly. This establishes the comparison with zero
loss in the unchanged architecture for every independent input triple.

There is also a direct strict-saddle check for the candidate's constructed
state. Fix any index `j`, let

\[
 K_j=E[b_1b_1^T\operatorname{sech}^2(w\cdot u_j)],
 \qquad v=t_j(b_1\cdot K_j^{-1}a).
\]

The same positive-definiteness argument makes `K_j` invertible. The
bounded odd lower perturbation `v` gives `delta a_j=a` and
`delta a_i=0` for `i!=j`, hence `delta H_j=J`. Put

\[
 k=J-\frac{E[JH]}{E[H^2]}H.
\]

Then `k` is bounded, odd, nonzero, and perpendicular to every current
upper feature. Its pure readout second loss variation is zero. If `Q`
denotes the second variation of the unhalved loss, its mixed derivative
therefore gives

\[
 Q[(v,s k,0)]
 =Q[(v,0,0)]+4s\rho_j\|k\|_2^2.
\]

All coefficients are finite, and `rho_j!=0`, so a finite choice of `s`
makes this negative. This independently verifies the strict-saddle
description, and agrees with the nonzero-middle theorem in the assigned
`plateau_finite_critical.md`.

The stronger assertion that the *canonical initialized hidden features
themselves* can fit the data also checks out. The subsequently authorized
`initialization_positivity.md` retains the actual ridge and correlated
reverse response. Its Gaussian integration-by-parts/Cauchy–Schwarz bound
gives `b^2>=tau gamma^2+eta`, hence `0<B_*<=1/gamma`. The lower bound on
the conditional tanh coefficient, together with its explicit bounds on
`nu` and `alpha`, yields the positive rational constant
`7/15-1936/4725-1/65=2552/61425`. The inequality directions are correct,
including multiplication by the negative quantity `m-alpha` in that
source's proof. Thus its odd coefficient `Psi(h)` has the sign of `h`.

With this input, equation (1) of `architectural_loss_floor.md` makes the
coordinate map `T` strictly increasing: the relevant shifted-Gaussian
expectation of `tanh(z) sech^2(z)` is positive by pairing its positive
and negative arguments. The integrable derivative bound and endpoint
dominated convergence justify differentiation and extension to the
closed interval. Therefore the initialized effective vectors distinguish
inputs modulo sign. The upper positive-density argument and the first
three nonzero odd Taylor coefficients of tanh give the stated invertible
Vandermonde system. Its positive-definite feature Gram then supplies a
bounded odd fitting readout at `w=g,M=D`. There is no remaining missing
scientific dependency for this ancillary claim within the reviewed chain.

## 5. Full-row-rank and near-critical variants

Two independent rows perpendicular to `a` exist because its orthogonal
complement has dimension five. Adding them leaves `Ma_i=sigma_i e_1`
unchanged and gives full row rank. Removing `B_2` from the readout makes
all three backward coordinates zero, so every full gradient vanishes
at the same positive loss. This does not falsely assert nonzero middle
contributions in this variant.

For the near-critical variant, retaining `B_2` and scaling the added rows
by `epsilon>0` preserves all predictions, backward vectors, and middle
contributions. The middle and readout gradients remain exactly zero,
while `M_epsilon^T d=epsilon delta n_2`. In particular,

\[
 \|w'_\epsilon\|_\infty
 \le 2\epsilon\delta\|b_1\|_\infty |n_2|
       \sum_i p_i|r_i|.
\]

This also bounds the physical population `L2` norm. The coefficient field
is not identically zero: independent inputs separate its nonzero
residual/gate coefficients, and `b_1 dot n_2` is nonzero almost surely by
absolute continuity. Thus this is a full-row-rank near-critical family,
not an overlooked additional stationary family with nonzero `d`.

## 6. Logical scope

The universal quantifiers are satisfied for arbitrary independent sphere
triples, positive probability weights, and binary labels. No coincidences,
antipodes, special orientation, modified feature law, or frozen trained
block are required. The counterexample defeats the static implication
from the stated cancellations to architectural input conflict.

It does not show that canonical initialized training reaches, approaches,
or escapes toward any constructed state. Bounded finite-state
realizability is not reachability, and negative curvature does not exclude
a fixed deterministic initialization from a saddle's stable set. The
candidate repeatedly preserves these distinctions. The initialized
plateau question therefore remains open exactly as stated.

## Separately scoped follow-up: nonlinear rank extensions

Follow-up verdict, 2026-09-18: **PASS.** This addendum was checked only
after completion of the original isolated review above. The new permitted
inputs were the complete frozen files:

* `rank_one_nonlinear_extensions.md`, SHA-256
  `e9c9c12a47f3a053e69216573b3d83165e393f300e510f5b6a480d722d2dc71c`;
* its declared algebraic source `rank_one_algebra_extensions.md`, SHA-256
  `df35ce798e5488af31127192e338e786aca10192204d6ded2113b834aa0f1ee5`.

The previous allowed scientific inputs and the already reviewed moment
lemma were retained. Neither new candidate was edited. No further source
or numerical result was used, and the original candidate and its review
verdict are unchanged.

For the rank-two construction, the prescribed moment norms are
`sqrt(2)t,sqrt(2)t,sqrt(5)t`, all strictly below `m_0` under its stated
bound. Thus the previously checked convex argument supplies a single
actual finite odd lower field realizing all three moments on the
unchanged correlated marks. The first two columns of the lower
contraction matrix are independent, all three belong to the same
two-dimensional span, and `2a_3=3a_1+a_2`. Its rank is therefore exactly
two. The middle matrix has independent nonzero `e_1` and `e_3` rows,
also has rank two, sends the contractions to `(-e_1,e_1,-e_1)`, and
annihilates `e_2` under its transpose.

The readout calculation supplies the derivative vectors, rather than
stipulating them: `c=U/(2s^2)+B_2` gives `d_i=delta e_2!=0`, predictions
`(-1/2,1/2,-1/2)`, and residual weights `(-3/8,-1/8,1/4)`. Their signed
sum is zero, giving readout stationarity. Their moment-weighted sum is
`(-3a_1-a_2+2a_3)/8=0`, giving middle stationarity with three nonzero
rank-one summands. The lower velocity vanishes pointwise because
`M^T d_i=0`. Since the right factors span two dimensions, this is an
exact nonlinear example of the common-left-factor branch without common
right factors. The loss is exactly `3/4`.

For the full-rank construction, every prescribed moment has norm
`sqrt(2)t<m_0`, so the same realizability lemma applies. The distinct
`f_4,f_5,f_6` coordinates prove independence of the three lower
contractions, and the middle matrix has row rank three. Their product
still gives `(-e_1,e_1,-e_1)` because those distinct coordinates lie in
the middle matrix's kernel. There is no rank contradiction: restriction
of a full-row-rank map to this particular three-dimensional subspace
need not be injective. For `c=U/(2s^2)`, orthogonality to `J` annihilates
the first backward coordinate, while independence and centering
annihilate the other two. Hence every `d_i=0` exactly, all middle and
lower contributions vanish individually, and the unchanged signed
feature relation gives readout stationarity and loss `3/4`.

Replacing `B_2` by `tanh(B_2)` in the nonzero-derivative constructions
preserves oddness and centering. The predictions and the first and third
backward coordinates are unchanged, while the second becomes
`E[B_2 tanh(B_2)] E[sech^2(B_1)]>0`. Both factors are strictly positive
under the canonical nondegenerate upper law. This replacement also
makes the displayed readout formula bounded on all of `R^3`: tanh is
bounded, and `z sech^2(z)` is continuous and tends to zero at both
infinities. The original formula already met the required boundedness
on the canonical carrier.

The zero-loss comparison follows from the moment lemma and the diagonal
positive feature Gram, as in the original review. The strict-saddle
description meets the previously checked theorem's hypotheses: the
inputs are distinct modulo sign, the states are finite, the loss is
positive, and `M!=0`. Each construction works for every independent
input triple with its stated fixed weights and labels. Matrix norms may
grow as the auxiliary scale tends to zero; no uniform bound is asserted.
These remain ambient stationary-state counterexamples, with no claim of
reachability or convergence from the prescribed initialization. No
mathematical gap was found in any of the three extensions.
