# Evaluating and separating the actual tanh constants

2026-10-04. Scoped continuation of this study. This candidate is conditional
on the same local Gaussian insertion, source continuation and autonomous
corrected-readout interfaces as its inputs. It changes neither the reference
network nor the optimizer. It is not a promotion review. The only computation
is evaluation of deterministic recurrences; the complete evaluator and inputs
are retained below. No other study, maintained book, manuscript or Git state
was accessed or modified.

The old tanh coefficients `16^(-62L)`, `16^(124L)` and `16^(82Ld)` are
very loose envelopes. Directly evaluating them is useful, but three additional
separations produce a larger gain:

1. A source coordinate error of `epsilon` has multiplier one, even though
   the carrier maximum has a much larger multiplier. Only the latter enters
   the width-dependent comparison exponent.
2. Learned query corrections contain the square of the activity allowance.
   Keeping that square removes their large endpoint-trace constants from
   the leading query-radius coefficient.
3. The time pole displacement contains `Y S`. Keeping it makes the time
   radius independent of depth after one explicit, dimension-independent
   label restriction already implied by the old label assumption.

For tanh the resulting leading storage coefficient has depth growth
`(64/15)^(2(L-2)(d-1))`, multiplied by the explicit numerical and
dimension factors below, in place of `16^(82Ld)`. This is a substantial
reduction for full-rank data. The remaining numerical constants are still
large; this is not a theorem giving practical or polynomial-in-depth-and-
dimension storage.

## 1. Contract and scientific inputs

The complete scientific inputs read are
`INPUT_DIMENSION_REFINEMENT.md`, `ARCHITECTURE_CONSTANT_REFINEMENT.md`,
`LABEL_DEPTH_RESCALING_ROUTE.md`, `DEPTH_CONSTANT_SEPARATION.md`,
`EXPLICIT_SOURCE_CONSTANTS_ROUTE.md`,
`EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md`,
`SPHERICAL_SOURCE_DIMENSION_ROUTE.md`, and their current-study dependencies
`EXPLICIT_LABEL_CONSTANTS_ROUTE.md` and `DATASET_LABEL_DEPENDENCE.md`.
Their references to other studies were not followed. The canonical-notation
and neural-network instructions, rigorous-proof skill, and research-contract,
evidence and adversarial-audit instructions were applied.

For unit input `v=x/sqrt(d)`, the canonical dense width-`n` network is
\[
 z^{(1)}=Av,\qquad z^{(j)}=W^{(j)}h^{(j-1)},\qquad
 h^{(j)}=\tanh z^{(j)},\qquad f_n=w^\top h^{(L)}/n.
\]
All hidden layers have width `n`; `L>=2`. The first matrix has independent
`N(0,1)` entries, the hidden mixers have independent `N(0,1/n)` entries,
all initialized blocks are independent, and `w(0)=0`. There are `m` fixed
unit training inputs. With `r_a=f_n(v_a)-y_a`, define
\[
 k_a^{(L)}=w,\qquad
 \delta_a^{(j)}=\tanh'(z_a^{(j)})\odot k_a^{(j)},\qquad
 k_a^{(j)}=W^{(j+1)\top}\delta_a^{(j+1)}.
\]
The loss is `m^(-1) sum_a r_a^2`, and physical-time mobilities remain
`(n,1,...,1,n)`, so
\[
 \dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\quad
 \dot W^{(j)}=-\frac2{mn}\sum_a r_a\delta_a^{(j)}h_a^{(j-1)\top},\quad
 \dot w=-\frac2m\sum_a r_a h_a^{(L)}.
\]
Let `Q^(0)_ab=v_a^T v_b`, and recursively
`Q^(j)_ab=E[tanh(Z_a)tanh(Z_b)]` for `Z~N(0,Q^(j-1))`. Write
\[
 \gamma=\lambda_{\min}(Q^{(L)})>0,\qquad
 \lambda=\gamma/m,\qquad Y=\|y\|_2/\sqrt m,\qquad
 \ell_n=\log(en).
\]
Here the old cap `min(1,gamma/m)` is inactive: `|tanh|<=1` on the
real axis implies `gamma<=1` and `gamma/m<=1`. Labels may have arbitrary
signs. Zero labels are handled by the exact stationary zero predictor.

Every claim is for fixed architecture and fixed data, at any fixed
confidence for sufficiently large width. The stochastic width threshold,
exact-real preprocessing cost and numerical precision remain unquantified.
The error is strictly `C/sqrt(n)`, uniform over all physical times,
including the fitted endpoint, and all unit sphere queries against the
same realized dense initialization. No data-rank assumption is added.

