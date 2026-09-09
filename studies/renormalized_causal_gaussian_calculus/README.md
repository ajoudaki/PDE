# Renormalized Causal Gaussian Calculus Program

**Short title:** RCGC Program  
**Status:** exploratory probe completed 24 August 2026; validation ladder
passed, D3 not resolved  
**Scientific target:** determine whether one extensible causal Gaussian
calculus can prove the positive-time infinite-width limits of the resolved
validation ladder and then decide the unresolved three-hidden-layer
arctangent model.

This is a new study. It does not resume the paused
[D3 Arctan Closure Program](../d3_arctan_closure_program/), and no claim from
that program is silently promoted here. The paused program is an evidence
source and a hostile regression suite.

## Validation ladder and hard gate

The calculus is developed in this order:

1. identity activation with one hidden layer;
2. identity activation with two hidden layers;
3. identity activation with three hidden layers;
4. a regular generic activation with one hidden layer;
5. arctangent activation with two hidden layers; and only then
6. arctangent activation with three hidden layers.

A stage passes only when the answer and the compact-time finite-width
identification follow from the same typed intermediate language, generic
rewrite rules, and generic analytic certificate rules used at earlier
stages. Reusing a model-specific spectral invariant, cyclic lift,
characteristic identity, or cavity estimate as an axiom does not pass. A
special simplification is admissible only when a general rewrite rule derives
it from the model syntax.

The unresolved stage is not opened merely because a plausible candidate IDE
has been written. Every preceding stage must pass the six promotion gates in
[`RESEARCH_CONTRACT.md`](RESEARCH_CONTRACT.md).

## Program thesis

The proposed proof object has three layers:

1. an exact typed compiler from finite-width forward/backward/gradient syntax
   to a causal action program;
2. a renormalized dynamic Gaussian layer which retains all order-one
   same-source returns as causal response operators and assigns a width grade
   to every unresolved excursion; and
3. a mesh- and cutoff-uniform analytic backend which turns fixed finite
   Gaussian programs into a continuous-time convergence theorem.

The study succeeds only if these become reusable theorems. Naming the
unresolved depth-three response estimate as a calculus rule would be a
failure, not a solution.

## Authoritative files

- [`RESEARCH_CONTRACT.md`](RESEARCH_CONTRACT.md): exact model family,
  observables, limits, anti-escape clauses, and promotion gates.
- [`CALCULUS_SPECIFICATION.md`](CALCULUS_SPECIFICATION.md): typed IR,
  finite and limiting semantics, rewrite families, and open soundness
  obligations.
- [`TAME_NATURAL_GATE_CLASS.md`](TAME_NATURAL_GATE_CLASS.md): reusable
  nonlinear activation interface containing an infinite reciprocal-polynomial
  family.
- [`EVIDENCE_LEDGER.md`](EVIDENCE_LEDGER.md): claim-level status.
- [`APPROACH_REGISTRY.md`](APPROACH_REGISTRY.md): distinct machinery routes
  and reopen conditions.
- [`SOURCE_MAP.md`](SOURCE_MAP.md): provenance and authoritative upstream
  artifacts.
- [`PROBE_REPORT.md`](PROBE_REPORT.md): terminal synthesis, gate results,
  falsified rules, exact D3 blocker, and corrected machinery frontier.
- [`linear_fixed_depth/`](linear_fixed_depth/): the first common-calculus
  validation theorem, covering all fixed linear depths at once.
- [`generic_l1/`](generic_l1/): the generic one-hidden-layer gate.
- [`arctan_l2/`](arctan_l2/): the nonlinear one-action gate.
- [`arctan_l3/`](arctan_l3/): base gates passed; the D3 calculus execution
  is attempted but not promoted.
- [`compiler/`](compiler/): executable exact-syntax compiler and regression
  tests; it emits proof obligations but does not decide convergence.
- [`audits/`](audits/): isolated designs, theorem-invocation checks, and
  hostile reconstructions at their actual claim levels.

Experiments, if any, must be preregistered under `experiments/` before code is
run. They can change route weights but cannot promote a proof claim.
