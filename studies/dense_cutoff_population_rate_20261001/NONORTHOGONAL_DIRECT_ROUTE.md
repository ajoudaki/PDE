# Direct two-layer tracking with arbitrary input geometry

2026-10-02. Scoped internal derivation. This note proves a deterministic
improvement of the actual closure defect and a conditional exponential-tail
tracking theorem. It does **not** establish the finite carrier-tail hypothesis
for arbitrary input geometry, and therefore does not remove the orthogonality
restriction from the existing unconditional same-width theorem.

Scientific inputs: the setting and closure in `paper/main.tex`, complete
`paper/results.tex`, `paper/proof_alltime.tex`, and `paper/proof_tracking.tex`,
and the own-study `FINITE_TAIL_ROUTE.md` and
`SAME_WIDTH_COMPARISON_CHECK.md`. The canonical-notation skill, its neural
reference, and the rigorous-math skill were applied. No other study,
experiment, Git operation, or manuscript edit was used.

## 1. Setup and exact defect

There are two tanh hidden layers of width \(n\), fixed training inputs
\(v_a=x_a/\sqrt d\), and arbitrary fixed input Gram matrix
\(G_{ab}=v_a^\top v_b\). Write \(W=W^{(2)}\). The forward pass and responses
are
\[
z_a^{(1)}=W^{(1)}v_a,\quad h_a^{(1)}=\tanh z_a^{(1)},\quad
z_a^{(2)}=Wh_a^{(1)},\quad h_a^{(2)}=\tanh z_a^{(2)},\quad
f_a=n^{-1}w^\top h_a^{(2)},
\]
\[
r_a=f_a-y_a,\quad \rho=\|r\|_m,
\quad \|r\|_m^2=m^{-1}\sum_a r_a^2,\qquad
\delta_a^{(2)}=w\odot g(z_a^{(2)}),\quad
k_a^{(1)}=W^\top\delta_a^{(2)},\quad
\delta_a^{(1)}=g(z_a^{(1)})\odot k_a^{(1)},
\]
where \(g=\tanh'=\operatorname{sech}^2\).
The loss is \(\mathcal L=\rho^2\), and the canonical dense flow has the
mobilities and factors of two stated in the manuscript.

Fix an initialization in the manuscript's event \(\mathcal G_n\), zero
readout, and \(0<Y=\|y\|_m\le Y_*\). The already proved fitting theorem
gives, for the dense path and every autonomous learning-speed closure,
\[
\rho(t)\le Ye^{-\kappa t},\qquad
\int_t^\infty\rho(s)\,ds\le\rho(t)/\kappa,
\qquad
\frac{\|\dot z_a^{(2)}(t)\|_2}{\sqrt n}\le CY\rho(t).
\tag{1}
\]
All constants here and below are independent of \(n,q,t\), and may be
chosen uniformly over \(0<Y\le Y_*\). The case \(Y=0\) is stationary.

For the closure, hats are suppressed in the rest of this section. Its clock
is \(\dot\tau=\rho\), \(\tau(0)=1\). It records the forward history
\(h_a^{(1)}\) and only the top backward history
\[
b_a^{(2)}=c_a\delta_a^{(2)},\qquad c_a=r_a/\rho.
\]
The forward history is constant on the unit prefix, and the backward
history is zero there. These histories specify the actual autonomous
Legendre closure in the manuscript; no clipping is inserted in its ODE.

Let \(\Pi_q^A\) be orthogonal projection in \(L^2(0,A)\) onto polynomials
of degree below \(q\). Differentiating the exact reconstruction gives
\(\dot{\widehat\theta}=F(\widehat\theta)+E\), where only the hidden
matrix block \(E_2\) is nonzero. The manuscript's projection-energy identity
gives, with \(A=\tau(t)\),
\[
E_2(t)=\frac{2\rho(t)}{mn}\sum_a
\bigl(b_a^{(2)}(t)-b_a^{(2)*}(t)\bigr)
\bigl(h_a^{(1)}(t)-h_a^{(1)*}(t)\bigr)^\top,
\qquad E_1=E_w=0,
\]
where stars mean evaluation of \(\Pi_q^A\) at its current right endpoint.
Its accumulated absolute norm satisfies
\[
\int_0^t\|E_2(s)\|_F\,ds
\le\frac2m\sum_a
\left(\frac1n\int_0^A|(I-\Pi_q^A)b_a^{(2)}|^2d\xi\right)^{1/2}
\left(\frac1n\int_0^A|(I-\Pi_q^A)h_a^{(1)}|^2d\xi\right)^{1/2}.
\tag{2}
\]
Vector absolute values in the integrals denote Euclidean norms.

## 2. An unconditional source estimate, without carrier clipping

**Proposition.** On \(\mathcal G_n\), for arbitrary fixed input geometry,
the two-layer tanh closure satisfies simultaneously for all orders
\[
\epsilon_q:=\int_0^\infty\|E_2(t)\|_Fdt
\le C Y^{5/2}\frac{\sqrt{\log(e+q)}}{q^2}.
\tag{3}
\]

The bounded top activation makes this stronger than the general-depth
argument. The exact readout equation gives a coordinate bound,
\[
\|w(t)\|_\infty
\le\frac2m\int_0^t\sum_a|r_a(s)|ds
\le2\int_0^t\rho(s)ds\le2Y/\kappa.
\tag{4}
\]
The same bound applies to \(\delta_a^{(2)}\). Since
\(\dot\delta_a^{(2)}=\dot w\odot g(z_a^{(2)})+
w\odot g'(z_a^{(2)})\odot\dot z_a^{(2)}\), bounded \(g,g'\), (1),
and \(\|\dot w\|_2/\sqrt n\le2\rho\) imply
\[
\frac{\|\dot\delta_a^{(2)}\|_2}{\sqrt n}\le C\rho.
\tag{5}
\]
No derivative of the first-layer gate appears in this calculation.
The closure residual equation and its relative-defect estimate already
give \(\|\dot c\|_m\le C\); also \(|c_a|\le\sqrt m\). Consequently
\[
\frac{\|b_a^{(2)}\|_2}{\sqrt n}\le CY,
\qquad
\frac{\|\dot b_a^{(2)}\|_2}{\sqrt n}\le C(Y+\rho).
\tag{6}
\]
The history joins continuously to its prefix because \(w(0)=0\).

Fix a physical time \(T\ge0\), and freeze \(b_a^{(2)}\) after \(T\),
calling the resulting history \(b_{a,T}^{(2)}\). If the current time is
less than \(T\), it is simply the original history. The remaining clock
mass after \(T\) is at most \(CY e^{-\kappa T}\), so
\[
\frac{\|b_a^{(2)}-b_{a,T}^{(2)}\|_{L^2(0,A)}}{\sqrt n}
\le CY^{3/2}e^{-\kappa T/2}.
\tag{7}
\]
For its weighted derivative energy, change from clock to physical time
and use \(A-\tau(s)\le\rho(s)/\kappa\):
\[
\begin{aligned}
\frac1n\int_0^A\xi(A-\xi)|(b_{a,T}^{(2)})'(\xi)|^2d\xi
&\le\frac{\sup_t\tau(t)}{\kappa n}
  \int_0^{\min(t,T)}|\dot b_a^{(2)}(s)|^2ds\\
&\le C Y^2(1+T).
\end{aligned}
\tag{8}
\]
The frozen history belongs to \(H^1\) on every such interval: at fixed
finite \(T\) the nonstationary residual is positive and continuous, and
the prefix and freeze joins are continuous. Thus the manuscript's weighted
Legendre bound applies. Projection contraction and (7) yield
\[
\frac{\|(I-\Pi_q^A)b_a^{(2)}\|_{L^2(0,A)}}{\sqrt n}
\le C\left[\frac{Y\sqrt{1+T}}q+
Y^{3/2}e^{-\kappa T/2}\right].
\tag{9}
\]
The already proved forward energy bound is
\[
\frac{\|(I-\Pi_q^A)h_a^{(1)}\|_{L^2(0,A)}}{\sqrt n}
\le CY^{3/2}/q.
\tag{10}
\]
Insert (9)--(10) into (2), and take increasing terminal times. This gives
\[
\epsilon_q\le C\left[
Y^{5/2}\frac{\sqrt{1+T}}{q^2}
+Y^3\frac{e^{-\kappa T/2}}q\right].
\]
Taking \(T=(2/\kappa)\log q\), including \(T=0\) when \(q=1\), proves
(3), after enlarging the constant uniformly for \(Y\le Y_*\).

This proof uses fitting of the actual closure before comparison to the
dense flow. The source bound therefore contains no dense tail, no unknown
parameter discrepancy, and no residual-difference feedback. It also holds
for a bounded top activation with bounded first and second derivatives,
provided the corresponding all-order fitting bounds hold.

## 3. Exponential tails are sufficient for the root-width target

Let
\[
D_{n,q}=\sup_{t\ge0}d_n(\widehat\theta_{n,q}(t),\theta_{n,D}(t)),
\]
where
\(d_n=\|\Delta W^{(1)}\|_F/\sqrt n+\|\Delta W\|_F+
\|\Delta w\|_2/\sqrt n\).
Define the dense weighted carrier tail
\[
Z_n(M)=\int_0^\infty\rho_D(t)
\left[
\max_a\frac{\|k_{D,a}^{(1)}(t)\mathbf1_{|k_{D,a}^{(1)}(t)|>M}\|_2}{\sqrt n}
+\frac{\|w_D(t)\mathbf1_{|w_D(t)|>M}\|_2}{\sqrt n}
\right]dt.
\]
The one-reference damping proof in `proof_tracking.tex` gives
\[
D_{n,q}\le C e^{bM}\,[\epsilon_q+Z_n(M)].
\tag{11}
\]
Moreover one may retain \(b=C_0Y\), with \(C_0\) independent of
\(Y\le Y_*\). Indeed its integrating factor is
\(\exp\{C(1+M)\int\rho_D\}\), all preceding tube and gap constants are
uniform for \(Y\le Y_*\), and \(\int\rho_D\le Y/\kappa\).
The factor \(e^{CY/\kappa}\) is absorbed into \(C\).

**Conditional corollary.** Suppose there is an event
\(\mathcal E_{n,\delta}\subseteq\mathcal G_n\) with probability at least
\(1-\delta\) on which
\[
Z_n(M)\le B_\delta e^{-aM}
\quad\text{for every integer }M\ge M_0,
\qquad a>b>0,
\tag{12}
\]
with constants independent of width and order. Set
\(\theta=1-b/a\in(0,1)\). Then simultaneously for every order,
\[
D_{n,q}\le C_\delta
q^{-2\theta}\,[\log(e+q)]^{\theta/2}.
\tag{13}
\]
To prove it, let \(s_q=\sqrt{\log(e+q)}/q^2\), absorb fixed powers of
\(Y\) into the constants, and choose an integer
\(M\ge M_0\) with \(B_\delta e^{-aM}\le s_q\) and
\(M\le C_\delta+a^{-1}\log(1/s_q)\) for small \(s_q\).
Equations (3) and (11) then give
\(D_{n,q}\le C_\delta s_q^{1-b/a}\), proving (13). The common physical
bound handles the finitely many remaining orders. There is no order
absorption condition and no squared damping factor in this two-layer proof.

If \(\theta>1/4\), equivalently \(a>4b/3\), take
\[
q_n=\left\lceil
n^{1/(4\theta)}[\log(e+n)]^{1/4}\right\rceil.
\tag{14}
\]
Then (13) is at most \(C_\delta n^{-1/2}\), and \(q_n=o(n)\).
The whole-input estimate in the manuscript transfers this to
\(\mathcal E_\mu(\widehat f_{n,q_n},f_{n,D})\) for every fixed test law
with finite second moment, or to the uniform absolute error on a fixed
bounded query set. The evolving state is
\[
2mnq_n+n(d+1)+O(1)
=O\!\left(n^{1+1/(4\theta)}[\log(e+n)]^{1/4}\right),
\]
strictly subquadratic. The initialized \(n\times n\) mixer is still stored
exactly; total storage and matrix-vector runtime are not reduced by this count.

One useful form of a potential missing finite-tail theorem would be
\[
Z_n(YR)\le B_\delta Y^2e^{-a_0R}
\quad\text{for every integer }R\ge R_0,
\tag{15}
\]
where \(a_0,R_0\) do not deteriorate as \(Y\downarrow0\).
The deterministic comparison works at every positive real cutoff; its
integer restriction in the manuscript is only for tail events.
At \(M=YR\), the amplification is \(e^{C_0Y^2R}\), so now
\(\theta=1-C_0Y^2/a_0\). Sufficiently small fixed labels would ensure
\(\theta>1/4\). Equation (15) remains a hypothesis in this note.

In contrast, a fixed polynomial-tail estimate \(Z_n(M)\le C_pM^{-p}\)
does not suffice in (11). For \(b>0\), the function
\(e^{bM}M^{-p}\) has a strictly positive minimum on \(M\ge1\), and
diverges as \(M\to\infty\). Merely substituting finite moments into this
unchanged comparison cannot even make its upper bound vanish as
\(q\to\infty\). This is a limitation of that estimate, not a
counterexample to actual convergence or to another stability argument.

## 4. Why the loss Hessian does not immediately close stability

In the Hilbert norm corresponding to the mobilities,
\[
\|\Delta\theta\|_{\mathrm{mob}}^2
=n^{-1}\|\Delta W^{(1)}\|_F^2+\|\Delta W\|_F^2
+n^{-1}\|\Delta w\|_2^2,
\]
the Hessian of the loss decomposes into a nonnegative Jacobian term plus
the residual-weighted prediction Hessian:
\[
D^2\mathcal L[U,U]
=2\|Df[U]\|_m^2+\frac2m\sum_a r_aD^2f_a[U,U].
\tag{16}
\]
For a unit direction supported on first-layer neuron \(i\), with
\(\Delta W^{(1)}=\sqrt n e_i u^\top\), \(\|u\|_2=1\), direct
differentiation gives
\[
D^2f_a[U,U]=(v_a^\top u)^2
\left[
g(z_{a,i}^{(1)})^2
\sum_j w_j\tanh''(z_{a,j}^{(2)})W_{ji}^2
+k_{a,i}^{(1)}\tanh''(z_{a,i}^{(1)})
\right].
\tag{17}
\]
The first term is bounded using \(\|w\|_\infty\) and
\(\|W_i\|_2\); the second contains an individual carrier.

The common physical tube alone does not give width-independent lower
curvature. For a concrete example, take one unit input, a fixed \(s>0\),
\(h=\tanh s\), and
\[
W^{(1)}=s\mathbf1,\qquad
W=I-\frac{\mathbf1 e_1^\top}{\sqrt n},\qquad
w=\tfrac12Y\mathbf1,\qquad y=Y.
\]
Here \(\|W\|_{\rm op}\le2\), the first-layer RMS is \(s\), the
readout coordinate bound is \(Y/2\), and
\(z_j^{(2)}=h(1-n^{-1/2})\) for every \(j\). Thus the readout-feature
Gram has a fixed positive gap for all sufficiently large \(n\), while
\[
r=Y\{\tfrac12\tanh[h(1-n^{-1/2})]-1\}<0,
\qquad
k_1^{(1)}=\tfrac12Yg[h(1-n^{-1/2})](1-\sqrt n)<0.
\]
Since \(\tanh''s<0\), the second term of (17), multiplied by \(r\),
is negative of size \(Y^2\sqrt n\). The remaining curvature terms,
including \(2|Df[U]|^2\), are \(O(Y^2)\). Hence
\[
D^2\mathcal L[U,U]\le-cY^2\sqrt n+CY^2
\]
for this family. It obeys the deterministic tube bounds but is not claimed
to be a Gaussian-initialized training trajectory. Therefore it rules out
a uniform semiconvexity estimate derived solely from those tube bounds;
it does not rule out a trajectory-specific argument, a special estimate
for the low-rank closure defect, or an averaged probabilistic estimate.

The bounded top response closes the source estimate (3). It does not
remove the first-layer term in (17), or prove (12)/(15). That finite
tail or a genuinely stronger stability estimate is the remaining bridge.
