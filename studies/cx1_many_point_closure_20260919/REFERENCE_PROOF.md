# Many-anchor fitted reference, full-row observations, and paired activity

Status: complete author candidate, internally checked; not independently reviewed
or promoted. This proves the orthogonal reference component of C-X1. It does
not assert the perturbed-configuration source estimate or the finite observable
closure theorem, which are separate obligations.

## 1. Contract, dependencies, and conclusions

Fix separately integers `1 <= m <= d` and labels `y_a in {-1,1}`. The training
law is `m^-1 sum_a delta_(sqrt(d)e_a,y_a)`. Both activations are `phi=tanh`.
The finite model has first rows `w_i in R^d`, middle matrix `A_n`, stored
readout `c_n`, predictions

\[
 z^1_{n,i}(u)=w_i\cdot u,\quad h^1_n(u)=\phi(z^1_n(u)),\quad
 z^2_n(u)=A_nh^1_n(u),\quad h^2_n(u)=\phi(z^2_n(u)),\quad
 f_n(\sqrt d\,u)=n^{-1}c_n^Th^2_n(u).
 \tag{1.1}
\]

The independent stored Gaussian variances are `(1,1/n,1/n^2)` and the
physical block mobilities are `(n,1,n)`. The loss is the unhalved **mean**
`m^-1 sum_a(f_n(sqrt(d)e_a)-y_a)^2`. In particular, the random finite readout
is part of the algorithm; only its population limit is zero.

The scientific inputs read for this proof are this study's README,
`docs/NOTATION.md`, the complete units A.1--A.4, B.1, C.3 (including its
weighted-loss correction), C.4.5.1 (including the complete rational
Gaussian certificate), and C.4.7.8 section 8 in `docs/global_nonlinear.md`,
and the complete unit
III.F.1--III.F.11 in `docs/special_data_limits.md`. No other study, another
author's route, conversation history, or unpublished finding is an input.
The two required mathematical skills and their research-contract and
adversarial-audit instructions were read. No training experiment is used.

The established inputs used below are these precise specializations.

* III.F and A.1 construct consistent deterministic joint laws for every
  fixed finite Gaussian program, with its actual transpose, and identify
  empirical laws in `W2`. Continuous coordinate instructions of at most
  linear growth are allowed in A.1. The root tuple here is the full
  `N(0,I_d)` first row; both matrix orientations and all required passive
  probes are included in finite unions before completion.
* A.3 gives `||A_0||op <= 2` on those canonical generated spaces.
* III.F.8--10 and A.4 give HS rank-one adjunction, the strong chain rule
  along `C1(L2)` curves, and continuous differentiability of the scalar
  prediction in the raw Hilbert metric. Tanh has bounded first and second
  derivatives, as required. An `L2`-valued activation map is not asserted
  to be Frechet differentiable on an entire `L2` ball.
* C.4.5.1's complete exact rational Gaussian certificate proves
  `39/100 < q < 2/5`, `v > 1/5`, `a_0 > 3/10`, and `r_0 > 3/5`, with the
  quantities defined below. It consists of outward-rounded rational
  lower/upper Riemann sums and Taylor bounds for the exponential; no
  trained trajectory enters these constants. Only `q>1/4` and `v>1/5`
  are needed for the numerical bounds below.

The resulting reference is a unique strong autonomous population flow
for all physical times, with full row and actual action/adjoint. It has a
fitted strong endpoint, whole-sphere prediction convergence, and

\[
 T_m=5m,\qquad
 \mathcal L_*(T_m)<e^{-4}<1/16.
 \tag{1.2}
\]

Both hidden layers have strictly positive paired activation displacement
and strictly positive best-affine-fit error on their visited preactivation
laws at the same explicit physical time in (7.13). Actual finite GF converges on
every compact physical interval. Actual raw GD has the same limit under
the sufficient condition `eta_n sqrt(n) -> 0`, proved in section 8.
Constants may depend on the separately fixed `m,d`, never on neural width,
closure order, or an auxiliary time resolution. No uniform growing-`m,d`
statement is made.

## 2. Full state and the exact feature flow

Let `H_l=L2(Omega_l)` be the two canonical generated probability spaces.
The full first row is `w=(w_1,...,w_d) in L2(Omega_1;R^d)`, initially
`g~N(0,I_d)`. Write `A=A_0+K`, where only the increment `K` is HS, and
let `c in H_2`, initially zero. The raw increment metric is

\[
 \|(v,B,a)\|_{\rm raw}^2
 =\|v\|_{L^2(\Omega_1;\mathbb R^d)}^2+\|B\|_{\rm HS}^2+\|a\|_2^2.
 \tag{2.1}
\]

Its exact finite counterpart is
`||Delta W1||F^2/n+||Delta A||F^2+||Delta c||2^2/n`.
For every unit `u`, define

\[
 Z^1(u)=w\cdot u,\ H^1(u)=\phi(Z^1(u)),\quad
 Z^2(u)=AH^1(u),\ H^2(u)=\phi(Z^2(u)),\quad
 f(\sqrt d\,u)=\langle c,H^2(u)\rangle_2.
 \tag{2.2}
\]

An anchor subscript means `u=e_a`. Put

\[
 h={1\over m}\sum_{a=1}^m y_aH^2_a,\qquad
 b=\langle c,h\rangle={1\over m}\sum_a y_af_a.
 \tag{2.3}
\]

For a hidden increment `(v,B)`, define the bounded map into `H_2`

