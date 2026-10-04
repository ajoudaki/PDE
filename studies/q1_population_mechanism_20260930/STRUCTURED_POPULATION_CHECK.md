# Structured population assembly: scoped internal mathematical check

Checker: `structured_assembly_check`, 2026-09-30.

**Final verdict: PASS for the stated conditional, sufficiently-small-fixed-epsilon local theorem and the stated architectural/endpoint constraints.** No blocking mathematical defect was found in the assigned assembly. One minor coordinate-notation ambiguity in the original frozen main file was reported and corrected; the original observation and correction check are retained below. This is an internal candidate check, not a promotion review or a proof that the assumed population flow exists.

## Scope and frozen evidence

The scientific inputs read completely were exactly the five assigned files and the two assigned generated certificates. No study README, other route, prior check report, other study, manuscript reconciliation file, book passage, Git history, or external scientific source was read. The corrected Section 7 was subsequently checked under an explicit bounded follow-up from the supervisor.

| Input | Verified SHA256 |
|---|---|
| Original `STRUCTURED_POPULATION_ANALYSIS.md` | `4eeb35371575281e4622e783da4e9cfc5577c1af13b80b86762a1bb7c711c7a7` |
| `WEAK_FACTOR_ROUTE.md` | `3ed97591b90f84d0fc14eb06c9bbca1f95410fde5c8d3b8bc22e695fb525a337` |
| `WEAK_FACTOR_SECOND_LAYER.md` | `8f1a558285028573ffb101eadb61603f94cbe666a6bee6236cd7b1d193ee7fd7` |
| `weak_factor_interval_certificate.py` | `51c7570b1f34a066287f286295868c87283ac45f16d0895d4b4d716c7010be54` |
| `weak_factor_coefficient_certificate.py` | `9d0b0322bcc59a88c6ca5bef1b6ac69911bd035c2cd92006b08e4e511605bba5` |
| `weak_factor_interval_certificate_20260930_01/results.json` | `316a83c28ccba4415d47d54f6bdb7ad2cd1a307150e86e0b9694ce4feded62cf` |
| `weak_factor_coefficient_certificate_20260930_01/results.json` | `586699805890bb62ee02dee03a2a091fafcfe63f4fb07f68e8cc3dae92349f1a` |

The last two paths are under `data/generated/q1_population_mechanism_20260930/`. The main theorem was checked from the equations and certificates themselves, not another checker’s verdict. Required skills were `solve-math-rigorously` and the claim-boundary/adversarial checklist of `investigate-conjectures`.

Provenance disclosure: a fresh prompt-only auxiliary checker received only the explicit mathematical hypotheses of (19)--(22), and supplied proofs of those bounds and the normal form. It read no repository scientific material or prior findings. The derivations below were also checked directly by the named checker. No pre-existing agent research or external verdict was used. The auxiliary work is part of this internal assembled check, not a second promotion review.

## 1. Population assumptions and normalization

The population flow and its canonical reused Gaussian source are explicit hypotheses. In particular the true-adjoint rule with the **full** source Gram is assumed, as are the joint marked realization, sufficient differentiability/integrability, uniqueness and equivariance. Replacing its Gaussian innovation covariance by a regression residual would change the second-layer calculation. The main file does not make that replacement or assert closure of unmarked marginal laws.

Normalization within equations (3)--(6) is consistent. From $r_a=y_a(f-1)$, $\rho=1-f$ while $f<1$, and $ds/dt=2(1-f)$, one obtains

\[
W'=G_y,\qquad A'=\operatorname{mean}_a y_aL_au_a,\qquad
V_a'=y_aD_a,\qquad \tau'=\tfrac12,\qquad
K_a'=\frac{H_a-K_a}{2+s}.
\]

Thus $\tau=1+s/2$. The factor $1/4$ in the memory operator and the normalized sample averages survive unchanged. Initially $W=V=0$, $K=H$, hence $A'=V'=K'=G'=0$. For any displayed hidden energy $E$, $E'(0)=0$, so the chain rule gives $\ddot E(0)=4E''(0)$. No additional clock or learning-rate factor is missing.

Agreement of these stipulated equations with material outside the frozen packet was outside scope. In particular the main file’s manuscript dictionary was not independently checked against its excluded reconciliation file. This is a check of the stated population model.

## 2. Symmetry and operational decoding

Bit flips permute the examples and reverse the labels. Under simultaneous label reversal, $W,r,D,L$ reverse sign, while $A,V,K,\tau$ remain unchanged: both products $rL$ and $rD$ are unchanged. Together with input-rotation equivariance and initialization symmetry, this gives the asserted output character $F_a=y_af$ and the invariant hidden covariance under the two bit translations. The signed-input argument in the main file gives the same covariance symmetry.

