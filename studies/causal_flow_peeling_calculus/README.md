# Causal Flow Peeling Calculus

This is a study record, not an established-library entry. Historical claims and
review labels below retain their original scope; consult the
[reconciled research map](../project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md)
for current qualifications and the [maintained library](../../docs/README.md)
for accepted self-contained presentations.

## Program identity

This study develops a proof-carrying, recursive calculus for finite-step-to-continuous-time mean-field feature-learning limits.  Its working name is **Causal Flow Peeling Calculus (CFPC)**.  The name is provisional: it describes the intended mechanism, not an established theorem.

The motivating target is the one-sample, three-hidden-layer nonlinear feature-learning model, with arctangent activation as the first concrete case.  The program is not allowed to count a reformulation, an infinite response hierarchy, or an equally difficult auxiliary limit as progress.  A proposed calculus survives only if its reusable rules discharge the difficult probabilistic and analytic obligations on a previously resolved ladder before they are applied to the target.

## Provenance and isolation boundary

This program was opened on 2026-08-24 in response to the request to investigate a machinery-level extension of Mean Field Peeling (MFP).

During the exploratory design phase, the supervising thread may read project material only under `studies/mean_field_peeling/`.  It must not inspect other project studies or prior proof attempts.  In particular, `studies/renormalized_causal_gaussian_calculus/` is an independent parallel study and is strictly outside the information boundary.  Clean-slate design agents receive a self-contained mathematical specification and no repository access.

All artifacts created by this program belong under this directory.

## Frozen success criterion

A successful calculus must provide all of the following through a stable collection of typed objects and reusable inference rules:

1. a finite-step mean-field semantics for adaptive forward and backward signals;
2. quantitative, composable certificates for width error, one-step consistency, stability, and time accumulation;
3. a restartable autonomous one-time limiting state, rather than a hidden dependence on the full training history or an unclosed infinite hierarchy;
4. compact-time convergence of the network state and raw tangent kernel after mesh removal;
5. a depth-recursive construction whose rules do not change qualitatively at the three-hidden-layer case;
6. recovery, without importing their tailored proofs, of the resolved ladder: deep linear networks of hidden depths 1, 2, and 3; one-hidden-layer networks with a generic admissible activation; and the two-hidden-layer arctangent model.

The desired Euler comparison must distinguish local truncation from global error.  In particular, a first-order global flow approximation normally requires a local defect of order `O(h^2)` together with a stable accumulation rule; an undifferentiated claim of `O(h)` “per step” is not sufficient.

## Mandatory rollback gates

The program must be redesigned or abandoned if any of these occurs:

- a node certificate contains, as an unproved premise, the same adaptive random-operator convergence needed by the original target;
- closure requires retaining an unbounded response hierarchy without a proved resummation or finite sufficient statistic;
- the probability rule assumes fresh Gaussianity after noiseless adaptive observation without an influence, cavity, conditioning, or equivalent correction theorem;
- stepwise errors cannot be made uniform enough to pass from fixed meshes to compact time;
- a ladder case can be recovered only by inserting a model-specific identity that is not an instance of a reusable rule;
- the state is called autonomous only by encoding the entire past as a nominal “state”;
- the depth-three rule introduces a qualitatively new oracle not already certified by the calculus.

## Initial stages

1. Reconstruct MFP at the level of its typed normal forms, peeling invariant, compiler rules, probability bridge, and fixed-depth recursion.
2. Compare several isolated machinery designs and identify their precise master estimates.
3. Freeze a contract, typed evidence ledger, and adversarial audit before substantial theorem-building.
4. Build and test the calculus on the resolved ladder in increasing order of complexity.
5. Use multi-input configurations selectively as discriminating pressure tests.
6. Attempt the three-hidden-layer arctangent target only after all earlier gates pass.

## Current claim level

The exploratory program is complete.  Its decisive synthesis is
[Machinery Verdict and Exact Proof Frontier](MACHINERY_VERDICT_AND_PROOF_FRONTIER.md).

The underlying calibration ladder is mathematically established through
Gaussian-seed two-hidden-layer arctangent: linear depths one through three and
generic nonlinear depth one follow reusable finite-program/coordinate-flow
rules, while the depth-two arctangent theorem uses mobility flattening,
Gaussian-seed clipping, width-uniform Euler stability, and fixed-program MFP.
That last theorem remains valid, but it does **not** pass the newer
“general calculus only, no tailored recovery” probe.

No candidate recovered the full depth-two arctangent flow solely from the
proposed extensible completion rules.  Universal chaos, ordinary Koopman
continuation, finite-query compression, ambient energy stability, absolute
chronological forests, laminar colored BBGKY, Gaussian transport,
square-exponential cavity estimates, random-matrix smoothing, entropy/LDP,
operator Dyson closure, weak compactness, typed Wick renormalization,
Gevrey/Borel continuation, and gradient-geometric compression all failed
explicit gates recorded in the
[authoritative evidence ledger](EVIDENCE_LEDGER.md).

The common unresolved object is a width-uniform **forced causal tangent /
occupation theorem** for the exact defects generated by source peeling,
truncation, and time discretization, together with an effectively truncatable
one-time representation of their source actions.  Ambient versions of that
theorem are false.  Rephrasing it as a marked local law, a Borel-sector bound,
a tangent spectral law, or a finite-action compression does not make it
easier.

The most credible future program is a dynamical marked-cavity and
forced-causal-response semigroup theory, with MFP retained as the fixed-mesh
compiler.  It must propagate subexponential rather than subgaussian hidden
tails, exploit the bounded arctangent logarithmic derivative, prove stability
on a forced causal tube, and derive effective restart/truncation.  This is a
concrete research program, not a completed result.

Preregistered experiments support stable behavior on sampled reachable
directions and the predicted marked-neuron versus bulk anisotropy, but the
locked occupation experiment was inconclusive and exact rare-event
counterexamples forbid interpreting those samples as a proof.

No three-hidden-layer convergence theorem or completed autonomous IDE is
claimed.
