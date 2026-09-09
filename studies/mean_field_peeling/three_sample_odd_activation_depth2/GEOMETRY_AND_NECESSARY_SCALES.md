# Three inputs, two hidden layers: rigorous geometry and necessary scales

This note concerns the exact raw model in `two_sample_odd_activation_depth56/PROOF.md`, restricted to two hidden layers and extended to three examples. Put \(u_i=x_i/\sqrt d\), \(\Gamma_{ij}=u_i\cdot u_j\), and assume \(\|u_i\|=1\), \(|\Gamma_{ij}|\le1-\delta\). The activation is
\[
\phi(z)=az+e\arctan z,\qquad a=1-e,\qquad 0<e\le1/2.
\]
The population readout initializes at zero. Write \(A\) for the one adjacent action, \(h_i^1=\phi(z_i^1)\), \(z_i^2=Ah_i^1\), \(h_i^2=\phi(z_i^2)\), and \(f_i=\langle C,h_i^2\rangle\). The algebraic parameter-state identities also hold at finite width with normalized inner products. Bounds using C(0)=0 and the canonical initialized action norm two concern the population initialization; at finite width their counterparts must retain the actual nonzero random readout and actual initialized action norm.

The result is positive initialization geometry, a matching sharp scale through layer two, and quantitative necessary dependence on \(e\). None of these statements is a counterexample to the qualitative positive-\(e\) global population theorem.

## 1. The top initialized feature Gram is uniformly positive, even at singular input Grams

Set \(s_\delta=\delta(2-\delta)\). For each \(i\ne j\), put
\[
v_{ij}=\frac{u_i-\Gamma_{ij}u_j}{\sqrt{1-\Gamma_{ij}^2}}.
\]
Its norm is one, it is orthogonal to \(u_j\), and \(u_i\cdot v_{ij}\ge\sqrt{s_\delta}\). If \(\{i,j,k\}=\{1,2,3\}\), then
\(R_i=u_i\otimes v_{ij}\otimes v_{ik}\) has norm one, annihilates \(u_j^{\otimes3},u_k^{\otimes3}\), and has pairing at least \(s_\delta\) with \(u_i^{\otimes3}\). Consequently, for any \(c\in\mathbb R^3\),
\[
|c_i|s_\delta\le\left\|\sum_jc_ju_j^{\otimes3}\right\|,
\qquad
\Gamma^{\circ3}\succeq\frac{s_\delta^2}{3}I_3.             \tag{1}
\]
Let \(G\) be standard normal,
\[
m=\mathbb E(1+G^2)^{-1}>1/2,\qquad b_3=(1-2m)/\sqrt6\ne0.
\]
Strict Jensen gives the displayed strict inequality. Integration by parts gives
\(\mathbb E[\arctan(G)(G^3-3G)]=1-2m\). The third Gaussian chaos projection of \(\phi(u_i\cdot g)\) is therefore \(eb_3[(u_i\cdot g)^3-3u_i\cdot g]/\sqrt6\). Its covariance is \(e^2b_3^2\Gamma^{\circ3}\); its residual is orthogonal to that entire third-chaos span. Thus the first initialized feature Gram satisfies
\[
Q_1\succeq e^2b_3^2\frac{s_\delta^2}{3}I_3.             \tag{2}
\]
At layer two the preactivation Gaussian has covariance \(Q_1\) and common positive marginal variance \(q\). Its first-chaos coefficient is
\[
c_q=\frac{\mathbb E[\phi(\sqrt qG)G]}{\sqrt q}\ge a,
\]
since \(z\arctan z\ge0\). Gaussian regression makes \(\phi(Z_i)-c_qZ_i\) orthogonal to all coordinates of \(Z\). Therefore
\[
Q_2(0)\succeq a^2e^2b_3^2\frac{\delta^2(2-\delta)^2}{3}I_3. \tag{3}
\]
This proves a positive initial full training kernel because its only nonzero block at population initialization is \(Q_2(0)\).

