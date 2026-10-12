# Positioning complete-trajectory compression against prior work

## Scope

The user's three-phase request is a full-text, adversarial but fair audit of the identified closest literature; comparison with the current manuscript's fully qualified theorem; and proposed introduction/related-work prose. This continues the same study. The subsequent request authorizes rewriting the paper's introduction and related work, adding a separate discussion, and compiling/checking the result. No code/training campaign, book promotion, or external communication is requested.

Permitted inputs are the user-provided notes and PDFs, explicitly assigned current paper/, established docs/, and public primary literature. Other studies and old_docs/ are excluded. The shared checkout is preserved; unrelated migration and other-study changes are untouched. Entry HEAD: 512121f.

## Final outputs

- [review.md](review.md): three-phase synthesis, closest competitors, strongest defensible positioning.
- [claim_ledger.md](claim_ledger.md): five comparative claims, scope corrections, severity/cascade summary.
- [evidence_log.md](evidence_log.md): exact corpus, versions, full-reading coverage, verification limits and manuscript hashes.
- [PROPOSED_INTRODUCTION_RELATED_WORK.md](PROPOSED_INTRODUCTION_RELATED_WORK.md): the earlier proposal, superseded as manuscript prose by the authorized rewrite in `paper/main.tex`.
- Source-specific AUDIT_*.md and universal-compression reports: exact assumptions, proof reconstructions, counterexamples, local repairs, source locations and surviving contributions.

Source PDFs, extractions and rendered checks live only in data/generated/compression_literature_positioning_20261011/. No code-audit artifact is claimed: no research code was supplied for execution or reproduced.

## Completion and assessment

The identified corpus has been read in full, including its supplied appendices. This includes the final 35-page Dyer–Gur-Ari publication, the complete 471-page effective-theory book, the 24-page projected-limit paper, the published 10-page DLDR paper plus its separate one-page appendix, and the 93-page Backward Feature Correction source. The user-requested publication-access gaps are closed. The supplied Huang–Yau proof PDF duplicates the existing 39-page source; the official proceedings page exposes no separate supplement.

Fresh source-only reviewers independently examined the principal theoretical competitors. Complete reading is distinguished from reconstruction: no claim is made to have independently proved every coefficient, audited every cited dependency, or reproduced experiments. Scope differences, conjectural/formal claims, false statements and missing proof steps are classified separately. Several errors admit explicit short repairs; none is used to infer misconduct.

The final synthesis **corrects the initial characterization of Pham–Nguyen's sharp finite-width rate**: it is a claimed quantitative result with a major proof gap, not a verified theorem in this audit. The coupled construction still deserves credit. The old reconnaissance reports remain identifiable below but are not the controlling assessments.

## Supersession map

- HIERARCHIES.md: still controls Huang–Yau, with the coordinator's independently checked integral repair. Its Dyer and partial-book sections are superseded by AUDIT_DYER_FINAL.md and AUDIT_EFFECTIVE_THEORY.md.
- TP_DMFT.md: superseded by AUDIT_TP4.md, AUDIT_DMFT.md, AUDIT_DMFT_FLUCTUATIONS.md and AUDIT_ADAPTIVE_KERNELS.md.
- RIGOROUS_MEANFIELD.md and TRAJECTORIAL_FLUCTUATIONS.md: superseded by AUDIT_NGUYEN_PHAM.md and AUDIT_FLUCTUATIONS.md.
- MEANFIELD_AND_CONTEXT.md: NHL assessment superseded by AUDIT_NHL.md; the Chorin conceptual read remains.
- REDUCTIONS.md: use the detailed final reduction/projected-limit audits for conclusions and current coverage.
- NICHANI_CONTEXT.md: the complete Nichani audit remains; its partial Backward Feature Correction addendum is superseded by AUDIT_BACKWARD_CORRECTION.md.

## Workflow and epistemic boundary

Applied review-ai-paper, solve-math-rigorously and explain-with-canonical-notation with the neural-network reference. The coordinator owns synthesis; source-first readers had neutral frozen-input assignments, not earlier verdicts. The user requested a comparative audit, not official conference scoring.

No reviewed source establishes the manuscript's full conjunction of finite-reference coupling, persistent nonlinear feature learning, small retained state, promised query domain and complete-trajectory accuracy below actual dense-run variability. This is not a global first-priority certificate or a fresh independent proof of the manuscript itself. Its assumptions and its ratio-of-trajectory-suprema interpretation remain explicit.

The literature-audit phase left the paper and maintained book unchanged. At the user's subsequent request, commit `507ca54` checkpointed all then-uncommitted repository material before manuscript editing. Other studies were committed only as authorized repository state, not read as research inputs. The present editorial continuation changes the introduction, related work, discussion and bibliography; the theorem statements and proof modules are preserved.

The completed rewrite adds a six-family comparison table and distinguishes derived response compressibility and closed-loop stability from conditional or formal reductions. A fresh scoped editorial review and correction pass checked its novelty and qualification claims. Extra historical checks fully read the original four-page backpropagation article and the published NTK paper plus supplement. The final PDF compiles to 122 pages with no missing citations/references or overfull/underfull boxes; revised pages were visually checked. Exact comparisons preserve the setup, both theorem statements, initialization proposition, assembly and all proof/figure modules. See the final section of [evidence_log.md](evidence_log.md) for details and limits. The maintained book is unchanged.

## Editorial revision after checkpoint `d0a9968`

The user's next request first checkpointed the current owned manuscript and
study files in `d0a9968`. Other active studies were not incorporated. The
subsequent revision changes the abstract to question–answer form, moves the
result before niche comparisons, introduces the deep/nonlinear/feature-learning
contract and the accuracy-qualified literal-hierarchy contrast, and rephrases
Related work in scientific rather than referee-report language. Discussion no
longer repeats the label-cap and feedback-stability explanations.

Two bounded primary-source reviews supply the missing reduced-regime category:
[lazy and shallow mean field](REDUCED_REGIMES_SHALLOW.md), and
[deep-linear dynamics](REDUCED_REGIMES_LINEAR.md). In particular, the paper
credits balanced deep-linear networks with an exact width-independent
end-to-end matrix flow. A scoped editorial reread checked the revised claims
against the unchanged formal statements. Its corrections make the hierarchy
accuracy target explicit, restore exact-real and zero-readout qualifications
in the abstract, and avoid implying architectural irreducibility from the
activity certificate.

The new experimental-section request is **pending source access**, not complete.
[EXPERIMENT_EDITORIAL_CHECK.md](EXPERIMENT_EDITORIAL_CHECK.md) records what the
current plotting and generation code establishes, and recomputed legacy
prediction discrepancies. Modern figure data are in another study's generated
namespace; the user has been asked for permission to inspect only their direct
data/configuration/producer dependencies. Their existence was checked, but
their contents were not read. The main plotting labels identify 8×8 Digits,
not raw MNIST; the older MNIST Legendre bundle does not establish a modern
Taylor/MNIST result. No new training or empirical reproduction was launched.
The unit-label sentence in the introduction is supported directly by the
saved circle labels in `paper/figures/response_memory_source.npz`.

The revised PDF is built in this study's `revision_build/` directory and
published as `paper/main.pdf`: 122 pages, no unresolved references/citations
or overfull/underfull boxes. The pre-existing `amsmath` warning remains.
Setup/main results and all material from the first proof input onward match
`d0a9968` exactly. Next authorized work is finalizing the modern experimental
section after its source-access question is resolved; no campaign expansion
is proposed.
