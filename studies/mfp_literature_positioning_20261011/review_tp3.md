# Tensor Programs III: complete scoped literature audit

Audit date: 2026-10-11. Scope: the complete primary paper and its version history; the assigned MFP sources only. This report is a literature comparison, not a promotion review or a claim that every printed result of TP III has been independently certified.

## Finding

For MFP's admitted smooth, polynomial-growth primitive programs, the finite Gaussian evaluator is already contained in the **stated** Tensor Programs III v3 master theorem, including scalar averages fed into later calculations, arbitrary finite matrix/transpose reuse, and singular or duplicate queries. The decisive result is **Theorem E.15, p.33**, not merely Theorem 2.10 or the rank-stable Theorem E.5. Box 1, pp.8–10, supplies the same source/correction construction. MFP's stronger all-finite-order moment and scalar Lp assertions are not supplied by the general TP III expectation theorems: Appendix A expressly leaves the general polynomial expectation extension as Conjecture A.4. This is a distinction relative to this source, not a global novelty conclusion.

MFP adds an explicit exact finite-width differentiation and update language, a symbolic implementation with separate physical and source derivatives, and a restricted initialization normal form. Complete inspection of TP III found neural forward/backward and NTK examples, but no corresponding general high-order AD/flow-jet compiler specification or implementation in this paper. The ability to evaluate a finite graph once its derivatives have been encoded is already the Tensor Programs method. These two statements must be kept together.

There is a qualification to independent verification: Appendix N's proof of E.15 is substantially more compressed than Appendix L's proof of the base theorem. I reconstructed the intended orthogonal-core argument, identified a printed normalization error, and could not independently justify its decisive coefficient-convergence assertion from the supplied argument alone. This is not a counterexample to E.15, does not erase its prior statement, and does not justify describing rank-free scalar feedback as absent from the literature.

## Source identity, versions, and coverage