An elementary numerical lower bound is available without evaluating a Gaussian integral. The identity
\[
m-\tfrac12=\tfrac14\mathbb E\frac{(G^2-1)^2}{1+G^2}
\]
follows by expanding \((1+x)^{-1}=1/2-(x-1)/4+(x-1)^2/[4(1+x)]\) and using \(\mathbb EG^2=1\). On \(|G|\le1/2\), the fraction is at least \(9/20\), while the probability of that interval is at least \(\exp(-1/8)/\sqrt{2\pi}\). Hence
\[
b_3^2\ge\frac{81\exp(-1/4)}{19200\pi},\qquad
Q_2(0)\succeq\frac{81\exp(-1/4)}{230400\pi}e^2\delta^2I_3. \tag{3a}
\]
The second bound uses \(a\ge1/2\) and \(s_\delta\ge\delta\).

As an expressivity check, freezing the hidden layers and training only the readout would give \(f(t)=y-e^{-Q_2t}y\) and loss at most \((3/2)e^{-2\lambda_{\min}(Q_2)t}\). This is an auxiliary frozen-feature flow, not the requested joint GF. It establishes that singular \(\Gamma\) is not a representation obstruction at positive \(e\).

## 2. Matching upper bound for the second initialized feature Gram

This strengthens the existing note's matching upper bound, which was stated only for \(Q_1\). Choose
\[
u_+=(c,\sqrt{1-c^2}),\quad u_0=(1,0),\quad u_-=(c,-\sqrt{1-c^2}),
\quad v=(1,-2c,1),\quad 0<c<1.
\]
Put \(C_0=2\sqrt3+2+\pi\). For first-layer Gaussians \(Z_0=G_1\), \(Z_\pm=cG_1\pm\sqrt{1-c^2}G_2\), the linear combination \(v\cdot Z\) is zero. Taylor's integral remainder and \(\|\arctan''\|_\infty\le1\) give
\[
\|v\cdot h^1\|_2\le e C_0(1-c).                       \tag{4}
\]
Explicitly, the centered second difference is bounded by \((1-c^2)G_2^2\), and
\[
\|\arctan(cG_1)-c\arctan(G_1)\|_2
\le(1-c)(1+\pi/2).
\]
Now let \((B_+,B_0,B_-)\) be the second-layer centered Gaussian tuple, with covariance \(Q_1\). Set
\(M=(B_++B_-)/2\), \(D=(B_+-B_-)/2\). Then
\[
\|2(M-cB_0)\|_2=\|v\cdot h^1\|_2\le eC_0(1-c).
\]
Since \(\phi\) is one-Lipschitz and \(|\phi(z)|\le|z|\),
\[
\operatorname{Var}(D)
=\tfrac14\mathbb E[\phi(Z_+)-\phi(Z_-)]^2\le1-c^2,
\qquad \|B_0\|_2\le1.
\]
There is no independence assumption on \(M,D,B_0\). Decomposing
\[
\begin{split}
v\cdot\arctan B={}&\arctan(M+D)+\arctan(M-D)-2\arctan M\\
&+2[\arctan M-\arctan(cB_0)]\\
&+2[\arctan(cB_0)-c\arctan B_0]
\end{split}
\]
and using \(\|D^2\|_2=\sqrt3\operatorname{Var}(D)\) gives
\[
\|v\cdot\arctan B\|_2\le(1+e)C_0(1-c).
\]
Combining its linear and nonlinear activation parts and using \(a+e=1\),
\[
\|v\cdot h^2\|_2
\le aeC_0(1-c)+e(1+e)C_0(1-c)=2eC_0(1-c).              \tag{5}
\]
Consequently
\[
\lambda_{\min}(Q_2)\le\frac{4e^2C_0^2(1-c)^2}{2+4c^2}. \tag{6}
\]
For \(0<\delta\le1/4\), choose \(c=1-\delta\). The correlations \(c,c,2c^2-1\) all satisfy the closed separation condition. Equations (3),(6) show that for every fixed \(d\ge2\), the infimum of \(\lambda_{\min}(Q_2)\) over all admissible triples is \(\Theta(e^2\delta^2)\), with absolute constants for \(0<e\le1/2\). For strict inequalities choose \(c=1-2\delta\), as in the existing note, and change the upper constant by four.

The recurrence in (5) also shows \(\|v\cdot h^L\|_2\le LeC_0(1-c)\) at every fixed initialized depth: the mixture identity \(a+e=1\) makes the induction coefficient increase by exactly one. This observation is about initialization, not all-time dynamics.

