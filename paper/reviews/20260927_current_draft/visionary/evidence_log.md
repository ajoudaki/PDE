# Evidence log — visionary scientific review

## Review Format Resolution

Author-requested, author-owned, venue-neutral feedback under `../ASSIGNMENT.md`, accessed 2026-09-27. No numerical score or acceptance recommendation. The review-ai-paper skill and its complete severity rubric were read before claim classification. The assignment authorizes ingestion; no confidential venue assignment or external-review policy is implicated. This review uses only the frozen `../inputs/`, the neutral assignment, required instructions, and three cited public primary sources. No other role's output, studies, book, repository history, or live manuscript was read. No manuscript edits or training runs were made.

## Inventory and read coverage

- Main submission: `inputs/main.tex` (1,954 lines), `main.pdf` (41 pages), `main_extracted.txt`; all manuscript text read, including the inline bibliography and appendices A–I.
- Included appendices: complete `comparison_appendix.tex` (390 lines) and `sphere_appendix.tex` (29 lines).
- Bibliography: complete `references.bib`; the compiled manuscript's inline bibliography controls its actual citations.
- Static code: complete `figures/capture_trajectory.py`, `figures/frozen_ntk.py`, `figures/learning_controls.py`, and `scripts/tikz_figures.py`.
- All 31 entries in `manifest.json` exist and match their recorded SHA-256 hashes. The initial `rg --files` listing omitted ignored NPZs; direct manifest verification found all six supplied NPZ bundles.
- Data: schemas of all six NPZ bundles inspected with `allow_pickle=False`; saved-array checks described below. The three capture manifests and relevant embedded metadata were inspected. Source provenance fields were treated as supplied records, not independently verified history.
- Visual coverage: all 41 manuscript pages rendered with `pdftoppm`, reviewed in seven contact sheets; pages 2, 9, 14, and 37 additionally inspected individually for the mechanism, moment notation, control plot, order trends, and MNIST residuals. Figures are legible and distinguish fitted endpoints, shared times, numerical sensitivity, and output rescalings. Source equations were read in TeX, avoiding reliance on OCR.

### Missing inputs and limits

The frozen packet contains plotting data and capture wrappers, not the underlying response-memory training engines, direct-factor trainer, all original training records, or the full joint-clock/dictionary sweeps. `capture_trajectory.py:33,57–69` names an external archived engine; `learning_controls.py:26,91–118` names external factor records. Those paths were not followed. This is a limit of the deliberately paper-only review packet, not evidence that these resources are absent from the repository or an eventual release. Full training reproduction, the 1,000-image MNIST claim, the dictionary comparison, and the 82-configuration joint-clock summary remain independently unverified here.

## A. Critical citations: theoretical dependencies

The main convergence proofs are self-contained: no external neural limit theorem is needed for Theorems 6.1–6.2. I re-derived the projection-energy identity, product defect, Legendre tail estimate, feedback step, and continuation structure directly.

