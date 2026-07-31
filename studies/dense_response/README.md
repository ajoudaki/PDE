# Dense response hierarchy

This program studies chronological q/r response truncations while retaining
the finite dense weight matrices. It is a precursor and diagnostic for the
width-free operator PDE, not itself such a PDE.

## Phases

1. [`early_audit`](early_audit/) contains the original audit layout: source
   scripts, final arrays and figures, agent audits, and the deliverable report.
   Start with
   [`early_audit/deliverables/dense_euclidean_continuous_depth_npde_audit.md`](early_audit/deliverables/dense_euclidean_continuous_depth_npde_audit.md).
2. [`long_horizon`](long_horizon/) contains the corrected and extended
   long-horizon release. Start with [`long_horizon/REPORT.md`](long_horizon/REPORT.md)
   and use [`long_horizon/REPRODUCE.md`](long_horizon/REPRODUCE.md) for its
   original reproduction instructions.

Current reading: the response hierarchy is a useful causal diagnostic and can
become exact at sufficient grade for a fixed finite discretization. Because it
retains every dense matrix, it does not establish width-independent finite
causal compression.

