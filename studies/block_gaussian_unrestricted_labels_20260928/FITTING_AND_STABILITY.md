# Unrestricted scalar-label fitting and the remaining multi-input gap

**Status.** The canonical dense flow has an unconditional, all-time fitting theorem for one nonzero input and every finite scalar label. Its residual clock and weighted parameter-path length have width-independent bounds on a high-probability event under the stated block-Gaussian initialization. For one input, compact response-clock approximation transfers directly to all-time comparison, with an explicit uniform clock-error bound. A finite response-memory closure also has an exact factorized gradient defect, and an accumulated negative defect budget preserves fitting without a small label. The approximation source bounds remain conditional. The unrestricted-label, multiple-input comparison remains open here.

**Scope and provenance.** This is fresh theoretical analysis of the assignment and two subsequent supervisor-supplied candidate arguments, proved below: the block-size-independent Gaussian lower bound and scalar clock-transfer estimate. No other study, research history, external source, or experiment was used. The required rigorous-math and conjecture-investigation instructions were read. Only this assigned report is written. The one-input result is a restricted positive result, not a substitution for the requested multiple-input theorem.

## 1. Model and exact gradient metric

Write

\[
h^1_a=\tanh(W_1x_a/\sqrt d),\qquad
h^\ell_a=\tanh(W_\ell h^{\ell-1}_a),\qquad
f_a=\frac1n w^Th^L_a.
\]

The hidden width is \(n=Bk\), and all entries of every learned matrix train. Define

\[
\delta^L_a=w\odot\tanh'(W_Lh^{L-1}_a),\qquad
\delta^\ell_a=\tanh'(z^\ell_a)\odot W_{\ell+1}^T\delta^{\ell+1}_a.
\]

Thus \(\nabla_w f_a=h^L_a/n\), \(\nabla_{W_1}f_a=\delta^1_ax_a^T/(n\sqrt d)\), and \(\nabla_{W_\ell}f_a=\delta^\ell_a(h^{\ell-1}_a)^T/n\) for \(\ell\ge2\). For the loss \(\mathcal L=\|r\|_2^2/m\), the assigned dynamics have learning rates \(n,n,1,\ldots,1\) on \(w,W_1,W_2,\ldots,W_L\). Consequently their exact dissipation identity is

\[
\dot{\mathcal L}
=-\frac{\|\dot w\|_2^2+\|\dot W_1\|_F^2}{n}
-\sum_{\ell=2}^L\|\dot W_\ell\|_F^2.
\tag{1}
\]

The kernel \(K\in\mathbb R^{m\times m}\) giving \(\dot r=-(2/m)Kr\) is

\[
K_{ab}=\frac{(h^L_a)^Th^L_b}{n}
+\frac{(\delta^1_a)^T\delta^1_b}{n}\frac{x_a^Tx_b}{d}
+\sum_{\ell=2}^L
\frac{[(\delta^\ell_a)^T\delta^\ell_b]
[(h^{\ell-1}_a)^Th^{\ell-1}_b]}{n^2}.
\tag{2}
\]

Each term is a Gram matrix, so \(K\succeq H_L^TH_L/n\succeq0\). Identity (1) by itself controls squared speed, not total path length or \(\int_0^\infty\rho\,dt\).

## 2. Dense one-input theorem for arbitrary label size

Take \(m=1\), a nonzero input, and \(w(0)=0\). Put

\[
Y=|y|,\qquad q_0=\frac{\|h^L(0)\|_2^2}{n}>0.
\]

The case \(Y=0\) is stationary. For \(Y>0\), let \(\sigma=\operatorname{sign}(y)\), \(v=\sigma w\), and define the signed prediction \(g=\sigma f\). Consider first the following trajectory in an independent variable \(s\ge0\):

\[
v_s=h^L,\qquad
(W_1)_s=\delta^1(v)x^T/\sqrt d,\qquad
(W_\ell)_s=\delta^\ell(v)(h^{\ell-1})^T/n\quad(\ell\ge2).
\tag{3}
\]

