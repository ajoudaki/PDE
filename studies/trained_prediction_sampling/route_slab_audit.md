# Audit of the source-calculus time-interval closure

Status: reconstructed candidate proof of the uniform finite-program first
and mixed second law-derivative bounds. The old/new source cancellation
closes the proposed estimate, provided the frozen-source tensor lemma in
the supplied route is used with its full tensor sums. This is an internal
comparison-phase derivation, not a promotion review or a completed sampling
theorem. It supplies no finite-width tangent statement.

Author: `/root/weak_topology_route`, 2026-09-11. The first phase was independent.
For this second phase the supervisor explicitly authorized the two same-study
inputs below. No other route or study was read.

Inputs:

- `source_calculus_candidate.md`, SHA-256
  `e597b6ee220a6a00f69640d61002437c6521c1cbf6f0f81d28eadad90c73fe29`.
- `route_source_response.md`, SHA-256
  `51eac24d314a529af831194c09efc8552e6c2be823396571ae09acf710c9f17c`.
- Complete established C.4.7 and the explicit dependency scope recorded in
  the frozen `route_weak_topology.md`. Its first-round bytes remain at
  SHA-256 `6da7885de6e6f701954525f13bfe6039c9570f82736b2fbf7d0758cb05946295`.
- The separately frozen higher-moment forcing lemma is
  `route_weak_forcing.md`, SHA-256
  `19db0a03f2eed48cd07cdbbfc282139f49a6ebcd076e4856be5f765716eabb91`.

The target here is precisely the finite raw population-Euler output, uniformly
over sufficiently fine meshes, atom counts, masses and covariance ranks, on a
smaller C.4.7 neighborhood through physical time 40. All residual feedback,
Gaussian covariances and response coefficients are differentiated. Both
orientations of the retained initialized matrix remain in N3–N8.

## 1. What has to be kept in the interval norm

Fix a finite law with weights p_b and a finite raw Euler graph satisfying
N-cap. All values and source tensors in this proof are evaluated at this
base graph. Let k0 be an interval's first node, and let its last node have
elapsed physical time at most ell. A source slot is **old** if its time is
strictly before k0, and **new** otherwise. The lower and upper source lists
have this convention separately. A source at node k0 is new.

Let `J_j` be the sum of absolute ordered jth named-source derivatives from
the supplied frozen lemma, and put `J_0(V)=|V|`. We use:

1. lower base tensors through order five have every fixed finite Lp moment,
   including the maximum over time and the supremum over passive directions;
2. upper base source tensors of positive order through five are bounded
   pointwise, uniformly over time and passive directions;
3. c and Delta are bounded pointwise, h and the upper activation by one;
4. Q has uniformly bounded individual Lp moments and
   `E exp(lambda sum_k h_k sum_b p_b |Q_kb|)` is bounded for every fixed lambda;
5. `sum_q |D_iq|<=D0`, `|F_i,sb|<=fB h_s p_b`, and
   `|gamma_kb|<=2R0 h_k p_b`.

Item 1's passive supremum causes no Gaussian-process maximum issue: every
lower feature source tensor is bounded by the same polynomial in the source
tensors of the two-component w. The only unbounded value Q is averaged over
the actual atom weights and integrated in time. Items 1–2 are precisely the
frozen lemma, whose partition/Leibniz proof retains repeated source indices.

Write a dot with superscript e for explicit parameter differentiation of a
coordinate expression at fixed named source values. Total derivatives of
expectations also include the covariance contractions. Let E be the maximum,
over output rows in this interval, of:

- the entry supremum norms of the two covariance derivatives Cxi' and Czeta';
- the absolute row sums of alpha', beta', F' and D';
- the scalar residual derivatives.

Include all old and new source columns in these rows. For covariance matrices
include the available prefix; in the homogeneous calculation old–old entries
are zero. All quantities in E are deterministic. The coordinate derivatives
are estimated from E and are not silently included as uncontrolled members
of this norm.

For one mass direction s=(s_b),

\[
 \gamma'_{kb}=-2h_k(s_b r_{kb}+p_b r'_{kb}),\qquad
 \sum_b|\gamma'_{kb}|\le C h_k(\|s\|_1+E).                 \tag{1}
\]

In the homogeneous interval calculation set s=0 and every old prefix
derivative equal to zero. Thus `sum_b |gamma'_kb|<=C h_k E` for new
updates; old gamma derivatives vanish. This homogeneous calculation is
legitimate because all first-variation equations are linear. General old
derivatives and the mass direction become a specified additive forcing.

