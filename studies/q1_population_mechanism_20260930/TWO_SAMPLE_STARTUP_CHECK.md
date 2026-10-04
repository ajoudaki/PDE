# Internal check of the two-sample population startup results

Checked 2026-09-30 by scoped checker `/root/population_startup_check`.

**Verdict: conditional PASS for the startup and symmetry statements, with the precise qualifications below.** I found no sign, factor, rank, or query-parity error in either frozen candidate. The first reverse law is the canonical law of this finite initialized Gaussian computation, not a consequence of merely assigning an arbitrary bounded operator its true adjoint. The time statements require the assumed strong population trajectory; its existence, uniqueness, and identification as a fixed-order trained-width limit are not proved by either candidate or by this check. This is an internal mathematical check, not a promotion review.

The qualifications that must accompany use of the result are:

1. The initialized operator must realize the **joint Gaussian forward/reverse conditioning construction**. Its initial forward covariance and adjunction alone do not determine the reverse innovation.
2. For the mixing jet, “strong solution” includes continuity of the reconstructed operator in operator norm, and the initial operator and true adjoint are bounded on the generated population spaces. These are exactly the meanings in the cited local-population source. No analyticity or convergent time series is needed.
3. Sample interchange gives exchangeability, but by itself does not give centered first-layer preactivations. Exact centering along time additionally uses the hidden-sign symmetry described below. The startup Pearson-correlation conclusion nevertheless follows from the displayed initialized jet even without assuming all-time centering.
4. All derivatives at initialization are right derivatives, in the specified feature or physical clock. The correlation statement is for each fixed nondegenerate correlation; no time interval uniform as the correlation approaches either endpoint has been proved.
5. The initial query sign is pointwise in the query. The mandatory zero plane holds throughout the assumed existence interval, but the absence of additional zeros at positive times or at a fitted endpoint remains open.

## Read scope, frozen versions, and check method

I read all 412 lines of each candidate, and all lines of the four assigned source ranges. No study README, other study, prior review, history, agent finding, external scientific source, archived book, or additional book section was consulted. No `list_agents` call was made. The symmetry candidate's own exposure disclosure at lines 7–9 was read as part of that frozen candidate; none of the earlier summaries mentioned there was retrieved.

| Frozen candidate | Lines read | SHA-256 of the complete raw file |
|---|---:|---|
| `TWO_SAMPLE_MIXING_ROUTE.md` | 1–412 | `10b415ed1249ee9f8f89b4dc58aa05c23810dcf1cd8ef2b7e7bc3a273619f622` |
| `TWO_SAMPLE_SYMMETRY_ROUTE.md` | 1–412 | `9e78832f5788f25574924216d8ff4b116feca66f328eaad38f81ac555f9b8393` |

| Assigned maintained source | Inclusive lines read | Bytes in range | SHA-256 of concatenated raw range bytes |
|---|---:|---:|---|
| `docs/02-gaussian-reuse.qmd` | 1–170 | 8269 | `1da78af8a55e0d00589209fc2137a3bba3f920783da83335cc4999c9a955c64d` |
| `docs/03-local-population.qmd` | 174–278 | 5442 | `a23dce9b5d2a3de98f274f51cf31cff5426546318c35a3a8208671883ea9e13d` |
| `paper/main.tex` | 178–443 | 14859 | `ac3b1ea9c36571f11d388efbf143cbcd6be7ea64c9a07389231c100ef5fe3fea` |
| `paper/main.tex` | 498–525 | 1591 | `8d7f6f9ece5b75c074991ed63451e4aa64e2ae8d084e2e462ad62c6d0c4ea553` |

All four range hashes equal the hashes recorded in the mixing candidate. Process reading was the complete root `AGENTS.md`, `RESEARCH_WORKFLOW.md` lines 1–151 (introduction and Part 1), both required skills at `/etc/codex/skills/{solve-math-rigorously,investigate-conjectures}/SKILL.md`, and the latter's complete `research-contract.md`, `adversarial-audit.md`, and `evidence-ledger.md` references. The scoped assignment replaced ordinary author startup. No experiment or proof-search orchestration was conducted.

