# Reconstruction of the dense local test and weak-mode diagnostic

This is an internal collaborative check, not an independent promotion review. After freezing the general first/second matched-loss derivation, the coordinator authorized the complete DENSE_MATCHED_LOSS_LOCAL.md and NEGATIVE_RATE_ASSESSMENT.md as additional same-study inputs. Both were read completely. The calculations below reconstruct their substantive claims from the canonical finite gradient flow and elementary Gaussian identities. No experiments, numerical rate fits, other studies, or linked research artifacts were used.

**Outcome:** the local dense cancellation test, conditional one-sample time transfer, and near-coincident initialization coefficient estimates pass this reconstruction. No material mathematical defect was found. Their conclusions remain local or conditional and do not supply either a positive trained root-width theorem or a slower-width counterexample.

## 1. Actual one-sample dense calculation

Let \(f=f_\theta(x_1)\), \(D\) be the canonical mobility matrix, \(j=\nabla_\theta f\), and \(K=j^\top Dj\). For one sample and label \(y>0\), the unhalved squared loss gives

\[
\dot\theta=2(y-f)Dj,\qquad
\dot f=2(y-f)K.
\]

Dividing on the branch \(f<y\), \(K>0\), gives \(d\theta/df=Dj/K\), with no loss factor remaining. Therefore the cross-kernel ratio in local equations (1)–(2) is exact. Zero initial readout makes the initial query prediction zero too, which justifies the endpoint integral with no additional initial value. The integral still uses the moving dense kernel.

For the two tanh layers, use the local note's initialized \(a,h,s,W,z,g,Q,\psi,T\). At zero readout all hidden derivatives vanish, and the initial training kernel equals \(Q=\|g\|_2^2/n\). The training-prediction derivative of the readout is \(g/Q\). Thus

\[
\partial_u\delta^{(2)}|_0
=\frac{g\odot\operatorname{sech}^2z}{Q}
=\frac{\psi(z)}Q,
\qquad
\partial_u\delta^{(1)}|_0=\frac{s\odot T}{Q}.
\]

The first hidden update per unit \(u\) is \(\delta^{(1)}v^\top/K\), and the second is \(\delta^{(2)}h^\top/(nK)\). Differentiating each at initialization gives exactly

\[
\partial_u^2W^{(1)}|_0=\frac{(s\odot T)v^\top}{Q^2},
\qquad
\partial_u^2W^{(2)}|_0=\frac{\psi(z)h^\top}{nQ^2}.
\]

These are derivatives in training prediction \(u\), as the note explicitly says. The formula for the initialization derivative of \(T=W^\top\psi(W\tanh a)\) follows by differentiating the outer matrix, then the inner argument. It retains both uses of \(W\).

For the explicit width-two example, put \(S(\varepsilon)=g_1^2+g_2(\varepsilon)^2\). At initialization, \(\partial_u w=2g/S\). With \(P=I-g(0)g(0)^\top/S(0)\) held fixed,

