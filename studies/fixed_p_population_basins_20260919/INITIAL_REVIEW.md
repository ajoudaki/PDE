# Independent isolated review of the initial-descent exclusion

Verdict: **PASS for the stated exact order-two population closure and the stated finite-data scope.** No blocking error was found. The proof establishes strict initial descent for every compatible finite probability law on the circle, global continuation at fixed order, and a permanent loss gap excluding every loss-one prediction limit. It does not establish convergence, exclusion of stationary limits with loss below one, a basin-measure result, or an approximation result at arbitrarily long times.

Reviewed frozen input: `INITIAL_EXCLUSION.md`, SHA256
`34b3f702d2876fb5c445f35ee45850af65d9978b1421f4a2238c73b787995a3c`.
The hash was checked before and after the scientific audit. The only established scientific inputs read were `docs/global_nonlinear.md`, complete assigned ranges 13161–13786 and 15146–15528, containing C.4.7.10.B, C.4.7.10.C.1, and C.4.7.10.D.3. The review used the required `solve-math-rigorously` skill. No study README, study history, other study, or other review was consulted. The author file was not edited.

## 1. Initialization, response correlations, and normalization

At order two the supplied dictionary has no additional bounded-code features beyond the polynomial core. Its only odd lower coordinates are
\((h_1,h_2,t_1,t_2)\), and its only odd upper coordinates are \((Z_1,Z_2)\). The simultaneous sign reversals preserve the separate Gaussian laws. Opposite-parity Gram entries vanish; the Cholesky recurrence in the supplied C.1 also verifies that normalization preserves the parity of each coordinate. Formula (H3.1) makes every initialized contraction entry involving an even feature vanish.

The lower pairs \((h_j,t_j)\) are independent across \(j\), centered, and identically distributed, because \((g_j,\zeta_j)\) have those properties across coordinates. Within each pair, the correlation \(\kappa\) must be retained. The raw odd Gram blocks are exactly
\[
 G_{1,\mathrm{odd}}=\operatorname{diag}
 \left(\begin{pmatrix}v&\kappa\\\kappa&\nu\end{pmatrix},
       \begin{pmatrix}v&\kappa\\\kappa&\nu\end{pmatrix}\right),
 \qquad G_{2,\mathrm{odd}}=\tau I_2.
\]
For upper row \(Z_j\), (H3.1) gives the matching lower-pair contraction
\[
 E[Z_j A_0h_j]=\alpha v,\qquad
 E[Z_j A_0t_j]=\alpha\kappa+\tau\beta.
\]
The second summand follows from
\(E[\partial_{\zeta_j}t_j]=\beta\) and \(E[Z_j^2]=\tau\). Cross-coordinate entries vanish. Thus the reverse-source response and the dependence of \(t_j\) on \(h_j\) are both included.

The inverse-Cholesky factors yield full ridged inverses on both sides of the raw contraction, not inverse square roots. Explicitly, with
\(m(u)=E_1[\psi_1\tanh(g\cdot u)]\),
\[
 b_2^TD a_0(u)
 =\psi_2^T(G_2+\eta I)^{-1}C(G_1+\eta I)^{-1}m(u).
\]
This follows by substituting all three definitions and using
\(L^{-T}L^{-1}=(G+\eta I)^{-1}\). Restricting this expression to the odd blocks gives exactly the author's factor \((\tau+\eta)^{-1}\), row \(qR^{-1}\), and formula (7). Conditioning the lower \(t_j\) correlation on \(g_j\) gives \(k(\tanh g_j)\); the other component of \(g\cdot u\) has independent Gaussian variance \(1-u_j^2\). This includes the endpoints \(u_j=\pm1\). The value \(\eta=1/9216\) agrees with the prescribed order-two schedule.

## 2. Strict positivity of the effective lower response

The coefficient \(\ell\) is not assumed to have a favorable sign. The bound on \(\ell+\alpha r b(h)\) is valid as written.

For completeness, the Cauchy–Schwarz step in (8) gives
\[
 (EW)^2\le E\frac{W}{1+W}\ E[W(1+W)],
 \qquad W=aG^2,
\]
so the claimed lower bound is \(a/(1+3a)\). Together with
\(\sinh^2x\ge x^2\), this proves \(v\ge1/4\),
\(\tau\ge1/7\), and \(0<\alpha\le6/7\).

