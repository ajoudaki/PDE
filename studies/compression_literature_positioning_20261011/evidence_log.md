# Evidence log

## Review Format Resolution

Public primary literature and an author-owned manuscript; user-requested comparative audit, not a confidential conference review. No scores. Access/review date: 11 October 2026. The review, rigorous-mathematics and canonical-notation workflows guide the checks. A different objective or a restrictive hypothesis is not itself a proof error. Reading an entire document does not certify every theorem or external dependency.

## Inventory and version resolution

The comparison target is paper/main.tex, its included theorem/proof modules and bibliography. The current main text and comparison-relevant statements were read, but this task does **not** independently re-prove the entire manuscript. Public PDFs, complete text extractions and selected rendered pages reside in data/generated/compression_literature_positioning_20261011/. Reports below give source URLs and exact theorem/page/equation locations.

The user's attachments resolve the requested publication gaps:

- Dyer–Gur-Ari: 1183_asymptotics_of_wide_networks_f.pdf is the final **35-page ICLR 2020** publication, not the 37-page arXiv preprint. A fresh reader audited the final version independently.
- DLDR: the two similarly named attachments are the **10-page TPAMI publication** and a **distinct one-page Appendix A–C**. Both were read completely; the supplement was not discarded as a duplicate.
- Huang–Yau: 1909.08156v1.pdf is byte-identical to the already read 39-page proof source. The official proceedings page provides no separate supplement; a hypothetical missing supplement is not a continuing access gap.
- The supplied Yang–Santacroce–Hu **24-page** paper closed its earlier access gap and received an independent full-source audit.

No paper/book edits, Git changes, author communications, code execution or training experiments are part of this audit. Unrelated repository changes are preserved.

## A. Full-source theoretical comparison corpus

“Complete” means sequential extracted-text reading through the document and appendices, with visual inspection of decisive mathematics; it does not mean every page was rendered or every proof independently reconstructed. Earlier reconnaissance reports are superseded by the indicated final audits where they differ.

| Source/version | Coverage | Controlling report |
|---|---|---|
| Wang et al., ICLR 2026 / arXiv:2510.00504v2 | Complete 26 pp.; coordinator and fresh independent full reader | [Primary assessment](UNIVERSAL_COMPRESSION.md), [fresh check](UNIVERSAL_FRESH_CHECK.md) |
| Huang–Yau, ICML 2020 + arXiv:1909.08156v1 | Complete 10-page publication and 39-page proof source; coordinator rechecked Appendix B and supplied an integral repair | [HIERARCHIES.md](HIERARCHIES.md), Huang–Yau section and update |
| Dyer–Gur-Ari, final ICLR 2020 | Complete 35 pp., fresh source-only reader; earlier 37-page preprint separately read | [AUDIT_DYER_FINAL.md](AUDIT_DYER_FINAL.md) |
| Roberts–Yaida–Hanin, arXiv:2106.10165v2 | Complete **471 pp.**, including appendices; fresh source-only reader and coordinator reconstruction checks | [AUDIT_EFFECTIVE_THEORY.md](AUDIT_EFFECTIVE_THEORY.md) |
| Yang–Hu, ICML 2021 Tensor Programs IV | Complete 11-page main and 38-page supplement | [AUDIT_TP4.md](AUDIT_TP4.md) |
| Bordelon–Pehlevan DMFT, arXiv:2205.09653v3 | Complete 55 pp.; separate later presentation not silently substituted | [AUDIT_DMFT.md](AUDIT_DMFT.md) |
| Bordelon–Pehlevan fluctuations, arXiv:2304.03408v3 | Complete 44 pp. | [AUDIT_DMFT_FLUCTUATIONS.md](AUDIT_DMFT_FLUCTUATIONS.md) |
| Lauditi–Bordelon–Pehlevan, ICML 2025 | Complete 32 pp. | [AUDIT_ADAPTIVE_KERNELS.md](AUDIT_ADAPTIVE_KERNELS.md) |
| Nguyen–Pham, MSL 2023 | Complete 157 pp., Appendices A–G; fresh source-only reconstruction after initial read | [AUDIT_NGUYEN_PHAM.md](AUDIT_NGUYEN_PHAM.md) |
| Pham–Nguyen, NeurIPS 2021 fluctuations | Complete 13-page main and 45-page supplement; fresh source-only reconstruction | [AUDIT_FLUCTUATIONS.md](AUDIT_FLUCTUATIONS.md) |
| Chen, JMLR 2024 Neural Hilbert Ladders | Complete 65 pp., Appendices A–E; fresh source-only reconstruction | [AUDIT_NHL.md](AUDIT_NHL.md) |
| Yang–Santacroce–Hu, ICLR 2022 | Complete 24 pp., Appendices A–F; independent read and coordinator checks | [AUDIT_PI_LIMIT.md](AUDIT_PI_LIMIT.md) |
| Nichani–Damian–Lee, NeurIPS 2023 | Complete 48 pp. | [NICHANI_CONTEXT.md](NICHANI_CONTEXT.md), main audit, not its superseded partial BFC addendum |
| Allen-Zhu–Li, arXiv:2001.04413v6 | Complete 93 pp., Appendices A–I; fresh source-only reader | [AUDIT_BACKWARD_CORRECTION.md](AUDIT_BACKWARD_CORRECTION.md) |
| Chorin–Hald–Kupferman, PNAS 2000 | Complete 6 pp.; conceptual source, not an imported proof of our theorem | [MEANFIELD_AND_CONTEXT.md](MEANFIELD_AND_CONTEXT.md) |

