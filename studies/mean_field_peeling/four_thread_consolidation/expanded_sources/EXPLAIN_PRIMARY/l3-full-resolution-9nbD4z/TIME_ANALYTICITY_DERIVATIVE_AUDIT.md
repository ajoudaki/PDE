# Time-analyticity: an exact fifth-derivative obstruction and an averaging warning

Status: two narrowly scoped obstructions, not a counterexample to a canonical
high-probability limit or to global continuation. The first uses the full,
unclipped, all-block-trained network with zero initial readout. It disproves
a deterministic width-uniform fifth-derivative bound based only on the usual
primal/operator bounds. Its Gaussian neighborhoods have positive probability
at each relevant width, with no width-uniform probability lower bound. The
second is an explicit scalar example, not a network identification.

## 1. An exact full-network prediction jet

Use normalized vector inner product and rank-one convention
\[
 \langle x,y\rangle_n=n^{-1}x^\top y,\qquad
 x\otimes y=n^{-1}xy^\top.
\]
Matrix norms and matrix inner products are ordinary Euclidean operator and
Frobenius ones. In this note the lower state uses the ORIGINAL first-layer
preactivation, not the transformed coordinate \(F(z^{(1)})\):
\[
 \theta=(z^{(1)},W^{(2)},W^{(3)}),\qquad
 \|\theta\|^2=\|z^{(1)}\|_n^2+
                \|W^{(2)}\|_{\rm F}^2+\|W^{(3)}\|_{\rm F}^2.
\]
Let \(\phi=\arctan\), \(h^{(1)}=\phi(z^{(1)})\),
\(z^{(2)}=W^{(2)}h^{(1)}\), \(h^{(2)}=\phi(z^{(2)})\),
\(z^{(3)}=W^{(3)}h^{(2)}\), and \(H(\theta)=h^{(3)}=\phi(z^{(3)})\).
The prediction and exact feature-time equations are
\[
 f=\langle C,H(\theta)\rangle_n,\qquad
 C'=H(\theta),\qquad \theta'=DH(\theta)^*C.                 \tag{1}
\]
Indeed, with \(D_\ell=\operatorname{diag}(\phi'(z^{(\ell)}))\),
\(\delta^{(3)}=D_3C\), \(q=(W^{(3)})^\top\delta^{(3)}\), and
\(\delta^{(2)}=D_2q\), the three lower updates in (1) are
\[
 (z^{(1)})'=D_1(W^{(2)})^\top\delta^{(2)},\quad
 (W^{(2)})'=\delta^{(2)}\otimes h^{(1)},\quad
 (W^{(3)})'=\delta^{(3)}\otimes h^{(2)}.
\]
Thus no trained block has been suppressed.

Suppose \(C(0)=0\). At \(\theta_0\), write
\[
 h=H(\theta_0),\qquad B=DH(\theta_0),\qquad V=B^*h,
 \qquad T=\langle h,D^2H(\theta_0)[V,V]\rangle_n.
\]
The finite-dimensional field is smooth. Time reversal in (1) makes
\(\theta\) even and \(C\) odd near zero. Differentiating (1) gives
\[
 \theta''(0)=V,\quad C'''(0)=BV,\quad
 \theta^{(4)}(0)=B^*BV+3\{D^2H(\theta_0)[V,\cdot]\}^*h.
\]
If \(H_4=(H(\theta(\cdot)))^{(4)}(0)\), then
\[
 H_4=B\theta^{(4)}(0)+3D^2H[V,V],\qquad
 \langle h,H_4\rangle_n=\|BV\|_n^2+6T.
\]
Expansion of \(f=\langle C,H\rangle_n\), using
\(C=sh+s^3BV/6+s^5H_4/120+O(s^7)\), proves
\[
 \boxed{f'(0)=\|h\|_n^2,\qquad
 f'''(0)=4\|V\|^2,\qquad
 f^{(5)}(0)=16\|BV\|_n^2+36T.}                          \tag{2}
\]
The derivative \(B\) has a width-independent operator bound when the two
hidden operator norms are bounded: propagate a perturbation through the
three layers, using \(\|\Delta W h\|_n\le
\|\Delta W\|_{\rm F}\|h\|_n\), bounded activations, and \(\|D_\ell\|\le1\).
Consequently the first and third derivatives in (2) are uniformly bounded
under those assumptions. The last contraction in (2) is different.

## 2. A bounded-operator family with an unbounded fifth derivative

For every \(n\ge2\), put
\[
 c=\pi/4,\quad d=1/2,\quad e=\phi''(1)=-1/2,\quad \alpha=c^{-1},
 \quad u=n^{-1/2}\mathbf1,
\]
\[
 v_n=\frac{e_1-u/\sqrt n}{\sqrt{1-1/n}},\quad
 w=\alpha u+v_n,\quad b=dc.
\]
Here \(u^\top v_n=0\) and \(\|v_n\|_2=1\). Choose the initial data
\[
 z^{(1)}_0=\mathbf1,\qquad
 W^{(2)}_0=\alpha uu^\top,\qquad
 W^{(3)}_0=uw^\top,\qquad C_0=0.                         \tag{3}
\]
All three preactivation vectors equal \(\mathbf1\), all three activation
vectors equal \(c\mathbf1\), and \(D_1=D_2=D_3=dI\). Moreover
\[
 \|W^{(2)}_0\|_{\rm op}=\alpha<2,\qquad
 \|W^{(3)}_0\|_{\rm op}=\sqrt{\alpha^2+1}<2,
 \qquad \|z^{(1)}_0\|_n=1.                              \tag{4}
\]
The first backward-query derivative is
\[
 q_1=q'(0)=(W^{(3)}_0)^\top D_3h=b\sqrt n\,w.
\]
Its first three empirical moments are exactly
\[
 \langle q_1,\mathbf1\rangle_n=b\alpha,\qquad
 \|q_1\|_n^2=b^2(\alpha^2+1),
\]
\[
 \langle q_1^3,\mathbf1\rangle_n
 =b^3\left[\alpha^3+3\alpha+\frac{n-2}{\sqrt{n-1}}\right]. \tag{5}
\]
For the last identity, expand \((\alpha/\sqrt n+v_{n,j})^3\) and use
\(\sum_jv_{n,j}^3=(n-2)/\sqrt{n(n-1)}\).

All the remaining quantities below are evaluated at (3), with variations
along the FIXED lower-parameter vector \(V\) from (2). Direct backpropagation
gives its three blocks:
\[
 V_z=\lambda\mathbf1,\quad \lambda=d^3/c,\qquad
 V_{W_2}=dcb\,wu^\top,\qquad V_{W_3}=bc\,uu^\top.         \tag{6}
\]
Write \(\zeta_\ell=Dz^{(\ell)}[V]\) and
\(\zeta_{2,2}=D^2z^{(2)}[V,V]\). Then
\[
 \zeta_2=kq_1+\gamma\mathbf1,\quad
 k=dc^2,\quad \gamma=d^4/c^2,
\]
\[
 \zeta_3=\eta\mathbf1,\quad
 \eta=bc^2+dkb(\alpha^2+1)+d\gamma\alpha,
 \qquad BV=d\eta\mathbf1,                               \tag{7}
\]
\[
 \zeta_{2,2}=Aq_1+B_0\mathbf1,\quad
 A=2d^2c\lambda,\quad B_0=e\lambda^2/c.                 \tag{8}
\]
For example, (8) is exactly
\(2V_{W_2}D_1V_z+W^{(2)}_0\phi''(z^{(1)}_0)V_z^2\);
in particular it includes first-layer motion.

The full second-order chain rule gives
\[
 T=ce\eta^2
   +2\langle b\mathbf1,V_{W_3}d\zeta_2\rangle_n
   +\langle q_1,e\zeta_2^2+d\zeta_{2,2}\rangle_n.         \tag{9}
\]
The second term only uses \(\langle q_1,\mathbf1\rangle_n\). Expanding
the last term using (7)--(8), every term except
\(ek^2\langle q_1^3,\mathbf1\rangle_n\) uses only the first two
moments in (5). These moments, \(\eta\), and every displayed scalar
coefficient are independent of \(n\). Equations (2), (5), and (9) therefore
prove the exact identity
\[
 \boxed{f^{(5)}(0)=C_*
       -\frac{9}{16}c^7\frac{n-2}{\sqrt{n-1}},}           \tag{10}
\]
where \(C_*\) is independent of \(n\). The coefficient follows from
\(36ek^2b^3=-9c^7/16\). This is a genuine cubic backward-query contraction
in the actual full-network output derivative, despite the bounded
\(L^2\) norm of \(q_1\).

### Exact force and limitations of (10)

The usual fixed-feature-time primal bounds depend only on the initial
hidden operator bounds and bounded activation. For example, with
\(a=\pi/2\), \(C_0=0\), and initial hidden operator bound \(M\),
\[
 \|C(s)\|_\infty\le as,\qquad
 \|W^{(3)}(s)\|_{\rm op}\le M+a^2s^2/2,
\]
\[
 \|q(s)\|_n\le as(M+a^2s^2/2),\qquad
 \|W^{(2)}(s)\|_{\rm op}
 \le M+a^2Ms^2/2+a^4s^4/8.
\]
These follow directly from (1); the bound for \(z^{(1)}\) follows by
integrating \(\|(z^{(1)})'\|_n\le\|W^{(2)}\|_{\rm op}\|q\|_n\).
Thus (3) satisfies those bounds uniformly on every fixed finite horizon,
with a uniformly bounded initial normalized first-layer norm.

At fixed \(n\), the fifth derivative is continuous in the initial lower
parameters. The independent Gaussian initialization of \(z^{(1)}\) and
of both hidden matrices has positive density everywhere in that finite
dimensional space. Consequently each center (3) has a sufficiently small
open neighborhood of positive Gaussian probability where both hidden
operator norms are below \(3\), the initial first-layer normalized norm
is below \(2\), and \(f^{(5)}(0)\) differs from (10) by less than \(1\).
It follows that a deterministic, width-uniform bound on
\(|f^{(5)}(0)|\) cannot hold almost surely on this entire norm event.
In particular, no factorial/Cauchy derivative bound depending only on
these primal constants is possible.

This is NOT a failure-probability estimate uniform in \(n\). It does not
disprove a bound on additional typical Gaussian events, Gaussian-averaged
analyticity, or analyticity of a limiting output. It does not identify
the tiny-random-readout target with the zero-readout proxy. It leaves
open whether high-order, typical-Gaussian contraction estimates for the
actual linked network yield an analytic continuation mechanism.

## 3. Exact arctan saturation does not justify analytic Gaussian averaging

This section concerns only an exogenously driven scalar characteristic.
Set \(F(z)=z+z^3/3\), \(D(z)=(1+z^2)^{-1}\), and let \(G\) be standard
Gaussian. The exact solution of
\[
 Z_t=D(Z)G,\qquad Z(0)=0
\]
is \(Z(t)=F^{-1}(tG)\). Write
\[
 g(x)=D(F^{-1}(x))=(F^{-1})'(x),\qquad M(t)=\mathbb E[g(tG)].
\]
Every individual sample is analytic near zero. Also \(0<M(t)\le1\),
and \(M\) is \(C^\infty\) on the whole real line. To justify the latter
claim and all derivative expectations, put \(z=F^{-1}(x)\).
Repeated application of \(d/dx=D(z)d/dz\) gives
\[
 g^{(m)}(x)=\frac{P_m(z)}{(1+z^2)^{2m+1}},\qquad
 \deg P_m\le m.                                        \tag{11}
\]
Indeed \(P_0=1\) and
\(P_{m+1}=(1+z^2)P_m'-(4m+2)zP_m\), proving (11) inductively.
Every fixed derivative is therefore bounded on \(\mathbb R\). The mean
value theorem and dominated convergence, with dominating function
\(\|g^{(m+1)}\|_\infty|G|^{m+1}\), justify induction in
\[
 M^{(m)}(t)=\mathbb E[G^m g^{(m)}(tG)].                  \tag{12}
\]
Continuity follows by the same domination. No infinite Taylor series
has been interchanged with expectation.

The local inverse exists analytically because \(F'(0)=1\). Its derivative
has the exact coefficient
\[
 [x^{2k}]g(x)=\frac{(-1)^k}{3^k}\binom{3k}{k}.            \tag{13}
\]
For completeness, the coefficient is the residue of
\(g(x)x^{-2k-1}dx\) at zero. Substituting \(x=F(z)\) gives
\(dz/[z^{2k+1}(1+z^2/3)^{2k+1}]\). Its residue, by the binomial
expansion, is the right side of (13).
Equations (12)--(13) show that the formal Taylor coefficient of \(M\)
at order \(2k\) is
\[
 \frac{M^{(2k)}(0)}{(2k)!}
 =\frac{(-1)^k}{3^k}\binom{3k}{k}\mathbb E[G^{2k}].       \tag{14}
\]
Since \(\binom{3k}{k}=\prod_{j=1}^k(2k+j)/j\ge3^k\), the absolute
coefficient is at least \((2k-1)!!\ge k!\). Its \(2k\)-th root tends
to infinity; for instance \(k!\ge(k/2)^{\lfloor k/2\rfloor}\).
Thus \(M\) has Taylor radius zero and is not analytic at \(t=0\).

This scalar example disproves the inference from samplewise analyticity,
bounded real fields, and arctan saturation to analyticity after Gaussian
averaging. It asserts no nonanalyticity at other times and no equality
with an actual network observable. Together with (10), it identifies
two precise additional proof obligations for an analytic-continuation
route; neither statement decides that route on canonical typical data.
