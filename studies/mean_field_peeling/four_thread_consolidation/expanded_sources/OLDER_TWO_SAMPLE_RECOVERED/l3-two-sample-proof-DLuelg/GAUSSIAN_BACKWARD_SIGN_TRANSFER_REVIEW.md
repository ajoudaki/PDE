# Independent adversarial audit: Gaussian backward sign transfer

Date: 2026-09-06.

**Verdict: scalar transfer and strict indefinite cone PASS; the assertion of an actual joint initial matrix law through both transposes REQUIRES PROOF COMPLETION as written.** No sign error, missing transpose correction, or counterexample to the intended equal-width initial law was found. Conditioning on the independent third matrix at the second transpose is legitimate. The outstanding issue is the passage from that finite conditional identity to the required joint empirical law and, especially, its unbounded-input second and mixed moments. The candidate outlines this passage but does not establish it at its advertised self-contained proof level.

This is a proof-completeness finding, not a claim that (6) or (7) is false. Section 5 below supplies an explicit finite-model reconstruction that closes the mathematical gap under stated equal-width assumptions. Those assumptions and that argument are additions in this review; they should not be silently attributed to the submitted candidate. No global trained-law theorem is being requested or evaluated.

## Audit boundary and hashes

The only mathematical inputs read were:

- `GAUSSIAN_BACKWARD_SIGN_TRANSFER.md`, all 214 lines.
- `GAUSSIAN_INITIAL_SIGNED_RESPONSE.md`, lines 1–315: introductory material and Sections 1–4. Its Section 5 was not read. The static-initial versus zero-delta distinction can be checked directly, without its source-slot program.

Both files are in `/tmp/l3-two-sample-proof-DLuelg`. No other reviews, ledgers, project mathematics, or task history were consulted. No agents, experiments, or candidate edits were used. The finite-array calculations below are analytic deductions from the permitted inputs, with any additional finite-model assumptions explicitly identified.

SHA-256:

```text
c37ffe3035b080bab0e0e79f94e45926e882c58239c370df25d90295a7173652
  GAUSSIAN_BACKWARD_SIGN_TRANSFER.md

05708450c2896f62e9ec39beeb67c9b9d1e804ba37a96fa8e342d6cd3692e1f1
  GAUSSIAN_INITIAL_SIGNED_RESPONSE.md (whole-file identity only)

9467e7031ad054239bece6a80b4ee3d7a8270e57f7d2887bafb774baf2370c08
  GAUSSIAN_INITIAL_SIGNED_RESPONSE.md, exact first 315 lines

9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7
  /etc/codex/skills/solve-math-rigorously/SKILL.md
```

The procedural skill was read in full by the reviewer. Computing the whole dependency's hash did not expose or use its Section 5 as mathematical input. References below use the candidate's original line numbers unless explicitly marked as dependency references.

## 1. Scalar identities, exact transfer, and every endpoint

### 1.1 Integral identities: PASS

The dependency's Sections 1–3 justify the identities used in candidate lines 18–42, including the endpoints. With

\[
w_q(u,v)=e^{-u-v-q(u^2+v^2)/2},\qquad u,v>0,
\]

the identities are

\[
B_q(t)=\iint w_q\cosh(tuv),\qquad
J_q(t)=\frac12\iint (u/v+v/u)w_q\sinh(tuv).
\]

For the curvature integral, the apparent singularity at an integration axis is harmless: the unsymmetrized absolute expectation is bounded by
\(qu^2e^{-u-v}\), using
\(\mathbb E|\sin(uX)\sin(vY)|\le uvq\).
For \(|t|\le q\),
\(e^{-q(u^2+v^2)/2+|t|uv}\le1\). The differentiated integrands are consequently bounded by integrable polynomial multiples of \(e^{-u-v}\). This justifies exchanges, continuity, and one-sided parameter derivatives at both singular endpoints.

In particular, \(B_q\) is even and positive; \(J_q\) is odd with

\[
J_q'(t)=\frac12\iint (u^2+v^2)w_q\cosh(tuv)>0.
\]

There is no sign assumption on \(t\). The integration-by-parts calculation

