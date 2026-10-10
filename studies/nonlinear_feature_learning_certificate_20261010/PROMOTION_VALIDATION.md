# Promotion package and edition validation

Status: **approved and integrated on 2026-10-10**.
The approved object is the complete [section](PROMOTION_SECTION.qmd), inserted
immediately before `sec-compression-assembly` in
`docs/08b-trajectory-compression.qmd`, Chapter 9, *Complete-trajectory compression*.
No other maintained content or global notation changed in this promotion.

## Scientific object and review provenance

The candidate preserves the final compact-paper theorem and shortened
adjoint proof. It supplies four supporting lemmas and the final transfer
argument, using the existing book fitting lemma and absolute approximation
propositions as dependencies. The local extra hypotheses are nonaffine
activations and no parallel/antiparallel distinct training inputs. Unbounded
activation values remain allowed. Its time is fixed and positive before the
width limit; it makes no endpoint, arbitrary shrinking-time, test-risk, or
all-kernels comparison. Hidden motion belongs to the dense reference;
compression transfers the two prediction gaps, not hidden coordinates.
Taylor adds at most four passive, unlabeled witness inputs before initialization.

Author/assembler: `/root`. Independent selection:
`/root/promotion_selector`, [original report](PROMOTION_SELECTION.md).
Fresh complete scientific reviewers: `/root/promotion_math_a` and
`/root/promotion_math_b`, [report A](PROMOTION_MATH_REVIEW_A.md) and
[report B](PROMOTION_MATH_REVIEW_B.md). Both read all 6,441 frozen packet lines,
including the entire original chapter and the final paper comparison inputs,
and found no required scientific correction. The coordinator read both reports
in full. The [exact neutral assignment](PROMOTION_REVIEW_ASSIGNMENT.md), original
reports, hash manifests and diagnostic scratch are retained. Reviewer numeric
checks are local algebra diagnostics, not new empirical claims for the book.

The scientific packet is
`data/generated/nonlinear_feature_learning_certificate_20261010/promotion_v1/review_inputs/`.
Its candidate digest is
`c04cc608c43cc0c402db40b1f0d4241e71a65eb9cd70bed5dcc18aff82fc307f`.
The final presentation packet is `promotion_v3/review_inputs/` in the same
generated root. Its candidate digest is
`a6627f8f435d94714a2496bacd5842c810a893e17496168ee695ecdb44a57ed3`.

Only the following presentation repairs separate v3 from the scientific
review packet:

1. Ten blank lines separate five proof anchors from their proof fences/content.
2. One invisible TeX brace pair protects a norm interior against the existing
   PDF formatter's inappropriate line break inside a function argument.
3. A redundant literal `Equation` preceding one native equation reference is
   removed, preventing the rendered phrase “Equation Equation”.

Undoing exactly those changes and discarding empty lines gives identical
linewise text. No assertion, hypothesis, proof step, normalization, constant,
cross-reference target or storage order changed. The presentation fixes were
reviewed separately by fresh integration reviewer
`/root/promotion_integration_final`, using the
[neutral integration assignment](PROMOTION_INTEGRATION_ASSIGNMENT.md), without
prior review verdicts. This is not a fresh audit of every unchanged book proof.

## Standalone assembly and reproduction

All generated paths below are relative to the repository root. The maintained
`docs/` and `code/` trees, not the repository or its Git metadata, were copied
into a new study-generated edition. Neither studies nor paper inputs are
needed by its renderer; frozen comparison inputs are kept separately for
review provenance. No retained book output was copied into the new edition.

The following is the original, pre-integration assembly command:

```sh
python studies/nonlinear_feature_learning_certificate_20261010/assemble_promotion.py \
  /home/amir/Codes/PDE \
  /home/amir/Codes/PDE/data/generated/nonlinear_feature_learning_certificate_20261010/promotion_v3
```

The script refuses an existing destination and any destination outside this
study's generated root. It expects the original, unpromoted chapter: do not
rerun it against the now-promoted live chapter, since that would insert the
section twice. The frozen v3 edition can be rendered directly using the
command below; alternatively, render the maintained book, whose inputs now
match that edition. Retain the exact candidate and dependency hashes first.
`edition_inputs.json` freezes every maintained edition input before rendering.
The scientific packet manifest separately records the original chapter,
candidate, final paper inputs and the exact assembled-chapter digest.

