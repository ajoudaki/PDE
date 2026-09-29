# Explicit depth constants for source tails and all-time feedback

Scoped author derivation, 28 September 2026. Inputs read completely were
`ACTIVATION_LOCAL_MODULUS.md`, `ACTIVATION_SMALL_LABEL_ROUTE.md`, and
`ACTIVATION_EXTENSION.md`, together with the required
`solve-math-rigorously` skill. The supervisor subsequently expanded the
scope to `DEPTH_SMALL_LABEL_SOURCE.md`, which was read completely for the
compatibility check in Section 6. No other research source, experiment, study
history, or maintained material was read or changed. This note makes the
constants in the source-tail and feedback arguments explicit, conditional
on the all-order existence, tube, Gram, and decay bootstrap in those inputs.
It is not an independent review or a promoted result.

The useful conclusion is that the constants **before** activity Gronwall
and **inside** its exponent have bounds singly exponential in depth when
the layer bounds are fixed and the inverse initial Gram gap is displayed
separately. The raw factor `exp(a_L Y)` can therefore be doubly exponential
as a bound in depth if the label threshold is left unchanged. Reducing the
label threshold to `Y <= 1/a_L` removes this extra cost from the final
`C_L/P` prefactor if the order condition depends only on curvature.
Alternatively, include `a_LY` in the order condition and retain the full
source theorem's label range. Both tradeoffs are explicit below.

## 1. Inputs and a forward-energy estimate without an artificial factor per layer

Take `L >= 2`. Write `X=max_a ||x_a||/sqrt(d)`, let `D>0` bound every
hidden operator on both trajectories, and let `R_1` bound every first
preactivation RMS on the tube. For example the supplied proof uses
`D=K+1` and `R_1=R_0+1`; any other already justified tube can be substituted.
Let `a_l=|phi_l(0)|` and `s_l=||phi_l'||_infinity`. Define

\[
 M_1=a_1+s_1R_1,\qquad
 M_l=a_l+s_lD M_{l-1}\quad(2\le l\le L),\qquad Q_0=1+M_L.
 \tag{1}
\]

Let `lambda>0` be the initial top-feature Gram gap, so the maintained
Gram lower bound is `lambda/2`. The supplied bootstrap gives

\[
 \kappa=\lambda/2,\quad
 \rho(t)\le Q_0Ye^{-\kappa t},\quad
 \int_t^\infty\rho(s)ds\le\rho(t)/\kappa,\quad
 \int_0^\infty\rho\le c_TY,\qquad c_T=\frac{2Q_0}{\lambda}.
 \tag{2}
\]

For either path use the stopped-cap readout bound with

\[
 c_S=\frac{4Q_0}{\lambda},\quad
 b=1+2M_Lc_S,\quad
 q_L=s_L,\quad q_l=s_lDq_{l+1},\quad b_l=bq_l.
 \tag{3}
\]

Then readout RMS is at most `bY` and backward RMS at layer `l` is at
most `b_lY`. Throughout impose the already available bootstrap label
conditions, `Y<=1`, `c_SY<=1`, and the following optional tightening:

\[
 Y b_lM_{l-1}\le\frac{D}{4L}\quad(2\le l\le L).
 \tag{4}
\]

Zero products impose no restriction. Condition (4) is independent of width,
order, and gate curvature. All subsequent constants are independent of `Y`.
This tightening is needed only for the particularly simple energy
coefficients (5). An already proved bound `Z_l<=v_l^2Y^3` can be inserted
directly in Section 2 with no new restriction. To obtain coefficients on
an original label range `0<Y<=bar Y` without (4), replace the propagation
coefficient `(1+1/L)s_lD` in (5) by
`s_l[D+2sqrt(2)b_lM_(l-1)bar Y]`. The derivation below proves that version
as well. The feedback recurrences require neither (4) nor a particular
choice of valid energy coefficients.

Define nonnegative forward-energy coefficients by

\[
 v_1=2s_1X^2b_1\sqrt{c_S},\qquad
 v_l=2s_l\sqrt{c_S}\,b_lM_{l-1}^2
            +(1+L^{-1})s_lD v_{l-1}.
 \tag{5}
\]

