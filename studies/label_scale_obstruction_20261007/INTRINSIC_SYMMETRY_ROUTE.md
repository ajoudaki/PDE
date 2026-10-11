# Intrinsic symmetry and rank-free endpoint coercivity

Status: exact symmetry and endpoint lemmas, with a conditional characteristic-support theorem. This is **not** a complete Gaussian fitting theorem for nonorthogonal data. The remaining construction and response-control obligations are stated in Section 7. No experiments were used.

The first round used only the supervisor's supplied model. The subsequent round was allowed, and read, the complete same-study files `GAUSSIAN_POSITIVE_GEOMETRY.md` and `GAUSSIAN_NONORTHOGONAL_EXTENSION.md`, and maintained-book III.F.1–11 in `docs/12-three-sample-learning.qmd`. No other scientific inputs were retrieved.

## 1. Model and target

Let the columns of \(X\in\mathbb R^{d\times m}\) be fixed unit vectors \(x_a\). The exact network is

\[
U=\tanh(AX),\qquad Z=WU,\qquad H=\tanh Z,\qquad
f=H^\top w/n,
\]

where \(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\), and \(w\in\mathbb R^n\). For fixed labels \(y\in\mathbb R^m\), put \(r=f-y\) and 
\(\mathcal L=\|r\|^2/m\). All parameters train by gradient flow with mobilities \((n,1,n)\), equivalently the parameter metric

\[
\|\Delta\theta\|_{\rm par}^2
=\|\Delta A\|_F^2/n+\|\Delta W\|_F^2+\|\Delta w\|^2/n.
\]

Initialization is independent \(A_{ij}\sim N(0,1)\), \(W_{ij}\sim N(0,1/n)\), and exactly \(w=0\).

The intended conclusion is that, for each fixed admissible dataset and label vector,

\[
\Pr\{\lim_{t\to\infty}\mathcal L_n(t)=0\}\longrightarrow1.
\]

The infinite-time limit here is the actual limit of each finite-width training trajectory. Population loss convergence alone is insufficient.

## 2. Transitive group symmetry allows many samples in dimension two

Let a finite group \(G\subset O(d)\) act transitively on the sample set. Let 
\(\chi:G\to\{\pm1\}\) be a real character that is trivial on the stabilizer of one sample \(x_0\). Define 
\(\sigma_a=\chi(Q)\) whenever \(x_a=Qx_0\); the stabilizer assumption makes this well defined. Fix any label amplitude \(\alpha>0\), and take \(y_a=\alpha\sigma_a\).

For \(Q\in G\), the transformation

\[
T_Q(A,W,w)=(AQ^{-1},W,\chi(Q)w)
\]

is a parameter isometry. It sends predictions to

\[
f_a(T_Q\theta)=\chi(Q)f_{Q^{-1}a}(\theta).
\]

Both the physical loss and the scalar functional

\[
g(\theta)=\frac1m\sum_a\sigma_af_a(\theta)
\]

are invariant under \(T_Q\). Their respective gradient fields are therefore equivariant. The initialized Gaussian law is invariant because \(AQ^{-1}\) has the same law as \(A\), and \(w=0\).

Consequently every finite prediction path has this symmetry **in law**. If these paths have a deterministic limit, that limit satisfies

\[
f_a(t)=\sigma_a g(t).
\tag{1}
\]

Indeed, invariance gives \(f_{Qa}=\chi(Q)f_a\), and transitivity determines the entire vector from one coordinate. This argument does not assert exact symmetry of a finite Gaussian realization or pathwise symmetry of a random subsequential limit.

A concrete mixed-sign family has arbitrarily many points with input rank two. Let \(k\ge3\) be odd. Let \(R\) rotate the plane by \(2\pi/k\), let \(S\) reflect across its first coordinate axis, and let

\[
x_0=(\cos\vartheta,\sin\vartheta),\qquad
\vartheta\notin\frac{\pi}{2k}\mathbb Z.
\]