\[
D_q=\mathbb E[(f h)'(Z)]
=q^{-1}\mathbb E[Z\arctan(Z)/(1+Z^2)]>0
\]

has bounded integrand derivative and a vanishing Gaussian boundary term; strict positivity uses \(q>0\). Finally,

\[
T_q'(t)=-\frac14\iint w_q
\{(u-v)^2e^{tuv}+(u+v)^2e^{-tuv}\}<0.
\]

The second term is strictly positive throughout the integration domain, so this is strict even when \(t=\pm q\) in the one-sided sense. Thus

\[
T_q(q)=D_q>0,\qquad T_q(t)>D_q\quad(-q\le t<q).
\]

No denominator \(q-c\) or \(q+c\) has been introduced. The variance-zero case is outside the claim and cannot inherit its strict conclusions.

### 1.2 Transfer (3): PASS, including all factors and indices

Let \(a,b\in\{1,2\}\). Differentiate in the ambient two coordinates with \(C\) and the realized independent source fixed:

\[
\partial_b D_a
=\mathbf1_{a=b}\phi''(Z_a)
  \left(\zeta_a+\sum_j C_{aj}\phi(Z_j)\right)
 +\phi'(Z_a)C_{ab}\phi'(Z_b).
\]

Independence and centering give
\(\mathbb E[\phi''(Z_a)\zeta_a]=0\). Oddness removes the constant part of \(\phi\), and

\[
\mathbb E[\phi''(Z_a)\phi(Z_j)]
=\begin{cases}
-\varepsilon^2J_q(q),&j=a,\\
-\varepsilon^2J_q(c),&j\ne a.
\end{cases}
\]

Because \(C=YM\) and \(Y^2=I\), the multiplier is
\(y_aC_{aj}=M_{aj}\), with no extra \(y_j\). Therefore

\[
N_{aa}=\varepsilon^2\{mB_q(q)-mJ_q(q)-bJ_q(c)\},
\qquad N_{a,3-a}=\varepsilon^2bB_q(c).
\]

This is exactly (3). There is no missing factor of two. The factor \(1/2\) in the top readout velocity belongs to the initial seed \(M^{(3)}\), not to this general transfer. Singular source covariance causes no difficulty.

### 1.3 Eigenvalue transfer (4) and cone (5): PASS

Write \(D=D_q\), \(B=B_q(c)\), \(J=J_q(c)\). Directly from (3),

\[
\nu_y=\varepsilon^2(Dm-Jb+\sigma Bb),\qquad
\nu_\perp=\varepsilon^2(Dm-Jb-\sigma Bb).
\]

Substituting \(m=(\lambda_y+\lambda_\perp)/2\) and
\(b=\sigma(\lambda_y-\lambda_\perp)/2\), and using
\(T_q(\sigma c)=B-\sigma J\), gives exactly both lines of (4), including the argument \(-\sigma c\) in the second line.

For \(\lambda_y>0>\lambda_\perp\), each \(D+T\) coefficient is positive and each \(D-T\) coefficient is nonpositive. The first transformed eigenvalue has a strictly positive term plus a nonnegative term; the second has a strictly negative term plus a nonpositive term. This proves strict preservation of the stated open cone. In \((m,b)\) coordinates that cone is \(\sigma b>|m|\).

For an explicit endpoint check, put \(A=B_q(q)\), \(J_*=J_q(q)>0\), so \(D=A-J_*\) and \(T_q(-q)=A+J_*\). Both physical endpoints and both label choices are covered by:

| Endpoint in label coordinates | \(\nu_y/\varepsilon^2\) | \(\nu_\perp/\varepsilon^2\) |
|---|---|---|
| \(\sigma c=q\) | \(D\lambda_y\) | \(-J_*\lambda_y+A\lambda_\perp\) |
| \(\sigma c=-q\) | \(A\lambda_y-J_*\lambda_\perp\) | \(D\lambda_\perp\) |

The signs remain strict for an input in the open cone. If an input eigenvalue is zero, the corresponding endpoint can preserve zero; the candidate does not claim strictness on that boundary. At \(c=0\), \(J_q(0)=0\) and \(B_q(0)>D_q\), consistent with the same proof.

The qualification about positive semidefiniteness is correct. For example, taking \(M\) to be the all-ones matrix and \(c=q\) gives transformed eigenvalues \(2\varepsilon^2D_q\) and \(-2\varepsilon^2J_q(q)\). Thus the linear map does not preserve the positive-semidefinite cone.

## 2. Initial seed and admissible covariance domain

The dependency's Sections 2–4 provide a valid seed; it is not enough merely to know the diagonal curvature is negative. From the complete top expression,

\[
\partial_b U^{(3)}_a
=\frac{y_b}{2}\phi'(Z^{(3)}_a)\phi'(Z^{(3)}_b)
 +\mathbf1_{a=b}V_0\phi''(Z^{(3)}_a).
\]

Consequently, at top variance and covariance \((q_3,c_3)\),

\[
M^{(3)}=\frac{\varepsilon^2}{2}
\begin{pmatrix}
D_{q_3}-\sigma J_{q_3}(c_3)&\sigma B_{q_3}(c_3)\\
\sigma B_{q_3}(c_3)&D_{q_3}-\sigma J_{q_3}(c_3)
\end{pmatrix}.
\]

Its eigenvalues are

\[
\lambda_y=\frac{\varepsilon^2}{2}
 [D_{q_3}+T_{q_3}(\sigma c_3)],\qquad
\lambda_\perp=\frac{\varepsilon^2}{2}
 [D_{q_3}-T_{q_3}(-\sigma c_3)].
\]

For completeness, the dependency's seed endpoints also check out. For a generic variance \(q>0\), let \(A=B_q(q)\), \(J_*=J_q(q)\), and \(D=A-J_*\). The signed diagonal curvature is
\(K_\sigma=-\varepsilon^2[J_*+\sigma J_q(c)]/2\). The complete endpoint classification is:

| Seed covariance and labels | \(\lambda_y/\varepsilon^2\) | \(\lambda_\perp/\varepsilon^2\) | \(K_\sigma/\varepsilon^2\) |
|---|---|---|---|
| \(c=-q,\sigma=+1\) | \(A\) | \(0\) | \(0\) |
| \(c=-q,\sigma=-1\) | \(D\) | \(-J_*\) | \(-J_*\) |
| \(c=q,\sigma=+1\) | \(D\) | \(-J_*\) | \(-J_*\) |
| \(c=q,\sigma=-1\) | \(A\) | \(0\) | \(0\) |

In the open interval, both curvatures are strictly negative and the seed is indefinite in both modes. At \(q=0\), outside the stated domain, the direct calculation instead gives zero curvature and \(M=\varepsilon^2yy^T/2\). These checks confirm the dependency's exceptions rather than extending a strict claim through them.

The dependency's integral for \(F_s\), its derivative \(F_s'=B_s>0\), and its covariance recursion are justified by the same integrable bounds. For a fixed root correlation \(\rho\in[-1,1)\), they give

