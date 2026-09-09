# Isolated audit: bounded quartic actual feedback

Date: 2026-09-05.

Candidate: `/tmp/l3-two-sample-Un7kw9/BOUNDED_QUARTIC_ACTUAL_FEEDBACK_TEST.md`.

Verified candidate SHA256:

```text
3d4a765e7e18b51ef4841256536f5ea2d5a46c5e78f54d1634fa0af00629bf94
```

## Verdict and scope

**PASS as the explicitly limited a priori calculation; no new coercive whole-network response control is established.** I found no incorrect identity or failed estimate among the candidate's claimed results, under its stated branch and response-domain qualifications. The unbounded weight is handled correctly, including its derivative growth and every trained-operator and lower-layer transport contribution. The initialized-return products remain open exactly where the candidate says they remain open.

As a proposed source of new coercive feedback control, this is **identities plus a bounded-primal restatement, rather than new coercive control**. That assessment does not reject the true identities or the valid integrability estimates: bounded activation supplies an actual bounded readout, which makes the complete transported energy identity legitimate without a readout fourth-moment hypothesis. The energy nevertheless controls no additional response norm in this argument. The top gate-response bound is also a valid direct consequence of bounded readout.

This is not a certification of the arbitrary-label contract, global existence, continuation, a population limit, or GF/exact-GD identification. None is asserted by the candidate. Fix a finite horizon contained in the existence interval of the constructed strong symmetric population branch. Initial operators are bounded, trained increments are Hilbert–Schmidt, the specified parameter metric and loss identity hold, and the population readout starts at zero. These are premises, not conclusions of this review.

I read `/etc/codex/skills/solve-math-rigorously/SKILL.md` completely and performed a proof-only audit myself. The mathematical dependencies used were exclusively:

- `CONTRACT.md`, SHA256 `e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd`.
- `COUPLED_EVEN_CHANNEL_ESTIMATE.md`, SHA256 `9fd58fa3256394644f23c6e7d0e66c253beac76f2f43f13ec49477137d413e20`, for the definitions and equations (2)–(9), (19), (23)–(29), (32), (35), and (37)–(40) specified in the audit request. Its activation-specific affine lower-slope and bounded-weight estimates are not imported.

The dependency hashes identify the files; they do not broaden the permitted mathematical scope. I did not follow the candidate's additional listed references or consult other routes, reviews, or history. No agents, experiments, or candidate changes were used. Equation numbers below refer to the candidate unless explicitly identified otherwise.

## 1. Actual activation, two sample forces, and bounded readout

For the single fixed choice

\[
\phi(z)=1+\varepsilon\int_0^z\frac{du}{1+u^4},
\qquad \varepsilon=1/10,
\]

the bound \(|\mathcal A|\le4/3\) gives \(1-m\le\phi\le H\), with \(m=2/15\), \(H=17/15\). Its derivative is strictly positive and bounded by \(\varepsilon\), and its second derivative is the displayed \(-4\varepsilon z^3/(1+z^4)^2\), bounded in absolute value by \(4\varepsilon\). The activation has no added affine term and is nonaffine on every open interval. Its stated expansions at zero are correct. No positive uniform lower slope is used.

Since the activation difference has magnitude at most \(2m\), \(|k|\le m/\delta\). The two endpoint slopes belong to \((0,\varepsilon]\), so \(|b|\le\varepsilon/(2\delta)=\beta\) and \(a+\delta|b|\le\varepsilon\). Thus (1) is valid, including its factor of two in the bound for \(b\).

On the opposite-label symmetric branch, the loss is \((1-g)^2\), \(g=\delta G\), and the specified metric gives

\[
\dot\Theta=2\delta(1-g)\nabla G,
\qquad
(1-g)'=-2\delta^2\|\nabla G\|^2(1-g).
\]

Starting from \(g(0)=0\), this yields \(0\le g\le1\) and \(0\le\lambda\le2\delta\). The loss identity and time Cauchy–Schwarz give (3). Both sample forces are retained: their unreduced readout sum is exactly \(\dot C=\lambda k_3\). Consequently

\[
|\dot C|\le2\delta\frac m\delta=R,
\qquad |C(t)|\le Rt,
\quad R=4/15.
\]

This is a bound on the actual readout in physical time, not a hypothesis on a prescribed driver. For arbitrary labels in \(\{\pm1\}\), a branch with the same zero population readout starts at loss one. Then

\[
|r_1|+|r_2|\le\sqrt{2(r_1^2+r_2^2)}\le2,
\qquad |\dot C|\le2H,
\]

which verifies the separately stated all-label readout bound. It does not extend the subsequent symmetric identities to arbitrary labels.

The Hilbert–Schmidt displacement estimate gives \(\|A\|_{\rm op},\|B\|_{\rm op}\le K_0+\sqrt T=K\), hence \(\|M_3\|_2\le KH\). These arguments use probability-normalized population spaces and require no cross-population neuron identification.

