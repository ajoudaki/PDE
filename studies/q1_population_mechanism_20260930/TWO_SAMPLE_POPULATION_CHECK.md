# Internal check of the two-sample population analysis

Date: 2026-09-30. Checker: scoped agent `population_theorem_check`.
This is an internal mathematical check, not a promotion review.

**Verdict:** the substantive conditional results pass: the full common energy
increases and the full difference energy decreases in both hidden populations
at order \(s^2\); the second-layer proof correctly includes the reused-source
read-in contribution and its jointly sampled innovations. The clock factors,
cubic training coefficient, adverse lag coefficient, symmetry restrictions,
initial query sign, and conditional endpoint decomposition also check out.
One minor correction is required to the general source class stated before
(9): boundedness and smoothness of a function do not alone imply existence of
the displayed derivative expectations. The actual four sources satisfy the
needed stronger condition, so this correction changes none of the substantive
results. Canonical population existence, trained-width identification, and
global fitting remain open, as the candidate says.

## Inputs, coverage, and provenance

The frozen candidate was read in full, including every scientific line:

- `TWO_SAMPLE_POPULATION_ANALYSIS.md`, lines 1–548, SHA-256
  `70ff598878f21224842e80d91c0e9fd7639a2c48d40bb3a0da9f62fadf0a9599`.
- `docs/02-gaussian-reuse.qmd`, lines 1–170, full-file SHA-256
  `a0f8175c8cd17c4d93aeb7174f2babe83e0917c4ed0f33862c7c9a89685d0a92`;
  exact excerpt SHA-256
  `1da78af8a55e0d00589209fc2137a3bba3f920783da83335cc4999c9a955c64d`.
- `docs/03-local-population.qmd`, lines 174–278, full-file SHA-256
  `3a6fc52191f815189337309f70e3fb822663b1532eedc54e4dea9402c3fdaebd`;
  exact excerpt SHA-256
  `a23dce9b5d2a3de98f274f51cf31cff5426546318c35a3a8208671883ea9e13d`.

The initial packet did not contain the manuscript equations needed to verify
the attribution in candidate lines 65–71. This limitation was reported. The
supervisor then explicitly extended the input scope to the primary manuscript:

- `paper/main.tex`, lines 178–443, 498–525, 1284–1333, and 1485–1498, all
  read completely. Full-file SHA-256
  `fa44deda090a456640b64080767511003dc8bc385790ccc49fd039c931a67605`.

No other scientific files were opened. In particular, no other study,
reconciliation document, route report, prior check, archived book, or study
history was read. The referenced material beyond the assigned book excerpts
was not imported as a proved dependency. The supplied excerpt about generated
population spaces is used for the stated source/adjoint framework, not as a
proof of the candidate's population-flow existence assumption.

Process inputs were root `AGENTS.md`, `RESEARCH_WORKFLOW.md` Part 1,
`solve-math-rigorously/SKILL.md`, and `investigate-conjectures/SKILL.md` with
its research-contract and adversarial-audit references. The initial workflow
read also displayed part of Part 2; it supplied no scientific input. Routine
metadata checks showed HEAD `7fce699a7decf2239dc3eb50486eca661783b535`, no
staged paths, and concurrent untracked study directories. None was opened.
Only this assigned report was written; no Git transaction was performed.

The checker started fresh. During the audit the author sent an unsolicited
editorial note and a consistency identity relating (19) and (20). The checker
had already derived those formulas independently from the candidate, requested
that subsequent messages remain coordination-only, and did not need that
message for any scientific step. This exposure is disclosed rather than
claiming a fully blind independent review. The later primary-source scope
extension was an explicit answer to the checker's missing-input request.

Actual checks consisted of complete numbered reads, SHA-256 verification,
independent differentiation and Gaussian-conditioning derivations, boundary
checks, and assumption/limit audits. No simulation, numerical quadrature,
finite-network training, or experiment was run.

