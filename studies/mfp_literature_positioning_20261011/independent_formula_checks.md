# Independent checks of selected primary-source formulas

This is a fresh, scoped reconstruction from the supplied PDFs. It does not use prior reports, manuscript claims, other studies, or Git history. Sources checked were TP IV arXiv v3, especially pp. 43, 48–53 and 57–61; Aitken–Gur-Ari, especially pp. 1–8 and 16–18; and Dyer–Gur-Ari, especially pp. 17–19 and 31–34. The conclusions below concern these frozen versions. They do not assert that a later correction does or does not exist.

Primary files: [TP IV](../../data/generated/mfp_literature_positioning_20261011/tp4/arxiv-v3.pdf), [Aitken–Gur-Ari](../../data/generated/mfp_literature_positioning_20261011/feynman/aitken.pdf), [Dyer–Gur-Ari](../../data/generated/mfp_literature_positioning_20261011/root/feynman.pdf). Independent scratch, fresh text extractions, page images and numerical checks are in [independent_formulas](../../data/generated/mfp_literature_positioning_20261011/independent_formulas/). The numerical checks illustrate the analytic calculations; the counterexamples do not depend on numerical fitting.

## 1. Tensor Programs IV

### A direct one-hidden-layer test of H.41–H.43

Use a scalar training input equal to 1, unit-variance independent Gaussian initial preactivation $Z$ and readout $V$, and initial loss derivative equal to 1. In the one-hidden-layer mean-field parametrization, the first-step preactivation is exactly

\[
Z_1=Z-\eta V\phi'(Z).
\]

This is the $L=\ell=1$, $\beta^1=-1$, $\widetilde Z_0^1=V$ specialization of H.37. Write

\[
\lambda(\eta)=\mathbb E\phi(Z_1)^2,\qquad
\gamma(\eta)=\mathbb E\phi(Z)\phi(Z_1),\qquad
\gamma_{11}(\eta)=\mathbb E\phi'(Z)\phi'(Z_1).
\]

For fixed positive smoothing parameter, the source's smoothed activation and all needed derivatives have sufficient Gaussian integrability. Differentiating these expectations therefore gives

\[
\begin{aligned}
\lambda''(0)&=\mathbb E(\phi^2)''(Z)\phi'(Z)^2=\kappa_2,\\
\gamma''(0)&=\mathbb E\phi(Z)\phi''(Z)\phi'(Z)^2=\kappa_3,\\
\gamma_{11}''(0)&=\mathbb E\phi'''(Z)\phi'(Z)^3=\dot\kappa_3,\\
\left.\frac{d^2}{d\eta^2}\mathbb EZ_1^2\right|_{\eta=0}
&=2\mathbb E\phi'(Z)^2.
\end{aligned}
\]

H.41 and H.42 instead give $2\kappa_2,2\kappa_3,2\dot\kappa_3$, because their $C$ is defined as twice the squared perturbation scale. H.43 gives 4 for the last quantity. For the source's smoothed activation, $0<\phi'<1$, so the correct last quantity is strictly below 2. These are discrepancies in the printed identities, already within their intended activation class.

The H.41 proof locates the factor error: the second derivative of $\phi(Z_1)^2$ contains $(\phi^2)''(Z_1)(\partial_\eta Z_1)^2$, without the additional factor 2 printed on p. 60.

More generally, taking H.37's scalar representation and the ZHat independence rule as the setup, define

\[
D_l=(\beta^l(0))^2\mathbb E(\widetilde Z_0^l)^2.
\]

The corresponding corrected second-derivative formulas are

\[
\begin{aligned}
(\lambda^l)''(0)&=D_l\kappa_2^l+
\tfrac12\kappa_1^l(\lambda^{l-1})''(0),\\
(\gamma^l)''(0)&=D_l\kappa_3^l+
\tfrac12\gamma_{02}^l(0)(\lambda^{l-1})''(0)
+\gamma_{11}^l(0)(\gamma^{l-1})''(0),\\
(\gamma_{11}^l)''(0)&=D_l\dot\kappa_3^l+
\tfrac12\gamma_{13}^l(\lambda^{l-1})''(0)
+\gamma_{22}^l(\gamma^{l-1})''(0),\\
\left.\partial_\eta^2\mathbb E(Z_1^l)^2\right|_0
&=(\lambda^{l-1})''(0)+2D_l\gamma_{11}^l(0).
\end{aligned}
\]

The last line follows directly by expanding the square in H.37: the cross term vanishes by independence and centering, the Gaussian part has variance $\lambda^{l-1}(\eta)$, and the perturbation's second moment is $\eta^2\beta^l(\eta)^2\mathbb E(\widetilde Z_0^l)^2\gamma_{11}^l(0)$. H.43 therefore needs more than a change in $C$.

### H.44: the signs and the small-smoothing limits are different claims

Definition H.1 gives

\[
\phi_\sigma(z)=zF(z/\sigma)+\frac{\sigma}{2\sqrt\pi}e^{-z^2/\sigma^2},
\qquad F(u)=\frac{1+\operatorname{erf}(u)}2.
\]

Consequently,

\[
\phi_\sigma'=F(z/\sigma),\quad
\phi_\sigma''=\frac{e^{-z^2/\sigma^2}}{\sigma\sqrt\pi},\quad
\phi_\sigma'''=-\frac{2z e^{-z^2/\sigma^2}}{\sigma^3\sqrt\pi}.
\]

