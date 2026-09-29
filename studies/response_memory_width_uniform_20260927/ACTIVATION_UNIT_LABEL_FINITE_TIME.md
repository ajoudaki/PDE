# Unit-label finite-time tracking for general activations

28 September 2026. This extends `UNIT_LABEL_JOINT_ORDER.md` to the activation
class in `ACTIVATION_EXTENSION.md`. It concerns the unchanged autonomous
old-clock closure, with multiple training inputs and fixed finite depth.
The proof below includes the continuation argument needed for unbounded
activations. It uses no small-label threshold, initial Gram gap, fitting
assumption, prescribed residual, or assumed closure boundedness. This is
internally checked research in the current study, not promoted book material.

## 1. The precise result

Fix the number of hidden layers `L>=2`, the number of samples `m`, input
dimension `d`, inputs `x_a`, and constants `K,A_0<infinity`. Different layers
may use different activations. Assume

\[
 \phi_\ell\in C^{1,1}_{\rm loc}(\mathbb R),\qquad
 a_\ell=|\phi_\ell(0)|<\infty,\qquad
 v_\ell=\sup_{u\in\mathbb R}|\phi_\ell'(u)|<\infty.
 \tag{1}
\]

The derivative is locally Lipschitz; its Lipschitz constant need not be
globally bounded. The activation itself need not be bounded. In particular,
`|phi_l(u)|<=a_l+v_l|u|`. No oddness, analyticity, monotonicity, nonlinearity,
or nonvanishing derivative is assumed.

At width `n`, use the canonical model

\[
 z_{1,a}=W_1x_a/\sqrt d,\quad h_{\ell,a}=\phi_\ell(z_{\ell,a}),\quad
 z_{\ell,a}=W_\ell h_{\ell-1,a}\ (\ell\ge2),\quad
 f_a=w^Th_{L,a}/n,
\]
\[
 r_a=f_a-y_a,\qquad \rho=\|r\|_m,
 \qquad \|u\|_m^2=m^{-1}\sum_a u_a^2.
 \tag{2}
\]

Backward responses exclude the residual:

\[
 \delta_{L,a}=w\odot\phi_L'(z_{L,a}),\qquad
 \delta_{\ell,a}=\phi_\ell'(z_{\ell,a})\odot
                         W_{\ell+1}^T\delta_{\ell+1,a}.
\]

The loss is `rho^2` and canonical gradient flow has block mobilities
`(n,1,...,1,n)`. Its vector field `F` is

\[
 F_1=-\frac2m\sum_a r_a\delta_{1,a}(x_a/\sqrt d)^T,\quad
 F_\ell=-\frac2{mn}\sum_a r_a\delta_{\ell,a}h_{\ell-1,a}^T,\quad
 F_w=-\frac2m\sum_a r_a h_{L,a}.
 \tag{3}
\]

Assume only the deterministic initial bounds

\[
 \max_{\ell\ge2}\|W_{0,\ell}\|_{\rm op}\le K,\qquad
 \max_a\frac{\|W_{1,0}x_a/\sqrt d\|_2}{\sqrt n}\le A_0,\qquad
 B_0:=\frac{\|w_0\|_2}{\sqrt n}\le1,\qquad Y:=\|y\|_m\le1.
 \tag{4}
\]

Inputs may be coincident, parallel, or otherwise degenerate; labels need not
be interpolable. The initial first-preactivation bound replaces the use of
bounded activation values in the tanh theorem. It is a uniform initial
scale bound, not a condition that labels be small. For bounded activations
and bounded derivative modulus one can retain the less restrictive tanh
initialization formulation.

Let `theta_D` be dense flow and `hat theta_(n,P)` the physical parameters
of the original order-`P` moment closure, initialized at the same network.
Use the mobility distance

\[
 d_n(\theta,\vartheta)^2=
 \frac{\|W_1-V_1\|_F^2}{n}
 +\sum_{\ell=2}^L\|W_\ell-V_\ell\|_F^2
 +\frac{\|w-v\|_2^2}{n}.
 \tag{5}
\]

For every finite `T`, the proof constructs finite constants
`R_T,C_T,Lambda_T>=1`, independent of width, order, and the particular
initialization and labels satisfying (4). They depend only on the fixed
inputs, depth, initial bounds, horizon, and the numbers `a_l,v_l`.
Define the explicit local gate modulus and width factor

