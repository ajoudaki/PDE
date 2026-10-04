# Explicit small-label constants for the existing source proof

2026-10-04. Scoped independent derivation, initially frozen before exchanging
findings at SHA-256
`aa2c2edd37dcb1a3c23d13395cada87c0fd48fbf8deb81867717dc16455591da`.
The following self-check revision replaces a sharp initialized-operator cap
by an elementary Gaussian-net cap; no other agent finding was used.
This is a quantitative reconstruction of the already checked insertion
interfaces, not an independent promotion review. No source theorem, maintained
file, experiment or Git state is changed. The recurrences below are
conservative; their role is to specify actual constants rather than guess
an unspecified large function of depth.

## Inputs and scope

Complete current-study inputs read: `LABEL_SEPARATE_BUDGETS.md`,
`LABEL_SEPARATE_BUDGETS_CHECK.md`, `DATASET_LABEL_DEPENDENCE.md`,
`DEPTH_INDEPENDENT_EXPONENT.md`, `INPUT_DEPTH_REFINEMENT.md`,
`DEEP_COMPLEX_SOURCE.md`, `DEEP_ACTIVATION_EXTENSION.md`,
`DATASET_SOURCE_CONSTANTS.md`, and `DATASET_MAXIMUM_REFINEMENT.md`.
The supervisor subsequently confirmed the user's persistent authorization
for the exact prior inputs `DEPTH_CAVITY_ROUTE.md`,
`DEPTH_INSERTION_CHECK.md`, and `DEPTH_CAVITY_PROBABILITY_CHECK.md` in
`studies/dense_cutoff_population_rate_20261001/`; these were then read
completely. No further prior references were followed. Appended unrelated
unbounded-activation conclusions in the complete check files are not inputs
to any claim below. Required canonical-notation, neural-network, and
rigorous-proof skills were read.

The scientific interfaces retained as inputs are the source's conditional
uniform Gaussian insertion event, its nonlinear remainder and full/cavity
continuation construction. Their fixed constants multiply negative powers
of width and affect the eventual width threshold. This report computes
the constants that survive that limit and select the allowed activity:
the physical tube, residual-Hessian growth, endpoint series, singleton
shift, activity modulus, and single-sample exponential moment.

## 1. Setup and an explicit real threshold

Let all activations be real on the real axis, holomorphic on
`|Im z|<a`, and bounded there by `B_phi`, with `a>0`. Use the canonical
width-n, depth-L network and physical mean-square-loss flow in the assigned
sources, with unit training inputs `v_a`, zero readout, and normalized
limiting feature gap

\[
 \lambda=\min\{1,\gamma/m\}>0,\qquad
 \gamma=\lambda_{\min}(Q^{(L)}),\qquad
 Y=\|y\|_2/\sqrt m.
\]

Throughout, `B` denotes an activation bound; `mathcal B` below denotes the
carrier budget. Set the explicit activation constants

\[
 B=\max(1,B_\phi),\quad
 s=\max(1,4B/a),\quad t=\max(1,32B/a^2).
 \tag{1}
\]

