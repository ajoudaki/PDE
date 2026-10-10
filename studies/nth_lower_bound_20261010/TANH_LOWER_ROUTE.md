# General-data tanh obstruction at frozen orders two and three

This is a scoped, theory-only author derivation. It is not an independent
review or established material. Scientific inputs were the supervisor's
assignment, the maintained notation contract, the complete setup and fitting
passage of `docs/08b-trajectory-compression.qmd`, and the two same-study notes
`NONLINEAR_ROUTE.md` and `STRONG_NONLINEAR_SEARCH.md`. No other study,
experiment, or external scientific source was used. The canonical-notation,
rigorous-mathematics, and conjecture-investigation instructions were applied.
The quantitative Gaussian Poincare improvement below was supplied by the
supervisor and checked here. The supervisor also checked the completed
lower-bound equations; this is an internal check, not independent review
or promotion. A subsequent authorized synthesis update uses Section 4
of the same-study TANH_UPPER_ROUTE.md and the explicit event calculation
in TANH_CHECK.md for the all-time conclusion.

The proved candidate is a general-correlated-data prediction lower bound for
frozen-top orders two and three. It does not establish a growing-order lower
bound, convergence failure for all orders, or any storage lower bound growing
with width. Those stronger questions remain open in this route.

## Model and statement

Let \(v_1,\ldots,v_m\in\mathbb R^d\) have unit norm, with fixed \(m\ge2\).
The two-hidden-layer network is

\[
h_a^{(1)}=\tanh(W^{(1)}v_a),\qquad
z_a^{(2)}=W^{(2)}h_a^{(1)},\qquad
h_a=\tanh z_a^{(2)},\qquad f_a=u^\top h_a/n.
\]

The independent initialization is \(W^{(1)}_{ij}\sim N(0,1)\),
\(W^{(2)}_{ij}\sim N(0,1/n)\), and \(u=0\). The mobility blocks are
\((n,1,n)\), and the loss is \(\mathcal L=\|f-y\|_2^2/(2m)\).
Thus physical time here is twice the time in the maintained full-MSE
equations. Write \(Y=\|y\|_2/\sqrt m\), and assume \(0<Y\le1\).
The population initialized feature covariances are

\[
Q^{(1)}_{ab}=\mathbb E[\tanh Z_a\tanh Z_b],
\quad Z\sim N(0,(v_a^\top v_b)_{ab}),
\qquad
Q^{(2)}_{ab}=\mathbb E[\tanh Z_a\tanh Z_b],
\quad Z\sim N(0,Q^{(1)}).
\]

Assume \(\gamma=\lambda_{\min}(Q^{(2)})>0\). No condition on the rank,
orthogonality, or signs of the input Gram is added.

Let \(g\) be the frozen order-two NTH prediction initialized at zero:

\[
\dot g=-K(0)(g-y)/m,\qquad
K_{ab}=\nabla f_a^\top M\nabla f_b,
\]

where \(M\) is the stated parameter mobility. Successive tensors use the
actual metric derivative

\[
K^{(j+1)}_{a_1\cdots a_jb}
=\nabla K^{(j)}_{a_1\cdots a_j}^\top M\nabla f_b.
\]

There are explicit \(T>0\) and \(a=\gamma^2/(32m^2)>0\), independent of
width and of the label direction, such that with probability tending to one,
simultaneously for \(0<t\le T\),

\[
\frac1m y^\top(f(t)-g(t))\ge\frac a{12}Y^4t^3,
\qquad
\max_{a\le m}|f_a(t)-g_a(t)|\ge\frac a{12}Y^3t^3. \tag{1}
\]

The same assertions hold for frozen-top order three. This is an error at
the same physical time in the two systems. No shared auxiliary clock is
used. A finite panel containing the training inputs, or the complete input
sphere, inherits this lower bound.

For a simpler bound, set \(\lambda=\gamma/m\), which is at most one, and
\(T_0=\lambda^2/10^5\). This time is below the \(T\) specified in the
proof. Consequently for either promised query domain,