The layer-cake identity and the derivative of the mass of a shifted symmetric Gaussian interval prove \(b(h)\le b(0)\). The displayed tanh addition identity is algebraically correct; symmetry of \(\zeta\) therefore gives
\(b(h)\ge b(0)\operatorname{sech}^2(\alpha h)\). The ratio of consecutive nonconstant terms in the cosh series is at most \((6/7)^2/12\), giving
\[
 \cosh(6/7)\le32/23,
 \qquad 2b_*-b^*\ge\frac{17}{512}b^*>0.
\]
There is a strict quantitative margin in the step needed later.

Since \(k'(h)=\alpha b(h)>0\) and \(k(0)=0\), the bounds
\(0<\kappa\le\alpha vb^*\) follow by integrating this derivative and multiplying by \(h\), with the sign handled equally for positive and negative \(h\). Conditional Gaussian integration by parts and centered Cauchy–Schwarz give
\[
 \operatorname{Var}_{\zeta}\tanh(\zeta+\alpha h)
 \ge\frac{(E[\zeta\tanh(\zeta+\alpha h)])^2}{\tau}
 =\tau b(h)^2.
\]
The conditional second-moment decomposition, followed by
\(\kappa^2\le vE[k(h_1)^2]\), proves (12) with all signs preserved.

Direct multiplication of \(qR^{-1}\) gives the two numerators in (13). In particular \(r>0\), and
\[
\begin{aligned}
 \Delta(\ell+\alpha r b(h))
 ={}&\alpha(v\nu-\kappa^2)-\tau\beta\kappa
       +\alpha\tau\beta v b(h)\\
 &+\alpha v\eta+\alpha^2\kappa\eta b(h)
       +\alpha\tau\beta\eta b(h).
\end{aligned}
\]
Every term on the second line is nonnegative. Applying the preceding bounds to the first line yields
\[
 \Delta(\ell+\alpha r b(h))
 \ge\alpha v\tau\beta(2b_*-b^*)>0.
\]
Thus the claimed \(\psi'(g)>0\) holds for every finite real \(g\), with the actual positive ridge still present in both coefficients. No unproved sign condition on \(\ell\) enters.

## 3. Correlation monotonicity, endpoints, and independence

The Gaussian integration-by-parts calculation for \(F'(s)\) is correct: the differentiated gate terms from \(G\) and \(V\) cancel, leaving
\[
 F'(s)=\frac{E[\psi'(G)\operatorname{sech}^2
       (sG+\sqrt{1-s^2}V)]}{\tau+\eta}>0
 \quad (-1<s<1).
\]
The bounds specified in the author file justify differentiation on every compact interior interval and both integrations by parts. Boundedness of \(\psi\) justifies continuity at \(s=\pm1\) by dominated convergence. Reflection gives oddness and \(F(0)=0\). Strict interior monotonicity plus an intermediate interior point proves strict monotonicity when either comparison endpoint is \(-1\) or \(1\). Consequently the coordinate map \(A(u)\) is injective, nonzero on the unit circle, and identifies antipodes exactly.

The ridge-function independence argument does not require the vectors \(a_j\) to be pairwise nonparallel. The finitely many forbidden lines leave a vector \(e\) for which the absolute projections are positive and distinct whenever \(a_i\ne\pm a_j\). The restricted functions are real analytic on all of \(\mathbb R\), so their local identity extends globally as claimed. For ordered positive slopes, subtracting the limiting constant and multiplying by the slowest exponential isolates its coefficient. Removing this term and iterating proves independence, including when slopes are rationally related. No assumption about disjoint higher exponential frequencies is needed.

The coordinatewise tanh transform of a nondegenerate independent Gaussian pair has positive density throughout \((-1,1)^2\). Continuity therefore upgrades an almost-sure zero relation to a pointwise relation on this square. The preceding ridge-function result applies there and proves (18). This establishes exactly the required finite-set nondegeneracy modulo antipodes.

## 4. Data aggregation, energy, and continuation

The signed class sums in (19) account for both identical and antipodal observations. Independence shows that their feature combination vanishes exactly when every class sum vanishes. Compatibility makes each sum a common nonzero sign times a strictly positive class mass; hence it cannot vanish. This verifies the universal quantifier over the stated compatible finite laws, including repeated directions and repeated antipodal pairs.

At \(c=0\), both backward quantities vanish, so the only initial velocity is
\(c'(0)=2\sum_i\omega_i y_iH_0(u_i)\). The unhalved loss and the actual population/Frobenius metric give
\(\mathcal L'(0)=-4\|\sum_i\omega_i y_iH_0(u_i)\|_2^2\).
Thus the factor four and the time convention are correct.

The extension of the fixed-order continuation argument beyond the small-arc data family is justified directly, rather than obtained by extending the order-to-infinity theorem. At fixed order, the right side is locally Lipschitz on
\(L^\infty(w-g)\times L^\infty(c)\times\mathbb R^{d_2\times d_1}\): fixed features are bounded, the frozen unbounded \(g\) appears only inside tanh gates, the input norm is one, and the data sum is finite. Local solutions satisfy the gradient identity. From \(\mathcal L\le1\), Cauchy–Schwarz gives \(\int|r|d\mu\le1\). The contraction bounds then give, successively,
\[
 \|c'\|_\infty\le2,\qquad
 \|M'\|_F\le2\|c\|_2\le4t,
\]
\[
 \|w'\|_\infty
 \le2\|b_1\|_{L^\infty(\ell^2)}\|M\|_{\rm op}\|c\|_2
 \le4t\|b_1\|_{L^\infty(\ell^2)}
       (\|D\|_{\rm op}+2t^2).
\]
Their integrals bound the state and their values bound the speed in the local existence norm on every finite interval. A finite maximal endpoint is therefore a Cauchy endpoint in that Banach space; local existence there contradicts maximality. This proves unique global continuation at fixed order for the stated data. No data support cap, Gaussian tail comparison, neural-width limit, or closure-order limit is required.

Strict initial descent and the energy identity give \(\mathcal L(t)<1\) for every \(t>0\). Fixing one such time gives the permanent strict gap in (23). The displayed lower bound on prediction norm is the reverse triangle inequality with \(\|y\|_2=1\). It excludes zero training predictions even as a subsequential limit. Continuity of finite-data loss also excludes every training-prediction limit having loss one, whether stationary or otherwise.

The stated strong-state topology indeed implies prediction continuity. If \(w_n\to w\) and \(c_n\to c\) in their population \(L^2\) spaces and \(M_n\to M\), the Lipschitz gates and contraction maps imply \(a_n(u)\to a(u)\) and \(H_n(u)\to H(u)\) in their stated norms. Then
\[
 |E[c_nH_n]-E[cH]|
 \le\|c_n-c\|_2+\|c\|_2\|H_n-H\|_2\longrightarrow0.
\]
There are finitely many training inputs, so this suffices for the loss-limit assertion.

## 5. Parity and scope of the verdict

The parity subsystem is closed, contains the initial state, and is preserved by the vector field exactly as described in the supplied C.1. The established characteristic uniqueness and continuation keep the trajectory in it at every finite time. This does not require the training law itself to be symmetric. The proof uses the actual order-two ridge throughout and makes no equality claim with the differently ridged order-one closure.

All substantive steps in the reviewed argument are justified by explicit estimates or by the supplied established initialization and closure equations. The final exclusion is an energy statement for this particular canonical trajectory. Stationary states with loss strictly below one and convergence of the trajectory remain unresolved, as the author explicitly states. The PASS does not apply to finite asymmetric particle approximations or to an exchange of long-time, width, precision, or closure-order limits.

## 6. Separately checked order-one extension

The supervisor additionally requested a check of whether the same argument applies at order one. It does. The supplied B/C.1 state that orders one and two have the same active odd lists and Gaussian initialization, with no extra active word features. At order one only the constant even feature remains; its contraction vanishes by the same parity argument. Hence the entire raw-block derivation above is unchanged except for the chosen ridge.

The positivity calculation is valid for every positive \(\eta\): the raw Gaussian quantities \(v,\tau,\alpha,\kappa,\nu,\beta\) do not depend on \(\eta\), \(\Delta>0\), and all terms discarded in the displayed expansion of \(\Delta(\ell+\alpha r b(h))\) are nonnegative for \(\eta>0\). The injectivity, feature-independence, signed-class, and fixed-order energy/continuation arguments therefore also hold with \(\eta_1=1/4096\). This verifies strict initial descent and exclusion of loss-one prediction limits for the canonical exact order-one population closure under the same compatible finite-data assumptions. It does not identify its predictions or trajectory with those at order two, whose prescribed ridge is different. This extension is separate from the frozen author's order-two claim and does not modify that file.