## 2. Certified tanh bounds and smaller elementary operator caps

Use the outer strip width and safe-strip bounds
\[
 a=\tfrac12,\qquad B=1,\qquad s=\tfrac{16}{15},\qquad t=1.
 \tag{1}
\]
These mean `|tanh z|<=B` on `|Im z|<a`, and first and second derivative
bounds `s,t` on `|Im z|<=a/2`. To verify them, put `u=sinh^2(x)` and
`b=sin^2(y)` for `z=x+iy`. Then
\[
 |\tanh z|^2=\frac{u+b}{u+1-b},\quad
 |\tanh' z|=\frac1{u+\cos^2y},\quad
 |\tanh''z|^2=\frac{4(u+b)}{(u+1-b)^3}.
\]
For `|y|<1/2<pi/4`, the first ratio is at most one. For `|y|<=1/4`,
`cos y>=1-y^2/2>=31/32`, so the first derivative is at most
`1024/961<16/15`. Maximizing the last expression over `u>=0`, with
`b<=sin^2(1/4)<1/4`, gives
\[
 \sup_x|\tanh''(x+iy)|=\frac4{3\sqrt3\cos(2y)}<1.
\]
Indeed `cos(2y)>=7/8`, and `32/(21 sqrt(3))<1`. Thus (1) is
certified without a generic Cauchy derivative loss. On the real line all
three norms `|tanh|, |tanh'|, |tanh''|` are at most one. The runtime
activation norm is consequently exactly bounded by `B_rt=1`.

The initialized hidden-operator cap can be reduced from eight to `7/2`
using an elementary one-sphere net. A `1/8`-net of the unit sphere has
at most `17^n` points by the disjoint-ball volume argument. For any matrix
`W`, its operator norm is at most `8/7` times its largest image norm on
that net. For fixed unit `u`, `n||W_0 u||^2` has the chi-square law with
`n` degrees of freedom. Its elementary moment-generating function gives,
for `q>1`,
\[
 \Pr\{\|W_0u\|^2\ge q\}
 \le\exp[-n(q-1-\log q)/2].
\]
This follows by applying Markov's inequality to
`exp(theta n||W_0u||^2)` and choosing `theta=(1-1/q)/2`.
For `q=(49/16)^2=2401/256`,
\[
 (q-1-\log q)/2>3.0702>\log17.
 \]
Only positivity of this gap is needed: `log q<7/3` and `log17<3`
give `(q-1-log q)/2>4643/1536>3`; the logarithmic bounds follow
from `q<10<exp(7/3)` and `17<exp(3)`, each verified by a finite
positive Taylor sum for the exponential.
The union bound therefore proves `||W_0||<7/2` with probability tending
to one. Fixed-size rectangular cavities obey the same bound by restriction.

For the normalized first matrix, a `1/4`-net of the fixed-dimensional
input sphere has at most `9^d` points. The same calculation at image
threshold `3/2` proves `||A_0||/sqrt(n)<2` with probability tending to
one. Use real and complex hidden tubes
\[
 R_{\rm real}=15/4,\qquad R_{\rm complex}=4.
 \tag{2}
\]
The real fitting proof gives hidden displacement at most `1/4`, with a
strict margin because the initialized cap is strict. The source activity
condition below gives normalized first-matrix displacement at most `1/2`.
Short complex continuation then leaves `||A||/sqrt(n)<3` and hidden
operator norm below four eventually. Hence the query RMS derivative starts
at six: its input derivative norm is at most two. These are changes to
proved initialization/tube bounds, not to the Gaussian initialization.

## 3. Actual finite source and label recurrence