An invariant covariance on this four-element group is diagonal in its normalized Walsh basis. Hence the four hidden fields are pairwise orthogonal; exchange of the last two input coordinates identifies the factor energies. If $Q_a=\sum_\psi\psi(a)Q_\psi$ and $E_\chi=\|Q_\chi\|^2>0$, then

\[
\left\langle Q_\chi/E_\chi,Q_a\right\rangle=\chi(a).
\]

Every feasible decoder satisfies $\langle b,Q_\chi\rangle=1$, giving $\|b\|^2\ge1/E_\chi$. This proves (8), including the impossibility when $E_\chi=0$. The decoder claim concerns exact recovery on the four specified examples; it does not imply a claim for an unseen distribution. Its use as a strict improvement in minimum decoder norm is valid.

## 3. First-layer identity, coefficients and mean drift

In the first route the matrix

\[
C_{ab}=\frac{y_ay_b}{16}\mathbb E[\phi'(z_a)\phi'(z_b)]
+\mathbf1_{a=b}\frac{y_a}{4}\mathbb E[g_y\phi''(z_a)]
\]

is exactly half the expected Hessian of $g_y^2$. Gaussian covariance differentiation therefore gives $\delta J=\sum C_{ab}\delta Q_{ab}$. The symmetric derivative of $H_aH_b$ has two equal terms, whereas the acceleration contains one; this verifies the factor $1/2$ in main (10). Walsh symmetry makes the corresponding covariance derivative diagonal, so the formula applies pointwise in the initial root after conditional expectation. The independent reverse innovation disappears only from that conditional mean.

I checked all seven leading gradient Gram entries in first-route (7). For example,

\[
\nabla h_\sigma^2=2\varepsilon^2(Y^2pq,Yp^2,0)+O_{L^r}(\varepsilon^4),
\]
\[
\nabla h_y^2=2\varepsilon^4(Y^2Z^2qr,YZ^2q^2,Y^2Zq^2)
+O_{L^r}(\varepsilon^6).
\]

Their dot product has expectations $12\mathbb E[pq^2r]+4\mathbb E[p^2q^2]$ at order six, and the self-product of the latter gradient has $36\mathbb E[q^2r^2]+24\mathbb E q^4$ at order eight. The reductions $q=-2\phi p$, $r=4p-6p^2$, $\phi^2=1-p$ give precisely the moment polynomials in first-route (8). The three main first-layer coefficients are $F_\sigma/2,F_0/2,F_y/2$, not the undivided brackets.

The variance derivative coefficients in route (6) follow from the heat identity applied before remainder estimation; they are not inferred by differentiating an uncontrolled big-O term. Both ratio formulas (10)--(11) have the correct denominators and scaling. Their denominators are nonzero near the limiting geometry because $v>0$ and $a_1>0$.

For the new mean drift (13), the $y$-character contributes

\[
\tfrac12J_y\partial_Y h_y^2
=\varepsilon^4 T_1 YZ^2q^2+O_{L^r}(\varepsilon^6),
\]

and the sigma-character contributes

\[
\tfrac12J_\sigma\partial_Y h_\sigma^2
=\varepsilon^4T_2aYp^2+O_{L^r}(\varepsilon^6).
\]

The context and tau terms start at order six. Thus (13) is correct, as is

\[
(\mathbb EY^2)''=2\varepsilon^4(T_1b+T_2a^2)+O(\varepsilon^6).
\]

This is a conditional mean and an averaged squared-weight claim. The Lr remainder does not make it a pointwise sign theorem for every actual neuron; the main file correctly avoids that conclusion.

## 4. Second-layer assembly and local-time implication

Direct differentiation of the memory term gives $Z_{a,\mathrm{memory}}''=\frac14\sum_bU_bC_{ab}$; terms involving $V$ or $V'$ vanish at initialization. Another normalized sample mean gives $2/16$ in main (14). The readin term transposes to $2\mathbb E A_U\cdot A_{Y^\chi}$, with no extra factor four.

The Walsh reverse-call rule has no additional normalization factor: $\sum_b\mathbb E\partial_{z_b}U_\chi H_b=\sum_\psi\mathbb E\partial_{Z_\psi}U_\chi H_\psi$. Character parity removes the off-diagonal terms. The exact coefficients $\beta_\chi=\mathbb E Q_{y\chi}^2+\mathbb E G_yR_y$ and the corresponding $\gamma_\chi^k$ are consistent with the first-layer heat derivatives.

