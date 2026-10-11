# MFP master theorem and compiler: literature positioning

## Question and authorized scope

Identify and fully scrutinize the closest literature to the committed manuscript
`paper_MFP/main.tex` and its bundled compiler; produce a comparison, an evidence-backed
positioning, and suggested introduction/related-work prose. Do not modify the manuscript.
The user's clarification centers the contribution on the master theorem and executable
calculus, not priority for a proof technique. The proposed cavity proof is not part of
this comparison. This is a new study, not a promotion request.

Baseline observed HEAD: `512121ff3e30688935dd4e60318cc1299452a9fc` (2026-10-11).
Permitted research inputs: the specified manuscript/package, established `docs/` and
`code/`, this study's own artifacts, and primary external literature and software.
No other studies' research is an input. Generated sources, extracts and logs belong in
`data/generated/mfp_literature_positioning_20261011/`.

## Deliverables and conclusion

The main deliverable is [literature_review.md](literature_review.md): the qualitatively
selected shortlist, common comparison, supported contribution, rejected novelty claims,
proof findings, evidence limits and proposed framing. [manuscript_assessment.md](manuscript_assessment.md)
records the actual MFP theorem and compiler contract.

The evidence supports an explicit, executable calculus with a constructive correctness
theorem for its declared derivative/update language. It does not support a first general
Gaussian-program master theorem, first feature-learning limit, first higher-order kernel
calculus, or first symbolic Gaussian expectation engine. The existing manuscript's
disclaimer of a new general probabilistic theorem is appropriate. The alternative cavity
proof is not needed for this contribution-level comparison and was not read here.

Complete-paper reports:

- [Tensor Programs III](review_tp3.md).
- [Non-Gaussian Tensor Programs](review_nongaus.md).
- [Tensor Programs IV](review_tp4.md).
- [Tensor Programs IVb](review_tp4b.md).
- [Neural tangent hierarchy](review_nth.md).
- [Label-Aware NTK](review_lantk.md).
- [Dyer and Aitken diagram papers](review_feynman.md).
- [Neural Tangents and software alternatives](review_software.md).

Fresh isolated checks:

- [MFP theorem/compiler bridge](independent_mfp_audit.md): complete manuscript and guide,
  with no substantive gap or claimed-example scope violation identified; bounded review,
  not a formal proof certificate.
- [NTH, NGTP and LANTK passages](independent_proof_checks.md): independently reconstructed
  counterexamples, corrections and exact consequences.
- [TP IV and diagram formulas](independent_formula_checks.md): separate finite algebra
  and asymptotic checks, with limited repairs distinguished from complete theorem proofs.

Suggested manuscript prose is separate and has **not** been installed:

- [proposed_introduction.tex](proposed_introduction.tex).
- [proposed_related_work.tex](proposed_related_work.tex).
- [references.bib](references.bib).
- [proposed_framing.tex](proposed_framing.tex), the standalone wrapper.
- [Compiled framing PDF](/home/amir/Codes/PDE/data/generated/mfp_literature_positioning_20261011/framing/proposed_framing.pdf).

The individual reports contain primary source links, versions, exact locations, hashes,
coverage, proof reconstruction and unverified dependencies. [source_inventory.json](source_inventory.json)
indexes frozen downloads and validation outputs. File presence is not a claim that every
version or supplementary software file was completely read.

## Validation and residual limits

All 72 bundled MFP tests passed. The calculus, symbolic/cubic MLP derivative, and all
three second-order kernel-jet example variants regenerated successfully. Logs, commands,
source/output hashes and runtimes are under `data/generated/mfp_literature_positioning_20261011/`.
The independent MFP reviewer additionally ran all 41 compiler tests. Small Tensorgrad
symbolic examples were executed; paper training experiments and numerical software suites
were not reproduced. There is no comparative performance benchmark or speed claim.

The complete accessible primary version of every shortlisted paper was read, including
appendices. Important access limits remain: Dyer's final ICLR PDF was blocked by a browser
challenge, so its conference-version comparison is incomplete; TP IVb's separate ICLR
PDF was likewise inaccessible; the final NTH conference appendix was not separately
available, so its proof audit concerns the complete arXiv
appendices. Some external ReLU/spectral dependencies and some broader theorem proof
branches remain explicitly uncertified. Complete reading is not complete verification.

Reproduce the MFP validation from `paper_MFP/`:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=code python -B -m unittest discover -s code/tests -p 'test_mfp_*.py' -v
```

Rebuild the separate proposed prose from this study directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/home/amir/Codes/PDE/data/generated/mfp_literature_positioning_20261011/framing proposed_framing.tex
```

## Ownership and validation

Root owns this README, manuscript assessment, synthesis, bibliography and proposed prose.
Scoped reviewers own separately named reports and generated source namespaces.
No book, compiler, manuscript, Git index, or other-study changes are authorized here.
Checks distinguish complete reading from complete verification and reported experiments
from reproduced experiments. Current status: completed review, with the access and
verification limits recorded above and in the individual reports.
No manuscript, established theory, maintained compiler, Git index, or other-study files
were changed by this task. This is a literature study, not promotion approval or Lean
verification. No commit was created for this new study.