## 2. Small increments of *base* lower source tensors

For every fixed j<=5 and finite p,

\[
 \left\|\max_{k\text{ in interval}}
       J_j(w_k-w_{k0})\right\|_p\le C_{j,p}\ell,
\quad
 \sup_u\left\|\max_k J_j(h_k(u)-h_{k0}(u))\right\|_p
                                           \le C_{j,p}\ell. \tag{2}
\]

These are differences of the formal expressions on one common source list,
not differences obtained after coupling two Gaussian laws. The first
inequality follows by differentiating the exact sum of new raw increments.
At each time the source tensor of `phi'(w.u)Q` is bounded by a fixed
polynomial in lower base source tensors times `1+|Q|`. Hölder and the
frozen lemma bound its Lp norm uniformly. Sum the original weights h_k p_b
and apply Minkowski; their sum is at most ell. This also handles j=0.

For the second inequality write the scalar identity

`phi(w_k.u)-phi(w_k0.u)
 = integral_0^1 phi'((w_k0+z(w_k-w_k0)).u) (w_k-w_k0).u dz`.

Differentiate j times in the source coordinates. Every Leibniz/partition
term contains one source derivative of `w_k-w_k0`, of order between zero
and j. It is O(ell) in any fixed Lp by the first inequality. The remaining
finitely many factors have all fixed moments by the base tensor bounds.
Hölder and summation prove (2). Derivatives of tanh through order j+1 are
bounded, so this argument also applies at j=5. There is no power
`(h_k p_b)^j` in this proof.

For every new forward slot i=(k,u), let `h_i^0=h_k0(u)`. For an old slot
put `h_i^0=h_i`. Every `h_i^0` depends only on old lower sources. Products
therefore satisfy

\[
 \|J_j(h_i h_l-h_i^0h_l^0)\|_p\le C_{j,p}\ell,
                                                       \tag{3}
\]

when at least one slot is new; use the product difference and (2). The
left side is zero for two old slots.

## 3. Explicit lower variations are O(ell E)

In the homogeneous interval calculation, for j<=3 and every finite p,

\[
 \left\|\max_k J_j(\dot w_k^e)\right\|_p+
       \sup_{k,u}\|J_j(\dot h_k^e(u))\|_p
                                  \le C_{j,p}\ell E.         \tag{4}
\]

Here is the closed recurrence behind (4). At fixed source values,

