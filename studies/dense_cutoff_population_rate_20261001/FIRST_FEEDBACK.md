# An explicit finite-width bias calculation at the first nonlinear feedback

This calculation tests whether the first genuine forward/adjoint feedback already forces a width-independent error. It does not: its bias is \(O(n^{-1})\), and its mean-square error is \(O(n^{-1})\). This is a local diagnostic for the actual dense model, not an all-time theorem.

## Setup and exact third derivative

Take two hidden tanh layers, one input \(x\) with \(\|x\|_2=\sqrt d\), label \(y\), and the manuscript's canonical dense flow. Write \(v=x/\sqrt d\), so \(\|v\|_2=1\). At initialization let

\[
a=W_0^{(1)}v,\quad h=\tanh(a),\quad s=\operatorname{sech}^2(a),
\quad W=W_0^{(2)},\quad z=Wh,\quad g=\tanh(z).
\]

The entries of \(a\) are independent standard Gaussians; \(W\) has independent \(N(0,1/n)\) entries and is independent of \(a\). Define the scalar function

\[
\psi(u)=\tanh(u)\operatorname{sech}^2(u)
\]

and the returned vector \(T=W^\top\psi(z)\). The relevant empirical quantities are

\[
q_n=\frac{\|h\|_2^2}{n},\quad Q_n=\frac{\|g\|_2^2}{n},\quad
B_n=\frac{\|\psi(z)\|_2^2}{n},\quad
D_n=\frac1n\sum_i s_i^2T_i^2.
\]

For every finite initialization, the exact dense training predictor satisfies

\[
f_n'''(0)=8yQ_n^3+32y^3(q_nB_n+D_n).
\tag{1}
\]

Indeed, zero readout implies \(\dot W^{(1)}(0)=\dot W^{(2)}(0)=0\),
\(\dot h(0)=\dot g(0)=0\), and

\[
\dot w(0)=2yg,\qquad \dot r(0)=2yQ_n,\qquad
\ddot w(0)=-4yQ_ng,\qquad \ddot r(0)=-4yQ_n^2.
\]

Differentiating the actual hidden updates gives

\[
\ddot W^{(1)}(0)=4y^2(s\odot T)v^\top,
\quad\ddot h(0)=4y^2s^2\odot T,
\quad\ddot W^{(2)}(0)=\frac{4y^2}{n}\psi(z)h^\top.
\]

Thus

\[
\ddot z(0)=4y^2\{q_n\psi(z)+W(s^2\odot T)\},
\qquad\frac{g^\top\ddot g(0)}n=4y^2(q_nB_n+D_n).
\]

Finally \(w'''(0)=8yQ_n^2g+2y\ddot g(0)\) and
\(f_n'''(0)=n^{-1}\{w'''(0)^\top g+3\dot w(0)^\top\ddot g(0)\}\), proving (1). All factors use the unhalved mean squared loss and the manuscript's mobilities.

## Exact finite conditional bias of the returned energy

For \(Z\sim N(0,q)\), put

\[
\alpha(q)=\mathbb E\psi'(Z),\qquad
\beta(q)=\mathbb E\psi(Z)^2,\qquad
\gamma(q)=\mathbb E[(\psi^2)''(Z)].
\]

Also set \(S_n=n^{-1}\sum_i s_i^2\) and
\(U_n=n^{-1}\sum_i s_i^2h_i^2\). Gaussian integration by parts in each row of \(W\), conditional on \(a\), gives exactly

\[
\mathbb E[T_i^2\mid a]
=\beta(q_n)+h_i^2\left[
\alpha(q_n)^2+
\frac{\gamma(q_n)-\alpha(q_n)^2}{n}\right].
\tag{2}
\]

For detail, a single row satisfies
\(\mathbb E[W_{ji}\psi(z_j)\mid a]=h_i\alpha(q_n)/n\) and
\(\mathbb E[W_{ji}^2\psi(z_j)^2\mid a]
=\beta(q_n)/n+h_i^2\gamma(q_n)/n^2\).
Sum the diagonal and off-diagonal row products in \(T_i^2\); different rows are conditionally independent. Therefore

\[
\mathbb E[D_n\mid a]
=\beta(q_n)S_n+\alpha(q_n)^2U_n
 +\frac{\gamma(q_n)-\alpha(q_n)^2}{n}U_n.
\tag{3}
\]

The last term is an explicit finite-width feedback correction. The order-one response \(h_i\alpha(q_n)\) is part of the population; omitting it would compare against the wrong population.

## Root-width error and smaller expectation bias

For an independent standard Gaussian \(A\), define

\[
q_* =\mathbb E\tanh(A)^2,\quad
S_* =\mathbb E\operatorname{sech}^4(A),\quad
U_* =\mathbb E[\operatorname{sech}^4(A)\tanh(A)^2],
\quad Q_* =\mathbb E\tanh(\sqrt{q_*}A)^2,
\]