The source recurrence is the one in `LABEL_DEPTH_RESCALING_ROUTE.md`,
with complex propagation ten replaced by four, real propagation nine
replaced by `15/4`, and the certified numbers (1). For completeness all
constants needed later are specified here. Set
\[
 K_j=2B(4s)^{L-j},\quad P_1=2,\quad
 P_j=B+4sP_{j-1}+1,
\]
\[
 A_H=2sP_L+2s^2\sum_{j=2}^LK_jP_{j-1}+tP_L^2K_L,
 \quad D_H=t\sum_{j<L}P_j^2,
\]
\[
 H_2=2sP_L+2s^2\sum_{j=2}^LK_jP_{j-1}
                  +t\sum_{j=1}^LP_j^2K_j,
\]
\[
 E=t\sum_{j=1}^L(4s)^{2(j-1)}K_j,
\]
\[
 D_0=\max\{1,B[2H_2^2+4A_H^2(e^2-1)+E]+Bs^2\max_jK_j^2\},
 \quad D_1=576e^3BD_H^3.
\]
Define activity-modulus coefficients by
\[
 V_1=sK_1,\quad V_j=B^2sK_j+4sV_{j-1},\quad
 G_L=sB+2BtV_L,
\]
\[
 G_j=4sG_{j+1}+Bs^3K_{j+1}^2+14tV_j+s,\quad
 G=\max(1,G_1,\ldots,G_L).
\]
The budget parameters and activity cap are
\[
 \eta=\min\{1,B^{-1},D_0^{-1},(128G)^{-1}\},\quad
 \mathcal B=64e^2L,\quad
 \Lambda=\log(e+\mathcal B)+\log(1/\eta),
\]
\[
 S_*=\min\left\{1,\frac1{4A_H},
 \sqrt{\frac\eta{4000D_H}},
 \sqrt{\frac\eta{16eD_H\sqrt{2\mathcal B}}},
 \sqrt{\frac\eta\Lambda},
 \left(\frac{\eta^2}{D_1\mathcal B}\right)^{1/4},
 \frac1{\sqrt{2sK_1}}\right\}.
 \tag{3}
\]
For real fitting put
\[
 b_j=s((15/4)s)^{L-j},\quad F_1=sb_1,\quad
 F_j=s[B^2b_j+(15/4)F_{j-1}],\quad
 C_*=\max(1,B^2b_1,F_L),
\]
\[
 c_{\rm src}=\min\{(8\sqrt{C_*})^{-1},S_*/16\}.
 \tag{4}
\]
The source proof then applies whenever `Y/lambda<=c_src`, with
`S=16Y/lambda`, `T=32 lambda^(-1) ell_n`, source coordinate error
`epsilon=n^(-1)`, and true carrier maximum
\[
 \max|k|\le K_{\rm src}S\sqrt{\ell_n},\qquad
 K_{\rm src}=32\max(1,\max_jK_j,\max_jsK_j).
 \tag{5}
\]
Nothing in the stopped Hessian, Dyson-series, tail-split or fixed-order
common-cavity argument uses eight, nine or ten except as the indicated
operator bounds. All inequalities are monotone in them. The first-weight
condition in (3), the displacement calculation in Section 2, and the new
net proof supply precisely the smaller physical tubes. The rescaled
budget, its logarithm `log(1/eta)`, and every nonvanishing smallness condition
are retained. This is the complete justification for substituting (1)-(2).

For the query response endpoints, define
\[
 f_j=sP_j,\quad t_j=sK_j,\quad
 g=t_1+B\sum_{j=2}^Lt_j,\quad r_j=P_jg,\quad q_j=f_jg,
\]
\[
 e_1=tr_1P_1,\quad
 e_j=tr_jP_j+s(q_{j-1}+t_jBf_{j-1}+4e_{j-1}),
\]
\[
 j_j=6(4s)^{j-1},\quad b_j^{\rm qry}=sj_j,\quad
 a_1=tj_1P_1+2s,\quad
 a_j=tj_jP_j+s(b_{j-1}^{\rm qry}+4a_{j-1}),
\]
\[
 T_Q=8\max_jf_j\max_j(f_jH_2+e_j),\qquad
 T_J=8\max_jf_j\max_ja_j.
 \tag{6}
\]
The duplicate letter `b` is disambiguated: `b_j` in (4) is a real fitting
coefficient, whereas `b_j^qry` in (6) is a passive query derivative RMS
coefficient. The numerical evaluator uses separate variables.

## 4. Runtime: source error and carrier maximum are different constants

