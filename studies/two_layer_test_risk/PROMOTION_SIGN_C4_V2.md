### C.4. Early test-risk improvement at equal training loss for a fixed tanh model

This subsection compares learned and frozen features for one fixed design.
It proves a strictly positive cubic test-risk difference, with a fourth-order
remainder on the actual population flow. The sign proof includes a finite
deterministic arithmetic certificate with all errors enclosed below.
The dependencies are C.1--C.3, including C.3's weighted-loss correction,
the Gaussian conditioning and source-response identities of Section 3,
and the bounded-action and strong-chain facts in Section 2 and A.1--A.4.
No population Taylor theorem is inferred from a finite-width jet.

#### Model, coefficient, and statement

There are exactly two hidden layers, both with activation `phi=tanh`, no
biases, and a scalar linear readout. At width `n` use the stored weights
and forward equations

\[
z^{(1)}_{n,x}=W_n^{(1)}x/\sqrt2,\quad
z^{(2)}_{n,x}=W_n^{(2)}\phi(z^{(1)}_{n,x}),\quad
f_n(x)=\frac{(W_n^{(3)})^\top\phi(z^{(2)}_{n,x})}{n}.
\tag{C4.1}
\]

All initial entries and blocks are independent Gaussian, with variances
`1`, `1/n`, and `1/n^2`, respectively. All three blocks train with raw
mobilities `(n,1,n)`. Fix

\[
x(\alpha)=\sqrt2(\cos\alpha,\sin\alpha),\qquad
(\alpha_1,\alpha_2,\alpha_3)=(0,\pi/5,-\pi/5),\qquad
y_a=\cos(3\alpha_a).
\]

Thus `y=(1,(1-sqrt(5))/4,(1-sqrt(5))/4)`. The training loss and test risk are

\[
\mathcal L(h)=\frac13\sum_{a=1}^3(h(x_a)-y_a)^2,\qquad
R(h)=\int_0^{2\pi}[h(x(\alpha))-\cos(3\alpha)]^2\frac{d\alpha}{2\pi}.
\tag{C4.2}
\]

Write `mu(d alpha)=d alpha/(2 pi)`, `p=y/3`, and `G_{xb}=x^T x_b/2`.
In particular the training input Gram is

\[
G=\begin{pmatrix}1&c_1&c_1\\c_1&1&c_2\\c_1&c_2&1\end{pmatrix},
\qquad c_1=(1+\sqrt5)/4,\quad c_2=(\sqrt5-1)/4.
\tag{C4.3}
\]

It has rank two and is retained without whitening or inversion. This is a
fixed-training-design risk question; no sample-size or input-dimension limit
is taken.

Let `f_t` be the strong population flow of C.1, with actual connector
`W^(2)(t)` and its adjoint. Let `g_s` freeze both initial hidden layers and
train only `W_g^(3)(s)` with the same mean loss. Both limiting readouts start
at zero. Write `L_f(t)=mathcal L(f_t)` and `L_g(s)=mathcal L(g_s)`.
Define the initialized fields

\[
Z_x=Z^{(1)}_{0,x},\quad Y_x=Z^{(2)}_{0,x},\quad
H_x^{(1)}=\phi(Z_x),\quad H_x^{(2)}=\phi(Y_x),
\]
\[
Q_{xb}=E_1[H_x^{(1)}H_b^{(1)}],\qquad
K_{xb}=E_2[H_x^{(2)}H_b^{(2)}].
\tag{C4.4}
\]

Throughout this subsection, hidden fields without a time argument are initialized
fields; `E_ell` always pairs fields of population `ell`. Training sums have
indices `a,b` from 1 to 3; `x` may be any passive circle input. Set

\[
\begin{aligned}
S&=\sum_bp_bH_b^{(2)},& U_x&=S\phi'(Y_x),\\
P_b&=(W_0^{(2)})^*U_b,& B_b&=\phi'(Z_b)P_b,\\
T_x&=\sum_bG_{xb}p_bB_b,& A_x&=\phi'(Z_x)T_x,\\
M_x&=\sum_bp_bQ_{xb}U_b,&
R_x^{\mathrm{hid}}&=M_x+W_0^{(2)}A_x,\\
E_x&=\phi'(Y_x)R_x^{\mathrm{hid}}.
\end{aligned}\tag{C4.5}
\]

`P,B,T,A` belong to population 1; `S,U,M,R^hid,E` belong to population 2.
The superscript on `R^hid` distinguishes this field from the risk functional.
Let `D_ab=E_1[B_aB_b]`, `V_ab=E_2[U_aU_b]`, and let `circ` denote entrywise
matrix multiplication. Define

\[
\begin{aligned}
B_0&=E_2[S^2]=p^\top Kp,&
\mathcal A&=p^\top(G\circ D+Q\circ V)p,\\
a(x)&=2E_2[S H_x^{(2)}],&
J(x)&=4E_2[S E_x]+\frac43\sum_bp_bE_2[H_x^{(2)}E_b],\\
\beta&=\frac{8\mathcal A}{3B_0},&
\chi&=2\int_0^{2\pi}\cos(3\alpha)
       [J(x(\alpha))-\beta a(x(\alpha))]\,d\mu(\alpha).
\end{aligned}\tag{C4.6}
\]

Here `B_0>0` and `mathcal A>0`, as checked below. All scalar quantities in
(C4.6) have an initialization-only Gaussian integral representation given
in (C4.27)--(C4.31); no future trajectory is needed to evaluate them.

**Theorem.** There exist `T>0` and a finite `M>=1`, depending only on this
fixed model and its C.1 bounds, such that the following statements hold.
Both clocks stay within the C.1 interval, and there is a unique
`tau(t)>=0` with `tau(0)=0` and `L_g(tau(t))=L_f(t)` for `0<=t<=T`. Uniformly
on that interval,

\[
\begin{aligned}
\sup_{\alpha}|f_t(x(\alpha))-g_t(x(\alpha))-J(x(\alpha))t^3|
 &\le Mt^4,\\
|\tau(t)-t-\beta t^3|&\le Mt^4,\qquad \beta>0,\\
|R(g_{\tau(t)})-R(f_t)-\chi t^3|&\le Mt^4.
\end{aligned}\tag{C4.7}
\]

The constants are independent of width and GD step; they are finite but
not numerically evaluated. The finite certificate below proves

\[
 \frac{27}{100000}<\chi<\frac{273}{1000000},\qquad
 \frac{35309}{1000000}<\beta<\frac{35311}{1000000}.
 \tag{C4.8a}
\]

Thus the cubic term is the first nonzero risk contribution. For
`t0=min(T,27/(200000M))`,

\[
 R(g_{\tau(t)})-R(f_t)\ge\frac{27}{200000}t^3>0
 \qquad(0<t\le t_0).
 \tag{C4.8}
\]

The initial risk is `1/2`; the leading benefit is about `0.000272 t^3`.
This establishes a small strict local improvement for this fixed design,
without a numerically evaluated time window or a practical magnitude claim.

The whole-circle predictions and risks have the finite-GF and raw-GD
capture stated below. Exact finite matching is asserted only on fixed
`[delta,T]`, `delta>0`, in probability in the width limit, with the actual
small random initial readout retained. No width rate, uniform finite-width
sign down to time zero, or arbitrary joint choice `delta_n -> 0` is claimed.

The proof first constructs passive predictions and unique matching. It
then bounds fourth moments of the fixed initialized directions, obtains
the remainder directly from the strong integral equations, and eliminates
the remaining operator actions from the scalar coefficient.

#### Passive circle inputs and unique matching

All C.1 hypotheses hold: tanh is bounded and `C^2`, with bounded first and
second derivatives; the data, depth and dimension are fixed; and the
Gaussian readout is an allowed vanishing initialization perturbation. Let
`T_*` be its interval and `B>=1` a common bound there for the connector
operator norm, readout `L2` norm and training first-layer `L2` norms.

The population state already determines every passive input. With
`theta=pi/5`, define

\[
u_1(\alpha)=\cos\alpha-\cot\theta\sin\alpha,\qquad
u_2(\alpha)=\sin\alpha/\sin\theta.
\]

At finite width, and also in the population,

\[
Z^{(1)}(t,\alpha)
=u_1(\alpha)Z^{(1)}(t,0)+u_2(\alpha)Z^{(1)}(t,\theta).
\tag{C4.9}
\]

For finite coordinates the same formula uses lowercase `z`. It is the
exact linear first-layer map, including at a raw-GD interpolation time.
Apply tanh, the current connector, tanh, and the current readout pairing
to (C4.9). For each fixed finite list of angles these are C.1's correctly
typed probes: linear combinations, Lipschitz coordinate maps, a forward
action, and a bounded factor multiplied by an `L2` field. The training
weights stay `1/3`; no zero-weight extension of C.1 is used.

The bounded derivatives of `u_1,u_2`, the norm ball and Lipschitz tanh give
a constant `C` such that

