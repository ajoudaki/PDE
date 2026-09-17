# Adaptive scope for one adjacent-pair endpoint claim

This note introduces a separate interpretation of the completed and continuing
campaign. It does not amend `CAMPAIGN_PLAN.md`, modify the frozen `ANALYZE.py`,
or replace any saved all-model verdict. The interpretation was specified after
the screen and common-time results showed that N1 and its controls could remain
moving while the question of interest concerned N3 versus N5. It is adaptive,
not a preregistered success under the original all-model contract.

The user requests at least one adjacent link with a settled shape difference.
For the link N3–N5, the scientifically relevant objects are the separately
evolved N3/N5 trajectories, their executed quadrature and step controls, and
the six actual-network reference/control trajectories. N1 is a different
trajectory: its current prediction, remaining drift and numerical error do
not enter either member of this pair or the network reference. Requiring N1
also to settle answers the stronger question whether all displayed models
have settled. It is not necessary for the narrower pair claim.

This restriction is legitimate provided all compared and reference trajectories
retain their original checks. `FOCUSED.py` therefore first invokes the unchanged
frozen analysis on the complete manifest with pair N3–N5. It preserves that
analysis's verdict and raw numerical evidence, then recomputes only the
aggregation needed for the narrower claim:

- Settling and remaining-100-unit-drift uncertainty use N3 and N5 at every
  executed main/fine/finest/half-step configuration, plus all six network
  reference/control trajectories. N1 configurations are listed as excluded
  from this aggregation, with their actual times and settling diagnostics.
- The same two 25-unit plateau windows, loss-change bounds, 100-unit drift
  bound, main and finest-resolution shape thresholds, previous-100-unit
  persistence, quadrature/step/precision bounds, loss-control bounds, width
  discrepancy, seed spread and five-times uncertainty margins remain in force.
- The original minimum-common-time rule and time cap remain in force. The
  relevant trajectories must share that time. The complete original saved-data
  correctness report remains required, including equation, initialization,
  source/hash and checkpoint replay checks; it is not weakened to excuse a
  failure in an excluded N1 job.
- Equally good training fit is a separate stronger claim, using the same
  frozen MSE and pairwise training-output bounds. Visible shape differences
  alone do not establish that claim or superiority against the network.

This is a change in the logical scope of the claim, not permission to remove
a difficult member of the compared pair, omit a control that changes its
answer, alter a threshold, choose a new angular gap, or stop checking numerical
uncertainty. All executed evidence and all-model results remain available.
The implementation also reports the remaining failure reasons explicitly.

A focused pass should be described as an **adaptive N3–N5 separation at a common
finite time, satisfying the stated settling diagnostics and numerical margins**.
It is not an established infinite-time limit, a pass under the original
all-model contract, proof that higher order is more accurate, or a convergence
theorem for the hierarchy. Any displayed N1 curve retains its own finite time
and moving/settled label. Future independent confirmation with this pair scope
fixed in advance would have stronger evidential status.