Tools: Quarto **1.10.19**, its bundled Pandoc, system XeLaTeX
**TeX Live 2022/dev/Debian**, Python and Poppler. Quarto was obtained from the
[official versioned release](https://github.com/quarto-dev/quarto-cli/releases/tag/v1.10.19),
unpacked only into the study-generated `promotion_tools/` directory, and not
installed globally. Its actual binary path is
`data/generated/nonlinear_feature_learning_certificate_20261010/promotion_tools/quarto-1.10.19/bin/quarto`.

From `promotion_v3/docs/`, the full edition command is:

```sh
XDG_CACHE_HOME=/home/amir/Codes/PDE/data/generated/nonlinear_feature_learning_certificate_20261010/promotion_tools/cache \
XDG_DATA_HOME=/home/amir/Codes/PDE/data/generated/nonlinear_feature_learning_certificate_20261010/promotion_tools/share \
/home/amir/Codes/PDE/data/generated/nonlinear_feature_learning_certificate_20261010/promotion_tools/quarto-1.10.19/bin/quarto \
  render --to all > ../render_all.log 2>&1
```

The full project retains its HTML/PDF/LaTeX formats, bibliography, native
cross-reference filters and source/code bundler. The original cache path was
read-only; the command uses dedicated study-local caches instead of altering
home-directory settings. With `--to all`, Quarto writes its editable export
to `data/generated/DTDL/book-latex/DTDL.tex` within the standalone edition.
An identical copy is placed beside `data/generated/DTDL/DTDL.pdf` for a
convenient editable-export entry point. This is packaging generated output,
not a source change. The complete original `book-latex/` source/code bundle
is retained.

Run the edition checks from the repository root:

```sh
python studies/nonlinear_feature_learning_certificate_20261010/check_promotion.py \
  data/generated/nonlinear_feature_learning_certificate_20261010/promotion_v3
```

The checker verifies frozen inputs, exact insertion/preservation, all 18 main
HTML pages, duplicate HTML IDs, unresolved native references, local link
targets and HTML fragments, and the PDF/editable-LaTeX outputs. Rendering
and link checks are not proofs of the mathematical results. There is no new
numerical implementation, API or empirical conclusion needing promotion.

## Edition validation record

The v3 `quarto render --to all` command exited **0**, producing all 18 HTML
pages, the complete **1,734-page PDF**, and editable LaTeX. The log is
`promotion_v3/render_all.log`; it contains no warning/error, undefined-reference,
or multiply-defined-label report. The five proof fences render as actual proof
environments. `check_promotion.py` exited **0**, reporting `html_pages: 18` and
`errors: []`; its full output is `promotion_v3/validation.json`.
All maintained source inputs are preserved, apart from the proposed exact
insertion into the staged Chapter 9. At this pre-approval validation stage,
no live `docs/` or Git-index change had been made.

Final generated output digests:

```text
37f1fb9ede0c2e4c9e4f7d0c84b224b9d3e0616130082b6d4c6c7bccba8a385b  DTDL.pdf
20b27cce274257fe2d0ff51e4eac30de7e41858d441a58ee6dffc621e4c5398a  DTDL.tex
```

`qpdf --check` found no syntax or stream-encoding errors in the full PDF.
The new section occupies printed pages 914–923; the theorem is on page 915.
The independent integration reviewer has visually inspected every one of
those pages. The author also inspected theorem and motion-proof images.
Native theorem/lemma/equation references render, the local hypotheses are
visible in the theorem, and the dense-feature qualification is retained.

For convenient user inspection, `qpdf --empty --pages DTDL.pdf 914-923 --
proposal-preview.pdf` produced the ten-page excerpt in
`promotion_preview/proposal-preview.pdf` under the study's generated root.
It includes a little unchanged surrounding material at its boundaries.
`qpdf --check` passes for that excerpt. References to other chapters or pages
outside the excerpt should be followed in the full edition instead. An earlier
Poppler split/merge preview emitted recursive-dictionary warnings and is not
the proposed preview; it is retained only as an unused generated intermediate.

The complete [independent integration report](PROMOTION_INTEGRATION_REVIEW.md)
returned **PASS**, with no required corrections or unresolved objections.
It independently verified exact insertion and all frozen inputs, all new
HTML/LaTeX formal environments, local references, and all ten new PDF pages.
Its report digest is
`3dc9ac7e2c2c96b3c3b1f87956c67133ac6aad01965749ae88c4b95b7103afa9`.
The coordinator read the report completely. The reviewer records the exact
older passages read and the unread complement. Browser screenshot tooling
could not run: browser-layout inspection is not claimed; actual HTML was
fully checked as markup/links, and visual inspection used the PDF.

## Approval and live integration

On 2026-10-10 the user approved the exact reviewed v3 package:
“ok great, then I approve the promotion”. Selection, paired complete scientific
review and independent integration/edition-validation gates were already
complete. No scientific changes were made after those reviews.

The candidate's 521 lines map exactly to lines 4493–5013 of
`docs/08b-trajectory-compression.qmd`, followed by one separating blank line.
The existing assembly heading now starts at line 5015. Removing this single
insertion restores the original chapter byte-for-byte. The final chapter
matches the approved standalone chapter byte-for-byte, with SHA-256
`5d068eaac00fe6b6ec8149e13d5320dc6c40f6935a7c2e467ab55e38abaf5bb8`.
The candidate retains its approved SHA-256
`a6627f8f435d94714a2496bacd5842c810a893e17496168ee695ecdb44a57ed3`.

All 104 live book/code inputs match `promotion_v3/edition_inputs.json`.
The review-input comparisons likewise match, accounting only for the approved
original-to-assembled chapter transition. The independent read-only checker
`/root/promotion_correspondence` confirmed the 104 inputs, candidate, chapter,
and assigned review inputs. This is a mechanical correspondence check, not
another mathematical review. The frozen assembler is unchanged.

Post-insertion checks:

- `cmp` between the live and approved assembled chapters: exit 0.
- `check_promotion.py promotion_v3`: exit 0, 18 HTML pages, no errors.
- `git diff --check -- docs/08b-trajectory-compression.qmd`: exit 0.
- Existing HTML/PDF/LaTeX validation applies to these identical maintained
  inputs; no new full render was needed or claimed after insertion.

A repository-wide whitespace check encountered an unreadable unrelated file,
`studies/quarto_capability_pilot_20260921/migration_decisions.json`; the scoped
check above passed. No permissions or unrelated files were changed.
No paper file was edited or staged by this promotion. No established result,
assumption or notation outside the approved insertion was altered.

The integration and this record are committed together under the shared Git
writer lock, with only the chapter and this study's source/evidence staged.
The exact commit is retained in Git history and reported at handoff; generated
render products are not committed. This completes the prescribed promotion.
