# Nonorthogonal finite-carrier route: exact reductions and the remaining estimate

2026-10-02. Scoped internal research attempt for the actual, unclipped,
two-tanh finite network. The target is a width-uniform residual-weighted
carrier tail for fixed finite input geometry. This note does **not** prove
that target. It records two exact reductions that go beyond the failed
coordinatewise transformation and identifies the finite probabilistic
estimate still needed.

Inputs were this study's complete `FINITE_TAIL_ROUTE.md`,
`FINITE_TAIL_CHECK.md`, and `SAME_WIDTH_COMPARISON_CHECK.md`; the setting in
`paper/main.tex`; complete `paper/results.tex`, `paper/proof_alltime.tex`,
and `paper/proof_tracking.tex`. The canonical-notation skill, its neural
reference, and the rigorous-proof skill were read and applied. No other
study, experiment, Git operation, or manuscript edit was used.

## 1. Setup and the sufficient target

Let \(v_a=x_a/\sqrt d\in\mathbb R^d\), \(a=1,\ldots,m\), be fixed,
and set \(G_{ab}=v_a^\top v_b\). Unit norms may be imposed, but no argument
below requires the off-diagonal Gram entries to vanish. Write
\[
 z_a^{(1)}=Av_a,\quad h_a=\tanh z_a^{(1)},\quad
 z_a^{(2)}=Wh_a,\quad h_a^{(2)}=\tanh z_a^{(2)},\quad
 f_a=n^{-1}w^\top h_a^{(2)}.
\]
Here \(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\),
and \(w\in\mathbb R^n\) are the actual dense parameters. Define
\[
 g_a=\operatorname{sech}^2 z_a^{(1)},\quad
 \gamma_a=\operatorname{sech}^2 z_a^{(2)},\quad
 \delta_a=w\odot\gamma_a,\quad k_a=W^\top\delta_a.
\]
Thus \(\delta_a\) is the second-layer response and \(k_a\) is the first
carrier. Products and scalar functions acting on vectors are coordinatewise.
The residuals and their RMS are \(r_a=f_a-y_a\) and
\(\rho=(m^{-1}\sum_a r_a^2)^{1/2}\).