\[
0<c_2<q_2,\qquad 1<c_3<q_3<1+\pi^2/400.
\]

In particular, both seed eigenvalues have the required strict signs, and Section 2 must then be applied with the *layer-two* parameters \((q_2,c_2)\), keeping this seed matrix fixed.

At the antiparallel root, \(H^{(1)}=(1+\varepsilon f(G),1-\varepsilon f(G))\). A linear relation between these two random variables would require

\[
(a+b)+\varepsilon(a-b)f(G)=0\quad\text{almost surely}.
\]

Since \(f(G)\) is nonconstant, this forces \(a=b=0\). Thus the first feature **second-moment** matrix is positive definite even though the root covariance is singular. Later Gaussian pairs are nondegenerate, and their strictly monotone features have positive-definite second-moment matrices as well. This supports the inversions used in the finite proof for fixed admissible inputs; it does not give a uniform inverse bound as \(\rho\uparrow1\).

The excluded coincident-input case \(\rho=1\) must remain excluded from the strict actual-seed statement. Algebraic validity of the scalar transfer at \(c=\pm q\) does not extend an inverse-Gram matrix argument through a singular feature Gram. At \(c=q,\sigma=-1\), for example, the top reverse input vanishes on its Gaussian support although its ambient derivative matrix need not vanish. Support identities cannot be used to redefine those derivatives, nor do they give uniqueness of a regression coefficient at a singular Gram.

