# Nonlinear tanh obstruction for frozen-NTK truncation

Correction and supersession, 2026-10-10: the two-hidden-layer early-time
argument below is superseded by the general-input proof in
[TANH_LOWER_ROUTE.md](TANH_LOWER_ROUTE.md). Its equation (11) used a
remainder coefficient `1/6` where the double integral gives `1/3`.
Do not use the old remainder constants. The amended proof and checked
two-sided result are in [TANH_RESULT.md](TANH_RESULT.md) and
[TANH_CHECK.md](TANH_CHECK.md). This correction does not concern the
separate one-hidden-layer discussion.

Scope and status: this is a scoped derivation, not an independent review or a
promoted result. The initial scientific input was the supervisor's self-contained
assignment. The subsequently authorized additional input was lines 1–150 of
`docs/08b-trajectory-compression.qmd`, used only for its architecture and scaling.
No other study or scientific source was read. Required repository instructions,
`solve-math-rigorously`, and the canonical-notation skill and neural-network
reference were read. The arguments below are complete mathematical candidates;
they have been algebraically checked by their author but not independently reviewed.

There are two different conclusions. For the canonical network with **two trained
hidden tanh layers**, a deterministic estimate gives an actual prediction gap at
a fixed positive time, with probability tending to one. It does not by itself
prove a dense-versus-dense concentration rate. For **one trained hidden tanh
layer**, an additional elementary coupling proves that independent dense runs
differ by \(O_{\mathbb P}(n^{-1/2})\) on every fixed compact time interval and finite
training panel. Neither argument alone establishes a complete-time, whole-sphere
dense-variability bound.

All flows below use the half-MSE loss

\[
\mathcal L=\frac1{2m}\sum_{a=1}^m(f_n(x_a)-y_a)^2.
\]

The book passage instead uses the full MSE. Its physical flow is twice the flow
here: replace time \(t\) below by \(2t\). No width-dependent clock is used.

## 1. Exact NTH convention and the omitted fourth tensor

Let \(\theta\) collect the parameters, let \(M\) be the constant diagonal block
mobility matrix, and write \(r_a=f_n(x_a)-y_a\). Define

\[
K^{(2)}_{ab}=\nabla f_n(x_a)^\top M\nabla f_n(x_b),\qquad
K^{(j+1)}_{a_1\cdots a_j b}
 =\nabla K^{(j)}_{a_1\cdots a_j}^\top M\nabla f_n(x_b).
\]

Then exact differentiation along gradient flow gives

\[
\dot f_a=-\frac1m\sum_bK^{(2)}_{ab}r_b,\qquad
\dot K^{(j)}_{a_1\cdots a_j}
 =-\frac1m\sum_bK^{(j+1)}_{a_1\cdots a_jb}r_b.
\]

The order-two truncation freezes \(K^{(2)}\) at initialization and solves
\(\dot g=-K^{(2)}(0)(g-y)/m\), with \(g(0)=0\). In both architectures below,
the readout is exactly zero initially and the tangent kernel is the sum of a
readout feature Gram and terms quadratic in the readout. Its derivative in a
readout direction therefore vanishes at initialization; the hidden part of
\(M\nabla f_b\) also vanishes there. Consequently
\(K^{(3)}(0)=0\) exactly at every width. The truncation which retains and freezes
\(K^{(3)}\) is identical to the frozen-NTK model. Thus every conclusion for
order two also holds for order three under this stated truncation convention.

There is a useful exact identity for any differentiable hidden feature map
\(h_a(w)\in\mathbb R^n\), readout \(u\), and output
\(f_a=u^\top h_a(w)/n\). Put

\[
H_y(w)=\frac1m\sum_a y_a h_a(w),\qquad
F(\theta)=\frac1m\sum_a y_af_a=\frac1n u^\top H_y(w).
\]