Let $Z\sim N(0,q)$, $q>0$, and let $p(0)=(2\pi q)^{-1/2}$ denote its density at zero. The correct limits are

| Quantity in H.44 | As $\sigma\downarrow0$ |
|---|---|
| $\mathbb E(\phi_\sigma^2)''(Z)$ | $1$ |
| $\mathbb E(\phi_\sigma^2)''(Z)\phi_\sigma'(Z)^2$ | $1$ |
| $\mathbb E\phi_\sigma(Z)\phi_\sigma''(Z)\phi_\sigma'(Z)^2$ | positive, $\Theta(\sigma)$ |
| $\mathbb E\phi_\sigma(Z)\phi_\sigma''(Z)$ | positive, $\Theta(\sigma)$ |
| $\mathbb E\phi_\sigma''(Z)^2$ | $p(0)/(\sigma\sqrt{2\pi})+o(\sigma^{-1})$ |
| $\mathbb E\phi_\sigma'(Z)\phi_\sigma'''(Z)$ | $-p(0)/(\sigma\sqrt{2\pi})+o(\sigma^{-1})$ |
| $\mathbb E\phi_\sigma'''(Z)\phi_\sigma'(Z)^3$ | negative, $-\Theta(\sigma^{-1})$ |

Here is sufficient detail to verify every limiting scale. Put $g(u)=uF(u)+e^{-u^2}/(2\sqrt\pi)$, so $\phi_\sigma(\sigma u)=\sigma g(u)$. Substitution $z=\sigma u$ gives

\[
\begin{aligned}
\mathbb E\phi_\sigma\phi_\sigma''\phi_\sigma'^j
&=\frac\sigma{\sqrt\pi}\int g(u)e^{-u^2}F(u)^j p(\sigma u)\,du,
\quad j=0,2,\\
\mathbb E\phi_\sigma''{}^2
&=\frac1{\sigma\pi}\int e^{-2u^2}p(\sigma u)\,du.
\end{aligned}
\]

The first integrals tend to positive finite constants after dividing by $\sigma$. Also $\mathbb E\phi_\sigma'^2\to1/2$ and $\mathbb E\phi_\sigma'^4\to1/2$ by bounded convergence. The identity $(\phi^2)''=2\phi'^2+2\phi\phi''$ then gives the first two limits. Finally, integration by parts in the rescaled variable gives

\[
\mathbb E\phi_\sigma'''\phi_\sigma'^3
\sim-\frac{3p(0)}{\sigma\pi}
\int e^{-2u^2}F(u)^2\,du.
\]