Use the integrated residuals
\[
 db_a=-\frac2m r_a\,dt.
\]
On the manuscript's fitting event, their total \(\ell^1\) variation is at
most \(S=2Y/\kappa\), where \(Y=(m^{-1}\sum_a y_a^2)^{1/2}\) and
\(\kappa>0\) is the fitting decay rate. As in the checked orthogonal route, every actual
prefix can be reparametrized and constantly extended to a control on
\([0,S]\) satisfying \(\sum_a|b_a'|\le1\). The controlled equations are
\[
 dA=\sum_b(g_b\odot k_b)v_b^\top db_b,\qquad
 dw=\sum_b h_b^{(2)}db_b,\qquad
 dW=\frac1n\sum_b\delta_bh_b^\top db_b.                 \tag{1}
\]
For every such control and \(\|W_0\|_{\rm op}\le K\), bounded activations
give, at variation time \(u\le S\le1\),
\[
 \|w(u)\|_\infty\le u,\quad
 \|\delta_a(u)\|_2/\sqrt n\le u,\quad
 \|W(u)-W_0\|_F\le S^2/2,\quad
 \|k_a(u)\|_2/\sqrt n\le (K+1)S.                    \tag{2}
\]
These estimates require no input orthogonality. They are only RMS bounds
on the lower carrier.

For same-width tracking a useful relaxed target is an exponential,
rather than Gaussian, tail such as
\[
 \mathbb E Z_n(M)\le C e^{-aM},\qquad
 Z_n(M)=\mathbf1_{\mathcal G_n}\int_0^\infty\rho(t)
 \max_a\frac{\|k_a(t)\mathbf1_{|k_a(t)|>M}\|_2}{\sqrt n}\,dt,       \tag{3}
\]
with \(a,C>0\) independent of width and with sufficient exponential
decay relative to the cutoff amplification in the comparison theorem.
The readout has no tail once \(M\ge S\). Neither (2) nor the identities
below prove (3).

## 2. Why a common coordinate straightening is unavailable

For one first-layer row \(u\in\mathbb R^d\), define the vector fields
\[
 X_a(u)=\operatorname{sech}^2(v_a^\top u)v_a.
\]
The row equation is \(du=\sum_a k_{a,i}X_a(u)db_a\). Write
\(g(z)=\operatorname{sech}^2z\), so \(g'(z)=-2\tanh(z)g(z)\).
Direct differentiation gives the Lie bracket
\[
 [X_a,X_b](u)
 =G_{ab}\{g(v_a^\top u)g'(v_b^\top u)v_b
          -g(v_b^\top u)g'(v_a^\top u)v_a\}.                 \tag{4}
\]
The convention here is \([X_a,X_b]=DX_bX_a-DX_aX_b\).
When \(v_a,v_b\) are nonparallel and \(G_{ab}\ne0\), the bracket is
nonzero at some points: their two linear forms can be assigned values
\(0\) and \(1\), making one coefficient zero and the other nonzero.

A smooth invertible coordinate map preserves Lie brackets. Therefore it
cannot simultaneously turn all these \(X_a\) into constant vector
fields. Constant vector fields have zero brackets. The scalar transform
used for orthogonal inputs is consequently not missing an immediate
multivariate analogue that removes every gate in this manner. This is an
obstruction to that proof architecture, not to the tail theorem.

## 3. The carrier equation has bounded operator coefficients

The derivative of the first activation is
\[
 dh_a=\sum_bG_{ab}\operatorname{diag}(g_a\odot g_b)k_b\,db_b.       \tag{5}
\]
In particular, no derivative of \(g_a\) appears in this exact equation.
Let 
\[
 \gamma'_a=-2\tanh(z_a^{(2)})\odot\gamma_a,
 \qquad \langle u,v\rangle_n=n^{-1}u^\top v.
\]
Substituting (1) and (5) into \(dz_a^{(2)}=dW\,h_a+W\,dh_a\), and then
into \(dk_a=dW^\top\delta_a+W^\top d\delta_a\), gives
\[
 dk_a=\sum_b F_{ab}\,db_b+
       \sum_bG_{ab}W^\top\operatorname{diag}(w\odot\gamma'_a)
                     W\operatorname{diag}(g_a\odot g_b)k_b\,db_b,       \tag{6}
\]
where the forcing is explicitly
\[
\begin{aligned}
 F_{ab}={}&h_b\langle\delta_b,\delta_a\rangle_n
       +W^\top\operatorname{diag}(\gamma_a)h_b^{(2)}\\
       &+W^\top\operatorname{diag}(w\odot\gamma'_a)
                       \delta_b\langle h_b,h_a\rangle_n .
\end{aligned}                                                       \tag{7}
\]
Equations (2), \(|g_a|,|\gamma_a|\le1\), and
\(|\gamma'_a|\le2\) show that
\[
 \|F_{ab}\|_2/\sqrt n\le C,
 \qquad
 \|G_{ab}W^\top\operatorname{diag}(w\odot\gamma'_a)
              W\operatorname{diag}(g_a\odot g_b)\|_{\rm op}
 \le C S.                                                        \tag{8}
\]
The constants depend on fixed \(G,m,K\), not on width. Thus the carrier
equation itself is affine in the carriers with bounded operator
coefficients. This avoids the unbounded gate-derivative multiplier in
the variational equation for first-layer states.

It does not permit a Gaussian conclusion by itself. Both the forcing and
the coefficients in (6) depend on the same random matrix and the evolving
carriers. A bounded adaptive operator can concentrate a vector's RMS
mass in one coordinate. For example, a permutation-invariant random
vector that equals \(\sqrt n e_I\), with \(I\) uniform on
\(\{1,\ldots,n\}\), has normalized norm one but
\(\mathbb E e^{c|U_i|}=1+(e^{c\sqrt n}-1)/n\). An RMS bound and
exchangeability therefore cannot replace control of this adaptation.
This example is not asserted to be a network trajectory.

## 4. The full variational equation isolates the difficult local blocks

There is a useful exact Euclidean representation. Set
\(H=\sqrt n W\) and \(\Theta=(A,H,w)\), with the sum-of-squares Euclidean
norm on these three arrays. For each sample define the scalar function
\[
 \mathcal F_b(\Theta)
 =w^\top\tanh\bigl((H/\sqrt n)\tanh(Av_b)\bigr)=nf_b.
\]
Equation (1) becomes
\[
 d\Theta=\sum_b\nabla\mathcal F_b(\Theta)\,db_b.               \tag{9}
\]
For a fixed control, its derivative \(J\) with respect to its initial
state solves
\[
 J'(u)=\left[\sum_b b_b'(u)\nabla^2\mathcal F_b(\Theta(u))\right]J(u).
                                                                    \tag{10}
\]
Split this Hessian as \(D(u)+B(u)\). The only unbounded part \(D\) acts
on the first-layer row variables and is block diagonal over neurons:
\[
 D_i(u)=\sum_b b_b'(u)k_{b,i}(u)g'(z_{b,i}^{(1)}(u))v_bv_b^\top.
                                                                    \tag{11}
\]
All other blocks satisfy \(\|B(u)\|_{\rm op}\le C\), uniformly in
width. To verify the bound, the first differential of \(z_b^{(2)}\) is
\[
 dz_b^{(2)}=W\operatorname{diag}(g_b)(dA)v_b+(dH)h_b/\sqrt n,
\]
whose operator norm from \(d\Theta\) to \(\mathbb R^n\) is bounded by
\(C\). The top-activation curvature is multiplied by
\(w\odot\gamma'_b\), of coordinate maximum at most \(2S\). The mixed
\((A,H)\) second differential pairs \(\delta_b\) with
\((dH)\operatorname{diag}(g_b)(dA)v_b/\sqrt n\), bounded by
\(CS\|dH\|_F\|dA\|_F\). The mixed readout blocks cost at most \(C\).
The remaining first-layer curvature is precisely (11).

This decomposition makes the issue local: the unbounded coefficient is
not a dense random operator, but a fixed-dimensional block at each
first-layer neuron. Ordinary operator-norm Gronwall nevertheless gives
\[
 \|J(u)\|_{\rm op}\le
 \exp\left\{CS+C\int_0^S\max_i\sum_b|k_{b,i}(v)|\,dv\right\}.        \tag{12}
\]
Even a Gaussian maximum of order \(S\sqrt{\log n}\) makes this bound
depend on width. Establishing Gaussian maxima first would also be circular.

## 5. The missing finite response estimate

Delete first-layer neuron \(i\) and its initialized column \(W_{0,i}\),
retaining normalization \(n\). For deterministic controls the resulting
cavity is independent of \(W_{0,i}\sim N(0,I_n/n)\). The learned column
still satisfies, without orthogonality,
\[
 \|W_i(u)-W_{0,i}\|_2\le S^2/(2\sqrt n).                       \tag{13}
\]
If \(\delta_a^{-i,b}\) denotes the cavity response for control \(b\), the
exact decomposition remains
\[
 k_{a,i}^b
 =W_{0,i}^\top\delta_a^{-i,b}
  +W_{0,i}^\top(\delta_a^b-\delta_a^{-i,b})
  +(W_i-W_{0,i})^\top\delta_a^b.                              \tag{14}
\]
The last term is bounded by \(S^3/2\). The first term is a centered
conditional Gaussian for each fixed deterministic driver. The missing
estimate is a width-uniform control of the middle term, jointly with
enough control-path regularity to cover the adaptive residual driver.
The orthogonal proof supplied the stronger deterministic statement
\[
 \sup_{b,u,a}\|\delta_a^b(u)-\delta_a^{-i,b}(u)\|_2\le CS
     (\|W_{0,i}\|_2+S^2/\sqrt n),                            \tag{15}
\]
and a width-uniform Lipschitz map from integrated controls to normalized
cavity responses. Neither statement has been proved here for general
\(G\).

The decomposition (10)--(11) suggests replacing full operator stability
by averaged or directional response bounds: a removed random column
produces a distributed perturbation, whereas the worst vector in (12)
can concentrate on a single unusually large local carrier. This is a
precise potential advantage, but it still requires proof that the
perturbation remains sufficiently spread under the adaptive flow.

Gaussian integration by parts offers another form of the same missing
estimate. For fixed deterministic \(b\), condition on the other
initialization coordinates and put \(x=W_{0,i}\),
\(U=x^\top\delta_a^b\), and \(A_i=\partial_x\delta_a^b\).
For a smooth compactly supported function
\(\chi:\mathbb R^n\to\mathbb R\), the exact conditional identity is
\[
 \mathbb E[\chi(x)Ue^{\lambda U}]
 =\frac1n\mathbb E\left[
       \{\chi(x)\operatorname{tr}A_i+\delta_a^{b\top}\nabla\chi(x)
          +\lambda\chi(x)\delta_a^{b\top}(\delta_a^b+A_i^\top x)\}
                     e^{\lambda U}\right].                         \tag{16}
\]
The displayed formula is the direct sum of the one-dimensional Gaussian
integration-by-parts identities. Compact localization makes it valid at
each fixed width. Passing to \(\chi=1\) requires integrable response
bounds and removal of the explicit \(\nabla\chi\) term. In particular,
a hard initialization-event indicator cannot be differentiated as if it
were constant. The missing bounds concern the response trace and the
directional response under the exponential tilt. The population response
proof in the manuscript bounds deterministic limiting response
coefficients; it does not supply these finite, tilted bounds.

Small labels help in precise ways: they give the short interval \(S\),
the coordinate bound \(\|w\|_\infty\le S\), the \(O(S^3)\) last term in
(14), and an \(O(S^2)\) integrated norm for the carrier-feedback
coefficients in (6). They also keep the contribution of \(B\) in (10)
bounded by \(e^{CS}\). They do not by themselves bound
\(\int_0^S\max_{a,i}|k_{a,i}(u)|\,du\) uniformly in width, control the
middle term in (14), or supply the tilted-response bounds in (16).

The present attempt therefore does not remove the orthogonal-input
restriction, even after relaxing Gaussian tails to exponential tails.
Equations (6) and (10)--(11) narrow the required new work. The checked
orthogonal theorem and its same-width consequence remain unchanged.