The source construction approximates **each member** of each paired action
with coordinate error at most `epsilon`, not `K_src epsilon`. Thus its
error multiplier is one. The initialized mixers have cap `K_0=7/2`, and
(5) gives the direct runtime carrier statement
\[
 M\le1+16K_{\rm src}(Y/\lambda)\sqrt{\ell_n}.
 \tag{7}
\]
All occurrences of `K` in the runtime recurrence except its carrier
exponent arose from coordinate-error transfer or initialized operator
norm. They must be separated. Use `B_rt=1`, `h=g=2`, `R=15/4`, and
\[
 \beta_j=2^{L-j+1}R^{L-j},\quad \beta=\max_j\beta_j,
 \quad U=(\beta_1^2+4\sum_{j=2}^L\beta_j^2)^{1/2},
\]
\[
 F_1=2,\quad F_j=2(2+RF_{j-1}),\quad F=\max_jF_j,
\]
\[
 D_\delta=3\beta+3,\quad W=64,\quad
 J_0=2\sqrt L(7\beta+3),\quad V_0=14FU,
\]
\[
 P_h=17,\quad P_\delta=18\beta+11,\quad D_r=8P_h,
\]
\[
 A_0=1+2(K_0+1)+8D_\delta P_h+16P_\delta,
 \quad C_f=F(1+A_0),
\]
\[
 H_0=1+3WC_f+3D_r,\quad
 Z_0=L(2R)^L(D_\delta+A_0+C_f),
\]
\[
 J_1=\sqrt L(2\beta H_0+2Z_0+D_\delta C_f),\quad
 D_{\rm gram}=P_h+L(4P_\delta+9\beta^2P_h),
\]
\[
 F_0=8C_f+24J_0J_1+6D_{\rm gram},\quad T'_0=6V_0,
 \quad G_{\rm rt}=4(T'_0+F_0)+2C_f+2J_1,
\]
\[
 C_1=40G_{\rm rt},\quad C_2=64K_{\rm src}G_{\rm rt},\quad
 O_0=4H_0+WC_f+D_r,
\]
\[
 W_1=4+50V_0+6(4+J_0^2),\quad T_1=2W_1+7V_0,
\]
\[
 c_{\rm rt}=\min\{1,(224FU)^{-1/2},(6J_0)^{-1}\}.
 \tag{8}
\]
These are all the runtime coefficients, with no implicit depth or
dimension dependence. To check the only modified paired-action term,
let `u` and `W_0u` each have source error at most `epsilon`. Transferring
the two errors to the selected space costs at most `2 epsilon` each.
The first is propagated by an initialized compressed operator of norm at
most `K_0`, giving initialized action defect at most
`2(K_0+1)epsilon`. This replaces `2K(K+1)epsilon` in the old `A_0`.
Every other pairing and selected-response estimate uses multiplier one;
in particular `W=32(1+1)`. The coefficient multiplying the actual carrier
term is read directly from (7), giving `C_2=64K_src G_rt`.

The original geometric cancellation is unchanged. If `0<Y/lambda<=c`
and `c<=min(c_src,c_rt)`, it proves
\[
 \sup_{t\in[0,\infty],\,\|v\|=1}|f_C(t,v)-f_n(t,v)|
 \le C_{\rm err}(c)\frac{Y}{\lambda^{3/2}\sqrt n},
 \tag{9}
\]
where
\[
 C_{\rm err}(c)=
 O_0[1+\sqrt e(C_1+C_2c)e^{C_1c+C_2^2c^4}]+8T_1.
 \tag{10}
\]
The coordinate tolerance is still exactly `n^(-1)`. No coefficient has
been removed by asking for a finer source approximation or by moving a
nonvanishing comparison coefficient into the width threshold.

## 5. Query and time radii with activity factors retained

The spherical source's Gaussian grid contains at most `n^(4d+10)`
points eventually. A complex Gaussian pairing of RMS coefficient `sigma`
has tail at most `4 exp[-u^2/(4 sigma^2)]`. Therefore the smaller explicit
grid multiplier
\[
 G_d=4\sqrt{d+3}
 \tag{11}
\]
is sufficient: its exponential contributes `n^(-4d-12)`, leaving
`O(n^(-2))` after the union. Fixed prefactors affect only the threshold.
Off-grid errors are unchanged and tend to zero relative to the strict
caps below. This is a direct check of the grid exponent, not an invocation
of a new stochastic theorem.

Write `b_*=max_{j<L}b_j^qry=6s(4s)^(L-2)`. Define two nonnegative,
dimension-independent time-response coefficients
\[
 A_U=\max\left\{4sK_{\rm src},\
 \max_{2\le j\le L}2[sK_{\rm src}(B^2+f_{j-1}^2+T_Q+Bq_{j-1})+1]
 \right\},\quad B_U=\max_{j<L}2q_j.
 \tag{12}
\]
The old, deliberately loose time-response formula therefore gives
`U_*<=A_U+B_U G_d`. For angular responses, the actual formula is sharper:
\[
 V^{\rm qry}_1=2(2G_d+2sK_{\rm src}S^2+1),
\]
\[
 V^{\rm qry}_j=
 2\{G_db_{j-1}^{\rm qry}
     +sK_{\rm src}S^2(T_J+Bb_{j-1}^{\rm qry})+1\},\quad j\ge2.
 \tag{13}
\]
To derive the square in (13), the same-root integral has one activity
factor `S` and a training carrier factor `K_src S sqrt(ell_n)`.
The learned-row term has exactly the same factors. The inherited trace
coefficients `T_J` have already removed their endpoint normalizations;
there is no inverse `S` in them. At layer one the learned first row is
an activity integral of the training response, again supplying `S^2`.
The original source derivation states these contributions before replacing
`S<=1`. Reinstating their factors changes no source or insertion identity.

Choose dimension-independent restrictions
\[
 c_{\rm ang}=
 [16\sqrt{sK_{\rm src}\max(2,T_J+Bb_*)}]^{-1},\qquad
 c_{\rm time}=\sqrt{\frac a{1024(A_U+B_U)}}.
 \tag{14}
\]
If `Y/lambda<=c<=min(c_ang,c_time)`, then `S=16Y/lambda<=16c` and
\[
 2sK_{\rm src}S^2\le1,\quad
 sK_{\rm src}S^2(T_J+Bb_*)\le1,\quad
 128c^2(A_U+B_U)\le a/8.
\]
It follows from `b_*>=2` that every query-response coefficient in (13)
is at most `2G_d b_*+4`. Take the explicit radii
\[
 c_t=G_d^{-1},\qquad
 c_q=\frac a{16G_db_*+32},\qquad
 r_t=c_t/\sqrt{\ell_n},\quad r_q=c_q/\sqrt{\ell_n}.
 \tag{15}
\]
For `d>=2`, `G_d>8`, so both coefficients are at most `1/8`. The time
rectangle has horizontal extension `r_t` on both ends and vertical
half-width `r_t`; the query domain is the intrinsic complex sphere tube.
Along both short time pieces and then the complex great-circle segment,
the preactivation displacement is at most
\[
 8c_tYSU_*+c_qV_*
 \le128c^2(A_U+B_U)+a/8\le a/4.
 \tag{16}
\]
Here `YS=16Y^2/lambda<=16c^2` since `lambda<=1`, and
`(A_U+B_U G_d)/G_d<=A_U+B_U`. The final value `a/4` is strictly
inside the safe strip `|Im z|<=a/2`. Increasing the pole margin allowance
from the old `3a/128` to `a/4` is legitimate: all derivatives used above
were certified on the entire safe strip. The small-contour remainder,
negative-real propagator and Gaussian correction still vanish, because
the widths remain fixed coefficients times `ell_n^(-1/2)`. They change
their eventual threshold only. All stopped response estimates still
precede the improved pole bound (16), so there is no analytic-continuation
circularity.

## 6. Complete label, error and retained-size statement

A convenient jointly sufficient cap keeping the comparison exponential
at most `e^2` is
\[
 c_L=\min\{c_{\rm src},c_{\rm rt},C_1^{-1},C_2^{-1/2},
                         c_{\rm ang},c_{\rm time}\}.
 \tag{17}
\]
This is a specified finite recurrence in `L` alone. One can omit the two
comparison-exponential restrictions and retain the exact larger value in
(10); doing so generally makes that error coefficient enormous. Neither
option changes the model. Under `Y<=c_L gamma/m`, (9)-(10) hold with
`lambda=gamma/m` and the radii (15).

The previous label condition `Y<=(gamma/m)16^(-62L)` implies (17).
Here is a check using only previously proved envelopes, rather than
floating-point observations. The new `B,s,t,R_real,R_complex` are no
larger than the old tanh values `2,2,4,9,10`, so monotonicity of the
positive recurrences gives `c_src>=16^(-32L)` and at least the old
runtime margins. The old runtime bounds give `C_1<=16^(57L)` and
`C_2<=16^(55L)`; source/error separation only decreases these expressions.
For (14), the old source table bounds `K_src<=16^(4L)`,
`T_J<=16^(14L)`, and `b_*<=16^(4L)`, so
`16 sqrt(s K_src max(2,T_J+B b_*))<=16^(12L)` for `L>=2`.
For the second restriction, `A_U+B_U` is at most twice the old `U_*`
evaluated at `d=2` with `G_d=8 sqrt(5)>1`, hence at most
`2*16^(30L) sqrt(5)`.
Thus `sqrt(1024(A_U+B_U)/a)<=16^(17L)`. In particular
`c_L>=16^(-60L)` is a common conservative bound. The old `16^(-62L)`
condition is preserved with room to spare.

Let `R_src` denote source-space rank, distinct from the operator tube
`R` in (8). For `d>=2`, the exact spherical count is still
\[
 R_{\rm src}\le4N+2m+d+1,\qquad
 N=\sum_{0\le j\le H/r_q}h_j
       \left(1+\left\lfloor\frac{H-r_qj}{\alpha}\right\rfloor\right),
 \tag{18}
\]
where `h_j=binom(j+d-1,d-1)-binom(j+d-3,d-1)`,
`alpha=c_t lambda/(128 ell_n^(3/2))`, and the explicit `H` is defined
by the spherical source tail calculation. More explicitly, put
\[
 D_d=2^{d+1}d^{d-2},\quad b_d=2d-2,\quad
 M_n=M_0\sqrt n,\quad M_0=8\max(B,\max_jsK_j),
\]
\[
 P=\frac{18D_d\,b_d!\,2^{b_d+1}}
                 {\alpha r_q^{b_d+1}},\qquad
 H=2\log(16M_nP/\epsilon),\qquad \epsilon=n^{-1}.
 \tag{19}
\]
`D_2=8`, in agreement with this formula. The same explicit logarithmic
thresholds as in the spherical source proof give
\[
 R_{\rm src}\le A_n+2m+d+1,\qquad
 A_n=\frac{1024\,9^dG_d}{d!}
       \left(\frac{16G_db_*+32}{a}\right)^{d-1}
       \lambda^{-1}\ell_n^{3d/2+1}.
 \tag{20}
\]
No inverse-radius coefficient has been absorbed into a width threshold.
Only fixed coefficients inside the tail logarithm and its lower-order
`log log n` terms are handled there, exactly as in the previous count.
All coefficient construction uses finitely many initial derivatives,
temporary quadratures, and identical scalar operations on paired source
members. None of those temporary objects remains at runtime.

The complete retained-coordinate inventory is consequently
\[
 \operatorname{size}(C)\le
 2040(L+1)A_n^2+2040(L+1)(2m+d+1)^2+10m(d+1).
 \tag{21}
\]
This counts moving variables, fixed mixers, neuron metrics, data and
solve caches. For tanh, (20) gives the convenient explicit envelope
\[
 A_n\le
 \frac{4096\,9^d}{d!}
 \left[\frac{4096}{5}(64/15)^{L-2}+32\right]^{d-1}
 (d+3)^{d/2}\frac m\gamma\ell_n^{3d/2+1}.
 \tag{22}
\]
Indeed `b_*=(32/5)(64/15)^(L-2)`, `a=1/2`,
`G_d=4 sqrt(d+3)`, and `64<=32 sqrt(d+3)`. Squaring (22) shows
the stated depth growth `(64/15)^(2(L-2)(d-1))`; the entire coefficient
is displayed, including its large numerical base. The factorial dimension
factor remains `(d+3)^d/(d!)^2<=25/4`. No low-rank folding is used.

For `d=1` there are two queries and no angular radius. The same time
argument uses `G_1=8`, `c_t=1/8`. The previously derived time-only count
gives `R_src<=8(514/c_t)lambda^(-1)ell_n^(5/2)+2m+2`, with no
depth factor in its leading coefficient. Formula (21) applies with that
time-only leading term. This avoids treating the two-point sphere as one
query.

## 7. Deterministic evaluations and their meaning

The following values are rounded evaluations of the exact displayed
recurrences. They are diagnostics, not certified floating-point upper
bounds; the theorem uses the formulas themselves. The ordinary double
precision evaluator below was run once at each stated depth. It is not a
training experiment or evidence for the stochastic interfaces.

| Hidden depth | `c_src` | joint cap `c_L` | `C_err(c_L)` |
| ---: | ---: | ---: | ---: |
| 2 | 2.858e-7 | 4.756e-16 | 1.644e24 |
| 3 | 1.138e-9 | 1.031e-19 | 4.181e29 |
| 5 | 3.567e-14 | 6.004e-27 | 2.264e40 |
| 10 | 2.810e-25 | 8.699e-45 | 8.798e66 |
| 20 | 2.091e-47 | 3.721e-80 | 6.523e119 |

At depth two the previous label and error envelopes were approximately
`10^(-149.31)` and `10^(298.62)`. The new finite coefficients are
much smaller, but even `1.6e24` is a poor practical error constant.
The source cap alone must not be advertised as the full usable cap with
a moderate comparison coefficient.

For illustration, compare the base-ten logarithm of the leading storage
coefficient multiplying `(m/gamma)^2 ell_n^(3d+2)`. The new column uses
(20)-(21), including `2040(L+1)`; the old column uses precisely the old
`16^(82Ld)(d+3)^d/(d!)^2`. Exact initialization terms are separate in
both statements.

| `L` | `d` | old logarithm | new logarithm |
| ---: | ---: | ---: | ---: |
| 2 | 2 | 395.747 | 21.481 |
| 2 | 10 | 1972.777 | 80.725 |
| 2 | 100 | 19632.911 | 664.714 |
| 5 | 10 | 4934.912 | 114.885 |
| 10 | 100 | 98623.182 | 1662.680 |

The remaining bottleneck is identifiable: the passive-query RMS bound
`b_*=6s(4s)^(L-2)` still propagates the deterministic layer operator
bound at every step. The spectral count then raises its inverse radius to
`d-1` and squares the source rank. Proving a smaller typical query-response
gain, or using a representation that does not pay this spectral count,
would be new scientific work. None of these estimates is a neural lower
bound or an obstruction to other autonomous representations.

## 8. Claim status and hostile checks

The tanh bounds, elementary Gaussian operator event, separated deterministic
runtime constants, retained activity powers and explicit radius algebra are
proved here. The probabilistic construction remains conditional on the
inherited local insertion and continuation interfaces; those have not been
reproved from original cavity sources in this scoped route. No result is
promoted into the maintained book.

The principal audit points are: source error one versus carrier coefficient
`K_src`; the two activity factors in (13); the safe-strip margin after
enlarging the radii; the one-net operator argument and strict real margin;
the dimension-independent extra label caps; and the endpoint term in (10).
All are calculated above. The dense reference, physical clock, optimizer,
source tolerance and observable norm stay fixed. The large remaining
coefficient is disclosed, not hidden in an asymptotic threshold.

The table should not be interpreted as evidence that the runtime inequality
is tight. It is the value of one explicit sufficient proof. In particular
the old beta envelopes are superseded as numerical bookkeeping, while the
strict root-width compression result and its probability quantifiers are
unchanged.

Before this file was frozen, the root agent sent the same observations
about retained query `S^2` and time `Y S` factors. Sections 1--8 above,
including those factors, their proofs, and the numerical tables, had
already been written before those messages arrived. They caused no
mathematical change to this route. This records the communication boundary;
the present author is not claimed to be an independent reviewer of the
shared source theorem or of a later assembled result.

## 9. Reproducible evaluator

The following Python code uses only the standard library. Its complete
inputs are the seven numerical constants on the first line of `evaluate`
and the depth list in the last loop. It mirrors equations (1)-(17).

```python
import math

def evaluate(L):
    a, B, s, t, R0, Rr, Rc = .5, 1., 16/15, 1., 3.5, 3.75, 4.
    K = [2*B*(Rc*s)**(L-j) for j in range(1,L+1)]
    P = [2.]
    for j in range(1,L): P.append(B+Rc*s*P[-1]+1)
    AH = 2*s*P[-1]+2*s*s*sum(K[j]*P[j-1] for j in range(1,L))+t*P[-1]**2*K[-1]
    DH = t*sum(v*v for v in P[:-1])
    H2 = 2*s*P[-1]+2*s*s*sum(K[j]*P[j-1] for j in range(1,L))+t*sum(P[j]**2*K[j] for j in range(L))
    E = t*sum((Rc*s)**(2*j)*K[j] for j in range(L))
    D0 = max(1.,B*(2*H2*H2+4*AH*AH*(math.e**2-1)+E)+B*s*s*max(K)**2)
    D1 = 576*math.e**3*B*DH**3
    V = [s*K[0]]
    for j in range(1,L): V.append(B*B*s*K[j]+Rc*s*V[-1])
    gg = [0.]*L
    gg[-1] = s*B+2*B*t*V[-1]
    for j in range(L-2,-1,-1): gg[j] = Rc*s*gg[j+1]+B*s**3*K[j+1]**2+14*t*V[j]+s
    eta = min(1.,1/B,1/D0,1/(128*max(1.,*gg)))
    budget = 64*math.e**2*L
    Lam = math.log(math.e+budget)+math.log(1/eta)
    Sstar = min(1.,1/(4*AH),math.sqrt(eta/(4000*DH)),math.sqrt(eta/(16*math.e*DH*math.sqrt(2*budget))),math.sqrt(eta/Lam),(eta*eta/(D1*budget))**.25,1/math.sqrt(2*s*K[0]))
    br = [s*(Rr*s)**(L-j) for j in range(1,L+1)]
    Fr = s*br[0]
    for j in range(1,L): Fr = s*(B*B*br[j]+Rr*Fr)
    Cstar = max(1.,B*B*br[0],Fr)
    csrc = min(1/(8*math.sqrt(Cstar)),Sstar/16)
    f = [s*x for x in P]
    tc = [s*x for x in K]
    grad = tc[0]+B*sum(tc[1:])
    rr = [x*grad for x in P]
    q = [x*grad for x in f]
    ee = [t*rr[0]*P[0]]
    for j in range(1,L): ee.append(t*rr[j]*P[j]+s*(q[j-1]+tc[j]*B*f[j-1]+Rc*ee[-1]))
    jq = [6*(Rc*s)**j for j in range(L)]
    bq = [s*x for x in jq]
    aj = [t*jq[0]*P[0]+2*s]
    for j in range(1,L): aj.append(t*jq[j]*P[j]+s*(bq[j-1]+Rc*aj[-1]))
    TQ = 8*max(f)*max(f[j]*H2+ee[j] for j in range(L))
    TJ = 8*max(f)*max(aj)
    Ksrc = 32*max(1.,*K,*tc)
    AU = max(4*s*Ksrc,*[2*(s*Ksrc*(B*B+f[j-1]**2+TQ+B*q[j-1])+1) for j in range(1,L)])
    BU = max(2*q[j-1] for j in range(1,L))
    # Runtime: source error multiplier is one; carrier multiplier is separate.
    h=g=2.
    bb = [g**(L-j+1)*Rr**(L-j) for j in range(1,L+1)]
    b = max(bb)
    U = math.sqrt(bb[0]**2+h*h*sum(x*x for x in bb[1:]))
    FF = g
    for j in range(1,L): FF = g*(h+Rr*FF)
    Ddel = 3*b+3
    W = 64.
    J0 = h*math.sqrt(L)*(7*b+3)
    V0 = 14*FF*U
    Ph, Pd = 17.,18*b+11
    Dr = 8*Ph
    A0 = 1+2*(R0+1)+8*Ddel*Ph+8*h*Pd
    Cf = FF*(1+A0)
    H0 = 1+3*W*Cf+3*Dr
    Z0 = L*(g*Rr)**L*(Ddel+A0+Cf)
    J1 = math.sqrt(L)*(h*b*H0+h*Z0+Ddel*Cf)
    Dgram = Ph+L*(Pd*h*h+9*b*b*Ph)
    F0 = 8*Cf+24*J0*J1+6*Dgram
    T0 = 6*V0
    G = 4*(T0+F0)+2*Cf+2*J1
    C1 = G*(8+W/2)
    C2 = 64*Ksrc*G
    O0 = 2*h*H0+W*Cf+Dr
    W1 = 2*h+50*V0+6*(h*h+J0*J0)
    T1 = h*W1+7*V0
    crt = min(1.,1/math.sqrt(224*FF*U),1/(6*J0))
    bprev = max(bq[:-1])
    cangle = 1/(16*math.sqrt(s*Ksrc*max(2.,TJ+B*bprev)))
    ctime = math.sqrt(a/(1024*(AU+BU)))
    c = min(csrc,crt,1/C1,1/math.sqrt(C2),cangle,ctime)
    cerr = O0*(1+math.sqrt(math.e)*(C1+C2*c)*math.exp(C1*c+C2*C2*c**4))+8*T1
    return dict(L=L,csrc=csrc,crt=crt,cangle=cangle,ctime=ctime,c=c,cerr=cerr,Ksrc=Ksrc,C1=C1,C2=C2,AU=AU,BU=BU,TJ=TJ,bprev=bprev)

if __name__ == '__main__':
    for L in (2,3,5,10,20):
        v=evaluate(L)
        print('L',L,' '.join(f'{k}={v[k]:.8e}' for k in ('csrc','crt','cangle','ctime','c','cerr','Ksrc','bprev')))
        print('logs',-math.log10(v['c']),math.log10(v['cerr']),62*L*math.log10(16),124*L*math.log10(16))

    # Exact inputs and evaluator for the storage table in Section 7.
    for L, d in ((2,2),(2,10),(2,100),(5,10),(10,100)):
        bprev = 6.4*(64/15)**(L-2)
        gd = 4*math.sqrt(d+3)
        cq_inverse = (16*gd*bprev+32)/.5
        log_factorial = math.lgamma(d+1)/math.log(10)
        new = math.log10(2040*(L+1))+2*(
            math.log10(1024)+d*math.log10(9)+math.log10(gd)
            +(d-1)*math.log10(cq_inverse)-log_factorial)
        old = 82*L*d*math.log10(16)+d*math.log10(d+3)-2*log_factorial
        print('storage',L,d,round(old,3),round(new,3))
```