## 3. Derivative convention and the meaning of initialization

**Fixed-coefficient convention: PASS.** When computing \(C^{(2)}\), the attained deterministic \(C^{(3)}\), the limiting forward covariance, and the source covariance are constants. For each realized independent \(\zeta^{(2)}\), the derivative is taken only through

\[
U^{(2)}_a(z,\zeta^{(2)})
=\phi'(z_a)\left[\zeta^{(2)}_a+
             \sum_j C^{(3)}_{aj}\phi(z_j)\right].
\]

One must not differentiate how \(C^{(3)}\) or the law of \(\zeta^{(2)}\) would change under a change in the forward distribution. Conversely, one must differentiate the entire displayed feature dependence, including the diagonal \(\phi''Q\) term. The source is held fixed, not set to zero. Its covariance affects the next reverse-input second moment even though it disappears from this expected derivative.

The required derivative is integrable: its absolute value is bounded by a constant times \(1+|\zeta^{(2)}_a|\). Conditional on the source, Gaussian integration by parts is valid with this bound and a vanishing boundary term. It is an identity for the limiting scalar function. It does **not**, by itself, assert convergence of derivatives of the finite random network. Such derivative convergence is unnecessary for (7); the mixed moment in Section 5 is sufficient.

**Zero deltas versus the static velocity query: PASS with the stated zero-readout interpretation.** If \(a_0=0\) and \(\dot a_0=V_0\), the ordinary top hidden delta \(a_t\phi'(Z^{(3)}_t)\) is zero at time zero, while its derivative there is \(V_0\phi'(Z^{(3)}_0)=U^{(3)}\). Differentiating a transpose product gives

\[
\left.\frac{d}{dt}(W^{(3)}_t)^T\delta^{(3)}_t\right|_0
=(W^{(3)}_0)^TU^{(3)},
\]

because the term containing \(\dot W^{(3)}_0\) multiplies the zero initial delta. The next gate and transpose give \(U^{(2)}\) and \((W^{(2)}_0)^TU^{(2)}\) in the same way. This explains the static initial query without making it a nonzero ordinary initial delta. Identifying \(V_0\) with a particular training velocity presupposes the readout convention stated in the candidate; the permitted inputs do not specify an additional finite training dynamics.

This initial tangent calculation neither identifies separate historical/current source-slot derivatives nor proves a causal time-response theorem. Candidate lines 163–165 are an ancillary scope statement, not an ingredient needed for the static proof. Their detailed time-mesh bookkeeping is not certified here, and no conclusion from the dependency's unread Section 5 is imported. Candidate Section 4 appropriately disclaims positive-time cone propagation, contraction, kernel monotonicity, and global continuation.

## 4. Required repairs to the actual matrix-law assertion

### R1. State the finite model, normalization, and meaning of “joint law”

Lines 122–127 and 138–154 refer to “usual” Gaussian laws and empirical limits without a finite array definition or a convergence mode. Within the permitted mathematical inputs, there is no explicit statement that both hidden matrices have independent \(N(0,1/n)\) entries, that their row and column widths have ratio one, or what class of empirical observables the joint assertion includes.

This normalization is substantive. For an \(m\)-by-\(n\) matrix with entry variance \(1/n\), a transpose residual has covariance

\[
\frac1nU^TU=\frac mn\left(\frac1mU^TU\right),
\]

and the limiting mean coefficient acquires the same aspect-ratio factor \(m/n\) under otherwise identical definitions. Equations (6)–(7) as printed are the ratio-one formulas. This is not a counterexample to an intended equal-width model, but that model needs to be stated locally.

A sufficient contract is the equal-width construction in Section 5, with joint empirical convergence in probability within each neuron population, plus convergence of the second and mixed moments used by the next transpose. Separate populations can have their empirical assertions hold jointly; no identification of unrelated neuron indices across layers or finite-coordinate iid claim is needed. Almost-sure convergence or unconditional mean-square convergence would require additional estimates beyond the argument supplied here.

### R2. Prove the two empirical moment limits needed at the second transpose

