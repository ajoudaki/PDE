# Exclusion of positive-loss local minima with a rank-one upper field

2026-09-19. Informed post-freeze subsidiary result. The lead supplied the small-population-subset stationarity argument from sections 1–3 of `finite_sample_theorem.md` and suggested the complex-pole proof of the final function-separation step. Both arguments are reproduced below, so the mathematical proof is self-contained. The initial line-range read accidentally displayed later sections of that file; those sections are not premises of this result.

The independent `abstract_route.md` remains unchanged, with SHA256 `5e70ae1e67a57a53526eca82fa8050c984a7d3c4c2dcd797872a45cb13abb891`. Its lower moment theorem invokes Lyapunov's convexity theorem and the infinite product for `cosh`. Those external dependencies and that complete moment theorem have **not been independently audited**. Neither is used here, and that moment theorem is not a premise of the accepted central argument.

This note proves a restricted landscape statement for arbitrary finite sample count. It does not settle the unrestricted landscape with higher-rank upper fields.

## 1. Model and statement

Let \(u_1,\ldots,u_m\in\mathbb R^d\) be unit vectors, with \(u_i\ne\pm u_j\) for \(i\ne j\). Let \(\mu_i>0\) and \(y_i\in\mathbb R\). The lower probability space is nonatomic. Both fixed mark vectors

\[
b_1:\Omega_1\to\mathbb R^{k_1},\qquad
b_2:\Omega_2\to\mathbb R^{k_2}
\]

are bounded and measurable; linear redundancies and arbitrary dependence among their coordinates are allowed. Train

\[
w\in L^2(\Omega_1;\mathbb R^d),\qquad
c\in L^2(\Omega_2),\qquad
M\in\mathbb R^{k_2\times k_1}.
\]

With \(\phi=\tanh\), define

\[
a_i=\mathbb E_1[b_1\phi(w\cdot u_i)],\qquad
z_i=b_2^TMa_i,\qquad H_i=\phi(z_i),
\]
\[
f_i=\mathbb E_2[cH_i],\qquad r_i=f_i-y_i,\qquad
L=\sum_{i=1}^m\mu_i r_i^2.
\tag{1}
\]

Local minima are taken in the ambient physical product topology of \(L^2\), \(L^2\), and the Frobenius matrix norm, with all displayed trainable variables available.

Let \(B_1\subseteq\mathbb R^{k_1}\) be the linear span of the essential range of \(b_1\). Equivalently,

\[
B_1=\ker(\mathbb E_1[b_1b_1^T])^\perp.
\]

Thus \(b_1\in B_1\) almost surely, every \(a_i\in B_1\), and

\[
v\in B_1\setminus\{0\}\quad\Longrightarrow\quad
\mathbb E_1(v\cdot b_1)^2>0.
\tag{2}
\]

Define \(U_2:\mathbb R^{k_2}\to L^2(\Omega_2)\) by \(U_2q=b_2^Tq\). The actual current operator is

\[
K=U_2M\big|_{B_1}:B_1\longrightarrow L^2(\Omega_2).
\]

**Theorem.** Suppose an ambient local minimum of (1) has \(\operatorname{rank}K=1\). Write its rank-one factorization as

\[
Kh=T(v\cdot h),\qquad h\in B_1,
\tag{3}
\]

where \(v\in B_1\setminus\{0\}\) and \(T\) is a nonzero scalar function. If \(T\) has infinite essential support, then \(r_i=0\) for every sample and \(L=0\).

A factorization (3) exists because a nonzero rank-one linear map on a finite-dimensional Euclidean space is a fixed nonzero output vector times a nonzero linear functional. Moreover \(T\) can, and therefore must, be bounded up to a constant rescaling: choose \(h\) with \(v\cdot h=1\), so \(T=Kh=b_2^TMh\). Infinite essential support is unaffected by a nonzero rescaling of the factorization.