## 1. Architecture and normalization

The manuscript learning-speed equations specialize exactly to candidate
(1)–(2). At \(q=1\), its moment equations are

\[
\dot{\bar h}_a=\rho H_a,\qquad
\dot{\bar\delta}_a=r_aD_a,\qquad \dot\tau=\rho.
\]

With \(K_a=\bar h_a/\tau\), \(V_a=-2\bar\delta_a\), and \(m=2\), the
population reconstruction is

\[
T-\frac{2}{m\tau}\sum_a\bar\delta_a\otimes\bar h_a
=T+\frac12\sum_aV_a\otimes K_a.
\]

Differentiating the quotient gives
\(\dot K_a=(\rho/\tau)(H_a-K_a)\). The manuscript first-layer/readout
factor \(2/m=1\) yields exactly the two remaining physical equations.
The candidate's unit mobilities are unit normalized population block rates;
no finite-width normalization has been lost.

For the joint clock, its \(q=1\) triangular matrix is zero, \(p_0=1\), and
its scalar Gram mass \(M\) satisfies \(\dot M=\rho\), \(M(0)=1\).
The zeroth forward/backward moments obey the same equations above. Zero
readout makes the initial backward response \(b_a(0)\) zero, so the joint
clock's prefix-product subtraction vanishes. Thus \(K_a=\bar h_a/M\) and
\(V_a=-2\bar\delta_a\) give the same physical reconstruction and state
equations, although the joint coordinate clock generally differs from \(M\).
This verifies candidate lines 65–71 against the primary equations.