The analogous calculation with $F$ in place of $F^3$ gives the displayed coefficient for $\mathbb E\phi_\sigma'\phi_\sigma'''$. Gaussian decay justifies the dominated convergence in these rescaled integrals. All the positivity claims in H.44 hold; both negative expectations are negative for every positive $\sigma$, by pairing $u$ with $-u$. Its assertion that the first five expectations all converge to zero is false.

### Consequences for H.45, H.46 and use of the paper

For the one-layer example above, $\lambda''(0)\to1$, whereas $\gamma''(0)\to0$. Thus H.45's claimed vanishing of both derivatives is false. The positive signs survive this correction. The corrected prefeature second derivative also remains positive. The errors therefore do not refute feature movement in this example.

H.46's proof uses the false claims $\gamma_{22}^l\to0$ and $(\lambda^l)''(0)\to0$. Its printed argument cannot establish its conclusion as written. There are additional local problems in its output identity:

* Differentiating $-\eta a(\eta)$ three times at zero gives $-3a''(0)$, not $-a''(0)$.
* From H.37 and ZHat independence, the contribution of the initial last-layer readout is $\eta\beta^L(\eta)\gamma_{11}^L(\eta)$. Replacing $\beta^L$ by $-\gamma^{L-1}$ omits its inherited term when earlier layers move.
* For general scaling choices, comparison with Eq. (55) shows the direct-update term in H.37's recurrence must retain its limiting coefficient: $\beta^l=-a_l\gamma^{l-1}+\beta^{l-1}\gamma_{11}^{l-1}$, where $a_l=\lim\theta_{W^l}\in\{0,1\}$ for moving layers. The fact that $\theta_l=1$ need not imply $a_l=1$; Eq. (46) defines $\theta_l$ as the maximum over earlier layers.

These observations identify a proof repair requirement, not a counterexample to H.46's nonzero-cubic conclusion. The one-layer case can be repaired completely. Its limiting updated output, when both layers have the mean-field update scale, is

