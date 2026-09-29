# Explicit depth dependence of the small-label bootstrap and source bounds

Scoped author derivation, 28 September 2026. Scientific inputs were the
complete `ACTIVATION_SMALL_LABEL_ROUTE.md` and `ACTIVATION_EXTENSION.md` in
this study. The `solve-math-rigorously` skill was read and applied. This note
does not use other studies, experiments, literature, or additional book/code
inputs. It is not an independent review or promoted result. The supervisor
handles the separate comparison/feedback argument.

The potentially superexponential depth loss in the old squared-energy
recursion is avoidable. Take a hidden-operator tube of radius `1/L`, apply
the triangle inequality before squaring the clock derivative norm, and use
label smallness on the defect contribution to its propagation coefficient.
The resulting explicit recurrences have only ordinary products of layer
gains. They even give polynomial depth dependence when the common gain
bound satisfies `v K <= 1`, provided the initial Gram gap is retained as an
explicit parameter.

## 1. Setup and computable constants

Use exactly the network, raw autonomous closure, initialization, residual
clock, and normalized norms of the two input notes. In particular `L>=2`,
`B_0<=Y`, and the actual initial feature Gram obeys
`Gamma_w(0)>=lambda_L I`. The activations may differ by layer and satisfy
`phi_l in C^{1,1}_loc`, `a_l=|phi_l(0)|`, and
`s_l=sup_R |phi_l'|<infinity`. Values of the activations need not be bounded.
Write `X=max_a ||x_a||/sqrt(d)`, and use the supplied initial bounds `K,A_0`.
For convenient treatment of large gaps set

\[
 \lambda=\min\{1,\lambda_L\},\qquad r_L=L^{-1},\qquad D=K+r_L.
 \tag{1}
\]

All recurrences below are finite scalar computations from these inputs.
Define forward bounds and the activity/readout coefficients by

\[
 M_1=a_1+s_1(A_0+1),\qquad
 M_l=a_l+s_lD M_{l-1}\quad(2\le l\le L),
\]
\[
 Q=1+M_L,\qquad c=4Q/\lambda,\qquad b=1+2M_Lc,
\]
\[
 b_L=s_Lb,\qquad b_l=s_lD b_{l+1}\quad(l<L).
 \tag{2}
\]

Thus, on the activity cap `S=cY` and tube, the readout RMS is at most `bY`
and the layer-`l` backward-response RMS is at most `beta_l=b_lY`.
Let

\[
 T_b=\max_{2\le l\le L}b_lM_{l-1}.
 \tag{3}
\]

The energy coefficients are

\[
 e_1=2s_1X^2b_1,
 \qquad
 e_l=2s_lb_lM_{l-1}^2+s_lD(1+L^{-1})e_{l-1}.
 \tag{4}
\]

Set

\[
 f_l=\sqrt c\,e_l,\qquad
 d_l=64b_lf_{l-1}\quad(l\ge2),\qquad
 J=\sum_{l=2}^L b_lM_{l-1}d_l.
 \tag{5}
\]

Interpret a threshold whose denominator vanishes as `+infinity`. One
fully explicit sufficient threshold is

\[
 Y_* =\min\left\{
 1,\frac1c,\frac{D}{2\sqrt2\,L T_b},
 \left(\frac{r_L}{4\sqrt{2c}\,T_b}\right)^{2/3},
 \left(\frac1{4X^2b_1c}\right)^{1/2},
 \left(\frac{\lambda}{4M_Lce_L}\right)^{1/2},
 \left(\frac{\lambda}{2J}\right)^{2/7}
 \right\}.
 \tag{6}
\]

It is positive. These constants require only the slopes and values at zero;
no derivative-Lipschitz modulus appears in this bootstrap threshold.

## 2. Bootstrap, including every order

For each dense trajectory and every original closure of order `P>=1`, if
`0<Y<=Y_*`, the following hold for all time:

