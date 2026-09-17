# Matched training-loss replot, P=n=4096

The user requests a validation scatter plot using earlier closure predictions
whose training MSE is similar to the actual network's final training MSE.
This is a postprocessing continuation of the same experiment. No training,
new scientific seeds, test-data selection, or model change is authorized here.

Keep the original scatter reference: the mean of the three actual networks'
validation outputs at T=600. Define the target loss as the arithmetic mean of
their individual training MSEs at T=600, not the MSE of their ensemble output.
For each of the three closures, choose the saved time minimizing absolute
training-loss difference from that target. Ties choose the earliest time.
Only saved predictions are used: no output interpolation or calibration.
Record the actual loss mismatch and both neighboring snapshots that bracket
the target. The training-loss target must lie in the saved loss range.

The primary comparison is validation output RMS against the same network
reference, before versus after matching. Relative RMS divides by reference
output RMS. Retain per-image exports, within-digit metrics, sign disagreements,
all nine individual network/closure pair comparisons, and bracketing-snapshot
sensitivity. As a sensitivity check, also match separately to each individual
network's final training loss; this does not couple their initializations.

Lower matched-loss RMS for all three closures, robust to both bracketing
snapshots, supports a contribution from differing training progress. Unchanged
or increased errors weaken that explanation at this endpoint. Mixed signs or
bracket-sensitive conclusions are inconclusive. No result implies a pure time
reparameterization or convergence of the learned functions.

Budget: saved-array CPU analysis and checks only, at most 10 minutes of CPU
process time and 100 MiB new generated artifacts. Stop after plotting, an
independent raw-array check, and recording the result. Existing audited runs
provide upstream evidence; this replot does not constitute new training
reproduction. Root owns MATCHED_LOSS.py, this note, README/REPORT updates and
generated matched_loss4096_001; scoped checker owns MATCHED_LOSS_CHECK.md and
generated matched_loss_check. Both are confined to this study.
