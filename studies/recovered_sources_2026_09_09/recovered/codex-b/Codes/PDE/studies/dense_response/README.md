# Dense response hierarchy

This program studies finite-matrix chronological q/r response approximations.
It is a precursor and mechanism diagnostic for the operator PDE, not itself a
width-independent finite PDE.

## Phases

1. [`early_audit`](early_audit/) contains the original broad audit in a flat
   working layout. Read [`early_audit/REPORT.md`](early_audit/REPORT.md), run
   the two scripts at the phase root, and consult `results/` for the cited
   arrays and figures. Independent audit notes are under `notes/`.
2. [`long_horizon`](long_horizon/) is the corrected, self-contained extension.
   Start with [`long_horizon/REPORT.md`](long_horizon/REPORT.md) and
   [`long_horizon/REPRODUCE.md`](long_horizon/REPRODUCE.md).

Current reading: low response order can reproduce the tested finite-network
transients surprisingly well, but every surrogate in this program retains the
dense matrices and therefore does not establish finite causal compression.