\[
 \|W_l(t)\|_{\rm op}<D\quad(l\ge2),\qquad
 \max_a\|z_{1,a}(t)\|_2/\sqrt n<A_0+1,
\]
\[
 \max_a\|h_{l,a}(t)\|_2/\sqrt n\le M_l,\qquad
 \|w(t)\|_2/\sqrt n\le bY,\qquad
 \max_a\|\delta_{l,a}(t)\|_2/\sqrt n\le b_lY,
\]
\[
 \Gamma_w(t)\succeq(\lambda_L-\lambda/2)I
                  \succeq\lambda_L I/2,
 \qquad \rho(t)\le QY e^{-\kappa t},
 \qquad \int_0^\infty\rho(t)dt\le 2QY/\lambda=cY/2,
 \quad \kappa=\lambda/2.
 \tag{7}
\]

For the closure, with `Z_l` the mean squared clock derivative energy and
`E_l` the physical hidden-block velocity defect,

\[
 Z_l(t)\le c e_l^2Y^3=f_l^2Y^3,
 \quad \|E_l(t)\|_F\le d_lY^{5/2}\rho(t),
 \quad \|J_{\rm pred}E(t)\|_m\le JY^{7/2}\rho(t).
 \tag{8}
\]

Here `J_pred` is the prediction Jacobian, whereas the scalar `J` was
defined in (5). Moreover

\[
 \varepsilon_P:=\int_0^\infty\sum_{l=2}^L\|E_l(t)\|_Fdt
 \le {C_0Y^3\over\sqrt{P(P+1)}},
 \qquad C_0=2c\sum_{l=2}^L b_le_{l-1}.
 \tag{9}
\]

Here and below every constant is independent of `n,P,t,Y` within (6).

To prove these statements, stop on the indicated tube and on `s(t)=S=cY`.
The readout equation and backward induction give (2). Projection
contraction in the raw reconstruction and the initial zero backward prefix
give

\[
 \|\widehat W_l-W_{l,0}\|_F
 \le2\sqrt{2c}\,b_lM_{l-1}Y^{3/2}\le r_L/2,
\]
\[
 \max_a\|z_{1,a}(t)-z_{1,a}(0)\|_2/\sqrt n
 \le2X^2b_1cY^2\le1/2.
 \tag{10}
\]

The dense displacement is bounded by `2S beta_l M_(l-1)` and hence obeys
the same bound since `S<=1`. The projection-energy estimate in the source
note, with `A=1+S<=2`, is

\[
 \int_0^t\rho\|E_l/\rho\|_F^2ds
 \le2A^2\beta_l^2 Z_{l-1}(t).
 \tag{11}
\]

Apply the triangle inequality in the joint `L2` space of clock, sample,
and neuron to the three differentiated forward terms. This gives

\[
 \sqrt{Z_l}\le s_l\left[
 2\sqrt S\,\beta_lM_{l-1}^2+
 \left(D+\sqrt2A\beta_lM_{l-1}\right)\sqrt{Z_{l-1}}
 \right].
 \tag{12}
\]

The third threshold in (6) ensures
`sqrt(2)A beta_l M_(l-1)<=D/L`. Also
`sqrt(Z_1)<=2sqrt(S)s_1X^2 beta_1`. Induction in (12) proves (4) and
the first part of (8). In particular no product of large `M_l` factors is
inserted into the energy propagation coefficient.

For the endpoint estimate, use the Hilbert norm
`||q||_H^2=(mn)^-1 sum_a ||q_a||_2^2` throughout. At every clock point,
`||b_l||_H<=beta_l`, because the residual direction has sample RMS one.
Thus the endpoint projection inequality requires no extra `sqrt(m)`.
The endpoint Legendre kernel satisfies `||K_P||_1<=32sqrt(P)`; a numerical
verification from the input proof is supplied below. Consequently

\[
 \|b_l-b_l^*\|_H\le33\sqrt P\,\beta_l,\qquad
 \|h_l-h_l^*\|_H\le\sqrt{A/(3P)}\sqrt{Z_l}.
 \tag{13}
\]

The second inequality follows from the exact squared endpoint multiplier
`A P/(4P^2-1)<=A/(3P)`. The rank-one defect identity and Cauchy--Schwarz
in samples now give