## B. Full-source algorithmic and empirical comparisons

| Source/version | Coverage | Controlling report |
|---|---|---|
| Liu–Zenke, ICML 2020 Neural Tangent Transfer | Complete 12-page main and 7-page supplement; exact-mask argument independently checked twice | [AUDIT_NTT_AND_SUBSPACES.md](AUDIT_NTT_AND_SUBSPACES.md) |
| Schotthöfer et al., NeurIPS 2022 DLRT | Complete 13-page main and 10-page supplement; coordinator reconstructed comparison counterexample | [AUDIT_DLRT.md](AUDIT_DLRT.md) |
| Li et al., arXiv:1804.08838v1 intrinsic dimension | Complete 23 pp.; source-first reader and coordinator checks | [AUDIT_NTT_AND_SUBSPACES.md](AUDIT_NTT_AND_SUBSPACES.md) |
| Gur-Ari et al., arXiv:1812.04754v1 tiny subspaces | Complete 19 pp.; source-first reader and coordinator checks | [AUDIT_NTT_AND_SUBSPACES.md](AUDIT_NTT_AND_SUBSPACES.md) |
| Dogra–Redman, NeurIPS 2020 Koopman training | Complete 11-page main and 8-page supplement | [AUDIT_NTT_AND_SUBSPACES.md](AUDIT_NTT_AND_SUBSPACES.md) |
| DLDR, published TPAMI 45(3), March 2023 | Complete 10-page final paper and one-page Appendix A–C, coordinator | [AUDIT_DLDR.md](AUDIT_DLDR.md) |
| Freitag–Nicolaus–Redmann, 2023 DEIM reduction | Complete 8 pp., coordinator | [AUDIT_DEIM_DMD.md](AUDIT_DEIM_DMD.md) |
| Tano–Portwood–Ragusa, arXiv:2006.14371 | Complete 13 pp., coordinator | [AUDIT_DEIM_DMD.md](AUDIT_DEIM_DMD.md) |
| NTK-SAP, arXiv:2304.02840v1 | Complete 32 pp., coordinator | [AUDIT_NTK_SAP.md](AUDIT_NTK_SAP.md) |

These are the identified, bounded audit corpus—not every publication in each paper's bibliography. Broad pruning, distillation, SNIP, shallow/kernel/linear learning remain contextual families; mentioning them does not imply a new full-paper audit. No additional campaign was started to inflate the source count.

All experimental results discussed are **author-reported, not reproduced**. Source text can reveal the protocol and resource accounting; it cannot establish undocumented implementation behavior. No research code was supplied for this audit or executed. Code-tree metadata inspected while locating PDFs is not a code audit. Therefore no completed code-audit report is claimed.

## C. Critical dependency and cross-check record

The strongest findings use explicit in-scope calculations rather than citation-by-reputation. Examples include the determinant/rank counterexample to universal compression's local theorem; the positive-semidefinite obstruction to exact NTT masking; a long-time DLRT counterexample satisfying its abstract gradient assumptions; the mean-field pair-sampling variance calculation; the exact random-feature inverse expansion in the effective-theory book; and a reconstruction of Huang–Yau's disputed estimate by repeated integration.

External dependencies inspected selectively include the DLRT integrator's actual time-dependent constants, the TP master theorem needed for the fixed-step limit, and the concentration/operator statements identified in the source-specific reports. These checks are **not** full audits of those entire dependency papers. When an alternative elementary proof is given, the report states which dependency it replaces and which obligations remain. No unverified dependency is imported into our manuscript.

Independent reviewers received frozen source assignments without earlier verdicts. Coordinating synthesis uses their reports plus source checks; it does not pretend every document had multiple independent full readers. Important corrections to the initial pass are propagated: the 2021 fluctuation paper's sharp rate is now a **stated claim with a major proof gap**, not a certified predecessor theorem; the book and projected-limit paper are no longer coverage gaps; final Dyer and DLDR publications control their comparisons.

## Manuscript scope and preservation

The target has fixed depth, strip-analytic activations (unbounded values permitted under its derivative bounds), Gaussian dense initialization with zero readout, specified layer mobilities, a positive population feature-Gram gap and a nonzero width-independent small-label cap. Its comparison is a **ratio of two complete-trajectory supremum norms**, not a per-time ratio or an endpoint-only lower bound. Taylor uses setup-declared input panels; Harmonic covers the sphere. Legendre counts moving state and retains dense fixed mixers. Efficient setup costs distinguish a supplied explicit matrix from a freshly generated implicit Gaussian reference. Early-time nonlinear/own-NTK certificates retain local additional assumptions.

