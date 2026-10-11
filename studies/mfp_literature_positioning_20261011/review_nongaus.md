# Scoped audit: Golikov–Yang, Non-Gaussian Tensor Programs

Frozen review, 2026-10-11. Scope: the complete NeurIPS 2022 paper and its complete supplement, with selected primary version and dependency checks, compared with the assigned MFP theory and interface. No other studies, reports, Git history, or implementation files were used. The canonical-notation skill, its neural-network reference, and solve-math-rigorously were read and applied.

## Conclusion

**For MFP's fixed Gaussian roots, fixed deterministic initial scalars, and polynomially smooth finite programs, the probabilistic foundation is already available from TP3's Gaussian scalar-feedback theorem together with NGTP Appendix J.** This route avoids NGTP's interpolation/backpropagation argument entirely. In particular, all finite scalar moments and expectation convergence are not a new MFP extension. Matrix reuse, transposes, scalar averages feeding later computations, and singular query Grams are within the relevant prior framework.

There are genuine defects in the published NGTP statements/proof, including a missing uniform-moment condition for width-dependent initial scalars and an incorrect backpropagation recurrence for chains of scalar feedback. They deserve accurate reporting but do **not** establish that MFP supplies a new general probabilistic theorem. The first defect is outside MFP's fixed deterministic-scalar assumptions. The second is bypassed in the Gaussian specialization and repaired by ordinary reverse differentiation with scalar adjoints.

MFP's defensible distinction from this paper is its explicit typed derivative language, exact lowering of represented updates, physical-versus-source derivative conventions, finite moving-flow jets, restricted activation-moment normal form, and executable symbolic interface. This audit establishes absence of those complete deliverables in NGTP; it does not establish their novelty against all literature. The existing MFP introduction already says it does not claim a new general probabilistic program theorem, which is the appropriate positioning.

## Source freeze and coverage

All generated files are in `data/generated/mfp_literature_positioning_20261011/nongaus/`. PDF page numbers below are one-based. The supplement's PDF pages 1–33 carry printed pages 14–46.

