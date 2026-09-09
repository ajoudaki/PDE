# Global Stieltjes proxy campaign: terminal results

Status: **closed inconclusive for the canonical finite-width bridge**.  The
exact no-width calibration passed strongly.  The canonical neural pilot
completed its hash-bound trajectories, but its uncertainty was far too large
for the registered Stieltjes brackets and it failed two frozen numerical
gates.  The hard stop
therefore prevented every deformation and multi-input neural branch.

## Exact calibration

At the exactly solvable Lambert-$W$ variance boundary, all 501 points on
$0\le y\le .99$ lay on the prescribed side of every rational convergent and
inside every nested Gauss/Radau bracket.  As accepted moments were added one
at a time, the sup log-kernel errors were

$$
1.43433\times10^{-1},\quad
7.87107\times10^{-3},\quad
5.51285\times10^{-4},\quad
3.39336\times10^{-5},\quad
2.27548\times10^{-6},\quad
1.43289\times10^{-7}.
$$

The last error was about sixty times smaller than the equal-information
five-moment Taylor error.  This is a non-circular demonstration that the
chosen rational hierarchy converges globally and rapidly in a model where
the Stieltjes representation is known exactly.  It is not evidence for the
separate canonical finite-width/global-trajectory bridge.

## Fail-closed pilot chronology

The original Stage-2 configuration used a physical horizon $0.012$.  Exact
pre-existing proxies imply $T(.99)\ge0.01493948\ldots$, so that horizon could
not reach its own final output node.  It stopped after 7.623 seconds without
writing an NPZ and remains null evidence.  Successor 01 was never run: a
hostile pre-execution audit found underspecified analysis and an untestable
single-width output-clock gate.

Successor 02 repaired those issues before execution, bound every source,
protocol, configuration, analysis rule, and validation record by hash, and
restored the original small raw-data caps.  CPU and both-GPU validation-v3
runs passed.  The one authorized scientific attempt then completed all five
points in 59.934 seconds.  Peak PyTorch GPU allocation was 0.133 GiB and peak
host RSS was 0.951 GiB, far below the 8-GiB point caps.  All 18,360 registered
batch-integrator steps completed.  Direct gates for finite positive kernels,
antithetic cancellation, monotone mean output, nonincreasing mean loss, and
output-clock identity passed.

## Frozen analysis outcome

Every one of the 2,000 registered bootstrap resamples was valid at every
point.  The ordinary and output-clock sensitivity-union intervals overlapped
at every node.  The maximum rank-one conditioning projection decreased from

$$
0.158869\quad(n=256)
\qquad\hbox{to}\qquad
0.0838078\quad(n=512),
$$

with scaled rate ratio $0.7460$.  None of the registered Jensen-gap,
self-averaging, or ordinary-versus-clock trend tests showed a statistically
resolved worsening.  This is only a fail-closed validity result: the central
self-averaging statistic itself rose from $0.06453$ to $0.09746$, but its 99%
difference interval $[-0.02436,0.08059]$ included zero.

Two mandatory gates nevertheless failed.

1. At $y=.9$, the full 99% ordinary width-sensitivity log-band width was
   $1.04499147$, while the maximum registered width was $0.0126402630$.
   The reference uncertainty was therefore $82.67$ times the pilot's
   resolution threshold.
2. The paired four-lineage full-step and half-step initial arrays were not
   bitwise identical.  This was only a batching-level floating discrepancy:
   the maximum initial-output difference was $5.55\times10^{-17}$ and the
   maximum initial-kernel difference was $5.68\times10^{-14}$.  The actual
   step-halving kernel discrepancy was tiny—at most
   $2.554\times10^{-6}$ through $y=.95$ and $3.80\times10^{-8}$ at $.99$—but
   the frozen rule required exact bitwise equality and cannot be weakened
   after execution.

Consequently all five rational prefixes are **inconclusive**, none is a valid
contrary result, and the larger-width Stage-3 branch is not authorized.  The
later one-input, two-input, and three-input neural simulations are closed
without execution.

There is a second preregistered limitation: at $y=0$ every rational proxy is
exactly $K(0)=111$, whereas a nondegenerate finite-width confidence band has
positive width.  Literal containment of the whole band in the degenerate
point bracket is therefore impossible.  This was detected before offline
interpretation but after the contract had been frozen, so it was not repaired.
It reinforces the inconclusive classification and must be corrected only in
a separately designed future experiment.  The defect is not hiding a positive
or negative conclusion: repeating the frozen containment and escape checks on
positive nodes only still gives neither a contained prefix nor a replicated
definite escape.

## What the central curves suggest, without certifying

At width 512 and $y=.9$, the ordinary central estimate was $147.688$ with a
simultaneous 99% interval $[126.252,172.764]$.  The successive rational
kernels were

$$
111, 166.393, 162.239, 163.060, 162.987, 163.000.
$$

Thus the first feature-learning correction was materially closer than NTK,
and all non-NTK levels lay inside that pointwise simultaneous interval.  The
additional moment corrections were much smaller than finite-width and Monte
Carlo uncertainty; their central errors did not improve monotonically.  This
is descriptive only.  The two-width sensitivity union at the same node was
$[121.011,344.081]$, so it cannot distinguish any nontrivial Stieltjes level.

The correct conclusion is not that the hierarchy failed.  It is that this
finite-width design cannot resolve its incremental corrections at acceptable
cost.  A future global-curve test would need materially more large-width
replication and a baseline-calibration rule at $y=0$; neither is authorized
by this closed campaign.

## Durable artifacts

- [`PROTOCOL.md`](PROTOCOL.md) is the original frozen suite.
- [`SUCCESSOR_02_PROTOCOL.md`](SUCCESSOR_02_PROTOCOL.md) is the executed
  successor contract.
- [`boundary_result.json`](boundary_result.json) is the exact calibration.
- [`summary.json`](reference/runs/canonical_pilot_successor02_20260813/summary.json)
  and [`manifest.json`](reference/runs/canonical_pilot_successor02_20260813/manifest.json)
  are the producer certificate and raw-array hash manifest.
- [`analysis_result.json`](reference/runs/canonical_pilot_successor02_20260813/analysis_result.json)
  is the frozen 2,000-resample analysis.
- [`analysis_manifest.json`](reference/runs/canonical_pilot_successor02_20260813/analysis_manifest.json)
  binds the compact results to the producer and unlock.

Raw NPZ trajectories remain local and Git-ignored; their sizes and SHA-256
hashes are preserved in the tracked producer manifest.