Then the closure's actual forward clock energy satisfies
`Z_l <= v_l^2 Y^3`. Here is a direct derivation that improves the
squared-three-term estimate in the supplied source. Its defect-energy
identity gives

\[
 \left(\int_0^t\rho\|E_l/\rho\|_F^2ds\right)^{1/2}
       \le\sqrt2 A\,b_lY\sqrt{Z_{l-1}},\qquad A=1+c_SY\le2.
\]

Minkowski's inequality in the sample/time Hilbert space, applied to the
forward chain rule, therefore gives

\[
 \sqrt{Z_l}\le
 2s_l\sqrt{c_S}\,b_lM_{l-1}^2Y^{3/2}
 +s_l[D+\sqrt2 A b_lYM_{l-1}]\sqrt{Z_{l-1}}.
\]

By (4), the coefficient in brackets is at most `D(1+1/L)`.
The first-layer energy gives the first line of (5); induction proves the
claim. Thus the extra product from the estimate itself is at most
`(1+1/L)^L <= e`, and the actual activation/operator gains remain visible.

## 2. Fully explicit source-tail coefficients

Let `C_leg` be any fixed absolute constant in the proved endpoint-kernel
bound `||Pi_P||_(L-infinity -> endpoint) <= C_leg sqrt(P)`. It has no
dependence on depth, data, width, gap, or activation. The forward endpoint
derivative inequality can be used with constant one, as follows from the
exact squared kernel norm in the supplied source. Put

\[
 e_l=2\sqrt2(1+C_{\rm leg})b_l v_{l-1}\quad(2\le l\le L),
 \qquad E_*=\sum_{l=2}^L e_l.
 \tag{6}
\]

Applying the kernel bound to the sample direct sum avoids an unnecessary
`sqrt(m)`: at every history time the direct-sum RMS of
`b_(l,a)=(r_a/rho)delta_(l,a)` is at most `b_lY`, because
`||r/rho||_m=1`. The forward endpoint error is at most
`sqrt(2/P) v_(l-1)Y^(3/2)`. Hence the exact physical defect satisfies

\[
 \|E_l(t)\|_F\le e_lY^{5/2}\rho(t),\qquad
 e_E(t):=\sum_{l=2}^L\|E_l(t)\|_F\le E_*Y^{5/2}\rho(t).
 \tag{7}
\]

Define hidden velocity and preactivation-speed coefficients

\[
 V_l=2b_lM_{l-1}+e_l\quad(l\ge2),\qquad
 t_1=2X^2b_1,\qquad
 t_l=V_lM_{l-1}+Ds_{l-1}t_{l-1}.
 \tag{8}
\]

Indeed hidden velocity is at most `V_lYrho`, using `Y<=1`, while
`||dot z_(l,a)||/sqrt(n) <= t_lYrho`; feature speed is bounded by
`s_l t_lYrho`. Let