## 2. The weight is unbounded, and its growth estimates are valid

For \(f(z)=(1+z^4)^{-1}\), the integral defining \(s\) is smooth and strictly positive at each finite \((M,D)\), and \(k=sV\). Direct endpoint subtraction gives the candidate's expression for \(b\) and the exact identity \(Mb=-\omega k\). The formula for \(\omega\) has a nonnegative numerator and positive denominator; it involves no division by \(M\) or \(V\).

It would be incorrect to reuse the affine candidate's bounded-weight conclusion. Here

\[
\omega(L,L)=L\frac{f(0)-f(2L)}{\mathcal A(2L)}
\sim\frac{L}{\mathcal A(\infty)}.
\]

The present candidate explicitly recognizes this and supplies a valid replacement. Differentiating the secant gives \(b=Vs_M\). With \(\ell=-f'/f\) and the candidate's probability measure \(\pi\),

\[
s_M/s=-\mathbb E_\pi\ell=-L,
\qquad \omega=ML.
\]

Differentiation of a normalized expectation gives

\[
L_M=\mathbb E_\pi\ell'-\operatorname{Var}_\pi\ell,
\qquad
L_D=\mathbb E_\pi(r\ell')-\operatorname{Cov}_\pi(\ell,r\ell).
\]

Indeed the two logarithmic density derivatives are the centered versions of \(-\ell\) and \(-r\ell\), respectively. Since \(|\ell|\le4\), \(|\ell'|\le6\), and both variances in the covariance bound are at most 16, \(|L_M|,|L_D|\le22\). The product rule now gives exactly

\[
0\le\omega\le4|M|,
\quad |\omega_M|\le4+22|M|,
\quad |\omega_D|\le22|M|.
\]

Thus (7) is a global growth estimate, not an assertion of bounded derivatives. At \(D=0\), the integral definition gives \(\omega=4M^4/(1+M^4)\). All these formulas extend through the axes without a singularity.

## 3. All trained transport is included and integrable

Equation (8) differentiates each actual operator action. For example,

\[
\dot M_3=\dot B_eh_2+B_e\dot h_2
=\lambda\|h_2\|_2^2b_3C+B_e\dot h_2,
\]

and the corresponding contrast formula contains \(\lambda\|k_2\|_2^2a_3C\). The derivatives of \(h_2,k_2\) include the trained \(A\) actions, its full lower-layer transport, and the first-layer updates. None has been frozen or omitted.

The complete variation estimate (9) also checks out. At layer one,

\[
\mu\|\eta_U\|_2+\delta\|\eta_{V_1}\|_2
\le\sqrt{\mu^2+\delta^2}
\sqrt{\|\eta_U\|_2^2+\|\eta_{V_1}\|_2^2}
\le\|\eta\|.
\]

At an activation, the derivative matrix on \((M,D)\) for the pair \((h,\delta k)\) has entries \(a,\delta b\), giving the stated sum-of-norms bound with \(\Gamma=3\varepsilon/2\). A full operator variation contributes at most \((H+m)\|\eta_W\|_{\rm HS}\); the current operator contributes at most \(K\Gamma\) times the previous variation bound. This proves the recursion for \(N_2,N_3\), for symmetry-preserving and symmetry-breaking variations alike. Applying it to \(\eta=\dot\Theta\) proves the full velocity estimate.

The Hilbert–Schmidt energy derivative is

\[
\frac d{dt}\|E_{B,e}\|_{\rm HS}^2
=2\lambda\langle b_3C,M_3-B_{0,e}h_2\rangle
=-2\langle\omega_3C,\dot C\rangle
-2\lambda\langle b_3C,B_{0,e}h_2\rangle.
\]

This cancels exactly the readout derivative in \(\mathbb E[\omega_3C^2]\), giving (10) with its displayed signs. Differentiating the weight includes the trained cubic-in-\(C\) terms displayed after (10), as well as every transported lower-layer term. The proof never assigns them a favorable sign.

The initialized-work bound is

\[
2\lambda\,|\langle b_3C,B_{0,e}h_2\rangle|
\le2\varepsilon RK_0H\,t.
\]

For transport, population Cauchy–Schwarz and the growth bounds give

\[
\left|\mathbb E[C^2\dot\omega_3]\right|
\le R^2t^2(4+22KH)
(\|\dot M_3\|_2+\|\dot D_3\|_2)
\le R^2t^2(4+22KH)N_3\|\dot\Theta\|.
\]

Time Cauchy–Schwarz, \(\int_0^t s^4ds=t^5/5\), and the loss identity prove precisely (11). No fourth moment of the readout, preactivations, or initialized-operator action is hidden in this estimate.

The identity is justified analytically on the stated branch. The forward fields have time derivatives in \(L^2([0,T]\times\Omega_3)\), so their integral representatives are pointwise absolutely continuous for almost every population point. Smooth composition supplies the pointwise weight chain rule. The growth estimate and bounded readout make \(\omega C^2\) integrable, the preceding bound makes \(C^2\dot\omega\) integrable in time and population, and

\[
\mathbb E|\omega C\dot C|\le4R^2t\|M_3\|_1
\]

handles the remaining product. Integration and Fubini therefore justify (10), not merely its formal algebra.

## 4. What the weighted energy does, and does not, add

The finite bound (11) is true. Nevertheless, its energy is already bounded directly by quantities available before the cancellation:

\[
0\le\mathcal E_B(t)
\le t+4KH R^2t^2.
\]

Here the first term is the displacement bound and the second is simply \(\omega\le4|M_3|\), \(\|M_3\|_1\le KH\), and \(\|C\|_\infty\le Rt\). Even the direct trained update yields

\[
\|\dot B_e(t)\|_{\rm HS}
\le\lambda\|b_3C\|_2\|h_2\|_2
\le\varepsilon RHt,
\]

and hence the further direct bound

\[
\mathcal E_B(t)
\le\frac{\varepsilon^2R^2H^2}{4}t^4+4KH R^2t^2.
\]

These observations classify what the proved energy estimate supplies; they are not proposed candidate modifications. The transported identity establishes a legitimate cancellation with finite work and transport, but the boundedness of its energy is a consequence of existing primal estimates.

There is also no pointwise domination of \(|Q_3|^2=|a_3C|^2\) by \(\omega_3C^2\): at \(M_3=0\), \(\omega_3=0\) whereas \(a_3=\varepsilon/(1+D_3^4)>0\). This is an algebraic degeneracy of the weight, not a counterexample along a reachable trajectory. More generally, the argument establishes no connection from this top-population weight to the initialized middle or first-layer return multiplied by a response. It does not rule out a future additional estimate using actual trajectory structure.

## 5. Initialized and trained returns, including the physical derivative

Taking the adjoint of the integrated rank-one updates against the current fields proves (12). The inner products correctly use both the past field at \(s\) and the actual current field at \(t\); no current field is replaced by an independent input. In particular,

\[
\|p_2^{\rm tr}(t)\|_\infty
\le2\delta H\beta^2R^2t\int_0^t s\,ds
=\delta H\beta^2R^2t^3,
\]

\[
\|q_2^{\rm tr}(t)\|_\infty
\le2m\varepsilon^2R^2t\int_0^t s\,ds
=m\varepsilon^2R^2t^3.
\]

The complete return satisfies \(\|q_2\|_2\le K\varepsilon Rt\), using the full current operator. These are the bounds in (13).

Differentiating the actual transpose gives

\[
\dot q_2=\underbrace{\lambda k_2\|Q_3\|_2^2}_{\dot B_o^*Q_3}
+B_o^*(a_3\dot C+C\dot a_3).
\]

The three terms are bounded respectively by

\[
2m\varepsilon^2R^2t^2,
\qquad K\varepsilon R,
\qquad4K\varepsilon RtN_3\|\dot\Theta\|.
\]

Thus (14) is valid and implies \(q_2\in H^1([0,T];L^2)\). Its proof retains the differentiated trained transpose and both transported arguments of the gate.

It is essential that \(p_2^{\rm tr},q_2^{\rm tr}\) are bounded pointwise, while the initialized returns in (12) have only the proved \(L^2\) bounds. A bounded \(L^2\) operator need not send a bounded input into \(L^p\), \(p>2\). Moreover, the actual gated readout depends on that same initialization. Neither an independent-input Gaussian action estimate nor higher population moments can be inferred from the assumptions used here. Time \(H^1\) regularity does not improve the population integrability exponent. The candidate makes these distinctions correctly.

## 6. Whole-gradient response, including nonsymmetric perturbations

The off-branch extension satisfies exactly

\[
f_1=F+\delta G,\quad f_2=F-\delta G,
\qquad\mathcal L=F^2+(\delta G-1)^2.
\]

At a general base state the differentiated negative loss gradient would contain

\[
\lambda D^2G\,\eta-2\delta^2\nabla G\,DG[\eta]
-2\nabla F\,DF[\eta]-2F D^2F\,\eta.
\]

At the actual symmetric base, \(F=0\), so the last term vanishes, while \(-2\nabla F\,DF[\eta]\) remains for a symmetry-breaking perturbation. This gives precisely the candidate's response equation and both nonnegative squares on the left of (17). It does not require the perturbation itself to preserve symmetry. Conversely, this specialization must not be applied unchanged at an arbitrary nonsymmetric base with \(F\ne0\); the candidate's stated scope does not do so.

The use of full \(\eta_A,\eta_B,A,B\) in (15) and the differentiated adjoints retains variations in both operator orientations. The identity

\[
d^2(Wh)=2\eta_Wdh+Wd^2h
\]

accounts for both mixed operator terms at each hidden matrix. Moving \(Wd^2h\) backwards by the current adjoint leaves the local activation curvature. Since

\[
p_\ell h_\ell+q_\ell k_\ell
=\frac12\sum_{\sigma=\pm1}
(p_\ell+\sigma q_\ell/\delta)\phi(z_{\ell,\sigma}),
\]

its local second differential is exactly \(\mathcal S_\ell\) in (17). The readout contributes \(2\langle\eta_C,dk_3\rangle\). Thus the quadratic Hessian identity, its factors of \(\delta\), and the full response-energy identity are correct.

The top residual bound (16) follows from \(p_3=0,q_3=C\), the displayed bounds on \(\alpha_3,\gamma_3\), and (9). No product of two merely \(L^2\) uncontrolled fields is used there: one factor is the bounded readout.

For the remaining bounded Hessian terms, the backward equations give

\[
\|P_2(t)\|_2\le2K\varepsilon\beta Rt=L_Pt,
\qquad
\|Q_2(t)\|_2\le K(\varepsilon^2+\delta^2\beta^2)Rt=L_Qt.
\]

The exact trained \(A\) returns therefore have the stated bounds \(\delta H L_P^2t^3\) and \(mL_Q^2t^3\). Every mixed operator contribution is bounded by the first term of \(H_T\), using \(\|\eta_W\|_{\rm op}\le\|\eta_W\|_{\rm HS}\) and \(\|dh_\ell\|_2+\|dk_\ell\|_2\le\Gamma N_\ell\|\eta\|/\delta\). Finally,

\[
\|\xi_{\ell,+}\|_2^2+\|\xi_{\ell,-}\|_2^2
=2(\|\xi_{M_\ell}\|_2^2+\|\xi_{D_\ell}\|_2^2)
\le2N_\ell^2\|\eta\|^2
\]

bounds the top curvature by \(4\varepsilon RTN_3^2\|\eta\|^2/\delta\) and each trained-return curvature by \(4\varepsilon N_\ell^2(U_\ell^P+U_\ell^Q/\delta)\|\eta\|^2\). These are exactly the remaining terms of \(H_T\). Since \(\lambda\ge0\), the inequality (21) has the correct direction. No further scalar Hessian term has been dropped from this decomposition.

## 7. The unresolved products are real proof obligations, not disproved claims

The surviving middle curvature is exactly (18), with

\[
B_{0,e}^*(b_3C)+\frac{\sigma}{\delta}B_{0,o}^*(a_3C)
\]

evaluated on the actual current trajectory and multiplied by the actual curvature and \(\xi_{2,\sigma}^2\). Its differentiated-backward counterpart is the residual pair (19). The first-layer initialized-return curvature is (20); the corresponding unresolved residuals are

\[
\alpha_1 A_{0,e}^*P_2+\gamma_1 A_{0,o}^*Q_2,
\qquad
\delta^2\gamma_1 A_{0,e}^*P_2+\alpha_1 A_{0,o}^*Q_2.
\]

The proved bounds give the initialized returns and preactivation variations in \(L^2\), but not their required products. For example, using only bounded curvature, the available Hölder estimate for a scalar curvature term would require

\[
\int |r|\,|\xi|^2
\le\|r\|_2\|\xi\|_4^2,
\]

and no \(L^4\) bound on these responses is proved. Likewise, the \(L^2\) norm of \(\alpha r\) is not controlled by two \(L^2\) norms. Keeping the exact quartic curvature is appropriate, but its vanishing at zero and decay at infinity provide no proved relation between this multiplier, the initialized return, and the perturbation. A bound on their actual product, or another justified way of controlling these contributions, remains necessary.

This is a lack of a demonstrated estimate, not a constructed reachable-state counterexample or an impossibility theorem. The candidate expressly leaves both existence and control of the relevant population-response products open. Consequently (17)–(21) are valid identities and estimates on their stated domain of justified differentiations and products; they do not establish a bounded Hessian on the whole parameter Hilbert space or construct the required population response for every source. That domain qualification is essential and is present in the candidate.

All constants containing \(\delta^{-1}\) are finite at each fixed allowed input pair. The antipodal case \(\delta=1,\mu=0\) is included by omitting \(U\); no division by \(\mu\) occurs. No angle-uniform response estimate as \(\rho\uparrow1\) is claimed, and the activation itself does not change with the angle or horizon.

The finite-dimensional interpretation of the identities is also subject to the symmetric-base specialization where used. No independently initialized finite network is silently assigned exact exchange symmetry or zero readout. The review therefore accepts the stated partial a priori results, including the actual transport closure, while leaving the initialized-return response problem and the full contract unresolved.