\[
 J(v,B)={1\over m}\sum_a y_a\phi'(Z^2_a)
       \{BH^1_a+A(\phi'(w_a)v_a)\}.
 \tag{2.4}
\]

This is its directional differential, and the chain rule along strong
curves is sufficient here. Rank-one HS adjunction gives

\[
 J^*c=\left(\left(
  (m^{-1}y_a\phi'(w_a)A^*(\phi'(Z^2_a)c))_{a\le m},\ 0_{a>m}\right),
  m^{-1}\sum_a y_a(\phi'(Z^2_a)c)\otimes H^1_a\right).
 \tag{2.5}
\]

We first solve the autonomous feature equation

\[
 c_s=h,\qquad (w,K)_s=J^*c.
 \tag{2.6}
\]

The `m^-1` in every hidden block is essential: it comes from the mean
loss and is not an additional physical mobility.

For existence, let `j(X,z)` solve `j_X=phi'(j)`, `j(0,z)=z`.
Its bounded globally Lipschitz scalar field gives a solution for all
real `X,z`, with

\[
 |j(X,z)-j(Y,z)|\le |X-Y|,\qquad |j(X,z)|\le |z|+|X|.
 \tag{2.7}
\]

Set `w_a=j(X_a,g_a)` for `a<=m`, leave `w_j=g_j` for `j>m`, and solve

\[
 (X_a)_s={y_a\over m}A^*(\phi'(Z^2_a)c),\qquad
 K_s={1\over m}\sum_a y_a(\phi'(Z^2_a)c)\otimes H^1_a,
 \qquad c_s=h.
 \tag{2.8}
\]

For fixed roots this field is Lipschitz on sets with bounded clock `L2`
norms, bounded `||K||HS`, and bounded readout supremum, in the sum of
clock `L2`, HS, and readout `L2` distances. Indeed the first features are
one-Lipschitz in their clocks, all activations are bounded by one, and

\[
 \|\phi'(Z)c-\phi'(\bar Z)\bar c\|_2
 \le\|c-\bar c\|_2+2\|\bar c\|_\infty\|Z-\bar Z\|_2.
 \tag{2.9}
\]

Adding and subtracting one factor treats the actions and rank-one terms.
The class `||c||infty<=B` is closed in `L2` and hence complete; the
integral map on a sufficiently short interval preserves an enlarged
supremum bound and is a contraction in the stated metric. This proves
local existence and uniqueness without assuming raw-ball Lipschitzness.

Directly from (2.8), for `s>=0`,

\[
 \|c(s)\|_\infty\le s,\quad \|K(s)\|_{\rm HS}\le s^2/2,\quad
 \|A(s)\|_{\rm op}\le2+s^2/2,
 \tag{2.10}
\]
\[
 \left(\sum_{a\le m}\|X_a(s)\|_2^2\right)^{1/2},\quad
 \|w(s)-g\|_2
 \ \le {1\over\sqrt m}(s^2+s^4/8).
 \tag{2.11}
\]

For (2.11), bound each clock velocity by `(2+s^2/2)s/m` and sum its
`m` component norms in Euclidean norm. These polynomial bounds prevent
finite-feature-time escape; integration gives a strong endpoint at any
putative finite terminal time and local contraction extends the solution.
The rank-one estimate gives a `C1` HS curve. The bounded-multiplier lemma
then gives a `C1` raw row curve and proves (2.6).

Conversely, a raw solution has the form (2.8): its scalar equation is
`w_a'=B_a(s)phi'(w_a)`, with `B_a` time-integrable at almost every
coordinate by Fubini. The scalar flow identity and the scalar Lipschitz
inequality imply `w_a(s)=j(int B_a,g_a)`. Thus the chart neither adds nor
loses a raw solution. At a restart, retain the current row, action and
readout, reset every active clock to zero, and apply the same construction.
Equal current joint action laws identify the generated spaces isometrically,
including the actual adjoint, and their future integral equations agree.
This is autonomy and restartability of the raw reference, without a past
transcript in its state.

## 3. Signed permutations and arbitrary binary labels

The required symmetry is an action-law assertion, not a pointwise
assertion about a realized finite initialized network.

For a permutation `pi` of the `m` active coordinates put
`epsilon_a=y_a y_{pi(a)}`. Transform the row by

\[
 \widetilde w_a=\epsilon_a w_{\pi(a)}\ (a\le m),\qquad
 \widetilde w_j=w_j\ (j>m),\qquad
 \widetilde A=A,\quad\widetilde c=c.
 \tag{3.1}
\]

Oddness of `phi` and evenness of `phi'` give
`Htilde_a^l=epsilon_a H_{pi(a)}^l` and
`phiprime(Ztilde_a^l)=phiprime(Z_{pi(a)}^l)`. Consequently
`htilde=h`: in its sum `y_a epsilon_a=y_{pi(a)}`. The transformed row
velocity is

\[
 \epsilon_a {y_{\pi(a)}\over m}
 \phi'(w_{\pi(a)})A^*(\phi'(Z^2_{\pi(a)})c)
 ={y_a\over m}\phi'(\widetilde w_a)
 A^*(\phi'(\widetilde Z^2_a)c),
 \tag{3.2}
\]

and the middle velocity is unchanged after reindexing. The readout
velocity is unchanged because `htilde=h`. This proves exact equivariance
of (2.6), including arbitrary mixed labels.

Here is the probabilistic step needed to turn this algebra into equality
of the population predictions. Adjoin to the countable canonical language
the images of every program under this finite signed-permutation group.
At finite width the joint initial law `(g,A_0)` is invariant under (3.1),
and every subsequent coordinate operation and the two orientations of
the same initialized matrix transform by the identities just proved.
Thus each finite tuple and its transformed tuple have identical limiting
laws. On the space of the countable coordinate tuple this substitution
is a probability-preserving bijection; its pullback is an `L2` isometry
preserving products, contractions, and both action orientations. It extends
to the completed spaces by their norm bounds. Unique integral construction
commutes with this isometry. Since predictions are deterministic scalar
contractions of these canonical laws,

\[
 f_a=\epsilon_a f_{\pi(a)},\qquad y_af_a=y_{\pi(a)}f_{\pi(a)}.
 \tag{3.3}
\]

The permutation group is transitive when `m>=2`, so (2.3) gives

\[
                         f_a=y_a b\qquad(a\le m).
 \tag{3.4}
\]

For `m=1`, (3.4) follows directly from `b=y_1f_1` and `y_1^2=1`;
no transitivity argument with two distinct samples is used.

For completeness, the symmetries used here have the following further
consequences and boundary checks.

* For any orthogonal change of coordinates in the passive subspace,
  initial Gaussian invariance and the same equivariance proof give the
  corresponding whole-sphere prediction symmetry. Each particular such
  transformation may be adjoined to the countable language before taking
  the limit; a countable dense set and the input continuity in section 5
  give all of them.
* More generally, transforming labels to
  `ytilde_a=epsilon_a y_{pi(a)}` and rows to
  `wtilde_a=epsilon_a w_{pi(a)}` gives the corresponding covariance
  between any two binary-label patterns. Therefore the constants below
  can be chosen independently of the pattern. Reversing every label can
  also be realized by `c -> -c` with the hidden path unchanged.
* For each fixed state, not merely in law,
  `f(sqrt(d)(-u))=-f(sqrt(d)u)` because both activations are odd.
* When `m=1,d=1`, the input sphere is `S^0={-1,1}`. A sufficiently small
  angular neighborhood of the sole anchor contains only that anchor.
  All reference conclusions remain true, but this case does not supply
  a nontrivial angular perturbation family. For `m=1,d>1`, moving the
  single unit input is a rotation of the problem. A nontrivial family of
  correlated distinct anchors requires `m>=2` (and `d>=m`).

The same transformations preserve the physical mean-loss field. Below it
is enough to construct that physical field by a scalar clock from (2.6).

## 4. Fitting, clocks, and explicit learning horizon

The strong chain and product rules give `h_s=J(w,K)_s`, hence

\[
 c_{ss}=JJ^*c,\qquad
 b_s=\|h\|_2^2+\|J^*c\|_{\rm hidden}^2
     =\|\theta_s\|_{\rm raw}^2,
 \tag{4.1}
\]

where `theta=(w,K,c)`. No derivative of `J` is invoked.

For a standard normal `G` define

\[
 q=E\tanh^2G,\qquad v=E\tanh^2(\sqrt qG),\qquad
 \beta_m=\|h(0)\|_2^2={v\over m}>{1\over5m}.
 \tag{4.2}
\]

Indeed `H^1_a(0)=tanh g_a` have Gram `q I_m`, so the initial Gaussian
forward tuple `Y_a=A_0H^1_a(0)` consists of independent `N(0,q)` variables.
The bounded odd `tanh Y_a` are independent and centered, and all label
squares equal one, proving (4.2).

On an interval where `g_c=||c||2>0`, scalar differentiation gives

\[
 (g_c)_s={b\over g_c},\qquad
 (g_c)_{ss}={\|h\|_2^2-(g_c)_s^2+\|J^*c\|_{\rm hidden}^2\over g_c}
 \ge0.
 \tag{4.3}
\]

The inequality is Cauchy--Schwarz applied to `b=<c,h>`. The expansion
`c(s)=s h(0)+o_L2(s)` gives `(g_c)_s(0+)=sqrt(beta_m)`. Convexity on
its first positive interval implies `g_c>=s sqrt(beta_m)`, which prevents
a return to zero at a positive endpoint. Thus for every `s>0`,

\[
 \|h(s)\|_2\ge(g_c)_s\ge\sqrt{\beta_m},\qquad b_s\ge\beta_m.
 \tag{4.4}
\]

There is a unique first `s_dagger` at which `b=1`, and
`0<s_dagger<=1/beta_m<5m`. Before that level set

\[
 t(s)=\int_0^s{dv\over2(1-b(v))}.
 \tag{4.5}
\]

This is increasing. On the compact feature segment through `s_dagger`,
`b_s` is continuous and bounded, so
`1-b(s)<=C(s_dagger-s)` and `t(s)->infty` at the endpoint. Its inverse
therefore exists for every `t>=0` and satisfies

\[
 s_t=2(1-b),\qquad s(0)=0.
 \tag{4.6}
\]

By (3.4), the physical residuals are `r_a=y_a(b-1)`. Substitution into
the exact mean-loss physical equations shows that their entire raw
velocity is `2(1-b)` times (2.6). Thus (4.6) is precisely physical GF,
not a replacement optimizer. Alternatively B.1 applies with
`kappa_1=kappa_2=kappa_3=1/m` to its sum-loss equations; all its
orthogonality, activation, and readout hypotheses hold, and its unique
physical solution is the one just constructed.

With `e(t)=1-b(s(t))`,

\[
 e_t=-2b_s e,\quad 0<e(t)\le e^{-2\beta_m t},\qquad
 \mathcal L_*(t)=e(t)^2\le e^{-4\beta_m t}.
 \tag{4.7}
\]

The scalar linear equation keeps `e` strictly positive at every finite
physical time, so the clock sign never changes. At `T_m=5m`,
`4 beta_m T_m>4` and (1.2) follows. The margin to `1/4` is strict; the
reference bound alone does not specify a perturbation radius.

## 5. Strong endpoint, full-row bounds, and the passive sphere

For `0<=s_1<=s_2<=s_dagger`, Cauchy--Schwarz and (4.1) yield

\[
 \|\theta(s_2)-\theta(s_1)\|_{\rm raw}
 \le\sqrt{(s_2-s_1)(b(s_2)-b(s_1))}.
 \tag{5.1}
\]

The endpoint is the actual autonomous feature solution stopped at its
first level `b=1`. In particular it is specified from initialization and
the equations; no fitted trajectory is stored as a coefficient. Put
`L_m=sqrt(5m)` and `B_m=2+L_m`. On the entire physical trajectory and
at its endpoint,

\[
 \|c\|_2\le L_m,\quad \|K\|_{\rm HS}\le L_m,\quad
 \|A\|_{\rm op}\le B_m,\quad
 \|w\|_{L^2(\mathbb R^d)}\le\sqrt d+L_m,\quad
 \|c\|_\infty\le5m.
 \tag{5.2}
\]

Moreover,

\[
 s_\dagger-s(t)\le e(t)/\beta_m,\qquad
 \|\theta(t)-\theta_\dagger\|_{\rm raw}
 \le e(t)/\sqrt{\beta_m}.
 \tag{5.3}
\]

All `d` row coordinates are retained: the last `d-m` are fixed Gaussian
coordinates, and the first `m` evolve. For every passive input `u` the
fields in (2.2) are defined by the same current action and actual adjoint,
with no fresh-matrix substitution. Input continuity gives

\[
 \|H^1(u)-H^1(v)\|_2\le(\sqrt d+L_m)|u-v|,
 \quad
 \|H^2(u)-H^2(v)\|_2\le B_m(\sqrt d+L_m)|u-v|,
 \tag{5.4}
\]
\[
 |f(\sqrt d\,u)-f(\sqrt d\,v)|
 \le L_m B_m(\sqrt d+L_m)|u-v|.
 \tag{5.5}
\]

For a scalar prediction at any unit `u`, its row, middle, and readout
raw gradient norms are at most `B_m L_m`, `L_m`, and `1`. The straight
segment between two states of the reference has these same bounds;
integrating the scalar gradient along that segment proves

\[
 \sup_{|u|=1}|f_\theta(\sqrt d\,u)-f_{\bar\theta}(\sqrt d\,u)|
 \le C_m\|\theta-\bar\theta\|_{\rm raw},\qquad
 C_m=\sqrt{1+L_m^2(1+B_m^2)}.
 \tag{5.6}
\]

Thus, with the endpoint prediction defined by (2.2) at `theta_dagger`,

\[
 \sup_{u\in S^{d-1}}|f_*(t,\sqrt d\,u)-f_*^\infty(\sqrt d\,u)|
 \le {C_m\over\sqrt{\beta_m}}e^{-2\beta_m t},\qquad
 f_*^\infty(\sqrt d\,e_a)=y_a.
 \tag{5.7}
\]

The whole sphere is covered simultaneously. Countable passive probes are
used only to build the canonical action; (5.4)--(5.6) define its extension
to every input and justify the uniform statements.

## 6. Initial reused-action calculation and strict coefficients

The following establishes paired **activation** motion; preactivation
motion alone would not suffice. All variables in this section are fixed
initialization queries, not learned-time estimates. Define

\[
 H_{0,a}=\phi(g_a),\quad Y_a=A_0H_{0,a},\quad
 h_0={1\over m}\sum_a y_a\phi(Y_a),
 \quad U_a=h_0\phi'(Y_a),\quad P_a=A_0^*U_a,
 \tag{6.1}
\]
\[
 V_a=\phi'(g_a)^2P_a,\quad R_a=qU_a+A_0V_a,
 \quad C_{ab}=E[U_aU_b],
 \tag{6.2}
\]
\[
 a_0=E\phi'(G)^4,\quad r_0=E\phi'(\sqrt qG)^2,\quad
 d_0=E[\phi(\sqrt qG)^2\phi'(\sqrt qG)^2],\quad
 c_* =\min(d_0,vr_0)>0.
 \tag{6.3}
\]

All these constants depend only on Gaussian initialization. They are
strictly positive because the tanh derivative is everywhere positive,
`q>0`, and a nondegenerate Gaussian is nonzero almost surely. They are
finite because all displayed scalar gates are bounded.

The matrix `C` is positive definite for every binary pattern and every
`m>=1`. If a linear combination of `U_a` vanishes, full Gaussian support
and continuity imply
`h_0(Y) sum_a z_a phi'(Y_a)=0` for every `Y in R^m`. The zero set of
`h_0` has empty interior, since each of its partial derivatives is
`y_a phi'(Y_a)/m != 0`. Hence `sum z_a phi'(Y_a)=0` on a dense open set,
then everywhere by continuity. Varying one coordinate and using
nonconstancy of `phi'` gives `z_a=0` for every `a`. This includes `m=1`.

The actual initial transpose response, obtained by conditioning the same
Gaussian matrix on its `m` initial forward calls, is

\[
 P_a=\sum_b p_{ab}H_{0,b}+\Gamma_a,\quad
 p_{ab}=E[Y_bU_a]/q,\quad \Gamma\sim N(0,C),
 \tag{6.4}
\]

where `Gamma` is independent of the full first row `g`. In the finite
conditioning formula, the conditional mean is the matrix fixed on the
span of the forward queries; the unused matrix part gives the Gaussian
term with covariance `C`. Projections of fresh output noise onto `m`
old directions have expected squared RMS `m/n` and vanish. The query
Gram `q I_m` is nonsingular, so III.F.3 applies directly. Bounded smooth
gates and fixed finite Gaussian envelopes justify the fixed-program
limit and all contractions in (6.4).

Let `alpha_b=E[H_{0,b}V_a]/q`,
`V_a^perp=V_a-sum_b alpha_b H_{0,b}`, and
`sigma_a^2=E[(V_a^perp)^2]`. Conditioning the same matrix on the forward
and reverse calls gives

\[
 A_0V_a=\sum_b\alpha_bY_b+\bar a\,U_a+\sigma_a\gamma_a,
 \qquad\bar a=E\phi'(G)^2,
 \tag{6.5}
\]

where, for each fixed `a`, `gamma_a` is standard normal independent of
the old second-layer tuple `Y`. No independence between different
`gamma_a` is asserted. To check its response coefficient, the general
conditional formula gives `C^-1 E[P V_a^perp]`. The deterministic part
of each `P_b` lies in the initial forward span and pairs to zero with
`V_a^perp`. The remaining expectation is
`E[Gamma_b Gamma_a] E[phi'(g_a)^2]=C_ba bar a`; multiplication by `C^-1`
gives `bar a` in coordinate `a`. The fresh variance is `sigma_a^2`.
This calculation retains both reused conditional responses.

Conditional variance given `g` yields

\[
 \|V_a\|_2^2\ge C_{aa}a_0,\quad
 \sigma_a^2\ge C_{aa}a_0,\quad
 \|\phi'(Y_a)R_a\|_2^2\ge C_{aa}a_0r_0.
 \tag{6.6}
\]

For the last bound condition on `Y` in (6.5). Every other term of `R_a`
is a function of that tuple and cannot cancel the fresh Gaussian term.
Independence and oddness of the initial `Y_b` give the exact diagonal

\[
 C_{aa}={d_0+(m-1)vr_0\over m^2}\ge {c_*\over m}.
 \tag{6.7}
\]

In particular `m=1` uses `d_0>0`; it does not rely on a nonexistent
other sample. Define the positive, pattern-independent constant

\[
 \alpha_m={\sqrt{a_0r_0c_*}\over2m^{3/2}}.
 \tag{6.8}
\]

The two feature-time leading activation coefficients
`y_a V_a/(2m)` and `y_a phi'(Y_a)R_a/(2m)` each have `L2` norm at least
`alpha_m`. The following remainder bounds produce a specified positive
time at which these coefficients imply actual displacement.

## 7. Explicit activity time and paired margin

We first record moment estimates for these fixed initial queries. Bessel's
inequality in the orthonormal tuple `Y_b/sqrt(q)` gives
`sum_b p_ab^2 <= ||U_a||2^2/q <= 1/q < 4`. Consequently
`sum_b |p_ab|<2 sqrt(m)` and (6.4) gives

\[
 \|P_a\|_4\le2\sqrt m+3^{1/4}\le4\sqrt m,\quad
 \|P_a\|_2\le2,\quad \|V_a\|_2\le2,
 \tag{7.1}
\]
\[
 \tau_R(P_a):=\|P_a1_{|P_a|>R}\|_2
 \le {\|P_a\|_4^2\over R}\le {16m\over R}.
 \tag{7.2}
\]

The second inequality in (7.1) also follows directly from bounded action
and `||U_a||2<=1`. In (6.5), `sum alpha_bY_b` is Gaussian with variance
`q sum alpha_b^2=||Proj_span(H0) V_a||2^2<=4`, and `sigma_a<=2`.
The two Gaussian terms therefore each have `L4` norm at most
`2 3^(1/4)`. Since `(q+bar a)|U_a|<=2`,

\[
                         \|R_a\|_4<8.
 \tag{7.3}
\]

For `0<=s<=1`, (2.10)--(2.11), the one-Lipschitz activations, and the
two-Lipschitz derivative give successively

\[
 \|A\|\le5/2,\quad\|c\|_\infty\le s,\quad\|K\|_{\rm HS}\le s^2/2,
 \quad\|w_a-g_a\|_2\le {5s^2\over4m},
 \tag{7.4}
\]
\[
 \|Z^2_a-Y_a\|_2\le4s^2,\quad\|h-h_0\|_2\le4s^2,
 \quad\|c-sh_0\|_2\le4s^3/3,
 \tag{7.5}
\]
\[
 \|\phi'(Z^2_a)c-sU_a\|_2\le10s^3,\quad
 \|A^*(\phi'(Z^2_a)c)-sP_a\|_2\le26s^3.
 \tag{7.6}
\]

For the first bound of (7.5), expand `A H1-A0 H10` to obtain
`s^2/2+(5/2)(5s^2/(4m))<=4s^2`. Integrating its average gives the
readout error. The first bound of (7.6) is at most
`4s^3/3+2s(4s^2)<10s^3`; its second bound is at most
`(5/2)10s^3+(s^2/2)s<26s^3`.

Truncating only the fixed initial `P_a` gives

\[
 \|(\phi'(w_a)-\phi'(g_a))P_a\|_2
 \le {5R\over2m}s^2+2\tau_R(P_a).
 \tag{7.7}
\]

Subtract `y_a s phi'(g_a)P_a/m` from the first raw velocity, use
(7.6)--(7.7), and integrate. The preactivation remainder is at most
`tau_R(P_a)s^2/m+(13/(2m)+5R/(8m^2))s^4`. Apply the tanh Taylor bound
`|phi(z+v)-phi(z)-phi'(z)v|<=|v|^2` to the artificial leading increment
`y_a s^2 phi'(g_a)P_a/(2m)`. Its `L2` remainder is at most
`s^4||P_a||4^2/(4m^2)<=4s^4/m`. Therefore, with
`B_1(R)=11/m+R/m^2`,

\[
 \|H^1_a(s)-H^1_a(0)-{y_as^2\over2m}V_a\|_2
 \le {\tau_R(P_a)\over m}s^2+B_1(R)s^4.
 \tag{7.8}
\]

The middle velocity differs from
`s m^-1 sum_b y_b U_b tensor H0_b` in HS norm by at most
`10s^3+5s^3/(4m)<=12s^3`, so its integrated remainder is at most
`3s^4`. Its leading increment applied to `H0_a` is
`y_a q U_a s^2/(2m)`, because the initial first-feature Gram is `q I`.
Expanding `A H1` and using `||A0||<=2`, (7.8), and
`||K Delta H1_a||2<=5s^4/(8m)` proves the second preactivation expansion
with error at most
`2 tau_R(P_a)s^2/m+[2B_1(R)+3+5/(8m)]s^4`.
The final tanh Taylor remainder is at most
`s^4||R_a||4^2/(4m^2)<=16s^4/m^2`. Thus, with

\[
 B_2(R)=4+{22\over m}+{2R+16\over m^2},
 \tag{7.9}
\]
\[
 \|H^2_a(s)-H^2_a(0)-{y_as^2\over2m}\phi'(Y_a)R_a\|_2
 \le {2\tau_R(P_a)\over m}s^2+B_2(R)s^4.
 \tag{7.10}
\]

We also preserve nonaffinity on the **visited preactivation law** at the
same time. For any real square-integrable random variable define

\[
 N(Z)=\inf_{a,b\in\mathbb R}E|\tanh Z-aZ-b|^2.
 \tag{7.10a}
\]

If `Var(Z)>0`, first minimizing over `b` and then completing the square
in `a` gives

\[
 N(Z)=\operatorname{Var}(\tanh Z)
       -{\operatorname{Cov}(Z,\tanh Z)^2\over\operatorname{Var}(Z)}.
 \tag{7.10b}
\]

For a standard Gaussian `G` and `sigma>0`, this formula attains the
minimum. Therefore `N(sigma G)>0`: otherwise its zero error gives an
affine identity for tanh almost surely on a Gaussian of full support;
continuity extends that identity to every real number. A bounded
nonconstant tanh cannot be affine on the entire real line. Define the
positive initialization constants

\[
 \nu_* =\min\{N(G),N(\sqrt qG)\}>0,\qquad
 \epsilon_*={\sqrt q\,\nu_*\over64}>0.
 \tag{7.10c}
\]

These are explicit one-dimensional Gaussian integrals through (7.10b).
In particular `nu_*<=1`, since choosing the zero affine function bounds
each error by one. No trained distribution is used to choose them.

Here is a quantitative continuity estimate, including control of the
denominator. Suppose `X~N(0,sigma^2)`, `0<sigma<=1`, and a variable `Z`
on the same space satisfies `epsilon=||Z-X||2<=sigma/2`. Centering is an
orthogonal projection in `L2`, hence a contraction. Write
`s_Z=sqrt(Var(Z))`, `V_Z=Var(Z)`, and
`C_Z=Cov(Z,tanh Z)`, with analogous notation for `X`. The one-Lipschitz
activation and its supremum bound one give

\[
 |s_Z-\sigma|\le\epsilon,\quad
 |V_Z-\sigma^2|\le(2\sigma+\epsilon)\epsilon,\quad
 V_Z\ge(\sigma-\epsilon)^2\ge\sigma^2/4,
 \tag{7.10d}
\]
\[
 |\operatorname{Var}(\tanh Z)-\operatorname{Var}(\tanh X)|
       \le2\epsilon,\quad
 |C_Z-C_X|\le(1+\sigma)\epsilon,\quad
 |C_Z|\le\sigma+\epsilon,\quad |C_X|\le\sigma.
 \tag{7.10e}
\]

For example, to bound the covariance difference, subtract the centered
first factor first, pair it with centered `tanh Z` of norm at most one,
then pair centered `X` of norm `sigma` with the centered activation
difference of norm at most `epsilon`. Consequently

\[
 \begin{aligned}
 |N(Z)-N(X)|
 &\le 2\epsilon+
 { |C_Z^2-C_X^2|\over V_Z}
 +{ C_X^2|V_Z-\sigma^2|\over V_Z\sigma^2}\\
 &\le2\epsilon+
 {(2\sigma+\epsilon)(2+\sigma)\epsilon\over(\sigma-\epsilon)^2}
 \le {32\epsilon\over\sigma}.
 \end{aligned}
 \tag{7.10f}
\]

For the last inequality use `epsilon<=sigma/2`, so the fraction is at
most `10(2+sigma)epsilon/sigma`; then use `sigma<=1` and
`2epsilon<=2epsilon/sigma`. If `sigma` is either `1` or `sqrt(q)` and
`epsilon<=epsilon_*`, (7.10c) ensures `epsilon<=sigma/2` and proves

\[
 \operatorname{Var}(Z)\ge q/4,\qquad N(Z)\ge\nu_*/2>0.
 \tag{7.10g}
\]

Choose, entirely from initialization constants,

\[
 R_m={128\over\alpha_m},\quad
 s_0=\min\left\{\frac12,
            \sqrt{\frac{\alpha_m}{4B_2(R_m)}},
            \sqrt{\frac{\epsilon_*}{4}}\right\}>0.
 \tag{7.11}
\]

Then (7.2) gives `2 tau_R(P_a)/m <= alpha_m/4`, and
`B_2(R_m)s^2<=alpha_m/4` for `s<=s_0`. Since `B_1<=B_2`,
(6.8), (7.8), and (7.10) prove, for every anchor and both layers,

\[
 \|H^\ell_a(s)-H^\ell_a(0)\|_2\ge\tfrac12\alpha_m s^2
 \qquad(0<s\le s_0,\ \ell=1,2).
 \tag{7.12}
\]

Before the fitting level, `0<=b(s)<=s` since `||c||2<=s` and
`||h||2<=1`. The physical clock therefore obeys
`1-e^{-2t}<=s(t)<=2t`. Set the explicit physical time and margin

\[
 t_{\rm act,m}=s_0/2>0,\qquad
 \delta_{\rm act,m}=\alpha_m s_0^2/8>0.
 \tag{7.13}
\]

At this time `s(t)<=s_0` and
`s(t)>=1-e^{-s_0}>=s_0/2`. The latter elementary inequality follows
from `e^{-a}<=1-a+a^2/2` for `0<=a<=1`. Consequently

\[
 D_{\ell,*}(t):=\left\{{1\over m}\sum_a
      E_\ell|H^\ell_a(t)-H^\ell_a(0)|^2\right\}^{1/2},
 \qquad D_{\ell,*}(t_{\rm act,m})\ge\delta_{\rm act,m}>0.
 \tag{7.14}
\]

These are paired initial/current observations on the same coordinate
population. They are not distances between separately sampled marginal
laws. The time and lower bound are uniform over all `2^m` binary patterns
and do not depend on `d>=m`. No assertion of displacement at `T_m` is
needed. In particular the positive small-time statement and the fitting
statement concern the same strong reference trajectory.

For every `0<=s<=s_0`, (7.4)--(7.5) give
`||w_a(s)-g_a||2<=5s^2/(4m)<=4s_0^2<=epsilon_*` and
`||Z^2_a(s)-Y_a||2<=4s_0^2<=epsilon_*`. Thus (7.10g), applied to the
paired initial/current variables, gives for **every** anchor

\[
 \operatorname{Var}(Z^\ell_a(t_{\rm act,m}))\ge q/4,\qquad
 N(Z^\ell_a(t_{\rm act,m}))\ge\nu_*/2>0,
 \quad a\le m,\quad\ell=1,2.
 \tag{7.15}
\]

The same bounds hold for `0<=t<=t_act,m`, since `s(t)<=2t<=s_0`.
In particular (7.14) and (7.15) establish actual paired learning and
nonaffinity on the distributions visited at the **same** positive time.
Shrinking `s_0` to obtain this statement preserves every preceding
activity estimate and leaves the learning horizon `T_m=5m` unchanged.

## 8. Finite GF, whole-sphere identification, and actual raw GD

For clarity the two discretizations are different: `Delta` is an
auxiliary proof mesh for a fixed Gaussian program; `eta_n` is the actual
optimizer step, applied to the raw finite weights.

### Finite GF and its population identification

At finite width use the same clock representation as (2.8), replacing
population contractions by normalized pairings. For the physical equations
the chart is

\[
 \dot X_{n,a}=-{2\over m}r_{n,a}A_n^TD_{n,a},\quad
 \dot A_n=-{2\over mn}\sum_a r_{n,a}D_{n,a}(h^1_{n,a})^T,\quad
 \dot c_n=-{2\over m}\sum_a r_{n,a}h^2_{n,a},
 \quad D_{n,a}=c_n\odot\phi'(z^2_{n,a}).
 \tag{8.1}
\]

The finite residuals are not replaced by the symmetric population value.
The exact finite identities give loss decrease; alternatively the following
coarser bounds suffice for both GF and raw GD. If `M=||c_n||infty`, then
`|r_{n,a}|<=1+M`, and the readout update/integral inequality gives, on
every fixed `[0,T]`, a bound depending only on `T` and `M(0)`:

\[
 1+M(t)\le(1+M(0))e^{2t}
 \tag{8.2}
\]

for GF, and the corresponding discrete bound
`1+M_k<=(1+M_0)(1+2eta_n)^k`. The middle Frobenius/HS increment is at
most the time integral of `2(1+M)M`, and the first row and clock RMS
increments are bounded by the time integral of
`2(1+M)||A_n||op M`. These bounds are uniform in width on the events
`||A_n(0)||op<=3`, `||W1(0)||F/sqrt(n)<=sqrt(d)+1`, and
`||c_n(0)||infty<=1`, whose probabilities tend to one. They imply global
finite GF existence and keep the transformed Lipschitz constants width
independent on every prescribed compact interval.

At fixed `Delta`, expand every middle update into its rank-one factors.
Freeze each residual and contraction to its recursively computed population
value. This yields a fixed finite Gaussian program with the full row roots,
the same initialized matrix and transpose, and finitely many continuous
linear-growth chart instructions. A.1 identifies its joint empirical laws
and contractions. The differences between its prescribed nodes and
recomputations with the corresponding finite proxy matrix are finite sums
of a bounded-RMS factor times a scalar empirical contraction error, hence
vanish in RMS. The transformed Lipschitz comparison then transfers those
limits to finite Euler with its actual empirical residual feedback.

For GF versus this auxiliary Euler scheme, the chart field has a bounded
velocity and a width-independent local Lipschitz constant on the reached
ball. The local error is `C_T Delta^2`, so the recursion
`e_{k+1}<=(1+C_T Delta)e_k+C_T Delta^2` gives `O_T(Delta)` on `[0,T]`.
A first-exit argument uses slightly larger bounds from (8.2) to close the
comparison. First let width tend to infinity at fixed proof mesh; then
remove that mesh. The identical population Euler estimate identifies the
limit with the unique strong population physical flow in section 4.

The actual small finite readout is included. To see explicitly why it does
not change the identified limit, couple it to zero readout on the same
finite first rows and middle matrix. On `||c_n(0)||infty<=1`, chart stability
on `[0,T]` bounds their difference by
`C_T ||c_n(0)||2/sqrt(n)`, which tends to zero in probability. This is a
comparison proving the limit of the specified random-readout algorithm,
not a replacement of that algorithm.

Every fixed finite family of passive inputs and generated forward/adjoint
probes is appended to the same finite program. Bounded-multiplier
continuity, clipping a fixed limiting `L2` factor when necessary, transfers
their joint same-layer laws and second moments. Products whose varying
factors are bounded and Lipschitz are included directly; unbounded
quadratic reverse observations use the same fixed-family clipping and
uniformly vanishing second-moment tails. Compact-time continuity and a
finite time grid give uniform-in-time observation convergence. Hidden
path laws in `W2` for finitely many passive inputs follow from

\[
 {1\over n}\sum_i\sup_{t\le T}
 |z_{n,i}(t)-z_{n,i}(\pi_h t)|^2
 \le h\int_0^T{\|\dot z_n(t)\|_2^2\over n}\,dt,
 \tag{8.3}
\]

and the population counterpart. The strong equations and the bounds just
proved bound the integrated squared speeds. Joint tuples include time
zero, so the paired quantities (7.14) are among the converging observables.

At finite width,

\[
 |f_n(t,\sqrt d\,u)-f_n(t,\sqrt d\,v)|
 \le {\|c_n(t)\|_2\over\sqrt n}\|A_n(t)\|_{\rm op}
       {\|W1_n(t)\|_F\over\sqrt n}|u-v|.
 \tag{8.4}
\]

The right-side coefficient is bounded in probability uniformly on `[0,T]`.
Use the proved time-uniform prediction limit on each finite net of the
compact sphere, (8.4), and (5.5), then refine the net. This proves

\[
 \sup_{t\le T,\ u\in S^{d-1}}
       |f_n(t,\sqrt d\,u)-f_*(t,\sqrt d\,u)|\longrightarrow0
 \quad\hbox{in probability}.
 \tag{8.5}
\]

There is no claim here that arbitrary nonlinear observables of a whole
continuum-indexed hidden path are controlled by a finite passive list.
The declared hidden/action observations are finite joint generated probes
and their limits as their fixed input arguments vary in `L2`; prediction
has the stronger whole-sphere uniform topology (8.5).

### Exact raw-GD bridge and its sufficient step condition

In a raw first-coordinate step write

\[
 z^+=z+\eta\phi'(z)b,\qquad
 b=-{2\over m}r_{n,a}(A_n^TD_{n,a})_i.
 \tag{8.6}
\]

If `2 eta |b|<=1/2`, the gate along the segment differs from its starting
value by at most half that value, because `Lip(phi')<=2`. Since the tanh
gate is positive, define the exact chart increment
`Delta X=int_z^{z+}du/phi'(u)`. Substitution along the segment proves

\[
 z^+=j(\Delta X,z),\qquad
 |\Delta X-\eta b|\le2\eta^2b^2.
 \tag{8.7}
\]

The raw iterates themselves have the bounds (8.2): readout first, then
middle increment, then row RMS and clocks. On the same high-probability
initialization events these imply

\[
 {\|b_a\|_2\over\sqrt n}\le C_T,\qquad
 \|b_a\|_\infty\le\|b_a\|_2\le C_T\sqrt n.
 \tag{8.8}
\]

Therefore `eta_n sqrt(n)->0` enforces the scalar condition in every
coordinate through the whole fixed horizon. The RMS clock defect per
step is at most

\[
 2\eta_n^2\left({1\over n}\sum_i b_{a,i}^4\right)^{1/2}
 \le2\eta_n^2\|b_a\|_\infty{\|b_a\|_2\over\sqrt n}
 \le C_T\eta_n^2\sqrt n.
 \tag{8.9}
\]

The exact lifted clocks are bounded by the sum of their leading increments
and these defects, giving `C_T(1+eta_n sqrt(n))`; hence they stay in a
common Lipschitz ball. Middle and readout updates are already Euler
updates for (8.1). Comparing the lifted raw iterates with finite GF adds
only the ordinary `C_T eta_n^2` local flow defect. The stable recurrence
therefore yields

\[
 \sup_{t\le T}d_n(\hbox{lifted raw GD},\hbox{finite GF})
 \le C_T(\eta_n+\eta_n\sqrt n)\longrightarrow0,
 \tag{8.10}
\]

where `d_n` is the sum of active clock RMS, middle increment Frobenius,
and readout RMS distances. Linear raw interpolation and the corresponding
chart segment have the same vanishing error; forward quantities are
recomputed from linearly interpolated raw weights. The passive coordinates
of the first row stay fixed in both algorithms. Thus (8.10), followed by
the already identified GF limit, proves (8.5) and the fixed joint hidden /
action / paired limits for actual raw GD. The growing optimizer transcript
is never treated as one fixed finite Gaussian program.

In particular, for both algorithms the final finite risk converges to a
value below `1/16`, and each paired activation RMS at `t_act,m` converges
to a value at least `delta_act,m`. Hence finite risk is below `1/16` and
both paired RMS values exceed `delta_act,m/2` with probability tending to
one. The empirical best-affine-fit errors at the same activity time also
converge to (7.15): the `W2` preactivation limit supplies the means and
second moments in (7.10b), the bounded Lipschitz activation supplies its
moments and cross moment, and the limiting variance is at least `q/4`.
Thus all `2m` empirical variances exceed `q/8` and empirical nonaffinity
errors exceed `nu_*/4` with probability tending to one. This concerns
every separately fixed `m,d`, not a simultaneous
growing-data limit. The GD step condition is sufficient, not asserted
necessary and not silently replaced by the weaker `eta_n->0`.

## 9. Claim boundaries and hostile checks

The proved claim ladder in this file is: exact raw/feature identities;
global strong reference existence and restart; deterministic action-law
symmetry; fitting and strong endpoint with explicit finite-horizon risk;
strict paired activation motion and visited-law nonaffinity at the same
time; finite GF identification and the stated
raw-GD bridge. There is no empirical rung: no training was run.

Checks against the plausible failure modes:

1. **Mixed-label asymmetry.** Plain permutations need not preserve a mixed
   label pattern. The exact signed permutations (3.1)--(3.3) do, and
   zero population readout plus Gaussian row invariance supply their
   initialization symmetry. No finite path is assumed symmetric.
2. **Mean/sum clock mismatch.** The feature average and each hidden block
   contain `1/m`, while the physical clock is exactly `s_t=2(1-b)`.
   The rate is `4v/m` for risk; the learning horizon is `5m`.
3. **One-anchor degeneracy.** Equation (3.4) is an identity for `m=1`;
   the activity lower bound uses `d_0`, not `(m-1)vr_0`. The discrete
   sphere at `d=1` is explicitly distinguished.
4. **A fresh-transpose surrogate.** Equations (6.4)--(6.5) condition the
   same Gaussian matrix in both orientations and keep both response
   terms. The upper-layer positivity uses an identified remaining
   Gaussian variance, not an unjustified independence assumption.
5. **Gate suppression.** Both leading coefficients are activation
   coefficients, and the explicit remainders prove (7.14) for the
   actual solution at a fixed physical time. The quantitative centered
   moment comparison (7.10d)--(7.10g) simultaneously proves a positive
   best-affine-fit error on each visited preactivation law, so global
   nonlinearity of tanh is not substituted for distributional nonaffinity.
6. **Projection onto active training coordinates.** The full row includes
   the fixed passive Gaussian coordinates. Their passive forward fields
   use the same learned action, and (8.4)--(8.5) cover the entire sphere.
7. **Raw-ball regularity or a false transformed optimizer.** Well-posedness
   uses a scalar coordinate valid for orthogonal anchors; raw GD is
   lifted with the explicit nonzero defect (8.7)--(8.10). No ambient raw
   Lipschitz estimate and no exact transformed-Euler identity is assumed.
8. **An existence proof mistaken for nearby-law continuation.** Only the
   exact orthogonal reference is proved here. Establishing an open
   nonorthogonal family requires the separate reached-source/tail and
   comparison argument, through the same horizon. The finite observable
   hierarchy also remains outside this file's assertion.

No reference-component obstruction remains in this candidate. The
remaining C-X1 obligations are the perturbed-law construction/identification
and compatible finite closure, followed by independent review of the
assembled complete theorem. The constants given here are deliberately
conservative and establish positivity and finite horizons, not practical
accuracy or complexity rates.
