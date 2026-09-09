# Finite-width calibration experiments

This is a study record, not an established-library entry. Historical claims and
review labels below retain their original scope; consult the
[reconciled research map](../project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md)
for current qualifications and the [maintained library](../../docs/README.md)
for accepted self-contained presentations.

This branch contains the later preregistered experiments.  The authoritative
interpretation is in
[`../../CURRENT_RESEARCH_STATE.md`](../stieltjes_program_history/CURRENT_RESEARCH_STATE.md).

Chronologically:

1. `PROTOCOL.md` tests a jet control variate on saved trajectories.
2. `FRESH_PAIR_MEDIAN_PROTOCOL.md` provides a fresh initialization-only local
   calibration.
3. `POSITIVE_TIME_PROTOCOL.md` tests a stopped pair-median common-clock proxy;
   its Loewner conclusion is inconclusive because fit-degree sensitivities
   reverse the small eigenvalue sign.
4. `FRESH_ORDER13_MEDIAN_PROTOCOL.md` records a raw order-thirteen estimator
   that failed calibration.
5. `FRESH_CALIBRATED_RATIO_PROTOCOL.md` records the improved adjacent-ratio
   estimator.  It gives a useful target for (mu_5), but also fails its frozen
   strong calibration gate and is therefore inconclusive.

Generated results and frozen integrity records are grouped under
[`runs/`](runs).  Old path strings inside those records are intentionally
unaltered historical provenance.