The main omission is at lines 149–154 and 183–191. The candidate must establish, for the **finite** reused-matrix reverse input,

\[
\frac1n(Z^{(2)})^TU^{(2)}
 \longrightarrow \mathbb E[Z^{(2)}(U^{(2)})^T],\qquad
\frac1n(U^{(2)})^TU^{(2)}
 \longrightarrow \mathbb E[U^{(2)}(U^{(2)})^T].
\tag{R}
\]

Merely identifying a limiting Gaussian-plus-shift scalar variable, with finite moments, does not imply these empirical convergences. For example, the deterministic array \((\sqrt n,0,\ldots,0)\) has empirical weak limit zero but empirical second moment one. This is a logical illustration of the missing implication, not an example from this network.

Nor does small projection rank alone establish a negligible normalized error. Conditional on the exposed data, the correct bound is

\[
\mathbb E\left[\frac1n\|\Pi_H G\|_F^2\,
       \middle|\,\text{exposed data}\right]
=\frac{\operatorname{rank}(\Pi_H)}n
       \operatorname{tr}\left(\frac1nU^TU\right).
\tag{P}
\]

At the first transpose, boundedness of \(U^{(3)}\) closes this bound. At the second, tightness of the displayed empirical reverse-input second moment must first be proved; it cannot be supplied by the limiting representation whose justification is in progress.

The sentence about truncation in \(L^2\) should therefore either be replaced by the direct moment calculation below or supported by a uniform finite-array tail bound and an estimate propagating the truncation error through the conditional transpose. The limiting scalar's finite moments alone are insufficient. A proof should also specify the conditioning sigma-field at the second exposure, as below, so that its conditional averaging is visibly legitimate despite reuse of both matrices.

These repairs are limited and local. They do not call for experiments, a general tensor-program theorem, or any trained-path result. They also do not require convergence of finite-network derivatives: after (R), ordinary Gaussian integration by parts for the limiting function identifies the coefficient.

## 5. Explicit finite conditioning and moment argument that closes R2

This section proves the intended law under the following explicit reconstruction of R1. It makes the omitted step reviewable rather than leaving “conditional averaging” as an unverified instruction.

### 5.1 Finite model and forward averages

Let all three hidden widths be \(n\), with \(n\to\infty\). Let the rows of \(Z^1\in\mathbb R^{n\times2}\) be iid centered Gaussian pairs with variance one and fixed correlation \(\rho\in[-1,1)\). Independently let \(W^2,W^3\) have iid \(N(0,1/n)\) entries and be independent of one another. Define entrywise

\[
H^1=\phi(Z^1),\quad Z^2=W^2H^1,\quad H^2=\phi(Z^2),
\quad Z^3=W^3H^2,\quad H^3=\phi(Z^3),
\]

\[
U^3_{ia}=\tfrac12(H^3_{i1}+\sigma H^3_{i2})\phi'(Z^3_{ia}),
\quad Q^2=(W^3)^TU^3,
\quad U^2_{ia}=\phi'(Z^2_{ia})Q^2_{ia},
\quad Q^1=(W^2)^TU^2.
\]

Rows are neurons; the two columns are sample coordinates. Put
\(K_{\ell,n}=(H^\ell)^TH^\ell/n\). Since \(\phi\) is bounded, the root law gives \(K_{1,n}\to K_1\) in probability. Conditional on \(H^1\), rows of \(Z^2\) are iid Gaussian with covariance \(K_{1,n}\). Conditional variances of empirical bounded tests are at most a constant divided by \(n\), and their Gaussian expectations converge as \(K_{1,n}\to K_1\). This gives the layer-two forward law and \(K_{2,n}\to K_2\). The same argument gives the layer-three forward law conditional on \(H^2\).

The argument also covers the forward functions of polynomial growth needed below: bounded feature entries bound the forward covariance uniformly, Gaussian moments bound the conditional variances of those functions, and a common Gaussian representation plus dominated convergence gives continuity of their expectations. In particular, \(\|Z^2\|_F^2/n=O_p(1)\). Here \(O_p(1)\) means bounded in probability, and \(o_p(1)\) means convergence to zero in probability. Both limiting matrices \(K_1,K_2\) are positive definite by Section 2. Their empirical inverses are consequently bounded on events whose probabilities tend to one.

