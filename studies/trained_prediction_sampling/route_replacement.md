# Second-phase route: replacement differences and Hoeffding projection

**Status:** conditional theorem, proved below. It does not establish the required law-response bounds for the neural flow. It does show that bounded second law derivatives, or the weaker second finite-difference conditions in Section 6, together with qualitative weak continuity of the first atom response suffice for the full sample expansion, including an \(L^2\) remainder. No quantitative rate for weak empirical convergence or for state perturbations is needed.

**Provenance:** this is a second-phase investigation following the frozen independent `route_statistical.md` (SHA256 `715877198a4b2231a854d841d9ffa1f6d0cb514ca489467bc90557b03eb33b61`). The supervisor then proposed a distinct route using replacement differences, mixed-law bias telescoping, first Hoeffding projections, and a finite-test cutoff. That proposal is an explicit additional input to this report. No other scientific material, other route report, external source, or Git history was read. Only this report was written during this phase; no experiments were run.

## 1. The sufficient local theorem (C² version; weakened in Section 6)

Let \(\mathcal Z\) be a compact metric space, \(H\) a separable real Hilbert space, and \(\mu\) a Borel probability on \(\mathcal Z\). Let \(U\) be a \(W_1\)-open neighborhood of \(\mu\). Suppose \(F:U\to H\) is bounded and Borel measurable; weak continuity of \(F\), as supplied in the motivating application, is more than enough for measurability.

The required differentiability concerns actual mixtures of probability laws, not an open ball in a Banach space of signed measures. Assume there are strongly measurable kernels

\[
 I_Q:\mathcal Z\to H,\qquad
 J_Q:\mathcal Z^2\to H,\qquad Q\in U,
\]

with the following properties.

**L1. Actual mixture calculus with an integral representation.** For every finite-dimensional affine family \(Q_s\) of probability measures lying in \(U\), the map \(s\mapsto F(Q_s)\) is twice continuously differentiable on its admissible parameter domain, with the corresponding one-sided limits at boundaries. If its coordinate directions are zero-mass finite signed measures \(\eta_i\), its derivatives are

\[
 \partial_i F(Q_s)=\int I_{Q_s}(z)\,\eta_i(dz),
\]

\[
 \partial_i\partial_jF(Q_s)
       =\iint J_{Q_s}(z,z')\,\eta_i(dz)\eta_j(dz').
\tag{1.1}
\]

All integrals are Bochner integrals, and \(\int I_Q\,dQ=0\). It is enough to require this calculus on the mixture segments, two-coordinate replacement rectangles, and finite-test cutoff products used in the proof. The stated version is convenient and explicit.

In particular,

\[
 I_Q(z)=\left.\frac d{d\epsilon}
 F((1-\epsilon)Q+\epsilon\delta_z)\right|_{\epsilon=0+}
\tag{1.2}
\]

is the actual centered contamination influence. The integral representation in (1.1) matters: bounded TV-linear functionals on the space of measures need not commute with integrating their atom values against a nonatomic law. Actual dynamic response kernels should supply this representation directly.

**L2. Uniform second-response bound.** For a finite \(M\),

\[
 \sup_{Q\in U}\sup_{z,z'\in\mathcal Z}\|J_Q(z,z')\|_H\le M.
\tag{1.3}
\]

