# Theorem-focused compact paper

## Current naming: Taylor compression

The user renamed the finite-panel method from Logarithmic to Taylor. The compact
copy, full manuscript and appendices, current paper documentation, explainer
source/pages, and current experimental display labels now use Taylor. Ordinary
logarithmic rate descriptions and the separate historical seeded decoder retain
their meanings. Frozen review packets/reports are unchanged. Existing code APIs,
configuration keys, result identifiers and file paths are preserved for
compatibility; no experimental run or numerical result was changed.

Both manuscripts rebuilt successfully in
`data/generated/compact_paper_20261009/taylor_xXSKsA/`, and the PDFs were copied to
`paper/compact.pdf` (47 pages) and `paper/main.pdf` (215 pages). The compact build
has no warnings; the full build has no unresolved references or errors, with
underfull-box notices in the long appendix. A naming-only comparison confirms
that the compact sources have no other changes. Three edited plotting scripts
passed syntax checks. The former restriction against editing the full paper
was extended only for this user-requested naming change.

Explainer HTML was rebuilt with the existing renderer. Its Firefox thumbnail
backend failed in this environment, so the six stale name-bearing thumbnails
were moved recoverably to `taylor_xXSKsA/previous_thumbnails/` in the same
generated directory. Rebuilding with `--no-thumbs` enables the existing live
HTML previews for those cards; the renamed figures remain fully available.
No figure data or source was removed.

## Current continuation: shorter statements

The user's follow-up requests only low-risk shortening of long statements,
without losing qualifications or obscuring their public interfaces. Eight
statements were tightened. Repeated setup, confidence, constant-dependence and
activation-evaluator conventions now refer to the central setup. The selected
transfer proposition cites the existing four source families instead of
displaying them again. The source proposition uses locally defined pregated
responses and a local radius to remove repeated cases and rectangle endpoints;
neither is new persistent notation. Compiler and approximation prose was
condensed. Every quantitative bound and the explicit source tolerance remain
public; no essential conclusion was moved into a private proof.

The largest source statement is approximately one third shorter by source
character count, and the transfer statement one fifth shorter. The fitting and
approximation statements retain their necessary quantitative detail. No attempt
was made to force every statement to an arbitrary length. All outer proof
bodies and the headline theorem are byte-for-byte unchanged from the frozen
post-notation-audit packet. The persistent inventory remains 29 objects.

A read-only editorial reader proposed cuts; a new scoped reviewer then compared
the complete before/after statements and their dependency interfaces. Review
evidence is in STATEMENT_EDIT_CHECK.md; the lead read the complete report.
The check passed after clarifying that the central activation/depth-only
constant convention applies to all stated bounds, with no unresolved issue.
This is an equivalence check for the
editorial changes, not a repeated whole-proof audit. The before version remains
in POSTAUDIT_INPUTS.tar.gz. The build and extracted comparison inputs are under
`data/generated/compact_paper_20261009/statements_BHp6Gs/`. Compilation from
`paper/` uses `latexmk -pdf -interaction=nonstopmode -halt-on-error` with that
directory's `build/` as `-outdir`. The resulting 47-page PDF is saved as
`paper/compact.pdf`. It has no warnings, unresolved references or box overflows;
136 labels resolve all 144 reference uses. The changed source and transfer
statement pages were visually checked. Original manuscript hashes are unchanged.

## Completed fresh audits and notation migration

The user requests fresh independent adversarial reviews, then a proof/notation
refactor with at most 30 persistent semantic symbols, then a second fresh audit
round. The earlier module cross-reviews below are historical evidence for the
previous version, not substitutes for this new request. Three new isolated agents
(`fresh_preaudit_a`, `fresh_preaudit_b`, `fresh_preaudit_c`) received only the five
frozen compact TeX inputs, a neutral proof-audit assignment, and required skills.
Each read the complete proof rather than a module. No previous verdict or
author notes are in their allowed inputs. Reports: PREAUDIT_A.md through C.md.
The frozen packet is PREAUDIT_INPUTS.tar.gz. The original manuscript remains out
of scope for edits. NOTATION_INVENTORY.md records the migration contract and
29-object persistent inventory, now independently checked after migration.

All three first-round reports are complete, with full 3,553-line coverage and
matching frozen hashes. None established a major mathematical flaw. Reviewer C
identified a minor wording defect: last-layer preactivations, not nonlinear
activated features, are Gaussian. This was corrected in the rewrite.
The reports explicitly limit confidence in the long source bookkeeping; an
internal positive audit is not formal verification. The three reviewers have
moved to clearly separated author/editor roles for the notation migration.
They did not serve as the fresh post-migration reviewers.

