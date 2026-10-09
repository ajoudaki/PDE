# Tensor-program size for stopped prediction observables

## Contract and authority

New theoretical question, requested 2026-10-08: can a TP-style numerical
program compute a fixed number of stopped-training prediction observables
to constant-comparable dense-versus-dense variability, with retained
program/state size polynomial in log(en) and polynomial in the sample,
input-dimension and inverse-gap parameters? Distinguish this storage
question from the stronger polylogarithmic total-runtime question.

Use the canonical Gaussian, zero-readout, all-layer nonlinear network,
fixed hidden depth, existing analytic activation class with bounded strip
derivative but possibly unbounded real values, and the stated label/gap
scope. The main reference is gradient flow stopped at a prescribed
training-loss threshold. A same-step dense-GD comparison is a separate
statement, not a substitute. The stopping threshold may need to depend on
the desired dense-variability accuracy; expose that choice explicitly.

The user clarified that a fixed number of unlabeled query inputs ARE
supplied at initialization. The principal contract is therefore a finite
declared panel, not a decoder for arbitrary inputs revealed later. A
terminal table of answers is not the intended numerical program; seek
an executable small-state construction. Post-setup queries remain a
separate stronger question and must not silently be substituted.

Count retained program instructions, constants, matrices, random seeds,
precision requirements and evaluation workspace honestly. A scalar output
table for queries known beforehand is not a learned query decoder. A
formal expectation node is not a numerically evaluated constant-cost
instruction. A generic dense simulator with a short loop is not by itself
a small-space execution. No future-trajectory oracle, hidden function
state, arbitrary real-number encoding or uncounted random-access dense
Gaussian oracle is allowed. A terminal predictor need not be a restartable
training system unless that stronger claim is explicitly made.

Permitted research inputs: established docs/code and published primary TP
literature. The user additionally approved directly relevant proofs in
initialization_panel_compression_20261008,
integrated_general_compression_20261004, and
adaptive_clock_compression_20261008. Read actual dependencies and current
corrections; do not infer their validity from prior conversational claims.
Unrelated studies remain excluded. No empirical campaign, paper changes,
promotion, or Git writes are requested.

## Bounded routes

1. Lead: freeze the computational contract; investigate constructive
   terminal evaluation, stopping, and numerically executable descriptions.
2. TP representation route: derive actual scalar/memory dependencies for
   finite training programs; distinguish exact limit formulas from a
   polylogarithmic retained algorithm and identify a provable compiler.
3. Terminal approximation route: investigate a finite predictor for
   the declared queries (or a stronger post-setup decoder where feasible),
   with polynomial data dependence and explicit accuracy, using analytic
   or probabilistic structure rather than a formal integration oracle.

Each route must return a proved statement or concrete construction and
the exact unclosed bridge. Initially allow one independent round, one
focused repair per genuinely distinct mechanism, then reconstruction of
the strongest candidate. Do not equate a failed route with a no-go
theorem. No assumption that an affirmative theorem exists.

## Current state

Declared-query and source clarifications received. The bounded route
round and focused repairs are complete. See RESULT.md for the synthesis.

- STREAMED_STOPPING.md adds a finite streamed Euler execution and an
  own-loss stopping comparison to the authorized third-power retained
  response-state theorem. STOPPING_CHECK.md reconstructs the new
  deterministic lemmas independently from their hypotheses.
- TP_REPRESENTATION.md supplies the fixed-Euler population recursions,
  shared-graph/table counts, singular-covariance numerical integration
  bridge, and the precise distinction from a selected small-state
  optimizer. Its focused dependency check includes the adaptive-clock
  source theorem and preserves its explicit lower-logarithm term.
- TERMINAL_APPROXIMATION.md proves a restricted nonlinear population
  endpoint theorem for one hidden layer and one training sample, with
  a bounded positive activation, an actual RMS dense-pair comparison,
  and a finite polylogarithmic-bit predictor. It is not the requested
  full-scope standard-TP theorem. TERMINAL_CHECK.md independently
  reconstructs its exact clock, mean bias, variance and numerical
  approximation/precision arguments; minor normalization and cost
  wording corrections are applied to the candidate.

The main remaining claims are a general polylogarithmic unrolled or
bit-bounded standard-TP computation and, if required, a relative bound
against stopped-query variability itself. The general positive result
uses the paper's whole-trajectory variability benchmark and counts
retained real coordinates. Total setup and Euler work remain separate.

The lead read each complete route and reconstructed the stopping,
Euler-buffer, covariance-continuity, shallow feature-clock,
empirical-root bias, query-variance and analytic-approximation arguments.
No unrelated research study was imported. The preceding conversation's
Euler analysis remains a diagnostic example, not a canonical neural
lower bound. Concurrent paper and other-study edits in the shared
checkout were left untouched; no Git write was made by this study.