\[
\|f-g\|_{\mathcal X}
\ge\frac{Y^3\lambda^8}{384\cdot10^{15}},\qquad
\|f-g\|_{\mathcal X}
=\sup_{t\in[0,\infty]}\sup_{v\in\mathcal X}|f(t,v)-g(t,v)|. \tag{1a}
\]

Here \(\mathcal X\) is the unit sphere in the normalized input \(v\), or
the specified finite panel containing the training inputs. The original
network input is \(x=\sqrt d\,v\). Under \(0<Y\le\lambda/64\), the fitted
endpoint exists on the explicit event used for the all-time comparison
below. Without that condition, the early-time maximum already has the
lower bound in (1a).

## A quantitative fourth-order source contraction

For hidden increments \(V=(V^{(1)},V^{(2)})\), use the metric

\[
\|V\|_{\rm hid}^2=\|V^{(1)}\|_F^2/n+\|V^{(2)}\|_F^2.
\]

Let \(J_a=D_wh_a\), where \(w=(W^{(1)},W^{(2)})\), and define its adjoint
by \(\langle J_a^*b,V\rangle_{\rm hid}=b^\top J_a[V]/n\). For a fixed
coefficient vector \(c\in\mathbb R^m\), put

\[
H_c=\frac1m\sum_a c_ah_a,\qquad J_c=\frac1m\sum_a c_aJ_a.
\]

Direct differentiation, with \(p_a^{(\ell)}=\operatorname{sech}^2
z_a^{(\ell)}\), gives

\[
\begin{aligned}
(J_a^*b)^{(1)}
 &= [p_a^{(1)}\odot W^{(2)\top}(b\odot p_a^{(2)})]v_a^\top,\\
(J_a^*b)^{(2)}&=(b\odot p_a^{(2)})h_a^{(1)\top}/n.
\end{aligned} \tag{2}
\]

In particular the exact physical flow and kernel are

\[
\dot u=H_y-H_f,\quad \dot w=J_y^*u-J_f^*u,
\qquad
K_{ab}=h_a^\top h_b/n+\langle J_a^*u,J_b^*u\rangle_{\rm hid}. \tag{3}
\]

Put \(A=J_y^*H_y\), and let \(A^{(2)}\) be its second hidden block.
Write \(c_a=y_a/(mY)\), so \(\sum_a|c_a|\le1\) and
\(\sum_ac_a^2=1/m\). At initialization define the first-layer empirical
Gram \(C_n=(h_a^{(1)\top}h_b^{(1)}/n)_{ab}\). Then

\[
\frac{\|A^{(2)}(0)\|_F^2}{Y^4}
=\frac1n\sum_{i=1}^n H(Z_i)^2 d(Z_i)^\top C_n d(Z_i),
\quad H(z)=\sum_a c_a\tanh z_a,
\quad d_a(z)=c_a\operatorname{sech}^2z_a, \tag{4}
\]

where conditional on the first layer, the \(Z_i\in\mathbb R^m\) are
independent \(N(0,C_n)\). Every summand is bounded by one. The first-layer
law of large numbers gives \(C_n\to Q^{(1)}\) in probability. Conditional
Chebyshev and continuity of the Gaussian covariance square root therefore
give convergence of (4) to

\[
\mathbb E[H(Z)^2 d(Z)^\top Q^{(1)}d(Z)],\qquad Z\sim N(0,Q^{(1)}).
\]

This limit has the explicit lower bound

\[
\mathbb E[H^2d^\top Q^{(1)}d]
\ge\frac14\mathbb EH^4
\ge\frac14(\mathbb EH^2)^2
\ge\frac{\gamma^2}{4m^2}=:a_0. \tag{5}
\]

Here is a justification valid also for singular \(Q^{(1)}\). Set
\(Z=Q^{(1)1/2}G\) for a standard Gaussian \(G\in\mathbb R^m\). Apply the
Gaussian Poincare inequality to
\(\psi(G)=H(Q^{(1)1/2}G)|H(Q^{(1)1/2}G)|\). This function is odd,
so its mean is zero, and its squared gradient is
\(4H^2d^\top Q^{(1)}d\). For completeness, the required Poincare
inequality follows by differentiating