### 5.2 Exact finite transpose identity

Let \(H,Z,U\) have two columns and let \(W\) be an \(n\)-by-\(n\) Gaussian matrix as above. Conditional on an exposure under which \(H,Z\), and \(U\) are known, \(WH=Z\), and the exposure does not reveal any component of \(W\) orthogonal to its two forward input directions, Gaussian conditioning gives

\[
W=Z(H^TH)^{-1}H^T+\widetilde W(I-\Pi_H),
\quad \Pi_H=H(H^TH)^{-1}H^T.
\]

The residual \(\widetilde W\) has independent original-variance Gaussian entries and is independent of the exposure. To see the independence directly, project each Gaussian row onto \(\operatorname{span}(H)\) and its orthogonal complement. Their cross covariance is zero; their joint Gaussian density, or characteristic function in the singular case, factors. Rows remain independent.

Set

\[
K_n=H^TH/n,\quad T_n=Z^TU/n,\quad S_n=U^TU/n.
\]

Then, in this conditional representation,

\[
W^TU=HK_n^{-1}T_n+(I-\Pi_H)G,
\tag{F}
\]

where rows of \(G=\widetilde W^TU\) are independent centered Gaussian pairs with covariance \(S_n\). This covariance is an uncentered reverse-input second moment, not \(\operatorname{Cov}(U)\). There is no subtraction of a regression covariance. The output-coordinate projection is exactly the one in (P).

### 5.3 First transpose: coefficients, source, and full local tuple

Expose all lower-layer data, including \(Z^2,H^2\), and then \(Z^3=W^3H^2\). The top reverse input \(U^3\) is now known and uniformly bounded. Conditional row averaging yields

\[
T_{3,n}:=(Z^3)^TU^3/n\to T_3:=\mathbb E[Z^3(U^3)^T],
\qquad S_{3,n}:=(U^3)^TU^3/n\to S_3:=\mathbb E[U^3(U^3)^T].
\]

For the first limit, the linear Gaussian factor has bounded conditional second moment; for the second, the summands are bounded. Their conditional variances vanish. All expectations on the right use the deterministic top forward limit.

For clarity about orientation, Gaussian integration by parts gives

\[
(T_3)_{ba}=\sum_k (K_2)_{bk}
  \mathbb E[\partial_k U^3_a]
=\bigl[K_2(C^3)^T\bigr]_{ba}.
\]

Thus \(K_{2,n}^{-1}T_{3,n}\to(C^3)^T\). By (F),

\[
Q^2=H^2K_{2,n}^{-1}T_{3,n}+(I-\Pi_{H^2})G_3,
\qquad (G_3)_{i,:}\mid\text{exposure}\sim N(0,S_{3,n})
\]

with independent rows. Boundedness of \(U^3\) makes \(S_{3,n}\) uniformly bounded, so (P) gives

\[
\frac1{\sqrt n}
\left\|Q^2-\left[H^2(C^3)^T+G_3\right]\right\|_F=o_p(1).
\tag{A}
\]

The coefficient error uses bounded features; the projection error has expected squared normalized norm \(O(1/n)\).

For any bounded Lipschitz test of a complete layer-two row tuple, first use (A) to discard this error. Given the exposure, the remaining Gaussian rows are independent, so the conditional variance of their empirical test average is \(O(1/n)\). Its conditional mean converges by the forward empirical law and \(S_{3,n}\to S_3\). Continuity in the Gaussian covariance holds even if \(S_3\) is singular, by coupling through a common standard Gaussian and its positive-semidefinite square root. This proves the joint empirical law of

\[
(Z^2,H^2,Q^2,U^2)
\quad\text{with}\quad
Q^2_a=\zeta^2_a+\sum_b C^3_{ab}H^2_b,
\quad \zeta^2\sim N(0,S_3)\ \text{independent of }Z^2.
\]

This proves (6) under the finite contract, and retains both sample coordinates and their covariance. No iid assertion about the projected finite coordinates has been made.

### 5.4 The unbounded-input moments needed for the next exposure

Define the unprojected approximation

