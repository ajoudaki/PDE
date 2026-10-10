# Reuniting the established MFP exposition

User-authorized editorial maintenance, 2026-10-10. Chapter 2 is to become
**Mean-Field Peeling: A Gaussian Calculus for Deep Networks**, in Part I,
between training geometry and local population evolution.

Scope: reorganize established `docs/` material only. Preserve statements,
proofs, formulas, canonical notation and all existing identifiers. Move the
finite derivative/Gaussian calculus from Chapter 7 into Chapter 2; keep closure,
trajectory approximation and the separate Taylor/Stieltjes obstructions in
Part II. No study results or implementations are newly promoted.

Root owns the edits and deterministic checks. The scoped `mfp_structure_check`
agent inspected only current Chapters 2, 7 and 8 for section boundaries and
cross-reference context; it made no edits or scientific acceptance decisions.
The prior organization is recoverable at Git commit
`af9ee2765187a9d53539b60e81575a7c02d252a5`.

`reorganize.py` records the exact moves and editorial replacements. Its check
compares the whole-book content with that Git version modulo those explicit
replacements, heading levels and link destinations, verifies unchanged display
mathematics and existing identifier/reference inventories, and checks all
current book cross-reference destinations. Generated evidence belongs under
`data/generated/mfp_book_reorganization_20261010/`.

## Completed organization and checks

Moved 1,542 lines in five complete spans: the moving-flow recurrence,
decorated-forest factorization, finite loss-GD pullbacks, contraction calculus
A–D, and observable heads E–F. The wrapper identifiers move with their methods.
The negative quadratic certificate, loss initial-layer obstruction, shallow
closure comparisons and moment-extension certificates remain in Chapter 7.
Chapter 8 retains refinement and autonomous computation.

The new introduction gives a linked route through the MFP method and its scope.
Split-induced context now names and links the supplying model or calculation.
Two existing Chapter 8 references wrongly pointed to loss-GD pullbacks while
naming the Gaussian source lemma; both now point to that unchanged lemma in
the trainability chapter. Chapter 2's stale integrated-memory location sentence
was corrected as well. Original filenames and all identifiers remain usable.

The scoped editorial follow-up passed after two local fixes (one section title
and the early model reference in the retained initial-layer theorem). This is
an editorial check, not a new scientific or promotion review.

- Whole-book source preservation passes modulo the script's explicit editorial
  replacements, heading levels and target paths; all 6,050 display blocks and
  5,215 Quarto identifiers are unchanged. Identifier recognition excludes
  escaped mathematical `\#` tokens.
- All 18 rendered HTML pages pass: every source target occurs once on its
  owning page, and 6,616 local fragment links resolve.
- The library boundary/link check passes on 93 files. Git's whitespace check
  reports existing trailing spaces on moved mathematical lines; the complete
  before/after whitespace-line multiset is unchanged.
- One HTML and one PDF render succeeded with Quarto 1.10.18. No unresolved
  reference warnings occurred. PDF integrity passes, and the MFP opening was
  visually checked on page 113 of the 1,725-page export. Editable LaTeX is
  retained by the PDF build.
- The served `data/generated/DTDL/` HTML, PDF, LaTeX and source bundle were
  refreshed from the checked outputs. Concurrent paper/study files were not
  edited or staged.

Evidence: `data/generated/mfp_book_reorganization_20261010/preservation.json`
records exact moves and editorial replacements; `build/build.json` records
source hashes, render commands, timings and published hashes;
`build/html_checks.json` records the rendered link/target checks.

Recheck the current rearrangement and its saved HTML build with:

```sh
python studies/mfp_book_reorganization_20261010/reorganize.py --check-render
python code/tools/check_library.py
```

Render normally using the root guide. For a fresh retained build, use the
commands in `build/build.json` with a new output directory and
`XDG_CACHE_HOME=/tmp/pde-quarto-cache`. The `--apply` option reproduces this
specific reorganization from its recorded Git baseline; it deliberately
rejects intervening book edits rather than overwriting them.
