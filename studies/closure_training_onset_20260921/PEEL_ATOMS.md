# Exact Gaussian-atom reduction of the prescribed p1 kernel

This is a scoped, prompt-only theory derivation. It does not use another study or a training experiment. All limits and error estimates below are mathematical statements; a finite truncation is an approximation, not a finite closure theorem.

Write \(\sigma=\tanh\), \(\eta=1/4096\), and use the definitions of \(v,\tau,\alpha,k,s,\beta,\gamma,A_\rho,B_\rho,\Lambda\) in the assignment. In particular
\[
v=\mathbb E\sigma(G)^2,\qquad
\tau=\mathbb E\sigma(\sqrt vG)^2,\qquad \alpha=1-\tau,
\]
so \(0<v,\tau,\alpha<1\). All Gaussian variables mentioned below are standard unless a scale is shown. A Gaussian atom is an expectation of a finite product of activation derivatives at jointly Gaussian arguments; repeated arguments and derivative order zero are permitted.

The construction has two steps. Expand the bounded lower-layer shift by a uniformly convergent Taylor series. Approximate the remaining outer activation on its bounded argument interval by an explicitly specified Chebyshev interpolation polynomial. Each finite polynomial reduces to finitely many Gaussian atoms. Both errors have geometric bounds.

## 1. Removing the lower random shift

Define
\[
m_j=\mathbb E\sigma(G)^j,\quad
d_j=\mathbb E\sigma^{(j)}(\sqrt\tau Z),\quad
C_j(\rho)=\mathbb E[\sigma(G)^j\sigma(\rho G+\sqrt{1-\rho^2}V)].
\]
Here \(m_0=1\), \(C_1=A_\rho\), and every displayed quantity is a Gaussian atom. The cases \(\rho=\pm1\) are allowed as degenerate jointly Gaussian pairs.

For real \(x,y\),
\[
|\tanh(x+iy)|^2
=\frac{\sinh^2x+\sin^2y}{\sinh^2x+\cos^2y}.
\]
Consequently, for any \(\alpha<r<\pi/2\), tanh is holomorphic on every radius-\(r\) disk about the real axis and is bounded there by
\[
M_r=\max\{1,\tan r\}.
\]
Cauchy's derivative formula gives
\[
\frac{|\sigma^{(j)}(x)|}{j!}\le M_rr^{-j}\qquad(x\in\mathbb R).
\]
Thus
\[
k_N(G,Z)=\sum_{j=0}^N\frac{\alpha^j}{j!}
 \sigma(G)^j\sigma^{(j)}(\sqrt\tau Z)
\]
converges uniformly to \(k\), with
\[
\|k-k_N\|_\infty\le
\varepsilon_N:=\frac{M_r(\alpha/r)^{N+1}}{1-\alpha/r}.
\tag{1}
\]
Uniform absolute convergence justifies expectations and all factorizations below. In particular,
\[
\beta=\sum_{j\ge0}\frac{\alpha^j}{j!}d_jm_{j+1},\qquad
B_\rho=\sum_{j\ge0}\frac{\alpha^j}{j!}d_jC_j(\rho).
\tag{2}
\]
The remainder of either series after degree \(N\) has absolute value at most \(\varepsilon_N\), uniformly in \(\rho\in[-1,1]\).

