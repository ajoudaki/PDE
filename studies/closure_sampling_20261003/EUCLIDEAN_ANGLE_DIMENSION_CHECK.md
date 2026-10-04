# Internal reconstruction of the Euclidean angular refinement

2026-10-04. **PASS for the stated refinement relative to its inherited
source and runtime interfaces.** No required correction was found in the
frozen candidate. This is an internal cross-check, not a fresh promotion
review or a proof-assistant verification.

Candidate checked completely:
`EUCLIDEAN_ANGLE_DIMENSION_ROUTE.md`,
SHA-256
`9f452338619a0c7334bae8944454f71309f2314a65c844f84150b947ba41c9d7`.
The candidate hash was verified before and after the reconstruction.
The result checked is the removal of the persistent $(d+3)^d$ factor
from the preceding simple storage bound, with the same
$\beta^{84Ld}$ coefficient, $\log(en)^{3d+2}$ power, label condition,
reference dynamics, and all-time whole-sphere error.

## 1. Assignment, isolation, and exact read scope

The supervisor requested independent reconstruction of the frozen candidate,
especially the fixed-direction insertion extension, complex angular frame,
stopping/net proof, and exact exponent absorption. Only this report was
written. No candidate, dependency, other route, maintained document, or Git
state was edited. No experiment or training computation was performed.

I authored the separately frozen `DIMENSION_ALTERNATIVE_ROUTE.md` before
this assignment. Its generic-analytic obstructions and exact finite count
were not used as premises here. I did not author or assemble the candidate
under review and did not see another review of it. The supervisor's candidate
was supplied after my route had frozen. This disclosure rules out treating
the present check as a fresh isolated promotion review.

The following files were read completely; truncated combined output from
the deep-source read was repaired by reading its complete insertion section
again. Earlier complete reads of the unchanged source-count and architecture
files in this same scoped session were reused.

| File | SHA-256 |
| --- | --- |
| `EUCLIDEAN_ANGLE_DIMENSION_ROUTE.md` | `9f452338619a0c7334bae8944454f71309f2314a65c844f84150b947ba41c9d7` |
| `EXPLICIT_SOURCE_CONSTANTS_ROUTE.md` | `d4a1bf4bd247d1b93909d4ee001da74c4c6f4573021370800f9c152dae05ab6a` |
| `DEPTH_INDEPENDENT_EXPONENT.md` | `73c12dafdd05dcae7f287b2ccc49cc237a540ef7b2f26d53204c96bcd9feceda` |
| `LABEL_DEPTH_RESCALING_ROUTE.md` | `d06ceea6598bf3f86e0843682c5600365ef01b4b80eaad6544ceec1a9d4ec1f1` |
| `DIMENSION_PREFACTOR_OPTIMIZATION.md` | `8e149122bcd83a8f64bceba97a6617f644f10e59fd97456f3cfa0e10273c8f2e` |
| `DEPTH_CONSTANT_SEPARATION.md` | `6e23f2eb95b1979e7be722f76bafb43ee239f83cc5175d58d17a0f9e73fcb17f` |
| `ARCHITECTURE_CONSTANT_REFINEMENT.md` | `b33f8b2ebb04eba386f59f125fd4d8f22ff3273bc094f64808db865dd27caba7` |
| `DEEP_COMPLEX_SOURCE.md` | `7a81a04bb3e52a1c60ee83f479238ea1dec54fe2b70277b4f7d513b5eb84c6f2` |
| `DEEP_ACTIVATION_EXTENSION.md` | `b5279562acc5d8ffceaad2d8ac744d43e51c4af91d0508e66804ab12954ef141` |
| `STORAGE_QUADRATIC_IMPROVEMENT.md` | `ec18f54a3e3977bf9c99ce5c26066f48688848f8b5a9c142b75424badeb025e2` |
| `GENERAL_ANALYTIC_COMPRESSION.md` | `4fd314dd28367430cd60fa8b88fe0eb4d9b12f575c61aadd60ff61dff76dec53` |