\[
 \ell_{n,T}=\max_\ell\operatorname{Lip}
        (\phi_\ell';[-R_T\sqrt n,R_T\sqrt n]),\qquad
 s_{n,T}=1+\sqrt n\,\ell_{n,T},\qquad
 H_{n,T}=e^{\Lambda_T s_{n,T}}.
 \tag{6}
\]

Every modulus in (6) is finite by (1). Then, for every integer order

\[
 \boxed{P\ge\max\{B_0^2H_{n,T}^2,\ s_{n,T}H_{n,T}\},}
 \tag{7}
\]

the closure exists uniquely throughout `[0,T]` and

\[
 \sup_{0\le t\le T}d_n(\widehat\theta_{n,P}(t),\theta_D(t))
 \le C_T H_{n,T}
       \left(\frac{B_0}{P^{3/2}}+\frac{s_{n,T}}{P^2}\right)
 \le\frac{2C_T}{P}.
 \tag{8}
\]

The constants in (6) are enlarged in the proof so (7) also supplies the
fixed minimum order needed for continuation. There is no unmentioned
additional boundedness condition. Two simpler sufficient order choices are

\[
 P\ge\left\lceil e^{2\Lambda_Ts_{n,T}}\right\rceil
       \quad(B_0\le1),\qquad
 P\ge\left\lceil s_{n,T}e^{\Lambda_Ts_{n,T}}\right\rceil
       \quad(w_0=0).
 \tag{9}
\]

Thus the result is width uniform on the stated joint width/order region,
for every prescribed compact time interval. It does not assert a
width-independent `C_T/P` bound at unrestricted fixed order. Unlike the
bounded-tanh theorem, it also does not assert existence through arbitrary
`T` for every low order when the activation is unbounded.

If the derivatives are globally Lipschitz, `ell_(n,T)<=J` with `J` fixed;
the sufficient scale is the same as before:

\[
 \log P\ge C_T(1+\sqrt n).
 \tag{10}
\]

For the merely local class, use (6)--(9). Constants in front of `1/P` remain
width independent, while the required order pays for the larger local
modulus. The value `1` in `Y<=1` and `B_0<=1` can be replaced by any fixed
finite bounds, with corresponding constants. There is no perturbative
label-size requirement in this finite-time theorem.

## 2. The algorithm is unchanged

The closure uses its own residual and its own clock

\[
 \tau(t)=1+\int_0^t\widehat\rho(s)ds.
\]

For each hidden link `ell=2,...,L` and sample, keep `P` forward and `P`
backward vectors. For `k=0,...,P-1` their equations are

\[
 \dot M_k=q-\frac{\widehat\rho}{\tau}
           \left[kM_k+\sum_{j<k}(2j+1)M_j\right].
 \tag{11}
\]

The forward source is `q=rho h_(ell-1,a)`; the backward source is
`q=r_a delta_(ell,a)`, with all fields evaluated in the reconstructed
network. Initially the degree-zero forward moment equals the initial
feature; other forward moments and all backward moments are zero.
Reconstruct

\[
 \widehat W_\ell=W_{0,\ell}
 -\frac2{mn\tau}\sum_{a=1}^m\sum_{k<P}(2k+1)
             M^b_{\ell,a,k}(M^h_{\ell-1,a,k})^T.
 \tag{12}
\]

The first layer and readout follow (3) in this network. No dense-path
information, truncation of activation values, extra state, or new clock
is introduced. The dense path is used only to prove a bound.

Equivalently, on clock space, the forward history equals its initial value
on `[0,1]` and its subsequent actual feature on `(1,tau]`. The backward
history is zero on `[0,1]` and equals
`b_(ell,a)=(r_a/rho)delta_(ell,a)` thereafter. Its only initial jump has
size `b_(ell,a)(1+)`. The moments are integrals of these histories against
`p_k(xi/tau)`, where `p_k(u)=L_k(2u-1)` is the shifted Legendre polynomial.
Polynomial differentiation gives exactly (11).

The raw ODE (11)--(12) is locally Lipschitz in its finite-dimensional
state for every fixed `n,P`: (1) makes the responses locally Lipschitz,
`rho` is a Lipschitz norm, and the only denominator is `tau>=1`.
If the initial residual is zero, all velocities vanish and the theorem
is immediate. Otherwise backward uniqueness prevents the raw solution
from reaching a zero-residual equilibrium at a finite interior time.
Thus division by `rho` below is legitimate before a stopping time;
the algorithm itself never divides by it.

## 3. Dense energy supplies a uniform region

Write `|v|_n` for the increment norm associated with (5). Exact gradient
flow satisfies

\[
 \frac{d}{dt}\mathcal L_D=-|F(\theta_D)|_n^2.
 \tag{13}
\]

Indeed multiplying each squared ordinary gradient by its mobility gives
exactly the squared velocity in this norm. Therefore

\[
 d_n(\theta_D(t),\theta_0)
 \le\int_0^t|\dot\theta_D|_n ds
 \le\sqrt{t\,\mathcal L_D(0)}.
 \tag{14}
\]

To bound the initial loss uniformly, set
`M_1^0=a_1+v_1 A_0` and
`M_l^0=a_l+v_l K M_(l-1)^0`. Forward induction gives initial feature RMS
at most `M_l^0`, so `rho(0)<=Q_0:=1+M_L^0`. Thus let
`D_T=sqrt(T)Q_0`. Equation (14) bounds the dense displacement by `D_T`.
It also proves global dense continuation: at every fixed finite width,
finite-time displacement bounds every physical parameter; local existence
then excludes a finite maximal endpoint.

Consider the closure up to first distance one from the dense path, or
its maximal existence time, whichever comes first. On this interval both
physical paths lie in the convex region

\[
 \|W_\ell\|_{\rm op}\le D:=K+D_T+1\ (\ell\ge2),\qquad
 \|w\|_2/\sqrt n\le B:=2+D_T,
\]
\[
 \max_a\|W_1x_a/\sqrt d\|_2/\sqrt n
 \le A:=A_0+X(D_T+1),\qquad X=\max_a\|x_a\|_2/\sqrt d.
 \tag{15}
\]

The region is convex because every constraint is a norm of a linear
parameter map. On it define

\[
 M_1=a_1+v_1A,\qquad
 M_\ell=a_\ell+v_\ell D M_{\ell-1},\qquad
 R_T=1+\max\{A,DM_1,\ldots,DM_{L-1}\}.
 \tag{16}
\]

Every feature RMS is at most `M_l`; every training preactivation RMS is
at most `R_T`. Consequently every individual preactivation lies within
the interval used in (6), including for every parameter segment in (15).
Backward induction gives fixed bounds

\[
 \beta_L=v_LB,\qquad\beta_\ell=v_\ell D\beta_{\ell+1},\qquad
 \max_a\|\delta_{\ell,a}\|_2/\sqrt n\le\beta_\ell.
 \tag{17}
\]

Finally `rho<=q:=1+BM_L`, accumulated activity is at most `S:=Tq`, and
`tau<=A_c:=1+S`. All constants in (15)--(17) are independent of `n,P`
and of any derivative-Lipschitz modulus. This is a stopped estimate; the
last step of the proof rules out stopping.

## 4. Exact defect and the polynomial estimates

Let `Pi_P` be orthogonal projection onto polynomials of degree below `P`
on `[0,tau]`. For a history `g` set

\[
 D_g=\int_0^\tau\|g-\Pi_Pg\|_2^2d\xi,
 \qquad g^*=(\Pi_Pg)(\tau).
\]

The prefix errors are zero. Orthogonality when differentiating the least
squares optimum gives, almost everywhere,

\[
 \dot D_g=\rho\|g-g^*\|_2^2.
 \tag{18}
\]

The moving endpoint contributes this term; the remaining term pairs the
error against the derivative of a degree-below-`P` polynomial and vanishes.
Differentiating the projected pairing in (12) likewise yields exactly

\[
 \dot{\widehat\theta}=F(\widehat\theta)+E,\qquad E_1=E_w=0,
\]
\[
 E_\ell=\frac{2\rho}{mn}\sum_a
        (b_{\ell,a}-b_{\ell,a}^*)
        (h_{\ell-1,a}-h_{\ell-1,a}^*)^T.
 \tag{19}
\]

In particular, for `e_E=sum_(ell>=2)||E_l||_F`,

\[
 \int_0^t\|E_\ell\|_Fds
 \le\frac2{mn}\sum_a\sqrt{D_{b,\ell,a}(t)D_{h,\ell-1,a}(t)}.
 \tag{20}
\]

This uses `||uv^T/n||_F=(||u||_2/sqrt(n))(||v||_2/sqrt(n))`
and Cauchy--Schwarz in physical time in (18).

Here are the needed polynomial bounds, valid also in the Hilbert space of
all samples and neurons with RMS normalization:

\[
 \|(I-\Pi_P)g\|_{L^2}
 \le\frac{\tau}{2\sqrt{P(P+1)}}\|g'\|_{L^2},
 \tag{21}
\]
\[
 \|g(\tau)-g^*\|\le C\sqrt{\tau/P}\|g'\|_{L^2},\qquad
 \|b^*\|\le C\sqrt P\|b\|_{L^\infty}.
 \tag{22}
\]

The first two require `g in H^1`; the last only requires bounded `b`.
For (21), the equation `-(u(1-u)p_k')'=k(k+1)p_k` gives weighted derivative
orthogonality; Bessel and Parseval bound the tail by
`[P(P+1)]^-1 integral u(1-u)||g'||^2`. Rescale and use `u(1-u)<=1/4`.
For the first inequality of (22), integration by parts in the endpoint
kernel gives the exact identity

\[
 g(\tau)-g^*=\frac12\int_0^\tau
   [p_P(\xi/\tau)+p_{P-1}(\xi/\tau)]g'(\xi)d\xi.
 \tag{23}
\]

The squared norm of its scalar kernel is
`tau[1/(2P+1)+1/(2P-1)]/4`.

For completeness the endpoint kernel has `L^1` norm `O(sqrt(P))`.
It is `K_P=(p_P'+p_(P-1)')/2`, so it suffices to bound the variation of
`L_j` by `C sqrt(j)`. Put
`v(theta)=sqrt(sin(theta)) L_j(cos(theta))` and
`Q=(j+1/2)^2+1/(4sin^2(theta))`. The Legendre equation gives
`v''+Qv=0`, and

\[
 (v^2+(v')^2/Q)'=-Q'(v')^2/Q^2\ge0
       \quad(0<\theta\le\pi/2).
\]

The central values
`L_(2k)(0)=(-1)^k binom(2k,k)/4^k`, `L_(2k+1)(0)=0`, and
`L_j'(0)=jL_(j-1)(0)` bound this energy by `C/j`; the elementary
bound `binom(2k,k)/4^k<=1/sqrt(k+1)` follows by successive ratios.
On `[1/j,pi/2]` this bounds the derivative of `L_j(cos(theta))` by
`C j^-1/2 [j(sin(theta))^-1/2+(sin(theta))^-3/2]`, with integral
`O(sqrt(j))`. On `[0,1/j]`, the inequality
`|L_j'|<=j(j+1)/2` bounds the variation by a constant. This inequality
follows by summing `L'_(j+1)-L'_(j-1)=(2j+1)L_j` and using `|L_j|<=1`;
the latter follows from the generating-function integral
`L_j(cos(theta))=pi^-1 integral_0^pi
(cos(theta)+i sin(theta)cos(alpha))^j d alpha`.
Parity handles the remaining half interval and `j=0` is immediate.
This proves the last bound in (22) without a regularity assumption on `b`.

We will also use

\[
 \|(I-\Pi_P)\mathbf1_{[1,\tau]}\|_{L^2(0,\tau)}
                   \le C\sqrt{\tau/P}.
 \tag{24}
\]

For `P>=2`, replace the step by a ramp of width `tau/P` on a side of the
jump with that much room. At least one side has room. The direct `L^2`
error is at most `sqrt(tau/P)`; the derivative norm of the ramp is
`sqrt(P/tau)`, so (21) proves (24) by contraction and the triangle
inequality. For `P=1` contraction suffices. At `tau=1` the step is zero
almost everywhere.

## 5. Forward energy bounds the relative defect without curvature

Suppress hats in calculations about the closure and put

\[
 Z_\ell(t)=\frac1{mn}\sum_a\int_0^{\tau(t)}
                          \|\partial_\xi h_{\ell,a}\|_2^2d\xi.
\]

All histories on a compact stopped subinterval have the regularity used
here, since `rho>0`; estimates will not depend on its minimum.
First-layer differentiation gives
`Z_1<=Z_1^*:=4Sv_1^2X^4 beta_1^2`.
The degree-below-`P` endpoint evaluation norm is `P/sqrt(tau)`.
The backward history has sample/neuron RMS at most `beta_l`, so its
endpoint error has RMS at most `(P+1)beta_l`. Equations (18)--(21) imply

\[
 \int_0^t\rho\|E_\ell/\rho\|_F^2ds
 \le 2A_c^2\beta_\ell^2 Z_{\ell-1}(t).
 \tag{25}
\]

Specifically the left side is at most
`4(P+1)^2 beta_l^2` times the normalized forward squared tail, which is
at most `A_c^2 Z_(l-1)/(4P(P+1))`.

Differentiate `h_l=phi_l(W_l h_(l-1))` in clock time and insert
`W_l'=F_l/rho+E_l/rho`. The three contributions are the canonical weight
velocity, its defect, and the preceding feature velocity. Their squared
norm is at most three times the sum of their squares. Since
`||F_l/rho||_F<=2beta_l M_(l-1)`, induction gives

\[
 Z_\ell\le Z_\ell^*,\qquad
 Z_\ell^*=3v_\ell^2\left[
 4S\beta_\ell^2M_{\ell-1}^4+
 (D^2+2A_c^2\beta_\ell^2M_{\ell-1}^2)Z_{\ell-1}^*
 \right].
 \tag{26}
\]

These are width- and order-independent bounds, with the factors for
unbounded feature values retained explicitly.

Apply (22) to the sample/neuron arrays: the forward endpoint error is
at most `C_T/sqrt(P)` in RMS by (26); the backward endpoint error is
at most `C_T sqrt(P)` by (17). Their product in (19) proves

\[
 e_E(t)\le C_T\rho(t).
 \tag{27}
\]

Inserting this in (3) and propagating forward through the bounded
operators and slopes gives

\[
 |\dot{\widehat\theta}|_n\le C_T\rho,\qquad
 \max_{\ell,a}\frac{\|\dot z_{\ell,a}\|_2+
                            \|\dot h_{\ell,a}\|_2}{\sqrt n}
                            \le C_T\rho.
 \tag{28}
\]

The prediction differential from (5) to sample RMS is uniformly bounded
on (15). In detail, for a parameter increment `v`, forward differentiation
successively bounds `||Dz[v]||_2/sqrt(n)` and `||Dh[v]||_2/sqrt(n)` by
`C_T|v|_n`, and `Df[v]=v_w^T h_L/n+w^TDh_L[v]/n` has the same bound.
Consequently

\[
 \|\dot r\|_m\le C_T\rho,\qquad |\dot\rho|\le C_T\rho.
 \tag{29}
\]

Let `eta=rho(0)>0`. Integrating on the fixed physical interval gives

\[
 c_T\eta\le\rho(t)\le C_T\eta,\qquad
 \int_0^t\rho\,ds\le C_T\eta,\qquad
 \eta\le Q_0.
 \tag{30}
\]

The lower bound is proved, not an assumed residual floor. For
`c=r/rho`, direct differentiation gives `||dot c||_m<=C_T`.
Equation (28) and (30) sharpen the forward energy to

\[
 Z_\ell(t)\le C_T\eta.
 \tag{31}
\]

## 6. Backward tails and cancellation of the inverse residual

The readout equation and (30) imply

\[
 \|w(t)\|_2/\sqrt n\le B_0+C_T\eta,\qquad
 \max_a\|\delta_{\ell,a}(t)\|_2/\sqrt n
                       \le C_T(B_0+\eta).
 \tag{32}
\]

A locally Lipschitz function composed with an absolutely continuous
scalar curve is absolutely continuous on a compact range, with derivative
bounded almost everywhere by its Lipschitz constant times the curve speed.
Apply this directly to `phi_l'(z_(l,a,i))`. No classical second derivative
everywhere is required. The gate derivative is at most
`ell_(n,T)|dot z_(l,a,i)|`.

Every full backward carrier `W_(l+1)^T delta_(l+1,a)` has supremum norm
at most its Euclidean norm, bounded by `C_T sqrt(n)` on the stopped region;
the top carrier `w` has the same bound. Differentiate backpropagation:
the terms are gate variation times carrier, matrix variation times the
next backward response, and the next backward variation times the matrix.
Equations (17), (28) and downward induction therefore give

\[
 \max_{\ell,a}\|\dot\delta_{\ell,a}\|_2/\sqrt n
                           \le C_Ts_{n,T}\rho.
 \tag{33}
\]

This is the only spatial loss in the source estimate. It uses full
carriers and never assumes individual unbounded feature coordinates are
bounded uniformly in width. Since `b_a=c_a delta_a`, (30), (32), (33)
and the bound on `dot c` yield

\[
 \left[\frac1{mn}\sum_a\|\dot b_{\ell,a}\|_2^2\right]^{1/2}
                       \le C_T(B_0+s_{n,T}\rho).
 \tag{34}
\]

Subtract the prefix step `b_(ell,a)(1+) 1_[1,tau]` from the backward
history. Its jump amplitude has sample/neuron RMS at most `C_T B_0`.
The remainder is continuous at one and has derivative `dot b/rho` on
the physical interval. By `d xi=rho dt` and (30), its clock derivative
energy is bounded by

\[
 \frac1{mn}\sum_a\int_0^{\tau(t)}
          \|\partial_\xi\widetilde b_{\ell,a}\|_2^2d\xi
 \le C_T\left(\frac{B_0^2}{\eta}+s_{n,T}^2\eta\right).
 \tag{35}
\]

Denote normalized `L^2` projection-tail norms by `Q_h,Q_b`. Equations
(21), (24), (31) and (35) give, uniformly up to each stopped endpoint,

\[
 Q_{h,\ell}\le\frac{C_T\sqrt\eta}{P},\qquad
 Q_{b,\ell}\le C_T\left[
 \frac{B_0}{\sqrt P}
 +\frac{B_0/\sqrt\eta+s_{n,T}\sqrt\eta}{P}\right].
 \tag{36}
\]

Multiplying these bounds in (20), and summing the fixed number of links,
proves the crucial absolute accumulated velocity bound

\[
 \int_0^t e_E(s)ds
 \le C_T\left[
 \frac{B_0\sqrt\eta}{P^{3/2}}
 +\frac{B_0+s_{n,T}\eta}{P^2}\right]
 \le C_T\left[\frac{B_0}{P^{3/2}}+\frac{s_{n,T}}{P^2}\right].
 \tag{37}
\]

The inverse residual has canceled. Constants remain uniform as a positive
initial residual tends to zero. The exactly zero case was already handled
without dividing. At zero readout the prefix jump is absent, removing the
`P^-3/2` term.

## 7. Feedback comparison and the continuation bootstrap

On the convex region (15), the forward and prediction increment bounds
are independent of width. The gate difference satisfies

\[
 \|\phi_\ell'(z)-\phi_\ell'(\widetilde z)\|_2
                 \le\ell_{n,T}\|z-\widetilde z\|_2.
\]

Subtract backpropagation using the full carrier on one of the two paths.
Its supremum norm is at most `C_T sqrt(n)`. The matrix-difference term
uses the operator bound by its Frobenius norm, and the next backward
difference propagates through an operator of bounded norm. Induction
therefore gives

\[
 \max_{\ell,a}
 \frac{\|\delta_{\ell,a}(\theta)-\delta_{\ell,a}(\vartheta)\|_2}
      {\sqrt n}
                  \le C_Ts_{n,T}d_n(\theta,\vartheta).
 \tag{38}
\]

Subtract each product in (3), applying (38) and the uniform forward,
residual and backward bounds. The rank-one norm identity then proves

\[
 |F(\theta)-F(\vartheta)|_n
                 \le C_Ts_{n,T}d_n(\theta,\vartheta).
 \tag{39}
\]

This finite-difference argument is valid for `C^{1,1}_loc`; it does not
assume a classical derivative of `F` at every parameter.

Subtract the dense and closure equations (19), integrate, and apply
Gronwall and (37). There are constants `C_*,a_T>=1`, independent of
`n,P`, such that on the stopped interval

\[
 d_n(t)\le C_*e^{a_Ts_{n,T}}
          [B_0P^{-3/2}+s_{n,T}P^{-2}].
 \tag{40}
\]

This estimate holds for every order until stopping. Put `C_T=C_*`, and
choose `Lambda_T>=max{1,a_T,log(4C_*)}`. Then
`H_(n,T)>=4C_*` and `H_(n,T)>=s_(n,T)`.
Under (7), multiplication of (40) by `P` bounds its two terms by `C_*`
each. Moreover `P>=s_(n,T)H_(n,T)>=4C_*`. Hence

\[
 d_n(t)\le2C_*/P\le1/2.
 \tag{41}
\]

Continuity rules out first distance one. A finite maximal raw-ODE endpoint
before `T` is also impossible: physical parameters remain in the bounded
radius-one tube about the dense path, `tau<=A_c`, and each moment is an
integral of bounded finite-width histories against `|p_k|<=1`. For example,
forward moment norms are at most `A_c sqrt(n)M_l`, and backward norms at
most `A_c sqrt(mn) beta_l`. Thus the entire finite-dimensional raw state
remains bounded, with `tau>=1`, and its locally Lipschitz vector field
allows continuation. This proves (8) on the full interval and closes
the proof without an assumed closure boundedness or stability estimate.

## 8. Predictions, activation examples, and the scope of the extension

If in addition `||W_(1,0)||_F/sqrt(n)<=A_1`, then (14), (41) also bound
that norm along both paths. Linear growth and forward differentiation on
a parameter segment give, for every test input (with prediction constants
now also allowed to depend on `A_1`),

\[
 |\widehat f_{n,P}(t,x)-f_{n,D}(t,x)|
 \le C_T(1+\|x\|_2/\sqrt d)\,
             d_n(\widehat\theta_{n,P}(t),\theta_D(t)).
 \tag{42}
\]

Consequently (7) implies uniform `C_(T,R)/P` prediction discrepancy on
any fixed bounded test set, simultaneously over `[0,T]`. More generally,
for any probability test measure with finite second input moment,

\[
 \sup_{t\le T}\|\widehat f_{n,P}(t,\cdot)-f_{n,D}(t,\cdot)\|_{L^2(\mu)}
                    \le C_{T,\mu}/P.
 \tag{43}
\]

Here `C_(T,mu)` additionally depends on the second moment of the test
inputs, through the `L^2(mu)` norm of `1+||x||_2/sqrt(d)`.

By the reverse triangle inequality, the absolute difference of the two
RMSEs to any square-integrable target is bounded by (43). Training-input
preactivation control alone would not justify (42) outside the training
span; the additional initial bound is stated for that reason.

Common activations covered with globally Lipschitz derivative include
tanh, sigmoid, arctangent, sine/cosine, erf, softsign, softplus, exact GELU,
SiLU, and ELU with negative-branch coefficient one. For example:

- softplus has slope `sigma(x)` and second derivative
  `sigma(x)(1-sigma(x))<=1/4`;
- exact GELU `x Phi(x)` has slope `Phi(x)+x varphi(x)` and second derivative
  `(2-x^2)varphi(x)`, both bounded;
- SiLU `x sigma(x)` has slope `sigma+x sigma'` and second derivative
  `2 sigma'+x sigma''`, bounded by exponential tail decay;
- softsign has Lipschitz derivative `(1+|x|)^-2`; unit-coefficient ELU has
  Lipschitz derivative `exp(x)` for negative `x` and `1` for positive `x`.

Fixed gains, offsets, finite linear combinations, and layer-dependent
choices preserve the class. Affine or constant activations are allowed:
there is no feature-richness hypothesis because this theorem tracks
training whether or not it fits. With vanishing gate modulus, (6) has
`s_(n,T)=1`, without an artificial square-root width penalty.

For an example in the wider local class,
`phi(x)=integral_0^x sin(u^2)du` has bounded slope, and its derivative has
Lipschitz constant at most `2R_T sqrt(n)` on the interval in (6). The
sufficient logarithmic order then grows like `C_T n`.
Exact ReLU, leaky ReLU and standard SELU have a gate jump and are not
covered by this proof. Neither does the argument cover arbitrary locally
smooth activations with unbounded slope: their width-independent feature
bounds require a different moment argument.

The finite-time result needs no initial Gram gap or small labels; the
all-time small-label result in `ACTIVATION_EXTENSION.md` additionally
proves fitting and controls total activity. Those remain distinct claims.
The large sufficient orders here can exceed width, so they establish
joint approximation, not efficient asymptotic rank reduction. No uniform
all-time conclusion, infinite-width existence theorem, or width-sampling
rate is being inferred. If dense predictors independently converge to a
population predictor, their approximation error simply adds to (43).

For globally Lipschitz gates, a sequence with
`log(P(n))/sqrt(n) -> infinity` eventually satisfies (9) for each fixed
`T`. This is an eventual-in-width statement. One cannot infer existence
for every finite exceptional pair `(n,P)` just by enlarging an error
constant; the continuation threshold still applies.