1. **Gu et al., HiPPO**, [arXiv PDF](https://arxiv.org/pdf/2008.07669), retrieved 2026-09-27; PDF identifies v2, October 2020. Relevant full-text locations: Definition 1, Theorem 2, §3, Appendix D.3. The source provides online polynomial projection of an input signal and its coefficient ODE. After normalization and replacing physical time by the learning clock, this supports the borrowed Legendre-memory ingredient. It does not establish stability of the manuscript's reconstructed neural-gradient-flow feedback. Invocation valid as attribution; shared projection machinery does not subsume the present theorem. The manuscript separately proves its tail bound. An attempted v3 HTML URL returned 404; the PDF succeeded.

2. **Huang–Yau, Neural Tangent Hierarchy**, [arXiv PDF](https://arxiv.org/pdf/1909.08156), retrieved 2026-09-27, current PDF served by the cited unversioned identifier. Relevant text: Assumptions 2.1–2.2, Theorem 2.6, equations (2.7)–(2.10), Corollary 2.4. The stated derivative orders, independent-input-subset requirement, even truncation, kernel lower bound, horizon, and output-error powers agree with Appendix E.2 after exchanging width/sample notation. Preconditions are modified/incomparable for the manuscript's mobility scaling; circle triples violate the source's independence condition. The draft correctly declines to transfer the guarantee. Table 1's specific `n^{-1/2}` characterization should be replaced by “width-suppressed corrections”: the cited source gives an `O(n^{-1})` kernel-velocity estimate in its own width notation. Attempted v2 HTML failed; PDF succeeded.

## B. Critical citations: empirical baselines or methodology

3. **Bordelon–Pehlevan, DMFT**, [full text, v3](https://arxiv.org/html/2205.09653v3), retrieved 2026-09-27. Checked §2 equations (1)–(4), §3 equations (9)–(10), Appendix B Algorithm 1. The source evolves feature/gradient covariance and response kernels over sample/time pairs and samples conditional paths. This supports the chosen direct-grid representation in Appendix E.3. The draft's streamed storage and solver-error allocations are its own conditional analysis, rather than a source convergence theorem. Matching requires the stated coordinate/mobility change and matching initialization law. Invocation valid at that scope; no framework-wide memory lower bound follows.

The frozen empirical kernel is computed from the manuscript's network, so its algebra can be checked directly without importing published benchmark numbers. Full training-engine equivalence is outside the packet.

## C. Potentially missing citations or baselines

No new omission is asserted. This was not a broad novelty search. Nguyen–Pham, Tensor Programs IV, the finite-width DMFT extension, and the deep-linear literature were not independently audited in this focused pass. Their general contextual descriptions should not be read as fully verified here. Population rates A1–A4 are explicitly hypotheses, and the main fixed-width proof does not depend on them.

## Internal mathematical verification

- **Theorem 6.1, pp. 18–21:** loss dissipation bounds dense path length on a compact horizon; local smoothness provides finite compact response bounds. Differentiating the projection energy leaves `rho*||q-q*||²`. Differentiating reconstruction gives exactly `F+E`, with `E` the endpoint-error outer product. Cauchy–Schwarz therefore controls integrated absolute velocity defect, not merely signed endpoint error. Endpoint norm `P/sqrt(tau)` yields an apparent `P²` factor that cancels the squared Legendre tail factor in the layer recursion; the displayed bound `(19)` is consistent. The first-exit argument then closes. Bounded activations/readout control allows all fixed P. No central mathematical error found; undefined `H` and `K` are localized notation mistakes (L1).
- **Theorem 6.2, pp. 21–25:** matching both initial histories is essential to continuity. Weighted projection retains the same defect identity; coarse total variation bounds precede the clock bound. Residual positivity is first established on the dense path, then maintained by stopping/first exit. The velocity formula is independent of clock speed, so its directional evaluation is explicit. The prefix makes the fixed-order Gram positive definite. Its conditioning need not be uniform in P; the text correctly limits what is proved. No circular clock assumption found.
- **Rank consequence:** LS correction is a sum of mP outer products. The joint correction includes the subtracted prefix and has rank at most m(P+1), consistent with Corollary 6.3. Compression gain requires a separate `mP<n` or state-budget `2mP<n` condition; the theorem itself does not guarantee it.
- **Appendix E:** checked error allocation calculus, matched-NTH recurrence and factorial/geometric specialization, scalar NTH example, streamed-DMFT arithmetic interpretation, and the weighted Jackson argument. These are sufficient representation costs under stated assumptions, not universal complexity lower bounds.
- **Appendices C–D:** read in full but not verified as complete theorems. C invokes a reference-trajectory exponential tail estimate without giving or citing its proof. D summarizes a colored-Fock-space construction, trace-class control, word-statistic convergence, and Euler convergence in one paragraph rather than supplying them. The graph-independence/noncancellation step in D.2 is also a sketch. These are proof-coverage gaps in the supplied manuscript, not established counterexamples (M1).

## Executed checks

Working directory for numerical checks: this role directory. Environment: Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0, Pillow 9.0.1. Torch, PyMuPDF, SymPy and pypdf unavailable. No dependencies installed.

1. A read-only Python manifest loop computed SHA-256 for all declared files: all matched. Its subsequent optional `import fitz` failed; no PDF conclusion was drawn from that attempt.
2. `pdftoppm -scale-to 1150 -png main.pdf /home/amir/Codes/PDE/paper/reviews/20260927_current_draft/visionary/page`, cwd `../inputs`, exit 0. A Pillow script assembled contact sheets.
3. `python check_saved_evidence.py`, cwd this directory, exit 0. Exact complete command logic is retained in that script; output is `saved_evidence_checks.json`. It imports no submitted code, performs no training, and reads only frozen arrays. It reproduces all Table 2 discrepancies, the 100-image MNIST numbers, sphere numbers, 39-time RMS and sensitivity arrays, five-task control numbers, and the 29 wins/28 wins over two from saved factor metadata. Control predictions reconstruct from saved cross-kernels/alpha to at most `3.73e-9` absolute difference. Independent degree-1–8 Legendre checks have maximum residual `2.85e-14`; a quadrature product-defect check has residual `4.57e-16`. These numerical identities supplement, rather than prove, the algebra.
4. Attempts to save the three public PDFs with Python `urllib.request.urlopen` failed because shell DNS was unavailable. Web full-text access succeeded; no local source PDFs are claimed to have been saved.

## Findings that inform the final assessment

- **M1:** supporting population/operator theorem proofs are incomplete at identifiable nontrivial steps; main finite-width theorems are independent.
- **L1:** undefined `H` in `(13)`, undefined `K` in `(22),(31),(32)`, and overloaded history/moment notation in Appendix B.
- **L2:** Table 1 mixes theorem scopes and conditional rates more tersely than Appendix E; its NTH correction exponent needs correction.
- **L3:** specify the actual small-readout law and report kernel fitting times/block traces from existing records. On quadrant-alternating, the frozen fit time is about `7.09e7` versus memory `244`; initial first/middle kernel block traces total about `1.06e-6` against readout `1.89`. This contextualizes, and does not invalidate, the matched-initialization control.
- **L4:** call the main MNIST example “3 versus 8” on first mention; report training-time vs fitted-function evidence separately as already done; correct the stated 1.5–3 orders to approximately 1.5–3.5 for the supplied shallow data.
- **L5:** lead with the concrete dynamical-memory result and move the Turing-machine analogy after it; preserve ambition while distinguishing the proved closure from its conjectural population significance.
- **L6:** Figure 2 plots normalized Legendre coefficients, whereas the algorithm stores unnormalized moments. State the conversion and distinguish these from full clock histories.