\[
f_1(\eta)=\mathbb E[(V-\eta\phi(Z))\phi(Z-\eta V\phi'(Z))],
\]

and direct differentiation gives

\[
f_1'''(0)=-3\bigl(\dot\kappa_3+\kappa_3\bigr)>0
\quad\text{for sufficiently small }\sigma,
\]

because the first term tends to $-\infty$ and the second tends to zero. This verifies the intended nonlinear dependence on the step size in this branch.

There is also a plausible finite-depth repair within the displayed Gaussian recurrence: its corrected equations give $(\lambda^l)''(0)=\Theta(1)>0$, $(\gamma^l)''(0)=O(\sigma)>0$, and $(\gamma_{11}^l)''(0)=-\Theta(\sigma^{-1})$. In particular the previously problematic product $\gamma_{22}^l(\gamma^{l-1})''(0)$ is only $O(1)$, while the negative terms in the last recurrence diverge. This report does **not** certify every parametrization branch, the lagged-initial-readout case, or the complete classification theorem by this observation.

The distinction matters for literature positioning. Remark H.15 explicitly separates the general tensor-program evaluation of fixed finite training histories, under the required activation regularity, from the special-activation argument used to classify feature learning versus kernel behavior. The identified defects are in that explicit one-step classification argument and its derivative identities. They do not by themselves contradict the master theorem or the existence of the finite-history scalar program. Conversely, fixed-history evaluability does not validate the false derivative formulas or automatically supply a fixed-size autonomous reduced model.

## 2. Aitken–Gur-Ari

### Eq. (11) has an extra first-layer width normalization

The model on p. 3 uses $d^{-1/2}U x$ at the first layer, $n^{-1/2}W^{(l)}$ at later hidden layers, and $n^{-1/2}V$ at the readout. The definition of $U_i(x)$ below Eq. (11) already contains $d^{-1/2}$, with no width normalization. Consequently a monomial having $p_l$ factors at layer $l$ has width factor

\[
n^{-(1+p_2+\cdots+p_L)/2},
\]

not Eq. (11)'s $n^{-(1+p_1+\cdots+p_L)/2}$. For the paper's one-layer quadratic example, the true factor is $n^{-1/2}$; Eq. (11) would give $n^{-3/2}$. Its coefficients are stipulated to be independent of $n$, so they cannot absorb the discrepancy.

The corresponding exponents in Eqs. (12) and (14) also require correction. The proof's U-pair counting largely follows the correct convention: adding a U pair introduces no net new free neuron index unless it connects components, in which case the covariance delta removes a sum. The parenthetical attribution of this loss to “explicit normalization factors” is incorrect for U. Removing $p_1$ from the normalization and attributing that loss to the delta constraint reconciles the local count. This check does not disprove the main correlation-exponent theorem; it exposes a mismatch between its displayed monomial expansion and the actual network.

### Exact check of the $C_{4,2}$ example and its variance

Use exactly the example on pp. 3–4:

\[
f(x)=\frac{x^2}{\sqrt n}\sum_{i=1}^n V_iU_i^2,
\qquad U_i,V_i\overset{\mathrm{iid}}\sim N(0,1).
\]

Set $P=\prod_{a=1}^4x_a^2$, $A_i=V_iU_i^2$, and $B_i=8V_iU_i^2(V_i^2+U_i^2)$. Differentiating the network with respect to all U and V parameters gives, for the random variable whose expectation is $C_{4,2}$,

\[
F_{4,2}=\frac P{n^2}\left(\sum_i A_i\right)\left(\sum_i B_i\right).
\]

Indeed the nonzero second derivatives are $\partial_{U_i}^2f=2V_ix^2/\sqrt n$ and $\partial_{U_i}\partial_{V_i}f=2U_ix^2/\sqrt n$. The UU contribution to the three-derivative contraction is $8V_i^3U_i^2/n^{3/2}$; the two mixed contributions total $8V_iU_i^4/n^{3/2}$.

Gaussian even moments give

\[
\mathbb EA_i=\mathbb EB_i=0,\quad
\mathbb EA_i^2=3,\quad
\mathbb EA_iB_i=192,\quad
\mathbb EB_i^2=15360,\quad
\mathbb EA_i^2B_i^2=4515840.
\]

Independence across neurons therefore yields the exact identities

\[
\mathbb EF_{4,2}=\frac{192P}{n},\qquad
\operatorname{Var}(F_{4,2})
=P^2\left(\frac{82944}{n^2}+\frac{4396032}{n^3}\right).
\]

For verification of the variance, if $A=\sum_iA_i$ and $B=\sum_iB_i$, then

\[
\mathbb EA^2B^2=n\mathbb EA_i^2B_i^2
+n(n-1)\bigl(\mathbb EA_i^2\mathbb EB_i^2+2(\mathbb EA_iB_i)^2\bigr),
\]

and $\mathbb EAB=n\mathbb EA_iB_i$. Subtracting its square gives the coefficients above. The source's Eq. (8), $\mathbb E\prod_a f(x_a)=(27+288/n)P$, is consistent with the same model, since $\mathbb EA_i^4=315$. Thus the discrepancy cannot be removed by changing the normalization of the example.

The PDF visibly prints 132, rather than 192, for the $C_{4,2}$ coefficient below Eq. (8). This is a local coefficient error; its exponent $n^{-1}$ remains correct.

The case study after Corollary 1 on p. 17 is a separate error. $C_{4,2}$'s cluster graph has component sizes 3 and 1, hence $(n_e,n_o)=(0,2)$, as stated earlier and in Table 2. The p. 17 case study instead uses $(1,0)$ and claims $O(n^{-3})$ variance. The exact variance above disproves that claim for nonzero inputs. Corollary 1, applied with the correct graph, predicts $O(n^{-2})$, agreeing with the calculation and Table 2. Connecting the isolated vertex in one copy to the isolated vertex in the other leaves component sizes 3, 3 and 2; it does not produce the single eight-vertex component claimed in the accompanying discussion. This is a misapplication in the example, not a counterexample to the correctly applied corollary.

## 3. Dyer–Gur-Ari

### Eq. (106) to Eq. (109): a finite-sum index error

For the truncated order-$1/n$ calculation, let $r_t=f_t-y$, $Q=I-\eta\Theta_0$, and let $O_{4;0}(\mathbf x)$ be the row vector over training examples. The stated leading residual and Eq. (106) give

\[
r_t=Q^tr_0,\qquad
O_{3;t+1}(\mathbf x)-O_{3;t}(\mathbf x)
=-\eta O_{4;0}(\mathbf x)Q^tr_0.
\]

Starting at $t=0$, the solution is

\[
O_{3;t}=O_{3;0}-\eta O_{4;0}\sum_{s=0}^{t-1}Q^sr_0.
\]

If $\Theta_0$ is invertible, this is

\[
O_{3;t}=O_{3;0}-O_{4;0}\Theta_0^{-1}(I-Q^t)r_0.
\]

Eq. (109) has an extra $Q$, corresponding to summing from 1 to $t$, as in the printed Eq. (108), rather than from 0 to $t-1$. At $t=1$, Eq. (106) requires $-\eta O_{4;0}r_0$; Eq. (109) gives $-\eta O_{4;0}Qr_0$. Their discrepancy is already of the retained $1/n$ order for a fixed nonzero learning rate. Eq. (107) additionally drops the factor $\eta$ present in Eq. (106). The polynomial finite-sum formula above is the appropriate repair when $\Theta_0$ is singular; an inverse should not be introduced in that case.

A network check realizes the recurrence: for $f=n^{-1/2}\sum_i u_iv_i$ on one training example,

\[
\Theta=\frac1n\sum_i(u_i^2+v_i^2),\quad
O_3=\frac{4f}{n},\quad O_4=\frac{4\Theta}{n}.
\]

An exact simultaneous gradient step with residual $r=f-y$ gives

\[
f_+=f-\eta r\Theta+\frac{\eta^2r^2f}{n},\qquad
O_{3;+}-O_3=-\eta O_4r+\frac{4\eta^2r^2f}{n^2}.
\]

For bounded $f,r,\Theta$, its leading correction is Eq. (106)'s first-step formula. The extra $Q$ in Eq. (109) is not supplied by the omitted $n^{-2}$ term. This is an algebraic error in the displayed discrete correction, with a direct repair; it does not disprove the continuous-time calculation or the diagrammatic scaling theorem.

### Smoothness alone does not supply the moments in Theorem 7

The one-hidden-layer proof on pp. 17–19 bounds the expectations in Eq. (46) by a finite $s_{\max}$. Smoothness alone does not imply that bound. For example, the smooth activation $\phi(z)=e^{z^2}$, unit Gaussian first-layer weights, and scalar input 1 give $\mathbb E f(1)^2=\mathbb E e^{2Z^2}=\infty$. Thus the unqualified smooth-activation claim needs a Gaussian-integrability hypothesis for every activation-derivative product used by the selected correlation function. Polynomial growth of the relevant derivatives is one sufficient condition. This is a missing assumption, not a failure of the counting argument for activations satisfying it.

## Verdict and limits

The frozen sources contain verifiable local normalization, derivative, and summation errors, and two false auxiliary asymptotic statements in TP IV. The Aitken variance case study is false for its named observable, while the correctly applied corollary survives the explicit test. Dyer's discrete formula has a repairable off-by-one error and its smooth-activation statement needs integrability. TP IV's printed special-activation proof needs substantive correction; the intended one-step nonlinearity conclusion survives the fully checked one-layer repair. None of these checks establishes that the central TP classification theorem or the central correlation-exponent theorem is false, and this report does not certify their entire repaired proofs.