Use the \(m=2k\) samples

\[
x_{j,+}=R^jx_0,\qquad x_{j,-}=R^jSx_0,
\qquad j=0,\ldots,k-1,
\]

with labels \(y_{j,+}=\alpha\), \(y_{j,-}=-\alpha\). The character is \(\chi(R)=1\), \(\chi(S)=-1\). The orbit is free, so the stabilizer condition holds. Points within either \(k\)-gon are not antipodal because \(k\) is odd. A coincidence between the two polygons would require \(\vartheta\in(\pi/k)\mathbb Z\); an antipodal pair between them would require \(\vartheta\in\pi/2+(\pi/k)\mathbb Z\). Both are excluded by the displayed choice. Thus all \(2k\) samples are distinct and nonantipodal.

This family lies outside every operator-norm ball of radius less than 1 about the \(m\times m\) identity Gram: its Gram has rank two and \(m>2\). Its labels are a specified character family, not arbitrary fixed label ratios.

## 3. Scalar ascent supplies a finite endpoint, conditional on population construction

Write \(u_a=\tanh(Ax_a)\), \(z_a=Wu_a\), \(h_a=\tanh z_a\), and 
\(b_a=w\odot\operatorname{sech}^2z_a\). Define

\[
\bar h=\frac1m\sum_a\sigma_ah_a,
\qquad g=\langle w,\bar h\rangle_n,
\qquad \langle v,q\rangle_n=v^\top q/n.
\]