There is no bound on the finite number \(m\), no mark-parity condition, and no upper density or polynomial requirement. The theorem's nondegeneracy assumption concerns the actual current scalar upper field \(T\), not the existence of a continuous unused coordinate elsewhere in the dictionary. An unused continuous coordinate alone does not establish this assumption.

The proof first extracts a samplewise necessary condition by changing the lower field on small measurable sets. Prediction-preserving changes of the readout then force a differentiated feature into the original finite feature span. The last step shows that this membership is impossible for a genuinely varying scalar upper field.

## 2. Independence of the input ridge functions

The functions \(s\mapsto\phi(s\cdot u_i)\), \(s\in\mathbb R^d\), are linearly independent. To prove this, choose \(\eta\in\mathbb R^d\) outside the finitely many hyperplanes orthogonal to \(u_i\) and \(u_i\pm u_j\). Each such hyperplane is proper under the input assumptions. Then

\[
\beta_i=\eta\cdot u_i\ne0,\qquad \beta_i^2\ne\beta_j^2\ (i\ne j).
\]

Every odd Taylor coefficient of \(\tanh\) at zero is nonzero. Indeed, writing

\[
\tanh t=\sum_{n\ge0}(-1)^n a_nt^{2n+1},
\]

the analytic identity \(\phi'=1-\phi^2\) gives \(a_0=1\) and

\[
(2n+1)a_n=\sum_{j+k=n-1}a_ja_k>0\qquad(n\ge1),
\]

by induction. Restricting a putative ridge relation \(\sum_i\gamma_i\phi(s\cdot u_i)=0\) to \(s=t\eta\), and comparing the first \(m\) odd Taylor coefficients, gives

\[
\sum_i\gamma_i\beta_i(\beta_i^2)^j=0,
\qquad 0\le j<m.
\]

The Vandermonde matrix in the distinct numbers \(\beta_i^2\) is invertible, and none of the \(\beta_i\) vanishes. Hence every \(\gamma_i=0\).

## 3. Small-set stationarity without a moment-range theorem

Set

\[
d_i=\mathbb E_2[b_2c\phi'(z_i)]\in\mathbb R^{k_2}.
\]

At fixed \(M,c\), the loss viewed as a function of the finite vectors \(a_i\) is twice continuously differentiable, with a locally uniform quadratic Taylor remainder. The bounded marks, bounded derivatives of \(\tanh\), and \(\mathbb E|c|\le\|c\|_2\) justify differentiation under the expectation. The first derivative and matrix gradient are

\[
\delta L=2\sum_i\mu_i r_i d_i^TM\delta a_i,
\qquad
\nabla_ML=2\sum_i\mu_i r_i d_i a_i^T.
\tag{4}
\]

At a local minimum define, for almost every lower carrier point \(\omega\),

\[
F_\omega(s)=\sum_i\mu_i r_i
\big[b_1(\omega)^TM^Td_i\big]\phi(s\cdot u_i),
\qquad s\in\mathbb R^d.
\tag{5}
\]

We claim that \(w(\omega)\) globally minimizes this function for almost every \(\omega\). If not, continuity in \(s\), countability of rational vectors, positive rational margins, and integer bounds on \(|w|\) provide one fixed \(s\in\mathbb Q^d\), constants \(\delta>0\), \(R<\infty\), and a measurable set \(E_0\) of positive probability such that

\[
|w(\omega)|\le R,\qquad
F_\omega(s)-F_\omega(w(\omega))\le-\delta
\quad(\omega\in E_0).
\]

Nonatomicity gives subsets \(E\subset E_0\) with arbitrarily small positive probability \(\varepsilon\). This elementary consequence needs no vector-measure theorem: repeatedly split a positive-measure set into two positive-measure subsets and retain a smaller one, whose measure is at most half that of its parent.

Replace \(w\) by \(s\) on \(E\), leaving it unchanged elsewhere. The new control remains \(L^2\), and its squared displacement is at most \(\varepsilon(|s|+R)^2\). Boundedness of \(b_1\) and \(\phi\) gives

\[
\delta a_i=\int_E b_1\big[\phi(s\cdot u_i)-\phi(w\cdot u_i)\big]\,dP_1
=O(\varepsilon).
\]

Using (4) with its quadratic Taylor remainder,

\[
L_{\rm new}-L
=2\int_E[F_\omega(s)-F_\omega(w)]\,dP_1+O(\varepsilon^2)
\le-2\delta\varepsilon+O(\varepsilon^2)<0
\]

for sufficiently small \(\varepsilon\). This contradicts the physical local minimum and proves the claim.

Consequently \(F_\omega(w)\le F_\omega(0)=0\) almost surely. On the other hand, matrix stationarity and (4) imply

\[
\mathbb E_1F_\omega(w)
=\sum_i\mu_i r_i d_i^TMa_i
=\tfrac12\langle\nabla_ML,M\rangle_F=0.
\]

The integrand is integrable, so \(F_\omega(w)=0\) almost surely. Its global minimum is therefore zero. Since \(F_\omega\) is odd, it must be identically zero: nonnegativity of both \(F_\omega(s)\) and \(F_\omega(-s)=-F_\omega(s)\) forces equality. Ridge independence from section 2, together with \(\mu_i>0\), now gives the necessary condition

\[
r_i b_1^TM^Td_i=0\quad\text{almost surely},\qquad i=1,\ldots,m.
\tag{6}
\]

No interiority, convexity, or local surjectivity of the lower moment range was used.

## 4. Rank one and readout-null changes

At the local minimum in the theorem, let

\[
\alpha_i=v\cdot a_i.
\]

Equation (3) gives \(z_i=\alpha_iT\), and hence \(H_i=\phi(\alpha_iT)\). Since \(b_1(\omega)\in B_1\) almost surely, (3) also gives

\[
b_1(\omega)^TM^Td_i
=\mathbb E_2\big[c\phi'(\alpha_iT)\,b_2^TMb_1(\omega)\big]
=(v\cdot b_1(\omega))\,\mathbb E_2[cT\phi'(\alpha_iT)].
\]

These expectations are integrable because \(T\) and \(\phi'\) are bounded and \(c\in L^2\). Equations (2) and (6) therefore imply

\[
r_i\mathbb E_2[cT\phi'(\alpha_iT)]=0
\qquad(i=1,\ldots,m).
\tag{7}
\]

Suppose for contradiction that \(r_i\ne0\) for some sample \(i\). Put

\[
\mathcal H=\operatorname{span}\{\phi(\alpha_jT):1\le j\le m\}
\subset L^2(\Omega_2).
\]

For any \(q\in\mathcal H^\perp\), replace \(c\) by \(c+\varepsilon q\). Every prediction is exactly unchanged. Choose \(\varepsilon\ne0\) sufficiently small that this point lies inside an open ball witnessing local minimality of the original point. A smaller ball about the new point lies inside the original ball; because the loss values agree, the new point is itself a local minimum. The same \(w,M,T,v,\alpha_j\), features, and residuals apply there.

Apply (7) at both readouts and subtract. Since \(r_i\ne0\),

\[
\mathbb E_2[qT\phi'(\alpha_iT)]=0
\qquad\text{for every }q\in\mathcal H^\perp.
\]

The function \(T\phi'(\alpha_iT)\) belongs to \(L^2\), and the finite-dimensional subspace \(\mathcal H\) is closed. Orthogonal decomposition in the Hilbert space \(L^2\) therefore gives

\[
T\operatorname{sech}^2(\alpha_iT)
\in\operatorname{span}\{\tanh(\alpha_jT):1\le j\le m\}.
\tag{8}
\]

The next lemma contradicts (8).

## 5. Scalar feature separation by pole order

**Lemma.** Let \(T\) be bounded and have infinite essential support. For arbitrary finite real numbers \(\alpha_1,\ldots,\alpha_m\), and every index \(i\),

\[
T\operatorname{sech}^2(\alpha_iT)
\notin\operatorname{span}\{\tanh(\alpha_jT):1\le j\le m\}.
\tag{9}
\]

**Proof.** A contrary membership gives real coefficients \(\gamma_j\) with

\[
T\operatorname{sech}^2(\alpha_iT)
=\sum_j\gamma_j\tanh(\alpha_jT)
\quad\text{almost surely}.
\tag{10}
\]

Let \(S\) be the support of the law of \(T\), namely the set of real \(t\) for which every open neighborhood has positive probability. It is compact because \(T\) is bounded, and infinite by hypothesis. The continuous difference of the two sides of (10), viewed as a function of a real argument \(t\), vanishes at every point of \(S\): a nonzero value at a support point would persist on a neighborhood of positive probability. The infinite compact set \(S\) has a finite accumulation point. Both sides are real analytic on the entire real line, so the identity theorem extends the equality to every \(t\in\mathbb R\).

If \(\alpha_i=0\), the left side is \(t\), whereas the right side is bounded by \(\sum_j|\gamma_j|\) on the real line. This is impossible.

Suppose \(\alpha_i\ne0\). Complexify the identity to the meromorphic functions

\[
z\operatorname{sech}^2(\alpha_i z)
\quad\text{and}\quad
\sum_j\gamma_j\tanh(\alpha_j z).
\]

The zeros of \(\cosh z=(e^z+e^{-z})/2\) are precisely \(i\pi(n+\tfrac12)\), \(n\in\mathbb Z\), and each zero is simple because \(\sinh\) is nonzero there. Thus every nonconstant \(\tanh(\alpha_j z)\) has only simple poles. Their finite sum has at most a simple pole at any point, even when some poles coincide. Terms with \(\alpha_j=0\) vanish identically.

The union of all poles involved is locally finite. Its complement in \(\mathbb C\) is connected: a polygonal path between two points can be modified around the finitely many poles it encounters in a bounded neighborhood of that path. The holomorphic identity theorem therefore extends the equality from a real interval to this pole-free connected set.

Now take

\[
z_0=\frac{i\pi}{2\alpha_i}\ne0.
\]

For \(\zeta=z-z_0\), the elementary Taylor expansion at \(\alpha_i z_0=i\pi/2\) gives

\[
\cosh(\alpha_i z)=i\alpha_i\zeta+O(\zeta^3),
\]

and hence

\[
z\operatorname{sech}^2(\alpha_i z)
=-\frac{z_0}{\alpha_i^2\zeta^2}
-\frac{1}{\alpha_i^2\zeta}+O(1).
\]

The coefficient of the double pole is nonzero. By contrast, multiplying the right side by \(\zeta^2\) gives a quantity tending to zero, because every summand has at most a simple pole at \(z_0\). Multiplying the meromorphic identity by \(\zeta^2\) and taking \(\zeta\to0\) thus gives the contradiction \(-z_0/\alpha_i^2=0\). This proves (9). \(\square\)

Combining the lemma with (8) excludes every nonzero residual and completes the theorem.

## 6. Scope and audit points

- The rank is that of \(U_2M|_{B_1}\), not necessarily the displayed matrix rank. Both lower and upper coordinate redundancies are automatically respected.
- The scalar distribution may be singular or purely atomic with infinitely many support points. Boundedness supplies an accumulation point; no density is used.
- Coincident, zero, or opposite scalar coefficients \(\alpha_j\) do not affect the pole argument. The finite sample count is otherwise arbitrary.
- Continuous unused upper marks do not ensure that the current rank-one image has infinite essential support. Constant or finite-support images are outside this theorem.
- Input duplicates and antipodes may be combined beforehand into signed groups when the labels are compatible. The proof then applies to the resulting distinct representatives. Incompatible signed observations require the corresponding irreducible-error formulation rather than a zero-loss conclusion.
- The reasoning uses exact prediction-preserving readout changes and arbitrarily small physical lower-field changes. It does not use an approximation, a limit in model order, a trajectory argument, a Gram-density argument, or the frozen moment-interior theorem.
- This is an internally derived subsidiary theorem. The unrestricted case with higher-rank projected upper marks remains open here.
