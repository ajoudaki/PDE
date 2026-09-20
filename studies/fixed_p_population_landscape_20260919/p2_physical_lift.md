# Physical lower-moment transfer in two input dimensions

2026-09-19. Informed continuation within this study. The lead suggested the elementary angular-variation proof of the sign-polytope lemma; that proof and the approximate switching construction are given completely below. This is not a fresh independent attempt. No other study, external scientific source, or experiment was used.

**Result.** In input dimension two, every physical local minimum is a local minimum with all lower moment columns independently free in their effective coefficient space, for every finite number of distinct unoriented sample directions. An approximate physical lift, with an explicit square-root displacement bound, suffices. The proof uses no Lyapunov vector-measure theorem, exact vector purification, isotropic-noise formula, or infinite-product identity. The earlier frozen moment theorem and its unaudited external dependencies are not premises.

When the effective lower mark dimension is at least the effective upper mark dimension, this transfer removes the sample-count restriction from the implication \(r_i d_i=0\) and from the resulting full-gate inclusions. It does not, by itself, prove the upper gate-separation property for the full canonical dictionary.

## 1. Model and theorem

Let \((\Omega_1,P_1)\) be a nonatomic probability space, and let \(b_1:\Omega_1\to\mathbb R^{k_1}\) be bounded and measurable. Let \(B_1\subseteq\mathbb R^{k_1}\) be the span of its essential range. Fix any finite collection of unit vectors

\[
u_1,\ldots,u_m\in S^1,\qquad u_i\ne\pm u_j\quad(i\ne j).
\]

For \(v\in\mathbb R^2\), write

\[
H(v)=(\tanh(v\cdot u_1),\ldots,\tanh(v\cdot u_m))^T.
\]

For a trainable physical field \(w\in L^2(\Omega_1;\mathbb R^2)\), its moment matrix is

\[
A(w)=\mathbb E_1[b_1H(w)^T]\in B_1^m.
\tag{1}
\]

Here \(B_1^m\) means the space of matrices with each of their \(m\) columns in \(B_1\), with the Frobenius norm.

**Approximate local lift.** For every \(w_0\in L^2\), there are finite constants \(\rho>0\) and \(C>0\) such that, for every \(\Delta\in B_1^m\) with \(\|\Delta\|_F<\rho\) and every \(\varepsilon>0\), there is \(w_{\Delta,\varepsilon}\in L^2\) satisfying

\[
\|A(w_{\Delta,\varepsilon})-A(w_0)-\Delta\|_F<\varepsilon,
\qquad
\|w_{\Delta,\varepsilon}-w_0\|_{L^2}^2
\le C\|\Delta\|_F+\varepsilon.
\tag{2}
\]

The constants may depend on the fixed directions, marks, and \(w_0\). There is no upper bound on their finite sample count. If \(B_1=\{0\}\), the assertion is trivial with \(w_{0,\varepsilon}=w_0\); henceforth assume \(B_1\ne\{0\}\).

**Local-minimum equivalence.** Let the upper marks \(b_2\) be bounded, \(M\in\mathbb R^{k_2\times k_1}\), and \(c\in L^2(\Omega_2)\). With positive weights \(\mu_i\), define the reduced loss on the whole space \(B_1^m\) by

\[
\mathcal L(A,M,c)
=\sum_i\mu_i\left(\mathbb E_2[c\tanh(b_2^TMa_i)]-y_i\right)^2.
\tag{3}
\]

Then \((w_0,M_0,c_0)\) is a local minimum of \(\mathcal L(A(w),M,c)\) in the physical \(L^2/L^2/\)Frobenius topology if and only if \((A(w_0),M_0,c_0)\) is a local minimum of (3) with \(A\) freely variable in \(B_1^m\).

This equivalence does not assert that every nearby matrix has an exact physical realization. Approximation with controlled physical displacement is sufficient for the local-minimum statement.

## 2. Elementary interiority of the circle ridge vector

The sign vectors

\[
\big(\operatorname{sign}(v\cdot u_i)\big)_{i=1}^m,
\qquad v\cdot u_i\ne0\text{ for all }i,
\]

form the vertices of a full-dimensional polytope \(P\subset\mathbb R^m\). We need the following stronger, quantitative description.

**Angular lemma.** There is an invertible \(m\)-by-\(m\) matrix \(V\), whose columns are sign-pattern vectors, such that