An equivalent sufficient condition is a uniform bound \(M\|\eta\|_{\rm TV}\|\xi\|_{\rm TV}\) on the bilinear second derivative, together with (1.1). Here \(\|\delta_z-\delta_{z'}\|_{\rm TV}\le2\). Essential bounds are enough only if versions valid at every atom/diagonal used by the statistic have been specified; empirical measures visit those values.

**L3. Qualitative continuity of the atom response at the target law.** As \(Q\to\mu\) in \(W_1\), with \(Q\in U\), require

\[
 \|I_Q-I_\mu\|_{L^2(\mu;H)}\longrightarrow0.
\tag{1.4}
\]

This is continuity under the fixed reference measure \(\mu\), not \(L^2(Q)\). Joint \(W_1\)-continuity in \(Q\) and continuity in the atom \(z\), with uniform bounds on a compact neighborhood, imply (1.4). Pointwise continuity in \(Q\) for every atom plus a uniform bound also suffices by dominated convergence. No modulus or rate is needed.

For iid \(Z_1,Z_2,\ldots\sim\mu\), let \(\mu_m=m^{-1}\sum_i\delta_{Z_i}\). Then there is a bounded global extension \(\widetilde F\) agreeing with \(F\) on a neighborhood of \(\mu\) such that

\[
 \widetilde F(\mu_m)-F(\mu)
    =\frac1m\sum_{i=1}^m I_\mu(Z_i)+r_m,
 \qquad m\mathbb E\|r_m\|_H^2\longrightarrow0.
\tag{1.5}
\]

The mismatch event \(\{\widetilde F(\mu_m)\ne F(\mu_m)\}\), wherever the latter is defined, has exponentially small probability. If the actual \(F(\mu_m)\) is defined on all outcomes, (1.5) holds in probability for that actual statistic as well. The \(L^2\) conclusion also transfers when the actual endpoint is uniformly bounded, or more generally when its squared size on the mismatch event is \(o(m^{-1})\) in expectation.

Consequently, under that interpretation of the statistic,

\[
 \sqrt m\,[F(\mu_m)-F(\mu)]\Rightarrow
       \mathcal N_H(0,C_\mu),\qquad
 C_\mu h=\int\langle I_\mu(z),h\rangle I_\mu(z)\,\mu(dz).
\tag{1.6}
\]

This applies separately to each \(\mu\) satisfying L1--L3. A statement for every Borel law still requires verifying those hypotheses and actual flow identification at every such law.

## 2. First prove the global version

Assume temporarily that \(F\) and the mixture calculus are defined on all probability laws, \(F\) is bounded, and both first and second kernels have uniform bounds. Write \(\|J_Q(z,z')\|\le M\). Only the second bound enters the rates; the first bound supplies integrability and the dominated-convergence step.

### 2.1 Bias is \(O(m^{-1})\)

Introduce the random mixed laws

\[
 \nu_i=\Bigl(1-\frac im\Bigr)\mu+
                  \frac1m\sum_{j=1}^i\delta_{Z_j},
 \quad 0\le i\le m.
\]

Thus \(\nu_0=\mu\), \(\nu_m=\mu_m\), and

\[
 \nu_i-\nu_{i-1}=m^{-1}(\delta_{Z_i}-\mu).
\]

Every interpolation between these consecutive laws remains a probability measure. Taylor's integral formula and (1.3) give

\[
 F(\nu_i)-F(\nu_{i-1})
 =\frac1m\int I_{\nu_{i-1}}(z)(\delta_{Z_i}-\mu)(dz)+R_i,
 \qquad \|R_i\|_H\le\frac{2M}{m^2}.
\tag{2.1}
\]

Conditional on \(Z_1,\ldots,Z_{i-1}\), the first term has mean zero because \(Z_i\) has law \(\mu\) and the derivative is represented by an integrable kernel. Summing the expectations of (2.1) gives

\[
 b_m:=\mathbb EF(\mu_m)-F(\mu),\qquad
 \|b_m\|_H\le\frac{2M}{m}.
\tag{2.2}
\]

This step controls the bias separately. Small replacement differences alone control variance and do not imply that the statistic is centered at \(F(\mu)\).

### 2.2 Second replacements are \(O(m^{-2})\)

Let \(T_m=F(\mu_m)\). For an independent replacement sample \(Z_i'\), write \(T_m^{(i)}\) for the statistic with \(Z_i\) replaced by \(Z_i'\), and define

\[
 D_{ij}T_m=T_m-T_m^{(i)}-T_m^{(j)}+T_m^{(ij)}.
\]

For \(i\ne j\), keep all other data fixed and use the affine rectangle with the \(i\)-th and \(j\)-th atoms independently mixed between original and replacement. Every point in this rectangle is a probability law. Its direction measures are

\[
 \eta=m^{-1}(\delta_{Z_i'}-\delta_{Z_i}),\qquad
 \xi=m^{-1}(\delta_{Z_j'}-\delta_{Z_j}).
\]

Twice applying the fundamental theorem of calculus and using (1.1) gives

\[
 \|D_{ij}T_m\|_H\le M\|\eta\|_{\rm TV}\|\xi\|_{\rm TV}
                   \le\frac{4M}{m^2}.
\tag{2.3}
\]

This is a deterministic estimate, including repeated observations and atomic laws.

### 2.3 A Hilbert-valued Hoeffding bound, proved directly

For a square-integrable function \(T=T(Z_1,\ldots,Z_m)\), define for \(S\subset\{1,\ldots,m\}\)

\[
 T_S=\sum_{A\subset S}(-1)^{|S|-|A|}\,
                   \mathbb E[T\mid Z_i:i\in A].
\tag{2.4}
\]

The empty conditional expectation is \(\mathbb ET\). Finite inclusion--exclusion gives \(T=\sum_ST_S\): the coefficient of each proper conditional expectation cancels. Integrating \(T_S\) over any one coordinate in \(S\) gives zero, by pairing terms in (2.4) that include that coordinate with terms that omit it. If \(S\ne R\), choose a coordinate in one set but not the other and condition on all remaining coordinates; this zero-mean property proves \(\mathbb E\langle T_S,T_R\rangle_H=0\).

Let

\[
 R^{\rm H}=T-\mathbb ET-
       \sum_{i=1}^m(\mathbb E[T\mid Z_i]-\mathbb ET)
       =\sum_{|S|\ge2}T_S.
\]

For a fixed pair \(i,j\), the double replacement kills components not containing both coordinates. For a component containing both, its four replacement terms have equal second moments and are pairwise orthogonal: two distinct terms differ in at least one independent centered coordinate. Components from distinct sets remain orthogonal after replacement, using a coordinate in their symmetric difference. Therefore

\[
 \mathbb E\|D_{ij}T\|_H^2
       =4\sum_{S\supset\{i,j\}}\mathbb E\|T_S\|_H^2.
\]

Sum over \(i<j\). Each \(S\) with \(|S|\ge2\) occurs \(\binom{|S|}{2}\ge1\) times. Orthogonality yields

\[
 \mathbb E\|R^{\rm H}\|_H^2
       \le\frac14\sum_{i<j}\mathbb E\|D_{ij}T\|_H^2.
\tag{2.5}
\]

Apply this with \(T=T_m\) and (2.3):

\[
 \mathbb E\|R_m^{\rm H}\|_H^2
 \le\frac14\binom m2\frac{16M^2}{m^4}
 \le\frac{2M^2}{m^2}.
\tag{2.6}
\]

### 2.4 Identify the first projection with the actual influence

Symmetry of the empirical statistic permits the definition

\[
 h_m(z)=m\{\mathbb E[T_m\mid Z_1=z]-\mathbb ET_m\},
 \qquad \int h_m\,d\mu=0.
\]

Let the random probability law

\[
 Q_m=\frac1m\mu+\frac1m\sum_{j=2}^m\delta_{Z_j}
\]

depend only on the other samples. For every \(z\), both \(Q_m\) and \(Q_m+m^{-1}(\delta_z-\mu)\) are probability laws. Taylor's formula gives

\[
 F\bigl(Q_m+m^{-1}(\delta_z-\mu)\bigr)
 =F(Q_m)+m^{-1}\Bigl[I_{Q_m}(z)-\int I_{Q_m}\,d\mu\Bigr]
                 +\varepsilon_m(z),
 \quad\|\varepsilon_m(z)\|_H\le2M/m^2.
\]

Average over the other samples, subtract the same expression averaged over \(z\sim\mu\), and multiply by \(m\). This proves

\[
 h_m(z)=\mathbb E\Bigl[I_{Q_m}(z)-\int I_{Q_m}\,d\mu\Bigr]+e_m(z),
 \qquad \sup_z\|e_m(z)\|_H\le4M/m.
\tag{2.7}
\]

The laws \(Q_m\) converge to \(\mu\) in \(W_1\) in probability. For completeness, on a compact space a finite continuous partition of unity as constructed in Section 3 reduces \(W_1\)-distance, up to an arbitrarily small deterministic error, to finitely many empirical averages of bounded continuous functions. Their variances tend to zero. The extra mass \(\mu/m\) in \(Q_m\) has no effect on this conclusion.

By (1.4) and the uniform first-kernel bound,

\[
 \mathbb E\|I_{Q_m}-I_\mu\|_{L^2(\mu;H)}^2\longrightarrow0.
\]

Indeed, continuity makes the integrand tend to zero in probability, and boundedness makes it uniformly bounded; splitting at any fixed small threshold proves expectation convergence. Since \(\mu I_\mu=0\), Jensen's inequality and (2.7) now show

\[
 \|h_m-I_\mu\|_{L^2(\mu;H)}\longrightarrow0.
\tag{2.8}
\]

The minimal continuity needed here is that of the gauge-invariant kernel \(I_Q-\mu I_Q\) in \(L^2(\mu;H)\); (1.4) is a transparent sufficient assumption.

### 2.5 Assemble the expansion in \(L^2\)

The Hoeffding decomposition reads

\[
 T_m-F(\mu)=b_m+\frac1m\sum_i h_m(Z_i)+R_m^{\rm H}.
\]

Subtract \(m^{-1}\sum_iI_\mu(Z_i)\), defining the difference as \(r_m\). The deterministic bias, the first-coordinate sum, and the higher-order remainder are mutually orthogonal in \(L^2\). The summands of the first-coordinate sum are independent and centered. Consequently the following identity holds:

\[
 m\mathbb E\|r_m\|_H^2
   =m\|b_m\|_H^2+m\mathbb E\|R_m^{\rm H}\|_H^2
                  +\|h_m-I_\mu\|_{L^2(\mu;H)}^2.
\tag{2.9}
\]

Equations (2.2), (2.6), and (2.8) make the right-hand side tend to zero. This proves the global theorem, with only qualitative convergence in the final term. In particular, a poor or unknown modulus in (1.4) does not obstruct asymptotic linearity.

## 3. Constructing the cutoff inside \(U\)

### 3.1 Finitely many continuous law tests suffice

Choose \(\rho>0\) such that \(B_{W_1}(\mu,\rho)\subset U\), and let \(D>0\) be the diameter of \(\mathcal Z\). A one-point space is trivial. Choose a finite \(\epsilon\)-net \(z_1,\ldots,z_N\), with \(\epsilon=\rho/16\), and define

\[
 a_j(z)=(2\epsilon-d(z,z_j))_+,
 \qquad \psi_j(z)=\frac{a_j(z)}{\sum_k a_k(z)}.
\]

The denominator is at least \(\epsilon\), each \(\psi_j\) is continuous with values in \([0,1]\), and \(\sum_j\psi_j=1\). If \(\psi_j(z)>0\), then \(d(z,z_j)<2\epsilon\). For any law \(Q\), let \(Q^d=\sum_j(Q\psi_j)\delta_{z_j}\). Sending a point \(z\) to \(z_j\) with probabilities \(\psi_j(z)\) couples \(Q\) and \(Q^d\) at cost at most \(2\epsilon\). Matching common mass in two discrete laws and transporting the remainder at cost at most \(D\) gives

\[
 W_1(Q,\mu)\le4\epsilon+
              \frac D2\sum_j|Q\psi_j-\mu\psi_j|.
\tag{3.1}
\]

Put \(b=\rho/(2DN)\). If \(\max_j|Q\psi_j-\mu\psi_j|\le b\), then (3.1) gives \(W_1(Q,\mu)\le\rho/2\).

Take a smooth scalar function \(\chi_0\) with \(0\le\chi_0\le1\), equal to one on \([-1/2,1/2]\), positive on \((-1,1)\), and zero off \((-1,1)\). Define

\[
 \chi(Q)=\prod_{j=1}^N
       \chi_0\bigl((Q\psi_j-\mu\psi_j)/b\bigr).
\tag{3.2}
\]

Its support lies in \(B_{W_1}(\mu,\rho)\), with a positive margin. It equals one on the finite-test neighborhood

\[
 V=\{Q:\max_j|Q\psi_j-\mu\psi_j|<b/2\}.
\]

Its first and second law derivatives have bounded continuous kernels, since they are finite sums of products of the bounded functions \(\psi_j\) and bounded derivatives of \(\chi_0\). For example the first uncentered kernel is

\[
 a_Q(z)=\sum_j (\partial_j\widehat\chi)(Q\psi_1,\ldots,Q\psi_N)\psi_j(z),
\]

with the analogous second kernel
\(b_Q(z,z')=\sum_{j,k}\partial_j\partial_k\widehat\chi\,\psi_j(z)\psi_k(z')\).
These symbols describe only the cutoff derivatives.

### 3.2 The first derivative is bounded on the cutoff support

A separate uniform first-response assumption can be avoided. Let \(B=\sup_{Q\in U}\|F(Q)\|_H\), and choose

\[
 \tau=\min\{1/2,\rho/(4D)\}>0.
\]

For any law \(Q\) in the cutoff support, \(W_1(Q,\mu)\le\rho/2\). The contamination path \(Q_s=(1-s)Q+s\delta_z\), \(0\le s\le\tau\), satisfies

\[
 W_1(Q_s,\mu)\le\rho/2+sD\le3\rho/4<\rho.
\]

Taylor's formula, (1.2), and (1.3) give

\[
 \|\tau I_Q(z)\|_H
  \le\|F(Q_\tau)-F(Q)\|_H+2M\tau^2
  \le2B+2M\tau^2.
\]

Thus uniformly on the cutoff support and over atoms,

\[
 \|I_Q(z)\|_H\le2B/\tau+2M\tau.
\tag{3.3}
\]

This is why bounded \(F\), a neighborhood with positive margin, and a bounded second derivative are enough to control the first derivative where needed.

### 3.3 Product and zero extension

Define on all probability laws

\[
 \widetilde F(Q)=
 \begin{cases}
   \chi(Q)F(Q),&Q\in U,\\
   0,&Q\notin U.
 \end{cases}
\]

It is bounded. Its first uncentered derivative kernel on \(U\) is

\[
 A_Q(z)=\chi(Q)I_Q(z)+F(Q)a_Q(z),
\]

and a second kernel is

\[
 B_Q(z,z')=\chi(Q)J_Q(z,z')+
       a_Q(z)I_Q(z')+a_Q(z')I_Q(z)+F(Q)b_Q(z,z').
\tag{3.4}
\]

Subtracting \(QA_Q\) from the first kernel centers it without changing derivatives in zero-mass directions. Equations (3.3)--(3.4) give uniform bounds for the first and second kernels. All cutoff derivatives vanish on the boundary of its support; its support lies strictly inside \(U\). The product and zero extension consequently retain the mixture calculus on all probability laws. This follows directly along any affine parameter family: outside the support the function and first two derivatives are zero, and their limits at a boundary are zero by the vanishing cutoff derivatives and the uniform bounds just proved.

On \(V\), \(\widetilde F=F\), \(\chi=1\), and the first and second cutoff derivatives vanish. The actual centered first response there equals \(I_Q\); in particular \(\widetilde I_\mu=I_\mu\), and (1.4) remains valid. The global theorem therefore applies to \(\widetilde F\).

### 3.4 The mismatch probability is exponentially small

Each \(\psi_j(Z_i)\) lies in \([0,1]\). For a centered variable with range length one, the log moment-generating function has second derivative equal to a tilted variance, at most \(1/4\). Its value and first derivative vanish at zero, so it is at most \(\lambda^2/8\). Exponential Markov, independence, and optimization then give

\[
 \mathbb P\bigl(|\mu_m\psi_j-\mu\psi_j|\ge b/2\bigr)
       \le2e^{-mb^2/2}.
\]

Taking a union bound,

\[
 \mathbb P(\mu_m\notin V)\le2N e^{-mb^2/2}.
\tag{3.5}
\]

Whenever \(\mu_m\in V\), the actual and cutoff statistics agree. This proves transfer in probability without a tail-size bound on the mismatch event. If the actual endpoint is bounded by \(B_*\) on all outcomes, then

\[
 m\mathbb E\|F(\mu_m)-\widetilde F(\mu_m)\|_H^2
       \le m(B_*+B)^2\,2N e^{-mb^2/2}\longrightarrow0,
\]

which proves the stated \(L^2\) transfer. If the actual endpoint is not defined outside \(U\), the theorem establishes only the bounded extension until that existence issue is resolved.

## 4. Hilbert CLT without an additional empirical-process theorem

The first kernel at \(\mu\) is bounded by (3.3) and centered, so \(I_\mu\in L^2(\mu;H)\). Its covariance \(C_\mu\) in (1.6) is positive and self-adjoint, and for any orthonormal basis \((e_j)\), Tonelli and Parseval give

\[
 \operatorname{tr}C_\mu
 =\sum_j\int|\langle I_\mu(z),e_j\rangle|^2\mu(dz)
 =\int\|I_\mu(z)\|_H^2\mu(dz)<\infty.
\]

The corresponding centered Hilbert Gaussian exists by the spectral series with coefficients \(\sqrt{\lambda_j}\) times independent scalar standard normals; summability of the \(\lambda_j\) gives convergence in \(L^2\). For every finite-dimensional projection, the iid CLT follows from the second-order expansion of the scalar characteristic function in each direction. The tail projection has second moment

\[
 \mathbb E\Big\|(1-\Pi_N)m^{-1/2}\sum_iI_\mu(Z_i)\Big\|_H^2
       =\int\|(1-\Pi_N)I_\mu(z)\|_H^2\mu(dz),
\]

uniformly in \(m\), and this tends to zero as \(N\to\infty\). Comparing bounded Lipschitz tests with their finite-dimensional projections proves the Hilbert CLT. Equation (1.5) then transfers it to the endpoint. The same \(L^2\) remainder also yields

\[
 m\mathbb E\|\widetilde F(\mu_m)-F(\mu)\|_H^2
       \longrightarrow\operatorname{tr}C_\mu,
\]

and to the actual endpoint whenever the \(L^2\) transfer above holds.

If initialization survives as an external random environment, the theorem is conditional on that environment. The unconditional limit is generally a Gaussian mixture unless its covariance is deterministic. Independence of sampling from initialization is enough for conditional iid arguments, not for eliminating that distinction.

## 5. What this route does and does not require for the neural problem

This mechanism needs actual first mixture responses and a **uniform second finite-difference bound on a positive \(W_1\)-neighborhood**. Uniformly bounded actual second responses are one sufficient source of that bound; Section 6 does not require a limiting second derivative to exist. A derivative merely at the target law does not suffice: both the replacement rectangles and the mixed-law telescoping pass through many nearby empirical laws. The atom first response must be weakly continuous at the target law in the explicit sense (1.4).

In exchange, the proof uses none of the following as separate assumptions: a raw-state empirical \(m^{-1/2}\) estimate, an operator-norm empirical derivative law, a Taylor remainder controlled by a power of \(W_1(\mu_m,\mu)\), a uniform Fréchet derivative over weak signed-measure balls, or a Donsker theorem for a large function class. The second replacement bound controls higher Hoeffding orders, and qualitative continuity identifies the surviving first order.

The needed derivative kernel representation should come from the actual dynamic response equations, retaining the changing features and actual initialized action and adjoint. A second formal derivative or bounds only on the unperturbed path do not verify L1--L2. Uniformity over the support of the cutoff, including atomic laws and diagonal atom pairs, must be proved. This is the remaining model-specific obligation assigned to the supervisor's dynamic route.

Sanity checks: if \(\mu\) is a point mass then \(\mu_m=\mu\) almost surely and the centered influence vanishes on its support; all conclusions reduce correctly to zero. The bias was estimated rather than silently removed. Every probability segment and rectangle stays in the simplex, so no inadmissible negative law is used. The cutoff preserves the actual influence at \(\mu\), and its rare mismatch was treated separately from defining the actual endpoint. The continuity requirement uses \(L^2(\mu)\), precisely the measure required by the limiting first projection.

**Route decision:** this gives a complete conditional bridge from uniformly controlled second law differences and weakly continuous actual atom first response to the desired expansion and Hilbert CLT, with the stronger \(L^2\) remainder. The actual neural theorem remains open until those dynamic hypotheses and the necessary identification/existence scope are verified.

## 6. The weaker formulation: first derivatives and second finite differences

The supervisor's subsequent continuum-passage proposal allows a weaker analytic interface than Section 1. No convergence, or even existence, of limiting second derivatives is needed. This section is the most economical hypothesis package for the probabilistic proof.

Retain boundedness and measurability of \(F\), the actual centered first mixture derivative and its integral representation,

\[
 \frac d{dt}F(Q+t\eta)=\int I_{Q+t\eta}(z)\,\eta(dz),
\tag{6.1}
\]

and qualitative continuity (1.4). It suffices that the derivative exists and the fundamental theorem of calculus holds on admissible mixture segments; continuity on finite-dimensional mixture families is a convenient sufficient condition. Replace all second-derivative assumptions by the following rectangular finite-difference estimate: whenever

\[
 Q+a\eta+b\xi,\qquad 0\le a\le s,\quad0\le b\le t,
\]

are probability laws in \(U\),

\[
 \|F(Q+s\eta+t\xi)-F(Q+s\eta)-F(Q+t\xi)+F(Q)\|_H
       \le Mst\|\eta\|_{\rm TV}\|\xi\|_{\rm TV}.
\tag{6.2}
\]

This is an estimate on actual values. It survives uniform convergence of functions on the rectangle. Thus finite-program second derivative bounds can be passed to the limit without proving convergence of those derivatives.

### 6.1 The line Taylor estimate follows from (6.2)

For a probability segment \(Q_t=Q+t\eta\), \(0\le t\le1\), let \(f(t)=F(Q_t)\). For \(0\le s<t<1\) and a sufficiently small \(h>0\), apply (6.2) to the rectangle with base \(Q_s\) and both direction measures equal to \(\eta\), with side lengths \(t-s\) and \(h\). Divide by \(h\) and let \(h\downarrow0\). The existence of the first derivatives gives

\[
 \|f'(t)-f'(s)\|_H\le M(t-s)\|\eta\|_{\rm TV}^2.
\]

One-sided limits give the same endpoint estimate. Integrating from zero to one yields

\[
 \Big\|F(Q+\eta)-F(Q)-\int I_Q\,d\eta\Big\|_H
       \le\frac M2\|\eta\|_{\rm TV}^2.
\tag{6.3}
\]

Equation (6.3) is exactly the estimate used for bias and first-projection identification. Equation (6.2) is exactly the estimate used for double replacements. All of Section 2 therefore applies under (6.1)--(6.2), provided first responses are uniformly bounded where needed.

### 6.2 The cutoff preserves the weaker calculus

The first-response bound (3.3) used only the line Taylor estimate and therefore follows from (6.3). If desired, take a slightly larger open ball around the cutoff support, for instance \(W_1(Q,\mu)<3\rho/4\), and use a smaller fixed contamination length. This gives the same kind of uniform first-response bound throughout that open ball.

The product \(\chi F\) has the first derivative from Section 3 by the ordinary product rule. To bound its second finite differences without a second derivative of \(F\), denote values at the corners of a rectangle by subscripts \(00,10,01,11\), and write \(\Delta_{12}\) for the mixed corner difference. The exact identity is

\[
\begin{aligned}
 \Delta_{12}(\chi F)
  ={}&\chi_{11}\Delta_{12}F
    +(\chi_{11}-\chi_{10})(F_{10}-F_{00})\\
   &+(\chi_{11}-\chi_{01})(F_{01}-F_{00})
    +(\Delta_{12}\chi)F_{00}.
\end{aligned}
\tag{6.4}
\]

On a rectangle in that larger open ball, (6.2) bounds the first term. The first derivative bounds for \(F\) and \(\chi\) bound each product of edge differences by a constant times \(st\|\eta\|_{\rm TV}\|\xi\|_{\rm TV}\). The cutoff's bounded second derivative and bounded \(F\) bound the last term the same way. Thus \(\chi F\) has a uniform mixed difference bound on such rectangles.

For an arbitrary probability rectangle, the inverse image of the cutoff support is a compact subset of the inverse image of that larger open ball. Its complement is open where the extended product is zero. These two open sets cover the compact parameter rectangle. A sufficiently fine rectangular grid has every small cell contained in one of the two sets: this follows by taking, from the finite subcover by parameter balls, a positive minimum radius for a refinement. Cells in the first set satisfy the bound just proved, and cells in the second have zero difference. Summing mixed differences over the grid telescopes to the mixed difference of the full rectangle; the products of side lengths sum to \(st\). This proves a global bound of the form (6.2) for the bounded zero extension.

The first derivative also extends across the support boundary: both \(\chi\) and its first derivatives vanish there, and \(F\) and its first response are uniformly bounded on an open neighborhood. The global first-derivative kernel is obtained by the product rule and centering. Consequently the complete localization proof and the \(L^2\) expansion remain valid under first mixture differentiability and (6.2).

### 6.3 Uniform value approximation supplies an actual first response

Here is the forward-quotient bridge relevant to finite neural programs. Suppose maps \(F_n\) converge uniformly to \(F\) on a law region \(\mathcal R\), with

\[
 a_n=\sup_{Q\in\mathcal R}\|F_n(Q)-F(Q)\|_H\longrightarrow0.
\]

Take base laws \(Q\) in a closed smaller region whose sufficiently small contaminations, uniformly in the atom, stay in \(\mathcal R\). All response suprema below concern those base laws. Suppose the finite maps have first contamination responses \(I_{n,Q}(z)\) and a common quadratic remainder

\[
 \left\|F_n((1-\epsilon)Q+\epsilon\delta_z)-F_n(Q)
                  -\epsilon I_{n,Q}(z)\right\|_H\le C\epsilon^2
\tag{6.5}
\]

uniformly in \(n,Q,z\) and sufficiently small positive \(\epsilon\). A uniform second TV derivative bound gives (6.5), with a common \(C\). Comparing two finite maps through their forward quotients shows

\[
 \sup_{Q,z}\|I_{n,Q}(z)-I_{k,Q}(z)\|_H
       \le2C\epsilon+2(a_n+a_k)/\epsilon.
\]

First fix a small \(\epsilon\), then let \(n,k\to\infty\), and finally let \(\epsilon\downarrow0\). The responses are uniformly Cauchy, so have a uniform limit \(I_Q(z)\). Passing \(n\to\infty\) in (6.5) gives

\[
 \left\|F((1-\epsilon)Q+\epsilon\delta_z)-F(Q)
                    -\epsilon I_Q(z)\right\|_H\le C\epsilon^2.
\tag{6.6}
\]

Thus the limit is an actual first contamination derivative; its finite-approximation error satisfies

\[
 \sup_{Q,z}\|I_{n,Q}(z)-I_Q(z)\|_H
       \le2C\epsilon+2a_n/\epsilon.
\tag{6.7}
\]

If \(F\) is \(W_1\)-continuous, then for every fixed positive \(\epsilon\) the quotient in (6.6) is jointly continuous in \((Q,z)\). The reason is that \((Q,z)\mapsto(1-\epsilon)Q+\epsilon\delta_z\) is continuous in \(W_1\): a coupling gives distance at most \((1-\epsilon)W_1(Q,Q')+\epsilon d(z,z')\). Equation (6.6) makes \(I\) a uniform limit of these continuous quotients as \(\epsilon\downarrow0\). Hence \(I\) is jointly continuous in law and atom on the smaller region. Compactness of the atom space then gives (1.4). Uniform convergence of continuous finite values is one way to prove the required continuity of \(F\).

Finite-dimensional mixture second-difference bounds pass to the limit directly by applying uniform value convergence to their four corners. This supplies (6.2), without differentiating a limiting second derivative.

### 6.4 Centering and the integral representation must also pass to the limit

The finite programs have exact finite-sum centering and first-direction formulas. Passing these identities to arbitrary laws is valid when their atom kernels converge uniformly and are jointly weak-law/atom continuous, as in the preceding paragraph, and the value approximations hold on the same neighborhood.

To see the essential point, approximate a law \(Q\) by finitely supported \(Q_k\) in \(W_1\). Joint continuity on a compact local set implies uniform convergence \(I_{Q_k}(z)\to I_Q(z)\) in \(z\). For a continuous \(H\)-valued function on the compact atom space, integrals converge in \(H\) under weak convergence of probability laws: a finite continuous partition of unity uniformly approximates the function by finite linear combinations of fixed vectors, reducing this assertion to finitely many scalar continuous tests. Therefore

\[
 0=\int I_{Q_k}(z)\,Q_k(dz)
        \longrightarrow\int I_Q(z)\,Q(dz).
\]

For the direction representation, approximate both \(Q\) and a second law \(\nu\) by finite laws in the same region. The finite first-order Taylor formula has leading term \(\epsilon\int I_Q\,d\nu\) and a uniform \(O(\epsilon^2)\) remainder, since the centered kernel integrates to zero under the base law. Passing to the weak-law limit at fixed \(\epsilon\) uses value continuity and the just-described integral convergence; then dividing by \(\epsilon\) and letting it decrease to zero proves

\[
 \left.\frac d{d\epsilon}F((1-\epsilon)Q+\epsilon\nu)\right|_{0+}
        =\int I_Q(z)\,\nu(dz)
        =\int I_Q(z)(\nu-Q)(dz).
\tag{6.8}
\]

The same argument applies at any interior point of an admissible mixture segment and along finite mixtures, provided the uniform approximation region contains them. It supplies the first calculus actually used above. All assertions in this passage are conditional on the specified uniform finite-program value and remainder bounds; pointwise convergence of values alone would not suffice.

**Final analytic interface:** bounded weakly continuous actual values on a positive law neighborhood; uniformly controlled second mixed finite differences there; actual first mixture response kernels with integral representation, obtained for example by the uniform-quotient passage; and qualitative \(L^2(\mu)\) continuity of the atom response. These conditions close the entire probabilistic step, including the stronger \(L^2\) remainder, while leaving the finite-program-to-actual-flow approximation and its uniform analytic bounds to the dynamic proof.
