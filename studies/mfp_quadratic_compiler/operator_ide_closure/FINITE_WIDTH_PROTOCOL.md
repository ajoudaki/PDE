# Preregistered finite-width boundary-layer check

Status: frozen before execution, 21 August 2026.

## Decision question

Does the full physical QQ flow show evidence of a shrinking extreme-neuron
interpolation layer, which would invalidate a regular \(O(1)\)-time continuum
interpretation, or does its signed residual-halving time stabilize with width?

This experiment can reject one mechanism.  It cannot prove an operator IDE or
compact-time convergence.

## Hypotheses

- H1 (regular physical scale): the median time at which the residual reaches
  half its initial signed value stabilizes to a nonzero constant.
- H0 (extreme-neuron collapse): that median time decreases by at least 25%
  under each of the last two width doublings.
- Any other pattern is inconclusive.

## Mechanism-preserving testbed

Use the exact one-sample, two-hidden-layer raw-square network and physical
full-MSE ODE in `PROTOCOL.md`, with \(y_\star=\eta=1\).  No layer, activation,
matrix reuse, transpose, or rank-one update is removed.  Width is the only
varied parameter.

## Frozen panel

- widths \(n=32,64,128,256\);
- six independent deterministic seeds per width;
- DOP853, `rtol=2e-9`, `atol=2e-11`, maximum step \(2.5\times10^{-4}\);
- stop at residual \(e(t)=e(0)/2\), in either direction, with hard horizon
  \(0.05\).

Pre-execution validity amendment: an initialization-only pilot found one
frozen seed with \(e(0)<0\).  The seed and target were retained; the event
direction was changed from negative-only to either direction.  No trajectory
or event time was inspected, and the pilot is not counted as evidence.

If the ratio of the width-256 and width-128 medians lies outside
\([0.8,1.2]\), the only authorized extension is \(n=512\) with four seeds.

## Numerical validity gates

1. Every solve reaches the event before the hard horizon.
2. The exact invariant \(f+e=y_\star\) has maximum sampled error below
   \(2\times10^{-6}\).
3. The sampled residual magnitude (equivalently the loss) is monotone
   nonincreasing.
4. Re-solving the first \(n=128\) seed with tolerances divided by ten changes
   the event time by less than \(0.5\%\).
5. The largest-width mean initial kernel lies within 25% of 111.

Failure of a validity gate makes the panel inconclusive.

## Interpretation

- H1 passes if both last-doubling median ratios lie in \([0.8,1.2]\) and the
  width-256 median exceeds \(10^{-3}\).
- H0 passes if both last-doubling ratios are below \(0.75\).
- Otherwise the result is inconclusive and no theorem claim changes.