Snapshot SHA-256 values at the end of the audit phase, before the subsequently authorized manuscript rewrite:

- paper/main.tex: 88d991be90071416da848836f68e0acadb9dc0d4af7143733674cff9b2c0b4a3
- paper/references.bib: 17aa71c11019200f7acbe2e84eec9e1c4f5666757cd6b36e80dcdf7b6cc33e59
- paper/compact_nth.tex: d7400e958da2e72b0eb450ee1b628e64b5b3118d9637f1bbf7681b1942f3f246
- paper/feature_learning_theorem.tex: f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f

## Remaining verification limits

The named publication-access gaps are closed. Reconstruction is concentrated on claims affecting novelty, quantifiers, state size and the main proof chains; every unrelated coefficient and reference has not been independently proved. Numerical evidence is not reproduced. The comparison is neither a global first-priority proof nor an independent certificate of our own entire theorem. Source-specific unresolved mathematical obligations are recorded as such, not converted into blanket claims of falsity or misconduct.

## Authorized manuscript integration, 2026-10-11

The user authorized a forceful, citation-backed introduction, a related-work comparison and a separate philosophical discussion. Rollback checkpoint `507ca54` preceded all manuscript edits. The new text is in `paper/main.tex`, with bibliography metadata in `paper/references.bib`. The earlier proposed Markdown prose is historical, not the current manuscript.

The positive framing is a finite sufficient memory for the specified dense learner: derive compressible response geometry, then control its own nonlinear feedback through fitting. The novelty claim is explicitly “to our knowledge” and requires the full conjunction, not priority for feature learning, finite closures, or dynamical compression in general. A six-family comparison table exposes the missing implication in each closest route. The text preserves Taylor's declared-panel contract, Legendre's retained fixed mixers, exact-real accounting, the fixed small-label assumption, and the ratio-of-trajectory-norms interpretation. Early-time feature-learning certificates are not described as all-time activity or endpoint separation.

### Additional historical citation checks

A fresh source-only reader fully read Rumelhart–Hinton–Williams, *Nature* 323, 533–536 (1986), four scanned pages from [Hinton's author copy](https://www.cs.toronto.edu/~hinton/absps/naturebp.pdf), DOI 10.1038/323533a0. Pages 533–535 support learning internal representations through backpropagation; this is historical context and illustrative evidence, not a universal representation-learning theorem or a claim that this paper invented backpropagation.

The same reader fully read Jacot–Gabriel–Hongler's **published NeurIPS 2018** paper (10 pages) and official supplement (8 pages), including mathematical-page renderings. [Main PDF](https://proceedings.neurips.cc/paper_files/paper/2018/file/5a4be1fa34e62bb8a6ec6b91d2462f5a-Paper.pdf), [official supplement](https://proceedings.neurips.cc/paper_files/paper/2018/file/5a4be1fa34e62bb8a6ec6b91d2462f5a-Supplemental.zip). Theorem 2 uses a smooth Lipschitz activation with bounded second derivative, a finite dataset, stochastic boundedness of the integrated training direction on the specified finite interval, and the NTK parameterization. The supplement's proof uses sequential hidden-width limits. Main Remark 4 explains that individual hidden-activation changes vanish but collective lower-layer updates still contribute to the output. Accordingly, the manuscript says **fixed tangent kernel**, not “only the readout learns.” The later arXiv-v4 positivity statement was not imported. Sources and renderings are in the study-owned `cited_papers/` generated directory.

A separate metadata reader verified the added entries against cached source first pages and primary proceedings records. The bibliography cites the audited effective-theory preprint v2 (2021), Backward Feature Correction v6 (2023), and DLDR's 2023 published year rather than its DOI registration year. Existing source audits control the substantive comparisons; this pass is not a new full audit of every historical contextual citation.

### Scoped editorial review and preservation

A fresh reader checked the rewritten three sections against the unchanged setup, main statements and the controlling source-scope reports. Five localized recommendations were applied: disambiguate the early-time activity versus complete-time compression scopes at the first novelty claim; make every predecessor table cell explicit about what is absent or assumed; qualify vanishing kernel-scaling corrections by fixed training time; remove a vague sentence about repairs to competing proofs; remove a repetitive Discussion recap. The reader's final reread found no remaining substantive framing issue within that assigned scope. This was an editorial/citation audit, not a reproof of our theorem or a second full reading of every cited source.

Exact string comparisons against `507ca54:paper/main.tex` confirm unchanged preamble/abstract, the complete Setup and main results block (including the initialization proposition), and everything from the first proof input onward. Git reports no differences in any proof module, feature-learning theorem module or figure module. No new persistent symbol was introduced.

Build command, from `paper/`: `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../data/generated/compression_literature_positioning_20261011/framing_build main.tex`. Final build exits successfully at 122 pages, with no undefined citations/references and no overfull/underfull boxes. The sole remaining warning is the pre-existing `amsmath` notice about `atopwithdelims` in an unchanged proof. The revised front matter and comparison/discussion pages were rendered for visual inspection. The existing theorem/proof content is not counted as newly audited merely because compilation succeeds.