I checked the drift dot product, both leading source-product expectations, the gradient-norm orders and the variance orders in second-route Sections 4--5. They give exactly its $\mathfrak D_1,\mathfrak N_1,\mathfrak M_1$ and context analogues. In particular the full reverse covariance contributes at order six for the bit; it cannot be omitted. The main coefficient is twice the sum of the three route coefficients. Every polynomial in second-route (6.1) agrees with the derivative identities. The main table of contributions includes that factor two.

Bounded tanh derivatives and finite Gaussian polynomial moments control the displayed startup expansions. The positive limiting normalized variances allow the fixed-Gaussian coupling without a singular square root. The derivations retain only exact initial accelerations, so no convergence of a time power series is needed.

The signed leading coefficients and their higher-order epsilon remainders yield one sufficiently small epsilon threshold for the finite collection of signs. For each fixed positive epsilon below it, continuity of the energy second derivatives and their zero first derivatives gives strict increase/decrease on a common positive initial interval. Since $f(0)=0$, the feature clock is increasing there. This justifies the theorem’s quantifiers and does not yield an explicit moderate-epsilon threshold, a uniform time interval, or an all-time sign assertion.

## 5. Output cubic and strict positivity

Write $g(s)=G_y(s)$ as an L2-valued function. Since $g'(0)=0$,

\[
g(s)=g(0)+\tfrac12g''(0)s^2+o_{L^2}(s^2),\qquad
W(s)=sg(0)+\tfrac16g''(0)s^3+o_{L^2}(s^3).
\]

Multiplication gives

\[
f(s)=\kappa s+\tfrac23\langle g(0),g''(0)\rangle s^3+o(s^3)
=\kappa s+\tfrac13E_{2,y}''(0)s^3+o(s^3),
\]

so the cubic factor in (15) is correct. Taking $\chi=y$ in (14) makes $Y=U$, and Walsh diagonalization gives (16) with its factor two.

For every allowed nondegenerate dataset $v_y>0$: the mixed finite difference of tanh is not the zero analytic function of the Gaussian root, as seen by its nonzero mixed derivative at $a=b=0$ and any background logit where tanh'' is nonzero. Conditional on the other forward Walsh calls, $G_y$ is strictly increasing in $Z_y$, with derivative $Q_0>0$. Thus $G_y\ne0$ in L2. The term $v_y\mathbb E(G_yQ_0)^2$ establishes strict positivity in (16).

The interval for the leading $\kappa$ coefficient encloses the quoted $0.260678\ldots$. The physical-time identities $\dot f(0)=2\kappa$, $\dot L(0)=-4\kappa$ follow immediately. No later fitting rate follows from this startup expansion; the main file states that restriction.

## 6. All-time factor constraint and unseen-query normal form

For the first-layer finite differences in (17), both differences have the sign of the sigma-direction logit coefficient. Their sum/difference therefore proves $|H_y|\le|H_\sigma|$, with strictness for finite logits and a nonzero sigma coefficient. Exchanging the bits proves the other inequality. It is statewise and does not rely on the flow assumptions.

For (19), define $D_t^H=(H_{+,t}-H_{-,t})/2=H_\sigma+tH_y$ and similarly $D_t^G$. Pointwise Lipschitz continuity and boundedness of $B$ give

\[
\begin{aligned}
\|G_y\|_2^2
&\le\tfrac12(\|D_+^G\|_2^2+\|D_-^G\|_2^2)\\
&\le\tfrac12(\|B(H_\sigma+H_y)\|_2^2+
                  \|B(H_\sigma-H_y)\|_2^2)\\
&=\|BH_\sigma\|_2^2+\|BH_y\|_2^2
\le2\|B\|^2E_{1,\sigma}.
\end{aligned}
\]

No hidden-field orthogonality is required in this argument; the parallelogram identity cancels the cross terms. Cauchy--Schwarz then proves (20). Its stated nonzero-norm restriction is necessary for division and is included. If either norm vanishes, $f=0$; the undivided inequality still holds. A bounded fitted endpoint has a strictly positive bound for both factors, but no epsilon-uniform norm bound or endpoint existence follows.

The label-reversal symmetry checked above gives each bit oddness in (21); exchanging the last two coordinates gives the exchange symmetry. Architectural oddness follows from odd tanh and linear $B$. Combining global oddness with the two bit oddness relations gives background-coordinate oddness. These identities persist under pointwise convergence.