Cauchy's formula gives `|phi'|<=s` and `|phi''|<=t` on
`|Im z|<=a/2`, as well as the finite third and fourth derivative bounds
used by the inherited local insertion proof. Choose the initialized hidden
operator cap 8. To verify its high-probability event without an unstated
sharp spectral-norm theorem, take 1/4-nets of the two unit spheres with
at most `9^n` points each. The operator norm is at most twice the maximum
bilinear form on their product: approximate both maximizing unit vectors
and absorb `2*(1/4)||W||_op`. Each fixed bilinear form for the initialized
matrix has variance `1/n`. The elementary Gaussian tail and a union bound
give

\[
 \Pr\{\|W_0\|_{\rm op}>8\}
 \le2\exp\{-n(8-2\log9)\}.
\]

A union over fixed L preserves convergence to zero. The net-size bound
comes from disjoint radius-1/8 balls centered at a maximal 1/4-separated
set, all contained in the ball of radius 9/8. The real tube cap is then 9.

Define

\[
 b_\ell=s(9s)^{L-\ell},\quad
 F_1=s b_1,\quad
 F_\ell=s(B^2b_\ell+9F_{\ell-1}),\quad
 C_*=\max(1,B^2b_1,F_L).
 \tag{2}
\]

Equivalently, without a recursion,

\[
 F_L=s^2\left[(9s)^{2L-2}
             +B^2\sum_{j=0}^{L-2}(9s)^{2j}\right].
 \tag{3}
\]

On an initialized normalized feature-gap event at least `lambda/2`,
`DATASET_LABEL_DEPENDENCE.md`, equations (5)--(8), applies if

\[
 Y\le\lambda/(8\sqrt{C_*}).                         \tag{4}
\]

It supplies residual RMS `rho(t)<=Y exp(-lambda t/4)` and
`int rho<=4Y/lambda`. The full initialization gap can be required to
exceed `3lambda/4`; fixed-size rectangular cavities then retain the
`lambda/2` margin for sufficiently large width, uniformly over the
sets of each fixed size. This changes the width threshold, not (4).

For the source proof take

\[
                    S=16Y/\lambda.                    \tag{5}
\]

The real residual-activity measure
`dmu=(2/m)sum_a |r_a|dt` has mass at most `S/2`.
On the short negative-real and vertical portions of the source contours,
the extra mass is `o(S)` at fixed parameters, by the inherited residual
bound and the shrinking contour radius. Thus, after increasing width,
the total contour activity is at most `S`. Real hidden norms are at most
9; the complex tube can use the strict enlarged cap 10. Integration of
the readout equation gives `||w||_infty<=B S` on those contours. We use
the weaker factor 2 below to retain a margin. These choices eliminate
an unspecified activity normalization `C_0`.

## 2. Explicit Hessian and response-endpoint constants

Put `R=10`, and define the carrier RMS bounds and forward derivative bounds

\[
 K_\ell=2B(Rs)^{L-\ell},\qquad
 P_1=2,\qquad P_\ell=B+RsP_{\ell-1}+1\quad(\ell\ge2).
 \tag{6}
\]

Then `||k_a^(ell)||_2/sqrt(n)<=K_ell S`. The numbers `P_ell`
bound the operator norms of the preactivation derivatives in mobility
coordinates `Theta=(A,sqrt(n)W^(2),...,sqrt(n)W^(L),w)`, including
one external preactivation vector `e` at any possible insertion layer.
Indeed the matrix variation costs `B`, propagation costs `RsP_(ell-1)`,
and an external injection costs at most 1. The first input map has norm
at most 1. Taking the sum of these bounds proves (6) also for rectangular
cavities with normalization n.

Set

\[
 A_H=2sP_L+2s^2\sum_{\ell=2}^L K_\ell P_{\ell-1}
                       +tP_L^2K_L,
\]
\[
 D_H=t\sum_{\ell=1}^{L-1}P_\ell^2,\qquad
 H=\max(1,A_H,D_H),
\]
\[
 H_2=2sP_L+2s^2\sum_{\ell=2}^L K_\ell P_{\ell-1}
                       +t\sum_{\ell=1}^L P_\ell^2K_\ell.
 \tag{7}
\]

Use carrier exponent `eta_0=1` and stop every cavity at its own
separate-sample budget `2mathcal B`. For `S<=1`, the Hessian of
`F_a=n f_a`, and its augmented version including e, satisfy

\[
 \|D^2F_a\|_{p,n}
 \le H[1+Sp(2\mathcal B)^{1/p}],\qquad p\ge2,
\]
\[
 \|D^2F_a\|_{2,n}\le H_2,\qquad
 \|D^2F_a\|_{\rm op}
 \le A_H+D_H S\log(2n\mathcal B).                       \tag{8}
\]

Here `||T||_(p,n)=n^(-1/p)||T||_(S_p)`. To verify every contribution,
use prior cavity equation (11). The two readout mixed terms each factor
through a space of dimension at most n and cost `sP_L` in normalized
Schatten norm. At layer ell the two matrix mixed terms each cost
`s^2K_ell S P_(ell-1)`, again with rank at most n. Curvature costs
`tP_ell^2 ||k_a^(ell)||_(p,n)`. At the top use the readout coordinate
bound `K_L S`; at the remaining layers use

\[
 \|k_a^{(\ell)}\|_{p,n}
 \le S(p/e)(2\mathcal B)^{1/p}
 \le Sp(2\mathcal B)^{1/p}.
\]

For the Hilbert--Schmidt estimate use `K_ell S` at every layer instead.
The operator estimate uses the stopped coordinate bound
`S log(2n mathcal B)` at non-top layers. These statements are preserved
under taking a matrix block. In particular the mixed response endpoint
`D_Theta delta_a^(j+1)` is a block of the augmented Hessian, so it has
all the corresponding bounds in (8). Normalized residual averages
preserve these constants by the triangle inequality.

The negative-Gram base propagator is contractive on positive real time.
All its complex or negative-real pieces together cost at most 2 after
increasing width. Thus the full variational propagator satisfies

\[
 \|\mathcal J\|_{\rm op}
 \le2\exp\{S A_H+D_HS^2\log(2n\mathcal B)\}.
 \tag{9}
\]

The explicit condition `D_H S^2<=1/4000` ensures the inherited
`n^(1/1000)` cap for sufficiently large n. The fixed exponential in
(9) goes into that width threshold. It cannot be used to absorb the
coefficient `D_H S^2` of `log n`; this is a real label restriction.

## 3. Endpoint series and the singleton insertion shift

The term with h residual-Hessian insertions between two response endpoints
has the normalized integrated trace bound

\[
 \frac{2S^h}{h!}
       [H\{1+S(h+2)(2\mathcal B)^{1/(h+2)}\}]^{h+2}.
 \tag{10}
\]

The factor 2 is the total base-propagator cost, used once. If
`HS<=1` and `2eHS^2<=1/2`, then summing h>=1 gives

\[
 \sum_{h\ge1}(10)
 \le4H^2(e^2-1)+576e^3H^3\mathcal B S^4.
 \tag{11}
\]

For completeness, split the (h+2)-nd power using
`(u+v)^(h+2)<=2^(h+1)(u^(h+2)+v^(h+2))`.
The first sum is at most `4H^2(exp(2HS)-1)`.
For the second use

\[
 \frac{(h+2)^{h+2}}{h!}\le e^{h+2}(h+2)^2,
 \qquad
 \sum_{h\ge1}q^h(h+2)^2\le36q\quad(0\le q\le1/2),
\]

with `q=2eHS^2`. This gives exactly the second term in (11).
The term h=0 is at most `2H_2^2`. Define

\[
 T_0=2H_2^2+4H^2(e^2-1),\quad T_1=576e^3H^3,
\]
\[
 E=t\sum_{\ell=1}^L(Rs)^{2(\ell-1)}K_\ell,
 \quad K_{\max}=\max_\ell K_\ell,
\]
\[
 D=\max\{1,\ B(T_0+T_1+E)+Bs^2K_{\max}^2\}.
 \tag{12}
\]

Here E bounds the direct external Hessian trace divided by S. In fact an
injection at layer p propagates with derivative norm at most
`(Rs)^(ell-p)`, and its external Hessian is the sum of curvature
contractions. Replacing p by 1 only increases the bound in (12).

Prior cavity Section 6 decomposes the singleton shift into the endpoint
trace, direct external trace, learned outgoing column, centered independent
incoming/outgoing forms, and a vanishing rank-one adaptation term. The
first costs at most `B S(T_0+T_1 mathcal B S^4)`, because its scalar
activation control is at most B. The second costs at most `B E S`.
The learned-column increment is at most `B s K_max S^2/sqrt(n)`;
pairing with the upper response costs at most `B s^2K_max^2S^3`.
The centered forms and the adaptation term contribute o(1) on the inherited
uniform insertion event. Consequently, for `S<=1`,

\[
 \sup_{a,z}|k_{a,i}^{(j)}(z)
          -x_i^\top\delta_a^{(j+1),-i}(z)|
 \le D S(1+S^2\mathcal B)+o(1).                        \tag{13}
\]

The constant D is explicit and independent of deletion count, empirical
moment degree, input dimension, sample count and data. It depends on depth
through (6)--(12). The complex calculation has already included its base
factor 2; no extra unquantified constant is inserted into (13).

## 4. Explicit single-sample Gaussian moment

For a real cavity, use activity parameter `u=mu([0,t])/S`, whose range
is contained in [0,1], and freeze its path beyond its own stop.
For two parameter values with `v=|u-u'|<=1`, physical updates imply

