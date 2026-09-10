### C.4. A controlled local risk expansion at equal training loss

This subsection compares learned and frozen features for one fixed design.
It proves a cubic expansion with a fourth-order remainder on the actual
population flow. The coefficient's sign and nonvanishing remain open.
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
`tau(t)>=0` with `tau(0)=0` and `L(g_tau(t))=L(f_t)` for `0<=t<=T`. Uniformly
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
not numerically evaluated. The cubic term is the first possible risk
contribution. Neither `chi!=0` nor a sign is asserted. If a separate
rigorous bound proves `chi!=0`, then with
`t0=min(T,abs(chi)/(2M))`,

\[
\operatorname{sign}(\chi)\,[R(g_{\tau(t)})-R(f_t)]
\ge\tfrac12|\chi|t^3>0\qquad(0<t\le t_0).
\tag{C4.8}
\]

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
Enlarge the finitely many constants to one `M>=1`. Inequality (C4.8)
then follows from `Mt<=abs(chi)/2`.

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
E[\Gamma_{F_1}\Gamma_{F_2}]=E_2[F_1F_2],
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

If the separate sign premise in (C4.8) is proved, its positive minimum
magnitude on every fixed `[delta,t0]` transfers that sign with probability
tending to one. This uses only `n -> infinity` with any deterministic
`eta_n -> 0` for raw GD, or the C.1 finite-GF corollary, on the fixed local
horizon. The small finite readout can produce lower-order terms before the
width limit, so no statement uniform down to time zero at finite width
follows.

C.3 already proves nonzero order-`t^2` activation and preactivation
displacements, order-`t` speeds, and locally positive absolute nonaffinity
for each training hidden marginal under this model's verified hypotheses.
Equations (C4.19)--(C4.21) provide the corresponding controlled onset
directions. These activity facts do not determine `chi`. If `chi=0`, a
later coefficient is required; if a sign is eventually proved, it concerns
only this fixed early-time comparison. No general feature-learning benefit,
global continuation, growing-design limit, or sample-complexity conclusion
is established here.
