# Round 1 — isolated document-only scope and strategy review

**Verdict: NEEDS_CORRECTIONS.** Four local corrections are required for precise mathematical and evidentiary statements. They do not overturn the central research strategy, establish a false external theorem, or require completing the research program before publishing an accurately qualified consolidation.

## Evidence boundary and full-read confirmation

- Sole research evidence: `/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md`.
- SHA256: `dee7a2fb5c4350d1883d2939f06bca67581274d9b94b44dce9b23225d7a8e62a`.
- **Full read confirmed:** all 541 lines, 79,991 bytes, including every section and both task maps. The source hash was identical before and after the read and analysis. All source line references below refer to this version.
- No linked sources, other project files, histories, audit reports, or other agents' outputs were read. No browsing, experiments, proof campaigns, or source edits were performed. Only the operational paper-review skill and its severity rubric were additionally read. This review is the only file written.
- The master's descriptions of earlier inspections are evidence about its declared audit coverage, not independent certification here of those external proofs. “Internal,” “checked,” and “dependency-qualified” below retain that distinction.

## Required corrections

### R1 — Distinguish the finite Gaussian response from its limiting coefficient

**Location:** line 72; compare the finite-program/annealed distinctions at lines 59–60 and 70.

The example starts with a finite Gaussian matrix, sets `Y = W 1`, and then assigns the response in `W^T g(Y)` the expectation coefficient `E g'(Y)`. At finite width the conditional response coefficient is random. The expectation is the limiting coefficient, and also the mean of the finite coefficient; those are different claims. The sentence's subsequent appeal to “exact conditional Gaussian projection” makes this distinction necessary.

This can be checked entirely from the displayed model. For an n-by-n matrix, put

\[
P=I-\frac{\mathbf1\mathbf1^T}{n},\qquad
a_n=\frac1n\sum_{i=1}^nY_i g(Y_i).
\]

Then the exact conditional statement is

\[
\mathbb E[W^Tg(Y)\mid Y]=a_n\mathbf1,\qquad
\operatorname{Cov}(W^Tg(Y)\mid Y)
=\frac{\|g(Y)\|_2^2}{n}P.
\]

For example, `g(u)=u` gives `a_n=||Y||_2^2/n`, which is not identically the proposed coefficient 1. Under the polynomial growth assumptions already stated, with `G` standard normal,