For a C3 endpoint in normalized query coordinates, the fundamental theorem of calculus gives the continuous quotient

\[
F_*(u)=u_0u_1u_2Q(u),\qquad
Q(u)=\int_{[0,1]^3}\partial_0\partial_1\partial_2
F_*(r_0u_0,r_1u_1,r_2u_2)\,dr.
\]

The quotient is separately even and invariant under exchange of the last two coordinates away from the planes; continuity extends these properties to the planes. Defining $\Psi(r)=Q(\sqrt{r_0},\sqrt{r_1},\sqrt{r_2})$ gives a continuous function on the closed positive orthant and establishes (22). Interpolation forces $\Psi(c^2,\varepsilon^2,\varepsilon^2)=1/(c\varepsilon^2)$. C3 gives continuity of this quotient, not unspecified higher smoothness in squared coordinates. The main file does not claim that stronger conclusion or infer C3 from a mere pointwise limit.

## 7. Interval certificate audit and reproduction

The interval class uses directed arithmetic for addition, multiplication, division and exact rational conversion; negation avoids ambient Decimal precision. One adjacent representable endpoint on each side of correctly rounded Decimal exp/sqrt encloses the transcendental operations used here. All denominators and square roots in this execution lie in their required domains. The Machin enclosure uses exact rational alternating-series bounds before outward conversion.

The integrand is evaluated in the standard-normal coordinate. The derivative operator $D=(1-t^2)d/dt$ gives exactly the integer polynomial coefficient bounds in the source. Since the variance is at most one, no omitted scale factor increases the derivative bound. Leibniz with the supplied Gaussian derivative bound yields the stated $M_n$; the composite Simpson bound, doubled for symmetry, is $20h^4M_n/180$. The positive tail is bounded by $2\phi(10)/10$. Uncertainty of the outer variance is propagated at every node, so the result is not merely a floating-point tolerance estimate.

The coefficient code implements the route formulas with the correct factors and ratio denominators. All displayed main intervals are outward widenings of its stored intervals, including the second-layer component intervals and both hierarchy ratios. The first-moment source hash, coefficient source hash and stored input hash match the frozen files.

Both scripts were executed with `python -B`, writing only fresh check-owned paths. The moment intervals and first coefficients matched the frozen output exactly; only elapsed time changed. All second-layer and ratio intervals also matched exactly. No training simulation or new scientific experiment was run.

Reproduction outputs under `data/generated/q1_population_mechanism_20260930/structured_assembly_check_20260930_01/`:

| Output | SHA256 |
|---|---|
| `interval_reproduction.json` | `b7d39ac8e9e3f88faf365119dc02b19205dc7ff1cb88173c5091f6a6c366d4b9` |
| `coefficient_reproduction.json` | `b159753033c1dc017f1697a041a9c870fecbf5c9b0d4127c9a40032aaacaea37` |

## 8. Original observation and correction addendum

**Original finding M1 — minor notation ambiguity.** In frozen main hash `4eeb3537...`, Section 1 identified manuscript coordinates as $x=\sqrt3u$, but Section 7 used $F(x)$ while imposing the normalized-coordinate amplitude condition at $(c^2,\varepsilon^2,\varepsilon^2)$. That amplitude condition is correct for the normalized query used by (3). If instead $x$ retained its manuscript-coordinate meaning, the corresponding factorization at the manuscript training input would have quotient value $1/(3\sqrt3c\varepsilon^2)$. The requested correction was to say explicitly which coordinates Section 7 uses, or consistently use $u$. No energy coefficient or symmetry sign depends on this notation choice.

**Correction addendum — closed.** The supervisor changed only Section 7 to explicitly state that $u$ denotes normalized query coordinates and $x=\sqrt3u$ the corresponding manuscript query, and changed its query variables from $x$ to $u$. The revised main SHA256 is `153947b283ec0c42c3c32e46c47e2800e4d314599308da96cc087879d854894f`. I read the complete changed section and reversed just those declared changes in memory; its resulting SHA256 exactly equalled the original frozen main hash. Thus there was no unreviewed main-file change. The corrected coordinate convention makes (22) unambiguous and closes M1.

**Final claim boundary.** The assembled result is an internally checked conditional local representation-acquisition theorem with certified scalar signs, plus exact statewise architectural inequalities and conditional endpoint constraints. Population-flow construction, global existence/fitting, bounded endpoint existence, persistence of acquisition, and generalization beyond the specified input constraints remain unproved. No missing in-scope scientific input blocked this check, and no finding from the excluded global-memory route is used to support the verdict.
