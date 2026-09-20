# Independent review: initialized positivity and terminal geometry

Date: 2026-09-18. Verdict: **PASS for the three stated mathematical results**, within their stated scope. No mathematical blocker was found. Two nonblocking scope clarifications appear at the end.

This review was conducted from the neutral assignment, the complete frozen `initialization_positivity.md` and `terminal_geometry.md`, all of `docs/observable_p1.md`, and the assigned model/state/existence portions of `docs/global_nonlinear.md` (C.4.7.9.3–4 and C.4.7.10.D.3). The required rigorous-mathematics and conjecture-audit instructions were applied. No other study, author history, diagnostic output, other review, or other agent's scientific finding was consulted. No experiment or numerical integration was run.

Reviewed source hashes (SHA-256):

```text
initialization_positivity.md
a785048dfbf22f3940941dbb92f985729cc393977b882eb5153ddf54dc39367b
terminal_geometry.md
60c6c5a5878735efbba9996efff8cf734c4aef899c676120a1c75161829742bc
docs/observable_p1.md
0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba
docs/global_nonlinear.md
81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c
```

## 1. Canonical object, correlation and metric checks

The object checked is the exact order-one, dimension-three population system, with exact Gaussian expectations, ridge \(\eta=1/4096\), and initialization \((w,c,M)=(g,0,D)\). The lower marks retain the full joint law

\[
h_j=\tanh G_j,\qquad
k_j=\tanh(\sqrt\tau Z_j+\alpha h_j),
\]

with independent coordinate pairs \((G_j,Z_j)\). In particular, \(G_j\) and \(k_j\) are not independent. The upper coordinates are independent copies of \(H=\tanh(\sqrt\nu\widetilde Z)\), on their own population. Both frozen candidates preserve these facts.

The bands

\[
d_h=\frac{\alpha\nu}{ac_*},\qquad
d_k=\frac{\alpha\beta\eta/(\nu+\eta)+\tau\gamma}{bc_*}
\]

agree exactly with the established contraction \(D=L_2^{-1}CL_1^{-T}\). In particular, the reversed-action response \(\tau\gamma\), the Cholesky subtraction \(\beta h/(\nu+\eta)\), and the right transpose all remain present. Neither candidate replaces the reverse operation by an independent Gaussian source.

Direct variation of a prediction yields

\[
\delta f_i=
E_1[\operatorname{sech}^2(w\cdot u_i)q_i u_i\cdot\delta w]
+E_2[h_i\delta c]+d_i^T\delta M a_i,
\quad q_i=b_1^TM^Td_i.
\]

Thus the displayed three-block gradient is the gradient in the population \(L^2\), population \(L^2\), and matrix Frobenius metric. The physical velocity is exactly \(-2\sum_i\mu_i(f_i-y_i)\nabla f_i\). All factors in the later clock and terminal exponents follow this unhalved loss convention.

Removal of the constant features is legitimate in the initialized odd sector. The lower activation and upper readout are odd in their respective simultaneous mark negations; gates are even. Hence the constant entries of \(a_i\) and \(d_i\) vanish. The omitted matrix-gradient row and column are zero, while the remaining gradients themselves have the proper parity. Consequently this reduction does not discard an additional first-order prediction direction available in the original full state.

## 2. Positivity of the full conditional initialized coefficient

The result in `initialization_positivity.md`, equations (2)–(7), is correct. The following verifies every inequality on which the positive margin depends.

Since all relevant Gaussian and conditional Gaussian variables are nondegenerate, \(0<\nu,\tau,s<1\), so \(\alpha,\gamma\in(0,1)\). Differentiation under the expectation defining \(K\) is allowed by the bounded derivative of tanh and gives

\[
K'(h)=\alpha E_Z\operatorname{sech}^2(\sqrt\tau Z+\alpha h)
\in(0,\alpha].
\]

Symmetry gives \(K(0)=0\) and oddness. Consequently \(hK(h)>0\) off zero and \(|K(h)|\le\alpha|h|\). Taking expectation at \(h=\tanh G\) proves \(0<\beta\le\alpha\nu\).

Set \(R=k-(\beta/\nu)h\). Then

\[
E R^2=s-\beta^2/\nu,\qquad
E[ZR]=\sqrt\tau\gamma.
\]

The second identity uses integration by parts in the independent Gaussian \(Z\); the integrand and derivative are bounded, so the Gaussian boundary term vanishes and all integrals exist. Cauchy–Schwarz, with \(EZ^2=1\), gives

\[
s-\beta^2/\nu\ge\tau\gamma^2.
\]

The exact ridge denominator therefore obeys

