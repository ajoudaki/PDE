# Source map and provenance

Conversation summaries are locators only. The following maintained files
are the technical sources used to freeze the probe.

## Mean-field peeling machinery

- [`../mean_field_peeling/CURRENT_RESEARCH_STATE.md`](../mean_field_peeling/CURRENT_RESEARCH_STATE.md):
  conditional Gaussian law, Wick--Stein elimination, equality partitions,
  width grading, source replacement, and the exact boundary of the local-jet
  program.
- [`../mean_field_peeling/MUP_TRAINING_CASE_STUDY.md`](../mean_field_peeling/MUP_TRAINING_CASE_STUDY.md):
  explicit multi-step and multi-channel execution.

## Rigorous fixed-program backend

- Greg Yang, [*Tensor Programs III: Neural Matrix Laws*](https://arxiv.org/pdf/2009.10685),
  especially Setup E.2 and Theorem E.15. The exact applicability and strict
  fixed-program boundary are recorded in
  [`audits/TENSOR_PROGRAM_FIXED_MESH_AUDIT.md`](audits/TENSOR_PROGRAM_FIXED_MESH_AUDIT.md).

This source is used only after exact rank-update elimination at a fixed
finite Euler mesh. It is not cited for growing-mesh or continuous-time
uniformity.

## Resolved validation models

- Linear (H=1):
  [`../mean_field_peeling/identity_compiler/linear_gaussian_program/DEPTH1_IDENTITY_DERIVATION.md`](../mean_field_peeling/identity_compiler/linear_gaussian_program/DEPTH1_IDENTITY_DERIVATION.md).
- Linear (H=2):
  [`../mean_field_peeling/identity_compiler/linear_gaussian_program/depth2_autonomous_mse_closure/THEOREM_AND_PROOF.md`](../mean_field_peeling/identity_compiler/linear_gaussian_program/depth2_autonomous_mse_closure/THEOREM_AND_PROOF.md).
- Linear (H=3):
  [`../mean_field_peeling/identity_compiler/linear_gaussian_program/depth3_unfrozen_readout_closure/THEOREM_AND_PROOF.md`](../mean_field_peeling/identity_compiler/linear_gaussian_program/depth3_unfrozen_readout_closure/THEOREM_AND_PROOF.md).
- Arctangent (H=2):
  [`../mean_field_peeling/nonlinear_activation_operator_ide/ARCTAN_THEOREM_AND_PROOF.md`](../mean_field_peeling/nonlinear_activation_operator_ide/ARCTAN_THEOREM_AND_PROOF.md).

The old proofs are used to freeze models and regression readouts. Their
model-specific solution devices are not premises of the new calculus.

## Unresolved target and hostile regression suite

- [`../d3_arctan_closure_program/FROZEN_CORE_CONTRACT_2026-08-23.md`](../d3_arctan_closure_program/FROZEN_CORE_CONTRACT_2026-08-23.md).
- [`../d3_arctan_closure_program/CORE_EVIDENCE_LEDGER_2026-08-23.md`](../d3_arctan_closure_program/CORE_EVIDENCE_LEDGER_2026-08-23.md).
- [`../d3_arctan_closure_program/annealed_audit_and_signed_abel.md`](../d3_arctan_closure_program/annealed_audit_and_signed_abel.md),
  especially Sections 25--28.
- [`../d3_arctan_closure_program/MULTICAVITY_HOSTILE_AUDIT_2026-08-23.md`](../d3_arctan_closure_program/MULTICAVITY_HOSTILE_AUDIT_2026-08-23.md).

No file in the paused study is modified by this program.