The displayed system is not dense gradient flow: differentiating its memory
operator introduces both \(V_a'\otimes K_a\) and
\(V_a\otimes K_a'\), with averaged keys rather than current \(H_a\).
The later negative lag term makes this distinction explicit.

Absorbing binary labels into inputs and into each sample's key/value preserves
the memory operator because each outer product acquires \(y_a^2=1\).
Oddness of both activations gives the signed residual transformation and
preserves the complete query predictor. With exchange symmetry,
\(r_1=r_2=f-1\), and before fitting,
\(\rho=1-f\), \(ds/dt=2(1-f)\), \(\tau=1+s/2\).
These identities give all factors in (4)–(6).

The input vectors \(e^{\rm raw}_\pm=(p_1\pm p_2)/2\) are orthogonal,
with squared norms \(\gamma_\pm=(1\pm c)/2\). Therefore
\(q_\pm'=\gamma_\pm L_\pm\). The tanh addition formulas give (7), and
the channel Jacobian is \(\begin{psmallmatrix}E&C\\ C&E\end{psmallmatrix}\).
Exchange parity removes exactly the cross-channel contractions in (4).
Finally, \(D_-=-2G_+G_-W\) and \(W'=G_+\) give (8) without a sign
assumption on the evolving fields.

## 2. First reverse source law and its qualification

The two-root feature Gram matrix is nonsingular for \(-1<c<1\): the first
Gaussian pair has full support, and the odd tanh features are not linearly
dependent. Consequently both channel variances \(a_\pm\) are positive.

The conditional matrix formula in the supplied Gaussian chapter gives, after
the two forward observations, a transpose mean with coefficients
\(\mathcal C^{-1}\mathbb E[zU]\). The remaining Gaussian matrix is projected
off the two-dimensional input span. For a finite list of reverse sources, its
joint covariance is the full source Gram matrix
\(\mathbb E[U_aU_b]\), not a regression-subtracted covariance. The finite-rank
input projection removes an asymptotically vanishing coordinate innovation;
the population innovation is independent of the original first-layer roots.
Gaussian integration by parts then converts the mean coefficients to the
derivative expectations in (9), provided those expectations and that identity
are justified. This is a fixed finite-source statement, not identification of
a trained trajectory or an unbounded adaptive program.

**Required minor correction R1 (candidate lines 171–177 and 193–195).** Replace
“bounded smooth functions” with, for example, “bounded \(C^1\) functions
with bounded first derivatives.” Equivalently, state the precise Gaussian
Sobolev/integration-by-parts conditions being imposed. Bounded smooth
functions alone need not have integrable derivatives. For example,

\[
U(z_1,z_2)=\sin(\exp(z_1^4))
\]

is bounded and smooth, whereas its first derivative has infinite absolute
Gaussian expectation for every positive variance of \(z_1\). On the positive
half-line, substituting \(t=\exp(z_1^4)\) into the absolute derivative integral
leaves a positive constant times
\(\int_1^\infty |\cos t|\exp[-\sqrt{\log t}/(2\sigma^2)]\,dt\), which
diverges; the positive and negative derivative parts both diverge. Thus the
expectation defining \(M\) is not generally defined as written. If the author
intended “bounded smooth” to mean \(C_b^\infty\), naming that class explicitly
resolves the issue.

Every \(U_a,Y_a\) actually used in (10) is a polynomial combination of tanh
and its bounded derivatives, so R1 affects neither its Gaussian law nor any
later calculation.

Exchange parity gives the four-channel reverse representations in (11).
Adjunction checks their coefficients directly:
\(\lambda_\pm a_\pm=\mathbb E[z_\pm U_\pm]\), and similarly for
\(\nu_\pm\). Since \(g_\pm\) has the sign of \(z_\pm\), \(P>0\), and the
Gaussian pair has full support, all four strict signs in (11) are correct.
The innovation pairings are exactly

\[
\mathbb E[U_+Y_+]=\mathbb E[U_-Y_-]
=-2\mathbb E[P g_+^2g_-^2]=\omega<0.
\]

The opposite-parity products integrate to zero. These computations confirm
that four jointly Gaussian innovations are necessary. Independent resampling
of the two source pairs would remove the negative covariance term used later.

## 3. Both full hidden-population energy signs

Initially \(W'=g_+\), while \(A'=V'=K'=0\). Bounded tanh gates, bounded
\(T^*\), and the strong-flow assumptions give \(D_a(s)/s\to U_a\) in
\(L^2\). Hence

\[
A''(0)=\mathcal A_U
=\frac12\sum_a(1-h_a^2)(T^*U_a)p_a,
\qquad V_\pm''(0)=U_\pm.
\]

A varying bounded gate times a convergent \(L^2\) field converges by splitting
off the limiting field and using bounded convergence in probability against
its squared magnitude. This justifies the indicated products without assuming
that the tanh Nemytskii map is globally Frechet differentiable on all of
\(L^2\). The same argument yields the stated directional second-order feature
jets; no convergent Taylor series is being used.

Differentiating the first-layer channel Jacobian gives (14), including the
coefficient \(EC\) in each mixed term because
\(\gamma_++\gamma_-=1\). Conditioning on \(A_0\) removes the mean-zero
innovations. Since \(C=-2h_+h_-\), the two pairings are exactly

\[
\chi_+=\lambda_+Q_+-2\lambda_-J_0>0,\qquad
\chi_-=-2\lambda_+J_0+\lambda_-Q_-<0.
\]

Here \(J_0,Q_+,Q_->0\) follows from positive gates, positive \(\gamma_\pm\),
and full support. Thus \(\mathcal S_1''=2\chi_+>0\) and
\(\mathcal D_1''=2\chi_-<0\).

For layer two, \(Z_\pm''=TH_\pm''+a_\pm U_\pm\). There is no leading key contribution because \(K'(0)=K''(0)=0\).
Applying the second tanh Jacobian to the memory part gives exactly (16).
Its common-energy contribution is positive and its difference-energy
contribution negative, both strictly.

For the read-in part, varying \(A\) with \(T\) fixed gives

\[
\nabla_A\|G_+\|^2=\sum_a(1-h_a^2)T^*U_a\,p_a
=2\mathcal A_U,
\]

and the difference-energy gradient is \(2\mathcal A_Y\), where the minus
sign in \(Y_2=-g_-(1-g_2^2)\) is essential. Because \(A'(0)=0\), the
second derivative contains the gradient paired with \(A''\), with no
quadratic Hessian term. This proves both factors of two in (17).

The conditional means of \(L^U_\pm,L^Y_\pm\) are exactly the four expressions
displayed after (17). Their products have negative sign almost surely outside
zero sets of Gaussian measure zero. The conditional innovation contribution
for each same-channel pairing is

\[
\operatorname{Cov}(E\zeta^U_++C\zeta^U_-,
                    E\zeta^Y_++C\zeta^Y_-\mid A_0)
=(E^2+C^2)\omega,
\]

and the same expression holds for the minus channel. There is no omitted
cross-parity term, and no mean-regression subtraction is appropriate here.
Both channel pairings are therefore strictly negative. Orthogonality of the
two raw input directions gives (18), so the entire moving-read-in
contribution to difference energy is negative. Combined with the memory part,
this proves the claimed full \(\mathcal D_2''<0\). The common contribution
\(2\|\mathcal A_U\|^2\), together with the strictly positive memory part,
proves \(\mathcal S_2''>0\).

All four energy first derivatives vanish. Differentiating the normalized
overlap gives \(2(D S''-S D'')/(S+D)^2>0\), so its initial strict increase
is justified. Strong chain rules also give the derivative asymptotics needed
if “increase” is read as monotonicity on a sufficiently short interval.
The input correlations \(c=\pm1\) are correctly excluded; no uniform positive
lower bound as \(c\to\pm1\) has been proved or claimed. Physical second
derivatives gain a factor four because \(ds/dt=2\) and the first derivatives
vanish at initialization.

The first-layer acceleration statement concerns the two sample channels:
their conditional covariance is nondegenerate. If interpreted as a covariance
matrix of the full vector \(A''\in\mathbb R^d\), it has support only in the
training plane and is singular when \(d>2\). Naming the two-channel covariance
in candidate line 301 would remove this optional notational ambiguity.

## 4. Rank, training expansion, and lag

The two initial \(U_\pm\) are nonzero in \(L^2\). Their expansions
\(V_\pm=s^2U_\pm/2+o_{L^2}(s^2)\), positive initial key norms, and exact
parity orthogonality make both left and right memory pairs independent for
small positive time. The reconstructed perturbation therefore has rank two.

Writing \(g''=G_+''(0)\), the independent cubic computation is

\[
\langle s g_++s^3g''/6,\ g_++s^2g''/2\rangle
=\kappa s+\frac23\langle g_+,g''\rangle s^3+o(s^3)
=\kappa s+\frac13\mathcal S_2''(0)s^3+o(s^3).
\]

This verifies (19) and its scope as progress per accumulated residual, rather
than an asserted all-time physical-loss monotonicity theorem.

Differentiating \(f=\langle W,G_+\rangle\) in its independent blocks gives
the gradients stated before (21), after restricting to the exchange-symmetric
state. Contracting with their velocities yields all four contributions in
(20). In particular, the key contribution is a current–past pairing and has
no square-norm sign guarantee. Solving the linear key equation and using
\(V_\pm'=D_\pm\), \(W'=G_+\) verifies all of (21).

The key has \(K_\pm=h_\pm+O_{L^2}(s^3)\), whereas
\(H_\pm=h_\pm+s^2H_\pm''(0)/2+o_{L^2}(s^2)\). Therefore

\[
a_--b_- =\chi_-s^2/2+o(s^2),\qquad
d_- =\|U_-\|^2s^3/2+o(s^3).
\]

Dividing their product by \(2+s\) gives
\(\chi_-\|U_-\|^2s^5/8+o(s^5)\), and integration gives coefficient
\(\chi_-\|U_-\|^2/48\) at order \(s^6\). Both are negative. Meanwhile,
\(b_-\|D_-\|^2=a_-\|U_-\|^2s^2+o(s^2)>0\), so the candidate correctly
does not infer increasing loss.

The conditional fitting bridge is algebraically correct: where
\(n=\|W\|>0\), \(n'=f/n\), and Cauchy–Schwarz yields
\(f^2\le n^2\|G_+\|^2\). Thus the extra hypothesis
\(f'\ge\|G_+\|^2\) gives \(n''\ge0\), \(n'(0+)=\sqrt\kappa\), and
\(f'\ge\kappa\). A regular feature curve continued to its first fitting
point consequently fits by \(s\le1/\kappa\). Along the associated physical
curve, \(\partial_t(1-f)=-2f'(1-f)\) gives the displayed loss bound
\(\mathcal L(t)\le e^{-4\kappa t}\).

The local foundation alone does not provide that continuation. Candidate
lines 430–432 already add regular continuation to the bridge; for maximal
precision, put that assumption before the crossing assertion as well: the
flow must remain regular until fitting or through \(s=1/\kappa\). This is a
clarification of the intended conditional result, not evidence that its
unproved dissipation hypothesis holds for the canonical population.

## 5. Whole-query statements and fitted endpoint

Uniqueness/equivariance plus deterministic scalar observables gives invariance
under the input reflection exchanging the two samples and under rotations
fixing their span. Combining those invariances with architectural oddness
gives exactly (23), including oddness in \(\alpha\) and evenness in \(\beta\).
The mandatory zero hyperplane (24) follows and survives pointwise limits.
No sign crossing or exclusion of further zeros follows from this argument.

For a \(C^1\) query function, division by \(\alpha\) extends continuously at
zero using the derivative integral. Its evenness and radial invariance give
the displayed continuous function of squared coordinates. Restriction to the
unit circle gives (25); evaluating a training point gives exactly
\(Q_*((1+c)/2)=1/\sqrt{(1+c)/2}\). The supplied bounded smooth example has
the required symmetries and training values, and for the indicated strict
bound on its parameter it has additional zeros. It is correctly identified
as a symmetry counterexample, not a reachable-flow construction.

At initialization only readout velocity contributes. The two-layer initial
covariance composition in (26) is correct with physical factor one for each
sample. For nonzero query norm, each covariance map is odd and strictly
increasing: differentiation of the nonsingular Gaussian density in its
off-diagonal covariance gives its mixed spatial derivative, and integrating
twice by parts against tanh produces
\(\mathbb E[\operatorname{sech}^2X\operatorname{sech}^2Y]>0\).
Boundedness permits continuous extension to the covariance endpoints. For
the zero query, both sides are zero directly. Therefore the comparison of
\(p_1\cdot u\) with \(-p_2\cdot u\) gives exactly the stated initial sign.
This is pointwise in the query; it is not uniform sign propagation over
arbitrarily nearby points or over all times.

At a finite-feature-time fitted endpoint, integration of \(W'=G_+\) gives
the first part of (27). Fitting and parity imply
\(\langle W_*,G_{+,*}\rangle=1\) and
\(\langle W_*,G_{-,*}\rangle=0\). In particular \(G_{+,*}\ne0\), so the
denominator is valid. Since the final plus/minus features are orthogonal,
\(G_{+,*}/\|G_{+,*}\|^2\) is the minimum-norm readout satisfying both
training constraints. The remainder is orthogonal to both training features,
which proves the full decomposition and its vanishing on training queries.
It does not determine the query-dependent history term from initialization.

For \(c=-1\), architectural oddness makes the two signed responses opposite,
so the specified \(W=V=0\), fixed \(A,K\), and \(\tau=1+t\) solution is
exact and never fits. For \(c=1\), the difference channel disappears. These
boundary statements are correct and do not extend the strict theorem to
degenerate inputs.

## Final claim levels and required action

1. **Exact initialized finite-source algebra:** the Gaussian regression and
   four-source covariance calculation, with source-class correction R1.
2. **Exact conditional population conclusions:** the identities, full local
   energy theorem, cubic progress coefficient, adverse lag, and symmetry/initial
   query sign hold for the stated regular equivariant population realization.
   The explicit actual-\(q=1\) identification is verified from the added primary
   manuscript ranges.
3. **Further conditional endpoint/long-time conclusions:** the fitting bridge
   requires its extra dissipation and continuation hypotheses; (27) requires
   the stated fitting/convergence endpoint. Neither supplies those hypotheses.
4. **Open canonical claims:** construction and uniqueness of the complete
   population flow, its trained-width identification, control of future
   memory work, global fitting, endpoint existence, and full fitted-query
   amplitude/sign. Formal finite jets do not close these gaps.

Correct the source-class wording in R1 before recording a whole-note PASS.
No change to the four-source proof, strict signs, normalization, or coefficients
is required. The continuation wording and the typed covariance clarification
above are recommended precision edits. This report establishes neither
promotion status nor a global theorem.

## Correction-verification addendum — 2026-09-30

**Verdict: PASS for the corrected note's stated conditional mathematical
claims.** Required correction R1 is resolved; both recommended precision
clarifications are also present. This verdict does not establish canonical
population existence, trained-width identification, global fitting, or
promotion status.

The corrected candidate is TWO_SAMPLE_POPULATION_ANALYSIS.md, 552 lines,
SHA-256 6fca4558d5d54a40fbb9c49b772ac0c621ab4e61e06c92b6be64700acbb034d2.
The original report above is preserved byte-for-byte; its pre-addendum SHA-256
is 8c6ce5967385ec603137234c51db153e166b6084ea7b6dcc7884ade438ebbf1e.

Actual new read scope: corrected candidate lines 1–12, 164–184, 259–343, and
424–443, plus the complete exact change diff. No README, other report, other
scientific file, or new dependency was read. The unchanged remainder retains
the complete original read/check recorded above.

To verify that this was a bounded correction, the checker reversed exactly
the seven edited text blocks in memory and hashed the reconstructed original.
The result was exactly the frozen original SHA-256
70ff598878f21224842e80d91c0e9fd7639a2c48d40bb3a0da9f62fadf0a9599.
This check establishes that there were no additional unnoticed changes. No
candidate or scratch file was written during that comparison.

The source class now explicitly requires bounded \(C^1\) functions with
bounded first derivatives (lines 172–173). Gaussian derivative expectations
are then finite, and the integration-by-parts argument applies. All four
actual sources remain in this class.

Lines 302–304 identify the nondegenerate covariance as that of the two sample
preactivation channels, with full-vector covariance supported on the training
plane. This is correct: the two \(U_a\) have a positive-definite source Gram
matrix, since no nontrivial constant linear combination of
\(g_+\operatorname{sech}^2z_1\) and
\(g_+\operatorname{sech}^2z_2\) vanishes on a full-support Gaussian pair.
The channel gate matrix and the positive \(\gamma_\pm\) factors are invertible,
so the conditional two-channel covariance is positive definite.

Lines 430–436 put regular continuation through fitting or \(s=1/\kappa\)
before the crossing bound. This supplies the continuation condition used in
the original check's conditional argument. It does not claim that the
unproved dissipation inequality holds on the canonical flow.

The remaining changes are the administrative status wording and TeX rendering
of \(\mathcal A_U,\mathcal A_Y\). No displayed equation, coefficient, sign,
normalization, source pairing, or theorem conclusion changed. The status
reference to README was not independently inspected, as instructed.

The original substantive checks therefore carry over, and no required
mathematical correction remains within this packet's explicit conditional
scope.
