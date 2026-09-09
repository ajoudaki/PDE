# Exact paired-step route and its first all-source obstruction

## 1. Claim status

For the already identified width-first population Euler dynamics of the
two-hidden-layer model, the coarse/fine discrepancy has the exact
factorization

\[
\Delta_t(h)=h^2\sum_{j=1}^t A_{j,t}(h).                 \tag{1.1}
\]

This identity is proved below before taking any absolute value. It gives
the desired power \(t^4h^5\) as soon as each transported local defect has
a third \(h\)-derivative bounded by \(C_A t^3\). The implication,
including the factor \(1/6\), is also proved below.

The remaining network theorem is **OPEN**. More precisely, Section 7
proves that a norm with a single scalar weight \(w_m\) cannot make both
the source shift and Leibniz multiplication bounded on the complete
derivative-jet algebra. Thus a generic all-source Banach-algebra proof
cannot be obtained by tuning a scalar sequence \(w_m\). This no-go result
does not by itself exclude a smaller class consisting only of actual
reachable OMFP histories. Closing that smaller class is the precise
unproved problem. A proof would have to exploit reachability, use
genuinely history- or tree-dependent weights, or estimate the composite
adjoint/product operation without splitting it into two ambient bounded
operators.

Nothing in this note uses finite-width Taylor expansion, finite-\(t\)
continuity in the activation amplitude, or separate estimates on the two
terminal outputs.

## 2. Population Euler notation

Let \(\mathcal X_{\mathrm{reach}}\) denote the generated population state
of the established \(q=1,L=2\) OMFP DAG, let

\[
E_h(\theta)=\theta+h g(\theta)                       \tag{2.1}
\]

be one simultaneous recomputed gradient-ascent step, and let
\(\mathcal O\) be the population output observable. Expectations over
the fixed Gaussian source space are included in \(\mathcal O\). Thus

\[
F_N(h)=\mathcal O(E_h^N\theta_0).                    \tag{2.2}
\]

For the algebra below it is enough that the directional derivatives
appearing along the finitely generated curves exist. This is already
known at each fixed finite horizon. No ambient Fréchet differentiability
on an \(L^2\) ball is used.

Put

\[
B_h=E_h\circ E_h,\qquad C_h=E_{2h}.                 \tag{2.3}
\]

Then

\[
\Delta_t(h)=F_{2t}(h)-F_t(2h)
=\mathcal O(B_h^t\theta_0)-\mathcal O(C_h^t\theta_0).
                                                               \tag{2.4}
\]

## 3. Exact local and global factorizations

### Lemma 3.1 (one paired step)

For every reachable state \(x\),

\[
B_hx-C_hx=h^2a_h(x),                                \tag{3.1}
\]

where

\[
a_h(x)=\int_0^1
Dg\bigl(x+s h g(x)\bigr)[g(x)]\,ds.                \tag{3.2}
\]

**Proof.** Directly from (2.1),

\[
\begin{aligned}
B_hx-C_hx
&=h\{g(x+h g(x))-g(x)\}\\
&=h^2\int_0^1Dg(x+s h g(x))[g(x)]\,ds,
\end{aligned}
\]

where the second equality is the fundamental theorem of calculus along
the displayed line segment. This proves (3.1). Notice that the identity
holds for positive and negative \(h\). \(\square\)

### Lemma 3.2 (hybrid telescope)

For \(1\le j\le t\), set

\[
y_j=B_h^{j-1}\theta_0,\qquad m_j=t-j,               \tag{3.3}
\]

\[
c_j=C_hy_j,\qquad b_j=B_hy_j
      =c_j+h^2a_h(y_j),                             \tag{3.4}
\]

and define

\[
A_{j,t}(h)=\int_0^1
D(\mathcal O\circ C_h^{m_j})
\bigl(c_j+\lambda h^2a_h(y_j)\bigr)
[a_h(y_j)]\,d\lambda.                              \tag{3.5}
\]

