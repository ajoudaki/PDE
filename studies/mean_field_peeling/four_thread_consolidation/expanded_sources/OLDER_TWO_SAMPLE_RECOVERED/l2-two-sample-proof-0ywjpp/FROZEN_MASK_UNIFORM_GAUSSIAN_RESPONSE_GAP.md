# A mesh-independent Gaussian response gap from a frozen initial subset

Root candidate, 2026-09-06. UNVERIFIED. This is a theorem about a
specified finite causal Gaussian population program, with a strict
response contraction independent of the number of time nodes. It does
not prove global population continuation, or identify the full raw-GD
limit. The final section explains precisely which feedback operators
are, and are not, bounded by this argument.

The construction is motivated by smooth first-layer saturation.
Unlike a gate-margin argument, it allows the first derivative to vanish.
It does not regard frozen neurons as evidence of nonlazy dynamics.
No experiment or external theorem is used.

## 1. The first population program and its mask

Choose once and for all \(0<R<1/4\), and a smooth even function
\(\phi_1'\) positive on \((-R,R)\) and zero on its complement. For example,
\[
 \phi_1'(z)=
 \begin{cases}\exp[-1/(1-(z/R)^2)],&|z|<R,\\0,&|z|\ge R,\end{cases}
 \qquad \phi_1(z)=\int_0^z\phi_1'(u)\,du.                 \tag{1}
\]
All derivatives are bounded; at a support endpoint each derivative
is a finite sum of powers of \(1/(1-(z/R)^2)\) times the decaying
exponential, hence tends to zero. The function \(\phi_1\) is bounded,
odd, and nonaffine. Its saturation value is
\(B=\int_0^R\phi_1'(u)\,du>0\).
The chosen activation is the same for every input correlation.

Fix any covariance \(C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\)
with \(-1\le\rho<1\). Let \(G=(G_1,G_2)\sim N(0,C)\).
Fix a finite node count \(N+1\). Let
\(\zeta=(\zeta_{k,a})_{0\le k\le N,\ a=1,2}\) be centered Gaussian
with an arbitrary positive semidefinite covariance matrix \(\Sigma\),
independent of \(G\). Singular covariances are permitted.
All coefficients below are deterministic. At each node let
\[
\begin{aligned}
 Z^{(1)}_{0,a}&=G_a,& H^{(1)}_{k,a}&=\phi_1(Z^{(1)}_{k,a}),\\
 Q^{(1)}_{k,a}
 &=\zeta_{k,a}
   +\sum_{\ell=0}^{k}\sum_{b=1}^2
       B_{ka,\ell b}H^{(1)}_{\ell,b},\\
 Z^{(1)}_{k+1,a}
 &= Z^{(1)}_{k,a}
   +\lambda_k\sum_b C_{ab}c_{k,b}
       \phi_1'(Z^{(1)}_{k,b})Q^{(1)}_{k,b}\quad(k<N).
\end{aligned}                                                    \tag{2}
\]
The coefficients \(B_{ka,\ell b}\), \(c_{k,b}\), and step sizes
\(\lambda_k\ge0\) are finite but need not obey a smallness bound.
Thus (2) is genuinely causal: \(H^{(1)}_k\) is determined before
the current Gaussian query \(Q^{(1)}_k\). It is a finite explicit
recursion, not an implicit fixed point.
The symbol \(B\) without indices denotes the scalar saturation value;
the entries \(B_{ka,\ell b}\) denote the deterministic response matrix.

Stack the first features into a vector \(H\in\mathbb R^{2(N+1)}\), and set
\[
 \Gamma=\mathbb E[HH^T],\qquad
 S=\mathbb E[D_\zeta H],\qquad
 F=\{|G_1|\ge R,\ |G_2|\ge R\},\qquad
 \alpha=\Pr(F^c).                                         \tag{3}
\]
These are uncentered feature second moments and the expected derivative
with respect to the formal Gaussian query coordinates, holding all
deterministic coefficients in (2) fixed. Derivatives are defined by
the recursion even if \(\Sigma\) is singular.
For each fixed finite program they have finite moments: the queries
are Gaussian coordinates plus finite deterministic linear combinations
of bounded features; differentiating (2) repeatedly gives, by finite
induction, bounds by polynomials in \(1+|\zeta|\) with finite coefficients.
Derivatives of \(\phi_1\) are bounded. No uniform derivative moment in
\(N\) is asserted or needed for the inequality below.

On \(F\), both initial first gates are zero. Induction in (2) gives
\[
 Z^{(1)}_{k,a}=G_a,\quad
 H^{(1)}_{k,a}=B\operatorname{sign}(G_a)
 \quad\hbox{for every node and every value of }\zeta.       \tag{4}
\]
This is exact for arbitrary coefficients and step sizes.
In particular \(1_F H\) depends only on \(G\), not on \(\zeta\).

Since each \(G_a\) has standard normal density bounded by
\(1/\sqrt{2\pi}\), a union bound gives
\[
 0<\alpha
 \le \Pr(|G_1|<R)+\Pr(|G_2|<R)
 \le\frac{4R}{\sqrt{2\pi}}<1.                              \tag{5}
\]
Strict positivity follows from \(\Pr(|G_1|<R)>0\).
Thus the same explicit contraction factor works for all correlations,
including the singular antiparallel case. This estimate concerns only
mask mass, not the smallest eigenvalue of an input-feature Gram matrix.

## 2. Strict covariance domination

The claim is the matrix inequality
\[
 S\Sigma S^T
 \preceq \alpha\,\mathbb E[1_{F^c}HH^T]
 \preceq \alpha\Gamma.                                    \tag{6}
\]
It is uniform in \(N\), all the coefficients in (2), all step sizes,
and the Gaussian covariance \(\Sigma\).

Write \(\zeta=\Sigma^{1/2}Z\), where \(Z\) is a standard Gaussian vector
in the same finite dimension, independent of \(G\).
For any deterministic vector \(v\), let \(L=v^TH\).
Gaussian integration by parts gives
\[
 \mathbb E[ZL]=\Sigma^{1/2}S^Tv.                           \tag{7}
\]
Here is a direct justification. In each coordinate of \(Z\), integrate
against its density, whose derivative is \(-z\) times that density.
The boundary term vanishes because \(L\) is bounded. Its derivative
has polynomial growth by the finite induction above and is integrable
against the Gaussian density. Integrate the remaining coordinates
and \(G\), using their integrable bounds. The chain rule is
\(D_ZH=(D_\zeta H)\Sigma^{1/2}\). This proves (7), without an inverse
covariance or a nonsingular-density assumption on \(\zeta\).

Independence of \(Z,G\) and (4) imply
\(\mathbb E[Z1_F L]=0\). For any deterministic unit vector \(u\),
Cauchy--Schwarz therefore gives
\[
 |u^T\mathbb E[ZL]|^2
 =|\mathbb E[1_{F^c}(u^TZ)L]|^2
 \le\mathbb E[1_{F^c}(u^TZ)^2]\,
         \mathbb E[1_{F^c}L^2]
 =\alpha\,\mathbb E[1_{F^c}L^2].                          \tag{8}
\]
Taking the supremum over \(u\) and using (7) proves
\(v^TS\Sigma S^Tv\le\alpha\,v^T\mathbb E[1_{F^c}HH^T]v\)
for every \(v\), which is (6).
This is a statement about the expected response \(S\), not about
\(\mathbb E[(D_\zeta H)\Sigma(D_\zeta H)^T]\).
The latter matrix is not bounded by the argument.

## 3. A dimension-independent inverse on covariance-supported spaces

The previous result can be paired with any differentiable second-population
program \(\Delta=\Delta(\xi)\in\mathbb R^{2(N+1)}\), where
\(\xi\sim N(0,\Gamma)\), such that the Gaussian integration by parts
below is justified (bounded outputs and polynomially bounded derivatives
suffice), and
\[
 \mathbb E[\Delta\Delta^T]=\Sigma,\qquad D=\mathbb E[D_\xi\Delta].
                                                               \tag{9}
\]
For example, a finite explicit upper program with \(\phi_2=\arctan\),
zero initial population readout, finitely many bounded readout increments,
and fixed causal response coefficients has those integrability properties.
Equation (9) is a stated covariance-consistency condition, not an
existence claim for a simultaneous population construction.

Gaussian integration by parts and Cauchy--Schwarz, this time without
any mask, give
\[
 D\Gamma D^T\preceq\Sigma.                                \tag{10}
\]
Indeed write \(\xi=\Gamma^{1/2}Z'\). For a vector \(v\), the norm of
\(\mathbb E[Z'v^T\Delta]=\Gamma^{1/2}D^Tv\) is at most
\((\mathbb E|v^T\Delta|^2)^{1/2}\), by testing against unit Gaussian
linear forms exactly as in (8).

Let \(P_\Gamma,P_\Sigma\) be the Euclidean orthogonal projections
onto the ranges of the two covariance matrices. Let their
pseudoinverse square roots be defined by diagonalizing the matrices,
inverting the positive eigenvalue square roots, and using zero on
their kernels. From (6) and (10),
\[
\begin{gathered}
 S\,\operatorname{ran}\Sigma\subseteq\operatorname{ran}\Gamma,
 \qquad D\,\operatorname{ran}\Gamma\subseteq\operatorname{ran}\Sigma,\\
 \|\Gamma^{\dagger/2}S\Sigma^{1/2}\|_{\rm op}\le\sqrt\alpha,
 \qquad
 \|\Sigma^{\dagger/2}D\Gamma^{1/2}\|_{\rm op}\le1.           \tag{11}
\end{gathered}
\]
To verify the range inclusion, a vector \(v\in\ker\Gamma\) has
\(v^TS\Sigma S^Tv=0\), hence is orthogonal to the range of
\(S\Sigma^{1/2}\). The other inclusion is identical.
Multiplying (6) by \(\Gamma^{\dagger/2}\) on both sides gives
\(TT^T\preceq\alpha P_\Gamma\) for
\(T=\Gamma^{\dagger/2}S\Sigma^{1/2}\), proving its norm bound.
The proof for \(D\) is the same.

Equip \(\operatorname{ran}\Sigma\) with the norm
\(|x|_\Sigma=|\Sigma^{\dagger/2}x|\) and
\(\operatorname{ran}\Gamma\) with \(|x|_\Gamma\) analogously.
These are well-defined ordinary finite-dimensional weighted norms.
Equation (11) implies
\[
 \|DS\|_{\operatorname{ran}\Sigma\to\operatorname{ran}\Sigma}
 \le\sqrt\alpha,\qquad
 \|SD\|_{\operatorname{ran}\Gamma\to\operatorname{ran}\Gamma}
 \le\sqrt\alpha,                                         \tag{12}
\]
where domain and target use their indicated covariance norms.
For instance write \(x=\Sigma^{1/2}u\) with \(u\in\operatorname{ran}\Sigma\)
and insert \(P_\Gamma=\Gamma^{1/2}\Gamma^{\dagger/2}\)
between \(D\) and \(S\), using the range inclusion.
The resulting conjugate of \(DS\) is the product of the two operators
in (11).

Consequently both supported inverses exist and satisfy
\[
 \|(I-DS)^{-1}\|_{\Sigma}\le\frac1{1-\sqrt\alpha},\qquad
 \|(I-SD)^{-1}\|_{\Gamma}\le\frac1{1-\sqrt\alpha}.           \tag{13}
\]
For a direct proof, the geometric series in either operator converges
absolutely in norm by (12); multiplication by \(I-DS\) or \(I-SD\)
telescopes, and the remainder tends to zero.
Thus (13) needs neither a lower bound on positive covariance eigenvalues,
nor finite-dimensional nilpotency with a bound proportional to \(N\).
It holds on the supported spaces even when the covariances are singular.
No bound on how these norms compare to Euclidean norms is asserted.

## 4. What this controls, and the remaining issue

The strict gap is a consequence of a Gaussian-independent initial mask
on which the first feature path is insensitive to every Gaussian query.
It is not merely pointwise nonaffinity of one marginal. In particular
it remains valid for arbitrary linear combinations across all time
nodes, including combinations cancelling the frozen contribution.
For such a combination the first inequality in (6) still has the
factor \(\alpha\); the masked Cauchy--Schwarz factor does not disappear.

In a Gaussian matrix-reuse construction, the expected derivative
matrices \(S,D\) are only the Gaussian response parts.
Trained rank memories add other matrices. For a full feedback pair
\(A_{\rm full}=S+M_A\), \(B_{\rm full}=D+M_B\), none of
\[
 M_A\operatorname{ran}\Sigma\subseteq\operatorname{ran}\Gamma,\qquad
 M_B\operatorname{ran}\Gamma\subseteq\operatorname{ran}\Sigma
\]
follows from (6) or (10).
Nor do those inequalities bound their norms in (11)'s covariance metrics.
For a simple algebraic warning, take
\(\Gamma=\Sigma=\operatorname{diag}(1,0)\), \(S=D=0\), and
\(M_Ae_1=e_2\). Equations (6), (10), and (13) all hold, but the
memory maps a supported vector outside the supported subspace.
This example is not claimed to be an actual trained trajectory.

Thus (13) is not a bound on \((I-B_{\rm full}A_{\rm full})^{-1}\),
not a bound on the full sample-wise Jacobian, and not a bound on the
time integral of the cavity trace kernel. Establishing any of these
requires retaining and controlling the actual learned memories, and
distinguishing mean response from mean-square response.
No step here asserts a full-population fixed-point uniqueness theorem.

The finite program (2) states all its mathematical inputs explicitly.
Using this lemma for a particular network limit additionally requires
identifying that network's first Gaussian query source as independent
of its initial root \(G\), and its coefficients as frozen when taking
the derivative in (3). No iid claim about trained finite neurons or
unaudited Gaussian-action theorem is implicit in this document.
The proposed gain is the unconditional estimate (6) for every program
(2), and its uniform supported inverse consequence under (9);
those are the claims to audit.
