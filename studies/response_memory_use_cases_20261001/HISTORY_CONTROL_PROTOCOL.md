# Post-confirmation nuisance audit (exploratory)

The first five fresh n256 repair confirmations have positive q4 improvements,
but seed202 has only1% improvement rather than the10% practical screen threshold.
Thus do not call the original strong effect uniformly confirmed. Before any
new control calculation, freeze this audit of step-size selection: compare
history and current-gradient edits using the same clean-training-loss line
search over alpha in {0,0.25,0.5,1,2,4}. Their unscaled edits have matching
Frobenius norm. Select strictly by immediate corrected training loss, never by
held-out truth or loss after cleanup. Both receive the same T_clean=2 afterward.
The strongest line-searched current-gradient control could erase the benefit;
retain that outcome if it occurs. Saved confirmation checkpoints are reused
for these new interventions, so this is a post-confirmation adversarial control,
not a new independent replication or a change to the original primary metric.

Also compare unedited cleanup for2.5 time units (25% more optimization time).
This deliberately gives the baseline more work to see whether a modest increase
in ordinary cleanup obviates the memory edit. No wall-time/energy advantage is
claimed for history recording. At most5 saved checkpoints, <2 CPU-minutes.

Original numerical refinement still runs seeds201/202 atdt1/128 using fresh
training trajectories and the original repair interventions.
