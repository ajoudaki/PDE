# PDE convergence audit and arbitrary-accuracy program

This is one chronological investigation of whether the finite-cutoff operator
PDE converges strongly enough to support an arbitrary-accuracy theorem.

## Chronology

1. [`01_proof_audit`](01_proof_audit/) contains the proof-obligation
   framework, protocol, source, mathematical checks, and the two completed
   frozen trajectories. This phase is incomplete: none of its seven proposed
   scientific gates passed, and only two \(P=5\) cubature trajectories
   completed.
2. [`02_lean_salvage`](02_lean_salvage/) contains the bounded follow-up
   diagnostics. Its ad hoc runner was not preserved; the report and raw
   results were. Its headline \(P=5,15,35\) noncontraction interpretation is
   superseded by phase 03's exact parity analysis.
3. [`03_bridgeability`](03_bridgeability/) repairs the even-shell parity flaw
   and tests the correct odd Hermite ladder. Its report, runner, manifest, and
   three results are all at the phase root. Its lifted outgoing-tail
   contraction is later qualified by phase 05: this is a lifted
   boundary/source diagnostic, not the actual trained high-shell velocity.
4. [`04_scalar_stress`](04_scalar_stress/) is the one-input Hermite ladder.
5. [`05_tail_and_compactness`](05_tail_and_compactness/) combines the
   high-to-low commutator experiment with the final coupled Cauchy ledger.
   The two runners are at the phase root and their data are under `results/`.
   Its `COMPACTNESS_REPORT.md` is the authoritative final convergence-status
   report.

Two explicit compatibility links remain at this program root:

- `pde_proof_obligation_audit` points to phase 01;
- `activation_linearity_smoking_gun` points to the operator-PDE activation
  source.

They preserve the original runners and frozen source hashes without keeping
five scattered links or another copied implementation. New convergence work
should import phase 01 and the operator-PDE source explicitly rather than add
another compatibility link.

Current reading: this is a convergence audit, not a convergence result. No
compact-time or all-time arbitrary-accuracy theorem was proved, and no
replicated aggregate Cauchy contraction was observed. The final open
compact-time bundle is collective source-Hermite tail compactness or strong
reachable regularity, uniqueness, and cutoff-uniform forced stability.
Ordered dense-limit identification, trained-depth homogenization, and all-time
control remain separate obligations.