Primary landing page: [arXiv:2009.10685](https://arxiv.org/abs/2009.10685). Audited primary PDF: [v3](https://arxiv.org/pdf/2009.10685v3), Greg Yang, *Tensor Programs III: Neural Matrix Laws*, last revised 8 May 2021. PDF page numbers below coincide with printed page numbers, including the unnumbered first page.

| Version | arXiv submission date | Pages | SHA-256 of downloaded PDF |
|---|---|---:|---|
| v1 | 22 Sep 2020 | 83 | `9fd961afb619a95b66a4546f274aaf5efa821a3ec165e4179a7ab79a41c2e27b` |
| v2 | 30 Nov 2020 | 86 | `02c16245dc9ebb60ffdbe0c1076e52b045d7397680b3354e87c7440ce88e1a71` |
| v3 | 8 May 2021 | 87 | `6b0d6504c12373e6837de0aff5ab77bb18675a225fcda10d59b56540ec74b5da` |

Downloads and page extracts are in `data/generated/mfp_literature_positioning_20261011/tp3/`. The v3 PDF is 1,521,166 bytes. The audit read **all 87 v3 pages**, including Sections 1–8, references, and Appendices A–N. Coverage: main pp.1–21; references pp.21–24; A pp.25–27; B p.27; C p.28; D pp.28–29; E pp.29–33; F pp.33–36; G pp.36–37; H pp.37–39; I pp.40–43; J pp.43–45; K pp.45–59; L pp.60–84; M pp.84–85; N pp.85–87. Pages with truncated extraction output were reread; p.86 was also inspected as a rendered image to distinguish a PDF error from extraction error.

Earlier versions were downloaded and searched/compared at the relevant theorem and appendix passages; they were **not** each reread from beginning to end. Material version fact: E.15 and Appendix N are absent in v1 and present already in v2. Thus a comparison based on v1 alone misses the rank-free scalar-feedback theorem. v2 additionally prints a variable-dimension rank-free Theorem F.11 on p.36; v3 does not print F.11. No reason for that omission was established. Equal-width MFP programs can be encoded in the equal-dimension theorem E.15, so this omission does not block the present overlap.

Searches for the exact title with “erratum” and “correction”, plus the arXiv version history and primary Microsoft Research publication listing, did not locate a separate authoritative erratum. This is a bounded search result, not proof that no correction exists. The authoritative visible arXiv record still lists v3 as latest.

Required canonical notation and neural-network conventions and the rigorous-math skill were read. Repository inputs inspected: `docs/02-gaussian-reuse.qmd:252–1293`, `docs/12-three-sample-learning.qmd:316–684`, the abstract/introduction and relevant theorem/compiler locations in `paper_MFP/main.tex`, and the complete `paper_MFP/code/MFP_CALCULUS.md`. No other studies or reviewer reports were read. No code tests or external experiments were run.

## Exact theorem domains and convergence

The base language (Definition 2.1, p.6) forms finitely many vectors by coordinate functions and multiplication by named Gaussian matrices or their actual transposes. Setup 2.2 (p.7) fixes Gaussian iid coordinate tuples for initial vectors and independent iid Gaussian matrices with variance sigma_W^2/n. The number of arguments and functions are fixed as width increases. Jointly Gaussian initial tuples may be singular; the base case in Appendix L.3 chooses a basis of their Gaussian span. A fixed mean can be absorbed into coordinate maps (p.60).

Theorem 2.10 (p.9) assumes polynomially bounded nonlinearities and polynomially bounded tests and gives almost sure convergence of empirical averages to the recursively specified scalar law. Differentiability is not required in this theorem. Its rank stability is proved rather than imposed: Theorem 6.3 (p.19), Lemma L.11 (pp.68–69), and the CoreSet induction (pp.60–74). This is stronger regularity coverage than MFP's smooth activation-derivative class, but does not allow scalar feedback within its basic language.

The enlarged language NETSOR⊤+ (Definition E.1, p.29) has Nonlin+, Moment, and MatMul. Moment computes normalized scalar averages, and later Nonlin+ may use them. Initial scalar sequences converge to deterministic constants; MFP's fixed deterministic initial scalars are a special case. Scalar arithmetic is included by taking no vector arguments in Moment. Definition E.3 (p.30) replaces computed scalars by their deterministic limits when constructing the representative law.

Three results must not be conflated:

* E.5, p.30: pseudo-Lipschitz program maps, rank stability E.7, and polynomially bounded empirical tests.
* E.11, pp.31–32: composed functions parameter-controlled at limiting scalar values, rank stability E.7, and corresponding parameter-controlled tests of G-vars. Parameter control permits some discontinuities in vector arguments and some divisions near nonzero limiting denominators.
* **E.15, p.33:** pseudo-Lipschitz program maps and pseudo-Lipschitz tests, **without rank stability**. This covers the MFP primitive class.

The implication needed for that last comparison is direct. Every MFP coordinate expression F has polynomially bounded first derivatives, hence, by integrating its derivative on the segment from x to y,

    |F(x)-F(y)| <= C (1+|x|+|y|)^d |x-y|.

This is the pseudo-Lipschitz condition of E.4. Scalar sums/products and normalized averages meet it. Types can be encoded using disjoint independent root blocks and named matrices in the equal-width language; no operation needs to mix forbidden types. Represented rank terms lower to coordinate maps and Moment: (u v^T/n)h = u (v^T h/n). Therefore a fixed compiled MFP program satisfies E.15's advertised hypotheses. No nonsingularity assumption is needed for this mapping.

Almost sure empirical convergence in E.15 also implies almost sure Wasserstein-2 convergence for each fixed tuple: use a countable determining family of bounded Lipschitz functions for weak convergence and the pseudo-Lipschitz test |x|^2 for second moments, then the finite-dimensional weak-plus-second-moment characterization. Thus MFP's empirical W2 convergence in probability is not a stronger empirical-law statement in this Gaussian/pseudo-Lipschitz subclass. MFP's separate C1 bounded-derivative foundation permits general finite-second-moment roots, whereas TP III's stated setup uses Gaussian roots; that difference should not be silently imported into its smooth fixed-Gaussian theorem.

The convergence-of-expectations boundary is explicit. A.1 (p.25) gives L1 for bounded tests. A.2 (pp.25–26) gives L1 for quadratically bounded tests with linearly bounded program nonlinearities. A.7 (p.27) states a scalar-feedback extension with rank stability and additional linear/quadratic parameter-control bounds. Conjecture A.4 (p.26) leaves the general polynomial expectation extension open. Theorem A.5 and A.6 (pp.26–27) give convergence in distribution of finitely many neuron coordinates, with distinct coordinates asymptotically independent; those statements are not uniform integrability.

Appendix L repeatedly proves **almost sure pathwise boundedness** of empirical higher moments (notably L.20, pp.78–79). A random pathwise bound need not have a bounded expectation. Consequently it cannot be substituted for MFP's bounds sup_n E[(n^-1 sum_i |v_i|^p)^q] < infinity or its scalar Lp convergence. The smooth raw-entry argument in MFP supplies precisely additional annealed control; its relevance should be stated without claiming that it settles Conjecture A.4 for every merely polynomially bounded discontinuous nonlinearity.

## Source rules: direct translation and singular coefficients

Write MFP's forward calls as y_r=W h_r and reverse calls as v_s=W^T u_s, with scalar representatives H_r,U_s. Take sigma_W=1. The exact dictionary to Box 1 is

| MFP | TP III |
|---|---|
| H_r, U_s | Z^{h_r}, Z^{u_s} |
| forward source xi_r | hat Z^{W h_r} |
| reverse source zeta_s | hat Z^{W^T u_s} |
| response part | dot Z |
| coordinate map | ZNonlin / ZNonlin+ |
| normalized average limit | ZMoment |

Both constructions specify Cov(xi_r,xi_t)=E[H_r H_t] and Cov(zeta_s,zeta_v)=E[U_s U_v]. These are uncentered input second moments. The forward and reverse Gaussian groups, and different named matrices' groups, are independent, but their full outputs are not. Their output rules agree:

    Y_r = xi_r + sum_{s earlier} U_s E[partial_{zeta_s} H_r],
    V_s = zeta_s + sum_{r earlier} H_r E[partial_{xi_r} U_s].

TP III Remark 2.11 (p.9) defines partials through the actual syntactic expression in named Gaussian source variables, and explicitly notes that equivalent ways to write a program can have different individual partials. Its footnote 16 freezes the deterministic limiting parameters in NETSOR⊤+. This is MFP's formal-source convention, distinct from differentiation through finite averages or through the Gaussian sampling law. The source response is not new to MFP under this comparison.

Remark 2.12 (p.10, Eq.(4)) supplies a pseudoinverse definition when classical derivatives do not exist. If C_{st}=E[U_s U_t] and b_s=E[zeta_s H], then the correction is U^T C^+ b. This does not demand an inverse or exclude duplicate queries. For MFP's smooth expressions, Gaussian integration by parts gives b=C E[grad_zeta H], so

    U^T C^+ b = U^T C^+ C E[grad_zeta H] = U^T E[grad_zeta H],

because U^T a=0 almost surely whenever a is in ker(C), as E[(U^T a)^2]=a^T C a=0. This proves equality of the total correction even when the Gram is singular.

A precision issue in Remark 2.12: its assertion that pseudoinverse coefficients agree with derivative expectations needs this quotient-space qualification. If U_1=U_2=1 and H=zeta_1 with zeta_1=zeta_2 on the Gaussian support, the formal derivative vector is (1,0), whereas C^+ b=(1/2,1/2). Their contracted corrections both equal one. MFP's explicit separate-slot convention is a useful clarification/implementation discipline; it is not evidence of a different limiting law. Its duplicate-call worked example is an immediate instance of this identity.

Repeated transposes are unrestricted in Definition 2.1. The introduction (pp.3–5), Example 2.5 (p.7), and Example 2.8 (p.8) explicitly distinguish W^T Wv from a product using an independent transpose copy. No BP-like/GIA condition is imposed by the general theorem. C.1 (p.28) applies the master theorem to NTKs without Simple GIA Check when forward/backward calculations are expressible and activation weak derivatives are polynomially bounded. D.1 is a special sufficient condition for ignoring response terms, not a restriction on the evaluator.

## Reconstruction of the load-bearing argument

The following reconstructs the mechanism in common notation; it is not an appeal to a theorem name alone.

Condition on the adaptive transcript. For one named matrix record W V=Y and W^T U=Q. The constraints are feasible because they came from the actual W. Their homogeneous solution space is K=P_{U^perp} K P_{V^perp}. Orthogonal projection of the vectorized isotropic Gaussian matrix onto that affine space yields

    W | transcript = M + P_{U^perp} W_tilde P_{V^perp},
    M = Y V^+ + (U^+)^T Q^T (I-V V^+).

This is Lemma K.9 (p.48), used in L.4.1, Eqs.(51)–(54), p.65. The printed K.9 has stray Y/Z names, but the minimum-Frobenius-norm characterization and L.4 formula identify the consistent formula. Conditional independence of residual named matrix factors is preserved as each adaptive call supplies a linear observation of its own factor with its input fixed by the existing transcript; the MFP book makes this justification especially explicit.

For a new forward input h, h_perp=h-V alpha_n, where alpha_n is its empirical least-squares coefficient. The conditional output is Y alpha_n + U beta_n + sigma_n P_{U^perp} g, with sigma_n^2=||h_perp||^2/n. Stable ranks let empirical Gram pseudoinverses converge (L.5–L.7, p.66). The limiting beta_n combines pairings against old transpose outputs. The source adjunction identity L.3 (pp.62–64), and the projection decomposition L.8–L.10 (pp.66–68), cancel the projections onto old forward inputs and yield precisely the dot-Z response above. The remaining Gaussian conditional mean and covariance match the next source law (L.19, p.76).

The base theorem needs empirical convergence even for discontinuous polynomially bounded tests. Appendix L therefore simultaneously proves Moments and CoreSet (p.60). CoreSet retains a basis of G-vars, equivalence of its limiting law to Lebesgue measure, and eventual avoidance of prescribed null sets. A nonnegative polynomially bounded function with zero limiting expectation then vanishes exactly on all finite coordinates eventually (L.12–L.13, pp.69–70). Applied to squared linear relations this proves equality of empirical/limiting Gram kernels (L.11). When sigma_limit=0 the new vector becomes an exact old linear combination eventually (L.14, p.71); otherwise it acquires a nondegenerate Gaussian conditional density and joins the core (pp.71–73). This explains why the base theorem can avoid rank assumptions despite nonsmooth maps; it is not continuity of pseudoinversion at rank loss.

The empirical fluctuation step uses K.23 (pp.56–59): for covariance given by a projection with fixed corank, normalized off-diagonal correlations have bounded squared sum (K.19, or the simpler sufficient argument K.20, pp.51–55). Hermite expansions K.13–K.16 give high even moments of centered empirical tests bounded by C n^-1.5 times high marginal moments. In L.7.2, these marginal moments are bounded conditionally along almost every previous transcript sequence; choosing the additional Hölder exponent greater than four produces a summable n^-1.25 bound. Conditional Markov and Borel–Cantelli then prove almost sure fluctuation decay. L.7.3 uses Gaussian smoothing at positive variance, the derivative formulas (77)–(78), p.83, and controls the finitely many coordinates with small projection diagonal separately. These steps account for the nonsmooth base theorem's heavy proof machinery.

For E.11, Appendix M (pp.84–85) adds the error caused by replacing random scalar parameters by their deterministic limits. Parameter control bounds it by a scalar factor tending to zero times an empirically bounded polynomial envelope. Rank stability remains an assumption there.

For E.15, Appendix N (pp.85–87) replaces exact rank stability by orthogonal retained directions and directions whose normalized empirical moments vanish. Lemma N.3 is justified by the pseudo-Lipschitz difference bound and Hölder: a vanishing input factor times bounded higher empirical moments has vanishing empirical moments. A vanishing matrix input has vanishing normalized second moment after multiplication because ||W||_op is eventually bounded. Higher moments after adaptive multiplication are the decisive additional point, delegated to N.2.

**Independent-verification limit for N.2.** Its proof asserts that coefficients of retained reverse inputs converge to zero and coefficients of vanishing reverse inputs converge to finite derivative expectations. The conditioning formula alone does not supply that statement at a collapsing Gram: one needs either quantitative cancellation or another approximation argument. The printed proof provides no such bound and invokes derivative expressions despite allowing merely pseudo-Lipschitz functions. I have not filled this gap for the full stated E.15 class. This does not show the theorem false. For the smoother MFP subclass, the assigned book's perturb-each-query, remove-perturbation-by-RMS, clip, and use raw-entry uniform moments is an independently specified route avoiding this particular coefficient claim.

The p.86 rewrite also literally defines h^1=h^0/(||hat h^0||^2/n), while its orthogonality invariant and the displayed decomposition require the residual hat h^0 divided by sqrt(||hat h^0||^2/n), with the corresponding coefficient in the decomposition. I checked the rendered PDF. Correcting this local formula is straightforward; it does not itself settle N.2. Moreover, scalar normalization is only regular on a neighborhood where its limiting denominator is positive; a proof should define a fallback on exceptional finite-width states. These are proof-detail limitations, not an alternative novelty claim.

External tools needed centrally were verified in the forms used: Gaussian conditioning by finite-dimensional orthogonal projection, Stein by integration by parts after writing a singular Gaussian as B G, Hölder for polynomial envelopes, and continuity of pseudoinverses restricted to fixed rank. K.23 and L's rank argument are proved inside the completely read paper. Bayati–Montanari is historical provenance for conditioning/AMP, not an unverified black-box assumption needed for this reconstruction. I did not independently audit all external free-probability facts used for the paper's spectral applications; they are not needed to identify the MFP evaluator.

## Other source issues kept separate from the evaluator

The complete read exposed collateral statements whose literal forms should not be relied on:

1. Corollary 5.1, p.15, says that mutually independent partitions of scalar representatives give asymptotically free diagonal collections. In general commuting independent diagonal variables are classically independent, not free. Let two independent root vectors have standard Gaussian coordinates and let D,E be their coordinatewise signs on the diagonal. They are bounded, centered asymptotically, and their limiting scalar representatives are independent. Nevertheless n^-1 tr(DEDE)=1, whereas freeness would require the alternating centered moment to vanish. Thus this extra clause is false as literally written. This does not refute Theorem 4.2, which treats the entire diagonal family as one collection free from the independent weight-matrix collections.
2. Theorem 5.2, p.15, displays laws of phi'(Z), while the preceding J^T J calculation requires laws of phi'(Z)^2. For phi(x)=2x and L=2, J=2W, so J^T J=4W^T W; the displayed unsquared law would scale it by two. The subsequent identity-activation remark also needs a depth qualification: at L>2, products yield repeated free multiplicative convolution rather than a single Marchenko–Pastur law.
3. Remark 2.12's individual-coefficient equality at singular covariance has the quotient qualification explained above.

No counterexample to the core Gaussian source rule was found. These issues must not be used to dismiss its clear prior statement and extensive base-theorem proof.

## Consequences for positioning MFP

A precise comparison can say: MFP organizes a smooth finite-program subclass of the Tensor Programs calculus into an exact physical-derivative compiler, gives a self-contained proof for the stated subclass, establishes explicit all-order uniform moments and scalar Lp limits, and supplies a inspectable Gaussian-expectation DAG and restricted activation-moment reduction. Whether the moment argument or software combination is novel requires the other assigned literature audits; TP III alone cannot establish that.

It should not say that TP III lacks reusable transposes, causal scalar averages, duplicate/singular queries, a finite recursive Gaussian evaluator, or rank-free convergence for the smooth polynomial-growth subclass. It should not describe MFP's empirical W2-in-probability mode as uniformly stronger than TP III's a.s. pseudo-Lipschitz empirical convergence. It should distinguish the MFP derivative theorem from a direct limit/derivative interchange: both its physical AD rules and finite rank update lowering are exact before the master theorem is applied.

TP III itself makes no efficient general high-order symbolic compiler claim. MFP's guide expressly disclaims efficient high-order/depth guarantees, performs no numerical quadrature, and leaves generic Gaussian integrals explicit. Its software can be a useful concrete artifact without establishing that these finite graphs are computationally small. No TP III experiment was reproduced; its main examples are analytical spectral-law/NTK calculations.
