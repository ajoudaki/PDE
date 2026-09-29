# Low-order response memory as a learning mechanism

29 September 2026. New research direction requested by the user: study the
finite-order autonomous closure in its own right, rather than its error to a
dense network. Seek an organizing principle for deep nonlinear learning.

## Contract

Use the residual-activity clock, constant forward prefix and zero backward
prefix, canonical mobilities, and the actual shared fixed Gaussian matrix and
transpose. Start with q=1 and compare q=2,3 structurally. Retain multiple
correlated inputs, fixed finite depth, tanh as a principal example and zero
initial readout; identify any narrower analytic benchmark. No block initializer,
independent fresh mixing, frozen features, or population independence assumption.
Finite width has O(Lmnq) evolving scalar entries, not O(1) global scalar state.

The scientific target is a precise explanation in terms of memory, feature
movement, feedback and an energy/alignment identity, with a checkable limit to
any proposed global-fitting claim. Exact identities, sufficient conditions,
heuristic interpretations and open global statements must remain distinct.

Inputs: the problem's defining closure equations, supplied self-contained in
MODEL.md; maintained docs/index.qmd and docs/notation.qmd; any directly needed
established docs/ results. No other study or unpublished paper result is a
scientific dependency. The manuscript is not being edited. The research and
rigorous-math skills govern the investigation.

## Bounded work

Parent derives low-order filters, memory pairings and the synthesis. Two fresh
scoped routes independently examine direct learning/alignment and stability/
counterexamples. Scope is mathematical analysis and inexpensive deterministic
identity verification, at most 120 seconds CPU for those checks. No neural
training campaign or new literature survey. An external result, if needed,
must be verified against a primary source; no novelty claim is planned.

All new source/proofs stay in this directory; generated verification products
go to data/generated/low_order_memory_mechanism_20260929/. No Git operations,
paper changes, or changes to maintained code are planned.

## Status

First theoretical investigation complete. Read INSIGHT.md for the synthesis:
adaptive reciprocal associative memory, where moving feature addresses change
the use of accumulated error credit. Exact higher moments are weighted
historical derivatives under the stated regularity, and the moment filter has
a dimension-free energy balance. These exact identities hold for the closure's
own responses at every finite width and order.

The two scoped reports LEARNING_GEOMETRY.md and STABILITY_PRINCIPLE.md were
read completely and checked against the parent derivation in
PROJECTION_MECHANISM.md. They give exact direct loss/alignment identities;
global-in-physical-time existence for every finite tanh closure; and global
exponential fitting for q=1, one sample, scalar width, arbitrary depth, zero
readout and almost every Gaussian initialization, with no small-label
restriction. A deterministic positive-matrix extension allows arbitrary width.
Neither this benchmark nor filter passivity proves general wide-Gaussian or
multi-input fitting. The scalar rate is not uniform in depth or initialization.

The algebra verifier was run once, for q=1,...,6, in approximately 0.03 seconds:

```
OPENBLAS_NUM_THREADS=1 python -B studies/low_order_memory_mechanism_20260929/check_identities.py \
  --output data/generated/low_order_memory_mechanism_20260929/identity_check_01
```

All checks passed; maximum absolute discrepancy 4.51e-13, tolerance 1e-9.
The generated checks.json includes source hashes and the complete check list.
Use a fresh output directory if reproducing. No neural training experiment,
external literature claim, paper edit, Git operation, or code promotion was
performed. These are internally derived results, not promoted book theorems.

## Continuation: learned function and intrinsic geometry

The user requested a substantially deeper continuation of this same
investigation, including the final function on the entire input space. The
canonical MODEL.md and existing results are unchanged. This continuation is
theoretical; deterministic algebra verification is allowed within the existing
120-second compute ceiling, but no neural experiment is authorized or planned.

