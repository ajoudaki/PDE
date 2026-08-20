# Fixed-P PDE generalization study

This report was generated from the preregistered metadata-selected analysis. No filename-based case selection or post-hoc reference-tier selection is used.

The width-independent closure is fixed at the complete degree-one Hermite basis P=5 before all references. The matrix changes labels, input geometry, m=2 through 5, and two smooth bounded slope-matched activation alternatives, including two interaction cases.

Only B0 and the exact-radius Y1 perturbation directly test the current narrow tanh conjecture. Every other case is extension evidence. This study does not prove the ordered width/depth limit, P-to-infinity convergence, or arbitrary-accuracy closure. In particular, the prior non-monotone P=5,15,35 observation is not revised by this fixed-P study.

- Bootstrap: B=2000, seed=2026072301, joint one-sided 95% bounds.
- Test override: `False`.
- Numerical gates: `False`.
- Broad verdict: **boundary_or_unresolved**.

| case | tier | active Gram | Gram UCB | output UCB | loss UCB | verdict |
|---|---|---:|---:|---:|---:|---|
| B0 | screening | True | 0.07747 | 0.072787 | 0.063313 | boundary_or_unresolved |
| Y1 | confirmation | True | 0.072042 | 0.074057 | 0.073452 | boundary_or_unresolved |
| Y2 | screening | True | 0.074961 | 0.072723 | 0.068918 | boundary_or_unresolved |
| Y3 | confirmation | True | 0.071809 | 0.074068 | 0.068932 | boundary_or_unresolved |
| Y4 | confirmation | True | 0.068936 | 0.066837 | 0.066361 | boundary_or_unresolved |
| X1 | screening | True | 0.084046 | 0.074657 | 0.065019 | boundary_or_unresolved |
| X2 | confirmation | True | 0.084891 | 0.075327 | 0.064008 | boundary_or_unresolved |
| M2 | screening | True | 0.075601 | 0.071155 | 0.063996 | boundary_or_unresolved |
| M4 | screening | True | 0.10085 | 0.074487 | 0.064852 | boundary_or_unresolved |
| M5 | confirmation | True | 0.090478 | 0.077735 | 0.079107 | boundary_or_unresolved |
| A1 | confirmation | True | 0.072767 | 0.073979 | 0.073175 | boundary_or_unresolved |
| A2 | screening | True | 0.07464 | 0.072519 | 0.062498 | boundary_or_unresolved |
| I1 | confirmation | True | 0.080382 | 0.069813 | 0.063791 | boundary_or_unresolved |
| I2 | confirmation | True | 0.083804 | 0.07625 | 0.079023 | boundary_or_unresolved |

The joint critical values take a single maximum over all 14 cases and all three normalized primary metrics. Inactive Gram cases are judged only on output and loss and do not count as Gram-transfer evidence. PDE and dense trajectories must independently pass both frozen plateau windows (8–16 and 16–32).

A failed numerical gate or a common plateau failure is reported as unresolved rather than averaged away. A joint lower bound above 0.10, an active feature-motion ratio outside [0.5,2], or a plateau pass/fail mismatch is a material counterexample under the frozen rule.