\[
 R=\max\{R_1,DM_1,\ldots,DM_{L-1}\},\quad
 \ell_n=\max_l\operatorname{Lip}(\phi_l';[-R\sqrt n,R\sqrt n]),\quad
 \chi=\ell_n\sqrt nY^2.
 \tag{9}
\]

The readout speed is at most `2M_Lrho`. Differentiating the backward
recursion with the Lipschitz chain rule gives

\[
 \max_a\frac{\|\dot\delta_{l,a}\|}{\sqrt n}
       \le(d_l^0+d_l^1\chi)\rho,
 \tag{10}
\]

where every coefficient is explicit:

\[
 d_L^0=2s_LM_L,\qquad d_L^1=bt_L,
\]
\[
 d_l^0=s_l(Dd_{l+1}^0+V_{l+1}b_{l+1}),\qquad
 d_l^1=s_lD d_{l+1}^1+Db_{l+1}t_l\quad(l<L).
 \tag{11}
\]

The operator-derivative term uses `Y^2<=1`. The gate-derivative term
uses precisely one coordinate loss: the full carrier supremum norm is
at most its RMS bound times `sqrt(n)`.

For the remaining constants write

\[
 u_1=X,\quad u_l=M_{l-1}\ (l\ge2),\qquad
 G_*=M_L^2+\sum_{l=1}^L b_l^2u_l^2,
 \quad J_* = \max_{2\le l\le L}b_lM_{l-1},
\]
\[
 R_r=2G_*+J_*E_*.
 \tag{12}
\]

The explicit tangent Gram formula gives `||Gamma|| <= G_*`, and
`||JE||_m <= J_*Y e_E`. Consequently
`||dot r||_m <= R_r rho` and
`||d(r/rho)/dt||_m <= 2R_r` on every nonstationary trajectory.
In the sample direct-sum norm this yields

\[
 \|\dot b_l\|\le2R_rb_lY+(d_l^0+d_l^1\chi)\rho.
 \tag{13}
\]

The zero backward prefix has one initial jump. Let `q_l^0` be the
initial backward gain: `q_L^0=s_L` and
`q_l^0=s_lKq_(l+1)^0`, where `K` bounds the initialized hidden operators.
One can instead use `q_l^0=q_l` whenever `K<=D`. Its jump RMS is at
most `q_l^0 B_0`.

To verify all gap factors in the terminal cutoff, integrate (13):

\[
 \int_0^T\|\dot b_l\|^2dt
 \le Y^2\left[8R_r^2b_l^2T+
       \frac{Q_0^2}{\kappa}(d_l^0+d_l^1\chi)^2\right].
 \tag{14}
\]

Here `integral rho^2 <= Q_0^2Y^2/(2kappa)` follows from (2).
The weighted clock energy of the continuous history frozen at `T` is
at most `(2/kappa)` times (14). Setting
`T=(2/kappa)log(e+P)` bounds its projected tail by

\[
 \frac{Y}{\kappa P}
 \left[\sqrt{32}R_rb_l\sqrt{\log(e+P)}
       +\sqrt2Q_0(d_l^0+d_l^1\chi)\right].
\]

The cutoff approximation error is at most
`2b_l sqrt(c_T)Y^(3/2)/(e+P)`, because its clock support has length
at most `c_TY exp(-kappa T)`. The scalar prefix step has projection tail
at most `3/sqrt(P)` when the total clock is at most two: a ramp of length
`tau/P` has direct error at most `sqrt(tau/P)` and projected error at
most half that value; `P=1` follows by contraction.

Thus define

\[
 B_l=\frac{\sqrt{32}R_rb_l+\sqrt2Q_0(d_l^0+d_l^1)}{\kappa}
                       +2b_l\sqrt{c_T}.
 \tag{15}
\]

For every terminal time the backward and forward tails satisfy

\[
 Q_{b,l}\le\frac{3q_l^0 B_0}{\sqrt P}
       +\frac{B_lY\sqrt{1+\chi^2+\log(e+P)}}P,
 \qquad Q_{h,l}\le\frac{v_lY^{3/2}}P.
 \tag{16}
\]

The exact projection-energy pairing gives
`integral e_E <= 2 sum_(l>=2) Q_(b,l) Q_(h,l-1)`. In particular, with

\[
 A_{\rm src}=2\sum_{l=2}^L v_{l-1}(3q_l^0+B_l),
 \tag{17}
\]

one obtains the fully quantitative absolute-defect bound

\[
 \varepsilon_{n,P}:=\int_0^\infty e_E(t)dt
 \le A_{\rm src}\left[
 \frac{B_0Y^{3/2}}{P^{3/2}}+
 \frac{Y^{5/2}\sqrt{1+\chi^2+\log(e+P)}}{P^2}\right].
 \tag{18}
\]

All coefficients in (18) are specified by finite recurrences and sums.
No backward-history regularity constant or inverse-gap factor is implicit.

## 3. Explicit feedback coefficients

Use the block-sum parameter discrepancy `d=x+eta`, where `x` is the
first-layer normalized Frobenius discrepancy plus the hidden Frobenius
discrepancies, and `eta` is the readout RMS discrepancy. This dominates
the mobility Hilbert norm in the local-modulus note and is exactly the
distance in the extension's statement.

Define forward-difference coefficients

\[
 z_1=X,\quad f_1=s_1X,\qquad
 z_l=M_{l-1}+Df_{l-1},\quad f_l=s_lz_l.
 \tag{19}
\]

Then preactivation and feature RMS differences are at most `z_l x` and
`f_l x`. These follow by subtracting `W_hat h_hat-W_D h_D` and using
the tube bounds on both trajectories.

Define backward-difference coefficients `j_l,p_l` by

\[
 j_L=0,\quad p_L=bz_L,
\]
\[
 j_l=s_l(Dj_{l+1}+b_{l+1}),\qquad
 p_l=s_lDp_{l+1}+Db_{l+1}z_l\quad(l<L).
 \tag{20}
\]

Writing `h=ell_n sqrt(n)`, subtraction of the backward recursion with
the full dense carrier in each gate-difference term gives

\[
 \max_a\frac{\|\widehat\delta_{l,a}-\delta_{D,l,a}\|}{\sqrt n}
 \le q_l\eta+Yj_lx+hYp_lx.
 \tag{21}
\]

For the explicit Gram-difference bound set

\[
 G_0=2M_Lf_L+2\sum_{l=1}^L b_lj_lu_l^2
                    +2\sum_{l=2}^L b_l^2M_{l-1}f_{l-1},
\]
\[
 G_\eta=2\sum_{l=1}^L b_lq_lu_l^2,\qquad
 G_\chi=2\sum_{l=1}^L b_lp_lu_l^2.
 \tag{22}
\]

Subtract each pair of forward/backward inner products in the tangent
Gram, using `Y^2<=1` in its curvature-free `x` coefficient. A sample
matrix whose entries have absolute value at most `C/m` has operator norm
at most `C`. The result is

\[
 \|\widehat\Gamma-\Gamma_D\|\le
                   (G_0+G_\chi\chi)x+G_\eta Y\eta.
 \tag{23}
\]

Let `v=||f_hat-f_D||_m`, `Q(t)=integral_0^t v`, and
`epsilon(t)=integral_0^t e_E`. The exact prediction discrepancy equation,
`2 Gamma_hat >= lambda I`, and zero initial discrepancy imply

\[
 Q(t)\le\frac2\lambda\int_0^t\rho_D
       [(G_0+G_\chi\chi)x+G_\eta Y\eta]ds
                       +\frac{J_*Y}{\lambda}\varepsilon(t).
 \tag{24}
\]

The norm derivative can be regularized at zero before integration. This
is the point at which damping supplies an explicit `1/lambda`.

For the parameter equations put

\[
 U=2\sum_{l=1}^L b_lu_l,\quad
 V=2\sum_{l=1}^L q_lu_l,\quad
 W=2\sum_{l=1}^L j_lu_l+2\sum_{l=2}^L b_lf_{l-1},\quad
 Z=2\sum_{l=1}^L p_lu_l.
 \tag{25}
\]

Subtracting the canonical readout and hidden updates gives

\[
 \eta(t)\le2M_LQ(t)+2f_L\int_0^t\rho_Dx\,ds,
\]
\[
 x(t)\le UYQ(t)+\int_0^t\rho_D
                  [V\eta+WYx+ZhYx]ds+\varepsilon(t).
 \tag{26}
\]

Set

\[
 T_*=2M_L+U,\qquad F_*=1+\frac{T_*J_*}{\lambda},
\]
\[
 c_0=\max\left\{2f_L+W+\frac{2T_*G_0}{\lambda},
                       V+\frac{2T_*G_\eta}{\lambda}\right\},
 \qquad c_1=Z+\frac{2T_*G_\chi}{\lambda}.
 \tag{27}
\]

Inserting (24) into (26), using `Y<=1` and `chi=hY^2<=hY`, proves

\[
 d(t)\le F_*\varepsilon(t)
       +\int_0^t(c_0+c_1hY)\rho_D(s)d(s)ds.
 \tag{28}
\]

Activity Gronwall and (2) therefore give

\[
 \sup_{t\ge0}d(t)\le F_*\varepsilon_{n,P}
       \exp\{c_Tc_0Y+c_Tc_1\chi\}.
 \tag{29}
\]

For a single coefficient pair one may take

\[
 A_L=\max\{1,F_*A_{\rm src}\},\qquad
 a_L=\max\{1,c_Tc_0,c_Tc_1\}.
 \tag{30}
\]

Equations (18) and (29) give exactly

\[
 \sup_{t\ge0}d(t)\le A_Le^{a_L(Y+\ell_n\sqrt nY^2)}
 \left\{\frac{B_0Y^{3/2}}{P^{3/2}}+
 \frac{Y^{5/2}\sqrt{1+(\ell_n\sqrt nY^2)^2+\log(e+P)}}{P^2}\right\}.
 \tag{31}
\]

This also bounds the fitted-limit discrepancy and the smaller mobility
Hilbert distance. No conversion factor depending on depth is needed in
that direction.

## 4. Joint order, label threshold, and the actual prefactor

There is a useful option that retains the full label range on which the
source coefficients were proved. Define

\[
 \eta_L=a_L(Y+\chi).
\]

If `P>=exp(2eta_L)`, the same calculation just below, using
`chi<=eta_L<=log(P)/2`, gives

\[
 \sup_t d(t)\le\frac{3A_LY^{5/2}}P.
 \tag{32a}
\]

There is no extra label reduction and no exponential hidden in this
prefactor: the order pays for both terms of the activity exponent.
For zero initial readout the sufficient order is
`P>=(1+eta_L)exp(eta_L)`, with prefactor `2A_LY^(5/2)`.
Monotonicity in `P` reduces verification to that lower endpoint;
`log(e+P)<=2+log(1+eta_L)+eta_L` there, and the square-root ratio
is at most `(2+eta_L)/(1+eta_L)<=2`.

The original order condition, depending only on `chi`, instead has the
following explicit label/prefactor tradeoff.

For `P >= exp(2a_L chi)`, multiply (31) by `P`. The initial-jump term
is bounded by `B_0Y^(3/2)`. For the continuous term let `u=log(P)`.
Then `chi<=u/2`, `log(e+P)<=2+u`, and

\[
 \frac{e^{a_L\chi}}P
       \sqrt{1+\chi^2+\log(e+P)}
 \le e^{-u/2}(2+u/2)\le2.
\]

Thus the explicit result, before any further label reduction, is

\[
 \sup_t d(t)\le
 \frac{3A_Le^{a_LY}Y^{5/2}}P\qquad(B_0\le Y).
 \tag{32}
\]

Reduce the allowable label threshold by the additional condition
`Y<=1/a_L`. Then the common width/time/order prefactor can be taken to be
`3e A_L Y_*^(5/2)`, or more coarsely `3e A_L`. The extra smallness cost
is explicit; it has not been hidden in a depth-dependent generic constant.

At `B_0=0`, the smaller sufficient condition with a universal prefactor is

\[
 P\ge (1+a_L\chi)e^{a_L\chi}.
 \tag{33}
\]

To check this, the continuous factor in (31), after multiplication by
`P`, decreases in `P`. At its lower bound write `u=a_Lchi`; then
`chi<=u` and the square root is at most `2+u`, while its prefactor is
`1/(1+u)`. Its ratio is at most two. Hence (32) improves to constant
`2A_L exp(a_LY)Y^(5/2)`. If one retains instead the original threshold
`(1+chi)exp(a_Lchi)`, the explicit available constant is
`A_L exp(a_LY)sqrt(4+a_L)Y^(5/2)`: the logarithm of that threshold
contributes a genuine `sqrt(a_L)` cost in this elementary estimate.
Either version remains singly exponential under the envelopes below.

## 5. A simple depth envelope and the critical-gain case

The recurrences above are the primary quantitative statement. For a
coarse closed expression suppose the initialization operator bound is at
most `D`, and put

\[
 H=4\max\{1,C_{\rm leg}+1,X,D,R_1,\max_la_l,\max_ls_l\},
 \qquad \nu=1+\lambda^{-1}.
 \tag{34}
\]

The following conservative envelopes suffice:

\[
 A_L\le H^{160L}\nu^{12},\qquad
 a_L\le H^{80L}\nu^6.
 \tag{35}
\]

They are intentionally loose, but have fixed exponents and expose the gap.
For verification, direct induction and the finite sums above give the
following intermediate upper bounds. Each entry may be used uniformly in
its layer index; enlarging an entry only improves later upper bounds.

| Coefficient group | An upper bound |
| --- | --- |
| `M_l,Q_0` | `H^(3L)` |
| `q_l,q_l^0` | `H^(2L)` |
| `c_S,c_T` | `H^(4L) nu` |
| `b,b_l` | `H^(10L) nu` |
| `v_l` | `H^(24L) nu^(3/2)` |
| `e_l,E_*,V_l` | `H^(36L) nu^(5/2)` |
| `t_l` | `H^(42L) nu^(5/2)` |
| `d_l^0,d_l^1` | `H^(56L) nu^(7/2)` |
| `J_*` | `H^(13L) nu` |
| `R_r` | `H^(50L) nu^(7/2)` |
| `B_l` | `H^(64L) nu^(11/2)` |
| `A_src` | `H^(90L) nu^7` |
| `z_l,f_l` | `H^(8L)` |
| `j_l,p_l` | `H^(22L) nu` |
| `G_0,G_eta,G_chi` | `H^(41L) nu^2` |
| `T_*` | `H^(16L) nu` |
| `F_*` | `H^(31L) nu^3` |
| `c_0,c_1` | `H^(60L) nu^4` |

For example (5) has source at most `H^(19L)nu^(3/2)` and multiplier
at most `H^3`; summing at most `L` terms gives its listed bound. Equations
(8), (11), (19), and (20) likewise have propagation multipliers at most
`H^2`; their source terms and a factor `L<=H^L` give the displayed
bounds. The terminal cutoff in (15) contributes one additional
`nu` to `R_r b_l`; feedback contributes `T_*J_*/lambda` and
`c_T/lambda`, as explicitly recorded in (27) and (30).
The margins between this table and (35) absorb fixed numerical sums and
the maxima with one; no parameter dependence is absorbed in an unspecified
constant. After `Y<=1/a_L`, (32) is therefore a single-exponential depth
bound on its joint order region. Without that label reduction one must
retain `exp(a_LY)`.

A useful improvement is available when the *actual segment gains* are
controlled. Suppose `X,D,s_l,M_l` are bounded independently of depth and
every contiguous product of `s_lD` is bounded independently of depth.
Then (3), (5), (8), (11), (19), and (20) are sums of at most polynomially
many bounded products. Explicitly, with constants depending only on these
fixed gain/feature bounds and `C_leg`, the recurrences give

\[
 A_L\le C(L+1)^6\nu^{10},\qquad
 a_L\le C(L+1)^4\nu^5.
 \tag{36}
\]

For transparency, their orders are
`v_l=O(L nu^(3/2))`, `t_l=O(L^2 nu^(5/2))`,
`d_l^1=O(L^3 nu^(7/2))`, `B_l=O(L^3 nu^(11/2))`,
`A_src=O(L^5 nu^7)`, `F_*=O(L nu^3)`, and
`c_1=O(L^4 nu^4)`. The factors in (5) contribute at most `e`.
These statements are bounds on the explicit recurrences, conditional on
the listed gain/feature assumptions and the already proved bootstrap.

For instance, a justified tube `D=K+1/L` with `K>=1` and `s_lK<=1`
has each segment product at most `(1+1/(KL))^L<=e`. If feature RMS
bounds also remain fixed, (36) applies. The gain condition alone does not
force bounded features when nonzero offsets accumulate, so that feature
condition must be checked or its actual growth included in (1).

Finally, `lambda=lambda_L` is the initialized top-feature Gram gap. Its
positivity at each fixed depth supplies **no quantitative lower bound
uniform in depth**. Saturation, contracting gains, or near-dependence of
sample features can make it arbitrarily small. Even the critical-gain
case therefore has a polynomial statement only in `L` and
`1/lambda_L`, not an unconditional polynomial statement in `L` alone.
With uniform elementary layer bounds, (35) reads
`exp(O(L))(1+1/lambda_L)^12` for `A_L` and
`exp(O(L))(1+1/lambda_L)^6` for `a_L`; a faster degeneration of the gap
must be paid for explicitly. None of these sufficient bounds establishes
optimal or necessary depth/order scaling.

## 6. Compatibility with the sharper source coefficients

The supervisor's separate source note `DEPTH_SMALL_LABEL_SOURCE.md`
supplies the full label threshold in its (6), source coefficients `S_0,S_1`
in its (25), and the following convenient envelope. In this section only,
write `lambda=min(1,lambda_L)`, `v=max_l s_l`, `a=max_l a_l`, and

\[
 \mathcal H_L=64e^{v+1}(1+X+A_0+a+v+K)^4(L+1)
                  \max\{1,vK\}^{L}.
 \tag{37}
\]

Its source estimates give `c_T<=mathcal H_L^2/lambda`,
`M_l<=mathcal H_L`, `b<=mathcal H_L^4/lambda`,
`b_l<=mathcal H_L^6/lambda`, and each layer-gain segment product at most
`mathcal H_L`. Insert those already proved coefficients directly into
Section 3; Sections 1--2 and their optional label tightening are unnecessary
for this combination. The following powers verify the resulting envelope
using only the finite feedback recurrences:

| Feedback coefficient | Upper bound, with `H=mathcal H_L` |
| --- | --- |
| `q_l` | `H^2` |
| `f_l,z_l` | `H^4`, `H^6` |
| `j_l,p_l` | `H^9/lambda`, `H^16/lambda` |
| `G_0,G_eta,G_chi` | `H^19/lambda^2`, `H^12/lambda`, `H^26/lambda^2` |
| `U,V,W,Z` | `H^9/lambda`, `H^5`, `H^12/lambda`, `H^19/lambda` |
| `T_*,J_*,F_*` | `H^10/lambda`, `H^7/lambda`, `H^18/lambda^3` |
| `c_0,c_1` | `H^30/lambda^4`, `H^37/lambda^4` |

For example unrolling (19) bounds a forward-difference source by `H^2`,
each propagating segment by `H`, and the number of terms by `L<=H`;
the actual definition of `H` leaves numerical slack for their sums.
For `p_l`, (20) has source at most `H^13/lambda`; summing the propagated
sources gives at most `H^16/lambda`, including its top boundary term.
In (22), the largest ordinary `x` summands before summing layers are
`H^17/lambda^2`, and the curvature summands are `H^24/lambda^2`;
summing and the factors two give the table. Finally (27) introduces
`T_*/lambda`, so its largest terms are `2H^29/lambda^4` and
`2H^36/lambda^4`. Since `H>=64`, the next power covers all numerical
sums. No new scientific estimate is required for this bookkeeping.

With the two source coefficients kept separate, take

\[
 A_L=\max\{1,F_*\max(S_0,S_1)\},\qquad
 a_L=\max\{1,c_Tc_0,c_Tc_1\}.
\]

The source bounds `S_0<=H^17lambda^(-3/2)` and
`S_1<=H^54lambda^(-6)` give

\[
 A_L\le\mathcal H_L^{72}\lambda^{-9},\qquad
 a_L\le\mathcal H_L^{39}\lambda^{-5}.
 \tag{38}
\]

Thus the source note's **unchanged full label threshold** and the full
activity-exponent order choice `P>=exp(2a_L(Y+chi))` give the explicit
width/time-uniform prefactor `3mathcal H_L^72lambda^(-9)Y^(5/2)`.
The zero-readout order option in Section 4 has prefactor twice, instead
of three times, `mathcal H_L^72lambda^(-9)Y^(5/2)`. Since
`mathcal H_L=O((L+1)max(1,vK)^L)` with the elementary input bounds fixed,
this is polynomial in depth and inverse gap when `vK<=1`, and singly
exponential in depth times a polynomial inverse-gap cost when `vK>1`.
Any degeneration of `lambda_L` remains separate, as it must.

For a stationary common initial residual, or `Y=0` with `B_0=0`, both
physical paths coincide identically; the same bounds hold without using
the normalized residual direction or a clock change.