\[
 \|\Delta w\|_\infty\le B S v,\quad
 \|\Delta A\|_F/\sqrt n\le sK_1S^2v,\quad
 \|\Delta W^{(\ell)}\|_F\le BsK_\ell S^2v.
\]

Define

\[
 V_1=sK_1,\qquad
 V_\ell=B^2sK_\ell+RsV_{\ell-1}.
 \tag{14}
\]

Forward subtraction then gives
`||Delta z_a^(ell)||_2/sqrt(n)<=V_ell S^2v`.
At a non-top backward gate split the reference carrier at `S R_c`,
where

\[
 R_c=4\log(8\sqrt{2\mathcal B}/v).
\]

The exponential budget gives

\[
 \|k\mathbf1_{|k|>SR_c}\|_2/\sqrt n
 \le4S\sqrt{2\mathcal B}\,e^{-R_c/4}.
\]

Indeed `x^2 e^(-x/2)<=16` for x>=0. The changed gate is bounded by
2s, so this high part costs at most `s S v`.
The low part costs `t V_ell S^3 R_c v`. For `mathcal B>=2`,
`R_c<=10 log(e+mathcal B)+4 log(1/v)`. Therefore, if
`S^2 log(e+mathcal B)<=1` and `S<=1`,

\[
 S^2R_cv\le14\sqrt v.
\]