The read commands were `cat` for process files, `nl -ba` for each complete candidate, and `nl -ba FILE | sed -n 'START,ENDp'` for each assigned scientific range. Hashes were computed using `sha256sum` for complete candidates and the following range procedure, which preserves line endings:

```python
lines = Path(name).read_bytes().splitlines(keepends=True)
data = b''.join(lines[start - 1:end])
digest = sha256(data).hexdigest()
```

The mathematical check was direct reconstruction of every displayed formula, the conditioning-to-population passage for the first source call, the necessary continuity arguments, sign and parity tests, and both degenerate geometries. The only use of a finite Gaussian matrix below is to verify a **fixed initialization computation** from the cited exact conditioning identity. There is no finite-width trajectory, dense trained reference, numerical integration, or experiment.

Before writing, HEAD was `7fce699a7decf2239dc3eb50486eca661783b535`; the index had no staged paths. Status was inspected as names only to preserve concurrent work. This checker owns and writes only this report; no staging or commit is performed.

## Normalization and strong-trajectory prerequisites

To avoid the candidates' different uses of the letter kappa, use the mixing notation here: the signed input correlation is \(c=u_1\cdot u_2\in(-1,1)\), and the initialized hidden-feature covariance is

\[
C=\begin{pmatrix}v&\kappa\\\kappa&v\end{pmatrix},\qquad
v=\mathbb E\tanh^2N>0,\quad |\kappa|<v.
\]

The symmetry candidate's signed input correlation called `kappa` is this \(c\). Both reports use two hidden tanh layers, unit normalized training inputs, binary labels converted to signed inputs with target \(+1\), Gaussian first rows, unit initialized mixing variance, zero readout, and the learning-speed q=1 closure. They concern population fields and the reused initialized operator, not finite scalar closure.

With synchronized residual \(e=F-1\), initially \(e=-1\). On a sufficiently short interval \(F<1\), put \(s=2\int_0^t(1-F(r))\,dr\). Then \(ds/dt=2\rho\), \(\tau=1+s/2\). If \(K_a,V_a\) denote the symmetry candidate's physical-time keys and values, and \(P_a,Q_a\) the mixing candidate's unnormalized forward and sign-reversed backward memories, the exact conversion is

\[
P_a=\tau K_a,\qquad Q_a=V_a/2,\qquad
B=T+\tfrac12\sum_aV_a\otimes K_a
 =T+\tau^{-1}\sum_aQ_a\otimes P_a.
\]

Indeed \(\dot P_a=\rho H_a\) and \(\dot Q_a=-eD_a=\rho D_a\). Dividing by \(2\rho\) gives \(P_a'=h_a/2\), \(Q_a'=D_a/2\), \(W'=g_+\), and \(A'=\frac12\sum_a\delta_a^{(1)}u_a\). These agree with the q=1 specialization of `paper/main.tex` 333–365 and the population outer-product normalization at 206–218 and 501–508. The two candidates therefore use the same closure and not two different clock conventions.

The assumptions needed for the jet are exactly continuity in \(L^2\) of the fields and in operator norm of \(B\), bounded \(T,T^*\), and the integral equations in those spaces. This is the strong-solution convention of `docs/03-local-population.qmd` 176–207. The generated-space construction and adjunction appear at 215–233. Those passages do not themselves prove the q=1 existence theorem; `paper/main.tex` 501–523 expressly leaves the fixed-q population claim conjectural.

Here is why no unproved second differentiability or \(L^4\) assertion is hidden in the startup computation. Bounded tanh activations give \(W(s)/s\to g_+\) in \(L^2\). Since the gates are bounded and converge in probability,

\[
\delta_a^{(2)}(s)/s\to U_a:=g_+k_a\quad\text{in }L^2.
\]