The refactor now has portable public interfaces for fitting, analytic sources,
Legendre approximation, dense variability, and selected source-to-runtime
transfer. Its statement boundaries use canonical quantities; construction and
coefficient notation is local to the corresponding proof. The source and
selected proofs contain named local claims and explicit internal steps. The
complete persistent inventory is printed in the paper and has 29 objects.
Three new isolated reviewers (`fresh_postaudit_a`, `fresh_postaudit_b`, and
`fresh_postaudit_notation`) checked the entire rewritten 3,958-line proof.
They have no earlier verdicts, editor messages, or study history in their inputs.
The notation reviewer is explicitly required to challenge the claimed count.
The frozen new packet is POSTAUDIT_INPUTS.tar.gz; reports are POSTAUDIT_A.md,
POSTAUDIT_B.md and POSTAUDIT_NOTATION.md. All three are complete: no concrete
mathematical defect or necessary repair was identified. The notation reviewer
independently counted 29 persistent semantic objects and traced statement-only
dependencies. The mathematical reviewers reconstructed the load-bearing steps;
reviewer B additionally checked 1,664 coefficient inequalities numerically,
with no violations. This diagnostic supplements, rather than proves, the
inequalities. The lead read all six complete reports. The reports explicitly
distinguish substantive independent review from formal verification of every
large numerical enclosure.

The lead read every before/after mathematical diff, checked the changed public
bounds against the preserved coefficient estimates, and mechanically checked
balanced proof environments, label resolution and cross-file private-label
imports. No cross-file private-label import remained. A clean integration build
and rendered-page check exposed a nearly blank page and one crowded display;
both were corrected before the post-audit snapshot. The new build is 48 pages
with the same 11-point text and one-inch margins. No original-manuscript source
has changed: the five original SHA-256 checksums still match the initial ones.

The headline theorem body is byte-for-byte identical to the pre-migration copy.
The final five source hashes match the post-audit frozen packet, with no
scientific edits after that review. The final clean build is in
`data/generated/compact_paper_20261009/refactor_build_GUrEBD/` and is saved as
`paper/compact.pdf`. It has no LaTeX warnings, undefined references, or
overfull/underfull boxes. All 146 reference uses resolve to 137 distinct labels;
proof environments, private-label imports, control characters and whitespace
were checked. The inventory, theorem, source interface and selected-transfer
interface were also inspected as rendered pages.

## Notation-round audited source checksums (before statement shortening)

SHA-256 (the sources reviewed in the second fresh round):

```text
a56acbdc765fa6e42f8aba186dec0b3ea3a59e9fa4c7d66ac1a7839bc0688445  paper/compact.tex
f35f1dfd9c47bd5abbf97c849b0176347e9e5da8adba5e7ab8b75c79868b2c51  paper/compact_fitting.tex
4e7d25a8501e7928f60e538f1c80e7e73a3e2f04d34a1ae4d40407ffc1f545f9  paper/compact_foundations.tex
bca774baab3a5ba9879340fc61a92b9cbdff522600620d1972ab12b876f48239  paper/compact_legendre.tex
cd203e7de6f8e3d23331d58ac64366350dd076405d63e8fc238f8f9a794beeee  paper/compact_selected.tex
89573592a8762f8ea03ea019bb4bebfd2047cb9f503dc3c21f6efa7da4114b21  paper/compact.pdf
```

## Scope and authority

User-authorized maintenance/rewrite of the current `paper/` manuscript into a
separate, self-contained LaTeX document. The original manuscript is preserved.
Inputs are the current `paper/main.tex`, `results.tex`, `methods.tex`,
`integrated_appendix.tex`, and `panel_appendix.tex`; no other study is an input.
The maintained notation guide is `docs/notation.qmd`. Initial repository HEAD:
`07c1e73` (concurrent unrelated changes are preserved).

The target is exactly the current three-method headline theorem: full physical
trajectory and endpoint, sphere/declared-panel query distinction, unchanged
storage dependence, initialization-only provenance, negligible relative dense
variability, and the additional Y/n accuracy for the selected methods. This
theorem-focused copy does not claim the independent dense upper/inverse theorem,
supplementary seeded decoder, experiments, or efficient-setup operation bounds.
Their omission is scope selection, not proof compression. The original document
retains those results. No book promotion or Git commit is requested.

## Owned outputs and collaboration

- Lead: `paper/compact.tex`, assembly, theorem equivalence, compile and final checks.
- Source author: `paper/compact_foundations.tex` (shared source event).
- Dense/Legendre author: `paper/compact_fitting.tex` and
  `paper/compact_legendre.tex` (fitting, signed comparison, Legendre construction
  and dense lower bound).
- Selected-model author: `paper/compact_selected.tex` (source approximation,
  coordinate selection, autonomous dynamics, Harmonic and finite-panel results).
