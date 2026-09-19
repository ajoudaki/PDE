# Independent alternative continuation attempt

Status: **incomplete**. The argument below proves a strong endpoint lemma, an exact monotone Volterra reformulation of the lower dynamics, and a pointwise readout envelope. It does not prove the forward-field exponential estimate required to continue the full stated activation class. No counterexample to continuation is obtained.

Scope: the mathematical inputs are exclusively the supervisor's problem statement. The required `solve-math-rigorously` and `investigate-conjectures` instructions and the latter's research-contract, adversarial-audit, and proof-search-orchestration references were read. No other study, book, maintained theory, code, experiment, or external theorem was used. This is one bounded independent attempt, with no Git operations.

## 1. Contract and notation

The target is the actual population Gaussian-matrix gradient flow with the same arbitrary fixed nonaffine \(C^{1,1}\) activation in both layers, bounded derivative, the two orthogonal inputs, the opposite labels, and all three trained parameter blocks. A successful result must continue the canonical local strong flow to \(T_\phi=\log(8)/(4q_0)\), preserve enough uniqueness and tails for the actual finite-width identification, and not infer continuation from a norm bound alone.

Write
\[
M=\|\phi'\|_\infty,\qquad a=|\phi(0)|,
\qquad U=(w_1,w_2,K,c).
\]
The Hilbert state space is
\[
\mathcal X=H_1^2\times\operatorname{HS}(H_1,H_2)\times H_2.
\]
The initialized Gaussian operator \(A_0\), with its actual adjoint, is fixed throughout. All the following deterministic identities apply on an existing strong interval. The supplied symmetry and loss identity give \(|r_a|\le1\). On an interval contained in \([0,T]\), define
\[
H_T=a+M(1+\sqrt T).
\]
The supplied energy estimate gives \(\|h_a(t)\|_2\le H_T\), \(\|c(t)\|_2\le\sqrt T\), and \(\|K(t)\|_{\rm HS}\le\sqrt T\).

## 2. The endpoint is a genuine Hilbert-space state

**Lemma 1.** The raw right-hand side \(F(U)\) is continuous on all of \(\mathcal X\), and maps bounded subsets into bounded subsets. Consequently, every strong solution on \([0,t_*)\) with \(t_*<\infty\) and the supplied energy bound has a strong endpoint \(U_*\in\mathcal X\). Moreover \(F(U(t))\to F(U_*)\), and the curve extended by \(U(t_*)=U_*\) is continuously differentiable from the left.