\[
 \|E_l\|_F/\rho
 \le66\sqrt{2/3}\,\beta_l\sqrt{Z_{l-1}}
 \le64\beta_l\sqrt{Z_{l-1}},
 \tag{14}
\]

which proves the defect bound in (8). The prediction differential of the
hidden block has norm at most `beta_l M_(l-1)||E_l||_F`, proving its last
bound. The integrated forward/backward projection-tail product gives (9).

The top feature displacement is at most `sqrt(S Z_L)<=ce_LY^2` in mean
RMS. Thus its Gram drift is at most `2M_Lce_LY^2<=lambda/2`. The residual
equation `dot r=-2Gamma r+J_pred E` then gives
`dot rho<=-(lambda-JY^(7/2))rho<=-kappa rho`. This implies activity at
most `cY/2`, and excludes the activity exit along with the strict spatial
margins in (10). At fixed finite width and order the raw ODE is locally
Lipschitz, including at zero residual, and its coordinates stay bounded on
the activity cap. Finite-time continuation is therefore available. The
same argument with `E=0` covers the dense path. The bounds below show
integrable parameter velocities, hence finite interpolating limits.
Stationary initial residual and `Y=0` have the constant fitted solution.

For completeness, a numerical bound on the endpoint kernel follows from
the Legendre calculation in the input. For degree `j>=1`, its midpoint
energy is at most `2/j`, so on `1/j<=theta<=pi/2`,

\[
 |\partial_\theta L_j(\cos\theta)|
 \le\sqrt{2/j}\left\{\frac{3j}{2\sqrt{\sin\theta}}
                         +\frac1{\sin^{3/2}\theta}\right\}.
\]

Using `sin(theta)>=2theta/pi`, the first term integrates to at most
`(3pi/sqrt(2))sqrt(j)<7sqrt(j)`, and the second to at most
`2sqrt(2)(pi/2)^(3/2)<6<=6sqrt(j)`. On `[0,1/j]`, the derivative bound
`|L_j'|<=j(j+1)/2` contributes at most `1/2`. Parity hence bounds the
total variation by `27sqrt(j)`. The identity
`K_P=(p'_P+p'_(P-1))/2` gives `||K_P||_1<=27sqrt(P)<=32sqrt(P)`;
degree zero has zero variation and `P=1` is also covered.

## 3. Explicit physical speeds and backward-source tails

The following deliberately uses `Y<=1`, so the constants can be computed
without solving an implicit threshold condition. Define hidden and
preactivation speed coefficients

\[
 u_l=2b_lM_{l-1}+d_l\quad(l\ge2),\qquad
 p_1=2X^2b_1,
 \qquad p_l=u_lM_{l-1}+Ds_{l-1}p_{l-1}.
 \tag{15}
\]

Then, on both paths,

\[
 {\|\dot W_1\|_F\over\sqrt n}\le2Xb_1Y\rho,
 \quad\|\dot W_l\|_F\le u_lY\rho,
 \quad{\|\dot w\|_2\over\sqrt n}\le2M_L\rho,
\]
\[
 \max_a{\|\dot z_{l,a}\|_2\over\sqrt n}\le p_lY\rho,
 \qquad
 \max_a{\|\dot h_{l,a}\|_2\over\sqrt n}\le s_lp_lY\rho.
 \tag{16}
\]

For use in a local gate modulus take

