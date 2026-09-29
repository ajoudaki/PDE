# Depth-explicit, width- and time-uniform small-label tracking

Author synthesis, 28 September 2026. This continues the multi-input old-clock
investigation in this study. It combines the complete explicit derivations in
[DEPTH_SMALL_LABEL_SOURCE.md](DEPTH_SMALL_LABEL_SOURCE.md) and
[DEPTH_SMALL_LABEL_FEEDBACK.md](DEPTH_SMALL_LABEL_FEEDBACK.md), whose source
inputs are the activation-general proofs already in this study. These are
internally checked author results, not independent promotion reviews. No
experiment, external literature search, or paper/book change is involved.

The result makes three quantities explicit together: the admissible label
size, the tracking prefactor, and the required order. It does not prove a
fixed-order width-uniform estimate. It does not assert an optimal dependence
on depth, or an initial Gram gap bounded uniformly over depths/datasets.

## 1. Model, metric, and initialization

There are L>=2 hidden layers of common width n, m fixed training inputs,
and scalar output. For sample a,

\[
 z_{1,a}=W_1x_a/\sqrt d,\quad
 z_{l,a}=W_lh_{l-1,a},\quad h_{l,a}=\phi_l(z_{l,a}),\quad
 f_a=w^\top h_{L,a}/n.
\]

Write r=f-y, rho=||r||_m, Y=||y||_m, with the mean-square sample norm.
The canonical flow for loss rho^2 has first/readout mobilities n and
hidden-matrix mobilities one. In particular,

\[
 \delta_L=w\odot\phi_L'(z_L),\quad
 \delta_l=\phi_l'(z_l)\odot W_{l+1}^{\top}\delta_{l+1},
\]
\[
 \dot W_1=-\frac2m\sum_a r_a\delta_{1,a}(x_a/\sqrt d)^\top,\quad
 \dot W_l=-\frac2{mn}\sum_a r_a\delta_{l,a}h_{l-1,a}^\top,\quad
 \dot w=-\frac2m\sum_a r_ah_{L,a}.
\]

The closure keeps W_(l,0) exactly. Its clock is
`tau=1+integral rho`, with its **own** residual. For each layer/sample it
stores the first P shifted Legendre moments of h_(l-1,a) and
b_(l,a)=(r_a/rho)delta_(l,a), in clock measure. The prefix [0,1] has
constant initial h and zero b. The physical moment sources are rho h and
r delta, so the algorithm never divides by rho. Reconstruction is

\[
 \widehat W_l=W_{l,0}-\frac2{mn\tau}
 \sum_{a,k<P}(2k+1)M^b_{l,a,k}(M^h_{l-1,a,k})^\top.
\]

The moment derivative with physical source q is

\[
 \dot M_k=q-\frac\rho\tau
       \left[kM_k+\sum_{j<k}(2j+1)M_j\right].
\]

Outer weights follow their canonical equations using current reconstructed
responses. Thus this is the actual autonomous closure, not a dense-driven
oracle. Use the block-sum discrepancy

\[
 d_n(\widehat\theta,\theta)=
 \frac{\|\widehat W_1-W_1\|_F}{\sqrt n}
 +\sum_{l=2}^L\|\widehat W_l-W_l\|_F
 +\frac{\|\widehat w-w\|_2}{\sqrt n}.
 \tag{1}
\]

It also dominates the corresponding mobility Hilbert distance.

Assume phi_l belongs to C^{1,1}_loc, its global slope bound is s_l<infinity,
and a_l=|phi_l(0)|. Bounded activation values are not required. Assume

\[
 X=\max_a\|x_a\|/\sqrt d<\infty,\quad
 \max_a\|z_{1,a}(0)\|/\sqrt n\le A_0,\quad
 \|W_{l,0}\|_{\rm op}\le K\quad(l\ge2),
\]
\[
 B_0=\|w_0\|/\sqrt n\le Y,\qquad
 \Gamma_w(0)=\left[\frac{\langle h_{L,a}(0),h_{L,b}(0)\rangle}{mn}\right]_{ab}
 \succeq\lambda_L I_m,
 \qquad\lambda=\min\{1,\lambda_L\}>0.
 \tag{2}
\]

These bounds, including the gap, must hold uniformly over the width family.
They are deterministic initialization hypotheses; the separate initialization
result establishes appropriate high-probability events for fixed compatible
data/depth and covered Gaussian initializations. The case Y=0 under B_0<=Y
is stationary. Below take Y>0. No condition is imposed on m beyond finiteness
and (2); dependence on sample geometry/number is retained through X and
lambda_L.