For scalar ascent \(\theta'=\operatorname{grad}_{\rm par}g\), the exact equations are

\[
\begin{aligned}
w'&=\bar h,\\
W'&=\frac1m\sum_a\sigma_a b_a\otimes u_a,\\
A_j'&=\frac1m\sum_a\sigma_a\operatorname{sech}^2(A_j\cdot x_a)
          (W^\top b_a)_j x_a,
\end{aligned}
\tag{2}
\]

where \(b\otimes u=bu^\top/n\) at finite width. At population level the inner products are the layer \(L^2\) inner products, \(W^\top\) is the actual Hilbert adjoint, and \(b\otimes u\) is the corresponding rank-one operator.

At finite width this ascent is global. In fact

\[
\|w(s)\|_\infty\le s,\qquad
\|W'(s)\|_F\le s,\qquad
\|W(s)\|_{\rm op}\le\|W_0\|_{\rm op}+s^2/2,
\]

and the third equation gives
\(\|A'(s)\|_F/\sqrt n\le s\|W(s)\|_{\rm op}\). These estimates preclude finite-time escape of the finite smooth ODE.

The supplied scalar readout-linearity lemma says that, along any constructed strong global population version of (2),

\[
q_0:=\|\bar h(0)\|_2^2>0
\quad\Longrightarrow\quad
g'(s)\ge q_0.
\]

It gives a unique finite target endpoint \(g(s_*)=\alpha\), with 
\(s_*\le\alpha/q_0\). Under (1), the physical population flow is its time change

\[
\dot s=2(\alpha-g(s)),\qquad
\mathcal L_\infty(t)\le\alpha^2e^{-4q_0t}.
\tag{3}
\]

Identification of this time change with the actual initialized population flow requires an existence/uniqueness or finite-width identification argument; symmetry in law is not that argument.

For distinct nonantipodal samples, \(q_0>0\). Section 4 proves positivity of the initial first-feature Gram. The initial top preactivation therefore has a nonsingular Gaussian sample law. The continuous function 
\(z\mapsto m^{-1}\sum_a\sigma_a\tanh z_a\) is not identically zero on \(\mathbb R^m\), so its squared expectation under that full-support Gaussian law is positive.

## 4. Full first-feature support implies a rank-free middle-layer gap

First, the ridge functions \(p\mapsto\tanh(p\cdot x_a)\) are linearly independent whenever the nonzero vectors \(x_a\) are distinct and nonantipodal unit vectors. Choose \(v\in\mathbb R^d\) outside the finitely many hyperplanes

\[
v\cdot x_a=0,\qquad v\cdot(x_a-x_b)=0,
\qquad v\cdot(x_a+x_b)=0.
\]

Then \(t_a=v\cdot x_a\) are nonzero and their squares are pairwise distinct. If 
\(\sum_ac_a\tanh(p\cdot x_a)=0\) for all \(p\), restriction to \(p=tv\) and derivatives at zero give

\[
\sum_a c_at_a^{2r+1}=0,
\qquad r=0,\ldots,m-1.
\]

All the relevant odd Taylor coefficients of tanh are nonzero: writing 
\(\tanh t=\sum_{r\ge0}(-1)^r\beta_rt^{2r+1}\), the equation 
\((\tanh t)'=1-\tanh^2t\) gives \(\beta_0=1\) and

\[
(2r+1)\beta_r=\sum_{p+q=r-1}\beta_p\beta_q>0
\qquad(r\ge1).
\]

The Vandermonde matrix in the distinct \(t_a^2\) is invertible, so \(c_at_a=0\) and \(c=0\).

It follows that any full-support first-row law 
\(p\in\mathbb R^d\) gives

\[
K_U=[\mathbb E\tanh(p\cdot x_a)\tanh(p\cdot x_b)]_{ab}\succ0.
\tag{4}
\]

Indeed a zero quadratic form would make the continuous function 
\(\sum_ac_a\tanh(p\cdot x_a)\) vanish almost surely, hence everywhere by full support, contradicting the proved independence.

Now consider any finite or strong population state with \(K_U\succ0\) and \(w\ne0\). Let \(K_b=[\langle b_a,b_b\rangle]_{ab}\). The middle-layer tangent Gram is

\[
K_W=K_U\odot K_b.
\]

If \(\lambda=\lambda_{\min}(K_U)>0\), then

\[
K_W\succeq\lambda\,\operatorname{diag}
       (\|b_1\|_2^2,\ldots,\|b_m\|_2^2)\succ0.
\tag{5}
\]

To verify the first inequality, the Hadamard product of two positive semidefinite matrices is a Gram matrix: if their entries are 
\(\langle v_a,v_b\rangle\) and \(\langle q_a,q_b\rangle\), their product is the Gram of \(v_a\otimes q_a\). Apply this fact to 
\(K_U-\lambda I\) and \(K_b\). For the strict inequality, 
\(b_a=w\operatorname{sech}^2z_a\ne0\), since \(w\ne0\) and the gate is strictly positive at every finite preactivation. An \(L^2\) preactivation is finite almost surely.

At a scalar target endpoint \(g(s_*)=\alpha>0\), necessarily \(w\ne0\). Thus preserving full first-feature support through that finite endpoint is sufficient for a positive tangent gap in **every** sample direction. No input-rank assumption, top-feature Fourier calculation, or first-layer tangent estimate is needed.

## 5. A conditional characteristic theorem preserves full support

The following is an exact implication, not an assertion that its hypotheses have been proved for the uncut initialized network. In (6)–(8), \(t\) is the scalar-ascent clock \(s\) from (2), not physical training time.

Fix \(T<\infty\). Suppose the actual first-layer reverse fields admit the representation

\[
B_a(t):=W(t)^*b_a(t)
=\zeta_a(t)+\sum_c\int_{[0,t]}u_c(s)\,R_{ac}(t,ds),
\tag{6}
\]

on a common probability space. Assume:

- The Gaussian source tuple \(\zeta\) is independent of the Gaussian first-row root \(p_0\sim N(0,I_d)\), and has jointly measurable paths with 
  \(\sum_a\int_0^T|\zeta_a(t)|dt<\infty\) almost surely.
- The \(R_{ac}(t,\cdot)\) are deterministic finite signed measures, jointly measurable in the sense needed for the integrals, supported on \([0,t]\), with
  \[
  \int_0^T\sum_{a,c}\|R_{ac}(t,\cdot)\|_{\rm TV}\,dt<\infty.
  \tag{7}
  \]
- Conditional on the source paths, the first row obeys the characteristic equation obtained by substituting (6) into (2), with 
  \(u_c(s)=\tanh(p(s)\cdot x_c)\).

Then the law of \(p(t)\) has full support in \(\mathbb R^d\) for every \(0\le t\le T\).

Here is a proof including the needed well-posedness. Fix any source realization satisfying the first assumption. The characteristic velocity has absolute value at most

\[
M(t)=\frac1m\left(
\sum_a|\zeta_a(t)|+
\sum_{a,c}\|R_{ac}(t,\cdot)\|_{\rm TV}\right),
\]

which is integrable. If \(V[p](t)\) denotes this velocity evaluated on a path \(p\), boundedness and Lipschitzness of tanh and \(\operatorname{sech}^2\) give

\[
|V[p](t)-V[\widetilde p](t)|
\le L(t)\sup_{s\le t}|p(s)-\widetilde p(s)|,\qquad
L(t)=\frac1m\left(2\sum_a|\zeta_a(t)|
+3\sum_{a,c}\|R_{ac}(t,\cdot)\|_{\rm TV}\right).
\]

Here the first gate difference contributes at most twice the path difference times the source-plus-memory bound, and the memory difference contributes the additional total-variation term. Thus \(L\) is integrable. Picard iteration on consecutive intervals with \(\int L<1\) is a contraction in the supremum norm, with the already constructed past held fixed, and gives a unique global absolutely continuous solution. The bound by \(M\) prevents escape on each such interval. For two initial roots, the same inequality and integral Gronwall give
\(\sup_{s\le t}|p(s)-\widetilde p(s)|
\le |p_0-\widetilde p_0|\exp(\int_0^t L)\).
This proves continuous dependence on \(p_0\). No inverse of the data Gram appears.

For every initial root, the displacement satisfies

\[
|p(t;p_0)-p_0|\le D_T:=\int_0^T M(s)ds<\infty,
\tag{8}
\]

and \(D_T\) does not depend on \(p_0\). The continuous map 
\(F_t:p_0\mapsto p(t;p_0)\) is therefore onto. To see this, fix a target \(q\in\mathbb R^d\). The map

\[
p_0\longmapsto q-[F_t(p_0)-p_0]
\]

maps the closed Euclidean ball of radius \(|q|+D_T+1\) into itself. The finite-dimensional Brouwer fixed-point theorem, which applies to a continuous self-map of a nonempty compact convex ball, supplies a fixed point. At it \(F_t(p_0)=q\).

Every nonempty open set \(O\subset\mathbb R^d\) has a nonempty open preimage \(F_t^{-1}(O)\). The conditional law of \(p_0\) is still a full-support Gaussian, by independence of the sources. Therefore 
\(\Pr(p(t)\in O\mid\zeta)>0\) for almost every source realization. Averaging proves the unconditional full-support claim. This argument uses surjectivity, not a backward-uniqueness assertion for a memory equation.

Combining this theorem with (4)–(5) proves strict endpoint coercivity at any finite scalar target under assumptions (6)–(7).

## 6. A positive endpoint gap would transfer to actual infinite-time fitting

Suppose a deterministic strong scalar endpoint has been constructed and identified, the associated physical flow satisfies (3), and finite-width physical predictions and the readout-plus-middle Gram converge on every fixed compact time interval. Assume (6)–(7) hold through the scalar endpoint, so (5) gives a deterministic positive endpoint gap.

Only one late, fixed physical time is then needed for the width limit. The subsequent infinite interval is controlled by exact finite-width inequalities, as follows.

At a finite reference state with \(\|w_*\|_\infty\le S\), 
\(\|W_*\|_{\rm op}\le M\), each sample's readout and middle tangent features are \(h_a\) and \(b_a\otimes u_a\). For parameter distance 
\(\rho=\|\theta-\theta_*\|_{\rm par}\), their normalized differences obey

\[
\|u_a-u_{*,a}\|_{2,n}\le\rho,
\quad
\|h_a-h_{*,a}\|_{2,n}\le(1+M)\rho,
\]

\[
\|b_a-b_{*,a}\|_{2,n}
\le[1+2S(1+M)]\rho.
\]

The last inequality uses the bounded reference readout:

\[
b_a-b_{*,a}=(w-w_*)\operatorname{sech}^2z_a
+w_*[\operatorname{sech}^2z_a-\operatorname{sech}^2z_{*,a}].
\]

The rank-one difference identity gives the same width-independent local continuity for the middle tangent features. Thus a positive Gram gap persists on a parameter ball of positive, width-independent radius determined by \(S,M,m\), and the gap. The argument uses only unit input norms, so it applies to the rank-two orbit.

If this ball has Gram lower bound \(\kappa I\), and the residual at its center satisfies \(\|r(T)\|<\rho\sqrt\kappa\), gradient flow remains in the ball. Indeed

\[
\|\dot\theta\|_{\rm par}
=\frac2m\sqrt{r^\top Kr}
\le-\frac1{\sqrt\kappa}\frac{d}{dt}\|r\|.
\]

Its remaining path length is less than \(\rho\), so a first exit is impossible. Exact loss dissipation then gives

\[
\mathcal L_n(t)\le\mathcal L_n(T)e^{-4\kappa(t-T)/m}
\qquad(t\ge T).
\]

By (3), the population residual can be made arbitrarily small while approaching the finite endpoint with its positive gap. Compact-time convergence transfers a strict capture condition to the actual finite-width flow with probability tending to one. Readout and middle-operator bounds at \(T\) follow from the exact accumulated-residual bounds; their population limit is controlled by the finite feature endpoint.

This conditional implication yields the intended order of limits. It does not claim that convergence of predictions alone supplies the endpoint Gram or basin entry.

## 7. What is still missing

The maintained fixed-program theorem in III.F does apply to every fixed capped Euler transcript for the nonorthogonal model. Roots may be correlated or singular across samples; matrix and transpose reuse are allowed; limiting empirical laws are deterministic. Its source rule also yields a discrete version of (6), with deterministic response coefficients multiplying earlier first features.

The learned part of that representation is explicitly controlled. Scalar ascent gives

\[
(W(t)-W_0)^*b_a(t)
=\frac1m\sum_c\sigma_c\int_0^t
  \langle b_c(s),b_a(t)\rangle\,u_c(s)ds.
\]

Its kernel is bounded on every finite feature horizon because 
\(\|b_c(s)\|_2\le s\). The Gaussian source in a valid uncut representation has covariance 
\(\mathbb E\zeta_a(t)\zeta_c(s)=\langle b_a(t),b_c(s)\rangle\), so the source integrability condition would follow from its bounded variances and Fubini. Direct same-time response atoms are allowed by the measure formulation in (6).

The missing estimate is the total variation of the **adaptive initialized-action response** as the Euler mesh is refined and the caps are removed. Fixed-mesh finiteness does not imply the uniform bound (7). The book's bounded common \(L^2\) action does not imply (7), and the orthogonal natural-coordinate argument does not prove it for these rank-two data.

Also missing is a complete construction and identification of the uncut strong scalar and physical population flows, or another compact-time approximation theorem with the required feature/Gram observations. The characteristic theorem above is a consequence of a specified response representation; it does not solve the self-consistent response/covariance system by itself.

Accordingly the route status is **conditional, with a concrete endpoint mechanism**. Established here are the transitive rank-two mixed-sign family, exact symmetry in law, the rank-free middle-layer endpoint inequality (5), and preservation of full first-layer support under the stated integrable-response characteristic model. Arbitrary-amplitude finite-width fitting for this family remains unproved until the uncut population construction and response bound are supplied. Arbitrary label ratios remain outside this character family even if those gaps are closed.