## 3. Equilateral inputs distinguish an obstruction to a rate from a counterexample to the theorem

Take \(u_1+u_2+u_3=0\), \(\Gamma_{ij}=-1/2\) for \(i\ne j\), and \(y=(1,1,1)\). This satisfies the closed condition for every \(\delta\le1/2\). At \(e=0\), every hidden feature sum vanishes and the population flow initialized at \(C=0\) is stationary. At \(e>0\), (3) gives
\[
H_0=\tfrac13\sum_i h_i^2(0)\ne0,
\qquad
\|H_0\|^2\ge a^2e^2b_3^2s_\delta^2/9.                \tag{7}
\]
In particular the positive-mixture trajectory is not initially stationary.

For this geometry, at every parameter state put \(T_\ell=\sum_i\arctan z_i^\ell\). Exact cancellation at the bottom gives
\[
\sum_i h_i^1=eT_1,\qquad
\sum_i h_i^2=e(aAT_1+T_2),\qquad \|T_\ell\|_2\le3\pi/2.
\]
Hence
\[
\left|\sum_i f_i\right|
\le\frac{3\pi}{2}e\|C\|_2(1+a\|A\|).                 \tag{8}
\]
At initialization \(\|A_0\|\le2\) in the canonical operator realization and therefore
\[
\|H_0\|\le\frac\pi2e(1+2a).                           \tag{9}
\]
The exact initial loss derivative is
\[
-\dot{\mathcal L}(0)=y^TQ_2(0)y=9\|H_0\|^2.
\]
Thus a certificate \(\mathcal L(t)\le\mathcal L(0)e^{-\kappa t}\) valid from time zero requires
\[
\kappa\le6\|H_0\|^2\le\frac{3\pi^2}{2}e^2(1+2a)^2.   \tag{10}
\]
In particular the two-input loss rate of order \(\delta\), independent of \(e\), cannot hold for all \(0<e\le c\delta^p\) on three inputs at depth two.

There is an exact leading coefficient as \(e\downarrow0\). Let \(X\) be a centered equilateral standard Gaussian triple and
\[
\eta=\tfrac13\mathbb E\left(\sum_i\arctan X_i\right)^2>0.
\]
The common-sector eigenvalue of \(Q_1\) is exactly \(e^2\eta\). Write the layer-two Gaussian as
\(B_i=\alpha_e X_i+e\sqrt{\eta/3}G\), where \(G\) is an independent standard normal and \(\alpha_e\to1\) matches the orthogonal-sector covariance. Since \(\sum X_i=0\),
\[
\frac1e\sum_i\phi(B_i)
\longrightarrow \sqrt{3\eta}G+\sum_i\arctan X_i
\quad\hbox{in }L^2.
\]
The two limiting terms are independent and centered. It follows that
\[
y^TQ_2(0)y=6\eta e^2+o(e^2),\qquad
\|H_0\|^2=\tfrac23\eta e^2+o(e^2).                    \tag{11}
\]
Positivity of \(\eta\) also follows directly from (2), or from the nonzero analytic function \(\sum\arctan X_i\) on the equilateral plane.

## 4. Any successful actual GF must make a large excursion, with fitting time at least order e^{-1}

If \(\mathcal L\le3/8\), then \(\|r\|_2\le\sqrt3/2\) and
\(\sum_i f_i\ge3-\sqrt3\|r\|_2\ge3/2\). Equation (8) implies
\[
\|C\|_2(1+a\|A\|)\ge\frac1{\pi e}.                   \tag{12}
\]
Let \(R\) be the raw Hilbert distance from the initialized state, and put \(x=\|C\|_2\), \(y=\|A-A_0\|_{HS}\). The raw metric and \(C_0=0\) imply \(x^2+y^2\le R^2\). Since \(\|A_0\|\le2\), \(a\le1\), and an operator norm is bounded by its Hilbert--Schmidt norm,
\[
\|C\|_2(1+a\|A\|)\le x(3+y)
\le3R+\frac{x^2+y^2}{2}\le3R+\frac{R^2}{2}.
\]
Combining with (12) and solving the resulting quadratic inequality gives
\[
R\ge R_e:=\sqrt{9+\frac{2}{\pi e}}-3.                \tag{13}
\]

