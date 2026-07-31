# Operator–Galerkin PDE program

This program contains the direct finite-cutoff PDE construction and the two
empirical extensions that use the same scientific machinery.

## Phases

1. [`core`](core/) gives the source-first operator–Galerkin construction,
   direct dense comparison, audits, processed evidence, and exact finite-cutoff
   identities. Start with
   [`core/FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT.md`](core/FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT.md).
2. [`generalization`](generalization/) applies the fixed low-order PDE to the
   preregistered transfer grid. Start with
   [`generalization/PDE_GENERALIZATION_FINAL_REPORT.md`](generalization/PDE_GENERALIZATION_FINAL_REPORT.md).
3. [`activation_controls`](activation_controls/) tests whether the agreement
   is explained by identity, deep-linear, or fixed-gain controls. Start with
   [`activation_controls/ACTIVATION_LINEARITY_SMOKING_GUN_REPORT.md`](activation_controls/ACTIVATION_LINEARITY_SMOKING_GUN_REPORT.md).
4. [`rerun_2026-07-31`](rerun_2026-07-31/) contains the later smoke and
   canonical reproductions, alongside rather than mixed into the frozen
   evidence.

Current reading: the finite-cutoff PDE has exact internal projected-gradient
and dissipation geometry, and the low-order experiments show strong but
statistically distinguishable agreement with the dense system. Identification
with the ordered dense limit and arbitrary-accuracy convergence remain open.

Each phase retains its own audited implementation. The original ZIP releases
in [`../../archive/bundles`](../../archive/bundles/) preserve byte-for-byte
provenance, including nested parent material omitted from the readable active
tree.