\[
\widehat Q^2_{ia}=\mu_{ia}+(G_3)_{ia},\qquad
\mu_{ia}=\sum_b C^3_{ab}H^2_{ib},\qquad
d_{ia}=\phi'(Z^2_{ia}),\qquad
\widehat U^2_{ia}=d_{ia}\widehat Q^2_{ia}.
\]

Both \(\mu\) and \(d\) are uniformly bounded. Conditional on the first exposure,

\[
\mathbb E[\widehat U^2_{ia}\widehat U^2_{ib}
                \mid\text{exposure}]
=d_{ia}d_{ib}\{\mu_{ia}\mu_{ib}+(S_{3,n})_{ab}\}.
\tag{B}
\]

Gaussian fourth-moment bounds make the conditional variance of the empirical average on the left \(O(1/n)\). The empirical average of the right side converges by the forward law and \(S_{3,n}\to S_3\). It converges exactly to
\(S_2:=\mathbb E[U^2(U^2)^T]\), with \(U^2\) defined by the just-proved scalar joint law. In particular \(\|\widehat U^2\|_F/\sqrt n=O_p(1)\).

For the mixed moment, the conditional mean is

\[
\mathbb E\left[\frac1n\sum_i Z^2_{ib}\widehat U^2_{ia}
                \middle|\text{exposure}\right]
=\frac1n\sum_i Z^2_{ib}d_{ia}\mu_{ia},
\]

which converges to \(\mathbb E[Z^2_bU^2_a]\) by the forward law. The centered Gaussian part has conditional variance

\[
\frac{(S_{3,n})_{aa}}{n^2}
       \sum_i (Z^2_{ib}d_{ia})^2
\le\frac{C}{n}\left(\frac1n\sum_i (Z^2_{ib})^2\right)
=O_p(1/n).
\tag{C}
\]

The actual reverse input is close enough to transfer both conclusions. Bounded gates and (A) give
\(\|U^2-\widehat U^2\|_F/\sqrt n=o_p(1)\).
For the second moment, use

\[
\left\|\frac{(U^2)^TU^2-(\widehat U^2)^T\widehat U^2}{n}\right\|_F
\le\frac{\|U^2-\widehat U^2\|_F}{\sqrt n}
    \frac{\|U^2\|_F+\|\widehat U^2\|_F}{\sqrt n}=o_p(1).
\]

For the mixed moment, Cauchy–Schwarz gives

\[
\left\|\frac{(Z^2)^T(U^2-\widehat U^2)}n\right\|_F
\le\frac{\|Z^2\|_F}{\sqrt n}
    \frac{\|U^2-\widehat U^2\|_F}{\sqrt n}=o_p(1).
\]

These calculations establish both limits (R) without invoking convergence of empirical unbounded observables from weak convergence alone. They also avoid needing a separate truncation theorem.

If the candidate retains its truncation presentation, the missing finite bound is obtainable: on events where \(K_{2,n}^{-1}T_{3,n}\) is bounded, each conditional row of \(Q^2\) has bounded mean and Gaussian covariance bounded by \(S_{3,n}\). Conditional fourth moments are uniformly bounded there, so \(n^{-1}\sum_i\|U^2_i\|^4=O_p(1)\). Hence empirical squared tails vanish in the iterated limit \(n\to\infty\), then truncation threshold \(R\to\infty\), using \(x^2\mathbf1_{|x|>R}\le x^4/R^2\). Formula (F), Cauchy–Schwarz for its mean, and the residual covariance bound propagate this tail error through the second transpose. This would justify the suggested truncation route at the convergence-in-probability level.

### 5.5 Second transpose and conditioning on the third matrix

Use the exposure

\[
\mathcal F_n=\sigma(Z^1,H^1,Z^2,W^3).
\]

Here \(H^2,Z^3,U^3,Q^2,U^2\) are all measurable: at finite width,

\[
U^2=\phi'(Z^2)\odot
 (W^3)^T u_3\bigl(W^3\phi(Z^2)\bigr),
\]

where \(u_3\) is the rowwise top reverse-input function. Thus the reverse input depends on \(W^2\) only through the already exposed \(Z^2=W^2H^1\).