Here \(\delta(v)\) means the same backpropagation formula with outer weight \(v\). Equation (3) is gradient ascent of the scalar function \(g=v^Th^L/n\) in the metric specified above. In particular, with

\[
p=\frac{\|v\|_2^2}{n},\qquad q=\frac{\|h^L\|_2^2}{n},
\]

one has the exact identities

\[
p_s=2g,\qquad
g_s=K=q+\frac{\|(W_1)_s\|_F^2}{n}
+\sum_{\ell=2}^L\|(W_\ell)_s\|_F^2,
\qquad g^2\le pq.
\tag{4}
\]

The kernel in (4) is scalar and evaluated along (3).

### Positivity and the initial normalized margin

At \(s=0\), all hidden velocities in (3) vanish because \(v(0)=0\). Therefore

\[
v(s)=s h^L(0)+O(s^3),\quad
p(s)=q_0s^2+O(s^4),\quad
g(s)=q_0s+O(s^3).
\tag{5}
\]

In particular, \(p,g>0\) for sufficiently small positive \(s\), and

\[
\lim_{s\downarrow0}\frac{g(s)}{\sqrt{p(s)}}=\sqrt{q_0}.
\tag{6}
\]

On every interval where \(p>0\), (4) gives

\[
\frac{d}{ds}\frac g{\sqrt p}
=\frac{K-g^2/p}{\sqrt p}\ge0.
\tag{7}
\]

Thus the normalized margin stays at least \(\sqrt{q_0}\). Since \(p_s=2g>0\), \(p\) cannot return to zero, so (7) continues throughout the trajectory. It follows that

\[
q\ge\frac{g^2}{p}\ge q_0,\qquad K\ge q_0,
\qquad g(s)\ge q_0s.
\tag{8}
\]

This proves coercivity along the full nonlinear trajectory, without a small-motion or frozen-feature assumption.

### Global existence in response time