\[
\|Z^{(1)}(t,\alpha)-Z^{(1)}(t,\alpha')\|_2
 +|f_t(x(\alpha))-f_t(x(\alpha'))|
\le C|\alpha-\alpha'|.
\tag{C4.10}
\]

At finite width the same proof uses vector norm divided by `sqrt(n)` and
holds on C.1's high-probability norm event. A finite angular epsilon-net
therefore bounds the uniform prediction error by its maximum at the net
points plus `2C epsilon`. C.1 supplies convergence uniformly in time at
those finitely many points. First let width tend to infinity, then epsilon
to zero. This proves whole-circle, uniform-in-time prediction convergence
in probability on `[0,T_*]`, both for finite GF and for every deterministic
raw-GD step sequence `eta_n>0` with `eta_n -> 0`. The GF assertion uses
exactly C.1's stated GF corollary. Uniformly bounded predictions and
`|u^2-v^2|<=|u-v|(|u|+|v|)` transfer this convergence to (C4.2)'s risk.
The same argument applies to the frozen model using C.1 with its two
hidden mobilities set to zero. This is compact passive-input capture,
not an iid-sample assertion.

The three directions are pairwise nonparallel and all labels are nonzero.
C.3's ridge-function argument gives `Q>0`, despite rank deficiency of `G`.
The upper training tuple `Y` is thus Gaussian with full support. A putative
identity `sum_a c_a tanh(Y_a)=0` holds everywhere by continuity; varying
one coordinate makes its coefficient zero. Hence `K>0` and `B_0>0`.
The frozen residual, prediction and loss are exactly

\[
\begin{aligned}
r^g(s)&=-e^{-2Ks/3}y,\\
g_s(x)&=K_{x,\mathrm{train}}K^{-1}(I-e^{-2Ks/3})y,\\
L_g(s)&=\tfrac13|e^{-2Ks/3}y|^2,\qquad
L'_g(s)=-\tfrac49(r^g(s))^\top Kr^g(s)<0.
\end{aligned}\tag{C4.11}
\]

These follow by solving `dot r^g=-(2/3)Kr^g` and integrating the passive
output equation. The strict inequality holds for every finite `s`: the
matrix exponential is invertible and `y!=0`. With `lambda=lambda_min(K)>0`,
spectral decomposition gives `L_g(s)<=L_g(0)exp(-4 lambda s/3)` and limit
zero. Thus `L_g` bijects `[0,infinity)` continuously onto `(0,L_g(0)]`.

The full trained kernel has the C.1 blocks
`G_ab E_1[delta_a^(1)delta_b^(1)]`,
`E_1[H_a^(1)H_b^(1)] E_2[delta_a^(2)delta_b^(2)]`, and
`E_2[H_a^(2)H_b^(2)]`. Their entries have absolute values bounded by
`B^4`, `B^2`, and `1`, respectively. Consequently
`||K(t)||_op<=B_K:=3(B^4+B^2+1)`. The exact loss equation implies

\[
-\tfrac43 B_K L_f(t)\le L'_f(t)\le0,\qquad
L_f(t)\ge L_f(0)e^{-4B_Kt/3}>0.
\tag{C4.12}
\]

Multiply the differential inequality by `exp(4B_Kt/3)` to prove the last
bound. Equations (C4.11)--(C4.12) establish unique matching throughout
`[0,T_*]`, and comparison of the exponential bounds gives

\[
0\le\tau(t)\le (B_K/\lambda)t.
\tag{C4.13}
\]

Choose initially `T<=min(1,T_*,lambda T_*/(2B_K))`; then `tau(T)<=T_*/2`.
Further reductions of `T` below preserve this clock margin. At zero both
loss derivatives equal `-4B_0<0`. Continuity gives strict trained decrease
on a shorter interval, and the inverse of `L_g` is `C^1` there because
its derivative is nonzero.

#### Fixed-direction fourth moments and the integral remainder

The needed higher moments concern only initialized directions. They are
not assumptions about products along the trained path. The hypotheses of
C.3 and its weighted correction hold, so `V>0` and `D>0`. The conditional
law after the initial three forward calls is

\[
P_b=\sum_j H_j^{(1)}[Q^{-1}E_2[Y U_b]]_j+\Gamma_b,
\qquad \Gamma\sim N(0,V),
\tag{C4.14}
\]

with `Gamma` independent of the entire first-layer Gaussian root. This is
Section 3's actual reused-transpose law: its innovation covariance is the
full second moment `V`. The deterministic part is bounded, so `P_b` has
finite fourth moment. Since the gates, the training coefficients and
`G_xb` are bounded, `sup_x(||T_x||_4+||A_x||_4)<infinity`.

To control the next forward action, use the fixed training Grams and set

\[
q_x=Q^{-1}E_1[H^{(1)}A_x],\quad
A_x^\perp=A_x-\sum_jq_{x,j}H_j^{(1)},\quad
v_x=V^{-1}E_1[P A_x^\perp].
\]

Here `H^(1)`, `Y`, and `P` in vector expressions denote their three-entry
training tuples; `q_x,v_x` are deterministic coefficient vectors.

Conditioning the same matrix on its forward and reverse calls gives

\[
W_0^{(2)}A_x=\sum_jq_{x,j}Y_j+\sum_jv_{x,j}U_j
                     +\|A_x^\perp\|_2\xi_x,
\tag{C4.15}
\]

where `xi_x` is standard Gaussian independent of the previously revealed
upper training coordinates. This is Section 3.2's conditional mean and
unused Gaussian term. Its finite output projection removes only a fixed
rank, whose normalized squared size tends to zero. The input `A_x` is
measurable after the lower root, the three forward calls and their reverse
calls have been revealed, as required for that conditioning. It does not
use its own future answer. No independence from the passive coordinate
`Y_x`, and no mutual independence of different `xi_x`, is asserted.
Cauchy--Schwarz and the fixed finite norms of `Q^-1,V^-1` bound `q_x,v_x`
uniformly. The `Y_j` are Gaussian and the `U_j` bounded. Thus

\[
\sup_x\bigl(\|T_x\|_4+\|A_x\|_4+\|R_x^{\mathrm{hid}}\|_4\bigr)<\infty.
\tag{C4.16}
\]

Only the fixed, positive training activation/response Grams were inverted.
Neither `G` nor an augmented passive covariance was inverted.

Hereafter `C` denotes a finite constant, enlarged finitely often, depending
only on the fixed data, tanh derivative bounds, the C.1 norm ball and the
fixed moments just proved. All following bounds are uniform over circle
inputs for `0<=t<=T`. The exact strong equations, with `r_b=f_b-y_b`, are

\[
\begin{aligned}
\dot Z_x^{(1)}(t)&=-\tfrac23\sum_bG_{xb}r_b(t)\delta_b^{(1)}(t),\\
\dot W^{(2)}(t)&=-\tfrac23\sum_br_b(t)
                    \delta_b^{(2)}(t)\otimes H_b^{(1)}(t),\\
\dot W^{(3)}(t)&=-\tfrac23\sum_br_b(t)H_b^{(2)}(t),\\
\delta_b^{(2)}(t)&=W^{(3)}(t)\phi'(Z_b^{(2)}(t)),\\
\delta_b^{(1)}(t)&=\phi'(Z_b^{(1)}(t))(W^{(2)}(t))^*\delta_b^{(2)}(t).
\end{aligned}\tag{C4.17}
\]

The last integral, with zero initial readout and `|H_b^(2)|<=1`, has an
`L-infinity` representative with `||W^(3)(t)||_infinity<=2rho t`, where
`rho` bounds the residual magnitudes. Hence `||delta^(2)||_2=O(t)` and
`||delta^(1)||_2=O(t)`. Integrating the first two equations gives

\[
\sup_x\|Z_x^{(1)}(t)-Z_x\|_2
 +\|W^{(2)}(t)-W_0^{(2)}\|_{\rm op}\le Ct^2.
\]

Lipschitz tanh and expansion of the upper forward product then give
`sup_x(||Z_x^(2)(t)-Y_x||_2+||H_x^(2)(t)-H_x^(2)||_2)<=Ct^2`.
Also `|r_b(t)+y_b|=|f_b(t)|<=Ct`. Comparing the readout integral to `2tS`
and using these estimates yields

\[
\|W^{(3)}(t)/t-2S\|_2\le Ct,\quad
\|\delta_b^{(2)}(t)/t-2U_b\|_2\le Ct,\quad
\|(W^{(2)}(t))^*\delta_b^{(2)}(t)/t-2P_b\|_2\le Ct.
\tag{C4.18}
\]

The first bound follows because the integrand error from the residual is
`O(t)` and that from the hidden activation is `O(t^2)`. For the second,
subtract the varying readout first and multiply the remaining gate error
by bounded `S`. The third uses the operator norm difference and bounded
initial adjoint.

For a bounded Lipschitz scalar function `b`,

\[
\|b(X)-b(Y)\|_4
\le (2\|b\|_\infty\operatorname{Lip}(b))^{1/2}\|X-Y\|_2^{1/2}.
\]

Indeed bound two factors of `|b(X)-b(Y)|^4` by `(2||b||_infinity)^2`
and the other two by `Lip(b)^2|X-Y|^2`, then integrate. With `b=phi'`,
the lower gate difference is therefore `O_L4(t)`. Hölder against the
fixed `P_b` in (C4.14), followed by (C4.18), proves
`||delta_b^(1)(t)/t-2B_b||_2<=Ct`. Substitute this and (C4.18) into
(C4.17), retaining `r_b(t)=-y_b+O(t)`, and integrate. The velocity errors
are `O(t^2)`, so

\[
\begin{aligned}
Z_x^{(1)}(t)-Z_x&=2t^2T_x+O_{L^2}(t^3),\\
W^{(2)}(t)-W_0^{(2)}
 &=2t^2\sum_bp_bU_b\otimes H_b^{(1)}+O_{\rm op}(t^3).
\end{aligned}\tag{C4.19}
\]

The activation Taylor estimate needed here is only along a fixed direction.
If `X_t=X_0+t^2 F+e_t`, `||e_t||_2<=Ct^3`, and `F` has finite fourth
moment, the bounded first and second derivatives give

\[
\|\phi(X_t)-\phi(X_0)-t^2\phi'(X_0)F\|_2
\le\|\phi'\|_\infty Ct^3
  +\tfrac12\|\phi''\|_\infty t^4\|F\|_4^2.
\tag{C4.20}
\]

First remove `e_t` by Lipschitz continuity, then apply scalar Taylor to
`X_0+t^2F`; this proves the inequality without an ambient `L2` smoothness
assumption. Applying it to the first line of (C4.19), expanding the
connector product, and applying it again using (C4.16), gives

\[
\begin{aligned}
H_x^{(1)}(t)-H_x^{(1)}&=2t^2A_x+O_{L^2}(t^3),\\
Z_x^{(2)}(t)-Y_x&=2t^2R_x^{\mathrm{hid}}+O_{L^2}(t^3),\\
H_x^{(2)}(t)-H_x^{(2)}&=2t^2E_x+O_{L^2}(t^3).
\end{aligned}\tag{C4.21}
\]

The cross product of the two `O(t^2)` increments is `O(t^4)`. All constants
in these estimates are uniform in `x` by (C4.16) and `|G_xb|<=1`.

#### Moving residual, clock correction, and risk

On the common second-layer space set
`D^(3)(t)=W^(3)(t)-W_g^(3)(t)` and
`F_x(t)=H_x^(2)(t)-H_x^(2)`. Exact subtraction gives

\[
\begin{aligned}
\dot D^{(3)}(t)&=-\tfrac23\sum_b
 \{[f_t(x_b)-g_t(x_b)]H_b^{(2)}+r_b(t)F_b(t)\},\\
f_t(x)-g_t(x)&=E_2[D^{(3)}(t)H_x^{(2)}]
                          +E_2[W^{(3)}(t)F_x(t)].
\end{aligned}\tag{C4.22}
\]

In particular the moving residual has not been frozen. From (C4.18) and
(C4.21), the second equation is bounded in absolute value by
`||D^(3)(t)||_2+Ct^3`. The first then implies
`||D^(3)(t)||_2<=C integral_0^t||D^(3)(s)||_2 ds+Ct^3`.
The integral Gronwall estimate of Section 2 gives `||D^(3)(t)||_2<=Ct^3`.
Inserting this bound and (C4.21) in the first equation yields

\[
D^{(3)}(t)=\tfrac43t^3\sum_bp_bE_b+O_{L^2}(t^4).
\]

The residual-difference sum contributes `O(t^4)` after integration, while
the term with `r_b=-y_b+O(t)` supplies the displayed cubic coefficient.
Use `W^(3)(t)=2tS+O_L2(t^2)` in the second equation of (C4.22).
Cauchy--Schwarz bounds all error products and proves the first line of
(C4.7) with `J` from (C4.6). Both hidden blocks occur in `R_x^hid`, and
the first term in (C4.22)'s output pairing retains the readout correction.

Adjunction and (C4.5) give the exact training identity

\[
E_2[S E_a]
=\sum_bp_b\{G_{ab}D_{ab}+Q_{ab}V_{ab}\}.
\tag{C4.23}
\]

For its lower contribution use
`E_2[U_a W_0^(2) A_a]=E_1[P_a A_a]`; the connector contribution is
`sum_b p_b Q_ab E_2[U_aU_b]`. Summing (C4.23) against `p_a` and interchanging
the two finite sums in the other part of `J` gives

\[
p^\top J_{\rm train}=\tfrac{16}{3}\mathcal A,\qquad
p^\top a_{\rm train}=2B_0.
\tag{C4.24}
\]

Here `mathcal A>0`: C.3 supplies `V>0`; decomposing `Q` into rank-one
summands gives `Q circ V >= lambda_min(V) diag(Q_aa)>0`. The matrix
`G circ D` is positive semidefinite by the same rank-one decomposition
argument, and `p!=0`. This uses the fixed activation Gram, not a positive
eigenvalue of the singular input Gram.

The predictor expansion in the mean training loss gives

\[
L_f(t)-L_g(t)=-2p^\top J_{\rm train}\,t^3+O(t^4).
\tag{C4.25}
\]

The frozen formula (C4.11) has uniformly bounded derivatives on the compact
clock interval, uniformly over the circle since `|K_xb|<=1`. Its initial
loss derivative is `-4B_0`, and `g'_s(x)=a(x)+O(s)` uniformly. Shorten `T`
so `|L'_g(s)|>=2B_0` between `t` and `tau(t)`, possible by (C4.13).
The mean-value formula applied to
`L_g(tau(t))-L_g(t)=L_f(t)-L_g(t)` first gives `|tau-t|<=Ct^3`.
Using `L'_g(s)=-4B_0+O(s)` in it then gives
`tau=t+(p^T J_train/(2B_0))t^3+O(t^4)`, namely (C4.7)'s second line.
Equations (C4.24) also imply

\[
p^\top(J_{\rm train}-\beta a_{\rm train})=0.
\tag{C4.26}
\]

Thus matching removes the positive training-speed contribution; its
positivity alone cannot decide the teacher projection. Bounded frozen
derivatives give `f_t(x)-g_tau(t)(x)=t^3[J(x)-beta a(x)]+O(t^4)` uniformly.
Subtract the squared errors in (C4.2). Their sum factor is
`-2 cos(3 alpha)+O(t)` and their difference factor is the negative of
this predictor difference. Integration gives the last line of (C4.7).
Enlarge the finitely many constants to one `M>=1`. Once the strict bound
(C4.8a) is established below, `Mt<=27/200000` gives (C4.8).

#### Explicit Gaussian contraction, including singular passive slots

For one test angle use the four formal slots `I={x,1,2,3}`, and put `p_x=0`.
With independent standard normals `xi_1,xi_2`, the exact lower law is
`Z_i=xi_1 cos(alpha_i)+xi_2 sin(alpha_i)`. Compute
`Q_ij=E_1[phi(Z_i)phi(Z_j)]`, and take `Y~N(0,Q)` in at most four Gaussian
coordinates. Define the lower moments

\[
L_{ab}=E_1[\phi'(Z_a)\phi'(Z_b)],\qquad
\mathcal T_{abij}=E_1[\phi'(Z_a)\phi'(Z_b)\phi(Z_i)\phi(Z_j)].
\tag{C4.27}
\]

For the bounded smooth upper functions used below, set

\[
\begin{aligned}
\Lambda_{ab}(F_1,F_2)
 &=L_{ab}E_2[F_1F_2]
 +\sum_{i,j\in I}\mathcal T_{abij}E_2[\partial_i F_1]E_2[\partial_j F_2],\\
\mathcal C_a(F)
 &=\sum_{b=1}^3p_b\{Q_{ab}E_2[FU_b]
                          +G_{ab}\Lambda_{ab}(F,U_b)\}.
\end{aligned}\tag{C4.28}
\]

Then the coefficient in (C4.6) is explicitly

\[
J(x)=4\mathcal C_x(U_x)
 +\tfrac43\sum_{a=1}^3p_a\mathcal C_a(H_x^{(2)}\phi'(Y_a)).
\tag{C4.29}
\]

All derivatives are ordinary derivatives in the formally separate slots:

\[
\begin{aligned}
\partial_iU_a
 &=p_i\phi'(Y_i)\phi'(Y_a)+\mathbf1_{i=a}S\phi''(Y_a),\\
\partial_i[H_x^{(2)}\phi'(Y_a)]
 &=\mathbf1_{i=x}\phi'(Y_x)\phi'(Y_a)
                  +\mathbf1_{i=a}H_x^{(2)}\phi''(Y_a).
\end{aligned}\tag{C4.30}
\]

To prove these formulas, the simultaneous transpose law for such functions
is

\[
(W_0^{(2)})^*F=\mu_F(Z)+\Gamma_F,\qquad
\mu_F(Z)=\sum_{i\in I}\phi(Z_i)E_2[\partial_iF],\qquad
E_1[\Gamma_{F_1}\Gamma_{F_2}]=E_2[F_1F_2],
\tag{C4.31}
\]

where the centered jointly Gaussian innovation family is independent of
the lower roots. For nonsingular `Q`, conditional Gaussian projection
gives response `Q^-1 E_2[YF]`; Gaussian integration by parts gives
`E_2[YF]=Q E_2[nabla F]`, proving (C4.31). For singular `Q`, represent
`Y=A gamma` and perform scalar Gaussian integration by parts in `gamma`.
Section 3.4's finite regularization, bounded-action comparison and
continuous covariance-square-root construction identify this source rule
with the actual action at rank loss. Its hypotheses hold here: tanh,
its derivatives, `U_a`, and the functions in (C4.30) are bounded smooth
coordinate functions. Thus all differentiation and Gaussian integrations
are integrable and their boundary terms vanish. Coincident or antipodal
passive slots need no inverse and stay formally separate; any null
covariance combination is the same zero `L2` combination of the source
input fields, so the contracted answer is unambiguous.

Condition on the lower roots in the product of two equations (C4.31),
multiply by `phi'(Z_a)phi'(Z_b)`, and take expectation. This proves

\[
E_1[\phi'(Z_a)\phi'(Z_b)((W_0^{(2)})^*F_1)
                              ((W_0^{(2)})^*F_2)]
=\Lambda_{ab}(F_1,F_2).
\]

The innovation covariance is the full second moment in (C4.31), and its
mean-product term is the second summand of `Lambda`; neither may be
discarded. Finally, adjunction and (C4.5) give

\[
E_2[F R_a^{\rm hid}]
=\sum_bp_b\{Q_{ab}E_2[FU_b]+G_{ab}\Lambda_{ab}(F,U_b)\}
=\mathcal C_a(F).
\]

Taking `F=U_x` and `F=H_x^(2)phi'(Y_a)` proves (C4.29), including the
second use of the initial connector. Equations (C4.27)--(C4.30), `K`, and
(C4.6) specify `chi` by only Gaussian moments and one circle integral.
All these moments depend continuously on the passive angle: couple the
upper Gaussians by continuous positive-semidefinite covariance square roots
and use bounded convergence. Hence the circle integral is well defined.

#### Finite clocks and limitations

At finite width both comparisons start from the same actual Gaussian
stored readout of variance `1/n^2`. Its small random values are retained
throughout GF or raw GD. The finite hidden-parameter tangent blocks need
not vanish at initialization; only their population limits vanish. The
frozen population kernel `K` consequently equals the full initial
population tangent kernel, whereas the finite frozen kernel contains only
the readout block.

Let `K_n` be that empirical frozen kernel. It converges to positive-definite
`K`, and the common initial residual tends to `-y!=0`; with probability
tending to one `K_n>0` and that residual is nonzero. The frozen finite GF
loss is strictly decreasing to zero by the same diagonalization as
(C4.11). For raw GD, eventually
`(2/3)eta_n lambda_max(K_n)<1`. In each eigendirection its residual then
has a factor in `(0,1)` per step. Within a step, affine parameter
interpolation multiplies it by `1-(2/3)u lambda_i`, `0<=u<=eta_n`, also
positive and strictly decreasing in magnitude for each nonzero component.
Therefore the interpolated frozen loss is strictly decreasing to zero.

Fix `delta>0` with `delta<=T`. After the strict-decrease reduction used
above, `L_f(t)` for `delta<=t<=T` lies a positive distance below `L_f(0)`
and above zero. Uniform population capture places the corresponding actual
finite losses in the interior of the frozen finite loss range with
probability tending to one. This proves unique finite matching clocks
`tau_n(t)` on that interval, for GF and for the interpolated raw-GD paths.
The clock margin `tau(T)<=T_*/2` and uniform loss convergence keep these
finite clocks in a compact subinterval of `[0,T_*]` with probability
tending to one. On that compact interval the population frozen derivative
in (C4.11) is bounded away from zero. The mean-value inequality for this
population loss bounds `|tau_n(t)-tau(t)|` by the sum of the two uniform
finite loss errors divided by that derivative bound. Thus the clocks
converge uniformly in probability. The passive prediction and risk
convergence, together with continuity of the frozen population risk,
give convergence of the matched finite risk differences too.

The positive minimum in (C4.8) on every fixed `[delta,t0]` transfers
the positive sign with probability
tending to one. This uses only `n -> infinity` with any deterministic
`eta_n -> 0` for raw GD, or the C.1 finite-GF corollary, on the fixed local
horizon. The small finite readout can produce lower-order terms before the
width limit, so no statement uniform down to time zero at finite width
follows.

C.3 already proves nonzero order-`t^2` activation and preactivation
displacements, order-`t` speeds, and locally positive absolute nonaffinity
for each training hidden marginal under this model's verified hypotheses.
Equations (C4.19)--(C4.21) provide the corresponding controlled onset
directions. These activity facts alone do not determine `chi`; its signed
certificate below adds the test-risk conclusion for this fixed early-time
comparison. No general feature-learning benefit,
global continuation, growing-design limit, or sample-complexity conclusion
is established here.

#### C.4 certificate: Gaussian integration and covariance

All Gaussian expectations are normalized. The symbols `E_1` and `E_2`
retain their population meanings from (C4.4); generic Gaussian laws
are specified explicitly. The integer `q` in the cubature lemma counts
Gaussian root coordinates and is unrelated to the network input dimension.

##### 1. Analytic-strip tensor rule, with a finite tail

Write `gamma(x)=exp(-x^2/2)/sqrt(2 pi)`. Let `F:R^q -> C` have a holomorphic
extension when any one coordinate is moved into `|Im z_j|<=a_j`, all other
coordinates remaining real. Suppose on those separate strips
`|F|<=M_j`, and on the real domain `|F|<=M_0`. We do not require boundedness
when multiple coordinates move into their complex strips simultaneously.
Let `N_1,...,N_q` be independent standard normal variables.
For positive `h_j`, integers `m_j>=1`, and `r_j=m_j h_j`, define

\[
 Q_j v=h_j\sum_{k=-m_j}^{m_j}\gamma(kh_j)v(kh_j),\qquad
 \delta_j=\frac{2e^{-2\pi^2/h_j^2}}{1-e^{-2\pi^2/h_j^2}},
\]

\[
 e_j=\frac{2M_j e^{a_j^2/2}}{e^{2\pi a_j/h_j}-1}
       +\frac{2M_0\gamma(r_j)}{r_j}.
\tag{C4.E1}
\]

Then

\[
 \left|E_{N(0,I_q)} F(N_1,\ldots,N_q)-Q_1\cdots Q_qF\right|
 \le \sum_{j=1}^q e_j\prod_{i<j}(1+\delta_i).
\tag{C4.E2}
\]

The constants apply uniformly to any fixed real external parameters in `F`.
In particular, they are valid at a coincident or antipodal passive input.
The finite rule weights need not sum to one, and are not implicitly
renormalized. If a producer does normalize them, it must charge that change.

**Proof of the one-coordinate bound.** Fix the other real coordinates and
put `f(z)=gamma(z)F(z)`. For real frequency `w`, shifting the Fourier integral
to `Im z=-a sign(w)` gives

\[
 |\widehat f(w)|\le M_j e^{a_j^2/2}e^{-a_j|w|}.
\]

The contour shift is legitimate: `F` is holomorphic on the strip, bounded
there, and on the two vertical sides the Gaussian factor tends to zero
uniformly as the real endpoint tends to infinity. A shift at a boundary
may equivalently be obtained by first using a smaller strip and taking its
limit. The periodization `sum_k f(x+kh)` converges uniformly on `[0,h]`,
since `F` is bounded on the real line and the Gaussian tails are summable.
Its Fourier coefficients are `hat f(2 pi l/h)/h`; the displayed exponential
bound makes their series absolutely convergent. Evaluate the series at
zero and separate its zero coefficient. This proves directly

\[
 \left|\int f(x)\,dx-h\sum_{k\in\mathbb Z}f(kh)\right|
 \le\frac{2M_j e^{a_j^2/2}}{e^{2\pi a_j/h}-1}.
\]

For the deleted terms, monotonicity of `gamma` on `[0,infinity)` gives

\[
 h\sum_{|k|>m}\gamma(kh)
 \le 2\int_{mh}^\infty\gamma(u)\,du
 \le\frac{2\gamma(mh)}{mh}.
\]

The last inequality follows by replacing `1` by `u/(mh)` in the integral
and integrating `u gamma(u)=-gamma'(u)`. This proves (C4.E1).

For the Gaussian weight alone, the same Fourier computation uses
`hat gamma(w)=exp(-w^2/2)`. The infinite rule mass is
`1+2 sum_{l>=1}exp(-2 pi^2 l^2/h^2)`, at most `1+delta_j` because
`l^2>=l`. The finite positive rule has no greater mass. Finally telescope
`I_1...I_q-Q_1...Q_q` by replacing one coordinate at a time. Already
replaced coordinates contribute their positive rule masses and remaining
integral coordinates have mass one. This proves (C4.E2). In this proof every
contour shift has just one nonreal coordinate; a joint polydisc hypothesis
has not been silently introduced.

##### 2. Apply the bound to tanh moments and anisotropic Gaussian roots

For `phi(z)=tanh z` and `|Im z|<=pi/4`,

\[
 |\phi(z)|\le1,\qquad |\phi'(z)|\le2,\qquad |\phi''(z)|\le4.
\tag{C4.E3}
\]

Indeed, writing `z=x+iy`, the square of the first modulus is
`(sinh^2 x+sin^2 y)/(sinh^2 x+cos^2 y)<=1`. Also
`|phi'(z)|=1/(sinh^2 x+cos^2 y)<=2`, and `phi''=-2phi phi'` gives the last bound.
All three functions are holomorphic on the wider strip `|Im z|<pi/2`.

Let the root map used for quadrature be a **specified real matrix** `A`,
with `Y=A N`, and let `c_j>=max_i|A_ij|` be certified upper bounds.
The one-coordinate strips in (C4.E1) are admissible whenever

\[
 a_j c_j\le\pi/4.
\tag{C4.E4}
\]

Changing only the `j`th root coordinate moves every preactivation by at
most `c_j a_j` in imaginary part. Large shifts in a small root column are
therefore legitimate; they need not be restricted by larger columns.
If `c_j=0`, any finite `a_j` may be used, or that dimension may be omitted.

For a monomial containing `r` factors `phi'` and `s` factors `phi''`, with any
number of factors `phi`, (C4.E3) gives `M_j=2^r 4^s`. On the real domain all
three factors have absolute value at most one, so `M_0=1`. Repeated named
slots do not change the proof: count every multiplicative factor. Linear
combinations are bounded by the corresponding sum of absolute coefficients.
Throughout the certificate set `P=27/50`, so
`sum_a|p_a|=(1+sqrt(5))/6<P`. Then, for example,

| Moment integrand | Real bound `M_0` | One-root strip bound `M_j` |
|---|---:|---:|
| `S^2` | `P^2` | `P^2` |
| `S^2 phi'(Y_a) phi'(Y_b)` | `P^2` | `4P^2` |
| `H_x^(2) S phi'(Y_a) phi'(Y_b)` | `P` | `4P` |
| `phi'(Y_i) phi'(Y_a)` | `1` | `4` |
| `S phi''(Y_a)` | `P` | `4P` |
| `H_x^(2) phi''(Y_a)` | `1` | `4` |
| `S H_x^(2)` | `P` | `P` |

Here `S=sum_a p_a H_a^(2)` uses the actual signed training weights. These are
bounds for quadrature; no signed weight is replaced inside the coefficient.
Lower-population moments `Q`, `L`, and `mathcal T` from (C4.27) use the same rule with the
actual two-root map `(cos alpha_i,sin alpha_i)`. In particular their
rank-deficient covariance is neither inverted nor whitened.

For a concrete parameter choice, fix the root radius at eight and `B=26` (or the
more conservative `B=30` ), then set

\[
 a_j=\min\{\pi/(4c_j),\sqrt{2B}\},\qquad
 h_j^*=\frac{2\pi a_j}{B+a_j^2/2},\qquad
 m_j=\lceil8/h_j^*\rceil,\qquad h_j=8/m_j.
\tag{C4.E5}
\]

All decisions and inequalities in this prescription must themselves be
certified if floating-point arithmetic constructs the rule. It gives
`2 pi a_j/h_j>=B+a_j^2/2`, so the strip error per coordinate is at most

\[
 \frac{2M_j e^{-B}}{1-e^{-B-a_j^2/2}}.
\]

The tail error is `2M_0 exp(-32)/(8 sqrt(2 pi))`, less than
`1.27e-15 M_0`. The finite exact formulas, rather than rounded decimals,
are the certificate. For a simple rational envelope in root dimensions `q<=4`,
(C4.E5) with `B=26` gives total analytic cubature error at most
`5e-11 M_* + 6e-15 M_0`, where `M_*=max_j M_j`. With `B=30` it gives
at most `1e-12 M_*` whenever `M_0<=M_*`. To verify these without trusting
rounded exponential values, use
`exp(26)>195000000000`, `exp(30)>10000000000000`, and
`exp(32)>78900000000000`: each follows from the exact rational partial
sum `sum_{j=0}^{80} x^j/j!` at the indicated positive integer `x`.
Also `sqrt(2 pi)>5/2`. The grid satisfies
`h_j<=pi sqrt(2/B)`, by maximizing `2 pi a/(B+a^2/2)` in `a`, so
`delta_j<=2/(exp(B)-1)`. Substituting these inequalities into (C4.E1)--(C4.E2)
gives the stated rational envelopes. These finite-sum inequalities can be
checked by integer arithmetic.
The executing certificate uses the dyadic grid specified below, which
satisfies these same strip, mass and tail inequalities.

##### 3. Covariance error without a passive square-root derivative

Suppose `Q` and `Qbar` are positive semidefinite `q by q` matrices, including
singular ones. Let `F:R^q -> R` be bounded and twice continuously
differentiable with bounded first and second derivatives. If
`epsilon_Q=max_ij|Q_ij-Qbar_ij|`, then

\[
 |E_{N(0,Q)}F-E_{N(0,\overline Q)}F|
 \le\frac{\epsilon_Q}{2}\sum_{i,j}
                   \|\partial_i\partial_jF\|_\infty.
\tag{C4.E6}
\]

**Proof.** For `delta>0` interpolate the positive definite matrices
`Q_s=(1-s)Q+s Qbar+delta I`. Differentiating their Gaussian densities gives
`partial_s rho_s=(1/2)sum_ij(Qbar-Q)_ij partial_i partial_j rho_s`.
This identity can also be checked by differentiating their characteristic
functions `exp(-xi^T Q_s xi/2)`. Integrating twice by parts is valid for
bounded `F` and its derivatives, because every density derivative is a
polynomial times a decaying Gaussian. Thus

\[
 \frac{d}{ds}E_{N(0,Q_s)}F
 =\frac12\sum_{i,j}(\overline Q-Q)_{ij}
                       E_{N(0,Q_s)}\partial_i\partial_jF.
\]

Integrating `s` from zero to one gives (C4.E6), uniformly in `delta`.
At each endpoint realize the regularized vector as its original Gaussian
vector plus an independent `sqrt(delta)` standard Gaussian. Boundedness,
continuity and dominated convergence then pass to `delta=0`.
This supplies the formula at singular passive covariances without any
inverse or derivative of a selected covariance square root.

For execution, treat each stored root entry of `A` as an exact rational
floating-point number and set `Qbar=A A^T` **in exact arithmetic**. It is
then automatically positive semidefinite. Compute a rigorous interval for
`Q-Qbar` from the certified lower moments and exact matrix products. No
claim that the numerical root is an exact root of `Q` is needed. A small
negative residual from a floating conditional-variance computation must
not be silently clipped and called exact; its resulting root is instead
handled by this explicit covariance perturbation certificate.

##### 4. Explicit Hessian constants for all upper primitive moments

On the real line,

\[
 |\phi|,|\phi'|,|\phi''|\le1,\qquad |\phi'''|\le2,\qquad |\phi''''|\le5.
\tag{C4.E7}
\]

For the first three assertions use `u=tanh x in[-1,1]`,
`phi'=1-u^2` and `phi''=-2u(1-u^2)`, whose maximum absolute value is
`4/(3 sqrt(3))<1`. Also `phi'''=(1-u^2)(-2+6u^2)` has absolute value
at most two. Finally `phi''''=16u-40u^3+24u^5` vanishes at the endpoints;
its interior extrema have `u^2=(15+-sqrt(105))/30`. Substitution gives
absolute values less than five (the two squared roots lie in
`[.15,.16]` and `[.84,.85]`, which already give this strict bound).

For a product `F=prod_{l=1}^r f_l(Y_{i_l})`, where each `|f_l|<=1`,
`|f_l'|<=b_l`, `|f_l''|<=c_l`, the product rule gives

\[
 \sum_{i,j}\|\partial_i\partial_jF\|_\infty
 \le\sum_l c_l+\sum_{l\ne k}b_l b_k.
\tag{C4.E8}
\]

This remains true for repeated slots: summing derivative terms before
bounding them can only create cancellations omitted by the right side.
Apply (C4.E8) with `(b,c)=(1,1)` for `phi`, `(1,2)` for `phi'`, and `(2,5)`
for `phi''`. The exact constants needed in (C4.E6) are consequently

| Monomial `F` | Hessian sum bound | Covariance error bound |
|---|---:|---:|
| `H_i^(2) H_j^(2)` | `4` | `2 epsilon_Q` |
| `phi'(Y_i) phi'(Y_j)` | `6` | `3 epsilon_Q` |
| `H_i^(2) phi''(Y_j)` | `10` | `5 epsilon_Q` |
| `H_i^(2) H_j^(2) phi'(Y_a) phi'(Y_b)` | `18` | `9 epsilon_Q` |

After expanding only the finite `S` sums this yields, with all indices
and repetitions allowed,

\[
\begin{aligned}
 |\delta E_2 S^2|&\le2P^2\epsilon_Q,\\
 |\delta E_2[S^2\phi'(Y_a)\phi'(Y_b)]|&\le9P^2\epsilon_Q,\\
 |\delta E_2[H_x^{(2)}S\phi'(Y_a)\phi'(Y_b)]|&\le9P\epsilon_Q,\\
 |\delta E_2[\partial_i U_a]|&\le
   (3|p_i|+5P\mathbf1_{i=a})\epsilon_Q,\\
 |\delta E_2[\partial_i(H_x^{(2)}\phi'(Y_a))]|&\le
   (3\mathbf1_{i=x}+5\mathbf1_{i=a})\epsilon_Q,\\
 |\delta\{2E_2[SH_x^{(2)}]\}|&\le4P\epsilon_Q.
\end{aligned}\tag{C4.E9}
\]

Here `delta E_2[F]=E_{N(0,Q)}[F]-E_{N(0,Qbar)}[F]` denotes
the difference of the upper-coordinate integrals under the two specified
covariance laws; it is not a derivative in time. In the formal passive slot `p_x=0`, exactly as
in (C4.27)--(C4.30). (C4.E9) certifies the full response means; it
does not remove the response mean-product term in `Lambda`.

##### 5. Arithmetic and final assembly obligations

The analytic inequalities enclose exact Gaussian integrals. A floating
sum becomes a certificate only after its arithmetic is also enclosed.
An acceptable implementation combines:

1. Certified input constants and stored root entries, with (C4.E6) charging
   the difference between the exact Gaussian covariance and `A A^T`.
2. Explicit error bounds for each elementary function and all arithmetic
   used to evaluate the tensor sum. Ordinary library `tanh` or `exp`
   accuracy is not an implicit theorem.
3. Positive Gaussian weights and a proved summation error bound. If
   `k` consecutive binary operations have unit roundoff `u` and `ku<1`,
   the usual product expansion bounds their accumulated relative factors
   by `gamma_k=ku/(1-ku)`. An actual producer must state its order/count,
   precision and absence of overflow/underflow; it cannot charge only
   the final scalar rounding.
4. Exact rational interval evaluation of the finite coefficient formulas,
   including the division by a strictly positive enclosed `B_0=E_2 S^2`.
   Separately enclose the clock subtraction: a positive unadjusted
   teacher projection does not establish a matched-loss sign.
5. The whole-circle integration bound below, which
   avoids differentiating a passive Cholesky factor. Every discrete
   angular value is enclosed using (C4.E1)--(C4.E9), whether its root choice
   changes smoothly with angle or not.

A practical elementary-function construction is available without calling
an assumed correctly-rounded `tanh`: for a real argument `|x|<=16`,
approximate `exp(-|x|/128)` by its degree-12 Taylor polynomial, square eight
times to obtain `exp(-2|x|)`, and form
`sign(x)(1-v)/(1+v)`. The alternating-series truncation is bounded by
`(|x|/128)^13/13!`. Rounding must be added at every Horner/squaring/ratio
step and the previously rounded argument must also be charged. The
implementation and its operation-by-operation error constants
are given below. The same construction handles Gaussian weights after
suitable range reduction.

A final interval `[chi_minus,chi_plus]` with `chi_minus>0` proves the
positive coefficient. An interval strictly below zero proves the opposite
sign. An interval containing zero remains inconclusive. Refinement trends,
parity residuals or a floating sign never replace this decision rule.
The already proved time remainder then supplies the corresponding finite
positive-time statement; it does not improve the numerical enclosure.

#### C.4 certificate: the executing arithmetic

##### Exact reduction of the costly integral

The mathematical slots remain `I={x,1,2,3}`, with training indices
`1,2,3` and `p_x=0`. The C++ array index bijection is
`iota(1)=0`, `iota(2)=1`, `iota(3)=2`, and `iota(x)=3`.
Thus the mathematical label `p_a` is the token `p0`, `p1`, or `p2`
when `a=1`, `2`, or `3`, respectively. Every slot of each code array
uses this bijection, including all four slots of `T_bits`.

Use `H_i^(2)=phi(Y_i)` and `S=sum_(a=1)^3 p_a H_a^(2)`. Take a
specified real factor `Lhat` whose training rows have zero fourth column,
and set `Y_i=sum_(j=1)^4 Lhat_(iota(i),j-1) gamma_j`, with independent
standard normal roots `gamma_1,...,gamma_4`. Here `E_gamma` means their
joint expectation. For covariance Q these coordinate integrals equal
the population expectations `E_2`. The executing rule uses an exact
dyadic factor and charges its covariance discrepancy by (C4.E6);
the following conditioning identities hold for either specified factor.

Conditional on `gamma_1,gamma_2,gamma_3`, all training quantities are
fixed and `Y_x=m_x+sigma_x gamma_4`, where
`m_x=sum_(j=1)^3 Lhat_(3,j-1) gamma_j` and `sigma_x=Lhat_(3,3)`.
For a scalar function v, define the conditional root integral
`E_{gamma_4}[v(Y_x)]=integral_R v(m_x+sigma_x z) exp(-z^2/2) dz/sqrt(2pi)`.
This integrates the fourth independent root, not a hidden population.
The three scalar functions of the retained roots are

`A=E_{gamma_4}[phi(Y_x)]`, `B=E_{gamma_4}[phi'(Y_x)]`,
and `C=E_{gamma_4}[phi''(Y_x)]`.

Write `E_{gamma_1:3}` for expectation over the first three independent
standard normal roots. The seventeen distinct dynamic outer moments are

- `E_{gamma_1:3}[S^2 B phi'(Y_b)]`, three values (`dynamic_V`);
- `E_{gamma_1:3}[S A phi'(Y_a)phi'(Y_b)]`, six symmetric values (`dynamic_C`);
- `E_{gamma_1:3}[B phi'(Y_a)]`, three values (`dynamic_dd`);
- `E_{gamma_1:3}[S C]`, one value (`dynamic_ESdd`);
- `E_{gamma_1:3}[A phi''(Y_a)]`, three values (`dynamic_Hdd`);
- `E_{gamma_1:3}[S A]`, one value (`dynamic_SH`).

These are conditional forms of the full root integrals. At covariance Q,
for example, `V_xb=E_2[S^2 phi'(Y_x)phi'(Y_b)]`, and `dynamic_C`
represents `E_2[H_x^(2) S phi'(Y_a)phi'(Y_b)]`. The two
reverse-response derivatives in (C4.30) are

`E_2[partial_i U_x]=p_i E_2[phi'(Y_i)phi'(Y_x)]+1_(i=x) E_2[S phi''(Y_x)]`,

`E_2[partial_i(H_x^(2)phi'(Y_a))]=1_(i=x) E_2[phi'(Y_x)phi'(Y_a)]+1_(i=a) E_2[H_x^(2)phi''(Y_a)]`.

For a dyadic factor the same identities use its specified `E_gamma` law.
Both matrix responses are retained. The training moments corresponding to
`E_2[S^2]`, `E_2[S^2 phi'(Y_a)phi'(Y_b)]`,
`E_2[phi'(Y_a)phi'(Y_b)]`, and `E_2[S phi''(Y_a)]` use only the
first three roots. Lower moments are the two-root tensors `Q_ij`,
`L_ab`, and `mathcal T_abij` of (C4.27), with their expectation `E_1`.
Expanding `S^2 phi'(Y_x)phi'(Y_b)` includes terms with four distinct
upper coordinates. Conditioning preserves that full law.

##### Finite-rule implementation and interface

The retained source is
[certificate_kernel.cpp](../code/tools/two_layer_risk/certificate_kernel.cpp).
It uses normalized Gaussian trapezoid weights without mass renormalization.
The certificate command chooses and certifies the spacings, truncations, covariance
perturbation and circle quadrature. This engine only evaluates the chosen
finite sum. Its compiler contract is

```
g++ -O3 -std=c++17 -fno-fast-math -ffp-contract=off certificate_kernel.cpp -o OUTPUT
```

The source requires binary64, round to nearest, and at least 64 significand
bits in `long double`. It invokes no library exponential or hyperbolic tangent.
Parsing is checked independently: all received real inputs are echoed as exact
IEEE binary64 bit patterns. Every reported scalar is cast once from its
long-double accumulator to binary64 and returned as a bit pattern too. The
driver must compare echoed inputs with the intended dyadic inputs; a mismatch
invalidates the run. Integer counts are parsed separately.

Input tokens for mode `lower` are, in this order:

```
lower
m0 m1
h0 h1 normal_density_constant
eight direction entries, row-major (four rows, two coordinates)
```

Output arrays `Q_bits`, `L_bits`, and `T_bits` are row-major with respectively
16,16,256 entries. They approximate the corresponding `Q`, `L`, and
`mathcal T` moments under the supplied dyadic lower law. The last tensor
is ordered `(iota(a),iota(b),iota(i),iota(j))`; its flat offset is
`64 iota(a)+16 iota(b)+4 iota(i)+iota(j)`. The name `T_bits` is a
code key for the tensor `mathcal T` in (C4.27), not the field `T_x`.

Input tokens for mode `upper` are

```
upper
m0 m1 m2 m3
h0 h1 h2 h3 normal_density_constant
sixteen factor entries, row-major
p0 p1 p2
```

Its training arrays are `ES2_bits`, `V_bits`, `ddgram_bits`, `ESdd_bits`.
Dynamic arrays have the names displayed above with suffix `_bits`; symmetric
three-by-three arrays are returned as all nine entries. Training rows must have
zero fourth column. A zero passive fourth column may use `m3=h3=0`, which
omits that independent Gaussian exactly; training axes cannot be omitted.
Metadata includes parsed input bits, actual outer/total node counts, long-double
mantissa size, and finite one-dimensional rule masses.

The primitive-only mode takes `primitives`, an integer count, and that many
real values; it returns tanh for each and exp(-x) where `0<=x<=64`. This is for
fixed deterministic arithmetic checks, not coefficient evaluation.

##### Elementary exponential and tanh enclosure

Write `u=2^-53`, the binary64 unit roundoff. For `0<=r<=64`, define
`s=r/256`, so `0<=s<=1/4`. The kernel evaluates the degree-twelve Taylor
polynomial of `exp(-s)` by Horner, then squares eight times. The coefficients
are reciprocals of exact integers `k!`, `0<=k<=12`; each computed coefficient
has relative error at most `u`. Multiplication by `1/256` is exact.

Here and below the elementary rounding model is used only for normal results;
the harmless tiny-input exception is covered explicitly below. If
`gamma_j=ju/(1-ju)`, induction on Horner's recurrence, expanding each operation's
factor `1+delta`, gives absolute evaluation error at most

`gamma_25 sum_(k=0)^12 s^k/k! <= (4/3) gamma_25`.

The last inequality follows from `sum s^k/k! <= sum s^k <=4/3`.
The alternating-series bound gives

`0 <= P_12(-s)-exp(-s) <= (1/4)^13/13!`.

Also `exp(-s)>=1-s>=3/4`. Consequently the initial relative error is at most

`delta_0 = (16/9) gamma_25 + (4/3)(1/4)^13/13! < 46u`.

Eight rounded squarings produce relative error bounded by

`(1+46u)^256 (1+u)^255 - 1 < 2e-12`.

The number 255 is the sum of the rounding-error multiplicities
`1+2+4+...+128`; the initial error has multiplicity 256. This proves the
kernel's relative bound `2e-12` for `exp_negative(r)`. The smallest final
exponential on this range is `exp(-64)>2^-93`, so squaring never approaches
underflow. Extremely tiny input `r` can make its division by 256 or a
multiplication inside Horner subnormal; each such absolute error is at most
`2^-1075`. Even pessimistically adding this at all 26 operations and
multiplying by 256 is smaller than
`2^-1060`, which is absorbed by the strict slack in `2e-12`.

For `|z|<=16`, the kernel substitutes `q=exp_negative(2|z|)` into

`tanh(z)=sign(z)(1-q)/(1+q)`.

The exact map in `q` has derivative of magnitude `2/(1+q)^2<=2` for `q>=0`.
Thus exponential error contributes at most `4e-12`. Rounding in the numerator,
denominator and division contributes less than `6u`; subtraction near zero
does not invalidate this absolute bound. Projection onto the correct interval
`[0,1]` cannot increase the error. For `|z|>16`, returning its sign has error
`2/(exp(2|z|)+1) < 2 exp(-32) < 3e-14`. Therefore the global absolute bound is

`|bounded_tanh(z)-tanh(z)| <= 5e-12`.

This proof depends on elementary rational inequalities and IEEE arithmetic,
not the accuracy of a platform `tanh` or `exp` implementation. Compiler fast-math
and fused contraction are excluded so that the stated operation counts apply.

##### Uniform arithmetic enclosure for every reported moment

The following intentionally loose envelope is used by the driver:

> Every returned moment differs by at most `1e-9` from the exact finite
> tensor sum at the supplied exact dyadic root factors, spacings, directions
> and label coefficients, using exact tanh and the true normal density.

The envelope requires all of the following, checked by source or driver:

1. `0<h_j<=1`, `m_j<=200`, `m_j h_j<=9` for present axes;
2. factor and direction entries have magnitude at most two;
3. `sum |p_a|<=1`;
4. the supplied density constant differs from `1/sqrt(2pi)` by at most `1e-15`;
5. exact finite one-dimensional Gaussian masses are at most `1.000001`;
6. binary64 and long-double contracts above and finite intermediate/output values.

Condition 5 follows, for example, from the Gaussian infinite-trapezoid identity
in the accompanying error proof and `h<=1`; truncation only decreases mass.
The source reports its masses as an additional diagnostic, not as a replacement
for that bound. The radius and coefficient bounds give Gaussian node magnitudes
at most nine and exact dot-product absolute sums at most 72. Node multiplication
and at most seven dot-product operations change each preactivation by less than
`1e-13`. The derivative bound `|tanh'|<=1` therefore enlarges the primitive
activation bound to at most `6e-12` at an exact quadrature node. Direct expansion
of `phi'(z)=1-phi(z)^2`, `phi''(z)=-2phi(z)+2phi(z)^3` for
`phi(z) in[-1,1]` gives errors at most `1.3e-11` and
`2.6e-11`, including their displayed arithmetic operations.

Each Gaussian exponent differs from its exact node exponent by at most
`1.5e-14`: forming a node, squaring it and dividing by two uses the bound
`3u * 81/2` with slack. Since `exp(-x)` has relative sensitivity one, the
primitive exponential, two weight multiplications, and the density-constant
error give a relative weight error below `3e-12`. A product of four weights
has relative error below `1.3e-11`, including the actual product operations.

For completeness, the real integrands contain only activation values,
their first two derivatives, and S. On real arguments,
`|phi|,|phi'|,|phi''|<=1` by (C4.E7), and `|S|<=1`; S is a
three-term weighted sum.
The code-local arrays `H`, `d`, `dd` evaluate `H_i^(2)`, `phi'(Y_i)`,
`phi''(Y_i)`; the lower arrays `h`, `e` evaluate `H_i^(1)`, `phi'(Z_i)`.
Every listed moment contains at most six such elementary activation/gate
factors after expanding `S` or `S^2`. The sum of absolute label coefficients
in these expansions is at most one. Multiplying telescopically, each product's
activation and gate error is less than `6*2.6e-11`, and arithmetic plus weight
error is less than `4e-11`. Hence `2e-10` bounds the pointwise-and-weight
contribution for every moment. The exact product rule mass is at most
`1.000001^4<1.000005`, so this contributes less than `2.00001e-10` in total.

The passive inner sums contain at most 401 terms and are accumulated in
long double. Outer sums contain at most `401^3=64,481,201` terms. With
long-double unit roundoff at most `2^-64`, the same elementary product-of-rounding
factors argument bounds total summation error by

`4 gamma_(64,481,201)(2^-64) < 1.5e-11`.

The factor four covers a bounded inner sum and its subsequent outer sum.
All remaining long-double products and the final binary64 cast contribute
less than `1e-13`; their multiplicands have the bounded magnitudes just stated.
This total is below `2.2e-10`, strictly below the declared `1e-9` enclosure.
Tiny underflowed summands are bounded in absolute value by `2^-1075` per
binary64 operation, or its still smaller long-double counterpart; even using
the maximal node count and 100 operations per node, their sum is far below
the `1e-13` slack. Overflow is excluded by the displayed finite ranges.

This arithmetic envelope is separate from Gaussian discretization/tails,
lower-law direction errors, upper covariance errors, algebraic propagation,
and the circle quadrature error. The final certificate must include all of them.

#### C.4 certificate: the circle rule

##### Statement

Assume the separately computed training clock coefficient satisfies
`|beta|<=1/10`. Use `P=27/50` and `sum_a|p_a|<P` as above.
Write `J(alpha)=J(x(alpha))`, `a(alpha)=a(x(alpha))`, and

`F(alpha)=2 cos(3 alpha) [J(alpha)-beta a(alpha)]`.

For `N=256`, the full periodic equally spaced rule satisfies

\[
 \left|\chi-\frac1N\sum_{j=0}^{N-1}F(2\pi j/N)\right|<10^{-6}.
 \tag{C4.A1}
\]

The rational calculation in
[angle_error_bound.py](../code/tools/two_layer_risk/angle_error_bound.py) gives
a sharper bound;
the looser displayed rational value is used by the certificate driver.
The hypothesis on beta must be checked by its independent rigorous interval,
not assumed from a floating estimate. The proof does not differentiate
any Cholesky factor, square root of a passive conditional variance, or
inverse of a singular augmented Gram.

##### Smooth Gaussian angular fields and derivative majorants

Write `phi=tanh`, `Z_alpha=N1 cos(alpha)+N2 sin(alpha)`, and
`H_alpha^(1)=phi(Z_alpha)`, where the two roots are independent standard normals.
The upper initialized Gaussian process `Y_alpha` has covariance
`E_1[H_alpha^(1) H_theta^(1)]`. It has derivatives in every fixed `L^p`: realize it
as an isonormal Gaussian map on the closed span of the lower `H_alpha^(1)`.
That map preserves L2 norms. The lower angular map is smooth in every
finite Lp by scalar differentiation, Gaussian moments and bounded
derivatives. Its image derivatives are centered Gaussian variables with
standard deviations `||partial_alpha^k H_alpha^(1)||_2`, uniformly in alpha. Gaussian
moments then give the claimed upper Lp differentiability by difference
quotients. This constructs the required derivative expectations without
requiring a sample-path analyticity assertion.

Let `m_r` bound `sup_real |phi^(r)|`. We use

\[
 m_0=m_1=m_2=1,\quad m_3=2,\qquad
 m_r=r!(4/3)^r\quad(r\ge4).
 \tag{C4.A2}
\]

The first four bounds follow from `phi'=1-phi^2`,
`phi''=-2phi(1-phi^2)` and `phi'''=-2+8phi^2-6phi^4` on `|phi|<=1`.
For the others, when `|Im z|<=3/4<pi/4`,

\[
 |\tanh(x+iy)|^2=
 \frac{\sinh^2x+\sin^2y}{\sinh^2x+\cos^2y}\le1.
\]

Cauchy's integral formula on a radius-3/4 circle centered at any real x
therefore gives `r!(4/3)^r`. No pole lies in that strip.

For a scalar `N~N(0,1)`, let `mu_j` be the following rational upper
bound for `E_{N(0,1)}|N|^j`:
`mu_(2s)=(2s-1)!!`, with `mu_0=1`, and
`mu_(2s+1)=(4/5)2^s s!`. Integration of the Gaussian density by parts gives
these moments with `sqrt(2/pi)` instead of `4/5` in the odd case, and
`sqrt(2/pi)<4/5`. Let `c_j` be the least integer whose square is at least
`(2j-1)!!`, so `sqrt(E_{N(0,1)}|N|^(2j))<=c_j`.

Use Stirling numbers `S(k,j)` and exponential partial Bell polynomials
`B_(k,j)` only as finite nonnegative combinatorial sums. They can be
defined, avoiding any theorem import, by

\[
 S(0,0)=1,\quad S(k,j)=S(k-1,j-1)+jS(k-1,j),
\]
\[
 B_{0,0}=1,\quad B_{k,j}(v)=
 \sum_{l=1}^{k-j+1}\binom{k-1}{l-1}v_l B_{k-l,j-1}(v),
 \tag{C4.A3}
\]

with other zero-boundary entries zero. Repeated product and chain rules
give the derivative expansion with `B_(k,j)`; this can also be proved
inductively from (C4.A3). Every derivative of `Z_alpha` is a signed rotated
standard Gaussian. Holder's inequality bounds the L1 norm of a product
of j such variables by `mu_j` and its L2 norm by `c_j`, regardless of
their dependence. Since `B_(k,j)(1,...,1)=S(k,j)`, define

\[
 s_k=\sum_{j=1}^k m_j S(k,j)c_j\quad(k\ge1),
\]
\[
 l_r(0)=u_r(0)=m_r,\quad
 l_r(k)=\sum_{j=1}^k m_{r+j}S(k,j)\mu_j,
 \quad
 u_r(k)=\sum_{j=1}^k m_{r+j}B_{k,j}(s)\mu_j.
 \tag{C4.A4}
\]

Then `s_k>=||partial_alpha^k H_alpha^(1)||_2`, `l_r(k)` bounds the L1 norm of the kth
angular derivative of `phi^(r)(Z_alpha)`, and `u_r(k)` bounds its upper
counterpart `phi^(r)(Y_alpha)`. For the last assertion apply Holder to
the jointly Gaussian upper derivatives with standard deviations at most
`s_k`, then apply the repeated chain rule. All orders used are at most
eight, with scalar tanh derivatives at most ten. The preceding finite
Gaussian moment bounds justify all derivative/expectation interchanges.

If two scalar functions have derivative bounds v,w, write
`(v*w)_k=sum_(j=0)^k binom(k,j) v_j w_(k-j)` for their product bound.
This notation denotes a finite convolution, not matrix multiplication.
Put `g_k=1` for a cosine of unit frequency and `t_k=3^k` for the teacher.

##### Bounding the exact coefficient without hiding a matrix response

Use the lower fields `H_i^(1)=phi(Z_i)` and upper fields
`H_i^(2)=phi(Y_i)` from (C4.4), with activation derivatives written
explicitly. Each `E_1` or `E_2` below contracts only its own population.
Here all named training fields are fixed as alpha varies. Set

\[
 S=\sum_a p_aH_a^{(2)},\qquad
 M_{bj}=p_j E_2[\phi'(Y_j)\phi'(Y_b)]+\mathbf1_{j=b}E_2[S\phi''(Y_b)],
 \qquad \mu_b=\sum_j H_j^{(1)}M_{bj}.
 \tag{C4.A5}
\]

Both sums over j here are training-only. The elementary bound
`sum_j |M_bj|<=2P` implies `|mu_b|<=2P` on the lower real probability
space. Expanding the exact inverse-free formula gives
`J(alpha)=4mathcal F(alpha)+(4/3)mathcal B(alpha)`,
where `x=x(alpha)` and

\[
\begin{aligned}
\mathcal F(\alpha)={}&\sum_b p_b\{Q_{xb}E_2[S^2\phi'(Y_x)\phi'(Y_b)]
 +G_{xb}E_1[\phi'(Z_x)\phi'(Z_b)]E_2[S^2\phi'(Y_x)\phi'(Y_b)]\\
&+G_{xb}\sum_{i,j}p_iM_{bj}E_1[\phi'(Z_x)\phi'(Z_b)H_i^{(1)}H_j^{(1)}]E_2[\phi'(Y_i)\phi'(Y_x)]\\
&+G_{xb}\sum_j M_{bj}E_1[\phi'(Z_x)\phi'(Z_b)H_x^{(1)}H_j^{(1)}]E_2[S\phi''(Y_x)]\},
\end{aligned}\tag{C4.A6}
\]

and

\[
\begin{aligned}
\mathcal B(\alpha)={}&\sum_{a,b}p_ap_b\{(Q_{ab}+G_{ab}E_1[\phi'(Z_a)\phi'(Z_b)])
                         E_2[H_x^{(2)}\phi'(Y_a)S\phi'(Y_b)]\\
 &+G_{ab}E_1[\phi'(Z_a)\phi'(Z_b)H_x^{(1)}\mu_b]E_2[\phi'(Y_x)\phi'(Y_a)]
  +G_{ab}E_1[\phi'(Z_a)\phi'(Z_b)H_a^{(1)}\mu_b]E_2[H_x^{(2)}\phi''(Y_a)]\}.
\end{aligned}\tag{C4.A7}
\]

All sums in (C4.A6)--(C4.A7) are over training indices. The factors involving
alpha in each expectation are exactly displayed; all other factors are
bounded in absolute value by one, P or 2P as appropriate. For example,
`Q_xb=E_1[H_x^(1)H_b^(1)]` has bounds `l_0`, while `E_2[S^2phi'(Y_x)phi'(Y_b)]` has bounds
`P^2 u_1`. Independence of lower and upper roots is not asserted for the
network; these are separate scalar expectations whose products follow
from the already derived response formula. Each is bounded separately.

The identity `phi'(Z_x) H_x^(1)=-phi''(Z_x)/2` improves the last term of (C4.A6).
Termwise product differentiation and sums of absolute label weights yield

\[
 |\mathcal F^{(k)}(\alpha)|\le P^3[l_0*u_1+3g*l_1*u_1+g*l_2*u_2]_k,
\]
\[
 |\mathcal B^{(k)}(\alpha)|\le P^3[4u_0+2l_0*u_1]_k,
 \qquad |a^{(k)}(\alpha)|\le2P u_0(k).
 \tag{C4.A8}
\]

Thus a bound for `sup_alpha |F^(8)(alpha)|` is the eighth entry of

\[
 t*2\left\{(27/50)^3
 \left[\tfrac{20}3 l_0*u_1+12g*l_1*u_1+4g*l_2*u_2
                         +\tfrac{16}3u_0\right]
          +2(1/10)(27/50)u_0\right\}.
 \tag{C4.A9}
\]

Every entry and operation in (C4.A2)--(C4.A9) is rational. The retained producer
evaluates them using exact integer/Fraction arithmetic and asserts the
final strict rational comparison to `10^-6`.

##### From derivative bounds to the periodic rule

For a 2pi-periodic C8 function with eighth derivative bounded by D, eight
integrations by parts give `|Fhat_k|<=D/|k|^8` for nonzero k. Its Fourier
series is absolutely convergent, equals F, and can be averaged termwise
over the N roots of unity. Only multiples of N survive, so the error is
at most `2 zeta(8)D/N^8`. The elementary integral comparison gives
`zeta(8)<=1+integral_1^infty x^-8 dx=8/7`. Using this slightly loose bound
and (C4.A9) proves (C4.A1) by the exact rational check.

Finally, the lower-root reflection `(xi_1,xi_2)->(xi_1,-xi_2)`,
together with exchange of training indices 2 and 3 and their equal
labels, gives `J(-alpha)=J(alpha)` and `a(-alpha)=a(alpha)`. Oddness of
tanh and the linear readout gives `J(alpha+pi)=-J(alpha)` and the same
for a. These properties also follow directly from (C4.A5)--(C4.A7), by changing
the passive signs and permuting training indices under reflection. The
teacher has the same two symmetries, hence F is even and pi-periodic.
Its value at pi/2 is zero because the teacher is zero. Therefore its full
N=256 rule is exactly

\[
 \frac{2}{256}F(0)+\frac{4}{256}
                   \sum_{j=1}^{63}F(2\pi j/256).
 \tag{C4.A10}
\]

This symmetry is used for the exact integrand, not inferred from
floating-point parity tests. Each of the 64 computed nodal values still
requires its own rigorous primitive/covariance/rounding enclosure.

#### C.4 certificate: exact interval assembly

##### Input constants and outward intervals

An interval has rational endpoints. Each elementary interval operation first
computes its endpoint extrema in Python integer/Fraction arithmetic, then
rounds the lower endpoint down and the upper endpoint up to multiples of
`2^-96`. Thus rounding in this layer enlarges the enclosure explicitly.
Addition, negation and multiplication use the endpoint sum/sign/product
rules. Reciprocal is used only for an interval with strictly one sign, and
division multiplies by its reciprocal. The general nonnegative-integer
power uses repeated interval products, preserving enclosure even when this
overestimates a square near zero. No floating-point comparison decides an
interval's mathematical sign.
An exact rational scalar is multiplied into the endpoints before outward
rounding. In particular the tiny Taylor coefficients are not first widened
to the absolute dyadic grid and then multiplied by large powers. This order and
the trigonometric-width gate keep the intervals
usefully narrow while preserving rigorous enclosure.

Pi is enclosed by

\[
 \pi=16\arctan(1/5)-4\arctan(1/239).
 \tag{C4.D1}
\]

For each arctangent the producer sums the first 64 terms of its alternating
power series exactly and encloses the remainder by the next positive term.
This series follows by integrating the geometric series for `1/(1+x^2)`;
the integrated remainder has the sign and bound of that next term.
For completeness, the tangent addition formula gives
`tan(4 arctan(1/5))=120/119` and
`tan(4 arctan(1/5)-arctan(1/239))=1`. The angle is between zero and pi/2,
so it is pi/4. This proves (C4.D1), not merely a numerical pi assumption.
The resulting rational interval is checked to lie inside `(25/8,22/7)`.

Square roots of positive rational endpoints are bounded by integer square
roots after multiplication by `2^192`. If `a=floor(sqrt(v)*2^96)`, then
`a/2^96<=sqrt(v)<(a+1)/2^96`; flooring the rational argument before the
integer square root gives that same integer a. Endpoint monotonicity then
encloses `sqrt(5)` and `1/sqrt(2pi)`. Labels are the exact intervals for
`p=(1/3,(1-sqrt(5))/12,(1-sqrt(5))/12)`. Their absolute sum is checked
below `P=27/50`. The binary64 labels passed to the kernel are independently
checked against the same P bound. The sum of their individual interval
deviations is denoted `epsilon_p`.

For every circle node and training angle, sin and cos are enclosed by their
Taylor polynomial of degree 79. The actual nonzero terms are summed using
the outward interval operations above. Every argument has absolute value
at most five, including `3 alpha`. The real Taylor remainder is at most
`5^80/80!`, since every real derivative of sin or cos is bounded by one.
This covers both the polynomial truncation and uncertainty in its argument;
no library trigonometric error assumption enters the proof. The binary64
values passed to the kernel are treated as exact dyadic constants, whose
errors are subsequently charged through their covariance discrepancy.

The normal-density constant passed to the kernel is checked to differ from
the exact `1/sqrt(2pi)` by less than `10^-15`. Received binary64 inputs are
echoed by the kernel as their integer IEEE bit patterns and compared with
the intended inputs. Reported primitive sums are also returned as bits;
the driver converts those bits to exact dyadic rationals before enlarging
them by error intervals. Thus decimal parsing or printing is not an
unexamined precision assumption.

##### Certified grid selection before integrand evaluation

For either specified dyadic root matrix A, let
`c_j=max_i |A_ij|`, in exact rational arithmetic. For the fixed
exponent target `B=26`, put

\[
 a_j=\min\{7,3/(4c_j)\},\quad
 h_j^*=\frac{6a_j}{B+a_j^2/2},\quad
 h_j=2^{-10}\lfloor2^{10}h_j^*\rfloor,
 \quad m_j=\lceil8/h_j\rceil.
 \tag{C4.D2}
\]

When `c_j=0`, take `a_j=7`. A zero fourth upper column can instead be
omitted exactly. All retained axes must pass
`0<h_j<=1`, `1<=m_j<=200`, `8<=m_j h_j<=9`. The dyadic spacings are
exactly representable. The driver additionally verifies, by rational
comparison,

\[
 c_ja_j\le3/4<\pi/4,\qquad
 6a_j/h_j-a_j^2/2\ge B,\qquad h_j^2\le18/B.
 \tag{C4.D3}
\]

Since pi>3, these imply the strip exponent and Gaussian-mass bounds used
in (C4.E1)--(C4.E5), with truncation radius at least eight.
They require no accuracy guarantee for a transcendental grid calculation.
In at most four dimensions the resulting analytic error envelope is

\[
 e_{\rm rule}\le 5\,10^{-11} M_{\rm strip}
                         +6\,10^{-15}M_{\rm real}.
 \tag{C4.D4}
\]

The proof and finite rational exponential lower bounds are in
the Gaussian-error proof above. The same inequalities with the optional
target B=30 allow the envelope `10^-12 M_strip` when
`M_real<=M_strip`. The actual floating-point sums are not normalized to
unit Gaussian mass. Training moments computed with three roots are
bounded by the same conservative four-dimensional envelope; they must
not be artificially multiplied by a passive rule mass.

Grid selection depends only on the specified root-column sizes and the
fixed target. It does not use the value or sign of the coefficient.
The slight rational conservatism relative to (C4.E5) changes work, not the
theorem or error envelope.

##### Enclose the two Gaussian laws and all primitive moments

Each reported primitive is enlarged first by `10^-9`, the proved arithmetic
envelope in the arithmetic proof above. The checked kernel input and compiler
contracts are retained in the run. The supplied-state kernel checks
independently test this implementation;
they are separate from the analytic error proof.

For the lower law, the exact input directions are enclosed as above. Their
original Gram G is obtained by interval dot products. The actual dyadic
directions `u_hat` used in the sum have exact rational Gram
`G_hat=u_hat u_hat^T`. Let `epsilon_G` enclose the maximum entry difference.
Both matrices are positive semidefinite, including the original singular G.
The covariance perturbation proof (C4.E6)--(C4.E8) gives these
primitive radii in addition to arithmetic and analytic rule error:

| Lower primitive | Strip / real bound | Covariance-error radius |
|---|---|---|
| `Q_ij=E_1[H_i^(1) H_j^(1)]` | `1 / 1` | `2 epsilon_G` |
| `L_ab=E_1[phi'(Z_a) phi'(Z_b)]` | `4 / 1` | `3 epsilon_G` |
| `mathcal T_abij=E_1[phi'(Z_a) phi'(Z_b) H_i^(1) H_j^(1)]` | `4 / 1` | `9 epsilon_G` |

The producer retains all entries, including the response tensor. Their
intervals enclose the true lower expectations, rather than moments for a
whitened or independent-sample substitute.

For the upper law, ordinary floating-point linear algebra chooses a convenient
four-by-four matrix `A_hat` whose training rows have zero fourth column.
These calculations are **not** used as a theorem that its covariance equals
Q. Treat its stored entries as exact dyadic numbers and form
`Q_hat=A_hat A_hat^T` exactly. This matrix is positive semidefinite by its
construction. Let `epsilon_Q` enclose its largest entry discrepancy from
the already certified lower Q intervals. This directly charges any error
in the solve, square root, covariance conditioning or clipping of a tiny
negative conditional variance. No inverse of the true passive covariance
appears in a proof, and no smoothness of the selected factor is needed.

With `H_i^(2)=phi(Y_i)`, `phi=tanh`, and
`S=sum p_a H_a^(2)`, the table specifies each additional radius. Row names
are exactly the kernel output groups. The column labelled p-error charges
the difference between the dyadic supplied labels and the exact labels.

| Group | Exact expectation | Strip / real bound | Price radius | p-error |
|---|---|---|---|---|
| ES2 | `E_2 S^2` | `P^2 / P^2` | `2P^2 epsilon_Q` | `2P epsilon_p` |
| V, dynamic_V | `E_2 S^2 phi'(Y_a) phi'(Y_b)`, `E_2 S^2 phi'(Y_x) phi'(Y_b)` | `4P^2 / P^2` | `9P^2 epsilon_Q` | `2P epsilon_p` |
| ddgram, dynamic_dd | `E_2 phi'(Y_a) phi'(Y_b)`, `E_2 phi'(Y_x) phi'(Y_a)` | `4 / 1` | `3 epsilon_Q` | `0` |
| ESdd, dynamic_ESdd | `E_2 S phi''(Y_a)`, `E_2 S phi''(Y_x)` | `4P / P` | `5P epsilon_Q` | `epsilon_p` |
| dynamic_C | `E_2 H_x^(2) S phi'(Y_a) phi'(Y_b)` | `4P / P` | `9P epsilon_Q` | `epsilon_p` |
| dynamic_Hdd | `E_2 H_x^(2) phi''(Y_a)` | `4 / 1` | `5 epsilon_Q` | `0` |
| dynamic_SH | `E_2 S H_x^(2)` | `P / P` | `2P epsilon_Q` | `epsilon_p` |

Each radius is the sum of its arithmetic, rule, Price and p-error terms.
The Price constants follow by expanding the finite label sums in (C4.E8).
For p-error, `|S-S_hat|<=epsilon_p`, and
`|S^2-S_hat^2|<=(P+P)epsilon_p`; all other real factors have magnitude
at most one. Both label sums are checked below P, so the same constants
apply. This error analysis does not suppress a matrix-response mean.

##### Exact contraction and matching subtraction

The interval assembly uses mathematical training indices `a,b,i,j` in
`{1,2,3}` and the passive slot x. Its arrays use the bijection iota
specified above. Define

\[
 M_{bj}=p_j E_2[\phi'(Y_j)\phi'(Y_b)]+\mathbf1_{j=b}E_2[S\phi''(Y_b)],
\]
\[
 D_{ab}=L_{ab}V_{ab}+\sum_{i,j}\mathcal T_{abij}M_{ai}M_{bj},
 \quad \mathcal A=\sum_{a,b}p_ap_b(G_{ab}D_{ab}+Q_{ab}V_{ab}).
 \tag{C4.D5}
\]

All factors in these equations have the enclosing intervals above.
The producer verifies `B0=E_2 S^2` has a strictly positive lower endpoint,
then encloses `beta=8 mathcal A/(3B0)`. It must verify the resulting
interval lies in `[-1/10,1/10]`, which closes the explicit hypothesis
of the circle-rule proof above. Training quantities are recomputed within each
node's primitive rule; all resulting beta intervals enclose the same
exact number and must overlap. Their intersection is recorded as an
additional consistency check. Each independently valid node interval is
used for its own clock term, so this intersection is not needed to repair
an invalid summand.

For the passive coefficient, the implemented formulas are exactly
(C4.A6)--(C4.A7): `J(alpha)=4mathcal F(alpha)+(4/3)mathcal B(alpha)`,
`a(alpha)=2 E_2[S H_x^(2)]`. In particular, both the `p_i E_2[phi'(Y_i) phi'(Y_x)]` and
`E_2[S phi''(Y_x)]` response terms enter `mathcal F(alpha)`, and both `E_2[phi'(Y_x) phi'(Y_a)]` and
`E_2[H_x^(2) phi''(Y_a)]` response terms enter `mathcal B(alpha)`. These are the explicit contraction
of both directions of the same initialized matrix, not an independent
Gaussian replacement. The unweighted input Gram G remains the true
correlated rank-two Gram; labels p carry the mean-loss normalization.

Write `J_j=J(2pi j/256)` and `a_j=a(2pi j/256)` for angular
node values. The exact symmetry-reduced periodic mean is enclosed by
the interval sum

\[
 C_N=\frac2{256}\,2[J_0-\beta a_0]
 +\frac4{256}\sum_{j=1}^{63}
 2\cos(6\pi j/256)[J_j-\beta a_j].
 \tag{C4.D6}
\]

The teacher factors are certified trigonometric intervals. The raw teacher
projection and clock subtraction are separately saved, as is their difference.
Adding `[-10^-6,10^-6]` to the nodal enclosure covers the remaining circle
error by the circle-rule proof above. This produces an enclosing interval for the
exact chi, including every stated approximation axis.

##### Decision and finite-time consequence

Only a strictly positive lower endpoint or strictly negative upper endpoint
decides the sign. All comparisons use exact rational endpoints. A zero-crossing
interval is inconclusive. No coarse/fine agreement or empirical confidence
level enters this decision. The sign proof combines the full mathematical
error bounds with the executing source and its checked arithmetic contracts.

If the certified lower endpoint is c>0, combine it with the already proved
`|R(g_tau(t))-R(f_t)-chi t^3|<=M t^4` on `[0,T]`. Then for
`0<t<=min(T,c/(2M))`, one has `R(g_tau(t))-R(f_t)>=c t^3/2>0`.
The negative case is identical after reversing signs. T,M retain their
original fixed-model, width-independent local scope; no evaluated time
radius or quantitative width rate is added by the certificate.

#### C.4 certificate: evaluated enclosure and reproducible decision

The complete fixed algorithm is
[certificate.py](../code/tools/two_layer_risk/certificate.py), its private
C++ kernel, and the exact angular-bound helper linked above. The
[tool guide](../code/tools/two_layer_risk/README.md) specifies the complete
input, arithmetic, resource and failure contracts, a fresh-output command,
an API example, and independent elementary-function and supplied-rule tests.
The mathematical coefficient and its inputs are fixed by (C4.1)--(C4.6).
Numerical linear algebra proposes dyadic root factors only; its accuracy
is charged by (C4.E6), not assumed. No retained array, study or Git history
is needed to regenerate the certificate.

At target `B=26`, the specified 256-angle rule, reduced to 64 evaluations,
and the certified root rules produce the enclosing interval

\[
 \frac{5358604107658561212253567}{19807040628566084398385987584}
 \le\chi\le
 \frac{21597479156841685713774185}{79228162514264337593543950336}.
 \tag{C4.32}
\]

It includes the full Gaussian-rule, covariance, elementary-function,
summation, input-constant, label, interval-rounding and circle-rule errors.
For the training clock the same execution gives

\[
 \frac{2797504526179671494928101665}{79228162514264337593543950336}
 \le\beta\le
 \frac{2797556156441557459457527739}{79228162514264337593543950336}.
 \tag{C4.33}
\]

Exact integer cross-multiplication places (C4.32)--(C4.33) strictly inside
(C4.8a), and in particular verifies the separate `|beta|<=1/10` premise
used for the circle bound. The displayed endpoints are approximately
`[0.00027054037037366814,0.00027259851133052906]` for chi and
`[0.03530947124611157,0.03531012291163362]` for beta; these decimal
displays do not decide any inequality. The angle bound obtained from
(C4.A9) is, more precisely,

\[
 D_8=\frac{41272525446939874982}{31640625},\qquad
 \frac{16D_8}{7\,256^8}
 =\frac{20636262723469937491}{127677049435953561600000000}
 <10^{-6}.
 \tag{C4.34}
\]

The evaluated calculation used 86,101,134 upper Gaussian nodes. The
complete mathematical bounds and executed finite arithmetic jointly
constitute a computer-assisted proof. Neither its positive output flag,
agreement at two resolutions, nor an unadjusted teacher projection would
alone prove the sign. A reproduced run may propose slightly different
dyadic factors on another supported platform; it certifies its own
enclosure only after all runtime contracts pass. The displayed enclosure
is the evaluated certificate, not a promised bit-identical result across
arbitrary platforms. The small local risk conclusion is exactly (C4.8),
with the finite-width and time limitations stated above.
