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

Owner: the main assistant in this task. No agents or training experiments.
The paper and shared code are not modified by this analysis.

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
No promotion or repository commit is requested.

The follow-up optimization is in `OPTIMAL_MOVING_MEMORY.md`: exact leading
error-budget allocations for dense and both clocks, corrected moving-only NTH
accounting, the conditional NTH order threshold, and the streamed TP/DMFT
memory optimum. Its dependence on task/horizon constants and numerical time
approximation order is explicit. These optimize stated error/cost models,
not universal lower bounds across all possible representations.
