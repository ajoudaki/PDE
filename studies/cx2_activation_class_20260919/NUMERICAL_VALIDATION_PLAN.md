# Bounded activation-adapter validation plan

Frozen before implementation/execution, 2026-09-19. Author consistency work;
no training experiment, trajectory sweep, target-data fitting or width study.

Decision: does the executable finite construction implement CLOSURE_PROOF.md
(4), (5), (8), (21), with a genuinely exhaustive nested smooth dictionary,
and use a supplied general activation in both moving layers and frozen pairs?
H1 is equality with those identities. H0 is a missing response/transpose,
normalization, derivative, activation-binding, or joint-restart component.
Only finite construction and operational consistency claims can change.

Predeclared checks (deterministic, no seeds):

1. Dictionary orders 1, 2, 4, 8 (code ceilings 16,32,64,128): every valid bounded decoded code is
   retained in order, including literal duplicates; previous lists remain
   prefixes. Order 8 contains bounded probes of both action directions.
   A separately compiled finite alternating nested source graph verifies the
   response rule and frozen named-source derivatives against direct formulas.
2. Generic initialization at order 8 (code ceiling 128), Q=32 and P=16; compare its
   marks and D with a separately assembled same-compiler raw contraction and
   inverse-Cholesky normalization. Repeat once with a different activation
   descriptor to establish that initialization is activation-independent.
   Inspect retained source count, joint replay and positive-ridge mode counts.
3. A fixed asymmetric supplied state, unequal positive population/data weights,
   two nonorthogonal unit directions and a nonzero supplied readout. Check
   every moving scalar gradient by centered differences at delta=1e-6,
   the independent loss directional/energy identity, and weighted adjunction.
   Use z+sin(z)/4 and the C1,1 flat-gate ramp (not C2 at 0,1).
4. A two-row supplied dense identity-mark state checks predictions and all
   velocity blocks against the maintained finite-network evaluator for the
   smooth nonodd shifted activation 1/5+z+sin(z)/4. This is an algebraic
   normalization control, not a neural-width numerical method or training run.
5. Reconstruct initial/current pairs from the same marks; compare weighted
   RMS directly. Compare one Heun algebraic map to its two explicit stages.
   Save/reload a supplied state, repeat that one map and require exact scalar
   equality. Exercise float64 and rational 24-digit restart. Reject a mismatched
   activation descriptor and malformed/nonfinite/shape-changing callbacks.
6. At the same fixed tiny initialization (N=1,Q=8,P=4), rational precision
   24 and 36 digits: compare source-normalized arrays and one supplied-state
   field evaluation. This checks operation of the independent precision axis,
   not a convergence rate. Exercise arbitrary represented C-H3 arc parameters
   and a supplied orthogonal-neighborhood law through the law adapters, without
   assigning the maintained tanh horizon to the general activation.

Pass gates: algebraic float comparisons absolute/relative tolerance 2e-11;
finite-difference gradients/energy relative-or-absolute tolerance 3e-6;
rational 24/36 scalar discrepancies below 1e-18 for the declared tiny case;
restart equality exact; all requested arrays finite and all positive pivots
resolved. A threshold violation is failure; overflow, unresolved pivots,
resource exhaustion or an invalid derivative evaluation makes that check
inconclusive until a code defect is identified. No scientific parameter search.

Budget: one process, one numerical thread, 120 CPU seconds and 120 wall seconds
per suite, maximum 1 GiB address space, at most three full suite attempts
(initial, necessary defect correction, final verification). No convergence
sweeps and no positive-time training trajectory. Stop after passing the fixed
suite or reaching the budget. Code corrections must be logged before rerun;
the original thresholds and supplied states remain fixed. Record source hashes,
command/environment, all failures and final raw log in
data/generated/cx2_activation_class_20260919/activation_numerics/.

Pre-execution clarification: the enumeration uses code ceiling 16N and the
specified ridge 2^-N. This is a cofinal nested enumeration of the same language.
It reaches both oriented bounded action probes at N=8. A literal code ceiling
N with ridge 2^-N would already require >38 decimal digits to distinguish the
ridge at code 126 amid duplicate columns; no such float64 success is assumed.
This clarification was made analytically before any validation run.
