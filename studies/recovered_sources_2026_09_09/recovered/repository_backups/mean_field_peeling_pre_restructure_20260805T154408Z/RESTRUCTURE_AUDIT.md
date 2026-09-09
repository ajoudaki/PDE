# Mean-field peeling restructure audit

**Snapshot time:** 2026-08-05T15:44:08Z  
**Final audit date:** 2026-08-05  
**Snapshot status:** frozen; none of the files covered by `MANIFEST.sha256`
were modified during the restructure.

## 1. Recovery baseline

Before any consolidation edit, the following were copied into this snapshot:

- `current_main/`: the complete working-tree document directory;
- `pushed_branch_afcb2fc/`: the complete document directory from pushed
  commit `afcb2fc6779d4968d4b833b390ae7961e00efff9`;
- `repository_context/`: the relevant repository and study indexes.

The working-tree commit at snapshot time was
`964ef9c9956edac803d5a4529ad66367691f1b95`. Direct tree comparisons passed
immediately after copying. `sha256sum -c MANIFEST.sha256` passed both before
the migration and after the final PDF build. All superseded documents and
build artifacts are therefore recoverable byte-for-byte.

## 2. Final active structure

The maintained directory is now:

```text
studies/derivative_wick_calculus/
  README.md
  MEAN_FIELD_PEELING_THEORY.md
  MUP_TRAINING_CASE_STUDY.md
  MEAN_FIELD_PEELING_REPORT.tex
  MEAN_FIELD_PEELING_REPORT.pdf
  build_report.py
  archive/
    ORIGINAL_NOTES_AND_NTK_SAMPLE.md
```

The ignored `build/` directory contains reproducible intermediates only. The
repository ignores `.backups/`, `build/`, `__pycache__/`, and notebook
checkpoints.

## 3. Source-to-destination ledger

| Earlier material | Final destination | Treatment |
|---|---|---|
| `MEAN_FIELD_PEELING_PROGRAM.md` in both preserved trees | `MEAN_FIELD_PEELING_THEORY.md`; historical opening proposal in `archive/ORIGINAL_NOTES_AND_NTK_SAMPLE.md` | Consolidated by concept and claim status; the raw proposal is separately frozen as history. |
| `TENSOR_PROGRAMS_CONTRAST_AND_THEOREM_FRAMING_REPORT.md` | Theory Sections 13--20 | The theorem ladder, Tensor Programs semantics, explicit unrolling distinction, novelty qualification, terminology, nonclaims, proof obligations, and worksheet were retained. |
| `MUP_TRAINING_PEELING_CASE_STUDY.md` | `MUP_TRAINING_CASE_STUDY.md` | The complete original worked body was retained, then extended with the general readout-scaled backward template and the complete five-branch audit. |
| Original raw notes and supplied NTK sample | `archive/ORIGINAL_NOTES_AND_NTK_SAMPLE.md` | Preserved as a clearly marked historical source, including tentative claims, with a repair-status appendix. |
| Full, compact, and self-contained TeX/PDF reports | One wrapper, one builder, and one canonical PDF | Duplicate presentation layers were removed from the active directory only after backup verification. Their unique mathematics was migrated to the Markdown sources. |
| Notebook checkpoint, old render scripts, caches, and auxiliary files | Frozen backup only | Removed from the maintained source surface; reproducible generated files are ignored. |

The TeX file now owns typography and source inclusion only. Mathematical
content is edited in Markdown. The builder generates protected Markdown
copies, checks every math placeholder, compiles with XeLaTeX, validates the
PDF, and copies one canonical artifact to the study directory.

## 4. Losslessness checks

Three complementary checks were used.

1. **Exact formula preservation.** All 547 dollar-delimited math spans from
   the earlier detailed case study occur exactly in the consolidated case
   study: zero missing. All 93 formula spans in the archived original-note and
   NTK-sample block occur exactly in the historical source: zero missing.
2. **Semantic source audit.** The program and Tensor Programs documents were
   mapped section-by-section because consolidation intentionally rewrote and
   reconciled their prose. The audit checked the scaling ledger, exact
   conditional Gaussian law, admissible grammar, Wick--Stein formulas,
   equality partitions, width valuation, covariance replacement, algorithm,
   feature-learning jets, theorem ladder, Tensor Programs semantics,
   nonclaims, proof obligations, terminology, literature, and practical
   worksheet. Two issues found during this pass were repaired: the explicit
   Tensor Programs unrolling
   `(Z^1,...,Z^m)=F(G)` with its Gaussian integral and complexity caveat was
   restored, and an overbroad “all-observable” phrase was replaced by the
   precise “full proposed admissible grammar.”
3. **Worked-case audit.** A separate audit checked the backward peel, all
   one-step and two-step equations, raw/effective scaling, the deep-linear
   coefficients, the arbitrary-depth formal template, and the five-branch
   expansion. It found and repaired four status/notation defects: expectation
   versus concentration, the definition `L:=H+1`, the centered-readout
   qualification, and the coincident-label derivative in Appendix B.

The final independent mathematical verdict was that no mathematically or
epistemically distinct source content remained omitted and no accidental
claim strengthening remained.

## 5. Final build and visual audit

The final build protected exactly 880 math spans from the three canonical
Markdown sources. It produced a 42-page A4 PDF. Every page contains at least
1,094 non-whitespace extracted characters; there are no empty divider pages.

Checks passed:

- `qpdf --check`: no syntax or stream errors;
- semantic text sentinels for the theory, backward audit, one-step and
  two-step case study, five-branch appendix, and historical source;
- no unresolved math placeholders or raw local-link fragments in extracted
  text;
- no LaTeX errors, undefined references, overfull boxes, or underfull boxes;
- representative visual inspection of pages 1, 4, 12, 15, 30, and 42: no
  clipping, missing equations, broken tables, duplicate heading numbers, or
  raw-URL footnote clutter.

The log contains only three benign Asana Math warnings that bold math shapes
are unavailable and the regular shapes are substituted in headings. The
representative heading and equation pages were visually checked for glyph
loss.

Final maintained-source hashes:

```text
6a34f34b39b3191d61e54e89c429a5fcbd18449cc3edb928af4ec00d01ef09c8  MEAN_FIELD_PEELING_THEORY.md
2ceb96c33f7ce5b63aad22331054bd9ef614fd31f557518d99917a7e518e79f6  MUP_TRAINING_CASE_STUDY.md
9693fc1ff9cc06fbf586724b96341cecd68f2151bf8451e6b9a3eceaf07060ac  archive/ORIGINAL_NOTES_AND_NTK_SAMPLE.md
f0e93c157c7c84e63b729a68a6abebc86ec01716582a685fa864eb1588e4203e  MEAN_FIELD_PEELING_REPORT.tex
bc38568d118d75928b604204206a9f6e14161dbdf7aaf99e647041e224765e03  build_report.py
e1691f11015f03ebd68eb5db73a1401eddaeb4f4b4b8a369ed4986daa327cf86  MEAN_FIELD_PEELING_REPORT.pdf
```

## 6. Final verdict

The restructuring is complete. There are two maintained mathematical
documents with distinct functions, one deliberately frozen historical source,
one presentation wrapper, one reproducible builder, and one canonical PDF.
The removed active files were duplicate presentations or generated artifacts;
their unique source content was migrated and their exact originals remain in
this checksum-protected snapshot.
