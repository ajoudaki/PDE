# Response memory with deferred Gaussian queries

> **Stopped by the user on 2026-10-02. Do not resume automatically.**
> The user cancelled the campaign; the research objective was not achieved.
> All owned GPU experiments have exited, and the width-extension experiment
> was never launched. Existing evidence is preserved locally; no commit or push.

## Saved status at cancellation

- [Rank screen](RANK_RESULTS.md): all four completed width-2048 cases failed the
  preset combined-rank resource gate. This is a single-seed significance screen,
  not a reproduced empirical claim or a rejection of an entire domain.
- [Gaussian-query derivation](GAUSSIAN_QUERY_THEORY.md): exact finite-dimensional
  identities and conditional tracking arguments, with explicit remaining gaps;
  not an established population solver or a promoted theorem.
- `deferred_gaussian.py` and `check_deferred_gaussian.py`: exploratory sampler
  and completed CPU checks. No learning simulation using this sampler was run.
- Raw rank evidence: `data/generated/response_memory_gaussian_queries_20261002/rank_screen01/`.
  A filename bug overwrote some detailed per-query histories/bases; numerical
  summaries and accepted-direction records survive. The executed source is
  archived there. See the results report for this limitation.
- CPU check evidence: `data/generated/response_memory_gaussian_queries_20261002/oracle_check01/checks.json`.

Everything below records the original scope and plan; its next-action language
is superseded by cancellation. No further work is authorized without a new request.

The manuscript and shared maintained code remain unchanged.

The question is whether the paper's autonomous response-memory system can be
simulated without either a dense initialized matrix or a growing record of every
matrix query. The consequential target is accurate nonlinear population
calculations at widths otherwise inaccessible at comparable cost, not merely a
same-width speedup. The fixed Gaussian mixer and its forward/adjoint correlations
must retain their actual law.

The primary prior is Yue M. Lu's [Householder Dice](https://arxiv.org/abs/2101.07464),
which already samples adaptive Gaussian matrix actions exactly without forming
the matrix, with storage growing with the number of queries. The candidate
extension is to retain every revealed constraint, but reveal a new direction
only when the current forward or backward query has a sufficiently large
component outside the retained span. The paper's Legendre moments compress
learned weight increments; this separate approximation compresses queries to the
fixed disorder. Neither approximation should be mistaken for the other.

Scientific inputs: the explicitly authorized current manuscript and all its
included mathematics; maintained `docs/`; primary external sources. No other
study is a scientific or code dependency. Startup instructions, manuscript,
notation and relevant skills have been read by root; HEAD at creation is
`4dfa5c1ef2c5b920eda2bbc84316b189b97da92e`. Existing concurrent modifications to
`paper/main.pdf` and an unrelated study README are preserved.

Initial decision: measure the numerical dimension of the actual forward and
backward query paths, before building a large simulator. A small dimension would
justify an adaptive Gaussian oracle and a coupled error comparison. A dimension
comparable with width would defeat the proposed resource advantage in that
regime. No rank-screen result alone establishes an accuracy–cost advantage.

Scope: two tanh hidden layers, finite training data, canonical Gaussian
initialization, zero readout, squared loss, physical-time mobilities `(n,1,n)`,
the paper's learning-speed clock and raw Legendre moments. Details, thresholds,
controls and resource limits will be fixed in the experiment protocol before
execution. Generated evidence belongs only in
`data/generated/response_memory_gaussian_queries_20261002/`.

Ownership: root owns this README and synthesis; scoped theory agent owns
`GAUSSIAN_QUERY_THEORY.md`; scoped experiment agent will own its protocol,
producer and screening results. Root owns any oracle implementation. These are
cooperating authors, not independent promotion reviewers.

Next authorized action: bounded query-dimension screen and Gaussian-conditioning
derivation; proceed to an actual approximate simulator only if the dimension
screen supports a plausible advantage. Compare against exact deferred Gaussian
simulation, ordinary finite-width ensembles and other strong methods before
claiming a consequential capability. No promotion or manuscript edits.
