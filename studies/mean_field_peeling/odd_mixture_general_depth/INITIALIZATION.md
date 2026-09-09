# The exact odd mixture at general depth: sharp initialization bounds and the remaining global question

This report uses exactly
\[
\phi_\theta(z)=(1-\theta)z+\theta\arctan z,
\qquad 0<\theta\le1.
\]
There are three inputs, and depth \(L\) is the number of hidden layers. No offset, gain change, or variance normalization is introduced.

**Status of the requested theorem.** A sufficient positive bound \(\theta_*(\delta,L)\) for the full global joint trained limit has not been established here. Neither has the existence or impossibility of a depth-independent sufficient bound \(\theta_*(\delta)>0\). The results proved below are a sharp arbitrary-depth initialization theorem and, in Part II, a conditional continuation criterion. The additional hypothesis in the latter remains unproved for the canonical trained system. In particular, the initialization theorem is not presented as a training theorem.

The strongest unconditional quantitative result is
\[
\inf_{\text{admissible triples}}\lambda_{\min}(Q_L(0))
\asymp \frac{\delta^2\theta^2 L}{(1+\theta L)^2}
\quad(0<\delta\le1/4, 0<\theta\le1, L\ge1),
\]
where the comparison constants are universal. This determines the sharp powers jointly in separation, mixture size and depth. It does not determine the sharp scale of a sufficient training cutoff.

## Exact finite model and initialization identification

Fix \(d\ge2\), \(L\ge1\), labels \(y_i\in\{-1,1\}\), and \(x_i\in\mathbb R^d\) with \(\|x_i\|^2=d\). Write \(u_i=x_i/\sqrt d\) and \(\Gamma_{ij}=u_i\cdot u_j\). Assume
\[
-1+\delta<\Gamma_{ij}<1-\delta\quad(i\ne j),\qquad 0<\delta<1.
\]
All assertions quantify only over realizable triples. In dimension one no triple is admissible, so it is excluded from the infima below.