and \(D_* =\beta(q_*)S_*+\alpha(q_*)^2U_*\). Set

\[
J_*=8yQ_*^3+32y^3\{q_*\beta(q_*)+D_*\}.
\]

There are finite constants depending only on fixed \(y\) such that

\[
|\mathbb E f_n'''(0)-J_*|\le C_y/n,
\qquad
\mathbb E|f_n'''(0)-J_*|^2\le C_y/n.
\tag{4}
\]

Here \(J_*\) is defined explicitly as a deterministic jet limit. No differentiation of the global population convergence theorem is used or required.

To prove (4), all derivatives of \(\psi\) and \(\tanh\) are bounded. Gaussian interpolation gives
\(\frac{d}{dq}\mathbb E F(\sqrt q A)=\frac12\mathbb E F''(\sqrt q A)\), also at \(q=0\) by continuity, for the smooth bounded functions used here. Thus \(\alpha,\beta,\gamma\), and the map defining \(Q_*\), have bounded first two derivatives on \([0,1]\). The empirical triple \((q_n,S_n,U_n)\) consists of averages of bounded independent tuples. Its covariance is \(O(n^{-1})\), and its mean is exactly \((q_*,S_*,U_*)\). Taylor's theorem applied to (3) proves

\[
|\mathbb E D_n-D_*|\le C/n,
\qquad \operatorname{Var}(\mathbb E[D_n\mid a])\le C/n.
\tag{5}
\]

For the remaining conditional variance, write \(W=G/\sqrt n\) with independent standard Gaussian entries. With \(h,s\) fixed, differentiating \(D_n=n^{-1}\|s\odot W^\top\psi(Wh)\|_2^2\) yields

\[
\|\nabla_G D_n\|_F^2
\le\frac C{n^2}(1+\|W\|_{\mathrm{op}}^2)\|T\|_2^2
\le\frac Cn(\|W\|_{\mathrm{op}}^2+\|W\|_{\mathrm{op}}^4).
\tag{6}
\]

For verification, if \(u=s^2\odot T\), the two gradient matrices before squaring are
\(2\psi(z)u^\top/(n\sqrt n)\) and
\(2\operatorname{diag}(\psi'(z))Wu h^\top/(n\sqrt n)\).
Use \(\|h\|_2\le\sqrt n\), \(\|\psi(z)\|_2\le\sqrt n\), and
\(\|T\|_2\le\sqrt n\|W\|_{\mathrm{op}}\).

The Gaussian variance inequality \(\operatorname{Var}F(G)\le\mathbb E\|\nabla F(G)\|_2^2\) follows by differentiating
\(\mathbb E[F(G)F(\sqrt tG+\sqrt{1-t}G')]\), integrating by parts in independent \(G,G'\), and integrating from zero to one. Its derivative equals
\(\mathbb E\langle\nabla F(G),\nabla F(\sqrt tG+\sqrt{1-t}G')\rangle/(2\sqrt t)\); Cauchy--Schwarz bounds the integral by the stated expectation. Smooth truncation justifies the formula here, where gradients have polynomial growth. The manuscript's elementary sphere-net Gaussian operator tail, integrated against fixed powers, gives \(\sup_n\mathbb E\|W\|_{\mathrm{op}}^4<\infty\). Applying this inequality to (6) proves
\(\mathbb E\operatorname{Var}(D_n\mid a)\le C/n\).
Together with (5), this proves the claimed bias and variance for \(D_n\).

Conditional on \(a\), the rows \(z_j\) are independent \(N(0,q_n)\). Hence \(Q_n\) and \(B_n\) are averages of bounded independent row functions. Their conditional variances are \(O(n^{-1})\). The conditional mean of \(B_n\) is exactly \(\beta(q_n)\); Taylor expansion of the cube gives
\(\mathbb E[Q_n^3\mid a]=\{\mathbb E\tanh(\sqrt{q_n}A)^2\}^3+O(n^{-1})\).
The same bounded-derivative Taylor argument in \(q_n\) gives \(O(n^{-1})\) unconditional biases for \(Q_n^3\) and \(q_nB_n\), with variance \(O(n^{-1})\). Substituting these and (5)--(6) into (1) proves (4).

## What this resolves and what it does not

The first nonlinear feedback has a genuine finite-width bias, but it vanishes at order \(1/n\); there is no constant-in-width bias at this order. The normalized fluctuations are at most root width. This rules out using the *existence* of forward/adjoint feedback as an argument that a nonvanishing error term is necessary.

Higher time derivatives introduce repeated adaptive returns. Neither a bound on this one jet nor a formal Taylor series sums their errors over a finite or infinite training interval. No all-time rate, clipping-cap rate, or lower bound against root width follows from (4).
