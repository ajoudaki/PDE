# Exact two-hidden-tanh limit for opposite-label pairs

2026-09-20. Surgical theoretical investigation requested by the user. New study;
only established `docs/` and this study's own artifacts are scientific inputs.
Earlier closure-study conclusions are questions/motivation, not imported lemmas.

## Contract

Two unit normalized directions x_+/sqrt(2), x_-/sqrt(2), correlation k in
[-1,1), equal masses, labels +1 and -1. Canonical bias-free two-hidden tanh
network, stored initial variances (1,1/n,1/n^2), mobilities (n,1,n), unhalved
probability-weighted square loss; actual middle matrix and transpose. Target:
strong autonomous population GF on every separately fixed physical horizon,
identified with actual finite GF, retaining both hidden populations. No changed
optimizer, frozen layers, fresh independent transpose or geometry-dependent
initialization. Constants may deteriorate as k approaches one.

The existing all-law short-time theorem is a starting point, not the target.
Separate conditional a priori estimates, controlled approximations, and an
actual extended exact-network limit. No new numerical experiment is planned.
Use investigate-conjectures and solve-math-rigorously. Work sequentially; stop
routes at a concrete missing estimate instead of expanding unclosed algebra.

## Routes and stopping rules

1. Derive the symmetric one-residual flow and normalized readout-contrast law
   directly from the exact population equations. Test whether this also bounds
   the source responses needed for continuation.
2. Examine whether physical dissipativity survives in the frozen-source
   derivatives used by the Gaussian calculus. Stop if the required cancellation
   is absent, and identify exactly what a substitute estimate must control.
3. If necessary, use symmetry-preserving action approximations to separate a
   uniform fitting/finite-travel estimate from the unresolved approximation
   compactness or causal-tail estimate. Do not infer the latter from energy.

## Startup and permitted sources

HEAD 4f2a590816d92dddcedc4407c729ca540f8450cd. Tracked status empty at startup;
no Git mutation or established-source edit authorized or performed.
Read AGENTS.md, RESEARCH_WORKFLOW.md Part 1, docs/README.md, docs/NOTATION.md,
and the required skills. Relevant established sources: global_nonlinear.md
C.4 (exact local model), C.4.5.1 (symmetry/feature clock), C.4.6.2 (signed
physical response), C.4.7.9 (finite action construction and comparison),
C.4.7.10.A (finite-source cap and limit), C.4.9.A (accumulated-force control),
special_data_limits.md J.1 (adaptive-tail and coordinate obstructions), and
the finite Gaussian/common-action constructions as needed.

## Result of the surgical pass

[RESULTS.md](RESULTS.md) contains the complete new argument and route audit.
**The requested exact-network extension was not achieved.** The exact
arbitrary-angle global population limit remains open. The results below are
partial calculations, not a successful resolution of that request.

The conditional calculation is that the single-residual geometry generalizes
to every k<1 without orthogonality. The initialized upper contrast
kappa(k)=E[(H_+^2(0)-H_-^2(0))^2]/4 is strictly positive, explicitly computable
by two Gaussian integrations, and has upper and lower bounds proportional
to 1-k. Along every existing symmetric exact strong flow:

- L(t)<=exp(-4 kappa t);
- total raw travel before fitting is at most 1/sqrt(kappa);
- a finite construction endpoint is a finite raw state with positive
  residual, positive useful contrast and a nonzero gradient.

These estimates are unconditional on the established short-time branch,
conditional on existence beyond it. They do not assume that continuation
has already been proved.

A data-dependent reflection symmetrization of the book's dense finite-action
hierarchy supplies an approximation-level theorem: every sufficiently
large order has a global fitting flow, with L_N(t)<=exp(-2 kappa t) and
total physical travel <=sqrt(2/kappa), uniformly in order. These are the
original gradient equations for each approximation, with no new optimizer
or layer-rate change. This auxiliary hierarchy is not claimed to equal
the earlier fixed p=1 dictionary. Its whole-circle predictors have
subsequences converging uniformly for all times, including their fitted
endpoints. They agree with canonical GF on the established local interval.
Beyond it, uniqueness of the subsequential predictors and identification
with exact-network GF remain unproved.

Two tempting routes were closed off promptly:

- Full physical variation includes a negative Gauss--Newton term that is
  absent from the frozen-source derivatives of the Gaussian calculus.
  Directly substituting one response equation for the other is invalid.
- The book's noncommuting two-control vector fields rule out extending
  the orthogonal gate-straightening coordinate to correlated inputs.

The remaining obligation is a uniform causal backward-field tail/stability
estimate plus noncircular action-error consistency, or a finite-program
construction that supplies both. Bounded energy, protected contrast, finite
travel and predictor compactness alone do not provide this estimate.
Direct control of contracted response fields is a possible next route,
not a result of this pass. The follow-up below tested its Gaussian-projection
version and did not obtain the needed control.

## Further attempt: failed

After the user rejected overstating the partial outcome, a further sequential
attempt checked direct Gaussian projection of the contracted response,
averaged response bounds, and whether tanh saturation removes the obstacle.
[FAILED_FOLLOWUP.md](FAILED_FOLLOWUP.md) records the calculations and their
limitations. Gaussian projection recovers only the existing L2 action bound;
the other approaches did not supply an extension either. No unconditional
extension or substantial new exact-dynamics result was proved. This is a
failure to achieve the objective, not evidence that the objective is false.

## Internal check and reproduction

Lead-only mathematical check, with full derivations in RESULTS.md:
physical-time factors; actual adjoints; Gaussian covariance differentiation
and singular endpoints; reflection and ridge-filter symmetry; characteristic
continuation at fixed order; uniform coefficient-to-raw contraction; and
all-time predictor compactness. The exact-flow theorem's continuation
premise and the approximation theorem's lack of exact-network identification
are retained in every conclusion. No independent-review or promotion claim.

Reproduction is verification of the displayed derivations against the named
book units. Source hashes are recorded in RESULTS.md. No experiment,
simulation, maintained-code edit, established-theory edit or Git mutation
was performed. Unrelated concurrent tracked edits were left untouched.

Checked RESULTS.md SHA-256:
`55104626b5f678651ff6c7af575f5a3477304ac00982666c04b57c8192ddc414`
(updated after correcting the outcome description).
A scoped Python check verified every recorded established-source hash,
local Markdown links, paired display delimiters, and trailing whitespace:
PASS. These document checks supplement, and do not replace, the analytic
check above. No further route is running after this bounded pass.
