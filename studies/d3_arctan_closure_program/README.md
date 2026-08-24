# D3 Arctan Closure Program

**Status:** paused on 23 August 2026 without a proof or a canonical-flow
counterexample.

This directory consolidates the complete effort to prove the strict
single-source, autonomous, one-time operator-IDE limit for the one-sample
vanilla arctan MLP with three hidden layers, including compact-time
finite-width convergence and the raw tangent kernel.  The architecture and
claim were not weakened during the program.

## Authoritative reading order

1. [Frozen core contract](FROZEN_CORE_CONTRACT_2026-08-23.md) — exact model,
   topology, convergence claim, and anti-escape clauses.
2. [Core evidence ledger](CORE_EVIDENCE_LEDGER_2026-08-23.md) — authoritative
   claim-level status, including the paused contract summary.
3. [Approach registry](APPROACH_REGISTRY_2026-08-23.md) — route history and
   the superseding paused proof frontier.
4. [Annealed audit and signed Abel reduction](annealed_audit_and_signed_abel.md)
   — detailed exact derivations, counterexamples, and Sections 25--28 from
   the final isolated audits.
5. [Final convergence audit](FINAL_CONVERGENCE_AUDIT.md) — the conditional
   closure from the middle-query tail to compact-time state and raw-kernel
   convergence.
6. [Rigorous theorem audit](RIGOROUS_THEOREM_AUDIT_2026-08-23.md) — what can
   and cannot be invoked from Tensor Programs, DMFT/GFOM/AMP, and sequential
   deep mean-field results.

## Exact pause frontier

The first open rung is C-13: uniformly on compact feature time, prove a
width- and cutoff-uniform \(\psi_1\) (or equivalent moderate-moment) envelope
for

\[
R_{2,i}(t)=\Gamma_{2,:i}^{\mathsf T}B_3(t)
+\int_0^tX_{2,i}(s)\langle B_3(s),B_3(t)\rangle_n\,ds .
\]

The learned integral is bounded.  The unresolved part is the adaptive static
Gaussian projection.  The sharpest audited formulation is joint dynamic low
influence for paired Gaussian row/column blocks after all order-one
same-block returns are retained as causal Volterra kernels.  Equivalently,
one may prove the joint multi-row column-Jacobian estimate (28.2) in the
annealed audit.  C-14--C-16 are downstream.

The experimental reports, preregistrations, scripts, raw JSON/JSONL data, and
GPU .npz outputs are preserved in this directory.  The final first-passage
study is summarized in
[GPU_FIRST_PASSAGE_COOPERATIVE_RESULTS_2026-08-23.md](GPU_FIRST_PASSAGE_COOPERATIVE_RESULTS_2026-08-23.md).
No empirical result is assigned theorem status.

See [consolidation provenance](CONSOLIDATION_PROVENANCE_2026-08-23.md) for
the relocation record.