- Review reports and substantive working notes: this flat study folder.
- Generated PDFs, logs and render checks: `data/generated/compact_paper_20261009/`.

All proof modules must be self-contained collectively, with internal references
only, and no input of the old manuscript or external study proof. Shared lemmas
must retain their actual hypotheses. Constants may depend only on activations
and depth unless a statement explicitly says otherwise; structural dependence
must not be hidden to shorten an argument.

## First completed copy and reduction (before notation migration)

Entry point: `paper/compact.tex`; compiled copy: `paper/compact.pdf`.
The new document has 43 pages, compared with the existing 215-page `main.pdf`
(80% fewer pages), with 11-point text and one-inch margins. It has one headline
theorem and 23 supporting lemmas, propositions and corollaries. This is not an
80% reduction of identical total content: the scope exclusions above account
for part of the reduction. No scope, storage dependence, label hypothesis,
confidence qualification or endpoint promise of the headline theorem was
weakened. The original five scientific input files remain byte-for-byte unchanged.

The proof reductions are substantive as well as organizational:

- One stopped-cavity, local-insertion, trace and Gaussian-moment argument supplies
  both analytic source domains, followed by their separate domain checks.
- One exact source metric, selected nonlinear optimizer, fitting argument and
  readout-deficit cancellation serve Harmonic and Taylor. Only source bases
  and their dimensions differ. The adaptive partition estimate is proved once.
- A conditional scalar final-layer fluctuation replaces the recursive matrix
  central limit theorem, with the same positive-time dense lower bound.
- Selected accuracy Y/n uses tighter source tolerance on the original finite
  comparison horizon plus real fitted tails. No arbitrary-horizon complex
  extension is needed. Legendre retains its separate real all-time carrier bound.
- Every construction, initialization-only coefficient compiler, storage inventory
  and probabilistic assembly used by the headline is included in the new copy.
  It does not import either long appendix or an external study.

## First-copy internal checks and resolutions

Three non-author scoped mathematical cross-reviews covered the complete proof
modules, with the lead checking the full assembled copy and interfaces:

- `REVIEW_SOURCE.md`: independent stopped references, uniform control nets,
  nonlinear remainders, trace absorption, moments, analytic domains and carriers.
- `REVIEW_LEGENDRE_DENSE.md`: dense fitting, projection identities, autonomous
  history dynamics, all-order physical bounds, comparison, scalar lower bound.
- `REVIEW_SELECTED.md`: exact metric, corrected runtime, fitting/cancellation,
  initialized jets, harmonic and panel approximation/counts, complete inventories.

All findings from these reviews were resolved and locally rechecked. In
particular the source proof now qualifies Gaussianity and conditional means
before adaptive-control substitution, and distinguishes first-layer row motion
from the smaller hidden-row retained ports. Other repairs make the dense real
tail bridge, positive integer Legendre order and factorial estimate explicit.
No outstanding mathematical issue was identified by this internal review.
These are bounded internal cross-checks, not formal verification, fresh
publication-level independent reviews, or book-promotion approval.

The final `latexmk -pdf -interaction=nonstopmode -halt-on-error` build succeeded
without LaTeX warnings, unresolved references, or overfull/underfull boxes.
The build products are in
`data/generated/compact_paper_20261009/build_gfjGvf/`.
All 130 internal reference uses resolve to the 131 distinct labels; environments,
control characters and trailing whitespace were checked. Rendered theorem,
source, comparison and ending pages were visually inspected. The saved PDF is
the final build, not the preliminary 33-page partial build.

An auxiliary 20-case deterministic numerical algebra check of exact metric
isometry, metric adjoints and the raw selected-velocity energy identity had
maximum residuals 1.19e-15, 9.95e-14 and 4.58e-16 respectively. This is only a
sanity check; the mathematical identities are proved in the document.

No commit, push, original-paper replacement, or book promotion was performed.
Unrelated concurrent changes were preserved; the repository HEAD advanced
independently during this task.

## First-copy source checksums

SHA-256 (after all mathematical corrections):

```text
64327f17c0a47b08a349890d274960b9732c8d650b2730e02a4d44d3e88fa6f9  paper/compact.tex
4cb10d4534f95ca5dbc9a957aac536c55a7268e0dc7128c105102de5bd195235  paper/compact_fitting.tex
8de151e32734ee2c9116a91a1cccb7c5ecee7ec1369ff4784e88fb4d79a6148a  paper/compact_foundations.tex
45c40b7e6c1c1b501d6f2643a226ac2ca4a00a91e3d9704502ed54fadf4fe238  paper/compact_legendre.tex
12b2d33bf7732172d454cf3a2d74a4b322f027a74474d8747f3da9ef85b96c11  paper/compact_selected.tex
```