This uses `v log(1/v)<=2sqrt(v)/e`. At the top use the deterministic
readout bound directly. Define the descending recurrence

\[
 G_L=sB+2BtV_L,
\]
\[
 G_\ell=RsG_{\ell+1}+Bs^3K_{\ell+1}^2+14tV_\ell+s
                  \quad(\ell<L),\qquad
 G=\max(1,G_1,\ldots,G_L).
 \tag{15}
\]

Backward subtraction proves, sample by sample,

\[
 \|\delta_a^{(\ell)}(u)-\delta_a^{(\ell)}(u')\|_2
             /(S\sqrt n)\le G\sqrt{|u-u'|}.            \tag{16}
\]

The `Bs^3K_(ell+1)^2` term is the changed-matrix term, propagated
through the slope. This accounts for every term of the downward recursion.

For an independent omitted root `x~N(0,I_n/n)`, put
`Z=sup_u |x^T delta_a(u)|/S`. Conditional on the cavity, the process
starts at zero and has increment standard deviation at most
`G sqrt(|u-u'|)`. A dyadic Gaussian argument with numerical constants gives

\[
 \Pr\{Z>32G(1+z)\mid\mathrm{cavity}\}\le e^{-z^2},
                           \qquad z\ge0.               \tag{17}
\]

One explicit construction uses grids of spacing `4^(-k)` and their
nearest lower-level parents. There are at most `2*4^k` increments at
level k, each of standard deviation at most `2G*2^(-k)`.
Allocate Gaussian thresholds
`2G*2^(-k)*sqrt(2[z^2+4(k+1)])`. The sum of failure probabilities is
at most `4e^(-4)/(1-4e^(-4))*e^(-z^2)<e^(-z^2)`.
Summing the thresholds, with
`sum 2^(-k)=2` and `sum 2^(-k)sqrt(k+1)<=4`, is bounded by
`32G(1+z)`. Continuity supplies the full interval from the nested grids.

Integrating (17) yields the fully specified moment bound

\[
 \mathcal M(q)=e^{32qG}
       [1+32qG\sqrt\pi\,e^{256q^2G^2}],\qquad
 \mathbb E[e^{qZ}\mid\mathrm{cavity}]\le\mathcal M(q).
 \tag{18}
\]

For the enlarged complex source radius, the normalized correction has
radius `O(log(en)^(-1/2)log log(en))` and its Gaussian supremum tends
to zero; this is the proved correction in
`DEPTH_INDEPENDENT_EXPONENT.md`, equations (30)--(31). Its fixed second
exponential moment is therefore at most 2 after increasing width.
Cauchy--Schwarz gives a common real/complex first exponential-moment bound

\[
                    \mathcal M_c=\sqrt{2\mathcal M(2)}.
 \tag{19}
\]

All coefficients in the vanishing complex correction can be absorbed
into the width threshold. This is legitimate because they multiply a
quantity tending to zero, and (19) is the fixed numerical target needed
for the carrier-budget argument. No sample maximum is taken here.

## 5. Closed label coefficient

Choose the explicit carrier budget

\[
 \mathcal B=2L+8(L-1)\mathcal M_c e^D.                  \tag{20}
\]

Define

\[
 S_* =\min\left\{
 1,\ H^{-1},\ (4eH)^{-1/2},\ (4000D_H)^{-1/2},
 \mathcal B^{-1/2},\
 \sqrt{\frac{\log2}{D\mathcal B}}\right\},
\]
\[
 c_{L,\phi}=\min\left\{\frac1{8\sqrt{C_*}},
                              \frac{S_*}{16}\right\}.
 \tag{21}
\]

Every denominator is positive. Equations (1)--(3), (6)--(7),
(12), (14)--(15), and (18)--(21) are a finite, explicitly evaluable
recurrence in L and the two strip bounds a,B_phi. They require no
input dimension or data-dependent constants.

The sufficient label condition

\[
                       0<Y\le c_{L,\phi}\lambda         \tag{22}
\]

implies the real fitting condition, the small propagator exponent,
the endpoint-series convergence, and the Gaussian modulus assumption:
`log(e+mathcal B)<=mathcal B` since `mathcal B>=2`.
It also gives `exp(D S^2mathcal B)<=2`. The distinct-index fixed-sample
moment base is therefore at most `2mathcal M_c e^D`. Equations
(20)--(21) give

\[
 \frac{(L-1)\mathcal M_c e^{D(1+S^2\mathcal B)}}
      {\mathcal B}\le\frac14.
 \tag{23}
\]

At each fixed empirical moment degree p, the limiting budget-hit
probability is at most `m 4^(-p)`. The width limit is taken first and
then the infimum over fixed p. All collision terms have finite moments
from (18), so they vanish with width exactly as in the checked source.
This closes both the real and complex budget under the explicit (22).

The asymmetric endpoint trace for passive queries in
`DEPTH_INDEPENDENT_EXPONENT.md` has the same residual-Hessian factors
as (10), but different fixed endpoint norms. Their depth and angle
constants multiply the already convergent series; they do not alter its
convergence threshold. They select the query-response caps and the radius
multiplier. Higher local graph constants and query-net cardinalities
likewise affect only the eventual width threshold, because all their
remainders keep the strict negative powers already proved in the source.
No additional smallness condition on S appears at those steps.

For an uncapped requested form, `gamma/m<=B^2` by the covariance trace
bound, and hence
`min(1,gamma/m)>=(gamma/m)/B^2`. Thus a sufficient statement for the
whole bounded-strip activation class is

\[
              0<Y\le\frac{c_{L,\phi}}{B^2}\frac\gamma m.
 \tag{24}
\]

If `B_phi<=1`, the cap is inactive and the factor `B^(-2)` is one.
The zero-label case is separately stationary and exact.

## 6. Quantitative meaning and limits

This is an explicit sufficient coefficient for the source label condition.
It is not an optimal depth dependence: the exponential moment and endpoint
series produce a very small value. It does not turn the fixed-depth source
proof into a growing-depth theorem, since the final width threshold remains
allowed to depend on d,L,m,gamma,Y and confidence.

The use of n large in this derivation is confined to: initialized operator
and Gram margins; fixed-size cavity transfer; fixed prefactors in the
variational bound; vanishing Gaussian insertion and nonlinear remainders;
the short-contour tube; and the vanishing complex Gaussian correction.
The nonvanishing quantities selecting label size are all explicitly
bounded in (1)--(23). In particular the coefficient of log n in the
variational exponent and the fixed-block moment base were not moved
into n_0.

The original source proof's source-radius and storage coefficients are a
separate task. This route establishes that its label coefficient can be
chosen independently of input dimension once inputs have unit norm, with
all dependence on L displayed in the stated recurrences. No conclusion
about the final error or retained-size coefficient is inferred from this
label calculation alone.