\[
b^2=(s-\beta^2/\nu)+\eta+
\frac{\beta^2\eta}{\nu(\nu+\eta)}
\ge\tau\gamma^2+\eta.
\]

For \(B_*=c_*d_k/b\), positivity is strict and

\[
\alpha\beta/(\nu+\eta)\le\alpha^2\le1/\gamma,
\quad
0<B_*\le
\frac{\eta/\gamma+\tau\gamma}{\eta+\tau\gamma^2}
=1/\gamma.
\]

The inequality \(\tanh^2 z\le z^2\) implies

\[
K'(h)\ge\alpha(1-\tau-\alpha^2h^2).
\]

Integrating from zero to \(h\in(0,1]\) gives

\[
K(h)/h\ge\alpha(1-\tau-\alpha^2h^2/3)
\ge m:=\alpha^2(1-\alpha/3).
\]

Here \(m<\alpha\). This sign is essential: it is why an upper bound for \(B_*\) produces the required lower bound. Substitution yields exactly

\[
\frac{c_*\Psi(h)}h\ge
\frac{\alpha\nu}{\nu+\eta}+B_*(m-\alpha)
\ge\frac\alpha\gamma
\left[\frac{\gamma\nu}{\nu+\eta}-1+\alpha-\frac{\alpha^2}{3}\right].
\]

The elementary numerical constants also check without quadrature:

- Integrating \(\tanh z\le z\) gives \(\log\cosh z\le z^2/2\), hence \(\operatorname{sech}^2 z\ge e^{-z^2}\). The exact Gaussian integral gives \(\nu\le1-1/\sqrt3<3/7\) and \(\alpha\ge1/\sqrt{1+2\nu}\ge\sqrt{7/13}>11/15\). The last strict comparison is \(1575>1573\) after squaring and clearing denominators.
- The set \(\{1/2\le|G|\le1\}\) has total interval length one and Gaussian density at least its value at one. That value exceeds \(1/5\), since \(2\pi e<24<25\) (the elementary \(\pi<4\), \(e<3\) suffice). For \(z\ge0\), the derivative of \(\tanh z-z+z^3/3\) is \(z^2-\tanh^2z\ge0\). Thus \(\tanh(1/2)\ge11/24\), whose square exceeds \(1/5\). Therefore \(\nu>1/25>1/64\), and the actual ridge gives \(\eta/(\nu+\eta)<1/65\).
- Independence and centering eliminate the cross term in \(E(\sqrt\tau Z+\alpha h)^2\). Hence \(\gamma\ge1-\tau-\alpha^2\nu=\alpha-\alpha^2\nu\).

Writing \(\gamma\nu/(\nu+\eta)=\gamma-\gamma\eta/(\nu+\eta)\), the bracket is bounded below by

\[
2\alpha-1-\alpha^2(\nu+1/3)-1/65.
\]

Its derivative in \(\alpha\) is at least \(2-2(3/7+1/3)=10/21>0\); its derivative in \(\nu\) is negative. The stated corner value is indeed

\[
\frac7{15}-\frac{1936}{4725}-\frac1{65}
=\frac{2552}{61425}>0.
\]

This proves the claimed pointwise lower bound for \(\Psi(h)/h\) with the actual positive ridge, including \(h=1\). Oddness then handles negative \(h\).

For a unit direction \(v\in S^2\), conditioning on \(G_j\) writes \(g\cdot v=v_jG_j+\sqrt{1-v_j^2}V\), with the second Gaussian independent of \(G_j\) and the reverse noise \(Z_j\). Therefore the conditional coefficient really is \(\Psi(\tanh G_j)\), and equation (6), \((Da_0(v))_j=T(v_j)\), follows from the full joint law. For \(0<r<1\), the conditional expectation of the second tanh factor is odd and has strictly positive derivative in \(G\), so it has the sign of \(G\). Its product with \(\Psi(\tanh G)\) is strictly positive almost surely off the null event \(G=0\). Thus \(T(r)>0\). The endpoints follow directly (or by dominated convergence), and symmetry gives \(T(-r)=-T(r)\). In particular \(\rho_0=\sqrt3T(1/\sqrt3)>0\).

## 3. Complete full-kernel classification at finite fitting states

The classification in `terminal_geometry.md`, equations (2)–(4), is correct for positive sample weights, three independent inputs, labels in \(\{\pm1\}\), and finite states in the initialized odd sector.

