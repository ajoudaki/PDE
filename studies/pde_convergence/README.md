# PDE convergence and arbitrary-accuracy program

These experiments form one chronological attempt to bridge the successful
finite-cutoff operator PDE to a cutoff-uniform, arbitrary-accuracy result.

## Chronology

1. [`01_proof_audit`](01_proof_audit/) freezes the full proof-obligation and
   software-audit framework.
2. [`02_lean_salvage`](02_lean_salvage/) records the smaller completed
   diagnostics. Its exact ad hoc mini-runner was not preserved; the report,
   analysis, and seven raw archives were.
3. [`03_bridgeability`](03_bridgeability/) repairs the even-shell parity flaw
   and tests the admissible odd Hermite ladder.
4. [`04_scalar_stress`](04_scalar_stress/) isolates the source-Hermite issue in
   a one-input model through degree 13.
5. [`05_tail_and_compactness`](05_tail_and_compactness/) contains the
   high-to-low commutator experiment and the final coupled Cauchy ledger.

Current reading: parity-aware bookkeeping improves the hierarchy, and some
per-mode tail diagnostics contract, but replicated aggregate Cauchy
contraction was not demonstrated. A strong source-weighted Hermite compactness
estimate remains the central analytic obstruction.

The compatibility links named `activation_linearity_smoking_gun` and
`pde_proof_obligation_audit` preserve historical sibling paths expected by the
unedited runners. The actual dependency copies are retained in phases 01 and
05; the links are not additional implementations.

