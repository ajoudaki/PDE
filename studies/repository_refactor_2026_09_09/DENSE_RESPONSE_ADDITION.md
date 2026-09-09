## 14. Exact dense residual-network identities and response tails

This section concerns a separate, fully dense residual architecture. All
identities and existence statements are at fixed finite width and depth.
The response estimate approximates derivatives along a supplied trajectory;
its matrices and vectors retain their original dimensions. It supplies no
width limit, continuous-depth limit, or autonomous compressed training model.
The scalar particle results of Sections 1–13 are not assumptions here.

### 14.1 Architecture, initialization, and physical clock

Fix integers \(n,L,d,m\ge1\), a finite batch
\((x_a,y_a)_{a=1}^m\in(\mathbb R^d\times\mathbb R)^m\), and a real
residual strength \(\gamma\). Inputs may be correlated, singular, or
coincident. The trainable parameters are \(B\in\mathbb R^{n\times d}\),
\(W_\ell\in\mathbb R^{n\times n}\) for \(0\le\ell<L\), and the stored
readout \(\mathbf a\in\mathbb R^n\). Define

\[
h_a^0=Bx_a,\qquad z_a^\ell=W_\ell h_a^\ell,\qquad
h_a^{\ell+1}=h_a^\ell+\frac\gamma L\phi(z_a^\ell),\qquad
\phi(z)=\tanh z,
\quad f_a=\frac{\mathbf a^T h_a^L}{n}.
\tag{14.1}
\]

Activation is coordinatewise. Here \(L\) counts residual blocks, and the
linear input map has **no** \(1/\sqrt d\) factor. In particular the input
pairing in the formulas below is \(x_a^Tx_b=dG_{ab}\), with the canonical
\(G_{ab}=x_a^Tx_b/d\). The Gaussian initialization for this architecture is
independent entries and blocks with

\[
(W_\ell(0))_{ij}\sim N(0,\sigma_w^2/n),\quad
B_{ij}(0)\sim N(0,1),\quad
\mathbf a_i(0)\sim N(0,A^2),
\tag{14.2}
\]

where \(\sigma_w,A>0\) are fixed. This is an order-one stored readout,
distinct from the small-readout initialization elsewhere in the book.
Every result below holds for every finite initial parameter state, so no
probability estimate or Gaussian theorem is needed to obtain it.

Use residuals \(r_a=f_a-y_a\), full mean loss
\(\mathcal L=m^{-1}\sum_a r_a^2\), and physical gradient flow

\[
\dot W_\ell=-L\nabla_{W_\ell}\mathcal L,\qquad
\dot B=-n\nabla_B\mathcal L,\qquad
\dot{\mathbf a}=-n\nabla_{\mathbf a}\mathcal L.
\tag{14.3}
\]

All matrices remain unconstrained and all blocks train. If a half-sum loss
\(E=\tfrac12\sum_a r_a^2\) is used with the same mobilities, its vector
field must be multiplied by \(2/m\) to obtain (14.3): a half-sum trajectory
\(\theta_E\) yields \(\theta(t)=\theta_E(2t/m)\). The depth factor
\(1/L\) in (14.1) is architectural, not a physical training step.

### 14.2 Adjoint, gradient, kernel, and finite global flow

Define unit-output adjoints and gated adjoints by