Here \(H_y\) is a vector and \(F\) is a scalar. With readout mobility \(n\) and
hidden mobility matrix \(M_w\), consider the auxiliary source flow
\(\theta'=M\nabla F\). At \(u=0\),

\[
u'=H_y,\quad w'=0,\quad u''=0,\quad
w''=\frac1nM_wD_wH_y^\top H_y.
\]

Differentiating \(F=u^\top H_y/n\) three times at this point gives

\[
F'''_{\rm source}(0)
 =\frac4{n^2}\big\|D_wH_y^\top H_y\big\|_{M_w}^2
 =\frac1{m^4}\sum_{a,b,c,d}y_ay_by_cy_dK^{(4)}_{abcd}(0),
\tag{1}
\]

where \(\|v\|_{M_w}^2=v^\top M_wv\). The coefficient 4 consists of the
one contribution from \(u'''\) and the three product-rule contributions from
\(u'\) and \(w''\). This is positivity of a contraction, not componentwise
positivity of the general fourth tensor.

For the actual training flow, let \(f\) be its output and \(g\) the frozen-NTK
output. Since \(K'(0)=0\), differentiating the prediction equations yields

\[
f'(0)=g'(0)=K(0)y/m,\qquad
f''(0)=g''(0)=-K(0)^2y/m^2,
\]

and

\[
f'''(0)-g'''(0)=K''(0)y/m,\qquad
K''_{ab}(0)=\frac1{m^2}\sum_{c,d}K^{(4)}_{abcd}(0)y_cy_d.
\]

Therefore the third derivative of \(y^\top(f-g)/m\) equals (1). A nonzero
derivative alone would not prove a fixed-time lower bound uniform in width.
The next section supplies that missing step without relying on a width-uniform
fourth-derivative estimate.

## 2. Two hidden tanh layers: a fixed-time finite-width lower bound

Take \(m=d=2\), \(v_a=x_a/\sqrt d=e_a\), \(y=(y_0,0)\), with
\(0<y_0\le1\). The matrices and vectors are

\[
\begin{aligned}
z_a^{(1)}&=W^{(1)}v_a,& h_a^{(1)}&=\tanh z_a^{(1)},\\
z_a^{(2)}&=W^{(2)}h_a^{(1)},& h_a&=\tanh z_a^{(2)},\\
f_a&=u^\top h_a/n.
\end{aligned}
\]

Initialization is independent across blocks, with
\(W^{(1)}_{ij}\sim N(0,1)\), \(W^{(2)}_{ij}\sim N(0,1/n)\), and \(u=0\).
The block mobilities are \((n,1,n)\). Thus both hidden layers actually train.
All constants in this section are independent of width and of \(y_0\in(0,1]\).

For hidden increments \(V=(V^{(1)},V^{(2)})\), define the inner product whose
squared norm is

\[
\|V\|_{\rm hid}^2=\|V^{(1)}\|_F^2/n+\|V^{(2)}\|_F^2.
\]

For feature vectors use \(\langle b,c\rangle_n=b^\top c/n\), with norm
\(\|b\|_n\). Let \(J_a=D_wh_a\), and let \(J_a^*\) denote the adjoint between
these two inner-product spaces. Writing \(p_a^{(\ell)}=\operatorname{sech}^2
z_a^{(\ell)}\), direct differentiation gives

\[
\begin{aligned}
(J_a^*b)^{(1)}
 &=\big[p_a^{(1)}\odot W^{(2)\top}(b\odot p_a^{(2)})\big]v_a^\top,\\
(J_a^*b)^{(2)}&=(b\odot p_a^{(2)})h_a^{(1)\top}/n.
\end{aligned}
\tag{2}
\]

For a coefficient vector \(c\in\mathbb R^m\), define
\(H_c=m^{-1}\sum_ac_ah_a\) and \(J_c=m^{-1}\sum_ac_aJ_a\), holding the
coefficients fixed when taking this derivative. The exact flow and kernel are

\[
\dot u=H_y-H_f,\qquad
\dot w=J_y^*u-J_f^*u,
\tag{3}
\]

\[
K_{ab}=\langle h_a,h_b\rangle_n+
       \langle J_a^*u,J_b^*u\rangle_{\rm hid}.
\tag{4}
\]

These are formulas for the full nonlinear finite network.

### Uniform early-time estimates

Work initially on the event \(\|W^{(2)}(0)\|_{\rm op}\le8\), and put

\[
M=9,\qquad B=\sqrt{M^2+1}=\sqrt{82},\qquad D=B^2/2=41.
\]

The loss decreases because \(\dot{\mathcal L}=-\nabla\mathcal L^\top
M\nabla\mathcal L\le0\). Consequently \(\|r(t)\|_2\le y_0\). Bounded tanh
and \(\operatorname{sech}^2\le1\) give, for \(0\le t\le1\),

\[
\|u(t)\|_\infty\le y_0t,\qquad
\|\dot W^{(2)}(t)\|_F\le y_0^2t,
\qquad \|W^{(2)}(t)\|_{\rm op}\le M.
\tag{5}
\]

Indeed \(m^{-1}\|r\|_1\le y_0\); each term of the second-layer velocity
has Frobenius norm at most \(|r_a|\|u\|_n/m\). Integration gives the operator
bound \(8+y_0^2t^2/2\le9\). Formula (2) and \(\|h_a^{(1)}\|_n\le1\) imply

\[
\|J_a\|_{\rm hid\to n}\le B,\qquad
\|\dot w\|_{\rm hid}\le By_0^2t,\qquad
\|\dot W^{(1)}\|_F/\sqrt n\le My_0^2t.
\tag{6}
\]

The derivative bound follows directly from
\(Dh_a[V]=p_a^{(2)}\odot(V^{(2)}h_a^{(1)}+
W^{(2)}(p_a^{(1)}\odot V^{(1)}v_a))\) and Cauchy–Schwarz in the two blocks.
Thus

\[
\|h_a(t)-h_a(0)\|_n\le Dy_0^2t^2,
\quad
\|h_a^{(1)}(t)-h_a^{(1)}(0)\|_n\le(M/2)y_0^2t^2,
\tag{7}
\]

and the same bound \(Dy_0^2t^2\) holds for
\(\|z_a^{(2)}(t)-z_a^{(2)}(0)\|_n\). For the latter, expand
\(W^{(2)}(t)h_a^{(1)}(t)-W^{(2)}(0)h_a^{(1)}(0)\), use (5), and use
\(1+8M\le1+M^2=B^2\).

Each entry of the readout Gram changes by at most \(2Dy_0^2t^2\); each entry
of the hidden Gram in (4) is at most \(B^2y_0^2t^2\). Since \(m=2\),

\[
\|K(t)-K(0)\|_{\rm op}\le C_Ky_0^2t^2,
\qquad C_K=4B^2=328.
\tag{8}
\]

No Gaussian coordinatewise maximum or bound on \(W^{(1)}(0)\) enters these
estimates. They also prevent finite-time blow-up on the stated interval:
the readout, hidden operator norm, and increments of both hidden matrices
remain bounded. The smooth finite-dimensional ODE therefore extends throughout it.

### A positive contribution from the last hidden layer

Define the fixed positive constants

\[
\gamma_1=\mathbb E\tanh^2G,\qquad
\kappa_2=\mathbb E\left[
\tanh^2(\sqrt{\gamma_1}G)\operatorname{sech}^4(\sqrt{\gamma_1}G)\right],
\qquad G\sim N(0,1).
\]

Both are positive because their nonnegative integrands are positive away from
zero. Use the first training sample to define

\[
q_1(t)=\|h_1^{(1)}(t)\|_n^2,\qquad
b_2(t)=\frac1n\sum_i\tanh^2z_{1i}^{(2)}(t)
                         \operatorname{sech}^4z_{1i}^{(2)}(t).
\]

Consider the initialization event

\[
\mathcal E_n=\left\{\|W^{(2)}(0)\|_{\rm op}\le8,
q_1(0)\ge\gamma_1/2,\ b_2(0)\ge\kappa_2/2\right\}.
\tag{9}
\]

The function \(\tanh^2z\operatorname{sech}^4z\) has derivative bounded in
absolute value by 6. By (7),

\[
|q_1(t)-q_1(0)|\le My_0^2t^2,\qquad
|b_2(t)-b_2(0)|\le3B^2y_0^2t^2.
\]

It follows on \(\mathcal E_n\) that \(q_1(t)\ge\gamma_1/4\) and
\(b_2(t)\ge\kappa_2/4\) whenever

\[
0\le t\le T_A:=\min\left\{1,
\sqrt{\gamma_1/(4M)},\sqrt{\kappa_2/(12B^2)}\right\}.
\]

Let \(A(t)=J_y^*H_y\). Since \(H_y=y_0h_1/2\), the second block in (2) gives
the exact identity

\[
\|A^{(2)}(t)\|_F^2
 =\frac{y_0^4}{16}q_1(t)b_2(t).
\]

Therefore

\[
\|A(t)\|_{\rm hid}^2\ge a y_0^4,
\qquad a=\gamma_1\kappa_2/256>0,
\quad 0\le t\le T_A.
\tag{10}
\]

This lower bound uses only one hidden block; first-layer training cannot
cancel it, because the two blocks contribute squared norms.

### An integrated lower bound, with an explicit error estimate

The prediction bound \(|f_a(t)|\le\|u(t)\|_n\le y_0t\) gives
\(\|H_f(t)\|_n\le y_0t\). Moreover (6) bounds the feature velocity by
\(\|\dot h_a(t)\|_n\le B^2y_0^2t\). Integrating (3) therefore yields

\[
\begin{aligned}
\|u(t)-tH_y(t)\|_n
&\le\int_0^t\|H_y(s)-H_y(t)\|_n\,ds
    +\int_0^t\|H_f(s)\|_n\,ds\\
&\le B^2y_0^3t^3/6+y_0t^2/2
 \le E y_0t^2,
\qquad E=\tfrac12+B^2/6.
\end{aligned}
\tag{11}
\]

Differentiate the squared label-feature norm using (3):

\[
\frac d{dt}\|H_y\|_n^2
 =2\langle A,J_y^*u-J_f^*u\rangle_{\rm hid}.
\]

Here \(\|A\|_{\rm hid}\le By_0^2/4\),
\(\|J_y\|\le By_0/2\), and \(\|J_f\|\le By_0t\). Substituting
\(u=tH_y+(u-tH_y)\) and applying (11) gives the uniform estimate

\[
\frac d{dt}\|H_y\|_n^2
 \ge2t\|A\|_{\rm hid}^2-C_Ey_0^4t^2,
\qquad C_E=B^2(E/4+1/2).
\tag{12}
\]

This explicitly bounds the error left after the positive leading term. It
is uniform in the Gaussian initialization on event (9), in width, and in
\(0<y_0\le1\). Unlike a formal jet calculation, it controls the integrated
trajectory. Combining (10)–(12), for
\(t\le\min(T_A,a/C_E)\),

\[
\|H_y(t)\|_n^2-\|H_y(0)\|_n^2
 \ge (a/2)y_0^4t^2.
\]

Equation (4), with \(u(0)=0\), now implies

\[
y^\top[K(t)-K(0)]y
 =m^2\left(\|H_y(t)\|_n^2-\|H_y(0)\|_n^2
              +\|J_y^*u(t)\|_{\rm hid}^2\right)
 \ge2a y_0^4t^2.
\tag{13}
\]

Let \(e=f-g\). Variation of constants, which follows by differentiating the
integrating factor, gives

\[
e(t)=\frac1m\int_0^t e^{-K(0)(t-s)/m}
                  [K(s)-K(0)](y-f(s))\,ds.
\tag{14}
\]

The initial kernel is positive semidefinite with operator norm at most \(m\).
Thus its exponential is a contraction and differs from the identity by at
most \(t-s\). Combining (8) and \(\|f(s)\|_2\le\sqrt2 y_0s\), the difference
between the scalar integrand in \(y^\top e(t)/m\), before its factor \(m^{-2}\),
and \(y^\top[K(s)-K(0)]y\) has absolute value at most

\[
C_K(1+\sqrt2)y_0^4t s^2.
\]

Set the fixed positive physical time bound

\[
T_0=\min\left\{T_A,\ a/C_E,\ a/[C_K(1+\sqrt2)]\right\}>0.
\tag{15}
\]

For every width, every initialization in \(\mathcal E_n\), and every
\(0<t\le T_0\), (13)–(14) imply

\[
\frac1m y^\top(f(t)-g(t))\ge\frac{a}{12}y_0^4t^3,
\qquad
f_1(t)-g_1(t)\ge\frac{a}{6}y_0^3t^3
 =\frac{\gamma_1\kappa_2}{1536}y_0^3t^3.
\tag{16}
\]

The time bound is deliberately crude and is not a practical calibration.
Its role is to be strictly positive and independent of width.

### Probability of the initialization event and the Gram-gap assumption

The sample mean \(q_1(0)\) converges in probability to \(\gamma_1\): its terms
are independent and bounded, so its variance is at most \(1/n\).
Conditional on the first-layer features, the second-layer preactivations at
the first sample are independent \(N(0,q_1(0))\). Hence the conditional
variance of \(b_2(0)\) is at most \(1/n\), and its conditional expectation is
the continuous function

\[
q\longmapsto\mathbb E[
\tanh^2(\sqrt qG)\operatorname{sech}^4(\sqrt qG)].
\]

Continuity follows by bounded convergence. Consequently
\(b_2(0)\to\kappa_2\) in probability.

For completeness, the operator-norm event also has probability tending to
one without importing a random-matrix limit. A Euclidean unit-sphere net of
radius \(1/4\) with at most \(9^n\) points is obtained from a maximal separated
set by comparing volumes of disjoint balls. Approximation of both unit
vectors gives \(\|W\|_{\rm op}\le2\max_{p,q\text{ in net}}|p^\top Wq|\).
Each fixed bilinear form for \(W^{(2)}(0)\) is \(N(0,1/n)\). The elementary
Gaussian Chernoff bound and a union bound therefore give

\[
\mathbb P(\|W^{(2)}(0)\|_{\rm op}>8)
 \le2\exp\{(2\log9-8)n\}\longrightarrow0.
\]

Thus \(\mathbb P(\mathcal E_n)\to1\), proving that (16) is a high-probability
finite-width prediction lower bound.

The two orthogonal inputs also satisfy the required positive population
feature-Gram condition. In layer one their limiting Gram is
\(\gamma_1I_2\): oddness and independence give zero cross entry. In layer two
it is \(\gamma_2I_2\), where
\(\gamma_2=\mathbb E\tanh^2(\sqrt{\gamma_1}G)>0\). This follows directly from
the Gaussian covariance recursion in the supplied setup. Tanh is holomorphic
on any strip strictly inside \(|\operatorname{Im}z|<\pi/2\), with bounded
derivatives on a smaller strip. The label \(y_0>0\) can be chosen arbitrarily
small, so it can also satisfy the book's additional fixed small-label condition.

## 3. One hidden layer: exact population reduction and explicit remainder

This section has the separate architecture

\[
f_n(x_a)=\frac1n\sum_{i=1}^nu_i\tanh z_{ia},\qquad
z_{ia}=a_i\cdot v_a,
\]

with the same \(m=d=2\), \(v_a=e_a\), \(y=(y_0,0)\), both block mobilities
equal to \(n\), independent \(a_i(0)\sim N(0,I_2)\), and \(u_i(0)=0\).
The exact particle equations are

\[
\dot u_i=-\tfrac12\sum_a r_a\tanh z_{ia},\qquad
\dot z_{ia}=-\tfrac12r_au_i\operatorname{sech}^2z_{ia}.
\tag{17}
\]

The following deterministic population solution is constructed explicitly;
it is not assumed to be the limit of (17). Let \(G_1,G_2\) be independent
standard Gaussians, and solve, in the scalar feature clock \(\tau\),

\[
\partial_\tau u=\tanh z,\qquad
\partial_\tau z=u\operatorname{sech}^2z,\qquad
u(0)=0,\ z(0)=G_1.
\tag{18}
\]

The second preactivation remains \(G_2\). Define

\[
F(\tau)=\mathbb E[u(\tau)\tanh z(\tau)],\quad
K(\tau)=F'(\tau)=\mathbb E[
\tanh^2z+u^2\operatorname{sech}^4z],
\]

and set \(\dot\tau=(y_0-F(\tau))/2\), \(\tau(0)=0\). Independence and
oddness imply that the second prediction is identically zero. Hence the
resulting physical-time state solves the population version of (17).

For \(\tau\ge0\), \(|u|\le\tau\) and \(|z-G_1|\le\tau^2/2\).
Moreover direct differentiation proves the pointwise invariant

\[
\cosh^2z-u^2=\cosh^2G_1.
\tag{19}
\]

For positive \(G_1\), both \(u\) and \(z-G_1\) are nonnegative; the negative
case is obtained by the sign symmetry, and at \(G_1=0\) the solution is zero.
Thus \(|z|\) never decreases. Writing \(p=\operatorname{sech}^2z\), the
integrand of \(K\) is

\[
1-\cosh^2G_1\,p^2.
\]

It increases from \(\tanh^2G_1\) and is at most one. Consequently, with
\(\gamma=\mathbb E\tanh^2G\),

\[
0<\gamma\le K(\tau)\le1.
\tag{20}
\]

All differentiation under expectation is justified by the displayed uniform
bounds on \(u,z-G_1\), bounded tanh derivatives, and the resulting deterministic
bounds on each integrand derivative on compact \(\tau\) intervals. Gaussian
unboundedness of \(G_1\) creates no unbounded dominating function.

Put \(\kappa=\mathbb E[\tanh^2G\operatorname{sech}^4G]>0\). A useful explicit
remainder bound is

\[
\left|K(\tau)-\gamma-2\kappa\tau^2\right|
 \le\frac{11}{3}\tau^4\qquad(\tau\ge0).
\tag{21}
\]

To verify it, abbreviate \(h=\tanh z\), \(p=h'\), \(q=h''\), and use
\(|h|,|p|\le1\), \(|q|\le2\). Differentiating gives

\[
K'(\tau)=\mathbb E[4uhp^2+2u^3p^2q].
\]

The bound on \(z-G_1\) implies
\(|u-\tau\tanh G_1|\le\tau^3/6\). Also
\(|(hp^2)'|=|p^3+2hpq|\le5\). Therefore

\[
|K'(\tau)-4\kappa\tau|
 \le4(1/6+5/2)\tau^3+4\tau^3
 =\frac{44}{3}\tau^3,
\]

and integration gives (21). In particular,
\(K(\tau)-\gamma\ge\kappa\tau^2\) for
\(\tau\le\tau_*:=\sqrt{3\kappa/11}\).

Let \(s(t)=y_0-F(\tau(t))\). Equation (20) implies

\[
\dot s=-K(\tau)s/2,\qquad
y_0e^{-t/2}\le s(t)\le y_0e^{-\gamma t/2},\qquad
\frac{y_0t}{2}e^{-T/2}\le\tau(t)\le\frac{y_0t}{2}
\quad(0\le t\le T).
\tag{22}
\]

The frozen population prediction is \(g_1(t)=y_0(1-e^{-\gamma t/2})\),
\(g_2=0\). The difference \(\delta(t)=F(\tau(t))-g_1(t)\) satisfies

\[
\delta(t)=\frac12\int_0^t e^{-\gamma(t-v)/2}
       [K(\tau(v))-\gamma]s(v)\,dv.
\]

The resulting bound is

\[
\delta(T)\ge\frac{\kappa}{24}y_0^3T^3e^{-2T}>0
\quad\text{whenever }y_0T/2\le\tau_*.
\tag{23}
\]

Indeed the four lower factors in the integral are respectively
\(e^{-T/2}\), \(\kappa\),
\(y_0^2v^2e^{-T}/4\), and \(y_0e^{-T/2}\), and
\(\int_0^T v^2\,dv=T^3/3\). At initialization the exact physical derivative
and leading coefficient are

\[
\delta'''(0)=\kappa y_0^3/2,
\qquad \delta(t)=\kappa y_0^3t^3/12+O(t^4).
\tag{24}
\]

The actual lower bound (23), rather than this final formal-looking expansion,
is what will be transferred to finite width.

For reference, the entire initialized fourth tensor can be computed in this
one-hidden-layer model. With \(h_a=\tanh G_a\), \(p_a=\operatorname{sech}^2G_a\),
the exact finite-width expression is the empirical mean of

\[
h_d\left[\mathbf1_{a=c}p_a^2h_b+
          \mathbf1_{b=c}h_ap_b^2+
          2\mathbf1_{a=b}h_cp_a^2\right].
\tag{25}
\]

This follows by applying the neuronwise direction
\(h_c\partial_u+up_c\partial_{z_c}\) to
\(h_ah_b+\mathbf1_{a=b}u^2p_a^2\), and then applying the direction with
index \(d\) at \(u=0\). In particular
\(\mathbb EK^{(4)}_{1111}=4\kappa\). If
\(\eta=\mathbb E\operatorname{sech}^4G\), the mixed entries include
\(\mathbb EK^{(4)}_{1122}=2\gamma\eta\) and
\(\mathbb EK^{(4)}_{1212}=\mathbb EK^{(4)}_{1221}=\gamma\eta\), all positive.
Entries with an odd total dependence on either independent Gaussian vanish
by parity. These mixed entries are not needed to obtain (23).

## 4. One hidden layer: compact-time finite-width fluctuations

Fix \(T<\infty\) and \(y_0>0\). Denote the deterministic population trajectory
constructed above by \(f_\infty(t)\). For each initialization \((G_{i1},G_{i2})\),
let \((\bar u_i,\bar z_{i1},\bar z_{i2})\) be the independent population
particle driven by that trajectory, and let

\[
\widehat f_{n,a}(t)=\frac1n\sum_i\bar u_i(t)\tanh\bar z_{ia}(t),\qquad
Z_{n,a}(t)=\widehat f_{n,a}(t)-f_{\infty,a}(t).
\]

Both a summand and its first time derivative are bounded by constants
depending only on \(T,y_0\), uniformly over the initial Gaussian values.
Independence, the variance identity for sample means, and Cauchy–Schwarz give

\[
\mathbb E\sup_{0\le t\le T}|Z_{n,a}(t)|
 \le\mathbb E|Z_{n,a}(0)|+
       \int_0^T\mathbb E|\dot Z_{n,a}(t)|\,dt
 \le C_{T,y_0}/\sqrt n.
\tag{26}
\]

Here \(Z(0)=0\); differentiating the mean under expectation is justified by
the same derivative bound. This proves a uniform-in-time empirical estimate
without assuming a functional central limit theorem.

Couple the actual finite particles in (17) to these population particles by
using their identical initial states. The finite flow has decreasing loss,
so \(\|r_n\|_2\le y_0\) and \(\max_i|u_i(t)|\le y_0T\). The population
readout satisfies the same upper bound. On this region, the right side of
(17) is Lipschitz in particle state and the two-component residual, with a
constant depending only on \(T,y_0\): this follows term by term from bounded
tanh and its first two derivatives. In particular the constant is uniform
over the Gaussian initial preactivations.

Let \(D_n(t)\) be the root mean square over particles of the difference
between their three-dimensional states. Subtract the integral equations,
apply the triangle inequality in the root mean square norm, and use the
Lipschitz output bound to obtain

\[
\begin{aligned}
D_n(t)&\le C_{T,y_0}\int_0^t
             (D_n(s)+\|f_n(s)-f_\infty(s)\|_2)\,ds,\\
\|f_n(t)-f_\infty(t)\|_2
 &\le C_{T,y_0}D_n(t)+\|Z_n(t)\|_2.
\end{aligned}
\]

Substitution followed by the elementary integral Gronwall inequality gives
\(\sup_{t\le T}D_n(t)\le C_{T,y_0}\sup_{t\le T}\|Z_n(t)\|_2\).
For completeness, the needed form of Gronwall is: if a nonnegative continuous
function obeys \(D(t)\le a+b\int_0^tD(s)ds\), then
\(D(t)\le ae^{bt}\); it follows by differentiating the right side and multiplying
by \(e^{-bt}\). Equations (26) and the output estimate prove

\[
\sup_{t\le T}\|f_n(t)-f_\infty(t)\|_2
 =O_{\mathbb P}(n^{-1/2}).
\tag{27}
\]

At initialization the finite tangent kernel is the empirical feature Gram.
Its entries are bounded independent sample means with mean
\(K_\infty(0)=\gamma I_2\), so
\(\|K_n(0)-\gamma I_2\|_{\rm op}=O_{\mathbb P}(n^{-1/2})\).
The frozen solution is \(g_n(t)=y-e^{-K_n(0)t/2}y\). Duhamel's formula for
the two positive-semidefinite matrix exponentials bounds their difference
by \((t/2)\|K_n(0)-\gamma I_2\|_{\rm op}\). Therefore

\[
\sup_{t\le T}\|g_n(t)-g_\infty(t)\|_2
 =O_{\mathbb P}(n^{-1/2}).
\tag{28}
\]

Combining (23), (27), and (28), with
\(c_T=\kappa y_0^3T^3e^{-2T}/24>0\), gives

\[
\mathbb P\big(f_{n,1}(T)-g_{n,1}(T)\ge c_T/2\big)\longrightarrow1.
\tag{29}
\]

If \(\widetilde f_n\) is an independent dense run, (27) and the triangle
inequality give

\[
\sup_{t\le T}\|f_n(t)-\widetilde f_n(t)\|_2
 =O_{\mathbb P}(n^{-1/2}).
\tag{30}
\]

Thus on this compact-time training-panel norm the frozen-NTK error divided
by independent-dense variability tends to infinity in probability. For any
fixed finite threshold, this follows by (29), while (30) makes the denominator
converge to zero. A zero denominator does not make an accuracy claim true.
No lower bound on the denominator is required to prove failure of relative
accuracy.

## 5. Exact scope and remaining gaps

1. Equations (9), (15), and (16) prove an actual fixed-physical-time, high-probability
   failure of absolute convergence for order-two and order-three NTH in the
   canonical two-hidden-layer trained tanh network. The initialization and
   small-label choices fit the supplied chapter setup after the stated factor-two
   loss-clock conversion. This is stronger than a derivative mismatch.
2. Equations (27)–(30) additionally prove a shrinking dense-variability comparison
   for the separate one-hidden-layer model on a compact physical-time interval
   and its two training points. They do not establish a complete-time or
   whole-sphere statement.
3. To turn the two-hidden-layer result into a relative lower bound in the
   chapter's complete-trajectory norm, one still needs a justified statement
   that its independent dense-run denominator tends to zero in that same norm.
   Compact-time concentration for a different depth or a smaller query set does
   not supply this. A proved denominator result with the exact deep setup would
   combine immediately with (16).
4. This candidate concerns fixed truncation orders two and three. It proves
   neither an all-fixed-order impossibility theorem nor a bound on how quickly
   the order must grow. It does not compare optimized compilers that retain other
   information, and it makes no discrete-GD claim.
5. The only randomness in the two-hidden-layer lower-bound proof is initialization.
   It uses no numerical experiments, imported random-matrix asymptotics,
   unproved mean-field limit for deep training, or exchange of width with a
   derivative limit. Finite-width dynamical inequalities hold before taking the
   high-probability initialization limit.