\[
 R=\max\{A_0+1,\max_{2\le l\le L}DM_{l-1}\},\qquad
 \ell_n=\max_l\operatorname{Lip}
       (\phi_l';[-R\sqrt n,R\sqrt n]),\qquad
 \chi_n=\ell_n\sqrt nY^2.
 \tag{17}
\]

Every visited preactivation coordinate is in this interval. Set

\[
 G=M_L^2+X^2b_1^2+\sum_{l=2}^Lb_l^2M_{l-1}^2,
 \qquad\Lambda=2G+\lambda/2.
 \tag{18}
\]

The exact tangent Gram formula and (8) give
`||dot r||_m<=Lambda rho` and
`rho(0)e^(-Lambda t)<=rho(t)<=rho(0)e^(-kappa t)`.
For the backward derivative define two scalar sequences downward:

\[
 A_L=2s_LM_L,\qquad C_L=bp_L,
\]
\[
 A_l=s_lDA_{l+1}+s_lu_{l+1}b_{l+1},\qquad
 C_l=s_lDC_{l+1}+Db_{l+1}p_l\quad(l<L).
 \tag{19}
\]

Almost everywhere in physical time,

\[
 \max_a\|\dot\delta_{l,a}\|_2/\sqrt n
 \le(A_l+C_l\chi_n)\rho.
 \tag{20}
\]

Indeed the differentiated top gate term is at most
`ell_n sqrt(n)bY p_LY rho=bp_L chi_n rho`. Below it the full carrier
has supremum norm at most `sqrt(n)D b_(l+1)Y`; the differentiated matrix
term is at most `s_l u_(l+1)b_(l+1)Y^2rho`. The remaining term propagates
by `s_lD`, giving (19). Local Lipschitz gates have the required almost
everywhere chain rule, so no globally bounded curvature is assumed.

For the initial backward jump use the sharper initial-operator sequence

\[
 g_L=s_L,\qquad g_l=s_lKg_{l+1}\quad(l<L).
 \tag{21}
\]

Its Hilbert RMS is at most `g_l B_0`. Define

\[
 V_l=\frac{16\Lambda^2b_l^2+Q^2(A_l^2+C_l^2)}{\kappa},
 \qquad
 t_l=\sqrt{2V_l/\kappa}+2b_l\sqrt{Q/\kappa}.
 \tag{22}
\]

The actual closure histories have the uniform-in-endpoint tails

\[
 \|(I-\Pi_P)h_l\|_{L^2(H)}\le f_lY^{3/2}/P,
\]
\[
 \|(I-\Pi_P)b_l\|_{L^2(H)}
 \le {3g_lB_0\over\sqrt P}
       +{t_lY\sqrt{1+\chi_n^2+\log(e+P)}\over P}.
 \tag{23}
\]

The second `b_l` here denotes the backward history, whereas in coefficients
`b_l` denotes the scalar from (2). To verify all factors, write the residual
direction as `c_r=r/rho`. It has `||dot c_r||_m<=2Lambda`, and hence

\[
 \|\dot b_l\|_H\le2\Lambda b_lY+(A_l+C_l\chi_n)\rho,
\]
\[
 \int_0^T\|\dot b_l\|_H^2dt
 \le Y^2\left[8\Lambda^2b_l^2T+
 {Q^2\over\kappa}(A_l^2+C_l^2)(1+\chi_n^2)\right].
 \tag{24}
\]

Subtract the initial step, freeze the continuous remainder after
`T=2log(e+P)/kappa`, and use remaining clock mass
`a(t)<=rho(t)/kappa`. The weighted clock derivative energy is at most
`2/kappa` times (24), yielding the first summand of `t_l`. The frozen
remainder error is at most
`2b_l sqrt(Q/kappa)Y^(3/2)/(e+P)`, absorbed by its second summand since
`Y<=1`. A linear ramp of width `tau/P` approximates the initial step with
tail at most `3g_lB_0/sqrt(P)`; for `P=1` use projection contraction.
These arguments prove (23), including `P=1` and the zero jump `B_0=0`.

The integrated rank-one defect identity consequently gives

\[
 \varepsilon_P\le
 S_0{B_0Y^{3/2}\over P^{3/2}}+
 S_1{Y^{5/2}\sqrt{1+\chi_n^2+\log(e+P)}\over P^2},
\]
\[
 S_0=6\sum_{l=2}^Lg_lf_{l-1},\qquad
 S_1=2\sum_{l=2}^Lt_lf_{l-1}.
 \tag{25}
\]

Equations (6), (9), (15)--(22), and (25) give fully computable depth
dependence for the fitting, activity, and source parts of the theorem.
For a particular network the formulas themselves are preferable to the
coarse envelope below.

## 4. A single-exponential envelope, polynomial at subcritical gains

Suppose `a=max_l a_l` and `v=max_l s_l` are bounded independently of depth,
as are `X,K,A_0`. Set

\[
 \gamma=\max\{1,vK\},\qquad
 H_L=64e^{v+1}(1+X+A_0+a+v+K)^4(L+1)\gamma^L.
 \tag{26}
\]

Then the explicit threshold (6) satisfies

\[
 Y_*\ge\lambda^{3/2}H_L^{-10}.
 \tag{27}
\]

All activity, tube, speed, and final source-tail norm coefficients displayed
above (including `C_0,S_0,S_1`, the `Z_l/Y^3` coefficients, and `Lambda`,
but excluding the intermediate squared-energy coefficient `V_l`) are at most

\[
 \mathcal C_L=H_L^{64}\lambda^{-8}.
 \tag{28}
\]

The exponents `10,64,8` are convenient conservative integers, not claimed
optimal. They explicitly rule out an `exp(constant L^2)` loss from this
bootstrap. If `vK<=1`, `gamma=1`, and both the label threshold and all
source constants have polynomial dependence on `L` and inverse Gram gap.
If `vK>1`, (27)--(28) have single-exponential depth dependence times
polynomial factors. Deterioration of `lambda_L` must still be inserted:
no depth-uniform Gram lower bound is implied by bounded slopes/operators.

Here is an explicit check of the envelope. For every segment of at most
`L` layers,

\[
 [v(K+L^{-1})]^j\le e^v\gamma^L,
 \qquad
 [v(K+L^{-1})(1+L^{-1})]^j\le e^{v+1}\gamma^L.
 \tag{29}
\]

Unrolling the forward recursion gives
`M_l<=e^v gamma^L [a+v(A_0+1)+aL]`. Thus `M_l,Q,X^2,v,D,D^-1,L`
and either segment product in (29) are bounded by `H=H_L`. The following
bounds follow by unrolling each recurrence once; at most `L` source terms
and one segment product occur, contributing at most `H^2`:

| Quantity | Upper bound |
| --- | --- |
| `c` | `H^2 lambda^-1` |
| `b` | `H^4 lambda^-1` |
| `b_l` | `H^6 lambda^-1` |
| `T_b` | `H^7 lambda^-1` |
| `e_l` | `H^12 lambda^-1` |
| `f_l` | `H^13 lambda^-3/2` |
| `d_l` | `H^20 lambda^-5/2` |
| `J` | `H^28 lambda^-7/2` |
| `u_l` | `H^22 lambda^-5/2` |
| `p_l` | `H^25 lambda^-5/2` |
| `A_l,C_l` | `H^34 lambda^-7/2` |
| `Lambda` | `H^18 lambda^-2` |
| `V_l,t_l` | `H^72 lambda^-8`, `H^39 lambda^-9/2` respectively |
| `g_l` | `H^2` |
| `C_0,S_0,S_1` | `H^22 lambda^-3`, `H^17 lambda^-3/2`, `H^54 lambda^-6` respectively |

`V_l` is an auxiliary squared derivative-energy coefficient rather than a
source/tail constant; it need not satisfy (28). Likewise (28) is for the
actual norm/speed coefficients, not arbitrary products or squares of them.
For example `ce_l^2<=H^26lambda^-3` and the sum of relative defects is
at most `H^21lambda^-5/2`, both covered by (28).

The nontrivial lower bounds on the seven positive entries of (6), in
their displayed order, are respectively

\[
 1,\quad \lambda H^{-2},\quad\lambda H^{-10},\quad
 \lambda H^{-20/3},\quad\lambda H^{-5},\quad
 \lambda^{3/2}H^{-8},\quad\lambda^{9/7}H^{-58/7}.
\]

Since `0<lambda<=1` and `H>=64`, each is at least
`lambda^(3/2)H^-10`, proving (27). The entire construction retains all
orders and all times; no order requirement was used to get fitting or
source regularity. A joint order/width restriction enters only when the
separate feedback comparison absorbs the local-curvature factor.
