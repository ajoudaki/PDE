# PDE convergence and arbitrary-accuracy program

This is one chronological investigation of whether the finite-cutoff operator
PDE converges strongly enough to support an arbitrary-accuracy theorem.

## Chronology

1. [`01_proof_audit`](01_proof_audit/) contains the proof-obligation
   framework, protocol, source, mathematical checks, and the two completed
   frozen trajectories.
2. [`02_lean_salvage`](02_lean_salvage/) contains the bounded follow-up
   diagnostics. Its ad hoc runner was not preserved; the report and raw
   results were.
3. [`03_bridgeability`](03_bridgeability/) repairs the even-shell parity flaw
   and tests the correct odd Hermite ladder. Its report, runner, manifest, and
   three results are all at the phase root.
4. [`04_scalar_stress`](04_scalar_stress/) is the one-input Hermite ladder.
5. [`05_tail_and_compactness`](05_tail_and_compactness/) combines the
   high-to-low commutator experiment with the final coupled Cauchy ledger.
   The two runners are at the phase root and their data are under `results/`.

Two explicit compatibility links remain at this program root:

- `pde_proof_obligation_audit` points to phase 01;
- `activation_linearity_smoking_gun` points to the operator-PDE activation
  source.

They preserve the original runners and frozen source hashes without keeping
five scattered links or another copied implementation. New convergence work
should import phase 01 and the operator-PDE source explicitly rather than add
another compatibility link.

Current reading: parity-aware bookkeeping improves several local diagnostics,
but replicated aggregate Cauchy contraction remains unproved. Strong
source-weighted Hermite compactness is still the central analytic obstruction.