\[
P\partial_\varepsilon(2g/S)
=\frac{2g_2'}S Pe_2,
\]
\[
P\partial_\varepsilon^2(2g/S)
=\left(\frac{2g_2''}S-\frac{8g_2(g_2')^2}{S^2}\right)Pe_2.
\]

The terms proportional to the base vector \(g\) vanish under \(P\). Since \(a_2,B>0\), the composition \(g_2(\varepsilon)=\tanh(B\tanh(a_2+\varepsilon))\) has positive first derivative and negative second derivative at zero; both terms in the displayed second coefficient are negative. Also \(Pe_2\ne0\) because \(g_1>0\). The resulting nonzero coefficients of the small-\(u\) first and second initialization variations therefore hold in the actual canonical dense model.

The example disproves an identity asserting cancellation of every transverse initialization response. A single deterministic initialization at width two is not a lower bound on random finite-to-population error; the note preserves that distinction. The projection used here is explicitly the base readout projection, not a silently differentiated moving projector.

## 2. Conditional transfer back to common physical time

With the local assumptions \(0<\lambda\le\gamma_j\le\Lambda\) and \(|\gamma_1-\gamma_2|\le\eta\lambda\), one has \(|\gamma_2/\gamma_1-1|\le\eta\). Hence the ratio of the hitting-time integrands is in \([1-\eta,1+\eta]\), and integration gives

\[
(1-\eta)t_2(u)\le t_1(u)\le(1+\eta)t_2(u).
\]

Inverting yields the interval in the note. The lower speed bound gives \(y-u_2(t)\le ye^{-2\lambda t}\), while the upper bound gives \(u_2'(t)\le2y\Lambda e^{-2\lambda t}\). The enclosing time interval has length \(2\eta t/(1-\eta^2)\). Bounding its speed by the speed bound at its earlier endpoint gives precisely the displayed estimate before local equation (8). Since \(t e^{-ct}\le1/(ce)\), it is uniform in physical time for \(\eta\le1/2\). The final query estimate then follows from the assumed matched-curve error and the Lipschitz constant in \(u\).

This proves the stated conditional transfer. It does not establish either input premise for a finite-to-population comparison.

## 3. Near-coincident initialization coefficient

For the two normalized inputs at angles zero and \(\vartheta\), differentiating the initialized second-layer feature at zero gives \(\operatorname{sech}^2z\odot T\). With the sample factor \(1/m=1/2\), the antisymmetric Rayleigh quotient is

\[
e_-^\top\Gamma_{w,n}e_-=\frac1{4n}\|g(\vartheta)-g(0)\|_2^2.
\]

Thus its quadratic coefficient is the stated
\(C_n=(4n)^{-1}\sum_j\operatorname{sech}^4(z_j)T_j^2\).
At finite width the column norms need not agree, so retaining the phrase “Rayleigh quotient” is necessary and correct.

Conditional on the first-layer vectors, rows of \((z,T)\) are independent centered Gaussian pairs with variances \(q_n,v_n\) and covariance \(c_n\). For \(q_n>0\), write
\(T=(c_n/q_n)Z+\xi\), with \(\xi\) independent of \(Z\) and variance \(v_n-c_n^2/q_n\). Then

\[
\begin{aligned}
\mathbb E[T^2F(Z)]
&=(v_n-c_n^2/q_n)\mathbb EF(Z)
+\frac{c_n^2}{q_n^2}\mathbb E[Z^2F(Z)]\\
&=v_n\mathbb EF(Z)+c_n^2\mathbb EF''(Z),
\end{aligned}
\]

where twice integrating the one-dimensional Gaussian density gives
\(\mathbb E[Z^2F(Z)]=q_n\mathbb EF(Z)+q_n^2\mathbb EF''(Z)\).
The inverse powers cancel, and continuity treats degeneracy. This reconstructs the conditional mean in negative-assessment equation (4).

Because \(0\le F=\operatorname{sech}^4\le1\), the conditional variance of \(C_n\) is at most \(3v_n^2/(16n)\). The underlying empirical triples are independent across neurons and have finite fourth moments. Expanding centered sums yields second moment \(O(n^{-1})\) and fourth moment \(O(n^{-2})\) for their centered averages. In particular,

\[
\mathbb E[v_n(q_n-q_*)]=O(n^{-1}),\qquad
\mathbb E[v_n(q_n-q_*)^2]
\le(\mathbb Ev_n^2)^{1/2}
(\mathbb E(q_n-q_*)^4)^{1/2}=O(n^{-1}).
\]

The function \(\beta(q)=\mathbb EF(\sqrt q\,G)\) has bounded first two derivatives on \([0,1]\), obtained by Gaussian integration by parts, including their one-sided limits at zero. Taylor expansion proves the claimed \(O(n^{-1})\) bias of \(v_n\beta(q_n)\); the additional \(c_n^2\gamma(q_n)\) has expectation \(O(n^{-1})\). The stated product splitting and the conditional variance bound yield mean-square error \(O(n^{-1})\). This is centered at the explicit population coefficient, so it includes the finite-width mean bias.

For the population small-angle coefficient, write \(h=\tanh\). Its first-layer covariance has zero first derivative, and its second derivative at angle zero is

\[
\mathbb E[h(G)h''(G)]-\mathbb E[G h(G)h'(G)]
=-\mathbb E[h'(G)^2]=-v_*.
\]

The equality follows by integrating the second expectation by parts. The second-layer product expectation has derivative \(\mathbb E[h'(Z_1)h'(Z_2)]\) with respect to the off-diagonal covariance; at coincidence this is \(\beta(q_*)\). Therefore its diagonal-minus-off-diagonal entry is \(v_*\beta(q_*)\vartheta^2/2+o(\vartheta^2)\). The remaining sample factor \(1/2\) gives the weak eigenvalue coefficient \(C_*=v_*\beta(q_*)/4\), agreeing with the finite coefficient's limit.

The proof estimates the angle derivative coefficient at each fixed finite width. It does not justify a uniform joint angle/width asymptotic or any trained estimate, and the note does not claim those conclusions.

## 4. Scope and checked versions

The quantifier checks in the negative assessment are appropriate: width-dependent data can shrink the gap and change the problem; a large constant for one fixed nearly singular dataset is not a slower exponent; an exactly singular full Gram fails the specified hypothesis. The general matched-loss note supplies an explicit coordinate singularity example, not a dense rate lower bound. No candidate here identifies a slower-than-root trained correction.

The following complete versions were checked:

- DENSE_MATCHED_LOSS_LOCAL.md: SHA-256 eff8fa6f698071733b1e8db67ecbe16dc76cc8cc0d2ba902d460889695234953.
- NEGATIVE_RATE_ASSESSMENT.md: SHA-256 bc54bf51e048ccd58f2fbb7031d1b08a85f74db547d40a6e50e27eb26c7772e8.

The reconstruction used only the assigned notes, the already-read canonical dense definitions, and mathematical skills. References to other supporting artifacts inside the notes were not followed. The author of this check also authored the general matched-loss derivation; this report is consequently an internal cross-check of the coordinator's separate local notes, not an isolated external review of the complete study.