For each coordinate, a relation \(Ah+Bk=0\) almost surely forces \(B=0\) because the conditional law of \(k\) given \(G\) is nondegenerate; then \(A=0\) because \(Eh^2>0\). Thus the raw two-coordinate Gram is positive definite. Independence and zero means make the full lower Gram a direct sum of these blocks. The invertible normalization preserves positive definiteness. This proves \(b_1^TM^Td_i=0\) almost surely if and only if \(M^Td_i=0\), without relying on ridge regularization to manufacture independence.

If \(\sum_i\lambda_i\nabla f_i=0\), linear independence of the three deterministic \(u_i\) forces each scalar lower coefficient \(\lambda_i\operatorname{sech}^2(w\cdot u_i)q_i\) to vanish almost surely. The lower gates are strictly positive at every finite argument, even though no uniform lower bound is available. Thus \(\lambda_iM^Td_i=0\). The readout and matrix components give the other two lines of (3). Conversely those three conditions annihilate every gradient component. Multiplication by positive sample-weight factors is invertible, so it does not change whether the full weighted kernel is singular.

The readout dependence argument is also complete. The upper mark distribution has a positive density on its open cube. A continuous function that is zero almost surely under that distribution is zero throughout the cube. Distinct nonzero vectors modulo sign permit a direction \(e\) avoiding finitely many proper hyperplanes, so their scalar projections are nonzero and have distinct squares. Restricting the identity to a short line through zero and using the first \(k\le3\) nonzero odd Taylor coefficients of tanh gives a matrix with determinant

\[
\left(\prod_j t_j\right)\prod_{j<\ell}(t_\ell^2-t_j^2)\ne0.
\]

There are consequently no missing dependencies from unequal collinear vectors or from a generic linear relation among the \(v_i\).

At fitting, \(v_i=0\) is impossible because it would give \(f_i=0\ne y_i\). A signed duplicate \(v_i=\varepsilon v_j\) forces \(y_i=\varepsilon y_j\). This justifies grouping exactly by equality of \(t_i=y_iv_i\), using \(\xi_i=y_i\lambda_i\), and taking a common \(d\) within a group because the upper gate is even. Checking the three partitions then gives:

- Three singleton groups force all \(\xi_i=0\), so the full kernel is positive definite.
- One pair and one singleton permit only a pair contrast. Its lower condition is \(M^Td=0\), and its matrix condition is \(d(A_1-A_2)^T=0\). A nonzero outer product vanishes only when one factor vanishes, giving the stated alternatives.
- One triple group permits zero-sum contrasts. Any nonzero contrast forces \(M^Td=0\). If \(d=0\), all two contrast directions remain. If \(d\ne0\), the remaining condition is \(\sum_i\xi_iA_i=0\), exactly affine dependence of the three \(A_i\). This last case is understood together with the required \(M^Td=0\).

Full row rank of \(M\) makes \(M^T\) injective, so the stated simplification to \(d=0\) is valid. These are differential criteria at fitting states, not proofs of their reachability from initialization.

## 4. Signed-axis fitting and terminal exponential rate

The result in `terminal_geometry.md`, equations (5)–(16), is correct for the prescribed equally weighted signed coordinate axes.

The architecture is odd in its input at every state. Thus the example \((y_ie_i,y_i)\) contributes exactly the same square loss as \((e_i,1)\), as an identity of functions on the full state space; differentiating preserves equality of their full gradients. Coordinate permutations preserve the canonical joint marks and \(D=[d_hI,d_kI]\), and the positive-axis law is permutation invariant. Uniqueness therefore gives equal predictions along both the physical and auxiliary gradient-ascent trajectories. The residual reduction and \(\theta_t=2(1-F)\nabla F\) follow, with \(\nabla F\) still the full three-block gradient.

For continuation, the normalized feature Gram is

\[
L^{-1}GL^{-T}=I-\eta L^{-1}L^{-T}\preceq I.
\]

Its synthesis and analysis maps are contractions. Hence \(|a_i|\le1\) and \(|d_i|\le\|c\|_2\). In the clock \(\theta_s=\nabla F\), \(\|c_s\|_\infty\le1\), \(\|M_s\|_F\le s\), and \(\|w_s\|_\infty\le B_1(\|D\|+s^2/2)s\). Integrating proves (10), taking matrix norms consistently as Frobenius norms (which also control operator norm).

The state space for the existence argument is the Banach space of bounded increments \(w-g\), bounded \(c\), and finite matrices. Although \(g\) is unbounded, it occurs only inside tanh and its bounded derivatives. Finite products, bounded feature multipliers, and probability integrals give a locally Lipschitz vector field in this space. On every bounded interval the displayed bounds bound both state and speed. A finite endpoint is therefore Cauchy in this complete space, and the local contraction construction restarts it. This proves existence at every finite auxiliary clock, independently of any loss descent or compactness assumption.