## 2. Exact computable constants

The formulas in this section are sharper than the closed envelope below.
All are finite recurrences independent of width, order, and time.
Take a middle-matrix tube radius 1/L and set D=K+1/L. Define

\[
 M_1=a_1+s_1(A_0+1),\quad M_l=a_l+s_lDM_{l-1},\quad
 Q=1+M_L,\quad c=4Q/\lambda,\quad b=1+2M_Lc,
\]
\[
 q_L=s_L,\quad q_l=s_lDq_{l+1},\quad b_l=bq_l,\quad
 T_b=\max_{l\ge2}b_lM_{l-1},
\]
\[
 e_1=2s_1X^2b_1,\quad
 e_l=2s_lb_lM_{l-1}^2+s_lD(1+1/L)e_{l-1},\quad
 v_l=\sqrt c\,e_l,\quad d_l=64b_lv_{l-1},\quad
 J=\sum_{l=2}^Lb_lM_{l-1}d_l.
 \tag{3}
\]

A sufficient label threshold is exactly

\[
 Y_*^{\rm src}=\min\left\{
 1,c^{-1},\frac{D}{2\sqrt2 LT_b},
 \left(\frac1{4L\sqrt{2c}T_b}\right)^{2/3},
 (4X^2b_1c)^{-1/2},
 \left(\frac\lambda{4M_Lce_L}\right)^{1/2},
 \left(\frac\lambda{2J}\right)^{2/7}
 \right\}.
 \tag{4}
\]

A zero denominator imposes no restriction. No extra reduction of this
threshold is needed for the main order condition below.

For the source coefficients, set kappa=lambda/2 and

\[
 u_l=2b_lM_{l-1}+d_l,\quad
 p_1=2X^2b_1,\quad p_l=u_lM_{l-1}+Ds_{l-1}p_{l-1},
\]
\[
 \Lambda=2\left(M_L^2+X^2b_1^2+\sum_{l=2}^Lb_l^2M_{l-1}^2\right)+\lambda/2,
\]
\[
 A_L^b=2s_LM_L,\quad C_L^b=bp_L,\qquad
 A_l^b=s_lDA_{l+1}^b+s_lu_{l+1}b_{l+1},\quad
 C_l^b=s_lDC_{l+1}^b+Db_{l+1}p_l,
\]
\[
 g_L=s_L,\quad g_l=s_lKg_{l+1},\quad
 V_l=\frac{16\Lambda^2b_l^2+Q^2[(A_l^b)^2+(C_l^b)^2]}\kappa,
\]
\[
 t_l=\sqrt{2V_l/\kappa}+2b_l\sqrt{Q/\kappa},\qquad
 S_0=6\sum_{l=2}^Lg_lv_{l-1},\quad
 S_1=2\sum_{l=2}^Lt_lv_{l-1}.
 \tag{5}
\]

For feedback, the following recurrences require only the already proved
tube and activity bounds. They do not require the optional smaller
threshold in the feedback component's separate source derivation.
Define the forward-difference coefficients

\[
 z_1^\Delta=X,\quad f_1^\Delta=s_1X,\quad
 z_l^\Delta=M_{l-1}+Df_{l-1}^\Delta,\quad
 f_l^\Delta=s_lz_l^\Delta,
\]

and the backward-difference coefficients

\[
 j_L=0,\quad k_L=bz_L^\Delta,\quad
 j_l=s_l(Dj_{l+1}+b_{l+1}),\quad
 k_l=s_lDk_{l+1}+Db_{l+1}z_l^\Delta.
\]

Put u_1^Delta=X, u_l^Delta=M_(l-1) for l>=2, and

\[
 G_0=2M_Lf_L^\Delta+2\sum_{l=1}^Lb_lj_l(u_l^\Delta)^2
                  +2\sum_{l=2}^Lb_l^2M_{l-1}f_{l-1}^\Delta,
\]
\[
 G_r=2\sum_{l=1}^Lb_lq_l(u_l^\Delta)^2,\qquad
 G_c=2\sum_{l=1}^Lb_lk_l(u_l^\Delta)^2,
\]
\[
 U=2\sum_{l=1}^Lb_lu_l^\Delta,\quad
 V=2\sum_{l=1}^Lq_lu_l^\Delta,\quad
 W=2\sum_{l=1}^Lj_lu_l^\Delta+2\sum_{l=2}^Lb_lf_{l-1}^\Delta,\quad
 Z=2\sum_{l=1}^Lk_lu_l^\Delta,
\]
\[
 T_*=2M_L+U,\quad J_*=T_b,\quad F_*=1+T_*J_*/\lambda,
\]
\[
 c_0=\max\{2f_L^\Delta+W+2T_*G_0/\lambda,
                         V+2T_*G_r/\lambda\},\quad
 c_1=Z+2T_*G_c/\lambda,
\]
\[
 \boxed{A_L=\max\{1,F_*\max(S_0,S_1)\},\qquad
 a_L=\max\{1,\tfrac c2c_0,\tfrac c2c_1\}.}
 \tag{6}
\]

