# Can autonomous compression beat a dimension-linear logarithmic exponent?

## Contract

Started 2026-10-05 as a new theoretical investigation requested in conversation.
The target is a width-n dense network with fixed hidden depth L >= 2, ordinary
independent Gaussian initialization, nonlinear activations, and genuinely learned
hidden features. There are m >= d training inputs on the radius-sqrt(d) sphere,
and their linear span is R^d; the numerical inequality alone is not a rank
assumption. Preserve correlated data, the existing admissible small-label regime,
and positive initialized feature-Gram gap. Do not replace the model by a shallow,
linear, frozen-feature, lazy, specially initialized or orthogonal-data surrogate.

The error is the supremum of prediction error over the complete input sphere
and all physical training times, including the fitted endpoint. The goal is
the dense network's self-variability scale. Distinguish a proved upper envelope
for that scale from comparison to the actual discrepancy of independent runs.
No stronger exact rate is imported from an unpromoted study.

Seek either (a) an initialization-only, autonomous, restartable representation
with total retained size O((log(en))^a(d)), where a(d)/d -> 0, or (b) an
impossibility theorem over an explicitly specified admissible representation
class. All instance-specific fixed coefficients, trainable state and decoder
data count. The representation may use the data and initialization but not a
future trajectory, time-indexed playback, a retained dense oracle, arbitrary-real
bit packing or uncounted computational workspace. Constants independent of n
must have their d dependence disclosed. Lower bounds requiring continuity,
Lipschitz bounds or finite precision are scoped to those assumptions.

Width tends to infinity for each fixed problem first. A sublinear exponent is
a separate assertion about the resulting family across dimensions; a fixed-d
bound does not establish uniform joint dimension/width control.

## Inputs and authority

Allowed scientific inputs: this study, the maintained docs/ and code/, the
explicit mathematical task specification, and checked external primary sources.
No other study is an input. Prior conversation identifies the question, not a
license to import unpromoted proof artifacts across study boundaries.

Read AGENTS.md, Part 1 of RESEARCH_WORKFLOW.md, docs/index.qmd and
docs/notation.qmd. The rigorous-math and conjecture-investigation skills apply.
The required custom canonical-notation skill at
/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md could not be
read (permission denied); apply the user's explicit notation instructions and
the maintained contract. No training experiments, book edits or promotion are
authorized by this study. Current initial HEAD:
3834145d910202a84824d943fe7d7f65714d96f2. The index was empty; unrelated dirty
files and other untracked studies are preserved.

## Routes and ownership

- Lead: contract, established-source inspection, synthesis and this README.
- Constructive route: a fresh scoped agent, separate CONSTRUCTIVE_ROUTE.md.
- Lower-bound route: a fresh scoped agent, separate LOWER_BOUND_ROUTE.md.
- Statistical-scale/representation audit: a fresh scoped agent, separate
  SCALE_AUDIT.md.

Independent routes receive the same target without other routes' arguments.
Their output is provisional until independently checked. No result is promoted.

## Current outcome

The requested general positive construction and general lower bound remain
open. [RESULT.md](RESULT.md) is the compact reader-facing report. No existing
compression estimate is replaced, and no result has been promoted.

The independently developed routes produced precise auxiliary statements:

- [LOWER_BOUND_ROUTE.md](LOWER_BOUND_ROUTE.md): finite-bit and bounded-Lipschitz
  decoder inequalities, a conditional spherical coefficient-ball lower bound,
  and a tight-fluctuation obstruction to obtaining growing information bounds
  at a fixed root-width tolerance. The actual neural richness/small-ball
  premise is unproved. Complete reconstruction: [LOWER_BOUND_CHECK.md](LOWER_BOUND_CHECK.md).
- [SCALE_AUDIT.md](SCALE_AUDIT.md): an all-time evolving-kernel comparison,
  conditional log-log spatial truncation of normalized fluctuations, exact
  precision accounting and the distinction between statistical covers and
  executable autonomous representations. Check: [SCALE_CHECK.md](SCALE_CHECK.md).
- [CONSTRUCTIVE_ROUTE.md](CONSTRUCTIVE_ROUTE.md): a serial Gaussian quadrature
  workspace lemma and a conditional short causal-program mechanism. Runtime
  can be enormous. The autonomous neural compiler, its regularity, whole-sphere
  comparison and selected-tolerance finite-width theorem remain missing.
  Check: [CONSTRUCTIVE_CHECK.md](CONSTRUCTIVE_CHECK.md).
- [STRUCTURAL_CHECKS.md](STRUCTURAL_CHECKS.md): exact sphere polynomial count,
  full-rank symmetry limitation, finite-parameter family cover, and the
  averaging-center identity. Check: [STRUCTURAL_CHECK.md](STRUCTURAL_CHECK.md).

Checks apply to their explicit auxiliary/conditional statements only. Each
report records the exact source hash it reconstructed. [RESULT_CHECK.md](RESULT_CHECK.md)
checks that the synthesis does not upgrade these to actual neural compression
or impossibility. Final version-bound checks are complete, including the narrow
wording corrections. Original freeze-status notes in route sources are
historical; the linked completed check reports determine current check status.
No unresolved neural premise is being called proved.

An adverse check of the constructive proposal is retained: the ordinary
unnormalized dense parameter norm has initial readout velocity of order
sqrt(n) under a positive initialized feature Gram and nonzero labels. A
width-independent derivative estimate in that norm is false. The revised
proposal explicitly uses a hypothetical typed population state and leaves
its estimates, finite compiler and identification as missing obligations.

## Sources, reproduction and next branch

The independent routes used their prompt/contract, docs/notation.qmd and the
selected maintained passages identified in their reports. The lead also read
the finite-program theorem statement and Gaussian-program definition in
docs/02-gaussian-reuse.qmd: its one-input, fixed-step feature-ascent scope does
not supply the requested general training theorem. The book's future-profile
encoding warning and fixed-program versus growing-time distinction were
respected. No other study was read.

External nonlinear-width literature was consulted for context only: Cohen,
DeVore, Petrova and Wojtaszczyk, *Optimal Stable Nonlinear Approximation*,
https://arxiv.org/abs/2009.09907, and the lower-route source cited in its report.
No external theorem is imported without a proof into any claimed lemma here.

Reproduction is mathematical: read each complete route and its named
reconstruction report; `sha256sum` identifies reviewed versions. No training
experiment or numerical approximation was run. No Git stage/commit was made.
An initial repository-wide whitespace diagnostic encountered permission
denied on an unrelated inherited migration JSON; it did not read or change
that file. Subsequent checks were limited to this study.

The highest-leverage constructive continuation is a causal Gaussian-program
compiler with quantitative temporal regularity and all-time query control,
whose accuracy exponents are independent of both d and m. The negative route
needs a representation class plus a genuine reachable-family or probability
obstruction; generic analytic entropy is insufficient. These are research
branches, not completed theorems. No new experiments are authorized by this
record alone.
