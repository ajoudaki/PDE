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

Fresh results route to repository `data/generated/stieltjes_finite_width/runs/`;
retained arrays and integrity records are under
`data/historical/studies/stieltjes_finite_width/runs/`. Old paths in immutable
records are intentionally unchanged.

The five Python entry points accept `--output-dir` under this study's generated
tree or external scratch; existing symlinks and hardlinked children are
rejected before work. `jet_control_variate.py` reads the generated direct-Loewner
corrected-clock run by default. `run_positive_time_pair_median.py` reads the
generated fresh-pair run. Both accept `--input-dir`, or explicit `--historical`
to select retained inputs and a separate generated `historical_review/` output.
They do not fall back to history when fresh input is missing. These interfaces
preserve the scientific calculations and resource requirements; migration alone
does not establish full campaign reproducibility.