\[
 \dot Q_i^e=\sum_q D'_{iq}h_q+\sum_q D_{iq}\dot h_q^e,
\]
\[
 \dot w_{k+1}^e=\dot w_k^e+
 \sum_b\left[\gamma'_{kb}\phi'(w_k.u_b)Q_{kb}u_b+
 \gamma_{kb}\{\phi''(w_k.u_b)(\dot w_k^e.u_b)Q_{kb}
                  +\phi'(w_k.u_b)\dot Q_{kb}^e\}u_b\right]. \tag{5}
\]

The direct Gaussian source has no explicit parameter derivative. The first
line has tensor bounds consisting of E times base lower tensors, plus D0
times current or earlier tensors of the explicit lower variation. In the
second line the highest mixed tensor is propagated with coefficient at
most `C h_k(D0+sum_b p_b |Q_kb|)`. All other terms contain strictly lower
variation tensor order, multiplied by base tensors, or a deterministic
coefficient derivative bounded by E. Equation (1) retains h_k in every
injection term. The initial variation is zero.

At order zero, iterate (5) pointwise and use the exponential integrating
factor controlled by item 4. Hölder and Minkowski bound its product with
the new-interval forcing by `C_p ell E`; in particular
`||sum_new h_k sum_b p_b |Q_kb|||_p<=C_p ell`. At order j, use the same
integrating factor and the already proved lower-order variation tensor
bounds, taking the finitely many higher Hölder exponents needed. The base
tensor bounds hold for every finite p, so no moment exponent is exhausted.
This finite induction proves (4). Applying the partition formula to h
proves its second term. No supremum of Q over neurons, times or atoms is used.

## 4. The lower covariance cancellation supplies the time factor

The source differentiation formula is

\[
 {d\over da}\mathbb E q
   =\mathbb E\dot q^e+\tfrac12\sum_{ij}C'_{ij}\mathbb E\partial_{ij}q.
                                                               \tag{6}
\]

The homogeneous Czeta' is zero on old–old entries. Since every `h_i^0`
depends only on old sources, its covariance contraction in (6) vanishes.
The remaining contraction for `E[h_i h_l]` can be replaced exactly by
the contraction of `h_i h_l-h_i^0h_l^0`. Equations (3),(4), with the
entry maximum of Czeta' bounded by E, give

\[
                 \|Cxi'\|_{\max}\le C\ell E.                \tag{7}
\]

The same cancellation works after summing the alpha row. Namely

\[
 \alpha'_{k u,p}=\mathbb E\partial_p\dot h_k^e(u)
      +\tfrac12\sum_{ij}Czeta'_{ij}
                             \mathbb E\partial_{ijp}h_k(u).
\]

Replace h_k in the second term by `h_k-h_k0`. A derivative in a new index
annihilates h_k0, and coefficients in two old indices are zero. Summing
absolute values over p then uses J3 of that difference, not an unweighted
number of source slots. Thus

\[
 \sup_{k,u}\sum_p|\alpha'_{k u,p}|\le C\ell E.               \tag{8}
\]

Finally differentiate
`F_iq=alpha_iq+1_(q<i) gamma_q E[h_i h_q]`. Old gamma derivatives vanish;
new gamma derivatives have total magnitude O(ell E) by (1); and the
covariance derivative of every contraction is O(ell E) by (7). The sum
of absolute *base* gamma values over the full past is at most 2R0T.
Consequently

\[
                    \sup_i\sum_q|F'_{iq}|\le C\ell E.        \tag{9}
\]

The factor ell in (8) is not a claim that all old source derivatives of
h_k are small. They are not. It comes from subtracting the old-prefix
expression before contracting the unknown covariance variation.

## 5. Upper explicit variations and the remaining coefficients

At fixed upper sources,

\[
 \dot Z_i^e=\sum_{q<i}F'_{iq}\Delta_q+
                              \sum_{q<i}F_{iq}\dot\Delta_q^e,
\]
\[
 \dot c_k^e=\sum_{q\text{ new},\ q<k}
        [\gamma'_q\phi(Z_q)+\gamma_q\phi'(Z_q)\dot Z_q^e],
\quad
 \dot\Delta_i^e=\dot c_k^e\phi'(Z_i)+c_k\phi''(Z_i)\dot Z_i^e.
                                                               \tag{10}
\]

Old explicit coordinate derivatives are zero in this homogeneous calculation.
Differentiate these identities j<=3 times in named sources and sum absolute
tensor entries. Every base upper source tensor is pointwise bounded. The
F' row in the first line costs O(ell E) by (9). The remaining F coefficients
have density fB h_s p_b, and only new slots carry an unknown coordinate
variation. Hence their total time is at most ell. The c equation has exactly
the same new-update weights. The highest variation tensor is linear; all
other terms have lower tensor order and bounded coefficients.

Discrete Gronwall, followed by induction on j, therefore proves the
pointwise bounds

\[
 \sup_{k,u}\{J_j(\dot Z_k^e(u))+J_j(\dot\Delta_k^e(u))\}
       +\max_kJ_j(\dot c_k^e)\le C_j\ell E,
                   \qquad j=0,1,2,3.                        \tag{11}
\]

The j=0 statement concerns variations, not the unbounded base Z values.
There is no need for `Delta_k-Delta_k0` to have small source tensors:
the new current upper source has derivative one, and cannot be identified
formally with the old current source. Equation (7), not such an identification,
supplies the covariance factor in the next step.

Apply (6) on the upper source space. The explicit derivatives of
`Delta_i Delta_l` are O(ell E) by (11), and their second source tensor
sum is bounded pointwise. Cxi' is O(ell E) by (7). Therefore

\[
                         \|Czeta'\|_{\max}\le C\ell E.       \tag{12}
\]

For beta, sum its expected first-source derivative over source columns
before estimating: its explicit term is bounded by J1(dot Delta), and
its covariance term by `||Cxi'||_max E J3(Delta)`. Thus

\[
             \sup_i\sum_p|\beta'_{ip}|\le C\ell E.           \tag{13}
\]

The residual derivative is treated as the expectation of `c phi(Z)`;
its explicit derivative obeys (11) and its covariance contraction uses
the bounded second source tensor. Hence `sup_i |r'_i|<=C ell E`.
Differentiating `D_iq=beta_iq+gamma_q E[Delta_i Delta_q]` now gives
`sup_i sum_q |D'_iq|<=C ell E`, using (12),(13), (1), and the bounded
full-past sum of base gamma values. This includes the distinguished current
beta coefficient; its row tensor sum is one direct slot, not the atom count.

All members of the defined norm E have now been bounded by C ell E.
Choose ell with C ell<=1/2. The homogeneous interval system has no nonzero
solution in this finite deterministic coefficient space, and its causal
inhomogeneous version has a uniform inverse estimate as follows.

## 6. Old-prefix forcing and finite interval iteration

The preceding proof is an estimate on the full finite linear differentiated
recursion, not an existence assumption for unknown coefficients. Their
values exist by the finite chronological construction. When old prefix
derivatives and the mass direction s are nonzero, put them on the known
side of every displayed linear equation. If their coefficient norms and
mixed coordinate tensor norms are bounded by K, the same proof gives

\[
                         E\le C(K+\|s\|_1)+C\ell E.          \tag{14}
\]

Here are the terms whose handling could otherwise conceal a loss. The
old–old covariance contraction no longer vanishes, but its matrix entry
bound is known and it is paired with the bounded full source tensor sum.
An explicit old h or Delta derivative is multiplied by a base D row or
the time-weighted base F row, so their total coefficients are bounded by
D0 or fBT. Derivatives of old gamma are summed in absolute value using
their already known bound `C h_k (|s_b|+p_b K)`. Differentiated old F/D rows
have their already known row-sum bound. Upper coordinate derivative tensors
from the old prefix are pointwise bounded; lower ones have every finite
moment, precisely as needed in the Hölder estimates for (5). Every such
term contributes to C(K+||s||_1), independently of how many old slots exist.

Absorb the last term in (14). Equations (4),(11) with their additional
known terms supply the same kind of coordinate tensor bounds for the enlarged
prefix. Thus the induction hypotheses on K propagate to the next interval.

Restrict h_max<=ell/2 in addition to the original cap threshold. A greedy
partition of the nodes gives intervals of length between ell/2 and ell,
apart from the last, and at most `ceil(2T/ell)+1` intervals. Their number is
independent of the mesh. The recurrence `K_next<=C(K+||s||_1)` over this
fixed number of intervals proves

\[
 \sup_{\text{all rows}}
  \{\|Cxi'\|_{\max},\|Czeta'\|_{\max},
       \|\alpha'\|_{\rm row},\|\beta'\|_{\rm row},
       \|F'\|_{\rm row},\|D'\|_{\rm row},|r'|\}
                          \le C_T\|s\|_1.                  \tag{15}
\]

The first explicit mixed source tensors through order three have corresponding
global bounds, pointwise in the upper population and in every finite Lp in
the lower population. Initial sensitivities vanish because initialization
does not depend on the law.

## 7. Mixed second law derivatives

Let s,t be two fixed signed mass directions. The full mixed derivative of
gamma is

\[
 \gamma^{st}_{kb}=-2h_k[p_b r^{st}_{kb}+s_b r^t_{kb}+t_b r^s_{kb}]. \tag{16}
\]

Its highest-order unknown is exactly the homogeneous first-variation term
with `r'` replaced by `r^(st)`. The other two terms have summed magnitude
at most `C h_k ||s||_1 ||t||_1` by (15).

For an expectation q with two parameters the formula is

\[
 (\mathbb E q)^{st}=\mathbb E q^{e,st}
 +\tfrac12\sum C^s_{ij}\mathbb E\partial_{ij}q^{e,t}
 +\tfrac12\sum C^t_{ij}\mathbb E\partial_{ij}q^{e,s}
 +\tfrac12\sum C^{st}_{ij}\mathbb E\partial_{ij}q
 +\tfrac14\sum C^s_{ij}C^t_{kl}\mathbb E\partial_{ijkl}q.   \tag{17}
\]

The terms linear in the unknown second coordinate/coefficient/covariance
variations are precisely the homogeneous first-order system already bounded
in Sections 3–5. Old–old unknown covariance entries again vanish after old
prefix second variations are moved to the known side. Thus the same subtraction
`h_k-h_k0` and the same small factor ell apply to these highest-order terms.

Every remaining term is a product of two already controlled first variations,
or a supplied old second variation. Its norm is bounded by
`C ||s||_1 ||t||_1` plus the old second-variation norm, with no slot-count
factor. For example:

- covariance products in (17) use entry suprema of C^s,C^t against the full
  fourth source tensor, or the fifth tensor for alpha and beta;
- the mixed explicit/covariance terms use first mixed source tensors of
  order two, or three for alpha and beta, already supplied by (15);
- differentiated lower products such as `Q dot w^s dot w^t` have every
  required fixed moment by Hölder and the global first mixed tensor bounds;
- `sum_q F^s_iq dot Delta^t_q` is bounded by the row sum of F^s and the
  pointwise upper variation bound. It need not carry a new h_q: it is a
  known quadratic forcing, not a coefficient of the unknown second variation;
- repeated derivatives at one old upper source are counted in the full
  tensor sums. Only the one actual quadrature factor of the underlying
  update is used.

The explicit second coordinate recursions require source tensors only through
order one to compute their expectation and alpha/beta rows. Their highest
terms obey the same linear estimate, and their remaining products are controlled
as above. Consequently, on each interval,

\[
 E_2\le C(K_{2,\rm old}+\|s\|_1\|t\|_1)+C\ell E_2.        \tag{18}
\]

Absorption and the same fixed interval count prove the global mixed second
coefficient and residual bounds `C_T ||s||_1 ||t||_1`. The needed second
explicit source tensors have the corresponding lower Lp and upper pointwise
bounds. There is no induction on the number of steps in (18).

## 8. Finite-graph smoothness, output, and remaining scope

At any fixed graph, all asserted derivatives exist before their uniform
bounds are sought. Chronologically, lower h and alpha determine the current
forward covariance and F row; then Z, Delta and beta determine the reverse
covariance and D row; only then is the raw state updated. Each Gaussian
expectation derivative is given by (6),(17), whose singular-covariance proof
was supplied and read. The finite graph has finite polynomial envelopes in
its Gaussian source list on a neighborhood of each coefficient configuration.
Thus the derivative construction is legitimate at rank loss. It differentiates
the covariance, not a square root of it.

If a direction adds a previously absent atom, include that atom's zero-weight
query slots in the base graph. At weight zero these are unused queries;
their old effects vanish with their update weight, while each current slot
is still a distinct formal argument. Equivalently take a positive-weight
limit of the fixed graph. Uniform tensor and coefficient bounds survive,
and no minimum-weight denominator occurs. For finite-graph differentiability
one may even allow signed training coefficients in a small parameter
neighborhood: the source covariances remain Gram matrices of the recursively
defined random inputs. Positivity of the training law is needed for the
uniform base N-cap bounds, not for this fixed-graph smoothness argument.

Append any passive query u. Apply (6),(17) to the scalar output
`E[c phi(Z(u))]`. Its base upper source tensors and the first/second explicit
variations have the bounds established above. Uniformity in passive u gives

\[
 \sup_{h,\lambda,t\le40,u}|D f_{h,\lambda}(t,u)[\sigma]|
                                      \le C_T\|\sigma\|_{TV},
\]
\[
 \sup_{h,\lambda,t\le40,u}|D^2 f_{h,\lambda}(t,u)[\sigma,\tau]|
                             \le C_T\|\sigma\|_{TV}\|\tau\|_{TV}. \tag{19}
\]

Here TV is the total mass of the variation measure, consistent with
`||s||_1` on a finite support. Coincident atoms can be kept distinct; the
Gaussian covariance may then be singular, already allowed. A time on an
affine raw Euler segment is the program obtained by appending one shorter
final step, so the constants also cover all interpolation times. The same
bounds hold in H=L2(circle), since that norm is at most the supremum norm
under normalized circle measure.

This establishes the proposed finite-program analytic estimate as a candidate
proof using the supplied frozen-source tensor lemma. Passing derivatives
through law completion and mesh removal, identifying the limiting influence,
and proving the statistical replacement/CLT statements remain separate
arguments. The estimate is for deterministic population Gaussian programs;
it has not been transferred to actual finite-network derivatives.

The most consequential audit checks were: the cancellation must occur in
the *lower* old-prefix source expression; one must not identify current upper
sources at different times; coefficient row sums must include all old columns;
and second-order known quadratic forcing need not carry ell, while every
highest-order unknown must. With these distinctions the proposed interval
absorption has no remaining identified atom-count, covariance-rank, or
step-count loss.