\[
P=\{V\lambda:\|\lambda\|_1\le1\},
\qquad
\|V^{-1}H(v)\|_1\le\tanh\|v\|<1
\quad(v\in\mathbb R^2).
\tag{4}
\]

To prove this, independently orient and order the sample lines so that their angles satisfy

\[
\theta_1<\theta_2<\cdots<\theta_m<\theta_1+\pi.
\]

An orientation change or reordering merely applies a signed permutation to the coordinates of every sign vector and every \(H(v)\); undoing that transformation gives the claimed matrix for the original directions. Thus we may work in this order without changing the model.

As the angle of \(v\) increases through a suitable half-turn, the signs change one at a time in the indicated order. The successive vectors are

\[
v_j=(\underbrace{1,\ldots,1}_{j},
\underbrace{-1,\ldots,-1}_{m-j}),
\qquad j=0,\ldots,m,
\]

with \(v_m=-v_0\). The other half-turn gives their negatives. Thus all vertices are \(\pm v_j\), \(0\le j<m\). Let \(V\) have columns \(v_0,\ldots,v_{m-1}\).

For any \(h\in\mathbb R^m\), its coefficients \(h=V\lambda\) are

\[
\lambda_0=-\tfrac12(h_1+h_m),\qquad
\lambda_j=\tfrac12(h_j-h_{j+1}),\quad 1\le j<m.
\tag{5}
\]

Indeed, the adjacent coordinate differences of \(V\lambda\) equal \(2\lambda_j\), and the sum of its first and last coordinates equals \(-2\lambda_0\). These quantities determine all its coordinates. This verifies (5), proves invertibility, and identifies the convex hull of the vertices as the displayed image of the \(\ell^1\) unit ball. With the antiperiodic endpoint \(h_{m+1}=-h_1\), (5) gives

\[
\|V^{-1}h\|_1=\frac12\sum_{j=1}^m|h_{j+1}-h_j|.
\tag{6}
\]

Write \(v=R(\cos\alpha,\sin\alpha)\), with \(R\ge0\), and define

\[
F(\theta)=\tanh(R\cos(\theta-\alpha)).
\]

Then \(F(\theta+\pi)=-F(\theta)\), and

\[
|F'(\theta)|
=R|\sin(\theta-\alpha)|\operatorname{sech}^2(R\cos(\theta-\alpha))
\]

is \(\pi\)-periodic. Its integral over any half-turn therefore equals its integral from \(\alpha\) to \(\alpha+\pi\). On this particular interval \(F\) is nonincreasing, so

\[
\int_{\theta_1}^{\theta_1+\pi}|F'(\theta)|\,d\theta
=F(\alpha)-F(\alpha+\pi)=2\tanh R.
\]