\[
a_n\longrightarrow \mathbb E[Gg(G)]=\mathbb E[g'(G)].
\]

**Proposed replacement:** “Conditionally on the finite vector Y, the response along the earlier input 1 has coefficient `n^{-1} sum_i Y_i g(Y_i)` and the remaining term is conditionally centered Gaussian in the orthogonal complement of 1. In the width limit the response coefficient converges to `E[G g(G)] = E[g'(G)]`, for standard normal G. A later forward call must retain this transpose-use response.”

This repairs the illustrative finite-versus-limit statement. It does not invalidate the response principle or identify a defect in an unread MFP proof.

### R2 — Do not give a mixed-evidence Stieltjes table a blanket decisive-negative label

**Location:** lines 129–137, particularly the introduction at line 129 and the QI/sine rows at lines 136–137; compare the evidence taxonomy at lines 25–29.

“There are nevertheless decisive scoped negatives” introduces both argument-backed counterexamples and rows whose reported support is an unrederived coefficient table or retained high-precision signs. The sine row explicitly says that no independent rigorous transcendental enclosure was audited. Its qualification is useful and should remain; the introductory certification is stronger than the evidence supplied for the table as a whole.

This is a calibration correction, not an assertion that the sine sign is wrong or that an uninspected rigorous source cannot exist. The QI coefficient-generation qualification likewise must not be converted into either a counterexample to its result or a fresh proof certification.

**Proposed replacement for line 129:** “There are scoped counterexamples and negative witnesses in other models, with different levels of verification:”

**Proposed wording for the sine row:** “Retained high-precision negative signs; computational evidence reported here, with rigorous enclosure status not independently certified in this audit.” Keep the QI row's explicit coefficient-generation qualification. The block-metric conclusion at line 139 can retain its stated, model-specific scope.

### R3 — State the three-sample separation hypotheses only for distinct samples

**Location:** table rows at lines 254–255, using the normalization defined at line 39.

The conditions are printed as `G_ab <= 1-delta` and `|G_ab| <= 1-delta`, without restricting the indices. The same document imposes `G_aa=1`. If the displayed restrictions include diagonal entries, neither theorem row has admissible normalized data for positive delta. The intended pairwise separation is clear from context, but a table presented as the exact scope must state it.

**Proposed repairs:**

- Bounded-shape/offset-gain row: “`m=3`, normalized inputs, and `G_ij <= 1-delta` for every distinct `i,j` in `{1,2,3}`, with `0<delta<1`.”
- Odd-overall-gain row: “`m=3`, normalized inputs, and `|G_ij| <= 1-delta` for every distinct `i,j` in `{1,2,3}`,” followed by the admissible separation range already intended for that theorem.

This is a missing quantifier in the consolidation, not a demonstrated vacuity of the underlying source theorems. Do not repair it by requiring an invertible raw Gram: that would contradict the intended singular-Gram coverage and materially change the scientific setting.

### R4 — Repair the exact odd-mixture formula before using its scientific consequences

**Location:** line 296 and the associated initialization and near-linear discussion at lines 298–310; compare the odd-network symmetry statement at line 437.

The purported definition is malformed as `phi_theta=$1-theta$z+theta arctan z`. It lacks an unambiguous parenthesized coefficient of z and working math delimiters. Read literally as `1-theta z+theta arctan z`, it has value 1 at zero and is not odd. These are materially different architectures in precisely the symmetry and near-linear comparisons that this section is making.

**Proposed replacement:**

\[
\phi_\theta(z)=(1-\theta)z+\theta\arctan z,
\qquad 0<\theta\le1.
\]

Use this explicit definition for the “exact odd mixture” throughout the report. Also render the three asymptotic scales at line 308 unambiguously as `(2 theta L)^{-1}`, `(12 theta L^3)^{-1}`, and `(6 L^2)^{-1}`, keeping their respective observable labels. This restates the intended reported formulas; it does not independently certify their external proofs or constants.

## Scope and strategy findings that survive

The document correctly separates activation nonaffinity, hidden displacement, kernel change, and separation from a reference predictor at line 66. It does not generally promote an initial derivative into persistent feature learning. The activity clauses at lines 210–212, the gain qualifications at lines 270–278, and the initialization-only limitations at lines 306–312 preserve these distinctions. In particular, it correctly declines to apply the small-relative-nonlinearity inequality to an odd activation whose two coefficients are equal.

The principal dense Gaussian model remains distinguishable from affine-first, gain, residual-particle, coherent-initialization, and altered-clipping constructions. The global examples are useful existence/fitting results at their declared scope; they are not presented as settling the moderate-scale correlated-data objective. The separation of the three clipping constructions at lines 318–359 is especially important and internally consistent.

Existence, finite optimization, population identification, and generalization are also kept separate. The finite pure-atan fitting result at line 292 does not become a global population theorem. The finite-horizon accuracy argument at lines 463–471 supports prescribed accuracy and does not exchange all-time and width limits. Passive test-input characterization at line 473 is explicitly a proposed bridge, not an existing risk guarantee.

The evidence levels at lines 25–29, history limitations at line 35, specific pending checks at lines 165, 221, 282, 290 and 429, and final qualification at line 541 are not grounds for calling the associated external results false. They are also not grounds for certifying them from this document alone. No further substantive contradiction was found in the treatment of historical status or in the main continuation recommendation. The recommendation is a defensible research judgment supported by the reported bottlenecks; the document does not prove it is the uniquely viable route.

## Optional suggestions — not required corrections

1. At lines 450–452, make the next milestone operational by naming the chosen activation, stored-readout convention, data/label class, and finite-depth/time quantifiers. If “moderately nonlinear” is intended as an acceptance criterion, specify a relative affine-fit residual on reached distributions and measure hidden displacement separately. Kernel change and separation from a fixed-kernel predictor should remain separate possible targets. This would improve research planning without changing current theorem status.
2. Give the affine-first row at line 248 an explicit audit-grade label, as the neighboring rows have. This is a request for consistent presentation of the master's existing coverage, not an inference here that its source is defective.
3. Repair the other malformed math delimiters, including the response expectation at line 72, the readout vector at line 108, and `r(u)=(1+u^2)^{-1}` at line 153. For the otherwise valid inequality at lines 272–278, say that the test affine fit uses slope `a` and intercept `e E[psi(Z)]`; that explicitly justifies the variance numerator.

The required changes are local to the master’s statements. An accurate consolidation can retain honestly marked source followups and an open central research objective.