Then the exact identity (1.1) holds.

**Proof.** Define the \(t+1\) hybrid outputs

\[
H_j=\mathcal O\bigl(C_h^{t-j}B_h^j\theta_0\bigr),
\qquad 0\le j\le t.                                \tag{3.6}
\]

They satisfy \(H_0=F_t(2h)\) and \(H_t=F_{2t}(h)\). With \(y_j\) from
(3.3),

\[
H_j-H_{j-1}
=(\mathcal O\circ C_h^{m_j})(b_j)
 -(\mathcal O\circ C_h^{m_j})(c_j).                \tag{3.7}
\]

Apply the fundamental theorem of calculus on the single segment from
\(c_j\) to \(b_j=c_j+h^2a_h(y_j)\). Equations (3.5) and (3.7) give

\[
H_j-H_{j-1}=h^2A_{j,t}(h).                         \tag{3.8}
\]

Summing (3.8) from \(j=1\) to \(t\) proves

\[
\Delta_t(h)=H_t-H_0=h^2\sum_{j=1}^tA_{j,t}(h).
\]

No triangle inequality has been used. \(\square\)

### Tangent form of \(A_{j,t}\)

The form needed for stability estimates is completely explicit. For
\(0\le\lambda\le1\), initialize

\[
z_{j,0}=c_j+\lambda h^2a_h(y_j),\qquad
v_{j,0}=a_h(y_j),                                  \tag{3.9}
\]

and, for \(0\le r<m_j\), recurse

\[
z_{j,r+1}=C_hz_{j,r}=z_{j,r}+2h g(z_{j,r}),         \tag{3.10}
\]

\[
v_{j,r+1}
=(I+2hDg(z_{j,r}))v_{j,r}.                         \tag{3.11}
\]

Thus, with the coarse tangent propagator

\[
P_{j,t}(h,\lambda)
=\prod_{r=m_j-1}^{0}\bigl(I+2hDg(z_{j,r})\bigr),   \tag{3.12}
\]

where the rightmost factor acts first,

\[
v_{j,m_j}=P_{j,t}(h,\lambda)a_h(y_j),              \tag{3.13}
\]

and

\[
A_{j,t}(h)=\int_0^1
D\mathcal O(z_{j,m_j})[v_{j,m_j}]\,d\lambda.       \tag{3.14}
\]

Equations (3.9)--(3.14) are identities, not bounds.

## 4. Parity, the cubic coefficient, and the exact remainder reduction

The established Gaussian sign involution of this OMFP DAG gives

\[
F_N(-h)=-F_N(h).                                    \tag{4.1}
\]

Consequently \(\Delta_t\) is odd. Put

\[
S_t(h)=\sum_{j=1}^tA_{j,t}(h).                     \tag{4.2}
\]

If the generated curves in (3.5) are \(C^3\) in \(h\), then (1.1)
implies that \(S_t\) is odd on the punctured interval, and continuity
extends this identity to zero. Hence

\[
S_t(0)=S_t''(0)=0.                                 \tag{4.3}
\]

Define

\[
\kappa_t=S_t'(0)
=\frac{F_{2t}^{(3)}(0)-8F_t^{(3)}(0)}{6}.          \tag{4.4}
\]

The already proved cubic OMFP recursion makes (4.4) an explicit Gaussian
activation integral. In the notation of that recursion,

\[
\kappa_t=\frac{t(2t-1)}2J_{\psi,2},                \tag{4.5}
\]

where \(J_{\psi,2}=\mathsf S_{\psi,2}+4\mathsf H_{\psi,2}\), and
\(\mathsf S_{\psi,2},\mathsf H_{\psi,2}\) are the terminating
nine-moment Gaussian recursion. The sign in (4.5) is positive because
the present discrepancy is fine minus coarse; the previously used
coarse-minus-fine discrepancy has the opposite sign.