Operator-norm continuity then gives \(B(s)^*\delta_a^{(2)}(s)/s\to T^*U_a\). For a fixed \(X\in L^2\) and uniformly bounded \(b_s\to b_0\) in probability, \(\|(b_s-b_0)X\|_2\to0\): truncate \(X\) at a fixed magnitude, use bounded convergence in probability on the truncated part, and then send the \(L^2\) tail to zero. This justifies the last gate multiplication even though \(T^*U_a\) is unbounded. Consequently

\[
\frac{A'(s)}s\to A''(0)=\frac12\sum_ad_aT^*U_a\,u_a,
\qquad A(s)=A_0+\frac{s^2}{2}A''(0)+o_{L^2}(s^2).
\]

The corresponding memories obey \(Q_a(s)=s^2U_a/4+o_{L^2}(s^2)\). The inequality \(\|u\otimes v\|_{\rm op}\le\|u\|_2\|v\|_2\), together with \(P_a(s)\to H_a\), yields

\[
B(s)=T+\frac{s^2}{4}\sum_aU_a\otimes H_a+o_{\rm op}(s^2).
\]

Thus \(B''(0)=\frac12\sum_aU_a\otimes H_a\), and the next forward acceleration in mixing lines 269–270 is correctly

\[
z_a''(0)=\frac12\sum_bC_{ba}U_b+T[d_a a_a''(0)].
\]

For moment second derivatives, use also \(A'(s)=sA''(0)+o_{L^2}(s)\), not merely a Peano expansion. Then differentiating \(\mathbb E S(s)^2\) once in \(L^2\) and taking its derivative at zero proves the displayed classical right second derivative. The same integral-equation reasoning supplies the needed initial derivatives of the gates.

## The first reverse law is canonical for the initialized computation

Let \(H=(H_1,H_2)^\top\), \(Z=TH\sim N(0,C)\), \(U_a(Z)=g_+(Z)k_a(Z)\), and \(R_a=T^*U_a\). The claimed law is

\[
R=MH+\Xi,\qquad M_{ab}=\mathbb E\partial_bU_a(Z),\qquad
\Xi\sim N(0,\Sigma),\quad\Sigma_{ab}=\mathbb E[U_aU_b],
\]

with \(\Xi\) independent of the entire first-layer Gaussian root \(A_0\).

The exact conditioning identity in `docs/02-gaussian-reuse.qmd` 108–169 supports this law, but its finite identity must be passed to the population. The following specializes and completes that step without importing another source theorem.

For this fixed initialized computation only, let \(V\) have rows \(H(A_{0,i})^\top\), let \(Y=WV\), and let the two columns of \(\mathcal U\) be \(U_a(Y_i)\). Conditional on the root rows, the rows of \(Y\) are iid \(N(0,C_n)\), where \(C_n=V^\top V/n\). Gaussian conditioning on \(WV=Y\) gives the joint reverse answer matrix

\[
W^\top\mathcal U
\overset d=
V C_n^{-1}B_n+(I-P_V)\Gamma\Sigma_n^{1/2},
\quad
B_n=Y^\top\mathcal U/n,\quad
\Sigma_n=\mathcal U^\top\mathcal U/n.
\]

Here \(P_V\) projects onto the two forward input columns, and \(\Gamma\) is an \(n\times2\) matrix of independent standard Gaussians, independent of the recorded roots and forward answers. This is exactly the transpose of the cited one-direction conditional identity; no previous reverse constraint exists yet. The covariance is the full source second moment \(\Sigma_n\). There is no subtraction of the projection of \(U\) onto \(Z\).

The ordinary iid law of large numbers gives \(C_n\to C\). Since \(C\) is positive definite, the inverses converge. Conditional on \(C_n\), averages of bounded continuous functions \(U_aU_b\), and of \(Y_jU_a(Y)\), converge to their Gaussian expectations. For the latter, conditional variances are bounded by a constant times the Gaussian second moments; for the former the summands are bounded. Gaussian representations using \(C_n^{1/2}N\) justify continuity of the expectations. Hence \(B_n\to B=\mathbb E[ZU^\top]\) and \(\Sigma_n\to\Sigma\).

The input projection disappears in empirical mean square: conditionally,

\[
\mathbb E\left[\frac1n
 \|P_V\Gamma\Sigma_n^{1/2}\|_F^2\;\middle|\;V,Y\right]
=\frac{\operatorname{rank}(P_V)}n\operatorname{tr}\Sigma_n\longrightarrow0.
\]

All entries of \(U\) are bounded, so the convergence is uniform for this estimate. Convergence of the covariance square roots and ordinary iid averages of the pairs \((A_{0,i},\Gamma_i)\) then give the joint population law with an innovation independent of \(A_0\). The deterministic response is \(H^\top C^{-1}B_{\cdot a}\).

Finally Gaussian integration by parts, valid because \(U\) and its first derivatives are bounded, gives \(B_{ja}=\sum_bC_{jb}\mathbb E\partial_bU_a\). Thus the response is precisely \(\sum_bM_{ab}H_b\). This proves the canonical first-computation statement represented in mixing (2)–(4), conditional only on using the stated generated initialized operator. It makes no claim about a width-dependent number of calls or a trained trajectory limit.

For comparison, define the bounded rank-two operator

\[
T_0f=Z^\top C^{-1}\mathbb E_1[Hf].
\]

It has \(T_0H_a=Z_a\) and a true adjoint, but \(T_0^*U_a=\sum_bM_{ab}H_b\), with no innovation. Thus an initial forward Gaussian law plus abstract adjunction is insufficient. This is why the explicit generated-law condition in the candidates must not be dropped. The counterexample concerns an inadmissible replacement of the initialized source, not the canonical construction.

## Drift, covariance, and strict correlation signs

Differentiating \(U_a=g_+k_a\) gives, with \(k_a=1-g_a^2\),

\[
\partial_bU_a=\tfrac12k_ak_b
 -2\mathbf1_{a=b}g_+g_ak_a.
\]

Exchangeability therefore gives

\[
M=\begin{pmatrix}m&n\\n&m\end{pmatrix},\quad
n=\tfrac12\mathbb E[k_1k_2]>0,\qquad
\Sigma=\begin{pmatrix}\sigma&\eta\\\eta&\sigma\end{pmatrix}.
\]

The full-support nondegenerate Gaussian pair implies \(\eta=\mathbb E[g_+^2k_1k_2]>0\), since \(g_+=0\) only on \(Z_1+Z_2=0\). Further,

\[
\sigma-\eta=\tfrac12\mathbb E[g_+^2(k_1-k_2)^2]>0.
\]

The integrand is positive on a nonempty open set. Thus \(\Sigma\) is strictly positive definite, including when the signed inputs are negatively correlated.

Set \(D=\operatorname{diag}(d_1,d_2)\), \(G_{aa}=1\), \(G_{12}=G_{21}=c\). The conditional law follows directly from the affine Gaussian representation:

\[
a''=\tfrac12GD(MH+\Xi),\quad
\mathbb E[a''\mid A_0]=\tfrac12GDMH,\quad
\operatorname{Cov}(a''\mid A_0)=\tfrac14GD\Sigma DG.
\]

It is positive definite almost surely because \(G,D,\Sigma\) are invertible. Its off-diagonal entry is

\[
\tfrac14\{c\sigma(d_1^2+d_2^2)+(1+c^2)\eta d_1d_2\}.
\]

This is strictly positive for \(c\ge0\). No fixed off-diagonal sign for \(c<0\) is asserted or implied. The vector-weight covariance is correctly supported on the two-dimensional training span. A fresh independent reverse source deletes the mean term and violates adjunction for these source fields; retaining only the mean deletes a positive covariance; independent innovations across samples delete \(\eta>0\). All three comparisons in mixing lines 248–263 are valid.

For \(\lambda_\pm=m\pm n\), integration by parts and exchangeability give

\[
(v+\kappa)\lambda_+
=\tfrac12\mathbb E[(Z_1+Z_2)g_+(k_1+k_2)]>0,
\]

because \(\tanh Z_1+\tanh Z_2\) has the sign of \(Z_1+Z_2\). Likewise,

\[
(v-\kappa)\lambda_-
=\tfrac12\mathbb E[(Z_1-Z_2)(U_1-U_2)]
=-\mathbb E[(Z_1-Z_2)g_+^2(g_1-g_2)]<0.
\]

Strictness uses nondegeneracy and strict monotonicity of tanh. Thus \(\lambda_+>0\) and \(\lambda_-<0\) for every fixed \(c\in(-1,1)\). The denominators \(v\pm\kappa\) are positive, with no omitted covariance factor.

Writing \(S_\pm=a_1\pm a_2\), expand \(MH\) into its two eigenchannels and use \(d_1-d_2=-(H_1-H_2)(H_1+H_2)\). This gives exactly

\[
\mathbb E[S_+''\mid A_0]
=\tfrac{1+c}{4}(H_1+H_2)
 [\lambda_+(d_1+d_2)-\lambda_-(H_1-H_2)^2],
\]

\[
\mathbb E[S_-''\mid A_0]
=\tfrac{1-c}{4}(H_1-H_2)
 [\lambda_-(d_1+d_2)-\lambda_+(H_1+H_2)^2].
\]

The brackets have respectively positive and negative signs. Tanh monotonicity and oddness identify the signs of \(H_1\pm H_2\) with those of \(S_\pm\). The exceptional zero lines have probability zero. Therefore, for \(V_\pm(s)=\mathbb E S_\pm(s)^2\),

\[
V_\pm'(0)=0,\qquad
V_+''(0)=2\mathbb E[S_+S_+'']>0,\qquad
V_-''(0)=2\mathbb E[S_-S_-'']<0.
\]

The innovations disappear from these expectations by their zero conditional mean; they remain present in the conditional acceleration law. The normalization \(a(s)=a_0+s^2a''(0)/2+o(s^2)\) supplies exactly the factor 2 above.

When preactivations are centered and exchangeable, Pearson correlation is

\[
r(s)=\frac{V_+(s)-V_-(s)}{V_+(s)+V_-(s)},\quad
r''(0)=\frac{(1-c)V_+''(0)-(1+c)V_-''(0)}4>0.
\]

Here \(V_\pm(0)=2(1\pm c)\). This proves \(r(s)>c\) for sufficiently small positive \(s\), and the raw cross moment has second derivative \((V_+''-V_-'')/4>0\). Since \(s(t)=2t+o(t)\) and the observables' first derivatives vanish, their physical-time curvatures are four times these values. None of this proves later monotonicity or a sign for every realized acceleration.

**Centering qualification.** At fixed data, the transformation

\[
(A,W,V_a,K_a)\mapsto(-A,-W,-V_a,-K_a),\qquad T,\tau\text{ unchanged},
\]

leaves \(B\) and all predictions unchanged, flips \(H,G,D,L\), and transports every physical-time equation to itself. Invariance of the complete initialized law under \(A_0\mapsto-A_0\), together with uniqueness and deterministic scalar expectations, therefore gives a sign-symmetric first-layer law and exact centering. This follows from the symmetry candidate's full Hypotheses 1–2, but it does **not** follow from sample swapping alone. The mixing note's “symmetric trajectory” should retain this meaning if its exact expression for correlation is used away from zero.

Even without global centering, its initialized jet has \(\mathbb E a''=0\): under \((A_0,\Xi)\mapsto(-A_0,-\Xi)\), its law is invariant and the acceleration changes sign. Hence \(\mathbb E a(s)=o(s^2)\). Exchangeability of the initial jet also gives \(\mathbb E a_1(s)^2-\mathbb E a_2(s)^2=o(s^2)\). Subtracting the squared means and using the geometric mean of the two variances changes the correlation formula by \(o(s^2)\), so the strict initial Pearson-correlation curvature survives. This qualification does not invalidate the startup mechanism.

## Symmetry normal form, both memories, and the initial query sign

The binary sign gauge is exact. Under \(p_a=y_au_a\), \(K_a\mapsto y_aK_a\), \(V_a\mapsto y_aV_a\), the memory operator is unchanged; the feature and output signs follow from oddness, while the derivatives are even. Residuals become \(e_a=y_ar_a\), and each physical-time equation, including the clock, transforms correctly. Equal signed norms and deterministic orthogonal/sample equivariance then give equal signed predictions and \(r_a=y_ae\).

For \(-1<c<1\), the orthonormal directions proportional to \(p_1+p_2\) and \(p_1-p_2\) give query coordinates \((\alpha,\beta,z)\). The stabilizer of the training span makes the dependence on \(z\) radial. Sample interchange negates \(\beta\) and preserves the predictor. Network oddness under query negation then forces oddness in \(\alpha\), so \(F_t=\Phi_t(\alpha,\beta,\|z\|)\) with the asserted parities and \(F_t=0\) on \(\alpha=0\). In dimension two only radius zero is available; in dimension one only the endpoint geometries occur.

The factorization \(F_t=\alpha\Psi_t(\alpha^2,\beta^2,\|z\|^2)\) needs only \(C^1\) regularity to make \(\Psi_t\) continuous: the integral of \(\partial_\alpha\Phi_t(\theta\alpha,\beta,s)\) over \(0\le\theta\le1\) supplies the value and continuity at \(\alpha=0\); composition with square roots is continuous on the nonnegative arguments. No differentiability of \(\Psi_t\) in its squared arguments is claimed. Vanishing tangent derivatives imply the gradient statement. The pointwise endpoint passage for the symmetry equalities is correct; the extra regularity of any factorized limit remains explicitly assumed.

The bounded smooth examples \(F_{\rm base}\) and \(F_\lambda\) have the asserted interpolation, parity, and additional zero planes. They correctly disprove an inference from symmetry and interpolation alone. They are not claimed to be reachable trajectories. At \(c=1\) the memories coalesce and there is no minus channel. At \(c=-1\), the displayed arrested state satisfies every equation with \(\tau=1+t\); uniqueness selects it. These degeneracies cannot be inserted into the strict nondegenerate rank or covariance conclusions.

The half-sum/half-difference factors in symmetry (4)–(10) are correct. In particular the original factor \(1/2\) multiplying two memory terms becomes one in each channel. The full-state sample-swap covariance makes deterministic scalar inner products of a plus and minus channel zero. Predictor equivariance alone is insufficient, as the candidate explicitly states. Applying the same adjoint and using these cross-inner-product cancellations gives its formulas for \(P_\pm,L_\pm\). The nonlinear gate identities contain both channels and do not give a scalar feature closure.

For the rank claim, put \(q_0=1-g_{+,0}^2-g_{-,0}^2=(k_{1,0}+k_{2,0})/2>0\). Initial physical-time equations yield

\[
W(t)/t\to2g_{+,0},\quad
D_+(t)/t\to2g_{+,0}q_0,\quad
D_-(t)/t\to-4g_{+,0}^2g_{-,0}.
\]

Integrating \(\dot v_\pm=-2eD_\pm\) gives exactly

\[
v_+(t)=2t^2g_{+,0}q_0+o_{L^2}(t^2),\qquad
v_-(t)=-4t^2g_{+,0}^2g_{-,0}+o_{L^2}(t^2).
\]

Both leading \(L^2\) norms are positive by the initialized Gaussian full support; both initial key norms are positive. Their nonzeroness persists on a single sufficiently short interval by the norm expansions and continuity. Plus and minus keys, and plus and minus values, are orthogonal by full scalar-state symmetry. The operator \(B-T=v_+\otimes k_++v_-\otimes k_-\) therefore has rank exactly two throughout that interval. No second-order differentiability of an entire nonlinear Nemytskii map is needed for this argument.

The initial query sign proof also checks. For a Gaussian pair with fixed positive variances \(v,w\), covariance \(b\), and tanh product expectation \(J_{v,w}(b)\), differentiating the explicit density gives \(\partial_b\varphi_b=\partial_x\partial_y\varphi_b\). There is no factor \(1/2\): varying one covariance parameter varies both off-diagonal entries. Gaussian domination in an interior covariance neighborhood and two integrations by parts give

\[
J'_{v,w}(b)=\mathbb E[\operatorname{sech}^2X\operatorname{sech}^2Y]>0.
\]

Bounded convergence using two independent standard normals proves continuity at the covariance endpoints; interior strict monotonicity then extends to the entire closed admissible interval. The two-layer initial kernel \(k_R\) is therefore odd and strictly increasing for every query norm \(R>0\). Its outer covariance is admissible by Cauchy–Schwarz; endpoint degeneracy is covered by the continuity argument.

Since \(W_0=0\), \(W(t)/t\to G_{1,0}+G_{2,0}\), and query features are \(L^2\)-continuous, the readout quotient directly gives

\[
\dot F_0(q)=k_R(p_1\cdot q)+k_R(p_2\cdot q).
\]

No derivative of the query feature is needed here. If \(\alpha>0\), its first argument exceeds the negative of its second; oddness and strict monotonicity give a positive sum. The other signs follow similarly, with \(q=0\) treated separately. The sign is exactly that of \((p_1+p_2)\cdot q\), including the coincident signed-input case and the identically zero antipodal case. The positivity \(\dot f(0)=2\|g_{+,0}\|_2^2>0\) is also correct. Continuity of the initial quotient gives a positive sign interval for each fixed off-plane query; it does not give a uniform interval over near-plane or unbounded queries.

## Complete coverage and claim status

| Candidate lines | Assertions checked | Outcome |
|---|---|---|
| Mixing 1–67 | Model, initialized covariances, strict nondegeneracy, clock, existence boundary | Correct with the strong-solution and parity meanings above |
| Mixing 68–130 | q=1 equations, first accelerations, \(L^2\)/operator jets and factors | Conditional PASS |
| Mixing 132–215 | Reused reverse law, adjunction, derivative coefficients, innovation covariance | PASS for the canonical initialized finite computation; population passage supplied above |
| Mixing 216–277 | Conditional Gaussian law, covariance, failed independence replacements, next source reuse | PASS; no general no-go theorem inferred |
| Mixing 279–381 | Response eigenvalue signs, mode curvature, correlation, physical clock | Conditional PASS; centering qualification recorded |
| Mixing 383–412 | Claim limits, provenance, open bridges | Correct; all provenance hashes match |
| Symmetry 1–50 | Explicit flow, integrability, symmetry and initial-Gaussian hypotheses | Correct conditional setup; no existence identification obtained |
| Symmetry 52–100 | Gauge and synchronization | Conditional PASS |
| Symmetry 102–201 | Query normal form, \(C^1\) factorization, endpoint passage, sharpness and degeneracies | Conditional PASS |
| Symmetry 203–278 | Two-channel equations, orthogonality, nonlinear coupling and adjoint reuse | Conditional PASS under full scalar-state covariance |
| Symmetry 280–320 | Initial expansions, nonzero coefficients and exact rank two | Conditional PASS |
| Symmetry 322–393 | Gaussian covariance derivative, query kernel, exact initial sign, training velocity | Conditional PASS |
| Symmetry 395–412 | Claim separation and limits | Correct; no promotion or all-time sign conclusion |

These findings leave the fixed-order population existence/uniqueness and trained-width identification bridge open. They also leave global fitting, endpoint existence, later-time query positivity, arbitrary-accuracy finite law-only closure, and q-dependent approximation claims open. The two notes may be used together as conditional startup results for the specified canonical source and assumed strong flow, with the centering and regularity qualifications retained. No frozen candidate was changed by this check.