These are the explicit source/feedback coefficients used in the theorem.
They do not hide products of gains or inverse-gap factors.

## 3. The theorem and its width/order region

Let 0<Y<=Y_*^src. Define

\[
 R=\max\{A_0+1,DM_1,\ldots,DM_{L-1}\},\quad
 \ell_n=\max_l\operatorname{Lip}(\phi_l';[-R\sqrt n,R\sqrt n]),
 \quad\chi_n=\ell_n\sqrt nY^2,
 \quad\eta_n=a_L(Y+\chi_n).
 \tag{7}
\]

Both dense and every finite-order autonomous closure exist for all time and

\[
 \rho_D(t),\widehat\rho_P(t)\le QY e^{-\lambda t/2}.
 \tag{8}
\]

For every n,P, before imposing any relation between them,

\[
 \boxed{\sup_{t\ge0}d_n(\widehat\theta_P(t),\theta_D(t))
 \le A_Le^{\eta_n}
 \left[
 \frac{B_0Y^{3/2}}{P^{3/2}}+
 \frac{Y^{5/2}\sqrt{1+\chi_n^2+\log(e+P)}}{P^2}
 \right].}
 \tag{9}
\]

Consequently the following sufficient joint order condition gives the
width- and time-uniform result:

\[
 \boxed{P\ge\exp(2\eta_n)\quad\Longrightarrow\quad
 \sup_{t\ge0}d_n(\widehat\theta_P(t),\theta_D(t))
 \le\frac{3A_LY^{5/2}}P.}
 \tag{10}
\]

For zero initial readout, the better condition suffices:

\[
 \boxed{B_0=0,\quad P\ge(1+\eta_n)e^{\eta_n}\quad\Longrightarrow\quad
 \sup_{t\ge0}d_n(\widehat\theta_P(t),\theta_D(t))
 \le\frac{2A_LY^{5/2}}P.}
 \tag{11}
\]

All bounds include the final fitted limits, since physical velocities are
integrable. The label threshold is unchanged in (10)--(11); the factor
exp(a_LY) has been absorbed explicitly into the sufficient order instead.
Alternatively, use only P>=exp(2a_Lchi_n) and retain the prefactor
3A_L exp(a_LY)Y^(5/2), or impose the additional label smallness Y<=1/a_L.
These are different certified trade-offs, not different underlying methods.

### Proof

On the tube ||W_l-W_(l,0)||_op<1/L and first-preactivation displacement
less than one, stop also when accumulated activity reaches cY. Projection
contraction bounds hidden displacement by
2sqrt(2c)b_lM_(l-1)Y^(3/2); first-preactivation displacement is bounded by
2X^2 b_1cY^2. Formula (4) makes these at most 1/(2L) and 1/2.

Let Z_l be the sample/neuron mean squared derivative energy of h_l in
clock measure. Differentiating the reconstruction gives the exact physical
velocity defect

\[
 E_l=\frac{2\rho}{mn}\sum_a
       (b_{l,a}-b^*_{l,a})(h_{l-1,a}-h^*_{l-1,a})^\top.
\]

The stars denote current-endpoint Legendre projections. Differentiating a
projection's squared tail gives rho times its squared endpoint error.
Consequently the forward energy obeys

\[
 \sqrt{Z_l}\le s_l\left[2\sqrt{cY}\,b_lYM_{l-1}^2
 +(D+\sqrt2(1+cY)b_lYM_{l-1})\sqrt{Z_{l-1}}\right].
\]

The third threshold in (4) reduces the propagation multiplier to
s_lD(1+1/L), proving Z_l<=v_l^2Y^3. The forward H1 endpoint estimate
and the endpoint Legendre kernel bound ||K_P||_1<=32sqrt(P) then give
||E_l||_F<=d_lY^(5/2)rho. In the prediction equation the additional
factor is b_lYM_(l-1), so ||JE||_m<=JY^(7/2)rho. The factors sqrt(P)
and 1/sqrt(P) cancel; no order restriction enters this step.

Top-feature Gram drift is at most 2M_Lce_LY^2<=lambda/2. Thus the
residual norm derivative is bounded above by
-(lambda-JY^(7/2))rho<=-lambda rho/2. Activity stays below cY/2,
excluding every stopping exit strictly. Bounded raw moments and the
locally Lipschitz physical ODE give global continuation at every finite
n,P. This proves (8) without assuming closure fitting or stability.

The speed recurrences (5) give
||dot delta_l||_(RMS)<= (A_l^b+C_l^b chi_n)rho and
||dot(r/rho)||_m<=2Lambda. The forward Legendre tail is at most
v_lY^(3/2)/P. Separate the backward prefix jump, whose tail is at most
3g_lB_0/sqrt(P). Freeze its continuous remainder after physical time
2log(e+P)/kappa. The remaining activity divided by current rho is at most
1/kappa, so the weighted Legendre derivative energy removes the inverse
clock speed. Integrating the backward derivative bound until that cutoff
and bounding the remaining tail gives

\[
 Q_{b,l}\le3g_lB_0/\sqrt P+
       t_lY\sqrt{1+\chi_n^2+\log(e+P)}/P.
\]

The exact integrated defect pairing is at most
2 sum_l Q_(b,l)Q_(h,l-1). Therefore

\[
 \varepsilon:=\int_0^\infty\sum_l\|E_l\|_Fdt
 \le S_0B_0Y^{3/2}P^{-3/2}
      +S_1Y^{5/2}\sqrt{1+\chi_n^2+\log(e+P)}P^{-2}.
 \tag{12}
\]

This also proves integrable velocities and fitted limits.

For feedback write d_n=x+z, separating hidden/first-layer discrepancy x
from readout discrepancy z, and h=ell_n sqrt(n). The exact recurrences (6)
follow from forward/backward subtraction; in particular backward discrepancy
at layer l is bounded by q_l z+Y(j_l+h k_l)x. The tangent Gram difference
is bounded by (G_0+G_c chi_n)x+G_rYz. Integrating the damped prediction
discrepancy equation yields, for Q_delta(t)=integral_0^t||fhat-fD||_m,

\[
 Q_\Delta(t)\le\frac2\lambda\int_0^t\rho_D
 [(G_0+G_c\chi_n)x+G_rYz]ds+\frac{J_*Y}\lambda\varepsilon(t).
\]

The readout and hidden difference equations are respectively bounded by
2M_L Q_delta+2f_L^Delta integral rho_D x and
UY Q_delta+integral rho_D[Vz+WYx+ZhYx]+epsilon(t). Combining gives

\[
 d_n(t)\le F_*\varepsilon(t)+
       \int_0^t(c_0+c_1hY)\rho_D(s)d_n(s)ds.
\]

Gronwall with integral rho_D<=cY/2 proves (9).

To check (10), multiply its desired error bound by P and set u=log P.
Here eta_n<=u/2 and chi_n<=eta_n<=u/2. The initial term is at most
B_0Y^(3/2)<=Y^(5/2). Since log(e+P)<=2+u,

\[
 \frac{e^{\eta_n}}P\sqrt{1+\chi_n^2+\log(e+P)}
 \le e^{-u/2}(2+u/2)\le2.
\]

For (11) the same continuous factor is decreasing in P. At
P=(1+eta_n)exp(eta_n), its numerator square root is at most 2+eta_n,
while exp(eta_n)/P=1/(1+eta_n). Their product is at most two.
The initial term vanishes. This proves both claims.

## 4. Closed depth envelope, retaining the Gram gap

For a readable bound set a=max_l a_l, v=max_l s_l and

\[
 g=\max\{1,vK\},\qquad
 H_L=64e^{v+1}(1+X+A_0+a+v+K)^4(L+1)g^L.
 \tag{13}
\]

Then the exact coefficients satisfy

\[
 \boxed{Y_*^{\rm src}\ge\lambda^{3/2}H_L^{-10},\qquad
 A_L\le H_L^{72}\lambda^{-9},\qquad
 a_L\le H_L^{39}\lambda^{-5}.}
 \tag{14}
\]

In particular an explicit sufficient theorem is obtained with
Y<=lambda^(3/2)H_L^-10 and eta_n replaced by
H_L^39 lambda^-5 (Y+ell_n sqrt(n)Y^2) in (10) or (11). Its parameter
tracking prefactor is at most

\[
 \boxed{C_L(Y)=3H_L^{72}\lambda^{-9}Y^{5/2}.}
 \tag{15}
\]

If a prefactor common to all permitted labels is desired, replace Y by
Y_*^src, or use the coarser C_L=3H_L^72 lambda^-9. Keeping Y visible is
more informative. No number in (14)--(15) is an optimality claim.

Here are explicit checks of the powers. Every segment product of s_lD
is at most exp(v)g^L; including the extra factors (1+1/L) changes this
by at most e. Unroll each inhomogeneous recurrence as a sum of at most L
such products. With H=H_L, the source calculation gives
M_l,Q,X^2,v,D,L<=H, c<=H^2/lambda, b<=H^4/lambda,
b_l<=H^6/lambda, S_0<=H^17/lambda^(3/2),
S_1<=H^54/lambda^6, and the first bound of (14).
The feedback recurrences then obey:

| Coefficients | Upper bound |
| --- | --- |
| q_l | H^2 |
| f_l^Delta, z_l^Delta | H^4, H^6 |
| j_l, k_l | H^9/lambda, H^16/lambda |
| G_0, G_r, G_c | H^19/lambda^2, H^12/lambda, H^26/lambda^2 |
| U, V, W, Z | H^9/lambda, H^5, H^12/lambda, H^19/lambda |
| T_*, J_*, F_* | H^10/lambda, H^7/lambda, H^18/lambda^3 |
| c_0, c_1 | H^30/lambda^4, H^37/lambda^4 |

These yield A_L<=H^72/lambda^9 and a_L<=H^39/lambda^5 directly.
Fixed numerical sums fit within the displayed margins since H>=64.

At fixed elementary layer/input bounds, this reads

\[
 C_L(Y)\le C_{\rm base}(L+1)^{72}
                  g^{72L}\lambda^{-9}Y^{5/2},
 \quad
 a_L\le C'_{\rm base}(L+1)^{39}g^{39L}\lambda^{-5}.
 \tag{16}
\]

Thus the layer-gain contribution is single exponential in depth in general,
and polynomial if vK<=1. Offsets may cause features to grow linearly in
this latter case; (14) already includes that growth. If actual feature
bounds and all segment products stay bounded independently of depth, the
sharper recurrence analysis in the feedback note gives instead
A_L<=C(L+1)^6(1+lambda^-1)^10 and
a_L<=C(L+1)^4(1+lambda^-1)^5. Those are a further structured case,
not hypotheses of the general theorem.

## 5. Why lambda_L cannot be removed from a depth claim

Compatibility of the training inputs gives positivity in appropriate
Gaussian initialization limits, not a lower bound independent of depth.
This failure can be extremely strong even with one fixed smooth activation.
For example take phi(z)=0.1 tanh(z)^3 in every layer and canonical Gaussian
hidden initialization. For normalized inputs let q_l be the population
initial second moment of a single feature. Conditional Gaussian rows give
q_l=E[phi(sqrt(q_(l-1))G)^2], with G standard normal. Hence

\[
 q_1\le10^{-2},\qquad
 q_l\le10^{-2}E[(\sqrt{q_{l-1}}G)^6]
       =0.15q_{l-1}^3,
 \qquad q_L\le(10^{-2})^{3^{L-1}}.
\]

For m<=d orthogonal normalized inputs, the Gaussian preactivations for
different samples remain independent at initialization in the population
recursion. This activation is odd, so their cross moments vanish at every
layer. The Gram is exactly (q_L/m)I_m: its gap is strictly positive and
equals q_L/m. Also |phi'|<=0.075, so all activation regularity and slope
bounds are fixed. The gap can therefore be superexponentially small despite
fixed smooth activation, controlled layer gains, and orthogonal fixed data.

This example concerns initialization conditioning and the fitting-rate
certificate. It is **not** a lower bound on actual closure tracking error.
It explains why this theorem yields an explicit function of depth *and*
the initial Gram gap, rather than a universal single-exponential bound
in depth alone over the entire activation/data class.

## 6. Output interpretation and limits of the conclusion

On the training inputs, forward subtraction gives

\[
 \|\widehat f-f_D\|_m\le(M_L+bY f_L^\Delta)d_n.
\]

The output multiplier is at most H_L^9/lambda under the coarse envelope.
Thus the same theorem gives an all-time training-prediction discrepancy
at most 3H_L^81 lambda^-10 Y^(5/2)/P. For a test input ball, the identical
recurrence uses its input radius and an initial full normalized first-layer
matrix bound to bound test features; integrating the pointwise bound gives
test L2 discrepancy and, by the reverse triangle inequality, the difference
between test RMSEs. This is discrepancy from the dense model, not a claim
that either model has small error against unseen target labels.

The constants in (10)--(11) are independent of n,t,P on the stated joint
region. The required order can be extremely large: for globally Lipschitz
gates, it contains exp(constant(L) sqrt(n)Y^2). The theorem therefore does
not yet certify the efficient small orders seen empirically, nor unrestricted
fixed-P width uniformity. All-order fitting (8) needs no such order condition.

Finally, 'the sharpest C_L' is not well-defined without fixing the order
region. Since (9) contains P^(-3/2) and P^(-2), increasing the sufficient
order threshold can absorb even A_L and make the displayed C/P coefficient
universal. Equations (4)--(11) are the substantive statement: they keep the
label threshold, source estimate, feedback amplification, and order cost
visible together. The recurrences are the strongest quantitatively resolved
version here; (14)--(16) are transparent, conservative summaries.

## 7. Sharp extraction of the sufficient order from the displayed bound

Follow-up algebra, 28 September 2026. The simpler schedules (10)--(11)
are valid but discard the actual initial readout size and some polynomial
factors. Put beta=B_0/Y in [0,1] and

\[
 D_n=\sqrt{1+\chi_n^2+\eta_n},\qquad
 P_{\min}=\max\{\beta^2e^{2\eta_n},D_ne^{\eta_n}\}.
 \tag{17}
\]

Then every integer P>=ceil(P_min) satisfies the same all-time bound
3A_LY^(5/2)/P. At beta=0 the coefficient can be replaced by 2.
This is a direct sharpening of the order extraction; no new assumption
or network estimate is introduced.

Indeed multiply (9) by P/(A_LY^(5/2)). Its right side is

\[
 R(P)=e^{\eta_n}\left[
 \frac\beta{\sqrt P}+
 \frac{\sqrt{1+\chi_n^2+\log(e+P)}}P\right].
\]

Both summands decrease with P. The first is at most one when
P>=beta^2 exp(2eta_n). For the second evaluate at P=D_n exp(eta_n).
Since D_n>=1,

\[
 \log(e+D_ne^{\eta_n})
 \le\eta_n+\log D_n+\log(e+1),
\]
\[
 \frac{1+\chi_n^2+\log(e+D_ne^{\eta_n})}{D_n^2}
 \le1+\frac{\log D_n+\log(e+1)}{D_n^2}
 \le1+\log(e+1)<4.
\]

The last inequality follows by differentiating the middle fraction on
D_n>=1. Thus the second summand of R is less than two. Also chi_n<=eta_n,
so D_n<=1+eta_n, confirming the improvement over (11).

The threshold (17) is optimal up to constant factors **for controlling
this particular upper bound by C/P**. To see this, suppose R(P)<=C with
C>0 fixed. Its first summand forces P>=C^-2 beta^2 exp(2eta_n).
Write H=1+chi_n^2+log(e+P). The other summand forces
P>=C^-1 exp(eta_n)sqrt(H). Since H>=1, it also implies
eta_n<=log(e+P)+log_+(C), whence
D_n^2<= [1+log_+(C)]H. Therefore

\[
 P\ge\frac{D_ne^{\eta_n}}{C\sqrt{1+\log_+ C}}.
\]

Together these inequalities prove the claim about the certificate. They
are not lower bounds on actual approximation error or necessary orders
for the algorithm.

For fixed depth, fixed nonzero Y, and a fixed positive global gate-Lipschitz
bound ell, take chi_n=ell sqrt(n)Y^2 and eta_n=a_LY+a_Lchi_n. At zero
readout the certificate scales as chi_n exp(eta_n); for a fixed positive
beta it scales as beta^2 exp(2eta_n). A vanishing nonzero readout must be
inserted into both terms of (17), rather than treated as exactly zero.
This concerns the uniform C/P guarantee; mere convergence or a fixed
accuracy can be obtained under different, weaker order conditions.

The coordinator checked this extraction against a separate prompt-only
algebra derivation by `order_bound_recheck`, which also verified the
constant-factor necessity for the displayed bound. This is an internal
algebra check, not an independent review of the neural theorem.