Because \(W^3\) was initially independent of \((Z^1,W^2)\), adding the entire \(W^3\) to this exposure reveals no component of the \(W^2\) residual orthogonal to \(H^1\). Independence follows from the conditional Gaussian decomposition in Section 5.2 together with this initial independence. It does not follow from an assertion that the reverse input itself is independent of \(W^2\), which would be false. Thus the candidate's conditioning idea is sound.

Applying (F) with this exposure gives

\[
Q^1=H^1K_{1,n}^{-1}T_{2,n}+(I-\Pi_{H^1})G_2,
\quad T_{2,n}=(Z^2)^TU^2/n,
\quad S_{2,n}=(U^2)^TU^2/n,
\]

where conditionally the rows of \(G_2\) are independent \(N(0,S_{2,n})\). Section 5.4 has already proved
\(T_{2,n}\to T_2\) and \(S_{2,n}\to S_2\).
In particular, (P) now tends to zero in probability. Conditional Markov's inequality first on \(\{\operatorname{tr}S_{2,n}\le L\}\), followed by tightness as \(L\to\infty\), justifies discarding this second projection without assuming an unconditional moment bound.

Gaussian integration by parts for the limiting pair \(Z^2\sim N(0,K_1)\), conditional on its independent source, gives

\[
T_2=K_1(C^2)^T,\qquad
C^2_{ab}=\mathbb E[\partial_b U^2_a].
\]

The derivative convention and integrability were checked in Section 3. Therefore
\(K_{1,n}^{-1}T_{2,n}\to(C^2)^T\). Conditional empirical averaging of bounded Lipschitz tests, now including the first-layer root coordinates, proves

\[
Q^1_a=\zeta^1_a+\sum_b C^2_{ab}H^1_b,
\qquad \zeta^1\sim N(0,S_2)
\quad\text{independent of }Z^1.
\]

This is (7) for the **same** initial second matrix. All finitely many population empirical assertions and moment limits above hold jointly in probability by taking a union bound on their exceptional events. There is no additional transpose correction missing from (7) under this contract, and there is no need to assume bounded \(U^2\).

Combining this established coefficient identification with Section 1 gives exactly the claimed strict sign pattern for \(M^2=YC^2\). The proof has not differentiated a distribution-dependent coefficient, replaced a reused matrix by a new matrix, or asserted independence of the finite projected coordinates.

## 6. Required changes versus optional presentation

**Required before an unqualified pass for the candidate's actual-law assertion:**

1. Add the finite normalization and convergence contract in R1, or an equally precise one with any necessary width factors.
2. Add the finite-array empirical moment justification in R2. The bounds (P), (A), (B), and (C), together with the second exposure and coefficient identification, are a sufficient short route. The existing statement that the limiting input is Gaussian plus a bounded shift does not replace these bounds.
3. Make clear that the integration-by-parts coefficient is identified from the limiting mixed moment with deterministic coefficients fixed. If lines 190–191 are meant to claim convergence of finite-network derivatives, either prove that distinct claim or remove it; it is not needed for (7).

**Optional presentation only:**

- Write \((q_2,c_2)\) and \((q_3,c_3)\) explicitly near the application to distinguish the seed's covariance from the transfer's covariance.
- Use “feature second-moment matrix” consistently. It is not the centered covariance of the features; the constant feature component is essential at the antiparallel root.
- “Label-conjugated” means the left weighting \(YC\) here, not the usual two-sided conjugation \(YCY\). The formulas are already consistent.
- The scalar transfer actually needs less than a Gaussian centered source: independence and integrability suffice here because \(\mathbb E\phi''(Z_a)=0\). Retaining the stronger Gaussian centered assumption matches the matrix-law application and is harmless; the word “only” at line 108 should not suggest those assumptions are all necessary.
- The endpoint table above may help readers, but the candidate's existing cone proof already includes those endpoints correctly.
- The source-slot remark can stay as a scope caveat, or be omitted from this static lemma. It should not serve as an unproved substitute for the finite initial-law argument.

The algebra, seed signs, ambient derivative convention, legitimate second conditioning, and restricted initialization scope survive adversarial checking. The advertised actual joint law needs the local proof additions identified above; scalar-algebra PASS alone does not certify that portion of the submitted text.