Taylor's formula with integral remainder, applied to \(S_t\), gives for
positive or negative \(h\)

\[
S_t(h)-\kappa_th
=\frac12\int_0^h(h-u)^2S_t'''(u)\,du.             \tag{4.6}
\]

Combining (1.1) and (4.6),

\[
\left|\Delta_t(h)-\kappa_th^3\right|
\le \frac{|h|^5}{6}
\sup_{|u|\le|h|}|S_t'''(u)|.                      \tag{4.7}
\]

In particular, the single estimate

\[
\sup_{\substack{1\le j\le t\\ |u|\le\rho/t}}
|A_{j,t}'''(u)|\le C_A t^3                         \tag{4.8}
\]

implies, with no further loss,

\[
\left|\Delta_t(h)-\kappa_th^3\right|
\le \frac{C_A}{6}t^4|h|^5,
\qquad |h|\le\rho/t.                               \tag{4.9}
\]

The factor \(t^4\) consists of exactly one factor \(t\) from the hybrid
sum and three factors from differentiating a transported local defect.
The numerical factor \(1/6\) is the mass of the third-order Taylor kernel.

## 5. What propagator estimates suffice

This section proves the internal numerical-analysis implication on a
reachable normed core. It deliberately does not assume an ambient
Banach-space ball.

Assume that, on every state and direction generated by (3.3)--(3.11), a
norm \(\|\cdot\|_{\mathfrak X}\) satisfies the restricted estimates

\[
\|D^qg(z)[u_1,\ldots,u_q]\|_{\mathfrak X}
\le K_q\prod_{i=1}^q\|u_i\|_{\mathfrak X},
\qquad 0\le q\le4,                                 \tag{5.1}
\]

where \(D^0g=g\), and

\[
|D^q\mathcal O(z)[u_1,\ldots,u_q]|
\le L_q\prod_{i=1}^q\|u_i\|_{\mathfrak X},
\qquad 1\le q\le4.                                 \tag{5.2}
\]

These inequalities are required only for the displayed reachable
directions. Suppose all paths remain in the core on \(|h|t\le\rho\).
The constants below are then finite terminating formulas in
\(\rho,K_0,\ldots,K_4,L_1,\ldots,L_4\).

### 5.1 State and local-defect jets

Every Euler string occurring in (3.3)--(3.11), including the auxiliary
point \(x+s h g(x)\), has total absolute Euler coefficient at most \(4t\).
Put

\[
H=\exp(4K_1\rho),                                  \tag{5.3}
\]

and define successively

\[
X_1=4HK_0,                                         \tag{5.4}
\]

\[
X_2=4H\{2K_1X_1+\rho K_2X_1^2\},                 \tag{5.5}
\]

\[
X_3=4H\{3(K_2X_1^2+K_1X_2)
+\rho(K_3X_1^3+3K_2X_1X_2)\}.                    \tag{5.6}
\]

Direct differentiation of \(x_+=x+a h g(x)\) gives

\[
x_+'=(I+a hDg)x'+a g,                              \tag{5.7}
\]

\[
x_+''=(I+a hDg)x''+2aDg[x']+a hD^2g[x',x'],       \tag{5.8}
\]

\[
\begin{aligned}
x_+'''=(I+a hDg)x'''
&+3a\{D^2g[x',x']+Dg[x'']\}\\
&+a h\{D^3g[x',x',x']+3D^2g[x',x'']\}.
\end{aligned}                                      \tag{5.9}
\]

The homogeneous products are bounded by

\[
\prod(1+|a h|K_1)
\le \exp(K_1|h|\sum|a|)\le H.                     \tag{5.10}
\]

Summing the inhomogeneous terms in increasing derivative order proves

\[
\|\partial_h^rx(h)\|_{\mathfrak X}\le X_rt^r,
\qquad 1\le r\le3.                                 \tag{5.11}
\]

Indeed, after division by \(t^r\), (5.7), (5.8), and (5.9) give exactly
the right sides (5.4), (5.5), and (5.6), respectively. Thus (5.11) is
not an assumed flow estimate.

For later use define

\[
G_0=K_0,\quad G_1=K_1X_1,                          \tag{5.12}
\]

\[
G_2=K_1X_2+K_2X_1^2,\qquad
G_3=K_1X_3+3K_2X_1X_2+K_3X_1^3,                  \tag{5.13}
\]

and

\[
R_0=K_1,\quad R_1=K_2X_1,                         \tag{5.14}
\]

\[
R_2=K_2X_2+K_3X_1^2,\qquad
R_3=K_2X_3+3K_3X_1X_2+K_4X_1^3.                  \tag{5.15}
\]

Faà di Bruno for \(g(x(h))\) gives the \(G_r\); the same formula for
\(Dg(x(h))\) gives the \(R_r\). Leibniz's rule in (3.2) therefore proves

\[
\|\partial_h^ra_h(y_j(h))\|_{\mathfrak X}
\le Q_rt^r,\qquad
Q_r=\sum_{q=0}^r{r\choose q}R_qG_{r-q},
\quad0\le r\le3.                                  \tag{5.16}
\]

All recursions terminate at \(r=3\).

The interpolation perturbation has the exact derivatives

\[
\partial_h^r(h^2a)
=h^2a^{(r)}+2rh a^{(r-1)}+r(r-1)a^{(r-2)},         \tag{5.17}
\]

with negative-index terms interpreted as zero. Hence the terminal
coarse path in (3.9)--(3.10) has bounds

\[
\|\partial_h^rz_{j,m_j}\|_{\mathfrak X}
\le Z_rt^r,\qquad1\le r\le3,                       \tag{5.18}
\]

where one completely explicit choice is obtained as follows. Put

\[
D_r=\rho^2Q_r+2r\rho Q_{r-1}+r(r-1)Q_{r-2},       \tag{5.19}
\]

and successively define

\[
Z_1=H\{X_1+D_1+4K_0\},                            \tag{5.20}
\]

\[
Z_2=H\{X_2+D_2+4(2K_1Z_1+\rho K_2Z_1^2)\},      \tag{5.21}
\]

\[
\begin{aligned}
Z_3=H\{X_3+D_3+4[3(K_2Z_1^2+K_1Z_2)\\
\hspace{37mm}+\rho(K_3Z_1^3+3K_2Z_1Z_2)]\}.
\end{aligned}                                      \tag{5.22}
\]

Equations (5.17), (5.7)--(5.10), restarted at the interpolation point,
prove (5.18). The constants are deliberately enlarged; their only role
is to be explicit and independent of \(j,t\).

### 5.2 One-step tangent estimate and its first three derivatives

For a micro-step the exact tangent is

\[
(I+hDg(z))V,
\]

and (5.1) with \(q=1\) proves, rather than assumes,

\[
\|(I+hDg(z))V\|_{\mathfrak X}
\le(1+K_1|h|)\|V\|_{\mathfrak X}.                 \tag{5.23}
\]

For the coarse step replace \(h\) by \(2h\). Along the coarse path put
\(L(h)=Dg(z(h))\). From (5.18),

\[
\|\partial_h^qL(h)\|_{\mathrm{op},\mathfrak X}
\le \ell_qt^q,\qquad0\le q\le3,                   \tag{5.24}
\]

where

\[
\ell_0=K_1,\quad \ell_1=K_2Z_1,                  \tag{5.25}
\]

\[
\ell_2=K_2Z_2+K_3Z_1^2,\qquad
\ell_3=K_2Z_3+3K_3Z_1Z_2+K_4Z_1^3.              \tag{5.26}
\]

If \(v_+=v+2hL(h)v\), Leibniz's rule gives, for \(0\le r\le3\),

\[
\begin{aligned}
v_+^{(r)}=v^{(r)}
&+2h\sum_{q=0}^r{r\choose q}L^{(q)}v^{(r-q)}\\
&+2r\sum_{q=0}^{r-1}{r-1\choose q}
      L^{(q)}v^{(r-1-q)}.
\end{aligned}                                      \tag{5.27}
\]

The second line is absent for \(r=0\). This is the requested set of
three derivative analogues of (5.23).

For a standalone propagator initialized by the identity, define

\[
C_0=e^{2K_1\rho},                                  \tag{5.28}
\]

and, successively for \(1\le r\le3\),

\[
\begin{aligned}
C_r=e^{2K_1\rho}\bigg[
&2\rho\sum_{q=1}^r{r\choose q}\ell_qC_{r-q}\\
&+2r\sum_{q=0}^{r-1}{r-1\choose q}
      \ell_qC_{r-1-q}\bigg].
\end{aligned}                                      \tag{5.29}
\]

Variation of constants in (5.27), the product bound
\(\prod_{r<m_j}(1+2|h|K_1)\le e^{2K_1\rho}\), and
\(m_j\le t\) prove

\[
\|\partial_h^rP_{j,t}(h,\lambda)\|_{\mathrm{op,reach},\mathfrak X}
\le C_rt^r,\qquad0\le r\le3.                      \tag{5.30}
\]

For clarity, the two sums in (5.29) have different origins. The first
contains the factor \(m_j|h|\le\rho\); after normalization by \(t^r\),
the second contains \(m_j/t\le1\). Thus no hidden horizon factor occurs.

Combining (5.16), (5.30), and Leibniz gives

\[
\|\partial_h^rv_{j,m_j}\|_{\mathfrak X}
\le V_rt^r,\qquad
V_r=\sum_{q=0}^r{r\choose q}C_qQ_{r-q}.           \tag{5.31}
\]

### 5.3 The terminal contraction

Three differentiations of the scalar integrand in (3.14) give exactly

\[
\begin{aligned}
\partial_h^3\{D\mathcal O(z)[v]\}
={}&D^4\mathcal O(z)[z',z',z',v]
+3D^3\mathcal O(z)[z'',z',v]\\
&+3D^3\mathcal O(z)[z',z',v']
+D^2\mathcal O(z)[z''',v]\\
&+3D^2\mathcal O(z)[z'',v']
+3D^2\mathcal O(z)[z',v'']
+D\mathcal O(z)[v'''].
\end{aligned}                                      \tag{5.32}
\]

Therefore (5.2), (5.18), and (5.31) prove (4.8) with

\[
\begin{aligned}
C_A={}&L_4Z_1^3V_0
+3L_3Z_2Z_1V_0+3L_3Z_1^2V_1\\
&+L_2Z_3V_0+3L_2Z_2V_1+3L_2Z_1V_2+L_1V_3.
\end{aligned}                                      \tag{5.33}
\]

Integration over \(\lambda\in[0,1]\) has mass one. This completes the
proof of the abstract internal stability theorem: (5.1)--(5.2) imply
(4.9) with \(C=C_A/6\).

## 6. The exact OMFP inequality still required

For the actual reused-matrix Gaussian dynamics, (5.1) cannot be imported
from an ambient \(L^2\) Fréchet derivative. It must be proved in an
all-source reachable norm. At the first connector, the exact response
identity has the schematic source-jet form

\[
\mathcal D^m(J^*V)
=\mathbb E_J[\mathcal D^{m+1}V].                  \tag{6.1}
\]

Consequently the first required estimate is

\[
\sum_{m\ge0}w_m
\left\|\mathbb E_J[\mathcal D^{m+1}V]\right\|_{p_m}
\le C_J\sum_{m\ge0}w_m
\|\mathcal D^mV\|_{p_m}.                         \tag{6.2}
\]

It must hold on all histories generated by the learned rank-one updates,
and must remain compatible with the Leibniz products needed in (5.1).
No estimate already established for a fixed finite source ledger implies
(6.2) uniformly in the horizon.

## 7. The requested single same-space norm fails

There is an obstruction even before the adjoint source shift is tested.

### Proposition 7.1 (raw-Gaussian product obstruction)

Let

\[
\|V\|_{\mathfrak X}
=\sum_{m\ge0}w_m\|\mathcal D^mV\|_{p_m},
\qquad w_m>0,\quad 1\le p_m\le\infty.              \tag{7.1}
\]

No such single space can both contain a raw Gaussian coordinate \(G\)
and obey a same-space product inequality

\[
\|UV\|_{\mathfrak X}
\le C_\times\|U\|_{\mathfrak X}\|V\|_{\mathfrak X} \tag{7.2}
\]

with finite \(C_\times\).

**Proof.** If \(p_0=\infty\), then the positive zeroth-order term
\(w_0\|G\|_\infty\) is infinite, so \(G\notin\mathfrak X\). Suppose
\(p_0<\infty\) and write \(N_G=\|G\|_{\mathfrak X}<\infty\).
Iteration of (7.2) gives

\[
\|G^n\|_{\mathfrak X}
\le C_\times^{\,n-1}N_G^n.                         \tag{7.3}
\]

On the other hand,

\[
\|G^n\|_{\mathfrak X}
\ge w_0\|G^n\|_{p_0}
=w_0\|G\|_{np_0}^{\,n}.                            \tag{7.4}
\]

There is a numerical \(c_*>0\) such that
\(\|G\|_q\ge c_*\sqrt q\) for every \(q\ge1\). To verify this, integrate
the Gaussian density over
\([\sqrt q,\sqrt q+q^{-1/2}]\); on this interval \(x^2\le q+3\), so

\[
\mathbb P\{\sqrt q\le G\le\sqrt q+q^{-1/2}\}
\ge\frac{e^{-3/2}}{\sqrt{2\pi q}}e^{-q/2}.
\]

Taking the \(q\)-th root gives the claimed bound because the remaining
positive factor has a positive infimum on \(q\ge1\). Consequently
(7.3)--(7.4) imply

\[
w_0^{1/n}c_*\sqrt{np_0}
\le C_\times^{\,1-1/n}N_G,
\]

whose left side diverges and whose right side stays bounded. This is a
contradiction. \(\square\)

The raw Gaussian sources belong to the initialization core, and closure
under products would contain their powers. Thus (7.2) is the first
precise same-space closure inequality that fails. This conclusion is
independent of the aggregation of positive-order source histories.
Taking \(w_0=0\) does not help: constants then have zero norm and terminal
Gaussian expectations are not controlled.

There is also an independent source-order obstruction, even if one
temporarily ignores Proposition 7.1.

### Proposition 7.2 (shift/product incompatibility)

The obstruction can be proved without making any choice of moment
exponents. Deterministic scalar jets have the same norm in every
\(L^{p_m}\), so changing \(p_m\) cannot repair it.

Let \(w_m>0\). Equip ordinary one-variable derivative jets with

\[
\|u\|_w=\sum_{m\ge0}w_m|u_m|,
\qquad u_m=D^mu.                                   \tag{7.5}
\]

There do not exist finite constants \(C_J,C_P\) such that both

\[
\|Su\|_w\le C_J\|u\|_w,
\qquad (Su)_m=u_{m+1},                             \tag{7.6}
\]

and

\[
\|uv\|_w\le C_P\|u\|_w\|v\|_w                    \tag{7.7}
\]

hold for all finite jets, where multiplication uses the ordinary
Leibniz rule.

**Proof.** Apply (7.6) to a jet supported only at order \(m\). It gives

\[
w_{m-1}\le C_Jw_m,\qquad m\ge1.                   \tag{7.8}
\]

Now take \(u\) supported at order \(1\) and \(v\) supported at order
\(m-1\). Their product has order-\(m\) coefficient
\({m\choose1}u_1v_{m-1}=m u_1v_{m-1}\). Thus (7.7) requires

\[
m w_m\le C_Pw_1w_{m-1}.                           \tag{7.9}
\]

Combining (7.8) and (7.9) yields

\[
m\le C_PC_Jw_1
\]

for every \(m\), an impossibility. \(\square\)

The same conclusion holds if normalized jets
\(\widetilde u_m=D^mu/m!\) are used. Then multiplication has no binomial
coefficient, but the shift is
\((S\widetilde u)_m=(m+1)\widetilde u_{m+1}\); applying the two estimates
again gives \(m\le C_PC_Jw_1\).

In particular, the usual analytic weights display the conflict
explicitly. For ordinary derivatives, \(w_m=R^m/m!\) makes the Leibniz
binomial coefficients form an exact convolution, but

\[
\frac{w_m}{w_{m+1}}=\frac{m+1}{R}\longrightarrow\infty,
\]

so the adjoint source shift is unbounded. Geometric weights
\(w_m=R^m\) make that shift bounded, but the middle Leibniz coefficient
\({m\choose\lfloor m/2\rfloor}\) is unbounded. The analytic hypothesis
\(\|\varphi^{(r)}\|_\infty\le MA^r r!\) therefore supplies natural
factorial activation bounds but does not, by itself, resolve the
adjoint/product incompatibility.

Proposition 7.2 applies directly if the closures demanded in
(6.1)--(6.2) and in activation/rank-one products are asserted on a
complete derivative-jet algebra. It is independent of how small the
nonzero near-identity amplitude is. Multiplying the shift by a fixed
\(|\alpha|>0\) only changes \(C_J\) by a finite factor and does not remove
the contradiction as \(m\to\infty\). For a strictly smaller reachable
class, one would additionally have to prove that the class contains a
sufficiently rich family of jets before invoking this no-go proposition;
that richness has not been proved here.

These propositions do **not** disprove the desired \(t^4h^5\) estimate.
It proves that an ambient scalar-order, absolute all-source Banach
algebra cannot be the missing proof mechanism. Possible mechanisms not
excluded by the argument are:

1. history-dependent or rooted-tree weights for which insertion of a
   new adjoint mark and distribution of old marks are charged jointly;
2. a norm for the composite connector/product operation, without
   separately bounding \(J^*\) and multiplication;
3. an orthogonal or signed resummation that retains Gaussian cancellation
   instead of taking absolute values at each source history.

None of these mechanisms is presently proved for the \(L=2\) OMFP
dynamics. Therefore the explicit near-identity constants
\(\alpha_0,\rho,C\) requested for the actual network cannot be certified
by this route, and extension to \(L=3\) is not justified.

## 8. Audited conclusion

The following statements are unconditional:

* the exact paired-step factorization (1.1), with \(A_{j,t}\) given by
  (3.5) or (3.9)--(3.14);
* the identity
  \(\kappa_t=t(2t-1)J_{\psi,2}/2\) for the present fine-minus-coarse
  convention;
* the implication (4.8) \(\Rightarrow\) (4.9), with the sharp Taylor
  factor \(1/6\);
* the terminating propagator and terminal-contraction recursions
  (5.3)--(5.33), conditional on the explicitly stated restricted
  generated-core estimates (5.1)--(5.2) and the stated reachable-core
  tube condition;
* the raw-Gaussian same-space product obstruction, Proposition 7.1, and
  the independent scalar source-shift/product obstruction,
  Proposition 7.2.

The first requested closure inequality that actually fails is the
same-space product estimate (7.2), already on raw reachable Gaussian
sources. The direct adjoint estimate (6.2) has the additional
scalar-weight conflict of Proposition 7.2. Therefore the requested
quantitative network theorem remains **OPEN** under the stated
single-norm proof architecture.