\[
p_a^L=\mathbf a,\qquad
D_a^\ell=\operatorname{diag}(\phi'(z_a^\ell)),\qquad
\beta_a^\ell=D_a^\ell p_a^{\ell+1},\qquad
p_a^\ell=\left(I+\frac\gamma L W_\ell^TD_a^\ell\right)p_a^{\ell+1}.
\tag{14.4}
\]

Indeed the Jacobian of one forward block is
\(I+(\gamma/L)D_a^\ell W_\ell\), so the chain rule gives
\(p_a^\ell=n\,\partial f_a/\partial h_a^\ell\). A variation of each
parameter block therefore gives the three output gradients

\[
\nabla_{\mathbf a}f_a=\frac{h_a^L}{n},\qquad
\nabla_Bf_a=\frac{p_a^0x_a^T}{n},\qquad
\nabla_{W_\ell}f_a=\frac\gamma{nL}\beta_a^\ell(h_a^\ell)^T.
\tag{14.5}
\]

Substituting \(\nabla\mathcal L=(2/m)\sum_b r_b\nabla f_b\) yields

\[
\dot{\mathbf a}=-\frac2m\sum_b r_bh_b^L,\qquad
\dot B=-\frac2m\sum_b r_bp_b^0x_b^T,\qquad
\dot W_\ell=-\frac{2\gamma}{mn}\sum_b
r_b\beta_b^\ell(h_b^\ell)^T.
\tag{14.6}
\]

For any one of these vector families write its sample Gram as
\(G^{u,\ell}_{ab}=(u_a^\ell)^Tu_b^\ell/n\). The scaled tangent kernel is

\[
K_{ab}=G^{h,L}_{ab}+(x_a^Tx_b)G^{p,0}_{ab}
+\frac{\gamma^2}{L}\sum_{\ell=0}^{L-1}
G^{h,\ell}_{ab}G^{\beta,\ell}_{ab},\qquad
\dot f=-\frac2m Kr.
\tag{14.7}
\]

To check every factor, the metric kernel is the sum of output-gradient
pairings weighted by the mobilities in (14.3). For the middle blocks the
Frobenius pairing of the rank-one gradients in (14.5), multiplied by \(L\),
is \(\gamma^2G^{h,\ell}_{ab}G^{\beta,\ell}_{ab}/L\); the other two
blocks give the first two terms. It is positive semidefinite directly:
these terms are the Euclidean Gram matrices of
\(h_a^L/\sqrt n\), \(x_a\otimes p_a^0/\sqrt n\), and
\(\gamma h_a^\ell\otimes\beta_a^\ell/(n\sqrt L)\), respectively.
The tensor identity
\((u\otimes v)^T(\widetilde u\otimes\widetilde v)
=(u^T\widetilde u)(v^T\widetilde v)\) follows by summing the two indices.
Thus \(c^TKc\) is a sum of squared norms for every \(c\in\mathbb R^m\).

Consequently

\[
-\dot{\mathcal L}=\frac4{m^2}r^TKr
=\frac{\|\dot{\mathbf a}\|_2^2}{n}
+\frac{\|\dot B\|_F^2}{n}
+\frac1L\sum_\ell\|\dot W_\ell\|_F^2.
\tag{14.8}
\]

These equations have a unique solution for every \(t\ge0\), from every
finite initial state. Here is the continuation argument. At fixed \(n,L\)
the parameter vector field is smooth. On a small closed parameter ball it
has a bound \(M\) and a Lipschitz constant \(C\). On a time interval of
length \(\tau\) with \(\tau M\) smaller than the ball radius and
\(\tau C<1\), the map \(u\mapsto\theta_0+\int_0^t F(u(s))\,ds\)
preserves that closed ball of continuous paths and contracts distances by
\(\tau C\). Its iterations are uniformly Cauchy by a geometric-series
bound and give a unique local solution. Flatten the parameters into
\(\theta=(\mathbf a,B,W_0,\ldots,W_{L-1})\), and let
\(D_{\rm res}\) be the diagonal matrix with entry \(n\) on readout and
input coordinates and \(L\) on every residual-matrix coordinate. Then
\(\|D_{\rm res}^{-1/2}\dot\theta\|_2^2\) is the last expression in
(14.8). For \(s<t\), Cauchy–Schwarz and (14.8) give

\[
\|D_{\rm res}^{-1/2}(\theta(t)-\theta(s))\|_2
\le\sqrt{(t-s)\,[\mathcal L(s)-\mathcal L(t)]}
\le\sqrt{(t-s)\mathcal L(0)}.
\tag{14.9}
\]

If a maximal interval had finite endpoint, (14.9) would give a finite
parameter limit there. The local construction at that limit extends the
solution, a contradiction. This proves finite-dimensional global flow;
loss monotonicity alone supplies no eventual fitting conclusion.

For later bounds put \(E_0=\mathcal L(0)\). On \([0,T]\), (14.9) gives

\[
\begin{split}
\frac{\|\mathbf a(t)\|_2}{\sqrt n}
&\le\frac{\|\mathbf a(0)\|_2}{\sqrt n}+\sqrt{TE_0},\qquad
\frac{\|B(t)\|_F}{\sqrt n}
\le\frac{\|B(0)\|_F}{\sqrt n}+\sqrt{TE_0},\\
\frac1L\sum_\ell\|W_\ell(t)\|_{\rm op}
&\le\frac1L\sum_\ell\|W_\ell(0)\|_{\rm op}+\sqrt{TE_0}.
\end{split}
\tag{14.10}
\]

For the last inequality, bound each operator norm by its Frobenius norm,
apply Cauchy–Schwarz to the average over layers, and then use (14.9).
Since \(|\tanh|\le1\), the forward recurrence also gives

\[
\frac{\|h_a^\ell(t)\|_2}{\sqrt n}
\le\left(\frac{\|B(0)\|_F}{\sqrt n}+\sqrt{TE_0}\right)\|x_a\|_2
+|\gamma|.
\tag{14.11}
\]

This bound retains the linear input map of (14.1).

### 14.3 Exact training-time responses

All derivatives here are in physical training time. Set
\(v_a^\ell=\dot h_a^\ell\), \(w_a^\ell=\dot p_a^\ell\), and
\(\mathsf A_a^\ell=\gamma D_a^\ell W_\ell\). Differentiating the
forward and adjoint recurrences gives

\[
\begin{split}
v_a^0&=-\frac2m\sum_b r_b(x_b^Tx_a)p_b^0,\\
v_a^{\ell+1}&=(I+\mathsf A_a^\ell/L)v_a^\ell+F_a^\ell/L,\qquad
F_a^\ell=-\frac{2\gamma^2}{m}\sum_b
r_bD_a^\ell\beta_b^\ell G^{h,\ell}_{ba},\\
w_a^L&=-\frac2m\sum_b r_bh_b^L,\\
w_a^\ell&=(I+(\mathsf A_a^\ell)^T/L)w_a^{\ell+1}+S_a^\ell/L,
\qquad S_a^\ell=(\dot{\mathsf A}_a^\ell)^Tp_a^{\ell+1}.
\end{split}
\tag{14.12}
\]

The exact backward source is determined without an extra assumption by

\[
\begin{split}
\dot z_a^\ell&=W_\ell v_a^\ell
-\frac{2\gamma}{m}\sum_b r_b\beta_b^\ell G^{h,\ell}_{ba},\\
\dot D_a^\ell&=\operatorname{diag}
  (\phi''(z_a^\ell)\odot\dot z_a^\ell),\\
\dot{\mathsf A}_a^\ell
&=\gamma(\dot D_a^\ell W_\ell+D_a^\ell\dot W_\ell),\qquad
\dot\beta_a^\ell=\dot D_a^\ell p_a^{\ell+1}+D_a^\ell w_a^{\ell+1}.
\end{split}
\tag{14.13}
\]

For example \(\dot W_\ell h_a^\ell\) in (14.6) is the second term of
\(\dot z_a^\ell\); multiplying it by \(\gamma D_a^\ell\) gives
\(F_a^\ell\). The product rule gives every remaining term in
(14.12)–(14.13), including the transpose in \(S\). For any vector family,
\(\dot G^{u,\ell}_{ab}=[(\dot u_a^\ell)^Tu_b^\ell
+(u_a^\ell)^T\dot u_b^\ell]/n\), so hidden Gram derivatives are also
determined. These formulas retain both directions of each same dense matrix.

### 14.4 Chronological products and exact-source tails

Fix a training time and sample for the next algebra, suppress their indices,
and set

\[
P(\ell,b)=(I+\mathsf A^{\ell-1}/L)\cdots(I+\mathsf A^b/L),
\quad P(b,b)=I.
\tag{14.14}
\]

Later-depth matrices stand on the left. Repeated substitution in (14.12)
gives exactly

\[
v^\ell=P(\ell,0)v^0+\frac1L\sum_{b<\ell}P(\ell,b+1)F^b.
\tag{14.15}
\]

Each degree-\(j\) part of \(P(\ell,b)\) is the sum
\(L^{-j}\mathsf A^{i_j}\cdots\mathsf A^{i_1}\) over strictly ordered
indices \(b\le i_1<\cdots<i_j<\ell\). With
\(c_i=\|\mathsf A^i\|_{\rm op}/L\), its norm is at most
\(\sum_{i_1<\cdots<i_j}c_{i_1}\cdots c_{i_j}\le(\sum_i c_i)^j/j!\).
The last inequality follows by expanding the scalar power: each product
with distinct indices occurs \(j!\) times, and all repeated-index terms
are nonnegative. This proof neither commutes matrices nor uses eigenvalues.

The same grading can be generated without explicitly forming products:

\[
\begin{array}{ll}
v^{[0],\ell}=v^0+L^{-1}\sum_{b<\ell}F^b,&
v^{[j],0}=0\quad(j\ge1),\\
v^{[j],\ell+1}=v^{[j],\ell}
+L^{-1}\mathsf A^\ell v^{[j-1],\ell}&(j\ge1),\\[2pt]
w^{[0],\ell}=w^L+L^{-1}\sum_{b\ge\ell}S^b,&
w^{[j],L}=0\quad(j\ge1),\\
w^{[j],\ell}=w^{[j],\ell+1}
+L^{-1}(\mathsf A^\ell)^Tw^{[j-1],\ell+1}&(j\ge1).
\end{array}
\tag{14.16}
\]

Thus \(v^\ell=\sum_{j=0}^L v^{[j],\ell}\) and
\(w^\ell=\sum_{j=0}^L w^{[j],\ell}\). To verify this, sum the recurrences
over grades; no grade above \(L\) survives the strictly ordered indices.
The sums have the same boundary values and inhomogeneous recurrences as
(14.12), whose solution is unique by successive substitution.
The source itself has grade zero: the grade counts only additional
propagator factors, not every matrix or nonlinear factor inside \(F,S\).

For a fixed \(T<\infty\), define the actual trajectory bounds

\[
\begin{split}
\Lambda_T&=\sup_{a,t\le T}\frac1L\sum_\ell
                 \|\mathsf A_a^\ell(t)\|_{\rm op},\\
B_{v,T}&=\sup_{a,t\le T}\left(
  \frac{\|v_a^0\|_2}{\sqrt n}
  +\frac1L\sum_\ell\frac{\|F_a^\ell\|_2}{\sqrt n}\right),\\
B_{w,T}&=\sup_{a,t\le T}\left(
  \frac{\|w_a^L\|_2}{\sqrt n}
  +\frac1L\sum_\ell\frac{\|S_a^\ell\|_2}{\sqrt n}\right).
\end{split}
\tag{14.17}
\]

They are finite at fixed \(n,L,T\) by global existence and continuity.
In particular (14.10) and \(\|D\|_{\rm op}\le1\) give
\(\Lambda_T\le|\gamma|[L^{-1}\sum_\ell\|W_\ell(0)\|_{\rm op}
+\sqrt{TE_0}]\); (14.4) gives
\(\|p_a^\ell\|_2/\sqrt n\le e^{\Lambda_T}
[\|\mathbf a(0)\|_2/\sqrt n+\sqrt{TE_0}]\).
For integer \(K\ge0\) set
\(R_K(\Lambda)=\sum_{j>K}\Lambda^j/j!\). The ordered-product bound in
(14.15), applied separately to the boundary and every forcing insertion,
proves

\[
\begin{split}
\sup_{a,\ell,t\le T}
\frac{\|v_a^\ell-\sum_{j=0}^K v_a^{[j],\ell}\|_2}{\sqrt n}
&\le B_{v,T}R_K(\Lambda_T),\\
\sup_{a,\ell,t\le T}
\frac{\|w_a^\ell-\sum_{j=0}^K w_a^{[j],\ell}\|_2}{\sqrt n}
&\le B_{w,T}R_K(\Lambda_T),\qquad
R_K(\Lambda)\le e^\Lambda\frac{\Lambda^{K+1}}{(K+1)!}.
\end{split}
\tag{14.18}
\]

For the backward equation reverse depth and transpose each generator;
their norms and the counting argument are unchanged. The scalar tail bound
uses \((K+1+j)!\ge(K+1)!j!\) term by term. Both actual errors vanish for
\(K\ge L\). Uniform constants for a family of widths or depths require
uniform bounds in (14.17); no such probabilistic or limiting assertion is
made here. The factorial is a count of depth orderings, not a claim of
analyticity in training time.

### 14.5 Recomputed backward sources

Keep the supplied trajectory, generators, and terminal \(w^L\) fixed, but
replace \(S\) in the grade-\(K\) backward recursion by a source
\(\widetilde S\). Let \(\widetilde w_K\) denote the resulting truncated
sum and put
\(E_{S,T}=\sup_{a,t\le T}L^{-1}\sum_\ell
\|S_a^\ell-\widetilde S_a^\ell\|_2/\sqrt n\).
Linearity of the source-to-response map and the sum of its degree bounds
give

\[
\sup_{a,\ell,t\le T}
\frac{\|w_a^\ell-\widetilde w_{K,a}^\ell\|_2}{\sqrt n}
\le B_{w,T}R_K(\Lambda_T)+e^{\Lambda_T}E_{S,T}.
\tag{14.19}
\]

For clarity, subtract the two truncated recursions with sources
\(S,\widetilde S\); their boundary difference is zero. Each source
difference is propagated by the sum of degrees \(0,\ldots,K\) of the
appropriate ordered product, of norm at most
\(\sum_{j=0}^K\Lambda_T^j/j!\le e^{\Lambda_T}\). Summing its
\(1/L\)-weighted norms proves the second term of (14.19); (14.18)
supplies the first.

For the particular replacement obtained by using
\(v_K=\sum_{j=0}^K v^{[j]}\) in (14.13), while keeping
\(W,\dot W,h,p,z,D,r\) exact, the source difference is exactly

\[
S_a^\ell-\widetilde S_a^\ell
=\gamma W_\ell^T\left[
\phi''(z_a^\ell)\odot p_a^{\ell+1}
\odot W_\ell(v_a^\ell-v_{K,a}^\ell)\right].
\tag{14.20}
\]

Consequently \(E_{S,T}\le C_T B_{v,T}R_K(\Lambda_T)\), where

\[
C_T=\sup_{a,t\le T}\frac{|\gamma|}{L}\sum_\ell
\|W_\ell\|_{\rm op}^2
\|\phi''(z_a^\ell)\odot p_a^{\ell+1}\|_\infty.
\tag{14.21}
\]

Indeed multiply the two operator-norm bounds and the coordinate multiplier
bound in (14.20), then use (14.18). This finite-state constant is finite;
the normalized adjoint bound above does not give a width-independent
coordinate maximum. If the approximate dynamics also change the trajectory
or \(\dot W\), (14.20) is no longer its entire source error. Establishing
an autonomous response approximation would require control of those changes
and of their full nonlinear feedback. The identities and supplied-trajectory
tail estimates do not provide that theorem, fitting, or nonlazy limit claims.