| Source | Version and coverage | SHA-256 |
|---|---|---|
| [NeurIPS main PDF](https://papers.nips.cc/paper_files/paper/2022/file/8707924df5e207fa496f729f49069446-Paper-Conference.pdf), `neurips-main.pdf` | 13 pages; all read, including references and checklist. PDF metadata modification 2023-01-14. | `05569ae157ef8e5adb43cadcae39426949ba1f855112a227c7145ea9639d3dac` |
| [Official supplemental archive](https://papers.nips.cc/paper_files/paper/2022/file/8707924df5e207fa496f729f49069446-Supplemental-Conference.zip), `neurips-supp.zip` | Archive listing inspected; `appendix.pdf` extracted. Supplied experiment notebooks/scripts not executed or audited. | `dc450374fccac0b016ec3720e1b84b08b73e5e4a3a9a54b16478893b5e1a3af2` |
| `appendix.pdf` from that archive | 33 pages; all Appendices A–N read. J and K–M checked in detail. Printed p39 rendered and visually checked against extraction. | `d72e99b926952aa133d28f21216783f46ea652c5877a68bd5d765563a7f4adb8` |
| [OpenReview reference mFynAUJ0On](https://openreview.net/references/pdf?id=mFynAUJ0On), `openreview-old.pdf` | 41-page line-numbered earlier manuscript; targeted version comparison only, especially p3. Not a complete second proof audit. | `24aa64245bf0469e3746971dab48c93f2bac5a393480f1bab7a80e449d670f38` |
| [OpenReview reference VOvpARqWV](https://openreview.net/references/pdf?id=VOvpARqWV), `openreview-revision.pdf` | 46-page reference manuscript; targeted checks of Setup 3.6/Theorem 3.7 and Appendix K p39. Not a complete second proof audit. | `9f0702014afbff70c7c2457be01f5cda4ce1cb590bab3cdd20185f1dd641f7cb` |
| [TP3](https://arxiv.org/abs/2009.10685), `TP3.pdf` | arXiv:2009.10685v3, 2021-05-08; 87 pages. Selected primary dependency: pp7–9, 25–26, 29–30, 33. Checked theorem assumptions and evaluation rule, not complete TP3 proof. | `6b0d6504c12373e6837de0aff5ab77bb18675a225fcda10d59b56540ec74b5da` |

Matching layout text files and page indexes were saved, together with `TP3-selected-pages.txt`, `version-comparison-selected.txt`, and `appendix-page39.png`. The current OpenReview forum and current PDF endpoints were inaccessible; the reference PDFs were accessible. The official main paper directs readers to an arXiv version but supplies no identifier. Exact-title searches did not locate that version or a correction notice. Thus this is an audit of the frozen official proceedings, not a certification that no later correction exists. OpenReview's reference endpoint returned only a bibliographic reference, insufficient for an exhaustive dated revision history; saved as `openreview-revisions.json`.

Repository comparison used the assigned `docs/02-gaussian-reuse.qmd` material, the corresponding substantive theorem, moment, derivative, worked-program, and bounded-foundation passages in `paper_MFP/main.tex`, and `code/MFP_CALCULUS.md`. This was a mathematical positioning audit, not a fresh independent verification of every MFP proof or its implementation/tests. No book, manuscript, code, or Git mutation was made.

## Exact scope and logical dependencies

NGTP Definition 3.1, Eq. (4), p4, fixes a finite number of matrices, initial vectors, initial scalars, and instructions. At instruction (i), a coordinate expression (x^i_\alpha=\phi^i(g^1_\alpha,\ldots,g^{i-1}_\alpha;c^1,\ldots,c^{i-1})) produces both (g^i=W^ix^i) and (c^i=n^{-1}\sum_\alpha x^i_\alpha); unused outputs can be ignored. Each (W^i) is a named matrix or its transpose. Appendix E, printed p23, identifies this with NETSOR-transpose-plus. Thus causal scalar feedback is explicitly permitted, rather than an inferred extension from a theorem about vectors alone.

Setup 3.6, p6, inherits Gaussian initial vectors and almost-surely convergent initial scalars from Setup 3.3, p5. Matrix entries are independent, centered, variance (1/n), with width-uniform scaled higher-moment bounds; they need not be identically distributed. Coordinate maps are (C^\infty), with every partial derivative polynomially bounded (Definition 3.5). The text additionally asks only that initial scalar moments exist; the missing uniformity is treated below. Gaussian tuples with fixed means and singular covariance are represented by fixed affine maps of independent standard Gaussian roots, as footnote 10, p5, explains for general Gaussian tuples. MFP's assumptions fit this special case.

Theorem 3.7, p6, states almost-sure and (L^p) convergence for every fixed finite (p\ge1), of every program scalar to the Gaussian-program limit. This is stronger in convergence mode than MFP's scalar statement. It is not merely weak convergence or almost-sure convergence without expectation control. All order, graph-size, and time-step parameters remain fixed before (n\to\infty). The informal training language on pp2–4 must be read with that quantifier, not as uniformity in an increasing number of training steps.

The proof's main dependencies are:

1. The Gaussian scalar limit, invoked as Theorem 3.4. The directly applicable primary statement is TP3 Theorem E.15, p33, with Setup E.2 and Definition E.3, pp29–30. It allows scalar feedback and pseudo-Lipschitz nonlinearities/tests without rank stability. A smooth map with polynomially growing first derivatives satisfies the needed pseudo-Lipschitz inequality by integrating its derivative along the segment between arguments.
2. The raw-entry a priori moment bound J.3/J.6, printed p32, proved in J.1–J.4, pp33–38.
3. The backpropagation representation K.1–K.5, pp39–40, used to strengthen scalar raw-entry derivatives to (O(n^{-1})) in (L^p) in K.6, Eq. (70), p40. K.7, p41, bounds products of those derivatives.
4. The interpolation (A(t)=\widetilde A\cos(\pi t/2)+A\sin(\pi t/2)), Definition 5.1/Eq. (7), p9. Lemma 5.3 and Appendix G give \(\mathbb E\dot a=\mathbb E[a\dot a]=0\) and scaled mixed moments. Appendix L, pp41–43, combines these cancellations with K.7 to prove \(\sup_t\mathbb E|\dot c(t)|^p=O(n^{-p/2})\).
5. Integrating in (t) and using an exponent (p>2) gives a summable Markov bound for the non-Gaussian/Gaussian scalar difference; Borel–Cantelli then transfers almost-sure limits. Appendix M, p43, uses a uniformly bounded moment of order (q>p) to obtain (L^p) convergence.

The Gaussian MFP specialization needs only items 1, 2, and the elementary uniform-integrability step in item 5. It does not need the disputed Appendix K recursion or the non-Gaussian interpolation theorem as a black box.

## Appendix J: proof mechanics verified

Setup J.2, printed p32, relaxes matrix variances to heterogeneous values bounded by \(\nu_2/n\), preserving centered independent entries and scaled higher-moment bounds. This strengthened induction is intentional: its use at shrunken or zero entries is explained in Remark J.4 and executed on p38.

The proof simultaneously establishes every fixed derivative order and every finite moment at each program node. Coordinate compositions use the finite higher-order chain/product rules and Hölder; normalized averages use Jensen (Proposition J.7). Scalar feedback is included in the argument vector in Claims 1–2 and Proposition J.8; it is not silently frozen.

For a matrix call, the product rule produces
\[
\partial^P g_\alpha^j=\sum_\beta W^j_{\alpha\beta}\partial^P x_\beta^j+R_\alpha,
\]
with only finitely many earlier-node terms in (R_\alpha) (J.4, p36). For an even (p)-th moment of the sum, let an index multiset have (b) distinct elements and (k) singleton elements. Write its matrix and earlier-node products as (w^Nz^N). Taylor expansion in the finitely many selected raw entries, at zero, through degree (k-1) kills every polynomial term by centering and independence. The remainder has (k) additional entry factors. Cauchy–Schwarz gives the size
\[
|\mathbb E[w^Nz^N]|\le Cn^{-(p+k)/2}\le Cn^{-b},
\qquad p+k\ge2b.
\]
There are (O(n^b)) tuples of each equality pattern; the number of patterns is finite at fixed (p). Lemma I.4 supplies the resulting uniform moment bound. This is the same substantive cancellation mechanism used and explicitly credited in MFP.

The derivative in \(\nabla^k z^N(tv)\) is a derivative of the original deterministic function, evaluated after entry shrinkage. It is **not** a derivative of the composite (v\mapsto z^N(tv)). No missing factors of (t), no division by (t), and no inverse query Gram are needed. Selected entries are shrunk consistently in every matrix reuse/transposed use. The proof's uniform smoothness-profile and input-moment constants make the strengthened induction applicable. This core argument is valid for MFP's fixed deterministic scalars.

Minor local repairs: the no-singleton case (k=0) cannot literally use the displayed Taylor factorial ((k-1)!); use Cauchy–Schwarz directly, with (p\ge2b). The remainder label on p37 says (R_{k+1}) after choosing order (k-1), while the subsequent derivative order is correctly (k). J.2, p35, bounds random scalar powers pointwise by moment bounds; that line should be placed inside an expectation with Hölder/Jensen. These repairs do not require new estimates.

J.3 gives \(\sup_{n,\alpha}\mathbb E|v_{n,\alpha}|^r<\infty\). Therefore, for fixed (p,q\ge1),
\[
\mathbb E\left(n^{-1}\sum_\alpha|v_{n,\alpha}|^p\right)^q
\le n^{-1}\sum_\alpha\mathbb E|v_{n,\alpha}|^{pq}\le C_{p,q}.
\]
This is exactly the type of vector-node bound stated in MFP. J.6 gives scalar-node bounds. The Gaussian theorem supplies scalar convergence, and these bounds supply every finite (L^p) limit.

For completeness, the empirical (\mathcal W_2) conclusion is likewise a routine consequence: apply the Gaussian theorem to a countable convergence-determining family of smooth compactly supported tests and to the squared Euclidean norm of a fixed same-type tuple. The former determines weak convergence and the latter second-moment convergence; together they determine quadratic Wasserstein convergence. This is not a distinct probabilistic obstruction overcome by MFP.

## Consequential defects, with explicit examples

### 1. Width-dependent initial scalars: the published theorem is false under its literal moment wording

Let (B_n\) be independent Bernoulli variables with \(\Pr(B_n=1)=n^{-2}\), (n\ge2), independent of roots and matrices, and set (c_n=n^2B_n). Then
\[
c_n\longrightarrow0\quad\text{almost surely},\qquad
\mathbb E|c_n|^q=n^{2q-2}<\infty\quad\text{for every fixed }n,q,
\]
because the event probabilities are summable. But \(\mathbb E|c_n|=1\), so (c_n\not\to0) in (L^1). It meets Setup 3.6's literal initial-scalar conditions and contradicts Theorem 3.7's claim for every scalar. If “every scalar” is interpreted as excluding initial ones, choose the next coordinate map to return the scalar argument; its average is again (c_n). All maps are linear and all matrices can be Gaussian.

The proof actually fixes constants (R_q\) with \(\sup_n\mathbb E|c_n|^q\le R_q\) for every initial scalar: Definition J.1(c), p32, and J.1, p33. The missing hypothesis is therefore visible within the paper. Add uniform all-moment bounds (or an appropriately sufficient stronger input condition) to restore this part. MFP's fixed deterministic initial scalars satisfy them automatically. This is a false overly broad published statement, not evidence against its fixed-input specialization.

### 2. Appendix K's printed backpropagation misses a chain of scalar feedback

Take (M_0=1), any unused standard Gaussian root (g^1), deterministic (c^1=0), one matrix (A), and (W^2=W^3=W^4=A). Use
\[
\phi^2=1,\qquad \phi^3(g;c)=g^2,\qquad \phi^4(g;c)=c^3.
\]
Thus (x^2=\mathbf1\), (g^2=A\mathbf1\), (c^2=1\), (x^3=g^2\), (c^3=\langle g^2\rangle\), (x^4=c^3\mathbf1\), and (c^4=c^3\), where \(\langle v\rangle=n^{-1}\sum_\alpha v_\alpha\). Let the objective in Eq. (67) be \(c=\langle\psi\rangle\) with \(\psi(g;c)=c^4\). Then
\[
c=\frac1n\mathbf1^TA\mathbf1,
\qquad n\nabla_{g^2}c=\mathbf1,
\qquad \frac{\partial c}{\partial A_{\alpha\beta}}=\frac1n.
\]

In the paper's notation the only nonzero partials needed are (x^3_{2;}=\mathbf1\), (x^4_{;3}=\mathbf1\), (x^5_{;4}=\mathbf1\), with (dx^5=\mathbf1\). Eq. (68) gives (dg^4=0\) and (dg^3=0\), hence Eq. (69) gives (dx^4=dx^3=0\). For (dg^2\), the only direct vector contribution is (x^3_{2;}\odot dx^3=0\); the only potentially useful scalar term has (k=3\), but (j=4\) multiplies (dx^4=0\), and (j=5\) has (x^5_{;3}=0\). Thus (dg^2=0\). Proposition K.2 then predicts a zero matrix derivative, contradicting the displayed exact derivative.

This disproves Proposition K.1's (dg) assertion and the resulting K.2 formula using the printed (dg), at every finite (n). The omission is the path (g^2\to c^3\to c^4\to c\). The example uses only linear maps, so it cannot be blamed on polynomial growth, nonsmoothness, singularity, or limiting operations. Printed p39 was inspected visually to exclude an OCR artifact. The 46-page OpenReview reference has the same recurrence, numbered (70)–(71).

The dependency impact is precise: K.6 invokes K.2, K.7 invokes K.6, and L.1 invokes K.7. Therefore the full scalar-feedback interpolation proof is incomplete as printed. **The example does not contradict K.6's bound or the master limiting conclusion.** Here the true scalar is Gaussian of variance (1/n\), and its claimed limit is indeed zero.

A repair uses scalar adjoints explicitly. For each instruction (g^i=W^ix^i\), (c^i=\langle x^i\rangle\), put (b_{g^i}=n\nabla_{g^i}c\), (a_{c^i}=\partial c/\partial c^i\), and
\[
b_{x^i}=W^{iT}b_{g^i}+a_{c^i}\mathbf1.
\]
In reverse instruction order, propagate (b_{g^k}\mathrel{+}=b_{x^i}\odot\partial_{g^k}\phi^i\) and (a_{c^k}\mathrel{+}=\langle b_{x^i}\partial_{c^k}\phi^i\rangle\). Seed the objective with (b_{g^k}=\partial_{g^k}\psi\) and (a_{c^k}=\langle\partial_{c^k}\psi\rangle\). These are again finite allowed operations, with polynomially smooth maps; applying J.3 to the corrected backprogram recovers the K.6 moment argument. MFP's reverse rules contain this scalar-adjoint bookkeeping. This is an elementary repair and clarification, not a new general limit principle.

### 3. Supplementary issues outside the central smooth Gaussian comparison

Appendix D, printed p22 after Eq. (40), infers almost-sure convergence of an interpolation difference from convergence in every (L^p\), citing Borel–Cantelli, without a rate or summable bound. That implication alone is false: independent indicators with probability (1/\log(n+2)\) converge to zero in every finite (L^p\) but equal one infinitely often almost surely. This is an explicit counterexample to the inference, **not** a constructed tensor program refuting Theorem D.2. Its nonsmooth Lipschitz extension is not needed for MFP. A uniform sub-Gaussian scale is also needed for the uniform operator-norm estimates used there; merely saying each width's entries are sub-Gaussian does not state such uniformity.

Proposition I.5, printed p31, drops the centering premise used immediately above it. The deterministic independent entries (x_\alpha=n^{-1/2}\) meet its stated absolute-moment bounds, but their sum is \(\sqrt n\). Thus that proposition is false as printed. The central J proof uses Lemma I.4 with explicitly verified cancellation and centered matrix entries, so this omission does not invalidate J's application.

Appendix A's illustrative p15 Taylor-remainder equality singles out the (y^2z^2\) remainder term even though the remainder coefficients can depend on both variables; termwise centering does not eliminate the other remainder terms as written. The full Appendix L argument bounds the entire derivative tensor and avoids that particular omission. Its zero-singleton case needs the same elementary direct estimate as J. This is not an additional obstruction to the repaired full proof.

## Overlap with MFP, and what remains to claim

| MFP component | Relation to the audited literature |
|---|---|
| Scalar limits in every finite (L^p\), hence expectation limits | NGTP Theorem 3.7 explicitly states them; for the exact Gaussian fixed-input scope they follow independently from TP3 E.15 plus NGTP J.3/J.6. |
| Uniform moments of vector/scalar nodes and raw-entry derivatives | NGTP Appendix J already proves the substantive mechanism with broader centered matrix-entry laws; MFP's version is an attributed Gaussian specialization with more explicit treatment of zero entries and singleton cancellation. |
| Arbitrary finite causal scalar feedback | Explicit in NGTP Eq. (4) and TP3 NETSOR-transpose-plus. The K recurrence defect does not remove it from the language or from J. |
| Reuse, transpose corrections, formal source partials | TP3 Box 1, pp8–9, gives the same Gaussian-plus-response structure. With variance one, MFP's (\xi_h\) corresponds to (\widehat Z^{Wh}\), its output to (Z^{Wh}\), and its response coefficient to (\mathbb E[\partial Z^h/\partial\widehat Z^{W^Tu}]\). Deterministic limiting scalars are held fixed. |
| Singular query Grams | TP3 E.15 explicitly removes rank stability for pseudo-Lipschitz programs; smooth MFP programs fall inside this scope. MFP provides a different self-contained bounded-map/regularization presentation. |
| Finite derivatives, represented gradients and updates | NGTP Appendix K attempts explicit scaled backpropagation, including reused/transposed matrix outer products. Exact AD closure of the smooth finite language and normalized rank-one lowering supply the required compilation. MFP makes those operations and distinctions explicit and implements them; it should not describe prior TP theory as unable to express backward passes or fixed training steps. |
| Fixed-order moving-flow jets and frozen seed semantics | No matching complete user-facing calculus or compiler was found in NGTP. These are potentially useful constructive deliverables, while their finite algebraic closure invokes ordinary differentiation and the existing program theorem. No positive-time or increasing-order limit follows. |
| Activation-derivative moment normal form | NGTP does not give MFP's stated restricted initialization normal-form theorem. Its mathematical novelty requires comparison with other primary sources; this audit alone cannot establish it. |

Because polynomially smooth maps are closed under every fixed finite derivative, MFP's activation assumptions do not create a new regularity class relative to NGTP. MFP is narrower in matrix law, root law, coefficients, and some interface operations. Its stronger presentation of admitted operations and exact output graphs can remain valuable without being presented as a stronger probabilistic foundation.

## Version changes, applications, and reproduction limits

The earlier 41-page line-numbered OpenReview file has Setup 2, p3, explicitly requiring initial scalar moments to exist **and converge**. Its Theorem 2 states convergence in probability, with expectation convergence only under additional linear/quadratic growth restrictions. The 46-page reference and proceedings strengthen the stated conclusion to all finite (L^p\) and almost-sure convergence, allow non-identically distributed matrix entries with uniform scaled moments, and use the current Appendix J–M architecture. In that change, the initial-scalar moment-convergence requirement is absent from Setup 3.6, even though uniform input moments remain needed in J. This is a substantive version difference, not a notation change. Exact revision dates and every intervening edit were not recovered.

The 46-page reference's Appendix K recurrence and initial-scalar wording are unchanged in the material audited here, though equation numbering differs. The proceedings' application section refines the treatment of non-Gaussian vector-like weights through polynomially smooth Gaussian images. Such images are an assumption, not a representation theorem for every distribution with all moments; in particular, a nonconstant two-point law cannot be the continuous image of a full-support one-dimensional Gaussian. This limitation does not affect Gaussian MFP roots.

Appendices C and D were read for convergence distinctions: full expectations, conditional expectations, and almost-sure conditional convergence are kept separate in C.3/C.13 and Conjectures C.5/C.7, printed pp18–20. C.13 specifically identifies the polynomially smooth expectation extension of TP3's Conjecture A.4 (footnote 24, p20). No general (n^{-1/2}\) rate to the deterministic Gaussian limit is proved there: C.5 labels it a conjecture under strengthened initial-scalar rates. The interpolation rate is a rate between two coupled programs, not automatically that rate to their common limit.

Appendix N reports empirical NNGP/NTK comparisons for RNN/GRU/Transformer examples, using 100 initializations and several weight distributions, including a cube-root-Cauchy distribution outside the all-moment theorem assumptions. Those experiments were **not reproduced** in this audit, and observed convergence is not used to weaken the theorem hypotheses. The main application theorems also depend on TP1/TP2b/TP4 and random-matrix arguments; their complete proofs were not independently re-audited here. Appendix F's comparison to Chen–Lam was read as the authors' comparison; the Chen–Lam paper was not separately verified. Higher-order chain/product identities from Appendix H were checked mathematically as finite calculus identities; Hardy's cited source was not independently fetched.

Recommended paper-level positioning: cite NGTP Theorem 3.7 and Appendix J directly for the established all-moment background, identify the Gaussian source-response rule with TP3, and describe MFP as a constructive typed derivative calculus and implementation with self-contained proofs. If discussing the published defects, include the exact hypotheses and counterexamples above, and make clear that they neither remove the prior Gaussian foundation nor prove general MFP novelty.