\[
C(s)=\mathbb E[\psi(G)\psi(sG+\sqrt{1-s^2}G')],\qquad 0<s<1,
\]

with \(G'\) independent standard Gaussian. Gaussian integration by parts
gives \(C'(s)=\mathbb E[\nabla\psi(G)^\top
\nabla\psi(sG+\sqrt{1-s^2}G')]\). Cauchy--Schwarz bounds this by
\(\mathbb E\|\nabla\psi(G)\|_2^2\). Integration from zero to one proves
the inequality. Smooth approximation justifies the calculation for the
bounded \(C^1\) function used here. Finally
\(\mathbb EH^2=c^\top Q^{(2)}c\ge\gamma/m\), proving (5).

Consequently the event

\[
\mathcal E_n=\{\|W^{(2)}(0)\|_{\rm op}\le8,
                  \|A^{(2)}(0)\|_F^2\ge(a_0/2)Y^4\} \tag{6}
\]

has probability tending to one. The operator assertion follows directly
from two \(1/4\)-nets of cardinality at most \(9^n\), the estimate
\(\|W\|_{\rm op}\le2\max_{p,q\text{ in nets}}|p^\top Wq|\), and
the Gaussian tail bound: its failure probability is at most
\(2\exp((2\log9-8)n)\).

The width threshold can be made explicit. For \(Q\succeq0\) with entries
bounded by one, let

\[
F(Q,z)=H(z)^2d(z)^\top Qd(z),\qquad
\mu(Q)=\mathbb E F(Q,Z),\quad Z\sim N(0,Q).
\]

Then \(0\le F\le1\), and

\[
|\mu(Q)-\mu(Q')|\le22\max_{ab}|Q_{ab}-Q'_{ab}|. \tag{6a}
\]

To verify the constant, \(\sum|c_a|\le1\) gives

\[
\sum_i|\partial_iH|\le1,\quad
\sum_{ij}|\partial_{ij}H|\le2.
\]

For \(D=d^\top Qd\), the bounds
\(|d_i'|\le2|c_i|\), \(|d_i''|\le6|c_i|\) give
\(\sum_i|\partial_iD|\le4\) and
\(\sum_{ij}|\partial_{ij}D|\le20\). Consequently
\(\sum_{ij}|\partial_{ij}(H^2D)|\le6+16+20=42\).
The direct change of \(Q\) in \(D\) costs at most
\(\max|Q-Q'|\). Gaussian covariance interpolation, whose derivative is
\(\frac12\sum_{ij}(Q-Q')_{ij}\mathbb E\partial_{ij}F\), costs at
most \(21\max|Q-Q'|\). Gaussian integration by parts proves that
derivative formula; adding \(\varepsilon I\) and taking
\(\varepsilon\downarrow0\) justifies singular covariance endpoints by
bounded convergence. This proves (6a).

Take \(\varepsilon=a_0/88\). The first-layer empirical Gram has

\[
\mathbb P(\max_{ab}|(C_n-Q^{(1)})_{ab}|>\varepsilon)
\le2m^2e^{-n\varepsilon^2/2},
\]

by Hoeffding's bound for independent variables in \([-1,1]\).
On its complement, (5) and (6a) give \(\mu(C_n)\ge3a_0/4\).
Conditional Hoeffding for the independent \([0,1]\)-valued summands
in (4), at deviation \(a_0/4\), then yields

\[
\mathbb P(\mathcal E_n^c)
\le2e^{-(8-2\log9)n}
 +2m^2e^{-na_0^2/15488}+e^{-na_0^2/8}. \tag{6b}
\]

The concentration bound used here follows directly from a moment bound:
for a variable in an interval of length \(b\), the second derivative of
its log moment generating function is its variance under exponential
tilting, at most \(b^2/4\). Integrating twice gives
\(\mathbb E e^{s(U-\mathbb EU)}\le e^{s^2b^2/8}\).
Independence and optimization in \(s\) give the two-sided bound with
\(b=2\) and the one-sided conditional bound with \(b=1\).

Thus \(n\ge C(m/\gamma)^4\log(m/\delta)\), for an absolute finite
\(C\) and \(0<\delta<1\), suffices for confidence \(1-\delta\) in (1).
The early-time theorem therefore has a quantitative width condition.
The same-study all-time bootstrap and the joint event calculation in
TANH_CHECK.md also give a quantitative width for the all-time comparison
below; no unspecified fitting width is needed.

The source scalar \(F=y^\top f/m=u^\top H_y/n\), evolved under the
constant unit source \(\theta'=M\nabla F\), satisfies at \(u=0\)

\[
F'''(0)=4\|J_y^*H_y\|_{\rm hid}^2
=\frac1{m^4}\sum_{a,b,c,d}y_ay_by_cy_dK^{(4)}_{abcd}(0). \tag{7}
\]

To check the factor four, \(u'=H_y\), \(w'=0\), \(u''=0\), and
\(w''=A\). The third derivative of \(u^\top H_y/n\) contains one
term \(u'''{}^\top H_y/n=\|A\|_{\rm hid}^2\) and three terms
\(u'{}^\top J_yw''/n=\|A\|_{\rm hid}^2\). Formula (5) bounds a
genuine deep-network contraction; it does not posit componentwise tensor
positivity.

## From the initial contraction to a width-uniform prediction gap

All following estimates are deterministic on (6). Put

\[
M_0=9,\quad B=\sqrt{82},\quad D=B^2/2,\quad
E=1/2+B^2/3,\quad C_A=3D+M_0/2,
\quad C_E=2B^2(E+1),\quad C_K=2B^2.
\]

Loss decay gives \(\|f-y\|_2\le\sqrt mY\). Using bounded tanh and
its first derivative, for \(0\le t\le1\),

\[
\begin{gathered}
\|u(t)\|_\infty\le Yt,\quad
\|\dot W^{(2)}(t)\|_F\le Y^2t,\quad
\|W^{(2)}(t)\|_{\rm op}\le M_0,\\
\|J_a[V]\|_2/\sqrt n\le B\|V\|_{\rm hid},\quad
\|\dot w\|_{\rm hid}\le BY^2t,\quad
\|\dot W^{(1)}\|_F/\sqrt n\le M_0Y^2t,\\
\|h_a(t)-h_a(0)\|_2/\sqrt n\le DY^2t^2,\quad
\|z_a^{(2)}(t)-z_a^{(2)}(0)\|_2/\sqrt n\le DY^2t^2,\\
\|h_a^{(1)}(t)-h_a^{(1)}(0)\|_2/\sqrt n
\le(M_0/2)Y^2t^2.
\end{gathered} \tag{8}
\]

For the operator estimate on \(J_a\), differentiate the forward pass and
bound its two hidden-block contributions by
\(\|V^{(2)}\|_F+M_0\|V^{(1)}\|_F/\sqrt n\); Cauchy--Schwarz gives
\(B\). Integration gives the feature bounds. For the second preactivation
subtract its two matrix products and use
\(1+8M_0\le B^2\). These bounds also ensure finite-width existence up
to time one: every parameter increment is finite there, so the smooth
ordinary differential equation can be continued.

The map \(z\mapsto\operatorname{sech}^2z\) is 2-Lipschitz on the real
line. Subtracting the three factors in the second block of (2), and using
\(\|H_y\|_\infty\le Y\), gives

\[
\|A^{(2)}(t)-A^{(2)}(0)\|_F\le C_A Y^4t^2. \tag{9}
\]

More explicitly the changes of \(H_y\), \(p_a^{(2)}\), and
\(h_a^{(1)}\) contribute respectively \(D\), \(2D\), and \(M_0/2\)
times \(Y^4t^2\). Let

\[
T_A=\min\left\{1,
 \left(\frac{\sqrt{a_0/2}}{2C_A}\right)^{1/2}\right\},\qquad
a=a_0/8=\frac{\gamma^2}{32m^2}.
\]

Equations (6) and (9), with \(Y\le1\), imply
\(\|A(t)\|_{\rm hid}^2\ge aY^4\) for \(t\le T_A\).

Next, integrating the first equation in (3), and using (8), gives

\[
\|u(t)-tH_y(t)\|_2/\sqrt n
\le B^2Y^3t^3/3+Yt^2/2
=E_{\rm eff}(t)Yt^2\le EYt^2,\qquad
E_{\rm eff}(t)=\frac12+\frac{B^2}{3}Y^2t. \tag{10}
\]

Indeed the two contributions are
\(\int_0^t\|H_y(s)-H_y(t)\|_2/\sqrt n\,ds\) and
\(\int_0^t\|H_f(s)\|_2/\sqrt n\,ds\), respectively. For the first,
\(\|\dot H_y(u)\|_2/\sqrt n\le B^2Y^3u\), so reversing the order of
integration gives the factor \(1/3\):

\[
\int_0^t\int_s^t B^2Y^3u\,du\,ds
=B^2Y^3\int_0^t u^2\,du
=B^2Y^3t^3/3.
\]

Also
\(\|A\|_{\rm hid}\le BY^2\),
\(\|J_y[V]\|_2/\sqrt n\le BY\|V\|_{\rm hid}\), and
\(\|J_f[V]\|_2/\sqrt n\le BYt\|V\|_{\rm hid}\).
Differentiating the label-feature energy in (3) and applying (10) therefore
yields

\[
\frac d{dt}\frac{\|H_y(t)\|_2^2}{n}
\ge2t\|A(t)\|_{\rm hid}^2
 -2B^2(E_{\rm eff}(t)+1)Y^4t^2
\ge2t\|A(t)\|_{\rm hid}^2-C_EY^4t^2.
\]

The uniform constant is \(C_E=14186/3\). A sharper short-time bound
uses \(Y\le1\): for \(t\le3/(2B^2)\), one has
\(E_{\rm eff}(t)\le1\), so the error coefficient is at most \(4B^2\).
Therefore, for \(t\le\min(T_A,3/(2B^2),a/(4B^2))\), integration and
the nonnegative hidden kernel contribution give

\[
y^\top[K(t)-K(0)]y\ge\frac{m^2a}{2}Y^4t^2. \tag{11}
\]

There is also the uniform operator upper bound

\[
\|K(t)-K(0)\|_{\rm op}\le mC_KY^2t^2, \tag{12}
\]

because each changed readout-Gram entry is at most \(B^2Y^2t^2\),
as is each hidden-Gram entry. The exact error \(e=f-g\) satisfies

\[
e(t)=\frac1m\int_0^t e^{-K(0)(t-s)/m}
                [K(s)-K(0)](y-f(s))\,ds. \tag{13}
\]

Since \(K(0)\succeq0\) and \(\|K(0)\|_{\rm op}\le m\), the
exponential is a contraction and its distance to identity is at most
\(t-s\). With \(\|f(s)\|_2\le\sqrt mYs\), (12) bounds the
difference between the scalar integrand \(y^\top e^{-K(0)(t-s)/m}
[K(s)-K(0)](y-f(s))\) and \(y^\top[K(s)-K(0)]y\) by

\[
m^2 C_KY^4ts^2.
\]

Set

\[
T=\min\{T_A,3/(2B^2),a/(4B^2),a/(4C_K)\}>0.
\]

To check the simpler choice in (1a), \(32(4B^2)<10^5\),
\(32(4C_K)<10^5\), and \(3/(2B^2)>10^{-5}\). Moreover
\(T_A=\min\{1,\sqrt{\lambda/(510\sqrt2)}\}\), which exceeds
\(\lambda^2/10^5\) for \(0<\lambda\le1\). Thus \(T_0\le T\).

Substitution of (11) into (13), followed by integration of \(s^2\),
proves the first inequality of (1). The second follows from
\(\|y\|_1\le mY\).

At initialization \(K^{(3)}=0\) exactly: the readout Gram has zero
readout derivative, the hidden Gram is quadratic in \(u\), and every
hidden component of \(M\nabla f_b\) vanishes at \(u=0\). Freezing
the third tensor therefore freezes the second tensor too. The order-three
prediction is exactly \(g\), proving its asserted lower bound.

## The requested whole-trajectory comparison and the remaining gap

Impose now \(0<Y\le\lambda/64\), where \(\lambda=\gamma/m\). This includes
the maintained chapter's label range. Section 4 of the same-study
TANH_UPPER_ROUTE.md proves directly, under the initialization event
\(\|W^{(2)}(0)\|_{\rm op}\le8\) and \(K(0)\succeq\gamma I_m/2\), that
the flow is global, converges in parameters, fits the labels, and satisfies

\[
\sup_{t\ge0}\|u(t)\|_2/\sqrt n\le2Y\sqrt{m/\gamma}.
\]

Its proof uses the actual half-MSE flow. The readout bound follows from
the finite parameter length
\(\int_0^\infty\|\dot\theta\|_{\rm par}\,dt\le2Y/\sqrt\lambda\).
The explicit event calculation in TANH_CHECK.md combines that event with
(6). For any \(0<\delta<1\),

\[
n\ge247808\,\lambda^{-4}\log\frac{20m^2}{\delta} \tag{13a}
\]

suffices for the combined event for the coupled dense/frozen pair and
the fitting event for one independent dense run with total confidence
at least \(1-\delta\). Indeed apply the checked joint width bound with
failure allowance \(\delta/2\) to the coupled pair and its weaker fitting
part with allowance \(\delta/2\) to the independent run, then take a union
bound. The fixed-order frozen model also converges and fits on this event.

Since tanh features have RMS at most one, two independent dense runs satisfy

\[
\|f_n-\widetilde f_n\|_{\mathcal X}
\le4Y\sqrt{m/\gamma}
\]

for either promised query domain on this explicit event. Combined
with (1) at the fixed time \(T\), this gives

\[
\frac{\|g-f_n\|_{\mathcal X}}
     {\|f_n-\widetilde f_n\|_{\mathcal X}}
\ge\frac a{48}Y^2T^3\sqrt{\gamma/m}>0 \tag{14}
\]

with confidence at least \(1-\delta\) under (13a). A zero denominator is a failure by
the original contract; the positive numerator does not disappear. Thus
orders two and three cannot have vanishing relative error in the exact
requested whole-trajectory norm. If an independent result supplies a
dense-pair \(O_{\mathbb P}(n^{-1/2})\) bound in that norm, the same fixed
numerator implies a divergent ratio; that rate is not proved here.

The route does not establish the requested high-order complexity law. The
positive quartic contraction says nothing about signs or sizes of later
omitted contractions. A separate mechanistic check conditions on the
initialized first-layer feature matrix \(X=[h_a^{(1)}]_{a=1}^m\) and all
second-layer preactivations \(Z=W^{(2)}X\). If \(P_X\) is the orthogonal
projection onto the column space of \(X\), the exact conditional law is

\[
W^{(2)}=ZX^+ +R(I-P_X),
\]

where \(X^+\) is the Moore--Penrose pseudoinverse and \(R_{ij}\) are
independent \(N(0,1/n)\), independent of the conditioned quantities.
For \(B_a=(y_a/m)(H_y\odot\operatorname{sech}^2Z_a)\), the random
part of the initial first-layer source acceleration contains

\[
g_a=(I-P_X)R^\top B_a,\qquad
\mathbb E[g_ag_b^\top\mid X,Z]
=\frac{B_a^\top B_b}{n}(I-P_X).
\]

Thus conditional Gaussian moments of order \(2k\) contain factors
\((2k-1)!!\) even for bounded tanh features. This identifies a possible
high-order mechanism. It is not a lower bound for the complete tensor:
other terms of that tensor can cancel a selected diagonal contribution,
and matrix contractions have substantially different moment growth.
Even a complete high-order coefficient bound would still need to control
the omitted sum at the chosen finite orders and the surrogate's own
residual-driven evolution at the same physical time. Those are the
unresolved steps. No assertion that every fixed order fails
asymptotically, or that \(q\gtrsim\log n\), follows from this route.

No claimed uniform complex source neighborhood, shrinking individual pole
radius, or formal high-order jet is substituted for those missing bounds.
The strongest established candidate here is (1)--(14).
