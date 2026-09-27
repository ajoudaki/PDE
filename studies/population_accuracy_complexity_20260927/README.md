# Population-flow accuracy versus computational cost

Question: compare dense canonical training, both response-memory clocks, NTH,
and numerical TP/DMFT on the same nonlinear feature-learning population
predictor, for fixed finite training data, fixed depth, and a finite horizon.

The consolidated self-contained deliverable is `COMPARATIVE_REPORT.md`.
It follows the user-supplied report's progression from a paper paragraph
through derivations and optimized costs to comparison tables. It corrects
the supplied NTH theorem/horizon, moving-memory accounting, and claimed
time-Taylor-radius barrier (with an explicit counterexample), and separates
limiting-process sampling from finite-width response-history storage.

Inputs: the user-designated current `paper/main.tex`, the maintained Quarto
book (`docs/03-local-population.qmd`, `docs/04-continuing-flows.qmd`), and full
primary-source papers. Other studies are not research inputs.

Owner: the main assistant in this task. The comparison analysis involved no
training experiments. A later scoped editorial agent advised on placement,
and a scoped coauthor prepared the technical appendix for the user-authorized
paper revision. Neither performed a new experimental or literature campaign.

Full primary PDFs and extracted texts are retained in
`data/generated/population_accuracy_complexity_20260927/full_texts/`, with
URLs and SHA-256 hashes in `sources.json`. These include NTH (full proof), TP IV
(full version), nonlinear DMFT (including Algorithm 1 in Appendix B), its
finite-width fluctuation follow-up, deep neuronal-embedding mean field,
quantitative GP tensor programs, and the 2025 muP feature-diversity paper.

The comparison and new derivations are in `ANALYSIS.md`. They distinguish
proved fixed-width closure rates, conditional population error bounds,
the expected square-root-width fluctuation law, and solver-dependent numerical
estimates. A sharper weighted polynomial estimate is derived for the existing
joint clock, avoiding a spurious width factor in its projection bound.
An RMS-normalized joint clock is also described as an optional variant,
not an unnoticed change to the manuscript's clock.

Status: source-based analysis with explicit conditional derivations; no new
population-limit theorem or convergence theorem for a TP/DMFT solver is claimed.
This is not a promotion into the maintained book or code.

The follow-up optimization is in `OPTIMAL_MOVING_MEMORY.md`: exact leading
error-budget allocations for dense and both clocks, corrected moving-only NTH
accounting, the conditional NTH order threshold, and the streamed TP/DMFT
memory optimum. Its dependence on task/horizon constants and numerical time
approximation order is explicit. These optimize stated error/cost models,
not universal lower bounds across all possible representations.

The user subsequently authorized incorporation into `paper/`. Before edits,
commit `df473babba4849c80db75c2578995011f3450f37` checkpointed the manuscript,
its current assets and portable figure bundles, and this study's reports.
The revision updates the introduction, related work, definitions and discussion,
and adds `paper/comparison.tex` and `paper/comparison_appendix.tex`. It preserves
the distinction between fixed-width theorems and conditional population/solver
scalings. The root owns the main text and integration; the scoped coauthor owns
only the new comparison appendix during drafting. Integration is complete:
the final manuscript has 31 pages and compiles without warnings or unresolved
references. Section 7 occupies pages 10–11, and Appendix E starts on page 27.
The new comparison table and representative equation pages were checked
visually. The build logs and page previews are retained in
data/generated/population_accuracy_complexity_20260927/paper_revision_zukyd7ar/.
The existing radial figures are retained; no experiments were rerun.

For the user's subsequent side-by-side manuscript comparison, the supplied
attachment was saved as paper/main_alternative.tex and compiled to the separate
28-page paper/main_alternative.pdf. Only two PDF bookmark strings were adjusted;
the attachment's visible text and figure choices were preserved. The final
build has no warnings or unresolved references. Representative pages were
checked visually, and hashes verify that the current main.tex and main.pdf
were unchanged. Build logs, the attachment hash and page previews are in
data/generated/population_accuracy_complexity_20260927/alternative_manuscript_y_6wn13y/.
A scoped read-only editorial comparison used only the two supplied manuscripts
and the current draft's included comparison files; no scientific audit or new
research was undertaken.

The user chose the alternative as the working manuscript. Commit `bbfef82`
preserves both drafts before adoption. `paper/main.tex` now follows the
alternative's narrative and retains its early comparison table, low-rank
corollary and fixed-width cost calculation, with targeted corrections to
exact-closure claims, horizon/order dependence, and empirical error wording.
The previous comparison appendix was integrated with its conditional
population hypotheses and derivations. Both radial circle figures are included.
A scoped figure coauthor used only the user-designated paper figure bundle,
manifest, guide and rendered assets, recomputed the three saved sphere RMS
values, and prepared `paper/sphere_appendix.tex`; the root integrated and
shortened it into one appendix page. The original alternative snapshot was
preserved. No training, new literature search or scientific audit was performed.

Validation: the final 34-page manuscript compiles with no warnings, undefined
references or overflowing boxes. The main comparison table, radial plots,
sphere page and representative appendix pages were checked visually. The
sphere results are expressly supplementary fitted-function evidence for
ReLU, outside the smooth-activation theorems, using individually fitted
float32 Euler endpoints without a continuous-flow refinement certificate.
The synthetic training preview and redundant sphere_comparison figure are
excluded. Build logs, input hashes and PDF previews are in
`data/generated/population_accuracy_complexity_20260927/alternative_adopted_awm6bb4z/`.
The final comparison appendix starts on page 28, radial plots are on pages
12–13, and the sphere appendix is on page 34.

For the user-authorized commit and push, manuscript PDFs are retained and
LaTeX auxiliary files are excluded. Local auxiliary files were removed for
both main and alternative manuscripts, and ignore rules were extended.
Two bibliography build files from the unpublished paper_v2 checkpoint were
removed from that unpublished commit chain without changing its final tree.
The checkpoint IDs in this record now refer to the cleaned equivalents;
the original chain remains on the local branch
`codex/paper-before-aux-cleanup-20260927`. Other tasks' working changes remain
untouched. Cleanup metadata is retained in
`data/generated/population_accuracy_complexity_20260927/git_publication_u_1r0khf/`.