At initialization the two active lower coefficients are precisely \(\nu/a\) and \(\beta\eta/((\nu+\eta)b)\); all other coordinates vanish by independence and centering. Positivity of \(\beta,d_h,d_k\) makes \(\ell>0\). The initialized upper activations are independent centered nonzero variables, whence

\[
\kappa(0)=\left\|\frac13\sum_i h_i(0)\right\|_2^2
=\frac13E\tanh^2(\ell b_{21})>0.
\]

The other two gradient blocks vanish because \(c=0\). Thus \(F(0)=0\) and \(F(s)>0\) for small positive \(s\), after which \(F_s=\kappa\ge0\) keeps it positive.

The identity \(d\|c\|_2^2/ds=2\langle c,m\rangle=2F\) is exact. If \(F<1\) forever, it gives \(\|c\|_2^2\le2s\). Once \(F\ge F_0>0\), Cauchy–Schwarz gives

\[
F_s\ge\|m\|_2^2\ge F^2/\|c\|_2^2\ge F_0^2/(2s).
\]

The logarithmically divergent integral contradicts \(F<1\). The global auxiliary continuation already proved rules out escape before this contradiction. Continuity therefore gives a finite first fitting clock \(s_*\); at it \(\|c(s_*)\|_2\) is finite and nonzero, and

\[
\kappa_*\ge\|m(s_*)\|_2^2\ge1/\|c(s_*)\|_2^2>0.
\]

This is a lower bound on the visited scalar direction only; no full-kernel coercivity assumption is hidden in the argument.

Bounded derivatives of tanh give locally continuous derivatives of the auxiliary vector field and \(F\) in the Banach norms above. In particular \(\kappa(s)\) is locally Lipschitz near the finite endpoint. Integrating \(F_s=\kappa\) gives

\[
q(s):=1-F(s)=\kappa_*(s_*-s)+O((s_*-s)^2).
\]

Thus \(t(s)=\int_0^s[2q(\sigma)]^{-1}d\sigma\) diverges at \(s_*\), is strictly increasing before it, and its inverse exists for all physical \(t\ge0\). The chain rule and physical uniqueness identify this reparameterized trajectory with the canonical flow. There is no illicit division by zero at fitting or assumption that fitting occurs at finite physical time.

For that flow, \(q_t=-2\kappa(s(t))q\) and \(q(0)=1\). Near the endpoint,

\[
\int|\kappa(s(t))-\kappa_*|\,dt
=\int\frac{|\kappa(s)-\kappa_*|}{2q(s)}\,ds<\infty,
\]

because numerator and denominator are respectively bounded above and below by positive constants times \(s_*-s\). The integral on the remaining compact interval is finite as well. Therefore

\[
C:=\exp\left(-2\int_0^\infty[\kappa(s(t))-\kappa_*]dt\right)
\in(0,\infty),
\]

and exactly

\[
1-F(t)=Ce^{-2\kappa_*t}(1+o(1)),\qquad
\mathcal L(t)=C^2e^{-4\kappa_*t}(1+o(1)).
\]

Bounded auxiliary speed and \(s_*-s(t)\asymp q(t)\) give the asserted state convergence in the bounded-increment/readout/Frobenius norms. The six-atom balanced extension is valid because each antipodal pair contributes an identical loss and gradient; it remains a six-atom statement.

## 5. Scope and nonblocking clarifications

The formal conclusions do not prove initialized sign preservation at positive time, reachability of any singular fitting state, convergence for arbitrary three-atom geometry or weights, a uniformly positive rate over other geometries, a result for rotated axes, or any neural-width/higher-order limit. The candidates already distinguish these limitations. Positive initial movement is not used as a substitute for endpoint regularity: the latter has its own proof above.

Two wording improvements would make the scope explicit without changing any proof:

1. Immediately before `initialization_positivity.md` equation (6), write \(v\in S^2\). The displayed formula with \(\sqrt{1-v_j^2}\) is the unit-direction formula, as intended by the study's sphere contract.
2. The final paragraph of `terminal_geometry.md` should be read as suggesting two unresolved routes, not as an exhaustive classification of all ways an initialized negative example could arise. A bounded trajectory approaching a nonfitting critical state is another logically unresolved possibility outside the protected family. The fitting-state classification does not address that case. No such reachable example is established or asserted by this review.

Neither point invalidates the positivity theorem, the stated fitting-state classification, or the prescribed signed-axis terminal theorem. Those three results pass independent mathematical review in their stated exact-population scope.
