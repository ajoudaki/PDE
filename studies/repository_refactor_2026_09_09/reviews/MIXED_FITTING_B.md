# Isolated complete-proof audit: Sections 10–11

Verdict: CLEAN.

No required mathematical correction was found. With the explicitly stated restriction \(n\ge n_*\), Section 10 proves fitting by the actual finite-width gradient flow on \(E\), with convergence to finite parameter endpoints as \(t\to\infty\). Section 11 proves permanent first-gate mass for each sample on \(E\cap E_S\). The stated probability bounds and limitations are justified. “Finite” here refers to network width and finite-valued parameter limits; this is not a claim of exact interpolation at finite training time.

## 1. Isolation, hashes, and complete read coverage

The only input files read were:

| Input | Complete coverage | Lines | Bytes | SHA-256 |
| --- | --- | ---: | ---: | --- |
| [PROOF.md](/tmp/pde-mixed-fitting-audit.GVYPqDG0/PROOF.md:1) | Lines 1–496, including the final line and EOF | 496 | 19,240 | 36a50c2aa599302db2b2942d0ddb21d5561488ac0eff5e4b34dd7e43e3717a78 |
| [NOTATION.md](/tmp/pde-mixed-fitting-audit.GVYPqDG0/NOTATION.md:1) | Lines 1–98, including the final line and EOF | 98 | 5,110 | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |

Total input coverage: 594 lines and 24,350 bytes. Both numbered reads were returned in full without truncation. SHA-256 values were obtained before the full reads and checked again after the mathematical audit; both checks agreed exactly.

No source repository, studies, previous reviews, history, internet, skill documents, other agents, or subagents were accessed. No input edits, experiments, generators, builds, installations, or Git operations were performed. The output directory was newly created by mktemp at /tmp/pde-mixed-fitting-complete-proof-report.aiupkC7Y. This REPORT.md is the sole output file and was created using apply_patch.

In the discussion below, P refers to PROOF.md and N to NOTATION.md. Line intervals refer to the exact hashed inputs above. References to an “established library” in N supply no additional premises: only the conventions actually written in N were used.

## 2. Premises, conventions, and scope

Locations: P 1–51, 229–241, 354–387, 389–424, 476–496; N 1–98.

The premises are sufficient and mutually consistent:

- There are exactly two deterministic inputs of squared norm \(d\), with Gram matrix \(G=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\), \(|\rho|<1\), and labels \(y=(1,-1)\). Hence \(G\) is positive definite and the two inputs are linearly independent; \(d\ge2\) follows.
- The smooth first activation is odd, has a nonnegative derivative supported on \([-R,R]\), and has strictly positive derivative in the interior. Smoothness forces its derivative to vanish at both endpoints. It equals \(A\) on \([R,\infty)\) and \(-A\) on \((-\infty,-R]\). Its derivative and second derivative have finite suprema.
- In particular, the later constant \(\lambda_1=\|(\phi^{(1)})''\|_\infty\) is finite and strictly positive. If it were zero, \((\phi^{(1)})'\) would be constant, contradicting both its support and its strict interior positivity.
- The second activation satisfies the stated global derivative and growth bounds. Its use is layer-specific, consistently with N.
- The raw stored weights, residual convention, Gaussian readout variance \(n^{-2}\), ordinary norms, and explicit factors of \(n\) and \(d\) agree with N.

Equation (10.2) specifies the optimizer completely. Under N's mobility convention it is sum-loss GF with unit multipliers, hence block mobilities \(n,1,n\). The passage to the mean loss divides every velocity by two and doubles the traversal time, as stated.

The deterministic fitting argument in Section 10.2 assumes a finite time with strict loss below 2. Section 10.3 proves that assumption on its event for \(n\ge n_*\). Section 11 uses those same width-qualified bounds; its final probability statement explicitly retains \(n\ge n_*\). No population or discrete-time premise is needed.

## 3. Raw gradients, kernel, energy, and global finite existence

Locations: P 28–90; N 16–42, 59–63, 70–82.

Direct differentiation of the normalized predictor gives

\[
\nabla_{W^{(1)}}f_a=\frac{\delta_a^{(1)}x_a^T}{n\sqrt d},
\qquad
\nabla_{W^{(2)}}f_a=\frac{\delta_a^{(2)}(h_a^{(1)})^T}{n},
\qquad
\nabla_{W^{(3)}}f_a=\frac{h_a^{(2)}}n.
\]

Multiplication of the sum-loss gradients by mobilities \(n,1,n\) gives exactly (10.2). Consequently the kernel is the sum of these Jacobian Gram matrices weighted by the respective mobilities:

\[
K^{(1)}_{ab}=\frac{G_{ab}}n(\delta_a^{(1)})^T\delta_b^{(1)},\quad
K^{(2)}_{ab}=\frac{((h_a^{(1)})^Th_b^{(1)})
((\delta_a^{(2)})^T\delta_b^{(2)})}{n^2},\quad
K^{(3)}_{ab}=\frac{(h_a^{(2)})^Th_b^{(2)}}n.
\]

Thus (10.3), its explicit Gram representatives, and \(\dot r=-2Kr\) all have the correct normalization. In particular, negative \(\rho\) does not spoil positivity of \(K^{(1)}\): its displayed matrix-valued feature representation proves positive semidefiniteness.

The inverse mobility metric is

\[
\|(V_1,V_2,V_3)\|_{\mathrm{metric}}^2
=\|V_1\|_F^2/n+\|V_2\|_F^2+\|V_3\|^2/n.
\]

The identity \(-\mathcal L_\Sigma'=4r^TKr=\|\dot W\|_{\mathrm{metric}}^2\) therefore gives precisely (10.4), with no extra factor of two or width.

On any interval of local existence, its integrated energy bounds each block's squared speed integral by \(\mathcal L_\Sigma(0)\). Cauchy–Schwarz gives (10.5) for arbitrary \(s<t\) in that interval. If a maximal endpoint were finite, these estimates would make every parameter block Cauchy at that endpoint. At fixed \(n,d\), each limiting block is a finite vector or matrix. The vector field is smooth on the entire finite-dimensional parameter space, so local existence and uniqueness apply at that limit and extend the solution. This proves global existence without assuming bounded weights in advance and without using \(E\).

## 4. Frozen rows and the permanent first-feature Gram bound

Locations: P 92–106.

A row whose two initial preactivations are outside \((-R,R)\), including its boundary, has both gates zero. Holding that row fixed while solving the remaining equations is a solution of the full local system, because the row's right-hand side remains zero. Uniqueness identifies it with the actual flow. The argument can be continued throughout the global solution.

Each equal-sign saturated row contributes
\(A^2(1,1)^T(1,1)/n\) to the sample Gram, and each opposite-sign row contributes
\(A^2(1,-1)^T(1,-1)/n\). Their total has eigenvalues \(2A^2N_s/n\) and \(2A^2N_o/n\). All remaining rows contribute positive semidefinite outer products. This proves (10.6) for all time.

This is a statement about rows with both gates zero. It does not assert that an arbitrary single saturated coordinate remains fixed when the other sample's gate is active. That distinction is essential for correlated inputs and is respected later.

## 5. Kernel coercivity, centered balance, and predictor bound

Locations: P 108–174.

Writing \(Q(t)=(\mathbf h^{(1)})^T\mathbf h^{(1)}/n\), the exact decomposition is

\[
K^{(2)}=\frac1n\sum_i(W_i^{(3)})^2D_iQ(t)D_i.
\]

Since \(Q(t)\succeq\gamma I_2\) and every diagonal entry of \(D_i\) is at least one,
\(D_iQ(t)D_i\succeq\gamma D_i^2\succeq\gamma I_2\).
Summation gives \(K^{(2)}\succeq\gamma M_3^2I_2\), hence both inequalities in (10.8). At zero residual every velocity is zero; constant continuation is valid by uniqueness.

For the homogeneity defect,

\[
D'(z)=-\frac{2\varepsilon z^2}{(1+z^2)^2},
\qquad
D(+\infty)=-\varepsilon\pi/2,\quad
D(-\infty)=\varepsilon\pi/2.
\]

Thus the claimed supremum \(\|D\|_\infty=\varepsilon\pi/2\) is exact.

The second-weight speed satisfies

\[
\|\dot W^{(2)}\|_F
\le\frac2n\sum_a|r_a|(M\sqrt nM_3)(A\sqrt n)
=2MA M_3\sum_a|r_a|
\le CeM_3,
\]

so \(M_2\le CS_w\).

Put \(\Delta W^{(2)}=W^{(2)}-W^{(2)}(0)\). Differentiating its squared norm and the normalized readout squared norm gives

\[
\frac{d}{dt}\|\Delta W^{(2)}\|_F^2
=-\frac4n\sum_a r_a(W^{(3)})^T
\bigl[(\phi^{(2)})'(z_a^{(2)})\odot
\Delta W^{(2)}h_a^{(1)}\bigr],
\]

\[
\frac{d}{dt}M_3^2
=-\frac4n\sum_a r_a(W^{(3)})^Th_a^{(2)}.
\]

Subtracting produces exactly (10.9), with the stated sign of the initial-matrix term. No derivative of a hidden feature should occur: these are parameter norm derivatives, with the current features substituted into the velocities.

The bracket in (10.9) has Euclidean norm at most
\(\sqrt n(\varepsilon\pi/2+MB_0A)\).
Its normalized pairing with \(W^{(3)}\), followed by
\(\sum_a|r_a|\le\sqrt2e\), bounds the absolute balance derivative by \(D_0eM_3\). Its initial value is \(-b_0^2\). This proves the first inequality in (10.10). The remaining two follow from

\[
M_2^2\le M_3^2+D_0S_w,\qquad
M_3^2\le M_2^2+b_0^2+D_0S_w,\qquad M_2\le CS_w.
\]

Finally,

\[
\|f\|\le\frac{\|W^{(3)}\|}{n}\|\mathbf h^{(2)}\|_F
\le\sqrt2MA M_3(B_0+M_2).
\]

Replacing \(\sqrt2MA\) by the larger \(C\) and using the centered estimate gives (10.11). All initial-matrix dependence here is through \(B_0\); no initial Frobenius norm of order \(\sqrt n\) has been inserted.

## 6. Closing the global bounds after the actual margin

Locations: P 177–227.

For \(t\ge t_0\), loss monotonicity and \(\|y\|=\sqrt2\) yield
\(\|f(t)\|\ge\nu=\sqrt2-e_0>0\).
When \(M_3\le1\), (10.11) and

\[
B_0+1+\sqrt{D_0S_w}
\le(B_0+1+\sqrt{D_0})(1+\sqrt{S_w})
\]

give \(M_3\ge c/(1+\sqrt{S_w})\). When \(M_3\ge1\), the same lower bound follows from \(c\le1\).

Because \(S_w'=eM_3\ge0\),

\[
e'\le-2\gamma M_3S_w'
\le-\frac{2\gamma cS_w'}{1+\sqrt{S_w}}.
\]

The primitive \(F(x)=2[\sqrt x-\log(1+\sqrt x)]\) has derivative \(1/(1+\sqrt x)\), including the right derivative at zero. Integration proves (10.12) directly in physical time. It neither divides by \(e\) at a zero nor requires an invertible feature clock.

For \(u\ge0\), the maximum of \(\log(1+u)-u/2\) occurs at \(u=1\) and is \(\log2-1/2\). The proof's weaker bound by \(\log2\) is therefore valid. It yields \(F(x)\ge\sqrt x-2\log2\) and the stated \(S_b\).

This bounds \(S_w\) after \(t_0\); monotonicity bounds it before \(t_0\) as well. The corresponding operator and readout upper bounds, and the positive post-margin lower bound \(\beta\), now follow. Substitution into (10.8) proves the loss exponent \(4\gamma\beta^2\) and the residual integral denominator \(2\gamma\beta^2\) in (10.13).

There is no circular use of a long-time weight bound. Before the margin, (10.5) already gives

\[
M_3(t)\le b_0+\sqrt{t\mathcal L_\Sigma(0)},\qquad
e(t)\le\sqrt{\mathcal L_\Sigma(0)},
\]

which integrate to the displayed bound for \(S_w(t_0)\).

The three speed bounds in (10.14) have the correct factors. For the first block, for example,
\(\|\delta_a^{(1)}\|/\sqrt n\le PMUM_3\) and \(\|x_a\|/\sqrt d=1\), giving \(2\sqrt2PMUeM_3\).
The second- and first-block speed integrals are controlled by \(S_w(\infty)\); the readout speed integral is controlled by \(\int_0^\infty e\). Thus every parameter block has finite total variation in its stated norm. At each fixed width this gives a finite parameter limit. Predictor continuity and loss decay prove that the limiting predictions equal both labels.

## 7. Gaussian events and conditioning

Locations: P 231–311.

### First-layer counts

Independent first-weight rows give independent preactivation pairs with law \(N(0,G)\). Nondegeneracy implies positive probabilities for both equal-sign and opposite-sign open saturated corners, so \(p_s,p_o,\gamma,\kappa\) are strictly positive. On \(E_F\), (10.6) gives precisely \(\gamma_n\ge A^2\min(p_s,p_o)=\gamma\).

For either count, variance \(np(1-p)\) and deviation threshold \(np/2\) give failure at most \(4(1-p)/(np)\). Summing these two bounds proves (10.16). No independence between the two counts is used.

### Second-feature moment and empirical kernel

Conditional only on the first weights, the second-preactivation rows are independent \(N(0,Q)\) pairs with \(Q=(\mathbf h^{(1)}(0))^T\mathbf h^{(1)}(0)/n\). On \(E_F\), \(Q-\gamma I_2\) is positive semidefinite and \(Q_{aa}\le A^2\).

The decomposition \(Z=U+\sqrt\gamma\,\xi\) is valid even if \(Q-\gamma I_2\) is singular. Conditional on \(U\), the transformed coordinates are independent. Since \((\phi^{(2)})'\ge1\), the independent-copy variance identity gives
\(\operatorname{Var}(\phi^{(2)}(U_a+\sqrt\gamma\,\xi_a)\mid U)\ge\gamma\).
More explicitly, for any deterministic \(v\in\mathbb R^2\),

\[
\mathbb E[(v^T\phi^{(2)}(Z))^2\mid U]
=\sum_a v_a^2\operatorname{Var}(\phi^{(2)}(Z_a)\mid U)
+\left(\sum_a v_a\mathbb E[\phi^{(2)}(Z_a)\mid U]\right)^2
\ge\gamma\|v\|^2.
\]

Thus the uncentered second-moment matrix is at least \(\gamma I_2\). The argument does not incorrectly discard conditional means or assume the transformed coordinates are unconditionally independent.

The growth bound and Cauchy–Schwarz give

\[
\mathbb E[\phi^{(2)}(Z_a)^2\phi^{(2)}(Z_b)^2\mid W^{(1)}_0]
\le3M^4Q_{aa}Q_{bb}\le3M^4A^4.
\]

There are four entries in the \(2\times2\) empirical matrix. Conditional row independence bounds its expected squared Frobenius deviation from its conditional mean by \(12M^4A^4/n\). Operator norm is at most Frobenius norm; Markov's inequality at \(\gamma/2\) therefore gives \(48M^4A^4/(n\gamma^2)\), as in (10.17). Independence between the four matrix entries is unnecessary.

### Norm events and their intersection

A maximal \(1/4\)-separated sphere set is a \(1/4\)-net, and the radius-\(1/8\) ball packing argument bounds its size by \(9^n\). Approximating each of two unit test vectors incurs at most \(\|W^{(2)}_0\|_{\rm op}/2\) total error. Thus operator norm greater than 8 forces some net bilinear form to have magnitude greater than 4. Each fixed bilinear form has variance \(1/n\), and its tail is at most \(2e^{-8n}\). A union bound over at most \(9^{2n}\) pairs gives the first bound in (10.18).

The stored readout normalization gives
\(b_0^2=n^{-3}\sum_i\xi_i^2\). The event \(b_0>2/n\) is therefore \(\sum_i\xi_i^2>4n\). Applying exponential Markov with parameter \(1/4\) and moment \(\sqrt2\) gives exactly \(e^{-(1-(\log2)/2)n}\).

For the intersection \(E\), the relevant bound is

\[
\mathbb P(E^c)\le
\mathbb P(E_F^c)
+\mathbb P(E_F\cap\{K^{(3)}(0)\not\succeq\kappa I_2\})
+\mathbb P(\|W^{(2)}_0\|_{\rm op}>8)
+\mathbb P(b_0>2/n).
\]

Integrating (10.17) over \(E_F\) bounds the second term. This is the valid conditioning order. The Gaussian row calculation is never reused after conditioning on the overlapping second-layer norm or kernel events. Equation (10.19), including the clipping at zero and \(p_n\to0\) for fixed input configuration, follows.

## 8. Actual loss margin and width-uniform constants

Locations: P 313–387.

The first-feature difference satisfies
\(\|\Delta\mathbf h^{(1)}\|_F\le P\sqrt2\|\Delta W^{(1)}\|_F\); only the two input norms are needed, so correlation causes no missing factor. Expanding the second preactivation difference exactly as in P 326–328 and using (10.5) gives (10.20).

If \(\mathcal L_\Sigma(0)\le4\) and \(t\le\tau\le1/4\), then \(\sqrt{t\mathcal L_\Sigma(0)}\le1\). The second-feature difference is bounded by

\[
M\sqrt{8\tau}\,[A+P(B_0+1)]\le\sqrt\kappa/2
\]

under the stated choice of \(\tau\). On \(E\), the initial feature map has smallest singular value at least \(\sqrt\kappa\). Applying the triangle inequality to every unit vector in the two-dimensional sample space proves that its value at time \(t\) is at least \(\sqrt\kappa/2\). Consequently \(K^{(3)}(t)\succeq\kappa I_2/4\), and loss contracts by \(e^{-\kappa t}\) throughout this interval.

At initialization the norm events actually give the sharper bound
\(\|f(0)\|\le CB_0/n\) from the first inequality of (10.11). The proof uses the valid looser bound \(2CB_0/n\).
The explicit \(n_*\) then ensures both

\[
\sqrt{\mathcal L_\Sigma(0)}
\le\sqrt2+\|f(0)\|\le2,\qquad
\sqrt{\mathcal L_\Sigma(0)}
\le\sqrt2\,e^{\kappa\tau/4}.
\]

These inequalities independently supply the prerequisite loss bound of 4 and the sharper bound \(2e^{\kappa\tau/2}\). Short-time contraction therefore gives the strict actual margin
\(\mathcal L_\Sigma(\tau)\le2e^{-\kappa\tau/2}<2\).
This is stronger than a negative initial derivative and does not replace the nonzero Gaussian readout by zero or assume favorable initial label alignment.

For \(n\ge n_*\ge2\), \(b_0\le1\), so the pre-margin integral is at most
\(2\tau+(8/3)\tau^{3/2}=S_{\rm pre}\).
Also \(e(\tau)\le e_*\) and the post-margin readout lower-bound coefficient can be replaced by the fixed \(c_*>0\). Repeating the already justified time-domain inequality with these bounds gives \(\overline S,\overline U,\beta_*\) and every estimate in (10.23). No width-dependent unknown is hidden in these constants.

These are normalized and aggregate bounds. They do not establish a width-uniform bound on each individual readout coordinate or on its product with second-activation curvature, consistent with P 384–387.

## 9. Reverse-query integral and strip geometry

Locations: P 391–465.

Multiplying the actual first-weight equation by \(x_a/\sqrt d\) gives

\[
\dot z^{(1)}_{a,i}
=\sum_bG_{ab}(\phi^{(1)})'(z^{(1)}_{b,i})c_bq^{(1)}_{b,i}.
\]

Thus (11.1) has no omitted width or input factor, and \(q_a^{(1)}\) contains no residual. Its norm satisfies
\(\|q_a^{(1)}\|/\sqrt n\le M\overline U M_3\).

For \(v_i(t)=\sum_a|c_aq^{(1)}_{a,i}|\), the ordinary Euclidean triangle inequality gives

\[
\frac{\|v(t)\|}{\sqrt n}
\le\sum_a|c_a|\frac{\|q_a^{(1)}\|}{\sqrt n}
\le2\sqrt2M\overline U\,eM_3.
\]

Integrating on a finite interval bounds
\(\|\int v\|/\sqrt n\) by \(V_*\). Each component integral is nonnegative and increases with the interval, so the limit gives (11.2). Since \(n\) is fixed, the bound also makes every \(V_i\) finite. This argument uses Section 10's bounds for the full actual trajectory and requires neither row independence nor a strip nonexit assumption.

The constants in (11.3) are well-defined: \(p_{\rm strip}>0\), \(V_*>0\), \(0<\delta_*\le R/2\), and the compact interval \([-R+\delta_*,R-\delta_*]\) lies strictly inside the region of positive first derivative. Its minimum \(p_*\) is therefore strictly positive.

Consider any row in \(I_a^0\), with \(b\ne a\). Initially \(|z_a(0)|\le R/2<R\), and
\[
|z_b(0)|\ge3R-|\rho|R/2>R.
\]
Before a first exit from \(|z_a|<R,\ |z_b|>R\), the \(b\)-gate is zero. Equation (11.1) then gives exactly

\[
\dot z_a=(\phi^{(1)})'(z_a)c_aq_a,\qquad
\dot z_b=\rho\dot z_a,\qquad
z_b-\rho z_a=z_b(0)-\rho z_a(0).
\]

The Lipschitz bound on the first derivative and its two zero endpoint values imply
\(0\le(\phi^{(1)})'(z)\le\lambda_1(R-|z|)\) inside the strip. The absolutely continuous function \(d_a(t)=R-|z_a(t)|\) consequently satisfies

\[
d_a'(t)\ge-\lambda_1|c_aq_a|d_a(t)
\]

almost everywhere, including the legitimate absolute-value treatment at crossings of zero. Its integrating factor yields

\[
d_a(t)\ge(R/2)\exp\!\left(-\lambda_1\int_0^t|c_aq_a|\,du\right)
\ge(R/2)e^{-\lambda_1V_i}>0.
\]

Meanwhile the conserved difference gives
\[
|z_b(t)|\ge3R-|\rho|R>2R.
\]
Both estimates hold up to any hypothetical first exit. Continuity contradicts that finite exit, so they hold for all finite time. The total integral \(V_i\), rather than merely local smoothness, supplies the uniform-in-time interior margin.

This addresses reachable saturation correctly. For a general row with the other sample's gate active, the correlation term can move a coordinate even when its own gate is zero; there is no universal coordinatewise barrier. The proof instead establishes a separated exterior coordinate for these specific strips, and only then uses the scalar barrier. It makes no assertion that every initially unsaturated row obeys this argument.

## 10. Strip selection, simultaneous mass, and probability

Locations: P 426–479.

By (11.2), the global bad set \(J=\{i:V_i>B_*\}\) satisfies

\[
\frac{|J|}{n}\le\frac{V_*^2}{B_*^2}=\frac{p_{\rm strip}}4.
\]

On \(E_S\), each initial strip has at least \(np_{\rm strip}/2\) rows. Removing \(J\) from each one separately leaves
\(|I_a|\ge np_{\rm strip}/4\).
For each remaining row, \(V_i\le B_*\), so the preceding distance estimate gives \(|z_{a,i}(t)|\le R-\delta_*\) for all time. Every one of those derivatives is at least \(p_*\). Squaring and summing gives the exact normalized lower bound in (11.4).

This is a deterministic worst-case count argument. The bad set may depend on the entire trajectory and may be correlated with both initial strips. No concentration for trajectory-selected rows is invoked. The sets are fixed in time once the trajectory is specified; they play no role in defining or modifying its dynamics. The same global bad-set bound suffices simultaneously for both samples.

For a Gaussian first row, \(z_a(0)\) and \(z_b(0)-\rho z_a(0)\) are jointly Gaussian with covariance zero and variances \(1\) and \(1-\rho^2\). They are therefore independent, and the strip probability is exactly

\[
[2\Phi(R/2)-1]\;2[1-\Phi(3R/\sqrt{1-\rho^2})].
\]

These indicators are independent across first-weight rows before any event conditioning. The two sample strip counts may depend on one another. Applying the same variance bound separately to each count and summing proves
\(\mathbb P(E_S^c)\le8(1-p_{\rm strip})/(np_{\rm strip})\).

The proof then uses the unconditional union bound
\(\mathbb P(E\cap E_S)\ge1-\mathbb P(E^c)-\mathbb P(E_S^c)\), with clipping at zero. It does not assume that row indicators remain independent conditional on \(E\), or that \(E\) and \(E_S\) are independent. The simultaneous all-time probability statement is valid as written for \(n\ge n_*\).

## 11. Necessity of augmentation and claimed limitations

Locations: P 481–496, also P 1–7 and 384–387.

The saturation example genuinely lies in the allowed finite parameter space. To check realizability under the raw normalization, write \(X=[x_1,x_2]\), so \(X^TX=dG\). For a prescribed pair \(s\in\mathbb R^2\), the row vector with transpose
\(w=XG^{-1}s/\sqrt d\) satisfies \(X^Tw/\sqrt d=s\). Hence both specified pairs \((2R,2R)\) and \((2R,-2R)\) are attainable.

With half the rows of each type, the first feature columns consist of all \(A\)'s and a balanced collection of \(A\)'s and \(-A\)'s. Taking \(W^{(2)}_0=I_n\), oddness of \(\phi^{(2)}\) gives exactly
\(K^{(3)}(0)=\phi^{(2)}(A)^2I_2\).
Also \(N_s=N_o=n/2\), \(\|W^{(2)}_0\|_{\rm op}=1\), and the readout choice gives \(b_0=1/n\).

All event inequalities are strict. In particular, \(p_s,p_o<1\), and
\(\kappa=A^2\min(p_s,p_o)/2<A^2<\phi^{(2)}(A)^2\).
The preactivations have strict saturation margins, so nearby first weights retain the same row types. Continuity preserves the norm and kernel inequalities in a sufficiently small full-dimensional neighborhood. At every fixed width the stated independent Gaussian law has strictly positive density throughout the finite parameter space, so this neighborhood has positive probability.

Every first row in that neighborhood stays saturated forever by the already proved invariant-row argument. Thus there is positive probability of \(E\) with zero first-gate mass for both samples. This verifies the claimed failure of an almost-sure gate-mass conclusion on \(E\) alone at those even widths. It does not claim a width-uniform lower bound on the probability of this obstruction, and none is needed.

The final limitations are accurate. The permanent lower bound concerns unweighted squared gates. It does not lower-bound \(c_a\), \(q_a^{(1)}\), their products, hidden velocities, or kernels weighted by reverse quantities. Residuals tend to zero in the fitting result, and all velocities vanish at an interpolating endpoint. Positive gates are entirely compatible with those facts. Nonaffinity of the activation formula alone does not supply a distributional nonaffinity theorem.

The proof neither passes to a population limit nor discretizes the raw optimizer, and it does not establish nonlazy feature motion. Its constants may depend on the fixed correlation and can deteriorate near either singular endpoint. The assumptions exclude both \(\rho=-1\) and \(\rho=1\); no endpoint case is silently included.

## 12. Coverage ledger and final disposition

| Source interval | Content checked | Disposition |
| --- | --- | --- |
| P 1–27 | Scope, input and activation premises | Valid |
| P 28–90 | Raw scaling, metric, kernel, energy, global finite existence | Valid |
| P 92–106 | Actual invariant rows and permanent Gram contribution | Valid |
| P 108–174 | Kernel coercivity, defect, centered balance, predictor bound | Valid |
| P 177–227 | Noncircular integral closure, decay, finite parameter endpoints | Valid |
| P 229–311 | Initialization, Gaussian moments, counts, norm tails, event intersection | Valid |
| P 313–357 | Actual short-time loss margin and width threshold | Valid |
| P 359–387 | Width-uniform estimates and their limitations | Valid |
| P 389–424 | First-coordinate equation, reverse-query integral, positive constants | Valid |
| P 426–465 | Strip nonexit, fixed subsets, deterministic all-time mass bound | Valid |
| P 467–479 | Strip probabilities and simultaneous event bound | Valid |
| P 481–496 | Positive-probability saturation obstruction and final scope | Valid |
| N 1–42 | Model, shapes, layer notation, residuals and loss conventions | Consistent |
| N 44–68 | Norm and finite/population type conventions | Consistent; no population premise imported |
| N 70–88 | Initialization, mobilities and physical clocks | Consistent; unused one-sample changes of variables not imported |
| N 90–98 | Scope and separation of claims | Respected |

All intervening headings and blank lines were included in the complete reads. No missing premise, invalid conditioning step, unreachable-invariant assumption, normalization error, or unjustified strengthening was identified. Required corrections: none.