On any true strong GF existing up to the fitting time \(T\), the exact energy identity gives
\[
R\le\int_0^T\|\dot\Theta\|_{\rm raw}
\le\sqrt{T[\mathcal L(0)-\mathcal L(T)]}\le\sqrt{3T/2}.
\]
Therefore
\[
T\ge\frac23\left[\sqrt{9+\frac{2}{\pi e}}-3\right]^2,
\qquad \liminf_{e\downarrow0}eT\ge\frac4{3\pi}.       \tag{14}
\]
The limit inferior applies to any family of successful fitting times with \(e\downarrow0\); the displayed inequality holds separately for every positive \(e\).
This refutes even a \(e\)-independent exponential bound with a larger fixed prefactor: such a bound would force a uniformly finite time to reach loss \(3/8\), whereas (14) diverges at fixed \(\delta\le1/2\). The conclusion is conditional only in the ordinary sense that it lower-bounds the fitting time of any successfully fitting strong GF. It does not assert that successful fitting occurs.

## 5. The nonlinear scalar clock is available in the symmetric case, subject to the analytic bridge

Assume a canonical strong ascent trajectory exists for
\[
J(\theta_h,C)=\langle C,H(\theta_h)\rangle,\qquad
H=\tfrac13\sum_i h_i^2,
\qquad \Theta'=\nabla J,\quad C(0)=0.
\]
The chain rule gives \(J'=\|\nabla_{\theta_h}J\|^2+\|H\|^2\). Continuity yields \(C(s)=sH_0+o(s)\) and \(J(s)=s\|H_0\|^2+o(s)\). Therefore \(J\) is positive first for small positive times and then for all later times by monotonicity; \((\|C\|^2)'=2J\) makes \(C\ne0\) at every positive time. For \(c=\|C\|>0\), \(c'=J/c\), and
\[
\left(\frac Jc\right)'
=\frac{\|\nabla_{\theta_h}J\|^2+\|H\|^2-|\langle C/c,H\rangle|^2}{c}\ge0.
\]
Its limit at zero is \(\|H_0\|\). Thus
\[
J'\ge\|H_0\|^2.
\]
Provided the strong trajectory continues, it reaches \(J=1\) by ascent time \(\|H_0\|^{-2}\). Up to that first hit the raw path length is at most \(\|H_0\|^{-1}\), by ascent energy and Cauchy--Schwarz.

The equilateral data symmetry forces equal population predictions once the canonical construction or its uniqueness justifies that symmetry. Physical GF then satisfies
\[
\dot\Theta=3(1-J)\nabla J,\qquad
\mathcal L=\tfrac32(1-J)^2,
\]
and the scalar inequality proves
\[
\mathcal L(t)\le\tfrac32\exp[-6\|H_0\|^2t]
\le\tfrac32\exp\left[-\tfrac23a^2e^2b_3^2s_\delta^2t\right]. \tag{15}
\]
If the strong ascent exists through its first hit \(s_*\) of \(J=1\), its continuous gradient is bounded on that compact ascent interval. Thus \(1-J(s)\le M(s_*-s)\) for some finite \(M\), and
\[
t(s)=\int_0^s\frac{du}{3(1-J(u))}\longrightarrow\infty
\quad(s\uparrow s_*).
\]
Its inverse supplies the global physical parametrization and (15). If the ascent instead stops before reaching the hit, the path-length bound gives a strong raw endpoint but does not by itself prove continuation of the uncut infinite-dimensional field from that endpoint.

The certified ascent horizon has size \(\Theta(e^{-2})\) at fixed separation, and the certified raw length is \(O(e^{-1})\), consistent with (13),(14). For generic triples, folding binary labels preserves the model but does not create transitive input symmetry, so their three residuals do not share this scalar clock.

This argument proves a useful nonlinear primal estimate. It does not prove uncut strong existence through the clock, source tails and cap removal, uniqueness, the finite-width GF/raw-GD limit, or an all-time trained activation-regression margin. No inference of nonexistence from the failure of an affine reference is justified. The requested qualitative full theorem is not contradicted by any result in this note; its quantitative rate must depend on the nonlinear amplitude on the admitted singular geometries.