At width \(n\), let all initialized entries be mutually independent:
\[
W^1_{ab}\sim N(0,1/d),\quad W^\ell_{ab}\sim N(0,1/n)\ (2\le\ell\le L),
\quad C_a\sim N(0,n^{-2}).
\]
Set \(z_i^1=W^1x_i\), \(h_i^\ell=\phi_\theta(z_i^\ell)\), \(z_i^{\ell+1}=W^{\ell+1}h_i^\ell\), and
\[
f_i=n^{-1}C^Th_i^L,\quad r_i=f_i-y_i,\quad \mathcal L=\tfrac12\sum_{i=1}^3r_i^2.
\]
For normalized vector inner products \(\langle v,w\rangle_n=n^{-1}v^Tw\), the raw increment metric is
\[
\|\Delta\Theta\|_{{\rm raw},n}^2
=\frac dn\|\Delta W^1\|_F^2+
\sum_{\ell=2}^L\|\Delta W^\ell\|_F^2+\|\Delta C\|_n^2.
\]
The true backward fields are \(b_i^L=C\phi_\theta'(z_i^L)\) and
\(b_i^\ell=\phi_\theta'(z_i^\ell)(W^{\ell+1})^Tb_i^{\ell+1}\). The exact raw gradient flow is
\[
\dot W^1=-d^{-1}\sum_i r_i b_i^1x_i^T,\quad
\dot W^\ell=-n^{-1}\sum_i r_i b_i^\ell(h_i^{\ell-1})^T\ (\ell\ge2),
\quad\dot C=-\sum_i r_i h_i^L.
\]
These factors follow by differentiating \(\mathcal L\) and applying the inverse block metric. Raw GD means simultaneous Euler for this same field with step \(n^{-2}\); its raw parameters are interpolated and hidden fields recomputed. The target width limit keeps \(L\) and every observation horizon fixed before width tends to infinity.

At every finite width GF exists for all finite times. Its field is smooth and locally Lipschitz. Along a local solution,
\[
\mathcal L(t)+\int_0^t\|\dot\Theta(s)\|_{{\rm raw},n}^2ds=\mathcal L(0).
\]
Thus finite-time displacement is bounded by \(\sqrt{t\mathcal L(0)}\), and increments approaching a finite endpoint are Cauchy by the same inequality. The finite-dimensional limit is a permissible state, from which local existence continues the solution. GD is defined at every finite node because its update is everywhere smooth. These finite-width facts do not assert convergence as width grows.

**Initialization lemma.** At every separately fixed depth, the initialized empirical feature Gram converges in probability to the recursively defined \(Q_\ell\) in Part I. All initial hidden kernel blocks tend to zero, and the initial readout kernel tends to \(Q_L\); hence the initialized total raw prediction kernel has limit \(Q_L\).

**Proof.** At layer one the neuron tuples \((z_{a,1}^1,z_{a,2}^1,z_{a,3}^1)\) are independent copies of \(N(0,\Gamma)\). The covariance products after activation have finite variance, since \(|\phi_\theta(z)|\le|z|\). Their averages converge by Chebyshev's inequality.

Conditionally on all preceding layers, each next-layer preactivation tuple is Gaussian with covariance the preceding empirical feature Gram, and the rows are conditionally independent. On the event that this Gram's diagonal is bounded by \(M\), every conditional variance of a product of two activated coordinates is at most \(3M^2\), by Cauchy--Schwarz and the Gaussian fourth moment. Chebyshev's inequality bounds the conditional mean-square averaging error by \(3M^2/n\). The bounded-diagonal event has probability tending to one for a sufficiently large fixed \(M\), by the induction hypothesis. The conditional expected product depends continuously on the covariance, including at singular matrices: couple Gaussians by their positive square roots, use continuity of the finite-dimensional positive square root, and apply the activation's 1-Lipschitz bound and Cauchy--Schwarz. This proves the finite induction, jointly across the finitely many layers and entries.

For completeness, the initialized square matrices have operator norms at most ten with probability tending to one. Choose a \(1/4\)-net of each Euclidean unit sphere with at most \(9^n\) elements (disjoint radius-\(1/8\) balls around a maximal separated family give this volume bound). Approximating the two vectors in the bilinear supremum shows \(\|W\|_{\rm op}\le2\max_{u,v\text{ in nets}}|u^TWv|\). Each net pairing is \(N(0,1/n)\), so the event \(\|W\|_{\rm op}>10\) has probability at most \(2\cdot9^{2n}e^{-25n/2}\), which vanishes. There are only finitely many layers.

Since \(|\phi_\theta'|\le1\), backward propagation gives
\(\|b_i^\ell(0)\|_n\le\|C(0)\|_n\prod_{j=\ell+1}^L\|W^j(0)\|_{\rm op}\).
Here \(E\|C(0)\|_n^2=n^{-2}\), so these norms are \(O_{\mathbb P}(n^{-1})\) at fixed depth. Initial feature norms are bounded in probability by the Gram induction. The raw kernel blocks are
\[
K^1_{ij}=\Gamma_{ij}\langle b_i^1,b_j^1\rangle_n,\qquad
K^\ell_{ij}=\langle b_i^\ell,b_j^\ell\rangle_n
\langle h_i^{\ell-1},h_j^{\ell-1}\rangle_n\ (2\le\ell\le L),
\quad K^{L+1}_{ij}=\langle h_i^L,h_j^L\rangle_n.
\]
The hidden blocks consequently vanish, and the readout block has the stated limit. \(\square\)

# Part I. Sharp initialized conditioning at arbitrary depth

The activation in this note is exactly
\[
\phi_\theta(z)=(1-\theta)z+\theta\arctan z,
\qquad 0<\theta\le1.
\]
There is no additive constant or gain. The results below concern Gaussian initialization only. They neither establish nor refute the requested global trained-flow theorem.

Let \(u_1,u_2,u_3\in\mathbb R^d\), \(d\ge2\), be unit vectors, and let \(\Gamma_{ij}=u_i\cdot u_j\). Assume the strict separation
\[
-1+\delta<\Gamma_{ij}<1-\delta\quad(i\ne j).
\]
Set \(Q_0=\Gamma\), \(q_0=1\), and recursively let \(Z^\ell\) be a centered Gaussian triple with covariance \(Q_{\ell-1}\), and
\[
Q_\ell=E[\phi_\theta(Z^\ell)\phi_\theta(Z^\ell)^T],
\qquad q_\ell=(Q_\ell)_{ii}.
\]
The scalar variance does not depend on the sample or on the off-diagonal geometry. Write \(C_\ell=Q_\ell/q_\ell\).

**Sharp joint-order theorem.** Let \(\Lambda_L(\theta,\delta;d)\) be the infimum of \(\lambda_{\min}(Q_L)\) over these strictly admissible triples in dimension \(d\). For every integer \(L\ge1\), \(0<\theta\le1\), and \(0<\delta\le1/4\),
\[
\frac{e^{-80/3}}{73728}\,
\frac{\delta^2\theta^2 L}{(1+\theta L)^2}
\ \le\ \Lambda_L(\theta,\delta;d)
\ \le\ 11520e^{128/3}\,
\frac{\delta^2\theta^2 L}{(1+\theta L)^2}.
\tag{A}
\]
The constants are deliberately coarse. Thus the small-separation exponent is exactly two at every depth, with joint depth/nonlinearity order
\(\delta^2\theta^2L/(1+\theta L)^2\). In particular, first-layer conditioning has sharp order \(\theta^2\delta^2\). The lower estimate applies to every admissible triple; the upper estimate uses an explicit planar triple that can be embedded in every \(d\ge2\).

The normalized version is
\[
\inf\lambda_{\min}(C_L)
\asymp\frac{\delta^2\theta^2 L}{1+\theta L},
\tag{B}
\]
with universal comparison constants and the same parameter ranges. Consequently, for a fixed positive \(\theta\) and fixed separation, normalized initialized conditioning remains bounded below uniformly over \(L\ge1\), whereas absolute conditioning necessarily tends to zero as depth increases.

## 1. Scalar variance estimates

Put \(h(z)=z-\arctan z\), and for \(0<q\le1\), let
\[
m(q)=E(1+qG^2)^{-1},\qquad
c(q)=1-\theta+\theta m(q),\qquad G\sim N(0,1).
\]
Gaussian integration by parts gives
\(E[\sqrt qG\arctan(\sqrt qG)]=qm(q)\).
The coefficient of the projection of \(\phi_\theta(\sqrt qG)\) onto \(\sqrt qG\) is therefore \(c(q)\). Since the function \(t\mapsto(1+qt)^{-1}\) is convex,
\[
c(q)\ge1-\theta+\frac{\theta}{1+q}\ge\frac12.
\tag{1}
\]
If \(q_+=E\phi_\theta(\sqrt qG)^2\), then projection gives \(q_+\ge q/4\). Also \(0<q_+<q\), because \(|\phi_\theta(z)|<|z|\) for every nonzero \(z\).

For \(Z=\sqrt qG\), the decrement is
\[
D(q):=q-q_+=2\theta E[Zh(Z)]-\theta^2E[h(Z)^2].
\]
The inequalities \(0\le h(z)^2\le zh(z)\) and
\(E[Zh(Z)]=q(1-m(q))\) yield
\[
\theta(2-\theta)q(1-m(q))\le D(q)\le2\theta q(1-m(q)).
\]
Cauchy--Schwarz applied to
\(|G|/\sqrt{1+qG^2}\) and \(|G|\sqrt{1+qG^2}\) gives
\[
\frac{q}{1+3q}\le1-m(q)
=qE\frac{G^2}{1+qG^2}\le q.
\]
Consequently
\[
\frac\theta4q^2\le D(q)\le2\theta q^2,
\qquad
\frac\theta4\le\frac1{q_+}-\frac1q\le8\theta.
\tag{2}
\]
Iteration and telescoping give
\[
\frac1{1+8\theta\ell}\le q_\ell
\le\frac1{1+\theta\ell/4},
\tag{3}
\]
\[
\sum_{k=0}^{L-1}q_k^2\le\min\{L,4/\theta\}
\le\frac{5L}{1+\theta L},
\qquad
\sum_{k=0}^{L-1}q_k^2\ge\frac{L}{1+8\theta L}.
\tag{4}
\]
The last inequality follows by comparing the decreasing function
\((1+8\theta x)^{-2}\) with its integral on \([0,L]\).

## 2. Gaussian correlation kernels and their derivatives

Use the probabilists' Hermite polynomials \(H_n\), defined by
\[
e^{tx-t^2/2}=\sum_{n\ge0}H_n(x)t^n/n!,
\qquad h_n=H_n/\sqrt{n!}.
\]
For standard normal \(G\), comparison of coefficients in
\(E[e^{sG-s^2/2}e^{tG-t^2/2}]=e^{st}\) proves
\(E[h_n(G)h_m(G)]=1_{n=m}\). These polynomials form a complete orthonormal system in Gaussian \(L^2\): if a function is orthogonal to every polynomial, the generating series at imaginary arguments, which converges in Gaussian \(L^2\), shows that its Gaussian-weighted Fourier transform vanishes; uniqueness of the Fourier transform of a finite signed measure gives the claim. Finiteness of that signed measure follows from Cauchy--Schwarz. Here is a direct verification of the uniqueness step. If its integrable density is \(v\) and its Fourier transform vanishes, convolution with the Gaussian density of variance \(s>0\) is zero: insert the Gaussian Fourier integral and use Fubini, whose absolute integral is bounded by \(\|v\|_1\int e^{-s\xi^2/2}d\xi\). These convolutions tend to \(v\) in \(L^1\) as \(s\downarrow0\); this follows by integrating \(\|v(\cdot-y)-v\|_1\) against the Gaussian kernel and using translation continuity in \(L^1\), first for bounded interval step functions and then by their density. Hence \(v=0\). The generating series used above converges in Gaussian \(L^2\) at every imaginary argument because its squared coefficient norms sum to \(\sum_{n\ge0}t^{2n}/n!=e^{t^2}\); its pointwise entire-function sum identifies that \(L^2\) limit. Thus no completeness or Gaussian-kernel theorem is left as an unproved specialized invocation.

If \((X,Y)\) is a standard Gaussian pair with correlation \(\rho\in[-1,1]\), the same generating-function calculation gives
\[
E[h_n(X)h_m(Y)]=1_{n=m}\rho^n.
\tag{5}
\]
This calculation includes the degenerate pairs at \(\rho=\pm1\). Polynomial approximation and Cauchy--Schwarz extend the formula to Gaussian \(L^2\) functions.

Expand \(f_q(x)=\phi_\theta(\sqrt qx)=\sum a_n(q)h_n(x)\). This is an odd function, so only odd \(n\ge1\) occur. Its squared norm is \(q_+\). Thus its normalized correlation kernel is
\[
K_q(\rho)=\frac{E[f_q(X)f_q(Y)]}{q_+}
=\sum_{n\text{ odd}}w_n(q)\rho^n,
\qquad w_n(q)=\frac{a_n(q)^2}{q_+},
\quad \sum_nw_n(q)=1.
\tag{6}
\]
All coefficients are nonnegative. Hence \(|K_q(\rho)|\le|\rho|\), and the normalized covariances satisfy
\[
(C_\ell)_{ij}=K_{q_{\ell-1}}((C_{\ell-1})_{ij}),
\qquad |(C_\ell)_{ij}|\le|\Gamma_{ij}|.
\tag{7}
\]
In particular absolute pairwise separation persists at every initialized depth.

The first two derivatives of \(f_q\) are bounded. Integration by parts gives
\(\langle f_q',h_{n-1}\rangle=\sqrt n\,a_n(q)\) and
\(\langle f_q'',h_{n-2}\rangle=\sqrt{n(n-1)}\,a_n(q)\).
Parseval therefore gives
\[
\sum_n n a_n(q)^2=qE\phi_\theta'(\sqrt qG)^2,
\quad
\sum_n n(n-1)a_n(q)^2=q^2E\phi_\theta''(\sqrt qG)^2.
\]
The series have nonnegative terms and finite sums, so monotone convergence as \(\rho\uparrow1\) justifies the derivatives at one:
\[
K_q'(1)=\frac{qE\phi_\theta'(\sqrt qG)^2}{q_+},
\qquad
K_q''(1)=\frac{q^2E\phi_\theta''(\sqrt qG)^2}{q_+}.
\tag{8}
\]
This also proves continuity of the first two derivatives up to that endpoint.

## 3. Uniform retention of first-chaos covariance

The first coefficient is \(a_1(q)=\sqrt q\,c(q)\). Write
\[
R(q)=q_+-q c(q)^2\ge0,
\qquad w_1(q)=\frac{q c(q)^2}{q_+}.
\]
Since an orthogonal projection minimizes its squared error, and
\(|h(z)|\le|z|^3/3\),
\[
R(q)\le E|\phi_\theta(\sqrt qG)-\sqrt qG|^2
\le\frac53\theta^2q^3.
\]
Using (1),
\[
-\log w_1(q)
=\log\left(1+\frac{R(q)}{q c(q)^2}\right)
\le\frac{20}{3}\theta^2q^2.
\]
By (4), every product of first-chaos weights from a consecutive set of initialized layers is bounded below by
\[
p_*:=e^{-80/3}.
\tag{9}
\]
Indeed the sum of \(\theta^2q_k^2\) over all layers is at most \(4\theta\le4\). This finite total is the reason first-layer distinctions survive normalization at arbitrary depth.

## 4. Cubic lifting and injection at every layer

Let \(C\) be any three-by-three Gram matrix of unit vectors with
\(|C_{ij}|\le1-\delta\). Put \(s_\delta=\delta(2-\delta)\). For unit representatives \(v_i\), define
\[
v_{ij}=\frac{v_i-C_{ij}v_j}{\sqrt{1-C_{ij}^2}},
\qquad
R_i=v_i\otimes v_{ij}\otimes v_{ik},
\quad \{i,j,k\}=\{1,2,3\}.
\]
The vector \(R_i\) has norm one, is orthogonal to \(v_j^{\otimes3}\) and \(v_k^{\otimes3}\), and has inner product at least \(s_\delta\) with \(v_i^{\otimes3}\). Hence for \(T=\sum c_i v_i^{\otimes3}\),
\(|c_i|s_\delta\le\|T\|\). Summing squares gives
\[
C^{\circ3}\succeq\frac{s_\delta^2}{3}I_3.
\tag{10}
\]
No invertibility of \(C\) is needed.

For the cubic coefficient of arctangent, integration by parts twice gives
\[
b_3(q):=E[\arctan(\sqrt qG)h_3(G)]
=-\sqrt{\frac23}\,q^{3/2}
E\frac{G^2}{(1+qG^2)^2}.
\tag{11}
\]
For detail, the first integration changes \(H_3\) to \(G^2-1\) and contributes \(\sqrt q/(1+qG^2)\); the identity
\(E[(G^2-1)r(G)]=E[Gr'(G)]\), applied to \(r(G)=(1+qG^2)^{-1}\), contributes \(-2qG^2/(1+qG^2)^2\).

The measure with density \(G^2\) relative to standard Gaussian measure is a probability measure, and under it \(E[G^2]=3\). Jensen applied to the convex function \(t\mapsto(1+qt)^{-2}\) gives
\[
E\frac{G^2}{(1+qG^2)^2}\ge\frac1{(1+3q)^2}\ge\frac1{16}.
\]
Consequently
\[
b_3(q)^2\ge\frac{q^3}{384},
\qquad
w_3(q)=\frac{\theta^2b_3(q)^2}{q_+}
\ge\frac{\theta^2q^2}{384}.
\tag{12}
\]

Each entrywise integer power of a Gram matrix is another Gram matrix, via tensor powers. Equations (6), (7), and (10) therefore give
\[
C_\ell\succeq w_1(q_{\ell-1})C_{\ell-1}
+\frac{s_\delta^2}{3}w_3(q_{\ell-1})I_3.
\]
Iterating, discarding the positive semidefinite propagated \(C_0\), and using (9), (12), and (4), yields
\[
\lambda_{\min}(C_L)
\ge\frac{p_*s_\delta^2\theta^2}{1152}
\sum_{k=0}^{L-1}q_k^2
\ge\frac{p_*s_\delta^2\theta^2L}{1152(1+8\theta L)}.
\tag{13}
\]
Multiplication by the lower bound for \(q_L\) in (3) gives
\[
\lambda_{\min}(Q_L)
\ge\frac{p_*s_\delta^2\theta^2L}{1152(1+8\theta L)^2}.
\tag{14}
\]
Since \(s_\delta\ge\delta\) for \(0<\delta\le1\), and
\(1+8\theta L\le8(1+\theta L)\), this proves the lower side of (A). It also proves finite-depth positive definiteness for the entire separation range, including singular input Grams.

## 5. Composed-kernel curvature and a matching strict example

Let
\[
F_0(\rho)=\rho,
\qquad F_\ell=K_{q_{\ell-1}}\circ F_{\ell-1}.
\]
Then \((C_L)_{ij}=F_L(\Gamma_{ij})\). Composition preserves an expansion
\[
F_L(\rho)=\sum_{n\text{ odd}}p_{n,L}\rho^n,
\qquad p_{n,L}\ge0,\qquad \sum_np_{n,L}=1.
\tag{15}
\]
All rearrangements of these nonnegative coefficient series are justified by monotone convergence, first for \(\rho\in[0,1)\), then by absolute convergence for \(\rho\in[-1,1]\).

Write \(d_k=K_{q_k}'(1)\), \(b_k=K_{q_k}''(1)\). Since
\(\phi_\theta''(z)=-2\theta z/(1+z^2)^2\), (8) and \(q_{k+1}\ge q_k/4\) imply
\[
0\le b_k\le16\theta^2q_k^2.
\]
Because all non-linear degrees are odd and at least three,
\[
1\le d_k=\sum_n n w_n(q_k),
\qquad d_k-1\le b_k/3.
\tag{16}
\]
Thus \(\sum b_k\le64\) and \(\sum(d_k-1)\le64/3\).

For \(A_\ell=F_\ell'(1)\) and \(B_\ell=F_\ell''(1)\), the ordinary chain rule gives
\[
A_{\ell+1}=d_\ell A_\ell,
\qquad B_{\ell+1}=b_\ell A_\ell^2+d_\ell B_\ell.
\]
Here \(A_0=1,B_0=0\). Dividing the second equality by \(A_{\ell+1}\) and iterating gives the exact identity
\[
B_L=A_L\sum_{k=0}^{L-1}\frac{b_k}{d_k}A_k.
\]
Since \(A_k\le\exp(\sum(d_j-1))\le e^{64/3}\), equations (4) and (16) give
\[
F_L''(1)\le16e^{128/3}\theta^2\sum_{k=0}^{L-1}q_k^2
\le80e^{128/3}\frac{\theta^2L}{1+\theta L}.
\tag{17}
\]

Now choose \(c=1-2\delta\), \(0<\delta\le1/4\), and the planar triple
\[
u_+=(c,\sqrt{1-c^2}),\qquad u_0=(1,0),\qquad
u_-=(c,-\sqrt{1-c^2}).
\tag{18}
\]
The three off-diagonal inner products are \(c,c,r\), where
\(r=2c^2-1=1-8\delta+8\delta^2\). The strict inequalities for \(c\) follow from
\((1-\delta)-c=\delta>0\) and \(c-(-1+\delta)=2-3\delta>0\). For \(r\),
\[
(1-\delta)-r=\delta(7-8\delta)>0,
\quad r-(-1+\delta)=2-9\delta+8\delta^2
=(1-4\delta)(2-2\delta)+\delta>0.
\]
This is therefore an admissible example for the strict class, including its endpoint \(\delta=1/4\).

Use \(v=(1,-2c,1)^T\), whose squared norm is \(2+4c^2\ge3\). For every odd degree \(n\),
\[
E_n(c):=v^T\Gamma^{\circ n}v
=2+4c^2+2(2c^2-1)^n-8c^{n+1}.
\tag{19}
\]
For \(n=1\), this is identically zero. For odd \(n\ge3\), both \(E_n(1)=0\) and \(E_n'(1)=0\). On \(1/2\le c\le1\), differentiation gives
\[
E_n''(c)=8+8n(2c^2-1)^{n-1}
+32n(n-1)c^2(2c^2-1)^{n-2}
-8n(n+1)c^{n-1}.
\]
Since \(|2c^2-1|\le1\),
\[
|E_n''(c)|\le40n^2-16n+8\le54n(n-1)\quad(n\ge3).
\]
Taylor's formula with integral remainder gives
\(0\le E_n(c)\le27n(n-1)(1-c)^2\). Summing with the nonnegative coefficients in (15),
\[
\lambda_{\min}(Q_L)
\le\frac{q_L\sum_np_{n,L}E_n(c)}{2+4c^2}
\le9q_L(1-c)^2F_L''(1)
=36q_L\delta^2F_L''(1).
\tag{20}
\]
Using (17) and \(q_L\le4/(1+\theta L)\) proves the upper side of (A). Omitting the factor \(q_L\) in (20), and combining (13) with (17), proves (B). This proof treats all regimes of \(L\theta\); it does not replace the composed kernel by its first-layer approximation.

## 6. What depth does to scalar nonaffinity

For each fixed \(\theta>0\), (2) implies \(q_\ell\downarrow0\). A sharper expansion gives
\[
q_\ell\sim\frac1{2\theta\ell}.
\tag{21}
\]
To verify the coefficient without a formal series argument, use
\(1-m(q)\sim q\) by dominated convergence and
\(E[h(\sqrt qG)^2]\le(5/3)q^3\). Thus \(D(q)/q^2\to2\theta\), and \(q_+/q\to1\). Therefore
\(q_{\ell+1}^{-1}-q_\ell^{-1}\to2\theta\); averaging these increments proves (21).

For a Gaussian scalar \(Z=\sqrt qG\), define the arctangent affine-regression gap
\[
\mathcal R(q)=\inf_{\alpha,\beta}E[\arctan Z-\alpha-\beta Z]^2.
\]
For every \(q>0\), \(\mathcal R(q)>0\): equality would make arctangent affine almost everywhere under a positive Gaussian density, hence everywhere by continuity, contradicting its nonconstant derivative. Nevertheless,
\[
\mathcal R(q)\sim\frac23q^3\qquad(q\downarrow0).
\tag{22}
\]
Indeed
\[
\left|\arctan z-z+z^3/3\right|\le|z|^5/5
\]
follows by integrating the exact remainder in \((1+t^2)^{-1}=1-t^2+t^4/(1+t^2)\). Gaussian \(L^2\) projection onto constants and \(G\) then gives
\[
\arctan(\sqrt qG)-\operatorname{Proj}_{\{1,G\}}
\arctan(\sqrt qG)
=-\frac{q^{3/2}}3H_3(G)+O_{L^2}(q^{5/2}).
\]
Since \(EH_3(G)^2=6\), (22) follows. The regression gap for the full activation is exactly \(\theta^2\mathcal R(q)\).

Accordingly, in layer \(\ell\), its initial preactivation variance is \(q_{\ell-1}\), and its activation's absolute regression gap is of order \(\theta^2q_{\ell-1}^3\). It tends to zero with depth; for fixed \(\theta\), it is asymptotic to \(1/(12\theta\ell^3)\). Even its fraction of the feature variance tends to zero, asymptotically as \(1/(6\ell^2)\). This is compatible with the positive normalized sample-Gram bound (B): distinctions injected at earlier depths persist, although the new nonlinearity introduced at a very deep layer is small.

## 7. Consequences and limits for the actual requested theorem

1. For every finite depth and every positive mixture, absolute pairwise separation implies \(Q_L\succ0\), even if \(\Gamma\) is singular. The optimal small-\(\delta\) power remains two after antipodal exclusion. The quantitative depth dependence is given by (A).
2. No positive absolute initialized covariance lower bound or scalar nonaffinity margin can hold uniformly over all depths with the same numerical constant: \(\lambda_{\min}(Q_L)\le q_L\to0\), and (22) already rules out such a margin at physical time zero.
3. This does **not** disprove the existence of one positive nonlinear parameter that works for every finite depth. Such a theorem could permit depth-dependent coercivity and regression-gap constants. Initialization alone supplies no all-time preservation of those constants.
4. A positive initial sample Gram does not establish canonical population-flow existence, source-tail bounds, uniqueness against all strong competitors, cap removal, or long-time trained-law nonaffinity. Those require dynamical arguments. The covariance recursion used here is valid at independent Gaussian initialization; it is not a recursion for the trained feature laws.
5. The zero-mixture affine obstruction is real and survives the stronger geometry. For \(\theta=0\), \(Q_L=\Gamma\) at every depth, and every bias-free affine network remains linear in the input at every parameter state. The equilateral planar triple with pairwise correlation \(-1/2\) is strictly admissible for \(0<\delta<1/2\), has \(\Gamma\mathbf1=0\), and cannot fit labels \((1,1,1)\). With the population-zero readout, its affine trajectory is stationary: the three feature sums are zero at every layer, so the readout derivative is zero, while every hidden derivative contains the zero readout as a factor. The affine field is a polynomial map on bounded primal balls and is locally Lipschitz, which gives uniqueness of this stationary solution. This obstructs that affine reference proof, not the positive-mixture theorem.
6. The odd mixture has zero Gaussian mean, so its Hermite expansion has no constant component. An argument that requires a positive constant-feature covariance term cannot insert that term into this model. The positive lift proved here instead comes from its cubic coefficient.

The proved conclusion is the sharp joint depth/nonlinearity initialization scale and the distinction between absolute and normalized depth-uniform conditioning. No assertion of a global trained limit is inferred from these calculations.