Three fresh routes initially receive only MODEL.md and the notation contract:
finite_memory_function owns FINAL_FUNCTION_ROUTE.md (test-function and
representer identities); finite_memory_geometry owns
INTRINSIC_GEOMETRY_ROUTE.md (memory geometry and relearning);
finite_memory_learning owns DIRECT_LEARNING_ROUTE.md (reachable fitting and
small-label terminal function). The parent owns activity-budget spatial bounds
and the synthesis. These are finite-closure results; no dense comparison,
population independence or unrestricted global fitting may be substituted.
After each route obtained concrete equations, overlapping terminal-function
results were shared explicitly for cross-checking and further derivation.

This continuation is complete. The current synthesis is
[DEEPER_INSIGHT.md](DEEPER_INSIGHT.md). The previous synthesis remains valid;
no previous theorem is superseded. New conclusions are:

| Claim | Scope and status | Complete proof |
|---|---|---|
| Final predictor = final-feature representer part + training-invisible historical part | Exact at any attained state, any finite m,n,q,L; terminal reading requires an endpoint | FINAL_FUNCTION_ROUTE.md |
| Historical part survives actual interpolation | Proved one-sample, two-hidden-layer, width-two small-label examples on a positive-probability Gaussian set, every fixed q | FINAL_FUNCTION_ROUTE.md |
| Universal one-sample activity path and strictly positive cubic feature feedback | Exact path reduction; local sum-of-squares feedback at any fixed depth; small-label endpoints and compact-test expansions | ACTIVITY_AND_FUNCTION.md, DIRECT_LEARNING_ROUTE.md |
| First q-dependent terminal coefficient occurs at degree six; finite-q label map is generically C5, not C6 | Proved one sample, two hidden layers, fixed finite n,q, zero readout, tanh; almost-sure nonzero effects include a fixed same-radius circle test point | DIRECT_LEARNING_ROUTE.md |
| Shared clock produces one leading nonlinear off-training function under label relearning | Proved under an explicit local contraction margin at a fitted augmented state, any finite m,n,q,L | INTRINSIC_GEOMETRY_ROUTE.md |
| Closed label cycle can change unseen predictions at first order | Proved conditional local theorem, with a reachable scalar Gaussian example for each fixed q | INTRINSIC_GEOMETRY_ROUTE.md |
| Finite total activity implies a terminal predictor on the whole domain | Proved conditional on finite activity; compact-uniform and L2(mu) for every probability law mu; spatial Lipschitz bound independent of n,q under fixed initial-operator/activity bounds | ACTIVITY_AND_FUNCTION.md |

The parent read all four source reports completely, including the final
reachable-state proof and the same-radius corollary. The function route
independently checked the learning route's sixth-order expansion, parity,
Gaussian nonvanishing argument and differentiability conclusion. The learning
route checked the parent's arbitrary-depth cubic coefficient and mobility
normalization; the function route checked the parent's activity-budget bounds
and whole-input convergence proof. These are internal study checks, not
independent promotion reviews. The parent supplied the scalar clock-drift
witness after the geometry route had proved its conditional theorem; that
route checked and incorporated the witness. The multi-input initialization
corollary in ACTIVITY_AND_FUNCTION.md is a direct parent deduction from the
checked local-return theorem.

Deterministic verification (no training) is in check_function_identities.py:
whole-function velocity vs the raw moment chain rule; terminal projection
and norm decomposition; arbitrary-depth cubic sum-of-squares identity;
local-response elimination; and the explicit scalar witness's sign identity.
Thirty checks passed with maximum absolute discrepancy 1.71e-13 (tolerance
1e-9). The final run and source hashes are under
data/generated/low_order_memory_mechanism_20260929/function_identity_check_03/.
Earlier run directories are preserved with their own source hashes. Each run
took under 0.1 seconds, within the original compute budget. Reproduce with:

```
OPENBLAS_NUM_THREADS=1 python -B studies/low_order_memory_mechanism_20260929/check_function_identities.py \
  --output data/generated/low_order_memory_mechanism_20260929/function_identity_check_NEW
```

The remaining general fitting question is still open; no all-label,
width-limit or statistically beneficial generalization theorem follows.
Newly exposed mechanisms concern actual function selection, including effects
that may be helpful or harmful. No training experiments, paper changes,
Git operations or scientific promotion were performed in this continuation.
