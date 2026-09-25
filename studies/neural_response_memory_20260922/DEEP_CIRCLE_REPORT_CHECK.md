# Bounded final-report consistency check

Checker: scoped agent `/root/deep_report_check`, 2026-09-25. Verdict: PASS
after one wording correction, applied by the supervisor and reread by the
checker. This is an author-side consistency check, not a complete independent
audit or promotion review. No training or saved-state replay was performed.

Checked report: `DEEP_CIRCLE_RESULTS.md`, SHA256
`b3d3e172a11a69d41a19b1cccf0600e0fb946fc2c1c34e5a4004ff9b054bd92f`.
This version explicitly left the replay and bitwise checks pending; the
supervisor's later completion text is supported separately by
`DEEP_CIRCLE_CHECK.md` and its evidence.

The sole correction was to change "each learned matrix" to "each learned
matrix increment" in the state-size section's rank statement. The full
matrix includes its dense initial value and does not have the MP rank bound.
No mathematical or numerical discrepancy remained in the checked scope.

Complete scientific read coverage: the report, `DEEP_CIRCLE_DERIVATION.md`,
`DEEP_CIRCLE_PROTOCOL.md`, `deep_circle_cases.json`,
`run_deep_circle_campaign.py`, and generated `deep_circle_analysis01/summary.md`.
The complete `metrics_summary.json` and `run_inventory.csv` were parsed;
every comparison, order-comparison and inventory row was checked
programmatically. Required process instructions and solve-math-rigorously
were read. No other study inputs were accessed and the checker edited no files.

Verified components:

- Gradient-flow scaling, moment transport, reconstruction, transpose use,
  defect sign/rank, initialization, and rational/direct-coordinate distinction.
- All 15 endpoint RMS values, winning orders, nonmonotonic conclusions,
  and both reported P3-minus-P2 gaps.
- All 75 comparison gates and 75 order-comparison calculations, including
  all 15 resolved endpoint comparisons.
- All 40 inventory rows, moving-state formulas, fixed storage, history ranks,
  measured memory and every runtime-table entry.
- Campaign command options and repeat-selection constraints against the
  launcher; the analysis command against its recorded invocation.

The largest recorded individual refinement change is
0.00018120651171193172, and the largest nested-grid change is
1.384309333829492e-15, consistent with the report's stated bounds.

Raw checkpoints, implementation-test/rescoring logs, pilot/repetition receipts,
repetition selections and pilot configuration files were outside this scope.
This check therefore does not independently verify the nine-test claim,
CPU-rescoring difference, original-file hash validation, aggregate timing,
Torch version, or byte-identical pilot-input statement. Those are checked
by the supervisor and the implementation audit. Pending replay/repetition
checks were intentionally excluded from this bounded assignment.