For every finite \(S\), \(\|v(s)\|_2\le\sqrt n S\) on \([0,S]\), because \(\|h^L\|_2\le\sqrt n\). The last-layer velocity has norm at most \(S\). Hence \(W_L\) remains bounded on \([0,S]\). Descending through the layers, the bound \(\|\delta^\ell(v)\|_2\le\|v\|_2\prod_{j=\ell+1}^L\|W_j\|_{\rm op}\), together with bounded activations and bounded \(\tanh'\), bounds each earlier matrix velocity. This induction gives finite bounds for every parameter on every finite \(s\)-interval, including \(W_1\). The finite-dimensional smooth vector field therefore extends for all finite \(s\). These existence bounds can depend on the realized initial matrices; they are not being asserted as width-uniform operator-norm bounds.

By (8), there is a unique \(s_*\in(0,Y/q_0]\) satisfying \(g(s_*)=Y\). The physical trajectory is obtained from

\[
\dot s=2[Y-g(s)],\qquad s(0)=0.
\tag{9}
\]

It stays below \(s_*\), approaches \(s_*\) as \(t\to\infty\), and gives exactly the assigned dense dynamics. In particular \(r=-\sigma\rho\), where \(\rho=Y-g\). From (4),

\[
\dot\rho=-2K\rho\le-2q_0\rho.
\]

Therefore, for every finite \(Y\),

\[
0\le\rho(t)\le Ye^{-2q_0t},\qquad
\int_0^\infty\rho(t)\,dt=\frac{s_*}{2}\le\frac{Y}{2q_0},
\qquad
\tau_\infty\le1+\frac{Y}{2q_0}.
\tag{10}
\]

No upper bound on \(Y\) is required.

### Width-uniform parameter-path length

For an increment of the full parameter vector, define

\[
\|d\Theta\|_{\mathsf G}^2
=\frac{\|dv\|_2^2+\|dW_1\|_F^2}{n}
+\sum_{\ell=2}^L\|dW_\ell\|_F^2.
\]

By (4), \(\|\Theta_s\|_{\mathsf G}^2=K=g_s\). The entire physical path lies in \(0\le s<s_*\), so Cauchy–Schwarz gives

\[
\int_0^\infty\|\dot\Theta(t)\|_{\mathsf G}\,dt
=\int_0^{s_*}\sqrt{g_s}\,ds
\le\sqrt{s_*[g(s_*)-g(0)]}
\le\frac{Y}{\sqrt{q_0}}.
\tag{11}
\]

In particular, each later matrix has total Frobenius path length at most \(Y/\sqrt{q_0}\); the first matrix and outer weights have the same bound after division by \(\sqrt n\). Also (7) directly gives \(\|w(t)\|_2/\sqrt n\le Y/\sqrt{q_0}\). The path length controls actual nonlinear training, including off-block entries created after initialization.

### Applicability to the Gaussian law

At initialization the \(B\) blocks of final features are independent and identically distributed. If

\[
Q_b=\frac1k\|h^L_b(0)\|_2^2,\qquad \bar q=\mathbb E Q_b,
\]

then \(q_0=B^{-1}\sum_bQ_b\), with \(0<Q_b<1\) almost surely. To verify positivity, the nonzero input produces a nondegenerate Gaussian first preactivation. At every subsequent block, a Gaussian matrix applied to a nonzero feature vector has a nondegenerate Gaussian distribution; applying \(\tanh\) does not map a nonzero vector to zero. Induction gives \(Q_b>0\) almost surely and hence \(\bar q>0\).

The bounded-variable Hoeffding inequality states that independent \(X_b\in[0,1]\) satisfy \(\Pr(B^{-1}\sum_bX_b-\mathbb EX_b\le-a)\le e^{-2Ba^2}\). One proof is to differentiate the log moment-generating function of a centered bounded variable twice: its second derivative is a tilted variance, at most \(1/4\). Its value and first derivative at zero vanish, so its log moment-generating function is at most \(t^2/8\). Independence, the exponential Markov inequality, and minimization over t give the displayed tail bound. Applying it with \(X_b=Q_b\) and \(a=\bar q/2\) gives

\[
\Pr\{q_0\ge\bar q/2\}\ge1-\exp(-B\bar q^2/2).
\tag{12}
\]

On this event, all constants in (10)–(11) depend on \(Y,k,L,x\), but not on width. Every Gaussian realization with \(q_0>0\) has the deterministic theorem with its own \(q_0\). A deterministic lower bound uniform over every Gaussian realization is not claimed.

There is also an explicit lower bound independent of block size. Let \(G\) be standard normal, \(\nu=\mathbb E\tanh^2G>0\), and \(a>0\) be the variance of the first preactivation at the given input. Write \(\psi(u)=\mathbb E\tanh^2(\sqrt uG)\). Concavity of \(\tanh\) on \([0,\infty)\), and \(\tanh(0)=0\), imply \(\tanh(\sqrt u|G|)\ge\sqrt u\tanh|G|\) for \(0\le u\le1\). Hence \(\psi(u)\ge\nu u\) on that interval. Conditional on a block's preceding feature vector, the next preactivation has coordinate variance \(Q_{\ell-1}=\|h^{\ell-1}_b\|_2^2/k\in[0,1]\), so

\[
\mathbb E[Q_\ell\mid h^{\ell-1}_b]=\psi(Q_{\ell-1})\ge\nu Q_{\ell-1}.
\]

Induction gives \(\bar q\ge q_{\rm G}:=\nu^{L-1}\psi(a)>0\), independently of \(k\). For a normalized input with unit first-preactivation variance, \(q_{\rm G}=\nu^L\). Therefore (12) also holds with \(\bar q\) replaced throughout by \(q_{\rm G}\). This uses the actual Gaussian block distribution, without imposing a uniform bound on the maximum block operator norm.

There is also a bound in total width, including the fully iid dense case
k=n. The function \(\chi(s)=\tanh^2(\sqrt s)\) has derivative
\(\chi'(s)=\tanh(\sqrt s)\operatorname{sech}^2(\sqrt s)/\sqrt s\)
for s>0, with \(\chi'(0)=1\), hence \(0\le\chi'\le1\). Since
\(\psi(u)=\mathbb E\chi(uG^2)\), differentiation dominated by G^2
gives \(0\le\psi'\le1\). Conditional on the preceding features, Q_l is an
average of k independent [0,1]-valued squared activations. Its conditional
variance is at most 1/(4k) and conditional mean is \(\psi(Q_{l-1})\). For any
1-Lipschitz scalar map psi and iid copies U,U',
\(\operatorname{Var}(\psi(U))=\tfrac12\mathbb E(\psi(U)-\psi(U'))^2
\le\operatorname{Var}(U)\). Total variance and induction therefore give
Var(Q_l)<=l/(4k). Averaging the B independent blocks yields

\[
\operatorname{Var}(q_0)\le\frac{L}{4n},\qquad
\mathbb P\{q_0<q_{\rm G}/2\}\le\frac{L}{n q_{\rm G}^2}.
\tag{12a}
\]

Thus the fitting, activity and path-length bounds hold with constants
independent of both width and block size, with probability tending to one
as n tends to infinity for any admissible block-size sequence. Equation
(12a) is an additional coordinator derivation using only this model.

## 3. Exact defect of the finite moment closure

Fix a layer, sample, and finite degree \(J\), and write \(\alpha_j=2j+1\). Suppress the layer/sample subscripts temporarily. Set

\[
(TZ)_j=jZ_j+\sum_{i<j}\alpha_iZ_i,\quad
M=\sum_{j=0}^J\alpha_jC_jB_j^T,\quad
b=\frac1\tau\sum_{j=0}^J\alpha_jB_j,\quad
c=\frac1\tau\sum_{j=0}^J\alpha_jC_j.
\]

The triangular-generator identity is

\[
\sum_j\alpha_j\{(TC)_jB_j^T+C_j(TB)_j^T\}
=\left(\sum_j\alpha_jC_j\right)
 \left(\sum_j\alpha_jB_j\right)^T-M.
\tag{13}
\]

For off-diagonal pairs \(i\ne j\), both sides have coefficient \(\alpha_i\alpha_j\). For a diagonal pair \(j=j\), the right-hand coefficient is \(\alpha_j^2-\alpha_j=2j\alpha_j\), equal to the left-hand coefficient. This verifies (13) term by term.

Using the assigned moment equations and \(\dot\tau=\rho\), differentiate \(M/\tau\). The two terms involving \(\rho M/\tau^2\) cancel, yielding

\[
\frac d{dt}\frac M\tau
=r\delta b^T+\rho c h^T-\rho cb^T.
\]

Restoring samples and the reconstruction coefficient, one obtains the exact identity

\[
\dot{\widehat W}_\ell
=-\frac2{nm}\sum_a r_a\delta^\ell_a(h^{\ell-1}_a)^T+E_\ell,
\qquad
E_\ell=\frac2{nm}\sum_a
(r_a\delta^\ell_a-\rho c^\ell_a)
(h^{\ell-1}_a-b^{\ell-1}_a)^T.
\tag{14}
\]

All quantities in (14) are evaluated self-consistently in the closure. Thus the defect is a product of endpoint reconstruction errors, not a free external perturbation. Define its predictor projection

\[
e_a=\frac1n\sum_{\ell=2}^L
(\delta^\ell_a)^TE_\ell h^{\ell-1}_a.
\tag{15}
\]

With canonical outer-weight and first-layer evolution, the closure satisfies

\[
\dot r=-\frac2mKr+e,
\qquad
\dot{\mathcal L}=-\frac4{m^2}r^TKr+\frac2m r^Te.
\tag{16}
\]

There is no sign certificate for \(r^Te\) in (14). Consequently the dense-flow identity (1) cannot simply be assigned to this closure. This is a proof obligation, not a counterexample to closure convergence.

## 4. A robust scalar fitting criterion with no small-label assumption

For one input, use the response coordinate \(s=2\int_0^t\rho(u)\,du\) and flip the outer weight as above. On the branch \(r=-\sigma\rho\), the closure equations become

\[
\tau=1+s/2,\quad v_s=h^L,\quad
(W_1)_s=\delta^1(v)x^T/\sqrt d,
\]

\[
(B_j)_s=\frac12h-\frac1{2\tau}(TB)_j,\qquad
(C_j)_s=-\frac12\delta(v)-\frac1{2\tau}(TC)_j.
\tag{17}
\]

In particular, this response trajectory is independent of the label magnitude \(Y\), and the hidden response trajectory is also independent of its sign. The label only selects the first level \(g=Y\) and the physical clock.

Let \(\mathcal E_\ell\) be the defect in \(s\)-time. Equations (14) and (17) give

\[
(\widehat W_\ell)_s
=\frac1n\delta^\ell(v)(h^{\ell-1})^T+\mathcal E_\ell,
\quad
\mathcal E_\ell=-\frac1n
[\delta^\ell(v)+c^\ell](h^{\ell-1}-b^{\ell-1})^T.
\tag{18}
\]

Define the scalar defect

\[
D(s)=\sum_{\ell=2}^L\left\langle
\frac1n\delta^\ell(v)(h^{\ell-1})^T,\mathcal E_\ell
\right\rangle_F.
\tag{19}
\]

It obeys \(D=\sigma e/(2\rho)\) wherever \(\rho>0\), and (18) gives its continuous response-time definition at zero residual. With \(R=\sqrt p\) and \(M=g/R\), the exact identities are

\[
p_s=2g,\qquad g_s=K+D,\qquad
M_s=\frac{K-g^2/p+D}{R}\ge-\frac{D_-}{R},
\quad D_-:=\max\{-D,0\}.
\tag{20}
\]

The same initial limit \(M(0+)=\sqrt{q_0}\) holds. Indeed, \(h_s(0)=0\), \(b_s(0)=0\), \(C_s(0)=0\), and \(\delta(v)=O(s)\). Hence \(h-b=O(s^2)\), \(c=O(s^2)\), \(\mathcal E_\ell=O(s^3)\), and

\[
D=O(s^4),\quad R=\sqrt{q_0}s+O(s^3),\quad D_-/R=O(s^3).
\tag{21}
\]

Thus the apparent singularity of the accumulated budget at the initial zero outer weight is integrable. The constants in this local statement can depend on degree and on the finite initialization.

**Conditional theorem.** Fix \(0<\theta<1\), put \(\mu=\theta\sqrt{q_0}\), and let \(S=Y/\mu^2\). Suppose the response path on \([0,S]\) satisfies

\[
\int_0^s\frac{D_-(u)}{R(u)}\,du
\le(1-\theta)\sqrt{q_0}\quad(0\le s\le S).
\tag{22}
\]

The budget is understood initially where \(R>0\); the conclusion below continues that positivity. Equation (20) gives \(M\ge\mu\). Since \(R_s=M\), this yields

\[
R(s)\ge\mu s,\qquad
g(s)=M(s)R(s)\ge\mu^2s,\qquad q(s)\ge M(s)^2\ge\mu^2.
\tag{23}
\]

In particular, \(g\) reaches \(Y\) by some first response time \(s_*\le S\). Before that first root, \(0<g<Y\), and \(\dot s=2[Y-g(s)]\) generates the physical closure. It follows that

\[
\int_0^\infty\rho(t)\,dt=\frac{s_*}{2}
\le\frac{Y}{2\theta^2q_0},\qquad
\frac{\|\widehat w(t)\|_2}{\sqrt n}\le\frac{Y}{\theta\sqrt{q_0}},
\qquad \widehat f(t)\longrightarrow y.
\tag{24}
\]

No pointwise bound of the form \(|e|\le c\rho\), and no exponential decay, is needed for (24). The relevant condition is the accumulated negative predictor defect, not the ambient size of arbitrary matrix perturbations.

For completeness, the finite-degree response system (17) exists on every finite \(s\)-interval. Its \(B\)-moments solve finite linear systems with bounded forcing. Since \(\|v\|_2\le\sqrt n s\), the top-layer \(C\)-moments have bounded forcing, so the reconstructed \(\widehat W_L\) is bounded. Descending through the layers bounds each remaining \(C\)-moment and reconstructed matrix. The canonical \(W_1\) then has bounded derivative. This gives finite-dimensional continuation. At the first root \(g=Y\), the physical-time system freezes; local Lipschitz continuity prevents crossing that root. Thus \(s(t)\to s_*\) and \(\rho(t)\to0\), justifying the all-time conclusion in (24).

### A noncircular sufficient source estimate

Suppose \(q_0\ge q_*>0\), and set \(\mu=\sqrt{q_*}/2\), \(S=4Y/q_*\). Let \(\omega\ge0\) satisfy

\[
I(S):=\int_0^S\frac{\omega(s)}s\,ds<\infty.
\]

If, on the response interval and during the bootstrap \(M\ge\mu\),

\[
D_-(s)\le\varepsilon\omega(s),\qquad
\varepsilon I(S)<q_*/4,
\tag{25}
\]

then \(R\ge\mu s\), and

\[
\int_0^sD_-/R\le\frac\varepsilon\mu I(S)<\sqrt{q_*}/2.
\]

The initial margin is at least \(\sqrt{q_*}\), so it cannot reach the bootstrap boundary \(\mu\). This proves (22) with the corresponding lower margin. Condition (21) is compatible with an integrable source envelope; it is not a uniform-in-degree or uniform-in-width proof of (25).

For every fixed finite \(Y\), the required interval \(S=4Y/q_*\) is finite. Thus a width-uniform approximation theorem making \(\varepsilon\) sufficiently small on each such interval would remove the small-label restriction in the one-input case. Degree could depend on \(Y\). This is an explicit bridge, with the unproved source estimate identified.

If one additionally has \(D_-\le\mu^2/2\), then (23) gives \(g_s=K+D\ge\mu^2/2\), so

\[
\rho(t)\le Ye^{-\mu^2t}.
\tag{26}
\]

Uniform exponential tails of this kind, combined with compact-time comparison of the training prediction, give all-time comparison of that training prediction by choosing a finite time after which both residuals are below the requested error. This statement alone does not control test predictions; their remaining motion would need a separate bound. The degree and constants must still be proved independent of width; neither (25) nor (26) is asserted for the actual closure without that estimate.

## 5. Compact response-clock comparison transfers to all time for one input

For scalar data, there is a simpler comparison route that does not require controlling the differentiated closure defect. Let \(g_D(s)\) be the dense signed training prediction and \(g_J(s)\) the autonomous closure's signed training prediction in response time. Both start at zero and are defined on finite response intervals by the preceding existence arguments. Suppose, for

\[
S=2Y/q_0,\qquad 0<\varepsilon<Y,
\]

that an actual approximation theorem gives

\[
\sup_{0\le s\le S}|g_J(s)-g_D(s)|\le\varepsilon.
\tag{27}
\]

By (8), \(g_D(S)\ge2Y\), so \(g_J(S)>Y\). Thus the closure reaches its first root \(g_J=Y\) at some \(s_J^*<S\), and its physical clock stays below that root. The dense clock stays below \(s_D^*\le Y/q_0\). Both solve

\[
\dot s_D=2[Y-g_D(s_D)],\qquad
\dot s_J=2[Y-g_J(s_J)].
\]

Let \(z=s_J-s_D\). Adding and subtracting \(g_D(s_J)\) gives

\[
\dot z=-2[g_D(s_J)-g_D(s_D)]
+2[g_D(s_J)-g_J(s_J)].
\]

The derivative bound \(g_D'\ge q_0\) and (27) imply the scalar upper-Dini-derivative inequality

\[
D^+|z|\le-2q_0|z|+2\varepsilon.
\]

At \(z=0\), the same inequality follows from \(|\dot z|\le2\varepsilon\). Multiplying the inequality by \(e^{2q_0t}\) and integrating from zero proves

\[
\sup_{t\ge0}|s_J(t)-s_D(t)|
\le\frac\varepsilon{q_0}.
\tag{28}
\]

This estimate requires neither monotonicity of \(g_J\) nor any control of its derivative.

For a training or test observable \(F(s)\), suppose the same response approximation gives \(\sup_{[0,S]}|F_J-F_D|\le\varepsilon_F\). Let

\[
\omega_F(a)=\sup\{|F_D(s)-F_D(u)|:0\le s,u\le S,\ |s-u|\le a\}
\]

be a modulus of continuity for the dense response observable. Then

\[
\sup_{t\ge0}|F_J(s_J(t))-F_D(s_D(t))|
\le\varepsilon_F+\omega_F(\varepsilon/q_0).
\tag{29}
\]

In particular, a response-time Lipschitz bound \(|F_D(s)-F_D(u)|\le L_F|s-u|\) gives \(\varepsilon_F+L_F\varepsilon/q_0\). The argument works in a normed observable space as well, provided the source estimate and modulus are in that norm.

For a width-uniform theorem, (27), the analogous observable estimate, and \(\omega_F\) must be uniform in width on the stated probability event. Smoothness for each fixed width does not establish that uniform modulus. Nevertheless, (28)–(29) remove an entire all-time stability obligation in the one-input case: a compact *response-time* approximation and uniform response regularity suffice for every finite \(Y\). A compact *physical-time* approximation alone does not provide (27).

## 6. Why this does not yet solve the multiple-input problem

There is an exact term obstructing the direct scalar-margin proof. For the dense flow with \(m>1\), on an interval with \(\rho>0\), define

\[
s=2\int_0^t\rho(u)\,du,\qquad
u=-\frac r{\sqrt m\rho},\qquad
h_u=\frac1{\sqrt m}H_Lu,\qquad
g=\frac{u^Tf}{\sqrt m},\qquad p=\frac{\|w\|_2^2}{n}.
\]

Here \(\|u\|_2=1\), \(w_s=h_u\), \(p_s=2g\), and

\[
g_s=\frac{u^TKu}{m}+\frac{u_s^Tf}{\sqrt m},\qquad
\frac{u^TKu}{m}\ge\frac{\|h_u\|_2^2}{n}\ge\frac{g^2}{p}.
\tag{30}
\]

Consequently,

\[
\left(\frac g{\sqrt p}\right)_s
\ge\frac{u_s^Tf}{\sqrt{mp}},\qquad
u_s=-\frac{Ku-u(u^TKu)}{m\rho}.
\tag{31}
\]

The residual direction rotates, and the last term in (31) has no established favorable sign or budget. For one input it vanishes identically. A closure introduces its additional projected defect as well. Therefore the scalar theorem does not prove that the multi-input hidden-feature Gram matrix remains coercive for arbitrary labels.

Equations (30)–(31) locate a concrete missing estimate. They do not prove that fitting fails, that the stated Gaussian initialization reaches a bad state, or that no admissible approximation can work. No bad deterministic initialization is substituted for the Gaussian law here.

## 7. Claim status and decisive remaining obligation

| Claim | Status | Scope |
|---|---|---|
| Dense dissipation and positive kernel | Exact | All stated finite sample sizes |
| Normalized-margin monotonicity, exponential fitting, finite response clock | Proved | One nonzero input, every finite scalar label |
| Weighted total parameter length \(\le Y/\sqrt{q_0}\) | Proved | Same dense scalar setting |
| Width- and block-size-independent positive \(q_0\) on a high-probability Gaussian event | Proved | One nonzero input; includes k=n by (12a) |
| Uniform physical clock error \(\le\varepsilon/q_0\) and observable transfer | Proved conditional theorem | One input; requires compact response-time approximation and a uniform observable modulus |
| Factorized closure defect (14) | Exact | Every finite degree, all sample sizes |
| Closure fitting under accumulated negative-defect budget | Proved conditional theorem | One input; no small-label bound |
| Uniform source estimate (25) for the proposed hierarchy | Open in this report | Necessary approximation-specific bridge |
| Unrestricted-label, multi-input all-time comparison | Open | Scalar argument leaves residual-direction rotation uncontrolled |

The most useful positive outcome is that large label magnitude alone does not prevent a finite residual clock in the actual nonlinear Gaussian model: it is completely harmless for the dense one-input flow. For the scalar closure, compact response-time approximation transfers to all-time comparison through (28)–(29); alternatively, the negative-defect budget gives a direct fitting criterion. The full multi-input question still requires a structural fitting estimate or control of the residual-direction term in (31), together with a width-uniform closure source estimate.