To check continuity, first note that \(u\mapsto\phi(u)\) is Lipschitz on \(L^2\), while \(u\mapsto\phi'(u)\) is bounded and Lipschitz on \(L^2\). The potentially difficult operation is multiplying a varying gate by an unbounded \(L^2\) field. If \(v_n\to v\) and \(z_n\to z\) in \(L^2\), then
\[
\begin{split}
\|v_n\phi'(z_n)-v\phi'(z)\|_2
&\le M\|v_n-v\|_2\\
&\quad+R\operatorname{Lip}(\phi')\|z_n-z\|_2
 +2M\|v\mathbf1_{\{|v|>R\}}\|_2.
\end{split}
\]
First choose \(R\) large, then let \(n\to\infty\). This proves the required continuity. Also
\[
\|A_nh_n-Ah\|_2
\le \|A_n\|\|h_n-h\|_2+
\|K_n-K\|_{\rm HS}\|h\|_2,
\]
and the analogous bound holds for the adjoints. Rank-one tensors are continuous because
\(\|u\otimes v\|_{\rm HS}=\|u\|_2\|v\|_2\).
These facts verify continuity of \(h,z,\delta,q,f,r\), hence of every component of \(F\).

On a bounded state set, \(h\) has bounded \(L^2\) norm by the linear growth of \(\phi\); \(A\), \(z\), \(f\), \(r\), \(\delta\), and \(q\) then have bounded norms in succession. The formulas for \(F\) give a finite bound for \(\|F(U)\|_{\mathcal X}\). This proves boundedness on bounded sets, without any coordinate-tail assumption.

The gradient-energy inequality gives
\[
\|U(t)-U(s)\|_{\mathcal X}
\le\sqrt{t-s}\left(\int_s^t\|U'(v)\|_{\mathcal X}^2\,dv\right)^{1/2}
\le\sqrt{t-s}.
\]
Thus \(U(t)\) is Cauchy as \(t\uparrow t_*\). Completeness gives \(U_*\). Continuity of \(F\) then proves \(U'(t)=F(U(t))\to F(U_*)\). The integral equation proves the left derivative at the endpoint.

This lemma **does not give a restart theorem**. A continuous vector field on an infinite-dimensional Hilbert space is not, merely by continuity, covered by the finite-dimensional Peano argument. In particular, the estimates above give no uniform exponential tails at \(U_*\), and the local canonical existence premise is not stated for arbitrary \(L^2\) initial states. Nevertheless, any alleged finite-time obstruction is now localized: neither norm blowup nor failure of the strong endpoint can be the obstruction.

## 3. Exact monotone lower-layer Volterra equation

Let \(J(x,g)\) solve
\[
\partial_xJ(x,g)=\phi'(J(x,g)),\qquad J(0,g)=g.
\]
The globally Lipschitz bounded scalar vector field gives a unique global solution for positive and negative \(x\): Picard iteration on a short interval is a contraction, its length depends only on \(\operatorname{Lip}(\phi')\), and the bound \(|J(x,g)-g|\le M|x|\) permits iteration for every finite interval. There is no division by \(\phi'\), including at zero gates.

Define
\[
F_g(x)=\phi(J(x,g)).
\]
An exact chain rule gives
\[
F_g'(x)=\phi'(J(x,g))^2\in[0,M^2].
\]
Thus \(F_g\) is monotone and globally \(M^2\)-Lipschitz, even if \(\phi\) is nonmonotone. Pointwise,
\[
\big(F_g(x)-F_g(y)\big)(x-y)
\ge M^{-2}|F_g(x)-F_g(y)|^2
\]
when \(M>0\); the present nonaffine class has \(M>0\). Integrating proves the same monotonicity and Lipschitz estimates for the Nemytskii map on \(H_1\).

Set
\[
X_a(t)=-\int_0^t r_a(v)q_a(v)\,dv.
\]
Then \(w_a(t)=J(X_a(t),g_a)\), by the scalar chain rule and uniqueness, and \(h_a(t)=F_{g_a}(X_a(t))\). Integrating the rank-one update gives
\[
K(t)=-\sum_b\int_0^t r_b(s)\delta_b(s)\otimes h_b(s)\,ds.
\]
Consequently, with the \(H_2\)-valued path
\[
u_a(t)=-\int_0^t r_a(v)\delta_a(v)\,dv,
\]
the exact lower equation is
\[
\begin{split}
X_a(t)&=A_0^*u_a(t)+v_a(t),\\
v_a(t)&=\sum_b\int_0^t\int_0^v
r_a(v)r_b(s)\langle\delta_b(s),\delta_a(v)\rangle\,h_b(s)\,ds\,dv.
\end{split}
\]
All integrals are Bochner integrals. On a finite existing strong interval they are justified by continuity and the displayed norm bounds. Fubini then gives pointwise versions almost everywhere.

The scalar coefficients in \(v_a\) satisfy
\[
|r_a(v)r_b(s)\langle\delta_b(s),\delta_a(v)\rangle|
\le M^2T.
\]
Thus, after the upper fields are fixed, the lower feature equation is a globally Lipschitz monotone scalar response to \(A_0^*u_a\), with a bounded causal integral kernel. This removes the troublesome lower-gate derivative from the local comparison. It does **not** turn \(A_0^*u_a\) into an independent Gaussian field: \(u_a\) depends on the same initialized matrix, including its transposed uses.

## 4. A pointwise envelope for the readout

**Lemma 2.** For \(t\le T\) in an existing strong interval, there are pointwise versions for which
\[
\sup_{0\le t\le T}|c(t)|
\le \cosh(2MH_TT)
\left[2aT+M\int_0^T\sum_{a=1}^2|A_0h_a(s)|\,ds\right]. \tag{1}
\]
For an interval ending before \(T\), replace the upper integration limits by its endpoint and retain the larger constants displayed here.

Indeed, the integrated rank-one formula gives
\[
|(K(t)h_a(t))(\omega_2)|
\le2MH_T^2\int_0^t|c(s,\omega_2)|\,ds.
\]
Since \(|\phi(z)|\le a+M|z|\), integration of the readout equation yields
\[
|c(t)|\le 2at+M\int_0^t\sum_a|A_0h_a(s)|\,ds
 +4M^2H_T^2\int_0^t(t-s)|c(s)|\,ds. \tag{2}
\]
The pointwise integrals are finite almost everywhere by the \(L^2\) estimates. Let \(B\) be the square bracket on the right of (1), and put \(\alpha=4M^2H_T^2\). Iterating (2) bounds its right-hand side by
\[
B\sum_{j=0}^{n}\frac{\alpha^jt^{2j}}{(2j)!}
 +\alpha^{n+1}\int_0^t\frac{(t-s)^{2n+1}}{(2n+1)!}|c(s)|\,ds.
\]
The last term tends to zero for almost every coordinate because its absolute value is at most
\(\alpha^{n+1}T^{2n+1}\int_0^T|c(s)|ds/(2n+1)!\).
Summing the series proves (1).

Here the needed source is a *time integral* of the forward frozen-operator fields; a supremum of those fields is unnecessary.

For example, if one could prove, uniformly along the reachable interval,
\[
\mathbb E\exp\big(|A_0h_a(t)|/B_T\big)\le2, \tag{3}
\]
then Jensen's inequality on the probability space \(\{1,2\}\times[0,T]\) gives
\[
\mathbb E\exp\left(\frac1{2TB_T}\int_0^T\sum_a|A_0h_a(t)|\,dt\right)\le2.
\]
Equation (1) then gives constants \(\eta_T>0\), \(C_T<\infty\) with
\(\mathbb E e^{\eta_T\sup_{t\le T}|c(t)|}\le C_T\).
This implies the required cutoff estimate, since for \(Z=\sup_{t\le T}|c(t)|\),
\[
\mathbb E[Z^2\mathbf1_{\{Z>R\}}]
\le16\eta_T^{-2}C_Te^{-\eta_TR/2}.
\]
The estimate follows from \(x^2e^{-\eta_Tx/2}\le16\eta_T^{-2}\) and \(x>R\).

## 5. A sufficient Gaussian-memory bridge, and the missing justification

A more structural sufficient statement would represent the actual forward fields as
\[
A_0h_a(t)=G_a(t)+\sum_b\int_0^t k_{ab}(t,s)\delta_b(s)\,ds, \tag{4}
\]
where \(G\) is a centered jointly Gaussian field with uniformly bounded variances and the causal kernels satisfy a deterministic bound \(|k_{ab}(t,s)|\le K_T<\infty\). Both the representation and its bound must be for the actual Gaussian matrix and actual adjoint, including all reuse correlations.

Under (4), \(|\delta_b|\le M|c|\) adds only another bounded Volterra term to (2). Hence (1) holds with altered constants and with \(A_0h_a\) replaced by \(G_a\). Gaussianity at each time already suffices for a subGaussian time-integrated source: if \(\mathbb E G_a(t)^2\le V_T\), then
\[
\mathbb E e^{G_a(t)^2/(4V_T)}\le\sqrt2.
\]
Cauchy--Schwarz in time followed by Jensen gives, for \(Y=\int_0^T\sum_a|G_a(t)|dt\),
\[
\mathbb E\exp\big(Y^2/(16T^2V_T)\big)\le\sqrt2.
\]
No independence across times or samples is needed. Thus a valid bounded-kernel version of (4) would actually yield subGaussian readout tails.

**Unresolved implication.** Neither (3), nor (4) with bounded causal kernels, has been proved here from the actual joint finite-program Gaussian limits plus the supplied energy bounds. Treating \(A_0h_a(t)\) as an independent Gaussian simply because \(A_0\) was initialized Gaussian is invalid: \(h_a(t)\) depends on transposed uses of the same matrix. In Gaussian-conditioning or dynamic-response expansions, the lower response is well controlled when the full upper path is fixed, but the response of that upper path contains terms of the form \(c\phi''(z)\). Bounded \(\phi'\), Lipschitz \(\phi'\), and \(\|c\|_2\) alone do not supply the asserted bound on the resulting kernels. Deriving that bound by assuming exponential moments of \(c\) would be circular.

A precise sufficient a priori lemma for this route is: for every finite \(T\), uniformly over initial canonical strong intervals contained in \([0,T]\), and over the bounded-energy approximation family used to construct or identify their continuation, the random variables
\[
\int_0^{T\wedge t_*}\sum_a|A_0h_a(t)|\,dt
\]
have an exponential moment with positive parameter and finite bound depending only on \(T\), \(\phi\), and the prescribed initialization law. This is a stronger sufficient statement than readout-tail control itself; it is **not claimed equivalent** to continuation and has not been established. Its approximation quantifier is needed to exclude proving only a tail property of a solution whose existence beyond the endpoint is already assumed.

## 6. Checks and final status

- For bounded \(\phi\), the readout directly satisfies \(|c(t)|\le2T\|\phi\|_\infty\); the upper-tail obstruction in this route is absent. This check does not cover all activations in the contract.
- The actual-adjoint operator is retained in every exact identity. No independent backward operator, frozen trainable block, altered loss, or time rescaling was substituted.
- The strong endpoint lemma uses continuity, not local Lipschitz continuity. Its proof therefore does not silently establish existence or uniqueness after the endpoint.
- The Volterra envelope is a proved source-to-tail estimate. It must not be reported as a proved source estimate.
- Gaussianity and a bounded-memory formula are conditional in Section 5. No Gaussian integration-by-parts or response theorem is being invoked without proof.
- The supplied feature-clock argument still gives loss \(\le e^{-4q_0t}\) on every strong interval, but this attempt does not prove that such an interval reaches \(T_\phi\).

Route registry: **blocked at the probabilistic source estimate**. The additional exact monotonicity of the transformed lower feature and the endpoint lemma may be reusable. Reopening this route requires a noncircular bound on the actual Gaussian reuse/response terms, or another proof of the integrated forward-field exponential estimate, with the required approximation control.