The identity \(\sigma'=1-\sigma^2\) also gives the especially short exact series
\[
\gamma=1-s
=\sum_{j\ge0}\frac{\alpha^j}{j!}d_{j+1}m_j.
\tag{3}
\]
Indeed \(|\sigma'(x+iy)|\le\sec^2r\) for \(|y|\le r\), so its Taylor-series remainder is bounded by
\[
\frac{\sec^2r(\alpha/r)^{N+1}}{1-\alpha/r}.
\]
Symmetry gives \(d_{2j}=m_{2j+1}=0\). Thus only odd indices survive in (2), and only even indices survive in (3).

For a finite computation, the following coherent Gram construction is preferable to separately truncating (3):
\[
\begin{aligned}
\beta_N&=\sum_{j=0}^N\frac{\alpha^j}{j!}d_jm_{j+1},\\
B_{N,\rho}&=\sum_{j=0}^N\frac{\alpha^j}{j!}d_jC_j(\rho),\\
s_N&=\sum_{i,j=0}^N\frac{\alpha^{i+j}}{i!j!}m_{i+j}e_{ij},\\
e_{ij}&=\mathbb E[\sigma^{(i)}(\sqrt\tau Z)\sigma^{(j)}(\sqrt\tau Z)],
\qquad \gamma_N=1-s_N.
\end{aligned}
\tag{4}
\]
These are exactly \(\mathbb E[\sigma(G)k_N]\), \(\mathbb E[k_N\sigma(G_\rho)]\), and \(\mathbb E k_N^2\). Therefore
\[
M_N=\begin{pmatrix}v+\eta&\beta_N\\\beta_N&s_N+\eta\end{pmatrix}
\succeq\eta I
\]
for every \(N\), even if a low-order approximation has \(s_N>1\). The inverse is always defined.

## 2. Certified propagation through the ridge inverse

Put \(t=\tau+\eta\),
\[
h=(\alpha v,\alpha\beta+\tau\gamma),\quad
F_\rho=(A_\rho,B_\rho)^\mathsf T,\quad
M=\begin{pmatrix}v+\eta&\beta\\\beta&s+\eta\end{pmatrix},
\]
and form \(h_N,F_{N,\rho}\) by the replacements in (4). Define
\[
\Lambda_N(\rho)=t^{-1}h_NM_N^{-1}F_{N,\rho}.
\tag{5}
\]
This is a finite expression in Gaussian atoms and elementary scalar operations. From (1), with \(\varepsilon=\varepsilon_N\),
\[
|\beta_N-\beta|,\ |B_{N,\rho}-B_\rho|\le\varepsilon,
\qquad |s_N-s|\le\delta:=\varepsilon(2+\varepsilon).
\]
Hence, in Euclidean/operator norm,
\[
\|h_N-h\|\le E:=\alpha\varepsilon+\tau\delta,
\quad \|M_N-M\|\le D:=\sqrt{2\varepsilon^2+\delta^2}.
\]
Since \(|\beta|\le1\), \(0\le\gamma\le1\), and \(\alpha+\tau=1\), we have \(\|h\|\le\sqrt2\). Also \(\|F_\rho\|\le\sqrt2\), \(\|F_{N,\rho}\|\le\sqrt2+\varepsilon\), and both inverse norms are at most \(1/\eta\). The resolvent identity then yields the uniform bound
\[
|\Lambda_N(\rho)-\Lambda(\rho)|\le \ell_N,
\qquad
\ell_N:=\frac1t\left[
\frac{E(\sqrt2+\varepsilon)}\eta
+\frac{\sqrt2D(\sqrt2+\varepsilon)}{\eta^2}
+\frac{\sqrt2\varepsilon}\eta\right].
\tag{6}
\]
For completeness, the three terms bound the decomposition
\[
t(\Lambda_N-\Lambda)
=(h_N-h)M_N^{-1}F_N
+h(M_N^{-1}-M^{-1})F_N+hM^{-1}(F_N-F).
\]
The bound is conservative but tends geometrically to zero.

## 3. A uniform bounded interval for the outer activation

For a particular angle \(\theta\), write
\[
a_{N,\theta}=\Lambda_N(\cos\theta),\qquad
b_{N,\theta}=\Lambda_N(\sin\theta).
\]
Because \(|H_i|\le1\), one may always use
\(R_{N,\theta}=|a_{N,\theta}|+|b_{N,\theta}|\).

There is also a useful angle-independent bound obtained entirely from the same atoms. Let
\[
(q_{N,A},q_{N,B})=t^{-1}h_NM_N^{-1},\qquad
\kappa_N=q_{N,A}^2v+2q_{N,A}q_{N,B}\beta_N+q_{N,B}^2s_N.
\]
Then
\[
R_N=\sqrt{2v\kappa_N}
\quad\hbox{satisfies}\quad
|a_{N,\theta}|+|b_{N,\theta}|\le R_N\quad\hbox{for all }\theta.
\tag{7}
\]
To prove (7), take independent copies \((G_i,Z_i)\), and set
\(L_i=q_{N,A}\sigma(G_i)+q_{N,B}k_N(G_i,Z_i)\).
The simultaneous sign reversal \((G_i,Z_i)\mapsto(-G_i,-Z_i)\) changes the sign of \(k_N\), hence \(\mathbb E L_i=0\). For \(u_1^2+u_2^2=1\), the joint-Gaussian marginal identities give
\[
\Lambda_N(u_i)=\mathbb E[L_i\sigma(u_1G_1+u_2G_2)].
\]
Choose \(\epsilon_i\in\{-1,1\}\) matching the signs of \(\Lambda_N(u_i)\). Independence and centering give \(\mathbb E(\epsilon_1L_1+\epsilon_2L_2)^2=2\kappa_N\); the other squared factor has expectation \(v\). Cauchy--Schwarz proves (7).

An optional sharper version integrates out \(Z\) first. Replace \(s_N\) in the definition of \(\kappa_N\) by
\[
\bar s_N=\sum_{i,j=0}^N
\frac{\alpha^{i+j}}{i!j!}d_id_jm_{i+j}
=\mathbb E\big(\mathbb E[k_N\mid G]\big)^2.
\]
The resulting \(\bar\kappa_N\) is the second moment of
\(q_{N,A}\sigma(G)+q_{N,B}\mathbb E[k_N\mid G]\).
The same proof gives \(\bar R_N=\sqrt{2v\bar\kappa_N}\), and conditional Jensen gives \(\bar\kappa_N\le\kappa_N\). The original \(s_N\), rather than \(\bar s_N\), still belongs in the ridge matrix (5).

## 4. Explicit geometric upper approximation

For any chosen \(R>0\), choose a strip height \(0<b<\pi/2\), and set
\[
\varrho=\frac{b+\sqrt{b^2+R^2}}R>1,
\qquad M_b=\max\{1,\tan b\}.
\]
The convenient fixed choice is \(b=1\). The ellipse parameter obeys
\(R(\varrho-\varrho^{-1})/2=b\).

For degree \(m\ge0\), put \(L=m+1\), \(\theta_k=(k+1/2)\pi/L\), and define the fully explicit coefficients
\[
c_j=\frac2L\sum_{k=0}^{L-1}
 \tanh(R\cos\theta_k)\cos(j\theta_k),\qquad 0\le j\le m.
\]
These are deterministic scalar coefficients. If desired, every tanh here may be written explicitly as \((e^{2R\cos\theta_k}-1)/(e^{2R\cos\theta_k}+1)\); no random non-Gaussian argument occurs. Define
\[
P_{m,R}(x)=\frac{c_0}2+\sum_{j=1}^m c_jT_j(x/R),
\tag{8}
\]
where \(T_0(t)=1\), \(T_1(t)=t\), and \(T_{j+1}(t)=2tT_j(t)-T_{j-1}(t)\). Then
\[
\sup_{|x|\le R}|\sigma(x)-P_{m,R}(x)|
\le e_{m,R}:=\frac{4M_b\varrho^{-m}}{\varrho-1}.
\tag{9}
\]

Here is a direct proof of the approximation estimate. The function
\(w\mapsto\tanh(R(w+w^{-1})/2)\) is holomorphic on a neighborhood of the closed annulus \(\varrho^{-1}\le|w|\le\varrho\), and its modulus on the bounding circles is at most \(M_b\). Cauchy's Laurent coefficient formula bounds its degree-\(j\) Laurent coefficient by \(M_b\varrho^{-j}\). The degree-\(j\ge1\) Chebyshev coefficient is twice this, so its magnitude is at most \(2M_b\varrho^{-j}\). This proves absolute uniform convergence of the Chebyshev series on the real interval. Interpolation at the roots used in (8) fixes each \(T_j\) of degree at most \(m\). For every higher \(j\), its nodal values alias to either zero or a signed \(T_r\), \(0\le r\le m\), because \(\cos((2L\pm r)\theta_k)=-\cos(r\theta_k)\) and \(\cos(L\theta_k)=0\). Thus the interpolant of any \(T_j\) has sup norm at most one. The interpolation error is consequently bounded by twice the Chebyshev-series tail:
\[
2\sum_{j=m+1}^\infty 2M_b\varrho^{-j}
=\frac{4M_b\varrho^{-m}}{\varrho-1}.
\]
This also establishes (8) as the interpolating polynomial by the discrete cosine orthogonality at the root nodes.

For \(R=0\), the relevant outer argument is identically zero, and one simply sets its polynomial and error to zero.

## 5. Finite Gaussian-atom formula for the kernel

Use any positive common bound \(R_N\) valid in (7), its sharper conditional version, or the maximum of the two angle-specific bounds. Write the monomial expansion
\[
P_{m,R_N}(x)=\sum_{p=0}^m p_px^p.
\]
Its coefficients can be generated without symbolic integration. If \(T_j(t)=\sum_l t_{j,l}t^l\), initialize \(t_{0,0}=1\), \(t_{1,1}=1\), take out-of-range entries to be zero, and use
\[
t_{j+1,l}=2t_{j,l-1}-t_{j-1,l},\qquad
p_l=\mathbf1_{l=0}\frac{c_0}2+
R_N^{-l}\sum_{j=1}^m c_jt_{j,l}.
\tag{10}
\]
Define the remaining Gaussian moments
\(\mu_j=\mathbb E\sigma(\sqrt vX)^j\), with \(\mu_0=1\).
Then the finite approximation to the requested kernel is exactly
\[
\begin{aligned}
K_{N,m}(\theta,\phi)
={}&\sum_{p,q=0}^m p_pp_q
\sum_{a=0}^p\sum_{b=0}^q
 {p\choose a}{q\choose b}
 a_{N,\theta}^{a}b_{N,\theta}^{p-a}
 a_{N,\phi}^{b}b_{N,\phi}^{q-b}\\
&\hspace{30mm}\cdot\mu_{a+b}\mu_{p+q-a-b}.
\end{aligned}
\tag{11}
\]
The formula follows by two binomial expansions and independence of \(H_1,H_2\). It contains only finitely many of the Gaussian atoms defined above, plus deterministic scalar operations. It contains no activation evaluated at a nonlinear random argument. Different valid radii for the two angles merely replace \(p_pp_q\) by their two separate monomial-coefficient arrays.

Because tanh is 1-Lipschitz on the real line and is bounded by one, replacing both coefficient pairs by their \(N\)-approximations changes the exact outer kernel by at most \(4\ell_N\). If (9) gives errors \(e_\theta,e_\phi\) for the two polynomial approximations, expansion of their product gives the final certified error
\[
|K_{N,m}(\theta,\phi)-K(\theta,\phi)|
\le4\ell_N+e_\theta+e_\phi+e_\theta e_\phi.
\tag{12}
\]
With a common radius and degree this is \(4\ell_N+2e_{m,R_N}+e_{m,R_N}^2\).

As \(N\to\infty\), all quantities in (4)--(7) converge, so the chosen global radii remain bounded. Therefore the geometric estimate (9) tends to zero as \(m\to\infty\), also along any diagonal \(N,m\to\infty\). Equations (1)--(12) prove the exact limiting representation
\[
K(\theta,\phi)=\lim_{N,m\to\infty}K_{N,m}(\theta,\phi),
\]
with uniform control over the angles when a global radius is used. Each finite stage is an explicitly specified finite Gaussian-atom expression.

## 6. What does and does not terminate

Even derivative atoms can be reduced to activation moments by the finite recurrence
\[
Q_0(t)=t,\qquad Q_{j+1}(t)=(1-t^2)Q_j'(t),\qquad
\sigma^{(j)}(x)=Q_j(\sigma(x)).
\]
Thus each fixed truncation can use derivative order zero alone, at the cost of moments of increasing degree. This is a finite recursion for every requested degree, followed by a convergent infinite-degree limit.

It is not an exact finite polynomial closure. For a nonzero shift coefficient, the map \(t\mapsto\tanh(y+\alpha t)\) is not a polynomial on any open interval: equality with a polynomial there would, by analyticity, force equality throughout the connected real line, whereas tanh has finite unequal limits at the two ends and a polynomial cannot. The analogous fact holds for a nonconstant outer linear argument. Consequently, no finite-degree universal pointwise polynomial peeling identity can replace these limits. This observation does not rule out arbitrary exceptional scalar identities or unrelated representations; it identifies exactly why the present algebraic hierarchy is infinite.
