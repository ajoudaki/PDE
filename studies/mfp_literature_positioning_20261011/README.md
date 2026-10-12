# MFP master theorem and compiler: literature positioning

## Question and authorized scope

Scrutinize the closest literature to `paper_MFP/main.tex` and its bundled compiler,
then develop the strongest evidence-backed framing and suggested introduction and
related work. The user's clarification centers the master theorem and executable
calculus, rather than priority for a proof technique. The alternative cavity proof
was not an input. This is a literature study, not a promotion request; the manuscript
and maintained code were not edited.

Permitted scientific inputs are the specified manuscript/package, established
`docs/` and `code/`, this study's own artifacts, and primary external literature and
software. No other studies' research was used. Generated sources and logs are in
`data/generated/mfp_literature_positioning_20261011/`.

Initial observed HEAD: `512121ff3e30688935dd4e60318cc1299452a9fc`.
Reassessment baseline HEAD: `507ca542f5cc8fed85448aaff740f4025a061a40`.
The reviewed MFP manuscript retains SHA-256
`a43acbc76e53a3437ed5136137fd8e5497a6d65826447c1ac95764a1cba8d38e`.
Concurrent changes outside this study were preserved.

## Current result

The requested substantive reassessment is complete. Start with the
[revised synthesis](literature_review.md) and the
[compiled introduction and related work](/home/amir/Codes/PDE/data/generated/mfp_literature_positioning_20261011/framing_v2/proposed_framing.pdf).

The positive case is a constructive symbolic calculus connecting an admitted neural
derivative query, exact finite-width compilation, a justified Gaussian limit and
an executable implementation. For standard initial MLP jets with polynomial loss,
the reduction closes in activation-derivative moments at the original forward
covariances. Each final activation integral uses at most one coordinate per sample,
independently of fixed depth and derivative order. The number of terms and other
costs can grow. This specialization was derived and independently checked under
the manuscript's scalar-limit theorem.

The probabilistic source-response foundation is already constructive in Tensor
Programs. MFP's defensible contribution is its explicit derivative-query contract,
closure/state semantics, initialization output algebra and executable realization.
The evidence supports a substantive mathematical calculus; it does not establish
priority for a new general Gaussian program limit or for its individual AD and
Gaussian integration operations.

The reassessment corrects the first delivery's underdeveloped positive argument and
adds three close papers: NTK Unlimited / finite-width Feynman diagrams, the updated
nonlinear DMFT treatment, and quantitative Tensor Programs. Twelve shortlisted
papers were read in full in their recorded accessible versions, including appendices
where present. Complete reading is distinguished from complete proof verification.
The individual reports identify assumptions, proof defects, explicit repairs,
external dependencies, software evidence and experimental limits.

## Revised deliverables

- [Synthesis and comparison table](literature_review.md).
- [Suggested introduction](proposed_introduction.tex).
- [Suggested related work](proposed_related_work.tex).
- [Bibliography](references.bib) and [standalone LaTeX wrapper](proposed_framing.tex).
- [Compiled proposed prose, five pages](/home/amir/Codes/PDE/data/generated/mfp_literature_positioning_20261011/framing_v2/proposed_framing.pdf).
- [Source and validation inventory](source_inventory.json).

These are proposals; they have not been installed in the paper or book. The first
synthesis and proposed prose are preserved as `*_v1` files. Their original PDF is
under generated `framing/`; the revised PDF is under `framing_v2/`.

## Fresh reassessments and checks

- [TP IVb: full paper and exact MFP correspondence](reassessment_tp4b.md).
- [MFP theorem, compiler and initial-jet moment reduction](reassessment_calculus.md).
- [Independent initial-jet normal-form check](reassessment_normal_form_check.md).
- [Discovery, ICML 2026 diagrams and NTK Unlimited](reassessment_discovery.md).
- [DMFT: complete journal/conference versions and code](reassessment_dmft.md).
- [Independent DMFT linear-kernel coefficient check](reassessment_dmft_linear_check.md).
- [Quantitative TP: complete paper and proof corrections](reassessment_quantitative_tp.md).
- [Final framing consistency check](reassessment_framing_check.md), explicitly not a
  fresh proof or software certification.
- [Targeted compiler checks](reassessment_calculus_checks.py): order-six moving
  scalar-feedback flow and five-root-to-one-preactivation integration reduction.

The DMFT checks distinguish its sound full response calculation from an erroneous
published linear perturbative shortcut. The quantitative TP report repairs a
zero-residual coupling step and preserves the rate claim. These specific findings
are not used to dismiss the entire predecessor frameworks.

## Retained full-paper reports and earlier independent checks

- [Tensor Programs III](review_tp3.md).
- [Non-Gaussian Tensor Programs](review_nongaus.md).
- [Tensor Programs IV](review_tp4.md).
- [Tensor Programs IVb, first audit](review_tp4b.md).
- [Neural tangent hierarchy](review_nth.md).
- [Label-Aware NTK](review_lantk.md).
- [Dyer and Aitken diagram papers](review_feynman.md).
- [Neural Tangents and software alternatives](review_software.md).
- [MFP manuscript assessment](manuscript_assessment.md).
- [Independent MFP theorem/compiler review](independent_mfp_audit.md).
- [Independent NTH, NGTP and LANTK checks](independent_proof_checks.md).
- [Independent TP IV and diagram formula checks](independent_formula_checks.md).

These earlier reports remain evidence, rather than predetermined conclusions for
the revision. Source versions, exact passages, hashes and unverified dependencies
are recorded in the reports. Download presence alone does not establish reading.

## Validation and residual limits

All 72 bundled MFP tests passed in both assessments. The first assessment also
regenerated the calculus, symbolic/cubic MLP derivative, and three second-order
kernel-jet example variants. The reassessment added two independent targeted
algebraic checks, both passing. No manuscript or compiler changes were needed.
An independent finite-network kernel-jet calculation also supports the analytically
derived DMFT comparison; its [source](reassessment_dmft_linear_check.py) imports
neither the manuscript compiler nor maintained code.
The revised five-page LaTeX draft compiles with resolved references and no final-log
warnings or overfull boxes. Tests and prose checks do not certify every implementation
execution, formalize the theorem in Lean or establish a complexity guarantee.

Small Tensorgrad examples were executed. External paper training experiments,
NTK Unlimited's full suite and the DMFT notebooks were not reproduced. There is no
comparative performance benchmark. Dyer's and TP IVb's separate final ICLR PDFs
remained inaccessible; the full specified arXiv versions were used. The final NTH
conference appendix was not separately available. Some external all-order,
ReLU/spectral dependencies and broader proof branches remain explicitly uncertified.

From `paper_MFP/`, reproduce the bundled tests with:

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=code python -B -m unittest discover -s code/tests -p 'test_mfp_*.py' -v
```

From the checkout root, reproduce the new targeted checks with:

```sh
python -B studies/mfp_literature_positioning_20261011/reassessment_calculus_checks.py
```

From this study directory, rebuild the proposed prose with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/home/amir/Codes/PDE/data/generated/mfp_literature_positioning_20261011/framing_v2 proposed_framing.tex
```

Root owns the synthesis and proposed prose; scoped reviewers own their named reports.
No Git index changes or commits were made by this reassessment. No changes to the
book, maintained compiler, target manuscript or other studies were made by this task.