The sum in (6), evaluated at \(h_j=F(\theta_j)\), is at most this total variation, by integrating \(|F'|\) on the successive intervals including the last interval to \(\theta_1+\pi\). This proves (4). The same formulas cover \(m=1\) and \(R=0\).

In particular, for any fixed finite \(R\), all ridge vectors with \(\|v\|\le R\) have a uniform strict margin inside \(P\).

## 3. Scalar splitting and approximate finite switching

We require only elementary scalar-measure splitting, not a convexity theorem for vector measures.

**Scalar splitting.** On a nonatomic finite measure space, every measurable set \(E\) has a measurable subset of each prescribed measure \(a\in[0,P(E)]\).

Here is a construction. Any positive-measure nonatomic set has positive-measure subsets of arbitrarily small measure: split it into two positive parts and repeatedly keep a smaller part, whose measure is at most half that of its parent. Starting from the empty set, let the remaining target at step \(n\) be \(t_n\). Among subsets of the unused part with measure at most \(t_n\), choose one whose measure is at least half the supremum of the admissible measures, and add it. If the remaining targets converged to \(t>0\), the unused part after all steps would have measure at least \(t\). It would contain a fixed positive-measure subset \(G\) of measure at most \(t\). This \(G\) would have been admissible at every step, forcing every added increment to have measure at least \(P(G)/2\), an impossibility in a finite measure space. Thus the remaining target tends to zero; the countable union has measure exactly \(a\). The endpoint cases are immediate. Repeated splitting gives a finite partition with any prescribed proportions.

**Approximate switching lemma.** Let \(F_0,\ldots,F_N\in L^1(\Omega_1;\mathbb R^D)\), and let measurable probabilities \(p_j\ge0\) satisfy \(\sum_jp_j=1\) almost surely. For every \(\varepsilon>0\), there is a measurable partition \(E_0,\ldots,E_N\) of \(\Omega_1\) such that

\[
\left\|\sum_j\int_{E_j}F_j\,dP_1
-\int\sum_jp_jF_j\,dP_1\right\|<\varepsilon.
\tag{7}
\]

To prove this, approximate the finitely many integrable vectors \(F_j\) by simple functions \(S_j\), constant on one common finite measurable partition, with

\[
\sum_j\|F_j-S_j\|_{L^1}<\varepsilon/2.
\]

Such approximation follows directly by truncating the integrable functions and quantizing their bounded coordinate values into finitely many intervals. For a cell \(C\) of positive measure, split it into pieces \(C_j\) with

\[
P_1(C_j)=\int_Cp_j\,dP_1.
\]

The measures on the right are nonnegative and sum to \(P_1(C)\), so scalar splitting applies. Since each \(S_j\) is constant on \(C\), these pieces give exact equality between the two expressions in (7) with \(F_j\) replaced by \(S_j\). The two errors are bounded by

\[
\sum_j\int_{E_j}\|F_j-S_j\|\,dP_1
+\sum_j\int p_j\|F_j-S_j\|\,dP_1
\le2\sum_j\|F_j-S_j\|_{L^1}<\varepsilon.
\]

This proves (7). Any specified finite measurable partition can also be included in the common refinement. For example, if all but one probability vanish outside a set \(E\), the selected nontrivial pieces can be confined to \(E\), up to null sets.

Apply this lemma to finitely many controls \(w_j\in L^2\), with the vector integrands

\[
F_j(\omega)=\left(
\operatorname{vec}\{b_1(\omega)H(w_j(\omega))^T\},
\|w_j(\omega)-w_0(\omega)\|^2
\right).
\tag{8}
\]

They are integrable because the marks and activations are bounded and the controls are \(L^2\). Choosing \(w=w_j\) on \(E_j\) gives an \(L^2\) field. Equation (7) simultaneously approximates its moment matrix and its squared physical displacement from \(w_0\), to arbitrary prescribed accuracy. The probabilities may depend measurably on the lower carrier point; no independent random coordinate is required.

## 4. Construction of the local approximate lift

Let \(A_0=A(w_0)\), and let \(L_1\) bound \(\|b_1\|\). On \(B_1\), the matrix

\[
G=\mathbb E_1[b_1b_1^T]
\]

is positive definite by the definition of \(B_1\). For

\[
E_R=\{\|w_0\|\le R\},\qquad
G_R=\mathbb E_1[1_{E_R}b_1b_1^T],
\]

one has

\[
\|G-G_R\|_{\rm op}\le L_1^2P_1(\|w_0\|>R)\longrightarrow0.
\]

Choose finite \(R>0\) for which \(G_R\) is still positive definite on \(B_1\). Its inverse below is always this restricted inverse. Put \(E=E_R\).

Choose the sign-pattern basis \(V\) from section 2. For each column of \(V\), choose a unit vector \(\xi_j\in\mathbb R^2\) in its open sign chamber. Then

\[
H(T\xi_j)\longrightarrow v_j\quad\text{as }T\to\infty.
\]

For sufficiently large but finite \(T\), the matrix \(S\) with columns \(H(T\xi_j)\) is invertible and its inverse is arbitrarily close to \(V^{-1}\). This follows, for example, from the adjugate formula for the inverse and continuity of the nonzero determinant at \(V\). Since \(\|H(v)\|_2\le\sqrt m\), (4) gives a choice of this finite \(T\) and a constant \(\kappa<1\) such that

\[
\|S^{-1}H(v)\|_1\le\kappa
\qquad(\|v\|\le R).
\tag{9}
\]

Let

\[
Q=\operatorname{conv}\{\pm H(T\xi_j):0\le j<m\}
=\{S\lambda:\|\lambda\|_1\le1\}.
\]

Because \(S^{-1}\) is bounded between finite-dimensional normed spaces, choose \(\eta>0\) so small that

\[
\|v\|\le R,\quad\|e\|_2\le\eta
\quad\Longrightarrow\quad H(v)+e\in Q.
\tag{10}
\]

Explicitly, any \(\eta\) satisfying \(\|S^{-1}\|_{2\to1}\eta<(1-\kappa)\) works.

Set

\[
J=L_1\|G_R^{-1}\|_{\rm op}>0,\qquad
\rho=\eta/J.
\]

Take \(0<\delta=\|\Delta\|_F<\rho\), and put \(t=\delta/\rho\in(0,1)\). On \(E\), define

\[
e(\omega)=\frac1t\Delta^TG_R^{-1}b_1(\omega).
\tag{11}
\]

Its norm is at most \(J\delta/t=\eta\), so (10) implies

\[
h_*(\omega)=H(w_0(\omega))+e(\omega)\in Q
\quad(\omega\in E).
\]

There is an explicit measurable representation of this vector by the finitely many constant controls \(T\xi_j\), \(-T\xi_j\), and \(0\). Namely put \(\lambda=S^{-1}h_*\), use weights \(\max(\lambda_j,0)\) and \(\max(-\lambda_j,0)\) for the two signed controls, and give the remaining weight \(1-\|\lambda\|_1\) to the zero control. Oddness of \(H\) and \(H(0)=0\) show that these nonnegative weights sum to one and average to \(h_*\).

Now define a pointwise finite randomization as follows. Outside \(E\), retain the old control \(w_0\) with probability one. On \(E\), retain it with probability \(1-t\); with probability \(t\), choose the just-described finite mixture of constant controls. Its expected ridge vector is

\[
H(w_0)+t1_E e.
\]

Consequently its expected moment matrix is exactly

\[
A_0+t\mathbb E_1[1_Eb_1e^T]
=A_0+G_RG_R^{-1}\Delta=A_0+\Delta.
\tag{12}
\]

Its expected squared physical displacement from \(w_0\) is at most

\[
t(T+R)^2P_1(E)
\le\frac{(T+R)^2}{\rho}\delta.
\tag{13}
\]

This randomization is only an intermediate finite list of measurable probabilities, not a modification of the carrier. Apply the approximate switching lemma to (8), with these probabilities. The resulting deterministic measurable \(L^2\) field has moment error less than \(\varepsilon\) relative to (12), and squared displacement at most the bound in (13) plus \(\varepsilon\). Thus (2) holds with \(C=(T+R)^2/\rho\). When \(\Delta=0\), use \(w_0\) itself.

This completes the construction. Every constant is finite, all switching takes place on the original carrier, and the full retained mark vector is used throughout.

## 5. Transfer of local minima

First note that the reduced loss (3) is continuous in all its variables. For example,

\[
\|\tanh(b_2^TMa_i)-\tanh(b_2^TM'a_i')\|_{L^2}
\le\|b_2\|_\infty\|Ma_i-M'a_i'\|,
\]

and \(\|c\|_{L^1}\le\|c\|_{L^2}\). These estimates justify continuity of every prediction and of the finite squared loss.

Suppose \((w_0,M_0,c_0)\) is a physical local minimum. If \((A_0,M_0,c_0)\) were not a reduced local minimum, there would be reduced points

\[
(A_n,M_n,c_n)\longrightarrow(A_0,M_0,c_0)
\]

with strictly smaller loss. Choose \(n\) sufficiently large that \(\|A_n-A_0\|_F<\rho\), the bound \(C\|A_n-A_0\|_F\) is smaller than a fixed fraction of the squared physical minimality radius, and the changes in \(M_n,c_n\) are also inside that radius. For this fixed \(n\), apply (2) with \(\Delta=A_n-A_0\) and let \(\varepsilon\) be sufficiently small. The resulting physical field lies inside the minimality ball. Continuity in \(A\) also makes its loss, at the fixed \(M_n,c_n\), still strictly smaller than the original loss. This is a contradiction.

For the converse, bounded marks and the unit input norms give

\[
\|A(w)-A(w_0)\|_F
\le L_1\sqrt m\,\|w-w_0\|_{L^2},
\]

using the 1-Lipschitz property of \(\tanh\), the triangle inequality for each moment integral, and Cauchy–Schwarz. Thus any sufficiently small physical perturbation induces a sufficiently small reduced perturbation. A reduced local minimum is therefore a physical local minimum. This proves the equivalence in section 1.

## 6. Consequence when the lower effective dimension dominates

Let \(B_2\) be the span of the essential range of \(b_2\), and let \(q_\ell=\dim B_\ell\). All upper fields depend only on the effective linear map

\[
M_{\rm eff}=P_{B_2}M|_{B_1}:B_1\to B_2.
\]

For a physical local minimum, section 5 permits independently varying the moment columns in the reduced loss. Define

\[
z_i=b_2^TMa_i,\qquad
d_i=\mathbb E_2[b_2c\operatorname{sech}^2z_i]\in B_2,
\qquad r_i=\mathbb E_2[c\tanh z_i]-y_i.
\]

**Corollary.** If \(q_1\ge q_2\), every physical local minimum satisfies

\[
r_id_i=0\quad\text{for every }i,
\tag{14}
\]

for arbitrary finite \(m\).

If \(\ker M_{\rm eff}\ne\{0\}\), choose \(v\ne0\) in that kernel and change one reduced moment column \(a_i\mapsto a_i+sv\). This preserves every upper field and prediction exactly. Every sufficiently small such point is a local minimum of the reduced loss, because it lies inside the original reduced minimality ball and has the same loss. Matrix stationarity is

\[
\nabla_M\mathcal L=2\sum_j\mu_jr_jd_ja_j^T=0.
\]

The stationarity equations before and after the change differ by \(2s\mu_ir_id_iv^T=0\). Since \(s\ne0\), \(\mu_i>0\), and \(v\ne0\), this proves (14).

If \(\ker M_{\rm eff}=\{0\}\), the assumption \(q_1\ge q_2\) forces \(q_1=q_2\) and makes \(M_{\rm eff}\) an isomorphism. Independent column stationarity gives \(r_iM_{\rm eff}^Td_i=0\), and invertibility of the transpose gives (14) again.

Now put \(\mathcal H=\operatorname{span}\{\tanh z_j\}\) in the upper population \(L^2\), and let \(V_2\) be the span of the coordinate functions of \(b_2\). For \(k\in\mathcal H^\perp\), a sufficiently small change \(c\mapsto c+sk\) preserves all physical predictions and local minimality. Apply (14) before and after this change. For any sample with \(r_i\ne0\), subtraction gives

\[
\mathbb E_2[b_2k\operatorname{sech}^2z_i]=0
\qquad(k\in\mathcal H^\perp),
\]

and hence

\[
\operatorname{sech}^2(z_i)V_2\subseteq\mathcal H.
\tag{15}
\]

Readout stationarity also gives \(\sum_j\mu_jr_j\tanh z_j=0\). Equations (14)–(15) therefore hold in the actual physical model with no sample-count restriction in dimension two whenever \(q_1\ge q_2\). In particular, the stated \(q_1>q_2\) assumption for the ongoing \(p=2,3\) investigation is sufficient for this corollary; this note does not independently recount those dictionary dimensions.

What remains outside this note is the upper analysis: (15) must still be contradicted for a bad sample, or stronger local-minimum conditions must be used. The present theorem closes the physical lower-moment transfer obligation. It does not identify the full canonical upper dictionary with a polynomial surrogate, remove any retained initialized word, or turn a generic full-rank statement into a landscape proof.

## 7. Audit checklist for this result

- The input dimension is exactly two. The half-turn variation argument is not claimed in higher dimensions.
- The sample count is any finite \(m\); distinctness is modulo sign. Signed-compatible duplicate or antipodal samples may be combined before applying the theorem.
- Nonatomicity is used only for scalar splitting. The vector integrals are approximated by elementary finite partitions; no exact vector purification is assumed.
- The local lift controls both moment error and physical \(L^2\) displacement. Continuity of the actual finite loss, rather than exact moment attainment, closes the transfer.
- The covariance is inverted only on \(B_1\), so redundant marks cause no artificial invertibility assumption.
- All finite constant controls, probability weights, and switched controls are constructed on the fixed carrier. No spare independent coordinate or changed mark distribution is used.
- The original frozen reports are unchanged. Their previously unaudited Lyapunov/infinite-product route is unnecessary for the theorem proved here.

Status: complete informed proof candidate for the physical lift and its corollary, awaiting independent audit. The unrestricted upper gate-separation problem is not declared solved by this note.