My previously authored alternative-route freeze is
`826fe412f8247ab6be9f1c26099e75b25f0ef02ff62dabd29ec13f140ca62e05`.
Required canonical-notation, neural-response-memory, rigorous-proof, and
research-contract/audit instructions and the shared workflow were applied.

The prior-study insertion theorems mentioned by the current-study sources
were outside this assignment's permitted scientific inputs and were not
opened. Their specified local Gaussian insertion interface remains inherited,
as it does in the candidate. This report reconstructs the new directional
extension from the complete current-study augmented graph and source
arguments. It does not claim a new audit of the prior-study theorem, the
spectral sparsification theorem, or the entire original runtime proof.

## 2. Complex angular geometry

Write $D=d-1$. The recursion
$v_d=(\cos\theta_1,\sin\theta_1v_{d-1})$ has the frame

\[
 w_1=(-\sin\theta_1,\cos\theta_1v_{d-1}),\qquad
 w_j=(0,w'_{j-1})\quad(2\le j\le D),
\]

where the primed columns form the lower-dimensional frame. Multiplying
the block frame $\operatorname{diag}(1,Q_{d-1})$ by the first-coordinate
plane rotation gives $Q_d=[v_d,w_1,\ldots,w_D]$. Iteration is a product
of $D$ complex plane rotations.

For a rotation through $x+iy$, its Hermitian singular values are
$e^{|y|}$ and $e^{-|y|}$: the real rotation is unitary and the purely
imaginary rotation is diagonalized by the fixed complex eigenvectors of
the real skew rotation generator. Thus

\[
 \|Q_d\|_{\rm op}\le e^{\sum_j|\Im\theta_j|}.
\]

Differentiating the recursion, with the above columns, gives exactly

\[
 D_\theta v_d=[w_1,\ldots,w_D]\,
 \operatorname{diag}(1,\sin\theta_1,
             \sin\theta_1\sin\theta_2,\ldots).
\]

Every product on the diagonal has magnitude at most
$e^{\sum_j|\Im\theta_j|}$, since $|\sin(x+iy)|\le e^{|y|}$.
Consequently

\[
 \|D_\theta v_d\|_{\rm op}\le e^{2\sum_j|\Im\theta_j|}
 \le e^{1/4}<2.
\]

For $\theta=\theta_R+ib$, its straight imaginary path therefore has input
length at most $2\|b\|_2$. This proves candidate equations (5)--(6).
No unitary claim for a complex orthogonal frame, and no componentwise
triangle inequality, is needed. The formula remains valid at the real
coordinate singularities where one or more sine factors vanish.

## 3. Fixed complex input directions: recurrences and insertion

For a deterministic $u\in\mathbb C^d$ with $\|u\|_2=1$, set
$J_u^{(\ell)}=D_vz^{(\ell)}[u]$ and
$q_u^{(\ell)}=D_vh^{(\ell)}[u]$. These are derivatives of the passive
query map at the current parameters, with $u$ held fixed; they are not
additional dynamical coordinates or training forces.

On the pole-safe tube the exact equations are

\[
 J_u^{(1)}=Au,\qquad
 J_u^{(\ell)}=W^{(\ell)}q_u^{(\ell-1)},\qquad
 q_u^{(\ell)}=\phi_\ell'(z^{(\ell)})\odot J_u^{(\ell)}.
\]

The normalized first-layer RMS is at most ten from
$\|A\|_{\rm op}/\sqrt n\le10$. The old angular bound starts at twenty,
because it allowed input derivatives of norm two. Its recurrence
$j_\ell=20(10s)^{\ell-1}$ therefore bounds the new one without change.

For clarity, the exact parameter derivative in a mobility-coordinate
direction $U=(U_A,U_{H^{(2)}},\ldots,U_w)$ is

\[
 D_\Theta q_u^{(\ell)}[U]
 =\operatorname{diag}(\phi_\ell''J_u^{(\ell)})
                  D_\Theta z^{(\ell)}[U]
  +\operatorname{diag}(\phi_\ell')
                  D_\Theta J_u^{(\ell)}[U],
\]
\[
 D_\Theta J_u^{(1)}[U]=U_Au,\qquad
 D_\Theta J_u^{(\ell)}[U]
 =\frac{U_{H^{(\ell)}}}{\sqrt n}q_u^{(\ell-1)}
       +W^{(\ell)}D_\Theta q_u^{(\ell-1)}[U].
\]

If each row of $D_\Theta z^{(\ell)}$ has norm at most $P_\ell$,
the first map has normalized Hilbert--Schmidt norm at most
$t_\phi j_\ell P_\ell$. For the second line, summing images of matrix
coordinate basis elements gives

\[
 \left\|U_H\longmapsto U_Hq/\sqrt n\right\|_{2,n}
 =\|q\|_{2,n},\qquad
 \left\|U_A\longmapsto U_Au\right\|_{2,n}=\|u\|_2=1.
\]

Thus the candidate's unchanged $a_\ell$ recurrence, $E_J$, and
$T_J=8f_*E_J$ are justified. In particular there is no factor $\sqrt d$
in this endpoint bound. The rescaled budget's trace summability conditions
are exactly those verified in `LABEL_DEPTH_RESCALING_ROUTE.md`,
equations (24) and (29); none becomes stronger after this substitution.

I checked the deletion interface against the complete augmented graph,
not just these RMS bounds. For deletion below a passive observable, the
new direct source is the initialized outgoing root times the deleted
$q_{u,i}^{(\ell)}$. There is no normalized feature-pairing term, exactly
as for the original angular observable in
`DEEP_ACTIVATION_EXTENSION.md`, equation (14). For deletion above
the observable, its dependence is through the retained parameter state;
there is no direct reverse observable term because $q_u$ contains no
training gradient. The ordinary reverse training force still contributes
the same endpoint trace through $D_\Theta q_u$.

The primitive graph has the same gate, coordinate-product, matrix-action,
and normalized-pairing rules. At its first layer the only new primitive
is the linear map $A\mapsto Au$, of coefficient norm one. If the direction
is held fixed when differentiating in query angle, the graph lacks the
additional derivative of the original $\partial_{\theta_j}v$ coefficient.
All required time/angular derivatives have the same or fewer terms and
the same $\sqrt n$ times fixed-polylogarithmic bound.

Consequently the current-study augmented-graph lemma applies with unchanged
negative powers. Its Euclidean remainder terms are still
$n^{-0.09}$, $n^{-0.08}$, $n^{-0.48}$ and the corresponding mixed
terms before logarithms; the variational factor is at most $n^{0.001}$.
At the $n^{-0.04}$ first-hit cap each is strictly smaller. First variations
and the forward applications of independent incoming-row probes are still
linear maps of the omitted roots conditional on retained initialization
and deterministic controls. Uniform control selection occurs before actual
root-dependent scalar controls are substituted.

The Gaussian centered term has RMS coefficient at most $b_{\ell-1}$;
the same-root term is at most $SsM_nT_J$; and the learned-row term is
at most $SsM_nBb_{\ell-1}$. These are precisely the terms already in
the reconciled $V_\ell$ recurrence. At layer one, $A_0u$ has real and
imaginary Gaussian variances at most one, and the learned-row contribution
is at most $SsM_n$. Thus the old $V_1$ also suffices.

These checks establish the claimed extension from the inherited local
insertion interface. They do not replace that interface by an unjustified
Gaussian assertion about a full adaptive source.

## 4. Uniformity over directions and removal of stops

A maximal set with pairwise distances greater than $1/2$ on the complex
unit sphere is a $1/2$-net. Disjoint real $2d$-dimensional balls of radius
$1/4$ around its points lie in the ball of radius $5/4$, so its size is
at most $5^{2d}$. Since $5^{2d}\le n^d$ for $n\ge25$, adjoining it to
the old query/time Gaussian mesh gives at most $n^{5d+3}$ entries
eventually. With $G_d=8\sqrt{d+3}$ the complex Gaussian tail bound is

\[
 4e^{-G_d^2\ell_n/4}
       =4e^{-16(d+3)\ell_n}.
\]

The resulting union probability is bounded by
$4n^{5d+3}e^{-16(d+3)\ell_n}\to0$. The surplus exponent
$11d+45$ leaves room for the inherited fixed layer/sample and mesh
prefactors. The insertion control event has the stronger exponential
scale stated in the current-study source; a fixed $5^{2d}$ multiplicity
also leaves its entropy comparison unchanged.

For every scalar complex-linear functional $T$,
$\|T\|\le2\max_{u\in\mathcal N}|Tu|$ follows by approximating a
maximizing unit vector by the net and bounding the error by
$\|T\|/2$. Applying this pointwise after the net event proves the
candidate's uniform $2V_*\sqrt{\ell_n}$ bound. This order is essential:
the direction along the angular path may depend on the query, but the
bound already holds for every complex direction.

Add only the finite net-direction response caps to the stopped proof.
Their coordinate-small cavity differences transfer them to doubled
cavity caps. They have no effect on the actual training equation, on the
samplewise carrier budget, or on the normalized activity and Hessian
propagator. The upward trace induction uses lower query gates and responses
only. Hence it improves the directional caps before the next pole exclusion,
as required to avoid circularity.

For the proposed $c_a$, every path point satisfies
$\sum_j|\Im\theta_j|\le(d-1)c_a/\sqrt{\ell_n}<1/8$.
The angular preactivation displacement is at most

\[
 (2V_*\sqrt{\ell_n})(2\|b\|_2)
 \le4V_*\sqrt{d-1}\,c_a\le a/128.
\]

The exact time response identity and complex residual bound $2Y$ give
$|\partial_tz|\le4YSU_*\sqrt{\ell_n}$. Both the short real excursion
and vertical segment together have length at most $2r_t$, so their
displacement is at most $8c_tYSU_*\le a/64$. The total is $3a/128$,
with a strict strip margin.

The carrier correction is still solely a time-domain calculation.
The rescaled-budget proof bounds its radius by a fixed multiple of
$r_t[1+(S^2/\eta)\log(e+\ell_n)]$ and its Gaussian mean by
$O(\ell_n^{-1/2}\log(e+\ell_n)^{3/2})$. Both vanish at fixed parameters.
Changing the angular radius does not enter that calculation. Thus the
order remains local transfer, carrier maximum, query responses, query
poles, complex moment, and then carrier budgets. There is no added
nonvanishing label or variational constraint.

## 5. Radii, source construction, and explicit storage arithmetic

The nongeometric angular reciprocal is

\[
 \frac{512\sqrt{d-1}V_*}{a}
 \le32\beta^{30L+1}\sqrt{(d-1)(d+3)}
 \le\beta^{32L}(d+3).
\]

The geometric branch $8d$ satisfies the same bound. Similarly
$c_t^{-1}\le\beta^{32L}\sqrt{d+3}$, including its branch eight.
This gives

\[
 c_t^{-1}c_a^{-(d-1)}
 \le\beta^{32Ld}(d+3)^{d-1/2}.
\]

I reconstructed the inherited Fourier interface in full:

* the cosine time map at
  $\alpha=c_t\lambda/(128\ell_n^{3/2})$ remains in the time rectangle;
* contour translation yields the weighted coefficient decay;
* the outside weighted-degree sum is at most $\epsilon/16$;
* disjoint nonnegative lattice cubes and angular sign choices yield the
  factor $2^{d-1}/d!$;
* the explicit logarithm defining $H$ retains all radius and dimension
  constants before its eventual bound $H\le7\ell_n$;
* the tensor-grid aliasing estimate bounds the omitted tail;
* finite initialized jets produce the nodal values, and identical scalar
  linear operations preserve each initialized matrix-image pair exactly.

No original-width coefficient array or interpolation table is retained
by the runtime. The changed radius requires no new source family.
The same four whole-query families, initialization additions, and two-point
$d=1$ handling therefore give the candidate's rank bound.

Here is explicit arithmetic for the additions that are abbreviated in the
candidate. Put $F_d=(d+3)^{d-1/2}/d!$. The arithmetic-geometric mean
bound $d!\le((d+1)/2)^d$ gives
$F_d\ge2^d/\sqrt{d+3}\ge1$. Also
$m\lambda\le B^2$ and $d\le\beta^{Ld}$.
The coefficient of the Fourier part in $8N$ satisfies

\[
 512\,18^d\le9216^d\le\beta^{2Ld},
\]

because $\beta\ge10$ and $L\ge2$. Its rank contribution is at most
$\beta^{34Ld}F_d\lambda^{-1}\ell_n^{3d/2+1}$.
The initialized additions satisfy

\[
 2m+d+1
 \le(2B^2+d+1)\lambda^{-1}\ell_n^{3d/2+1}
 \le\beta^{2Ld}F_d\lambda^{-1}\ell_n^{3d/2+1}.
\]

For the last inequality, $B^2\le\beta^{Ld}$ and
$2B^2+d+1\le4\beta^{Ld}\le\beta^{2Ld}$.
Adding these terms gives the stated $\beta^{36Ld}$ bound with slack.
The same right-hand side separately dominates $d$ and $m$, so replacing
$R$ by $R_0=\max(R,d,m)$ preserves it. This explicitly covers the
first-weight and sample-rank requirements.

The full inventory is still
$1020(L+1)R_0^2+10m(d+1)$. Since
$\lambda^{-2}\le B^4(m/\gamma)^2$ and
$1020(L+1)B^4\le\beta^{10Ld}$, squaring gives exactly the candidate's
coefficient $\beta^{82Ld}$ and factorial expression
$(d+3)^{2d-1}/(d!)^2$.

Finally,

\[
 F_d\le e^{d+3}/\sqrt{d+3}\le e^{4d}\le\beta^{Ld}
\]

for every $d\ge1$, $L\ge2$, $\beta\ge10$. Therefore
$F_d^2\le\beta^{2Ld}$ yields $\beta^{84Ld}$ with no remaining
power $d^d$. The $d=1$ estimate already includes both sphere points;
no nonexistent angular integration or missing sign factor is used.

## 6. Runtime transfer, verdict, and limits

Only the source geometry changed. Its runtime inputs still have coordinate
accuracy $n^{-1}$, exact paired initialized forward and transpose actions,
exact initial training features, and the same training-carrier coefficient.
The real reference and every reduced runtime equation are untouched.
The initialized mixer contraction, fixed metrics, learned matrices,
corrected readout, moving own residual, and all solve/data caches are
counted by the unchanged inventory.

The label condition implies
$Y/\lambda\le B^2\beta^{-62L}\le\beta^{-60L}$, which is smaller than
the source requirement $\beta^{-32L}$ and meets the refined runtime
condition. Its all-time comparison and independent exponential fitting
tails therefore apply with the same physical horizon
$32\lambda^{-1}\ell_n$. Their conversion
$\lambda^{-3/2}\le B^3(m/\gamma)^{3/2}$ gives the unchanged error
$\beta^{124L}Y(m/\gamma)^{3/2}/\sqrt n$. The endpoint is included by
the same sphere-uniform tail; no trajectory playback or frozen endpoint
is introduced. Zero labels retain the exact stationary zero predictor.

**Verdict:** the candidate's new implication passes this internal
reconstruction. The extra direction net, full complex Jacobian estimate,
stopping argument, and complete coefficient inventory justify removing
the previous $(d+3)^d$ factor. I found no missing persistent dimension
coefficient in that conclusion and no required correction to the frozen
file.

This is a fixed-architecture, fixed-data, sufficiently-large-width result.
It does not improve $\beta^{84Ld}$ or the exponent $3d+2$, quantify
the width threshold, establish growing-dimension uniformity, bound setup
work or precision, prove optimality, or replace the inherited base insertion
and runtime theorems by new independent proofs. Those limitations are
consistent with the candidate's stated scope.
